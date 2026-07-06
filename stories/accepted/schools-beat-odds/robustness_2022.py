"""
Robustness appendix: Schools That Beat the Odds — PISA 2022 comparison.

Core questions:
  1. Does the school-level SES-performance gradient (median r ≈ 0.71) replicate?
  2. Does the ~16.9% odds-breaking rate among low-SES schools replicate?
  3. Do odds-breaking schools still show higher student-reported climate scores?

2022 variable availability vs 2018:
  Available (both): ESCS, CNTSCHID, W_FSTUWT, BELONG, TEACHSUP
  2022 equivalent:  DISCLIM (maths disciplinary climate) ≈ 2018 DISCLIMA (language)
  Absent in 2022:   DISCLIMA, school questionnaire variables (STAFFSHORT, EDUSHORT,
                    STUBEHA, TEACHBEHA, PROATCE, STRATIO — no SCH file present)

Output: charts/robustness_2022.png
"""

import zipfile, tempfile, os, warnings
import numpy as np
import pandas as pd
import pyreadstat
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from scipy.stats import pearsonr, ttest_ind
warnings.filterwarnings("ignore")

ROOT       = os.path.expanduser("~/code/pisa-data-stories")
RAW_2022   = os.path.join(ROOT, "data/raw/SPSS_STU_QQQ_2022.zip")
REF_SCH    = os.path.join(ROOT, "data/processed/schools_beat_odds.csv")
REF_CNT    = os.path.join(ROOT, "data/processed/schools_beat_odds_country.csv")
PROC_DIR   = os.path.join(ROOT, "data/processed")
CHARTS_DIR = os.path.join(ROOT, "stories/accepted/schools-beat-odds/charts")

MATH_PVS = [f"PV{i}MATH" for i in range(1, 11)]
READ_PVS = [f"PV{i}READ" for i in range(1, 11)]
SCIE_PVS = [f"PV{i}SCIE" for i in range(1, 11)]

LOAD_COLS = (
    ["CNT", "CNTSCHID", "W_FSTUWT", "ESCS", "DISCLIM", "TEACHSUP", "BELONG"]
    + MATH_PVS + READ_PVS + SCIE_PVS
)

# ---------------------------------------------------------------------------
# 1. Load 2022 student data
# ---------------------------------------------------------------------------
print("Loading PISA 2022 student data…")
with zipfile.ZipFile(RAW_2022) as z:
    sav = next(n for n in z.namelist() if n.upper().endswith(".SAV"))
    with tempfile.TemporaryDirectory() as tmp:
        z.extract(sav, tmp)
        path = os.path.join(tmp, sav)
        _, meta = pyreadstat.read_sav(path, row_limit=1)
        use_cols = [c for c in LOAD_COLS if c in meta.column_names]
        missing  = [c for c in LOAD_COLS if c not in meta.column_names]
        if missing:
            print(f"  Note: absent from 2022 file: {missing}")
        print(f"  Reading {len(use_cols)} columns from {sav}…")
        stu, _ = pyreadstat.read_sav(path, usecols=use_cols)

stu = stu[stu["W_FSTUWT"] > 0].dropna(subset=["W_FSTUWT", "ESCS"])
print(f"  {len(stu):,} students with valid weight + ESCS, {stu['CNT'].nunique()} countries.")

# Composite performance
math_pvs = [c for c in MATH_PVS if c in stu.columns]
read_pvs = [c for c in READ_PVS if c in stu.columns]
scie_pvs = [c for c in SCIE_PVS if c in stu.columns]
stu["perf"] = stu[math_pvs + read_pvs + scie_pvs].mean(axis=1)

# ---------------------------------------------------------------------------
# 2. School-level aggregation
# ---------------------------------------------------------------------------
def wmean(grp, col):
    v = grp[col].to_numpy(dtype=float)
    w = grp["W_FSTUWT"].to_numpy(dtype=float)
    mask = np.isfinite(v) & (w > 0)
    return np.average(v[mask], weights=w[mask]) if mask.sum() > 0 else np.nan

print("Aggregating to school level…")
agg_cols = ["ESCS", "perf", "DISCLIM", "TEACHSUP", "BELONG"]
records = []
for (cnt, schid), grp in stu.groupby(["CNT", "CNTSCHID"]):
    rec = {"CNT": cnt, "CNTSCHID": schid, "N_STU": len(grp)}
    for col in agg_cols:
        if col in grp.columns:
            rec[f"sch_{col}"] = wmean(grp, col)
    records.append(rec)

schools = pd.DataFrame(records).dropna(subset=["sch_ESCS", "sch_perf"])
print(f"  {len(schools):,} schools with valid ESCS + performance.")

# ---------------------------------------------------------------------------
# 3. Within-country OLS → SES gradient
# ---------------------------------------------------------------------------
print("Running within-country OLS…")
ols_records = []
residuals = []
MIN_SCHOOLS = 10

for cnt, grp in schools.groupby("CNT"):
    if len(grp) < MIN_SCHOOLS:
        continue
    x, y = grp["sch_ESCS"].values, grp["sch_perf"].values
    slope, intercept = np.polyfit(x, y, 1)
    r, _ = pearsonr(x, y)
    ols_records.append({"CNT": cnt, "slope": slope, "r_escs_perf": r,
                        "n_schools": len(grp)})
    tmp_df = grp.copy()
    tmp_df["ols_slope"] = slope
    tmp_df["ols_intercept"] = intercept
    residuals.append(tmp_df)

schools_ols = pd.concat(residuals, ignore_index=True)
ols_df = pd.DataFrame(ols_records)
print(f"  {len(schools_ols):,} schools in {len(ols_df)} countries.")

# ---------------------------------------------------------------------------
# 4. Odds-breaking classification (identical criterion to 2018)
# ---------------------------------------------------------------------------
# Low-SES: bottom ESCS tertile within country
t33 = schools_ols.groupby("CNT")["sch_ESCS"].quantile(0.333).rename("escs_t33")
schools_ols = schools_ols.join(t33, on="CNT")
schools_ols["low_ses"] = schools_ols["sch_ESCS"] <= schools_ols["escs_t33"]
schools_ols = schools_ols.drop(columns=["escs_t33"])

# Odds-breaking: low SES AND performance >= country median
perf_med = schools_ols.groupby("CNT")["sch_perf"].median().rename("perf_med")
schools_ols = schools_ols.join(perf_med, on="CNT")
schools_ols["odds_breaking"] = (
    schools_ols["low_ses"] & (schools_ols["sch_perf"] >= schools_ols["perf_med"]))
schools_ols = schools_ols.drop(columns=["perf_med"])

n_lo = schools_ols["low_ses"].sum()
n_ob = schools_ols["odds_breaking"].sum()
r22_median = ols_df["r_escs_perf"].median()
pct_ob_22  = n_ob / n_lo * 100

print(f"\n  2022 median r (ESCS–performance): {r22_median:.3f}")
print(f"  Low-SES schools: {n_lo:,}")
print(f"  Odds-breaking:   {n_ob:,} ({pct_ob_22:.1f}% of low-SES)")

# Country-level prevalence
cnt_stats_22 = (schools_ols[schools_ols["low_ses"]]
                .groupby("CNT")
                .agg(n_low_ses=("CNTSCHID","count"),
                     n_ob=("odds_breaking","sum"))
                .assign(pct_ob=lambda d: d["n_ob"]/d["n_low_ses"]*100)
                .reset_index()
                .merge(ols_df[["CNT","r_escs_perf"]], on="CNT"))

cnt_stats_22.to_csv(os.path.join(PROC_DIR, "schools_beat_odds_country_2022.csv"), index=False)
schools_ols.to_csv(os.path.join(PROC_DIR, "schools_beat_odds_2022.csv"), index=False)

# ---------------------------------------------------------------------------
# 5. Climate characteristic comparison (same method as 2018)
# ---------------------------------------------------------------------------
lo_ob  = schools_ols[schools_ols["odds_breaking"]]
lo_exp = schools_ols[schools_ols["low_ses"] & ~schools_ols["odds_breaking"]]
print(f"\n  Odds-breaking: n={len(lo_ob)},  Expected: n={len(lo_exp)}")

# 2022 climate variables available; labelled with 2018 names for comparison
CLIMATE_VARS_22 = [
    ("DISCLIM",    "Disciplinary climate",  1),   # 2022 DISCLIM ≈ 2018 DISCLIMA
    ("TEACHSUP",   "Teacher support",       1),
    ("BELONG",     "Sense of belonging",    1),
]

results_22 = {}
for col, label, direction in CLIMATE_VARS_22:
    scol = f"sch_{col}"
    a = lo_ob[scol].dropna() if scol in lo_ob.columns else pd.Series(dtype=float)
    b = lo_exp[scol].dropna() if scol in lo_exp.columns else pd.Series(dtype=float)
    if len(a) < 5 or len(b) < 5:
        results_22[label] = None
        continue
    pool_sd = np.sqrt(((len(a)-1)*a.std()**2 + (len(b)-1)*b.std()**2) / (len(a)+len(b)-2))
    d = (a.mean() - b.mean()) / pool_sd * direction if pool_sd > 0 else 0
    _, pval = ttest_ind(a, b)
    results_22[label] = {"d22": d, "pval": pval, "sig": pval < 0.05,
                          "mean_ob": a.mean(), "mean_exp": b.mean()}
    sig = "**" if pval < 0.05 else "  "
    print(f"  {sig} {label:30s} d={d:+.3f}  (ob={a.mean():.3f}  exp={b.mean():.3f}  p={pval:.4f})")

# ---------------------------------------------------------------------------
# 6. Load 2018 reference values for comparison
# ---------------------------------------------------------------------------
D18 = {
    "Disciplinary climate": 0.584,
    "Teacher support":      0.226,
    "Sense of belonging":   0.398,
}

# ---------------------------------------------------------------------------
# 7. Cross-cycle country stability
# ---------------------------------------------------------------------------
cnt18 = pd.read_csv(REF_CNT)
c18_idx = (cnt18.rename(columns={"pct_odds_breaking":"pct_ob_18",
                                  "r_escs_perf":"r_18"})
               .set_index("CNT")[["pct_ob_18","r_18"]])
c22_idx = (cnt_stats_22.rename(columns={"pct_ob":"pct_ob_22",
                                         "r_escs_perf":"r_22"})
                .set_index("CNT")[["pct_ob_22","r_22"]])
both = c18_idx.join(c22_idx).dropna()
stability_r, _ = pearsonr(both["pct_ob_18"], both["pct_ob_22"])
print(f"\n  Countries in both cycles: {len(both)}")
print(f"  Country-level % odds-breaking correlation (2018 vs 2022): r = {stability_r:.3f}")

r18_med = cnt18["r_escs_perf"].median()
pct18   = cnt18["pct_odds_breaking"].mean()
print(f"\n  Summary comparison:")
print(f"    Median r (ESCS–perf):     2018 = {r18_med:.3f}  |  2022 = {r22_median:.3f}")
print(f"    Mean % odds-breaking:     2018 = {pct18:.1f}%   |  2022 = {pct_ob_22:.1f}%")

# Notable countries
print("\n  Country-level odds-breaking rates (shared countries):")
hdr = f"  {'CNT':5s}  {'pct18':>7s}  {'pct22':>7s}  {'r18':>6s}  {'r22':>6s}"
print(hdr)
for cnt in ["ALB","NOR","ISL","EST","KAZ","DEU","NLD","FRA","HUN","BRN"]:
    if cnt not in both.index: continue
    row = both.loc[cnt]
    print(f"  {cnt:5s}  {row['pct_ob_18']:7.1f}  {row['pct_ob_22']:7.1f}  "
          f"{row['r_18']:6.3f}  {row['r_22']:6.3f}")

# ---------------------------------------------------------------------------
# 8. Comparison figure: climate Cohen's d (2018 vs 2022) + summary stats
# ---------------------------------------------------------------------------
print("\nGenerating robustness figure…")

clim_labels = ["Disciplinary climate", "Sense of belonging", "Teacher support"]
d18_vals = [D18[l] for l in clim_labels]
d22_vals = [results_22[l]["d22"] if results_22.get(l) else np.nan for l in clim_labels]
sig22    = [results_22[l]["sig"] if results_22.get(l) else False for l in clim_labels]

BLUE  = "#2471a3"
AMBER = "#e67e22"
GRAY  = "#aab4be"

fig = plt.figure(figsize=(12, 5.5))
fig.patch.set_facecolor("#fafafa")
gs = fig.add_gridspec(1, 2, width_ratios=[1.5, 1], wspace=0.35)

# Left panel: grouped bar chart of Cohen's d
ax1 = fig.add_subplot(gs[0])
ax1.set_facecolor("#fafafa")

n = len(clim_labels)
x = np.arange(n)
w = 0.32

bars18 = ax1.bar(x - w/2, d18_vals, w, color=BLUE, alpha=0.85,
                 label="PISA 2018", edgecolor="white", linewidth=0.5)
bars22 = ax1.bar(x + w/2, d22_vals, w, color=AMBER, alpha=0.85,
                 label="PISA 2022", edgecolor="white", linewidth=0.5)

# Significance stars on 2022 bars
for i, (d, sig) in enumerate(zip(d22_vals, sig22)):
    if sig and np.isfinite(d):
        ax1.text(i + w/2, d + 0.01, "★", ha="center", va="bottom",
                 fontsize=10, color="#333")

ax1.axhline(0, color="#444", lw=0.8)
ax1.set_xticks(x)
ax1.set_xticklabels(clim_labels, fontsize=10)
ax1.set_ylabel("Cohen's d (odds-breaking vs. expected low-SES)", fontsize=9.5)
ax1.set_title(
    "Student-reported school climate\nOdds-breaking vs. expected low-SES schools",
    fontsize=10.5, fontweight="bold", pad=8)
ax1.legend(fontsize=9, framealpha=0.9)
ax1.spines[["top","right"]].set_visible(False)
ax1.set_ylim(0, max(max(d18_vals), max(d for d in d22_vals if np.isfinite(d))) + 0.12)

for bar, d in zip(bars18, d18_vals):
    ax1.text(bar.get_x() + bar.get_width()/2, d + 0.01,
             f"{d:.2f}", ha="center", va="bottom", fontsize=8, color=BLUE)
for bar, d in zip(bars22, d22_vals):
    if np.isfinite(d):
        ax1.text(bar.get_x() + bar.get_width()/2, d + 0.01,
                 f"{d:.2f}", ha="center", va="bottom", fontsize=8, color=AMBER)

# Right panel: summary table (text plot)
ax2 = fig.add_subplot(gs[1])
ax2.set_facecolor("#fafafa")
ax2.axis("off")

r18_med_str  = f"{r18_med:.3f}"
r22_med_str  = f"{r22_median:.3f}"
pct18_str    = f"{pct18:.1f}%"
pct22_str    = f"{pct_ob_22:.1f}%"
stab_str     = f"r = {stability_r:.2f}"

table_data = [
    ["", "2018", "2022"],
    ["Countries", "79", str(len(ols_df))],
    ["Schools", "21,684", f"{len(schools_ols):,}"],
    ["Low-SES schools", "7,227", f"{n_lo:,}"],
    ["Odds-breaking", "16.9%", f"{pct_ob_22:.1f}%"],
    ["Median r (ESCS)", r18_med_str, r22_med_str],
    ["Country stability", "", stab_str],
]

ax2.set_xlim(0, 1)
ax2.set_ylim(0, 1)
row_h = 0.11
for i, row in enumerate(table_data):
    y = 0.95 - i * row_h
    for j, cell in enumerate(row):
        x_pos = [0.02, 0.38, 0.72][j]
        is_header = (i == 0)
        is_row_header = (j == 0)
        weight = "bold" if (is_header or is_row_header) else "normal"
        color = "#1a1212" if (is_header or is_row_header) else "#4a3f3a"
        if j == 1 and not is_header:
            color = BLUE
        if j == 2 and not is_header:
            color = AMBER
        ax2.text(x_pos, y, cell, transform=ax2.transAxes,
                 fontsize=9, fontweight=weight, color=color, va="top",
                 fontfamily="monospace" if not is_row_header else "serif")
    if i == 0:
        ax2.plot([0.02, 0.98], [y - 0.03, y - 0.03], color="#ccc", lw=0.8,
                 transform=ax2.transAxes)

ax2.set_title("Summary comparison", fontsize=10.5, fontweight="bold", pad=8)
ax2.text(0.5, -0.04,
         "★ p < 0.05  |  2022 DISCLIM = math discipline\nvs 2018 DISCLIMA = language discipline",
         transform=ax2.transAxes, fontsize=7.5, color="#888",
         ha="center", va="top")

fig.suptitle(
    "Robustness check: PISA 2022 replication — The Schools That Beat the Odds",
    fontsize=12, fontweight="bold", y=1.02,
)

plt.tight_layout()
out = os.path.join(CHARTS_DIR, "robustness_2022.png")
plt.savefig(out, dpi=150, bbox_inches="tight")
plt.close()
print(f"  Saved: {out}")
print("\nDone.")
