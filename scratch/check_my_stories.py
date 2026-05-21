#!/usr/bin/env python3
import sys
import os
import json

# Add current directory to path to import novel_editor
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import novel_editor

stories = [1927, 1933, 1948, 2227]

print("Uploading helper...")
novel_editor.upload_helper()

try:
    for sid in stories:
        print(f"\n--- Story {sid} ---")
        try:
            res = novel_editor.get_story_chapters(sid)
            if res.get("success"):
                chapters = res.get("chapters", [])
                print(f"Success! Found {len(chapters)} chapters.")
                for ch in chapters[:3]:
                    print(f"  Chap {ch['id']}: {ch['title']} ({ch['word_count']} words)")
                if len(chapters) > 3:
                    print(f"  ... and {len(chapters) - 3} more.")
            else:
                print(f"Error: {res.get('error')}")
        except Exception as e:
            print(f"Exception for {sid}: {e}")
finally:
    print("\nRemoving helper...")
    novel_editor.remove_helper()
