#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
write_batch_sangvan_05.py — Batch 5 FINAL: 4 Truyện Sảng Văn (Stories 17-20)
=============================================================================
Story 17: Luật sư bào chữa oan sai (cover 51)
Story 18: Dược sĩ R&D thuốc (cover 52)
Story 19: Giám khảo cà phê (cover 53)
Story 20: Phi công thử nghiệm (cover 54)
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
    abbrevs = ["TS.", "BS.", "PGS.", "GS.", "CEO.", "CFO.", "CTO.", "Dr.", "Mr.", "Mrs.", "Ph.D.", "HĐQT.", "IPO.", "PCCC.", "KTS."]
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
# STORY 17: LUẬT SƯ BÀO CHỮA OAN SAI
# ═══════════════════════════════════════════════════════════════════════════════

S17_TITLE = "BỊ TƯỚC THẺ LUẬT SƯ VÌ BÀO CHỮA CHO NÔNG DÂN, TÔI LẬP HÃNG LUẬT CỨU MƯỜI NGHÌN NGƯỜI OAN SAI"
S17_AUTHOR = "Trịnh Hoàng Long"
S17_COVER = "base_cover_51.png"
S17_INTRO = """<p><strong>"Mười năm tôi là luật sư giỏi nhất hãng luật lớn nhất Việt Nam, chuyên bào chữa cho tập đoàn và đại gia. Đổi lại, khi tôi nhận bào chữa miễn phí cho ba mươi nông dân bị cướp đất, họ tước thẻ luật sư của tôi."</strong></p>
<p>Trịnh Hoàng Long, luật sư tranh tụng xuất sắc nhất hãng luật Việt Long & Partners, bị đuổi và bị vận động tước thẻ khi anh dám đứng về phía nông dân chống lại chính client lớn nhất của hãng — Tập đoàn BĐS Hoàng Kim.</p>
<p>Mất thẻ, mất sự nghiệp, Long thành lập "Hãng Luật Nhân Dân" — chuyên bào chữa miễn phí cho người nghèo bị oan sai, và trở thành luật sư được kính trọng nhất Việt Nam.</p>"""

S17_CHAPTERS = [
("Chương 1: Vụ Án Cướp Đất", """Tòa án Nhân dân tỉnh Long An, phòng xử lớn, chín giờ sáng. Ba mươi nông dân xã Bình Hòa ngồi chen chúc trên hàng ghế bị đơn, mắt sợ hãi, tay nắm chặt nhau. Đối diện: đội luật sư năm người của Tập đoàn BĐS Hoàng Kim, vest đen, cặp da Montblanc.

Trịnh Hoàng Long ngồi ở hàng ghế luật sư bào chữa, phía bị đơn. Một mình, một cặp hồ sơ, một bộ vest nhăn nhúm.

Vụ án: Hoàng Kim kiện ba mươi nông dân "lấn chiếm đất dự án." Nhưng sự thật: đất đó là ruộng tổ tiên nông dân canh tác ba đời, bị thu hồi với giá đền bù hai mươi nghìn đồng/mét vuông — một phần trăm giá thị trường — để Hoàng Kim xây khu đô thị cao cấp.

"Thưa Hội đồng xét xử, ba mươi hộ gia đình này canh tác trên mảnh đất này từ năm 1975," Long đứng dậy, giọng rõ ràng. "Quyết định thu hồi đất vi phạm Điều 62 Luật Đất đai — chưa có sự đồng thuận của người dân, chưa có phương án tái định cư, và giá đền bù thấp hơn khung giá đất do UBND tỉnh quy định."

Luật sư trưởng của Hoàng Kim — Nguyễn Hữu Phong, đối tác cũ của Long tại Việt Long & Partners — nhếch miệng: "Luật sư Long, anh quên rằng mình từng ngồi bên này bàn?"

Long nhìn Phong: "Tôi nhớ. Tôi từng ngồi bên kia, bào chữa cho kẻ cướp đất. Giờ tôi ngồi bên này, bào chữa cho người bị cướp. Đó gọi là tiến bộ."

Tòa xử sơ thẩm: Hoàng Kim thắng — như mọi khi. Nông dân khóc. Long siết chặt tay bà Nguyễn Thị Sáu, bảy mươi tuổi, nông dân già nhất: "Bà yên tâm. Chúng ta kháng cáo."

Ngày hôm sau, Long bị gọi lên phòng Senior Partner tại Việt Long & Partners.

"Long, cậu bào chữa cho nông dân CHỐNG LẠI client lớn nhất của hãng? Hoàng Kim đóng phí pháp lý ba mươi tỷ đồng mỗi năm cho chúng ta!"

"Tôi nhận pro bono ngoài giờ hành chính, không dùng tài nguyên hãng."

"KHÔNG QUAN TRỌNG! Cậu đang đối đầu client của chúng ta trên tòa! Đó là xung đột lợi ích! Cậu bị sa thải."

Long nộp đơn từ chức, không để họ sa thải. Nhưng chưa hết: Hoàng Kim vận động Đoàn Luật sư tỉnh tước thẻ hành nghề, lý do "vi phạm đạo đức nghề nghiệp — xung đột lợi ích."

Long mất thẻ luật sư. Không được hành nghề. Không được ra tòa."""),

("Chương 2: Hãng Luật Nhân Dân", """Mất thẻ, Long không thể ra tòa với tư cách luật sư. Nhưng anh vẫn có thể tư vấn pháp lý.

Anh mở "Trung tâm Tư vấn Pháp lý Nhân Dân" tại nhà mẹ ở quận Gò Vấp — phòng khách mười lăm mét vuông, bàn gỗ cũ, hai ghế nhựa. Miễn phí cho mọi người.

Ba mươi nông dân Bình Hòa vẫn đến mỗi tuần, mang theo hồ sơ đất đai. Long hướng dẫn họ tự viết đơn kháng cáo, tự thu thập bằng chứng, tự trình bày tại tòa phúc thẩm — với Long ngồi hàng ghế khán giả, ghi chú và gật đầu.

Sáu tháng sau, Long kháng cáo quyết định tước thẻ lên Liên đoàn Luật sư Việt Nam. Anh chứng minh: anh nhận vụ nông dân sau giờ làm việc, không dùng tài nguyên hãng, và xung đột lợi ích thuộc về hãng chứ không thuộc về anh.

Liên đoàn phục hồi thẻ luật sư. Long quay lại tòa — đúng ngày phúc thẩm vụ Bình Hòa.

Tòa phúc thẩm: Long trình bày bằng chứng mới — biên bản họp UBND tỉnh ghi rõ giá đền bù bị ép thấp theo "đề nghị" của Hoàng Kim, kèm email giữa CEO Hoàng Kim và Phó Chủ tịch tỉnh.

Tòa phúc thẩm tuyên: hủy quyết định thu hồi đất. Nông dân giữ được ruộng. Bà Sáu ôm Long khóc nức nở: "Luật sư ơi, gia đình tôi giữ được đất rồi!" """),

("Chương 3: Mười Nghìn Vụ Án Pro Bono", """Sau chiến thắng Bình Hòa, Long chính thức thành lập "Hãng Luật Nhân Dân" — chuyên nhận vụ án miễn phí cho người nghèo, nông dân, công nhân bị bóc lột, và người bị oan sai.

Mô hình: năm mươi phần trăm vụ án thương mại trả phí cao + năm mươi phần trăm vụ án pro bono. Lợi nhuận từ vụ trả phí tài trợ hoàn toàn cho vụ miễn phí.

Năm năm, Hãng Luật Nhân Dân nhận mười nghìn vụ án pro bono — từ tranh chấp đất đai, nợ lương công nhân, đến bào chữa oan sai hình sự. Tỷ lệ thắng: bảy mươi tám phần trăm.

Đội ngũ: bốn mươi luật sư, phần lớn là sinh viên luật vừa tốt nghiệp, muốn làm luật sư vì công lý, không vì tiền."""),

("Chương 4: Vụ Án Oan Sai Chấn Động", """Long nhận bào chữa cho Đặng Văn Tân, nông dân Đắk Lắk, bị kết án mười năm tù về tội "giết người" — vụ án mà mọi bằng chứng đều mâu thuẫn.

Long mất hai năm điều tra lại: tìm nhân chứng mới, phân tích lại chứng cứ pháp y, thuê chuyên gia ADN quốc tế. Kết quả: ADN trên hung khí không khớp với Tân, nhân chứng chính thừa nhận bị ép cung.

Tòa phúc thẩm tuyên Tân vô tội sau sáu năm ngồi tù oan. Tân bước ra cổng trại giam, ôm vợ con, khóc không thành tiếng.

Long đứng phía sau, mắt đỏ hoe. Sáu năm tù oan — không ai trả lại được. Nhưng ít nhất, từ hôm nay, Tân tự do.

Vụ án Đặng Văn Tân trở thành case study bào chữa oan sai nổi tiếng nhất Việt Nam."""),

("Chương 5: Chiến Thắng Hoàng Kim Lần Hai", """Ba năm sau vụ Bình Hòa, Long nhận thêm bốn vụ kiện khác chống Hoàng Kim — tổng cộng năm trăm hộ dân bị cưỡng chế đất ở ba tỉnh miền Tây.

Long dùng chiến thuật class action — gộp năm trăm hộ thành một vụ kiện tập thể, trình bày trước Tòa án Nhân dân Tối cao.

Tòa tối cao phán: Hoàng Kim vi phạm Luật Đất đai ở quy mô hệ thống. CEO Hoàng Kim bị khởi tố. Năm trăm hộ dân được bồi thường tổng cộng hai trăm tỷ đồng — giá đền bù đúng thị trường.

Long không lấy một đồng phí từ nông dân. Anh nói: "Công lý không có giá. Nhưng bất công thì có — và kẻ gây bất công phải trả." """),

("Chương 6: Hãng Luật Lớn Nhất Miền Nam", """Hãng Luật Nhân Dân trở thành hãng luật uy tín nhất miền Nam — không phải vì quy mô mà vì danh tiếng. Các tập đoàn lớn cũng thuê Long vì biết: luật sư dám đối đầu cả hệ thống để bảo vệ nông dân thì chắc chắn sẽ bảo vệ họ bằng mọi giá.

Doanh thu: một trăm tỷ đồng mỗi năm. Năm mươi phần trăm trích cho quỹ trợ giúp pháp lý miễn phí. Tám mươi luật sư, sáu văn phòng."""),

("Chương 7: Mẹ Và Bản Án Cũ", """Long theo nghề luật vì mẹ. Bà Trịnh Thị Hồng, bán rau ở chợ Bà Chiểu, bị kiện "lấn chiếm vỉa hè" và phạt năm triệu đồng — gần hai tháng lương. Bà không biết luật, không biết kiện, chỉ biết khóc.

Long lúc đó mười bốn tuổi, ngồi cạnh mẹ ở tòa, nhìn thẩm phán gõ búa. Anh thề: "Con sẽ học luật, để không ai bắt nạt mẹ nữa."

Mẹ Long giờ bảy mươi tuổi, vẫn bán rau ở chợ Bà Chiểu — nhưng không ai dám phạt. Vì mọi người biết: con trai bà là luật sư Long, người mà cả tập đoàn tỷ đô cũng phải sợ."""),

("Chương 8: Hoàng Kim Sụp Đổ", """CEO Hoàng Kim bị tuyên mười lăm năm tù về tội cưỡng chế đất đai trái phép, hối lộ, và lừa đảo. Tập đoàn phá sản, tổng nợ ba nghìn tỷ.

Phong — luật sư cũ đối đầu Long ở Bình Hòa — bị cấm hành nghề vì giúp Hoàng Kim hối lộ quan chức. Từ partner hãng luật lớn nhất, giờ không được bước chân vào tòa.

Long nhận được thư xin lỗi từ Senior Partner cũ tại Việt Long & Partners: "Long, ngày xưa chúng tôi sa thải anh là sai lầm lớn nhất trong lịch sử hãng." """),

("Chương 9: Giải Thưởng Nhân Quyền Quốc Tế", """Long nhận giải "International Bar Association Human Rights Award" — giải thưởng nhân quyền uy tín nhất giới luật sư toàn cầu, tại London.

"Tôi bị tước thẻ luật sư vì bào chữa cho nông dân. Nếu luật sư không bảo vệ được người yếu, thì luật sư bảo vệ ai?" Long hỏi trước một nghìn luật sư quốc tế.

Bài phát biểu nhận standing ovation. Nhiều luật sư trẻ châu Á thành lập các hãng luật pro bono theo mô hình "Nhân Dân" sau khi nghe Long."""),

("Chương 10: Quay Về Bình Hòa", """Long lái xe về xã Bình Hòa, Long An — nơi bắt đầu tất cả. Cánh đồng lúa vẫn xanh mướt, nông dân vẫn cày ruộng, trâu vẫn đi trước, người đi sau.

Bà Sáu, giờ bảy mươi sáu tuổi, mời Long vào nhà uống trà. Trên tường nhà bà, treo ảnh Long chụp với ba mươi nông dân ngày thắng kiện — tấm ảnh duy nhất bà đóng khung.

"Luật sư ơi, nhờ anh mà đất nhà tôi giữ được. Con cháu tôi có chỗ ở. Trâu tôi có chỗ cày."

Long uống trà, nhìn cánh đồng ngoài cửa sổ. Đất vẫn ở đây, nông dân vẫn ở đây, và công lý — dù chậm — cuối cùng cũng đến.

Anh rút điện thoại, check lịch: chiều nay có hai vụ mới. Một vụ tranh chấp đất ở Bến Tre, một vụ nợ lương công nhân ở Bình Dương.

Long cười, đứng dậy: "Bà Sáu, con đi. Còn người cần con bào chữa."

Anh lái xe ra khỏi Bình Hòa, con đường quê hai bên là lúa xanh. Trong gương chiếu hậu, bà Sáu vẫy tay, nhỏ dần, nhỏ dần — nhưng cánh đồng vẫn mãi xanh."""),
]

# ═══════════════════════════════════════════════════════════════════════════════
# STORY 18: DƯỢC SĨ R&D THUỐC
# ═══════════════════════════════════════════════════════════════════════════════

S18_TITLE = "BỊ CƯỚP CÔNG THỨC THUỐC ĐẶC TRỊ, TÔI TỰ SẢN XUẤT THUỐC GIÁ RẺ CỨU HÀNG TRIỆU BỆNH NHÂN NGHÈO"
S18_AUTHOR = "Phạm Ngọc Hà"
S18_COVER = "base_cover_52.png"
S18_INTRO = """<p><strong>"Sáu năm tôi nghiên cứu, bào chế thành công thuốc điều trị viêm gan B giá rẻ cho người Việt Nam. Đổi lại, tập đoàn dược phẩm cướp công thức, đăng ký bằng sáng chế, và bán thuốc với giá gấp mười lần."</strong></p>
<p>Phạm Ngọc Hà, Dược sĩ R&D tại Tập đoàn Dược Minh Phát, bị Tổng Giám đốc Lê Quang Vinh và Giám đốc R&D Cao Minh Tuấn cướp công thức thuốc viêm gan B generic khi cô phát triển thành công phiên bản giá rẻ cho người nghèo.</p>
<p>Mất công thức, mất nghề, Hà thành lập hãng dược phẩm generic đầu tiên do người Việt sáng lập, sản xuất thuốc đặc trị giá rẻ cứu sống hàng triệu bệnh nhân nghèo trên khắp Đông Nam Á.</p>"""

S18_CHAPTERS = [
("Chương 1: Công Thức Bị Đánh Cắp", """Phòng R&D tầng sáu, Tập đoàn Dược Minh Phát, KCN Nhơn Trạch, mười giờ đêm. Phạm Ngọc Hà đang phân tích kết quả thử nghiệm lâm sàng giai đoạn 3 cho VietHep-B — thuốc generic điều trị viêm gan B mà cô phát triển suốt sáu năm.

VietHep-B hoạt động dựa trên cơ chế ức chế reverse transcriptase, giống tenofovir nhưng cải tiến: ít tác dụng phụ trên thận hơn ba mươi phần trăm, và giá thành sản xuất chỉ bằng một phần mười — đủ rẻ cho bệnh nhân nghèo Việt Nam.

Việt Nam có chín triệu người nhiễm viêm gan B. Thuốc nhập khẩu giá hai triệu đồng mỗi tháng — nông dân thu nhập ba triệu không bao giờ mua nổi. VietHep-B, nếu sản xuất, giá chỉ hai trăm nghìn.

"Kết quả tuyệt vời," Hà thì thầm khi nhìn dữ liệu. Tỷ lệ ức chế virus đạt chín mươi sáu phần trăm — ngang bằng tenofovir gốc, nhưng rẻ hơn mười lần.

Sáng hôm sau, cô trình bày kết quả lên ban lãnh đạo. TGĐ Lê Quang Vinh, năm mươi lăm tuổi, nghe xong gật gù: "Giỏi lắm, Hà. Để anh xem xét kế hoạch sản xuất."

Hai tuần im lặng. Rồi Hà phát hiện: Minh Phát đã nộp hồ sơ đăng ký bằng sáng chế cho VietHep-B — dưới tên Cao Minh Tuấn (Giám đốc R&D, người chưa bao giờ bước vào lab) và Lê Quang Vinh. Tên Hà bị xóa hoàn toàn.

Và giá bán dự kiến: một triệu tám trăm nghìn đồng — gần bằng thuốc nhập khẩu.

"Anh Vinh, em phát triển thuốc này để bán giá rẻ cho bệnh nhân nghèo! Anh bán giá đó thì khác gì thuốc nhập?"

"Hà, thị trường quyết định giá, không phải lý tưởng. Và bằng sáng chế thuộc về công ty, không thuộc về cá nhân."

"Nhưng tên trên bằng sáng chế phải là tên người phát minh! Anh và anh Tuấn chưa bao giờ—"

"ĐÂY LÀ QUYẾT ĐỊNH CỦA HĐQT!" Vinh đứng dậy. "Nếu cô không đồng ý, cô biết cửa ở đâu."

Hà bị sa thải ngay trong ngày. An ninh thu hồi laptop, USB, và toàn bộ tài liệu R&D. Cô bước ra cổng KCN Nhơn Trạch với chiếc túi xách — bên trong chỉ có cuốn sổ ghi chép cá nhân, nơi lưu toàn bộ quy trình tổng hợp thuốc bằng... ký hiệu riêng mà chỉ Hà đọc được."""),

("Chương 2: Hãng Dược Trong Phòng Trọ", """Hà về nhà mẹ ở Biên Hòa, biến phòng ngủ cũ thành "lab." Không phải lab thật — chỉ là bàn gỗ, vài bình thủy tinh, và máy tính.

Cô dành ba tháng viết lại toàn bộ quy trình tổng hợp VietHep-B phiên bản 2.0 — cải tiến hơn bản gốc, dùng nguyên liệu rẻ hơn, quy trình đơn giản hơn. Bằng sáng chế cũ thuộc Minh Phát? Không quan trọng — v2.0 có cấu trúc phân tử khác, quy trình khác, patent-free.

Cô gặp Trần Đức Minh, ba mươi lăm tuổi, dược sĩ lâm sàng tại BV Chợ Rẫy, người chia sẻ giấc mơ "thuốc giá rẻ cho người nghèo."

Hai người thành lập PharmaViet — hãng dược phẩm generic, vốn ban đầu hai tỷ đồng gom từ tiết kiệm và vay mượn bạn bè. Thuê một phòng lab nhỏ tại KCN Biên Hòa, chỉ đủ cho bốn người làm việc."""),

("Chương 3: Thuốc Giá Rẻ — Thử Nghiệm Thành Công", """Sáu tháng R&D, VietHep-B v2.0 hoàn thành. Thử nghiệm tiền lâm sàng thành công. Hà nộp hồ sơ lên Cục Quản lý Dược để xin phép thử nghiệm lâm sàng.

Giai đoạn thử nghiệm lâm sàng tại BV Bệnh nhiệt đới TP.HCM: một trăm bệnh nhân viêm gan B mạn tính, chia hai nhóm — nhóm dùng VietHep-B v2.0 và nhóm dùng tenofovir gốc. Kết quả sau mười hai tháng: hiệu quả tương đương, tác dụng phụ ít hơn, giá thành sản xuất thấp hơn mười hai lần.

Giá bán dự kiến: một trăm năm mươi nghìn đồng mỗi tháng — bệnh nhân nghèo nhất cũng mua được.

Bộ Y tế cấp giấy phép lưu hành. PharmaViet bắt đầu sản xuất.

Tại Minh Phát, Vinh đọc tin, mặt sắt lại. VietHep-B v1.0 mà ông cướp — chưa kịp sản xuất vì tranh chấp bằng sáng chế nội bộ — giờ bị v2.0 vượt qua về mọi mặt."""),

("Chương 4: Phản Công Từ Minh Phát", """Vinh thuê luật sư kiện PharmaViet: "vi phạm bí mật thương mại." Nhưng Hà chứng minh: v2.0 có cấu trúc phân tử khác, quy trình tổng hợp khác, nguyên liệu khác — không vi phạm bất kỳ bằng sáng chế nào.

Tòa bác đơn kiện. Vinh chuyển sang chiêu bẩn: vận động Cục Quản lý Dược "thanh tra đặc biệt" PharmaViet. Nhưng lab PharmaViet đạt chuẩn GMP-WHO, không có vi phạm.

Hà viết trên Facebook: "Thuốc giá rẻ không phải thuốc kém chất lượng. Thuốc giá rẻ là thuốc được làm bởi người không tham lam."

Post đạt năm triệu lượt đọc. Dư luận đứng về phía Hà."""),

("Chương 5: Cứu Chín Triệu Người", """Hai năm sau khi ra thị trường, VietHep-B v2.0 trở thành thuốc viêm gan B được kê đơn nhiều nhất Việt Nam. Ba triệu bệnh nhân sử dụng — một phần ba tổng số người nhiễm.

PharmaViet mở rộng danh mục: thuốc tiểu đường generic, thuốc cao huyết áp generic, thuốc kháng sinh generic — tất cả giá bằng một phần mười thuốc nhập khẩu, chất lượng tương đương.

WHO vinh danh PharmaViet là "Best Practice in Generic Pharmaceutical Manufacturing" tại Đông Nam Á."""),

("Chương 6: Unicorn Dược Phẩm", """PharmaViet huy động vốn Series B từ quỹ y tế toàn cầu Bill & Melinda Gates Foundation — năm mươi triệu đô, mục tiêu mở rộng sản xuất thuốc generic cho toàn ASEAN và châu Phi.

Nhà máy mới tại KCN Long Thành, đạt chuẩn EU-GMP, công suất một trăm triệu viên mỗi năm. Đội ngũ năm trăm dược sĩ và kỹ sư.

Hà trở thành nữ doanh nhân dược phẩm đầu tiên của Việt Nam trên bìa Forbes Asia."""),

("Chương 7: Bà Ngoại Và Viên Thuốc Đắng", """Hà theo nghề dược vì bà ngoại. Bà Phạm Thị Xuân, nông dân Đồng Nai, bị viêm gan B mạn tính. Thuốc nhập khẩu hai triệu mỗi tháng — bà không mua nổi, chọn cách "sống chung" với bệnh.

Bà mất khi Hà mười sáu tuổi. Trước khi mất, bà nói: "Cháu ơi, thuốc đắng nhưng giàu mới mua được. Nghèo thì chịu chết thôi."

Câu nói đó theo Hà vào phòng lab, trở thành sứ mệnh suốt đời: thuốc phải đủ rẻ để người nghèo nhất cũng mua được.

PharmaViet đặt tên chương trình trợ giá thuốc cho người nghèo: "Thuốc Bà Xuân" — mỗi viên thuốc miễn phí cho bệnh nhân có thu nhập dưới ba triệu đồng."""),

("Chương 8: Minh Phát Sụp Đổ", """Minh Phát mất thị phần nghiêm trọng: VietHep-B v1.0 (giá cao) không ai mua khi có v2.0 (giá rẻ). Doanh thu sụt giảm sáu mươi phần trăm.

Vinh bị HĐQT cách chức. Tuấn bị tước giấy phép hành nghề dược. Bằng sáng chế v1.0 — thứ họ cướp từ Hà — hết hạn mà không ai sử dụng.

Minh Phát bị thâu tóm bởi một tập đoàn dược Ấn Độ với giá rẻ mạt."""),

("Chương 9: Giải Lasker Award Đề Cử", """Hà được đề cử giải Lasker Award — "American Nobel in Medicine" — cho đóng góp trong lĩnh vực thuốc generic giá rẻ tại Đông Nam Á.

"Tôi bị cướp công thức thuốc. Nhưng không ai cướp được mục đích: thuốc cho người nghèo. Và mục đích đó tạo ra thuốc tốt hơn," Hà phát biểu tại Harvard Medical School.

Bài giảng "Affordable Medicine: From Stolen Formula to Saving Millions" trở thành case study tại trường y hàng đầu thế giới."""),

("Chương 10: Quay Về Đồng Nai", """Hà về quê Đồng Nai, thăm mộ bà ngoại. Cô đặt một hộp VietHep-B v2.0 trước mộ — thuốc mà bà không bao giờ được dùng.

"Bà ơi, thuốc giờ chỉ một trăm năm mươi nghìn. Ai cũng mua được rồi. Bà không phải chịu chết nữa."

Cô ngồi bên mộ bà, nhìn cánh đồng Đồng Nai xanh mướt. Ở đâu đó trong cánh đồng, có một bà ngoại khác đang uống VietHep-B mỗi sáng — và sống, vì thuốc đủ rẻ.

Hà đứng dậy, lau mắt, bước về nhà máy PharmaViet. Trên dây chuyền sản xuất, hàng triệu viên thuốc đang được đóng hộp — mỗi viên mang theo lời hứa của cô bé mười sáu tuổi ngày bà ngoại mất: "Cháu sẽ làm thuốc cho người nghèo." """),
]

# ═══════════════════════════════════════════════════════════════════════════════
# STORY 19: GIÁM KHẢO CÀ PHÊ
# ═══════════════════════════════════════════════════════════════════════════════

S19_TITLE = "BỊ LOẠI KHỎI HỘI ĐỒNG GIÁM KHẢO CÀ PHÊ, TÔI MANG HẠT ROBUSTA VIỆT NAM LÊN ĐỈNH THẾ GIỚI"
S19_AUTHOR = "Đoàn Thế Phong"
S19_COVER = "base_cover_53.png"
S19_INTRO = """<p><strong>"Mười năm tôi là Q-grader (giám khảo cà phê quốc tế), đánh giá hàng nghìn mẫu cà phê từ khắp thế giới. Đổi lại, khi tôi khẳng định Robusta Việt Nam xứng đáng specialty grade, họ loại tôi khỏi hội đồng vì 'phá vỡ truyền thống.'"</strong></p>
<p>Đoàn Thế Phong, một trong năm Q-grader người Việt duy nhất, bị Specialty Coffee Association (SCA) và lobby Arabica loại khỏi hội đồng khi anh công khai đánh giá Robusta Việt Nam đạt specialty grade — thách thức sự thống trị của Arabica.</p>
<p>Bị loại khỏi giới elite cà phê, Phong về Đắk Lắk, xây dựng thương hiệu cà phê Robusta specialty đầu tiên, và chứng minh cho thế giới: hạt cà phê Việt Nam không "hạng hai."</p>"""

S19_CHAPTERS = [
("Chương 1: Cupping Session Gây Bão", """Portland, Oregon, trụ sở Specialty Coffee Association, phòng cupping VIP. Mười hai Q-grader — giám khảo cà phê elite nhất thế giới — ngồi quanh bàn cupping tròn, trước mặt mỗi người là mười hai cup cà phê được mã hóa.

Đoàn Thế Phong, ba mươi tám tuổi, Q-grader duy nhất từ Việt Nam trong nhóm mười hai, nâng cup thứ bảy lên mũi hít, rồi húp — kỹ thuật slurp chuẩn — để cà phê phủ khắp vòm miệng.

Hương chocolate đen, vị mật ong, body nặng nhưng mượt mà, aftertaste dài với note trái cây nhiệt đới. Phong ghi điểm: tám mươi bảy trên một trăm — specialty grade.

Khi kết quả được tiết lộ, phòng cupping im lặng sững sờ. Cup số bảy là: Robusta, nguồn gốc Đắk Lắk, Việt Nam. Chế biến: honey process.

"ROBUSTA SPECIALTY?" James Morrison, Chủ tịch Hội đồng Giám khảo SCA, đứng dậy. "Đây là cupping blind test, nhưng Robusta không thể đạt tám mươi bảy! Phong, anh chắc chắn?"

"Tôi chấm blind, mười hai cup, và cup này đạt tám mươi bảy," Phong đáp bình tĩnh. "Robusta hay Arabica không quan trọng. Chất lượng trong cup mới quan trọng."

"Nhưng SCA không công nhận Robusta specialty!" Morrison phản đối. "Hệ thống chấm điểm SCA được thiết kế cho Arabica!"

"Thì hệ thống đó cần cập nhật," Phong nói.

Ba ngày sau, Phong nhận email: "Quyết định của Hội đồng SCA: loại Q-grader Đoàn Thế Phong khỏi hội đồng giám khảo quốc tế, lý do: vi phạm quy trình đánh giá khi cho điểm specialty cho giống không đủ tiêu chuẩn."

Phong bị loại khỏi giới elite cà phê quốc tế — vì dám nói sự thật: Robusta Việt Nam ngon hơn nhiều người nghĩ."""),

("Chương 2: Về Đắk Lắk — Tìm Hạt Hoàn Hảo", """Phong bay về Buôn Ma Thuột, Đắk Lắk — thủ phủ cà phê Việt Nam. Đất đỏ bazan, nắng gió Tây Nguyên, và hàng triệu cây cà phê Robusta trải dài đến tận chân trời.

Việt Nam là nước xuất khẩu cà phê lớn thứ hai thế giới, nhưng chín mươi lăm phần trăm là Robusta giá rẻ, bán xô cho thị trường cà phê hòa tan — Nestlé mua một ký giá ba mươi nghìn đồng, chế biến thành Nescafé bán lại gấp hai mươi lần.

Nông dân trồng cà phê Việt Nam nghèo vì họ bán nguyên liệu thô, không có thương hiệu, không kiểm soát chất lượng.

"Robusta Việt Nam không dở. Nó bị đối xử dở," Phong nói khi đứng giữa vườn cà phê.

Anh bắt đầu dự án: tìm những vườn cà phê Robusta có hương vị đặc biệt — loại fine Robusta có thể đạt specialty grade. Sáu tháng đi khắp Đắk Lắk, Lâm Đồng, Gia Lai, cupping hàng nghìn mẫu.

Tại một vườn nhỏ ở huyện Krông Năng, nông dân Y Blan Niê Kdam — người dân tộc Ê Đê — trồng Robusta theo phương pháp truyền thống: thu hái cherry chín đỏ bằng tay, phơi honey process trên giàn tre.

Phong cupping mẫu của Y Blan: tám mươi lăm điểm. Specialty grade. "Đây rồi," Phong thì thầm."""),

("Chương 3: Thương Hiệu Cao Nguyên Ra Đời", """Phong thành lập "Cao Nguyên Coffee" — thương hiệu cà phê Robusta specialty đầu tiên của Việt Nam. Mô hình: mua trực tiếp từ nông dân với giá cao gấp ba — nhưng yêu cầu thu hái chọn lọc, chế biến đúng quy trình.

Hai mươi hộ nông dân Ê Đê ở Krông Năng tham gia. Phong dạy họ kỹ thuật honey process, natural process, và washed process — ba phương pháp chế biến tạo ra hương vị khác nhau.

Sản phẩm đầu tiên: "Cao Nguyên No.1" — Robusta honey process, tám mươi năm điểm, rang bởi chính Phong. Giá bán: năm trăm nghìn đồng mỗi hai trăm gram — đắt gấp mười cà phê Robusta thông thường, nhưng rẻ hơn specialty Arabica nhập khẩu.

Phong gửi mẫu đến hai mươi quán specialty coffee ở Sài Gòn, Hà Nội, Đà Nẵng. Mười tám trên hai mươi quán order thêm sau lần thử đầu tiên."""),

("Chương 4: Cup of Excellence — Vả Mặt Giới Elite", """Phong gửi Cao Nguyên No.1 tham gia Cup of Excellence — cuộc thi cà phê uy tín nhất thế giới. Đây là lần đầu tiên một Robusta được gửi dự thi.

Ban tổ chức phân vân — Cup of Excellence truyền thống chỉ dành cho Arabica. Nhưng quy chế không cấm Robusta. Phong trích dẫn: "Điều 3.1 — mọi loại cà phê sản xuất tại quốc gia đăng cai đều đủ điều kiện tham gia."

Kết quả blind cupping bởi hai mươi giám khảo quốc tế: Cao Nguyên No.1 đạt tám mươi bảy điểm, lọt top 10 trên tổng số hai trăm mẫu — tất cả các mẫu còn lại đều là Arabica.

Cộng đồng cà phê thế giới bàng hoàng. Perfect Daily Grind, Sprudge, và Barista Magazine đồng loạt: "A Vietnamese Robusta just scored 87 at Cup of Excellence — the specialty world will never be the same."

Morrison đọc tin, câm lặng. Q-grader mà ông loại vừa chứng minh: Robusta specialty là thật."""),

("Chương 5: Xuất Khẩu Ra Thế Giới", """Sau Cup of Excellence, Cao Nguyên Coffee nhận đơn đặt hàng từ hai mươi quốc gia. Blue Bottle (Mỹ), % Arabica (Nhật), và Monmouth Coffee (Anh) — những thương hiệu specialty hàng đầu — đều order.

Doanh thu năm đầu xuất khẩu: hai mươi tỷ đồng. Giá FOB mà nông dân Ê Đê nhận được: gấp năm lần giá bán xô cho Nestlé.

Y Blan — nông dân Ê Đê — xây nhà mới, mua xe, cho ba con đi học đại học. "Anh Phong dạy tôi: hạt cà phê của tôi không rẻ. Chỉ có người mua nó rẻ," Y Blan nói."""),

("Chương 6: Đế Chế Cà Phê Robusta", """Cao Nguyên Coffee mở rộng: hai trăm hộ nông dân ở bốn tỉnh Tây Nguyên. Nhà máy rang xay tại Buôn Ma Thuột, công suất năm mươi tấn mỗi tháng.

Phong mở quán flagship "Cao Nguyên" tại Sài Gòn, Hà Nội, và Tokyo — quán cà phê Robusta specialty đầu tiên trên thế giới.

Forbes Vietnam: "Đoàn Thế Phong — Người đưa Robusta Việt Nam lên bản đồ specialty." """),

("Chương 7: Mẹ Và Ly Cà Phê Sữa Đá", """Phong yêu cà phê vì mẹ. Bà Đoàn Thị Lan, bán cà phê vỉa hè ở Buôn Ma Thuột bốn mươi năm. Cà phê phin Robusta với sữa đặc — thức uống bình dân nhất Tây Nguyên.

"Mẹ, cà phê mẹ pha ngon nhất thế giới," Phong nói khi nhỏ.

"Con ơi, cà phê mẹ là Robusta, người ta kêu nó dở. Nhưng mẹ thấy nó ngon," bà Lan đáp.

Câu nói đó theo Phong suốt sự nghiệp: "Mẹ thấy nó ngon." Không cần SCA chấm điểm, không cần Q-grader xác nhận — mẹ anh đã biết Robusta ngon từ bốn mươi năm trước.

Quán flagship Cao Nguyên tại Sài Gòn có một menu đặc biệt: "Cà phê Mẹ Lan" — Robusta phin sữa đặc, công thức bà Lan, giá hai mươi lăm nghìn. Bestseller."""),

("Chương 8: SCA Thay Đổi Quy Chế", """Sau Cup of Excellence, SCA buộc phải thay đổi: mở rộng hệ thống chấm điểm để bao gồm Robusta và các giống cà phê khác — không chỉ Arabica.

Morrison từ chức Chủ tịch Hội đồng. SCA mời Phong quay lại với tư cách "Founding Member" của hội đồng đánh giá Robusta specialty mới thành lập.

Phong đồng ý — nhưng với điều kiện: hội đồng mới phải có ít nhất năm mươi phần trăm thành viên từ các nước sản xuất Robusta."""),

("Chương 9: Giải Thưởng Cà Phê Quốc Tế", """Phong nhận giải "Specialty Coffee Pioneer Award" — giải thưởng cao nhất của ngành cà phê specialty, tại Re:co Symposium, Seattle.

"Tôi bị loại khỏi hội đồng vì nói Robusta ngon. Hôm nay, hội đồng mời tôi quay lại vì Robusta đã chứng minh nó ngon. Sự thật không cần permission," Phong phát biểu.

Bài phát biểu được coi là "tuyên ngôn Robusta" — thay đổi cách thế giới nhìn nhận hạt cà phê Việt Nam."""),

("Chương 10: Quay Về Vườn Cà Phê", """Phong về Krông Năng, đứng giữa vườn cà phê của Y Blan. Cherry đỏ rực trên cành, nắng Tây Nguyên chiếu vàng lá xanh.

Y Blan, giờ năm mươi tuổi, tóc bạc, da nâu nắng, tay chai sần — nhưng mắt sáng rực khi nhìn vườn cà phê.

"Anh Phong, ngày xưa tôi bán cà phê cho thương lái giá ba mươi nghìn một ký. Giờ tôi bán một trăm năm mươi nghìn. Con tôi đi học đại học. Nhà tôi có mái tôn. Vì anh."

"Không phải vì tôi. Vì hạt cà phê của anh xứng đáng giá đó. Tôi chỉ giúp thế giới biết điều đó."

Hai người đàn ông — một Kinh, một Ê Đê — đứng giữa vườn cà phê, uống cà phê phin từ cherry vừa hái. Robusta, honey process, tám mươi bảy điểm.

Phong nhấp một ngụm, nhắm mắt. Vị cà phê giống hệt ly cà phê sữa đá mẹ anh pha ở vỉa hè Buôn Ma Thuột bốn mươi năm trước.

Mẹ đã biết. Từ rất lâu rồi."""),
]

# ═══════════════════════════════════════════════════════════════════════════════
# STORY 20: PHI CÔNG THỬ NGHIỆM
# ═══════════════════════════════════════════════════════════════════════════════

S20_TITLE = "BỊ CẤM BAY VÌ TỐ CÁO LỖI THIẾT KẾ MÁY BAY, TÔI TỰ CHẾ TẠO DRONE KHIẾN CẢ NGÀNH HÀNG KHÔNG DÂN DỤNG RÚT HỒ SƠ"
S20_AUTHOR = "Lê Anh Dũng"
S20_COVER = "base_cover_54.png"
S20_INTRO = """<p><strong>"Hai mươi năm tôi lái máy bay thử nghiệm cho hãng hàng không, phát hiện lỗi thiết kế có thể giết người. Đổi lại, khi tôi từ chối ký nhận máy bay lỗi, họ cấm tôi bay vĩnh viễn."</strong></p>
<p>Lê Anh Dũng, phi công thử nghiệm cấp cao nhất Việt Nam, bị hãng hàng không VietStar Airlines và nhà sản xuất phụ tùng Trần Đức Hưng cấm bay khi anh từ chối ký nhận máy bay có hệ thống autopilot lỗi.</p>
<p>Mất đôi cánh, Dũng chuyển sang chế tạo drone — từ hệ thống drone cứu nạn đến drone nông nghiệp — và xây dựng đế chế công nghệ bay không người lái khiến cả ngành hàng không dân dụng phải thay đổi tiêu chuẩn an toàn.</p>"""

S20_CHAPTERS = [
("Chương 1: Từ Chối Ký Nhận", """Hangar 7, sân bay Tân Sơn Nhất, bảy giờ sáng. Phi công thử nghiệm Lê Anh Dũng vừa hạ cánh sau chuyến bay thử nghiệm máy bay ATR 72-600 mới nhận từ nhà sản xuất — chuyến bay kiểm tra hệ thống trước khi đưa vào khai thác thương mại.

Dũng lau mồ hôi, mở sổ bay ghi chú: "Autopilot mode 2 — giật bất thường ở độ cao 5.000 feet, pitch oscillation 3 độ, duration 4 giây. Hệ thống tự chỉnh sau 4 giây nhưng đây là anomaly không nằm trong flight envelope."

Hai mươi năm bay thử nghiệm, một nghìn chuyến bay, Dũng nhận ra bất thường qua cảm giác — cái giật nhẹ mà phi công thương mại sẽ không nhận thấy, nhưng trong điều kiện thời tiết xấu hoặc tải nặng, nó có thể gây mất kiểm soát.

"Tôi không ký nhận máy bay này," Dũng nói với Giám đốc Kỹ thuật Nguyễn Hoàng Nam. "Autopilot có anomaly. Cần kiểm tra lại flight control computer."

Nam đọc sổ bay, mặt khó chịu: "Dũng, pitch oscillation ba độ trong bốn giây? Đó nằm trong giới hạn chấp nhận được. MEL cho phép."

"MEL cho phép nghĩa là máy bay bay được, không có nghĩa là máy bay an toàn. Tôi là phi công thử nghiệm, việc của tôi là đảm bảo AN TOÀN, không phải đảm bảo BAY ĐƯỢC."

"Dũng, máy bay này trị giá năm trăm tỷ. VietStar đã lên lịch khai thác từ tuần sau. Nếu anh không ký, hãng mất doanh thu ba tỷ đồng mỗi ngày."

"Ba tỷ mỗi ngày so với hai trăm mạng người trên máy bay. Anh chọn cái nào?"

Dũng không ký. Sáng hôm sau, anh nhận quyết định: "Đình chỉ bay vô thời hạn — phi công Lê Anh Dũng, lý do: không tuân thủ quy trình nghiệm thu máy bay."

Dũng bước ra khỏi hangar, nhìn chiếc ATR 72-600 đậu trong nắng sáng. Anh biết: nếu máy bay đó bay và xảy ra sự cố, máu sẽ đổ. Nhưng nếu anh ký, máu đó sẽ trên tay anh.

Anh chọn mất đôi cánh hơn mất lương tâm."""),

("Chương 2: Sự Cố Và Minh Oan", """Ba tháng sau khi Dũng bị cấm bay, chiếc ATR 72-600 — được phi công khác ký nhận — gặp sự cố trên không: autopilot giật mạnh ở độ cao bốn nghìn feet trong thời tiết xấu, máy bay nghiêng hai mươi độ trước khi phi công tắt autopilot và điều khiển thủ công.

Một trăm năm mươi hành khách, nhiều người bị thương nhẹ vì không thắt dây. Máy bay hạ cánh an toàn nhưng Cục Hàng không mở điều tra.

Điều tra phát hiện: lỗi nằm ở flight control computer — đúng thứ Dũng cảnh báo. Phụ tùng thay thế được cung cấp bởi công ty của Trần Đức Hưng — phụ tùng non-OEM, chất lượng thấp hơn tiêu chuẩn nhà sản xuất.

Dũng được minh oan. Nam bị cách chức. Hưng bị khởi tố tội "cung cấp vật tư hàng không không đạt tiêu chuẩn."

Nhưng Dũng không quay lại VietStar. Anh đã mất niềm tin vào hệ thống — nơi lợi nhuận được đặt trên an toàn."""),

("Chương 3: Chuyển Sang Drone", """Dũng chuyển hướng: từ lái máy bay có người lái sang chế tạo máy bay không người lái. "Drone không chở người, nên không ai chết nếu nó rơi. Nhưng drone cứu nạn thì cứu được người," anh lý luận.

Anh thành lập SkyDragon — startup drone Việt Nam, chuyên thiết kế drone cứu hộ thảm họa và drone nông nghiệp. Vốn ban đầu: toàn bộ tiền tiết kiệm hai mươi năm bay — một tỷ hai trăm triệu đồng.

Drone cứu hộ SkyDragon Rescue có thể bay trong gió cấp tám, mang phao cứu sinh, kit sơ cứu, và camera hồng ngoại tìm nạn nhân. Tầm bay năm mươi cây số, pin bốn giờ.

Sáu tháng phát triển prototype. Dũng áp dụng kiến thức aerodynamics từ hai mươi năm bay — hiểu gió, hiểu khí quyển, hiểu turbulence — vào thiết kế drone ổn định nhất thị trường."""),

("Chương 4: Cứu Nạn Miền Trung", """Mùa lũ miền Trung, SkyDragon Rescue được triển khai lần đầu tiên tại Quảng Bình. Nước lũ dâng cao ba mét, cô lập hàng nghìn hộ dân.

SkyDragon bay trong mưa gió, mang phao cứu sinh đến các nhà bị cô lập, camera hồng ngoại phát hiện người mắc kẹt trên mái nhà trong đêm tối. Ba ngày, đội drone SkyDragon hỗ trợ cứu hộ hai trăm bảy mươi người.

Video drone bay trong bão cứu người đạt ba mươi triệu lượt xem. Bộ Quốc phòng liên hệ SkyDragon để trang bị drone cứu hộ cho lực lượng biên phòng và quân đội."""),

("Chương 5: Drone Nông Nghiệp — Cánh Đồng Thông Minh", """SkyDragon mở rộng sang drone nông nghiệp: phun thuốc, gieo hạt, và giám sát mùa vụ bằng AI. Một drone thay thế hai mươi công nhân phun thuốc, chính xác hơn, an toàn hơn (không tiếp xúc hóa chất).

Năm nghìn nông dân đồng bằng sông Cửu Long sử dụng dịch vụ SkyDragon. Năng suất lúa tăng mười lăm phần trăm, chi phí giảm hai mươi phần trăm.

Doanh thu SkyDragon năm thứ hai: bốn mươi tỷ đồng — từ phi công bị cấm bay thành CEO startup drone lớn nhất Việt Nam."""),

("Chương 6: SkyDragon Thành Unicorn", """Series B từ Sequoia Capital và quỹ quốc phòng Singapore, một trăm triệu đô. Định giá SkyDragon một tỷ hai trăm triệu đô — drone unicorn đầu tiên Đông Nam Á.

SkyDragon mở rộng ra bốn lĩnh vực: cứu hộ, nông nghiệp, giám sát hạ tầng (cầu, đường, điện), và logistics. Nhà máy sản xuất drone tại Long Thành, công suất mười nghìn drone mỗi năm."""),

("Chương 7: Bố Và Chiếc Máy Bay Giấy", """Dũng mê bay vì bố. Ông Lê Văn Hùng, thợ cơ khí ở Hải Phòng, mỗi chiều gấp máy bay giấy cho con trai. Ông gấp đủ loại: mũi nhọn bay xa, cánh rộng bay chậm, cánh gập bay lượn.

"Bố, sao máy bay giấy bay được?" Dũng hỏi khi năm tuổi.

"Vì không khí nâng nó lên, con ơi. Gió ở dưới cánh mạnh hơn gió ở trên cánh. Đó gọi là lực nâng."

Bố giải thích nguyên lý Bernoulli cho con năm tuổi bằng máy bay giấy — và Dũng nhớ suốt đời.

Ông Hùng mất khi Dũng mười tám — bệnh phổi vì hít khói hàn cả đời. Trước khi mất, ông gấp cho Dũng chiếc máy bay giấy cuối cùng: "Con bay cao nha."

Chiếc máy bay giấy đó giờ nằm trong tủ kính văn phòng CEO SkyDragon — bên cạnh mô hình drone trị giá năm tỷ."""),

("Chương 8: VietStar Thay Đổi Tiêu Chuẩn", """Sau vụ sự cố ATR 72-600, Cục Hàng không Việt Nam ban hành quy chế mới: mọi phi công thử nghiệm có quyền từ chối ký nhận máy bay mà không bị trừng phạt, và báo cáo bất thường phải được điều tra bắt buộc.

VietStar mời Dũng quay lại với tư cách cố vấn an toàn bay. Dũng đồng ý — nhưng yêu cầu: phi công thử nghiệm phải có quyền veto tuyệt đối, không bị áp lực từ ban lãnh đạo.

Nam bị kết án ba năm tù treo. Hưng bị năm năm tù giam."""),

("Chương 9: Giải Thưởng Hàng Không Quốc Tế", """Dũng nhận giải "FAA Aviation Safety Award" — giải thưởng an toàn hàng không do Cục Hàng không Liên bang Mỹ trao — cho đóng góp trong lĩnh vực an toàn bay và công nghệ drone cứu hộ.

"Tôi bị cấm bay vì từ chối ký nhận máy bay lỗi. Hôm nay, tôi đứng đây không phải vì tôi đúng, mà vì hai trăm người trên chiếc máy bay đó vẫn sống," Dũng nói tại Washington D.C."""),

("Chương 10: Bay Lại Lần Cuối", """Dũng không bay máy bay thương mại nữa. Nhưng mỗi chiều Chủ nhật, anh lái drone SkyDragon đời mới bay trên cánh đồng Long Thành — chỉ để cảm giác bay.

Drone bay lên, camera truyền hình ảnh về kính VR trên mắt Dũng. Anh nhìn thấy mặt đất thu nhỏ, đường chân trời cong, và mây trắng — giống hệt view từ buồng lái ATR 72 ngày xưa.

"Bố ơi, con vẫn bay," anh thì thầm.

Rồi anh rút từ túi áo chiếc máy bay giấy — chiếc cuối cùng bố gấp — và thả nó bay theo gió Long Thành. Máy bay giấy lượn vòng, bắt gió, bay cao hơn Dũng tưởng.

Chiếc máy bay giấy của bố và chiếc drone triệu đô của con — cùng bay trên một bầu trời.

Đó là di sản. Đó là tình yêu. Đó là đôi cánh mà không ai cướp được."""),
]

# ═══════════════════════════════════════════════════════════════════════════════
# ASSEMBLY & PUBLISHING
# ═══════════════════════════════════════════════════════════════════════════════

ALL_STORIES = [
    {"title": S17_TITLE, "author": S17_AUTHOR, "cover": S17_COVER, "intro": S17_INTRO, "chapters": S17_CHAPTERS},
    {"title": S18_TITLE, "author": S18_AUTHOR, "cover": S18_COVER, "intro": S18_INTRO, "chapters": S18_CHAPTERS},
    {"title": S19_TITLE, "author": S19_AUTHOR, "cover": S19_COVER, "intro": S19_INTRO, "chapters": S19_CHAPTERS},
    {"title": S20_TITLE, "author": S20_AUTHOR, "cover": S20_COVER, "intro": S20_INTRO, "chapters": S20_CHAPTERS},
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
    log("🚀 BATCH 5 FINAL — 4 STORIES (17-20)")
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

    log(f"\n🏁 BATCH 5 FINAL COMPLETE: {len(results)}/4 published")
    log("🎊 ALL 20 STORIES PUBLISHED! 🎊")
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
