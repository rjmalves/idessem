# ticket-002 Migrate STORAGE string literal to StorageType enum

## Context

### Background

cfinterface v1.9.0 introduced the `StorageType` enum to replace string literals `"BINARY"` and `"TEXT"`. Using the old string literals emits `DeprecationWarning`. idessem has 1 file that declares `STORAGE = "BINARY"` and must be migrated to `STORAGE = StorageType.BINARY`.

### Relation to Epic

This is the second ticket in Epic 01. It requires cfinterface >= 1.9.0 (ticket-001) and is a prerequisite for the deprecation-free test verification in ticket-003.

### Current State

One file in `idessem/dessem/` contains `STORAGE = "BINARY"`:

1. `/home/rogerio/git/idessem/idessem/dessem/hidr.py` (line 19) -- RegisterFile subclass

No files use `STORAGE = "TEXT"` -- all other handlers inherit the default `StorageType.TEXT` from their base classes.

## Specification

### Requirements

1. In `hidr.py`, replace `STORAGE = "BINARY"` with `STORAGE = StorageType.BINARY`
2. In `hidr.py`, add `from cfinterface.storage import StorageType` to the cfinterface import group
3. The import must be placed adjacent to the existing cfinterface import (before idessem local imports)
4. No other code changes in this file

### Inputs/Props

- 1 handler file: `/home/rogerio/git/idessem/idessem/dessem/hidr.py`

### Outputs/Behavior

- The file has `STORAGE = StorageType.BINARY` instead of `STORAGE = "BINARY"`
- The file imports `StorageType` from `cfinterface.storage`

### Error Handling

Not applicable -- this is a static code change.

## Acceptance Criteria

- [ ] Given the command `grep -r 'STORAGE = "BINARY"' idessem/`, when executed after migration, then zero matches are found
- [ ] Given the command `grep -r 'StorageType.BINARY' idessem/`, when executed after migration, then exactly 1 match is found in `hidr.py`
- [ ] Given the command `grep -r 'from cfinterface.storage import StorageType' idessem/`, when executed after migration, then exactly 1 match is found in `hidr.py`
- [ ] Given `/home/rogerio/git/idessem/idessem/dessem/hidr.py`, when opened, then `from cfinterface.storage import StorageType` appears in the cfinterface import group before idessem imports
- [ ] Given the command `pytest tests/dessem/test_hidr.py -v`, when executed, then all tests in this file pass

## Implementation Guide

### Suggested Approach

Apply the following transformation to `/home/rogerio/git/idessem/idessem/dessem/hidr.py`:

1. Add `from cfinterface.storage import StorageType` adjacent to the existing cfinterface import (line 1)
2. Replace `STORAGE = "BINARY"` with `STORAGE = StorageType.BINARY` (line 19)

**Before:**

```python
from cfinterface.files.registerfile import RegisterFile
from idessem.dessem.modelos.hidr import RegistroUHEHidr
from idessem.config import MESES_ABREV
import pandas as pd  # type: ignore
...

class Hidr(RegisterFile):
    ...
    STORAGE = "BINARY"
```

**After:**

```python
from cfinterface.files.registerfile import RegisterFile
from cfinterface.storage import StorageType
from idessem.dessem.modelos.hidr import RegistroUHEHidr
from idessem.config import MESES_ABREV
import pandas as pd  # type: ignore
...

class Hidr(RegisterFile):
    ...
    STORAGE = StorageType.BINARY
```

### Key Files to Modify

- `/home/rogerio/git/idessem/idessem/dessem/hidr.py` (line 1 for import, line 19 for STORAGE attribute)

### Patterns to Follow

- Follow the idecomp pattern: `from cfinterface.storage import StorageType` in the cfinterface import group, before idessem local imports. See `/home/rogerio/git/idecomp/idecomp/decomp/hidr.py` for reference.
- Import ordering convention: cfinterface imports first (all adjacent), then idessem imports, then third-party/stdlib imports last.

### Pitfalls to Avoid

- Do NOT add `STORAGE = StorageType.TEXT` to files that don't currently have a STORAGE attribute -- they inherit TEXT from their base class and must not be given a redundant attribute (inewave learning)
- Do NOT change any other code in this file -- the ticket scope is strictly the STORAGE attribute and its import
- Do NOT reorder other imports while adding the StorageType import

## Testing Requirements

### Unit Tests

No new tests needed. Existing tests for `hidr.py` serve as regression tests.

### Integration Tests

- Run `pytest tests/dessem/test_hidr.py -v` to confirm no regressions
- Run `pytest -W error::DeprecationWarning tests/dessem/test_hidr.py` to confirm no STORAGE-related deprecation warnings from this file

### E2E Tests

Not applicable.

## Dependencies

- **Blocked By**: ticket-001-bump-cfinterface-dependency.md
- **Blocks**: ticket-003-migrate-set-version-verify-suite.md

## Effort Estimate

**Points**: 1
**Confidence**: High

## Out of Scope

- Migrating set_version calls in test files (ticket-003)
- Adding StorageType to files that don't currently have STORAGE attributes
- Any changes to the model files under `modelos/`
