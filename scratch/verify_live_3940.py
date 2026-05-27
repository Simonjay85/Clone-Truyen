#!/usr/bin/env python3
import json
import os
import sys

sys.path.append("/Users/aaronnguyen/TN/App/doctieuthuyet/scratch")
import novel_editor

def verify():
    print("Uploading helper to production...")
    novel_editor.upload_helper()
    
    try:
        print("Fetching current live chapters for Story ID 3940...")
        res = novel_editor.get_story_chapters(3940)
        if not res.get("success"):
            print(f"❌ Failed to fetch: {res.get('error')}")
            return
            
        chapters = res.get("chapters", [])
        print(f"Found {len(chapters)} live chapters.")
        
        # Verify Chapter 1 (index 0)
        ch1 = chapters[0]
        print(f"\n[Verification] Chapter 1: {ch1['title']} (ID: {ch1['id']})")
        
        # Check name replacements
        if "Nguyễn Lâm Phong" in ch1['content']:
            print("❌ Error: 'Nguyễn Lâm Phong' still exists in live Chapter 1 content!")
        else:
            print("✅ Success: 'Nguyễn Lâm Phong' was successfully removed from live Chapter 1.")
            
        if "Vũ Hoài Lâm" in ch1['content']:
            print("✅ Success: 'Vũ Hoài Lâm' exists in live Chapter 1.")
        else:
            print("❌ Error: 'Vũ Hoài Lâm' is missing from live Chapter 1!")
            
        # Check clichés
        if "nảy lên mấy vòng rồi nằm im lìm trong góc tối" in ch1['content']:
            print("❌ Error: Old ring cliché still exists in live Chapter 1!")
        else:
            print("✅ Success: Old ring cliché was successfully purged from live Chapter 1.")
            
        if "bẻ gãy thẻ hành nghề" in ch1['content']:
            print("❌ Error: Old license bẻ gãy cliché still exists in live Chapter 1!")
        else:
            print("✅ Success: Old license bẻ gãy cliché was successfully purged.")

        # Print Chapter 1 excerpt for visual verification
        clean_text = ch1['content'].replace("<p>", "").replace("</p>", "\n")
        print("\n=== Live Chapter 1 Snippet (Polished Dialogues) ===")
        print(clean_text[400:1500])
        
        # Verify Chapter 8 (index 7)
        if len(chapters) >= 8:
            ch8 = chapters[7]
            print(f"\n[Verification] Chapter 8: {ch8['title']} (ID: {ch8['id']})")
            if "Nguyễn Lâm Phong" in ch8['content']:
                print("❌ Error: 'Nguyễn Lâm Phong' still exists in live Chapter 8!")
            else:
                print("✅ Success: 'Nguyễn Lâm Phong' successfully renamed to 'Vũ Hoài Lâm' in Chapter 8 too.")
                
    finally:
        print("\nCleaning up helper...")
        novel_editor.remove_helper()
        print("Verification complete.")

if __name__ == "__main__":
    verify()
