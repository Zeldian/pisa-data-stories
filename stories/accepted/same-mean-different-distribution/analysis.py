"""
PISA 2018 Story: Same Mean, Different Distribution
Hypothesis: Two countries can have nearly identical average PISA scores while
having fundamentally different distributions of student performance.

Domain: Reading (primary domain in PISA 2018)
Methodology: Correct PV pooling (Rubin's rules for means), weighted percentiles.
BRR standard errors are omitted in this pilot; means are labelled as point
estimates and not used for significance testing.
"""

import zipfile
import tempfile
import os
import numpy as np
import pandas as pd
import pyreadstat
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from scipy.stats import gaussian_kde

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
ROOT = os.path.expanduser("~/code/pisa-data-stories")
RAW_ZIP = os.path.join(ROOT, "data/raw/SPSS_STU_QQQ.zip")
PROCESSED_DIR = os.path.join(ROOT, "data/processed")
CHARTS_DIR = os.path.join(ROOT, "stories/accepted/same-mean-different-distribution/charts")
os.makedirs(PROCESSED_DIR, exist_ok=True)
os.makedirs(CHARTS_DIR, exist_ok=True)

PV_COLS = [f"PV{i}READ" for i in range(1, 11)]
LOAD_COLS = ["CNT"] + PV_COLS + ["W_FSTUWT"]

# ---------------------------------------------------------------------------
# 1. Load data (select columns only)
# ---------------------------------------------------------------------------
print("Extracting SPSS file from zip...")
with zipfile.ZipFile(RAW_ZIP) as z:
    sav_name = [n for n in z.namelist() if n.endswith(".sav")][0]
    print(f"  Found: {sav_name}")
    with tempfile.TemporaryDirectory() as tmpdir:
        z.extract(sav_name, tmpdir)
        sav_path = os.path.join(tmpdir, sav_name)
        print("  Reading SPSS file (selecting columns)...")
        df, meta = pyreadstat.read_sav(sav_path, usecols=LOAD_COLS)

print(f"Loaded {len(df):,} student rows across {df['CNT'].nunique()} countries.")

# ---------------------------------------------------------------------------
# 2. Per-country weighted statistics
# ---------------------------------------------------------------------------

def weighted_quantile(values, weights, quantiles):
    """Weighted quantile via sorted cumulative weight."""
    values = np.asarray(values, dtype=float)
    weights = np.asarray(weights, dtype=float)
    mask = np.isfinite(values) & np.isfinite(weights) & (weights > 0)
    values, weights = values[mask], weights[mask]
    if len(values) == 0:
        return np.full(len(quantiles), np.nan)
    sorter = np.argsort(values)
    values, weights = values[sorter], weights[sorter]
    cumw = np.cumsum(weights)
    cumw /= cumw[-1]
    return np.interp(quantiles, cumw, values)

def weighted_mean(values, weights):
    mask = np.isfinite(values) & np.isfinite(weights) & (weights > 0)
    if mask.sum() == 0:
        return np.nan
    return np.average(values[mask], weights=weights[mask])

def weighted_std(values, weights):
    mask = np.isfinite(values) & np.isfinite(weights) & (weights > 0)
    if mask.sum() == 0:
        return np.nan
    v, w = values[mask], weights[mask]
    m = np.average(v, weights=w)
    variance = np.average((v - m) ** 2, weights=w)
    return np.sqrt(variance)

QUANTILES = [0.10, 0.25, 0.50, 0.75, 0.90]

print("Computing per-country statistics across 10 plausible values...")
records = []
for cnt, grp in df.groupby("CNT"):
    w = grp["W_FSTUWT"].values
    # Pool across PVs (Rubin's rules: average point estimates)
    pv_means  = [weighted_mean(grp[pv].values, w) for pv in PV_COLS]
    pv_stds   = [weighted_std(grp[pv].values, w) for pv in PV_COLS]
    pv_quants = [weighted_quantile(grp[pv].values, w, QUANTILES) for pv in PV_COLS]

    mean = np.mean(pv_means)
    sd   = np.mean(pv_stds)
    q    = np.mean(pv_quants, axis=0)  # averaged across 10 PVs

    # Proportion below 407 (PISA Level 1b lower boundary ≈ below basic)
    # and above 625 (Level 5 lower boundary)
    pv_below400 = [weighted_mean((grp[pv].values < 407).astype(float), w) for pv in PV_COLS]
    pv_above600 = [weighted_mean((grp[pv].values >= 626).astype(float), w) for pv in PV_COLS]

    records.append({
        "country": cnt,
        "n_students": len(grp),
        "mean": mean,
        "sd": sd,
        "p10": q[0], "p25": q[1], "p50": q[2], "p75": q[3], "p90": q[4],
        "p90_p10_range": q[4] - q[0],
        "pct_below_level1b": np.mean(pv_below400) * 100,
        "pct_level5_plus":   np.mean(pv_above600) * 100,
    })

summary = pd.DataFrame(records).dropna(subset=["mean"]).sort_values("mean", ascending=False).reset_index(drop=True)
summary.to_csv(os.path.join(PROCESSED_DIR, "country_reading_summary.csv"), index=False)
print(f"Summary written: {len(summary)} countries.")
print(summary[["country","mean","sd","p10","p90","p90_p10_range","pct_below_level1b","pct_level5_plus"]].head(20).to_string(index=False))

# ---------------------------------------------------------------------------
# 3. Find compelling country pairs
# ---------------------------------------------------------------------------
print("\nSearching for country pairs with similar means but different distributions...")

MEAN_THRESHOLD = 5      # max difference in mean scores
SPREAD_THRESHOLD = 20   # min difference in P90-P10 range

pairs = []
s = summary.copy()
for i in range(len(s)):
    for j in range(i + 1, len(s)):
        a, b = s.iloc[i], s.iloc[j]
        mean_diff   = abs(a["mean"] - b["mean"])
        spread_diff = abs(a["p90_p10_range"] - b["p90_p10_range"])
        pct_diff    = abs(a["pct_below_level1b"] - b["pct_below_level1b"])
        if mean_diff < MEAN_THRESHOLD and spread_diff > SPREAD_THRESHOLD:
            pairs.append({
                "country_a": a["country"], "country_b": b["country"],
                "mean_a": a["mean"], "mean_b": b["mean"],
                "mean_diff": mean_diff,
                "range_a": a["p90_p10_range"], "range_b": b["p90_p10_range"],
                "spread_diff": spread_diff,
                "pct_below_a": a["pct_below_level1b"], "pct_below_b": b["pct_below_level1b"],
                "pct_diff_below": pct_diff,
            })

pairs_df = pd.DataFrame(pairs).sort_values("spread_diff", ascending=False)
print(f"Found {len(pairs_df)} qualifying pairs.")
print(pairs_df.head(10).to_string(index=False))

# Pick the most striking pair: largest spread difference with meaningful pct_below contrast
best = pairs_df.iloc[0]
cnt_a, cnt_b = best["country_a"], best["country_b"]
print(f"\nSelected pair: {cnt_a} vs {cnt_b}")
print(f"  Mean: {best['mean_a']:.1f} vs {best['mean_b']:.1f}  (diff={best['mean_diff']:.1f})")
print(f"  P90-P10: {best['range_a']:.1f} vs {best['range_b']:.1f}  (diff={best['spread_diff']:.1f})")
print(f"  % below Level 1b: {best['pct_below_a']:.1f}% vs {best['pct_below_b']:.1f}%")

# Also note a runner-up pair if available
if len(pairs_df) >= 2:
    runner = pairs_df.iloc[1]
    print(f"\nRunner-up pair: {runner['country_a']} vs {runner['country_b']}")
    print(f"  Mean: {runner['mean_a']:.1f} vs {runner['mean_b']:.1f}")
    print(f"  P90-P10: {runner['range_a']:.1f} vs {runner['range_b']:.1f}")

# ---------------------------------------------------------------------------
# 4. Chart helpers
# ---------------------------------------------------------------------------

# PISA proficiency level boundaries for reading
LEVEL_BOUNDARIES = [
    (189, 262, "#d73027", "Below 1c"),
    (262, 335, "#f46d43", "Level 1c"),
    (335, 407, "#fdae61", "Level 1b"),
    (407, 480, "#fee090", "Level 1a"),
    (480, 553, "#e0f3f8", "Level 2"),
    (553, 626, "#abd9e9", "Level 3"),
    (626, 698, "#74add1", "Level 4"),
    (698, 800, "#4575b4", "Level 5+"),
]

PALETTE = {"a": "#1b6ca8", "b": "#e05c1a"}   # blue / orange

def get_country_pvs(cnt):
    """Return a single merged PV array (all 10 PVs stacked) with repeated weights."""
    grp = df[df["CNT"] == cnt]
    scores = np.concatenate([grp[pv].values for pv in PV_COLS])
    weights = np.tile(grp["W_FSTUWT"].values, 10)
    mask = np.isfinite(scores) & np.isfinite(weights) & (weights > 0)
    return scores[mask], weights[mask]

# ---------------------------------------------------------------------------
# 4a. Chart 1: Overlapping weighted KDE density curves
# ---------------------------------------------------------------------------
print("\nGenerating Chart 1: density comparison...")

fig, ax = plt.subplots(figsize=(11, 6))
fig.patch.set_facecolor("#fafafa")
ax.set_facecolor("#fafafa")

score_range = np.linspace(100, 820, 1000)

for key, cnt, color in [("a", cnt_a, PALETTE["a"]), ("b", cnt_b, PALETTE["b"])]:
    scores, weights = get_country_pvs(cnt)
    # Weighted KDE: repeat each score proportional to its weight
    w_norm = weights / weights.sum()
    kde = gaussian_kde(scores, weights=w_norm, bw_method=0.15)
    density = kde(score_range)
    ax.fill_between(score_range, density, alpha=0.25, color=color)
    ax.plot(score_range, density, color=color, linewidth=2.5, label=cnt)

    # Weighted mean line
    wmean = np.average(scores, weights=weights)
    ax.axvline(wmean, color=color, linewidth=1.5, linestyle="--", alpha=0.8)

# Level boundary shading (subtle)
for lo, hi, col, lbl in LEVEL_BOUNDARIES:
    ax.axvspan(lo, hi, alpha=0.06, color=col, zorder=0)

# Annotations for level boundaries
for lo, hi, col, lbl in LEVEL_BOUNDARIES[2:]:   # label from Level 1b upward
    ax.text((lo + hi) / 2, ax.get_ylim()[1] * 0.01, lbl,
            ha="center", va="bottom", fontsize=7, color="#555", rotation=90,
            transform=ax.get_xaxis_transform())

ax.set_xlabel("PISA Reading Score", fontsize=12)
ax.set_ylabel("Weighted Density", fontsize=12)
ax.set_title(
    f"Same average, different distribution\n{cnt_a} vs {cnt_b} — PISA 2018 Reading",
    fontsize=13, fontweight="bold", pad=14
)
ax.legend(fontsize=11, framealpha=0.9)
ax.set_xlim(100, 820)
ax.spines[["top", "right"]].set_visible(False)

plt.tight_layout()
chart1_path = os.path.join(CHARTS_DIR, "density_comparison.png")
plt.savefig(chart1_path, dpi=150, bbox_inches="tight")
plt.close()
print(f"  Saved: {chart1_path}")

# ---------------------------------------------------------------------------
# 4b. Chart 2: Landscape scatter — all countries, mean vs P90-P10 range
# ---------------------------------------------------------------------------
print("Generating Chart 2: landscape scatter...")

fig, ax = plt.subplots(figsize=(11, 7))
fig.patch.set_facecolor("#fafafa")
ax.set_facecolor("#fafafa")

# All countries as grey dots
ax.scatter(summary["mean"], summary["p90_p10_range"],
           s=40, color="#bbb", zorder=2, linewidths=0, alpha=0.7)

# Label every country (small)
for _, row in summary.iterrows():
    ax.text(row["mean"] + 0.8, row["p90_p10_range"], row["country"],
            fontsize=5.5, color="#888", va="center")

# Highlight selected pair
for key, cnt, color in [("a", cnt_a, PALETTE["a"]), ("b", cnt_b, PALETTE["b"])]:
    row = summary[summary["country"] == cnt].iloc[0]
    ax.scatter(row["mean"], row["p90_p10_range"], s=120, color=color,
               zorder=5, edgecolors="white", linewidths=1.5, label=cnt)
    ax.text(row["mean"] + 1.5, row["p90_p10_range"], cnt,
            fontsize=9, fontweight="bold", color=color, va="center")

ax.set_xlabel("Mean PISA Reading Score (weighted, 10 PVs)", fontsize=12)
ax.set_ylabel("P90–P10 Range (spread)", fontsize=12)
ax.set_title("Country landscape: mean score vs. performance spread\nPISA 2018 Reading",
             fontsize=13, fontweight="bold", pad=14)
ax.legend(title="Highlighted pair", fontsize=10, framealpha=0.9)
ax.spines[["top", "right"]].set_visible(False)

plt.tight_layout()
chart2_path = os.path.join(CHARTS_DIR, "landscape_scatter.png")
plt.savefig(chart2_path, dpi=150, bbox_inches="tight")
plt.close()
print(f"  Saved: {chart2_path}")

# ---------------------------------------------------------------------------
# 4c. Chart 3: Percentile bar chart (P10/P25/median/P75/P90)
# ---------------------------------------------------------------------------
print("Generating Chart 3: percentile comparison bars...")

stats_a = summary[summary["country"] == cnt_a].iloc[0]
stats_b = summary[summary["country"] == cnt_b].iloc[0]

fig, ax = plt.subplots(figsize=(9, 5))
fig.patch.set_facecolor("#fafafa")
ax.set_facecolor("#fafafa")

labels = ["P10", "P25", "Median\n(P50)", "P75", "P90"]
vals_a = [stats_a["p10"], stats_a["p25"], stats_a["p50"], stats_a["p75"], stats_a["p90"]]
vals_b = [stats_b["p10"], stats_b["p25"], stats_b["p50"], stats_b["p75"], stats_b["p90"]]

x = np.arange(len(labels))
width = 0.35

bars_a = ax.bar(x - width/2, vals_a, width, color=PALETTE["a"], alpha=0.85, label=cnt_a)
bars_b = ax.bar(x + width/2, vals_b, width, color=PALETTE["b"], alpha=0.85, label=cnt_b)

for bar in bars_a:
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 3,
            f"{bar.get_height():.0f}", ha="center", va="bottom", fontsize=9, color=PALETTE["a"])
for bar in bars_b:
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 3,
            f"{bar.get_height():.0f}", ha="center", va="bottom", fontsize=9, color=PALETTE["b"])

ax.set_xticks(x)
ax.set_xticklabels(labels, fontsize=11)
ax.set_ylabel("PISA Reading Score", fontsize=12)
ax.set_title(f"Percentile comparison: {cnt_a} vs {cnt_b}\nPISA 2018 Reading",
             fontsize=13, fontweight="bold", pad=12)
ax.legend(fontsize=11, framealpha=0.9)
ax.set_ylim(0, max(vals_a + vals_b) * 1.12)
ax.spines[["top", "right"]].set_visible(False)

plt.tight_layout()
chart3_path = os.path.join(CHARTS_DIR, "percentile_bars.png")
plt.savefig(chart3_path, dpi=150, bbox_inches="tight")
plt.close()
print(f"  Saved: {chart3_path}")

# ---------------------------------------------------------------------------
# 5. Print key statistics for the report
# ---------------------------------------------------------------------------
print("\n=== KEY STATISTICS FOR REPORT ===")
for cnt, key in [(cnt_a, "a"), (cnt_b, "b")]:
    row = summary[summary["country"] == cnt].iloc[0]
    print(f"\n{cnt}:")
    print(f"  Mean:             {row['mean']:.1f}")
    print(f"  SD:               {row['sd']:.1f}")
    print(f"  P10:              {row['p10']:.1f}")
    print(f"  P50:              {row['p50']:.1f}")
    print(f"  P90:              {row['p90']:.1f}")
    print(f"  P90-P10 range:    {row['p90_p10_range']:.1f}")
    print(f"  % below Level1b:  {row['pct_below_level1b']:.1f}%")
    print(f"  % Level 5+:       {row['pct_level5_plus']:.1f}%")

print("\nDone.")
