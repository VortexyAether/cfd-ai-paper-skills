# Task: CFD-AI turbulence closure review benchmark

## Purpose

This benchmark tests whether an agent can write a CFD-native review seed for machine-learning turbulence closure without confusing offline regression with deployable closure evidence.

It stresses:

- a priori vs a posteriori evaluation;
- coupled-solver evidence;
- invariance and realizability;
- RANS/LES closure traps;
- uncertainty, calibration, and verifiability;
- cautious review-paper LaTeX production.

## Review topic

**Trend:** Machine-learning turbulence closures for RANS and LES: from data-fit closure terms to solver-coupled, invariant, verifiable models.

## Skills under test

Primary:

- `related-work-synthesis`
- `related-work-cartographer`
- `scientific-journal-writing`
- `paper-claim-auditor`
- `cfd-ml-paper-reviewer`
- `sciml-experiment-auditor`
- `cfd-reproducibility-checker`
- `figure-and-result-storytelling`
- `latex-paper-production`

Optional:

- `reviewer-simulator`
- `journal-submission-checklist`

## Gold-answer references

Read when available:

- `references/gold-papers/brunton-2020-machine-learning-fluid-mechanics.md`
- `references/gold-papers/brunton-2021-applying-ml-fluid-mechanics.md`
- `references/gold-papers/maulik-2020-probabilistic-neural-networks-prf.md`
- `references/gold-papers/vinuesa-2022-enhancing-cfd-ml.md`
- `references/cfd-ai-benchmark-landscape.md`
- `references/field-terminology-style-guide.md`
- `rubrics/claim-evidence-rubric.md`
- `rubrics/cfd-reproducibility-rubric.md`
- `rubrics/sciml-experiment-rubric.md`
- `rubrics/figure-evidence-rubric.md`

## Baseline-agent / model prompt

You are writing a CFD-AI / scientific-ML **review article seed** in LaTeX. Your output must be a complete compilable `main.tex` file, not a bullet memo.

### Target

Draft a 5--7 page mini-review manuscript seed for a Journal of Fluid Mechanics / Journal of Computational Physics / Physics of Fluids audience.

### Review title

**Machine-learning turbulence closures: why a priori accuracy is not enough for RANS and LES deployment**

### Review thesis

The review should argue that ML turbulence closure papers need to move from data-fit closure-term accuracy toward solver-coupled evidence: invariant inputs/outputs, realizability or boundedness checks, a posteriori stability, uncertainty/calibration, and reproducible coupling details.

### Evidence packet

Use only the evidence below. You may use placeholder citation keys, but do not invent bibliographic details, DOI values, author lists, benchmark numbers, or solver settings.

#### Known closure settings to cover

1. **RANS closure discrepancy models**
   - Aim: learn Reynolds-stress anisotropy, eddy-viscosity corrections, or model-form discrepancy.
   - Required evidence: invariant features or clear coordinate-frame handling; a posteriori RANS runs.
   - Trap: good Reynolds-stress fit can worsen mean velocity, pressure, or separation prediction after coupling.

2. **LES subgrid-scale closures**
   - Aim: learn SGS stress, scalar flux, or deconvolution-like closures.
   - Required evidence: energy spectra, dissipation behavior, long-rollout stability, and filter/grid dependence.
   - Trap: one-step SGS stress correlation does not prove stable LES.

3. **Data-driven uncertainty indicators**
   - Aim: identify regions of high model-form uncertainty or closure extrapolation.
   - Required evidence: calibration, held-out flows, uncertainty tied to decision-making.
   - Trap: uncertainty heatmaps without calibration are not verifiability.

4. **Hybrid solver-ML coupling**
   - Aim: integrate learned closures inside finite-volume, finite-difference, or spectral solvers.
   - Required evidence: solver time step, stability controls, residual behavior, wall-clock cost, fallback policy.
   - Trap: offline neural inference speed does not equal CFD solver speedup.

#### Validation axes the review must emphasize

- a priori target fit vs a posteriori coupled-solver behavior;
- invariant representation, tensor bases, frame indifference, and nondimensional inputs;
- realizability, boundedness, and numerical stability;
- training/test flow separation by geometry, Reynolds number, pressure gradient, and regime;
- RANS quantities: mean velocity, Reynolds stresses, skin friction, pressure coefficient, separation/reattachment;
- LES quantities: spectra, SGS dissipation, resolved kinetic energy, long-horizon drift;
- UQ/calibration: reliability diagrams, coverage, abstention/fallback policies;
- reproducibility: DNS/LES/RANS source, mesh/filter, solver, time step, coupling code, seeds, hardware/runtime.

#### Review claim boundaries

The review may say:

- ML closures can improve selected closure components under specific regimes;
- a priori accuracy is useful but insufficient for closure deployment;
- invariant and nondimensional formulations reduce avoidable failure modes;
- coupled-solver tests and uncertainty evidence are central reviewer demands.

The review must not say as fact:

- learned closures solve turbulence modeling;
- invariant inputs guarantee physical consistency;
- RANS/LES deployment is demonstrated without a posteriori solver evidence;
- the model is real-time, robust, or state-of-the-art without same-solver/same-data evidence;
- uncertainty is verified without calibration.

### Required LaTeX output

Generate one complete compilable LaTeX file using standard packages only:

- `article`
- `geometry`
- `amsmath`
- `booktabs`
- `graphicx`
- `hyperref`

The manuscript must include:

1. Title.
2. Abstract with review-paper moves: field context, closure-evidence gap, taxonomy contribution, validation agenda, limitation boundary.
3. Introduction explaining why closure papers need solver-coupled evidence.
4. Taxonomy organized first by closure role, then by ML method family.
5. Section on a priori vs a posteriori evidence.
6. Section on invariance, realizability, and numerical stability.
7. Section on UQ/verifiability and reproducibility.
8. At least two tables:
   - closure evidence ladder table;
   - reviewer-trap rewrite table.
9. At least three boxed figure placeholders:
   - closure coupling loop;
   - a priori/a posteriori validation ladder;
   - uncertainty and fallback decision flow.
10. A "Reviewer traps" section with 6--8 overclaims and safer rewrites.
11. A concrete research agenda.
12. `thebibliography` with placeholder entries only, e.g. `\bibitem{ling2016invariance} TODO: verified entry...`.

### Hard constraints

- Use `TODO` for missing bibliography and unsupported evidence.
- Do not invent exact benchmark numbers, DOI values, author lists, solver settings, datasets, or code repositories.
- Do not collapse RANS and LES into one generic "turbulence model" category.
- Do not use `robust`, `generalizable`, `physically consistent`, `state-of-the-art`, or `real-time` unless immediately bounded by evidence or flagged as unsupported.
- Every figure caption must state what claim the figure supports.
- Every table must include a limitation, validation, or reviewer-risk column.
- Make the prose sound like a cautious CFD/SciML review, not a hype blog post.

### Output format

Return only the LaTeX source code inside one fenced code block:

```latex
...
```

## Evaluator instructions

Score with:

- `rubrics/vocabulary-style-rubric.md`
- `rubrics/claim-evidence-rubric.md`
- `rubrics/sciml-experiment-rubric.md`
- `rubrics/cfd-reproducibility-rubric.md`
- `rubrics/figure-evidence-rubric.md`
- `rubrics/skill-quality-rubric.md`

## Expected pass criteria

A pass-level output should:

- compile with Tectonic or standard LaTeX without fatal errors;
- distinguish RANS and LES closure evidence;
- explain a priori vs a posteriori validation without treating either as optional;
- include invariance/realizability/stability discussion;
- require solver-coupled evidence and runtime/cost accounting;
- include at least two meaningful tables and three evidence-linked figure placeholders;
- include reviewer-trap rewrites and a concrete research agenda;
- mark bibliography and missing evidence as TODO;
- avoid unsupported claims about solved turbulence, real-time deployment, physical consistency, broad generalization, or state-of-the-art status.

## Scorecard

| Axis | Score 0--3 | Notes |
|---|---:|---|
| LaTeX compilability |  |  |
| Review-paper structure |  |  |
| RANS/LES distinction |  |  |
| A priori vs a posteriori evidence |  |  |
| Coupled-solver validation |  |  |
| Invariance/realizability/stability |  |  |
| UQ/verifiability |  |  |
| Reproducibility discipline |  |  |
| Figure/table evidence logic |  |  |
| Field-native vocabulary |  |  |
| Non-hallucination |  |  |

Minimum internal pass: average score >= 2.3 and no score below 1 on LaTeX compilability, non-hallucination, or coupled-solver validation.

## Common failure modes

| Failure | Why it matters |
|---|---|
| Treats a priori regression as deployment proof | Closure feedback can destabilize or degrade the solver. |
| Merges RANS and LES | The closures, diagnostics, and solver risks differ. |
| Says invariant means physically consistent | Invariance is necessary evidence, not full validation. |
| Omits realizability or boundedness | Tensor outputs can be numerically unsafe. |
| Claims real-time speedup from neural inference only | Solver coupling and hardware/runtime dominate deployment claims. |
| Uses external figures | Benchmark must compile standalone. |
| Invents paper-specific numbers or DOI values | Hallucination. |
