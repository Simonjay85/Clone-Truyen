import os
import json
import time
import requests
import re
import random
import urllib.parse

OPENAI_KEY = "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"

# The approved V12 blueprint for "Trọng Sinh 2008: Cơn Sốt Đất Đông Anh"
NOVEL_BLUEPRINT = {
    "title": "Trọng Sinh 2008: Cơn Sốt Đất Đông Anh",
    "author": "Thanh Phong",
    "genre": "Sảng Văn",
    "intro": """<p><strong>"Ba năm trước, tôi chết trong nghèo khổ bên vệ đường Hà Nội, bị kẻ thù cướp sạch dự án bất động sản tâm huyết và đẩy gia đình vào nợ nần chồng chất."</strong></p>
<p>Nhưng ông trời có mắt! Tôi mở mắt ra và thấy mình quay về mùa hè năm 2008 — thời điểm lịch sử khi Hà Tây chuẩn bị sáp nhập vào Hà Nội, và vùng đất Đông Anh đang trước thềm cơn sốt đất làm rung chuyển giới đầu cơ thủ đô. Với ký ức vô giá về mọi mốc quy hoạch: cầu Nhật Tân, đường vành đai 3, đại lộ Võ Nguyên Giáp, tôi thề sẽ lấy lại tất cả những gì thuộc về mình!</p>
<p>Nhưng thương trường là chiến trường khốc liệt. Đối đầu với ông trùm tín dụng đen Hoàng Mạnh Cường câu kết với các nhóm lợi ích tham lam, Trần Huy phải cùng Nguyễn Thanh Vy — ái nữ sắc sảo của Tập đoàn xây dựng Thanh Bình — lập nên liên minh thế kỷ. Một bộ truyện sảng văn/vả mặt tuyệt đỉnh với những cú lật kèo pháp lý, tài chính tinh vi chuẩn xác sẽ đưa bạn vào trung tâm cơn sốt đất vàng Hà Thành!</p>""",
    "cover_prompt": "A highly detailed, professional anime-style book cover, a young determined Vietnamese man in a modern casual suit overlooking a vast river with a grand bridge in the golden hour sunset, cinematic lighting, vivid colors, premium web novel art look",
    "outlines": [
        {
            "chap_num": 1,
            "outline": "Chương 1: Trọng Sinh Về Năm 2008. Trần Huy mở mắt nhận ra mình quay về mùa hè năm 2008. Ngay trong ngày đầu tiên, anh phải đối mặt với cảnh trùm tín dụng đen Hoàng Mạnh Cường (Cường Đại Bàng) dẫn theo côn đồ xông vào nhà dùng giấy nợ lãi cắt cổ để siết căn nhà mặt đường vành đai 3 tương lai của cha mẹ. Trần Huy dùng kiến thức quy hoạch cầu Nhật Tân tương lai để đàm phán xin khất nợ đúng 3 ngày, để lại lời thách thức lạnh lùng khiến Cường phải hoãn binh."
        },
        {
            "chap_num": 2,
            "outline": "Chương 2: Mỹ Nhân Phố Hiến & Cú Bắt Đầu. Trần Huy tiếp cận Nguyễn Thanh Vy, ái nữ kiêu kỳ của Tập đoàn Thanh Bình đang thực địa Đông Anh. Thanh Vy nghi ngờ tầm nhìn của anh. Trần Huy không giải thích nhiều, anh trực tiếp chỉ ra lô đất đầm lầy hoang vu tại Vĩnh Ngọc thực chất nằm ngay chân cầu Nhật Tân tương lai (khi đó dự án vẫn nằm trong quy hoạch mật). Anh giúp cô thương lượng mua đứt mảnh đất đó với giá cực hời từ một đầu nậu trước khi giá đất tăng vọt 50% chỉ sau một đêm, khiến Thanh Vy chấn động hoàn toàn trước tài năng của anh."
        },
        {
            "chap_num": 3,
            "outline": "Chương 3: Gom Đất Chân Cầu. Thanh Vy chưa rót vốn ngay. Cô đặt thử thách: Trần Huy phải tự giải quyết mâu thuẫn tranh chấp đất đai cực kỳ phức tạp tại khu vực Vĩnh Ngọc giữa người dân bản địa và đám côn đồ của Hoàng Mạnh Cường đang ép giá đền bù giải tỏa. Trần Huy dùng Luật Đất đai 2003 để đấu tranh đòi lại quyền lợi chính đáng cho dân nghèo, đồng thời gom sạch các lô đất đắc địa nhất sát chân cầu. Thanh Vy hoàn toàn bùng nổ lòng tin, chuyển khoản ngay 10 tỷ VND thông qua Vietcombank mở tài khoản mới để cùng lập Siêu Quỹ Đất."
        },
        {
            "chap_num": 4,
            "outline": "Chương 4: Trực Chiến Tín Dụng Đen. Cơn sốt đất Đông Anh chính thức bùng nổ dữ dội sau tin tức sáp nhập Hà Tây rò rỉ. Cường 'Đại Bàng' điên cuồng vì mất các lô đất vàng, cho tay sai dùng vũ lực phong tỏa các lối vào khu đất của Trần Huy, đe dọa các hộ dân đã bán đất cho anh. Trần Huy không hề lùi bước, anh trực tiếp đối đầu với Cường, vạch trần âm mưu lập hồ sơ khống cướp đất công ích của hắn trước mặt đông đảo người dân và chính quyền địa phương, buộc Cường phải tạm rút trong nhục nhã."
        },
        {
            "chap_num": 5,
            "outline": "Chương 5: Khủng Hoảng Truyền Thông. Cường 'Đại Bàng' liên kết với các thế lực lớn hơn ở thành phố để tung tin đồn Trần Huy bán dự án ma, lừa đảo huy động vốn trái phép. Sở Tài nguyên và Môi trường cùng Công an kinh tế vào cuộc phong tỏa toàn bộ giao dịch các lô đất của Trần Huy trong vòng 48 giờ để thanh tra. Khách hàng hoang mang kéo đến đòi rút cọc kịch liệt, ngân hàng đóng băng hạn mức tín dụng, đẩy liên minh của Trần Huy và Thanh Vy vào thế chân tường khủng hoảng cực đại."
        },
        {
            "chap_num": 6,
            "outline": "Chương 6: Lật Ngược Thế Cờ. Giữa đêm tối đen tối nhất của khủng hoảng, Trần Huy và Thanh Vy tung ra bằng chứng thép: Toàn bộ giấy chứng nhận quyền sử dụng đất hợp pháp cùng quyết định phê duyệt quy hoạch chi tiết 1/500 chính thức từ Bộ Xây dựng mà Trần Huy đã đi trước một bước xin cấp phép bằng danh nghĩa tập đoàn Thanh Bình. Đồng thời nộp đơn tố cáo Cường tội vu khống, lừa đảo chiếm đoạt tài sản công dân kèm chữ ký kiểm định pháp y chứng minh chữ ký trên tờ giấy nợ của gia đình anh là giả mạo."
        },
        {
            "chap_num": 7,
            "outline": "Chương 7: Bão Táp Đông Anh. C03 và Công an TP Hà Nội vào cuộc triệt phá toàn bộ đường dây tín dụng đen và thao túng đất đai của Hoàng Mạnh Cường. Cường điên cuồng ôm tiền lừa đảo đền bù đất đai định bỏ trốn sang biên giới, nhưng bị Trần Huy và lực lượng cảnh sát đón lỏng vây bắt ngoạn mục ngay tại chân cầu Thăng Long cũ trong cơn giông bão."
        },
        {
            "chap_num": 8,
            "outline": "Chương 8: Vua Đất Hà Thành. Dự án cầu Nhật Tân và đường Võ Nguyên Giáp chính thức khởi công. Giá trị các lô đất sát chân cầu của Trần Huy tăng vọt gấp 10 lần, biến anh thành tỷ phú đô la trẻ tuổi nhất Đông Anh. Trước đại tiệc mừng công của Siêu Quỹ Đất Hà Thành, Trần Huy và Thanh Vy đứng bên bờ sông Hồng dưới hoàng hôn lãng mạn, Thanh Vy bày tỏ tình yêu tự nguyện sâu sắc của cô dành cho anh. Tại buổi họp báo tối hôm đó, trước giới tài phiệt thủ đô, cô tự hào giới thiệu Trần Huy là hôn phu và gọi một tiếng ngọt ngào 'Chồng yêu'. Kết thúc viên mãn."
        }
    ]
}

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

def call_openai(system_prompt, user_prompt, max_tokens=3500, temperature=0.7):
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
    for attempt in range(3):
        try:
            res = requests.post(url, json=payload, headers=headers, timeout=120)
            res.raise_for_status()
            data = res.json()
            return data['choices'][0]['message']['content'].strip()
        except Exception as e:
            print(f"OpenAI Call Error (Attempt {attempt+1}): {e}")
            time.sleep(5)
    raise SystemExit("Fatal: Failed to connect to OpenAI API after multiple attempts.")

def main():
    print("=" * 60)
    print("🎬 GENERATING NEW NOVEL: TRỌNG SINH 2008: CƠN SỐT ĐẤT ĐÔNG ANH")
    print("=" * 60)
    
    chapters_content = []
    
    for i, outline_item in enumerate(NOVEL_BLUEPRINT['outlines'], 1):
        print(f"\nGenerating detailed Chapter {i}/8: {outline_item['outline'][:70]}...")
        
        system_writer_prompt = """Bạn là THE GHOSTWRITER - Nhà văn truyện mạng sảng văn/vả mặt đô thị số 1 Việt Nam. Bạn có văn phong miêu tả cực kỳ sống động, chân thực, sắc sảo và cuốn hút.

QUY TẮC VIẾT MASTERPIECE V12:
1. SHOW, DON'T TELL: Miêu tả chi tiết hành động vật lý, nét mặt, sự run rẩy, giọt mồ hôi chảy dài, hay tiếng giày gót nhọn giẫm xuống sàn gạch. Tránh các tính từ sáo rỗng như 'vô biên', 'tột cùng', 'kinh hoàng'.
2. HỘI THOẠI ĐINH TAI NHỨC ÓC: Các câu thoại sắc lẹm, thể hiện sự kiêu ngạo, tham lam của kẻ thù trước khi bị vả mặt, và sự điềm tĩnh tối thượng của nhân vật chính.
3. CHI TIẾT BẤT ĐỘNG SẢN & ĐỜI SỐNG THỰC TẾ TẠI HÀ NỘI (2008): Sử dụng các chi tiết thật về cơ cấu quy hoạch (cầu Nhật Tân, đường vành đai 3, đại lộ Võ Nguyên Giáp, huyện Đông Anh, xã Vĩnh Ngọc), luật pháp (Luật Đất đai 2003, phê duyệt quy hoạch chi tiết 1/500 từ Bộ Xây dựng), sao kê tài chính ngân hàng Việt Nam (Vietcombank), và thói quen sinh hoạt bản địa Hà Nội năm 2008.
4. ĐỘ DÀI CỰC KHỦNG (1200 - 1800 TỪ): Bắt buộc viết cực kỳ chi tiết, chậm rãi, phát triển sâu sắc tâm lý nhân vật và các đoạn hội thoại gay cấn dài lâu. Dung lượng bắt buộc phải đạt từ 1200 đến 1800 từ (khoảng 7000 - 10000 ký tự tiếng Việt bao gồm khoảng trắng). Tuyệt đối không được viết tóm tắt hay kết thúc chương quá nhanh.
5. ĐỊNH DẠNG: Chỉ sử dụng các thẻ HTML cơ bản như <p>, <strong>, <em>, <hr> để trình bày nội dung sạch sẽ.
6. KHÔNG META TEXT: Tuyệt đối không chứa bất kỳ văn bản thừa nào bên ngoài cấu trúc JSON."""

        user_writer_prompt = f"""Dựa trên bản thiết kế truyện sau:
- Tựa truyện: {NOVEL_BLUEPRINT['title']}
- Giới thiệu thế giới quan & nhân vật: {NOVEL_BLUEPRINT['intro']}
- Tác giả: {NOVEL_BLUEPRINT['author']}

Hãy viết CHI TIẾT CHƯƠNG {i} của bộ truyện.
- Dàn ý Chương {i}: {outline_item['outline']}
{f"- Các chương trước đã viết tóm tắt: {json.dumps([c['title'] for c in chapters_content], ensure_ascii=False)}" if chapters_content else ""}

YÊU CẦU ĐẶC BIỆT VỀ ĐỘ DÀI & VĂN PHONG V12:
- Bắt buộc nội dung trong phần "content" phải có độ dài tối thiểu từ 1200 từ trở lên (khoảng 7000 - 10000 ký tự tiếng Việt). Hãy viết cực kỳ chi tiết, diễn giải từng hành động, suy nghĩ và hội thoại chậm rãi để đạt đủ độ dài này. Không viết tóm tắt!
- Hãy viết thật mượt mà, sâu sắc, lột tả chân thực bối cảnh sốt đất Đông Anh Hà Nội năm 2008.

YÊU CẦU TRẢ VỀ dạng JSON chính xác:
{{
  "title": "Chương {i}: Tên chương giật gân, cuốn hút và thuần Việt",
  "content": "Nội dung chương viết hoàn chỉnh bằng Tiếng Việt 100%, định dạng HTML với các thẻ <p>, <strong>, <em>..."
}}"""

        chap_raw = call_openai(system_writer_prompt, user_writer_prompt, max_tokens=4000, temperature=0.7)
        
        try:
            chap_data = robust_json_parse(chap_raw)
            # Verify word count / character length
            word_count = len(chap_data['content'].split())
            print(f"  -> ✓ Finished Chapter {i}: {chap_data['title']} ({len(chap_data['content'])} chars, ~{word_count} words)")
            chapters_content.append(chap_data)
        except Exception as e:
            print(f"Failed to parse Chapter {i} JSON, trying fallback regex...")
            try:
                title_match = re.search(r'"title"\s*:\s*"(.*?)"', chap_raw)
                content_match = re.search(r'"content"\s*:\s*"(.*)"', chap_raw, re.DOTALL)
                if title_match and content_match:
                    content_str = content_match.group(1).replace('\\"', '"').replace('\\n', '\n')
                    # Strip any wrapping quote from the end if regex over-captured
                    if content_str.endswith('"') or content_str.endswith('"}'):
                        content_str = content_str.rstrip('"}').rstrip('"')
                    recovered_chap = {
                        "title": title_match.group(1),
                        "content": content_str
                    }
                    word_count = len(recovered_chap['content'].split())
                    chapters_content.append(recovered_chap)
                    print(f"  -> ✓ Recovered Chapter {i} via regex (~{word_count} words)")
                else:
                    raise e
            except Exception as e2:
                print(chap_raw[:1000])
                raise SystemExit(f"Fatal error generating Chapter {i}: {e2}")
                
        time.sleep(2)

    # Save to pending_novel.json draft
    print("\nSaving complete story draft to pending_novel.json...")
    pending_file = "/Users/aaronnguyen/TN/App/doctieuthuyet/pending_novel.json"
    pending_data = {
        "title": NOVEL_BLUEPRINT['title'],
        "author": NOVEL_BLUEPRINT['author'],
        "genre": NOVEL_BLUEPRINT['genre'],
        "intro": NOVEL_BLUEPRINT['intro'],
        "cover_prompt": NOVEL_BLUEPRINT['cover_prompt'],
        "chapters": chapters_content
    }
    with open(pending_file, "w", encoding="utf-8") as f:
        json.dump(pending_data, f, ensure_ascii=False, indent=2)
    print("✓ Successfully saved pending_novel.json.")

if __name__ == "__main__":
    main()
