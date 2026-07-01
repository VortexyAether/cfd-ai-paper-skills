# Generic Review to CFD Review

## Generic review

The paper is interesting and the method appears promising. The authors should add more baselines, describe the data better, and improve the figures. Some claims are too strong.

## CFD review

### Fatal / major issues

| Severity | Issue | Required fix |
|---|---|---|
| Fatal | The manuscript claims Reynolds-number generalization but uses a random snapshot split. | Redesign split by unseen Re and report train/val/test regimes. |
| Major | Boundary conditions, domain size, mesh resolution, timestep, CFL, and solver tolerances are missing. | Add a reproducibility table and solver/config commands or supplementary dictionaries. |
| Major | Only RMSE is reported for turbulent fields. | Add vorticity spectra, energy/enstrophy or relevant force/pressure diagnostics. |
| Major | The neural operator is compared only with a small CNN. | Add FNO/DeepONet or task-appropriate neural baseline plus a classical ROM/interpolation baseline. |
| Major | "Physically consistent" is claimed without residual or conservation evidence. | Report divergence/momentum residual, BC violation, or conservation diagnostics. |

### Claim wording fix

| Original | Safer wording |
|---|---|
| The model generalizes to turbulent flows. | The model interpolates within the tested Reynolds-number range and shows preliminary extrapolation behavior under the specified cylinder-wake setup. |

### Required experiments

1. Leakage-safe split across Re/time/geometry as claimed.
2. GT/pred/error fields with shared color scales.
3. Physical diagnostics beyond pointwise error.
4. Baseline matrix with same data and metrics.
5. Failure case or OOD boundary.

