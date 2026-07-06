"""
Robustness appendix: Excellence Without Misery — PISA 2022 comparison.

Core question: does the negative correlation between national performance
and student life satisfaction hold in PISA 2022?

2022 availability vs 2018:
  Available (both cycles): ST016Q01NA, BELONG, ESCS
  New in 2022: ANXMAT (math anxiety; partial proxy for GFOFAIL)
  Dropped in 2022: BEINGBULLIED, SWBP, GFOFAIL

Outputs:
  charts/robustness_2022.png  — side-by-side 2018 vs 2022 scatter
  data/processed/excellence_wellbeing_country_2022.csv
"""

import zipfile, tempfile, os, warnings
import numpy as np
import pandas as pd
import pyreadstat
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from scipy.stats import pearsonr

warnings.filterwarnings("ignore")

ROOT       = os.path.expanduser("~/code/pisa-data-stories")
RAW_2022   = os.path.join(ROOT, "data/raw/SPSS_STU_QQQ_2022.zip")
REF_CSV    = os.path.join(ROOT, "data/processed/excellence_wellbeing_country.csv")
PROC_DIR   = os.path.join(ROOT, "data/processed")
CHARTS_DIR = os.path.join(ROOT, "stories/accepted/excellence-without-misery/charts")

PALETTE = {
    "hi_hi": "#2471a3",
    "hi_lo": "#c0392b",
    "lo_hi": "#1a7a4a",
    "lo_lo": "#888",
}

LOAD_COLS = (
    ["CNT", "W_FSTUWT", "ST016Q01NA", "BELONG", "ESCS", "ANXMAT"]
    + [f"PV{i}MATH" for i in range(1, 11)]
    + [f"PV{i}READ" for i in range(1, 11)]
    + [f"PV{i}SCIE" for i in range(1, 11)]
)

# ---------------------------------------------------------------------------
# 1. Load 2022 raw SPSS
# ---------------------------------------------------------------------------
print("Loading PISA 2022 student data…")
with zipfile.ZipFile(RAW_2022) as z:
    sav_name = next(n for n in z.namelist() if n.upper().endswith(".SAV"))
    with tempfile.TemporaryDirectory() as tmp:
        z.extract(sav_name, tmp)
        sav_path = os.path.join(tmp, sav_name)
        _, meta = pyreadstat.read_sav(sav_path, row_limit=1)
        use_cols = [c for c in LOAD_COLS if c in meta.column_names]
        missing  = [c for c in LOAD_COLS if c not in meta.column_names]
        if missing:
            print(f"  Note: {len(missing)} columns absent from 2022 file: {missing}")
        print(f"  Reading {len(use_cols)} columns from {sav_name}…")
        df, _ = pyreadstat.read_sav(sav_path, usecols=use_cols)

df = df[df["W_FSTUWT"] > 0].dropna(subset=["W_FSTUWT"])
print(f"  {len(df):,} students, {df['CNT'].nunique()} countries.")

# ---------------------------------------------------------------------------
# 2. Student-level composite score (all three domains, 10 PVs each)
# ---------------------------------------------------------------------------
math_pvs = [c for c in df.columns if c.startswith("PV") and c.endswith("MATH")]
read_pvs = [c for c in df.columns if c.startswith("PV") and c.endswith("READ")]
scie_pvs = [c for c in df.columns if c.startswith("PV") and c.endswith("SCIE")]
df["perf"] = df[math_pvs + read_pvs + scie_pvs].mean(axis=1)

# ---------------------------------------------------------------------------
# 3. Weighted country means
# ---------------------------------------------------------------------------
def wmean(grp, col):
    v = grp[col].to_numpy(dtype=float)
    w = grp["W_FSTUWT"].to_numpy(dtype=float)
    mask = np.isfinite(v) & (w > 0)
    return np.average(v[mask], weights=w[mask]) if mask.sum() > 0 else np.nan

print("Computing country-level aggregates…")
records = []
for cnt, grp in df.groupby("CNT"):
    records.append({
        "country": cnt,
        "perf":    wmean(grp, "perf"),
        "lifesat": wmean(grp, "ST016Q01NA") if "ST016Q01NA" in df.columns else np.nan,
        "belong":  wmean(grp, "BELONG")      if "BELONG"     in df.columns else np.nan,
        "anxmat":  wmean(grp, "ANXMAT")      if "ANXMAT"     in df.columns else np.nan,
        "escs":    wmean(grp, "ESCS")        if "ESCS"       in df.columns else np.nan,
    })

c22 = pd.DataFrame(records).dropna(subset=["perf", "lifesat"])
print(f"  {len(c22)} countries with complete performance + life satisfaction data.")

# Assign quadrants using 2022 medians
perf_med_22   = c22["perf"].median()
lifesat_med_22 = c22["lifesat"].median()

def quad(row, pm, lm):
    hp = row["perf"]    >= pm
    hw = row["lifesat"] >= lm
    if hp and hw:       return "hi_hi"
    if hp and not hw:   return "hi_lo"
    if not hp and hw:   return "lo_hi"
    return "lo_lo"

c22["quadrant"] = c22.apply(lambda r: quad(r, perf_med_22, lifesat_med_22), axis=1)

r22, p22 = pearsonr(c22["perf"], c22["lifesat"])
print(f"\n  2022 correlation (performance × life satisfaction): r = {r22:.3f}, p = {p22:.4f}")
print(f"  2022 medians — performance: {perf_med_22:.1f}  life satisfaction: {lifesat_med_22:.2f}")
print(f"\n  2022 quadrant counts:\n{c22['quadrant'].value_counts().to_string()}")

c22.to_csv(os.path.join(PROC_DIR, "excellence_wellbeing_country_2022.csv"), index=False)
print(f"\n  Saved → data/processed/excellence_wellbeing_country_2022.csv")

# ---------------------------------------------------------------------------
# 4. Load 2018 reference
# ---------------------------------------------------------------------------
c18 = pd.read_csv(REF_CSV)
r18, p18 = pearsonr(c18["perf"], c18["lifesat"])
perf_med_18    = c18["perf"].median()
lifesat_med_18 = c18["lifesat"].median()
c18["quadrant"] = c18.apply(lambda r: quad(r, perf_med_18, lifesat_med_18), axis=1)

# ---------------------------------------------------------------------------
# 5. Country overlap and quadrant stability
# ---------------------------------------------------------------------------
common = set(c18["country"]) & set(c22["country"])
both = (c18.set_index("country")[["perf","lifesat","quadrant"]]
          .join(c22.set_index("country")[["perf","lifesat","quadrant"]],
                lsuffix="_18", rsuffix="_22")
          .dropna())
stable = (both["quadrant_18"] == both["quadrant_22"]).mean()
print(f"\n  Countries in both cycles: {len(both)}")
print(f"  Quadrant stability (same quadrant in both cycles): {stable:.0%}")

# Notable country stats
print("\n  Key country comparison:")
hdr = f"  {'CNT':4s}  {'perf18':>7s}  {'perf22':>7s}  {'ls18':>6s}  {'ls22':>6s}  {'q18':8s}  {'q22':8s}"
print(hdr)
for cnt in ["FIN","JPN","KOR","TAP","NLD","EST","CHE"]:
    if cnt not in both.index: continue
    row = both.loc[cnt]
    print(f"  {cnt:4s}  {row['perf_18']:7.1f}  {row['perf_22']:7.1f}  "
          f"{row['lifesat_18']:6.2f}  {row['lifesat_22']:6.2f}  "
          f"{row['quadrant_18']:8s}  {row['quadrant_22']:8s}")

# ---------------------------------------------------------------------------
# 6. Comparison figure: two scatter panels (2018 | 2022)
# ---------------------------------------------------------------------------
print("\nGenerating robustness figure…")

quad_bg = {
    "hi_hi": "#d6eaf8",
    "hi_lo": "#fde8e8",
    "lo_hi": "#d5f5e3",
    "lo_lo": "#f2f3f4",
}

LABEL = {
    "FIN":"FIN","JPN":"JPN","KOR":"KOR","TAP":"TAP",
    "NLD":"NLD","CHE":"CHE","EST":"EST","HKG":"HKG",
    "MAC":"MAC","QCI":"CHN*","BLR":"BLR","ISL":"ISL",
}

fig, axes = plt.subplots(1, 2, figsize=(14, 6.5), sharey=False)
fig.patch.set_facecolor("#fafafa")
fig.suptitle(
    "National academic performance vs. student life satisfaction\nPISA 2018 and PISA 2022",
    fontsize=13, fontweight="bold", y=1.01,
)

panels = [
    (axes[0], c18, perf_med_18, lifesat_med_18, r18, p18, "PISA 2018",
     f"{len(c18)} countries"),
    (axes[1], c22, perf_med_22, lifesat_med_22, r22, p22, "PISA 2022",
     f"{len(c22)} countries"),
]

for ax, data, pm, lm, r_val, p_val, title, subtitle in panels:
    ax.set_facecolor("#fafafa")

    xl = (data["perf"].min() - 12, data["perf"].max() + 12)
    yl = (data["lifesat"].min() - 0.12, data["lifesat"].max() + 0.18)

    # Background quadrant shading
    ax.fill_between([pm, xl[1]], [lm, lm], [yl[1], yl[1]],
                    color=quad_bg["hi_hi"], alpha=0.5, zorder=0)
    ax.fill_between([pm, xl[1]], [yl[0], yl[0]], [lm, lm],
                    color=quad_bg["hi_lo"], alpha=0.5, zorder=0)
    ax.fill_between([xl[0], pm], [lm, lm], [yl[1], yl[1]],
                    color=quad_bg["lo_hi"], alpha=0.5, zorder=0)
    ax.fill_between([xl[0], pm], [yl[0], yl[0]], [lm, lm],
                    color=quad_bg["lo_lo"], alpha=0.5, zorder=0)

    ax.axvline(pm, color="#777", lw=0.8, ls="--", alpha=0.6, zorder=1)
    ax.axhline(lm, color="#777", lw=0.8, ls="--", alpha=0.6, zorder=1)

    # Scatter
    for _, row in data.iterrows():
        cnt = row["country"]
        q   = row["quadrant"]
        labeled = cnt in LABEL
        ax.scatter(row["perf"], row["lifesat"],
                   color=PALETTE[q],
                   s=75 if labeled else 28,
                   alpha=0.9 if labeled else 0.55,
                   edgecolors="white" if labeled else "none",
                   linewidths=0.6,
                   zorder=5 if labeled else 3)
        if labeled:
            ax.annotate(
                LABEL[cnt],
                (row["perf"], row["lifesat"]),
                xytext=(4, 4), textcoords="offset points",
                fontsize=8, fontweight="bold",
                color=PALETTE[q], zorder=6,
            )
        else:
            ax.text(row["perf"] + 1.2, row["lifesat"],
                    cnt, fontsize=4.5, color="#bbb", va="center", zorder=2)

    ax.set_xlim(*xl)
    ax.set_ylim(*yl)
    ax.set_xlabel("Mean composite score (Math + Reading + Science)", fontsize=10)
    ax.set_ylabel("Mean life satisfaction (0–10)", fontsize=10)
    ax.set_title(f"{title}\n{subtitle}", fontsize=11, fontweight="bold", pad=8)
    ax.spines[["top", "right"]].set_visible(False)

    p_str = "< 0.001" if p_val < 0.001 else f"= {p_val:.3f}"
    ax.text(0.97, 0.03,
            f"r = {r_val:.3f}\n(p {p_str})",
            transform=ax.transAxes, fontsize=9, color="#444",
            ha="right", va="bottom",
            bbox=dict(facecolor="white", edgecolor="#ccc",
                      alpha=0.85, boxstyle="round,pad=0.3"))

    # Quadrant labels (top corners only)
    pad = dict(facecolor="white", edgecolor="none", alpha=0.7, boxstyle="round,pad=0.15")
    ax.text(pm + 2, yl[1] - 0.05,
            "Excellence\nwithout misery", fontsize=7.5, color=PALETTE["hi_hi"],
            fontweight="bold", va="top", bbox=pad)
    ax.text(pm + 2, lm - 0.05,
            "Excellence\nwith misery", fontsize=7.5, color=PALETTE["hi_lo"],
            fontweight="bold", va="top", bbox=pad)

# Shared legend
legend_els = [
    Line2D([0],[0], marker="o", color="w", markerfacecolor=PALETTE["hi_hi"],
           markersize=8, label="Excellence + well-being"),
    Line2D([0],[0], marker="o", color="w", markerfacecolor=PALETTE["hi_lo"],
           markersize=8, label="Excellence + misery"),
    Line2D([0],[0], marker="o", color="w", markerfacecolor=PALETTE["lo_hi"],
           markersize=8, label="Lower perf. + well-being"),
    Line2D([0],[0], marker="o", color="w", markerfacecolor=PALETTE["lo_lo"],
           markersize=8, label="Lower perf. + misery"),
]
fig.legend(handles=legend_els, loc="lower center", ncol=4,
           fontsize=8.5, bbox_to_anchor=(0.5, -0.06), framealpha=0.9)

plt.tight_layout()
out = os.path.join(CHARTS_DIR, "robustness_2022.png")
plt.savefig(out, dpi=150, bbox_inches="tight")
plt.close()
print(f"  Saved: {out}")

# ---------------------------------------------------------------------------
# 7. Print summary statistics for the appendix text
# ---------------------------------------------------------------------------
q18 = c18["quadrant"].value_counts()
q22 = c22["quadrant"].value_counts()

print("\n=== APPENDIX STATISTICS ===")
print(f"\n  2018: r = {r18:.3f}, N = {len(c18)}")
print(f"  2022: r = {r22:.3f}, N = {len(c22)}")

for q_key, q_label in [("hi_hi","Excellence + well-being"), ("hi_lo","Excellence + misery")]:
    n18 = q18.get(q_key, 0)
    n22 = q22.get(q_key, 0)
    print(f"\n  {q_label}:")
    print(f"    2018: {n18} countries")
    print(f"    2022: {n22} countries")
    cnts_22 = c22[c22["quadrant"]==q_key].sort_values("perf", ascending=False)["country"].tolist()
    print(f"    2022 members: {cnts_22}")

print(f"\n  Quadrant stability (same in both cycles): {stable:.0%} of {len(both)} shared countries")

# Finland vs Japan in 2022
for cnt in ["FIN","JPN"]:
    if cnt in both.index:
        row = both.loc[cnt]
        print(f"\n  {cnt}: perf 2018={row['perf_18']:.0f}→2022={row['perf_22']:.0f}  "
              f"lifesat 2018={row['lifesat_18']:.2f}→2022={row['lifesat_22']:.2f}  "
              f"quadrant {row['quadrant_18']}→{row['quadrant_22']}")

print("\nDone.")
