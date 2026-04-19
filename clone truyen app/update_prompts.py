import os

file_path = "/Users/aaronnguyen/TN/App/Clone Truyen/clone truyen app/src/lib/engine.ts"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update Puppet Master
content = content.replace(
    "Thành công của truyện phụ thuộc vào Drama, tính cách nhân vật có chiều sâu, vết thương lòng trong quá khứ.",
    "Thành công của truyện phụ thuộc vào Drama, tính cách nhân vật có chiều sâu, vết thương lòng trong quá khứ. ĐẶC BIỆT: Nhân vật phụ/phản diện khi chuyển biến phải có xung đột nội tâm sâu sắc, vật lộn với lòng kiêu ngạo, không 'quay xe' đột ngột thiếu logic."
)

# 2. Update Expand Rules
expand_rule_orig = "QUY TẮC CỐT LÕI TỪ NHÀ SẢN XUẤT: Bắt buộc thiết kế một chương 'Phản đòn' từ phe phản diện khiến nữ chính bị lộ tẩy hoặc đẩy vào chân tường trước khi cô lật kèo! VỀ TIÊU ĐỀ CHƯƠNG: TUYỆT ĐỐI KHÔNG dùng lặp lại quá 2 lần các từ chung chung như 'Bí mật', 'Bí ẩn', 'Cuộc gặp', 'Bất ngờ'. BẮT BUỘC dùng cấu trúc ĐỘNG TỪ MẠNH, SÁT THƯƠNG CAO ở mỗi đầu chương (Ví dụ: Bóc phốt, Lột mặt nạ, Tước đoạt, Đập tan tành, Xé nát sự thật, Bẫy gông cùm...)."

expand_rule_new = """QUY TẮC CỐT LÕI TỪ NHÀ SẢN XUẤT: 
- CẤM LORE DUMP: Không nhồi nhét bối cảnh, rải rác 'world-building' chậm rãi qua hành động.
- BẪY & MANH MỐI GIẢ: Xuyên suốt phải có chướng ngại vật thực sự, linh hồn lừa gạt hoặc thông tin sai. Không giải quyết quá 'tiện lợi'.
- CẤM CLICHÉ: Kết thúc cấm dùng 'sức mạnh tình bạn/tình yêu'. Phải dựa trên luật lệ logic, có sự hy sinh (Sacrifice-based) và Plot Twist quay xe.
- Bắt buộc thiết kế chương 'Phản đòn' đẩy nữ chính vào chân tường! VỀ TIÊU ĐỀ: BẮT BUỘC dùng ĐỘNG TỪ MẠNH (Bóc phốt, Lột mặt nạ, Tước đoạt...). Cấm lặp từ 'Bí mật', 'Bất ngờ'."""

content = content.replace(expand_rule_orig, expand_rule_new)

# 3. Update Write/Rewrite Rules (Ghostwriter, MicroDrama, Grok, Claude, Gemini Rewrite)
# Instead of replacing exact lines, we find the "Tỉ lệ hội thoại phải chiếm ít nhất 60% thời lượng chương" part and inject the new rule right after.

content = content.replace(
    "Tỉ lệ hội thoại phải chiếm ít nhất 60% thời lượng chương. Các nhân vật phải cãi vã, châm biếm, và đối thoại mỉa mai liên tục bằng ngôn ngữ đời thường, ngắn gọn như dao găm.",
    "Tỉ lệ hội thoại phải chiếm ít nhất 60% thời lượng chương. [CẤM sáo rỗng: Tuyệt đối không dùng từ khinh miệt rập khuôn như 'nhà quê', 'hậu đậu'. Hãy bắt nạt bằng thế thượng đẳng, bạo lực lạnh, cô lập, nụ cười giả tạo]. Các nhân vật phải đối thoại mỉa mai, châm biếm liên tục bằng ngôn ngữ đời thường, sắc bén như dao găm."
)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated prompts successfully")
