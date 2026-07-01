# Bad to Good Abstract

## Bad

We propose a novel AI model for CFD that accurately predicts turbulent flows. The method is robust, fast, and physically consistent. Results show state-of-the-art performance on several simulations and demonstrate the promise of deep learning for fluid mechanics.

## Why it fails

| Problem | Reviewer risk |
|---|---|
| No flow regime | Reviewer cannot tell whether this is laminar, transitional, turbulent, compressible, wall-bounded, etc. |
| "AI model" vague | Architecture and task are unclear. |
| "Robust" unsupported | No noise/OOD/rollout evidence named. |
| "Physically consistent" unsupported | No conservation, residual, spectrum, or force diagnostic named. |
| "State-of-the-art" unsupported | No baselines or split. |

## Better

We study data-driven super-resolution for two-dimensional incompressible wake and decaying-turbulence fields where high-resolution measurements or simulations are unavailable at inference time. A convolutional reconstruction model maps downsampled velocity/vorticity snapshots to high-resolution fields and is compared with bicubic interpolation and a U-Net-style baseline under fixed train/test splits. On unseen snapshots at the stated Reynolds-number regimes, the model reduces relative field error and better preserves vorticity-spectrum trends, while remaining less reliable for out-of-distribution Reynolds numbers and near sharp shear-layer extrema. The results support a scoped claim: learned reconstruction can recover selected high-wavenumber flow content from coarse inputs when the training data cover the target regime.

## Evidence map

| Claim | Evidence required |
|---|---|
| Super-resolution works in target regime | GT/coarse/pred/error fields; relative L2; same color scale |
| Better than classical baseline | Bicubic and learned baseline on same split |
| Preserves physics | Spectrum/vorticity PDF/conservation residual as appropriate |
| Limited OOD reliability | Unseen Re or forced failure case |

