import json
import os
import glob
import re

def count_words(text):
    clean_text = re.sub(r'<[^>]+>', ' ', text)
    words = clean_text.split()
    return len(words)

print("="*60)
print("🧐 VERIFYING BATCH 3 DRAFTS (Novel 14 to 18)")
print("="*60)

for idx in [14, 15, 16, 17, 18]:
    path = f"scratch/draft_novel_{idx}.json"
    if not os.path.exists(path):
        print(f"➖ File not found (still writing): {path}")
        continue
        
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            
        print(f"\n📖 [Novel ID {idx}]")
        print(f"   Title: {data.get('title')}")
        print(f"   Subtitle: {data.get('subtitle')}")
        print(f"   Author: {data.get('author')}")
        print(f"   Genre: {data.get('genre')}")
        print(f"   Cover Prompt: {data.get('cover_prompt')[:80]}...")
        
        chaps = data.get("chapters", [])
        print(f"   Chapters Count: {len(chaps)}")
        
        all_passed = True
        errors = []
        
        for i, chap in enumerate(chaps):
            c_title = chap.get("title", "")
            content = chap.get("content", "")
            words = count_words(content)
            paragraphs = content.count("<p>")
            
            print(f"      Chapter {i+1}: '{c_title}' -> {words} words, {paragraphs} paragraphs")
            
            if words < 1000:
                all_passed = False
                errors.append(f"Chapter {i+1} has only {words} words (minimum 1000 required).")
                
            content_stripped = content.strip()
            if not content_stripped.startswith("<p>"):
                all_passed = False
                errors.append(f"Chapter {i+1} content does not start with '<p>'.")
            if not content_stripped.endswith("</p>"):
                all_passed = False
                errors.append(f"Chapter {i+1} content does not end with '</p>'.")
                
        if all_passed:
            print("   ✅ V12 Compliance: PASSED!")
        else:
            print("   ❌ V12 Compliance: FAILED!")
            for err in errors:
                print(f"      - {err}")
                
    except Exception as e:
        print(f"❌ Error parsing {path}: {e}")

print("\n"+"="*60)
