"""
Robustness appendix: Calculators, Creators, or Both?

This story already uses PISA 2022. Three robustness checks:

1. CROSS-CYCLE: Do 2018 academic rankings predict 2022 creative thinking scores?
   If yes, the academic–CT alignment is not a 2022 artefact — it reflects stable
   system characteristics across at least two PISA cycles (4-year gap).

2. OECD-ONLY: Does r=0.92 hold within the 37 OECD-member countries in the sample?

3. DOMAIN SENSITIVITY: Does the correlation hold if we use only Math performance
   rather than the mean of Math + Reading + Science?

Outputs:
  charts/robustness_cross_cycle.png  — 2018 academic vs 2022 CT scatter
  Printed summary for HTML appendix
"""

import io
import os
import warnings
import zipfile

import matplotlib
matplotlib.use("Agg")
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pyreadstat
from scipy.stats import pearsonr, spearmanr

warnings.filterwarnings("ignore")

ROOT       = os.path.expanduser("~/code/pisa-data-stories")
RAW_2018   = os.path.join(ROOT, "data/raw/SPSS_STU_QQQ.zip")
RAW_QQQ22  = os.path.join(ROOT, "data/raw/SPSS_STU_QQQ_2022.zip")
CRT_ZIP    = os.path.join(ROOT, "data/raw/SPSS_CRT_2022.zip")
CNT_CSV    = os.path.join(ROOT, "data/processed/calculators_creators_country.csv")
CHARTS_DIR = os.path.join(ROOT, "stories/accepted/calculators-creators/charts")

MATH_PVS_18 = [f"PV{i}MATH" for i in range(1, 11)]
READ_PVS_18 = [f"PV{i}READ" for i in range(1, 11)]
SCIE_PVS_18 = [f"PV{i}SCIE" for i in range(1, 11)]
CT_PVS      = [f"PV{i}CRTH_NC" for i in range(1, 11)]
MATH_PVS_22 = [f"PV{i}MATH" for i in range(1, 11)]

COUNTRY_NAMES = {
    "ALB":"Albania","ARE":"UAE","AUS":"Australia","BEL":"Belgium","BGR":"Bulgaria",
    "BRA":"Brazil","BRN":"Brunei","CAN":"Canada","CHL":"Chile","COL":"Colombia",
    "CRI":"Costa Rica","CZE":"Czech Rep.","DEU":"Germany","DNK":"Denmark",
    "DOM":"Dominican Rep.","ESP":"Spain","EST":"Estonia","FIN":"Finland",
    "FRA":"France","GRC":"Greece","HKG":"Hong Kong","HRV":"Croatia",
    "HUN":"Hungary","IDN":"Indonesia","ISL":"Iceland","ISR":"Israel",
    "ITA":"Italy","JAM":"Jamaica","JOR":"Jordan","KAZ":"Kazakhstan",
    "KOR":"Korea","LTU":"Lithuania","LVA":"Latvia","MAC":"Macao",
    "MAR":"Morocco","MDA":"Moldova","MEX":"Mexico","MKD":"N. Macedonia",
    "MLT":"Malta","MNG":"Mongolia","MYS":"Malaysia","NLD":"Netherlands",
    "NZL":"New Zealand","PAN":"Panama","PER":"Peru","PHL":"Philippines",
    "POL":"Poland","PRT":"Portugal","PSE":"Palestine","QAT":"Qatar",
    "QAZ":"Baku (AZE)","QUR":"Tatarstan","ROU":"Romania","SAU":"Saudi Arabia",
    "SGP":"Singapore","SLV":"El Salvador","SRB":"Serbia","SVK":"Slovakia",
    "SVN":"Slovenia","TAP":"Chinese Taipei","THA":"Thailand","URY":"Uruguay",
    "UZB":"Uzbekistan",
}

OECD_2022 = {
    "AUS","AUT","BEL","CAN","CHL","COL","CRI","CZE","DNK","EST",
    "FIN","FRA","DEU","GRC","HUN","ISL","ISR","ITA","JPN","KOR",
    "LVA","LTU","LUX","MEX","NLD","NZL","NOR","POL","PRT","SVK",
    "SVN","ESP","SWE","CHE","TUR","GBR","USA",
}

COLORS = {
    "Both":        "#2ecc71",
    "Calculators": "#3498db",
    "Creators":    "#e67e22",
    "Low Both":    "#bdc3c7",
}


def wmean(grp, col):
    m = grp[[col, "W_FSTUWT"]].dropna()
    m = m[m["W_FSTUWT"] > 0]
    return np.average(m[col], weights=m["W_FSTUWT"]) if len(m) else np.nan


def load_sav_cols(zip_path, cols):
    with zipfile.ZipFile(zip_path) as z:
        sav = [n for n in z.namelist() if n.upper().endswith(".SAV")][0]
        with z.open(sav) as f:
            buf = io.BytesIO(f.read())
    return pyreadstat.read_sav(buf, usecols=cols)[0]


# ─── LOAD ALREADY-COMPUTED 2022 COUNTRY MEANS ────────────────────────────────
print("Loading 2022 country means...")
cnt22 = pd.read_csv(CNT_CSV)
print(f"  {len(cnt22)} countries, quadrants: {cnt22['quadrant'].value_counts().to_dict()}")

# ─── CHECK 1: 2018 ACADEMIC → 2022 CT ────────────────────────────────────────
print("\nLoading 2018 QQQ for academic means...")
cols18 = ["CNT", "W_FSTUWT"] + MATH_PVS_18 + READ_PVS_18 + SCIE_PVS_18
qqq18 = load_sav_cols(RAW_2018, cols18)
print(f"  {len(qqq18):,} rows, {qqq18['CNT'].nunique()} countries")

qqq18["math_score"] = qqq18[MATH_PVS_18].mean(axis=1)
qqq18["read_score"] = qqq18[READ_PVS_18].mean(axis=1)
qqq18["scie_score"] = qqq18[SCIE_PVS_18].mean(axis=1)
qqq18["academic"]   = (qqq18["math_score"] + qqq18["read_score"] + qqq18["scie_score"]) / 3

cnt18 = (
    qqq18[qqq18["W_FSTUWT"] > 0]
    .groupby("CNT")
    .apply(lambda g: pd.Series({
        "academic_18": wmean(g, "academic"),
        "math_18":     wmean(g, "math_score"),
    }))
    .reset_index()
)
print(f"  2018 country means: {len(cnt18)} countries")

# Join 2018 academic with 2022 CT
both = cnt22[["CNT", "ct_score", "academic", "quadrant", "ESCS"]].merge(
    cnt18, on="CNT", how="inner"
)
print(f"  Overlap: {len(both)} countries in both 2018 and 2022 CT")

r_cross, p_cross       = pearsonr(both["academic_18"], both["ct_score"])
r_cross_ac, _          = pearsonr(both["academic_18"], both["academic"])
rho_cross, _           = spearmanr(both["academic_18"], both["ct_score"])
print(f"\n  2018 academic → 2022 CT:         r = {r_cross:.3f}  (p = {p_cross:.4f})")
print(f"  2018 academic → 2022 academic:   r = {r_cross_ac:.3f}")
print(f"  Spearman rank (2018→2022 CT):   ρ = {rho_cross:.3f}")

# ─── CHECK 2: OECD-ONLY SUBSET ───────────────────────────────────────────────
oecd = cnt22[cnt22["CNT"].isin(OECD_2022)].dropna(subset=["ct_score", "academic"])
r_oecd, _ = pearsonr(oecd["academic"], oecd["ct_score"])
print(f"\n  OECD-only ({len(oecd)} countries):   r(CT, academic) = {r_oecd:.3f}")

# ─── CHECK 3: MATH-ONLY SENSITIVITY ──────────────────────────────────────────
print("\nLoading 2022 Math-only means (from QQQ)...")
# Math 2022 per-country means from the QQQ file (we need math_score separately)
# Load 2022 with just math PVs
cols22 = ["CNT", "W_FSTUWT"] + MATH_PVS_22
qqq22_math = load_sav_cols(RAW_QQQ22, cols22)
qqq22_math["math_score"] = qqq22_math[MATH_PVS_22].mean(axis=1)
cnt22_math = (
    qqq22_math[qqq22_math["W_FSTUWT"] > 0]
    .groupby("CNT")
    .apply(lambda g: pd.Series({"math_22": wmean(g, "math_score")}))
    .reset_index()
)
# Merge with CT
math_ct = cnt22[["CNT", "ct_score"]].merge(cnt22_math, on="CNT", how="inner")
r_math, _ = pearsonr(math_ct["math_22"], math_ct["ct_score"])
print(f"  Math-only ({len(math_ct)} countries):  r(CT, Math) = {r_math:.3f}")

# ─── CHART: 2018 ACADEMIC vs 2022 CT ─────────────────────────────────────────
ALWAYS_LABEL = {
    "SGP","KOR","EST","FIN","AUS","CAN","NZL","HKG","MAC","TAP",
    "DEU","FRA","POL","NLD","ISL","ALB","PHL","UZB","DOM","MAR",
    "CHL","MEX","BRN","QUR","ARE","BGR","THA","IDN",
}

fig, ax = plt.subplots(figsize=(13, 8))
fig.patch.set_facecolor("#0f1117")
ax.set_facecolor("#0f1117")

# Quadrant dividers at 2022 medians (same as main analysis)
ct_med22 = cnt22["ct_score"].median()
ac_med22 = cnt22["academic"].median()

for q, color in COLORS.items():
    sub = both[both["quadrant"] == q]
    ax.scatter(sub["academic_18"], sub["ct_score"], c=color, s=100,
               alpha=0.9, zorder=3, edgecolors="#0f1117", linewidths=0.6, label=q)

for _, row in both.iterrows():
    lbl = COUNTRY_NAMES.get(row["CNT"], row["CNT"])
    ax.annotate(lbl, xy=(row["academic_18"], row["ct_score"]),
                xytext=(4, 4), textcoords="offset points",
                fontsize=6.5, color="#dddddd", zorder=4)

# Regression line
x_all = both["academic_18"].values
y_all = both["ct_score"].values
m, b  = np.polyfit(x_all, y_all, 1)
xr    = np.linspace(x_all.min(), x_all.max(), 200)
ax.plot(xr, m * xr + b, color="#ffffff40", lw=1.5)

ax.set_xlabel("2018 Academic Performance (PISA scale)", color="#cccccc", fontsize=11)
ax.set_ylabel("2022 Creative Thinking Score (PISA CT scale, 0–48)", color="#cccccc", fontsize=11)
ax.set_title(
    f"Cross-Cycle Robustness: 2018 Academic Rank → 2022 Creative Thinking\n"
    f"{len(both)} shared countries · r = {r_cross:.2f}  (Spearman ρ = {rho_cross:.2f})",
    color="white", fontsize=12, pad=12,
)

legend_patches = [mpatches.Patch(color=c, label=q) for q, c in COLORS.items()]
ax.legend(handles=legend_patches, loc="lower right", framealpha=0.3,
          labelcolor="white", facecolor="#0f1117", edgecolor="#555555", fontsize=9)

for spine in ax.spines.values():
    spine.set_edgecolor("#333333")
ax.tick_params(colors="#999999")
ax.grid(True, color="#222222", lw=0.5, alpha=0.6)

plt.tight_layout()
out_path = os.path.join(CHARTS_DIR, "robustness_cross_cycle.png")
plt.savefig(out_path, dpi=150, bbox_inches="tight", facecolor=fig.get_facecolor())
plt.close()
print(f"\nSaved: {out_path}")

# ─── PRINT SUMMARY ───────────────────────────────────────────────────────────
print("\n" + "="*60)
print("ROBUSTNESS SUMMARY")
print("="*60)
print(f"Cross-cycle (2018 academic → 2022 CT):  r = {r_cross:.3f}")
print(f"Spearman rank correlation:              ρ = {rho_cross:.3f}")
print(f"2018 academic → 2022 academic:          r = {r_cross_ac:.3f}")
print(f"OECD-only (n={len(oecd)}) CT–academic:    r = {r_oecd:.3f}")
print(f"Math-only (n={len(math_ct)}) CT–Math:      r = {r_math:.3f}")
print(f"Main result (all 63):                   r = 0.922")

# Country stability table
print("\nCountry position stability (2018 academic rank → 2022 CT quadrant):")
both_sorted = both.sort_values("academic_18", ascending=False)
print(both_sorted[["CNT", "academic_18", "ct_score", "quadrant"]].head(12).to_string(index=False))
print("...")
print(both_sorted[["CNT", "academic_18", "ct_score", "quadrant"]].tail(5).to_string(index=False))

print("\nDone.")
