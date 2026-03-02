# ticket-005 Fix re-export visibility for DataEstudo and VersaoModelo

## Context

### Background

Under mypy strict mode, 64 `attr-defined` errors occur because 32 handler files import `DataEstudo` and `VersaoModelo` from `idessem.dessem.modelos.arquivos.arquivocsv`, which itself imports them from `idessem.dessem.modelos.blocos.dataestudo` and `idessem.dessem.modelos.blocos.versaomodelo`. mypy strict mode requires re-exported names to be explicitly listed in `__all__` or the module's `__init__.py`. The fix is to add an `__all__` list to `arquivocsv.py` that includes these re-exported names.

### Relation to Epic

This ticket fixes a structural issue that accounts for 64 of the ~1155 strict-mode errors. It must be done before or concurrently with ticket-006 (dessem strict enablement) so the annotation ticket does not have to suppress 64 errors with `# type: ignore[attr-defined]`.

### Current State

- `idessem/dessem/modelos/arquivos/arquivocsv.py` imports `VersaoModelo`, `DataEstudo`, and `TabelaCSV` from their respective `blocos/` modules
- 32 handler files (all ArquivoCSV subclasses plus `pdo_operacao.py`, `avl_estatfpha.py`, `des_log_relato.py`) import `DataEstudo` and/or `VersaoModelo` from `idessem.dessem.modelos.arquivos.arquivocsv`
- These imports work at runtime but mypy strict flags them as `[attr-defined]` because `arquivocsv.py` does not explicitly re-export them
- Running `mypy idessem/ --strict --no-warn-return-any 2>&1 | grep "attr-defined" | wc -l` returns 64

## Specification

### Requirements

1. Add an `__all__` list to `/home/rogerio/git/idessem/idessem/dessem/modelos/arquivos/arquivocsv.py` that includes `"ArquivoCSV"`, `"VersaoModelo"`, `"DataEstudo"`, and `"TabelaCSV"`
2. After adding `__all__`, the 64 `attr-defined` errors must disappear from `mypy idessem/ --strict` output
3. No changes to any other files

### Inputs/Props

- File: `/home/rogerio/git/idessem/idessem/dessem/modelos/arquivos/arquivocsv.py`

### Outputs/Behavior

- `arquivocsv.py` has an `__all__` list after the imports that includes all 4 names used by downstream handlers
- `mypy idessem/ --strict 2>&1 | grep "attr-defined" | wc -l` returns 0

### Error Handling

Not applicable -- this is a static code change.

## Acceptance Criteria

- [ ] Given `/home/rogerio/git/idessem/idessem/dessem/modelos/arquivos/arquivocsv.py`, when opened, then an `__all__` list is present containing `"ArquivoCSV"`, `"VersaoModelo"`, `"DataEstudo"`, and `"TabelaCSV"`
- [ ] Given the command `mypy idessem/ --strict 2>&1 | grep "attr-defined" | wc -l`, when executed, then the output is `0`
- [ ] Given the command `pytest -x -q`, when executed, then all 558 tests pass (no runtime impact)
- [ ] Given the command `python -c "from idessem.dessem.modelos.arquivos.arquivocsv import DataEstudo, VersaoModelo; print('OK')"`, when executed, then it prints `OK`

## Implementation Guide

### Suggested Approach

Add an `__all__` list to `/home/rogerio/git/idessem/idessem/dessem/modelos/arquivos/arquivocsv.py` immediately after the import block (after line 8, before the class definition):

```python
from idessem.dessem.modelos.blocos.versaomodelo import VersaoModelo
from idessem.dessem.modelos.blocos.dataestudo import DataEstudo
from idessem.dessem.modelos.blocos.tabelacsv import TabelaCSV

from cfinterface.files.blockfile import BlockFile
from datetime import datetime
import pandas as pd  # type: ignore
from typing import TypeVar, Optional

__all__ = ["ArquivoCSV", "VersaoModelo", "DataEstudo", "TabelaCSV"]


class ArquivoCSV(BlockFile):
    ...
```

### Key Files to Modify

- `/home/rogerio/git/idessem/idessem/dessem/modelos/arquivos/arquivocsv.py` (add `__all__` after imports)

### Patterns to Follow

- Python convention for re-exporting: `__all__` must include every name that downstream modules import from this module
- Reference: Python docs on `__all__` and mypy's `--strict` re-export checking

### Pitfalls to Avoid

- Do NOT forget to include `"TabelaCSV"` in `__all__` -- while fewer handlers import it directly from `arquivocsv`, it is used by the `ArquivoCSV` class and the `_tabela` method references it
- Do NOT add the `__all__` to the wrong file -- it goes in `arquivocsv.py`, not in `__init__.py`
- Do NOT change any imports in the 32 handler files -- the fix is entirely in the re-exporting module

## Testing Requirements

### Unit Tests

No new tests needed.

### Integration Tests

- `mypy idessem/ --strict 2>&1 | grep "attr-defined" | wc -l` returns 0
- `pytest -x -q` passes all 558 tests

### E2E Tests

Not applicable.

## Dependencies

- **Blocked By**: ticket-004-add-mypy-strict-config.md
- **Blocks**: ticket-006-enable-mypy-strict-dessem.md

## Effort Estimate

**Points**: 1
**Confidence**: High

## Out of Scope

- Fixing type annotation errors (ticket-006, ticket-007)
- Changing imports in handler files
- Adding `__all__` to other `__init__.py` files
