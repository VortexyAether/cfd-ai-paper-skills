---
title: Brunton 2016 SINDy PNAS deep analysis
created: 2026-06-30
updated: 2026-06-30
status: v0.4-arxiv-abstract-grounded
source_scope: arXiv metadata/abstract and DOI metadata; full PDF not read in this pass
---

# Brunton 2016: Discovering governing equations from data by sparse identification of nonlinear dynamical systems

## Metadata

| Field | Value |
|---|---|
| Title | Discovering governing equations from data by sparse identification of nonlinear dynamical systems |
| Authors | Steven L. Brunton, Joshua L. Proctor, J. Nathan Kutz |
| Year / venue | 2016, PNAS 113(15), 3932-3937 |
| DOI / arXiv / URL | DOI: https://doi.org/10.1073/pnas.1517384113; arXiv: https://arxiv.org/abs/1509.03580 |
| Role | Brunton first author; corresponding-author status unknown/TODO |

## Source Scope

ArXiv metadata/abstract plus DOI metadata. Exact algorithm tables, thresholds, and supplementary details are TODO.

## Why Answer Key

This paper is a model for interpretable scientific ML: the ML method is valuable because it recovers sparse governing dynamics, not because it is a black-box predictor. The answer-key pattern is parsimony, candidate-library transparency, validation on canonical systems, and a fluid vortex-shedding demonstration.

## Abstract Grammar

| Move | Pattern |
|---|---|
| Context | Discovering physical laws from data is central to science. |
| Gap | Data-driven models often lack parsimonious governing equations. |
| Method | Sparse regression over a nonlinear candidate-function library. |
| Evidence | Linear/nonlinear oscillators, Lorenz system, and fluid vortex shedding behind an obstacle. |
| Implication | Sparse models can generalize to parameterized, time-varying, and forced systems. |

## Introduction Move Structure

1. Start from governing equations as scientific knowledge.
2. Introduce data abundance as an opportunity but not a substitute for interpretability.
3. State sparsity as the physical prior.
4. Present the algorithm as model discovery, not curve fitting.
5. Demonstrate across canonical dynamics and a fluid example.

## Method/Reproducibility Checklist

| Item | Status |
|---|---|
| State/derivative data | Confirmed at abstract level; exact derivative estimation TODO. |
| Candidate library | Confirmed: nonlinear candidate functions; exact library choices TODO. |
| Sparse regression | Confirmed; exact optimizer/thresholding TODO. |
| Canonical cases | Confirmed: oscillators, Lorenz, vortex shedding. |
| Noise robustness | Unknown/TODO from abstract. |
| Code/data | Unknown/TODO. |

## Experiment/Evidence Stack

1. Algorithm schematic/equation form.
2. Simple systems where known equations can be recovered.
3. Chaotic Lorenz demonstration.
4. Fluid vortex-shedding reduced-order dynamics.
5. Generalization variants: parameterized/time-varying/forced systems.

## Figure Grammar With Confidence Labels

| Figure role | Confidence |
|---|---|
| Sparse-library regression schematic/equations | likely |
| Canonical system recovery table/plots | likely |
| Lorenz attractor reconstruction | likely |
| Fluid vortex-shedding dynamics example | confirmed by abstract but exact panels TODO |
| Generalization/forcing examples | confirmed by abstract but exact panels TODO |

## Reviewer-Defense Patterns

- Uses the physical prior "few active terms" as the claim boundary.
- Demonstrates on systems with known answers before the fluid case.
- Prioritizes interpretability and parsimony over black-box accuracy.
- Makes model complexity a scientific variable.

## Skill Lessons

- `related-work-cartographer` should separate discovery/identification from surrogate prediction.
- `paper-claim-auditor` should require candidate-library, sparsity, and validation details for discovery claims.
- `scientific-journal-writing` should frame interpretability as equation recovery, not vague explainability.

## Eval Task Derived From Paper

Ask a baseline agent to critique a "we discover governing equations" claim. It must request state variables, derivative estimation, candidate library, sparsity threshold, noise tests, and recovery of known equations.

## Unknowns/TODOs

- Full PDF/supplement extraction for exact experiments and thresholds.
- Corresponding-author status.

