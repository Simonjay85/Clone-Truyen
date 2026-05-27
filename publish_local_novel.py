import os
import json
import time
import random
import requests
import ftplib

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"
WP_URL = "https://doctieuthuyet.com"

def main():
    print("=" * 60)
    print("🚀 LOCAL NOVEL PUBLISHER ENGINE")
    print("=" * 60)
    
    pending_file = "pending_novel.json"
    if not os.path.exists(pending_file):
        print(f"❌ Error: {pending_file} not found!")
        return
        
    try:
        with open(pending_file, "r", encoding="utf-8") as f:
            novel_data = json.load(f)
        print(f"✓ Loaded story draft: {novel_data['title']} by {novel_data['author']}")
    except Exception as e:
        print("❌ Error parsing pending JSON:", e)
        return

    # 1. Determine Cover Image Source (local ChatGPT Image Generation output only).
    local_cover_file = "pending_cover.png"
    cover_local_filename = ""
    
    def get_ftp_connection(retries=5, delay=5):
        for i in range(retries):
            try:
                print(f"Connecting to FTP (attempt {i+1}/{retries})...")
                ftp = ftplib.FTP(FTP_HOST, timeout=60)
                ftp.login(FTP_USER, FTP_PASS)
                return ftp
            except Exception as e:
                print(f"FTP connection failed: {e}")
                if i < retries - 1:
                    time.sleep(delay * (i + 1))
        raise Exception("Failed to connect to FTP after multiple attempts")

    if os.path.exists(local_cover_file):
        print(f"✓ Found local ChatGPT cover: {local_cover_file}")
        # Generate a unique remote filename
        random_id = random.randint(100000, 999999)
        cover_local_filename = f"cover_sideload_{random_id}.png"
        
        # Upload the local cover file directly to FTP wp-content/uploads/
        print(f"📤 Uploading premium cover to FTP root /wp-content/uploads/{cover_local_filename}...")
        try:
            ftp = get_ftp_connection()
            ftp.cwd("wp-content/uploads")
            with open(local_cover_file, "rb") as f:
                ftp.storbinary(f"STOR {cover_local_filename}", f)
            print("✓ Uploaded premium cover via FTP.")
            ftp.quit()
        except Exception as e:
            print("❌ FTP Upload Error for ChatGPT cover:", e)
            cover_local_filename = ""
            
    if not cover_local_filename:
        print("⚠️ Không có pending_cover.png. Bỏ qua ảnh bìa tự động.")
        print("   Hãy tạo cover bằng ChatGPT Image Generation, lưu thành pending_cover.png, rồi chạy lại nếu cần gắn cover.")

    # 2. Upload publish_novel.php helper script via FTP
    print("\nUploading publish_novel.php endpoint to FTP root...")
    try:
        ftp = get_ftp_connection()
        
        with open("publish_novel.php", "rb") as f:
            ftp.storbinary("STOR publish_novel.php", f)
        print("✓ Uploaded publish_novel.php to server.")
        ftp.quit()
    except Exception as e:
        print("❌ FTP Upload Error for helper script:", e)
        return
        
    # 3. Trigger story publication via HTTP call to publish_novel.php
    print("\nTriggering novel publication to doctieuthuyet.com database...")
    payload = {
        "secret_token": "ZEN_TRUYEN_2026_BYPASS",
        "title": novel_data['title'],
        "intro": novel_data['intro'],
        "author": novel_data['author'],
        "genre": novel_data.get('genre', 'Sảng Văn'),
        "chapters": novel_data['chapters']
    }
    if cover_local_filename:
        payload["cover_local_filename"] = cover_local_filename
    
    try:
        api_url = f"{WP_URL}/publish_novel.php"
        res = requests.post(api_url, json=payload, timeout=120)
        res_data = res.json()
        
        if res_data.get('success'):
            print("=" * 60)
            print("🎉 NOVEL PUBLISHED SUCCESSFULLY TO THE LIVE WEBSITE!")
            print(f"ID: {res_data['story_id']}")
            print(f"Title: {res_data['title']}")
            print(f"Author: {res_data['author']}")
            print(f"Cover Status: {res_data['cover_status']}")
            print(f"Chapters Published: {res_data['chapters_count']}")
            print("=" * 60)
            
            # Clean up the publish helper script from remote for security
            try:
                ftp = get_ftp_connection()
                ftp.delete("publish_novel.php")
                print("✓ Deleted publish_novel.php helper from remote server for security.")
                ftp.quit()
            except Exception as ce:
                print("⚠️ Note: Could not delete remote publish_novel.php helper:", ce)
                pass
                
            # Update existing novels registry to prevent duplicate generation
            existing_path = "existing_novels.json"
            existing = []
            if os.path.exists(existing_path):
                try:
                    with open(existing_path, "r", encoding="utf-8") as f:
                        existing = json.load(f)
                except:
                    pass
                    
            new_novel_entry = {
                "id": res_data['story_id'],
                "title": res_data['title'],
                "slug": res_data['title'].lower().replace(" ", "-"),
                "intro": novel_data['intro']
            }
            existing.append(new_novel_entry)
            with open(existing_path, "w", encoding="utf-8") as f:
                json.dump(existing, f, ensure_ascii=False, indent=2)
            print("✓ Updated existing_novels.json local database.")
            
            # Clean up pending draft file and cover files
            os.remove(pending_file)
            print("✓ Cleaned up pending_novel.json draft file.")
            
            if os.path.exists("pending_cover.png"):
                try:
                    os.remove("pending_cover.png")
                    print("✓ Cleaned up local pending_cover.png file.")
                except Exception as ce:
                    print("⚠️ Note: Could not delete pending_cover.png:", ce)
            if os.path.exists("base_cover.png"):
                try:
                    os.remove("base_cover.png")
                    print("✓ Cleaned up local base_cover.png file.")
                except Exception as ce:
                    print("⚠️ Note: Could not delete base_cover.png:", ce)
            
        else:
            print("❌ Failed to publish novel via API response:", res_data)
            
    except Exception as e:
        print("❌ API Call Error during publication:", e)
        
if __name__ == "__main__":
    main()
