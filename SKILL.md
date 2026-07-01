---
name: cfd-ai-paper-skills
description: Use when writing, reviewing, auditing, revising, or producing LaTeX for CFD-AI and scientific-ML manuscripts, reviews, experiment plans, reproducibility audits, related-work positioning, reviewer responses, or benchmark evaluations.
version: v0.6.5
---

# CFD-AI Paper Skills

Umbrella router for the CFD-AI paper skills package. Use this root skill as the installable entrypoint when the task involves CFD-AI, scientific ML, neural operators, PINNs, surrogate modeling, turbulence closure, flow reconstruction, CFD acceleration, geometry-aware models, flow control, or journal-paper production.

## Trigger Conditions

Use this package when the user asks for any of the following:

- write, revise, or review a CFD-AI/SciML manuscript, abstract, introduction, method, result, discussion, or limitations section;
- audit unsupported claims, reviewer risks, reproducibility, experiment design, validation splits, baselines, diagnostics, figures, or LaTeX build readiness;
- plan or critique CFD-AI experiments, benchmark tasks, ablations, held-out regimes, geometry generalization, mesh transfer, solver coupling, or physical diagnostics;
- synthesize related work, build a review-paper taxonomy, position a contribution, or convert a citation dump into a CFD-native evidence map;
- detect and rewrite AI-ish manuscript language so it follows field-native, gold-paper-like CFD-AI/SciML prose patterns;
- produce a LaTeX manuscript seed, response-to-reviewers letter, revision plan, journal checklist, or benchmark review output.

Do not use this package for generic grammar polishing unless the task also needs claim-evidence alignment, scientific accuracy boundaries, CFD/SciML validation logic, or journal-review risk analysis.

## Progressive Disclosure

Read only the files needed for the requested artifact first:

1. Start with this router and identify the task type.
2. Read the relevant subskill `SKILL.md` files from the routing table.
3. Read only the references, rubrics, examples, and templates named by those subskills.
4. Load gold-paper notes only when they directly inform the task's writing pattern, experiment logic, figure logic, or reviewer-defense pattern.
5. Use rubrics and templates after the task route is known, not before.

Unknown scientific facts stay `TODO`. Do not infer solver settings, mesh details, train/test splits, DOI values, dataset licenses, benchmark numbers, author roles, or corresponding-author status from context.

## Routing Table

| Task type | Start with | Add when needed |
|---|---|---|
| Manuscript writing, abstract/intro rewrite, or AI-ish prose repair | `skills/scientific-journal-writing/SKILL.md` | `references/gold-paper-style-patterns.md`, `rubrics/gold-paper-closeness-rubric.md`, `examples/generic-ai-to-gold-paper-prose.md` |
| Unsupported claims, overclaim rewrites, claim-evidence maps | `skills/paper-claim-auditor/SKILL.md` | `skills/cfd-ml-paper-reviewer/SKILL.md`, `rubrics/claim-evidence-rubric.md`, `templates/claim-evidence-map.md` |
| Decision-oriented reviewer audit, rejection-risk gate, submission readiness | `skills/reviewer-audit-toolkit/SKILL.md` | `templates/reviewer-audit-report.md`, `rubrics/reviewer-audit-rubric.md`, `skills/paper-claim-auditor/SKILL.md`, `skills/cfd-ml-paper-reviewer/SKILL.md` |
| Reproducibility and numerical-method audit | `skills/cfd-reproducibility-checker/SKILL.md` | `rubrics/cfd-reproducibility-rubric.md`, `references/field-terminology-style-guide.md` |
| Experiment design | `skills/experiment-design-for-sciml/SKILL.md` | `skills/sciml-experiment-auditor/SKILL.md`, `templates/experiment-plan.md`, `rubrics/sciml-experiment-rubric.md` |
| Experiment audit, validation split critique, benchmark-risk review | `skills/sciml-experiment-auditor/SKILL.md` | `skills/cfd-reproducibility-checker/SKILL.md`, `references/cfd-ai-benchmark-landscape.md` |
| Related-work positioning or citation-map construction | `skills/related-work-cartographer/SKILL.md` | `skills/related-work-synthesis/SKILL.md`, `references/gold-standard-paper-map.md` |
| Review article or taxonomy synthesis | `skills/related-work-synthesis/SKILL.md` | `skills/scientific-journal-writing/SKILL.md`, `skills/figure-and-result-storytelling/SKILL.md` |
| Figure/result story, table design, visual evidence logic | `skills/figure-and-result-storytelling/SKILL.md` | `rubrics/figure-evidence-rubric.md`, `references/figure-archetypes.md` |
| LaTeX manuscript or PDF-oriented production | `skills/latex-paper-production/SKILL.md` | `skills/scientific-journal-writing/SKILL.md`, compile/build checks, selected templates |
| Reviewer simulation and journal-risk report | `skills/reviewer-simulator/SKILL.md` | `skills/cfd-ml-paper-reviewer/SKILL.md`, `templates/reviewer-report.md` |
| Response to reviewers | `skills/response-to-reviewers/SKILL.md` | `skills/paper-revision-loop-manager/SKILL.md`, `templates/response-letter.md` |
| Revision planning and manuscript-change management | `skills/paper-revision-loop-manager/SKILL.md` | `skills/reviewer-audit-toolkit/SKILL.md`, `skills/scientific-journal-writing/SKILL.md`, `templates/reviewer-editor-loop-report.md`, `rubrics/reviewer-editor-loop-rubric.md` |
| Multi-agent reviewer-editor workflow | `skills/multi-agent-paper-orchestrator/SKILL.md` | `references/multi-agent-paper-roles.md`, `templates/multi-agent-paper-workflow-report.md`, `rubrics/multi-agent-paper-workflow-rubric.md` |
| Ethics, limitations, and LLM disclosure | `skills/limitations-ethics-llm-disclosure/SKILL.md` | journal instructions supplied by the user |
| Benchmark review output or package evaluation | `evaluation/tasks/*.md` matching the topic | `evaluation/scorecards/cfd-ai-skill-scorecard.md`, relevant subskills above |

## Output Schema

Choose the contract that matches the route. If the user asks for multiple artifacts, keep each contract separate rather than merging them into prose.

### Claim-Evidence Map

| Claim | Evidence supplied | Missing evidence/TODO | Reviewer risk | Safer wording | Location |
|---|---|---|---|---|---|

### Reviewer-Risk Report

| Severity | Issue | Evidence boundary | Likely reviewer objection | Required fix | Suggested rewrite |
|---|---|---|---|---|---|

### Reviewer Audit Gate

| Gate | Decision | Evidence boundary | Minimum rescue path |
|---|---|---|---|
| Submission readiness | accept / revise / reject-risk | | |
| Fatal blockers | count | | |
| Major blockers | count | | |

Use `templates/reviewer-audit-report.md` when the user asks whether a manuscript is submission-ready.

### Reproducibility Checklist

| Item | Known | Missing/TODO | Why it matters | Manuscript location |
|---|---|---|---|---|

### Experiment Matrix

| Claim tested | Dataset/flow case | Split axis | Baseline | Metric/diagnostic | Ablation/UQ | Failure mode | Reproducibility TODO |
|---|---|---|---|---|---|---|---|

### LaTeX Manuscript Seed

- complete `main.tex` source when requested;
- standard packages unless the user supplies a template;
- `TODO` bibliography entries for unverified citations;
- figure placeholders that state the claim supported by each figure;
- explicit compile notes and no external image dependency unless supplied.

### Response Letter

| Reviewer point | Response strategy | Evidence needed | Manuscript change | Draft response | Status |
|---|---|---|---|---|---|

### Benchmark Review Output

| Axis | Evidence expected | Evidence supplied | Failure mode caught | Score/decision | TODO |
|---|---|---|---|---|---|

### Gold-Paper Manuscript Seed / Style Reconstruction

| Section | Gold-paper move expected | Current draft evidence | AI-ish marker | Required rewrite/TODO |
|---|---|---|---|---|

### Reviewer-Editor Loop

| Stage | Output |
|---|---|
| Reviewer gate | accept / revise / reject-risk + Fatal/Major blocker count |
| Editor rewrite | revised abstract/section with unsupported claims removed or bounded |
| Re-audit | before/after risk and residual blockers |
| Next actions | experiments/tables/figures needed to rescue remaining claims |

Use `templates/reviewer-editor-loop-report.md` for full reviewer→editor→reviewer cycles.

### Multi-Agent Paper Workflow

| Agent | Artifact |
|---|---|
| Reviewer | Fatal/Major rejection risks |
| Evidence Auditor | claim-evidence map and TODOs |
| Experiment Planner | validation/baseline/diagnostic rescue plan |
| Figure/Table Editor | evidence-bearing figure/table sequence |
| Prose Editor | field-native revised text |
| Gatekeeper | residual-risk re-audit |

Use `templates/multi-agent-paper-workflow-report.md` when the user asks for explicit multi-agent structure.

## Anti-Patterns

- Generic polishing that makes claims smoother without checking evidence.
- Inventing solver settings, benchmark numbers, DOI values, dataset licenses, author roles, citation metadata, hardware/runtime, or train/test split details.
- Treating resource lists, library features, or citation density as proof of benchmark quality.
- Making unbounded claims such as "generalizable", "real-time", "physically consistent", "state-of-the-art", "robust", or "solves turbulence" without same-scope evidence.
- Collapsing different validation axes into one generic "accuracy" claim.
- Treating random snapshot performance as geometry, regime, mesh, BC/IC, time-horizon, or solver-coupled generalization.
- Producing LaTeX/PDF deliverables without a compile/build check or explicit note that the check could not be run.
- Hiding unknowns in polished prose instead of marking them as `TODO`.
- Letting generic AI academic phrases stand in for field-native problem, gap, evidence, and limitation moves.

## Verification Checklist

- Relevant subskills were read before drafting the artifact.
- Reviewer-audit tasks produce a gate decision, Fatal/Major blocker count, and minimum rescue path.
- Reviewer-editor loop tasks produce a reviewer gate, an editor rewrite, and a re-audit with residual blockers.
- Multi-agent paper workflows keep role outputs separate until the orchestrator merge and gatekeeper re-audit.
- Every major claim is mapped to evidence, limitation, or `TODO`.
- CFD/SciML validation axes are explicit: regime, geometry, mesh, BC/IC, time horizon, QoI, diagnostics, UQ, runtime, and solver coupling where applicable.
- Resource lists, tools, datasets, and benchmark suites are distinguished by source scope and evidence role.
- Reviewer-risk terms are either avoided, bounded, or rewritten.
- Tables/checklists include missing-evidence columns when facts are incomplete.
- LaTeX deliverables include compile/build evidence or a clear reason the check could not be run.
- Output stays within the evidence packet and does not invent scientific facts.
- Manuscript prose can be scored by `rubrics/gold-paper-closeness-rubric.md` when the task includes writing or style reconstruction.
