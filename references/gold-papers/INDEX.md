---
title: Gold-paper index v0.4
created: 2026-06-30
updated: 2026-06-30
status: v0.4
---

# Gold-Paper Index v0.4

## Kai Fukami

| Paper | Type | Main skill lessons | Future PDF priority |
|---|---|---|---|
| `fukami-2019-super-resolution-jfm.md` | method / super-resolution | GT/coarse/pred/error; interpolation baselines; turbulence diagnostics. | high: verify exact figure sequence and solver/code details. |
| `fukami-2021-spatiotemporal-super-resolution-jfm.md` | method / super-resolution | Separate spatial and temporal sparsity; include frame-interval robustness. | high: extract downsampling and temporal-correlation details. |
| `fukami-2023-super-resolution-survey-tcfd.md` | review / super-resolution | Survey taxonomy plus case-study evidence; fluid-specific SR constraints. | medium: extract taxonomy and open-challenge list. |

## Steven L. Brunton

| Paper | Type | Main skill lessons | Future PDF priority |
|---|---|---|---|
| `brunton-2016-sindy-pnas.md` | method / discovery | Parsimony, candidate-library transparency, canonical validation before fluid example. | high: extract algorithm details and fluid example figures. |
| `brunton-2020-machine-learning-fluid-mechanics.md` | review / taxonomy | Taxonomy over chronology; ML role in workflow; limitations with opportunity. | high: extract section taxonomy and figures. |
| `brunton-2021-applying-ml-fluid-mechanics.md` | review / tutorial | Five-stage ML workflow; locate physics in problem/data/architecture/loss/optimization. | medium: extract examples and diagrams. |

## Romit Maulik

| Paper | Type | Main skill lessons | Future PDF priority |
|---|---|---|---|
| `maulik-2020-probabilistic-neural-networks-prf.md` | method / UQ / surrogate | Trust claims need uncertainty intervals, noisy/sparse tests, and calibration-style evidence. | high: extract exact UQ diagnostics and baselines. |
| `maulik-2021-rom-advection-poF.md` | method / ROM | Compare against POD-Galerkin; separate compression from stable latent dynamics. | high: extract metrics and architecture/training details. |
| `maulik-2023-multiscale-gnn-autoencoders-jcp.md` | method / ROM / interpretability | Mesh-aware GNNs need latent artifacts tied to physical space. | high: extract mesh, LES, and baseline details. |

## Sangseung Lee

| Paper | Type | Main skill lessons | Future PDF priority |
|---|---|---|---|
| `lee-2019-cylinder-wake-jfm.md` | method / prediction | Re splits, conservation losses, rollout and solver details are reviewer-critical. | high: extract solver/mesh/CFL and exact figures. |
| `lee-2021-cnn-wake-analysis-pof.md` | method / interpretability | CNN interpretation requires feature maps, spectra, time-history and variable contribution analysis. | high: extract regimes and figure sequence. |
| `lee-2022-rough-surface-transfer-learning-jfm.md` | method / transfer learning | Empirical correlations can be transferable approximate physics; data-amount sweeps matter. | medium: extract roughness statistics and DNS setup. |

## Ricardo Vinuesa

| Paper | Type | Main skill lessons | Future PDF priority |
|---|---|---|---|
| `vinuesa-2022-enhancing-cfd-ml.md` | review / CFD opportunity | Map ML to CFD bottlenecks and limitations. | high: extract exact four-figure grammar. |
| `vinuesa-2023-transformative-ml-experiments-nrp.md` | review / experiment | Experiments need their own ML taxonomy: measurement, design, digital twins, estimation/control. | medium: extract full taxonomy and examples. |
| `vinuesa-2023-drl-drag-reduction-epje.md` | control / DRL | Control papers need action/reward/observation, closed-loop baselines, and simulator reproducibility. | high: extract environment and reward details. |

## Cross-Paper Lessons

| Skill area | Gold-paper pattern |
|---|---|
| Writing | Start from a physics bottleneck, define ML role, calibrate contribution, and state limitations early. |
| Reviewing | Attack generalization, solver/mesh/BC details, baselines, physical diagnostics, and unsupported interpretability. |
| Reproducibility | Require equations/regimes, data-generation setup, train/test split, hyperparameters, compute, and code/data status. |
| Figures | Prefer task schematic, GT/baseline/pred/error, physical diagnostics, ablations, OOD/failure, and efficiency. |
| Related work | Build taxonomies by workflow role: reconstruction, discovery, ROM, UQ, experiments, control, closure, acceleration. |

