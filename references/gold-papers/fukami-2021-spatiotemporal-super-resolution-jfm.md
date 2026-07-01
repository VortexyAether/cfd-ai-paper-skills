---
title: Fukami 2021 spatio-temporal super-resolution JFM deep analysis
created: 2026-06-30
updated: 2026-06-30
status: v0.4-arxiv-abstract-grounded
source_scope: arXiv metadata/abstract and DOI metadata; full PDF not read in this pass
---

# Fukami 2021: Machine-learning-based spatio-temporal super resolution reconstruction of turbulent flows

## Metadata

| Field | Value |
|---|---|
| Title | Machine-learning-based spatio-temporal super resolution reconstruction of turbulent flows |
| Authors | Kai Fukami, Koji Fukagata, Kunihiko Taira |
| Year / venue | 2021, Journal of Fluid Mechanics 909, A9 |
| DOI / arXiv / URL | DOI: https://doi.org/10.1017/jfm.2020.948; arXiv: https://arxiv.org/abs/2004.11566 |
| Role | Fukami first author; corresponding-author status unknown/TODO |

## Source Scope

ArXiv metadata/abstract plus DOI metadata. Exact figure captions, solver settings, and training hyperparameters are TODO until PDF/full-text extraction.

## Why Answer Key

This paper extends Fukami 2019 from spatial super-resolution to coupled space-time reconstruction. The answer-key move is incremental but defensible: first establish the spatial reconstruction line, then add temporal inbetweening and test whether turbulence statistics survive coarse sampling in both dimensions.

## Abstract Grammar

| Move | Pattern |
|---|---|
| Context | Coarse computational/experimental flow data can miss both small spatial scales and intermediate temporal evolution. |
| Gap | Spatial super-resolution alone cannot recover time histories when frames are sparse. |
| Method | DSC/MS convolutional model inspired by super-resolution and inbetweening. |
| Evidence | Cylinder wake at Re_D = 100, 2D decaying homogeneous isotropic turbulence, and 3D turbulent channel flow at Re_tau = 180. |
| Implication | Reconstruction may support computational and experimental workflows when sampling is very coarse. |

## Introduction Move Structure

1. Reuse the low-resolution measurement/simulation bottleneck from the 2019 JFM paper.
2. Add temporal sparsity as a separate bottleneck.
3. Translate image inbetweening into a fluid-flow reconstruction task.
4. Claim a multiscale architecture only within tested canonical flows.
5. Preview space-time diagnostics and robustness to training amount/frame interval.

## Method/Reproducibility Checklist

| Item | Status |
|---|---|
| Flow cases | Confirmed from abstract: cylinder wake, 2D decaying isotropic turbulence, 3D channel flow. |
| Regimes | Confirmed: Re_D = 100; Re_tau = 180 for channel. |
| Model family | Confirmed: DSC/MS CNN. |
| Spatial/temporal downsampling protocol | TODO exact factors and frame intervals. |
| DNS/source solver | DNS/reference data named; solver/grid/timestep TODO. |
| Statistics | Confirmed at abstract level for turbulence statistics; exact diagnostics TODO. |
| Training data amount study | Confirmed at abstract level. |
| Code/data availability | Unknown/TODO. |

## Experiment/Evidence Stack

1. Space-time low-resolution input definition.
2. Architecture/pipeline schematic for spatio-temporal reconstruction.
3. Cylinder wake sanity case with reference/reconstruction/error.
4. 2D turbulence test with statistics.
5. 3D channel-flow stress test.
6. Training-snapshot dependence.
7. Temporal two-point correlation or frame-interval robustness study.

## Figure Grammar With Confidence Labels

| Figure role | Confidence |
|---|---|
| Space-time reconstruction schematic | likely |
| Cylinder wake GT/coarse/pred/error panels | likely |
| 2D turbulence statistics | confirmed from abstract but exact plot TODO |
| 3D channel-flow reconstruction panels | likely |
| Training amount sensitivity | confirmed from abstract but exact plot TODO |
| Temporal correlation/frame-interval robustness | confirmed from abstract but exact plot TODO |

## Reviewer-Defense Patterns

- Extends a known task along one clear new axis instead of claiming a new field.
- Tests laminar/canonical wake before turbulent cases.
- Uses turbulence statistics to avoid pure image-reconstruction evidence.
- Names the frame interval/training-data amount as a robustness question.

## Skill Lessons

- `figure-and-result-storytelling` should require time-axis evidence for spatio-temporal SR.
- `sciml-experiment-auditor` should separate spatial downsampling from temporal sparsity.
- `cfd-reproducibility-checker` should ask for sampling interval, not just grid resolution.

## Eval Task Derived From Paper

Ask a dumb agent to extend a spatial-SR evidence stack into a spatio-temporal one. It must add frame-interval, rollout/inbetweening, temporal-correlation, and turbulence-statistics checks without inventing solver settings.

## Unknowns/TODOs

- Full PDF extraction for exact figures, losses, grids, and frame intervals.
- Corresponding-author status.
- Code/data repository status.

