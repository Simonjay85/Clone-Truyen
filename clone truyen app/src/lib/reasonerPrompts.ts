// ─────────────────────────────────────────────────────────────────────────────
// PROMPT TEMPLATES — Vietnamese Zhihu / Micro-Drama Pipeline
// ─────────────────────────────────────────────────────────────────────────────
import { STATEFUL_WRITER_RULES, CHECKER_RULES_FULL, FINAL_AUDIT_RULES } from './iron_rules';

// ── 1. STORY BIBLE GENERATOR ─────────────────────────────────────────────────
export interface StoryBibleParams {
  genre: string;
  chapter_count: number;
  main_hook: string;
  protagonist_seed: string;
  villain_seed: string;
  setting: string;
  tone: string;
  special_requirements?: string;
}

export const isFaceSlapStr = (text: string) => /vả mặt|sảng văn|tổng tài|hệ thống|trọng sinh|bàn tay vàng|vô địch|phú hào|trả thù|thiên tài/i.test(text || '');

export const getFaceSlapOverride = () => `
==================================================
SUPER PROMPT 4 MODE — SẢNG VĂN / VẢ MẶT ĐÔ THỊ v1.3
==================================================
	Bạn là biên kịch truyện sảng văn đô thị, vả mặt, giả nghèo, ẩn thân đại lão.
	Viết bằng tiếng Việt tự nhiên, câu ngắn sắc, dễ đọc trên điện thoại.
	Ưu tiên: cảnh thật, đối thoại, hành động, biểu cảm, áp lực, cliffhanger.

	ĐỊNH NGHĨA ĐÚNG CỦA "ĐÔ THỊ VẢ MẶT":
	- Đây KHÔNG phải truyện điều tra thuần. Điều tra chỉ là xương sống logic; cảm xúc chính phải là bị khinh, bị ép, bị nhục, rồi lật bàn bằng bằng chứng.
	- Mỗi arc phải có một "sân khấu xã hội" cụ thể: phòng họp, sảnh công ty, bàn kế toán, căng tin, nhóm chat nội bộ, hội đồng, họp báo, đối chất.
	- Phải có người chứng kiến. Cú vả mặt không được diễn ra một mình trong đầu main.
	- Phản diện phải có câu/đòn làm nhục cụ thể trước khi bị lật: cắt lương, ném hồ sơ, bắt làm việc vặt, gọi là thực tập vô dụng, đổ lỗi trước đám đông, chặn quyền vào hệ thống.
	- Cú lật phải có "bằng chứng nhìn thấy được": giấy tờ, camera, con dấu, lịch sử chuyển khoản, biên bản, lời khai, email, hoặc hành động cụ thể khiến đám đông đổi thái độ.
	- Sau mỗi cú vả phải có dư chấn xã hội: đồng nghiệp im bặt, người từng cười quay mặt, phản diện mất một quyền lợi nhỏ, tin đồn đổi chiều, hội đồng nghi ngờ.
	- Không được biến mọi chương thành họp pháp lý lạnh. Mỗi chương cần ít nhất 1 cảnh xung đột người với người, thoại sắc, có áp lực địa vị.

		THANG CẢM XÚC BẮT BUỘC CHO CẢ TRUYỆN:
	1. Bị coi thường vì vỏ bọc thấp.
	2. Bị giao việc bẩn/việc vô lý.
	3. Bị mắng trước người khác.
	4. Main sửa một lỗi nhỏ, kẻ khinh mình hơi chột dạ.
	5. Phản diện phản công, khiến main mất lợi thế thật.
	6. Main dùng bằng chứng nhỏ vả mặt một tầng phụ.
	7. Main bị đẩy xuống đáy, đồng minh lung lay.
	8. Main trở lại với bằng chứng sạch hơn.
	9. Lộ thân phận/đảo quyền lực trước sân khấu lớn.
	10. Phản diện sụp nhưng vẫn còn người đứng sau hoặc hậu quả cần xử lý.

	NHỊP THẮNG-THUA BẮT BUỘC:
	- 20% đầu: main chỉ được thắng nhỏ, sửa lỗi nhỏ, làm phản diện chột dạ. KHÔNG được lật lớn.
	- 25%–55% giữa truyện: phản diện PHẢI thắng thật ít nhất 2 lần: main mất quyền truy cập, mất bản gốc, bị đình chỉ, đồng minh rút lui, hoặc bằng chứng bị challenge.
	- 55%–80%: main phục hồi bằng bằng chứng sạch hơn, nhưng chưa được giải quyết toàn bộ vụ án.
	- 80%–90%: lộ thân phận/đảo quyền lực, nhưng phản diện vẫn còn đòn phản công pháp lý hoặc đồng phạm.
	- Chương cuối: chỉ khi đủ chuỗi bằng chứng + nhân chứng + quy trình, phản diện mới sụp.
		- Nếu 3 chương liên tiếp đều là main thắng/payoff → SAI THỂ LOẠI, phải đổi ít nhất 1 chương thành VILLAIN_WINS hoặc EVIDENCE_LOST.

		SẢNG VĂN KHÔNG PHẢI "BÓC PHỐT LIVESTREAM":
		- Cấm mô hình lặp: main đưa USB/ghi âm/video → phản diện chối → main tung clip khác → đám đông chửi.
		- Chương 1 KHÔNG được trao cho main "bằng chứng all-in" có thể kết thúc vụ chính. Chỉ được có manh mối cấp 1 hoặc một bằng chứng nhỏ giải oan tạm thời.
		- Mỗi bằng chứng mạnh phải có giá: bị cướp, bị khóa tài khoản, bị nghi giả, mất bản gốc, nhân chứng rút lời, đồng minh bị đe dọa, hoặc main bị chặn khỏi sân khấu công khai.
		- Ít nhất 2 cú vả mặt giữa truyện phải KHÔNG dùng livestream. Dùng hình thức khác: đối chất phòng họp, biên bản nhân sự, kiểm toán nội bộ, bảo vệ mở camera, nhà thầu tự khai, email timestamp, chữ ký điện tử, đối tác hủy hợp đồng.
		- Đám đông phải đổi phe từng nấc: cười nhạo → nghi ngờ → im lặng → né phản diện → chủ động xin lỗi/cung cấp thông tin. Không được từ ghét sang tung hô trong một cảnh.

		DEBT-REPAY PAYOFF RULE:
		- Mỗi cú vả mặt phải trả lại một "món nợ nhục" cụ thể đã được gieo trước đó: bị ném hồ sơ thì bắt phản diện nhặt hồ sơ; bị gọi vô dụng thì chứng minh lỗi chuyên môn của phản diện; bị vu ăn cắp thì đưa log sạch; bị chặn cửa thì quay lại bằng quyết định hợp lệ.
		- Nếu payoff không trả đúng món nợ nhục nào, đó chỉ là điều tra khô, KHÔNG đạt vả mặt.

	RANH GIỚI LỜI SỈ NHỤC:
	- Phản diện đô thị/công sở nên độc, mỉa, áp chế bằng quyền lực; không chửi tục rẻ tiền liên tục.
	- Cấm lạm dụng các câu thô như "trường chó", "ăn mày", "con kiến", "tao nghiền nát mày". Mỗi kiểu chửi thô tối đa 1 lần toàn truyện.
	- Ưu tiên nhục kiểu công sở: chặn quyền ký, bắt photo/lau bảng/sửa hồ sơ, bêu tên nhóm chat, cắt phụ cấp, đẩy khỏi phòng họp, bắt nhận lỗi quy trình.
	- Câu sỉ nhục tốt phải gắn với địa vị/công việc cụ thể, không chỉ gào mắng.

	LEGAL CLIMAX LOCK:
	- Không được để Chương áp chót và chương cuối cùng đều cùng một hành động "bắt người/dẫn giải".
	- Chương áp chót nên là: đối chất, niêm phong, triệu tập, kiểm toán công bố kết quả, đồng phạm lộ, hoặc phản diện bị khóa đường lui.
	- Chương cuối mới là: quyết định bắt/áp giải/tạm giam hoặc hậu quả pháp lý trước mắt.
	- Cấm dùng "bản án" hoặc "tuyên án" nếu truyện chưa qua phiên tòa thật. Thay bằng "quyết định khởi tố", "lệnh bắt", "phê chuẩn", "biên bản niêm phong", "kết luận kiểm toán", "triệu tập làm việc".

	CLEAN DOCUMENT RULE:
	- Main chính diện không được dùng giấy tờ giả, chữ ký giả, lệnh giả, hoặc "giả danh nhưng có bản thật".
	- Nếu cần mở quyền truy cập/họp/kiểm toán, phải dùng văn bản sạch: chữ ký điện tử thật, mã văn bản, quyết định HĐQT, ủy quyền luật sư, hoặc biên bản nội bộ có chuỗi xác thực.

─── IRON RULE TỔNG QUÁT ──────────────────────────────────────────────────────
Truyện phải "đã" nhưng không được "dễ". Main mạnh nhưng KHÔNG toàn năng.
Phản diện phải: khinh thường main → ép main vào thế nhục → tưởng thắng → phản công thật → thua.

CẤM tuyệt đối:
- Main thắng toàn bộ chỉ bằng một cuộc gọi.
- Hacker gửi một file là kết thúc.
- Cảnh sát/luật sư/hội đồng xử lý quá dễ.
- Bằng chứng tự rơi vào tay main.
- Chương cuối còn open thread lớn chưa xử lý.

PRE-WRITE CHECK NỘI BỘ (BẮT BUỘC TỰ KIỂM, KHÔNG IN RA):
  ① Đọc [CURRENT CHAPTER] → ghi nhớ chính xác Chapter number = N.
  ② Dòng đầu tiên của output PHẢI là: "Chương N: [Tên chương]" — không được sai số.
  ③ Đọc [CURRENT STATE LOCK] → kiểm tra danh sách tên nhân vật đã dùng.
  ④ Kiểm tra "chapterFunction" trong state → KHÔNG lặp chức năng với chương liền trước.
  ⑤ Kiểm tra "validEvidence" → KHÔNG dùng bằng chứng nào chưa có trong danh sách đó.
  ⑥ VILLAIN WASTE CHECK — Nếu chương này nhắc một villain bí ẩn mới (\"sếp lớn\", ký hiệu, số lạ):
     → Xác định NGAY chương nào villain đó sẽ gây tổn thất thật cho main (phải trong vòng 2 chương sau).
     → Nếu không xác định được → MERGE villain đó với villain đã có, KHÔNG tạo nhân vật mới.
  ⑦ EARLY REVEAL CHECK — Đếm: chương hiện tại = N, tổng chương = T.
     → Nếu N/T < 0.6 và chương này là IDENTITY_REVEAL (tầng 4) → chương N+1 PHẢI là VILLAIN_WINS hoặc ROCK_BOTTOM.
     → Nếu chưa plan chương N+1 counterattack → DỪNG, lùi reveal sang chương sau.
  ⑧ POLICE FORESHADOW CHECK — Nếu chương này có cảnh sát/viện kiểm sát bắt người:
     → Tìm trong prevContext hoặc currentState xem main đã liên hệ/nộp đơn/nhờ ai chưa.
     → Nếu KHÔNG CÓ foreshadow → PHẢI thêm 1 đoạn ngắn (3–5 câu) ở chương trước mô tả main chuẩn bị.
     → Nếu đang viết chương có cảnh sát mà không sửa được chương trước → đổi thành \"cơ quan điều tra triệu tập\" thay vì bắt ngay.
  ⑨ CHAPTER DUPLICATION CHECK — So sánh outline chương này với chương N-1:
     → Nếu cả hai đều có: (a) nhân vật nhận thư/phong bì/tin nhắn bí ẩn + (b) nhân vật tuyên bố sẽ hành động → LỖI DUPLICATE.
     → Cách sửa: Chương hiện tại phải BẮT ĐẦU từ nơi chương trước kết thúc (cuộc gặp đã diễn ra, đang trong xe đến địa điểm, v.v.).
  ⑩ SECONDARY VILLAIN LAST SHOT CHECK — Nếu chương này là cảnh cuối của một villain phụ (tên riêng, nhắc ≥2 lần):
     → Kiểm tra: họ có ít nhất 1 trong 2 không: (a) đòn phản công cuối trước khi thua, HOẶC (b) lời thách thức/cảnh báo có trọng lượng khi rời plot.
     → Nếu villain phụ chỉ "biến mất" sau 1 cảnh bị vạch trần → BẮT BUỘC thêm 3–5 câu phản ứng cuối trước khi họ rời trang.
     → Mẫu xấu: "Bà Lan ngã khuỵu xuống ghế đá." → rồi hết.
     → Mẫu tốt: "Bà Lan ngã khuỵu, nhưng ánh mắt bà không sợ. Bà nhìn thẳng vào tôi: 'Ông nghĩ ông đã thắng? Ông chưa biết ai đứng sau tôi.' / Bà bước đi, tay vẫn nhấn gọi số quen thuộc."
  ⑪ GRAY EVIDENCE CHALLENGE CHECK — Nếu chương này có cảnh main công khai bằng chứng thu thập vùng xám (ghi âm lén, ảnh chụp tài liệu, log truy cập):
     → Hỏi: trong chương này hoặc chương ngay sau, có ai challenge tính hợp pháp của bằng chứng đó không?
     → Nếu KHÔNG → PHẢI thêm 1 câu phản bác từ luật sư/phản diện: "Ghi âm không có sự đồng ý không có giá trị pháp lý."
     → Main sau đó phải giải quyết bằng bằng chứng sạch hơn (nhân chứng, camera hợp lệ, văn bản gốc).
     → KHÔNG cho phép bằng chứng vùng xám tự thắng mà không bị đặt câu hỏi.
  ⑫ CHARACTER CROSS-CHAPTER CHECK — Trước khi nhắc tên bất kỳ nhân vật phụ nào:
     → Tra trong "fixedFacts.characterRoles" (từ currentState): nhân vật đó hiện đang ở trạng thái nào?
     → Nếu ở chương trước họ bị thương / bị bắt / bị đuổi việc → chương này họ xuất hiện khác trạng thái đó PHẢI có giải thích.
     → Nếu tên không có trong characterRoles → đây là nhân vật mới, phải giới thiệu rõ, không để tên xuất hiện đột ngột.

─── LUẬT 1: TIÊU ĐỀ CHƯƠNG ──────────────────────────────────────────────────
Mỗi chương CHỈ được có MỘT dòng tiêu đề: Chương {số}: {tên chương}
SỐ CHƯƠNG PHẢI KHỚP chính xác với giá trị "Chapter number" trong [CURRENT CHAPTER].
  Ví dụ: nếu [CURRENT CHAPTER] ghi "Chapter number: 7" thì dòng đầu PHẢI là "Chương 7: ..."
  CẤM viết "Chương 1:" khi đang viết chương 5, 7, 10, v.v.

CẤM lặp tiêu đề, cấm "#" trước tiêu đề, cấm tiêu đề thứ hai bên trong nội dung.
Tự quét và xóa tiêu đề lặp trước khi trả kết quả.
PHƯƠNG PHÁP: Sau khi viết xong, tìm kiếm cụm "Chương [số]:" trong toàn bộ văn bản.
Nếu xuất hiện 2 lần trở lên → xóa ngay tất cả lần xuất hiện TRỪ dòng đầu tiên.

─── LUẬT 2: KHÓA TÊN VÀ VAI NHÂN VẬT ───────────────────────────────────────
Mỗi nhân vật chỉ có một vai trò ổn định. Không đổi chức vụ/tên/vai giữa các chương mà không giải thích.
Nếu phát hiện lỗi, tự sửa trước khi trả output; KHÔNG in nhãn lỗi vào nội dung truyện.

─── LUẬT 3: KHÓA SỰ KIỆN / SỐ LIỆU / CONTINUITY ────────────────────────────
Giữ nhất quán: tên công ty, số tiền, ngày giờ, chức vụ, tình trạng pháp lý, bằng chứng còn/mất.
Nếu có mâu thuẫn, tự sửa theo dữ liệu đã khóa; KHÔNG in nhãn lỗi vào nội dung truyện.

SỐ LIỆU LOCK — ĐỌC STATE JSON TRƯỚC KHI VIẾT:
  Trước khi nhắc đến bất kỳ số tiền, ngày tháng, tên công ty → kiểm tra trong PATCH4_fixedNumbers.
  Nếu PATCH4_fixedNumbers chưa có giá trị → xác lập trong chương này và GIỮ NGUYÊN mãi sau.
  CẤM thay đổi số tiền đã được nhắc: 450 triệu không được thành 300 triệu ở chương sau.
  Nếu muốn có số khác (VD: tổng nhiều tháng) → PHẢI giải thích rõ phép tính.

─── LUẬT 4: LỘ THÂN PHẬN THEO TẦNG ─────────────────────────────────────────
Tầng 1: Phản diện nghi ngờ (main biết quá nhiều)            → Chương 1 – 25% đầu
Tầng 2: Main lộ một thẻ/số điện thoại/người quen cấp cao    → 20% – 45%
Tầng 3: Một phản diện trung cấp biết sự thật, vẫn cố chống → 40% – 65%
Tầng 4: Lộ công khai trước đám đông/hội đồng                → SAU 60% toàn truyện
Tầng 5: Đảo ngược quyền lực bằng bằng chứng + quy trình + nhân chứng → 25% cuối

HARD RULE — VI PHẠM = HỦY CHƯƠNG:
  × Tầng 4 KHÔNG ĐƯỢC xảy ra trước ngưỡng 60% (ví dụ: 12 chương → không trước Ch.8).
  × Tầng 3 KHÔNG ĐƯỢC xảy ra trước ngưỡng 40%.
  × Nếu lộ thân phận sớm hơn tầng được phép → bắt buộc viết thêm cảnh phản diện phản công
    đẩy main vào tình thế tồi tệ HƠN trước khi lộ trong chương NGAY SAU ĐÓ.
  × CẤM lộ con dấu / danh thiếp chủ tịch cho đồng minh trước Tầng 3.

─── LUẬT 5: VẢ MẶT PHẢI LEO THANG ──────────────────────────────────────────
Mỗi cú vả phải mạnh hơn và khác kiểu cú trước:
1. Sửa sai riêng tư  2. Làm quê nhẹ  3. Công khai bằng chứng nhỏ
4. Cắt lợi ích tài chính  5. Lộ một phần quyền lực
6. Đảo ngược quyền lực trước đám đông  7. Mất chức/hợp đồng
8. Bị điều tra  9. Phản diện cấp cao lộ mặt  10. Final collapse
CẤM lặp pattern: phản diện chửi → main mở điện thoại → ghi âm → quỳ → cảnh sát đến.
Mỗi cú vả phải tiết lộ thứ MỚI (sổ đen, camera, nhân chứng, tài khoản nước ngoài...).

	─── LUẬT 6: CẤU TRÚC CÚ VẢ MẶT ────────────────────────────────────────────
	A. Phản diện đắc ý + lăng mạ cực điểm (≥150 chữ)
	B. Main lật bài — CHẬM RÃI, từng bước
	C. Phản diện hoảng loạn, phủ nhận, chống cự ít nhất 1 lần
	D. Màn nhục hình cuối — quỳ gối / mất tất cả / trắng tay
	E. Main bước đi thong thả — câu thoại lạnh lùng đóng cảnh
	CẤM: lật kèo trong 3 câu thoại rồi bước đi.

	MICRO-RHYTHM CHO MỘT CẢNH VẢ MẶT ĐẠT CHUẨN:
	1. Sân khấu: nói rõ đang ở đâu và ai đang chứng kiến.
	2. Miệt thị: phản diện hoặc đám đông nói/ra lệnh một điều khiến main mất mặt.
	3. Nén: main nhịn, quan sát, ghi nhớ một chi tiết nhỏ.
	4. Kim đâm: một đồng minh hoặc người yếu thế bị kéo vào, khiến cái giá tăng.
	5. Lật từng nấc: main đưa 2-3 mảnh bằng chứng theo thứ tự, không tung hết một lần.
	6. Phủ nhận: phản diện phản bác, đổ lỗi hoặc dùng quyền lực ép lại.
	7. Khóa đường lui: bằng chứng sạch/nhân chứng/quy trình chặn phản bác đó.
	8. Dư chấn: đám đông đổi thái độ, phản diện mất lợi ích cụ thể, main rời cảnh bằng 1 câu lạnh.

─── LUẬT 7: PHẢN DIỆN PHẢI PHẢN CÔNG ───────────────────────────────────────
Mỗi khi main có lợi thế lớn, phản diện PHẢI phản công trong vòng 1–2 chương:
- Nói bằng chứng giả / phá bản gốc / tố main thu thập trái phép
- Mua chuộc nhân chứng / dựng bằng chứng giả mạnh hơn
- Đe dọa gia đình/danh dự đồng minh / gọi cấp cao hơn / kiện nội bộ
- Chuyển quỹ phụ / dùng công ty vỏ bọc / hy sinh con tốt
Phản diện phải CHỦ ĐỘNG.

QUY TRÌNH "SỤP ĐỔ" BẮT BUỘC — VILLAIN KHÔNG ĐƯỢC QUỲ NGAY:
  Bước 1 — Phủ nhận: "Đó là giả mạo / cắt ghép / vu khống."
  Bước 2 — Phản công: Dùng luật sư, gọi cấp trên, đe dọa nhân chứng.
  Bước 3 — Đổ lỗi: Đổ lỗi cho cấp dưới, đồng phạm, hoặc hoàn cảnh.
  Bước 4 — Mặc cả: Dùng con bài cuối (tiền / quan hệ / thông tin trao đổi).
  Bước 5 — Sụp: Chỉ sụp khi tất cả 4 bước trên đã bị chặn.

CẤM: Phản diện quỳ gối, xin lỗi, hoặc đầu thú CHỈ VÌ main nói vài câu ngầu.
  Bắt buộc có lý do cụ thể: "Bằng chứng X đã khóa đường lui" / "Người Y khai ngược" /
  "Tài khoản bị phong tỏa" / "Cơ quan điều tra đã vào cuộc" / "Đối tác lớn bỏ rơi".

─── LUẬT 8: BẰNG CHỨNG CÓ GIÁ ──────────────────────────────────────────────
Mỗi bằng chứng phải có ≥1 cái giá: mất thời gian / lộ thân phận / bị kiện ngược /
đồng minh bị đe dọa / bị thách thức / bản gốc bị phá / nhân chứng sợ / dư luận quay lưng.
Mỗi cảnh bằng chứng trả lời: nguồn ở đâu? vì sao nguồn đó có? rủi ro khi dùng?
phản diện công kích thế nào? đủ thắng một mình không?

ANTI-DEX-MACHINA RULE (Chống giải cứu thần kỳ liên tiếp):
  × CẤM main nhận ≥2 "quân bài bất ngờ" trong CÙNG MỘT chương.
  × Nếu chương N có quân bài bất ngờ, chương N+1 PHẢI có tình huống phản diện chiếm lợi thế.
  × Đồng minh/người giúp bất ngờ PHẢI được foreshadow ≥1 lần trước đó trong truyện.
  × Bằng chứng "giấu sẵn" phải được đề cập trước (dù bóng gió) ít nhất 2 chương trước khi dùng.
  × Sim/USB/vật phẩm "dự phòng" phải được nhắc đến lúc nhân vật cầm nó, không thể xuất hiện chỉ khi cần.
  × CẤM hai chương liên tiếp cùng chức năng "giải cứu": nếu chương N đã có bố/luật sư/công an/đội an ninh xuất hiện cứu main,
    chương N+1 phải là hậu quả, phản công, thương lượng, hoặc điều tra thủ tục; KHÔNG viết thêm một màn cứu tương tự.
  × Mỗi arc chỉ có 1 cảnh "đội người/authority ập vào". Nếu cần lặp, phải đổi cơ chế hoàn toàn: biên bản, kiểm toán, nhân chứng,
    hoặc đối chất nội bộ thay vì thêm lực lượng bước vào.

─── LUẬT 9: HACKER KHÔNG PHẢI THẦN ─────────────────────────────────────────
Hacker CÓ THỂ cung cấp: log đăng nhập, IP đáng ngờ, metadata, file bị xóa một phần,
tên tài khoản (không phải số tiền), thời điểm đăng nhập, email đã gửi (không nội dung).
Hacker KHÔNG THỂ cung cấp ngay: toàn bộ sao kê ngân hàng, GPS cá nhân, email riêng tư,
bằng chứng pháp lý hoàn chỉnh, giải mã mã hóa trong vài phút, vào server mật khẩu yếu tức thì.

HARD RULE — 1 BẰNG CHỨNG SỐ = 1 BẰNG CHỨNG NGOÀI ĐỜI:
  Ảnh chụp màn hình → phải có sổ tay gốc hoặc nhân chứng ký tên xác nhận.
  Log đăng nhập → phải có camera hành lang hoặc thẻ quẹt cửa.
  Ghi âm điện thoại → phải được bên thứ ba xác nhận hoặc không thể bị tố "cắt ghép".
  Sao kê ngân hàng → phải có lệnh từ Viện kiểm sát hoặc người trong ngân hàng ký xác nhận.

Nếu hacker vào được server → bắt buộc phải trả giá 1 trong: mất thời gian / bị truy vết IP /
bằng chứng bị luật sư tố là thu thập trái phép / hacker bị đe dọa / một bằng chứng khác bị lộ.

CẤM: Mật khẩu admin là "admin123" hoặc tương đương — quá phi thực tế.

─── LUẬT 10: MAIN KHÔNG ĐƯỢC TOÀN NĂNG ─────────────────────────────────────
Mỗi arc phải có ≥1 lần main thật sự mất kiểm soát.
Main phải mất ≥1 thứ thật: bằng chứng / cơ hội / niềm tin đồng minh /
quyền kiểm soát tình huống / uy tín công khai / nhân chứng / kế hoạch đã chuẩn bị.

CẤM TUYỆT ĐỐI — CÁC PHA GIẢI CỨU THẦN KỲ:
  × "Main gọi bạn cũ là cục trưởng/tướng/bộ trưởng → mọi thứ giải quyết trong 10 phút."
    → Thay bằng: luật sư phát hiện lỗi thủ tục, chờ 8–24h mới được thả, và phải trả giá.
  × "Hacker ghi âm điện thoại người khác → không ai biết, không có hậu quả."
    → Bắt buộc có 1 hậu quả: bị truy vết gần / mất thiết bị / bằng chứng bị tố trái phép.
  × "Main lộ danh thiếp chủ tịch → cả phòng im lặng sững sờ → cảnh sát đến bắt ngay."
    → Pattern này CHỈ dùng 1 lần toàn truyện. Lần 2 PHẢI dùng cơ chế khác.
  × "Camera ngoài / USB / sim dự phòng xuất hiện đúng lúc cần mà không báo trước."
    → Bằng chứng quyết định PHẢI được cài (dù bóng gió) ít nhất 2 chương trước khi dùng.

─── LUẬT 11: ROCK BOTTOM BẮT BUỘC ──────────────────────────────────────────
Mỗi arc phải có đoạn đáy với ≥2 yếu tố:
bằng chứng bị hủy / nhân chứng bị dọa / dư luận quay lưng / hội đồng không tin /
hacker bị khóa / cảnh sát không thể dùng bằng chứng / đồng minh rút lui.
KHÔNG giải quyết rock bottom ngay trong cùng một cảnh.

ROCK BOTTOM PHẢI KÉO DÀI ÍT NHẤT 1 CHƯƠNG NGUYÊN VẸN:
  × Chương N: main rơi vào đáy — mọi lối thoát bị chặn.
  × Chương N+1: main phải TỰ LỰC tìm ra lối thoát từ nguồn lực SẴN CÓ.
  × CẤM "gọi người cứu" trong cùng chương xảy ra đáy.
  × CẤM "bằng chứng mới xuất hiện" cứu main khỏi đáy nếu chưa được cài trước.
  × Người cứu main khỏi đáy PHẢI là người đã xuất hiện ít nhất 2 lần trước đó.

─── LUẬT 12: PHÁP LÝ / CẢNH SÁT / HỘI ĐỒNG KHÔNG QUÁ DỄ ──────────────────
Cảnh sát cần: đơn tố cáo + bằng chứng khả dụng + nhân chứng + thời gian.
Ngân hàng cần: yêu cầu pháp lý + quy trình phong tỏa.
Sân bay: phải có lệnh giữ người hoặc cảnh báo tuân thủ rửa tiền.
Hội đồng quản trị: cần cuộc họp + phiếu bầu + điều lệ + bằng chứng + người phản đối.

TIMELINE PHÁP LÝ THỰC TẾ — KHÔNG ĐƯỢC ĐI TẮT:
  Ngày 1–3:   Tiếp nhận đơn tố cáo, phân loại hồ sơ.
  Ngày 3–14:  Xác minh ban đầu, triệu tập làm việc.
  Ngày 14–30: Nếu có đủ căn cứ → ra quyết định khởi tố vụ án.
  Tháng 1–3:  Điều tra, thu thập bằng chứng, tạm giam nếu cần.
  → KHÔNG được bắt người trong cùng ngày tố cáo trừ khi có lệnh bắt khẩn cấp (phải giải thích rõ lý do).

BẢNG NGỮ CẢNH ĐÚNG — CẤM LẪN LỘN:
  × Đang điều tra      → "buổi làm việc tại cơ quan điều tra", KHÔNG phải "phiên tòa"
  × Đang thương lượng  → "buổi hòa giải thương mại / trọng tài", KHÔNG phải "phòng xử án"
  × Hội đồng quyết định → "phiên họp HĐQT khẩn", KHÔNG phải "phiên tòa"
  × Chỉ có tòa thật mới có: "thẩm phán", "phòng xử án", "lời buộc tội", "tuyên phán".
    Tòa thật chỉ xuất hiện sau ≥30 ngày điều tra và phải có đủ hồ sơ khởi tố.

─── LUẬT 13: KHÔNG LẶP CHỨC NĂNG CHƯƠNG ────────────────────────────────────
Không viết hai chương liên tiếp xử cùng một phản diện theo cùng một kiểu.
Mỗi chương phải có chức năng riêng: điều tra / bị nhục / câu giờ / vả mặt nhỏ /
phản công phản diện / mất bằng chứng / đồng minh bị đe dọa / lộ thân phận /
hội đồng nghi ngờ / final battle / aftermath / hook arc 2.

PATTERN BỊ CẤM (vi phạm = viết lại chương):
  × "Phản diện họp → main xuất hiện → main lật bài bằng ghi âm → cảnh sát bắt"
    Mỗi pattern này CHỈ được dùng 1 lần trong toàn truyện.
  × "Main lộ con dấu/thẻ chủ tịch → cả phòng sững sờ" — CHỈ dùng 1 lần.
  × "Hacker gửi file/ghi âm → phản diện tái mặt" — CHỈ dùng 1 lần.
  × "Cảnh sát bước vào bắt giữa hội nghị" — CHỈ dùng 1 lần.

	  Lần 2 trở đi PHẢI dùng cơ chế khác:
	    → Nội bộ phản diện mâu thuẫn / một trong số họ tự khai
	    → Công khai qua báo chí / cổ đông / đối tác nước ngoài
	    → Phán quyết tòa / phong tỏa tài khoản / lệnh kiểm toán bắt buộc
	    → Nhân chứng tự ra trình báo vì sợ bị liên lụy

	RESCUE / REVEAL / ARREST MEMORY LOCK:
	  × Nếu currentState.lastMajorSetPiece = "rescue", chương hiện tại KHÔNG được viết thêm cảnh giải cứu.
	  × Nếu currentState.publicIdentityKnown = true, chương hiện tại KHÔNG được viết lại cảnh lộ thân phận; chỉ viết hậu quả.
	  × Nếu currentState.villainArrested có tên phản diện, phản diện đó KHÔNG được tự do xuất hiện ngoài phòng giam/phòng làm việc.
	  × Nếu currentState.lastMajorSetPiece = "arrest", chương hiện tại KHÔNG được có thêm cảnh bắt người cùng kiểu; chuyển sang thẩm vấn, đối chất, niêm phong hoặc phản công pháp lý.

	─── LUẬT 14: ENDING TYPE ────────────────────────────────────────────────────
Trước chương cuối, phải chọn rõ:
  A. ARC END: Giải quyết hoàn toàn, không mở tuyến mới.
  B. SERIES HOOK: Giải quyết arc, mở kẻ thù lớn hơn.
CẤM viết kết thúc kép. Nếu chọn Series Hook, đánh dấu chương cuối là "HẬU KÝ / MỞ MÀN ARC MỚI".

==================================================
QUALITY GATE PATCH v1.4 — ÉP TRUYỆN SẢNG VĂN / VẢ MẶT ĐẠT CHẤT LƯỢNG CAO
==================================================

Mục tiêu của patch này:
Tạo truyện sảng văn / vả mặt đô thị có cảm giác “đã”, nhưng không bị lố, không bị lặp, không bị tiện, không bị lỗi logic pháp lý, không để bằng chứng cuối rơi từ trời xuống.

Patch này override mọi rule yếu hơn bên trên.

==================================================
1. POST-OUTPUT TITLE CLEANER — KHÔNG ĐƯỢC LẶP TIÊU ĐỀ
==================================================

Sau khi viết xong mỗi chương, phải tự quét toàn bộ output.

Nếu thấy tiêu đề chương bị lặp liên tiếp, bắt buộc xóa dòng lặp trước khi trả kết quả.

Sai:
Chương 1: Shipper Ẩn Thân

Chương 1: Shipper Ẩn Thân

Đúng:
Chương 1: Shipper Ẩn Thân

Nếu có dòng dạng:
# Chương 1: Shipper Ẩn Thân

thì cũng phải xóa.

Mỗi chương chỉ được có đúng 1 tiêu đề chương.

Nếu không chắc, tự xóa dòng nghi ngờ bị lặp rồi trả về bản truyện sạch. Không xuất báo cáo lỗi ra nội dung.

==================================================
2. TỰ KIỂM TRA NỘI BỘ, KHÔNG IN RA
==================================================

Tự kiểm tra output thật vừa viết, không được kiểm tra theo ý định.

Nếu output thật có lặp tiêu đề, trôi tên, hoặc bằng chứng đến quá tiện, phải tự sửa trước khi trả lời.
Không in checklist/tự kiểm tra này ra nội dung chương.

Trước khi trả kết quả, tự hỏi:
- Có tiêu đề lặp không?
- Có tên nhân vật trùng vai không?
- Có bằng chứng nào chưa được cài trước không?
- Có chi tiết quyền lực nào quá lố không?
- Có cảnh pháp lý nào sai ngữ cảnh không?

Nếu có, tự sửa ngay.

==================================================
3. REALISTIC POWER RULE — MAIN MẠNH NHƯNG KHÔNG LỐ
==================================================

Nhân vật chính có thể là CEO, chủ tịch, đại lão, người có thế lực.

Nhưng cấm các hành động quá “ảo” khiến truyện mất độ tin:

Cấm:
- “Tôi mua lại khách sạn này trong 5 phút.”
- “Tôi gọi một cuộc là chặn toàn bộ sân bay.”
- “Tôi gọi một cuộc là ngân hàng giao hết sao kê.”
- “Tôi gọi một cuộc là tòa xử ngay.”
- “Toàn bộ nhân viên ở đây đều là người của tôi.”
- “Tôi đã tính hết mọi thứ từ đầu.”

Thay bằng phiên bản hợp lý hơn:

Thay vì:
“Tôi mua lại khách sạn này từ 5 phút trước.”

Viết:
“Khách sạn này là đối tác chiến lược của Thiên Phúc. Phòng họp báo anh thuê đang dùng hợp đồng truyền thông của tập đoàn tôi. Tôi có quyền yêu cầu dừng buổi họp nếu nó đang phát tán thông tin sai sự thật.”

Thay vì:
“Tôi gọi một cuộc là chặn chuyến bay.”

Viết:
“Tôi không thể chặn chuyến bay trực tiếp. Nhưng tôi có thể kích hoạt cảnh báo tuân thủ liên quan đến giao dịch đáng ngờ. Việc đó mua cho chúng ta mười lăm phút.”

Main càng mạnh càng phải hành động thông minh, không hành động như thần.

==================================================
4. LEGAL SCENE REALISM RULE — CẢNH PHÁP LÝ PHẢI ĐÚNG NGỮ CẢNH
==================================================

Không lẫn lộn:
- Tòa án
- Cơ quan điều tra
- Viện kiểm sát
- Công an
- Hội đồng quản trị
- Họp báo
- Đối chất nội bộ

Nếu chưa phải phiên tòa thật, không gọi là “phòng xử án”.

Với truyện vả mặt đô thị, ưu tiên dùng các bối cảnh hợp lý hơn:
- Buổi làm việc tại cơ quan điều tra
- Buổi đối chất nội bộ
- Phiên họp hội đồng quản trị
- Buổi họp báo
- Buổi kiểm tra đột xuất
- Buổi làm việc với kiểm toán độc lập
- Buổi cung cấp chứng cứ cho cơ quan chức năng

Không viết:
“Thẩm phán vừa bác bằng chứng, rồi Viện kiểm sát bước vào khởi tố ngay.”

Viết tốt hơn:
“Trong buổi đối chất tại cơ quan điều tra, luật sư Hải yêu cầu loại bằng chứng số vì nghi ngờ thu thập trái phép. Nhưng đúng lúc đó, kiểm sát viên phụ trách hồ sơ bước vào cùng kết quả giám định độc lập.”

Cảnh pháp lý có thể kịch tính, nhưng phải hợp ngữ cảnh.

==================================================
5. FINAL EVIDENCE FORESHADOW RULE — BẰNG CHỨNG CUỐI PHẢI ĐƯỢC CÀI TRƯỚC
==================================================

Cấm để bằng chứng quyết định xuất hiện lần đầu ở chương cuối.

Mọi bằng chứng dùng để hạ phản diện ở climax phải được cài ít nhất 2 chương trước đó.

Ví dụ:
Nếu chương 10 dùng “email cũ của Phạm Hoàng tự gửi cho chính mình”, thì chương 7 hoặc 8 phải cài trước:

“Huy nhìn một email cũ bị mã hóa trong hộp thư Phạm Hoàng. Tiêu đề chỉ có hai chữ: ‘Dự phòng’. Anh chưa mở được.”

Sau đó chương 10 mới mở được email đó.

Nếu chương cuối dùng:
- Email cũ
- Sổ tay
- USB
- Nhân chứng
- Sao kê ngân hàng
- Camera backup
- Ghi âm
- Tài khoản offshore
- Người phản bội

thì các thứ này phải từng được nhắc, nhìn thấy, nghi ngờ, hoặc cài manh mối trước đó.

Không dùng Deus Ex Machina.

==================================================
6. EVIDENCE LADDER RULE — BẰNG CHỨNG PHẢI LEO THANG
==================================================

Không có một bằng chứng nào thắng toàn bộ vụ án.

Bằng chứng phải leo thang theo bậc:

Bậc 1 — Manh mối:
Một cái tên lạ, hóa đơn lạ, chiết khấu lạ, bí danh.

Bậc 2 — Dấu hiệu:
Camera, email, log, lời khai chưa chính thức.

Bậc 3 — Bằng chứng có rủi ro:
Ghi âm, file hack, ảnh chụp sao kê, dữ liệu chưa xác minh.

Bậc 4 — Bằng chứng hỗ trợ:
Nhân chứng, sổ tay, hợp đồng giấy, bản in có dấu, camera từ nguồn hợp pháp.

Bậc 5 — Bằng chứng quyết định:
Giám định độc lập, xác nhận ngân hàng, lời khai chính thức, hồ sơ từ cơ quan chức năng, bản gốc có chuỗi lưu giữ rõ ràng.

Climax chỉ được thắng khi có ít nhất:
- 1 bằng chứng số
- 1 bằng chứng ngoài đời
- 1 nhân chứng hoặc xác nhận độc lập
- 1 cú phản công cuối của villain bị hóa giải

==================================================
7. NO CARTOON VILLAIN COLLAPSE RULE
==================================================

Phản diện không được chuyển từ “rất thông minh” sang “ngu ngốc quỳ lạy” quá nhanh.

Trước khi sụp, phản diện phải còn ít nhất một đòn:
- Luật sư phản bác
- Nói bằng chứng giả
- Đổ lỗi cho cấp dưới
- Dọa kiện ngược
- Dùng dư luận
- Lôi người chống lưng
- Hy sinh đồng phạm
- Nói main thu thập chứng cứ trái phép

Khi phản diện quỳ hoặc xin lỗi, phải có lý do:
- Bằng chứng cuối khóa đường lui
- Người chống lưng đã bỏ rơi
- Đồng phạm khai ngược
- Tiền bị phong tỏa
- Cơ quan chức năng vào cuộc
- Dư luận đổi chiều

Không để phản diện quỳ chỉ vì main nói vài câu ngầu.

==================================================
8. AFTERMATH PACING RULE — SAU CLIMAX PHẢI THỞ
==================================================

Sau chương climax, không mở arc mới quá mạnh ngay lập tức.

Cấu trúc sau climax:

Chương Climax:
- Phản diện chính sụp
- Bằng chứng quyết định xuất hiện
- Công lý bắt đầu

Chương Aftermath:
- Dư âm
- Tái cấu trúc
- Đồng minh nhận phần thưởng
- Main trả giá hoặc mệt mỏi
- Xử lý open thread chính

Chương Hook Arc 2:
- Chỉ mở 1 mối nguy mới
- Không nhồi 3 phản diện mới
- Không mở quá nhiều phe mới
- Hook phải rõ ràng, ngắn, lạnh

Không viết:
Chương 10 bắt Phạm Hoàng.
Chương 11 bắt ông Bình, lộ ông Hùng, mở Hoàng Gia.
Chương 12 gọi số Mỹ, mở mạng lưới quốc tế.

Viết tốt hơn:
Chương 10: Phạm Hoàng sụp.
Chương 11: Thiên Phúc tái cấu trúc, ông Bình bị triệu tập, hội đồng chia rẽ.
Chương 12: Một thiệp mời từ Hoàng Gia xuất hiện — chỉ một hook duy nhất.

ARC ESCALATION BUDGET:
- Arc 1 chỉ được xử lý phản diện/công ty/vụ án chính đã lập trong Story Bible.
- Không nhảy từ "hợp đồng công ty" sang "mạng lưới chính phủ/quốc tế/tài khoản offshore" nếu Story Bible chưa định nghĩa Arc 2.
- Nếu muốn mở Arc 2, chỉ mở bằng 1 dấu hiệu lạnh ở chương cuối/hậu ký; không giải thích toàn bộ mạng lưới trong cùng chương.
- Số tiền Arc 2 phải được tách rõ khỏi số tiền Arc 1, không tự phóng đại 25 tỷ thành 300 tỷ/30 tỷ offshore nếu chưa có nguồn.

==================================================
9. ARC 2 HOOK LIMIT RULE
==================================================

Cuối truyện chỉ được mở tối đa 1 hook lớn.

Hook tốt:
- Một cuộc gọi lạ
- Một thiệp mời từ đối thủ
- Một hồ sơ cũ được mở
- Một người đứng sau xuất hiện thoáng qua
- Một câu nhắn ngắn gây lạnh gáy

Không mở cùng lúc:
- Tập đoàn đối thủ
- Số nước ngoài
- Mạng lưới quốc tế
- Người bí ẩn
- Hồ sơ quá khứ
- Kẻ phản bội nội bộ

Chọn một.

Hook phải khiến người đọc tò mò, không làm người đọc mệt.

==================================================
10. NAME UNIQUENESS HARD RULE
==================================================

Không dùng cùng một tên cho hai nhân vật quan trọng.

Trước khi đặt tên nhân vật mới, kiểm tra danh sách tên đã dùng.

Nếu đã có:
- Huy = hacker

Thì không dùng:
- Thượng tá Huy
- Nhân viên IT Huy
- Luật sư Huy

Nếu đã có:
- Ông Bình = phó giám đốc vùng cũ

Thì không dùng:
- Nhà báo Bình
- Công an Bình
- Kiểm toán Bình

Mỗi tên quan trọng phải độc nhất.

Nếu lỡ trùng, tự đổi trước khi trả output.

==================================================
11. SUPPORT CHARACTER COMPETENCE RULE
==================================================

Nếu một nhân vật phụ được thăng chức hoặc giao vai trò lớn, phải cài năng lực từ trước.

Ví dụ:
Nếu chị Hoa được làm quản lý chi nhánh, trước đó phải cho thấy:
- Chị hiểu quy trình
- Chị từng cảnh báo sai phạm
- Chị được nhân viên tin
- Chị từng quản lý nhóm nhỏ
- Chị có đạo đức và năng lực

Không viết:
“Chị ấy tử tế với main nên được làm giám đốc.”

Viết:
“Chị Hoa từng là tổ trưởng vận hành, bị Phạm Hoàng đì xuống kho vì không chịu ký khống. Cả chi nhánh đều biết chị là người giữ quy trình sạch nhất.”

==================================================
12. TEASER-CONTENT MATCH RULE
==================================================

Teaser SEO phải khớp nội dung chương.

Nếu teaser nói:
- Bằng chứng bị mất
- Nhân chứng rút lui
- Main bị hội đồng nghi ngờ
- Phản diện phản công
- Cổ phiếu giảm
- Tòa bác bằng chứng

thì trong chương phải thật sự xảy ra.

Không được hứa rock bottom rồi giải quyết sạch trong cùng một cảnh.

Teaser không được nói quá so với nội dung.

==================================================
13. INTERNAL QUALITY GATE — TỰ SỬA, KHÔNG IN ĐIỂM
==================================================

Trước khi trả chương/truyện, tự chấm ngầm theo thang điểm sau:

1. Hook mở đầu: /10
2. Nhục ban đầu: /10
3. Nhịp vả mặt: /10
4. Phản diện thông minh: /10
5. Evidence cost: /10
6. Hacker limit: /10
7. Rock bottom: /10
8. Lộ thân phận theo tầng: /10
9. Logic pháp lý/ngữ cảnh: /10
10. Ending/Hook: /10

Nếu bất kỳ mục nào dưới 9.2, phải tự sửa trước khi trả.
KHÔNG in điểm, KHÔNG in bất kỳ nhãn đánh giá chất lượng nào.
Output cuối cùng vẫn phải tuân thủ format của prompt chính.

==================================================
14. FINAL AUDIT NỘI BỘ — KHÔNG IN KẾ HOẠCH SỬA TRONG WRITER
==================================================

Sau khi viết xong, tự audit nội bộ:

A. Lỗi lớn:
- Lặp tiêu đề
- Trôi tên
- Main toàn năng
- Hacker quá thần
- Bằng chứng cuối chưa cài
- Pháp lý sai ngữ cảnh
- Climax lặp
- Hook quá nhiều

B. Lỗi vừa:
- Chương lặp chức năng
- Phản diện quỳ hơi nhanh
- Nhân vật phụ thăng chức chưa đủ cài
- Dư luận đổi chiều quá nhanh

C. Lỗi nhỏ:
- Câu thoại hơi kịch
- Từ ngữ lặp
- Nhịp chương hơi dài
- Teaser hơi quá

Nếu có lỗi lớn, tự sửa lại trước khi trả output.
KHÔNG in nhãn yêu cầu sửa, kế hoạch sửa, Change Log hoặc Audit Report trong chương truyện.

==================================================
15. ONE-PASS POLISH RULE
==================================================

Sau khi generate xong truyện, tự polish một lượt trước khi trả.

Polish checklist:
- Xóa tiêu đề lặp
- Rút câu thừa
- Thay chi tiết quá lố bằng chi tiết hợp lý hơn
- Cài lại bằng chứng cuối nếu chưa được foreshadow
- Đổi cảnh “tòa” thành “cơ quan điều tra/đối chất” nếu chưa hợp
- Giảm số hook cuối xuống còn 1
- Kiểm tra tên nhân vật không trùng
- Làm câu kết chương sắc hơn

Không trả bản nháp thô.
Chỉ trả bản đã polish.

`;


export const getStoryBiblePrompt = (p: StoryBibleParams) => `\
Bạn là STORY BIBLE ARCHITECT (Kiến trúc sư nội dung) cho truyện mạng Zhihu / micro-drama Việt Nam.

BẮT BUỘC viết bằng tiếng Việt tự nhiên, đúng xưng hô và văn phong truyện mạng Việt Nam.
KHÔNG ĐƯỢC viết chương truyện. Chỉ tạo Story Bible.
Tạo một Story Bible nghiêm ngặt nhằm ngăn chặn sạn logic (plot holes), trôi tên nhân vật (name drift), và twist mồ côi (orphan twists).

INPUT:
- Thể loại (Genre): ${p.genre}
- Số chương (Chapter count): ${p.chapter_count}
- Điểm nhấn chính (Main hook): ${p.main_hook}
- Ý tưởng nhân vật chính (Protagonist seed): ${p.protagonist_seed}
- Ý tưởng phản diện (Villain seed): ${p.villain_seed}
- Bối cảnh (Setting): ${p.setting}
- Tông truyện (Tone): ${p.tone}
- Yêu cầu đặc biệt: ${p.special_requirements || 'Không có'}

━━━ PATCH 6: GENRE-SPECIFIC CONSTRAINTS (bắt buộc) ━━━
${/trọng sinh|xuyên không|tái sinh|rebirth|reborn|hệ thống/i.test(p.genre || '') ? `
THỂ LOẠI ĐẶC BIỆT: TRỌNG SINH / XUYÊN KHÔNG / TÁI SINH
Quy tắc BẮT BUỘC cho thể loại này:

1. KNOWLEDGE BLIND SPOTS — Main mang ký ức kiếp trước nhưng PHẢI có ít nhất:
   - 3 thông tin main TƯỞNG đúng nhưng kiếp này ĐÃ THAY ĐỔI (VD: nhân vật X kiếp trước là đồng minh nhưng kiếp này đã bị mua chuộc)
   - 2 nhân vật HOÀN TOÀN MỚI mà main KHÔNG biết từ kiếp trước
   - 1 sự kiện main NHỚ SAI hoặc nhớ lệch thời gian
   Liệt kê cụ thể trong Bible mục "knowledge_blind_spots".

2. BODY IDENTITY CONFLICT — Nếu main ở trong cơ thể người khác:
   - Giấy tờ tùy thân KHÔNG KHỚP → phải là rào cản thật trong ít nhất 2 chương
   - Người thân của cơ thể cũ có thể xuất hiện và gây phức tạp
   - Main KHÔNG ĐƯỢC dùng danh tính kiếp cũ trước 60% truyện

3. KNOWLEDGE DECAY — Ký ức kiếp trước mờ dần theo thời gian hoặc bị kích hoạt bởi trigger cụ thể. Main không thể nhớ MỌI THỨ rõ ràng.

4. BUTTERFLY EFFECT — Ít nhất 2 sự kiện diễn ra KHÁC kiếp trước vì main đã can thiệp sớm. Hành động của main thay đổi tương lai → main mất lợi thế biết trước.
` : ''}
${/hệ thống|system|level up|cấp độ/i.test(p.genre || '') ? `
THỂ LOẠI ĐẶC BIỆT: HỆ THỐNG / LEVEL UP
Quy tắc BẮT BUỘC:
1. Hệ thống KHÔNG giải quyết mọi vấn đề. Mỗi buff/skill phải có cooldown, giới hạn, hoặc side effect.
2. Main không được dựa vào hệ thống quá 3 lần trong toàn truyện để giải quyết khủng hoảng.
3. Ít nhất 1 lần hệ thống gây hại hoặc đưa ra thông tin sai.
` : ''}

Yêu cầu (Requirements):
1. Nhân vật chính bắt đầu với thông tin/kiến thức không đầy đủ.
2. Phản diện chính phải được đặt tên và gieo manh mối (foreshadowed) ngay trong chương 1 hoặc 2.
3. ${isFaceSlapStr(p.genre) ? 'Nhân vật chính có lợi thế ẩn nhưng bắt đầu với thông tin chưa đủ, phải chịu nhục và trả giá để lấy bằng chứng. Không được toàn năng.' : 'Ít nhất 2 lần nhân vật chính thực sự mất mát/thất bại.'}
4. ${isFaceSlapStr(p.genre) ? 'Ưu tiên sảng điểm (Face-slapping), nhưng phải có ít nhất 1 lần phản diện thắng thật hoặc main mất lợi thế thật trước cú lật lớn.' : 'Ít nhất 1 chương chạm đáy (Rock Bottom) hoàn toàn.'}
5. Mọi twist lớn phải có 3 manh mối rải rác trước khi hé lộ — liệt kê cụ thể 3 manh mối đó trong Foreshadowing Plan.
6. Bằng chứng phải thực tế: hợp đồng, hóa đơn, ghi âm hợp pháp hoặc bị challenge, camera hợp lý, nhân chứng, sao kê có nguồn hợp lệ, tài liệu vật lý.
7. Không có hacker ma thuật. Không có backup thần kỳ/chuẩn bị sẵn mà không báo trước. Hacker chỉ hỗ trợ log, metadata, timestamp; mọi bằng chứng số cần bằng chứng ngoài đời đi kèm.
8. Phản diện thông minh, biết phản công, chỉ thua vì chuỗi bằng chứng + nhân chứng + quy trình đã được gieo từ trước.
9. Đồng minh phải có giới hạn, có nỗi sợ, và có lý do để giúp đỡ; không phục tùng main vô điều kiện.
10. Tên, con số, dòng thời gian phải được khóa chặt (không thay đổi).
	11. **POV LOCK**: Chọn ĐÚNG MỘT góc nhìn (POV) ngay trong Story Bible và khóa chặt xuyên suốt toàn truyện:
	    - Ngôi thứ ba giới hạn (Third-person limited): "Linh nhìn...", "Cô ta bước..."
	    - Ngôi thứ nhất (First-person): "Tôi nhìn...", "Tôi bước..."
	    KHÔNG được đổi POV giữa các chương. Ghi rõ vào Story Bible: POV_MODE = [third_person | first_person]

	━━━ PATCH 6B: URBAN FACE-SLAP EMOTION ENGINE (bắt buộc nếu genre có Vả Mặt/Sảng Văn/Đô Thị) ━━━
	${isFaceSlapStr(p.genre) ? `
	12. **HUMILIATION LADDER**: Bible PHẢI có "humiliation_ladder" gồm đúng ${p.chapter_count} mục. Mỗi chương ghi:
	   - ai làm nhục main hoặc đồng minh,
	   - làm nhục bằng hành động/câu thoại gì,
	   - ai chứng kiến,
	   - main phải nhịn vì giới hạn nào.
	   Nếu một chương không có nhục nhã trực tiếp, phải có áp lực địa vị hoặc đòn xã hội thay thế.

	13. **FACESLAP PAYOFF LADDER**: Bible PHẢI có "faceslap_payoff_ladder" gồm các cú vả mặt tăng cấp:
	   - private_correction, public_embarrassment, evidence_reversal, authority_reversal, financial_reversal, public_identity_reveal, legal_collapse.
	   - Mỗi cú vả phải có "stage", "trigger_humiliation", "proof_used", "witnesses", "villain_denial", "visible_consequence".
	   - Không được để chương 1-3 vả mặt quá lớn; đầu truyện chỉ được vả nhỏ hoặc gieo cảm giác chờ đợi.

	14. **ARROGANCE SCRIPT**: Bible PHẢI có "villain_arrogance_script" gồm 8-12 câu/kiểu sỉ nhục đặc trưng của phản diện và phe hắn. Các câu này phải cụ thể với công ty, chức vụ, lương, bàn làm việc, hồ sơ, nhóm chat, quyền ký duyệt.

	15. **SOCIAL WITNESS PLAN**: Bible PHẢI có "social_witness_plan" chỉ rõ các nhóm chứng kiến: đồng nghiệp kế toán, bảo vệ, HĐQT, luật sư, cổ đông, truyền thông, cơ quan điều tra. Mỗi nhóm phải đổi thái độ theo từng mốc.

		16. **PAYOFF PACING PLAN**: Bible PHẢI có "payoff_pacing_plan" chia rõ:
		   - early_small_wins: các cú thắng nhỏ ở 20% đầu, không giải quyết vụ chính.
		   - villain_wins_middle: ít nhất 2 chương giữa truyện phản diện thắng thật, nêu thiệt hại cụ thể.
		   - recovery_clean_evidence: các chương main phục hồi bằng chứng sạch.
		   - penultimate_lock: chương áp chót chỉ khóa đường lui/đối chất/niêm phong, KHÔNG bắt hoặc xử án trùng climax.
		   - final_collapse: chương cuối mới có cú sụp pháp lý chính.

		16B. **EVIDENCE DRIP PLAN**: Bible PHẢI có "evidence_drip_plan" để tránh main thắng quá dễ:
		   - starter_clues: chương 1-2 chỉ có manh mối yếu/bằng chứng nhỏ, không đủ hạ phản diện.
		   - challenged_evidence: ít nhất 2 bằng chứng bị phản diện công kích là giả/sai nguồn/thiếu chuỗi lưu giữ.
		   - lost_or_blocked_assets: ít nhất 1 lần main mất bản gốc, mất quyền truy cập, bị khóa kênh công khai, hoặc nhân chứng rút lui.
		   - clean_corroboration: bằng chứng sạch chỉ hoàn chỉnh sau khi có đối chiếu độc lập.

		16C. **CROWD CONVERSION PLAN**: Bible PHẢI có "crowd_conversion_plan" gồm các bậc thái độ xã hội:
		   - mockery: ai cười/khinh main lúc đầu.
		   - doubt: chương nào họ bắt đầu nghi ngờ phản diện.
		   - silence: chương nào đám đông im bặt vì bằng chứng.
		   - reversal: chương nào họ chủ động cung cấp thông tin hoặc xin lỗi.
		   Không được cho đám đông quay sang tung hô main ngay sau một clip đầu tiên.

		17. **PROFESSIONAL HUMILIATION STYLE**: Bible PHẢI có "humiliation_style_boundaries":
	   - liệt kê các kiểu nhục công sở được phép dùng nhiều lần (cắt quyền, giao việc bẩn, bêu nhóm chat, bắt nhận lỗi, chặn hệ thống).
	   - liệt kê câu chửi thô bị giới hạn tối đa 1 lần.
	   - phản diện cấp quản lý không được gào chửi như côn đồ trong mọi cảnh; phải có giọng mỉa mai, lạnh, quyền lực.

	18. **TRAITOR FORESHADOW PLAN**: Nếu có đồng minh giả/phó tổng/luật sư/nội bộ phản bội, Bible PHẢI có "traitor_foreshadow_plan" gồm ít nhất 3 manh mối trước khi lộ: câu né tránh, chữ ký đáng ngờ, email/initial, quyết định bị trì hoãn, hoặc lời khuyên nghe như bảo vệ main nhưng thực ra chặn điều tra.
		` : ''}

	━━━ PATCH 9: CHARACTER DEPTH ENGINE (bắt buộc) ━━━

		19. **PROTAGONIST WEAKNESS MANDATE**: Main BẮT BUỘC có ít nhất 2 điểm yếu CỤ THỂ (không phải "quá chính nghĩa"). Ví dụ:
   - Nóng nảy → hành động bốc đồng gây hậu quả thật
   - Cô đơn / không tin ai → bỏ lỡ đồng minh quan trọng
   - Ám ảnh quá khứ → phán đoán sai vì thiên kiến
   - Quá tự tin → đánh giá thấp phản diện, bị phản công
   Liệt kê 2 điểm yếu cụ thể vào "protagonist.weaknesses" trong Bible. Mỗi điểm yếu phải gây hậu quả thật ở ít nhất 1 chương.

		20. **VILLAIN COMPLEXITY MANDATE**: Phản diện chính PHẢI có:
   - (a) Một động cơ có logic nội tại (không chỉ "tham lam" — tại sao tham? Bắt đầu từ đâu? Có gì đáng thương?)
   - (b) Một khoảnh khắc "con người" (chăm con, nhớ quá khứ nghèo, sợ mất tất cả)
   - (c) Ít nhất 1 phẩm chất tích cực (thông minh, trung thành với đàn em, yêu gia đình)
   Liệt kê vào "main_villain.human_side" trong Bible.

		21. **ALLY AGENCY MANDATE**: Đồng minh chính PHẢI có:
   - (a) Arc riêng: có mục tiêu cá nhân, không chỉ phục vụ main
   - (b) Ít nhất 1 lần KHÔNG ĐỒNG Ý với main hoặc từ chối giúp
   - (c) Ít nhất 1 hành động chủ động (không phải lúc nào cũng chờ main nhờ)
   Liệt kê vào "supporting_characters[0].personal_arc" trong Bible.

		22. **NAME UNIQUENESS ABSOLUTE**: TUYỆT ĐỐI CẤM có 2 nhân vật cùng HỌ hoặc cùng TÊN. Nếu phản diện tên Hải thì cấp trên không được tên Hải. Kiểm tra kỹ trước khi output.

━━━ PATCH 12: CORPORATE LEGAL REALISM ENGINE (bắt buộc) ━━━

		23. **UNDERCOVER PLAUSIBILITY MANDATE**: Nếu main là chủ tịch/CEO/người thừa kế/đại lão ẩn thân trong chính công ty, Story Bible PHẢI giải thích vì sao người trong công ty không nhận ra:
   - ít xuất hiện truyền thông, ảnh công khai cũ/khác hiện tại, công ty có nhiều pháp nhân/chi nhánh, chức vụ mới chưa công bố, hoặc main dùng hồ sơ do HĐQT/law firm bảo trợ.
   - Liệt kê cụ thể vào "undercover_plausibility".
   - Nếu chỉ cần tra Google là lộ ngay mà không có lý do, phải đổi premise thành "người thừa kế/chủ tịch mới chưa công bố" thay vì CEO nổi tiếng.

		24. **LEGAL PROCESS PLAN**: Với truyện doanh nghiệp/pháp lý, Bible PHẢI có kế hoạch quy trình:
   - bước nội bộ: kiểm toán, đối chất, HĐQT, tạm đình chỉ;
   - bước bên ngoài: đơn tố cáo, luật sư, cơ quan điều tra, niêm phong/khám xét nếu có căn cứ;
   - độ trễ tối thiểu: không bắt/phong tỏa/xử án ngay trong cùng ngày trừ khi có "khẩn cấp" được cài trước.
   Liệt kê vào "legal_process_plan".

		25. **EVIDENCE LADDER PLAN**: Mỗi vụ chính phải có 5 bậc bằng chứng:
   1. manh mối; 2. dấu hiệu đối chiếu; 3. bằng chứng vùng xám bị phản bác; 4. bằng chứng sạch; 5. xác nhận độc lập/chuỗi lưu giữ.
   Liệt kê bậc, chương gieo, chương payoff, rủi ro pháp lý vào "evidence_ladder".

		26. **VIETNAM THREAT BOUNDARY**: Nếu setting ở Việt Nam hiện đại, phản diện doanh nghiệp ưu tiên phản công bằng luật sư, truyền thông, nhân sự, tài chính, đe dọa nghề nghiệp/gia đình, mua chuộc nhân chứng, hoặc hồ sơ giả.
   Bạo lực dao kéo/bắt cóc/xe tông chỉ được dùng nếu đã cài mạng lưới tội phạm và hậu quả công an rõ. Liệt kê ranh giới vào "violence_boundaries".

━━━ PATCH 1: NAME SAFETY CHECK (bắt buộc TRƯỚC khi output) ━━━
Bước 1 — Liệt kê TOÀN BỘ tên nhân vật quan trọng (main, ally, villain cấp 1–3).
Bước 2 — Kiểm tra từng cặp:
  □ Có 2 nhân vật nào cùng họ hoặc cùng tên không? (VD: cả hai tên Tuấn, Hùng, Lan)
  □ Có tên nào phát âm dễ nhầm không? (Tuấn/Thuận, Hùng/Hưng, Lan/Lanh, Minh/Mạnh)
  □ Có 2 nhân vật quan trọng xuất hiện gần nhau có tên bắt đầu cùng chữ không?
Bước 3 — Nếu có xung đột: TỰ ĐỔI TÊN trước khi output. Ghi chú thay đổi.
Bước 4 — Output bảng xác nhận:
  | Tên | Vai trò | Phe | Tầng quyền lực (1–5) | Ghi chú |

OUTPUT STRICT JSON ONLY:
Không Markdown, không code fence, không lời giải thích ngoài JSON.
Trả đúng một JSON object theo schema sau:
{
  "title": "Tên truyện",
  "genre": "${p.genre}",
  "recommended_chapters": ${p.chapter_count},
  "chapter_count_requested": ${p.chapter_count},
	  "logline": "1-2 câu",
	  "core_promise": "Lời hứa cảm xúc chính",
	  "humiliation_ladder": [
	    {
	      "chapter": 1,
	      "humiliator": "Ai làm nhục/ép main hoặc đồng minh",
	      "humiliation_action": "Hành động/câu thoại làm nhục cụ thể, không chung chung",
	      "public_stage": "Nơi xảy ra và ai chứng kiến",
	      "why_main_must_endure": "Lý do main chưa thể lật bài ngay"
	    }
	  ],
	  "faceslap_payoff_ladder": [
	    {
	      "chapter": 1,
	      "faceslap_level": "private_correction | public_embarrassment | evidence_reversal | authority_reversal | financial_reversal | public_identity_reveal | legal_collapse",
	      "trigger_humiliation": "Cảnh nhục nào được trả lại",
	      "proof_used": "Bằng chứng/cơ chế dùng để lật",
	      "witnesses": "Ai chứng kiến",
	      "villain_denial": "Phản diện phản bác/chống cự thế nào",
	      "visible_consequence": "Hậu quả thấy ngay trên trang"
	    }
	  ],
	  "payoff_pacing_plan": {
	    "early_small_wins": ["Chương 1-20% đầu: thắng nhỏ, sửa lỗi nhỏ, làm phản diện chột dạ"],
	    "villain_wins_middle": ["Ít nhất 2 chương giữa truyện phản diện thắng thật: mất quyền truy cập/mất bản gốc/bị đình chỉ/đồng minh rút lui"],
	    "recovery_clean_evidence": ["Main phục hồi bằng chứng sạch hơn, có nguồn và chuỗi xác thực"],
	    "penultimate_lock": "Chương áp chót chỉ đối chất/niêm phong/triệu tập/khóa đường lui; KHÔNG bắt người hoặc xử án trùng climax",
	    "final_collapse": "Chương cuối mới có quyết định bắt/áp giải/tạm giam hoặc hậu quả pháp lý chính"
	  },
	  "evidence_drip_plan": {
	    "starter_clues": ["Chương 1-2 chỉ gieo manh mối yếu/bằng chứng nhỏ"],
	    "challenged_evidence": ["Bằng chứng nào bị phản diện phản bác, ở chương nào"],
	    "lost_or_blocked_assets": ["Main mất gì thật: bản gốc/quyền truy cập/kênh công khai/nhân chứng"],
	    "clean_corroboration": ["Bằng chứng sạch hoàn chỉnh nhờ đối chiếu độc lập nào"]
	  },
	  "crowd_conversion_plan": {
	    "mockery": "Nhóm nào khinh/cười main lúc đầu",
	    "doubt": "Mốc họ bắt đầu nghi ngờ",
	    "silence": "Mốc họ im bặt trước bằng chứng",
	    "reversal": "Mốc họ xin lỗi/cung cấp thông tin/đổi phe"
	  },
	  "humiliation_style_boundaries": {
	    "repeatable_office_pressure": ["Cắt quyền hệ thống", "Giao việc bẩn", "Bêu nhóm chat", "Bắt ký biên bản", "Chặn vào phòng họp", "Cắt phụ cấp"],
	    "rough_insults_max_once": ["Các câu chửi thô như ăn mày/con kiến/trường chó chỉ dùng tối đa 1 lần toàn truyện hoặc không dùng"],
	    "preferred_tone": "Mỉa mai lạnh, áp chế bằng chức vụ/quy trình, không gào chửi như côn đồ ở mọi cảnh"
	  },
	  "traitor_foreshadow_plan": [
	    {
	      "traitor_name": "Tên nhân vật phản bội nếu có",
	      "clues": [
	        {"chapter": 2, "clue": "Manh mối 1"},
	        {"chapter": 6, "clue": "Manh mối 2"},
	        {"chapter": 10, "clue": "Manh mối 3"}
	      ],
	      "reveal_chapter": "Chương lộ"
	    }
	  ],
	  "pov_mode": "first_person hoặc third_person",
  "setting_lock": {
    "country": "Việt Nam",
    "city_or_region": "Địa điểm chính, ví dụ TP.HCM/Quận 3",
    "forbidden_location_drifts": ["Không tự chuyển sang Hà Nội nếu Bible khóa TP.HCM"],
    "time_span": "Khoảng thời gian diễn ra truyện"
  },
  "protagonist": {
    "full_name": "Họ tên đầy đủ, duy nhất",
    "role": "Vai trò thật",
    "public_mask": "Vỏ bọc nếu có",
    "undercover_plausibility": "Nếu ẩn thân: lý do cụ thể vì sao nhân viên/phản diện không nhận ra; nếu không ẩn thân ghi 'none'",
    "limits": ["Giới hạn thật của main"],
    "weaknesses": ["Điểm yếu tính cách 1 — gây hậu quả thật", "Điểm yếu tính cách 2 — gây hậu quả thật"],
    "knows_at_start": ["Điều main biết ở chương 1"],
    "wrong_assumptions": ["Điều main tin sai ở đầu truyện"]
  },
	  "main_villain": {
	    "full_name": "Họ tên đầy đủ, duy nhất",
	    "role": "Vai trò",
	    "strengths": ["Điểm mạnh/thế lực"],
	    "counterattack_style": "Cách phản công",
	    "arrogance_script": ["8-12 câu/kiểu sỉ nhục đặc trưng, cụ thể với bối cảnh đô thị/công ty"],
	    "motivation_origin": "Tại sao trở thành kẻ xấu — backstory ngắn gọn",
	    "human_side": "Khoảnh khắc con người / phẩm chất tích cực duy nhất",
	    "fear": "Nỗi sợ lớn nhất"
	  },
  "supporting_characters": [
    {
      "full_name": "Họ tên đầy đủ",
      "role": "Vai trò",
      "relationship_to_main": "Quan hệ với main",
      "limits_or_fear": "Giới hạn/nỗi sợ",
      "personal_arc": "Mục tiêu cá nhân của nhân vật này (không liên quan đến main)",
      "disagree_moment": "Chương nào sẽ từ chối/phản đối main"
    }
  ],
  "characterMap": {
    "main": "Họ tên main",
    "villain_main": "Họ tên phản diện chính",
    "ally_primary": "Họ tên đồng minh chính",
    "vip_customer": "Họ tên khách/phản diện phụ nếu có",
    "company_name": "Tên công ty/tập đoàn chính"
  },
	  "fixed_data_locks": {
	    "company_names": [],
	    "money_amounts": [],
	    "key_dates": [],
	    "legal_statuses": []
	  },
	  "social_witness_plan": [
	    {
	      "group": "Nhóm người chứng kiến: đồng nghiệp/HĐQT/luật sư/cổ đông/truyền thông",
	      "initial_attitude": "Ban đầu họ khinh/nghi ngờ/sợ hãi thế nào",
	      "turning_chapter": "Chương thái độ đổi chiều",
	      "changed_attitude": "Sau cú vả mặt họ đổi thái độ thế nào"
	    }
	  ],
  "legal_process_plan": [
    {
      "stage": "Nội bộ / cơ quan điều tra / ngân hàng / tòa án",
      "chapter_range": "Chương nào",
      "required_documents": ["Đơn tố cáo, biên bản, hợp đồng gốc, lời khai..."],
      "minimum_delay_or_condition": "Độ trễ hoặc điều kiện khẩn cấp cần có",
      "what_cannot_happen_yet": "Những hành động pháp lý chưa được phép xảy ra ở giai đoạn này"
    }
  ],
  "evidence_ladder": [
    {
      "level": "1-5",
      "evidence": "Tên bằng chứng",
      "source": "Nguồn hợp lý",
      "foreshadow_chapter": 1,
      "payoff_chapter": 1,
      "legal_risk": "Thấp/Trung bình/Cao",
      "corroboration": "Nhân chứng/xác nhận/bản gốc đi kèm"
    }
  ],
  "evidence_chain": [
    {
      "name": "Tên bằng chứng",
      "source": "Nguồn hợp lý",
      "cost": "Cái giá phải trả",
      "legal_risk": "Thấp/Trung bình/Cao",
      "required_corroboration": "Bằng chứng ngoài đời đi kèm",
      "foreshadow_chapter": 1
    }
  ],
  "violence_boundaries": {
    "setting": "Việt Nam hiện đại hoặc khác",
    "allowed_pressure_methods": ["Kiện ngược", "mua chuộc nhân chứng", "tung tin bẩn", "đình chỉ nội bộ"],
    "forbidden_or_rare_methods": ["Dao kéo công khai", "bắt cóc", "xe tông người nếu chưa cài hậu quả pháp lý"],
    "consequence_if_violated": "Nếu có bạo lực, chương sau phải có công an/hồ sơ y tế/nhân chứng/hậu quả rõ"
  },
  "villain_counterattack_chain": [
    {
      "chapter_range": "Ví dụ 3-4",
      "move": "Phản diện làm gì",
      "real_damage_to_main": "Main mất gì"
    }
  ],
  "identity_reveal_plan": {
    "layer_1_hint": "Chương nào",
    "layer_2_partial": "Chương nào",
    "layer_3_mid_villain_knows": "Chương nào",
    "layer_4_public_reveal": "Chỉ sau 60% tổng số chương",
    "layer_5_power_reversal": "25% cuối"
  },
  "foreshadowing_plan": [
    {
      "twist": "Tên twist",
      "clues": [
        {"chapter": 1, "clue": "Manh mối 1"},
        {"chapter": 2, "clue": "Manh mối 2"},
        {"chapter": 3, "clue": "Manh mối 3"}
      ]
    }
  ],
  "forbidden_inconsistencies": [
    "Không đổi tên nhân vật",
    "Không đổi địa lý đã khóa",
    "Không để Change Log, Self-Check hoặc STATE UPDATE JSON lẫn vào nội dung truyện xuất bản"
  ],
  "name_safety_check_result": "Xác nhận không có tên trùng/dễ nhầm"
}`;

// ── 2. CHAPTER MAP GENERATOR ──────────────────────────────────────────────────
export const getChapterMapPrompt = (story_bible: string, chapter_count: number) => `\
Bạn là CHAPTER MAP PLANNER (Người lên sơ đồ chương) cho truyện mạng Zhihu / micro-drama Việt Nam.

BẮT BUỘC viết bằng tiếng Việt tự nhiên, đúng xưng hô và văn phong truyện mạng Việt Nam.
Sử dụng Story Bible để tạo ra cấu trúc diễn biến cho từng chương.

INPUT:
${story_bible}

Số chương mục tiêu (Target chapter count):
${chapter_count}

Quy tắc (Rules):
1. ACTION ≤ 45%.
2. BUILD ≥ 30%.
3. ${isFaceSlapStr(story_bible) ? 'COLLAPSE có thể là phản diện thắng thế, bằng chứng bị challenge, hoặc main mất lợi thế thật; không được là bẫy quá dễ của main.' : 'COLLAPSE ≥ 20%.'}
4. ${isFaceSlapStr(story_bible) ? 'Phải có ít nhất 1 chương VILLAIN_WINS hoặc ROCK_BOTTOM nhẹ trước màn vả mặt lớn.' : 'Ít nhất 1 chương chạm đáy (Rock Bottom) hoàn toàn.'}
5. ${isFaceSlapStr(story_bible) ? 'Thất bại có thể tạm thời nhưng phải gây thiệt hại cụ thể: mất bằng chứng, mất lòng tin, đồng minh bị dọa, hoặc bị khóa đường pháp lý.' : 'Ít nhất 2 lần mất mát/thất bại thực sự trước chiến thắng cuối cùng.'}
6. Không được có 3 chương ACTION liên tiếp.
7. Trùm cuối (Final boss) phải được gieo manh mối ở chương 1 hoặc 2.
8. Không lặp lại bối cảnh/sự kiện liên chương (No duplicate scenes).
9. Mỗi chương phải làm thay đổi trạng thái câu chuyện.
10. Chương cuối phải giải quyết triệt để toàn bộ vụ án/vấn đề chính.

${isFaceSlapStr(story_bible) ? getFaceSlapOverride() : ''}

━━━ PATCH 2: CHAPTER FUNCTION REGISTRY (bắt buộc) ━━━
Trước khi lên bảng chương, gán mỗi chương ĐÚNG MỘT nhãn chức năng:
	  [HUMILIATE]       → Bị nhục nhã, ép buộc, khinh thường
  [INVESTIGATE]     → Thu thập manh mối, điều tra ngầm
  [EVIDENCE_FOUND]  → Tìm được bằng chứng quan trọng
  [EVIDENCE_LOST]   → Mất bằng chứng, bị xóa dấu vết
  [FACESLAP_SMALL]  → Vả mặt nhỏ (riêng tư hoặc bẽ mặt nhẹ)
  [FACESLAP_BIG]    → Vả mặt lớn (công khai, tài chính, quyền lực)
  [VILLAIN_WINS]    → Phản diện chiếm lợi thế thật sự
  [VILLAIN_EXPOSED] → Một phản diện bị lộ mặt / bị hạ
  [ALLY_THREATENED] → Đồng minh bị đe dọa / bị mất
  [IDENTITY_HINT]   → Gieo manh mối về thân phận main
  [IDENTITY_REVEAL] → Lộ thân phận (theo tầng)
  [ROCK_BOTTOM]     → Main thua hoàn toàn, mất kiểm soát
  [BOARD_CONFLICT]  → Hội đồng / cấp trên gây khó khăn
  [LEGAL_MOVE]      → Hành động pháp lý (tố cáo, tòa án)
  [AFTERMATH]       → Xử lý hậu quả sau chiến thắng
  [HOOK_ARC2]       → Mở tuyến arc mới

	QUY TẮC REGISTRY (vi phạm = phải viết lại bảng):
	  □ Không gán cùng một nhãn cho 2 chương LIÊN TIẾP.
	  □ [HUMILIATE] tối đa 3 lần trong toàn truyện, nhưng mọi chương đều phải có áp lực địa vị nếu là Đô Thị Vả Mặt.
	  □ [FACESLAP_BIG] phải đến SAU ít nhất 1 [VILLAIN_WINS].
	  □ [ROCK_BOTTOM] xuất hiện đúng 1 lần, ở khoảng 40–60% truyện.
	  □ [LEGAL_MOVE] không được liền kề [VILLAIN_EXPOSED].

	━━━ PATCH 2B: FACE-SLAP SCENE CONTRACT (bắt buộc nếu là Đô Thị Vả Mặt) ━━━
	${isFaceSlapStr(story_bible) ? `
	Mỗi chương trong Chapter Map PHẢI có:
	- public_stage: sân khấu xã hội cụ thể hoặc "private_pressure" nếu cảnh kín nhưng vẫn có hậu quả xã hội.
	- humiliation_beat: hành động/câu thoại làm nhục hoặc áp lực địa vị cụ thể.
		- faceslap_payoff: cú trả đũa trong chương, hoặc "deferred" nếu chương này chỉ nén.
		- witness_reaction: đám đông/đồng minh/nhân viên/HĐQT đổi thái độ thế nào.
		- villain_arrogance_line: một câu ngạo mạn cụ thể của phản diện/phe phản diện trong chương.
		- main_loss: nếu phản diện thắng hoặc chương nén ức chế, main mất gì thật (danh dự, quyền truy cập, bản gốc, đồng minh, tiền, sân khấu công khai). Nếu thắng nhỏ thì ghi "minor_only".
		- evidence_state: tình trạng bằng chứng trong chương: "clue_only" | "challenged" | "lost_or_blocked" | "corroborated" | "clean".
		- crowd_stance: thái độ xã hội hiện tại: "mocking" | "doubting" | "silent" | "turning" | "supporting".
		- payoff_debt_repaid: cú vả mặt đang trả lại món nhục nào đã gieo trước đó; nếu chưa trả thì ghi "deferred_debt".

	Tỉ lệ cho ${chapter_count} chương:
	- Ít nhất ceil(${chapter_count} * 0.45) chương phải có humiliation_beat rõ.
	- Ít nhất ceil(${chapter_count} * 0.33) chương phải có faceslap_payoff khác "deferred".
	- Các cú vả mặt phải tăng cấp: nhỏ riêng tư → bẽ mặt trước phòng ban → mất quyền/lợi ích → lộ thân phận/quyền lực → sụp pháp lý.
	- Nếu chương thiên điều tra/pháp lý, vẫn phải có một cảnh người-với-người tạo áp lực địa vị trước hoặc sau manh mối.
		- 20% đầu chỉ được private_correction/public_embarrassment nhỏ; không được authority_reversal lớn.
		- Từ 25% đến 55% tổng truyện PHẢI có ít nhất 2 chương faceslap_payoff = "deferred" nhưng villain_counterattack/loss gây thiệt hại thật.
		- Chương 1-2 không được evidence_state = "clean" cho vụ chính và không được main_loss = "none"; nếu main thắng, chỉ thắng nhỏ.
		- Không được có quá 2 chương liên tiếp crowd_stance = "supporting"; đám đông phải chuyển phe từ từ.
		- Chương áp chót KHÔNG được dùng faceslap_payoff = "legal_collapse" nếu chương cuối cũng legal_collapse; chương áp chót dùng "authority_reversal" hoặc "evidence_reversal" để khóa đường lui.
	- Chương cuối là payoff pháp lý chính; không được lặp lại cùng beat bắt/dẫn giải đã dùng ở chương áp chót.
	` : ''}

━━━ PATCH 3: IDENTITY REVEAL GATE (bắt buộc) ━━━
Áp dụng ngưỡng lộ thân phận theo số chương:
  Tầng 1 (nghi ngờ):            Chương đầu → 25% đầu
  Tầng 2 (có chống lưng):       20% → 45%
  Tầng 3 (trung cấp biết):      40% → 65%
  Tầng 4 (lộ công khai):        Từ 60% trở đi
  Tầng 5 (đảo ngược quyền lực): Trong 25% cuối
Ghi rõ chương nào sẽ xảy ra mỗi tầng. Nếu tầng 4 xuất hiện sớm hơn 60%
→ phản diện PHẢI phản công và đẩy main vào [ROCK_BOTTOM] ngay chương tiếp.

━━━ PATCH 10: LOGIC GATE — CHỐNG LỖ HỔNG CỐT TRUYỆN (bắt buộc) ━━━

A. IDENTITY CONTINUITY: Nếu main dùng vỏ bọc (nhân viên, tài xế, v.v.) rồi bị lộ/bị đuổi → main KHÔNG THỂ quay lại cùng tổ chức với vai trò khác trừ khi:
   (1) Có thay đổi ngoại hình cụ thể (tóc, kính, râu) VÀ (2) phản diện chưa từng gặp trực tiếp main ở vai cũ, HOẶC (3) có trung gian giới thiệu và giải thích rõ tại sao phản diện không nhận ra.
   Nếu không đáp ứng → PHẢI thay đổi cốt truyện, dùng cách tiếp cận khác (ví dụ: qua đồng minh nội bộ, qua vỏ bọc hoàn toàn mới ở tổ chức liên quan).

B. VILLAIN RESPONSE PROPORTIONALITY: Khi phản diện phát hiện main là kẻ thù:
   - Phản diện có vệ sĩ/thế lực → PHẢI có phản ứng tương xứng (giữ lại, dọa, bắt giữ, phi tang bằng chứng), KHÔNG chỉ đơn thuần "đuổi đi".
   - Phản diện biết main nắm bằng chứng → PHẢI cố thu hồi/hủy bằng chứng TRƯỚC khi thả main.

C. AUTHORITY CONSISTENCY: Nếu main bị đình chỉ/mất quyền → main KHÔNG THỂ dẫn đầu hoạt động chính thức (khám xét, bắt giữ) trừ khi:
   (1) Có quyết định phục hồi chức vụ từ cấp trên cao hơn, HOẶC (2) có cơ quan khác tiếp quản vụ án.
   Ghi rõ chương nào phục hồi quyền lực và bằng cách nào.

D. NAME CROSS-CHECK: Mọi nhân vật trong Chapter Map phải dùng ĐÚNG tên trong Story Bible. TUYỆT ĐỐI CẤM 2 nhân vật khác vai trò mà cùng họ hoặc cùng tên.

E. MOTIF DIVERSITY: Không lặp cùng một sự kiện/mô-típ quá 2 lần trong toàn truyện:
   - "Phong bì/thư nặc danh đe dọa" tối đa 1 lần
   - "Gọi điện → đầu dây im lặng → rồi trả lời" tối đa 2 lần
   - "Nhìn ra cửa sổ suy tư" tối đa 1 lần
   Nếu Chapter Map cần nhiều cảnh đe dọa → PHẢI dùng hình thức khác nhau mỗi lần (tin nhắn, gặp mặt, hành động trực tiếp).

F. CORPORATE LEGAL REALISM: Nếu có HĐQT/cổ đông/cơ quan điều tra/ngân hàng/tòa án:
   - Mỗi chương pháp lý phải ghi rõ stage hiện tại: nội bộ, tố cáo, xác minh, triệu tập, niêm phong, khởi tố, xét xử.
   - Không được nhảy từ "phát hiện hóa đơn" sang "bắt người/tòa bác bằng chứng" nếu legal_process_plan chưa có bước chuẩn bị.
   - Chương có bắt giữ/khám xét/phong tỏa phải có căn cứ đã cài: đơn tố cáo, nguy cơ tiêu hủy chứng cứ, nhân chứng, hoặc lệnh/biên bản.
   - Nếu chưa đủ điều kiện, dùng "tạm đình chỉ", "đối chất nội bộ", "kiểm toán độc lập", "triệu tập làm việc" thay cho "bắt/tòa xử".

G. EVIDENCE LADDER MAPPING: Mỗi bằng chứng quyết định trong climax phải có chapter map chỉ rõ:
   - Chương gieo manh mối, chương bị phản bác, chương tìm được bản sạch, chương có xác nhận độc lập.
   - Không để 2+ bằng chứng quyết định xuất hiện lần đầu trong cùng một chương climax.
   - Nếu bằng chứng là ghi âm/ảnh chụp/tài liệu lấy lén, phải có chương phản diện hoặc luật sư challenge tính hợp pháp.

H. VIETNAM THREAT ESCALATION: Với Việt Nam hiện đại, phản diện doanh nghiệp không được mặc định dùng dao kéo/xã hội đen.
   - Ưu tiên phản công: kiện ngược, tố main ăn cắp dữ liệu, cắt lương/đuổi việc, đe dọa mẹ/con/việc làm qua quan hệ, mua chuộc nhân chứng, tung tin truyền thông, gọi kiểm toán/thuế.
	   - Nếu vẫn dùng bạo lực vật lý, phải cài trước kẻ thực thi và hậu quả pháp lý ngay chương sau.

	I. PENULTIMATE VS FINAL CLIMAX SPLIT:
	   - Chương ${Math.max(1, chapter_count - 1)} là khóa đường lui: đối chất, niêm phong, triệu tập, kiểm toán, đồng phạm lộ, hoặc quyết định nội bộ.
	   - Chương ${chapter_count} mới là cú sụp chính: bắt/áp giải/tạm giam/hậu quả pháp lý trước mắt.
	   - Không được cho cả hai chương cùng là cảnh "công an bước vào bắt Hải".

	J. CLEAN AUTHORITY DOCUMENTS:
	   - Nếu main dùng quyết định/ủy quyền/văn bản để mở quyền truy cập, field evidence_or_loss phải ghi rõ nguồn sạch: HĐQT ký thật, chữ ký điện tử xác thực, mã văn bản, luật sư xác nhận.
	   - Cấm "giấy tờ giả", "giả danh", "chữ ký giả nhưng có bản thật" dưới mọi dạng.

OUTPUT STRICT JSON ONLY:
Không Markdown, không bảng Markdown, không code fence, không lời giải thích.
Trả đúng một JSON object có key "chapters".
Field "chapters" là một JSON array có CHÍNH XÁC ${chapter_count} object. Mỗi object có schema:
{
  "chapters": [
{
  "chapter": 1,
  "title": "Tên chương, không lặp",
  "type": "BUILD | ACTION | COLLAPSE",
  "chapter_type": "BUILD | ACTION | COLLAPSE",
  "functionTag": "HUMILIATE | INVESTIGATE | EVIDENCE_FOUND | EVIDENCE_LOST | FACESLAP_SMALL | FACESLAP_BIG | VILLAIN_WINS | VILLAIN_EXPOSED | ALLY_THREATENED | IDENTITY_HINT | IDENTITY_REVEAL | ROCK_BOTTOM | BOARD_CONFLICT | LEGAL_MOVE | AFTERMATH | HOOK_ARC2",
  "identityRevealLayer": "Tầng lộ thân phận ở chương này, hoặc none",
  "opening_state": "Trạng thái đầu chương",
  "protagonist_goal": "Main muốn gì",
	  "main_obstacle": "Vật cản chính",
	  "public_stage": "Sân khấu xã hội: phòng họp/sảnh/căng tin/nhóm chat/HĐQT/họp báo/đối chất/private_pressure",
	  "humiliation_beat": "Ai làm nhục ai, bằng câu thoại/hành động gì, ai chứng kiến",
	  "villain_arrogance_line": "Một câu ngạo mạn sắc, cụ thể, có thể đưa vào chương",
		  "faceslap_payoff": "private_correction | public_embarrassment | evidence_reversal | authority_reversal | financial_reversal | public_identity_reveal | legal_collapse | deferred",
		  "witness_reaction": "Người chứng kiến phản ứng/đổi thái độ thế nào",
		  "pacing_role": "early_small_win | villain_win | clean_evidence_recovery | identity_reveal | penultimate_lock | final_collapse | aftermath",
		  "main_loss": "minor_only | danh dự/quyền truy cập/bản gốc/đồng minh/tiền/sân khấu công khai bị mất",
		  "evidence_state": "clue_only | challenged | lost_or_blocked | corroborated | clean",
		  "crowd_stance": "mocking | doubting | silent | turning | supporting",
		  "payoff_debt_repaid": "Món nợ nhục cụ thể được trả lại, hoặc deferred_debt",
		  "clean_authority_document": "Nếu có văn bản/quyền lực/HĐQT/luật sư: nguồn sạch và cách xác thực; nếu không có ghi 'none'",
	  "beats": ["Beat 1", "Beat 2", "Beat 3", "Beat 4", "Beat 5"],
  "evidence_or_loss": "Bằng chứng lấy được hoặc thứ main mất",
  "win": "Main thắng gì",
  "loss": "Main mất/hiểu sai gì",
  "foreshadowing": "Manh mối gieo",
  "human_moment": "Khoảnh khắc con người",
  "cliffhanger": "Câu hỏi/cú móc cuối chương",
  "cliffhanger_type": "mysterious_call | name_drop | threat | revelation | betrayal | evidence_found | deadline | physical_danger | emotional_blow | other — MỖI TYPE CHỈ DÙNG TỐI ĐA 2 LẦN TRONG TOÀN TRUYỆN",
  "villain_counterattack": "Phản diện phản công gì trong chương này (nếu type=ACTION hoặc FACESLAP_BIG, BẮT BUỘC phải có). Ghi 'none' nếu không áp dụng.",
  "legal_stage": "none | internal_audit | board_meeting | complaint_filed | investigation_review | summons | emergency_search | indictment | trial — không nhảy cóc stage",
  "authority_condition": "Điều kiện để HĐQT/công an/ngân hàng/tòa được can thiệp; nếu chưa đủ ghi 'not yet'",
  "threat_method": "Cách phản diện gây áp lực trong chương này; ưu tiên pháp lý/tài chính/truyền thông/nhân sự thay vì bạo lực thô",
  "evidence_introduced": "Tên bằng chứng mới xuất hiện trong chương này, hoặc 'none'",
  "evidence_ladder_level": "1 | 2 | 3 | 4 | 5 | none",
  "evidence_challenge": "Bằng chứng này bị phản bác/challenge thế nào, hoặc 'none'",
  "evidence_foreshadow_required_at": "Số chương mà bằng chứng này ĐÃ PHẢI được gieo manh mối trước đó. VD: nếu chương 7 dùng USB backup thì giá trị = 5 (phải gieo ở Ch.5). Nếu 'none' thì bỏ qua.",
  "main_wrong_assumption": "Điều main TƯỞNG ĐÚNG nhưng sẽ sai ở chương sau (bắt buộc ít nhất 3 lần trong toàn truyện). Ghi 'none' nếu không áp dụng."
}
  ]
}

Ràng buộc máy đọc:
- Field "chapter" phải chạy từ 1 đến ${chapter_count}.
- Không dùng "Chapter" viết hoa thay cho "chapter".
- Không được thiếu "beats".
- Không được để 2 chương liên tiếp cùng "functionTag".
- Nếu có IDENTITY_REVEAL công khai, chapter phải >= ceil(${chapter_count} * 0.6).`;

// ── 3. CHAPTER WRITER ─────────────────────────────────────────────────────────
export interface ChapterWriterParams {
  story_bible: string;
  chapter_map: string;
  chapter_number: number;
  chapter_title: string;
  chapter_type: string;
  chapter_beats: string;
  previous_summary: string;
  current_state: string;
}

export const getChapterWriterPrompt = (p: ChapterWriterParams) => `\
Bạn là CHAPTER WRITER cho truyện mạng Zhihu / micro-drama Việt Nam.

BẮT BUỘC viết truyện bằng tiếng Việt tự nhiên, đúng xưng hô và văn phong truyện mạng Việt Nam.
CHỈ VIẾT đúng chương được giao.
Không thay đổi tên, con số, dòng thời gian hay vai trò nhân vật.
Không thêm twist mới ngoài Chapter Map.
Không giải quyết sớm các tình tiết của chương sau.

⚠️ QUY TẮC POV BẮT BUỘC:
- Đọc POV_MODE trong Story Bible trước khi viết.
- Nếu POV_MODE = third_person: LUÔN dùng ngôi thứ ba ("[Tên nhân vật] nhìn...", "Cô ta..."). CẤM TUYỆT ĐỐI dùng "Tôi" hay "tao".
- Nếu POV_MODE = first_person: LUÔN dùng ngôi thứ nhất ("Tôi nhìn..."). CẤM TUYỆT ĐỐI dùng tên nhân vật làm chủ ngữ.
- Viết tiêu đề chương đúng số và tên ở phần [CURRENT CHAPTER]. Không bao giờ tự đổi thành chương khác.

⚠️ QUY TẮC FORESHADOW BẮT BUỘC:
- Nếu chương này gieo manh mối cho twist, phải cập nhật rõ trong STATE UPDATE JSON mục "foreshadowingPlanted".
- Manh mối phải tinh tế: một câu thoại bình thường, một chi tiết nhỏ, hoặc hành động vô tình — KHÔNG phải lời nhắc trực tiếp.
- KHÔNG được có twist lớn nào ở chương cuối mà không có ít nhất 3 manh mối từ chương 1-10.

━━━ PATCH 7: PRE-WRITE EVIDENCE GATE (bắt buộc) ━━━
TRƯỚC KHI VIẾT, đọc Chapter Map cho chương hiện tại:
1. Nếu chapter_map[N].evidence_introduced !== 'none':
   → Kiểm tra chapter_map[N].evidence_foreshadow_required_at = M
   → Kiểm tra trong currentState.foreshadowingPlanted[] xem có manh mối nào đã gieo ở chương M không
   → NẾU KHÔNG CÓ và N > M: KHÔNG ĐƯỢC dùng bằng chứng đó để thắng/payoff trong chương này. PHẢI đổi sang bằng chứng đã có foreshadow, hoặc hạ nó thành manh mối yếu và đẩy payoff sang chương sau.
   → NẾU KHÔNG CÓ và N <= M: chỉ được gieo manh mối, chưa được dùng nó như bằng chứng kết liễu.
   → TUYỆT ĐỐI CẤM đưa bằng chứng mới lần đầu tiên trong cảnh hội trường/đối chất/climax mà chưa được nhắc ở chương trước

2. Nếu chương hiện tại có nhân vật mới cung cấp thông tin quan trọng:
   → Nhân vật đó PHẢI đã được nhắc tên hoặc vai trò ở ít nhất 1 chương trước
   → Nếu chưa → PHẢI thêm 1-2 câu giới thiệu gián tiếp (ai đó nhắc đến, biển hiệu, email CC)

━━━ PATCH 8: CLIFFHANGER DIVERSITY TRACKER (bắt buộc) ━━━
Đọc danh sách cliffhanger_type đã dùng ở các chương trước (từ chapter_map hoặc currentState):
- NẾU cliffhanger_type dự kiến cho chương này TRÙNG với chương N-1 hoặc N-2 → PHẢI đổi sang type khác
- NẾU cùng một cliffhanger_type đã dùng 2 lần trong toàn truyện → CẤM dùng lại
- CẤM kết chương bằng: "cuộc chiến chưa kết thúc", "cuộc chơi mới bắt đầu", hoặc bất kỳ biến thể nào (đã nằm trong BANNED PHRASES)
- Mỗi cliffhanger phải tạo CÂU HỎI CỤ THỂ mà người đọc muốn biết đáp án, không phải cảm xúc chung chung

Ví dụ cliffhanger TỐT (câu hỏi cụ thể):
- "Trong điện thoại Hùng có 1 cuộc gọi lúc 2 giờ sáng — đầu dây bên kia là số nội bộ của... chính phòng cô." (→ ai gọi? tại sao?)
- "Lan đặt tờ giấy lên bàn: 'Tôi biết cô không phải Nguyễn Thị Hoa.'" (→ Lan biết từ đâu? sẽ làm gì?)

Ví dụ cliffhanger XẤU (cảm xúc rỗng):
- "Cô siết chặt nắm tay. Cuộc chiến chỉ mới bắt đầu." (→ không có câu hỏi, không có thông tin mới)

━━━ PATCH 12: CORPORATE LEGAL + EVIDENCE GATE (bắt buộc) ━━━
Trước khi viết chương, kiểm tra Story Bible + Chapter Map:
1. Nếu chương có main ẩn thân trong công ty:
   → Phải giữ lý do không bị nhận ra nhất quán với "undercover_plausibility".
   → Nếu chương cho phản diện phát hiện thân phận, phải viết cơ chế phát hiện cụ thể, không chỉ "hắn Google thấy".

2. Nếu chương có công an/tòa/ngân hàng/HĐQT can thiệp:
   → Kiểm tra "legal_stage" và "authority_condition".
   → Nếu legal_stage chưa đủ điều kiện, KHÔNG được viết bắt giữ/khám xét/phong tỏa/tòa bác chứng cứ.
   → Thay bằng hành động đúng stage: kiểm toán, đối chất, tạm đình chỉ, triệu tập, niêm phong, hoặc nộp đơn.

3. Nếu chương dùng bằng chứng để lật kèo:
   → Kiểm tra "evidence_ladder_level".
   → Level 1-2 chỉ là manh mối/dấu hiệu, KHÔNG đủ thắng.
   → Level 3 phải bị phản bác hoặc có rủi ro pháp lý.
   → Level 4-5 mới được dùng ở climax, nhưng phải có nguồn và xác nhận độc lập.

	4. Nếu setting là Việt Nam hiện đại và chương có bạo lực vật lý:
	   → Chỉ viết khi Chapter Map đã cài "threat_method" phù hợp.
	   → Phải thêm hậu quả: hồ sơ y tế, camera, nhân chứng, công an truy tìm, hoặc phản diện phải trả giá.
	   → Nếu không, đổi bạo lực thành phản công pháp lý/tài chính/truyền thông/nhân sự.

	5. Nếu Story Bible/Chapter Map thuộc Đô Thị Vả Mặt:
	   → Chương PHẢI có ít nhất 1 cảnh áp lực địa vị hoặc nhục nhã cụ thể, bám "humiliation_beat".
	   → Nếu "faceslap_payoff" khác "deferred", chương PHẢI viết đủ micro-rhythm: sân khấu → miệt thị → main nén → lật từng nấc → phản diện phủ nhận → khóa đường lui → dư chấn.
	   → Nếu "faceslap_payoff" = "deferred", chương PHẢI tăng cảm giác ức chế và kết bằng một câu hỏi cụ thể, không được chỉ điều tra khô.
	   → Phải đưa "villain_arrogance_line" vào đối thoại hoặc biến thể gần nghĩa của nó.
	   → Phải có "witness_reaction": ít nhất một người chứng kiến đổi thái độ, im bặt, né mắt, hoặc bắt đầu nghi ngờ phản diện.
	   → Phải thể hiện "crowd_stance" đúng bậc: mocking/doubting/silent/turning/supporting. Không được nhảy thẳng từ mocking sang supporting trong cùng một chương.
	   → Phải thể hiện "evidence_state": clue_only không được thắng lớn; challenged phải có phản bác thật; lost_or_blocked phải làm main mất đường công khai; clean mới được dùng để khóa đường lui.
	   → Nếu có "payoff_debt_repaid", cú vả mặt phải trả đúng món nợ nhục đó bằng cảnh cụ thể, không chỉ đọc bằng chứng chung chung.
	   → Nếu pacing_role = "villain_win", chương KHÔNG được cho main thắng ngược trong cùng cảnh; main phải mất thứ thật và chỉ giữ lại một manh mối nhỏ.
	   → Nếu pacing_role = "penultimate_lock", chỉ được viết đối chất/niêm phong/triệu tập/khóa đường lui. KHÔNG bắt người, KHÔNG tuyên án.
	   → Nếu pacing_role = "final_collapse", mới được viết quyết định bắt/áp giải/tạm giam/hậu quả pháp lý chính, và phải khác beat với chương áp chót.
	   → Nếu có clean_authority_document khác "none", văn bản phải là sạch và xác thực được; tuyệt đối không dùng giấy giả/chữ ký giả/giả danh.
	   → Thoại sỉ nhục phải sắc kiểu công sở. Cấm lặp chửi thô; nếu dùng câu thô, chỉ dùng một lần và đổi phần còn lại thành mỉa mai lạnh.

	KHÔNG được in checklist, PRE-WRITE DECLARATION, Self-Check, Change Log, Audit Report, hoặc lời giải thích trước/sau chương.

INPUT CỐ ĐỊNH, ĐẶT TRƯỚC ĐỂ TẬN DỤNG DEEPSEEK CONTEXT CACHE:
[STORY BIBLE]
${p.story_bible}

[CHAPTER MAP]
${p.chapter_map}

[CURRENT STATE LOCK]
${p.current_state}

[PREVIOUS CHAPTER SUMMARY]
${p.previous_summary}

[CURRENT CHAPTER]
Chapter number: ${p.chapter_number}
Title: ${p.chapter_title}
Type: ${p.chapter_type}
	Current chapter contract (beats + legal/evidence locks):
	${p.chapter_beats}

	ĐÔ THỊ VẢ MẶT STYLE LOCK:
	- Nếu chapter contract có public_stage/humiliation_beat/faceslap_payoff/witness_reaction, phải viết chúng thành cảnh thật, không tóm tắt.
	- Tỉ lệ chương nên có nhiều thoại đối đầu, câu ngắn, phản ứng đám đông, chi tiết công sở/đô thị cụ thể.
	- Main không được "ngầu im lặng" quá lâu nếu cảnh cần payoff; main phải phản đòn bằng hành động/bằng chứng có trình tự.
	- Tránh giọng báo cáo điều tra. Mọi bằng chứng phải đi qua xung đột người-với-người.
	- Giữa truyện phải để phản diện thắng thật khi chapter contract yêu cầu; đừng tự cứu main bằng một cuộc gọi hoặc bằng chứng backup.

	━━━ PATCH 5: TITLE GUARD (kiểm tra bắt buộc) ━━━
	Dòng đầu tiên của output PHẢI LÀ: Chương ${p.chapter_number}: ${p.chapter_title}
	Tiếp theo là: [TEASER SEO]: ...
TUYỆT ĐỐI CẤM:
  × Lặp lại dòng tiêu đề bất kỳ lần nào nữa
  × Thêm # hoặc ## trước tiêu đề
  × Có chuỗi "Chương X:" nào khác bên trong nội dung truyện
	Sau khi viết xong, QUÉT LẠI toàn bộ output — nếu phát hiện tiêu đề lặp → XÓA BẢN LẶP trước khi trả kết quả.

	━━━ PATCH 13: STATE MEMORY FLAGS (bắt buộc) ━━━
	Sau khi viết chương, cập nhật STATE UPDATE JSON như sau:
	- Nếu chương có lộ thân phận công khai/tầng 4: set publicIdentityKnown=true, revealedAtChapter=${p.chapter_number}, lastMajorSetPiece="identity_reveal".
	- Nếu chương có bố/luật sư/công an/đội an ninh/cơ quan chức năng giải cứu main: set lastMajorSetPiece="rescue" và lastRescueMechanism ghi cơ chế cụ thể.
	- Nếu chương có bắt/áp giải/tạm giam phản diện: set villainArrested=tên phản diện bị bắt và lastMajorSetPiece="arrest".
	- Nếu chương chỉ xử lý hậu quả sau climax: set lastMajorSetPiece="aftermath".
	- Nếu mở arc mới: set arcPhase="arc2_hook"; chỉ thêm 1 hook vào arc2Hooks, không mở nhiều phe mới.
	- Nếu currentState đã có publicIdentityKnown=true hoặc villainArrested khác rỗng, phải giữ nguyên/cập nhật tiếp, không xóa về false/rỗng.

	${STATEFUL_WRITER_RULES}

${isFaceSlapStr(p.story_bible) ? getFaceSlapOverride() : ''}

OUTPUT CONTRACT V1 — TUÂN THỦ TUYỆT ĐỐI:
- Không dùng markdown heading (#, ##).
- Không bọc JSON trong \`\`\`json.
- Không viết bất kỳ lời giải thích nào trước dòng tiêu đề hoặc sau dấu } cuối cùng.
- Dòng tiêu đề chỉ xuất hiện đúng 1 lần.
- Trong phần nội dung truyện, cấm xuất hiện chuỗi "Chương ${p.chapter_number}:" hoặc bất kỳ "Chương X:" nào khác.

Output:
Chương ${p.chapter_number}: ${p.chapter_title}

[TEASER SEO]: Viết 30–40 chữ tiếng Việt giật gân, tóm tắt sự kịch tính của chương để câu khách.

<Nội dung chương truyện (Chapter content)>

STATE UPDATE JSON:
{
  "schemaVersion": "StoryStateV1",
  "chapterNumber": "",
	  "chapterTitle": "",
	  "chapterFunction": "",
	  "identityRevealLayer": "",
	  "publicIdentityKnown": false,
	  "revealedAtChapter": 0,
	  "villainArrested": "",
	  "lastMajorSetPiece": "",
	  "lastRescueMechanism": "",
	  "arcPhase": "arc1",
		  "legalStage": "",
		  "authorityCondition": "",
		  "threatMethod": "",
		  "evidenceLadderLevel": "",
		  "evidenceChallenge": "",
		  "publicStage": "",
		  "humiliationBeat": "",
		  "faceslapPayoff": "",
		  "witnessReaction": "",
		  "villainArroganceLine": "",
		  "pacingRole": "",
		  "cleanAuthorityDocument": "",
		  "characterMap": {
    "main": "",
    "villain_main": "",
    "ally_primary": "",
    "vip_customer": "",
    "company_name": ""
  },
  "PATCH4_fixedNumbers": {
    "_note": "SAO CHÉP NGUYÊN VẸN từ chương trước. KHÔNG ĐỔI bất kỳ giá trị đã khóa.",
    "corruptionAmount": "",
    "contractValues": [],
    "companyCapitals": [],
    "keyDates": {
      "crimeStartDate": "",
      "investigationStart": ""
    },
    "lockedAfterChapter": 1
  },
  "fixedFacts": {
    "characterRoles": [],
    "companyNames": [],
    "evidenceNames": [],
    "legalStatuses": []
  },
  "mainKnows": [],
  "mainHas": [],
  "mainLost": [],
  "villainKnows": [],
  "villainHas": [],
  "villainLost": [],
  "validEvidence": [
    {
      "name": "",
      "source": "",
      "cost": "",
      "legalRisk": "",
      "nonDigitalCorroboration": "",
      "canBeAttackedHow": "",
      "isEnoughToWinAlone": false
    }
  ],
  "lostEvidence": [],
  "activeAllies": [],
  "disabledAllies": [],
  "openThreads": [],
	  "resolvedThreads": [],
	  "arc2Hooks": [],
	  "usedFaceslapPayoffs": [],
	  "usedPublicStages": [],
	  "humiliationDebt": "",
	  "continuityWarnings": [],
  "nextChapterPressure": "",
  "foreshadowingPlanted": []
}

STATE UPDATE JSON phải parse được bằng JSON.parse sau khi cắt từ dấu { đầu tiên đến dấu } cuối cùng.
Sau dấu } cuối cùng của STATE UPDATE JSON, KHÔNG viết thêm bất kỳ chữ nào.`;

// ── 4. IRON RULES CHECKER ─────────────────────────────────────────────────────
export interface IronRulesCheckerParams {
  story_bible: string;
  chapter_map: string;
  previous_state: string;
  chapter_draft: string;
  chapter_number: number;
  custom_iron_rules?: string;
}

export const getIronRulesCheckerPrompt = (p: IronRulesCheckerParams) => `\
Bạn là IRON RULES CHECKER cho truyện mạng Zhihu / micro-drama Việt Nam.

BẮT BUỘC trả lời bằng tiếng Việt tự nhiên, nhưng giữ nguyên các nhãn máy đọc (machine-readable labels) bằng tiếng Anh.
KHÔNG viết lại toàn bộ chương.
Hãy chấm điểm và rà soát bản nháp chương (chapter draft) dựa trên Story Bible, Chapter Map, Previous State, và Iron Rules.

[DEFAULT IRON RULES — CHECKER_RULES_FULL]
${CHECKER_RULES_FULL}
${p.custom_iron_rules ? '\n[CUSTOM IRON RULES]\n' + p.custom_iron_rules : ''}

${isFaceSlapStr(p.story_bible) ? getFaceSlapOverride() : ''}

INPUT:
[STORY BIBLE]
${p.story_bible}

[CHAPTER MAP]
${p.chapter_map}

[PREVIOUS STATE]
${p.previous_state}

[CHAPTER DRAFT]
${p.chapter_draft}

	P0 Critical (Lỗi nghiêm trọng):
- Sai tên nhân vật (Wrong character name).
- Sai số liệu/dòng thời gian (Wrong number/timeline).
- Lặp lại cảnh cũ (Duplicate scene).
- Backup thần kỳ (Instant backup).
- Cứu viện từ trên trời rơi xuống (Deus ex rescue).
- Twist mồ côi không manh mối (Orphan twist).
- NVC tự dưng biết thông tin không qua điều tra (Protagonist knows unearned information).
- Phản diện tự dưng biết kế hoạch bí mật (Villain knows secret plan without mechanism).
	- Chương không làm thay đổi trạng thái câu chuyện (Chapter does not change story state).
	- Có chứa cụm từ bị cấm (Banned phrase).
		- Với Đô Thị Vả Mặt: chương có faceslap_payoff khác "deferred" nhưng thiếu sân khấu, thiếu người chứng kiến, thiếu phản diện phủ nhận, hoặc thiếu hậu quả thấy ngay.
		- Với Đô Thị Vả Mặt: chapter contract ghi pacing_role = "villain_win" nhưng chương lại cho main thắng ngược/thoát sạch ngay trong cùng cảnh.
		- Với Đô Thị Vả Mặt: chương 1-2 đưa bằng chứng clean/all-in có thể hạ vụ chính ngay, hoặc main giữ USB/video/ghi âm giải quyết mọi nút thắt từ đầu.
		- Với Đô Thị Vả Mặt: 3 chương liên tiếp dùng cùng công thức livestream/video/ghi âm để vả mặt, không có hình thức payoff mới.
		- Với Đô Thị Vả Mặt: crowd_stance nhảy từ mocking sang supporting quá nhanh mà không qua doubt/silence/turning.
		- Với Đô Thị Vả Mặt: faceslap_payoff không trả lại một humiliation debt cụ thể đã gieo trước đó.
		- Chương áp chót và chương cuối lặp cùng một climax pháp lý: cùng bắt người/dẫn giải/tạm giam hai lần.
	- Main dùng giấy tờ giả, chữ ký giả, giả danh, hoặc văn bản không có nguồn xác thực để mở quyền lực.
	- Dùng "bản án", "tuyên án", "kết tội tại tòa" khi Story Bible/Chapter Map chưa có phiên tòa thật.

	P1 Major (Lỗi cấu trúc):
- NVC thắng quá dễ dàng (Protagonist wins too easily).
- Phản diện hành xử ngu ngốc (Villain acts stupid).
- Đồng minh đưa thông tin không rõ nguồn gốc (Ally gives information with no source).
- Hành vi phi pháp/vùng xám không có hậu quả (Gray legal/moral action has no consequence).
- Lời thoại không khớp thân phận/tuổi tác (Dialogue does not match role/age).
- Cliffhanger yếu (Weak cliffhanger).
- Kể cảm xúc thay vì tả (Telling emotion instead of showing).

P2 Style (Lỗi văn phong):
- Đoạn văn quá dài (Long paragraph).
- Câu quá dài (Long sentence).
- Tả cảnh lê thê (Excessive scenery).
- Lặp lại cấu trúc "lật bài" (Repeated structure).
- SEO Teaser yếu (Weak teaser).

OUTPUT JSON CONTRACT — ƯU TIÊN CAO NHẤT:
Bỏ qua mọi format markdown trong CHECKER_RULES_FULL nếu có xung đột. Chỉ trả về JSON hợp lệ, không markdown fence, không lời giải thích.

Schema bắt buộc:
{
  "chapter_number": ${p.chapter_number},
  "score": 0,
  "verdict": "PASS_WITH_PATCHES",
  "p0": [
    { "issue": "", "evidence": "", "fix": "" }
  ],
  "p1": [
    { "issue": "", "evidence": "", "fix": "" }
  ],
  "p2": [
    { "issue": "", "evidence": "", "fix": "" }
  ],
  "errors": [],
  "patch_notes": "",
  "name_data_consistency": "",
  "logic_check": "",
  "pacing_check": "",
  "cliffhanger_check": ""
}

Quy tắc verdict:
- Field "verdict" chỉ được là một trong ba giá trị: "PASS", "PASS_WITH_PATCHES", "REWRITE_REQUIRED".
- PASS: score >= 9.2 và không có P0/P1 cần sửa.
- PASS_WITH_PATCHES: score >= 8.2, không có P0, nhưng còn P1/P2 hoặc cần polish để đạt mức xuất bản.
- REWRITE_REQUIRED: có bất kỳ P0 nào, sai format output, sai số chương, thiếu JSON state, lộ meta, hoặc score < 8.2.
- Nếu chương đọc được nhưng còn tiện, lỏng logic pháp lý, bằng chứng chưa đủ giá phải trả, phản diện yếu, hoặc cảm xúc nhân vật mỏng thì KHÔNG được cho PASS dù văn phong trôi.`;

// ── 5. CHAPTER REWRITER ───────────────────────────────────────────────────────
export interface ChapterRewriterParams {
  chapter_draft: string;
  audit_report: string;
  story_bible: string;
  current_state: string;
}

export const getChapterRewriterPrompt = (p: ChapterRewriterParams) => `\
Bạn là CHAPTER REWRITER.

BẮT BUỘC viết truyện bằng tiếng Việt tự nhiên, đúng xưng hô và văn phong truyện mạng Việt Nam.
Chỉnh sửa lại bản nháp chương dựa trên Audit Report.
Giữ lại những đoạn tốt.
Không thay đổi Story Bible.
Không thay đổi Chapter Map.
Không thêm twist mới.
Không đổi tên hoặc con số.
Không làm chương dài ra quá 15%.
Không thay đổi outcome, bằng chứng, trạng thái nhân vật, thứ main biết/mất/có, hoặc cliffhanger đã có trong bản nháp trừ khi Audit Report yêu cầu trực tiếp.
Nếu Audit Report yêu cầu sửa logic có thể làm đổi state, hãy sửa theo hướng KHỚP với CURRENT STATE thay vì tạo state mới.
Nếu Audit Report đánh lỗi P0/P1 về pháp lý, chuỗi bằng chứng, lộ thân phận, bạo lực quá lố, hoặc phản diện ngu, được phép chỉnh cơ chế cảnh trong phạm vi cùng mục tiêu chương: hạ bằng chứng xuống manh mối, đổi bắt giữ thành đối chất/niêm phong/triệu tập, thêm cái giá phải trả, hoặc chuyển đòn bạo lực thành đòn pháp lý/tài chính. Không cần giữ nguyên cách cảnh cũ vận hành nếu cách đó là lỗi.

${isFaceSlapStr(p.story_bible) ? getFaceSlapOverride() : ''}

INPUT:
[CHAPTER DRAFT]
${p.chapter_draft}

[IRON RULES AUDIT]
${p.audit_report}

[STORY BIBLE]
${p.story_bible}

[CURRENT STATE]
${p.current_state}

Output:
Chỉ trả về chương đã sửa.
Bắt đầu bằng đúng tiêu đề chương nếu bản nháp có tiêu đề, sau đó là [TEASER SEO] và nội dung truyện.
KHÔNG trả Change Log.
KHÔNG trả Updated Self-Check.
KHÔNG trả STATE UPDATE JSON.
KHÔNG thêm bằng chứng mới, nhân vật mới, twist mới, hay trạng thái mới không có trong bản nháp/CURRENT STATE.`;

// ── 6. FINAL AUDIT ───────────────────────────────────────────────────────────────
export interface FinalAuditParams {
  story_bible: string;
  chapter_map: string;
  all_chapters: string;
  current_state: string;
  audit_reports: string;
  custom_iron_rules?: string;
}

export const getFinalAuditPrompt = (p: FinalAuditParams) => `\
Bạn là SUPREME EDITOR (Biên tập viên tối cao) cho truyện mạng Zhihu / micro-drama Việt Nam.
Nhiệm vụ của bạn là thực hiện Final Audit (Kiểm duyệt tổng thể) toàn bộ câu chuyện trước khi xuất bản.

BẮT BUỘC trả lời bằng tiếng Việt tự nhiên, nhưng giữ nguyên các nhãn máy đọc (machine-readable labels) bằng tiếng Anh.

[FINAL AUDIT RULES — FINAL_AUDIT_RULES]
${FINAL_AUDIT_RULES}
${p.custom_iron_rules ? '\n[CUSTOM IRON RULES]\n' + p.custom_iron_rules : ''}

${isFaceSlapStr(p.story_bible) ? getFaceSlapOverride() : ''}

INPUT:
[STORY BIBLE]
${p.story_bible}

[CHAPTER MAP]
${p.chapter_map}

[ALL CHAPTERS]
${p.all_chapters}

[CURRENT STATE]
${p.current_state}

[AUDIT REPORTS]
${p.audit_reports}

Yêu cầu (Requirements):
Kiểm tra toàn bộ truyện để tìm các lỗi:
1. Tính nhất quán tên gọi (Name consistency - Tên nhân vật có đúng từ đầu tới cuối không?)
2. Tính nhất quán số liệu (Number consistency - Nợ, ngày tháng, tuổi tác, mã số bằng chứng)
3. Tuyến truyện chưa giải quyết (Unresolved plot threads)
4. Lặp lại cảnh cũ (Duplicate scenes)
5. Kết thúc yếu/lửng lơ (Weak ending / No Cliffhanger at finale)
6. Twist mồ côi (Orphan twists - Không có manh mối báo trước)
7. Backup thần kỳ (Instant backup - Giải quyết bằng công nghệ/bản copy phi lý)
8. Cứu viện từ trên trời rơi xuống (Deus ex rescue)
9. Trừng phạt phản diện có trực tiếp không (Villain punishment shown directly - Cấm xử lý off-screen)
10. Số phận nhân vật phụ quan trọng (Side character arcs closed)
11. Chương cuối đã giải quyết xong vụ án/mục tiêu chính (Finale resolves main case)
12. Các cụm từ bị cấm / văn phong sáo rỗng (Banned phrases)
13. Từng chương có đi theo đúng Type đã lên kế hoạch không (ACTION/BUILD/COLLAPSE)

QUALITY BAR:
- READY_TO_EXPORT chỉ được dùng khi Score >= 9.2/10 và không còn Critical/Major Issue.
- NEEDS_PATCHES nếu Score từ 8.0 đến 9.19 hoặc còn lỗi cảm xúc/logic/bằng chứng có thể sửa cục bộ.
- REWRITE_ENDING nếu finale, chuỗi bằng chứng, hoặc legal climax sai gốc dù văn phong ổn.
- Không chấm nương tay vì truyện "đủ dài"; phải đánh vào trải nghiệm đọc, logic, payoff, và độ đáng tin.

## FINAL AUDIT ADD-ON v2.1
Ngoài checklist cơ bản ở trên, bắt buộc kiểm tra thêm 7 điểm sau. Nếu bất kỳ điểm nào FAIL, xuất PATCH PLAN trước khi viết lại:

**Điểm 1 — Tiêu đề chương trùng lặp (Duplicate Chapter Titles)**
- Có chương nào xuất hiện hai tiêu đề không?
- Có chương nào vô tình ghi "Chương 1" bên trong nội dung khi thực tế là chương khác không?
→ Nếu FAIL: Xuất danh sách chương bị sai, ghi đúng số thứ tự phải là bao nhiêu.

**Điểm 2 — Drift dòng thời gian (Timeline Drift)**
- Ngày tháng hợp đồng có nhất quán không?
- Ngày tháng file/tài liệu có nhất quán không?
- Ngày tòa xử có nhất quán không?
- Tuổi nhân vật và thời gian quan hệ giữa các nhân vật có nhất quán không?
→ Nếu FAIL: Xuất bảng timeline so sánh chương phát sinh mâu thuẫn.

**Điểm 3 — Chi phí bằng chứng (Evidence Cost)**
- Mỗi bằng chứng quan trọng có tốn một cái giá thực sự (thời gian, rủi ro, hi sinh) không?
- Có bằng chứng nào xuất hiện quá thuận tiện (không cần nỗ lực, không có hậu quả) không?
→ Nếu FAIL: Liệt kê bằng chứng "free", đề xuất cái giá phải trả tương xứng.

**Điểm 4 — Sức kháng cự của phản diện (Villain Resistance)**
- Sau mỗi lần nhân vật chính có được lợi thế, phản diện có phản công không?
- Phản diện có dùng ít nhất 3 trong số: luật pháp, truyền thông, cảm xúc, đồng minh, bằng chứng giả không?
→ Nếu FAIL: Chỉ ra chương nào phản diện ngồi yên, đề xuất phản công cụ thể.

**Điểm 5 — Chạm đáy thực sự (Rock Bottom)**
- Nhân vật chính có ít nhất một thời điểm hoàn toàn mất kiểm soát không?
- Có khoảnh khắc cô ấy không có giải pháp rõ ràng không?
→ Nếu FAIL: Xác định chương phù hợp để đào sâu thêm cảm giác tuyệt vọng.

**Điểm 6 — Đóng kết tuyến truyện (Thread Closure)**
- Toàn bộ openThreads đã được giải quyết, chuyển hóa, hoặc cố ý để ngỏ thành hook Season 2 chưa?
- Có nhật ký, USB, ghi âm, nhân chứng, bí mật nào không được dùng đến không?
→ Nếu FAIL: Liệt kê từng thread còn treo lơ lửng và đề xuất đóng hoặc chuyển thành hook.

**Điểm 7 — Payoff cảm xúc (Emotional Payoff)**
- Quyết định cuối cùng của nhân vật chính đến từ sự trưởng thành của nhân vật, hay chỉ là giải pháp tình tiết tiện lợi?
- Kết thúc có mang lại catharsis thực sự cho độc giả không?
→ Nếu FAIL: Ghi rõ quyết định nào cần được xây dựng lại từ nội tâm nhân vật.

---
Nếu có bất kỳ điểm FAIL nào, xuất theo format:
PATCH PLAN:
- Problem: [Mô tả vấn đề cụ thể]
- Chapter affected: [Số chương bị ảnh hưởng]
- Why it weakens the story: [Lý do nó làm yếu câu chuyện]
- Fix: [Cách sửa cụ thể, có thể áp dụng ngay]

Output MUST exactly follow this structure:
# FINAL STORY AUDIT

## Score
[Điểm trên 10] /10

## Critical Issues
[Danh sách lỗi nghiêm trọng]

## Major Issues
[Danh sách lỗi lớn]

## Minor Issues
[Danh sách lỗi nhỏ]

## Name & Data Consistency
[Phân tích tính nhất quán]

## Unresolved Threads
[Các tuyến truyện chưa đóng]

## Chapter Type Accuracy
[Phân tích cấu trúc chương Hành động / Xây dựng / Sụp đổ]

## Ending Satisfaction
[Phân tích mức độ thỏa mãn của kết truyện - Catharsis]

## ADD-ON v2.1 Results
### 1. Duplicate Titles: [PASS / FAIL]
[Chi tiết]
### 2. Timeline Drift: [PASS / FAIL]
[Chi tiết — Bảng timeline nếu có mâu thuẫn]
### 3. Evidence Cost: [PASS / FAIL]
[Chi tiết]
### 4. Villain Resistance: [PASS / FAIL]
[Chi tiết]
### 5. Rock Bottom: [PASS / FAIL]
[Chi tiết]
### 6. Thread Closure: [PASS / FAIL]
[Chi tiết — Danh sách thread còn mở]
### 7. Emotional Payoff: [PASS / FAIL]
[Chi tiết]

## Patch Plan (nếu có FAIL)
[Danh sách PATCH PLAN theo format trên]

## Required Fixes
[Danh sách các bước cần sửa chữa, ưu tiên theo P0 → P1 → P2]

## Final Verdict

Chọn ĐÚNG MỘT trong các nhãn sau (Choose exactly one of the following):
- READY_TO_EXPORT
- NEEDS_PATCHES
- REWRITE_ENDING`;

// ─────────────────────────────────────────────────────────────────────────────
// PROMPT DISPATCHER
// Selects the correct system prompt based on taskType.
// Returns null if taskType is missing/unknown → caller should use its own default.
// ─────────────────────────────────────────────────────────────────────────────

export type TaskType =
  | 'story_bible'
  | 'chapter_map'
  | 'chapter_writer'
  | 'chapter_rewriter'
  | 'iron_rules_checker'
  | 'final_audit'
  | 'format_export';

export type PromptParams =
  | ({ taskType: 'story_bible' } & StoryBibleParams)
  | { taskType: 'chapter_map'; story_bible: string; chapter_count: number }
  | ({ taskType: 'chapter_writer' } & ChapterWriterParams)
  | ({ taskType: 'chapter_rewriter' } & ChapterRewriterParams)
  | ({ taskType: 'iron_rules_checker' } & IronRulesCheckerParams)
  | ({ taskType: 'final_audit' } & FinalAuditParams)
  | { taskType: 'format_export' };

/**
 * Returns the system prompt string for a given taskType.
 * Returns null for unknown/missing taskType — caller falls back to its own default.
 */
export function selectPrompt(params: PromptParams): string | null {
  switch (params.taskType) {
    case 'story_bible':
      return getStoryBiblePrompt(params);

    case 'chapter_map':
      return getChapterMapPrompt(params.story_bible, params.chapter_count);

    case 'chapter_writer':
      return getChapterWriterPrompt(params);

    case 'chapter_rewriter':
      return getChapterRewriterPrompt(params);

    case 'iron_rules_checker':
      return getIronRulesCheckerPrompt(params);

    case 'final_audit':
      return getFinalAuditPrompt(params);

    default:
      return null; // caller uses its own default
  }
}
