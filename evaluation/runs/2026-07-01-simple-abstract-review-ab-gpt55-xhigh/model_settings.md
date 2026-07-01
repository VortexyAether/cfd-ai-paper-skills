# Simple abstract-review A/B benchmark

| Field | Value |
|---|---|
| Model | `gpt-5.5` |
| Reasoning effort | `xhigh` |
| Runner | `codex exec` |
| Run date | 2026-07-01 |
| Task type | single flawed abstract review |

## Contamination controls

| Arm | Working directory | Source scope |
|---|---|---|
| `no_skill` | temporary directory outside the package | only `prompt-no-skill.md`; `--ignore-rules`; no package files named |
| `with_skill` | package root | same abstract plus explicitly listed package skills/rubrics/examples |

The no-skill prompt intentionally did not mention Fukami/Brunton/Maulik/Lee/Vinuesa, package rubrics, gold-paper notes, or field-style guides.
