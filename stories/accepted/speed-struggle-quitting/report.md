# Speed, Struggle, and Quitting — Technical Report

**PISA 2018 — 71 computer-based countries, 551,792 students**

---

## Hypothesis

Students and countries with similar academic scores may reach those scores through
fundamentally different test-taking behavior: some answer fast and confidently, some
work slowly and persist, and some give up on a substantial share of items rather than
attempting them. Country-level score averages hide this entirely — two systems scoring
identically on the PISA scale could be producing very different kinds of test-takers.

**Result: Confirmed.** Response style (the balance of fast vs. slow correct answers)
is only weakly correlated with performance (r = 0.61) — meaning most of the variation
in style happens *within* a given performance level, not because of it. Within a
20-country band scoring 495–520 points, "speed style" (the share of correct answers
given fast) ranges from 40.3% (Sweden) to 81.0% (Korea) — a 2x spread at essentially
the same academic level. Giving up is even less tied to performance (r = −0.65, but
with wide scatter): the Netherlands and Sweden score within 0.1 points of each other,
yet Swedish students omit or fail to reach 4x as many items (10.3% vs 2.5%).

---

## Data and Method

### Source

PISA 2018 cognitive process data, `SPSS_STU_COG.zip` (`CY07_MSU_STU_COG.sav`). For
each computer-based cognitive item, this file carries — alongside the standard scored
response — genuine process/log variables: `*T` (timing of last visit), `*F` (time to
first action), and `*A` (number of actions). This is not the restricted PISA "log
file" special study; it is part of the standard public-use cognitive file, previously
undownloaded in this repository.

### Item scope: 311 items

Restricted to items with a single plain scored-response column (`*S`) plus a
time-to-first-action column (`*F`) — i.e. excluding multi-part items whose credit is
split across sub-parts (`*SA`/`*SB`/...) and excluding Reading Fluency items, which
carry only `*S`+`*T` (no per-action timing). This keeps one consistent timing
definition and one consistent credit definition across every item used.

| Domain | Items |
|--------|-------|
| Math (CM) | 60 |
| Science (CS) | 83 |
| Reading (CR) | 168 |
| **Total** | **311** |

### Student scope: computer-based administration only

`ADMINMODE == 2`. Of 606,627 students in the file, 551,930 (91%) took the
computer-based assessment across 71 countries; only these have item-level timing.
The 8 paper-based countries — Argentina, Jordan, Lebanon, Moldova, North Macedonia,
Romania, Saudi Arabia, Ukraine — have no process data and are excluded entirely.

**Important implementation detail:** by default, `pyreadstat` silently converts
SPSS-declared "user missing" codes (6 = Not Reached, 9 = No Response, etc.) to `NaN`.
Reading with `user_missing=True` was required to recover these codes — without it,
every omission is invisible and `share_omit` reads as exactly 0% for every item.

### Item-level classification

Per item, the classification uses the item's own SPSS value-label text — not a
hardcoded code scheme — because one item (`CR561Q06S`) uses non-standard codes
(96/97/98/99 with graded partial credit 0/11/12/13/21, vs. the usual 0/1/6/7/8/9).
For each item's scored column:

- `full_credit_codes` = codes whose label contains "full credit"
- `omit_codes` = codes whose label contains "not reached" or "no response"
- `excluded_codes` = codes whose label contains "not applicable" or "invalid"
  (item not in this student's rotated form, or a data artifact — dropped, not
  counted as an omission)

For every (student, item) pair actually administered:

1. **Omit/Quit** — score in `omit_codes`.
2. Otherwise, **Correct** = score in `full_credit_codes` (partial credit is grouped
   with "not fully right" — a stated simplification); else **Wrong**.
3. For attempted items, **Fast** / **Slow** = time-to-first-action (`*F`,
   milliseconds) below / at-or-above that item's own median among attempted,
   valid-timing (`F ≥ 0`) respondents. A **within-item median split** is used
   instead of a fixed cutoff because items vary hugely in expected engagement time
   (a one-click multiple-choice item vs. a multi-step interactive simulation); this
   keeps "fast" and "slow" meaningful as relative, comparable labels across formats.

This yields five profiles per item response: **Fast-Right, Slow-Right, Fast-Wrong,
Slow-Wrong, Omit/Quit**. 96,923 attempted responses (0.41%) had missing/negative
timing and were dropped from the profile calculation.

### Aggregation

- **Student level**: share of a student's administered items falling into each
  profile (denominator = items actually administered to that student, since PISA
  uses rotated booklets — median 46 of the 311 items per student). Students with
  fewer than 10 classified items (138 students, 0.02%) were dropped.
- **Country level**: `W_FSTUWT`-weighted mean of student shares — point estimates,
  consistent with this repository's existing simplified-weighting convention (no
  BRR standard errors).
- **Speed style** (used for Charts 1–2): of a student's *correctly* answered items,
  what share were fast? `n_fast_right / (n_fast_right + n_slow_right)`. This isolates
  response-time style from raw ability — a student who gets 90% right slowly and one
  who gets 90% right fast have identical accuracy but opposite styles, and this
  metric captures only that difference, not the shared accuracy.
- **Academic performance**: mean of PV1–10 for Math, Reading, and Science (simple
  point estimate per this repo's established convention), averaged across the three
  domains, then weighted-averaged per country. Used only to find countries at
  similar performance levels — not as a behavioral outcome.
- Countries with fewer than 200 CBA students in the merged sample were dropped
  (none were, in practice — all 71 CBA countries retained).

---

## Key Results

### Global averages (mean of 71 country means)

| Profile | % of items |
|---|---|
| Fast-Right | 24.4% |
| Slow-Right | 26.1% |
| Fast-Wrong | 21.8% |
| Slow-Wrong | 21.1% |
| Omit/Quit | 6.6% |

### Same score, very different style

Among the 20 countries scoring 495–520 points (mean of Math/Reading/Science):

| Country | Score | Speed style |
|---|---|---|
| Korea | 520 | **81.0%** |
| Chinese Taipei | 517 | **76.3%** |
| Japan | 520 | 57.2% |
| UK | 503 | 56.6% |
| USA | 495 | 57.1% |
| Australia | 499 | 56.2% |
| Netherlands | 502 | 54.6% |
| Canada | 517 | 53.4% |
| Finland | 516 | 47.6% |
| Poland | 513 | 47.7% |
| Sweden | 503 | **40.3%** |

East/Southeast Asian systems (Korea, Chinese Taipei, Hong Kong, Macao, Singapore,
B-S-J-Z China, Japan) average 70.6% speed-style vs. 44.8% for every other system —
a distinct cluster, not a smooth gradient. Across all 71 countries, academic
performance explains only a moderate share of style variation (r = 0.61); the East
Asian cluster drives most of that correlation. Excluding it, the relationship between
score and style essentially flattens.

### Giving up is not explained by performance alone

Academic score vs. omit share correlates at r = −0.65 across all 71 countries — but
with wide scatter around that trend. The clearest example: **Netherlands (502.5 pts,
2.5% omitted) and Sweden (502.6 pts, 10.3% omitted)** score within a tenth of a point
of each other, yet Swedish students give up on roughly 4x as many items.

### Giving up is also an equity story within countries

| Country | Q1 (lowest SES) | Q5 (highest SES) | Gradient |
|---|---|---|---|
| Peru | 22.2% | 10.1% | Steep (12.1 pp) |
| France | 11.6% | 6.0% | Steep (5.7 pp) |
| USA | 6.7% | 2.4% | Steep (4.3 pp) |
| Sweden | 12.1% | 9.9% | **Flat (2.2 pp)** |

Peru, France, and the USA show the expected pattern: disadvantaged students give up
far more often than wealthy ones. Sweden is different — its overall omit rate is high
*and* nearly flat across the SES distribution, suggesting Sweden's elevated omission
is less a disadvantage-driven phenomenon and more a broadly shared national pattern,
unlike the sharply unequal "quitting" seen in Peru.

---

## Limitations

1. **Restricted to 71 of 79 countries.** The 8 paper-based countries have no item
   timing data at all and are entirely absent from this analysis. Conclusions apply
   only to systems that ran the computer-based assessment.

2. **Partial credit collapsed into "wrong."** 15 of 311 items award partial credit
   (0/1/2 or graded schemes). This analysis treats only full credit as "Correct" —
   a defensible but coarsening simplification for a behavioral (not scoring)
   classification.

3. **Within-item median split, not an absolute time threshold.** "Fast" and "slow"
   are relative to each item's own response-time distribution, not a universal
   number of seconds. This is intentional (see Method) but means "fast" in a
   30-second item and "fast" in a 3-minute item are not the same absolute duration.

4. **"Not Reached" vs. "No Response" are combined** into a single Omit/Quit category.
   "Not Reached" (ran out of time before reaching the item) and "No Response" (saw
   the item but skipped it) are conceptually distinct — one reflects pacing/time
   pressure, the other active disengagement. This report does not separate them;
   a finer future analysis could.

5. **Descriptive, not causal.** This story compares behavioral profile distributions
   across countries, schools, and SES groups. It does not test why an education
   system produces one style over another (culture, item exposure, test-taking
   coaching, timed-test familiarity, etc. are all plausible and untested
   explanations).

6. **Item pool covers 311 of the full item bank.** Items lacking a plain single
   scored-response column, and the 8 skipped stems with unusable value-label text,
   are not represented. This is unlikely to bias domain coverage meaningfully (each
   domain still retains 60–168 items) but is not the complete cognitive item set.

---

## Files

| File | Description |
|------|-------------|
| `analysis.py` | Full analysis pipeline (classification + aggregation + charts) |
| `PLAN.md` | Pre-implementation design rationale |
| `story.json` | Story metadata |
| `charts/same_score_different_style.png` | Bar: speed style, 20 countries scoring 495–520 |
| `charts/academic_vs_speed_style.png` | Scatter: academic score vs. speed style, 71 countries |
| `charts/academic_vs_omit.png` | Scatter: academic score vs. omit share, NLD/SWE callout |
| `charts/omit_by_escs.png` | Bar: omit rate by SES quintile, 4 countries |
| `../../data/processed/speed_struggle_quitting_student_profiles.csv.gz` | Student-level profile shares |
| `../../data/processed/speed_struggle_quitting_country.csv` | Country-level aggregates |
| `../../data/processed/speed_struggle_quitting_matched_pairs.csv` | Near-identical-score country pairs ranked by omit-share gap |
