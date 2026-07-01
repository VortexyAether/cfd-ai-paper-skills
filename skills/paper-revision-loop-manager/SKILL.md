---
name: paper-revision-loop-manager
description: Use when running iterative reviewer-to-editor revision of a CFD-AI/SciML manuscript: reviewer audit, editorial rewrite, re-audit, residual-risk tracking, and submission-readiness gating.
version: 0.4.0
author: CFD-AI Paper Skills maintainers
metadata:
  short-description: Reviewer-to-editor writing loop for CFD-AI/SciML papers
---

# Paper Revision Loop Manager

## Trigger

Use for major manuscript improvement, advisor feedback, reviewer comments, abstract rescue, journal-readiness passes, or repeated audit/rewrite cycles.

Use this skill when the user wants the paper to become **better written because it has survived reviewer logic**, not merely smoother.

## Core idea

Run two roles in sequence:

1. **Reviewer**: harshly audits claim-evidence risk and identifies Fatal/Major blockers.
2. **Editor**: rewrites the manuscript so the text becomes readable, field-native, and evidence-bounded.
3. **Reviewer again**: re-audits the edited text and records residual risks.

The editor is not allowed to invent evidence. If the reviewer finds a missing experiment, the editor must either:

- remove the claim;
- narrow the claim;
- add a TODO/evidence placeholder;
- add a required table/figure/experiment plan;
- or explicitly mark the claim as unsupported.

## Progressive disclosure

Read in this order:

1. `skills/reviewer-audit-toolkit/SKILL.md`
2. `skills/scientific-journal-writing/SKILL.md`
3. `skills/paper-claim-auditor/SKILL.md`
4. `skills/cfd-ml-paper-reviewer/SKILL.md`
5. `rubrics/reviewer-editor-loop-rubric.md`
6. `templates/reviewer-editor-loop-report.md`
7. `examples/reviewer-audit-to-editor-rewrite.md`

For explicit multi-agent workflows, route to `skills/multi-agent-paper-orchestrator/SKILL.md` after this loop manager identifies the revision goal.

Add section-specific skills as needed:

| Need | Add |
|---|---|
| Missing experiments / validation matrix | `skills/experiment-design-for-sciml/SKILL.md`, `skills/sciml-experiment-auditor/SKILL.md` |
| Missing numerics / reproducibility | `skills/cfd-reproducibility-checker/SKILL.md` |
| Missing figure logic | `skills/figure-and-result-storytelling/SKILL.md` |
| LaTeX output | `skills/latex-paper-production/SKILL.md` |
| Response letter | `skills/response-to-reviewers/SKILL.md` |

## Loop

### Pass 0 — Source-scope ledger

Record what exists before judging:

- draft text;
- available method details;
- available results/figures/tables;
- unavailable but needed evidence;
- facts that must remain TODO.

### Pass 1 — Reviewer audit

Use `reviewer-audit-toolkit` to produce:

- gate decision;
- Fatal/Major/Minor issues;
- claim-evidence map;
- missing evidence surfaces;
- required rescue experiments/tables/figures;
- unsafe phrases and safer wording.

### Pass 2 — Editor rewrite

Use `scientific-journal-writing` to rewrite under these rules:

- physical/numerical object first;
- gap second;
- method role third;
- evidence fourth;
- limitation boundary last;
- no loaded adjective without evidence;
- no hidden solver/data/metric/citation invention.

If evidence is missing, the editor writes cautious text and creates TODO placeholders rather than making the paper sound complete.

When the user wants both critique and improved writing, route through `skills/paper-revision-loop-manager/SKILL.md`: reviewer audit first, editor rewrite second, re-audit third. Do not let the writing pass outrun the evidence pass.

### Pass 3 — Re-audit

Reviewer audits the edited version:

- Which Fatal issues were removed?
- Which Major issues remain?
- Did the editor introduce any new overclaims?
- Are TODOs explicit enough to guide experiments?
- Is the manuscript safer but still meaningful?

### Pass 4 — Next-action plan

Prioritize only the actions that reduce reviewer risk:

1. evidence that rescues Fatal claims;
2. tables/figures that make evidence inspectable;
3. wording changes that prevent overclaiming;
4. polish only after Fatal/Major blockers are controlled.

## Output schema

Use `templates/reviewer-editor-loop-report.md` for full runs.

Compressed output:

| Stage | Output |
|---|---|
| Reviewer gate | accept / revise / reject-risk + blocker count |
| Editor action | removed/narrowed/rewrote claims and added TODOs |
| Revised text | edited abstract/section/manuscript seed |
| Re-audit | before/after risk and residual blockers |
| Next actions | experiments/tables/figures needed next |

## Anti-patterns

- Reviewer gives criticism, editor ignores it and only polishes English.
- Editor hides missing evidence by writing smoother prose.
- Reviewer keeps asking for broad “more validation” instead of exact rescue artifacts.
- Loop continues polishing while Fatal issues remain.
- Re-audit is skipped.
- Claims are downgraded silently without recording what changed.

## Verification

- Every Fatal/Major reviewer issue has an editor action or a TODO rescue artifact.
- The edited text is more readable but not more speculative.
- Before/after risk is recorded.
- Unsupported claims are removed, narrowed, or explicitly marked TODO.
- No endless polishing before fatal issues fixed.
