#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
write_batch_sangvan_01.py — Batch 1: 4 Truyện Sảng Văn (Stories 1-4)
=====================================================================
Story 1: Bác sĩ phẫu thuật thần kinh bị đuổi (cover 35)
Story 2: Kỹ sư AI bị cướp code (cover 36)
Story 3: NTK Thời trang bị phản bội (cover 37)
Story 4: Portfolio Manager bị vu oan (cover 38)
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
    abbrevs = ["TS.", "BS.", "PGS.", "GS.", "CEO.", "CFO.", "CTO.", "Dr.", "Mr.", "Mrs.", "A.I.", "ICU.", "CT.", "MRI.", "PCCC.", "HĐQT.", "IPO.", "Ph.D."]
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
# STORY 1: BÁC SĨ PHẪU THUẬT THẦN KINH
# ═══════════════════════════════════════════════════════════════════════════════

S1_TITLE = "BỊ ĐUỔI KHỎI BỆNH VIỆN TOP 1, TÔI MỞ PHÒNG KHÁM KHIẾN CẢ HỘI ĐỒNG Y KHOA NGHIÊNG MÌNH"
S1_AUTHOR = "Lê Quang Huy"
S1_COVER = "base_cover_35.png"
S1_INTRO = """<p><strong>"Tám năm tôi cầm dao mổ cứu hơn ba nghìn bệnh nhân, không một ca tử vong trên bàn phẫu thuật. Đổi lại, họ vu oan tôi sơ suất giết người, tước chứng chỉ hành nghề ngay trước mặt bệnh nhân đang chờ mổ."</strong></p>
<p>Lê Quang Huy, bác sĩ phẫu thuật thần kinh xuất sắc nhất Bệnh viện Trung ương Sài Gòn, bị Phó Giám đốc Trần Đình Phong cùng đồng nghiệp Nguyễn Hoàng Sơn dàn dựng hồ sơ y khoa giả để cướp vị trí Trưởng khoa và chiếm đoạt công trình nghiên cứu kỹ thuật mổ nội soi thần kinh đột phá.</p>
<p>Bị tước mọi thứ, Huy gặp Vũ Thanh Mai, nữ CEO hãng thiết bị y tế sắc sảo. Cùng nhau, họ xây dựng phòng khám thần kinh tư nhân với trang thiết bị tiên tiến nhất Đông Nam Á, lật trần bộ mặt thối nát của kẻ phản bội và đưa kỹ thuật mổ não Việt Nam lên bản đồ y khoa thế giới.</p>"""

S1_CHAPTERS = [
("Chương 1: Ca Mổ Cuối Cùng", """Đồng hồ phòng mổ số 3 Bệnh viện Trung ương Sài Gòn chỉ hai giờ mười bảy phút sáng. Lê Quang Huy đang thực hiện ca phẫu thuật loại bỏ khối u thân não cho bé Nguyễn Minh Anh, bảy tuổi — ca mổ mà chín mươi phần trăm bệnh viện trong nước từ chối vì tỷ lệ tử vong quá cao.

Đôi tay Huy vững chãi như thép nguội dưới ánh đèn phẫu thuật trắng xanh lạnh lẽo. Anh điều khiển kính vi phẫu Zeiss OPMI Pentero 900 trị giá mười hai tỷ đồng, mũi dao bistoury số 15 lướt qua mô não mềm như đậu hũ mà không chạm vào một sợi mạch máu nào.

"Hút dịch. Bipolar ba milliamp. Cẩn thận nhánh động mạch tiểu não trước dưới," Huy ra lệnh, giọng trầm vững không một gợn sóng dù trái tim anh đang đập một trăm hai mươi nhịp mỗi phút.

Tám năm. Ba nghìn một trăm hai mươi bảy ca phẫu thuật. Không một ca tử vong trên bàn mổ. Đó là thành tích mà không bác sĩ phẫu thuật thần kinh nào dưới bốn mươi tuổi trong cả nước đạt được.

Bốn tiếng sau, khối u được lấy ra hoàn toàn. Bé Minh Anh tỉnh lại, cử động được cả hai tay. Cha mẹ bé ôm nhau khóc nức nở ngoài phòng hồi sức.

Huy cởi găng tay, bước ra hành lang, tựa lưng vào tường. Mồ hôi đẫm ướt cả lưng áo blouse xanh. Anh nhắm mắt, thở ra một hơi dài.

"Bác sĩ Huy, lên phòng Phó Giám đốc ngay. Có cuộc họp khẩn." Cô y tá trực đêm hấp tấp chạy đến.

Huy nhíu mày. Họp khẩn lúc sáu giờ sáng? Sau ca mổ bốn tiếng?

Anh bước vào phòng họp tầng năm. Ngồi ở đầu bàn là Trần Đình Phong, Phó Giám đốc phụ trách chuyên môn, năm mươi ba tuổi, gương mặt vuông chữ điền lúc nào cũng mang vẻ nghiêm nghị giả tạo. Bên cạnh hắn là Nguyễn Hoàng Sơn — bác sĩ cùng khoa, người mà Huy đã tận tay dạy kỹ thuật vi phẫu suốt ba năm.

"Lê Quang Huy," Phong mở một tập hồ sơ dày, giọng lạnh như phòng mổ. "Hội đồng y khoa bệnh viện đã xem xét hồ sơ ca bệnh nhân Trần Văn Tú, nam, sáu mươi hai tuổi, phẫu thuật u màng não ngày 12 tháng 3. Bệnh nhân tử vong sau mổ hai mươi bốn giờ do xuất huyết não thứ phát."

Huy sững người. "Ca bệnh nhân Tú? Tôi đã mổ thành công, không có biến chứng trong mổ. Bệnh nhân tử vong là do đột quỵ tái phát hậu phẫu — biến chứng nội khoa, không liên quan đến kỹ thuật phẫu thuật!"

"Hồ sơ phẫu thuật ghi rõ: trong quá trình mổ, bác sĩ phẫu thuật đã cắt nhầm nhánh động mạch não giữa, gây xuất huyết thứ phát," Sơn lên tiếng, đẩy tờ phiếu phẫu thuật về phía Huy. "Đây, chữ ký của anh."

Huy nhìn tờ phiếu, máu dồn lên mặt. Đó KHÔNG phải nội dung anh viết. Phần mô tả phẫu thuật đã bị sửa đổi — thay thế hoàn toàn bằng một bản ghi giả mô tả sai sót kỹ thuật. Nhưng chữ ký ở dưới đúng là của anh, vì anh ký ngay sau mổ lúc mệt rã rời mà không kiểm tra lại toàn bộ nội dung.

"Các người giả mạo hồ sơ!" Huy đứng bật dậy, ghế xô ra sau kêu kin kít trên nền gạch. "Camera phòng mổ ghi lại toàn bộ ca phẫu thuật, các người kiểm tra đi!"

Phong khẽ cười. "Camera phòng mổ số 3 bị trục trặc kỹ thuật vào đúng ngày hôm đó. File ghi hình bị corrupt, không thể phục hồi."

"Bị corrupt?" Huy nghiến răng. "Các người phá hủy bằng chứng?"

"Đủ rồi!" Phong đập bàn. "Hội đồng y khoa đã biểu quyết: đình chỉ chức danh Trưởng khoa Phẫu thuật Thần kinh của bác sĩ Lê Quang Huy, tạm đình chỉ chứng chỉ hành nghề chờ điều tra, và đề nghị chuyển hồ sơ cho Sở Y tế xem xét kỷ luật."

Phong ném một phong bì trắng xuống bàn. "Đơn nghỉ việc. Ký đi, để bệnh viện còn giữ thể diện cho cậu. Nếu không, báo chí sẽ biết rằng Trưởng khoa Lê Quang Huy giết chết bệnh nhân trên bàn mổ."

Huy nhìn Sơn, người mà anh coi như em trai, người mà anh đã dành hàng trăm giờ truyền dạy kỹ thuật vi phẫu. "Sơn, tại sao?"

Sơn tránh ánh mắt Huy, chỉnh lại ống nghe trên cổ. "Anh Huy, anh giỏi quá. Giỏi đến mức không ai trong khoa được mổ ca lớn. Anh Phong hứa cho em vị trí Trưởng khoa, kèm hai mươi phần trăm hoa hồng từ hợp đồng thiết bị mới. Em xin lỗi."

Bảo vệ bệnh viện ập vào, thu lại thẻ nhân viên, chìa khóa phòng mổ, và áo blouse trắng có thêu tên "BS. Lê Quang Huy — Trưởng khoa PTTK." Chiếc áo blouse bị gấp gọn bỏ vào túi nhựa như một món đồ vô giá trị.

Huy bước ra khỏi cổng bệnh viện lúc bảy giờ sáng, khi dòng bệnh nhân đang xếp hàng chờ khám. Mặt trời Sài Gòn chiếu thẳng vào mắt anh nhưng anh không nheo mắt. Trong túi áo anh chỉ còn chiếc điện thoại và cuốn sổ ghi chép phẫu thuật cá nhân — thứ duy nhất mà Phong không cướp được.

"Trần Đình Phong, Nguyễn Hoàng Sơn," Huy thì thầm qua hàm răng nghiến chặt. "Tôi cứu ba nghìn mạng người bằng đôi tay này. Các người nghĩ đuổi tôi khỏi bệnh viện là xong? Tôi sẽ xây một nơi mà bệnh nhân cả nước tìm đến, và các người sẽ phải quỳ xin tôi hội chẩn." """),

("Chương 2: Phòng Khám Hẻm Nhỏ Và Nữ CEO", """Hai tuần sau ngày bị đuổi, Huy thuê một mặt bằng năm mươi mét vuông trong con hẻm trên đường Nguyễn Trãi, quận 5. Tiền thuê mười lăm triệu một tháng, gần hết số tiết kiệm bốn trăm triệu mà anh dành dụm tám năm.

Phòng khám nhỏ bé, chỉ có một phòng khám bệnh, một phòng tiểu phẫu đơn giản, và khu vực chờ ba ghế nhựa. Biển hiệu ghi tay: "Phòng khám Chuyên khoa Thần kinh — BS. Lê Quang Huy."

Tuần đầu tiên, không một bệnh nhân nào đến. Tin đồn "bác sĩ Huy giết chết bệnh nhân" đã lan khắp giới y khoa Sài Gòn. Không bệnh viện nào dám giới thiệu bệnh nhân cho anh. Các đồng nghiệp cũ tránh anh như tránh dịch bệnh.

Ngày thứ mười, một bà cụ bảy mươi tuổi dẫn theo cháu trai bốn tuổi bước vào. Cháu bé bị động kinh, co giật liên tục, đã đi khám mười hai bệnh viện mà không tìm ra nguyên nhân.

Huy khám cẩn thận, phát hiện cháu bé có dị dạng mạch máu não nhỏ mà các bác sĩ khác đã bỏ sót trên phim MRI. Anh viết đơn giới thiệu sang bệnh viện lớn để mổ, nhưng bà cụ lắc đầu: "Bác sĩ ơi, chúng tôi đã bán hết ruộng rồi, không còn tiền nằm viện."

Huy nhìn cháu bé, trái tim anh nhói đau. Anh quyết định: sẽ mổ tại phòng khám, miễn phí hoàn toàn. Anh mượn thiết bị gây mê từ một người bạn bác sĩ gây mê, dùng kính lúp phẫu thuật cá nhân thay vì kính vi phẫu hàng tỷ đồng.

Ca mổ kéo dài ba tiếng trong căn phòng nhỏ xíu. Huy xử lý dị dạng mạch máu bằng kỹ thuật vi phẫu mà anh đã thực hiện hàng trăm lần — nhưng lần này không có đội ngũ mười người hỗ trợ, không có thiết bị hiện đại. Chỉ có đôi tay anh, con dao, và ý chí sắt đá.

Ca mổ thành công. Cháu bé hết co giật. Bà cụ quỳ xuống khóc nức nở, lạy tạ Huy.

Câu chuyện lan truyền trong xóm lao động quận 5. Rồi một người quay video bà cụ kể lại, đăng lên Facebook. Video đạt năm trăm nghìn lượt xem trong một tuần.

Người tiếp theo đến phòng khám là Vũ Thanh Mai, ba mươi hai tuổi, CEO của MedTech Việt Nam — công ty chuyên nhập khẩu và phân phối thiết bị phẫu thuật thần kinh cao cấp nhất Đông Nam Á.

Mai mặc blazer xám sang trọng, tóc búi cao gọn gàng, đeo kính cận gọng titan mảnh. Cô bước vào phòng khám nhỏ bé, nhìn quanh với đôi mắt sắc sảo đánh giá mọi chi tiết.

"Anh Huy, tôi là Vũ Thanh Mai, MedTech Việt Nam. Tôi cung cấp kính vi phẫu Zeiss và hệ thống neuronavigation cho mười hai bệnh viện lớn nhất cả nước, bao gồm Bệnh viện Trung ương Sài Gòn," cô nói thẳng. "Tôi biết anh là ai. Tôi cũng biết hồ sơ ca bệnh nhân Trần Văn Tú là giả."

Huy sững lại. "Cô biết?"

"Tôi bán thiết bị cho bệnh viện, tôi có quyền truy cập log bảo trì hệ thống. Camera phòng mổ số 3 không bị trục trặc kỹ thuật — file ghi hình bị xóa thủ công bởi tài khoản admin của phòng IT, theo lệnh của Phó Giám đốc Phong. Tôi có bản log backup."

Huy nhìn Mai, đôi mắt anh sáng lên lần đầu tiên sau hai tuần u ám. "Tại sao cô giúp tôi?"

Mai đặt một chiếc USB lên bàn khám. "Vì tôi là doanh nhân, và tôi đầu tư vào người giỏi nhất. Anh là bác sĩ phẫu thuật thần kinh số một Việt Nam, mà đang ngồi trong phòng khám hai mươi mét vuông mổ bằng kính lúp. Đó là lãng phí tài nguyên quốc gia."

"Cô muốn gì?"

"Tôi muốn đầu tư xây phòng khám chuyên khoa thần kinh tư nhân đạt chuẩn quốc tế, trang bị thiết bị tốt nhất thế giới, với anh là Giám đốc Y khoa. Không phải làm thuê — anh sở hữu năm mươi mốt phần trăm, tôi bốn mươi chín. Anh có toàn quyền chuyên môn."

Huy nhìn chiếc USB, rồi nhìn Mai. Lần đầu tiên sau hai tuần, anh thấy con đường phía trước không còn tối đen.

"Tôi đồng ý. Nhưng có một điều kiện," Huy nói. "Phòng khám này sẽ dành hai mươi phần trăm công suất để khám và mổ miễn phí cho bệnh nhân nghèo. Không thương lượng."

Mai mỉm cười — nụ cười đầu tiên kể từ khi cô bước vào. "Đó chính là lý do tôi chọn đầu tư vào anh chứ không phải một bác sĩ khác." """),

("Chương 3: Ca Mổ Livestream Gây Chấn Động", """Ba tháng sau, Phòng khám Neuro Center Sài Gòn khai trương tại một tòa nhà năm tầng trên đường Lý Tự Trọng, quận 1. Tổng đầu tư mười tám tỷ đồng, trang bị kính vi phẫu Zeiss KINEVO 900, hệ thống neuronavigation Brainlab Curve, và robot hỗ trợ phẫu thuật ROSA từ Pháp.

Mai đề xuất ý tưởng táo bạo: livestream ca phẫu thuật đầu tiên trên YouTube để giới y khoa và công chúng tận mắt chứng kiến tay nghề của Huy.

"Anh điên à? Livestream phẫu thuật não?" Huy phản đối.

"Anh sợ người ta thấy anh mổ?" Mai hỏi ngược, ánh mắt thách thức. "Hay anh sợ Phong và Sơn thấy anh mổ?"

Câu hỏi đó khiến Huy im lặng ba giây, rồi gật đầu.

Ca phẫu thuật được livestream là loại bỏ u dây thần kinh thính giác cho bệnh nhân nữ, bốn mươi lăm tuổi, bị mất thính lực hoàn toàn bên trái. Đây là ca mổ cực khó — phải lấy u mà không làm tổn thương dây thần kinh mặt, nếu không bệnh nhân sẽ bị liệt nửa mặt vĩnh viễn.

Ba mươi nghìn người xem trực tiếp. Trong đó có hàng trăm bác sĩ từ khắp cả nước, các giáo sư y khoa từ Hà Nội, và — Nguyễn Hoàng Sơn, đang ngồi trong phòng trực Bệnh viện Trung ương, mồ hôi tay ướt đẫm.

Huy mổ bốn tiếng rưỡi. Camera 4K gắn trên kính vi phẫu truyền hình ảnh sắc nét đến từng mao mạch. Đôi tay Huy di chuyển với độ chính xác không thể tin được — mũi dao tách u khỏi dây thần kinh mặt với khoảng cách chỉ 0.3 millimet, mỏng hơn sợi tóc.

Khi khối u được lấy ra hoàn toàn, ba mươi nghìn người xem đồng loạt gửi biểu tượng vỗ tay. Comment tràn ngập: "Đôi tay vàng!" "Thần y!" "Đây mới là bác sĩ thật!"

Nhưng khoảnh khắc viral nhất không phải lúc mổ. Đó là khi bệnh nhân tỉnh dậy trong phòng hồi sức, Huy kiểm tra dây thần kinh mặt — bệnh nhân cười được, nhắm mắt được, nhíu mày được. Hoàn toàn bình thường.

Rồi Huy đặt tai nghe lên tai trái bệnh nhân — tai đã mất thính lực sáu năm — bật một bản nhạc. Bệnh nhân bật khóc: "Tôi nghe được! Bác sĩ ơi, tôi nghe được rồi!"

Video clip mười lăm giây đó trở thành hiện tượng mạng. Năm triệu lượt xem trong ba ngày. Hashtag #BácSĩHuy trending khắp Việt Nam.

Tại Bệnh viện Trung ương, Trần Đình Phong ngồi trong phòng họp, mặt tái xám. Lượng bệnh nhân chỉ định mổ thần kinh tại bệnh viện giảm ba mươi phần trăm trong tuần đó — họ xin chuyển viện đến Neuro Center của Huy.

Phong gọi Sơn vào phòng: "Mày phải tìm cách phá thằng Huy. Nó mà lớn mạnh, chúng ta xong!"

Sơn nuốt nước bọt. Hắn vừa xem lại ca livestream, và thừa nhận trong lòng: mình không bao giờ mổ được như vậy. Vị trí Trưởng khoa mà hắn chiếm được giờ nặng như xiềng xích trên cổ."""),

("Chương 4: Đoàn Thanh Tra Và Cú Lật Ngược", """Một tháng sau ca livestream, Huy nhận được thông báo: Sở Y tế TP.HCM cử đoàn thanh tra kiểm tra toàn diện Neuro Center vì "có đơn tố cáo cơ sở hoạt động không phép."

Huy biết ngay ai đứng sau. Nhưng lần này, anh không còn là chàng bác sĩ ngây thơ.

Đoàn thanh tra bảy người đến vào chín giờ sáng. Dẫn đầu là Phó Giám đốc Sở Y tế Hoàng Đức Anh — người có quan hệ thân thiết với Phong.

"Bác sĩ Lê Quang Huy, chúng tôi nhận được tố cáo rằng cơ sở này thực hiện phẫu thuật thần kinh không có giấy phép hoạt động đúng phạm vi," Hoàng Đức Anh nói, vẻ mặt đắc thắng.

Huy mỉm cười — nụ cười mà Mai gọi là "nụ cười phòng mổ," lạnh lùng và chính xác tuyệt đối.

"Mời đoàn kiểm tra," Huy mở tủ hồ sơ, rút ra một tập tài liệu dày hai trăm trang, đóng bìa cứng, có công chứng. "Giấy phép hoạt động cơ sở khám chữa bệnh phạm vi chuyên khoa phẫu thuật thần kinh, cấp bởi Bộ Y tế — không phải Sở." Lật trang. "Chứng chỉ hành nghề quốc tế của tôi do Hội Phẫu thuật Thần kinh Hoa Kỳ cấp, được Bộ Y tế Việt Nam công nhận tương đương." Lật trang. "Giấy phép trang thiết bị y tế loại C và D, kiểm định bởi Viện Trang thiết bị và Công trình Y tế."

Mồ hôi bắt đầu chảy trên trán Hoàng Đức Anh.

Nhưng Huy chưa dừng lại. "Và đây," anh mở laptop, bật file video. "Bản ghi hình camera phòng mổ số 3 Bệnh viện Trung ương, ngày 12 tháng 3, ca bệnh nhân Trần Văn Tú. File này được backup tự động trên cloud server của hệ thống Zeiss mà Phó Giám đốc Phong không biết."

Trên màn hình, ca phẫu thuật diễn ra hoàn hảo. Huy không cắt nhầm bất kỳ mạch máu nào. Hồ sơ phẫu thuật bị giả mạo — bằng chứng rõ ràng, không thể chối cãi.

Mai bước vào, bên cạnh là luật sư Trần Quốc Việt, Đoàn Luật sư TP.HCM. "Thưa đoàn thanh tra, tôi đại diện Neuro Center thông báo: chúng tôi đã nộp đơn tố cáo Phó Giám đốc Trần Đình Phong và bác sĩ Nguyễn Hoàng Sơn lên Bộ Y tế về hành vi giả mạo hồ sơ y khoa, phá hủy bằng chứng, và vu khống bác sĩ gây chết người. Hồ sơ kèm bản ghi camera gốc và log hệ thống IT chứng minh file bị xóa thủ công."

Hoàng Đức Anh tái mặt, lùi ra cửa. "Tôi... chúng tôi sẽ xem xét lại đơn tố cáo ban đầu."

Đoàn thanh tra rút lui trong im lặng.

Tin tức đoàn thanh tra bị "vả mặt" tại Neuro Center lan khắp giới y khoa Sài Gòn. Video bản ghi camera gốc được Huy công bố trên trang web phòng khám với dòng chú thích: "Sự thật không thể bị xóa. Công lý chỉ đến muộn, không bao giờ vắng mặt."

Đêm hôm đó, điện thoại Phong rung liên tục. Bộ Y tế yêu cầu giải trình. Giám đốc bệnh viện triệu tập họp khẩn. Sơn khóa cửa phòng trực, không dám ra ngoài."""),

("Chương 5: Hội Nghị Y Khoa — Nghiền Nát Kẻ Phản Bội", """Bốn tháng sau sự kiện thanh tra, Huy được mời tham dự Hội nghị Phẫu thuật Thần kinh Châu Á - Thái Bình Dương (APCNS) tại Singapore — hội nghị y khoa uy tín nhất khu vực, quy tụ hơn hai nghìn bác sĩ từ ba mươi quốc gia.

Trùng hợp — hoặc không — Nguyễn Hoàng Sơn cũng được Bệnh viện Trung ương cử đi trình bày báo cáo khoa học tại cùng hội nghị.

Sơn trình bày về "Kỹ thuật vi phẫu nội soi u thân não" — chính xác là công trình nghiên cứu mà Huy đã phát triển suốt năm năm, bị Phong và Sơn chiếm đoạt.

Sơn đứng trên sân khấu hội trường lớn chứa tám trăm người, trình bày tự tin. Slide PowerPoint chỉn chu, dữ liệu đầy đủ, kết quả lâm sàng ấn tượng.

Khi đến phần hỏi đáp, một cánh tay giơ lên ở hàng ghế thứ ba.

"Tôi có câu hỏi." Lê Quang Huy đứng dậy, giọng vang khắp hội trường. "Bác sĩ Sơn, trong slide số 17, anh trình bày kỹ thuật tiếp cận u thân não qua đường retrosigmoid cải tiến. Anh có thể giải thích cơ chế bảo vệ dây thần kinh sọ số 7 trong quá trình bóc tách không? Cụ thể, khi gặp u bám dính vào dây thần kinh, anh xử lý bằng phương pháp nào?"

Sơn đông cứng trên sân khấu. Đây là chi tiết kỹ thuật cốt lõi nhất của công trình — thứ mà chỉ người phát minh ra nó mới hiểu tường tận.

"Tôi... chúng tôi sử dụng kỹ thuật stimulation mapping kết hợp..." Sơn ấp úng.

"Sai," Huy nói, giọng không to nhưng sắc như dao mổ. "Kỹ thuật mà tôi phát triển dùng phương pháp submilimetric dissection với đầu dò siêu âm vi phẫu tần số bốn mươi MHz, kết hợp monitoring điện sinh lý realtime. Không phải stimulation mapping. Anh đã trình bày công trình mà anh không hiểu."

Tám trăm bác sĩ quay đầu nhìn Huy, rồi nhìn Sơn. Không khí trong hội trường nặng như chì.

Chủ tọa phiên họp, Giáo sư Takeshi Yamamoto từ Đại học Tokyo, lên tiếng: "Xin lỗi, bác sĩ Huy, anh nói kỹ thuật mà 'anh phát triển'?"

"Đúng, thưa Giáo sư Yamamoto. Đây là công trình nghiên cứu cá nhân của tôi, thực hiện từ năm 2022 đến 2025 tại Bệnh viện Trung ương Sài Gòn. Tôi có toàn bộ lab notebook gốc, bản thảo ban đầu gửi cho tạp chí Neurosurgery quốc tế với timestamp email, và video ghi lại toàn bộ quá trình phát triển kỹ thuật trên cadaver." Huy rút từ cặp ra một USB, đưa cho ban tổ chức.

Giáo sư Yamamoto xem qua dữ liệu, đối chiếu với bài trình bày của Sơn. Sau năm phút, ông lên micro: "Ban tổ chức APCNS tạm đình chỉ bài trình bày này để xác minh quyền tác giả. Nếu kết quả xác minh đúng, bác sĩ Nguyễn Hoàng Sơn sẽ bị cấm tham dự vĩnh viễn và thông báo cho tất cả hội nghị y khoa quốc tế."

Sơn đứng trên sân khấu, hai chân run rẩy. Tám trăm đôi mắt đổ dồn vào hắn với ánh nhìn khinh bỉ tột cùng — trong y khoa, đạo văn nghiên cứu là tội nặng nhất, còn hơn cả sai sót phẫu thuật.

Huy bước ra khỏi hội trường, Mai đang đợi ở hành lang. "Xong rồi," anh nói. "Bắt đầu phase hai."

Mai gật đầu, mắt sáng rực. Phase hai: mở rộng Neuro Center thành bệnh viện chuyên khoa thần kinh tư nhân đầu tiên tại Việt Nam."""),

("Chương 6: Bệnh Viện Neuro Center Ra Đời", """Với danh tiếng từ hội nghị APCNS và ca livestream viral, Huy không khó khăn gì trong việc huy động vốn. Mai mang đến ba nhà đầu tư quốc tế: quỹ Temasek từ Singapore, tập đoàn thiết bị y tế Olympus từ Nhật Bản, và quỹ y tế Bill & Melinda Gates Foundation — tổng cộng hai trăm tỷ đồng.

Bệnh viện Neuro Center Sài Gòn khai trương trong tòa nhà chín tầng tại khu đô thị Thủ Đức, với ba phòng mổ hiện đại nhất Đông Nam Á, mười hai giường ICU, và đội ngũ năm mươi bác sĩ được Huy tự tay tuyển chọn và đào tạo.

Điều đặc biệt: tầng một dành riêng làm phòng khám miễn phí cho bệnh nhân nghèo, hoạt động mỗi thứ Bảy, do chính Huy khám và mổ.

Ngày khai trương, Giáo sư Yamamoto bay từ Tokyo đến cắt băng, phát biểu: "Bệnh viện này là bằng chứng rằng y học Việt Nam đang vươn tầm thế giới. Bác sĩ Huy không chỉ là phẫu thuật gia xuất sắc mà còn là người có trái tim y đức hiếm thấy."

Trong khi đó, Bệnh viện Trung ương Sài Gòn chìm trong khủng hoảng. Sơn bị APCNS cấm vĩnh viễn, kèm thông báo đạo văn gửi đến mọi tạp chí y khoa quốc tế. Hắn không dám ra ngoài, không dám lên mạng. Danh tiếng hắn — thứ quý nhất của một bác sĩ — tan thành tro bụi.

Phong cũng bắt đầu gánh hậu quả. Bộ Y tế chính thức điều tra vụ giả mạo hồ sơ. Ba bệnh nhân cũ nộp đơn kiện bệnh viện vì nghi ngờ hồ sơ của họ cũng bị sửa đổi. Cổ phiếu của công ty dược phẩm mà Phong là cổ đông lớn lao dốc hai mươi phần trăm.

Huy không hả hê. Anh không có thời gian hả hê. Mỗi ngày anh vẫn cầm dao mổ từ sáng đến tối, cứu người, đào tạo bác sĩ trẻ. Bên cạnh anh, Mai điều hành bệnh viện với sự sắc sảo và hiệu quả đáng kinh ngạc.

Một buổi tối muộn, khi cả hai ngồi trong phòng nghiên cứu tầng chín, nhìn xuống thành phố đêm lung linh, Mai nói nhẹ: "Anh Huy, anh có bao giờ hối hận không? Về việc rời bệnh viện cũ?"

Huy cười. "Tôi không rời. Tôi bị đuổi. Nhưng đôi khi, bị đuổi là điều tốt nhất xảy ra trong đời." Anh nhìn Mai. "Nếu không bị đuổi, tôi đã không gặp cô."

Mai quay mặt đi, nhưng Huy kịp thấy đôi tai cô đỏ ửng."""),

("Chương 7: Bí Mật Của Gia Đình Bác Sĩ", """Bệnh viện Neuro Center hoạt động sáu tháng, tiếp nhận hơn ba nghìn bệnh nhân, thực hiện bốn trăm ca phẫu thuật lớn, tỷ lệ thành công chín mươi tám phần trăm — cao nhất Đông Nam Á.

Nhưng có một ca bệnh đặc biệt khiến Huy phải đối mặt với quá khứ. Bệnh nhân là Trần Đình Khải, sáu mươi tám tuổi, bố đẻ của Trần Đình Phong — người đã đuổi Huy khỏi bệnh viện.

Ông Khải bị u não ác tính giai đoạn 3, vị trí u nằm sâu trong vùng vận động — nơi mà chỉ vài bác sĩ trên thế giới dám mổ. Phong đã đưa bố đi khắp Hàn Quốc, Nhật Bản, Singapore, nhưng tất cả đều từ chối vì rủi ro quá cao.

Sự lựa chọn cuối cùng: Lê Quang Huy.

Phong gọi điện cho Huy lúc nửa đêm, giọng run rẩy — hoàn toàn khác với kẻ hống hách đã ném hồ sơ vào mặt anh sáu tháng trước.

"Huy, tôi biết tôi không có quyền xin cậu bất cứ điều gì. Nhưng đó là bố tôi. Ông ấy vô tội trong chuyện của chúng ta. Xin cậu, cứu bố tôi."

Huy im lặng ba mươi giây. Rồi anh nói: "Mang bố anh đến bệnh viện tôi. Sáu giờ sáng."

Mai biết chuyện, hỏi: "Anh chắc chứ? Nếu ca mổ thất bại, Phong sẽ dùng nó để hại anh lần nữa."

"Tôi biết. Nhưng tôi là bác sĩ. Bệnh nhân đến, tôi mổ. Đó là lời thề Hippocrates."

Ca mổ kéo dài bảy tiếng — dài nhất trong sự nghiệp Huy. Khối u nằm ở vị trí hiểm hóc nhất, bao quanh bởi các mạch máu sống còn và vùng vỏ não điều khiển tay phải.

Huy mổ với sự tập trung tuyệt đối, đôi tay không run một millimet dù mồ hôi ướt đẫm lưng. Anh dùng kỹ thuật awake craniotomy — mổ não khi bệnh nhân tỉnh — để kiểm tra chức năng vận động realtime. Ông Khải vẫn cử động được ngón tay khi Huy cắt từng lớp u.

Khi miếng u cuối cùng được lấy ra, phòng mổ vỡ ra tiếng thở phào. Ông Khải vẫn tỉnh, vẫn cử động bình thường. Ca mổ thành công hoàn hảo.

Phong đứng ngoài phòng hồi sức, nhìn bố mình qua cửa kính. Khi Huy bước ra, Phong quỳ xuống — ngay giữa hành lang bệnh viện, trước mặt mười nhân viên y tế.

"Cảm ơn, Huy," Phong nói, nước mắt chảy ròng. "Tôi sai. Tôi hoàn toàn sai."

Huy nhìn xuống người đã từng phá hủy sự nghiệp mình. Trong lòng anh không có hận thù, không có hả hê. Chỉ có sự mệt mỏi của bảy tiếng cầm dao và sự bình yên của người đã làm đúng lương tâm.

"Đứng lên. Anh là Phó Giám đốc bệnh viện, quỳ giữa hành lang thế này không ra thể thống gì," Huy nói. "Bố anh khỏe rồi. Hãy chăm sóc ông ấy."

Rồi Huy quay lưng bước đi, Mai đang đợi anh ở cuối hành lang với ly cà phê nóng."""),

("Chương 8: Đế Chế Phong — Sơn Sụp Đổ", """Một tháng sau ca mổ cho bố Phong, Bộ Y tế chính thức công bố kết luận điều tra: Trần Đình Phong bị cách chức Phó Giám đốc, cấm đảm nhiệm vị trí quản lý y tế mười năm. Nguyễn Hoàng Sơn bị thu hồi chứng chỉ hành nghề, đình chỉ vĩnh viễn tại Bệnh viện Trung ương.

Phong nộp đơn từ chức trong im lặng. Ông từ một Phó Giám đốc quyền lực thành một bác sĩ thường trở lại phòng khám quận, khám ngoại trú cho bệnh nhân cao huyết áp và tiểu đường. Nhưng ít nhất, ông còn được hành nghề.

Sơn thì tệ hơn. Mất chứng chỉ hành nghề, hắn không thể làm bác sĩ ở bất kỳ cơ sở y tế nào trong cả nước. Vợ hắn — người cưới hắn vì thấy hắn là "Trưởng khoa trẻ nhất bệnh viện" — nộp đơn ly hôn. Căn penthouse Thảo Điền mà Phong hứa cho hắn chưa bao giờ trở thành hiện thực.

Hắn ngồi trong phòng trọ hai mươi mét vuông ở Gò Vấp, nhìn tấm bằng bác sĩ treo trên tường, nghĩ lại lời Huy: "Mày đã trình bày công trình mà mày không hiểu."

Đúng vậy. Sơn chưa bao giờ thực sự giỏi. Hắn chỉ giỏi trong việc đứng cạnh người giỏi và chiếm đoạt thành quả. Khi Huy bị đuổi, Sơn mất đi cái bóng mà hắn vẫn núp — và lộ ra bản chất thực sự: một bác sĩ tay nghề trung bình với tham vọng phi thường.

Trong khi đó, Kim Ngân Bệnh viện — à không, Bệnh viện Trung ương — đối mặt với cuộc di cư nhân tài chưa từng có. Bảy bác sĩ phẫu thuật giỏi nhất xin nghỉ việc chuyển sang Neuro Center trong vòng ba tháng. Họ nói: "Ở đó, bác sĩ được tôn trọng. Ở đây, bác sĩ giỏi bị đuổi."

Giám đốc bệnh viện phải lên truyền hình xin lỗi công khai và cam kết cải tổ bộ máy quản lý."""),

("Chương 9: Giải Thưởng Y Khoa Quốc Tế", """Một năm sau ngày khai trương, Neuro Center nhận được email từ Viện Hàn lâm Y khoa Hoàng gia Anh: Bác sĩ Lê Quang Huy được đề cử cho giải Hunterian Medal — giải thưởng phẫu thuật uy tín nhất thế giới, đặt theo tên John Hunter, cha đẻ phẫu thuật hiện đại.

Huy bay đến London, đứng trên sân khấu Viện Hàn lâm, trình bày công trình "Submilimetric Microsurgical Technique for Deep Brain Tumors" trước hội đồng gồm các giáo sư phẫu thuật hàng đầu thế giới.

Khi MC công bố: "The 2027 Hunterian Medal is awarded to Dr. Le Quang Huy from Neuro Center Saigon, Vietnam" — hội trường bốn trăm bác sĩ từ khắp thế giới đứng dậy vỗ tay.

Huy là bác sĩ Việt Nam đầu tiên nhận giải thưởng này trong hơn hai trăm năm lịch sử.

Anh cầm tấm huy chương, nhìn vào camera truyền hình quốc tế, và nói bằng tiếng Việt: "Tôi dành giải thưởng này cho mỗi bệnh nhân đã tin tưởng đặt mạng sống vào đôi tay tôi, và cho mỗi bác sĩ trẻ Việt Nam đang bị đánh giá thấp — hãy tiếp tục cầm dao, vì thế giới đang nhìn."

Tại Việt Nam, video phát biểu được phát trên VTV1 bản tin tối. Cả nước biết đến Lê Quang Huy. Thủ tướng gửi thư chúc mừng. Bộ trưởng Bộ Y tế mời Huy tham gia Hội đồng Tư vấn Phát triển Y tế Quốc gia.

Bệnh viện Neuro Center trở thành bệnh viện chuyên khoa thần kinh được xếp hạng top mười châu Á bởi Newsweek, đứng cạnh các bệnh viện từ Nhật Bản, Hàn Quốc và Singapore.

Phong xem bản tin từ phòng khám quận, nơi ông đang khám cho một bệnh nhân viêm họng. Trên TV, Huy cầm huy chương vàng, đứng giữa London.

Phong tắt TV, thở dài. Không phải thở dài vì ghen tị, mà vì ông cuối cùng cũng hiểu: mình đã cố hủy diệt một vì sao, nhưng vì sao đó chỉ bay cao hơn."""),

("Chương 10: Kẻ Phản Bội Quỳ Gối, Người Thầy Đứng Thẳng", """Hai năm sau ngày bị đuổi khỏi Bệnh viện Trung ương, Lê Quang Huy đứng trước cổng chính bệnh viện cũ — nơi anh từng bước ra với đôi tay trắng và trái tim đầy vết thương.

Nhưng hôm nay, anh đến với tư cách khác: Neuro Center vừa ký hợp đồng hợp tác đào tạo với Bệnh viện Trung ương. Giám đốc mới của bệnh viện — người thay Phong — chủ động đề nghị hợp tác, vì Neuro Center đã trở thành trung tâm đào tạo phẫu thuật thần kinh tốt nhất Việt Nam.

Huy đi qua hành lang quen thuộc, ngang qua phòng mổ số 3 — nơi anh đã mổ ba nghìn ca, nơi camera bị xóa, nơi giấc mơ bị đánh cắp. Anh dừng lại một giây, rồi bước tiếp.

Trong phòng họp, anh gặp lại Phong — giờ chỉ là bác sĩ ngoại trú, ngồi ở cuối bàn. Phong đứng dậy khi Huy bước vào, gật đầu chào lịch sự nhưng không dám nhìn thẳng.

Sau cuộc họp, Phong đợi Huy ở hành lang. "Huy, tôi xin lỗi. Một lần nữa. Tôi biết lời xin lỗi không thay đổi được gì, nhưng tôi muốn cậu biết: tôi đã sai lầm lớn nhất đời."

Huy nhìn Phong — người đàn ông từng quyền lực giờ già đi mười tuổi, lưng hơi còng, mắt đầy hối hận. "Anh Phong, tôi không tha thứ cho anh. Nhưng tôi không hận anh nữa. Vì hận ai đó là tự nhốt mình trong quá khứ, mà tôi đang bận xây tương lai."

Rồi Huy rút từ cặp ra một phong bì, đưa cho Phong. "Đây là thư mời anh tham gia chương trình khám miễn phí cho bệnh nhân nghèo tại Neuro Center, mỗi thứ Bảy. Anh vẫn là bác sĩ giỏi ở mảng nội thần kinh. Nếu anh muốn chuộc lỗi, hãy dùng tay nghề của mình cứu người, thay vì ngồi khám viêm họng."

Phong cầm phong bì, tay run. Ông biết đây không phải sự khoan dung, đây là một cách trừng phạt tinh tế hơn: bắt kẻ phản bội phải nhìn thành quả của người bị phản bội mỗi tuần.

Huy bước ra khỏi bệnh viện cũ, nắng Sài Gòn chiếu rực rỡ. Mai đang đợi anh bên chiếc xe, mỉm cười.

"Xong hết rồi?" cô hỏi.

"Xong." Huy nắm tay vợ. Họ đã kết hôn ba tháng trước, trong một lễ cưới giản dị tại tầng một Neuro Center — nơi dành cho bệnh nhân nghèo, nơi mà Huy yêu thích nhất trong cả tòa nhà.

"Về bệnh viện đi. Chiều nay còn ba ca mổ," anh nói.

"Ba ca? Anh mới mổ bảy tiếng sáng nay!"

"Bệnh nhân không đợi được, Mai." Huy cười, nụ cười của người đã đi qua địa ngục và tìm thấy thiên đường ở phía bên kia. "Tay tôi còn vững, mắt tôi còn sáng, thì tôi còn mổ."

Chiếc xe lăn bánh trên đường Xa lộ Hà Nội, hướng về Thủ Đức, nơi tòa nhà chín tầng của Neuro Center đứng sừng sững dưới nắng — biểu tượng mới của y khoa Việt Nam, được xây bởi đôi tay của một bác sĩ bị đuổi."""),
]

# ═══════════════════════════════════════════════════════════════════════════════
# STORY 2: KỸ SƯ AI BỊ CƯỚP CODE
# ═══════════════════════════════════════════════════════════════════════════════

S2_TITLE = "BỊ CƯỚP SOURCE CODE Ở SILICON VALLEY, TÔI VỀ VIỆT NAM DỰNG STARTUP TỶ ĐÔ"
S2_AUTHOR = "Phạm Tuấn Kiệt"
S2_COVER = "base_cover_36.png"
S2_INTRO = """<p><strong>"Ba năm tôi viết hai triệu dòng code, xây dựng engine AI xử lý ngôn ngữ tự nhiên tiếng Việt đầu tiên trên thế giới. Đổi lại, CEO cướp trắng bằng sáng chế, đuổi tôi khỏi công ty ngay trước ngày IPO."</strong></p>
<p>Phạm Tuấn Kiệt, kỹ sư AI thiên tài gốc Việt tại Silicon Valley, bị CEO startup David Chen và CTO đồng hương Hà Minh Trí phản bội, chiếm đoạt toàn bộ source code engine VietNLP và đẩy anh ra khỏi danh sách co-founder ngay trước thềm IPO trị giá hai tỷ đô.</p>
<p>Trở về Việt Nam với hai bàn tay trắng và ý chí sắt đá, Kiệt gặp Lý Hạ Nguyên, nữ venture capitalist sắc sảo tốt nghiệp Stanford. Cùng nhau, họ xây dựng VietAI — startup trí tuệ nhân tạo Việt Nam đầu tiên được định giá unicorn, vả mặt kẻ phản bội trên chính sân chơi công nghệ toàn cầu.</p>"""

S2_CHAPTERS = [
("Chương 1: Bị Đuổi Trước Ngày IPO", """Văn phòng NovaMind AI tầng hai mươi bảy tòa nhà Salesforce Tower, San Francisco, chín giờ tối thứ Sáu. Phạm Tuấn Kiệt vừa hoàn thành commit cuối cùng cho VietNLP Engine v3.0 — hai triệu ba trăm nghìn dòng code, ba năm phát triển, engine xử lý ngôn ngữ tự nhiên tiếng Việt chính xác nhất thế giới với tỷ lệ hiểu ngữ cảnh chín mươi bảy phần trăm.

"Push to production thành công," Kiệt thở phào, gỡ headphone ra khỏi tai. Bàn làm việc của anh bừa bộn lon Red Bull và hộp pizza nguội ngắt — dấu hiệu của bảy mươi hai giờ code liên tục không ngủ.

Ngày mai, NovaMind AI sẽ nộp hồ sơ S-1 lên SEC để IPO trên NASDAQ, định giá dự kiến hai tỷ đô. Kiệt, với tư cách co-founder và Chief AI Architect, sở hữu tám phần trăm cổ phần — xấp xỉ một trăm sáu mươi triệu đô.

Nhưng khi Kiệt vừa tắt máy, cửa phòng conference room bất ngờ mở.

David Chen, CEO NovaMind, bước vào cùng ba luật sư mặc vest đen và Hà Minh Trí — CTO, người Việt đồng hương mà Kiệt đã rủ vào NovaMind từ ngày đầu.

"Kiệt, ngồi xuống. Chúng ta cần nói chuyện," David nói, giọng lạnh tanh.

David đẩy một xấp giấy sang bên Kiệt. Đó là bản sửa đổi Agreement Assignment, ghi rõ: "Phạm Tuấn Kiệt tự nguyện chuyển nhượng toàn bộ quyền sở hữu trí tuệ đối với VietNLP Engine, bao gồm source code, model weights, training data, và bằng sáng chế liên quan, cho NovaMind AI Inc."

"Cái gì đây?" Kiệt trợn mắt. "Tôi là co-founder! VietNLP là đứa con tinh thần của tôi!"

"Kiểm tra lại employment agreement của cậu, điều khoản 8.2," luật sư trưởng lên tiếng, giọng đều đều. "Mọi sản phẩm trí tuệ tạo ra trong thời gian làm việc tại NovaMind thuộc sở hữu của công ty. Cậu ký điều khoản này khi gia nhập."

"Tôi viết VietNLP TRƯỚC khi gia nhập NovaMind! Prototype đầu tiên tôi code từ phòng ký túc xá Stanford, hai năm trước khi công ty thành lập!"

David nhún vai. "Cậu không có bằng chứng. Commit history trên GitHub nội bộ ghi rõ mọi dòng code đều được push từ account NovaMind."

"Vì Trí đã migrate toàn bộ repo cá nhân của tôi vào repo công ty từ ngày đầu! Trí, mày biết rõ chuyện này!" Kiệt quay sang đồng hương.

Hà Minh Trí tránh ánh mắt Kiệt, giọng lạnh lùng: "Anh Kiệt, commit history không nói dối. Repository NovaMind là duy nhất. Tôi không nhớ có repo cá nhân nào của anh."

"Mày nói gì?!" Kiệt đứng bật dậy. "Ba năm trước mày là thằng dev junior không ai thuê, tao kéo mày vào, dạy mày machine learning từ con số không!"

David ra hiệu cho bảo vệ. "Kiệt, cậu có hai lựa chọn. Ký giấy chuyển nhượng, nhận bốn trăm nghìn đô severance package và NDA. Hoặc chúng tôi kiện cậu vi phạm hợp đồng lao động và IP agreement, cậu sẽ không được một xu, thậm chí còn nợ chi phí pháp lý."

Bốn trăm nghìn đô. So với một trăm sáu mươi triệu đô cổ phần.

Kiệt nhìn xấp giấy, rồi nhìn David, rồi nhìn Trí. Ba năm tuổi trẻ, hai triệu dòng code, hàng nghìn đêm thức trắng. Tất cả bị cướp bằng một bản hợp đồng và một lời nói dối.

Anh ký giấy. Không phải vì anh chấp nhận, mà vì anh biết: cuộc chiến pháp lý ở Mỹ với một startup được Sequoia Capital chống lưng sẽ kéo dài năm năm và ngốn hàng triệu đô mà anh không có.

"Cảm ơn sự hợp tác," David nở nụ cười giả tạo. "Bảo vệ sẽ escort cậu ra khỏi tòa nhà. Badge và laptop để lại."

Kiệt bước vào thang máy, cánh cửa đóng lại. Trong gương phản chiếu, anh thấy khuôn mặt mình — gầy rộc, bọng mắt thâm quầng, nhưng đôi mắt vẫn sáng rực như màn hình terminal lúc nửa đêm.

"David, Trí," anh thì thầm. "Các người cướp code của tôi, nhưng các người không cướp được bộ não viết ra nó. Tôi sẽ viết lại, tốt hơn gấp trăm lần, và lần này — nó sẽ thuộc về Việt Nam." """),

("Chương 2: Về Nước Và Gặp Nhà Đầu Tư", """Kiệt bay về Hà Nội một tuần sau, mang theo bốn trăm nghìn đô — tương đương mười tỷ đồng, nghe nhiều nhưng trong giới startup AI thì chỉ đủ chạy sáu tháng.

Anh thuê một phòng làm việc bốn mươi mét vuông tại tầng ba tòa nhà cũ trên phố Trần Đại Nghĩa, cạnh Đại học Bách Khoa Hà Nội — nơi anh từng học bốn năm trước khi sang Stanford.

"VietAI" — anh đặt tên công ty mới. Tầm nhìn: xây dựng nền tảng AI ngôn ngữ tự nhiên tiếng Việt mạnh nhất, phục vụ 100 triệu người Việt, không phụ thuộc công nghệ nước ngoài.

Tuần đầu tiên, Kiệt viết lại core architecture từ đầu. Không sao chép bất kỳ dòng code nào từ NovaMind — anh đã ký NDA và anh tôn trọng chữ ký của mình, dù đối phương không tôn trọng. Nhưng ba năm kinh nghiệm và kiến thức trong đầu anh không thuộc sở hữu của ai.

Engine mới, Kiệt đặt tên là PhoenixNLP — Phượng Hoàng — được thiết kế từ zero với kiến trúc transformer thế hệ mới, tối ưu cho tiếng Việt với hệ thống xử lý thanh điệu, từ ghép, và ngữ cảnh văn hóa mà không model AI phương Tây nào hiểu.

Tháng thứ hai, khi Kiệt đang ăn mì gói lúc hai giờ sáng trong phòng làm việc bừa bộn, chuông cửa reo.

Lý Hạ Nguyên, hai mươi tám tuổi, tóc dài ngang vai, kính cận gọng đen, mặc áo hoodie Stanford — cô vừa bay từ San Francisco về Hà Nội sau khi đọc một bài viết của Kiệt trên ArXiv về kiến trúc PhoenixNLP.

"Phạm Tuấn Kiệt? Tôi là Lý Hạ Nguyên, partner tại Horizon Ventures Việt Nam. Tôi đọc paper ArXiv của anh — kiến trúc attention mechanism cho tonal languages của anh là breakthrough. Tôi muốn đầu tư."

Kiệt nhìn cô gái trẻ đứng trước cửa phòng làm việc lúc hai giờ sáng, tay cầm laptop và ly cà phê Starbucks. "Cô bay từ San Francisco về đây lúc nửa đêm để nói với tôi điều này?"

"Paper của anh được post lúc sáu giờ chiều giờ San Francisco. Tôi đọc xong lúc tám giờ, book vé lúc chín giờ, bay mười hai tiếng, đến đây," Nguyên nói, giọng không một chút đùa. "Trong giới VC, nếu bạn không move fast, bạn mất deal."

Hai người ngồi xuống giữa đống lon Red Bull và giấy note dán đầy tường, thảo luận đến năm giờ sáng. Nguyên đề xuất: Horizon Ventures sẽ đầu tư năm triệu đô vòng seed, định giá VietAI hai mươi triệu đô pre-money. Kiệt giữ sáu mươi phần trăm cổ phần và toàn quyền kỹ thuật.

"Tại sao cô tin tôi?" Kiệt hỏi. "Cả Silicon Valley đang nói tôi là kẻ bị đuổi, không có gì trong tay."

Nguyên nhìn thẳng vào mắt anh. "Vì tôi đọc được thứ mà David Chen không đọc được: kiến trúc PhoenixNLP không chỉ tốt hơn VietNLP — nó tốt hơn cả GPT cho ngôn ngữ tonal. Anh không mất gì khi rời NovaMind. Họ mới là người mất anh." """),

("Chương 3: PhoenixNLP Gây Bão Cộng Đồng Tech", """Sáu tháng sau khi nhận vốn, VietAI ra mắt PhoenixNLP beta — nền tảng AI tiếng Việt mã nguồn mở trên GitHub.

Trong bảy mươi hai giờ đầu tiên, repository nhận được mười lăm nghìn star trên GitHub, cao hơn bất kỳ dự án AI nào từ Đông Nam Á. Cộng đồng developer Việt Nam bùng nổ — hàng trăm developer contribute code, báo cáo bug, và viết blog review.

Benchmark cho thấy PhoenixNLP đạt độ chính xác chín mươi chín phần trăm trên các bài test hiểu ngôn ngữ tiếng Việt — cao hơn ba điểm so với VietNLP của NovaMind, và cao hơn năm điểm so với Google Translate.

VnExpress, Dân Trí, CafeF đồng loạt đăng bài: "Kỹ sư Việt bị cướp code ở Mỹ, về nước viết engine AI tốt hơn." Bài viết trên VnExpress đạt ba triệu lượt đọc.

Tại San Francisco, David Chen đọc bài báo, mặt tái xanh. VietNLP Engine mà hắn cướp được đang bị PhoenixNLP vượt mặt — trên mọi benchmark. Tệ hơn, PhoenixNLP là mã nguồn mở, miễn phí, trong khi NovaMind bán license API giá trăm nghìn đô mỗi năm.

Hà Minh Trí gọi cho David lúc nửa đêm: "David, thằng Kiệt viết lại engine mới trong sáu tháng, và nó tốt hơn cái chúng ta mất ba năm phát triển. Nếu khách hàng biết PhoenixNLP miễn phí và tốt hơn, họ sẽ hủy contract với mình."

David nghiến răng: "Kiện nó! Vi phạm NDA, sao chép IP!"

Nhưng luật sư NovaMind phân tích source code PhoenixNLP và kết luận: "Không một dòng code nào giống VietNLP. Kiến trúc hoàn toàn khác. Chúng ta không có cơ sở kiện."

Kiệt không sao chép. Anh viết lại từ đầu, tốt hơn. Đó là thứ mà David không bao giờ hiểu: anh cướp code, nhưng không cướp được trí tuệ."""),

("Chương 4: NovaMind Phản Công Và Cú Phản Đòn", """David không từ bỏ. Hắn thuê một công ty PR tung chiến dịch bôi nhọ: leak tin Kiệt bị đuổi vì "vi phạm đạo đức nghề nghiệp" và "sao chép code đồng nghiệp." Bài viết xuất hiện trên TechCrunch và The Verge.

Cộng đồng tech quốc tế bắt đầu nghi ngờ. Một số đối tác tiềm năng của VietAI rút lui.

Kiệt bình tĩnh. Anh đã chuẩn bị cho kịch bản này.

"Nguyên, giờ đến lượt mình," anh nói với cô partner.

Nguyên tổ chức một buổi livestream kỹ thuật trên YouTube, mời cộng đồng developer toàn cầu tham dự. Kiệt ngồi trước camera, chia màn hình: bên trái là source code PhoenixNLP, bên phải là bản demo VietNLP mà NovaMind đã public trên API.

Anh chạy side-by-side comparison trực tiếp, phân tích từng module: tokenizer, embedding, attention mechanism, decoder. Mọi thứ khác biệt hoàn toàn — từ kiến trúc đến thuật toán, từ data pipeline đến inference engine.

Rồi Kiệt chiếu lên màn hình: git log cá nhân từ repo Stanford, có timestamp hai năm trước khi NovaMind thành lập, chứng minh prototype VietNLP ban đầu là của anh. Git log có chữ ký GPG verified, không thể giả mạo.

"David Chen, anh cướp code của tôi từ hai năm trước khi công ty anh tồn tại. Nhưng tôi không kiện anh — vì tôi bận viết thứ tốt hơn," Kiệt nói thẳng vào camera. "Cộng đồng developer tự phán xét."

Buổi livestream có năm mươi nghìn người xem trực tiếp. Hashtag #JusticeForKiet trending trên Twitter/X. Hàng trăm developer Mỹ và châu Âu ký thư yêu cầu NovaMind minh bạch.

TechCrunch rút bài bôi nhọ, đăng bài mới: "NovaMind CEO accused of stealing Vietnamese engineer's AI code — evidence mounting."

Cổ phiếu NovaMind, đang chuẩn bị IPO, lao dốc mười tám phần trăm. SEC yêu cầu bổ sung hồ sơ minh bạch IP trước khi duyệt S-1. IPO bị hoãn vô thời hạn."""),

("Chương 5: Demo Quốc Gia — AI Cho 100 Triệu Người Việt", """Ba tháng sau cuộc phản công, VietAI tổ chức sự kiện ra mắt PhoenixNLP chính thức tại Trung tâm Hội nghị Quốc gia Hà Nội. Năm trăm khách mời từ giới công nghệ, chính phủ, và truyền thông.

Kiệt demo trực tiếp PhoenixNLP tích hợp vào năm ứng dụng thực tế: trợ lý ảo tiếng Việt cho điện thoại, hệ thống chatbot chăm sóc khách hàng cho ngân hàng, công cụ dịch thuật y khoa chuyên ngành, phần mềm đọc hiểu văn bản pháp luật, và hệ thống phân tích cảm xúc mạng xã hội cho doanh nghiệp.

Mỗi demo đều nhận được tràng pháo tay. Nhưng khoảnh khắc cao trào là khi Kiệt demo tính năng cuối: PhoenixNLP đọc hiểu và tóm tắt Truyện Kiều bằng ngôn ngữ hiện đại — hiểu thơ lục bát, nắm bắt điển tích, và diễn giải cảm xúc nhân vật với độ chính xác khiến cả hội trường sửng sốt.

"Không AI nào trên thế giới làm được điều này," Kiệt nói. "Vì không AI nào hiểu tiếng Việt như người Việt. PhoenixNLP được xây bởi người Việt, cho người Việt."

Bộ trưởng Bộ Thông tin và Truyền thông lên sân khấu bắt tay Kiệt, công bố: Chính phủ Việt Nam chọn PhoenixNLP làm nền tảng AI quốc gia cho chương trình chuyển đổi số, hợp đồng trị giá ba trăm tỷ đồng.

Nguyên ngồi ở hàng ghế VIP, mỉm cười. Cô vừa nhận được email từ SoftBank Vision Fund: họ muốn dẫn đầu vòng Series A cho VietAI, định giá ba trăm triệu đô.

Từ phòng trọ bốn mươi mét vuông trên phố Trần Đại Nghĩa đến unicorn ba trăm triệu đô — trong chưa đầy một năm."""),

("Chương 6: VietAI Thành Unicorn", """SoftBank đầu tư năm mươi triệu đô vòng Series A. Sau đó là Sequoia Southeast Asia, Tiger Global, và GIC Singapore ở vòng Series B — tổng cộng hai trăm triệu đô, định giá VietAI một tỷ hai trăm triệu đô. Unicorn đầu tiên của Việt Nam trong lĩnh vực AI.

VietAI mở văn phòng tại tòa nhà Landmark 81, tầng sáu mươi hai, với ba trăm kỹ sư. PhoenixNLP được tích hợp vào hệ thống của Vietcombank, VinGroup, FPT, và mười hai cơ quan chính phủ.

Kiệt trở thành gương mặt trang bìa Forbes Vietnam, được vinh danh trong Forbes 30 Under 30 châu Á. Nhưng anh vẫn đi xe máy đến công ty mỗi sáng, vẫn code đến hai giờ đêm, vẫn ăn mì gói khi quá bận.

Nguyên giờ không chỉ là nhà đầu tư — cô là COO của VietAI. Và trong những buổi tối muộn ở văn phòng tầng sáu mươi hai, nhìn xuống thành phố Sài Gòn lung linh, mối quan hệ giữa họ đã vượt xa hai chữ "đồng nghiệp."

Tại San Francisco, NovaMind đang chết dần. IPO bị hủy vĩnh viễn. Khách hàng chuyển sang PhoenixNLP miễn phí hoặc giá rẻ. David Chen bị hội đồng quản trị sa thải, thay bằng CEO mới. Hà Minh Trí bị FBI điều tra về hành vi đánh cắp tài sản trí tuệ — vì git log Stanford của Kiệt đã được nộp làm bằng chứng trong đơn tố cáo liên bang."""),

("Chương 7: Bí Mật Của Dòng Code Đầu Tiên", """Một buổi tối, Nguyên hỏi Kiệt: "Tại sao anh đặt tên engine là Phoenix?"

Kiệt mở laptop, tìm đến một thư mục cũ trong ổ cứng cá nhân. Trong đó là file code đầu tiên anh viết: hello_vietnamese.py, timestamp 15/09/2019, lúc anh mới hai mươi hai tuổi, là sinh viên năm nhất Stanford.

"File này là dòng code đầu tiên tôi viết để máy tính hiểu tiếng Việt," Kiệt nói. "Comment đầu tiên trong file: '# Mẹ ơi, con sẽ làm máy tính nói tiếng Việt cho mẹ.' Mẹ tôi ở Hà Tĩnh, không biết tiếng Anh, không dùng được smartphone vì mọi thứ đều bằng tiếng Anh. Tôi code AI tiếng Việt vì mẹ."

Nguyên im lặng, mắt rưng rưng.

"Phoenix — Phượng Hoàng — vì ông ngoại tôi kể chuyện Phượng Hoàng tái sinh từ tro tàn. Code bị cướp, bị đốt, nhưng ý tưởng không bao giờ chết. Nó sẽ tái sinh, mạnh hơn."

Kiệt bật app VietAI Assistant trên điện thoại mẹ anh ở Hà Tĩnh. Mẹ anh, sáu mươi hai tuổi, giờ có thể nói chuyện với điện thoại bằng tiếng Việt giọng Nghệ Tĩnh, đọc tin tức, gọi video, thậm chí đặt hàng online — tất cả nhờ PhoenixNLP hiểu tiếng Việt vùng miền.

"Con ơi, cái điện thoại này nó nói chuyện hay lắm, y như người Hà Tĩnh mình!" Mẹ anh nói qua video call, cười móm mém.

Kiệt quay mặt đi, lau mắt. Nguyên nắm tay anh dưới gầm bàn."""),

("Chương 8: NovaMind Sụp Đổ Hoàn Toàn", """Mười tám tháng sau khi Kiệt rời NovaMind, công ty chính thức nộp đơn phá sản Chapter 11. Doanh thu bằng không khi toàn bộ khách hàng chuyển sang PhoenixNLP. Tài sản trí tuệ — bao gồm VietNLP Engine mà David cướp từ Kiệt — được rao bán đấu giá.

FBI kết thúc điều tra, truy tố Hà Minh Trí về tội wire fraud và theft of trade secrets theo Luật Liên bang. Trí bị bắt tại sân bay LAX khi cố chạy trốn về Việt Nam, đối mặt bản án tối đa mười năm tù liên bang.

David Chen bị SEC cấm làm giám đốc công ty đại chúng mười năm vì che giấu tranh chấp IP trong hồ sơ IPO. Hắn từ tỷ phú tương lai trở thành người thất nghiệp, bị cộng đồng tech Silicon Valley tẩy chay.

Kiệt đọc tin trên Bloomberg, không hả hê. Anh chỉ nói: "David cướp hai triệu dòng code. Trí phản bội đồng hương. Cả hai đều quên rằng: code có thể sao chép, nhưng tài năng viết code thì không."

Anh đóng laptop, quay sang Nguyên: "Mình về viết code tiếp đi. PhoenixNLP v4.0 cần ship trước Tết." """),

("Chương 9: Giải Thưởng Turing Award Đề Cử", """Hai năm sau ngày về Việt Nam, Phạm Tuấn Kiệt nhận email từ Association for Computing Machinery (ACM): anh được đề cử cho Turing Award — "giải Nobel của khoa học máy tính" — nhờ công trình đột phá về kiến trúc AI cho ngôn ngữ thanh điệu.

Kiệt bay đến San Francisco — thành phố mà anh bị đuổi — để nhận giải. Lễ trao giải tại Moscone Center, nơi hàng nghìn nhà khoa học máy tính hàng đầu thế giới tề tựu.

Khi Kiệt bước lên sân khấu, toàn bộ hội trường đứng dậy standing ovation kéo dài hai phút. Họ biết câu chuyện của anh — kỹ sư bị cướp code, về nước viết lại, và tạo ra thứ tốt hơn.

"Tôi viết dòng code đầu tiên cho AI tiếng Việt vì muốn mẹ tôi dùng được điện thoại," Kiệt nói trước hai nghìn người. "Hôm nay, một trăm triệu người Việt Nam đang nói chuyện với máy tính bằng tiếng mẹ đẻ. Đó mới là giải thưởng thật sự của tôi."

Ở hàng ghế sau, Nguyên lau nước mắt. Bên cạnh cô, mẹ của Kiệt — bà Nguyễn Thị Lan, sáu mươi bốn tuổi, lần đầu tiên bay ra nước ngoài — đang cầm điện thoại quay video, miệng nói nhỏ bằng giọng Hà Tĩnh: "Con ơi, mẹ tự hào lắm!" Câu nói được PhoenixNLP dịch realtime ra tiếng Anh trên subtitle, khiến khán giả xung quanh rưng rưng."""),

("Chương 10: Mua Lại NovaMind Và Bài Học Cuối", """Ba tháng sau lễ trao giải Turing, VietAI mua lại tài sản trí tuệ của NovaMind tại phiên đấu giá phá sản — giá hai mươi triệu đô, bằng một phần trăm giá trị IPO mà David từng mơ.

Kiệt bay đến San Francisco ký hợp đồng. Anh ngồi trong phòng họp tầng hai mươi bảy Salesforce Tower — cùng phòng mà hai năm trước, David đã ném bản chuyển nhượng vào mặt anh.

Hắn ký mua lại chính source code của mình.

"Anh Kiệt." Giọng quen thuộc vang lên sau lưng.

Hà Minh Trí đứng ở cửa phòng họp, được hai nhân viên FBI áp giải. Trí đang tại ngoại chờ ra tòa, được phép gặp Kiệt mười lăm phút để bàn giao tài liệu kỹ thuật.

"Anh Kiệt, em xin lỗi," Trí nói, giọng khàn đặc. "Em tham lam, em ngu. David hứa cho em năm phần trăm cổ phần pre-IPO, em bán đứng anh vì mấy triệu đô."

Kiệt nhìn đồng hương — người mà anh từng dạy viết code, từng chia cơm trưa trong cafeteria Stanford, từng thức đêm debug cùng. Giờ Trí đứng đó, tay đeo vòng theo dõi GPS, mặt hốc hác.

"Trí, tôi không tha thứ cho mày," Kiệt nói thẳng. "Nhưng khi mày ra tù, nếu mày muốn viết code lại, VietAI có chương trình đào tạo kỹ sư tái hòa nhập. Mày có thể đăng ký. Không ưu tiên, không đặc cách — phải thi đầu vào như mọi người."

Trí cúi đầu, nước mắt rơi xuống sàn đá hoa cương lạnh.

Kiệt bước ra khỏi Salesforce Tower, ánh nắng San Francisco chiều thu chiếu vàng rực trên mặt vịnh. Nguyên đang đợi anh bên ngoài, tay cầm ly cà phê Việt Nam — cà phê phin pha sẵn từ startup của một cựu nhân viên VietAI.

"Mua xong rồi. VietNLP Engine giờ thuộc về VietAI," Kiệt nói. "Tôi sẽ open source nó luôn. Cho cả thế giới dùng miễn phí."

"Anh mua hai mươi triệu đô rồi cho free?" Nguyên cười.

"Code sinh ra để chia sẻ, không phải để nhốt trong két sắt. David mất tất cả vì ôm code quá chặt. Tôi không lặp lại sai lầm đó."

Họ bước đi trên đường Market Street, nắng thu chiếu vàng hai bóng người dài. Kiệt rút điện thoại, gọi cho mẹ ở Hà Tĩnh.

"Mẹ ơi, con về Việt Nam ngày mai. Mẹ nấu cơm chờ con nhé."

"Ừ con, mẹ nấu canh cua rau đay cho con. Con ơi, cái điện thoại nó dịch bài hát tiếng Anh ra tiếng Việt hay lắm, mẹ nghe suốt ngày!"

Kiệt cười, mắt cay cay. Đó là PhoenixNLP v4.0. Hai triệu dòng code, được viết bởi ba trăm kỹ sư Việt Nam, phục vụ một trăm triệu người — bắt đầu từ một dòng comment trong phòng ký túc xá Stanford: "Mẹ ơi, con sẽ làm máy tính nói tiếng Việt cho mẹ." """),
]

# ═══════════════════════════════════════════════════════════════════════════════
# STORY 3: NTK THỜI TRANG BỊ PHẢN BỘI
# ═══════════════════════════════════════════════════════════════════════════════

S3_TITLE = "BỊ HỦY HỢP ĐỒNG Ở TUẦN LỄ THỜI TRANG, TÔI MANG BST GỐC LÊN SÀN DIỄN PARIS"
S3_AUTHOR = "Nguyễn Khánh Linh"
S3_COVER = "base_cover_37.png"
S3_INTRO = """<p><strong>"Năm năm tôi thiết kế mười hai bộ sưu tập, đưa thương hiệu từ xưởng may gia đình lên sàn diễn quốc tế. Đổi lại, họ xóa tên tôi khỏi label, tuyên bố tôi chưa bao giờ tồn tại."</strong></p>
<p>Nguyễn Khánh Linh, nhà thiết kế thời trang tài năng nhất thế hệ millennials Việt Nam, bị chính Giám đốc Fashion House Trương Quỳnh Anh và NTK đối thủ Đặng Hải Long phản bội, cướp trắng BST "Áo Dài Mới" — bộ sưu tập kết hợp áo dài truyền thống với haute couture đương đại.</p>
<p>Mất thương hiệu, mất xưởng, Khánh Linh gặp Trần Minh Khôi, nhiếp ảnh gia thời trang quốc tế. Cùng nhau, họ xây dựng thương hiệu "LINH" từ con số không, đưa thời trang Việt Nam lên sàn catwalk Paris Fashion Week và khiến những kẻ phản bội phải cúi đầu xấu hổ trước cả thế giới.</p>"""

S3_CHAPTERS = [
("Chương 1: Bị Xóa Tên Trước Giờ Diễn", """Hậu trường Vietnam International Fashion Week, Trung tâm Hội nghị GEM Center quận 1, bảy giờ tối — một giờ trước show diễn. Nguyễn Khánh Linh đang chỉnh lại đường chỉ cuối cùng trên chiếc áo dài lụa Hà Đông phối cùng corset xương cá Pháp — thiết kế tâm đắc nhất trong BST "Áo Dài Mới" mà cô đã ấp ủ hai năm ròng.

Mười hai thiết kế. Mỗi thiết kế mất ba tháng nghiên cứu, hai tuần draping trên mannequin, và hàng trăm giờ may tay thủ công. BST kết hợp kỹ thuật thêu tay truyền thống Huế với cắt cúp haute couture Paris — thứ chưa ai làm được.

"Linh, lên phòng họp gấp. Chị Quỳnh Anh gọi." Trợ lý chạy đến, mặt tái mét.

Khánh Linh bước vào phòng VIP tầng hai. Ngồi ở đầu bàn là Trương Quỳnh Anh, bốn mươi hai tuổi, Giám đốc Fashion House "QA Couture" — nơi Khánh Linh làm việc năm năm với tư cách Lead Designer. Bên cạnh là Đặng Hải Long, ba mươi lăm tuổi, NTK mới được chiêu mộ từ một thương hiệu Hàn Quốc.

"Khánh Linh, BST 'Áo Dài Mới' từ hôm nay sẽ được trình diễn dưới tên Đặng Hải Long, không phải em," Quỳnh Anh nói thản nhiên, tay lật giở cuốn catalog mới in — trong đó, mọi credit thiết kế đều ghi tên Hải Long.

"Chị nói gì?" Khánh Linh trợn mắt. "Mười hai thiết kế này là của em! Em vẽ sketch, em draping, em chọn vải, em thêu tay từng đường kim!"

"Hợp đồng lao động điều khoản 7: mọi thiết kế tạo ra trong thời gian làm việc thuộc sở hữu của QA Couture," Hải Long đẩy bản hợp đồng sang, nụ cười đắc thắng. "Tên trên label là QA Couture, không phải Nguyễn Khánh Linh."

"Mày!" Khánh Linh chỉ thẳng mặt Hải Long. "Mày mới vào đây sáu tháng, chưa vẽ nổi một sketch hoàn chỉnh, giờ mày gắn tên mày lên tác phẩm của tôi?"

Quỳnh Anh đứng dậy: "Đủ rồi. Linh, em bị sa thải kể từ bây giờ. Bảo vệ sẽ đưa em ra khỏi hậu trường. Chìa khóa xưởng, laptop, và tất cả sketch gốc — để lại."

Khánh Linh nhìn Quỳnh Anh — người chị mà cô từng ngưỡng mộ, người đã dạy cô cách dựng pattern từ năm hai mươi ba tuổi.

"Chị Quỳnh Anh, em coi chị như chị ruột. Tại sao?"

Quỳnh Anh liếc sang Hải Long, rồi nói lạnh lùng: "Vì Hải Long mang đến hợp đồng phân phối với Lotte Department Store Hàn Quốc, trị giá hai mươi tỷ đồng. Em giỏi thiết kế, nhưng em không mang được tiền về."

Bảo vệ áp sát. Khánh Linh bị dẫn ra cửa hậu, ngang qua dãy mannequin trưng bày mười hai thiết kế của cô — giờ đã gắn label "Designed by Đặng Hải Long."

Cô bước ra con hẻm sau GEM Center, trời Sài Gòn đang mưa phùn. Trong túi xách chỉ còn điện thoại, ví tiền, và một cuộn vải lụa Hà Đông nhỏ mà cô luôn mang theo như bùa may mắn — mảnh vải mà bà ngoại, nghệ nhân thêu tay cuối cùng của làng Quất Động, đã tặng cô trước khi mất.

"Bà ơi, họ cướp hết rồi," Khánh Linh thì thầm, siết chặt cuộn vải lụa trong tay. "Nhưng con còn đôi tay bà dạy. Đôi tay này, không ai cướp được." """),

("Chương 2: Xưởng May Trong Phòng Trọ", """Khánh Linh thuê phòng trọ hai mươi mét vuông ở quận Bình Thạnh, biến nửa phòng thành xưởng may: một máy may công nghiệp cũ mua thanh lý ba triệu đồng, một bàn cắt gấp, và mannequin duy nhất mượn từ cô bạn học cũ.

Tiền tiết kiệm còn năm mươi triệu — đủ sống ba tháng nếu tiết kiệm tối đa.

Ngày thứ năm trong phòng trọ, khi Khánh Linh đang draping một mẫu áo dài mới trên mannequin, điện thoại rung. Một tin nhắn Instagram từ tài khoản @minhkhoi.photo, có hai trăm nghìn followers: "Chị Linh, tôi là nhiếp ảnh gia Trần Minh Khôi. Tôi chụp BST Áo Dài Mới cho VIFW năm ngoái. Tôi biết đó là thiết kế của chị, không phải Hải Long. Tôi có bộ ảnh gốc với metadata timestamp chứng minh. Gặp nhau được không?"

Minh Khôi, ba mươi hai tuổi, nhiếp ảnh gia thời trang freelance có tên tuổi, từng chụp cho Vogue Việt Nam và Harper's Bazaar. Anh mang đến quán cà phê một chiếc USB chứa bốn trăm tấm ảnh RAW — chụp suốt quá trình Khánh Linh làm việc trong xưởng QA Couture, từ lúc draping đến lúc thêu tay.

"Mỗi file RAW có EXIF data: ngày giờ, GPS location tại xưởng QA Couture, và trong nhiều tấm, chị đang trực tiếp may trên chính những bộ áo dài đó. Hải Long không xuất hiện trong bất kỳ tấm ảnh nào trước tháng 9 — ba tháng sau khi BST hoàn thành," Khôi giải thích.

Khánh Linh nhìn những tấm ảnh, nước mắt lưng tròng. Đó là bằng chứng cô cần.

"Tại sao anh giúp tôi?" cô hỏi.

"Vì tôi là nhiếp ảnh gia. Công việc của tôi là ghi lại sự thật. Và sự thật là: BST Áo Dài Mới là kiệt tác của chị, không phải của kẻ ăn cắp."

Khôi đề nghị hợp tác: anh sẽ chụp lookbook miễn phí cho BST mới của Khánh Linh, đăng trên trang cá nhân hai trăm nghìn followers để tạo buzz. Cô chỉ cần thiết kế — thứ mà cô giỏi nhất trên đời.

Khánh Linh siết chặt cuộn lụa Hà Đông trong tay, gật đầu. "Tôi sẽ làm BST mới. Đẹp hơn gấp mười lần. Và lần này, tên trên label sẽ là LINH — chỉ LINH." """),

("Chương 3: BST 'Phượng' Gây Bão Mạng", """Hai tháng trong phòng trọ, Khánh Linh hoàn thành BST mới: "PHƯỢNG" — năm thiết kế áo dài haute couture kết hợp kỹ thuật thêu tay cổ truyền Quất Động với cắt cúp giải cấu trúc (deconstruction) của Rei Kawakubo.

Khôi chụp lookbook trong bối cảnh bất ngờ: không phải studio sang trọng, mà ở chính con hẻm quận Bình Thạnh nơi Khánh Linh ở trọ — xe máy, dây phơi quần áo, tường rêu phong, bà bán xôi đầu hẻm. Model mặc áo dài haute couture đứng giữa đời thường. Sự tương phản tạo nên hình ảnh mạnh đến nghẹt thở.

Khôi đăng bộ ảnh trên Instagram với caption: "Thiết kế bị đánh cắp. Nhà thiết kế bị đuổi. Nhưng tài năng thì không ai cướp được. BST PHƯỢNG by @khanhlinh.design — may tay trong phòng trọ 20m²."

Bốn mươi tám giờ. Hai trăm nghìn like. Năm nghìn share. Hashtag #PHƯỢNG trending. Tạp chí Elle Việt Nam, Vogue Singapore, và Hypebeast đồng loạt đăng bài.

Điện thoại Khánh Linh rung không ngừng: đơn đặt hàng từ fashionista khắp châu Á, lời mời hợp tác từ nhà sản xuất vải, tin nhắn ủng hộ từ cộng đồng thời trang quốc tế.

Tại văn phòng QA Couture, Quỳnh Anh đập bàn: "Ai cho con bé đó dùng kỹ thuật thêu Quất Động? Đó là kỹ thuật của xưởng tao!"

"Chị ơi, kỹ thuật thêu Quất Động là di sản gia đình cô ấy. Bà ngoại cô ấy là nghệ nhân," trợ lý rụt rè nhắc.

Quỳnh Anh tái mặt. Cô ta mới nhớ ra: kỹ thuật thêu đặc biệt đó không thuộc QA Couture — nó thuộc về dòng họ Nguyễn ở làng Quất Động, được truyền qua ba thế hệ. Khánh Linh mang kỹ thuật đó vào QA Couture, nhưng nó chưa bao giờ thuộc sở hữu công ty.

Và BST "Áo Dài Mới" mà Hải Long đang gắn tên — nếu không có kỹ thuật thêu Quất Động, nó chỉ là những chiếc áo dài bình thường."""),

("Chương 4: Cuộc Chiến Bản Quyền", """Quỳnh Anh thuê luật sư gửi thư cảnh cáo Khánh Linh: yêu cầu ngừng sử dụng "kỹ thuật thiết kế thuộc sở hữu trí tuệ của QA Couture."

Khánh Linh đáp trả bằng một buổi livestream trên Instagram: cô ngồi trước máy may, trực tiếp thêu tay mẫu hoa sen trên vải lụa, giải thích từng kỹ thuật.

"Đây là mũi thêu nối, kỹ thuật của bà ngoại tôi — nghệ nhân Nguyễn Thị Hồng, làng Quất Động, Thường Tín. Bà dạy tôi từ năm tám tuổi. Kỹ thuật này được Bộ Văn hóa công nhận là di sản văn hóa phi vật thể quốc gia năm 2015. Không ai, không công ty nào sở hữu nó."

Cô đưa lên màn hình: giấy chứng nhận nghệ nhân của bà ngoại, video bà dạy cô thêu khi cô còn nhỏ, và bản đăng ký bản quyền mẫu thiết kế BST PHƯỢNG mà cô đã nộp cho Cục Sở hữu Trí tuệ — trước cả khi Quỳnh Anh kịp phản ứng.

Luật sư QA Couture rút đơn trong im lặng. Quỳnh Anh biết: nếu đưa ra tòa, bà sẽ thua, và scandal sẽ phá hủy thương hiệu.

Nhưng Hải Long không dừng lại. Hắn đăng story Instagram chế giễu Khánh Linh: "Thiết kế trong phòng trọ thì cũng chỉ là đồ phòng trọ."

Comment tràn ngập phản hồi tiêu cực — nhưng hướng về Hải Long, không phải Khánh Linh. Cộng đồng thời trang Việt Nam đã chọn phe."""),

("Chương 5: Sàn Diễn Paris — Nghiền Nát Mọi Nghi Ngờ", """Bốn tháng sau scandal, Khánh Linh nhận được email từ Fédération de la Haute Couture et de la Mode: cô được mời trình diễn BST tại Paris Fashion Week — Guest Designer slot dành cho tài năng mới nổi từ châu Á.

Đây là cơ hội mà mọi NTK Việt Nam đều mơ ước. Và nó đến với cô, không phải QA Couture.

Khánh Linh mở rộng BST PHƯỢNG từ năm lên mười hai thiết kế. Cô thuê bốn thợ thêu tay từ làng Quất Động — những bà cụ sáu mươi, bảy mươi tuổi, nghệ nhân cuối cùng giữ kỹ thuật cổ — bay sang Paris cùng cô.

Show diễn tại Palais de Tokyo, Paris. Ba trăm khách mời: Anna Wintour, Edward Enninful, Virgil Abloh's team, và hàng chục biên tập viên thời trang từ mọi tạp chí hàng đầu thế giới.

Khi model đầu tiên bước ra sàn catwalk trong chiếc áo dài lụa trắng kết hợp cấu trúc origami Nhật Bản, thêu tay hoa sen vàng ròng — cả hội trường im lặng. Không phải im lặng vì thất vọng, mà im lặng vì choáng ngợp.

Mười hai thiết kế, mười hai phút diễn. Mỗi bước chân model là một câu chuyện: áo dài gặp corset, lụa Hà Đông gặp tweed Chanel, thêu Quất Động gặp laser cutting. Đông gặp Tây, truyền thống gặp đương đại, phòng trọ gặp haute couture.

Khi Khánh Linh bước ra cuối show để chào khán giả — trong chiếc áo dài trắng giản dị, tóc búi thấp, tay nắm tay bốn bà thợ thêu Quất Động — ba trăm người đứng dậy vỗ tay. Anna Wintour gật đầu — cử chỉ hiếm hoi mà giới thời trang coi như sự tôn vinh tối thượng.

Vogue Paris chạy headline: "LINH: The Vietnamese Designer Who Turned a 20m² Room Into Paris Fashion Week." Bài viết được share hơn hai trăm nghìn lần.

Tại Sài Gòn, Hải Long xem livestream show diễn trên laptop, tay run. Hắn biết: sự nghiệp thời trang của hắn kết thúc từ giây phút này. Không ai muốn mặc đồ của kẻ ăn cắp khi bản gốc đang tỏa sáng ở Paris."""),

("Chương 6: Thương Hiệu LINH Ra Đời", """Sau Paris Fashion Week, đơn đặt hàng ào ạt đổ về. Net-a-Porter, Ssense, Lane Crawford — các nhà bán lẻ luxury hàng đầu thế giới liên hệ muốn phân phối BST PHƯỢNG.

Khánh Linh mở xưởng may chính thức tại quận 3, diện tích hai trăm mét vuông, thuê hai mươi thợ may và mười nghệ nhân thêu tay. Thương hiệu "LINH" chính thức ra mắt, định vị: luxury Vietnamese fashion — áo dài Việt Nam ở phân khúc haute couture.

Khôi trở thành Creative Director, phụ trách hình ảnh và branding. Mối quan hệ giữa họ đã vượt xa chuyên môn — nhưng cả hai đều chưa nói ra.

Doanh thu tháng đầu tiên: một tỷ hai trăm triệu đồng — từ phòng trọ hai mươi triệu tháng lên doanh nghiệp tỷ đồng trong chín tháng.

Trong khi đó, QA Couture chìm trong khủng hoảng. Hợp đồng Lotte bị hủy khi Lotte phát hiện BST "Áo Dài Mới" là đạo nhái. Quỳnh Anh mất uy tín trong giới thời trang Việt Nam. Hải Long bị QA Couture đuổi — y hệt cách Khánh Linh bị đuổi."""),

("Chương 7: Di Sản Bà Ngoại — Bí Mật Mũi Thêu Vàng", """Một đêm, khi xưởng may đã vắng, Khánh Linh ngồi lại một mình, lật giở cuốn sổ cũ của bà ngoại. Cuốn sổ ghi chép mười bảy kỹ thuật thêu tay cổ truyền Quất Động, trong đó có ba kỹ thuật đã thất truyền mà bà là người cuối cùng biết.

"Kỹ thuật thêu vàng ròng trên lụa — dùng sợi vàng 24K kéo mỏng như tóc, thêu bằng kim số 13, mỗi mũi cách nhau đúng 0.3mm." Khánh Linh đọc ghi chú, tay run. Đây là kỹ thuật mà triều đình Nguyễn từng dùng để thêu long bào cho Hoàng đế, đã mất từ năm 1945.

Cô quyết định phục dựng kỹ thuật thêu vàng, đưa vào BST mới: "HOÀNG HẬU" — bộ sưu tập áo dài lấy cảm hứng từ trang phục cung đình Huế, phục dựng bằng kỹ thuật cổ và biến tấu bằng thẩm mỹ đương đại.

Ba tháng phục dựng, hàng trăm lần thất bại, mười ngón tay rướm máu vì sợi vàng sắc như dao. Nhưng cuối cùng, chiếc áo dài đầu tiên thêu vàng ròng hoàn thành — rực rỡ như mặt trời, tinh xảo đến mức khiến cả xưởng may nghẹn ngào.

BST "HOÀNG HẬU" được trình diễn tại Tuần lễ Thời trang Haute Couture Paris — lần này Khánh Linh không còn là Guest, mà là Official Member, NTK Việt Nam đầu tiên trong lịch sử được Fédération công nhận.

Thế giới gọi cô: "The Golden Thread of Vietnam." """),

("Chương 8: QA Couture Phá Sản", """Scandal đạo nhái BST "Áo Dài Mới" cuối cùng cũng bùng nổ khi một blogger thời trang quốc tế đăng bài so sánh chi tiết: ảnh EXIF metadata của Khôi chứng minh Khánh Linh thiết kế BST trước Hải Long sáu tháng.

Bài viết được Business of Fashion, WWD, và Fashionista đăng lại. QA Couture bị liệt vào danh sách đen của mọi tuần lễ thời trang quốc tế. Các đối tác bán lẻ đồng loạt hủy hợp đồng.

Quỳnh Anh nộp đơn phá sản cá nhân. Từ một Fashion House triệu đô, bà trở lại thành thợ may — may quần áo gia công cho một thương hiệu nội địa giá rẻ.

Hải Long không ai thuê, không ai hợp tác. Cái tên "Đặng Hải Long" gắn liền với "đạo nhái" trong mọi kết quả Google.

Khánh Linh không hả hê. Cô bận may áo dài cho show diễn tiếp theo."""),

("Chương 9: Giải Thưởng LVMH Prize", """Thương hiệu LINH được đề cử cho LVMH Prize for Young Fashion Designers — giải thưởng thời trang danh giá nhất thế giới, do tập đoàn LVMH (Louis Vuitton, Dior, Givenchy) trao tặng. Giải thưởng ba trăm nghìn euro và cơ hội mentorship từ các giám đốc sáng tạo hàng đầu.

Khánh Linh bay đến Paris, trình bày BST "HOÀNG HẬU" trước ban giám khảo gồm: Nicolas Ghesquière (Louis Vuitton), Maria Grazia Chiuri (Dior), và Jonathan Anderson (Loewe).

Khi chiếc áo dài thêu vàng ròng được đưa ra, Chiuri — nữ Giám đốc Sáng tạo đầu tiên của Dior — đứng dậy sờ vào đường thêu, nhắm mắt cảm nhận.

"This is not fashion. This is art that you can wear. This is a civilization speaking through thread," bà nói.

Khánh Linh thắng giải Grand Prize — NTK Việt Nam đầu tiên, NTK Đông Nam Á đầu tiên trong lịch sử LVMH Prize.

Trên sân khấu, cô nói: "Tôi dành giải thưởng này cho bà ngoại tôi, nghệ nhân Nguyễn Thị Hồng, làng Quất Động. Bà dạy tôi rằng: mỗi mũi kim là một lời nói, mỗi đường chỉ là một câu chuyện. Tôi kể câu chuyện Việt Nam bằng kim chỉ, và thế giới đã lắng nghe."

Khôi chụp khoảnh khắc cô cầm cúp — tấm ảnh đó trở thành bìa tạp chí Vogue tháng sau."""),

("Chương 10: Trở Về Và Tha Thứ", """Một năm sau LVMH Prize, thương hiệu LINH có mặt tại mười hai quốc gia, doanh thu hàng năm hai trăm tỷ đồng. Xưởng may mở rộng tại Huế, tạo việc làm cho một trăm nghệ nhân thêu tay truyền thống.

Khánh Linh và Khôi kết hôn trong một lễ cưới giản dị tại chính làng Quất Động — cả hai mặc áo dài do cô tự may, thêu bằng kỹ thuật vàng ròng phục dựng từ bà ngoại.

Ngày cưới, Khánh Linh nhận được một bó hoa và tấm thiệp, không ghi tên người gửi. Chữ viết tay quen thuộc: "Em ơi, chị xin lỗi. Chị đã sai. Chúc em hạnh phúc. — Q.A."

Khánh Linh nhìn tấm thiệp hồi lâu, rồi đặt vào ngăn kéo. Cô không trả lời, nhưng cô cũng không xé nó.

Có những vết thương không bao giờ lành hẳn, nhưng có thể biến thành sẹo đẹp — như đường thêu tay trên lụa, vĩnh viễn in dấu nhưng không còn đau.

Cô quay sang Khôi, mỉm cười: "Mình đi thăm xưởng thêu Huế đi. Đội thợ mới cần học kỹ thuật thêu vàng."

"Ngày cưới mà vẫn nghĩ đến công việc?" Khôi cười.

"Bà ngoại nói: tay thêu ngừng là tay cứng. Mình không được ngừng." """),
]

# ═══════════════════════════════════════════════════════════════════════════════
# STORY 4: PORTFOLIO MANAGER BỊ VU OAN
# ═══════════════════════════════════════════════════════════════════════════════

S4_TITLE = "BỊ VU OAN LÀM MẤT 200 TỶ QUỸ ĐẦU TƯ, TÔI DÙNG SAO KÊ BLOCKCHAIN LẬT NGƯỢC THẾ CỜ"
S4_AUTHOR = "Trần Bảo Minh"
S4_COVER = "base_cover_38.png"
S4_INTRO = """<p><strong>"Tôi quản lý quỹ đầu tư 200 tỷ, sinh lời 23% mỗi năm trong bốn năm liên tiếp. Đổi lại, chủ tịch quỹ vu oan tôi biển thủ, đuổi tôi ra trước mặt nhà đầu tư và báo công an."</strong></p>
<p>Trần Bảo Minh, Portfolio Manager thiên tài của Quỹ đầu tư Hưng Thịnh Capital, bị Chủ tịch Lý Gia Hưng và CFO Hoàng Thị Diễm dàn dựng bằng chứng biển thủ 47 tỷ đồng để chiếm đoạt toàn bộ chiến lược đầu tư và danh sách khách hàng VIP.</p>
<p>Mất việc, bị truy tố, danh dự tan nát. Minh gặp Đặng Thu Ngân, nữ luật sư tài chính sắc sảo chuyên về forensic accounting. Cùng nhau, họ dùng blockchain và dữ liệu on-chain để lật trần âm mưu, xây dựng quỹ đầu tư mới và buộc kẻ phản bội phải quỳ gối trước pháp luật.</p>"""

S4_CHAPTERS = [
("Chương 1: Bị Đuổi Trước Mặt Nhà Đầu Tư", """Phòng họp VIP tầng ba mươi sáu tòa nhà Bitexco, mười giờ sáng thứ Hai. Trần Bảo Minh đang trình bày báo cáo quý III cho hai mươi nhà đầu tư VIP của Quỹ Hưng Thịnh Capital — những doanh nhân và tỷ phú nắm giữ tổng cộng hai trăm tỷ đồng tài sản ủy thác.

"Quý III, danh mục tăng trưởng mười chín phần trăm, vượt benchmark VN-Index bảy điểm. Chiến lược long-short equity kết hợp derivatives hedging tiếp tục phát huy hiệu quả," Minh trình bày, slide PowerPoint hiển thị đường cong lợi nhuận ấn tượng.

Bốn năm. Lợi nhuận trung bình hai mươi ba phần trăm mỗi năm. Không một quý nào lỗ. Minh là Portfolio Manager trẻ nhất và giỏi nhất trên thị trường chứng khoán Việt Nam, người mà giới tài chính gọi là "Midas của Sài Gòn."

Nhưng giữa lúc Minh đang chiếu slide chiến lược quý IV, cánh cửa phòng họp bật mở. Lý Gia Hưng, Chủ tịch HĐQT Hưng Thịnh Capital, bước vào cùng Hoàng Thị Diễm — CFO, và hai sĩ quan công an kinh tế mặc thường phục.

"Dừng lại!" Hưng gầm, ném một xấp giấy lên bàn trước mặt hai mươi nhà đầu tư đang kinh ngạc. "Trần Bảo Minh, tôi vừa phát hiện anh biển thủ bốn mươi bảy tỷ đồng từ quỹ đầu tư thông qua các giao dịch OTC giả mạo trong hai năm qua!"

Minh sững người. "Cái gì? Tôi chưa bao giờ—"

"Đây!" Diễm mở laptop, chiếu lên projector một bảng sao kê giao dịch chi tiết, ghi rõ bốn mươi bảy giao dịch chuyển tiền từ tài khoản quỹ sang các tài khoản cá nhân — mang tên Trần Bảo Minh. "Mỗi giao dịch từ năm trăm triệu đến hai tỷ, được thực hiện qua nền tảng OTC ngoài sàn. Chữ ký điện tử và mã OTP đều từ thiết bị của anh Minh."

Hai mươi nhà đầu tư nhốn nháo. Có người đứng dậy, mặt đỏ tía: "Bốn mươi bảy tỷ? Tiền của chúng tôi?"

"Các anh chị yên tâm," Hưng trấn an nhà đầu tư. "Tôi đã báo công an kinh tế và luật sư của quỹ đang chuẩn bị khởi kiện. Trần Bảo Minh sẽ chịu trách nhiệm hình sự. Quỹ sẽ bồi thường toàn bộ từ quỹ dự phòng."

Hai sĩ quan công an bước tới: "Anh Trần Bảo Minh, mời anh về đồn để làm việc."

Minh nhìn Hưng, rồi nhìn Diễm. Trong mắt cả hai đều lóe lên tia đắc thắng mà chỉ người trong cuộc mới nhận ra. Anh hiểu: đây là vở kịch được dàn dựng hoàn hảo.

"Tôi không biển thủ đồng nào," Minh nói, giọng bình tĩnh dù tim đập dồn dập. "Những tài khoản đó không phải của tôi. Tôi yêu cầu kiểm tra forensic toàn bộ hệ thống giao dịch."

"Anh sẽ có cơ hội giải trình tại cơ quan điều tra," sĩ quan nói. "Mời anh."

Minh bị dẫn ra khỏi phòng họp trước mặt hai mươi nhà đầu tư — những người mà anh đã kiếm hàng chục tỷ lợi nhuận. Trong mắt họ giờ chỉ có sự phẫn nộ và khinh bỉ.

Hưng đứng bên cửa sổ tầng ba mươi sáu, nhìn Minh bước lên xe công an phía dưới, khẽ mỉm cười. Bốn năm anh ta kiếm lời cho quỹ, giờ danh sách khách hàng VIP, chiến lược đầu tư, và mọi thứ đều thuộc về Hưng.

Cái giá để loại bỏ Minh? Bốn mươi bảy tỷ — tiền mà Hưng và Diễm đã chuyển từ quỹ sang tài khoản shell companies ở Singapore, rồi giả mạo sao kê gán cho Minh. Hoàn hảo."""),

("Chương 2: Nữ Luật Sư Blockchain", """Minh bị tạm giữ bốn mươi tám tiếng, rồi được tại ngoại với lệnh cấm xuất cảnh. Tài khoản ngân hàng bị phong tỏa, tài sản bị kê biên. Từ một Portfolio Manager lương tháng trăm triệu, anh trở thành nghi phạm hình sự không một đồng trong túi.

Anh ngồi trong quán cà phê bình dân ở quận 3, nhìn ly cà phê đen mà không uống. Điện thoại rung — số lạ.

"Anh Trần Bảo Minh? Tôi là Đặng Thu Ngân, luật sư chuyên về tội phạm tài chính và forensic accounting. Tôi đọc tin vụ của anh trên CafeF, và tôi tin anh vô tội."

"Cô tin tôi? Cả Sài Gòn đang nghĩ tôi là kẻ biển thủ."

"Vì tôi hiểu tài chính, và sao kê mà Hưng Thịnh công bố có nhiều điểm bất thường. Giao dịch OTC bốn mươi bảy tỷ mà không có counterparty confirmation, không có settlement record từ ngân hàng lưu ký. Chỉ có sao kê nội bộ — thứ mà CFO có toàn quyền tạo và chỉnh sửa."

Minh ngẩng đầu, mắt sáng lên.

Ngân đến quán cà phê ba mươi phút sau. Ba mươi tuổi, tóc ngắn ngang vai, kính cận gọng đen, mặc áo sơ mi trắng với quần tây đen — trông như một auditor hơn luật sư. Cô mở laptop, chiếu lên một sơ đồ phức tạp.

"Anh Minh, tôi chuyên về blockchain forensics. Tôi đã trace các tài khoản mà Hưng Thịnh nói là của anh. Bốn mươi bảy tỷ đó không nằm trong tài khoản ngân hàng Việt Nam — nó được chuyển thành USDT trên mạng Tron, rồi rửa qua ba mixer trước khi đổ vào ví lạnh."

"Ví lạnh? Crypto?"

"Đúng. Và đây là điểm mấu chốt: blockchain không nói dối. Mọi giao dịch đều có hash, timestamp, và địa chỉ ví. Tôi đã trace ngược toàn bộ dòng tiền, và ví nguồn — ví đầu tiên nhận bốn mươi bảy tỷ — có giao dịch test amount từ một ví khác mà on-chain analysis cho thấy thuộc về... Hoàng Thị Diễm."

Minh siết chặt tay. "Diễm? CFO?"

"Đúng. Diễm tạo tài khoản giả mạo tên anh, chuyển tiền quỹ qua crypto để rửa, rồi gán bằng chứng cho anh. Nhưng cô ta quên rằng blockchain là sổ cái bất biến — mọi dấu vết đều còn."

Minh nhìn Ngân, lần đầu tiên sau bốn mươi tám giờ địa ngục, anh thấy ánh sáng cuối đường hầm.

"Cô giúp tôi?" anh hỏi.

"Tôi không giúp ai miễn phí. Phí luật sư của tôi là năm phần trăm số tiền thu hồi được. Nhưng vụ này, tôi lấy thêm một điều kiện: khi anh được minh oan, anh mở quỹ đầu tư mới, tôi là legal counsel."

Minh bắt tay Ngân. Bàn tay cô lạnh nhưng siết rất chắc."""),

("Chương 3: Bằng Chứng On-Chain Gây Sốc", """Ngân mất hai tuần để hoàn thành báo cáo forensic blockchain dài ba mươi hai trang. Báo cáo trace chi tiết dòng tiền bốn mươi bảy tỷ từ tài khoản quỹ → ví crypto → mixer → ví lạnh, với bằng chứng on-chain không thể chối cãi rằng ví nguồn thuộc về Diễm.

Minh nộp báo cáo cho cơ quan điều tra công an kinh tế TP.HCM. Điều tra viên đọc báo cáo, mời chuyên gia blockchain từ Bộ Công an xác minh.

Kết quả: xác nhận báo cáo của Ngân chính xác. Ví crypto đã nhận bốn mươi bảy tỷ có liên kết trực tiếp với email và số điện thoại của Hoàng Thị Diễm thông qua KYC data của sàn Binance.

Cơ quan điều tra lập tức chuyển hướng: từ truy tố Minh sang điều tra Diễm và Hưng. Lệnh phong tỏa tài sản Minh được dỡ bỏ.

Tin tức vỡ ra trên CafeF, VnExpress, Thanh Niên: "Vụ biển thủ 47 tỷ đồng: Portfolio Manager được minh oan, Chủ tịch quỹ bị điều tra."

Cổ phiếu của các công ty liên quan đến Hưng Thịnh lao dốc. Nhà đầu tư VIP ồ ạt rút vốn. Hưng bị cấm xuất cảnh, Diễm bị bắt tạm giam.

Minh ngồi trong văn phòng luật sư Ngân, đọc tin trên điện thoại. Anh không vui. Bốn mươi bảy tỷ là tiền của nhà đầu tư — những người đã tin tưởng giao tiền cho anh quản lý. Dù tiền sẽ được thu hồi, niềm tin đã bị tổn thương.

"Tôi sẽ trả lại từng đồng cho nhà đầu tư," Minh nói. "Dù không phải lỗi tôi, nhưng tôi là người họ tin tưởng. Trách nhiệm vẫn là của tôi."

Ngân nhìn anh, ánh mắt dịu lại. Đây là lý do cô chọn vụ này: không phải vì tiền, mà vì người đàn ông này có thứ hiếm hơn tài năng — đó là lương tâm."""),

("Chương 4: Phản Công Tại Đại Hội Cổ Đông", """Hai tháng sau khi được minh oan, Minh xuất hiện tại Đại hội Cổ đông bất thường của Hưng Thịnh Capital — do nhóm nhà đầu tư VIP triệu tập để truy vấn ban lãnh đạo.

Hưng vẫn cố giữ vẻ bình tĩnh, nhưng mồ hôi lấm tấm trên trán khi Minh bước vào phòng họp — đúng căn phòng tầng ba mươi sáu Bitexco nơi anh bị đuổi.

Minh không nói nhiều. Anh mở laptop, kết nối projector, và chiếu lên màn hình: sơ đồ dòng tiền on-chain, bằng chứng blockchain, và — điều khiến Hưng tái mặt — bản ghi âm cuộc họp nội bộ giữa Hưng và Diễm bàn kế hoạch chuyển tiền, do chính hệ thống ghi âm phòng họp công ty lưu lại mà họ quên xóa.

"Trong bản ghi này, anh Hưng nói nguyên văn: 'Chuyển bốn mươi bảy tỷ sang ví crypto, gán cho thằng Minh, xong đuổi nó.' Timestamp ngày 15 tháng 7, ba tuần trước khi tôi bị vu oan," Minh nói, giọng bình thản như đang trình bày báo cáo quý.

Phòng họp im lặng. Hai mươi nhà đầu tư quay sang nhìn Hưng với ánh mắt giết người.

Hưng lắp bắp: "Đó là... bản ghi giả..."

"Forensic audio analysis bởi Viện Khoa học Hình sự Bộ Công an xác nhận bản ghi không bị chỉnh sửa. Giọng nói khớp 99.7% với mẫu giọng của anh Lý Gia Hưng," Ngân đứng dậy, tay cầm văn bản kết luận giám định.

Hưng đứng bật dậy, lao ra cửa. Nhưng hai sĩ quan công an đã đợi sẵn ở hành lang.

"Anh Lý Gia Hưng, anh bị bắt theo lệnh truy tố về tội lừa đảo chiếm đoạt tài sản, rửa tiền, và vu khống."

Hưng bị còng tay dẫn đi trước mặt hai mươi nhà đầu tư. Cánh cửa thang máy đóng lại, kết thúc sự nghiệp của kẻ từng đứng trên đỉnh cao tài chính Sài Gòn."""),

("Chương 5: Quỹ Mới — Minh Bạch Tuyệt Đối", """Ba tháng sau vụ bắt Hưng, Minh thành lập quỹ đầu tư mới: Phoenix Capital — đặt tên theo biểu tượng tái sinh. Quỹ hoạt động với triết lý khác biệt hoàn toàn: toàn bộ giao dịch được ghi nhận trên blockchain công khai, nhà đầu tư có thể verify realtime.

Ngân là Chief Legal Officer, thiết kế hệ thống compliance dựa trên smart contract — hợp đồng tự động thực thi trên blockchain, không ai có thể chỉnh sửa hay giả mạo.

Hai mươi nhà đầu tư cũ từ Hưng Thịnh chuyển toàn bộ vốn sang Phoenix Capital. Họ tin Minh hơn bao giờ hết — không chỉ vì tài năng, mà vì sự minh bạch.

Quỹ quản lý năm trăm tỷ đồng trong năm đầu tiên, lợi nhuận hai mươi tám phần trăm — cao nhất thị trường."""),

("Chương 6: Mở Rộng Đế Chế Tài Chính", """Phoenix Capital mở rộng sang quản lý tài sản số: crypto fund, DeFi yield farming, và NFT art fund. Tổng tài sản quản lý đạt hai nghìn tỷ đồng sau hai năm.

Minh được Forbes Vietnam vinh danh "Financier of the Year." Bloomberg đăng profile: "The Vietnamese Fund Manager Who Used Blockchain to Clear His Name and Build an Empire."

Ngân giờ không chỉ là luật sư, mà là người phụ nữ bên cạnh Minh. Họ kết hôn trong lễ cưới trên du thuyền tại vịnh Hạ Long — khách mời là hai mươi nhà đầu tư trung thành đã đi cùng Minh từ ngày khó khăn nhất."""),

("Chương 7: Bí Mật Thuật Toán Gia Truyền", """Minh ít khi kể, nhưng chiến lược đầu tư thiên tài của anh không đến từ trường học hay sách vở. Nó đến từ ông ngoại — cụ Trần Văn Đức, một thương nhân buôn gạo ở chợ Bến Thành trước 1975.

Cụ Đức không biết chữ, nhưng cụ có khả năng tính nhẩm và đọc xu hướng thị trường phi thường. Cụ ghi chép giá gạo hàng ngày trong cuốn sổ tay, vẽ biểu đồ bằng tay, và phát triển một "công thức" dự đoán giá dựa trên mùa vụ, thời tiết, và tâm lý đám đông.

Minh đã số hóa "công thức cụ Đức" thành thuật toán machine learning, kết hợp với dữ liệu hiện đại. Đó là bí mật đằng sau tỷ lệ lợi nhuận vượt trội của anh.

"Ông ngoại không biết blockchain là gì," Minh kể với Ngân. "Nhưng ông hiểu thị trường bằng trực giác mà không AI nào thay thế được. Tôi chỉ đặt trực giác đó lên nền tảng công nghệ."

Ngân mỉm cười: "Vậy Phoenix Capital thực ra được xây bởi một ông cụ buôn gạo chợ Bến Thành?"

"Đúng vậy. Và ông sẽ rất tự hào." """),

("Chương 8: Hưng Thịnh Sụp Đổ Hoàn Toàn", """Tòa án TP.HCM tuyên án: Lý Gia Hưng mười tám năm tù về tội lừa đảo chiếm đoạt tài sản và rửa tiền. Hoàng Thị Diễm mười hai năm tù. Toàn bộ tài sản bị tịch thu để bồi thường cho nhà đầu tư.

Bốn mươi bảy tỷ đồng được thu hồi gần như toàn bộ từ ví crypto bị đóng băng. Minh đích thân gọi điện cho từng nhà đầu tư để thông báo hoàn tiền.

Ngày tuyên án, Minh không đến tòa. Anh ở văn phòng Phoenix Capital, đọc báo cáo quý mới. Quá khứ đã khép lại, anh không cần nhìn nó thêm lần nào."""),

("Chương 9: Giải Thưởng Tài Chính Châu Á", """Phoenix Capital nhận giải "Best Transparent Fund in Asia" tại Asian Financial Awards, Singapore. Mô hình quỹ blockchain-based của Minh được Harvard Business School viết thành case study.

Minh đứng trên sân khấu Marina Bay Sands, nhận cúp trước năm trăm chuyên gia tài chính châu Á.

"Tôi bị vu oan biển thủ bốn mươi bảy tỷ đồng. Blockchain đã cứu tôi. Từ đó, tôi xây quỹ đầu tư trên blockchain để không ai phải chịu oan như tôi nữa. Minh bạch không phải là lựa chọn — đó là nghĩa vụ."

Bên dưới sân khấu, Ngân vỗ tay, mắt rưng rưng. Bên cạnh cô, bà ngoại Minh — cụ bà tám mươi tuổi, vợ cụ Đức buôn gạo chợ Bến Thành — đang cầm điện thoại quay video, miệng nói nhỏ: "Thằng cháu tôi giỏi quá!" """),

("Chương 10: Mua Lại Hưng Thịnh Và Bài Học Cuối", """Phoenix Capital mua lại thương hiệu và giấy phép của Hưng Thịnh Capital tại phiên đấu giá tài sản phá sản. Giá: mười tỷ đồng — bằng năm phần trăm giá trị đỉnh cao khi Minh còn quản lý.

Minh đổi tên Hưng Thịnh thành Phoenix Legacy — quỹ dành riêng cho giáo dục tài chính cộng đồng, dạy người dân bình thường cách đầu tư an toàn trên blockchain, miễn phí.

Ngày khai trương Phoenix Legacy, Minh đứng trong chính căn phòng tầng ba mươi sáu Bitexco — nơi anh từng bị còng tay đuổi ra.

Anh nhìn ra cửa sổ, thành phố Sài Gòn trải rộng dưới chân. Hai năm trước, anh đứng ở vị trí này với tư cách nghi phạm. Hôm nay, anh đứng đây với tư cách chủ nhân.

Ngân đứng bên cạnh, nắm tay anh. "Anh có nhớ lần đầu gặp nhau ở quán cà phê quận 3 không?"

"Nhớ. Cô nói: 'blockchain không nói dối.' Câu đó thay đổi cuộc đời tôi."

"Không. Anh thay đổi cuộc đời anh. Blockchain chỉ là công cụ. Lương tâm mới là thuật toán quan trọng nhất."

Minh cười, ôm vợ. Phía dưới tầng ba mươi sáu, Sài Gòn vẫn náo nhiệt, vẫn tràn đầy cơ hội và cạm bẫy. Nhưng ở đâu có người tài năng giữ được lương tâm, ở đó công lý luôn thắng — dù đôi khi nó đến muộn hơn mong đợi.

Từ Portfolio Manager bị còng tay trước mặt nhà đầu tư đến chủ đế chế tài chính blockchain minh bạch nhất châu Á — câu chuyện của Trần Bảo Minh là minh chứng rằng: sự thật không bao giờ bị xóa, chỉ cần đúng công cụ để tìm ra nó."""),
]

# ═══════════════════════════════════════════════════════════════════════════════
# ASSEMBLY & PUBLISHING
# ═══════════════════════════════════════════════════════════════════════════════

ALL_STORIES = [
    {"title": S1_TITLE, "author": S1_AUTHOR, "cover": S1_COVER, "intro": S1_INTRO, "chapters": S1_CHAPTERS},
    {"title": S2_TITLE, "author": S2_AUTHOR, "cover": S2_COVER, "intro": S2_INTRO, "chapters": S2_CHAPTERS},
    {"title": S3_TITLE, "author": S3_AUTHOR, "cover": S3_COVER, "intro": S3_INTRO, "chapters": S3_CHAPTERS},
    {"title": S4_TITLE, "author": S4_AUTHOR, "cover": S4_COVER, "intro": S4_INTRO, "chapters": S4_CHAPTERS},
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
    log("🚀 BATCH 1 LIVE PUBLISH — 4 STORIES")
    # Upload helper
    ftp = get_ftp()
    with open(os.path.join(BASE_DIR, "publish_novel.php"), "rb") as f:
        ftp.storbinary("STOR publish_novel.php", f)
    ftp.quit()
    log("✓ Helper uploaded")

    results = []
    for i, n in enumerate(novels):
        log(f"\n{'='*60}\n📖 PUBLISHING {i+1}/4: {n['title'][:50]}...\n{'='*60}")
        # Generate cover
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
                # Update registry
                reg_path = os.path.join(BASE_DIR, "existing_novels.json")
                reg = json.load(open(reg_path,"r",encoding="utf-8")) if os.path.exists(reg_path) else []
                reg.append({"id": res["story_id"], "title": n["title"], "slug": n["title"].lower().replace(" ","-"), "intro": n["intro"]})
                json.dump(reg, open(reg_path,"w",encoding="utf-8"), ensure_ascii=False, indent=2)
            else:
                log(f"❌ API Error: {res}")
        except Exception as e:
            log(f"❌ Exception: {e}")
        time.sleep(5)

    # Cleanup
    try:
        ftp = get_ftp(); ftp.delete("publish_novel.php"); ftp.quit()
        log("✓ Helper cleaned up")
    except: pass

    log(f"\n🏁 BATCH 1 COMPLETE: {len(results)}/4 published")
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
