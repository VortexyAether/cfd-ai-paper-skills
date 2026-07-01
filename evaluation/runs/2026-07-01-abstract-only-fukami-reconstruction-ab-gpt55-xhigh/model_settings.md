# Abstract-only Fukami reconstruction A/B benchmark

| Field | Value |
|---|---|
| Model | `gpt-5.5` |
| Reasoning effort | `xhigh` |
| Runner | `codex exec` |
| Run date | 2026-07-01 |
| Task type | title+abstract-only paper-content reconstruction |
| Target | Fukami et al., *Super-resolution reconstruction of turbulent flows with machine learning* |

## Contamination controls

| Arm | Working directory | Source scope |
|---|---|---|
| `no_skill` | temporary directory outside the package | only title+abstract prompt; `--ignore-rules`; no package terms |
| `with_skill` | package root | same title+abstract plus general skills/rubrics/style guides; explicit ban on opening the exact `fukami-2019` answer-key note or prior run outputs |
| evaluator | package root after generation | uses `references/gold-papers/fukami-2019-super-resolution-jfm.md` as answer key |
