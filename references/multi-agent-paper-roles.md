# Multi-Agent Paper Role Cards

Use these role cards for CFD-AI/SciML manuscript improvement. They can be simulated in one session or assigned to actual workers.

## Shared rules for all roles

- Work only from supplied evidence and allowed files.
- Mark hidden facts as TODO; do not infer solver settings, grid, timestep, metrics, DOI, code links, author roles, or benchmark numbers.
- Use CFD/SciML-native evidence expectations, not generic academic advice.
- Keep claim-evidence alignment above prose polish.
- Produce structured output that the orchestrator can merge.

## Role 1 — Orchestrator / Managing Editor

Mission:

- define source scope;
- assign workers;
- merge role outputs;
- decide which claims survive;
- produce final report.

Output:

| Item | Content |
|---|---|
| Source scope | supplied / allowed / forbidden |
| Role assignments | worker, files, expected output |
| Merge decision | keep, narrow, remove, TODO |
| Final artifacts | revised text, risk ledger, next actions |

Failure mode: writes final prose before reviewer/evidence pass.

## Role 2 — Reviewer

Mission:

- identify likely rejection risks;
- label Fatal/Major/Minor;
- state likely reviewer objection.

Output:

| Severity | Issue | Reviewer objection | Required fix |
|---|---|---|---|

Failure mode: polite summary with no gate decision.

## Role 3 — Evidence Auditor

Mission:

- extract claims;
- map each claim to supplied evidence;
- mark missing evidence and unsafe wording.

Output:

| Claim | Type | Supplied evidence | Missing/TODO | Safe status |
|---|---|---|---|---|

Failure mode: fills missing facts because the claim sounds plausible.

## Role 4 — Experiment Planner

Mission:

- design minimum validation needed to rescue claims;
- name baselines, split axes, diagnostics, ablations, and runtime/UQ checks.

Output:

| Claim rescued | Experiment / validation | Baseline | Metric / diagnostic | Failure mode tested |
|---|---|---|---|---|

Failure mode: says “add more experiments” without exact validation axis.

## Role 5 — Figure/Table Editor

Mission:

- convert evidence requirements into figures and tables;
- ensure every major claim has an inspectable artifact.

Output:

| Figure/table | Claim supported | Required panels/columns | Caption claim | Missing data |
|---|---|---|---|---|

Failure mode: accepts pretty flow contours without error maps or diagnostics.

## Role 6 — Prose Editor

Mission:

- rewrite the manuscript after reading the merged ledger;
- make the text field-native and cautious;
- preserve value without unsupported hype.

Output:

- one-sentence paper claim;
- revised abstract/section;
- claims removed or downgraded;
- TODO placeholders for missing evidence.

Failure mode: hides missing evidence behind smoother prose.

## Role 7 — Gatekeeper / Meta-Reviewer

Mission:

- re-audit the revised text;
- compare before/after risk;
- catch new overclaims;
- decide whether the draft is safer, not merely prettier.

Output:

| Original risk | After edit | Residual blocker | Next action |
|---|---|---|---|

Failure mode: approves because the prose sounds better.

## Recommended role bundles

### Short abstract rescue

- Reviewer
- Evidence Auditor
- Prose Editor
- Gatekeeper

### Full paper revision

- Reviewer
- Evidence Auditor
- Experiment Planner
- Figure/Table Editor
- Prose Editor
- Gatekeeper

### Results section rewrite

- Evidence Auditor
- Experiment Planner
- Figure/Table Editor
- Prose Editor
- Gatekeeper

### Submission-readiness pass

- Reviewer
- Reproducibility Auditor
- Gatekeeper
