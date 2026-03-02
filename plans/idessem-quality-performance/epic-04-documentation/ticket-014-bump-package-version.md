# ticket-014 Bump package version to v1.2.0

> **[OUTLINE]** This ticket requires refinement before execution.
> It will be refined with learnings from earlier epics.

## Objective

Update the package version from `1.1.0` to `1.2.0` in `idessem/__init__.py` and verify all metadata is consistent. This is the final step before release.

## Anticipated Scope

- **Files likely to be modified**: `/home/rogerio/git/idessem/idessem/__init__.py` (line 9: `__version__`)
- **Key decisions needed**: Whether to also update any version references in documentation or CI configuration
- **Open questions**:
  - Are there any other files that reference the version string besides `__init__.py`?
  - Should the `[tool.uv.sources]` local override added in ticket-001 be removed before the version bump?

## Dependencies

- **Blocked By**: ticket-013-write-migration-guide-changelog.md
- **Blocks**: None (last ticket in the plan)

## Effort Estimate

**Points**: 1
**Confidence**: Low (will be re-estimated during refinement)
