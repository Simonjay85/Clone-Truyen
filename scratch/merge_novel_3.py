#!/usr/bin/env python3
"""Merge 10 chapter JSON files into pending_novel_3.json - fixes unescaped quotes"""
import json
import os
import re

DRAFT_DIR = os.path.join(os.path.dirname(__file__), "novel_3_drafts")
OUTPUT = os.path.join(os.path.dirname(os.path.dirname(__file__)), "pending_novel_3.json")

def parse_chapter_file(path):
    """Parse chapter JSON even if content has unescaped double quotes."""
    with open(path, "r", encoding="utf-8") as f:
        raw = f.read()
    
    # Try standard parsing first
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        pass
    
    # Extract title - it's always clean
    title_match = re.search(r'"title"\s*:\s*"((?:[^"\\]|\\.)*)"', raw)
    title = title_match.group(1) if title_match else "Unknown"
    
    # Extract content: find the opening and closing quotes of the content field
    # Pattern: "content": "....."   where the last " before \n} is the closing one
    content_start_pattern = '"content": "'
    start_idx = raw.find(content_start_pattern)
    if start_idx == -1:
        content_start_pattern = '"content":"'
        start_idx = raw.find(content_start_pattern)
    
    start_idx += len(content_start_pattern)
    
    # The closing quote is the last " before the final }
    # Find the last occurrence of "\n}" or "}"
    end_pattern = raw.rfind('"\n}')
    if end_pattern == -1:
        end_pattern = raw.rfind('"}')
    
    content_raw = raw[start_idx:end_pattern]
    
    # Escape any unescaped double quotes in the content
    # (quotes that are not preceded by backslash and not part of HTML tags)
    # Actually, just properly escape all internal double quotes
    content_escaped = content_raw.replace('\\"', '\x00ESCAPED_QUOTE\x00')  # save already escaped
    content_escaped = content_escaped.replace('"', '\\"')  # escape all remaining
    content_escaped = content_escaped.replace('\x00ESCAPED_QUOTE\x00', '\\"')  # restore
    
    # Now parse the fixed JSON
    fixed_json = '{"title": "' + title + '", "content": "' + content_escaped + '"}'
    try:
        return json.loads(fixed_json)
    except json.JSONDecodeError as e:
        print(f"  Still can't parse {path}: {e}")
        # Last resort: return with raw content
        return {"title": title, "content": content_raw}


novel = {
    "title": "Chiến Thần Dược Phẩm Độc Bản",
    "author": "Trung Kiên",
    "genre": "Sảng Văn",
    "intro": "<p><strong>\"Năm năm nghiên cứu trong phòng lab lạnh giá Đà Lạt, tôi tìm ra công thức thuốc gan đột phá dùng kỹ thuật khóa phân tử độc nhất vô nhị. Thế nhưng sếp cũ cướp trắng thành quả, đạp tôi ra khỏi cửa lab dưới cơn mưa rừng thông và cười khẩy: 'Mày chỉ là thằng nghiên cứu sinh quèn!'\"</strong></p><p>Nhưng hắn không biết, công thức mà hắn cướp được có một lỗi khóa phân tử chết người mà chỉ tôi mới nắm giữ chìa khóa. Khi hắn mang công thức lỗi lên sàn HoSE để IPO, chính là lúc tôi sẽ khiến đế chế dược phẩm nghìn tỷ của hắn sụp đổ tan tành!</p><p>Một cuộc chiến trí tuệ đỉnh cao trong thế giới dược phẩm Việt Nam, nơi khoa học, pháp luật và thương trường đan xen tạo nên những cú lật kèo ngoạn mục nhất!</p>",
    "cover_prompt": "A highly detailed, professional anime-style book cover, a determined Vietnamese scientist in a white lab coat holding a glowing molecular formula in a modern pharmaceutical laboratory in Da Lat highlands, misty pine forest visible through windows, dramatic blue-green lighting, premium web novel art",
    "chapters": []
}

total_words = 0
for i in range(1, 11):
    path = os.path.join(DRAFT_DIR, f"chap{i}.json")
    chap = parse_chapter_file(path)
    
    # Count Vietnamese words
    text = re.sub(r'<[^>]+>', '', chap["content"])
    words = len(text.split())
    total_words += words
    print(f"  Chương {i}: {words} words — {chap['title']}")
    
    novel["chapters"].append({
        "title": chap["title"],
        "content": chap["content"]
    })

with open(OUTPUT, "w", encoding="utf-8") as f:
    json.dump(novel, f, ensure_ascii=False, indent=2)

print(f"\nTotal: {total_words} words across {len(novel['chapters'])} chapters")
print(f"Output: {OUTPUT}")

# Verify
with open(OUTPUT, "r", encoding="utf-8") as f:
    verify = json.load(f)
print(f"Verification: {len(verify['chapters'])} chapters loaded OK")
print("Done!")
