# Codex native subagents for CFD-AI paper workflows

This project is ready for **one Codex CLI session** to spawn native Codex subagents internally.

## Start

From this package root:

```bash
codex
```

Then paste one of the prompt templates:

```text
.codex/prompts/smoke-test.md
.codex/prompts/iterative-edit-review-loop.md
.codex/prompts/multi-agent-abstract-rescue.md
.codex/prompts/full-paper-reviewer-editor.md
```

## Quick iterative prompt

```text
Use native Codex subagents and run a bounded edit-review loop.

Spawn cfd_reviewer, evidence_auditor, experiment_planner, and figure_table_editor in parallel on this abstract.
Wait for all.
Merge their outputs into a blocker ledger.
Run prose_editor -> gatekeeper -> prose_editor -> gatekeeper for max 2 cycles.
Stop early if no Fatal/Major blockers remain, no new overclaim appears, or remaining blockers require new evidence rather than wording.
Return final revised abstract, residual-risk table, stop reason, and next experiments/tables/figures.

<Abstract here>
```

## Agents

| Agent | Job |
|---|---|
| `managing_editor` | orchestrates source scope, merge ledger, and bounded edit-review loop |
| `cfd_reviewer` | Fatal/Major reviewer risks |
| `evidence_auditor` | claim-evidence map and TODOs |
| `experiment_planner` | validation/baseline/diagnostic rescue plan |
| `figure_table_editor` | evidence-bearing figures/tables |
| `prose_editor` | evidence-bounded rewrite after the blocker ledger exists; later cycles revise from gatekeeper residuals |
| `gatekeeper` | residual-risk re-audit after each edit; continue/stop decision |

## Loop policy

- Abstracts: max 2 edit-review cycles.
- Longer sections/full drafts: max 3 edit-review cycles.
- Stop early if no Fatal/Major blockers remain.
- Stop early if the editor introduced no new overclaim and remaining issues need experiments/data/figures/tables rather than prose.
- Never loop indefinitely.

## Codex controls

- Use `/agent` in Codex CLI to inspect or switch active agent threads.
- The local config sets:

```toml
[agents]
max_threads = 6
max_depth = 1
```

## Smoke-test evidence

A prior smoke test from this package root successfully spawned `cfd_reviewer` and `evidence_auditor` inside a single Codex run. The Codex log showed:

```text
collab: SpawnAgent
collab: SpawnAgent
collab: Wait
```

So this is native Codex subagents, not separate external Codex processes.
