#!/usr/bin/env python3
"""
Build script for PISA Data Stories.

Usage:
    python scripts/build_site.py          # regenerate docs/index.html
    python scripts/build_site.py --check  # audit only, no writes

Each accepted story must have:
    stories/accepted/<slug>/story.json    -- metadata (required)
    docs/<slug>/index.html                -- published page (warned if missing)

docs/index.html is always regenerated from scratch.
Story pages in docs/<slug>/ are never modified by this script.
"""

import json
import sys
import warnings
from datetime import date, datetime
from pathlib import Path

# ── Paths ──────────────────────────────────────────────────────────────────────
ROOT       = Path(__file__).parent.parent
STORIES    = ROOT / "stories" / "accepted"
DOCS       = ROOT / "docs"

CHECK_ONLY = "--check" in sys.argv


def load_stories() -> list[dict]:
    """Scan stories/accepted/ and return sorted list of story metadata dicts."""
    stories = []
    for story_dir in sorted(STORIES.iterdir()):
        if not story_dir.is_dir():
            continue
        slug = story_dir.name
        meta_path = story_dir / "story.json"

        if not meta_path.exists():
            print(f"  WARN  [{slug}] missing story.json — skipping", file=sys.stderr)
            continue

        try:
            meta = json.loads(meta_path.read_text())
        except json.JSONDecodeError as e:
            print(f"  ERROR [{slug}] invalid story.json: {e}", file=sys.stderr)
            continue

        required = {"title", "subtitle", "description", "date"}
        missing = required - meta.keys()
        if missing:
            print(f"  WARN  [{slug}] story.json missing fields: {missing}", file=sys.stderr)

        published = DOCS / slug / "index.html"
        if not published.exists():
            print(f"  WARN  [{slug}] no published page at docs/{slug}/index.html", file=sys.stderr)
            meta["_missing_page"] = True
        else:
            meta["_missing_page"] = False

        meta["slug"] = slug
        stories.append(meta)

    # Sort newest first
    def sort_key(s):
        try:
            return datetime.strptime(s.get("date", "1970-01-01"), "%Y-%m-%d")
        except ValueError:
            return datetime.min

    stories.sort(key=sort_key, reverse=True)
    return stories


def tag_html(tag: str) -> str:
    return f'<span class="tag">{tag}</span>'


def card_html(story: dict) -> str:
    slug        = story["slug"]
    title       = story.get("title", slug)
    subtitle    = story.get("subtitle", "")
    description = story.get("description", "")
    raw_date    = story.get("date", "")
    tags        = story.get("tags", [])
    missing     = story.get("_missing_page", False)

    try:
        display_date = datetime.strptime(raw_date, "%Y-%m-%d").strftime("%B %-d, %Y")
    except (ValueError, TypeError):
        display_date = raw_date

    tags_html = "".join(tag_html(t) for t in tags[:5])
    link      = f"./{slug}/"
    disabled  = ' aria-disabled="true" tabindex="-1"' if missing else ""
    cls       = "story-card missing" if missing else "story-card"
    missing_badge = '<span class="badge-missing">page not yet published</span>' if missing else ""

    return f"""
      <a href="{link}" class="{cls}"{disabled}>
        <div class="card-inner">
          <div class="card-meta">
            <span class="card-subtitle">{subtitle}</span>
            <span class="card-date">{display_date}</span>
          </div>
          <h2 class="card-title">{title}</h2>
          <p class="card-desc">{description}</p>
          {missing_badge}
          <div class="card-tags">{tags_html}</div>
          <span class="card-arrow">Read story →</span>
        </div>
      </a>"""


def build_index(stories: list[dict]) -> str:
    built_at  = date.today().strftime("%B %-d, %Y")
    n         = len(stories)
    cards     = "\n".join(card_html(s) for s in stories)
    count_txt = f"{n} {'story' if n == 1 else 'stories'}"

    return f"""<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>PISA Data Stories</title>
<meta name="description" content="Evidence-backed stories from PISA education data.">
<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect fill='%230d1117' width='64' height='64' rx='10'/%3E%3Ctext x='32' y='42' text-anchor='middle' font-size='34' font-family='serif'%3E📊%3C/text%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;0,900;1,700&family=Lora:ital,wght@0,400;0,600;1,400&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
<style>
:root {{
  --bg:      #f7f4ef;
  --bg2:     #ede9e2;
  --text:    #1a1212;
  --text2:   #4a3f3a;
  --text3:   #7a6f6a;
  --border:  #d4cfc8;
  --accent:  #c0392b;
  --card:    #ffffff;
  --shadow:  rgba(0,0,0,0.07);
}}
[data-theme="dark"] {{
  --bg:      #0d1117;
  --bg2:     #161b22;
  --text:    #e8e3da;
  --text2:   #b0a89f;
  --text3:   #6e6660;
  --border:  #2a2a35;
  --accent:  #e05c1a;
  --card:    #161b22;
  --shadow:  rgba(0,0,0,0.4);
}}

*, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
html {{ scroll-behavior: smooth; }}

body {{
  background: var(--bg);
  color: var(--text);
  font-family: 'Lora', Georgia, serif;
  min-height: 100vh;
  transition: background 0.3s, color 0.3s;
}}

/* ── Nav ── */
nav {{
  position: sticky; top: 0; z-index: 50;
  display: flex; align-items: center; justify-content: space-between;
  padding: 0.75rem 2rem;
  background: var(--bg);
  border-bottom: 1px solid var(--border);
  backdrop-filter: blur(8px);
  transition: background 0.3s, border-color 0.3s;
}}
.nav-brand {{
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.7rem; font-weight: 600;
  letter-spacing: 0.15em; text-transform: uppercase;
  color: var(--text3);
}}
.btn-icon {{
  background: none; border: 1px solid var(--border); cursor: pointer;
  color: var(--text2); width: 36px; height: 36px; border-radius: 6px;
  display: flex; align-items: center; justify-content: center;
  font-size: 0.9rem; transition: all 0.2s;
}}
.btn-icon:hover {{ border-color: var(--accent); color: var(--accent); }}

/* ── Hero ── */
.hero {{
  max-width: 900px; margin: 0 auto;
  padding: 5rem 2rem 4rem;
}}
.hero-kicker {{
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.72rem; font-weight: 600;
  letter-spacing: 0.18em; text-transform: uppercase;
  color: var(--accent); margin-bottom: 1rem;
  opacity: 0; animation: fadeUp 0.6s ease 0.1s forwards;
}}
.hero h1 {{
  font-family: 'Playfair Display', Georgia, serif;
  font-size: clamp(2.8rem, 7vw, 5rem);
  font-weight: 900; line-height: 1.05;
  letter-spacing: -0.03em; margin-bottom: 1rem;
  opacity: 0; animation: fadeUp 0.7s ease 0.2s forwards;
}}
.hero-sub {{
  font-size: clamp(1rem, 2.5vw, 1.2rem);
  color: var(--text2); max-width: 540px; line-height: 1.65;
  opacity: 0; animation: fadeUp 0.7s ease 0.35s forwards;
}}
.hero-count {{
  margin-top: 2rem;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.72rem; color: var(--text3); letter-spacing: 0.06em;
  opacity: 0; animation: fadeUp 0.6s ease 0.5s forwards;
}}
.hero-rule {{
  border: none; border-top: 1px solid var(--border);
  margin: 0 2rem;
  opacity: 0; animation: fadeIn 0.6s ease 0.55s forwards;
}}

@keyframes fadeUp  {{ from {{ opacity:0; transform:translateY(18px) }} to {{ opacity:1; transform:translateY(0) }} }}
@keyframes fadeIn  {{ from {{ opacity:0 }} to {{ opacity:1 }} }}

/* ── Grid ── */
.grid {{
  max-width: 900px; margin: 0 auto;
  padding: 3rem 2rem 6rem;
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
  gap: 1.25rem;
}}

/* ── Card ── */
.story-card {{
  display: block; text-decoration: none; color: inherit;
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: 10px;
  transition: border-color 0.2s, box-shadow 0.2s, transform 0.2s;
  opacity: 0; animation: fadeUp 0.6s ease forwards;
}}
.story-card:hover {{
  border-color: var(--accent);
  box-shadow: 0 6px 24px var(--shadow);
  transform: translateY(-2px);
}}
.story-card:focus-visible {{
  outline: 2px solid var(--accent); outline-offset: 3px;
}}
.story-card.missing {{
  opacity: 0.45; pointer-events: none;
}}
.card-inner {{ padding: 1.6rem 1.75rem; }}
.card-meta {{
  display: flex; align-items: center; justify-content: space-between;
  margin-bottom: 0.6rem;
}}
.card-subtitle {{
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.65rem; font-weight: 600;
  letter-spacing: 0.12em; text-transform: uppercase;
  color: var(--accent);
}}
.card-date {{
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.65rem; color: var(--text3);
}}
.card-title {{
  font-family: 'Playfair Display', Georgia, serif;
  font-size: 1.35rem; font-weight: 700;
  line-height: 1.25; margin-bottom: 0.65rem;
  letter-spacing: -0.01em;
}}
.card-desc {{
  font-size: 0.88rem; color: var(--text2);
  line-height: 1.65; margin-bottom: 1rem;
}}
.badge-missing {{
  display: inline-block;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.62rem; letter-spacing: 0.08em; text-transform: uppercase;
  padding: 0.2rem 0.5rem; border-radius: 4px;
  background: var(--border); color: var(--text3);
  margin-bottom: 0.75rem;
}}
.card-tags {{ display: flex; flex-wrap: wrap; gap: 0.35rem; margin-bottom: 1.1rem; }}
.tag {{
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.62rem; font-weight: 600;
  letter-spacing: 0.07em; text-transform: uppercase;
  padding: 0.2rem 0.55rem; border-radius: 4px;
  background: var(--bg2); color: var(--text3);
  border: 1px solid var(--border);
}}
.card-arrow {{
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.72rem; color: var(--accent);
  letter-spacing: 0.04em;
  transition: letter-spacing 0.2s;
}}
.story-card:hover .card-arrow {{ letter-spacing: 0.1em; }}

/* ── Footer ── */
footer {{
  border-top: 1px solid var(--border);
  padding: 2rem;
  text-align: center;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.7rem; color: var(--text3); line-height: 1.9;
}}

@media (max-width: 600px) {{
  .hero {{ padding: 3rem 1.25rem 2.5rem; }}
  .grid {{ padding: 2rem 1.25rem 5rem; grid-template-columns: 1fr; }}
  nav {{ padding: 0.6rem 1.25rem; }}
}}
</style>
</head>
<body>

<nav>
  <span class="nav-brand">PISA Data Stories</span>
  <button class="btn-icon" id="theme-toggle" aria-label="Toggle dark mode" title="Toggle theme">☀︎</button>
</nav>

<header class="hero">
  <p class="hero-kicker">OECD PISA 2018</p>
  <h1>PISA Data Stories</h1>
  <p class="hero-sub">Evidence-backed stories from PISA education data. Each story tests one hypothesis against 612,004 students across 79 countries.</p>
  <p class="hero-count">{count_txt} · built {built_at}</p>
</header>

<hr class="hero-rule">

<main class="grid" id="story-grid">
{cards}
</main>

<footer>
  Data: OECD PISA 2018 Database · Analysis: June 2026<br>
  Not affiliated with the OECD · Source on GitHub
</footer>

<script>
// ── Dark mode ──
const html = document.documentElement;
const btn  = document.getElementById('theme-toggle');
function applyTheme(dark) {{
  html.setAttribute('data-theme', dark ? 'dark' : 'light');
  btn.textContent = dark ? '☀︎' : '☾';
  const url = new URL(location);
  url.searchParams.set('dark', dark ? '1' : '0');
  history.replaceState(null, '', url.toString());
}}
const p = new URL(location).searchParams.get('dark');
applyTheme(p === null ? true : p === '1');
btn.addEventListener('click', () => applyTheme(html.getAttribute('data-theme') === 'light'));

// ── Stagger card animations ──
document.querySelectorAll('.story-card').forEach((card, i) => {{
  card.style.animationDelay = (0.6 + i * 0.12) + 's';
}});
</script>
</body>
</html>
"""


def main():
    print("PISA Data Stories — build")
    print(f"  root: {ROOT}")
    print()

    stories = load_stories()

    if not stories:
        print("  ERROR no stories found — nothing to build.", file=sys.stderr)
        sys.exit(1)

    print(f"  found {len(stories)} story/stories:")
    for s in stories:
        flag = " [missing page]" if s.get("_missing_page") else ""
        print(f"    · {s['slug']}{flag}")

    if CHECK_ONLY:
        print("\n  --check mode: no files written.")
        return

    print()
    DOCS.mkdir(exist_ok=True)
    index_path = DOCS / "index.html"
    index_path.write_text(build_index(stories), encoding="utf-8")
    print(f"  wrote  {index_path.relative_to(ROOT)}")
    print("\n  done.")


if __name__ == "__main__":
    main()
