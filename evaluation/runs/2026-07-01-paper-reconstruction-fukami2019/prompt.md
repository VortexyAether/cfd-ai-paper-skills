# Paper reconstruction from summary benchmark

Task: Using only `source_summary_dense.md`, reconstruct a reviewer-defensible LaTeX manuscript seed of Fukami et al. 2019, *Super-resolution reconstruction of turbulent flows with machine learning*.

A/B setup:

- `no_skill/`: generic manuscript reconstruction from the summary.
- `with_skill/`: reconstruction using root `SKILL.md`, claim-evidence discipline, figure/result storytelling, CFD reproducibility checks, and LaTeX production rules.

Hard rule: missing scientific facts must stay `TODO`; do not invent exact numbers, solver settings, architecture details, citation metadata, or figure panels.