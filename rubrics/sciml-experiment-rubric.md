# SciML Experiment Rubric

Use for neural operators, PINNs, surrogates, ROMs, closure models, reconstruction, control, and discovery papers.

| Axis | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| Baselines | None | Weak/generic | Relevant but incomplete | Classical + ML baselines, same data/splits/metrics |
| Splits | Missing | Random only | One meaningful holdout | Leakage-safe unseen time/parameter/geometry/BC as claimed |
| Metrics | RMSE only or missing | Generic ML metrics | Task metric + one physics metric | ML metrics, physical diagnostics, uncertainty/variance |
| Ablations | None | Cosmetic | Tests main component | Mechanism-revealing ablations with failure expectation |
| Robustness | None | Noise only | One stress test | Noise/sparsity/OOD/long rollout/failure boundary |
| Uncertainty | Claimed only | Error bars vague | Multiple seeds or intervals | Calibrated uncertainty/error bars tied to decisions |
| Efficiency | Missing | Speedup claim only | Timing reported | Hardware, wall-clock, memory, parameter count, fair comparison |

## Minimum publishable matrix

1. Main task comparison against relevant baselines.
2. Leakage-safe generalization split matching the claim.
3. Physical diagnostic beyond pointwise error.
4. Ablation for every claimed mechanism.
5. Failure/limitation case.

