import os
import json

def count_words(text):
    return len(text.strip().split())

def main():
    chapters_dir = "/Users/aaronnguyen/TN/App/doctieuthuyet/scratch/chapters"
    if not os.path.exists(chapters_dir):
        os.makedirs(chapters_dir)
        print(f"✓ Created directory: {chapters_dir}")
        return

    novel_data = {
        "title": "Vương Quốc Nước Mắm Truyền Thống Phú Quốc: Chàng Rể Ẩn Thế Vực Dậy Quốc Hồn",
        "author": "Đông Hải Cư Sĩ",
        "genre": "Sảng Văn",
        "intro": (
            "<p><strong>\"Trịnh Gia Huy, nghệ nhân ủ chượp kiêm chuyên gia sinh hóa thực phẩm xuất sắc nhất đảo ngọc Phú Quốc, "
            "bị gã anh rể hách dịch vu oan trộm cắp công thức, đạp ngã bên sườn đồi Dương Đông, "
            "đổ sạch sành sanh ba trăm thùng chượp nước mắm hoàng kim mà anh ủ ròng rã suốt ba năm trời...\"</strong></p>"
            "<p>Thế nhưng chúng không bao giờ có thể ngờ rằng, đống nước mắm hóa chất công nghiệp mà chúng đang hăm hở sản xuất "
            "chỉ là thứ độc dược trá hình. Bằng phương pháp tách chiết ly tâm sinh học tự nhiên và công nghệ độc bản lọc Histamine, "
            "Gia Huy kết hợp cùng đại tiểu thư Nguyễn Thanh Mai - ái nữ của tập đoàn resort 5 sao lớn nhất Việt Nam - "
            "đã vực dậy vương quốc nước mắm truyền thống, giăng ra cái bẫy pháp lý và kinh tế hoàn hảo để tống giam lũ gian thương hèn hạ, "
            "phục hưng quốc hồn quốc túy ẩm thực Việt Nam.</p>"
        ),
        "cover_prompt": (
            "A premium book cover, highly detailed anime illustration, a powerful young Vietnamese man with determined eyes "
            "standing next to giant traditional wooden barrels of fish sauce in a sunny Phu Quoc island setting, with a beautiful "
            "and sophisticated luxury resort and turquoise sea in the background. Cinematic lighting, professional typhography, "
            "dramatic shadows, vivid colors."
        ),
        "chapters": []
    }

    chapter_files = sorted([f for f in os.listdir(chapters_dir) if f.startswith("chapter_") and f.endswith(".txt")])

    if not chapter_files:
        print("❌ No chapter files found! Please write the chapter text files first under scratch/chapters/")
        return

    for filename in chapter_files:
        filepath = os.path.join(chapters_dir, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()

        raw_text = "".join(lines)
        word_count = count_words(raw_text)
        print(f"📖 Processing {filename}... Word count: {word_count}")

        # V12 formatting: wrap each sentence in a <p> tag
        formatted_paragraphs = []
        for line in lines:
            trimmed = line.strip()
            if not trimmed:
                continue
            # If the line already has <p>, keep it; otherwise wrap it
            if trimmed.startswith("<p>") and trimmed.endswith("</p>"):
                formatted_paragraphs.append(trimmed)
            else:
                # Basic escape for HTML safety (though sảng văn shouldn't have raw html elements in narrative text)
                formatted_paragraphs.append(f"<p>{trimmed}</p>")

        chapter_content = "".join(formatted_paragraphs)
        chapter_title = f"Chương {filename.split('_')[1].split('.')[0]}: "
        
        # Determine specific titles based on filename
        num = filename.split('_')[1].split('.')[0]
        if num == "1":
            chapter_title += "Nhà Thùng Nhục Nhã"
        elif num == "2":
            chapter_title += "Mỹ Nhân Resort 5 Sao"
        elif num == "3":
            chapter_title += "Khủng Hoảng Truyền Thông Bẩn"
        elif num == "4":
            chapter_title += "Kỹ Thuật Lọc Độc Bản Lật Ngược Thế Cờ"
        elif num == "5":
            chapter_title += "Phán Quyết C03 Và Hôn Ước Vàng"

        novel_data["chapters"].append({
            "title": chapter_title,
            "content": chapter_content
        })

    # Save to pending_novel.json
    output_path = "/Users/aaronnguyen/TN/App/doctieuthuyet/pending_novel.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(novel_data, f, ensure_ascii=False, indent=2)

    print("=" * 60)
    print(f"🎉 SUCCESS: Compiled {len(novel_data['chapters'])} chapters into pending_novel.json")
    print("=" * 60)

if __name__ == "__main__":
    main()
