import os
import json
import time
import requests
import sys
from ftplib import FTP

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"
WP_URL = "https://doctieuthuyet.com"

def deploy_story_from_json(json_path):
    print(f"📖 Starting deployment from local JSON: {json_path}")
    if not os.path.exists(json_path):
        print(f"❌ JSON file does not exist: {json_path}")
        return False
        
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            story_json = json.load(f)
    except Exception as e:
        print(f"❌ Failed to load/parse JSON file: {e}")
        return False
        
    story_id = story_json.get("story_id")
    title = story_json.get("title")
    intro = story_json.get("intro")
    chapters = story_json.get("chapters")
    seo = story_json.get("seo")
    
    if not story_id or not title or not intro or not chapters:
        print(f"❌ Story JSON is missing required fields (story_id, title, intro, chapters)")
        return False
        
    print(f"✓ Story loaded: ID={story_id}, Title='{title}'")
    print(f"✓ Total chapters: {len(chapters)}")
    
    # 1. Connect FTP and upload update_story.php
    print("Connecting to FTP (timeout=30)...")
    try:
        ftp = FTP(FTP_HOST, timeout=30)
        ftp.login(FTP_USER, FTP_PASS)
        print("✓ Connected to FTP. Uploading update_story.php...")
        
        # Read the update_story.php helper
        helper_path = "/Users/aaronnguyen/TN/App/doctieuthuyet/scratch/update_story.php"
        with open(helper_path, "rb") as f:
            ftp.storbinary("STOR update_story.php", f)
        print("✓ update_story.php uploaded successfully.")
        ftp.quit()
    except Exception as e:
        print(f"❌ FTP upload error: {e}")
        return False
        
    # 2. Call the deploy API
    print("Gửi request POST tới WordPress để cập nhật truyện (timeout=90)...")
    payload = {
        "secret_token": "ZEN_TRUYEN_2026_BYPASS",
        "story_id": story_id,
        "title": title,
        "intro": intro,
        "chapters": chapters,
        "seo": seo
    }
    
    deploy_success = False
    try:
        api_url = f"{WP_URL}/update_story.php"
        res = requests.post(api_url, json=payload, timeout=90)
        print(f"WordPress Response Status: {res.status_code}")
        
        try:
            res_data = res.json()
            if res_data.get("success"):
                print(f"🎉 SUCCESS: Published Story ID {story_id} to live website!")
                print(f"   Deleted Chapters: {res_data.get('deleted_chapters_count')}")
                print(f"   New Chapters: {res_data.get('chapters_count')}")
                deploy_success = True
            else:
                print(f"❌ WordPress API error: {res_data}")
        except Exception as e:
            print(f"❌ WordPress returned invalid JSON: {res.text[:500]}")
    except Exception as e:
        print(f"❌ API connection or execution failed: {e}")
        
    # 3. Always clean up FTP
    print("Reconnecting to FTP to clean up update_story.php...")
    try:
        ftp = FTP(FTP_HOST, timeout=30)
        ftp.login(FTP_USER, FTP_PASS)
        ftp.delete("update_story.php")
        print("✓ Successfully deleted update_story.php from server.")
        ftp.quit()
    except Exception as e:
        print(f"⚠️ Clean up FTP helper error: {e}")
        
    return deploy_success

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 deploy_v13_story.py <path_to_json_file>")
        sys.exit(1)
    path = sys.argv[1]
    success = deploy_story_from_json(path)
    if success:
        print("🚀 DEPLOYMENT COMPLETED WITH SUCCESS!")
        sys.exit(0)
    else:
        print("❌ DEPLOYMENT FAILED.")
        sys.exit(1)
