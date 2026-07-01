# Task: Minimal reviewer-audit flawed abstract

## Skill under test

- `reviewer-audit-toolkit`
- `paper-claim-auditor`
- `cfd-ml-paper-reviewer`
- `sciml-experiment-auditor`
- `cfd-reproducibility-checker`

## Prompt

Given only the abstract below, produce a decision-oriented reviewer audit. Do not invent solver, data, metric, or citation details.

> We propose a robust physics-informed AI framework for predicting turbulent wake flows. The model achieves state-of-the-art accuracy and generalizes to unseen Reynolds numbers, geometries, and boundary conditions. Velocity contour plots show excellent agreement with CFD, and the method is fast enough for real-time engineering design. These results demonstrate that the model can replace expensive CFD simulations for practical flow-control optimization.

Required output:

1. gate summary;
2. Fatal/Major reviewer risks;
3. claim-evidence map;
4. missing evidence surfaces;
5. minimum rescue experiments/tables/figures;
6. safer rewritten abstract.

## Expected answer-key patterns

- Verdict should be reject-risk unless evidence is added.
- Must reject or bound: robust, physics-informed, state-of-the-art, generalizes, real-time, replaces CFD.
- Must demand physical/numerical setup: geometry, BC/IC, Re range, solver/fidelity, mesh/grid, timestep/CFL.
- Must demand split axes: held-out Re, geometry, BC, mesh, long-time rollout or OOD/noise if claimed.
- Must demand named same-scope baselines and metrics.
- Must demand physical diagnostics beyond velocity contours: residual/divergence, forces, Strouhal/frequency, spectra or other flow-appropriate QoIs.
- Must demand runtime evidence: hardware, latency, memory, batch size, end-to-end solver-coupled workflow, fallback policy.
- Must produce concrete rescue artifacts, not generic advice.
