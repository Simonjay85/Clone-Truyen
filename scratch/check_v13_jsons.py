import json
import os

scratch_dir = "/Users/aaronnguyen/TN/App/doctieuthuyet/scratch"
ids = [2745, 2752, 2759, 2766, 2773]

for truyen_id in ids:
    path = os.path.join(scratch_dir, f"rewrite_{truyen_id}_v13.json")
    if not os.path.exists(path):
        print(f"[MISSING] {truyen_id}")
        continue
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        chapters = data.get("chapters", [])
        print(f"[ID:{truyen_id}] Focus: {data.get('focus_keyword')}, Title: {data.get('seo_title')}, Chaps: {len(chapters)}")
        for idx, c in enumerate(chapters):
            content = c.get("content", "")
            word_count = len(content.split())
            print(f"  Chap {idx+1}: {c.get('title')} ({word_count} words)")
    except Exception as e:
        print(f"[ERROR] {truyen_id}: {e}")
