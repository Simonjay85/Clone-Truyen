#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
write_batch_sangvan_02.py — Batch 2: 4 Truyện Sảng Văn (Stories 5-8)
=====================================================================
Story 5: Tiến sĩ vật liệu nano bị trục xuất (cover 39)
Story 6: Nữ kiểm toán viên bị gạt khỏi HĐQT (cover 40)
Story 7: Nhạc trưởng bị đuổi khỏi dàn nhạc (cover 41)
Story 8: Kỹ sư địa chất bị cướp mỏ (cover 42)
"""

import json, os, sys, re, time, random, subprocess, ftplib, requests

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"
WP_URL = "https://doctieuthuyet.com"
SECRET_TOKEN = "ZEN_TRUYEN_2026_BYPASS"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def log(msg):
    print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)

def split_sentences(text):
    t = re.sub(r'\s+', ' ', text).strip()
    abbrevs = ["TS.", "BS.", "PGS.", "GS.", "CEO.", "CFO.", "CTO.", "Dr.", "Mr.", "Mrs.", "Ph.D.", "HĐQT.", "IPO."]
    for i, a in enumerate(abbrevs):
        t = t.replace(a, f"__A{i}__")
    t = re.sub(r'([.!?]["\'\"]?)\s+(?=[A-ZÀÁẠẢÃÂẦẤẬẨẪĂẰẮẶẲẴÈÉẸẺẼÊỀẾỆỂỄĐÌÍỊỈĨÒÓỌỎÕÔỒỐỘỔỖƠỜỚỢỞỠÙÚỤỦŨƯỪỨỰỬỮỲÝỴỶỸ"\'\"\d])', r'\1‖', t)
    for i, a in enumerate(abbrevs):
        t = t.replace(f"__A{i}__", a)
    return [s.strip() for s in t.split("‖") if s.strip()]

def fmt(raw):
    clean = re.sub(r'<[^>]+>', ' ', raw)
    return "\n".join(f"<p>{s}</p>" for s in split_sentences(clean)) + "\n"

# ═══════════════════════════════════════════════════════════════════════════════
# STORY 5: TIẾN SĨ VẬT LIỆU NANO
# ═══════════════════════════════════════════════════════════════════════════════

S5_TITLE = "BỊ TRỤC XUẤT KHỎI PHÒNG THÍ NGHIỆM, TÔI MANG BẰNG SÁNG CHẾ VẬT LIỆU MỚI KHIẾN CẢ NGÀNH CHẤN ĐỘNG"
S5_AUTHOR = "Võ Đức Trung"
S5_COVER = "base_cover_39.png"
S5_INTRO = """<p><strong>"Mười năm nghiên cứu, hai nghìn giờ trong phòng thí nghiệm, tôi phát minh ra vật liệu nano tự phục hồi đầu tiên trên thế giới. Đổi lại, giáo sư hướng dẫn cướp bằng sáng chế, đuổi tôi khỏi viện nghiên cứu giữa đêm."</strong></p>
<p>Võ Đức Trung, Tiến sĩ vật liệu nano tài năng nhất Viện Khoa học Vật liệu Việt Nam, bị GS.TS Bùi Quốc Đạt và nghiên cứu sinh Lê Thanh Tùng phản bội, cướp trắng bằng sáng chế công trình đột phá về vật liệu composite tự phục hồi.</p>
<p>Mất phòng lab, mất bằng sáng chế, Trung được nhà đầu tư công nghệ Hàn Quốc Park Ji-yeon phát hiện tại một hội thảo nhỏ. Cùng nhau, họ xây dựng NanoViet — startup deeptech đầu tiên của Việt Nam vươn tầm thế giới, khiến cả ngành vật liệu quốc tế chấn động.</p>"""

S5_CHAPTERS = [
("Chương 1: Bị Đuổi Lúc Nửa Đêm", """Phòng thí nghiệm B7, Viện Khoa học Vật liệu, khu công nghệ cao Hòa Lạc, mười một giờ đêm. Võ Đức Trung đang nhỏ giọt dung dịch polymer nano lên tấm mẫu thử thứ một nghìn ba trăm bảy mươi hai — gần một năm kiên nhẫn thử nghiệm để tìm tỷ lệ pha trộn hoàn hảo.

Anh ghi chú vào sổ lab: "Mẫu 1372 — tỷ lệ graphene oxide 0.05%, polymer matrix PVA/PAA, nhiệt độ 180°C." Rồi dùng kính hiển vi điện tử quét SEM kiểm tra cấu trúc — và nghẹn thở.

Mẫu vật liệu composite bị cắt đôi bằng dao, sau tám giờ tự khép lại hoàn toàn, phục hồi chín mươi bảy phần trăm độ bền ban đầu. Vật liệu tự phục hồi — thứ mà cả ngành vật liệu thế giới săn đuổi suốt hai mươi năm.

"Trời ơi... thành công rồi!" Trung kêu lên trong phòng lab trống. Tay anh run, không phải vì lạnh mà vì nhận ra: phát minh này sẽ thay đổi mọi thứ — từ vỏ máy bay tự sửa chữa, đường ống dầu không bao giờ nứt, đến thiết bị y tế cấy ghép bền vĩnh viễn.

Anh chụp ảnh mẫu, ghi data vào sổ lab, rồi gọi ngay cho GS.TS Bùi Quốc Đạt — giáo sư hướng dẫn, Viện trưởng Viện Khoa học Vật liệu, người mà Trung coi như cha đỡ đầu trong sự nghiệp khoa học.

"Thầy ơi, em tìm ra rồi! Mẫu 1372 phục hồi chín mươi bảy phần trăm! Em cần thầy xuống lab verify ngay!"

GS Đạt đến lab lúc hai giờ sáng, mặc áo khoác vội bên ngoài pyjama. Ông nhìn qua kính hiển vi, kiểm tra data, và suốt mười phút không nói lời nào.

Rồi ông quay sang Trung, mắt lóe sáng — nhưng không phải ánh sáng của niềm vui. Đó là ánh sáng của lòng tham.

"Trung, giỏi lắm. Em để sổ lab và mẫu thử ở đây, thầy sẽ cho nhóm verify lại. Em về nghỉ đi, mai bàn tiếp."

Trung giao sổ lab, về phòng ngủ say sưa với giấc mơ Nobel. Anh không biết rằng GS Đạt đã gọi ngay cho nghiên cứu sinh Lê Thanh Tùng — con trai một đại gia bất động sản — và hai người thức trắng đêm photocopy toàn bộ sổ lab, sao chép dữ liệu, và soạn hồ sơ đăng ký bằng sáng chế.

Hai tuần sau, Trung bị triệu tập lên phòng Viện trưởng. Ngồi đó không chỉ có GS Đạt mà cả Tùng và một luật sư sở hữu trí tuệ.

"Trung, công trình nghiên cứu vật liệu tự phục hồi là tài sản của Viện. Bằng sáng chế đã được nộp dưới tên Viện Khoa học Vật liệu, đồng tác giả: GS Bùi Quốc Đạt và NCS Lê Thanh Tùng. Tên em không có trong hồ sơ."

"CÁI GÌ?" Trung đứng bật dậy. "Tôi là người phát minh ra nó! Mười năm! Một nghìn ba trăm bảy mươi hai mẫu thử!"

"Theo quy chế nghiên cứu của Viện, mọi phát minh trong phòng lab thuộc sở hữu Viện," luật sư đọc monotone.

"Nhưng tên trên bằng sáng chế phải có tên người phát minh! Đây là đạo đức khoa học cơ bản!"

GS Đạt thở dài giả tạo: "Trung ơi, thầy hiểu em buồn. Nhưng đây là quyết định của Viện." Rồi ông đẩy một tờ giấy: thông báo chấm dứt hợp đồng nghiên cứu.

Trung bị thu hồi thẻ lab, khóa email viện, và áp tải ra cổng bởi bảo vệ — lúc nửa đêm, để không ai chứng kiến.

Anh đứng ngoài cổng Viện trong đêm Hà Nội tháng mười hai, gió lạnh cắt da. Mười năm tuổi trẻ, hai nghìn giờ lab, một nghìn ba trăm bảy mươi hai mẫu thử — tất cả bị cướp bởi người thầy mà anh tin tưởng nhất.

Trong túi áo anh còn một thứ: chiếc USB chứa toàn bộ video quay time-lapse của mọi thí nghiệm, tự động backup từ camera cá nhân anh gắn trên bàn lab. GS Đạt cướp sổ lab, nhưng quên rằng: khoa học thực nghiệm không nằm trong giấy tờ — nó nằm trong đầu người làm ra nó."""),

("Chương 2: Hội Thảo Nhỏ Và Nhà Đầu Tư Hàn Quốc", """Ba tháng sau khi bị đuổi, Trung nhận lời mời tham dự một hội thảo vật liệu nhỏ tại Đại học Bách Khoa Hà Nội — buổi seminar sinh viên, khán giả chỉ ba mươi người.

Trung trình bày lý thuyết về cơ chế tự phục hồi ở cấp phân tử — không tiết lộ tỷ lệ pha trộn cụ thể, nhưng đủ để người am hiểu nhận ra đây là đột phá thực sự.

Trong ba mươi người, có một phụ nữ Hàn Quốc ngồi hàng cuối, chăm chú ghi chép. Park Ji-yeon, ba mươi sáu tuổi, giám đốc quỹ đầu tư deeptech "Seoul Materials Ventures," chuyên đầu tư vào startup vật liệu mới ở châu Á.

Sau buổi thuyết trình, Ji-yeon đợi Trung ở sảnh.

"Tiến sĩ Trung, phần trình bày của anh thiếu dữ liệu thực nghiệm, nhưng lý thuyết cơ chế polymer crosslinking reversible mà anh đề xuất hoàn toàn mới và hợp lý. Anh đã có prototype chưa?"

"Có, nhưng bị cướp," Trung cười gượng.

Ji-yeon không tỏ ra ngạc nhiên: "Ở Hàn Quốc, hai mươi phần trăm các nhà nghiên cứu trẻ bị giáo sư cướp bằng sáng chế. Đó là bệnh dịch của giới học thuật châu Á."

Cô đề nghị: Seoul Materials Ventures sẽ đầu tư hai triệu đô để Trung xây phòng lab mới, phát triển lại vật liệu từ đầu. Điều kiện: Trung giữ bảy mươi phần trăm cổ phần startup, và bằng sáng chế mới thuộc về Trung.

"Tại sao cô tin tôi?" Trung hỏi. "Tôi không có lab, không có mẫu thử, không có bằng sáng chế."

"Vì tôi là kỹ sư vật liệu trước khi trở thành nhà đầu tư. Tôi đọc slide của anh, và tôi biết: chỉ người đã làm thí nghiệm hàng nghìn lần mới trình bày được cơ chế phân tử chi tiết đến vậy. Lý thuyết thì ai cũng đọc được, nhưng trực giác thực nghiệm thì không ai đánh cắp được."

Trung nhìn người phụ nữ Hàn Quốc đứng trước mình, mắt sáng rực quyết tâm. Lần đầu tiên sau ba tháng, anh cảm thấy được hiểu.

"Tôi đồng ý. Nhưng tôi cần thêm một thứ: phòng lab phải ở Việt Nam, và nhóm nghiên cứu là người Việt." """),

("Chương 3: Vật Liệu Mới — Tốt Hơn Bản Gốc", """NanoViet Lab được thành lập tại khu công nghệ cao Sài Gòn, phòng lab một trăm mét vuông với thiết bị hiện đại nhập từ Hàn Quốc. Trung tuyển năm nghiên cứu sinh trẻ từ Bách Khoa và ĐHQG.

Sáu tháng nghiên cứu lại từ đầu. Trung không sao chép công thức cũ — anh cải tiến nó. Vật liệu mới, NanoHeal, đạt tỷ lệ phục hồi chín mươi chín phần trăm, có khả năng phục hồi ở nhiệt độ phòng thay vì cần gia nhiệt, và bền gấp ba lần bản gốc.

"Mẫu 1372 là bước đầu. NanoHeal là đích đến," Trung nói với nhóm nghiên cứu khi kết quả verify lần cuối.

Paper nghiên cứu được gửi đến tạp chí Nature Materials — tạp chí vật liệu uy tín nhất thế giới. Sau ba tháng peer review, paper được accept và đăng trang bìa.

Cộng đồng khoa học quốc tế bùng nổ. Reuters, Science Daily, và Nikkei Asia đồng loạt đưa tin: "Vietnamese startup creates world's first room-temperature self-healing material."

Tại Viện Khoa học Vật liệu, GS Đạt đọc paper Nature Materials, mặt xám ngoét. Bằng sáng chế mà ông cướp từ Trung — vật liệu cần gia nhiệt 180 độ để phục hồi — giờ trở nên lạc hậu trước NanoHeal của chính Trung.

Tùng run rẩy gọi GS Đạt: "Thầy ơi, paper của Trung trên Nature. Vật liệu của hắn tốt hơn nhiều. Bằng sáng chế của mình bây giờ..."

"Vô giá trị," GS Đạt gầm lên. "Vô giá trị!" """),

("Chương 4: Hội Nghị MRS — Vả Mặt Giáo Sư", """Trung được mời keynote tại Materials Research Society Fall Meeting ở Boston — hội nghị vật liệu lớn nhất thế giới, sáu nghìn nhà khoa học tham dự.

GS Đạt cũng có mặt — ông trình bày poster về bằng sáng chế vật liệu tự phục hồi "của ông" tại phiên poster session.

Khi Trung keynote trên sân khấu lớn, ông ngồi ở hàng ghế sau, vã mồ hôi. Mọi dữ liệu Trung trình bày đều chứng minh NanoHeal vượt trội hoàn toàn so với bằng sáng chế mà ông đứng tên.

Phần hỏi đáp, một giáo sư MIT hỏi: "Dr. Trung, mối quan hệ giữa NanoHeal và bằng sáng chế VN-2025-0847 đăng ký bởi Viện Khoa học Vật liệu Việt Nam?"

Trung đáp bình tĩnh: "Bằng sáng chế đó dựa trên nghiên cứu ban đầu mà tôi thực hiện tại Viện. Tôi là người phát minh, nhưng tên tôi không có trên bằng. NanoHeal là công trình hoàn toàn mới, phát triển tại NanoViet Lab với kiến trúc phân tử khác biệt."

Rồi anh chiếu lên màn hình: video time-lapse từ camera cá nhân, ghi lại toàn bộ quá trình thí nghiệm 1.372 mẫu trong phòng lab Viện — mỗi video có timestamp và watermark. Chỉ có Trung xuất hiện trong video. Không có GS Đạt, không có Tùng.

"Đây là bằng chứng video của quá trình nghiên cứu thực tế. Tôi có một nghìn ba trăm bảy mươi hai video, từ mẫu đầu tiên đến mẫu thành công. Ai muốn verify, tôi sẵn sàng chia sẻ."

Sáu nghìn nhà khoa học quay đầu nhìn về phía GS Đạt — người đứng tên trên bằng sáng chế nhưng không có mặt trong bất kỳ video thí nghiệm nào.

Đạt rời khỏi hội trường trong im lặng, poster của ông bị gỡ khỏi phiên trưng bày cùng ngày."""),

("Chương 5: Hợp Đồng Với Boeing", """Sau hội nghị MRS, NanoViet nhận được email từ Boeing Advanced Materials Division: họ muốn test NanoHeal cho vỏ máy bay thương mại.

Nếu thành công, đây sẽ là hợp đồng trị giá hàng chục triệu đô — vật liệu tự phục hồi cho vỏ máy bay sẽ giảm chi phí bảo trì hàng tỷ đô mỗi năm cho ngành hàng không toàn cầu.

Trung bay đến Seattle, mang theo mẫu NanoHeal. Kỹ sư Boeing test trong phòng lab Boeing R&D Center: chịu lực, chịu nhiệt, chịu hóa chất, chịu tia UV, chịu rung — tất cả đều pass với kết quả vượt xa tiêu chuẩn FAA.

"This is the best composite material we've tested in twenty years," Trưởng nhóm R&D Boeing nói.

Boeing ký Letter of Intent mua bản quyền sử dụng NanoHeal cho chương trình máy bay thế hệ mới, trị giá năm mươi triệu đô trong năm năm.

Ji-yeon gọi Trung từ Seoul: "Anh vừa ký hợp đồng lớn nhất lịch sử startup deeptech Đông Nam Á."

Trung cười: "Tôi chỉ ký giấy thôi. Một nghìn ba trăm bảy mươi hai mẫu thử mới là người ký hợp đồng." """),

("Chương 6: NanoViet Thành Unicorn", """Sau hợp đồng Boeing, NanoViet huy động vốn vòng Series B: hai trăm triệu đô từ Softbank, Temasek, và quỹ khí hậu của Bill Gates. Định giá một tỷ năm trăm triệu đô — deeptech unicorn đầu tiên của Đông Nam Á.

NanoViet mở rộng sang bốn lĩnh vực: hàng không, y tế cấy ghép, xây dựng, và năng lượng tái tạo. Nhà máy sản xuất NanoHeal tại khu công nghệ cao Sài Gòn, diện tích mười nghìn mét vuông, tuyển ba trăm kỹ sư.

Trung được TIME đưa vào danh sách "100 Most Influential People" — nhà khoa học Việt Nam đầu tiên nhận vinh dự này.

Tại Viện Khoa học Vật liệu, GS Đạt nộp đơn từ chức Viện trưởng. Bộ KH&CN mở điều tra về vụ đánh cắp bằng sáng chế. Tùng bị rút học vị Tiến sĩ — vì luận án của hắn dựa trên nghiên cứu đánh cắp từ Trung.

Cả hai từ đỉnh cao học thuật rơi xuống đáy."""),

("Chương 7: Di Sản Của Người Mẹ Đơn Thân", """Ít ai biết rằng Trung lớn lên ở xóm nghèo Thanh Hóa, mẹ đơn thân làm công nhân may gia công. Bà Võ Thị Hạnh nuôi con ăn học bằng tiền lương hai triệu đồng mỗi tháng.

Mỗi đêm, sau ca làm mười hai tiếng ở xưởng may, bà Hạnh ngồi vá lại quần áo rách cho Trung bằng những đường kim mũi chỉ kiên nhẫn, tỉ mỉ.

"Con ơi, mẹ chỉ biết vá quần áo. Nhưng mẹ muốn con biết: thứ gì rách cũng vá được, nếu mình kiên nhẫn."

Câu nói đó theo Trung vào phòng lab, trở thành triết lý nghiên cứu: vật liệu tự phục hồi — thứ tự vá lại sau khi bị rách — được sinh ra từ đôi tay một người mẹ vá quần áo đêm đêm.

Trung xây cho mẹ một ngôi nhà tại Thanh Hóa, nhưng bà Hạnh vẫn giữ chiếc máy may cũ. "Mẹ vẫn nhận vá quần áo cho mấy đứa nhỏ trong xóm. Miễn phí," bà cười.

NanoViet tài trợ chương trình học bổng "Bàn Tay Mẹ" cho một nghìn sinh viên nghèo theo đuổi ngành khoa học vật liệu mỗi năm. Logo của chương trình: đôi tay đang vá vải, với hạt nano lấp đầy vết rách."""),

("Chương 8: GS Đạt Và Tùng Sụp Đổ", """Bộ KH&CN kết luận: GS Bùi Quốc Đạt vi phạm đạo đức khoa học nghiêm trọng. Bằng sáng chế bị hủy. Đạt bị cấm nghiên cứu và giảng dạy vĩnh viễn, cấm tham gia mọi hội đồng khoa học quốc gia.

Từ một Viện trưởng quyền lực, GS Đạt trở thành kẻ bị tẩy chay trong giới khoa học. Không trường đại học, không viện nghiên cứu nào thuê. Ông ngồi trong căn hộ chung cư cũ, nhìn tấm bằng giáo sư trên tường và thấy nó nặng như đá tảng.

Tùng mất học vị, mất việc, trở về nhà bố — nhưng bố hắn, ông đại gia bất động sản, cũng đã phá sản vì bong bóng BĐS. Từ con nhà giàu có người hầu kẻ hậu, Tùng đi giao hàng Grab để kiếm sống.

Hắn chạy qua khu công nghệ cao Sài Gòn, nhìn tòa nhà NanoViet sáng đèn, và hiểu: hắn đã đánh mất cơ hội trở thành đồng tác giả của phát minh vĩ đại nhất thế kỷ — vì lòng tham nhỏ mọn."""),

("Chương 9: Nobel Vật Liệu", """Hai năm sau hợp đồng Boeing, NanoHeal đã được ứng dụng trong ba mươi lĩnh vực, từ vỏ máy bay đến stent tim mạch. Ước tính giảm chi phí bảo trì toàn cầu năm tỷ đô mỗi năm.

Viện Hàn lâm Khoa học Hoàng gia Thụy Điển công bố: Giải Nobel Hóa học năm nay được trao cho TS Võ Đức Trung vì "phát minh vật liệu nano tự phục hồi, mở ra kỷ nguyên mới cho khoa học vật liệu."

Trung đứng trên sân khấu Stockholm Concert Hall, nhận huy chương từ tay Quốc vương Thụy Điển. Bài phát biểu của anh ngắn gọn:

"Vật liệu tự phục hồi được sinh ra từ câu nói của mẹ tôi: thứ gì rách cũng vá được, nếu mình kiên nhẫn. Giải thưởng này dành cho mẹ tôi, và cho mọi nhà khoa học trẻ bị đánh cắp công trình — hãy kiên nhẫn, vì khoa học không bao giờ nói dối."

Bà Hạnh ngồi ở hàng ghế danh dự, mặc áo dài Việt Nam, tay nắm chặt chiếc khăn thêu cũ. Bà khóc, nhưng nụ cười không tắt."""),

("Chương 10: Quay Về Viện Cũ", """Một năm sau Nobel, Trung quay lại Viện Khoa học Vật liệu — giờ đã được đổi tên thành Viện NanoViet-VAST theo chương trình hợp tác. NanoViet tài trợ toàn bộ trang thiết bị lab mới trị giá năm mươi tỷ đồng.

Trung đi qua phòng lab B7 — nơi anh phát minh NanoHeal, nơi anh bị đuổi lúc nửa đêm. Phòng lab giờ sáng choang, thiết bị hiện đại gấp mười lần, có mười nghiên cứu sinh trẻ đang hăng say thí nghiệm.

Cửa phòng lab mở. Một người đàn ông gầy yếu, lưng còng, tóc bạc trắng, đứng ngoài hành lang.

GS Đạt.

"Trung," ông nói, giọng khàn đặc. "Thầy xin lỗi. Thầy biết lời xin lỗi muộn rồi, nhưng..."

Trung nhìn người thầy cũ — người đã dạy anh yêu khoa học, rồi cướp thành quả khoa học của anh. Trong lòng anh, vết thương đã lành — như NanoHeal, tự phục hồi theo thời gian.

"Thầy, em không hận thầy. Nhưng em không tha thứ. Vì tha thứ ở đây có nghĩa là chấp nhận rằng đánh cắp nghiên cứu là chuyện bình thường. Nó không bình thường."

Rồi anh rút một phong bì: "Viện mới có chương trình cố vấn cho nghiên cứu sinh trẻ. Thầy có kinh nghiệm giảng dạy, dù thầy đã sai về đạo đức. Nếu thầy muốn chuộc lỗi, hãy dạy lại. Nhưng lần này, dạy cả đạo đức khoa học."

GS Đạt cầm phong bì, tay run. Ông cúi đầu, lần đầu tiên trong đời, trước học trò cũ.

Trung quay lưng, bước về phía phòng lab mới. Ji-yeon đang đợi ở đó — cô đã trở thành vợ anh, và đang mang thai đứa con đầu lòng.

"Xong chưa?" cô hỏi.

"Xong." Trung nắm tay vợ, nhìn đội nghiên cứu trẻ đang hào hứng trong lab. "Bây giờ, để thế hệ sau tiếp tục."

Trong phòng lab B7, mẫu NanoHeal mới nhất đang tự phục hồi trên bàn thí nghiệm — vết cắt khép lại, hoàn hảo, như chưa bao giờ bị tổn thương."""),
]

# ═══════════════════════════════════════════════════════════════════════════════
# STORY 6: NỮ KIỂM TOÁN VIÊN
# ═══════════════════════════════════════════════════════════════════════════════

S6_TITLE = "BỊ GẠT KHỎI HỘI ĐỒNG QUẢN TRỊ, TÔI MANG BẰNG CHỨNG GIAN LẬN SỔ SÁCH KHIẾN CẢ TẬP ĐOÀN RƠI TỰ DO"
S6_AUTHOR = "Đỗ Thanh Hằng"
S6_COVER = "base_cover_40.png"
S6_INTRO = """<p><strong>"Bảy năm tôi kiểm toán cho tập đoàn, phát hiện bốn lỗ hổng tài chính cứu công ty khỏi phá sản. Đổi lại, khi tôi phát hiện CEO biển thủ, họ đuổi tôi và dọa kiện tôi phá hoại uy tín doanh nghiệp."</strong></p>
<p>Đỗ Thanh Hằng, nữ kiểm toán viên forensic sắc sảo nhất Việt Nam, bị Chủ tịch HĐQT Ngô Văn Thắng và Kế toán trưởng Phạm Thị Loan đuổi khỏi Tập đoàn Thiên Phú khi cô phát hiện đường dây biển thủ ba trăm tỷ đồng qua hệ thống hóa đơn giả.</p>
<p>Bị vu khống, bị dọa, Hằng không chạy. Cô mang bằng chứng forensic accounting vạch trần toàn bộ, thành lập hãng kiểm toán forensic đầu tiên tại Việt Nam, và buộc đế chế tham nhũng phải sụp đổ trước pháp luật.</p>"""

S6_CHAPTERS = [
("Chương 1: Con Số Không Khớp", """Tầng hai mươi hai, trụ sở Tập đoàn Thiên Phú, quận 7. Đỗ Thanh Hằng ngồi trước bốn màn hình, mắt không rời chuỗi số trên bảng tính Excel. Ba triệu dòng dữ liệu kế toán của bảy năm, và cô vừa tìm thấy thứ không đúng.

Hóa đơn mua hàng từ công ty Minh Phát Logistics, tổng cộng ba trăm mười hai tỷ đồng trong bốn năm. Nhưng khi Hằng kiểm tra chéo với dữ liệu thuế GTGT, mã số thuế của Minh Phát Logistics dẫn đến một công ty "ma" — được thành lập hai tháng trước hóa đơn đầu tiên, không có nhân viên, không có trụ sở thực.

Ba trăm mười hai tỷ đồng chảy vào hư không.

"Chị Loan ơi, em cần xem sổ quỹ tiền mặt tháng 3 năm 2023," Hằng gọi Kế toán trưởng Phạm Thị Loan.

Loan, bốn mươi tám tuổi, gương mặt lúc nào cũng mang vẻ hiền hậu như giáo viên tiểu học, nhưng mắt thoáng lo lắng: "Hằng ơi, sổ quỹ đó đang... cập nhật. Tuần sau em lấy được."

"Nhưng em cần bây giờ, chị. Kiểm toán quý này phải nộp trong hai tuần."

"Tuần sau, Hằng. Đó là chỉ thị của anh Thắng." Loan tắt điện thoại.

Hằng nhíu mày. Bảy năm làm kiểm toán nội bộ, chưa bao giờ bị từ chối cung cấp sổ sách. Trừ khi trong sổ đó có thứ không thể cho ai thấy.

Cô đặt tay lên bàn phím, mở hệ thống ERP nội bộ bằng quyền admin mà cô có từ ngày đầu. Sổ quỹ tiền mặt hiện lên — và Hằng nghẹn thở.

Ba trăm mười hai tỷ đồng hóa đơn "mua hàng" từ Minh Phát Logistics được thanh toán bằng tiền mặt — không qua ngân hàng. Và người ký duyệt chi: Ngô Văn Thắng, Chủ tịch HĐQT.

Hằng in toàn bộ dữ liệu, copy vào USB cá nhân, và soạn báo cáo kiểm toán đặc biệt gửi lên HĐQT.

Ngày hôm sau, cô bị gọi lên phòng Chủ tịch.

Ngô Văn Thắng, năm mươi lăm tuổi, to béo, mặc vest Brioni, đeo đồng hồ Patek Philippe, ngồi sau bàn gỗ sồi trị giá một tỷ. Bên cạnh là Loan và hai luật sư.

"Hằng, HĐQT quyết định: chấm dứt hợp đồng với em, có hiệu lực ngay. Lý do: vi phạm quy chế bảo mật thông tin nội bộ — em truy cập dữ liệu tài chính ngoài phạm vi được phân công."

"Ngoài phạm vi? Em là kiểm toán nội bộ, em có quyền truy cập MỌI dữ liệu tài chính!"

Luật sư đẩy tờ giấy: "Phạm vi kiểm toán nội bộ đã được HĐQT thu hẹp theo nghị quyết mới, ký ngày hôm qua. Kiểm toán nội bộ chỉ kiểm tra chi nhánh, không kiểm tra trụ sở chính."

"Nghị quyết ký hôm qua?" Hằng cười khẩy. "Các anh ký nghị quyết mới để đuổi tôi vì tôi phát hiện các anh biển thủ ba trăm tỷ?"

"Cẩn thận lời nói," Thắng gầm, mắt đỏ ngầu. "Nếu cô tung tin sai sự thật, tôi kiện cô tội vu khống và phá hoại uy tín doanh nghiệp. Cô sẽ ngồi tù."

Hằng đứng dậy, siết chặt chiếc USB trong túi áo. "Anh Thắng, tôi là kiểm toán viên. Công việc của tôi là tìm sự thật. Và sự thật là: ba trăm mười hai tỷ đồng đã biến mất qua hóa đơn ma. Anh có thể đuổi tôi, nhưng anh không thể đuổi được con số."

Bảo vệ áp tải Hằng ra cửa. Khi bước qua sảnh, Hằng ngoái lại nhìn tòa nhà kính sáng loáng của Thiên Phú — nơi cô từng cống hiến bảy năm tuổi trẻ. Bên trong đó, ba trăm tỷ đồng đang thối rữa."""),

("Chương 2: Lập Hãng Kiểm Toán Forensic", """Hằng không chạy. Cô thuê một văn phòng nhỏ trên đường Nguyễn Huệ, treo biển "Hằng & Associates — Forensic Accounting Services." Đây là hãng kiểm toán pháp y đầu tiên tại Việt Nam — chuyên điều tra gian lận tài chính cho doanh nghiệp.

Ba tháng đầu, không khách hàng. Cái tên "Đỗ Thanh Hằng" bị Thiên Phú bôi nhọ khắp giới tài chính: "Nhân viên kiểm toán bị đuổi vì vi phạm bảo mật, cố tình phá hoại uy tín công ty."

Nhưng Hằng có thứ mà tiền không mua được: bằng chứng. Cô gửi toàn bộ báo cáo forensic kèm USB dữ liệu cho Cơ quan Điều tra Bộ Công an — đơn vị chuyên xử lý tội phạm kinh tế lớn.

Sáu tháng điều tra, công an xác nhận: Minh Phát Logistics là shell company, ba trăm mười hai tỷ đồng chảy vào tài khoản cá nhân của Ngô Văn Thắng và Phạm Thị Loan qua ba lớp rửa tiền.

Lệnh bắt được ban hành. Thắng bị bắt tại sân golf Long Thành, vẫn đang mặc quần short và giày golf. Loan bị bắt tại nhà riêng, trong két sắt còn năm tỷ tiền mặt.

VnExpress, Tuổi Trẻ, CafeF đồng loạt: "Nữ kiểm toán viên bị đuổi phá vỡ đường dây biển thủ 312 tỷ đồng tại Tập đoàn Thiên Phú."

Danh tiếng Hằng vụt sáng. Từ "người bị đuổi" trở thành "hero tài chính."

Khách hàng ào đến. Các tập đoàn lớn thuê Hằng & Associates kiểm toán forensic để phát hiện gian lận nội bộ. Doanh thu năm đầu tiên: mười hai tỷ đồng."""),

("Chương 3: Vụ Thứ Hai — Chuỗi Khách Sạn 5 Sao", """Tiếng tăm từ vụ Thiên Phú mang đến cho Hằng khách hàng lớn: Tập đoàn Hoàng Gia Hospitality, chuỗi khách sạn năm sao hàng đầu Việt Nam với mười hai property từ Hà Nội đến Phú Quốc.

HĐQT Hoàng Gia thuê Hằng kiểm tra nghi vấn CFO biển thủ qua hệ thống procurement giả mạo. Hằng mất bốn tháng phân tích hai mươi triệu dòng giao dịch, phát hiện: CFO đã tạo một mạng lưới bốn mươi hai nhà cung cấp ma, rút rỗng tám mươi bảy tỷ đồng trong ba năm.

Khi Hằng trình bày kết quả trước HĐQT, CFO bỏ chạy — nhưng công an đã đợi sẵn ở sảnh.

Vụ án thứ hai càng củng cố vị thế Hằng & Associates. Forbes Vietnam đưa Hằng vào danh sách "50 Phụ nữ Ảnh hưởng nhất Việt Nam." """),

("Chương 4: Kẻ Thù Phản Công", """Thắng và Loan tuy trong tù nhưng vẫn còn đồng minh bên ngoài. Một đêm, văn phòng Hằng bị đột nhập, laptop và ổ cứng bị đánh cắp. Hằng phát hiện ngay sáng hôm sau.

"Họ tưởng dữ liệu nằm trong laptop?" Hằng cười lạnh. Toàn bộ dữ liệu forensic được cô mã hóa và lưu trên hệ thống cloud với backup ba nơi khác nhau. Laptop bị trộm chỉ chứa... mèo ảnh.

Hằng báo công an, camera an ninh tòa nhà ghi lại kẻ đột nhập. Truy ra: người thuê là em trai của Loan, vừa lĩnh thêm án hai năm tù.

Sự kiện này khiến Hằng quyết định đầu tư mạnh vào cybersecurity: tất cả dữ liệu forensic từ nay được bảo vệ bằng hệ thống mã hóa cấp quân sự. Không ai có thể phá hủy bằng chứng."""),

("Chương 5: Hội Nghị ACFE — Vả Mặt Trên Sân Khấu Quốc Tế", """Hằng được mời keynote tại Hội nghị Thường niên của Association of Certified Fraud Examiners (ACFE) tại Las Vegas — hội nghị kiểm toán gian lận lớn nhất thế giới, bốn nghìn chuyên gia tham dự.

Bài trình bày "From Fired Auditor to Fraud Fighter: The Vietnamese Model" nhận standing ovation năm phút. Hằng chia sẻ methodology forensic accounting của cô: kết hợp data analytics với điều tra thực địa, sử dụng Benford's Law, network analysis, và AI pattern recognition để phát hiện gian lận.

Sau keynote, ACFE mời Hằng viết case study cho giáo trình đào tạo toàn cầu. Hãng kiểm toán Big Four — Deloitte, PwC, EY, KPMG — đều liên hệ hợp tác.

Hằng & Associates mở chi nhánh Singapore và Bangkok, trở thành hãng kiểm toán forensic hàng đầu Đông Nam Á."""),

("Chương 6: Mở Rộng Đế Chế", """Sau hội nghị ACFE, Hằng mở rộng dịch vụ: ngoài kiểm toán forensic, Hằng & Associates cung cấp đào tạo compliance, tư vấn chống rửa tiền, và điều tra do diligence cho M&A.

Doanh thu năm thứ ba: năm mươi tỷ đồng. Đội ngũ: bảy mươi chuyên gia forensic từ tám quốc gia. Văn phòng tại Sài Gòn, Hà Nội, Singapore, Bangkok.

Hằng vẫn giữ nguyên tắc: mỗi tháng nhận một vụ pro-bono cho doanh nghiệp nhỏ bị gian lận tài chính."""),

("Chương 7: Gia Đình Và Sự Thật Đằng Sau", """Hằng ít kể, nhưng cô theo đuổi nghề kiểm toán vì bố. Bố cô, ông Đỗ Minh Đức, từng là kế toán trưởng một xí nghiệp quốc doanh. Ông phát hiện giám đốc biển thủ và báo cáo — nhưng thay vì được bảo vệ, ông bị đuổi, bị vu khống, và chết trong nghèo đói khi Hằng mới mười hai tuổi.

"Bố chết vì nói sự thật và không ai bảo vệ ông. Tôi thề sẽ trở thành người bảo vệ cho những kế toán nói sự thật," Hằng chia sẻ trong một bài phỏng vấn trên BBC Vietnamese.

Hằng & Associates thành lập Quỹ "Người Tố Cáo" — bảo vệ pháp lý miễn phí cho nhân viên tố cáo gian lận tài chính bị trả thù."""),

("Chương 8: Thiên Phú Sụp Đổ Hoàn Toàn", """Tòa án TP.HCM tuyên án: Ngô Văn Thắng hai mươi năm tù, Phạm Thị Loan mười lăm năm tù. Tập đoàn Thiên Phú phá sản, tổng nợ một nghìn hai trăm tỷ đồng.

Ba trăm mười hai tỷ biển thủ được thu hồi một phần — hai trăm tỷ từ tài sản cá nhân, còn lại mất trong đầu tư thua lỗ và tiêu xài hoang phí.

Ngày tuyên án, Hằng không đến tòa. Cô ở văn phòng, kiểm toán vụ mới. Khi đồng nghiệp hỏi, cô nói: "Bố tôi không được thấy ngày công lý đến. Tôi thấy rồi. Thế là đủ." """),

("Chương 9: Giải Thưởng Quốc Tế Chống Tham Nhũng", """Hằng nhận giải "Global Anti-Corruption Champion" do Transparency International trao tại Berlin — giải thưởng chống tham nhũng uy tín nhất thế giới.

Trên sân khấu, cô nói: "Tôi bị đuổi vì phát hiện ba trăm tỷ đồng biến mất. Nhưng tôi không biến mất. Gian lận tài chính không phải vấn đề của riêng Việt Nam — nó là đại dịch toàn cầu. Và kiểm toán forensic là vaccine."

Bài phát biểu được truyền hình trực tiếp. Tại Việt Nam, Quốc hội mời Hằng tham gia soạn thảo Luật Bảo vệ Người tố cáo — lần đầu tiên trong lịch sử lập pháp Việt Nam."""),

("Chương 10: Quay Về Thiên Phú", """Hằng & Associates mua lại tòa nhà trụ sở cũ của Thiên Phú tại phiên đấu giá phá sản. Cô biến tầng hai mươi hai — nơi cô bị đuổi — thành trung tâm đào tạo kiểm toán forensic miễn phí cho sinh viên.

Ngày khai trương, Hằng đứng trước phòng cô từng ngồi kiểm toán, giờ là lớp học với năm mươi sinh viên háo hức.

"Các em, kiểm toán không phải nghề đếm tiền. Kiểm toán là nghề bảo vệ sự thật. Và sự thật," cô mỉm cười, "không bao giờ sợ ai."

Trên tường phòng học, cô treo một tấm ảnh: bố cô, ông Đỗ Minh Đức, trong bộ áo sơ mi trắng ngồi trước chồng sổ sách — tấm ảnh duy nhất cô còn giữ được.

Dưới ảnh, dòng chữ: "Dành cho bố — người kế toán trung thực nhất mà con biết."

Hằng quay lưng, bước vào lớp. Bài giảng đầu tiên: "Benford's Law — Khi con số tố cáo gian lận." """),
]

# ═══════════════════════════════════════════════════════════════════════════════
# STORY 7: NHẠC TRƯỞNG BỊ ĐUỔI
# ═══════════════════════════════════════════════════════════════════════════════

S7_TITLE = "BỊ ĐUỔI KHỎI DÀN NHẠC GIAO HƯỞNG, TÔI TỰ LẬP ORCHESTRA KHIẾN CẢ CHÂU Á ĐỨNG DẬY VỖ TAY"
S7_AUTHOR = "Nguyễn Quốc Bảo"
S7_COVER = "base_cover_41.png"
S7_INTRO = """<p><strong>"Mười hai năm tôi cống hiến cho Dàn nhạc Giao hưởng Quốc gia, từ violinist vô danh thành nhạc trưởng được công chúng yêu mến. Đổi lại, họ sa thải tôi vì tôi dám chơi nhạc Việt Nam trên sân khấu cổ điển."</strong></p>
<p>Nguyễn Quốc Bảo, nhạc trưởng trẻ tài năng nhất Việt Nam, bị Giám đốc Nhà hát Hoàng Trọng Nghĩa và Concertmaster Vũ Đình Khải sa thải vì dám đưa nhạc cụ dân tộc — đàn bầu, đàn tranh, sáo trúc — vào chương trình biểu diễn giao hưởng.</p>
<p>Bị gạt bỏ, Bảo thành lập Vietnam Philharmonic — dàn nhạc giao hưởng tư nhân đầu tiên tại Việt Nam, kết hợp âm nhạc cổ điển phương Tây với nhạc cụ dân tộc, tạo nên thể loại "Vietnamese Symphonic" độc nhất vô nhị.</p>"""

S7_CHAPTERS = [
("Chương 1: Bản Nhạc Cuối Cùng", """Nhà hát Lớn Hà Nội, tám giờ tối thứ Bảy. Một nghìn hai trăm khán giả im lặng khi Nguyễn Quốc Bảo giơ đũa chỉ huy lên — bắt đầu chương trình "Giao hưởng Việt Nam," tác phẩm mà anh soạn suốt hai năm.

Đây không phải giao hưởng thông thường. Bảo đã sáng tác bản giao hưởng bốn chương kết hợp dàn nhạc phương Tây với nhạc cụ dân tộc: đàn bầu solo trong chương hai, đàn tranh hòa tấu cùng violon trong chương ba, và sáo trúc đối thoại với flute trong chương bốn.

Nhạc cất lên. Chương một — "Đồng bằng" — tiếng cello trầm mô tả cánh đồng lúa mênh mông. Rồi đàn bầu cất tiếng, giai điệu uốn lượn như ngọn gió qua đồng — và cả khán phòng nín thở.

Không ai từng nghe thứ này trước đây. Đàn bầu — nhạc cụ dân gian bình dị — vang lên giữa dàn nhạc tám mươi người như đứa con lạc về với gia đình, vừa lạ lẫm vừa thân thuộc đến nghẹn lòng.

Khi bản giao hưởng kết thúc, khán giả đứng dậy vỗ tay năm phút liên tục. Nhiều người khóc. Đàn bầu đã chạm vào thứ sâu nhất trong họ: ký ức tuổi thơ, quê hương, và niềm tự hào dân tộc.

Nhưng phía sau cánh gà, Giám đốc Nhà hát Hoàng Trọng Nghĩa không vỗ tay. Ông đứng khoanh tay, mặt tối sầm.

Sáng hôm sau, Bảo bị gọi lên phòng Giám đốc.

"Quốc Bảo, cậu đưa đàn bầu lên sân khấu Nhà hát Lớn? Đó là sân khấu dành cho nhạc cổ điển phương Tây, không phải nhạc chèo!" Nghĩa đập bàn.

"Thưa anh, tôi không chơi nhạc chèo. Tôi viết giao hưởng dựa trên thang âm Việt Nam, kết hợp nhạc cụ dân tộc với—"

"Tôi không quan tâm! Nhà tài trợ Hàn Quốc của dàn nhạc muốn chương trình toàn Beethoven và Tchaikovsky. Cậu chơi đàn bầu thì họ rút tài trợ!"

Concertmaster Vũ Đình Khải ngồi cạnh, gật gù: "Bảo, em giỏi chỉ huy, nhưng em quá cực đoan. Nhạc cổ điển là nhạc cổ điển, nhạc dân tộc là nhạc dân tộc. Đừng trộn lẫn."

Nghĩa ném quyết định sa thải: "Nhạc trưởng mới sẽ là anh Khải. Cậu thu dọn đồ, trả đũa chỉ huy."

Bảo nhìn chiếc đũa chỉ huy bằng gỗ mun — món quà mẹ tặng khi anh đậu vào Nhạc viện. Anh siết chặt nó trong tay.

"Tôi đi. Nhưng đũa này tôi giữ. Và âm nhạc Việt Nam — nó xứng đáng đứng trên mọi sân khấu thế giới."

Anh bước ra khỏi Nhà hát Lớn dưới cơn mưa Hà Nội tháng mười, chiếc đũa mun ướt nước mưa. Trong đầu anh, giai điệu bản giao hưởng vẫn vang — không ai tắt được."""),

("Chương 2: Dàn Nhạc Trong Nhà Kho", """Bảo thuê một nhà kho cũ ở quận Long Biên, diện tích hai trăm mét vuông, làm phòng tập. Tường bê tông trần, trần tôn, ánh sáng từ bóng đèn huỳnh quang.

Anh đăng tin tuyển nhạc công: "Vietnam Philharmonic tìm nhạc công yêu âm nhạc Việt Nam. Lương: zero. Đam mê: bắt buộc."

Ba mươi nhạc công đến — phần lớn là sinh viên nhạc viện, giáo viên nhạc, và nhạc công freelance. Trong đó có Trần Minh Tâm, nghệ nhân đàn bầu cuối cùng của phố cổ Hà Nội, bảy mươi hai tuổi, lưng đã còng nhưng ngón tay vẫn nhanh như gió.

"Cháu ơi, ông nghe cháu chơi ở Nhà hát Lớn. Đàn bầu của ông chưa bao giờ được chơi cùng dàn nhạc giao hưởng. Đêm đó, ông khóc," ông Tâm nói khi đến nhà kho.

Bảo ôm ông cụ, mắt cay. "Ông ơi, ông sẽ là soloist. Đàn bầu xứng đáng đứng center stage."

Ba tháng tập luyện trong nhà kho, không lương, không tài trợ, không khán giả. Nhưng âm nhạc vang lên mỗi đêm — và hàng xóm bắt đầu kéo đến ngồi ngoài cửa nghe.

Một video TikTok do hàng xóm quay — cảnh ba mươi nhạc công chơi giao hưởng trong nhà kho, đàn bầu solo giữa tiếng violin — đạt năm triệu lượt xem."""),

("Chương 3: Concert Đầu Tiên — Viral Toàn Quốc", """Bảo tổ chức concert đầu tiên không phải ở nhà hát, mà ở sân Văn Miếu Quốc Tử Giám — không gian mở, miễn phí, giữa lòng Hà Nội cổ kính.

Hai nghìn người đến. Nhiều hơn sức chứa. Người ta ngồi trên bậc đá, đứng ngoài tường, trèo lên cây để nghe.

Bảo chỉ huy dàn nhạc ba mươi người chơi "Giao hưởng Việt Nam" phiên bản mở rộng. Đàn bầu, đàn tranh, sáo trúc hòa quyện cùng violin, cello, flute — dưới ánh trăng và đèn lồng Văn Miếu.

Khi ông Tâm solo đàn bầu trong chương "Nguyệt" — khúc nhạc mô tả đêm trăng trên sông Hương — hai nghìn người im lặng tuyệt đối. Không tiếng ho, không tiếng thì thầm. Chỉ có tiếng đàn bầu và gió đêm Hà Nội.

Concert trở thành hiện tượng văn hóa. Video đàn bầu tại Văn Miếu đạt hai mươi triệu lượt xem trên YouTube. CNN, BBC, NHK đồng loạt đưa tin.

Tại Nhà hát Lớn, dàn nhạc quốc gia dưới sự chỉ huy của Khải đang chơi Beethoven cho hai trăm khán giả — nửa hội trường trống."""),

("Chương 4: Nhà Tài Trợ Và Cuộc Chiến", """Nghĩa không chịu nổi. Ông cử Khải viết đơn kiện Bảo: "sử dụng tác phẩm 'Giao hưởng Việt Nam' là tài sản trí tuệ của Nhà hát."

Nhưng Bảo đã đăng ký bản quyền tác phẩm từ trước khi biểu diễn tại Nhà hát Lớn — bản giao hưởng là sáng tác cá nhân, không phải công trình của nhà hát. Đơn kiện bị bác.

Thay vào đó, một nhà tài trợ bất ngờ xuất hiện: Tập đoàn Vingroup đề nghị tài trợ mười tỷ đồng mỗi năm cho Vietnam Philharmonic, với điều kiện: dàn nhạc trình diễn ít nhất bốn concert miễn phí cho cộng đồng mỗi năm.

Bảo đồng ý ngay lập tức. Vietnam Philharmonic có nhà, có tiền, có sứ mệnh."""),

("Chương 5: Tour Châu Á — Đàn Bầu征服 Thế Giới", """Một năm sau concert Văn Miếu, Vietnam Philharmonic khởi động tour diễn châu Á: Tokyo, Seoul, Singapore, Bangkok, Kuala Lumpur — năm thành phố trong ba tuần.

Tokyo Suntory Hall, Nhật Bản: hai nghìn khán giả Nhật — vốn cực kỳ khó tính với nhạc cổ điển — đứng dậy vỗ tay bảy phút sau concert. Báo Asahi Shimbun viết: "Vietnam Philharmonic đã làm điều mà không ai nghĩ tới: biến nhạc cụ dân tộc thành ngôn ngữ phổ quát."

Ông Tâm, bảy mươi ba tuổi, solo đàn bầu trên sân khấu Suntory Hall — nơi mà Berliner Philharmoniker từng biểu diễn. Ông chơi bằng ngón tay đã chai sạn sáu mươi năm, và khán giả Nhật — những người tôn thờ truyền thống — cúi đầu kính trọng.

Tour thành công vượt kỳ vọng: mười nghìn vé bán hết, doanh thu bốn tỷ đồng, và lời mời biểu diễn tại Berlin Philharmonie, Carnegie Hall, và Sydney Opera House."""),

("Chương 6: Vietnam Philharmonic Thành Huyền Thoại", """Hai năm sau ngày thành lập, Vietnam Philharmonic có trụ sở riêng tại Hà Nội, tám mươi nhạc công chính thức, và lịch biểu diễn bốn mươi concert mỗi năm — bao gồm mười hai concert miễn phí cho cộng đồng.

Bảo soạn thêm ba bản giao hưởng: "Mekong," "Hoàng Thành," và "Trường Sơn" — mỗi bản kết hợp nhạc cụ dân tộc khác nhau. Đĩa nhạc "Vietnamese Symphonies" do Deutsche Grammophon phát hành, lọt top 10 Billboard Classical Chart — lần đầu tiên cho một nghệ sĩ Đông Nam Á."""),

("Chương 7: Ông Tâm Và Đàn Bầu Cuối Cùng", """Một đêm, sau concert tại Seoul, ông Tâm gọi Bảo lại.

"Cháu, ông già rồi. Ngón tay ông bắt đầu run. Nhưng trước khi ông không chơi được nữa, ông muốn tặng cháu thứ này."

Ông Tâm đưa cho Bảo một cuốn sổ cũ — bản ghi chép tay bảy mươi hai làn điệu đàn bầu cổ từ thế kỷ XIX, được ông nội ông Tâm ghi lại. Nhiều làn điệu đã thất truyền hoàn toàn.

"Ông nội ông là nghệ nhân đàn bầu cung đình Huế. Mấy làn điệu này chỉ có trong cuốn sổ này. Ông trao cho cháu — hãy biến chúng thành giao hưởng."

Bảo ôm cuốn sổ, mắt rưng rưng. Bảy mươi hai làn điệu cổ — kho báu âm nhạc vô giá.

Anh soạn bản giao hưởng "Cung Đình" dựa trên mười hai làn điệu cổ nhất, và ra mắt tại UNESCO Heritage Concert tại Paris."""),

("Chương 8: Dàn Nhạc Quốc Gia Sụp Đổ", """Nhà hát Lớn ngày càng vắng khán giả. Dàn nhạc quốc gia dưới sự chỉ huy của Khải chơi nhạc an toàn, nhàm chán — Beethoven, Tchaikovsky, Dvorak lặp đi lặp lại mà không có sáng tạo.

Nhà tài trợ Hàn Quốc rút vốn vì doanh thu bán vé quá thấp. Khải bị sa thải. Nghĩa bị cách chức Giám đốc vì quản lý yếu kém.

Dàn nhạc quốc gia mời Bảo trở lại với tư cách nhạc trưởng khách mời. Anh đồng ý — nhưng với điều kiện: đàn bầu phải có ghế chính thức trong dàn nhạc.

Lần đầu tiên trong lịch sử, đàn bầu được liệt kê là nhạc cụ chính thức của dàn nhạc giao hưởng quốc gia."""),

("Chương 9: Grammy Đề Cử", """Đĩa nhạc "Vietnamese Symphonies Vol. 2" được đề cử Grammy hạng mục Best Orchestral Performance — lần đầu tiên cho một dàn nhạc châu Á.

Bảo bay đến Los Angeles, ngồi giữa các nhạc trưởng huyền thoại: Gustavo Dudamel, Yannick Nézet-Séguin, và Mirga Gražinytė-Tyla.

Vietnam Philharmonic không thắng Grammy năm đó, nhưng đề cử đã là lịch sử. Ông Tâm, xem từ Hà Nội qua livestream, mỉm cười: "Đàn bầu đã đến Grammy. Ông chết cũng mãn nguyện rồi." """),

("Chương 10: Concert Cuối Cùng Của Ông Tâm", """Sáu tháng sau Grammy, ông Tâm yếu dần. Bảy mươi bốn tuổi, ngón tay run, nhưng ông vẫn muốn chơi một concert cuối cùng.

Vietnam Philharmonic tổ chức concert đặc biệt tại Hoàng Thành Thăng Long — di sản UNESCO — dành riêng cho ông Tâm. Năm nghìn khán giả, truyền hình trực tiếp.

Ông Tâm solo đàn bầu chương cuối "Cung Đình" — khúc nhạc mà ông nội ông chơi cho Hoàng đế cuối cùng của triều Nguyễn. Ngón tay ông run, nhưng mỗi nốt nhạc vẫn trong veo, vẫn chạm đến tận cùng tâm hồn.

Khi nốt cuối vang lên, năm nghìn người đứng dậy. Bảo quay sang, cúi mình trước ông cụ — người nghệ nhân đã giữ đàn bầu sống qua sáu thập kỷ.

Ông Tâm nhìn Bảo, mỉm cười, đặt tay lên đàn bầu: "Ông giao đàn cho cháu rồi. Cháu chơi tiếp."

Hai tháng sau, ông Tâm mất. Bảo chơi đàn bầu trong lễ tang ông — khúc nhạc cuối cùng ông Tâm dạy: "Hát Ru" — khúc hát mà bà mẹ Việt Nam nào cũng thuộc.

Cây đàn bầu của ông Tâm giờ nằm trên sân khấu Vietnam Philharmonic, bên cạnh ghế nhạc trưởng. Mỗi concert, Bảo nhìn nó trước khi giơ đũa — nhớ ông cụ, nhớ âm nhạc, nhớ rằng: truyền thống không bao giờ chết, nó chỉ chờ người đúng để tái sinh."""),
]

# ═══════════════════════════════════════════════════════════════════════════════
# STORY 8: KỸ SƯ ĐỊA CHẤT
# ═══════════════════════════════════════════════════════════════════════════════

S8_TITLE = "BỊ CƯỚP QUYỀN KHAI THÁC MỎ, TÔI DÙNG BẢN ĐỒ ĐỊA CHẤT CỔ LẬT KÈO THÂU TÓM CẢ VÙNG KHOÁNG SẢN"
S8_AUTHOR = "Hoàng Minh Đạt"
S8_COVER = "base_cover_42.png"
S8_INTRO = """<p><strong>"Mười năm tôi đi khắp Tây Bắc, khoan hàng trăm mũi khoan thăm dò, tìm ra mỏ đất hiếm lớn nhất Đông Nam Á. Đổi lại, chủ mỏ cấu kết quan chức cướp giấy phép, đuổi tôi khỏi vùng mỏ giữa đêm mưa rừng."</strong></p>
<p>Hoàng Minh Đạt, kỹ sư địa chất tài năng nhất ngành khoáng sản Việt Nam, bị chủ mỏ Trần Quốc Vương và Phó GĐ Sở TNMT Lý Hữu Phước cấu kết cướp trắng quyền khai thác mỏ đất hiếm mà anh phát hiện.</p>
<p>Mất mỏ, mất sự nghiệp, Đạt tìm thấy trong tay bản đồ địa chất cổ do ông nội — một nhà địa chất thời Pháp — để lại. Bản đồ dẫn anh đến mỏ đất hiếm thứ hai, lớn gấp ba lần, và là vũ khí lật kèo thâu tóm toàn bộ vùng khoáng sản Tây Bắc.</p>"""

S8_CHAPTERS = [
("Chương 1: Mỏ Đất Hiếm Và Cú Phản Bội", """Bản Phúc, Bắc Yên, Sơn La, bốn giờ sáng. Hoàng Minh Đạt nằm trong lều vải bạt giữa rừng già, mưa rừng xối xả. Bên cạnh anh là hai mươi mẫu đá lõi khoan — kết quả của mũi khoan thăm dò thứ ba trăm bảy mươi tám.

Anh rọi đèn pin lên mẫu đá, tim đập dồn. Hàm lượng neodymium ba phần trăm, cerium năm phần trăm, lanthanum bốn phần trăm — cao gấp ba lần ngưỡng khai thác thương mại. Mỏ đất hiếm lớn nhất từng được phát hiện tại Đông Nam Á.

Đất hiếm — nguyên liệu không thể thiếu cho xe điện, điện thoại, vệ tinh, vũ khí — hiện do Trung Quốc kiểm soát chín mươi phần trăm sản lượng toàn cầu. Mỏ này có thể thay đổi cán cân địa chính trị.

Đạt gọi cho Trần Quốc Vương, Giám đốc Công ty Khoáng sản Tây Bắc — người thuê anh làm kỹ sư thăm dò suốt mười năm.

"Anh Vương, em tìm thấy rồi! Mỏ đất hiếm tại Bản Phúc, trữ lượng ước tính năm trăm nghìn tấn oxide, giá trị có thể lên đến mười nghìn tỷ đồng!"

Vương bay từ Hà Nội đến Sơn La ngay sáng hôm sau, cùng Phó GĐ Sở TNMT tỉnh Lý Hữu Phước — "người bạn thân" mà Vương luôn mang theo mỗi khi liên quan đến giấy phép khai thác.

Ba người đứng trên đỉnh đồi nhìn xuống vùng mỏ, mưa đã tạnh, nắng sớm chiếu vàng rừng già. Vương vỗ vai Đạt: "Giỏi lắm, em! Mười năm không uổng!"

Hai tuần sau, Đạt nhận thông báo: giấy phép thăm dò mỏ Bản Phúc được cấp cho... Công ty TNHH Phước Vương Minerals — công ty mới thành lập bởi Vương và Phước, không có tên Đạt.

"Anh Vương, em là người phát hiện mỏ! Trong hợp đồng em ký, điều khoản 12 ghi rõ kỹ sư thăm dò được hưởng năm phần trăm quyền lợi khai thác!"

Vương cười nhạt: "Đạt ơi, hợp đồng đó ký với Công ty Khoáng sản Tây Bắc, không phải Phước Vương Minerals. Đây là công ty mới, hợp đồng cũ không áp dụng."

"Anh lập công ty mới chỉ để xóa hợp đồng của em?"

"Kinh doanh là kinh doanh, Đạt. Em là kỹ sư giỏi, nhưng em không hiểu luật chơi." Vương ném phong bì trên bàn — bốn mươi triệu đồng. "Tiền công mười năm. Nhận rồi đi."

Đêm đó, xe Đạt bị chặn ở cổng vùng mỏ bởi nhóm bảo vệ Phước Vương. Anh bị tống ra khỏi khu vực, hành lý ném xuống đường, giữa mưa rừng Tây Bắc lạnh buốt.

Đạt đứng bên đường, mưa xối lên lưng, tay siết chặt cuốn sổ thăm dò — cuốn sổ chứa mười năm dữ liệu khoan, bản đồ địa chất, và phân tích khoáng vật mà không ai sao chép được vì ở trong đầu anh.

"Vương, mày cướp một mỏ. Nhưng Tây Bắc không chỉ có một mỏ." """),

("Chương 2: Bản Đồ Địa Chất Cổ", """Đạt trở về Hà Nội, ở nhờ nhà mẹ già tại phố Hàng Bạc. Mẹ anh, bà Hoàng Thị Mai, bảy mươi tuổi, bán phở sáng ở đầu ngõ.

Một đêm, Đạt lục tìm trong kho đồ cũ của ông nội — Hoàng Văn Khánh, kỹ sư địa chất tốt nghiệp Đại học Mỏ Paris năm 1952, một trong những nhà địa chất đầu tiên của Việt Nam.

Trong chiếc rương gỗ phủ bụi, Đạt tìm thấy: một bản đồ địa chất vẽ tay trên giấy da, niên đại 1954, ghi chú bằng tiếng Pháp và tiếng Việt. Bản đồ chi tiết vùng Tây Bắc, đánh dấu bảy vị trí "anomalie géochimique" — bất thường địa hóa.

Bản Phúc — mỏ mà Đạt vừa bị cướp — là vị trí số ba trên bản đồ. Nhưng vị trí số một — được ông nội đánh dấu bằng ngôi sao đỏ và dòng chữ "gisement exceptionnel" (mỏ đặc biệt) — nằm ở một thung lũng hẻo lánh tại Mường La, cách Bản Phúc năm mươi cây số về phía bắc.

Nếu ông nội đúng, mỏ ở Mường La có thể lớn hơn Bản Phúc nhiều lần.

Đạt cần tiền để thăm dò. Anh tìm đến Nguyễn Phương Dung, bốn mươi tuổi, CEO của một startup khoáng sản xanh, người mà anh quen tại một hội thảo ngành mỏ.

Dung nghe kế hoạch, xem bản đồ cổ, và quyết định trong mười phút: "Tôi đầu tư năm tỷ cho thăm dò. Nếu mỏ có thật, chúng ta fifty-fifty."

Đạt khoanh vùng mỏ Mường La, nộp hồ sơ xin giấy phép thăm dò. Phước ở Sở TNMT tìm mọi cách cản — nhưng mỏ Mường La thuộc tỉnh Lai Châu, ngoài quyền hạn của Phước tại Sơn La."""),

("Chương 3: Mỏ Thứ Hai — Lớn Gấp Ba Lần", """Ba tháng khoan thăm dò tại Mường La, bốn mươi mũi khoan. Kết quả: mỏ đất hiếm trữ lượng ước tính một triệu năm trăm nghìn tấn oxide — lớn gấp BA lần Bản Phúc.

Đạt trình bày kết quả tại hội nghị của Tổng cục Địa chất và Khoáng sản, trước sự chứng kiến của Bộ trưởng Bộ TNMT. Các chuyên gia quốc tế từ USGS (Cục Khảo sát Địa chất Mỹ) xác nhận: đây là một trong mười mỏ đất hiếm lớn nhất thế giới.

Tin tức lan nhanh như lửa. Reuters, Bloomberg, Financial Times đồng loạt: "Vietnam discovers massive rare earth deposit — could challenge China's monopoly."

Vương ngồi tại văn phòng Phước Vương Minerals, đọc tin, mặt trắng bệch. Mỏ Bản Phúc mà hắn cướp được — giờ trở nên nhỏ bé trước mỏ Mường La. Và người phát hiện mỏ mới chính là kỹ sư mà hắn đuổi."""),

("Chương 4: Thanh Tra Và Vả Mặt", """Phát hiện mỏ Mường La kéo theo cuộc thanh tra toàn diện ngành khoáng sản Tây Bắc. Thanh tra Chính phủ vào cuộc, phát hiện: giấy phép mỏ Bản Phúc được Phó GĐ Sở Phước cấp sai quy trình, vi phạm Luật Khoáng sản.

Đạt nộp hồ sơ tố cáo kèm bằng chứng: email nội bộ giữa Vương và Phước bàn kế hoạch lập công ty mới để xóa quyền lợi của Đạt, và biên lai chuyển tiền hai tỷ đồng từ Vương cho Phước.

Giấy phép Bản Phúc bị thu hồi. Phước bị cách chức. Vương bị khởi tố.

Tại phiên tòa sơ thẩm, khi Đạt bước vào phòng xử với tư cách bị hại, Vương nhìn anh bằng ánh mắt hận thù.

"Vương, anh cướp của tôi một mỏ, nhưng tôi tìm được mỏ lớn hơn," Đạt nói trước tòa. "Anh cướp được tài nguyên, nhưng không cướp được tài năng." """),

("Chương 5: Hợp Đồng Quốc Tế", """Mỏ Mường La thu hút sự chú ý quốc tế. Bộ Ngoại giao Mỹ, EU, và Nhật Bản liên hệ Việt Nam — đất hiếm là tài nguyên chiến lược, các cường quốc đều muốn giảm phụ thuộc Trung Quốc.

Đạt và Dung thành lập VietRare Earth Corp, ký hợp đồng hợp tác khai thác với Toyota Tsusho (Nhật) và Lynas Rare Earth (Úc) — hai tập đoàn đất hiếm lớn nhất ngoài Trung Quốc. Tổng đầu tư: năm nghìn tỷ đồng.

Đạt đàm phán với điều kiện: sáu mươi phần trăm cổ phần thuộc Việt Nam, công nghệ chế biến phải được chuyển giao cho kỹ sư Việt, và nhà máy phải đặt tại Tây Bắc để tạo việc làm cho đồng bào."""),

("Chương 6: Đế Chế Khoáng Sản Ra Đời", """VietRare Earth Corp trở thành công ty khoáng sản chiến lược quốc gia. Nhà máy chế biến đất hiếm tại Mường La — hiện đại nhất Đông Nam Á — tuyển hai nghìn công nhân, chủ yếu là người dân tộc thiểu số địa phương.

Đạt thiết lập quy trình khai thác xanh: không xả thải ra sông, phục hồi rừng sau khai thác, và chia sẻ lợi nhuận với cộng đồng bản địa.

Doanh thu năm đầu: ba nghìn tỷ đồng. VietRare Earth được Forbes đánh giá là "startup khoáng sản có giá trị nhất Đông Nam Á." """),

("Chương 7: Di Sản Của Ông Nội", """Đạt mang bản đồ địa chất cổ đến Bảo tàng Địa chất Quốc gia, tặng làm hiện vật. Bản đồ được trưng bày cạnh ảnh ông nội — Hoàng Văn Khánh, người đã đi bộ khắp Tây Bắc trong những năm 1950 để vẽ bản đồ.

"Ông nội không sống đủ lâu để khai thác mỏ," Đạt nói trong buổi lễ trao tặng. "Nhưng bản đồ của ông đã chờ bảy mươi năm để tìm đúng người."

Mẹ Đạt đứng bên cạnh, mắt ướt. Bà nắm tay con trai, nhìn bức ảnh chồng trên tường bảo tàng — người đàn ông đã mất khi Đạt mới mười tuổi, để lại chiếc rương gỗ và tấm bản đồ."""),

("Chương 8: Vương Và Phước Sụp Đổ", """Tòa án tuyên: Trần Quốc Vương mười năm tù, Lý Hữu Phước tám năm tù. Tài sản phong tỏa, Phước Vương Minerals giải thể.

Mỏ Bản Phúc được nhà nước thu hồi và giao cho VietRare Earth quản lý — Đạt trở thành người quản lý cả hai mỏ.

Vương ngồi trong trại giam, nhìn ra cửa sổ hướng Tây Bắc — phía đó, núi rừng chứa kho báu đất hiếm mà hắn đã cướp rồi mất."""),

("Chương 9: Giải Thưởng Địa Chất Quốc Tế", """VietRare Earth Corp nhận giải "Excellence in Mineral Discovery" tại International Association of Geochemistry Conference ở Montreal. Đạt là nhà địa chất Đông Nam Á đầu tiên nhận giải.

"Tôi tìm mỏ đất hiếm này không phải vì tiền. Tôi tìm vì đó là nghề ông nội dạy: đọc đá, hiểu đất, và kể câu chuyện mà Trái Đất giấu dưới chân mình bốn tỷ năm."

Bài phát biểu được truyền trực tiếp về Việt Nam. Mẹ Đạt xem từ quán phở đầu ngõ Hàng Bạc, mắt đỏ hoe, tay vẫn cầm đôi đũa gắp phở cho khách."""),

("Chương 10: Quay Về Bản Phúc", """Một năm sau, Đạt quay lại Bản Phúc — nơi anh bị đuổi giữa đêm mưa. Nhà máy mới sáng đèn, xe tải chở quặng ra vào tấp nập. Anh đứng đúng vị trí ngày bị tống ra khỏi cổng.

"Anh Đạt!" Một người đàn ông chạy đến — người bảo vệ cũ đã xua đuổi anh năm trước, giờ là công nhân nhà máy. "Em xin lỗi anh. Hồi đó em không biết..."

"Không sao," Đạt cười. "Giờ em có công việc ổn định, lương tốt. Đó mới là quan trọng."

Đạt đi lên đỉnh đồi — nơi Vương vỗ vai anh nói "Giỏi lắm em!" rồi cướp mỏ. Anh nhìn xuống: hai nhà máy, hai mỏ, hai nghìn công nhân, ba nghìn tỷ doanh thu.

Tất cả bắt đầu từ một mẫu đá lõi khoan trong đêm mưa, và một tấm bản đồ bảy mươi năm tuổi.

Dung gọi điện: "Đạt, hội nghị với Toyota Tsusho tuần sau. Bay Tokyo sáng mai."

"Mười phút nữa. Cho tôi đứng đây mười phút."

Đạt nhắm mắt, nghe tiếng gió Tây Bắc lùa qua rừng già. Trong gió có tiếng ông nội thì thầm: "Đất không bao giờ nói dối, cháu ơi. Cứ đào, rồi sẽ thấy." """),
]

# ═══════════════════════════════════════════════════════════════════════════════
# ASSEMBLY & PUBLISHING (same pipeline as batch 01)
# ═══════════════════════════════════════════════════════════════════════════════

ALL_STORIES = [
    {"title": S5_TITLE, "author": S5_AUTHOR, "cover": S5_COVER, "intro": S5_INTRO, "chapters": S5_CHAPTERS},
    {"title": S6_TITLE, "author": S6_AUTHOR, "cover": S6_COVER, "intro": S6_INTRO, "chapters": S6_CHAPTERS},
    {"title": S7_TITLE, "author": S7_AUTHOR, "cover": S7_COVER, "intro": S7_INTRO, "chapters": S7_CHAPTERS},
    {"title": S8_TITLE, "author": S8_AUTHOR, "cover": S8_COVER, "intro": S8_INTRO, "chapters": S8_CHAPTERS},
]

def build_all():
    novels = []
    for s in ALL_STORIES:
        chapters = []
        total = 0
        for title, raw in s["chapters"]:
            html = fmt(raw)
            c = html.count("<p>")
            total += c
            chapters.append({"title": title, "content": html})
        novels.append({
            "title": s["title"], "author": s["author"], "genre": "Sảng Văn",
            "intro": s["intro"], "chapters": chapters, "cover_base": s["cover"],
            "_stats": f"{len(chapters)} chapters, {total} sentences"
        })
        log(f"✓ {s['title'][:50]}... — {total} sentences")
    return novels

def get_ftp():
    for i in range(5):
        try:
            ftp = ftplib.FTP(FTP_HOST, timeout=60)
            ftp.login(FTP_USER, FTP_PASS)
            return ftp
        except Exception as e:
            log(f"FTP retry {i+1}: {e}")
            time.sleep(5*(i+1))
    raise Exception("FTP failed")

def publish_all(novels):
    log("🚀 BATCH 2 LIVE PUBLISH — 4 STORIES (5-8)")
    ftp = get_ftp()
    with open(os.path.join(BASE_DIR, "publish_novel.php"), "rb") as f:
        ftp.storbinary("STOR publish_novel.php", f)
    ftp.quit()
    log("✓ Helper uploaded")

    results = []
    for i, n in enumerate(novels):
        log(f"\n{'='*60}\n📖 PUBLISHING {i+1}/4: {n['title'][:50]}...\n{'='*60}")
        cover_file = ""
        base = os.path.join(BASE_DIR, n["cover_base"])
        if os.path.exists(base):
            out = os.path.join(BASE_DIR, "pending_cover.png")
            cmd = ["python3", os.path.join(BASE_DIR, "cover_overlay_standard.py"),
                   "--input", base, "--output", out, "--title", n["title"],
                   "--subtitle", f"Sảng văn của {n['author']}"]
            r = subprocess.run(cmd, capture_output=True, text=True)
            if r.returncode == 0 and os.path.exists(out):
                rid = random.randint(100000,999999)
                cover_file = f"cover_sideload_{rid}.png"
                ftp = get_ftp(); ftp.cwd("wp-content/uploads")
                with open(out,"rb") as cf: ftp.storbinary(f"STOR {cover_file}", cf)
                ftp.quit(); os.remove(out)
                log(f"✓ Cover uploaded: {cover_file}")

        payload = {"secret_token": SECRET_TOKEN, "title": n["title"], "intro": n["intro"],
                   "author": n["author"], "genre": "Sảng Văn", "chapters": n["chapters"]}
        if cover_file: payload["cover_local_filename"] = cover_file

        try:
            res = requests.post(f"{WP_URL}/publish_novel.php", json=payload, timeout=300).json()
            if res.get("success"):
                log(f"🎉 Published! ID={res['story_id']}, chapters={res['chapters_count']}")
                results.append({"id": res["story_id"], "title": n["title"]})
                reg_path = os.path.join(BASE_DIR, "existing_novels.json")
                reg = json.load(open(reg_path,"r",encoding="utf-8")) if os.path.exists(reg_path) else []
                reg.append({"id": res["story_id"], "title": n["title"], "slug": n["title"].lower().replace(" ","-"), "intro": n["intro"]})
                json.dump(reg, open(reg_path,"w",encoding="utf-8"), ensure_ascii=False, indent=2)
            else:
                log(f"❌ API Error: {res}")
        except Exception as e:
            log(f"❌ Exception: {e}")
        time.sleep(5)

    try:
        ftp = get_ftp(); ftp.delete("publish_novel.php"); ftp.quit()
    except: pass

    log(f"\n🏁 BATCH 2 COMPLETE: {len(results)}/4 published")
    for r in results: log(f"  → ID {r['id']}: {r['title'][:60]}")

if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--live", action="store_true")
    a = p.parse_args()
    if not a.dry_run and not a.live:
        print("Use --dry-run or --live"); sys.exit(1)
    novels = build_all()
    if a.dry_run:
        print(f"\n{'='*60}\n🔬 DRY-RUN: {len(novels)} stories\n{'='*60}")
        for n in novels:
            print(f"\n📖 {n['title']}")
            print(f"   ✍️ {n['author']} | 📊 {n['_stats']}")
            for ch in n["chapters"]:
                print(f"   → {ch['title']} ({ch['content'].count('<p>')} sentences)")
    elif a.live:
        publish_all(novels)
