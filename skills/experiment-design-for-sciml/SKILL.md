---
name: experiment-design-for-sciml
description: Use when designing experiments, baselines, ablations, generalization tests, and physical diagnostics for CFD-AI and scientific ML manuscripts.
version: 0.4.0
author: VA + TARS
metadata:
  short-description: Experiment matrix design for CFD-AI/SciML papers
---

# Experiment Design for SciML

## Trigger

Use when the user claims accuracy, generalization, robustness, physical consistency, efficiency, or journal readiness for a CFD-AI/SciML method.

## Core rule

Every experiment must defend a claim. Every claim without an experiment becomes a TODO or is weakened.

## Progressive disclosure

Read the relevant gold note before designing a matrix:

| Claim/task | Read |
|---|---|
| Super-resolution or reconstruction | `references/gold-papers/fukami-2019-super-resolution-jfm.md` |
| Spatio-temporal super-resolution | `references/gold-papers/fukami-2021-spatiotemporal-super-resolution-jfm.md` |
| Neural ROM / advection-dominated systems | `references/gold-papers/maulik-2021-rom-advection-poF.md` |
| Cylinder wake prediction | `references/gold-papers/lee-2019-cylinder-wake-jfm.md` |
| CNN wake mechanism analysis | `references/gold-papers/lee-2021-cnn-wake-analysis-pof.md` |
| DRL/control | `references/gold-papers/vinuesa-2023-drl-drag-reduction-epje.md` |

## Workflow

### 1. List claims

Extract claims:

- accuracy,
- generalization,
- physical consistency,
- efficiency,
- robustness,
- interpretability,
- data efficiency,
- stability.

### 2. Build baseline matrix

Choose baselines by task:

- surrogate/operator: FNO, DeepONet, U-Net/CNN, GNO/MeshGraphNet where relevant,
- PINN: vanilla PINN, improved PINN variants, numerical solver reference,
- reconstruction: interpolation/POD/autoencoder/super-resolution baselines; for spatio-temporal SR also test temporal interpolation/frame interval,
- closure/ROM: classical ROM, eddy-viscosity or existing closure model,
- control: uncontrolled flow, classical controller, and learned controller under the same simulator budget,
- generative flow: diffusion/FM baseline, deterministic predictor, statistical model.

### 3. Split design

Require splits that test the actual claim:

- random split = interpolation only,
- temporal split = rollout/generalization,
- parameter split = unseen Re/Ra/Ma/etc.,
- geometry split = unseen shapes,
- boundary-condition split,
- mesh/resolution split,
- OOD split.

### 4. Ablations

Ablate:

- physics loss/constraint,
- architecture modules,
- spectral/frequency block,
- data size,
- sensor count/sparsity,
- resolution,
- loss weights,
- normalization.

### 5. Physical diagnostics

Select diagnostics:

- conservation residual,
- BC violation,
- energy spectrum,
- dissipation/enstrophy,
- drag/lift/pressure drop,
- heat flux/Nusselt number,
- rollout stability,
- statistical moments.

### 5a. v0.4 benchmark-backed checks

| Task | Minimum added evidence |
|---|---|
| Spatio-temporal SR | spatial downsampling, temporal frame interval, GT/coarse/pred/error, turbulence statistics, and training/frame-interval sensitivity. |
| Wake prediction | Re/regime split, rollout horizon, conservation/force/frequency diagnostics, and named baselines. |
| Neural ROM | POD/Galerkin or classical ROM baseline, latent dimension, rollout stability, and parametric test if claimed. |
| DRL/control | reward, action limits, observations, closed-loop baseline, seeds, and simulator fidelity. |

### 6. Efficiency reporting

Report:

- training/inference time,
- hardware,
- parameter count,
- memory,
- solver speedup baseline,
- preprocessing cost.

## Output template

1. Claim list
2. Required experiment matrix
3. Baselines
4. Metrics/physical diagnostics
5. Ablations
6. Generalization/OOD tests
7. Minimum publishable experiment set
8. Stretch experiments

## Anti-patterns

- Claiming generalization from random snapshot splits.
- Listing baselines without matching data, split, metric, and compute conditions.
- Using RMSE-only evidence for turbulent or physical-consistency claims.
- Omitting failure cases for robustness or OOD claims.

## Verification

- Experiments map to claims.
- Baselines are task-appropriate.
- Splits actually test generalization.
- Physical metrics are not replaced by only RMSE.
