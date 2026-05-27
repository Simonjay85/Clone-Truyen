#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
write_batch_mix_06.py — Batch 6: 5 Truyện MIX TỔNG HỢP (Stories 26-30)
=========================================================================
Mix all 4 genres for variety:
Story 26: Sảng Văn (Template A) — 9 ch — cover 29
Story 27: Ngược (Template B) — 10 ch — cover 30
Story 28: Ngọt (Template C) — 8 ch — cover 31
Story 29: Cung Đấu (Template D) — 11 ch — cover 32
Story 30: Sảng Văn (Template A) — 10 ch — cover 33
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
# STORY 26: SẢNG VĂN — THỢ CẮT TÓC BỊ ĐUỔI — 9 CHƯƠNG
# ═══════════════════════════════════════════════════════════════════════════════

S26_TITLE = "BỊ ĐUỔI KHỎI SALON VÌ 'CẮT QUÁ RẺ,' TÔI MỞ TIỆM VỈA HÈ KHIẾN CẢ THÀNH PHỐ XẾP HÀNG"
S26_AUTHOR = "Võ Quốc Bảo"
S26_COVER = "base_cover_29.png"
S26_INTRO = """<p><strong>"Chủ salon bảo tôi: 'Mày cắt giá năm mươi nghìn thì tao bán gì? Mày phá giá thị trường!' Tôi trả lời: 'Tôi không phá giá — tôi cắt cho người không có tiền cắt giá cao.'"</strong></p>
<p>Võ Quốc Bảo, thợ cắt tóc 27 tuổi, bị sa thải vì cắt tóc quá rẻ. Anh kéo chiếc ghế nhựa ra vỉa hè, treo tấm bảng "Cắt tóc 30K" — và tạo ra hiện tượng.</p>"""

S26_CHAPTERS = [
("Chương 1: Bị Đuổi Khỏi Salon Sang", """Salon Đẹp Plus — chuỗi salon lớn nhất quận 7, Sài Gòn. Chủ salon Trần Văn Hiếu gọi Bảo vào phòng: "Bảo, tao sa thải mày."

"Tại sao anh? Em làm sai gì?"

"Mày cắt giá năm mươi nghìn cho khách nghèo, trong khi salon tao thu hai trăm nghìn. Khách thấy mày rẻ thì đòi giảm giá. Mày phá giá thị trường."

"Anh ơi, bác xe ôm đó lương ngày ba trăm nghìn. Em lấy hai trăm nghìn, bác ấy ăn gì?"

"Đó là vấn đề của bác ấy, không phải của salon tao."

Bảo thu dọn đồ: một bộ tông đơ, hai cái kéo Nhật, và chiếc ghế xoay cũ. Bảy năm làm thợ cắt tóc giỏi nhất salon — ra đi với ba món đồ."""),

("Chương 2: Chiếc Ghế Nhựa Trên Vỉa Hè", """Bảo kéo chiếc ghế nhựa ra vỉa hè trước nhà trọ — hẻm nhỏ quận Bình Thạnh. Treo tấm bảng carton viết tay: "CẮT TÓC 30K — ĐẸP NHƯ SALON."

Ngày đầu: ba khách. Bác xe ôm, chú bảo vệ chung cư, cậu sinh viên. Bảo cắt — nghiêm túc như cắt trong salon: tỉa, gội, sấy, vuốt gel.

"Ê, ba mươi nghìn mà sấy luôn hả?"

"Dạ, cắt tóc phải đẹp. Đẹp không phân biệt giá tiền."

Ngày thứ ba: mười khách. Ngày thứ bảy: hai mươi khách — xếp hàng trên vỉa hè.

"Sao đông thế?"

"Vì thằng Bảo cắt đẹp mà rẻ. Salon hai trăm cũng không đẹp bằng." """),

("Chương 3: Viral — Video Triệu View", """Một tiktoker quay video Bảo cắt tóc trên vỉa hè — zoom vào tay Bảo cầm kéo: chính xác, nhanh, nghệ thuật. Cùng một kiểu tóc mà salon thu hai trăm nghìn, Bảo làm trên ghế nhựa với ba mươi nghìn.

Video đạt mười triệu view. Caption: "Thợ cắt tóc giỏi nhất Sài Gòn ngồi vỉa hè."

Khách đổ về từ khắp thành phố. Bảo phải đặt lịch hẹn — và vẫn chỉ thu ba mươi nghìn.

"Sao anh không tăng giá? Khách đông mà."

"Vì khách đầu tiên của tôi là bác xe ôm. Tôi tăng giá, bác ấy không cắt được nữa." """),

("Chương 4: Salon Đẹp Plus Phản Công", """Hiếu — chủ salon cũ — thấy mất khách. Anh ta đăng Facebook: "Cắt tóc vỉa hè không đảm bảo vệ sinh. Dùng kéo bẩn, ghế nhựa nhiễm khuẩn. Coi chừng nấm da đầu."

Bảo đáp — không trên mạng — mà bằng hành động: anh mua tủ tiệt trùng UV, khăn mới mỗi khách, kéo Nhật rửa cồn sau mỗi lần cắt. Và quay video quy trình vệ sinh đăng lên.

"Vệ sinh không phụ thuộc salon hay vỉa hè. Vệ sinh phụ thuộc người thợ." """),

("Chương 5: Tiệm Tóc Bảo Ra Đời", """Tiết kiệm sau sáu tháng vỉa hè, Bảo thuê mặt bằng nhỏ — hai mươi mét vuông, sát chợ. Sửa sang giản dị: ghế cắt tóc secondhand, gương, và tấm bảng: "Tiệm Tóc Bảo — 50K."

Năm mươi nghìn — tăng từ ba mươi vì có phòng, có máy lạnh. Nhưng vẫn rẻ nhất thành phố cho chất lượng salon.

Quy tắc: không upsell, không ép mua dầu gội, không "anh nên nhuộm thêm." Cắt xong, trả tiền, đi. Đơn giản.

Khách xếp hàng mỗi ngày — từ bác xe ôm đến giám đốc công ty. Vì ở đây, mọi người bình đẳng trước chiếc ghế cắt tóc."""),

("Chương 6: Hiếu Xin Hợp Tác", """Sáu tháng sau, Salon Đẹp Plus doanh thu giảm 40%. Hiếu gọi điện cho Bảo: "Bảo à, mình hợp tác đi. Anh nhượng quyền salon cho em, em quản lý."

"Anh ơi, salon anh thu hai trăm nghìn, em thu năm mươi. Triết lý khác nhau."

"Nhưng em giỏi hơn mọi thợ của anh!"

"Giỏi không phải lý do. Lý do là em muốn mọi người đều được cắt tóc đẹp — không phải chỉ người có tiền."

Hiếu cúp máy. Sáu tháng sau, Salon Đẹp Plus đóng cửa ba chi nhánh."""),

("Chương 7: Mẹ Và Chiếc Kéo Cũ", """Bảo theo nghề vì mẹ. Bà Võ Thị Lan, thợ cắt tóc chợ Bà Chiểu — cắt tóc bằng kéo cũ, ghế gỗ, không salon, không bảng hiệu. Năm nghìn đồng một lần cắt.

"Mẹ ơi, sao mẹ cắt rẻ thế?"

"Vì khách mẹ là bà bán rau, ông lái xe ba gác. Họ không có tiền salon. Nhưng họ cũng muốn đẹp."

Bảo thừa hưởng triết lý: đẹp không phân biệt giàu nghèo. Chiếc kéo cũ của mẹ — anh giữ trong tủ kính tiệm, bên cạnh bộ kéo Nhật."""),

("Chương 8: Chuỗi Tiệm Tóc Bảo — Cắt Đẹp Giá Rẻ", """Hai năm sau: Tiệm Tóc Bảo mở năm chi nhánh — Bình Thạnh, Gò Vấp, Tân Bình, Thủ Đức, quận 12. Giá thống nhất: năm mươi nghìn.

Mỗi chi nhánh: ba thợ, đào tạo theo chuẩn Bảo — cắt đẹp, vệ sinh, không upsell.

Báo chí: "Tiệm Tóc Bảo — chuỗi cắt tóc giá rẻ chất lượng salon đầu tiên tại Việt Nam."

Doanh thu: không cao. Lợi nhuận: vừa đủ. Nhưng mỗi ngày, hai trăm người — bác xe ôm, chú bảo vệ, cô giúp việc — được cắt tóc đẹp với giá họ trả được."""),

("Chương 9: Chiếc Ghế Nhựa Vẫn Còn", """Mỗi Chủ nhật, Bảo kéo chiếc ghế nhựa cũ ra vỉa hè — cắt tóc miễn phí cho người vô gia cư, bán vé số, xe ôm.

"Anh Bảo, anh có năm chi nhánh rồi mà sao vẫn ra vỉa hè?"

"Vì vỉa hè là nơi tôi bắt đầu. Và vì ở đây, tôi nhớ tại sao tôi cắt tóc."

Chiều Chủ nhật, Sài Gòn nắng nhẹ. Bảo ngồi trên ghế nhựa, cầm kéo Nhật, cắt tóc cho bác bán vé số — cẩn thận, tỉ mỉ, như cắt cho khách VIP.

"Đẹp rồi bác. Bác về nhé."

"Cảm ơn con. Lâu rồi bác không cắt tóc đẹp thế này."

Bảo cười, rồi gọi người tiếp theo: "Mời bác ngồi." """),
]

# ═══════════════════════════════════════════════════════════════════════════════
# STORY 27: NGƯỢC — BÉ GÁI BỊ BÁN QUA BIÊN GIỚI — 10 CHƯƠNG
# ═══════════════════════════════════════════════════════════════════════════════

S27_TITLE = "BỊ BÁN QUA BIÊN GIỚI NĂM MƯỜI HAI TUỔI, TÔI TRỐN VỀ VÀ TRỞ THÀNH LUẬT SƯ BẢO VỆ TRẺ EM"
S27_AUTHOR = "Vàng Thị Mai"
S27_COVER = "base_cover_30.png"
S27_INTRO = """<p>Vàng Thị Mai, người H'Mông, mười hai tuổi bị kẻ buôn người lừa bán qua Trung Quốc. Mười tháng bị giam, bị đánh, bị bỏ đói. Cô trốn thoát — chạy bộ ba ngày qua rừng về Việt Nam.</p>
<p>Mười lăm năm sau, Mai trở thành luật sư chuyên bảo vệ trẻ em bị buôn bán — người phụ nữ H'Mông đầu tiên trong lịch sử tỉnh Lào Cai tốt nghiệp Đại học Luật.</p>"""

S27_CHAPTERS = [
("Chương 1: Cô Bé Mười Hai Tuổi", """Vàng Thị Mai sinh ở bản Lao Chải, Sa Pa — bản nghèo nhất huyện, không điện, không đường, không trường cấp ba. Mười hai tuổi, Mai xinh, ngây thơ, chưa ra khỏi bản lần nào.

Một người phụ nữ đến bản — nói tiếng H'Mông, mặc đẹp, tặng kẹo: "Mai ơi, đi với chị xuống thành phố. Chị xin cho Mai việc làm, kiếm tiền gửi về cho bố mẹ."

Bố mẹ Mai nghèo — bốn đứa con, nương ngô không đủ ăn. Họ tin. Mai tin. Cô bé leo lên xe máy, rời bản — không biết rằng mình đang bị bán.

Hai ngày sau, Mai ở bên kia biên giới — một ngôi nhà kín cửa ở Vân Nam, Trung Quốc. Cánh cửa khóa ngoài."""),

("Chương 2: Mười Tháng Địa Ngục", """Mai bị nhốt cùng ba cô gái khác — đều người H'Mông, đều bị lừa. Mỗi ngày: ăn cơm nguội, uống nước lã, không được ra ngoài.

Kẻ buôn người nói: "Mày sẽ làm vợ người Trung Quốc. Đừng trốn — biên giới xa, không ai cứu mày."

Mai bị đánh khi cố mở cửa. Bị bỏ đói khi khóc. Mười hai tuổi, cô bé không hiểu tại sao thế giới lại tàn nhẫn thế.

Nhưng Mai nhớ: bà ngoại từng kể chuyện con hổ H'Mông — bị bẫy nhưng không bao giờ chết trong bẫy. Hổ chờ — rồi thoát."""),

("Chương 3: Trốn Chạy — Ba Ngày Qua Rừng", """Đêm mưa, kẻ canh gác say rượu. Mai cạy khóa cửa sổ bằng chiếc thìa mài nhọn — cô mài mười tháng.

Chạy. Đêm tối, rừng sâu, không đường, không bản đồ. Mai chạy theo hướng mặt trời mọc — vì bà ngoại dạy: "Việt Nam ở phía mặt trời mọc."

Ba ngày: uống nước suối, ăn lá rừng, ngủ trên cây. Chân rách, tay sưng, sốt cao. Nhưng Mai không dừng.

Ngày thứ ba, cô gặp bộ đội biên phòng Việt Nam — đồn Bát Xát, Lào Cai. Cô ngã quỵ trước cổng đồn, nói một câu bằng tiếng H'Mông: "Em muốn về nhà." """),

("Chương 4: Về Nhà — Nhưng Nhà Đã Khác", """Mai được đưa về bản Lao Chải. Bố mẹ khóc. Bản làng nhìn Mai bằng ánh mắt thương hại — và định kiến: "Con bé bị bán rồi, ai lấy nữa?"

Mai không nói chuyện ba tháng — chấn thương tâm lý. Cô ngồi im trong nhà, không ra ngoài, không cười.

Cô Nguyễn Thị Lan — giáo viên cắm bản — đến nhà mỗi ngày. Không ép Mai nói. Chỉ ngồi cạnh, đọc sách to.

Ngày thứ chín mươi, Mai nói — câu đầu tiên: "Cô ơi, cho em đi học."

"Em muốn học gì?"

"Em muốn học... để không ai bị bán như em nữa." """),

("Chương 5: Đi Học — Từ Bản Lên Huyện", """Mai đi bộ mười cây số mỗi ngày — từ bản Lao Chải xuống trường cấp hai huyện. Bốn giờ sáng dậy, đi bộ, học, đi bộ về.

Bạn bè trêu: "Con bé bị bán." Mai im lặng. Cô học — như con hổ bà ngoại kể: kiên nhẫn, không bỏ cuộc.

Lớp sáu: đứng cuối. Lớp bảy: đứng giữa. Lớp tám: đứng nhất. Lớp chín: thủ khoa huyện.

Cô Lan khóc khi nhìn bảng điểm: "Mai ơi, em giỏi quá."

"Không giỏi, cô ơi. Em chỉ sợ. Sợ nếu em không học, em sẽ bị bán lần nữa." """),

("Chương 6: Đại Học Luật — Giấc Mơ Không Tưởng", """Mai thi đỗ Đại học Luật Hà Nội — cô gái H'Mông đầu tiên từ huyện Sa Pa vào trường luật.

Ở Hà Nội: Mai ở ký túc xá, ăn cơm sinh viên, làm thêm rửa bát quán ăn. Tiền học bổng + tiền rửa bát = vừa đủ sống.

Bạn đại học hỏi: "Sao Mai học luật?"

"Vì em bị bán năm mười hai tuổi. Không ai bảo vệ em. Em muốn trở thành người bảo vệ." """),

("Chương 7: Luật Sư Vàng Thị Mai", """Tốt nghiệp loại giỏi. Mai không ở Hà Nội — cô về Lào Cai, mở văn phòng luật sư miễn phí cho phụ nữ và trẻ em bị buôn bán.

Văn phòng: một phòng nhỏ trong thị trấn Sa Pa. Bàn gỗ, hai ghế, và tấm biển: "Luật sư Vàng Thị Mai — Bảo vệ phụ nữ và trẻ em miễn phí."

Ca đầu tiên: bé gái mười ba tuổi, người Dao, bị lừa giống Mai. Mai đại diện pháp lý, đưa kẻ buôn người ra tòa — mười hai năm tù.

Bé gái ôm Mai: "Chị ơi, cảm ơn chị."

"Em không cần cảm ơn. Chị từng là em." """),

("Chương 8: Chiến Dịch Chống Buôn Người", """Mai lập "Mạng lưới An Toàn" — hệ thống cảnh báo buôn người ở các bản vùng cao. Tình nguyện viên: phụ nữ H'Mông, Dao, Tày — những người từng bị lừa hoặc suýt bị lừa.

"Chúng tôi dạy bà con nhận biết chiêu trò: 'đi thành phố làm việc,' 'lấy chồng giàu,' 'du lịch miễn phí.' Và dạy: nếu thấy người lạ rủ con gái đi, gọi ngay cho chúng tôi."

Ba năm: Mạng lưới An Toàn ngăn chặn hai mươi ba vụ buôn người, cứu bốn mươi phụ nữ và trẻ em."""),

("Chương 9: Bà Ngoại Và Con Hổ", """Mai theo nghề vì bà ngoại. Bà Vàng Thị Páo, tám mươi tuổi, thêu thổ cẩm ở bản Lao Chải.

"Bà ơi, sao bà kể chuyện con hổ hoài?"

"Vì hổ là con vật mạnh nhất rừng. Nhưng hổ không mạnh vì nanh vuốt — hổ mạnh vì kiên nhẫn. Hổ chờ đúng lúc, rồi vồ."

Mai mang triết lý hổ vào cuộc sống: chờ mười tháng trong căn phòng khóa, chờ chiếc thìa mài nhọn, chờ đêm mưa. Rồi vồ — chạy ba ngày qua rừng.

"Bà ơi, con đã thành hổ chưa?"

"Con thành rồi. Nhưng hổ thật không hỏi mình có phải hổ không." Bà cười."""),

("Chương 10: Bình Minh Sa Pa", """Năm giờ sáng, Sa Pa sương mù dày. Mai đứng trên đỉnh dốc nhìn xuống bản Lao Chải — ruộng bậc thang xanh, mái nhà gỗ nâu, khói bếp bay lên.

Mười lăm năm trước, cô bé mười hai tuổi rời bản trên chiếc xe máy — không biết mình đang bị bán.

Hôm nay, luật sư Vàng Thị Mai đứng đây — bằng đại học luật trong tay, văn phòng luật sư dưới chân núi, và bốn mươi phụ nữ đã được cứu.

Điện thoại reo: "Chị Mai ơi, có bé gái ở Bắc Hà bị người lạ rủ đi!"

Mai nhấc máy: "Em gửi địa chỉ. Chị lên ngay."

Cô bước xuống dốc, vào xe máy, chạy về phía Bắc Hà — mặt trời mọc sau lưng, sương tan dần, và con hổ H'Mông lại lên đường."""),
]

# ═══════════════════════════════════════════════════════════════════════════════
# STORY 28: NGỌT — ÔNG BÁN CHÈ VÀ CẬU BÉ MỒ CÔI — 8 CHƯƠNG
# ═══════════════════════════════════════════════════════════════════════════════

S28_TITLE = "ÔNG GIÀ BÁN CHÈ ĐÊM VÀ CẬU BÉ MỒ CÔI — CÂU CHUYỆN VỀ TÔ CHÈ ẤM NHẤT SÀI GÒN"
S28_AUTHOR = "Trần Văn Phước"
S28_COVER = "base_cover_31.png"
S28_INTRO = """<p>Ông Trần Văn Phước, bảy mươi tuổi, bán chè đêm ở vỉa hè quận 5, Sài Gòn. Mỗi đêm từ chín giờ tối đến hai giờ sáng, chiếc xe chè của ông sáng đèn ở góc đường — nơi bảo vệ, tài xế xe ôm, sinh viên đến ăn chè và kể chuyện.</p>
<p>Một đêm, cậu bé mười tuổi — bẩn, gầy, ngồi cạnh xe chè — thay đổi cuộc đời ông mãi mãi.</p>"""

S28_CHAPTERS = [
("Chương 1: Xe Chè Đêm Góc Đường", """Ông Phước bán chè đêm ba mươi năm — kể từ khi vợ mất. Xe chè: thùng nhôm sáng bóng, sáu nồi chè — chè đậu đen, đậu xanh, bắp, khoai môn, thập cẩm, chè trôi nước.

"Sao ông bán đêm?"

"Vì ban ngày người ta bận. Ban đêm người ta cô đơn. Ăn tô chè nóng lúc mười hai giờ đêm — ấm bụng, ấm lòng."

Khách quen: bác bảo vệ chung cư Hùng, anh xe ôm công nghệ Dũng, chị bán hàng online Thảo, cậu sinh viên Tú. Mỗi người một câu chuyện — ông Phước nghe hết, nhớ hết.

"Ông Phước ơi, sao ông nhớ tên tụi con hết?"

"Vì mỗi người đến đây đều quan trọng. Tô chè thì giống nhau, nhưng người ăn thì khác nhau." """),

("Chương 2: Cậu Bé Ngồi Cạnh Xe Chè", """Một đêm mưa, khoảng mười một giờ, ông Phước thấy: cậu bé gầy, quần áo rách, chân đất, ngồi co ro cạnh xe chè — nhìn nồi chè bằng đôi mắt đói.

"Con ơi, con muốn ăn chè không?"

Cậu bé lắc đầu — nhưng bụng sôi.

Ông Phước múc tô chè đậu đen, đặt trước mặt: "Ăn đi con. Ông mời."

Cậu bé ăn — nhanh, ngấu nghiến, như chưa ăn mấy ngày. Ăn xong, cậu lau miệng, nói nhỏ: "Cảm ơn ông."

"Con tên gì?"

"Con tên Bảo. Mười tuổi."

"Bố mẹ con đâu?"

Im lặng. Cậu bé không trả lời — vì câu trả lời là: không có."""),

("Chương 3: Ông Phước Đưa Bảo Về Nhà", """Ông Phước không hỏi thêm. Đêm đó, ông đưa Bảo về phòng trọ — căn phòng mười hai mét vuông ở hẻm quận 5.

"Con ngủ giường ông. Ông ngủ võng."

"Ông ơi, ông không sợ con ăn trộm?"

"Con đói đến mức ăn chè ngấu nghiến thế kia thì con cần giúp, không phải sợ."

Bảo ở lại đêm đó. Rồi đêm sau. Rồi đêm sau nữa. Ông Phước không nói "ở lại" hay "đi đi" — ông chỉ nấu cơm đủ hai người, mua thêm chiếc chiếu, và mỗi sáng hỏi: "Con ăn sáng gì?"

Bảo — cậu bé mồ côi lang thang ba năm — lần đầu tiên có người hỏi "con ăn sáng gì." """),

("Chương 4: Dạy Bảo Đọc Chữ", """Bảo không biết đọc. Mười tuổi, chưa đi học ngày nào. Bố mất khi Bảo bốn tuổi, mẹ bỏ đi, Bảo sống với bà — bà mất khi Bảo bảy tuổi. Từ đó: đường phố.

Ông Phước dạy Bảo đọc — bằng menu chè. "Chè đậu đen — đ-ậ-u đ-e-n. Đọc đi con."

Bảo đọc chậm, sai, đọc lại. Mỗi tối, sau khi đẩy xe chè về, ông Phước ngồi dạy Bảo — đến khi cậu ngủ gục trên bàn.

Ba tháng: Bảo đọc được menu. Sáu tháng: đọc được truyện tranh. Một năm: đọc được báo.

"Ông ơi, ông dạy con giỏi hơn thầy giáo!"

"Ông không giỏi. Ông kiên nhẫn. Giống nấu chè — chè ngon phải nấu chậm." """),

("Chương 5: Bảo Đi Học", """Ông Phước đăng ký cho Bảo vào trường tiểu học — lớp tình thương dành cho trẻ em đường phố. Bảo mười một tuổi, học lớp một.

"Con lớn hơn bạn bè bốn tuổi. Con có xấu hổ không?"

"Không. Vì ông dạy con: xấu hổ là khi mình không cố gắng. Con cố gắng thì không xấu hổ."

Bảo học nhanh — vì cậu đã biết đọc nhờ menu chè. Lớp một nửa năm, chuyển lên lớp hai. Rồi lớp ba. Cậu bé đường phố đuổi kịp bạn bè.

Ông Phước bán chè thêm hai tiếng mỗi đêm — từ hai giờ sáng đến bốn giờ — để có tiền mua sách vở cho Bảo."""),

("Chương 6: Ông Ốm — Bảo Đẩy Xe Chè", """Ông Phước bảy mươi ba tuổi, bị viêm khớp nặng — không đẩy xe chè ra vỉa hè được. Bảo — giờ mười ba — nói: "Ông nghỉ. Con bán."

Bảo đẩy xe chè ra góc đường, múc chè cho khách, tính tiền, rửa bát. Mười ba tuổi, cậu bé làm chủ xe chè — thuần thục như ông Phước.

Khách quen hỏi: "Ông Phước đâu?"

"Ông ốm. Con bán thay ông."

"Chè con nấu có ngon bằng ông không?"

"Ông dạy con nấu. Cùng công thức. Cùng tình," Bảo cười.

Ông Phước nằm nhà, nghe Bảo kể: "Hôm nay bán hết sáu nồi, ông ơi!"

Ông cười, mắt ướt — vì đứa trẻ mồ côi ngày xưa giờ biết chăm người khác."""),

("Chương 7: Bảo Lớn — Ông Già Đi", """Bảo mười tám tuổi, thi đỗ Đại học Bách khoa — ngành Cơ khí. Ông Phước bảy mươi tám, lưng còng, tay run, không bán chè nữa.

"Ông ơi, con đi học xa, ai chăm ông?"

"Ông tự chăm. Con đi học cho giỏi."

Bảo đi — nhưng mỗi cuối tuần về thăm, nấu cơm, dọn nhà, và đẩy xe chè ra vỉa hè bán — "để ông vui."

"Con ơi, con không cần bán chè nữa."

"Con biết. Nhưng xe chè này là nhà con — nơi con gặp ông. Con không bỏ nhà." """),

("Chương 8: Tô Chè Cuối Cùng", """Sinh nhật Bảo hai mươi tuổi. Ông Phước — tám mươi — vào bếp, nấu chè đậu đen — tô chè đầu tiên ông nấu cho Bảo mười năm trước.

Tay run, múc chè chậm, đường hơi nhiều — nhưng khi Bảo ăn, đó là tô chè ngon nhất đời cậu.

"Ông ơi, sao ông nhận con về? Hồi đó con bẩn, con gầy, con không có gì."

"Vì con giống ông. Ông cũng từng không có gì. Nhưng có người cho ông tô chè — và ông hiểu: được cho thì phải cho lại."

Bảo ôm ông, khóc. Ông xoa đầu Bảo — tay nhăn nheo, run run, nhưng ấm.

Ngoài cửa, Sài Gòn đêm khuya — xe cộ thưa dần, đèn đường vàng nhạt. Trong phòng trọ nhỏ, hai ông cháu ngồi ăn chè — tô chè ấm nhất Sài Gòn.

Không phải vì đường ngọt. Mà vì tình thật."""),
]

# ═══════════════════════════════════════════════════════════════════════════════
# STORY 29: CUNG ĐẤU — NỮ GIÁM ĐỐC MARKETING BỊ ĐẠO Ý TƯỞNG — 11 CHƯƠNG
# ═══════════════════════════════════════════════════════════════════════════════

S29_TITLE = "BỊ SẾP ĐẠO TOÀN BỘ CHIẾN DỊCH MARKETING, CÔ NHÂN VIÊN CŨ TẠO AGENCY RIÊNG VÀ CƯỚP MỌI KHÁCH HÀNG LỚN"
S29_AUTHOR = "Lê Thanh Hà"
S29_COVER = "base_cover_32.png"
S29_INTRO = """<p><strong>"Tôi dành ba tháng xây campaign 'Vị Quê Hương' cho hãng nước mắm Phú Quốc. Sếp tôi đứng tên, nhận giải thưởng, rồi sa thải tôi vì 'không phù hợp văn hóa công ty.' Campaign đó thắng Golden Dragon Award — dưới tên sếp."</strong></p>
<p>Lê Thanh Hà, 29 tuổi, Creative Director bị đánh cắp ý tưởng và đuổi việc, quyết định mở agency riêng và chứng minh: ý tưởng thuộc về người tạo ra nó.</p>"""

S29_CHAPTERS = [
("Chương 1: Campaign Bị Đánh Cắp", """Hà ngồi trước TV, xem lễ trao giải Golden Dragon Award — giải thưởng marketing danh giá nhất Việt Nam. Khi MC đọc: "Campaign xuất sắc nhất — 'Vị Quê Hương' — Agency BlueStar, Creative Director Nguyễn Hữu Phong," Hà tắt TV.

Phong — sếp cũ — đứng trên sân khấu, nhận cúp, phát biểu: "Tôi đã dồn tâm huyết vào campaign này."

Sự thật: Hà tạo mọi thứ — concept, storyboard, tagline "Mắm ngon vì nhớ nhà," casting diễn viên, chọn nhạc. Phong chỉ ký duyệt.

Ba tháng trước, khi campaign sắp ra mắt, Phong gọi Hà vào phòng: "Hà, công ty restructure. Vị trí em bị cắt." Rồi Phong đứng tên toàn bộ campaign.

"Đó là ý tưởng của tôi," Hà nói.

"Ý tưởng tạo ra trong công ty thuộc về công ty," luật sư BlueStar đáp."""),

("Chương 2: Không Ai Tin", """Hà kể cho bạn bè, đồng nghiệp cũ. Phản ứng: "Phong là sếp, Phong có quyền. Em chỉ là nhân viên."

"Nhưng em tạo ra nó!"

"Trong marketing, ai đứng tên người đó sở hữu. Thực tế thôi, Hà."

Hà nhận ra: ngành marketing không bảo vệ người sáng tạo — chỉ bảo vệ người có chức. Cô cần thay đổi luật chơi."""),

("Chương 3: Lập Agency — Thanh Hà Creative", """Hà dùng tiền tiết kiệm — một trăm triệu — thuê phòng nhỏ ở quận 1, lập Thanh Hà Creative. Ba người: Hà (creative), Minh (account, bạn cũ), Lan (designer, bạn đại học).

"Chúng ta không có danh tiếng, không có khách hàng, không có giải thưởng," Minh nói.

"Chúng ta có thứ BlueStar không có: ý tưởng thuộc về người tạo ra nó. Và chúng ta chứng minh bằng campaign tiếp theo." """),

("Chương 4: Campaign Đầu Tiên — Viral", """Khách hàng đầu tiên: một tiệm bún bò nhỏ ở Huế muốn bán online — budget năm triệu. Không ai trong ngành nhận budget nhỏ thế.

Hà nhận. Cô tạo campaign "Tô Bún Của Mạ" — video ngắn quay bằng iPhone: bà chủ tiệm sáu mươi tuổi nấu bún bò, kể chuyện mạ dạy nấu. Chân thực, không diễn, không diễn viên.

Video đạt năm triệu view. Tiệm bún bò sold out hai tuần liên tiếp. Báo chí viết: "Agency vô danh tạo campaign viral với budget năm triệu."

Thanh Hà Creative bắt đầu có tên."""),

("Chương 5: Phong Phản Đòn", """Phong thấy Hà nổi — lo lắng. Anh ta dùng quan hệ trong ngành: "Thanh Hà Creative là agency nhỏ, non kinh nghiệm. Đừng tin."

Phong còn liên hệ khách hàng tiềm năng của Hà — chặn trước: "Tôi sẽ giảm giá nếu anh ký với BlueStar thay vì Thanh Hà."

Hà biết. Nhưng cô không đáp — cô để portfolio nói."""),

("Chương 6: Cướp Khách Hàng Lớn", """Sáu tháng sau: Thanh Hà Creative pitch thắng campaign cho Vinamilk — budget hai tỷ. Concept: "Sữa Việt, Vị Mẹ" — tương tự triết lý "Vị Quê Hương" nhưng nâng cấp.

Vinamilk chọn Hà vì: "Campaign của cô chân thực. BlueStar bóng bẩy nhưng thiếu hồn."

Phong mất khách hàng lớn nhất. BlueStar doanh thu giảm 30%.

Hai tháng sau: ba khách hàng lớn nữa chuyển từ BlueStar sang Thanh Hà — vì nhân viên cũ của Phong rỉ tai: "Campaign hay nhất BlueStar đều do Hà làm." """),

("Chương 7: Phong Xin Hợp Tác", """Phong gọi Hà: "Hà à, anh sai. Anh muốn hợp tác — sáp nhập BlueStar và Thanh Hà."

"Anh đánh cắp campaign của em, đuổi em, rồi giờ muốn hợp tác?"

"Anh biết anh sai. Nhưng anh giỏi quản lý, em giỏi sáng tạo."

"Anh ơi, anh giỏi quản lý người khác. Em giỏi quản lý ý tưởng. Khác nhau."

Hà từ chối."""),

("Chương 8: Golden Dragon Award — Lần Này Đúng Tên", """Thanh Hà Creative thắng Golden Dragon Award với campaign "Sữa Việt, Vị Mẹ." Hà đứng trên sân khấu — cùng sân khấu mà Phong từng đứng với ý tưởng của cô.

"Campaign này thuộc về team Thanh Hà Creative. Mỗi ý tưởng đều có tên người tạo ra — và tên đó xứng đáng được gọi."

Khán phòng vỗ tay. Phong ngồi dưới — im lặng."""),

("Chương 9: Mẹ Và Cuốn Sổ Ý Tưởng", """Hà sáng tạo vì mẹ. Bà Lê Thị Hồng, thợ may gia công — may áo theo mẫu người khác, không bao giờ được đứng tên.

"Mẹ ơi, sao mẹ không thiết kế áo riêng?"

"Vì mẹ may gia công. Thiết kế thuộc về chủ xưởng. Mẹ chỉ là đôi tay."

Hà từ chối trở thành "đôi tay" không tên. Cuốn sổ ý tưởng — cô viết mỗi ngày — giờ có tên cô trên bìa."""),

("Chương 10: Quy Tắc Thanh Hà", """Agency Thanh Hà Creative — giờ ba mươi nhân viên — có quy tắc: mọi campaign phải ghi tên người sáng tạo. Từ creative director đến intern — ai nghĩ ra, tên người đó xuất hiện.

"Trong ngành này, ý tưởng là tài sản quý nhất. Và tài sản phải có chủ."

Nhiều agency khác học theo — phong trào "Credit the Creator" trong ngành marketing Việt Nam."""),

("Chương 11: Sáng Thứ Hai Ở Agency", """Sáng thứ Hai, Hà vào office — quận 1, tầng mười hai, view sông Sài Gòn. Ba mươi người ngồi quanh bàn họp, brainstorm campaign mới.

"Okay team, campaign mới cho thương hiệu cà phê. Ai có idea?"

Intern Linh — hai mươi hai tuổi, mới vào — giơ tay run run: "Em có idea... nhưng nó hơi khác..."

"Khác là tốt. Nói đi, Linh."

Linh trình bày. Idea hay. Cả phòng vỗ tay.

Hà ghi lên bảng: "Campaign Cà Phê — Concept: Linh Nguyễn."

Linh nhìn tên mình trên bảng, mắt sáng.

Hà mỉm cười — vì cô nhớ: ngày xưa, không ai viết tên cô lên bảng."""),
]

# ═══════════════════════════════════════════════════════════════════════════════
# STORY 30: SẢNG VĂN — THỢ XÂY BỊ KHINH — 10 CHƯƠNG
# ═══════════════════════════════════════════════════════════════════════════════

S30_TITLE = "BỊ KHINH LÀ THỢ XÂY MẶT ĐEN, TÔI XÂY ĐƯỢC NGÔI NHÀ ĐẸP NHẤT TỈNH VÀ THÀNH KIẾN TRÚC SƯ TỰ HỌC"
S30_AUTHOR = "Nguyễn Đình Tài"
S30_COVER = "base_cover_33.png"
S30_INTRO = """<p><strong>"Chủ thầu bảo tôi: 'Mày là thợ xây, biết gì mà đòi thiết kế? Xây cho đúng bản vẽ là được rồi.' Tôi xây đúng bản vẽ — nhưng tôi biết: bản vẽ đó sai."</strong></p>
<p>Nguyễn Đình Tài, thợ xây 30 tuổi từ Nghệ An, bị chủ thầu khinh rẻ vì góp ý thiết kế. Anh tự học kiến trúc qua YouTube, sách, và thực hành — rồi xây ngôi nhà đẹp nhất tỉnh.</p>"""

S30_CHAPTERS = [
("Chương 1: Thợ Xây Mặt Đen", """Nguyễn Đình Tài, ba mươi tuổi, thợ xây từ năm mười sáu — mười bốn năm trộn vữa, đổ bê tông, xây gạch dưới nắng. Da đen cháy, tay chai sạn, lưng đau từ năm hai mươi lăm.

Công trình hiện tại: biệt thự cho đại gia Nguyễn Văn Hoàng ở TP Vinh. Chủ thầu Trần Đức Mạnh — bụng phệ, lái Fortuner — chỉ đạo từ xa.

Tài nhìn bản vẽ: cầu thang thiết kế sai — bậc quá hẹp, góc cua quá gấp, người già sẽ té. Tài nói với Mạnh: "Anh ơi, cầu thang này nguy hiểm. Em đề nghị sửa."

"Mày là thợ xây, biết gì mà đòi sửa? Xây đúng bản vẽ!"

Tài xây đúng bản vẽ. Ba tháng sau: mẹ ông Hoàng trượt cầu thang, gãy tay. Mạnh đổ tội cho thợ xây — Tài bị đuổi."""),

("Chương 2: Tự Học Kiến Trúc — YouTube Và Sách", """Tài bị đuổi nhưng không tìm chủ thầu mới. Anh dùng tiền tiết kiệm — mười triệu — mua laptop secondhand, kết nối wifi quán cà phê, bắt đầu tự học kiến trúc.

YouTube: MIT OpenCourseWare về kiến trúc, kênh ArchDaily, hướng dẫn AutoCAD. Sách: "Kiến trúc dành cho người không chuyên" mượn thư viện tỉnh.

Mỗi đêm, sau ca xây (vẫn đi làm phụ hồ để sống), Tài học đến hai giờ sáng. Vẽ bản vẽ trên giấy A4, rồi trên AutoCAD crack.

"Em không có bằng kiến trúc sư. Nhưng em có mười bốn năm xây nhà — em biết cái nào xây được, cái nào không."

Hai năm tự học: Tài vẽ được bản vẽ kỹ thuật, hiểu kết cấu, biết tính tải trọng, và có gu thẩm mỹ — từ nhà truyền thống Nghệ An đến minimalist Nhật Bản."""),

("Chương 3: Ngôi Nhà Đầu Tiên — Nhà Cho Mẹ", """Tài xây ngôi nhà đầu tiên — cho mẹ. Bà Nguyễn Thị Lành, bảy mươi tuổi, sống trong nhà cấp bốn dột nát ở quê Quỳnh Lưu, Nghệ An.

"Mẹ ơi, con xây nhà mới cho mẹ."

"Con ơi, mẹ ở nhà cũ quen rồi."

"Mẹ ở nhà cũ vì mẹ không có nhà mới. Con xây cho mẹ — con tự thiết kế, tự xây."

Tài thiết kế: nhà một tầng, ba phòng, sân trước trồng rau, mái ngói Nghệ An truyền thống nhưng kết cấu hiện đại. Cầu thang — nếu cần nâng tầng sau — bậc rộng, tay vịn chắc, góc cua thoải.

Tài tự xây — một mình, ba tháng. Hàng xóm đến phụ: "Tài ơi, nhà mày đẹp quá!"

Mẹ Tài bước vào nhà mới, sờ tường, sờ cửa: "Con xây đẹp quá. Mẹ không nghĩ thợ xây xây được nhà đẹp thế này." """),

("Chương 4: Tin Đồn — Thợ Xây Thiết Kế Nhà Đẹp", """Hàng xóm kể: "Thằng Tài thợ xây mà tự thiết kế nhà đẹp hơn kiến trúc sư!" Tin đồn lan khắp huyện. Người ta đến xem nhà mẹ Tài — và đặt hàng.

Khách đầu tiên: ông Phan Văn Thọ, nông dân, muốn xây nhà cho con trai cưới vợ — budget ba trăm triệu.

"Tài ơi, tao muốn nhà vừa đẹp vừa rẻ. KTS ngoài thành phố đòi phí thiết kế năm mươi triệu — tao không có."

Tài thiết kế miễn phí, tự xây, chỉ lấy tiền vật liệu và công thợ. Nhà ông Thọ: hai tầng, kiểu Nghệ An cách tân, ban công rộng, bếp mở — ba trăm triệu bao gồm tất cả.

"Đẹp hơn nhà năm trăm triệu ngoài phố!" ông Thọ khen."""),

("Chương 5: Mạnh Quay Lại — Đòi Hợp Tác", """Chủ thầu Mạnh nghe tiếng Tài — đến gặp: "Tài à, quay lại làm với anh. Anh cho mày làm 'tư vấn thiết kế' — tăng lương gấp đôi."

"Anh ơi, anh đuổi em vì em góp ý cầu thang. Giờ anh muốn em thiết kế?"

"Anh biết anh sai lần đó. Nhưng kinh doanh là kinh doanh."

"Kinh doanh của anh để mẹ ông Hoàng gãy tay. Em không làm với người coi sinh mạng là 'kinh doanh.' "

Tài từ chối."""),

("Chương 6: Ngôi Nhà Đẹp Nhất Tỉnh", """Tài nhận thiết kế và xây nhà cho anh Lê Hồng Phong — Việt kiều Mỹ về quê xây biệt thự — budget hai tỷ.

Tài thiết kế: biệt thự hai tầng, phong cách Indochine pha Nghệ An — cột gỗ lim, mái ngói đỏ, sân vườn cây quê, bên trong hiện đại. Cầu thang rộng, tay vịn gỗ, mỗi bậc đúng chuẩn.

Sáu tháng xây. Khi hoàn thành — cả tỉnh đến xem: "Nhà đẹp nhất Nghệ An!"

Báo Nghệ An đăng bài: "Thợ xây tự học trở thành kiến trúc sư — ngôi nhà Indochine đẹp nhất tỉnh."

Anh Phong nói: "Tài ơi, nhà anh ở bên Mỹ không đẹp bằng. Anh muốn về ở luôn." """),

("Chương 7: Mẹ Và Viên Gạch Đầu Tiên", """Tài xây nhà vì mẹ. Bà Lành, nông dân Quỳnh Lưu — bốn đứa con, chồng mất sớm, nuôi con bằng ruộng lúa.

"Mẹ ơi, sao mẹ không xây nhà mới?"

"Mẹ không có tiền. Và mẹ không biết xây."

"Con biết xây. Con sẽ xây cho mẹ."

Mẹ dạy Tài: kiên nhẫn. "Xây nhà giống cấy lúa — phải đợi, phải chăm, không được vội."

Viên gạch đầu tiên Tài đặt — năm mười sáu tuổi, phụ hồ — giờ nằm trong tường nhà mẹ. Tài giữ lại viên gạch đó — viên gạch bắt đầu mọi thứ."""),

("Chương 8: Công Ty Kiến Trúc Đình Tài", """Tài lập Công ty Kiến trúc Đình Tài — chuyên thiết kế và xây nhà cho người thu nhập trung bình ở nông thôn Nghệ An. Giá thiết kế: miễn phí nếu budget dưới năm trăm triệu.

"Tôi không có bằng KTS. Nhưng tôi có mười bốn năm xây nhà và hai năm tự học. Tôi biết cái gì xây được trong ngân sách nông dân."

Năm đầu: hai mươi nhà. Năm thứ hai: bốn mươi. Mỗi ngôi nhà — Tài thiết kế riêng, phù hợp gia đình, phù hợp đất, phù hợp túi tiền.

Đồng nghiệp KTS có bằng nói: "Thằng Tài không bằng cấp mà thiết kế."

Khách hàng nói: "Nhà thằng Tài đẹp hơn nhà KTS. Vì Tài biết xây — KTS chỉ biết vẽ." """),

("Chương 9: Giải Thưởng Kiến Trúc Nông Thôn", """Tài được mời trình bày tại Hội nghị Kiến trúc Nông thôn Việt Nam — anh là diễn giả duy nhất không có bằng KTS.

"Tôi là thợ xây. Tôi tự học kiến trúc. Tôi thiết kế nhà cho nông dân — những người mà KTS thành phố không phục vụ vì 'budget quá nhỏ.' "

Khán phòng im lặng. Rồi vỗ tay.

Tài nhận giải "Kiến trúc sư cộng đồng" — giải thưởng đặc biệt dành cho người đóng góp kiến trúc nông thôn."""),

("Chương 10: Bình Minh Trên Công Trường", """Năm giờ sáng, Tài đứng trên công trường — ngôi nhà thứ sáu mươi. Tay cầm bản vẽ, mắt nhìn khung thép, miệng hướng dẫn thợ.

Da vẫn đen. Tay vẫn chai. Lưng vẫn đau. Nhưng mắt Tài sáng — sáng vì anh đang xây thứ mà mười bốn năm trước anh bị cấm: ý tưởng của mình.

"Tài ơi, sao mày không thuê người xây, mày chỉ thiết kế thôi?"

"Vì tôi là thợ xây. Thiết kế mà không xây — như vẽ mà không tô. Tôi muốn tô."

Mặt trời mọc trên cánh đồng Nghệ An — ánh vàng rải trên những ngôi nhà mới, mái ngói đỏ, sân vườn xanh.

Nguyễn Đình Tài — thợ xây mặt đen, kiến trúc sư tự học — cầm bay, trộn vữa, và tiếp tục xây."""),
]

# ═══════════════════════════════════════════════════════════════════════════════
# ASSEMBLY & PUBLISHING
# ═══════════════════════════════════════════════════════════════════════════════

ALL_STORIES = [
    {"title": S26_TITLE, "author": S26_AUTHOR, "cover": S26_COVER, "intro": S26_INTRO, "chapters": S26_CHAPTERS, "genre": "Sảng Văn"},
    {"title": S27_TITLE, "author": S27_AUTHOR, "cover": S27_COVER, "intro": S27_INTRO, "chapters": S27_CHAPTERS, "genre": "Ngược"},
    {"title": S28_TITLE, "author": S28_AUTHOR, "cover": S28_COVER, "intro": S28_INTRO, "chapters": S28_CHAPTERS, "genre": "Ngọt"},
    {"title": S29_TITLE, "author": S29_AUTHOR, "cover": S29_COVER, "intro": S29_INTRO, "chapters": S29_CHAPTERS, "genre": "Cung Đấu"},
    {"title": S30_TITLE, "author": S30_AUTHOR, "cover": S30_COVER, "intro": S30_INTRO, "chapters": S30_CHAPTERS, "genre": "Sảng Văn"},
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
    log("🚀 MIX BATCH 6 — 5 STORIES (🎭 Mix Tổng Hợp — FINAL BATCH)")
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
            genre_label = {"Sảng Văn": "Sảng văn", "Ngược": "Ngược văn", "Ngọt": "Ngọt văn", "Cung Đấu": "Cung đấu văn"}
            subtitle = f"{genre_label.get(n['genre'], n['genre'])} của {n['author']}"
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

    log(f"\n🏁 MIX BATCH 6 (FINAL) COMPLETE: {len(results)}/5 published")
    log("🎊 ALL 30 STORIES PUBLISHED!")
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
