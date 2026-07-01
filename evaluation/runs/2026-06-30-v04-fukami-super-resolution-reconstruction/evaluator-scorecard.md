# Evaluator Scorecard

## Verdict

fail

## Rubric table

| Axis | Score 0-3 | Evidence | Fix |
|---|---:|---|---|
| Gold-paper alignment | 1 | Mentions SR but misses spatio-temporal extension and three-case stack. | Skill must force spatial and temporal sparsity separation. |
| Physics specificity | 1 | Says "turbulence" but omits cylinder wake Re_D = 100 and channel Re_tau = 180. | Require named flow cases/regimes from gold note when available. |
| Experiment stack | 1 | Generic "show images/error" only. | Require cylinder sanity case, 2D turbulence statistics, 3D channel stress test, training/frame-interval sensitivity. |
| Figure grammar | 1 | No GT/coarse/pred/error or time-axis figure rule. | Add spatio-temporal figure checklist. |
| Reviewer-defense realism | 1 | Generic baselines/generalization only. | Add downsampling protocol, temporal interval, and turbulence-statistics attacks. |
| Unknown/TODO discipline | 2 | Does not invent solver settings. | Keep; add more unknown categories. |
| Output schema compliance | 2 | Usable but too shallow. | Add required confidence labels. |

Average: 1.29

## Blocking failures

- Missed the temporal-inbetweening part of the task.
- Missed the three-level evidence stack.
- Did not require frame interval or temporal two-point correlation evidence.

