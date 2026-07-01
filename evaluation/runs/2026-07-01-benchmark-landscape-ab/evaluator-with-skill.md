# Deterministic LaTeX evaluator report: main.tex

- Benchmark: `benchmark-landscape-review`
- Source: `evaluation/runs/2026-07-01-benchmark-landscape-ab/with_skill/main.tex`
- Judge type: deterministic surface checks only; this is not a semantic LLM review.
- Compile check: **not-run** - Compile check skipped; use --compile to enable.
- Simple score: **11/11** checks passed.

## Scorecard

| Check | Result | Detail |
|---|---:|---|
| Input file | pass | evaluation/runs/2026-07-01-benchmark-landscape-ab/with_skill/main.tex |
| Document class | pass | Expected \documentclass{...}. |
| Title | pass | Expected title/maketitle. |
| Abstract | pass | Expected abstract environment. |
| Required sections | pass | 7/7: Introduction, Benchmark, Validation, Reproducibility, Failure, Research agenda, Conclusion |
| Figure count | pass | 3 found; benchmark minimum is 3. |
| Table count | pass | 4 table-like environments found; benchmark minimum is 2. |
| Bibliography/TODO | pass | Expected bibliography marker and TODO discipline for missing evidence. |
| Required CFD terms | pass | 14/14: dataset, benchmark, split, validation, reproducibility, failure, surrogate, geometry, mesh, solver, source, license, PDEBench, DeepXDE |
| reviewer-trap markers | pass | Expected reviewer-trap markers with evidence language. |
| Risky phrase discipline | pass | 1 risky hits; 0 appear unbounded by TODO/limitation context. |

## Risky Phrase Scan

| Phrase | Line | Bounded? | Context |
|---|---:|---:|---|
| `conservation` | 20 | yes |  This review treats benchmark design as a claim-evidence problem. The first question is not which model is best, but which claim the benchmark can support. A random snapshot split supports a different claim from a held-out geometry split; same-grid field error supports a different claim from mesh-transfer conservation or force-coefficient agreement; offline inference timing supports a different claim from coupled-solver wall-clock speedup. Missing source details, license terms, solver settings, dataset sizes, and leaderboard numbers are therefore marked as TODO rather than filled in from memory.  |

## Interpretation Limits

This script checks visible LaTeX structure, benchmark-specific markers, risky phrases, and term coverage.
It cannot verify factual correctness, novelty, citation accuracy, solver settings, or whether a claim is scientifically true.
Use manual rubric review for semantic quality and keep unknown facts marked as TODO.
