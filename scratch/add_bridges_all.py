#!/usr/bin/env python3
"""
Add continuity bridges between ALL chapters for all 10 stories.
For each chapter N (N>=2): prepend a bridge paragraph referencing end of chapter N-1.
"""
import ftplib, requests, io, json, time, re

FTP_HOST = "51.79.53.190"; FTP_USER = "alotoinghe"; FTP_PASS = "Nghia234!"
WP_URL = "https://doctieuthuyet.com"; SECRET = "ZEN_TRUYEN_2026_BYPASS"

def strip_html(html):
    """Remove HTML tags and return plain text."""
    text = re.sub(r'<[^>]+>', ' ', html)
    text = re.sub(r'&[a-z]+;', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def get_last_sentences(content, n=3):
    """Get last N meaningful sentences from chapter content."""
    text = strip_html(content)
    # Split by sentence-ending punctuation
    sentences = re.split(r'(?<=[.!?…"»])\s+', text)
    sentences = [s.strip() for s in sentences if len(s.strip()) > 20]
    return sentences[-n:] if len(sentences) >= n else sentences

def get_first_name(content):
    """Try to extract first proper name mentioned in content."""
    text = strip_html(content)
    # Common Vietnamese name patterns (Nguyen Van X, Tran Thi X, etc.)
    m = re.search(r'([A-ZĐÀÁẢÃẠĂẮẶẰẲẴÂẤẦẨẪẬ][a-zđàáảãạăắặằẳẵâấầẩẫậ]+ '
                  r'[A-ZĐÀÁẢÃẠĂẮẶẰẲẴÂẤẦẨẪẬ][a-zđàáảãạăắặằẳẵâấầẩẫậ]+)', text)
    if m:
        # Return just last name part (shorter)
        parts = m.group(1).split()
        return parts[-1] if parts else "Anh"
    return "Anh"

def generate_bridge(prev_content, prev_title, curr_title, story_id):
    """
    Generate a contextual bridge paragraph connecting prev chapter to current.
    Extracts key elements from the end of the previous chapter.
    """
    last_sents = get_last_sentences(prev_content, 2)
    last_text = ' '.join(last_sents).strip()
    
    # Extract chapter numbers for context
    m_prev = re.search(r'\d+', prev_title)
    m_curr = re.search(r'\d+', curr_title)
    prev_num = int(m_prev.group()) if m_prev else 0
    curr_num = int(m_curr.group()) if m_curr else 0
    
    # Detect tone of previous chapter ending
    crisis_keywords = ['phong tỏa', 'bắt', 'cáo buộc', 'tố cáo', 'nguy', 'khủng hoảng',
                       'sụp đổ', 'thất bại', 'mất', 'bẫy', 'đe dọa', 'tấn công', 'tan vỡ',
                       'khóa', 'niêm phong', 'tạm giam', 'điều tra', 'phanh phui', 'vỡ lở',
                       'kiện', 'thua', 'mất hết', 'ruồng bỏ', 'đuổi', 'sa thải', 'ép', 'độc']
    victory_keywords = ['thắng', 'thành công', 'chiến thắng', 'chứng minh', 'phục hồi',
                        'lật kèo', 'vạch trần', 'bóc trần', 'nở nụ cười', 'ngẩng đầu',
                        'tuyên bố', 'xử lý', 'giải quyết', 'vinh quang', 'ký kết']
    romance_keywords = ['ánh mắt', 'bàn tay', 'im lặng', 'tim đập', 'cảm giác', 
                        'nhìn nhau', 'chạm', 'gần', 'hơi ấm', 'nụ cười của cô', 'của anh']
    
    last_lower = last_text.lower()
    
    has_crisis = any(k in last_lower for k in crisis_keywords)
    has_victory = any(k in last_lower for k in victory_keywords)
    has_romance = any(k in last_lower for k in romance_keywords)
    
    # Build bridge based on detected tone
    if has_crisis:
        templates = [
            f"<p>Tiếng vang của {_extract_key_noun(last_text)} còn chưa kịp lắng xuống khi bình minh ló dạng — và với {_extract_protagonist(prev_content)}, đó là khởi đầu của một ngày đòi hỏi sự tỉnh táo hơn bao giờ hết.</p>",
            f"<p>Cả đêm đó, {_extract_protagonist(prev_content)} không chợp mắt. Trong đầu anh, những mảnh ghép của {_extract_key_noun(last_text)} cứ xoay vòng, và đến lúc bình minh ló rạng, anh đã có một quyết định.</p>",
            f"<p>Không khí vẫn còn nặng nề từ những gì xảy ra trước đó. {_extract_protagonist(prev_content)} ngồi thẳng lưng, nhìn vào khoảng tối trước mắt — và bắt đầu tính bước tiếp theo.</p>",
        ]
    elif has_victory:
        templates = [
            f"<p>Nhưng chiến thắng không có nghĩa là kết thúc. {_extract_protagonist(prev_content)} hiểu điều đó hơn ai hết — kẻ thù thực sự vẫn còn đứng sau bóng tối, và bước đi tiếp theo mới chính là thử thách thật sự.</p>",
            f"<p>Dù vậy, {_extract_protagonist(prev_content)} không để mình say men chiến thắng quá lâu. Còn quá nhiều thứ chưa ngã ngũ, và thời gian không đứng về phía người đứng yên.</p>",
            f"<p>Khoảnh khắc đó sẽ khắc vào trí nhớ — nhưng chỉ trong một chớp mắt, thực tại kéo {_extract_protagonist(prev_content)} trở lại: trận chiến vẫn còn dang dở.</p>",
        ]
    elif has_romance:
        templates = [
            f"<p>Cảm giác đó còn vương vấn mãi. {_extract_protagonist(prev_content)} biết mình không nên để tâm — nhưng có những thứ không thể kiểm soát chỉ bằng lý trí.</p>",
            f"<p>Đêm đó, {_extract_protagonist(prev_content)} nằm nhìn trần nhà và tự hỏi điều gì đang xảy ra trong lòng mình — rồi lật người, gạt đi, và tập trung vào những việc còn quan trọng hơn.</p>",
        ]
    else:
        templates = [
            f"<p>Sáng sớm hôm sau, trước khi ánh nắng kịp len qua khe cửa, {_extract_protagonist(prev_content)} đã ngồi dậy — trong đầu anh, những gì xảy ra ngày hôm qua vẫn còn đó, nhưng hướng đi đã rõ hơn.</p>",
            f"<p>Vài giờ trôi qua. {_extract_protagonist(prev_content)} gác điện thoại xuống sau cuộc gọi cuối cùng trong đêm và nhìn ra cửa sổ — thành phố vẫn sáng đèn, và guồng quay không cho phép ai dừng lại.</p>",
            f"<p>Đêm không dài với người không ngủ được. {_extract_protagonist(prev_content)} đã dành cả đêm đó để chuẩn bị — và khi trời sáng, anh bước ra ngoài với một kế hoạch hoàn chỉnh trong tay.</p>",
        ]
    
    # Use first template or rotate based on chapter number
    idx = (curr_num - 2) % len(templates)
    return templates[idx]

def _extract_protagonist(content):
    """Extract the main character name from chapter content."""
    text = strip_html(content)
    # Find most frequently mentioned proper name
    # Look for Vietnamese name patterns
    names = re.findall(r'\b([A-ZĐÀÁẢÃẠĂẮẶẰẲẴÂẤẦẨẪẬ][a-zđàáảãạăắặằẳẵâấầẩẫậ]{1,8})\b', text)
    if not names:
        return "Anh"
    # Count frequency
    from collections import Counter
    counts = Counter(names)
    # Filter out common words
    stopwords = {'Chương', 'Nhưng', 'Không', 'Được', 'Trong', 'Ngoài', 'Khi',
                 'Sau', 'Trước', 'Một', 'Hai', 'Còn', 'Đã', 'Sẽ', 'Có', 'Và',
                 'Với', 'Từ', 'Đây', 'Đó', 'Anh', 'Cô', 'Ông', 'Bà', 'Hắn'}
    for sw in stopwords:
        counts.pop(sw, None)
    if counts:
        return counts.most_common(1)[0][0]
    return "Anh"

def _extract_key_noun(text):
    """Extract a key noun phrase from text to use in bridge."""
    # Common dramatic nouns in Vietnamese fiction
    keywords = ['tin tức', 'sự kiện', 'cú sốc', 'quyết định', 'biến cố', 
                'thông tin', 'bằng chứng', 'cáo buộc', 'phán quyết', 'thách thức',
                'sự phản bội', 'mối đe dọa', 'cuộc điều tra', 'vụ việc']
    text_lower = text.lower()
    for kw in keywords:
        if kw in text_lower:
            return kw
    return "những gì vừa xảy ra"

# ============================================================
# MAIN
# ============================================================
if __name__ == "__main__":
    with open("/tmp/all_10_stories.json","r",encoding="utf-8") as f:
        all_stories = json.load(f)
    
    with open("scratch/novel_editor.py","r",encoding="utf-8") as f: py = f.read()
    php_start = py.find('UPDATE_PHP = """') + len('UPDATE_PHP = """')
    php_end = py.find('"""\n', php_start)
    php_code = py[php_start:php_end]
    
    total_bridges = 0
    
    for sid_str, chapters in all_stories.items():
        sid = int(sid_str)
        print(f"\n{'='*55}")
        print(f"Story {sid} — {len(chapters)} chapters")
        
        # Upload helper
        ftp = ftplib.FTP(FTP_HOST, timeout=30); ftp.login(FTP_USER, FTP_PASS)
        ftp.storbinary("STOR novel_editor.php", io.BytesIO(php_code.encode()))
        ftp.quit()
        
        for i in range(1, len(chapters)):
            prev_ch = chapters[i-1]
            curr_ch = chapters[i]
            
            # Generate bridge from prev chapter ending
            bridge = generate_bridge(
                prev_ch['content'], 
                prev_ch['title'],
                curr_ch['title'],
                sid
            )
            
            # Check if bridge already exists (avoid double-adding)
            curr_content = curr_ch['content']
            if bridge[:50] in curr_content:
                print(f"  Ch{i+1} [SKIP - bridge exists]")
                continue
            
            # Prepend bridge to current chapter
            new_content = bridge + "\n" + curr_content
            
            # Deploy
            API = f"{WP_URL}/novel_editor.php"
            payload = {
                "action": "update_chapter",
                "chapter_id": curr_ch['id'],
                "title": curr_ch['title'],
                "content": new_content,
                "secret": SECRET
            }
            r = requests.post(API, json=payload, timeout=90)
            try:
                result = r.json()
                ok = '✓' if result.get('success') else '✗'
            except:
                ok = '?'
            
            print(f"  Ch{i+1} [{curr_ch['id']}] {ok} bridge added → {curr_ch['title'][:40]}")
            total_bridges += 1
            time.sleep(0.35)
        
        # Cleanup
        ftp = ftplib.FTP(FTP_HOST, timeout=30); ftp.login(FTP_USER, FTP_PASS)
        try: ftp.delete("novel_editor.php")
        except: pass
        ftp.quit()
        
        print(f"  ✅ Story {sid} done")
        time.sleep(0.5)
    
    print(f"\n✅ ALL DONE: {total_bridges} bridges added across 10 stories")
