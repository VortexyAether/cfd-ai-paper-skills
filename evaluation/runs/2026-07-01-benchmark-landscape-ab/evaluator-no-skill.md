# Deterministic LaTeX evaluator report: main.tex

- Benchmark: `benchmark-landscape-review`
- Source: `evaluation/runs/2026-07-01-benchmark-landscape-ab/no_skill/main.tex`
- Judge type: deterministic surface checks only; this is not a semantic LLM review.
- Compile check: **not-run** - Compile check skipped; use --compile to enable.
- Simple score: **6/11** checks passed.

## Scorecard

| Check | Result | Detail |
|---|---:|---|
| Input file | pass | evaluation/runs/2026-07-01-benchmark-landscape-ab/no_skill/main.tex |
| Document class | pass | Expected \documentclass{...}. |
| Title | pass | Expected title/maketitle. |
| Abstract | pass | Expected abstract environment. |
| Required sections | fail | 5/7: Introduction, Benchmark, Validation, Failure, Research agenda |
| Figure count | fail | 0 found; benchmark minimum is 3. |
| Table count | pass | 3 table-like environments found; benchmark minimum is 2. |
| Bibliography/TODO | pass | Expected bibliography marker and TODO discipline for missing evidence. |
| Required CFD terms | fail | 12/14: dataset, benchmark, split, validation, reproducibility, failure, surrogate, geometry, mesh, source, PDEBench, DeepXDE |
| reviewer-trap markers | fail | Expected reviewer-trap markers with evidence language. |
| Risky phrase discipline | fail | 12 risky hits; 11 appear unbounded by TODO/limitation context. |

## Risky Phrase Scan

| Phrase | Line | Bounded? | Context |
|---|---:|---:|---|
| `robust` | 14 | no | \begin{abstract} Machine learning has become a state-of-the-art approach for computational fluid dynamics benchmarks. This review summarizes important resources including PDEBench, DeepXDE, DrivAerNet, The Well, and curated machine-learning fluid-mechanics lists. We argue that modern CFD-AI benchmarks are robust, generalizable, and increasingly ready for real-time deployment in engineering design. The article provides a compact overview of datasets, tools, and future directions for AI-based CFD acceleration. \end{abstract} |
| `generalizable` | 14 | no | \begin{abstract} Machine learning has become a state-of-the-art approach for computational fluid dynamics benchmarks. This review summarizes important resources including PDEBench, DeepXDE, DrivAerNet, The Well, and curated machine-learning fluid-mechanics lists. We argue that modern CFD-AI benchmarks are robust, generalizable, and increasingly ready for real-time deployment in engineering design. The article provides a compact overview of datasets, tools, and future directions for AI-based CFD acceleration. \end{abstract} |
| `real-time` | 14 | no | \begin{abstract} Machine learning has become a state-of-the-art approach for computational fluid dynamics benchmarks. This review summarizes important resources including PDEBench, DeepXDE, DrivAerNet, The Well, and curated machine-learning fluid-mechanics lists. We argue that modern CFD-AI benchmarks are robust, generalizable, and increasingly ready for real-time deployment in engineering design. The article provides a compact overview of datasets, tools, and future directions for AI-based CFD acceleration. \end{abstract} |
| `state-of-the-art` | 14 | no | \begin{abstract} Machine learning has become a state-of-the-art approach for computational fluid dynamics benchmarks. This review summarizes important resources including PDEBench, DeepXDE, DrivAerNet, The Well, and curated machine-learning fluid-mechanics lists. We argue that modern CFD-AI benchmarks are robust, generalizable, and increasingly ready for real-time deployment in engineering design. The article provides a compact overview of datasets, tools, and future directions for AI-based CFD acceleration. \end{abstract} |
| `real-time` | 20 | no |  Popular resources such as PDEBench, DeepXDE, DrivAerNet, and The Well collectively show that AI methods can solve a wide range of PDE and CFD problems. These resources also demonstrate the strong generalization capacity of neural networks when trained on enough simulation data. In many cases, reported errors are low enough to support real-time digital twins and fast design loops.  |
| `physically consistent` | 30 | no | PDEBench & Dataset suite & PDE learning & Broad coverage \\ DeepXDE & Tool & PINNs & Physically consistent models \\ DrivAerNet & Dataset & Aerodynamics & Geometry generalization \\ |
| `generalize` | 59 | no | \section{Failure Modes} Benchmark failure modes include overfitting, noisy data, limited resolution, and poor model architecture. However, these problems can usually be addressed by larger models, more data, and better physics-informed losses. Neural operators and graph networks are especially promising because they can generalize across discretizations and geometries.  |
| `state-of-the-art` | 83 | no | Benchmarks are comprehensive & Benchmarks cover many cases \\ Models are state-of-the-art & Models are competitive \\ PINNs are physically consistent & PINNs include physics losses \\ |
| `physically consistent` | 84 | no | Models are state-of-the-art & Models are competitive \\ PINNs are physically consistent & PINNs include physics losses \\ Surrogates are real-time & Surrogates can be fast \\ |
| `real-time` | 85 | no | PINNs are physically consistent & PINNs include physics losses \\ Surrogates are real-time & Surrogates can be fast \\ Models generalize & Models can generalize \\ |
| `generalize` | 86 | no | Surrogates are real-time & Surrogates can be fast \\ Models generalize & Models can generalize \\ \bottomrule |
| `real-time` | 93 | yes | \section{Research Agenda} Future work should add more datasets, larger models, better leaderboards, and more real-time deployment studies. Benchmark maintainers should unify data formats and report accuracy. The community should also create a single comprehensive CFD-AI leaderboard.  |

## Interpretation Limits

This script checks visible LaTeX structure, benchmark-specific markers, risky phrases, and term coverage.
It cannot verify factual correctness, novelty, citation accuracy, solver settings, or whether a claim is scientifically true.
Use manual rubric review for semantic quality and keep unknown facts marked as TODO.
