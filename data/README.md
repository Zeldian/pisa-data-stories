# PISA 2018 Data Inventory

## Source

All files downloaded from the OECD PISA 2018 database file server:
`https://webfs.oecd.org/pisa2018/`

Official database page (Cloudflare-protected, may require a browser):
`https://www.oecd.org/pisa/data/2018database/`

Downloaded: 2026-06-29

---

## Files in `data/raw/`

| File | Size | Format | Description |
|------|------|--------|-------------|
| `SPSS_STU_QQQ.zip` | 478 MB | SPSS `.sav` (zipped) | Student questionnaire — all background variables + plausible values for reading, math, and science |
| `SPSS_SCH_QQQ.zip` | 3.0 MB | SPSS `.sav` (zipped) | School questionnaire — principal-reported school characteristics |
| `SPSS_TCH_QQQ.zip` | 13 MB | SPSS `.sav` (zipped) | Teacher questionnaire — teacher-reported data on instruction and working conditions |
| `PISA2018_codebook.xlsx` | 5.2 MB | Excel | Variable codebook — names, labels, response scales, and derived index documentation for the student questionnaire |

Additional available files **not yet downloaded** (fetch only when a hypothesis requires them):
- `SPSS_STU_COG.zip` (~477 MB) — cognitive item-level responses (needed for item-difficulty or DIF analyses)
- `SAS_STU_QQQ.zip`, `SAS_SCH_QQQ.zip`, `SAS_TCH_QQQ.zip` — SAS format equivalents (redundant if using SPSS files)

---

## What each file is used for

**`SPSS_STU_QQQ.zip`** — primary data file for nearly all story analyses.
Contains ~612,000 student records across 79 countries/economies. Key variable groups:
- `PV1READ`–`PV10READ`, `PV1MATH`–`PV10MATH`, `PV1SCIE`–`PV10SCIE` — 10 plausible values per domain (use all 10 for correct variance estimation)
- `W_FSTUWT` + `W_FSTURWT1`–`W_FSTURWT80` — student final weight + 80 replicate weights (needed for standard error calculation)
- `CNT`, `CNTRYID`, `CNTSCHID`, `CNTSTUID` — country, school, student identifiers
- `ST001D01T` (grade), `ST004D01T` (gender), `ESCS` (socioeconomic index), `IMMIG` (immigration status), `LANGN` (language at home)
- Derived indices: `JOYREAD`, `MOTIVA`, `BELONG`, `ANXTEST`, `GRIT`, `MASTGOAL`, `PERCOMP`, `COMPETE`, `WORKMAST`, `ICTRES`, `HOMEPOS`, `PAREDINT`, `WEALTH`

**`SPSS_SCH_QQQ.zip`** — school-level analysis and multi-level modelling.
Contains one record per school (~21,000 schools). Links to student data via `CNTSCHID`.
Key variables: school type (public/private), size, resources, principal leadership, disciplinary climate, teacher shortages.

**`SPSS_TCH_QQQ.zip`** — teacher-level analysis (limited countries).
Contains ~260,000 teacher records. Links to schools via `CNTSCHID`.
Note: teacher data is only available for a subset of participating countries.

**`PISA2018_codebook.xlsx`** — reference for all variable names and response scales in the student questionnaire. Check here first when identifying which variables to use for a hypothesis.

---

## Variable catalog

[`variable_catalog.csv`](variable_catalog.csv) and [`variable_catalog.md`](variable_catalog.md) list all 1,664 variables across the three questionnaires with name, label, category, and source file. Use them for fast feasibility checks before opening the full codebook.

---

## Which file to use

| Analysis type | Primary file | Secondary file |
|---------------|-------------|----------------|
| Student performance by country | `SPSS_STU_QQQ.zip` | — |
| Student background → performance | `SPSS_STU_QQQ.zip` | — |
| School characteristics → performance | `SPSS_STU_QQQ.zip` | `SPSS_SCH_QQQ.zip` |
| Teacher practices → performance | `SPSS_TCH_QQQ.zip` | `SPSS_SCH_QQQ.zip` |
| Multi-level (student + school) | `SPSS_STU_QQQ.zip` | `SPSS_SCH_QQQ.zip` |
| Item-level / psychometric | `SPSS_STU_COG.zip` | `SPSS_STU_QQQ.zip` |

---

## Methodology

See [`methodology.md`](methodology.md) for required analysis procedures: plausible value pooling, student weights, BRR standard errors, and benchmarking. These apply to every analysis in this project.
