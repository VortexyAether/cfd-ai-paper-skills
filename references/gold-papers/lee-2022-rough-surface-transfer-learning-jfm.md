---
title: Lee 2022 rough-surface transfer learning JFM deep analysis
created: 2026-06-30
updated: 2026-06-30
status: v0.4-arxiv-abstract-grounded
source_scope: arXiv metadata/abstract and DOI metadata; full PDF not read in this pass
---

# Lee 2022: Predicting drag on rough surfaces by transfer learning of empirical correlations

## Metadata

| Field | Value |
|---|---|
| Title | Predicting drag on rough surfaces by transfer learning of empirical correlations |
| Authors | Sangseung Lee, Jiasheng Yang, Pourya Forooghi, Alexander Stroh, Shervin Bagheri |
| Year / venue | 2022, Journal of Fluid Mechanics 933, A18 |
| DOI / arXiv / URL | DOI: https://doi.org/10.1017/jfm.2021.1041; arXiv: https://arxiv.org/abs/2106.05995 |
| Role | Lee first author; corresponding-author status unknown/TODO |

## Source Scope

ArXiv metadata/abstract plus DOI metadata. Exact roughness statistics, DNS setup, and figures are TODO.

## Why Answer Key

This paper is an answer key for physics-informed transfer learning that does not rely on vague "physics prior" language. It transfers empirical correlations as approximate high-fidelity knowledge to reduce the DNS data burden for rough-wall drag prediction.

## Abstract Grammar

| Move | Pattern |
|---|---|
| Context | Neural networks can estimate drag on irregular rough surfaces. |
| Gap | High-fidelity DNS datasets are expensive and too small for practical training. |
| Method | Transfer learning from empirical correlations reported in the literature. |
| Evidence | Improved drag prediction under limited high-fidelity DNS data. |
| Implication | Approximate physics knowledge helps neural networks learn surface statistics affecting drag. |

## Introduction Move Structure

1. Establish rough-wall drag prediction as a practical CFD/engineering problem.
2. Name the data scarcity of DNS as the bottleneck.
3. Reframe empirical correlations as transferable approximate knowledge.
4. Claim improved learning efficiency, not universal replacement of DNS.
5. Tie roughness statistics to physical drag dependencies.

## Method/Reproducibility Checklist

| Item | Status |
|---|---|
| Target quantity | Confirmed: drag on irregular rough surfaces. |
| Prior knowledge | Confirmed: empirical correlations from literature. |
| Data bottleneck | Confirmed: limited DNS. |
| Transfer-learning design | Confirmed at abstract level; exact procedure TODO. |
| Roughness descriptors/statistics | Implied; exact list TODO. |
| DNS details | Unknown/TODO. |
| Baselines | Unknown/TODO exact baseline matrix. |

## Experiment/Evidence Stack

1. Roughness/drag problem setup.
2. Empirical-correlation pretraining or transfer procedure.
3. Limited-DNS training comparison.
4. Error versus amount of high-fidelity data.
5. Analysis of roughness statistics and drag dependency.

## Figure Grammar With Confidence Labels

| Figure role | Confidence |
|---|---|
| Rough-surface examples/statistics | likely |
| Transfer-learning workflow | likely |
| Prediction error versus DNS data amount | likely |
| Baseline comparison with/without empirical transfer | confirmed in claim but exact plot TODO |
| Physical interpretation of surface statistics | likely |

## Reviewer-Defense Patterns

- Turns empirical correlations into an explicit data-efficiency mechanism.
- Bounds claims to limited high-fidelity data settings.
- Connects model performance to known roughness-statistics effects.

## Skill Lessons

- `related-work-cartographer` should mark empirical correlations as prior knowledge, not just old baselines.
- `sciml-experiment-auditor` should require data-amount sweeps for transfer-learning claims.
- `paper-claim-auditor` should ask what is transferred and why it is physically relevant.

## Eval Task Derived From Paper

Ask a dumb agent to design evidence for "transfer learning improves rough-wall drag prediction." It must include empirical-correlation source, limited-DNS sweep, roughness statistics, and baseline without transfer.

## Unknowns/TODOs

- Full PDF extraction for DNS setup, roughness descriptors, and exact metrics.
- Corresponding-author status.

