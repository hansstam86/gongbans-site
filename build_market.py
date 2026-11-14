#!/usr/bin/env python3
"""
build_market.py — external market-check findings on the start packs, from data/market-check.json.

For every idea that has an entry:

    startpacks/<slug>.md   (a) a callout at the end of section 1 (Summary), before the validate-demand
                               gate: verdict, two-sentence summary, main risk, caveat, and the audience
                               correction when the research found one
                               — between <!-- market-check:start --> … <!-- market-check:end -->
                           (b) a sub-table appended to the "### Competition" subsection of the business
                               plan with the competitors / signals / comparables found and their sources
                               — between <!-- market-competitors:start --> … <!-- market-competitors:end -->

The research was done by web search in November 2026 (see data/market-check.json → method). Sources are
cited by name as given; none is linked, because no link was verified here. Verdicts are quoted, never
strengthened. Every block repeats the "verify before relying on it" caveat.

Run from the repo root:  python3 build_market.py      (build_ideas.py calls patch_packs() before rendering)
"""

import json
import re
from pathlib import Path

ROOT = Path(__file__).parent
MARKET_JSON = ROOT / "data" / "market-check.json"
PACK_DIR = ROOT / "startpacks"

CALLOUT_START, CALLOUT_END = "<!-- market-check:start -->", "<!-- market-check:end -->"
TABLE_START, TABLE_END = "<!-- market-competitors:start -->", "<!-- market-competitors:end -->"


def load():
    return json.loads(MARKET_JSON.read_text(encoding="utf-8"))


def callout_md(entry, data):
    L = [f"> **External market check ({data['researched']}): {entry['verdict']}.** {entry['summary']} "
         f"**Main risk:** {entry['risk']} "
         f"*{data['caveat']} Competitors and sources found: see [the market check in the competition table](#external-market-check).*"]
    corr = entry.get("correction")
    if corr:
        L.append(">")
        L.append(f"> **{corr['title']}.** {corr['text']}")
    return "\n".join(L) + "\n"


def table_md(entry, data):
    L = ["#### External market check",
         "",
         f"Competitors, demand signals and price comparables found by web search in {data['researched']}. "
         f"Sources are named as found and not linked; {data['caveat'][0].lower() + data['caveat'][1:]}",
         "",
         "| Who / source | What it is | What it tells us |",
         "|---|---|---|"]
    for who, what, tells in entry["rows"]:
        L.append(f"| {who} | {what} | {tells} |")
    L.append("")
    L.append(f"**Verdict as researched: {entry['verdict']}.** Main risk: {entry['risk']}")
    return "\n".join(L) + "\n"


def replace_or_insert(md, start, end, block, insert_at):
    if start in md and end in md:
        return md[:md.index(start)] + f"{start}\n{block}{end}" + md[md.index(end) + len(end):]
    return md[:insert_at] + f"{start}\n{block}{end}\n\n" + md[insert_at:]


def patch_md(md, entry, data, slug):
    # (a) callout: end of section 1, i.e. just before "## 2."
    m = re.search(r"^## 2\. ", md, re.M)
    if not m:
        raise SystemExit(f"{slug}: no section 2")
    md = replace_or_insert(md, CALLOUT_START, CALLOUT_END, callout_md(entry, data), m.start())
    # (b) table: end of the "### Competition" subsection (before the next ### or ## heading)
    c = re.search(r"^### Competition.*$", md, re.M)
    if not c:
        raise SystemExit(f"{slug}: no Competition subsection")
    nxt = re.search(r"^##{1,2} ", md[c.end():], re.M)
    at = c.end() + nxt.start() if nxt else len(md)
    if TABLE_START in md:
        md = replace_or_insert(md, TABLE_START, TABLE_END, table_md(entry, data), at)
    else:
        md = md[:at].rstrip("\n") + "\n\n" + f"{TABLE_START}\n{table_md(entry, data)}{TABLE_END}\n\n" + md[at:]
    return md


def patch_packs():
    data = load()
    n = 0
    for slug, entry in data["ideas"].items():
        path = PACK_DIR / f"{slug}.md"
        if not path.exists():
            raise SystemExit(f"market-check.json names a pack that does not exist: {slug}")
        md = path.read_text(encoding="utf-8")
        new = patch_md(md, entry, data, slug)
        if new != md:
            path.write_text(new, encoding="utf-8")
        n += 1
    verdicts = {}
    for e in data["ideas"].values():
        verdicts[e["verdict"]] = verdicts.get(e["verdict"], 0) + 1
    print(f"startpacks/: external market check on {n} packs ({', '.join(f'{v} {k.lower()}' for k, v in verdicts.items())}); "
          f"corrections: {[s for s, e in data['ideas'].items() if e.get('correction')]}")
    return data


if __name__ == "__main__":
    patch_packs()
