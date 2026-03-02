# ticket-003 Migrate set_version calls and verify test suite

## Context

### Background

cfinterface v1.9.0 deprecated the `set_version()` class method in favor of passing `version=` to `read()`. idessem has 5 test files with 38 `set_version()` call sites that emit `DeprecationWarning`. These must be migrated to the `read(content, version="...")` pattern. Additionally, after all Epic 01 changes, the full test suite must be verified to pass with zero failures and zero deprecation warnings from STORAGE strings or `set_version()`.

### Relation to Epic

This is the final ticket in Epic 01, completing the foundation by ensuring all 558 tests pass with zero failures and zero deprecation warnings from cfinterface APIs.

### Current State

- 5 test files use `set_version()` with 38 call sites total:
  1. `/home/rogerio/git/idessem/tests/dessem/test_avl_desvfpha.py` -- 6 calls (`AvlDesvFpha.set_version("19.3")`)
  2. `/home/rogerio/git/idessem/tests/dessem/test_avl_fpha1.py` -- 6 calls (`AvlFpha1.set_version("19.3")` and `AvlFpha1.set_version("193")`)
  3. `/home/rogerio/git/idessem/tests/dessem/test_pdo_aval_qmaxusih.py` -- 6 calls (`PdoAvalQmaxUsih.set_version("20.1")`)
  4. `/home/rogerio/git/idessem/tests/dessem/test_pdo_eco_fcfcortes.py` -- 6 calls (`PdoEcoFcfCortes.set_version("19.4.1")`)
  5. `/home/rogerio/git/idessem/tests/dessem/test_pdo_eco_usih.py` -- 14 calls (`PdoEcoUsih.set_version("19.4.2")` and `PdoEcoUsih.set_version("19.3.1")`)
- Running `pytest` shows: 558 passed, 46 warnings (38 from set_version, 1 from STORAGE, 7 other)
- Running `pytest -W error::DeprecationWarning` shows: 41 failures (from set_version and STORAGE deprecation warnings)
- Documentation file `docs/source/geral/tutorial.rst` also references `set_version` on lines 58-59 and 97

## Specification

### Requirements

1. In all 5 test files, replace `Handler.set_version("X.Y"); handler = Handler.read(path)` with `handler = Handler.read(path, version="X.Y")`
2. The pattern in these test files is:
   - A `set_version()` call BEFORE the `mock_open` context or inside it
   - Followed by `Handler.read(ARQ_TESTE)` inside the `with patch(...)` block
   - Replace with: remove `set_version()` line, add `version="X.Y"` parameter to `Handler.read(ARQ_TESTE, version="X.Y")`
3. Update `docs/source/geral/tutorial.rst` to remove `set_version` references and show the `version=` parameter pattern instead
4. After all fixes, the full test suite must pass with zero failures
5. After all fixes, running `pytest -W error::DeprecationWarning` must not raise errors from `set_version()` calls

### Inputs/Props

- 5 test files + 1 docs file listed in Current State section

### Outputs/Behavior

- All 558 tests pass
- No DeprecationWarning from `set_version()` calls
- No DeprecationWarning from STORAGE strings (fixed in ticket-002)
- Documentation shows current API

### Error Handling

Not applicable -- all changes are in test files and documentation.

## Acceptance Criteria

- [ ] Given the command `grep -r "set_version" tests/ --include="*.py"`, when executed, then zero matches are found
- [ ] Given the command `grep -r "set_version" docs/`, when executed, then zero matches are found
- [ ] Given the command `pytest -v`, when executed, then 558 tests pass and 0 tests fail
- [ ] Given the command `pytest -W error::DeprecationWarning tests/dessem/test_avl_fpha1.py tests/dessem/test_avl_desvfpha.py tests/dessem/test_pdo_eco_usih.py tests/dessem/test_pdo_eco_fcfcortes.py tests/dessem/test_pdo_aval_qmaxusih.py -v`, when executed, then all tests pass with zero DeprecationWarning errors
- [ ] Given `tests/dessem/test_avl_fpha1.py`, when opened, then versioned tests use `AvlFpha1.read(ARQ_TESTE, version="19.3")` instead of `AvlFpha1.set_version("19.3"); ... AvlFpha1.read(ARQ_TESTE)`

## Implementation Guide

### Suggested Approach

**Step 1: Migrate set_version() in each test file**

Each test file follows a pattern like:

```python
def test_something_v190300():
    m: MagicMock = mock_open(read_data="".join(MockData))
    with patch("builtins.open", m):
        Handler.set_version("19.3")
        log = Handler.read(ARQ_TESTE)
        assert log.something is not None
```

Replace with:

```python
def test_something_v190300():
    m: MagicMock = mock_open(read_data="".join(MockData))
    with patch("builtins.open", m):
        log = Handler.read(ARQ_TESTE, version="19.3")
        assert log.something is not None
```

Simply: (a) remove the `Handler.set_version("X.Y")` line, (b) add `version="X.Y"` as a keyword argument to the `Handler.read()` call.

**Special case in `test_avl_fpha1.py`**: Line 111 uses `AvlFpha1.set_version("193")` (typo: `"193"` instead of `"19.3"`). This is an existing test that passes, so preserve the exact version string: `AvlFpha1.read(ARQ_TESTE, version="193")`.

**Step 2: Update documentation**

In `docs/source/geral/tutorial.rst`, replace the `set_version` usage example with the new `version=` parameter pattern. The current lines 58-59 explain `set_version` and line 97 shows `AvlFpha1.set_version("19.3")`. Replace with `AvlFpha1.read(path, version="19.3")` style.

**Step 3: Verify full suite**

Run `pytest -v` and `pytest -W error::DeprecationWarning` to confirm zero failures and zero deprecation warnings from STORAGE or set_version.

### Key Files to Modify

1. `/home/rogerio/git/idessem/tests/dessem/test_avl_desvfpha.py` -- 6 set_version removals
2. `/home/rogerio/git/idessem/tests/dessem/test_avl_fpha1.py` -- 6 set_version removals
3. `/home/rogerio/git/idessem/tests/dessem/test_pdo_aval_qmaxusih.py` -- 6 set_version removals
4. `/home/rogerio/git/idessem/tests/dessem/test_pdo_eco_fcfcortes.py` -- 6 set_version removals
5. `/home/rogerio/git/idessem/tests/dessem/test_pdo_eco_usih.py` -- 14 set_version removals
6. `/home/rogerio/git/idessem/docs/source/geral/tutorial.rst` -- documentation update

### Patterns to Follow

- **read(version=...) convention**: `Handler.read(path, version="19.3")` instead of deprecated `Handler.set_version("19.3"); Handler.read(path)`.
- Reference: idecomp test files `tests/decomp/test_dec_oper_usih.py` for the version read pattern after migration.

### Pitfalls to Avoid

- Do NOT change the test assertions, only the setup code (how handlers are read)
- Do NOT change handler code -- all changes are in test files and docs only
- Do NOT "fix" the `"193"` version string in `test_eq_avl_fpha1_v190300` -- it is intentional and the test passes with it
- Do NOT change mock data or mock file paths

## Testing Requirements

### Unit Tests

The tests themselves are being fixed. Verification is done by running the full suite.

### Integration Tests

- `pytest -v` -- all 558 tests pass
- `pytest -W error::DeprecationWarning` on the 5 affected test files -- no deprecation warnings

### E2E Tests

Not applicable.

## Dependencies

- **Blocked By**: ticket-001-bump-cfinterface-dependency.md, ticket-002-migrate-storage-literal.md
- **Blocks**: All tickets in epic-02 and beyond

## Effort Estimate

**Points**: 2
**Confidence**: High

## Out of Scope

- Fixing mypy errors (epic-02)
- Adding new tests (epic-03)
- Changes to production code (only test and docs files are modified)
- Fixing the `"193"` version string in test_eq_avl_fpha1_v190300 (existing behavior, not a bug)
