# -*- coding: utf-8 -*-
import json
import os

FINAL_PATH = "/Users/aaronnguyen/TN/App/doctieuthuyet/pending_novel_11.json"

def validate():
    if not os.path.exists(FINAL_PATH):
        print("Error: Final file does not exist!")
        return
    
    with open(FINAL_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    print("Checking keys...")
    required_keys = ["idx", "title", "author", "genre", "intro", "chapters"]
    for key in required_keys:
        if key not in data:
            print(f"Error: Missing key '{key}'")
            return
        
    print(f"Index: {data['idx']}")
    print(f"Title: {data['title']}")
    print(f"Author: {data['author']}")
    print(f"Genre: {data['genre']}")
    
    print("\nChecking Intro V13 format...")
    intro = data["intro"]
    if not intro.startswith("<p><strong>"):
        print("Warning: Intro does not start with <p><strong>")
    
    paragraphs = intro.split("\n")
    print(f"Intro paragraph count: {len(paragraphs)}")
    for p in paragraphs:
        if not (p.startswith("<p>") and p.endswith("</p>")):
            print(f"Warning: Intro paragraph formatting incorrect: {p}")
            
    print("\nChecking Chapters (Must be exactly 10)...")
    chapters = data["chapters"]
    print(f"Total chapters: {len(chapters)}")
    if len(chapters) != 10:
        print("Error: Must be exactly 10 chapters!")
        return
        
    for i, ch in enumerate(chapters, 1):
        print(f"\nChapter {i}: {ch['title']}")
        content = ch["content"]
        ch_paragraphs = content.split("\n")
        print(f"  Paragraph count: {len(ch_paragraphs)}")
        
        # Word count calculation (Vietnamese approximation by splitting spaces)
        words_count = 0
        for p in ch_paragraphs:
            if not (p.startswith("<p>") and p.endswith("</p>")):
                print(f"  Error: Paragraph not wrapped in <p>...</p>: {p[:50]}")
                return
            # Remove html tags for counting words
            clean_p = p.replace("<p>", "").replace("</p>", "")
            words_count += len(clean_p.split())
        
        print(f"  Approximate word count: {words_count}")
        if words_count < 1000 or words_count > 1500:
            print(f"  Warning: Word count is {words_count}, expected between 1000 and 1500!")
            
    print("\nValidation completed successfully!")

if __name__ == "__main__":
    validate()
