# Evaluation tasks

Benchmark tasks live under `evaluation/tasks/`. Each task should name the skills under test, source constraints, expected output format, hard constraints, pass criteria, common failure modes, and scorecard axes.

## Task Index

| Task | Purpose | Current gate status |
|---|---|---|
| `cfd-ai-full-manuscript-generation-benchmark.md` | Draft a complete reviewer-defensible LaTeX mini-manuscript from a bounded evidence packet. | Useful manuscript seed gate; current internal A/B separates overclaiming from claim-evidence discipline. |
| `cfd-ai-trend-review-manuscript-benchmark.md` | Draft a review-paper LaTeX seed for geometry-aware neural operators and mesh graph surrogates. | Recommended deployment gate for v0.5 because it stresses taxonomy, validation axes, reviewer traps, and reproducibility. |
| `cfd-ai-closure-review-benchmark.md` | Draft a turbulence-closure review seed that distinguishes a priori fit from a posteriori coupled-solver evidence. | Hard closure-modeling gate for RANS/LES traps, invariance, UQ, verifiability, and solver-coupling claims. |
| `cfd-ai-benchmark-landscape-review.md` | Draft a benchmark-landscape review seed that classifies datasets/tools by validation axis, split design, failure mode, and reproducibility. | Hard benchmark-design gate for preventing resource-list prose and unsupported dataset/tool claims. |
| `gold-paper-reconstruction-template.md` | Template for reconstructing gold-paper patterns without inventing PDF-only facts. | Template task. |
| `fukami-super-resolution-reconstruction.md` | Gold-paper reconstruction benchmark. | v0.4 sanity run present. |
| `lee-cylinder-wake-reviewer-attack.md` | Reviewer-defense benchmark for wake-analysis claims. | v0.4 sanity run present. |
| `brunton-taxonomy-reconstruction.md` | Related-work taxonomy benchmark. | v0.4 sanity run present. |
| `maulik-experiment-matrix.md` | Experiment-matrix benchmark. | Available task; no listed v0.5 A/B run yet. |
| `vinuesa-related-work-positioning.md` | Related-work positioning benchmark. | Available task; no listed v0.5 A/B run yet. |

## Pass Criteria

Pass-level outputs must:

- preserve source-scope honesty and mark unknown facts as `TODO`;
- avoid invented solver settings, DOI values, corresponding-author claims, datasets, code repositories, or exact numbers;
- map claims to supplied evidence or limitations;
- include benchmark-required tables, figures, reviewer-risk/trap handling, and bibliography TODOs;
- use field-native CFD/SciML vocabulary without unsupported hype terms;
- compile or provide a clear compile-failure artifact when LaTeX output is requested.

For v0.5 deployment checks, run the trend-review benchmark first, then use `scripts/evaluate_latex_output.py` as a deterministic surface scan before manual rubric scoring. For harder v0.6-style checks, add the closure-review and benchmark-landscape-review tasks.
