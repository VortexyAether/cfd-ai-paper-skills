# Gold-Paper Style Reconstruction Task Template

Use this task template when evaluating whether a manuscript seed is close to the gold-paper target rather than merely fluent.

## Inputs

- Target paper metadata and dense summary.
- Source-scope statement listing what is confirmed and what remains unknown.
- Optional gold-paper note for the with-skill arm only.

## Output required

Generate a manuscript seed with these sections:

1. Title candidate.
2. Abstract.
3. Introduction skeleton with paragraph purpose labels.
4. Method summary with confirmed vs TODO details.
5. Results sequence with figure/table plan.
6. Limitations and reviewer-risk paragraph.
7. Claim-evidence map.

## Style target

The output should read like a careful CFD-AI/SciML journal seed:

- physical problem before AI capability;
- narrow gap before method;
- input/output map before architecture detail;
- baseline and physical diagnostic before broad claim;
- limitations before future-work promise.

## Prohibited moves

- `novel framework` without prior-art contrast;
- `robust`, `generalizable`, `state-of-the-art`, `physically consistent`, or `real-time` without evidence;
- generic context paragraph that could fit any AI-for-science paper;
- invented solver, mesh, BC/IC, split, figure, or citation details;
- decorative figure captions.

## Scoring

Score with:

- `rubrics/gold-paper-closeness-rubric.md`;
- `rubrics/vocabulary-style-rubric.md`;
- `rubrics/claim-evidence-rubric.md`;
- domain-specific reproducibility or figure rubrics as needed.
