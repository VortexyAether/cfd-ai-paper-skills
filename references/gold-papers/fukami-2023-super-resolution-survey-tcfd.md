---
title: Fukami 2023 super-resolution survey TCFD deep analysis
created: 2026-06-30
updated: 2026-06-30
status: v0.4-arxiv-abstract-grounded
source_scope: arXiv metadata/abstract and DOI metadata; full PDF not read in this pass
---

# Fukami 2023: Super-resolution analysis via machine learning: A survey for fluid flows

## Metadata

| Field | Value |
|---|---|
| Title | Super-resolution analysis via machine learning: A survey for fluid flows |
| Authors | Kai Fukami, Koji Fukagata, Kunihiko Taira |
| Year / venue | 2023, Theoretical and Computational Fluid Dynamics 37, 421-444 |
| DOI / arXiv / URL | DOI: https://doi.org/10.1007/s00162-023-00663-0; arXiv: https://arxiv.org/abs/2301.10937 |
| Role | Fukami first author; corresponding-author status unknown/TODO |

## Source Scope

ArXiv metadata/abstract plus DOI metadata. Full section taxonomy and figure list are TODO.

## Why Answer Key

This is the survey counterpart to Fukami's JFM reconstruction papers. It defines how to position super-resolution as a fluid-flow task: not generic image enhancement, but reconstruction from spatially limited numerical or experimental measurements with fluid-specific physics constraints.

## Abstract Grammar

| Move | Pattern |
|---|---|
| Context | Super-resolution reconstructs high-resolution flow fields from low-resolution data. |
| Gap | Fluid-flow SR inherits image-reconstruction tools but faces vortical/turbulent constraints. |
| Method | Survey recent applications plus case studies on 2D decaying isotropic turbulence. |
| Evidence | Physics-inspired model designs and spatially limited measurements. |
| Implication | Survey insights can support SR analysis of numerical and experimental flow data. |

## Introduction Move Structure

1. Define super-resolution in a way a fluid-mechanics reader accepts.
2. Separate computer-vision inheritance from fluid-specific requirements.
3. Survey representative applications.
4. Add case studies to prevent purely bibliographic review.
5. Close with open challenges and outlook.

## Method/Reproducibility Checklist

| Item | Status |
|---|---|
| Review scope | Confirmed at abstract level: recent SR applications for fluid flows. |
| Case study | Confirmed: 2D decaying isotropic turbulence. |
| Physics-inspired designs | Confirmed as a theme; exact designs TODO. |
| Inclusion/exclusion criteria | Unknown/TODO. |
| Experimental vs numerical data discussion | Implied; exact coverage TODO. |
| Open challenges | Confirmed at abstract level; exact list TODO. |

## Experiment/Evidence Stack

1. Definition and task taxonomy for SR.
2. Literature taxonomy across vortical/turbulent applications.
3. Case-study setup for decaying isotropic turbulence.
4. Comparison of model-design choices.
5. Fluid-specific challenges and outlook.

## Figure Grammar With Confidence Labels

| Figure role | Confidence |
|---|---|
| SR task schematic | likely |
| Literature taxonomy/table | likely |
| 2D turbulence case-study fields | confirmed by abstract but exact panels TODO |
| Physics-inspired design comparison | likely |
| Challenges/outlook summary | TODO |

## Reviewer-Defense Patterns

- Makes a review useful by pairing taxonomy with case studies.
- Avoids "SR works" as a generic claim; asks what flow data and physics constraints demand.
- Turns open problems into evaluation axes for future manuscripts.

## Skill Lessons

- `related-work-cartographer` should classify SR work by data source, reconstruction target, and physical diagnostic.
- `scientific-journal-writing` should define imported ML terms in fluid-mechanics language.
- `sciml-experiment-auditor` should treat survey challenges as checklist items.

## Eval Task Derived From Paper

Give a citation dump of SR papers. The baseline agent must produce a taxonomy by input data, reconstruction target, architecture, flow regime, and physical diagnostic.

## Unknowns/TODOs

- Full PDF extraction for exact survey categories and figure/table order.
- Corresponding-author status.

