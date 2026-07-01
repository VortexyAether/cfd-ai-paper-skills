---
title: Gold-standard bibliography v0.2
created: 2026-06-30
updated: 2026-06-30
source: delegated bibliography review
status: archived-v0.2-input-superseded-by-v0.3
aliases:
  - CFD-AI 정답지 논문 목록
tags:
  - cfd-ai
  - sciml
  - gold-standard
  - bibliography
---

# Gold-standard bibliography v0.2

> v0.4 note: this bibliography remains useful as a broad source list. The current evaluator-facing bibliography is `references/gold-standard-bibliography-v0.4.md`, and the current answer-key files are indexed in `references/gold-papers/INDEX.md`.

Gold-standard answer-key authors: **Kai Fukami, Steven L. Brunton, Romit Maulik, Sangseung Lee, Ricardo Vinuesa**의 first-author 또는 senior/corresponding-author급 논문들.

원칙: 이 목록은 citation 장식이 아니라 **skill evaluation answer key**다. 각 논문에서 abstract/introduction/method/experiment/figure/reviewer-defense 패턴을 뽑아야 한다.

> [!warning]
> Corresponding author 여부는 웹 추출에서 명시 확인된 경우만 verified. 나머지는 uncertain으로 둔다. 추후 PDF title page/footnote로 확인 필요.

---

## Kai Fukami

### 1. Super-resolution reconstruction of turbulent flows with machine learning

- Authors: Fukami, Fukagata & Taira
- Year/Venue: 2019, *Journal of Fluid Mechanics*, 870, 106–120
- DOI: https://doi.org/10.1017/jfm.2019.238
- Role: Fukami first author; corresponding uncertain
- Why exemplar: image super-resolution idea를 turbulent-flow reconstruction으로 번역한 JFM-style 고전.
- Skill extraction target:
  - low-resolution measurement/CFD bottleneck → CNN/SRCNN analogy
  - turbulence-specific validation, not generic image ML
  - vorticity/field comparison + spectra/quantitative error

### 2. Machine-learning-based spatio-temporal super resolution reconstruction of turbulent flows

- Authors: Fukami, Fukagata & Taira
- Year/Venue: 2021, *Journal of Fluid Mechanics*, 909, A9
- DOI: https://doi.org/10.1017/jfm.2020.948
- Role: Fukami first; corresponding uncertain
- Why exemplar: spatial SR에서 temporal interpolation까지 확장하는 incremental novelty 구조.
- Pattern:
  - task → gap → method → cases → accuracy
  - coarse/input–truth–prediction–error 반복 figure grammar

### 3. Assessment of supervised machine learning methods for fluid flows

- Authors: Fukami, Fukagata & Taira
- Year/Venue: 2020, *Theoretical and Computational Fluid Dynamics*
- arXiv: https://arxiv.org/abs/2001.09618
- Role: Fukami first; corresponding uncertain
- Why exemplar: reviewer가 좋아하는 method comparison + limitations 논문.
- Pattern:
  - architectures를 같은 benchmark에서 비교
  - interpretability/generalizability/physical consistency를 evaluation axis로 명시

### 4. Super-resolution analysis via machine learning: A survey for fluid flows

- Authors: Fukami, Fukagata & Taira
- Year/Venue: 2023, *Theoretical and Computational Fluid Dynamics*, 37, 421–444
- DOI/arXiv: https://doi.org/10.1007/s00162-023-00663-0 / https://arxiv.org/abs/2301.10937
- Role: Fukami first; invited; corresponding uncertain
- Why exemplar: review/perspective 구조 정답지.
- Pattern:
  - definition → taxonomy → representative datasets → open issues
  - computer vision analogy와 fluid-specific constraints 연결

### 5. Grasping extreme aerodynamics on a low-dimensional manifold

- Authors: Fukami & Taira
- Year/Venue: 2023, *Nature Communications*, 14, 6480
- DOI/arXiv: https://doi.org/10.1038/s41467-023-42213-6 / https://arxiv.org/abs/2305.08024
- Role: Fukami first; Taira senior; corresponding uncertain
- Why exemplar: high-impact style: broad motivation + interpretable latent manifold + extreme aerodynamics.

### 6. Data-driven nonlinear turbulent flow scaling with Buckingham Pi variables

- Authors: Fukami, Goto & Taira
- Year/Venue: 2024, *Journal of Fluid Mechanics*, 984, R4
- DOI/arXiv: https://doi.org/10.1017/jfm.2024.211 / https://arxiv.org/abs/2402.17990
- Role: Fukami first; corresponding uncertain
- Why exemplar: ML output을 dimensional analysis/Buckingham Pi로 물리 해석하는 reviewer-friendly model.

### 7. Single-snapshot machine learning for super-resolution of turbulence

- Authors: Fukami & Taira
- Year/Venue: 2024, *Journal of Fluid Mechanics*, 1001, A32
- DOI/arXiv: https://doi.org/10.1017/jfm.2024.1136 / https://arxiv.org/abs/2409.04923
- Role: Fukami first; corresponding uncertain
- Why exemplar: minimal-data regime을 명확한 claim으로 잡은 concise JFM paper.

### 8. Observable-augmented manifold learning for multi-source turbulent flow data

- Authors: Fukami & Taira
- Year/Venue: 2025, *Journal of Fluid Mechanics*, 1010, R4
- DOI: https://doi.org/10.1017/jfm.2025.383
- Role: Fukami first; corresponding uncertain
- Why exemplar: multi-source data fusion + latent variables + physically meaningful observables.

---

## Steven L. Brunton

### 1. Machine Learning for Fluid Mechanics

- Authors: Brunton, Noack & Koumoutsakos
- Year/Venue: 2020, *Annual Review of Fluid Mechanics*, 52, 477–508
- DOI/arXiv: https://doi.org/10.1146/annurev-fluid-010719-060214 / https://arxiv.org/abs/1905.11075
- Role: Brunton first; corresponding uncertain
- Why exemplar: field-defining review; taxonomy/introduction answer key.
- Pattern:
  - historical arc → supervised/unsupervised/RL taxonomy
  - sensing/modeling/control/optimization applications
  - opportunities + caveats

### 2. Applying machine learning to study fluid mechanics

- Author: Brunton
- Year/Venue: 2021, *Acta Mechanica Sinica*, 37, 1718–1726
- DOI/arXiv: https://doi.org/10.1007/s10409-021-01143-6 / https://arxiv.org/abs/2110.02083
- Role: sole/first; corresponding-author status unknown/TODO pending source-backed verification
- Why exemplar: short tutorial/perspective with clean workflow.
- Pattern: problem formulation → data curation → architecture → loss → optimization/validation.

### 3. Discovering governing equations from data by sparse identification of nonlinear dynamical systems

- Authors: Brunton, Proctor & Kutz
- Year/Venue: 2016, *PNAS*, 113, 3932–3937
- DOI: https://doi.org/10.1073/pnas.1517384113
- Role: Brunton first; corresponding uncertain
- Why exemplar: SINDy; interpretable scientific ML archetype.
- Pattern: black-box vs interpretable laws; recovered equations + prediction trajectories.

### 4. Enhancing computational fluid dynamics with machine learning

- Authors: Vinuesa & Brunton
- Year/Venue: 2022, *Nature Computational Science*, 2, 358–366
- DOI: https://doi.org/10.1038/s43588-022-00264-7
- Role: Vinuesa first; Brunton coauthor/senior-like; corresponding uncertain
- Why exemplar: opportunity/challenge perspective for CFD-AI.

### 5. An empirical mean-field model of symmetry-breaking in a turbulent wake

- Authors: Callaham, Rigas, Loiseau & Brunton
- Year/Venue: 2022, *Science Advances*, 8, eabm4786
- DOI: https://doi.org/10.1126/sciadv.abm4786
- Role: Brunton senior/last; corresponding uncertain
- Why exemplar: data-driven model used to reveal fluid physics, not just prediction.

### 6. On the role of nonlinear correlations in reduced-order modelling

- Authors: Callaham, Brunton & Loiseau
- Year/Venue: 2022, *Journal of Fluid Mechanics*, 938, A1
- DOI: https://doi.org/10.1017/jfm.2021.994
- Role: Brunton middle; include as Brunton-group exemplar
- Why exemplar: careful ROM critique and nuance.

### 7. Promoting global stability in data-driven models of quadratic nonlinear dynamics

- Authors: Kaptanoglu et al.
- Year/Venue: 2021, *Physical Review Fluids*, 6, 094401
- DOI: https://doi.org/10.1103/PhysRevFluids.6.094401
- Role: Brunton senior/last; corresponding uncertain
- Why exemplar: directly addresses learned-model long-time stability.

### 8. PySINDy: A comprehensive Python package for robust sparse system identification

- Authors: Kaptanoglu et al.
- Year/Venue: 2022, *Journal of Open Source Software*, 7, 3994
- DOI: https://doi.org/10.21105/joss.03994
- Role: Brunton senior/last; corresponding uncertain
- Why exemplar: software/reproducibility paper.

---

## Romit Maulik

### 1. Probabilistic neural networks for fluid flow surrogate modeling and data recovery

- Authors: Maulik, Fukami, Ramachandra, Fukagata & Taira
- Year/Venue: 2020, *Physical Review Fluids*, 5, 104401
- DOI/arXiv: https://doi.org/10.1103/PhysRevFluids.5.104401 / https://arxiv.org/abs/2005.04271
- Role: Maulik first; corresponding uncertain
- Why exemplar: uncertainty quantification in CFD-AI across canonical cases.
- Pattern: prediction/error/uncertainty maps.

### 2. Reduced-order modeling of advection-dominated systems with recurrent neural networks and convolutional autoencoders

- Authors: Maulik, Lusch & Balaprakash
- Year/Venue: 2021, *Physics of Fluids*, 33, 037106
- DOI: https://doi.org/10.1063/5.0039986
- Role: Maulik first; corresponding uncertain
- Why exemplar: neural latent dynamics + ROM; addresses POD failure for advection.

### 3. Efficient high-dimensional variational data assimilation with machine-learned reduced-order models

- Authors: Maulik et al.
- Year/Venue: 2022, *Geoscientific Model Development*, 15, 3433–3445
- DOI: https://doi.org/10.5194/gmd-15-3433-2022
- Role: Maulik first; corresponding uncertain
- Why exemplar: ML-ROM inside established scientific workflow.

### 4. Quantifying uncertainty for deep learning based forecasting and flow-reconstruction using neural architecture search ensembles

- Authors: Maulik, Egele, Raghavan & Balaprakash
- Year/Venue: 2023, *Physica D*, 454, 133852
- DOI: not verified in delegated extraction
- Role: Maulik first; corresponding uncertain
- Why exemplar: UQ + NAS ensembles for forecasting/reconstruction.

### 5. PythonFOAM: In-situ data analyses with OpenFOAM and Python

- Authors: Maulik, Fytanidis, Lusch, Patel & Vishwanath
- Year/Venue: 2022, *Journal of Computational Science*, 62, 101750
- DOI: not verified in delegated extraction
- Role: Maulik first; corresponding uncertain
- Why exemplar: infrastructure/reproducibility paper for CFD-AI workflows.

### 6. Multi-fidelity reinforcement learning framework for shape optimization

- Authors: Bhola, Pawar, Balaprakash & Maulik
- Year/Venue: 2023, *Journal of Computational Physics*, 482, 112018
- DOI: not verified in delegated extraction
- Role: Maulik senior/last; corresponding uncertain
- Why exemplar: multi-fidelity DRL/design optimization with cost–accuracy tradeoff.

### 7. Multiscale graph neural network autoencoders for interpretable scientific machine learning

- Authors: Barwey, Shankar, Vishwanathan & Maulik
- Year/Venue: 2023, *Journal of Computational Physics*, 495, 112537
- DOI: https://doi.org/10.1016/j.jcp.2023.112537
- Role: Maulik senior/last; corresponding uncertain
- Why exemplar: mesh/unstructured-compatible SciML + interpretability.

### 8. Scientific machine learning for closure models in multiscale problems: a review

- Authors: Sanderse, Stinis, Maulik & Ahmed
- Year/Venue: 2024, *Foundations of Data Science*
- DOI/arXiv: https://doi.org/10.3934/fods.2024043 / https://arxiv.org/abs/2403.02913
- Role: Maulik coauthor, not first/last; include due to direct relevance
- Why exemplar: closure taxonomy and a priori/a posteriori evaluation language.

---

## Sangseung Lee

### 1. Data-driven prediction of unsteady flow over a circular cylinder using deep learning

- Authors: Lee & You
- Year/Venue: 2019, *Journal of Fluid Mechanics*, 879, 217–254
- DOI/arXiv: https://doi.org/10.1017/jfm.2019.700 / https://arxiv.org/abs/1804.06076
- Role: Lee first; corresponding uncertain
- Why exemplar: early JFM deep-learning flow prediction paper; canonical cylinder-wake task.
- Pattern: physics-informed vs non-physics-informed losses; Re generalization; fields + lift/drag/time histories.

### 2. Analysis of a convolutional neural network for predicting unsteady volume wake flow fields

- Authors: Lee & You
- Year/Venue: 2021, *Physics of Fluids*, 33, 035152
- arXiv: https://arxiv.org/abs/1909.06042
- Role: Lee first; corresponding uncertain
- Why exemplar: mechanism/interpretability; addresses black-box criticism.

### 3. Predicting drag on rough surfaces by transfer learning of empirical correlations

- Authors: Lee, Yang, Forooghi, Stroh & Bagheri
- Year/Venue: 2022, *Journal of Fluid Mechanics*, 933, A18
- DOI/arXiv: https://doi.org/10.1017/jfm.2021.1041 / https://arxiv.org/abs/2106.05995
- Role: Lee first; corresponding uncertain
- Why exemplar: transfer learning + empirical correlations as physical prior.

### 4. Prediction of a typhoon track using a generative adversarial network and satellite images

- Authors: Rüttgers, Lee, Jeon & You
- Year/Venue: 2019, *Scientific Reports*, 9, 6057
- arXiv: https://arxiv.org/abs/1808.05382
- Role: Lee coauthor; include as broader geophysical AI exemplar

### 5. Prediction of a typhoon track and intensity using a generative adversarial network with observational and meteorological data

- Authors: Rüttgers, Jeon, Lee & You
- Year/Venue: 2022, *IEEE Access*, 10, 48434–48446
- DOI: https://doi.org/10.1109/ACCESS.2022.3172301
- Role: Lee coauthor; include as multimodal extension example

### 6. Strategies and applications for predicting flow using neural networks: a review

- Authors: Kang, Shin & Lee
- Year/Venue: 2024, *JMST Advances*, 6, 55–60
- DOI: https://doi.org/10.1007/s42791-024-00066-0
- Role: Lee senior/last; corresponding-author status unknown/TODO pending source-backed verification
- Why exemplar: concise pedagogical review; spatiotemporal prediction, small-data learning, aero/hydrodynamic applications.

### 7. Data-driven discovery of drag-inducing elements on a rough surface through convolutional neural networks

- Authors: Shin, Khorasani, Shi, Yang, Bagheri & Lee
- Year/Venue: 2024, *Physics of Fluids*, 36, 095172
- arXiv: https://arxiv.org/abs/2405.09071
- Role: Lee senior/last; corresponding uncertain
- Why exemplar: explainability + rough-wall turbulence; discovery framing.

### 8. Drag prediction of rough-wall turbulent flow using data-driven regression

- Authors: Shi, Khorasani, Shin, Yang, Lee & Bagheri
- Year/Venue: 2025, *Flow*, 5, E5
- arXiv: https://arxiv.org/abs/2405.09256
- Role: Lee coauthor; include as regression/feature-importance complement

---

## Ricardo Vinuesa

### 1. Enhancing computational fluid dynamics with machine learning

- Authors: Vinuesa & Brunton
- Year/Venue: 2022, *Nature Computational Science*, 2, 358–366
- DOI: https://doi.org/10.1038/s43588-022-00264-7
- Role: Vinuesa first; corresponding uncertain
- Why exemplar: CFD-AI perspective writing answer key.

### 2. Emerging trends in machine learning for computational fluid dynamics

- Authors: Vinuesa & Brunton
- Year/Venue: 2022, *Computing in Science & Engineering*, 24, 33–41
- DOI: not verified in delegated extraction
- Role: Vinuesa first; corresponding uncertain
- Why exemplar: trend/future-work language.

### 3. Flow control in wings and discovery of novel approaches via deep reinforcement learning

- Authors: Vinuesa, Lehmkuhl, Lozano-Durán & Rabault
- Year/Venue: 2022, *Fluids*, 7, 62
- DOI: unknown/TODO pending source-backed verification
- Role: Vinuesa first; corresponding uncertain
- Why exemplar: DRL for flow control as discovery, not just optimization.

### 4. Deep reinforcement learning for turbulent drag reduction in channel flows

- Authors: Guastoni, Rabault, Schlatter, Azizpour & Vinuesa
- Year/Venue: 2023, *European Physical Journal E*, 46, 27
- DOI: https://doi.org/10.1140/epje/s10189-023-00285-8
- Role: Vinuesa senior/last; corresponding uncertain
- Why exemplar: DRL environment/benchmark for wall-bounded turbulence control.

### 5. Recent advances in applying deep reinforcement learning for flow control: perspectives and future directions

- Authors: Vignon, Rabault & Vinuesa
- Year/Venue: 2023, *Physics of Fluids*, 35, 031301
- DOI: not verified in delegated extraction
- Role: Vinuesa senior/last; corresponding uncertain
- Why exemplar: focused DRL flow-control mini-review.

### 6. The transformative potential of machine learning for experiments in fluid mechanics

- Authors: Vinuesa, Brunton & McKeon
- Year/Venue: 2023, *Nature Reviews Physics*, 5, 536–545
- DOI/arXiv: https://doi.org/10.1038/s42254-023-00622-y / https://arxiv.org/abs/2303.15832
- Role: Vinuesa first; corresponding uncertain
- Why exemplar: top-tier review/perspective for experimental fluid mechanics ML.

### 7. β-Variational autoencoders and transformers for reduced-order modelling of fluid flows

- Authors: Solera-Rico et al. & Vinuesa
- Year/Venue: 2024, *Nature Communications*, 15, 1361
- DOI: not verified in delegated extraction
- Role: Vinuesa senior/last; corresponding uncertain
- Why exemplar: modern latent ROM + transformer high-impact format.

### 8. Physics-informed deep-learning applications to experimental fluid mechanics

- Authors: Eivazi, Wang & Vinuesa
- Year/Venue: 2024, *Measurement Science and Technology*, 35, 075303
- DOI/arXiv: https://doi.org/10.1088/1361-6501/ad3fd3 / https://arxiv.org/abs/2203.15402
- Role: Vinuesa senior/last; corresponding uncertain
- Why exemplar: PINNs for experimental data augmentation/super-resolution.

---

# Cross-author answer-key patterns

## Abstract grammar

- One-sentence bottleneck: expensive CFD, sparse/noisy experiments, low resolution, stability, uncertainty, data scarcity.
- One-sentence method: CNN/GAN/VAE/transformer/GNN/SINDy/PINN/DRL with physical constraints or priors.
- One-sentence evidence: canonical flow cases, turbulence, cylinder wakes, airfoils, channel flows, rough walls, geophysical flows.
- One-sentence contribution: accuracy plus interpretability/generalization/uncertainty/stability/computational savings.

## Introduction grammar

- Starts from fluid-mechanics pain point, not “AI is popular.”
- Explains why CFD/ROM/POD/RANS/LES/experiments are insufficient.
- Positions ML as augmentation of physics, not replacement.
- Names reviewer-facing risks: generalization, interpretability, uncertainty, stability, scarce data, physical consistency.

## Method grammar

Strong papers define:

- input/output tensors or observables,
- architecture,
- loss terms,
- physics constraints,
- training/test split,
- baselines,
- nondimensional parameters / Reynolds numbers / flow configuration.

Best exemplars add physical inductive bias:

- conservation loss,
- Buckingham Pi variables,
- empirical correlations,
- PINN residuals,
- stability constraints,
- uncertainty distributions.

## Experiment grammar

Strong papers test:

- interpolation and extrapolation,
- sparse/noisy/low-resolution inputs,
- long-time rollout,
- cross-Reynolds-number or cross-geometry transfer,
- uncertainty or stability.

Typical baselines:

- POD,
- linear regression,
- empirical correlations,
- classical ROM,
- vanilla CNN/GAN/FNO/PINN.

## Figure grammar

1. conceptual schematic / pipeline,
2. dataset or flow configuration,
3. architecture/loss diagram,
4. prediction vs truth vs error fields,
5. spectra / forces / drag / lift / time histories,
6. latent space / manifold / feature attribution / uncertainty map,
7. ablation/generalization plot.

## Reviewer-defense grammar

- Claims are bounded: “for these flows/regimes/data conditions.”
- Physical interpretation follows numerical accuracy.
- Limitations are explicit: data dependence, Re extrapolation, sensor noise, stability, cost.
- ML outputs are translated into fluid-mechanics language: vorticity, spectra, skin friction, drag, pressure, coherent structures, conservation residuals.
