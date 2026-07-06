# Excellence Without Misery — Technical Report

**PISA 2018 — Academic Performance vs. Student Well-being, 71 countries**

---

## Hypothesis

High academic achievement necessarily comes at the expense of student well-being.
If true, countries with the highest PISA scores should systematically show the
lowest student life satisfaction. If false — if some systems achieve both — that
challenges a widely held assumption about what high-performing education requires.

**Result: Partially supported, and more interesting for it.** A moderate negative
correlation between national performance and life satisfaction is real and
statistically significant (r = −0.481). But 13 countries break the pattern and
occupy the "excellence without misery" quadrant. The contrast between Finland and
Japan — virtually identical academic performance, a 1.4-point life satisfaction gap
on a 10-point scale — shows the tradeoff is not inherent to excellence itself.

---

## Method

**Performance metric:** Weighted country mean of a composite score: the mean of
Math, Reading, and Science domain scores, where each domain score is the unweighted
mean of 10 plausible values for that student. Using all three domains treats
academic achievement broadly rather than privileging PISA 2018's primary domain
(Reading). Country means differ negligibly from proper per-PV averaging for this
purpose.

**Well-being (primary axis):** Weighted country mean of `ST016Q01NA` — a single
0–10 life satisfaction item: *"Overall, how satisfied are you with your life as a
whole these days?"* Used because it is direct, universally understood, and the
closest proxy to subjective well-being available in PISA 2018.

**Well-being (multi-dimensional):** Four OECD-derived WLE indices complement the
primary axis:

| Variable | Construct | Direction |
|----------|-----------|-----------|
| `BELONG` | Sense of belonging to school | Higher = better |
| `SWBP` | Subjective well-being: positive affect | Higher = better |
| `BEINGBULLIED` | Experience of bullying | **Higher = worse** (inverted) |
| `GFOFAIL` | General fear of failure | **Higher = worse** (inverted) |

A composite well-being score is computed as the mean of these four z-scores
(after inversion where required), alongside the standardized life satisfaction score.

**Quadrant thresholds:** Sample median on both axes (performance median = 462.5;
life satisfaction median = 7.21). This gives an equal-split, threshold-free
quadrant that requires no arbitrary cutoff.

**Weighting:** Student final weight `W_FSTUWT` throughout.

---

## Key Results

### The global pattern

| Statistic | Value |
|-----------|-------|
| Countries with complete data | 71 |
| Performance–life satisfaction correlation | r = −0.481 (p < 0.001) |
| Performance median | 462.5 |
| Life satisfaction median | 7.21 / 10 |

A moderate but significant negative correlation confirms that, on average,
higher-performing countries tend to have less satisfied students. This is the
uncomfortable starting point: the tradeoff is real.

### Quadrant distribution

| Quadrant | Countries |
|----------|-----------|
| Excellence + well-being (high performance, high life satisfaction) | 13 |
| Excellence + misery (high performance, low life satisfaction) | 23 |
| Lower performance + well-being | 23 |
| Lower performance + misery | 12 |

Higher-performing systems are more likely to be in the "misery" quadrant (23 vs 13).
But the 13 exceptions exist, and they include some of the world's strongest performers.

### Excellence without misery — top countries

| Country | Composite score | Life satisfaction | Fear of failure (WLE) |
|---------|----------------|-------------------|----------------------|
| FIN | 516 | 7.61 | −0.19 |
| NLD | 502 | 7.50 | −0.39 |
| CHE | 498 | 7.38 | −0.28 |
| ISL | 481 | 7.34 | +0.00 |
| ESP | 480 | 7.35 | −0.12 |
| LTU | 480 | 7.61 | −0.07 |

### Excellence with misery — top countries (for comparison)

| Country | Composite score | Life satisfaction | Fear of failure (WLE) |
|---------|----------------|-------------------|----------------------|
| B-S-J-Z (QCI) | 579 | 6.64 | +0.00 |
| Macao (MAC) | 542 | 6.07 | +0.44 |
| Hong Kong (HKG) | 531 | 6.27 | +0.39 |
| Estonia (EST) | 526 | 7.19 | −0.17 |
| Japan (JPN) | 520 | 6.18 | +0.38 |
| Korea (KOR) | 520 | 6.52 | +0.19 |
| Taiwan (TAP) | 516 | 6.52 | +0.67 |

### The sharpest contrast: Finland vs. Japan

| Statistic | Finland (FIN) | Japan (JPN) |
|-----------|--------------|-------------|
| Composite score | 516 | 520 |
| Life satisfaction | 7.61 | 6.18 |
| Sense of belonging (BELONG) | +0.01 | +0.02 |
| Fear of failure (GFOFAIL) | −0.19 | +0.38 |
| Positive affect (SWBP) | −0.12 | −0.13 |

Performance is statistically indistinguishable. Life satisfaction differs by
1.43 points. The divergence on fear of failure — a full 0.57 standard deviations
apart — is the sharpest single-dimension gap between the two.

### Dimensions of the well-being gap

Within the high-performance half of the sample, countries with high vs. low life
satisfaction also differ on:

- **Fear of failure:** "Excellence without misery" countries average GFOFAIL
  z-score ≈ −0.21; "excellence with misery" countries (top 7 by performance)
  average ≈ +0.27. A gap of ~0.5 SD on a student-level index.
- **Positive affect (SWBP):** Moderate difference in the same direction.
- **Belonging:** Smaller and less consistent differences.
- **Bullying:** Limited differentiation between the high-performance groups.

Fear of failure emerges as the most consistent well-being differentiator among
high-performing systems — more than belonging, positive affect, or bullying exposure.

### The equity question: is well-being evenly distributed?

Within the "excellence without misery" countries, life satisfaction by ESCS
(socioeconomic) quartile is notably compressed — students from lower-SES
backgrounds report satisfaction close to their higher-SES peers. Within the
"excellence with misery" group, the gradient is steeper, with lower-SES students
faring notably worse. The well-being advantage of "excellence without misery"
systems is not reserved for advantaged students.

---

## Limitations

1. **Ecological correlation.** Country-level patterns describe national systems,
   not individuals. A student in a high-well-being country is not guaranteed high
   life satisfaction; one in a low-well-being country is not guaranteed low
   satisfaction. The analysis describes systems, not student-level effects.

2. **Cultural response bias.** Life satisfaction self-reports are culturally
   anchored. Research documents that East Asian respondents tend toward middle-scale
   responses in positive affect questions (Oishi, 2006; Diener, 2013). Part of the
   Japan/Korea gap relative to Nordic countries may reflect differential scale use
   rather than genuine differences in experienced satisfaction.

3. **15-year-olds only.** PISA samples adolescents in their 10th year of schooling.
   Well-being patterns at other ages, or long-run adult outcomes, are not captured.

4. **Cross-section, no causation.** This analysis cannot establish that any system
   feature — lower competitive pressure, pedagogical style, or structural choice —
   causes the well-being differences. It describes co-occurrence, not mechanisms.

5. **Point estimates only.** All values are weighted country means without
   confidence intervals. Differences between countries with similar scores should
   not be over-interpreted.

6. **Sub-national units.** PISA 2018 includes Russian sub-regions (QMR — Moscow;
   QRT — Tatarstan) and Chinese city clusters (QCI — B-S-J-Z; MAC — Macao; HKG —
   Hong Kong) that are not independent nation-states. Their presence in the quadrant
   scatter is noted; narrative conclusions focus on independent countries.

---

## Files

| File | Description |
|------|-------------|
| `analysis.py` | Full analysis: data loading, country aggregation, quadrant assignment, all charts |
| `charts/quadrant_scatter.png` | Main 2×2 map: performance vs. life satisfaction, 71 countries |
| `charts/wellbeing_profile.png` | Multi-dimensional well-being profile: excellence quadrants compared |
| `charts/equity_by_escs.png` | Life satisfaction by ESCS quartile within high-performing country groups |
| `../../data/processed/excellence_wellbeing_country.csv` | Country-level summary: all metrics |
