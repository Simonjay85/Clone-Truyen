#!/usr/bin/env python3
import re

filepath = "/Users/aaronnguyen/TN/App/doctieuthuyet/scratch/rewrite_and_deploy_group_i.py"

with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
    content = f.read()

# We can replace using regex or exact string matching
# Let's locate the first occurrences of the function write_v13_chapter and def write_v13_story
# And remove the garbage in between.

pattern = r'def write_v13_chapter\(story_title, intro, female_lead, crisis, evidence, idx, outline_item, prev_titles\):.*?(def write_v13_story\(story_id, original_title, original_intro, keywords, focus_keyword\):)'

clean_function = """def write_v13_chapter(story_title, intro, female_lead, crisis, evidence, idx, outline_item, prev_titles):
    \"\"\"
    Helper function to generate a single chapter (run in thread pool).
    \"\"\"
    system_writer_prompt = \"\"\"Bạn là nhà văn chuyên nghiệp viết sảng văn Việt Nam số 1 hiện nay. Bạn có văn phong miêu tả cực kỳ sống động, chân thực, sắc sảo.
QUY TẮC VIẾT 10/10 CHUYÊN NGHIỆP:
1. SHOW, DON'T TELL VẬT LÝ: Miêu tả chi tiết hành động vật lý, cử chỉ, biểu cảm gương mặt (nét mặt tái mét, mồ hôi lạnh chảy dài, khớp tay siết chặt đến rớm máu, ánh mắt vằn tia máu, nhịp tim đập loạn xạ nghe rõ mồn một), các đồ vật hay số liệu tài chính rõ ràng (như số tài khoản, số tiền cụ thể bằng VNĐ tại Việt Thương Bank/Kỹ Thương Bank) thay vì nói chung chung.
2. BỐI CẢNH ĐỊA DANH THẬT HOẶC BIẾN TẤU CHUẨN VIỆT NAM: Câu chuyện diễn ra tại các địa điểm thật/biến tấu ở Việt Nam (đường phố, quận huyện, tòa nhà, bệnh viện thực tế). Tên nhân vật thuần Việt.
3. KHỦNG HOẢNG 24H+ & NỮ CHÍNH LÝ TÍNH: Thể hiện rõ nét các mâu thuẫn được dồn nén nghẹt thở liên tục trên 24 giờ và sự xuất sắc, lý trí đặt điều kiện thương lượng sòng phẳng của nhân vật nữ chính (ví dụ: chuyển nhượng tài sản riêng, ký hợp đồng dịch vụ, phân chia cổ phần trước khi ra tay giúp đỡ).
4. BẰNG CHỨNG SỐ/PHÁP LÝ CỤ THỂ: Giải quyết mâu thuẫn bằng các chứng cứ cứng rắn, tài liệu thép (ghi âm, sao kê ngân hàng đóng dấu giáp lai, mã hash blockchain, hợp đồng CA chữ ký số), không dùng võ mồm hay may mắn.
5. HTML MỖI CÂU 1 THẺ <p>: Từng câu văn, câu thoại hoặc câu tả ngắn đều PHẢI nằm trong một thẻ <p> độc lập. Tuyệt đối không gộp nhiều câu vào một thẻ <p>.
6. ĐỘ DÀI CỰC KHỦNG (TỐI THIỂU 1000 TỪ): Viết cực kỳ chi tiết, kéo dài các màn đối thoại gay cấn và hội thoại đấu trí, mô tả tâm lý nhân vật dồn dập. Bắt buộc phải viết đủ tối thiểu 1000 từ tiếng Việt cho phần nội dung chương.\"\"\"

    user_writer_prompt = f\"\"\"Dấu mốc thời gian rõ ràng. Hãy viết CHI TIẾT CHƯƠNG {idx} của bộ truyện: '{story_title}'.
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
}}\"\"\"

    for parse_attempt in range(3):
        try:
            chap_raw = call_openai(system_writer_prompt, user_writer_prompt, max_tokens=4500, temperature=0.7)
            raw_data = robust_json_parse(chap_raw)
            chap_data = normalize_chapter_data(raw_data)
            
            # Clean and format HTML to guarantee compliance
            chap_data["content"] = clean_and_format_html(chap_data["content"])
            
            # Check word count
            w_count = count_words(chap_data["content"])
            if w_count < 1000:
                print(f"    ⚠️ Chapter {idx} has only {w_count} words. Asking for expansion...")
                expansion_prompt = f\"\"\"Dưới đây là một chương truyện viết chưa đủ độ dài (chỉ có {w_count} từ):
Tiêu đề: {chap_data['title']}
Nội dung: {chap_data['content']}

Hãy viết lại chương này, giữ nguyên cốt truyện nhưng MỞ RỘNG cực kỳ chi tiết, thêm nhiều đoạn đối thoại đấu trí sắc bén, miêu tả vật lý chi tiết hơn nữa để đạt độ dài TRÊN 1000 từ. Vẫn tuân thủ luật HTML mỗi câu văn nằm trong 1 thẻ `<p>` riêng biệt. Trả về JSON y hệt.\"\"\"
                chap_raw = call_openai(system_writer_prompt, expansion_prompt, max_tokens=4500, temperature=0.7)
                raw_data_expanded = robust_json_parse(chap_raw)
                chap_data_expanded = normalize_chapter_data(raw_data_expanded)
                chap_data["content"] = clean_and_format_html(chap_data_expanded["content"])
                if chap_data_expanded["title"]:
                    chap_data["title"] = chap_data_expanded["title"]
                
            return chap_data
        except Exception as e:
            print(f"    [Retry Attempt {parse_attempt+1}] Chapter {idx} generation error: {e}")
            time.sleep(2)
            
    raise Exception(f"Fatal: Failed to generate Chapter {idx} for '{story_title}' after 3 attempts.")

"""

new_content, count = re.subn(pattern, clean_function + "\n\\1", content, flags=re.DOTALL)
print(f"Substituted: {count}")

with open(filepath, "w", encoding="utf-8") as f:
    f.write(new_content)
print("Saved cleaned file successfully.")
