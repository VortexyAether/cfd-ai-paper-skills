---
name: paper-claim-auditor
description: Use when auditing a CFD-AI/SciML manuscript's abstract, introduction, contributions, or discussion to verify that every claim is supported by evidence and scoped correctly.
version: 0.3.0
author: CFD-AI Paper Skills maintainers
metadata:
  short-description: Claim-evidence audit for CFD-AI/SciML papers
---

# Paper Claim Auditor

## Trigger

Use when asked to avoid overclaiming, check novelty, audit abstract/introduction/conclusion, or map claims to evidence.

## Progressive disclosure

- Read `rubrics/claim-evidence-rubric.md` before scoring.
- Read `rubrics/vocabulary-style-rubric.md` when the text contains loaded adjectives such as robust, generalizable, physically consistent, novel, state-of-the-art, interpretable, efficient, real-time, promising, or transformative.
- Use `references/field-terminology-style-guide.md` to replace AI-ish prose with field-native CFD-AI/SciML wording.
- Use `templates/claim-evidence-map.md` for full audits.
- Use `examples/bad-to-good-abstract.md` and `examples/ai-ish-to-field-native-prose.md` when rewriting abstracts or conclusions.
- Read gold-paper files only when the claim domain matches:
  - reconstruction: `references/gold-papers/fukami-2019-super-resolution-jfm.md`
  - field taxonomy: `references/gold-papers/brunton-2020-machine-learning-fluid-mechanics.md`
  - uncertainty/trust: `references/gold-papers/maulik-2020-probabilistic-neural-networks-prf.md`
  - wake prediction: `references/gold-papers/lee-2019-cylinder-wake-jfm.md`
  - CFD opportunity framing: `references/gold-papers/vinuesa-2022-enhancing-cfd-ml.md`

## Workflow

1. Extract all major claims.
2. Classify claim type: novelty, accuracy, physical consistency, generalization, robustness, efficiency, interpretability, reproducibility.
3. Map each claim to evidence location.
4. Score evidence strength: supported / weak / missing / overclaimed.
5. Suggest safer wording or required experiment.

## Output schema

| Claim | Type | Evidence location | Status | Risk | Fix |
|---|---|---|---|---|---|

Add a rubric score:

| Claim | Score 0-3 | Missing evidence | Safer wording |
|---|---:|---|---|

## Anti-patterns

- “robust” without robustness tests.
- “generalizable” from random split only.
- “physics-informed” without locating physics in loss/architecture/data/constraints.
- “state-of-the-art” without fair baselines.
- “real-time” without hardware/runtime.

## Verification

- Every claim has evidence or TODO.
- No solver/citation details invented.
- Safer wording preserves contribution without hype.
- Claims scored 0-1 are either removed, narrowed, or converted to explicit TODOs.
