#!/usr/bin/env python3
"""
prepare_pisa_cycle.py -- Download and extract minimal PISA datasets for cross-cycle work.

Produces two processed outputs per cycle:

  Core extract      pisa_{cycle}_core.csv.gz
      One row per student. Identifiers, final weight, and all plausible values
      (math / reading / science). Use this when student-level data is needed.

  School summary    pisa_{cycle}_school_summary.csv
      One row per school. Weighted student counts and weighted domain means/SDs.
      Use this first — it avoids re-reading the core extract for most school-level work.

Replicate weights (W_FSTURWT1-80) are excluded from the core extract to keep file
sizes manageable. Load raw SPSS data only if full BRR standard errors are required.

Usage:
    python3 scripts/prepare_pisa_cycle.py --cycle 2022
    python3 scripts/prepare_pisa_cycle.py --cycle 2015 --raw-zip ~/Downloads/file.zip
    python3 scripts/prepare_pisa_cycle.py --cycle 2022 --force

Outputs (all relative to project root):
    data/raw/SPSS_STU_QQQ_{cycle}.zip           (gitignored, re-downloadable)
    data/processed/pisa_{cycle}_core.csv.gz
    data/processed/pisa_{cycle}_school_summary.csv
    data/processed/pisa_cycles_inventory.csv     (updated each run)
"""

import argparse
import csv
import os
import sys
import tempfile
import urllib.request
import zipfile
from datetime import datetime, timezone
from pathlib import Path

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

PROCESSING_VERSION = "1.0"

ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = ROOT / "data" / "raw"
PROC_DIR = ROOT / "data" / "processed"
INVENTORY_PATH = PROC_DIR / "pisa_cycles_inventory.csv"

# Columns extracted from raw SPSS into the core CSV.
# Replicate weights are excluded — use raw data for BRR SEs.
KEEP_COLS = (
    ["CNT", "CNTSCHID", "CNTSTUID", "W_FSTUWT"]
    + [f"PV{i}MATH" for i in range(1, 11)]
    + [f"PV{i}READ" for i in range(1, 11)]
    + [f"PV{i}SCIE" for i in range(1, 11)]
)
DOMAINS = {
    "MATH": [f"PV{i}MATH" for i in range(1, 11)],
    "READ": [f"PV{i}READ" for i in range(1, 11)],
    "SCIE": [f"PV{i}SCIE" for i in range(1, 11)],
}

# Per-cycle download configuration.
# url=None means automated download is unavailable; user must supply --raw-zip.
#
# URL availability (verified 2026-07-06):
#   webfs.oecd.org hosts 2018 and 2022 without authentication. All other years
#   return 404 on webfs. Pre-2015 cycles are hosted on oecd.org/pisaproducts/,
#   but that path returns 403 — OECD requires free account registration to access
#   those files. No bypass is available via URL manipulation or Referer spoofing.
CYCLE_CONFIG = {
    "2012": {
        "url": None,  # oecd.org/pisaproducts/ returns 403; requires OECD account registration
        "download_note": (
            "OECD requires free account registration to access PISA 2012 files.\n"
            "      No public direct-download URL exists for pre-2015 cycles.\n"
            "      Register at: https://www.oecd.org/en/data/register.html"
        ),
        "manual_download_page": "https://www.oecd.org/pisa/data/2012database/",
        "manual_file_hint": (
            "Student questionnaire data file (SPSS format). "
            "Look for a file named 'INT_STU12_DEC03.zip' or similar."
        ),
        "raw_filename": "SPSS_STU_QQQ_2012.zip",
        # PISA 2012 used different identifier variable names than 2015+.
        # These mappings are based on OECD documentation; verify against actual
        # column names if the pipeline reports them as missing.
        "var_map": {
            "SCHOOLID": "CNTSCHID",  # pre-2015 identifier name
            "STIDSTD": "CNTSTUID",   # pre-2015 identifier name
        },
    },
    "2015": {
        "url": None,  # OECD 2015 data page is Cloudflare-gated; requires browser download
        "download_note": "The OECD 2015 data page is Cloudflare-gated (requires a browser).",
        "manual_download_page": "https://www.oecd.org/pisa/data/2015database/",
        "manual_file_hint": "Student questionnaire data file (SPSS format, "
                            "typically 'PUF_SPSS_COMBINED_CMB_STU_QQQ.zip')",
        "raw_filename": "SPSS_STU_QQQ_2015.zip",
        "var_map": {},  # core variable names are identical to 2018
    },
    "2022": {
        "url": "https://webfs.oecd.org/pisa2022/STU_QQQ_SPSS.zip",
        "download_note": None,
        "manual_download_page": "https://www.oecd.org/pisa/data/2022database/",
        "manual_file_hint": None,
        "raw_filename": "SPSS_STU_QQQ_2022.zip",
        "var_map": {},  # core variable names are identical to 2018
    },
}

# ---------------------------------------------------------------------------
# Inventory schema
# ---------------------------------------------------------------------------

INVENTORY_FIELDS = [
    "cycle",
    "raw_filename",
    "n_countries",
    "n_schools",
    "n_students",
    "core_filename",
    "core_size_mb",
    "school_summary_filename",
    "school_summary_size_mb",
    "variables_included",
    "date_processed",
    "processing_script_version",
    "notes",
]

# ---------------------------------------------------------------------------
# Download
# ---------------------------------------------------------------------------


def download_file(url: str, dest: Path) -> None:
    """Download url → dest, preferring curl (avoids Python SSL cert issues on macOS)."""
    import shutil
    import subprocess

    tmp = dest.with_suffix(".part")
    print(f"  Downloading {url}")
    print(f"  → {dest.relative_to(ROOT)}")
    try:
        if shutil.which("curl"):
            subprocess.run(
                ["curl", "-L", "--progress-bar", "-o", str(tmp), url],
                check=True,
            )
        else:
            import ssl
            ctx = ssl.create_default_context()
            ctx.check_hostname = False
            ctx.verify_mode = ssl.CERT_NONE
            print("  (curl not found; using urllib with unverified SSL)")
            opener = urllib.request.build_opener(urllib.request.HTTPSHandler(context=ctx))
            with opener.open(url) as resp, open(tmp, "wb") as f:
                total = int(resp.headers.get("Content-Length", 0))
                downloaded = 0
                while chunk := resp.read(65536):
                    f.write(chunk)
                    downloaded += len(chunk)
                    if total:
                        print(f"\r  {downloaded/total*100:5.1f}%  {downloaded/1e6:.0f}/{total/1e6:.0f} MB",
                              end="", flush=True)
            print()
        tmp.rename(dest)
    except Exception:
        if tmp.exists():
            tmp.unlink()
        raise


# ---------------------------------------------------------------------------
# Core extract (raw SPSS → slim student CSV)
# ---------------------------------------------------------------------------


def find_sav_in_zip(zip_path: Path) -> str:
    """Return the filename of the student .sav inside the zip."""
    with zipfile.ZipFile(zip_path) as z:
        names = [n for n in z.namelist() if n.lower().endswith(".sav")]
    if not names:
        raise ValueError(f"No .sav file found in {zip_path}")
    if len(names) > 1:
        stu = [n for n in names if "STU" in n.upper() or "QQQ" in n.upper()]
        if stu:
            names = stu
    return names[0]


def extract_core(zip_path: Path, cycle: str, var_map: dict) -> tuple:
    """Extract SPSS zip → core CSV.gz. Returns (out_path, df)."""
    try:
        import pyreadstat
    except ImportError:
        sys.exit("pyreadstat is required. Install with: uv pip install pyreadstat")
    import pandas as pd

    out_path = PROC_DIR / f"pisa_{cycle}_core.csv.gz"

    sav_name = find_sav_in_zip(zip_path)
    print(f"  Found SPSS file: {sav_name}")
    print("  Probing column availability…")

    with zipfile.ZipFile(zip_path) as z:
        with tempfile.TemporaryDirectory() as tmpdir:
            z.extract(sav_name, tmpdir)
            sav_path = os.path.join(tmpdir, sav_name)

            _, meta = pyreadstat.read_sav(sav_path, row_limit=1)
            available = set(meta.column_names)

            # Resolve KEEP_COLS through var_map so pre-2015 raw names (e.g.
            # SCHOOLID, STIDSTD) are requested from the file, not the harmonized
            # names (CNTSCHID, CNTSTUID) that don't exist in pre-2015 files.
            reverse_map = {v: k for k, v in var_map.items()}
            raw_keep = [reverse_map.get(c, c) for c in KEEP_COLS]

            raw_use_cols = [rc for rc in raw_keep if rc in available]
            harmonized_missing = [KEEP_COLS[i] for i, rc in enumerate(raw_keep)
                                  if rc not in available]

            if harmonized_missing:
                print(f"  WARNING: {len(harmonized_missing)} requested columns not in this cycle:")
                for m in harmonized_missing:
                    print(f"    - {m}")

            print(f"  Reading {len(raw_use_cols)} columns from {len(meta.column_names)}-column dataset…")
            df, _ = pyreadstat.read_sav(sav_path, usecols=raw_use_cols)

    if var_map:
        df = df.rename(columns=var_map)
        print(f"  Applied {len(var_map)} variable renames.")

    df.insert(0, "CYCLE", int(cycle))

    before = len(df)
    df = df[df["W_FSTUWT"].notna() & (df["W_FSTUWT"] > 0)]
    if (dropped := before - len(df)):
        print(f"  Dropped {dropped:,} rows with missing/zero weight.")

    print(f"  Writing {len(df):,} student rows, {df['CNT'].nunique()} countries…")
    PROC_DIR.mkdir(parents=True, exist_ok=True)
    df.to_csv(out_path, index=False, compression="gzip")

    mb = out_path.stat().st_size / 1e6
    print(f"  Core extract: {out_path.relative_to(ROOT)}  ({mb:.1f} MB)")
    return out_path, df


# ---------------------------------------------------------------------------
# School summary (core CSV → aggregated school CSV)
# ---------------------------------------------------------------------------


def compute_school_summary(core_path: Path, cycle: str) -> tuple:
    """Aggregate core extract into a per-school summary. Returns (out_path, school_df).

    Scores are computed as the unweighted mean across the 10 plausible values per
    student (a point estimate, not full Rubin's-rules pooling). School-level means
    and SDs are then weighted by W_FSTUWT. This is appropriate for exploration and
    quick lookup; use the core extract with proper PV pooling for rigorous analysis.
    """
    import numpy as np
    import pandas as pd

    out_path = PROC_DIR / f"pisa_{cycle}_school_summary.csv"
    print(f"  Reading core extract for aggregation…")
    df = pd.read_csv(core_path)

    # Detect which domains are fully present
    active_domains = {d: cols for d, cols in DOMAINS.items()
                      if all(c in df.columns for c in cols)}
    if not active_domains:
        print("  WARNING: No PV columns found in core extract. School summary will be counts only.")

    # --- student-level scores (mean of 10 PVs per domain) ---
    for d, cols in active_domains.items():
        df[f"SCORE_{d}"] = df[cols].mean(axis=1)
        df[f"WX_{d}"] = df["W_FSTUWT"] * df[f"SCORE_{d}"]

    # --- step 1: weighted sums per school ---
    base_agg = {"N_STUDENTS_SAMPLED": ("W_FSTUWT", "count"),
                "SUM_W_FSTUWT": ("W_FSTUWT", "sum")}
    for d in active_domains:
        base_agg[f"_WSUM_{d}"] = (f"WX_{d}", "sum")

    school = df.groupby(["CNT", "CNTSCHID"]).agg(**base_agg).reset_index()

    for d in active_domains:
        school[f"MEAN_{d}"] = school[f"_WSUM_{d}"] / school["SUM_W_FSTUWT"]

    # --- step 2: weighted population SD (two-pass) ---
    score_cols = [f"SCORE_{d}" for d in active_domains]
    mean_cols = [f"MEAN_{d}" for d in active_domains]
    dev_df = df[["CNT", "CNTSCHID", "W_FSTUWT"] + score_cols].merge(
        school[["CNT", "CNTSCHID"] + mean_cols], on=["CNT", "CNTSCHID"]
    )
    for d in active_domains:
        dev_df[f"_WSQ_{d}"] = dev_df["W_FSTUWT"] * (dev_df[f"SCORE_{d}"] - dev_df[f"MEAN_{d}"]) ** 2

    sq_sums = dev_df.groupby(["CNT", "CNTSCHID"])[
        [f"_WSQ_{d}" for d in active_domains]
    ].sum().reset_index()

    school = school.merge(sq_sums, on=["CNT", "CNTSCHID"])
    for d in active_domains:
        school[f"SD_{d}"] = np.sqrt(school[f"_WSQ_{d}"] / school["SUM_W_FSTUWT"])

    # Drop intermediate columns and prepend CYCLE
    drop = [c for c in school.columns if c.startswith("_")]
    school = school.drop(columns=drop)
    school.insert(0, "CYCLE", int(cycle))

    school.to_csv(out_path, index=False)
    kb = out_path.stat().st_size / 1e3
    print(f"  School summary: {out_path.relative_to(ROOT)}  "
          f"({len(school):,} schools, {kb:.0f} KB)")
    return out_path, school


# ---------------------------------------------------------------------------
# Inventory
# ---------------------------------------------------------------------------


def load_inventory() -> dict:
    rows = {}
    if INVENTORY_PATH.exists():
        with open(INVENTORY_PATH, newline="") as f:
            for row in csv.DictReader(f):
                rows[row["cycle"]] = row
    return rows


def save_inventory(rows: dict) -> None:
    PROC_DIR.mkdir(parents=True, exist_ok=True)
    with open(INVENTORY_PATH, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=INVENTORY_FIELDS, extrasaction="ignore")
        w.writeheader()
        for cyc in sorted(rows):
            w.writerow(rows[cyc])


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main():
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("--cycle", required=True, choices=sorted(CYCLE_CONFIG),
                        help="PISA cycle year (e.g. 2022)")
    parser.add_argument("--raw-zip", metavar="PATH",
                        help="Path to a manually downloaded student SPSS zip. "
                             "Copies it to data/raw/ and skips the download step.")
    parser.add_argument("--force", action="store_true",
                        help="Re-extract and re-aggregate even if outputs exist.")
    args = parser.parse_args()

    cycle = args.cycle
    cfg = CYCLE_CONFIG[cycle]
    RAW_DIR.mkdir(parents=True, exist_ok=True)

    raw_path = RAW_DIR / cfg["raw_filename"]
    core_path = PROC_DIR / f"pisa_{cycle}_core.csv.gz"
    summary_path = PROC_DIR / f"pisa_{cycle}_school_summary.csv"

    print(f"\n=== PISA {cycle} — v{PROCESSING_VERSION} ===")

    # ── Step 1: ensure raw file exists ──────────────────────────────────────
    if raw_path.exists() and not args.force:
        print(f"[1/4] Raw file present: {raw_path.relative_to(ROOT)}")
    elif args.raw_zip:
        import shutil
        src = Path(args.raw_zip).expanduser().resolve()
        if not src.exists():
            sys.exit(f"ERROR: --raw-zip path does not exist: {src}")
        print(f"[1/4] Copying zip → {raw_path.relative_to(ROOT)}")
        shutil.copy2(src, raw_path)
    elif cfg["url"]:
        print("[1/4] Downloading raw data…")
        try:
            download_file(cfg["url"], raw_path)
        except Exception as e:
            sys.exit(
                f"ERROR: Download failed: {e}\n"
                f"  Try manually from: {cfg['manual_download_page']}\n"
                f"  Then re-run with: --raw-zip /path/to/file.zip"
            )
    else:
        note = cfg.get("download_note") or "Automated download is unavailable."
        print(f"[1/4] Automated download unavailable for PISA {cycle}.")
        print(f"      {note}")
        print()
        print(f"      Steps:")
        print(f"        1. Open: {cfg['manual_download_page']}")
        if cfg.get("manual_file_hint"):
            print(f"        2. Download: {cfg['manual_file_hint']}")
        print(f"        3. Re-run:")
        print(f"             python3 scripts/prepare_pisa_cycle.py "
              f"--cycle {cycle} --raw-zip /path/to/downloaded.zip")
        sys.exit(1)

    # ── Step 2: core extract (raw SPSS → student CSV) ───────────────────────
    # Migration: rename old _harmonized files produced before v1.0
    old_name = PROC_DIR / f"pisa_{cycle}_harmonized.csv.gz"
    if old_name.exists() and not core_path.exists():
        print(f"[2/4] Migrating {old_name.name} → {core_path.name}")
        old_name.rename(core_path)

    if core_path.exists() and not args.force:
        print(f"[2/4] Core extract present: {core_path.relative_to(ROOT)}")
    else:
        print("[2/4] Extracting core data from raw SPSS…")
        core_path, _ = extract_core(raw_path, cycle, cfg["var_map"])

    # ── Step 3: school summary (core → per-school CSV) ───────────────────────
    if summary_path.exists() and not args.force:
        print(f"[3/4] School summary present: {summary_path.relative_to(ROOT)}")
    else:
        print("[3/4] Aggregating school summary from core extract…")
        summary_path, school_df = compute_school_summary(core_path, cycle)

    # ── Step 4: update inventory ─────────────────────────────────────────────
    print("[4/4] Updating cycle inventory…")
    import re
    import pandas as pd
    _peek = pd.read_csv(core_path, usecols=["CNT", "CNTSCHID"])
    n_students = len(_peek)
    n_countries = _peek["CNT"].nunique()
    n_schools = _peek["CNTSCHID"].nunique()

    # Build a compact variables description from the actual columns present.
    _cols = pd.read_csv(core_path, nrows=0).columns.tolist()
    _pv_nums = [int(m) for c in _cols for m in re.findall(r"^PV(\d+)", c)]
    _max_pv = max(_pv_nums) if _pv_nums else 0
    _pv_range = f"[1-{_max_pv}]" if _max_pv else ""
    vars_desc = (
        f"CYCLE,CNT,CNTSCHID,CNTSTUID,W_FSTUWT,"
        f"PV{_pv_range}MATH,PV{_pv_range}READ,PV{_pv_range}SCIE"
    )

    rows = load_inventory()

    raw_2018 = RAW_DIR / "SPSS_STU_QQQ.zip"
    if "2018" not in rows:
        rows["2018"] = {
            "cycle": "2018",
            "raw_filename": "SPSS_STU_QQQ.zip",
            "n_countries": "",
            "n_schools": "",
            "n_students": "",
            "core_filename": "",
            "core_size_mb": "",
            "school_summary_filename": "",
            "school_summary_size_mb": "",
            "variables_included": "see variable_catalog.csv",
            "date_processed": "",
            "processing_script_version": "",
            "notes": "Primary cycle. Stories read raw SPSS directly; no core extract.",
        }
    rows["2018"]["raw_filename"] = "SPSS_STU_QQQ.zip"

    rows[cycle] = {
        "cycle": cycle,
        "raw_filename": cfg["raw_filename"],
        "n_countries": n_countries,
        "n_schools": n_schools,
        "n_students": n_students,
        "core_filename": core_path.name,
        "core_size_mb": f"{core_path.stat().st_size / 1e6:.1f}",
        "school_summary_filename": summary_path.name,
        "school_summary_size_mb": f"{summary_path.stat().st_size / 1e6:.2f}",
        "variables_included": vars_desc,
        "date_processed": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "processing_script_version": PROCESSING_VERSION,
        "notes": "",
    }
    save_inventory(rows)
    print(f"  Written: {INVENTORY_PATH.relative_to(ROOT)}")

    print(f"""
Done. Quick reference:

  School-level work (first choice):
    pd.read_csv('data/processed/pisa_{cycle}_school_summary.csv')

  Student-level work:
    pd.read_csv('data/processed/pisa_{cycle}_core.csv.gz')

  Replicate weights / full BRR SEs:
    Load from data/raw/{cfg['raw_filename']}  (raw SPSS)
""")


if __name__ == "__main__":
    main()
