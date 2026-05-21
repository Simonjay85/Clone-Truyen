#!/usr/bin/env python3
"""Merge novel_2 chapter drafts into pending_novel.json for Bát Tràng novel"""
import json
import os
import re

DRAFT_DIR = "/Users/aaronnguyen/TN/App/doctieuthuyet/scratch/novel_2_drafts"
OUTPUT_FILE = "/Users/aaronnguyen/TN/App/doctieuthuyet/pending_novel.json"

novel = {
    "title": "Đế Chế Gốm Sứ Bát Tràng: Nghệ Nhân Bị Phản Bội Thiêu Đốt Cả Làng Nghề",
    "author": "Nguyễn Quang Minh",
    "genre": "Sảng Văn",
    "intro": '<p><strong>"Trần Thế Hải, đứa học trò ruột tôi cưu mang năm năm, ăn cắp công thức men ngọc rạn ngũ đại gia truyền, liên doanh với tập đoàn gốm sứ hóa chất ngoại bang mở nhà xưởng hiện đại ngay đối diện xưởng tôi. Hắn dùng truyền thông bẩn bôi nhọ tôi đầu độc khách hàng bằng men chì, niêm phong lò củi gia truyền dòng họ..."</strong></p>\n<p>Nhưng hắn và lũ gian thương ngoại bang không bao giờ biết được rằng, men ngọc đích thực đòi hỏi nhiệt độ biến thiên tinh tế của lửa củi nhãn, chứ không phải thứ men frit chì bóng lộn công nghiệp rẻ tiền. Được sự bảo trợ của Phạm Thu Hương - nữ giám đốc trẻ trung đầy quyền lực của Sở Công Thương, Nguyễn Quang Minh đã bảo vệ lò củi cổ kính vượt qua đêm giông bão phá hoại, mang kiệt tác độc bản chấn động Triển lãm Quốc tế, giăng cái bẫy pháp lý hoàn hảo đưa kẻ phản bội và lũ buôn lậu vào tù, vực dậy đế chế gốm sứ Bát Tràng di sản nghìn tỷ!</p>\n<p>Truyện sảng văn vả mặt cực đỉnh, thương chiến đấu trí làng nghề Bát Tràng kịch tính tột cùng!</p>',
    "cover_prompt": "Vietnamese ceramic artisan crafting a beautiful jade-glazed vase, elegant businesswoman examining pottery, traditional kiln fire glowing, Bat Trang village",
    "chapters": []
}

# Load chapters 1 to 9 in order
for i in range(1, 10):
    filepath = os.path.join(DRAFT_DIR, f"chap{i}.json")
    with open(filepath, "r", encoding="utf-8") as f:
        chapter = json.load(f)
    novel["chapters"].append(chapter)
    
    # Count words (Vietnamese: split by spaces)
    text = re.sub(r'<[^>]+>', '', chapter["content"])
    words = len(text.split())
    chars = len(text)
    print(f"  {chapter['title']}: {words} words, {chars} chars")

# Write output to pending_novel.json
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(novel, f, ensure_ascii=False, indent=2)

print(f"\nMerged {len(novel['chapters'])} chapters into {OUTPUT_FILE}")
print("Done!")
