import json
import os

DRAFT_DIR = os.path.join(os.path.dirname(__file__), "novel_5_drafts")
OUTPUT_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "pending_novel_5.json")

novel = {
    "title": "Thiên Tài Khởi Nghiệp Fintech",
    "author": "Gia Bảo",
    "genre": "Sảng Văn",
    "intro": "<p><strong>\"Tôi viết từng dòng code đầu tiên cho PayViet ngay tại căn phòng trọ 15 mét vuông trên phố Duy Tân. Ba năm sau, khi app có 2 triệu người dùng và vừa gọi được Series A, thằng bạn đồng sáng lập dùng luật sư dilute cổ phần của tôi xuống 0.5% rồi đuổi thẳng cổ.\"</strong></p>\n<p>Nhưng hắn không biết, blockchain không bao giờ nói dối. Mọi dòng code gốc đều có timestamp bất biến chứng minh tôi là tác giả duy nhất. Và khi hắn mang sản phẩm ăn cắp đi gọi vốn Series B, chính là lúc tôi sẽ khiến đế chế fintech của hắn sụp đổ như domino!</p>\n<p>Một bộ truyện sảng văn công nghệ đỉnh cao, nơi thiên tài blockchain dùng chính vũ khí mà kẻ thù không hiểu nổi để lật kèo ngoạn mục nhất giới startup Việt Nam!</p>",
    "cover_prompt": "A highly detailed, professional anime-style book cover, a young Vietnamese tech genius in a hoodie and glasses standing before floating holographic blockchain data visualizations in a modern Hanoi office at night, neon blue and purple lighting, Lotte Center visible through windows, premium web novel art",
    "chapters": []
}

total_words = 0
for i in range(1, 10):
    filepath = os.path.join(DRAFT_DIR, f"chap{i}.json")
    with open(filepath, "r", encoding="utf-8") as f:
        chapter = json.load(f)
    novel["chapters"].append(chapter)
    
    # Count words (Vietnamese: split by spaces)
    content = chapter["content"]
    # Remove HTML tags for word counting
    import re
    clean = re.sub(r'<[^>]+>', '', content)
    words = len(clean.split())
    chars = len(clean)
    total_words += words
    print(f"  Chapter {i}: {words} words, {chars} chars - {chapter['title']}")

print(f"\nTotal: {total_words} words across {len(novel['chapters'])} chapters")

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(novel, f, ensure_ascii=False, indent=2)

print(f"\n✅ Merged novel written to: {OUTPUT_FILE}")
