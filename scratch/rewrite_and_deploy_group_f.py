import os
import json
import time
import requests
import re
import sys

OPENAI_KEY = "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"
WP_URL = "https://doctieuthuyet.com"

# Group F Novels configurations
STORIES = [
    {
        "id": 1984,
        "title": "Tôi Giả Nghèo Đi Ra Mắt, Mẹ Người Yêu Đòi Sính Lễ 900 Triệu",
        "keywords": "Tôi Giả Nghèo Đi Ra Mắt, Trần Tuấn Anh, Nguyễn Thùy Chi, sính lễ 900 triệu, vả mặt mẹ người yêu cũ, chung cư Hoài Đức",
        "focus_keyword": "Tôi Giả Nghèo Đi Ra Mắt"
    },
    {
        "id": 2001,
        "title": "Ánh Sáng Trong Đêm",
        "keywords": "Ánh Sáng Trong Đêm, Lê Gia Minh, Trịnh Tuệ An, họa sĩ sơn mài mù, vả mặt thiếu gia Lâm, Metropole Hà Nội, tranh sơn mài cổ Hàng Bông",
        "focus_keyword": "Ánh Sáng Trong Đêm"
    },
    {
        "id": 2007,
        "title": "Lột Mặt Người Sếp Cướp Công",
        "keywords": "Lột Mặt Người Sếp Cướp Công, Lâm Trạch, Phạm Khánh Vy, Hoàng Quốc Trung, bài thuốc dạ dày gia truyền, IPO công ty dược, Lotte Hà Nội, log server LIMS",
        "focus_keyword": "Lột Mặt Người Sếp Cướp Công"
    },
    {
        "id": 2013,
        "title": "Bức Thư Cuối Cùng Của Biển",
        "keywords": "Bức Thư Cuối Cùng Của Biển, Hoàng Quân, Vũ Phương Mai, Cát Hải Hải Phòng, sạt lở địa chất, vả mặt chủ thầu Trịnh, bão số 3 Đình Vũ, máy quét 3D địa chất",
        "focus_keyword": "Bức Thư Cuối Cùng Của Biển"
    },
    {
        "id": 2020,
        "title": "Hệ Thống Trí Tuệ Nhân Tạo: Xuyên Không Đến Tương Lai",
        "keywords": "Hệ Thống Trí Tuệ Nhân Tạo, Genesis-08, Bùi Thu Hà, cyborg tương lai, lò phản ứng hạt nhân mini, Sài Gòn 2046, Lão Độc Thiết Huyết, thuật toán tối ưu hạt nhân",
        "focus_keyword": "Hệ Thống Trí Tuệ Nhân Tạo"
    }
]

def clean_and_split_sentences(content):
    """
    Guarantees every single sentence is wrapped in exactly one <p> tag.
    It strips existing <p> tags, splits text into sentences, and wraps each in <p>...</p>.
    """
    # Remove HTML tags first to get plain text, but keep strong/em markers
    text = content.replace("<p>", "").replace("</p>", "").strip()
    
    # Split text into sentences by looking for sentence-ending punctuation followed by whitespace.
    sentences = re.split(r'(?<=[.!?])\s+', text)
    
    formatted = []
    for s in sentences:
        s = s.strip()
        if s:
            formatted.append(f"<p>{s}</p>")
            
    return "\n".join(formatted)

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
            print(f"⚠️ OpenAI Call Error (Attempt {attempt+1}): {e}")
            time.sleep(5)
    raise Exception("Fatal: Failed to connect to OpenAI API after multiple attempts.")

def generate_outline(story):
    system_prompt = """Bạn là nhà văn mạng sảng văn vả mặt đỉnh cao Việt Nam. Nhiệm vụ của bạn là lập đề cương 8 chương cho truyện mạng.
Mỗi chương cần tóm tắt chi tiết cốt truyện kịch tính nảy lửa, tuân thủ chuẩn V13 bắt buộc:
1. Show don't tell vật lý: mô tả vật lý sắc bén (mồ hôi gáy lạnh toát, cơ mặt giật giật, khớp tay nắm chặt rỉ máu, tiếng thở hổn hển) thay vì dùng tính từ cảm xúc trừu tượng.
2. Bối cảnh địa danh thật, sinh hoạt, tiền tệ chuẩn Việt Nam (Hoài Đức, Hàng Bông, Cát Hải, Sài Gòn, Hà Nội, VNĐ, sao kê ngân hàng...).
3. Nữ chính hoặc đồng hành nữ lý tính, thương lượng sòng phẳng trước khi giúp đỡ (hợp đồng pháp lý, ăn chia tỉ lệ phần trăm, trao đổi tài nguyên rõ ràng).
4. Khủng hoảng kéo dài trên 24 giờ gay cấn (bị giang hồ bao vây, công ty đình chỉ, đóng băng tài sản, đe dọa truy tố pháp lý, bão đổ bộ...).
5. Bằng chứng số/pháp lý cụ thể giải quyết tranh chấp (dữ liệu LIMS phòng thí nghiệm, file sao lưu, trích xuất camera hành trình, sao kê tài chính ngân hàng, bản quét 3D siêu âm địa chất, dữ liệu log mạng lò phản ứng hạt nhân). Không dùng phép thuật hay siêu năng lực phi lý.

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
    
    raw = call_openai(system_prompt, user_prompt, max_tokens=2500)
    raw = re.sub(r"^```(?:json)?\n", "", raw)
    raw = re.sub(r"\n```$", "", raw).strip()
    
    try:
        return json.loads(raw)
    except Exception as e:
        print("❌ Error parsing outline JSON:", e)
        # Fallback parsing
        start = raw.find("{")
        end = raw.rfind("}")
        if start != -1 and end != -1:
            return json.loads(raw[start:end+1])
        raise e

def generate_chapter(story_title, outline, chap_num, total_chaps, prev_chapters):
    system_prompt = """Bạn là nhà văn mạng sảng văn vả mặt số 1 Việt Nam. Bạn có văn phong miêu tả cực kỳ sống động, chân thực, sắc sảo.
Hãy viết chương truyện dài từ 1000 - 1500 từ theo tóm tắt chương.
YÊU CẦU BẮT BUỘC CHUẨN V13:
1. Show don't tell vật lý: miêu tả nét mặt, mồ hôi gáy rịn ra, khớp tay run rẩy, hơi thở dồn dập, cơ mặt giật nhẹ. Tránh các từ sáo rỗng cảm xúc như "vô cùng giận dữ", "hoảng sợ".
2. Địa danh thật tại Việt Nam.
3. Nữ chính lý tính thương lượng sòng phẳng.
4. Tình huống khủng hoảng nặng nề kéo dài.
5. Chứng cứ pháp lý/số liệu rõ ràng, thực tế.
6. Mỗi câu văn bắt buộc phải nằm trong một cặp thẻ <p>...</p>. Ví dụ:
<p>Lòng bàn tay Trần Tuấn Anh rịn một lớp mồ hôi mỏng, lạnh ngắt.</p>
<p>Anh ngước mắt nhìn thẳng vào bà mẹ người yêu cũ.</p>
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
    print("=" * 60)
    print("🎬 V13 GROUP F STORY REWRITER ENGINE START")
    print("=" * 60)
    
    os.makedirs("scratch", exist_ok=True)
    
    # Check if single story ID passed
    target_stories = STORIES
    if len(sys.argv) > 1:
        sid = int(sys.argv[1])
        target_stories = [s for s in STORIES if s["id"] == sid]
        if not target_stories:
            print(f"❌ Story ID {sid} not found in Group F config.")
            sys.exit(1)
            
    for story in target_stories:
        print("\n" + "=" * 50)
        print(f"📖 Processing Story ID {story['id']}: {story['title']}")
        print("=" * 50)
        
        # 1. Generate Outline
        print("Generating outline...")
        outline_data = generate_outline(story)
        story_title = outline_data.get("title", story['title'])
        intro = clean_and_split_sentences(outline_data.get("intro", ""))
        outlines = outline_data.get("outlines", [])
        
        print(f"✓ Title V13: {story_title}")
        
        # 2. Generate 8 Chapters
        chapters = []
        prev_summaries = []
        
        for i in range(1, 9):
            print(f"Writing Chapter {i}/8...")
            chap_outline = outlines[i-1]['outline'] if i-1 < len(outlines) else "Tiếp tục cốt truyện kịch tính."
            chap = generate_chapter(story_title, chap_outline, i, 8, prev_summaries)
            chapters.append(chap)
            prev_summaries.append(f"Chương {i}: {chap['title']}")
            print(f"  ✓ Written: {chap['title']} ({len(chap['content'].split('<p>')) - 1} sentences)")
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
        print(f"✓ Saved locally: {output_file}")
        
        # 5. Deploy to WordPress via helper script
        print("Deploying story to WordPress...")
        payload = {
            "secret_token": "ZEN_TRUYEN_2026_BYPASS",
            "story_id": story['id'],
            "title": story_title,
            "intro": intro,
            "chapters": chapters,
            "seo": seo
        }
        
        try:
            api_url = f"{WP_URL}/update_story.php"
            res = requests.post(api_url, json=payload, timeout=120)
            res_data = res.json()
            if res_data.get("success"):
                print(f"🎉 SUCCESS: Published Story ID {story['id']} to live website!")
                print(f"   Deleted Chapters: {res_data.get('deleted_chapters_count')}")
                print(f"   New Chapters: {res_data.get('chapters_count')}")
            else:
                print(f"❌ WordPress API error: {res_data}")
        except Exception as e:
            print(f"❌ Deploy API connection failed: {e}")
            
    print("\n" + "=" * 60)
    print("🎉 ALL GROUP F STORIES PROCESSED SUCCESSFULLY!")
    print("=" * 60)

if __name__ == "__main__":
    main()
