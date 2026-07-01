# A/B Skill Improvement Loop

## Goal

Keep skill improvements only when they improve benchmark behavior, reduce hallucination, or make output shorter without losing critical CFD evidence.

## Roles

| Agent | Variant | Input |
|---|---|---|
| Baseline Agent A | Current skill | Same task and source limits |
| Baseline Agent B | Patched skill | Same task and source limits |
| Evaluator | Blind comparison | Outputs A and B, gold file, rubrics |
| Evaluator Integrator | Final decision | Evaluator score and diff |

## Procedure

1. Select one benchmark task from `evaluation/evals.json`.
2. Freeze source access: abstract-only, gold-note-only, or full-PDF, as declared.
3. Run Agent A and Agent B independently.
4. Evaluator scores both with the same rubrics.
5. Keep the patch only if:
   - average score improves by at least 0.2, or
   - a critical hallucination is removed, or
   - output is materially shorter while preserving all critical risks.
6. Save artifacts under `evaluation/runs/YYYY-MM-DD_task-id/`.

## Required run artifacts

```text
prompt.md
source-scope.md
skill-A.md
skill-B.md
baseline-output-A.md
baseline-output-B.md
evaluator-scorecard.md
evaluator-decision.md
patched-skill-diff.md
```

## Decision record

| Field | Required |
|---|---|
| Benchmark failure | What failed before patch |
| Patch hypothesis | Why this skill edit should help |
| A score / B score | Per-axis table |
| Hallucination delta | worse / same / better |
| Decision | keep / reject / revise |

