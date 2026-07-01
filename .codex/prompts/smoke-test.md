# Codex native subagent smoke test

Paste this into Codex from the package root to check that project agents load.

```text
Use native Codex subagents `cfd_reviewer` and `evidence_auditor` in parallel on this draft. Wait for both. Return only:
- agents_used
- one reviewer finding
- one evidence-audit finding

Draft:
We propose a robust AI model that replaces CFD for turbulent wake design using velocity contour plots.
```

Expected signs in Codex activity/logs:

```text
SpawnAgent
SpawnAgent
Wait
```
