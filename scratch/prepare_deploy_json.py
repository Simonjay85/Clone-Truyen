import json

# Polished Intro from existing_novels.json with V13 improvements
intro_html = """<p><strong>"Cút khỏi Viện Phổi Quốc tế ngay lập tức! Loại bác sĩ Đông y quèn chỉ biết bốc lá cây và châm cứu rác rưởi như mày không xứng đáng đứng chung hàng ngũ với chúng tao!"</strong></p>
<p>Lời mắng chửi tàn nhẫn của Lê Hữu Hoài - Viện trưởng Viện Phổi Quốc tế Việt - Đức - như một nhát búa đập tan năm năm cống hiến thầm lặng của Nguyễn Lâm Phong. Cứu hàng ngàn bệnh nhân và âm thầm nghiên cứu công thức giải độc phế nang đột phá, nhưng thứ Phong nhận lại chỉ là sự phản bội tàn nhẫn từ người thầy kính trọng và vị hôn thê Phan Mỹ Hạnh, kẻ sẵn sàng từ bỏ hôn ước để chạy theo Trần Quốc Dũng, Giám đốc điều hành của tập đoàn hóa chất dược phẩm đa quốc gia NexaCorp.</p>
<p>Bị vu oan ăn cắp vật tư y tế và bị tống cổ khỏi bệnh viện dưới cơn mưa giông tầm tã của Hà Nội, Phong ngỡ như mất tất cả. Thế nhưng, cơ duyên đưa anh gặp Trịnh Khánh Vy, nữ Chủ tịch điều hành vô cùng nhạy bén và sắc sảo của Tập đoàn Y tế Vạn An. Bằng sự kết hợp kỳ diệu giữa bí thuật châm cứu "Cửu Châm Đoạt Mệnh" và các xét nghiệm lâm sàng Tây y hiện đại, Phong cứu sống siêu tỷ phú Trịnh Vạn An khỏi ranh giới sinh tử, chứng minh hiệu quả thần kỳ của phương thuốc cổ truyền. Cùng nhau, họ vượt qua đòn bẩn phong tỏa 24 giờ, dùng bản gốc nhật ký commit Git, bằng sáng chế quốc tế độc quyền, báo cáo kiểm toán Big 4 của EY và lệnh bắt giữ khẩn cấp từ cơ quan C03 Bộ Công an để đè bẹp tập đoàn phản bội, bắt những kẻ kiêu ngạo phải tự quỳ gối đền tội dưới chân mình.</p>"""

with open("scratch/story_3940_polished.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Build deploy payload
deploy_data = {
    "story_id": 3940,
    "title": "Bác Sĩ Đông Y Bị Đuổi Khỏi Viện Phổi, Mũi Kim Thần Đông Tây Kết Hợp Vả Sập Tập Đoàn Phản Bội",
    "intro": intro_html,
    "chapters": [],
    "seo": {
        "focus_keyword": "Bác Sĩ Đông Y Bị Đuổi Khỏi Viện Phổi",
        "seo_title": "Bác Sĩ Đông Y Bị Đuổi Khỏi Viện Phổi, Mũi Kim Thần Đông Tây Kết Hợp Vả Sập Tập Đoàn Phản Bội",
        "seo_description": "Nguyễn Lâm Phong dùng Cửu Châm Đoạt Mệnh và Sâm Đá hồi sinh kẽ phổi, vạch trần âm mưu ăn cắp công trình của Viện trưởng Lê Hữu Hoài."
    }
}

# Add chapters
for idx, ch in enumerate(data["chapters"]):
    deploy_data["chapters"].append({
        "title": ch["title"],
        "content": ch["content"]
    })

with open("scratch/story_3940_deploy_ready.json", "w", encoding="utf-8") as f:
    json.dump(deploy_data, f, indent=4, ensure_ascii=False)

print("✓ Saved deploy-ready payload to scratch/story_3940_deploy_ready.json")
