# ticket-009 Implement lazy imports for dessem module

## Context

### Background

`idessem/dessem/__init__.py` eagerly imports all 43 handler classes at package load time. This means `import idessem` triggers importing all handler files, their model files, and transitively cfinterface, pandas, and numpy. The PEP 562 lazy import pattern (`__getattr__` + `__dir__`) can defer these imports until the specific handler is first accessed, reducing import time for users who only need a subset of handlers.

### Relation to Epic

This is the final ticket in Epic 02. It improves runtime performance through lazy loading while maintaining full backward compatibility for `from idessem.dessem import Entdados` style imports.

### Current State

- `idessem/dessem/__init__.py` has 43 eager import statements (lines 3-45)
- `idessem/__init__.py` has `from . import dessem` which triggers all 43 imports
- `idessem/libs/__init__.py` has only 1 import (`UsinasHidreletricas`) -- not worth converting
- The 43 handlers map to these module paths:
  ```
  Areacont -> .areacont
  AvlAltQueda -> .avl_altqueda
  AvlDesvFpha -> .avl_desvfpha
  AvlEstatFpha -> .avl_estatfpha
  AvlFpha1 -> .avl_fpha1
  AvlFpha2 -> .avl_fpha2
  AvlFpha3 -> .avl_fpha3
  Dadvaz -> .dadvaz
  Deflant -> .deflant
  DesLogRelato -> .des_log_relato
  Desselet -> .desselet
  DessemArq -> .dessemarq
  Dessopc -> .dessopc
  Entdados -> .entdados
  Hidr -> .hidr
  LogInviab -> .log_inviab
  LogMatriz -> .log_matriz
  Operuh -> .operuh
  Operut -> .operut
  PdoAvalQmaxUsih -> .pdo_aval_qmaxusih
  PdoCmoBar -> .pdo_cmobar
  PdoEcoFcfCortes -> .pdo_eco_fcfcortes
  PdoEcoUsih -> .pdo_eco_usih
  PdoEcoUsihConj -> .pdo_eco_usih_conj
  PdoEcoUsihPolin -> .pdo_eco_usih_polin
  PdoEolica -> .pdo_eolica
  PdoHidr -> .pdo_hidr
  PdoInter -> .pdo_inter
  PdoOperLpp -> .pdo_oper_lpp
  PdoOperTerm -> .pdo_oper_term
  PdoOperTitulacaoContratos -> .pdo_oper_titulacao_contratos
  PdoOperTitulacaoUsinas -> .pdo_oper_titulacao_usinas
  PdoOperTviagCalha -> .pdo_oper_tviag_calha
  PdoOperUct -> .pdo_oper_uct
  PdoOperacao -> .pdo_operacao
  PdoReserva -> .pdo_reserva
  PdoSist -> .pdo_sist
  PdoSomFlux -> .pdo_somflux
  PdoTerm -> .pdo_term
  Renovaveis -> .renovaveis
  Respot -> .respot
  Term -> .termdat
  Uch -> .uch
  ```

## Specification

### Requirements

1. Replace the 43 eager imports in `idessem/dessem/__init__.py` with PEP 562 lazy import pattern:
   - A `_LAZY_IMPORTS: dict[str, str]` dictionary mapping class names to module paths
   - A `__all__` list generated from `sorted(_LAZY_IMPORTS.keys())`
   - A `def __getattr__(name: str) -> Any:` function that imports on first access and caches via `globals()[name] = value`
   - A `def __dir__() -> list[str]: return __all__` function
2. All existing import patterns must continue to work:
   - `from idessem.dessem import Entdados`
   - `import idessem.dessem; idessem.dessem.Entdados`
   - `from idessem.dessem import *`
3. `idessem/libs/__init__.py` is NOT converted (only 1 import, overhead negligible)
4. After conversion, all 558 tests must pass
5. The `__getattr__` function must have `-> Any` return annotation for mypy strict compatibility

### Inputs/Props

- File: `/home/rogerio/git/idessem/idessem/dessem/__init__.py`

### Outputs/Behavior

- `idessem/dessem/__init__.py` uses PEP 562 lazy import pattern
- `dir(idessem.dessem)` returns all 43 class names
- First access to any handler class triggers its import and caches it
- Subsequent accesses bypass `__getattr__` entirely

### Error Handling

- If a class name is not in `_LAZY_IMPORTS`, `__getattr__` raises `AttributeError(f"module 'idessem.dessem' has no attribute '{name}'")`

## Acceptance Criteria

- [ ] Given `idessem/dessem/__init__.py`, when opened, then it contains `_LAZY_IMPORTS` dict with exactly 43 entries
- [ ] Given `idessem/dessem/__init__.py`, when opened, then it contains `def __getattr__(name: str) -> Any:` and `def __dir__() -> list[str]:`
- [ ] Given the command `python -c "from idessem.dessem import Entdados; print(type(Entdados))"`, when executed, then it prints `<class 'idessem.dessem.entdados.Entdados'>`
- [ ] Given the command `python -c "import idessem.dessem; print(len([x for x in dir(idessem.dessem) if not x.startswith('_')]))"`, when executed, then the output is 43 or greater
- [ ] Given the command `pytest -x -q`, when executed, then all 558 tests pass

## Implementation Guide

### Suggested Approach

Replace the contents of `idessem/dessem/__init__.py` with:

```python
from typing import Any
import importlib

_LAZY_IMPORTS: dict[str, str] = {
    "Areacont": ".areacont",
    "AvlAltQueda": ".avl_altqueda",
    "AvlDesvFpha": ".avl_desvfpha",
    "AvlEstatFpha": ".avl_estatfpha",
    "AvlFpha1": ".avl_fpha1",
    "AvlFpha2": ".avl_fpha2",
    "AvlFpha3": ".avl_fpha3",
    "Dadvaz": ".dadvaz",
    "Deflant": ".deflant",
    "DesLogRelato": ".des_log_relato",
    "Desselet": ".desselet",
    "DessemArq": ".dessemarq",
    "Dessopc": ".dessopc",
    "Entdados": ".entdados",
    "Hidr": ".hidr",
    "LogInviab": ".log_inviab",
    "LogMatriz": ".log_matriz",
    "Operuh": ".operuh",
    "Operut": ".operut",
    "PdoAvalQmaxUsih": ".pdo_aval_qmaxusih",
    "PdoCmoBar": ".pdo_cmobar",
    "PdoCmosist": ".pdo_cmosist",
    "PdoEcoFcfCortes": ".pdo_eco_fcfcortes",
    "PdoEcoUsih": ".pdo_eco_usih",
    "PdoEcoUsihConj": ".pdo_eco_usih_conj",
    "PdoEcoUsihPolin": ".pdo_eco_usih_polin",
    "PdoElev": ".pdo_elev",
    "PdoEolica": ".pdo_eolica",
    "PdoHidr": ".pdo_hidr",
    "PdoInter": ".pdo_inter",
    "PdoOperLpp": ".pdo_oper_lpp",
    "PdoOperTerm": ".pdo_oper_term",
    "PdoOperTitulacaoContratos": ".pdo_oper_titulacao_contratos",
    "PdoOperTitulacaoUsinas": ".pdo_oper_titulacao_usinas",
    "PdoOperTviagCalha": ".pdo_oper_tviag_calha",
    "PdoOperUct": ".pdo_oper_uct",
    "PdoOperUsih": ".pdo_oper_usih",
    "PdoOperacao": ".pdo_operacao",
    "PdoReserva": ".pdo_reserva",
    "PdoSist": ".pdo_sist",
    "PdoSomFlux": ".pdo_somflux",
    "PdoTerm": ".pdo_term",
    "Renovaveis": ".renovaveis",
    "Respot": ".respot",
    "Term": ".termdat",
    "Uch": ".uch",
}

__all__ = sorted(_LAZY_IMPORTS.keys())


def __getattr__(name: str) -> Any:
    if name in _LAZY_IMPORTS:
        module = importlib.import_module(
            _LAZY_IMPORTS[name], __name__
        )
        value = getattr(module, name)
        globals()[name] = value
        return value
    raise AttributeError(
        f"module {__name__!r} has no attribute {name!r}"
    )


def __dir__() -> list[str]:
    return __all__
```

Note: The current `__init__.py` has 43 imports but the exact class/module mapping must be verified against the current file. The mapping above was derived from the current imports. Key mappings to double-check:

- `Term` comes from `.termdat` (not `.term`)
- `PdoCmosist` is the class name (not `PdoCmoSist`) -- verify from the import line

### Key Files to Modify

- `/home/rogerio/git/idessem/idessem/dessem/__init__.py`

### Patterns to Follow

- Exact same pattern as idecomp's `idecomp/decomp/__init__.py`. See `/home/rogerio/git/idecomp/idecomp/decomp/__init__.py` for reference.
- `__dir__` is required alongside `__getattr__` (inewave learning)
- `globals()[name] = value` caching eliminates repeat `__getattr__` calls (inewave learning)
- `-> Any` return annotation on `__getattr__` is required for mypy strict (inewave learning)

### Pitfalls to Avoid

- Do NOT forget `__dir__` -- without it, `dir(idessem.dessem)` returns only already-cached names
- Do NOT forget `globals()[name] = value` caching -- without it, every access goes through `__getattr__`
- Module names must be extracted from the existing imports, not guessed -- verify each `_LAZY_IMPORTS` value matches the actual module filename
- Do NOT convert `idessem/libs/__init__.py` -- it has only 1 import, overhead is negligible
- Do NOT change `idessem/__init__.py` -- `from . import dessem` triggers the subpackage `__init__.py` but `__getattr__` handles deferred class loading
- Verify the class name `PdoCmosist` vs `PdoCmoSist` -- the existing import uses `from .pdo_cmosist import PdoCmosist`

## Testing Requirements

### Unit Tests

No new tests. All 558 existing tests serve as regression tests for import compatibility.

### Integration Tests

- `python -c "from idessem.dessem import Entdados; print(Entdados)"` -- works
- `python -c "from idessem.dessem import *; print(Entdados)"` -- works
- `python -c "import idessem.dessem; print(idessem.dessem.Entdados)"` -- works

### E2E Tests

Not applicable.

## Dependencies

- **Blocked By**: ticket-008-replace-bare-type-ignores.md
- **Blocks**: None (last ticket in epic-02)

## Effort Estimate

**Points**: 2
**Confidence**: High (pattern is well-established from idecomp)

## Out of Scope

- Converting `idessem/libs/__init__.py` to lazy imports
- Benchmarking import time improvements (deferred to epic-03)
- Changing `idessem/__init__.py`
