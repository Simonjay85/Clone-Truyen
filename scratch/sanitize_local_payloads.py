#!/usr/bin/env python3
import json
import os
import re

def sanitize_content(content):
    if not content:
        return content
    # Protagonist renames
    content = content.replace("Nguyễn Lâm Phong", "Vũ Hoài Lâm")
    content = content.replace("Lâm Phong", "Hoài Lâm")
    
    # Safe regex case-sensitive word boundary for single "Phong" -> "Lâm"
    content = re.sub(r'\bPhong\b', 'Lâm', content)
    
    # Typo correction
    content = content.replace("Hà Ngoại", "Hà Nội")
    
    # Joint venture name
    content = content.replace("Phong An", "Lâm An")
    
    return content

def main():
    print("🧹 SANITIZING STORY 3940 LOCAL PAYLOADS...")
    
    # 1. Sanitize scratch/story_3940_deploy_ready.json
    json_path = "/Users/aaronnguyen/TN/App/doctieuthuyet/scratch/story_3940_deploy_ready.json"
    if os.path.exists(json_path):
        print(f"Loading {json_path}...")
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            
        data["title"] = sanitize_content(data["title"])
        data["intro"] = sanitize_content(data["intro"])
        
        # Sanitize SEO focus keyword, title, description
        if "seo" in data:
            data["seo"]["focus_keyword"] = sanitize_content(data["seo"]["focus_keyword"])
            data["seo"]["seo_title"] = sanitize_content(data["seo"]["seo_title"])
            data["seo"]["seo_description"] = sanitize_content(data["seo"]["seo_description"])
            
        # Sanitize Chapters
        for idx, chap in enumerate(data.get("chapters", [])):
            chap["title"] = sanitize_content(chap["title"])
            chap["content"] = sanitize_content(chap["content"])
            
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print(f"✓ Sanitized and saved {json_path}")
    else:
        print(f"❌ Warning: {json_path} not found!")

    # 2. Sanitize existing_novels.json
    registry_path = "/Users/aaronnguyen/TN/App/doctieuthuyet/existing_novels.json"
    if os.path.exists(registry_path):
        print(f"Loading {registry_path}...")
        with open(registry_path, "r", encoding="utf-8") as f:
            novels = json.load(f)
            
        updated = False
        for novel in novels:
            if novel.get("id") == 3940:
                print("Found story ID 3940 in existing_novels.json, updating registry...")
                novel["title"] = sanitize_content(novel["title"])
                novel["intro"] = sanitize_content(novel["intro"])
                updated = True
                break
                
        if updated:
            with open(registry_path, "w", encoding="utf-8") as f:
                json.dump(novels, f, indent=4, ensure_ascii=False)
            print(f"✓ Sanitized and saved {registry_path}")
        else:
            print("❌ Warning: Story ID 3940 not found in existing_novels.json!")
    else:
        print(f"❌ Warning: {registry_path} not found!")

    print("🎉 SANITIZATION COMPLETED SUCCESSFULLY!")

if __name__ == "__main__":
    main()
