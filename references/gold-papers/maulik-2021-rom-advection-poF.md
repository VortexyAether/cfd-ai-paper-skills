---
title: Maulik 2021 ROM advection Physics of Fluids deep analysis
created: 2026-06-30
updated: 2026-06-30
status: v0.4-arxiv-abstract-grounded
source_scope: arXiv metadata/abstract and DOI metadata; full PDF not read in this pass
---

# Maulik 2021: Reduced-order modeling of advection-dominated systems with recurrent neural networks and convolutional autoencoders

## Metadata

| Field | Value |
|---|---|
| Title | Reduced-order modeling of advection-dominated systems with recurrent neural networks and convolutional autoencoders |
| Authors | Romit Maulik, Bethany Lusch, Prasanna Balaprakash |
| Year / venue | 2021, Physics of Fluids 33, 037106 |
| DOI / arXiv / URL | DOI: https://doi.org/10.1063/5.0039986; arXiv: https://arxiv.org/abs/2002.00470 |
| Role | Maulik first author; corresponding-author status unknown/TODO |

## Source Scope

ArXiv metadata/abstract plus DOI metadata. Exact architecture, training, and plots are TODO.

## Why Answer Key

This paper is a ROM answer key for advection-dominated systems. It frames the weakness of POD/Galerkin truncation, proposes CAE latent spaces plus RNN evolution, and evaluates on PDE systems where sharp advective features expose ROM failure.

## Abstract Grammar

| Move | Pattern |
|---|---|
| Context | POD/Galerkin is a common reduced-order strategy for nonlinear PDEs. |
| Gap | Advection-dominated PDEs are poorly represented when truncation discards high-mode interactions. |
| Method | Convolutional autoencoder for encoding plus recurrent neural network for latent time evolution. |
| Evidence | Viscous Burgers shock profile, inviscid shallow-water equations, and parametric embedding. |
| Implication | CAE/RNN low-dimensional models can outperform POD-Galerkin for advection-dominated dynamics. |

## Introduction Move Structure

1. Establish ROM need for expensive PDE systems.
2. Explain why POD-Galerkin truncation fails for moving/sharp features.
3. Introduce nonlinear latent encoding.
4. Add recurrent latent dynamics.
5. Show parametric extension.

## Method/Reproducibility Checklist

| Item | Status |
|---|---|
| Baseline | Confirmed: POD-Galerkin. |
| Models | Confirmed: CAE plus RNN. |
| Cases | Confirmed: viscous Burgers, inviscid shallow water. |
| Latent dimensions | Confirmed from abstract: two for Burgers, six for shallow water. |
| Parameter embedding | Confirmed at abstract level. |
| Numerical solver/data generation | Unknown/TODO. |
| Training split/seed/hyperparameters | Unknown/TODO. |

## Experiment/Evidence Stack

1. POD-Galerkin failure framing.
2. CAE latent reconstruction.
3. RNN latent time evolution.
4. Burgers sharp-profile result at low viscosity.
5. Shallow-water evolution result.
6. Parametric trend detection in latent space.

## Figure Grammar With Confidence Labels

| Figure role | Confidence |
|---|---|
| CAE/RNN ROM pipeline | likely |
| POD-Galerkin vs CAE/RNN comparison | likely |
| Burgers shock reconstruction/evolution | confirmed by abstract but exact panels TODO |
| Shallow-water evolution | confirmed by abstract but exact panels TODO |
| Parametric latent embedding/trends | confirmed by abstract but exact panels TODO |

## Reviewer-Defense Patterns

- Names a specific classical ROM failure mode.
- Uses PDE cases matched to that failure mode.
- Reports latent dimension as part of the evidence, not just architecture.
- Extends to parametric ROM without hiding the added claim.

## Skill Lessons

- `sciml-experiment-auditor` should require classical ROM baselines for neural ROM claims.
- `figure-and-result-storytelling` should show temporal evolution, not static reconstruction only.
- `paper-claim-auditor` should distinguish compression accuracy from stable latent dynamics.

## Eval Task Derived From Paper

Ask for a minimum evidence stack for a neural ROM of an advection-dominated PDE. The baseline agent must include POD/Galerkin comparison, latent dimension, rollout, parametric tests, and failure modes.

## Unknowns/TODOs

- Full PDF extraction for solver settings, training details, and metrics.
- Corresponding-author status.

