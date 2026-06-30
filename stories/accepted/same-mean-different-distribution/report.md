# Same Average, Different Distribution

**PISA 2018 Reading — Lebanon vs Kosovo**

---

## Hypothesis

Two countries can have nearly identical average PISA scores while having fundamentally different distributions of student performance.

**Result: Confirmed.** Lebanon (LBN) and Kosovo (KSV) had essentially the same average PISA Reading score in 2018 — differing by less than one point — yet their distributions of student performance were strikingly different.

---

## Key Finding

| Statistic | Lebanon | Kosovo |
|-----------|---------|--------|
| Mean (10 PVs, weighted) | 353.4 | 353.1 |
| Standard deviation | 113.3 | 68.3 |
| P10 (bottom 10%) | 211 | 265 |
| P25 | 268 | 304 |
| Median (P50) | 347 | 352 |
| P75 | 434 | 398 |
| P90 (top 10%) | 507 | 442 |
| P90–P10 range | 296 | 177 |
| % below PISA Level 1b (< 407) | 67.6% | 78.6% |
| % at Level 5+ (≥ 626) | 0.7% | 0.0% |

**The distributions cross near the median.** Kosovo's bottom students outperform Lebanon's bottom students (P10: 265 vs 211), but Lebanon's top students comfortably outperform Kosovo's top students (P90: 507 vs 442). Neither country's education system is better in every respect — they are differently structured.

### What this looks like

- **Lebanon**: A wide, flat distribution spanning from very low to moderately high scores. The system is highly stratified. A small minority of students reaches respectable performance levels, while the majority score very poorly. The standard deviation (113 points) is among the highest of any PISA 2018 participant.

- **Kosovo**: A narrow, concentrated distribution. Almost all students perform in a tight band around the low-average. There is very little differentiation — few students reach higher levels, but also fewer fall to the extreme bottom. Kosovo's system is more uniform, though uniformly low.

### The landscape context

Across all 79 PISA 2018 countries, there is no strong relationship between a country's average score and its performance spread. Lebanon is a clear outlier — the country with the highest spread among all low-scoring nations. Kosovo sits at the opposite extreme for its score range. On the scatter plot of mean vs. P90–P10 range, both countries occupy almost the same horizontal position (same mean) but very different vertical positions (different spread).

---

## Methods

- **Domain**: PISA 2018 Reading (primary domain)
- **Sample**: All 612,004 students across 79 countries; Lebanon n=10,035; Kosovo n=4,798
- **PV handling**: All 10 plausible values used; means and percentiles computed per PV and averaged (Rubin's rule for point estimates)
- **Weighting**: Student final weight `W_FSTUWT` applied to all statistics
- **Pair selection**: Countries were ranked by mean; pairs within 5 score points of each other were compared by P90–P10 range; the pair with the greatest range difference was selected
- **KDE bandwidth**: 0.15 (Scott's rule starting point, tightened slightly)

---

## Limitations

- **No BRR standard errors**: This pilot does not compute BRR standard errors. Means should be treated as point estimates, not benchmarks for significance testing. Mean differences of less than ~5 points between countries are generally within the margin of error.
- **Single domain**: The finding is for Reading only. The pattern may differ in Mathematics or Science.
- **No causal interpretation**: This analysis describes distributions; it does not explain why they differ. Plausible factors for Lebanon (private/public school divide, socioeconomic stratification, displacement) and Kosovo (post-conflict education reconstruction, limited school quality variation) are not tested here.
- **Country codes**: PISA uses `KSV` for Kosovo and `LBN` for Lebanon. These correspond to the OECD's standard participant codes.

---

## Files

| File | Description |
|------|-------------|
| `analysis.py` | Full analysis script — loads data, computes statistics, selects pair, generates all charts |
| `charts/density_comparison.png` | Overlapping weighted KDE curves for Lebanon and Kosovo |
| `charts/percentile_bars.png` | P10/P25/P50/P75/P90 side-by-side bar chart |
| `charts/landscape_scatter.png` | All 79 countries: mean score vs. P90–P10 spread |
| `../../data/processed/country_reading_summary.csv` | Per-country summary statistics for all 79 countries |
