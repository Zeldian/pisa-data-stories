# PISA Data Stories

Evidence-backed stories from the OECD PISA 2018 dataset.
Live site: **https://zeldian.github.io/pisa-data-stories/**

## What this is

Each story tests one hypothesis against PISA 2018 data (612,004 students, 79 countries). Stories that pass a feasibility check become reproducible analyses with charts, a technical report, and a published webpage.

## Repository layout

```
data/
    raw/              # Original PISA files — gitignored, re-downloadable from OECD
    processed/        # Derived CSVs committed here
    README.md         # Data inventory and download instructions
    methodology.md    # Required analysis procedures (plausible values, weights)
    variable_catalog  # All 1,664 PISA variables (CSV + Markdown)
stories/
    accepted/<slug>/  # One folder per published story
        analysis.py   # Reproducible analysis script
        report.md     # Technical report
        story.json    # Metadata consumed by the build script
        charts/       # Generated chart images
    rejected/         # One Markdown file per rejected hypothesis
scripts/
    build_site.py     # Regenerates docs/index.html from stories/accepted/
docs/                 # Static site served by GitHub Pages
    index.html        # Generated homepage — do not edit by hand
    <slug>/           # One folder per published story
        index.html    # Story webpage
```

## Adding a new story

```bash
# 1. Run the analysis and create the story folder
stories/accepted/<slug>/analysis.py
stories/accepted/<slug>/report.md
stories/accepted/<slug>/charts/
stories/accepted/<slug>/story.json   # see format below

# 2. Write the story webpage
docs/<slug>/index.html

# 3. Regenerate the homepage
python scripts/build_site.py

# 4. Commit and push
git add .
git commit -m "Add story: <slug>"
git push
```

### story.json format

```json
{
  "title": "Story Title",
  "subtitle": "PISA 2018 · Subject",
  "description": "One or two sentences shown on the homepage card.",
  "date": "YYYY-MM-DD",
  "tags": ["tag1", "tag2"]
}
```

## Data access

Raw PISA 2018 files are not committed (too large). Download from:
**https://www.oecd.org/pisa/data/2018database/**

See `data/README.md` for the exact files needed and `data/methodology.md` for required analysis procedures.

## Analysis conventions

- Use all 10 plausible values (PV1–PV10); average estimates before forming ratios (Rubin's rules)
- Apply `W_FSTUWT` student final weights throughout
- See `data/methodology.md` for the full list of requirements
