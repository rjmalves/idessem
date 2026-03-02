# ticket-011 Add pytest-xdist and optimize test execution

> **[OUTLINE]** This ticket requires refinement before execution.
> It will be refined with learnings from earlier epics.

## Objective

Add `pytest-xdist` as a dev dependency and configure parallel test execution so `pytest -n auto` works correctly. This improves developer feedback loop and CI run time. The 558 tests currently run in ~10.5 seconds sequentially; parallel execution should reduce this.

## Anticipated Scope

- **Files likely to be modified**: `/home/rogerio/git/idessem/pyproject.toml` (add pytest-xdist to dev dependencies), `/home/rogerio/git/idessem/.github/workflows/main.yml` (optionally add `-n auto` to pytest invocation)
- **Key decisions needed**: Whether to enable `-n auto` in CI by default or only locally (CI may have single-core runners where parallel overhead is counterproductive)
- **Open questions**:
  - Do any tests have shared mutable state that breaks under parallel execution (e.g., class-level `set_version` calls that mutate class state)?
  - After epic-01's set_version migration, are there still any tests that mutate class-level state?

## Dependencies

- **Blocked By**: ticket-003-migrate-set-version-verify-suite.md (set_version class state mutation must be gone)
- **Blocks**: None

## Effort Estimate

**Points**: 2
**Confidence**: Low (will be re-estimated during refinement)
