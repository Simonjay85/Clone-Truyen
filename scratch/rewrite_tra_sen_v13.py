import os
import json
import time
import requests
import re
import sys

CLAUDE_KEY = "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"
OPENAI_KEY = "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"

STORY_ID = 3633
STORY_TITLE = "Nghệ Nhân Trà Sen Bị Khinh Rẻ Trục Xuất, Lật Kèo Đêm Hội Trà Quốc Tế Đưa Kẻ Phản Bội Vào Tù"
FOCUS_KEYWORD = "trà sen Tây Hồ"

def clean_and_split_sentences(content):
    """
    Cleans HTML tags and wraps every single sentence in exactly one <p>...</p> tag.
    Ensures that empty/redundant lines are removed.
    """
    # Remove existing <p> and </p> tags
    text = content.replace("<p>", "").replace("</p>", "").strip()
    
    # Split text into sentences by looking for sentence-ending punctuation (. ! ?) followed by whitespace
    sentences = re.split(r'(?<=[.!?])\s+', text)
    
    formatted = []
    for s in sentences:
        s = s.strip()
        if s:
            formatted.append(f"<p>{s}</p>")
            
    return "\n".join(formatted)

def call_claude(system_prompt, user_prompt, max_tokens=4000, temperature=0.7):
    url = "https://api.anthropic.com/v1/messages"
    headers = {
        "content-type": "application/json",
        "x-api-key": CLAUDE_KEY,
        "anthropic-version": "2023-06-01"
    }
    payload = {
        "model": "claude-sonnet-4-6",
        "max_tokens": max_tokens,
        "system": system_prompt,
        "messages": [
            {"role": "user", "content": user_prompt}
        ],
        "temperature": temperature
    }
    for attempt in range(5):
        try:
            res = requests.post(url, json=payload, headers=headers, timeout=120)
            res.raise_for_status()
            data = res.json()
            return data['content'][0]['text'].strip()
        except Exception as e:
            print(f"⚠️ Claude Call Error (Attempt {attempt+1}): {e}")
            if 'res' in locals():
                print("Response:", res.text)
            time.sleep(5)
            
    # Fallback to OpenAI gpt-4o-mini if Claude fails completely (e.g. quota exhausted)
    print("⚠️ Fallback to OpenAI gpt-4o-mini active...")
    return call_openai(system_prompt, user_prompt, max_tokens, temperature)

def call_openai(system_prompt, user_prompt, max_tokens=4000, temperature=0.7):
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
            print(f"⚠️ OpenAI Call Error (Attempt {attempt+1}): {e}")
            time.sleep(5)
    raise Exception("Fatal: Failed to connect to both Claude and OpenAI APIs after multiple attempts.")

def generate_outline():
    return {
        "title": "Nghệ Nhân Trà Sen Bị Khinh Rẻ Trục Xuất, Lật Kèo Đêm Hội Trà Quốc Tế Đưa Kẻ Phản Bội Vào Tù",
        "intro": "<p>Đêm mưa bão tại đầm sen Tây Hồ Quảng An, nghệ nhân trà trẻ tuổi Duy Anh chịu đựng sự sỉ nhục tột cùng.</p>\n<p>Lê Hoài Nam, CEO của Trà Hoài Nam Corp, cấu kết với mụ Lan để tịch thu đầm sen di sản và trục xuất anh không thương tiếc.</p>\n<p>Giữa lúc tuyệt vọng, Duy Anh gặp gỡ Lâm Khánh Chi, CFO sắc sảo của quỹ đầu tư Vạn An Capital.</p>\n<p>Không có sự thương hại vô lý, họ thiết lập một thỏa thuận sòng phẳng 100 tỷ đổi lấy 30% cổ phần để phục hưng trà sen Bách Diệp Tây Hồ cổ truyền.</p>\n<p>Bằng sự kết hợp giữa kỹ thuật sắc ký khí ghép khối phổ GC-MS, bài thuốc y học Đông y Liên Diệp Cam Thảo cổ truyền, và sự vào cuộc quyết liệt của Cảnh sát điều tra C03, Duy Anh đã lật kèo ngoạn mục ngay tại Đêm hội trà quốc tế, đưa kẻ phản bội vào tù.</p>",
        "outlines": [
            {
                "chap_num": 1,
                "outline": "Cảnh bão táp tại đầm sen Tây Hồ cổ truyền Quảng An. Duy Anh chứng kiến cảnh Lê Hoài Nam (CEO Trà Hoài Nam Corp) cùng mụ Lan đắc ý tuyên bố trục xuất Duy Anh khỏi đầm sen di sản gia truyền. Duy Anh nắm chặt khớp ngón tay phát ra tiếng rắc khe khẽ, mồ hôi gáy lạnh toát rịn ra đầm đìa làm ướt sũng lưng áo, nhưng anh vẫn im lặng thu dọn hành lý. Anh thề sẽ phục hận đêm hội trà quốc tế."
            },
            {
                "chap_num": 2,
                "outline": "Lâm Khánh Chi, CFO sắc sảo của quỹ đầu tư Vạn An Capital, gặp gỡ Duy Anh tại quán trà cổ bên Hồ Tây. Không có sự thương hại hay tình cảm mù quáng, Lâm Khánh Chi đưa ra thỏa thuận thương mại sòng phẳng: quỹ Vạn An Capital sẽ rót vốn 100 tỷ đồng đổi lấy 30% cổ phần của hợp tác xã để xây dựng phòng thí nghiệm hiện đại và phục hồi thương hiệu Trà sen Bách Diệp cổ truyền. Duy Anh đồng ý, hai bên ký kết hợp đồng sòng phẳng."
            },
            {
                "chap_num": 3,
                "outline": "Lê Hoài Nam cấu kết với thanh tra bẩn Trần Văn Bản ban hành quyết định niêm phong đầm sen của Duy Anh và phong tỏa tài khoản Vietcombank của hợp tác xã. Những tin đồn thất thiệt trà sen bị nhiễm độc chì lan truyền dồn dập trên mạng xã hội khiến xã viên hoang mang, người dân phẫn nộ đòi bồi thường. Duy Anh cùng Lâm Khánh Chi bình tĩnh đối phó, bắt đầu hành trình thu thập chứng cứ pháp lý kỹ thuật độc lập kéo dài hơn 24 giờ."
            },
            {
                "chap_num": 4,
                "outline": "Duy Anh sử dụng hệ thống sắc ký khí ghép khối phổ (GC-MS) tiên tiến tại phòng thí nghiệm của Vạn An Capital để phân tích mẫu trà Modern Lotus bán chạy của Lê Hoài Nam. Kết quả GC-MS phát hiện hàm lượng chất tạo hương nhân tạo độc hại Ethyl Vanillin vượt ngưỡng an toàn cho phép gấp 5 lần nhằm đánh lừa người dùng bằng hương thơm sen giả tạo. Lâm Khánh Chi lưu trữ tất cả kết quả phân tích và lập hồ sơ báo cáo lên Cảnh sát điều tra tội phạm C03."
            },
            {
                "chap_num": 5,
                "outline": "Đêm hội trà quốc tế long trọng khai mạc tại khách sạn 5 sao cạnh Hồ Tây. Lê Hoài Nam cùng bè lũ cực kỳ ngạo nghễ, trưng bày sản phẩm trà Modern Lotus của mình như biểu tượng mới của trà Việt. Duy Anh lặng lẽ chuẩn bị một bàn trà cổ truyền nhỏ ở góc khuất, sử dụng nước giếng cổ đun sôi bằng than củi đỏ rực và những đóa sen Bách Diệp hái lúc tinh sương tại đầm Quảng An, hương sen dịu mát lan tỏa khác biệt hoàn toàn với mùi hóa chất nồng nặc của Modern Lotus."
            },
            {
                "chap_num": 6,
                "outline": "Ngài Pierre Laurent, Đại sứ Pháp và là một chuyên gia ẩm thực danh tiếng, đột ngột lên cơn co thắt phế quản cấp tính ngay tại Đêm hội do dị ứng với hương liệu hóa học từ gian hàng của Lê Hoài Nam. Giữa lúc mọi người hoảng loạn, Duy Anh bình tĩnh bước tới, áp dụng kỹ thuật bấm huyệt Nội Quan và Nhân Trung để khai thông phế khí, đồng thời cho ngài Đại sứ uống ấm nước thuốc 'Liên Diệp Cam Thảo' nóng hổi vừa sắc khẩn cấp. Cơn hen dịu hẳn, huyết áp của ngài Đại sứ ổn định trở lại trong sự thán phục của toàn bộ quan khách quốc tế."
            },
            {
                "chap_num": 7,
                "outline": "Sau khi hồi phục, Đại sứ Pierre Laurent đích thân kiểm chứng chén trà sen Tây Hồ Bách Diệp do Duy Anh pha bằng nước giếng cổ. Sự thuần khiết và thanh tao tuyệt đối khiến ngài thốt lên lời khen ngợi vô giá. Đúng lúc này, Lâm Khánh Chi bước lên sân khấu chính, công bố toàn bộ kết quả phân tích GC-MS về chất độc Ethyl Vanillin trong trà của Hoài Nam, cùng bảng sao kê dòng tiền hối lộ thanh tra bẩn Trần Văn Bản từ Vietcombank của Lê Hoài Nam do kiểm toán Big 4 xác minh."
            },
            {
                "chap_num": 8,
                "outline": "Sắc mặt Lê Hoài Nam xám ngoét như tro tàn, cơ mặt giật liên hồi, mồ hôi hột rịn ra đầm đìa, chân run lẩy bẩy không đứng vững. Các chiến sĩ thuộc Cảnh sát điều tra tội phạm C03 bước vào hội trường, đọc lệnh bắt khẩn cấp Lê Hoài Nam và mụ Lan về tội đầu độc người tiêu dùng và đưa hối lộ. Hợp tác xã trà sen Tây Hồ Bách Diệp của Duy Anh được giải tỏa niêm phong, mở rộng quy mô sản xuất ra quốc tế dưới sự đồng hành của Vạn An Capital."
            }
        ]
    }


def generate_chapter(story_title, outline, chap_num, total_chaps, prev_chapters):
    system_prompt = """Bạn là nhà văn mạng sảng văn vả mặt số 1 Việt Nam. Bạn có văn phong miêu tả cực kỳ sống động, chân thực, sắc sảo và kịch tính nghẹt thở.
Hãy viết chương truyện dài từ 1000 - 1500 từ theo tóm tắt chương.
YÊU CẦU BẮT BUỘC CHUẨN V13:
1. Show don't tell vật lý: miêu tả cơ mặt giật nhẹ, mồ hôi gáy lạnh toát rịn ra làm ướt đẫm áo, khớp ngón tay siết chặt phát ra tiếng rắc khe khẽ, móng tay bấu rỉ máu đỏ tươi, tiếng thở khò khè dồn dập. Tránh hoàn toàn các tính từ sáo rỗng cảm xúc như "vô cùng tức giận", "kinh hoàng", "hoảng sợ".
2. Địa danh thật chuẩn xác tại Việt Nam: Đầm sen Tây Hồ, phường Quảng An, quận Tây Hồ, Hà Nội.
3. Nữ chính lý tính thương lượng sòng phẳng: Lâm Khánh Chi, CFO sắc sảo của Vạn An Capital, đàm phán hợp đồng 100 tỷ lấy 30% cổ phần sòng phẳng trên các điều khoản thương mại rõ ràng chứ không cứu giúp vô điều kiện.
4. Tình huống khủng hoảng nặng nề kéo dài trên 24 giờ: niêm phong đầm sen, phong tỏa tài khoản Vietcombank của hợp tác xã, tin đồn độc chì bôi nhọ dồn dập trên mạng.
5. Chứng cứ kỹ thuật/pháp lý/số liệu rõ ràng, thực tế: kết quả phân tích sắc ký khí ghép khối phổ (GC-MS) chứng minh chất tạo hương Ethyl Vanillin trong trà Modern Lotus của Lê Hoài Nam vượt ngưỡng gấp 5 lần gây nguy hại tim mạch; sao kê hối lộ, kiểm toán Big 4, quyết định của Cảnh sát điều tra tội phạm (C03).
6. Nghi thức pha trà cổ truyền: pha trà bằng nước giếng cổ đun sôi bằng than củi, mùi hương sen bách diệp thanh cao, nhẹ dịu lan tỏa thư thái khác biệt hoàn toàn với hóa chất nhân tạo.
7. Y học Đông y: Duy Anh cấp cứu co thắt phế quản cấp tính cho ngài Đại sứ Pháp Pierre Laurent bằng bấm huyệt Nội Quan, Nhân Trung kết hợp bài thuốc Liên Diệp Cam Thảo phơi khô nấu ấm hạ áp khẩn cấp.
8. Mỗi câu văn bắt buộc phải nằm trong một cặp thẻ <p>...</p>. Không được gộp nhiều câu vào một dòng. Ví dụ:
<p>Duy Anh chèo chiếc thuyền gỗ luồn lách qua những lá sen khổng lồ.</p>
<p>Lòng bàn tay anh rịn một lớp mồ hôi mỏng, lạnh ngắt.</p>
<p>Anh ngước mắt nhìn bóng người đang đứng trên cầu gỗ.</p>

Hãy trả về JSON nguyên bản, không chứa bất kỳ văn bản thừa nào bên ngoài (không dùng ```json hoặc ```). Cấu trúc:
{
  "title": "Chương N: Tên chương giật gân cuốn hút",
  "content": "Nội dung chương viết hoàn chỉnh bằng Tiếng Việt 100%, định dạng HTML với các thẻ <p>, <strong>, <em>..."
}
"""
    user_prompt = f"""
- Tựa truyện: {story_title}
- Viết Chương: {chap_num} / {total_chaps}
- Tóm tắt chi tiết Chương {chap_num}: {outline}
- Các chương trước đã viết tóm tắt: {json.dumps(prev_chapters, ensure_ascii=False)}
- Bối cảnh chính: Đầm sen Tây Hồ, Quảng An, Vạn An Capital, Lâm Khánh Chi, GC-MS, Ethyl Vanillin, C03, Đêm hội trà quốc tế, cấp cứu Đông y.

YÊU CẦU: Viết cực kỳ chi tiết, hội thoại sắc sảo, kéo dài kịch tính, đạt tối thiểu 1000 từ tiếng Việt. Mỗi câu phải được bọc trong một cặp thẻ <p>...</p>.
"""
    raw = call_claude(system_prompt, user_prompt, max_tokens=4000)
    raw = re.sub(r"^```(?:json)?\n", "", raw)
    raw = re.sub(r"\n```$", "", raw).strip()
    
    try:
        data = json.loads(raw)
        data['content'] = clean_and_split_sentences(data['content'])
        return data
    except Exception as e:
        print(f"⚠️ Error parsing Chapter {chap_num} JSON, trying fallback...")
        title_match = re.search(r'"title"\s*:\s*"(.*?)"', raw)
        content_match = re.search(r'"content"\s*:\s*"(.*)"', raw, re.DOTALL)
        if title_match and content_match:
            content = content_match.group(1).replace('\\"', '"').replace('\\n', '\n')
            return {
                "title": title_match.group(1),
                "content": clean_and_split_sentences(content)
            }
        else:
            return {
                "title": f"Chương {chap_num}: Đang cập nhật",
                "content": clean_and_split_sentences(raw)
            }

def main():
    print("\n" + "=" * 60)
    print(f"🎬 GENERATING V13 CONTENT FOR NOVEL ID {STORY_ID}")
    print("=" * 60)
    
    # 1. Generate Outline
    print("Generating outline...")
    outline_data = generate_outline()
    story_title = outline_data.get("title", STORY_TITLE)
    intro = clean_and_split_sentences(outline_data.get("intro", ""))
    outlines = outline_data.get("outlines", [])
    
    print(f"✓ Title V13: {story_title}")
    print(f"✓ Intro sentences: {len(intro.split('<p>')) - 1}")
    
    # 2. Generate 8 Chapters
    chapters = []
    prev_summaries = []
    
    for i in range(1, 9):
        print(f"\nWriting Chapter {i}/8...")
        chap_outline = outlines[i-1]['outline'] if i-1 < len(outlines) else "Tiếp tục cốt truyện kịch tính."
        chap = generate_chapter(story_title, chap_outline, i, 8, prev_summaries)
        
        # Word count check
        content_text = re.sub(r'<[^>]+>', ' ', chap['content'])
        words = content_text.split()
        word_count = len(words)
        
        print(f"  ✓ Written: {chap['title']}")
        print(f"  ✓ Word count: {word_count} words | Sentences: {len(chap['content'].split('<p>')) - 1}")
        
        # If too short, ask model to expand
        if word_count < 1000:
            print(f"  ⚠️ Chapter too short ({word_count} words). Expanding...")
            expansion_prompt = f"""
Chương truyện sau đây hơi ngắn ({word_count} từ), hãy viết tiếp và mở rộng thêm nội dung chi tiết cho chương này để đạt tối thiểu 1200 từ.
Đảm bảo bối cảnh Việt Nam, Show don't tell vật lý và mỗi câu nằm trong một thẻ <p>...</p>.

Tên chương: {chap['title']}
Nội dung hiện tại: {chap['content']}

Hãy trả về duy nhất nội dung chương đầy đủ đã mở rộng, định dạng HTML với mỗi câu trong một thẻ <p>...</p>.
"""
            expanded_raw = call_claude("Bạn là nhà văn sảng văn xuất sắc. Hãy mở rộng chương truyện theo đúng phong cách và định dạng.", expansion_prompt, max_tokens=4000)
            chap['content'] = clean_and_split_sentences(expanded_raw)
            expanded_text = re.sub(r'<[^>]+>', ' ', chap['content'])
            print(f"  ✓ Expanded word count: {len(expanded_text.split())} words")
            
        chapters.append(chap)
        prev_summaries.append(f"Chương {i}: {chap['title']}")
        time.sleep(2)
        
    # 3. Save locally to scratch directory
    output_file = f"scratch/rewrite_{STORY_ID}_v13.json"
    story_json = {
        "story_id": STORY_ID,
        "title": story_title,
        "intro": intro,
        "chapters": chapters,
        "focus_keyword": FOCUS_KEYWORD
    }
    
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(story_json, f, ensure_ascii=False, indent=2)
        
    print(f"\n🎉 SUCCESS: Generated & saved V13 JSON to {output_file}!")
    print("=" * 60)

if __name__ == "__main__":
    main()
