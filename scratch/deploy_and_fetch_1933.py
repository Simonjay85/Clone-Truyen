import ftplib
import urllib.request
import json
import os

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"

# Step 1: Upload fetch_story_full.php to server
print("1. Uploading fetch_story_full.php to server...")
try:
    ftp = ftplib.FTP(FTP_HOST)
    ftp.login(FTP_USER, FTP_PASS)
    local_path = "fetch_story_full.php"
    with open(local_path, "rb") as f:
        ftp.storbinary(f"STOR fetch_story_full.php", f)
    print("   ✅ Uploaded successfully")
    ftp.quit()
except Exception as e:
    print(f"   ❌ FTP Error: {e}")
    exit(1)

# Step 2: Fetch story 1933
print("\n2. Fetching story 1933...")
url = "https://doctieuthuyet.com/fetch_story_full.php"
payload = json.dumps({
    "secret_token": "ZEN_TRUYEN_2026_BYPASS",
    "story_id": 1933
}).encode('utf-8')

req = urllib.request.Request(url, data=payload, headers={'Content-Type': 'application/json'})
try:
    resp = urllib.request.urlopen(req, timeout=60)
    data = json.loads(resp.read().decode('utf-8'))
    
    # Save full data
    os.makedirs("scratch", exist_ok=True)
    with open("scratch/story_1933_full.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"\n   Title: {data['title']}")
    print(f"   Status: {data['status']}")
    print(f"   Author: {data['author']}")
    print(f"   Genre: {data['genre']}")
    print(f"   Total chapters: {data['total_chapters']}")
    print(f"\n   Intro (200 chars): {data.get('intro','')[:200]}...")
    print()
    
    for i, ch in enumerate(data.get('chapters', [])):
        wc = ch.get('word_count', 0)
        status = "⚠️ NGẮN" if wc < 1000 else "✅"
        print(f"   Ch{i+1}: {ch['title']} — {wc} chars {status}")
        
        content = ch.get('plain_text') or ch.get('content', '')
        # Check for banned phrases
        content_lower = content.lower()
        banned = []
        for phrase in ['tóm lại', 'nhìn chung', 'có thể nói', 'tổng kết', 'nói cách khác', 'cuối cùng,']:
            if phrase in content_lower:
                banned.append(phrase)
        if banned:
            print(f"      ⚠️ Banned phrases: {', '.join(banned)}")
        
        # Check for Chinese names
        chinese_names = ['Tô Khanh', 'Lâm Vũ', 'Tiêu Hàn', 'Trương', 'Lý Thiên', 'Vương']
        found_cn = [n for n in chinese_names if n in content]
        if found_cn:
            print(f"      ⚠️ Chinese-style names: {', '.join(found_cn)}")

    print("\n   ✅ Data saved to scratch/story_1933_full.json")
except Exception as e:
    print(f"   ❌ Error: {e}")
    import traceback
    traceback.print_exc()
