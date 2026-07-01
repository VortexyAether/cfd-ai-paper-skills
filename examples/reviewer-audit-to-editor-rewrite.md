# Reviewer Audit to Editor Rewrite

## Draft abstract

> We propose a robust physics-informed AI framework that predicts turbulent wake flows with state-of-the-art accuracy. The model generalizes to arbitrary Reynolds numbers and replaces expensive CFD simulations for real-time engineering design. Velocity contour plots show excellent agreement.

## Pass 1 — reviewer audit

| Severity | Claim / issue | Missing evidence | Required fix |
|---|---|---|---|
| Fatal | `state-of-the-art accuracy` | named baselines, same data/split/metric, uncertainty or repeated runs | add baseline table and quantitative metrics |
| Fatal | `generalizes to arbitrary Reynolds numbers` | held-out Reynolds-number split and failure boundary | report interpolation/extrapolation split by Reynolds number |
| Fatal | `replaces expensive CFD simulations` | task-limited deployment evidence, error tolerance, runtime, fallback | narrow to surrogate/post-processing role |
| Major | `physics-informed` | location of physics in loss/architecture/constraints/evaluation | state exact physics mechanism or remove phrase |
| Major | `contour plots show agreement` | error maps and physical diagnostics | add GT/pred/error, divergence/residual, force/frequency/QoI diagnostics |

## Editorial plan

1. Start from the physical/numerical bottleneck, not AI capability.
2. Replace universal claims with tested-scope claims.
3. Convert missing evidence into TODOs or future validation requirements.
4. Preserve contribution as a wake-flow surrogate only if the evidence supports it.
5. End with limitation boundary, not generic future work.

## Edited abstract

> Accurate reconstruction of unsteady wake fields remains difficult when only sparse or low-resolution flow data are available. We evaluate a physics-informed neural surrogate for wake-field prediction under the tested flow configuration. The current evidence is limited to qualitative velocity-contour agreement, so the result should be interpreted as a preliminary surrogate demonstration rather than proof of state-of-the-art accuracy, Reynolds-number generalization, or CFD replacement. To support stronger claims, the study must report the numerical setup, train/test split, quantitative errors against same-scope baselines, physical diagnostics such as residuals or force spectra, and measured inference cost on stated hardware.

## Pass 3 — re-audit

| Original risk | After edit | Residual risk | Next action |
|---|---|---|---|
| SOTA overclaim | removed | accuracy still unproven | add baseline/metric table |
| arbitrary-Re generalization | removed | generalization still untested | add held-out Re split |
| CFD replacement | downgraded to preliminary surrogate | deployment not supported | add runtime/error-tolerance/fallback evidence |
| contour-only evidence | named as limitation | physical fidelity unknown | add residual/QoI diagnostic figure |

## Lesson

The editor does not “make the review disappear.” The editor converts reviewer attacks into safer claims, explicit TODOs, and manuscript structure that does not promise evidence the paper lacks.
