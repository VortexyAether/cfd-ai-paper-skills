# Task: CFD-AI benchmark landscape review

## Purpose

This benchmark tests whether an agent can design a CFD-AI benchmark landscape review that classifies datasets and tools by validation axis, split design, failure mode, and reproducibility rather than listing popular resources.

It stresses:

- benchmark taxonomy;
- dataset/tool source-scope honesty;
- validation-axis classification;
- split-design critique;
- failure-mode analysis;
- reproducibility and license/data logistics;
- cautious review-paper LaTeX production.

## Review topic

**Trend:** Benchmarking CFD-AI models across surrogate modeling, physics-informed learning, solver acceleration, turbulence closure, reconstruction, aerodynamic design, flow control, and multiphase flows.

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

- `references/cfd-ai-benchmark-landscape.md`
- `references/related-projects-distillation.md`
- `references/gold-papers/brunton-2020-machine-learning-fluid-mechanics.md`
- `references/gold-papers/vinuesa-2022-enhancing-cfd-ml.md`
- `references/gold-papers/vinuesa-2023-transformative-ml-experiments-nrp.md`
- `references/field-terminology-style-guide.md`
- `rubrics/claim-evidence-rubric.md`
- `rubrics/cfd-reproducibility-rubric.md`
- `rubrics/sciml-experiment-rubric.md`
- `rubrics/figure-evidence-rubric.md`

## Baseline-agent / model prompt

You are writing a CFD-AI / scientific-ML **review article seed** in LaTeX. Your output must be a complete compilable `main.tex` file, not a bullet memo.

### Target

Draft a 5--7 page mini-review manuscript seed for a Journal of Computational Physics / Computer Methods in Applied Mechanics and Engineering / Nature Computational Science perspective-style article.

### Review title

**How should CFD-AI benchmarks be reviewed? Validation axes, splits, failure modes, and reproducibility**

### Review thesis

The review should argue that CFD-AI benchmark quality depends less on the number of datasets listed and more on whether each benchmark tests the intended validation axis: geometry, mesh, regime, boundary condition, time horizon, quantities of interest, solver coupling, uncertainty, and reproducibility.

### Evidence packet

Use only the evidence below. You may use placeholder citation keys, but do not invent bibliographic details, DOI values, exact dataset sizes, author lists, benchmark numbers, or solver settings.

#### Resources to classify

1. **PDEBench-like scientific-ML PDE benchmarks**
   - Role: broad PDE benchmark datasets with generation/evaluation code and baseline models.
   - Validation axes: PDE family, forward/inverse task, parameters, boundary/initial conditions.
   - Risk: treating broad PDE performance as CFD deployment evidence.

2. **DeepXDE-like physics-informed learning tools**
   - Role: PINN and scientific-ML tooling for forward/inverse PDE problems and complex geometries.
   - Validation axes: residual formulation, BC/IC handling, optimizer, geometry, data availability.
   - Risk: tool support is mistaken for benchmark validation.

3. **DrivAerNet-like aerodynamic datasets**
   - Role: automotive geometry/CFD data for drag, fields, geometry-conditioned surrogates, and design.
   - Validation axes: held-out geometries, meshes, force coefficients, surface/flow fields, license.
   - Risk: random or near-duplicate geometry splits overstate design generalization.

4. **The Well-like physics simulation collections**
   - Role: large spatiotemporal simulation datasets and benchmark infrastructure across physics domains.
   - Validation axes: dataset-specific physics, temporal rollout, model families, data logistics.
   - Risk: broad physics coverage is treated as CFD-specific coverage.

5. **Curated ML-fluid resource lists**
   - Role: inventories of papers, datasets, tools, open-source CFD codes, and application areas.
   - Validation axes: source scope, update date, domain coverage.
   - Risk: list inclusion is mistaken for benchmark quality.

#### CFD-AI areas to cover

- data-driven surrogates;
- physics-informed surrogates;
- ML-assisted numerical solutions;
- turbulence closure;
- PIV/reconstruction;
- lift/drag/aerodynamic design;
- flow control;
- multiphase/reacting/non-Newtonian flows.

#### Benchmark claim boundaries

The review may say:

- benchmark design should specify workflow role and validation axis;
- held-out geometry, mesh, BC/IC, regime, and time-horizon splits test different claims;
- source scope and reproducibility metadata matter as much as model architecture;
- benchmark papers should report failure modes and data logistics.

The review must not say as fact:

- a resource is comprehensive for all CFD-AI;
- a dataset proves deployability without solver/runtime evidence;
- a model family is state-of-the-art without same-data/same-split comparison;
- exact dataset sizes, licenses, or benchmark scores unless supplied.

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
2. Abstract with review-paper moves: field context, benchmark gap, taxonomy contribution, validation agenda, limitation boundary.
3. Introduction explaining why CFD-AI benchmark reviews need validation-axis classification.
4. Benchmark taxonomy organized by CFD workflow role and validation axis.
5. Section classifying datasets/tools by split design.
6. Section on failure modes and reviewer traps.
7. Section on reproducibility, licensing, and data logistics.
8. At least two tables:
   - resource classification table;
   - validation-axis/split-design table.
   - source-boundary table distinguishing datasets, tools, benchmark suites, curated lists, and review claims.
9. At least three boxed figure placeholders:
   - benchmark landscape map;
   - split-design decision tree;
   - failure-mode/reproducibility funnel.
10. A "Reviewer traps" section with 6--8 overclaims and safer rewrites.
11. A concrete research agenda.
12. `thebibliography` with placeholder entries only, e.g. `\bibitem{pdebench} TODO: verified entry...`.

### Hard constraints

- Use `TODO` for missing bibliography and unsupported evidence.
- Do not invent exact dataset sizes, benchmark numbers, DOI values, author lists, license terms, or solver settings.
- Do not turn the review into a list of resources.
- Do not use `robust`, `generalizable`, `physically consistent`, `state-of-the-art`, or `real-time` unless immediately bounded by evidence or flagged as unsupported.
- Every figure caption must state what claim the figure supports.
- Every table must include a limitation, validation, split, or reproducibility column.
- Do not merge held-out time, parameter, geometry, mesh, BC/IC, cross-solver, and coupled-solver axes into one generic "generalization" row.
- Distinguish resource-list coverage from evidence that a benchmark supports a CFD-AI claim.
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
- classify resources by workflow role, validation axis, split design, failure mode, and reproducibility;
- keep source-boundary distinctions explicit: datasets, tools, benchmark suites, curated resource lists, and review claims support different evidence levels;
- force validation axes apart rather than using one generic generalization/accuracy bucket;
- distinguish datasets, tooling, benchmark suites, and curated resource lists;
- cover data-driven surrogates, physics-informed surrogates, ML-assisted numerical solutions, closure, reconstruction, aero, flow control, and multiphase cases;
- include at least two meaningful tables and three evidence-linked figure placeholders;
- include reviewer-trap rewrites and a concrete research agenda;
- mark bibliography and missing evidence as TODO;
- avoid unsupported claims about comprehensive coverage, deployability, state-of-the-art status, real-time use, or solved CFD.

## Scorecard

| Axis | Score 0--3 | Notes |
|---|---:|---|
| LaTeX compilability |  |  |
| Review-paper structure |  |  |
| Resource classification |  |  |
| Validation-axis depth |  |  |
| Split-design critique |  |  |
| Failure-mode analysis |  |  |
| Reproducibility/data logistics |  |  |
| Reviewer-trap handling |  |  |
| Figure/table evidence logic |  |  |
| Field-native vocabulary |  |  |
| Non-hallucination |  |  |

Minimum internal pass: average score >= 2.3 and no score below 1 on LaTeX compilability, non-hallucination, or validation-axis depth.

## Common failure modes

| Failure | Why it matters |
|---|---|
| Resource list instead of taxonomy | It does not help reviewers judge benchmark claims. |
| Merges validation axes into generic generalization | It hides whether the claim is about time, regime, geometry, mesh, BC/IC, solver, or deployment. |
| Treats source scope as evidence strength | A dataset, tool, list, and benchmark suite do not prove the same kind of claim. |
| Omits split design | Benchmark claims depend on what was held out. |
| Treats tools as validation evidence | A library capability does not prove model behavior. |
| Claims comprehensive CFD coverage | Most resources cover only selected domains. |
| Omits data/license/logistics caveats | Reproducibility and reuse can fail outside the model. |
| Uses external figures | Benchmark must compile standalone. |
| Invents dataset sizes or scores | Hallucination. |
