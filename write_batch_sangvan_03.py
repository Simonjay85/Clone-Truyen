#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
write_batch_sangvan_03.py — Batch 3: 4 Truyện Sảng Văn (Stories 9-12)
=====================================================================
Story 9: Kỹ sư vệ tinh bị sa thải (cover 43)
Story 10: KTS resort sinh thái bị xé hợp đồng (cover 44)
Story 11: Kỹ sư PCCC bị đổ tội cháy nhà máy (cover 45)
Story 12: Sinh viên robotics bị gạch tên (cover 46)
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
# STORY 9: KỸ SƯ VỆ TINH
# ═══════════════════════════════════════════════════════════════════════════════

S9_TITLE = "BỊ SA THẢI NGAY TRƯỚC GIỜ PHÓNG VỆ TINH, TÔI MANG DỮ LIỆU QUỸ ĐẠO CHỨNG MINH AI MỚI LÀ THIÊN TÀI"
S9_AUTHOR = "Lý Thanh Sơn"
S9_COVER = "base_cover_43.png"
S9_INTRO = """<p><strong>"Bốn năm tôi tính toán quỹ đạo cho vệ tinh quan sát Trái Đất đầu tiên của Việt Nam. Đổi lại, Giám đốc cướp công, đuổi tôi khỏi phòng điều khiển ba tiếng trước giờ phóng."</strong></p>
<p>Lý Thanh Sơn, kỹ sư quỹ đạo thiên tài tại Trung tâm Vũ trụ Việt Nam (VNSC), bị Giám đốc Phạm Quốc Hùng và Trưởng nhóm Đặng Văn Bình sa thải ngay trước giờ phóng vệ tinh VNSat-2 để chiếm công trình tính toán quỹ đạo đột phá.</p>
<p>Bị tước mọi thứ, Sơn thành lập SkyViet — startup vệ tinh tư nhân đầu tiên của Việt Nam, phóng chùm vệ tinh quan sát giá rẻ khiến cả ngành hàng không vũ trụ Đông Nam Á phải nể phục.</p>"""

S9_CHAPTERS = [
("Chương 1: Ba Tiếng Trước Giờ Phóng", """Trung tâm Điều khiển Vệ tinh, Khu Công nghệ cao Hòa Lạc, hai giờ sáng. Lý Thanh Sơn ngồi trước bốn màn hình hiển thị dữ liệu telemetry, mắt dán vào chuỗi tọa độ quỹ đạo đang nhấp nháy xanh — tất cả nominal.

Còn ba tiếng nữa, vệ tinh VNSat-2 sẽ được phóng từ bãi phóng Satish Dhawan, Ấn Độ. Đây là vệ tinh quan sát Trái Đất đầu tiên do Việt Nam thiết kế và chế tạo, mang theo camera quang học độ phân giải một mét — đủ để nhìn rõ từng chiếc xe trên đường phố Hà Nội từ không gian.

Sơn là người tính toán toàn bộ quỹ đạo cho VNSat-2. Bốn năm ròng, anh phát triển thuật toán tối ưu quỹ đạo mới — giảm nhiên liệu đẩy bốn mươi phần trăm so với phương pháp truyền thống, cho phép vệ tinh hoạt động lâu hơn hai năm so với thiết kế.

"Sơn, lên phòng Giám đốc. Ngay." Giọng qua intercom lạnh tanh.

Sơn rời bàn điều khiển, bước lên tầng ba. Trong phòng, Giám đốc Phạm Quốc Hùng ngồi cạnh Đặng Văn Bình — Trưởng nhóm quỹ đạo, người mà Sơn đã training suốt hai năm.

"Lý Thanh Sơn, ban lãnh đạo Trung tâm quyết định: từ giờ phút này, anh bị đình chỉ công tác. Lý do: vi phạm quy chế bảo mật khi chia sẻ dữ liệu quỹ đạo với bên thứ ba chưa được phê duyệt."

"Bên thứ ba? Tôi gửi paper cho tạp chí Journal of Spacecraft and Rockets, đó là công bố khoa học, không phải vi phạm bảo mật!"

"Paper đó chứa thông tin nhạy cảm về thuật toán quỹ đạo VNSat-2," Bình lên tiếng. "Và từ nay, thuật toán đó sẽ được đăng ký dưới tên Trung tâm, tác giả: Phạm Quốc Hùng và Đặng Văn Bình."

Sơn nhìn Bình — đứa em mà anh dạy từ cách dùng MATLAB đến viết code orbit propagation. "Bình, mày biết rõ ai viết thuật toán đó."

Bình tránh mắt: "Anh Sơn, đây là quyết định tập thể."

Bảo vệ thu badge, laptop, và USB token truy cập hệ thống. Sơn bị đưa ra cổng — ba tiếng trước khi vệ tinh mà anh dành bốn năm đời mình phóng lên quỹ đạo.

Anh đứng ngoài hàng rào, nhìn qua khe cửa vào phòng điều khiển sáng đèn. Trên màn hình lớn, countdown đang chạy: T-02:47:33.

"Vệ tinh bay lên quỹ đạo tôi tính. Thuật toán tôi viết. Nhưng tên tôi bị xóa," Sơn thì thầm.

Trong túi áo khoác, anh còn một chiếc điện thoại cũ — nơi lưu toàn bộ code thuật toán version đầu tiên, với git commit từ bốn năm trước. Bằng chứng mà không ai cướp được."""),

("Chương 2: Startup Vệ Tinh Trong Garage", """Sơn về nhà mẹ ở Đống Đa, Hà Nội. Ba tháng thất nghiệp, anh dùng thời gian cải tiến thuật toán quỹ đạo — phiên bản mới, tốt hơn, nhanh hơn, chính xác hơn.

Anh gặp Trần Hải Yến, ba mươi tuổi, kỹ sư hệ thống vệ tinh từng làm việc tại Airbus Defence and Space ở Toulouse. Yến vừa về Việt Nam, muốn xây startup vệ tinh nhỏ giá rẻ.

"Anh Sơn, thị trường vệ tinh quan sát toàn cầu đạt hai mươi tỷ đô năm 2026. Planet Labs chụp ảnh trái đất mỗi ngày bằng chùm hai trăm vệ tinh nano. Việt Nam hoàn toàn có thể làm tương tự — nếu có người tính quỹ đạo giỏi."

"Tôi tính quỹ đạo giỏi nhất Đông Nam Á," Sơn nói, không khoe khoang mà nêu sự thật.

Hai người thành lập SkyViet trong garage nhà Sơn. Vốn ban đầu: năm trăm triệu đồng tiết kiệm của cả hai. Mục tiêu: thiết kế và phóng chùm vệ tinh nano quan sát Trái Đất, giá rẻ bằng một phần mười vệ tinh truyền thống.

Yến thiết kế phần cứng — vệ tinh CubeSat 6U, nặng mười hai kg, dùng linh kiện thương mại giá rẻ thay vì linh kiện quân sự đắt đỏ. Sơn viết phần mềm quỹ đạo và điều khiển — thuật toán cho phép vệ tinh nhỏ xíu chụp ảnh chính xác như vệ tinh lớn gấp mười lần.

Sáu tháng, prototype đầu tiên hoàn thành. Họ đặt tên nó: Chim Lạc-1."""),

("Chương 3: Chim Lạc Bay Lên", """SkyViet gọi vốn thành công từ quỹ SpaceVC Singapore — mười triệu đô, đủ để phóng ba vệ tinh Chim Lạc.

Vệ tinh được phóng piggyback trên tên lửa SpaceX Falcon 9 — chia sẻ chuyến bay với hai mươi vệ tinh khác để giảm chi phí. Giá phóng: năm trăm nghìn đô mỗi vệ tinh, rẻ hơn hai mươi lần so với VNSat-2.

Ngày phóng, Sơn và Yến ngồi trong phòng điều khiển tạm — một phòng họp thuê tại Bách Khoa Hà Nội, ba laptop nối internet. Không có phòng điều khiển triệu đô như VNSC.

"T minus ten, nine, eight..." Sơn đếm ngược, tim đập điên cuồng.

Falcon 9 cất cánh, ba vệ tinh Chim Lạc tách khỏi tên lửa, mở tấm pin mặt trời, bắt đầu truyền tín hiệu.

"Contact! Chim Lạc-1, Chim Lạc-2, Chim Lạc-3 — all three healthy!" Yến hét lên, nước mắt chảy.

Tấm ảnh đầu tiên từ Chim Lạc-1: đồng bằng sông Cửu Long nhìn từ không gian, độ phân giải năm mét — đủ để theo dõi diện tích trồng lúa, mực nước sông, và xói lở bờ biển.

Hình ảnh viral trên mạng. "Người Việt tự chụp ảnh Việt Nam từ vũ trụ!" Hashtag #ChimLạc trending khắp Việt Nam.

Tại VNSC, Hùng đọc tin, mặt tái mét. Vệ tinh VNSat-2 trị giá bốn trăm tỷ mà anh ta cướp công — giờ bị ba vệ tinh nhỏ xíu giá rẻ bằng một phần mười làm lu mờ."""),

("Chương 4: Đối Đầu Tại Hội Nghị IAC", """Sơn trình bày paper tại International Astronautical Congress (IAC) ở Paris — hội nghị vũ trụ lớn nhất thế giới. Bình cũng có mặt, trình bày thuật toán quỹ đạo "của mình" cho VNSat-2.

Khi đến phần Q&A bài trình bày của Bình, Sơn giơ tay: "Anh Bình, trong slide 14, hệ số J2 perturbation mà anh dùng có giá trị 1.08263×10^-3. Giá trị này tôi tính bằng phương pháp riêng, khác với giá trị chuẩn trong textbook. Anh giải thích tại sao anh dùng giá trị này?"

Bình đông cứng. Hắn dùng số liệu của Sơn mà không hiểu tại sao.

Sơn tiếp: "Và đây," anh chiếu git log từ điện thoại lên màn hình — commit history bốn năm trước, chứng minh thuật toán là của anh.

Ban tổ chức IAC ghi nhận. Paper của Bình bị gắn cờ "authorship dispute." Đạo đức khoa học trong ngành vũ trụ nghiêm khắc — danh tiếng Bình và VNSC bị tổn thương nặng nề."""),

("Chương 5: Chùm Vệ Tinh — Mắt Thần Trên Bầu Trời", """Hai năm sau, SkyViet phóng thêm mười hai vệ tinh Chim Lạc, tạo thành chùm mười lăm vệ tinh bao phủ toàn bộ Đông Nam Á. Cập nhật ảnh vệ tinh mỗi sáu giờ — nhanh hơn bất kỳ hệ thống nào trong khu vực.

Khách hàng ào ạt: Bộ TNMT mua dữ liệu theo dõi rừng và sạt lở, Bộ NN&PTNT dùng để giám sát mùa vụ, hải quân dùng để tuần tra biển đảo, và các công ty bảo hiểm dùng để đánh giá thiên tai.

Doanh thu năm thứ hai: năm mươi tỷ đồng. SkyViet trở thành startup vũ trụ giá trị nhất Đông Nam Á, được TechCrunch gọi là "Planet Labs of Southeast Asia."

Sơn và Yến không chỉ là đồng nghiệp nữa — họ yêu nhau giữa những đêm thức trắng theo dõi quỹ đạo vệ tinh, giữa tiếng beep beep của tín hiệu telemetry từ không gian."""),

("Chương 6: SkyViet Thành Unicorn", """Series B do Softbank và quỹ vũ trụ của Jeff Bezos đồng dẫn đầu, hai trăm triệu đô, định giá SkyViet một tỷ đô. Unicorn vũ trụ đầu tiên của Đông Nam Á.

SkyViet mở rộng sang ba lĩnh vực: ảnh vệ tinh cho nông nghiệp, theo dõi khí hậu, và kết nối IoT vệ tinh cho vùng sâu vùng xa. Nhà máy lắp ráp vệ tinh tại Hòa Lạc, tuyển hai trăm kỹ sư.

Sơn vẫn tự tay code mỗi đêm, vẫn tính quỹ đạo cho mỗi vệ tinh mới. "Vệ tinh là đứa con, quỹ đạo là đường đi. Bố phải tính đường cho con," anh nói."""),

("Chương 7: Ước Mơ Thuở Nhỏ", """Ít ai biết Sơn mê vũ trụ từ năm tám tuổi, khi bố — một thợ điện ở Thanh Xuân — mua cho anh cuốn sách cũ "Từ Trái Đất đến Mặt Trăng" của Jules Verne ở chợ sách Nguyễn Xí.

Bố mất khi Sơn mười lăm tuổi — tai nạn điện trong lúc sửa đường dây. Trước khi mất, bố nói: "Con nhìn lên trời đi. Bố ở trên đó nhìn con."

Mỗi vệ tinh Chim Lạc mang theo một chip nhớ nhỏ, lưu ảnh bố Sơn — người thợ điện đã cho con trai ước mơ bay lên trời.

SkyViet thành lập học bổng "Chim Lạc" — tài trợ mỗi năm hai mươi sinh viên nghèo theo đuổi ngành hàng không vũ trụ."""),

("Chương 8: VNSC Sụp Đổ", """Vụ đạo văn thuật toán quỹ đạo bùng nổ khi tạp chí Journal of Spacecraft and Rockets chính thức xác nhận Sơn là tác giả gốc. Bộ KH&CN mở điều tra VNSC.

Hùng bị cách chức Giám đốc, cấm giữ chức vụ quản lý khoa học mười năm. Bình bị thu hồi bài báo, cấm công bố khoa học quốc tế năm năm.

Nhiều kỹ sư giỏi nhất VNSC xin chuyển sang SkyViet. Sơn nhận tất cả — không phân biệt, không trả thù."""),

("Chương 9: Hợp Đồng NASA", """NASA liên hệ SkyViet để hợp tác chương trình giám sát khí hậu toàn cầu — dùng chùm vệ tinh Chim Lạc bổ sung cho hệ thống Landsat.

Hợp đồng trị giá một trăm triệu đô trong năm năm. Sơn bay đến Houston, ký hợp đồng tại Johnson Space Center, nơi các phi hành gia Apollo từng huấn luyện.

"Tôi tính quỹ đạo vệ tinh vì muốn nhìn Việt Nam từ trên cao," Sơn nói tại lễ ký. "Giờ NASA dùng vệ tinh Việt Nam để nhìn cả Trái Đất. Bố tôi nói đúng: ông đang nhìn từ trên đó." """),

("Chương 10: Quay Về Phòng Điều Khiển", """SkyViet ký hợp đồng hợp tác với VNSC — giờ đã có ban lãnh đạo mới. Sơn quay lại phòng điều khiển nơi anh bị đuổi.

Phòng vẫn vậy — bốn màn hình, bàn console, tiếng beep beep tín hiệu. Nhưng giờ trên màn hình hiển thị: mười lăm vệ tinh Chim Lạc đang bay, phủ sóng toàn Đông Nam Á.

Bình đứng ở góc phòng, gầy hơn, xanh xao. "Anh Sơn, em xin lỗi."

Sơn nhìn đứa em: "Mày giỏi kỹ thuật, nhưng mày yếu đạo đức. Đó là lỗi tôi — tôi dạy mày code mà quên dạy mày làm người."

Rồi anh rút USB: "Đây là codebase thuật toán quỹ đạo thế hệ mới. Tôi open source nó — ai cũng dùng được, kể cả mày. Lần này, học đi."

Sơn quay ra, nắm tay Yến — giờ đã là vợ anh. Trên bầu trời Hòa Lạc, nếu nhìn kỹ vào thời điểm đúng, có thể thấy một chấm sáng nhỏ xíu bay ngang — Chim Lạc-1, đứa con đầu lòng, vẫn đang bay ở độ cao năm trăm cây số, vẫn đang chụp ảnh Việt Nam mỗi ngày."""),
]

# ═══════════════════════════════════════════════════════════════════════════════
# STORY 10: KTS RESORT SINH THÁI
# ═══════════════════════════════════════════════════════════════════════════════

S10_TITLE = "BỊ XÉ HỢP ĐỒNG Ở VINPEARL, TÔI DỰNG RESORT SINH THÁI KHIẾN CẢ ĐÔNG NAM Á HỌC THEO"
S10_AUTHOR = "Trương Hải Yến"
S10_COVER = "base_cover_44.png"
S10_INTRO = """<p><strong>"Ba năm tôi thiết kế resort sinh thái hoàn hảo nhất Đông Nam Á — không chặt một cây, không đổ một mét khối bê tông. Đổi lại, chủ đầu tư xé hợp đồng, xây khách sạn bê tông cốt thép trên chính mảnh đất tôi quy hoạch."</strong></p>
<p>Trương Hải Yến, kiến trúc sư cảnh quan tài năng, bị tập đoàn BĐS Nguyễn Đức Thành và đối tác Hàn Quốc Lee Sang-ho phản bội khi họ loại bỏ thiết kế xanh để xây resort bê tông tối đa hóa lợi nhuận.</p>
<p>Mất hợp đồng triệu đô, Yến xây dựng EcoNest — resort sinh thái mái lá giữa rừng nhiệt đới, trở thành biểu tượng du lịch bền vững và khiến cả châu Á phải học theo mô hình.</p>"""

S10_CHAPTERS = [
("Chương 1: Bản Thiết Kế Bị Xé", """Phòng họp VIP tầng năm mươi Landmark 81, mười giờ sáng. Trương Hải Yến đang trình bày bản thiết kế resort sinh thái năm sao tại Phú Quốc trước hai mươi lãnh đạo tập đoàn BĐS Thành Phát.

"Resort EcoVilla không chặt một cây rừng ngập mặn nào," Yến chiếu mô hình 3D lên màn hình. "Hai mươi villa nằm giữa tán cây, nối bằng lối đi gỗ nâng cao. Nền móng dùng cọc xoắn thay vì đổ bê tông, nước thải xử lý bằng hệ thống đất ngập nhân tạo. Zero waste, zero carbon."

Thiết kế tuyệt đẹp: villa mái lá dừa uốn cong như sóng biển, tường kính nhìn ra rừng ngập mặn, hồ bơi sinh thái lọc bằng thực vật thay vì chlorine.

Nhưng Nguyễn Đức Thành — Chủ tịch Thành Phát, năm mươi tuổi, gương mặt xương xẩu — không cười.

"Cô Yến, hai mươi villa thì bán cho ai? Tôi muốn hai trăm phòng. Bê tông, thép, điều hòa trung tâm, pool bar, karaoke. Du khách Trung Quốc và Hàn Quốc muốn khách sạn năm sao, không muốn ngủ trong lều."

"Nhưng anh Thành, bản thiết kế đã được phê duyệt bởi UNESCO vì bảo tồn rừng ngập mặn—"

"UNESCO không trả tiền thuê đất!" Thành gầm lên. Bên cạnh, đối tác Hàn Quốc Lee Sang-ho gật gù: "We need volume, not trees."

Thành ném bản hợp đồng thiết kế lên bàn: "Hủy. Tôi thuê công ty kiến trúc Hàn Quốc thiết kế lại. Bê tông, hai trăm phòng, tối đa revenue per square meter."

"Anh sẽ phá rừng ngập mặn?" Yến đứng dậy, mặt đỏ bừng. "Rừng đó bảo vệ bờ biển, nuôi dưỡng hệ sinh thái cả vùng!"

"Cô lo chuyện cây cối, tôi lo chuyện tiền. Bảo vệ thu lại laptop và file thiết kế. Hợp đồng hủy, cô về đi."

Yến bước ra khỏi Landmark 81, tay siết chặt USB — bản backup cuối cùng của thiết kế EcoVilla. Cô nhìn xuống sông Sài Gòn lấp lánh dưới nắng trưa.

"Anh Thành, anh phá rừng để xây bê tông. Còn tôi sẽ xây resort mà rừng là nền tảng."

Trong đầu cô, bản thiết kế vẫn sống — hoàn hảo hơn bao giờ hết."""),

("Chương 2: Resort Mái Lá Giữa Rừng", """Yến bán căn hộ ở quận 2, gom được hai tỷ đồng. Cô tìm đến Phú Yên — nơi có bãi biển đẹp hoang sơ mà chưa bị BĐS tàn phá.

Cô thuê năm hecta đất rừng tràm ven biển, ký hợp đồng với UBND xã cam kết: không chặt một cây, không đổ bê tông, không xả thải ra biển.

Bốn tháng xây dựng, Yến thiết kế và giám sát thi công mọi thứ. Năm villa mái lá dừa, nền gỗ nâng cao một mét rưỡi, tường tre đan, nội thất từ vật liệu tái chế. Mỗi villa có tên một loài chim biển: Bồ Nông, Hải Âu, Nhạn, Cò, Vạc.

Khu resort nhỏ nhắn, giản dị, nhưng đẹp đến nghẹt thở — nằm giữa rừng tràm, nhìn ra biển xanh ngắt, nghe tiếng sóng vỗ và chim hót suốt ngày.

Yến đặt tên: EcoNest — tổ chim sinh thái.

Khách đầu tiên đến là một cặp vợ chồng Pháp, travel blogger có năm trăm nghìn followers. Họ ở ba đêm, quay video, đăng lên YouTube.

"EcoNest is the most beautiful eco-resort we've ever stayed in. No concrete, no plastic, just pure nature. Vietnam is leading sustainable tourism."

Video đạt hai triệu lượt xem. Booking tràn ngập. EcoNest kín phòng ba tháng liên tiếp."""),

("Chương 3: Condé Nast Traveler Và Giải Thưởng", """Sáu tháng sau khai trương, Condé Nast Traveler — tạp chí du lịch uy tín nhất thế giới — đưa EcoNest vào danh sách "Top 50 Best New Hotels in the World."

Ảnh EcoNest lên bìa tạp chí: villa mái lá dừa giữa rừng tràm, ánh hoàng hôn chiếu xuyên tán lá. Caption: "The future of luxury is not marble and gold — it's leaves and wind."

Đơn đặt phòng đến từ khắp thế giới. Giá mỗi đêm: mười lăm triệu đồng — đắt hơn nhiều resort năm sao bê tông, nhưng khách vẫn xếp hàng chờ sáu tháng.

Trong khi đó, resort bê tông của Thành Phát tại Phú Quốc khai trương ồn ào rồi ế khách. Du khách quốc tế không muốn ở khách sạn bê tông giống hệt mọi nơi — họ muốn trải nghiệm authentic, unique, sustainable. EcoNest có tất cả."""),

("Chương 4: Thành Phát Phản Công", """Thành thuê luật sư kiện Yến: "sử dụng thiết kế bị hủy bỏ thuộc sở hữu trí tuệ của Thành Phát." Nhưng luật sư Yến chứng minh: thiết kế EcoNest hoàn toàn khác EcoVilla — vật liệu, cấu trúc, quy mô, vị trí đều mới. Đơn kiện bị bác.

Thành chuyển sang chiêu bẩn: thuê troll đăng review 1 sao trên TripAdvisor và Google, nội dung: "Resort nhà lá, muỗi cắn, nhà vệ sinh tạm bợ."

Nhưng khách thật — những người đã ở EcoNest — phản bác bằng review 5 sao kèm ảnh thật. Điểm TripAdvisor: 4.9/5, cao nhất Việt Nam.

Yến không phản ứng, không chiến tranh PR. Cô chỉ làm một việc: mời hai mươi travel blogger quốc tế ở miễn phí ba đêm, tự đánh giá. Kết quả: mười chín trên hai mươi viết bài ca ngợi."""),

("Chương 5: Mô Hình EcoNest Nhân Rộng", """Hai năm sau, Yến mở rộng: EcoNest Phú Yên, EcoNest Ninh Thuận, EcoNest Kon Tum — mỗi nơi một hệ sinh thái khác nhau, thiết kế hòa quyện với tự nhiên.

Mô hình EcoNest được UN World Tourism Organization (UNWTO) vinh danh là "Best Practice in Sustainable Tourism." Các nước Thái Lan, Indonesia, Philippines gửi phái đoàn đến học tập.

Doanh thu chuỗi EcoNest: tám mươi tỷ đồng mỗi năm. Tỷ suất lợi nhuận bốn mươi phần trăm — cao gấp đôi resort bê tông thông thường, vì chi phí xây dựng thấp và giá phòng premium."""),

("Chương 6: Đế Chế Du Lịch Xanh", """EcoNest Hospitality Group huy động vốn Series A từ quỹ khí hậu Green Climate Fund — năm mươi triệu đô để mở rộng ra mười quốc gia ASEAN.

Yến trở thành gương mặt trang bìa Forbes Asia: "The Vietnamese Architect Who Proved Luxury Can Be Green." Cô được mời TED Talk tại Vancouver, bài nói "Building Without Destroying" đạt năm triệu lượt xem."""),

("Chương 7: Bà Ngoại Và Ngôi Nhà Lá", """Yến yêu kiến trúc sinh thái vì bà ngoại. Bà Trương Thị Hoa, tám mươi tuổi, sống trong ngôi nhà lá dừa ở Bến Tre — mát mẻ suốt mùa hè, ấm áp mùa mưa, không cần điều hòa.

"Con ơi, nhà lá mát hơn nhà tường. Lá thở, tường không thở," bà nói khi Yến nhỏ.

Câu nói đó thành triết lý thiết kế: "kiến trúc phải thở." Mỗi villa EcoNest đều có hệ thống thông gió tự nhiên dựa trên nguyên lý nhà lá miền Tây, kết hợp mô phỏng khí động học bằng phần mềm CFD.

Bà Hoa giờ sống trong villa đẹp nhất EcoNest Phú Yên — nhưng vẫn giữ chiếc chổi lá dừa tự đan để quét sân mỗi sáng."""),

("Chương 8: Thành Phát Phá Sản", """Resort bê tông Thành Phát tại Phú Quốc phá sản sau hai năm — ế khách, nợ ngân hàng một nghìn tỷ. Rừng ngập mặn bị phá, bờ biển xói lở, chính quyền buộc Thành bồi thường phục hồi môi trường.

Thành bán tháo tài sản, nộp đơn phá sản cá nhân. Lee Sang-ho rút về Hàn Quốc.

Yến không hả hê. Cô dùng tiền của EcoNest tài trợ chương trình phục hồi rừng ngập mặn Phú Quốc — trồng lại một trăm nghìn cây trên chính mảnh đất mà Thành đã phá."""),

("Chương 9: Giải Pritzker Đề Cử", """Yến được đề cử Giải Pritzker — "Nobel kiến trúc" — cho công trình kiến trúc sinh thái. Dù chưa thắng giải, đề cử đã là lịch sử: kiến trúc sư Việt Nam đầu tiên, kiến trúc sư dưới ba mươi lăm tuổi trẻ nhất được đề cử.

Ban giám khảo Pritzker nhận xét: "Trương Hải Yến chứng minh rằng kiến trúc vĩ đại không cần phá hủy tự nhiên, mà có thể sinh ra từ tự nhiên."

Yến nói: "Tôi không thiết kế resort. Tôi thiết kế cách con người sống hòa hợp với rừng." """),

("Chương 10: Trở Về Rừng Tràm", """Một năm sau, Yến đứng trên lối gỗ giữa rừng tràm EcoNest Phú Yên — resort đầu tiên, nơi bắt đầu tất cả.

Rừng tràm vẫn xanh ngắt, chim vẫn hót, sóng vẫn vỗ. Không một cây nào bị chặt. Resort tồn tại giữa rừng như một phần của rừng — không phải kẻ xâm lược.

Yến nắm tay chồng — Lê Hoàng Nam, kỹ sư môi trường người Yến gặp trong chuyến phục hồi rừng ngập mặn Phú Quốc.

"Em nhớ ngày anh Thành xé hợp đồng không?" cô hỏi.

"Nhớ. Ngày xấu nhất đời em."

"Không. Ngày tốt nhất. Vì nếu không bị xé, em đã xây resort cho người khác, trên đất người khác, theo ý người khác. Giờ em xây cho mình, giữa rừng mình yêu."

Cô ngồi xuống bậc gỗ, nghe rừng tràm xào xạc trong gió chiều. Ở đâu đó trên cành cây, một con bồ nông đang xây tổ — giống hệt biểu tượng trên logo EcoNest.

Thiên nhiên không bao giờ phản bội ai yêu nó thật lòng."""),
]

# ═══════════════════════════════════════════════════════════════════════════════
# STORY 11: KỸ SƯ PCCC
# ═══════════════════════════════════════════════════════════════════════════════

S11_TITLE = "BỊ ĐỔ TỘI LÀM CHÁY NHÀ MÁY, TÔI DÙNG LOG HỆ THỐNG PCCC VẠCH TRẦN ÂM MƯU BẢO HIỂM 800 TỶ"
S11_AUTHOR = "Phan Đình Khoa"
S11_COVER = "base_cover_45.png"
S11_INTRO = """<p><strong>"Mười năm tôi thiết kế hệ thống PCCC cho sáu mươi nhà máy, không để xảy ra một vụ cháy nào. Đổi lại, khi nhà máy cố tình phóng hỏa để lấy bảo hiểm, họ đổ tội cho tôi thiết kế sai hệ thống."</strong></p>
<p>Phan Đình Khoa, kỹ sư phòng cháy chữa cháy hàng đầu Việt Nam, bị chủ nhà máy Vũ Hoàng Long và Trưởng phòng Bảo hiểm Trần Thị Mỹ Hạnh đổ tội khi nhà máy bị "cháy" để lấy bồi thường tám trăm tỷ đồng.</p>
<p>Bị truy tố, bị bắt tạm giam, Khoa dùng dữ liệu log hệ thống PCCC IoT do chính anh cài đặt để vạch trần âm mưu phóng hỏa, giải cứu bản thân và thành lập hãng tư vấn PCCC công nghệ đầu tiên tại Việt Nam.</p>"""

S11_CHAPTERS = [
("Chương 1: Đêm Nhà Máy Cháy", """Hai giờ mười lăm phút sáng, điện thoại Phan Đình Khoa reo. Màn hình hiện thông báo từ hệ thống PCCC IoT: "CẢNH BÁO CHÁY — Nhà máy Thiên Long Plastics, KCN Bình Dương. Sector C, kho nguyên liệu."

Khoa lao xe từ quận 7 đến Bình Dương trong bốn mươi phút. Khi đến nơi, nhà máy đã chìm trong biển lửa — ngọn lửa cao hai mươi mét, khói đen cuồn cuộn.

Khoa nhìn đám cháy bằng con mắt chuyên gia mười năm: cháy bắt đầu từ kho nguyên liệu nhựa PVC, lan nhanh bất thường ra toàn bộ sector C trong vòng mười lăm phút. Hệ thống sprinkler tự động — thứ anh thiết kế — không kích hoạt.

Bất thường. Hệ thống sprinkler anh thiết kế có độ tin cậy chín mươi chín phần trăm. Mười năm, sáu mươi nhà máy, chưa bao giờ lỗi.

Sáng hôm sau, cảnh sát PCCC triệu tập Khoa. Chủ nhà máy Vũ Hoàng Long — mặt đen sì vì khói, nhưng mắt lại bình tĩnh đáng ngờ — tố cáo: "Kỹ sư Phan Đình Khoa thiết kế hệ thống PCCC sai tiêu chuẩn, sprinkler không hoạt động, gây thiệt hại tám trăm tỷ đồng."

Trưởng phòng Bảo hiểm Mỹ Hạnh cung cấp "bằng chứng": báo cáo kiểm tra hệ thống PCCC ghi rõ nhiều lỗi kỹ thuật, ký bởi kỹ sư kiểm định độc lập.

"Bản kiểm tra này giả mạo!" Khoa hét lên. "Hệ thống của tôi được kiểm định bởi Cục PCCC, đạt chuẩn NFPA 13! Tôi có giấy chứng nhận!"

"Giấy chứng nhận cấp hai năm trước. Kể từ đó, hệ thống có thể xuống cấp," Long nói bình tĩnh.

Khoa bị bắt tạm giam ba mươi ngày, khởi tố tội "vi phạm quy định về phòng cháy chữa cháy gây hậu quả nghiêm trọng." Nếu bị kết tội, anh đối mặt mười năm tù.

Nhưng trong đầu Khoa, một chi tiết nhảy múa: hệ thống sprinkler không kích hoạt. Anh thiết kế nó. Anh biết nó không tự hỏng. Ai đó đã tắt nó."""),

("Chương 2: Log Hệ Thống Không Nói Dối", """Trong trại tạm giam, Khoa nhớ ra: hệ thống PCCC IoT mà anh cài đặt cho nhà máy Thiên Long có một tính năng ẩn — cloud logging. Mọi dữ liệu cảm biến khói, nhiệt độ, trạng thái van sprinkler đều được gửi realtime về server cloud của anh.

Long không biết tính năng này. Khi mua hệ thống, Khoa cài đặt cloud backup như tiêu chuẩn cho mọi dự án — "bảo hiểm" cho chính mình.

Khoa gọi luật sư, yêu cầu truy xuất log cloud. Dữ liệu hiện lên rõ ràng:

Lúc 01:47 — cảm biến khói sector C kích hoạt (bình thường). Lúc 01:48 — van sprinkler sector C nhận lệnh kích hoạt (bình thường). Lúc 01:48:03 — van sprinkler bị override manual OFF từ bảng điều khiển chính. Người dùng override: tài khoản admin factory, password sử dụng lần cuối bởi IP nội bộ nhà máy.

Ai đó đã tắt sprinkler thủ công đúng ba giây sau khi nó chuẩn bị phun nước.

Hệ thống hoạt động hoàn hảo. Nó BỊ TẮT.

Luật sư nộp log cloud cho cơ quan điều tra. Giám định kỹ thuật xác nhận: log không thể giả mạo — dữ liệu mã hóa SHA-256, timestamp UTC, lưu trên AWS với audit trail.

Cơ quan điều tra chuyển hướng: từ Khoa sang chủ nhà máy Long.

Khoa được tại ngoại sau bảy ngày — thay vì ba mươi ngày dự kiến."""),

("Chương 3: Âm Mưu Bảo Hiểm 800 Tỷ", """Điều tra mở rộng phát hiện: Long mua bảo hiểm cháy nổ tám trăm tỷ đồng cho nhà máy — gấp ba giá trị thực — ba tháng trước khi cháy. Mỹ Hạnh, Trưởng phòng bảo hiểm, phê duyệt hợp đồng bất thường này mà không thẩm định.

Long thuê một nhân viên bảo vệ phóng hỏa bằng xăng công nghiệp trong kho PVC, rồi tắt sprinkler từ bảng điều khiển để lửa lan nhanh. Kế hoạch hoàn hảo — trừ việc Long không biết hệ thống có cloud logging.

Long bị bắt, Mỹ Hạnh bị bắt, nhân viên bảo vệ khai nhận. Khoa được minh oan hoàn toàn.

Tin tức bùng nổ trên truyền thông: "Kỹ sư PCCC bị vu oan phóng hỏa, dùng log IoT vạch trần âm mưu bảo hiểm 800 tỷ." """),

("Chương 4: Thành Lập FireTech", """Sau khi minh oan, Khoa thành lập FireTech — hãng tư vấn PCCC công nghệ cao, chuyên cung cấp hệ thống PCCC IoT với cloud monitoring và AI phát hiện cháy sớm.

Slogan: "Fire doesn't lie. Data doesn't lie."

Sáu mươi nhà máy mà Khoa từng thiết kế — tất cả đều liên hệ ký hợp đồng nâng cấp lên hệ thống IoT mới. Doanh thu năm đầu: hai mươi tỷ đồng.

Hệ thống FireTech dùng AI phân tích dữ liệu cảm biến để phát hiện nguy cơ cháy trước hai mươi phút — sớm hơn cảm biến khói thông thường, cho phép sơ tán và xử lý kịp thời."""),

("Chương 5: Cứu Nhà Máy Samsung", """FireTech nhận hợp đồng lớn nhất: lắp đặt hệ thống PCCC IoT cho nhà máy Samsung Thái Nguyên — nhà máy điện thoại lớn nhất thế giới.

Ba tháng sau lắp đặt, hệ thống AI phát hiện bất thường nhiệt độ trong kho pin lithium — cảnh báo trước hai mươi hai phút. Đội PCCC Samsung can thiệp kịp thời, ngăn chặn vụ nổ pin có thể gây thiệt hại hàng nghìn tỷ.

Samsung cấp giấy khen và mở rộng hợp đồng ra toàn bộ hệ thống nhà máy Samsung tại Việt Nam. FireTech trở thành nhà cung cấp PCCC công nghệ cho các tập đoàn FDI lớn nhất."""),

("Chương 6: Mở Rộng Ra ASEAN", """FireTech huy động vốn Series A từ quỹ Temasek Singapore, hai mươi triệu đô. Mở rộng sang Thái Lan, Indonesia, Philippines — các quốc gia có tỷ lệ cháy nhà máy cao.

Đội ngũ ba trăm kỹ sư. Đã bảo vệ hơn năm trăm nhà máy. Ngăn chặn mười bảy vụ cháy tiềm tàng nhờ AI cảnh báo sớm.

Khoa được vinh danh "ASEAN Young Entrepreneur of the Year" — kỹ sư PCCC đầu tiên nhận danh hiệu doanh nhân."""),

("Chương 7: Người Cha Cứu Hỏa", """Khoa theo nghề PCCC vì bố. Ông Phan Đình Lực, lính cứu hỏa Công an TP.HCM, hy sinh khi cứu ba em nhỏ khỏi đám cháy chung cư Carina năm 2018.

"Bố cứu người bằng tay. Con cứu người bằng công nghệ," Khoa viết trong bản thảo tự truyện.

FireTech tài trợ trang bị PCCC cho một nghìn chung cư cũ tại TP.HCM và Hà Nội — miễn phí. Logo FireTech gắn hình mũ cứu hỏa của bố Khoa.

Mẹ Khoa, bà Nguyễn Thị Lan Anh, dự lễ khai trương trụ sở mới. Bà đặt tay lên tấm bảng ghi tên công ty, mắt ướt: "Bố con tự hào lắm." """),

("Chương 8: Long Và Hạnh Lĩnh Án", """Tòa án tuyên: Vũ Hoàng Long hai mươi năm tù về tội hủy hoại tài sản, lừa đảo bảo hiểm, và vu khống. Trần Thị Mỹ Hạnh mười hai năm tù về tội đồng phạm.

Tám trăm tỷ tiền bảo hiểm không được chi trả. Bảo hiểm siết tài sản Long để bồi thường. Nhà máy Thiên Long phá sản.

Khoa không đến tòa ngày tuyên án. Anh đang lắp đặt hệ thống PCCC miễn phí cho trường mầm non ở Thủ Đức."""),

("Chương 9: Giải Thưởng An Toàn Cháy Nổ Toàn Cầu", """FireTech nhận giải "Global Fire Safety Innovation Award" tại NFPA Conference ở Las Vegas — giải thưởng PCCC danh giá nhất thế giới.

"Tôi bị bỏ tù vì lửa. Tôi thoát tù nhờ dữ liệu. Từ đó, tôi dùng dữ liệu để chiến đấu với lửa," Khoa nói trước bốn nghìn chuyên gia PCCC toàn cầu.

Hệ thống FireTech AI được NFPA đưa vào giáo trình đào tạo toàn cầu — tiêu chuẩn mới cho PCCC thế kỷ 21."""),

("Chương 10: Trở Lại Nhà Máy Cũ", """FireTech mua lại mặt bằng nhà máy Thiên Long phá sản, biến thành trung tâm đào tạo PCCC quốc gia — nơi huấn luyện lính cứu hỏa và kỹ sư PCCC miễn phí.

Khoa đứng giữa nhà máy đã được tái thiết, nhìn hệ thống sprinkler mới sáng bóng trên trần.

"Sprinkler này sẽ không bao giờ bị tắt nữa," anh nói với học viên lính cứu hỏa trẻ. "Vì giờ nó kết nối cloud, và tôi đang theo dõi nó hai mươi bốn trên bảy."

Trên tường trung tâm, Khoa treo ảnh bố — người lính cứu hỏa mặt đen khói, mỉm cười, tay bế em bé vừa cứu từ đám cháy.

Dòng chữ dưới ảnh: "Anh hùng cứu hỏa Phan Đình Lực — Người dạy con trai rằng lửa không đáng sợ, sợ chỉ khi ta bỏ cuộc." """),
]

# ═══════════════════════════════════════════════════════════════════════════════
# STORY 12: SINH VIÊN ROBOTICS
# ═══════════════════════════════════════════════════════════════════════════════

S12_TITLE = "BỊ GẠCH TÊN KHỎI ĐỘI TUYỂN ROBOT, TÔI TỰ CHẾ ROBOT THẮNG GIẢI THẾ GIỚI KHIẾN THẦY CŨ CÂM LẶNG"
S12_AUTHOR = "Đặng Minh Quân"
S12_COVER = "base_cover_46.png"
S12_INTRO = """<p><strong>"Hai năm tôi thiết kế và lập trình robot cứu hộ tự hành — thức trắng hàng trăm đêm trong lab sinh viên. Đổi lại, giáo sư gạch tên tôi khỏi đội tuyển ba ngày trước giải đấu quốc tế, ghi tên con trai mình vào."</strong></p>
<p>Đặng Minh Quân, sinh viên cơ điện tử năm cuối Đại học Bách Khoa Hà Nội, bị GS hướng dẫn Lê Đức Hải và Trưởng nhóm Cao Trung Hiếu loại khỏi đội tuyển robot quốc gia trước giải FIRST Global Challenge.</p>
<p>Mất đội, mất lab, mất mentor. Quân tự tay chế robot từ linh kiện phế liệu trong phòng trọ sinh viên, đăng ký thi đấu với tư cách đội tuyển độc lập — và tạo ra kỳ tích mà cả thế giới robotics phải ngả mũ.</p>"""

S12_CHAPTERS = [
("Chương 1: Bị Gạch Tên", """Lab Robotics tầng bốn, Khoa Cơ Điện tử, Đại học Bách Khoa Hà Nội. Đặng Minh Quân đang calibrate cảm biến lidar trên robot cứu hộ RescueBot V3 — đứa con tinh thần mà anh đã phát triển hai năm ròng.

RescueBot V3 là robot tự hành có khả năng di chuyển trên địa hình khắc nghiệt, phát hiện nạn nhân bằng camera hồng ngoại và sensor CO2, và giao tiếp với trung tâm chỉ huy qua mesh network. Thiết kế của Quân — từ khung cơ khí, mạch điện tử, đến thuật toán SLAM navigation — tất cả.

Ba ngày nữa, đội tuyển robot Bách Khoa sẽ bay đến Geneva dự FIRST Global Challenge — giải đấu robot quốc tế lớn nhất thế giới.

"Quân, lên phòng thầy Hải." Tin nhắn Zalo.

GS Lê Đức Hải, năm mươi hai tuổi, Trưởng bộ môn Cơ điện tử, ngồi sau bàn. Bên cạnh là Cao Trung Hiếu — Trưởng nhóm robot, con trai GS Hải, sinh viên năm ba, tay nghề tầm thường nhưng luôn đứng tên "project leader."

"Quân, do giới hạn visa và ngân sách, đội tuyển chỉ đưa năm người đi Geneva. Tên em bị rút khỏi danh sách."

"Nhưng thầy, em thiết kế toàn bộ robot! Em code toàn bộ firmware! Không có em, không ai vận hành được RescueBot!"

"Hiếu sẽ vận hành. Thầy đã training Hiếu cách điều khiển."

"Training trong ba ngày? Em mất hai năm phát triển hệ thống! Hiếu thậm chí không biết đọc log sensor!"

GS Hải đứng dậy, giọng lạnh: "Đây là quyết định của ban tổ chức đội tuyển. Em không phải thành viên nữa. Trả lại badge lab và chìa khóa phòng thiết bị."

Quân nhìn Hiếu — cậu ta ngồi im, tránh mắt, nhưng khóe miệng khẽ nhếch. Quân hiểu: GS Hải muốn con trai mình đứng trên sân khấu quốc tế, còn Quân — sinh viên nghèo từ Hải Dương, không gia thế, không quan hệ — chỉ là "nhân công" phía sau.

Quân đặt badge và chìa khóa lên bàn. Nhưng trước khi đi, anh lấy từ trong túi một chiếc USB nhỏ.

"Đây là firmware RescueBot v3.2, bản cuối cùng em viết. Không có nó, robot chỉ là đống sắt. Em giữ bản gốc, các thầy dùng bản trên máy — nhưng bản đó là v3.0, thiếu module obstacle avoidance và sensor fusion."

Quân bước ra, đóng cửa lab. Tiếng cửa đóng vang trong hành lang vắng như tiếng mõ gõ xuống kết thúc một chương."""),

("Chương 2: Robot Phế Liệu Trong Phòng Trọ", """Phòng trọ mười lăm mét vuông ở ngõ Tạ Quang Bửu, giá hai triệu rưỡi một tháng. Quân biến nửa phòng thành lab: bàn gỗ cũ, mỏ hàn, oscilloscope second-hand, và một thùng linh kiện phế liệu mua từ chợ Nhật Tảo.

Anh quyết định: tự chế robot mới, đăng ký thi đấu FIRST Global Challenge với tư cách đội tuyển độc lập — "Team Vietnam Independent."

Vấn đề: ngân sách gần zero. Robot chính thức của Bách Khoa tốn năm trăm triệu đồng linh kiện. Quân chỉ có tám triệu tiền để dành từ dạy thêm.

Nhưng Quân có thứ quý hơn tiền: kiến thức. Hai năm phát triển RescueBot dạy anh cách tối ưu hóa mọi thứ.

Khung robot: ống nhôm tái chế từ giàn giáo xây dựng phế liệu, cắt bằng cưa tay. Motor: motor xe đạp điện cũ, mua ở chợ Nhật Tảo giá ba trăm nghìn mỗi cái. Cảm biến: camera Raspberry Pi giá năm trăm nghìn thay cho lidar năm mươi triệu — bù bằng thuật toán computer vision mà Quân tự viết.

"Robot giàu dùng linh kiện đắt tiền. Robot nghèo dùng thuật toán thông minh," Quân tự nhủ khi hàn mạch lúc ba giờ sáng.

Hai tuần, robot hoàn thành. Quân đặt tên: Rồng Việt. Nhìn thô sơ, xấu xí, đầy vết hàn — nhưng chạy mượt mà, navigation chính xác, và có khả năng leo dốc ba mươi độ mà robot đội Bách Khoa không làm được.

Quân đăng ký FIRST Global, nộp video demo. Ban tổ chức chấp nhận — đội một người, robot phế liệu, nhưng kỹ thuật khiến họ ấn tượng."""),

("Chương 3: Geneva — Rồng Việt Gây Sốc", """Geneva, Thụy Sĩ. FIRST Global Challenge quy tụ một trăm chín mươi đội từ một trăm chín mươi quốc gia. Mỗi đội có năm đến mười thành viên, robot trị giá hàng trăm triệu, được tài trợ bởi các tập đoàn lớn.

Team Vietnam Independent: một người, Đặng Minh Quân, mang theo Rồng Việt trong vali — vì robot nhỏ đủ xếp gọn.

Khi Quân lắp robot trong khu vực pit, các đội khác nhìn Rồng Việt bằng ánh mắt tò mò xen lẫn thương hại: khung nhôm tái chế, motor xe đạp, camera Raspberry Pi dán bằng băng keo.

Đội Bách Khoa chính thức cũng có mặt — RescueBot V3, bóng loáng, hiện đại, do GS Hải đích thân dẫn đội. Hiếu đeo badge "Project Leader."

Vòng đấu loại: nhiệm vụ robot thu gom "nạn nhân" (banh tennis) trên địa hình giả lập đổ nát, di chuyển về vùng an toàn. Robot phải tự hành, không điều khiển từ xa.

Rồng Việt vào trận đầu tiên. Motor xe đạp gầm lên, camera quét 360 độ, thuật toán SLAM của Quân xử lý realtime — robot tìm và thu gom bảy banh trong ba phút, nhanh nhất bảng.

Khán đài ồ lên. Trọng tài kiểm tra: robot tự hành hoàn toàn, không vi phạm. Rồng Việt đứng đầu bảng A vòng loại.

RescueBot V3 của đội Bách Khoa gặp sự cố: module obstacle avoidance hoạt động không ổn (vì Hiếu dùng firmware v3.0 thiếu module mà Quân viết). Robot va vào tường hai lần, bị trừ điểm. Đội Bách Khoa đứng thứ mười sáu.

GS Hải ngồi ở khán đài, mặt trắng bệch khi nhìn Rồng Việt — robot phế liệu do sinh viên mà ông đuổi — nghiền nát mọi đối thủ."""),

("Chương 4: Chung Kết — David Đánh Bại Goliath", """Rồng Việt vào chung kết, đối đầu với đội MIT (Mỹ), đội ETH Zurich (Thụy Sĩ), và đội KAIST (Hàn Quốc) — những đội có robot trị giá hàng trăm triệu, thiết kế bởi phòng lab hàng đầu thế giới.

Nhiệm vụ chung kết khó hơn: địa hình phức tạp với dốc, hố, và chướng ngại vật di động. Robot phải tìm, nhận diện, và giải cứu "nạn nhân" trong năm phút.

Robot MIT dùng lidar Velodyne giá ba nghìn đô. ETH Zurich dùng depth camera Intel RealSense. KAIST dùng sensor array mười hai kênh.

Rồng Việt dùng camera Raspberry Pi năm trăm nghìn đồng — và thuật toán vision của Quân.

Bốn robot khởi động đồng thời. MIT và ETH nhanh chóng vượt lên, KAIST bám sát. Rồng Việt chậm hơn vì motor yếu — nhưng algorithm của Quân tối ưu đường đi, không thừa một bước.

Ba phút ba mươi giây: MIT thu bảy nạn nhân, ETH sáu, KAIST năm, Rồng Việt bốn. Quân ở phía sau.

Nhưng ở phút thứ tư, khu vực khó nhất — dốc nghiêng ba mươi lăm độ với chướng ngại vật di động — robot MIT trượt bánh, ETH bị kẹt, KAIST lật nghiêng. Rồng Việt — với motor xe đạp momen xoắn lớn và trọng tâm thấp — bò lên dốc vững chãi, thu thêm năm nạn nhân.

Kết quả: Rồng Việt chín nạn nhân, MIT tám, ETH bảy, KAIST năm.

"CHAMPION: TEAM VIETNAM INDEPENDENT — Đặng Minh Quân!" MC hét vào micro.

Hội trường hai nghìn người đứng dậy. Standing ovation cho chàng sinh viên Việt Nam một mình, robot phế liệu, thắng MIT và ETH Zurich.

Quân đứng trên sân khấu, ôm Rồng Việt — robot xấu xí bằng nhôm tái chế — và khóc. Không phải khóc vì vui, mà khóc vì nhớ những đêm hàn mạch một mình trong phòng trọ mười lăm mét vuông."""),

("Chương 5: Viral Toàn Cầu", """Video Rồng Việt chiến thắng đạt năm mươi triệu lượt xem trên YouTube. Câu chuyện "sinh viên nghèo bị đuổi khỏi đội, tự chế robot phế liệu thắng giải thế giới" trở thành hiện tượng toàn cầu.

CNN, BBC, NHK đồng loạt phỏng vấn. Elon Musk tweet: "This kid is the real deal. Vietnam has incredible talent." Tweet đó đạt hai trăm nghìn like.

Tại Hà Nội, GS Hải đóng cửa phòng làm việc. Đội tuyển Bách Khoa mà ông dẫn về tay không — không giải, không danh dự, chỉ có sự nhục nhã khi sinh viên bị đuổi thắng giải thế giới.

Hiếu xóa mọi bài đăng liên quan đến robot trên mạng xã hội. Cậu ta biết: cái tên "Cao Trung Hiếu" giờ gắn liền với "kẻ cướp chỗ của thiên tài." """),

("Chương 6: RoboViet Ra Đời", """MIT gửi thư mời Quân theo học thạc sĩ, học bổng toàn phần. Nhưng Quân từ chối.

"Tôi ở Việt Nam. Tôi muốn xây robot cho nông dân Việt Nam, không phải cho phòng lab MIT."

Quân thành lập RoboViet — startup robotics, chuyên sản xuất robot giá rẻ cho nông nghiệp và cứu hộ thảm họa. Vốn đầu tư từ quỹ Sequoia Southeast Asia, mười triệu đô.

Robot cứu hộ RoboViet Rescue được trang bị cho mười hai đội cứu hộ thảm họa, đã tham gia cứu nạn trong ba trận lũ lụt miền Trung, phát hiện và cứu hai mươi mốt người."""),

("Chương 7: Ước Mơ Của Cậu Bé Hải Dương", """Quân lớn lên ở xã nghèo tại Hải Dương. Bố mẹ làm công nhân nhà máy, thu nhập bốn triệu mỗi tháng cho cả gia đình.

Lúc mười tuổi, Quân tháo chiếc quạt hỏng của nhà, lắp lại thành quạt chạy ngược — gió thổi ngược lên trần thay vì xuống đất. Bố không mắng, chỉ cười: "Con giỏi tháo lắp, nhưng lần sau nhớ lắp đúng chiều."

Từ đó, Quân tháo lắp mọi thứ: đồng hồ, radio, nồi cơm điện. Năm mười lăm, anh chế robot tưới cây tự động cho vườn rau nhà bằng motor từ máy giặt cũ.

RoboViet có chương trình "Robot Nhí" — dạy lập trình và chế tạo robot miễn phí cho trẻ em nông thôn. Logo: một chiếc quạt quay ngược — kỷ vật tuổi thơ của Quân."""),

("Chương 8: GS Hải Mất Chức", """Vụ bê bối đội tuyển robot khiến Đại học Bách Khoa mở điều tra nội bộ. Kết luận: GS Hải vi phạm quy chế đào tạo khi thay đổi thành viên đội tuyển vì lý do cá nhân, gây tổn hại uy tín trường.

GS Hải bị cách chức Trưởng bộ môn. Hiếu bỏ học giữa chừng, xấu hổ không dám đối mặt bạn bè.

Bách Khoa mời Quân trở lại với tư cách giảng viên thỉnh giảng khoa Cơ điện tử. Quân đồng ý — nhưng với điều kiện: mở lab robotics mở, bất kỳ sinh viên nào cũng được sử dụng, không phân biệt."""),

("Chương 9: Giải Edison Award", """RoboViet nhận giải Edison Award — giải thưởng sáng tạo danh giá nhất thế giới, đặt theo tên Thomas Edison — cho sản phẩm "Robot cứu hộ giá rẻ cho quốc gia đang phát triển."

"Thomas Edison nói: thiên tài là một phần trăm cảm hứng, chín mươi chín phần trăm mồ hôi. Tôi nói: thiên tài là một phần trăm linh kiện đắt tiền, chín mươi chín phần trăm thuật toán thông minh," Quân nói trước hai nghìn khách mời.

Rồng Việt — robot phế liệu chiến thắng FIRST Global — giờ được trưng bày tại Bảo tàng Khoa học và Công nghệ Smithsonian, Washington D.C."""),

("Chương 10: Quay Về Lab Tầng Bốn", """Quân trở lại lab tầng bốn Bách Khoa — nơi anh bị đuổi. Lab giờ mang tên "RoboViet Open Lab," trang bị đầy đủ, mở cửa hai mươi bốn trên bảy cho mọi sinh viên.

Anh đứng trước bàn nơi ngày xưa anh calibrate RescueBot, giờ có năm sinh viên năm nhất đang hì hục lắp robot đầu tiên.

"Thầy ơi, motor này mắc quá, em không mua nổi," một sinh viên nữ rụt rè.

Quân cười, mở ngăn tủ lấy ra một motor xe đạp điện cũ: "Motor này ba trăm nghìn ở chợ Nhật Tảo. Thầy dùng đúng loại này thắng giải thế giới. Robot giỏi không cần đắt tiền, chỉ cần người chế nó đủ giỏi."

Sinh viên nhận motor, mắt sáng rực — giống hệt ánh mắt Quân năm xưa khi lần đầu bước vào lab.

Quân quay ra cửa sổ, nhìn xuống sân trường Bách Khoa. Ở đâu đó dưới kia, có một cậu sinh viên nghèo đang mơ chế robot. Quân biết, vì anh từng là cậu sinh viên đó.

Rồng Việt phiên bản gốc — robot phế liệu xấu xí — giờ đứng trong tủ kính ở góc lab, bên cạnh chiếc cúp FIRST Global Challenge bằng vàng. Trên bảng tên ghi: "Rồng Việt — Budget: 8,000,000 VNĐ (~320 USD). Champion: FIRST Global Challenge 2027. Builder: Đặng Minh Quân, phòng trọ 15m²."

Tám triệu đồng. Ba trăm hai mươi đô. Đó là giá của một giấc mơ — khi giấc mơ được chế tạo bởi đôi tay đúng."""),
]

# ═══════════════════════════════════════════════════════════════════════════════
# ASSEMBLY & PUBLISHING
# ═══════════════════════════════════════════════════════════════════════════════

ALL_STORIES = [
    {"title": S9_TITLE, "author": S9_AUTHOR, "cover": S9_COVER, "intro": S9_INTRO, "chapters": S9_CHAPTERS},
    {"title": S10_TITLE, "author": S10_AUTHOR, "cover": S10_COVER, "intro": S10_INTRO, "chapters": S10_CHAPTERS},
    {"title": S11_TITLE, "author": S11_AUTHOR, "cover": S11_COVER, "intro": S11_INTRO, "chapters": S11_CHAPTERS},
    {"title": S12_TITLE, "author": S12_AUTHOR, "cover": S12_COVER, "intro": S12_INTRO, "chapters": S12_CHAPTERS},
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
    log("🚀 BATCH 3 LIVE PUBLISH — 4 STORIES (9-12)")
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

    log(f"\n🏁 BATCH 3 COMPLETE: {len(results)}/4 published")
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
