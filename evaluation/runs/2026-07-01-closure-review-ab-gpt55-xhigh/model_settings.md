# Model settings

| Field | Value |
|---|---|
| Model | `gpt-5.5` |
| Reasoning effort | `xhigh` |
| Runner | `codex exec` |
| Run date | 2026-07-01 |
| Benchmark | no-skill vs with-skill closure review manuscript seed |
| Task | `evaluation/tasks/cfd-ai-closure-review-benchmark.md` |
| Run directory | `evaluation/runs/2026-07-01-closure-review-ab-gpt55-xhigh/` |

## Arm definitions

| Arm | Source scope | Package guidance |
|---|---|---|
| no_skill | Benchmark task packet only, copied to `no_skill/task.md` | Not used; Codex run used `--ignore-rules` from isolated run directory |
| with_skill | Same task packet plus listed package skills/rubrics/gold notes | Used explicitly |
