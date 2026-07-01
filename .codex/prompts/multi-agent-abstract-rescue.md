# Codex native multi-agent abstract rescue prompt

Copy this into one Codex CLI session started from the package root.

```text
Use native Codex subagents and run a bounded edit-review loop.

Source-scope rules:
- Use only the draft abstract and any files I explicitly mention.
- Do not invent solver, grid, timestep, metric, dataset, citation, architecture, runtime, or code details.
- Hidden facts must stay TODO.

Workflow:
1. Spawn `cfd_reviewer`, `evidence_auditor`, `experiment_planner`, and `figure_table_editor` in parallel on the draft abstract.
2. Wait for all four agents.
3. Merge their outputs into a blocker ledger: Fatal blockers, Major blockers, safer wording, and rescue artifacts.
4. Run an edit-review loop for max 2 cycles:
   - Cycle 1: send draft abstract + blocker ledger to `prose_editor` and ask it to rewrite.
   - Review 1: send original draft + blocker ledger + revised abstract to `gatekeeper` and ask for residual-risk table plus continue/stop decision.
   - If gatekeeper says continue, send current revision + residual-risk table back to `prose_editor`.
   - Review again with `gatekeeper`.
5. Stop early if no Fatal/Major blockers remain, no new overclaim is introduced, or remaining blockers require new evidence rather than wording.
6. Return the final report with these sections:
   - source-scope contract
   - agent outputs summary
   - orchestrator merge ledger
   - edit-review cycle log
   - final revised abstract
   - gatekeeper residual-risk table
   - stop reason
   - next experiments/tables/figures

Draft abstract:

<PASTE ABSTRACT HERE>
```
