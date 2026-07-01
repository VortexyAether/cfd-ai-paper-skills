# CFD-AI Skill Scorecard

Score 0–3.

| Criterion | Score | Evidence | Notes |
|---|---:|---|---|
| Physics specificity |  |  |  |
| Numerical reproducibility |  |  |  |
| Claim-evidence alignment |  |  |  |
| Baseline fairness |  |  |  |
| Physical diagnostics |  |  |  |
| Generalization reasoning |  |  |  |
| Reviewer realism |  |  |  |
| Gold-paper alignment |  |  |  |
| Output schema compliance |  |  |  |
| Non-hallucination / unknown marking |  |  |  |
| Actionability |  |  |  |

## Pass thresholds

- MVP: average ≥ 2.2
- Strong: average ≥ 2.6
- Release: average ≥ 2.8 and no hallucination score below 2

## Fatal failure flags

- Invents solver/data details.
- Claims citation support without source.
- Misses train/test leakage in a task where it is central.
- Uses only generic writing advice.
