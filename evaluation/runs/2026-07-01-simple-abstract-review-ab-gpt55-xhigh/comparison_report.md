# Simple abstract-review A/B comparison

## Purpose

This run responds to the contamination concern by using a deliberately simpler benchmark: one flawed abstract, one short review task, no LaTeX, no paper package context in the no-skill arm.

## Contamination controls

| Arm | Control |
|---|---|
| `no_skill` | Ran from a temporary directory outside the package; prompt only; `--ignore-rules`; no package files, rubrics, gold-paper notes, or field-style guide named. |
| `with_skill` | Same abstract and output shape, but explicitly loaded the package router, claim auditor, reviewer, writing skill, field terminology guide, gold-paper style guide, rubrics, and rewrite example. |

Both arms used `gpt-5.5` with `xhigh` reasoning.

## Task

Review this abstract:

> We propose a novel AI framework that robustly predicts turbulent flows with state-of-the-art accuracy. Our physics-informed neural network generalizes to arbitrary Reynolds numbers and provides physically consistent results in real time. We trained on simulation data and demonstrate the effectiveness of the method using velocity contour plots. These results show that the model can replace expensive CFD solvers for engineering design. Future work will improve scalability and robustness.

Output shape was fixed:

1. Verdict
2. Five most serious issues
3. Required evidence
4. Safer rewritten abstract

## Result summary

| Axis | no_skill | with_skill | Difference |
|---|---:|---:|---|
| Verdict catches rejection-level overclaim | 3 | 3 | Both reject. |
| Loaded-phrase detection | 2 | 3 | With-skill explicitly gates novelty, robust, SOTA, arbitrary-Re, physical consistency, real-time, solver replacement. |
| CFD setup specificity | 1 | 3 | With-skill asks for geometry, governing variables, Reynolds range, solver fidelity, mesh/grid, BC/IC, timestep/CFL. |
| Method specificity | 1 | 3 | With-skill asks for architecture, input/output map, normalization, loss terms/weights, optimizer, where physics enters. |
| Metrics/baselines | 2 | 3 | With-skill names relative L2/RMSE/MAE and same-data/split/metric baselines. |
| Physical diagnostics | 1 | 3 | With-skill names mass/momentum residuals, divergence, spectra, vorticity/statistical diagnostics, drag/lift/pressure drop. |
| Generalization evidence | 2 | 3 | With-skill demands leakage-safe Re interpolation/extrapolation split and optional geometry/BC/mesh/rollout axes. |
| Efficiency/deployment | 2 | 3 | With-skill asks for latency, hardware, batch size, memory, params, solver/runtime requirements. |
| Safer rewrite | 2 | 3 | No-skill rewrite still says “AI-based framework” and “turbulent flow fields”; with-skill narrows to preliminary surrogate claim and blocks deployment claims. |
| **Average** | **1.78** | **3.00** | Simpler benchmark shows larger skill margin. |

## Deterministic term coverage

| Term family | no_skill | with_skill |
|---|---|---|
| Flow/numerics | Reynolds only | Reynolds, geometry, BC/IC, mesh, CFL |
| Method internals | not specific | architecture, loss, input/output map, physics-informed component |
| Metrics | generic quantitative metrics | relative L2, RMSE, MAE, same-scope baselines |
| Physical diagnostics | conservation/residual broad only | mass/momentum residuals, divergence, spectra, vorticity, drag/lift, pressure drop |
| Deployment evidence | runtime benchmarks | latency, hardware, batch size, memory, params, solver/runtime requirements |

## Interpretation

This simpler benchmark reduces contamination suspicion because the no-skill arm had almost no context surface. It still caught the obvious hype, because the abstract is very bad and the base model is strong. But it stayed generic.

The with-skill arm converts the same criticism into field-native reviewer demands: exact flow/numerical setup, leakage-safe split axes, named CFD diagnostics, physical QoIs, method internals, and deployment evidence.

Bottom line: **skill value is most visible when the task is simple but demands domain-specific evidence, not when the task prompt itself already contains a full review rubric.**

## Files

- `prompt-no-skill.md`
- `prompt-with-skill.md`
- `no_skill_output.md`
- `with_skill_output.md`
- `model_settings.md`
