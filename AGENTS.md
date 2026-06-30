# PISA Data Story Agent

## Goal

Test one PISA data story hypothesis at a time.

Determine whether the available PISA data can support the hypothesis. If it can, produce a complete, reproducible data story. If it cannot, reject the idea quickly with a short explanation.

## Workflow

1. Read the hypothesis.
2. Verify that the required PISA variables and data exist.
3. If the hypothesis is unsupported:

   * Stop immediately.
   * Create a Markdown file in `stories/rejected/` explaining why.
4. If the hypothesis is supported:

   * Create a new folder in `stories/accepted/<story-name>/`.
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

## Project Structure

```
data/
stories/
    accepted/
    rejected/
docs/
```
