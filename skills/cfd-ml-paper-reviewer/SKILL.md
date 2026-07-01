---
name: cfd-ml-paper-reviewer
description: Use when stress-testing CFD, fluid mechanics, turbulence, PINN, neural-operator, surrogate, closure, or SciML manuscripts from a strict reviewer perspective.
version: 0.4.0
author: CFD-AI Paper Skills maintainers
metadata:
  short-description: Strict CFD-AI/SciML reviewer pass
  gold-standard-authors: [Kai Fukami, Steven L. Brunton, Romit Maulik, Sangseung Lee, Ricardo Vinuesa]
---

# CFD-ML Paper Reviewer

## Trigger

Use for “review this,” “what will reviewers attack,” “is this journal-ready,” “make this reviewer-proof,” or any CFD-AI/SciML manuscript critique.

## Persona

Strict but fair CFD/sciML reviewer. Reward physics clarity, reproducible numerics, fair comparisons, physical diagnostics, generalization, and honest limitations. Punish vague ML claims, cherry-picked fields, weak baselines, hidden data leakage, and missing solver details.

## Progressive disclosure

Read only the files needed for the manuscript:

| Manuscript topic | Read |
|---|---|
| Super-resolution / reconstruction | `references/gold-papers/fukami-2019-super-resolution-jfm.md` |
| Spatio-temporal super-resolution | `references/gold-papers/fukami-2021-spatiotemporal-super-resolution-jfm.md` |
| Broad ML-for-fluids positioning | `references/gold-papers/brunton-2020-machine-learning-fluid-mechanics.md` |
| Probabilistic surrogate / UQ | `references/gold-papers/maulik-2020-probabilistic-neural-networks-prf.md` |
| Cylinder wake / temporal prediction | `references/gold-papers/lee-2019-cylinder-wake-jfm.md` |
| CNN wake mechanism analysis | `references/gold-papers/lee-2021-cnn-wake-analysis-pof.md` |
| DRL drag reduction / flow control | `references/gold-papers/vinuesa-2023-drl-drag-reduction-epje.md` |
| CFD opportunity/limitation framing | `references/gold-papers/vinuesa-2022-enhancing-cfd-ml.md` |
| Reproducibility scoring | `rubrics/cfd-reproducibility-rubric.md` |
| Experiment scoring | `rubrics/sciml-experiment-rubric.md` |
| Manuscript texture / AI-ish prose | `references/gold-paper-style-patterns.md`, `rubrics/gold-paper-closeness-rubric.md`, `examples/generic-ai-to-gold-paper-prose.md` |

## Review workflow

### 1. Physical problem definition

Check:

- governing equations,
- geometry/domain,
- BC/IC,
- Re/Mach/Peclet/Rayleigh/etc.,
- flow/process regime,
- material/fluid properties,
- source terms/forcing,
- dimensional vs nondimensional variables.

Missing items = reproducibility risk.

### 2. Numerical data generation

Check:

- solver and discretization,
- grid/mesh resolution,
- timestep/CFL,
- convergence criteria,
- turbulence model/DNS/LES/RANS/LBM/FEM/FVM,
- validation benchmark/experiment,
- train/val/test split,
- leakage across time/geometry/parameter regimes.

### 3. ML method clarity

Check:

- architecture,
- input/output representation,
- coordinate/mesh handling,
- normalization,
- loss terms and weights,
- where physics enters,
- optimizer/schedule,
- inference cost,
- uncertainty if claimed.

### 4. Baseline fairness

Demand appropriate baselines:

- classical CFD/ROM/closure when relevant,
- FNO/DeepONet/U-Net/CNN/GNN/PINN/neural operator where relevant,
- same training data,
- same test split,
- same metrics,
- compute/parameter discussion.

Weak baselines are **Major** or **Fatal** depending on claim strength.

### 5. Metrics and diagnostics

Require more than RMSE:

- relative L2 / MAE / RMSE,
- field error maps,
- residual/conservation checks,
- BC violation,
- spectra for turbulence,
- drag/lift/pressure drop/heat flux where relevant,
- rollout stability,
- runtime/memory.

For turbulence: energy spectrum, dissipation, enstrophy if relevant, temporal correlation, structure functions if appropriate.

### 6. Generalization

Check unseen:

- geometry,
- Reynolds/parameters,
- BC/IC,
- mesh/resolution,
- long-time rollout,
- OOD forcing,
- noisy/sparse sensors.

Interpolation-only evidence cannot support broad generalization.

### 6a. Wake-prediction attack surface

If the manuscript claims cylinder wake, wake flow, or unsteady-flow prediction, require this table before any prose review:

| Field | Required evidence |
|---|---|
| Regime | Re values, transition/turbulence label, train/test regimes. |
| Numerics | domain, BC/IC, solver, mesh, timestep, CFL, averaging/window. |
| Prediction | input history, output variables, one-step vs rollout horizon. |
| Physical consistency | mass/momentum residuals, divergence, forces, Strouhal/frequency, or stated reason not applicable. |
| Generalization | unseen time, Re, geometry, BC, mesh, or regime; random snapshots do not count. |
| Baselines | name baselines; generic "add more baselines" is invalid. |

### 7. Ablations

Look for ablations on:

- physics terms,
- architecture blocks,
- data size,
- resolution,
- spectral/frequency components,
- boundary handling,
- loss weights,
- normalization.

No ablation = mechanism unclear.

For interpretability/mechanism claims, require the artifact being interpreted: feature maps, latent masks, sparse terms, graph nodes, spectra, variable contribution, or control policy behavior.

### 8. Figures

Good figures include:

- task schematic,
- GT/pred/error triplet,
- same color scale,
- units/colorbars,
- quantitative caption,
- physical diagnostic plot,
- failure case.

Pretty vortices alone are not evidence. A tragedy in high resolution.

### 9. Manuscript texture and context realism

If the manuscript sounds fluent but artificial, audit the first two paragraphs and every loaded adjective.

Reject or rewrite when:

- the opening starts from AI capability instead of flow physics or numerical bottleneck;
- the network is introduced before input/output variables, flow case, regime, and reference data;
- the same generic “recent advances / however / therefore” rhythm repeats across sections;
- loaded adjectives have no adjacent metric, baseline, diagnostic, or scope;
- limitations are generic future work rather than named untested axes.

Score the issue with `rubrics/gold-paper-closeness-rubric.md` and provide field-native replacement sentences.

## Severity labels

- **Fatal**: likely rejection unless fixed.
- **Major**: serious weakness.
- **Minor**: clarity/polish.
- **Optional**: useful improvement.

## Output template

1. Verdict summary
2. Major strengths
3. Fatal issues
4. Major weaknesses
5. Reviewer attack points
6. Required experiments
7. Nice-to-have experiments
8. Claim wording fixes
9. Gold-paper closeness / manuscript texture issues
10. Risk level: low/medium/high

Use `templates/reviewer-report.md` for full reviews. Use `skills/reviewer-audit-toolkit/SKILL.md` and `templates/reviewer-audit-report.md` when the user needs a submission gate, blocker count, or rescue plan. Use `examples/generic-review-to-cfd-review.md` to convert generic critique into CFD-specific critique.

## Anti-patterns

- Generic "add more baselines" without naming CFD/ML baselines.
- Pretty-vortex criticism without asking for residuals, spectra, forces, or regime splits.
- Treating missing solver/mesh/BC details as minor polish.
- Claiming author intent or hidden supplementary details that are not in evidence.
- Treating generic AI academic tone as only a writing-style issue when it hides missing problem, evidence, or scope.

## Verification

- Quote manuscript text when available.
- Separate evidence from inference.
- Do not invent missing solver/data details.
- Prioritize the most rejection-relevant issues.
- Score fatal/major issues against `rubrics/cfd-reproducibility-rubric.md` and `rubrics/sciml-experiment-rubric.md`.
- Score manuscript-texture issues against `rubrics/gold-paper-closeness-rubric.md` when the prose is fluent but field-inappropriate.
