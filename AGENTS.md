# AGENTS.md — CFD-AI Paper Skills Package

Agent-facing instructions for maintaining this package.

## Goal

Build and evaluate a Hermes/Codex-compatible skill package for CFD-AI and scientific ML journal paper writing, reviewing, reproducibility auditing, experiment design, related-work positioning, LaTeX production, and revision management.

## Ground truth

Gold-standard authors:

- Kai Fukami
- Steven L. Brunton
- Romit Maulik
- Sangseung Lee
- Ricardo Vinuesa

Do not treat these names as decorative citations. Extract writing, experiment, figure, and reviewer-defense patterns from their papers.

## Rules

1. One skill = one focused job.
2. Every `SKILL.md` starts at byte 0 with YAML frontmatter and includes `name` and `description`.
3. Descriptions must be trigger-oriented.
4. Every skill needs output schema, anti-patterns, and verification checklist.
5. Unknown facts must be marked as unknown/TODO; do not invent solver details, citations, DOI, or corresponding-author status.
6. Claim-evidence alignment outranks prose polishing.
7. Evaluation artifacts go under `evaluation/runs/`.
8. Skill improvements must be justified by benchmark/eval failures, not taste.

## Validation

Run from package root:

```bash
python3 - <<'PY'
from pathlib import Path
import json, re
root=Path('.')
for p in sorted(root.glob('skills/*/SKILL.md')):
    txt=p.read_text()
    assert txt.startswith('---\n'), p
    fm=txt.split('---',2)[1]
    assert 'name:' in fm and 'description:' in fm, p
json.loads((root/'evaluation/evals.json').read_text())
print('ok')
PY
```

## Preferred output style

Concise, evidence-grounded, table/checklist-heavy in files. No marketing language.
