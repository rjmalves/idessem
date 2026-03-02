# Epic 03: Testing and Performance

## Goals

1. Optimize O(n^2) DataFrame concatenation in `pdo_operacao.py`
2. Add pytest-xdist for parallel test execution
3. Create a benchmark baseline for read performance

## Scope

- **In scope**: Concatenation optimization, parallel testing, benchmark baseline
- **Out of scope**: New handler implementations, API changes, documentation, new round-trip tests (13 already exist and ArquivoCSV handlers are read-only)

## Tickets

| Ticket     | Title                                            | Points |
| ---------- | ------------------------------------------------ | ------ |
| ticket-010 | Optimize DataFrame concatenation in pdo_operacao | 2      |
| ticket-011 | Add pytest-xdist and optimize test execution     | 2      |
| ticket-012 | Create benchmark suite for read performance      | 2      |

## Success Criteria

- `pdo_operacao.py` uses collect-then-concat pattern (no O(n^2) loop)
- `pytest -n auto` runs successfully
- Benchmark baseline documented in `benchmarks/`
