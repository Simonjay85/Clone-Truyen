#!/usr/bin/env python3
import json
import os
import sys

sys.path.append("/Users/aaronnguyen/TN/App/doctieuthuyet/scratch")
import novel_editor

def inspect():
    print("Uploading helper...")
    novel_editor.upload_helper()
    
    try:
        print("Fetching all chapters for Story ID 3940...")
        res = novel_editor.get_story_chapters(3940)
        if not res.get("success"):
            print(f"Error: {res.get('error')}")
            return
            
        chapters = res.get("chapters", [])
        print(f"\nTotal live chapters found: {len(chapters)}")
        for idx, ch in enumerate(chapters, 1):
            print(f"[{idx}] ID: {ch['id']} | Title: {ch['title']} | Word Count: {ch['word_count']}")
            # print a small excerpt
            clean_text = ch['content'][:150].replace("\n", " ").strip()
            print(f"    Excerpt: {clean_text}...")
            
    finally:
        print("\nCleaning up...")
        novel_editor.remove_helper()

if __name__ == "__main__":
    inspect()
