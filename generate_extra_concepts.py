#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generate_extra_concepts.py — Generates 13 new V13 Vietnamese sảng văn concepts (indices 51 to 63) and appends to novel_concepts_50.json.
"""

import os
import json
import requests
import re
import sys

OPENAI_KEY = "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"
CONCEPTS_PATH = "novel_concepts_50.json"

def call_openai(system_prompt, user_prompt):
    url = "https://api.openai.com/v1/chat/completions"
    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        "temperature": 0.8,
        "max_tokens": 3000
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_KEY}"
    }
    
    res = requests.post(url, json=payload, headers=headers, timeout=120)
    res.raise_for_status()
    data = res.json()
    return data['choices'][0]['message']['content'].strip()

def robust_json_parse(raw_str):
    cleaned = raw_str.strip()
    if cleaned.startswith("```"):
        cleaned = re.sub(r"^```(?:json)?\n", "", cleaned)
        cleaned = re.sub(r"\n```$", "", cleaned).strip()
    try:
        return json.loads(cleaned)
    except Exception as parse_err:
        start_idx = cleaned.find("[")
        end_idx = cleaned.rfind("]")
        if start_idx != -1 and end_idx != -1 and end_idx > start_idx:
            try:
                return json.loads(cleaned[start_idx:end_idx+1])
            except Exception:
                pass
        raise parse_err

def main():
    print("🚀 EXPANDING CONCEPTS POOL TO 63 NOVELS...")
    
    if not os.path.exists(CONCEPTS_PATH):
        print(f"❌ Error: {CONCEPTS_PATH} not found.")
        sys.exit(1)
        
    with open(CONCEPTS_PATH, "r", encoding="utf-8") as f:
        concepts = json.load(f)
        
    print(f"Current concepts count: {len(concepts)}")
    
    # Check if indices 51 to 63 already exist
    existing_indices = {c["idx"] for c in concepts}
    missing_indices = [idx for idx in range(51, 64) if idx not in existing_indices]
    
    if not missing_indices:
        print("✓ All indices 51 to 63 are already present in novel_concepts_50.json.")
        return
        
    print(f"Generating missing indices: {missing_indices}")
    
    system_prompt = """Bạn là biên tập viên văn học kỳ cựu và là bậc thầy lập kịch bản sảng văn/vả mặt đô thị tài phiệt số 1 Việt Nam.
Nhiệm vụ của bạn là tạo ra các concept truyện sảng văn/vả mặt V13 cực kỳ đặc sắc, lấy bối cảnh 100% tại Việt Nam.

QUY TẮC PHẢI TUÂN THỦ:
1. CẤM PLOT AI/API: Tuyệt đối không cho nhân vật chính khởi nghiệp hay lật kèo bằng việc viết API, tích hợp AI ChatGPT hay vẽ tranh AI. Mọi cú lật kèo phải sử dụng bằng chứng kinh điển: sao kê đóng dấu đỏ, video camera an ninh, nhật ký commit Git cục bộ, hợp đồng sở hữu trí tuệ chính thức, kiểm toán Big 4, hoặc sự can thiệp quyết liệt của lực lượng cảnh sát C03.
2. NHÂN VẬT NỮ ĐỒNG HÀNH LÝ TÍNH: Mỹ nhân hào môn phải thông minh, thực tế, luôn thương lượng trên các điều khoản thương mại sòng phẳng (ví dụ: CFO quỹ đầu tư lớn thẩm định kỹ trước khi rót vốn).
3. ĐA DẠNG NGÀNH NGHỀ VIỆT NAM: Hãy chọn các ngành thực tế ở các địa phương Việt Nam (Ví dụ: nước mắm Phú Quốc, gốm sứ Bát Tràng, cà phê Buôn Ma Thuột, du lịch Nha Trang, hải sản Quảng Ninh, dệt may Bình Dương, v.v.).
4. ĐỊNH DẠNG: Xuất ra mảng JSON hợp lệ chứa các concept mới."""

    user_prompt = f"""Hãy tạo đúng {len(missing_indices)} concept truyện mới cho các chỉ số (idx) sau: {missing_indices}.
Mỗi concept trong mảng phải có cấu trúc chính xác sau:
{{
  "idx": [chỉ số idx],
  "title": "[Tiêu đề dài 12-22 từ, giật gân, cuốn hút, thể hiện rõ mâu thuẫn khốc liệt]",
  "author": "[Tên tác giả người Việt]",
  "num_chapters": 10,
  "setting": "[Địa điểm thực tế ở Việt Nam, cơ quan nhà nước, ngân hàng]",
  "male_lead": "[Tên nam chính, nghề nghiệp, mâu thuẫn ban đầu]",
  "female_lead": "[Tên nữ chính, chức vụ lớn (CFO/VP/Kiểm toán viên), vai trò lý tính]",
  "conflict": "[Mâu thuẫn kinh doanh thực tế, không có AI, ví dụ: đối thủ mua chuộc kiểm nghiệm viên phá hoại chất lượng nước mắm, nam chính phản đòn bằng kết quả GC-MS và C03 vào cuộc]",
  "cover_desc": "[Mô tả ảnh bìa chi tiết bằng tiếng Anh phục vụ AI vẽ tranh. Yêu cầu: Cinematic drama character poster, nhân vật nam/nữ chính đứng ở bối cảnh Việt Nam, strictly frame character in the middle and lower 65%, top 35% is empty dark sky or dark empty wall covered in shadow, photorealistic, no text]",
  "genre_visual": "[Thể loại visual của ảnh bìa, ví dụ: fish sauce industry empire drama]"
}}

Hãy trả về duy nhất mảng JSON nguyên bản, không chứa ```json hay ```."""

    try:
        raw_res = call_openai(system_prompt, user_prompt)
        new_concepts = robust_json_parse(raw_res)
        
        # Verify indices and merge
        for nc in new_concepts:
            idx = nc["idx"]
            if idx in missing_indices:
                concepts.append(nc)
                print(f"✓ Generated concept index {idx}: {nc['title']}")
                
        # Sort concepts by index to be clean
        concepts.sort(key=lambda x: x["idx"])
        
        with open(CONCEPTS_PATH, "w", encoding="utf-8") as f:
            json.dump(concepts, f, ensure_ascii=False, indent=2)
            
        print(f"🎉 Successfully expanded novel_concepts_50.json to {len(concepts)} total concepts!")
    except Exception as e:
        print(f"❌ Failed to generate and save new concepts: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
