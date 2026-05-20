#!/usr/bin/env python3
"""Merge novel_2 chapter drafts into pending_novel_2.json"""
import json
import os
import re

DRAFT_DIR = "/Users/aaronnguyen/TN/App/doctieuthuyet/scratch/novel_2_drafts"
OUTPUT_FILE = "/Users/aaronnguyen/TN/App/doctieuthuyet/pending_novel_2.json"

novel = {
    "title": "Người Thừa Kế Trăm Tỷ Giả Nghèo",
    "author": "Minh Quang",
    "genre": "Sảng Văn",
    "intro": "<p><strong>\"Tôi đi xe ôm đến ra mắt gia đình người yêu. Mẹ cô ấy nhìn tôi từ đầu đến chân rồi nhổ nước bọt: 'Thằng ăn mày này cũng dám đòi cưới con gái tôi? Sính lễ 5 tỷ, có thì nói, không có thì cút!'\"></strong></p>\n<p>Nhưng bà ta không biết, chiếc xe ôm tôi đi là vì tôi thích thế. Căn penthouse trên tầng cao nhất Landmark 81 đứng tên tôi. Quỹ ủy thác nghìn tỷ đồng tôi làm chủ tịch. Và khi đám cưới tổ chức tại đại sảnh Phú Mỹ Hưng với sự chứng kiến của toàn bộ giới tài phiệt Sài Gòn — tôi muốn xem mặt bà ta lúc đó sẽ ra sao!</p>\n<p>Truyện sảng văn vả mặt đỉnh cao: Người thừa kế trăm tỷ giả nghèo đi thử lòng, kẻ khinh thường sẽ phải quỳ gối!</p>",
    "cover_prompt": "A highly detailed, professional anime-style book cover, a confident young Vietnamese man in casual streetwear standing before the illuminated Landmark 81 skyscraper at night in Ho Chi Minh City, city lights reflecting, dramatic contrast between his humble appearance and the luxury backdrop, vivid colors, premium web novel art",
    "chapters": []
}

# Load chapters in order
for i in range(1, 7):
    filepath = os.path.join(DRAFT_DIR, f"chap{i}.json")
    with open(filepath, "r", encoding="utf-8") as f:
        chapter = json.load(f)
    novel["chapters"].append(chapter)
    
    # Count words (Vietnamese: split by spaces)
    text = re.sub(r'<[^>]+>', '', chapter["content"])
    words = len(text.split())
    chars = len(text)
    print(f"  {chapter['title']}: {words} words, {chars} chars")

# Write output
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(novel, f, ensure_ascii=False, indent=2)

print(f"\nMerged {len(novel['chapters'])} chapters into {OUTPUT_FILE}")
print("Done!")
