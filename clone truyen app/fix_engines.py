import re

with open("src/lib/engine.ts", "r") as f:
    text = f.read()

# Replace signatures
text = re.sub(r'targetChapters: number', 'targetChapters: { minChapters?: number, maxChapters?: number } | number', text)

# Update prompts
old_prompt = r'Bạn là Tổng Đạo Diễn.*?(?=Bạn PHẢI MỞ RỘNG)'
new_prompt = r'''Bạn là Tổng Đạo Diễn. Nhiệm vụ của bạn là nhận Story Bible và TỰ ĐỘNG CHIA NHỎ thành Dàn ý (Timeline) chi tiết.
CHÚ Ý CỰC KỲ QUAN TRỌNG VỀ ĐỘ DÀI: Bạn phải tự đánh giá độ phức tạp của cốt truyện để quyết định số chương phù hợp, nằm trong khoảng từ ${typeof targetChapters === 'object' ? targetChapters.minChapters || 10 : targetChapters} ĐẾN ${typeof targetChapters === 'object' ? targetChapters.maxChapters || 30 : targetChapters} chương!
KÍCH HOẠT VẢ MẶT (FACE-SLAPPING OVERRIDE): Cực kỳ chú ý: Nếu truyện mang hơi hướm 'Chủ tịch giả danh', 'Giấu tài', 'Bị khinh thường', BẠN PHẢI bôi ra nhiều vòng lặp Vả mặt. Hãy để thế lực phản diện khinh bỉ, sỉ nhục nhân vật chính nhiều lần ở các sự kiện khác nhau, sau đó nhân vật chính lật bài ngửa vả sưng mặt tụi nó. Càng vả nhiều vòng càng tốt để tạo kịch tính!
'''

text = re.sub(r'Bạn là Tổng Đạo Diễn.*?Mỗi object CÓ ĐÚNG các properties sau:', new_prompt + '\nMỗi object CÓ ĐÚNG các properties sau:', text, flags=re.DOTALL)

with open("src/lib/engine.ts", "w") as f:
    f.write(text)

