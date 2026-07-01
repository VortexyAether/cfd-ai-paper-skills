# Evaluator Scorecard

## Verdict

fail

## Rubric table

| Axis | Score 0-3 | Evidence | Fix |
|---|---:|---|---|
| Physics specificity | 1 | "Describe data" does not name Re, domain, BC/IC, mesh, timestep, CFL, solver. | Reviewer skill must require cylinder-wake reproducibility fields explicitly. |
| Evidence alignment | 1 | Does not require conservation residuals, rollout horizon, GT/pred/error with same scales. | Add wake-specific evidence checklist. |
| Reviewer realism | 1 | "Add more baselines" is generic. | Name persistence/POD-DMD/CNN/GAN/physics-loss variants as task-appropriate. |
| Gold-paper alignment | 1 | Misses Lee 2019 Re split and Lee 2021 mechanism analysis. | Progressive disclosure should mention both Lee gold files. |
| Output schema | 2 | Table is readable. | Add fatal/major/minor plus score columns. |
| Non-hallucination | 3 | No invented details. | Keep. |
| Actionability | 1 | Fixes are too vague. | Require exact missing fields and pass conditions. |

Average: 1.43

## Blocking failures

- Generic critique missed fatal CFD reproducibility risks.
- Did not attack generalization through unseen Re/regime and rollout horizon.
- Did not ask where physical consistency enters: loss, residual, or diagnostic.

