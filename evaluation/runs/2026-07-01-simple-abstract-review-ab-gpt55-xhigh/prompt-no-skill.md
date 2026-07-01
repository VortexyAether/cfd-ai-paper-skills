# No-skill arm prompt

You are reviewing a CFD/AI paper abstract. Do not use any external files, tools, rubrics, or package guidance. Use only the abstract below.

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
