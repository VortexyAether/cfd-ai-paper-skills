---
title: Figure archetypes for CFD-AI papers
created: 2026-06-30
updated: 2026-06-30
status: v0.3
tags:
  - cfd-ai
  - figures
  - evidence
---

# Figure Archetypes

Use with `rubrics/figure-evidence-rubric.md`.

| Archetype | Claim it can support | Required panels / labels | Anti-pattern |
|---|---|---|---|
| Flow setup schematic | Problem definition and reproducibility | domain, geometry, BC/IC, variables, nondimensional numbers | decorative domain with no BC/IC |
| Data/split map | Generalization and leakage control | train/val/test regimes across Re/time/geometry/BC | random split shown as generalization |
| Method workflow | Mechanism clarity | inputs, outputs, physics terms, loss/data path | architecture art with no variables |
| GT/pred/error fields | Accuracy and spatial structure | same colorbar, units, aligned panels, metric | pretty prediction without error map |
| Physical diagnostic | Physical consistency | spectrum, residual, drag/lift, pressure drop, heat flux, conservation metric | RMSE-only for physics claim |
| Ablation figure | Mechanism evidence | model variants, same split/metric, expected failure | ablation that changes multiple factors |
| OOD/failure case | Claim boundary | unseen regime and failure mode | hiding failed extrapolation |
| Efficiency table | Speed/cost claim | hardware, runtime, memory, parameters, baseline | "real-time" without hardware |

## Minimum figure sequence

1. Flow setup and task definition.
2. Data/regime split map.
3. Main quantitative comparison.
4. GT/pred/error field comparison.
5. Physical diagnostic.
6. Ablation.
7. Generalization or failure case.

