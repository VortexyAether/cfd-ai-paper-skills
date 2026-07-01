# Weak to Publishable Experiment Plan

## Weak plan

Train a neural operator on CFD snapshots and compare RMSE with a baseline. Show some velocity plots. Test on held-out data.

## Publishable plan

### Claim

The neural operator predicts unsteady incompressible flow over a cylinder across Reynolds-number regimes with stable rollout and physically meaningful diagnostics.

### Split design

| Split | Purpose |
|---|---|
| Train | Re = 100, 200, 300, 400 time windows |
| Validation | Later windows from trained Re values, no overlapping rollout starts |
| Test-interpolation | Re = 250 or 350 if available |
| Test-extrapolation | Re = 500; Re = 3000 only if solver/data regime is clearly justified |
| Rollout | Multi-step prediction over at least several shedding periods |

### Baselines

| Baseline | Why |
|---|---|
| Persistence / previous snapshot | Minimum sanity baseline |
| DMD/POD-ROM | Classical reduced-order comparator |
| FNO or DeepONet | Neural-operator comparator |
| CNN/U-Net sequence model | Direct image-to-image comparator |

### Metrics

- Relative L2 and MAE for velocity/pressure/vorticity.
- Drag/lift coefficient time histories if force data are available.
- Divergence or mass-conservation residual.
- Vorticity spectrum or shedding frequency/Strouhal number.
- Runtime, memory, parameter count, hardware.

### Ablations

| Ablation | Tests |
|---|---|
| Remove physics loss | Whether conservation term matters |
| Remove coordinate/geometry encoding | Whether model handles domain structure |
| Reduce training Re values | Data efficiency and interpolation sensitivity |
| Longer rollout | Error accumulation and stability |

### Failure cases

Report where rollout phase drifts, wake frequency shifts, or OOD Re produces nonphysical residuals.

