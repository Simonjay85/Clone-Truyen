#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
write_batch_mix_03.py — Batch 3: 5 Truyện NGƯỢC / Abuse → Vươn Lên (Stories 11-15)
====================================================================================
Template B: Đau đớn → kiên cường → rực rỡ
Tone: Thương cảm, nghẹn ngào, khâm phục
Số chương random 8-13

Story 11: Con gái bị bỏ rơi → CEO may mặc (10 ch) — cover 14
Story 12: Trẻ mồ côi → nhà tâm lý học (9 ch) — cover 15
Story 13: Khuyết tật tay → nghệ sĩ piano (11 ch) — cover 16
Story 14: Bị tạt axit → người mẫu / founder mỹ phẩm (8 ch) — cover 17
Story 15: Con nhà nợ nần → vua BĐS (10 ch) — cover 18
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
# STORY 11: CON GÁI BỊ BỎ RƠI → CEO MAY MẶC — 10 CHƯƠNG (Template B: Ngược)
# ═══════════════════════════════════════════════════════════════════════════════

S11_TITLE = "BỊ MẸ BỎ RƠI Ở CỔNG CHÙA TỪ LÚC SƠ SINH, TÔI LỚN LÊN THÀNH CEO TẬP ĐOÀN MAY MẶC LỚN NHẤT ĐÔNG NAM Á"
S11_AUTHOR = "Trần Thị Ngọc"
S11_COVER = "base_cover_14.png"
S11_INTRO = """<p>Một đêm mưa tháng Mười, ai đó đặt em bé gái trong chiếc rổ tre trước cổng chùa Linh Ứng, Đà Nẵng. Không tên, không tuổi, không cha mẹ — chỉ có tấm khăn len đỏ quấn quanh và một mảnh giấy nhàu: "Xin hãy nuôi con giúp."</p>
<p>Trần Thị Ngọc — cái tên sư thầy đặt cho — lớn lên trong chùa, bị trêu chọc vì "không có nguồn gốc," bị từ chối ở mọi nơi vì "con mồ côi." Nhưng đôi bàn tay khéo léo may vá áo cho sư thầy từ năm mười tuổi đã đưa Ngọc đến đỉnh cao ngành thời trang Đông Nam Á.</p>"""

S11_CHAPTERS = [
("Chương 1: Đêm Mưa Cổng Chùa", """Sư thầy Thích Minh Đức nghe tiếng khóc lúc ba giờ sáng. Mưa xối xả, gió giật từng hồi. Thầy mở cổng chùa Linh Ứng, nhìn xuống: một chiếc rổ tre, bên trong là em bé gái đỏ hỏn, khóc ngằn ngặt, quấn trong tấm khăn len đỏ đã ướt sũng.

Mảnh giấy kẹp trong khăn, mực đã nhòe vì mưa: "Xin hãy nuôi con giúp. Con không có tội."

Sư thầy bế em bé vào, đặt tên Ngọc — "viên ngọc giữa bùn."

Ngọc lớn lên trong chùa. Bảy tuổi, theo sư thầy ra chợ mua vải vá áo cà sa cũ. Mười tuổi, tự may áo cho sư thầy — đường kim mũi chỉ thẳng tắp, sư thầy ngạc nhiên: "Con may đẹp hơn thợ chợ."

Nhưng ngoài chùa, Ngọc bị trêu chọc: "Con không có bố mẹ! Con bị bỏ rơi!" Bọn trẻ trong xóm ném đá, gọi cô là "con chùa." Ngọc chạy về ôm sư thầy khóc.

"Ngọc ơi, người ta bỏ con, nhưng Phật không bỏ. Và con không cần ai công nhận nguồn gốc — con tự tạo nguồn gốc cho mình."

Câu nói đó Ngọc khắc vào lòng — hai mươi năm sau, nó trở thành slogan của tập đoàn may mặc lớn nhất Đông Nam Á."""),

("Chương 2: Cô Giáo Lương — Ân Nhân Đầu Tiên", """Mười hai tuổi, Ngọc vào lớp 6 trường THCS Hòa Vang. Cô giáo dạy Công nghệ — Lương Thị Hạnh — phát hiện Ngọc may giỏi khi bài tập khâu vá của Ngọc đẹp nhất lớp.

"Em học may ở đâu?"

"Dạ em may áo cho sư thầy ở chùa, cô."

Cô Lương dạy Ngọc thêm: cách đọc rập, cách cắt vải đúng canh sợi, cách may bằng máy. Mỗi chiều sau giờ học, Ngọc ở lại phòng Công nghệ luyện tập.

Cô Lương còn tặng Ngọc thứ quý hơn kỹ năng: niềm tin. "Ngọc ơi, em có bàn tay vàng. Đừng để ai nói em không xứng đáng."

Cuối năm lớp 9, cô Lương gửi portfolio may vá của Ngọc cho trường dạy nghề may ở Sài Gòn — Ngọc nhận được học bổng toàn phần."""),

("Chương 3: Sài Gòn — Tia Sáng Đầu Tiên", """Mười lăm tuổi, Ngọc rời chùa Linh Ứng vào Sài Gòn học nghề. Sư thầy tiễn ở cổng chùa, tặng cô tấm khăn len đỏ — tấm khăn đêm mưa cổng chùa.

"Con giữ cái này. Để nhớ mình đi từ đâu."

Trường nghề may — ba năm. Ngọc học nhanh hơn mọi người vì cô đã may từ năm mười tuổi. Năm thứ hai, cô thắng cuộc thi thiết kế nội bộ — chiếc áo dài cải tiến từ vải tơ tằm Quảng Nam, phom dáng hiện đại nhưng giữ hồn truyền thống.

Nhưng Sài Gòn cũng tàn nhẫn. Ngọc bị bạn cùng phòng trọ ăn cắp tiền. Bị chủ xưởng may bóc lột — may gia công từ sáu giờ sáng đến mười hai giờ đêm, lương hai triệu. Bị khách hàng đánh vì giao chậm một ngày.

"Con ơi, con có muốn về chùa không?" Sư thầy gọi điện hỏi.

"Dạ không, thầy. Con chưa tạo xong nguồn gốc cho mình." """),

("Chương 4: Rào Cản — Bị Từ Chối Vì Quá Khứ", """Mười tám tuổi, Ngọc xin việc tại công ty thời trang lớn nhất Việt Nam — Ivy Moda. Phỏng vấn xuất sắc, portfolio ấn tượng. Nhưng khi HR hỏi "gia đình," Ngọc nói thật: "Em lớn lên trong chùa. Em không có gia đình."

HR nhìn cô bằng ánh mắt thương hại — loại thương hại mà Ngọc ghét nhất. "Em ơi, vị trí này cần người có background... ổn định hơn."

Ngọc bị từ chối. Không phải vì thiếu tài năng, mà vì xã hội không tin trẻ mồ côi.

Cô nộp đơn thêm mười hai công ty. Bảy cái từ chối, năm cái không trả lời.

Ngọc về phòng trọ, ngồi trước máy khâu cũ, khóc. Rồi cô lau nước mắt, bật máy khâu, và may — vì đó là thứ duy nhất không từ chối cô."""),

("Chương 5: Bước Ngoặt — Cuộc Thi Thiết Kế", """Cuộc thi Vietnam Young Fashion Designer 2015 — giải thưởng cho nhà thiết kế trẻ. Ngọc gom tiền mua vải, may bộ sưu tập năm bộ trong hai tuần — chủ đề "Roots" (Nguồn Gốc): áo dài kết hợp thổ cẩm Cơ Tu, vải lụa Hội An, và... tấm khăn len đỏ cũ.

"Bộ sưu tập của tôi kể câu chuyện của những người không có nguồn gốc — và cách họ tạo ra nguồn gốc cho mình," Ngọc thuyết trình trước ban giám khảo, giọng run nhưng mắt sáng.

Giải nhất. Trước năm trăm khán giả, Ngọc đứng trên bục, tay cầm cup, mắt tìm sư thầy trong khán phòng — thầy ngồi hàng cuối, tay lần tràng hạt, mắt ướt.

Giải thưởng kèm: học bổng du học thiết kế thời trang tại Parsons School of Design, New York."""),

("Chương 6: New York — Vươn Lên", """Bốn năm Parsons. Ngọc vừa học vừa may gia công đêm để kiếm sống. GPA 3.9 — top 5% khóa.

Bộ sưu tập tốt nghiệp: "Orphan" — áo dài hiện đại kết hợp streetwear New York, lấy cảm hứng từ trẻ mồ côi Việt Nam. Show diễn tại Parsons gây chấn động — Vogue gọi: "Trần Thị Ngọc brings Vietnamese soul to global fashion."

Nhận lời mời thực tập tại Dior, nhưng Ngọc từ chối. "Em muốn về Việt Nam. Em muốn may cho người Việt."

Quyết định điên rồ — nhưng đúng."""),

("Chương 7: Gặp Lại Mẹ", """Hai mươi ba tuổi, Ngọc về Việt Nam, mở xưởng may nhỏ ở Đà Nẵng. Một ngày, một phụ nữ trung niên đến xưởng, đứng ngoài cửa nhìn vào, mắt đỏ hoe.

"Cô tìm ai ạ?"

Người phụ nữ khóc: "Con... con là Ngọc phải không? Con chùa Linh Ứng..."

Đó là mẹ ruột — Lê Thị Hồng — người đã bỏ Ngọc ở cổng chùa hai mươi ba năm trước. Bà kể: năm đó bà mười bảy tuổi, bị gia đình chồng đuổi ra khỏi nhà vì sinh con gái, không có tiền nuôi con.

"Mẹ xin lỗi. Mẹ không có lựa chọn nào khác..."

Ngọc im lặng rất lâu. Trái tim cô đau — nhưng không phải cơn đau thù hận. Mà là cơn đau thương xót cho người mẹ mười bảy tuổi không có lựa chọn.

"Con không trách mẹ. Nhưng con cần thời gian."

Bà Hồng gật đầu, khóc, rồi ra đi. Trên bàn xưởng, tấm khăn len đỏ cũ kỹ nằm im lặng."""),

("Chương 8: Tập Đoàn NGỌC Fashion", """Xưởng may nhỏ thành NGỌC Fashion — tập đoàn may mặc chuyên sustainable fashion, sử dụng vải tự nhiên Việt Nam: tơ tằm Quảng Nam, thổ cẩm Tây Nguyên, lụa Hà Đông.

Đặc biệt: NGỌC Fashion tuyển dụng ưu tiên trẻ em mồ côi và phụ nữ đơn thân — đào tạo nghề may miễn phí, cung cấp nhà ở.

Năm năm: doanh thu hai nghìn tỷ, xuất khẩu mười hai quốc gia, ba nghìn nhân viên — trong đó năm trăm là trẻ mồ côi trưởng thành.

Forbes 30 Under 30 Asia. Fortune gọi NGỌC Fashion "the most ethical fashion brand in Southeast Asia." """),

("Chương 9: Tha Thứ Hay Không", """Một năm sau lần gặp đầu tiên, Ngọc gọi mẹ ruột đến xưởng.

"Mẹ, con đã suy nghĩ rất lâu. Con không tha thứ được — vì con không có quyền tha thứ cho nỗi đau của đứa bé bị bỏ rơi dưới mưa. Nhưng con hiểu. Và con mời mẹ đến làm việc tại NGỌC Fashion — nếu mẹ muốn."

Bà Hồng khóc: "Con cho mẹ cơ hội thật sao?"

"Con không cho mẹ cơ hội vì mẹ là mẹ. Con cho vì mẹ là một người phụ nữ cần việc làm. Ở đây, mọi người đều bình đẳng."

Bà Hồng bắt đầu làm — kiểm hàng, đóng gói. Bà không đòi hỏi đặc quyền. Và Ngọc không gọi bà là "mẹ" — chỉ gọi "cô Hồng."

Nhưng mỗi sáng, Ngọc để trên bàn làm việc của bà một ly trà nóng."""),

("Chương 10: Tấm Khăn Len Đỏ", """Show thời trang lớn nhất năm của NGỌC Fashion — "Origins" — tại Nhà hát lớn Hà Nội.

Bộ sưu tập cuối: Ngọc tự mặc chiếc áo dài trắng, thắt eo bằng tấm khăn len đỏ cũ — tấm khăn đêm mưa cổng chùa hai mươi tám năm trước.

"Đây là tấm khăn tôi được quấn khi bị bỏ rơi," Ngọc nói trước hai nghìn khán giả. "Nó là thứ duy nhất tôi có từ mẹ. Và hôm nay, tôi biến nó thành thứ đẹp nhất trên sàn diễn — vì mọi vết sẹo đều có thể trở thành nghệ thuật."

Khán phòng im lặng, rồi đứng dậy vỗ tay. Sư thầy Minh Đức — giờ tám mươi tuổi — ngồi hàng đầu, mắt nhắm, tay lần tràng hạt, mỉm cười.

Cô Hồng — mẹ ruột — đứng sau cánh gà, nhìn con gái trên sân khấu, khóc không thành tiếng.

Ngọc bước xuống sân khấu, đi thẳng đến sư thầy, quỳ xuống.

"Con cảm ơn thầy đã nhặt con lên."

"Ngọc ơi, không phải thầy nhặt con. Là con đã tự đứng dậy." """),
]

# ═══════════════════════════════════════════════════════════════════════════════
# STORY 12: TRẺ MỒ CÔI → NHÀ TÂM LÝ HỌC — 9 CHƯƠNG
# ═══════════════════════════════════════════════════════════════════════════════

S12_TITLE = "BỊ BẮT NẠT SUỐT TUỔI THƠ VÌ LÀ TRẺ MỒ CÔI, TÔI TRỞ THÀNH NHÀ TÂM LÝ HỌC CỨU HÀNG NGHÌN ĐỨA TRẺ GIỐNG MÌNH"
S12_AUTHOR = "Lê Hải Minh"
S12_COVER = "base_cover_15.png"
S12_INTRO = """<p>Lê Hải Minh mất cả bố lẫn mẹ trong tai nạn giao thông năm lên bốn. Lớn lên trong trung tâm bảo trợ xã hội, bị bắt nạt vì "không ai thương," Minh biến nỗi đau thành động lực trở thành nhà tâm lý học trẻ em hàng đầu Việt Nam — người chữa lành hàng nghìn tâm hồn nhỏ bé.</p>"""

S12_CHAPTERS = [
("Chương 1: Trung Tâm Bảo Trợ Số 3", """Trung tâm Bảo trợ Xã hội Số 3, quận Bình Thạnh, Sài Gòn — nơi Lê Hải Minh lớn lên từ năm bốn tuổi đến mười tám tuổi. Ba mươi hai đứa trẻ, sáu phòng ngủ, hai bảo mẫu quá tải. Cơm ngày hai bữa, áo quần quyên góp, dép tổ ong mòn đế.

Minh là đứa trẻ ít nói nhất trung tâm. Cậu không khóc — vì bảo mẫu nói: "Khóc không ai nghe đâu, nín đi." Cậu không kể chuyện bố mẹ — vì bọn trẻ lớn hơn trêu: "Mày không có bố mẹ, mày là đồ bỏ đi!"

Mỗi đêm, Minh nằm trên giường tầng trên, ôm chiếc gối mỏng dính, và tưởng tượng mẹ đang ngồi bên hát ru. Cậu không nhớ mặt mẹ — chỉ nhớ mùi nước hoa nhài mà bảo mẫu nói "giống mùi của mẹ cháu."

Mỗi sáng thức dậy, mùi nhài bay mất. Minh biết: cậu phải tự mình đi qua."""),

("Chương 2: Cô Tâm — Ánh Sáng Giữa Bóng Tối", """Năm Minh mười tuổi, trung tâm nhận tình nguyện viên mới: Nguyễn Thị Tâm, sinh viên năm ba khoa Tâm lý, Đại học Sư phạm.

Cô Tâm không giống bảo mẫu — cô ngồi xuống ngang tầm mắt trẻ con, lắng nghe, và không bao giờ nói "nín đi." Cô hỏi: "Em buồn à? Kể cho chị nghe."

Minh không kể. Hai tuần liền, cô Tâm đến, ngồi cạnh Minh, im lặng đọc sách. Không ép, không hỏi. Chỉ ngồi cạnh.

Tuần thứ ba, Minh lên tiếng: "Chị ơi, em mơ thấy mẹ mà không nhớ mặt mẹ. Em buồn."

Cô Tâm ôm Minh: "Buồn là đúng rồi. Buồn chứng tỏ em yêu mẹ."

Câu nói đó — "buồn chứng tỏ em yêu" — thay đổi mọi thứ. Lần đầu tiên, Minh hiểu: nỗi đau không phải yếu đuối, mà là bằng chứng của tình yêu."""),

("Chương 3: Học Tâm Lý Vì Muốn Chữa Lành", """Mười tám tuổi, Minh rời trung tâm bảo trợ. Không tiền, không người thân, không nhà. Nhưng có một mục tiêu rõ ràng: học tâm lý học — vì cô Tâm đã chữa lành cậu, và cậu muốn chữa lành những đứa trẻ khác.

Thi đỗ Đại học Khoa học Xã hội và Nhân văn, khoa Tâm lý — học bổng toàn phần dành cho trẻ mồ côi. Bốn năm đại học, Minh vừa học vừa làm — phục vụ quán cà phê ban đêm, gia sư ban ngày.

GPA 3.8. Luận văn tốt nghiệp: "Tác động tâm lý dài hạn của việc bắt nạt lên trẻ em mồ côi tại Việt Nam" — dựa trên chính trải nghiệm bản thân. Luận văn đạt điểm tuyệt đối, được đăng trên tạp chí Tâm lý học Việt Nam."""),

("Chương 4: Phòng Tham Vấn Đầu Tiên — Cũng Là Phòng Ngủ", """Sau khi tốt nghiệp, Minh mở phòng tham vấn tâm lý trẻ em — trong chính phòng trọ mười lăm mét vuông. Bàn tham vấn là bàn ăn, ghế tham vấn là ghế nhựa, và "phòng chờ" là hành lang ngoài cửa.

Khách hàng đầu tiên: một bé gái mười hai tuổi bị bắt nạt ở trường. Mẹ bé dẫn đến, khóc: "Cháu không chịu đi học nữa."

Minh ngồi xuống ngang tầm mắt bé — giống hệt cách cô Tâm đã ngồi với cậu. "Em buồn à? Kể cho anh nghe."

Bé kể. Minh lắng nghe. Không phán xét, không giải pháp vội — chỉ lắng nghe. Và bé bắt đầu khóc — lần đầu tiên sau ba tháng giữ trong lòng.

"Khóc đi em. Khóc chứng tỏ em dũng cảm." """),

("Chương 5: Bước Ngoặt — TED Talk Viral", """Minh được mời nói chuyện tại TEDxSaigon — chủ đề "Đứa Trẻ Không Ai Thương."

"Tôi lớn lên trong trung tâm bảo trợ. Tôi bị gọi là 'đồ bỏ đi.' Nhưng tôi không bỏ đi — tôi đi tới. Và hôm nay tôi đứng đây để nói với mọi đứa trẻ bị bỏ rơi: các em không phải đồ bỏ. Các em là viên ngọc chưa được mài."

Video TED đạt mười lăm triệu lượt xem. Phụ huynh khắp Việt Nam gọi đến đặt lịch. Phòng tham vấn trong phòng trọ quá tải."""),

("Chương 6: Trung Tâm Chữa Lành — MinhTâm Center", """Minh mở MinhTâm Center — trung tâm tâm lý trẻ em chuyên nghiệp. "Minh" từ tên mình, "Tâm" từ tên cô Tâm — ân nhân.

Năm trăm trẻ em mỗi năm được tham vấn miễn phí — trẻ mồ côi, trẻ bị bắt nạt, trẻ bị bạo lực gia đình. Đội ngũ: mười hai chuyên gia tâm lý, tất cả đều từng có tuổi thơ khó khăn.

UNICEF Việt Nam tài trợ. Bộ Lao động — Thương binh — Xã hội đưa MinhTâm vào mô hình mẫu quốc gia."""),

("Chương 7: Gặp Lại Những Đứa Trẻ Bắt Nạt Mình", """Một ngày, Minh nhận email từ Hoàng — đứa trẻ lớn nhất ở trung tâm bảo trợ ngày xưa, người trêu Minh là "đồ bỏ đi."

"Minh à, tao xin lỗi. Hồi đó tao cũng đau — tao cũng mồ côi, tao cũng sợ. Tao trêu mày vì... tao không biết cách xử lý nỗi đau của mình."

Minh gọi lại Hoàng, nói chuyện hai tiếng đồng hồ. Không trách móc, không thù hận — chỉ hai đứa trẻ mồ côi lớn lên, hiểu nhau hơn sau hai mươi năm.

"Tao tha thứ cho mày rồi, Hoàng. Vì tao hiểu: mày cũng là nạn nhân."

Hoàng khóc qua điện thoại."""),

("Chương 8: Cuốn Sách Và Lọ Nước Hoa Nhài", """Minh viết sách: "Đứa Trẻ Tự Chữa Lành" — bestseller, ba trăm nghìn bản. Tất cả lợi nhuận quyên góp cho trẻ em mồ côi.

Cô Tâm — giờ đã là PGS Tâm lý học — viết lời tựa: "Minh là đứa trẻ im lặng nhất tôi từng gặp. Và giờ, tiếng nói của em vang vọng nhất."

Minh đặt lọ nước hoa nhài trên bàn làm việc — mùi hương mẹ. Không phải vì nhớ mẹ — mà vì muốn nhắc mình: mỗi đứa trẻ đến MinhTâm đều cần được yêu thương, như cậu bé bốn tuổi tưởng tượng mẹ hát ru mỗi đêm."""),

("Chương 9: Quay Về Trung Tâm Bảo Trợ Số 3", """Minh quay về Trung tâm Bảo trợ Số 3 — nơi cậu lớn lên. Trung tâm giờ đã sửa chữa, sạch sẽ hơn, nhưng vẫn ba mươi đứa trẻ, vẫn sáu phòng ngủ, vẫn đôi mắt buồn.

Minh ngồi xuống giữa bọn trẻ, lấy cuốn sách ra đọc cho các em nghe — giống hệt cách cô Tâm đã ngồi cạnh cậu hai mươi năm trước. Không ép, không hỏi. Chỉ ngồi cạnh.

Một bé trai sáu tuổi bò lên ngồi vào lòng Minh: "Anh ơi, anh có nhà không?"

"Anh không có nhà khi còn nhỏ. Nhưng bây giờ anh có rồi."

"Nhà anh ở đâu?"

Minh mỉm cười, nhìn quanh phòng — ba mươi đứa trẻ mồ côi, đôi mắt trong veo.

"Nhà anh ở đây. Ở chỗ các em." """),
]

# ═══════════════════════════════════════════════════════════════════════════════
# STORY 13: KHUYẾT TẬT TAY → NGHỆ SĨ PIANO — 11 CHƯƠNG
# ═══════════════════════════════════════════════════════════════════════════════

S13_TITLE = "MẤT BA NGÓN TAY PHẢI TRONG TAI NẠN, TÔI TRỞ THÀNH NGHỆ SĨ PIANO KHIẾN CẢ VIENNA ĐỨNG DẬY VỖ TAY"
S13_AUTHOR = "Đặng Quang Huy"
S13_COVER = "base_cover_16.png"
S13_INTRO = """<p>Đặng Quang Huy, thần đồng piano mười hai tuổi, mất ba ngón tay phải (ngón trỏ, giữa, áp út) trong tai nạn máy xay lúa ở quê. Bác sĩ nói: "Cháu không bao giờ chơi piano được nữa." Mười năm sau, Huy đứng trên sân khấu Musikverein Vienna — thánh đường âm nhạc cổ điển — chơi Chopin bằng bảy ngón tay.</p>"""

S13_CHAPTERS = [
("Chương 1: Bảy Ngón Tay", """Tai nạn xảy ra vào mùa gặt, khi Huy mười hai tuổi. Cậu phụ bà ngoại cho lúa vào máy xay — tay phải bị cuốn vào trục quay. Ba ngón tay — trỏ, giữa, áp út — bị cắt đứt.

Bà ngoại ôm cháu chạy ba cây số đến trạm y tế xã, máu thấm đỏ ướt áo bà. Xe cứu thương chở Huy lên bệnh viện tỉnh — nhưng quá muộn để nối lại.

Mười hai tuổi, Huy đã chơi piano năm năm — thần đồng của huyện Lý Nhân, Hà Nam. Cậu thắng mọi cuộc thi piano cấp tỉnh, đang chuẩn bị thi quốc gia.

Giờ cậu nhìn bàn tay phải — hai ngón còn lại: ngón cái và ngón út. Bảy ngón tay tổng cộng.

"Bác sĩ nói cháu không chơi piano được nữa," mẹ Huy khóc.

Huy im lặng nhìn bàn tay. Rồi cậu nói, giọng run: "Con không tin." """),

("Chương 2: Thầy Tuấn — Người Không Bỏ Cuộc", """Thầy Nguyễn Văn Tuấn — giáo viên piano duy nhất ở thị trấn — là người đầu tiên nói với Huy: "Con vẫn có thể chơi."

Thầy Tuấn không phải nghệ sĩ nổi tiếng — chỉ là thầy dạy piano ở nhà văn hóa huyện, lương ba triệu. Nhưng thầy đọc mọi tài liệu về pianists khuyết tật: Paul Wittgenstein — nghệ sĩ Áo mất cánh tay phải trong Thế chiến I, vẫn chơi piano một tay; Nicholas McCarthy — sinh ra không có tay phải, tốt nghiệp Royal Academy of Music London.

"Con ơi, người ta mất cả cánh tay mà vẫn chơi. Con còn bảy ngón — nhiều hơn rất nhiều rồi."

Thầy Tuấn thiết kế bài tập riêng: tay trái đảm nhận nhiều nốt hơn, hai ngón tay phải còn lại (cái và út) tập kéo dãn biên độ rộng nhất có thể. Mỗi ngày bốn giờ tập — đau, mỏi, chảy máu vết sẹo — nhưng không dừng."""),

("Chương 3: Đau Và Kiên Nhẫn", """Hai năm đầu sau tai nạn: Huy chỉ chơi được những bản đơn giản. Tay phải yếu, hai ngón không đủ bao phủ phím. Bạn bè trêu: "Thằng cụt đàn piano! Ha ha ha!"

Huy khóc mỗi đêm, nhưng sáng vẫn dậy tập. Bà ngoại — người tự trách mình vì tai nạn — ngồi bên cạnh, quạt cho Huy mỗi buổi tập mùa hè.

"Bà ơi, con đau tay quá."

"Đau thì nghỉ một lát rồi tập tiếp. Bà ngồi đây với con."

Năm thứ ba: breakthrough. Huy phát triển kỹ thuật chơi riêng — "floating right hand" — hai ngón phải di chuyển liên tục, nhảy qua nhảy lại giữa các phím, tạo hiệu ứng legato mà người nghe không nhận ra chỉ có hai ngón."""),

("Chương 4: Cuộc Thi Piano Quốc Gia — Bị Từ Chối", """Huy đăng ký thi Piano Quốc gia năm mười bảy tuổi. Ban tổ chức từ chối: "Thí sinh phải có đủ mười ngón tay. Quy chế không cho phép ngoại lệ."

Thầy Tuấn gửi thư khiếu nại: "Quy chế đánh giá trình độ, không đánh giá số ngón tay." Ban tổ chức im lặng.

Huy quay video chơi Chopin Ballade No. 1 — bản nhạc khó bậc nhất trong repertoire piano — và đăng YouTube. Video đạt năm triệu lượt xem. Comments: "Đây là bằng chứng rằng talent không cần đủ mười ngón."

Ban tổ chức chịu áp lực dư luận, cuối cùng cho phép Huy dự thi."""),

("Chương 5: Bước Ngoặt — Giải Nhì Piano Quốc Gia", """Huy thi — bản Chopin Ballade No. 1, bốn phút mười hai giây. Ban giám khảo sáu người, bốn người khóc khi nghe.

Giải nhì. Giải nhất thuộc về một cậu trai mười ngón tay, kỹ thuật hoàn hảo. Nhưng giám khảo trưởng nói riêng với Huy: "Em chơi bằng trái tim. Cậu kia chơi bằng mười ngón."

Giải nhì, nhưng video buổi thi đạt hai mươi triệu lượt xem — gấp mười lần giải nhất."""),

("Chương 6: Du Học Vienna", """Nhờ video viral, Huy nhận học bổng toàn phần tại University of Music and Performing Arts Vienna — trường âm nhạc hàng đầu thế giới.

Bốn năm Vienna. Huy vừa học vừa biểu diễn tại các nhà thờ, phòng hòa nhạc nhỏ. Kỹ thuật "floating right hand" được giáo sư Vienna gọi là "Huy Technique" — kỹ thuật mới trong lịch sử piano.

"Anh ấy không chơi bằng bảy ngón — anh ấy chơi bằng bảy ngón và một trái tim," giáo sư hướng dẫn viết trong recommendation letter."""),

("Chương 7: Bà Ngoại Và Chiếc Quạt Mo", """Giữa Vienna lạnh giá, Huy nhận tin: bà ngoại mất.

Bà mất trong giấc ngủ, tay ôm chiếc quạt mo — chiếc quạt bà hay quạt cho Huy mỗi buổi tập piano mùa hè.

Huy bay về Việt Nam, quỳ trước bàn thờ bà, chơi bản nhạc bà yêu nhất — "Bà Ơi" — trên chiếc piano cũ ở nhà văn hóa huyện, nơi Huy học chơi lần đầu.

Bảy ngón tay trên phím, nước mắt trên má, và tiếng piano vang trong căn phòng nhỏ — nơi bà từng ngồi quạt cho cháu."""),

("Chương 8: Đối Mặt Quá Khứ — Trở Về Cánh Đồng", """Huy về thăm cánh đồng nơi tai nạn xảy ra. Chiếc máy xay lúa cũ vẫn nằm đó — rỉ sét, bỏ hoang.

Huy đứng trước máy, nhìn bàn tay phải — hai ngón. Nhớ lại mùi máu, tiếng bà kêu thét, tiếng xe cứu thương xa xa.

Rồi anh mỉm cười — nụ cười nhẹ, buồn nhưng bình yên.

"Mày lấy ba ngón tay của tao. Nhưng tao giữ bảy ngón và cả thế giới."

Anh quay lưng, bước đi khỏi cánh đồng. Không oán hận. Không nhìn lại."""),

("Chương 9: Đỉnh Cao — Musikverein Vienna", """Musikverein Vienna — Sảnh Vàng — thánh đường âm nhạc cổ điển, nơi Beethoven, Brahms, Mahler đã biểu diễn. Huy được mời chơi solo recital — nghệ sĩ Việt Nam đầu tiên.

Chương trình: toàn bộ Chopin. Ballade No. 1, Nocturne Op. 9 No. 2, Polonaise "Heroic."

Hai nghìn khán giả. Huy ngồi trước cây Bösendorfer Imperial — cây piano hai trăm nghìn đô — và đặt bảy ngón tay lên phím.

Khi bản Ballade kết thúc, Sảnh Vàng im lặng ba giây — rồi bùng nổ. Standing ovation. Hai nghìn người đứng dậy vỗ tay năm phút không dừng."""),

("Chương 10: Thầy Tuấn Ngồi Hàng Ghế Cuối", """Huy mời thầy Tuấn sang Vienna dự concert. Thầy — giáo viên piano huyện Lý Nhân, lương ba triệu — lần đầu ra nước ngoài, lần đầu ngồi trong Musikverein.

Thầy ngồi hàng ghế cuối cùng, mắt đỏ hoe, tay ôm chương trình biểu diễn có ảnh Huy trên bìa.

Sau concert, Huy chạy ra, ôm thầy.

"Thầy ơi, không có thầy thì không có con trên sân khấu này."

"Thầy không dạy con giỏi. Con tự giỏi. Thầy chỉ không bỏ con." """),

("Chương 11: Quay Về Nhà Văn Hóa Huyện", """Huy về Lý Nhân, mở lớp dạy piano miễn phí cho trẻ em nông thôn — tại nhà văn hóa huyện, nơi Huy học chơi lần đầu.

Chiếc piano cũ vẫn đứng đó — phím vàng ố, đàn hơi lệch tông. Huy ngồi xuống, chơi một bản nhạc ngắn cho bọn trẻ nghe.

Một bé gái bảy tuổi, mắt tròn xoe, chạy đến sờ bàn tay phải Huy: "Anh ơi, sao tay anh thiếu ngón?"

"Vì anh bị tai nạn."

"Anh vẫn đàn hay thế, sao tay thiếu ngón mà vẫn đàn được?"

Huy cười: "Vì âm nhạc không ở trong ngón tay, em ơi. Nó ở trong đây." Anh chỉ vào ngực.

Bé gái gật đầu, leo lên ghế, đặt mười ngón tay nhỏ xíu lên phím piano. Huy ngồi bên cạnh, hướng dẫn — giống hệt thầy Tuấn hai mươi năm trước.

Tiếng piano vang lên trong nhà văn hóa huyện Lý Nhân — vụng về, lệch nhịp, nhưng đẹp. Đẹp như mọi khởi đầu."""),
]

# ═══════════════════════════════════════════════════════════════════════════════
# STORY 14: BỊ TẠT AXIT → NGƯỜI MẪU / FOUNDER MỸ PHẨM — 8 CHƯƠNG
# ═══════════════════════════════════════════════════════════════════════════════

S14_TITLE = "BỊ TẠT AXIT VÌ TỪ CHỐI TÌNH CẢM, TÔI TRỞ THÀNH NGƯỜI MẪU VÀ FOUNDER MỸ PHẨM CHO NGƯỜI CÓ SẸO"
S14_AUTHOR = "Nguyễn Hạ Vy"
S14_COVER = "base_cover_17.png"
S14_INTRO = """<p>Hai mươi tuổi, Nguyễn Hạ Vy — sinh viên năm hai Đại học Mỹ thuật — bị người theo đuổi tạt axit vì từ chối tình cảm. Nửa mặt phải bị bỏng, sẹo lồi chạy từ trán xuống cổ. Bác sĩ nói sẹo sẽ theo cô suốt đời.</p>
<p>Vy không giấu sẹo. Cô biến nó thành nghệ thuật — trở thành người mẫu đầu tiên tại Việt Nam dùng sẹo như một phần bản sắc, và sáng lập thương hiệu mỹ phẩm dành cho người có sẹo.</p>"""

S14_CHAPTERS = [
("Chương 1: Đêm Axit", """Mười giờ đêm, con hẻm nhỏ sau ký túc xá Đại học Mỹ thuật. Hạ Vy đang đi bộ về phòng trọ sau buổi học vẽ muộn. Túi đựng bảng vẽ trên vai, tai nghe nhạc, không để ý bóng người phía sau.

Một bàn tay ném thứ gì đó vào mặt cô. Nóng. Đau. Cháy.

Axit. Hydrochloric acid nồng độ cao.

Vy la hét, ngã xuống đất, tay bám vào mặt — da rộp lên, mùi thịt cháy. Người đi đường chạy đến, dội nước, gọi cấp cứu.

Kẻ tạt axit: Trần Đình Quân — sinh viên cùng trường, theo đuổi Vy sáu tháng, bị từ chối ba lần. "Tao không có được mày thì không ai được," hắn nói trước khi bỏ chạy.

Hắn bị bắt ba giờ sau.

Vy nằm trong phòng cấp cứu, nửa mặt phải băng kín, đau đến mức thuốc giảm đau không tác dụng. Bác sĩ nói: "Bỏng độ 2-3, sẹo vĩnh viễn. Phẫu thuật thẩm mỹ có thể giảm nhưng không xóa hoàn toàn."

Mẹ Vy ôm con khóc suốt đêm. Vy không khóc. Cô nhìn lên trần bệnh viện, mắt trái — mắt còn nguyên — mở to, khô rang."""),

("Chương 2: Gương — Đối Mặt Với Sẹo", """Hai tháng sau, Vy ra viện. Bước đầu tiên: đứng trước gương.

Nửa mặt trái — đẹp như trước: da trắng, mắt sáng, má hồng. Nửa mặt phải — sẹo: da đỏ bầm, lồi lõm, kéo từ trán xuống cổ, mí mắt phải hơi xệ.

Vy nhìn gương mười phút. Rồi cô lấy bút vẽ — bút vẽ cô dùng ở trường Mỹ thuật — và vẽ lên sẹo. Hoa. Hoa sen. Hoa đào. Hoa mai.

"Nếu sẹo là vĩnh viễn, tôi sẽ biến nó thành bức tranh," cô nói với mẹ.

Mẹ khóc. Vy lau nước mắt cho mẹ bằng bàn tay vẫn còn vết bỏng."""),

("Chương 3: Quay Lại Trường — Không Giấu Sẹo", """Ba tháng sau tai nạn, Vy quay lại Đại học Mỹ thuật. Không khẩu trang, không che sẹo. Đi thẳng lưng, mặt ngẩng cao.

Bạn bè nhìn, có người thương, có người tránh. Một bạn thì thầm: "Tội nghiệp, đẹp thế mà giờ..."

Vy nghe thấy. Cô quay lại: "Giờ sao? Giờ tôi có thêm một câu chuyện để kể."

Giảng viên hội họa — thầy Nguyễn Văn Khánh — mời Vy vẽ bộ tranh tự họa. "Em vẽ chính mình — cả hai nửa mặt. Đó sẽ là tác phẩm mạnh nhất lớp."

Bộ tranh tự họa "Hai Nửa" — năm bức — trở thành triển lãm tốt nghiệp của Vy, và viral trên mạng xã hội."""),

("Chương 4: Từ Họa Sĩ Đến Người Mẫu — Bước Ngoặt Lớn Nhất", """Nhiếp ảnh gia Lê Hạ Vi (trùng tên) — chuyên gia chân dung nổi tiếng — liên hệ Vy sau khi xem triển lãm "Hai Nửa": "Chị muốn chụp em — không retouch, không giấu sẹo. Bộ ảnh tên 'Scars Are Beautiful.'"

Bộ ảnh đăng trên Vogue Vietnam — lần đầu tiên tạp chí thời trang Việt Nam đăng người mẫu có sẹo trên bìa.

Một triệu lượt xem trong ngày đầu. Comments: "Đây là bìa tạp chí đẹp nhất tôi từng thấy." Nhưng cũng có: "Kinh quá, sao lại đưa mặt sẹo lên bìa?"

Vy đọc cả hai loại comment, mỉm cười, rồi nói: "Cảm ơn cả người khen lẫn người chê. Các bạn đều đang nhìn thấy tôi — và đó là đủ." """),

("Chương 5: Thương Hiệu ScarBeauty Ra Đời", """Vy phát hiện: trên thị trường mỹ phẩm Việt Nam, không có sản phẩm nào thiết kế riêng cho người có sẹo. Kem che sẹo thì có, nhưng kem dưỡng da sẹo, make-up cho da sẹo — không.

Cô sáng lập "ScarBeauty" — thương hiệu mỹ phẩm đầu tiên tại Việt Nam dành cho người có sẹo: kem dưỡng phục hồi da sẹo, primer cho da không đều, và palette màu thiết kế cho tông da sẹo.

"Tôi không giấu sẹo. Tôi chăm sóc sẹo," Vy nói trong buổi ra mắt.

ScarBeauty bán online — sold out trong tuần đầu. Không chỉ người có sẹo mua — mà cả người bình thường, vì công thức dưỡng da tốt cho mọi loại da."""),

("Chương 6: Kẻ Tạt Axit Gửi Thư Từ Tù", """Quân — kẻ tạt axit — gửi thư cho Vy từ trong tù: "Vy, tao xin lỗi. Tao đã hủy hoại cuộc đời mày. Tao xứng đáng ở đây."

Vy đọc thư, im lặng lâu. Cô không trả lời. Cô không tha thứ — không phải vì thù hận, mà vì cô biết: tha thứ không phải nghĩa vụ. Nạn nhân không nợ kẻ gây hại sự tha thứ.

"Tôi không tha thứ và cũng không thù hận. Tôi chỉ sống tiếp — tốt hơn anh ta tưởng tượng. Đó là câu trả lời duy nhất tôi có," Vy viết trong nhật ký."""),

("Chương 7: New York Fashion Week", """ScarBeauty được mời tham gia New York Fashion Week — show riêng, người mẫu đều là phụ nữ có sẹo: sẹo bỏng, sẹo phẫu thuật, sẹo tai nạn.

Vy đi cuối — chiếc áo dài trắng, nửa mặt sẹo không che, tóc búi cao. Sàn catwalk im lặng khi cô bước ra — rồi vỡ òa trong tiếng vỗ tay.

The New York Times: "ScarBeauty redefines beauty — scars included."

Vogue US: "Nguyễn Hạ Vy is the face beauty industry needed but didn't know it." """),

("Chương 8: Quay Về Con Hẻm", """Vy quay về con hẻm sau ký túc xá — nơi cô bị tạt axit năm năm trước. Hẻm vẫn vậy: tối, hẹp, đèn vàng leo lét.

Cô đứng đúng chỗ cũ. Nhớ lại cảm giác nóng rát, mùi thịt cháy, tiếng la hét của chính mình.

Rồi cô mỉm cười — nụ cười lệch, vì sẹo kéo mép phải hơi cứng. Nhưng nó đẹp — đẹp theo cách riêng, đẹp vì nó thật.

"Tôi bị tạt axit ở đây. Và tôi đã đứng dậy từ đây."

Vy bước đi khỏi con hẻm, lần này không có tai nghe, không có nhạc — chỉ có tiếng bước chân của cô vang trên mặt đường, tự tin và rõ ràng.

Trên mặt cô, sẹo vẫn ở đó — vĩnh viễn. Và Vy không muốn xóa nó nữa. Vì sẹo là một phần của cô — phần đã đưa cô đến đây."""),
]

# ═══════════════════════════════════════════════════════════════════════════════
# STORY 15: CON NHÀ NỢ NẦN → VUA BĐS — 10 CHƯƠNG
# ═══════════════════════════════════════════════════════════════════════════════

S15_TITLE = "BỐ MẸ NỢ HAI TỶ PHÁ SẢN, TÔI TỪ CẬU BÉ BỊ XIẾT NỢ THÀNH ÔNG TRÙM BẤT ĐỘNG SẢN MIỀN TÂY"
S15_AUTHOR = "Bùi Đức Thịnh"
S15_COVER = "base_cover_18.png"
S15_INTRO = """<p>Năm Bùi Đức Thịnh mười bốn tuổi, chủ nợ đến nhà đập phá, lấy đi mọi thứ — tivi, tủ lạnh, xe máy, cả bàn thờ ông bà. Bố mẹ nợ hai tỷ đồng vì kinh doanh thất bại, gia đình bị đẩy ra đường.</p>
<p>Từ cậu bé mười bốn tuổi ngủ dưới gầm cầu, Thịnh vươn lên thành ông trùm bất động sản miền Tây — nhưng anh xây nhà cho người nghèo, không phải biệt thự cho đại gia.</p>"""

S15_CHAPTERS = [
("Chương 1: Đêm Xiết Nợ", """Mười giờ đêm, cánh cửa nhà bị đạp tung. Năm người đàn ông — da mặt đen sạm, tay cầm búa — xông vào nhà Bùi Đức Thịnh ở huyện Châu Thành, Tiền Giang.

"Bùi Văn Tài! Nợ hai tỷ! Không trả thì lấy nhà!" Kẻ cầm đầu hét.

Bố Thịnh — ông Bùi Văn Tài, chủ vựa trái cây vỡ nợ — quỳ xuống: "Xin cho tôi thêm thời gian..."

Họ không nghe. Tivi bị kéo đi. Tủ lạnh bị khiêng ra. Xe máy bị dắt. Thậm chí bàn thờ ông bà — bộ lư đồng — cũng bị giật khỏi tay mẹ Thịnh.

Mẹ Thịnh ôm bàn thờ khóc: "Cái này là thờ cúng tổ tiên, đừng lấy!"

Kẻ xiết nợ giật mạnh: "Tổ tiên mày nợ tiền tao!"

Thịnh — mười bốn tuổi — đứng góc phòng, ôm em gái sáu tuổi, hai tay bịt tai em bé để em không nghe tiếng mẹ khóc. Nhưng chính Thịnh nghe — và âm thanh đó anh nhớ suốt hai mươi năm."""),

("Chương 2: Gầm Cầu Và Ổ Bánh Mì Đầu Tiên", """Gia đình bị đuổi khỏi nhà. Bố mẹ dẫn Thịnh và em gái đến gầm cầu Mỹ Thuận — nơi những gia đình vỡ nợ miền Tây tá túc.

Ba tháng sống dưới gầm cầu. Ăn cơm từ thiện, ngủ trên bìa carton. Mẹ giặt đồ thuê kiếm ba mươi nghìn/ngày. Bố trầm cảm, nằm im suốt ngày.

Thịnh bỏ học, xin phụ bán bánh mì ở vỉa hè chợ Mỹ Tho — bốn giờ sáng dậy, nhồi bột, bán đến trưa, kiếm năm mươi nghìn/ngày. Không đủ ăn — nhưng đủ để mua sữa cho em gái.

"Con ơi, ba xin lỗi." Bố nói mỗi đêm.

"Ba đừng xin lỗi. Ba hãy đứng dậy," Thịnh trả lời — giọng một đứa trẻ mười bốn tuổi nhưng mắt một người lớn."""),

("Chương 3: Chú Năm — Ân Nhân Của Cậu Bé Bánh Mì", """Chú Năm — Nguyễn Văn Năm — chủ sạp vải ở chợ Mỹ Tho, người mua bánh mì của Thịnh mỗi sáng.

"Mày thức dậy sớm, chịu khó, nhanh nhẹn. Muốn phụ tao bán vải buổi chiều không?"

Thịnh nhận. Từ bán bánh mì sáng chuyển sang phụ bán vải chiều. Chú Năm dạy Thịnh đọc thị trường: vải nào bán chạy mùa nào, giá nhập bao nhiêu, lời lãi ra sao.

"Buôn bán không khó. Khó là biết giữ tiền và đừng tham."

Câu nói đó Thịnh khắc vào xương — vì bố anh tham, vay nợ đầu tư quá tay, và gia đình trả giá."""),

("Chương 4: Từ Vải Đến Đất — Phát Hiện Đam Mê", """Mười tám tuổi, Thịnh tiết kiệm được hai trăm triệu từ bán vải (bốn năm không tiêu gì). Anh dùng tiền mua miếng đất ruộng bỏ hoang ở ngoại ô Mỹ Tho — năm trăm mét vuông, giá rẻ vì ngập nước.

Người ta cười: "Thằng nhỏ mua đất ruộng ngập! Đồ điên!"

Thịnh không điên. Anh đã quan sát: Mỹ Tho đang mở rộng đô thị về phía đông — đúng hướng miếng đất. Hai năm sau, tỉnh phê duyệt quy hoạch đường mới đi qua khu đó — đất tăng giá gấp năm.

Thịnh bán, lời tám trăm triệu. Anh dùng tiền trả nợ cho bố mẹ — không phải hai tỷ, nhưng đủ để chủ nợ ngừng đe dọa."""),

("Chương 5: Bùi Đức Thịnh BĐS — Xây Nhà Cho Người Nghèo", """Thịnh lập công ty BĐS — nhưng không phải BĐS luxury. "Bùi Đức Thịnh BĐS" chuyên xây nhà ở xã hội — căn hộ giá rẻ cho công nhân, người thu nhập thấp, và đặc biệt: gia đình vỡ nợ bị mất nhà.

"Tôi từng ngủ dưới gầm cầu. Tôi biết cảm giác không có nhà. Nên tôi xây nhà — cho những người giống gia đình tôi ngày xưa."

Dự án đầu tiên: khu nhà ở xã hội năm trăm căn ở Long An — giá 300 triệu/căn, trả góp hai mươi năm. Sold out trong một tháng."""),

("Chương 6: Đế Chế Miền Tây", """Mười năm, Thịnh xây mười khu nhà ở xã hội trên khắp miền Tây — Tiền Giang, Long An, Bến Tre, Cần Thơ. Tổng cộng năm nghìn căn hộ, năm nghìn gia đình có nhà.

Doanh thu công ty: ba nghìn tỷ/năm. Thịnh là ông trùm BĐS miền Tây — nhưng không ai gọi anh là "đại gia." Người ta gọi anh là "anh Thịnh nhà xã hội."

Forbes Vietnam: "Bùi Đức Thịnh — tỷ phú xây nhà cho người nghèo." """),

("Chương 7: Bố Và Bàn Thờ Mới", """Ngày khánh thành dự án thứ mười, Thịnh mời bố mẹ đến. Trong căn hộ mẫu, Thịnh đặt sẵn một thứ: bộ lư đồng mới — giống hệt bộ bị chủ nợ giật năm xưa.

"Bố mẹ ơi, con mua bàn thờ mới rồi. Không ai giật được nữa."

Bố Thịnh đứng trước bàn thờ, tay run, mắt ướt. Ông thắp nhang, cúi đầu lạy tổ tiên — lần đầu tiên sau mười năm.

"Con ơi, ba... ba cảm ơn con."

"Ba đừng cảm ơn con. Ba hãy tha thứ cho chính mình." """),

("Chương 8: Từ Chối Hay Đối Mặt Quá Khứ", """Một ngày, kẻ cầm đầu nhóm xiết nợ năm xưa — Nguyễn Văn Hiệp — đến văn phòng Thịnh, xin mua nhà ở xã hội cho gia đình.

Hiệp không nhận ra Thịnh — nhưng Thịnh nhận ra Hiệp ngay lập tức. Khuôn mặt đen sạm, giọng nói hách dịch — giờ đã già, gầy, nhưng vẫn giọng đó.

Thịnh nhìn Hiệp mười giây.

Rồi anh ký duyệt đơn mua nhà: "Anh đủ điều kiện. Nhà sẽ giao sau sáu tháng."

Hiệp cảm ơn, ra về. Không biết anh ta vừa nhận nhà từ tay đứa trẻ mà anh ta từng đẩy ra đường.

Thư ký hỏi: "Anh biết ông đó là ai phải không?"

"Biết. Nhưng nhà tôi xây cho người cần, không phải cho người tôi thích." """),

("Chương 9: Em Gái Và Ly Sữa", """Em gái Thịnh — Bùi Thị Mai, hai mươi bốn tuổi — giờ là kế toán trưởng công ty anh. Mai không nhớ đêm xiết nợ — lúc đó em mới sáu tuổi. Nhưng Mai nhớ: "Anh Hai bịt tai em, ôm em chạy ra hẻm."

"Anh ơi, hồi đó anh sợ không?"

"Sợ. Nhưng anh sợ em nghe tiếng mẹ khóc hơn anh sợ cho mình."

Mai im lặng, rồi pha ly sữa nóng đặt trước mặt anh — giống hệt ly sữa Thịnh mua cho em bằng tiền bán bánh mì năm mười bốn tuổi."""),

("Chương 10: Quay Về Gầm Cầu Mỹ Thuận", """Thịnh lái xe đến gầm cầu Mỹ Thuận — nơi gia đình từng sống ba tháng. Gầm cầu giờ đã được rào chắn, không ai ở nữa.

Thịnh đứng nhìn. Nhớ lại mùi bùn, tiếng xe tải rung cầu mỗi đêm, tiếng mẹ khóc thầm.

Rồi anh rút điện thoại, gọi cho kiến trúc sư: "Anh thiết kế giúp tôi một khu nhà tình thương ở gần đây — cho hai mươi gia đình vỡ nợ. Miễn phí. Tôi tài trợ."

"Dạ anh, kinh phí ước tính..."

"Bao nhiêu cũng được. Đừng để đứa trẻ nào phải ngủ dưới gầm cầu."

Thịnh cúp máy, nhìn gầm cầu lần cuối, rồi lên xe.

Trong gương chiếu hậu, gầm cầu Mỹ Thuận nhỏ dần, xa dần — nhưng ký ức thì không bao giờ xa.

Thịnh mỉm cười, nhấn ga, chạy về phía công trình mới — nơi hai mươi gia đình sắp có nhà."""),
]

# ═══════════════════════════════════════════════════════════════════════════════
# ASSEMBLY & PUBLISHING
# ═══════════════════════════════════════════════════════════════════════════════

ALL_STORIES = [
    {"title": S11_TITLE, "author": S11_AUTHOR, "cover": S11_COVER, "intro": S11_INTRO, "chapters": S11_CHAPTERS, "genre": "Ngược"},
    {"title": S12_TITLE, "author": S12_AUTHOR, "cover": S12_COVER, "intro": S12_INTRO, "chapters": S12_CHAPTERS, "genre": "Ngược"},
    {"title": S13_TITLE, "author": S13_AUTHOR, "cover": S13_COVER, "intro": S13_INTRO, "chapters": S13_CHAPTERS, "genre": "Ngược"},
    {"title": S14_TITLE, "author": S14_AUTHOR, "cover": S14_COVER, "intro": S14_INTRO, "chapters": S14_CHAPTERS, "genre": "Ngược"},
    {"title": S15_TITLE, "author": S15_AUTHOR, "cover": S15_COVER, "intro": S15_INTRO, "chapters": S15_CHAPTERS, "genre": "Ngược"},
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
    log("🚀 MIX BATCH 3 — 5 STORIES (💔 Ngược / Abuse → Vươn Lên)")
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
            subtitle = f"Ngược văn của {n['author']}"
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

    log(f"\n🏁 MIX BATCH 3 COMPLETE: {len(results)}/5 published")
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
