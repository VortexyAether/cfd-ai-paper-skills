# Trend review manuscript A/B benchmark run

Run root:

`evaluation/runs/2026-07-01-trend-review-ab/`

Benchmark prompt:

`evaluation/tasks/cfd-ai-trend-review-manuscript-benchmark.md`

## Run type

Controlled baseline ablation:

- `no_skill/main.tex`: same review benchmark, generic/no-skill behavior.
- `with_skill/main.tex`: same benchmark, CFD-AI/SciML skill-guided behavior.

This is still an internal controlled A/B, not an external weak-model run.

## Compile verification

Both outputs compile with Tectonic.

```text
no_skill/main.pdf    28K
with_skill/main.pdf  38K
```

No fatal LaTeX errors.

Warnings:

- no-skill: none surfaced in compile log scan.
- with-skill: layout warnings from dense taxonomy/checklist tables; acceptable for benchmark artifact.

## Risky phrase scan

### No-skill baseline

The no-skill output repeatedly uses unsupported review-paper overclaims:

- `state-of-the-art tools`
- `robust`
- `physically consistent`
- `real-time CFD applications`
- `can generalize across these cases`
- `deployment-ready CFD models`
- `real-time digital twins`

It treats architecture labels as evidence and uses validation words as goals rather than evidence contracts.

### Skill-guided output

The skill-guided output mentions risky phrases primarily as traps, limitations, or TODO-gated claims:

- geometry transfer requires held-out geometries;
- physical fidelity requires spectra/forces/residuals/conservation diagnostics;
- deployment requires hardware/runtime/coupling evidence;
- state-of-the-art requires same-data/same-split comparison;
- solved complex CFD is explicitly rewritten as a scoped selected-task claim.

## Scorecard

Manual manual evaluator scores using the trend-review benchmark scorecard.

| Axis | No skill | With skill | Notes |
|---|---:|---:|---|
| LaTeX compilability | 3 | 3 | Both compile. |
| Review-paper structure | 1 | 3 | No-skill is shallow survey; with-skill has review sections, agenda, traps. |
| Trend specificity | 1 | 3 | No-skill says geometry/mesh but stays generic; with-skill centers the bottleneck. |
| Workflow-first taxonomy | 0 | 3 | No-skill starts method-family list; with-skill starts CFD workflow role. |
| Method-family coverage | 2 | 3 | Both cover families; with-skill separates strengths/validation limits. |
| Validation-axis depth | 1 | 3 | No-skill names metrics; with-skill maps claims to validation axes. |
| Reproducibility discipline | 1 | 3 | No-skill says report details; with-skill names numerical + ML reproducibility. |
| Reviewer-trap handling | 0 | 3 | No-skill commits traps; with-skill has explicit trap rewrite table. |
| Figure/table evidence logic | 1 | 3 | No-skill figures are decorative; with-skill captions state supported claims. |
| Field-native vocabulary | 1 | 3 | No-skill hype wording; with-skill uses CFD validation vocabulary. |
| Non-hallucination | 1 | 3 | No-skill implies SOTA/generalization/deployment; with-skill marks TODOs. |

Average:

- No skill: **1.1 / 3.0**
- With skill: **3.0 / 3.0**

Benchmark internal pass threshold:

- average score >= 2.3;
- no score below 1 on LaTeX compilability, non-hallucination, or workflow-first taxonomy.

Result:

- No skill: **fail**.
- With skill: **pass**.

## Main finding

This review benchmark separates skill use more strongly than the single-method manuscript benchmark.

The no-skill output is fluent but review-useless: it lists method families, repeats broad promises, and treats validation as a generic checklist.

The skill-guided output produces an actual review scaffold: workflow-first taxonomy, method-family map, validation axes, reproducibility requirements, evidence-linked figures, reviewer trap rewrites, and a concrete agenda.

## Recommendation

Use this trend-review benchmark as the stronger deployment gate for the CFD-AI/SciML package.

Next upgrade: run the same prompt on a real weaker model with and without the skill package, keep raw outputs, compile logs, and evaluator scorecards.
