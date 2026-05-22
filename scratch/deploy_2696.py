import os
import json
import time
import requests
import re
import ftplib
import urllib.parse
import random

OPENAI_KEY = "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"
FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"
WP_URL = "https://doctieuthuyet.com"

STORY_ID = 2696
TITLE_HINT = "Nhà Chồng Khinh Tôi Không Biết Nấu Ăn, Tôi Giật Giải Đầu Bếp Michelin"

def clean_and_format_html(text):
    text = text.replace("<p>", "").replace("</p>", "\n")
    text = re.sub(r'\n+', '\n', text).strip()
    
    lines = text.split('\n')
    formatted_lines = []
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        sentences = re.split(r'(?<=[.!?])\s+', line)
        for s in sentences:
            s = s.strip()
            if s:
                if not s.startswith("<p>"):
                    s = f"<p>{s}</p>"
                formatted_lines.append(s)
                
    return "\n".join(formatted_lines)

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

def call_openai(system_prompt, user_prompt, max_tokens=3000, temperature=0.7):
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
            time.sleep(5)
    raise Exception("Fatal: Failed to connect to OpenAI API after 5 attempts.")

def fetch_original_story(story_id):
    url = f"{WP_URL}/wp-json/wp/v2/truyen/{story_id}"
    try:
        res = requests.get(url, verify=False, timeout=30)
        if res.status_code == 200:
            data = res.json()
            title = data.get('title', {}).get('rendered', '')
            intro = data.get('content', {}).get('rendered', '')
            print(f"✓ Successfully fetched original story {story_id}: {title}")
            return {"title": title, "intro": intro}
    except Exception as e:
        print(f"⚠️ Warning: Could not fetch original story {story_id} from WP API. Error: {e}")
    return None

def get_chapter_data(system_prompt, user_prompt):
    for attempt in range(3):
        try:
            chap_raw = call_openai(system_prompt, user_prompt, max_tokens=4500, temperature=0.7)
            try:
                return robust_json_parse(chap_raw)
            except Exception as parse_err:
                print(f"      [Parse Error] Attempt {attempt+1} robust_json_parse failed, trying regex fallback...")
                
                title_match = re.search(r'"title"\s*:\s*"(.*?)"', chap_raw)
                content_match = re.search(r'"content"\s*:\s*"(.*)"', chap_raw, re.DOTALL)
                
                if title_match and content_match:
                    content_str = content_match.group(1).strip()
                    if content_str.endswith('"}') or content_str.endswith('"} '):
                        content_str = content_str[:-2]
                    elif content_str.endswith('"') and not content_str.endswith('\\"'):
                        content_str = content_str[:-1]
                    
                    content_str = content_str.replace('\\"', '"').replace('\\n', '\n').replace('\\t', '\t')
                    return {
                        "title": title_match.group(1),
                        "content": content_str
                    }
                print(f"      [Parse Error] Regex fallback also failed. Retrying OpenAI call...")
        except Exception as e:
            print(f"      [OpenAI/Parse Error] {e}")
            time.sleep(3)
    raise Exception("Fatal: Failed to generate chapter after 3 retries.")

def write_v13_story(story_id, original_title, original_intro):
    print(f"🤖 Generating V13 content for Story ID {story_id}...")
    
    system_plan_prompt = """Bạn là biên tập viên văn học kỳ cựu và là bậc thầy lập kịch bản sảng văn / vả mặt (slap-in-the-face web novel) số 1 Việt Nam.
Nhiệm vụ của bạn là dựa vào tiêu đề và giới thiệu gốc của câu chuyện để lập kế hoạch thiết lập chi tiết và dàn ý 8 chương theo chuẩn sảng văn V13 đỉnh cao.

CHUẨN V13 BẮT BUỘC:
1. SHOW, DON'T TELL VẬT LÝ: Tả chi tiết hành động vật lý (như nét mặt run rẩy, khớp tay siết chặt trắng bệch, mồ hôi lạnh chảy dài sau gáy, ánh mắt vằn tia máu, nhịp tim đập loạn xạ nghe rõ mồn một), các số liệu thực tế (như sao kê tài khoản Techcombank/Vietcombank hiển thị số tài khoản và số tiền cụ thể bằng VNĐ, mã số hồ sơ đăng ký tại Cục Sở hữu Trí tuệ Việt Nam, chiếc xe VinFast VF9 màu xanh sẫm hay Mercedes-Benz S450 biển số Hà Nội 30F-..., giấy tờ pháp lý có dấu mộc đỏ giáp lai). Không dùng từ sáo rỗng chung chung.
2. BỐI CẢNH ĐỊA DANH THẬT VIỆT NAM: Câu chuyện phải diễn ra tại các địa điểm có thật ở Việt Nam như đường phố Hà Nội (Cầu Giấy, Hoàn Kiếm, Long Biên, Mỹ Đình), TP.HCM (Phú Mỹ Hưng Quận 7, Landmark 81, Quận 1), Hải Phòng (cảng Đình Vũ, Đồ Sơn), v.v. Các tòa nhà, văn phòng cụ thể. Tên nhân vật thuần Việt (ví dụ: Lê Mai, Cao Hùng, Minh Nguyệt, v.v.).
3. NỮ CHÍNH LÝ TÍNH ĐẶT ĐIỀU KIỆN TRƯỚC KHI HỢP TÁC: Nữ chính hoặc trợ lý đồng hành là người cực kỳ tài năng, có đầu óc sắc sảo, độc lập về tài chính và tư duy. Cô ấy không yêu đương mù quáng vô lý mà sẽ đặt ra điều kiện cụ thể (ví dụ: yêu cầu chuyển nhượng 20% lợi nhuận ròng của chuỗi nhà hàng mới, sở hữu thương hiệu cá nhân độc lập, tự chủ hoàn toàn ban điều hành bếp) trước khi hợp tác với nam chính/nữ chính.
4. KHỦNG HOẢNG 24H+: Một sự kiện dồn ép nhân vật vào chân tường kéo dài ít nhất 24 giờ liên tục, có mốc thời gian rõ ràng, đếm ngược từng tiếng (ví dụ: 24 giờ trước khi diễn ra sự kiện công bố cẩm nang ẩm thực Michelin Guide Việt Nam, nhà chồng cũ đâm đơn kiện đòi bồi thường 10 tỷ đồng và niêm phong nhà hàng của cô).
5. BẰNG CHỨNG SỐ/PHÁP LÝ CỤ THỂ ĐỂ GIẢI QUYẾT TRANH CHẤP: Việc lật kèo phải dựa trên các tài liệu thép: file ghi âm kỹ thuật số lưu trên iCloud được giám định pháp y, bản sao kê tài khoản ngân hàng chính thống có đóng dấu giáp lai đỏ, mã hash giao dịch blockchain chứng minh dòng tiền bẩn đi ra nước ngoài, hợp đồng chuyển nhượng cổ phần hợp pháp có chữ ký số CA, trích xuất camera an ninh chuẩn Full HD từ ổ cứng đầu ghi của tòa nhà có biên bản niêm phong của công an quận.
6. ĐỊA BÀN VÀ NHÂN VẬT THUẦN VIỆT."""

    user_plan_prompt = f"""Dựa vào thông tin truyện gốc sau:
- ID: {story_id}
- Tiêu đề gốc: {original_title}
- Giới thiệu gốc: {original_intro}

Hãy thiết kế một bản kế hoạch viết lại V13 cực kỳ chi tiết cho truyện này, bao gồm:
1. Tóm tắt intro viết lại cực kỳ kịch tính, lôi cuốn độc giả (HTML, mỗi câu 1 thẻ <p>).
2. Tên nhân vật chính Lê Mai, chồng cũ Cao Hùng, mẹ chồng Hà Thịnh, đối tác lý tính/nam chính.
3. Chi tiết bối cảnh địa danh thật cụ thể tại Việt Nam.
4. Chi tiết khủng hoảng 24h+ cụ thể.
5. Chi tiết bằng chứng số/pháp lý cụ thể để giải quyết tranh chấp ở chương cuối.
6. Thỏa thuận điều kiện cụ thể của nữ chính lý tính Lê Mai.
7. Focus Keyword (2-3 từ), SEO Title (<60 ký tự), SEO Description (<160 ký tự).
8. Dàn ý chi tiết cho 8 chương (Mỗi chương ghi rõ diễn biến kịch tính).

Trả về chính xác cấu trúc JSON sau (không chứa văn bản thừa bên ngoài):
{{
  "title": "Tiêu đề truyện cực kỳ giật gân, cuốn hút và thuần Việt",
  "focus_keyword": "focus keyword 2-3 từ",
  "seo_title": "seo title dưới 60 ký tự",
  "seo_description": "seo description dưới 160 ký tự",
  "intro": "Giới thiệu truyện tóm tắt cực kỳ kịch tính, mỗi câu 1 thẻ <p>...",
  "female_lead": "Tên nữ chính và thỏa thuận hợp tác",
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
    
    print(f"  Outline created successfully for: {plan_data['title']}")
    
    chapters = []
    
    for idx in range(1, 9):
        print(f"  -> Writing Chapter {idx}/8...")
        outline_item = plan_data['outlines'][idx-1]
        
        system_writer_prompt = """Bạn là nhà văn chuyên nghiệp viết sảng văn Việt Nam số 1 hiện nay. Bạn có văn phong miêu tả cực kỳ sống động, chân thực, sắc sảo.
QUY TẮC VIẾT 10/10 CHUYÊN NGHIỆP:
1. SHOW, DON'T TELL VẬT LÝ: Miêu tả chi tiết hành động vật lý, cử chỉ, biểu cảm gương mặt (nét mặt tái mét, mồ hôi lạnh chảy dài, khớp tay siết chặt đến rớm máu, ánh mắt vằn tia máu, nhịp tim đập loạn xạ nghe rõ mồn một), các đồ vật hay số liệu tài chính rõ ràng thay vì nói chung chung.
2. BỐI CẢNH ĐỊA DANH THẬT VIỆT NAM: Câu chuyện diễn ra tại các địa điểm thật ở Việt Nam (đường phố, quận huyện, tòa nhà, bệnh viện thực tế). Tên nhân vật thuần Việt.
3. KHỦNG HOẢNG 24H+ & NỮ CHÍNH LÝ TÍNH: Thể hiện rõ nét các mâu thuẫn được dồn nén nghẹt thở liên tục trên 24 giờ và sự xuất sắc, lý trí đặt điều kiện rõ ràng của nhân vật nữ chính.
4. BẰNG CHỨNG SỐ/PHÁP LÝ CỤ THỂ: Giải quyết mâu thuẫn bằng các chứng cứ cứng rắn, không dùng võ mồm hay may mắn.
5. ĐỊA BÀN VÀ NHÂN VẬT THUẦN VIỆT.
6. HTML MỖI CÂU 1 THẺ <p>: Từng câu văn, câu thoại hoặc câu tả ngắn đều PHẢI nằm trong một thẻ <p> độc lập. Tuyệt đối không gộp nhiều câu vào một thẻ <p>.
7. ĐỘ DÀI CỰC KHỦNG (TỐI THIỂU 1000 TỪ): Viết cực kỳ chi tiết, diễn giải sâu sắc tâm lý nhân vật, kéo dài các màn đối đầu kịch tính và hội thoại gay cấn. Không viết tóm tắt! Bắt buộc phải viết đủ tối thiểu 1000 từ tiếng Việt cho phần nội dung chương.
8. LƯU Ý BẢO MẬT JSON: Chỉ trả về mã JSON chuẩn, không sử dụng ký tự xuống dòng thô không được escape trong chuỗi, không sử dụng dấu ngoặc kép thừa trong thuộc tính."""

        user_writer_prompt = f"""Dựa trên kế hoạch truyện sau:
- Tựa truyện: {plan_data['title']}
- Giới thiệu thế giới quan & nhân vật: {plan_data['intro']}
- Nữ chính lý tính & thỏa thuận: {plan_data['female_lead']}
- Khủng hoảng 24h+: {plan_data['crisis']}
- Bằng chứng số/pháp lý: {plan_data['evidence']}

Hãy viết CHI TIẾT CHƯƠNG {idx} của bộ truyện.
- Dàn ý Chương {idx}: {outline_item['outline']}
{f"- Các chương trước đã viết tóm tắt: {json.dumps([c['title'] for c in chapters], ensure_ascii=False)}" if chapters else ""}

YÊU CẦU CỰC KỲ QUAN TRỌNG:
1. Viết chi tiết, dài dòng, đầy kịch tính để đạt tối thiểu 1000 từ tiếng Việt. Tuyệt đối không viết tóm tắt!
2. Định dạng HTML: Từng câu văn hoặc câu thoại ngắn PHẢI nằm trong một thẻ `<p>...</p>`.
3. Trả về chính xác định dạng JSON sau (không chứa văn bản thừa bên ngoài):
{{
  "title": "Chương {idx}: [Tên chương giật gân, cuốn hút]",
  "content": "[Nội dung chương viết hoàn chỉnh bằng Tiếng Việt 100%, định dạng HTML với các thẻ <p> cho TỪNG CÂU VĂN]"
}}"""

        chap_data = get_chapter_data(system_writer_prompt, user_writer_prompt)
        
        chap_data["content"] = clean_and_format_html(chap_data["content"])
        
        chapters.append({
            "title": chap_data["title"],
            "content": chap_data["content"]
        })
        print(f"     ✓ Finished Chapter {idx}: {chap_data['title']} ({len(chap_data['content'])} chars)")
        time.sleep(2)
        
    plan_data["intro"] = clean_and_format_html(plan_data["intro"])
    
    result = {
        "post_id": story_id,
        "title": plan_data["title"],
        "focus_keyword": plan_data["focus_keyword"],
        "seo_title": plan_data["seo_title"],
        "seo_description": plan_data["seo_description"],
        "intro": plan_data["intro"],
        "chapters": chapters
    }
    
    return result

def deploy_story_via_ftp(story_id, story_data):
    print(f"📤 Deploying Story ID {story_id} via FTP & PHP Bypass...")
    
    temp_php_filename = f"deploy_temp_{story_id}_{random.randint(100000, 999999)}.php"
    
    PHP_CONTENT = r'''<?php
require_once("wp-load.php");header("Content-Type: application/json");
$d=json_decode(file_get_contents("php://input"),true);
if(!$d||$d["secret"]!=="ZEN_TRUYEN_2026_BYPASS"){echo json_encode(["error"=>"Unauthorized"]);exit;}
$pid=intval($d["post_id"]);
if(!empty($d["intro"]))wp_update_post(["ID"=>$pid,"post_content"=>$d["intro"]]);
if(!empty($d["focus_keyword"]))update_post_meta($pid,"rank_math_focus_keyword",$d["focus_keyword"]);
if(!empty($d["seo_title"]))update_post_meta($pid,"rank_math_title",$d["seo_title"]);
if(!empty($d["seo_description"]))update_post_meta($pid,"rank_math_description",$d["seo_description"]);
update_post_meta($pid,"rank_math_robots",["index","follow"]);
$old=get_posts(["post_type"=>"chuong","meta_key"=>"_truyen_id","meta_value"=>$pid,"posts_per_page"=>100,"post_status"=>"any"]);
foreach($old as $c)wp_delete_post($c->ID,true);
$n=0;
foreach($d["chapters"] as $i=>$c){
$id=wp_insert_post(["post_title"=>$c["title"],"post_content"=>$c["content"],"post_status"=>"publish","post_type"=>"chuong","menu_order"=>$i+1]);
if($id&&!is_wp_error($id)){update_post_meta($id,"_truyen_id",$pid);update_post_meta($id,"_chapter_number",$i+1);$n++;}
}
update_post_meta($pid,"_chapter_count",$n);
if(function_exists("litespeed_purge_all"))litespeed_purge_all();
echo json_encode(["success"=>true,"published"=>$n]);
?>'''

    try:
        ftp = ftplib.FTP(FTP_HOST, timeout=30)
        ftp.login(FTP_USER, FTP_PASS)
        
        local_temp_path = f"/Users/aaronnguyen/TN/App/doctieuthuyet/scratch/{temp_php_filename}"
        with open(local_temp_path, "w", encoding="utf-8") as f:
            f.write(PHP_CONTENT)
            
        with open(local_temp_path, "rb") as f:
            ftp.storbinary(f"STOR {temp_php_filename}", f)
            
        print(f"  ✓ Uploaded temporary PHP endpoint: {temp_php_filename}")
        ftp.quit()
    except Exception as e:
        print(f"  ❌ FTP Upload Error: {e}")
        return False
        
    success = False
    try:
        payload = {
            "secret": "ZEN_TRUYEN_2026_BYPASS",
            "post_id": story_id,
            "intro": story_data["intro"],
            "focus_keyword": story_data["focus_keyword"],
            "seo_title": story_data["seo_title"],
            "seo_description": story_data["seo_description"],
            "chapters": story_data["chapters"]
        }
        
        api_url = f"{WP_URL}/{temp_php_filename}"
        print(f"  👉 Sending POST request to {api_url}...")
        
        res = requests.post(api_url, json=payload, verify=False, timeout=120)
        res_data = res.json()
        
        if res_data.get("success"):
            print(f"  🎉 SUCCESS! Story {story_id} deployed successfully with {res_data.get('published')} chapters.")
            success = True
        else:
            print(f"  ❌ Deployment Failed via API: {res_data}")
    except Exception as e:
        print(f"  ❌ Deployment Request Error: {e}")
        
    try:
        ftp = ftplib.FTP(FTP_HOST, timeout=30)
        ftp.login(FTP_USER, FTP_PASS)
        ftp.delete(temp_php_filename)
        print(f"  ✓ Deleted remote temporary PHP endpoint: {temp_php_filename}")
        ftp.quit()
    except Exception as e:
        print(f"  ⚠️ Warning: Could not delete remote temporary PHP endpoint {temp_php_filename}: {e}")
        
    try:
        os.remove(local_temp_path)
    except:
        pass
        
    return success

def main():
    print("=" * 60)
    print(f"🌟 REWRITE V13 & DEPLOY ENGINE FOR STORY {STORY_ID} 🌟")
    print("=" * 60)
    
    os.makedirs("/Users/aaronnguyen/TN/App/doctieuthuyet/scratch", exist_ok=True)
    
    orig_data = fetch_original_story(STORY_ID)
    if orig_data:
        original_title = orig_data["title"]
        original_intro = orig_data["intro"]
    else:
        original_title = TITLE_HINT
        original_intro = f"Tiêu đề gốc: {TITLE_HINT}. Hãy viết lại thành truyện sảng văn chuẩn V13 đỉnh cao."
        
    story_data = write_v13_story(STORY_ID, original_title, original_intro)
    
    scratch_path = f"/Users/aaronnguyen/TN/App/doctieuthuyet/scratch/rewrite_{STORY_ID}_v13.json"
    with open(scratch_path, "w", encoding="utf-8") as f:
        json.dump(story_data, f, ensure_ascii=False, indent=2)
    print(f"✓ Saved V13 rewrite data to {scratch_path}")
    
    deploy_success = deploy_story_via_ftp(STORY_ID, story_data)
    if deploy_success:
        print(f"✓ Story {STORY_ID} is completely processed and live!")
    else:
        print(f"❌ Failed to deploy Story {STORY_ID}!")

if __name__ == "__main__":
    main()
