#!/usr/bin/env python3
import sys
import os

# Add scratch to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import novel_editor

stories = [2129, 2137, 2145, 2156, 2165]

print("Checking Group I stories deployment status...")
novel_editor.upload_helper()

try:
    for sid in stories:
        print(f"\n--- Story {sid} ---")
        try:
            res = novel_editor.get_story_chapters(sid)
            if res.get("success"):
                chapters = res.get("chapters", [])
                print(f"Success! Found {len(chapters)} chapters.")
                for ch in chapters:
                    print(f"  Chap {ch['id']}: {ch['title']} ({ch['word_count']} words)")
            else:
                print(f"Error: {res.get('error')}")
        except Exception as e:
            print(f"Exception for {sid}: {e}")
finally:
    print("\nRemoving helper...")
    novel_editor.remove_helper()
