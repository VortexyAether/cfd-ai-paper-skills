# Task: CFD-AI full manuscript generation benchmark

## Purpose

This benchmark is designed to test whether a model can use the CFD-AI/SciML paper skill package to draft a reviewer-defensible LaTeX manuscript, not merely produce generic academic prose.

The task intentionally includes enough evidence to write a scoped paper, plus several tempting but unsupported claims. A good model should convert unsupported claims into limitations/TODOs instead of polishing them.

## Skill under test

Primary:

- `scientific-journal-writing`
- `latex-paper-production`
- `paper-claim-auditor`
- `sciml-experiment-auditor`
- `figure-and-result-storytelling`
- `cfd-reproducibility-checker`
- `related-work-synthesis`

Optional:

- `journal-submission-checklist`
- `reviewer-simulator`

## Gold-answer references

Read when available:

- `references/gold-papers/fukami-2019-super-resolution-jfm.md`
- `references/gold-papers/fukami-2021-spatiotemporal-super-resolution-jfm.md`
- `references/gold-papers/brunton-2020-machine-learning-fluid-mechanics.md`
- `references/gold-papers/vinuesa-2022-enhancing-cfd-ml.md`
- `references/field-terminology-style-guide.md`
- `rubrics/claim-evidence-rubric.md`
- `rubrics/sciml-experiment-rubric.md`
- `rubrics/figure-evidence-rubric.md`

## Dumb-agent / model prompt

You are writing a CFD-AI / scientific-ML journal manuscript seed in LaTeX. Your output must be a complete compilable `main.tex` file, not a prose memo.

### Target

Draft a 4--6 page mini-manuscript suitable as an early seed for a Journal of Fluid Mechanics / Physics of Fluids / Journal of Computational Physics style paper.

### Paper topic

**Title idea:** Regime-scoped super-resolution of two-dimensional wake and decaying-turbulence vorticity fields using a residual convolutional reconstruction model.

The paper studies a neural reconstruction model that maps coarse vorticity snapshots to high-resolution vorticity fields. The scientific objective is to evaluate whether learned reconstruction improves field accuracy and selected turbulence diagnostics compared with classical interpolation and a small U-Net baseline.

### Evidence packet

Use only the evidence below. Do not invent solver details, author names, citations, DOI, dataset links, code repositories, or exact numerical values not provided here.

#### Flow cases

1. **Circular-cylinder wake**
   - Governing regime: two-dimensional incompressible flow.
   - Reynolds number: $Re_D=100$ for training/in-regime testing.
   - Out-of-regime probe: $Re_D=300$ wake snapshots are used only as a stress test.
   - Quantity reconstructed: scalar vorticity $\omega$.

2. **Homogeneous decaying turbulence**
   - Governing regime: two-dimensional incompressible decaying turbulence.
   - Quantity reconstructed: scalar vorticity $\omega$.
   - Evaluation emphasizes high-wavenumber spectral content.

#### Data and downsampling

- High-resolution vorticity snapshots are downsampled spatially by factors $r=4$ and $r=8$.
- The low-resolution input is upsampled internally by the model to produce a high-resolution vorticity field.
- Train/validation/test snapshots are separated by time index; exact split counts are not provided.
- Boundary conditions, grid resolution, solver, time step, CFL number, snapshot cadence, random seeds, and data availability are **not provided**.

#### Model

- Proposed model: residual convolutional reconstruction network with multiscale skip paths.
- Loss: normalized $L_2$ reconstruction loss on vorticity.
- Baselines:
  1. bicubic interpolation,
  2. small U-Net reconstruction baseline.

#### Results provided

- At $r=4$ on in-regime cylinder-wake test snapshots, the proposed model reduces relative $L_2$ vorticity error by **22% vs bicubic interpolation** and **9% vs the small U-Net**.
- At $r=8$, the proposed model still improves over bicubic interpolation, but the performance gap to U-Net is smaller. Exact number is not provided.
- For decaying turbulence, the proposed model better preserves the qualitative high-wavenumber trend of the vorticity spectrum than bicubic interpolation. Exact spectral error values are not provided.
- Vorticity-PDF agreement improves relative to bicubic interpolation for in-regime turbulence snapshots. Exact KL divergence or statistical metric is not provided.
- On $Re_D=300$, error increases and shear-layer extrema are visibly smoothed. This is a limitation, not a success claim.

#### Claims that are **not** supported

The following claims must not be stated as facts:

- real-time inference,
- general CFD acceleration,
- 3D turbulence validity,
- experimental PIV validity,
- conservation or Navier--Stokes residual consistency,
- state-of-the-art performance,
- broad Reynolds-number generalization,
- deployability for control or design loops.

If relevant, mention these as future work or TODO evidence.

### Required LaTeX output

Generate one complete compilable LaTeX file using standard packages only: `article`, `geometry`, `amsmath`, `booktabs`, `graphicx`, `hyperref`.

The file must include:

1. Title.
2. Abstract with five moves:
   - physical/numerical context,
   - gap,
   - method,
   - concrete evidence,
   - scoped implication/limitation.
3. Introduction with field-native positioning, not generic “AI improves CFD”.
4. Related-work paragraph organized by CFD-ML role, not citation chronology. Since citations are not provided, use placeholder citation keys only where necessary, e.g. `\cite{fukami2019superresolution,brunton2020mlfluid,vinuesa2022enhancing}` and mark bibliography TODO.
5. Methods section including:
   - problem definition,
   - downsampling operator,
   - model mapping,
   - loss function,
   - baseline matrix,
   - missing reproducibility details as TODOs.
6. Results section with:
   - quantitative reconstruction result,
   - physical/statistical diagnostics,
   - generalization stress test,
   - limitations.
7. A figure plan using `figure` environments with boxed placeholders, not external image files. Each caption must state what claim the figure would support.
8. A claim--evidence table using `booktabs`.
9. Reviewer-risk paragraph listing 4--6 attack points.
10. Conclusion with scoped claims only.
11. A small `thebibliography` block with placeholder entries or a clear TODO statement.

### Hard constraints

- Use the phrase `TODO` for missing evidence.
- Do not use the words `robust`, `state-of-the-art`, `real-time`, `physically consistent`, or `generalizable` unless immediately bounded by explicit evidence or stated as unsupported.
- Do not claim conservation/residual correctness because no residual audit is provided.
- Do not invent numerical settings.
- Do not cite specific papers beyond placeholder citation keys unless they are in the prompt.
- Make the manuscript sound like a cautious CFD/SciML draft, not a startup demo.

### Output format

Return only the LaTeX source code inside one fenced code block:

```latex
...
```

## Evaluator instructions

Evaluate the output with:

- `rubrics/claim-evidence-rubric.md`
- `rubrics/sciml-experiment-rubric.md`
- `rubrics/figure-evidence-rubric.md`
- `rubrics/cfd-reproducibility-rubric.md`
- `rubrics/vocabulary-style-rubric.md`

## Expected pass criteria

A pass-level output should:

- compile with Tectonic or standard LaTeX without fatal errors;
- contain an explicit claim--evidence table;
- state exact supported numerical claims: 22% vs bicubic, 9% vs U-Net for $r=4$ in-regime wake;
- avoid unsupported `real-time`, `state-of-the-art`, `general CFD acceleration`, `3D`, `PIV`, and conservation-residual claims;
- include TODOs for solver/grid/BC/time-step/split/seed/code details;
- treat $Re_D=300$ as a stress-test limitation;
- use field-native vocabulary: vorticity, downsampling, Reynolds number, spectrum, vorticity PDF, shear-layer extrema, relative $L_2$ error;
- organize related work by CFD-ML role, not a random citation list;
- include figure placeholders whose captions map to specific claims.

## Common failure modes

| Failure | Why it matters |
|---|---|
| Claims “physically consistent” from visual similarity | No residual/conservation evidence was supplied. |
| Claims “real-time” | No runtime or hardware evidence. |
| Claims general Reynolds-number validity | $Re_D=300$ degrades. |
| Omits baselines | Reviewer cannot judge contribution. |
| Omits TODOs | Model is inventing reproducibility details. |
| Writes only abstract/introduction | Fails full-manuscript benchmark. |
| Uses external images | Benchmark should compile standalone. |

## Scorecard

| Axis | Score 0--3 | Notes |
|---|---:|---|
| LaTeX compilability |  |  |
| Physics/regime specificity |  |  |
| Claim-evidence alignment |  |  |
| Baseline fairness |  |  |
| Physical diagnostics |  |  |
| Reproducibility/TODO discipline |  |  |
| Limitation honesty |  |  |
| Figure/story logic |  |  |
| Field-native vocabulary |  |  |
| Non-hallucination |  |  |

Minimum internal pass: average score $\ge 2.2$ and no score below 1 on claim-evidence, non-hallucination, or LaTeX compilability.
