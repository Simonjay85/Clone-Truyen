import re

filepath = "src/lib/engine.ts"
with open(filepath, 'r') as f:
    content = f.read()

# We want to replace the weak instruction with a very strict instruction for ALL Expand agents
# Let's target the exact string:
old_str_1 = "Tự đánh giá độ phức tạp của cốt truyện để quyết định số chương phù hợp,"
new_str_1 = "MỆNH LỆNH TỐI THƯỢNG: TUYỆT ĐỐI PHẢI OUTPUT CHÍNH XÁC ĐÚNG SỐ CHƯƠNG MỤC TIÊU ĐƯỢC GIAO. KHÔNG THỪA, KHÔNG THIẾU."

content = content.replace(old_str_1, new_str_1)

old_str_2 = "nằm trong khoảng từ ${typeof targetChapters === 'object' ? targetChapters.minChapters || 10 : targetChapters} ĐẾN ${typeof targetChapters === 'object' ? targetChapters.maxChapters || 30 : targetChapters} chương! Chuyện dở thì ngắn, hay thì bẻ dài ra!"
new_str_2 = "THIẾT LẬP ĐÚNG BẰNG ${typeof targetChapters === 'object' ? targetChapters.minChapters || targetChapters.maxChapters : targetChapters} TẬP! Tuyệt đối tuân thủ con số này!"

content = content.replace(old_str_2, new_str_2)

old_str_3 = "scale tự động từ ${typeof targetChapters === 'object' ? targetChapters.minChapters || 10 : targetChapters} đến ${typeof targetChapters === 'object' ? targetChapters.maxChapters || 30 : targetChapters} tập"
new_str_3 = "BẮT BUỘC ĐÚNG ${typeof targetChapters === 'object' ? targetChapters.minChapters || targetChapters.maxChapters : targetChapters} tập. SÓNG CHẾT CŨNG PHẢI ĐÚNG SỐ TẬP NÀY."

content = content.replace(old_str_3, new_str_3)

# ensure agentGeminiDramaExpand, agentGrokDramaExpand, agentClaudeDramaExpand are also updated if they have different texts
# let's just make sure we capture all of them
def enforce_strict_chapters(text):
    return re.sub(
        r'Tự đánh giá độ phức tạp.*?chuơng!',
        r'MỆNH LỆNH TỐI THƯỢNG: TUYỆT ĐỐI PHẢI SẢN XUẤT CHÍNH XÁC ĐÚNG ${typeof targetChapters === "object" ? targetChapters.minChapters || targetChapters.maxChapters : targetChapters} TẬP! KHÔNG ĐƯỢC LỆCH 1 TẬP NÀO!',
        text
    )

content = enforce_strict_chapters(content)

with open(filepath, 'w') as f:
    f.write(content)
    print("Fixed engine.ts prompts")
