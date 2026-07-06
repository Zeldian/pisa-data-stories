"""
PISA 2018 Story: The Schools That Beat the Odds
Hypothesis: Some schools consistently help disadvantaged students outperform
expectations based on socioeconomic status.

Method:
  1. Aggregate student data to school level (weighted means: ESCS, performance).
  2. For each country (≥10 schools), fit OLS: school_perf ~ school_ESCS.
  3. Residuals measure how far a school sits above/below its country's SES gradient.
  4. "Odds-breaking" school: bottom ESCS tertile for its country AND residual > 0.
  5. Merge with school questionnaire to compare odds-breaking vs expected schools.
"""

import zipfile, tempfile, os, warnings
import numpy as np
import pandas as pd
import pyreadstat
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.lines import Line2D
from scipy.stats import pearsonr, ttest_ind
warnings.filterwarnings("ignore")

ROOT        = os.path.expanduser("~/code/pisa-data-stories")
RAW_STU     = os.path.join(ROOT, "data/raw/SPSS_STU_QQQ.zip")
RAW_SCH     = os.path.join(ROOT, "data/raw/SPSS_SCH_QQQ.zip")
PROC_DIR    = os.path.join(ROOT, "data/processed")
CHARTS_DIR  = os.path.join(ROOT, "stories/accepted/schools-beat-odds/charts")
os.makedirs(PROC_DIR, exist_ok=True)
os.makedirs(CHARTS_DIR, exist_ok=True)

PALETTE = {
    "odds_breaking":  "#2471a3",
    "other_lo":       "#aab4be",
    "hi_ses":         "#e8e4de",
    "accent":         "#e67e22",
    "pos":            "#2471a3",
    "neg":            "#c0392b",
    "neutral":        "#7f8c8d",
}

MATH_PVS = [f"PV{i}MATH" for i in range(1, 11)]
READ_PVS = [f"PV{i}READ" for i in range(1, 11)]
SCIE_PVS = [f"PV{i}SCIE" for i in range(1, 11)]

STU_COLS = (
    ["CNT", "CNTSCHID", "W_FSTUWT", "ESCS",
     "DISCLIMA", "TEACHSUP", "BELONG", "PERFEED", "EMOSUPS"]
    + MATH_PVS + READ_PVS + SCIE_PVS
)

SCH_COLS = [
    "CNT", "CNTSCHID",
    "SCHSIZE", "STRATIO", "CLSIZE",
    "STAFFSHORT", "EDUSHORT", "STUBEHA", "TEACHBEHA",
    "PROATCE", "SCHLTYPE", "CREACTIV",
    "SC064Q01TA", "SC064Q02TA", "SC001Q01TA",
]

# ---------------------------------------------------------------------------
# 1. Load student data
# ---------------------------------------------------------------------------
print("Loading student data…")
with zipfile.ZipFile(RAW_STU) as z:
    sav = next(n for n in z.namelist() if n.lower().endswith(".sav"))
    with tempfile.TemporaryDirectory() as tmp:
        z.extract(sav, tmp)
        path = os.path.join(tmp, sav)
        _, meta = pyreadstat.read_sav(path, row_limit=1)
        available = set(meta.column_names)
        use_cols = [c for c in STU_COLS if c in available]
        missing  = [c for c in STU_COLS if c not in available]
        if missing:
            print(f"  Note: absent from student file: {missing}")
        print(f"  Reading {len(use_cols)} columns…")
        stu, _ = pyreadstat.read_sav(path, usecols=use_cols)

stu = stu[stu["W_FSTUWT"] > 0].dropna(subset=["W_FSTUWT", "ESCS"])
print(f"  {len(stu):,} students with valid weight + ESCS, {stu['CNT'].nunique()} countries.")

# Student-level composite performance
math_pvs = [c for c in MATH_PVS if c in stu.columns]
read_pvs = [c for c in READ_PVS if c in stu.columns]
scie_pvs = [c for c in SCIE_PVS if c in stu.columns]
stu["perf"] = stu[math_pvs + read_pvs + scie_pvs].mean(axis=1)

# ---------------------------------------------------------------------------
# 2. Aggregate to school level
# ---------------------------------------------------------------------------
def wmean(grp, col):
    v = grp[col].to_numpy(dtype=float)
    w = grp["W_FSTUWT"].to_numpy(dtype=float)
    mask = np.isfinite(v) & (w > 0)
    return np.average(v[mask], weights=w[mask]) if mask.sum() > 0 else np.nan

print("Aggregating to school level…")
school_records = []
agg_cols = ["ESCS", "perf", "DISCLIMA", "TEACHSUP", "BELONG", "PERFEED", "EMOSUPS"]
for (cnt, schid), grp in stu.groupby(["CNT", "CNTSCHID"]):
    rec = {"CNT": cnt, "CNTSCHID": schid, "N_STU": len(grp),
           "SUM_W": grp["W_FSTUWT"].sum()}
    for col in agg_cols:
        if col in grp.columns:
            rec[f"sch_{col}"] = wmean(grp, col)
    school_records.append(rec)

schools = pd.DataFrame(school_records).dropna(subset=["sch_ESCS", "sch_perf"])
print(f"  {len(schools):,} schools with valid ESCS + performance.")

# ---------------------------------------------------------------------------
# 3. Within-country OLS → residuals + odds-breaking classification
# ---------------------------------------------------------------------------
print("Running within-country OLS (school_perf ~ school_ESCS)…")
ols_stats = []
residuals = []
MIN_SCHOOLS = 10

for cnt, grp in schools.groupby("CNT"):
    if len(grp) < MIN_SCHOOLS:
        continue
    x = grp["sch_ESCS"].values
    y = grp["sch_perf"].values
    slope, intercept = np.polyfit(x, y, 1)
    pred = intercept + slope * x
    res  = y - pred
    r, _ = pearsonr(x, y)
    ols_stats.append({"CNT": cnt, "slope": slope, "intercept": intercept,
                      "r_escs_perf": r, "n_schools": len(grp)})
    tmp_df = grp.copy()
    tmp_df["predicted"] = pred
    tmp_df["residual"]  = res
    tmp_df["ols_slope"] = slope
    tmp_df["ols_intercept"] = intercept
    residuals.append(tmp_df)

schools_ols = pd.concat(residuals, ignore_index=True)
ols_df = pd.DataFrame(ols_stats)
print(f"  {len(schools_ols):,} schools in {len(ols_df)} countries after OLS.")

# Within-country ESCS tertile → low-SES flag
t33_per_country = schools_ols.groupby("CNT")["sch_ESCS"].quantile(0.333).rename("escs_t33")
schools_ols = schools_ols.join(t33_per_country, on="CNT")
schools_ols["low_ses"] = schools_ols["sch_ESCS"] <= schools_ols["escs_t33"]
schools_ols = schools_ols.drop(columns=["escs_t33"])

# Odds-breaking: low SES AND performance >= country median performance
# (Low-SES school that achieves above-average academic results for its country)
# With strong SES-performance correlation, far fewer than half of low-SES schools
# will reach the median — so this metric meaningfully varies across countries.
perf_med_by_cnt = schools_ols.groupby("CNT")["sch_perf"].median().rename("perf_med")
schools_ols = schools_ols.join(perf_med_by_cnt, on="CNT")
schools_ols["odds_breaking"] = (
    schools_ols["low_ses"] & (schools_ols["sch_perf"] >= schools_ols["perf_med"]))
schools_ols = schools_ols.drop(columns=["perf_med"])

n_lo  = schools_ols["low_ses"].sum()
n_ob  = schools_ols["odds_breaking"].sum()
print(f"\n  Low-SES schools: {n_lo:,}")
print(f"  Odds-breaking schools: {n_ob:,} ({n_ob/n_lo*100:.1f}% of low-SES)")

# Country-level prevalence
country_stats = (schools_ols[schools_ols["low_ses"]]
                 .groupby("CNT")
                 .agg(n_low_ses=("CNTSCHID","count"),
                      n_odds_breaking=("odds_breaking","sum"))
                 .reset_index())
country_stats["pct_odds_breaking"] = (
    country_stats["n_odds_breaking"] / country_stats["n_low_ses"] * 100)
country_stats = country_stats.merge(ols_df[["CNT","r_escs_perf","slope"]], on="CNT")
country_stats = country_stats[country_stats["n_low_ses"] >= 5].sort_values(
    "pct_odds_breaking", ascending=False)

print(f"\n  Countries with ≥5 low-SES schools: {len(country_stats)}")
print(country_stats[["CNT","n_low_ses","n_odds_breaking","pct_odds_breaking"]].head(15).to_string(index=False))

# Save school-level output
schools_ols.to_csv(os.path.join(PROC_DIR, "schools_beat_odds.csv"), index=False)
country_stats.to_csv(os.path.join(PROC_DIR, "schools_beat_odds_country.csv"), index=False)

# ---------------------------------------------------------------------------
# 4. Load school questionnaire
# ---------------------------------------------------------------------------
print("\nLoading school questionnaire…")
with zipfile.ZipFile(RAW_SCH) as z:
    sav = next(n for n in z.namelist() if n.lower().endswith(".sav"))
    with tempfile.TemporaryDirectory() as tmp:
        z.extract(sav, tmp)
        path = os.path.join(tmp, sav)
        _, meta = pyreadstat.read_sav(path, row_limit=1)
        available_sch = set(meta.column_names)
        use_sch = [c for c in SCH_COLS if c in available_sch]
        sch_df, _ = pyreadstat.read_sav(path, usecols=use_sch)

print(f"  {len(sch_df):,} schools in questionnaire.")

# Merge with school-level residuals
merged = schools_ols.merge(sch_df, on=["CNT", "CNTSCHID"], how="left")
print(f"  Matched: {merged['STRATIO'].notna().sum():,} schools with school-Q data.")

# ---------------------------------------------------------------------------
# 5. School characteristics: odds-breaking vs other low-SES
# ---------------------------------------------------------------------------
print("\nComparing school characteristics…")

lo_ob  = merged[(merged["low_ses"]) & (merged["odds_breaking"])]
lo_exp = merged[(merged["low_ses"]) & (~merged["odds_breaking"])]
print(f"  Odds-breaking: n={len(lo_ob)}, Expected low-SES: n={len(lo_exp)}")

# Characteristics to compare (label, column, direction: +1=more is better)
CHARS = [
    ("Student behaviour\n(lower = better)",  "STUBEHA",      -1),
    ("Teacher behaviour\n(lower = better)",  "TEACHBEHA",    -1),
    ("Staff shortage\n(lower = better)",     "STAFFSHORT",   -1),
    ("Resource shortage\n(lower = better)",  "EDUSHORT",     -1),
    ("Disciplinary climate\n(student-rep.)", "sch_DISCLIMA",  1),
    ("Teacher support\n(student-rep.)",      "sch_TEACHSUP",  1),
    ("Sense of belonging\n(student-rep.)",   "sch_BELONG",    1),
    ("Certified teachers\n(proportion)",     "PROATCE",       1),
    ("Extra-curricular\nactivities",         "CREACTIV",      1),
    ("Parent–teacher\nmeetings",             "SC064Q01TA",    1),
]

char_results = []
for label, col, direction in CHARS:
    a = lo_ob[col].dropna()
    b = lo_exp[col].dropna()
    if len(a) < 5 or len(b) < 5:
        continue
    mean_ob  = a.mean()
    mean_exp = b.mean()
    pooled_sd = np.sqrt(((len(a)-1)*a.std()**2 + (len(b)-1)*b.std()**2) / (len(a)+len(b)-2))
    cohens_d = (mean_ob - mean_exp) / pooled_sd if pooled_sd > 0 else 0
    _, pval = ttest_ind(a, b)
    char_results.append({
        "label": label, "col": col, "direction": direction,
        "mean_ob": mean_ob, "mean_exp": mean_exp,
        "cohens_d": cohens_d,
        "adjusted_d": cohens_d * direction,
        "n_ob": len(a), "n_exp": len(b),
        "pval": pval, "sig": pval < 0.05
    })

char_df = pd.DataFrame(char_results).sort_values("adjusted_d", ascending=False)
print("\nCharacteristic differences (adjusted Cohen's d; positive = better for odds-breaking):")
for _, row in char_df.iterrows():
    sig = "**" if row["sig"] else "  "
    print(f"  {sig} {row['label'].replace(chr(10),' '):35s} d={row['adjusted_d']:+.3f}")

# ---------------------------------------------------------------------------
# 6. Chart 1 — The SES gradient and who escapes it
# ---------------------------------------------------------------------------
print("\nGenerating Chart 1: school scatter…")

# Select countries for small-multiples panel (6 diverse countries)
PANEL_CNTS = ["FIN", "USA", "JPN", "BRA", "QCI", "DEU"]
# Fallback if not all present
avail_cnts = schools_ols["CNT"].unique().tolist()
panel_cnts = [c for c in PANEL_CNTS if c in avail_cnts]

fig, axes = plt.subplots(2, 3, figsize=(15, 9))
fig.patch.set_facecolor("#fafafa")
axes = axes.flatten()

FULL_NAMES = {
    "FIN": "Finland", "USA": "United States", "JPN": "Japan",
    "BRA": "Brazil", "QCI": "China (B-S-J-Z)", "DEU": "Germany",
    "AUS": "Australia", "CAN": "Canada", "KOR": "Korea",
    "POL": "Poland", "EST": "Estonia",
}

for ax, cnt in zip(axes, panel_cnts):
    ax.set_facecolor("#fafafa")
    grp = schools_ols[schools_ols["CNT"] == cnt].copy()

    x_min, x_max = grp["sch_ESCS"].min() - 0.1, grp["sch_ESCS"].max() + 0.1
    y_min, y_max = grp["sch_perf"].min() - 5,   grp["sch_perf"].max() + 5

    # Thresholds used in odds-breaking classification
    escs_t33 = grp["sch_ESCS"].quantile(0.333)
    perf_med  = grp["sch_perf"].median()

    # Quadrant shading
    ax.fill_between([x_min, escs_t33], [perf_med, perf_med], [y_max, y_max],
                    color="#d6eaf8", alpha=0.45, zorder=0)   # low SES + high perf = odds-breaking
    ax.fill_between([x_min, escs_t33], [y_min, y_min], [perf_med, perf_med],
                    color="#fde8e8", alpha=0.3, zorder=0)    # low SES + low perf

    # Threshold lines
    ax.axvline(escs_t33, color="#999", lw=0.9, ls=":", zorder=1)
    ax.axhline(perf_med, color="#999", lw=0.9, ls=":", zorder=1)

    # Regression line for gradient context
    slope = grp["ols_slope"].iloc[0]
    inter = grp["ols_intercept"].iloc[0]
    xline = np.array([x_min, x_max])
    ax.plot(xline, inter + slope * xline,
            color="#aaa", lw=1.4, ls="--", zorder=2, alpha=0.75)

    # Plot schools
    hi_ses   = grp[~grp["low_ses"]]
    lo_exp2  = grp[grp["low_ses"] & ~grp["odds_breaking"]]
    lo_ob2   = grp[grp["low_ses"] & grp["odds_breaking"]]

    ax.scatter(hi_ses["sch_ESCS"],  hi_ses["sch_perf"],
               color="#d5d8dc", s=20, alpha=0.6, zorder=3)
    ax.scatter(lo_exp2["sch_ESCS"], lo_exp2["sch_perf"],
               color="#c0392b", s=28, alpha=0.8, zorder=4, marker="s")
    ax.scatter(lo_ob2["sch_ESCS"],  lo_ob2["sch_perf"],
               color=PALETTE["odds_breaking"], s=44, alpha=1.0, zorder=5,
               edgecolors="white", linewidths=0.5)

    n_ob_cnt = lo_ob2.shape[0]
    n_lo_cnt = lo_exp2.shape[0] + lo_ob2.shape[0]
    r_cnt, _ = pearsonr(grp["sch_ESCS"], grp["sch_perf"])

    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    ax.set_title(f"{FULL_NAMES.get(cnt, cnt)}", fontsize=11, fontweight="bold", pad=6)
    ax.set_xlabel("School mean ESCS (socioeconomic index)", fontsize=8.5)
    ax.set_ylabel("School mean performance", fontsize=8.5)
    ax.spines[["top","right"]].set_visible(False)
    ax.text(0.97, 0.03, f"r = {r_cnt:.2f}", transform=ax.transAxes,
            fontsize=8, color="#666", ha="right", va="bottom")
    ax.text(0.03, 0.97,
            f"{n_ob_cnt}/{n_lo_cnt} low-SES\nschools beat odds",
            transform=ax.transAxes, fontsize=7.5, color=PALETTE["odds_breaking"],
            fontweight="bold", va="top")

# Hide unused subplots if fewer than 6 countries found
for ax in axes[len(panel_cnts):]:
    ax.set_visible(False)

legend_els = [
    mpatches.Patch(color="#d5d8dc", label="Higher SES school"),
    mpatches.Patch(color="#c0392b", label="Low SES — performing as expected"),
    mpatches.Patch(color=PALETTE["odds_breaking"], label="Low SES — odds-breaking"),
]
fig.legend(handles=legend_els, loc="lower center", ncol=3, fontsize=9,
           bbox_to_anchor=(0.5, -0.04), framealpha=0.9)
fig.suptitle(
    "The SES gradient and who escapes it — PISA 2018\n"
    "Each dot is a school. Dashed line = country regression (perf ~ SES).",
    fontsize=12, fontweight="bold", y=1.01
)
plt.tight_layout()
out1 = os.path.join(CHARTS_DIR, "school_scatter.png")
plt.savefig(out1, dpi=150, bbox_inches="tight")
plt.close()
print(f"  Saved: {out1}")

# ---------------------------------------------------------------------------
# 7. Chart 2 — Country prevalence of odds-breaking schools
# ---------------------------------------------------------------------------
print("Generating Chart 2: country prevalence…")

cs = country_stats[country_stats["n_low_ses"] >= 8].copy()
cs_sorted = cs.sort_values("pct_odds_breaking", ascending=True).tail(40)

fig, ax = plt.subplots(figsize=(10, max(7, len(cs_sorted)*0.28)))
fig.patch.set_facecolor("#fafafa")
ax.set_facecolor("#fafafa")

colors = [PALETTE["odds_breaking"] if v >= 50 else
          PALETTE["accent"] if v >= 40 else
          PALETTE["other_lo"]
          for v in cs_sorted["pct_odds_breaking"]]

bars = ax.barh(range(len(cs_sorted)), cs_sorted["pct_odds_breaking"],
               color=colors, edgecolor="white", linewidth=0.4, height=0.7)

ax.axvline(50, color="#aaa", lw=1, ls="--", alpha=0.7)
ax.set_yticks(range(len(cs_sorted)))
ax.set_yticklabels(cs_sorted["CNT"], fontsize=8)
ax.set_xlabel("% of low-SES schools that are odds-breaking", fontsize=10)
ax.set_title(
    "How many low-SES schools beat the odds?\nPISA 2018 — % of bottom-ESCS-tertile schools performing above their country's SES gradient",
    fontsize=11, fontweight="bold", pad=10
)

# Annotate bar values
for i, (_, row) in enumerate(cs_sorted.iterrows()):
    ax.text(row["pct_odds_breaking"] + 0.5, i,
            f"{row['pct_odds_breaking']:.0f}%",
            va="center", fontsize=7.5, color="#333")

ax.set_xlim(0, 100)
ax.spines[["top","right"]].set_visible(False)
ax.text(0.99, -0.06,
        f"Countries shown: those with ≥8 low-SES schools (N={len(cs_sorted)})",
        transform=ax.transAxes, fontsize=7.5, color="#888", ha="right")

plt.tight_layout()
out2 = os.path.join(CHARTS_DIR, "country_prevalence.png")
plt.savefig(out2, dpi=150, bbox_inches="tight")
plt.close()
print(f"  Saved: {out2}")

# ---------------------------------------------------------------------------
# 8. Chart 3 — School characteristics: what makes odds-breakers different?
# ---------------------------------------------------------------------------
print("Generating Chart 3: school characteristics…")

char_df_sorted = char_df.sort_values("adjusted_d")
labels   = [r.replace("\n", " ") for r in char_df_sorted["label"]]
d_vals   = char_df_sorted["adjusted_d"].tolist()
sig_list = char_df_sorted["sig"].tolist()

fig, ax = plt.subplots(figsize=(9, max(5, len(char_df_sorted) * 0.65 + 1.5)))
fig.patch.set_facecolor("#fafafa")
ax.set_facecolor("#fafafa")

y_pos = np.arange(len(d_vals))
bar_colors = [PALETTE["pos"] if d > 0 else PALETTE["neg"] for d in d_vals]

bars = ax.barh(y_pos, d_vals, color=bar_colors, alpha=0.85,
               edgecolor="white", linewidth=0.4, height=0.6)

# Significance marker
for i, (d, sig) in enumerate(zip(d_vals, sig_list)):
    xoff = 0.01 if d >= 0 else -0.01
    ha   = "left" if d >= 0 else "right"
    if sig:
        ax.text(d + xoff, i, "★", va="center", ha=ha, fontsize=9,
                color="#333")

ax.axvline(0, color="#444", lw=1, zorder=3)
ax.set_yticks(y_pos)
ax.set_yticklabels(labels, fontsize=9.5)
ax.set_xlabel(
    "Standardized mean difference (Cohen's d)\n"
    "Positive = odds-breaking schools score higher on this dimension",
    fontsize=9.5
)
ax.set_title(
    "What distinguishes odds-breaking schools?\n"
    "Comparison of low-SES schools: odds-breaking vs. expected | ★ p < 0.05",
    fontsize=11, fontweight="bold", pad=10
)

# Reference lines
for xref in [-0.2, 0.2]:
    ax.axvline(xref, color="#ccc", lw=0.8, ls=":", zorder=1)

ax.spines[["top","right"]].set_visible(False)
legend_els = [
    mpatches.Patch(color=PALETTE["pos"], alpha=0.85, label="Advantage for odds-breaking schools"),
    mpatches.Patch(color=PALETTE["neg"], alpha=0.85, label="Advantage for expected schools"),
]
ax.legend(handles=legend_els, loc="lower right", fontsize=8.5, framealpha=0.9)

plt.tight_layout()
out3 = os.path.join(CHARTS_DIR, "school_characteristics.png")
plt.savefig(out3, dpi=150, bbox_inches="tight")
plt.close()
print(f"  Saved: {out3}")

# ---------------------------------------------------------------------------
# 9. Summary statistics for report
# ---------------------------------------------------------------------------
print("\n=== KEY STATISTICS ===")
n_countries   = len(ols_df)
n_schools_tot = len(schools_ols)
n_lo_all      = schools_ols["low_ses"].sum()
n_ob_all      = schools_ols["odds_breaking"].sum()

print(f"Countries included in OLS: {n_countries}")
print(f"Schools total: {n_schools_tot:,}")
print(f"Low-SES schools (bottom ESCS tertile): {n_lo_all:,}")
print(f"Odds-breaking schools: {n_ob_all:,} ({n_ob_all/n_lo_all*100:.1f}% of low-SES)")

print("\nCountry SES gradients (r):")
r_stats = ols_df["r_escs_perf"]
print(f"  Median r: {r_stats.median():.3f}  "
      f"Min: {r_stats.min():.3f}  Max: {r_stats.max():.3f}")

print("\nTop 10 countries by % odds-breaking:")
print(country_stats.head(10)[["CNT","n_low_ses","pct_odds_breaking"]].to_string(index=False))
print("\nBottom 10 countries by % odds-breaking:")
print(country_stats.tail(10)[["CNT","n_low_ses","pct_odds_breaking"]].to_string(index=False))

print("\nCharacteristic differences (odds-breaking vs expected low-SES):")
for _, r in char_df.iterrows():
    sig = "**" if r["sig"] else "  "
    print(f"  {sig} {r['label'].replace(chr(10),' '):35s} "
          f"adj_d={r['adjusted_d']:+.3f}  "
          f"ob={r['mean_ob']:.3f}  exp={r['mean_exp']:.3f}  "
          f"p={r['pval']:.4f}")

# Distribution of residuals among low-SES schools
lo_res = schools_ols[schools_ols["low_ses"]]["residual"]
print(f"\nResidual distribution (low-SES schools):")
print(f"  Mean: {lo_res.mean():.1f}  Median: {lo_res.median():.1f}  "
      f"SD: {lo_res.std():.1f}  "
      f"P25: {lo_res.quantile(0.25):.1f}  P75: {lo_res.quantile(0.75):.1f}")

print("\nDone.")
