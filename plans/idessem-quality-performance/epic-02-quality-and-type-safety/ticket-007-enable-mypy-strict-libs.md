# ticket-007 Enable mypy strict mode for libs module

## Context

### Background

The `idessem/libs/` module contains 1 handler file (`usinas_hidreletricas.py`) and a `modelos/` subdirectory with Register definitions. Under mypy strict mode from ticket-004's configuration, this module will also report type annotation errors. The libs module is much smaller than dessem (~2 files) but follows the same cfinterface patterns and needs the same annotation treatment.

### Relation to Epic

This ticket handles the libs module in parallel with (or after) ticket-006 for dessem. Together they cover all production code in idessem.

### Current State

- `/home/rogerio/git/idessem/idessem/libs/usinas_hidreletricas.py` -- RegisterFile subclass with 8 accessor methods, 1 bare `# type: ignore` on pandas import
- `/home/rogerio/git/idessem/idessem/libs/modelos/usinas_hidreletricas.py` -- Register definitions for 8 register types
- `/home/rogerio/git/idessem/idessem/libs/__init__.py` -- 1 eager import (not converting to lazy)
- `/home/rogerio/git/idessem/idessem/libs/modelos/__init__.py` -- empty

## Specification

### Requirements

1. Add type annotations to all functions and methods in the libs module that lack them
2. Apply the same cfinterface annotation patterns as ticket-006: `IO[Any]`, `# type: ignore[override]`, `Optional[Any]`, `ClassVar[...]`
3. Replace the bare `# type: ignore` on `import pandas as pd` with `# type: ignore[import-untyped]`
4. After all fixes, `mypy idessem/libs/` must pass under the strict configuration
5. All 558 tests must still pass

### Inputs/Props

- All Python files in `idessem/libs/` and `idessem/libs/modelos/`

### Outputs/Behavior

- `mypy idessem/libs/` reports zero errors under strict mode configuration from ticket-004
- All existing tests pass unchanged

### Error Handling

Not applicable -- this is a type annotation change with no runtime impact.

## Acceptance Criteria

- [ ] Given the command `mypy idessem/libs/`, when executed with the strict config from ticket-004, then zero errors are reported
- [ ] Given the command `grep -r '# type: ignore$' idessem/libs/`, when executed, then zero bare type-ignore comments are found
- [ ] Given the command `pytest tests/libs/ -v`, when executed, then all libs tests pass
- [ ] Given the command `pytest -x -q`, when executed, then all 558 tests pass

## Implementation Guide

### Suggested Approach

Run `mypy idessem/libs/` to see the error list, then fix each error using the same patterns from ticket-006.

The libs module is small (2 source files), so this should be a quick pass:

1. **`usinas_hidreletricas.py`**: Add `-> None` to `__init__`, type the `__registros_ou_df` private method, add return annotations to all 8 accessor methods, replace bare `# type: ignore` on pandas import
2. **`modelos/usinas_hidreletricas.py`**: Add annotations to Register subclass `__init__` methods, `read()`/`write()` overrides

**Key pattern for `__registros_ou_df`**:

```python
def __registros_ou_df(
    self, t: Type[T], **kwargs: Any
) -> Optional[Union[T, List[T], pd.DataFrame]]:
```

### Key Files to Modify

- `/home/rogerio/git/idessem/idessem/libs/usinas_hidreletricas.py`
- `/home/rogerio/git/idessem/idessem/libs/modelos/usinas_hidreletricas.py`

### Patterns to Follow

- Same annotation patterns as ticket-006 and idecomp's libs module
- Reference: `/home/rogerio/git/idecomp/idecomp/libs/restricoes.py` for RegisterFile handler annotations
- `IO[Any]` on all read/write, `Optional[Any]` for init params, `ClassVar` for class attributes

### Pitfalls to Avoid

- Do NOT convert `idessem/libs/__init__.py` to lazy imports -- it has only 1 import, overhead is negligible
- Do NOT change test files
- Do NOT change runtime behavior

## Testing Requirements

### Unit Tests

No new tests. All existing tests must pass.

### Integration Tests

- `mypy idessem/libs/` passes with zero errors

### E2E Tests

Not applicable.

## Dependencies

- **Blocked By**: ticket-004-add-mypy-strict-config.md
- **Blocks**: ticket-008-replace-bare-type-ignores.md

## Effort Estimate

**Points**: 2
**Confidence**: High (small module, patterns established)

## Out of Scope

- Fixing type errors in `idessem/dessem/` (ticket-006)
- Converting `idessem/libs/__init__.py` to lazy imports
- Adding tests for libs module
