import os
import json
import requests
import ftplib
import sys

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"
WP_URL = "https://doctieuthuyet.com"
SECRET_TOKEN = "ZEN_TRUYEN_2026_BYPASS"

def upload_helper():
    print("📤 Uploading wp_update_story_v13.php to FTP root...")
    try:
        ftp = ftplib.FTP(FTP_HOST, timeout=30)
        ftp.login(FTP_USER, FTP_PASS)
        local_file = "/Users/aaronnguyen/TN/App/doctieuthuyet/scratch/wp_update_story_v13.php"
        with open(local_file, "rb") as f:
            ftp.storbinary("STOR wp_update_story_v13.php", f)
        print("✓ Uploaded wp_update_story_v13.php successfully.")
        ftp.quit()
        return True
    except Exception as e:
        print(f"❌ FTP Upload Error: {e}")
        return False

def delete_helper():
    print("🧹 Deleting wp_update_story_v13.php from FTP root...")
    try:
        ftp = ftplib.FTP(FTP_HOST, timeout=30)
        ftp.login(FTP_USER, FTP_PASS)
        ftp.delete("wp_update_story_v13.php")
        print("✓ Deleted wp_update_story_v13.php successfully.")
        ftp.quit()
        return True
    except Exception as e:
        print(f"⚠️ FTP Deletion Warning: {e}")
        return False

def deploy_story(story_id):
    json_path = f"/Users/aaronnguyen/TN/App/doctieuthuyet/scratch/rewrite_{story_id}_v13.json"
    if not os.path.exists(json_path):
        print(f"❌ Local JSON not found for ID {story_id} at: {json_path}")
        return False
        
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            story_data = json.load(f)
        print(f"✓ Loaded rewrite data for: '{story_data['title']}' (ID: {story_id})")
    except Exception as e:
        print(f"❌ Error reading JSON for ID {story_id}: {e}")
        return False

    # 1. Upload helper
    if not upload_helper():
        print("❌ Cannot proceed without FTP upload helper.")
        return False

    # 2. Trigger via POST request
    print(f"🚀 Deploying story ID {story_id} to WordPress...")
    payload = {
        "secret_token": SECRET_TOKEN,
        "story_id": int(story_id),
        "intro": story_data["intro"],
        "focus_keyword": story_data["focus_keyword"],
        "seo_title": story_data["seo_title"],
        "seo_description": story_data["seo_description"],
        "chapters": story_data["chapters"]
    }

    success = False
    try:
        res = requests.post(f"{WP_URL}/wp_update_story_v13.php", json=payload, timeout=120)
        print(f"HTTP Status: {res.status_code}")
        
        # Check if JSON
        try:
            res_data = res.json()
            if res.status_code == 200 and res_data.get("success"):
                print("=" * 60)
                print(f"🎉 SUCCESS DEPLOYING STORY '{res_data['title']}' (ID: {res_data['story_id']})")
                print(f"✓ Deleted chapters count: {res_data['deleted_chapters_count']}")
                print(f"✓ Inserted chapters count: {res_data['inserted_chapters_count']}")
                print(f"✓ SEO Title: {res_data['seo']['seo_title']}")
                print(f"✓ SEO Description: {res_data['seo']['seo_description']}")
                print(f"✓ SEO Focus Keyword: {res_data['seo']['focus_keyword']}")
                print("=" * 60)
                success = True
            else:
                print(f"❌ Server side error: {res_data.get('error')}")
        except ValueError:
            print(f"❌ Response is not valid JSON. Excerpt:\n{res.text[:1000]}")
            
    except Exception as e:
        print(f"❌ HTTP Request Error: {e}")

    # 3. Always clean up helper
    delete_helper()
    
    return success

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 deploy_v13_manager.py <story_id>")
        sys.exit(1)
    
    sid = sys.argv[1]
    ok = deploy_story(sid)
    if ok:
        sys.exit(0)
    else:
        sys.exit(1)
