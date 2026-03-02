# Master Plan: idessem Quality and Performance Upgrade

## Executive Summary

Upgrade the idessem package (v1.1.0, 108 Python source files, 558 tests) to fully leverage cfinterface v1.9.0, applying the patterns and learnings from the completed inewave and idecomp overhauls. This plan covers four epics: foundation upgrade with StorageType migration, quality and type safety improvements, testing and performance enhancements, and documentation updates.

## Goals and Non-Goals

### Goals

1. **Eliminate deprecation warnings**: Replace the 1 `STORAGE = "BINARY"` string literal with `StorageType.BINARY` and bump cfinterface dependency to >= 1.9.0
2. **Migrate deprecated API usage**: Replace 5 test files using `set_version()` with `read(content, version="...")` pattern (38 call sites across 5 test files)
3. **Strengthen type safety**: Move toward mypy strict mode (1,862 errors in 72 files down to 0), replace 49 bare `# type: ignore` comments with specific error codes
4. **Fix re-export visibility**: Add `__all__` to `idessem/dessem/modelos/arquivos/arquivocsv.py` to resolve 64 `attr-defined` errors from DataEstudo/VersaoModelo re-exports
5. **Implement lazy imports**: Convert the `idessem/dessem/__init__.py` eager imports (43 entries) to PEP 562 lazy imports
6. **Optimize performance**: Fix O(n^2) DataFrame concatenation in `pdo_operacao.py`
7. **Improve test infrastructure**: Add pytest-xdist for parallel test execution
8. **Update documentation**: Migration guide, changelog, version bump to v1.2.0

### Non-Goals

- Changing the public API surface (all changes must be backward-compatible)
- Adding TabularSection adoption -- idessem's TabelaCSV pattern is already schema-driven (LINE_MODEL + COLUMN_NAMES), same decision as idecomp
- Adding async file I/O support
- Dropping Python 3.10 support
- Removing pandas as a dependency
- Adding new VERSIONS dictionaries (the 5 existing ones already cover known DESSEM format differences)
- Migrating `idessem/libs/__init__.py` to lazy imports (only 1 import, overhead negligible)
- Adding mypy strict overrides for test files

## Architecture Overview

### Current State

```
idessem/
  dessem/          # 43 handlers (28 ArquivoCSV, 7 BlockFile, 9 RegisterFile) + models
    modelos/
      blocos/      # 3 base block types (TabelaCSV, VersaoModelo, DataEstudo)
      arquivos/    # 1 base archive class (ArquivoCSV)
      componentes/ # 1 custom field (StageDateField)
      *.py         # 46 model files for individual handlers
    *.py           # 43 handler files
  libs/            # 1 handler file (UsinasHidreletricas) + models
    modelos/       # Register definitions for libs
  config.py        # Constants (MESES_ABREV)
```

**Key patterns**:

- `STORAGE = "BINARY"` used as string literal in 1 file: `hidr.py`
- 28 ArquivoCSV subclasses use the TabelaCSV pattern with LINE_MODEL + COLUMN_NAMES -- already schema-driven
- 5 handlers have VERSIONS dictionaries for format evolution (pdo_eco_usih, pdo_eco_fcfcortes, pdo_aval_qmaxusih, avl_fpha1, avl_desvfpha)
- Tests use mock data via `tests/mocks/` with `unittest.mock.patch` on `builtins.open`
- 49 bare `# type: ignore` comments (no error code specified) across 30 files
- mypy default mode: 0 errors; mypy strict: 1,862 errors in 72 files
- No mypy configuration in `pyproject.toml`
- 558 tests passing, 46 warnings (1 STORAGE deprecation + 38 set_version + 7 other)
- 13 round-trip tests already exist (`test_leitura_escrita_*`)
- `idessem/dessem/__init__.py` has 43 eager import lines
- O(n^2) pd.concat in `pdo_operacao.py`

### Target State

```
idessem/
  dessem/          # Same structure, STORAGE = StorageType.BINARY, lazy imports
    modelos/       # Same files, improved type annotations, __all__ on arquivocsv
      blocos/      # Same
      arquivos/    # Same, with __all__ for re-exports
      componentes/ # Same
  libs/            # Same, type annotations improved
  config.py        # Unchanged
```

**Key improvements**:

- All `STORAGE` attributes use `StorageType` enum (1 file)
- cfinterface dependency >= 1.9.0
- All 558+ tests pass (0 failures, 0 deprecation warnings from STORAGE or set_version)
- mypy strict mode passing on all production code via per-module overrides
- Zero bare `# type: ignore` comments
- Lazy imports for dessem module (43 handlers)
- O(n) DataFrame concatenation in pdo_operacao.py
- pytest-xdist for parallel test execution
- Documented migration guide and changelog

### Key Design Decisions

1. **No TabularSection migration needed**: Like idecomp, idessem's TabelaCSV is already schema-driven. Each subclass defines `LINE_MODEL`, `COLUMN_NAMES`, and `BEGIN_PATTERN` -- this IS the schema-driven approach. Migrating to TabularSection would add complexity without reducing boilerplate.
2. **No new VERSIONS needed**: The 5 existing VERSIONS dictionaries cover known DESSEM format differences. No other format divergences have been reported.
3. **4-epic structure following idecomp pattern**: idessem is similar in scale to idecomp (~108 files vs 192 files). The proven 4-epic structure applies directly.
4. **attr-defined fix via `__all__`**: The 64 `attr-defined` errors come from 32 handler files importing `DataEstudo` and `VersaoModelo` from `arquivocsv.py`, which itself imports them from `blocos/`. Adding `__all__` to `arquivocsv.py` that explicitly re-exports these names resolves all 64 errors.
5. **Single concatenation optimization**: Unlike idecomp (6 locations in 4 files), idessem has only 1 O(n^2) concat in `pdo_operacao.py`. The other 2 `pd.concat` calls in `avl_fpha2.py` and `avl_fpha3.py` are single calls outside loops (O(1) -- not problematic).

## Technical Approach

### Tech Stack

- **Language**: Python 3.10+
- **Dependencies**: cfinterface >= 1.9.0, numpy >= 2.2.1, pandas >= 2.2.3
- **Build**: Hatchling
- **CI**: pytest + coverage, mypy, ruff, sphinx
- **Quality**: ruff (80 char line length), mypy, pytest + coverage

### Component/Module Breakdown

| Module      | Files                   | Migration Scope                                        |
| ----------- | ----------------------- | ------------------------------------------------------ |
| `dessem/`   | 43 handlers, ~46 models | 1 STORAGE migration, 5 set_version test updates, types |
| `libs/`     | 1 handler, 1 model dir  | Type annotations                                       |
| `config.py` | 1 file                  | Unchanged                                              |

### Handler File Distribution by Base Class

| Base Class   | Count  | Has VERSIONS? | Notes                               |
| ------------ | ------ | ------------- | ----------------------------------- |
| ArquivoCSV   | 28     | 5 of 28       | TabelaCSV subclass per handler      |
| RegisterFile | 9      | 0             | entdados, dessemarq, hidr, etc.     |
| BlockFile    | 7      | 0             | pdo_operacao, dessopc, operut, etc. |
| **Subtotal** | **44** |               | 43 dessem + 1 libs RegisterFile     |

Note: ArquivoCSV itself is a BlockFile subclass, so the 28 ArquivoCSV handlers are indirectly BlockFile subclasses.

### Data Flow

```
File on disk
    |
    v
cfinterface BlockFile/RegisterFile.read()
    |
    v
Block.read() / Register.read()
    |
    v
Handler properties (.tabela, .cadastro, etc.) -- convert to pd.DataFrame
    |
    v
User code (downstream consumers like sintetizador-dessem)
```

### Testing Strategy

- **Regression tests**: All 558 existing tests must pass
- **set_version migration**: Replace deprecated API in 5 test files (38 call sites)
- **Round-trip tests**: 13 already exist; ArquivoCSV handlers are read-only (no write support) so no new round-trip tests needed
- **Parallel execution**: Add pytest-xdist for development speed

## Phases and Milestones

| Epic | Name                                 | Scope                                            | Duration Estimate |
| ---- | ------------------------------------ | ------------------------------------------------ | ----------------- |
| 1    | Foundation and StorageType Migration | Bump cfinterface, migrate 1 STORAGE literal, fix | 1 week            |
| 2    | Quality and Type Safety              | mypy strict, type annotations, lazy imports      | 2-3 weeks         |
| 3    | Testing and Performance              | O(n^2) fix, pytest-xdist, benchmark              | 1-2 weeks         |
| 4    | Documentation                        | Migration guide, changelog, version bump         | 1 week            |

## Risk Analysis

| Risk                                                  | Probability | Impact | Mitigation                                                                                      |
| ----------------------------------------------------- | ----------- | ------ | ----------------------------------------------------------------------------------------------- |
| mypy strict reveals many cfinterface boundary issues  | High        | Medium | Apply idecomp/inewave proven patterns: `IO[Any]`, `# type: ignore[override]`, `Optional[Any]`   |
| attr-defined re-export issue needs different approach | Low         | Low    | `__all__` in arquivocsv.py is proven; alternative is direct imports from blocos/                |
| Downstream breakage (sintetizador-dessem)             | Low         | High   | Preserve all public property signatures and DataFrame column names; version bump with changelog |
| Test mock data incompatible after changes             | Low         | Low    | Existing tests are the primary regression gate; mock data format is not changing                |
| 1862 strict errors is a large batch                   | Medium      | Medium | Error categories match idecomp exactly; proven patterns reduce this to mechanical work          |

## Success Metrics

1. Zero `STORAGE = "BINARY"` string literals remaining
2. cfinterface dependency bumped to >= 1.9.0
3. All 558+ tests pass (0 failures, 0 deprecation warnings from STORAGE or set_version)
4. mypy strict mode passes on all production modules (via per-module overrides)
5. Zero bare `# type: ignore` comments (all have specific error codes)
6. Lazy imports for `idessem/dessem/__init__.py`
7. O(n) DataFrame concatenation in pdo_operacao.py
8. pytest-xdist installed and `pytest -n auto` works
9. Documented migration guide for downstream users
10. Package version bumped to v1.2.0
