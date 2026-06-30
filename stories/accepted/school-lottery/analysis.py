"""
PISA 2018 Story: The School Lottery
Hypothesis: National average PISA scores may conceal substantial between-school
variation. In some systems the school a student attends predicts achievement
as powerfully as the country's overall performance level.

Domain: Mathematics (PV1MATH–PV10MATH)
Key metric: Intraclass Correlation Coefficient (ICC) via weighted variance
decomposition — equivalent to the null-model ICC from multilevel modelling.

Methodology follows PISA 2018 Technical Report (Chapter 8, variance
decomposition). BRR SEs are omitted in this pilot; all values are point
estimates.
"""

import zipfile, tempfile, os
import numpy as np
import pandas as pd
import pyreadstat
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from scipy.stats import gaussian_kde

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
ROOT       = os.path.expanduser("~/code/pisa-data-stories")
RAW_ZIP    = os.path.join(ROOT, "data/raw/SPSS_STU_QQQ.zip")
PROC_DIR   = os.path.join(ROOT, "data/processed")
CHARTS_DIR = os.path.join(ROOT, "stories/accepted/school-lottery/charts")
os.makedirs(PROC_DIR,   exist_ok=True)
os.makedirs(CHARTS_DIR, exist_ok=True)

PV_COLS   = [f"PV{i}MATH" for i in range(1, 11)]
LOAD_COLS = ["CNT", "CNTSCHID"] + PV_COLS + ["W_FSTUWT"]
MIN_SCHOOL_WEIGHT = 10   # exclude schools with very few sampled students

PALETTE = {
    "highlight_a": "#c0392b",   # high-ICC country (warm red)
    "highlight_b": "#2471a3",   # low-ICC comparison country (blue)
    "neutral":     "#aab4be",
    "quad_line":   "#555",
}

# ---------------------------------------------------------------------------
# 1. Load data
# ---------------------------------------------------------------------------
print("Extracting student data…")
with zipfile.ZipFile(RAW_ZIP) as z:
    sav_name = [n for n in z.namelist() if n.endswith(".sav")][0]
    with tempfile.TemporaryDirectory() as tmpdir:
        z.extract(sav_name, tmpdir)
        sav_path = os.path.join(tmpdir, sav_name)
        print(f"  Reading {sav_name} (selected columns)…")
        df, _meta = pyreadstat.read_sav(sav_path, usecols=LOAD_COLS)

df = df.dropna(subset=["W_FSTUWT", "CNTSCHID"])
df = df[df["W_FSTUWT"] > 0]
print(f"Loaded {len(df):,} student rows, {df['CNT'].nunique()} countries.")

# ---------------------------------------------------------------------------
# 2. Variance decomposition per country
# ---------------------------------------------------------------------------

def decompose_variance(grp_df, pv):
    """
    Weighted between/within-school variance for one PV in one country.
    Returns (sigma2_b, sigma2_w) or (nan, nan) if insufficient data.
    """
    vals   = grp_df[pv].values.astype(float)
    w      = grp_df["W_FSTUWT"].values.astype(float)
    school = grp_df["CNTSCHID"].values

    # Drop missing PV values
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


print("Computing ICC for each country across 10 plausible values…")
records = []
for cnt, grp in df.groupby("CNT"):
    b_list, w_list, mean_list = [], [], []
    for pv in PV_COLS:
        vals = grp[pv].values.astype(float)
        wts  = grp["W_FSTUWT"].values.astype(float)
        mask = np.isfinite(vals) & (wts > 0)
        if mask.sum() == 0:
            continue
        mn = np.average(vals[mask], weights=wts[mask])
        mean_list.append(mn)

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

    n_schools = grp["CNTSCHID"].nunique()
    records.append({
        "country":   cnt,
        "mean_math": np.mean(mean_list),
        "sigma2_b":  sb_avg,
        "sigma2_w":  sw_avg,
        "sigma2_tot": total,
        "icc":       icc,
        "sd_total":  np.sqrt(total),
        "sd_between": np.sqrt(sb_avg),
        "n_schools": n_schools,
        "n_students": len(grp),
    })

summary = pd.DataFrame(records).dropna(subset=["icc"]) \
            .sort_values("icc", ascending=False) \
            .reset_index(drop=True)
summary.to_csv(os.path.join(PROC_DIR, "country_math_icc.csv"), index=False)
print(f"\nSummary: {len(summary)} countries")
print(summary[["country","mean_math","icc","sd_between","sd_total","n_schools"]].head(20).to_string(index=False))

# ---------------------------------------------------------------------------
# 3. Identify "school lottery" countries
# ---------------------------------------------------------------------------
MEAN_THRESHOLD = 480   # near OECD average
ICC_THRESHOLD  = 0.35  # high between-school variance

lottery = summary[(summary["mean_math"] >= MEAN_THRESHOLD) &
                  (summary["icc"]       >= ICC_THRESHOLD)].copy()
print(f"\n'School lottery' candidates (mean≥{MEAN_THRESHOLD}, ICC≥{ICC_THRESHOLD}):")
print(lottery[["country","mean_math","icc","sd_between","n_schools"]].to_string(index=False))

# Pick the most extreme: highest ICC among lottery countries
focal_cnt = lottery.iloc[0]["country"] if len(lottery) > 0 else summary.iloc[0]["country"]

# Pick a contrasting country: similar mean, low ICC
ref_row = summary[
    (np.abs(summary["mean_math"] - summary.loc[summary["country"]==focal_cnt,"mean_math"].values[0]) < 20) &
    (summary["icc"] < 0.20) &
    (summary["country"] != focal_cnt)
].nsmallest(1, "icc")
ref_cnt = ref_row["country"].values[0] if len(ref_row) > 0 else None

focal_stats = summary[summary["country"] == focal_cnt].iloc[0]
print(f"\nFocal country  : {focal_cnt}  (mean={focal_stats['mean_math']:.1f}, ICC={focal_stats['icc']:.3f})")
if ref_cnt:
    ref_stats = summary[summary["country"] == ref_cnt].iloc[0]
    print(f"Reference country: {ref_cnt}  (mean={ref_stats['mean_math']:.1f}, ICC={ref_stats['icc']:.3f})")


def weighted_school_means(cnt):
    """Return array of (school_mean, school_weight) for a country, using PV1."""
    grp = df[df["CNT"] == cnt]
    rows = []
    for sch, sg in grp.groupby("CNTSCHID"):
        v = sg["PV1MATH"].values.astype(float)
        w = sg["W_FSTUWT"].values.astype(float)
        mask = np.isfinite(v) & (w > 0)
        if mask.sum() == 0 or w[mask].sum() < MIN_SCHOOL_WEIGHT:
            continue
        mn  = np.average(v[mask], weights=w[mask])
        rows.append((mn, w[mask].sum()))
    means, weights = zip(*rows) if rows else ([], [])
    return np.array(means), np.array(weights)

# ---------------------------------------------------------------------------
# 4. Chart 1 — Scatter: national mean vs ICC (all countries)
# ---------------------------------------------------------------------------
print("\nGenerating Chart 1: mean vs ICC scatter…")

fig, ax = plt.subplots(figsize=(11, 7))
fig.patch.set_facecolor("#fafafa")
ax.set_facecolor("#fafafa")

# Quadrant reference lines
ax.axvline(MEAN_THRESHOLD, color=PALETTE["quad_line"], lw=0.8, ls="--", alpha=0.5)
ax.axhline(ICC_THRESHOLD,  color=PALETTE["quad_line"], lw=0.8, ls="--", alpha=0.5)

# Quadrant labels
ax.text(MEAN_THRESHOLD + 2,  ICC_THRESHOLD + 0.01, "School lottery\n(high mean, high ICC)",
        fontsize=8, color="#c0392b", fontweight="bold", va="bottom")
ax.text(MEAN_THRESHOLD + 2,  0.02, "Strong & equitable\n(high mean, low ICC)",
        fontsize=8, color="#1a7a4a", fontweight="bold", va="bottom")
ax.text(330,                 ICC_THRESHOLD + 0.01, "High inequality, low mean",
        fontsize=8, color="#888", va="bottom")
ax.text(330,                 0.02, "Uniform but low",
        fontsize=8, color="#888", va="bottom")

# All countries
for _, row in summary.iterrows():
    cnt = row["country"]
    if cnt == focal_cnt:
        color, zorder, s = PALETTE["highlight_a"], 6, 140
    elif cnt == ref_cnt:
        color, zorder, s = PALETTE["highlight_b"], 6, 140
    else:
        color, zorder, s = PALETTE["neutral"], 3, 45
    ax.scatter(row["mean_math"], row["icc"], color=color, s=s, zorder=zorder,
               edgecolors="white", linewidths=0.8)

# Country labels for highlighted pair
for cnt, color in [(focal_cnt, PALETTE["highlight_a"]), (ref_cnt, PALETTE["highlight_b"])]:
    if cnt is None:
        continue
    row = summary[summary["country"] == cnt].iloc[0]
    ax.annotate(cnt, (row["mean_math"], row["icc"]),
                xytext=(8, 4), textcoords="offset points",
                fontsize=9, fontweight="bold", color=color)

# Small labels for all others
for _, row in summary.iterrows():
    if row["country"] in (focal_cnt, ref_cnt):
        continue
    ax.text(row["mean_math"] + 1.5, row["icc"], row["country"],
            fontsize=5.5, color="#999", va="center")

ax.set_xlabel("Mean PISA Mathematics Score (weighted, 10 PVs)", fontsize=12)
ax.set_ylabel("ICC — Proportion of variance between schools", fontsize=12)
ax.set_title("National mean score vs. between-school inequality\nPISA 2018 Mathematics",
             fontsize=13, fontweight="bold", pad=14)
ax.yaxis.set_major_formatter(mticker.PercentFormatter(xmax=1, decimals=0))
ax.spines[["top","right"]].set_visible(False)
plt.tight_layout()
p = os.path.join(CHARTS_DIR, "mean_vs_icc_scatter.png")
plt.savefig(p, dpi=150, bbox_inches="tight")
plt.close()
print(f"  Saved: {p}")

# ---------------------------------------------------------------------------
# 5. Chart 2 — Distribution of school means: focal vs reference country
# ---------------------------------------------------------------------------
if ref_cnt:
    print("Generating Chart 2: school-mean distributions…")

    fig, axes = plt.subplots(1, 2, figsize=(12, 5.5), sharey=False)
    fig.patch.set_facecolor("#fafafa")

    score_range = np.linspace(100, 800, 1000)

    # Student-level KDE (PV1, weighted) — for backdrop
    def student_kde(cnt):
        grp = df[df["CNT"] == cnt]
        v = grp["PV1MATH"].values.astype(float)
        w = grp["W_FSTUWT"].values.astype(float)
        mask = np.isfinite(v) & (w > 0)
        w_n = w[mask] / w[mask].sum()
        return gaussian_kde(v[mask], weights=w_n, bw_method=0.15)

    for ax, cnt, color, label in [
        (axes[0], focal_cnt, PALETTE["highlight_a"], "School lottery"),
        (axes[1], ref_cnt,   PALETTE["highlight_b"], "More equitable"),
    ]:
        ax.set_facecolor("#fafafa")
        row = summary[summary["country"] == cnt].iloc[0]

        # Student distribution backdrop
        kde_stu = student_kde(cnt)
        dens_stu = kde_stu(score_range)
        dens_stu_norm = dens_stu / dens_stu.max()
        ax.fill_between(score_range, dens_stu_norm * 0.35, alpha=0.12, color=color)

        # School means
        sch_means, sch_wts = weighted_school_means(cnt)
        if len(sch_means) > 2:
            wn = sch_wts / sch_wts.sum()
            kde_sch = gaussian_kde(sch_means, weights=wn, bw_method=0.25)
            dens_sch = kde_sch(score_range)
            dens_sch_norm = dens_sch / dens_sch.max()
            ax.fill_between(score_range, dens_sch_norm, alpha=0.35, color=color)
            ax.plot(score_range, dens_sch_norm, color=color, lw=2.2)

        # Grand mean line
        ax.axvline(row["mean_math"], color=color, lw=1.5, ls="--", alpha=0.8)
        ax.text(row["mean_math"] + 4, 0.92,
                f"Mean\n{row['mean_math']:.0f}", fontsize=8, color=color, va="top")

        # ICC annotation
        ax.text(0.03, 0.97,
                f"ICC = {row['icc']:.2f}\nSD between schools = {row['sd_between']:.0f} pts",
                transform=ax.transAxes, fontsize=9, va="top",
                bbox=dict(boxstyle="round,pad=0.4", fc="white", ec=color, alpha=0.85))

        ax.set_title(f"{cnt} — {label}", fontsize=12, fontweight="bold", color=color, pad=10)
        ax.set_xlabel("PISA Mathematics Score", fontsize=11)
        ax.set_ylabel("Relative density (school means)", fontsize=10)
        ax.set_xlim(100, 800)
        ax.set_ylim(0, 1.1)
        ax.set_yticks([])
        ax.spines[["top","right","left"]].set_visible(False)

    fig.suptitle("Distribution of school means: same country, different schools\nPISA 2018 Mathematics",
                 fontsize=13, fontweight="bold", y=1.02)
    plt.tight_layout()
    p = os.path.join(CHARTS_DIR, "school_means_distribution.png")
    plt.savefig(p, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"  Saved: {p}")

# ---------------------------------------------------------------------------
# 6. Chart 3 — What the lottery means: school-mean percentiles vs country ranks
# ---------------------------------------------------------------------------
print("Generating Chart 3: lottery impact chart…")

sch_means_focal, sch_wts_focal = weighted_school_means(focal_cnt)

def wq(vals, wts, q):
    sorter = np.argsort(vals)
    v, w = vals[sorter], wts[sorter]
    cw = np.cumsum(w) / w.sum()
    return float(np.interp(q, cw, v))

p10_school = wq(sch_means_focal, sch_wts_focal, 0.10)
p90_school = wq(sch_means_focal, sch_wts_focal, 0.90)
p25_school = wq(sch_means_focal, sch_wts_focal, 0.25)
p75_school = wq(sch_means_focal, sch_wts_focal, 0.75)
median_school = wq(sch_means_focal, sch_wts_focal, 0.50)
mean_focal = summary[summary["country"]==focal_cnt]["mean_math"].values[0]

# Where would these school-mean scores rank among countries?
def country_rank(score, col="mean_math"):
    above = (summary[col] >= score).sum()
    return above

print(f"\n{focal_cnt} school mean percentiles (PV1, weighted):")
print(f"  P10 school: {p10_school:.0f}  -> ranked #{country_rank(p10_school)} of {len(summary)} countries")
print(f"  P25 school: {p25_school:.0f}")
print(f"  P50 school: {median_school:.0f}")
print(f"  P75 school: {p75_school:.0f}")
print(f"  P90 school: {p90_school:.0f}  -> ranked #{country_rank(p90_school)} of {len(summary)} countries")
print(f"  National mean: {mean_focal:.0f}  -> ranked #{country_rank(mean_focal)} of {len(summary)} countries")

# Chart: horizontal span showing school range vs country mean positions
fig, ax = plt.subplots(figsize=(11, 5.5))
fig.patch.set_facecolor("#fafafa")
ax.set_facecolor("#fafafa")

# Plot all country means as dots on a vertical axis
sorted_means = summary.sort_values("mean_math")
y_positions  = {row["country"]: i for i, (_, row) in enumerate(sorted_means.iterrows())}
n_countries  = len(sorted_means)

for _, row in sorted_means.iterrows():
    cnt = row["country"]
    if cnt == focal_cnt:
        ax.scatter(row["mean_math"], y_positions[cnt], color=PALETTE["highlight_a"],
                   s=80, zorder=5, edgecolors="white", lw=1)
        ax.text(row["mean_math"] + 2, y_positions[cnt], f"{cnt} (national mean)",
                fontsize=9, fontweight="bold", color=PALETTE["highlight_a"], va="center")
    else:
        ax.scatter(row["mean_math"], y_positions[cnt], color=PALETTE["neutral"],
                   s=20, zorder=3, alpha=0.7)

# Overlay school-mean range for focal country
ax.axvspan(p10_school, p90_school, alpha=0.12, color=PALETTE["highlight_a"],
           label=f"{focal_cnt} school P10–P90 range")
ax.axvspan(p25_school, p75_school, alpha=0.22, color=PALETTE["highlight_a"],
           label=f"{focal_cnt} school P25–P75 range")
ax.axvline(median_school, color=PALETTE["highlight_a"], lw=1.5, ls=":", alpha=0.9,
           label=f"{focal_cnt} median school")

# Bracket annotations
y_top = n_countries * 0.96
ax.annotate("", xy=(p90_school, y_top), xytext=(p10_school, y_top),
            arrowprops=dict(arrowstyle="<->", color=PALETTE["highlight_a"], lw=1.5))
ax.text((p10_school + p90_school)/2, y_top + 0.5,
        f"P10–P90 school range: {p90_school - p10_school:.0f} pts",
        ha="center", fontsize=9, color=PALETTE["highlight_a"], fontweight="bold")

ax.set_xlabel("PISA Mathematics Score", fontsize=12)
ax.set_ylabel("Countries ranked by national mean →", fontsize=10)
ax.set_title(
    f"The school lottery in {focal_cnt}: where would each school rank among nations?\nPISA 2018 Mathematics",
    fontsize=12, fontweight="bold", pad=12
)
ax.set_yticks([])
ax.legend(fontsize=9, loc="lower right", framealpha=0.9)
ax.spines[["top","right","left"]].set_visible(False)

plt.tight_layout()
p = os.path.join(CHARTS_DIR, "lottery_national_comparison.png")
plt.savefig(p, dpi=150, bbox_inches="tight")
plt.close()
print(f"  Saved: {p}")

# ---------------------------------------------------------------------------
# 7. Print key stats for report
# ---------------------------------------------------------------------------
print("\n=== KEY STATISTICS FOR REPORT ===")
print(f"Countries analysed: {len(summary)}")
print(f"ICC range: {summary['icc'].min():.3f} – {summary['icc'].max():.3f}")
print(f"Median ICC: {summary['icc'].median():.3f}")
print(f"\nFocal: {focal_cnt}")
for k in ["mean_math","icc","sd_between","sd_total","n_schools","n_students"]:
    print(f"  {k}: {focal_stats[k]:.2f}" if isinstance(focal_stats[k], float) else f"  {k}: {focal_stats[k]}")
if ref_cnt:
    print(f"\nReference: {ref_cnt}")
    for k in ["mean_math","icc","sd_between","sd_total","n_schools","n_students"]:
        print(f"  {k}: {ref_stats[k]:.2f}" if isinstance(ref_stats[k], float) else f"  {k}: {ref_stats[k]}")

print(f"\nSchool P10–P90 range ({focal_cnt}): {p10_school:.0f} – {p90_school:.0f} ({p90_school-p10_school:.0f} pts)")
print(f"National mean rank of {focal_cnt}: #{country_rank(mean_focal)} of {len(summary)}")
print(f"P10 school would rank: #{country_rank(p10_school)} of {len(summary)}")
print(f"P90 school would rank: #{country_rank(p90_school)} of {len(summary)}")
print("\nDone.")
