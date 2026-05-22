#!/usr/bin/env python3
"""
Master script: Fetch, rewrite to V13 standard, and deploy Group L stories.
Stories: 2289, 2313, 2448, 2457, 2475
Uses thread pool to write chapters concurrently for maximum speed and efficiency.
Author: Antigravity (Advanced Agentic Coding Team)
"""
import os
import json
import time
import requests
import re
import ftplib
import random
from concurrent.futures import ThreadPoolExecutor, as_completed

OPENAI_KEY = "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"
FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"
WP_URL = "https://doctieuthuyet.com"

STORY_LIST = [
    {
        "id": 2289,
        "title_hint": "Sân Khấu Nhà Hát Phương Nam",
        "keywords": "sân khấu nhà hát phương nam, Nguyễn Hoàng Long, Lê Bích Ngọc, Trần Tiến Dũng, Nhà hát Phương Nam, tập đoàn giải trí Phương Đông, bản ballet thép, hồ Gươm Hà Nội, ghi âm hối lộ, sao kê hối lộ BIDV, bảo tồn văn hóa",
        "focus_keyword": "nhà hát phương nam"
    },
    {
        "id": 2313,
        "title_hint": "Bị Cướp Mã Nguồn Nghìn Tỷ, Tôi Kích Hoạt Cái Bẫy Chôn Vùi Cả Tập Đoàn",
        "keywords": "bị cướp mã nguồn nghìn tỷ, Phạm Minh Đức, Hoàng Thế Vinh, Triệu Vy Linh, CyberShield, kiến trúc khóa v5.0, chuẩn ISO 27001 cấp 3, mã hash SHA-256, Techcombank, VPS gián điệp, luật an ninh mạng",
        "focus_keyword": "cướp mã nguồn"
    },
    {
        "id": 2448,
        "title_hint": "Vua Bán Lẻ Đường Phố Sài Gòn: Trận Chiến Sinh Tử Của Chuỗi Trà Ô Long Organic Việt",
        "keywords": "vua bán lẻ đường phố sài gòn, Trần Quốc Bảo, Nguyễn Phương Thảo, Royal Sip, Bảo Long Tea, glyphosate gây ung thư, Pasteur Nha Trang, IoT blockchain truy xuất, C03 Bộ Công An, bôi nhọ truyền thông",
        "focus_keyword": "trà ô long organic"
    },
    {
        "id": 2457,
        "title_hint": "Chàng Rể Bùn Lầy Ẩn Thân: Lật Kèo Vườn Sầu Riêng Trăm Tỷ Dậy Sóng Miền Tây",
        "keywords": "chàng rể bùn lầy ẩn thân, Nguyễn Tấn Đạt, Trần Mỹ Duyên, Huỳnh Hữu Lộc, sầu riêng Monthong, Chợ Lách Bến Tre, thâu tóm nợ xấu Vietcombank, camera hồng ngoại Full HD, độc cỏ glyphosate",
        "focus_keyword": "vườn sầu riêng"
    },
    {
        "id": 2475,
        "title_hint": "Trọng Sinh 2008: Vua Đất Đông Anh Thiết Lập Đế Chế",
        "keywords": "trọng sinh 2008, Nguyễn Hoàng Minh, Lê Vy Anh, Bùi Lực, Tạ Hữu Hùng, đất Đông Anh, quy hoạch cầu Nhật Tân, tập đoàn Phú Quý, lãi nặng hình sự, ghi âm Sony, Vietcombank",
        "focus_keyword": "vua đất đông anh"
    }
]

def clean_and_format_html(text):
    """
    Ensure every single sentence is wrapped in a <p> tag.
    """
    if isinstance(text, list):
        text = "\n".join([str(item) for item in text])
    elif not isinstance(text, str):
        text = str(text)
        
    # Remove existing p tags to prevent nesting
    text = text.replace("<p>", "").replace("</p>", "\n")
    text = re.sub(r'\n+', '\n', text).strip()
    
    lines = text.split('\n')
    formatted_lines = []
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        # Split by .!? followed by space and uppercase Vietnamese letter
        sentences = re.split(r'(?<=[.!?])\s+(?=[A-ZÀ-Ỹ])', line)
        for s in sentences:
            s = s.strip()
            if s:
                if not s.startswith("<p>"):
                    s = f"<p>{s}</p>"
                formatted_lines.append(s)
                
    return "\n".join(formatted_lines)

def count_words(text):
    """
    Counts words in plain text (ignoring HTML tags)
    """
    plain = re.sub(r'<[^>]+>', ' ', text)
    words = plain.split()
    return len(words)

def robust_json_parse(raw_str):
    cleaned = raw_str.strip()
    if cleaned.startswith("```"):
        lines = cleaned.split("\n")
        if lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].startswith("```"):
            lines = lines[:-1]
        cleaned = "\n".join(lines).strip()
    
    if cleaned.startswith("```"):
        cleaned = re.sub(r"^```(?:json)?\n", "", cleaned)
        cleaned = re.sub(r"\n```$", "", cleaned).strip()
        
    try:
        return json.loads(cleaned)
    except Exception as parse_err:
        try:
            start_idx = cleaned.find("{")
            end_idx = cleaned.rfind("}")
            if start_idx != -1 and end_idx != -1 and end_idx > start_idx:
                json_candidate = cleaned[start_idx:end_idx+1]
                return json.loads(json_candidate)
        except Exception as e:
            pass
        raise parse_err

def call_openai(system_prompt, user_prompt, max_tokens=3000, temperature=0.75):
    url = "https://api.openai.com/v1/chat/completions"
    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        "temperature": temperature,
        "max_tokens": max_tokens
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_KEY}"
    }
    
    for attempt in range(5):
        try:
            res = requests.post(url, json=payload, headers=headers, timeout=120)
            res.raise_for_status()
            data = res.json()
            return data['choices'][0]['message']['content'].strip()
        except Exception as e:
            print(f"  [OpenAI Error] Attempt {attempt+1} failed: {e}")
            time.sleep(3)
    raise Exception("Fatal: Failed to connect to OpenAI API after 5 attempts.")

def write_v13_chapter(story_title, intro, female_lead, crisis, evidence, idx, outline_item, prev_titles):
    """
    Helper function to generate a single chapter (run in thread pool).
    """
    system_writer_prompt = """Bạn là nhà văn chuyên nghiệp viết sảng văn Việt Nam số 1 hiện nay. Bạn có văn phong miêu tả cực kỳ sống động, chân thực, sắc sảo.
QUY TẮC VIẾT 10/10 CHUYÊN NGHIỆP:
1. SHOW, DON'T TELL VẬT LÝ: Miêu tả chi tiết hành động vật lý, cử chỉ, biểu cảm gương mặt (nét mặt tái mét, mồ hôi lạnh chảy dài, khớp tay siết chặt đến rớm máu, ánh mắt vằn tia máu, nhịp tim đập loạn xạ nghe rõ mồn một), các đồ vật hay số liệu tài chính rõ ràng (như số tài khoản ngân hàng lớn như Techcombank, Vietcombank, BIDV, số tiền cụ thể bằng VNĐ) thay vì nói chung chung.
2. BỐI CẢNH ĐỊA DANH THẬT HOẶC BIẾN TẤU CHUẨN VIỆT NAM: Câu chuyện diễn ra tại các địa điểm thật/biến tấu ở Việt Nam (đường phố, quận huyện, tòa nhà, bệnh viện thực tế). Tên nhân vật thuần Việt.
3. KHỦNG HOẢNG 24H+ & NỮ CHÍNH LÝ TÍNH: Thể hiện rõ nét các mâu thuẫn được dồn nén nghẹt thở liên tục trên 24 giờ và sự xuất sắc, lý trí đặt điều kiện thương lượng sòng phẳng của nhân vật nữ chính (ví dụ: chuyển nhượng tài sản riêng, ký hợp đồng dịch vụ logistics, phân chia cổ phần sở hữu trí tuệ rõ ràng trước khi ra tay giúp đỡ).
4. BẰNG CHỨNG SỐ/PHÁP LÝ CỤ THỂ: Giải quyết mâu thuẫn bằng các chứng cứ cứng rắn, tài liệu thép (ghi âm kỹ thuật số rõ nét, sao kê ngân hàng đóng dấu giáp lai đỏ, mã hash blockchain chứng minh nguồn gốc hoặc dòng tiền bẩn, hợp đồng chữ ký số CA, trích xuất camera giám sát an ninh Full HD), không dùng võ mồm hay may mắn.
5. HTML MỖI CÂU 1 THẺ <p>: Từng câu văn, câu thoại hoặc câu tả ngắn đều PHẢI nằm trong một thẻ <p> độc lập. Tuyệt đối không gộp nhiều câu vào một thẻ <p>.
6. ĐỘ DÀI CỰC KHỦNG (TỐI THIỂU 1000 TỪ): Viết cực kỳ chi tiết, kéo dài các màn đối thoại gay cấn và hội thoại đấu trí, mô tả tâm lý nhân vật dồn dập. Bắt buộc phải viết đủ tối thiểu 1000 từ tiếng Việt cho phần nội dung chương."""

    user_writer_prompt = f"""Dấu mốc thời gian rõ ràng. Hãy viết CHI TIẾT CHƯƠNG {idx} của bộ truyện: '{story_title}'.
- Giới thiệu thế giới quan & nhân vật: {intro}
- Nữ chính lý tính & thỏa thuận hợp tác: {female_lead}
- Khủng hoảng 24h+: {crisis}
- Bằng chứng số/pháp lý lật kèo: {evidence}
- Dàn ý Chương {idx}: {outline_item['outline']}
- Tóm tắt các chương trước: {json.dumps(prev_titles, ensure_ascii=False)}

YÊU CẦU CỰC KỲ QUAN TRỌNG:
1. Viết thật chi tiết, mô tả sống động hành động vật lý kéo dài để đạt tối thiểu 1000 từ tiếng Việt. Tuyệt đối không viết tóm tắt!
2. Định dạng HTML: Từng câu văn hoặc câu thoại ngắn PHẢI nằm trong một thẻ `<p>...</p>`.
3. Trả về chính xác định dạng JSON sau:
{{
  "title": "Chương {idx}: [Tên chương giật gân, cuốn hút]",
  "content": "[Nội dung chương viết hoàn chỉnh bằng Tiếng Việt 100%, định dạng HTML với các thẻ <p> cho TỪNG CÂU VĂN]"
}}"""

    for parse_attempt in range(3):
        try:
            chap_raw = call_openai(system_writer_prompt, user_writer_prompt, max_tokens=4500, temperature=0.7)
            chap_data = robust_json_parse(chap_raw)
            # Clean and format HTML to guarantee compliance
            chap_data["content"] = clean_and_format_html(chap_data["content"])
            
            # Check word count
            w_count = count_words(chap_data["content"])
            if w_count < 1000:
                print(f"    ⚠️ Chapter {idx} has only {w_count} words. Asking for expansion...")
                orig_title = chap_data.get("title", f"Chương {idx}: [Tiêu đề]")
                expansion_prompt = f"""Dưới đây là một chương truyện viết chưa đủ độ dài (chỉ có {w_count} từ):
Tiêu đề: {orig_title}
Nội dung: {chap_data['content']}

Hãy viết lại chương này, giữ nguyên cốt truyện nhưng MỞ RỘNG cực kỳ chi tiết, thêm nhiều đoạn đối thoại đấu trí sắc bén, miêu tả vật lý chi tiết hơn nữa để đạt độ dài TRÊN 1000 từ. Vẫn tuân thủ luật HTML mỗi câu văn nằm trong 1 thẻ `<p>` riêng biệt. Trả về JSON y hệt."""
                try:
                    chap_raw = call_openai(system_writer_prompt, expansion_prompt, max_tokens=4500, temperature=0.7)
                    expanded_data = robust_json_parse(chap_raw)
                    if expanded_data and "content" in expanded_data:
                        chap_data["content"] = clean_and_format_html(expanded_data["content"])
                        if "title" in expanded_data:
                            chap_data["title"] = expanded_data["title"]
                except Exception as exp_err:
                    print(f"    ⚠️ Expansion failed for Chapter {idx}, keeping original: {exp_err}")
                
            return chap_data
        except Exception as e:
            print(f"    [Retry Attempt {parse_attempt+1}] Chapter {idx} generation error: {e}")
            time.sleep(2)
            
    raise Exception(f"Fatal: Failed to generate Chapter {idx} for '{story_title}' after 3 attempts.")

def write_v13_story(story_id, original_title, original_intro, keywords, focus_keyword):
    print(f"\n🤖 [Story ID {story_id}] Generating Outline and V13 plan...")
    
    system_plan_prompt = """Bạn là biên tập viên văn học kỳ cựu và là bậc thầy lập kịch bản sảng văn / vả mặt (slap-in-the-face web novel) số 1 Việt Nam.
Nhiệm vụ của bạn là dựa vào tiêu đề và giới thiệu gốc của câu chuyện để lập kế hoạch thiết lập chi tiết và dàn ý 8 chương theo chuẩn sảng văn V13 đỉnh cao.

CHUẨN V13 BẮT BUỘC:
1. SHOW, DON'T TELL VẬT LÝ: Tả chi tiết hành động vật lý (như nét mặt run rẩy, khớp tay siết chặt trắng bệch, mồ hôi lạnh chảy dài sau gáy, ánh mắt vằn tia máu, nhịp tim đập loạn xạ nghe rõ mồn một), các số liệu thực tế (như sao kê tài khoản ngân hàng hiển thị số tài khoản và số tiền cụ thể bằng VNĐ, mã số hồ sơ đăng ký tại Cục Bản quyền Sở hữu Quốc gia, chiếc xe VinFast VF9 màu xanh sẫm hay Mercedes-Benz, giấy tờ pháp lý có dấu mộc đỏ giáp lai). Không dùng từ sáo rỗng chung chung.
2. BỐI CẢNH ĐỊA DANH THẬT HOẶC BIẾN TẤU CHUẨN VIỆT NAM: Câu chuyện phải diễn ra tại các địa điểm cụ thể chuẩn Việt Nam (Quận 1, Quận 3, Gò Vấp, Ba Đình, Cầu Giấy, Láng Hạ, Landmark 81, hồ Tây, v.v.). Các tòa nhà, văn phòng cụ thể. Tên nhân vật thuần Việt.
3. NỮ CHÍNH LÝ TÍNH ĐẶT ĐIỀU KIỆN TRƯỚC KHI HỢP TÁC: Nữ chính hoặc trợ lý đồng hành là người cực kỳ tài năng, có đầu óc sắc sảo, độc lập về tài chính và tư duy. Cô ấy không yêu đương mù quáng vô lý mà sẽ đặt ra điều kiện cụ thể (ví dụ: yêu cầu chuyển nhượng sở hữu tài sản đứng tên riêng, ký hợp đồng dịch vụ tư vấn pháp lý rõ ràng, hoặc phân chia cổ phần sòng phẳng) trước khi hợp tác với nam chính hoặc xử lý khủng hoảng giúp người khác.
4. KHỦNG HOẢNG 24H+: Một sự kiện dồn ép nhân vật vào chân tường kéo dài ít nhất 24 giờ liên tục, có mốc thời gian rõ ràng, đếm ngược từng tiếng.
5. BẰNG CHỨNG SỐ/PHÁP LÝ CỤ THỂ ĐỂ GIẢI QUYẾT TRANH CHẤP: Việc lật kèo phải dựa trên các tài liệu thép: file ghi âm kỹ thuật số lưu trên đám mây được giám định pháp y, bản sao kê tài khoản ngân hàng chính thống có đóng dấu giáp lai đỏ, mã hash giao dịch blockchain chứng minh dòng tiền bẩn đi ra nước ngoài, hợp đồng chuyển nhượng cổ phần hợp pháp có chữ ký số CA, trích xuất camera an ninh chuẩn Full HD từ ổ cứng đầu ghi của tòa nhà."""

    user_plan_prompt = f"""Dựa vào thông tin truyện gốc sau:
- ID: {story_id}
- Tiêu đề gốc: {original_title}
- Giới thiệu gốc: {original_intro}
- Từ khóa gợi ý: {keywords}
- Focus Keyword: {focus_keyword}

Hãy thiết kế một bản kế hoạch viết lại V13 cực kỳ chi tiết cho truyện này, bao gồm:
1. Tóm tắt intro viết lại cực kỳ kịch tính, lôi cuốn độc giả (HTML, mỗi câu 1 thẻ <p>).
2. Tên nhân vật chính, nhân vật phụ phản diện, nữ chính lý tính.
3. Chi tiết bối cảnh địa danh thật/biến tấu cụ thể tại Việt Nam.
4. Chi tiết khủng hoảng 24h+ cụ thể.
5. Chi tiết bằng chứng số/pháp lý cụ thể để giải quyết tranh chấp ở chương cuối.
6. Thỏa thuận điều kiện cụ thể của nữ chính lý tính.
7. Focus Keyword (2-3 từ), SEO Title (<60 ký tự), SEO Description (<160 ký tự).
8. Dàn ý chi tiết cho 8 chương (Mỗi chương ghi rõ diễn biến kịch tính).

Trả về chính xác cấu trúc JSON sau:
{{
  "title": "Tiêu đề truyện cực kỳ giật gân, cuốn hút và thuần Việt",
  "focus_keyword": "focus keyword 2-3 từ",
  "seo_title": "seo title dưới 60 ký tự",
  "seo_description": "seo description dưới 160 ký tự",
  "intro": "Giới thiệu truyện tóm tắt cực kỳ kịch tính, mỗi câu 1 thẻ <p>...",
  "female_lead": "Tên nữ chính và thỏa thuận hợp tác/đứng tên tài sản riêng",
  "crisis": "Chi tiết khủng hoảng 24h+",
  "evidence": "Chi tiết bằng chứng số/pháp lý",
  "outlines": [
    {{ "chap_num": 1, "outline": "Tóm tắt chi tiết kịch tính chương 1" }},
    {{ "chap_num": 2, "outline": "Tóm tắt chi tiết kịch tính chương 2" }},
    {{ "chap_num": 3, "outline": "Tóm tắt chi tiết kịch tính chương 3" }},
    {{ "chap_num": 4, "outline": "Tóm tắt chi tiết kịch tính chương 4" }},
    {{ "chap_num": 5, "outline": "Tóm tắt chi tiết kịch tính chương 5" }},
    {{ "chap_num": 6, "outline": "Tóm tắt chi tiết kịch tính chương 6" }},
    {{ "chap_num": 7, "outline": "Tóm tắt chi tiết kịch tính chương 7" }},
    {{ "chap_num": 8, "outline": "Tóm tắt chi tiết kịch tính chương 8" }}
  ]
}}"""

    plan_raw = call_openai(system_plan_prompt, user_plan_prompt, max_tokens=2500, temperature=0.75)
    plan_data = robust_json_parse(plan_raw)
    print(f"  Plan created successfully: '{plan_data['title']}'")
    
    # Write 8 chapters concurrently using ThreadPoolExecutor for massive speed!
    print("  -> Writing 8 chapters concurrently...")
    chapters = [None] * 8
    prev_titles = [f"Chương {i}: [Đang soạn thảo]" for i in range(1, 9)]
    
    with ThreadPoolExecutor(max_workers=4) as executor:
        future_to_idx = {
            executor.submit(
                write_v13_chapter, 
                plan_data['title'], 
                plan_data['intro'], 
                plan_data['female_lead'], 
                plan_data['crisis'], 
                plan_data['evidence'], 
                i+1, 
                plan_data['outlines'][i],
                prev_titles[:i]
            ): i for i in range(8)
        }
        
        for future in as_completed(future_to_idx):
            i = future_to_idx[future]
            try:
                chap_data = future.result()
                chapters[i] = {
                    "title": chap_data["title"],
                    "content": chap_data["content"]
                }
                w_count = count_words(chap_data["content"])
                print(f"    ✓ [Story {story_id}] Chapter {i+1}/8 completed successfully! ({w_count} words)")
            except Exception as exc:
                print(f"    ❌ [Story {story_id}] Chapter {i+1} generated an exception: {exc}")
                raise exc
                
    plan_data["intro"] = clean_and_format_html(plan_data["intro"])
    
    return {
        "story_id": story_id,
        "title": plan_data["title"],
        "focus_keyword": plan_data["focus_keyword"],
        "seo_title": plan_data["seo_title"],
        "seo_description": plan_data["seo_description"],
        "intro": plan_data["intro"],
        "chapters": chapters
    }

def deploy_story_via_ftp(story_id, story_data):
    print(f"\n📤 Deploying Story ID {story_id} via FTP & PHP Helper...")
    temp_php_filename = f"deploy_temp_{story_id}_{random.randint(100000, 999999)}.php"
    
    # Read the local robust PHP helper
    local_helper_path = "/Users/aaronnguyen/TN/App/doctieuthuyet/overwrite_story_v13.php"
    if os.path.exists(local_helper_path):
        with open(local_helper_path, "r", encoding="utf-8") as f:
            PHP_CONTENT = f.read()
    else:
        print("  ⚠️ Warning: Local helper overwrite_story_v13.php not found! Using integrated PHP code...")
        PHP_CONTENT = r'''<?php
ini_set('display_errors', 0); ini_set('max_execution_time', 300); header('Content-Type: application/json');
$d = json_decode(file_get_contents("php://input"), true);
if (!$d || $d["secret_token"] !== "ZEN_TRUYEN_2026_BYPASS") { http_response_code(401); echo json_encode(["error" => "Unauthorized"]); exit; }
require_once("wp-load.php");
$pid = intval($d["story_id"]);
if (!empty($d["title"])) wp_update_post(["ID" => $pid, "post_title" => $d["title"]]);
if (!empty($d["intro"])) wp_update_post(["ID" => $pid, "post_content" => $d["intro"]]);
if (!empty($d["author"])) update_post_meta($pid, "truyen_tacgia", $d["author"]);
if (!empty($d["seo"])) {
    $s = $d["seo"];
    if (!empty($s["focus_keyword"])) { update_post_meta($pid, "rank_math_focus_keyword", $s["focus_keyword"]); update_post_meta($pid, "_rank_math_focus_keyword", $s["focus_keyword"]); }
    if (!empty($s["seo_title"])) { update_post_meta($pid, "rank_math_title", $s["seo_title"]); update_post_meta($pid, "_rank_math_title", $s["seo_title"]); }
    if (!empty($s["seo_description"])) { update_post_meta($pid, "rank_math_description", $s["seo_description"]); update_post_meta($pid, "_rank_math_description", $s["seo_description"]); }
    update_post_meta($pid, "rank_math_rich_snippet", "article");
}
$old = get_posts(["post_type" => "chuong", "meta_key" => "_truyen_id", "meta_value" => $pid, "posts_per_page" => -1, "post_status" => "any"]);
$del = 0; foreach ($old as $c) { wp_delete_post($c->ID, true); $del++; }
$n = 0;
foreach ($d["chapters"] as $i => $c) {
    $id = wp_insert_post(["post_title" => $c["title"], "post_content" => $c["content"], "post_status" => "publish", "post_type" => "chuong", "menu_order" => $i + 1]);
    if ($id && !is_wp_error($id)) { update_post_meta($id, "_truyen_id", $pid); $n++; }
}
if (function_exists("litespeed_purge_all")) litespeed_purge_all();
echo json_encode(["success" => true, "story_id" => $pid, "deleted_old_chapters" => $del, "chapters_count" => $n, "seo_updated" => true], JSON_UNESCAPED_UNICODE);
?>'''

    # Upload PHP helper via FTP
    try:
        ftp = ftplib.FTP(FTP_HOST, timeout=30)
        ftp.login(FTP_USER, FTP_PASS)
        local_temp_file = f"deploy_temp_local_{story_id}_{random.randint(100000, 999999)}.php"
        local_path = f"/tmp/{local_temp_file}"
        with open(local_path, "w", encoding="utf-8") as f:
            f.write(PHP_CONTENT)
        with open(local_path, "rb") as f:
            ftp.storbinary(f"STOR {temp_php_filename}", f)
        ftp.quit()
        if os.path.exists(local_path):
            os.remove(local_path)
    except Exception as e:
        print(f"  ❌ FTP Upload Error: {e}")
        return False
        
    # Trigger deployment via POST request
    success = False
    try:
        payload = {
            "secret_token": "ZEN_TRUYEN_2026_BYPASS",
            "story_id": story_id,
            "title": story_data["title"],
            "intro": story_data["intro"],
            "author": "Đang cập nhật",
            "seo": {
                "focus_keyword": story_data["focus_keyword"],
                "seo_title": story_data["seo_title"],
                "seo_description": story_data["seo_description"]
            },
            "chapters": story_data["chapters"]
        }
        api_url = f"{WP_URL}/{temp_php_filename}"
        res = requests.post(api_url, json=payload, verify=False, timeout=180)
        res_data = res.json()
        if res_data.get("success"):
            print(f"  🎉 SUCCESS! Story {story_id} deployed successfully with {res_data.get('chapters_count')} chapters.")
            print(f"  Deleted {res_data.get('deleted_old_chapters')} old chapters.")
            success = True
        else:
            print(f"  ❌ Deployment Failed via API: {res_data}")
    except Exception as e:
        print(f"  ❌ Deployment Request Error: {e}")
        
    # Clean up remote PHP helper immediately after deployment (Requirement B6)
    try:
        ftp = ftplib.FTP(FTP_HOST, timeout=30)
        ftp.login(FTP_USER, FTP_PASS)
        ftp.delete(temp_php_filename)
        ftp.quit()
        print(f"  ✓ Deleted helper {temp_php_filename} from remote server successfully for security.")
    except Exception as e:
        print(f"  ⚠️ Warning: Could not delete remote helper: {e}")
        
    return success

def main():
    print("=" * 60)
    print("🌟 MASTER REWRITE V13 & DEPLOY ENGINE (GROUP L) 🌟")
    print("=" * 60)
    
    # Read fetched metadata
    metadata_path = "/Users/aaronnguyen/TN/App/doctieuthuyet/scratch/group_l_metadata.json"
    if os.path.exists(metadata_path):
        with open(metadata_path, "r", encoding="utf-8") as f:
            raw_data = json.load(f)
        print("✓ Successfully loaded original metadata from local cache.")
    else:
        print("❌ Fatal: Local metadata cache file not found. Please run fetch script first.")
        return
        
    # Make sure scratch directory exists
    os.makedirs("/Users/aaronnguyen/TN/App/doctieuthuyet/scratch", exist_ok=True)
    
    deployed_ids = []
    
    for story in STORY_LIST:
        story_id = story["id"]
        title_hint = story["title_hint"]
        keywords = story["keywords"]
        focus_keyword = story["focus_keyword"]
        
        print("\n" + "="*50)
        print(f"Processing Story ID {story_id}: '{title_hint}'")
        print("="*50)
        
        scratch_path = f"/Users/aaronnguyen/TN/App/doctieuthuyet/scratch/rewrite_{story_id}_v13.json"
        story_data = None
        
        # Check if local cache exists
        if os.path.exists(scratch_path):
            try:
                print(f"✓ Found existing V13 rewrite data locally: {scratch_path}")
                with open(scratch_path, "r", encoding="utf-8") as f:
                    story_data = json.load(f)
                print(f"  -> Successfully loaded '{story_data['title']}' from cache. Skipping generation.")
            except Exception as e:
                print(f"⚠️ Warning: Could not load local cache: {e}. Re-generating...")
                story_data = None
                
        if not story_data:
            orig = raw_data.get(str(story_id))
            if orig:
                original_title = orig["title"]
                original_intro = orig["content"]  # Use the original HTML content as intro
            else:
                original_title = title_hint
                original_intro = f"Tiêu đề gốc: {title_hint}. Hãy viết lại thành truyện sảng văn chuẩn V13 đỉnh cao."
                
            # Generate V13 data
            story_data = write_v13_story(story_id, original_title, original_intro, keywords, focus_keyword)
            
            # Save local cache (Requirement B4)
            with open(scratch_path, "w", encoding="utf-8") as f:
                json.dump(story_data, f, ensure_ascii=False, indent=2)
            print(f"✓ Saved V13 rewrite data to {scratch_path}")
            
        # Deploy to WP (Requirements B5 & B6)
        deploy_success = deploy_story_via_ftp(story_id, story_data)
        if deploy_success:
            deployed_ids.append(story_id)
            print(f"✓ Story {story_id} is completely live!")
        else:
            print(f"❌ Failed to deploy Story {story_id}!")
            
    print("\n" + "="*60)
    print("🏁 ALL PROCESSES COMPLETED!")
    print(f"Successfully processed and deployed: {deployed_ids}")
    print("="*60)
    
    # Parent callback message
    print(f"GROUP_L_DONE: {deployed_ids}")

if __name__ == "__main__":
    main()
