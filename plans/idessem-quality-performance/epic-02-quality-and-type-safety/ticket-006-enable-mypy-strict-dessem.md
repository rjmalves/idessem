# ticket-006 Enable mypy strict mode for dessem handlers and models

## Context

### Background

With the mypy strict configuration in place (ticket-004) and the re-export fix applied (ticket-005), running `mypy idessem/` will report strict-mode errors across all production code. The dessem module is the largest module (~95% of production code) and will have the most errors (~1050+ after attr-defined and no-any-return are resolved). The idecomp plan established proven annotation patterns for cfinterface subclasses: `IO[Any]` for read/write, `# type: ignore[override]` for return type mismatches, `Optional[Any]` for `__init__` parameters, and `# type: ignore[import-untyped]` for pandas/numpy.

### Relation to Epic

This is the largest ticket in Epic 02. It fixes all strict-mode errors in the dessem module (handlers, models, blocos, arquivos, componentes). After this ticket, `mypy idessem/dessem/` passes under strict mode.

### Current State

Error categories in idessem (from `mypy --strict --no-warn-return-any`):

| Error Code        | Count | Description                                          |
| ----------------- | ----- | ---------------------------------------------------- |
| `no-untyped-def`  | 957   | Functions missing type annotations                   |
| `type-arg`        | 129   | Missing type parameters for generics (IO, dict, etc) |
| `attr-defined`    | 64    | Re-export issue (fixed by ticket-005)                |
| `unused-ignore`   | 3     | Unnecessary type: ignore in operut.py                |
| `assignment`      | 1     | Type mismatch in hidr.py line 164                    |
| `no-untyped-call` | 1     | Call to untyped function                             |

After ticket-005 fixes the 64 attr-defined errors, the remaining work is:

- ~957 `no-untyped-def` errors: Add type annotations to all functions/methods
- ~129 `type-arg` errors: Add type parameters to generic types (IO -> IO[Any], dict -> dict[str, list], etc.)
- 3 `unused-ignore` errors: Remove unnecessary `# type: ignore` in operut.py
- 1 `assignment` error: Fix type annotation in hidr.py line 164
- 1 `no-untyped-call` error: Add annotations or ignore

## Specification

### Requirements

1. Add type annotations to all functions and methods in the dessem module that lack them
2. Add `# type: ignore[override]` with explanation comments on all Block/Register `read()` and `write()` methods that override cfinterface base return types
3. Replace bare `# type: ignore` on `import pandas as pd` and `import numpy as np` lines with `# type: ignore[import-untyped]`
4. Use `IO[Any]` for all `read()` and `write()` file parameter types
5. Use `Optional[Any]` for cfinterface `__init__` parameter types (`previous`, `next`, `data`)
6. Fix the 3 `unused-ignore` errors in `operut.py` (remove or correct the ignore comments)
7. Fix the 1 `assignment` error in `hidr.py` line 164 (type the list comprehension correctly)
8. After all fixes, `mypy idessem/dessem/` must pass under the strict configuration
9. All 558 tests must still pass

### Inputs/Props

- All Python files in `idessem/dessem/` and `idessem/dessem/modelos/`

### Outputs/Behavior

- `mypy idessem/dessem/` reports zero errors under strict mode configuration from ticket-004
- All existing tests pass unchanged

### Error Handling

Not applicable -- this is a type annotation change with no runtime impact.

## Acceptance Criteria

- [ ] Given the command `mypy idessem/dessem/`, when executed with the strict config from ticket-004, then zero errors are reported
- [ ] Given the command `grep -r '# type: ignore$' idessem/dessem/`, when executed, then zero bare type-ignore comments are found (all have specific error codes)
- [ ] Given the command `pytest -x -q`, when executed, then all 558 tests pass
- [ ] Given any `read()` or `write()` method in a Block/Register subclass in `idessem/dessem/`, when inspected, then the file parameter is typed as `IO[Any]` and the method has `# type: ignore[override]` if it overrides a cfinterface base method

## Implementation Guide

### Suggested Approach

Work through the errors module by module. Run `mypy idessem/dessem/ 2>&1 | head -50` to see the first batch, fix them, then iterate until zero errors.

**Common fix patterns** (from idecomp epic-02 learnings at `/home/rogerio/git/idecomp/plans/idecomp-quality-performance/learnings/epic-02-summary.md`):

1. **Missing return type on `__init__`**:

   ```python
   def __init__(self, data: Optional[Any] = ...) -> None:
   ```

2. **Missing parameter annotations on `__init__` for Block/Register subclasses**:

   ```python
   def __init__(self, previous: Optional[Any] = None,
                next: Optional[Any] = None,
                data: Optional[Any] = None) -> None:
   ```

3. **read/write override**:

   ```python
   def read(self, file: IO[Any], *args: Any, **kwargs: Any) -> None:  # type: ignore[override]  # cfinterface base returns bool
   ```

4. **pandas/numpy imports**:

   ```python
   import pandas as pd  # type: ignore[import-untyped]
   import numpy as np  # type: ignore[import-untyped]
   ```

5. **Property setter return type**:

   ```python
   @property_name.setter
   def property_name(self, value: pd.DataFrame) -> None:
   ```

6. **Class variable annotations** (for BLOCKS, REGISTERS, COLUMN_NAMES, etc.):

   ```python
   from typing import ClassVar, List, Type
   BLOCKS: ClassVar[List[Type[Block]]] = [...]
   COLUMN_NAMES: ClassVar[List[str]] = [...]
   ```

7. **Generic type parameters** (IO, Dict, List in function signatures):

   ```python
   # Before: def read(self, file: IO, ...):
   # After:  def read(self, file: IO[Any], ...):
   # Before: dados: Dict[str, list] = ...
   # After:  dados: dict[str, list[Any]] = ...
   ```

8. **The IDENTIFIER slice issue in entdados.py** (17 occurrences of `self.__class__.IDENTIFIER[:2]  # type: ignore`):
   These are accessing `IDENTIFIER` which is a string class variable. The `# type: ignore` is bare and needs a specific error code. Check what error code mypy reports and add it, or if the code is no longer needed after adding annotations, remove the ignore.

9. **The assignment error in hidr.py line 164**:

   ```python
   # Before: registros: List[RegistroUHEHidr] = [r for r in self.data][1:]
   # After:  registros = [r for r in self.data][1:]  # type: ignore[assignment]  # data yields Register, narrowed to RegistroUHEHidr
   # Or cast: registros: List[RegistroUHEHidr] = cast(List[RegistroUHEHidr], [r for r in self.data][1:])
   ```

10. **The unused-ignore errors in operut.py**:
    Lines 3, 113, 263 have `# type: ignore` comments that are unnecessary. Check if removing them causes errors; if not, remove them.

### Key Files to Modify

All Python files under:

- `/home/rogerio/git/idessem/idessem/dessem/*.py` (~43 handler files)
- `/home/rogerio/git/idessem/idessem/dessem/modelos/*.py` (~46 model files)
- `/home/rogerio/git/idessem/idessem/dessem/modelos/blocos/*.py` (3 files: tabelacsv.py, versaomodelo.py, dataestudo.py)
- `/home/rogerio/git/idessem/idessem/dessem/modelos/arquivos/arquivocsv.py` (1 file)
- `/home/rogerio/git/idessem/idessem/dessem/modelos/componentes/stagedatefield.py` (1 file)

### Patterns to Follow

- Follow idecomp's annotation patterns exactly. Reference files:
  - `/home/rogerio/git/idecomp/idecomp/decomp/modelos/dadger.py` for Register subclass annotations
  - `/home/rogerio/git/idecomp/idecomp/decomp/modelos/blocos/tabelacsv.py` for TabelaCSV Block subclass annotations
  - `/home/rogerio/git/idecomp/idecomp/decomp/hidr.py` for RegisterFile handler annotations
- `# type: ignore` always has specific code AND inline explanation. Zero bare ignores.
- `IO[Any]` over `IO[str]` for ALL read/write overrides (inewave learning: `Line.write()` returns `Union[str, bytes]`)

### Pitfalls to Avoid

- Do NOT use `IO[str]` -- this caused 193 errors in inewave due to `Line.write()` returning `Union[str, bytes]`
- Do NOT remove `# type: ignore` comments without checking if they are still needed -- some are needed even under strict
- Do NOT add `warn_return_any = true` -- this would produce 707 meaningless errors from cfinterface's `Any`-typed data
- Do NOT annotate test files -- they are out of scope for strict mode
- Do NOT change any runtime behavior -- only type annotations and ignore comments
- The `entdados.py` model file is very large (2900+ lines) with 17 bare `# type: ignore` occurrences on `IDENTIFIER[:2]` -- these all need the same fix pattern applied consistently

## Testing Requirements

### Unit Tests

No new tests. All 558 existing tests must pass.

### Integration Tests

- `mypy idessem/dessem/` passes with zero errors

### E2E Tests

Not applicable.

## Dependencies

- **Blocked By**: ticket-004-add-mypy-strict-config.md, ticket-005-fix-reexport-visibility.md
- **Blocks**: ticket-008-replace-bare-type-ignores.md

## Effort Estimate

**Points**: 3
**Confidence**: Medium (error count is high but patterns are well-established from idecomp/inewave)

## Out of Scope

- Fixing type errors in `idessem/libs/` (ticket-007)
- Replacing bare type-ignore comments that may already have codes (ticket-008 verifies completeness)
- Adding type stubs for pandas/numpy
- Changing any runtime behavior
