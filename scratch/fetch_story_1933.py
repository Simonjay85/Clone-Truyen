import urllib.request
import json

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
    with open("scratch/story_1933_full.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"Title: {data['title']}")
    print(f"Status: {data['status']}")
    print(f"Author: {data['author']}")
    print(f"Genre: {data['genre']}")
    print(f"Total chapters: {data['total_chapters']}")
    print(f"\nIntro: {data['intro'][:200]}...")
    print()
    
    for i, ch in enumerate(data['chapters']):
        print(f"  Ch{i+1}: {ch['title']} — {ch['word_count']} chars")
        # Check for banned phrases
        content_lower = ch['plain_text'].lower() if ch.get('plain_text') else ch['content'].lower()
        banned = []
        for phrase in ['tóm lại', 'nhìn chung', 'có thể nói', 'tổng kết', 'nói cách khác', 'cuối cùng,']:
            if phrase in content_lower:
                banned.append(phrase)
        if banned:
            print(f"    ⚠️ Banned phrases: {', '.join(banned)}")
        
        # Check for Chinese names
        chinese_names = ['Tô Khanh', 'Lâm Vũ', 'Tiêu Hàn', 'Trương', 'Lý Thiên', 'Vương']
        found_cn = [n for n in chinese_names if n in (ch.get('plain_text') or ch['content'])]
        if found_cn:
            print(f"    ⚠️ Chinese-style names: {', '.join(found_cn)}")

    print("\n✅ Data saved to scratch/story_1933_full.json")
except Exception as e:
    print(f"Error: {e}")
