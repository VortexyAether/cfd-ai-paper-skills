# With-skill arm prompt

You are given the same paper title and abstract. Infer what the full paper probably contains. Use general CFD-AI paper-skill guidance, but do **not** read the exact answer-key/gold note for this paper: do not open any file matching `references/gold-papers/fukami-2019-*` and do not read prior benchmark run outputs for this paper.

Read and apply only general guidance:
- `SKILL.md`
- `skills/figure-and-result-storytelling/SKILL.md`
- `skills/experiment-design-for-sciml/SKILL.md`
- `skills/sciml-experiment-auditor/SKILL.md`
- `skills/paper-claim-auditor/SKILL.md`
- `skills/scientific-journal-writing/SKILL.md`
- `references/field-terminology-style-guide.md`
- `references/gold-paper-style-patterns.md`
- `rubrics/figure-evidence-rubric.md`
- `rubrics/sciml-experiment-rubric.md`
- `rubrics/claim-evidence-rubric.md`

Title: Super-resolution reconstruction of turbulent flows with machine learning

Abstract:

> We use machine learning to perform super-resolution analysis of grossly under-resolved turbulent flow field data to reconstruct the high-resolution flow field. Two machine-learning models are developed; namely the convolutional neural network (CNN) and the hybrid Downsampled Skip-Connection Multi-Scale (DSC/MS) models. These machine-learning models are applied to two-dimensional cylinder wake as a preliminary test and show remarkable ability to reconstruct laminar flow from low-resolution flow field data. We further assess the performance of these models for two-dimensional homogeneous turbulence. The CNN and DSC/MS models are found to reconstruct turbulent flows from extremely coarse flow field images with remarkable accuracy. For the turbulent flow problem, the machine-learning based super-resolution analysis can greatly enhance the spatial resolution with as little as 50 training snapshot data, holding great potential to reveal subgrid-scale physics of complex turbulent flows. With the growing availability of flow field data from high-fidelity simulations and experiments, the present approach motivates the development of effective super-resolution models for a variety of fluid flows.

Return exactly these sections:

1. Likely paper thesis
2. Likely method details
3. Likely experiments and baselines
4. Likely figure sequence
5. Likely reviewer attack points
6. What must remain unknown from abstract alone

Constraints:
- Do not invent exact solver, grid, timestep, architecture layer counts, metrics values, figure numbers, citations, DOI, or code links.
- Use confidence labels: confirmed from abstract / likely / speculative / unknown.
- Keep under 900 words.
