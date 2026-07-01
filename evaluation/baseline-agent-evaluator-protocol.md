---
title: Baseline-agent + evaluator protocol
created: 2026-06-30
updated: 2026-06-30
source: internal evaluator
status: draft
tags:
  - cfd-ai
  - skill-evaluation
  - multi-agent
---

# Baseline-agent + evaluator protocol

Purpose: test whether the CFD-AI/SciML skill package actually improves manuscript work.

The weak agent is intentionally underpowered: it receives a skill and a task, then tries to critique/write/reconstruct. The evaluator compares its output against gold-standard papers and scores it. the evaluator updates the skill based on failures.

## Agents

### 1. Baseline Writer / Baseline Reviewer

Inputs:

- One skill or skill subset.
- A task prompt.
- Limited manuscript/paper excerpt.

Constraints:

- Must follow the skill literally.
- Must output in the skill's required schema.
- Must mark unknowns instead of inventing.

Purpose:

- Reveal whether the skill is operational enough for a weak agent.

### 2. Evaluator Agent

Inputs:

- Baseline-agent output.
- Gold-standard paper excerpt/metadata.
- Evaluation rubric.

Outputs:

- Scorecard.
- Missed criteria.
- Hallucinations/inventions.
- Skill-level fix recommendations.

### 3. Evaluator Integrator

Role:

- Does not trust either agent blindly.
- Reads evidence, updates skill text, keeps version notes.
- Runs next iteration.

## Task families

### A. Gold-answer reconstruction

Give baseline agent a title/abstract from a gold paper. Ask it to infer:

- problem statement
- gap
- contribution
- required evidence
- likely figure structure
- reviewer risks

Evaluator checks against full paper notes.

### B. Reviewer attack simulation

Give a weak manuscript paragraph with missing CFD details.

Baseline agent must flag:

- missing equations/BC/IC
- missing solver/grid/CFL
- baseline weakness
- absent physical diagnostics
- unsupported claims

Evaluator checks whether high-risk omissions were found.

### C. Experiment plan generation

Give method claim:

> Our neural operator generalizes to turbulent flows across Reynolds numbers.

Baseline agent must propose:

- baseline matrix
- train/test split
- unseen Re tests
- spectral diagnostics
- rollout stability
- runtime/parameter reporting
- failure cases

Evaluator scores completeness.

### D. Related-work positioning

Give a proposed paper idea and close prior art candidates.

Baseline agent must produce:

- taxonomy
- close prior-art risks
- gap paragraph
- citations to verify

Evaluator penalizes fake novelty.

### E. Figure storyboarding

Give results inventory.

Baseline agent must propose figure sequence:

1. task schematic
2. dataset/flow setup
3. main quantitative table
4. GT/pred/error field
5. physical diagnostic/spectrum
6. ablation
7. generalization/failure

Evaluator checks whether each figure supports a claim.

## Scoring rubric

Score each 0–3.

| Criterion | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| Physics specificity | generic | names physics vaguely | checks some CFD details | equations/regimes/BC/IC/solver all targeted |
| Evidence alignment | unsupported | weak mapping | mostly mapped | every claim tied to evidence/TODO |
| Reviewer realism | no risk | generic risk | relevant risks | likely reviewer objections prioritized |
| Gold-paper alignment | none | superficial | partial | reproduces answer-key patterns |
| Output schema | chaotic | partial | usable | exact structured output |
| Non-hallucination | invents | some inventions | marks some unknowns | clean unknown/TODO discipline |
| Actionability | vague | broad | concrete | directly executable edits/experiments |

Pass threshold:

- MVP: average ≥ 2.2
- Strong: average ≥ 2.6
- Release: average ≥ 2.8 and no hallucination score below 2

## Iteration loop

1. Select one skill and one test task.
2. Run baseline agent.
3. Run evaluator.
4. the evaluator inspects evaluator comments.
5. Patch skill:
   - add missing checklist item
   - sharpen output schema
   - add anti-pattern
   - add example
6. Re-run same task.
7. Record before/after score.
8. Only keep changes that improve score or reduce hallucination.

## Competitive loop

Run two variants:

- Agent A: current skill.
- Agent B: experimental skill patch.

Evaluator compares blind outputs.

Keep B only if:

- score improves, or
- output is shorter but preserves critical risks, or
- hallucination rate decreases.

## Artifacts to save

```text
evaluation/runs/YYYY-MM-DD_task-name/
├── prompt.md
├── skill-version.md
├── baseline-output.md
├── evaluator-scorecard.md
├── evaluator-decision.md
└── patched-skill-diff.md
```

## Minimal first benchmark set

1. Fukami super-resolution paper: reconstruct evidence/figure pattern.
2. Brunton ARFM review: reconstruct taxonomy structure.
3. Lee cylinder wake prediction: reviewer attack on data/solver/generalization.
4. Maulik turbulence closure: experiment matrix and uncertainty/verifiability.
5. Vinuesa emerging trends: related-work positioning and responsible claims.

## Failure modes to detect

- Generic “add more baselines” without naming baselines.
- Says “physics-informed” without locating physics in loss, architecture, data, or constraints.
- Calls something robust without robustness tests.
- Invents solver details.
- Misses train/test leakage.
- Ignores nondimensional groups.
- Produces pretty prose but no experiment plan.

This protocol is the part that prevents skill theater. Good. Annoying. Necessary.
