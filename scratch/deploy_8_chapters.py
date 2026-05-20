# -*- coding: utf-8 -*-
import os
import json
import requests
import ftplib

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"
WP_URL = "https://doctieuthuyet.com"
STORY_ID = 2052

def main():
    print("=" * 60)
    print("🚀 DEPLOY ENGINE FOR 8-CHAPTER OVERWRITE")
    print("=" * 60)
    
    pending_file = "/Users/aaronnguyen/TN/App/doctieuthuyet/scratch/pending_novel_8.json"
    if not os.path.exists(pending_file):
        print(f"❌ Error: {pending_file} not found! Generation might still be in progress.")
        return
        
    try:
        with open(pending_file, "r", encoding="utf-8") as f:
            novel_data = json.load(f)
        print(f"✓ Loaded story draft: {novel_data['title']} ({len(novel_data['chapters'])} chapters)")
    except Exception as e:
        print("❌ Error parsing pending JSON:", e)
        return

    # 1. Upload overwrite helper via FTP
    print("\nUploading overwrite_story_2052.php helper to FTP root...")
    local_php_path = "/Users/aaronnguyen/TN/App/doctieuthuyet/scratch/overwrite_story_2052.php"
    if not os.path.exists(local_php_path):
        print("❌ PHP helper script not found locally!")
        return
        
    try:
        ftp = ftplib.FTP(FTP_HOST, timeout=30)
        ftp.login(FTP_USER, FTP_PASS)
        with open(local_php_path, "rb") as f:
            ftp.storbinary("STOR overwrite_story_2052.php", f)
        print("✓ Uploaded overwrite_story_2052.php successfully.")
        ftp.quit()
    except Exception as e:
        print("❌ FTP Upload Error:", e)
        return
        
    # 2. Trigger Database Overwrite via HTTP POST request
    print("\nTriggering story overwrite on doctieuthuyet.com...")
    payload = {
        "secret_token": "ZEN_TRUYEN_2026_BYPASS",
        "story_id": STORY_ID,
        "title": novel_data['title'],
        "intro": novel_data['intro'],
        "chapters": novel_data['chapters']
    }
    
    try:
        api_url = f"{WP_URL}/overwrite_story_2052.php"
        res = requests.post(api_url, json=payload, timeout=120)
        res_data = res.json()
        
        if res_data.get('success'):
            print("=" * 60)
            print("🎉 STORY OVERWRITTEN AND REFINED SUCCESSFULLY!")
            print(f"Story ID: {res_data['story_id']}")
            print(f"Title: {res_data['title']}")
            print(f"Chapters Deleted: {res_data['deleted_chapters_count']}")
            print(f"Chapters Inserted: {res_data['inserted_chapters_count']}")
            print("=" * 60)
            
            # 3. Clean up helper script from remote server for security
            try:
                ftp = ftplib.FTP(FTP_HOST, timeout=30)
                ftp.login(FTP_USER, FTP_PASS)
                ftp.delete("overwrite_story_2052.php")
                print("✓ Deleted remote helper script overwrite_story_2052.php.")
                ftp.quit()
            except Exception as clean_err:
                print("⚠️ Failed to clean up remote helper:", clean_err)
                
            # 4. Sync local existing_novels.json
            existing_path = "/Users/aaronnguyen/TN/App/doctieuthuyet/existing_novels.json"
            if os.path.exists(existing_path):
                try:
                    with open(existing_path, "r", encoding="utf-8") as f:
                        data = json.load(f)
                    
                    updated = False
                    for novel in data:
                        if novel.get("id") == STORY_ID:
                            novel["title"] = novel_data['title']
                            novel["intro"] = novel_data['intro']
                            updated = True
                            break
                    
                    if not updated:
                        data.append({
                            "id": STORY_ID,
                            "title": novel_data['title'],
                            "slug": "than-y-phong-kham-quan-5",
                            "intro": novel_data['intro']
                        })
                    
                    with open(existing_path, "w", encoding="utf-8") as f:
                        json.dump(data, f, ensure_ascii=False, indent=2)
                    print("✓ Synced local registry existing_novels.json.")
                except Exception as sync_err:
                    print("⚠️ Failed to sync existing_novels.json:", sync_err)
                    
        else:
            print("❌ Overwrite failed:", res_data.get('error', 'Unknown Error'))
            
    except Exception as e:
        print("❌ HTTP trigger call failed:", e)

if __name__ == "__main__":
    main()
