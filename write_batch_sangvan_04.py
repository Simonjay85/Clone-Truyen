#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
write_batch_sangvan_04.py — Batch 4: 4 Truyện Sảng Văn (Stories 13-16)
=====================================================================
Story 13: Đầu bếp sao Michelin bị trục xuất (cover 47)
Story 14: Nữ bác sĩ thú y bị cấm hành nghề (cover 48)
Story 15: Kỹ sư cầu đường bị gạt khỏi dự án (cover 49)
Story 16: Giám đốc sáng tạo quảng cáo bị sa thải (cover 50)
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
# STORY 13: ĐẦU BẾP SAO MICHELIN
# ═══════════════════════════════════════════════════════════════════════════════

S13_TITLE = "BỊ ĐUỔI KHỎI NHÀ HÀNG 3 SAO MICHELIN, TÔI MỞ QUÁN PHỞ KHIẾN CẢ PARIS XẾP HÀNG DÀI NỬA PHỐ"
S13_AUTHOR = "Ngô Văn Tài"
S13_COVER = "base_cover_47.png"
S13_INTRO = """<p><strong>"Tám năm tôi làm sous chef ở nhà hàng ba sao Michelin Paris, sáng tạo mười hai món signature ghi tên bếp trưởng. Đổi lại, khi tôi đề xuất đưa ẩm thực Việt Nam vào menu, họ sa thải tôi vì 'xúc phạm nền ẩm thực Pháp.'"</strong></p>
<p>Ngô Văn Tài, sous chef người Việt tại nhà hàng Le Petit Château (3 sao Michelin, Paris), bị Bếp trưởng Jean-Pierre Moreau và chủ nhà hàng sa thải khi anh đề xuất đưa nguyên liệu Việt Nam vào haute cuisine.</p>
<p>Mất việc ở đỉnh cao ẩm thực, Tài mở quán phở nhỏ trong ngõ hẻm Paris, rồi biến nó thành nhà hàng Việt đầu tiên nhận sao Michelin, khiến cả giới ẩm thực Pháp phải cúi đầu thừa nhận.</p>"""

S13_CHAPTERS = [
("Chương 1: Bị Đuổi Khỏi Bếp", """Bếp nhà hàng Le Petit Château, quận 8 Paris, mười giờ tối. Ngô Văn Tài đang hoàn thiện món tráng miệng cuối cùng cho khách VIP — soufflé chanh yuzu với sốt mango reduction — khi Bếp trưởng Jean-Pierre Moreau bước đến.

"Tài, vào phòng tôi. Ngay."

Moreau, sáu mươi tuổi, hai mét Chevalier de la Légion d'honneur, bếp trưởng giữ ba sao Michelin mười lăm năm liên tiếp. Ông là thầy, là idol, là kẻ áp bức — tất cả trong một.

"Tài, proposal tuần trước của cậu — đưa nước mắm, rau thơm Việt Nam, và phở vào menu degustation — tôi đã đọc."

"Vâng, chef. Tôi nghĩ flavor profile của nước mắm có thể complement umami trong sốt bò Pháp, tạo ra—"

"CẬU ĐIÊN RỒI!" Moreau đập bàn. "Nước mắm trong nhà hàng ba sao Michelin? Phở trên đĩa Limoges? Cậu muốn biến Le Petit Château thành quán ăn đường phố Sài Gòn?"

"Nhưng chef, Gaggan ở Bangkok dùng gia vị Ấn Độ và giữ hai sao Michelin. Den ở Bangkok kết hợp Thai-French và có một sao. Ẩm thực châu Á—"

"ĐÂY LÀ PARIS! KHÔNG PHẢI BANGKOK!" Moreau ném tạp dề lên bàn. "Tám năm tôi training cậu, dạy cậu từ cách cầm dao đến plating kỹ thuật, và cậu trả ơn bằng cách xúc phạm nền ẩm thực Pháp?"

"Tôi không xúc phạm! Tôi muốn MỞ RỘNG—"

"Ra khỏi bếp tôi. Cậu bị sa thải. Bỏ tạp dề, bỏ dao, ra cửa sau."

Tài cởi tạp dề, gấp gọn đặt lên bàn. Bộ dao cá nhân — quà sinh nhật bốn mươi tuổi, Tài tự mua bằng hai tháng lương — anh cầm theo.

Anh bước ra cửa sau nhà hàng, đứng trong ngõ hẻm Paris tháng mười một, mưa phùn lạnh buốt. Mùi rác, mùi ống thoát nước, mùi khói thuốc — mặt thật của Paris phía sau những nhà hàng sáng đèn.

"Nước mắm xúc phạm ẩm thực Pháp à?" Tài lẩm bẩm, siết chặt túi dao. "Được. Tôi sẽ cho ông thấy nước mắm xứng đáng đứng bên cạnh foie gras."

Trong túi áo anh, cuốn sổ tay ghi chép mười hai năm ở Pháp — từ công thức beurre blanc đến cách làm nước dùng phở của mẹ. Hai nền ẩm thực, hai dòng máu, một đầu bếp."""),

("Chương 2: Quán Phở Trong Ngõ Hẻm", """Tài thuê một mặt bằng bé tí — hai mươi mét vuông — trong ngõ hẻm rue des Martyrs, quận 9 Paris. Khu vực đa văn hóa, giá thuê rẻ, hàng xóm là tiệm bánh mì Thổ Nhĩ Kỳ và quán rượu Algérie.

Anh mở quán phở nhỏ, mười hai chỗ ngồi, tên: "Mẹ" — chỉ một chữ, viết bằng tiếng Việt trên biển hiệu gỗ sồi.

Menu: năm món duy nhất. Phở bò truyền thống (nước dùng hầm hai mươi bốn giờ), bún chả Hà Nội, bánh mì paté, gỏi cuốn, và chè bưởi. Không fusion, không biến tấu — thuần Việt, chuẩn công thức mẹ.

Nhưng kỹ thuật trình bày: haute cuisine. Phở được phục vụ trong bát sứ Limoges, rau thơm trang trí như herb garden trên đĩa Michelin, nước dùng trong vắt như consommé — vì nó được lọc kỹ bằng kỹ thuật clarification Pháp.

"Hương vị Việt Nam, kỹ thuật Pháp," Tài giải thích cho khách đầu tiên — một cặp vợ chồng Pháp lạc vào ngõ hẻm.

Người vợ húp một muỗng phở và nhắm mắt: "Mon Dieu... c'est extraordinaire."

Tin đồn lan nhanh. Food blogger Paris đầu tiên đến, rồi hai, rồi mười. Instagram tràn ngập hình phở bát sứ Limoges. Hashtag #MeRestaurantParis trending.

Ba tháng sau, hàng đợi dài nửa phố mỗi trưa. Hai mươi mét vuông, mười hai ghế, nhưng đặt bàn phải chờ hai tuần."""),

("Chương 3: Sao Michelin Gõ Cửa", """Một năm sau khai trương, Guide Michelin cử thanh tra viên ẩn danh đến "Mẹ" — lần đầu tiên trong lịch sử, thanh tra Michelin đánh giá một quán phở.

Kết quả: "Mẹ" nhận một sao Michelin — nhà hàng Việt Nam đầu tiên tại châu Âu nhận ngôi sao danh giá.

Le Figaro: "Un restaurant de phở étoilé Michelin? La cuisine vietnamienne entre dans l'histoire."

Moreau đọc tin trên Le Monde, tay run. Sous chef mà ông đuổi vì "xúc phạm ẩm thực Pháp" vừa được ẩm thực Pháp trao danh hiệu cao quý nhất.

Tài nhận điện thoại chúc mừng từ khắp thế giới. Nhưng cuộc gọi quan trọng nhất: mẹ anh, bà Ngô Thị Liên, bảy mươi tuổi, bán phở ở phố cổ Hà Nội.

"Con ơi, ngôi sao gì mà to dữ vậy?"

"Ngôi sao cho phở của mẹ, mẹ ơi. Con nấu đúng công thức mẹ dạy."

Bà Liên khóc. Sáu mươi năm nấu phở, chưa bao giờ bà nghĩ phở mình sẽ nhận sao Michelin."""),

("Chương 4: Moreau Phản Công", """Moreau không chấp nhận. Ông viết bài trên tạp chí ẩm thực L'Art Culinaire, chỉ trích: "Michelin đang hạ thấp tiêu chuẩn khi trao sao cho quán phở đường phố."

Bài báo gây tranh cãi lớn trong giới ẩm thực. Nhiều bếp trưởng Pháp bảo thủ đồng ý với Moreau. Nhưng thế hệ mới — những chef như Alain Ducasse, Hélène Darroze — lên tiếng bảo vệ Tài.

Ducasse viết trên Instagram: "La cuisine n'a pas de frontières. Félicitations à Tài — he brought truth to the table."

Tài không phản bác Moreau bằng lời. Anh phản bác bằng món ăn. Nhà hàng "Mẹ" mở rộng menu: thêm bún bò Huế, cơm tấm, và một món tráng miệng mới — "Saigon Soufflé," soufflé cà phê Việt Nam với sốt sữa đặc.

Khách đông hơn. Sao sáng hơn."""),

("Chương 5: Mở Rộng Ra Châu Âu", """Hai năm sau sao Michelin, Tài mở thêm ba chi nhánh: "Mẹ" London, "Mẹ" Amsterdam, "Mẹ" Berlin. Mỗi nhà hàng giữ menu thuần Việt, kỹ thuật haute cuisine, và không gian intimate tối đa ba mươi chỗ.

"Mẹ" London nhận Bib Gourmand. "Mẹ" Amsterdam lọt Gault & Millau top 50. Chuỗi "Mẹ" trở thành thương hiệu ẩm thực Việt uy tín nhất châu Âu.

Doanh thu chuỗi: hai trăm tỷ đồng mỗi năm — từ món phở bắt đầu trong ngõ hẻm hai mươi mét vuông."""),

("Chương 6: Đế Chế Ẩm Thực Việt", """Tài ký hợp đồng với Netflix làm series "Phở & Âm Nhạc" — docuseries bốn tập kể chuyện hành trình từ quán phở vỉa hè Hà Nội đến sao Michelin Paris. Series đạt top 5 Netflix toàn cầu.

Anh xuất bản sách "The Art of Phở: From Hanoi Streets to Michelin Stars" — bestseller tại Pháp, Mỹ, và Nhật Bản.

Tài trở thành gương mặt của ẩm thực Việt Nam trên thế giới — người chứng minh rằng phở, bún chả, bánh mì không kém bất kỳ món Pháp, Nhật, hay Ý nào."""),

("Chương 7: Mẹ Và Bát Phở Đầu Tiên", """Tài học nấu phở từ mẹ — bà Liên, bán phở trên phố cổ Hà Nội từ năm hai mươi tuổi. Quán nhỏ, ba bàn, mở từ năm giờ sáng đến chín giờ sáng mỗi ngày.

"Con ơi, bí quyết phở là gì?" Tài hỏi khi mười tuổi.

"Kiên nhẫn," mẹ đáp. "Nước dùng hầm hai mươi bốn giờ, không tắt lửa. Xương bò phải trụng rồi rửa sạch, không được hà tiện thời gian. Phở ngon là phở nấu bằng tình."

Tài mang bà Liên đến Paris lần đầu tiên. Bà bảy mươi tuổi, chưa bao giờ ra khỏi Hà Nội. Bà bước vào nhà hàng "Mẹ," nhìn bát phở trên đĩa sứ Limoges, rồi nếm.

"Đúng vị rồi, con. Nhưng thiếu một chút hạt tiêu." Bà rắc hạt tiêu vào, gật đầu hài lòng.

Tài cười, mắt cay. Michelin cho một sao, nhưng mẹ cho "đúng vị" — và đó mới là ngôi sao quan trọng nhất."""),

("Chương 8: Le Petit Château Mất Sao", """Ba năm sau khi Tài rời đi, Le Petit Château xuống còn hai sao Michelin — mất một sao vì menu "thiếu sáng tạo và lặp lại."

Moreau nghỉ hưu, trầm cảm. Mười hai món signature mà Tài sáng tạo bị gỡ khỏi menu — nhưng không ai thay thế được. Nhà hàng đau đớn nhận ra: mười lăm năm ba sao, một phần lớn nhờ sous chef người Việt mà họ sa thải.

Nhà hàng đóng cửa sáu tháng sau khi Moreau nghỉ hưu. Mặt bằng được rao bán. Không ai mua."""),

("Chương 9: James Beard Award", """Tài nhận James Beard Award — "Oscar ẩm thực" — hạng mục "Outstanding Chef International." Lễ trao giải tại New York, trước hai nghìn đầu bếp hàng đầu thế giới.

"Tôi bị đuổi vì muốn đưa nước mắm vào nhà hàng Pháp. Hôm nay, nước mắm đứng trên sân khấu này," Tài giơ chai nước mắm Phú Quốc lên, cả hội trường vỗ tay.

Chai nước mắm đó — loại mẹ anh dùng mỗi sáng — giờ được trưng bày tại James Beard Foundation Museum, bên cạnh dao của Julia Child."""),

("Chương 10: Quay Về Phố Cổ", """Tài bay về Hà Nội mỗi Tết, ngồi bán phở cùng mẹ ở quán nhỏ phố cổ — ba bàn, vẫn mở năm giờ sáng.

Khách đến quán không biết người đàn ông đang múc phở là chef sao Michelin, James Beard Award winner, gương mặt trang bìa Netflix.

"Bát phở hai mươi lăm nghìn," mẹ anh thu tiền, như mọi ngày.

Tài múc phở, nghe tiếng phố cổ thức giấc — tiếng xe máy, tiếng gánh hàng rong, tiếng hàng xóm chào nhau. Mùi phở bay trên phố Hà Nội tháng giêng, giống hệt mùi phở bay trên rue des Martyrs tháng mười một.

"Mẹ ơi, con nấu phở ở Paris, London, Amsterdam, Berlin. Nhưng phở ngon nhất vẫn là phở ở đây."

Bà Liên cười, tay vẫn thái hành: "Vì phở ở đây nấu bằng tình, con ơi."

Tài gật đầu, múc thêm bát nữa. Trên tường quán, bên cạnh tấm giấy ghi giá phở hai mươi lăm nghìn, anh treo một tấm ảnh nhỏ: ngôi sao Michelin — lấp lánh giữa phố cổ Hà Nội như chưa bao giờ thuộc về nơi nào khác."""),
]

# ═══════════════════════════════════════════════════════════════════════════════
# STORY 14: NỮ BÁC SĨ THÚ Y
# ═══════════════════════════════════════════════════════════════════════════════

S14_TITLE = "BỊ CẤM HÀNH NGHỀ THÚ Y, TÔI DỰNG TRẠI CỨU HỘ ĐỘNG VẬT KHIẾN CẢ NGÀNH CHĂN NUÔI PHẢI THAY ĐỔI"
S14_AUTHOR = "Lê Phương Thảo"
S14_COVER = "base_cover_48.png"
S14_INTRO = """<p><strong>"Mười năm tôi chữa trị cho hàng nghìn con vật, từ chó mèo hoang đến voi rừng bị thương. Đổi lại, khi tôi tố cáo trang trại heo công nghiệp bơm thuốc tăng trọng, họ vận động cấm tôi hành nghề."</strong></p>
<p>Lê Phương Thảo, nữ bác sĩ thú y hàng đầu Việt Nam, bị Chủ trang trại Đinh Văn Bắc và Chánh Thanh tra Sở NN&PTNT Trần Quốc Phong cấm hành nghề khi cô phát hiện và tố cáo đường dây bơm salbutamol vào heo.</p>
<p>Bị tước giấy phép, bị dọa, Thảo thành lập Trại cứu hộ động vật đầu tiên tại miền Nam, rồi xây dựng hệ sinh thái chăn nuôi sạch khiến ngành chăn nuôi Việt Nam phải thay đổi tiêu chuẩn.</p>"""

S14_CHAPTERS = [
("Chương 1: Phát Hiện Chấn Động", """Trang trại heo công nghiệp Phú Nông, huyện Củ Chi, hai giờ chiều. BS thú y Lê Phương Thảo đang khám định kỳ cho đàn heo hai nghìn con khi phát hiện bất thường: heo run, tim đập nhanh bất thường, và cơ bắp phì đại không tự nhiên.

"Đây không phải bệnh. Đây là triệu chứng ngộ độc salbutamol," Thảo thì thầm với trợ lý.

Salbutamol — chất cấm trong chăn nuôi — được bơm vào thức ăn heo để tăng tỷ lệ nạc, giảm mỡ, giúp heo "đẹp" hơn khi xuất chuồng. Nhưng tồn dư trong thịt gây nguy hiểm cho người ăn: tim đập nhanh, run tay, và nguy cơ ung thư lâu dài.

Thảo lấy mẫu nước tiểu heo, gửi xét nghiệm tại phòng lab độc lập. Kết quả: dương tính salbutamol, nồng độ gấp năm mươi lần ngưỡng cho phép.

"Hai nghìn con heo ở trang trại này đều bị bơm thuốc. Và mỗi ngày, năm mươi con được xuất ra chợ," Thảo tính nhẩm. Năm mươi con mỗi ngày, ba trăm sáu mươi lăm ngày mỗi năm — hàng triệu người ăn thịt heo nhiễm salbutamol.

Thảo viết báo cáo, gửi cho Sở NN&PTNT và Chi cục Thú y. Ngày hôm sau, cô nhận cuộc gọi từ Đinh Văn Bắc — chủ trang trại Phú Nông, đại gia chăn nuôi hàng đầu miền Nam.

"Thảo, gặp anh tại văn phòng. Ngay."

Bắc ngồi cạnh Chánh Thanh tra Trần Quốc Phong — người mà Thảo gửi báo cáo.

"Thảo, em là bác sĩ giỏi. Nhưng em can thiệp vào chuyện không phải của em. Trang trại Phú Nông là đơn vị đạt chuẩn VietGAP, sản phẩm sạch. Báo cáo của em gây hoảng loạn thị trường."

"Anh Bắc, kết quả xét nghiệm cho thấy salbutamol gấp năm mươi lần. Đây không phải hoảng loạn, đây là sự thật!"

"Kết quả xét nghiệm có thể sai," Phong lên tiếng, giọng mượt mà. "Chúng tôi sẽ cho kiểm tra lại bằng phòng lab của Sở."

"Phòng lab của Sở?" Thảo cười khẩy. "Phòng lab mà anh Phong kiểm soát? Kết quả chắc sẽ 'âm tính' ngay."

Phong đập bàn: "Cô cẩn thận! Tôi có quyền thu hồi giấy phép hành nghề thú y của cô!"

Một tuần sau, Thảo nhận quyết định: tạm đình chỉ giấy phép hành nghề BS thú y sáu tháng, lý do "vi phạm quy trình lấy mẫu và báo cáo." """),

("Chương 2: Trại Cứu Hộ Động Vật", """Mất giấy phép, Thảo không chữa trị chuyên nghiệp được. Nhưng cô không bỏ cuộc. Cô dùng toàn bộ tiền tiết kiệm — bốn trăm triệu đồng — thuê hai hecta đất ở Bình Dương, mở Trại cứu hộ động vật "Bàn Tay Xanh."

Trại nhận nuôi chó mèo bị bỏ rơi, động vật hoang dã bị thương, và gia súc bị bạo hành từ trang trại công nghiệp. Tháng đầu, Thảo cứu ba mươi con chó từ lò mổ, mười lăm con mèo hoang, và một con voi con bị xích chân ở Đắk Lắk.

Cô đăng video cứu hộ lên YouTube — kênh "Bàn Tay Xanh" đạt năm trăm nghìn subscribers trong ba tháng. Video cứu voi con đạt mười triệu lượt xem.

Nhưng quan trọng hơn, Thảo dùng nền tảng này để tố cáo: cô đăng kết quả xét nghiệm salbutamol, quay video bí mật bên trong trang trại Phú Nông, và phỏng vấn công nhân tiết lộ quy trình bơm thuốc.

Video đạt hai mươi triệu lượt xem. Bộ NN&PTNT buộc phải vào cuộc."""),

("Chương 3: Thanh Tra Và Đổ Bể", """Bộ NN&PTNT cử đoàn thanh tra cấp trung ương kiểm tra trang trại Phú Nông. Bắc bị bắt quả tang: kho chứa năm tấn salbutamol dạng bột, hệ thống trộn thuốc vào thức ăn, và sổ sách ghi chép liều lượng.

Bắc bị bắt. Phong bị cách chức. Trang trại Phú Nông bị đóng cửa. Hai nghìn con heo bị tiêu hủy.

Giấy phép hành nghề của Thảo được khôi phục ngay lập tức. Bộ trưởng Bộ NN&PTNT gọi điện cá nhân xin lỗi.

VnExpress: "Nữ BS thú y bị cấm hành nghề phá vỡ đường dây salbutamol lớn nhất miền Nam." """),

("Chương 4: Chăn Nuôi Sạch", """Sau vụ Phú Nông, Thảo thành lập GreenFarm — hệ sinh thái chăn nuôi sạch, kết nối trang trại organic với người tiêu dùng. Mỗi sản phẩm có QR code truy xuất nguồn gốc, từ con giống đến thức ăn, từ xét nghiệm thuốc đến ngày xuất chuồng.

Năm trăm trang trại gia đình tại miền Tây và Tây Nguyên tham gia. Doanh thu năm đầu: năm mươi tỷ đồng. Thịt heo GreenFarm có giá cao hơn ba mươi phần trăm — nhưng người tiêu dùng sẵn sàng trả vì tin tưởng."""),

("Chương 5: Cứu Voi Rừng Đắk Lắk", """Thảo dẫn đội cứu hộ "Bàn Tay Xanh" đến Đắk Lắk cứu ba con voi bị xích chân phục vụ du lịch. Chiến dịch kéo dài sáu tháng — đàm phán với chủ voi, huy động quỹ quốc tế, và xây dựng khu bảo tồn.

Ba con voi được giải phóng, chuyển đến Khu bảo tồn voi Yok Đôn — vùng rừng tự nhiên rộng một trăm hecta. Video khoảnh khắc voi bước vào rừng lần đầu sau mười năm bị xích đạt năm mươi triệu lượt xem, được chia sẻ bởi National Geographic và WWF.

"Mỗi con vật đều xứng đáng được sống tự do," Thảo nói trước camera, mắt đỏ hoe."""),

("Chương 6: GreenFarm Nhân Rộng", """GreenFarm huy động vốn Series A từ quỹ tác động xã hội Omidyar Network — mười lăm triệu đô. Mở rộng sang truy xuất nguồn gốc cho thủy sản, gia cầm, và rau củ.

Đội ngũ hai trăm người. Mười lăm nghìn trang trại kết nối. Một triệu người dùng app GreenFarm để quét QR code khi mua thịt.

Thảo được Forbes Vietnam vinh danh "Nữ doanh nhân tác động xã hội của năm." """),

("Chương 7: Con Mèo Ba Chân", """Thảo yêu động vật vì một con mèo. Năm mười tuổi, ở quê Bình Định, cô nhặt được con mèo hoang bị xe cán mất một chân trước. Bố không cho nuôi. Mẹ lén giấu mèo trong bếp.

Thảo dùng thanh tre và băng vải quấn chân mèo — "phẫu thuật" đầu tiên của cô. Con mèo sống, đi bằng ba chân, theo Thảo suốt mười hai năm.

"Mèo Ba Chân dạy tôi: sinh vật nào cũng xứng đáng được chữa trị, dù bị cả thế giới bỏ rơi," Thảo viết trong tự truyện.

Logo của "Bàn Tay Xanh" là hình một con mèo ba chân — kỷ vật tuổi thơ, biểu tượng cho mọi sinh vật bị bỏ rơi."""),

("Chương 8: Bắc Và Phong Lĩnh Án", """Tòa tuyên: Đinh Văn Bắc năm năm tù, Trần Quốc Phong bốn năm tù về tội "sản xuất thực phẩm kém chất lượng" và "lợi dụng chức vụ."

Trang trại Phú Nông bị tịch thu, đất đai được chuyển thành khu chăn nuôi mẫu của GreenFarm — từ nơi bơm thuốc trở thành biểu tượng chăn nuôi sạch.

Thảo không dự phiên tòa. Cô đang cứu hộ đàn khỉ bị nuôi nhốt trái phép ở Bình Phước."""),

("Chương 9: Giải Goldman Environmental Prize", """Thảo nhận Goldman Environmental Prize — "Nobel Môi trường" — giải thưởng danh giá nhất thế giới cho nhà hoạt động môi trường.

"Tôi bị cấm chữa trị động vật. Nhưng không ai cấm được lòng thương xót," Thảo nói trên sân khấu San Francisco, trước ba trăm nhà hoạt động toàn cầu.

"Mỗi bát thịt sạch trên bàn ăn là một chiến thắng. Mỗi con vật được giải cứu là một phép màu." """),

("Chương 10: Trở Về Trang Trại", """Thảo đứng giữa trang trại GreenFarm mẫu tại Củ Chi — trên chính mảnh đất của Phú Nông cũ. Heo chạy tự do trong chuồng mở, ăn thức ăn organic, không thuốc, không xích.

Cô ngồi xuống cạnh một con heo mẹ đang cho bầy con bú, vuốt tai nó nhẹ nhàng.

"Chị biết không, ngày xưa ở đây chị bị nhốt, bị bơm thuốc, bị đau," cô thì thầm. "Giờ chị được sống đúng cách rồi."

Trên cánh tay Thảo, một vết sẹo dài — kỷ niệm lần bị chó cắn khi cứu hộ năm đầu tiên. Cô không xóa sẹo. Đó là huân chương.

Mèo Ba Chân — phiên bản mới, một con mèo hoang ba chân mà trại vừa cứu — đang ngủ cuộn tròn bên chân Thảo.

Vòng tròn khép lại. Từ con mèo ba chân ở Bình Định đến trại cứu hộ hàng nghìn con vật, từ bác sĩ bị cấm hành nghề đến người thay đổi ngành chăn nuôi — Thảo vẫn là cô bé mười tuổi yêu động vật, chỉ giờ có thêm sức mạnh."""),
]

# ═══════════════════════════════════════════════════════════════════════════════
# STORY 15: KỸ SƯ CẦU ĐƯỜNG
# ═══════════════════════════════════════════════════════════════════════════════

S15_TITLE = "BỊ GẠT KHỎI DỰ ÁN CẦU TREO, TÔI TỰ THIẾT KẾ CẦU CỨU CẢ VÙNG CAO TÂY BẮC THOÁT CÔ LẬP"
S15_AUTHOR = "Bùi Đức Anh"
S15_COVER = "base_cover_49.png"
S15_INTRO = """<p><strong>"Năm năm tôi khảo sát địa hình, tính toán kết cấu, thiết kế cầu treo dây văng cho vùng cao Tây Bắc. Đổi lại, nhà thầu thông đồng quan chức cắt bớt vật liệu, cầu sập, và đổ tội cho thiết kế của tôi."</strong></p>
<p>Bùi Đức Anh, kỹ sư kết cấu cầu đường tài năng, bị nhà thầu Lương Đình Phú và quan chức Sở GTVT tỉnh Trần Đại Nghĩa vu oan khi cầu treo Nà Hản sập do bớt vật liệu, không phải do thiết kế sai.</p>
<p>Mất danh dự, bị truy tố, Đức Anh dùng bằng chứng kỹ thuật minh oan và tự tay thiết kế, xây dựng năm mươi cây cầu dân sinh cứu hàng nghìn đồng bào vùng cao thoát cô lập.</p>"""

S15_CHAPTERS = [
("Chương 1: Cầu Sập", """Sáu giờ sáng, cầu treo Nà Hản bắc qua suối Nậm Mu, huyện Mù Cang Chải, sập khi mười ba người dân — gồm năm em học sinh tiểu học — đang qua cầu đi chợ và đi học.

Bốn người bị thương nặng, trong đó hai em nhỏ gãy chân. Không ai chết, nhưng cả vùng rúng động.

Cầu treo Nà Hản — thiết kế bởi kỹ sư Bùi Đức Anh, thi công bởi nhà thầu Lương Đình Phú, kiểm định bởi Sở GTVT tỉnh do Trần Đại Nghĩa phụ trách — vừa hoàn thành sáu tháng trước.

Đức Anh nhận tin khi đang khảo sát địa hình cho dự án cầu mới ở Lai Châu. Anh lái xe bốn tiếng về Nà Hản, lao xuống lòng suối kiểm tra xác cầu.

Và anh thấy ngay: cáp thép treo cầu — thiết kế yêu cầu cáp đường kính hai mươi tư milimet, loại chịu lực mười lăm tấn — thực tế được thay bằng cáp mười sáu milimet, chịu lực chỉ bảy tấn. Bản lề thép không gỉ bị thay bằng bản lề sắt thường, đã rỉ sét sau sáu tháng.

"Nhà thầu cắt bớt vật liệu," Đức Anh thì thầm, tay run. "Cầu sập không phải vì thiết kế sai, mà vì bọn chúng ăn bớt năm mươi phần trăm vật liệu."

Nhưng khi đoàn thanh tra đến, Phú — nhà thầu — đã chuẩn bị sẵn: hồ sơ thi công giả ghi rõ vật liệu đúng thiết kế, và biên bản nghiệm thu có chữ ký Nghĩa. Kết luận thanh tra: "Lỗi thiết kế kết cấu — kỹ sư Bùi Đức Anh tính toán sai tải trọng."

Đức Anh bị khởi tố."""),

("Chương 2: Minh Oan Bằng Kỹ Thuật", """Trong trại tạm giam, Đức Anh nhờ luật sư yêu cầu giám định độc lập. Viện Khoa học Công nghệ Xây dựng — đơn vị giám định cấp quốc gia — cử chuyên gia đến hiện trường.

Kết quả: cáp thép thực tế là mười sáu milimet, không phải hai mươi bốn milimet theo thiết kế. Mẫu bê tông mố cầu đạt sáu mươi phần trăm cường độ yêu cầu — bớt xi măng. Tổng giá trị vật liệu bị cắt bớt: một tỷ hai trăm triệu đồng trên tổng giá trị cầu ba tỷ.

Hồ sơ thi công giả bị phát hiện: giấy xuất kho vật liệu ghi ngày cung cấp cáp hai mươi bốn milimet, nhưng nhà cung cấp xác nhận chưa bao giờ bán loại cáp đó cho Phú.

Đức Anh được minh oan. Phú và Nghĩa bị bắt."""),

("Chương 3: Năm Mươi Cây Cầu", """Sau minh oan, Đức Anh không quay lại làm thuê. Anh thành lập "Quỹ Cầu Dân Sinh" — tổ chức phi lợi nhuận thiết kế và xây cầu treo miễn phí cho vùng cao.

Mô hình: Đức Anh thiết kế kỹ thuật miễn phí, vật liệu do doanh nghiệp tài trợ, thi công do đồng bào địa phương tham gia dưới sự giám sát trực tiếp của anh. Không qua nhà thầu, không qua trung gian.

Ba năm, năm mươi cây cầu treo dân sinh được xây dựng tại Yên Bái, Lào Cai, Lai Châu, Sơn La, Hà Giang. Mỗi cây cầu kết nối một bản làng với trường học, chợ, và trạm y tế.

Hai mươi nghìn đồng bào dân tộc thoát cô lập nhờ cầu của Đức Anh."""),

("Chương 4: Cầu Thông Minh IoT", """Đức Anh phát triển "Smart Bridge" — cầu treo tích hợp sensor IoT giám sát kết cấu realtime: sensor đo lực căng cáp, gia tốc kế đo rung, và camera giám sát.

Dữ liệu truyền về cloud, AI phân tích, cảnh báo trước khi cầu có nguy cơ hỏng. Không bao giờ để cầu sập mà không ai biết trước.

Công nghệ Smart Bridge được Bộ GTVT áp dụng thí điểm cho một trăm cầu dân sinh toàn quốc."""),

("Chương 5: Giải Thưởng Kỹ Thuật Hạ Tầng", """Đức Anh nhận giải "ASCE Outstanding Civil Engineering Achievement Award" — giải thưởng kỹ thuật xây dựng uy tín nhất thế giới do Hiệp hội Kỹ sư Xây dựng Mỹ trao.

"Năm mươi cây cầu không phải công trình vĩ đại. Nhưng mỗi cây cầu cứu một em nhỏ khỏi lội suối đi học mùa lũ — và đó là kỹ thuật vĩ đại nhất," Đức Anh phát biểu."""),

("Chương 6: Mở Rộng Ra Lào Và Campuchia", """Quỹ Cầu Dân Sinh mở rộng sang Lào và Campuchia — các nước có hàng nghìn bản làng cô lập. Tổng cộng một trăm cầu trong năm năm, ba quốc gia.

UNDP tài trợ năm triệu đô cho chương trình. Đức Anh trở thành chuyên gia tư vấn hạ tầng vùng cao cho Liên Hợp Quốc tại Đông Nam Á."""),

("Chương 7: Bố Và Cây Cầu Ván", """Đức Anh theo nghề cầu đường vì bố. Ông Bùi Văn Hùng, dân tộc Thái, lớn lên ở bản Nà Hản — đúng nơi cây cầu sập.

Thuở nhỏ, bố Đức Anh mỗi ngày lội suối Nậm Mu đi học — mùa lũ, nước dâng ngang ngực, nhiều bạn bè bỏ học vì sợ. Bố tự đóng cầu ván bắc qua suối — hai tấm ván gỗ, không lan can — để con cái trong bản đi học.

"Cầu ván của bố là cây cầu đầu tiên con nhìn thấy. Nó xấu lắm, nhưng nó cứu mạng," Đức Anh kể.

Cây cầu Nà Hản mới — do Đức Anh thiết kế lại, miễn phí — giờ mang tên "Cầu Bố Hùng." Bố anh dự lễ khánh thành, tay sờ lan can thép không gỉ, mắt ướt: "Cầu này đẹp hơn cầu ván của bố nhiều quá." """),

("Chương 8: Phú Và Nghĩa Lĩnh Án", """Tòa tuyên: Lương Đình Phú mười hai năm tù, Trần Đại Nghĩa tám năm tù. Bồi thường cho bốn người bị thương hai tỷ đồng. Tài sản Phú bị kê biên.

Đức Anh gửi thư cho Phú trong trại giam: "Anh bớt một tỷ hai trăm triệu tiền vật liệu. Tôi xây năm mươi cây cầu, mỗi cây ba tỷ, tổng một trăm năm mươi tỷ. Thế nào rẻ hơn, anh tự biết." """),

("Chương 9: Đại Sứ Hạ Tầng UNDP", """Đức Anh được bổ nhiệm Đại sứ Hạ tầng Bền vững của UNDP — đại diện toàn cầu cho chương trình kết nối hạ tầng vùng sâu vùng xa.

Anh đi hai mươi quốc gia, từ Nepal đến Ethiopia, chia sẻ mô hình "cầu dân sinh cộng đồng" — thiết kế chuyên nghiệp, thi công cộng đồng, giám sát IoT."""),

("Chương 10: Đi Qua Cầu Nà Hản", """Đức Anh quay về Nà Hản một sáng mùa thu. Cầu Bố Hùng sáng loáng dưới nắng sớm, cáp thép hai mươi bốn milimet căng đều, sensor IoT nhấp nháy đèn xanh.

Năm em nhỏ — con của những em bị thương ngày cầu sập — đang chạy qua cầu đi học, cặp sách nhảy trên lưng, tiếng cười vang khắp thung lũng.

Đức Anh đứng đầu cầu, nhìn các em qua. Bố anh đứng bên cạnh, tay chống gậy.

"Bố ơi, cầu bố đóng ngày xưa bằng hai tấm ván. Giờ con đóng cầu bằng thép và cáp. Nhưng ý nghĩa giống nhau."

"Ý nghĩa gì?" bố hỏi.

"Để mấy đứa nhỏ đi học không phải lội suối."

Bố cười, vỗ vai con trai. Hai người cùng đi qua cầu — cây cầu thứ nhất và cây cầu thứ năm mươi mốt."""),
]

# ═══════════════════════════════════════════════════════════════════════════════
# STORY 16: GIÁM ĐỐC SÁNG TẠO QUẢNG CÁO
# ═══════════════════════════════════════════════════════════════════════════════

S16_TITLE = "BỊ SA THẢI VÌ TỪ CHỐI LÀM QUẢNG CÁO GIẢ DỐI, TÔI LẬP AGENCY KHIẾN CẢ NGÀNH TRUYỀN THÔNG THAY ĐỔI"
S16_AUTHOR = "Vương Bảo Ngọc"
S16_COVER = "base_cover_50.png"
S16_INTRO = """<p><strong>"Mười hai năm tôi là Giám đốc Sáng tạo, tạo ra hàng trăm chiến dịch quảng cáo đoạt giải. Đổi lại, khi tôi từ chối làm quảng cáo cho sản phẩm giảm cân giả mạo, họ sa thải tôi ngay trước giải Cannes Lions."</strong></p>
<p>Vương Bảo Ngọc, Giám đốc Sáng tạo hàng đầu ngành quảng cáo Việt Nam, bị sa thải khỏi MediaMax khi cô từ chối làm quảng cáo cho dòng sản phẩm giảm cân chứa chất cấm, gây nguy hiểm cho người tiêu dùng.</p>
<p>Mất việc, mất danh tiếng ngành, Ngọc thành lập TruthAds — agency quảng cáo "chỉ nói sự thật," phá vỡ mọi quy tắc ngành và chứng minh: trung thực bán được hàng hơn gian dối.</p>"""

S16_CHAPTERS = [
("Chương 1: Chiến Dịch Cuối Cùng", """Phòng sáng tạo tầng mười hai, MediaMax Agency, quận 1, mười giờ tối. Vương Bảo Ngọc ngồi trước storyboard chiến dịch quảng cáo cho SlimPro — dòng sản phẩm giảm cân "thần tốc" của tập đoàn Minh Quang Pharma.

Brief yêu cầu: "Quảng cáo SlimPro giảm mười kg trong hai tuần, không cần ăn kiêng, không cần tập luyện." Kèm theo: testimonial giả của người nổi tiếng, ảnh before/after photoshop, và khẩu hiệu "Khoa học đứng sau mỗi viên SlimPro."

Ngọc đọc brief, đọc lại, rồi mở laptop kiểm tra: SlimPro chứa sibutramine — chất cấm trong thực phẩm chức năng, gây tăng huyết áp, đau tim, và tử vong. Đã bị FDA và ANSM Pháp cấm từ 2010.

"Sản phẩm này chứa chất cấm gây chết người," Ngọc nói thẳng trong cuộc họp với CEO MediaMax Nguyễn Hữu Đại và Giám đốc Marketing Minh Quang Pharma.

"Ngọc, cô là Creative Director, không phải pharmacist," Đại gầm. "Minh Quang là client lớn nhất, revenue năm mươi tỷ mỗi năm. Cô làm quảng cáo, không làm thanh tra y tế!"

"Tôi làm quảng cáo, nhưng tôi không làm quảng cáo giết người. Sibutramine đã khiến hai mươi mốt người chết ở châu Âu."

"CÔ TỪ CHỐI CLIENT?" Đại đứng dậy, mặt đỏ bừng. "Từ chối Minh Quang nghĩa là từ chối MediaMax. Cô bị sa thải, effective immediately."

Ngọc đứng dậy bình tĩnh: "Anh Đại, tôi làm quảng cáo mười hai năm. Mỗi chiến dịch tôi tạo ra đều trung thực. Đó là giới hạn của tôi, và tôi không nhượng bộ."

Cô thu dọn đồ — portfolio bản in, cúp Cannes Lions Bronze ba lần, và bức ảnh team cũ — rồi bước ra khỏi MediaMax lần cuối.

Trong thang máy, Ngọc nhìn phản chiếu mình trong gương: ba mươi tám tuổi, mười hai năm sự nghiệp, Creative Director trẻ nhất lịch sử MediaMax. Giờ thất nghiệp.

Nhưng cô mỉm cười. Vì cô biết: mỗi viên SlimPro mà cô từ chối quảng cáo là một mạng người cô bảo vệ."""),

("Chương 2: TruthAds Ra Đời", """Ngọc thuê văn phòng nhỏ trên đường Nguyễn Đình Chiểu, treo biển: "TruthAds — We Only Tell The Truth."

Quy tắc sắt: TruthAds chỉ nhận client có sản phẩm thật, không phóng đại, không testimonial giả, không ảnh photoshop. Mỗi claim trong quảng cáo phải có bằng chứng khoa học.

Ba tháng đầu, không client nào đến. Các brand đều muốn "làm đẹp" sản phẩm, không muốn "nói thật."

Nhưng Ngọc kiên nhẫn. Cô viết bài trên LinkedIn: "Tại sao quảng cáo trung thực bán hàng tốt hơn?" — phân tích case study của Patagonia, Dove, và IKEA, chứng minh transparent advertising tăng brand loyalty bốn mươi phần trăm.

Bài viết viral — hai triệu lượt đọc. Client đầu tiên đến: một startup mỹ phẩm organic muốn quảng cáo "đúng sự thật, không hứa hẹn phép màu." """),

("Chương 3: Chiến Dịch Đầu Tiên — Viral Vì Trung Thực", """Client đầu tiên: BotanicSkin, startup mỹ phẩm thiên nhiên. Sản phẩm: kem dưỡng da từ nghệ và dầu dừa.

Quảng cáo thông thường sẽ nói: "Da trắng mịn sau 7 ngày!" TruthAds nói: "Kem dưỡng từ nghệ. Da mềm hơn sau 3 tuần sử dụng đều đặn. Không có phép màu, chỉ có kiên nhẫn."

Video quảng cáo: phụ nữ thật, không makeup, không filter, thoa kem và kể trải nghiệm thật — "Tôi dùng hai tuần, da hết khô. Không trắng hơn, nhưng khỏe hơn."

Internet sốc vì sự trung thực. Video đạt mười triệu lượt xem. BotanicSkin tăng doanh thu bốn trăm phần trăm — vì người tiêu dùng tin tưởng.

"Người ta nghĩ trung thực thì mất khách. Thực ra, trung thực tạo lòng tin. Và lòng tin tạo khách trung thành," Ngọc nói."""),

("Chương 4: MediaMax Sụp Đổ", """Sáu tháng sau khi Ngọc rời đi, SlimPro bị Cục An toàn Thực phẩm thu hồi — phát hiện sibutramine. Ba người nhập viện vì biến chứng tim mạch sau khi dùng SlimPro.

MediaMax bị kiện vì quảng cáo sai sự thật. Đại bị phạt và mất giấy phép quảng cáo dược phẩm. Minh Quang Pharma bị khởi tố.

Các client lớn rút hợp đồng khỏi MediaMax — không ai muốn liên quan đến agency dính scandal sản phẩm gây hại. MediaMax thu hẹp từ hai trăm nhân viên xuống ba mươi.

Ngọc không lên tiếng, không chỉ trích cũ. Cô chỉ đăng một dòng trên LinkedIn: "The truth always wins. It just takes time." """),

("Chương 5: TruthAds Bùng Nổ", """Sau scandal MediaMax, các brand đổ xô đến TruthAds — muốn agency "sạch" để bảo vệ danh tiếng.

Hai năm, TruthAds có năm mươi client, doanh thu sáu mươi tỷ đồng, đội ngũ tám mươi người. Chiến dịch cho Vinamilk Organic, Phúc Long, và The Coffee House đều đoạt giải Effie Awards.

Ngọc thiết lập "Truth Score" — bộ chỉ số đánh giá mức độ trung thực của mỗi chiến dịch quảng cáo. Brand nào đạt Truth Score 90/100 trở lên được gắn "TruthAds Certified" — trở thành tiêu chuẩn tin cậy trong ngành."""),

("Chương 6: Cannes Lions Grand Prix", """TruthAds đoạt Cannes Lions Grand Prix — giải cao nhất liên hoan quảng cáo sáng tạo thế giới — cho chiến dịch "Honest Beauty" cùng BotanicSkin: phụ nữ Việt Nam ở mọi lứa tuổi, không filter, kể chuyện da thật.

Ngọc đứng trên sân khấu Palais des Festivals, Cannes, nhận cúp vàng. Ba lần Bronze trước đó ở MediaMax, giờ một lần Grand Prix ở TruthAds.

"Quảng cáo hay nhất không phải quảng cáo đẹp nhất. Quảng cáo hay nhất là quảng cáo thật nhất," cô nói, và cả hội trường đứng dậy vỗ tay."""),

("Chương 7: Mẹ Và Chợ Bến Thành", """Ngọc yêu sự trung thực vì mẹ. Bà Vương Thị Hoa, bán trái cây ở chợ Bến Thành bốn mươi năm. Bà không bao giờ gian lận: trái nào dập thì nói dập, trái nào chua thì nói chua.

"Mẹ, sao mẹ không nói xoài ngọt để bán nhanh?"

"Con ơi, mình nói dối một lần, khách mất niềm tin cả đời. Mẹ bán chợ bốn mươi năm, khách quen theo mẹ từ đời ông bà ngoại con."

Triết lý bán trái cây trở thành triết lý quảng cáo. TruthAds về bản chất chỉ là phiên bản digital của sạp trái cây bà Hoa ở chợ Bến Thành."""),

("Chương 8: Đại Bị Phạt", """Đại bị phạt hai tỷ đồng, cấm hành nghề quảng cáo dược phẩm năm năm. MediaMax chính thức giải thể sau ba năm lao dốc.

Nhiều nhân viên cũ của MediaMax xin vào TruthAds. Ngọc nhận tất cả — nhưng yêu cầu mỗi người ký cam kết: "Tôi không bao giờ tạo quảng cáo sai sự thật." """),

("Chương 9: TED Talk Và Luật Quảng Cáo Mới", """Ngọc được mời TED Talk "The Business of Truth" — bài nói về sức mạnh kinh tế của quảng cáo trung thực, đạt bốn triệu lượt xem.

Quốc hội Việt Nam mời Ngọc tham gia góp ý Luật Quảng cáo sửa đổi — bổ sung quy định bắt buộc ghi rõ bằng chứng cho mọi claim trong quảng cáo thực phẩm chức năng và mỹ phẩm."""),

("Chương 10: Quay Về Chợ Bến Thành", """Ngọc đưa mẹ đi xem văn phòng TruthAds mới — tầng penthouse tòa nhà trên đường Nguyễn Huệ, view sông Sài Gòn.

Bà Hoa nhìn quanh văn phòng sáng đèn, tám mươi nhân viên, cúp Cannes Lions Grand Prix trên kệ.

"Ngọc ơi, công ty con đẹp quá. Nhưng sao không ai ở đây ăn trái cây?"

Ngọc cười, đặt rổ xoài của mẹ lên bàn meeting room. Ngày hôm đó, tám mươi nhân viên TruthAds ăn xoài từ sạp bà Hoa — xoài thật, không hóa chất, không nói dối, giống hệt quảng cáo của TruthAds.

Trên tường meeting room, Ngọc treo một tấm biển gỗ viết tay: "Trái nào dập nói dập, trái nào chua nói chua — Bà Vương Thị Hoa, chợ Bến Thành."

Đó là slogan đầu tiên của TruthAds, viết bởi người phụ nữ bán trái cây bốn mươi năm — triết lý kinh doanh vĩ đại nhất mà không trường MBA nào dạy."""),
]

# ═══════════════════════════════════════════════════════════════════════════════
# ASSEMBLY & PUBLISHING
# ═══════════════════════════════════════════════════════════════════════════════

ALL_STORIES = [
    {"title": S13_TITLE, "author": S13_AUTHOR, "cover": S13_COVER, "intro": S13_INTRO, "chapters": S13_CHAPTERS},
    {"title": S14_TITLE, "author": S14_AUTHOR, "cover": S14_COVER, "intro": S14_INTRO, "chapters": S14_CHAPTERS},
    {"title": S15_TITLE, "author": S15_AUTHOR, "cover": S15_COVER, "intro": S15_INTRO, "chapters": S15_CHAPTERS},
    {"title": S16_TITLE, "author": S16_AUTHOR, "cover": S16_COVER, "intro": S16_INTRO, "chapters": S16_CHAPTERS},
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
    log("🚀 BATCH 4 LIVE PUBLISH — 4 STORIES (13-16)")
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

    log(f"\n🏁 BATCH 4 COMPLETE: {len(results)}/4 published")
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
