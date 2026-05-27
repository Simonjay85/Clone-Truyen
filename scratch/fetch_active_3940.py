#!/usr/bin/env python3
import json
import os
import sys

sys.path.append("/Users/aaronnguyen/TN/App/doctieuthuyet/scratch")
import novel_editor

def fetch():
    print("Uploading helper to production...")
    novel_editor.upload_helper()
    
    try:
        print("Fetching all live chapters for Story ID 3940...")
        res = novel_editor.get_story_chapters(3940)
        if not res.get("success"):
            print(f"❌ Error: {res.get('error')}")
            return
            
        chapters = res.get("chapters", [])
        print(f"Found {len(chapters)} live chapters.")
        
        # Save to local file
        out_path = "/Users/aaronnguyen/TN/App/doctieuthuyet/scratch/active_story_3940_dump.json"
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(res, f, ensure_ascii=False, indent=4)
        print(f"✓ Saved live chapters to {out_path}")
        
    finally:
        print("Cleaning up...")
        novel_editor.remove_helper()

if __name__ == "__main__":
    fetch()
