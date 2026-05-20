import os
import json
import time
import urllib.parse
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

    # 1. Construct Cover Image URL via Pollinations
    cover_prompt = novel_data.get("cover_prompt", "masterpiece, highly detailed book cover, anime illustration style, vivid lighting")
    escaped_prompt = urllib.parse.quote(cover_prompt + ", masterpiece, highly detailed book cover, anime illustration style, vivid lighting")
    cover_url = f"https://image.pollinations.ai/prompt/{escaped_prompt}?width=800&height=1200&seed={random.randint(1, 99999)}&nologo=true"

    # 2. Upload publish_novel.php helper script via FTP
    print("\nUploading publish_novel.php endpoint to FTP root...")
    try:
        ftp = ftplib.FTP(FTP_HOST, timeout=30)
        ftp.login(FTP_USER, FTP_PASS)
        
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
        "cover_url": cover_url,
        "chapters": novel_data['chapters']
    }
    
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
                ftp = ftplib.FTP(FTP_HOST, timeout=30)
                ftp.login(FTP_USER, FTP_PASS)
                ftp.delete("publish_novel.php")
                print("✓ Deleted publish_novel.php helper from remote server for security.")
                ftp.quit()
            except:
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
            
            # Clean up pending draft file
            os.remove(pending_file)
            print("✓ Cleaned up pending_novel.json draft file.")
            
        else:
            print("❌ Failed to publish novel via API response:", res_data)
            
    except Exception as e:
        print("❌ API Call Error during publication:", e)
        
if __name__ == "__main__":
    main()
