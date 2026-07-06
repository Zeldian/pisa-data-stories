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
   * Briefly describe the planned analysis approach before writing any code. Include the variables to be used, the proposed analytical method, the expected outputs, and a short justification for why this approach is appropriate. If multiple reasonable approaches exist, briefly explain why the chosen one is preferred. This acts as a sanity check before implementation.
   * Write the analysis code.
   * Generate the required charts.
   * Write a clear technical report.
   * Use the most appropriate available global Claude Code data analysis skills to review the methodology, verify the analysis, improve visualizations where appropriate, and ensure the statistical conclusions are well supported.
   * Use the most appropriate available global Claude Code data storytelling skills to transform the technical report into a clear, engaging narrative suitable for a general audience while preserving factual accuracy.
   * Use the most appropriate available global Claude Code webpage/design skills to generate a clean, accessible, and visually appealing GitHub Pages webpage from the structured data story.
   * Generate the publishable webpage and supporting assets in `docs/`.

## Rules

* Work on only one hypothesis at a time.
* Reject unsupported ideas as early as possible.
* Do not continue analysis if the required data is unavailable.
* Keep each accepted story completely self-contained.
* Prefer simple, reproducible analyses over unnecessary complexity.
* Clearly state any assumptions and limitations.
* Do not modify previously accepted stories unless instructed.
* Do not invent variables or unsupported conclusions. When uncertain, explicitly state the limitation instead of making assumptions.
* Use available global Claude Code skills to enhance each stage of the workflow when appropriate, but always follow this project's workflow and requirements. Global skills should complement the project rather than replace its methodology.

## Publishing Workflow

After a story is accepted and its webpage is written, publish it:

1. Create `stories/accepted/<slug>/story.json` with title, subtitle, description, date, and tags.
2. Place the story webpage at `docs/<slug>/index.html`.
3. Run the build script to regenerate the homepage:
   ```
   python scripts/build_site.py
   ```
4. Commit and push:
   ```
   git add .
   git commit -m "Add story: <slug>"
   git push
   ```

GitHub Pages redeploys automatically. The homepage (`docs/index.html`) is always generated — never edit it by hand.

## Cross-cycle data

PISA 2018 is the primary dataset. Supplementary cycles are used for robustness
checks only. Do not replace 2018 as the basis for any story.

### Installed cycles (immediately available)

| Cycle | Status | Files present |
|-------|--------|---------------|
| 2018 | Installed | `data/raw/SPSS_STU_QQQ.zip` (primary; stories read raw directly) |
| 2022 | Installed | `data/raw/SPSS_STU_QQQ_2022.zip` + core extract + school summary |

### Supported cycles (pipeline ready; raw data not installed)

| Cycle | What is needed | How to obtain |
|-------|----------------|---------------|
| 2015 | Student SPSS zip | Browser download from `oecd.org/pisa/data/2015database/` (Cloudflare-gated) |
| 2012 | Student SPSS zip | Free OECD account registration at `oecd.org/en/data/register.html`, then download from `oecd.org/pisa/data/2012database/` |

Once the raw zip is supplied, the pipeline generates the core extract and school
summary automatically — no further configuration is needed:
```
python3 scripts/prepare_pisa_cycle.py --cycle 2022                                  # automated
python3 scripts/prepare_pisa_cycle.py --cycle 2015 --raw-zip ~/Downloads/<file>.zip
python3 scripts/prepare_pisa_cycle.py --cycle 2012 --raw-zip ~/Downloads/<file>.zip
```

**Use the smallest dataset that covers your needs:**

| Need | File to use |
|------|-------------|
| School-level analysis | `data/processed/pisa_{cycle}_school_summary.csv` |
| Student-level analysis | `data/processed/pisa_{cycle}_core.csv.gz` |
| BRR standard errors / full variable set | `data/raw/SPSS_STU_QQQ_{cycle}.zip` (raw SPSS) |

See `data/README.md` for full download instructions and variable harmonization notes.
Check `data/processed/pisa_cycles_inventory.csv` for machine-readable cycle status.

## Project Structure

```
data/
    raw/                  # Original downloaded files (gitignored, re-downloadable)
    processed/            # Cleaned/derived datasets (committed)
        country_reading_summary.csv          # 2018 story aggregate
        country_math_icc.csv                 # 2018 story aggregate
        pisa_2022_core.csv.gz                # 2022 cross-cycle student extract (installed)
        pisa_2022_school_summary.csv         # 2022 cross-cycle school summary (installed)
        pisa_cycles_inventory.csv            # Cycle metadata and file registry
    README.md             # File inventory, hierarchy, and download instructions
    methodology.md        # Required analysis procedures (PVs, weights, BRR SEs)
    variable_catalog.csv  # All 1,664 variables across student/school/teacher files
    variable_catalog.md   # Same catalog in readable Markdown
scripts/
    build_site.py         # Regenerates docs/index.html from stories/accepted/
    prepare_pisa_cycle.py # Downloads and processes additional PISA cycles (v1.0)
stories/
    accepted/             # One subfolder per completed story
        <slug>/
            analysis.py   # Reproducible analysis script
            report.md     # Technical report
            story.json    # Metadata for the build script
            charts/       # Generated chart images
    rejected/             # One Markdown file per rejected hypothesis
docs/                     # Static site served by GitHub Pages
    index.html            # Generated homepage — do not edit by hand
    <slug>/               # One folder per published story
```
