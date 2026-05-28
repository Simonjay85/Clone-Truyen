import ftplib
import urllib.request
import json

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"

# Step 1: Upload overwrite_story_v13.php to server
print("1. Uploading overwrite_story_v13.php to server...")
try:
    ftp = ftplib.FTP(FTP_HOST)
    ftp.login(FTP_USER, FTP_PASS)
    with open("overwrite_story_v13.php", "rb") as f:
        ftp.storbinary("STOR overwrite_story_v13.php", f)
    print("   ✅ Uploaded successfully")
    ftp.quit()
except Exception as e:
    print(f"   ❌ FTP Error: {e}")
    exit(1)

# Step 2: Upload story data
print("\n2. Uploading rewritten story 1933...")
with open("scratch/story_1933_rewrite.json", "r", encoding="utf-8") as f:
    story_data = json.load(f)

url = "https://doctieuthuyet.com/overwrite_story_v13.php"
payload = json.dumps(story_data).encode('utf-8')
req = urllib.request.Request(url, data=payload, headers={'Content-Type': 'application/json'})
try:
    resp = urllib.request.urlopen(req, timeout=120)
    result = json.loads(resp.read().decode('utf-8'))
    print(f"   ✅ Upload success!")
    print(f"   Story ID: {result.get('story_id')}")
    print(f"   Title: {result.get('title')}")
    print(f"   Deleted old chapters: {result.get('deleted_old_chapters')}")
    print(f"   New chapters: {result.get('chapters_count')}")
    print(f"   SEO updated: {result.get('seo_updated')}")
except Exception as e:
    print(f"   ❌ Error: {e}")
    try:
        err_body = e.read().decode('utf-8') if hasattr(e, 'read') else str(e)
        print(f"   Response: {err_body[:500]}")
    except:
        pass

# Step 3: Clear cache
print("\n3. Clearing cache...")
try:
    resp = urllib.request.urlopen("https://doctieuthuyet.com/run_clear_cache.php", timeout=15)
    print(f"   {resp.read().decode('utf-8')[:200]}")
except:
    print("   Cache clear skipped (no endpoint)")
