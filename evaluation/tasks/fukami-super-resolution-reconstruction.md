# Task: Fukami super-resolution reconstruction

## Skill under test

- `scientific-journal-writing`
- `figure-and-result-storytelling`
- `experiment-design-for-sciml`

## Gold reference

Kai Fukami et al., *Super-resolution reconstruction of turbulent flows with machine learning*, arXiv:1811.11328.

## Baseline-agent prompt

Given only the title and abstract of the paper, reconstruct:

1. the physical problem,
2. the ML task transformation,
3. the likely evidence stack,
4. the likely figure sequence,
5. reviewer attack points,
6. experiments a new paper in this line must include.

Do not invent solver details; mark unknowns.

## Expected answer-key patterns

- Low-resolution → high-resolution turbulent field reconstruction.
- Must include qualitative field comparison and quantitative reconstruction error.
- Should discuss generalization limits and data requirements.
- Should not treat this as generic image super-resolution; fluid physics and turbulence structures matter.
