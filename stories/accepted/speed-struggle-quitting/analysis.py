"""
Speed, Struggle, and Quitting
PISA 2018 · Computer-based cognitive process data (item-level timing + scoring)

Hypothesis: students/countries with similar academic performance can reach that
performance through very different test-taking behavior — fast confident answers,
slow persistence, or a tendency to omit/quit items rather than attempt them.

Method: for 311 Math/Science/Reading items that carry both a scored response and a
"time to first action" timestamp, classify every administered (student, item) pair
into one of five profiles:
    Omit/Quit    — coded "Not Reached" or "No Response" for that item
    Fast-Right   — attempted, full credit, time-to-first-action below the item's
                   own median (among attempted responses with valid timing)
    Slow-Right   — attempted, full credit, at/above the item median
    Fast-Wrong   — attempted, not full credit, below the item median
    Slow-Wrong   — attempted, not full credit, at/above the item median
Value-label text (not hardcoded codes) determines "full credit" / "not reached" /
"no response" / "not applicable" / "invalid" per item, since one item (CR561Q06S)
uses a non-standard code scheme. See PLAN.md for full rationale.

Restricted to ADMINMODE == 2 (computer-based administration): 71 of 79 countries.
The 8 paper-based countries (ARG, JOR, LBN, MDA, MKD, ROU, SAU, UKR) have no item
timing data and are excluded from this story.
"""

import io
import os
import re
import warnings
import zipfile
from collections import defaultdict

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

ROOT = os.path.expanduser("~/code/pisa-data-stories")
COG_ZIP = os.path.join(ROOT, "data/raw/SPSS_STU_COG.zip")
QQQ_ZIP = os.path.join(ROOT, "data/raw/SPSS_STU_QQQ.zip")
PROC_DIR = os.path.join(ROOT, "data/processed")
OUT_DIR = os.path.join(ROOT, "stories/accepted/speed-struggle-quitting/charts")
os.makedirs(PROC_DIR, exist_ok=True)
os.makedirs(OUT_DIR, exist_ok=True)

MIN_ITEMS_PER_STUDENT = 10  # drop students with too few classified items for a stable share

# ---------------------------------------------------------------------------
# 1. Identify item stems with a plain scored-response + time-to-first-action pair
# ---------------------------------------------------------------------------
print("Reading COG metadata...")
with zipfile.ZipFile(COG_ZIP) as z:
    sav_name = [n for n in z.namelist() if n.endswith(".sav")][0]
    with z.open(sav_name) as f:
        buf = io.BytesIO(f.read())
_, meta_all = pyreadstat.read_sav(buf, metadataonly=True)
all_cols = set(meta_all.column_names)


def stems_with_full_process(prefix):
    stem_suffixes = defaultdict(set)
    for c in all_cols:
        m = re.match(rf"^({prefix}\d+Q\d+)([A-Z]?)$", c)
        if m:
            stem_suffixes[m.group(1)].add(m.group(2))
    return sorted(s for s, sufs in stem_suffixes.items() if {"S", "F"}.issubset(sufs))


item_stems = {p: stems_with_full_process(p) for p in ["CM", "CS", "CR"]}
all_stems = [s for v in item_stems.values() for s in v]
print(f"  Items: Math={len(item_stems['CM'])}  Science={len(item_stems['CS'])}  "
      f"Reading={len(item_stems['CR'])}  Total={len(all_stems)}")

# ---------------------------------------------------------------------------
# 2. Load only the needed columns
# ---------------------------------------------------------------------------
print("Loading COG item data (S + F for each item)...")
usecols = ["CNT", "CNTSCHID", "CNTSTUID", "ADMINMODE"] + [
    s + suf for s in all_stems for suf in ["S", "F"]
]
buf.seek(0)
cog, meta = pyreadstat.read_sav(buf, usecols=usecols, user_missing=True)
print(f"  Loaded {len(cog):,} rows, {len(cog.columns)} columns")

cog = cog[cog["ADMINMODE"] == 2].copy()
print(f"  After CBA filter: {len(cog):,} students, {cog['CNT'].nunique()} countries")

# ---------------------------------------------------------------------------
# 3. Classify every (student, item) pair, accumulate per-student profile counts
# ---------------------------------------------------------------------------
print("Classifying item responses into behavioral profiles...")
n = len(cog)
cats = ["omit", "fast_right", "slow_right", "fast_wrong", "slow_wrong"]
counts = {c: np.zeros(n) for c in cats}
denom = np.zeros(n)
dropped_unknown_speed = 0
total_attempted = 0
total_administered = 0
skipped_items = []

for stem in all_stems:
    s_col, f_col = stem + "S", stem + "F"
    vl = meta.variable_value_labels.get(s_col)
    if not vl:
        skipped_items.append(stem)
        continue
    full_credit = {k for k, v in vl.items() if "full credit" in v.lower()}
    omit_codes = {k for k, v in vl.items() if "not reached" in v.lower() or "no response" in v.lower()}
    excluded = {k for k, v in vl.items() if "not applicable" in v.lower() or "invalid" in v.lower()}
    if not full_credit or not omit_codes:
        skipped_items.append(stem)
        continue

    s = cog[s_col].values
    f = cog[f_col].values
    notna = ~pd.isna(s)
    administered = notna & ~np.isin(s, list(excluded))
    omit_mask = administered & np.isin(s, list(omit_codes))
    attempted = administered & ~omit_mask
    correct = attempted & np.isin(s, list(full_credit))
    valid_f = attempted & ~pd.isna(f) & (f >= 0)

    total_administered += administered.sum()
    total_attempted += attempted.sum()
    dropped_unknown_speed += int((attempted & ~valid_f).sum())

    if valid_f.sum() > 0:
        med = np.median(f[valid_f])
    else:
        med = np.nan

    fast = valid_f & (f < med)
    slow = valid_f & (f >= med)

    counts["omit"] += omit_mask
    counts["fast_right"] += valid_f & correct & fast
    counts["slow_right"] += valid_f & correct & slow
    counts["fast_wrong"] += valid_f & ~correct & fast
    counts["slow_wrong"] += valid_f & ~correct & slow
    denom += omit_mask.astype(float) + valid_f.astype(float)

print(f"  Skipped items (no usable value labels): {len(skipped_items)} -> {skipped_items}")
print(f"  Total administered item-responses: {total_administered:,}")
print(f"  Total attempted (non-omit): {total_attempted:,}")
print(f"  Dropped (attempted but invalid/missing timing): {dropped_unknown_speed:,} "
      f"({dropped_unknown_speed/max(total_attempted,1)*100:.2f}% of attempted)")

for c in cats:
    cog[f"n_{c}"] = counts[c]
cog["n_items_classified"] = denom

print("\nDistribution of classified-items-per-student:")
print(cog["n_items_classified"].describe())

before = len(cog)
cog = cog[cog["n_items_classified"] >= MIN_ITEMS_PER_STUDENT].copy()
print(f"\nDropped {before - len(cog):,} students with < {MIN_ITEMS_PER_STUDENT} classified items "
      f"({(before - len(cog))/before*100:.1f}%)")

for c in cats:
    cog[f"share_{c}"] = cog[f"n_{c}"] / cog["n_items_classified"]

print("\nGlobal unweighted mean shares:")
print(cog[[f"share_{c}" for c in cats]].mean())

# ---------------------------------------------------------------------------
# 4. Save intermediate student-level profile table (small, needed downstream)
# ---------------------------------------------------------------------------
keep_cols = ["CNT", "CNTSCHID", "CNTSTUID", "n_items_classified"] + [f"share_{c}" for c in cats] + [f"n_{c}" for c in cats]
cog_out = cog[keep_cols].copy()
cog_out.to_csv(os.path.join(PROC_DIR, "speed_struggle_quitting_student_profiles.csv.gz"), index=False, compression="gzip")
print(f"\nSaved student profile table: {len(cog_out):,} rows")
print("Done with Part 1 (classification).")

# ---------------------------------------------------------------------------
# 5. Merge with QQQ for weights, ESCS, gender, and academic performance
# ---------------------------------------------------------------------------
print("\nLoading QQQ for weights / ESCS / gender / plausible values...")
MATH_PVS = [f"PV{i}MATH" for i in range(1, 11)]
READ_PVS = [f"PV{i}READ" for i in range(1, 11)]
SCIE_PVS = [f"PV{i}SCIE" for i in range(1, 11)]
QQQ_COLS = ["CNT", "CNTSCHID", "CNTSTUID", "W_FSTUWT", "ESCS", "ST004D01T"] + MATH_PVS + READ_PVS + SCIE_PVS

with zipfile.ZipFile(QQQ_ZIP) as z:
    sav_name = [n for n in z.namelist() if n.endswith(".sav")][0]
    with z.open(sav_name) as f:
        buf = io.BytesIO(f.read())
qqq, _ = pyreadstat.read_sav(buf, usecols=QQQ_COLS)
qqq["academic"] = (qqq[MATH_PVS].mean(axis=1) + qqq[READ_PVS].mean(axis=1) + qqq[SCIE_PVS].mean(axis=1)) / 3
qqq = qqq[["CNT", "CNTSCHID", "CNTSTUID", "W_FSTUWT", "ESCS", "ST004D01T", "academic"]]
print(f"  QQQ rows: {len(qqq):,}")

merged = cog_out.merge(qqq, on=["CNT", "CNTSCHID", "CNTSTUID"], how="inner")
merged = merged[merged["W_FSTUWT"] > 0].copy()
print(f"  Merged rows: {len(merged):,} ({merged['CNT'].nunique()} countries)")

SHARE_COLS = [f"share_{c}" for c in cats]

# "Speed style" isolates response-time style from raw ability: of the items a
# student got right, what share were answered fast? This is independent of how
# many items the student got right in total, so it lets us compare countries
# at the *same* performance level on pure style rather than accuracy.
n_correct_total = merged["n_fast_right"] + merged["n_slow_right"]
merged["speed_style"] = np.where(n_correct_total > 0, merged["n_fast_right"] / n_correct_total * 100, np.nan)

# ---------------------------------------------------------------------------
# 6. Country-level weighted aggregation
# ---------------------------------------------------------------------------
def wmean(grp, col):
    m = grp[[col, "W_FSTUWT"]].dropna()
    m = m[m["W_FSTUWT"] > 0]
    return np.average(m[col], weights=m["W_FSTUWT"]) if len(m) else np.nan


print("\nComputing country-level statistics...")
cnt = (
    merged.groupby("CNT")
    .apply(lambda g: pd.Series({
        "academic": wmean(g, "academic"),
        **{sc: wmean(g, sc) * 100 for sc in SHARE_COLS},
        "speed_style": wmean(g, "speed_style"),
        "n_students": len(g),
    }))
    .reset_index()
)
cnt = cnt[cnt["n_students"] >= 200].copy()  # keep only countries with a stable sample
print(f"  Countries retained: {len(cnt)}")

OECD = {
    "AUS", "AUT", "BEL", "CAN", "CHL", "COL", "CRI", "CZE", "DNK", "EST",
    "FIN", "FRA", "DEU", "GRC", "HUN", "ISL", "ISR", "ITA", "JPN", "KOR",
    "LVA", "LTU", "LUX", "MEX", "NLD", "NZL", "NOR", "POL", "PRT", "SVK",
    "SVN", "ESP", "SWE", "CHE", "TUR", "GBR", "USA",
}
COUNTRY_NAMES = {
    "ALB": "Albania", "ARE": "UAE", "AUS": "Australia", "AUT": "Austria",
    "BEL": "Belgium", "BGR": "Bulgaria", "BIH": "Bosnia", "BLR": "Belarus",
    "BRA": "Brazil", "BRN": "Brunei", "CAN": "Canada", "CHE": "Switzerland", "CHL": "Chile", "CHN": "China",
    "COL": "Colombia", "CRI": "Costa Rica", "CZE": "Czech Rep.", "DEU": "Germany",
    "DNK": "Denmark", "DOM": "Dom. Rep.", "ESP": "Spain", "EST": "Estonia",
    "FIN": "Finland", "FRA": "France", "GBR": "UK", "GEO": "Georgia",
    "GRC": "Greece", "HKG": "Hong Kong", "HRV": "Croatia", "HUN": "Hungary",
    "IDN": "Indonesia", "IRL": "Ireland", "ISL": "Iceland", "ISR": "Israel",
    "ITA": "Italy", "JPN": "Japan", "KAZ": "Kazakhstan",
    "KOR": "Korea", "KSV": "Kosovo", "LTU": "Lithuania",
    "LUX": "Luxembourg", "LVA": "Latvia", "MAC": "Macao", "MAR": "Morocco",
    "MEX": "Mexico", "MLT": "Malta",
    "MNE": "Montenegro", "MYS": "Malaysia", "NLD": "Netherlands", "NOR": "Norway",
    "NZL": "New Zealand", "PAN": "Panama", "PER": "Peru", "PHL": "Philippines",
    "POL": "Poland", "PRT": "Portugal", "QAT": "Qatar", "QAZ": "Baku (AZE)",
    "QCI": "B-S-J-Z (China)", "QMR": "Moscow Reg.", "QRT": "Tatarstan",
    "RUS": "Russia", "SGP": "Singapore", "SRB": "Serbia",
    "SVK": "Slovakia", "SVN": "Slovenia", "SWE": "Sweden", "TAP": "Chinese Taipei",
    "THA": "Thailand", "TUR": "Turkey", "URY": "Uruguay",
    "USA": "USA", "UZB": "Uzbekistan", "VNM": "Vietnam",
}

cnt["oecd"] = cnt["CNT"].isin(OECD)
cnt["name"] = cnt["CNT"].map(lambda c: COUNTRY_NAMES.get(c, c))
cnt.to_csv(os.path.join(PROC_DIR, "speed_struggle_quitting_country.csv"), index=False)
print(f"  Saved: speed_struggle_quitting_country.csv")
print(cnt[["CNT", "name", "academic", "share_omit"]].sort_values("share_omit", ascending=False).head(10).to_string(index=False))

# ---------------------------------------------------------------------------
# 7. Matched-performance pairs: nearest-neighbor by academic score, ranked
#    by how differently they behave (omit-share gap)
# ---------------------------------------------------------------------------
print("\nFinding matched-performance country pairs with divergent omit behavior...")
acad = cnt.set_index("CNT")["academic"]
omit = cnt.set_index("CNT")["share_omit"]
pairs = []
codes = cnt["CNT"].tolist()
for i, a in enumerate(codes):
    for b in codes[i + 1:]:
        gap_score = abs(acad[a] - acad[b])
        if gap_score <= 4:  # within 4 PISA points ~ near-identical performance
            gap_omit = abs(omit[a] - omit[b])
            pairs.append((a, b, gap_score, gap_omit))
pairs_df = pd.DataFrame(pairs, columns=["a", "b", "score_gap", "omit_gap"]).sort_values("omit_gap", ascending=False)
print(pairs_df.head(10).to_string(index=False))
pairs_df.to_csv(os.path.join(PROC_DIR, "speed_struggle_quitting_matched_pairs.csv"), index=False)

EAST_ASIA = {"KOR", "TAP", "HKG", "MAC", "SGP", "QCI", "JPN"}

# ---------------------------------------------------------------------------
# 8. CHART 1 — Hero chart: same score band, wildly different "speed style"
# ---------------------------------------------------------------------------
print("\nBuilding charts...")
band = cnt[(cnt["academic"] >= 495) & (cnt["academic"] <= 521)].sort_values("speed_style", ascending=True)
print(f"  Score band 495-521: {len(band)} countries, "
      f"academic range {band['academic'].min():.0f}-{band['academic'].max():.0f}")

fig, ax = plt.subplots(figsize=(11, 9))
fig.patch.set_facecolor("#0f1117")
ax.set_facecolor("#0f1117")

colors = ["#e67e22" if c in EAST_ASIA else "#2471a3" for c in band["CNT"]]
y_pos = np.arange(len(band))
ax.barh(y_pos, band["speed_style"], color=colors, alpha=0.9, height=0.7)
for i, (_, row) in enumerate(band.iterrows()):
    ax.text(row["speed_style"] + 1, i, f"{row['academic']:.0f} pts", va="center",
            fontsize=8, color="#aaaaaa")

ax.set_yticks(y_pos)
ax.set_yticklabels(band["name"], fontsize=9, color="#dddddd")
ax.set_xlabel("Speed style: of items answered correctly, % answered fast", color="#cccccc", fontsize=10.5)
ax.set_title(
    "Same Score, Different Style\n"
    f"Countries scoring {band['academic'].min():.0f}-{band['academic'].max():.0f} on PISA 2018 "
    "(mean of Math/Reading/Science) — numbers show each country's actual score",
    color="white", fontsize=12.5, pad=12,
)
legend_patches = [
    mpatches.Patch(color="#e67e22", label="East/Southeast Asian systems"),
    mpatches.Patch(color="#2471a3", label="Other systems"),
]
ax.legend(handles=legend_patches, loc="lower right", framealpha=0.3,
          labelcolor="white", facecolor="#0f1117", edgecolor="#555555", fontsize=9)
ax.set_xlim(0, 100)
for spine in ax.spines.values():
    spine.set_edgecolor("#333333")
ax.tick_params(colors="#999999")
ax.xaxis.set_major_formatter(mticker.PercentFormatter())
ax.grid(True, axis="x", color="#222222", lw=0.5, alpha=0.6)
plt.tight_layout()
plt.savefig(f"{OUT_DIR}/same_score_different_style.png", dpi=150, bbox_inches="tight", facecolor=fig.get_facecolor())
plt.close()
print("  Saved: same_score_different_style.png")

# ---------------------------------------------------------------------------
# 9. CHART 2 — Scatter: academic score vs speed style, all 71 countries
# ---------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(12, 8))
fig.patch.set_facecolor("#0f1117")
ax.set_facecolor("#0f1117")

for _, row in cnt.iterrows():
    color = "#e67e22" if row["CNT"] in EAST_ASIA else ("#2ecc71" if row["oecd"] else "#7f8c8d")
    ax.scatter(row["academic"], row["speed_style"], c=color, s=70, alpha=0.85,
               zorder=3, edgecolors="#0f1117", linewidths=0.5)
    ax.annotate(row["name"], xy=(row["academic"], row["speed_style"]),
                xytext=(4, 3), textcoords="offset points", fontsize=5.5, color="#cccccc", zorder=4)

ax.axvspan(495, 521, color="#ffffff10", zorder=1)
ax.text(508, 4, "Score band shown\nin Chart 1", ha="center", color="#888888", fontsize=8)

r, p = pearsonr(cnt["academic"], cnt["speed_style"])
ax.set_xlabel("Academic performance (mean Math + Reading + Science, PISA scale)", color="#cccccc", fontsize=11)
ax.set_ylabel("Speed style: % of correct answers that were fast", color="#cccccc", fontsize=11)
ax.set_title(
    f"Response Style Is Only Weakly Tied to Performance\n"
    f"PISA 2018 · 71 computer-based countries · r = {r:.2f}",
    color="white", fontsize=12, pad=12,
)
legend_patches = [
    mpatches.Patch(color="#e67e22", label="East/Southeast Asian systems"),
    mpatches.Patch(color="#2ecc71", label="Other OECD"),
    mpatches.Patch(color="#7f8c8d", label="Other non-OECD"),
]
ax.legend(handles=legend_patches, loc="upper left", framealpha=0.3,
          labelcolor="white", facecolor="#0f1117", edgecolor="#555555", fontsize=9)
for spine in ax.spines.values():
    spine.set_edgecolor("#333333")
ax.tick_params(colors="#999999")
ax.yaxis.set_major_formatter(mticker.PercentFormatter())
ax.grid(True, color="#222222", lw=0.5, alpha=0.6)
plt.tight_layout()
plt.savefig(f"{OUT_DIR}/academic_vs_speed_style.png", dpi=150, bbox_inches="tight", facecolor=fig.get_facecolor())
plt.close()
print("  Saved: academic_vs_speed_style.png")
print(f"  Correlation academic vs speed_style: r={r:.3f}, p={p:.4f}")

# ---------------------------------------------------------------------------
# 10. CHART 3 — Scatter: academic score vs omit share, with NLD/SWE callout
# ---------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(12, 8))
fig.patch.set_facecolor("#0f1117")
ax.set_facecolor("#0f1117")

for _, row in cnt.iterrows():
    color = "#2ecc71" if row["oecd"] else "#7f8c8d"
    ax.scatter(row["academic"], row["share_omit"], c=color, s=70, alpha=0.85,
               zorder=3, edgecolors="#0f1117", linewidths=0.5)
    ax.annotate(row["name"], xy=(row["academic"], row["share_omit"]),
                xytext=(4, 3), textcoords="offset points", fontsize=5.5, color="#cccccc", zorder=4)

nld = cnt[cnt["CNT"] == "NLD"].iloc[0]
swe = cnt[cnt["CNT"] == "SWE"].iloc[0]
ax.annotate(
    f"Netherlands & Sweden score within\n0.1 points of each other —\nbut Sweden's students give up on\n4x as many items ({swe['share_omit']:.1f}% vs {nld['share_omit']:.1f}%)",
    xy=(swe["academic"], swe["share_omit"]), xytext=(420, 17),
    arrowprops=dict(arrowstyle="->", color="#e74c3c", lw=1.3),
    color="#e74c3c", fontsize=9, fontweight="bold",
)

r2, p2 = pearsonr(cnt["academic"], cnt["share_omit"])
ax.set_xlabel("Academic performance (mean Math + Reading + Science, PISA scale)", color="#cccccc", fontsize=11)
ax.set_ylabel("% of items omitted or not reached", color="#cccccc", fontsize=11)
ax.set_title(
    f"Giving Up Is Not Just a Low-Performance Problem\n"
    f"PISA 2018 · 71 computer-based countries · r = {r2:.2f}",
    color="white", fontsize=12, pad=12,
)
legend_patches = [
    mpatches.Patch(color="#2ecc71", label="OECD member"),
    mpatches.Patch(color="#7f8c8d", label="Non-OECD"),
]
ax.legend(handles=legend_patches, loc="upper right", framealpha=0.3,
          labelcolor="white", facecolor="#0f1117", edgecolor="#555555", fontsize=9)
for spine in ax.spines.values():
    spine.set_edgecolor("#333333")
ax.tick_params(colors="#999999")
ax.yaxis.set_major_formatter(mticker.PercentFormatter())
ax.grid(True, color="#222222", lw=0.5, alpha=0.6)
plt.tight_layout()
plt.savefig(f"{OUT_DIR}/academic_vs_omit.png", dpi=150, bbox_inches="tight", facecolor=fig.get_facecolor())
plt.close()
print("  Saved: academic_vs_omit.png")
print(f"  Correlation academic vs share_omit: r={r2:.3f}, p={p2:.4f}")

# ---------------------------------------------------------------------------
# 11. CHART 4 — Within-country drill-down: omit share by ESCS quintile
# ---------------------------------------------------------------------------
DRILLDOWN_COUNTRIES = ["SWE", "PER", "FRA", "USA"]
merged["escs_q"] = pd.qcut(merged["ESCS"], 5, labels=["Q1 (lowest SES)", "Q2", "Q3", "Q4", "Q5 (highest SES)"], duplicates="drop")

qresults = []
for c in DRILLDOWN_COUNTRIES:
    sub = merged[merged["CNT"] == c]
    name = COUNTRY_NAMES.get(c, c)
    for q in sub["escs_q"].cat.categories:
        sg = sub[sub["escs_q"] == q]
        if len(sg) > 20 and sg["W_FSTUWT"].sum() > 0:
            pct = np.average(sg["share_omit"], weights=sg["W_FSTUWT"]) * 100
        else:
            pct = np.nan
        qresults.append({"CNT": c, "name": name, "quartile": str(q), "pct_omit": pct})
qdf = pd.DataFrame(qresults)

fig, ax = plt.subplots(figsize=(11, 7))
fig.patch.set_facecolor("#0f1117")
ax.set_facecolor("#0f1117")

q_labels = ["Q1 (lowest SES)", "Q2", "Q3", "Q4", "Q5 (highest SES)"]
q_colors = ["#c0392b", "#e67e22", "#f1c40f", "#7fb37f", "#2ecc71"]
x = np.arange(len(DRILLDOWN_COUNTRIES))
width = 0.16

for i, (q, color) in enumerate(zip(q_labels, q_colors)):
    vals = [qdf[(qdf["CNT"] == c) & (qdf["quartile"] == q)]["pct_omit"].values for c in DRILLDOWN_COUNTRIES]
    vals = [v[0] if len(v) > 0 and not np.isnan(v[0]) else 0 for v in vals]
    ax.bar(x + i * width, vals, width, color=color, alpha=0.9, label=q)

ax.set_xticks(x + 2 * width)
ax.set_xticklabels([COUNTRY_NAMES.get(c, c) for c in DRILLDOWN_COUNTRIES], fontsize=10.5, color="#dddddd")
ax.set_ylabel("% of items omitted or not reached", color="#cccccc", fontsize=11)
ax.set_title(
    "Giving Up Is Also an Equity Story Within Countries\n"
    "Omit/quit rate by socioeconomic quintile (ESCS) · PISA 2018",
    color="white", fontsize=12, pad=12,
)
ax.legend(framealpha=0.3, labelcolor="white", facecolor="#0f1117", edgecolor="#555555", fontsize=8.5)
for spine in ax.spines.values():
    spine.set_edgecolor("#333333")
ax.tick_params(colors="#999999")
ax.yaxis.set_major_formatter(mticker.PercentFormatter())
ax.grid(True, axis="y", color="#222222", lw=0.5, alpha=0.6)
plt.tight_layout()
plt.savefig(f"{OUT_DIR}/omit_by_escs.png", dpi=150, bbox_inches="tight", facecolor=fig.get_facecolor())
plt.close()
print("  Saved: omit_by_escs.png")
print(qdf.to_string(index=False))

print("\nDone.")
