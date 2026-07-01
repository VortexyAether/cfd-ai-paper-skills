---
title: Lee 2019 cylinder wake JFM deep analysis
created: 2026-06-30
updated: 2026-06-30
status: v0.4-harmonized-abstract-and-metadata-grounded
source_scope: arXiv metadata/abstract
---

# Lee 2019: Data-driven prediction of unsteady flow fields over a circular cylinder using deep learning

## Bibliographic metadata

| Field | Value |
|---|---|
| Title | Data-driven prediction of unsteady flow fields over a circular cylinder using deep learning |
| Authors | Sangseung Lee, Donghyun You |
| Year / venue | 2019, Journal of Fluid Mechanics, 879, 217-254 |
| DOI / arXiv / URL | DOI: https://doi.org/10.1017/jfm.2019.700; arXiv: https://arxiv.org/abs/1804.06076 |
| Confirmed from | arXiv page metadata/abstract; page gives JFM reference and DOI |
| Unknown/TODO | Corresponding-author status; exact numerical solver and mesh details from PDF |

## Source Scope

ArXiv metadata/abstract was used. Exact numerical solver, mesh, CFL, and final figure sequence remain TODO.

## Why this paper is an answer key

It is a canonical early JFM flow-prediction paper with explicit conservation-law loss comparisons and Reynolds-number generalization claims. The answer-key pattern is: future flow prediction from previous snapshots -> compare physics-informed and non-physics-informed networks -> test unseen Reynolds numbers -> analyze mechanisms such as physical losses, adversarial training, and network size.

## Abstract grammar

| Move | Paper pattern |
|---|---|
| Context | Unsteady cylinder wakes are a canonical flow-prediction problem. |
| Gap | Deep models must predict future flow fields and preserve governing-physics behavior, not just match images. |
| Method | CNN and GAN variants, each with and without conservation-law-informed losses. |
| Evidence | Train at Re = 100, 200, 300, 400; predict Re = 500 and 3000; analyze physical losses, adversarial training, and network size. |
| Implication | Predicted fields agree favorably with numerical simulation under the studied conditions. |

## Introduction move structure

1. Start from unsteady wake prediction as a CFD/time-evolution problem.
2. Introduce deep learning as an alternative mapping from prior snapshots to future fields.
3. Identify physical consistency as a weakness of generic neural prediction.
4. Introduce conservation-law loss terms and adversarial feature learning.
5. Preview Reynolds-number interpolation/extrapolation tests.

## Method/reproducibility checklist

| Item | Extracted / inferable status |
|---|---|
| Geometry | Circular cylinder wake. |
| Reynolds numbers | Training: 100, 200, 300, 400; prediction: 500 and 3000. |
| Prediction task | Future flow fields from previous flow fields. |
| Models | CNN and GAN, with/without conservation laws. |
| Physics terms | Conservation of mass and momentum in physical loss functions. |
| Numerical truth | Flow fields computed by numerical simulations. Exact solver/grid/time step TODO. |
| Generalization design | Unseen Re tests confirmed; whether Re=3000 is turbulent/transitional in setup requires PDF details. |
| Metrics | Prediction accuracy analyzed; exact metrics TODO. |

## Experiment/evidence stack

1. Data generation and flow setup.
2. Network variants: CNN, physics-CNN, GAN, physics-GAN.
3. One-step/future snapshot prediction.
4. Unseen Re evaluation at 500 and 3000.
5. Ablations: physical losses, adversarial training, network size.
6. GT/pred/error field comparisons.
7. Physical diagnostics: mass/momentum residuals or lift/drag/time histories likely; exact confirmed panels TODO.

## Figure grammar with confidence labels

| Figure role | Confidence |
|---|---|
| Cylinder setup and training/prediction workflow | likely; verify in PDF. |
| Network architecture comparison | likely. |
| Field predictions by model variant | likely from abstract. |
| Re generalization panels | likely from abstract. |
| Ablation or accuracy curves for physical loss/GAN/network size | likely from abstract. |
| Physical residual/force time-history diagnostic | Unknown/TODO. |

## Reviewer-defense patterns

- Compares physics-aware and non-physics-aware variants.
- Uses unseen Reynolds-number tests rather than only random time splits.
- Separates architecture effects from physics-loss effects.
- States agreement with numerical simulations, not experiments, keeping the validation source clear.

## Skill lessons

- `cfd-ml-paper-reviewer` should attack cylinder-wake claims on Re split, rollout horizon, conservation residuals, and solver details.
- `sciml-experiment-auditor` should require model-variant ablations when physics losses are proposed.
- `figure-and-result-storytelling` should demand time-series or rollout evidence, not isolated pretty snapshots.

## Eval task derived from this paper

Give a weak manuscript claim: "Our deep learning model predicts cylinder wakes and generalizes to new flow conditions." The dumb reviewer must ask for Re split, solver/grid/CFL, temporal rollout, conservation residuals, GT/pred/error fields, and bounded claim wording.

## Unknowns/TODOs

- Full PDF extraction for solver, mesh, CFL, exact metrics, and figure sequence.
- Corresponding-author status.
