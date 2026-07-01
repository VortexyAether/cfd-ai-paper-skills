# With-skill arm prompt

You are reviewing the same CFD/AI paper abstract. Before answering, use the package guidance listed below, then return the same output shape as the no-skill arm.

Read and apply:
- `SKILL.md`
- `skills/paper-claim-auditor/SKILL.md`
- `skills/cfd-ml-paper-reviewer/SKILL.md`
- `skills/scientific-journal-writing/SKILL.md`
- `references/field-terminology-style-guide.md`
- `references/gold-paper-style-patterns.md`
- `rubrics/claim-evidence-rubric.md`
- `rubrics/vocabulary-style-rubric.md`
- `rubrics/gold-paper-closeness-rubric.md`
- `examples/generic-ai-to-gold-paper-prose.md`

Task: Return a concise reviewer-style critique with exactly these sections:

1. Verdict: accept / weak / reject
2. Five most serious issues
3. Required evidence to make the claims credible
4. One safer rewritten abstract

Abstract to review:

> We propose a novel AI framework that robustly predicts turbulent flows with state-of-the-art accuracy. Our physics-informed neural network generalizes to arbitrary Reynolds numbers and provides physically consistent results in real time. We trained on simulation data and demonstrate the effectiveness of the method using velocity contour plots. These results show that the model can replace expensive CFD solvers for engineering design. Future work will improve scalability and robustness.

Constraints:
- Do not invent solver settings, data sizes, equations, metrics, or citations.
- If evidence is missing, say exactly what evidence is needed.
- Keep the answer under 700 words.
