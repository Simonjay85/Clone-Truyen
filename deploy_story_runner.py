import os
import json
import requests
import ftplib
import sys

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"
WP_URL = "https://doctieuthuyet.com"

def deploy(story_id, json_filepath):
    print("=" * 60)
    print(f"🚀 DEPLOYING STORY ID {story_id} VIA FTP + PHP HELPER ENGINE")
    print("=" * 60)
    
    if not os.path.exists(json_filepath):
        print(f"❌ Error: {json_filepath} not found!")
        return False
        
    try:
        with open(json_filepath, "r", encoding="utf-8") as f:
            novel_data = json.load(f)
        print(f"✓ Loaded story draft: {novel_data['title']} by {novel_data['author']}")
    except Exception as e:
        print("❌ Error parsing JSON:", e)
        return False

    # 1. Upload helper script via FTP
    print("\n📤 Uploading overwrite_story_v13.php endpoint to FTP root...")
    try:
        ftp = ftplib.FTP(FTP_HOST, timeout=30)
        ftp.login(FTP_USER, FTP_PASS)
        
        with open("/Users/aaronnguyen/TN/App/doctieuthuyet/overwrite_story_v13.php", "rb") as f:
            ftp.storbinary("STOR overwrite_story_v13.php", f)
        print("✓ Uploaded overwrite_story_v13.php to server.")
        ftp.quit()
    except Exception as e:
        print("❌ FTP Upload Error for helper script:", e)
        return False
        
    # 2. Trigger story publication/overwrite via HTTP call
    print("\n🔌 Triggering novel publication to doctieuthuyet.com database...")
    
    # Chuẩn bị payload
    payload = {
        "secret_token": "ZEN_TRUYEN_2026_BYPASS",
        "story_id": int(story_id),
        "title": novel_data['title'],
        "intro": novel_data['intro'],
        "author": novel_data['author'],
        "seo": novel_data.get('seo', {}),
        "chapters": novel_data['chapters']
    }
    
    try:
        api_url = f"{WP_URL}/overwrite_story_v13.php"
        res = requests.post(api_url, json=payload, timeout=180) # timeout lớn đề phòng việc xử lý 8 chương lâu
        
        # In kết quả raw trước nếu lỗi
        if res.status_code != 200:
            print(f"❌ Server returned non-200 code: {res.status_code}")
            print(res.text[:1000])
            success = False
        else:
            try:
                res_data = res.json()
                if res_data.get('success'):
                    print("=" * 60)
                    print("🎉 NOVEL DEPLOYED SUCCESSFULLY TO THE LIVE WEBSITE!")
                    print(f"ID: {res_data['story_id']}")
                    print(f"Title: {res_data['title']}")
                    print(f"Author: {res_data['author']}")
                    print(f"Deleted Old Chapters: {res_data['deleted_old_chapters']}")
                    print(f"Chapters Published: {res_data['chapters_count']}")
                    print(f"SEO Updated: {res_data['seo_updated']}")
                    print("=" * 60)
                    success = True
                else:
                    print("❌ Failed to publish novel via API response:", res_data)
                    success = False
            except Exception as parse_err:
                print("❌ Failed to parse response JSON:", parse_err)
                print(res.text[:2000])
                success = False
                
    except Exception as e:
        print("❌ API Call Error during publication:", e)
        success = False
        
    # 3. Clean up the publish helper script from remote for security
    print("\n🗑️ Cleaning up remote helper script...")
    try:
        ftp = ftplib.FTP(FTP_HOST, timeout=30)
        ftp.login(FTP_USER, FTP_PASS)
        ftp.delete("overwrite_story_v13.php")
        print("✓ Deleted overwrite_story_v13.php from remote server.")
        ftp.quit()
    except Exception as clean_err:
        print("⚠️ Warning: Could not delete remote helper script:", clean_err)
        
    return success

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 deploy_story_runner.py <story_id> <json_filepath>")
    else:
        deploy(sys.argv[1], sys.argv[2])
