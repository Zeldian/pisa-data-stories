"""
PISA 2018 Story: Excellence Without Misery
Hypothesis: High academic achievement and high student well-being are not
necessarily competing goals — some education systems achieve both.

Performance: Weighted country mean composite (Math + Reading + Science, 10 PVs each).
Well-being (primary):  ST016Q01NA — life satisfaction (0–10).
Well-being (secondary): BELONG, BEINGBULLIED (inverted), SWBP, GFOFAIL (inverted).

Quadrant thresholds: sample medians on both axes.
"""

import zipfile, tempfile, os
import numpy as np
import pandas as pd
import pyreadstat
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.colors import to_rgba
import matplotlib.ticker as mticker
from scipy.stats import pearsonr

ROOT       = os.path.expanduser("~/code/pisa-data-stories")
RAW_ZIP    = os.path.join(ROOT, "data/raw/SPSS_STU_QQQ.zip")
PROC_DIR   = os.path.join(ROOT, "data/processed")
CHARTS_DIR = os.path.join(ROOT, "stories/accepted/excellence-without-misery/charts")
os.makedirs(PROC_DIR,   exist_ok=True)
os.makedirs(CHARTS_DIR, exist_ok=True)

MATH_PVS = [f"PV{i}MATH" for i in range(1, 11)]
READ_PVS = [f"PV{i}READ" for i in range(1, 11)]
SCIE_PVS = [f"PV{i}SCIE" for i in range(1, 11)]

LOAD_COLS = (
    ["CNT", "CNTSCHID", "CNTSTUID", "W_FSTUWT", "OECD", "ESCS"]
    + MATH_PVS + READ_PVS + SCIE_PVS
    + ["ST016Q01NA", "BELONG", "BEINGBULLIED", "SWBP", "GFOFAIL"]
)

PALETTE = {
    "hi_hi":   "#2471a3",   # high performance, high well-being (the star quadrant)
    "hi_lo":   "#c0392b",   # high performance, low well-being
    "lo_hi":   "#1a7a4a",   # low performance, high well-being
    "lo_lo":   "#888",      # low performance, low well-being
    "neutral":  "#aab4be",
    "oecd":     "#2c3e50",
}

HIGHLIGHT = {
    "FIN": "hi_hi", "EST": "hi_hi", "CAN": "hi_hi", "DNK": "hi_hi",
    "NLD": "hi_hi", "AUS": "hi_hi",
    "JPN": "hi_lo", "KOR": "hi_lo", "SGP": "hi_lo", "HKG": "hi_lo",
    "TAP": "hi_lo",
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
        print(f"  Probing columns…")
        _, meta = pyreadstat.read_sav(sav_path, row_limit=1)
        available = set(meta.column_names)
        use_cols = [c for c in LOAD_COLS if c in available]
        missing = [c for c in LOAD_COLS if c not in available]
        if missing:
            print(f"  WARNING: {len(missing)} columns missing from file: {missing}")
        print(f"  Reading {len(use_cols)} columns…")
        df, _meta = pyreadstat.read_sav(sav_path, usecols=use_cols)

df = df[df["W_FSTUWT"] > 0].dropna(subset=["W_FSTUWT"])
print(f"Loaded {len(df):,} students, {df['CNT'].nunique()} countries.")

# ---------------------------------------------------------------------------
# 2. Student-level scores
# ---------------------------------------------------------------------------
# Performance: mean across 10 PVs for each domain, then composite
math_pvs = [c for c in MATH_PVS if c in df.columns]
read_pvs = [c for c in READ_PVS if c in df.columns]
scie_pvs = [c for c in SCIE_PVS if c in df.columns]

df["score_math"] = df[math_pvs].mean(axis=1)
df["score_read"] = df[read_pvs].mean(axis=1)
df["score_scie"] = df[scie_pvs].mean(axis=1)
df["score_composite"] = df[["score_math", "score_read", "score_scie"]].mean(axis=1)

# ---------------------------------------------------------------------------
# 3. Country-level aggregates
# ---------------------------------------------------------------------------
def wmean(grp, col):
    v = grp[col].values.astype(float)
    w = grp["W_FSTUWT"].values.astype(float)
    mask = np.isfinite(v) & (w > 0)
    if mask.sum() == 0:
        return np.nan
    return np.average(v[mask], weights=w[mask])

def wstd(grp, col):
    v = grp[col].values.astype(float)
    w = grp["W_FSTUWT"].values.astype(float)
    mask = np.isfinite(v) & (w > 0)
    if mask.sum() < 2:
        return np.nan
    m = np.average(v[mask], weights=w[mask])
    variance = np.average((v[mask] - m)**2, weights=w[mask])
    return np.sqrt(variance)

print("Computing country-level aggregates…")
records = []
for cnt, grp in df.groupby("CNT"):
    is_oecd = grp["OECD"].iloc[0] if "OECD" in grp.columns else np.nan
    records.append({
        "country":    cnt,
        "oecd":       int(is_oecd) if np.isfinite(is_oecd) else 0,
        "n_students": len(grp),
        "perf_math":  wmean(grp, "score_math"),
        "perf_read":  wmean(grp, "score_read"),
        "perf_scie":  wmean(grp, "score_scie"),
        "perf":       wmean(grp, "score_composite"),
        "lifesat":    wmean(grp, "ST016Q01NA") if "ST016Q01NA" in df.columns else np.nan,
        "belong":     wmean(grp, "BELONG")      if "BELONG"     in df.columns else np.nan,
        "bullied":    wmean(grp, "BEINGBULLIED") if "BEINGBULLIED" in df.columns else np.nan,
        "swbp":       wmean(grp, "SWBP")        if "SWBP"       in df.columns else np.nan,
        "gfofail":    wmean(grp, "GFOFAIL")     if "GFOFAIL"    in df.columns else np.nan,
        "escs_mean":  wmean(grp, "ESCS")        if "ESCS"       in df.columns else np.nan,
    })

country = pd.DataFrame(records).dropna(subset=["perf"])

# Well-being composite: standardize, invert negatives, average
for col in ["lifesat", "belong", "bullied", "swbp", "gfofail"]:
    if col in country.columns:
        mu, sd = country[col].mean(), country[col].std()
        country[f"z_{col}"] = (country[col] - mu) / sd if sd > 0 else 0

wb_cols = []
if "z_lifesat" in country.columns: wb_cols.append("z_lifesat")
if "z_belong"  in country.columns: wb_cols.append("z_belong")
if "z_swbp"    in country.columns: wb_cols.append("z_swbp")
if "z_bullied" in country.columns:
    country["z_bullied_inv"] = -country["z_bullied"]
    wb_cols.append("z_bullied_inv")
if "z_gfofail" in country.columns:
    country["z_gfofail_inv"] = -country["z_gfofail"]
    wb_cols.append("z_gfofail_inv")

country["wellbeing_composite"] = country[wb_cols].mean(axis=1)

# Drop rows where primary well-being measure is missing
country = country.dropna(subset=["lifesat"])
print(f"  {len(country)} countries with complete performance + well-being data.")

# Quadrant thresholds: median of both primary axes
perf_med   = country["perf"].median()
lifesat_med = country["lifesat"].median()

def quadrant(row):
    hi_p = row["perf"]    >= perf_med
    hi_w = row["lifesat"] >= lifesat_med
    if hi_p and hi_w:  return "hi_hi"
    if hi_p and not hi_w: return "hi_lo"
    if not hi_p and hi_w: return "lo_hi"
    return "lo_lo"

country["quadrant"] = country.apply(quadrant, axis=1)

print(f"\nPerformance median: {perf_med:.1f}   Life satisfaction median: {lifesat_med:.2f}")
print(f"\nQuadrant counts:")
print(country["quadrant"].value_counts())
print("\nHigh-performance, HIGH well-being countries:")
print(country[country["quadrant"]=="hi_hi"].sort_values("perf", ascending=False)[
    ["country","perf","lifesat","belong","wellbeing_composite"]].to_string(index=False))
print("\nHigh-performance, LOW well-being countries:")
print(country[country["quadrant"]=="hi_lo"].sort_values("perf", ascending=False)[
    ["country","perf","lifesat","belong","wellbeing_composite"]].to_string(index=False))

country.to_csv(os.path.join(PROC_DIR, "excellence_wellbeing_country.csv"), index=False)
print(f"\nSaved country summary → {PROC_DIR}/excellence_wellbeing_country.csv")

# ---------------------------------------------------------------------------
# 4. Chart 1 — The 2×2 Map
# ---------------------------------------------------------------------------
print("\nGenerating Chart 1: 2×2 map…")

quad_colors = {
    "hi_hi": "#d6eaf8",
    "hi_lo": "#fde8e8",
    "lo_hi": "#d5f5e3",
    "lo_lo": "#f2f3f4",
}
quad_dot = {
    "hi_hi": PALETTE["hi_hi"],
    "hi_lo": PALETTE["hi_lo"],
    "lo_hi": PALETTE["lo_hi"],
    "lo_lo": PALETTE["lo_lo"],
}

fig, ax = plt.subplots(figsize=(12, 8))
fig.patch.set_facecolor("#fafafa")
ax.set_facecolor("#fafafa")

xlim = (country["perf"].min() - 10, country["perf"].max() + 10)
ylim = (country["lifesat"].min() - 0.1, country["lifesat"].max() + 0.15)

# Quadrant shading
ax.axvspan(perf_med, xlim[1], ymin=0, ymax=1, color=quad_colors["hi_hi"], alpha=0.55, zorder=0)
ax.axvspan(xlim[0], perf_med, ymin=0, ymax=1, color=quad_colors["lo_lo"], alpha=0.55, zorder=0)
# Overlay the vertical split for hi-lo and lo-hi
ax.fill_between([perf_med, xlim[1]],
                [ylim[0], ylim[0]], [lifesat_med, lifesat_med],
                color=quad_colors["hi_lo"], alpha=0.55, zorder=0)
ax.fill_between([xlim[0], perf_med],
                [lifesat_med, lifesat_med], [ylim[1], ylim[1]],
                color=quad_colors["lo_hi"], alpha=0.55, zorder=0)

# Median lines
ax.axvline(perf_med,    color="#777", lw=0.9, ls="--", alpha=0.7, zorder=1)
ax.axhline(lifesat_med, color="#777", lw=0.9, ls="--", alpha=0.7, zorder=1)

# Quadrant labels
pad = dict(facecolor="white", edgecolor="none", alpha=0.7, boxstyle="round,pad=0.2")
ax.text(perf_med + 2,  ylim[1] - 0.05,
        "Excellence\nwithout misery", fontsize=8.5, color=PALETTE["hi_hi"],
        fontweight="bold", va="top", bbox=pad)
ax.text(perf_med + 2,  lifesat_med - 0.05,
        "Excellence\nwith misery",   fontsize=8.5, color=PALETTE["hi_lo"],
        fontweight="bold", va="top", bbox=pad)
ax.text(xlim[0] + 2,   ylim[1] - 0.05,
        "Low performance,\nhigh well-being", fontsize=7.5, color=PALETTE["lo_hi"],
        fontweight="bold", va="top", bbox=pad)
ax.text(xlim[0] + 2,   lifesat_med - 0.05,
        "Low performance,\nlow well-being",  fontsize=7.5, color=PALETTE["lo_lo"],
        fontweight="bold", va="top", bbox=pad)

# All countries
for _, row in country.iterrows():
    cnt = row["country"]
    q = row["quadrant"]
    is_key = cnt in HIGHLIGHT
    color  = quad_dot[q]
    s = 100 if is_key else 35
    zorder = 6 if is_key else 3
    ec = "white" if is_key else "none"
    lw = 0.8 if is_key else 0
    ax.scatter(row["perf"], row["lifesat"], color=color, s=s, zorder=zorder,
               edgecolors=ec, linewidths=lw)
    if is_key:
        dx, dy = 4, 0.02
        ha = "left"
        ax.annotate(cnt, (row["perf"], row["lifesat"]),
                    xytext=(dx, dy * 18), textcoords="offset points",
                    fontsize=9, fontweight="bold", color=color, ha=ha)
    else:
        ax.text(row["perf"] + 1.5, row["lifesat"], cnt,
                fontsize=5, color="#aaa", va="center")

ax.set_xlim(*xlim)
ax.set_ylim(*ylim)
ax.set_xlabel("Mean Academic Score — composite of Math, Reading, Science (PISA scale)", fontsize=12)
ax.set_ylabel("Mean Life Satisfaction (0 = not at all, 10 = completely)", fontsize=12)
ax.set_title("National academic performance vs. student life satisfaction\nPISA 2018 — 15-year-olds",
             fontsize=13, fontweight="bold", pad=14)

# Correlation annotation
valid = country.dropna(subset=["perf", "lifesat"])
r, p = pearsonr(valid["perf"], valid["lifesat"])
ax.text(0.98, 0.02, f"r = {r:.2f} (p {'< 0.01' if p < 0.01 else f'= {p:.2f}'})",
        transform=ax.transAxes, fontsize=9, color="#555",
        ha="right", va="bottom",
        bbox=dict(facecolor="white", edgecolor="#ccc", alpha=0.8, boxstyle="round,pad=0.3"))

ax.spines[["top","right"]].set_visible(False)
plt.tight_layout()
p1 = os.path.join(CHARTS_DIR, "quadrant_scatter.png")
plt.savefig(p1, dpi=150, bbox_inches="tight")
plt.close()
print(f"  Saved: {p1}")

# ---------------------------------------------------------------------------
# 5. Chart 2 — Well-being profile: excellence quadrants compared
# ---------------------------------------------------------------------------
print("Generating Chart 2: well-being profile…")

# Countries in the high-performance half
hi_perf = country[country["perf"] >= perf_med].copy()
# Split by well-being quadrant
hi_hi = hi_perf[hi_perf["quadrant"] == "hi_hi"].nlargest(7, "perf")
hi_lo = hi_perf[hi_perf["quadrant"] == "hi_lo"].nlargest(7, "perf")

# Dimensions to compare (display labels)
dims = [
    ("lifesat",  "Life\nsatisfaction", False, 0, 10),
    ("belong",   "Sense of\nbelonging", False, None, None),
    ("swbp",     "Positive\naffect",   False, None, None),
    ("bullied",  "Bullied\n(lower = better)", True,  None, None),
    ("gfofail",  "Fear of\nfailure (lower = better)", True,  None, None),
]

fig, axes = plt.subplots(1, len(dims), figsize=(14, 5.5), sharey=False)
fig.patch.set_facecolor("#fafafa")
fig.suptitle(
    "Well-being profile: high-performing countries split by student well-being\nPISA 2018",
    fontsize=12, fontweight="bold", y=1.01
)

def group_means(grp_df, col):
    valid = grp_df[col].dropna()
    return valid.mean() if len(valid) > 0 else np.nan

for ax, (col, label, invert, lo, hi) in zip(axes, dims):
    ax.set_facecolor("#fafafa")
    if col not in country.columns:
        ax.axis("off")
        continue

    val_hi_hi = hi_hi[col].dropna()
    val_hi_lo = hi_lo[col].dropna()

    m_hi_hi = val_hi_hi.mean()
    m_hi_lo = val_hi_lo.mean()

    # Individual country dots
    jitter_x = 0.08
    rng = np.random.default_rng(42)
    for v in val_hi_hi:
        ax.scatter(0.3 + rng.uniform(-jitter_x, jitter_x), v,
                   color=PALETTE["hi_hi"], alpha=0.55, s=28, zorder=3)
    for v in val_hi_lo:
        ax.scatter(0.7 + rng.uniform(-jitter_x, jitter_x), v,
                   color=PALETTE["hi_lo"], alpha=0.55, s=28, zorder=3)

    # Group means
    ax.plot([0.22, 0.38], [m_hi_hi, m_hi_hi], color=PALETTE["hi_hi"], lw=2.5, zorder=4)
    ax.plot([0.62, 0.78], [m_hi_lo, m_hi_lo], color=PALETTE["hi_lo"], lw=2.5, zorder=4)
    ax.plot([0.3, 0.7], [m_hi_hi, m_hi_lo], color="#ccc", lw=1, ls="--", zorder=2)

    ax.set_xticks([0.3, 0.7])
    ax.set_xticklabels(["High\nwell-being", "Low\nwell-being"], fontsize=8)
    ax.set_xlim(0, 1)
    ax.set_title(label, fontsize=9.5, pad=6)
    ax.spines[["top","right","bottom"]].set_visible(False)
    ax.tick_params(axis="x", length=0)

# Legend
from matplotlib.lines import Line2D
legend_els = [
    Line2D([0],[0], color=PALETTE["hi_hi"], lw=2.5, label="Excellence + well-being"),
    Line2D([0],[0], color=PALETTE["hi_lo"], lw=2.5, label="Excellence + misery"),
]
fig.legend(handles=legend_els, loc="lower center", ncol=2, fontsize=9,
           bbox_to_anchor=(0.5, -0.06), framealpha=0.9)

plt.tight_layout()
p2 = os.path.join(CHARTS_DIR, "wellbeing_profile.png")
plt.savefig(p2, dpi=150, bbox_inches="tight")
plt.close()
print(f"  Saved: {p2}")

# ---------------------------------------------------------------------------
# 6. Chart 3 — Equity check: well-being by ESCS quartile, per country group
# ---------------------------------------------------------------------------
print("Generating Chart 3: equity check…")

hi_hi_cnts = country[country["quadrant"]=="hi_hi"].nlargest(6, "perf")["country"].tolist()
hi_lo_cnts = country[country["quadrant"]=="hi_lo"].nlargest(6, "perf")["country"].tolist()

def escs_wellbeing(cnt_list, label):
    sub = df[df["CNT"].isin(cnt_list)].copy()
    if "ESCS" not in sub.columns or "ST016Q01NA" not in sub.columns:
        return None
    sub = sub.dropna(subset=["ESCS", "ST016Q01NA", "W_FSTUWT"])
    sub["escs_q"] = pd.qcut(sub["ESCS"], 4, labels=["Q1\n(lowest)", "Q2", "Q3", "Q4\n(highest)"])
    result = []
    for q, grp in sub.groupby("escs_q", observed=True):
        result.append({
            "group": label,
            "quartile": q,
            "mean_lifesat": wmean(grp, "ST016Q01NA"),
        })
    return pd.DataFrame(result)

eq_hi_hi = escs_wellbeing(hi_hi_cnts, "Excellence\n+ well-being")
eq_hi_lo = escs_wellbeing(hi_lo_cnts, "Excellence\n+ misery")

if eq_hi_hi is not None and eq_hi_lo is not None:
    fig, ax = plt.subplots(figsize=(9, 5.5))
    fig.patch.set_facecolor("#fafafa")
    ax.set_facecolor("#fafafa")

    quartiles = ["Q1\n(lowest)", "Q2", "Q3", "Q4\n(highest)"]
    x = np.arange(len(quartiles))
    width = 0.35

    bars_a = [eq_hi_hi[eq_hi_hi["quartile"]==q]["mean_lifesat"].values
              for q in quartiles]
    bars_b = [eq_hi_lo[eq_hi_lo["quartile"]==q]["mean_lifesat"].values
              for q in quartiles]

    vals_a = [v[0] if len(v) > 0 else np.nan for v in bars_a]
    vals_b = [v[0] if len(v) > 0 else np.nan for v in bars_b]

    ax.bar(x - width/2, vals_a, width, color=PALETTE["hi_hi"], alpha=0.85,
           label="Excellence + well-being", edgecolor="white", linewidth=0.5)
    ax.bar(x + width/2, vals_b, width, color=PALETTE["hi_lo"], alpha=0.85,
           label="Excellence + misery",    edgecolor="white", linewidth=0.5)

    ax.set_xticks(x)
    ax.set_xticklabels(quartiles, fontsize=10)
    ax.set_xlabel("Socioeconomic quartile (ESCS)", fontsize=11)
    ax.set_ylabel("Mean life satisfaction (0–10)", fontsize=11)
    ax.set_title(
        "Is well-being equitably distributed?\nLife satisfaction by socioeconomic quartile, within high-performing country groups",
        fontsize=12, fontweight="bold", pad=12
    )
    ymin = min(v for v in vals_a + vals_b if np.isfinite(v)) - 0.3
    ymax = max(v for v in vals_a + vals_b if np.isfinite(v)) + 0.3
    ax.set_ylim(ymin, ymax)
    ax.legend(fontsize=10, framealpha=0.9)
    ax.spines[["top","right"]].set_visible(False)

    plt.tight_layout()
    p3 = os.path.join(CHARTS_DIR, "equity_by_escs.png")
    plt.savefig(p3, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"  Saved: {p3}")

# ---------------------------------------------------------------------------
# 7. Key statistics for report
# ---------------------------------------------------------------------------
print("\n=== KEY STATISTICS ===")
print(f"Countries with complete data: {len(country)}")
print(f"Performance median: {perf_med:.1f}")
print(f"Life satisfaction median: {lifesat_med:.2f}")
print(f"\nCorrelation (performance × life satisfaction): r = {r:.3f}, p = {p:.4f}")

print(f"\nExcellence + well-being quadrant ({len(country[country['quadrant']=='hi_hi'])}):")
print(country[country["quadrant"]=="hi_hi"].sort_values("perf", ascending=False)[
    ["country","perf","lifesat","belong","swbp","gfofail","wellbeing_composite"]
].to_string(index=False))

print(f"\nExcellence + misery quadrant ({len(country[country['quadrant']=='hi_lo'])}):")
print(country[country["quadrant"]=="hi_lo"].sort_values("perf", ascending=False)[
    ["country","perf","lifesat","belong","swbp","gfofail","wellbeing_composite"]
].to_string(index=False))

print(f"\nNotable country pairs (similar performance, contrasting well-being):")
for hi_cnt in ["FIN", "EST", "CAN"]:
    if hi_cnt not in country["country"].values: continue
    r_hi = country[country["country"]==hi_cnt].iloc[0]
    print(f"  {hi_cnt}: perf={r_hi['perf']:.0f}, lifesat={r_hi['lifesat']:.2f}, belong={r_hi['belong']:.2f}, gfofail={r_hi['gfofail']:.2f}")
for lo_cnt in ["JPN", "KOR", "SGP"]:
    if lo_cnt not in country["country"].values: continue
    r_lo = country[country["country"]==lo_cnt].iloc[0]
    print(f"  {lo_cnt}: perf={r_lo['perf']:.0f}, lifesat={r_lo['lifesat']:.2f}, belong={r_lo['belong']:.2f}, gfofail={r_lo['gfofail']:.2f}")

print("\nDone.")
