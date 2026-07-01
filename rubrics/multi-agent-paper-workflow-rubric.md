# Multi-Agent Paper Workflow Rubric

Use this rubric to score reviewer-driven multi-agent manuscript workflows.

Score each axis 0--3.

| Score | Meaning |
|---:|---|
| 0 | Missing or unsafe. |
| 1 | Nominal role labels but generic output. |
| 2 | Useful role separation with some integration. |
| 3 | Real role separation, source-scoped outputs, verified merge, and final re-audit. |

## Axes

### 1. Role separation

- 0: one writer does everything.
- 1: role names appear but outputs overlap.
- 2: roles produce distinct critique/edit artifacts.
- 3: each role has source scope, artifact, and forbidden actions.

### 2. Source-scope discipline

- 0: workers invent missing facts.
- 1: source scope is vague.
- 2: most facts are scoped or TODO.
- 3: every role states supplied/allowed/forbidden information.

### 3. Reviewer severity

- 0: no rejection-risk gate.
- 1: generic comments.
- 2: Fatal/Major labels.
- 3: Fatal/Major labels tied to claims and required rescue artifacts.

### 4. Evidence audit completeness

- 0: no claim-evidence map.
- 1: obvious claims only.
- 2: major claims mapped.
- 3: claims mapped by type with evidence, TODO, and safe wording.

### 5. Experiment and figure rescue plan

- 0: no rescue plan.
- 1: vague “add validation.”
- 2: concrete experiments or figures.
- 3: each high-risk claim has a validation/table/figure that would rescue it.

### 6. Editorial rewrite quality

- 0: no rewrite.
- 1: grammar polish only.
- 2: overclaims mostly narrowed.
- 3: physical problem -> gap -> method -> evidence -> limitation, with no invented details.

### 7. Integration quality

- 0: role outputs are pasted together.
- 1: weak summary.
- 2: merged blocker ledger.
- 3: contradictions resolved and priorities assigned by risk.

### 8. Gatekeeper and loop control

- 0: no re-audit.
- 1: says “better.”
- 2: before/after risk table.
- 3: residual blockers, new overclaims, continue/stop decision, cycle limit, and next actions are explicit.

### 9. Bounded edit-review loop

- 0: no loop or unbounded loop.
- 1: loop named but not executed or no stop rule.
- 2: at least one edit-review cycle with residual-risk-driven revision.
- 3: bounded prose_editor -> gatekeeper loop with explicit stop reason and no polishing around evidence-required blockers.

## Pass gate

A multi-agent paper workflow passes only if:

- no role invents hidden scientific details;
- the editor sees the merged blocker ledger before rewriting;
- edit-review cycles are bounded and driven by gatekeeper residual blockers, not taste;
- final text is safer and still meaningful;
- the gatekeeper identifies residual risk rather than rubber-stamping the edit.
