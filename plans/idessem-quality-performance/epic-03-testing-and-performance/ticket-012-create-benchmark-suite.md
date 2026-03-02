# ticket-012 Create benchmark suite for read performance

## Context

### Background

The idessem package handles four distinct file format types through cfinterface: binary RegisterFile (e.g., `Hidr`), text RegisterFile (e.g., `Entdados`), ArquivoCSV (e.g., `PdoEcoUsih`), and BlockFile (e.g., `PdoOperacao`). After the type annotation work in epic-02 and the concatenation optimization in ticket-010, a performance benchmark baseline is needed to detect future regressions and quantify the impact of optimizations.

The project currently has no benchmarking infrastructure. The existing test mock files in `tests/mocks/arquivos/` provide representative data for each handler type and can serve as benchmark inputs.

### Relation to Epic

Epic 03 targets testing and performance improvements. This ticket creates the benchmark baseline that documents post-optimization read performance, completing the epic's third goal.

### Current State

- **No `benchmarks/` directory** exists at the repo root.
- **No benchmarking dependencies** are in `pyproject.toml`.
- **Mock data** exists in `tests/mocks/arquivos/` for all handler types:
  - `hidr.dat` -- binary file for `Hidr` (RegisterFile, binary storage)
  - `entdados.py` -- Python mock string data for `Entdados` (RegisterFile, text storage)
  - `pdo_eco_usih.py` -- Python mock string data for `PdoEcoUsih` (ArquivoCSV)
  - `pdo_operacao.py` -- Python mock string data for `PdoOperacao` (BlockFile)
- All tests use `mock_open` with these mock data strings to simulate file reads.

## Specification

### Requirements

1. Add `pytest-benchmark` to the `[project.optional-dependencies] dev` list in `pyproject.toml`.
2. Create a `benchmarks/` directory at the repo root containing a `test_read_performance.py` file with benchmark tests.
3. Create benchmarks for four representative handler reads, one for each file format type:
   - `Hidr.read()` -- binary RegisterFile (reads real file `tests/mocks/arquivos/hidr.dat`)
   - `Entdados.read()` -- text RegisterFile (uses `mock_open` with `MockEntDados` data)
   - `PdoEcoUsih.read()` -- ArquivoCSV (uses `mock_open` with `MockPdoEcoUsih` data)
   - `PdoOperacao.read()` -- BlockFile (uses `mock_open` with `MockPdoOperacao` data)
4. Each benchmark function must use `pytest-benchmark`'s `benchmark` fixture to measure read time with statistical rigor (min 5 rounds, auto-calibrated warmup).
5. Create a `benchmarks/README.md` with instructions on how to run benchmarks and interpret results.
6. Benchmarks must not be included in the regular `pytest` run. They run only when explicitly invoked.

### Inputs/Props

Each benchmark uses the same mock data that the existing tests use, ensuring reproducibility.

### Outputs/Behavior

- Running `uv run pytest benchmarks/ --benchmark-only -n 0` produces a benchmark table with min/max/mean/stddev timing for each handler read.
- Running `uv run pytest tests/` does not execute benchmarks (benchmarks are excluded from the default test path).
- Benchmark results can optionally be saved to JSON via `--benchmark-save=baseline` for future comparison.

### Error Handling

If a benchmark handler read fails, pytest-benchmark reports it as a test failure with the standard traceback. No special error handling is needed.

## Acceptance Criteria

- [ ] Given the updated `pyproject.toml`, when running `uv sync --all-extras --dev && uv run pip show pytest-benchmark`, then the package is installed and its version is printed.
- [ ] Given the benchmark file `benchmarks/test_read_performance.py`, when running `uv run pytest benchmarks/ --collect-only -n 0`, then exactly 4 test items are collected with names containing `hidr`, `entdados`, `pdo_eco_usih`, and `pdo_operacao`.
- [ ] Given the installed dependencies, when running `uv run pytest benchmarks/ --benchmark-only -n 0`, then all 4 benchmarks execute with 0 failures and pytest output contains a benchmark table with columns `min`, `max`, `mean`, `stddev`.
- [ ] Given the default test path, when running `uv run pytest tests/ --collect-only -q`, then the output contains `558 tests collected` and no benchmark tests are listed.
- [ ] Given the file `benchmarks/README.md`, when reading its contents, then it contains the command `uv run pytest benchmarks/ --benchmark-only -n 0` and a table listing all four benchmarked handlers.

## Implementation Guide

### Suggested Approach

1. Add `"pytest-benchmark"` to the dev dependencies in `/home/rogerio/git/idessem/pyproject.toml`:

```toml
dev = [
    "pytest",
    "pytest-cov",
    "pytest-xdist",
    "pytest-benchmark",
    "ruff",
    ...
]
```

2. Create directory `benchmarks/` at the repo root.

3. Create `benchmarks/__init__.py` (empty file, needed for imports).

4. Create `benchmarks/test_read_performance.py` with four benchmark functions. Follow the existing test patterns (mock_open with patch for text-based handlers, direct read for binary). Example structure:

```python
"""Benchmark suite for idessem read performance.

Run with: uv run pytest benchmarks/ --benchmark-only -n 0
"""

from unittest.mock import patch

from idessem.dessem.hidr import Hidr
from idessem.dessem.entdados import Entdados
from idessem.dessem.pdo_eco_usih import PdoEcoUsih
from idessem.dessem.pdo_operacao import PdoOperacao
from tests.mocks.mock_open import mock_open
from tests.mocks.arquivos.entdados import MockEntDados
from tests.mocks.arquivos.pdo_eco_usih import MockPdoEcoUsih
from tests.mocks.arquivos.pdo_operacao import MockPdoOperacao


HIDR_PATH = "./tests/mocks/arquivos/hidr.dat"
DUMMY_PATH = "./tests/__init__.py"


def test_read_hidr(benchmark):
    """Benchmark binary RegisterFile read (Hidr)."""
    benchmark(Hidr.read, HIDR_PATH)


def test_read_entdados(benchmark):
    """Benchmark text RegisterFile read (Entdados)."""
    m = mock_open(read_data="".join(MockEntDados))
    with patch("builtins.open", m):
        benchmark(Entdados.read, DUMMY_PATH)


def test_read_pdo_eco_usih(benchmark):
    """Benchmark ArquivoCSV read (PdoEcoUsih)."""
    m = mock_open(read_data="".join(MockPdoEcoUsih))
    with patch("builtins.open", m):
        benchmark(PdoEcoUsih.read, DUMMY_PATH)


def test_read_pdo_operacao(benchmark):
    """Benchmark BlockFile read (PdoOperacao)."""
    m = mock_open(read_data="".join(MockPdoOperacao))
    with patch("builtins.open", m):
        benchmark(PdoOperacao.read, DUMMY_PATH)
```

Note: The `mock_open` and `patch` must wrap the `benchmark()` call because `benchmark` calls the function multiple times. The mock must be set up before `benchmark()` is invoked and stay active for all iterations.

5. Create `benchmarks/README.md` with instructions for running benchmarks, saving baselines, comparing against baselines, and a table listing the four benchmarked handlers (Hidr/RegisterFile/Binary, Entdados/RegisterFile/Text, PdoEcoUsih/ArquivoCSV/Text-CSV, PdoOperacao/BlockFile/Text).

6. Run `uv sync --all-extras --dev` to install `pytest-benchmark`.
7. Run `uv run pytest benchmarks/ --benchmark-only -n 0` to verify all four benchmarks pass and produce output.
8. Run `uv run pytest tests/` to verify benchmarks are not collected in the regular test run.

### Key Files to Modify

- `/home/rogerio/git/idessem/pyproject.toml` -- add `pytest-benchmark` to dev dependencies
- `/home/rogerio/git/idessem/benchmarks/__init__.py` -- new empty file
- `/home/rogerio/git/idessem/benchmarks/test_read_performance.py` -- new benchmark file
- `/home/rogerio/git/idessem/benchmarks/README.md` -- new documentation file

### Patterns to Follow

Follow the same mock data usage patterns as existing tests in `tests/dessem/`. Specifically:

- Use `mock_open(read_data="".join(MockXxx))` with `patch("builtins.open", m)` for text-based handlers.
- Use direct `Hidr.read(path)` for the binary handler (same as `tests/dessem/test_hidr.py`).

### Pitfalls to Avoid

- Do not add benchmarks to the `tests/` directory. They must be in a separate `benchmarks/` directory to avoid being collected by the default `uv run pytest tests/` invocation.
- Do not run benchmarks with `-n auto` (pytest-xdist parallelism). Benchmark accuracy requires sequential, single-process execution. Use `-n 0` to disable xdist.
- Do not use `pedantic` mode for the initial baseline -- standard `benchmark()` with default calibration is sufficient.
- The `mock_open` context manager must wrap the `benchmark()` call, not be called inside the benchmarked function, because `benchmark()` invokes the function multiple times and the mock must persist across all iterations.

## Testing Requirements

### Unit Tests

No unit tests needed for the benchmark suite itself. The benchmarks are validated by running them and confirming they produce timing output without errors.

### Integration Tests

Verify that `uv run pytest benchmarks/ --benchmark-only -n 0` runs all four benchmarks and exits with code 0.

### E2E Tests

Not applicable.

## Dependencies

- **Blocked By**: ticket-010-optimize-dataframe-concatenation.md (benchmark should measure post-optimization performance)
- **Blocks**: None

## Effort Estimate

**Points**: 2
**Confidence**: High
