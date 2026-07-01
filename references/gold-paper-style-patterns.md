---
title: Gold-paper style patterns for CFD-AI / SciML prose
created: 2026-07-01
updated: 2026-07-01
status: v1.0-candidate
source: local synthesis from gold-paper notes and benchmark failures
tags:
  - cfd-ai
  - sciml
  - manuscript-style
  - gold-paper-patterns
---

# Gold-paper style patterns for CFD-AI / SciML prose

Purpose: make generated manuscript text closer to the gold-paper target, not merely safer. This file focuses on the criticism that AI-assisted papers often use unnatural words, generic context, and paragraph rhythms that do not sound like normal fluid-mechanics or SciML papers.

This is a qualitative style guide derived from the package gold-paper notes. Do not present it as corpus statistics.

## What makes AI-written CFD-AI prose easy to spot

Typical failure modes:

1. **Method-first opening.** The text starts with “deep learning has revolutionized CFD” before naming a flow, variable, or numerical bottleneck.
2. **Decorative adjectives.** `novel`, `robust`, `powerful`, `comprehensive`, `seamless`, and `state-of-the-art` appear without a metric, baseline, or diagnostic.
3. **Generic context paragraph.** The introduction could fit any physics-ML paper after replacing two nouns.
4. **Over-symmetrical structure.** Every paragraph has the same “however, therefore, this paper” rhythm.
5. **Architecture fetish.** The model is described before the input/output map, governing quantity, reference data, or validation task.
6. **Evidence-free physical language.** “Physically consistent” is used when the paper only shows visually plausible fields.
7. **Fake completeness.** Unknown solver, grid, split, or code details are smoothed over instead of being marked as missing.
8. **Context drift.** Results discuss broad CFD acceleration when the evidence supports only a specific reconstruction/prediction task.

## Gold-paper paragraph moves

### 1. Problem-context paragraph

Gold-paper texture starts with a physical or numerical problem, not AI capability.

Pattern:

> [Flow/process] requires [quantity/diagnostic] at [resolution/regime] because [physical/numerical bottleneck]. Conventional [DNS/LES/RANS/experiment/interpolation] is limited by [cost/data/sensing/closure/control constraint].

Use nouns like:

- velocity field, pressure field, vorticity field, wall shear stress, drag coefficient, lift coefficient;
- low-resolution snapshot, sparse sensor, high-fidelity reference, DNS/LES/RANS, PIV, wake, channel flow, homogeneous turbulence;
- Reynolds number, friction Reynolds number, rollout horizon, temporal correlation, spectrum, residual.

Avoid:

> Recent advances in artificial intelligence have opened new possibilities for solving complex CFD problems.

### 2. Gap paragraph

Gold-paper gap is narrow and testable.

Pattern:

> Existing [method family] addresses [nearby task], but [specific missing condition] remains unresolved: [resolution gap, sparse observation, unseen regime, physical diagnostic, uncertainty, solver compatibility, experimental constraint].

Bad gap:

> However, existing approaches lack robustness and generalizability.

Better gap:

> Existing reconstruction studies show lower field error on randomly split snapshots, but do not test whether high-wavenumber vorticity content is recovered under coarser spatial sampling or unseen Reynolds-number conditions.

### 3. Method-role paragraph

The method is introduced as a role in the scientific workflow.

Pattern:

> Here, we use [architecture/model family] to map [input representation] to [target quantity] for [flow case/regime]. The model is trained on [reference data] and compared with [baseline] under [split].

Do not say only:

> We propose a novel AI framework.

### 4. Evidence paragraph

Gold-paper results are not just metrics. They stack evidence.

Preferred order:

1. baseline and primary metric;
2. field visualization with error map;
3. physical/statistical diagnostic;
4. ablation or mechanism evidence;
5. generalization/stress test;
6. limitation/failure boundary.

Pattern:

> We assess the reconstruction using [metric] against [baseline], then examine [vorticity PDF/spectrum/residual/force history] to test whether lower error corresponds to physically meaningful recovery.

### 5. Limitation paragraph

A normal paper names the boundary before reviewers do.

Pattern:

> The claim is limited to [regime/data/split/geometry/horizon]. Extension to [untested axis] requires [specific experiment or diagnostic].

Bad:

> Future work will improve scalability and robustness.

Better:

> The present evidence does not establish robustness to noisy sparse sensors or Reynolds-number extrapolation; those claims require controlled noise sweeps and holdout regimes absent from the training data.

## Author-pattern reminders

### Fukami-type reconstruction

- Natural object: reconstruction of high-resolution flow fields from low-resolution or sparse inputs.
- Natural evidence: interpolation baseline, relative field error, vorticity contours, PDFs, spectra, high-wavenumber recovery.
- Avoid: broad CFD acceleration or general turbulence prediction unless tested.

### Brunton-type taxonomy

- Natural object: ML as a role in fluid-mechanics workflow: sensing, modeling, simulation, control, optimization, discovery.
- Natural evidence: taxonomy, mechanism, physical prior, sparse/interpretable representation.
- Avoid: chronological citation dump.

### Maulik-type uncertainty / ROM / closure

- Natural object: reliability of surrogate/ROM/closure under uncertainty, sparse/noisy observations, rollout stability.
- Natural evidence: predictive distribution, calibration, confidence interval, stress test, classical ROM/closure baseline.
- Avoid: point accuracy alone supporting trust.

### Lee-type wake/mechanism

- Natural object: unsteady wake prediction, Reynolds-number split, conservation-law-informed loss, mechanism/feature analysis.
- Natural evidence: rollout horizon, mass/momentum residual, pressure/velocity field, Strouhal/frequency/force diagnostics, Fourier/feature-map analysis.
- Avoid: “complex dynamics” without mechanism or diagnostic.

### Vinuesa-type opportunity+caveat

- Natural object: ML enhances CFD/experiments by addressing a named bottleneck.
- Natural evidence: where ML enters the workflow and what remains limited.
- Avoid: replacement rhetoric.

## Rewrite checklist

Before accepting generated prose, search for these patterns:

- `AI framework`, `powerful`, `comprehensive`, `seamless`, `unlock`, `transformative`, `robust`, `generalizable`, `physically consistent`, `state-of-the-art`, `complex dynamics`.
- If present, replace with flow case, variable, metric, diagnostic, baseline, and scope.
- Check whether the first three sentences contain a physical object, not just AI capability.
- Check whether each paragraph has a local purpose: context, gap, method role, evidence, limitation.
- Check whether a skeptical reviewer can identify exactly what was tested and what was not.

## One-sentence gold-paper target

> We use [model family] to map [input] to [target variable] for [flow/regime], compare against [baseline] using [metric], and test physical credibility with [diagnostic], with claims limited to [scope].
