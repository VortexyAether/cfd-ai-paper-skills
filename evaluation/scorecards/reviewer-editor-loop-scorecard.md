# Reviewer-Editor Loop Scorecard

Use for `paper-revision-loop-manager` benchmark outputs.

| Axis | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| Reviewer gate | none | vague | Fatal/Major labels | gate + blocker count + exact claim links |
| Editor rewrite | none | polish only | safer wording | evidence-bounded, field-native rewrite |
| Traceability | none | implicit | most issues addressed | every Fatal/Major issue mapped to edit/TODO/artifact |
| Re-audit | none | generic | before/after risk | residual blockers + new overclaim check |
| Claim calibration | loaded claims remain | softened | mostly bounded | scoped to evidence with limitation boundary |
| Action plan | none | vague validation | concrete fixes | prioritized experiments/tables/figures by claim rescued |
| Non-hallucination | invents details | unsupported assumptions | mostly scoped | all hidden facts TODO |

Pass threshold: average >= 2.5 and no invented solver/data/metric/citation/runtime details.
