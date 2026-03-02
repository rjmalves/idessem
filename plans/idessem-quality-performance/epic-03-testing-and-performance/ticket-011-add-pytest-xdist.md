# ticket-011 Add pytest-xdist and optimize test execution

## Context

### Background

The idessem test suite contains 558 tests that run sequentially in approximately 10.5 seconds. Adding `pytest-xdist` enables parallel test execution with `pytest -n auto`, which distributes tests across CPU cores to reduce wall-clock time. This improves the developer feedback loop during development and potentially reduces CI run time.

The test suite is a good candidate for parallelism because:

- All `set_version` class-level state mutations were removed in epic-01 (ticket-003). No `set_version` calls remain in tests.
- No test classes, `setUpClass`, `@classmethod` fixtures, or session/module-scoped fixtures exist.
- All filesystem writes in tests go through `mock_open` / `patch("builtins.open")` -- no actual filesystem mutation occurs.
- The only real file read is `tests/mocks/arquivos/hidr.dat` (a binary file), which is read-only and safe for concurrent access.
- Tests are pure functions with no shared mutable state.

### Relation to Epic

Epic 03 targets testing and performance improvements. This ticket optimizes the test execution infrastructure, complementing the code-level optimization in ticket-010.

### Current State

- **`pyproject.toml`**: dev dependencies include `pytest` and `pytest-cov` but not `pytest-xdist`.
- **`.github/workflows/main.yml`**: runs `uv run pytest --cov-report=xml --cov=idessem ./tests` without `-n` flag.
- **No `conftest.py`** exists at any level in the test tree.
- **No `pytest.ini_options`** section exists in `pyproject.toml`.
- CI runs on `ubuntu-latest` with a matrix of Python 3.10, 3.11, 3.12.

## Specification

### Requirements

1. Add `pytest-xdist` to the `[project.optional-dependencies] dev` list in `pyproject.toml`.
2. Add a `[tool.pytest.ini_options]` section in `pyproject.toml` with `addopts = "-n auto"` so that parallel execution is the default for both local and CI runs.
3. Verify that all 558 tests pass under `pytest -n auto` with no failures, no warnings related to shared state, and no test ordering dependencies.

### Inputs/Props

Not applicable (infrastructure change).

### Outputs/Behavior

- `uv run pytest -n auto` executes all tests in parallel across available CPU cores and all pass.
- `uv run pytest -n 0` falls back to sequential execution (xdist default behavior) and all pass.
- CI workflow continues to pass with the updated configuration.

### Error Handling

Not applicable. If any test fails under parallel execution, it indicates a shared-state bug that must be investigated and fixed before this ticket is considered complete.

## Acceptance Criteria

- [ ] Given the file `/home/rogerio/git/idessem/pyproject.toml`, when reading the `[project.optional-dependencies] dev` list, then `"pytest-xdist"` is present as an entry.
- [ ] Given the file `/home/rogerio/git/idessem/pyproject.toml`, when reading the `[tool.pytest.ini_options]` section, then `addopts` contains `"-n auto"`.
- [ ] Given the updated `pyproject.toml`, when running `uv sync --all-extras --dev && uv run pytest -n auto`, then all 558 tests pass with 0 failures.
- [ ] Given the updated `pyproject.toml`, when running `uv run pytest -n 0`, then all 558 tests pass with 0 failures (sequential fallback works).
- [ ] Given the file `/home/rogerio/git/idessem/pyproject.toml`, when running `uv run ruff check idessem/`, then ruff reports 0 violations (no regressions).

## Implementation Guide

### Suggested Approach

1. Open `/home/rogerio/git/idessem/pyproject.toml`.
2. In the `[project.optional-dependencies]` section, add `"pytest-xdist"` to the `dev` list. Place it after `"pytest-cov"` to keep the pytest-related deps grouped:

```toml
dev = [
    "pytest",
    "pytest-cov",
    "pytest-xdist",
    "ruff",
    "mypy",
    ...
]
```

3. Add a `[tool.pytest.ini_options]` section to `pyproject.toml`:

```toml
[tool.pytest.ini_options]
addopts = "-n auto"
```

4. Run `uv sync --all-extras --dev` to install the new dependency.
5. Run `uv run pytest` (which now defaults to `-n auto` via addopts) and verify all 558 tests pass.
6. Run `uv run pytest -n 0` to verify sequential fallback works.
7. No CI workflow changes are needed -- the `addopts` in `pyproject.toml` automatically applies `-n auto` to the existing `uv run pytest ...` command in `.github/workflows/main.yml`.

### Key Files to Modify

- `/home/rogerio/git/idessem/pyproject.toml` -- add `pytest-xdist` to dev deps and add `[tool.pytest.ini_options]` section

### Patterns to Follow

The project already uses `pyproject.toml` for all tool configuration (ruff, mypy, hatch). Adding pytest config here follows the same single-file convention.

### Pitfalls to Avoid

- Do not modify `.github/workflows/main.yml`. The `addopts` setting in `pyproject.toml` will automatically apply to the pytest invocation in CI. The CI already uses `uv run pytest --cov-report=xml --cov=idessem ./tests`, and `-n auto` will be prepended from addopts.
- Do not add `--dist loadscope` or `--dist loadfile` unless tests fail with the default `load` distribution. The default `load` strategy gives the best parallelism for independent function-level tests.
- Do not create a `conftest.py` unless a test actually fails due to missing fixture isolation. The current test suite has no shared state.
- Ensure `pytest-xdist` is compatible with `pytest-cov`. When using xdist, pytest-cov automatically handles coverage merging from workers, but verify coverage output is still produced.

## Testing Requirements

### Unit Tests

No new test files needed. The validation is running the existing 558 tests under `pytest -n auto` and confirming they all pass.

### Integration Tests

Verify that `pytest-cov` still produces coverage output when running with `-n auto` by checking that `coverage.xml` is generated after `uv run pytest --cov-report=xml --cov=idessem ./tests`.

### E2E Tests

Not applicable.

## Dependencies

- **Blocked By**: ticket-003-migrate-set-version-verify-suite.md (completed -- set_version class state mutation is gone)
- **Blocks**: None

## Effort Estimate

**Points**: 1
**Confidence**: High
