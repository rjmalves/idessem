# ticket-004 Add mypy strict configuration to pyproject.toml

## Context

### Background

idessem has no mypy configuration in `pyproject.toml`. Running `mypy idessem/ --strict` reports 1,862 errors in 72 files. Before enabling strict mode per-module, a `[tool.mypy]` section must be added with global settings and per-module `[[tool.mypy.overrides]]` blocks. The idecomp and inewave plans established proven patterns for this: `strict = true` per module with `warn_return_any = false` globally (because cfinterface's `Section.data`, `Block.data`, and `Register.data` are `Any`-typed, producing 707 meaningless `no-any-return` errors).

### Relation to Epic

This ticket provides the mypy configuration infrastructure. Subsequent tickets (005, 006, 007, 008) will fix the actual type errors and re-export issues to make each module pass under strict mode.

### Current State

- `pyproject.toml` has no `[tool.mypy]` section
- `mypy idessem/` passes with 0 errors (default mode)
- `mypy idessem/ --strict` reports 1,862 errors in 72 files
- `mypy idessem/ --strict --no-warn-return-any` reports 1,155 errors in 71 files (removing 707 no-any-return errors)
- cfinterface's `Block.data`, `Section.data`, `Register.data` are `Any`-typed, which makes `warn_return_any` produce hundreds of meaningless errors

## Specification

### Requirements

1. Add a `[tool.mypy]` section to `/home/rogerio/git/idessem/pyproject.toml` with `warn_return_any = false`
2. Add `[[tool.mypy.overrides]]` blocks for each production code module, all with `strict = true` and `warn_return_any = false`:
   - `idessem.dessem.*`
   - `idessem.dessem.modelos.*`
   - `idessem.dessem.modelos.blocos.*`
   - `idessem.dessem.modelos.arquivos.*`
   - `idessem.dessem.modelos.componentes.*`
   - `idessem.libs.*`
   - `idessem.libs.modelos.*`
   - `idessem.config`
3. Do NOT enable strict mode at the global level -- use per-module overrides only
4. After adding the configuration, `mypy idessem/` should still run (it will report strict-mode errors, which will be fixed in tickets 005-008)

### Inputs/Props

- File: `/home/rogerio/git/idessem/pyproject.toml`

### Outputs/Behavior

- `pyproject.toml` has a `[tool.mypy]` section with `warn_return_any = false`
- `pyproject.toml` has 8 `[[tool.mypy.overrides]]` blocks (one per module)

### Error Handling

Not applicable.

## Acceptance Criteria

- [ ] Given `pyproject.toml`, when searching for `[tool.mypy]`, then exactly one section is found
- [ ] Given `pyproject.toml`, when searching for `strict = true`, then exactly 8 matches are found (one per override block)
- [ ] Given `pyproject.toml`, when counting `warn_return_any = false` occurrences, then 9 matches are found (1 global + 8 overrides)
- [ ] Given the command `mypy idessem/config.py`, when executed, then zero errors are reported (config.py is simple enough to pass strict immediately)
- [ ] Given the command `mypy idessem/`, when executed (without --strict flag), then the mypy configuration is picked up from `pyproject.toml` and strict mode is applied per-module

## Implementation Guide

### Suggested Approach

Add the following configuration to `/home/rogerio/git/idessem/pyproject.toml` after the `[tool.ruff]` section but before any `[tool.uv.sources]` section:

```toml
[tool.mypy]
warn_return_any = false

[[tool.mypy.overrides]]
module = "idessem.dessem.*"
strict = true
warn_return_any = false

[[tool.mypy.overrides]]
module = "idessem.dessem.modelos.*"
strict = true
warn_return_any = false

[[tool.mypy.overrides]]
module = "idessem.dessem.modelos.blocos.*"
strict = true
warn_return_any = false

[[tool.mypy.overrides]]
module = "idessem.dessem.modelos.arquivos.*"
strict = true
warn_return_any = false

[[tool.mypy.overrides]]
module = "idessem.dessem.modelos.componentes.*"
strict = true
warn_return_any = false

[[tool.mypy.overrides]]
module = "idessem.libs.*"
strict = true
warn_return_any = false

[[tool.mypy.overrides]]
module = "idessem.libs.modelos.*"
strict = true
warn_return_any = false

[[tool.mypy.overrides]]
module = "idessem.config"
strict = true
warn_return_any = false
```

### Key Files to Modify

- `/home/rogerio/git/idessem/pyproject.toml`

### Patterns to Follow

- Exact same pattern as idecomp's `pyproject.toml` `[tool.mypy]` section. See `/home/rogerio/git/idecomp/pyproject.toml` for reference.
- `warn_return_any = false` is mandatory both globally and per-override because cfinterface's `Section.data`, `Block.data`, and `Register.data` are all `Any`-typed.

### Pitfalls to Avoid

- Do NOT set `strict = true` at the global `[tool.mypy]` level -- only in per-module overrides. Global strict breaks third-party imports.
- Do NOT omit `warn_return_any = false` from any override block -- this would produce hundreds of errors from cfinterface's `Any`-typed data attributes.
- Do NOT add overrides for test files -- tests are not production code and strict mode on tests is out of scope.
- idessem has one more subdirectory than idecomp: `modelos/componentes/` -- include it in the override blocks.

## Testing Requirements

### Unit Tests

No new tests.

### Integration Tests

- `mypy idessem/config.py` passes with zero errors (config.py is trivially strict-compliant)
- `mypy idessem/` runs without configuration errors

### E2E Tests

Not applicable.

## Dependencies

- **Blocked By**: ticket-003-migrate-set-version-verify-suite.md (all tests must be passing first)
- **Blocks**: ticket-005-fix-reexport-visibility.md, ticket-006-enable-mypy-strict-dessem.md, ticket-007-enable-mypy-strict-libs.md

## Effort Estimate

**Points**: 2
**Confidence**: High

## Out of Scope

- Fixing type errors revealed by strict mode (tickets 005, 006, 007)
- Adding mypy overrides for test files
- Changing any Python source files
