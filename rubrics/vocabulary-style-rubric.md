# Vocabulary Style Rubric

Use this rubric to detect AI-ish or field-inappropriate wording in CFD-AI/SciML manuscript text.

Score each axis 0–3.

| Axis | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| Task specificity | Generic AI/CFD wording | Mentions CFD or ML but no concrete task | Names task and method family | Names flow case, variable, regime, input/output, and ML role |
| Claim calibration | Unsupported adjectives | Some evidence but vague scope | Most claims evidence-linked | Every loaded adjective maps to metric/baseline/diagnostic/scope |
| Physics vocabulary | Visual/ML metrics only | Some physical terms but no diagnostics | Names relevant quantities | Uses diagnostics/QoIs tied to claims: residuals, spectra, forces, statistics, etc. |
| Related-work positioning | Chronological citation dump | Broad method list | Partial taxonomy | Workflow/data/regime/evidence taxonomy with close-prior-art boundary |
| Limitation precision | Vague future work | Names broad limitation | Names untested axis | Names untested regime/diagnostic/deployment/data assumption and required test |
| Figure-caption evidence | Decorative captions | Caption says what is shown | Caption includes condition/metric | Caption states evidence role, condition, diagnostic, and claim supported |
| AI-ish phrase control | Marketing/prose filler | Some suspicious phrases remain | Suspicious phrases mostly scoped | Suspicious phrases are removed or explicitly evidence-backed |

## Suspicious phrase gates

For each phrase, require the listed evidence before allowing it.

| Phrase | Required evidence |
|---|---|
| robust | noise/sparsity/OOD/rollout/mesh stress test with range and failure boundary |
| generalizable | leakage-safe holdout on claimed axis: Re, geometry, BC, roughness, time interval, parameter range |
| physically consistent | conservation residual, spectrum, vorticity PDF, force coefficient, wall shear, pressure drop, temporal correlation, or equation recovery |
| real-time | end-to-end latency on stated hardware vs acquisition/control interval |
| state-of-the-art | fair same-data/same-split/same-metric comparison to named baselines |
| novel | specific prior-art contrast and exact new component or claim boundary |
| interpretable | inspectable artifact validated against physical structure/diagnostic |
| efficient | hardware, wall-clock time, memory/params, and comparator; training vs inference separated |

## Evaluator output schema

Use this table:

| Phrase | Risk | Required evidence | Field-native rewrite | Residual TODO |
|---|---|---|---|---|

## Pass threshold

- MVP pass: average ≥ 2.2 and no score 0.
- v1.0 pass: average ≥ 2.6, AI-ish phrase control ≥ 3, claim calibration ≥ 3.
- Reject: any unsupported “state-of-the-art,” “physically consistent,” “generalizable,” or “real-time” claim in abstract/conclusion.
