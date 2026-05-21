#!/usr/bin/env python3
"""Merge 10 chapter JSON files into pending_novel.json"""
import json
import os

DRAFT_DIR = os.path.join(os.path.dirname(__file__), "novel_1_drafts")
OUTPUT_FILE = os.path.join(os.path.dirname(__file__), "..", "pending_novel.json")

novel = {
    "title": "Vua Tôm Hùm Phú Yên: Chàng Ngư Dân Bị Khinh Rẻ Thâu Tóm Vùng Biển Nghìn Tỷ",
    "author": "Hải Phong",
    "genre": "Sảng Văn",
    "intro": '<p><strong>"Ngày hôm đó, cha con chủ nhiệm Hợp tác xã tước đoạt toàn bộ lồng tôm hùm gia truyền của tôi, đẩy người cha già bám biển ngã chấn thương cột sống nằm liệt giường. Họ bảo kẻ nghèo rách mồng tơi như tôi không có quyền cắm một cây cọc xuống bãi biển Phú Yên."</strong></p>\n<p>Nhưng họ không biết rằng, đôi bàn tay từng bị đạp xuống bùn này lại nắm giữ chìa khóa công nghệ tảo đỏ sinh học đột phá và thế hệ tôm hùm giáp vàng F3 kháng bệnh duy nhất trên thế giới.</p>\n<p>Khi dịch bệnh sữa bùng phát quét sạch hàng nghìn ô lồng thủy sản, khi cha con kẻ địch điên cuồng ép giá thu mua xuống mức rác rưởi một trăm năm mươi ngàn đồng một kg, Trần Hải Phong sẽ bắt đầu cuộc phản kích tàn khốc.</p>\n<p>Kết nối trực tiếp hợp đồng xuất khẩu chính ngạch nghìn tỷ sang Singapore, đối đầu trực diện với những thế lực thương lái độc quyền bỉ ổi, Trần Hải Phong sẽ vả mặt từng kẻ đã khinh rẻ anh và bước lên ngôi vị Vua Tôm Hùm Phú Yên tối cao!</p>',
    "cover_prompt": "A highly photorealistic cinematic movie poster featuring a handsome young Vietnamese fisherman with wind-blown hair and sun-kissed skin standing on a modern high-tech polymer lobster cage in Phu Yen. In his hands, he proudly holds a huge, glowing golden-armored lobster (Vua Tom Hum) that shines like gold under a dramatic ocean sunset. Behind him, the breathtaking coastal view of Vung Ro bay and Deo Ca mountains is bathed in a majestic golden hour light. Premium quality, 8k resolution, cinematic lighting, dramatic masterpiece.",
    "chapters": []
}

for i in range(1, 11):
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
