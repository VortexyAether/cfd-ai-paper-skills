# Simulated baseline-agent run: Fukami super-resolution reconstruction

Label: simulated baseline-agent run. No external model was spawned.

## Task

Use the package skills to reconstruct the evidence stack for:

- Kai Fukami, Koji Fukagata, Kunihiko Taira, "Machine-learning-based spatio-temporal super resolution reconstruction of turbulent flows"
- Source allowed to baseline agent: title, abstract-level summary, and `references/gold-papers/fukami-2021-spatiotemporal-super-resolution-jfm.md`
- Benchmark task skills under test: `scientific-journal-writing`, `figure-and-result-storytelling`, `experiment-design-for-sciml`

## Prompt

Given the title and abstract-level source, reconstruct:

1. physical problem,
2. ML task transformation,
3. minimum experiment/evidence stack,
4. likely figure sequence,
5. reviewer attack points,
6. unknowns/TODOs.

Do not invent solver details.
