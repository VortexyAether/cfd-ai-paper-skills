# Paper reconstruction benchmark: Fukami 2019, gpt-5.5 xhigh

Run date: 2026-07-01

Model setting: `gpt-5.5`, `xhigh reasoning`, Codex exec.

## Purpose

Rerun the no-skill vs with-skill paper reconstruction benchmark with a stronger model/reasoning setting to test whether the CFD-AI skill package still improves source-bounded manuscript reconstruction.

## Task and Sources

Target task:

- `evaluation/tasks/fukami-super-resolution-reconstruction.md`

Target paper:

- Fukami, Fukagata, and Taira, *Super-resolution reconstruction of turbulent flows with machine learning*, Journal of Fluid Mechanics, 2019.

Source scope:

- benchmark task prompt;
- dense source summary from the previous run;
- for the with-skill arm, local package guidance and the Fukami 2019 gold-paper note.

Unknown details remain TODO/unknown. No exact solver settings, numerical errors, architecture layer counts, split seeds, or PDF-level figure captions were invented.

## Outputs

| Arm | TeX | PDF |
|---|---|---|
| no_skill | `no_skill/main.tex` | `no_skill/main.pdf` |
| with_skill | `with_skill/main.tex` | `with_skill/main.pdf` |

Other reports:

- `model_settings.md`
- `comparison_report.md`

## Compilation

Direct `tectonic main.tex` failed in this sandbox because Tectonic panicked while initializing its default network bundle client. A local Tectonic bundle was built from the existing cache and compilation succeeded with:

```bash
TECTONIC_CACHE_DIR=<temporary-cache> tectonic --bundle <local-cache-bundle.ttb> --only-cached --keep-logs main.tex
```

To fit the cached bundle, optional LaTeX dependencies were removed from the manuscripts: `array`, `hyperref`, `\texttt`, `\url`, and italic emphasis. This did not change the scientific content.
