---
title: Gold-standard bibliography v0.4
created: 2026-06-30
updated: 2026-06-30
source: TARS + arXiv/DOI metadata and v0.4 gold-paper notes
status: v0.4
tags:
  - cfd-ai
  - sciml
  - gold-standard
  - bibliography
---

# Gold-Standard Bibliography v0.4

This bibliography indexes the evaluator-facing gold-paper files under `references/gold-papers/`. Exact source scope lives in each paper file.

## Source-Scope Rule

- `full PDF/arXiv full text`: only when the file explicitly says so.
- `arXiv metadata/abstract`: title, authors, abstract, and arXiv metadata were used.
- `DOI metadata`: DOI/venue metadata was used.
- `unknown/TODO`: do not infer solver details, figure captions, corresponding-author status, code availability, or exact metrics.

## Kai Fukami

| File | Paper | Source scope |
|---|---|---|
| `references/gold-papers/fukami-2019-super-resolution-jfm.md` | Super-resolution reconstruction of turbulent flows with machine learning | arXiv metadata/abstract and accessible arXiv text; PDF-level TODO |
| `references/gold-papers/fukami-2021-spatiotemporal-super-resolution-jfm.md` | Machine-learning-based spatio-temporal super resolution reconstruction of turbulent flows | arXiv metadata/abstract and DOI metadata |
| `references/gold-papers/fukami-2023-super-resolution-survey-tcfd.md` | Super-resolution analysis via machine learning: A survey for fluid flows | arXiv metadata/abstract and DOI metadata |

## Steven L. Brunton

| File | Paper | Source scope |
|---|---|---|
| `references/gold-papers/brunton-2016-sindy-pnas.md` | Discovering governing equations from data by sparse identification of nonlinear dynamical systems | arXiv metadata/abstract and DOI metadata |
| `references/gold-papers/brunton-2020-machine-learning-fluid-mechanics.md` | Machine Learning for Fluid Mechanics | arXiv metadata/abstract; full taxonomy TODO |
| `references/gold-papers/brunton-2021-applying-ml-fluid-mechanics.md` | Applying Machine Learning to Study Fluid Mechanics | arXiv metadata/abstract and DOI metadata |

## Romit Maulik

| File | Paper | Source scope |
|---|---|---|
| `references/gold-papers/maulik-2020-probabilistic-neural-networks-prf.md` | Probabilistic neural networks for fluid flow surrogate modeling and data recovery | arXiv metadata/abstract |
| `references/gold-papers/maulik-2021-rom-advection-poF.md` | Reduced-order modeling of advection-dominated systems with recurrent neural networks and convolutional autoencoders | arXiv metadata/abstract and DOI metadata |
| `references/gold-papers/maulik-2023-multiscale-gnn-autoencoders-jcp.md` | Multiscale graph neural network autoencoders for interpretable scientific machine learning | arXiv metadata/abstract and DOI metadata |

## Sangseung Lee

| File | Paper | Source scope |
|---|---|---|
| `references/gold-papers/lee-2019-cylinder-wake-jfm.md` | Data-driven prediction of unsteady flow fields over a circular cylinder using deep learning | arXiv metadata/abstract |
| `references/gold-papers/lee-2021-cnn-wake-analysis-pof.md` | Analysis of a convolutional neural network for predicting unsteady volume wake flow fields | arXiv metadata/abstract and DOI metadata |
| `references/gold-papers/lee-2022-rough-surface-transfer-learning-jfm.md` | Predicting drag on rough surfaces by transfer learning of empirical correlations | arXiv metadata/abstract and DOI metadata |

## Ricardo Vinuesa

| File | Paper | Source scope |
|---|---|---|
| `references/gold-papers/vinuesa-2022-enhancing-cfd-ml.md` | Enhancing Computational Fluid Dynamics with Machine Learning | arXiv metadata/abstract |
| `references/gold-papers/vinuesa-2023-transformative-ml-experiments-nrp.md` | The transformative potential of machine learning for experiments in fluid mechanics | arXiv metadata/abstract and DOI metadata |
| `references/gold-papers/vinuesa-2023-drl-drag-reduction-epje.md` | Deep reinforcement learning for turbulent drag reduction in channel flows | arXiv metadata/abstract and DOI metadata |

## v0.5 Bibliography Work

1. PDF-level extraction for the 15 indexed files.
2. Corresponding-author verification from title pages or publisher metadata.
3. Figure-by-figure grammar tables with confirmed captions.
4. Code/data availability checks.
