import os
import json
import time
import requests
import re
import subprocess
import sys

# Ensure we can import from scratch
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'scratch')))
try:
    from novel_editor import get_story_chapters, update_chapter, upload_helper, remove_helper
except Exception as e:
    print("Warning: novel_editor not found", e)

OPENAI_KEY = "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"

def call_openai(system, user):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {"Authorization": f"Bearer {OPENAI_KEY}", "Content-Type": "application/json"}
    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user}
        ],
        "temperature": 0.8
    }
    for _ in range(5):
        try:
            resp = requests.post(url, headers=headers, json=payload, timeout=120)
            return resp.json()["choices"][0]["message"]["content"]
        except Exception as e:
            print("OpenAI error:", e)
            time.sleep(5)
    return ""

def load_json(path, default=None):
    if default is None: default = {}
    if os.path.exists(path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading {path}: {e}")
    return default

def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def generate_novel(idea):
    title = idea["title_hint"]
    theme = idea["theme"]
    protagonist = idea["protagonist"]
    love_interest = idea["love_interest"]
    setting = idea["setting"]
    author = idea["author"]
    
    system_prompt = """Bạn là bậc thầy tiểu thuyết mạng Chuẩn Vàng V13 cho doctieuthuyet.com.
    QUY TẮC BẮT BUỘC (CRITICAL):
    1. TÁCH MỖI CÂU THÀNH 1 HÀNG. Mỗi câu (hoặc lời thoại) phải nằm trong 1 thẻ <p> riêng biệt. Không được viết đoạn văn dài. Xuống dòng liên tục.
    2. CHI TIẾT TẬN CÙNG: Khai thác sâu nội tâm, hội thoại, bối cảnh, mùi vị, âm thanh, trang phục và hậu quả cụ thể. Tuyệt đối không đẩy nhanh tình tiết. Mỗi chương mục tiêu 1000-1500 từ.
    3. Thể loại: Sảng Văn / Vả Mặt, có 3-5 vòng phản kích tăng cấp, không thắng quá dễ.
    4. Bối cảnh Việt Nam 100% chân thực: địa danh, cơ quan, ngân hàng, giấy tờ, chứng cứ và quy trình pháp lý/kinh doanh cụ thể.
    5. Show, Don't Tell: Mô tả hành động, vật lý chi tiết, không lạm dụng "kinh hoàng", "vô biên", "sốc".
    6. Chống template: mỗi truyện phải có story_dna riêng gồm nghề nghiệp, vật chứng trung tâm, 5 set-piece riêng, khủng hoảng giữa truyện và kiểu kết riêng.
    7. Cover prompt phải dành cho ChatGPT Image Generation: tiếng Anh, photorealistic/cinematic, người Việt thật, ảnh 1:1, không chữ, không watermark.
    """
    
    print(f"Generating Clickbait Title based on hint: {title}")
    title_prompt = f"""Tạo MỘT (1) tiêu đề truyện Sảng Văn cực kỳ clickbait, dài 12-22 từ tiếng Việt, có đủ nhục ban đầu -> cú lật -> payoff/vả mặt. KHÔNG dùng lại title_hint ban đầu.
    Gợi ý ban đầu (title_hint): {title}
    Theme: {theme}
    Bối cảnh: {setting}
    Chỉ trả về 1 dòng tiêu đề duy nhất, KHÔNG markdown, KHÔNG ngoặc kép. Ví dụ: Bị Sếp Khinh Thường Đuổi Việc, Tôi Vô Tình Lộ Thân Phận Cổ Đông Lớn Nhất Công Ty"""
    generated_title = call_openai(system_prompt, title_prompt).strip().strip('"').strip("'")
    if not generated_title:
        generated_title = title
    title = generated_title
    print(f"-> CLICKBAIT TITLE: {title}")
    
    print(f"Generating Outline for: {title}")
    outline_prompt = f"""Tạo dàn ý 8-15 chương cho truyện:
    Tiêu đề: {title}
    Theme: {theme}
    Nam chính: {protagonist}
    Nữ chính: {love_interest} (thông minh, sắc sảo)
    Bối cảnh: {setting}
    
    Yêu cầu:
    - Chương 1: Bị sỉ nhục, dồn vào đường cùng.
    - Chương 4-5: Khủng hoảng cực đại.
    - Phải có 3-5 vòng vả mặt tăng cấp.
    - Giữa truyện phải có khủng hoảng thật: đình chỉ, phong tỏa, mất đối tác, truyền thông bẩn, hoặc bẫy pháp lý.
    - Lật kèo bằng chứng cứ nghề nghiệp/pháp lý/kinh doanh cụ thể.
    - Kết truyện có trả giá rõ cho phản diện và một cảnh tình cảm/chữa lành đủ thuyết phục.
    - Trước danh sách chương, tạo `story_dna` riêng để chống trùng template.
    
    Trả về định dạng JSON (chỉ có JSON, không markdown):
    {{
      "story_dna": {{
        "profession_world": "...",
        "central_evidence": "...",
        "unique_set_pieces": ["...", "...", "...", "...", "..."],
        "midpoint_crisis": "...",
        "relationship_signature": "...",
        "ending_signature": "..."
      }},
      "cover_prompt": "Square 1:1 photorealistic Vietnamese web novel cover...",
      "outlines": [
        {{"chap_num": 1, "title": "Chương 1: ...", "outline": "..."}}, ...
      ]
    }}
    """
    outline_res = call_openai(system_prompt, outline_prompt)
    try:
        outline_res = outline_res.replace('```json', '').replace('```', '').strip()
        outline_payload = json.loads(outline_res)
        if isinstance(outline_payload, list):
            outline = outline_payload
            story_dna = {}
            generated_cover_prompt = ""
        else:
            outline = outline_payload["outlines"]
            story_dna = outline_payload.get("story_dna", {})
            generated_cover_prompt = outline_payload.get("cover_prompt", "")
    except:
        print("Failed to parse outline, retrying...")
        return None
        
    print(f"Generating Intro...")
    intro_prompt = f"""Dựa trên truyện: {title}. Viết Intro 3-5 đoạn HTML ngắn, hook mạnh trong 2 câu đầu. Đoạn đầu là 1 câu trích dẫn sỉ nhục cực sốc in đậm <p><strong>...</strong></p>. Hứa hẹn vả mặt tăng cấp và bằng chứng lật kèo, không viết lan man."""
    intro = call_openai(system_prompt, intro_prompt)
    intro = intro.replace('```html', '').replace('```', '').strip()
    
    chapters = []
    for chap in outline:
        print(f"Generating Chapter {chap['chap_num']}...")
        chap_prompt = f"""Viết chi tiết nội dung {chap['title']}.
        Story DNA chống trùng: {json.dumps(story_dna, ensure_ascii=False)}
        Dàn ý chương này: {chap['outline']}
        
        LUẬT TỐI THƯỢNG:
        1. TÁCH MỖI CÂU THÀNH 1 HÀNG. Bọc mỗi câu trong 1 thẻ <p>. Ví dụ:
        <p>Anh ta bước đi.</p>
        <p>"Mày nghĩ mày là ai?" Hắn cười khẩy.</p>
        <p>Gió thổi tung tà áo.</p>
        2. TUYỆT ĐỐI KHÔNG GỘP NHIỀU CÂU VÀO 1 THẺ <P>.
        3. CỰC KỲ DÀI VÀ CHI TIẾT (Bắt buộc phải đạt 1000 - 1500 từ). Mô tả nội tâm nhân vật sâu sắc, các đoạn hội thoại tranh luận qua lại nhiều lần. Mô tả quang cảnh, âm thanh, mùi vị, trang phục chi tiết. TUYỆT ĐỐI KHÔNG đốt cháy giai đoạn. Kéo dài diễn biến của một tình huống càng lâu càng tốt.
        4. Trả về mã HTML thuần túy, không chứa markdown ```html.
        """
        chap_content = call_openai(system_prompt, chap_prompt)
        chap_content = chap_content.replace('```html', '').replace('```', '').strip()
        chapters.append({
            "title": chap['title'],
            "content": chap_content
        })
        
    novel_data = {
        "title": title,
        "author": author,
        "genre": "Sảng Văn",
        "intro": intro,
        "cover_prompt": generated_cover_prompt or f"Square 1:1 photorealistic Vietnamese web novel cover, real human actors, cinematic movie poster, {setting}, a wronged Vietnamese protagonist preparing a legal and business comeback, dramatic conflict visible, dark top 30 percent for title readability, high contrast lighting, no text, no watermark.",
        "chapters": chapters
    }
    return novel_data

def publish_novel():
    print("Publishing novel...")
    result = subprocess.run(["python3", "publish_local_novel.py"], capture_output=True, text=True)
    out = result.stdout
    print(out)
    match = re.search(r"Successfully imported novel '.*?' with ID: (\d+)", out)
    if match:
        return int(match.group(1))
    return None

def evaluate_novel(novel_data):
    # Quick LLM evaluate
    prompt = f"""Đánh giá truyện Sảng Văn sau trên thang 1-10:
    Tiêu đề: {novel_data['title']}
    Số chương: {len(novel_data['chapters'])}
    Intro: {novel_data['intro']}
    
    Chỉ trả về 1 con số (ví dụ: 8.5)
    """
    res = call_openai("Bạn là giám khảo.", prompt)
    try:
        return float(re.findall(r"[\d\.]+", res)[0])
    except:
        return 8.0

def main():
    os.chdir("/Users/aaronnguyen/TN/App/doctieuthuyet")
    pipeline_path = "scratch/pipeline_100.json"
    progress_path = "scratch/progress.json"
    existing_path = "existing_novels.json"
    
    pipeline = load_json(pipeline_path)
    progress = load_json(progress_path, {"completed": [], "published": [], "batch_scores": {}})
    
    ideas = pipeline.get("novel_ideas", [])
    
    for idea in ideas:
        novel_id = idea["id"]
        if novel_id in progress["completed"]:
            continue
            
        print(f"=== BẮT ĐẦU TRUYỆN #{novel_id} ===")
        
        # Xóa pending_novel.json cũ nếu có
        if os.path.exists("pending_novel.json"):
            os.remove("pending_novel.json")
            
        novel_data = None
        while not novel_data:
            novel_data = generate_novel(idea)
            
        save_json("pending_novel.json", novel_data)
        
        story_id = publish_novel()
        if not story_id:
            print("Publish failed, retrying once...")
            time.sleep(10)
            story_id = publish_novel()
            
        if story_id:
            score = evaluate_novel(novel_data)
            print(f"Thành công! Story ID: {story_id}, Điểm: {score}")
            progress["completed"].append(novel_id)
            progress["published"].append({
                "novel_id": novel_id,
                "story_id": story_id,
                "title": novel_data["title"],
                "score": score
            })
            save_json(progress_path, progress)
            
            # Cập nhật existing_novels.json
            existing = load_json(existing_path, [])
            existing.append({
                "id": story_id,
                "title": novel_data["title"],
                "author": novel_data["author"]
            })
            save_json(existing_path, existing)
            
        else:
            print(f"Lỗi khi publish truyện #{novel_id}. Bỏ qua.")
            
        # Nghỉ chút
        time.sleep(5)

if __name__ == "__main__":
    main()
