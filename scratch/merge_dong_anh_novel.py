import os
import json

def main():
    print("=" * 60)
    print("🔄 MERGING CHAPTERS FOR: TRỌNG SINH 2008: CƠN SỐT ĐẤT ĐÔNG ANH")
    print("=" * 60)
    
    drafts_dir = "/Users/aaronnguyen/TN/App/doctieuthuyet/scratch/dong_anh_drafts"
    chapters = []
    
    for i in range(1, 9):
        file_path = os.path.join(drafts_dir, f"chap{i}.json")
        if not os.path.exists(file_path):
            print(f"❌ Error: {file_path} not found!")
            return
            
        with open(file_path, "r", encoding="utf-8") as f:
            chap_data = json.load(f)
            
        word_count = len(chap_data['content'].split())
        char_count = len(chap_data['content'])
        print(f"✓ Loaded Chapter {i}: {chap_data['title']} ({char_count} chars, ~{word_count} words)")
        
        # Verify word count meets V12 standard (1000 - 1500 words or 1200 - 1800 words)
        if word_count < 1000:
            print(f"⚠️ WARNING: Chapter {i} is below 1000 words! ({word_count} words)")
        elif word_count > 1800:
            print(f"⚠️ WARNING: Chapter {i} is above 1800 words! ({word_count} words)")
            
        chapters.append({
            "title": chap_data['title'],
            "content": chap_data['content']
        })
        
    intro = """<p><strong>"Ba năm trước, tôi chết trong nghèo khổ bên vệ đường Hà Nội, bị kẻ thù cướp sạch dự án bất động sản tâm huyết và đẩy gia đình vào nợ nần chồng chất."</strong></p>
<p>Nhưng ông trời có mắt! Tôi mở mắt ra và thấy mình quay về mùa hè năm 2008 — thời điểm lịch sử khi Hà Tây chuẩn bị sáp nhập vào Hà Nội, và vùng đất Đông Anh đang trước thềm cơn sốt đất làm rung chuyển giới đầu cơ thủ đô. Với ký ức vô giá về mọi mốc quy hoạch: cầu Nhật Tân, đường vành đai 3, đại lộ Võ Nguyên Giáp, tôi thề sẽ lấy lại tất cả những gì thuộc về mình!</p>
<p>Nhưng thương trường là chiến trường khốc liệt. Đối đầu với ông trùm tín dụng đen Hoàng Mạnh Cường câu kết với các nhóm lợi ích tham lam, Trần Huy phải cùng Nguyễn Thanh Vy — ái nữ sắc sảo của Tập đoàn xây dựng Thanh Bình — lập nên liên minh thế kỷ. Một bộ truyện sảng văn/vả mặt tuyệt đỉnh với những cú lật kèo pháp lý, tài chính tinh vi chuẩn xác sẽ đưa bạn vào trung tâm cơn sốt đất vàng Hà Thành!</p>"""

    cover_prompt = "A highly detailed, professional anime-style book cover, a young determined Vietnamese man in a modern casual suit overlooking a vast river with a grand bridge in the golden hour sunset, cinematic lighting, vivid colors, premium web novel art look"

    pending_data = {
        "title": "Trọng Sinh 2008: Cơn Sốt Đất Đông Anh",
        "author": "Thanh Phong",
        "genre": "Sảng Văn",
        "intro": intro,
        "cover_prompt": cover_prompt,
        "chapters": chapters
    }
    
    pending_file = "/Users/aaronnguyen/TN/App/doctieuthuyet/pending_novel.json"
    with open(pending_file, "w", encoding="utf-8") as f:
        json.dump(pending_data, f, ensure_ascii=False, indent=2)
        
    print("\n✓ Successfully assembled and saved pending_novel.json!")
    print("=" * 60)

if __name__ == "__main__":
    main()
