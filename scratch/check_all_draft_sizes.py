import os
import json
import re

def count_words(html_content):
    clean = re.sub(r'<[^>]+>', ' ', html_content)
    words = clean.strip().split()
    return len(words)

def main():
    folder = "scratch/novel_1_drafts"
    print("Checking draft sizes in", folder)
    if not os.path.exists(folder):
        print("Folder not found.")
        return
        
    for i in range(1, 11):
        path = os.path.join(folder, f"chap{i}.json")
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
                words = count_words(data["content"])
                print(f"Chapter {i}: {data['title']} -> {words} words ({len(data['content'])} chars)")
        else:
            print(f"Chapter {i} not found.")

if __name__ == "__main__":
    main()
