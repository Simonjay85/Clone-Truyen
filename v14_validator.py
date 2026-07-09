# -*- coding: utf-8 -*-
import json
import os
import re

def validate_v14_novel(json_path):
    print(f"=== VALIDATING NOVEL AGAINST V14 STANDARD: {os.path.basename(json_path)} ===")
    
    if not os.path.exists(json_path):
        print(f"Error: File {json_path} does not exist.")
        return False
        
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            novel = json.load(f)
    except Exception as e:
        print(f"Error parsing JSON: {e}")
        return False
        
    passed = True
    
    # 1. Title verification
    title = novel.get("title", "")
    title_words = len(title.split())
    print(f"Title: \"{title}\" ({title_words} words)")
    if title_words < 12 or title_words > 22:
        print(f"[-] WARNING: Title length should ideally be 12-22 words for maximum CTR (current: {title_words}).")
        
    # 2. Intro verification
    intro = novel.get("intro", "")
    if not intro.strip().startswith("<p><strong>"):
        print("[-] FAIL: Intro should start with kịch tính block formatted as <p><strong>\"Trích dẫn...\"</strong></p>.")
        passed = False
    else:
        print("[+] PASS: Intro format conforms to V14 Gold.")
        
    # 3. Chapters count
    chapters = novel.get("chapters", [])
    print(f"Total Chapters: {len(chapters)}")
    if len(chapters) < 8 or len(chapters) > 15:
        print(f"[-] WARNING: Chapter count is {len(chapters)}, V14 standard recommends 8-15 chapters.")
        
    # 4. Detailed check for each chapter
    banned_cliches = [
        "tôi không cần cô tin tôi",
        "nếu chỉ là uất ức",
        "chúng ta đứng cùng nhau",
        "không ăn mừng, không đăng đàn",
        "sang chương",
        "cuộc chiến bước vào lớp"
    ]
    
    for idx, ch in enumerate(chapters, 1):
        ch_title = ch.get("title", "")
        ch_content = ch.get("content", "")
        
        # Word count calculation (approximate by whitespace splitting)
        # Remove HTML tags first to count actual text words
        text_only = re.sub(r"<[^>]*>", " ", ch_content)
        words = text_only.split()
        word_count = len(words)
        
        print(f"  -> Chapter {idx}: \"{ch_title}\" - {word_count} words")
        
        if word_count < 1000:
            print(f"  [-] FAIL: Chapter {idx} has {word_count} words, which is under the V14 minimum of 1000 words.")
            passed = False
        else:
            print(f"  [+] PASS: Word count is sufficient ({word_count} words).")
            
        # HTML tag check (only <p>, <strong>, <em> allowed)
        unallowed_tags = re.findall(r"<(?!(?:p|/p|strong|/strong|em|/em|hr\s*/?|br\s*/?)\b)[^>]+>", ch_content)
        if unallowed_tags:
            print(f"  [-] WARNING: Chapter {idx} contains unallowed tags: {set(unallowed_tags)}")
            
        # Meta narrative leaks
        meta_words = ["nhân vật chính", "cốt truyện", "chapter"]
        found_meta = [w for w in meta_words if w in text_only.lower()]
        if found_meta:
            print(f"  [-] WARNING: Chapter {idx} might contain meta-narrative leaks: {found_meta}")
            
        # Banned cliches check
        found_cliches = [c for c in banned_cliches if c in text_only.lower()]
        if found_cliches:
            print(f"  [-] FAIL: Chapter {idx} contains reused cliches: {found_cliches}")
            passed = False
            
    # 5. V14 Motif check (approximate detection of motif repetition)
    full_text = " ".join([re.sub(r"<[^>]*>", " ", ch.get("content", "")) for ch in chapters]).lower()
    
    # We look for recurring nouns as possible motifs (e.g. bút, đồng hồ, sổ, mùi, sương,...)
    print("V14 Elements Summary Check:")
    
    # Check for direct confrontation clues (dialogue quotes inside paragraph tags)
    dialogues = re.findall(r"<p>\"[^\"]+\"</p>", "".join([ch.get("content", "") for ch in chapters]))
    print(f"  - Dialogues found: {len(dialogues)} paragraphs. (V14 requires at least 3 deep face-to-face scenes).")
    
    if passed:
        print("[SUCCESS] Novel passes the primary V14 verification criteria.")
    else:
        print("[FAILURE] Novel has critical V14 format or content errors.")
        
    return passed

if __name__ == "__main__":
    import sys
    path = "/Users/aaronnguyen/TN/App/doctieuthuyet/pending_novel.json"
    if len(sys.argv) > 1:
        path = sys.argv[1]
    validate_v14_novel(path)
