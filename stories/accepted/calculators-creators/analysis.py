"""
Calculators, Creators, or Both?
PISA 2022 · 63 Countries · Academic Performance × Creative Thinking

CT PVs:  PV1CRTH_NC–PV10CRTH_NC  (CRT_SPSS.zip / CY08MSP_CRT_COG.SAV)
Weights: W_FSTUWT from STU_QQQ (joined on CNTSTUID)
"""

import io
import zipfile

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np
import pandas as pd
import pyreadstat
from scipy.stats import pearsonr, ttest_ind

# ─── CONFIG ──────────────────────────────────────────────────────────────────
QQQ_ZIP = "data/raw/SPSS_STU_QQQ_2022.zip"
CRT_ZIP = "data/raw/SPSS_CRT_2022.zip"
OUT_DIR = "stories/accepted/calculators-creators/charts"

CT_PVS   = [f"PV{i}CRTH_NC" for i in range(1, 11)]
MATH_PVS = [f"PV{i}MATH"    for i in range(1, 11)]
READ_PVS = [f"PV{i}READ"    for i in range(1, 11)]
SCIE_PVS = [f"PV{i}SCIE"    for i in range(1, 11)]

CREAT_VARS = ["CREATSCH", "CREATEFF", "CREATACT", "CREATOR", "CREATOPN"]
CLIMATE_VARS = ["TEACHSUP", "BELONG", "DISCLIM"]

COLORS = {
    "Both":        "#2ecc71",
    "Calculators": "#3498db",
    "Creators":    "#e67e22",
    "Low Both":    "#bdc3c7",
}

# ─── HELPERS ─────────────────────────────────────────────────────────────────
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


# ─── LOAD DATA ───────────────────────────────────────────────────────────────
print("Loading CRT file...")
crt = load_sav_cols(CRT_ZIP, ["CNT", "CNTSTUID", "CNTSCHID"] + CT_PVS)
print(f"  {len(crt):,} rows, {crt['CNT'].nunique()} countries")

print("Loading QQQ file...")
qqq_cols = (["CNT", "CNTSTUID", "W_FSTUWT", "ESCS"]
            + MATH_PVS + READ_PVS + SCIE_PVS
            + [v for v in CREAT_VARS + CLIMATE_VARS])
qqq = load_sav_cols(QQQ_ZIP, qqq_cols)
print(f"  {len(qqq):,} rows")

# ─── JOIN + FILTER ────────────────────────────────────────────────────────────
print("Joining on CNTSTUID...")
df = crt.merge(
    qqq.drop(columns=["CNT"]),
    on="CNTSTUID", how="left"
)
print(f"  Joined: {len(df):,} rows | missing W_FSTUWT: {df['W_FSTUWT'].isna().sum():,}")

df = df.dropna(subset=["W_FSTUWT", CT_PVS[0], MATH_PVS[0]])
df = df[df["W_FSTUWT"] > 0]
print(f"  After filter: {len(df):,} rows, {df['CNT'].nunique()} countries")

# ─── STUDENT SCORES ──────────────────────────────────────────────────────────
df["ct_score"]    = df[CT_PVS].mean(axis=1)
df["math_score"]  = df[MATH_PVS].mean(axis=1)
df["read_score"]  = df[READ_PVS].mean(axis=1)
df["scie_score"]  = df[SCIE_PVS].mean(axis=1)
df["academic"]    = (df["math_score"] + df["read_score"] + df["scie_score"]) / 3

# ─── COUNTRY-LEVEL WEIGHTED MEANS ────────────────────────────────────────────
print("Computing country means...")
SCORE_COLS = ["ct_score", "academic", "math_score", "read_score", "scie_score", "ESCS"]
CONT_COLS  = [v for v in CREAT_VARS + CLIMATE_VARS if v in df.columns]
ALL_AGG    = SCORE_COLS + CONT_COLS

country = (
    df.groupby("CNT")
    .apply(lambda g: pd.Series({c: wmean(g, c) for c in ALL_AGG}
                               | {"n_students": len(g)}))
    .reset_index()
)

# ESCS control: partial out ESCS from CT? — we'll show raw and ESCS-adjusted rank
# For now, work with raw means.

# ─── QUADRANT ASSIGNMENT ─────────────────────────────────────────────────────
ct_med = country["ct_score"].median()
ac_med = country["academic"].median()
country["quadrant"] = "Low Both"
country.loc[(country["ct_score"] >= ct_med) & (country["academic"] >= ac_med), "quadrant"] = "Both"
country.loc[(country["ct_score"] <  ct_med) & (country["academic"] >= ac_med), "quadrant"] = "Calculators"
country.loc[(country["ct_score"] >= ct_med) & (country["academic"] <  ac_med), "quadrant"] = "Creators"

r_raw, p_raw = pearsonr(country["ct_score"], country["academic"])
print(f"\nCorrelation (CT vs academic): r = {r_raw:.3f}, p = {p_raw:.4f}")
print(f"\nMedians → CT: {ct_med:.1f}, Academic: {ac_med:.1f}")
print(f"\nQuadrant counts:\n{country['quadrant'].value_counts()}")

for q in ["Both", "Calculators", "Creators", "Low Both"]:
    sub = country[country["quadrant"] == q].sort_values("academic", ascending=False)
    print(f"\n── {q} ({len(sub)}) ──")
    print(sub[["CNT", "ct_score", "academic", "ESCS"]].to_string(index=False))

# Save country-level data
country.to_csv("data/processed/calculators_creators_country.csv", index=False)
print("\nSaved: data/processed/calculators_creators_country.csv")

# ─── CHART 1: MAIN SCATTER ───────────────────────────────────────────────────
# Country name lookup (abbreviated display names)
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

# Countries to always label
ALWAYS_LABEL = {
    "SGP","KOR","EST","FIN","AUS","CAN","NZL","JPN","HKG","MAC","TAP",
    "GBR","USA","DEU","FRA","ITA","POL","NLD","NOR","SWE","ISL",
    "ALB","PHL","UZB","DOM","MAR",
}

fig, ax = plt.subplots(figsize=(14, 9))
fig.patch.set_facecolor("#0f1117")
ax.set_facecolor("#0f1117")

# Quadrant shading
ax.axvline(ac_med, color="#ffffff20", lw=1, ls="--")
ax.axhline(ct_med, color="#ffffff20", lw=1, ls="--")

# Quadrant labels (background)
pad_x = (country["academic"].max() - country["academic"].min()) * 0.02
pad_y = (country["ct_score"].max() - country["ct_score"].min()) * 0.02
ax_xmin, ax_xmax = country["academic"].min() - pad_x*3, country["academic"].max() + pad_x*3
ax_ymin, ax_ymax = country["ct_score"].min() - pad_y*3, country["ct_score"].max() + pad_y*3

for (xloc, yloc, label, halign) in [
    (ac_med - pad_x, ct_med + pad_y, "CREATORS\n(creative, not academic)", "right"),
    (ac_med + pad_x, ct_med + pad_y, "BOTH\n(academic + creative)", "left"),
    (ac_med - pad_x, ct_med - pad_y, "LOW BOTH", "right"),
    (ac_med + pad_x, ct_med - pad_y, "CALCULATORS\n(academic, less creative)", "left"),
]:
    ax.text(xloc, yloc, label, color="#ffffff30", fontsize=8,
            ha=halign, va="center", style="italic")

# Plot points
for q, color in COLORS.items():
    sub = country[country["quadrant"] == q]
    ax.scatter(sub["academic"], sub["ct_score"], c=color, s=110,
               alpha=0.9, zorder=3, edgecolors="#0f1117", linewidths=0.6)

# Labels
for _, row in country.iterrows():
    lbl = COUNTRY_NAMES.get(row["CNT"], row["CNT"])
    if row["CNT"] in ALWAYS_LABEL or True:  # label all
        ax.annotate(
            lbl,
            xy=(row["academic"], row["ct_score"]),
            xytext=(4, 4), textcoords="offset points",
            fontsize=6.5, color="#dddddd", zorder=4,
        )

# Regression line
x_fit = np.linspace(ax_xmin, ax_xmax, 200)
m, b = np.polyfit(country["academic"], country["ct_score"], 1)
ax.plot(x_fit, m * x_fit + b, color="#ffffff40", lw=1.5, ls="-", zorder=2)

ax.set_xlim(ax_xmin, ax_xmax)
ax.set_ylim(ax_ymin, ax_ymax)

ax.set_xlabel("Academic Performance (mean Math + Reading + Science, PISA scale)", color="#cccccc", fontsize=11)
ax.set_ylabel("Creative Thinking Score (PISA CT scale, 0–48)", color="#cccccc", fontsize=11)
ax.set_title(
    f"Calculators, Creators, or Both?\n"
    f"Country-level Academic vs Creative Thinking · PISA 2022 · 63 countries · "
    f"r = {r_raw:.2f}",
    color="white", fontsize=13, pad=14,
)

legend_patches = [mpatches.Patch(color=c, label=q) for q, c in COLORS.items()]
ax.legend(handles=legend_patches, loc="lower right", framealpha=0.3,
          labelcolor="white", facecolor="#0f1117", edgecolor="#555555", fontsize=9)

for spine in ax.spines.values():
    spine.set_edgecolor("#333333")
ax.tick_params(colors="#999999")
ax.xaxis.set_tick_params(labelsize=9)
ax.yaxis.set_tick_params(labelsize=9)
ax.grid(True, color="#222222", lw=0.5, alpha=0.6)

plt.tight_layout()
plt.savefig(f"{OUT_DIR}/country_scatter.png", dpi=150, bbox_inches="tight",
            facecolor=fig.get_facecolor())
plt.close()
print("Saved: country_scatter.png")

# ─── CHART 2: CREATIVE PARADOX ───────────────────────────────────────────────
# High-performing countries' students report LESS creative identity than low-performing
# Show: country CT score vs country mean creative identity (CREATOR / CREATOPN)
# Also add a secondary panel for CREATACT

creat_avail = [v for v in ["CREATOR", "CREATOPN", "CREATACT", "CREATEFF"] if v in country.columns and country[v].notna().sum() >= 40]

if len(creat_avail) >= 1:
    fig, axes = plt.subplots(1, 2, figsize=(15, 7))
    fig.patch.set_facecolor("#0f1117")
    fig.suptitle(
        "The Creative Paradox: High CT Scorers Report Less Creative Identity\n"
        "Country-level means · PISA 2022 · 63 countries",
        color="white", fontsize=13, y=1.00,
    )

    var_labels = {
        "CREATOR": "Creative Identity Index",
        "CREATOPN": "Creative Openness Index",
        "CREATACT": "Creative Activities Index",
        "CREATEFF": "Creative Self-Efficacy",
    }

    pairs = [(creat_avail[0], "ct_score"), (creat_avail[1] if len(creat_avail) > 1 else creat_avail[0], "academic")]

    for ax, (yvar, xvar) in zip(axes, pairs):
        ax.set_facecolor("#0f1117")
        valid_c = country[[xvar, yvar, "quadrant", "CNT"]].dropna()

        for q, color in COLORS.items():
            sub = valid_c[valid_c["quadrant"] == q]
            ax.scatter(sub[xvar], sub[yvar], c=color, s=90, alpha=0.9,
                       zorder=3, edgecolors="#0f1117", linewidths=0.5, label=q)

        for _, row in valid_c.iterrows():
            lbl = COUNTRY_NAMES.get(row["CNT"], row["CNT"])
            ax.annotate(lbl, xy=(row[xvar], row[yvar]),
                        xytext=(3, 3), textcoords="offset points",
                        fontsize=6, color="#cccccc", zorder=4)

        # Regression
        m2, b2 = np.polyfit(valid_c[xvar], valid_c[yvar], 1)
        xr = np.linspace(valid_c[xvar].min(), valid_c[xvar].max(), 200)
        ax.plot(xr, m2 * xr + b2, color="#ffffff40", lw=1.5)
        r_p, _ = pearsonr(valid_c[xvar], valid_c[yvar])

        xlabel = ("Creative Thinking Score (PISA CT scale)" if xvar == "ct_score"
                  else "Academic Performance (PISA scale)")
        ax.set_xlabel(xlabel, color="#cccccc", fontsize=10)
        ax.set_ylabel(var_labels.get(yvar, yvar), color="#cccccc", fontsize=10)
        ax.set_title(f"r = {r_p:.2f}", color="#aaaaaa", fontsize=10, pad=6)
        ax.tick_params(colors="#999999", labelsize=8)
        for spine in ax.spines.values():
            spine.set_edgecolor("#333333")
        ax.grid(True, color="#222222", lw=0.5, alpha=0.6)

    legend_patches = [mpatches.Patch(color=c, label=q) for q, c in COLORS.items()]
    axes[1].legend(handles=legend_patches, loc="upper right", framealpha=0.3,
                   labelcolor="white", facecolor="#0f1117", edgecolor="#555555", fontsize=8)

    plt.tight_layout()
    plt.savefig(f"{OUT_DIR}/creative_paradox.png", dpi=150, bbox_inches="tight",
                facecolor=fig.get_facecolor())
    plt.close()
    print("Saved: creative_paradox.png")

    # Print paradox correlation numbers
    for v in creat_avail:
        vc = country[["ct_score", "academic", v]].dropna()
        r_ct, _ = pearsonr(vc["ct_score"], vc[v])
        r_ac, _ = pearsonr(vc["academic"], vc[v])
        print(f"{v:12s}: r(CT) = {r_ct:.3f}  r(academic) = {r_ac:.3f}")

# ─── CHART 3: WHAT DISTINGUISHES — CREATIVE ACTIVITIES + CLIMATE ─────────────
# Compare "Both" vs "Calculators" countries on school creative activity and climate
# Variables available: CREATSCH, CREATEFF, CREATACT, CREATOR, CREATOPN, TEACHSUP, BELONG, DISCLIM

avail_cont = [v for v in CREAT_VARS + CLIMATE_VARS if v in country.columns and country[v].notna().sum() > 5]
print(f"\nAvailable context vars: {avail_cont}")

if avail_cont:
    both_countries    = country[country["quadrant"] == "Both"]["CNT"].tolist()
    calc_countries    = country[country["quadrant"] == "Calculators"]["CNT"].tolist()
    creator_countries = country[country["quadrant"] == "Creators"]["CNT"].tolist()
    low_countries     = country[country["quadrant"] == "Low Both"]["CNT"].tolist()

    # Student-level comparisons across quadrants
    df["quadrant"] = df["CNT"].map(country.set_index("CNT")["quadrant"])

    def group_d(grp_a, grp_b, col):
        a = grp_a[col].dropna()
        b = grp_b[col].dropna()
        if len(a) < 10 or len(b) < 10:
            return np.nan, np.nan, np.nan
        pool_sd = np.sqrt(((len(a)-1)*a.std()**2 + (len(b)-1)*b.std()**2) / (len(a)+len(b)-2))
        d = (a.mean() - b.mean()) / pool_sd if pool_sd > 0 else 0
        _, p = ttest_ind(a, b, equal_var=False)
        return d, p, len(a) + len(b)

    both_stu    = df[df["quadrant"] == "Both"]
    calc_stu    = df[df["quadrant"] == "Calculators"]
    creator_stu = df[df["quadrant"] == "Creators"]
    low_stu     = df[df["quadrant"] == "Low Both"]

    VAR_LABELS = {
        "CREATSCH": "Creative activities\nat school",
        "CREATEFF": "Creative self-efficacy",
        "CREATACT": "Creative activities\n(overall)",
        "CREATOR":  "Creative identity",
        "CREATOPN": "Creative openness",
        "TEACHSUP": "Teacher support",
        "BELONG":   "Sense of belonging",
        "DISCLIM":  "Disciplinary climate",
    }

    results = []
    for v in avail_cont:
        d_bc, p_bc, _ = group_d(both_stu, calc_stu, v)
        d_bl, p_bl, _ = group_d(both_stu, low_stu,  v)
        results.append({
            "var": v,
            "label": VAR_LABELS.get(v, v),
            "d_vs_calc": d_bc,
            "p_vs_calc": p_bc,
            "d_vs_low": d_bl,
            "p_vs_low": p_bl,
        })

    res_df = pd.DataFrame(results)
    print("\nBoth vs Low Both (Cohen's d):")
    print(res_df[["label","d_vs_low","p_vs_low"]].sort_values("d_vs_low", ascending=False).to_string(index=False))
    print("\nBoth vs Calculators (Cohen's d):")
    print(res_df[["label","d_vs_calc","p_vs_calc"]].sort_values("d_vs_calc", ascending=False).to_string(index=False))

    # Bar chart: Both vs Low Both (meaningful n=30 vs n=29)
    fig, ax = plt.subplots(figsize=(11, 6))
    fig.patch.set_facecolor("#0f1117")
    ax.set_facecolor("#0f1117")

    sub = res_df.dropna(subset=["d_vs_low"]).sort_values("d_vs_low")
    y_pos = np.arange(len(sub))
    bar_colors = [COLORS["Both"] if d > 0 else COLORS["Low Both"] for d in sub["d_vs_low"]]
    ax.barh(y_pos, sub["d_vs_low"], color=bar_colors, alpha=0.85, height=0.6)

    for i, (d, p) in enumerate(zip(sub["d_vs_low"], sub["p_vs_low"])):
        sig = "***" if p < 0.001 else ("**" if p < 0.01 else ("*" if p < 0.05 else "ns"))
        ax.text(d + (0.01 if d >= 0 else -0.01), i, sig,
                va="center", ha="left" if d >= 0 else "right",
                color="#cccccc", fontsize=8)

    ax.set_yticks(y_pos)
    ax.set_yticklabels(sub["label"], color="#dddddd", fontsize=10)
    ax.axvline(0, color="#555555", lw=1)
    ax.set_xlabel("Cohen's d  (positive = favours high-performing countries)", color="#cccccc", fontsize=11)
    ax.set_title(
        "What Distinguishes High-Performing ('Both') Countries from Lower-Performing?\n"
        "Student-level Cohen's d · PISA 2022 · n = 30 vs 29 countries",
        color="white", fontsize=12, pad=12,
    )
    ax.tick_params(colors="#999999")
    for spine in ax.spines.values():
        spine.set_edgecolor("#333333")
    ax.grid(True, axis="x", color="#222222", lw=0.5, alpha=0.6)

    plt.tight_layout()
    plt.savefig(f"{OUT_DIR}/both_vs_low.png", dpi=150, bbox_inches="tight",
                facecolor=fig.get_facecolor())
    plt.close()
    print("Saved: both_vs_low.png")

# ─── ESCS CONTROL ────────────────────────────────────────────────────────────
from numpy.linalg import lstsq

valid = country[["ct_score", "academic", "ESCS"]].dropna()
r_ac_escs, _ = pearsonr(valid["academic"], valid["ESCS"])
r_ct_escs, _ = pearsonr(valid["ct_score"], valid["ESCS"])
print(f"\nESCS vs academic: r = {r_ac_escs:.3f}")
print(f"ESCS vs CT:       r = {r_ct_escs:.3f}")

def partial_r(x, y, z):
    c = np.column_stack([z, np.ones(len(z))])
    rx = x - c @ lstsq(c, x, rcond=None)[0]
    ry = y - c @ lstsq(c, y, rcond=None)[0]
    return pearsonr(rx, ry)

r_partial, p_partial = partial_r(valid["ct_score"].values, valid["academic"].values, valid["ESCS"].values)
print(f"Partial r (CT–academic, controlling ESCS): {r_partial:.3f}, p = {p_partial:.4f}")

# ─── PRINT SUMMARY ───────────────────────────────────────────────────────────
print("\n" + "="*60)
print("SUMMARY")
print("="*60)
print(f"Countries: {len(country)}")
print(f"CT–Academic correlation:              r = {r_raw:.3f}")
print(f"Partial r (controlling ESCS):         r = {r_partial:.3f}")
print(f"ESCS–Academic r:                      r = {r_ac_escs:.3f}")
print(f"ESCS–CT r:                            r = {r_ct_escs:.3f}")
print(f"\nQuadrant distribution:")
for q in ["Both","Calculators","Creators","Low Both"]:
    n = (country["quadrant"] == q).sum()
    print(f"  {q:14s}: {n:2d} countries")

print(f"\nTop 5 'Both' countries (academic rank):")
both = country[country["quadrant"]=="Both"].sort_values("academic", ascending=False)
for _, r in both.head(5).iterrows():
    print(f"  {r['CNT']:4s}  academic={r['academic']:.1f}  CT={r['ct_score']:.1f}  ESCS={r['ESCS']:.2f}")

print(f"\nTop 'Calculators' (academic rank):")
calc = country[country["quadrant"]=="Calculators"].sort_values("academic", ascending=False)
for _, r in calc.head(5).iterrows():
    print(f"  {r['CNT']:4s}  academic={r['academic']:.1f}  CT={r['ct_score']:.1f}  ESCS={r['ESCS']:.2f}")

print(f"\n'Creators' (CT rank):")
crea = country[country["quadrant"]=="Creators"].sort_values("ct_score", ascending=False)
for _, r in crea.iterrows():
    print(f"  {r['CNT']:4s}  academic={r['academic']:.1f}  CT={r['ct_score']:.1f}  ESCS={r['ESCS']:.2f}")

print("\nDone.")
