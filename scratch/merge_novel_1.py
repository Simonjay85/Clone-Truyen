#!/usr/bin/env python3
"""Merge 7 chapter JSON files into pending_novel.json"""
import json
import os

DRAFT_DIR = os.path.join(os.path.dirname(__file__), "novel_1_drafts")
OUTPUT_FILE = os.path.join(os.path.dirname(__file__), "..", "pending_novel.json")

novel = {
    "title": "Chàng Rể Bếp Trưởng Ẩn Thế",
    "author": "Hải Đăng",
    "genre": "Sảng Văn",
    "intro": '<p><strong>"Ngày đó, sư phụ cướp trắng công thức gia truyền ba đời, đạp tôi ra khỏi nhà hàng năm sao giữa Sài Gòn. Mẹ vợ khinh tôi là thằng rửa bát vô dụng, anh rể nhổ nước bọt vào mặt tôi trước mặt cả nhà."</strong></p><p>Nhưng họ không biết, đôi bàn tay từng chế biến cho nguyên thủ quốc gia này sẽ khiến cả Phú Quốc phải quỳ gối. Khi đại tiệc Michelin dành cho đoàn ngoại giao quốc tế sắp diễn ra, khi kẻ thù dùng đủ thủ đoạn bẩn thỉu từ gài nợ, đầu độc đến cướp hợp đồng — Đặng Quốc Bảo sẽ dùng chính tài năng ẩm thực thiên bẩm để vả mặt từng kẻ đã khinh thường mình!</p><p>Một bộ truyện sảng văn đô thị cực cuốn với những màn lật kèo ngoạn mục trong thế giới ẩm thực cao cấp Việt Nam!</p>',
    "cover_prompt": "A highly detailed, professional anime-style book cover, a handsome Vietnamese chef in white uniform holding a gleaming knife standing in a luxury ocean-view restaurant kitchen in Phu Quoc, golden sunset through windows, vivid colors, premium web novel art",
    "chapters": []
}

for i in range(1, 8):
    filepath = os.path.join(DRAFT_DIR, f"chap{i}.json")
    with open(filepath, "r", encoding="utf-8") as f:
        chapter = json.load(f)
    novel["chapters"].append(chapter)
    word_count = len(chapter["content"].replace("<p>", " ").replace("</p>", " ").split())
    print(f"  Chapter {i}: {chapter['title']} — ~{word_count} words")

output_path = os.path.abspath(OUTPUT_FILE)
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(novel, f, ensure_ascii=False, indent=2)

print(f"\nMerged {len(novel['chapters'])} chapters into {output_path}")
print(f"Novel: {novel['title']} by {novel['author']}")
