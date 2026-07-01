# Claim-Evidence Rubric

Use this 0-3 rubric to score each major manuscript claim. Unsupported facts become `unknown/TODO`, not invented evidence.

| Score | Descriptor | Evaluator test |
|---|---|---|
| 0 | Unsupported or contradicted | No cited evidence, or evidence points against the claim. |
| 1 | Weak / partial | Evidence exists but is generic, incomplete, or mismatched to claim strength. |
| 2 | Supported with scope limits | Evidence supports the claim under named conditions; limits are explicit. |
| 3 | Strongly supported | Multiple direct evidence types support the claim, with assumptions and limitations stated. |

## Axes

| Axis | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| Novelty | No contrast | Vague contrast | Specific prior-art gap | Gap plus exact contribution boundary |
| Accuracy | No metric | Single weak metric | Fair metric/baseline | Fair metric, baseline, uncertainty/error bars |
| Physical consistency | Not checked | Visual only | One diagnostic | Residual/conservation/spectrum/forces as relevant |
| Generalization | Claimed only | Random split | One unseen regime | Unseen regime plus failure boundary |
| Efficiency | Claimed only | Timing vague | Hardware/timing stated | Hardware, runtime, memory, parameter count, comparison |
| Limitation honesty | Missing | Generic | Specific limitation | Limitation tied to evidence and future test |

## Output line

`Claim | Score | Evidence | Missing evidence | Safer wording | Required experiment/TODO`

