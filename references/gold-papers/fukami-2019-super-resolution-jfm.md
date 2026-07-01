---
title: Fukami 2019 super-resolution JFM deep analysis
created: 2026-06-30
updated: 2026-06-30
status: v0.4-harmonized-abstract-and-arxiv-grounded
source_scope: arXiv metadata/abstract and accessible arXiv text; PDF-level verification still TODO
---

# Fukami 2019: Super-resolution reconstruction of turbulent flows with machine learning

## Bibliographic metadata

| Field | Value |
|---|---|
| Title | Super-resolution reconstruction of turbulent flows with machine learning |
| Authors | Kai Fukami, Koji Fukagata, Kunihiko Taira |
| Year / venue | 2019, Journal of Fluid Mechanics 870, 106-120 |
| DOI / arXiv / URL | DOI: https://doi.org/10.1017/jfm.2019.238; arXiv: https://arxiv.org/abs/1811.11328 |
| Confirmed from | arXiv page metadata and abstract |
| Unknown/TODO | Corresponding-author status; final PDF figure captions beyond accessible arXiv text |

## Source Scope

ArXiv metadata/abstract and accessible arXiv text were used. Full PDF figure-caption verification remains TODO.

## Why this paper is an answer key

It translates a computer-vision task into a fluid-mechanics reconstruction problem without letting the paper become generic image ML. The answer-key pattern is: low-resolution flow data bottleneck -> specific super-resolution model -> canonical laminar test -> turbulent-flow stress test -> quantitative and physical diagnostics.

## Abstract grammar

| Move | Paper pattern |
|---|---|
| Context | High-fidelity simulations and experiments produce valuable flow-field data, but practical measurements/data can be under-resolved. |
| Gap | Grossly coarse flow data cannot directly reveal high-resolution turbulent structures. |
| Method | CNN and hybrid Downsampled Skip-Connection/Multi-Scale models reconstruct high-resolution fields from low-resolution inputs. |
| Evidence | Cylinder wake preliminary test; two-dimensional homogeneous turbulence; comparison to coarse inputs and traditional interpolation; small-data claim with as few as 50 training snapshots. |
| Implication | Super-resolution may help reveal subgrid-scale physics and support broader fluid-flow reconstruction. |

## Introduction move structure

1. Establish high-resolution flow data as a central experimental/computational aim.
2. Explain why growing data volume makes ML useful for reconstruction, not only modeling/control.
3. Import super-resolution from image processing, then narrow it to fluid data.
4. State the objective: reconstruct high-resolution flow fields from low-resolution images.
5. Preview models, test cases, and discussion of multi-scale turbulent reconstruction.

## Method/reproducibility checklist

| Item | Extracted / inferable status |
|---|---|
| Governing equations | Confirmed in accessible text for incompressible Navier-Stokes cylinder wake and 2D vorticity transport for turbulence. |
| Flow cases | Cylinder wake at Re_D = 100; 2D homogeneous decaying turbulence. |
| Data generation | DNS is stated; solver implementation details need PDF/code confirmation. |
| Input/output variables | Velocity vector and/or vorticity; low-resolution input to high-resolution output. |
| Downsampling | Average and max pooling; pooling factors reported in accessible text. |
| Models | CNN and hybrid DSC/MS; bicubic interpolation baseline. |
| Loss/training | L2 reconstruction objective, Adam, early stopping noted in accessible text. |
| Splits | Training/validation/test separation indicated; exact randomization and seeds unknown/TODO. |
| Code/data | Code availability statement appears in accessible arXiv text; actual repository status unknown/TODO. |

## Experiment/evidence stack

1. Method schematic for low-resolution input -> learned reconstruction -> high-resolution output.
2. Cylinder wake sanity case with vorticity contours and L2 error.
3. Snapshot-count sensitivity.
4. Vorticity PDF agreement for cylinder wake.
5. Homogeneous turbulence reconstructions across coarse resolutions, variables, and pooling methods.
6. Quantitative error comparison against bicubic interpolation, CNN, and DSC/MS.
7. Turbulence-specific diagnostics such as spectra/statistics where confirmed in the full paper; exact panels TODO.

## Figure grammar with confidence labels

| Figure role | Confidence |
|---|---|
| Pipeline schematic | Confirmed in accessible text. |
| Downsampling illustration | Confirmed in accessible text. |
| CNN/DSC-MS architecture schematic | Confirmed in accessible text. |
| Cylinder wake reconstruction | Confirmed in accessible text. |
| Error vs training snapshots | Confirmed in accessible text. |
| Vorticity PDF | Confirmed in accessible text. |
| Turbulent field GT/coarse/prediction/error | Likely/partly confirmed; exact panel order TODO. |
| Spectral/statistical diagnostic | likely for turbulence; verify from PDF before using as exact answer. |

## Reviewer-defense patterns

- Uses canonical cases before claiming value for turbulent flows.
- Includes a classical interpolation baseline rather than only comparing learned models.
- Reports physical variables and nondimensional regimes.
- Treats turbulent high-wavenumber content as a hard test, not a decorative visualization.
- Bounds the claim to reconstruction from low-resolution fields; broader deployment remains scoped.

## Skill lessons

- `figure-and-result-storytelling` should require GT/coarse/pred/error panels plus quantitative error.
- `sciml-experiment-auditor` should ask for classical interpolation/reconstruction baselines for super-resolution papers.
- `paper-claim-auditor` should reject broad "reveals turbulence physics" unless spectra/statistics or physical diagnostics are present.
- `cfd-reproducibility-checker` should require downsampling protocol, train/test split, variables, and nondimensional regimes.

## Eval task derived from this paper

Give a dumb agent only the title and abstract. It must reconstruct the evidence stack and figure sequence without inventing solver details. Score with `rubrics/figure-evidence-rubric.md`, `rubrics/sciml-experiment-rubric.md`, and hallucination checks.

## Unknowns/TODOs

- Full PDF extraction for exact figure captions and panel order.
- Corresponding-author status.
- Solver/code repository status beyond accessible text notes.
