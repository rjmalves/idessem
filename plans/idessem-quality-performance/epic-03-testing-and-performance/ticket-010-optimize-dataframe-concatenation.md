# ticket-010 Optimize DataFrame concatenation in pdo_operacao

> **[OUTLINE]** This ticket requires refinement before execution.
> It will be refined with learnings from earlier epics.

## Objective

Replace the O(n^2) `pd.concat([df, df_estagio])` loop in `PdoOperacao.__concatena_blocos()` with the O(n) collect-then-concat pattern. This is the only performance-critical DataFrame concatenation anti-pattern in idessem (the other two `pd.concat` calls in `avl_fpha2.py` and `avl_fpha3.py` are single calls outside loops).

## Anticipated Scope

- **Files likely to be modified**: `/home/rogerio/git/idessem/idessem/dessem/pdo_operacao.py` (the `__concatena_blocos` method, lines 38-57)
- **Key decisions needed**: Whether to extract the collect-then-concat pattern into a shared helper used by future similar methods, or keep it inline (idecomp kept it inline since each implementation has slightly different logic)
- **Open questions**:
  - Are there any other hidden O(n^2) concat patterns in model files under `modelos/` that were not caught by the initial grep?
  - Does the type annotation work from epic-02 change the method signature in a way that affects the refactor?

## Dependencies

- **Blocked By**: ticket-006-enable-mypy-strict-dessem.md (type annotations must be in place)
- **Blocks**: ticket-012-create-benchmark-suite.md

## Effort Estimate

**Points**: 2
**Confidence**: Low (will be re-estimated during refinement)
