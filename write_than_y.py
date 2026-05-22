# -*- coding: utf-8 -*-
import json
import os
import re
import sys
import time
import requests

# Configuration
OPENAI_KEY = "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"
INPUT_DRAFT = "/Users/aaronnguyen/TN/App/doctieuthuyet/draft_than_y.json"
OUTPUT_FILE = "/Users/aaronnguyen/TN/App/doctieuthuyet/pending_novel.json"

def log(msg):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {msg}")
    sys.stdout.flush()

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
            log(f"⚠️ OpenAI Call Error (Attempt {attempt+1}): {e}")
            time.sleep(5)
    raise SystemExit("Fatal: Failed to connect to OpenAI API after multiple attempts.")

def split_into_sentences(text):
    # Standardize spaces
    t = re.sub(r'\s+', ' ', text).strip()
    
    # Abbreviations list to avoid splitting on them
    abbrevs = ["TS.", "BS.", "CFO.", "Dr.", "Mr.", "Mrs.", "Ms.", "A.S.A.P.", "Deloitte.", "Keangnam.", "BIDV.", "GC-MS."]
    for i, abb in enumerate(abbrevs):
        t = t.replace(abb, f"__ABB{i}__")
        
    # Mark sentence endings: punctuation (. ! ?) followed by optional quotes, then space, then capital or quote/number
    t = re.sub(r'([.!?]["”\'’]?)\s+(?=[A-Z"“\'‘\d\-\w])', r'\1[SENTENCE_END]', t)
    
    # Restore abbreviations
    for i, abb in enumerate(abbrevs):
        t = t.replace(f"__ABB{i}__", abb)
        
    sentences = t.split("[SENTENCE_END]")
    result = []
    for s in sentences:
        s = s.strip()
        if s:
            result.append(s)
    return result

def clean_and_format_content(raw_text):
    # Remove HTML tags returned by LLM to let the Python splitter handle V13 paragraph wrapping purely
    clean_text = re.sub(r'<[^>]+>', ' ', raw_text)
    sentences = split_into_sentences(clean_text)
    
    v13_paragraphs = []
    for s in sentences:
        if s:
            v13_paragraphs.append(f"<p>{s}</p>")
            
    return "\n".join(v13_paragraphs) + "\n"

def count_words(text):
    # Basic word count for Vietnamese
    words = text.split()
    return len(words)

def main():
    log("🚀 NOVEL EXPANSION ENGINE - V13 GOLD STANDARD")
    
    if not os.path.exists(INPUT_DRAFT):
        log(f"❌ Input draft not found at: {INPUT_DRAFT}")
        return
        
    with open(INPUT_DRAFT, "r", encoding="utf-8") as f:
        draft_data = json.load(f)
        
    log(f"✓ Loaded draft: {draft_data['title']}")
    
    novel_blueprint = {
        "title": draft_data["title"],
        "author": draft_data["author"],
        "genre": draft_data["genre"],
        "intro": draft_data["intro"],
        "cover_prompt": "A highly premium, cinematic anime-style web novel cover. A handsome 32-year-old Vietnamese traditional doctor in a modern laboratory, holding a vintage wooden medical box with intricate gold patterns. Beside him stands a beautiful, sophisticated 30-year-old Vietnamese corporate woman (CFO) wearing a elegant blazer. Background displays state-of-the-art chemical analysis screens showing GC-MS chromatography graphs and molecular models of gan cells. Beautiful dramatic studio lighting, golden accents, bold and inspiring art.",
        "chapters": []
    }
    
    system_prompt = """Bạn là THE GHOSTWRITER - Nhà văn truyện mạng sảng văn/vả mặt số 1 Việt Nam. Bạn có văn phong miêu tả cực kỳ sống động, chân thực, sắc sảo và sâu sắc.
Nhiệm vụ của bạn là mở rộng bản nháp chương truyện thành một chương truyện sảng văn/vả mặt dài, chi tiết, chậm rãi, cực kỳ cuốn hút theo tiêu chuẩn vàng của Việt Nam.

QUY TẮC PHẢI TUÂN THỦ TUYỆT ĐỐI:
1. SHOW, DON'T TELL: Miêu tả chi tiết hành động vật lý, biểu cảm, nét mặt, sự run rẩy, giọt mồ hôi, hay tiếng giày gót nhọn giẫm xuống sàn bê tông, tiếng đũa va vào bát, tiếng rót trà lách cách. Tránh các tính từ sáo rỗng như 'vô biên', 'tột cùng', 'kinh hoàng'.
2. HỘI THOẠI ĐINH TAI NHỨC ÓC: Các câu thoại sắc lẹm, kịch tính, thể hiện sự kiêu ngạo của kẻ thù trước khi bị vả mặt, và sự điềm tĩnh tối thượng của nhân vật chính.
3. CHI TIẾT KỸ THUẬT & PHÁP LÝ CHÍNH XÁC: Sử dụng chi tiết thật về y học cổ truyền Việt Nam, phân tích sắc ký sắc ký khí GC-MS, kiểm toán độc lập Deloitte (mã kiểm toán DLV-2024-HN-09917), Git commit forensic logs trên máy chủ, cơ quan điều tra C03 Bộ Công an, luật sở hữu trí tuệ Việt Nam.
4. ĐỘ DÀI BẮT BUỘC (1200 - 1400 TỪ VIỆT NAM): Chương viết phải cực kỳ dài, chi tiết, chậm rãi và đạt độ dài tối thiểu là 1200 từ và tối đa là 1400 từ. Hãy kéo dài các cảnh tranh chấp, các màn đối thoại, suy nghĩ nội tâm và các tình tiết kỹ thuật y học một cách phong phú để đạt được độ dài này. Tuyệt đối không được viết ngắn dưới 1000 từ hay tóm tắt nhanh chóng.
5. VĂN PHONG VIỆT NAM HIỆN ĐẠI: Đặt bối cảnh và lối sống hiện đại 100% tại Hà Nội (Tràng Tiền, Hàng Bồ, Ngụy Như Kon Tum, Keangnam, Hồ Tây). Cách xưng hô tự nhiên của người Việt (anh, em, ông, bà, mày, tao, chú, cháu).
6. FORMAT: Chỉ trả về nội dung văn xuôi Tiếng Việt hoàn chỉnh, không cần thẻ HTML (Python sẽ tự động chia thẻ <p> ở mức câu). Tránh các lời giải thích hay lời nhắn ở đầu/cuối phản hồi."""

    for i, ch in enumerate(draft_data["chapters"]):
        chap_num = ch["chap_num"]
        chap_title = ch["title"]
        draft_content = ch["draft"]
        
        log(f"📝 Expanding Chapter {chap_num}/{len(draft_data['chapters'])}: {chap_title}...")
        
        user_prompt = f"""Hãy mở rộng bản nháp chương sau đây thành một chương truyện đầy đủ, sống động và kịch tính có độ dài từ 1200 đến 1400 từ Tiếng Việt:
- Tiêu đề chương: {chap_title}
- Bản nháp gốc: {draft_content}

Yêu cầu cụ thể cho Chương {chap_num}:
- Hãy phát triển tất cả các nhân vật, đối thoại kịch tính, kéo dài các màn giao tiếp xã hội, phân tích y thuật hoặc đấu trí pháp lý một cách chậm rãi, giàu chất cảm và tình tiết kịch tính.
- Đảm bảo độ dài văn bản Tiếng Việt trong khoảng 1200 - 1400 từ. Hãy viết thật sâu sắc và phong phú!"""

        # Call API to generate expanded content
        expanded_raw = call_openai(system_prompt, user_prompt, max_tokens=4000, temperature=0.7)
        
        # Enforce V13 formatting
        formatted_content = clean_and_format_content(expanded_raw)
        
        word_cnt = count_words(formatted_content)
        log(f"  -> ✓ Finished Chapter {chap_num}. Generated {word_cnt} words.")
        
        # Adjust text dynamic checks to ensure gold standard word counts (1000 - 1500 words per chapter)
        if word_cnt < 1000:
            log(f"  -> ⚠️ Chapter {chap_num} is too short ({word_cnt} words). Retrying expansion to hit target length...")
            user_prompt += "\nLƯU Ý: Nội dung trước quá ngắn. Hãy viết dài hơn nữa, miêu tả chi tiết sâu sắc hơn nữa các bối cảnh và hội thoại của các nhân vật để đạt ít nhất 1200 từ."
            expanded_raw = call_openai(system_prompt, user_prompt, max_tokens=4000, temperature=0.7)
            formatted_content = clean_and_format_content(expanded_raw)
            word_cnt = count_words(formatted_content)
            log(f"  -> ✓ Retry finished Chapter {chap_num}. Generated {word_cnt} words.")
            
        novel_blueprint["chapters"].append({
            "title": chap_title,
            "content": formatted_content
        })
        
        # Sleep to avoid rate limits
        time.sleep(2)
        
    # Write to final pending_novel.json
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(novel_blueprint, f, ensure_ascii=False, indent=2)
        
    log(f"🎉 SUCCESS! Completed V13 gold standard expansion for {draft_data['title']}")
    log(f"Saved complete novel file to: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
