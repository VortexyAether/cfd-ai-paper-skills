# AI-ish to Field-Native Prose

Purpose: examples for rewriting generic AI-assisted manuscript language into CFD-AI/SciML field-native prose.

## Example 1 — Abstract claim

### Bad

We propose a novel AI framework that robustly predicts turbulent flows with state-of-the-art accuracy and strong physical consistency.

### Diagnosis

| Problem | Missing evidence |
|---|---|
| novel AI framework | task, architecture, prior-art boundary |
| robust | stress axis and tested range |
| turbulent flows | flow case, regime, variables |
| state-of-the-art | named baselines, same split/metric |
| physical consistency | conservation/spectrum/force diagnostic |

### Field-native rewrite

We evaluate a convolutional surrogate for predicting velocity and vorticity fields in the unsteady circular-cylinder wake, using Reynolds-number holdouts to test interpolation and extrapolation. The physics-loss variant is compared with an unconstrained CNN/GAN baseline using field error and conservation-residual diagnostics; claims are limited to the tested Reynolds-number range and rollout horizon.

## Example 2 — Related work

### Bad

Recent advances in deep learning have revolutionized CFD, and many works have applied AI to fluid mechanics.

### Diagnosis

This is a citation dump opening. It gives no workflow taxonomy and no contribution boundary.

### Field-native rewrite

Prior ML-for-fluids work can be grouped by workflow role: reconstruction of under-resolved fields, surrogate/ROM acceleration, turbulence closure, flow control, discovery of governing structure, and experimental sensing or estimation. This study belongs to [role] because it maps [input] to [output] under [flow/regime], and differs from [specific prior class] by [bounded contribution].

## Example 3 — Results

### Bad

The proposed model significantly improves performance and captures the complex physics of the flow.

### Diagnosis

No metric, baseline, physical diagnostic, or failure boundary.

### Field-native rewrite

On the unseen $Re=[value]$ test case, the model reduces relative [velocity/vorticity/drag] error compared with [baseline] and better matches the [spectrum/vorticity PDF/force time history]. The largest errors remain near [shear layer/wall region/wake transition], which bounds the physical-consistency claim.

## Example 4 — Figure caption

### Bad

Visualization of model performance on turbulent flow.

### Field-native rewrite

Ground-truth, low-resolution input, reconstructed vorticity, and pointwise error for the [flow case] at [regime]. The shared color scale shows that the learned reconstruction recovers [structure/spectral band] better than [baseline], while errors concentrate near [region].

## Example 5 — Limitation

### Bad

Although promising, future work will further improve the robustness and applicability of the framework.

### Field-native rewrite

The present evidence does not establish robustness outside the trained [Re/geometry/roughness/noise] range. Future tests should include [specific OOD axis], [noise/sparse-sensor condition], and [physical diagnostic] before claiming generalization beyond the current setup.

## Example 6 — Reviewer response

### Bad

We thank the reviewer and believe our method is robust and physically consistent.

### Field-native rewrite

We thank the reviewer for raising the issue of physical consistency. We have added [diagnostic] in Section [X] and Figure [Y], comparing the proposed model with [baseline] on the same test split. The revised text now limits the claim to [tested regime] and states that [untested regime] remains future work.
