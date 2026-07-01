---
title: Gold-standard paper map
created: 2026-06-30
updated: 2026-06-30
source: TARS + arXiv/API/web search
status: draft-needs-deeper-reading
tags:
  - cfd-ai
  - sciml
  - gold-standard
---

# Gold-standard paper map

This file is the initial answer-key map for the CFD-AI Paper Skills Package.

Rule: do not use these papers as mere citation decoration. Use them as writing-pattern exemplars.

## What to extract from every gold paper

For each paper, extract:

1. Problem statement: what physics/engineering bottleneck is named?
2. Gap: why existing CFD/ML methods are insufficient.
3. Contribution claim: exact novelty, not hype.
4. Evidence stack: datasets, baselines, diagnostics, ablations, generalization tests.
5. Physics contract: governing equations, regimes, BC/IC, nondimensional groups, solver details.
6. Figure logic: what each figure proves.
7. Reviewer defense: what likely objections are pre-answered.
8. Limitations: what is admitted or bounded.

## Kai Fukami — exemplar patterns

Initial arXiv/API hits:

- 2018/2019 — *Super-resolution reconstruction of turbulent flows with machine learning* — arXiv:1811.11328. Pattern: image-super-resolution idea translated into turbulent-flow reconstruction, with clear low-res → high-res task and visual/quantitative validation.
- 2020 — *Assessment of supervised machine learning methods for fluid flows* — arXiv:2001.09618. Pattern: method comparison paper; useful for baseline/metric framing.
- 2020 — *Generalization techniques of neural networks for fluid flow estimation* — arXiv:2011.11911. Pattern: attacks the reviewer question “does it generalize?” directly.
- 2023 — *Super-Resolution Analysis via Machine Learning for Vortical and Turbulent Flows* — arXiv:2301.10937. Pattern: survey + case studies; good related-work taxonomy model.
- 2024 — *Single-snapshot machine learning for super-resolution of turbulence* — arXiv:2409.04923. Pattern: hard task definition; tests what can be inferred from minimal input.
- 2025 — *Compressing fluid flows with nonlinear machine learning: mode decomposition, latent modeling, and flow control* — arXiv:2505.00343. Pattern: compression/latent modeling/control bridge.

Writing lessons:

- Use concrete task transformations: sparse → dense, low-res → high-res, compressed → reconstructed.
- Pair qualitative vortex/field plots with quantitative error.
- Explicitly address generalization, not as an afterthought.
- Fluid-mechanics language stays central; ML is the tool, not the protagonist.

## Steven L. Brunton — exemplar patterns

Initial arXiv/API and web hits:

- 2020 — *Machine Learning for Fluid Mechanics*, Annual Review of Fluid Mechanics. Pattern: field-defining taxonomy; extremely strong introduction/related-work model.
- 2021 — *Enhancing Computational Fluid Dynamics with Machine Learning* — arXiv:2110.02085 / Nature Machine Intelligence. Pattern: agenda-setting CFD+ML review; good for opportunity taxonomy and limitations.
- 2021 — *Applying Machine Learning to Study Fluid Mechanics* — arXiv:2110.02083. Pattern: pedagogical bridge; suitable for skill examples.
- 2023 — *The transformative potential of machine learning for experiments in fluid mechanics* — arXiv:2303.15832, with Vinuesa/McKeon. Pattern: connects ML to experimental bottlenecks.
- SINDy line of work, e.g. sparse identification of nonlinear dynamics. Pattern: interpretable discovery, concise governing-equation framing, model parsimony.

Writing lessons:

- Start from a clean taxonomy of where ML touches the scientific workflow.
- Define “what the method buys”: acceleration, closure, control, discovery, sensing, uncertainty.
- Strong papers teach reviewers the map before selling a method.
- Prefer interpretable structure and scientific insight over black-box performance claims.

## Romit Maulik — exemplar patterns

Initial arXiv/API hits:

- 2020 — *Probabilistic neural networks for fluid flow surrogate modeling and data recovery* — arXiv:2005.04271.
- 2020 — *Probabilistic neural network-based reduced-order surrogate for fluid flows* — arXiv:2012.08719.
- 2021 — *Machine-learning accelerated turbulence modelling of transient flashing jets* — arXiv:2109.15203.
- 2023 — *Generalizable data-driven turbulence closure modeling on unstructured grids with differentiable physics* — arXiv:2307.13533.
- 2024 — *Leveraging Interpolation Models and Error Bounds for Verifiable Scientific Machine Learning* — arXiv:2404.03586.

Writing lessons:

- Strong emphasis on uncertainty, verifiability, differentiable physics, and closure modeling.
- Good target for skills dealing with reduced-order models, surrogate reliability, and turbulence closure.
- Reviewer defense should include uncertainty/error bounds when claims are made about trustworthy prediction.

## Sangseung Lee — exemplar patterns

Initial arXiv/API/web hits:

- 2018/2019 — *Data-driven prediction of unsteady flow fields over a circular cylinder using deep learning* — arXiv:1804.06076 / JFM 879:217–254 (web search). Pattern: canonical CFD deep-learning prediction paper; clear benchmark geometry and unsteady wake task.
- 2018 — *Deep learning approach in multi-scale prediction of turbulent mixing-layer* — arXiv:1809.07021.
- 2019 — *Mechanisms of a Convolutional Neural Network for Learning Three-dimensional Unsteady Wake Flow* — arXiv:1909.06042. Pattern: not just performance; mechanism/interpretability of CNN learning.
- 2024 — *Data-driven discovery of drag-inducing elements on a rough surface through convolutional neural networks* — arXiv:2405.09071.
- 2024 — *Drag prediction of rough-wall turbulent flow using data-driven regression* — arXiv:2405.09256.
- 2026 — *UrbanFlow-3K: A Dataset of 3,000 Lattice-Boltzmann Simulations of Random Building Layouts* — arXiv:2603.16554.

Writing lessons:

- Strong benchmark-style flow setup: cylinder wake, mixing layer, rough-wall drag.
- Good examples for linking ML output to physical mechanism, not only error reduction.
- Useful for dataset/task design and applied CFD-AI narrative.

## Ricardo Vinuesa — exemplar patterns

Initial arXiv/API hits:

- 2021 — *Enhancing Computational Fluid Dynamics with Machine Learning* — arXiv:2110.02085.
- 2022/2023 — *Emerging trends in machine learning for computational fluid dynamics* — arXiv:2211.15145.
- 2020 — *On the use of recurrent neural networks for predictions of turbulent flows* — arXiv:2002.01222.
- 2023 — *The transformative potential of machine learning for experiments in fluid mechanics* — arXiv:2303.15832.
- 2024 — *Active and inactive contributions to the wall pressure and wall-shear stress in turbulent boundary layers* — arXiv:2406.15733.

Writing lessons:

- Strong for field-level positioning and responsible ML-for-CFD framing.
- Repeatedly links method opportunity to real CFD/experimental bottlenecks.
- Good standard for “what would the community actually care about?”

## Cross-author answer-key patterns

A CFD-AI/SciML paper should usually pass these:

1. Physics-first problem setup.
2. ML role is specific: closure, surrogate, super-resolution, sensing, control, discovery, compression, or uncertainty.
3. Reproducible numerical setup.
4. Baseline matrix is fair and not ornamental.
5. Metrics include physical diagnostics, not only ML losses.
6. Generalization is explicitly tested or honestly bounded.
7. Figures prove claims: ground truth, prediction, error, spectra/diagnostics, ablation, failure.
8. Related work is a taxonomy, not a citation landfill.
9. Claims are calibrated to evidence.
10. Limitations are present before the reviewer weaponizes them.

## Next deeper-reading tasks

- Verify corresponding-author status from PDF footnotes where needed.
- Extract abstract/introduction templates from 2–3 papers per author.
- Build a table of common experiment matrices.
- Build a figure archetype library.
- Create gold-answer tasks for the dumb-agent protocol.
