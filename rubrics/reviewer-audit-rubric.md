# Reviewer Audit Rubric

Use this rubric for decision-oriented CFD-AI/SciML manuscript audits. It scores whether the output would help an author survive reviewer scrutiny, not whether the prose sounds polite.

Score each axis 0--3.

| Score | Meaning |
|---:|---|
| 0 | Missing or misleading. |
| 1 | Generic; catches obvious problems but not field-specific risk. |
| 2 | Useful; identifies most domain risks but lacks gate/action precision. |
| 3 | Reviewer-grade; source-scoped, field-specific, prioritized, and actionable. |

## Axes

### 1. Source-scope discipline

- 0: invents solver/data/citation/metric details.
- 1: says facts are missing but still implies unsupported certainty.
- 2: separates known/unknown facts.
- 3: uses a source-scope ledger and turns unknowns into TODOs.

### 2. Claim-evidence alignment

- 0: summarizes claims without checking evidence.
- 1: flags broad claims generically.
- 2: maps major claims to evidence or missing evidence.
- 3: classifies each claim type and supplies safer wording.

### 3. Physical/numerical completeness

- 0: ignores flow setup and solver details.
- 1: asks for “more details” generically.
- 2: requests geometry, BC/IC, regime, mesh/grid, timestep/CFL, solver/fidelity.
- 3: ties each missing numerical detail to a reviewer risk.

### 4. ML-method reproducibility

- 0: accepts model names as sufficient.
- 1: asks for architecture only.
- 2: asks for input/output, normalization, loss, optimizer, split, uncertainty when relevant.
- 3: identifies where physics enters and what ablation proves the method component.

### 5. Validation and generalization

- 0: accepts random held-out accuracy as generalization.
- 1: asks for broader validation but not split axes.
- 2: names held-out Re/geometry/BC/mesh/time/noise/OOD axes.
- 3: distinguishes interpolation, extrapolation, rollout, solver-coupled, and deployment claims.

### 6. Metrics and physical diagnostics

- 0: accepts visual plots only.
- 1: asks for quantitative metrics only.
- 2: asks for error metrics plus physical diagnostics/QoIs.
- 3: names diagnostics appropriate to the flow: residuals, divergence, spectra, forces, pressure drop, heat flux, conservation, uncertainty calibration, or rollout stability.

### 7. Baseline fairness

- 0: does not discuss baselines.
- 1: says “add baselines.”
- 2: names baseline classes and same-data/split/metric requirements.
- 3: separates classical CFD/ROM/interpolation/closure baselines from ML baselines and ties them to claims.

### 8. Figure/table evidence logic

- 0: accepts pretty visuals.
- 1: asks for more figures.
- 2: demands GT/input/pred/error and quantitative captions.
- 3: specifies a figure/table that rescues each Fatal/Major claim.

### 9. Prioritization and gate decision

- 0: no verdict.
- 1: verdict without severity.
- 2: Fatal/Major/Minor labels.
- 3: submission-readiness gate with exact blockers and minimum rescue plan.

### 10. Actionability

- 0: critique only.
- 1: vague suggestions.
- 2: required fixes are listed.
- 3: each fix names the needed experiment/table/figure/rewrite and the claim it rescues.

## Release gate

A reviewer audit passes only if:

- no hallucinated scientific details are present;
- every Fatal issue has a required fix;
- broad terms such as `robust`, `generalizable`, `physically consistent`, `state-of-the-art`, `real-time`, and `solver replacement` are bounded or rejected;
- the final decision is consistent with the evidence, not the tone.
