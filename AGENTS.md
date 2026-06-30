# PISA Data Story Agent

## Goal

Test one PISA data story hypothesis at a time.

Determine whether the available PISA data can support the hypothesis. If it can, produce a complete, evidence-backed data story. If it cannot, reject the idea quickly with a short explanation.

## Feasibility Checklist

Before writing any analysis code, output both tables below.

### Required Checks

All three must pass. A single ❌ stops the analysis immediately.

| Check | Result | Reason |
|-------|--------|--------|
| Data Availability | ✅/❌ | Can the hypothesis be tested using the available PISA 2018 data? |
| Variable Availability | ✅/❌ | Are all required variables present in the downloaded datasets? |
| Analytical Soundness | ✅/❌ | Can it be tested with an appropriate method without unsupported causal claims? |

**If any Required Check is ❌:** Stop immediately. Do not write analysis code.
Create a short Markdown file in `stories/rejected/` explaining which check
failed and why.

### Quality Checks

These are not automatic rejection criteria. For each, briefly explain the
trade-offs and make a recommendation on whether the story is still worth
pursuing.

| Check | Result | Notes |
|-------|--------|-------|
| Story Potential | ✅/⚠️/❌ | Is the expected finding meaningful or insightful for a general audience? |
| Novelty / Insight | ✅/⚠️/❌ | Does it reveal something non-obvious or add a fresh angle? |
| Reproducibility | ✅/⚠️/❌ | Can the analysis be reproduced entirely from data and code in this repository? |

**If one or more Quality Checks are weak (⚠️ or ❌):** Explain the trade-offs
and recommend whether the story is still worth pursuing. Do not automatically
reject — the final call may depend on context.

**Only proceed to the Workflow if all Required Checks are ✅.**

## Workflow

1. Read the hypothesis.
2. Verify that the required PISA variables and data exist.
3. If the hypothesis is unsupported:

   * Stop immediately.
   * Create a Markdown file in `stories/rejected/` explaining why.
4. If the hypothesis is supported:

   * Create a new folder in `stories/accepted/<story-name>/`.
   * Briefly describe the planned analysis approach (variables, method, expected output) before writing any code. This acts as a sanity check.
   * Write the analysis code.
   * Generate the required charts.
   * Write a clear report.
   * Generate a publishable webpage in `docs/`.

## Rules

* Work on only one hypothesis at a time.
* Reject unsupported ideas as early as possible.
* Do not continue analysis if the required data is unavailable.
* Keep each accepted story completely self-contained.
* Prefer simple, reproducible analyses over unnecessary complexity.
* Clearly state any assumptions and limitations.
* Do not modify previously accepted stories unless instructed.
* Do not invent variables or unsupported conclusions. When uncertain, explicitly state the limitation instead of making assumptions.

## Project Structure

```
data/
    raw/                  # Original downloaded files (gitignored)
    processed/            # Cleaned/derived datasets
    README.md             # File inventory and usage guide
    methodology.md        # Required analysis procedures (PVs, weights, BRR SEs)
    variable_catalog.csv  # All 1,664 variables across student/school/teacher files
    variable_catalog.md   # Same catalog in readable Markdown
stories/
    accepted/             # One subfolder per completed story
    rejected/             # One Markdown file per rejected hypothesis
docs/                     # Publishable webpages (one per accepted story)
```
