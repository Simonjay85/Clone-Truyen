import json
import os
import sys
import re
import urllib.parse
import random
import time

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import novel_editor

def split_into_single_sentences(text):
    # Strip HTML tags and normalize spaces
    text = re.sub(r'</?p>', ' ', text)
    text = re.sub(r'<br\s*/?>', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    
    # Tokenize the text into narrative and dialogue blocks
    tokens = []
    # Match various smart and standard double quotes
    pattern = re.compile(r'([“"[].*?[”"\]])')
    last_end = 0
    for match in pattern.finditer(text):
        start, end = match.span()
        if start > last_end:
            tokens.append(('narrative', text[last_end:start]))
        tokens.append(('dialogue', text[start:end]))
        last_end = end
    if last_end < len(text):
        tokens.append(('narrative', text[last_end:]))
        
    # Process tokens
    processed_blocks = []
    for i, (t_type, t_val) in enumerate(tokens):
        t_val = t_val.strip()
        if not t_val:
            continue
        
        if t_type == 'narrative':
            # Split narrative into sentences
            sub_parts = re.split(r'([.!?…]+(?:\s+|$))', t_val)
            sub_sentences = []
            current = ""
            for j in range(0, len(sub_parts), 2):
                chunk = sub_parts[j]
                delim = sub_parts[j+1] if j+1 < len(sub_parts) else ""
                current += chunk + delim
                if delim or j == len(sub_parts) - 1:
                    if current.strip():
                        sub_sentences.append(current.strip())
                    current = ""
            
            for s in sub_sentences:
                processed_blocks.append(('narrative', s))
        else:
            processed_blocks.append(('dialogue', t_val))
            
    # Now merge dialogue with introducing phrase if the preceding block ends with colon or comma
    final_sentences = []
    skip_next = False
    for i in range(len(processed_blocks)):
        if skip_next:
            skip_next = False
            continue
            
        t_type, t_val = processed_blocks[i]
        if t_type == 'narrative' and (t_val.endswith(':') or t_val.endswith(',')) and i + 1 < len(processed_blocks) and processed_blocks[i+1][0] == 'dialogue':
            # Merge narrative and dialogue
            final_sentences.append(t_val + " " + processed_blocks[i+1][1])
            skip_next = True
        else:
            final_sentences.append(t_val)
            
    # Wrap in <p> tags
    formatted = ""
    for s in final_sentences:
        if s.strip():
            formatted += f"<p>{s.strip()}</p>\n"
    return formatted

def process_novel_1927():
    print("=== PROCESSING NOVEL 1927 ===")
    with open("scratch/original_1927.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        
    novel_editor.upload_helper()
    
    # 1. Update Title and Intro
    title = "Nhà Của Mẹ Chồng? Không, Biệt Thự Gò Vấp 5 Tỷ Đứng Tên Riêng Của Tôi!"
    intro = ("<p>Mâm cơm giỗ ba chồng, mẹ chồng sỉ nhục tôi là \"person ngoài\" trước mặt họ hàng.</p>"
             "<p>Chị chồng cười khẩy, chồng thì cúi đầu làm thinh.</p>"
             "<p>Nhưng họ không biết, căn biệt thự ba tầng mặt tiền Gò Vấp trị giá hơn 5 tỷ đồng họ đang ngồi ăn sướng miệng đã đứng tên riêng của tôi từ lâu!</p>"
             "<p>Một bộ truyện sảng văn gia đình cực kỳ xuất sắc với những cú lật kèo pháp lý sắc bén sẽ mang đến cho bạn cảm giác vả mặt sảng khoái tột cùng!</p>")
             
    print("Updating story meta for 1927...")
    res = novel_editor.update_story_meta(1927, title=title, intro=intro)
    print("Meta result:", res)
    
    # 2. Update Cover
    cover_prompt = "highly detailed book cover, anime illustration style, a premium modern luxury villa in Go Vap Saigon at twilight, warm window lights, vivid colors, cinematic lighting, professional illustration, no text, no logo"
    escaped_prompt = urllib.parse.quote(cover_prompt)
    cover_url = f"https://image.pollinations.ai/prompt/{escaped_prompt}?width=1200&height=1200&seed={random.randint(1, 99999)}&nologo=true"
    print("Updating cover for 1927...")
    res = novel_editor.update_story_cover(1927, cover_url)
    print("Cover result:", res)
    
    # 3. Format and update chapters
    chapters = data.get("chapters", [])
    print(f"Found {len(chapters)} chapters for 1927.")
    
    # Let's get the official chapters list from WordPress first to match IDs
    wp_chapters = novel_editor.get_story_chapters(1927).get("chapters", [])
    print(f"WordPress has {len(wp_chapters)} chapters.")
    
    for i, ch in enumerate(chapters):
        c_title = ch["title"]
        c_content = ch["content"]
        
        # Split into single-sentence paragraphs
        formatted_content = split_into_single_sentences(c_content)
        
        # Match by index
        if i < len(wp_chapters):
            wp_id = wp_chapters[i]["id"]
            print(f"Updating Chapter {i+1} (ID: {wp_id}): {c_title}")
            res = novel_editor.update_chapter(wp_id, c_title, formatted_content)
            print("Result:", res)
        else:
            print(f"Warning: WordPress does not have Chapter {i+1}!")
        time.sleep(0.5)
        
    novel_editor.remove_helper()
    print("Finished Novel 1927!")

def process_novel_1948():
    print("=== PROCESSING NOVEL 1948 ===")
    with open("scratch/original_1948.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        
    novel_editor.upload_helper()
    
    # 1. Update Title and Intro
    title = "Giám Đốc Ngầm: Thực Tập Sinh Trăm Tỷ Vả Mặt Trưởng Phòng Nhân Sự Cướp Dự Án"
    intro = ("<p>Lâm Uyển Nhu, ái nữ duy nhất của Chủ tịch tập đoàn Lâm Thị, quyết định ẩn thân làm thực tập sinh quèn để trải nghiệm thực tế và vạch trần những góc tối công sở.</p>"
             "<p>Nhưng Trưởng phòng nhân sự đố kỵ và cướp công luôn tìm cách chà đạp cô, thậm chí gài bẫy để cô bị sa thải và cướp dự án trăm tỷ.</p>"
             "<p>Họ không ngờ, giám đốc điều hành trẻ tuổi Lục Dạ Minh và cả vị Chủ tịch tối cao đứng sau cô sẵn sàng lột mặt nạ từng kẻ kiêu ngạo!</p>"
             "<p>Văn phong V12 sảng văn đô thị kịch tính, lật kèo thông minh bằng bằng chứng và tài chính đỉnh cao!</p>")
             
    print("Updating story meta for 1948...")
    res = novel_editor.update_story_meta(1948, title=title, intro=intro)
    print("Meta result:", res)
    
    # 2. Update Cover
    cover_prompt = "highly detailed book cover, anime illustration style, a beautiful confident Vietnamese female business executive in a high-rise office overlooking Saigon skyline at sunset, gorgeous lighting, premium illustration, no text, no logo"
    escaped_prompt = urllib.parse.quote(cover_prompt)
    cover_url = f"https://image.pollinations.ai/prompt/{escaped_prompt}?width=1200&height=1200&seed={random.randint(1, 99999)}&nologo=true"
    print("Updating cover for 1948...")
    res = novel_editor.update_story_cover(1948, cover_url)
    print("Cover result:", res)
    
    # 3. Format and update chapters
    chapters = data.get("chapters", [])
    print(f"Found {len(chapters)} chapters for 1948.")
    
    wp_chapters = novel_editor.get_story_chapters(1948).get("chapters", [])
    print(f"WordPress has {len(wp_chapters)} chapters.")
    
    for i, ch in enumerate(chapters):
        c_title = ch["title"]
        c_content = ch["content"]
        
        # Split into single-sentence paragraphs
        formatted_content = split_into_single_sentences(c_content)
        
        # Match by index
        if i < len(wp_chapters):
            wp_id = wp_chapters[i]["id"]
            print(f"Updating Chapter {i+1} (ID: {wp_id}): {c_title}")
            res = novel_editor.update_chapter(wp_id, c_title, formatted_content)
            print("Result:", res)
        else:
            print(f"Warning: WordPress does not have Chapter {i+1}!")
        time.sleep(0.5)
        
    novel_editor.remove_helper()
    print("Finished Novel 1948!")

if __name__ == "__main__":
    process_novel_1927()
    process_novel_1948()
