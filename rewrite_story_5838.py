#!/usr/bin/env python3
"""
REWRITE: Bị Khinh Là Thợ Xây Mặt Đen (Story ID 5838)
Viết lại toàn bộ 10 chương theo chuẩn V13+
Mỗi chương 1000-1500 từ, show don't tell, cliffhanger, character depth
"""

import json, os, sys, requests, time, ftplib

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

WP_URL = "https://doctieuthuyet.com"
SECRET_TOKEN = "ZEN_TRUYEN_2026_BYPASS"
FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"
STORY_ID = 5838

# ═══════════════════════════════════════════════════════════════════════════════
# CHARACTER BIBLE
# ═══════════════════════════════════════════════════════════════════════════════

CHARACTER_BIBLE = {
    "protagonist": {
        "name": "Nguyễn Đình Tài",
        "age": 30,
        "role": "Thợ xây → Kiến trúc sư tự học",
        "background": "Quê Quỳnh Lưu, Nghệ An. Bố mất năm 12 tuổi, mẹ nuôi 4 anh em bằng ruộng lúa. Đi phụ hồ từ 16 tuổi, 14 năm kinh nghiệm xây dựng.",
        "appearance": "Da đen cháy nắng, tay chai sạn, lưng hơi gù vì mang vác nặng. Mắt sáng, bàn tay to nhưng vẽ chính xác.",
        "ability": "14 năm kinh nghiệm thực chiến xây dựng — biết cái gì xây được, cái gì không. Gu thẩm mỹ bẩm sinh.",
        "weakness": "Không bằng cấp, mặc cảm xuất thân, hay nhún nhường quá mức. Lưng đau mãn tính.",
        "goal": "Chứng minh thợ xây cũng thiết kế được nhà đẹp. Xây nhà cho người nghèo nông thôn.",
        "voice": "Giọng Nghệ trầm, ít nói, khi nói thì chắc nịch. Không bao giờ nói quá."
    },
    "mother": {
        "name": "Nguyễn Thị Lành",
        "age": 70,
        "role": "Mẹ — nguồn động lực và triết lý sống",
        "personality": "Kiên nhẫn, chịu khó, không bao giờ than. Nói ít nhưng mỗi câu đều thấm.",
        "signature_quote": "Xây nhà giống cấy lúa — phải đợi, phải chăm, không được vội."
    },
    "antagonist_1": {
        "name": "Trần Đức Mạnh",
        "age": 45,
        "role": "Chủ thầu — đại diện cho sự coi thường lao động chân tay",
        "background": "Học hết cấp 3, khởi nghiệp từ buôn vật liệu xây dựng. Giàu nhờ mối quan hệ, không nhờ tay nghề. Lái Fortuner, bụng phệ, hay gọi thợ bằng 'mày'.",
        "weakness": "Tham lợi nhuận, cắt góc vật liệu. Sợ mất mối làm ăn với đại gia.",
        "arc": "Khinh Tài → đuổi Tài → quay lại xin hợp tác → bị từ chối → cố phá → thất bại"
    },
    "antagonist_2": {
        "name": "Phạm Quốc Bảo",
        "age": 35,
        "role": "Kiến trúc sư có bằng — đại diện cho sự ngạo mạn học thuật",
        "background": "Tốt nghiệp ĐH Kiến trúc HN, mở văn phòng ở Vinh. Thiết kế đẹp trên giấy nhưng không hiểu thực tế thi công.",
        "weakness": "Kiêu ngạo, coi thường thợ xây, thiết kế phi thực tế."
    },
    "supporter_1": {
        "name": "Lê Hồng Phong",
        "age": 50,
        "role": "Việt kiều Mỹ — khách hàng lớn, người tin tưởng Tài",
        "personality": "Cởi mở, trọng thực tài hơn bằng cấp. Về quê xây biệt thự."
    },
    "supporter_2": {
        "name": "Phan Văn Thọ",
        "age": 55,
        "role": "Nông dân — khách hàng đầu tiên",
        "personality": "Thật thà, tiết kiệm, muốn xây nhà cho con trai cưới vợ."
    }
}

# ═══════════════════════════════════════════════════════════════════════════════
# OUTLINE CẢI THIỆN
# ═══════════════════════════════════════════════════════════════════════════════
#
# ARC 1: SỈ NHỤC & BẾ TẮC (Ch 1-2)
# ARC 2: TỰ HỌC & CHỨNG MINH (Ch 3-5)
# ARC 3: ĐỐI ĐẦU & VẢ MẶT (Ch 5-7)
# ARC 4: ĐỈNH CAO & KHÉP LẠI (Ch 8-10)
#
# Sửa lỗi gốc:
# - Chương 3 & 7 cũ bị trùng (đều xây nhà cho mẹ) → tách rõ
# - Thêm antagonist 2 (KTS Bảo) cho chiều sâu xung đột
# - Thêm setback ở chương 7 (bị kiện/tố cáo hành nghề không phép)
# - Mỗi chương có cliffhanger

# ═══════════════════════════════════════════════════════════════════════════════
# 10 CHƯƠNG VIẾT LẠI — V13+
# ═══════════════════════════════════════════════════════════════════════════════

TITLE = "BỊ KHINH LÀ THỢ XÂY MẶT ĐEN, TÔI XÂY ĐƯỢC NGÔI NHÀ ĐẸP NHẤT TỈNH VÀ THÀNH KIẾN TRÚC SƯ TỰ HỌC"
AUTHOR = "Nguyễn Đình Tài"

INTRO = """<p><strong>"Chủ thầu bảo tôi: 'Mày là thợ xây, biết gì mà đòi thiết kế? Cầm bay trộn vữa cho đúng bản vẽ là được rồi.' Tôi xây đúng bản vẽ — nhưng tôi biết: bản vẽ đó sai. Và cái sai đó sẽ khiến người ta gãy xương."</strong></p>
<p>Nguyễn Đình Tài, thợ xây ba mươi tuổi từ Nghệ An, mười bốn năm cầm bay dưới nắng — da đen cháy, lưng còng, tay chai sạn. Bị đuổi khỏi công trường vì dám góp ý thiết kế. Bị cười nhạo vì thợ xây mà đòi làm kiến trúc sư.</p>
<p>Nhưng mười bốn năm xây nhà cho người ta dạy anh một thứ mà không trường đại học nào dạy: biết cái gì xây được — và cái gì sẽ sập.</p>
<p>Anh tự học kiến trúc qua YouTube và sách mượn thư viện. Anh xây ngôi nhà đầu tiên — cho mẹ. Rồi ngôi nhà đẹp nhất tỉnh. Rồi giải thưởng kiến trúc toàn quốc. Tất cả bắt đầu từ một viên gạch — và một câu nói: <em>"Mày là thợ xây, biết gì?"</em></p>"""

CHAPTERS = [

# ─────────────────────────────────────────────────────────────────────────────
# CHƯƠNG 1: THỢ XÂY MẶT ĐEN
# Arc: Sỉ nhục | Cliffhanger: Bị đuổi oan, mẹ ông chủ gãy tay
# ─────────────────────────────────────────────────────────────────────────────
("Chương 1: Thợ Xây Mặt Đen", """<p>Bốn giờ rưỡi sáng, chuông điện thoại đổ.</p>
<p>Nguyễn Đình Tài mở mắt trong phòng trọ mười hai mét vuông ở ngoại ô TP Vinh. Trần nhà ẩm mốc, quạt trần rung lắc, mùi xi măng vẫn bám trên tay dù đã tắm ba lần tối qua. Anh tắt chuông, ngồi dậy, lưng nhói một phát từ xương cùng lên tới gáy — cái đau quen thuộc từ năm hai mươi lăm tuổi, năm anh vác một lúc hai bao xi măng năm mươi ký lên tầng ba vì thiếu người.</p>
<p>Ba mươi tuổi. Mười bốn năm cầm bay.</p>
<p>Tài rửa mặt bằng nước lạnh, mặc áo thun cũ đã ngả vàng, xỏ đôi dép tổ ong mòn gót. Gương phòng tắm soi lại một khuôn mặt đen sạm — không phải đen di truyền, mà đen vì mười bốn mùa hè dưới nắng Nghệ An, loại nắng bốn mươi độ chiếu thẳng xuống đỉnh đầu từ sáng tới chiều.</p>
<p>Sáu giờ, Tài có mặt tại công trường biệt thự ông Nguyễn Văn Hoàng — đại gia bất động sản TP Vinh, căn biệt thự ba tầng ở khu đô thị mới, tổng vốn bảy tỷ. Công trường đang giai đoạn hoàn thiện nội thất.</p>
<p>Chủ thầu Trần Đức Mạnh đến lúc chín giờ — như mọi ngày. Fortuner trắng đỗ ngoài cổng, Mạnh bước xuống, bụng phệ, kính râm, tay cầm trà sữa. Bốn mươi lăm tuổi, chưa bao giờ tự tay trộn một mẻ vữa, nhưng biết cách trúng thầu nhờ nhậu đúng người.</p>
<p>"Mạnh ơi, xong tầng hai chưa?" — Mạnh gọi thợ bằng tên, nhưng thợ phải gọi Mạnh bằng "anh".</p>
<p>"Dạ, gần xong," Tài đáp. Rồi ngập ngừng. "Anh ơi, em muốn nói về cầu thang."</p>
<p>Mạnh liếc, không bỏ kính.</p>
<p>Tài mở bản vẽ — tờ A3 đã nhàu vì bụi — chỉ vào cầu thang xoắn từ tầng một lên tầng hai. "Bậc thang rộng có mười lăm phân, tiêu chuẩn tối thiểu là hai mươi lăm. Góc cua sáu mươi độ — quá gấp. Người già bước lên sẽ không đủ chỗ đặt cả bàn chân."</p>
<p>"Rồi sao?"</p>
<p>"Mẹ ông Hoàng bảy mươi hai tuổi, anh. Bà sống ở tầng hai. Em đề nghị nới rộng bậc thang, giảm góc cua xuống bốn mươi lăm độ. Chi phí thêm khoảng hai mươi triệu."</p>
<p>Mạnh hạ kính, nhìn Tài như nhìn một con kiến vừa bò lên giày. "Mày là thợ xây, Tài. Biết gì mà đòi sửa bản vẽ? Kiến trúc sư thiết kế, kỹ sư ký, chủ đầu tư duyệt. Mày cầm bay, trộn vữa, xây cho đúng. Hết."</p>
<p>"Nhưng anh, nếu bà cụ té—"</p>
<p>"Té thì bảo hiểm lo. Mày lo phần mày."</p>
<p>Tài đứng giữa công trường, tay vẫn cầm bản vẽ, miệng mím chặt. Mười hai người thợ khác im lặng — ai cũng nghe, không ai lên tiếng. Ở công trường, thợ xây không có quyền ý kiến. Đó là luật bất thành văn.</p>
<p>Anh gấp bản vẽ, nhét vào túi sau, và tiếp tục xây.</p>
<hr>
<p>Ba tháng sau.</p>
<p>Tài đang trộn vữa ở một công trình khác thì điện thoại rung. Số lạ.</p>
<p>"Tài hả? Mạnh đây."</p>
<p>Giọng Mạnh khác hẳn — không còn cái giọng chủ thầu ra lệnh. Có cái gì đó run trong thanh âm.</p>
<p>"Mẹ ông Hoàng té cầu thang. Gãy xương cẳng tay phải, nứt xương chậu, đang nằm Bệnh viện Hữu nghị Đa khoa Nghệ An."</p>
<p>Tài không nói gì. Tay cầm bay buông thõng, vữa rơi xuống đất, bắn lên ống quần.</p>
<p>"Ông Hoàng đòi kiện," Mạnh nói tiếp, giọng nhanh hơn. "Tao đang cần xác nhận — thi công đúng bản vẽ, không có lỗi thợ. Mày ký xác nhận cho tao."</p>
<p>"Anh muốn em ký cái gì?"</p>
<p>"Ký xác nhận thi công đúng thiết kế. Lỗi do kiến trúc sư, không phải lỗi thầu."</p>
<p>"Anh ơi, em có nói với anh. Em nói bậc thang hẹp. Em nói—"</p>
<p>"Mày nói cái gì? Mày có bằng không? Mày có giấy tờ gì không? Mày nói bằng mồm thì ai tin?" Giọng Mạnh bắt đầu gắt. "Ký đi. Ký xong tao cho mày làm công trình sau. Không ký — ra khỏi danh sách thợ của tao."</p>
<p>Tài nhắm mắt. Mùi vữa trộn dở xộc vào mũi. Tiếng máy trộn bê tông vẫn ầm ầm phía sau.</p>
<p>"Em không ký."</p>
<p>Im lặng ba giây.</p>
<p>"Vậy thì mày cút. Từ giờ, tao nói với tất cả chủ thầu ở Vinh: thằng Tài thợ xây — thi công sai, bà cụ gãy tay. Mày hết đường làm ở thành phố này."</p>
<p>Tiếng cúp máy.</p>
<p>Tài đứng giữa công trường, điện thoại áp bên tai, tay kia vẫn cầm bay. Mười hai năm làm thợ cho Mạnh. Mười hai năm xây nhà cho người ta mà không bao giờ được xây cho mình.</p>
<p>Tối hôm đó, Tài về phòng trọ, mở điện thoại. Ba cuộc gọi nhỡ từ ba chủ thầu quen — tất cả đều nhắn tin giống nhau: <em>"Tài ơi, anh nghe nói chuyện ở công trình ông Hoàng. Thông cảm, đợt này anh không nhận thợ mới."</em></p>
<p>Mạnh đã gọi hết.</p>
<p>Tài ngồi trên giường, nhìn bàn tay chai sạn của mình. Mười bốn năm — và bây giờ anh không có việc, không có tiếng, không có gì ngoài một đôi tay biết xây nhà nhưng không ai cho xây.</p>
<p>Anh mở ví: còn mười một triệu ba trăm ngàn.</p>
<p>Rồi anh mở YouTube — không phải để giải trí. Anh gõ vào thanh tìm kiếm: <em>"how to design a house."</em></p>"""),

# ─────────────────────────────────────────────────────────────────────────────
# CHƯƠNG 2: TỰ HỌC KIẾN TRÚC — YOUTUBE VÀ SÁCH
# Arc: Bế tắc → Âm thầm chuẩn bị | Cliffhanger: Bản vẽ đầu tiên
# ─────────────────────────────────────────────────────────────────────────────
("Chương 2: Tự Học Kiến Trúc — YouTube Và Sách", """<p>Tài dùng bảy triệu rưỡi mua một chiếc laptop Dell cũ đời 2018 từ tiệm máy tính Trần Phú. Màn hình có một vệt sáng ở góc trái, pin chỉ trụ được hai tiếng, nhưng chạy được AutoCAD bản crack — và đó là tất cả những gì anh cần.</p>
<p>Ba triệu tám còn lại chia làm ba: tiền trọ một tháng, tiền ăn hai tuần, và một thẻ wifi tháng năm mươi ngàn.</p>
<p>Ban ngày, Tài đi phụ hồ cho một đội thợ nhỏ ở huyện Nghi Lộc — không phải đội của Mạnh, mà của một ông chủ thầu già tên Sáu, chuyên xây nhà cấp bốn. Lương một trăm năm mươi ngàn một ngày, đủ sống nhưng không đủ để tiết kiệm.</p>
<p>Ban đêm, Tài học.</p>
<p>Chín giờ tối, sau khi tắm rửa, Tài mở laptop trên chiếc bàn nhựa kê sát giường. YouTube: MIT OpenCourseWare — "Introduction to Architecture" — giáo sư người Mỹ giảng bằng tiếng Anh, Tài bật phụ đề tự động rồi dùng Google Translate dịch từng đoạn. Một bài giảng bốn mươi lăm phút, Tài mất ba tiếng để hiểu.</p>
<p>Tuần đầu tiên, anh không hiểu gì cả.</p>
<p>Tuần thứ hai, anh hiểu tại sao mái nhà phải có độ dốc nhất định để thoát nước.</p>
<p>Tuần thứ ba, anh nhận ra: mười bốn năm xây nhà đã dạy anh tám mươi phần trăm kiến thức thực hành. Thứ anh thiếu là hai mươi phần trăm lý thuyết — tải trọng, kết cấu, tỷ lệ vàng, nguyên lý thẩm mỹ.</p>
<p>Và AutoCAD.</p>
<p>AutoCAD là cơn ác mộng. Giao diện tiếng Anh, phím tắt phức tạp, bàn tay chai sạn quen cầm bay bây giờ phải cầm chuột kéo từng đường thẳng trên màn hình. Ngón tay Tài to gấp rưỡi ngón tay bình thường — hai ngón liên tục bấm nhầm phím.</p>
<p>Đêm thứ mười hai, hai giờ sáng, Tài vẽ xong bản vẽ đầu tiên trên AutoCAD — mặt bằng một ngôi nhà cấp bốn, ba phòng, giống hệt nhà mẹ ở Quỳnh Lưu. Anh so sánh với bản vẽ tay trên giấy A4 — gần giống. Anh in ra ở quán photocopy đầu ngõ sáng hôm sau, mang vào công trường, lén đưa cho ông Sáu.</p>
<p>Ông Sáu nhìn bản vẽ, nheo mắt. "Mày vẽ à?"</p>
<p>"Dạ."</p>
<p>"Vẽ được." Ông Sáu gật. "Nhưng kết cấu móng sai. Đất Quỳnh Lưu nhiều cát, mày phải đổ móng băng, không phải móng đơn."</p>
<p>Tài về, sửa. Đêm đó anh tra thêm sáu tiếng về các loại móng nhà.</p>
<hr>
<p>Tháng thứ ba.</p>
<p>Tài tìm được kênh YouTube của một kiến trúc sư Nhật Bản tên Tadao Ando — người không có bằng kiến trúc sư chính quy, tự học, trở thành huyền thoại. Anh xem đi xem lại bộ phim tài liệu về Ando mười một lần.</p>
<p>Mỗi lần xem, anh đều dừng ở câu này: <em>"Kiến trúc không phải là bằng cấp. Kiến trúc là hiểu ánh sáng, hiểu gió, hiểu cách con người sống trong không gian."</em></p>
<p>Tài viết câu đó lên mảnh giấy, dán trên tường phòng trọ, ngay cạnh bản vẽ đầu tiên.</p>
<p>Tháng thứ năm, Tài đã vẽ được mười bảy bản vẽ — từ nhà cấp bốn đến nhà hai tầng, từ nhà ống phố thị đến nhà vườn nông thôn. Anh mượn sách ở thư viện tỉnh Nghệ An — "Kiến trúc nhà ở nông thôn Việt Nam", "Cơ học kết cấu cơ bản", và một cuốn cũ mèm "Mỹ thuật kiến trúc" bìa đã bong.</p>
<p>Mỗi cuốn, anh đọc ba lần. Lần một đọc lướt. Lần hai gạch chân. Lần ba chép tay những đoạn quan trọng vào một cuốn sổ — cuốn sổ bìa cứng màu nâu mà sau này anh gọi là "sổ xây".</p>
<p>Tháng thứ tám. Một đêm mưa, hai giờ sáng, Tài ngồi trước laptop, mắt cay vì thiếu ngủ. Lưng đau. Ngón tay mỏi. Bản vẽ trên màn hình là ngôi nhà thứ hai mươi ba — và anh biết nó vẫn chưa đủ tốt.</p>
<p>Anh gục đầu xuống bàn. Mùi nhựa laptop nóng xộc vào mũi.</p>
<p><em>Mày là thợ xây, biết gì?</em></p>
<p>Giọng Mạnh vọng lại trong đầu, rõ như đứng ngay sau lưng.</p>
<p>Tài muốn tắt máy. Muốn ngủ. Muốn thôi không cố nữa. Mười bốn năm cầm bay, giờ ngồi cầm chuột — có khi nào anh đang tự lừa mình?</p>
<p>Điện thoại rung. Tin nhắn của mẹ, gửi lúc mười giờ tối nhưng anh giờ mới thấy: <em>"Con ơi, mẹ biết con đang cố. Xây nhà giống cấy lúa — phải đợi, phải chăm, không được vội. Mẹ đợi con."</em></p>
<p>Tài đọc tin nhắn hai lần. Rồi ngồi thẳng lưng, dù lưng đau. Mở lại bản vẽ thứ hai mươi ba.</p>
<p>Sửa móng. Sửa mái. Thêm cửa sổ hướng đông để đón nắng sáng. Bỏ bớt một bức tường ngăn để phòng khách thông thoáng hơn.</p>
<p>Bốn giờ sáng, bản vẽ xong. Tài nhìn nó — và lần đầu tiên trong tám tháng, anh nghĩ: <em>ngôi nhà này đẹp.</em></p>
<hr>
<p>Hai năm.</p>
<p>Bảy trăm ba mươi đêm. Bốn mươi sáu bản vẽ. Ba cuốn "sổ xây" viết kín. AutoCAD từ crack lên bản student miễn phí. YouTube từ MIT mở rộng sang ArchDaily, Dezeen, kênh kiến trúc nông thôn Nhật Bản.</p>
<p>Ngày Tài vẽ xong bản vẽ thứ bốn mươi sáu — ngôi nhà một tầng ba phòng, sân trước trồng rau, mái ngói Nghệ An truyền thống nhưng kết cấu chịu lực hiện đại — anh nhìn bản vẽ và biết: đây không phải bản tập. Đây là bản thật.</p>
<p>Anh gọi điện cho mẹ.</p>
<p>"Mẹ ơi, con sẽ xây nhà mới cho mẹ. Con tự thiết kế."</p>
<p>Đầu dây bên kia im lặng ba giây. Rồi tiếng mẹ, hơi khàn: "Con ơi, mẹ ở nhà cũ quen rồi."</p>
<p>"Mẹ ở nhà cũ vì mẹ chưa có nhà mới. Con sẽ xây cho mẹ — và đây sẽ là ngôi nhà con xây cho chính mình, lần đầu tiên."</p>"""),

# ─────────────────────────────────────────────────────────────────────────────
# CHƯƠNG 3: NGÔI NHÀ ĐẦU TIÊN — NHÀ CHO MẸ
# Arc: Phản công nhỏ | Cliffhanger: Hàng xóm chụp ảnh, tin đồn lan
# ─────────────────────────────────────────────────────────────────────────────
("Chương 3: Ngôi Nhà Đầu Tiên — Nhà Cho Mẹ", """<p>Tài về Quỳnh Lưu vào một buổi chiều tháng ba, ba lô đựng laptop, cuốn "sổ xây", và bốn mươi triệu tiền tiết kiệm sau hai năm vừa phụ hồ vừa tự học.</p>
<p>Nhà mẹ nằm cuối con ngõ đất đỏ, cách đường tỉnh lộ hai trăm mét. Nhà cấp bốn, xây năm 1995 bằng gạch mộc, mái ngói đã võng giữa, tường nứt dọc hai vết từ nền lên nóc. Mỗi mùa mưa, nước ngấm qua trần, mẹ phải kê chậu hứng ở ba chỗ — phòng ngủ, bếp, và góc thờ.</p>
<p>"Mẹ ơi, con về." Tài đặt ba lô xuống hiên, nhìn mẹ đang ngồi nhặt rau muống ngoài sân. Bà Lành bảy mươi tuổi, lưng còng, tóc bạc búi sau gáy, tay gầy nhưng vẫn thoăn thoắt.</p>
<p>"Con ăn cơm chưa?"</p>
<p>"Chưa, mẹ."</p>
<p>"Vào rửa tay, mẹ nấu."</p>
<p>Suốt bữa cơm, Tài không nói về nhà mới. Anh nhìn trần nhà — vết mốc loang đen ở góc, thanh gỗ đòn tay đã mối mọt, bóng đèn tuýp chớp chớp vì dây điện cũ.</p>
<p>Sau bữa cơm, anh mở laptop, bày bản vẽ ra bàn.</p>
<p>"Mẹ, con muốn mẹ xem cái này."</p>
<p>Bà Lành đeo kính lão, cúi nhìn. Trên màn hình là bản vẽ 3D một ngôi nhà một tầng — mái ngói đỏ truyền thống Nghệ An, nhưng đường nét sắc sảo hơn, mái hơi vươn ra che hiên rộng. Sân trước có giàn hoa giấy, lối đi lát gạch cũ, vườn rau bên hông.</p>
<p>"Nhà ai đây con?"</p>
<p>"Nhà mẹ."</p>
<p>Bà Lành nhìn Tài, rồi nhìn lại màn hình. "Con ơi, mẹ không có tiền."</p>
<p>"Con có. Bốn mươi triệu, cộng thêm vật liệu con xin được từ ông Sáu — đủ. Con tự xây."</p>
<p>"Một mình?"</p>
<p>"Một mình."</p>
<hr>
<p>Ngày thứ nhất: phá dỡ.</p>
<p>Tài tháo mái ngói từng viên một, xếp gọn — viên nào còn tốt giữ lại, viên nào vỡ bỏ. Tường cũ đập, gạch cũ cạo vữa sạch, xếp thành đống vuông vắn. Bốn mươi phần trăm gạch cũ còn dùng được — Tài tính trước rồi.</p>
<p>"Mày điên à?" Hàng xóm, ông Hùng, đứng ngoài rào nhìn. "Nhà mẹ mày dù dột nhưng vẫn ở được. Giờ phá ra, ở đâu?"</p>
<p>"Mẹ em ở tạm nhà bác Tư trong lúc con xây. Hai tháng xong."</p>
<p>"Hai tháng? Mày xây một mình? Kiến trúc sư vẽ cho mày à?"</p>
<p>"Em tự vẽ."</p>
<p>Ông Hùng cười lớn, quay sang nói với mấy người qua đường: "Thằng Tài thợ xây mà đòi tự thiết kế nhà! Hai tháng nữa nhà chưa xong, mẹ nó ở ngoài đường."</p>
<p>Tài không đáp. Anh tiếp tục đập tường.</p>
<hr>
<p>Ngày thứ mười: đổ móng.</p>
<p>Đất Quỳnh Lưu nhiều cát pha sét — Tài đào móng sâu tám mươi phân, đổ móng băng thay vì móng đơn, đúng như bài học từ ông Sáu. Một mình trộn bê tông bằng máy trộn thuê, một mình đầm, một mình cân chỉnh thước thủy.</p>
<p>Mẹ mang cơm ra công trường — đúng hơn là ra sân nhà mình. "Con ơi, nghỉ trưa đi."</p>
<p>"Dạ, mẹ để đó, con làm xong đoạn này."</p>
<p>Bà Lành ngồi trên ghế nhựa, nhìn con trai. Lưng Tài ướt đẫm mồ hôi, áo dính bê tông, tay trần cầm bay — anh không đeo găng vì quen tay không. Bà nhìn thấy cái lưng hơi gù, cái cách Tài thỉnh thoảng đứng thẳng, nhăn mặt, rồi cúi xuống tiếp tục — lưng đau, nhưng không dừng.</p>
<p>"Tài ơi."</p>
<p>"Dạ?"</p>
<p>"Con nhớ viên gạch đầu tiên không?"</p>
<p>Tài dừng tay. "Viên gạch nào, mẹ?"</p>
<p>"Viên gạch con đặt lần đầu tiên, năm mười sáu tuổi, phụ hồ cho chú Bảy. Con đặt xong, con quay lại sờ nó, cười tủm tỉm. Mẹ đứng ngoài đường nhìn."</p>
<p>Tài nhớ. Viên gạch đầu tiên — hơi nghiêng, vữa thừa chảy ra ngoài, nhưng khi anh ấn nó xuống và cảm nhận nó nằm chắc trong hàng, anh biết: đây là thứ anh muốn làm.</p>
<p>"Con nhớ, mẹ."</p>
<p>"Viên gạch đó giờ nằm trong tường nhà chú Bảy. Nhà chú Bảy vẫn đứng. Mười bốn năm rồi."</p>
<p>Tài gật. Rồi tiếp tục xây.</p>
<hr>
<p>Ngày thứ năm mươi ba: hoàn thiện.</p>
<p>Không phải hai tháng. Gần hai tháng rưỡi — vì tuần thứ ba trời mưa liền bảy ngày, và tuần thứ sáu Tài bị sốt nằm hai hôm.</p>
<p>Nhưng ngôi nhà đứng đó.</p>
<p>Một tầng. Ba phòng — phòng ngủ mẹ, phòng thờ, phòng khách kiêm bếp mở. Sân trước rộng bốn mươi mét vuông, lát gạch cũ xen gạch mới tạo hoa văn. Mái ngói đỏ, đòn tay gỗ mới, trần thạch cao trắng tinh. Cầu thang — dù nhà một tầng — Tài vẫn xây sẵn lõi cầu thang ở góc nhà, bậc rộng ba mươi phân, tay vịn gỗ, phòng khi muốn nâng tầng sau.</p>
<p>Và một chi tiết mà không ai nhận ra: cửa sổ phòng ngủ mẹ hướng đông, đúng góc để nắng sáng sớm chiếu vào giường mà không chiếu vào mắt — vì mẹ hay dậy lúc năm giờ, và Tài muốn mẹ thức dậy thấy ánh sáng, không phải thấy bóng tối.</p>
<p>Mẹ Tài bước vào nhà mới.</p>
<p>Bà đi chậm, tay sờ tường — tường trắng, phẳng, không có vết nứt. Sờ cánh cửa — gỗ nhẵn, khớp khít. Bước vào phòng thờ — bàn thờ gỗ xoan đào, Tài tự đóng, chạm hoa sen hai bên.</p>
<p>Bà quay lại nhìn Tài. Mắt bà đỏ.</p>
<p>"Con xây đẹp quá." Giọng bà nghẹn. "Mẹ không nghĩ thợ xây xây được nhà đẹp thế này."</p>
<p>Tài cười, mắt cũng cay. "Mẹ ơi, thợ xây xây được. Chỉ là không ai cho thợ xây thiết kế."</p>
<p>Ông Hùng — người cười Tài ngày đầu — đứng ngoài cổng, im lặng nhìn. Rồi ông rút điện thoại ra, chụp ảnh ngôi nhà, đăng lên nhóm Facebook "Quỳnh Lưu quê tôi" với dòng chữ: <em>"Thằng Tài thợ xây xóm tôi tự thiết kế tự xây nhà cho mẹ. Nhà cấp bốn mà đẹp hơn biệt thự. Ai cần xây nhà inbox."</em></p>
<p>Bài đăng đó có hai ngàn tám trăm lượt thích trong hai ngày.</p>"""),

# ─────────────────────────────────────────────────────────────────────────────
# CHƯƠNG 4: TIN ĐỒN — THỢ XÂY THIẾT KẾ NHÀ ĐẸP
# Arc: Phản công | Cliffhanger: KTS Bảo xuất hiện, thách thức
# ─────────────────────────────────────────────────────────────────────────────
("Chương 4: Tin Đồn — Thợ Xây Thiết Kế Nhà Đẹp", """<p>Sau bài đăng của ông Hùng, tin đồn lan khắp huyện Quỳnh Lưu trong một tuần, rồi ra cả TP Vinh trong tháng.</p>
<p>"Thằng Tài thợ xây mà tự thiết kế nhà đẹp hơn kiến trúc sư" — câu đó được truyền miệng, mỗi lần truyền lại thêm thắt một chút, nhưng cái lõi không đổi: một thợ xây da đen, không bằng cấp, xây được ngôi nhà mà ai nhìn cũng muốn ở.</p>
<p>Khách đầu tiên đến gõ cửa nhà mẹ Tài vào một buổi sáng chủ nhật.</p>
<p>Ông Phan Văn Thọ, năm mươi lăm tuổi, nông dân, tay vẫn còn vết phèn từ ruộng lúa. Ông ngồi trên ghế nhựa ngoài hiên, uống trà, nhìn quanh ngôi nhà mẹ Tài rồi nói: "Tài ơi, tao muốn xây nhà cho con trai cưới vợ. Budget ba trăm triệu — kể cả đất. KTS ngoài Vinh đòi phí thiết kế năm mươi triệu, chưa kể xây."</p>
<p>"Bác Thọ muốn nhà kiểu gì?"</p>
<p>"Tao muốn nhà đẹp, chắc, và vừa đủ cho vợ chồng nó với đứa cháu sau này. Tao không cần biệt thự. Tao cần nhà — mà nhà nào nhìn vào cũng biết là có tâm."</p>
<p>Tài gật. "Em thiết kế miễn phí, bác. Em chỉ lấy tiền vật liệu và công thợ."</p>
<p>Ông Thọ trợn mắt. "Miễn phí? Mày không sống bằng gì?"</p>
<p>"Em đang tập, bác. Nhà bác là bài thực hành thứ hai của em. Em cần xây nhiều hơn — mỗi ngôi nhà dạy em một thứ mới."</p>
<hr>
<p>Tài khảo sát đất ông Thọ — mảnh đất một trăm hai mươi mét vuông ở ven đường liên xã, hướng nam, trước mặt là cánh đồng lúa. Đất thịt pha sét, nền chắc — không cần xử lý móng đặc biệt.</p>
<p>Anh thiết kế trong mười một đêm: nhà hai tầng, kiểu Nghệ An cách tân — mái ngói nhưng cải tiến kết cấu bê tông, ban công rộng hướng nam để đón gió đồng, bếp mở thông ra sân sau. Tầng một: phòng khách, bếp, phòng ngủ bố mẹ. Tầng hai: hai phòng ngủ, sân phơi. Cầu thang rộng hai mươi tám phân mỗi bậc, tay vịn inox, góc cua thoải — Tài ám ảnh về cầu thang kể từ vụ ông Hoàng.</p>
<p>Tổng chi phí: hai trăm tám mươi ba triệu, bao gồm vật liệu, công thợ, và hoàn thiện cơ bản. Tài thuê thêm hai thợ phụ — không đủ tiền thuê đội lớn.</p>
<p>Ba tháng rưỡi xây. Mỗi sáng Tài có mặt ở công trường lúc năm giờ, mỗi tối về lúc bảy giờ, ăn cơm rồi lên laptop sửa bản vẽ cho phần tiếp theo.</p>
<p>Ngày hoàn thành, ông Thọ đứng trước nhà, tay chống nạnh, miệng há ra.</p>
<p>"Tài ơi."</p>
<p>"Dạ?"</p>
<p>"Đẹp hơn nhà năm trăm triệu ngoài phố."</p>
<p>Tài cười. "Vì em biết xây, bác. KTS thành phố vẽ đẹp, nhưng thợ xây thi công không đúng ý. Em vừa vẽ vừa xây — nên nhà ra đúng như bản vẽ."</p>
<p>Ông Thọ kéo Tài lại, giọng nhỏ: "Tài ơi, ông Minh xóm trên cũng muốn xây. Bà Hoa đầu ngõ cũng hỏi. Tao cho số mày rồi."</p>
<hr>
<p>Trong ba tháng tiếp theo, Tài nhận thêm bốn đơn thiết kế — tất cả từ nông dân và công nhân Quỳnh Lưu, budget từ hai trăm đến bốn trăm triệu. Tài thiết kế miễn phí, lấy công xây, và bắt đầu có thu nhập ổn định — khoảng mười lăm triệu một tháng, gấp đôi lúc đi phụ hồ.</p>
<p>Nhưng tiếng lành thì đồn xa, mà tiếng thị phi cũng đồn không kém.</p>
<p>Một buổi chiều, Tài đang ngồi ở quán cà phê gần thư viện tỉnh, vẽ bản vẽ trên laptop, thì có người kéo ghế ngồi đối diện.</p>
<p>Phạm Quốc Bảo. Ba mươi lăm tuổi, kiến trúc sư, tốt nghiệp Đại học Kiến trúc Hà Nội, chủ Văn phòng Kiến trúc Bảo Phạm ở TP Vinh. Áo sơ mi trắng, kính gọng vàng, tay đeo đồng hồ Daniel Wellington.</p>
<p>"Tài hả? Mình là Bảo, KTS." Bảo đặt danh thiếp lên bàn.</p>
<p>"Dạ, em biết anh." Tài không nhìn danh thiếp.</p>
<p>"Nghe nói em đang thiết kế nhà ở Quỳnh Lưu? Không có chứng chỉ hành nghề, không có bằng?"</p>
<p>"Em không gọi là thiết kế. Em gọi là tư vấn xây dựng. Em tự xây, tự tư vấn cho khách."</p>
<p>Bảo cười, loại cười mà không lên đến mắt. "Tài ơi, tư vấn thiết kế kiến trúc là nghề có luật. Theo Luật Xây dựng 2014, thiết kế công trình phải do người có chứng chỉ hành nghề ký. Em đang hành nghề trái phép."</p>
<p>Tài đặt tay lên bàn. Bàn tay chai sạn, móng tay còn dính xi măng, cạnh bàn tay trắng mịn của Bảo.</p>
<p>"Anh Bảo. Em không ký bản vẽ. Em không đóng dấu. Em vẽ nhà cho người ta, rồi em tự xây. Người ta trả tiền xây, không trả tiền thiết kế."</p>
<p>"Nhưng em đang lấy khách của thị trường KTS. Nông dân giờ không thuê KTS nữa, vì có 'thằng Tài thợ xây' làm miễn phí."</p>
<p>"Anh Bảo ơi, nông dân Quỳnh Lưu chưa bao giờ thuê KTS. Vì KTS đòi năm mươi triệu phí thiết kế — bằng một phần năm ngân sách xây nhà của họ. Họ không phải khách của anh. Họ là khách mà không ai phục vụ."</p>
<p>Bảo im lặng ba giây. Cơ hàm hơi siết. Rồi anh ta đứng dậy, nhặt danh thiếp lên.</p>
<p>"Tài, mình nói thật: nếu em tiếp tục, sẽ có người khiếu nại lên Sở Xây dựng. Không phải mình — nhưng mình không ngăn được."</p>
<p>Bảo đi rồi, Tài ngồi lại, nhìn màn hình laptop. Bản vẽ ngôi nhà thứ bảy — cho bà Hoa đầu ngõ — vẫn hiện trên màn hình.</p>
<p>Tay Tài hơi run. Không phải vì sợ. Mà vì lần đầu tiên, anh nhận ra: xây nhà đẹp chưa đủ. Anh còn phải đối mặt với một hệ thống không có chỗ cho người như anh.</p>"""),

# ─────────────────────────────────────────────────────────────────────────────
# CHƯƠNG 5: MẠNH QUAY LẠI — ĐÒI HỢP TÁC
# Arc: Vả mặt vòng 1 | Cliffhanger: Mạnh đe dọa báo Sở Xây dựng
# ─────────────────────────────────────────────────────────────────────────────
("Chương 5: Mạnh Quay Lại — Đòi Hợp Tác", """<p>Fortuner trắng đỗ trước cổng nhà mẹ Tài vào một buổi trưa tháng sáu.</p>
<p>Tài đang đứng trên giàn giáo ngôi nhà thứ tám — nhà ông Minh xóm trên — khi em gái gọi điện: "Anh Tài ơi, có ông lái xe hơi đến nhà mẹ, nói tìm anh."</p>
<p>Tài biết là ai trước khi leo xuống giàn giáo.</p>
<p>Hai mươi phút sau, Tài về đến nhà. Mạnh đang ngồi trong hiên, uống trà mẹ Tài rót, chân gác lên ghế nhựa, mắt nhìn quanh ngôi nhà — ngôi nhà Tài xây cho mẹ.</p>
<p>"Đẹp thật," Mạnh nói, không nhìn Tài. "Mày xây à?"</p>
<p>"Dạ."</p>
<p>"Thiết kế?"</p>
<p>"Dạ, em tự thiết kế."</p>
<p>Mạnh quay lại, cười. Nụ cười của người vừa tìm ra một cơ hội kiếm tiền. "Tài à, quay lại làm với anh. Anh biết anh sai lần đó — vụ cầu thang. Giờ anh mở hướng mới: thiết kế nhà cho phân khúc trung bình, thị trường nông thôn. Mày thiết kế, anh xây. Anh cho mày chức 'tư vấn thiết kế', lương mười lăm triệu một tháng, cộng phần trăm."</p>
<p>Tài kéo ghế ngồi đối diện. Anh nhìn Mạnh — cái bụng phệ hơn hai năm trước, cái kính râm đắt hơn, nhưng cái nhìn thì vẫn vậy: nhìn Tài như nhìn một công cụ có thể mua.</p>
<p>"Anh ơi, anh đuổi em vì em góp ý cầu thang. Anh nói với tất cả chủ thầu ở Vinh rằng em thi công sai. Anh cắt đường sống của em."</p>
<p>"Chuyện cũ rồi, Tài. Kinh doanh mà, có lúc phải quyết nhanh."</p>
<p>"Kinh doanh của anh để mẹ ông Hoàng gãy tay, anh Mạnh."</p>
<p>Mạnh hạ chân khỏi ghế, ngồi thẳng. Mặt hơi đỏ. "Lỗi đó là lỗi kiến trúc sư, không phải lỗi tao."</p>
<p>"Em biết. Nhưng em nói với anh, bậc thang hẹp, và anh bảo em: 'Mày là thợ xây, biết gì?' Anh nhớ không?"</p>
<p>Im lặng.</p>
<p>"Em nhớ, anh. Mỗi đêm em ngồi vẽ bản vẽ, em đều nhớ. Và mỗi cái cầu thang em thiết kế — bậc rộng ba mươi phân, tay vịn chắc, góc cua thoải — là vì em nhớ."</p>
<p>Mạnh nhìn Tài. Lần đầu tiên trong hai năm, hắn nhìn thấy thứ gì đó trong mắt thằng thợ xây da đen mà hắn không nhận ra trước đó: Tài không giận. Tài đã đi qua cơn giận từ lâu. Thứ còn lại trong mắt anh là sự rõ ràng — rõ ràng về chỗ đứng của mình, và chỗ đứng của Mạnh.</p>
<p>"Em không làm với anh, anh Mạnh."</p>
<p>Mạnh đứng dậy. Ghế nhựa kêu rít trên nền gạch. "Mày nghĩ mày tự làm được? Không bằng cấp, không chứng chỉ? Thằng Bảo KTS đang chuẩn bị đơn khiếu nại lên Sở Xây dựng — mày hành nghề kiến trúc trái phép. Mày biết không?"</p>
<p>Tài không trả lời.</p>
<p>"Làm với tao thì tao che cho mày — dùng chứng chỉ của tao, bản vẽ đứng tên tao. Không làm — mày tự lo với Sở."</p>
<p>Mạnh bước ra cổng, lên xe. Tiếng Fortuner nổ máy, bụi đỏ tung lên con ngõ.</p>
<p>Mẹ Tài từ trong bếp đi ra, tay cầm khăn lau tay. Bà không hỏi gì. Bà chỉ nhìn Tài.</p>
<p>"Mẹ ơi, anh Mạnh muốn con làm cho anh ấy."</p>
<p>"Con nói gì?"</p>
<p>"Con nói không."</p>
<p>Bà Lành gật. "Xây nhà giống cấy lúa, con. Đừng để ai giẫm lên ruộng mình."</p>
<hr>
<p>Tối hôm đó, Tài ngồi ngoài hiên, nhìn cánh đồng lúa phía trước nhà trong bóng tối. Đom đóm lập lòe. Tiếng ếch kêu đều đều.</p>
<p>Anh mở điện thoại, tìm trên Google: <em>"Luật Xây dựng 2014, chứng chỉ hành nghề thiết kế."</em></p>
<p>Điều 148, khoản 2: thiết kế công trình từ cấp III trở lên phải do tổ chức hoặc cá nhân có chứng chỉ hành nghề. Nhà ở riêng lẻ dưới ba tầng, diện tích dưới 250m2 — thuộc công trình cấp IV — không bắt buộc phải có chứng chỉ thiết kế.</p>
<p>Tài đọc lại ba lần. Rồi anh mở cuốn "sổ xây", lật đến trang cuối, ghi:</p>
<p><em>"Nhà cấp IV — không cần chứng chỉ. Nhà cấp III trở lên — cần. Mình hợp pháp."</em></p>
<p>Anh gấp sổ, nhìn lên trời. Trăng non mỏng như lưỡi liềm.</p>
<p>Hợp pháp — nhưng Mạnh và Bảo sẽ không dừng lại. Anh biết điều đó.</p>
<p>Điện thoại rung. Tin nhắn từ số lạ: <em>"Chào Tài. Tôi là Lê Hồng Phong, Việt kiều Mỹ. Tôi thấy nhà anh xây trên Facebook. Tôi muốn xây biệt thự ở quê — budget hai tỷ. Anh có nhận không?"</em></p>
<p>Hai tỷ. Gấp bảy lần ngân sách lớn nhất Tài từng xây.</p>
<p>Tài nhìn tin nhắn, tim đập nhanh. Bàn tay chai sạn siết chặt điện thoại.</p>
<p>Biệt thự hai tỷ — là công trình cấp III. Cần chứng chỉ hành nghề.</p>
<p>Chính xác thứ mà Tài không có.</p>"""),

# ─────────────────────────────────────────────────────────────────────────────
# CHƯƠNG 6: DỰ ÁN HAI TỶ
# Arc: Bế tắc → Tìm cách | Cliffhanger: Bảo phá, kiểm tra đột xuất
# ─────────────────────────────────────────────────────────────────────────────
("Chương 6: Dự Án Hai Tỷ", """<p>Tài gặp Lê Hồng Phong ở quán phở đầu phố Quang Trung, TP Vinh — ông Phong chọn chỗ, bảo "tôi xa quê hai mươi năm, thèm phở bò hơn steak".</p>
<p>Năm mươi tuổi, da ngăm vì golf, đôi mắt sáng và cái bắt tay chắc nịch. Ông Phong là kỹ sư phần mềm ở California, vừa về hưu sớm, muốn về quê Nghệ An xây một ngôi nhà "để sống những năm cuối đời cho ra sống".</p>
<p>"Tài ơi, tôi xem bài đăng trên Facebook, xem ảnh nhà anh xây — nhà mẹ anh, nhà ông Thọ. Tôi thích." Ông Phong húp phở, nói tiếp. "KTS ở Vinh tôi gặp hai người rồi. Thiết kế đẹp trên giấy, nhưng khi tôi hỏi: 'Cái mái ngói này thợ xây thực tế có làm được không?' — họ ngắc."</p>
<p>"Vì KTS vẽ trên máy tính, chú. Không phải ai cũng biết cái gì xây được."</p>
<p>"Đúng. Mà Tài biết. Vì Tài là thợ xây." Ông Phong đặt đũa xuống. "Tôi muốn Tài thiết kế và xây biệt thự cho tôi. Hai tầng, phong cách Indochine — cột gỗ lim, mái ngói đỏ, sân vườn rộng, bên trong hiện đại. Budget hai tỷ."</p>
<p>Tài hít vào. "Chú Phong, em nói thật: biệt thự hai tầng trên 250 mét vuông là công trình cấp III. Theo luật, em cần chứng chỉ hành nghề thiết kế — mà em không có. Em không có bằng kiến trúc sư."</p>
<p>Ông Phong gật. "Tôi biết. Tôi tra luật rồi."</p>
<p>"Chú biết mà vẫn—"</p>
<p>"Tài, tôi sống ở Mỹ hai mươi năm. Ở bên đó, Frank Lloyd Wright không có bằng KTS. Tadao Ando cũng không. Tôi không cần bằng. Tôi cần người biết xây."</p>
<p>Ông Phong lấy từ túi ra một tờ giấy đã gấp sẵn. "Đây là cách giải quyết: tôi sẽ thuê một KTS có chứng chỉ để ký pháp lý — chỉ ký, không thiết kế. Tài thiết kế, Tài giám sát xây dựng. Trên giấy tờ, KTS ký tên. Trên thực tế, mọi thứ là của Tài."</p>
<p>"Chú tìm được KTS nào chịu ký?"</p>
<p>"Có. Một ông bạn cũ — KTS về hưu, ở Hà Nội. Phí ký mười lăm triệu. Ông ấy tin tôi."</p>
<p>Tài nhìn tờ giấy. Lần đầu tiên, có ai giải bài toán mà anh nghĩ không có lời giải.</p>
<p>"Chú Phong, tại sao chú tin em?"</p>
<p>Ông Phong cười. "Vì cầu thang nhà mẹ Tài. Tôi zoom ảnh vào — bậc rộng, góc cua thoải, tay vịn cao đúng tám mươi phân. Nhà một tầng, không cần cầu thang — mà Tài vẫn xây sẵn, vì sợ mẹ già sau này muốn nâng tầng. Người thiết kế như vậy — không phải thợ xây. Là người yêu cái nhà mình xây."</p>
<hr>
<p>Tài bắt đầu thiết kế biệt thự Phong — dự án lớn nhất đời anh — trong phòng trọ mười hai mét vuông ở ngoại ô Vinh.</p>
<p>Sáu tuần vẽ. Mỗi đêm đến ba giờ sáng. Phong cách Indochine pha Nghệ An — Tài nghiên cứu kiến trúc Pháp thuộc ở Huế, kết hợp với nhà truyền thống Nghệ An: cột gỗ lim, xà gồ gỗ, mái ngói vảy cá đỏ tươi, nhưng kết cấu bê tông cốt thép bên trong. Sân vườn trồng cây bản địa — mít, nhãn, bưởi — thay vì cọ hay thông ngoại nhập.</p>
<p>Bản vẽ gửi cho ông Phong qua email. Ông Phong phản hồi trong hai tiếng: <em>"Tuyệt vời. Bắt đầu."</em></p>
<p>KTS về hưu ở Hà Nội — ông Trần Văn Khôi, bảy mươi hai tuổi, ba mươi năm hành nghề — xem bản vẽ và gọi cho Tài: "Tài ơi, bản vẽ này tốt hơn nhiều thứ tôi thấy từ KTS trẻ bây giờ. Tôi ký."</p>
<p>Tài khởi công vào tháng chín.</p>
<hr>
<p>Tháng thứ hai của công trình. Mọi thứ đang suôn sẻ — móng xong, khung cột tầng một dựng xong, thợ đang chuẩn bị đổ sàn tầng hai.</p>
<p>Rồi một buổi sáng, một chiếc xe con biển xanh đỗ trước công trường.</p>
<p>Hai người bước xuống: một cán bộ Sở Xây dựng Nghệ An và một thanh tra xây dựng huyện. Họ cầm giấy tờ, đeo thẻ công vụ.</p>
<p>"Anh là Nguyễn Đình Tài? Chúng tôi nhận được đơn khiếu nại về việc hành nghề thiết kế kiến trúc không phép tại công trình này."</p>
<p>Tài đứng giữa công trường, tay dính bê tông, mặt đen nhẻm dưới nắng. Mười hai người thợ dừng tay, nhìn.</p>
<p>"Đơn khiếu nại của ai?"</p>
<p>"Đơn nặc danh. Nhưng nội dung cụ thể: anh không có chứng chỉ hành nghề thiết kế kiến trúc, đang tự ý thiết kế và thi công công trình cấp III."</p>
<p>Tài biết ai gửi đơn. Không cần hỏi.</p>
<p>Tay anh siết chặt cây bay, vữa ướt rỉ qua kẽ ngón.</p>"""),

# ─────────────────────────────────────────────────────────────────────────────
# CHƯƠNG 7: VIÊN GẠCH VÀ GIỌT MỒ HÔI
# Arc: Bế tắc nặng → Giải quyết pháp lý | Cliffhanger: Công trình tiếp tục
# (REWORK: không lặp xây nhà cho mẹ — thay bằng đối mặt thanh tra + flashback)
# ─────────────────────────────────────────────────────────────────────────────
("Chương 7: Viên Gạch Và Giọt Mồ Hôi", """<p>Tài mời hai cán bộ vào lán công trường, rót nước, lấy hồ sơ.</p>
<p>Bàn tay anh run — không phải vì sợ, mà vì tức. Tức vì anh biết ai gửi đơn. Tức vì anh biết mình không sai, nhưng hệ thống có thể bảo anh sai. Tức vì ngôi nhà đang xây dở — mười hai người thợ đang đứng ngoài kia, mỗi người một gia đình, mỗi ngày không làm là mỗi ngày không có cơm.</p>
<p>Nhưng Tài không để tay run lâu. Anh mở cặp hồ sơ — cặp nhựa xanh, loại năm ngàn đồng mua ở tiệm văn phòng phẩm — bên trong có:</p>
<p>Giấy phép xây dựng — do UBND huyện cấp, đúng quy trình. Bản vẽ thiết kế — có chữ ký và con dấu của KTS Trần Văn Khôi, chứng chỉ hành nghề số 2847, cấp bởi Sở Xây dựng Hà Nội, còn hiệu lực. Hợp đồng tư vấn thiết kế giữa chủ đầu tư Lê Hồng Phong và KTS Khôi.</p>
<p>"Đây là toàn bộ hồ sơ pháp lý," Tài nói, giọng trầm nhưng rõ. "KTS ký là ông Trần Văn Khôi, ba mươi năm hành nghề. Bản vẽ đúng quy chuẩn. Giấy phép đúng thủ tục."</p>
<p>Cán bộ Sở Xây dựng — người đeo kính, khoảng bốn mươi tuổi — lật từng trang, kiểm tra con dấu, đối chiếu số chứng chỉ. Thanh tra huyện đi kiểm tra công trường — đo khoảng lùi, kiểm tra móng, xem kết cấu.</p>
<p>Hai mươi phút.</p>
<p>"Hồ sơ đầy đủ," cán bộ Sở nói. "Công trình đúng phép."</p>
<p>"Vậy đơn khiếu nại—"</p>
<p>"Không có cơ sở. Chúng tôi sẽ phản hồi."</p>
<p>Hai người lên xe đi. Tài đứng ngoài cổng công trường, nhìn xe biển xanh khuất sau đường cua. Rồi anh quay lại, nhìn mười hai người thợ đang đứng chờ.</p>
<p>"Làm tiếp, anh em."</p>
<hr>
<p>Tối hôm đó, Tài không về phòng trọ. Anh ngồi lại công trường, trên đống gạch chưa xây, nhìn ngôi nhà dở dang dưới ánh trăng.</p>
<p>Khung cột tầng một đứng im trong đêm — bê tông xám, cốt thép nhô ra ở đầu cột như những ngón tay chưa hoàn thiện. Giàn giáo thép bao quanh, lưới bảo vệ rung nhẹ trong gió.</p>
<p>Tài nghĩ về viên gạch đầu tiên.</p>
<p>Năm mười sáu tuổi. Công trình nhà chú Bảy — nhà hai tầng ở xã Quỳnh Bảng. Tài phụ hồ, trộn vữa, bưng gạch. Đến ngày thứ ba, ông thợ cả bảo: "Mày đặt thử viên gạch đi."</p>
<p>Tài cầm viên gạch — nặng chừng hai ký, đỏ au, còn mới — phết vữa lên mặt dưới, đặt lên hàng. Ấn xuống, cân chỉnh bằng thước thủy.</p>
<p>Viên gạch nằm chắc. Vữa lồi ra hai bên vừa đủ. Đường mạch thẳng.</p>
<p>Ông thợ cả gật. "Được."</p>
<p>Một tiếng — "được" — và Tài biết mình sẽ làm nghề này cả đời.</p>
<p>Mười bốn năm sau, anh vẫn nhớ cảm giác đó: viên gạch nằm đúng chỗ, vữa dính chắc, hàng thẳng. Cảm giác của sự chính xác — của việc tạo ra thứ gì đó từ tay mình, chắc chắn, đứng vững.</p>
<p>Và giờ — ngồi trên đống gạch ở tuổi ba mươi hai, giữa một công trường đang bị người ta cố phá — Tài nhận ra: cảm giác đó không thay đổi. Viên gạch vẫn nặng hai ký. Vữa vẫn phải dính chắc. Hàng vẫn phải thẳng.</p>
<p>Chỉ khác một thứ: bây giờ anh không chỉ đặt gạch. Anh vẽ ra nơi viên gạch nằm.</p>
<hr>
<p>Sáng hôm sau, Tài gọi cho ông Phong.</p>
<p>"Chú Phong, hôm qua Sở Xây dựng xuống kiểm tra. Hồ sơ đủ, không có vấn đề. Nhưng em biết chắc sẽ có đợt kiểm tra tiếp — người gửi đơn sẽ không dừng."</p>
<p>"Tài, Tài cứ xây. Chuyện pháp lý để tôi lo. Tôi có luật sư ở Vinh."</p>
<p>"Chú, em không muốn chú tốn thêm tiền vì em."</p>
<p>"Tài ơi, tôi đầu tư hai tỷ vào ngôi nhà này. Mười lăm triệu phí KTS ký và vài triệu luật sư là bảo hiểm cho khoản đầu tư đó. Đừng nghĩ đó là giúp — đó là kinh doanh."</p>
<p>Tài cười. Lần đầu tiên trong tuần, anh cười.</p>
<p>Chiều hôm đó, anh nhận tin nhắn từ Phạm Quốc Bảo — tin nhắn duy nhất, ngắn gọn: <em>"Nghe nói hồ sơ anh đủ. Chúc mừng."</em></p>
<p>Tài không trả lời. Anh đặt điện thoại xuống, cầm bay lên, và tiếp tục xây.</p>
<p>Nhưng trong lòng anh biết: Bảo không chúc mừng. Bảo đang thăm dò. Và trận tiếp theo — nếu có — sẽ không phải trên giấy tờ.</p>
<p>Trận tiếp theo sẽ là trên công trình. Bảo sẽ đợi Tài xây xong — rồi so sánh. Và nếu nhà Tài xây không đẹp bằng nhà Bảo thiết kế — tất cả những gì Tài xây dựng suốt hai năm sẽ sụp đổ nhanh hơn một bức tường không có móng.</p>"""),

# ─────────────────────────────────────────────────────────────────────────────
# CHƯƠNG 8: NGÔI NHÀ ĐẸP NHẤT TỈNH
# Arc: Vả mặt vòng 2 | Cliffhanger: Báo đăng bài, Bảo sốc
# ─────────────────────────────────────────────────────────────────────────────
("Chương 8: Ngôi Nhà Đẹp Nhất Tỉnh", """<p>Sáu tháng xây. Một trăm tám mươi ngày, từ mùa thu sang xuân.</p>
<p>Tài có mặt ở công trường mỗi sáng lúc năm giờ — trước cả thợ. Anh kiểm tra từng mối nối thép, từng đường mạch gạch, từng lớp vữa trát. Không phải vì không tin thợ — mà vì đây là ngôi nhà anh thiết kế, và anh muốn nó ra đúng như trong đầu anh, đúng đến từng centimét.</p>
<p>Cột gỗ lim — mua từ một xưởng gỗ ở Nam Đàn, loại lim xanh mười năm tuổi — Tài chọn từng cây, gõ nghe tiếng, ngửi mùi gỗ để kiểm tra độ ẩm. Mái ngói vảy cá — đặt từ lò gạch ở Đô Lương, mỗi viên Tài lật kiểm tra mặt sau: ngói tốt thì mặt sau nhẵn, ngói xấu thì sần sùi, giòn, hay vỡ.</p>
<p>Ông Phong bay từ Mỹ về hai lần trong sáu tháng — mỗi lần đều đứng im nhìn công trường mười phút không nói gì. Lần thứ hai, ông nói: "Tài ơi, tôi đi khắp nước Mỹ, tôi chưa thấy ai xây nhà mà yêu nó như anh yêu."</p>
<p>Tài cười. "Vì em ở trong nhà này mỗi ngày, chú. Em biết nó thở."</p>
<hr>
<p>Ngày hoàn thành, Tài đứng ngoài cổng nhìn vào.</p>
<p>Biệt thự hai tầng, tổng diện tích xây dựng ba trăm hai mươi mét vuông, trên khuôn viên năm trăm mét vuông. Phong cách Indochine — cột gỗ lim sẫm nâu, mái ngói đỏ tươi vươn ra che hiên rộng hai mét, lan can tầng hai bằng sắt uốn hoa văn cổ điển. Sân trước lát đá ong, hai bên là hai hàng nhãn lồng Hưng Yên — ông Phong đặt giống từ quê vợ.</p>
<p>Bên trong: sàn gỗ tự nhiên, trần cao bốn mét tạo cảm giác thoáng đãng, cửa sổ lớn đón gió đông nam. Phòng khách thông lên tầng hai bằng cầu thang gỗ lim — bậc rộng ba mươi phân, tay vịn gỗ đánh bóng, mỗi bậc có đèn LED nhỏ chiếu sáng nhẹ.</p>
<p>Cầu thang. Luôn là cầu thang.</p>
<p>Tài đứng dưới chân cầu thang, đặt tay lên tay vịn. Gỗ mát, nhẵn, vừa tay. Anh bước lên từng bậc — một, hai, ba — mỗi bậc vừa chân, không hẹp, không gấp. Một bà cụ bảy mươi hai tuổi có thể đi lên đi xuống mà không sợ.</p>
<p>Anh đứng ở đầu cầu thang tầng hai, nhìn xuống. Ánh sáng từ giếng trời rọi xuống sàn gỗ, tạo một vệt vàng ấm.</p>
<p>Ngôi nhà thở. Tài nghe thấy.</p>
<hr>
<p>Tin lan nhanh hơn Tài tưởng.</p>
<p>Ông Phong mời bạn bè đến xem nhà — Việt kiều, doanh nhân địa phương, và vài người bạn cũ thời đại học. Mỗi người đến đều đứng im ở cổng giây lát trước khi bước vào — phản ứng giống hệt ông Phong lần đầu.</p>
<p>"Nhà này ai thiết kế?" — câu hỏi đầu tiên, luôn luôn.</p>
<p>"Tài. Nguyễn Đình Tài. Thợ xây."</p>
<p>"Thợ xây?"</p>
<p>Rồi họ nhìn Tài — đứng ở góc sân, da đen, tay dính vữa, mặc áo thun cũ — và không tin.</p>
<p>Một tuần sau ngày hoàn thành, phóng viên báo Nghệ An gọi điện. "Anh Tài ơi, chúng tôi nghe về ngôi nhà Indochine ở Quỳnh Lưu. Cho phép chúng tôi đến chụp ảnh và phỏng vấn?"</p>
<p>Tài định từ chối. Anh không quen trước ống kính. Nhưng ông Phong nói: "Tài, đây không phải về anh. Đây là về những người như anh — thợ xây, nông dân, người lao động — những người bị bảo 'biết gì mà đòi'. Để họ thấy: mình biết."</p>
<p>Tài đồng ý.</p>
<p>Bài báo đăng ngày thứ hai tuần sau, trang bất động sản báo Nghệ An: <em>"Thợ xây tự học trở thành kiến trúc sư — ngôi nhà Indochine đẹp nhất tỉnh."</em> Ảnh bìa: Tài đứng trước cổng biệt thự, tay cầm bản vẽ, da đen, cười.</p>
<p>Bài báo được báo VnExpress đăng lại. Rồi Tuổi Trẻ. Rồi VTV4 gọi điện đặt lịch phỏng vấn.</p>
<p>Trong ba ngày, bài báo có mười bốn ngàn lượt chia sẻ trên Facebook.</p>
<hr>
<p>Phạm Quốc Bảo đọc bài báo lúc sáng sớm, trong văn phòng kiến trúc ở TP Vinh.</p>
<p>Anh ta đọc chậm, từng dòng. Nhìn ảnh. Nhìn ngôi nhà. Nhìn cầu thang. Nhìn chi tiết cột gỗ lim, mái ngói, sân vườn.</p>
<p>Rồi anh ta đặt điện thoại xuống bàn. Hai tay chống cằm. Mắt nhìn ra cửa sổ — ngoài kia là TP Vinh, những tòa nhà xấu xí, những biệt thự copy thiết kế châu Âu lệch tông.</p>
<p>Bảo là KTS có bằng. Bảo tốt nghiệp trường danh giá. Bảo có mười năm hành nghề, hai mươi ba công trình, và một văn phòng thuê mặt tiền phố Lê Lợi.</p>
<p>Nhưng không có công trình nào của Bảo lên báo VnExpress.</p>
<p>Cơ hàm Bảo siết chặt. Ngón tay gõ lên bàn — một, hai, ba lần. Rồi anh ta mở laptop, vào trang Facebook cá nhân, gõ bài đăng:</p>
<p><em>"Xã hội tôn vinh người không bằng cấp, thiết kế kiến trúc bằng YouTube — đó là sự sỉ nhục với những KTS đã bỏ 5 năm đại học và hàng chục năm hành nghề. Tôi tôn trọng sự nỗ lực cá nhân, nhưng kiến trúc không phải trò chơi."</em></p>
<p>Bài đăng đó — trong vòng hai ngày — nhận được ba trăm bình luận. Hai phần ba là phản đối Bảo.</p>"""),

# ─────────────────────────────────────────────────────────────────────────────
# CHƯƠNG 9: CÔNG TY KIẾN TRÚC ĐÌNH TÀI
# Arc: Phản công lớn | Cliffhanger: Được mời phát biểu hội nghị toàn quốc
# ─────────────────────────────────────────────────────────────────────────────
("Chương 9: Công Ty Kiến Trúc Đình Tài", """<p>Sau biệt thự ông Phong, Tài nhận thêm mười hai đơn thiết kế trong ba tháng — từ nông dân, công nhân, giáo viên, cả một bác sĩ trạm y tế xã. Budget từ hai trăm triệu đến một tỷ. Tài không thể tự xây hết — anh cần một đội.</p>
<p>Ông Phong gợi ý: "Tài, lập công ty đi. Tôi góp vốn."</p>
<p>"Chú ơi, em là thợ xây, em không biết kinh doanh."</p>
<p>"Tài biết xây nhà. Kinh doanh là xây một thứ khác — xây tổ chức. Nguyên lý giống nhau: móng phải chắc, tường phải thẳng, mái phải kín."</p>
<p>Tháng ba, Công ty TNHH Kiến trúc Đình Tài được thành lập — vốn điều lệ năm trăm triệu, trong đó ông Phong góp ba trăm triệu (sáu mươi phần trăm), Tài góp hai trăm triệu tiền tiết kiệm từ các công trình trước (bốn mươi phần trăm). Giám đốc: Nguyễn Đình Tài.</p>
<p>Văn phòng: một phòng ba mươi mét vuông trên tầng hai nhà mẹ Tài ở Quỳnh Lưu — phòng Tài tự xây thêm khi nâng tầng nhà mẹ.</p>
<p>Nhân sự: Tài, hai thợ xây lành nghề đi theo từ đầu, và một bạn trẻ tên Hoàng — sinh viên năm cuối Đại học Xây dựng Vinh, thực tập — giúp Tài chuyển bản vẽ tay sang AutoCAD chuyên nghiệp hơn.</p>
<p>Và một KTS hợp tác ký pháp lý — không phải ông Khôi (ông đã già, nghỉ hẳn), mà một KTS trẻ tên Nguyễn Thị Mai, hai mươi tám tuổi, tốt nghiệp ĐH Kiến trúc TP HCM, về quê Nghệ An mở văn phòng nhưng không có khách.</p>
<p>"Tài ơi, tôi tốt nghiệp hai năm rồi mà không có ai thuê thiết kế," Mai nói trong buổi gặp đầu. "KTS thành phố đông quá, giá cạnh tranh. Tôi đang tính bỏ nghề đi bán hàng online."</p>
<p>"Chị Mai, em cần người có chứng chỉ hành nghề để ký pháp lý. Nhưng em không muốn chị chỉ ký — em muốn chị làm cùng. Em thiết kế concept, chị hoàn thiện bản vẽ kỹ thuật, cùng giám sát thi công."</p>
<p>Mai nhìn bản vẽ của Tài — bản thiết kế nhà hai tầng cho một giáo viên ở Yên Thành, budget ba trăm năm mươi triệu. Mai lật từng trang, mắt sáng dần.</p>
<p>"Tài, anh vẽ đẹp hơn nhiều KTS tôi học cùng."</p>
<p>"Chị biết cái gì em không biết: quy chuẩn, tiêu chuẩn, và cách trình bày hồ sơ cho đúng luật. Em biết cái gì chị không biết: cái nào xây được trong ba trăm năm mươi triệu."</p>
<p>Mai cười. "Hợp tác."</p>
<hr>
<p>Mô hình kinh doanh của Đình Tài đơn giản đến mức nhiều người không tin:</p>
<p>Thiết kế miễn phí cho khách hàng có budget dưới năm trăm triệu. Thu phí thiết kế cho budget trên năm trăm triệu — nhưng phí chỉ bằng một phần ba thị trường. Lợi nhuận đến từ thi công — Tài tự quản lý đội thợ, mua vật liệu trực tiếp, không qua trung gian, cắt bỏ lớp chủ thầu béo bở mà Mạnh từng sống nhờ.</p>
<p>"Mày thiết kế miễn phí thì sống bằng gì?" — câu hỏi mà ai cũng hỏi.</p>
<p>"Em sống bằng xây. Thiết kế miễn phí để có khách xây. Nông dân không có năm mươi triệu trả KTS — nhưng họ có ba trăm triệu xây nhà. Em lấy tiền xây, không lấy tiền vẽ."</p>
<p>Năm đầu: hai mươi ngôi nhà. Doanh thu: khoảng bốn tỷ, lợi nhuận ròng bốn trăm triệu — chia hai giữa Tài và ông Phong.</p>
<p>Năm thứ hai: bốn mươi ngôi nhà. Tài thuê thêm hai đội thợ. Hoàng tốt nghiệp, trở thành nhân viên chính thức.</p>
<p>Mỗi ngôi nhà, Tài vẫn tự đến khảo sát đất, tự vẽ concept ban đầu, tự đến công trường ít nhất hai lần một tuần. Anh không ngồi văn phòng — vì văn phòng của anh là công trường.</p>
<hr>
<p>Tháng mười, Tài nhận email từ Hội Kiến trúc sư Việt Nam.</p>
<p>Anh đọc hai lần, vì nghĩ mình hiểu sai tiếng Anh (email có cả bản tiếng Anh, vì có đối tác quốc tế đồng tổ chức):</p>
<p><em>"Kính gửi ông Nguyễn Đình Tài, Giám đốc Công ty TNHH Kiến trúc Đình Tài. Hội Kiến trúc sư Việt Nam trân trọng mời ông tham gia Hội nghị Kiến trúc Nông thôn Việt Nam lần thứ V, tổ chức tại Hà Nội ngày 15/11. Ông được đề cử trình bày tham luận chủ đề 'Kiến trúc nông thôn — từ thực tiễn đến thiết kế' và là ứng viên Giải thưởng Kiến trúc sư Cộng đồng 2026."</em></p>
<p>Tài đọc lại lần ba. Rồi gọi cho Mai.</p>
<p>"Chị Mai, em nhận được email từ Hội KTS Việt Nam. Họ mời em phát biểu ở hội nghị. Nhưng em không phải KTS."</p>
<p>"Tài, đọc lại dòng cuối đi."</p>
<p>Tài đọc: <em>"Giải thưởng Kiến trúc sư Cộng đồng được trao cho cá nhân có đóng góp xuất sắc trong kiến trúc phục vụ cộng đồng, không giới hạn bằng cấp."</em></p>
<p>"Không giới hạn bằng cấp," Mai nhắc lại. "Họ mời anh vì nhà anh xây, không phải vì bằng anh có."</p>
<p>Tài ngồi im. Ngoài cửa sổ, nắng chiều chiếu lên cánh đồng Quỳnh Lưu — lúa đang chín vàng.</p>
<p>Anh nghĩ đến Bảo — người đăng bài "sỉ nhục KTS" — và tự hỏi: Bảo có nhận được email này không?</p>"""),

# ─────────────────────────────────────────────────────────────────────────────
# CHƯƠNG 10: BÌNH MINH TRÊN CÔNG TRƯỜNG
# Arc: Kết | Vả mặt vòng 3 (công khai) + Circle back
# ─────────────────────────────────────────────────────────────────────────────
("Chương 10: Bình Minh Trên Công Trường", """<p>Hội nghị Kiến trúc Nông thôn Việt Nam lần thứ V — khách sạn Melia Hanoi, phòng hội nghị tầng ba, hai trăm ghế.</p>
<p>Tài ngồi ở hàng ghế diễn giả, bàn tay đặt trên đùi. Anh mặc áo sơ mi trắng — chiếc áo sơ mi duy nhất anh có, mua ở chợ Vinh ba trăm ngàn — và quần tây đen. Tay anh vẫn chai sạn, móng tay vẫn có vết xi măng mà không cách nào rửa sạch.</p>
<p>Hai trăm người trong phòng: KTS, giáo sư, quan chức Bộ Xây dựng, phóng viên, và một số đại biểu quốc tế — người Nhật, người Hàn, người Singapore. Hầu hết mặc vest.</p>
<p>Tài là diễn giả thứ tư — sau ba KTS có bằng tiến sĩ.</p>
<p>MC giới thiệu: "Diễn giả tiếp theo — ông Nguyễn Đình Tài, Giám đốc Công ty TNHH Kiến trúc Đình Tài, Nghệ An. Ông Tài là ứng viên Giải Kiến trúc sư Cộng đồng năm nay."</p>
<p>Tài đứng dậy, bước lên bục. Chân hơi cứng — anh chưa bao giờ đứng trước hơn mười người. Tay cầm micro, mồ hôi thấm lòng bàn tay.</p>
<p>Anh nhìn xuống — hai trăm đôi mắt. Một số tò mò. Một số hoài nghi. Một vài cặp mắt — ở góc phải, hàng ba — anh nhận ra: Phạm Quốc Bảo, ngồi khoanh tay, mặt không biểu cảm.</p>
<p>Tài hít vào. Rồi bắt đầu — không phải bằng bài phát biểu soạn sẵn, mà bằng câu chuyện:</p>
<p>"Tôi là thợ xây."</p>
<p>Im lặng.</p>
<p>"Tôi xây nhà từ năm mười sáu tuổi. Mười bốn năm cầm bay, trộn vữa, đổ bê tông. Da tôi đen vì nắng, lưng tôi đau vì vác, tay tôi chai vì gạch. Tôi không có bằng kiến trúc sư. Tôi không tốt nghiệp đại học. Tôi tự học kiến trúc bằng YouTube, sách thư viện, và AutoCAD crack."</p>
<p>Vài tiếng cười nhẹ trong phòng. Tài không cười.</p>
<p>"Nhưng tôi biết một thứ mà nhiều KTS không biết: nông dân Việt Nam xây nhà bằng bao nhiêu tiền."</p>
<p>Anh bấm slide — hình ảnh ngôi nhà ông Thọ, budget ba trăm triệu. Rồi ngôi nhà bà Hoa, hai trăm bảy mươi triệu. Rồi ngôi nhà thầy giáo ở Yên Thành, ba trăm năm mươi triệu.</p>
<p>"Những ngôi nhà này — budget dưới năm trăm triệu — là phân khúc mà kiến trúc sư thành phố không phục vụ. Vì phí thiết kế tối thiểu năm mươi triệu — bằng một phần năm đến một phần mười ngân sách xây nhà của họ. Họ không đủ tiền thuê KTS — nên họ tự xây, theo bản vẽ tay, không kết cấu, không thẩm mỹ, không an toàn."</p>
<p>Slide tiếp: ảnh những ngôi nhà tự xây ở nông thôn Nghệ An — tường nứt, mái lệch, cầu thang hẹp.</p>
<p>"Tôi không đến đây để nói kiến trúc sư sai. Tôi đến đây để nói: có một thị trường mà kiến trúc sư chưa chạm đến. Có hàng triệu gia đình nông thôn cần nhà đẹp, nhà an toàn, nhà vừa túi tiền — và không ai giúp họ."</p>
<p>Slide cuối: ảnh biệt thự ông Phong — Indochine, cột gỗ lim, mái ngói đỏ, sân vườn xanh.</p>
<p>"Và đây là ngôi nhà cuối cùng tôi muốn cho quý vị xem. Budget hai tỷ — khác hẳn những ngôi nhà ba trăm triệu. Nhưng nguyên lý thiết kế giống nhau: hiểu đất, hiểu người, hiểu ngân sách, và xây bằng tay mình."</p>
<p>Tài đặt micro xuống, nhìn thẳng vào khán phòng.</p>
<p>"Tôi là thợ xây. Tôi tự học kiến trúc. Tôi thiết kế nhà cho nông dân — những người mà KTS thành phố không phục vụ vì 'budget quá nhỏ'. Tôi không xin phép ai để làm điều đó. Tôi chỉ xây — và để ngôi nhà nói thay."</p>
<p>Im lặng bốn giây.</p>
<p>Rồi vỗ tay. Từ hàng sau lên hàng trước, từ lẻ tẻ đến đồng loạt. Hai trăm người đứng dậy — standing ovation — thứ mà Tài chỉ thấy trên YouTube.</p>
<p>Anh nhìn xuống hàng ba, góc phải. Bảo vẫn ngồi. Không vỗ tay. Nhưng tay Bảo — bấu chặt mép ghế, trắng bệch.</p>
<hr>
<p>Tài nhận Giải Kiến trúc sư Cộng đồng — cúp pha lê nhỏ, nặng chừng nửa ký, khắc tên anh.</p>
<p>Sau lễ trao giải, một người đàn ông Nhật Bản — giáo sư kiến trúc ĐH Tokyo — bước đến, bắt tay Tài qua phiên dịch: "Ông Tài, tôi nghiên cứu kiến trúc nông thôn châu Á hai mươi năm. Câu chuyện của ông giống Tadao Ando — nhưng Ando xây cho người giàu. Ông xây cho nông dân. Đó còn khó hơn."</p>
<p>Tài cười. "Cảm ơn giáo sư. Nhưng tôi không phải Ando. Tôi là thợ xây."</p>
<hr>
<p>Trên chuyến xe khách Hà Nội — Vinh, Tài ngồi ghế cửa sổ, cúp pha lê để trong ba lô dưới chân. Mười hai tiếng đường dài. Anh không ngủ.</p>
<p>Anh nghĩ về mẹ — bà Lành, giờ đang ngồi trong ngôi nhà anh xây, uống trà, xem TV màn hình lớn mà anh mua tặng. Bà không biết anh vừa nhận giải thưởng — anh chưa nói, vì muốn về tận nơi đưa cúp cho mẹ cầm.</p>
<p>Anh nghĩ về Mạnh — chủ thầu béo lái Fortuner. Mạnh giờ vẫn xây, vẫn cắt góc, nhưng mất ba mối lớn vì khách chuyển sang Đình Tài. Mạnh không liên lạc nữa — im lặng hơn cả thù hận.</p>
<p>Anh nghĩ về Bảo — KTS có bằng. Bảo xóa bài đăng "sỉ nhục" sau hội nghị. Không ai nói gì, nhưng Tài biết: bài đăng biến mất lúc nửa đêm, ngay sau khi video bài phát biểu của Tài được đăng lên YouTube Hội KTS Việt Nam và có bốn mươi ngàn lượt xem trong hai ngày.</p>
<p>Và anh nghĩ về viên gạch đầu tiên — năm mười sáu tuổi, phụ hồ cho chú Bảy, viên gạch đỏ nặng hai ký, đặt hơi nghiêng, vữa lồi ra hai bên.</p>
<p>Viên gạch đó vẫn nằm trong tường nhà chú Bảy. Mười tám năm rồi. Nhà vẫn đứng.</p>
<hr>
<p>Năm giờ sáng hôm sau, Tài có mặt ở công trường — ngôi nhà thứ sáu mươi. Tay cầm bản vẽ, mắt nhìn khung thép, miệng hướng dẫn thợ.</p>
<p>Da vẫn đen. Tay vẫn chai. Lưng vẫn đau.</p>
<p>Nhưng trên bàn tay chai sạn cầm bản vẽ, có một thứ mà mười bốn năm trước không có: đường nét do anh vẽ, ngôi nhà do anh thiết kế, cuộc đời do anh quyết định.</p>
<p>"Tài ơi, sao mày không thuê người xây, mày chỉ thiết kế thôi?" — thợ Hùng, đứa em kết nghĩa, hỏi trong lúc trộn vữa.</p>
<p>"Vì tao là thợ xây, Hùng. Thiết kế mà không xây — như vẽ mà không tô. Tao muốn tô."</p>
<p>Mặt trời mọc trên cánh đồng Nghệ An. Ánh vàng rải trên những ngôi nhà mới — mái ngói đỏ, sân vườn xanh, cầu thang rộng.</p>
<p>Nguyễn Đình Tài — thợ xây mặt đen, kiến trúc sư tự học — cầm bay, trộn vữa, và tiếp tục xây.</p>
<p>Vì mỗi viên gạch anh đặt — từ viên đầu tiên năm mười sáu tuổi đến viên hôm nay — đều nói cùng một câu:</p>
<p><em>Tôi ở đây. Tôi đứng vững. Và tôi sẽ không sập.</em></p>"""),
]

# ═══════════════════════════════════════════════════════════════════════════════
# QA REVIEW
# ═══════════════════════════════════════════════════════════════════════════════

def qa_review():
    print("=== BÁO CÁO QA REVIEW ===")
    total_words = 0
    for title, content in CHAPTERS:
        words = len(content.split())
        p_count = content.count("<p>")
        print(f"  {title}: ~{words} từ, {p_count} đoạn")
        total_words += words
    print(f"\nTổng: {len(CHAPTERS)} chương, ~{total_words} từ")
    print(f"Trung bình: ~{total_words // len(CHAPTERS)} từ/chương")

def build_chapters():
    chapters = []
    for title, raw_html in CHAPTERS:
        chapters.append({"title": title, "content": raw_html})
    return chapters

def get_ftp():
    for i in range(3):
        try:
            ftp = ftplib.FTP(FTP_HOST, timeout=60)
            ftp.login(FTP_USER, FTP_PASS)
            return ftp
        except Exception as e:
            print(f"  FTP retry {i+1}: {e}")
            time.sleep(3*(i+1))
    raise Exception("FTP connect failed after 3 retries")

def update_story():
    """Update existing story 5838 on WordPress"""
    chapters = build_chapters()
    qa_review()

    print(f"\n🚀 UPDATING story {STORY_ID}: {TITLE[:60]}...")
    print(f"   Chapters: {len(chapters)}")

    # Step 1: Upload update_novel.php via FTP
    print("\n📤 Uploading update_novel.php via FTP...")
    helper_path = os.path.join(BASE_DIR, "update_novel.php")
    ftp = get_ftp()
    with open(helper_path, "rb") as f:
        ftp.storbinary("STOR update_novel.php", f)
    ftp.quit()
    print("   ✓ update_novel.php uploaded")

    # Step 2: Call update API
    print("\n📡 Calling update API...")
    payload = {
        "secret_token": SECRET_TOKEN,
        "story_id": STORY_ID,
        "intro": INTRO,
        "chapters": chapters,
    }

    try:
        res = requests.post(f"{WP_URL}/update_novel.php", json=payload, timeout=300)
        data = res.json()
        if data.get("success"):
            print(f"\n🎉 SUCCESS!")
            print(f"   Story ID: {data['story_id']}")
            print(f"   Title: {data.get('story_title', 'N/A')}")
            print(f"   Intro: {data.get('intro_status', 'N/A')}")
            print(f"   Old chapters deleted: {data.get('old_chapters_deleted', 0)}")
            print(f"   New chapters created: {data.get('new_chapters_count', 0)}")
            for ch in data.get('chapters', []):
                print(f"     → ID {ch['id']}: {ch['title']}")
        else:
            print(f"❌ API Error: {data}")
    except Exception as e:
        print(f"❌ Exception: {e}")
        import traceback; traceback.print_exc()

    # Step 3: Cleanup - remove update_novel.php from server
    print("\n🧹 Cleaning up update_novel.php from server...")
    try:
        ftp = get_ftp()
        ftp.delete("update_novel.php")
        ftp.quit()
        print("   ✓ Cleaned up")
    except:
        print("   ⚠️ Cleanup failed (non-critical)")

if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser(description="Rewrite story 5838")
    p.add_argument("--dry-run", action="store_true", help="QA review only, no publish")
    p.add_argument("--live", action="store_true", help="Update on WordPress")
    a = p.parse_args()

    if a.dry_run:
        qa_review()
        print("\n📋 DRY RUN — no changes published")
        print("\n📖 INTRO preview:")
        print(INTRO[:300] + "...")
        for title, content in CHAPTERS:
            print(f"\n{'='*60}")
            print(f"📖 {title}")
            print(f"{'='*60}")
            # Show first 500 chars
            print(content[:500] + "...")
    elif a.live:
        update_story()
    else:
        print("Use --dry-run or --live")
