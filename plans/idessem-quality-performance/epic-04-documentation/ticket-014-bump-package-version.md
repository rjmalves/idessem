# ticket-014 Bump package version to v1.2.0

## Context

### Background

All code changes for the idessem v1.2.0 release are complete (epics 01-03) and the migration guide and changelog have been written (ticket-013). The final step before release is to bump the version number and remove the local development override for cfinterface that was added during development.

### Relation to Epic

This is the last ticket in Epic 04 (Documentation) and the last ticket in the entire plan. It makes the version metadata consistent with the documented v1.2.0 release. After this ticket, the repository is ready for a GitHub release tag.

### Current State

- `/home/rogerio/git/idessem/idessem/__init__.py` line 9 declares `__version__ = "1.1.0"`
- `/home/rogerio/git/idessem/pyproject.toml` uses `[tool.hatch.version] path = "idessem/__init__.py"` to read the version dynamically -- Hatch reads it from `__init__.py`, so only one file needs updating
- `/home/rogerio/git/idessem/docs/source/conf.py` imports `__version__` from the package at line 22 (`from idessem import __version__`) and sets `release = __version__` at line 32 -- this auto-updates when `__init__.py` changes
- `/home/rogerio/git/idessem/pyproject.toml` lines 106-108 contain a `[tool.uv.sources]` section with `cfinterface = { path = "/home/rogerio/git/cfinterface" }` that overrides the PyPI dependency with a local path. This was needed during development but must be removed before release, as it would cause build failures for other users.
- No other files in the repository hardcode the version string `1.1.0` (confirmed by grep).
- CI workflows (`.github/workflows/main.yml`, `publish.yml`, `docs.yml`) do not reference the version string.

## Specification

### Requirements

1. Change `__version__ = "1.1.0"` to `__version__ = "1.2.0"` in `/home/rogerio/git/idessem/idessem/__init__.py` on line 9.
2. Remove the `[tool.uv.sources]` section (lines 106-108) from `/home/rogerio/git/idessem/pyproject.toml`. This section contains:
   ```toml
   # Remove this override once cfinterface 1.9.0 is published to PyPI
   [tool.uv.sources]
   cfinterface = { path = "/home/rogerio/git/cfinterface" }
   ```
3. Verify that `hatch version` reports `1.2.0` after the change.

### Inputs/Props

Not applicable -- this ticket modifies existing configuration values.

### Outputs/Behavior

After this ticket:

- `python -c "import idessem; print(idessem.__version__)"` prints `1.2.0`
- `hatch version` (or `uv run hatch version`) reports `1.2.0`
- `pyproject.toml` has no `[tool.uv.sources]` section
- Sphinx documentation build reads `release = "1.2.0"` automatically via the `conf.py` import

### Error Handling

Not applicable -- this ticket modifies static configuration values.

## Acceptance Criteria

- [ ] Given `/home/rogerio/git/idessem/idessem/__init__.py`, when reading line 9, then it contains `__version__ = "1.2.0"`
- [ ] Given `/home/rogerio/git/idessem/pyproject.toml`, when searching for `[tool.uv.sources]`, then no match is found
- [ ] Given `/home/rogerio/git/idessem/pyproject.toml`, when searching for the comment `# Remove this override`, then no match is found
- [ ] Given the installed package, when running `python -c "import idessem; print(idessem.__version__)"`, then the output is `1.2.0`

## Implementation Guide

### Suggested Approach

1. Open `/home/rogerio/git/idessem/idessem/__init__.py` and change line 9 from:

   ```python
   __version__ = "1.1.0"
   ```

   to:

   ```python
   __version__ = "1.2.0"
   ```

2. Open `/home/rogerio/git/idessem/pyproject.toml` and delete lines 106-108 (the comment and the `[tool.uv.sources]` section):

   ```toml
   # Remove this override once cfinterface 1.9.0 is published to PyPI
   [tool.uv.sources]
   cfinterface = { path = "/home/rogerio/git/cfinterface" }
   ```

   After deletion, the file should end at the `[tool.pytest.ini_options]` section (line 103-104).

3. Verify the version by running:
   ```bash
   cd /home/rogerio/git/idessem
   python -c "import idessem; print(idessem.__version__)"
   ```
   Expected output: `1.2.0`

### Key Files to Modify

- **Edit**: `/home/rogerio/git/idessem/idessem/__init__.py` (line 9 -- version string)
- **Edit**: `/home/rogerio/git/idessem/pyproject.toml` (remove lines 106-108 -- uv.sources override)

### Patterns to Follow

- The version string format is `"X.Y.Z"` with double quotes, matching PEP 440 and the existing format in `__init__.py`
- Hatch reads the version from `__init__.py` via the `[tool.hatch.version]` config -- do not add a static `version =` field to `[project]` in pyproject.toml

### Pitfalls to Avoid

- Do NOT add a `version = "1.2.0"` field to `[project]` in pyproject.toml -- the version is `dynamic = ["version"]` and read from `__init__.py` by Hatch
- Do NOT modify `/home/rogerio/git/idessem/docs/source/conf.py` -- it auto-reads the version via `from idessem import __version__`
- Do NOT leave the `[tool.uv.sources]` section in pyproject.toml -- it points to a local path (`/home/rogerio/git/cfinterface`) that does not exist on other machines and would cause `uv sync` to fail for other developers
- Do NOT remove the `[tool.pytest.ini_options]` section -- only remove the `[tool.uv.sources]` section below it

## Testing Requirements

### Unit Tests

Not applicable -- this ticket modifies version metadata only. Existing tests will continue to pass.

### Integration Tests

Run the full test suite after the change to confirm nothing breaks:

```bash
cd /home/rogerio/git/idessem && uv run pytest ./tests -x
```

### E2E Tests

Not applicable.

## Dependencies

- **Blocked By**: ticket-013-write-migration-guide-changelog.md
- **Blocks**: None (last ticket in the plan)

## Effort Estimate

**Points**: 1
**Confidence**: High
