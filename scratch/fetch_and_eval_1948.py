import urllib.request
import json

# Fetch story 1948 (STT 187)
story_id = 1948
print(f"Fetching story {story_id}...")

url = "https://doctieuthuyet.com/fetch_story_full.php"
payload = json.dumps({
    "secret_token": "ZEN_TRUYEN_2026_BYPASS",
    "story_id": story_id
}).encode('utf-8')

req = urllib.request.Request(url, data=payload, headers={'Content-Type': 'application/json'})
resp = urllib.request.urlopen(req, timeout=60)
data = json.loads(resp.read().decode('utf-8'))

with open(f"scratch/story_{story_id}_full.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\nTitle: {data['title']}")
print(f"Status: {data['status']}")
print(f"Author: {data['author']}")
print(f"Genre: {data['genre']}")
print(f"Chapters: {data['total_chapters']}")
print(f"\nIntro: {data.get('intro','')[:300]}...\n")

# Quality check each chapter
issues = []
for i, ch in enumerate(data.get('chapters', [])):
    wc = ch.get('word_count', 0)
    status = "⚠️ NGẮN" if wc < 800 else ("⚠️ HƠI NGẮN" if wc < 1200 else "✅")
    print(f"  Ch{i+1}: {ch['title']} — {wc} chars {status}")
    
    content = ch.get('plain_text') or ch.get('content', '')
    content_lower = content.lower()
    
    # Banned phrases
    banned = []
    for phrase in ['tóm lại', 'nhìn chung', 'có thể nói', 'tổng kết', 'nói cách khác']:
        if phrase in content_lower:
            banned.append(phrase)
    if banned:
        print(f"      ⚠️ Banned: {', '.join(banned)}")
        issues.append(f"Ch{i+1}: banned phrases")
    
    # Chinese names
    chinese_markers = ['Tô ', 'Thẩm ', 'Lâm Vũ', 'Tiêu Hàn', 'Lý Thiên', 'Mộ Dung', 'Tư Mã', 'Công Tôn']
    found_cn = [n for n in chinese_markers if n in content]
    if found_cn:
        print(f"      ⚠️ Chinese names: {', '.join(found_cn)}")
        issues.append(f"Ch{i+1}: Chinese names")
    
    if wc < 800:
        issues.append(f"Ch{i+1}: too short ({wc} chars)")

    # First 300 chars of chapter for content analysis
    first_300 = (ch.get('plain_text') or '')[:300]
    if i == 0:
        print(f"\n  === CH1 OPENING (first 300 chars) ===")
        print(f"  {first_300}")
        print(f"  === END ===\n")

print(f"\n=== TỔNG KẾT ===")
if not issues:
    print("Không phát hiện lỗi nghiêm trọng. Có thể SỬA NHẸ.")
else:
    print(f"Phát hiện {len(issues)} vấn đề:")
    for iss in issues:
        print(f"  - {iss}")
    if any("Chinese" in i for i in issues) or any("too short" in i for i in issues):
        print("\n→ CẦN REWRITE TOÀN BỘ")
    else:
        print("\n→ CẦN SỬA NHẸ")
