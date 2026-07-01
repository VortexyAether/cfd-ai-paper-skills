---
name: limitations-ethics-llm-disclosure
description: Use when drafting or auditing limitations, ethics, compute, data/code availability, and LLM-usage disclosure sections for CFD-AI/SciML papers.
version: 0.3.0
author: VA + TARS
metadata:
  short-description: Limitations, ethics, and LLM disclosure audit
---

# Limitations, Ethics, and LLM Disclosure

## Trigger

Use near submission, revision, or when a manuscript needs honest limitations and disclosure language.

## Checklist

- physical assumptions
- simulation assumptions
- generalization boundary
- dataset bias or generation limits
- compute/energy cost
- proprietary code/data limits
- safety/dual-use if relevant
- LLM use: writing, code generation, ideation, data analysis, method component

## Output schema

| Area | Current statement | Missing risk | Suggested text |
|---|---|---|---|

## Wording rule

Limitations should narrow claims without sabotaging the paper.

## Anti-patterns

- Generic limitations such as "more work is needed" with no experiment boundary.
- Hiding LLM use in code, writing, or analysis when disclosure is required.
- Claiming sustainability, fairness, or safety benefits without evidence.
- Turning limitations into new unsupported claims.

## Verification

- Do not disclose nonexistent use.
- Do not hide material LLM/method/data involvement.
- Match target journal policy when known.
