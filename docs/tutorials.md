# Tutorials

These tutorials are practical task patterns for using the package with any agent that can read local files.

## Tutorial 1: Claim-Evidence Audit

Use when you have an abstract, introduction, or full draft.

Prompt:

```text
Use skills/paper-claim-auditor/SKILL.md.
Audit draft.md for claim-evidence alignment.

Return a table with:
- claim;
- evidence supplied;
- missing evidence;
- risk level;
- safer wording;
- location in draft.

Do not invent solver settings, citations, DOI values, or benchmark numbers.
```

Expected output:

- findings first;
- a claim-evidence table;
- TODOs for missing facts;
- concrete safer rewrites.

## Tutorial 2: CFD Reproducibility Review

Use when you have methods notes, experiments, or a paper draft.

Prompt:

```text
Use skills/cfd-reproducibility-checker/SKILL.md and skills/sciml-experiment-auditor/SKILL.md.
Review methods.md and results.md for numerical reproducibility.

Check:
- governing equations and nondimensional groups;
- solver, mesh, BC/IC, time step, convergence;
- train/test split and held-out axes;
- baselines and ablations;
- physical diagnostics;
- uncertainty/calibration;
- hardware/runtime;
- code/data availability.
```

Expected output:

- reproducibility checklist;
- high-risk missing items;
- experiment matrix;
- reviewer-facing TODOs.

## Tutorial 3: Related-Work Taxonomy

Use when you have a citation dump or broad topic.

Prompt:

```text
Use skills/related-work-cartographer/SKILL.md and skills/related-work-synthesis/SKILL.md.
Turn citations.md into a CFD-AI related-work taxonomy.

Organize by:
1. CFD workflow role;
2. ML method family;
3. validation axis;
4. limitation or reviewer risk.

Do not write a chronological citation list.
```

Expected output:

- taxonomy table;
- gap/positioning paragraph;
- claim boundaries;
- citation TODOs where metadata is missing.

## Tutorial 4: LaTeX Review-Paper Seed

Use when you have an evidence packet and want a standalone draft seed.

Prompt:

```text
Use skills/scientific-journal-writing/SKILL.md, skills/figure-and-result-storytelling/SKILL.md, and skills/latex-paper-production/SKILL.md.
Create a complete standalone LaTeX mini-review from evidence_packet.md.

Include:
- title and abstract;
- workflow-first taxonomy;
- validation and reproducibility sections;
- at least two tables;
- boxed figure placeholders with claim-support captions;
- reviewer traps with safer rewrites;
- research agenda;
- TODO bibliography entries.
```

Expected output:

- compilable `main.tex` source when possible;
- no external figures unless supplied;
- no invented benchmark numbers;
- TODOs for missing bibliography.

## Tutorial 5: Response To Reviewers

Use when reviews arrive.

Prompt:

```text
Use skills/paper-revision-loop-manager/SKILL.md and skills/response-to-reviewers/SKILL.md.
Build a response plan from reviews.md and the current manuscript.

For each reviewer point, return:
- issue summary;
- evidence needed;
- manuscript change;
- response text draft;
- risk if not addressed;
- TODOs.
```

Expected output:

- response table;
- revision checklist;
- places where new analysis or text is required;
- no invented new experiments.
