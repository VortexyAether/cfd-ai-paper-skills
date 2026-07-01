# Dense source summary — Fukami 2019 reconstruction benchmark

Source target: Fukami, Fukagata, and Taira, *Super-resolution reconstruction of turbulent flows with machine learning*, Journal of Fluid Mechanics, 2019.

Source scope for this benchmark: internal gold-paper note based on arXiv metadata/abstract and accessible arXiv text. Full PDF figure-caption verification remains TODO.

## Compressed summary given to the model

The paper frames super-resolution as a fluid-flow reconstruction problem rather than a generic image-processing task. High-fidelity simulations and experiments can produce valuable flow-field data, but practical measurements or stored datasets may be under-resolved. The goal is to reconstruct high-resolution flow fields from low-resolution inputs.

The method uses convolutional neural networks and hybrid downsampled skip-connection / multi-scale models. The input is a coarse flow representation and the output is a reconstructed high-resolution field. The paper compares learned reconstruction against classical interpolation, especially bicubic interpolation. Training uses reconstruction loss; accessible text notes L2-type training, Adam, and early stopping, but exact solver/training details, seeds, and full hyperparameter tables must remain TODO unless verified from the paper.

The evidence sequence is approximately:

1. Introduce a low-resolution-to-high-resolution reconstruction pipeline.
2. Demonstrate on a canonical cylinder wake at Reynolds number based on diameter, `Re_D=100`.
3. Use vorticity/velocity-field visualizations and quantitative error to compare ground truth, coarse input, interpolation, and learned reconstruction.
4. Examine training-snapshot sensitivity; accessible text notes a small-data claim with as few as 50 snapshots, but exact curves and values must not be invented.
5. Use vorticity-PDF agreement for the cylinder wake.
6. Stress the method on two-dimensional homogeneous decaying turbulence using low-resolution inputs and high-resolution outputs.
7. Discuss turbulent small-scale/high-wavenumber reconstruction using quantitative and physical diagnostics; exact spectral/statistical panels require PDF verification and should be TODO if not supplied.

Known flow cases:

- incompressible cylinder wake at `Re_D=100`;
- two-dimensional homogeneous decaying turbulence.

Known or inferable variables:

- velocity vector and/or vorticity fields;
- low-resolution flow images/fields to high-resolution flow fields.

Known downsampling/model details:

- average and max pooling are mentioned in accessible text;
- CNN and hybrid DSC/MS model family;
- bicubic interpolation baseline.

Allowed claims:

- The paper studies super-resolution reconstruction of fluid-flow fields from coarse inputs.
- It uses canonical cylinder wake and 2D homogeneous turbulence examples.
- It compares learned models with classical interpolation.
- It treats physical/statistical diagnostics as important for turbulent-flow reconstruction.
- It suggests super-resolution may help recover under-resolved flow structures under the tested conditions.

Do not claim unless marked TODO or externally verified:

- exact numerical error values;
- exact architecture layer counts;
- exact solver implementation details;
- exact train/validation/test split seeds;
- exact figure captions and panel order;
- code repository status;
- broad real-time deployment, universal turbulence recovery, 3D CFD generalization, or solver acceleration.

## Reconstruction task

Using only this dense summary, reconstruct a reviewer-defensible LaTeX manuscript seed of the original paper. Do not invent missing numbers, solver settings, citation metadata, or figure results. Mark missing details as TODO.