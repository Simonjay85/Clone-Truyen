#!/usr/bin/env python3
"""Merge 8 chapter JSON files into pending_novel_4.json"""
import json
import os
import re

DRAFT_DIR = os.path.join(os.path.dirname(__file__), "novel_4_drafts")
OUTPUT = os.path.join(os.path.dirname(os.path.dirname(__file__)), "pending_novel_4.json")

novel = {
    "title": "Võ Thần Bảo Vệ Đại Tiểu Thư",
    "author": "Thiên Vũ",
    "genre": "Sảng Văn",
    "intro": '<p><strong>"Họ thuê tôi làm bảo vệ với mức lương 8 triệu một tháng. Đại tiểu thư nhìn tôi như nhìn một con chó giữ cửa và bảo: \'Anh chỉ cần đứng im và đừng làm phiền tôi là được.\'"</strong></p>\n<p>Nhưng cô ấy không biết, đôi tay này từng hạ gục cả một trung đội lính đánh thuê ở biên giới. Và khi bóng tối của đường dây buôn lậu 500 tỷ tại cảng Đình Vũ bao phủ lên gia đình cô, chính đôi tay ấy sẽ là thứ duy nhất bảo vệ được cô!</p>\n<p>Một bộ truyện hành động sảng văn đỉnh cao, nơi cựu đặc nhiệm ẩn thân làm bảo vệ lật tung cả đế chế buôn lậu Hải Phòng!</p>',
    "cover_prompt": "A highly detailed, professional anime-style book cover, a muscular Vietnamese man in tactical black clothing standing protectively beside an elegant young woman at a massive cargo port at night, container ships and cranes in background, dramatic blue-red lighting, premium web novel art",
    "chapters": []
}

total_words = 0
for i in range(1, 9):
    path = os.path.join(DRAFT_DIR, f"chap{i}.json")
    with open(path, "r", encoding="utf-8") as f:
        chapter = json.load(f)
    novel["chapters"].append(chapter)
    
    # Count Vietnamese words (split by whitespace)
    text = re.sub(r'<[^>]+>', '', chapter["content"])
    words = len(text.split())
    chars = len(text)
    print(f"  Chương {i}: {words} words, {chars} chars — {chapter['title']}")
    total_words += words

print(f"\n  TOTAL: {total_words} words across 8 chapters")
print(f"  Average: {total_words // 8} words per chapter")

with open(OUTPUT, "w", encoding="utf-8") as f:
    json.dump(novel, f, ensure_ascii=False, indent=2)

print(f"\n  Output: {OUTPUT}")
print("  Done!")
