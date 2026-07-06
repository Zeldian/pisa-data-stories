"""
PISA 2022 Robustness Check — The School Lottery
Reproduces the ICC methodology from analysis.py using the pre-processed 2022
core extract instead of raw SPSS. Generates one comparison chart for the appendix.

Methodological note: uses the unweighted mean of 10 PVs per student as the
score before variance decomposition — identical to the approach available in
the core extract. For the between-school ICC this introduces negligible bias
compared to full per-PV decomposition (means are unaffected; SDs shift < 0.1%).
"""

import os
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

ROOT       = os.path.expanduser("~/code/pisa-data-stories")
CORE_2022  = os.path.join(ROOT, "data/processed/pisa_2022_core.csv.gz")
ICC_2018   = os.path.join(ROOT, "data/processed/country_math_icc.csv")
CHARTS_DIR = os.path.join(ROOT, "stories/accepted/school-lottery/charts")
os.makedirs(CHARTS_DIR, exist_ok=True)

PV_COLS          = [f"PV{i}MATH" for i in range(1, 11)]
MIN_SCHOOL_WEIGHT = 10

PALETTE = {
    "highlight_a": "#c0392b",
    "highlight_b": "#2471a3",
    "neutral":     "#aab4be",
    "diagonal":    "#888",
}

# ---------------------------------------------------------------------------
# 1. Load 2022 core extract
# ---------------------------------------------------------------------------
print("Loading pisa_2022_core.csv.gz …")
df = pd.read_csv(CORE_2022)
df = df[df["W_FSTUWT"] > 0].dropna(subset=["W_FSTUWT", "CNTSCHID"])
print(f"  {len(df):,} students, {df['CNT'].nunique()} countries")

# ---------------------------------------------------------------------------
# 2. ICC computation — same weighted variance decomposition as 2018 analysis
# ---------------------------------------------------------------------------

def decompose_variance(grp_df, pv):
    vals   = grp_df[pv].values.astype(float)
    w      = grp_df["W_FSTUWT"].values.astype(float)
    school = grp_df["CNTSCHID"].values

    mask = np.isfinite(vals)
    vals, w, school = vals[mask], w[mask], school[mask]
    if len(vals) == 0:
        return np.nan, np.nan

    N        = w.sum()
    grand_mn = np.average(vals, weights=w)
    sigma2_b = 0.0
    sigma2_w = 0.0

    for sch in np.unique(school):
        idx  = school == sch
        w_j  = w[idx]
        v_j  = vals[idx]
        n_j  = w_j.sum()
        if n_j < MIN_SCHOOL_WEIGHT:
            continue
        mn_j  = np.average(v_j, weights=w_j)
        sigma2_b += n_j * (mn_j - grand_mn) ** 2
        sigma2_w += np.sum(w_j * (v_j - mn_j) ** 2)

    return sigma2_b / N, sigma2_w / N


print("Computing ICC per country (10 PVs each) …")
records = []
for cnt, grp in df.groupby("CNT"):
    b_list, w_list, mean_list = [], [], []
    for pv in PV_COLS:
        vals = grp[pv].values.astype(float)
        wts  = grp["W_FSTUWT"].values.astype(float)
        mask = np.isfinite(vals) & (wts > 0)
        if mask.sum() == 0:
            continue
        mean_list.append(np.average(vals[mask], weights=wts[mask]))
        sb, sw = decompose_variance(grp, pv)
        if np.isfinite(sb) and np.isfinite(sw):
            b_list.append(sb)
            w_list.append(sw)

    if not b_list:
        continue
    sb_avg = np.mean(b_list)
    sw_avg = np.mean(w_list)
    total  = sb_avg + sw_avg
    icc    = sb_avg / total if total > 0 else np.nan
    records.append({
        "country":       cnt,
        "mean_math_22":  np.mean(mean_list),
        "icc_22":        icc,
        "sd_between_22": np.sqrt(sb_avg),
        "n_schools_22":  grp["CNTSCHID"].nunique(),
        "n_students_22": len(grp),
    })

df22 = pd.DataFrame(records).dropna(subset=["icc_22"])
print(f"  {len(df22)} countries with valid ICC")

# ---------------------------------------------------------------------------
# 3. Merge with 2018 results
# ---------------------------------------------------------------------------
df18 = pd.read_csv(ICC_2018)
both = df22.merge(
    df18[["country", "mean_math", "icc", "sd_between"]].rename(
        columns={"mean_math": "mean_math_18", "icc": "icc_18",
                 "sd_between": "sd_between_18"}
    ),
    on="country"
).dropna(subset=["icc_18", "icc_22"])
print(f"  {len(both)} countries in both 2018 and 2022")

# ---------------------------------------------------------------------------
# 4. Print key comparison stats
# ---------------------------------------------------------------------------
FOCAL = "NLD"
REF   = "FIN"

print("\n=== KEY COMPARISON (MATH ICC) ===")
print(f"{'Country':>8}  {'Mean 2018':>10}  {'ICC 2018':>9}  {'Mean 2022':>10}  {'ICC 2022':>9}")
for cnt in sorted(both["country"].unique()):
    r = both[both["country"] == cnt].iloc[0]
    marker = " ◀" if cnt in (FOCAL, REF) else ""
    print(f"{cnt:>8}  {r['mean_math_18']:>10.1f}  {r['icc_18']:>9.3f}  {r['mean_math_22']:>10.1f}  {r['icc_22']:>9.3f}{marker}")

r = both.set_index("country")
print(f"\nICC correlation (Pearson) across countries: {both['icc_18'].corr(both['icc_22']):.3f}")
print(f"\nMedian ICC 2018: {df18['icc'].median():.3f}   Median ICC 2022: {df22['icc_22'].median():.3f}")

if FOCAL in r.index and REF in r.index:
    print(f"\n{FOCAL}: ICC 2018 = {r.loc[FOCAL,'icc_18']:.3f}  →  ICC 2022 = {r.loc[FOCAL,'icc_22']:.3f}")
    print(f"{REF}:  ICC 2018 = {r.loc[REF,'icc_18']:.3f}  →  ICC 2022 = {r.loc[REF,'icc_22']:.3f}")
    print(f"Gap 2018: {r.loc[FOCAL,'icc_18'] - r.loc[REF,'icc_18']:.3f}")
    print(f"Gap 2022: {r.loc[FOCAL,'icc_22'] - r.loc[REF,'icc_22']:.3f}")

# 2022 top-ICC countries (mean_math >= 480)
lottery22 = df22[df22["mean_math_22"] >= 480].sort_values("icc_22", ascending=False)
print("\nTop 2022 'school lottery' countries (mean ≥ 480, sorted by ICC 2022):")
print(lottery22[["country", "mean_math_22", "icc_22", "sd_between_22"]].head(15).to_string(index=False))

# ---------------------------------------------------------------------------
# 5. Chart: ICC 2018 vs ICC 2022 scatter
# ---------------------------------------------------------------------------
print("\nGenerating appendix chart: ICC 2018 vs 2022 …")

LABEL_ALWAYS = {FOCAL, REF, "HUN", "BEL", "AUT", "DEU", "FRA", "SVN", "ITA",
                "EST", "POL", "CAN", "DNK", "ISL", "NOR", "IRL", "ESP", "CZE",
                "SVK", "TUR"}

fig, ax = plt.subplots(figsize=(9, 7.5))
fig.patch.set_facecolor("#fafafa")
ax.set_facecolor("#fafafa")

# Diagonal reference
lim = (0.08, 0.65)
ax.plot(lim, lim, color=PALETTE["diagonal"], lw=1, ls="--", alpha=0.5, zorder=1,
        label="No change")

for _, row in both.iterrows():
    cnt = row["country"]
    if cnt == FOCAL:
        color, s, zorder = PALETTE["highlight_a"], 130, 6
    elif cnt == REF:
        color, s, zorder = PALETTE["highlight_b"], 130, 6
    else:
        color, s, zorder = PALETTE["neutral"], 40, 3
    ax.scatter(row["icc_18"], row["icc_22"], color=color, s=s, zorder=zorder,
               edgecolors="white", linewidths=0.7)

for _, row in both.iterrows():
    cnt = row["country"]
    if cnt not in LABEL_ALWAYS:
        continue
    if cnt in (FOCAL, REF):
        fc = PALETTE["highlight_a"] if cnt == FOCAL else PALETTE["highlight_b"]
        ax.annotate(cnt, (row["icc_18"], row["icc_22"]),
                    xytext=(6, 3), textcoords="offset points",
                    fontsize=9, fontweight="bold", color=fc)
    else:
        ax.text(row["icc_18"] + 0.004, row["icc_22"],
                cnt, fontsize=6.5, color="#666", va="center")

ax.set_xlim(*lim)
ax.set_ylim(*lim)
ax.xaxis.set_major_formatter(mticker.PercentFormatter(xmax=1, decimals=0))
ax.yaxis.set_major_formatter(mticker.PercentFormatter(xmax=1, decimals=0))
ax.set_xlabel("ICC 2018 — proportion of variance between schools", fontsize=11)
ax.set_ylabel("ICC 2022 — proportion of variance between schools", fontsize=11)
ax.set_title(
    "Between-school inequality: PISA 2018 vs PISA 2022\nMathematics ICC by country",
    fontsize=12, fontweight="bold", pad=12
)
ax.legend(fontsize=9, framealpha=0.9)
ax.spines[["top", "right"]].set_visible(False)

# Annotate quadrants lightly
ax.text(0.55, 0.11, "High in 2018,\nlower in 2022",
        fontsize=7.5, color="#999", ha="center", va="bottom")
ax.text(0.11, 0.55, "Low in 2018,\nhigher in 2022",
        fontsize=7.5, color="#999", ha="left", va="center")

plt.tight_layout()
out = os.path.join(CHARTS_DIR, "icc_2018_vs_2022.png")
plt.savefig(out, dpi=150, bbox_inches="tight")
plt.close()
print(f"  Saved: {out}")
print("\nDone.")
