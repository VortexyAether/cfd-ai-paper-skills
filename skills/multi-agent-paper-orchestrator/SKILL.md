---
name: multi-agent-paper-orchestrator
description: Use when coordinating multiple specialized CFD-AI/SciML paper agents: reviewer, evidence auditor, experiment planner, figure editor, prose editor, and final gatekeeper.
version: 0.1.0
author: CFD-AI Paper Skills maintainers
metadata:
  short-description: Multi-agent orchestration pattern for reviewer-driven manuscript writing
---

# Multi-Agent Paper Orchestrator

## Trigger

Use when the user wants a CFD-AI/SciML manuscript improved by multiple roles instead of one monolithic writer:

- reviewer criticizes and finds rejection risks;
- evidence auditor checks claim support and missing facts;
- experiment planner proposes rescue validation;
- figure editor turns claims into figure/table evidence;
- prose editor rewrites the section;
- gatekeeper re-audits the edited draft;
- orchestrator repeats prose_editor -> gatekeeper in a bounded loop when residual blockers are fixable by wording or structure.

This skill can be executed in three modes:

1. **Simulated multi-agent mode**: one model runs the roles sequentially with strict role separation.
2. **Codex native subagent mode**: one Codex CLI session spawns project-scoped custom agents from `.codex/agents/` and manages them with `/agent`.
3. **External worker mode**: the orchestrator launches separate Hermes/Codex/Claude processes and verifies/integrates their outputs.

Use simulated mode for short abstracts. Use Codex native subagent mode when the user wants one Codex CLI session with internal parallel agents. Use external worker mode for durable long runs, separate worktrees, or non-Codex orchestration.

## Progressive disclosure

Read in this order:

1. `references/multi-agent-paper-roles.md`
2. `skills/paper-revision-loop-manager/SKILL.md`
3. `skills/reviewer-audit-toolkit/SKILL.md`
4. `skills/scientific-journal-writing/SKILL.md`
5. `skills/sciml-experiment-auditor/SKILL.md`
6. `skills/figure-and-result-storytelling/SKILL.md`
7. `rubrics/multi-agent-paper-workflow-rubric.md`
8. `templates/multi-agent-paper-workflow-report.md`

Add topic-specific gold-paper notes only after the manuscript domain is known. Do not give every worker every file by default; source scope is part of the experiment.

## Agent roles

| Role | Job | Must not do |
|---|---|---|
| Orchestrator | define source scope, assign roles, merge outputs, verify final answer | write final prose before receiving audits |
| Reviewer | identify Fatal/Major risks and likely objections | polish prose |
| Evidence Auditor | map claims to supplied evidence and TODOs | invent missing solver/data/metric details |
| Experiment Planner | propose minimum validation, baselines, diagnostics, ablations | claim experiments were run |
| Figure/Table Editor | design evidence-bearing figures/tables | accept decorative contours as proof |
| Prose Editor | rewrite into field-native manuscript text | hide missing evidence in smooth language |
| Gatekeeper | re-audit final draft and list residual blockers | rubber-stamp the editor |

## Workflow

### 1. Source-scope contract

Before spawning or simulating roles, write:

- supplied text and evidence;
- files each role may read;
- facts that must remain TODO;
- output expected from each role.

### 2. Parallel critique pass

Independent roles inspect the same draft from different angles:

- Reviewer: rejection risks;
- Evidence Auditor: claim-evidence map;
- Experiment Planner: rescue experiments and baselines;
- Figure/Table Editor: evidence-bearing visual/table plan.

### 3. Integration pass

Orchestrator merges disagreements into a single priority ledger:

1. Fatal blockers;
2. Major blockers;
3. wording edits that reduce risk;
4. experiments/tables/figures needed to support stronger claims.

### 4. Editorial pass

Prose Editor rewrites only after the integration ledger exists. The rewrite must:

- preserve supplied evidence;
- downgrade unsupported claims;
- add TODO placeholders for missing facts;
- follow physical problem -> gap -> method -> evidence -> limitation;
- avoid generic AI academic language.

### 5. Bounded edit-review loop

After the first editorial pass, Gatekeeper reviews the revised text. If residual blockers are fixable by wording, structure, claim calibration, or TODO placement, the orchestrator runs another edit-review cycle:

```text
prose_editor(cycle N revision + residual-risk table)
-> gatekeeper(original + ledger + previous revision + current revision)
```

Default limits:

- abstracts: maximum 2 edit-review cycles;
- longer sections/full drafts: maximum 3 edit-review cycles;
- never loop indefinitely.

Stop early when:

- no Fatal/Major blockers remain;
- no new overclaim was introduced by the editor;
- remaining blockers require new experiments/data/figures/tables rather than prose.

If the blocker requires evidence, the editor must downgrade the claim or insert a TODO. Do not polish around missing evidence.

### 6. Final gate

Gatekeeper compares old vs new text:

- risks removed;
- risks downgraded;
- risks remaining;
- new overclaims introduced by the editor;
- next actions required before submission.

## Codex native subagent mode

For users who want one Codex CLI session to spawn several internal agents, configure project-scoped agents under `.codex/agents/` and start Codex from the package root. This package includes agent definitions for:

- `managing_editor`
- `cfd_reviewer`
- `evidence_auditor`
- `experiment_planner`
- `figure_table_editor`
- `prose_editor`
- `gatekeeper`

Prompt pattern:

```text
Use native Codex subagents. Spawn cfd_reviewer, evidence_auditor, experiment_planner, and figure_table_editor in parallel on this draft. Wait for all. Merge their outputs. Then run prose_editor -> gatekeeper -> prose_editor -> gatekeeper as a bounded edit-review loop. Stop when no Fatal/Major blockers remain, remaining blockers need new evidence, or the max cycle count is reached.
```

Use `/agent` inside Codex CLI to inspect or switch between active agent threads.

## Actual multi-agent launch guidance

When using external Hermes/Codex/Claude workers rather than native Codex subagents, the orchestrator should:

- assign each worker a self-contained prompt with source scope and role boundaries;
- keep workers read-only unless they are explicitly writing a named artifact;
- require structured outputs, not free-form chat;
- verify worker claims by reading generated files and checking source scope;
- integrate outputs centrally instead of letting workers edit the same manuscript concurrently.

Suitable worker prompts:

- `Reviewer`: “Return Fatal/Major/Minor risks only; no rewrite.”
- `Evidence Auditor`: “Map each claim to supplied evidence or TODO; do not infer hidden details.”
- `Experiment Planner`: “Return minimum validation matrix and baselines that rescue claims.”
- `Figure Editor`: “Return figure/table sequence where each item supports one claim.”
- `Prose Editor`: “Rewrite only after reading the merged ledger; do not invent evidence.”
- `Gatekeeper`: “Audit the revised text against the original ledger and list residual blockers.”

## Output schema

Use `templates/multi-agent-paper-workflow-report.md` for full workflows.

Compressed form:

| Agent | Output | Key blocker/fix |
|---|---|---|
| Reviewer | | |
| Evidence Auditor | | |
| Experiment Planner | | |
| Figure/Table Editor | | |
| Prose Editor | | |
| Gatekeeper | | |

Then provide:

1. merged blocker ledger;
2. revised text;
3. edit-review cycle log;
4. residual-risk table;
5. stop reason;
6. next experiments/tables/figures.

## Anti-patterns

- Calling it multi-agent when one role simply writes everything.
- Letting the prose editor see no reviewer/evidence ledger.
- Allowing workers to invent missing experiments or paper facts.
- Giving every worker the answer key when the benchmark is supposed to test inference.
- Merging worker outputs without resolving contradictions.
- Treating worker self-reports as verified evidence.
- Parallel workers editing the same file without an orchestrator merge step.

## Verification

- Source scope is stated for every role.
- Each role returns a distinct artifact.
- The final rewrite traces to reviewer/evidence findings.
- Gatekeeper identifies residual risk rather than approving by default.
- Edit-review loops are bounded and include an explicit stop reason.
- The editor does not run another prose cycle when the remaining blocker requires new evidence rather than wording.
- No hidden solver, metric, citation, data, or runtime detail is invented.
- The workflow can be scored by `rubrics/multi-agent-paper-workflow-rubric.md`.
