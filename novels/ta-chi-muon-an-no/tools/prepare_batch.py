#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "planning" / "master_manifest.json"
LEDGER = ROOT / "continuity" / "ledger.json"
CHAPTERS = ROOT / "chapters"
SCRATCH = ROOT / "scratch"


def first_missing():
    for n in range(1, 801):
        if not (CHAPTERS / f"chapter_{n:03d}.md").exists():
            return n
    return 801


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--start", type=int)
    ap.add_argument("--size", type=int, default=5)
    args = ap.parse_args()
    start = args.start or first_missing()
    if start > 800:
        print("ALL_CHAPTER_FILES_PRESENT")
        return 0
    end = min(800, start + args.size - 1)
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
    planned = [c for c in manifest["chapters"] if start <= c["chapter"] <= end]
    last_entries = ledger.get("entries", [])[-10:]
    parts = [
        f"# Batch context {start:03d}-{end:03d}",
        "",
        "Read `story_bible.md` and `writer_contract.md` before drafting.",
        "",
        "## Manifest records",
        "```json",
        json.dumps(planned, ensure_ascii=False, indent=2),
        "```",
        "",
        "## Latest continuity entries",
        "```json",
        json.dumps(last_entries, ensure_ascii=False, indent=2),
        "```",
        "",
        "## Relevant unresolved hooks",
        "```json",
        json.dumps([h for h in ledger.get("unresolved_hooks", []) if h.get("status") != "paid"], ensure_ascii=False, indent=2),
        "```",
    ]
    for n in range(max(1, start-2), start):
        p = CHAPTERS / f"chapter_{n:03d}.md"
        if p.exists():
            parts.extend(["", f"## Full previous chapter {n}", p.read_text(encoding="utf-8")])
    SCRATCH.mkdir(parents=True, exist_ok=True)
    out = SCRATCH / f"batch_{start:03d}_{end:03d}_context.md"
    out.write_text("\n".join(parts), encoding="utf-8")
    print(out)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
