---
name: figure-and-result-storytelling
description: Use when designing figures, result flow, captions, and visual evidence for CFD-AI/SciML journal manuscripts.
version: 0.4.0
author: VA + TARS
metadata:
  short-description: Evidence-first figure planning for CFD-AI/SciML papers
---

# Figure and Result Storytelling

## Trigger

Use when planning or critiquing paper figures, result sections, captions, visual comparisons, or graphical abstracts.

## Core rule

A figure is not decoration. It is evidence for a claim.

## Progressive disclosure

- Read `rubrics/figure-evidence-rubric.md` before scoring a figure plan.
- For super-resolution/reconstruction figure grammar, read `references/gold-papers/fukami-2019-super-resolution-jfm.md`.
- For spatio-temporal super-resolution, read `references/gold-papers/fukami-2021-spatiotemporal-super-resolution-jfm.md`.
- For cylinder-wake prediction/rollout figures, read `references/gold-papers/lee-2019-cylinder-wake-jfm.md`.
- For CNN mechanism/interpretability figures, read `references/gold-papers/lee-2021-cnn-wake-analysis-pof.md`.
- For uncertainty figures, read `references/gold-papers/maulik-2020-probabilistic-neural-networks-prf.md`.

## Figure archetypes

1. **Problem schematic** — domain, BC/IC, inputs/outputs, data pipeline.
2. **Method schematic** — architecture or workflow, but only if it clarifies mechanism.
3. **Dataset/regime map** — Re/geometry/parameter split; train vs test vs OOD.
4. **Main quantitative comparison** — metrics table/bar with fair baselines.
5. **GT/pred/error fields** — same color scale, units, colorbar.
6. **Physical diagnostic** — spectrum, conservation residual, drag/lift, heat flux, etc.
7. **Ablation** — mechanism evidence.
8. **Generalization/OOD** — unseen regime proof.
9. **Efficiency** — speed/memory/params.
10. **Failure case** — honest boundary of method.

## v0.4 figure add-ons

| Claim type | Required visual evidence |
|---|---|
| Spatio-temporal SR | GT/coarse-input/pred/error fields plus time-axis or frame-interval evidence. |
| Wake rollout | Time horizon, not only isolated snapshots; include force/frequency/residual where relevant. |
| Interpretability | The interpreted artifact itself: feature maps, spectra, latent masks, graph nodes, sparse terms, or policy behavior. |
| Control | Controlled vs uncontrolled vs classical baseline time histories and actuation constraints. |

## Workflow

1. Extract claims.
2. Assign at least one figure/table to each major claim.
3. Check whether every figure has a quantitative takeaway.
4. Ensure visual comparisons use same scales and units.
5. Draft captions as mini-arguments.

## Caption template

Use:

> Figure X. [What is shown.] [Experimental condition.] [Key quantitative/physical takeaway.] [Why it supports the claim.]

Bad caption:

> Velocity field comparison.

Good caption:

> Predicted and reference vorticity fields for the unseen $Re=2000$ cylinder wake. The proposed model preserves shear-layer roll-up and reduces relative $L_2$ error by 31% compared with FNO, while the error map shows remaining bias near vortex shedding extrema.

## Output template

1. Figure sequence
2. Claim supported by each figure
3. Required panels
4. Caption draft
5. Missing plots/data
6. Visual risk checklist

Also include:

| Figure/table | Claim | Rubric score 0-3 | Missing evidence | Required fix |
|---|---|---:|---|---|

For gold-paper reconstruction tasks, add a confidence column: `confirmed`, `likely`, or `TODO`.

## Anti-patterns

- Field snapshots without GT/pred/error or metric.
- Different color scales for compared fields.
- Caption states only what is shown, not what is learned.
- Turbulence claim with no spectrum/statistical diagnostic.
- Generalization claim with no unseen-regime panel.

## Verification

- Same colorbar/scale for comparisons.
- Units and nondimensional quantities are labeled.
- Every figure is referenced in text.
- Captions state takeaway, not just content.
- Pretty fields are paired with quantitative/physical diagnostics.
- Each major claim has at least one figure/table with rubric score 2 or 3.
