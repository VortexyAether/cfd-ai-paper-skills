# Task: Multi-agent reviewer-editor workflow

## Skill under test

- `multi-agent-paper-orchestrator`
- `paper-revision-loop-manager`
- `reviewer-audit-toolkit`
- `scientific-journal-writing`
- `figure-and-result-storytelling`
- `sciml-experiment-auditor`

## Prompt

Given only the draft abstract below, run a multi-agent reviewer-editor workflow with a bounded edit-review loop. You may simulate the agents in one answer, but roles must remain separated. Run at most two prose_editor -> gatekeeper cycles for this abstract.

Draft abstract:

> We introduce a novel AI framework that predicts turbulent wake dynamics with state-of-the-art accuracy. The model is robust across Reynolds numbers and geometries, physically consistent, and faster than CFD. These results reveal hidden flow physics and enable engineering design.

Required agents:

1. Reviewer;
2. Evidence Auditor;
3. Experiment Planner;
4. Figure/Table Editor;
5. Prose Editor;
6. Gatekeeper.

Required final output:

- source-scope contract;
- one structured output from each agent;
- orchestrator merge ledger;
- edit-review cycle log;
- revised abstract;
- final gatekeeper re-audit with continue/stop decision;
- stop reason;
- next experiments/tables/figures.

Do not invent solver, data, metric, architecture, citation, runtime, or benchmark details.

## Expected answer-key patterns

- Reviewer must reject/bound: novel, state-of-the-art, robust, generalizes across Re/geometries, physically consistent, faster than CFD, hidden physics, engineering design.
- Evidence Auditor must map claims to missing evidence or TODO, not fill facts.
- Experiment Planner must propose validation split axes, baselines, metrics, physical diagnostics, runtime evidence, and ablations.
- Figure/Table Editor must propose GT/pred/error, validation matrix, physical diagnostic, baseline metric, and runtime table.
- Prose Editor must produce a cautious abstract beginning from wake-flow prediction or fast estimates, not AI capability.
- Gatekeeper must list residual blockers and next actions instead of rubber-stamping.
- The loop must stop rather than keep polishing if remaining blockers require new evidence, experiments, tables, or figures.
