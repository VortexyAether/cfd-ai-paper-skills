---
title: Experiment matrices for CFD-AI papers
created: 2026-06-30
updated: 2026-06-30
status: v0.3
tags:
  - cfd-ai
  - experiments
  - sciml
---

# Experiment Matrices

Use with `rubrics/sciml-experiment-rubric.md` and `templates/experiment-plan.md`.

## Reconstruction / super-resolution

| Axis | Minimum |
|---|---|
| Baselines | Bicubic/interpolation, CNN/U-Net, task-relevant learned baseline |
| Splits | unseen time snapshots plus any claimed unseen Re/geometry |
| Metrics | relative L2/MAE, error maps, spectrum/PDF/statistics |
| Stress tests | coarsening factor, sensor sparsity, noise |
| Failure | OOD regime or high-frequency breakdown |

## Neural operator / surrogate

| Axis | Minimum |
|---|---|
| Baselines | FNO/DeepONet/GNN where relevant, POD/DMD/ROM when appropriate |
| Splits | unseen parameter/Re/geometry/BC matching claim |
| Metrics | field error, rollout stability, conservation/residual, runtime |
| Stress tests | long horizon, mesh/resolution transfer, noise/OOD |
| Failure | parameter range where prediction degrades |

## PINN / physics-constrained model

| Axis | Minimum |
|---|---|
| Baselines | numerical solver, non-physics network, classical inverse/data-assimilation method |
| Splits | sparse/noisy sensors or unseen conditions if claimed |
| Metrics | residual, BC/IC violation, field error, compute |
| Stress tests | collocation density, noise, stiffness/regime difficulty |
| Failure | residual convergence or boundary failure case |

## Turbulence closure

| Axis | Minimum |
|---|---|
| Baselines | classical closure, tensor-basis or ML closure if relevant |
| Splits | a priori and a posteriori, unseen flow/regime |
| Metrics | mean profiles, stresses, spectra, stability, wall/friction quantities |
| Stress tests | long-time stability and mesh sensitivity |
| Failure | closure instability or poor extrapolation |

