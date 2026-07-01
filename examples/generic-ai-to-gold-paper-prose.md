# Generic AI Prose to Gold-Paper-Like CFD-AI Prose

Use these examples when a generated manuscript sounds like generic AI academic writing rather than a normal CFD-AI/SciML paper.

## Example 1 — Opening context

### Generic AI-ish

Recent advances in artificial intelligence have revolutionized computational fluid dynamics by enabling powerful models to solve complex turbulent flows with unprecedented accuracy.

### Gold-paper-like rewrite

High-resolution velocity and vorticity fields are often required to analyze wake dynamics, turbulent structures, and spectral energy content, but direct numerical simulation or dense experimental measurement can be too expensive or unavailable at the desired resolution. This motivates reconstruction methods that infer high-resolution flow fields from low-resolution snapshots while preserving the quantities used in fluid-mechanics analysis.

### Why better

- Starts from the physical/numerical bottleneck.
- Names variables and evidence objects.
- Does not claim revolution, accuracy, or generality before experiments.

## Example 2 — Gap statement

### Generic AI-ish

Existing models lack robustness and fail to generalize to diverse flow conditions.

### Gold-paper-like rewrite

Existing reconstruction results are often evaluated on snapshots drawn from the same simulated regime as the training data, leaving unclear whether the model recovers small-scale vorticity content under stronger downsampling, sparse observations, or Reynolds-number holdouts.

### Why better

- Replaces `robustness` with test axes.
- Replaces `diverse flow conditions` with specific holdout conditions.
- Suggests the required experiment.

## Example 3 — Method description

### Generic AI-ish

We propose a novel hybrid deep learning framework that seamlessly integrates physics into the model.

### Gold-paper-like rewrite

We train a convolutional reconstruction model to map downsampled velocity or vorticity snapshots to high-resolution fields. Physics enters the evaluation through vorticity statistics and spectral diagnostics; if a physics-based loss is used, its residual terms and weights must be reported separately from the architecture.

### Why better

- Names input/output map.
- Separates architecture from physics evidence.
- Does not use `seamlessly` or `novel` without prior-art contrast.

## Example 4 — Result paragraph

### Generic AI-ish

The proposed model achieves superior performance and captures complex flow structures more effectively than existing methods.

### Gold-paper-like rewrite

Against bicubic interpolation on the same low-resolution inputs, the model reduces the reported field error for the tested cylinder-wake and homogeneous-turbulence snapshots. Visual comparisons should be paired with error maps, vorticity PDFs, and spectra to show whether the improved metric corresponds to recovery of small-scale flow structures rather than smoother fields.

### Why better

- Names comparator and tested cases.
- Distinguishes metric improvement from physical recovery.
- Converts missing diagnostics into required evidence.

## Example 5 — Figure caption

### Generic AI-ish

Comparison of predicted turbulent flow fields showing the effectiveness of the proposed method.

### Gold-paper-like rewrite

Reference, low-resolution input, reconstructed vorticity, and pointwise error for the tested wake snapshot at the stated Reynolds number. The panel supports the reconstruction claim only if the same color scale is used and the error map is reported with a quantitative metric; spectral or PDF diagnostics are required before claiming recovery of small-scale turbulent content.

### Why better

- States panel roles.
- Adds condition and evidence requirement.
- Blocks overclaiming from a pretty field plot.

## Example 6 — Limitation paragraph

### Generic AI-ish

Future work will improve the model's scalability and robustness for real-world applications.

### Gold-paper-like rewrite

The present evidence does not establish performance under noisy sensors, unseen geometries, or Reynolds-number extrapolation. Those claims require leakage-safe holdout splits, controlled noise/sparsity sweeps, and physical diagnostics such as spectra, conservation residuals, or force histories under each regime.

### Why better

- Names untested axes.
- Names required tests.
- Avoids vague deployment promise.

## Quick conversion rule

For every sentence of the form:

> Our [adjective] AI framework [verb] complex CFD dynamics.

Rewrite as:

> For [flow/regime], [model family] maps [input] to [output] and is evaluated against [baseline] using [metric] plus [physical diagnostic]; claims are limited to [tested scope].
