# Plan: Speed, Struggle, and Quitting

## Data

- **Cognitive process file**: `data/raw/SPSS_STU_COG.zip` (`CY07_MSU_STU_COG.sav`, 606,627 students).
  For each cognitive item, the file carries a scored response (`*S`), timing of last
  visit (`*T`), time to first action (`*F`), and number of actions (`*A`).
- **Item scope**: items across Math (`CM`), Science (`CS`), and Reading (`CR`) that
  have a single plain scored-response column plus a time-to-first-action column
  (i.e. excluding multi-part items whose credit is split across `SA`/`SB`/... and
  excluding Reading Fluency items, which only carry `S`+`T`, no `F`/`A`). This yields
  **311 items** (60 Math, 83 Science, 168 Reading).
- **Students**: restricted to `ADMINMODE == 2` (computer-based administration) —
  551,930 students in **71 of 79 countries**. The 8 paper-based countries (ARG, JOR,
  LBN, MDA, MKD, ROU, SAU, UKR) have no process data and are excluded, and this will
  be stated as an explicit limitation.
- **Merge**: COG joined to `SPSS_STU_QQQ.zip` on `CNT`+`CNTSCHID`+`CNTSTUID` for
  `W_FSTUWT`, `ESCS`, `ST004D01T` (gender), and `PV1-10` for MATH/READ/SCIE (used only
  to rank countries/students by performance, not as the behavioral outcome).

## Item-level classification

Per item, value labels are read from the SPSS metadata directly (not hardcoded),
since one item (`CR561Q06S`) uses a non-standard code scheme (96/97/98/99 instead of
6/7/8/9, with graded partial-credit codes 11/12/13/21). For each item's scored column:

- `full_credit_codes` = codes whose label contains "full credit"
- `omit_codes` = codes whose label contains "not reached" or "no response"
- `excluded_codes` = codes whose label contains "not applicable" or "invalid" (item
  not in this student's form, or a data artifact — dropped, not counted as omission)

For each (student, item) pair actually administered (score not excluded):

1. **Omit/Quit**: score in `omit_codes`.
2. Otherwise, **Correct** = score in `full_credit_codes` (partial credit counts as
   "not fully right", grouped with "wrong" — a stated simplification), else **Wrong**.
3. For attempted (non-omit) items, **Fast**/**Slow** = the item's time-to-first-action
   (`*F`, milliseconds) is below/above that item's own median among attempted,
   valid-timing (`F >= 0`) respondents. A within-item median split is used (rather
   than a fixed absolute threshold) because items vary hugely in expected engagement
   time, and this keeps "fast" and "slow" meaningful as relative, comparable labels
   across items of different formats and difficulty.

This yields five mutually exclusive profiles per item response: **Fast-Right,
Slow-Right, Fast-Wrong, Slow-Wrong, Omit/Quit**. A small number of attempted
responses with missing/negative `F` are dropped from the profile calculation
(count and % will be reported).

## Student- and country-level aggregation

- Per student: share of administered items falling into each of the 5 profiles
  (each student's own denominator = items actually administered to them, since PISA
  uses rotated booklets).
- Per country: `W_FSTUWT`-weighted mean of each student-level share (point estimates,
  consistent with this repo's existing simplified-weighting convention — no BRR SEs).
- Country mean performance = weighted mean of the unweighted-PV-average across
  MATH/READ/SCIE, used only to find countries with **similar overall performance**
  but **different behavioral profile mixes** — the core comparison the hypothesis asks for.

## Planned outputs

1. **Chart 1** — Scatter: country mean score (x) vs. Omit/Quit share (y), all 71
   CBA countries, to show that omission behavior is not simply explained by ability.
2. **Chart 2** — Stacked bar: profile-share composition for a small set of
   performance-matched country pairs/groups with visibly different mixes (e.g. one
   "fast-guessing" system vs. one "slow-persisting" system at a similar score).
3. **Chart 3** — Within-country drill-down: Omit/Quit and Fast-Wrong shares by ESCS
   quintile and by gender, for 2-3 illustrative countries, to connect the behavioral
   story to known equity patterns already surfaced elsewhere in this repo (e.g.
   `hidden-underclass`).

## Why this approach

- Item-level classification directly answers "how did students get to their score,"
  not just what the score was — matching the hypothesis's ask.
- Median-split-within-item avoids inventing an arbitrary absolute time cutoff.
- Reading value labels from metadata (rather than assuming a fixed code scheme)
  avoids silently misclassifying the one item with a different coding convention —
  consistent with the project rule against inventing/assuming variable semantics.
- Restricting to items with a plain `S`+`F` pair keeps the classification internally
  consistent (one action-time definition, one credit definition per item) rather than
  mixing timing definitions (`F` vs `T`) across item types.
