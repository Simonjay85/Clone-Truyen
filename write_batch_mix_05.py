#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
write_batch_mix_05.py — Batch 5: 5 Truyện CUNG ĐẤU (Stories 21-25)
====================================================================
Template D: Mưu mô → đấu trí → đảo ngược quyền lực
Tone: Hồi hộp, chiến thuật, twist
Số chương 8-13

Story 21: Con dâu tranh thừa kế khách sạn (10 ch) — cover 24
Story 22: Thư ký bị vu oan biển thủ (9 ch) — cover 25
Story 23: Em gái út thâu tóm đế chế (11 ch) — cover 26
Story 24: Nữ quản lý quỹ đối đầu cha nuôi (8 ch) — cover 27
Story 25: BS trưởng khoa lập viện riêng (10 ch) — cover 28
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
# STORY 21: CON DÂU TRANH THỪA KẾ KHÁCH SẠN — 10 CHƯƠNG
# ═══════════════════════════════════════════════════════════════════════════════

S21_TITLE = "CON DÂU BỊ CẢ GIA ĐÌNH CHỒNG KHINH RẺ, LẬT NGƯỢC TÌNH THẾ NẮM TOÀN BỘ ĐẾ CHẾ KHÁCH SẠN"
S21_AUTHOR = "Lâm Thiên Hương"
S21_COVER = "base_cover_24.png"
S21_INTRO = """<p><strong>"Gia đình nhà chồng gọi tôi là 'con bé bán phở' — vì tôi xuất thân từ quán phở vỉa hè quận 10. Họ ép tôi ký giấy từ bỏ quyền thừa kế. Họ sai."</strong></p>
<p>Lâm Thiên Hương, con dâu nhà họ Trần — gia tộc sở hữu chuỗi khách sạn năm sao lớn nhất miền Nam — bị mẹ chồng và chị dâu liên minh đẩy ra ngoài. Nhưng Hương không phải con bé bán phở vô hại — cô là MBA từ NUS Singapore, và cô có kế hoạch.</p>"""

S21_CHAPTERS = [
("Chương 1: Bữa Tối Gia Tộc", """Bàn ăn nhà họ Trần: bàn gỗ gụ mười hai chỗ, đèn chùm pha lê, bát đĩa Hermès. Mười người ngồi — nhưng quyền lực chỉ thuộc về một: bà Trần Thanh Nga, mẹ chồng Hương, Chủ tịch Tập đoàn Trần Hotel Group.

"Hương à, con dâu phải biết vị trí của mình trong gia đình," bà Nga nói, tay xoay ly rượu vang Pétrus. "Con lo việc nhà, chăm cháu. Việc kinh doanh để Phương lo."

Phương — chị dâu, vợ anh cả Trần Đức Minh — gật đầu tự mãn. Phương là con gái gia đình bất động sản, mang theo hồi môn hai trăm tỷ, và được bà Nga coi là "con dâu xứng đáng."

Hương — vợ anh hai Trần Đức Khải — im lặng gắp thức ăn. Cô biết: trong gia đình này, cô là "con bé bán phở" — mẹ cô bán phở vỉa hè quận 10, bố mất sớm, Hương tự học, tự thi, tự đỗ MBA NUS Singapore.

"Dạ, con hiểu ạ," Hương nói, mắt cúi xuống.

Nhưng dưới bàn, tay Hương nắm chặt — vì cô vừa phát hiện điều mà cả gia đình không biết: Trần Hotel Group đang lỗ — và bà Nga đang giấu."""),

("Chương 2: Phát Hiện Lỗ Hổng Tài Chính", """Hương có quyền truy cập hệ thống kế toán công ty — vì Khải, chồng cô, là Phó TGĐ và vô tình để lại mật khẩu trên laptop. Hương đọc báo cáo tài chính: Trần Hotel Group doanh thu hai nghìn tỷ, nhưng lợi nhuận thực âm ba trăm tỷ.

Lý do: bà Nga và Phương đã rút tiền công ty đầu tư vào bất động sản nghỉ dưỡng — dự án resort Phú Quốc trị giá một nghìn tỷ — mà không thông qua HĐQT. Resort đang chậm tiến độ, chi phí phát sinh gấp đôi, và nhà thầu đe dọa kiện.

"Họ đang đốt tiền công ty vào dự án cá nhân," Hương ghi chép. "Nếu cổ đông biết, giá cổ phiếu sụp."

Hương không hành động ngay. Cô chờ — vì MBA dạy cô: timing là tất cả."""),

("Chương 3: Chị Dâu Phản Đòn", """Phương phát hiện Hương "hỏi nhiều quá" về tài chính công ty. Phương nói với bà Nga: "Mẹ ơi, con Hương nó dòm ngó. Phải cắt quyền truy cập."

Bà Nga đồng ý. Thêm nữa: bà ép Khải ký giấy ủy quyền quản lý cổ phần cho mẹ — lấy lý do "con trai chưa đủ kinh nghiệm."

Khải — con trai ngoan nhưng yếu đuối — ký. Hương nhìn chồng ký, không can ngăn. Cô đã copy xong toàn bộ dữ liệu.

"Em à, anh biết mẹ làm đúng," Khải nói.

"Anh nghĩ thế thì tốt. Em chỉ lo cho gia đình," Hương đáp, giọng bình thản."""),

("Chương 4: Xây Liên Minh Ngầm", """Hương tiếp cận hai cổ đông thiểu số của Trần Hotel Group: ông Lê Văn Phú (15% cổ phần) và bà Nguyễn Thị Mai (10%). Cả hai đều bất mãn vì không nhận cổ tức hai năm liên tiếp.

Hương trình bày số liệu — chi tiết, rõ ràng, MBA-level: "Dự án Phú Quốc đã tiêu hết ngân sách, và bà Nga đang dùng vốn lưu động của công ty để bù lỗ. Nếu không xử lý, công ty phá sản trong mười tám tháng."

Ông Phú nhìn số liệu, mặt tái: "Tôi đầu tư ba trăm tỷ vào công ty này!"

"Con có kế hoạch cứu công ty. Nhưng cần sự ủng hộ của bác và cô Mai trong đại hội cổ đông," Hương nói."""),

("Chương 5: Bà Nga Phản Công", """Bà Nga phát hiện Hương gặp cổ đông ngoài. Bà triệu tập họp gia đình, tuyên bố: "Lâm Thiên Hương phản bội gia đình. Tôi yêu cầu Khải ly hôn."

Phương đồng tình: "Con bé bán phở muốn cướp công ty!"

Khải bối rối. Hương bình tĩnh: "Con không cướp gì cả, mẹ. Con chỉ muốn hỏi: tại sao dự án Phú Quốc đã chi vượt năm trăm tỷ mà HĐQT không biết?"

Bà Nga im lặng hai giây — hai giây đủ để mọi người trong phòng hiểu: Hương nói đúng.

"Chuyện kinh doanh không phải việc con dâu," bà Nga nói, giọng lạnh.

"Chuyện kinh doanh là việc của cổ đông. Và chồng con là cổ đông 20%," Hương đáp."""),

("Chương 6: Đại Hội Cổ Đông — Trận Chiến", """Đại hội cổ đông bất thường. Hương đứng trước ba mươi cổ đông — tay cầm bản trình bày 40 slide — trình bày tình hình tài chính thực.

"Trần Hotel Group lỗ thực ba trăm tỷ. Dự án Phú Quốc đội vốn gấp đôi. Vốn lưu động chỉ còn đủ sáu tháng. Nếu không restructure ngay, công ty phá sản."

Bà Nga đứng lên: "Con dâu tôi không có quyền phát biểu tại đây!"

Ông Phú đáp: "Bà Nga, cổ đông có quyền nghe sự thật. Và cô Hương đang nói sự thật."

Bỏ phiếu: 65% cổ đông yêu cầu kiểm toán độc lập. Bà Nga thua."""),

("Chương 7: Kiểm Toán Phơi Bày Tất Cả", """Kiểm toán Big Four (Deloitte) vào cuộc: phát hiện bà Nga và Phương đã rút bốn trăm tỷ từ công ty vào tài khoản cá nhân thông qua "phí tư vấn" giả, thanh toán cho công ty con do Phương đứng tên.

"Đây không chỉ là quản lý yếu kém. Đây là chiếm đoạt tài sản công ty," luật sư Hương tuyên bố.

Bà Nga thuê luật sư đối phó — nhưng bằng chứng quá rõ ràng.

Khải — lần đầu tiên đối mặt sự thật — nhìn mẹ: "Mẹ, sao mẹ rút tiền công ty?"

"Mẹ làm vì gia đình!"

"Mẹ làm vì mẹ. Và Phương," Khải nói, giọng run."""),

("Chương 8: Hương Lên Ghế CEO", """HĐQT bỏ phiếu: miễn nhiệm bà Nga khỏi chức Chủ tịch. Đề cử CEO mới: Lâm Thiên Hương — người duy nhất có kế hoạch cứu công ty.

Hương nhận chức, trình bày kế hoạch restructure: bán dự án Phú Quốc lỗ, tái cấu trúc nợ, tập trung vào mảng khách sạn thành phố — nơi Trần Hotel Group mạnh nhất.

Mười hai tháng sau: Trần Hotel Group từ lỗ ba trăm tỷ sang lãi một trăm tỷ. Cổ phiếu tăng 40%.

"Con bé bán phở" giờ ngồi ghế CEO — và công ty sống lại nhờ cô."""),

("Chương 9: Mẹ Và Quán Phở", """Hương thành công vì mẹ. Bà Lâm Thị Hạnh, bán phở vỉa hè quận 10 — ba giờ sáng dậy nấu nước lèo, bán đến trưa, nuôi con gái ăn học.

"Mẹ ơi, con bị người ta gọi là 'con bé bán phở.' "

"Bán phở không xấu. Xấu là người khinh người bán phở."

Mẹ dạy Hương: kiên nhẫn, quan sát, và không bao giờ lộ bài. "Nấu phở phải chờ nước lèo sôi liu riu — ép sôi nhanh thì nước đục."

Triết lý đó Hương mang vào thương trường: chờ đợi, quan sát, hành động đúng lúc."""),

("Chương 10: Bữa Tối Mới", """Bàn ăn nhà họ Trần. Cùng bàn gỗ gụ, cùng đèn chùm. Nhưng vị trí đã đổi.

Hương ngồi đầu bàn — ghế của CEO. Bà Nga ngồi góc, im lặng. Phương không đến.

Khải ngồi cạnh Hương, lần đầu tiên nhìn vợ bằng ánh mắt kính trọng: "Em giỏi hơn anh tưởng."

"Em không giỏi hơn anh tưởng. Em giỏi hơn mẹ anh tưởng."

Hương gắp thức ăn cho bà Nga — vì dù tất cả, bà vẫn là mẹ chồng. "Mẹ ơi, con nấu phở hôm nay. Công thức mẹ con. Mẹ ăn thử."

Bà Nga ăn miếng phở, im lặng một lúc, rồi nói — nhỏ đến mức chỉ Hương nghe: "Phở ngon."

Hai chữ. Nhưng đủ.

Hương mỉm cười, tiếp tục ăn bữa tối gia đình — bữa tối mà lần đầu tiên, cô ngồi đúng vị trí của mình."""),
]

# ═══════════════════════════════════════════════════════════════════════════════
# STORY 22: THƯ KÝ BỊ VU OAN BIỂN THỦ — 9 CHƯƠNG
# ═══════════════════════════════════════════════════════════════════════════════

S22_TITLE = "BỊ VU OAN BIỂN THỦ MƯỜI TỶ, CÔ THƯ KÝ LẶNG LẼ THU THẬP BẰNG CHỨNG KHIẾN GIÁM ĐỐC PHẢI QUỲ"
S22_AUTHOR = "Đào Thanh Trúc"
S22_COVER = "base_cover_25.png"
S22_INTRO = """<p><strong>"Bảy năm tôi làm thư ký cho ông ta — trung thành, cần mẫn, không nghỉ phép. Khi ông ta cần người đổ tội biển thủ mười tỷ, ông ta chọn tôi — vì tôi 'hiền' nhất."</strong></p>
<p>Đào Thanh Trúc, thư ký Tổng giám đốc Công ty CP Thép Đông Á, bị TGĐ Ngô Quốc Dũng vu oan biển thủ mười tỷ đồng để che giấu việc ông ta rút tiền công ty nuôi nhân tình.</p>"""

S22_CHAPTERS = [
("Chương 1: Bị Gọi Lên Phòng Kỷ Luật", """Đào Thanh Trúc bước vào phòng họp, thấy bốn người: TGĐ Ngô Quốc Dũng, Trưởng phòng Tài chính Lê Văn Hùng, luật sư công ty, và một người lạ — thanh tra nội bộ.

"Trúc, chúng tôi phát hiện khoản chi bất thường mười tỷ đồng từ quỹ đại diện trong hai năm qua. Tất cả chứng từ đều mang chữ ký của cô," TGĐ Dũng nói, giọng nghiêm.

Trúc nhìn chứng từ: đúng chữ ký của cô — nhưng cô không ký những khoản này. Ai đó đã giả chữ ký.

"Tôi không biển thủ. Tôi không ký những chứng từ này."

"Chữ ký giống hệt," luật sư nói. "Cô bị đình chỉ công tác ngay lập tức."

Dũng nhìn Trúc bằng ánh mắt mà cô đã thấy bảy năm — ánh mắt của người coi thư ký như đồ vật. "Trúc à, nếu cô thú nhận và trả lại tiền, tôi sẽ không kiện hình sự."

Trúc đứng dậy, bình tĩnh: "Tôi không nhận tội vì tôi không có tội." """),

("Chương 2: Bị Đuổi Và Bị Dư Luận Ép", """Trúc bị đuổi việc. Tin "thư ký biển thủ mười tỷ" lan khắp ngành thép. Không công ty nào nhận cô.

Bạn bè xa lánh. Người yêu bỏ. Mẹ cô bị hàng xóm dèm pha: "Con gái bà ăn cắp tiền công ty!"

Trúc ngồi trong phòng trọ, nhìn tờ giấy sa thải, khóc. Rồi cô lau nước mắt, mở laptop, bắt đầu ghi chép: mọi giao dịch bất thường cô từng thấy trong bảy năm làm thư ký.

"Ông Dũng rút tiền quỹ đại diện mỗi tháng — nói là 'tiếp khách.' Nhưng không bao giờ có biên lai tiếp khách."

Trúc nhớ. Vì thư ký giỏi nhớ mọi thứ."""),

("Chương 3: Manh Mối — Nhân Tình Của Giám Đốc", """Trúc điều tra: khoản mười tỷ rút từ quỹ đại diện được chuyển vào tài khoản của Nguyễn Thùy Linh — người mà công ty ghi là "nhà tư vấn marketing." Nhưng Trúc biết: Linh là nhân tình của TGĐ Dũng — cô từng đặt vé máy bay, book khách sạn cho hai người nhiều lần.

"Ông Dũng rút tiền công ty nuôi nhân tình, rồi đổ tội cho tôi," Trúc nói với luật sư — luật sư Phan Minh Tuấn, luật sư trẻ chuyên lao động, nhận vụ pro bono.

Bằng chứng: email đặt phòng, tin nhắn Zalo (Trúc giữ backup vì cô quản lý điện thoại giám đốc), và đặc biệt — hóa đơn từ nhà hàng và spa mà "nhà tư vấn" Linh ký nhận."""),

("Chương 4: Giám Định Chữ Ký", """Luật sư Tuấn gửi chứng từ mười tỷ đi giám định chữ ký tại Viện Khoa học Hình sự. Kết quả: chữ ký trên chứng từ không phải của Trúc — mà là bản scan chữ ký cô, được photoshop ghép vào chứng từ mới.

"Ai đó đã lấy chữ ký cô từ chứng từ cũ, cắt dán vào chứng từ giả," giám định viên kết luận.

Ai có quyền truy cập file chữ ký cũ? Trưởng phòng Tài chính Lê Văn Hùng — người bà con Dũng, người đã "phát hiện" khoản biển thủ."""),

("Chương 5: Trúc Phản Công", """Trúc gửi hồ sơ cho báo chí, kèm: giám định chữ ký giả, bằng chứng nhân tình, sao kê chuyển khoản từ quỹ đại diện vào tài khoản Linh.

Báo Tuổi Trẻ đăng phóng sự: "TGĐ Thép Đông Á biển thủ mười tỷ, đổ tội thư ký." Viral khắp mạng.

Dũng phản ứng: thuê luật sư kiện Trúc "phỉ báng." Nhưng mọi bằng chứng Trúc đưa ra đều có xác nhận pháp lý.

Cổ phiếu Thép Đông Á giảm 30% trong tuần. HĐQT triệu tập họp khẩn."""),

("Chương 6: Hùng Khai Hết", """Trưởng phòng Tài chính Hùng — dưới áp lực điều tra — khai: "TGĐ Dũng chỉ đạo tôi tạo chứng từ giả và ghép chữ ký Trúc. Ông ấy hứa thưởng tôi năm trăm triệu."

"Tại sao anh chọn cô Trúc?"

"Vì cô ấy hiền. Không ai nghĩ cô ấy sẽ phản kháng."

Dũng bị khởi tố: biển thủ tài sản, làm giả tài liệu, vu khống. Linh bị triệu tập. Hùng bị khởi tố tòng phạm."""),

("Chương 7: Mẹ Và Đôi Tay Chai Sạn", """Trúc theo nghề thư ký vì mẹ. Bà Đào Thị Lan, công nhân nhà máy may — mười sáu tiếng/ngày, tay chai sạn vì cầm kéo.

"Con ơi, mẹ làm công nhân để con đi học. Con học cho giỏi, đừng phải cầm kéo như mẹ."

Trúc học văn thư, làm thư ký — "nghề sạch sẽ, phòng máy lạnh," mẹ nói tự hào.

Khi bị vu oan, Trúc gọi mẹ: "Mẹ ơi, con bị đổ tội oan."

"Con không làm thì con không sợ. Mẹ tin con."

Bốn chữ: "Mẹ tin con." Đủ để Trúc đứng dậy."""),

("Chương 8: Dũng Lĩnh Án — Climax", """Tòa tuyên: Ngô Quốc Dũng bảy năm tù giam — biển thủ tài sản doanh nghiệp, vu khống. Hùng ba năm tù treo. Linh bị buộc trả lại toàn bộ tiền.

Trúc được minh oan công khai. Thép Đông Á bồi thường cho Trúc một tỷ đồng — tiền lương bị mất, thiệt hại tinh thần.

Tại phiên tòa, Dũng nhìn Trúc: "Tôi không nghĩ cô dám..."

"Thưa ông, ông khinh tôi vì tôi hiền. Nhưng hiền không phải yếu — hiền là đợi đúng lúc." """),

("Chương 9: Thư Ký Mới — Nhưng Không Hiền Nữa", """Trúc không quay lại Thép Đông Á. Cô mở công ty tư vấn quản trị doanh nghiệp — chuyên kiểm soát nội bộ, phòng chống gian lận.

"Tôi từng là nạn nhân của gian lận nội bộ. Giờ tôi giúp doanh nghiệp không để điều đó xảy ra."

Năm đầu: mười khách hàng doanh nghiệp. Năm thứ ba: năm mươi. Trúc thuê năm nhân viên — tất cả đều là cựu thư ký, kế toán, nhân viên văn phòng từng bị đối xử bất công.

"Chúng tôi biết mọi góc khuất của văn phòng — vì chúng tôi từng sống ở đó," Trúc nói trong buổi ra mắt công ty.

Trên bàn làm việc: tấm ảnh mẹ, đôi tay chai sạn, và câu nói: "Mẹ tin con." """),
]

# ═══════════════════════════════════════════════════════════════════════════════
# STORY 23: EM GÁI ÚT THÂU TÓM ĐẾ CHẾ — 11 CHƯƠNG
# ═══════════════════════════════════════════════════════════════════════════════

S23_TITLE = "BỊ HAI ANH TRAI ĐẨY RA NGOÀI CUỘC CHIẾN THỪA KẾ, EM GÁI ÚT LẶNG LẼ THÂU TÓM TOÀN BỘ ĐẾ CHẾ"
S23_AUTHOR = "Trương Bảo Ngọc"
S23_COVER = "base_cover_26.png"
S23_INTRO = """<p>Gia đình Trương — đế chế logistics lớn nhất Bắc Bộ — có ba người thừa kế: anh cả Trương Bảo Hùng (40 tuổi), anh hai Trương Bảo Minh (37), và em gái út Trương Bảo Ngọc (32). Khi ông Trương Văn Đại — người sáng lập — đổ bệnh, hai anh trai bắt đầu cuộc chiến thừa kế.</p>
<p>Không ai để ý đến Ngọc — "con gái chỉ nên lấy chồng." Sai lầm lớn nhất của họ.</p>"""

S23_CHAPTERS = [
("Chương 1: Cha Đổ Bệnh — Cuộc Chiến Bắt Đầu", """Ông Trương Văn Đại, sáu mươi bảy tuổi, đột quỵ tại văn phòng — não xuất huyết, mê man. Bác sĩ nói: ông có thể không tỉnh lại.

Chưa kịp thương cha, hai anh trai đã họp: "Ai làm Chủ tịch?"

Hùng — anh cả, quản lý mảng vận tải đường bộ — tuyên bố: "Tôi là trưởng. Tôi kế nhiệm."

Minh — anh hai, quản lý mảng kho bãi — phản đối: "Anh quản lý tệ. Doanh thu mảng anh giảm hai năm liền."

Ngọc — em gái, quản lý mảng nhân sự — ngồi im. Hai anh nhìn cô: "Ngọc, em lo việc nhà, chăm cha. Chuyện kinh doanh để anh."

"Dạ, em hiểu," Ngọc nói."""),

("Chương 2: Hai Anh Trai Đánh Nhau", """Hùng và Minh đấu đá công khai: Hùng liên minh với Phó TGĐ kinh doanh, Minh liên minh với Phó TGĐ tài chính. Công ty chia hai phe — nhân viên bị ép chọn bên.

Hiệu suất giảm: đơn hàng trễ, khách hàng phàn nàn, nhân viên chủ chốt nghỉ việc. Doanh thu quý ba giảm 25%.

Ngọc quan sát tất cả — từ phòng nhân sự, nơi không ai để ý. Cô ghi chép: ai theo ai, ai bất mãn, ai trung lập. Bản đồ quyền lực toàn công ty — Ngọc vẽ trong đầu."""),

("Chương 3: Bí Mật Của Cha", """Ngọc vào phòng cha ở bệnh viện mỗi ngày. Một ngày, cô tìm thấy trong tủ đồ cha: phong bì đóng dấu công chứng, ghi "Mở khi cha mất."

Ngọc mở — bên trong là di chúc: ông Đại để lại 40% cổ phần cho Ngọc, 30% cho Hùng, 30% cho Minh. Kèm thư viết tay: "Ngọc à, cha biết hai anh con giỏi nhưng không biết hợp tác. Con im lặng nhưng con nhìn rõ nhất. Cha tin con sẽ giữ được gia đình."

Ngọc đọc thư, khóc. Rồi cô cất di chúc — chưa công bố. Chưa đúng lúc."""),

("Chương 4: Ngọc Thu Phục Lòng Người", """Trong khi hai anh đánh nhau, Ngọc âm thầm làm việc mà không ai để ý: cô giải quyết vấn đề nhân sự — giữ lại nhân viên chủ chốt bằng cách tăng phúc lợi, lắng nghe, và cam kết ổn định.

Cô cũng gặp khách hàng lớn — những người đang muốn rời đi — và đảm bảo: "Tập đoàn Trương sẽ ổn. Tôi cam kết cá nhân."

Khách hàng tin Ngọc — vì cô là người duy nhất trong gia đình Trương nói chuyện kinh doanh thay vì chính trị nội bộ.

Sáu tháng: nhờ Ngọc, công ty mất ít khách hàng hơn dự kiến. Nhưng hai anh không biết."""),

("Chương 5: Hùng Phạm Sai Lầm Lớn", """Hùng — để nắm quyền nhanh — ký hợp đồng vận chuyển với đối tác Trung Quốc mà không qua HĐQT. Hợp đồng có điều khoản bất lợi: phạt vi phạm gấp mười lần giá trị hợp đồng.

Khi đối tác cố tình tạo vi phạm giả, Hùng bị kẹt — phạt hợp đồng ba trăm tỷ. Công ty đứng trước nguy cơ mất 30% doanh thu.

Hùng hoảng loạn: "Minh, giúp anh!"

Minh cười lạnh: "Anh tự ký, anh tự lo." """),

("Chương 6: Ngọc Cứu Công Ty", """Ngọc can thiệp. Cô bay sang Thượng Hải, gặp đối tác Trung Quốc, đàm phán — không phải bằng tiền, mà bằng đề xuất hợp tác logistics xuyên biên giới dài hạn, có lợi cho cả hai bên.

"Các anh phạt chúng tôi ba trăm tỷ, được một lần. Nhưng hợp tác dài hạn, các anh được hàng nghìn tỷ trong mười năm," Ngọc trình bày.

Đối tác đồng ý rút phạt — ký hợp đồng mới, có lợi hơn.

Hùng nhìn Ngọc khi cô về: "Em... em cứu anh."

"Em cứu công ty. Không phải cứu anh," Ngọc nói."""),

("Chương 7: Minh Phạm Sai Lầm Lớn Hơn", """Minh — thấy Hùng yếu — đẩy mạnh chiến dịch lật đổ: ông ta bí mật bán 10% cổ phần cho đối thủ cạnh tranh — Vinalink Logistics — để lấy tiền và liên minh.

Khi Ngọc phát hiện, cô hiểu: Minh không muốn giữ công ty — Minh muốn bán.

"Anh Minh, anh bán cổ phần cho đối thủ? Anh đang phản bội gia đình," Ngọc nói trong cuộc họp kín.

"Công ty này sẽ chết nếu không có đối tác chiến lược!" Minh hét.

"Công ty sẽ sống nếu anh em biết hợp tác. Nhưng anh không biết," Ngọc đáp."""),

("Chương 8: Công Bố Di Chúc", """Ngọc triệu tập HĐQT, công bố di chúc cha: 40% cho Ngọc, 30% Hùng, 30% Minh. Kèm thư tay — đọc to trước HĐQT.

Hai anh choáng váng. "Cha cho em 40%? Tại sao?" Hùng hỏi.

"Vì cha biết hai anh sẽ đánh nhau. Và cha biết em sẽ giữ," Ngọc nói.

Với 40% cổ phần + sự ủng hộ của nhân viên và khách hàng + 10% từ cổ đông thiểu số (mà Ngọc đã vận động), Ngọc nắm quyền kiểm soát 50%+."""),

("Chương 9: Sắp Xếp Lại Đế Chế", """Ngọc không đuổi hai anh. Cô sắp xếp: Hùng quản lý mảng vận tải (thế mạnh), Minh quản lý kho bãi (thế mạnh), Ngọc làm Chủ tịch HĐQT — kiểm soát chiến lược.

"Em không lấy hết. Em chia đúng. Mỗi người làm việc mình giỏi nhất. Đó là cách cha muốn."

Hùng phản đối yếu ớt, nhưng chấp nhận — vì anh biết: không có Ngọc, anh đã mất ba trăm tỷ.

Minh im lặng. Rồi gật đầu. Vì anh biết: không có Ngọc, anh đã bán công ty cho đối thủ."""),

("Chương 10: Cha Tỉnh Lại", """Sáu tháng sau, ông Đại tỉnh lại — yếu, nằm xe lăn, nhưng tỉnh. Ngọc đẩy xe lăn cha vào phòng họp — nơi ba anh em ngồi cùng nhau lần đầu tiên sau một năm.

"Cha ơi, công ty ổn. Anh Hùng quản lý vận tải tốt. Anh Minh quản lý kho bãi tốt. Con kiểm soát chiến lược."

Ông Đại nhìn ba đứa con, nước mắt chảy trên khuôn mặt già nua. Ông nắm tay Ngọc — bàn tay run run.

"Con gái... cha biết con sẽ giữ được."

Ngọc mỉm cười: "Cha dạy con: im lặng nhưng đừng bao giờ vắng mặt." """),

("Chương 11: Bức Thư Trong Tủ", """Ngọc về phòng riêng, mở lại bức thư cha. Đọc lại dòng cuối: "Ngọc à, con im lặng nhưng con nhìn rõ nhất. Cha tin con."

Cô gấp thư, cất vào tủ kính — cạnh ảnh gia đình chụp khi Ngọc còn nhỏ: bốn người, cười, ông Đại bế Ngọc trên vai.

Ngoài cửa sổ, bãi container của Tập đoàn Trương trải dài đến chân trời — đỏ, xanh, vàng, xếp thành hàng ngay ngắn.

Em gái út — người bị coi thường nhất — giờ giữ đế chế.

Không phải vì cô giành giật. Mà vì cô giữ."""),
]

# ═══════════════════════════════════════════════════════════════════════════════
# STORY 24: NỮ QUẢN LÝ QUỸ ĐỐI ĐẦU CHA NUÔI — 8 CHƯƠNG
# ═══════════════════════════════════════════════════════════════════════════════

S24_TITLE = "BỊ CHA NUÔI LỪA LẤY TOÀN BỘ QUỸ ĐẦU TƯ, CÔ GÁI MỒ CÔI LẬP QUỸ RIÊNG VÀ ĐÁNH BẠI ÔNG TA TRÊN SÀN CHỨNG KHOÁN"
S24_AUTHOR = "Hoàng Khánh Linh"
S24_COVER = "base_cover_27.png"
S24_INTRO = """<p>Hoàng Khánh Linh, mồ côi từ nhỏ, được ông Vũ Quốc Thắng — chủ quỹ đầu tư Thắng Capital — nhận nuôi. Linh tưởng cha nuôi yêu thương, nhưng thực chất ông ta cần cô: IQ 145, tốt nghiệp đầu MIT, và khả năng phân tích tài chính thiên tài.</p>
<p>Khi Linh phát hiện cha nuôi dùng tên cô để lừa nhà đầu tư, cô phải chọn: im lặng hay đối đầu người đã nuôi mình lớn.</p>"""

S24_CHAPTERS = [
("Chương 1: Cha Nuôi Và Con Gái Thiên Tài", """Linh được nhận nuôi năm mười tuổi — từ trại trẻ mồ côi số 5. Ông Thắng chọn Linh vì cô giải bài toán mà ông đưa ra trong ba phút — bài toán dành cho sinh viên đại học.

Mười năm nuôi dưỡng: trường quốc tế, gia sư riêng, SAT perfect score, MIT full scholarship. Linh yêu cha nuôi — người duy nhất cho cô gia đình.

Tốt nghiệp MIT, Linh về Việt Nam làm việc tại Thắng Capital — quỹ đầu tư chứng khoán do cha nuôi lập. Linh quản lý portfolio hai nghìn tỷ — trẻ nhất Việt Nam.

Nhưng Linh không biết: cha nuôi dùng tên cô — "Hoàng Khánh Linh, MIT, quản lý portfolio" — làm bình phong huy động vốn từ nhà đầu tư nước ngoài. Tiền vào — nhưng không đầu tư đúng chỗ."""),

("Chương 2: Phát Hiện Sự Thật", """Linh kiểm tra lại danh mục đầu tư — phát hiện: 40% vốn quỹ (tám trăm tỷ) không nằm trong portfolio mà cô quản lý. Tiền được chuyển vào tài khoản công ty con do ông Thắng đứng tên — đầu tư bất động sản rủi ro cao.

"Cha, tiền ở đâu?" Linh hỏi thẳng.

"Con đừng lo. Cha có kế hoạch."

"Cha, nhà đầu tư đổ tiền vào vì tin con quản lý. Nhưng con không quản lý tám trăm tỷ đó. Cha đang lừa họ bằng tên con."

Ông Thắng im lặng. Rồi nói, giọng lạnh — giọng mà Linh chưa bao giờ nghe: "Con sống được đến ngày hôm nay là nhờ cha. Con nợ cha."

Linh nhìn cha nuôi — mười năm yêu thương, hay mười năm đầu tư vào công cụ?"""),

("Chương 3: Chọn Lựa Đau Đớn", """Linh có hai lựa chọn: im lặng — giữ gia đình, nhưng đồng lõa lừa đảo. Hoặc tố giác — mất cha nuôi, nhưng bảo vệ nhà đầu tư và danh dự bản thân.

Ba đêm mất ngủ. Linh gọi cho người bạn MIT duy nhất cô tin tưởng: "Nếu người nuôi em lớn lừa dối em, em làm gì?"

"Linh, lòng biết ơn không phải xiềng xích."

Linh quyết định: tố giác. Không phải vì thù hận — mà vì cô không thể sống với tên mình trên bản cáo trạng."""),

("Chương 4: Tố Giác Và Chiến Tranh", """Linh gửi báo cáo cho Ủy ban Chứng khoán Nhà nước: chi tiết dòng tiền bất thường, tài khoản công ty con, và bằng chứng huy động vốn gian lận.

Ông Thắng phản ứng: ông ta kiện Linh "trộm dữ liệu nội bộ" và tuyên bố Linh "tâm thần, bất ổn" — chiến thuật discredit kinh điển.

Truyền thông chia rẽ: nửa ủng hộ Linh, nửa ủng hộ "cha nuôi tốt bụng bị con gái phản bội."

Linh im lặng trước truyền thông — cô để bằng chứng nói."""),

("Chương 5: UBCK Vào Cuộc — Sụp Đổ", """Ủy ban Chứng khoán xác nhận: Thắng Capital huy động vốn gian lận, sử dụng sai mục đích tám trăm tỷ đồng. Ông Thắng bị khởi tố.

Tại phiên tòa, ông Thắng nhìn Linh: "Cha nuôi con mười năm. Con trả cha thế này?"

Linh đáp, giọng run nhưng rõ ràng: "Cha nuôi con để dùng con. Nhưng con cảm ơn cha — vì nhờ cha, con biết phân biệt đúng sai."

Ông Thắng lĩnh mười hai năm tù."""),

("Chương 6: Lập Quỹ Riêng — Linh Capital", """Linh lập Linh Capital — quỹ đầu tư mới, minh bạch tuyệt đối. Mọi giao dịch công khai realtime trên dashboard cho nhà đầu tư xem.

"Tôi từng là bình phong. Giờ tôi là mặt tiền — và mặt tiền này trong suốt," Linh nói trong buổi ra mắt.

Nhà đầu tư tin tưởng — vì Linh đã chứng minh: cô chọn sự thật, dù sự thật đau đớn.

Ba năm: Linh Capital trở thành quỹ đầu tư hiệu suất cao nhất Việt Nam — ROI trung bình 28%/năm."""),

("Chương 7: Thăm Cha Trong Tù", """Linh đến thăm cha nuôi trong tù — mỗi tháng một lần. Mang theo sách, trái cây.

"Con vẫn thăm cha?"

"Con thăm vì con nợ cha mười năm nuôi dưỡng. Nhưng con không nợ cha sự im lặng trước gian lận."

Ông Thắng nhìn Linh: "Con giỏi hơn cha tưởng."

"Vì cha dạy con giỏi. Cha chỉ quên dạy con biết vâng lời." """),

("Chương 8: Quay Về Trại Trẻ Số 5", """Linh quay về trại trẻ mồ côi số 5 — nơi cô lớn lên mười năm đầu đời. Trại vẫn vậy: tường cũ, sân xi măng, giường tầng sắt.

Linh tặng trại một tỷ đồng — xây phòng máy tính, thư viện, và quỹ học bổng cho trẻ mồ côi giỏi toán.

Một bé gái mười tuổi — giống Linh năm xưa — giải bài toán trên bảng, nhanh, chính xác.

Linh nhìn bé, mỉm cười. Cô không nhận nuôi — vì cô biết: nhận nuôi có thể vì yêu, nhưng cũng có thể vì mục đích khác.

Thay vào đó, cô lập quỹ: mỗi trẻ mồ côi giỏi sẽ được tài trợ du học — không điều kiện, không ràng buộc, không nợ.

"Tôi muốn cho các em thứ cha nuôi tôi không cho: tự do." """),
]

# ═══════════════════════════════════════════════════════════════════════════════
# STORY 25: BS TRƯỞNG KHOA LẬP VIỆN RIÊNG — 10 CHƯƠNG
# ═══════════════════════════════════════════════════════════════════════════════

S25_TITLE = "BỊ GIÁM ĐỐC BỆNH VIỆN ÉP NGHỈ VÌ TỪ CHỐI NHẬN PHONG BÌ, BÁC SĨ LẬP VIỆN RIÊNG KHIẾN BỆNH NHÂN BỎ VIỆN LỚN"
S25_AUTHOR = "Trần Minh Đức"
S25_COVER = "base_cover_28.png"
S25_INTRO = """<p><strong>"Mười lăm năm tôi làm Trưởng khoa Ngoại, BV Nhân Dân — bệnh viện lớn nhất tỉnh. Tôi từ chối nhận phong bì vì tôi tin: bác sĩ cứu người, không bán người. Giám đốc ép tôi nghỉ vì tôi 'gây mất đoàn kết' — ý là tôi khiến bác sĩ khác xấu hổ."</strong></p>
<p>BS. Trần Minh Đức, trưởng khoa Ngoại giỏi nhất tỉnh, bị ép nghỉ vì từ chối phong bì và phản đối tham nhũng trong bệnh viện. Anh lập viện tư — nơi không phong bì, không sân sau, và bệnh nhân được đặt lên đầu.</p>"""

S25_CHAPTERS = [
("Chương 1: Phong Bì Bị Trả Lại", """Ca mổ thành công — ung thư đại tràng giai đoạn II, bệnh nhân Nguyễn Văn Tâm, năm mươi tuổi. Gia đình mang phong bì — năm triệu — đến phòng trực.

BS. Đức trả lại: "Cảm ơn gia đình, nhưng tôi không nhận phong bì. Lương bệnh viện trả cho tôi rồi."

Gia đình ngạc nhiên — vì ở bệnh viện này, phong bì là "luật bất thành văn." Không phong bì = bác sĩ lạnh nhạt, ca mổ bị xếp cuối.

BS. Đức biết: đồng nghiệp nhận phong bì trung bình năm đến hai mươi triệu mỗi ca. Trưởng khoa khác thu nhiều hơn. Giám đốc bệnh viện — PGS. Lê Quang Hải — biết và im lặng — vì chính ông cũng nhận.

"Đức à, sao em cứ gây khó? Em không nhận, bệnh nhân sẽ nghĩ bệnh viện mình lạ. Ảnh hưởng đồng nghiệp," giám đốc Hải nói.

"Anh ơi, phong bì ảnh hưởng bệnh nhân nghèo. Họ vay nợ để bỏ phong bì," Đức đáp."""),

("Chương 2: Bị Cô Lập Trong Bệnh Viện", """Đồng nghiệp xa lánh Đức — vì anh "phá luật." Hộ lý không hợp tác: bệnh nhân Đức mổ bị xếp giường xấu nhất, thuốc đặt chậm.

Giám đốc Hải cắt giảm budget khoa Đức: không mua thiết bị mới, không cử đi đào tạo.

"Anh muốn ép tôi nghỉ," Đức nói thẳng.

"Anh không ép. Anh chỉ phân bổ nguồn lực hợp lý," Hải đáp, cười nhạt.

Đức biết: nếu ở lại, bệnh nhân của anh sẽ thiệt. Nếu nghỉ, bệnh nhân mất bác sĩ giỏi nhất."""),

("Chương 3: Nộp Đơn Nghỉ — Và Lập Viện", """Đức nộp đơn nghỉ việc. Dùng tiền tiết kiệm mười lăm năm — hai tỷ — thuê mặt bằng, lập Phòng khám Minh Đức. Quy mô nhỏ: hai phòng khám, một phòng tiểu phẫu, năm giường bệnh.

Quy tắc số 1: KHÔNG PHONG BÌ. Bảng ghi lớn treo ngay cửa: "Phòng khám Minh Đức — Không nhận phong bì, quà tặng dưới mọi hình thức."

Đồng nghiệp cười: "Đức điên. Không phong bì thì sống bằng gì?"

"Bằng lương. Bằng viện phí hợp lý. Bằng lương tâm." """),

("Chương 4: Bệnh Nhân Đổ Về", """Tin đồn lan: "Có phòng khám không phong bì." Bệnh nhân nghèo — những người từng vay nợ bỏ phong bì — đổ về Minh Đức.

Bà Nguyễn Thị Lụa, sáu mươi tuổi, khối u vú: "Tôi đi BV Nhân Dân, họ bảo mổ mười triệu, phong bì năm triệu nữa. Tôi không có tiền phong bì nên bị xếp chờ ba tháng."

Đức mổ cho bà Lụa — viện phí đúng quy định, không phong bì.

"Bác sĩ ơi, sao bác sĩ tốt thế?"

"Tôi không tốt. Tôi chỉ làm đúng." """),

("Chương 5: Giám Đốc Hải Phản Công", """Hải thấy bệnh nhân rời BV Nhân Dân sang Minh Đức — mất doanh thu. Hải vận động: cản trở giấy phép mở rộng, chỉ đạo bệnh viện không chuyển viện sang Minh Đức.

Thêm nữa: Hải tung tin "BS. Đức bị đuổi vì vi phạm y đức" — dù sự thật ngược lại.

Đức không đáp trả trực tiếp. Anh quay video ca mổ (được bệnh nhân đồng ý), đăng YouTube: "Quy trình mổ minh bạch — không phong bì." Video đạt năm triệu lượt xem."""),

("Chương 6: Bí Mật Của BV Nhân Dân", """Một cựu kế toán BV Nhân Dân liên hệ Đức: "Anh ơi, em có bằng chứng: giám đốc Hải rút quỹ bảo hiểm y tế, khai khống thuốc, và ăn chênh giá thiết bị y tế — tổng cộng hơn hai mươi tỷ trong năm năm."

Đức gửi bằng chứng cho Bộ Y tế và Thanh tra Chính phủ.

Điều tra: xác nhận gian lận. Hải bị đình chỉ chức vụ, khởi tố."""),

("Chương 7: Mẹ Và Viên Thuốc", """Đức theo nghề vì mẹ. Bà Trần Thị Hoa, y tá huyện — lương hai triệu, tiêm, phát thuốc, đỡ đẻ, sơ cứu — một mình phụ trách trạm y tế xã.

"Mẹ ơi, sao mẹ không nhận quà của bệnh nhân?"

"Vì họ nghèo hơn mẹ. Mẹ nhận quà của họ, mẹ ăn cắp."

Câu nói đó Đức mang theo suốt mười lăm năm hành nghề. "Nhận phong bì là ăn cắp của người bệnh — vì họ vay nợ để mua hy vọng sống." """),

("Chương 8: BV Nhân Dân Thay Đổi", """Giám đốc mới BV Nhân Dân — được bổ nhiệm sau khi Hải bị khởi tố — ban hành quy định: CẤM phong bì trong toàn bệnh viện. Gắn camera phòng trực. Lập đường dây tố giác.

Bệnh nhân vỗ tay. Bác sĩ phản đối ngầm nhưng chấp nhận.

"BS. Đức, nhờ anh mà bệnh viện thay đổi," giám đốc mới nói.

"Không nhờ tôi. Nhờ bệnh nhân — họ đã chịu đựng quá lâu." """),

("Chương 9: Bệnh Viện Minh Đức Ra Đời", """Phòng khám Minh Đức nâng cấp thành Bệnh viện Minh Đức — trăm giường, mười chuyên khoa. Quy tắc: không phong bì, viện phí minh bạch, bệnh nhân nghèo giảm 50%.

Hai mươi bác sĩ trẻ rời BV lớn về Minh Đức — vì "ở đây tôi tập trung chữa bệnh, không phải tập trung thu tiền."

Forbes Vietnam: "BS. Đức — người thay đổi văn hóa phong bì." """),

("Chương 10: Ca Trực Đêm", """Đêm khuya, phòng trực Bệnh viện Minh Đức. Đức vừa mổ xong ca cấp cứu — vỡ lách do tai nạn. Bệnh nhân ổn.

Gia đình mang phong bì đến — theo thói quen.

Đức trả lại: "Cảm ơn gia đình. Nhưng ở đây không nhận phong bì."

Người nhà ngạc nhiên: "Bác sĩ ơi, thật à? Bệnh viện nào cũng nhận mà."

"Bệnh viện này không. Vì bác sĩ ở đây tin: cứu người là việc nên làm, không phải hàng để bán."

Đức quay về phòng trực, rửa tay, ngồi xuống ghế, uống ly cà phê nguội. Đồng hồ chỉ hai giờ sáng.

Trên bàn, tấm ảnh mẹ — bà y tá huyện, tay cầm ống tiêm, cười.

Đức mỉm cười theo, rồi nhấc điện thoại: "Phòng cấp cứu, có ca mới không?" """),
]

# ═══════════════════════════════════════════════════════════════════════════════
# ASSEMBLY & PUBLISHING
# ═══════════════════════════════════════════════════════════════════════════════

ALL_STORIES = [
    {"title": S21_TITLE, "author": S21_AUTHOR, "cover": S21_COVER, "intro": S21_INTRO, "chapters": S21_CHAPTERS, "genre": "Cung Đấu"},
    {"title": S22_TITLE, "author": S22_AUTHOR, "cover": S22_COVER, "intro": S22_INTRO, "chapters": S22_CHAPTERS, "genre": "Cung Đấu"},
    {"title": S23_TITLE, "author": S23_AUTHOR, "cover": S23_COVER, "intro": S23_INTRO, "chapters": S23_CHAPTERS, "genre": "Cung Đấu"},
    {"title": S24_TITLE, "author": S24_AUTHOR, "cover": S24_COVER, "intro": S24_INTRO, "chapters": S24_CHAPTERS, "genre": "Cung Đấu"},
    {"title": S25_TITLE, "author": S25_AUTHOR, "cover": S25_COVER, "intro": S25_INTRO, "chapters": S25_CHAPTERS, "genre": "Cung Đấu"},
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
            "title": s["title"], "author": s["author"], "genre": s["genre"],
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
    log("🚀 MIX BATCH 5 — 5 STORIES (⚔️ Cung Đấu)")
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
            subtitle = f"Cung đấu văn của {n['author']}"
            cmd = ["python3", os.path.join(BASE_DIR, "cover_overlay_standard.py"),
                   "--input", base, "--output", out, "--title", n["title"],
                   "--subtitle", subtitle]
            r = subprocess.run(cmd, capture_output=True, text=True)
            if r.returncode == 0 and os.path.exists(out):
                rid = random.randint(100000,999999)
                cover_file = f"cover_sideload_{rid}.png"
                ftp = get_ftp(); ftp.cwd("wp-content/uploads")
                with open(out,"rb") as cf: ftp.storbinary(f"STOR {cover_file}", cf)
                ftp.quit(); os.remove(out)
                log(f"✓ Cover uploaded: {cover_file}")

        payload = {"secret_token": SECRET_TOKEN, "title": n["title"], "intro": n["intro"],
                   "author": n["author"], "genre": n["genre"], "chapters": n["chapters"]}
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

    log(f"\n🏁 MIX BATCH 5 COMPLETE: {len(results)}/5 published")
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
            print(f"   ✍️ {n['author']} | 🏷️ {n.get('genre','?')} | 📊 {n['_stats']}")
            for ch in n["chapters"]:
                print(f"   → {ch['title']} ({ch['content'].count('<p>')} sentences)")
    elif a.live:
        publish_all(novels)
