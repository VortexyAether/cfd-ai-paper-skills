---
name: latex-paper-production
description: Use when writing, editing, compiling, or debugging LaTeX scientific manuscripts, journal templates, equations, figures, tables, captions, and BibTeX.
version: 0.3.0
author: VA + TARS
metadata:
  short-description: Produce and debug LaTeX CFD-AI/SciML manuscripts
---

# LaTeX Paper Production

## Trigger

Use for LaTeX manuscript drafting, journal templates, equations, figures, tables, BibTeX, Overleaf/local compile issues, and final PDF checks.

## Workflow

1. Inspect project structure: `main.tex`, `sections/`, `figures/`, `tables/`, `refs.bib`, `.cls`, `.sty`.
2. Identify document class and citation system before editing.
3. Preserve template conventions.
4. Make minimal targeted edits.
5. Compile and inspect first fatal error if build fails.

## Citation systems

Do not mix:

- `natbib`: `\citep`, `\citet`
- plain BibTeX: `\cite`
- `biblatex`: `\parencite`, `\textcite`
- IEEE: numerical style

## Equations

Rules:

- Define symbols near first use.
- Keep notation consistent.
- Use `equation` for key equations and `align` for derivations.
- Label important equations: `eq:pde-loss`, `eq:total-loss`.

## Figures

Use journal-safe files: PDF/SVG/EPS/PNG depending on template.

Figure block:

```latex
\begin{figure}[t]
\centering
\includegraphics[width=0.95\linewidth]{figures/main_result.pdf}
\caption{Prediction and error fields for the unseen test case at $Re=1000$. The proposed model reduces high-frequency error near shear layers compared with the baseline.}
\label{fig:main-result}
\end{figure}
```

## Tables

Prefer `booktabs` if available. Avoid vertical rules unless template requires them.

## Compile verification

Run:

```bash
latexmk -pdf -interaction=nonstopmode main.tex
```

If Unicode/Korean appears:

```bash
latexmk -xelatex -interaction=nonstopmode main.tex
```

## Debugging order

First fatal error first:

- undefined control sequence,
- missing brace,
- missing package,
- duplicate label,
- undefined citation,
- figure path typo,
- special chars `_ % & #`,
- Unicode with pdfLaTeX.

## Output template

1. Detected template/citation system
2. Files changed or proposed patch
3. Compile command
4. Compile result / first blocker
5. Remaining unresolved refs/citations

## Anti-patterns

- Editing generated LaTeX artifacts instead of source files.
- Hiding BibTeX or compilation errors under cosmetic formatting changes.
- Reflowing equations without checking labels, references, and units.
- Introducing manual citation text instead of bibliography entries.

## Verification

- PDF compiles or blocker is explicit.
- No unresolved `??` where possible.
- Citations match project system.
- Figures/tables are referenced.
