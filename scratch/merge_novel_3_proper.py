#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Properly merge all 12 chapters of "Thiên Tài Cầu Đường Cao Tốc" into pending_novel.json.
Validates word count (>= 1000 per chapter) and sentence-by-sentence paragraphing tags <p>...</p>\\n.
"""

import json
import os
import re

DRAFT_DIR = "/Users/aaronnguyen/TN/App/doctieuthuyet/scratch/novel_3_drafts"
OUTPUT = "/Users/aaronnguyen/TN/App/doctieuthuyet/pending_novel.json"

def parse_chapter_file(path):
    with open(path, "r", encoding="utf-8") as f:
        raw = f.read()
    
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        pass
    
    # Extract title
    title_match = re.search(r'"title"\s*:\s*"((?:[^"\\]|\\.)*)"', raw)
    title = title_match.group(1) if title_match else "Unknown"
    
    # Extract content
    content_start_pattern = '"content": "'
    start_idx = raw.find(content_start_pattern)
    if start_idx == -1:
        content_start_pattern = '"content":"'
        start_idx = raw.find(content_start_pattern)
    
    start_idx += len(content_start_pattern)
    end_pattern = raw.rfind('"\n}')
    if end_pattern == -1:
        end_pattern = raw.rfind('"}')
        
    content_raw = raw[start_idx:end_pattern]
    
    # Escape internal quotes
    content_escaped = content_raw.replace('\\"', '\x00ESCAPED_QUOTE\x00')
    content_escaped = content_escaped.replace('"', '\\"')
    content_escaped = content_escaped.replace('\x00ESCAPED_QUOTE\x00', '\\"')
    
    fixed_json = '{"title": "' + title + '", "content": "' + content_escaped + '"}'
    try:
        return json.loads(fixed_json)
    except json.JSONDecodeError as e:
        print(f"  Failed parsing {path}: {e}")
        return {"title": title, "content": content_raw}

def main():
    print("=" * 60)
    print("🛠️ MERGING NOVEL 3: THIÊN TÀI CẦU ĐƯỜNG CAO TỐC")
    print("=" * 60)
    
    novel = {
        "title": "Thiên Tài Cầu Đường Cao Tốc: Kỹ Sư Bị Sa Thải Xây Cầu Vượt Biển Nghìn Tỷ",
        "author": "Hoàng Đức Trung",
        "genre": "Sảng Văn",
        "intro": '<p><strong>"Nhân viên kỹ thuật quèn của Viện Thiết Kế Cầu Đường thì không được phép phản biện dự án sai kỹ thuật sao? Lê Khắc Nam cướp trắng bản quyền thiết kế của tôi, đẩy tôi ra khỏi Viện trong ngày giông bão Hải Phòng và lớn tiếng: \'Mày chỉ là thằng kỹ sư quèn, đòi cãi lý với chuyên gia!\'"</strong></p><p>Trớ trêu thay, chính hắn không biết bản thiết kế hoàn hảo mà hắn cướp được chứa một lỗi cấu trúc trụ cầu chết người mà tôi đã cố ý cài vào để vạch mặt hắn. Khi hắn tự mãn mang thiết kế lỗi ấy đi đấu thầu dự án thế kỷ Tân Vũ - Lạch Huyện, đó cũng là lúc tôi thành lập tổng công ty cầu đường riêng, giật lại dự án siêu khủng này.</p><p>Hành trình khẳng định vị thế của một thiên tài cầu đường đích thực, đối đầu trực diện với những kẻ ăn bớt chất lượng xây dựng bằng sự trung thực, tri thức chuyên môn và những nhịp cầu thép nối liền hai miền biển cả Việt Nam!</p>',
        "cover_prompt": "A highly detailed cinematic movie poster background of a handsome, rugged young Vietnamese highway and bridge engineer holding blue blueprints in a modern high-tech office, giant modern sea-crossing bridge construction under dramatic orange sunset clouds, cinematic lighting, photorealistic, NO text, NO words",
        "chapters": []
    }
    
    total_words = 0
    validation_passed = True
    
    for i in range(1, 13):
        path = os.path.join(DRAFT_DIR, f"chap{i}.json")
        if not os.path.exists(path):
            print(f"❌ Error: Chapter {i} file not found at {path}!")
            validation_passed = False
            continue
            
        chap = parse_chapter_file(path)
        content = chap["content"]
        
        # Word count validation (strip HTML tags first)
        plain_text = re.sub(r'<[^>]+>', ' ', content)
        # normalize spaces
        plain_text = re.sub(r'\s+', ' ', plain_text).strip()
        words = len(plain_text.split())
        total_words += words
        
        # Sentence-by-sentence paragraph check:
        # Every <p> should contain roughly one sentence. No huge multi-sentence blocks.
        paragraphs = re.findall(r'<p>(.*?)</p>', content, re.DOTALL)
        bad_paragraphs = []
        for idx, p in enumerate(paragraphs):
            # Check if paragraph has multiple sentence terminals (e.g. ".", "?", "!") not followed by abbreviations
            # A simple heuristic: count sentences
            sentences = re.split(r'(?<=[.!?])\s+', p.strip())
            # filter out empty elements
            sentences = [s for s in sentences if s.strip()]
            if len(sentences) > 1:
                # Some abbreviations like "TP.", "NXB.", "Co." might trigger false positives, but let's log it
                # If there are many sentences in one paragraph, it's a block.
                if len(sentences) >= 3 or (len(sentences) == 2 and len(p) > 200):
                    bad_paragraphs.append((idx + 1, p[:80] + "..."))
        
        status_str = "✓"
        if words < 1000:
            status_str = "❌"
            validation_passed = False
            print(f"{status_str} Chương {i:02d}: {words:5d} từ (DƯỚI 1000 TỪ!) — {chap['title']}")
        else:
            print(f"{status_str} Chương {i:02d}: {words:5d} từ — {chap['title']}")
            
        if bad_paragraphs:
            print(f"  ⚠️ Cảnh báo V12: Phát hiện {len(bad_paragraphs)} đoạn văn có thể chứa nhiều câu (block). Ví dụ:")
            for p_num, p_snippet in bad_paragraphs[:2]:
                print(f"    - Đoạn {p_num}: {p_snippet}")
                
        novel["chapters"].append({
            "title": chap["title"],
            "content": content
        })
        
    print("-" * 60)
    print(f"Tổng số từ: {total_words} từ")
    print(f"Số lượng chương: {len(novel['chapters'])}")
    
    if validation_passed:
        with open(OUTPUT, "w", encoding="utf-8") as f:
            json.dump(novel, f, ensure_ascii=False, indent=2)
        print(f"🎉 MERGE SUCCESSFUL! pending_novel.json written to: {OUTPUT}")
    else:
        print("❌ MERGE FAILED due to validation errors. Please check the issues above.")

if __name__ == "__main__":
    main()
