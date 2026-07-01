---
title: Field terminology and style guide
created: 2026-06-30
updated: 2026-06-30
status: v1.0-candidate
source: internal style and terminology review
tags:
  - cfd-ai
  - sciml
  - writing-style
  - terminology
---

# Field terminology and style guide

Purpose: prevent AI-assisted CFD-AI/SciML manuscripts from drifting into generic AI booster prose.

Core rule:

> Every evaluative adjective must either be backed by measurable CFD/SciML evidence or replaced with a scoped, field-native statement.

This guide is qualitative. It is based on local gold-paper notes and web-scouted terminology patterns from papers/reviews associated with Kai Fukami, Steven L. Brunton, Romit Maulik, Sangseung Lee, and Ricardo Vinuesa. Do not present these as corpus statistics.

---

## Why generic AI wording fails

Generic AI academic wording hides the evidence contract that CFD/fluid-mechanics reviewers expect. Phrases such as “robust AI framework,” “state-of-the-art performance,” or “physically consistent predictions” do not identify:

- flow regime
- governing quantity
- numerical/reference data
- train/test split
- baseline
- physical diagnostic
- limitation boundary

Reviewer-safe prose names these directly.

---

## Field-native vocabulary by context

### Problem framing

| Use | Avoid |
|---|---|
| low-resolution flow-field reconstruction | AI-enhanced resolution |
| spatio-temporal super-resolution from coarsely sampled snapshots | recovering hidden dynamics |
| surrogate modeling for [flow case/quantity] | AI model for CFD |
| reduced-order modeling of advection-dominated systems | compact deep model |
| turbulence closure / closure modeling | learning turbulence |
| wake prediction at unseen Reynolds numbers | general flow prediction |
| rough-wall drag prediction under limited DNS data | industrial drag AI |
| ML-augmented measurement, design, estimation, or control | transformative experiment platform |

Pattern: start from the physical or numerical bottleneck, then name the ML role.

### CFD / numerical setup

Prefer:

- circular-cylinder wake, turbulent channel flow, backward-facing step, rough-wall surface, NACA0012 airfoil, shallow-water system
- Reynolds number, friction Reynolds number, laminar/transitional/turbulent regime, 3D wake transition, shear-layer transition
- DNS, LES, RANS, high-fidelity simulation, experimental measurement, reference solution
- velocity components, vorticity, pressure, drag, lift, wall shear stress, sea-surface temperature, latent coefficients
- spatial downsampling, temporal subsampling, sparse observations, sensor layout
- grid/mesh, boundary conditions, time step, CFL, train/validation/test split, seeds, code/data availability

Avoid “simulation data” alone when solver fidelity, regime, and variables matter.

### SciML method description

| Task | Field-native wording |
|---|---|
| Super-resolution | convolutional reconstruction model, downsampled input, high-resolution target, bicubic interpolation baseline, vorticity PDF/spectrum |
| Spatio-temporal SR | inbetweening, frame-interval robustness, temporal correlation, space-time reconstruction |
| Discovery | sparse regression, candidate-function library, derivative estimation, governing-equation recovery, parsimony |
| ROM | POD-Galerkin baseline, nonlinear latent space, convolutional autoencoder, recurrent latent dynamics, rollout stability |
| UQ | predictive distribution, confidence intervals, calibration, noisy/sparse-observation stress tests |
| Graph CFD | unstructured mesh, graph neural network autoencoder, adaptive graph reduction, multiscale message passing |
| Wake prediction | CNN/GAN variants, conservation-law-informed loss, mass/momentum residuals, Reynolds-number extrapolation/interpolation |
| Control | action/observation/reward specification, wall blowing/suction, opposition-control baseline, closed-loop drag reduction |
| Transfer learning | empirical-correlation transfer, limited-DNS sweep, roughness descriptors, high-fidelity data burden |

Avoid method-first descriptions that do not identify input, output, physics role, and evidence.

### Evaluation vocabulary

Use terms that map to the experiment matrix:

- baseline matrix
- leakage-safe split
- unseen Reynolds number / geometry / boundary condition / time horizon
- train/validation/test regimes
- noise level and sparse-observation layout
- long-rollout error growth
- data-amount sweep
- ablation of physical loss, architecture, latent dimension, transfer source, or graph coarsening
- failure case / out-of-distribution boundary
- same data, same metrics, same color scale

Avoid “extensive experiments” unless the axes are named.

### Physical diagnostics

Prefer named diagnostics:

- conservation residuals
- mass and momentum residuals
- vorticity contours
- energy spectrum / wavenumber spectrum
- vorticity PDF
- drag/lift coefficients
- wall shear stress
- pressure drop
- temporal correlation
- force/time-history comparison
- feature-map/Fourier analysis tied to physical structures
- masked-field or sensor-region interpretation

Avoid “physically meaningful outputs” unless a diagnostic is named.

---

## Suspicious AI-ish phrases and replacements

| Avoid phrase | Why bad | Field-native replacement | Example sentence |
|---|---|---|---|
| novel AI framework | Does not name task, architecture, or contribution boundary. | convolutional/operator/graph model for [task] with [specific mechanism] | We evaluate a convolutional model for vorticity super-resolution with multiscale skip connections. |
| accurately predicts turbulent flows | Missing regime, horizon, variable, and metric. | predicts [variable] in [flow] over [horizon] with [metric] | The model predicts cylinder-wake velocity fields over a 20-step rollout at $Re=500$ with lower relative $L_2$ error than the baseline. |
| robust model | Robust to what is unspecified. | stable under [noise/sparsity/OOD/rollout] within [range] | Prediction error remains bounded under 5% additive sensor noise for the tested sparse layouts. |
| physically consistent | Requires physics diagnostic, not visual similarity. | reduces [mass/momentum/spectrum/drag] error | The physics-loss variant reduces mass-residual error relative to the unconstrained CNN. |
| state-of-the-art | Unsupported without fair benchmark. | outperforms [named baseline] on [same split/metric] | Against bicubic interpolation and a U-Net baseline on the same snapshots, the model reduces relative vorticity error. |
| generalizable | Needs leakage-safe holdout. | tested on unseen [Re/geometry/BC/roughness/time interval] | Generalization is evaluated on $Re=500$, absent from training. |
| interpretable | Vague unless artifact is inspectable. | interpreted via [feature maps/Fourier modes/latent graph masks/library terms] | Feature-map and Fourier analyses indicate which wavenumber bands are transported across CNN layers. |
| efficient | Needs hardware, runtime, memory, comparator. | uses [runtime/memory/parameters] relative to [baseline] on [hardware] | Inference takes 3 ms per snapshot on an A100, excluding data loading. |
| real-time | Deployment-specific and often overclaimed. | meets [control/estimation] update interval on [hardware] | The estimator runs faster than the 10 ms control interval on the stated GPU. |
| revolutionary / transformative | Promotional unless perspective-style and caveated. | may enhance [workflow] by [mechanism] | The method may enhance sparse-PIV reconstruction by reducing dependence on dense measurements. |
| seamlessly integrates physics | Does not say where physics enters. | uses physics in [problem/data/architecture/loss/optimization] | Conservation terms enter the loss through residuals of mass and momentum. |
| captures complex dynamics | Too broad. | recovers [vortical structures/spectral band/latent trajectory] | The reconstruction better recovers high-wavenumber vorticity content than interpolation. |
| significantly improves | Statistical/practical meaning unclear. | reduces [metric] by [amount] under [test] | The transfer model reduces drag-prediction error in the 20-sample DNS setting. |
| cutting-edge deep learning | Empty prestige marker. | [architecture] selected because [mesh/time/physics reason] | A graph autoencoder is used because LES snapshots are defined on an unstructured mesh. |
| demonstrates promise | Weak filler. | supports use for [scoped task] when [condition] | The results support learned reconstruction when training and test regimes share the same Reynolds-number range. |
| hallucination | NLP-specific. | unphysical prediction / spurious structure / conservation violation | The rollout produces spurious vortical structures after the training horizon. |

---

## Claim calibration rules

| Claim word | Evidence required before use | Safer wording if evidence is incomplete |
|---|---|---|
| robust | Stress test matched to claim: noise, sparse sensors, long rollout, mesh/resolution perturbation, unseen regime, or data scarcity; include failure boundary. | stable under the tested [noise/sparsity/rollout] condition |
| generalizable | Leakage-safe holdout on the claimed axis: unseen Reynolds number, geometry, boundary condition, roughness distribution, time interval, or parameter range. Random split is not enough. | evaluated on an unseen [axis] within [range] |
| physically consistent | Direct diagnostic: conservation residual, spectrum, vorticity PDF, force coefficient, wall-shear stress, pressure drop, temporal correlation, or equation/library recovery. | better preserves [specific diagnostic] under [test] |
| real-time | End-to-end latency on stated hardware meets stated control/estimation/acquisition interval; include batch size and data movement assumptions. | low-latency inference on [hardware]; real-time deployment remains TODO |
| state-of-the-art | Fair comparison to relevant baselines on same data/splits/metrics; repeated runs or variation if appropriate. | outperforms [named baseline] on [metric] for [task] |
| novel | Specific prior-art contrast and exact new component/claim boundary. | extends [prior task] by adding [component] under [condition] |
| interpretable | Inspectable artifact plus validation: sparse terms, feature/Fourier analysis, latent graph masks, sensor-region selection, or physical-region mapping. | provides [artifact] consistent with [physical diagnostic] |
| efficient | Hardware, wall-clock time, memory, parameter count, and fair baseline; distinguish training and inference. | reduces [cost metric] relative to [baseline] on [hardware] |

Hard rule: if evidence is absent, replace the adjective with the exact TODO experiment.

---

## Gold-author style patterns

### Fukami-style reconstruction language

- Define the task as low-resolution to high-resolution flow-field reconstruction.
- Keep variables central: velocity, vorticity, turbulent structures, high-wavenumber content.
- Compare against interpolation or relevant reconstruction baselines.
- Pair field plots with quantitative error and physical/statistical diagnostics.

Sentence pattern:

> We reconstruct high-resolution [velocity/vorticity] fields from [downsampled/sparse] inputs for [flow case/regime] and compare against [interpolation/baseline] using [error] and [spectrum/PDF/residual] diagnostics.

### Brunton-style taxonomy/interpretable-model language

- Start from scientific workflow and physical knowledge, not architecture fashion.
- Classify ML role: understanding, modeling, optimization, control, sensing, simulation support, or discovery.
- For discovery, emphasize sparse candidate libraries, parsimony, derivative estimation, and governing-equation recovery.

Sentence pattern:

> This contribution enters the [workflow role] stage: it uses [physical prior/data/architecture/loss] to [specific scientific objective], rather than replacing the governing model.

### Maulik-style UQ/ROM/closure language

- Distinguish point prediction from predictive distributions.
- Tie trustworthiness to confidence intervals, calibration, noisy/sparse-observation tests, and error bounds.
- For ROMs, name classical failure mode and test stable latent rollout.

Sentence pattern:

> The method is evaluated as a [surrogate/ROM/closure] under [case] with [baseline], [uncertainty/error-bound evidence], and [stress test], so the reliability claim is limited to [regime].

### Lee-style wake/roughness/mechanism language

- Make geometry/regime explicit: circular-cylinder wake, 3D wake transition, shear-layer transition, rough-wall drag.
- Treat physical consistency as conservation-law or mechanism evidence, not only lower error.
- Use feature maps, Fourier/wavenumber analysis, variable/time-history contribution, or roughness descriptors for mechanism claims.

Sentence pattern:

> For [wake/rough-wall] prediction, we test [model variant] on [regime split], compare with [baseline], and analyze [conservation residual/Fourier feature/roughness descriptor] to support the physical mechanism claim.

### Vinuesa-style opportunity/limitation language

- Position ML as enhancing CFD or experiments, not replacing them.
- Name the bottleneck: DNS cost, turbulence closure, ROM fidelity, measurement quality, experimental design, real-time estimation/control.
- Pair opportunity with caveat.

Sentence pattern:

> ML may enhance [CFD/experimental workflow] by addressing [bottleneck], but the claim is limited by [data/regime/solver/control/deployment caveat].

---

## Manuscript polishing checklist

Search for:

`novel|robust|generaliz|physical|state-of-the-art|efficient|real-time|interpretable|promise|transformative|seamless|powerful|cutting-edge|unlock|holistic|comprehensive`

For every hit, require evidence in the same sentence or adjacent sentence.

Pass conditions:

- The first problem paragraph states flow case, regime, variables, and bottleneck.
- The ML role is classified as reconstruction, surrogate, ROM, closure, control, sensing, discovery, UQ, acceleration, or experiment design.
- “AI model” is replaced with architecture and input/output mapping.
- “Physics-informed” states where physics enters: problem, data, architecture, loss, optimization, constraint, or diagnostic.
- Generalization names the holdout axis.
- Robustness names stress condition and range.
- Physical consistency names at least one physical diagnostic.
- Efficiency includes hardware, runtime/memory/parameters, and comparator.
- Limitations name untested regimes, missing diagnostics, deployment constraints, or data assumptions.

---

## Concrete rewrite examples

### Abstract

Bad:

> We propose a novel AI framework that robustly predicts turbulent flows with state-of-the-art accuracy and strong physical consistency.

Field-native rewrite:

> We evaluate a convolutional surrogate for predicting velocity and vorticity fields in the unsteady circular-cylinder wake, using Reynolds-number holdouts to test interpolation and extrapolation. The physics-loss variant is compared with an unconstrained CNN/GAN baseline using field error and conservation-residual diagnostics; claims are limited to the tested Reynolds-number range and rollout horizon.

### Related work

Bad:

> Recent advances in deep learning have revolutionized CFD, and many works have applied AI to fluid mechanics.

Field-native rewrite:

> Prior ML-for-fluids work can be grouped by workflow role: reconstruction of under-resolved fields, surrogate/ROM acceleration, turbulence closure, control, discovery of governing structure, and experimental sensing or estimation. This study belongs to [role] because it maps [input] to [output] under [flow/regime], and differs from [specific prior class] by [bounded contribution].

### Results

Bad:

> The proposed model significantly improves performance and captures the complex physics of the flow.

Field-native rewrite:

> On the unseen $Re=[value]$ test case, the model reduces relative [velocity/vorticity/drag] error compared with [baseline] and better matches the [spectrum/vorticity PDF/force time history]. The largest errors remain near [shear layer/wall region/wake transition], which bounds the physical-consistency claim.

### Limitations

Bad:

> Although promising, future work will further improve the robustness and applicability of the framework.

Field-native rewrite:

> The present evidence does not establish robustness outside the trained [Re/geometry/roughness/noise] range. Future tests should include [specific OOD axis], [noise/sparse-sensor condition], and [physical diagnostic] before claiming generalization beyond the current setup.
