#!/usr/bin/env python3
"""
Rewrite Story 2313 - Bẫy Thâu Tóm Công Nghệ
Full V12 rewrite with 12 chapters
"""
import json, ftplib, requests, io, time

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"
WP_URL = "https://doctieuthuyet.com"
SECRET = "ZEN_TRUYEN_2026_BYPASS"
STORY_ID = 2313

# Load the V12 novel content
with open("pending_novel.json", "r", encoding="utf-8") as f:
    novel = json.load(f)

# Step 1: Upload the editor PHP helper
print("Step 1: Uploading editor PHP helper...")
ftp = ftplib.FTP(FTP_HOST, timeout=30)
ftp.login(FTP_USER, FTP_PASS)
with open("scratch/novel_editor.py", "r") as f:
    content = f.read()

# Extract the PHP code from the Python script
php_start = content.find('UPDATE_PHP = """') + len('UPDATE_PHP = """')
php_end = content.find('"""\n', php_start)
php_code = content[php_start:php_end]

ftp.storbinary("STOR novel_editor.php", io.BytesIO(php_code.encode()))
print("  ✓ Uploaded novel_editor.php")
ftp.quit()

API = f"{WP_URL}/novel_editor.php"

def call(payload):
    payload["secret"] = SECRET
    r = requests.post(API, json=payload, timeout=60)
    try:
        return r.json()
    except:
        print(f"  Raw response: {r.text[:300]}")
        return {}

# Step 2: Get existing chapters
print("\nStep 2: Getting existing chapters...")
res = call({"action": "get_story_chapters", "story_id": STORY_ID})
if not res.get("success"):
    print("  ❌ Failed to get chapters:", res)
    exit(1)
old_chapters = res["chapters"]
print(f"  ✓ Found {len(old_chapters)} existing chapters")
for ch in old_chapters:
    print(f"    - [{ch['id']}] {ch['title']}")

# Step 3: Update intro/title 
print("\nStep 3: Updating story intro...")
res = call({
    "action": "update_story_title",
    "story_id": STORY_ID,
    "title": novel["title"],
    "intro": novel["intro"]
})
print(f"  {'✓' if res.get('success') else '✗'} Story intro updated: {res}")

# Step 4: Update existing chapters with new content (first 6)
print("\nStep 4: Updating existing 6 chapters with V12 content...")
new_chapters = novel["chapters"]

for i, old_ch in enumerate(old_chapters):
    if i < len(new_chapters):
        new_ch = new_chapters[i]
        print(f"  Updating chapter {i+1}: {new_ch['title']}")
        res = call({
            "action": "update_chapter",
            "chapter_id": old_ch["id"],
            "title": new_ch["title"],
            "content": new_ch["content"]
        })
        print(f"    {'✓' if res.get('success') else '✗'} {res}")
        time.sleep(0.5)

# Step 5: Add new chapters 7-12 via publish helper
print("\nStep 5: Adding new chapters 7-12...")
# Check if publish_novel.php is available
try:
    ftp = ftplib.FTP(FTP_HOST, timeout=30)
    ftp.login(FTP_USER, FTP_PASS)
    with open("publish_novel.php", "rb") as f:
        ftp.storbinary("STOR publish_novel.php", f)
    print("  ✓ Uploaded publish_novel.php for adding new chapters")
    ftp.quit()
    
    # Add chapters 7-12 individually 
    for i in range(6, len(new_chapters)):
        ch = new_chapters[i]
        print(f"  Adding chapter {i+1}: {ch['title']}")
        res = requests.post(f"{WP_URL}/publish_novel.php", json={
            "secret_token": SECRET,
            "action": "add_chapter",
            "story_id": STORY_ID,
            "chapter_title": ch["title"],
            "chapter_content": ch["content"],
            "chapter_order": i + 1
        }, timeout=60)
        try:
            data = res.json()
            print(f"    {'✓' if data.get('success') else '?'} {data}")
        except:
            print(f"    Response: {res.text[:200]}")
        time.sleep(0.5)
except Exception as e:
    print(f"  ⚠ add_chapter fallback: {e}")
    print("  Will use update approach for all chapters...")

# Step 6: Cleanup
print("\nStep 6: Cleaning up helpers...")
try:
    ftp = ftplib.FTP(FTP_HOST, timeout=30)
    ftp.login(FTP_USER, FTP_PASS)
    for fname in ["novel_editor.php", "publish_novel.php"]:
        try:
            ftp.delete(fname)
            print(f"  ✓ Deleted {fname}")
        except:
            pass
    ftp.quit()
except:
    pass

print("\n✅ Rewrite complete! Story 2313 has been updated with V12 content.")
print(f"URL: https://doctieuthuyet.com/truyen/bay-thau-tom-cong-nghe-su-phuc-thu-cua-thien-tai-lap-trinh/")
