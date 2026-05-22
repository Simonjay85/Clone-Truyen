import os
import json
import time
import requests
import re
import sys

OPENAI_KEY = "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"

STORIES = {
    2013: {
        "id": 2013,
        "title": "Bức Thư Cuối Cùng Của Biển",
        "keywords": "Bức Thư Cuối Cùng Của Biển, Hoàng Quân, Vũ Phương Mai, Cát Hải Hải Phòng, sạt lở địa chất, vả mặt chủ thầu Trịnh, bão số 3 Đình Vũ, máy quét 3D địa chất",
        "focus_keyword": "Bức Thư Cuối Cùng Của Biển"
    },
    2020: {
        "id": 2020,
        "title": "Hệ Thống Trí Tuệ Nhân Tạo: Xuyên Không Đến Tương Lai",
        "keywords": "Hệ Thống Trí Tuệ Nhân Tạo, Genesis-08, Bùi Thu Hà, cyborg tương lai, lò phản ứng hạt nhân mini, Sài Gòn 2046, Lão Độc Thiết Huyết, thuật toán tối ưu hạt nhân",
        "focus_keyword": "Hệ Thống Trí Tuệ Nhân Tạo"
    }
}

def clean_and_split_sentences(content):
    """
    Cleans HTML tags and wraps every single sentence in exactly one <p>...</p> tag.
    Also removes double spacing and redundant empty tags.
    """
    # Remove existing <p> and </p> tags
    text = content.replace("<p>", "").replace("</p>", "").strip()
    
    # Split text into sentences by looking for sentence-ending punctuation (. ! ?) followed by whitespace
    sentences = re.split(r'(?<=[.!?])\s+', text)
    
    formatted = []
    for s in sentences:
        s = s.strip()
        if s:
            # Clean double quotes and format properly
            formatted.append(f"<p>{s}</p>")
            
    return "\n".join(formatted)

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
            res = requests.post(url, json=payload, headers=headers, timeout=120)
            res.raise_for_status()
            data = res.json()
            return data['choices'][0]['message']['content'].strip()
        except Exception as e:
            print(f"⚠️ OpenAI Call Error (Attempt {attempt+1}): {e}")
            time.sleep(5)
    raise Exception("Fatal: Failed to connect to OpenAI API after multiple attempts.")

def generate_outline(story):
    system_prompt = """Bạn là nhà văn mạng sảng văn vả mặt đỉnh cao Việt Nam. Nhiệm vụ của bạn là lập đề cương 8 chương cho truyện mạng.
Mỗi chương cần tóm tắt chi tiết cốt truyện kịch tính nảy lửa, tuân thủ chuẩn V13 bắt buộc:
1. Show don't tell vật lý: mô tả vật lý sắc bén (mồ hôi gáy lạnh toát, cơ mặt giật giật, khớp tay nắm chặt rỉ máu, tiếng thở hổn hển) thay vì dùng tính từ cảm xúc trừu tượng.
2. Bối cảnh địa danh thật, sinh hoạt, tiền tệ chuẩn Việt Nam (Cát Hải Hải Phòng, bão số 3 Đình Vũ, Sài Gòn 2046, VNĐ, sao kê ngân hàng...).
3. Nữ chính hoặc đồng hành nữ lý tính, thương lượng sòng phẳng trước khi giúp đỡ (hợp đồng pháp lý, ăn chia tỉ lệ phần trăm, trao đổi tài nguyên rõ ràng).
4. Khủng hoảng kéo dài trên 24 giờ gay cấn (bão sạt lở đe dọa chôn vùi thị trấn, lò phản ứng hạt nhân quá tải sắp nổ, bị bao vây đe dọa truy tố pháp lý...).
5. Bằng chứng số/pháp lý cụ thể giải quyết tranh chấp (trích xuất camera, sao kê, máy quét 3D địa chất siêu âm sạt lở, dữ liệu log mạng lò phản ứng hạt nhân mini Genesis-08). Không dùng phép thuật hay siêu năng lực phi lý.

Hãy trả về JSON nguyên bản, không chứa bất kỳ văn bản thừa nào bên ngoài (không dùng ```json hoặc ```). Cấu trúc:
{
  "title": "Tên truyện giật gân chuẩn V13",
  "intro": "Mô tả truyện tóm tắt kịch tính (HTML, mỗi câu 1 thẻ <p>)",
  "outlines": [
    {"chap_num": 1, "outline": "Tóm tắt chương 1..."},
    {"chap_num": 2, "outline": "Tóm tắt chương 2..."},
    {"chap_num": 3, "outline": "Tóm tắt chương 3..."},
    {"chap_num": 4, "outline": "Tóm tắt chương 4..."},
    {"chap_num": 5, "outline": "Tóm tắt chương 5..."},
    {"chap_num": 6, "outline": "Tóm tắt chương 6..."},
    {"chap_num": 7, "outline": "Tóm tắt chương 7..."},
    {"chap_num": 8, "outline": "Tóm tắt chương 8..."}
  ]
}
"""
    user_prompt = f"Hãy tạo đề cương V13 cho truyện ID {story['id']} có tiêu đề gốc: '{story['title']}'. Từ khóa đặc biệt cần có: {story['keywords']}."
    
    raw = call_openai(system_prompt, user_prompt, max_tokens=3000)
    raw = re.sub(r"^```(?:json)?\n", "", raw)
    raw = re.sub(r"\n```$", "", raw).strip()
    
    try:
        return json.loads(raw)
    except Exception as e:
        print("❌ Error parsing outline JSON:", e)
        start = raw.find("{")
        end = raw.rfind("}")
        if start != -1 and end != -1:
            return json.loads(raw[start:end+1])
        raise e

def generate_chapter(story_title, outline, chap_num, total_chaps, prev_chapters, keywords):
    system_prompt = """Bạn là nhà văn mạng sảng văn vả mặt số 1 Việt Nam. Bạn có văn văn phong miêu tả cực kỳ sống động, chân thực, sắc sảo.
Hãy viết chương truyện dài từ 1000 - 1500 từ theo tóm tắt chương.
YÊU CẦU BẮT BUỘC CHUẨN V13:
1. Show don't tell vật lý: miêu tả nét mặt, mồ hôi gáy rịn ra, khớp tay run rẩy, hơi thở dồn dập, cơ mặt giật nhẹ. Tránh các từ sáo rỗng cảm xúc như "vô cùng giận dữ", "hoảng sợ".
2. Địa danh thật tại Việt Nam.
3. Nữ chính lý tính thương lượng sòng phẳng (ví dụ: ăn chia phần trăm lợi nhuận, ký hợp đồng rõ ràng mới giúp đỡ).
4. Tình huống khủng hoảng nặng nề kéo dài trên 24 giờ.
5. Chứng cứ pháp lý/số liệu kỹ thuật/dữ liệu số rõ ràng, thực tế (LIMS, camera, sao kê, log server, máy quét 3D địa chất...).
6. Mỗi câu văn bắt buộc phải nằm trong một cặp thẻ <p>...</p>. Ví dụ:
<p>Lòng bàn tay Hoàng Quân rịn một lớp mồ hôi mỏng, lạnh ngắt.</p>
<p>Anh ngước mắt nhìn thẳng vào gã chủ thầu Trịnh.</p>
<p>Khớp ngón tay anh siết chặt đến mức phát ra tiếng rắc khe khẽ.</p>

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
- Từ khóa bối cảnh cần lưu ý: {keywords}

YÊU CẦU: Viết cực kỳ chi tiết, hội thoại sắc sảo, kéo dài kịch tính, đạt tối thiểu 1000 từ tiếng Việt. Mỗi câu phải được bọc trong một cặp thẻ <p>...</p>.
"""
    raw = call_openai(system_prompt, user_prompt, max_tokens=4000)
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
    if len(sys.argv) < 2:
        print("Usage: python3 generate_v13_json.py <story_id>")
        sys.exit(1)
        
    sid = int(sys.argv[1])
    if sid not in STORIES:
        print(f"❌ Story ID {sid} not found in Group F local config.")
        sys.exit(1)
        
    story = STORIES[sid]
    print("\n" + "=" * 60)
    print(f"🎬 GENERATING V13 CONTENT FOR ID {sid}: {story['title']}")
    print("=" * 60)
    
    # 1. Generate Outline
    print("Generating outline...")
    outline_data = generate_outline(story)
    story_title = outline_data.get("title", story['title'])
    intro = clean_and_split_sentences(outline_data.get("intro", ""))
    outlines = outline_data.get("outlines", [])
    
    print(f"✓ Title V13: {story_title}")
    print(f"✓ Intro sentences: {len(intro.split('<p>')) - 1}")
    
    # 2. Generate 8 Chapters
    chapters = []
    prev_summaries = []
    
    for i in range(1, 9):
        print(f"Writing Chapter {i}/8...")
        chap_outline = outlines[i-1]['outline'] if i-1 < len(outlines) else "Tiếp tục cốt truyện kịch tính."
        chap = generate_chapter(story_title, chap_outline, i, 8, prev_summaries, story['keywords'])
        
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
            expanded_raw = call_openai("Bạn là nhà văn sảng văn xuất sắc. Hãy mở rộng chương truyện theo đúng phong cách và định dạng.", expansion_prompt, max_tokens=4000)
            chap['content'] = clean_and_split_sentences(expanded_raw)
            expanded_text = re.sub(r'<[^>]+>', ' ', chap['content'])
            print(f"  ✓ Expanded word count: {len(expanded_text.split())} words")
            
        chapters.append(chap)
        prev_summaries.append(f"Chương {i}: {chap['title']}")
        time.sleep(1)
        
    # 3. Create SEO RankMath Tags
    focus_keyword = story['focus_keyword']
    seo_title = f"{story_title[:45]} - Sảng Văn V13 Full"
    seo_description = f"{story_title}. Đọc truyện sảng văn vả mặt chuẩn V13 kịch tính đỉnh cao, bối cảnh thực tế tại Việt Nam với pháp lý và chứng cứ số sắc bén."
    
    seo = {
        "focus_keyword": focus_keyword,
        "seo_title": seo_title,
        "seo_description": seo_description
    }
    
    # 4. Save locally
    output_file = f"scratch/rewrite_{story['id']}_v13.json"
    story_json = {
        "story_id": story['id'],
        "title": story_title,
        "intro": intro,
        "chapters": chapters,
        "seo": seo
    }
    
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(story_json, f, ensure_ascii=False, indent=2)
        
    print(f"\n🎉 SUCCESS: Generated & saved V13 JSON to {output_file}!")
    print("=" * 60)

if __name__ == "__main__":
    main()
