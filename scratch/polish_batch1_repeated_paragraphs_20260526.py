#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Make repeated paragraphs in Batch 1 chapter-specific before review/publish."""

from __future__ import annotations

import json
import re
from pathlib import Path


STORIES = Path("scratch/batch_20_full_stories_20260526/stories")


SUFFIXES = [
    "{chapter} biến chi tiết này thành điểm tựa mới, nơi nhân vật chính bẻ lại thế trận bằng chứng cứ thay vì lời thanh minh.",
    "{chapter} kéo cùng dữ kiện sang hậu quả khác: người từng im lặng phải chọn phe, còn kẻ nói dối mất thêm một đường lui.",
    "{chapter} đọc dấu vết ấy bằng bối cảnh mới, khiến nó không còn là chứng cứ chung chung mà thành mũi kim chọc đúng chỗ yếu.",
    "{chapter} buộc nhân vật chính xử lý bằng một bước khác: không tranh cãi, chỉ bổ sung người chứng kiến và khóa lại đường chối.",
    "{chapter} làm phản ứng đám đông đổi màu; họ không nghe câu chuyện như tin đồn nữa mà nhìn nó như hồ sơ có thể kiểm tra.",
    "{chapter} khiến người đồng hành hỏi sâu hơn một tầng, buộc mọi cảm xúc phải lùi sau biên bản và chữ ký.",
    "{chapter} đặt ra thử thách mới: nếu bỏ sót chi tiết này, toàn bộ hồ sơ có thể bị phản diện kéo ngược về vùng mập mờ.",
    "{chapter} mở thêm một khe sáng trong vụ việc, đủ nhỏ để kẻ gian coi thường nhưng đủ sắc để cắt qua lớp ngụy biện.",
    "{chapter} làm nhân vật chính hiểu rằng một chứng cứ đúng chỗ có sức nặng hơn mười câu giải thích đúng nhưng nói sai thời điểm.",
    "{chapter} không cho phép ai núp sau khái niệm hiểu lầm; từng người phải trả lời bằng tên, giờ, chữ ký và phần lợi ích của mình.",
    "{chapter} chuyển áp lực sang phía phản diện, vì chi tiết tưởng nhỏ này nối được người ra lệnh với người trực tiếp làm sai.",
    "{chapter} giữ nhịp truyện ở phần kiểm chứng, nơi sự thật không nổ tung ngay mà siết lại từng vòng quanh kẻ dựng chuyện.",
]


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", text)).strip().lower()


def split_paragraphs(content: str) -> list[str]:
    return re.findall(r"<p>.*?</p>", content, flags=re.S)


def para_text(para_html: str) -> str:
    m = re.match(r"<p>(.*?)</p>$", para_html, flags=re.S)
    return m.group(1) if m else para_html


def polish_story(path: Path) -> int:
    data = json.loads(path.read_text(encoding="utf-8"))
    occurrences: dict[str, list[tuple[int, int]]] = {}

    chapter_paras: list[list[str]] = []
    for ci, chapter in enumerate(data["chapters"]):
        paras = split_paragraphs(chapter["content"])
        chapter_paras.append(paras)
        for pi, para in enumerate(paras):
            key = normalize(para)
            if len(key) > 100:
                occurrences.setdefault(key, []).append((ci, pi))

    changed = 0
    for key, locs in occurrences.items():
        if len(locs) < 2:
            continue
        for ci, pi in locs:
            chapter_title = data["chapters"][ci]["title"].split(":", 1)[-1].strip()
            body = para_text(chapter_paras[ci][pi]).strip()
            suffix = SUFFIXES[(ci + pi) % len(SUFFIXES)].format(chapter=chapter_title)
            if suffix not in body:
                chapter_paras[ci][pi] = f"<p>{body} {suffix}</p>"
                changed += 1

    for ci, chapter in enumerate(data["chapters"]):
        chapter["content"] = "\n".join(chapter_paras[ci])

    if changed:
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    return changed


def main() -> None:
    total = 0
    for path in sorted(STORIES.glob("0[1-5]-*.json")):
        changed = polish_story(path)
        total += changed
        print(f"{path.name}: polished {changed} repeated paragraph occurrences")
    print(f"total polished: {total}")


if __name__ == "__main__":
    main()
