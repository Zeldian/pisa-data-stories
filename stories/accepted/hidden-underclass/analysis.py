"""
The Hidden Underclass Inside Rich Education Systems
PISA 2018 · 79 countries · 612,004 students

Hardship index: 6 binary indicators of serious burden at the student level.
- b_bullied:      BEINGBULLIED WLE > 0 (above-average bullying experience)
- b_low_belong:   BELONG WLE ≤ global 25th percentile
- b_no_quiet:     ST011Q03TA == 2 (no quiet place to study at home)
- b_no_desk:      ST011Q01TA == 2 (no desk to study at home)
- b_skip:         ST062Q01TA ≥ 2 OR ST062Q02TA ≥ 2 (skipped school in past 2 weeks)
- b_threatened:   ST038Q05NA ≥ 2 (threatened by another student in past year)

Hardship count = sum of indicators. NaN treated as 0 (conservative).
"Multi-burden" = count ≥ 3. "Severe burden" = count ≥ 4.
"""

import io
import os
import warnings
import zipfile

import matplotlib
matplotlib.use("Agg")
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np
import pandas as pd
import pyreadstat
from scipy.stats import pearsonr

warnings.filterwarnings("ignore")

ROOT      = os.path.expanduser("~/code/pisa-data-stories")
RAW_2018  = os.path.join(ROOT, "data/raw/SPSS_STU_QQQ.zip")
PROC_DIR  = os.path.join(ROOT, "data/processed")
OUT_DIR   = os.path.join(ROOT, "stories/accepted/hidden-underclass/charts")

MATH_PVS = [f"PV{i}MATH" for i in range(1, 11)]
READ_PVS = [f"PV{i}READ" for i in range(1, 11)]
SCIE_PVS = [f"PV{i}SCIE" for i in range(1, 11)]

LOAD_COLS = (
    ["CNT", "CNTSCHID", "W_FSTUWT", "ESCS", "IMMIG"]
    + ["BEINGBULLIED", "BELONG", "GFOFAIL", "ST016Q01NA"]
    + ["ST011Q01TA", "ST011Q03TA"]
    + ["ST038Q05NA"]
    + ["ST062Q01TA", "ST062Q02TA"]
    + MATH_PVS + READ_PVS + SCIE_PVS
)

OECD = {
    "AUS","AUT","BEL","CAN","CHL","COL","CRI","CZE","DNK","EST",
    "FIN","FRA","DEU","GRC","HUN","ISL","ISR","ITA","JPN","KOR",
    "LVA","LTU","LUX","MEX","NLD","NZL","NOR","POL","PRT","SVK",
    "SVN","ESP","SWE","CHE","TUR","GBR","USA",
}

COUNTRY_NAMES = {
    "ALB":"Albania","ARE":"UAE","ARG":"Argentina","AUS":"Australia","AUT":"Austria",
    "BEL":"Belgium","BGR":"Bulgaria","BIH":"Bosnia","BLR":"Belarus",
    "BRA":"Brazil","BRN":"Brunei","CAN":"Canada","CHL":"Chile","CHN":"China",
    "COL":"Colombia","CRI":"Costa Rica","CZE":"Czech Rep.","DEU":"Germany",
    "DNK":"Denmark","DOM":"Dom. Rep.","ESP":"Spain","EST":"Estonia",
    "FIN":"Finland","FRA":"France","GBR":"UK","GEO":"Georgia",
    "GRC":"Greece","HKG":"Hong Kong","HRV":"Croatia","HUN":"Hungary",
    "IDN":"Indonesia","IRL":"Ireland","ISL":"Iceland","ISR":"Israel",
    "ITA":"Italy","JOR":"Jordan","JPN":"Japan","KAZ":"Kazakhstan",
    "KOR":"Korea","KSV":"Kosovo","LBN":"Lebanon","LTU":"Lithuania",
    "LUX":"Luxembourg","LVA":"Latvia","MAC":"Macao","MAR":"Morocco",
    "MDA":"Moldova","MEX":"Mexico","MKD":"N. Macedonia","MLT":"Malta",
    "MNE":"Montenegro","MYS":"Malaysia","NLD":"Netherlands","NOR":"Norway",
    "NZL":"New Zealand","PAN":"Panama","PER":"Peru","PHL":"Philippines",
    "POL":"Poland","PRT":"Portugal","QAT":"Qatar","QAZ":"Baku (AZE)",
    "QCI":"B-S-J-Z (China)","QMR":"Moscow Reg.","QRT":"Tatarstan",
    "QUC":"Ukraine (Excl.Lviv)","ROM":"Romania","ROU":"Romania",
    "RUS":"Russia","SAU":"Saudi Arabia","SGP":"Singapore","SRB":"Serbia",
    "SVK":"Slovakia","SVN":"Slovenia","SWE":"Sweden","TAP":"Chinese Taipei",
    "THA":"Thailand","TUR":"Turkey","UKR":"Ukraine","URY":"Uruguay",
    "USA":"USA","UZB":"Uzbekistan","VNM":"Vietnam",
}

# ─── LOAD DATA ───────────────────────────────────────────────────────────────
print("Loading 2018 QQQ...")
with zipfile.ZipFile(RAW_2018) as z:
    sav = [n for n in z.namelist() if n.upper().endswith(".SAV")][0]
    with z.open(sav) as f:
        buf = io.BytesIO(f.read())
df, meta = pyreadstat.read_sav(buf, usecols=LOAD_COLS)
print(f"  {len(df):,} rows, {df['CNT'].nunique()} countries")

# Filter to valid weight
df = df[df["W_FSTUWT"] > 0].copy()
print(f"  After weight filter: {len(df):,}")

# ─── ACADEMIC SCORE ──────────────────────────────────────────────────────────
df["academic"] = (df[MATH_PVS].mean(axis=1)
                  + df[READ_PVS].mean(axis=1)
                  + df[SCIE_PVS].mean(axis=1)) / 3

# ─── HARDSHIP INDICATORS ─────────────────────────────────────────────────────
# Compute global thresholds on the full dataset (weighted)
belong_p25 = df["BELONG"].quantile(0.25)
print(f"\nGlobal BELONG p25: {belong_p25:.3f}")
print(f"Global BEINGBULLIED median: {df['BEINGBULLIED'].median():.3f}")

# Binary indicators (NaN → 0)
df["b_bullied"]    = (df["BEINGBULLIED"] > 0).astype(float).fillna(0)
df["b_low_belong"] = (df["BELONG"] <= belong_p25).astype(float).fillna(0)
df["b_no_quiet"]   = (df["ST011Q03TA"] == 2).astype(float).fillna(0)
df["b_no_desk"]    = (df["ST011Q01TA"] == 2).astype(float).fillna(0)
# Skip: at least one whole day OR some classes skipped in past 2 weeks
skip = ((df["ST062Q01TA"].fillna(1) >= 2) | (df["ST062Q02TA"].fillna(1) >= 2))
df["b_skip"]       = skip.astype(float)
df["b_threatened"] = (df["ST038Q05NA"] >= 2).astype(float).fillna(0)

BURDEN_COLS = ["b_bullied","b_low_belong","b_no_quiet","b_no_desk","b_skip","b_threatened"]
BURDEN_LABELS = {
    "b_bullied":    "Above-avg bullying",
    "b_low_belong": "Low sense of belonging",
    "b_no_quiet":   "No quiet study space",
    "b_no_desk":    "No desk at home",
    "b_skip":       "Skipped school",
    "b_threatened": "Threatened at school",
}

df["hardship"] = df[BURDEN_COLS].sum(axis=1)
df["multi_burden"] = (df["hardship"] >= 3).astype(int)
df["severe_burden"] = (df["hardship"] >= 4).astype(int)
df["oecd"] = df["CNT"].isin(OECD).astype(int)

print(f"\nHardship distribution (unweighted):")
print(df["hardship"].value_counts().sort_index())
print(f"\nMulti-burden (3+): {df['multi_burden'].mean()*100:.1f}%")
print(f"Severe (4+):       {df['severe_burden'].mean()*100:.1f}%")

# ─── WEIGHTED COUNTRY MEANS ──────────────────────────────────────────────────
def wmean(grp, col):
    m = grp[[col,"W_FSTUWT"]].dropna()
    m = m[m["W_FSTUWT"] > 0]
    return np.average(m[col], weights=m["W_FSTUWT"]) if len(m) else np.nan

print("\nComputing country-level statistics...")
cnt = (
    df.groupby("CNT")
    .apply(lambda g: pd.Series({
        "academic":        wmean(g, "academic"),
        "pct_multi":       wmean(g, "multi_burden") * 100,
        "pct_severe":      wmean(g, "severe_burden") * 100,
        "mean_hardship":   wmean(g, "hardship"),
        "escs_mean":       wmean(g, "ESCS"),
        "pct_bullied":     wmean(g, "b_bullied") * 100,
        "pct_low_belong":  wmean(g, "b_low_belong") * 100,
        "pct_no_quiet":    wmean(g, "b_no_quiet") * 100,
        "pct_no_desk":     wmean(g, "b_no_desk") * 100,
        "pct_skip":        wmean(g, "b_skip") * 100,
        "pct_threatened":  wmean(g, "b_threatened") * 100,
        "n_students":      len(g),
    }))
    .reset_index()
)
cnt["oecd"] = cnt["CNT"].isin(OECD)
cnt["name"]  = cnt["CNT"].map(lambda c: COUNTRY_NAMES.get(c, c))

print(f"Countries: {len(cnt)}")
print(f"\nGlobal weighted multi-burden rate: {cnt['pct_multi'].mean():.1f}%")
print(f"\nTop 10 multi-burden (% 3+ burdens):")
print(cnt.nlargest(10,"pct_multi")[["CNT","name","academic","pct_multi","escs_mean"]].to_string(index=False))
print(f"\nTop 10 OECD countries by academic:")
oecd_df = cnt[cnt["oecd"]].nlargest(10,"academic")
print(oecd_df[["CNT","name","academic","pct_multi","pct_severe","escs_mean"]].to_string(index=False))

cnt.to_csv(os.path.join(PROC_DIR, "hidden_underclass_country.csv"), index=False)
print("\nSaved: hidden_underclass_country.csv")

# ─── BURDEN DISTRIBUTION BY GROUP ────────────────────────────────────────────
# Global weighted distribution of hardship counts
def burden_dist(sub):
    total_w = sub["W_FSTUWT"].sum()
    return {
        k: sub[sub["hardship"] == k]["W_FSTUWT"].sum() / total_w * 100
        for k in range(7)
    }

global_dist  = burden_dist(df)
oecd_dist    = burden_dist(df[df["oecd"] == 1])
nonoecd_dist = burden_dist(df[df["oecd"] == 0])
print("\nGlobal hardship distribution (weighted %):")
for k,v in global_dist.items():
    print(f"  {k} burdens: {v:.1f}%")

# ─── CHART 1: BURDEN DISTRIBUTION STACKED BARS ───────────────────────────────
# For top 20 highest-academic countries + global + OECD avg
top20 = cnt.nlargest(20, "academic")["CNT"].tolist()

groups = {"Global": df, "OECD avg": df[df["oecd"]==1]}
for cnt_code in top20:
    groups[cnt_code] = df[df["CNT"]==cnt_code]

# Compute distribution for each group
dist_records = []
for label, sub in groups.items():
    total_w = sub["W_FSTUWT"].sum()
    if total_w == 0:
        continue
    rec = {"label": label}
    for k in range(7):
        rec[f"b{k}"] = sub[sub["hardship"]==k]["W_FSTUWT"].sum()/total_w*100
    dist_records.append(rec)
dist_df = pd.DataFrame(dist_records)
dist_df["name"] = dist_df["label"].map(lambda c: COUNTRY_NAMES.get(c, c))
# Sort by % with 3+ burdens (ascending = left side has least)
dist_df["pct_3plus"] = dist_df[["b3","b4","b5","b6"]].sum(axis=1)
# Separate reference rows from country rows
ref_rows = dist_df[dist_df["label"].isin(["Global","OECD avg"])].copy()
cnt_rows = dist_df[~dist_df["label"].isin(["Global","OECD avg"])].sort_values("pct_3plus")
dist_df = pd.concat([ref_rows, cnt_rows], ignore_index=True)

BAR_COLORS = ["#2c3e50","#1a7a4a","#f0e442","#e67e22","#c0392b","#8e44ad","#7f8c8d"]
BAR_LABELS  = ["0 burdens","1 burden","2 burdens","3 burdens","4 burdens","5 burdens","6 burdens"]

fig, ax = plt.subplots(figsize=(16, 9))
fig.patch.set_facecolor("#0f1117")
ax.set_facecolor("#0f1117")

y_pos = np.arange(len(dist_df))
left  = np.zeros(len(dist_df))

for k, (color, lbl) in enumerate(zip(BAR_COLORS, BAR_LABELS)):
    vals = dist_df[f"b{k}"].values
    bars = ax.barh(y_pos, vals, left=left, color=color, alpha=0.9, height=0.7, label=lbl)
    # Label bars ≥ 4%
    for i, (v, l) in enumerate(zip(vals, left)):
        if v >= 5:
            ax.text(l + v/2, i, f"{v:.0f}%", ha="center", va="center",
                    fontsize=6.5, color="white", fontweight="bold")
    left += vals

# Vertical line at 3+ boundary
ax.axvline(100 - dist_df["pct_3plus"].mean(), color="#ffffff30", lw=0.8, ls=":")

tick_labels = []
for _, row in dist_df.iterrows():
    n = COUNTRY_NAMES.get(row["label"], row["label"])
    pct = row["pct_3plus"]
    if row["label"] in ("Global","OECD avg"):
        tick_labels.append(f"── {n} ── ({pct:.1f}% carry 3+)")
    else:
        tick_labels.append(f"{n} ({pct:.1f}%)")

ax.set_yticks(y_pos)
ax.set_yticklabels(tick_labels, fontsize=7.5, color="#dddddd")
ax.set_xlabel("% of students", color="#cccccc", fontsize=11)
ax.set_title(
    "Distribution of Hardship Burdens — Top 20 High-Performing Countries vs Benchmarks\n"
    "PISA 2018 · 6-indicator hardship index · Weighted student population",
    color="white", fontsize=12, pad=12,
)
ax.set_xlim(0, 100)
ax.legend(loc="lower right", framealpha=0.3, labelcolor="white",
          facecolor="#0f1117", edgecolor="#555555", fontsize=8)
for spine in ax.spines.values():
    spine.set_edgecolor("#333333")
ax.tick_params(colors="#999999", labelsize=7.5)
ax.xaxis.set_major_formatter(mticker.PercentFormatter())
ax.grid(True, axis="x", color="#222222", lw=0.5, alpha=0.6)

# Separate reference group visually
ax.axhline(1.5, color="#ffffff25", lw=1, ls="--")

plt.tight_layout()
plt.savefig(f"{OUT_DIR}/burden_distribution.png", dpi=150, bbox_inches="tight",
            facecolor=fig.get_facecolor())
plt.close()
print("Saved: burden_distribution.png")

# ─── CHART 2: ACADEMIC vs % MULTI-BURDEN (country scatter) ───────────────────
ALWAYS_LABEL = {
    "SGP","KOR","JPN","EST","FIN","CAN","AUS","NZL","GBR","USA",
    "DEU","FRA","CHE","NLD","SWE","NOR","ISL","DNK","IRL","AUT",
    "BRA","COL","MEX","CHL","ARG","DOM","GTM","PAN","PHL","IDN",
    "QCI","HKG","TAP","MAC","VNM","RUS","BGR","ROU","UKR",
}

fig, ax = plt.subplots(figsize=(13, 8))
fig.patch.set_facecolor("#0f1117")
ax.set_facecolor("#0f1117")

col_oecd    = "#2ecc71"
col_nonoecd = "#bdc3c7"
col_line    = "#e74c3c"

for _, row in cnt.iterrows():
    color = col_oecd if row["oecd"] else col_nonoecd
    ax.scatter(row["academic"], row["pct_multi"], c=color, s=80,
               alpha=0.85, zorder=3, edgecolors="#0f1117", linewidths=0.5)
    if row["CNT"] in ALWAYS_LABEL or True:
        ax.annotate(COUNTRY_NAMES.get(row["CNT"], row["CNT"]),
                    xy=(row["academic"], row["pct_multi"]),
                    xytext=(4,3), textcoords="offset points",
                    fontsize=5.5, color="#cccccc", zorder=4)

# Reference lines
ac_med = cnt["academic"].median()
mb_med = cnt["pct_multi"].median()
ax.axvline(ac_med, color="#ffffff20", lw=1, ls="--")
ax.axhline(mb_med, color="#ffffff20", lw=1, ls="--")

# Regression
valid_ac = cnt.dropna(subset=["academic","pct_multi"])
m, b = np.polyfit(valid_ac["academic"], valid_ac["pct_multi"], 1)
xr = np.linspace(valid_ac["academic"].min(), valid_ac["academic"].max(), 200)
ax.plot(xr, m*xr+b, color="#e74c3c55", lw=1.5)
r, p = pearsonr(valid_ac["academic"], valid_ac["pct_multi"])
print(f"\nCorrelation (academic vs pct_multi): r = {r:.3f}")

ax.set_xlabel("Academic Performance (mean Math + Reading + Science, PISA scale)", color="#cccccc", fontsize=11)
ax.set_ylabel("% of students with 3+ hardship burdens", color="#cccccc", fontsize=11)
ax.set_title(
    f"Higher-Performing Countries Have Fewer Burdened Students — But Not Zero\n"
    f"PISA 2018 · 79 countries · r = {r:.2f}",
    color="white", fontsize=12, pad=12,
)
legend_patches = [
    mpatches.Patch(color=col_oecd,    label="OECD member"),
    mpatches.Patch(color=col_nonoecd, label="Non-OECD"),
]
ax.legend(handles=legend_patches, loc="upper right", framealpha=0.3,
          labelcolor="white", facecolor="#0f1117", edgecolor="#555555", fontsize=9)
for spine in ax.spines.values():
    spine.set_edgecolor("#333333")
ax.tick_params(colors="#999999")
ax.yaxis.set_major_formatter(mticker.PercentFormatter())
ax.grid(True, color="#222222", lw=0.5, alpha=0.6)

plt.tight_layout()
plt.savefig(f"{OUT_DIR}/academic_vs_hardship.png", dpi=150, bbox_inches="tight",
            facecolor=fig.get_facecolor())
plt.close()
print("Saved: academic_vs_hardship.png")

# ─── CHART 3: PERFORMANCE PENALTY ────────────────────────────────────────────
# Weighted mean academic score by hardship count (0–6), globally and for top OECD

penalty_global = []
penalty_oecd   = []

for k in range(7):
    sub_g  = df[df["hardship"] == k]
    sub_oe = df[(df["hardship"] == k) & (df["oecd"] == 1)]
    if len(sub_g) == 0:
        penalty_global.append(np.nan)
        penalty_oecd.append(np.nan)
        continue
    penalty_global.append(np.average(sub_g["academic"].dropna(),
                                     weights=sub_g.loc[sub_g["academic"].notna(),"W_FSTUWT"]))
    if len(sub_oe) > 0 and sub_oe["academic"].notna().sum() > 0:
        penalty_oecd.append(np.average(sub_oe["academic"].dropna(),
                                       weights=sub_oe.loc[sub_oe["academic"].notna(),"W_FSTUWT"]))
    else:
        penalty_oecd.append(np.nan)

print("\nPerformance by hardship count:")
for k in range(7):
    print(f"  {k} burdens: global={penalty_global[k]:.1f}  OECD={penalty_oecd[k]:.1f}")

fig, ax = plt.subplots(figsize=(11, 6))
fig.patch.set_facecolor("#0f1117")
ax.set_facecolor("#0f1117")

x = np.arange(7)
valid_g = [(i,v) for i,v in enumerate(penalty_global) if not np.isnan(v)]
valid_o = [(i,v) for i,v in enumerate(penalty_oecd) if not np.isnan(v)]

ax.plot([i for i,_ in valid_g], [v for _,v in valid_g],
        color="#bdc3c7", lw=2.5, marker="o", ms=8, label="All 79 countries")
ax.plot([i for i,_ in valid_o], [v for _,v in valid_o],
        color="#2ecc71", lw=2.5, marker="s", ms=8, label="OECD countries only")

# Annotate the gap at 0 burdens vs 5+ burdens
if not np.isnan(penalty_global[0]) and not np.isnan(penalty_global[5]):
    delta = penalty_global[0] - penalty_global[5]
    ax.annotate(f"−{delta:.0f} pts\n(0→5+ burdens)",
                xy=(5, penalty_global[5]),
                xytext=(4.2, penalty_global[5]+20),
                arrowprops=dict(arrowstyle="->", color="#e74c3c", lw=1.5),
                color="#e74c3c", fontsize=10, fontweight="bold")

ax.set_xticks(range(7))
ax.set_xticklabels([f"{k} burden{'s' if k!=1 else ''}" for k in range(7)], color="#cccccc")
ax.set_xlabel("Number of simultaneous hardship burdens", color="#cccccc", fontsize=11)
ax.set_ylabel("Mean academic performance (PISA scale)", color="#cccccc", fontsize=11)
ax.set_title(
    "The Performance Cliff: Academic Score by Number of Hardship Burdens\n"
    "PISA 2018 · Weighted country means",
    color="white", fontsize=12, pad=12,
)
ax.legend(framealpha=0.3, labelcolor="white", facecolor="#0f1117",
          edgecolor="#555555", fontsize=10)
for spine in ax.spines.values():
    spine.set_edgecolor("#333333")
ax.tick_params(colors="#999999")
ax.grid(True, color="#222222", lw=0.5, alpha=0.6)
ax.yaxis.set_major_formatter(mticker.FormatStrFormatter("%.0f"))

plt.tight_layout()
plt.savefig(f"{OUT_DIR}/performance_cliff.png", dpi=150, bbox_inches="tight",
            facecolor=fig.get_facecolor())
plt.close()
print("Saved: performance_cliff.png")

# ─── CHART 4: WITHIN OECD — ESCS QUARTILE × HARDSHIP ────────────────────────
# For top-20 academic OECD countries: show % multi-burden by ESCS quartile
top_oecd_cnts = cnt[cnt["oecd"]].nlargest(15, "academic")["CNT"].tolist()
top_df = df[df["CNT"].isin(top_oecd_cnts)].copy()

# Global ESCS quartiles
escs_q = top_df["ESCS"].quantile([0.25, 0.5, 0.75])
top_df["escs_q"] = pd.cut(
    top_df["ESCS"],
    bins=[-np.inf, escs_q[0.25], escs_q[0.5], escs_q[0.75], np.inf],
    labels=["Q1 (lowest SES)","Q2","Q3","Q4 (highest SES)"]
)

# Per-country % multi-burden by ESCS quartile
qresults = []
for cnt_code in top_oecd_cnts:
    sub = top_df[top_df["CNT"] == cnt_code]
    name = COUNTRY_NAMES.get(cnt_code, cnt_code)
    for q in ["Q1 (lowest SES)","Q2","Q3","Q4 (highest SES)"]:
        sg = sub[sub["escs_q"] == q]
        if len(sg) > 10 and sg["W_FSTUWT"].sum() > 0:
            pct = np.average(sg["multi_burden"], weights=sg["W_FSTUWT"]) * 100
        else:
            pct = np.nan
        qresults.append({"CNT": cnt_code, "name": name, "quartile": q, "pct_multi": pct})

qdf = pd.DataFrame(qresults)

fig, ax = plt.subplots(figsize=(14, 7))
fig.patch.set_facecolor("#0f1117")
ax.set_facecolor("#0f1117")

q_colors = ["#e74c3c","#e67e22","#f1c40f","#2ecc71"]
q_labels  = ["Q1 (lowest SES)","Q2","Q3","Q4 (highest SES)"]

x = np.arange(len(top_oecd_cnts))
width = 0.2

for i, (q, color) in enumerate(zip(q_labels, q_colors)):
    vals = [qdf[(qdf["CNT"]==c) & (qdf["quartile"]==q)]["pct_multi"].values
            for c in top_oecd_cnts]
    vals = [v[0] if len(v) > 0 and not np.isnan(v[0]) else 0 for v in vals]
    ax.bar(x + i*width, vals, width, color=color, alpha=0.85, label=q)

ax.set_xticks(x + 1.5*width)
ax.set_xticklabels([COUNTRY_NAMES.get(c,c) for c in top_oecd_cnts],
                   rotation=35, ha="right", fontsize=8.5, color="#dddddd")
ax.set_ylabel("% of students with 3+ burdens", color="#cccccc", fontsize=11)
ax.set_title(
    "The Hidden Underclass: Multi-Burden Students by SES Quartile\n"
    "Top 15 OECD countries by academic performance · PISA 2018",
    color="white", fontsize=12, pad=12,
)
ax.legend(framealpha=0.3, labelcolor="white", facecolor="#0f1117",
          edgecolor="#555555", fontsize=9)
for spine in ax.spines.values():
    spine.set_edgecolor("#333333")
ax.tick_params(colors="#999999")
ax.yaxis.set_major_formatter(mticker.PercentFormatter())
ax.grid(True, axis="y", color="#222222", lw=0.5, alpha=0.6)

plt.tight_layout()
plt.savefig(f"{OUT_DIR}/hidden_underclass_escs.png", dpi=150, bbox_inches="tight",
            facecolor=fig.get_facecolor())
plt.close()
print("Saved: hidden_underclass_escs.png")

# ─── SUMMARY STATS ───────────────────────────────────────────────────────────
print("\n" + "="*60)
print("SUMMARY")
print("="*60)

# Global
total_w = df["W_FSTUWT"].sum()
for k in range(7):
    w = df[df["hardship"]==k]["W_FSTUWT"].sum()
    print(f"  {k} burdens: {w/total_w*100:.1f}%")

print(f"\nGlobal multi-burden (3+): {df['multi_burden'].mean()*100:.1f}% (unweighted)")

# OECD subset
oecd_sub = df[df["oecd"]==1]
print(f"\nOECD multi-burden: {np.average(oecd_sub['multi_burden'], weights=oecd_sub['W_FSTUWT'])*100:.1f}%")

# Top 10 OECD multi-burden rates
print("\nTop-10-academic OECD countries: % with 3+ burdens")
oecd_cnt = cnt[cnt["oecd"]].nlargest(10,"academic")[["CNT","name","academic","pct_multi","pct_severe"]]
print(oecd_cnt.to_string(index=False))

# Performance penalty
print(f"\nPerformance penalty (0 vs 4+ burdens, OECD):")
p0 = penalty_oecd[0]
p4 = penalty_oecd[4] if not np.isnan(penalty_oecd[4]) else penalty_oecd[3]
print(f"  0 burdens: {p0:.1f} pts | 4+ burdens: {p4:.1f} pts | gap: {p0-p4:.0f} pts")

# Immigrant status
if "IMMIG" in df.columns:
    # IMMIG: 1=native, 2=second-gen immigrant, 3=first-gen immigrant
    for v, lbl in [(1,"Native"),(2,"2nd-gen immig"),(3,"1st-gen immig")]:
        sub = df[df["IMMIG"]==v]
        if len(sub) > 0:
            rate = np.average(sub["multi_burden"], weights=sub["W_FSTUWT"]) * 100
            print(f"  {lbl}: {rate:.1f}% multi-burden")

# Individual burden prevalence
print(f"\nPrevalence of each burden (global, weighted %):")
for col in BURDEN_COLS:
    rate = np.average(df[col], weights=df["W_FSTUWT"]) * 100
    print(f"  {BURDEN_LABELS[col]:35s}: {rate:.1f}%")

print("\nDone.")
