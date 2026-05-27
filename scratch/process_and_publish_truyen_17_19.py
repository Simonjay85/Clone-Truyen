#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import re
import json
import subprocess
import shutil

sys.path.append("/Users/aaronnguyen/TN/App/doctieuthuyet")
from scratch.apply_text_overlay import add_title_to_cover

SOURCE_FILE = "/Users/aaronnguyen/Downloads/batch_04_rewrite_v2_truyen_17_19_full.md"
WORKSPACE_DIR = "/Users/aaronnguyen/TN/App/doctieuthuyet"

def clean_paragraph_into_sentences(text):
    text = text.strip()
    if not text:
        return ""
    # Normalise quotes
    text = text.replace('“', '“').replace('”', '”')
    text = text.replace('...', '___ELLIPSIS___')
    text = text.replace('…', '___ELLIPSIS___')
    
    # Split on . ! ? that are not preceded by a digit and are followed by space or end of line
    # Taking into account potential closing quotes: ([.!?])([”"”]?)(?=\s|$)
    pattern = r'(?<!\d)([.!?])([”"”]?)(?=\s|$)'
    marked = re.sub(pattern, r'\1\2___BOUNDARY___', text)
    
    marked = marked.replace('___ELLIPSIS___', '...')
    
    parts = marked.split('___BOUNDARY___')
    html_paragraphs = []
    for part in parts:
        s = part.strip()
        if s:
            html_paragraphs.append(f"<p>{s}</p>")
    
    return "\n".join(html_paragraphs)

def run_overlay_and_publish(story_num):
    print("=" * 70)
    print(f"🎬 PROCESSING AND PUBLISHING TRUYỆN {story_num}")
    print("=" * 70)
    
    # 1. Parse the source markdown file
    if not os.path.exists(SOURCE_FILE):
        print(f"❌ Error: Source file not found: {SOURCE_FILE}")
        return False
        
    with open(SOURCE_FILE, "r", encoding="utf-8") as f:
        content = f.read()
        
    parts = re.split(r'# TRUYỆN (\d+)', content)
    stories = {}
    for i in range(1, len(parts), 2):
        num = int(parts[i])
        text = parts[i+1]
        stories[num] = text
        
    if story_num not in stories:
        print(f"❌ Error: Story {story_num} not found in source file!")
        return False
        
    story_text = stories[story_num]
    
    # Extract Title
    title_match = re.search(r'^#\s*(.+)$', story_text, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else "Unknown Title"
    
    # Extract Author
    author_match = re.search(r'-\s*Tác giả:\s*(.+)$', story_text, re.MULTILINE)
    author = author_match.group(1).strip() if author_match else "Unknown Author"
    
    print(f"📖 Story Title: {title}")
    print(f"✍️ Author: {author}")
    
    # Extract Intro
    intro_start = story_text.find("## Giới thiệu")
    ch1_start = story_text.find("## Chương 1")
    
    if intro_start != -1 and ch1_start != -1:
        intro_text = story_text[intro_start + len("## Giới thiệu"):ch1_start].strip()
        intro_paragraphs = [p.strip() for p in intro_text.split("\n\n") if p.strip()]
        # Formatted with premium paragraph wraps
        intro_html = "\n".join([f"<p>{p}</p>" for p in intro_paragraphs])
    else:
        intro_html = "<p>Đang cập nhật</p>"
        
    # Extract and parse Chapters
    chap_headers = re.findall(r'^##\s*(Chương \d+:\s*(.+))$', story_text, re.MULTILINE)
    split_pattern = r'^##\s*Chương \d+:.*$'
    chap_contents = re.split(split_pattern, story_text, flags=re.MULTILINE)
    
    chapters_payload = []
    for idx, header_info in enumerate(chap_headers):
        full_header, chap_title = header_info
        chap_content_raw = chap_contents[idx + 1].strip()
        
        # Trim extra content for Truyen 19 Chapter 10
        if story_num == 19 and idx == 9:
            end_idx = chap_content_raw.find("---")
            if end_idx != -1:
                chap_content_raw = chap_content_raw[:end_idx].strip()
                
        # Split into one-sentence-per-paragraph tags
        paragraphs = [p.strip() for p in chap_content_raw.split("\n\n") if p.strip()]
        formatted_paragraphs = []
        for p in paragraphs:
            formatted_p = clean_paragraph_into_sentences(p)
            if formatted_p:
                formatted_paragraphs.append(formatted_p)
                
        final_content = "\n".join(formatted_paragraphs)
        chapters_payload.append({
            "title": full_header.strip(),
            "content": final_content
        })
        
    print(f"✓ Parsed {len(chapters_payload)} chapters successfully.")
    
    # 2. Cover Art Generation & Text Overlay
    pending_cover = os.path.join(WORKSPACE_DIR, "pending_cover.png")
    
    if story_num == 17:
        # Music theme
        base_cover = os.path.join(WORKSPACE_DIR, "scratch/base_3813.png")
        title_lines = "Bị Thay Thế Trước Đêm Diễn\nTôi Mở File Master Khiến Cả Nhà Hát Đứng Im"
        subtitle = "Tác giả: Lạc Nhiên | Thể loại: Sảng Văn"
        accent_rgb = (235, 172, 35) # Gold
    elif story_num == 19:
        # Logistics theme
        base_cover = os.path.join(WORKSPACE_DIR, "scratch/base_3767.png")
        title_lines = "Bị Gạch Tên Khỏi Hội Nghị Sữa\nTôi Mở Log Nhiệt Độ Khiến Tập Đoàn Xin Mua Lại Chuỗi Lạnh"
        subtitle = "Tác giả: Kiều Anh | Thể loại: Sảng Văn"
        accent_rgb = (0, 180, 216) # Cool Cyan
    else:
        print("❌ Unknown story index!")
        return False
        
    print(f"🎨 Running text overlay on {os.path.basename(base_cover)}...")
    if not os.path.exists(base_cover):
        print(f"❌ Error: Base cover not found at {base_cover}!")
        return False
        
    success_cover = add_title_to_cover(
        input_path=base_cover,
        output_path=pending_cover,
        title=title_lines,
        subtitle=subtitle,
        color_accent_rgb=accent_rgb
    )
    
    if not success_cover or not os.path.exists(pending_cover):
        print("❌ Cover overlay failed!")
        return False
        
    # 3. Create pending_novel.json payload
    novel_data = {
        "title": title,
        "author": author,
        "genre": "Sảng Văn",
        "intro": intro_html,
        "chapters": chapters_payload
    }
    
    pending_json = os.path.join(WORKSPACE_DIR, "pending_novel.json")
    with open(pending_json, "w", encoding="utf-8") as f:
        json.dump(novel_data, f, ensure_ascii=False, indent=2)
    print("✓ Created pending_novel.json payload.")
    
    # 4. Trigger publishing script
    print("🚀 Triggering WordPress publish script...")
    publish_script = os.path.join(WORKSPACE_DIR, "publish_local_novel.py")
    
    result = subprocess.run(
        ["python3", publish_script],
        cwd=WORKSPACE_DIR,
        capture_output=True,
        text=True
    )
    
    print("--- PUBLISHER OUTPUT ---")
    print(result.stdout)
    if result.stderr:
        print("--- ERROR LOG ---")
        print(result.stderr)
    print("------------------------")
    
    # Verify success from output
    if "🎉 NOVEL PUBLISHED SUCCESSFULLY TO THE LIVE WEBSITE!" in result.stdout:
        print(f"🎉 SUCCESS: Truyện {story_num} has been successfully published!")
        return True
    else:
        print(f"❌ FAILURE: Publishing script failed for Truyện {story_num}!")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 process_and_publish_truyen_17_19.py <17|19>")
        sys.exit(1)
        
    story = int(sys.argv[1])
    ok = run_overlay_and_publish(story)
    if not ok:
        sys.exit(1)
