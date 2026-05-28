# -*- coding: utf-8 -*-
import json
import os
import time
import requests
import ftplib
import re

OPENAI_KEY = "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"
FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"
WP_URL = "https://doctieuthuyet.com"
STORY_ID = 5200

# Strict V13 Chapter Outline for Chàng Rể Nuôi Tôm Hùm
CHAPTER_OUTLINES = [
    {
        "chap_num": 1,
        "title": "Chương 1: Ngày Bị Trục Xuất Khỏi Đầm Vịnh Vũng Rô",
        "outline": "Mở đầu kịch tính với cảnh Phong đứng trong căn nhà gỗ ven đầm Vũng Rô, đôi ủng cao su hôi hám còn dính rong biển. Mẹ vợ là bà Mai lớn tiếng nhục mạ, ném đơn ly hôn ép anh cút đi tay trắng. Người vợ Vy lặng câm, tay bấu chiếc túi hiệu Chanel mà thiếu gia Vinh tặng. Vinh - kẻ thừa kế Thịnh Phát kiêu ngạo bước vào cười nhạo Phong chỉ là tên ngư dân nghèo nàn, ăn cắp bí quyết vi sinh của tập đoàn gã. Phong không thèm cãi vã, ký đơn dứt khoát rồi rời đi dưới cơn bão gầm rú. Anh đã bảo mật toàn bộ mã nguồn giống tôm bằng khóa PGP số và Git commit bất biến từ trước."
    },
    {
        "chap_num": 2,
        "title": "Chương 2: Người Đồng Hành Lý Tính Và Bản Hợp Đồng Tỷ Đô",
        "outline": "Phong đến gặp Lê Thị Ngọc Diệp - Phó Giám đốc Sở Thủy sản Phú Yên kiêm đại diện Quỹ đầu tư Vạn An tại văn phòng Đông Tác. Diệp là nữ CEO/thạc sĩ cực kỳ thông minh, lý tính và sòng phẳng. Cô thẩm định cẩn thận các nghiên cứu của Phong, không tin vào những lời quảng bá sáo rỗng. Khi Phong trình bày các biểu đồ vi sinh nước ao sạch hơn 10 lần tự nhiên và chứng minh bản quyền Git commit, Diệp lập tức nhận ra cơ hội. Cô đề xuất hợp đồng đầu tư 100 tỷ đồng với điều kiện: mẫu tôm đầu tiên phải vượt qua cuộc audit kiểm định sinh học khắt khe của SGS."
    },
    {
        "chap_num": 3,
        "title": "Chương 3: Thử Thách Men Vi Sinh Và Sự Khẳng Định Vượt Trội",
        "outline": "Buổi kiểm định độc lập của SGS diễn ra tại Tuy Hòa dưới sự giám sát của hai chuyên gia người Pháp và Ngọc Diệp. Hoàng Thế Vinh và mẹ vợ cũ cũng kéo đến để xem Phong thất bại nhục nhã. Phong điềm tĩnh lấy ra hạt men vi sinh sinh học đặc chủng MR3, tiến hành đo các chỉ số độ mặn và xử lý bồn tôm nhiễm bệnh đốm trắng. Kết quả đo sinh học hiển thị tỷ lệ sống sót đạt 98%, tôm hùm bơi lội khỏe mạnh. SGS đóng dấu đỏ xác nhận tiêu chuẩn vàng. Vinh mặt trắng bệch không còn giọt máu, lắp bắp khi biết công nghệ này vượt trội hoàn toàn so với AgroChem của gã. Diệp kiêu hãnh ký bản hợp đồng 100 tỷ."
    },
    {
        "chap_num": 4,
        "title": "Chương 4: Khủng Hoảng Đêm Bão Và Đòn Bẩn Từ Đối Thủ",
        "outline": "Cú sốc giữa truyện cực kỳ căng thẳng. Biết Phong thắng thế, Hoàng Thế Vinh thuê côn đồ đột nhập khu lồng bè đầm Vũng Rô trong đêm bão lớn, đổ hàng chục thùng hóa chất tẩy Clo nồng độ cao làm chết trắng 10 tấn tôm hùm. Đồng thời gã chi tiền thuê KOL bẩn livestream bôi nhọ Phong đầu độc môi trường. Cục Thủy sản lập tức đình chỉ cơ sở Phong 24 giờ. Agribank phong tỏa tài khoản của anh. Đối tác đòi nợ kéo đến đập phá. Diệp đứng ra bảo trợ, chuyển khẩn cấp 20 tỷ từ Quỹ Vạn An để đền bù xoa dịu ngư dân. Phong vẫn tĩnh lặng như nước vì camera ẩn hồng ngoại chạy năng lượng mặt trời của anh đã ghi lại toàn bộ khuôn mặt nhóm côn đồ đang gọi điện cho Vinh."
    },
    {
        "chap_num": 5,
        "title": "Chương 5: Trận Chiến Cứu Sinh Mạng Đêm Hoàng Hôn",
        "outline": "Cựu Thứ trưởng Bộ Thủy sản (ông nội Diệp) đột quỵ do sốc tim khi nghe tin đầm vịnh bị đầu độc. Ông rơi vào trạng thái suy tim phổi cấp, huyết áp tụt sâu còn 50 mmHg, các bác sĩ đầu ngành bất lực. Diệp hoảng sợ tột cùng kêu cứu Phong. Phong dùng y thuật châm cứu các huyệt Nhân Trung, Nội Quan, Kỳ Môn kết hợp sử dụng dịch chiết gan tôm hùm bông giàu astaxanthin tinh khiết cực mạnh. Bác sĩ Tây y ban đầu phẫn nộ ngăn cản, nhưng Diệp gánh trách nhiệm. Chỉ sau 10 phút, monitor điện tâm đồ phục hồi sóng nhịp tim 72 lần/phút ổn định. Kết quả men tim lâm sàng phục hồi hoàn toàn khiến y bác sĩ bàng hoàng thán phục."
    },
    {
        "chap_num": 6,
        "title": "Chương 6: Cuộc Nói Chuyện Riêng Tư Và Bản Đính Ước Thầm Lặng",
        "outline": "Cảnh lãng mạn bình yên sau giông bão. Phong và Diệp đi dạo trên bè gỗ nuôi tôm hùm Vũng Rô dưới ánh hoàng hôn rực đỏ như lửa. Tiếng gót giày cao gót của Diệp cộp nhẹ trên thớ gỗ sũng nước mặn. Diệp trút bỏ vẻ nữ tổng tài sắc lạnh, bày tỏ sự ngưỡng mộ và lòng biết ơn chân thành. Họ đối thoại sâu sắc về định hướng chấn hưng thủy sản sạch của Việt Nam. Diệp chủ động nắm chặt tay Phong, trao lời đính ước sòng phẳng cùng nhau thâu tóm Thịnh Phát. Bức tranh hoàng hôn biển cả chứng giám cho tình yêu sắc sảo, kiên cường của họ."
    },
    {
        "chap_num": 7,
        "title": "Chương 7: Vòng Vây Bằng Chứng Và Lệnh Còng Tay Từ C03",
        "outline": "Đại hội cổ đông và lễ ký kết IPO định giá 1000 tỷ của Thịnh Phát tại khách sạn Sheraton Sài Gòn hoành tráng. Vinh và Mai tự đắc ăn mừng chiến thắng. Đúng lúc Vinh chuẩn bị đặt bút ký, Phong cùng Diệp và các chiến sĩ Cục Cảnh sát điều tra tội phạm kinh tế C03 ập vào. Họ trưng ra lệnh bắt khẩn cấp và phong tỏa tài sản. Diệp trình chiếu video hồng ngoại ẩn ghi hình nhóm côn đồ đầu độc tôm và sao kê chuyển khoản của Vinh. Phong công khai bản quyền Git commit SHA-256 có khóa PGP. Vinh sợ hãi bủn rủn, hai đầu gối quỵ xuống sàn granite kêu cộp. Mẹ vợ cũ Mai mồ hôi lạnh chảy ròng ròng, đánh rơi túi Chanel rách nát. Handcuffs click đóng lại."
    },
    {
        "chap_num": 8,
        "title": "Chương 8: Ván Bài Lật Ngược, Thâu Tóm Tập Đoàn Và Ngày Chiến Thắng",
        "outline": "Quỹ Vạn An thâu tóm toàn bộ Thịnh Phát với giá rẻ mạt sau khi cổ phiếu sụp đổ trắng bên mua. Thương hiệu tôm hùm hữu cơ Vũng Rô đạt chứng nhận OCOP 5 sao quốc gia xuất khẩu đi Nhật Bản và châu Âu mang lại doanh thu hàng ngàn tỷ. Bà Mai và Vy nợ nần chồng chất phải làm thuê dọn vỏ tôm ở quán vỉa hè trong hối hận tột độ. Trong buổi tiệc vinh quang lộng lẫy tại Landmark 81, Diệp mặc đầm sapphire kiêu sa, ôm chặt Phong và trao nụ hôn nồng cháy dưới pháo hoa rực rỡ và tiếng chúc tụng của giới tài phiệt."
    }
]

def call_openai(system_prompt, user_prompt, max_tokens=4000, temperature=0.75):
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
            res = requests.post(url, json=payload, headers=headers, timeout=180)
            res.raise_for_status()
            data = res.json()
            return data['choices'][0]['message']['content'].strip()
        except Exception as e:
            print(f"  [Attempt {attempt+1}/5] OpenAI call error: {e}")
            time.sleep(6 * (attempt + 1))
    raise Exception("Fatal: Failed to contact OpenAI API sequentially.")

def clean_json_response(raw_str):
    cleaned = raw_str.strip()
    if cleaned.startswith("```"):
        cleaned = re.sub(r"^```(?:json)?\n", "", cleaned)
        cleaned = re.sub(r"\n```$", "", cleaned).strip()
    try:
        return json.loads(cleaned)
    except Exception as e:
        start_idx = cleaned.find("{")
        end_idx = cleaned.rfind("}")
        if start_idx != -1 and end_idx != -1 and end_idx > start_idx:
            try:
                return json.loads(cleaned[start_idx:end_idx+1])
            except:
                pass
        raise e

def count_words(html_content):
    # Strip HTML tags
    clean = re.sub(r'<[^>]+>', ' ', html_content)
    words = clean.strip().split()
    return len(words)

def main():
    print("=" * 60)
    print("🌟 PERFECT 10/10 SEQUENTIAL WEBNOVEL COMPILER & AUTO-PUBLISHER 🌟")
    print("=" * 60)
    print(f"Target Novel ID: {STORY_ID}")
    print("Genre: Sảng Văn (Vả Mặt)")
    
    novel_data = {
        "story_id": STORY_ID,
        "title": "Chàng Rể Nuôi Tôm Hùm Bị Gia Đình Vợ Khinh Rẻ, Lật Kèo Thâu Tóm Tập Đoàn Thủy Sản Nghìn Tỷ",
        "author": "Trần Hải Phong",
        "genre": "Sảng Văn",
        "intro": """<p><strong>"Một thằng ngư dân quèn đi ủng cao su hôi hám như mày cả đời cũng không ngóc đầu lên nổi! Mau ký đơn ly hôn rồi cút khỏi đầm vịnh Vũng Rô ngay!"</strong></p>
<p>Trần Hải Phong, một kỹ sư nuôi trồng thủy sản kiêm bác sĩ y học cổ truyền tài ba, bỗng dưng bị gia tộc bên vợ sỉ nhục, vu oan đầu độc nguồn nước để ép anh ra đi tay trắng. Chúng muốn cướp đoạt toàn bộ bí quyết phối trộn thức ăn vi sinh đặc chủng giúp tôm hùm bông kháng bệnh để dâng cho Hoàng Thế Vinh - thiếu gia tập đoàn xuất khẩu Thịnh Phát nhằm chuẩn bị cho đợt IPO trăm tỷ.</p>
<p>Bị đuổi khỏi nhà vợ, lồng tôm bị đầu độc làm tôm chết hàng loạt, tài khoản Agribank bị phong tỏa, đối thủ dùng KOL bẩn bôi nhọ trên livestream. Thế nhưng, chúng không ngờ Hải Phong đã âm thầm bảo mật toàn bộ nhật ký thí nghiệm giống tôm và quy trình kiểm định sinh học bằng mã hóa Git commit gốc. Với sự bảo trợ của Lê Thị Ngọc Diệp - Phó Giám đốc Sở Thủy sản và tài lực từ Quỹ đầu tư Vạn An, Hải Phong vùng lên thực hiện cú lật kèo chấn động, thâu tóm toàn bộ đế chế đối thủ.</p>""",
        "seo": {
            "focus_keyword": "chàng rể nuôi tôm hùm",
            "seo_title": "Chàng Rể Nuôi Tôm Hùm Lật Kèo Thâu Tóm Tập Đoàn Nghìn Tỷ",
            "seo_description": "Truyện sảng văn Chàng Rể Nuôi Tôm Hùm cực hay. Từ kẻ đi ủng cao su bị nhà vợ đuổi đi, anh lật kèo ngoạn mục thâu tóm đế chế thủy sản nghìn tỷ."
        },
        "chapters": []
    }
    
    system_writer_prompt = """Bạn là THE GHOSTWRITER - Nhà văn truyện mạng sảng văn/vả mặt số 1 Việt Nam. Bạn nổi tiếng với lối viết chân thực, giàu cảm xúc, dẫn truyện chậm rãi chi tiết và đẩy cao trào vô cùng nghẹt thở.

QUY TẮC CỐT LÕI ĐỂ ĐẠT 10/10 ĐIỂM CHUYÊN MÔN:
1. DUNG LƯỢNG KHỦNG (TỐI THIỂU 1200 TỪ): Bạn bắt buộc phải triển khai chương vô cùng chi tiết, không được tóm tắt. Hãy viết thật chậm, mô tả chi tiết từng hành động nhỏ, biểu cảm khuôn mặt, cảnh quan thiên nhiên và đối thoại kéo dài sâu sắc giữa các nhân vật. Nội dung chương phải dài ít nhất 1200 từ đến 1600 từ.
2. SHOW, DON'T TELL: Thay vì dùng tính từ rỗng tuếch như "vô cùng tức giận", "sốc tột độ". Hãy miêu tả phản ứng vật lý chân thực của cơ thể:
   - "Mồ hôi lạnh chảy ròng ròng ướt đẫm gáy áo sơ mi đắt tiền."
   - "Hai gối bủn rủn, quỵ rạp xuống nền đá hoa cương lạnh toát kêu cộp."
   - "Ngón tay run rẩy bấu chặt vào mép bàn gỗ gõ đỏ đến mức móng tay rỉ ra vệt máu tươi."
   - "Sắc mặt xám ngoét như tro tàn, môi trắng bệch cắt không còn giọt máu."
3. CHI TIẾT NGÀNH NGHỀ & PHÁP LÝ THẬT TẠI VIỆT NAM:
   - Sử dụng các thuật ngữ và kiến thức nuôi tôm hùm thực tế (nồng độ oxy đáy, vi sinh MR3, dịch chiết astaxanthin, PCR kiểm định giống của Cục Thú y, audit độc lập của SGS).
   - Cơ cấu kinh doanh thực tế: IPO, sao kê ngân hàng Agribank đóng dấu đỏ, video camera ẩn hồng ngoại, khóa PGP và nhật ký commit Git gốc bảo mật bất biến, thâu tóm thù địch (hostile takeover), Cục Cảnh sát điều tra tội phạm kinh tế C03 Bộ Công an.
4. HỘI THOẠI CỰC ĐỈNH: Các câu thoại sắc lạnh thể hiện rõ nét sự sỉ nhục hách dịch của phản diện và sự tĩnh lặng, thâm sâu vô bờ bến của nam chính Hải Phong.
5. ĐỊNH DẠNG: Chỉ sử dụng các thẻ HTML cơ bản như <p>, <strong>, <em>. Tuyệt đối không lặp lại tiêu đề chương bên trong nội dung. Không thêm bất kỳ ghi chú hay văn bản thừa nào ngoài JSON.

JSON mẫu bắt buộc trả về:
{
  "title": "[Tên chương giật gân, cuốn hút]",
  "content": "<p>Nội dung chi tiết...</p>"
}"""

    # Generate each chapter sequentially
    for i, outline_item in enumerate(CHAPTER_OUTLINES, 1):
        print(f"\n✍️ [CHAPTER {i}/{len(CHAPTER_OUTLINES)}] Generating: {outline_item['title']}...")
        
        # Prepare context of the previous chapter to maintain perfect continuity
        prev_context = ""
        if novel_data["chapters"]:
            last_chap = novel_data["chapters"][-1]
            prev_context = f"""- DANH SÁCH CÁC CHƯƠNG ĐÃ QUA: {[c['title'] for c in novel_data['chapters']]}
- NỘI DUNG CHI TIẾT CHƯƠNG TRƯỚC ĐÓ ({last_chap['title']}) - ĐỌC KỸ ĐỂ NỐI TIẾP VĂN PHONG VÀ CHI TIẾT LIỀN MẠCH, TRÁNH LẶP Ý HOẶC TRÙNG LẶP:
\"\"\"
{last_chap['content']}
\"\"\"
"""
        
        user_prompt = f"""DỰA TRÊN THÔNG TIN TÁC PHẨM:
- Tựa truyện: {novel_data['title']}
- Tác giả: {novel_data['author']}
- Giới thiệu chung: {novel_data['intro']}

- Chương cần viết: {outline_item['title']}
- Dàn ý chi tiết của chương này: {outline_item['outline']}

BẮT BUỘC NGỮ CẢNH TRƯỚC ĐÓ (NẾU CÓ):
{prev_context}

YÊU CẦU ĐẶC BIỆT VỀ ĐỘ DÀI:
Nội dung HTML trong "content" phải cực kỳ dài, chi tiết và sinh động, tối thiểu 1200 từ tiếng Việt trở lên (khoảng 7000 đến 10000 ký tự bao gồm khoảng trắng). Hãy mô tả kỹ lưỡng hành vi, cử chỉ, tâm lý và các đoạn đối thoại kịch tính dài hơi để đạt tiêu chuẩn độ dài này. Cấm tóm tắt!

HÃY TRẢ VỀ DẠNG JSON CHUẨN:
{{
  "title": "{outline_item['title']}",
  "content": "Nội dung chương viết hoàn chỉnh bằng Tiếng Việt 100%, định dạng HTML với các thẻ <p>, <strong>, <em>..."
}}"""
        
        # Call API
        chap_raw = call_openai(system_writer_prompt, user_prompt, max_tokens=4000, temperature=0.78)
        
        try:
            chap_data = clean_json_response(chap_raw)
            word_count = count_words(chap_data["content"])
            print(f"  -> ✓ Successfully generated. Word count: {word_count} words ({len(chap_data['content'])} chars)")
            
            # If word count is still a bit short, we warn but append. Let's make sure it is rich.
            novel_data["chapters"].append({
                "title": chap_data["title"],
                "content": chap_data["content"]
            })
        except Exception as e:
            print(f"  -> ⚠️ Parser error: {e}. Trying backup regex extraction...")
            title_match = re.search(r'"title"\s*:\s*"(.*?)"', chap_raw)
            content_match = re.search(r'"content"\s*:\s*"(.*)"', chap_raw, re.DOTALL)
            if title_match and content_match:
                title_ext = title_match.group(1)
                content_ext = content_match.group(1).replace('\\"', '"').replace('\\n', '\n').replace('\\t', '\t')
                novel_data["chapters"].append({
                    "title": title_ext,
                    "content": content_ext
                })
                print(f"  -> ✓ Recovered via backup regex extraction. Length: {len(content_ext)} chars")
            else:
                print("Raw Response was:")
                print(chap_raw[:2000])
                raise SystemExit("Fatal: Could not parse or recover chapter JSON.")
        
        # Sleep to avoid rate limiting
        time.sleep(3)

    # Save draft locally
    local_draft_path = "scratch/tom_hum_perfect_draft.json"
    with open(local_draft_path, "w", encoding="utf-8") as f:
        json.dump(novel_data, f, ensure_ascii=False, indent=2)
    print(f"\n✓ Saved perfect draft locally to {local_draft_path}")

    # 4. Upload overwrite_story_v13.php via FTP
    print("\n📤 Uploading overwrite_story_v13.php helper to remote root via FTP...")
    try:
        ftp = ftplib.FTP(FTP_HOST, timeout=60)
        ftp.login(FTP_USER, FTP_PASS)
        with open("overwrite_story_v13.php", "rb") as f:
            ftp.storbinary("STOR overwrite_story_v13.php", f)
        print("✓ Uploaded overwrite_story_v13.php.")
        ftp.quit()
    except Exception as e:
        print("❌ FTP Upload Error:", e)
        return

    # 5. POST to overwrite_story_v13.php
    print("\n🔗 Triggering overwrite request via API call...")
    payload = {
        "secret_token": "ZEN_TRUYEN_2026_BYPASS",
        "story_id": STORY_ID,
        "title": novel_data["title"],
        "intro": novel_data["intro"],
        "author": novel_data["author"],
        "chapters": novel_data["chapters"],
        "seo": novel_data["seo"]
    }
    
    try:
        api_url = f"{WP_URL}/overwrite_story_v13.php"
        headers = {"Content-Type": "application/json"}
        # Allow 5 minutes for remote execution
        res = requests.post(api_url, json=payload, headers=headers, timeout=300)
        res_data = res.json()
        
        if res_data.get('success'):
            print("=" * 60)
            print("🎉 NOVEL OVERWRITTEN SUCCESSFULLY ON THE LIVE SITE!")
            print(f"Story ID: {res_data['story_id']}")
            print(f"Title: {res_data['title']}")
            print(f"Author: {res_data['author']}")
            print(f"Old Chapters Deleted: {res_data['deleted_old_chapters']}")
            print(f"New Chapters Published: {res_data['chapters_count']}")
            print(f"SEO Metadata Updated: {res_data['seo_updated']}")
            print("=" * 60)
        else:
            print("❌ Failed to overwrite:", res_data)
            
    except Exception as e:
        print("❌ API Call Error:", e)

    # 6. Delete helper script from remote via FTP for security
    print("\n🧹 Cleaning up remote helper script...")
    try:
        ftp = ftplib.FTP(FTP_HOST, timeout=60)
        ftp.login(FTP_USER, FTP_PASS)
        ftp.delete("overwrite_story_v13.php")
        print("✓ Deleted remote overwrite_story_v13.php for security.")
        ftp.quit()
    except Exception as e:
        print("⚠️ Note: Could not delete remote overwrite_story_v13.php:", e)

if __name__ == "__main__":
    main()
