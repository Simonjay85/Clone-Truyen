import os
import json
import re
import sys

def count_words(text):
    # Strip HTML tags
    clean_text = re.sub(r'<[^>]+>', ' ', text)
    return len(clean_text.split())

def verify_v12_compliance(path):
    if not os.path.exists(path):
        return False, [f"File {path} does not exist"]
    
    try:
        with open(path, "r", encoding="utf-8") as f:
            draft = json.load(f)
    except Exception as e:
        return False, [f"JSON Parse Error: {e}"]
        
    errors = []
    
    # 1. Check basic fields
    for field in ["title", "subtitle", "author", "genre", "intro", "cover_prompt", "chapters"]:
        if field not in draft:
            errors.append(f"Missing required field: '{field}'")
            
    if errors:
        return False, errors

    # 2. Check chapters length and content
    chapters = draft["chapters"]
    if len(chapters) < 5:
        errors.append(f"Expected at least 5 chapters, found only {len(chapters)}")
        
    for idx, chap in enumerate(chapters):
        c_num = idx + 1
        c_title = chap.get("title", f"Chương {c_num}")
        c_content = chap.get("content", "")
        
        # Word count check
        w_count = count_words(c_content)
        print(f"   📖 Chapter {c_num}: '{c_title}' -> {w_count} words")
        if w_count < 1000:
            errors.append(f"Chapter {c_num} ('{c_title}') has only {w_count} words. Must be >= 1000 words.")
            
        content_stripped = c_content.strip()
        if not (content_stripped.startswith("<p>") or content_stripped.startswith("<strong>") or content_stripped.startswith("<!--") or content_stripped.startswith("<hr")):
            errors.append(f"Chapter {c_num} ('{c_title}') content does not seem to start with standard HTML tags.")
            
        if not content_stripped.endswith("</p>"):
            errors.append(f"Chapter {c_num} ('{c_title}') content does not end with '</p>'.")
            
        # Count <p> tags to make sure it's structured nicely
        p_count = content_stripped.count("<p>")
        if p_count < 10:
            errors.append(f"Chapter {c_num} has only {p_count} <p> tags. Must have rich, detailed mobile paragraphs.")

    if errors:
        return False, errors
    return True, []

def main():
    print("=" * 60)
    print("🔍 Dry-Run Verifying Drafts 2, 3, 4, 5, 8...")
    print("=" * 60)
    for id_ in [2, 3, 4, 5, 8]:
        path = f"scratch/draft_novel_{id_}.json"
        print(f"\nChecking Novel ID {id_} ({path}):")
        ok, errors = verify_v12_compliance(path)
        if ok:
            print(f"✅ Novel ID {id_} is 100% COMPLIANT with V12!")
        else:
            print(f"❌ Novel ID {id_} FAILED verification:")
            for err in errors:
                print(f"   - {err}")

if __name__ == "__main__":
    main()
