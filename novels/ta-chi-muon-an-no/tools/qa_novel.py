#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations
import argparse
import hashlib
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "planning" / "master_manifest.json"
CHAPTERS = ROOT / "chapters"
REPORTS = ROOT / "reports"

PLACEHOLDERS = [
    r"\bTODO\b", r"\bTBD\b", r"\[placeholder\]", r"\[viết thêm\]",
    r"nội dung chương", r"sang chương \d+", r"cốt truyện", r"nhân vật chính"
]
AI_PHRASES = [
    "sắc mặt đại biến", "hít một ngụm khí lạnh", "không thể tin nổi",
    "kinh thiên động địa", "khóe miệng nhếch lên"
]

def word_count(text: str) -> int:
    body = re.sub(r"^#.*$", "", text, flags=re.M)
    return len(re.findall(r"\b[\wÀ-ỹĐđ]+\b", body, flags=re.UNICODE))


def normalize_para(p: str) -> str:
    p = re.sub(r"[#*_>`~\[\](){}]", " ", p.lower())
    p = re.sub(r"\s+", " ", p).strip()
    return p


def chapter_path(n: int) -> Path:
    return CHAPTERS / f"chapter_{n:03d}.md"


def parse_range(spec: str | None, max_chap: int = 800):
    if not spec:
        return 1, max_chap
    m = re.fullmatch(r"(\d+)(?:-(\d+))?", spec.strip())
    if not m:
        raise SystemExit("--range must be N or A-B")
    a = int(m.group(1)); b = int(m.group(2) or a)
    if a < 1 or b > max_chap or a > b:
        raise SystemExit("invalid chapter range")
    return a, b


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--range", dest="range_spec")
    ap.add_argument("--hard-floor", type=int, default=1500)
    ap.add_argument("--allow-missing", action="store_true")
    args = ap.parse_args()

    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    hard = []
    warn = []
    stats = {}

    if manifest.get("chapter_count") != 800 or len(manifest.get("chapters", [])) != 800:
        hard.append("Manifest does not contain exactly 800 chapter records")
    nums = [c.get("chapter") for c in manifest.get("chapters", [])]
    if nums != list(range(1, 801)):
        hard.append("Manifest numbering is not exactly 1..800")
    if len(manifest.get("arcs", [])) != 80:
        hard.append("Manifest does not contain exactly 80 ten-chapter sub-arcs")

    a, b = parse_range(args.range_spec)
    seen_titles = {}
    paragraph_hashes = defaultdict(list)
    phrase_counts = Counter()
    checked = 0
    missing = []
    word_counts = {}

    for n in range(a, b + 1):
        p = chapter_path(n)
        if not p.exists():
            missing.append(n)
            if not args.allow_missing:
                hard.append(f"Missing chapter file: {p.name}")
            continue
        checked += 1
        text = p.read_text(encoding="utf-8")
        wc = word_count(text)
        word_counts[n] = wc
        if wc < args.hard_floor:
            hard.append(f"Ch{n:03d} word count {wc} < hard floor {args.hard_floor}")

        first = text.splitlines()[0].strip() if text.splitlines() else ""
        m = re.match(r"^#\s*Chương\s+(\d+)\s*:\s*(.+)$", first, flags=re.I)
        if not m:
            hard.append(f"Ch{n:03d} invalid/missing heading")
        else:
            heading_num = int(m.group(1))
            title = m.group(2).strip().lower()
            if heading_num != n:
                hard.append(f"Ch{n:03d} heading number says {heading_num}")
            if title in seen_titles:
                hard.append(f"Duplicate chapter title Ch{n:03d} and Ch{seen_titles[title]:03d}: {title}")
            seen_titles[title] = n

        for pat in PLACEHOLDERS:
            if re.search(pat, text, flags=re.I):
                hard.append(f"Ch{n:03d} placeholder/meta match: {pat}")

        lower = text.lower()
        for phrase in AI_PHRASES:
            count = lower.count(phrase)
            if count:
                phrase_counts[phrase] += count

        paras = [normalize_para(x) for x in re.split(r"\n\s*\n", text) if len(normalize_para(x)) >= 80]
        for para in paras:
            digest = hashlib.sha1(para.encode("utf-8")).hexdigest()
            paragraph_hashes[digest].append((n, para[:120]))

    dup_groups = [v for v in paragraph_hashes.values() if len(v) > 1]
    for group in dup_groups[:50]:
        locs = ", ".join(f"Ch{x[0]:03d}" for x in group)
        hard.append(f"Exact repeated paragraph across {locs}: {group[0][1]}...")

    for phrase, count in phrase_counts.items():
        span = max(1, b-a+1)
        if count > max(2, span // 15):
            warn.append(f"Overused AI phrase '{phrase}': {count} times in {span} chapters")

    if word_counts:
        stats["word_count_min"] = min(word_counts.values())
        stats["word_count_max"] = max(word_counts.values())
        stats["word_count_avg"] = round(sum(word_counts.values())/len(word_counts), 1)
    stats.update({
        "range": f"{a}-{b}",
        "checked_files": checked,
        "missing_files": missing,
        "hard_fail_count": len(hard),
        "warning_count": len(warn),
    })

    report = {"status": "PASS" if not hard else "FAIL", "stats": stats, "hard_failures": hard, "warnings": warn}
    REPORTS.mkdir(parents=True, exist_ok=True)
    out = REPORTS / "qa_latest.json"
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if not hard else 1

if __name__ == "__main__":
    sys.exit(main())
