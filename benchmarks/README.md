# idessem Benchmarks

## Benchmarked Handlers

| Handler     | File Type    | Storage | Mock Source                            |
| ----------- | ------------ | ------- | -------------------------------------- |
| Hidr        | RegisterFile | Binary  | `tests/mocks/arquivos/hidr.dat`        |
| Entdados    | RegisterFile | Text    | `tests/mocks/arquivos/entdados.py`     |
| PdoEcoUsih  | ArquivoCSV   | CSV     | `tests/mocks/arquivos/pdo_eco_usih.py` |
| PdoOperacao | BlockFile    | Text    | `tests/mocks/arquivos/pdo_operacao.py` |

## Running Benchmarks

Run all benchmarks:

```bash
uv run pytest benchmarks/ --benchmark-only -n 0
```

Save results as a baseline:

```bash
uv run pytest benchmarks/ --benchmark-only -n 0 --benchmark-save=baseline
```

Compare against a saved baseline:

```bash
uv run pytest benchmarks/ --benchmark-only -n 0 --benchmark-compare=0001_baseline
```

## Notes

- Always use `-n 0` to disable pytest-xdist parallelism. Benchmarks require sequential, single-process execution for accurate timing.
- Benchmark results include min, max, mean, and stddev columns.
- The `Hidr` benchmark reads a real binary file; the others use `mock_open` with mock data strings from the test fixtures.
