import urllib.request
import json

story_id = 1968
print(f"=== ĐÁNH GIÁ CHUYÊN SÂU — TRUYỆN ID={story_id} ===\n")

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

print(f"TIÊU ĐỀ: {data['title']}")
print(f"TÁC GIẢ: {data['author']}")
print(f"THỂ LOẠI: {data['genre']}")
print(f"TRẠNG THÁI: {data['status']}")
print(f"SỐ CHƯƠNG: {data['total_chapters']}")
print(f"\nGIỚI THIỆU:\n{data.get('intro','')[:500]}")

# Collect all character names mentioned
all_names = set()
import re

for i, ch in enumerate(data.get('chapters', [])):
    text = ch.get('plain_text') or ch.get('content', '')
    wc = ch.get('word_count', len(text))
    
    print(f"\n{'='*60}")
    print(f"CHƯƠNG {i+1}: {ch['title']} — {wc} ký tự")
    print(f"{'='*60}")
    
    # Print first 500 chars  
    plain = ch.get('plain_text', '')
    print(f"\n[MỞ ĐẦU]:\n{plain[:500]}")
    print(f"\n[KẾT THÚC]:\n{plain[-300:]}")
    
    # Find potential names (Vietnamese pattern: 2-4 syllable capitalized words)
    name_pattern = r'(?:[A-ZÀÁẢÃẠĂẮẰẲẴẶÂẤẦẨẪẬĐÈÉẺẼẸÊẾỀỂỄỆÌÍỈĨỊÒÓỎÕỌÔỐỒỔỖỘƠỚỜỞỠỢÙÚỦŨỤƯỨỪỬỮỰỲÝỶỸỴ][a-zàáảãạăắằẳẵặâấầẩẫậđèéẻẽẹêếềểễệìíỉĩịòóỏõọôốồổỗộơớờởỡợùúủũụưứừửữựỳýỷỹỵ]+\s){1,3}[A-ZÀÁẢÃẠĂẮẰẲẴẶÂẤẦẨẪẬĐÈÉẺẼẸÊẾỀỂỄỆÌÍỈĨỊÒÓỎÕỌÔỐỒỔỖỘƠỚỜỞỠỢÙÚỦŨỤƯỨỪỬỮỰỲÝỶỸỴ][a-zàáảãạăắằẳẵặâấầẩẫậđèéẻẽẹêếềểễệìíỉĩịòóỏõọôốồổỗộơớờởỡợùúủũụưứừửữựỳýỷỹỵ]+'
    found = re.findall(name_pattern, plain)
    for name in found:
        name = name.strip()
        if len(name) > 5 and len(name) < 30:
            all_names.add(name)
    
    # Check issues
    issues = []
    text_lower = text.lower()
    
    # Banned phrases
    for bp in ['tóm lại', 'nhìn chung', 'có thể nói', 'tổng kết', 'nói cách khác']:
        if bp in text_lower:
            issues.append(f"Banned: '{bp}'")
    
    # AI template
    if 'nhân vật chính' in text_lower:
        issues.append("META: 'nhân vật chính'")
    if 'Đến đoạn này, không ai trong phòng' in text:
        issues.append("AI TEMPLATE TEXT")
    if 'Nhưng cú phản công đầu tiên' in text:
        issues.append("AI TEMPLATE TEXT v2")
    
    # Chinese names
    cn_names = ['Tô Khanh', 'Lâm Uyển', 'Thẩm Triệt', 'Khanh Khanh', 'Uyển Nhu']
    for cn in cn_names:
        if cn in text:
            issues.append(f"Tên TQ: '{cn}'")
    
    if issues:
        print(f"\n⚠️ VẤN ĐỀ: {'; '.join(issues)}")
    else:
        print(f"\n✅ Không phát hiện lỗi kỹ thuật")

print(f"\n{'='*60}")
print(f"TẤT CẢ TÊN NHÂN VẬT PHÁT HIỆN:")
print(f"{'='*60}")
for name in sorted(all_names):
    print(f"  - {name}")
