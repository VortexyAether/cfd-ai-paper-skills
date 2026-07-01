# Deterministic LaTeX evaluator report: main.tex

- Benchmark: `trend-review`
- Source: `/Users/va/Obsidian/VA_obs/20_Research/CFD-AI_Paper_Skills_Package/evaluation/runs/2026-07-01-trend-review-ab/with_skill/main.tex`
- Judge type: deterministic surface checks only; this is not a semantic LLM review.
- Compile check: **not-run** - Compile check skipped; use --compile to enable.
- Simple score: **11/11** checks passed.

## Scorecard

| Check | Result | Detail |
|---|---:|---|
| Input file | pass | /Users/va/Obsidian/VA_obs/20_Research/CFD-AI_Paper_Skills_Package/evaluation/runs/2026-07-01-trend-review-ab/with_skill/main.tex |
| Document class | pass | Expected \documentclass{...}. |
| Title | pass | Expected title/maketitle. |
| Abstract | pass | Expected abstract environment. |
| Required sections | pass | 7/7: Introduction, Taxonomy, Validation, Reproducibility, Reviewer, Research agenda, Conclusion |
| Figure count | pass | 3 found; benchmark minimum is 3. |
| Table count | pass | 8 table/tabular markers found; benchmark minimum is 2. |
| Bibliography/TODO | pass | Expected bibliography marker and TODO discipline for missing evidence. |
| Required CFD terms | pass | 9/9: geometry, mesh, neural operator, graph, workflow, validation, boundary, uncertainty, reproducibility |
| reviewer-trap markers | pass | Expected reviewer-trap markers with evidence language. |
| Risky phrase discipline | pass | 7 risky hits; 0 appear unbounded by TODO/limitation context. |

## Risky Phrase Scan

| Phrase | Line | Bounded? | Context |
|---|---:|---:|---|
| `conservation` | 43 | yes | \section{Method-Family Map} Regular-grid neural operators, such as FNO-style surrogates, are useful when fields live on structured domains and boundary conditions are controlled. Their limitation is not speed after training, but whether the learned operator remains meaningful under mesh changes, geometry changes, and new nondimensional regimes. Physics-informed neural operators and related constrained surrogates add PDE residuals, boundary losses, or conservation-inspired terms, but residual minimization should not be equated with CFD-grade physical fidelity unless diagnostics and coupled tests support it.  |
| `physically consistent` | 75 | yes | Mesh independence & mesh-refinement and cross-mesh tests & call it mesh-specific performance \\ Physical fidelity & spectra, forces, residuals, wall shear, heat flux, or conservation diagnostics & avoid ``physically consistent'' language \\ Deployment or speed & hardware, runtime, memory, batch size, coupling overhead & mark runtime/deployment TODO \\ |
| `conservation` | 75 | yes | Mesh independence & mesh-refinement and cross-mesh tests & call it mesh-specific performance \\ Physical fidelity & spectra, forces, residuals, wall shear, heat flux, or conservation diagnostics & avoid ``physically consistent'' language \\ Deployment or speed & hardware, runtime, memory, batch size, coupling overhead & mark runtime/deployment TODO \\ |
| `generalizable` | 113 | yes | \midrule Geometry-generalizable surrogate & Requires held-out geometry tests & evaluated on the supplied geometry split; geometry transfer TODO \\ Physically consistent prediction & Needs diagnostics, not only loss terms & includes residual/force/spectrum diagnostics where reported \\ |
| `physically consistent` | 114 | yes | Geometry-generalizable surrogate & Requires held-out geometry tests & evaluated on the supplied geometry split; geometry transfer TODO \\ Physically consistent prediction & Needs diagnostics, not only loss terms & includes residual/force/spectrum diagnostics where reported \\ Real-time CFD & Needs hardware and coupling evidence & low-latency inference reported only when runtime is stated \\ |
| `real-time` | 115 | yes | Physically consistent prediction & Needs diagnostics, not only loss terms & includes residual/force/spectrum diagnostics where reported \\ Real-time CFD & Needs hardware and coupling evidence & low-latency inference reported only when runtime is stated \\ State-of-the-art & Needs same-data comparison & outperforms named baselines under the reported split \\ |
| `state-of-the-art` | 116 | yes | Real-time CFD & Needs hardware and coupling evidence & low-latency inference reported only when runtime is stated \\ State-of-the-art & Needs same-data comparison & outperforms named baselines under the reported split \\ Solved complex CFD & Unsupported field-wide claim & improves selected surrogate tasks under stated regimes \\ |

## Interpretation Limits

This script checks visible LaTeX structure, benchmark-specific markers, risky phrases, and term coverage.
It cannot verify factual correctness, novelty, citation accuracy, solver settings, or whether a claim is scientifically true.
Use manual rubric review for semantic quality and keep unknown facts marked as TODO.
