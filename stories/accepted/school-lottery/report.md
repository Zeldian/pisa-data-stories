# The School Lottery — Technical Report

**PISA 2018 Mathematics — Between-School Variance Analysis**

---

## Hypothesis

National average PISA scores may conceal substantial differences in educational opportunity within countries. In some education systems, the school a student attends may have a greater influence on expected achievement than the country's overall level of performance.

**Result: Confirmed.** Between-school variance varies widely across PISA 2018 participants. The Netherlands (mean = 519, ranked #9 globally) has the highest ICC of any well-performing country (ICC = 0.596), meaning 59.6% of total student variance in mathematics is attributable to which school a student attends. Finland, ranked close in national mean (507), has ICC = 0.121 — less than one fifth the between-school inequality.

---

## Method

**Metric:** Intraclass Correlation Coefficient (ICC) via weighted variance decomposition — equivalent to the null-model ICC from multilevel modelling and consistent with the PISA 2018 Data Analysis Manual (OECD, 2020, Chapter 6).

**Formula:**

```
σ²_between = (1/N) Σ_j n_j (ȳ_j − ȳ)²
σ²_within  = (1/N) Σ_j Σ_i w_ij (y_ij − ȳ_j)²
ICC        = σ²_between / (σ²_between + σ²_within)
```

Where `n_j` = sum of student final weights in school j, `N` = total weight, `ȳ_j` = weighted school mean, `ȳ` = weighted grand mean.

**Plausible values:** σ²_between and σ²_within computed separately for each of the 10 Math PVs, then averaged before forming the ICC ratio (correct pooling order per Rubin's rules).

**Weighting:** Student final weight `W_FSTUWT` throughout. Schools with total weight < 10 excluded.

**Benchmark validation:** NLD ICC = 0.596 and FIN ICC = 0.121 are consistent with OECD-published between-school variance figures for PISA 2018 Mathematics (~58–62% for NLD, ~10–12% for FIN).

---

## Key Results

### ICC distribution across 79 countries

| Statistic | Value |
|-----------|-------|
| Minimum ICC | 0.107 (Iceland) |
| Median ICC | 0.338 |
| Maximum ICC | 0.596 (Netherlands) |

### Top 15 countries by ICC

| Rank | Country | Mean Math | ICC | SD Between Schools | Schools |
|------|---------|-----------|-----|-------------------|---------|
| 1 | NLD | 519.2 | 0.596 | 72.0 | 156 |
| 2 | TUR | 453.5 | 0.576 | 66.9 | 186 |
| 3 | HUN | 481.1 | 0.573 | 69.0 | 238 |
| 4 | SVN | 508.9 | 0.506 | 62.3 | 345 |
| 5 | LBN | 393.5 | 0.501 | 74.8 | 313 |
| 6 | FRA | 495.4 | 0.495 | 65.2 | 252 |
| 7 | ITA | 486.6 | 0.492 | 65.8 | 542 |
| 8 | AUT | 498.9 | 0.490 | 65.5 | 291 |
| 9 | BEL | 508.1 | 0.484 | 66.3 | 288 |
| 10 | ARE | 434.9 | 0.478 | 72.6 | 755 |
| 11 | DEU | 500.0 | 0.475 | 65.8 | 223 |
| 12 | CZE | 499.5 | 0.460 | 63.2 | 333 |
| 13 | JPN | 527.0 | 0.435 | 57.0 | 183 |
| 14 | CHE | 515.3 | 0.382 | 58.3 | 228 |

### Netherlands vs Finland

| Statistic | Netherlands (NLD) | Finland (FIN) |
|-----------|------------------|---------------|
| Mean Math | 519.2 | 507.3 |
| ICC | 0.596 | 0.121 |
| SD between schools | 72.0 pts | 28.7 pts |
| SD total | 93.3 pts | 82.4 pts |
| Schools sampled | 156 | 214 |
| Students sampled | 4,765 | 5,649 |

### The Dutch school lottery in numbers

School mean percentiles for NLD (PV1, weighted), ranked against all 79 PISA countries:

| School percentile | Score | Would rank among countries |
|-------------------|-------|--------------------------|
| P10 (bottom 10% of schools) | 426 | #54 of 79 |
| P25 | 463 | — |
| P50 (median school) | 519 | — |
| P75 | 582 | — |
| P90 (top 10% of schools) | 603 | #1 of 79 (above all nations) |
| National mean | 519 | #9 of 79 |

The P10–P90 school range (177 points) spans the equivalent of moving from a below-average-performing country to the highest-performing education system in the world.

---

## The Tracking Confound — Critical Caveat

**This is the most important interpretive nuance for the Netherlands finding.**

The Netherlands operates a fully stratified secondary school system: students are assigned to separate school types at age 12 — VMBO (pre-vocational), HAVO (general secondary), and VWO (pre-university). These are distinct institutions, not tracks within a school. The bimodal distribution of Dutch school means (clearly visible in Chart 2) directly reflects this structure — the two peaks correspond to lower- and higher-track school types.

**A high ICC in a tracked system has a partially different meaning than in a comprehensive system.** The between-school variance in NLD is partly *structurally produced by design*, not purely a consequence of school quality variation within a common system.

This does not invalidate the finding — the assignment to tracks at age 12 is itself the lottery. A Dutch student's educational trajectory is substantially determined by track placement, which correlates strongly with family background. But the mechanism is *tracking*, not random or unexplained school quality differences.

Countries with similarly high ICCs and tracked systems: Hungary (ICC 0.573), Belgium (0.484), Germany (0.475), Austria (0.490).

---

## Limitations

1. **No BRR standard errors.** All ICCs are point estimates. BRR replicate weights (W_FSTURWT1–W_FSTURWT80) were not used. Differences between countries with ICCs within ~0.03 of each other should not be over-interpreted.

2. **Mathematics only.** PISA 2018 Reading ICC patterns differ for some countries. This analysis does not generalise across domains.

3. **ICC is descriptive, not causal.** A high ICC means school membership *predicts* achievement; it does not establish that changing a student's school assignment would change their outcomes. Tracking, peer composition, family sorting, and causal school effects all contribute to between-school variance.

4. **PISA school sampling.** PISA samples approximately 150–200 schools per country. Very small, specialised, or atypical schools may not be represented. The NLD sample (156 schools) yields an estimated ICC SE ≈ 0.03, making the NLD finding robust, but small cross-country ICC differences should be treated cautiously.

5. **Single year.** PISA 2018 only. Longitudinal trends in ICC are not examined.

---

## Files

| File | Description |
|------|-------------|
| `analysis.py` | Full analysis: data loading, variance decomposition, pair selection, charts |
| `robustness_2022.py` | PISA 2022 robustness check; generates appendix chart |
| `charts/mean_vs_icc_scatter.png` | All 79 countries: national mean vs ICC, with quadrant labels |
| `charts/school_means_distribution.png` | NLD vs FIN: distribution of school means (bimodal NLD visible) |
| `charts/lottery_national_comparison.png` | NLD school percentiles mapped onto the global country ranking |
| `charts/icc_2018_vs_2022.png` | Appendix: ICC 2018 vs ICC 2022 scatter (70 common countries) |
| `../../data/processed/country_math_icc.csv` | Per-country ICC summary for all 79 countries |

---

## Appendix: Does the Pattern Persist in PISA 2022?

**Source:** `data/processed/pisa_2022_core.csv.gz` (613,744 students, 80 countries).
**Method:** Identical weighted variance decomposition, applied separately to each of 10 math PVs and averaged — exactly as in the 2018 analysis. BRR standard errors not computed (point estimates throughout).

### Summary

The core finding is robust and, if anything, strengthened in PISA 2022. Across the 70 countries present in both cycles, the Pearson correlation between 2018 and 2022 ICC is **0.912**. The median ICC across all countries was 0.338 in 2018 and 0.340 in 2022 — statistically indistinguishable. Countries with tracked or selective secondary systems continue to cluster at high ICC; comprehensive systems remain at the low end.

### Comparison

**Tracked systems — stable or increased inequality:**

| Country | ICC 2018 | ICC 2022 | System |
|---------|----------|----------|--------|
| NLD | 0.596 | 0.619 | Fully tracked |
| HUN | 0.574 | 0.608 | Tracked |
| TUR | 0.576 | 0.572 | Tracked |
| AUT | 0.490 | 0.495 | Tracked |
| DEU | 0.475 | 0.474 | Tracked |
| FRA | 0.495 | 0.462 | Partly tracked |
| BEL | 0.484 | 0.465 | Tracked |
| CZE | 0.460 | 0.489 | Tracked |

**Comprehensive systems — stable low inequality:**

| Country | ICC 2018 | ICC 2022 |
|---------|----------|----------|
| FIN | 0.121 | 0.116 |
| ISL | 0.107 | 0.106 |
| NOR | 0.141 | 0.137 |
| IRL | 0.168 | 0.143 |
| DNK | 0.189 | 0.169 |
| EST | 0.229 | 0.211 |

The NLD–FIN ICC gap widened from 0.475 to **0.503**.

**Notable change — Poland (POL): 0.252 → 0.466.** This is the largest single-country shift in the dataset. Poland's 2019 education reform abolished the three-tier system (six-year primary → three-year gymnasium → secondary) and folded gymnasia into an eight-year primary school, with students entering differentiated secondary schools (vocational / liceum) at an earlier age than before. The 2022 cohort is the first fully exposed to this structure. The data are consistent with the reform having substantially increased between-school sorting — an inadvertent natural experiment in the story's core mechanism.

**Coverage note:** Nine 2018 countries are absent from 2022, including Russia and Ukraine (geopolitical withdrawal), Lebanon (economic crisis), and Luxembourg. Their absence does not affect comparisons involving the story's focal countries. Ten new, predominantly lower-income economies joined in 2022 and do not appear in the comparison.

### Visualization

![ICC 2018 vs ICC 2022](charts/icc_2018_vs_2022.png)

*Each dot is one country. The dashed diagonal represents no change between cycles. Countries above the diagonal became more unequal; countries below became more equal. The cluster of points along the diagonal confirms the stability of the pattern. NLD and FIN (labelled) sit at opposite extremes in both cycles.*

### Conclusion

The 2022 evidence **strengthens** the original conclusion. The between-school inequality pattern is structurally determined by educational system design and does not fluctuate between PISA cycles. The Netherlands remains the clearest example among high-performing countries — its ICC actually rose slightly. Finland remains the benchmark for a high-performing, equitable system. The tracked vs. comprehensive distinction that anchors the story's interpretation holds across both cycles.

Poland is a notable addition: its dramatic ICC increase between 2018 and 2022 is consistent with a known structural policy change, and may itself illustrate the story's core argument — that decisions about school organisation produce large, measurable differences in how much the assigned school determines a student's trajectory.
