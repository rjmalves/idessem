# Epic 01: Foundation and StorageType Migration

## Goals

1. Bump cfinterface dependency from >= 1.8.0 to >= 1.9.0
2. Replace the 1 `STORAGE = "BINARY"` string literal with `StorageType.BINARY`
3. Migrate 5 test files (38 call sites) from deprecated `set_version()` to `read(content, version="...")`
4. Verify the full test suite passes with zero failures and zero deprecation warnings

## Scope

- **In scope**: pyproject.toml dependency bump, 1 handler file STORAGE migration, 5 test file set_version migration, full test suite verification
- **Out of scope**: mypy strict mode, lazy imports, new VERSIONS, TabularSection adoption

## Tickets

| Ticket     | Title                                              | Points |
| ---------- | -------------------------------------------------- | ------ |
| ticket-001 | Bump cfinterface dependency to >= 1.9.0            | 1      |
| ticket-002 | Migrate STORAGE string literal to StorageType enum | 1      |
| ticket-003 | Migrate set_version calls and verify test suite    | 2      |

## Success Criteria

- `grep -r 'STORAGE = "BINARY"' idessem/` returns zero matches
- `pyproject.toml` declares `"cfinterface>=1.9.0"`
- `grep -r "set_version" tests/ --include="*.py"` returns zero matches
- `pytest` shows 558 tests passed, 0 failed
- `pytest -W error::DeprecationWarning` shows 0 failures from STORAGE or set_version
