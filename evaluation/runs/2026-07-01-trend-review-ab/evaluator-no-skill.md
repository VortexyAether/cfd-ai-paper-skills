# Deterministic LaTeX evaluator report: main.tex

- Benchmark: `trend-review`
- Source: `evaluation/runs/2026-07-01-trend-review-ab/no_skill/main.tex`
- Judge type: deterministic surface checks only; this is not a semantic LLM review.
- Compile check: **not-run** - Compile check skipped; use --compile to enable.
- Simple score: **9/11** checks passed.

## Scorecard

| Check | Result | Detail |
|---|---:|---|
| Input file | pass | evaluation/runs/2026-07-01-trend-review-ab/no_skill/main.tex |
| Document class | pass | Expected \documentclass{...}. |
| Title | pass | Expected title/maketitle. |
| Abstract | pass | Expected abstract environment. |
| Required sections | pass | 7/7: Introduction, Taxonomy, Validation, Reproducibility, Reviewer, Research agenda, Conclusion |
| Figure count | pass | 3 found; benchmark minimum is 3. |
| Table count | pass | 4 table/tabular markers found; benchmark minimum is 2. |
| Bibliography/TODO | pass | Expected bibliography marker and TODO discipline for missing evidence. |
| Required CFD terms | pass | 8/9: geometry, mesh, neural operator, graph, workflow, validation, boundary, reproducibility |
| reviewer-trap markers | fail | Expected reviewer-trap markers with evidence language. |
| Risky phrase discipline | fail | 16 risky hits; 9 appear unbounded by TODO/limitation context. |

## Risky Phrase Scan

| Phrase | Line | Bounded? | Context |
|---|---:|---:|---|
| `robust` | 15 | yes | \begin{abstract} Artificial intelligence is rapidly transforming computational fluid dynamics by enabling fast and accurate prediction of complex flows. Neural operators and graph neural networks provide state-of-the-art tools for learning flow maps across geometries and meshes. This review surveys geometry-aware neural operators, mesh-based graph surrogates, physics-informed models, and hybrid CFD-ML workflows. These approaches are robust, physically consistent, and promising for real-time CFD applications. We discuss their advantages, limitations, and future directions, showing that AI-based surrogates will play an important role in next-generation engineering simulation. \end{abstract} |
| `physically consistent` | 15 | yes | \begin{abstract} Artificial intelligence is rapidly transforming computational fluid dynamics by enabling fast and accurate prediction of complex flows. Neural operators and graph neural networks provide state-of-the-art tools for learning flow maps across geometries and meshes. This review surveys geometry-aware neural operators, mesh-based graph surrogates, physics-informed models, and hybrid CFD-ML workflows. These approaches are robust, physically consistent, and promising for real-time CFD applications. We discuss their advantages, limitations, and future directions, showing that AI-based surrogates will play an important role in next-generation engineering simulation. \end{abstract} |
| `real-time` | 15 | yes | \begin{abstract} Artificial intelligence is rapidly transforming computational fluid dynamics by enabling fast and accurate prediction of complex flows. Neural operators and graph neural networks provide state-of-the-art tools for learning flow maps across geometries and meshes. This review surveys geometry-aware neural operators, mesh-based graph surrogates, physics-informed models, and hybrid CFD-ML workflows. These approaches are robust, physically consistent, and promising for real-time CFD applications. We discuss their advantages, limitations, and future directions, showing that AI-based surrogates will play an important role in next-generation engineering simulation. \end{abstract} |
| `state-of-the-art` | 15 | yes | \begin{abstract} Artificial intelligence is rapidly transforming computational fluid dynamics by enabling fast and accurate prediction of complex flows. Neural operators and graph neural networks provide state-of-the-art tools for learning flow maps across geometries and meshes. This review surveys geometry-aware neural operators, mesh-based graph surrogates, physics-informed models, and hybrid CFD-ML workflows. These approaches are robust, physically consistent, and promising for real-time CFD applications. We discuss their advantages, limitations, and future directions, showing that AI-based surrogates will play an important role in next-generation engineering simulation. \end{abstract} |
| `generalize` | 21 | no |  The field is moving from simple regular-grid benchmarks toward geometry-aware and mesh-aware models. This transition is important because engineering flows involve complex bodies, unstructured meshes, variable boundary conditions, and many Reynolds numbers. Geometry-aware neural operators and mesh-based graph surrogates can generalize across these cases and therefore provide a pathway toward real-time simulation and optimization.  |
| `real-time` | 21 | no |  The field is moving from simple regular-grid benchmarks toward geometry-aware and mesh-aware models. This transition is important because engineering flows involve complex bodies, unstructured meshes, variable boundary conditions, and many Reynolds numbers. Geometry-aware neural operators and mesh-based graph surrogates can generalize across these cases and therefore provide a pathway toward real-time simulation and optimization.  |
| `physically consistent` | 34 | no | Neural operators & Fast prediction & Need training data \\ Physics-informed operators & Physically consistent & Hard to tune \\ Graph surrogates & Complex meshes & Expensive training \\ |
| `generalizable` | 36 | no | Graph surrogates & Complex meshes & Expensive training \\ Geometry-conditioned models & Generalizable & Need many geometries \\ Hybrid CFD-ML & Practical deployment & Coupling complexity \\ |
| `robust` | 43 | no | \section{Validation and Failure Modes} Validation is important for CFD-AI. Models should be tested on accuracy, speed, physical consistency, and robustness. Good validation includes relative error, visualization, force coefficients, spectra, and generalization to new geometries. Random splits are useful for evaluating performance, while held-out geometries can test generalization.  |
| `physical consistency` | 43 | no | \section{Validation and Failure Modes} Validation is important for CFD-AI. Models should be tested on accuracy, speed, physical consistency, and robustness. Good validation includes relative error, visualization, force coefficients, spectra, and generalization to new geometries. Random splits are useful for evaluating performance, while held-out geometries can test generalization.  |
| `real-time` | 55 | no | Generalization & New geometry error & Low \\ Speed & Runtime & Real-time \\ Robustness & Noise and OOD tests & Stable \\ |
| `robust` | 56 | no | Speed & Runtime & Real-time \\ Robustness & Noise and OOD tests & Stable \\ \bottomrule |
| `deployment-ready` | 80 | no | \fbox{\parbox{0.85\linewidth}{Placeholder: validation funnel from visual fields to deployment.}} \caption{Validation should move from visual checks to deployment-ready CFD models.} \end{figure} |
| `real-time` | 84 | yes | \section{Reviewer Traps} Common concerns include lack of generalization, insufficient physics, missing real-time benchmarks, and limited comparisons. These can be addressed by adding more datasets, stronger baselines, and better physical losses.  |
| `robust` | 87 | yes | \section{Research Agenda} Future work should develop more robust neural operators, improve graph learning on unstructured meshes, integrate physics more strongly, and build real-time digital twins for engineering design. Combining CFD solvers with neural surrogates will enable fast optimization and control.  |
| `real-time` | 87 | yes | \section{Research Agenda} Future work should develop more robust neural operators, improve graph learning on unstructured meshes, integrate physics more strongly, and build real-time digital twins for engineering design. Combining CFD solvers with neural surrogates will enable fast optimization and control.  |

## Interpretation Limits

This script checks visible LaTeX structure, benchmark-specific markers, risky phrases, and term coverage.
It cannot verify factual correctness, novelty, citation accuracy, solver settings, or whether a claim is scientifically true.
Use manual rubric review for semantic quality and keep unknown facts marked as TODO.
