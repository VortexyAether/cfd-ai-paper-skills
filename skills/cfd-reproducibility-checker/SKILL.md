---
name: cfd-reproducibility-checker
description: Use when auditing CFD-AI/SciML papers for reproducibility: governing equations, nondimensional numbers, geometry, mesh, boundary conditions, solver settings, datasets, splits, baselines, hyperparameters, compute, and exact commands.
version: 0.4.0
author: VA + TARS
metadata:
  short-description: CFD reproducibility audit for AI/ML manuscripts
---

# CFD Reproducibility Checker

## Trigger

Use when a manuscript reports CFD simulations, CFD-generated datasets, neural surrogates, PINNs, closure models, or flow-control experiments and needs reproducibility review.

## Progressive disclosure

- Read `rubrics/cfd-reproducibility-rubric.md` before scoring.
- For reconstruction/super-resolution, read `references/gold-papers/fukami-2019-super-resolution-jfm.md`.
- For spatio-temporal super-resolution, read `references/gold-papers/fukami-2021-spatiotemporal-super-resolution-jfm.md`.
- For cylinder-wake prediction, read `references/gold-papers/lee-2019-cylinder-wake-jfm.md`.
- For uncertainty-aware surrogate/data recovery, read `references/gold-papers/maulik-2020-probabilistic-neural-networks-prf.md`.
- For flow-control/DRL, read `references/gold-papers/vinuesa-2023-drl-drag-reduction-epje.md`.

## Checklist

### Physics setup

- governing equations
- assumptions
- nondimensional numbers: Re/Ma/Pr/Pe/Ra/etc.
- geometry and coordinate system
- IC/BC
- forcing/source terms

### Numerical setup

- solver/software/version
- discretization scheme
- mesh type/resolution/quality
- time step/CFL
- convergence criteria
- turbulence model or DNS/LES/RANS/LBM/FEM/FVM label
- averaging window
- validation benchmark

### ML setup

- dataset provenance
- train/val/test split
- leakage across time/Re/geometry/BC
- preprocessing/normalization
- architecture/hyperparameters
- seeds/runs
- compute/hardware/runtime

### Task-specific additions

| Task | Extra reproducibility fields |
|---|---|
| Spatio-temporal SR | Spatial downsampling factor, temporal frame interval, input/output variables, reference-resolution source. |
| Wake prediction | Re split, domain, BC/IC, solver, mesh, timestep/CFL, rollout horizon, force/frequency diagnostics. |
| Neural ROM | Full-order solver, latent dimension, rollout horizon, POD/Galerkin baseline setup. |
| DRL/control | Simulator version, action limits, observation locations/variables, reward, baseline controller, seeds/training budget. |

## Output schema

| Item | Present? | Evidence location | Risk | Required fix |
|---|---|---|---|---|

Also include:

| Rubric axis | Score 0-3 | Evidence | Blocking TODO |
|---|---:|---|---|

## CFD anti-patterns

- “OpenFOAM default settings” with no dictionaries.
- no mesh/time-step convergence.
- random split causing regime leakage.
- force/drag averaging window unspecified.
- nondimensionalization inconsistent.

## Verification

- Missing details are flagged, not guessed.
- Highest rejection-risk omissions are prioritized.
- Every 0-1 score has a concrete required fix.
