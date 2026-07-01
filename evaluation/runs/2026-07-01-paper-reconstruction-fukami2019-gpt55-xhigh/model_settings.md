# Model settings

| Field | Value |
|---|---|
| Model | `gpt-5.5` |
| Reasoning effort | `xhigh` |
| Execution surface | Codex exec |
| Run date | 2026-07-01 |
| Working directory | package root |
| Benchmark | no-skill vs with-skill paper reconstruction |
| Target task | `evaluation/tasks/fukami-super-resolution-reconstruction.md` |
| Target run directory | `evaluation/runs/2026-07-01-paper-reconstruction-fukami2019-gpt55-xhigh/` |

## Arm definitions

| Arm | Source scope | Package guidance |
|---|---|---|
| no_skill | Task prompt and dense source summary | Not used for generation |
| with_skill | Task prompt, dense source summary, relevant gold-paper note, and listed package guidance | Used explicitly |

## With-skill guidance used

- `skills/scientific-journal-writing/SKILL.md`
- `skills/paper-claim-auditor/SKILL.md`
- `skills/cfd-reproducibility-checker/SKILL.md`
- `rubrics/claim-evidence-rubric.md`
- `rubrics/cfd-reproducibility-rubric.md`
- `rubrics/vocabulary-style-rubric.md`
- `references/gold-papers/fukami-2019-super-resolution-jfm.md`
- `references/field-terminology-style-guide.md`

## Compiler setting

Tectonic was the only available LaTeX compiler. Direct default-bundle compilation failed with a runtime panic in Tectonic's network client. Compilation succeeded after building a local Tectonic bundle from the existing cache and redirecting `TECTONIC_CACHE_DIR` to a temporary writable cache directory.
