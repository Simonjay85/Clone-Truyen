import json
import os

def main():
    path = "existing_novels.json"
    if not os.path.exists(path):
        print("existing_novels.json not found!")
        return
        
    with open(path, "r", encoding="utf-8") as f:
        novels = json.load(f)
        
    print(f"Total novels: {len(novels)}")
    for i, novel in enumerate(novels):
        nid = novel.get("id")
        title = novel.get("title")
        intro = novel.get("intro", "")
        # Remove HTML tags to get raw length
        import re
        clean_text = re.sub('<[^<]+?>', '', intro)
        word_count = len(clean_text.split())
        print(f"{i+1}. ID: {nid} | Title: {title} | Words: {word_count}")
        # Print a snippet of the intro
        print(f"   Snippet: {clean_text[:120]}...")

if __name__ == "__main__":
    main()
