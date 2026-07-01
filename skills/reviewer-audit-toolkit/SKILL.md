---
name: reviewer-audit-toolkit
description: Use when turning a CFD-AI/SciML draft, abstract, result section, or manuscript idea into a strict reviewer-audit gate with rejection risks, missing evidence, and concrete fixes.
version: 0.1.0
author: CFD-AI Paper Skills maintainers
metadata:
  short-description: Decision-oriented reviewer audit gate for CFD-AI/SciML manuscripts
---

# Reviewer Audit Toolkit

## Trigger

Use when the task asks for:

- “will reviewers reject this?”;
- “audit this paper/abstract/experiment plan”;
- “make a rejection-risk checklist”;
- “turn this into reviewer-safe claims”;
- “what evidence is missing before submission?”;
- “score whether this draft is journal-ready.”

This skill is the package’s decision-oriented audit route. It combines claim auditing, CFD/SciML review, reproducibility, experiment validation, figure evidence, and field-native wording into one gate report. When the user also wants the draft rewritten after the audit, route to `skills/paper-revision-loop-manager/SKILL.md` so an editor pass and re-audit are enforced.

## Progressive disclosure

Read these in order:

1. `skills/paper-claim-auditor/SKILL.md`
2. `skills/cfd-ml-paper-reviewer/SKILL.md`
3. `skills/sciml-experiment-auditor/SKILL.md`
4. `skills/cfd-reproducibility-checker/SKILL.md`
5. `rubrics/reviewer-audit-rubric.md`
6. `rubrics/claim-evidence-rubric.md`
7. `rubrics/sciml-experiment-rubric.md`
8. `rubrics/cfd-reproducibility-rubric.md`
9. `templates/reviewer-audit-report.md`

Add topic-specific gold-paper notes only when the domain is clear:

- reconstruction / super-resolution: Fukami notes;
- wake prediction / flow-structure learning: Lee notes;
- uncertainty / surrogate trust: Maulik notes;
- review/taxonomy / field positioning: Brunton notes;
- CFD-AI opportunity/limitation framing: Vinuesa notes.

## Workflow

### 1. Source-scope ledger

Start by separating what is supplied from what is inferred.

- Supplied manuscript text, abstract, figures, tables, methods, source notes.
- Missing but needed evidence.
- Forbidden inventions: solver settings, mesh, metrics, DOI, code links, author roles, exact benchmark numbers.

### 2. Claim extraction

Extract every major claim and classify it:

- novelty;
- accuracy;
- physical consistency;
- generalization;
- robustness;
- efficiency / real time;
- interpretability;
- reproducibility;
- solver replacement / deployment;
- mechanism or physics discovery.

### 3. Reviewer-risk gate

Score each claim by rejection risk.

- **Fatal**: likely rejection unless fixed.
- **Major**: serious weakness that blocks strong acceptance.
- **Minor**: clarity, framing, or missing detail.
- **Optional**: nice improvement.

A claim is Fatal when the text makes a high-level contribution claim but the evidence packet lacks the necessary validation axis.

### 4. Evidence-surface audit

For CFD-AI/SciML, check these surfaces explicitly:

- physical problem: governing variables, geometry/domain, BC/IC, regime, nondimensional numbers;
- numerical data: solver/fidelity, mesh/grid, timestep/CFL, convergence, train/val/test split;
- ML method: input/output map, architecture, normalization, loss terms, physics location, optimizer, uncertainty;
- validation: leakage-safe split, held-out geometry/Re/BC/mesh/time horizon, OOD/noise/sparse-sensor stress;
- metrics: relative L2/RMSE/MAE plus physical diagnostics and QoIs;
- baselines: classical CFD/ROM/interpolation/closure and same-scope ML baselines;
- figures: GT/input/pred/error, same color scale, quantitative caption, diagnostic/failure panel;
- deployment: runtime, memory, hardware, solver-coupled cost, fallback policy.

### 5. Action plan

Convert audit findings into fixes:

- required experiment;
- required table/figure;
- safer wording;
- manuscript location to edit;
- minimum evidence needed to remove the risk.

## Output schema

Use the full template for serious audits. For short responses, preserve the same fields in compressed form.

### Gate summary

| Gate | Decision | Reason |
|---|---|---|
| Submission readiness | accept / revise / reject-risk | |
| Fatal issues | count | |
| Major issues | count | |
| Highest-risk claim | claim text | |

### Reviewer-risk ledger

| Severity | Claim / issue | Evidence supplied | Missing evidence | Likely reviewer objection | Required fix | Safer wording |
|---|---|---|---|---|---|---|

### Evidence-surface checklist

| Surface | Present? | Missing/TODO | Why reviewers care |
|---|---|---|---|

### Action list

| Priority | Fix | Artifact to add | Claim rescued |
|---|---|---|---|

## Anti-patterns

- Producing a polite peer review without a gate decision.
- Listing “more baselines” without naming the baseline class and same-scope condition.
- Treating missing solver/mesh/BC/split details as cosmetic.
- Accepting pretty contour plots without physical diagnostics, error maps, QoIs, or failure cases.
- Saying “generalization” from random snapshots.
- Saying “physics-informed” without identifying whether physics enters loss, architecture, constraints, data, or evaluation.
- Rewriting overclaims into smoother prose while leaving evidence gaps unresolved.
- Inventing exact details to make the paper look complete.

## Verification

- Every Fatal/Major issue maps to a claim or missing evidence surface.
- Every loaded adjective is either removed, bounded, or paired with evidence.
- Unknowns are marked as TODO, not filled from memory.
- The audit produces at least one concrete experiment/table/figure fix for each Fatal issue.
- The final decision is harsher than the prose if evidence is missing. Niceness is not evidence.
