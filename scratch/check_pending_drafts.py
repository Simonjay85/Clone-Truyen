import json
import os

files = [
    "pending_novel_2.json",
    "pending_novel_3.json",
    "pending_novel_4.json",
    "pending_novel_5.json"
]

for file in files:
    if os.path.exists(file):
        try:
            with open(file, "r", encoding="utf-8") as f:
                data = json.load(f)
            print(f"File: {file}")
            print(f"  Title: {data.get('title')}")
            print(f"  Author: {data.get('author')}")
            print(f"  Genre: {data.get('genre')}")
            print(f"  Cover Prompt: {data.get('cover_prompt')[:60]}...")
            print(f"  Intro Length: {len(data.get('intro'))} chars")
            chapters = data.get('chapters', [])
            print(f"  Chapters Count: {len(chapters)}")
            for idx, chap in enumerate(chapters):
                content = chap.get('content', '')
                p_count = content.count("<p>")
                words = len(content.split())
                print(f"    Chap {idx+1}: {chap.get('title')} ({words} words, {p_count} paragraphs)")
        except Exception as e:
            print(f"Error reading {file}: {e}")
    else:
        print(f"File {file} does not exist!")
