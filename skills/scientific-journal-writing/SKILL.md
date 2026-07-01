---
name: scientific-journal-writing
description: Use when writing, revising, outlining, or critiquing CFD-AI and scientific ML journal papers; focuses on argument structure, claim-evidence alignment, novelty, and reviewer defense.
version: 0.4.0
author: CFD-AI Paper Skills maintainers
metadata:
  short-description: Structure and sharpen CFD-AI/SciML journal manuscripts
  gold-standard-authors: [Kai Fukami, Steven L. Brunton, Romit Maulik, Sangseung Lee, Ricardo Vinuesa]
---

# Scientific Journal Writing for CFD-AI / SciML

## Trigger

Use when the user asks for paper outline, abstract, introduction, methods, results, discussion, conclusion, novelty framing, contribution bullets, or manuscript critique for CFD-AI/SciML work.

## Core rule

Do not merely improve English. First make the manuscript defensible.

A paper is defensible only if it has:

1. a physics/engineering problem,
2. a specific gap,
3. a calibrated contribution,
4. evidence for every major claim,
5. limitations before reviewers weaponize them.

## Gold-standard writing target

Model the discipline of papers by Fukami, Brunton, Maulik, Lee, and Vinuesa:

- physics-first setup,
- ML role clearly scoped,
- reproducible numerical setup,
- fair baselines,
- physical diagnostics,
- generalization tests,
- figure sequence that proves claims,
- cautious wording.

The target is not “more academic English.” It is normal CFD-AI/SciML paper texture: physical problem first, narrow gap second, method role third, evidence sequence fourth, limitation boundary last. If the prose could fit any AI-for-science paper after replacing two nouns, it is not close enough to the gold-paper target.

Use progressive disclosure:

| Task | Read first |
|---|---|
| Super-resolution/reconstruction abstract, intro, or results | `references/gold-papers/fukami-2019-super-resolution-jfm.md` |
| Spatio-temporal super-resolution | `references/gold-papers/fukami-2021-spatiotemporal-super-resolution-jfm.md` |
| Field positioning or related-work taxonomy | `references/gold-papers/brunton-2020-machine-learning-fluid-mechanics.md` and `references/gold-papers/vinuesa-2022-enhancing-cfd-ml.md` |
| ML workflow staging / physics insertion points | `references/gold-papers/brunton-2021-applying-ml-fluid-mechanics.md` |
| Uncertainty/trustworthy surrogate claims | `references/gold-papers/maulik-2020-probabilistic-neural-networks-prf.md` |
| Cylinder-wake prediction/generalization | `references/gold-papers/lee-2019-cylinder-wake-jfm.md` |
| Experimental-fluid-mechanics opportunity framing | `references/gold-papers/vinuesa-2023-transformative-ml-experiments-nrp.md` |
| Claim strength decisions | `rubrics/claim-evidence-rubric.md` |
| AI-ish / field-inappropriate vocabulary | `references/field-terminology-style-guide.md`, `rubrics/vocabulary-style-rubric.md`, `examples/ai-ish-to-field-native-prose.md` |
| Gold-paper closeness / normal paper texture | `references/gold-paper-style-patterns.md`, `rubrics/gold-paper-closeness-rubric.md`, `examples/generic-ai-to-gold-paper-prose.md` |

## Workflow

### 1. Classify manuscript state

Classify as:

- idea only
- outline
- partial draft
- full draft
- revision
- response letter
- LaTeX production

If missing, infer. Ask only when ambiguity blocks work.

### 2. Extract one-sentence claim

Use:

> We propose X for Y under Z physical/numerical conditions, using W, and demonstrate A/B/C against baselines D/E.

If this cannot be written, stop polishing and diagnose the missing piece.

### 3. Contribution taxonomy

Classify each contribution:

- method/architecture
- physical modeling
- numerical algorithm
- surrogate/ROM/closure
- dataset/benchmark
- empirical physical insight
- uncertainty/verifiability
- software/workflow

Reject vague contribution bullets such as “we propose a novel framework.” Require mechanism + evidence.

### 4. Claim-evidence map

For every major claim, build:

| Claim | Evidence needed | Current evidence | Risk |
|---|---|---|---|
| accurate | fair metrics + baselines | ? | high if no baseline |
| physically consistent | conservation/residual/BC/spectrum | ? | high |
| generalizes | unseen Re/geometry/BC/time | ? | high |
| efficient | wall-clock/memory/params | ? | medium |
| robust | noise/sparsity/OOD tests | ? | high |

Unsupported claims become TODOs, not prose.

### 5. Section logic

#### Abstract

Five moves:

1. physical/engineering context,
2. unresolved limitation,
3. proposed method,
4. concrete evidence/result,
5. implication/limited scope.

No “promising,” “robust,” “SOTA,” or “physically consistent” without measurable evidence.

Gold-paper closeness gate: the first sentence must name a physical/numerical object or bottleneck, not AI capability. Accept “high-resolution vorticity reconstruction from low-resolution snapshots”; reject “AI has revolutionized CFD.”

#### Introduction

Flow:

1. Why the fluid/process problem matters.
2. Why conventional CFD/experiments/current ML are limited.
3. Narrow gap.
4. Proposed approach.
5. Contribution bullets with evidence hooks.

#### Related work

Use taxonomy, not chronology:

- fluid-mechanics workflow role: discovery, modeling, sensing/reconstruction, experiments, closure, ROM, control, optimization, acceleration,
- ML insertion point: problem, data, architecture, loss, optimization, deployment/control,
- then method family: PINN, operator, CNN, GNN, ROM, sparse identification, RL, generative, or domain-specific model.

End with precise contrast.

#### Methods

Must include governing equations/assumptions, solver/data generation, BC/IC, nondimensional groups where relevant, architecture, loss, training, implementation details.

#### Results

Recommended sequence:

1. validation/sanity case,
2. main quantitative comparison,
3. field visualization GT/pred/error,
4. physics diagnostic,
5. ablation,
6. generalization,
7. efficiency,
8. failure/limitations.

#### Discussion

Explain why results matter physically. Do not restate tables.

## Output template

Return:

1. One-sentence paper claim
2. Contribution bullets
3. Claim-evidence map
4. Section-level structure
5. Reviewer attack points
6. Required evidence/TODOs
7. Gold-paper closeness score, if writing/reconstruction is requested
8. Exact rewrite, if requested

For abstracts, use `examples/bad-to-good-abstract.md` as the style and evidence standard. For prose that sounds generic or AI-written, use `references/gold-paper-style-patterns.md`, `rubrics/gold-paper-closeness-rubric.md`, and `examples/generic-ai-to-gold-paper-prose.md`. When the user wants reviewer criticism to drive the rewrite, route through `skills/paper-revision-loop-manager/SKILL.md` and use `templates/reviewer-editor-loop-report.md`. For experiments, route to `templates/experiment-plan.md` and `rubrics/sciml-experiment-rubric.md`.

## v0.4 eval-backed checks

These checks were added after simulated baseline-agent failures in `evaluation/runs/2026-06-30-v04-*`.

| Trigger | Extra requirement |
|---|---|
| Spatio-temporal super-resolution | Separate spatial downsampling, temporal frame interval, high-resolution reference, and time-axis diagnostics. |
| Brunton-style taxonomy | Classify by workflow role before model family; gap paragraph must name CFD bottleneck, closest prior role, unresolved boundary, mechanism, and decisive evidence. |
| Cylinder/wake prediction | State Re/regime, split type, rollout horizon, and physical-consistency evidence before polishing prose. |

## Anti-patterns

- “novel” repeated as a substitute for novelty.
- “physics-informed” without saying where physics enters.
- “generalizable” from interpolation-only tests.
- “real-time” without hardware/timing.
- “state-of-the-art” without a fair baseline matrix.
- Generic opening context that could belong to any AI-for-science paper.
- Method-first paragraphs that name the network before the flow case, variable, and reference data.

## Verification

Before finalizing:

- Every claim is supported or marked TODO.
- Unknown numerical details are not invented.
- Reviewer objections are explicit.
- Suggested text preserves scientific tone and does not overclaim.
- The final answer can be scored by `rubrics/claim-evidence-rubric.md`.
- If manuscript prose is generated, the final answer can also be scored by `rubrics/gold-paper-closeness-rubric.md`.
