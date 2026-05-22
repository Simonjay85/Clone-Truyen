import json

temp_file_path = "/Users/aaronnguyen/TN/App/doctieuthuyet/pending_novel_9_temp.json"
with open(temp_file_path, "r", encoding="utf-8") as f:
    novel_data = json.load(f)

# Find Chapter 5
ch5 = novel_data["chapters"][4] # 0-indexed: ch1 is 0, ch2 is 1, ch3 is 2, ch4 is 3, ch5 is 4

# Let's see current content sentences
sentences = ch5["content"].split("</p>\\n")
# Clean up
sentences = [s.replace("<p>", "").replace("</p>", "").strip() for s in sentences if s.strip()]

extra_sentences = [
    "Cộng đồng âm nhạc cổ điển trong nước bắt đầu xôn xao bàn tán về lá thư giới thiệu đầy quyền lực của Giáo sư Janusz Olejniczak.",
    "Bản thân vị giáo sư người Ba Lan này là một tượng đài sống, người đã từng đào tạo ra nhiều thế hệ nghệ sĩ piano đoạt giải vàng thế giới.",
    "Trong bức thư, giáo sư viết rõ: 'Tôi đã nghe bản demo của Lam Hoang Phuc, tiếng đàn của cậu ấy mang linh hồn của Chopin, một sự kết hợp hoàn mỹ giữa kỹ thuật điêu luyện và cảm xúc dạt dào'.",
    "Đây là lời khen ngợi cao nhất mà giáo sư từng dành cho một nghệ sĩ trẻ châu Á từ trước đến nay.",
    "Tại Đại sứ quán Ba Lan ở Hà Nội trên đường Chùa Một Cột, việc cấp thị thực ngoại giao cho Phúc được tiến hành chỉ trong vòng hai mươi bốn giờ.",
    "Ngài Đại sứ đích thân ký phê duyệt visa dài hạn, chúc Phúc sẽ tỏa sáng rực rỡ tại thủ đô Warsaw lịch sử.",
    "Sự kiện này như một gáo nước lạnh dội thẳng vào âm mưu bẩn thỉu của cha con Nguyễn Thế Phong, khiến mọi nỗ lực ngăn chặn của họ trở nên lố bịch.",
    "Nhà báo Hoàng Nam của báo Tuổi Trẻ đã viết một bài bình luận sâu sắc: 'Khi một tài năng thực sự được thế giới công nhận, mọi xiềng xích của quyền lực cục bộ đều trở nên bất lực'.",
    "Phúc ngồi trong khoang hạng nhất, ngắm nhìn bầu trời đêm rực rỡ ngàn sao qua cửa sổ máy bay, lòng tự hứa sẽ không phụ sự kỳ vọng của cô Diệu Linh và giáo sư."
]

# Insert them near the end or at the end
sentences.extend(extra_sentences)

# Re-format Chapter 5
content = ""
for s in sentences:
    content += f"<p>{s}</p>\\n"
if content.endswith("\\n"):
    content = content[:-2]

ch5["content"] = content
novel_data["chapters"][4] = ch5

# Write back
with open(temp_file_path, "w", encoding="utf-8") as f:
    json.dump(novel_data, f, ensure_ascii=False, indent=2)

print("Chapter 5 successfully expanded.")
