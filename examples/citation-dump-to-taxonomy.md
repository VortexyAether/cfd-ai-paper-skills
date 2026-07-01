# Citation Dump to Taxonomy

## Citation dump

Many works use PINNs, FNOs, DeepONets, CNNs, graph neural networks, and reinforcement learning for CFD. Prior studies have accelerated simulations, predicted flows, modeled turbulence, reconstructed fields, and controlled wakes.

## Taxonomy version

| Category | CFD bottleneck | Representative methods | Evidence needed |
|---|---|---|---|
| Reconstruction / super-resolution | Measurements or simulations are sparse/coarse | CNN/U-Net/SR models, sensor reconstruction | GT/coarse/pred/error, spectra, sensor sparsity tests |
| Neural operators / surrogates | Repeated PDE solves are expensive | FNO, DeepONet, graph operators | Unseen parameter/geometry tests, runtime, conservation checks |
| PINNs / physics-constrained learning | Data are sparse but equations are known | PINNs, residual losses, constrained networks | Residual convergence, BC/IC satisfaction, comparison to CFD |
| Turbulence closure | RANS/LES closures fail across regimes | Tensor-basis networks, GNN closures, learned eddy viscosity | A priori and a posteriori tests, stability, wall/friction metrics |
| ROM / latent dynamics | Full-order dynamics are high-dimensional | POD/DMD/SINDy/autoencoders/RNNs | Long-horizon stability, modal energy, nonlinear correlations |
| Control / optimization | Design/control loops are expensive | RL, Bayesian optimization, differentiable surrogates | Closed-loop tests, constraints, safety, compute budget |

## Gap paragraph pattern

Existing neural-operator CFD studies mainly address fast field prediction on fixed or mildly varying domains, while super-resolution work targets reconstruction from coarse fields and closure work targets modeled subgrid effects. Our contribution belongs to the reconstruction/surrogate boundary: it learns a mesh-aware mapping from sparse wall and wake observations to full-field vorticity for unseen Reynolds numbers. Therefore the decisive evidence is not a generic RMSE table; it is leakage-safe Re splits, sensor-sparsity stress tests, vorticity-spectrum preservation, and comparison with both interpolation and operator-learning baselines.

