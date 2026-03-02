# ticket-008 Replace bare type-ignore comments with error codes

## Context

### Background

idessem currently has 49 bare `# type: ignore` comments (no error code specified) across 30 files. After tickets 006 and 007 enable mypy strict mode, most of these will have been replaced during annotation work. This ticket is a cleanup pass to ensure ALL remaining `# type: ignore` comments have specific error codes and explanations, following the idecomp convention of zero bare ignores.

Note: idecomp's learnings revealed that this cleanup ticket was a no-op after the annotation tickets applied the policy inline. The same is likely here, but the ticket ensures completeness verification.

### Relation to Epic

This is a verification and cleanup ticket that runs after the main strict-mode enablement (tickets 006, 007). It ensures the codebase meets the "zero bare ignores" quality standard.

### Current State

- 49 bare `# type: ignore` comments across 30 files (counted via `grep -r "# type: ignore$" idessem/ --include="*.py" | wc -l`)
- Breakdown: 26 are `import pandas as pd  # type: ignore`, 1 is `import numpy as np  # type: ignore`, 17 are `IDENTIFIER[:2]  # type: ignore` in entdados.py, 2 are numpy slice ops in operut.py, 3 are in operut.py that may be unnecessary
- After tickets 006 and 007, many will already have codes; this ticket catches any remaining

## Specification

### Requirements

1. Scan all Python files in `idessem/` for bare `# type: ignore` (without error code)
2. For each bare ignore, determine the specific mypy error code and add it with an inline explanation
3. After completion, `grep -r '# type: ignore$' idessem/ --include="*.py"` returns zero matches
4. `mypy idessem/` still passes with zero errors

### Inputs/Props

- All Python files in `idessem/`

### Outputs/Behavior

- Zero bare `# type: ignore` comments remain
- Every `# type: ignore` has a specific error code like `[import-untyped]`, `[override]`, `[arg-type]`, etc.
- Every `# type: ignore` has an inline explanation

### Error Handling

Not applicable.

## Acceptance Criteria

- [ ] Given the command `grep -r '# type: ignore$' idessem/ --include="*.py"`, when executed, then zero matches are found
- [ ] Given the command `grep -c 'type: ignore\[' idessem/ -r --include="*.py" | grep -v ":0$"`, when executed, then a count is returned showing files with coded ignores
- [ ] Given the command `mypy idessem/`, when executed, then zero errors are reported
- [ ] Given the command `pytest -x -q`, when executed, then all 558 tests pass

## Implementation Guide

### Suggested Approach

1. Run `grep -rn '# type: ignore$' idessem/ --include="*.py"` to find all remaining bare ignores
2. For each line, run `mypy` on that specific file to determine what error code the ignore suppresses
3. Replace `# type: ignore` with `# type: ignore[error-code]  # brief explanation`

**Common replacements**:

- `import pandas as pd  # type: ignore` -> `import pandas as pd  # type: ignore[import-untyped]`
- `import numpy as np  # type: ignore` -> `import numpy as np  # type: ignore[import-untyped]`
- `tabela = tabela[:indice_linha, :]  # type: ignore` -> check if still needed; if so, `# type: ignore[index]  # numpy array slicing`
- `self.__class__.IDENTIFIER[:2]  # type: ignore` -> check if still needed after adding ClassVar annotation; if so, `# type: ignore[attr-defined]  # IDENTIFIER is defined on subclasses`

4. If a `# type: ignore` is no longer needed (the underlying issue was fixed by annotations), remove it entirely rather than adding a code
5. After all replacements, verify `mypy idessem/` still passes

### Key Files to Modify

All Python files in `idessem/` that have bare `# type: ignore` comments. The exact list depends on what was already fixed in tickets 006 and 007. The most likely remaining files are:

- `idessem/dessem/modelos/entdados.py` (17 IDENTIFIER occurrences if not already fixed)
- `idessem/dessem/modelos/operut.py` (numpy-related ignores)

### Patterns to Follow

- idecomp convention: `# type: ignore[error-code]  # brief reason`
- Never use bare `# type: ignore` -- always include the specific error code
- Reference: `/home/rogerio/git/idecomp/idecomp/decomp/modelos/dadger.py` for annotated ignore patterns

### Pitfalls to Avoid

- Do NOT remove `# type: ignore` comments without checking if they are still needed -- removing a needed ignore will cause mypy to fail
- Do NOT add explanation comments that are longer than 60 characters -- keep them concise
- If a `# type: ignore` is no longer needed (the underlying issue was fixed), remove it entirely rather than adding a code

## Testing Requirements

### Unit Tests

No new tests.

### Integration Tests

- `mypy idessem/` passes with zero errors
- `pytest -x -q` shows all 558 tests pass

### E2E Tests

Not applicable.

## Dependencies

- **Blocked By**: ticket-006-enable-mypy-strict-dessem.md, ticket-007-enable-mypy-strict-libs.md
- **Blocks**: ticket-009-implement-lazy-imports-dessem.md

## Effort Estimate

**Points**: 2
**Confidence**: Medium (depends on how many bare ignores remain after tickets 006/007; idecomp found 0 remaining)

## Out of Scope

- Adding type stubs for pandas/numpy
- Annotating test files
- Removing valid type-ignore comments that have error codes
