# Calculators, Creators, or Both? — Technical Report

**PISA 2022 — Creative Thinking domain, 63 countries, 499,843 students**

---

## Hypothesis

Countries with the strongest academic performance (Math, Reading, Science) also achieve
the strongest creative thinking results. If this is true, the common narrative that
academic rigor comes at the cost of creativity is wrong — and the interesting question
becomes *why* the two align so closely.

**Result: Strongly confirmed.** The country-level Pearson correlation between academic
performance and Creative Thinking (CT) is r = 0.922 (p < 0.001). After controlling for
national socioeconomic status (ESCS), the partial correlation is r = 0.820 — still
among the strongest cross-domain relationships in comparative education research.
Nearly all countries fall on the diagonal: 30 "Both" (high academic + high CT) and
29 "Low Both", with only 2 "Calculators" (high academic, lower CT) and 2 "Creators"
(lower academic, higher CT).

---

## Data

- **Creative Thinking PVs**: `PV1CRTH_NC`–`PV10CRTH_NC` from `CRT_SPSS.zip`
  (`CY08MSP_CRT_COG.SAV`). Scale: PISA CT scale (0–48+). 499,843 students, 63
  countries. CT was an optional domain in 2022; these 63 countries opted in.
- **Academic PVs + weights**: `PV1MATH`–`PV10MATH`, `PV1READ`–`PV10READ`,
  `PV1SCIE`–`PV10SCIE`, plus `W_FSTUWT` and `ESCS`, loaded from `STU_QQQ_SPSS.zip`.
- **Context variables**: `CREATSCH`, `CREATEFF`, `CREATACT`, `CREATOR`, `CREATOPN`,
  `TEACHSUP`, `BELONG`, `DISCLIM` — from QQQ file, joined via CNTSTUID.
- **Join**: CRT ← QQQ on `CNTSTUID`. No weight missing (0 missing after join).
  Filter: W_FSTUWT > 0, non-NaN on CT PV1 and Math PV1.

---

## Method

### Score computation

- **Academic performance**: mean of 10 PVs × 3 domains (Math, Reading, Science)
  per student, then averaged: `(math_score + read_score + scie_score) / 3`.
- **CT performance**: mean of `PV1CRTH_NC`–`PV10CRTH_NC` per student.
- **Country-level means**: weighted by `W_FSTUWT`, dropping NaN and w ≤ 0.

### Quadrant assignment

- Medians computed over the 63-country distribution: CT median = 28.7,
  academic median = 439.1.
- **Both**: country mean CT ≥ median AND academic ≥ median.
- **Calculators**: academic ≥ median, CT < median.
- **Creators**: CT ≥ median, academic < median.
- **Low Both**: both below median.

### ESCS control

Partial correlation of CT and academic, removing the linear effect of ESCS via
residuals from OLS. Done on the 62-country subset with valid ESCS (Costa Rica missing).

### Context variable comparisons

Student-level Cohen's d between "Both" and "Low Both" country students, for each
context index. Significance via Welch's t-test.

---

## Key Results

### The diagonal is the story

| Statistic | Value |
|-----------|-------|
| Countries | 63 |
| Students | 499,843 |
| CT–Academic correlation | **r = 0.922** |
| Partial r (controlling ESCS) | **r = 0.820** |
| ESCS–Academic r | 0.755 |
| ESCS–CT r | 0.768 |

The correlation is near-perfect. Countries that do well academically do well creatively;
countries that struggle academically struggle creatively. The 2×2 map is mostly diagonal.

### Quadrant distribution

| Quadrant | Countries | N |
|----------|-----------|---|
| Both (high academic + high CT) | Singapore, Korea, Estonia, Canada, Australia, Finland, New Zealand, Poland, Czechia, Denmark, Belgium, Slovenia, Latvia, Germany, Netherlands, France, Portugal, Spain, Hungary, Lithuania, Italy, Croatia, Israel, Malta, Slovakia, Iceland, Serbia, Macao, Hong Kong, Chinese Taipei | 30 |
| Low Both | Greece, Romania, UAE, Uruguay, Qatar, Bulgaria, Moldova, Kazakhstan, Mongolia, Malaysia, Costa Rica, Peru, Colombia, Brazil, Jamaica, Thailand, Saudi Arabia, Baku (AZE), Panama, N. Macedonia, Indonesia, Albania, Palestine, El Salvador, Jordan, Morocco, Philippines, Uzbekistan, Dominican Rep. | 29 |
| Calculators | Tatarstan (QUR), Brunei | 2 |
| Creators | Chile, Mexico | 2 |

### The East Asian "calculator" narrative is wrong

Singapore (CT = 41.0), Korea (CT = 38.1), Canada (CT = 37.9), and Australia (CT = 37.3)
are the four highest CT scorers. East Asian systems routinely associated with academic
pressure and rote learning — Singapore, Korea, Hong Kong, Macao, Chinese Taipei — are
all in the "Both" quadrant. The data does not support the idea that academic excellence
in East Asia comes at the cost of creative thinking performance.

### The Creative Paradox

Despite producing the highest CT outcomes, students in high-performing countries
consistently *self-report lower creative identity, openness, and activities* than
students in low-performing countries.

| Variable | Cohen's d (Both vs Low Both) | Direction |
|----------|------------------------------|-----------|
| Creative identity | **−0.532** | High-performing → lower |
| Creative openness | −0.523 | High-performing → lower |
| Creative activities (overall) | −0.454 | High-performing → lower |
| Creative activities at school | −0.288 | High-performing → lower |
| Teacher support | −0.304 | High-performing → lower |
| Creative self-efficacy | −0.124 | High-performing → lower |
| Sense of belonging | +0.149 | High-performing → higher |
| Disciplinary climate | −0.013 | No difference |

Country-level: Creative self-efficacy correlates r = −0.34 with CT score and
r = −0.49 with academic performance. Panama, Albania, and Colombia top the
self-reported creative confidence ranking — and score near the bottom of CT.

The most plausible interpretation is **social calibration**: in countries where creative
achievement is widespread and visible, students compare themselves to a higher standard
and rate their own creativity lower. A child in Finland surrounded by creative peers may
feel less exceptional than a child in Albania with fewer reference points. The measured
output (CT score) and the self-perception (creative identity) are measuring genuinely
different things.

---

## Limitations

1. **CT scale differs from academic scale.** The PISA CT scale (0–48+) is not
   directly comparable in absolute terms to the 300–600 PISA academic scale. Both
   are properly calibrated IRT scores; the correlation analysis is valid.

2. **63 countries, not 79+.** Creative Thinking was an optional domain. Countries
   that opted in may not be representative of all PISA participants. Notably, Japan
   and the United Kingdom are absent.

3. **CNTSTUID join assumes uniqueness.** CNTSTUID is assumed to uniquely identify
   students across the QQQ and CRT files. No duplicates were found in the merge.

4. **Context variable confound.** The "Both vs Low Both" comparison conflates
   country effects with within-country student-level variation. Countries in each
   quadrant differ on income, culture, and education system — any one variable
   should not be interpreted causally.

5. **ESCS partial correlation is country-level.** The partial r = 0.820 is computed
   on 62 country means. Individual-level ESCS effects may differ.

---

## Files

| File | Description |
|------|-------------|
| `analysis.py` | Full analysis: data loading, join, country means, quadrants, charts |
| `story.json` | Story metadata |
| `report.md` | This document |
| `charts/country_scatter.png` | Main scatter: academic vs CT, r = 0.922, quadrant coloring |
| `charts/creative_paradox.png` | Creative self-efficacy vs CT/academic — the inverse relationship |
| `charts/both_vs_low.png` | Cohen's d: Both vs Low Both on creative + climate variables |
| `../../data/processed/calculators_creators_country.csv` | Country-level results |
