# The Hidden Underclass Inside Rich Education Systems — Technical Report

**PISA 2018 — 79 countries, 612,004 students**

---

## Hypothesis

High-performing or wealthy education systems may conceal a subgroup of students
carrying multiple serious burdens simultaneously. Country-level averages, by
definition, hide the distribution underneath them. A student who is bullied, lacks
a quiet place to study, has skipped school, feels they don't belong, and was recently
threatened — while also scoring far below their country's average — may be invisible
in every headline statistic their government publishes.

**Result: Confirmed.** 19.0% of students globally (16.5% within OECD) carry 3 or
more simultaneous hardship burdens. The variation within top-performing countries is
extreme: Korea 1.8%, Japan 6.4% vs New Zealand 25.1%, Canada 20.9%, UK 20.5%.
Each additional burden costs roughly 20–25 PISA points. Students carrying 4+ burdens
in OECD countries score 48 points below their zero-burden peers — almost a full year
of schooling.

---

## Hardship Index

Six binary indicators, each scored 0/1 per student. NaN treated as 0 (conservative).

| Indicator | Variable | Threshold | Global prevalence |
|-----------|----------|-----------|-------------------|
| Above-average bullying | BEINGBULLIED (WLE) | > 0 | 40.1% |
| Low sense of belonging | BELONG (WLE) | ≤ global 25th pct (−0.67) | 24.8% |
| No quiet study space | ST011Q03TA | == 2 (No) | 17.1% |
| No desk at home | ST011Q01TA | == 2 (No) | 16.6% |
| Skipped school | ST062Q01TA or ST062Q02TA | ≥ 2 (at least once/2 wks) | 31.0% |
| Threatened at school | ST038Q05NA | ≥ 2 (at least once/year) | 17.9% |

**Hardship count** = sum of all six indicators (0–6).
**Multi-burden**: count ≥ 3. **Severe burden**: count ≥ 4.

Variables not included due to coverage limitations:
- `FL156Q03TA` (paid work outside school): 79% missing — optional module
- `WB154Q07HA` (sleep problems): 65% missing — optional module
- `ST016Q01NA` (life satisfaction): 31% missing — administered in ~70% of countries
- Food insecurity: not directly measured in PISA 2018

---

## Key Results

### Global hardship distribution

| Burden count | % of students (weighted) |
|---|---|
| 0 | 30.2% |
| 1 | 27.3% |
| 2 | 20.1% |
| 3 | 12.7% |
| 4 | 6.8% |
| 5 | 2.3% |
| 6 | 0.5% |

**22.3% carry 3 or more burdens** (weighted global).

### Wide variation within top OECD performers

| Country | Academic | % Multi-burden (3+) | % Severe (4+) |
|---------|----------|---------------------|----------------|
| Estonia | 526 | 16.0% | 5.4% |
| Japan | 520 | **6.4%** | 1.6% |
| Korea | 520 | **1.8%** | 0.3% |
| Canada | 517 | 20.9% | 7.6% |
| Finland | 516 | 12.6% | 4.2% |
| Poland | 513 | 18.5% | 5.9% |
| Slovenia | 504 | 13.2% | 4.4% |
| UK | 503 | 20.5% | 7.6% |
| New Zealand | 503 | **25.1%** | 10.2% |
| Sweden | 503 | 11.3% | 3.9% |

Korea and Japan achieve top-tier academic results with very low multi-burden rates.
New Zealand, Canada, and UK achieve similar or lower academic results with 4–14×
higher multi-burden rates.

### The performance cliff

Each additional burden is associated with a measurable academic penalty:

| Burdens | Global mean | OECD mean |
|---------|-------------|-----------|
| 0 | 471 | 490 |
| 1 | 459 | 488 |
| 2 | 445 | 484 |
| 3 | 424 | 468 |
| 4 | 395 | 441 |
| 5 | 376 | 430 |
| 6 | 358 | 414 |

0→6 burdens: **−113 pts globally**, **−76 pts within OECD**. The step from 3→4
burdens is the steepest, consistent with a threshold effect where multiple serious
stressors become mutually compounding.

### ESCS gradient within rich systems

Within the top 15 OECD countries by academic performance, the SES gradient in
multi-burden rates is steep and universal. But the absolute rates for even the
wealthiest quartile (Q4) are substantial in several countries:

| Country | Q1 (lowest SES) | Q4 (highest SES) | Gap |
|---------|-----------------|------------------|-----|
| New Zealand | 35% | 14% | 21 pp |
| Australia | 34% | 18% | 16 pp |
| Canada | 31% | 15% | 16 pp |
| UK | 29% | 17% | 12 pp |
| Denmark | 19% | 8% | 11 pp |
| Finland | 20% | 10% | 10 pp |
| Estonia | 19% | 12% | 7 pp |
| Korea | 4% | <1% | 3 pp |

In New Zealand and Australia, 14–18% of even the wealthiest-quartile students carry
3+ simultaneous burdens. In Korea, the rate is below 1% at every SES level.

### Immigrant status

| Group | Multi-burden rate |
|-------|-------------------|
| Native | 23.5% |
| 2nd-gen immigrant | 19.4% |
| 1st-gen immigrant | 22.1% |

Immigrant status does not independently drive multi-burden rates — native students
globally carry slightly higher rates, likely because the immigrant-status indicator
conflates within-country and cross-country variation.

---

## Limitations

1. **NaN treated as 0.** Students with missing data on any indicator are assumed
   burden-free for that indicator. This understates the true hardship count for
   countries with high item non-response. All rates reported are lower bounds.

2. **Skipping threshold is low.** ST062Q01TA ≥ 2 = skipped at least one day in the
   past two weeks. This captures occasional, not chronic, absenteeism. A stricter
   threshold (≥ 3 = three or more days) would reduce the global prevalence to ~10%.

3. **BEINGBULLIED WLE threshold.** Using > 0 captures the upper ~40% of the
   distribution — students with above-average bullying experience. The WLE is designed
   so 0 is the cross-national mean; positive values indicate more bullying than
   average. A stricter threshold (> 1, approximately top 25%) would reduce the
   global rate.

4. **Cross-sectional, no causal inference.** Hardship indicators and academic
   performance are measured at the same point in time. The direction of causation
   between burden accumulation and academic underperformance cannot be established
   from this design.

5. **Food insecurity absent.** PISA 2018 does not include a direct food insecurity
   measure. This is a significant gap; hunger is likely the most acute single hardship
   for many students globally and its absence understates true hardship in all countries.

---

## Appendix — PISA 2022 Robustness Check

See `robustness_2022.py` and the online appendix.

---

## Files

| File | Description |
|------|-------------|
| `analysis.py` | Full analysis pipeline |
| `robustness_2022.py` | PISA 2022 cross-cycle check |
| `story.json` | Story metadata |
| `charts/burden_distribution.png` | Stacked bar: hardship distribution, top-20 countries |
| `charts/academic_vs_hardship.png` | Scatter: academic performance vs % multi-burden |
| `charts/performance_cliff.png` | Line: academic score by burden count |
| `charts/hidden_underclass_escs.png` | Bar: multi-burden by ESCS quartile, top-15 OECD |
| `../../data/processed/hidden_underclass_country.csv` | Country-level results |
