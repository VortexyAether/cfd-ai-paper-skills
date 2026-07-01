# Quickstart: Claude Code and Claude-Like Agents

This package is portable because the skill instructions are plain files. Do not assume an official install command unless your Claude-like tool documents one.

## 1. Give the agent the package path

```text
You can read this package:
/path/to/cfd-ai-paper-skills

Use these files as instructions:
- skills/scientific-journal-writing/SKILL.md
- skills/sciml-experiment-auditor/SKILL.md
- skills/cfd-reproducibility-checker/SKILL.md
```

## 2. State the hard scientific rule

Use this line in most tasks:

```text
Unknown solver settings, dataset details, DOI values, benchmark numbers, author roles, and citation metadata must remain TODO. Do not invent them.
```

## 3. Choose a workflow

### Draft audit

```text
Follow skills/paper-claim-auditor/SKILL.md and skills/cfd-ml-paper-reviewer/SKILL.md.
Audit draft.md for unsupported CFD-AI claims. Return findings first, then a claim-evidence table, then concrete edits.
```

### Experiment plan

```text
Follow skills/experiment-design-for-sciml/SKILL.md and skills/sciml-experiment-auditor/SKILL.md.
Turn notes.md into an experiment matrix for a CFD surrogate paper. Include splits, baselines, diagnostics, ablations, UQ, runtime, and reproducibility TODOs.
```

### Related work

```text
Follow skills/related-work-cartographer/SKILL.md and skills/related-work-synthesis/SKILL.md.
Convert citations.md into a taxonomy organized by CFD workflow role, ML method family, validation axis, and evidence limitation.
```

### LaTeX production

```text
Follow skills/latex-paper-production/SKILL.md.
Create a complete standalone main.tex from evidence_packet.md. Use boxed figure placeholders and TODO bibliography entries. Do not use external image files.
```

## 4. Reuse the repository as a skill bundle

If your environment supports reusable local skills, copy or symlink the whole repository according to that environment's documented procedure. Keep the directory structure intact so skill files can load:

- `references/`
- `rubrics/`
- `examples/`
- `templates/`
- `evaluation/tasks/`

## 5. Review the output

Ask for reviewer-style outputs rather than polished prose only:

```text
Before final prose, show a table of claims, evidence, missing evidence, and reviewer risk. Then revise only the claims whose evidence is sufficient.
```
