# PISA 2018 Methodology Notes

These requirements apply to every analysis in this project. Violating any of them produces incorrect estimates or standard errors.

## 1. Use all 10 plausible values

PISA does not report a single student score. Each student has **10 plausible values** (PV1–PV10) per domain, drawn from the posterior distribution of their latent ability. They must all be used.

**Correct procedure:**
1. Run your analysis 10 times — once per plausible value.
2. Average the 10 point estimates (Rubin's rule for the mean).
3. Combine sampling variance (from replicate weights) and imputation variance (across PVs) to get the final standard error.

Never use a single PV as if it were a score. Doing so underestimates variance and produces biased regression coefficients.

**Variables:** `PV1MATH`–`PV10MATH`, `PV1READ`–`PV10READ`, `PV1SCIE`–`PV10SCIE`  
Reading subscales also have 10 PVs each (e.g., `PV1RTML`–`PV10RTML`).

## 2. Apply student weights for population estimates

Raw counts in PISA are not population-representative — sampling was stratified and unequal-probability. Always weight by `W_FSTUWT` when computing means, proportions, or counts that should represent the 15-year-old population.

School-level analyses use the school weight variable in the school file.

## 3. Use replicate weights for standard errors

`W_FSTURWT1`–`W_FSTURWT80` are 80 balanced repeated replication (BRR) replicate weights. They are the correct way to estimate standard errors that account for the complex stratified cluster sampling design.

**Procedure:** Apply the BRR formula — run the statistic 80 times (once per replicate weight), then compute the variance as `(1/20) * sum((estimate_r - estimate_full)^2)` across the 80 replicates.

Using `se = sd / sqrt(n)` is **wrong** for PISA data and will underestimate standard errors by ignoring clustering.

## 4. Benchmark against official estimates

Country-level means and standard errors published in the OECD PISA 2018 Results (Volumes I–V) are the authoritative reference. Replicate them before extending any analysis. If your means differ by more than 1–2 score points from the official figures, something is wrong with weighting or PV handling.

## 5. Missing data

PISA uses system-missing for skip patterns and out-of-scope items. Do not treat missing as zero. For items that were not administered (e.g., financial literacy questions only asked in participating countries), restrict the analysis to the relevant subsample.

## References

- OECD (2020). *PISA 2018 Technical Report*. OECD Publishing.
- OECD (2020). *PISA 2018 Data Analysis Manual: SPSS Users* (2nd ed.). OECD Publishing.
- Official PISA 2018 Results: https://www.oecd.org/pisa/publications/pisa-2018-results.htm
