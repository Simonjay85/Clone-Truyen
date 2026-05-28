import urllib.request
import json
import time

with open("scratch/story_categories.json", "r", encoding="utf-8") as f:
    categories = json.load(f)

stories_to_check = categories["need_fetch"]
print(f"Batch fetching {len(stories_to_check)} stories for evaluation...\n")

url = "https://doctieuthuyet.com/fetch_story_full.php"
results = {"rewrite": [], "light_fix": [], "errors": []}

CHINESE_NAMES = [
    'Tô Khanh', 'Lâm Uyển', 'Thẩm Triệt', 'Mộ Dung', 'Tư Mã', 'Công Tôn',
    'Tiêu Hàn', 'Lý Thiên Minh', 'Vương Tử', 'Hoàng Phủ', 'Tống Nhạc',
    'Trương Thiên', 'Lưu Bách', 'Tần Phong', 'Hạ Lam', 'Cố Minh',
    'Mạc Thần', 'Diệp Phong', 'Tạ Lâm', 'Cảnh Dạ', 'Lục Diệp',
    'Khanh Khanh', 'Uyển Nhu', 'Nhược Tình', 'Thiên Thiên'
]
AI_TEMPLATES = [
    'Đến đoạn này, không ai trong phòng cần nghe thêm thuật ngữ',
    'nhân vật chính',
    'Câu nói ấy rơi xuống trước mặt nhân vật chính',
    'Nhưng cú phản công đầu tiên chưa kịp thành hình'
]
BANNED = ['tóm lại', 'nhìn chung', 'có thể nói', 'tổng kết', 'nói cách khác']

for idx, entry in enumerate(stories_to_check):
    story_id = entry["id"]
    try:
        payload = json.dumps({
            "secret_token": "ZEN_TRUYEN_2026_BYPASS",
            "story_id": story_id
        }).encode('utf-8')
        req = urllib.request.Request(url, data=payload, headers={'Content-Type': 'application/json'})
        resp = urllib.request.urlopen(req, timeout=30)
        data = json.loads(resp.read().decode('utf-8'))
        
        issues = []
        needs_rewrite = False
        
        # Check intro
        intro = data.get('intro', '')
        for cn in CHINESE_NAMES:
            if cn in intro:
                issues.append(f"INTRO: Tên TQ '{cn}'")
                needs_rewrite = True
        
        # Check each chapter
        short_count = 0
        for i, ch in enumerate(data.get('chapters', [])):
            text = ch.get('plain_text') or ch.get('content', '')
            wc = ch.get('word_count', len(text))
            
            # Chinese names
            for cn in CHINESE_NAMES:
                if cn in text:
                    issues.append(f"Ch{i+1}: Tên TQ '{cn}'")
                    needs_rewrite = True
                    break
            
            # AI template
            for tmpl in AI_TEMPLATES:
                if tmpl in text:
                    issues.append(f"Ch{i+1}: AI template")
                    needs_rewrite = True
                    break
            
            # Short chapters
            if wc < 800:
                short_count += 1
            
            # Banned phrases
            text_lower = text.lower()
            for bp in BANNED:
                if bp in text_lower:
                    issues.append(f"Ch{i+1}: banned '{bp}'")
                    break
        
        if short_count >= 4:
            issues.append(f"{short_count}/8 chapters too short")
            needs_rewrite = True
        
        entry_result = {
            **entry,
            'title_full': data.get('title', ''),
            'author': data.get('author', ''),
            'genre': data.get('genre', ''),
            'total_chapters': data.get('total_chapters', 0),
            'issues': issues,
            'needs_rewrite': needs_rewrite
        }
        
        if needs_rewrite:
            results["rewrite"].append(entry_result)
        else:
            results["light_fix"].append(entry_result)
        
        status_icon = "🔴" if needs_rewrite else "🟢"
        issue_str = "; ".join(issues[:3]) if issues else "OK"
        print(f"  {idx+1}/{len(stories_to_check)} {status_icon} STT {entry['stt']} ID={story_id} — {issue_str}")
        
    except Exception as e:
        results["errors"].append({**entry, 'error': str(e)})
        print(f"  {idx+1}/{len(stories_to_check)} ❌ STT {entry['stt']} ID={story_id} — Error: {e}")
    
    # Small delay to not overwhelm server
    if idx % 10 == 9:
        time.sleep(1)

# Save results
with open("scratch/batch_eval_results.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(f"\n=== BATCH EVALUATION COMPLETE ===")
print(f"🔴 Need REWRITE: {len(results['rewrite'])}")
print(f"🟢 Light fix only: {len(results['light_fix'])}")
print(f"❌ Errors: {len(results['errors'])}")
print(f"Saved to scratch/batch_eval_results.json")
