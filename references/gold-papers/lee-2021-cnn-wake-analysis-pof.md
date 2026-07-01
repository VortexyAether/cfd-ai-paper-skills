---
title: Lee 2021 CNN wake analysis Physics of Fluids deep analysis
created: 2026-06-30
updated: 2026-06-30
status: v0.4-arxiv-abstract-grounded
source_scope: arXiv metadata/abstract and DOI metadata; full PDF not read in this pass
---

# Lee 2021: Analysis of a convolutional neural network for predicting unsteady volume wake flow fields

## Metadata

| Field | Value |
|---|---|
| Title | Analysis of a convolutional neural network for predicting unsteady volume wake flow fields |
| Authors | Sangseung Lee, Donghyun You |
| Year / venue | 2021, Physics of Fluids 33, 035152 |
| DOI / arXiv / URL | DOI: https://doi.org/10.1063/5.0040268; arXiv: https://arxiv.org/abs/1909.06042 |
| Role | Lee first author; corresponding-author status unknown/TODO |

## Source Scope

ArXiv metadata/abstract plus DOI metadata. Exact POF figure sequence and numerical setup are TODO.

## Why Answer Key

This paper shifts from "CNN predicts wake fields" to "what mechanisms does the CNN learn?" It is an answer key for interpretability claims: feature maps, wave-number analysis, variable/time-history contributions, and parameter reduction are used as evidence.

## Abstract Grammar

| Move | Pattern |
|---|---|
| Context | CNNs are used for fluid-dynamics prediction. |
| Gap | The mechanisms by which CNNs learn fluid dynamics are not well understood. |
| Method | CNN prediction of 3D unsteady wake flow plus feature-map and Fourier analyses. |
| Evidence | Circular-cylinder wake in 3D wake transition and shear-layer transition regimes. |
| Implication | CNN feature maps transport wave-number information and can reveal redundant learned structures. |

## Introduction Move Structure

1. Start from deep-learning wake prediction.
2. Identify black-box mechanism uncertainty.
3. Introduce feature-map visualization and Fourier analysis.
4. Compare across wake regimes.
5. Translate mechanism analysis into parameter-reduction insight.

## Method/Reproducibility Checklist

| Item | Status |
|---|---|
| Flow case | Confirmed: circular-cylinder wake. |
| Regimes | Confirmed: 3D wake transition and shear-layer transition regimes. |
| Model | Confirmed: CNN for future 3D unsteady wake fields. |
| Mechanism probes | Confirmed: feature maps, Fourier analysis, variable/time-history contributions. |
| Parameter reduction | Confirmed: 85 percent parameter reduction without performance loss, per abstract. |
| Solver/mesh/Re/time step | TODO. |
| Training data/splits | TODO. |

## Experiment/Evidence Stack

1. CNN prediction setup.
2. Wake-regime comparison.
3. Feature-map visualization.
4. Fourier/wave-number transport analysis.
5. Variable and time-history contribution analysis.
6. Redundant feature-map similarity and parameter reduction.

## Figure Grammar With Confidence Labels

| Figure role | Confidence |
|---|---|
| Wake/CNN prediction setup | likely |
| Feature maps in two regimes | confirmed by abstract but exact panels TODO |
| Fourier/wave-number analysis | confirmed by abstract but exact panels TODO |
| Variable/time-history contribution plots | confirmed by abstract but exact panels TODO |
| Parameter reduction/performance comparison | confirmed by abstract but exact panels TODO |

## Reviewer-Defense Patterns

- Treats interpretability as analyses of internal representations, not just verbal explanation.
- Compares mechanisms across physically distinct regimes.
- Connects interpretation to model simplification.

## Skill Lessons

- `paper-claim-auditor` should reject "interpretable" unless specific probes are named.
- `figure-and-result-storytelling` should require feature maps plus physical interpretation for CNN-mechanism papers.
- `cfd-ml-paper-reviewer` should ask whether interpretation changes model design or claim scope.

## Eval Task Derived From Paper

Ask a weak reviewer to critique a CNN wake prediction paper claiming interpretability. It must demand feature maps, spectral analysis, variable/time-history contributions, and physical-regime comparison.

## Unknowns/TODOs

- Full PDF extraction for exact regimes, solver details, and panel order.
- Corresponding-author status.

