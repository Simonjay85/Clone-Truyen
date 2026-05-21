import json
import os

def main():
    pending_file = "/Users/aaronnguyen/TN/App/doctieuthuyet/pending_novel.json"
    
    # Read chapters
    chapters = []
    titles = [
        "Chương 1: Cú Đánh Úp Nửa Đêm Của Gã Khổng Lồ",
        "Chương 2: Đêm Trắng Ban Công Và Thỏa Thuận Sòng Phẳng",
        "Chương 3: Bẫy Sập Và Lời Đề Nghị Rác Thải",
        "Chương 4: C03 Vào Cuộc Và Chìa Khóa Blockchain",
        "Chương 5: Hào Quang Organic Việt Và Lời Hứa Hoàng Hôn"
    ]
    
    for i in range(1, 6):
        path = f"/Users/aaronnguyen/TN/App/doctieuthuyet/scratch/chapter_{i}.html"
        with open(path, "r", encoding="utf-8") as f:
            content = f.read().strip()
        chapters.append({
            "title": titles[i-1],
            "content": content
        })
        
    intro = """<p><strong>"Trần Quốc Bảo, người sáng lập chuỗi Bảo Long Tea thuần hữu cơ bị đối thủ đa quốc gia Royal Sip hãm hại bằng truyền thông bẩn bôi nhọ chè chứa Glyphosate gây ung thư, toàn bộ chi nhánh bị Quản lý thị trường tạm đình chỉ 24 giờ..."</strong></p>
<p>Thế nhưng họ không ngờ, từng ly trà của Bảo Long Tea đều được dán nhãn QR truy xuất nguồn gốc bằng công nghệ Blockchain thời gian thực liên kết thiết bị IoT tại nông trường Bảo Lộc. Sự minh bạch tối thượng ấy kết hợp với trí tuệ lý tính, sắc sảo của đại tiểu thư logistics Nguyễn Phương Thảo đã chắp cánh cho Bảo Long Tea lật ngược thế cờ ngoạn mục. Với sự vào cuộc điều tra quyết liệt của C03 Bộ Công An và A05 Cục An ninh mạng, đường dây bôi nhọ giả mạo con dấu Viện Pasteur bị phanh phui, kẻ phản diện hống hách Henry Wong bị khởi tố bắt giam ngay tại chỗ. Một bản hùng ca ngọt ngào về nông sản sạch Việt Nam và tình yêu tự nguyện chớm nở dưới hoàng hôn Sài Gòn.</p>"""

    cover_prompt = "Vua Ban Le Duong Pho Sai Gon book cover, dramatic low angle shot, a handsome Vietnamese entrepreneur man in smart casual attire standing side by side with a stunning and intelligent Vietnamese business woman with high ponytail on a modern high-rise balcony looking at the gorgeous sunset over Ho Chi Minh City skyline, bright warm lighting, professional anime digital art style, photorealistic details, high-end F&B retail aesthetic, deep warm orange and gold hues, highly detailed, masterpieces"

    novel_data = {
        "title": "Vua Bán Lẻ Đường Phố Sài Gòn: Trận Chiến Sinh Tử Của Chuỗi Trà Ô Long Organic Việt",
        "author": "Bảo Quốc Sài Thành",
        "genre": "Sảng Văn",
        "intro": intro,
        "cover_prompt": cover_prompt,
        "chapters": chapters
    }
    
    with open(pending_file, "w", encoding="utf-8") as f:
        json.dump(novel_data, f, ensure_ascii=False, indent=2)
        
    print("✓ Successfully generated pending_novel.json at:", pending_file)

if __name__ == "__main__":
    main()
