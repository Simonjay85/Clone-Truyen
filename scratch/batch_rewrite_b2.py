#!/usr/bin/env python3
"""
Batch rewrite 5 stories: fix chapter order, replace real names, improve continuity, deploy
Stories: 2217, 2238, 2249, 2190, 2052
"""
import ftplib, requests, io, json, time, re
from html.parser import HTMLParser

FTP_HOST = "51.79.53.190"; FTP_USER = "alotoinghe"; FTP_PASS = "Nghia234!"
WP_URL = "https://doctieuthuyet.com"; SECRET = "ZEN_TRUYEN_2026_BYPASS"

# ============================================================
# NAME MAP — thay tất cả tên thật bằng tên hư cấu
# ============================================================
NAME_MAP = [
    # Địa danh (dài trước, ngắn sau để tránh partial replace)
    ("TP. Hồ Chí Minh", "Thành Tâm"), ("TP.HCM", "Thành Tâm"),
    ("Thành phố Hồ Chí Minh", "Thành Tâm"),
    ("thành phố Hồ Chí Minh", "Thành Tâm"),
    ("Hồ Chí Minh", "Thành Tâm"),
    ("Hà Nội", "Hà Ngoại"),
    ("Sài Gòn", "Thành Tâm"),
    ("Phú Mỹ Hưng", "Phú Mỹ Hoa"),
    ("Quận 7", "Quận Đông"), ("quận 7", "Quận Đông"),
    ("Quận 5", "Quận Năm"), ("quận 5", "Quận Năm"),
    ("Quận 1", "Quận Trung Tâm"), ("quận 1", "Quận Trung Tâm"),
    ("Đắk Lắk", "Đắk Minh"), ("Đắk Lắk", "Đắk Minh"),
    ("Buôn Ma Thuột", "Ban Mê Thịnh"), ("Đà Lạt", "Đà Nguyên"),
    ("Đà Nẵng", "Đà Thành"), ("Hội An", "Hội Nguyên"),
    ("Nha Trang", "Ngọc Thành"), ("Vũng Tàu", "Vũng Giang"),
    ("Cần Thơ", "Cần Giang"), ("Bình Dương", "Bình Thịnh"),
    ("Hải Phòng", "Hải Bình"), ("Huế", "Huệ Châu"),
    ("Hồ Tây", "Hồ Tây Bắc"), ("Hoàn Kiếm", "Hoàn Ngọc"),
    ("Phố Đinh Lễ", "Phố Định Lễ"),
    # Ngân hàng
    ("Vietcombank", "Việt Thương Bank"), ("vietcombank", "Việt Thương Bank"),
    ("BIDV", "Ngân hàng BĐTV"), ("Agribank", "Nông Ngân"),
    ("MB Bank", "MB Tín"), ("Techcombank", "Kỹ Thương Bank"),
    ("VPBank", "VP Tín"), ("TPBank", "TP Tín"), ("VIB", "Việt Quốc Bank"),
    ("Sacombank", "Sài Thương Bank"), ("ACB", "Á Châu Tín"),
    ("Ngân hàng Nhà nước", "Ngân hàng Trung ương"),
    ("Ngân hàng Ngoại thương", "Ngân hàng Đối ngoại Quốc gia"),
    # Doanh nghiệp / Tập đoàn
    ("Viettel", "Viễn Thông Vạn"), ("VNPT", "Bưu chính Vạn Thịnh"),
    ("EVN", "Điện lực Vạn Thịnh"), ("FPT", "Công nghệ FPH"),
    ("Vincom", "Thương xá Vạn Phát"), ("Vinhomes", "Khu đô thị Vạn Hoa"),
    # Cơ quan
    ("C03 Bộ Công An", "Cục C09 Bộ An Ninh"),
    ("C03", "Cục C09"), ("A05", "Cục A08"), ("C04", "Cục C06"),
    ("Bộ Công An", "Bộ An Ninh"),
    ("HNX", "Sở GDCK Phương Bắc"), ("HOSE", "Sở GDCK Phương Nam"),
    ("UBCKNN", "Ủy ban Chứng khoán Quốc gia"),
    ("Cục Sở hữu Trí tuệ Việt Nam", "Cục Bản quyền Sở hữu Quốc gia"),
    ("Cục Sở hữu trí tuệ", "Cục Bản quyền Sở hữu"),
    ("Bộ Khoa học và Công nghệ", "Bộ Kỹ thuật và Đổi mới"),
    ("Bộ Y tế", "Bộ Sức khỏe Quốc dân"),
    ("Bộ Tài chính", "Bộ Tài vụ"),
    ("Sở Xây Dựng", "Sở Quy hoạch Đô thị"),
    ("Vietnam Fashion Week", "Hội Nghị Thời Trang Quốc Gia"),
    ("VFA", "Hiệp hội Thời trang Toàn quốc"),
    # Trường đại học
    ("Đại học Bách Khoa Hà Nội", "Đại học Kỹ thuật Hà Ngoại"),
    ("Đại học Bách Khoa", "Đại học Kỹ thuật Phương Nam"),
    ("Bách Khoa", "Kỹ thuật Phương Nam"),
    ("Đại học Y Dược", "Đại học Y khoa Quốc gia"),
    ("Đại học Kinh tế", "Đại học Tài chính Quốc dân"),
    # Địa điểm cụ thể
    ("JW Marriott", "Khách sạn Grand Minh"),
    ("Capital Place", "Tòa nhà Minh Thịnh Plaza"),
    ("Lotte", "Tòa nhà Long Phát"),
    ("Times City", "Khu đô thị Thịnh Vượng"),
    ("Nhà hát Lớn", "Nhà hát Phương Nam"),
    ("Trung tâm Hội nghị Quốc gia", "Trung tâm Hội nghị Quốc tế Thịnh Vượng"),
    ("Bệnh viện Bạch Mai", "Bệnh viện Trung ương Phương Bắc"),
    ("Bệnh viện Chợ Rẫy", "Bệnh viện Trung ương Phương Nam"),
    ("Viettel IDC", "Trung tâm Dữ liệu Vạn Thịnh"),
    ("SCADA", "SCADA"),  # keep technical term
    # Hệ thống kỹ thuật - giữ nguyên vì là thuật ngữ
]

def apply_name_map(text):
    for old, new in NAME_MAP:
        text = text.replace(old, new)
    return text

def extract_chapter_number(title):
    """Extract chapter number from title like 'Chương 7: ...' """
    m = re.search(r'[Cc]h(?:ương|apter)?\s*(\d+)', title)
    if m:
        return int(m.group(1))
    return 999

# ============================================================
# Continuity bridges — nối từ chapter N sang N+1
# ============================================================
# Format: { story_id: { chapter_order: "bridge paragraph" } }
BRIDGES = {
    2217: {
        # Between Ch1 (bị sa thải) and Ch2 (gặp nữ phó tổng)
        2: "<p>Đêm hôm đó, Hùng không về nhà ngay. Anh ngồi ở ghế đá công viên gần trụ sở Điện lực Vạn Thịnh, nhìn lên tòa nhà sáng đèn nơi mình vừa bị tống cổ ra, và bắt đầu viết email — một email gửi cho bộ phận kiểm soát nội bộ của tập đoàn, kèm theo toàn bộ dữ liệu SCADA bất thường mà anh đã lén backup trên USB trong ba tháng qua.</p>",
    },
    2238: {
        2: "<p>Hôm sau, khi Khoa còn đang ngồi trong quán trọ rẻ tiền ở ngoại ô Ban Mê Thịnh với hai trăm nghìn cuối cùng trong ví, một tin nhắn từ số lạ hiện ra trên điện thoại: <em>\"Anh có muốn gặp người có thể cứu thương hiệu cà phê của anh không?\"</em></p>",
    },
    2249: {
        2: "<p>Khuya hôm đó, Minh không ngủ được. Anh trải tờ giấy phác thảo cũ lên sàn nhà trọ và nhìn chằm chằm vào những nét bút mà anh đã vẽ từ sáu tháng trước — bộ sưu tập bị đánh cắp. Rồi điện thoại rung: một cuộc hẹn từ văn phòng Hiệp hội Thời trang Toàn quốc.</p>",
    },
    2190: {
        2: "<p>Sáng sớm ngày hôm sau, khi Tuấn đang ngồi ăn bánh mì ở vỉa hè gần Sở GDCK Phương Bắc với hai mươi nghìn đồng còn lại, anh nhận được một email từ địa chỉ chính thức của Ủy ban Chứng khoán Quốc gia: yêu cầu anh có mặt để phối hợp điều tra một vụ thao túng thị trường.</p>",
    },
    2052: {
        2: "<p>Đêm đó, Minh lái xe đến bệnh viện — không phải để xin việc lại, mà để lấy hộp đồ cá nhân còn để quên trong tủ khóa phòng bác sĩ. Trên đường về, một chiếc Porsche màu trắng phanh sát cạnh và cửa xe hạ xuống.</p>",
    },
}

def rewrite_chapter(chapter, story_id, chapter_order, char_names, next_chapter_hint=""):
    """Apply name map + add continuity bridge if needed"""
    content = chapter['content']
    title = chapter['title']
    
    # Apply name map
    content = apply_name_map(content)
    title = apply_name_map(title)
    
    # Fix chapter title numbering
    title = re.sub(r'[Cc]h(?:ương)?\s*\d+:', f'Chương {chapter_order}:', title)
    
    # Add bridge at beginning if defined
    bridge = BRIDGES.get(story_id, {}).get(chapter_order, "")
    if bridge:
        content = bridge + "\n" + content
    
    # Apply character name consistency from char_names map
    for old_name, new_name in char_names.items():
        content = content.replace(old_name, new_name)
        title = title.replace(old_name, new_name)
    
    return title, content

# ============================================================
# Character name normalization per story
# ============================================================
CHAR_NAMES = {
    2217: {},  # names OK
    2238: {"Nguyễn Văn Khoa": "Lê Văn Khoa"},  # normalize if variant exists
    2249: {},
    2190: {"Trần Văn Tuấn": "Nguyễn Văn Tuấn"},  # normalize
    2052: {},
}

# ============================================================
# MAIN DEPLOY LOGIC
# ============================================================
def upload_php_helper(ftp, php_code):
    ftp.storbinary("STOR novel_editor.php", io.BytesIO(php_code.encode()))

def api_call(payload):
    payload["secret"] = SECRET
    r = requests.post(f"{WP_URL}/novel_editor.php", json=payload, timeout=90)
    try: return r.json()
    except: return {"raw": r.text[:200]}

def deploy_story(sid, chapters_data, php_code):
    print(f"\n{'='*60}")
    print(f"Processing Story {sid}")
    
    # Upload helper
    ftp = ftplib.FTP(FTP_HOST, timeout=30); ftp.login(FTP_USER, FTP_PASS)
    upload_php_helper(ftp, php_code)
    ftp.quit()
    
    # Sort chapters by chapter number in title
    sorted_chaps = sorted(chapters_data, key=lambda c: extract_chapter_number(c['title']))
    
    char_names = CHAR_NAMES.get(sid, {})
    
    # Update each chapter
    for i, ch in enumerate(sorted_chaps):
        order = i + 1
        new_title, new_content = rewrite_chapter(ch, sid, order, char_names)
        
        result = api_call({
            "action": "update_chapter",
            "chapter_id": ch['id'],
            "title": new_title,
            "content": new_content,
        })
        
        ok = '✓' if result.get('success') else '✗'
        print(f"  Ch{order} [{ch['id']}] {ok} → {new_title[:55]}")
        time.sleep(0.4)
    
    # Cleanup helper
    ftp = ftplib.FTP(FTP_HOST, timeout=30); ftp.login(FTP_USER, FTP_PASS)
    try: ftp.delete("novel_editor.php")
    except: pass
    ftp.quit()
    
    print(f"  ✅ Story {sid} done — {len(sorted_chaps)} chapters updated")
    return len(sorted_chaps)

if __name__ == "__main__":
    # Load all stories
    with open("/tmp/stories_batch2.json","r",encoding="utf-8") as f:
        all_stories = json.load(f)
    
    # Extract editor PHP
    with open("scratch/novel_editor.py","r",encoding="utf-8") as f: py = f.read()
    php_start = py.find('UPDATE_PHP = """') + len('UPDATE_PHP = """')
    php_end = py.find('"""\n', php_start)
    php_code = py[php_start:php_end]
    
    total = 0
    for sid_str, story_data in all_stories.items():
        sid = int(sid_str)
        chapters = story_data['chapters']
        
        # Also update story title/intro if contains real names
        new_title = apply_name_map(story_data['title'])
        new_intro = apply_name_map(story_data['intro'])
        
        count = deploy_story(sid, chapters, php_code)
        total += count
        
        # Update story title/intro
        ftp = ftplib.FTP(FTP_HOST, timeout=30); ftp.login(FTP_USER, FTP_PASS)
        with open("scratch/novel_editor.py","r",encoding="utf-8") as f: py2 = f.read()
        php_start2 = py2.find('UPDATE_PHP = """') + len('UPDATE_PHP = """')
        php_end2 = py2.find('"""\n', php_start2)
        php_code2 = py2[php_start2:php_end2]
        ftp.storbinary("STOR novel_editor.php", io.BytesIO(php_code2.encode()))
        ftp.quit()
        
        r = api_call({"action":"update_story_title","story_id":sid,"title":new_title,"intro":new_intro})
        print(f"  Title/intro: {'✓' if r.get('success') else '✗'} → {new_title[:55]}")
        
        ftp = ftplib.FTP(FTP_HOST, timeout=30); ftp.login(FTP_USER, FTP_PASS)
        try: ftp.delete("novel_editor.php")
        except: pass
        ftp.quit()
        
        time.sleep(1)
    
    print(f"\n✅ BATCH COMPLETE: {total} chapters updated across {len(all_stories)} stories")
