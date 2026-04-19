const fs = require('fs');
const dbPath = './data/mcore_db.json';

const dbRaw = fs.readFileSync(dbPath, 'utf8');
const db = JSON.parse(dbRaw);

const newId = Math.random().toString(36).substring(2, 10);

const newItem = {
  id: "rewrite_" + newId,
  title: "Khế Ước Đen Tối: Nàng Dâu Hèn Mọn Bóp Nát Đế Chế Của Mẹ Chồng",
  prompt: "Làm lại truyện này cực kỳ giật gân: Đằng sau danh phận “Con dâu nghìn tỷ” là tròng một cái rọ khổng lồ với mạng lưới âm mưu tàn độc nhằm tước đoạt toàn bộ nhân quyền và tài sản. Nữ chính từ hèn mọn cam chịu vùng lên bóp nát đế chế mẹ chồng.",
  genres: "Gia Đấu, Vả Mặt, Trả Thù, Hào Môn",
  status: "draft_outline",
  chaptersDone: 0,
  wordCount: 0,
  targetChapters: 20,
  maxChapters: 30,
  outlineEngine: "gemini",
  writeEngine: "gemini",
  isSocialShared: false,
  publishData: {},
  bible: {
     super_title: "Khế Ước Đen Tối: Nàng Dâu Hèn Mọn Bóp Nát Đế Chế Của Mẹ Chồng",
     summary: "Đằng sau danh phận “Con dâu nghìn tỷ” là một cái rọ khổng lồ với mạng lưới âm mưu tàn độc nhằm tước đoạt toàn bộ nhân quyền và sinh mạng. Nữ chính từ một con dâu cam chịu bất hạnh, phát hiện ra sự thật kinh hoàng về mẹ chồng ác độc và quyết định vùng lên. Bằng mưu trí và thủ đoạn cay nghiệt, cô từng bước lật tẩy bộ mặt giả tạo, thâu tóm cổ phần và tự tay bóp nát đế chế hào môn lừng lẫy của mụ ta.",
     worldSettings: "Thế giới tinh hoa hào môn, nơi cái ác được che đậy dưới những buổi tiệc xa hoa, đồng tiền mua được cả máu và danh dự.",
     characterArc: "Từ tuyệt vọng, khép nép -> Phẫn nộ tột độ -> Trở thành ác nữ thao túng tâm lý khét lẹt.",
     plotTwists: "Đứa con bị sẩy năm xưa thực ra là do chính tay mẹ chồng bỏ thuốc. Hợp đồng hôn nhân vốn dĩ là bản án tử hình máu lạnh.",
     overallSizzle: "Nhiều pha vả mặt trực diện, vạch trần tội ác trước mặt họ hàng, tát lật mặt tiểu tam, ép mẹ chồng quỳ lạy xin tha.",
     suggestedChapters: 20
  }
};

db.queue.push(newItem);
fs.writeFileSync(dbPath, JSON.stringify(db, null, 2));
console.log("Injected story ID:", newItem.id);
