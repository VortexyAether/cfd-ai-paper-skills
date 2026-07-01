# Simple abstract-review A/B benchmark

Run date: 2026-07-01

## Purpose

A minimal contamination-resistant benchmark: one flawed abstract, one reviewer critique task, markdown outputs only.

## Arms

| Arm | Scope | Output |
|---|---|---|
| `no_skill` | temporary directory outside package; prompt only; `--ignore-rules` | `no_skill_output.md` |
| `with_skill` | same abstract plus explicit package skills/rubrics/style guides | `with_skill_output.md` |

## Score summary

```text
no_skill average:   1.78 / 3.00
with_skill average: 3.00 / 3.00
```

## Main finding

No-skill catches the obvious hype but stays generic. With-skill asks for CFD-native evidence: geometry, BC/IC, mesh, CFL, architecture/loss, leakage-safe Reynolds splits, physical diagnostics, drag/lift/pressure drop, hardware/latency/memory, and task-limited solver-replacement boundaries.

See `comparison_report.md`.
