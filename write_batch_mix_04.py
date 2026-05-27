#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
write_batch_mix_04.py — Batch 4: 5 Truyện NGỌT / Healing (Stories 16-20)
=========================================================================
Template C: Tình cảm ấm áp → chữa lành → hạnh phúc
Tone: Dịu dàng, ấm lòng, lãng mạn nhẹ nhàng
Số chương random 8-13

Story 16: Quán cà phê chữa lành (9 ch) — cover 19
Story 17: Thầy giáo vùng cao (10 ch) — cover 20
Story 18: Bà ngoại và tiệm bánh (8 ch) — cover 21
Story 19: Bác sĩ về quê mở phòng khám miễn phí (11 ch) — cover 22
Story 20: Cô gái câm mở tiệm hoa (10 ch) — cover 23
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
# STORY 16: QUÁN CÀ PHÊ CHỮA LÀNH — 9 CHƯƠNG (Template C: Ngọt)
# ═══════════════════════════════════════════════════════════════════════════════

S16_TITLE = "QUÁN CÀ PHÊ NHỎ GIỮA HẺM SÂU SÀI GÒN — NƠI NGƯỜI LẠ ĐẾN KHÓC VÀ RA VỀ BÌNH YÊN"
S16_AUTHOR = "Hoàng Phúc An"
S16_COVER = "base_cover_19.png"
S16_INTRO = """<p>Trong con hẻm sâu ba mươi mét ở quận 3, Sài Gòn, có một quán cà phê không bảng hiệu. Không wifi, không menu, không nhạc. Chỉ có một chàng trai ba mươi tuổi pha cà phê bằng phin, lắng nghe bạn nói chuyện, và không phán xét.</p>
<p>"Quán Không Tên" — nơi người lạ đến khóc, người quen đến im lặng, và ai cũng ra về nhẹ nhõm hơn một chút.</p>"""

S16_CHAPTERS = [
("Chương 1: Quán Không Tên", """Hoàng Phúc An mở quán cà phê sau khi bỏ công việc marketing lương hai mươi triệu tại agency lớn nhất Sài Gòn. Lý do: "Tôi mệt mỏi vì bán đồ người ta không cần."

Quán nằm sâu trong hẻm, tổng diện tích mười lăm mét vuông. Bốn bàn gỗ cũ, tám chiếc ghế, một bàn pha cà phê, và một kệ sách nhỏ. Không wifi. Không bảng giá. Khách đến, An pha phin, đặt trước mặt, và nói: "Uống xong trả bao nhiêu cũng được."

Tuần đầu: không ai đến. Tuần thứ hai: một chị bán vé số ngồi ngoài hiên, An mang ra ly cà phê sữa đá miễn phí. Tuần thứ ba: chị đó dẫn bạn đến. Tháng thứ hai: quán bắt đầu có khách quen — không phải vì cà phê ngon, mà vì An biết lắng nghe.

"Quán này bán gì?"

"Bán sự im lặng. Và cà phê phin." """),

("Chương 2: Vị Khách Đầu Tiên Khóc", """Vị khách đặc biệt đầu tiên: một phụ nữ bốn mươi tuổi, trang điểm kỹ, tay xách túi hàng hiệu, ngồi vào bàn góc. An pha phin, đặt trước mặt, định quay đi.

"Em ơi, em có thể ngồi đây không?"

An ngồi xuống. Chị bắt đầu kể — giọng run, mắt đỏ: chồng ngoại tình ba năm, con gái mười hai tuổi biết nhưng không nói, chị giữ thể diện trước gia đình bằng lớp trang điểm và nụ cười giả.

"Chị không biết kể ai. Bạn bè chị ai cũng ghen tị vì chị 'hạnh phúc.' Mà chị không hạnh phúc."

An lắng nghe. Không khuyên, không phán xét, không đưa giải pháp. Chỉ nghe. Và khi chị khóc, An lấy khăn giấy đặt nhẹ trên bàn.

Chị khóc mười lăm phút, rồi lau mắt, uống hết ly cà phê, để lại năm trăm nghìn.

"Cà phê em không đáng năm trăm nghìn, chị."

"Nhưng lắng nghe thì vô giá." """),

("Chương 3: Bác Bảo Vệ Và Bức Thư Không Gửi", """Bác Nguyễn Văn Hải, sáu mươi hai tuổi, bảo vệ chung cư gần đó — đến quán mỗi sáng trước ca làm. Bác ngồi im, uống cà phê đen, không nói gì.

Sau hai tuần, An hỏi: "Bác uống một mình mỗi ngày, bác có muốn nói chuyện không?"

Bác Hải lấy từ túi áo ra bức thư viết tay — giấy đã ố vàng, nếp gấp nhàu. "Bác viết cho vợ bác. Bà ấy mất năm năm rồi. Bác viết mỗi ngày, nhưng không biết gửi cho ai."

An đọc bức thư — những lời yêu thương giản dị: "Bà ơi, hôm nay bác ăn cơm với cá kho, bà thích cá kho. Bác nhớ bà."

An đề nghị: "Bác muốn bác đọc to bức thư lên không? Cho bà nghe."

Bác Hải gật đầu. An đọc bức thư, giọng nhẹ, trong quán vắng lặng buổi sáng. Bác Hải nghe, nước mắt chảy trên khuôn mặt nhăn nheo.

Từ đó, mỗi sáng thứ Bảy, bác Hải đến quán, đưa An bức thư mới, và An đọc to — cho bà Hải nghe, ở đâu đó."""),

("Chương 4: Cậu Sinh Viên Và Cuộc Gọi Cuối Cùng", """Một đêm mưa, gần mười một giờ, có người gõ cửa quán (An ở ngay phía sau). Cậu sinh viên hai mươi tuổi, ướt sũng, mắt vô hồn.

"Em... em muốn uống cà phê."

An mở cửa, pha phin. Cậu ngồi im, hai tay ôm ly nóng. An nhìn cổ tay cậu — vết cắt mới, máu còn ri rỉ.

An không nói gì. Anh lấy hộp cứu thương, ngồi xuống cạnh cậu, nhẹ nhàng sát trùng và băng vết thương. Xong, anh ngồi xuống đối diện.

"Em muốn kể không?"

Cậu kể — áp lực học hành, bố mẹ ly hôn, bạn gái bỏ, nợ học phí. "Em không thấy lý do nào để sống nữa."

An im lặng mười giây, rồi nói: "Anh không có giải pháp cho em. Nhưng anh có một ly cà phê nóng, một cái ghế, và cả đêm nay. Em ngồi đây với anh được không?"

Cậu sinh viên ở lại đến bốn giờ sáng. Khi đi, cậu nói: "Anh ơi, cảm ơn anh."

"Ngày mai em quay lại nhé. Anh pha cho em ly nữa."

Cậu gật đầu. Và cậu quay lại — mỗi ngày, suốt sáu tháng, cho đến khi cậu ổn."""),

("Chương 5: Quán Cà Phê Thành Nơi Chữa Lành", """Tin đồn lan truyền: có quán cà phê ở hẻm quận 3 mà ông chủ lắng nghe bạn — thật sự lắng nghe. Không phán xét. Không quảng cáo. Không giải pháp. Chỉ nghe.

Khách đến đông hơn — nhưng An giữ quy tắc: tối đa tám người, không nhận quá. "Vì nếu quá đông, tôi không thể lắng nghe từng người."

Báo chí viết bài. VTV phỏng vấn. An từ chối tất cả quảng cáo: "Quán này không cần nổi tiếng. Quán này cần yên tĩnh."

Một nhà tâm lý học đến quán, nói với An: "Anh đang làm tâm lý trị liệu mà không biết."

"Tôi không trị liệu. Tôi chỉ pha cà phê và lắng nghe." """),

("Chương 6: Mẹ Và Bếp Lửa", """An mở quán vì mẹ. Bà Hoàng Thị Hạnh, bán xôi ở chợ Bến Thành bốn mươi năm.

"Mẹ ơi, sao mẹ bán xôi mà khách nào cũng kể chuyện với mẹ?"

"Vì mẹ lắng nghe. Người ta mua xôi không phải vì đói — mà vì cần ai đó hỏi 'hôm nay thế nào.' "

An mang triết lý đó vào quán cà phê: không bán cà phê — bán câu hỏi "hôm nay thế nào."

Logo quán Không Tên: hình ly cà phê phin — giống ly cà phê mẹ uống mỗi sáng trước khi ra chợ."""),

("Chương 7: Cô Gái Và Cuốn Sách Để Quên", """Một cô gái hai mươi lăm tuổi đến quán, uống cà phê, đọc sách hai tiếng, rồi đi — để quên cuốn sách trên bàn. An cất cuốn sách vào kệ, đợi cô quay lại.

Cô không quay lại. Nhưng tuần sau, một cuốn sách khác xuất hiện trên cùng chiếc bàn. Rồi tuần sau nữa. Mỗi tuần, cô đến, để lại một cuốn sách, và đi.

An đọc mỗi cuốn. Gạch chân những đoạn cô đã gạch chân. Hiểu dần: cô đang trải qua nỗi mất mát — cuốn sách nào cũng về mất mát.

Tuần thứ tám, An viết tờ giấy nhỏ kẹp trong cuốn sách: "Cuốn tiếp theo, cô chọn cuốn vui hơn được không?"

Tuần thứ chín, cô để lại cuốn sách — cuốn đầu tiên có ending happy. Kèm tờ giấy: "Cảm ơn anh. Tôi ổn hơn rồi."

Cô không bao giờ quay lại. Nhưng kệ sách quán có thêm chín cuốn — chín tuần chữa lành bằng sách."""),

("Chương 8: Đêm Giáng Sinh Của Người Cô Đơn", """Đêm hai mươi bốn tháng Mười Hai, An mở cửa quán đến khuya — cho những ai không có nơi nào đi. Cà phê miễn phí. Không cần lý do.

Bác Hải đến — với bức thư mới cho vợ. Cậu sinh viên năm xưa đến — giờ đã tốt nghiệp, có việc làm. Chị phụ nữ bốn mươi tuổi đến — đã ly hôn, bình yên hơn. Chị bán vé số đến — mang theo nồi chè.

Tám người ngồi trong quán nhỏ mười lăm mét vuông, uống cà phê, ăn chè, kể chuyện. Không ai quen ai ngoài An — nhưng đêm đó, họ là gia đình.

"Anh An ơi, quán này tên gì?"

"Quán Không Tên."

"Sao lại không tên?"

"Vì mỗi người đến đây đều mang theo tên riêng của câu chuyện mình. Quán không cần tên — các bạn mới cần." """),

("Chương 9: Sáng Hôm Sau", """Sáng mồng Một Tết — An mở cửa quán lúc năm giờ sáng, pha phin đầu tiên. Hẻm vắng, sương mù nhẹ, tiếng xe máy xa xa.

Mẹ An gọi điện: "Con ơi, Tết này con có về không?"

"Con về chiều nay, mẹ. Sáng con pha xong mẻ cà phê cuối năm."

"Con pha cho ai?"

"Cho con. Cho quán. Cho năm mới."

An ngồi một mình, uống cà phê phin — giọt cà phê nhỏ xuống chậm rãi, mùi thơm bay trong quán nhỏ, hẻm sâu, Sài Gòn yên tĩnh.

Trên bàn, chín cuốn sách của cô gái nằm xếp hàng trên kệ. Bức thư của bác Hải kẹp trong cuốn sổ. Hộp cứu thương vẫn ở góc phòng.

An mỉm cười, nhấp ngụm cà phê, và nghĩ: "Năm nay, mình sẽ tiếp tục lắng nghe." """),
]

# ═══════════════════════════════════════════════════════════════════════════════
# STORY 17: THẦY GIÁO VÙNG CAO — 10 CHƯƠNG
# ═══════════════════════════════════════════════════════════════════════════════

S17_TITLE = "THẦY GIÁO MANG TỦ SÁCH LÊN NÚI — CÂU CHUYỆN CỦA NGƯỜI ĐÀN ÔNG ĐI BỘ BA MƯƠI CÂY SỐ MỖI TUẦN ĐỂ TRẺ EM VÙNG CAO BIẾT ĐỌC"
S17_AUTHOR = "Đỗ Trọng Nghĩa"
S17_COVER = "base_cover_20.png"
S17_INTRO = """<p>Thầy giáo Đỗ Trọng Nghĩa, hai mươi lăm tuổi, từ chối công việc tại công ty tư vấn lương cao ở Hà Nội, tình nguyện lên dạy học ở bản Suối Giàng, Yên Bái — nơi không có đường nhựa, không có sóng điện thoại, và hơn nửa trẻ em chưa biết đọc.</p>
<p>Ba năm trên núi, thầy Nghĩa đi bộ ba mươi cây số mỗi tuần mang sách từ thị trấn lên bản — và thay đổi cuộc đời của hai mươi đứa trẻ H'Mông.</p>"""

S17_CHAPTERS = [
("Chương 1: Lên Núi", """Đỗ Trọng Nghĩa bước xuống xe khách ở thị trấn Văn Chấn lúc năm giờ chiều. Từ đây đến bản Suối Giàng: mười lăm cây số đường đất, dốc ngược, không xe máy nào lên được khi mưa.

Ba lô nặng hai mươi ký — quần áo, sách giáo khoa, và một thùng sách truyện thiếu nhi bạn bè quyên góp. Nghĩa đi bộ bốn tiếng, đến bản lúc chín giờ tối, trời tối đen như mực.

Trưởng bản Thào A Phử đón ở đầu bản, cầm đuốc: "Thầy giáo mới à? Thầy trẻ quá. Thầy trước bỏ về sau ba tháng."

"Em biết. Em không bỏ."

Bản Suối Giàng: hai mươi bảy hộ gia đình H'Mông, một trăm ba mươi người, hai mươi đứa trẻ từ sáu đến mười lăm tuổi — mười ba đứa chưa biết đọc tiếng Việt."""),

("Chương 2: Lớp Học Dưới Gốc Cây", """Trường học — nếu gọi là trường — là căn nhà gỗ nghiêng, mái tôn thủng ba chỗ, không bàn ghế. Nghĩa dùng thùng gỗ làm bàn, tảng đá làm ghế, bảng phấn treo trên cây.

Ngày đầu tiên: mười ba đứa trẻ ngồi trên đất, mắt tròn xoe nhìn "thầy giáo từ Hà Nội." Đứa lớn nhất — Thào A Sử, mười lăm tuổi — nhìn Nghĩa bằng ánh mắt nghi ngờ: "Thầy ơi, học để làm gì? Bố em bảo đi nương kiếm ăn được rồi."

Nghĩa không trả lời ngay. Anh lấy cuốn truyện tranh ra, đọc to — câu chuyện Sơn Tinh Thủy Tinh. Bọn trẻ nghe, mắt sáng. Đứa nhỏ nhất — Giàng Thị Mây, sáu tuổi — bò đến gần, chỉ vào tranh: "Thầy ơi, con muốn đọc!"

"Vậy thầy dạy em đọc nhé."

Mây gật đầu. Sử vẫn nghi ngờ — nhưng cậu ở lại."""),

("Chương 3: Ba Mươi Cây Số Mỗi Tuần", """Vấn đề lớn nhất: không có sách. Trường chỉ có bốn cuốn sách giáo khoa cũ, rách bìa. Bọn trẻ cần sách truyện, sách khoa học, sách tiếng Việt cho người dân tộc.

Giải pháp của Nghĩa: mỗi tuần, anh đi bộ ba mươi cây số khứ hồi — mười lăm cây xuống thị trấn Văn Chấn, mua sách bằng lương (ba triệu rưỡi/tháng — gần hết mua sách), và gùi lên lại.

Mỗi chuyến: mười đến mười lăm cuốn sách trong ba lô. Đi sáng sớm, về tối muộn. Mùa mưa: đường trơn, suýt trượt xuống vực hai lần. Mùa đông: nhiệt độ xuống năm độ C, tay tê cóng.

"Thầy ơi, sao thầy không mua xe máy?"

"Đường này xe máy không đi được khi mưa. Và thầy không có tiền mua xe." """),

("Chương 4: Thào A Sử Biết Đọc", """Sáu tháng sau, Sử — cậu bé mười lăm tuổi nghi ngờ nhất — đọc được trang đầu tiên của cuốn "Dế Mèn Phiêu Lưu Ký."

"Thầy ơi! Em đọc được! 'Tôi sống độc lập từ thuở bé...' Em đọc được thầy ơi!"

Sử khóc. Nghĩa khóc. Cả lớp vỗ tay.

Từ cậu bé nói "học để làm gì," Sử thành đứa trẻ đọc nhiều nhất bản — mỗi tuần hai cuốn, đọc cho cả nhà nghe buổi tối.

Bố Sử — ông Thào A Páo — đến gặp Nghĩa: "Thầy ơi, thằng Sử nhà tôi giờ đọc sách cho tôi nghe mỗi tối. Nó đọc hay quá, tôi cũng muốn học."

Nghĩa mở thêm lớp buổi tối — cho người lớn."""),

("Chương 5: Tủ Sách Suối Giàng", """Sau một năm, Nghĩa đăng câu chuyện "đi bộ ba mươi cây mỗi tuần mang sách lên núi" trên Facebook. Post viral — năm trăm nghìn lượt chia sẻ.

Sách quyên góp tràn về: hai nghìn cuốn trong ba tháng, từ khắp cả nước. Nghĩa dựng "Tủ Sách Suối Giàng" — kệ gỗ trong lớp học, xếp theo chủ đề: truyện tranh, khoa học, lịch sử, tiếng Việt.

Bọn trẻ mê mẩn. Mây — bé gái sáu tuổi — giờ bảy, đọc trôi chảy, mỗi ngày đọc to cho em bé nghe.

"Thầy ơi, con muốn đọc hết tủ sách!" Mây nói, mắt lấp lánh.

"Con cứ đọc. Sách không bao giờ hết — vì thầy sẽ mang thêm." """),

("Chương 6: Mẹ Và Chiếc Cặp Sách", """Nghĩa lên núi vì mẹ. Bà Đỗ Thị Lan, giáo viên mầm non ở Thanh Hóa — lương hai triệu, dạy trẻ con nhà nghèo ở xã miền núi.

"Mẹ ơi, sao mẹ dạy ở đó? Lương thấp, đường xa."

"Vì ở đó có đứa trẻ nào cũng xứng đáng được học. Giống con ngày xưa — mẹ nghèo nhưng con vẫn được đi học, phải không?"

Nghĩa mang triết lý đó lên Suối Giàng: mọi đứa trẻ đều xứng đáng. Kể cả đứa trẻ H'Mông trên đỉnh núi cao nhất Yên Bái."""),

("Chương 7: Mùa Đông Khắc Nghiệt", """Mùa đông năm thứ hai: nhiệt độ xuống hai độ C, sương muối phủ trắng nương. Bọn trẻ đến lớp chân đất, tay tím bầm, môi nứt nẻ.

Nghĩa dùng hết lương mua tất, găng tay, và áo ấm cho hai mươi đứa trẻ. Anh nhịn ăn sáng — uống nước nóng thay.

Trưởng bản Phử mang đến nhà Nghĩa một nồi thắng cố: "Thầy ơi, thầy gầy quá. Ăn đi."

"Bác Phử, em không sao..."

"Thầy không sao thì sao mắt thầy đỏ?" Phử đặt nồi thắng cố trước mặt Nghĩa.

Nghĩa ăn, nước mắt rơi vào bát — vì lần đầu tiên trên núi, có người chăm sóc anh."""),

("Chương 8: Sử Đỗ Đại Học", """Ba năm sau, Thào A Sử — cậu bé từng nói "học để làm gì" — thi đỗ Đại học Tây Bắc, ngành Sư phạm.

Sử là sinh viên đại học đầu tiên trong lịch sử bản Suối Giàng.

Ngày Sử xuống núi nhập học, cả bản tiễn. Bố Sử — ông Páo — đeo cho con chiếc vòng bạc H'Mông truyền thống: "Con đi học, rồi về dạy lại cho em út."

Sử ôm Nghĩa: "Thầy ơi, em sẽ quay lại. Em sẽ dạy như thầy."

Nghĩa vỗ vai Sử, không nói gì — vì anh đang khóc."""),

("Chương 9: Thầy Không Đi", """Nhiều người hỏi: "Thầy Nghĩa, bao giờ thầy xuống núi?"

Ba năm hợp đồng tình nguyện đã hết. Nhiều tổ chức mời Nghĩa về Hà Nội — lương cao, công việc nhẹ.

Nghĩa từ chối tất cả.

"Em ở lại. Vì Mây còn chưa đọc hết tủ sách. Vì lớp người lớn còn mười hai người chưa biết viết. Vì Suối Giàng cần thầy giáo hơn Hà Nội cần em."

Sáng hôm sau, Nghĩa dậy lúc năm giờ, đi bộ xuống thị trấn mua sách — lần thứ một trăm năm mươi. Ba lô nặng, đường dốc, sương mù dày.

Nhưng ở cuối con đường, hai mươi đứa trẻ đang đợi thầy — và tủ sách cần thêm sách mới."""),

("Chương 10: Bình Minh Suối Giàng", """Bình minh trên Suối Giàng: mặt trời mọc sau dãy núi, ánh vàng rải trên nương chè cổ thụ, sương tan dần.

Nghĩa ngồi trên bậc đá trước lớp học, uống ly trà nóng từ lá chè Suối Giàng — loại chè shan tuyết cổ thụ mà trưởng bản Phử tặng.

Bọn trẻ chạy đến, Mây dẫn đầu: "Thầy ơi! Hôm nay đọc truyện gì thầy?"

Nghĩa mỉm cười, mở ba lô, lấy ra cuốn sách mới — "Hoàng Tử Bé" — bìa xanh dương, trang giấy thơm mùi mực mới.

"Hôm nay thầy kể cho các em nghe chuyện Hoàng Tử Bé — một cậu bé ở trên ngôi sao rất xa."

Hai mươi đứa trẻ ngồi quanh thầy, mắt sáng, lắng nghe. Bình minh rải vàng trên mái tôn lớp học nhỏ, giữa núi rừng Tây Bắc.

Và thầy Nghĩa kể — như mọi ngày, như mọi sáng — bằng giọng nhẹ nhàng, kiên nhẫn, và yêu thương."""),
]

# ═══════════════════════════════════════════════════════════════════════════════
# STORY 18: BÀ NGOẠI VÀ TIỆM BÁNH — 8 CHƯƠNG
# ═══════════════════════════════════════════════════════════════════════════════

S18_TITLE = "TIỆM BÁNH CỦA BÀ NGOẠI — NƠI MÙI BÁNH FLAN CHỮA LÀNH MỌI VẾT THƯƠNG TUỔI THƠ"
S18_AUTHOR = "Phạm Minh Thư"
S18_COVER = "base_cover_21.png"
S18_INTRO = """<p>Khi bố mẹ ly hôn, Phạm Minh Thư sáu tuổi bị đẩy qua đẩy lại giữa hai gia đình. Không ai muốn nuôi. Cuối cùng, bà ngoại — bà Nguyễn Thị Bảy, bảy mươi tuổi, bán bánh flan ở chợ Bà Chiểu — nhận cháu về.</p>
<p>Hai mươi năm sau, tiệm bánh flan nhỏ của bà ngoại trở thành thương hiệu nổi tiếng cả nước — nhưng với Thư, tiệm bánh mãi là nơi bà dạy cháu rằng "yêu thương không cần lý do."</p>"""

S18_CHAPTERS = [
("Chương 1: Bé Gái Không Ai Nhận", """Phạm Minh Thư ngồi trên chiếc ghế nhựa ở sảnh tòa án quận Bình Thạnh, chân không chạm đất. Sáu tuổi. Tóc buộc hai bím, áo hoa nhàu nhĩ. Bên trong phòng xử, bố mẹ đang cãi nhau — không phải vì ai cũng muốn nuôi con, mà vì không ai muốn nhận.

"Tôi không đủ điều kiện nuôi con." Bố nói.

"Tôi cũng không. Tôi sắp lấy chồng mới." Mẹ nói.

Thư nghe qua cánh cửa. Sáu tuổi, cô bé chưa hiểu hết, nhưng hiểu đủ: bố mẹ không muốn mình.

Bà ngoại — bà Nguyễn Thị Bảy, bảy mươi tuổi, lưng còng, tay xách giỏ nhựa — bước vào phòng xử: "Tôi nhận cháu. Cho tôi nuôi."

Thẩm phán nhìn bà: "Bà bảy mươi tuổi, thu nhập bao nhiêu?"

"Tôi bán bánh flan ở chợ Bà Chiểu. Ngày kiếm hai trăm nghìn. Đủ nuôi cháu."

Thẩm phán gật đầu. Bà ngoại bước ra, nắm tay Thư, dẫn đi.

"Bà ơi, bà có muốn nuôi con không?"

"Muốn chứ. Bà muốn nhất trên đời." """),

("Chương 2: Tiệm Bánh Flan Chợ Bà Chiểu", """Bà Bảy bán bánh flan ở chợ Bà Chiểu từ năm bốn mươi tuổi — ba mươi năm, mỗi ngày đẩy xe bánh ra chợ lúc năm giờ sáng, về lúc hai giờ chiều.

Bánh flan bà Bảy: caramel đắng nhẹ, trứng mịn, vị vani tự nhiên. Bí quyết: trứng gà ta, sữa tươi Mộc Châu, và caramel nấu bằng đường phên — không đường trắng.

Thư lớn lên bên cạnh xe bánh. Sáu tuổi, ngồi xổm cạnh bà, phụ đổ caramel vào khuôn. Mười tuổi, tự đánh trứng, hấp bánh. Mười ba tuổi, thay bà đẩy xe ra chợ khi bà bị đau lưng.

"Bà ơi, sao bánh flan bà ngon hơn tiệm?"

"Vì bà nấu bằng tay. Máy làm nhanh nhưng không có tình. Tay bà chậm nhưng mỗi cái bánh đều có bà trong đó." """),

("Chương 3: Chữa Lành Bằng Bánh", """Mỗi khi Thư buồn — bị bạn trêu "con không cha," bị điểm kém, nhớ mẹ — bà ngoại không nói gì. Bà vào bếp, nấu bánh flan, đặt trước mặt Thư.

"Ăn đi con. Buồn thì ăn bánh."

"Bà ơi, ăn bánh có hết buồn không?"

"Không hết. Nhưng bớt. Vì khi ăn bánh, con biết bà ở đây."

Thư ăn bánh, khóc, rồi lau nước mắt, cười. Và bà cười theo — nụ cười nhăn nheo, ít răng, nhưng ấm hơn mọi lời an ủi.

Hai mươi năm sau, Thư vẫn nhớ vị bánh flan đêm bà nấu cho cô khi bố gọi điện nói "bố không đến sinh nhật con được." Caramel đắng — giống nước mắt. Trứng mịn — giống tay bà xoa đầu."""),

("Chương 4: Bà Ốm — Thư Thay Bà Đẩy Xe", """Năm Thư mười sáu, bà bị đau khớp nặng — không đẩy xe ra chợ được. Bà nằm giường, tay sưng, mắt ướt: "Bà không bán được thì lấy gì nuôi con?"

Thư nghỉ học một tuần, tự đẩy xe bánh ra chợ Bà Chiểu. Mười sáu tuổi, tóc buộc cao, tay đánh trứng, miệng rao: "Bánh flan bà Bảy đây!"

Khách quen hỏi: "Bà Bảy đâu?"

"Bà ốm. Con bán thay bà."

"Bánh con làm có ngon bằng bà không?"

Thư cười: "Bà dạy con nấu. Trứng gà ta, sữa Mộc Châu, đường phên. Mời cô ăn thử."

Khách ăn, gật đầu: "Ngon. Đúng vị bà Bảy."

Thư mang tiền về, đặt dưới gối bà, không nói. Bà biết, cũng không nói. Hai bà cháu im lặng yêu thương."""),

("Chương 5: Đại Học — Đi Xa Để Quay Về", """Thư thi đỗ Đại học Công nghệ Thực phẩm. Bà vui — nhưng lo: "Con đi học, ai bán bánh với bà?"

"Bà ơi, con học xong sẽ về mở tiệm lớn hơn cho bà. Con hứa."

Bốn năm đại học, Thư vừa học vừa làm — phục vụ quán ăn, dạy kèm — gửi tiền về cho bà. Mỗi cuối tuần, gọi video hỏi bà: "Bà ơi, hôm nay bán được bao nhiêu?"

"Được hai trăm, đủ ăn. Con đừng lo."

Thư biết bà nói dối — bà gầy hơn, xe bánh cũ hơn. Nhưng Thư không nói. Cô chỉ học giỏi hơn."""),

("Chương 6: Thương Hiệu 'Bánh Bà Bảy' Ra Đời", """Tốt nghiệp, Thư về nhà, mở tiệm "Bánh Bà Bảy" — tiệm bánh flan đầu tiên có thương hiệu, đóng gói đẹp, giao hàng online.

Công thức: giữ nguyên 100% công thức bà — trứng gà ta, sữa Mộc Châu, đường phên. Không công nghiệp hóa. Mỗi ngày chỉ bán hai trăm hộp — hết thì nghỉ.

"Sao con không làm nhiều hơn?"

"Vì bà dạy con: 'Máy làm nhanh nhưng không có tình.' Con giữ chậm để giữ tình, bà ạ."

Năm đầu: sold out mỗi ngày. Năm thứ hai: mở thêm hai chi nhánh. Báo chí viết: " 'Bánh Bà Bảy' — thương hiệu bánh flan handmade nổi tiếng nhất Sài Gòn." """),

("Chương 7: Bà Bảy Và Tấm Ảnh Trên Tường", """Tiệm Bánh Bà Bảy — trang trí giản dị: tường trắng, bàn gỗ, và một tấm ảnh duy nhất — ảnh bà Bảy bảy mươi tuổi, đứng cạnh xe bánh flan ở chợ Bà Chiểu, cười nhăn nheo.

Khách hỏi: "Bà Bảy là ai?"

Thư trả lời: "Bà ngoại tôi. Người duy nhất muốn nuôi tôi khi không ai khác muốn."

Bà Bảy — giờ tám mươi chín — không bán bánh nữa. Bà ngồi ở tiệm mỗi sáng, uống trà, nhìn cháu bán bánh. Tay bà run, mắt bà mờ, nhưng nụ cười vẫn ấm.

"Bà ơi, con thành công rồi. Nhờ bà."

"Nhờ gì bà. Bà chỉ nấu bánh thôi."

"Bà nấu bánh và yêu con. Đó là tất cả." """),

("Chương 8: Vị Bánh Flan Cuối Cùng", """Sinh nhật Thư hai mươi sáu tuổi. Bà Bảy — tám mươi chín, tay run, lưng còng gập — vào bếp. Thư cản: "Bà ơi, để con nấu."

"Không. Sinh nhật con, bà nấu."

Bà nấu — chậm hơn xưa, caramel hơi cháy một chút, trứng hơi bọt — nhưng khi Thư ăn, đó là chiếc bánh flan ngon nhất đời cô.

"Bà ơi, bánh bà vẫn ngon nhất."

"Vì bà nấu cho con. Bánh cho người mình thương bao giờ cũng ngon hơn."

Thư ôm bà, mắt ướt. Bà xoa đầu cháu — tay nhăn nheo, run run, nhưng dịu dàng như mọi khi.

Ngoài cửa sổ, Sài Gòn ồn ào. Trong bếp nhỏ, hai bà cháu ôm nhau, mùi caramel bay trong không khí — mùi thơm hai mươi năm yêu thương."""),
]

# ═══════════════════════════════════════════════════════════════════════════════
# STORY 19: BÁC SĨ VỀ QUÊ MỞ PHÒNG KHÁM MIỄN PHÍ — 11 CHƯƠNG
# ═══════════════════════════════════════════════════════════════════════════════

S19_TITLE = "BÁC SĨ GIỎI NHẤT BỆNH VIỆN LỚN VỀ QUÊ MỞ PHÒNG KHÁM MIỄN PHÍ CHO NGƯỜI NGHÈO"
S19_AUTHOR = "Lương Đức Hải"
S19_COVER = "base_cover_22.png"
S19_INTRO = """<p>BS. Lương Đức Hải, ba mươi lăm tuổi, Phó khoa Ngoại Bệnh viện Chợ Rẫy — bác sĩ phẫu thuật giỏi nhất thế hệ, lương bảy mươi triệu, tương lai rộng mở. Một ngày, anh nộp đơn xin nghỉ, về quê Quảng Trị mở phòng khám miễn phí.</p>
<p>"Vì ở Sài Gòn, không thiếu bác sĩ giỏi. Ở quê tôi, không có bác sĩ nào."</p>"""

S19_CHAPTERS = [
("Chương 1: Đơn Xin Nghỉ", """Giám đốc Bệnh viện Chợ Rẫy nhìn đơn xin nghỉ của Hải, lắc đầu: "Hải à, em là Phó khoa Ngoại giỏi nhất bệnh viện. Em nghỉ là thiệt hại lớn."

"Em biết, anh. Nhưng ở quê em, huyện Triệu Phong, Quảng Trị — ba mươi nghìn dân, không có bác sĩ chuyên khoa ngoại nào. Người ta bị viêm ruột thừa phải chạy ba tiếng lên Huế — có người chết trên đường."

"Nhưng lương em ở đây bảy mươi triệu. Về quê mở phòng khám miễn phí — em sống bằng gì?"

"Em sống bằng tiết kiệm. Và bằng cách không để ai chết vì thiếu bác sĩ nữa."

Giám đốc ký đơn, mắt ướt: "Em đi. Nhưng bất cứ lúc nào muốn quay lại, cửa luôn mở." """),

("Chương 2: Phòng Khám Trong Nhà Cũ", """Hải về Triệu Phong, sửa lại nhà cũ của bố mẹ thành phòng khám. Phòng mổ — nếu gọi là phòng mổ — là phòng khách cũ, lát gạch trắng, đèn LED, và bộ dụng cụ phẫu thuật anh mua bằng tiền tiết kiệm.

Bảng hiệu: "Phòng Khám BS. Hải — Khám miễn phí cho bà con."

Ngày đầu tiên: bốn mươi bệnh nhân xếp hàng từ năm giờ sáng. Bà cụ bảy mươi tuổi, đau khớp mười năm chưa khám — vì không có tiền đi Huế. Ông lão sáu mươi tuổi, u nang bã đậu to bằng quả trứng — chưa mổ vì sợ tốn tiền.

Hải khám từ sáng đến tối. Miễn phí. Thuốc — anh mua bằng tiền riêng, phát miễn phí."""),

("Chương 3: Ca Mổ Đầu Tiên Ở Quê", """Một đêm, anh Nguyễn Văn Thắng — nông dân bốn mươi tuổi — được vợ chở đến phòng khám bằng xe máy, bụng đau quằn quại. Hải khám: viêm ruột thừa cấp, sắp vỡ.

"Chở anh lên Huế ba tiếng — không kịp. Mổ tại đây."

Hải mổ — bàn mổ là giường bệnh, đèn mổ là đèn LED, y tá phụ là vợ Hải — chị Lan, điều dưỡng đã nghỉ việc theo chồng về quê.

Ca mổ bốn mươi phút. Thành công. Ruột thừa viêm nặng — nếu chậm hai tiếng, vỡ, nhiễm trùng, chết.

Thắng tỉnh dậy: "Bác sĩ ơi, em nợ bác sĩ bao nhiêu?"

"Không nợ gì. Anh khỏe là đủ." """),

("Chương 4: Bà Con Đến Ngày Càng Đông", """Tin đồn lan khắp huyện: "Có bác sĩ giỏi nhất Chợ Rẫy về quê khám miễn phí." Bệnh nhân từ Triệu Phong, Hải Lăng, Cam Lộ đổ về.

Mỗi ngày: năm mươi đến bảy mươi bệnh nhân. Hải khám từ sáu giờ sáng đến chín giờ tối. Không nghỉ trưa. Ăn cơm giữa hai ca khám.

Thuốc hết. Tiền tiết kiệm cạn. Hải đăng Facebook kêu gọi — ba trăm triệu quyên góp trong tuần đầu.

Nhưng Hải biết: quyên góp không bền. Anh cần giải pháp lâu dài."""),

("Chương 5: Cộng Đồng Bác Sĩ Tình Nguyện", """Hải lập "Mạng lưới BS. Về Quê" — kêu gọi bác sĩ trẻ về nông thôn khám miễn phí mỗi cuối tuần. Mười hai bác sĩ từ Huế, Đà Nẵng tình nguyện — mỗi người một chuyên khoa: nội, nhi, sản, da liễu.

Phòng khám Hải thành hub — cuối tuần có chuyên gia, ngày thường Hải khám đa khoa.

Sở Y tế Quảng Trị hỗ trợ: cấp thiết bị X-quang, máy siêu âm, và trợ cấp lương cho y tá.

"BS. Hải, anh đã tạo ra mô hình phòng khám cộng đồng mà cả nước nên học," Giám đốc Sở Y tế nói."""),

("Chương 6: Bố Và Chai Thuốc Cũ", """Hải theo nghề vì bố. Ông Lương Văn Đức — nông dân Triệu Phong — mất vì viêm phúc mạc khi Hải mười hai tuổi. Bệnh bắt đầu từ viêm ruột thừa — bệnh đơn giản, mổ ba mươi phút. Nhưng không có bác sĩ ở huyện, không có tiền đi Huế, ông chịu đau ba ngày rồi mất.

"Bố mất vì một ca mổ đơn giản mà không ai mổ cho bố," Hải nói trong buổi khai trương phòng khám. "Phòng khám này mang tên bố — để không ai phải chết vì thiếu bác sĩ như bố."

Trên bàn phòng khám, Hải đặt chai thuốc cũ — chai thuốc hạ sốt paracetamol duy nhất mà bố dùng trước khi mất. Chai thuốc rẻ tiền — nhưng vô dụng khi bệnh cần dao mổ."""),

("Chương 7: Chị Lan — Người Vợ Phía Sau", """Vợ Hải — Lương Thị Lan — bỏ nghề điều dưỡng lương bốn mươi triệu ở Sài Gòn, theo chồng về quê. Chị làm y tá, tiếp đón bệnh nhân, quản lý thuốc, và nấu cơm cho chồng giữa hai ca khám.

"Lan ơi, anh xin lỗi vì kéo em về quê."

"Anh không kéo em. Em chọn đi cùng anh. Vì ở Sài Gòn, em là một trong triệu điều dưỡng. Ở đây, em là điều dưỡng duy nhất — và bà con cần em."

Chị Lan mang thai tháng thứ bảy — vẫn làm việc mỗi ngày. Bà con mang trứng, rau, gạo đến biếu — "để bác sĩ và cô Lan ăn cho khỏe."

Hải nhìn vợ — bụng lớn, tay phát thuốc, miệng cười với bệnh nhân — và biết: anh đã chọn đúng người để đi cùng."""),

("Chương 8: Mổ Dưới Đèn Pin", """Mất điện. Một đêm bão, điện cúp toàn huyện. Bệnh nhân cấp cứu: bé trai tám tuổi, gãy xương cẳng tay hở, máu chảy.

Hải mổ dưới ánh đèn pin — vợ cầm đèn, Hải phẫu thuật. Bốn mươi phút. Xương được nắn, vết thương khâu, bé trai ổn định.

"Bác sĩ ơi, làm sao anh mổ được trong tối thế?"

"Vì tay bác sĩ quen rồi. Mắt có thể không thấy rõ, nhưng tay nhớ." """),

("Chương 9: Sáng Kiến Khám Bệnh Từ Xa", """Hải kết nối phòng khám với bệnh viện Chợ Rẫy qua hệ thống tele-medicine — gọi video để các chuyên gia Sài Gòn tư vấn từ xa cho ca bệnh phức tạp.

"Ở quê không có CT scan. Nhưng có smartphone và wifi. Chúng tôi gửi ảnh X-quang chụp bằng máy cũ lên cho chuyên gia đọc."

Mô hình tele-medicine Triệu Phong được Bộ Y tế nhân rộng ra mười huyện khác — giảm sáu mươi phần trăm ca chuyển tuyến lên tỉnh."""),

("Chương 10: Con Trai Ra Đời — Tại Chính Phòng Khám", """Chị Lan sinh con tại phòng khám — Hải đỡ đẻ cho chính vợ mình. Bé trai khỏe mạnh, ba ký rưỡi.

"Đặt tên con gì, anh?"

"Lương Đức Phong — Phong vì Triệu Phong. Để con nhớ quê mình."

Bà con mang quà đến đầy phòng khám — trứng, gạo, rau, và một tấm biển gỗ khắc tay: "BS. Hải — Ân nhân của bà con Triệu Phong."

Hải nhìn tấm biển, rồi nhìn con trai — bé Phong nằm trong tay mẹ, ngủ ngon."""),

("Chương 11: Bình Minh Triệu Phong", """Năm giờ sáng, Hải mở cửa phòng khám. Bệnh nhân đã xếp hàng — bà cụ đau khớp, ông lão ho lâu ngày, bé gái sốt cao.

Hải mặc áo blouse trắng, rửa tay, bắt đầu khám. Chị Lan — bé Phong địu sau lưng — phát thuốc, ghi sổ.

Bên ngoài, bình minh lên trên cánh đồng Triệu Phong — lúa xanh, trời trong, gió mát.

Hải nghe ống nghe trên ngực bà cụ: "Bà ơi, tim bà khỏe lắm. Bà sống lâu nhé."

"Sống lâu để bác sĩ khám cho bà nữa." Bà cười.

Hải cười theo. Rồi gọi bệnh nhân tiếp theo: "Mời bác vào." """),
]

# ═══════════════════════════════════════════════════════════════════════════════
# STORY 20: CÔ GÁI CÂM MỞ TIỆM HOA — 10 CHƯƠNG
# ═══════════════════════════════════════════════════════════════════════════════

S20_TITLE = "CÔ GÁI CÂM MỞ TIỆM HOA — NƠI NGÔN NGỮ CỦA HOA THAY LỜI CÔ KHÔNG NÓI ĐƯỢC"
S20_AUTHOR = "Nguyễn Ngọc Trâm"
S20_COVER = "base_cover_23.png"
S20_INTRO = """<p>Nguyễn Ngọc Trâm sinh ra đã câm — dây thanh quản bị tổn thương bẩm sinh, không phát ra được âm thanh. Trong thế giới ồn ào, Trâm im lặng. Nhưng đôi bàn tay cô nói được — bằng hoa.</p>
<p>Tiệm hoa "Im Lặng" của Trâm ở Đà Lạt trở thành nơi mọi người đến mua hoa và nhận được thông điệp mà lời nói không diễn tả nổi.</p>"""

S20_CHAPTERS = [
("Chương 1: Thế Giới Không Có Tiếng", """Nguyễn Ngọc Trâm mở mắt mỗi sáng và thế giới im lặng. Không phải vì cô điếc — cô nghe rõ mọi thứ: tiếng chim, tiếng gió, tiếng người nói. Nhưng cô không nói được.

Câm bẩm sinh. Dây thanh quản tổn thương từ lúc sinh, không phẫu thuật được.

Lớn lên ở Đà Lạt, giữa rừng thông và vườn hoa. Trâm giao tiếp bằng tay — ngôn ngữ ký hiệu. Nhưng không nhiều người ở Đà Lạt hiểu ngôn ngữ ký hiệu.

Nên Trâm viết. Cô mang theo cuốn sổ nhỏ, viết ra mọi thứ muốn nói. Ở trường, cô được gọi là "con bé sổ" — vì đi đâu cũng cầm sổ.

Bạn bè trêu. Giáo viên thương nhưng bất lực. Và Trâm học được: thế giới không đợi người im lặng — nếu muốn được nghe, cô phải tìm cách nói mà không cần giọng."""),

("Chương 2: Hoa — Ngôn Ngữ Đầu Tiên", """Mười hai tuổi, Trâm phát hiện: hoa nói được những gì cô không nói.

Bà ngoại trồng hoa hồng trong vườn. Trâm hái một bông, tặng bạn gái cùng lớp — bạn cười rạng rỡ. Ngày hôm sau, bạn chơi với Trâm — không cần lời.

Cô bắt đầu học "ngôn ngữ hoa": hoa hồng đỏ là yêu, hoa cúc trắng là tiếc thương, hoa lavender là trung thành, hoa hướng dương là hy vọng.

"Mỗi bông hoa là một câu. Bó hoa là một bức thư," Trâm viết trong nhật ký.

Trâm tự trồng vườn hoa nhỏ sau nhà — hai trăm gốc. Mỗi sáng, cô cắt hoa, bó thành bó nhỏ, để trước cổng — ai đi qua thích thì lấy. Miễn phí.

Hàng xóm gọi cô là "bé hoa câm." Trâm không biết đó là khen hay chê — nhưng cô thích."""),

("Chương 3: Tiệm Hoa Im Lặng Ra Đời", """Hai mươi tuổi, Trâm mở tiệm hoa nhỏ ở con dốc yên tĩnh gần hồ Xuân Hương. Biển hiệu: "Im Lặng — Tiệm Hoa." Logo: bông hoa hồng và bàn tay ra dấu "yêu" trong ngôn ngữ ký hiệu.

Tiệm mười mét vuông. Tường gỗ, kệ hoa, và một tấm bảng nhỏ: "Chủ tiệm không nói được. Nhưng hoa sẽ nói thay. Hãy viết điều bạn muốn gửi — tôi sẽ chọn hoa cho bạn."

Khách đầu tiên: một chàng trai hai mươi lăm tuổi, muốn mua hoa tặng bạn gái sau khi cãi nhau. Trâm đưa sổ, chàng trai viết: "Em muốn nói xin lỗi nhưng không biết nói sao."

Trâm chọn: hoa tulip trắng (tha thứ) + hoa hyacinth tím (xin lỗi) + một cành baby breath (chân thành). Bó lại, kèm thiệp viết tay: "Lời xin lỗi không cần nói — chỉ cần chân thành."

Chàng trai cảm ơn, mắt hơi ướt."""),

("Chương 4: Khách Hàng Đặc Biệt — Ông Cụ Và Hoa Cho Vợ", """Ông Nguyễn Văn Tư, tám mươi tuổi, đến tiệm mỗi tuần mua một bó hoa nhỏ. Luôn cùng một loại: hoa cúc vàng.

Tuần thứ năm, Trâm đưa sổ hỏi: "Ông mua hoa cho ai ạ?"

Ông Tư viết lên sổ — tay run, chữ nguệch ngoạc: "Cho bà nhà tôi. Bà mất hai năm rồi. Nhưng tôi vẫn mua hoa mỗi tuần, đặt trên bàn thờ."

Trâm bó hoa cẩn thận hơn mọi khi. Kèm theo: một bông hoa forget-me-not (đừng quên tôi).

Ông Tư nhìn bông forget-me-not, mắt ướt: "Cháu hiểu ông."

Trâm gật đầu, mỉm cười. Không cần lời."""),

("Chương 5: Viral — Tiệm Hoa Câm Lặng Nổi Tiếng", """Một travel blogger đến tiệm, quay video quá trình Trâm chọn hoa cho khách — không nói một lời, chỉ đọc sổ, chọn hoa, bó, viết thiệp. Im lặng nhưng đẹp — như bộ phim không lời.

Video đạt mười triệu lượt xem. "Im Lặng" trở thành tiệm hoa nổi tiếng nhất Đà Lạt. Khách xếp hàng — không phải vì hoa đẹp nhất, mà vì ở đây, hoa được chọn bằng câu chuyện, không bằng giá tiền.

Trâm vẫn tự bó mỗi bó — tối đa ba mươi bó mỗi ngày. "Vì hoa cần được chọn bằng tay, không bằng máy." """),

("Chương 6: Mẹ Và Bàn Tay", """Trâm mở tiệm vì mẹ. Bà Nguyễn Thị Hạnh, giáo viên dạy trẻ khuyết tật tại trung tâm Đà Lạt.

"Mẹ ơi, sao mẹ dạy trẻ khuyết tật?"

"Vì mẹ có con. Và mẹ muốn thế giới biết: khuyết tật không phải thiếu — mà là khác."

Mẹ dạy Trâm ngôn ngữ ký hiệu từ bé. Dạy cô viết đẹp. Dạy cô rằng im lặng không phải yếu đuối.

"Con không nói được, nhưng tay con nói được — bằng hoa, bằng chữ, bằng yêu thương."

Logo tiệm Im Lặng: bàn tay ra dấu "yêu" — bàn tay mẹ dạy cô."""),

("Chương 7: Đám Cưới Không Lời", """Một cặp đôi — anh Minh câm bẩm sinh, chị Lan điếc bẩm sinh — đặt hoa cưới tại Im Lặng. Đám cưới im lặng hoàn toàn: không nhạc, không MC, không lời chúc bằng miệng. Chỉ có hoa, nến, và ngôn ngữ ký hiệu.

Trâm bó năm mươi bó hoa cho đám cưới — mỗi bó kèm thiệp viết tay. Cô khóc khi bó bó hoa cô dâu — vì lần đầu tiên, cô thấy sự im lặng không phải cô đơn, mà là bình yên.

"Im lặng là khi hai người hiểu nhau không cần nói," Trâm viết trong nhật ký đêm hôm đó."""),

("Chương 8: Giải Thưởng Thiết Kế Hoa Quốc Tế", """Trâm được mời tham gia cuộc thi thiết kế hoa quốc tế tại Hà Lan — xứ sở hoa tulip. Chủ đề: "Flowers Without Words" (Hoa Không Lời).

Tác phẩm của Trâm: một khu vườn hoa nhỏ — không biển tên, không hướng dẫn. Người xem bước vào, ngửi, chạm, cảm nhận — và hiểu câu chuyện bằng giác quan, không bằng lời.

Giải nhất. Ban giám khảo: "Trâm sống im lặng cả đời — và vì thế, hoa của cô nói to hơn bất kỳ ai." """),

("Chương 9: Cuốn Sổ Đầy Chữ", """Cuốn sổ nhỏ Trâm mang theo mỗi ngày — cuốn sổ mà cô dùng để "nói" — giờ đã đầy. Trâm thay sổ mới, nhưng giữ sổ cũ trong tủ kính tiệm.

Hai mươi ba cuốn sổ — hai mươi ba năm im lặng. Mỗi cuốn đầy chữ: "Cảm ơn," "Xin chào," "Tôi yêu bạn," "Hôm nay trời đẹp," "Tôi buồn."

Mỗi dòng chữ là một câu Trâm không nói được — nhưng đã viết ra, đã gửi đi, đã được đọc.

"Người ta sợ im lặng. Nhưng tôi sống trong im lặng — và tôi thấy thế giới đẹp hơn khi không ồn ào," Trâm viết ở trang cuối cuốn sổ thứ hai mươi ba."""),

("Chương 10: Sáng Mai Ở Đà Lạt", """Năm giờ sáng, Đà Lạt sương mù dày đặc. Trâm mở cửa tiệm Im Lặng, bê khay hoa từ vườn sau ra kệ.

Hoa hồng còn sương, lavender thơm nhẹ, hướng dương vàng rực. Trâm sắp hoa lên kệ — mỗi bông ở đúng vị trí, mỗi màu hài hòa.

Khách đầu tiên hôm nay: một cô gái trẻ, mắt đỏ, viết lên sổ: "Tôi vừa chia tay. Cho tôi bó hoa để tự tặng mình."

Trâm chọn: hoa hướng dương (hy vọng) + hoa daisy (niềm vui) + một cành eucalyptus (chữa lành). Kèm thiệp: "Bạn xứng đáng được yêu — bởi chính mình."

Cô gái đọc thiệp, mỉm cười — nụ cười đầu tiên sau nhiều ngày.

Trâm mỉm cười theo. Không nói. Không cần.

Ngoài cửa tiệm, Đà Lạt thức dậy — sương tan dần, nắng vàng nhẹ chiếu qua rừng thông, và mùi hoa tươi bay trong không khí.

Im lặng. Nhưng đẹp. Đẹp vì im lặng."""),
]

# ═══════════════════════════════════════════════════════════════════════════════
# ASSEMBLY & PUBLISHING
# ═══════════════════════════════════════════════════════════════════════════════

ALL_STORIES = [
    {"title": S16_TITLE, "author": S16_AUTHOR, "cover": S16_COVER, "intro": S16_INTRO, "chapters": S16_CHAPTERS, "genre": "Ngọt"},
    {"title": S17_TITLE, "author": S17_AUTHOR, "cover": S17_COVER, "intro": S17_INTRO, "chapters": S17_CHAPTERS, "genre": "Ngọt"},
    {"title": S18_TITLE, "author": S18_AUTHOR, "cover": S18_COVER, "intro": S18_INTRO, "chapters": S18_CHAPTERS, "genre": "Ngọt"},
    {"title": S19_TITLE, "author": S19_AUTHOR, "cover": S19_COVER, "intro": S19_INTRO, "chapters": S19_CHAPTERS, "genre": "Ngọt"},
    {"title": S20_TITLE, "author": S20_AUTHOR, "cover": S20_COVER, "intro": S20_INTRO, "chapters": S20_CHAPTERS, "genre": "Ngọt"},
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
    log("🚀 MIX BATCH 4 — 5 STORIES (🍯 Ngọt / Healing)")
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
            subtitle = f"Ngọt văn của {n['author']}"
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

    log(f"\n🏁 MIX BATCH 4 COMPLETE: {len(results)}/5 published")
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
