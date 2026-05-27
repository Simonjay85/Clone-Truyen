#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
write_batch_mix_02.py — Batch 2: 5 Truyện Sảng Văn CẢI TIẾN (Stories 6-10)
===========================================================================
Số chương random: 8-13 tùy cốt truyện
Story 6: Giảng viên bị ép nghỉ (9 ch) — cover 9
Story 7: Thợ đồng hồ luxury VN (11 ch) — cover 10
Story 8: Nữ phóng viên điều tra (8 ch) — cover 11
Story 9: Thuyền trưởng bị vu oan (10 ch) — cover 12
Story 10: Nghệ nhân gốm (12 ch) — cover 13
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
    abbrevs = ["TS.", "BS.", "PGS.", "GS.", "CEO.", "CFO.", "CTO.", "Dr.", "Mr.", "Mrs.", "Ph.D.", "HĐQT.", "IPO.", "PCCC.", "KTS.", "NFT.", "USD.", "MBA.", "IELTS.", "TOEIC."]
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
# STORY 6: GIẢNG VIÊN BỊ ÉP NGHỈ — 9 CHƯƠNG
# ═══════════════════════════════════════════════════════════════════════════════

S6_TITLE = "BỊ ÉP NGHỈ VÌ DẠY GIỎI HƠN TRƯỞNG KHOA, TÔI MỞ HỌC VIỆN ONLINE KHIẾN CẢ KHOA MẤT SINH VIÊN"
S6_AUTHOR = "Lý Minh Châu"
S6_COVER = "base_cover_9.png"
S6_INTRO = """<p><strong>"Tám năm tôi cống hiến cho khoa Kinh tế, giúp sinh viên đạt giải quốc gia, nâng xếp hạng khoa lên top 5. Đổi lại, trưởng khoa ép tôi nghỉ vì sinh viên yêu cầu tôi dạy thay ông ta."</strong></p>
<p>Lý Minh Châu, giảng viên kinh tế vi mô xuất sắc nhất Đại học Thương mại Hà Nội, bị PGS Trần Đức Mạnh — trưởng khoa Kinh tế — ép nghỉ việc vì ghen tị.</p>
<p>Mất giảng đường, Châu mở học viện online miễn phí, thu hút hàng trăm nghìn sinh viên, và chứng minh rằng giáo dục tốt không cần tường gạch — chỉ cần tâm huyết.</p>"""

S6_CHAPTERS = [
("Chương 1: Kiến Nghị Sinh Viên", """Lý Minh Châu đọc lá thư kiến nghị của lớp K62 — năm mươi bảy chữ ký — yêu cầu nhà trường cho cô dạy môn Kinh tế vĩ mô thay PGS Trần Đức Mạnh. Lý do: "Cô Châu giảng dễ hiểu hơn, bài tập thực tế hơn, và cô trả lời tin nhắn hỏi bài lúc mười một giờ đêm."

Lá thư này đáng lẽ phải khiến ban giám hiệu vui — sinh viên yêu quý giảng viên là điều tốt. Nhưng PGS Mạnh không nghĩ vậy.

Ba ngày sau lá thư, Châu bị triệu tập lên phòng trưởng khoa. PGS Mạnh ngồi sau bàn gỗ lớn, cặp kính gọng vàng hơi tuột trên sống mũi, giọng ông ta ngọt nhạt: "Châu à, trường đang restructure nhân sự giảng viên. Khoa mình phải cắt giảm một vị trí hợp đồng."

"Em là giảng viên rating cao nhất khoa, anh Mạnh. Rating sinh viên đánh giá 4.9/5 suốt tám năm liên tiếp."

"Rating không phải tiêu chí duy nhất." Ông ta xoay bút trên tay. "Cô chưa có học hàm PGS, chưa có bài báo ISI Q1, và quan trọng nhất — cô dạy một cách quá 'giải trí,' thiếu tính hàn lâm. Sinh viên thích cô vì cô vui, không phải vì cô giỏi."

Châu nhìn thẳng vào mắt ông ta. Cô biết sự thật: PGS Mạnh có bài báo ISI — nhưng không ai trích dẫn. PGS Mạnh có học hàm — nhưng sinh viên ngủ gục trong giờ ông dạy. PGS Mạnh có chức vụ — nhưng không có tâm.

"Anh đuổi em vì lá thư kiến nghị."

"Tôi cắt giảm nhân sự vì ngân sách. Và cô nên biết — nếu cô phản đối, tôi sẽ đưa hồ sơ cô ra hội đồng kỷ luật vì tội 'dạy sai chương trình khung.'"

Châu đứng dậy, cầm quyết định sa thải, bước ra ngoài hành lang. Sinh viên đi ngang nhìn cô lo lắng — tin đồn đã lan khắp khoa."""),

("Chương 2: Học Viện Online — Bắt Đầu Từ Phòng Ngủ", """Châu về nhà, mở laptop, lập kênh YouTube "Kinh Tế Với Châu." Video đầu tiên quay trong phòng ngủ, bảng trắng dán tường, marker ba màu.

"Xin chào, mình là Lý Minh Châu, cựu giảng viên kinh tế. Hôm nay mình giảng Supply-Demand bằng ví dụ bún bò Huế — vì kinh tế học không nên buồn chán."

Video đầu tiên: hai trăm nghìn lượt xem trong tuần đầu. Comments tràn ngập: "Cô ơi, sao trường đuổi cô?" "Học với cô trên YouTube thích hơn đi học!"

Châu upload hai video mỗi tuần. Ba tháng: một triệu subscribers. Nội dung: kinh tế vi mô, vĩ mô, tài chính cá nhân — tất cả miễn phí, giải thích bằng ví dụ đời thường Việt Nam.

Forbes Vietnam viết bài: "'Cô giáo YouTube' Lý Minh Châu — giảng viên bị đuổi trở thành hiện tượng giáo dục online." """),

("Chương 3: PGS Mạnh Phản Công", """PGS Mạnh tức giận khi thấy Châu nổi tiếng. Ông ta kiện Châu: "sử dụng tài liệu giảng dạy của trường cho mục đích thương mại."

Đồng thời, ông ta chỉ đạo khoa gửi công văn cảnh cáo sinh viên: "Không được chia sẻ hay quảng bá kênh YouTube của cá nhân không thuộc hệ thống giảng viên chính thức."

Sinh viên lập petition online phản đối — mười nghìn chữ ký trong ba ngày. Hashtag #FreeCôChâu trending trên Twitter Việt Nam.

Châu không phản bác trực tiếp. Cô quay video mới: "Kinh tế học về quyền lực — khi người có quyền sợ người có tri thức." Video đạt năm triệu lượt xem."""),

("Chương 4: Phát Hiện Gian Lận Nghiên Cứu", """Twist: trong quá trình chuẩn bị bào chữa tại tòa, luật sư Châu phát hiện: bài báo ISI Q1 duy nhất của PGS Mạnh — bài báo giúp ông ta thăng chức PGS — có dấu hiệu đạo văn. Turnitin check: trùng lặp bốn mươi hai phần trăm với một bài báo của nghiên cứu sinh Ấn Độ đăng trước đó hai năm.

Châu gửi report cho Hội đồng Giáo sư Nhà nước. Điều tra: PGS Mạnh đã tự đạo văn và gian lận chỉ số trích dẫn bằng cách nhờ đồng nghiệp trích dẫn chéo giả tạo.

"Ông ấy đuổi tôi vì thiếu ISI Q1. Nhưng ISI Q1 duy nhất của ông ấy là đạo văn," Châu nói trong phỏng vấn VTV."""),

("Chương 5: Học Viện MinhChâu Academy Chính Thức", """Châu nâng cấp kênh YouTube thành MinhChâu Academy — nền tảng học trực tuyến miễn phí, kết hợp video, quiz, và mentoring.

Google.org tài trợ năm trăm nghìn đô. Quỹ Vingroup hỗ trợ hạ tầng server. Hai triệu sinh viên đăng ký trong năm đầu — gấp mười lần tổng sinh viên Đại học Thương mại.

Đặc biệt: MinhChâu Academy mời các giảng viên trẻ bị đánh giá thấp tại các trường đại học — cùng nhau giảng dạy online. "Giáo dục không cần biên chế — chỉ cần đam mê," Châu nói."""),

("Chương 6: Mẹ Và Chiếc Bảng Phấn", """Châu dạy vì mẹ. Bà Lý Thị Hạnh, giáo viên tiểu học ở Thái Bình — lương ba triệu, dạy hai ca, về nhà vẫn soạn bài.

"Mẹ ơi, sao lương ít thế mà mẹ vẫn dạy?"

"Vì mai kia có đứa học trò thành người tốt, mẹ sẽ tự hào. Lương ít nhưng tự hào nhiều, con ạ."

Châu mang triết lý đó lên YouTube: dạy miễn phí, dạy vì tự hào, không vì tiền. Logo MinhChâu Academy là hình chiếc bảng phấn — bảng phấn cũ kỹ của lớp học mẹ ở Thái Bình."""),

("Chương 7: PGS Mạnh Bị Tước Học Hàm — Climax", """Hội đồng Giáo sư Nhà nước ra quyết định: tước học hàm PGS của Trần Đức Mạnh vì "đạo văn nghiêm trọng và gian lận chỉ số trích dẫn." Ông ta bị miễn nhiệm chức trưởng khoa.

Tại buổi công bố, Mạnh xin nói một câu: "Tôi hối hận vì đã đuổi Lý Minh Châu."

Châu không có mặt. Cô đang quay video bài giảng mới — "Kinh tế học về sự tha thứ" — bài giảng hay nhất cô từng dạy."""),

("Chương 8: TEDx Và Hai Triệu Sinh Viên", """Châu được mời nói chuyện tại TEDxHanoi: "Giáo dục trong thời đại bị đuổi việc."

"Tôi bị đuổi vì dạy tốt. Nghe vô lý nhưng nó xảy ra hàng ngày — khi hệ thống coi trọng chức vụ hơn chất lượng. Nhưng internet là giảng đường không ai có thể đuổi bạn ra khỏi."

Standing ovation. Video TEDx đạt mười triệu lượt xem, dịch sang sáu ngôn ngữ."""),

("Chương 9: Quay Về Trường — Nhưng Khác", """Đại học Thương mại mời Châu quay lại — lần này với chức danh "Giảng viên thỉnh giảng danh dự." Châu từ chối vị trí fulltime, nhưng đồng ý giảng một lớp mỗi kỳ.

Buổi giảng đầu tiên khi quay lại, giảng đường chật kín — sinh viên ngồi cả hành lang. Châu cầm marker, viết lên bảng: "Supply = Demand," rồi quay sang sinh viên:

"Chào các em, cô quay lại rồi. Hôm nay mình học kinh tế bằng ví dụ bún bò Huế nhé."

Cả giảng đường vỗ tay.

Mẹ Châu ở Thái Bình xem livestream buổi giảng, gọi điện: "Con dạy hay quá. Mẹ tự hào."

"Con cũng tự hào vì mẹ, mẹ ạ." """),
]

# ═══════════════════════════════════════════════════════════════════════════════
# STORY 7: THỢ ĐỒNG HỒ LUXURY VN — 11 CHƯƠNG
# ═══════════════════════════════════════════════════════════════════════════════

S7_TITLE = "BỊ KHINH LÀ THỢ SỬA ĐỒNG HỒ VỈA HÈ, TÔI CHẾ TẠO ĐỒNG HỒ LUXURY MADE IN VIETNAM KHIẾN THỤY SĨ PHẢI KINH NGẠC"
S7_AUTHOR = "Ngô Hải Sơn"
S7_COVER = "base_cover_10.png"
S7_INTRO = """<p><strong>"Mười lăm năm sửa đồng hồ vỉa hè, tay chai sạn, lưng còng vì cúi xuống bàn kính lúp. Khi tôi nói muốn chế tạo đồng hồ luxury Việt Nam, cả giới đồng hồ cười vào mặt tôi."</strong></p>
<p>Ngô Hải Sơn, thợ sửa đồng hồ vỉa hè phố Hàng Bông, bị giới đồng hồ và cả gia đình coi thường khi tuyên bố sẽ chế tạo đồng hồ cơ luxury thương hiệu Việt Nam.</p>
<p>Từ vỉa hè Hà Nội đến Basel World — hội chợ đồng hồ lớn nhất thế giới — Sơn chứng minh rằng đôi bàn tay Việt Nam có thể tạo ra kiệt tác ngang tầm Thụy Sĩ.</p>"""

S7_CHAPTERS = [
("Chương 1: Tiếng Cười Của Giới Đồng Hồ", """Ngô Hải Sơn ngồi trên chiếc ghế nhựa thấp ở góc phố Hàng Bông, bàn sửa đồng hồ là một chiếc bàn gỗ cũ rộng năm mươi phân. Kính lúp gắn trên trán, nhíp trong tay, và hàng trăm linh kiện nhỏ li ti nằm trên khay nhung đen.

Mười lăm năm, Sơn sửa mọi loại đồng hồ — từ đồng hồ Casio sinh viên đến Rolex Submariner của đại gia. Tay anh quen thuộc với từng loại movement: ETA 2824, Miyota 9015, Seiko 4R36 — anh biết rõ từng bánh răng, từng lò xo, từng viên ruby.

Một ngày, khách hàng mang chiếc Patek Philippe Calatrava đến sửa. Sơn tháo ra, nhìn movement 324 SC — 213 linh kiện, finish bằng tay, Côtes de Genève decoration. Đẹp đến nín thở.

"Một ngày nào đó, tôi sẽ làm ra movement đẹp như thế này," Sơn nói với khách hàng.

Khách hàng — một doanh nhân đeo suit đắt tiền — cười khẩy: "Anh à, Thụy Sĩ mất năm trăm năm để làm được Patek. Việt Nam? Việt Nam chỉ bán đồng hồ giả ở Bến Thành thôi."

Sơn im lặng, trả đồng hồ, thu hai trăm nghìn tiền công sửa. Nhưng câu nói đó anh nhớ mãi — không phải vì đau, mà vì nó đúng. Việt Nam chưa có thương hiệu đồng hồ cơ luxury nào."""),

("Chương 2: Nghiên Cứu Trong Gian Bếp", """Sơn bắt đầu nghiên cứu chế tạo movement đồng hồ cơ trong gian bếp mười mét vuông của căn nhà trọ. Anh mua máy tiện CNC mini secondhand từ Nhật — ba mươi triệu, vay nóng — để gia công bánh răng.

Tám tháng thất bại. Bánh răng không đủ chính xác — sai số 0.02mm, trong khi Thụy Sĩ đạt sai số 0.005mm. Lò xo mainspring quá yếu — đồng hồ chạy được bốn tiếng rồi chết.

"Mày bỏ cái trò điên đó đi." Vợ Sơn — chị Lan — nói khi thấy anh thức đến ba giờ sáng mài bánh răng. "Mày sửa đồng hồ kiếm ngày ba trăm nghìn, nuôi hai đứa con, đừng mơ mộng nữa."

"Anh không mơ. Anh đang làm."

Lan thở dài, pha cho anh ly cà phê, rồi đi ngủ. Sơn uống cà phê, cầm nhíp, tiếp tục mài bánh răng thứ sáu trăm."""),

("Chương 3: Prototype Đầu Tiên — 'Sơn Hà Một'", """Mười bốn tháng sau, Sơn hoàn thành prototype movement đầu tiên: SH-01, viết tắt "Sơn Hà." 127 linh kiện, power reserve 38 giờ, sai số +/- 12 giây/ngày.

So với Thụy Sĩ? Tệ. Sai số cao gấp ba lần. Finish thô. Nhưng nó chạy. Movement đồng hồ cơ đầu tiên hoàn toàn made in Vietnam — chạy bằng lò xo, không pin.

Sơn đăng video trên YouTube: tay anh lắp ráp SH-01, từng bánh răng nhỏ xíu. Video đạt năm trăm nghìn lượt xem. Comments: "Anh ơi, Việt Nam mình làm được đồng hồ cơ rồi!" Nhưng cũng có: "Sai số 12 giây mà đòi luxury? Đừng mơ."

Sơn đọc cả hai loại comment, gật đầu, rồi bắt đầu làm SH-02."""),

("Chương 4: Ông Thầy Từ Nhật Bản", """Qua YouTube, Sơn được Nakamura Kenji — nghệ nhân đồng hồ bậc thầy người Nhật, cựu kỹ sư Grand Seiko — liên hệ.

"Tôi xem video của anh. Tay nghề tốt nhưng thiếu kỹ thuật finishing. Tôi muốn dạy anh — miễn phí."

Nakamura bay sang Hà Nội, ở nhà trọ Sơn hai tuần. Ông dạy Sơn kỹ thuật Zaratsu polishing — cách đánh bóng mặt phẳng hoàn hảo mà Grand Seiko nổi tiếng. Dạy cách điều chỉnh hairspring để giảm sai số. Dạy triết lý monozukuri — "tinh thần chế tạo."

"Sơn-san, anh có tay nghề của thợ bậc thầy. Nhưng anh cần kiên nhẫn — không phải kiên nhẫn ngày, mà kiên nhẫn năm."

Hai tuần đó thay đổi tất cả."""),

("Chương 5: SH-05 — Breakthrough", """Sau hai năm cải tiến liên tục, SH-05 ra đời: 168 linh kiện, power reserve 72 giờ, sai số +/- 3 giây/ngày — ngang ngửa movement ETA 2824 của Swatch Group Thụy Sĩ.

Và điều đặc biệt: SH-05 có decoration "Sóng Hồng" — hoa văn Côtes de Genève cải tiến, lấy cảm hứng từ sóng nước sông Hồng — nét vẽ bằng tay, không máy CNC.

Sơn gửi SH-05 đi kiểm định tại COSC (Contrôle Officiel Suisse des Chronomètres) — tổ chức kiểm định đồng hồ chính thức Thụy Sĩ.

Kết quả: ĐẠT chuẩn COSC chronometer. Movement đồng hồ Việt Nam đầu tiên đạt chuẩn Thụy Sĩ."""),

("Chương 6: Thương Hiệu 'SƠN HÀ' Ra Mắt", """Sơn thành lập thương hiệu đồng hồ "SƠN HÀ" — mỗi chiếc đồng hồ hoàn toàn handmade, giới hạn năm mươi chiếc mỗi năm. Giá: bốn mươi triệu/chiếc — cao cho Việt Nam, nhưng rẻ hơn đồng hồ Thụy Sĩ cùng cấp mười lần.

Bộ sưu tập đầu tiên: "Hà Nội 36 Phố" — mỗi chiếc có mặt số khắc laser hình một con phố cổ Hà Nội. Năm mươi chiếc sold out trong hai tuần — không cần quảng cáo.

Hodinkee — tạp chí đồng hồ uy tín nhất thế giới — viết bài: "Sơn Hà: The Vietnamese watchmaker who learned from the sidewalk."

Người doanh nhân khinh Sơn năm trước đặt mua chiếc số 01."""),

("Chương 7: Bố Và Chiếc Đồng Hồ Poljot", """Sơn theo nghề vì bố. Ông Ngô Văn Bảo, thợ sửa đồng hồ ở Hàng Bông trước Sơn — ba mươi năm trên cùng góc phố đó.

Bố tặng Sơn chiếc đồng hồ Poljot Liên Xô cũ khi Sơn mười tuổi: "Con giữ cái này. Đồng hồ cơ chạy bằng lò xo, không cần pin. Giống người thợ — chạy bằng ý chí."

Chiếc Poljot đó giờ nằm trong tủ kính showroom SƠN HÀ — hiện vật số 0, không bán."""),

("Chương 8: Những Kẻ Hoài Nghi Quay Lại", """Khi SƠN HÀ nổi tiếng, một số "chuyên gia" đồng hồ Việt Nam lên mạng tố: "SH-05 dùng linh kiện Trung Quốc gắn mác Việt Nam" và "Sơn chỉ là thợ lắp ráp, không phải chế tạo."

Sơn đáp bằng video mười lăm phút: quay cận cảnh toàn bộ quy trình chế tạo — từ thanh thép thô, tiện thành bánh răng, mài, polishing, đến lắp ráp — trong xưởng nhỏ ở Hà Nội. Mỗi bước ghi rõ ngày giờ, nhà cung cấp vật liệu Việt Nam.

"Tôi không giấu gì cả. Mỗi linh kiện có xuất xứ rõ ràng. Mời các anh đến xưởng xem trực tiếp."

Video đạt mười triệu lượt xem. Không ai tố nữa."""),

("Chương 9: Vợ Đeo Chiếc Đồng Hồ Đầu Tiên", """Chiếc đồng hồ SƠN HÀ đầu tiên — prototype, không bán — Sơn tặng vợ.

"Em à, em nói anh đừng mơ mộng. Nhưng cảm ơn em đã pha cà phê cho anh mỗi đêm khi anh mài bánh răng."

Lan — người vợ hay cằn nhằn nhưng chưa bao giờ bỏ cuộc — đeo chiếc đồng hồ, mắt ướt: "Anh ơi, nó đẹp quá. Nhưng nó nặng."

"Ừ, nặng. Vì nó chứa mười lăm năm vỉa hè trong đó."

Lan cười, ôm chồng."""),

("Chương 10: Baselworld — Sân Khấu Của Sơn", """SƠN HÀ được mời tham gia Baselworld — hội chợ đồng hồ lớn nhất thế giới tại Thụy Sĩ. Gian hàng nhỏ nhất hội chợ — bốn mét vuông — nhưng đông nhất.

Giám đốc Patek Philippe đến xem SH-05, gật đầu: "Impressive craftsmanship. Where did you learn?"

"On a sidewalk in Hanoi." Sơn trả lời.

Câu trả lời đó được The New York Times trích dẫn, thành headline: "He Learned Watchmaking on a Hanoi Sidewalk. Now He's at Baselworld." """),

("Chương 11: Quay Về Vỉa Hè", """Sơn quay về Hà Nội, về góc phố Hàng Bông. Anh không dọn bàn sửa đồng hồ vỉa hè — vẫn ngồi đó, vẫn sửa đồng hồ Casio cho sinh viên, vẫn thu hai trăm nghìn.

"Anh ơi, anh nổi tiếng rồi sao còn ngồi đây?"

"Vì tay tôi nhớ vỉa hè. Và vỉa hè nhớ tay tôi."

Buổi sáng, Sơn sửa đồng hồ cho khách. Buổi chiều, vào xưởng chế tạo SƠN HÀ. Buổi tối, dạy học trò — ba thanh niên muốn theo nghề — cách mài bánh răng.

Trên cổ tay Sơn, chiếc Poljot bố tặng vẫn chạy — tích tắc, tích tắc — bằng lò xo, bằng ý chí."""),
]

# ═══════════════════════════════════════════════════════════════════════════════
# STORY 8: NỮ PHÓNG VIÊN ĐIỀU TRA — 8 CHƯƠNG
# ═══════════════════════════════════════════════════════════════════════════════

S8_TITLE = "BỊ SA THẢI VÌ PHANH PHUI THAM NHŨNG, TÔI LẬP TÒA SOẠN ĐỘC LẬP KHIẾN CẢ HỆ THỐNG RÚT ĐƠN"
S8_AUTHOR = "Vũ Phương Nhi"
S8_COVER = "base_cover_11.png"
S8_INTRO = """<p><strong>"Sáu năm tôi theo đuổi phóng sự điều tra, phanh phui đường dây tham nhũng đất đai tại tỉnh H. Đổi lại, tổng biên tập giết bài, sa thải tôi, và giao nguồn tin cho bên bị điều tra."</strong></p>
<p>Vũ Phương Nhi, phóng viên điều tra tòa soạn Thời Đại, bị TBT Hoàng Bá Linh sa thải và phản bội nguồn tin vì tòa soạn nhận tiền bịt miệng từ doanh nghiệp tham nhũng.</p>
<p>Mất việc, bị đe dọa, Nhi lập tòa soạn độc lập và đăng phóng sự, buộc cả hệ thống phải xử lý.</p>"""

S8_CHAPTERS = [
("Chương 1: Bài Báo Bị Giết", """Vũ Phương Nhi nộp phóng sự điều tra dài mười hai nghìn từ — "Đất Đen Tỉnh H" — cho TBT Hoàng Bá Linh lúc năm giờ chiều thứ Sáu. Bài báo phơi bày đường dây cấp sổ đỏ giả cho ba mươi hecta đất nông nghiệp tại tỉnh H, liên quan đến Phó Chủ tịch tỉnh Nguyễn Đình Lộc và Tổng giám đốc Tập đoàn BĐS Hoàng Gia.

Sáu tháng điều tra. Ba mươi hai nguồn tin. Bản sao sổ đỏ giả, biên bản họp kín, và ghi âm cuộc gọi giữa PCT Lộc và TGĐ Hoàng Gia thỏa thuận "phí bôi trơn" hai mươi tỷ đồng.

TBT Linh đọc bài, mặt tái xanh, rồi gọi Nhi vào phòng: "Bài này không đăng được. Chưa đủ bằng chứng."

"Anh Linh, em có ba mươi hai nguồn tin, ghi âm, bản sao sổ đỏ..."

"TÔI NÓI KHÔNG ĐĂNG LÀ KHÔNG ĐĂNG." Linh đập tay xuống bàn. "Và từ hôm nay, cô bị chuyển sang mục Đời Sống. Không được tiếp cận bất kỳ hồ sơ điều tra nào nữa."

Ba ngày sau, Nhi bị sa thải. Lý do ghi trong quyết định: "Vi phạm quy trình tác nghiệp." Và tệ hơn: nguồn tin chính — anh Trần Văn Đạt, cán bộ địa chính tỉnh H — bị lộ danh tính và bị đe dọa."""),

("Chương 2: Tòa Soạn Trong Quán Cà Phê", """Nhi không bỏ cuộc. Cô lập "Tin Trong" — tòa soạn báo độc lập trên Substack — một mình viết, biên tập, đăng bài.

"Đất Đen Tỉnh H" đăng full text trên Tin Trong. Hai triệu lượt đọc trong bốn mươi tám giờ — viral trên Facebook, Zalo, Twitter. Báo chính thống im lặng, nhưng dư luận sôi sục.

Bộ Tài nguyên Môi trường vào cuộc. Thanh tra Chính phủ lập đoàn kiểm tra.

TBT Linh hoảng loạn: nếu phóng sự được xác nhận, mọi người sẽ hỏi — tại sao tòa soạn Thời Đại giết bài?"""),

("Chương 3: Bị Đe Dọa", """Nhi nhận tin nhắn đe dọa: "Dừng lại hoặc hối hận." Có người theo dõi cô ngoài quán cà phê. Mẹ cô bị gọi điện hăm dọa.

Nhi không dừng. Cô đăng bài thứ hai: "Ai Đã Giết Bài?" — phơi bày TBT Linh nhận năm trăm triệu từ Hoàng Gia để bịt miệng phóng sự. Bằng chứng: sao kê chuyển khoản từ tài khoản Hoàng Gia sang tài khoản vợ Linh.

Hội Nhà báo Việt Nam vào cuộc. Bộ Công an Cục An ninh mạng điều tra nguồn đe dọa."""),

("Chương 4: Nguồn Tin Được Bảo Vệ", """Twist: anh Trần Văn Đạt — nguồn tin bị lộ — không im lặng. Sau khi bị đe dọa, anh ra trước Thanh tra Chính phủ khai báo toàn bộ. Kèm theo: USB chứa bản sao database sổ đỏ giả — chứng cứ gốc mà Nhi chưa từng có.

"Tôi sợ. Nhưng phóng viên Nhi đã đặt cược sự nghiệp để bảo vệ nông dân. Tôi không thể hèn hơn cô ấy," Đạt nói trước đoàn thanh tra.

Database sổ đỏ giả: ba mươi bảy sổ, tổng diện tích đất bị chiếm đoạt trái phép hơn năm mươi hecta, thiệt hại hơn hai trăm tỷ đồng."""),

("Chương 5: Đổ Domino", """Kết quả điều tra:
— PCT tỉnh H Nguyễn Đình Lộc: khởi tố, tạm giam.
— TGĐ Hoàng Gia: khởi tố, phong tỏa tài sản.
— TBT Hoàng Bá Linh: thu hồi thẻ nhà báo, khởi tố về tội "nhận hối lộ."
— Ba cán bộ địa chính: khởi tố.

Tổng cộng: bảy người bị khởi tố từ một bài báo bị giết.

Nhi đứng trước tòa soạn Thời Đại — nơi cô từng làm việc — giờ bị niêm phong. Cô không vui. Cô nghĩ đến nông dân tỉnh H mất đất."""),

("Chương 6: Mẹ Và Trang Nhật Ký", """Nhi theo nghề báo vì mẹ. Bà Vũ Thị Thanh, nhà giáo hưu trí, viết nhật ký mỗi ngày — ghi lại mọi điều bất công nhỏ nhặt trong cuộc sống.

"Con ơi, mẹ viết nhật ký vì mẹ tin: nếu ghi lại, sự thật sẽ không bị quên."

Nhi mang triết lý đó vào nghề báo: ghi lại, đăng lên, không để sự thật bị chôn vùi.

"Tin Trong" — tên tòa soạn — lấy từ câu mẹ hay nói: "Tin gì thì tin, nhưng phải tin vào sự thật bên trong." """),

("Chương 7: Giải Thưởng Báo Chí — Climax", """Nhi nhận Giải Báo chí Quốc gia cho phóng sự "Đất Đen Tỉnh H" — giải lần đầu trao cho bài đăng trên nền tảng độc lập, không qua tòa soạn truyền thống.

"Tôi không viết bài này để nhận giải. Tôi viết vì nông dân tỉnh H mất đất. Giải thưởng thuộc về họ — và về anh Trần Văn Đạt, người đã dũng cảm hơn tôi," Nhi nói trên bục nhận giải.

Đạt ngồi hàng ghế đầu, mắt đỏ hoe.

Mẹ Nhi xem truyền hình trực tiếp, viết vào nhật ký: "Con gái mẹ nhận giải. Sự thật không bị quên." """),

("Chương 8: Quay Về Tỉnh H", """Nhi đến tỉnh H, gặp lại nông dân bị mất đất. Đất đã được trả lại — sổ đỏ thật được cấp cho ba mươi bảy hộ gia đình.

Một bà cụ nắm tay Nhi: "Cảm ơn con. Nhờ con mà đất nhà bà không bị mất."

Nhi cười, mắt cay. Cô mở laptop trong quán cà phê tỉnh lẻ, bắt đầu viết phóng sự tiếp theo — vì ở tỉnh K, có một câu chuyện tương tự đang xảy ra.

"Tin Trong" giờ có năm phóng viên, ba trăm nghìn subscribers. Nhỏ, nhưng mỗi bài đều thật.

Nhi gõ dòng đầu tiên của phóng sự mới, nghe tiếng mưa rơi ngoài cửa sổ quán cà phê tỉnh lẻ, và nghĩ đến mẹ — người viết nhật ký mỗi ngày để sự thật không bị quên."""),
]

# ═══════════════════════════════════════════════════════════════════════════════
# STORY 9: THUYỀN TRƯỞNG BỊ VU OAN — 10 CHƯƠNG
# ═══════════════════════════════════════════════════════════════════════════════

S9_TITLE = "BỊ VU OAN ĐẮM TÀU, TÔI TỰ TRỤC VỚT BẰNG CHỨNG DƯỚI ĐÁY BIỂN KHIẾN KẺ THỦ ÁC PHẢI LĨNH ÁN"
S9_AUTHOR = "Phạm Quốc Tuấn"
S9_COVER = "base_cover_12.png"
S9_INTRO = """<p><strong>"Mười hai năm đi biển, chưa bao giờ mất một container hàng. Nhưng khi con tàu đắm vì lỗi kỹ thuật do chủ tàu cắt giảm bảo trì, họ đổ tội cho tôi — thuyền trưởng."</strong></p>
<p>Phạm Quốc Tuấn, thuyền trưởng tàu hàng Hải Phong Star, bị vu oan gây chìm tàu khi thực chất chủ tàu Nguyễn Hải Đăng cắt giảm chi phí bảo trì để kiếm lời, khiến tàu gặp sự cố giữa biển Đông.</p>
<p>Mất bằng thuyền trưởng, bị kiện đòi bồi thường, Tuấn tự lặn xuống đáy biển trục vớt bằng chứng, minh oan cho mình và bảo vệ danh dự của thủy thủ đoàn.</p>"""

S9_CHAPTERS = [
("Chương 1: Đêm Tàu Đắm", """Hai giờ sáng, giữa biển Đông, tàu hàng Hải Phong Star chở ba nghìn tấn gạo xuất khẩu bỗng rung lắc dữ dội. Tiếng kim loại gãy vang lên từ hầm máy — đường ống dẫn dầu thủy lực nứt, dầu phun ra như máu đen.

Thuyền trưởng Phạm Quốc Tuấn lao xuống hầm máy, đánh giá nhanh: vỏ tàu phía mạn phải bị nứt — đường nứt dài hơn hai mét, nước biển tràn vào. Không phải do va chạm — mà do mối hàn cũ không chịu nổi áp lực sóng.

"Bơm nước! Đóng khoang kín!" Tuấn ra lệnh. Nhưng anh biết: bơm hút nước đã hỏng từ tháng trước — anh đã báo cáo cho chủ tàu sáu lần, yêu cầu sửa chữa. Sáu lần bị từ chối.

Tuấn ra quyết định: bỏ tàu, cứu người. Mười tám thủy thủ lên xuồng cứu sinh, không ai thiệt mạng. Hải Phong Star chìm xuống đáy biển Đông ở độ sâu bốn mươi hai mét.

Ba nghìn tấn gạo — trị giá bốn mươi tỷ đồng — mất theo.

Chủ tàu Nguyễn Hải Đăng tuyên bố: "Thuyền trưởng Phạm Quốc Tuấn điều hướng sai, gây chìm tàu. Kiện đòi bồi thường toàn bộ thiệt hại." """),

("Chương 2: Bằng Thuyền Trưởng Bị Tước", """Cục Hàng hải đình chỉ bằng thuyền trưởng của Tuấn "chờ điều tra." Không bằng, Tuấn không được lên bất kỳ con tàu nào.

Đăng — chủ tàu, doanh nhân ngành vận tải biển — thuê luật sư giỏi nhất, cung cấp "bằng chứng": nhật ký hành trình bị sửa, báo cáo thời tiết cho thấy Tuấn "điều hướng vào vùng sóng lớn."

"Thuyền trưởng có trách nhiệm tuyệt đối với an toàn tàu," luật sư Đăng tuyên bố. "Nếu tàu chìm, lỗi là thuyền trưởng."

Nhưng Tuấn biết sự thật: nhật ký hành trình gốc — bản viết tay — ghi rõ tàu đi đúng hải trình, thời tiết bình thường. Bản mà Đăng nộp cho tòa là bản photocopy đã bị chỉnh sửa."""),

("Chương 3: Lặn Xuống Đáy Biển", """Tuấn cần bằng chứng vật lý: đường nứt trên vỏ tàu chứng minh lỗi kỹ thuật, không phải va chạm.

Anh thuê thuyền cá, mua bộ lặn scuba secondhand, và tự lặn xuống đáy biển — bốn mươi hai mét — nơi Hải Phong Star nằm.

Lặn sâu bốn mươi mét không phải chuyện đùa — áp suất, tầm nhìn kém, và nguy cơ nhiễm nitơ. Nhưng Tuấn từng là thợ lặn trước khi thành thuyền trưởng.

Ba lần lặn, mỗi lần hai mươi phút. Anh quay video dưới nước bằng GoPro: đường nứt trên vỏ tàu — rõ ràng là mối hàn cũ bị ăn mòn, không phải va chạm. Và quan trọng nhất: nhật ký hành trình bản gốc — cuốn sổ bọc nhựa chống nước — vẫn nằm trong ngăn tủ buồng lái."""),

("Chương 4: Phát Hiện Đăng Cắt Giảm Bảo Trì", """Tuấn mang video và nhật ký lên bờ. Luật sư của anh — luật sư hàng hải Trần Văn Minh — so sánh nhật ký gốc với bản Đăng nộp: ba trang bị sửa, tọa độ hải trình bị thay đổi.

Và thêm: hồ sơ bảo trì tàu Hải Phong Star từ cơ quan đăng kiểm cho thấy — tàu quá hạn kiểm tra định kỳ tám tháng. Sáu báo cáo yêu cầu sửa chữa của Tuấn đều có trong hồ sơ — với bút phê của Đăng: "Hoãn. Chưa có ngân sách."

"Chủ tàu cắt giảm bảo trì, bỏ qua sáu cảnh báo của thuyền trưởng, và khi tàu chìm — đổ tội cho thuyền trưởng," luật sư Minh trình bày trước tòa."""),

("Chương 5: Thủy Thủ Đoàn Đứng Lên", """Mười bảy thủy thủ — toàn bộ đoàn trừ Tuấn — cùng ký đơn khai báo ủng hộ Tuấn. Mỗi người khai: đã chứng kiến bơm hút nước hỏng, đường ống rỉ sét, và Tuấn liên tục báo cáo nhưng bị bỏ qua.

Thợ máy Nguyễn Văn Hùng khai: "Tôi sửa đường ống tạm bợ bằng băng keo sáu lần vì không có phụ tùng thay thế. Thuyền trưởng Tuấn là người duy nhất quan tâm an toàn tàu."

"Anh Tuấn cứu mạng mười tám người chúng tôi đêm đó," máy trưởng Lê Đức Thắng nói trước tòa, giọng run."""),

("Chương 6: Bố Và Biển", """Tuấn đi biển vì bố. Ông Phạm Văn Hải, ngư dân Quảng Ngãi, mất trên biển khi Tuấn mười hai tuổi — bão đánh chìm thuyền, không tìm thấy thi thể.

"Con ơi, biển cho mình cá nhưng cũng lấy mình bất cứ lúc nào. Đi biển thì phải biết kính biển."

Tuấn thề: sẽ đi biển, nhưng không để ai chết trên biển nữa. Mười hai năm thuyền trưởng, chưa mất một người. Và đêm tàu đắm, anh giữ lời — mười tám người sống."""),

("Chương 7: Đăng Lĩnh Án — Climax", """Tòa tuyên: Nguyễn Hải Đăng bốn năm tù giam về tội "vi phạm quy định an toàn giao thông đường thủy" và "làm giả tài liệu." Bồi thường cho thủy thủ đoàn và bảo hiểm tổng sáu mươi tỷ đồng.

Tuấn được minh oan hoàn toàn. Bằng thuyền trưởng được trả lại, kèm thư xin lỗi chính thức từ Cục Hàng hải.

Tại phiên tòa, Đăng quay sang Tuấn: "Tao chỉ muốn tiết kiệm chi phí..."

"Anh tiết kiệm chi phí, suýt giết mười tám người," Tuấn nói, giọng bình thản nhưng mắt đỏ hoe."""),

("Chương 8: Ra Khơi Lần Nữa", """Tuấn nhận lời mời làm thuyền trưởng cho hãng tàu mới — điều kiện duy nhất: "Tôi có quyền từ chối xuất bến nếu tàu không đạt chuẩn an toàn."

Hãng đồng ý. Tuấn lên tàu mới — Việt Hải Star — sạch sẽ, bảo trì đầy đủ, thủy thủ đoàn mười hai người.

Ngày đầu ra khơi, Tuấn đứng trên cabin, nhìn biển Đông. Gió mặn thổi vào mặt. Anh nhớ bố — người ngư dân mất trên biển ba mươi năm trước.

"Bố ơi, con lại ra khơi."

Tàu rẽ sóng, hướng về phía đường chân trời."""),

("Chương 9: Nhật Ký Thuyền Trưởng", """Mỗi ngày trên biển, Tuấn viết nhật ký hành trình — viết tay, bằng bút bi, trên sổ bọc nhựa chống nước. Giống hệt cuốn nhật ký đã cứu anh dưới đáy biển.

Trang cuối cuốn nhật ký cũ — cuốn được trục vớt — Tuấn viết thêm một dòng:

"Biển không có lỗi. Người tham mới có lỗi. Tàu chìm vì người, không vì sóng."

Cuốn nhật ký đó giờ nằm trong Bảo tàng Hàng hải Việt Nam — hiện vật kể câu chuyện về thuyền trưởng tự lặn xuống đáy biển để minh oan."""),

("Chương 10: Đêm Trăng Trên Biển", """Đêm rằm, Tuấn đứng trên boong tàu Việt Hải Star, nhìn trăng phản chiếu trên mặt biển Đông — mênh mông, lấp lánh, bình yên.

Thợ máy trẻ hỏi: "Anh Tuấn, sau tất cả những chuyện đó, anh có sợ biển không?"

"Không. Tao sợ người. Biển thì lúc nào cũng thật — sóng to thì nói to, lặng thì nói lặng. Chỉ có người mới nói một đằng làm một nẻo."

Thợ máy trẻ cười, rồi im lặng nhìn biển.

Tuấn cũng im lặng, tay sờ lên lan can tàu — cảm giác kim loại lạnh dưới bàn tay, cảm giác quen thuộc mười hai năm.

Biển đêm. Trăng. Và thuyền trưởng Phạm Quốc Tuấn — người từ đáy biển trở về — đang lái tàu hướng về phía ánh sáng."""),
]

# ═══════════════════════════════════════════════════════════════════════════════
# STORY 10: NGHỆ NHÂN GỐM — 12 CHƯƠNG
# ═══════════════════════════════════════════════════════════════════════════════

S10_TITLE = "BỊ ĐUỔI KHỎI LÀNG GỐM VÌ DÁM ĐỔI MỚI, TÔI TẠO RA DÒNG GỐM KHIẾN CẢ LÀNG PHẢI HỌC LẠI TỪ ĐẦU"
S10_AUTHOR = "Trịnh Bảo Khánh"
S10_COVER = "base_cover_13.png"
S10_INTRO = """<p><strong>"Bốn đời gia đình tôi làm gốm ở Bát Tràng. Khi tôi thử nghiệm men gốm mới kết hợp truyền thống và hiện đại, trưởng làng cấm tôi đốt lò, hội đồng nghề khai trừ tôi — vì 'phá hoại truyền thống.'"</strong></p>
<p>Trịnh Bảo Khánh, nghệ nhân gốm thế hệ thứ tư ở Bát Tràng, bị khai trừ khỏi Hội Nghệ nhân Gốm vì dám thử nghiệm men reactive glaze kết hợp truyền thống và hiện đại.</p>
<p>Bị cấm đốt lò trong làng, Khánh lập xưởng riêng, tạo ra dòng gốm mới vừa giữ hồn truyền thống vừa chinh phục thị trường quốc tế, khiến chính những người từng khai trừ anh phải quay lại học hỏi.</p>"""

S10_CHAPTERS = [
("Chương 1: Lò Gốm Bị Cấm", """Trịnh Bảo Khánh đứng trước lò gốm gia đình — cái lò cũ bằng gạch chịu lửa mà ông cố xây từ năm 1920 — và đọc tờ quyết định của Hội đồng Nghệ nhân Gốm Bát Tràng: "Khai trừ Trịnh Bảo Khánh khỏi hội, cấm sử dụng lò gốm chung, cấm bán sản phẩm mang thương hiệu Bát Tràng."

Lý do: "Sử dụng men gốm phi truyền thống, gây ảnh hưởng xấu đến uy tín và bản sắc gốm Bát Tràng."

Men "phi truyền thống" mà họ nói: reactive glaze — men phản ứng hóa học tạo hiệu ứng màu độc nhất mỗi lần nung, kết hợp khoáng chất tự nhiên Việt Nam (đất đỏ bazan Đắk Lắk, cát Mũi Né, tro núi lửa Phú Quý) với công thức men truyền thống Bát Tràng.

"Cháu à, Bát Tràng làm gốm năm trăm năm bằng một công thức. Cháu muốn thay đổi? Đó là phá hoại," trưởng làng Nguyễn Văn Thọ nói, giọng lạnh.

"Men truyền thống là nền tảng, bác Thọ. Nhưng nếu không đổi mới, gốm Bát Tràng sẽ chết — vì khách hàng trẻ không mua bát đĩa truyền thống nữa."

"Gốm Bát Tràng sống năm trăm năm không cần ý kiến của thằng nhóc ba mươi tuổi."

Khánh nhìn cái lò gốm gia đình — cái lò mà ông cố, ông nội, bố anh đã đốt hàng chục nghìn lần — giờ bị niêm phong bằng tấm biển đỏ của hội đồng."""),

("Chương 2: Xưởng Gốm Trong Nhà Kho", """Khánh thuê nhà kho cũ ở ngoại thành Hà Nội, tự xây lò gốm mới — lò gas hiện đại, kiểm soát nhiệt độ chính xác từng độ, kết hợp với kiến thức đốt lò truyền thống bốn đời.

Ba tháng thí nghiệm. Mỗi ngày nung hai mẻ, mỗi mẻ thử một công thức men mới. Kết quả ghi chép trong sổ dày ba trăm trang — từng tỷ lệ khoáng chất, từng nhiệt độ, từng thời gian nung.

Mẻ thứ sáu mươi bảy: reactive glaze hoàn hảo. Men phản ứng với nhiệt tạo ra vân xanh ngọc — giống ngọc phỉ thúy — trên nền men trắng Bát Tràng truyền thống. Mỗi sản phẩm có vân duy nhất — không hai chiếc nào giống nhau.

Khánh đặt tên: men "Ngọc Rồng." """),

("Chương 3: Viral Trên TikTok", """Khánh quay video quá trình nung gốm Ngọc Rồng — khoảnh khắc mở lò, sản phẩm lộ ra với vân xanh ngọc lấp lánh — và đăng TikTok.

Video đạt hai mươi triệu lượt xem. Comments từ khắp thế giới: "This is the most beautiful pottery I've ever seen!" "Where can I buy?"

Đơn đặt hàng tràn về — từ Mỹ, Nhật, Hàn, châu Âu. Khánh mở Etsy shop, bán mỗi chiếc bát Ngọc Rồng giá 80 USD — sold out trong ngày."""),

("Chương 4: Làng Gốm Ghen Tị", """Thành công của Khánh khiến làng Bát Tràng chia rẽ. Nghệ nhân trẻ muốn học hỏi, nghệ nhân già phản đối.

Trưởng làng Thọ tuyên bố: "Sản phẩm Trịnh Bảo Khánh không phải gốm Bát Tràng. Không được dùng tên Bát Tràng trong bất kỳ hình thức quảng bá nào."

Khánh đáp: "Tôi chưa bao giờ gắn tên Bát Tràng. Thương hiệu tôi là 'Khánh Gốm' — không cần mượn danh ai."

Nhưng khách hàng tự so sánh: "Khánh Gốm" rated 4.9 trên Etsy, gốm Bát Tràng truyền thống khó bán — vì không ai mua bát đĩa trơn khi có option vân ngọc thạch."""),

("Chương 5: Christie's Gõ Cửa", """Christie's — nhà đấu giá nghệ thuật top thế giới — liên hệ: muốn đấu giá bộ sưu tập "Ngọc Rồng: Bốn Mùa" — bốn chiếc bình lớn, mỗi chiếc đại diện một mùa, men reactive glaze tạo bốn gam màu khác nhau.

Giá khởi điểm: năm mươi nghìn đô cho cả bộ. Giá chốt: hai trăm tám mươi nghìn đô.

Người mua: bảo tàng Victoria and Albert Museum, London — bộ sưu tập vĩnh viễn.

"Gốm Việt Nam trong bảo tàng V&A," Khánh nói khi nghe tin, giọng run."""),

("Chương 6: Ông Nội Và Bí Mật Men Cổ", """Khánh theo nghề vì ông nội. Ông Trịnh Văn Đức, nghệ nhân gốm bậc thầy, mất khi Khánh mười lăm tuổi.

Trước khi mất, ông tặng Khánh cuốn sổ nhỏ viết tay — công thức men gốm gia truyền, ghi từ thời ông cố: tỷ lệ đất sét, feldspat, thạch anh, và một thành phần bí mật — tro cây sen Hồ Tây.

"Cháu à, ông nội để lại cho cháu công thức cũ. Nhưng ông muốn cháu tìm ra công thức mới. Truyền thống không phải cái chết — truyền thống là gốc rễ để mọc cành mới."

Cuốn sổ đó — giờ mờ nhòe vì thời gian — nằm trên bàn xưởng Khánh, bên cạnh sổ ghi chép ba trăm trang công thức men Ngọc Rồng."""),

("Chương 7: Lửa Trong Lò", """Khánh mở cửa xưởng cho nghệ nhân trẻ Bát Tràng đến học — miễn phí. Mười hai nghệ nhân trẻ đến, bất chấp lệnh cấm của trưởng làng.

"Anh Khánh, bác Thọ nói ai học của anh sẽ bị khai trừ khỏi hội."

"Tay các em biết nặn gốm. Không ai khai trừ được tay các em."

Xưởng Khánh thành workshop — mỗi tuần một buổi, dạy từ men reactive đến thiết kế hiện đại. Nghệ nhân trẻ Bát Tràng bắt đầu tạo ra sản phẩm mới — mỗi người một phong cách."""),

("Chương 8: Trưởng Làng Thay Đổi", """Doanh thu gốm Bát Tràng truyền thống giảm ba mươi phần trăm trong hai năm. Du khách đến Bát Tràng hỏi: "Gốm Ngọc Rồng mua ở đâu?" — nhưng Khánh không ở trong làng.

Trưởng làng Thọ — người khai trừ Khánh — cuối cùng phải thừa nhận: gốm truyền thống cần đổi mới hoặc chết.

Ông Thọ đến xưởng Khánh, đứng ngoài cửa, ngần ngừ. Khánh mở cửa:

"Bác Thọ."

"Cháu Khánh... bác đến xin lỗi. Và xin học."

Khánh im lặng ba giây, rồi mở cửa rộng: "Bác vào đây. Lò đang nóng." """),

("Chương 9: Bộ Sưu Tập 'Hồn Bát Tràng'", """Khánh tạo bộ sưu tập đặc biệt: "Hồn Bát Tràng" — kết hợp men truyền thống Bát Tràng (công thức ông cố) với men reactive Ngọc Rồng (công thức của Khánh). Truyền thống + hiện đại trong một sản phẩm.

Bộ sưu tập ra mắt tại Maison & Objet Paris — hội chợ thiết kế nội thất lớn nhất thế giới. Khách hàng châu Âu đặt hàng năm nghìn sản phẩm."""),

("Chương 10: Lò Gốm Gia Đình Mở Lại", """Hội đồng Nghệ nhân Bát Tràng bỏ phiếu: phục hồi tư cách hội viên cho Trịnh Bảo Khánh, mời anh làm cố vấn đổi mới cho làng gốm.

Khánh đồng ý — với điều kiện: "Không ai bị khai trừ vì đổi mới nữa."

Lò gốm gia đình — cái lò ông cố xây từ 1920 — được gỡ niêm phong. Khánh đốt lò lần đầu sau ba năm. Lửa bùng lên, sưởi ấm gạch chịu lửa cũ kỹ."""),

("Chương 11: Dạy Cháu Nặn Gốm", """Con trai Khánh — bé Minh, năm tuổi — lần đầu vào xưởng. Bé ngồi trên đùi bố, hai bàn tay nhỏ xíu đặt lên đất sét ướt trên bàn xoay.

"Bố ơi, đất sét trơn trượt quá!"

"Từ từ con, nắm nhẹ thôi. Đất sét giống người — ép mạnh quá thì nát."

Bé Minh nặn được chiếc bát méo — méo hơn cả chiếc bát đầu tiên của Khánh hai mươi lăm năm trước. Khánh nung chiếc bát méo trong lò, tráng men Ngọc Rồng.

Ra lò: chiếc bát méo nhưng vân xanh ngọc lấp lánh — đẹp theo cách riêng của nó."""),

("Chương 12: Quay Về Lò Cũ", """Khánh ngồi trước lò gốm gia đình, lửa cháy đều. Trên kệ: chiếc bát ông cố — men trắng truyền thống, năm trăm năm. Bên cạnh: chiếc bát Khánh — men Ngọc Rồng xanh ngọc. Và chiếc bát méo của bé Minh — men ngọc trên dáng méo.

Ba thế hệ, ba chiếc bát, một ngọn lửa.

Khánh nhìn lửa trong lò — ngọn lửa mà ông cố đã đốt, ông nội đã giữ, bố đã truyền, và bé Minh sẽ tiếp.

"Truyền thống không phải cái chết — truyền thống là gốc rễ để mọc cành mới."

Câu nói của ông nội vang lên trong đầu Khánh.

Anh mỉm cười, thêm củi vào lò, giữ lửa cháy."""),
]

# ═══════════════════════════════════════════════════════════════════════════════
# ASSEMBLY & PUBLISHING
# ═══════════════════════════════════════════════════════════════════════════════

ALL_STORIES = [
    {"title": S6_TITLE, "author": S6_AUTHOR, "cover": S6_COVER, "intro": S6_INTRO, "chapters": S6_CHAPTERS},
    {"title": S7_TITLE, "author": S7_AUTHOR, "cover": S7_COVER, "intro": S7_INTRO, "chapters": S7_CHAPTERS},
    {"title": S8_TITLE, "author": S8_AUTHOR, "cover": S8_COVER, "intro": S8_INTRO, "chapters": S8_CHAPTERS},
    {"title": S9_TITLE, "author": S9_AUTHOR, "cover": S9_COVER, "intro": S9_INTRO, "chapters": S9_CHAPTERS},
    {"title": S10_TITLE, "author": S10_AUTHOR, "cover": S10_COVER, "intro": S10_INTRO, "chapters": S10_CHAPTERS},
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
        log(f"✓ {s['title'][:55]}... — {total} sentences")
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
    log("🚀 MIX BATCH 2 — 5 STORIES (Sảng Văn Cải Tiến, 8-12 chương)")
    ftp = get_ftp()
    with open(os.path.join(BASE_DIR, "publish_novel.php"), "rb") as f:
        ftp.storbinary("STOR publish_novel.php", f)
    ftp.quit()
    log("✓ Helper uploaded")

    results = []
    for i, n in enumerate(novels):
        log(f"\n{'='*60}\n📖 PUBLISHING {i+1}/5: {n['title'][:55]}...\n{'='*60}")
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

    log(f"\n🏁 MIX BATCH 2 COMPLETE: {len(results)}/5 published")
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
