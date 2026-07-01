# Recommended Patch

Add v0.4 super-resolution rules:

1. For spatio-temporal SR, require separate rows for spatial downsampling, temporal frame interval, and reference high-resolution source.
2. Figure grammar must include GT/coarse-input/prediction/error for both field snapshots and temporal evolution.
3. Experiments must include at least one sanity case, one turbulent statistics case, and one robustness axis: training snapshots, downsampling factor, or frame interval.

