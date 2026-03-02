# ticket-012 Create benchmark suite for read performance

> **[OUTLINE]** This ticket requires refinement before execution.
> It will be refined with learnings from earlier epics.

## Objective

Create a benchmark suite that measures read performance for representative handlers (binary RegisterFile `Hidr`, text RegisterFile `Entdados`, ArquivoCSV `PdoEcoUsih`, BlockFile `PdoOperacao`). This establishes a baseline for future optimization work and verifies that the type annotation changes from epic-02 did not introduce performance regressions.

## Anticipated Scope

- **Files likely to be modified**: New directory `benchmarks/` at repo root with benchmark scripts, potentially `pyproject.toml` if a benchmarking dependency is added (e.g., `pytest-benchmark`)
- **Key decisions needed**: Whether to use `pytest-benchmark`, raw `timeit`, or a custom script for benchmarking
- **Open questions**:
  - Which mock data files are suitable for benchmarking (need to be representative of production file sizes)?
  - Should the benchmark suite be integrated into CI or remain a local developer tool?

## Dependencies

- **Blocked By**: ticket-010-optimize-dataframe-concatenation.md (benchmark should measure post-optimization performance)
- **Blocks**: None

## Effort Estimate

**Points**: 2
**Confidence**: Low (will be re-estimated during refinement)
