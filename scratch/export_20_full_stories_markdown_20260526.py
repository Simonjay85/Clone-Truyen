#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Export generated story JSON payloads into readable Markdown manuscripts."""

from __future__ import annotations

import json
import re
from pathlib import Path


BASE = Path("scratch/batch_20_full_stories_20260526")
STORIES = BASE / "stories"
OUT = BASE / "manuscripts_md"


def html_to_md(value: str) -> str:
    text = value
    text = text.replace("</p><p>", "</p>\n<p>")
    text = re.sub(r"<p>(.*?)</p>", lambda m: m.group(1).strip() + "\n", text, flags=re.S)
    text = re.sub(r"<strong>(.*?)</strong>", r"**\1**", text, flags=re.S)
    text = re.sub(r"<em>(.*?)</em>", r"*\1*", text, flags=re.S)
    text = re.sub(r"<hr\s*/?>", "\n---\n", text)
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    combined_lines = [
        "# 20 truyện full chờ duyệt",
        "",
        "Bản đọc này được xuất từ JSON payload trong cùng thư mục. Chưa đăng website.",
        "",
    ]

    for path in sorted(STORIES.glob("*.json")):
        story = json.loads(path.read_text(encoding="utf-8"))
        lines = [
            f"# {story['title']}",
            "",
            f"- Tác giả: {story['author']}",
            f"- Thể loại: {story['genre']}",
            f"- Số chương: {len(story['chapters'])}",
            "",
            "## Giới thiệu",
            "",
            html_to_md(story["intro"]),
            "",
            "## Prompt cover ChatGPT Image Generation",
            "",
            story["cover_prompt"],
            "",
        ]
        for chapter in story["chapters"]:
            lines.extend(
                [
                    f"## {chapter['title']}",
                    "",
                    html_to_md(chapter["content"]),
                    "",
                ]
            )

        md = "\n".join(lines).strip() + "\n"
        out_path = OUT / f"{path.stem}.md"
        out_path.write_text(md, encoding="utf-8")

        combined_lines.extend([f"---", "", md, ""])

    (BASE / "20_truyen_full_ban_doc.md").write_text("\n".join(combined_lines).strip() + "\n", encoding="utf-8")
    print(f"Exported {len(list(STORIES.glob('*.json')))} stories to {OUT}")
    print(f"Combined manuscript: {BASE / '20_truyen_full_ban_doc.md'}")


if __name__ == "__main__":
    main()
