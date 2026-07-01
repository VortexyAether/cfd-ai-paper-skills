# Codex native iterative edit-review loop prompt

Copy this into one Codex CLI session started from the package root.

```text
Use native Codex subagents and run a bounded edit-review loop.

Source-scope rules:
- Use only the draft and any files I explicitly mention.
- Do not invent solver, grid, timestep, metric, dataset, citation, architecture, runtime, or code details.
- Hidden facts must stay TODO.
- If a claim needs new data/experiment/figure/table, stop polishing and mark the needed artifact.

Initial critique pass:
1. Spawn `cfd_reviewer`, `evidence_auditor`, `experiment_planner`, and `figure_table_editor` in parallel on the draft.
2. Wait for all four agents.
3. Merge their outputs into a blocker ledger: Fatal blockers, Major blockers, safer wording, and rescue artifacts.

Edit-review loop:
- Maximum cycles: 2 for abstracts, 3 for longer sections.
- Cycle 1: send the blocker ledger + draft to `prose_editor`; get revised text.
- Review 1: send original draft + blocker ledger + revised text to `gatekeeper`; get residual-risk table and continue/stop decision.
- If gatekeeper says continue and max cycles is not reached, send residual-risk table + current revision back to `prose_editor` for the next edit.
- After each edit, run `gatekeeper` again.
- Stop early if no Fatal/Major blockers remain and no new overclaim is introduced.
- Stop early if remaining blockers require new evidence rather than wording.

Return the final report with:
1. source-scope contract;
2. initial agent outputs summary;
3. merged blocker ledger;
4. edit-review cycle log;
5. final revised text;
6. final gatekeeper residual-risk table;
7. stop reason;
8. next experiments/tables/figures.

Draft:

<PASTE DRAFT HERE>
```
