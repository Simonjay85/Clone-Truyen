# WRITER CONTRACT — 800 CHAPTERS

Phạm vi chỉ dành cho `novels/ta-chi-muon-an-no/`. Không tự publish.

## Mỗi chương
- Viết tiếng Việt, Markdown UTF-8.
- Mục tiêu 1.800–2.600 từ; bản `final` tối thiểu 1.500 từ trừ interlude được manifest cho phép.
- File `chapters/chapter_NNN.md`, NNN từ 001 đến 800.
- Dòng đầu: `# Chương N: <tên chương>`.
- Không để bullet outline, TODO, placeholder, ghi chú tác giả hoặc meta như “nhân vật chính”, “cốt truyện”, “arc”.
- Mỗi chương phải thay đổi ít nhất một state: mục tiêu, nguy cơ, kiến thức, quan hệ, địa điểm, vật phẩm, tu vi, thương tích, ân/nợ, vị thế phe phái hoặc unresolved hook.

## Cảnh và nhịp
- Mỗi chương thường có 2–4 cảnh thật; ít nhất một cảnh có mục tiêu vật lý cụ thể.
- Không dùng chương chỉ để recap hoặc giải thích lore.
- Hài đến từ tính cách và chênh lệch nhận thức; không dùng meme hiện đại.
- Không dùng một running gag quá 2 lần trong 10 chương.
- Sau mất mát nghiêm túc phải có khoảng thở cảm xúc trước khi quay lại hài.

## Tình cảm
- 1v1 tuyệt đối: Tạ Tiểu Bảo × Lục Thanh Nghi.
- Trước Ch300 chủ yếu là subtext/hành động.
- Ch351–400 mới xác nhận tình cảm sau khi đã đủ tích lũy.
- Sau khi thành đôi vẫn phải có partnership, bất đồng phương pháp, đời sống, vulnerability và mục tiêu riêng của Thanh Nghi.
- Không tạo nữ nhân vật chỉ để mê Tiểu Bảo; không harem bait.

## Chiến đấu và tu luyện
- Ghi rõ địa hình, giới hạn, mục tiêu chiến đấu.
- Vượt cấp phải có leverage đã gieo trước và có cái giá cụ thể.
- Thương tích lớn phải được track và chỉ hồi phục khi có cơ chế/thời gian hợp lý.
- Tuân thứ tự cảnh giới trong `story_bible.md`.
- Đại đột phá cần setup + trigger + aftermath.
- Nhân Gian Lô chỉ luyện/chuyển hóa thứ Tiểu Bảo đã hấp thu/chịu đựng/hiểu; không tạo sức mạnh miễn phí.

## Bí ẩn
- Không reveal sớm hơn mốc trong manifest.
- Foreshadow trước reveal phải có thể hiểu theo ít nhất hai cách.
- Sau payoff, continuity note phải trỏ về seed cũ.
- Mộc Vô Nhai chỉ biết một phần chân tướng.

## Thoại
- Tiểu Bảo: nhanh, thực dụng, thích mặc cả; khi thật sự giận sẽ im và ít đùa.
- Thanh Nghi: ngắn, chính xác, dry humor; không lạm dụng “lạnh lùng nói”.
- Mộc Vô Nhai: bề ngoài lỏng lẻo, bên trong nhìn người rất chuẩn.
- Sở Thiên Tử: trang trọng và sĩ diện lúc đầu, bớt cứng dần khi thân nhóm.
- Không để mọi nhân vật cùng nói kiểu dí dỏm.

## Chống lặp
- Hạn chế các cụm AI quen: “sắc mặt đại biến”, “hít một ngụm khí lạnh”, “không thể tin nổi”, “kinh thiên động địa”, “khóe miệng nhếch lên”.
- Không kết mọi chương bằng một âm mưu mơ hồ.
- Luân phiên cliffhanger: quyết định, reveal, arrival, consequence, lựa chọn cảm xúc, đồng hồ đếm ngược, dị tượng, thất bại, lời hứa.

## Handoff sau mỗi chương
Cập nhật `continuity/ledger.json` với: chapter, POV, địa điểm đầu/cuối, timeline, tu vi, thương tích, inventory, ân/nợ, relationship beat, knowledge gained, hooks opened/paid, foreshadow seed, next objective.

## Batch protocol
Batch chuẩn = 5 chương.
1. Đọc Story Bible, manifest của batch, 2 chương trước, 10 ledger entry gần nhất và hook liên quan.
2. Viết 5 chương.
3. Chạy `python3 tools/qa_novel.py --range A-B`.
4. Sửa hard fail.
5. Cập nhật ledger + batch report.
6. Goal Runner checkpoint với evidence.

Không chapter nào được đánh dấu `final` nếu còn placeholder, thiếu số/tên, sai continuity, nhảy cảnh giới vô cớ, nhân vật biết điều chưa được học, romance lệch 1v1 hoặc lặp sự kiện chính của chương trước.