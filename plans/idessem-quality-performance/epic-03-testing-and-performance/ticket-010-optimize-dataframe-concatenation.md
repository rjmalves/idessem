# ticket-010 Optimize DataFrame concatenation in pdo_operacao

## Context

### Background

The `PdoOperacao.__concatena_blocos()` method in `pdo_operacao.py` uses an O(n^2) pattern: it calls `pd.concat([df, df_estagio])` inside a loop, growing the DataFrame one block at a time. Each concat copies the entire accumulated DataFrame, making the cost quadratic in the number of blocks. The standard fix is the collect-then-concat pattern: accumulate DataFrames in a list, then call `pd.concat` once outside the loop.

This is the only O(n^2) concat in the codebase. The other two `pd.concat` calls (`avl_fpha2.py` line 54, `avl_fpha3.py` line 55) already use the correct pattern -- they collect into a list via list comprehension and call `pd.concat` once.

### Relation to Epic

Epic 03 targets performance and testing improvements. This ticket addresses the single identified performance anti-pattern in the codebase, eliminating the O(n^2) DataFrame growth before the benchmark suite (ticket-012) establishes the performance baseline.

### Current State

File `/home/rogerio/git/idessem/idessem/dessem/pdo_operacao.py`, method `__concatena_blocos` (lines 38-57):

```python
def __concatena_blocos(self, bloco: Type[T]) -> Optional[pd.DataFrame]:
    df = None
    for i, b in enumerate(self.data.of_type(bloco)):
        if not isinstance(b, Block):
            continue
        df_estagio = b.data
        if df is None:
            df = df_estagio
        else:
            df = pd.concat([df, df_estagio], ignore_index=True)
    if df is not None:
        return df
    return None
```

The method is called by `custos_operacao` (line 117) with `BlocoCustos`. All 558 tests pass. mypy strict passes on all 108 files with 0 errors. ruff is clean.

## Specification

### Requirements

1. Replace the loop-concat pattern with collect-then-concat: gather all valid block DataFrames into a `list[pd.DataFrame]`, then call `pd.concat(frames, ignore_index=True)` once.
2. Keep the inline implementation (do not extract a shared helper). Each handler has slightly different concatenation logic, and the `avl_fpha2.py`/`avl_fpha3.py` files already use their own inline collect-then-concat.
3. Preserve the method's public contract: return `Optional[pd.DataFrame]`, return `None` when no valid blocks exist.
4. Preserve the `isinstance(b, Block)` guard.
5. The method must continue to pass mypy strict mode with no new errors.

### Inputs/Props

- `bloco: Type[T]` -- the block type to search for via `self.data.of_type(bloco)`.

### Outputs/Behavior

- Returns a single concatenated `pd.DataFrame` with `ignore_index=True` when one or more valid blocks exist.
- Returns `None` when no valid blocks exist (same as current behavior).

### Error Handling

No change to error handling. The method does not raise exceptions; it returns `None` for the empty case.

## Acceptance Criteria

- [ ] Given the file `/home/rogerio/git/idessem/idessem/dessem/pdo_operacao.py`, when inspecting the `__concatena_blocos` method, then there is exactly one call to `pd.concat` and it is outside any loop.
- [ ] Given the file `/home/rogerio/git/idessem/idessem/dessem/pdo_operacao.py`, when inspecting the `__concatena_blocos` method, then there is a `list` variable that accumulates DataFrames from the loop before `pd.concat` is called.
- [ ] Given the refactored method, when running `uv run pytest tests/dessem/test_pdo_operacao.py -v`, then all 12 tests in that file pass with 0 failures.
- [ ] Given the refactored method, when running `uv run mypy idessem/dessem/pdo_operacao.py --strict --warn-return-any=false`, then mypy reports 0 errors.
- [ ] Given the refactored method, when running `uv run ruff check idessem/dessem/pdo_operacao.py`, then ruff reports 0 violations.

## Implementation Guide

### Suggested Approach

1. Open `/home/rogerio/git/idessem/idessem/dessem/pdo_operacao.py`.
2. Replace the `__concatena_blocos` method body with the collect-then-concat pattern. The new method should look like:

```python
def __concatena_blocos(self, bloco: Type[T]) -> Optional[pd.DataFrame]:
    """
    Adiciona uma coluna com o estagio de cada bloco.
    :param bloco: O tipo de bloco
    :type bloco: Type[T]
    :return: O DataFrame com os estagios
    :rtype: pd.DataFrame
    """
    frames: list[pd.DataFrame] = []
    for b in self.data.of_type(bloco):
        if not isinstance(b, Block):
            continue
        df_estagio = b.data
        if isinstance(df_estagio, pd.DataFrame):
            frames.append(df_estagio)
    if frames:
        return pd.concat(frames, ignore_index=True)
    return None
```

3. Note the removal of the unused `i` variable from `enumerate()` (it was unused in the original). Also note the addition of an `isinstance(df_estagio, pd.DataFrame)` guard for type safety -- `b.data` can return non-DataFrame types in the general `Block` interface.
4. Run the test suite, mypy, and ruff to validate.

### Key Files to Modify

- `/home/rogerio/git/idessem/idessem/dessem/pdo_operacao.py` -- the `__concatena_blocos` method (lines 38-57)

### Patterns to Follow

Follow the same collect-then-concat pattern already used in `avl_fpha2.py` (lines 46-57) and `avl_fpha3.py` (lines 46-58). Those files collect into a list comprehension then call `pd.concat` once.

### Pitfalls to Avoid

- Do not modify `avl_fpha2.py` or `avl_fpha3.py` -- they already use the correct pattern.
- Do not remove the `ignore_index=True` parameter from `pd.concat` -- it is required to reset the index after concatenation.
- Do not change the method signature or return type. The method is called from `custos_operacao` which caches the result.
- Do not remove the `isinstance(b, Block)` guard -- it filters out non-Block items returned by `of_type()`.

## Testing Requirements

### Unit Tests

No new tests needed. The existing 12 tests in `tests/dessem/test_pdo_operacao.py` already cover:

- `test_atributos_encontrados_pdo_operacao`: verifies `custos_operacao is not None` (exercises the concat path)
- `test_atributos_naoencontrados_pdo_operacao`: verifies `custos_operacao is None` (exercises the empty path)

### Integration Tests

Not applicable. The refactor is internal to one method.

### E2E Tests

Not applicable.

## Dependencies

- **Blocked By**: ticket-006-enable-mypy-strict-dessem.md (completed -- type annotations are in place)
- **Blocks**: ticket-012-create-benchmark-suite.md

## Effort Estimate

**Points**: 1
**Confidence**: High
