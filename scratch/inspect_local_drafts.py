import json
import glob
import os

print("Inspecting local pending_novel_*.json files:")
files = sorted(glob.glob("pending_novel_*.json"))
for path in files:
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            chaps = data.get("chapters", [])
            print(f"\nFile: {path}")
            print(f"Title: {data.get('title')}")
            print(f"Author: {data.get('author')}")
            print(f"Genre: {data.get('genre')}")
            print(f"Intro length: {len(data.get('intro', ''))} chars")
            print(f"Number of chapters: {len(chaps)}")
            for i, c in enumerate(chaps):
                content = c.get("content", "")
                words = len(content.split())
                paragraphs = content.count("<p>")
                print(f"  Chapter {i+1}: '{c.get('title')}' -> {words} words, {paragraphs} paragraphs")
    except Exception as e:
        print(f"Error reading {path}: {e}")
