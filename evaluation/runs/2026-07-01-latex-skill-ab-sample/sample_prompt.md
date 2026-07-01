# CFD-AI LaTeX A/B sample prompt

Write a short LaTeX mini-paper sample for a CFD-AI manuscript.

Topic:

> A convolutional super-resolution model reconstructs high-resolution vorticity fields from downsampled snapshots of two-dimensional incompressible cylinder wake and decaying turbulence. The sample should be suitable as a seed manuscript for a JFM/Physics of Fluids style paper.

Available fictional-but-scoped evidence for this sample:

- Flow cases: circular-cylinder wake at $Re_D=100$ and two-dimensional homogeneous decaying turbulence.
- Inputs: spatially downsampled vorticity snapshots with downsampling factors $r=4$ and $r=8$.
- Output: reconstructed high-resolution vorticity field.
- Baselines: bicubic interpolation and a small U-Net baseline.
- Metrics: relative $L_2$ error, vorticity spectrum error, and vorticity-PDF agreement.
- Claimed results: 22% lower relative $L_2$ error than bicubic interpolation at $r=4$ on in-regime test snapshots; improved high-wavenumber spectral trend relative to bicubic; weaker reliability for unseen $Re_D=300$ and sharp shear-layer extrema.
- Missing evidence: no runtime benchmark, no 3D turbulence, no experimental PIV validation, no conservation-residual audit yet.

Generate:

1. title
2. abstract
3. short introduction
4. method sketch
5. result/limitation paragraph

A/B condition:

- `no_skill_baseline.tex`: answer without using the CFD-AI paper skill package; typical generic AI writing is allowed.
- `with_skill_cfd_ai.tex`: answer using the CFD-AI/SciML paper skills package, especially claim-evidence alignment, field-native vocabulary, scoped claims, baselines, physical diagnostics, and TODO marking.
