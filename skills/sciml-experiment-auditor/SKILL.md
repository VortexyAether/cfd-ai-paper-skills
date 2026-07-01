---
name: sciml-experiment-auditor
description: Use when auditing CFD-AI/SciML experiments for baselines, ablations, generalization, physical diagnostics, uncertainty, compute reporting, and leakage-safe evaluation.
version: 0.4.0
author: VA + TARS
metadata:
  short-description: Experiment audit for CFD-AI/SciML manuscripts
---

# SciML Experiment Auditor

## Trigger

Use when reviewing experimental design or claims of accuracy, generalization, robustness, efficiency, physical consistency, or trustworthy prediction.

## Progressive disclosure

- Read `rubrics/sciml-experiment-rubric.md` before scoring.
- Read `examples/weak-to-publishable-experiment-plan.md` before writing a new plan.
- For super-resolution, read `references/gold-papers/fukami-2019-super-resolution-jfm.md`.
- For spatio-temporal super-resolution, read `references/gold-papers/fukami-2021-spatiotemporal-super-resolution-jfm.md`.
- For probabilistic/UQ claims, read `references/gold-papers/maulik-2020-probabilistic-neural-networks-prf.md`.
- For neural ROM/advection claims, read `references/gold-papers/maulik-2021-rom-advection-poF.md`.
- For wake prediction/generalization, read `references/gold-papers/lee-2019-cylinder-wake-jfm.md`.
- For flow-control/DRL claims, read `references/gold-papers/vinuesa-2023-drl-drag-reduction-epje.md`.

## Workflow

1. Extract claims.
2. Identify task: surrogate/operator/PINN/closure/reconstruction/control/discovery.
3. Select baseline matrix.
4. Audit splits for leakage.
5. Audit metrics and physical diagnostics.
6. Audit ablations and uncertainty.
7. Produce minimum publishable experiment set.

## Required checks

- baselines appropriate to task
- same data/split/metrics across baselines
- unseen Re/geometry/BC/time if generalization claimed
- physical diagnostics beyond RMSE
- multiple seeds/error bars if stochastic
- runtime/memory/hardware
- failure cases

## v0.4 claim-specific checks

| Claim | Extra checks |
|---|---|
| Spatio-temporal reconstruction | Spatial downsampling, temporal frame interval, reference data, turbulence statistics, and frame-interval sensitivity. |
| Neural ROM | Classical POD/Galerkin or task-appropriate ROM baseline, latent dimension, reconstruction error, and rollout stability. |
| Wake prediction | Unseen Re/regime split, rollout horizon, conservation/force/frequency diagnostics, and named baselines. |
| DRL/control | Reward, action limits, observation variables, closed-loop baseline, seeds, simulator fidelity, and physical side effects. |

## Output schema

| Claim | Missing experiment | Baseline | Metric | Severity | Fix |
|---|---|---|---|---|---|

Then add:

| Rubric axis | Score 0-3 | Evidence | Minimum experiment to reach 3 |
|---|---:|---|---|

Use `templates/experiment-plan.md` for full experiment plans.

## Anti-patterns

- Random split used as evidence for generalization.
- RMSE-only evaluation for physical-consistency claims.
- UQ claim without calibration, intervals, or multiple stochastic runs.
- Efficiency claim without hardware/runtime/memory.

## Verification

- Experiments map directly to claims.
- Generalization split actually tests generalization.
- No broad claim remains supported only by interpolation.
- Every proposed experiment has a baseline, metric, and pass condition.
- Generic "add baselines" is rejected unless the baselines are named and matched to the claim.
