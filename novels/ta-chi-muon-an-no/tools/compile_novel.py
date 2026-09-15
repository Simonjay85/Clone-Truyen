#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "planning" / "master_manifest.json"
CHAPTERS = ROOT / "chapters"
OUT = ROOT / "compiled"


def main():
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    OUT.mkdir(parents=True, exist_ok=True)
    missing = []
    all_parts = [f"# {manifest['title']}\n"]
    for volume in range(1, 17):
        info = [c for c in manifest["chapters"] if c["volume"] == volume]
        title = info[0]["volume_title"]
        parts = [f"# Quyển {volume}: {title}\n"]
        for c in info:
            p = ROOT / c["draft_file"]
            if not p.exists():
                missing.append(c["chapter"])
                continue
            text = p.read_text(encoding="utf-8").strip()
            parts.append(text + "\n")
            all_parts.append(text + "\n")
        (OUT / f"volume_{volume:02d}.md").write_text("\n\n".join(parts), encoding="utf-8")
    (OUT / "full_novel.md").write_text("\n\n".join(all_parts), encoding="utf-8")
    print(f"compiled 16 volume files; missing={len(missing)}")
    if missing:
        print("missing chapters:", missing[:100], "..." if len(missing) > 100 else "")
        return 1
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
