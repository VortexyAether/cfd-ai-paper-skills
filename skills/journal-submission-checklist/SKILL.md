---
name: journal-submission-checklist
description: Use before submitting a CFD-AI/SciML journal manuscript to check formatting, files, declarations, figures, references, cover letter, and reviewer-risk items.
version: 0.3.0
author: CFD-AI Paper Skills maintainers
metadata:
  short-description: Preflight checklist for CFD-AI/SciML journal submission
---

# Journal Submission Checklist

## Trigger

Use before submission or resubmission to JFM, Physics of Fluids, JCP, CMAME, EAAI, Scientific Reports/Nature-style journals, or semiconductor/process journals.

## Workflow

### 1. Journal requirements

Check:

- template,
- word/page limits,
- abstract limit,
- figure/table limits,
- reference style,
- supplementary rules,
- data/code availability,
- conflict of interest,
- author contribution,
- funding,
- highlights/graphical abstract if required.

### 2. Manuscript completeness

Check title, abstract, keywords, introduction, related work, methods, results, discussion, conclusion, acknowledgements, data/code availability, conflicts, references, appendices.

### 3. Scientific defensibility

Before submission:

- claims have evidence,
- baselines are fair,
- limitations stated,
- equations/BC/IC/solver details present,
- figures readable,
- no unsupported SOTA/generalization/robustness,
- no hidden train/test leakage.

### 4. Figure/table preflight

For every figure:

- referenced in text,
- caption has takeaway,
- labels readable,
- units/colorbar present,
- same scale for comparison,
- high-resolution source exists.

For every table:

- metrics defined,
- units specified,
- uncertainty where relevant,
- best values marked only if allowed.

### 5. References

- all citations resolve,
- no uncited references,
- no duplicate BibTeX,
- DOI/arXiv where possible,
- recent/close prior art covered honestly.

### 6. Cover letter

Include:

- manuscript title,
- target journal,
- significance paragraph,
- journal fit,
- originality/no simultaneous submission,
- suggested reviewers if requested.

Avoid hype.

## Output template

1. Readiness: ready / not ready
2. Blocking issues
3. Major reviewer risks
4. Minor fixes
5. Missing files/statements
6. Final action list

## Anti-patterns

- Treating journal submission as formatting only while claims remain unsupported.
- Leaving placeholder code/data URLs or missing supplementary files.
- Ignoring required disclosure statements for LLM use, conflicts, or data access.
- Submitting figures with inconsistent scales, missing units, or unresolved TODOs.

## Verification

- PDF compiles.
- No `??` references.
- Required statements present.
- Submission files listed.
