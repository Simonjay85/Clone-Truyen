#!/usr/bin/env python3
import sys
import os
import json

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import novel_editor

target_ids = [2197, 2207, 2259, 2269, 2279, 2289, 2217, 2238, 2249, 2190]

print("Uploading helper...")
novel_editor.upload_helper()

results = {}
try:
    for sid in target_ids:
        print(f"\nFetching Story ID {sid}...")
        try:
            # Let's get chapters
            res = novel_editor.get_story_chapters(sid)
            if res.get("success"):
                chapters = res.get("chapters", [])
                print(f"Success! Story ID {sid} has {len(chapters)} chapters.")
                results[sid] = {
                    "success": True,
                    "chapters_count": len(chapters),
                    "chapters": [{"id": c["id"], "title": c["title"], "word_count": c["word_count"]} for c in chapters]
                }
            else:
                print(f"Error for Story ID {sid}: {res.get('error')}")
                results[sid] = {"success": False, "error": res.get("error")}
        except Exception as e:
            print(f"Exception for Story ID {sid}: {e}")
            results[sid] = {"success": False, "error": str(e)}
finally:
    print("\nRemoving helper...")
    novel_editor.remove_helper()

with open("story_inspection.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print("\nResults written to story_inspection.json")
