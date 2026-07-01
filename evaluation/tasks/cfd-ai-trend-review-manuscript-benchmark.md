# Task: CFD-AI trend review manuscript benchmark

## Purpose

This is a stronger benchmark than a single-method mini-paper. It tests whether a model can write a CFD-AI **review manuscript seed** about a specific trend without collapsing into a citation dump, hype essay, or generic “AI for CFD” overview.

The benchmark stresses:

- taxonomy building,
- trend framing,
- close-prior-art separation,
- evidence/limitation discipline,
- figure/table planning,
- review-paper LaTeX production.

## Review topic

**Trend:** Geometry-aware neural operators and mesh-based graph surrogates for CFD: moving from regular-grid benchmarks toward complex geometries, unstructured meshes, and engineering validation.

This trend is intentionally specific. It sits between neural operators, GNN/mesh surrogates, CFD acceleration, geometry generalization, and trustworthy validation.

## Skills under test

Primary:

- `related-work-synthesis`
- `related-work-cartographer`
- `scientific-journal-writing`
- `paper-claim-auditor`
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
- `references/gold-papers/vinuesa-2022-enhancing-cfd-ml.md`
- `references/gold-papers/vinuesa-2023-transformative-ml-experiments-nrp.md`
- `references/gold-papers/maulik-2023-multiscale-gnn-autoencoders-jcp.md`
- `references/field-terminology-style-guide.md`
- `rubrics/vocabulary-style-rubric.md`
- `rubrics/claim-evidence-rubric.md`
- `rubrics/sciml-experiment-rubric.md`
- `rubrics/figure-evidence-rubric.md`

## Dumb-agent / model prompt

You are writing a CFD-AI / scientific-ML **review article seed** in LaTeX. Your output must be a complete compilable `main.tex` file, not a bullet memo.

### Target

Draft a 5--7 page mini-review manuscript seed suitable for a Journal of Computational Physics / Physics of Fluids / Nature Computational Science perspective-style article.

### Review title

**Geometry-aware neural operators and mesh-based graph surrogates for CFD: from regular-grid benchmarks to engineering validation**

### Review thesis

The review should argue that CFD-AI surrogate modeling is moving from regular-grid proof-of-concepts toward geometry-aware and mesh-aware models, but that the field is bottlenecked by geometry generalization, boundary-condition transfer, mesh dependence, physical diagnostics, uncertainty, and reproducibility.

### Evidence packet

Use only the evidence below. You may use placeholder citation keys, but do not invent bibliographic details, DOI values, author lists, benchmark numbers, or paper-specific claims not provided here.

#### Known method families to cover

1. **Regular-grid neural operators**
   - Examples: FNO-style and operator-learning surrogates on structured domains.
   - Strength: fast mapping between discretized function spaces after training.
   - Limitation: often easiest on regular grids, fixed domains, or controlled boundary conditions.

2. **Physics-informed neural operators / physics-constrained surrogates**
   - Strength: can include PDE residuals, boundary-condition penalties, or conservation-inspired losses.
   - Limitation: residual minimization does not automatically guarantee CFD-grade validation; residual weighting and stiffness can dominate results.

3. **Mesh-based graph neural networks / graph autoencoders**
   - Strength: can represent unstructured meshes and local connectivity.
   - Limitation: mesh resolution, graph construction, message-passing depth, and long-horizon stability remain concerns.

4. **Geometry-conditioned surrogates**
   - Strength: can condition predictions on airfoil/body/channel/roughness descriptors or signed-distance/implicit geometry fields.
   - Limitation: true geometry generalization requires held-out geometries, not random snapshot splits.

5. **Hybrid CFD-ML workflows**
   - Strength: may accelerate selected solver stages, provide ROMs, initialize solvers, estimate closure terms, or support design loops.
   - Limitation: deployment requires error bounds, coupling stability, runtime/hardware reporting, and failure detection.

#### CFD validation axes the review must emphasize

- flow regime: laminar / transitional / turbulent;
- geometry: canonical case vs complex engineering body;
- mesh: structured vs unstructured, mesh refinement sensitivity;
- boundary and initial conditions;
- nondimensional groups: Reynolds number, Mach number, Peclet number where relevant;
- quantities of interest: velocity, pressure, vorticity, drag/lift, wall shear stress, heat flux;
- diagnostics: relative error, spectra, force coefficients, conservation/residuals, long-rollout drift, uncertainty/calibration;
- split design: random snapshot split vs held-out time, Reynolds number, geometry, boundary condition, or mesh;
- reproducibility: solver, grid, seeds, code/data availability, hardware/runtime.

#### Review claim boundaries

The review may say:

- neural operators and graph surrogates are promising for selected CFD surrogate tasks;
- geometry-aware and mesh-aware models address limitations of regular-grid surrogates;
- validation must move beyond random snapshot splits and visual field comparisons;
- CFD-AI review papers should classify methods by workflow role and validation axis.

The review must not say as fact:

- neural operators have solved CFD surrogate modeling;
- mesh-based GNNs are generally geometry-generalizable;
- physics-informed losses ensure physical consistency;
- these models are real-time or deployable without hardware/runtime evidence;
- one method family is state-of-the-art without a same-data/same-split comparison;
- 3D turbulent engineering flows are solved unless specific evidence is supplied.

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
2. Abstract with review-paper moves:
   - field context,
   - trend/gap,
   - taxonomy contribution,
   - validation agenda,
   - limitation boundary.
3. Introduction explaining why geometry/mesh awareness is the next CFD-AI bottleneck.
4. A taxonomy section organized first by **CFD workflow role**, then by **ML method family**.
5. A section on validation axes and failure modes.
6. A section on reproducibility requirements for CFD surrogate papers.
7. At least two tables:
   - method-family taxonomy table;
   - validation checklist table.
8. At least three figure placeholders using boxed `figure` environments, no external image files:
   - trend map / workflow map;
   - geometry-and-mesh generalization matrix;
   - validation funnel from visual fields to deployment evidence.
9. A “Reviewer traps” section listing 6--8 common overclaims and how to rewrite them.
10. A “Research agenda” section with concrete open problems.
11. Conclusion with scoped claims.
12. `thebibliography` with placeholder entries only, e.g. `\bibitem{brunton2020mlfluid} TODO: verified entry...`.

### Hard constraints

- Use `TODO` for missing bibliography and unsupported evidence.
- Do not invent exact benchmark numbers, datasets, author lists, venues, DOI values, or solver settings.
- Do not organize the review as a chronological citation list.
- Do not use `robust`, `generalizable`, `physically consistent`, `state-of-the-art`, or `real-time` unless immediately bounded by evidence or flagged as unsupported.
- Every figure caption must state what claim the figure supports.
- Every table must include a limitation or validation column.
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
- produce a review-paper structure rather than a single-method paper;
- classify the trend by CFD workflow role before ML method family;
- distinguish regular-grid operators, physics-informed operators, mesh GNNs, geometry-conditioned surrogates, and hybrid CFD-ML workflows;
- define validation axes: regime, geometry, mesh, BC/IC, QoIs, diagnostics, splits, reproducibility;
- include at least two meaningful tables and three evidence-linked figure placeholders;
- mark bibliography and missing evidence as TODO;
- avoid unsupported claims about real-time deployment, broad geometry generalization, physical consistency, state-of-the-art status, or solved 3D turbulence;
- include reviewer-trap rewrites and a concrete research agenda.

## Scorecard

| Axis | Score 0--3 | Notes |
|---|---:|---|
| LaTeX compilability |  |  |
| Review-paper structure |  |  |
| Trend specificity |  |  |
| Workflow-first taxonomy |  |  |
| Method-family coverage |  |  |
| Validation-axis depth |  |  |
| Reproducibility discipline |  |  |
| Reviewer-trap handling |  |  |
| Figure/table evidence logic |  |  |
| Field-native vocabulary |  |  |
| Non-hallucination |  |  |

Minimum internal pass: average score $\ge 2.3$ and no score below 1 on LaTeX compilability, non-hallucination, or workflow-first taxonomy.

## Common failure modes

| Failure | Why it matters |
|---|---|
| Citation dump | Review does not teach the field structure. |
| Method-family-only taxonomy | Ignores where ML enters the CFD workflow. |
| Claims geometry generalization from random splits | Invalid validation logic. |
| Says physics-informed means physically consistent | Residual terms are not enough without diagnostics. |
| Omits mesh/BC/geometry axes | Misses the trend’s central bottleneck. |
| Uses external figures | Benchmark must compile standalone. |
| Invents specific benchmark numbers | Hallucination. |
| Turns the review into one proposed method paper | Wrong genre. |
