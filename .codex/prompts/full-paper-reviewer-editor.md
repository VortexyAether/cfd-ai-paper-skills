# Codex native multi-agent full-paper prompt

Use this for a longer manuscript section or full draft. Paste into one Codex CLI session from the package root.

```text
Use native Codex subagents for a CFD-AI/SciML manuscript workflow and run a bounded edit-review loop.

Source-scope rules:
- Use only the manuscript text and files I explicitly provide.
- Separate supplied evidence from inferred risks.
- Do not invent solver, mesh, timestep, metric, citation, runtime, code, or dataset details.
- Mark missing facts as TODO.

Parallel pass:
- Spawn `cfd_reviewer`: Fatal/Major reviewer risks only.
- Spawn `evidence_auditor`: claim-evidence map and TODOs.
- Spawn `experiment_planner`: minimum validation/baseline/diagnostic/ablation plan.
- Spawn `figure_table_editor`: figures/tables needed to make claims inspectable.
- Wait for all agents.

Integration pass:
- Merge outputs into one blocker ledger.
- Prioritize Fatal blockers, then Major blockers, then wording fixes.
- Resolve contradictions between agents explicitly.

Bounded edit-review loop:
- Maximum cycles: 3.
- Cycle 1: send the merged ledger to `prose_editor`; ask it to rewrite only the requested section, preserving evidence boundaries.
- Review 1: send original text + merged ledger + revised text to `gatekeeper`; ask for residual blockers, new overclaims, and continue/stop decision.
- If gatekeeper says continue, send residual-risk table + current revision back to `prose_editor` for Cycle 2.
- Run `gatekeeper` after every edit.
- Stop early when no Fatal/Major blockers remain and no new overclaim is introduced.
- Stop early when remaining blockers require new experiments/data/figures/tables rather than prose.

Return:
1. source-scope contract;
2. per-agent summaries;
3. merged blocker ledger;
4. edit-review cycle log;
5. final revised section;
6. gatekeeper residual-risk table;
7. stop reason;
8. prioritized next experiments/tables/figures.

Manuscript / section:

<PASTE TEXT HERE>
```
