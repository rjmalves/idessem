# Epic 02: Quality and Type Safety

## Goals

1. Add mypy strict configuration to `pyproject.toml` with per-module overrides
2. Enable mypy strict mode on all production code modules (fixing ~1155 errors after warn_return_any=false)
3. Replace all 49 bare `# type: ignore` comments with specific error codes and explanations
4. Fix the 64 `attr-defined` errors from DataEstudo/VersaoModelo re-exports
5. Implement lazy imports for `idessem/dessem/__init__.py` (43 eager imports)

## Scope

- **In scope**: mypy strict configuration, type annotation fixes, bare type-ignore cleanup, re-export fix, lazy imports for dessem
- **Out of scope**: New tests (epic-03), documentation (epic-04), changes to public API, test file annotations

## Tickets

| Ticket     | Title                                                    | Points |
| ---------- | -------------------------------------------------------- | ------ |
| ticket-004 | Add mypy strict configuration to pyproject.toml          | 2      |
| ticket-005 | Fix re-export visibility for DataEstudo and VersaoModelo | 1      |
| ticket-006 | Enable mypy strict for dessem handlers and models        | 3      |
| ticket-007 | Enable mypy strict for libs module                       | 2      |
| ticket-008 | Replace bare type-ignore comments with error codes       | 2      |
| ticket-009 | Implement lazy imports for dessem module                 | 2      |

## Success Criteria

- `mypy idessem/` passes with zero errors (per-module overrides in `pyproject.toml`)
- `grep -r '# type: ignore$' idessem/` returns zero matches
- `idessem/dessem/__init__.py` uses PEP 562 `__getattr__` lazy import pattern
- All 558 tests continue to pass
