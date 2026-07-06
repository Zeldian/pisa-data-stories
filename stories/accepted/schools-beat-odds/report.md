# The Schools That Beat the Odds — Technical Report

**PISA 2018 — School equity analysis, 79 countries, 21,684 schools**

---

## Hypothesis

Some schools consistently help disadvantaged students outperform expectations based
on socioeconomic status. If true, a meaningful subset of low-SES schools should
achieve above-average academic results, and these schools should differ from their
peers in identifiable ways — not necessarily in their material resources, but in
their school environment and climate.

**Result: Confirmed, with an important nuance.** 16.9% of bottom-ESCS-tertile
schools achieve above their country's median performance (1,220 of 7,227
low-SES schools across 79 countries). The gap between these "odds-breaking" schools
and their peers is not explained by teacher qualifications or material resources.
It is explained by school climate: disciplinary structure (d = +0.58), student
belonging (d = +0.40), teacher support (d = +0.23).

---

## Method

### Data

- **Student questionnaire** (`SPSS_STU_QQQ.zip`): 597,625 students with valid ESCS
  and student weight after filtering. Variables: ESCS, 10 PVs × 3 domains (Math,
  Reading, Science), DISCLIMA, TEACHSUP, BELONG, PERFEED, EMOSUPS, W_FSTUWT.
- **School questionnaire** (`SPSS_SCH_QQQ.zip`): 21,903 schools. Variables:
  STAFFSHORT, EDUSHORT, STUBEHA, TEACHBEHA, STRATIO, PROATCE, SCHLTYPE, CREACTIV,
  SC064Q01TA, SC001Q01TA.

### School-level aggregation

For each school, compute weighted means (using `W_FSTUWT`) of ESCS, performance
composite, and student-reported climate indices (DISCLIMA, TEACHSUP, BELONG).
Performance composite = mean of 10 PVs across Math, Reading, and Science domains.

### Within-country OLS

For each country with ≥10 schools, fit OLS:  
`school_mean_perf ~ school_mean_ESCS`

This captures the country-specific SES gradient. Slope and R² summarise how strongly
socioeconomic composition predicts academic outcomes at the school level.

### "Odds-breaking" definition

- **Low-SES school**: school mean ESCS ≤ 33rd percentile of that country's school
  ESCS distribution.
- **Odds-breaking**: low-SES school AND school mean performance ≥ country median
  school performance.

This is the "cross-quadrant" criterion: a school that is socioeconomically
disadvantaged yet academically above average for its country. It is interpretable
without reference to a regression model and produces a meaningful base rate: if SES
and performance were uncorrelated, 50% of low-SES schools would qualify. With
median r = 0.71, only 16.9% do.

### School characteristics comparison

Merge school residuals with school questionnaire data (CNTSCHID key). For each
characteristic, compute standardized mean difference (Cohen's d) between
odds-breaking (n=1,220) and non-odds-breaking low-SES schools (n=6,007). Student-
reported variables (DISCLIMA, TEACHSUP, BELONG) are aggregated to school level
before merging. Significance tested with two-sample t-test.

---

## Key Results

### The SES gradient is universal and strong

| Statistic | Value |
|-----------|-------|
| Countries in analysis | 79 |
| Schools | 21,684 |
| Median school-level r (ESCS–performance) | 0.71 |
| Range of r across countries | 0.32 – 0.93 |

In every country in the sample, school ESCS is a strong positive predictor of
school performance. The weakest relationship (r = 0.32) is in Kazakhstan; the
strongest (r = 0.93) is in Bulgaria.

### 16.9% of low-SES schools beat the odds

| Group | N schools | % of low-SES |
|-------|-----------|--------------|
| Low-SES, odds-breaking (low ESCS + above-median performance) | 1,220 | 16.9% |
| Low-SES, expected (low ESCS + below-median performance) | 6,007 | 83.1% |
| Higher-SES (top two ESCS tertiles) | 14,457 | — |

If SES had no predictive power, 50% of low-SES schools would qualify. The actual
rate of 16.9% quantifies the odds these schools are beating.

### Country variation: 0% to 40%

| Top countries | % odds-breaking | Bottom countries | % odds-breaking |
|---------------|-----------------|------------------|-----------------|
| Macao (MAC) | 40.0% | Netherlands (NLD) | 0.0% |
| Albania (ALB) | 36.7% | Luxembourg (LUX) | 0.0% |
| Tatarstan region (QRT) | 35.4% | Brunei (BRN) | 0.0% |
| Norway (NOR) | 34.9% | France (FRA) | 3.6% |
| Iceland (ISL) | 34.0% | Hungary (HUN) | 3.8% |
| Estonia (EST) | 29.9% | Germany (DEU) | 4.1% |

Countries with the lowest rates — Netherlands, Luxembourg, Germany, France, Hungary
— share a structural feature: highly tracked school systems where students are sorted
into academic and vocational tracks at age 12–14. Within a tracked system, "low-SES"
schools in the PISA sample are predominantly vocational-track schools that, by
design, serve lower-performing students. The cross-track performance difference is
structural, not addressable school-by-school.

### What distinguishes odds-breaking schools

All ten school characteristics measured favoured odds-breaking schools. Six reached
statistical significance (p < 0.05):

| Characteristic | Cohen's d | Significant |
|----------------|-----------|-------------|
| Disciplinary climate (student-reported) | +0.584 | ✓ |
| Sense of belonging (student-reported) | +0.398 | ✓ |
| Student behaviour hindering learning | +0.239 | ✓ |
| Teacher support (student-reported) | +0.226 | ✓ |
| Parent–teacher meetings (% participating) | +0.135 | ✓ |
| Extra-curricular activities offered | +0.102 | ✓ |
| Staff shortage | +0.061 | – |
| Resource shortage | +0.053 | – |
| Teacher behaviour hindering learning | +0.049 | – |
| Proportion of certified teachers | −0.013 | – |

The pattern is consistent: **school climate and engagement variables are the
differentiating factors; resource and staffing variables are not.** Odds-breaking
schools do not have fewer staff shortages, better-qualified teachers, or more
educational materials — they have measurably better disciplinary structure, stronger
student belonging, and higher teacher support.

### The proportion of certified teachers is essentially identical

The Cohen's d for certified teacher proportion is −0.013 (p = 0.70): odds-breaking
and expected low-SES schools have statistically indistinguishable teacher
qualification profiles. This is the sharpest null result in the data: teacher
credentials do not explain school effectiveness in this context.

---

## Limitations

1. **School-level ecological analysis.** All characteristics comparisons are at the
   school level. Effects describe school-level patterns; individual student
   experiences will vary.

2. **Cross-sectional, no causal inference.** The comparison shows that odds-breaking
   schools score higher on climate variables. It does not establish that improving
   school climate causes performance gains. Selection effects are plausible (e.g.,
   more engaged families may choose certain schools).

3. **School questionnaire non-response.** The school questionnaire covers 21,903
   schools. Characteristics comparisons include all schools with matched school-Q
   data (~17,855). Non-response may introduce bias if certain school types are more
   likely to respond.

4. **Single cross-section.** A school that appears "odds-breaking" in 2018 may not
   be consistently so across years. Panel data would be needed to identify durably
   effective schools.

5. **Performance composite is approximate.** Using the mean of 10 PVs × 3 domains
   per student differs from full PISA statistical methodology (BRR standard errors,
   per-PV Rubin's rules). For school-level comparisons the approximation is adequate.

6. **Tracking confound.** In tracked systems, "low-SES school" in the PISA sample
   is often synonymous with "vocational-track school." The near-zero odds-breaking
   rates in NLD, LUX, DEU, FRA may reflect structural system design rather than
   school-level effectiveness failures.

---

## Files

| File | Description |
|------|-------------|
| `analysis.py` | Full analysis: data loading, school aggregation, OLS, classification, charts |
| `charts/school_scatter.png` | 6-country panel scatter (school ESCS vs performance, odds-breaking highlighted) |
| `charts/country_prevalence.png` | Country-level % of odds-breaking schools among low-SES schools |
| `charts/school_characteristics.png` | Cohen's d comparison: odds-breaking vs expected low-SES schools |
| `../../data/processed/schools_beat_odds.csv` | School-level summary: ESCS, performance, residuals, classification |
| `../../data/processed/schools_beat_odds_country.csv` | Country-level: N schools, % odds-breaking, OLS stats |
