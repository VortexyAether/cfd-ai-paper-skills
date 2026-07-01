---
title: Journal expectations for CFD-AI and SciML papers
created: 2026-06-30
updated: 2026-06-30
status: v0.3
tags:
  - cfd-ai
  - journal-writing
  - reviewer-defense
---

# Journal Expectations

## Baseline expectations

| Area | Journal-ready expectation |
|---|---|
| Physics setup | Governing equations, assumptions, nondimensional groups, geometry, BC/IC. |
| Numerical setup | Solver/version, discretization, mesh/time step, convergence or validation, averaging windows. |
| ML setup | Architecture, inputs/outputs, preprocessing, loss, optimizer, hyperparameters, seeds/runs. |
| Evaluation | Fair baselines, leakage-safe splits, physical diagnostics, ablations, uncertainty where claimed. |
| Claims | Every abstract/contribution claim maps to evidence or explicit TODO. |
| Figures | Same scales, units, GT/pred/error, quantitative captions, physical diagnostics. |
| Reproducibility | Code/data/commands or honest access limitations; no placeholder URLs. |
| Limitations | Specific scope boundaries before reviewer attack. |

## Rejection-risk language

| Phrase | Required evidence before use |
|---|---|
| state-of-the-art | fair baseline matrix under same data/split/metrics |
| generalizes | unseen regime test matching claim |
| robust | noise/sparsity/OOD/failure stress tests |
| physically consistent | residual, conservation, spectrum, force, or relevant diagnostic |
| real-time | hardware, wall-clock, memory, and comparison |
| trustworthy | uncertainty calibration, error bars, or decision-relevant confidence evidence |

