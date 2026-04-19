import json
import random
import string

db_path = './data/mcore_db.json'

with open(db_path, 'r', encoding='utf-8') as f:
    db = json.load(f)

new_id = "rewrite_" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))

new_item = {
  "id": new_id,
  "title": "Khế Ước Đen Tối: Nàng Dâu Hèn Mọn Bóp Nát Đế Chế Của Mẹ Chồng",
  "prompt": "Làm lại truyện này cực kỳ giật gân: Đằng sau danh phận “Con dâu nghìn tỷ” là tròng một cái rọ khổng lồ với mạng lưới âm mưu tàn độc nhằm tước đoạt toàn bộ nhân quyền và tài sản. Nữ chính từ hèn mọn cam chịu vùng lên bóp nát đế chế mẹ chồng.",
  "genres": "Gia Đấu, Vả Mặt, Trả Thù, Hào Môn",
  "status": "draft_outline",
  "chaptersDone": 0,
  "wordCount": 0,
  "targetChapters": 20,
  "maxChapters": 30,
  "outlineEngine": "gemini",
  "writeEngine": "gemini",
  "isSocialShared": False,
  "publishData": {},
  "bible": {
     "super_title": "Khế Ước Đen Tối: Nàng Dâu Hèn Mọn Bóp Nát Đế Chế Của Mẹ Chồng",
     "summary": "Đằng sau danh phận “Con dâu nghìn tỷ” là một cái rọ khổng lồ với mạng lưới âm mưu tàn độc nhằm tước đoạt toàn bộ nhân quyền và sinh mạng. Nữ chính từ một con dâu cam chịu bất hạnh, phát hiện ra sự thật kinh hoàng về mẹ chồng ác độc và quyết định vùng lên. Bằng mưu trí và thủ đoạn cay nghiệt, cô từng bước lật tẩy bộ mặt giả tạo, thâu tóm cổ phần và tự tay bóp nát đế chế hào môn lừng lẫy của mụ ta.",
     "worldSettings": "Thế giới tinh hoa hào môn, nơi cái ác được che đậy dưới những buổi tiệc xa hoa, đồng tiền mua được cả máu và danh dự.",
     "characterArc": "Từ tuyệt vọng, khép nép -> Phẫn nộ tột độ -> Trở thành ác nữ thao túng tâm lý khét lẹt.",
     "plotTwists": "Đứa con bị sẩy năm xưa thực ra là do chính tay mẹ chồng bỏ thuốc. Hợp đồng hôn nhân vốn dĩ là bản án tử hình máu lạnh.",
     "overallSizzle": "Nhiều pha vả mặt trực diện, vạch trần tội ác trước mặt họ hàng, tát lật mặt tiểu tam, ép mẹ chồng quỳ lạy xin tha.",
     "suggestedChapters": 20
  }
}

db['queue'].insert(0, new_item)

with open(db_path, 'w', encoding='utf-8') as f:
    json.dump(db, f, indent=2, ensure_ascii=False)

print("Injected story ID:", new_item['id'])
