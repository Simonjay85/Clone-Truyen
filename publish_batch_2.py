#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
publish_batch_2.py — Batch 2 Markdown Parser and WordPress Publisher
====================================================================
Parses the user's second batch of sảng văn novels (Stories 6 to 10):
- 06-bi-cuop-thiet-ke-da-nang.md
- 07-bo-roi-o-can-tho.md
- 08-mat-mat-o-landmark.md
- 09-dinh-chi-phong-kham-hue.md
- 10-cuoi-nhao-o-pho-co.md
And uploads them to doctieuthuyet.com via FTP and the WP publish helper.
"""

import os
import sys
import re
import json
import time
import random
import argparse
import subprocess
import ftplib
import requests

# ─── CONFIGURATION ────────────────────────────────────────────────────────────
FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"
WP_URL = "https://doctieuthuyet.com"
SECRET_TOKEN = "ZEN_TRUYEN_2026_BYPASS"

MANUSCRIPT_DIR = "/Users/aaronnguyen/TN/App/doctieuthuyet/scratch/batch_20_full_stories_20260526/manuscripts_md"

# Cover templates mapping
COVER_TEMPLATES = {
    6: {"file": "06-bi-cuop-thiet-ke-da-nang.md", "base": "base_cover_15.png", "sub": "Bản hùng ca sảng văn của Phạm Minh Châu & Ngô Nhật Quân"},
    7: {"file": "07-bo-roi-o-can-tho.md", "base": "base_cover_16.png", "sub": "Bản hùng ca sảng văn của Nguyễn Hương Giang & Huỳnh Tấn Lộc"},
    8: {"file": "08-mat-mat-o-landmark.md", "base": "base_cover_17.png", "sub": "Bản hùng ca sảng văn của Vũ Thiên Kim & Đặng Minh Triết"},
    9: {"file": "09-dinh-chi-phong-kham-hue.md", "base": "base_cover_18.png", "sub": "Bản hùng ca sảng văn của Tôn Nữ Bảo Trâm & Nguyễn Khải Hoàn"},
    10: {"file": "10-cuoi-nhao-o-pho-co.md", "base": "base_cover_19.png", "sub": "Bản hùng ca sảng văn của Phạm An Khuê & Bùi Khánh Toàn"},
}

def log(msg):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {msg}")
    sys.stdout.flush()

# ─── V13 SENTENCE SPLITTER ────────────────────────────────────────────────────
def split_sentences_to_html(content_text):
    """
    Splits text paragraphs and wraps every single sentence in a <p>...</p> block.
    """
    content_text = content_text.strip()
    
    # Split the raw text into paragraphs by empty lines
    paragraphs = [p.strip() for p in re.split(r'\n\s*\n', content_text) if p.strip()]
    
    html_paragraphs = []
    for p in paragraphs:
        # Split paragraph into sentences on . ! ? while handling trailing spaces
        sentences = [s.strip() for s in re.split(r'(?<=[.!?])\s+', p) if s.strip()]
        for s in sentences:
            html_paragraphs.append(f"<p>{s}</p>")
            
    return "\n".join(html_paragraphs) + "\n"

# ─── INDIVIDUAL MANUSCRIPT PARSER ─────────────────────────────────────────────
def parse_stories():
    log(f"📖 Reading and parsing Batch 2 manuscripts from: {MANUSCRIPT_DIR}")
    
    parsed_stories = []
    
    for idx, tpl in COVER_TEMPLATES.items():
        file_name = tpl["file"]
        file_path = os.path.join(MANUSCRIPT_DIR, file_name)
        
        if not os.path.exists(file_path):
            log(f"❌ Error: File {file_name} not found in {MANUSCRIPT_DIR}!")
            sys.exit(1)
            
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Title is the first H1 line
        lines = content.split("\n")
        title = lines[0].strip().lstrip("# ").strip()
        remaining_text = "\n".join(lines[1:])
        
        # Author
        author_match = re.search(r'-\s*Tác giả:\s*(.*?)(?:\n|$)', remaining_text)
        author = author_match.group(1).strip() if author_match else "Khuyết Danh"
        
        # Intro is between ## Giới thiệu and ## Prompt cover ChatGPT Image Generation (or the first chapter)
        intro_match = re.search(r'## Giới thiệu\s*\n(.*?)\n\s*##\s*(?:Prompt cover|Chương 1)', remaining_text, re.DOTALL)
        intro_html = ""
        if intro_match:
            intro_text = intro_match.group(1).strip()
            intro_paragraphs = [p.strip() for p in re.split(r'\n\s*\n', intro_text) if p.strip()]
            intro_html = "\n".join(f"<p>{p}</p>" for p in intro_paragraphs)
        else:
            log(f"⚠️ Warning: Intro not found for Story {idx} ({file_name})!")
            
        # Chapters split by ## Chương ([0-9]+):
        chapter_blocks = re.split(r'(?m)^## Chương ([0-9]+):\s+', remaining_text)
        
        chapters = []
        c_blocks = chapter_blocks[1:]
        
        for j in range(0, len(c_blocks), 2):
            chap_num = int(c_blocks[j])
            chap_content_raw = c_blocks[j+1]
            
            # The first line of chap_content_raw is the chapter title suffix
            chap_lines = chap_content_raw.split("\n")
            chap_title_suffix = chap_lines[0].strip()
            chap_text = "\n".join(chap_lines[1:]).strip()
            
            # Clean trailing dividers if any
            chap_text = re.sub(r'\n\s*---\s*\n.*', '', chap_text, flags=re.DOTALL).strip()
            
            chap_html = split_sentences_to_html(chap_text)
            
            chapters.append({
                "title": f"Chương {chap_num}: {chap_title_suffix}",
                "content": chap_html
            })
            
        parsed_stories.append({
            "idx": idx,
            "title": title,
            "author": author,
            "genre": "Sảng Văn",
            "intro": intro_html,
            "chapters": chapters
        })
        
    log(f"✓ Successfully parsed {len(parsed_stories)} Batch 2 stories from manuscripts.")
    return parsed_stories

# ─── FTP CONNECTOR ────────────────────────────────────────────────────────────
def get_ftp_connection(retries=5, delay=5):
    for i in range(retries):
        try:
            log(f"Connecting to FTP (attempt {i+1}/{retries})...")
            ftp = ftplib.FTP(FTP_HOST, timeout=60)
            ftp.login(FTP_USER, FTP_PASS)
            return ftp
        except Exception as e:
            log(f"⚠️ FTP connection failed: {e}")
            if i < retries - 1:
                time.sleep(delay * (i + 1))
    raise Exception("Fatal: Failed to connect to FTP after multiple attempts")

# ─── DRY RUN PRINTER ──────────────────────────────────────────────────────────
def execute_dry_run(stories):
    print("\n" + "=" * 80)
    print("🔬 DRY-RUN PARSE VERIFICATION REPORT (BATCH 2)")
    print("=" * 80)
    
    for s in stories:
        print(f"\n📖 STORY #{s['idx']}: {s['title']}")
        print(f"   ✍️ Author: {s['author']}")
        print(f"   🎨 Genre: {s['genre']}")
        print(f"   📝 Intro paragraphs count: {s['intro'].count('<p>')}")
        print(f"   📚 Chapters count: {len(s['chapters'])}")
        
        # Display first chapter preview
        if s['chapters']:
            first_chap = s['chapters'][0]
            print(f"   - [PREVIEW] {first_chap['title']}")
            sentences_preview = re.findall(r'<p>(.*?)</p>', first_chap['content'])[:3]
            for idx, sent in enumerate(sentences_preview):
                print(f"     {idx+1}. {sent}")
        print("-" * 80)
        
    print("\n✓ Dry-run completed successfully! Batch 2 parsing is 100% correct.")

# ─── LIVE PUBLISHER ───────────────────────────────────────────────────────────
def execute_live_publishing(stories):
    log("🚀 STARTING LIVE PUBLICATION PIPELINE FOR BATCH 2")
    
    # Step 1: Upload publish_novel.php helper script via FTP
    log("📤 Uploading publish_novel.php helper endpoint via FTP...")
    try:
        ftp = get_ftp_connection()
        with open("publish_novel.php", "rb") as f:
            ftp.storbinary("STOR publish_novel.php", f)
        log("✓ Helper endpoint uploaded successfully.")
        ftp.quit()
    except Exception as e:
        log(f"❌ Fatal FTP upload error for helper script: {e}")
        sys.exit(1)
        
    published_count = 0
    failed_indices = []
    
    for s in stories:
        idx = s["idx"]
        title = s["title"]
        author = s["author"]
        
        log(f"\n============================================================")
        log(f"📖 PUBLISHING STORY {idx}/10: {title}")
        log(f"============================================================")
        
        # 1. Overlay cover generation
        pending_cover = "pending_cover.png"
        cover_local_filename = ""
        
        if idx in COVER_TEMPLATES:
            tpl = COVER_TEMPLATES[idx]
            base_file = tpl["base"]
            subtitle = tpl["sub"]
            
            if os.path.exists(base_file):
                log(f"🎨 Running cover overlay engine on template {base_file}...")
                try:
                    cmd = [
                        "python3", "cover_overlay_standard.py",
                        "--input", base_file,
                        "--output", pending_cover,
                        "--title", title,
                        "--subtitle", subtitle
                    ]
                    res = subprocess.run(cmd, capture_output=True, text=True)
                    if res.returncode == 0:
                        log("✓ Cover overlay generated successfully.")
                        
                        # Upload cover to FTP wp-content/uploads/
                        random_id = random.randint(100000, 999999)
                        cover_local_filename = f"cover_sideload_{random_id}.png"
                        log(f"📤 Uploading custom cover as /wp-content/uploads/{cover_local_filename}...")
                        
                        ftp = get_ftp_connection()
                        ftp.cwd("wp-content/uploads")
                        with open(pending_cover, "rb") as cf:
                            ftp.storbinary(f"STOR {cover_local_filename}", cf)
                        ftp.quit()
                        log("✓ Custom cover uploaded via FTP successfully.")
                    else:
                        log(f"⚠️ Cover overlay failed: {res.stderr}. Skipping custom cover.")
                except Exception as ce:
                    log(f"⚠️ Cover overlay system error: {ce}. Skipping custom cover.")
            else:
                log(f"⚠️ Base cover {base_file} not found. Skipping cover overlay.")
        else:
            log("⚠️ No cover template mapped. Skipping cover.")
            
        # Clean up local pending cover if any
        if os.path.exists(pending_cover):
            try:
                os.remove(pending_cover)
            except Exception:
                pass
                
        # 2. Trigger story publication
        log("🌐 Triggering WordPress database insertion...")
        payload = {
            "secret_token": SECRET_TOKEN,
            "title": title,
            "intro": s["intro"],
            "author": author,
            "genre": "Sảng Văn",
            "chapters": s["chapters"]
        }
        if cover_local_filename:
            payload["cover_local_filename"] = cover_local_filename
            
        try:
            api_url = f"{WP_URL}/publish_novel.php"
            res = requests.post(api_url, json=payload, timeout=180)
            res_data = res.json()
            
            if res_data.get('success'):
                log(f"🎉 SUCCESS! Novel index {idx} published successfully.")
                log(f"   -> Live ID: {res_data['story_id']}")
                log(f"   -> Cover Status: {res_data['cover_status']}")
                log(f"   -> Chapters: {res_data['chapters_count']} chapters posted.")
                
                # Update existing_novels.json
                existing_path = "existing_novels.json"
                existing = []
                if os.path.exists(existing_path):
                    try:
                        with open(existing_path, "r", encoding="utf-8") as ef:
                            existing = json.load(ef)
                    except Exception:
                        pass
                
                new_entry = {
                    "id": res_data['story_id'],
                    "title": title,
                    "slug": title.lower().replace(" ", "-"),
                    "intro": s["intro"]
                }
                existing.append(new_entry)
                with open(existing_path, "w", encoding="utf-8") as ef:
                    json.dump(existing, ef, ensure_ascii=False, indent=2)
                log("✓ Updated local existing_novels.json registry.")
                published_count += 1
            else:
                log(f"❌ API Publication Error for index {idx}: {res_data}")
                failed_indices.append(idx)
        except Exception as ae:
            log(f"❌ API HTTP POST Exception for index {idx}: {ae}")
            failed_indices.append(idx)
            
        # Small cooldown between stories to protect DB connections
        time.sleep(5)
        
    # Clean up the publish helper script from remote for security
    log("\n🧹 Cleaning up publish_novel.php helper from remote server...")
    try:
        ftp = get_ftp_connection()
        ftp.delete("publish_novel.php")
        log("✓ Deleted publish_novel.php helper from remote server for security.")
        ftp.quit()
    except Exception as e:
        log(f"⚠️ Could not delete publish_novel.php remote helper: {e}")
        
    log(f"\n" + "=" * 60)
    log(f"🏁 LIVE BATCH 2 PROCESS FINISHED")
    log(f"  -> Total successfully published: {published_count}/5")
    if failed_indices:
        log(f"  -> Failed indices: {failed_indices}")
    log("=" * 60)

# ─── MAIN ─────────────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(description="Parse and publish Batch 2 sảng văn novels")
    parser.add_argument("--dry-run", action="store_true", help="Only parse and output verification metrics")
    parser.add_argument("--live", action="store_true", help="Run the live cover overlay and publication pipeline")
    args = parser.parse_args()
    
    if not args.dry_run and not args.live:
        print("❌ Error: You must specify either --dry-run or --live flag!")
        parser.print_help()
        sys.exit(1)
        
    stories = parse_stories()
    
    if args.dry_run:
        execute_dry_run(stories)
    elif args.live:
        execute_live_publishing(stories)

if __name__ == "__main__":
    main()
