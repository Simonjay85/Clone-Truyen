#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
write_dau_bep_story.py — Direct Novel Writer: ĐẦU BẾP BỊ ĐUỔI, QUÁN VỈA HÈ THÀNH ĐẾ CHẾ ẨM THỰC
====================================================================================================
Truyện sảng văn/vả mặt 10 chương.
Chủ đề: Ẩm thực Việt Nam — Head Chef bị phản bội, xây dế chế từ quán vỉa hè.
Format: V13 Gold Standard (mỗi câu 1 <p>)
Pipeline: Generate cover → FTP upload → publish_novel.php
"""

import json
import os
import re
import sys
import time
import random
import subprocess
import ftplib
import requests

# ─── CONFIGURATION ────────────────────────────────────────────────────────────
FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"
WP_URL = "https://doctieuthuyet.com"
SECRET_TOKEN = "ZEN_TRUYEN_2026_BYPASS"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ─── V13 SENTENCE SPLITTER ────────────────────────────────────────────────────
def split_into_sentences(text):
    t = re.sub(r'\s+', ' ', text).strip()
    abbrevs = ["TS.", "BS.", "CEO.", "CFO.", "Dr.", "Mr.", "Mrs.", "Ms.", "HACCP.", "ISO.", "GMP.", "Michelin.", "TripAdvisor.", "F&B."]
    for i, abb in enumerate(abbrevs):
        t = t.replace(abb, f"__ABB{i}__")
    t = re.sub(r'([.!?]["\"\']?)\s+(?=[A-ZÀÁẠẢÃÂẦẤẬẨẪĂẰẮẶẲẴÈÉẸẺẼÊỀẾỆỂỄĐÌÍỊỈĨÒÓỌỎÕÔỒỐỘỔỖƠỜỚỢỞỠÙÚỤỦŨƯỪỨỰỬỮỲÝỴỶỸ"\"\'\d\-\w])', r'\1[SENTENCE_END]', t)
    for i, abb in enumerate(abbrevs):
        t = t.replace(f"__ABB{i}__", abb)
    sentences = t.split("[SENTENCE_END]")
    return [s.strip() for s in sentences if s.strip()]

def format_v13(raw_text):
    """Format raw text into V13 Gold Standard HTML (each sentence in <p>)."""
    clean = re.sub(r'<[^>]+>', ' ', raw_text)
    sentences = split_into_sentences(clean)
    return "\n".join(f"<p>{s}</p>" for s in sentences) + "\n"

def log(msg):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {msg}")
    sys.stdout.flush()

# ═══════════════════════════════════════════════════════════════════════════════
# NỘI DUNG TRUYỆN
# ═══════════════════════════════════════════════════════════════════════════════

NOVEL_TITLE = "ĐẦU BẾP BỊ ĐUỔI, TAY KHÔNG DỰNG ĐẾ CHẾ ẨM THỰC"
NOVEL_AUTHOR = "Hoàng Việt Anh"
NOVEL_GENRE = "Sảng Văn"
COVER_BASE = "base_cover_34.png"

NOVEL_INTRO = """<p><strong>"Anh dành sáu năm tuổi trẻ, sáng tạo ra 47 món signature đưa nhà hàng từ vô danh lên ngôi vương ẩm thực Sài Gòn. Đổi lại, họ vu oan anh ăn cắp nguyên liệu, đuổi anh ra khỏi bếp giữa đêm mưa như trút nước."</strong></p>
<p>Trần Minh Đức, Head Chef thiên tài của nhà hàng năm sao Kim Ngân Palace, bị chính người đồng nghiệp thân tín Lý Thiên Phúc phản bội và ông chủ tập đoàn F&B Hoàng Gia Khánh âm mưu cướp đoạt toàn bộ công thức gia truyền ba đời.</p>
<p>Bị vứt ra đường với hai bàn tay trắng, Minh Đức mở quán phở vỉa hè nhỏ bé ở con hẻm quận 4. Tình cờ gặp Nguyễn Bảo Ngọc, nữ nhà phê bình ẩm thực quốc tế sắc sảo từng tu nghiệp tại Le Cordon Bleu Paris, hai người bắt đầu hành trình vả mặt tất cả những kẻ từng khinh thường anh.</p>
<p>Từ quán vỉa hè bị chê là "rác rưởi", Minh Đức từng bước xây dựng đế chế ẩm thực khiến cả Sài Gòn rung chuyển, biến những kẻ phản bội thành trò cười của ngành F&B và đưa ẩm thực đường phố Việt Nam lên bản đồ Michelin thế giới.</p>"""

# ─── CHƯƠNG 1 ──────────────────────────────────────────────────────────────────
ch1_title = "Chương 1: Bị Đuổi Giữa Đêm Mưa"
ch1 = """Đồng hồ trên tường bếp nhà hàng Kim Ngân Palace chỉ mười một giờ bốn mươi lăm phút đêm. Trần Minh Đức đang cẩn thận rưới lớp sốt demi-glace lên đĩa thăn bò wagyu A5 cuối cùng trong ca tối, đôi tay anh vững chãi như phẫu thuật gia đang thực hiện ca mổ đòi hỏi độ chính xác tuyệt đối.

"Order lên! Bàn VIP 7, wagyu demi-glace kèm foam nấm truffle và gel rượu vang đỏ Bordeaux 2018!" Minh Đức hô dõng dạc, giọng anh vang khắp căn bếp rộng hai trăm mét vuông với hệ thống hút khói công nghiệp trị giá ba tỷ đồng.

Mười hai đầu bếp phụ đồng loạt đáp "Oui, Chef!" như một dàn nhạc được chỉ huy bởi nhạc trưởng bậc thầy. Đó là nề nếp mà Minh Đức đã xây dựng suốt sáu năm ròng, kể từ khi anh bước chân vào căn bếp này với vị trí commis ở tuổi hai mươi hai.

Sáu năm. Hai nghìn một trăm chín mươi ngày. Bốn mươi bảy công thức signature do chính tay anh sáng tạo. Kim Ngân Palace từ một nhà hàng buffet tầm trung không ai biết đến đã vươn lên vị trí số một trên TripAdvisor khu vực Đông Nam Á, với danh hiệu "Best Fine Dining Ho Chi Minh City" ba năm liên tiếp.

Tất cả nhờ đôi bàn tay và khối óc của Trần Minh Đức.

Nhưng đêm nay, khi Minh Đức vừa cởi tạp dề trắng đã lấm tấm vết sốt, chuẩn bị kết thúc ca làm việc mười bốn tiếng liên tục, cánh cửa inox của phòng bếp bất ngờ bật mở đánh rầm.

Hoàng Gia Khánh, Chủ tịch tập đoàn Hoàng Kim F&B Group, chủ sở hữu chuỗi mười hai nhà hàng cao cấp trải dài từ Sài Gòn đến Đà Nẵng, bước vào với bộ vest Armani đen bóng. Theo sau hắn là bốn bảo vệ to cao và một người mà Minh Đức không bao giờ ngờ tới — Lý Thiên Phúc, sous chef, người anh coi như em ruột suốt năm năm qua.

"Trần Minh Đức!" Khánh gầm lên, ném một xấp giấy A4 thẳng vào mặt Minh Đức. "Giải thích đi! Mày ăn cắp nguyên liệu nhà hàng để bán ra ngoài, tổng thiệt hại ước tính bốn trăm năm mươi triệu đồng trong hai năm qua!"

Minh Đức sững người, nhặt tờ giấy lên. Đó là một bản kê khai chi tiết ghi rõ ngày giờ, số lượng thịt bò wagyu, nấm truffle Périgord, saffron Iran, cùng hàng chục loại nguyên liệu nhập khẩu đắt tiền khác bị "mất tích" khỏi kho lạnh.

"Cái gì? Tôi chưa bao giờ lấy một gram nguyên liệu nào ra khỏi nhà hàng!" Minh Đức trợn mắt, anh quay sang nhìn Thiên Phúc. "Phúc! Em quản lý kho lạnh, em biết rõ tôi không bao giờ làm chuyện này! Nói đi!"

Lý Thiên Phúc khoanh tay trước ngực, ánh mắt lạnh tanh như cá chết. Hắn chỉnh lại chiếc tạp dề xanh navy — tạp dề của sous chef mà chính Minh Đức đã trao cho hắn ba năm trước.

"Anh Đức à, em rất tiếc. Nhưng camera kho lạnh đã ghi lại hết," Thiên Phúc nói, giọng đều đều như đang đọc kịch bản đã soạn sẵn. "Anh thường xuyên vào kho lạnh lúc khuya, mang theo ba lô cá nhân lớn. Em không muốn tố cáo anh đâu, nhưng anh Khánh ép em phải nói sự thật."

Minh Đức cảm thấy máu dồn lên đỉnh đầu. Camera kho lạnh? Anh vào kho lạnh lúc khuya là để kiểm tra nhiệt độ bảo quản và chuẩn bị nguyên liệu cho ngày hôm sau, điều mà bất kỳ Head Chef có trách nhiệm nào cũng phải làm!

"Mày dàn dựng! Thiên Phúc, chính mày quản lý chìa khóa kho, chính mày có quyền chỉnh sửa log xuất nhập!" Minh Đức chỉ thẳng mặt Thiên Phúc, tay anh run lên vì phẫn nộ.

Khánh bước tới, đẩy Minh Đức ra xa bằng một cú đẩy mạnh vào ngực. "Im! Tao đã báo công an quận 1. Mày có hai lựa chọn: một, ký đơn tự nguyện nghỉ việc và giao lại toàn bộ công thức signature cho nhà hàng. Hai, ra tòa với bằng chứng camera và chứng từ kho."

"Giao công thức?" Minh Đức cười gằn, nụ cười mang theo cơn đau xé lòng. "Bốn mươi bảy công thức đó là tâm huyết sáu năm của tôi, là di sản gia truyền ba đời nhà họ Trần mà ông nội tôi truyền lại! Các người muốn cướp trắng?"

Khánh nhếch miệng cười khinh bỉ. "Cướp? Hợp đồng lao động điều khoản 14 mục 3 ghi rõ: 'Mọi sản phẩm trí tuệ được tạo ra trong thời gian làm việc thuộc sở hữu của công ty.' Mày tự ký tên vào đó sáu năm trước, quên rồi à?"

Minh Đức lảo đảo lùi lại như bị đấm thẳng vào bụng. Điều khoản 14 mục 3. Đúng vậy, anh đã ký khi còn là một chàng trai hai mươi hai tuổi ngây thơ, háo hức được vào bếp nhà hàng lớn mà không hề đọc kỹ hợp đồng.

"Anh Khánh, anh không thể..." Minh Đức cố gắng giữ bình tĩnh.

"Bảo vệ! Đưa người này ra khỏi bếp của tôi. Từ giờ phút này, Trần Minh Đức không còn là nhân viên của Kim Ngân Palace!" Khánh phẩy tay ra lệnh.

Bốn gã bảo vệ xông vào, tước tạp dề trắng khỏi người Minh Đức. Chiếc tạp dề thêu tên "Chef Đức" bằng chỉ vàng — thứ mà anh trân quý như mạng sống — bị vò nát ném xuống sàn bếp ướt nhẫy.

Mười hai đầu bếp phụ đứng im như tượng đá, không ai dám lên tiếng. Trong mắt họ đều ngập tràn sự bất lực và nỗi sợ mất việc.

Minh Đức bị lôi qua cửa sau, đẩy ra con hẻm tối mù phía sau nhà hàng. Trời Sài Gòn đang đổ mưa như trút nước, những hạt mưa tháng sáu nặng trĩu quất thẳng vào mặt anh.

"Đợi đã!" Thiên Phúc chạy ra, ném một túi ni-lông xuống vũng nước bẩn trước mặt Minh Đức. "Đồ cá nhân của anh. Con dao chef Masamoto mà anh hay khoe là ông nội để lại, tôi cũng cho vào đó rồi."

Minh Đức cúi xuống nhặt túi ni-lông lên, lôi con dao ra kiểm tra. Con dao chef Masamoto KS bằng thép carbon xanh dài 270mm, cán gỗ mun đen bóng — gia bảo ba đời nhà họ Trần, thứ mà ông nội anh đã dùng để nấu phở cho cả trung đoàn trong thời kháng chiến.

Lưỡi dao vẫn sáng loáng dưới ánh đèn đường hắt vào, nhưng trên thân dao có một vết xước dài — vết xước mới, cố ý.

"Mày xước dao của tôi," Minh Đức nói, giọng lạnh đến rợn người.

Thiên Phúc nhún vai, cười nhạt. "Ồ, xin lỗi. Tay trượt. À mà anh Đức, anh nên quên mấy công thức đi nhé. Từ mai, tôi sẽ là Head Chef mới của Kim Ngân Palace. Anh Khánh đã hứa cho tôi mười lăm phần trăm cổ phần và một căn penthouse ở Thảo Điền."

"Mày phản bội tao vì tiền?" Minh Đức nghiến răng.

"Không phải phản bội, anh Đức. Đó gọi là 'nắm bắt cơ hội,'" Thiên Phúc búng tay. "Anh giỏi nấu ăn thật, nhưng anh quá ngu trong chuyện làm người. Sáu năm cống hiến mà không giữ được một cái hợp đồng tử tế, anh xứng đáng bị đuổi."

Cánh cửa sắt đóng sầm lại trước mặt Minh Đức. Tiếng cười khinh khỉnh của Thiên Phúc vọng lại qua kẽ hở.

Minh Đức đứng giữa cơn mưa tầm tã, nước mưa hòa với mồ hôi và có lẽ cả nước mắt chảy ròng trên gương mặt sạm đen vì khói bếp sáu năm. Anh siết chặt con dao Masamoto trong tay, lưỡi thép carbon xanh phản chiếu ánh chớp xé toạc bầu trời đêm Sài Gòn.

"Hoàng Gia Khánh, Lý Thiên Phúc," anh thì thầm, giọng rít qua kẽ răng. "Các người cướp nhà hàng của tôi, cướp danh dự của tôi, xước con dao gia truyền của tôi. Tôi thề, tôi sẽ xây một đế chế ẩm thực khiến Kim Ngân Palace của các người trở thành cái bóng nhạt nhòa. Tôi sẽ khiến các người phải quỳ xuống cầu xin tôi quay lại!"

Sấm nổ rền vang trên bầu trời quận 1, như thể trời đất cũng đang chứng giám lời thề sắt máu của người đầu bếp bị đuổi."""

# ─── CHƯƠNG 2 ──────────────────────────────────────────────────────────────────
ch2_title = "Chương 2: Quán Phở Vỉa Hè Và Cô Gái Lạ"
ch2 = """Ba ngày sau đêm bị đuổi, Trần Minh Đức tìm được một mặt bằng nhỏ xíu rộng vẻn vẹn mười hai mét vuông trong con hẻm 47 đường Tôn Đản, quận 4. Tiền thuê ba triệu rưỡi một tháng, rẻ nhất khu vực vì nằm sâu trong hẻm, cách mặt đường lớn gần trăm mét.

Toàn bộ gia sản của Minh Đức lúc này gồm: con dao Masamoto gia truyền, hai mươi ba triệu đồng tiền tiết kiệm, một chiếc nồi inox mười lít mua thanh lý, và cuốn sổ tay công thức viết bằng bút mực của ông nội — thứ duy nhất không bị Khánh cướp được vì anh luôn giữ trong ba lô cá nhân.

"Phở Đức — Gia Truyền Ba Đời." Minh Đức tự tay kẻ tấm bảng hiệu bằng sơn đỏ trên miếng ván ép cũ, chữ viết tay nắn nót nhưng vẫn lấm lem.

Anh quyết định bắt đầu lại từ con số không với món phở — linh hồn của ẩm thực Việt Nam, cũng là món mà ông nội Trần Văn Hào đã nấu nổi tiếng khắp vùng Hà Nội xưa trước khi di cư vào Nam năm 1954.

Ngày đầu tiên mở quán, Minh Đức thức dậy từ ba giờ sáng. Anh ninh xương ống bò trong mười hai tiếng, dùng kỹ thuật blanching ba lần để nước dùng trong vắt như hổ phách. Hồi, quế, thảo quả, đinh hương — anh rang trên lửa than hồng đúng bảy phút, không hơn không kém, để tinh dầu tỏa ra mà không bị cháy khét.

Bánh phở anh tự tráng bằng tay trên nồi hấp, sợi mỏng như lụa, dai nhưng mềm, tan trên đầu lưỡi mà vẫn giữ được kết cấu khi ngâm trong nước dùng nóng.

Tất cả đều theo công thức ông nội, nhưng Minh Đức thêm vào những biến tấu tinh tế mà chỉ một Head Chef đã trải qua sáu năm fine dining mới nghĩ ra: một chút nước mắm cốt Phú Quốc 40 độ đạm ủ ba năm thay vì nước mắm công nghiệp, vài giọt dầu truffle trắng Alba nhẹ nhàng tạo hương thơm quý phái ẩn sau vị bò truyền thống.

Nhưng đến mười một giờ trưa, chỉ có đúng ba khách ghé ăn. Hai người là công nhân bốc vác ở cảng Khánh Hội, một người là bà bán vé số dạo. Cả ba đều khen ngon, nhưng ba tô phở chỉ thu về chín mươi nghìn đồng.

Minh Đức ngồi bệt xuống vỉa hè, nhìn nồi nước dùng còn đầy ắp mà thở dài. Nguyên liệu ninh nước dùng hôm nay tốn gần hai triệu đồng.

"Ông ơi, con xin lỗi, hình như con nấu phở ngon quá mà không ai biết," anh thì thầm nhìn lên trời, nơi ông nội đang ở đâu đó mỉm cười.

Ngày thứ hai, năm khách. Ngày thứ ba, bảy khách. Doanh thu không đủ trả tiền nguyên liệu. Nhưng Minh Đức không hạ chất lượng. Anh vẫn ninh xương mười hai tiếng, vẫn dùng thịt bò tươi từ lò mổ Vissan loại nhất, vẫn tráng phở bằng tay.

Ngày thứ bảy, khi Minh Đức đang lau bàn lúc hai giờ chiều, một người phụ nữ trẻ bước vào quán. Cô mặc áo sơ mi trắng giản dị, tóc buộc đuôi ngựa gọn gàng, kính cận gọng mảnh che đi đôi mắt sáng thông minh. Trên tay cô là một cuốn sổ da bìa cứng màu nâu đỏ và cây bút Montblanc.

"Cho tôi một tô phở tái nạm gầu, nước dùng riêng một chén, rau ăn kèm để đĩa riêng. Không giá sống," cô nói, giọng rõ ràng, dứt khoát.

Minh Đức khẽ nhíu mày. Cách gọi món của cô cho thấy đây không phải khách ăn bình thường. Tách nước dùng riêng để đánh giá độ trong, hương vị và nhiệt độ — đó là cách các nhà phê bình ẩm thực chuyên nghiệp thử món.

Anh bưng tô phở ra, bày trí cẩn thận như thể đang phục vụ trong nhà hàng năm sao: thịt bò tái xếp hình cánh hoa hồng, hành lá thái chỉ rắc đều, vài lát ớt đỏ tươi tạo điểm nhấn màu sắc.

Người phụ nữ nhìn tô phở, đôi mắt sau cặp kính khẽ sáng lên.

Cô nhấc chén nước dùng lên, nghiêng nhẹ để quan sát độ trong. Nước dùng vàng óng như hổ phách, không một vẩn đục. Cô đưa lên mũi, hít sâu. Hồi, quế, thảo quả — ba tầng hương tách bạch rõ ràng, không lẫn vào nhau mà hòa quyện tinh tế.

Cô nhấp một ngụm nhỏ, nhắm mắt lại.

Rồi cô mở mắt, nhìn Minh Đức với ánh mắt sửng sốt. "Anh dùng kỹ thuật consommé của Pháp để lọc nước dùng phở Việt?"

Minh Đức giật mình. "Cô nhận ra?"

"Tôi học ba năm tại Le Cordon Bleu Paris, tôi nhận ra mùi raft đậu trắng lẫn trong nước dùng. Anh dùng lòng trắng trứng và thịt bò xay làm bè lọc, đúng không? Nhưng anh biến tấu — thay vì mirepoix truyền thống, anh dùng hành tím Ninh Thuận nướng than và gừng già Hưng Yên." Cô nói một mạch, mắt long lanh.

"Cô là ai?" Minh Đức hỏi, lần đầu tiên sau bảy ngày anh thấy có người thực sự hiểu những gì anh đang làm.

Cô đặt tấm danh thiếp lên bàn: "Nguyễn Bảo Ngọc — Food & Beverage Consultant, cựu Phó Tổng biên tập tạp chí Ẩm Thực Sài Gòn."

"Anh là Trần Minh Đức, cựu Head Chef Kim Ngân Palace, đúng không?" Bảo Ngọc nói thẳng, giọng không vòng vo. "Tôi đã theo dõi sự nghiệp của anh ba năm nay. Tô phở này có giá ba mươi nghìn đồng, nhưng chất lượng không dưới năm trăm nghìn. Anh đang lãng phí tài năng ở đây."

"Tôi không lãng phí. Tôi đang bắt đầu lại," Minh Đức đáp, giọng điềm tĩnh nhưng cứng như thép.

Bảo Ngọc gấp cuốn sổ lại, nhìn thẳng vào mắt anh. "Bắt đầu lại theo cách phá sản trong hai tháng? Nước dùng kiểu này chi phí ít nhất một triệu rưỡi mỗi ngày, bán ba mươi nghìn một tô, anh cần bán tối thiểu năm mươi tô mỗi ngày mới hòa vốn. Hôm nay anh bán được bao nhiêu?"

Minh Đức im lặng. Hôm nay mới có sáu tô.

Bảo Ngọc đứng dậy, rút ví trả tiền. "Tô phở này ngon nhất mà tôi từng ăn trong đời, kể cả tô phở tại nhà hàng Việt một sao Michelin ở Paris. Nhưng ngon thôi chưa đủ, anh cần chiến lược."

Cô để lại tấm danh thiếp và một câu nói khiến Minh Đức trằn trọc suốt đêm: "Gọi cho tôi khi anh sẵn sàng nghiêm túc. Tài năng không có chiến lược thì chỉ là nước dùng đổ xuống cống."

Cánh cửa quán phở cũ kỹ khép lại sau lưng Bảo Ngọc, nhưng trong đầu Minh Đức, một cánh cửa mới vừa hé mở."""

# ─── CHƯƠNG 3 ──────────────────────────────────────────────────────────────────
ch3_title = "Chương 3: Bát Phở Thần Thánh Gây Bão Mạng"
ch3 = """Hai tuần sau cuộc gặp với Bảo Ngọc, Minh Đức quyết định gọi cho cô. Không phải vì anh yếu đuối, mà vì anh đủ thông minh để biết: một mình nấu giỏi thì chỉ là đầu bếp, biết kết hợp thì mới thành doanh nhân.

Bảo Ngọc đến quán vào buổi sáng sớm, khi Minh Đức đang ninh nồi xương cho ngày mới. Cô ngồi xuống chiếc ghế nhựa thấp lè tè, mở laptop Macbook Pro ra đặt lên cái bàn inox cũ, bắt đầu phân tích.

"Anh Đức, vấn đề không phải chất lượng. Vấn đề là positioning," Bảo Ngọc gõ bàn phím lách cách. "Anh bán phở ba mươi nghìn trong hẻm quận 4, khách hàng mục tiêu là công nhân và người lao động. Nhưng chi phí nguyên liệu của anh là chi phí fine dining. Mô hình này tự sát tài chính."

"Vậy cô muốn tôi tăng giá?"

"Không. Tôi muốn anh giữ nguyên giá nhưng thay đổi cách khách hàng nhìn nhận. Anh có biết khái niệm 'hidden gem' trong ngành F&B không? Những quán ăn bình dân nhưng chất lượng cao bất thường luôn tạo hiệu ứng viral khủng khiếp trên mạng xã hội."

Bảo Ngọc đề xuất kế hoạch: cô sẽ mời ba food blogger có ảnh hưởng nhất Sài Gòn đến ăn thử, quay video đánh giá trung thực. Không tốn đồng nào quảng cáo.

Ba ngày sau, Hùng Vlog — food blogger ba triệu subscriber trên YouTube — ngồi trong quán phở vỉa hè của Minh Đức, máy quay 4K đặt trên tripod chĩa thẳng vào tô phở.

"Ê mọi người, hôm nay Hùng dẫn mọi người đến một quán phở vỉa hè bí ẩn ở quận 4, nghe đồn là cựu Head Chef nhà hàng năm sao mở. Giá ba mươi nghìn một tô. Hùng sẽ đánh giá khách quan nhé!" Hùng nói vào camera, vẻ mặt hoài nghi rõ ràng.

Minh Đức bưng tô phở ra, vẫn bày trí tinh tế như mọi khi.

Hùng nhấc đũa, gắp sợi phở lên. Sợi phở tươi tráng tay trắng muốt, mềm mại rủ xuống như dải lụa. Hùng cho vào miệng, nhai chậm rãi.

Camera zoom vào khuôn mặt Hùng. Đôi mắt anh ta bỗng mở to, hàm ngừng nhai một giây như bị đóng băng. Rồi Hùng nuốt xuống, lặng im năm giây — điều chưa từng xảy ra trong bốn năm làm food review.

"Trời ơi." Hùng buông đũa, nhìn thẳng vào camera. "Mọi người ơi, Hùng làm food review bốn năm, ăn qua hơn hai nghìn quán ở Sài Gòn, kể cả mấy nhà hàng Michelin ở Bangkok và Singapore. Nhưng tô phở này... tô phở ba mươi nghìn vỉa hè quận 4 này... Hùng chưa ăn tô phở nào ngon hơn trong đời."

Video được đăng lên YouTube tối hôm đó. Trong bốn mươi tám giờ, nó đạt hai triệu lượt xem, mười hai nghìn bình luận, và trở thành video trending số một Việt Nam.

Sáng hôm sau, hàng người xếp hàng trước quán phở của Minh Đức kéo dài ra tận đầu hẻm, gần năm mươi mét. Người ta đến từ khắp Sài Gòn: dân công sở Phú Mỹ Hưng lái Mercedes đến ăn phở vỉa hè, sinh viên đại học rủ nhau đi thử, thậm chí có cả đoàn khách du lịch Hàn Quốc cầm điện thoại dịch Google Maps.

Minh Đức nấu từ năm giờ sáng đến hai giờ chiều, bán sạch một trăm năm mươi tô. Doanh thu bốn triệu rưỡi trong một ngày — gấp mười lăm lần ngày đầu tiên.

Tin tức lan nhanh đến tai Hoàng Gia Khánh.

Sáng hôm đó, Khánh đang ngồi trong phòng làm việc tầng hai mươi ba của tòa nhà Hoàng Kim Tower, uống cà phê Kopi Luwak giá triệu rưỡi một ly, lướt điện thoại. Khi thấy video của Hùng Vlog hiện lên trên bảng tin Facebook với dòng tiêu đề "CỰU HEAD CHEF NHÀ HÀNG 5 SAO BÁN PHỞ VỈA HÈ 30K, NGON HƠN MỌI NHÀ HÀNG SANG", ly cà phê trong tay hắn suýt rơi.

"Cái gì?!" Khánh gầm lên, nhấn vào video. Hai triệu lượt xem. Comment tràn ngập lời khen Minh Đức và chê bai Kim Ngân Palace.

"Ông chủ Kim Ngân đuổi đầu bếp giỏi nhất Sài Gòn, đúng là tự hủy!"

"Cắn rơm cắn cỏ cũng phải đi ăn phở anh Đức!"

"Kim Ngân Palace giờ mất anh Đức thì còn gì? Mấy lần gần đây đến ăn dở tệ!"

Khánh ném điện thoại xuống bàn, mặt tái xanh. Hắn bấm intercom gọi Thiên Phúc lên ngay lập tức.

Thiên Phúc bước vào, mặt cũng cắt không còn giọt máu. Hắn đã xem video từ đêm qua.

"Anh Khánh, em sẽ xử lý. Thằng Đức chỉ là quán vỉa hè, em sẽ cho nó biết thế nào là luật chơi của ngành F&B Sài Gòn," Thiên Phúc nói, mắt hắn lóe lên tia sáng nham hiểm.

"Mày phải diệt nó ngay! Không được để nó lớn lên!" Khánh đập bàn. "Gọi cho thằng Tuấn bên phòng quản lý thị trường quận 4, bảo nó kiểm tra vệ sinh an toàn thực phẩm quán đó. Phải đóng cửa nó bằng mọi giá!"

Thiên Phúc gật đầu, nụ cười độc ác nở trên môi. "Em hiểu. Quán vỉa hè mà, thiếu gì lỗi. Giấy phép kinh doanh, chứng nhận HACCP, nguồn gốc xuất xứ nguyên liệu... Em sẽ khiến thằng Đức không bao giờ ngóc đầu lên được nữa."

Nhưng cả Khánh lẫn Thiên Phúc đều không biết rằng, ở quán phở nhỏ bé kia, Bảo Ngọc đã ngồi cạnh Minh Đức, mỉm cười bí ẩn. Trên màn hình laptop của cô, một kế hoạch kinh doanh bài bản đã được chuẩn bị sẵn — bao gồm cả phương án phòng thủ cho đúng tình huống mà Khánh đang âm mưu."""

# ─── CHƯƠNG 4 ──────────────────────────────────────────────────────────────────
ch4_title = "Chương 4: Vả Mặt Đội Kiểm Tra"
ch4 = """Đúng như dự đoán của Bảo Ngọc, bốn ngày sau khi video viral, một đoàn kiểm tra vệ sinh an toàn thực phẩm quận 4 bất ngờ ập đến quán phở Đức vào lúc mười giờ sáng — giờ cao điểm nhất.

Đoàn gồm năm người, dẫn đầu là Nguyễn Hữu Tuấn, Phó phòng Quản lý thị trường quận 4, người mà Thiên Phúc đã "bôi trơn" bằng một phong bì năm mươi triệu đồng.

"Trần Minh Đức! Đoàn kiểm tra liên ngành về vệ sinh an toàn thực phẩm!" Tuấn hống hách vung tờ quyết định, bước vào quán giữa lúc ba mươi khách đang ngồi ăn. "Yêu cầu ngừng kinh doanh ngay lập tức để kiểm tra!"

Khách ăn nhốn nháo, nhiều người rút điện thoại quay video. Minh Đức đặt muôi xuống, bình tĩnh lau tay vào khăn sạch. Anh đã được Bảo Ngọc cảnh báo trước.

"Mời anh kiểm tra," Minh Đức nói, giọng điềm nhiên đến lạ lùng. Anh rút từ ngăn kéo ra một tập hồ sơ dày cộp, đặt lên bàn.

Tuấn giật mình. Một quán phở vỉa hè mà có hồ sơ?

Minh Đức mở từng trang, giọng rành rọt như đang thuyết trình trước hội đồng giám khảo Michelin.

"Giấy phép kinh doanh hộ cá thể, đăng ký ngày 15 tháng 5, số 47/GP-Q4." Lật trang. "Giấy chứng nhận đủ điều kiện vệ sinh an toàn thực phẩm, cấp bởi Chi cục An toàn thực phẩm TP.HCM." Lật trang. "Giấy khám sức khỏe định kỳ của chủ cơ sở." Lật trang. "Hóa đơn VAT nguồn gốc xuất xứ nguyên liệu: thịt bò từ Vissan, xương bò từ trang trại Củ Chi có chứng nhận VietGAHP, rau sạch từ HTX Phước An Đà Lạt có chứng nhận GlobalGAP."

Tuấn đứng há hốc mồm. Quán vỉa hè mà hồ sơ pháp lý chặt chẽ hơn cả nhà hàng năm sao?

"Anh Tuấn, anh muốn kiểm tra gì thêm? Nhiệt độ kho lạnh? Mời," Minh Đức mở nắp thùng xốp bảo ôn, bên trong có nhiệt kế điện tử hiển thị 2.1 độ C. "Tôi ghi log nhiệt độ mỗi hai tiếng, đây là sổ log bảy ngày qua."

Tuấn lật sổ log, mặt tái dần. Mọi thứ hoàn hảo đến từng chi tiết. Không tìm được bất kỳ lỗi vi phạm nào.

"Xong chưa? Hay anh muốn test nhanh dư lượng kháng sinh trong thịt bò? Tôi có sẵn kit test nhanh ở đây," Minh Đức rút ra một hộp kit rapid test Romer Labs, loại mà ngay cả nhiều nhà máy thực phẩm lớn cũng không trang bị.

Tuấn nuốt nước bọt, nhìn sang đồng nghiệp. Không ai tìm được gì.

"Tốt, hồ sơ đầy đủ," Tuấn lí nhí, cố giữ thể diện. "Nhưng theo quy định, quán vỉa hè không được phép kinh doanh trên lòng lề đường, anh đang lấn chiếm—"

"Tôi kinh doanh trong nhà, không phải trên vỉa hè," Minh Đức cắt ngang. "Địa chỉ đăng ký kinh doanh là số 47/12 Tôn Đản, đây là mặt bằng trong hẻm có hợp đồng thuê chính chủ. Bàn ghế khách ngồi nằm trong phạm vi mặt bằng thuê, không lấn ra vỉa hè hay lòng đường. Anh có thể đo lại nếu muốn."

Tuấn đỏ mặt tía tai. Hắn rút điện thoại ra nhắn tin cho Thiên Phúc: "Không xử được, thằng này chuẩn bị hồ sơ kín kẽ quá."

Nhưng khoảnh khắc đó, một giọng nữ trong trẻo vang lên từ phía sau.

"Anh Tuấn! Phó phòng Quản lý thị trường quận 4, đúng không?"

Bảo Ngọc bước vào, tay cầm điện thoại đang quay video. Bên cạnh cô là một người đàn ông trung niên mặc vest xám, đeo kính.

"Đây là luật sư Phạm Quốc Trung, Đoàn Luật sư TP.HCM. Và tôi là Nguyễn Bảo Ngọc, nhà tư vấn F&B. Tôi muốn hỏi: quyết định kiểm tra đột xuất của anh có được phê duyệt bởi Chi cục trưởng theo đúng quy trình không? Vì theo Nghị định 115/2018, kiểm tra đột xuất chỉ được thực hiện khi có đơn tố cáo bằng văn bản hoặc chỉ đạo từ cấp trên. Anh có giấy tờ nào không?"

Tuấn lắp bắp. Đây là kiểm tra theo "yêu cầu miệng" của Thiên Phúc, không có văn bản chính thức.

Luật sư Trung bước tới, giọng trầm ấm nhưng sắc lạnh. "Nếu đây là cuộc kiểm tra không đúng quy trình, gây ảnh hưởng đến hoạt động kinh doanh hợp pháp và danh dự của thân chủ tôi, chúng tôi có quyền khiếu nại lên UBND quận và Thanh tra Sở Công Thương. Video này sẽ là bằng chứng."

Tuấn mồ hôi đầm đìa, lùi ra cửa. "Thôi được, kết quả kiểm tra: đạt yêu cầu. Chúng tôi sẽ ra biên bản sau." Hắn kéo đoàn kiểm tra rút lui nhanh như chạy giặc.

Khi đoàn kiểm tra biến mất, ba mươi khách trong quán đồng loạt vỗ tay rào rào. Nhiều người đã quay video toàn bộ cuộc đối đầu và đăng lên TikTok ngay lập tức.

Minh Đức quay sang Bảo Ngọc, ánh mắt anh ấm áp lẫn ngạc nhiên. "Cô chuẩn bị hồ sơ pháp lý cho tôi từ bao giờ?"

Bảo Ngọc đẩy gọng kính lên, mỉm cười. "Từ ngày tôi ăn tô phở đầu tiên ở đây. Tôi biết sớm muộn gì Hoàng Gia Khánh cũng sẽ ra tay. Người ta chỉ đánh kẻ ngã ngựa, nhưng nếu kẻ ngã ngựa có áo giáp, thì người đánh mới là kẻ bị thương."

Video đoàn kiểm tra bị "vả mặt" tại quán phở Đức trở thành hiện tượng mạng xã hội. Trong ba ngày, nó đạt năm triệu lượt xem trên TikTok, với hashtag #PhoĐức và #HeadChefVỉaHè trending số một Việt Nam.

Đêm hôm đó, Khánh gọi điện cho Thiên Phúc, giọng run vì tức giận: "Mày làm ăn kiểu gì? Không những không diệt được nó mà còn biến nó thành anh hùng! Giờ cả Sài Gòn ai cũng biết thằng Đức, còn Kim Ngân Palace thì bị chê bai khắp nơi!"

Thiên Phúc nuốt nước bọt đắng ngắt. Hắn bắt đầu nhận ra rằng, đối thủ không chỉ là một đầu bếp bị đuổi — mà là một đầu bếp bị đuổi có đồng minh rất đáng sợ."""

# ─── CHƯƠNG 5 ──────────────────────────────────────────────────────────────────
ch5_title = "Chương 5: Cuộc Thi Đầu Bếp — Nghiền Nát Kẻ Phản Bội"
ch5 = """Một tháng sau sự kiện kiểm tra thất bại, cơ hội vả mặt thực sự đến với Minh Đức theo cách bất ngờ nhất. Saigon Chef Championship — cuộc thi đầu bếp lớn nhất miền Nam, được tổ chức thường niên bởi Hiệp hội Ẩm thực Việt Nam tại Gem Center quận 1, với giải thưởng năm trăm triệu đồng và danh hiệu "Siêu Đầu Bếp Sài Gòn".

Hoàng Gia Khánh đăng ký cho Lý Thiên Phúc tham gia với tư cách đại diện Kim Ngân Palace, hắn muốn dùng cuộc thi để chứng minh rằng mất Minh Đức, Kim Ngân vẫn mạnh. Thiên Phúc tự tin vì hắn đã thuộc lòng nhiều công thức mà Minh Đức để lại.

Bảo Ngọc là người phát hiện thông tin này. Cô đến quán phở vào buổi tối, đặt tờ đơn đăng ký cuộc thi trước mặt Minh Đức.

"Anh phải tham gia," cô nói dứt khoát. "Không phải vì giải thưởng, mà vì đây là sân khấu hoàn hảo để chứng minh ai mới là đầu bếp thật sự."

Minh Đức nhìn tờ đơn, lặng im hồi lâu. "Tôi chỉ có quán phở vỉa hè, họ sẽ cười tôi."

"Họ cười anh ở vòng đăng ký, nhưng sẽ câm miệng ở vòng chung kết. Đó mới là cách vả mặt đẳng cấp nhất," Bảo Ngọc đáp.

Ngày thi đến. Gem Center quận 1 chật kín năm trăm khán giả, mười hai thí sinh đứng sau mười hai bếp nấu inox sáng loáng. Camera truyền hình trực tiếp trên VTV3.

Khi MC đọc tên Trần Minh Đức — quán Phở Đức, quận 4 — một tiếng xì xào lan khắp hội trường. Thiên Phúc đứng ở bếp số 3, nhếch miệng cười mỉa. Khánh ngồi ở hàng ghế VIP, khoanh tay trước ngực với vẻ mặt đắc thắng.

Đề thi vòng chung kết: "Sáng tạo một món ăn Việt Nam fusion trong chín mươi phút, sử dụng nguyên liệu bắt buộc: cá tra đồng bằng sông Cửu Long."

Cá tra — loại cá bị xem thường nhất trong ẩm thực cao cấp Việt Nam, thường chỉ dùng để xuất khẩu đông lạnh hoặc nấu canh chua bình dân. Biến nó thành fine dining là thách thức khổng lồ.

Thiên Phúc tự tin bắt đầu. Hắn nấu món cá tra áp chảo kiểu Pháp, rưới bơ chanh, kèm purée khoai tây và rau rocket. Kỹ thuật chuẩn mực nhưng... nhàm chán. Đó là công thức tiêu chuẩn mà bất kỳ sinh viên trường dạy nấu ăn nào cũng biết.

Minh Đức đứng trước bếp, nhắm mắt lại ba giây. Trong đầu anh hiện lên hình ảnh ông nội bên bếp lửa than, ninh nồi nước dùng phở trong căn nhà nhỏ ở phố cổ Hà Nội. Ông nói: "Đức ơi, đầu bếp giỏi không phải người biết nhiều công thức, mà là người biến nguyên liệu tầm thường thành phi thường."

Chín mươi phút bắt đầu.

Minh Đức tách phi lê cá tra với tốc độ kinh hoàng — ba nhát dao sắc lẹm, phi lê sạch không dính một vảy xương. Con dao Masamoto gia truyền lướt qua thịt cá như cắt lụa. Camera zoom cận cảnh, khán giả trầm trồ.

Anh ướp phi lê bằng hỗn hợp nước mắm Phú Quốc cốt 40 độ đạm, mật ong rừng U Minh, tiêu Phú Quốc xay tươi và một chút bột nghệ Hưng Yên — hoàn toàn nguyên liệu Việt Nam, không pha trộn bất kỳ gia vị phương Tây nào.

Rồi anh làm điều khiến ban giám khảo phải đứng dậy khỏi ghế: anh cuốn phi lê cá tra đã ướp trong lá sen tươi Đồng Tháp, buộc bằng dây lạt, rồi hấp cách thủy trong nồi đất nung trên bếp than hoa — kỹ thuật "hấp sen khói" gia truyền mà ông nội anh đã phát minh từ năm 1962.

Trong khi cá hấp, Minh Đức chuẩn bị sốt đi kèm: nước cốt dừa Bến Tre đun sôi với sả Quảng Ngãi băm nhuyễn, lá chanh Thái cắt chỉ, ớt hiểm xanh và một chút mẻ chua ủ theo phương pháp cổ truyền Bắc Bộ. Anh lọc sốt qua rây lụa, thu được một chất lỏng trắng ngà, sánh mịn, thơm nức mũi.

Món phụ: cơm cháy giòn tan chiên từ cơm nguội nấu bằng gạo ST25, rải lên trên lớp chà bông cá tra tự làm, phủ trứng muối cắt bốn phần tư.

Đồng hồ điểm. Chín mươi phút kết thúc.

Mười hai đĩa được đưa ra trước ban giám khảo gồm năm chuyên gia: một đầu bếp Pháp hai sao Michelin, một giáo sư ẩm thực từ Đại học RMIT, một nhà báo chuyên mảng F&B, và hai đại diện Hiệp hội Ẩm thực Việt Nam.

Thiên Phúc trình bày trước. Đĩa cá tra áp chảo bơ chanh của hắn trông đẹp mắt, sạch sẽ, nhưng khi giám khảo người Pháp nếm thử, ông ta chỉ gật đầu nhẹ: "Technically correct, but uninspired. This could be from any restaurant in the world. Where is Vietnam in this dish?"

Thiên Phúc tái mặt.

Đến lượt Minh Đức. Anh đặt đĩa lên bàn giám khảo: phi lê cá tra hấp lá sen nằm trên nền sốt dừa sả trắng ngà, cạnh đó là miếng cơm cháy ST25 phủ chà bông vàng óng, trang trí bằng hoa đậu biếc tím và lá kinh giới xanh mướt. Đẹp như một tác phẩm nghệ thuật.

Giám khảo Pháp cắt miếng cá, đưa vào miệng. Ông ta ngừng nhai, nhắm mắt lại. Khi mở mắt, trong đó lấp lánh sự kinh ngạc.

"Mon Dieu," ông thốt lên. "Cá tra mà có thể ngon như thế này sao? Thịt cá mềm như bơ, hương lá sen thoang thoảng, vị nước mắm và mật ong tạo nên một umami cực kỳ sâu. Và sốt dừa sả này — đây không phải fusion, đây là bản sắc! Đây là Việt Nam trong từng thớ thịt!"

Giáo sư RMIT gật đầu liên tục: "Kỹ thuật hấp sen khói tôi chưa từng thấy trong bất kỳ giáo trình nào. Đây là di sản ẩm thực sống."

Kết quả được công bố. Trần Minh Đức — quán Phở Đức, quận 4 — Giải Nhất tuyệt đối, điểm số 48/50, cao nhất trong mười hai năm lịch sử cuộc thi.

Lý Thiên Phúc — Kim Ngân Palace — Hạng 7.

Khi MC trao cúp vàng cho Minh Đức, năm trăm khán giả đứng dậy vỗ tay. Camera VTV3 zoom thẳng vào khuôn mặt Thiên Phúc — tái nhợt, đôi mắt trống rỗng, tay hắn run rẩy nắm chặt chiếc tạp dề xanh navy.

Minh Đức bước xuống sân khấu, đi ngang qua Thiên Phúc. Anh không nói gì, chỉ khẽ đặt tay lên vai hắn, siết nhẹ một cái rồi bước tiếp. Cái siết vai đó nặng hơn mọi lời sỉ nhục — nó nói: "Mày ăn cắp công thức của tao, nhưng mày không bao giờ ăn cắp được tài năng."

Hoàng Gia Khánh ngồi ở hàng ghế VIP, mặt xám ngoét. Hắn biết rằng kể từ hôm nay, cái tên Trần Minh Đức sẽ không còn là "đầu bếp bị đuổi" nữa — mà là "Siêu Đầu Bếp Sài Gòn," bốn chữ như bốn cái tát nảy lửa vào mặt hắn."""

# ─── CHƯƠNG 6 ──────────────────────────────────────────────────────────────────
ch6_title = "Chương 6: Nhà Hàng 'Vỉa Hè' Ra Đời"
ch6 = """Sau cuộc thi, mọi thứ thay đổi chóng mặt. Minh Đức nhận được hàng chục lời mời hợp tác từ các tập đoàn F&B lớn, nhưng anh từ chối tất cả. Anh không muốn làm thuê cho ai nữa.

Bảo Ngọc ngồi với anh trong quán phở đã đóng cửa lúc nửa đêm, trước mặt hai người là xấp giấy A4 chi chít số liệu.

"Anh Đức, thời điểm này là hoàn hảo. Tiền giải thưởng năm trăm triệu, cộng với doanh thu tích lũy từ quán phở hai tháng qua gần ba trăm triệu, anh có tám trăm triệu. Đủ để mở một nhà hàng nhỏ," Bảo Ngọc tính toán.

"Nhà hàng? Tôi mới bị đuổi khỏi nhà hàng, giờ mở nhà hàng?" Minh Đức cười khổ.

"Không phải nhà hàng bình thường. Anh sẽ mở một nhà hàng mang tên 'Vỉa Hè' — fine dining street food. Không gian thiết kế như quán vỉa hè Sài Gòn xưa: ghế nhựa, bàn inox, quạt trần cũ. Nhưng thức ăn là fine dining level, giá tầm trung để ai cũng tiếp cận được. Concept này chưa ai làm ở Việt Nam."

Minh Đức im lặng suy nghĩ. Mắt anh dần sáng lên.

Ba tháng sau, nhà hàng "VỈA HÈ" khai trương tại một căn nhà phố cổ ba tầng trên đường Lê Lợi, quận 1. Bảo Ngọc đã thương lượng được hợp đồng thuê dài hạn với giá ưu đãi nhờ mối quan hệ rộng trong ngành.

Không gian nhà hàng khiến giới F&B Sài Gòn choáng váng. Tầng một thiết kế y hệt một quán ăn vỉa hè những năm 1990: nền gạch tàu, ghế nhựa đỏ xanh, bàn inox gập, xe đẩy bán hàng rong, đèn dây tóc vàng mờ ảo, tường dán poster phim Việt cũ. Nhưng ẩn sau vẻ ngoài bình dân đó là hệ thống bếp mở hiện đại nhất Sài Gòn: bếp than hoa Josper nhập từ Tây Ban Nha, lò nướng đa năng Rational, tủ lạnh Hoshizaki, và hệ thống thông gió cấp nhà hàng Michelin.

Tầng hai là private dining room cho khách VIP, thiết kế tối giản kiểu Nhật nhưng sử dụng toàn bộ vật liệu Việt Nam: gỗ mít Tây Nguyên, gốm Bát Tràng, lụa Hà Đông.

Tầng ba là bếp nghiên cứu và phòng đào tạo, nơi Minh Đức sẽ phát triển menu mới và đào tạo thế hệ đầu bếp trẻ.

Menu nhà hàng Vỉa Hè gồm mười hai món, mỗi món là một biến tấu fine dining từ món ăn đường phố kinh điển Việt Nam. Phở bò wagyu hầm hai mươi bốn giờ. Bún chả Hà Nội với thịt lợn Iberico nướng than nhãn. Bánh mì ổ với gan ngỗng foie gras và pate gia truyền. Cơm tấm sườn với sườn non bò Mỹ sous vide bảy mươi hai giờ. Chè khúc bạch vị trà ô long Lâm Đồng.

Giá trung bình: hai trăm năm mươi nghìn đồng một suất — rẻ hơn nhiều so với fine dining truyền thống nhưng đắt hơn quán ăn bình thường. Đủ để tạo cảm giác "sang nhưng không xa xỉ."

Đêm khai trương, nhà hàng full chỗ sáu mươi khách trong vòng mười lăm phút mở đặt bàn. Hàng trăm người xếp hàng bên ngoài. Food blogger từ khắp châu Á bay đến — từ Hàn Quốc, Nhật Bản, Singapore.

Nhưng khoảnh khắc đáng nhớ nhất đêm đó không phải lúc khai trương. Đó là lúc mười giờ tối, khi cánh cửa nhà hàng mở ra và bước vào là — Hoàng Gia Khánh.

Hắn đến không phải với tư cách thù địch. Hắn đến với tư cách đối thủ cạnh tranh, muốn tận mắt xem Minh Đức làm được gì.

Khánh ngồi vào bàn góc, gọi đúng năm món đắt nhất trong menu. Thiên Phúc ngồi bên cạnh, mặt cúi gằm.

Minh Đức thấy họ từ bếp mở. Anh không tức giận, không run rẩy. Anh bình thản bưng từng đĩa ra bàn của Khánh, tự tay phục vụ.

"Phở bò wagyu Nhật A5, nước dùng ninh hai mươi bốn tiếng từ xương bò Kobe và xương gà Bình Định, ăn kèm chanh Hậu Giang và ớt hiểm Tiền Giang," Minh Đức đặt tô phở xuống, giọng chuyên nghiệp không chút cảm xúc.

Khánh nhìn tô phở, rồi nhìn Minh Đức. Hắn nhấc đũa ăn, không nói một lời. Khi nước dùng chạm vào vị giác, Khánh biết — không, toàn bộ hội trường đều biết qua biểu cảm trên mặt hắn — rằng Kim Ngân Palace chưa bao giờ và sẽ không bao giờ nấu được tô phở này.

Khánh đặt đũa xuống, im lặng đứng dậy, rút ví trả tiền không thiếu một đồng. Khi bước ra cửa, hắn dừng lại, không quay đầu lại.

"Trần Minh Đức, mày giỏi hơn tao tưởng," Khánh nói khẽ, giọng khàn đặc.

"Tôi biết," Minh Đức đáp, giọng bình thản.

Cánh cửa nhà hàng Vỉa Hè đóng lại sau lưng Khánh, nhưng cuộc chiến giữa hai bên chỉ mới thực sự bắt đầu."""

# ─── CHƯƠNG 7 ──────────────────────────────────────────────────────────────────
ch7_title = "Chương 7: Bí Mật Gia Truyền Ba Đời"
ch7 = """Nhà hàng Vỉa Hè hoạt động được hai tháng, doanh thu ổn định ở mức một tỷ hai trăm triệu mỗi tháng, lợi nhuận ròng ba trăm sáu mươi triệu. Con số mà bất kỳ nhà hàng mới mở nào cũng phải mơ ước.

Nhưng Minh Đức không hài lòng. Anh biết rằng để thực sự xây dựng đế chế, anh cần nhiều hơn một nhà hàng. Anh cần một thương hiệu, một câu chuyện, một di sản.

Một buổi tối, sau khi nhà hàng đóng cửa, Minh Đức ngồi trong bếp nghiên cứu tầng ba, lật giở cuốn sổ tay công thức cũ kỹ của ông nội. Cuốn sổ bìa da nâu sẫm, đã ngả vàng theo thời gian, mỗi trang viết tay bằng mực tím nắn nót.

Bảo Ngọc ngồi đối diện, quan sát anh. Hai tháng làm việc cùng nhau, mối quan hệ giữa họ đã vượt ra ngoài khuôn khổ đối tác kinh doanh, nhưng cả hai đều giả vờ không nhận ra điều đó.

"Anh biết không, ông nội tôi không chỉ là đầu bếp phở," Minh Đức bắt đầu kể, giọng trầm lắng. "Ông là Trần Văn Hào, sinh năm 1930 tại phố Hàng Đồng, Hà Nội. Ông được học nấu ăn từ năm mười hai tuổi dưới sự dạy dỗ của cụ nội tôi — Trần Văn Khiêm, người từng là bếp trưởng cho một gia đình quý tộc Pháp tại Hà Nội thời thuộc địa."

"Cụ nội anh nấu cho người Pháp?" Bảo Ngọc ngạc nhiên.

"Đúng. Nhưng cụ không nấu món Pháp cho họ. Cụ nấu món Việt Nam đẳng cấp đến mức gia đình quý tộc đó từ bỏ rượu vang Bordeaux để uống rượu nếp cái hoa vàng, từ bỏ bouillabaisse để ăn bún cá Hà Nội. Cụ chính là người sáng tạo ra kỹ thuật hấp sen khói mà tôi dùng trong cuộc thi."

Minh Đức lật đến trang cuối cùng của cuốn sổ. Ở đó, viết bằng nét chữ run run của ông nội trước khi qua đời, là mười hai công thức "Quốc Bảo" — mười hai món ăn mà ông Hào tin rằng đại diện cho đỉnh cao ẩm thực Việt Nam, nhưng chưa bao giờ được công bố.

"Mười hai món Quốc Bảo," Minh Đức đọc tên từng món, giọng anh rung nhẹ. "Phở hoàng cung — công thức nguyên bản từ thời Nguyễn. Bún bò huế đại nội — gia vị mười sáu loại không trùng lặp. Chả cá Lã Vọng cổ truyền — trước khi bị thương mại hóa và đơn giản hóa. Nem rán Hà thành — với nhân tôm he và mộc nhĩ rừng Tây Bắc..."

Bảo Ngọc ngồi lặng nghe, đôi mắt cô sáng lên với mỗi cái tên. Cô là người hiểu ẩm thực, và cô biết rằng những gì Minh Đức đang giữ trong tay không chỉ là công thức — đó là di sản văn hóa phi vật thể vô giá.

"Anh Đức, anh có biết mình đang giữ gì không?" Bảo Ngọc nói, giọng nghiêm trang. "Đây không phải công thức nấu ăn. Đây là bản đồ ADN của ẩm thực Việt Nam suốt một trăm năm. Nếu được phục dựng và giới thiệu đúng cách, nó có thể thay đổi cách thế giới nhìn nhận ẩm thực Việt."

Minh Đức gật đầu chậm rãi. "Tôi biết. Vì vậy tôi không bao giờ bán nó, không bao giờ để nó rơi vào tay những kẻ như Khánh. Ông nội dặn tôi: 'Chỉ truyền cho người có tâm, có tầm, và có đức. Nếu không tìm được người xứng đáng, thà mang theo xuống mồ.'"

Bảo Ngọc đưa tay đặt lên bàn tay Minh Đức, nhẹ nhàng nhưng chắc chắn. "Anh đã tìm được cách rồi. Nhà hàng Vỉa Hè sẽ là nơi phục dựng mười hai món Quốc Bảo này. Không phải dưới dạng fine dining xa xỉ mà chỉ giới siêu giàu được ăn, mà dưới dạng ẩm thực đại chúng — để mọi người Việt Nam đều được nếm thử đỉnh cao di sản cha ông."

Đêm hôm đó, Minh Đức bắt đầu phục dựng món đầu tiên trong bộ sưu tập Quốc Bảo: Phở Hoàng Cung. Anh nghiên cứu từng dòng chữ viết tay của ông nội, giải mã những thuật ngữ ẩm thực cổ xưa, thử nghiệm liều lượng gia vị hàng chục lần.

Ba tuần sau, Phở Hoàng Cung chính thức xuất hiện trên menu nhà hàng Vỉa Hè, giới hạn mười suất mỗi ngày, giá ba trăm năm mươi nghìn đồng. Tin tức lan truyền như lửa cháy rừng. Danh sách chờ kéo dài đến ba tháng.

Một nhà báo ẩm thực quốc tế từ tạp chí Bon Appétit bay từ New York sang Sài Gòn chỉ để ăn thử. Bài viết của ông đăng trên số tháng sau với dòng tiêu đề: "The Lost Royal Pho of Vietnam: A Street Food Chef is Resurrecting a Nation's Culinary Heritage."

Bài báo được chia sẻ hơn một trăm nghìn lần trên toàn thế giới. Đế chế ẩm thực của Trần Minh Đức không còn là giấc mơ — nó đang thành hình."""

# ─── CHƯƠNG 8 ──────────────────────────────────────────────────────────────────
ch8_title = "Chương 8: Đế Chế Kim Ngân Sụp Đổ"
ch8 = """Trong khi nhà hàng Vỉa Hè lên như diều gặp gió, Kim Ngân Palace đang chìm trong khủng hoảng.

Kể từ khi Minh Đức ra đi, chất lượng món ăn tại Kim Ngân tụt dốc thảm hại. Thiên Phúc dù đã học thuộc nhiều công thức, nhưng hắn thiếu thứ quan trọng nhất — khẩu vị thiên bẩm và khả năng cân chỉnh gia vị theo trực giác mà chỉ những đầu bếp bậc thầy mới có.

Sốt demi-glace của Minh Đức cần ninh chín tiếng ở nhiệt độ chính xác 87 độ C, Thiên Phúc ninh ở 92 độ khiến sốt bị đắng. Nước dùng phở cần ba lần hớt bọt trong ba mươi phút đầu, Thiên Phúc chỉ hớt hai lần khiến nước đục. Mỗi sai số nhỏ tích lũy lại thành thảm họa.

Điểm TripAdvisor của Kim Ngân Palace rơi từ 4.8 xuống 3.9 trong vòng ba tháng. Lượng đặt bàn giảm bốn mươi phần trăm. Doanh thu sụt hai tỷ mỗi tháng.

Nhưng đó chưa phải điều tệ nhất. Điều tệ nhất xảy ra vào một tối thứ Bảy, khi một đoàn khách VIP mười hai người từ tập đoàn Samsung Hàn Quốc đến dùng bữa tại Kim Ngân Palace. Đây là bữa tiệc tiếp khách quan trọng do một công ty đối tác Việt Nam tổ chức, tổng hóa đơn dự kiến hơn một trăm triệu đồng.

Thiên Phúc quyết định trổ tài với món signature mà hắn tự tin nhất: bò wagyu áp chảo truffle. Nhưng vì muốn tiết kiệm chi phí để lấy lòng Khánh (hắn đã bị cắt thưởng hai tháng liên tiếp do doanh thu giảm), Thiên Phúc dùng truffle Trung Quốc giả truffle Périgord Pháp, và thịt bò Úc loại 2 thay vì wagyu Nhật A5.

Giám đốc Samsung Hàn Quốc, một người sành ăn bậc nhất, cắn miếng đầu tiên và nhíu mày. Ông ta gọi quản lý ra, nói bằng tiếng Anh lạnh lùng: "This is not wagyu A5. The marbling is wrong, the texture is wrong, and this truffle smells like soil, not like Périgord. Are you trying to cheat us?"

Bữa tiệc kết thúc trong im lặng chết chóc. Samsung hủy toàn bộ hợp đồng đối tác. Công ty Việt Nam tổ chức bữa tiệc đâm đơn kiện Kim Ngân Palace về tội gian lận thương mại, với bằng chứng là hóa đơn menu ghi rõ "wagyu A5 Nhật Bản" và "truffle Périgord Pháp."

Báo chí nhảy vào. VnExpress, Tuổi Trẻ, Thanh Niên đồng loạt đăng bài: "Nhà hàng 5 sao Kim Ngân Palace bị tố gian lận nguyên liệu, dùng hàng Trung Quốc giá rẻ thay thế hàng cao cấp."

Cổ phiếu tập đoàn Hoàng Kim F&B Group trên sàn HOSE lao dốc hai mươi ba phần trăm trong một tuần, mất gần ba trăm tỷ đồng vốn hóa. Các nhà đầu tư rút vốn hàng loạt. Ba chi nhánh Kim Ngân tại Đà Nẵng, Nha Trang và Hà Nội buộc phải đóng cửa tạm thời.

Hoàng Gia Khánh họp báo khẩn, đổ hết tội cho Thiên Phúc: "Đây là hành vi cá nhân của bếp trưởng Lý Thiên Phúc, không đại diện cho chính sách của tập đoàn. Chúng tôi đã sa thải ngay lập tức."

Thiên Phúc bị đuổi việc — y hệt cách hắn từng giúp Khánh đuổi Minh Đức. Nhưng lần này, không có food blogger nào quay video khen hắn, không có nhà tư vấn nào chìa tay giúp, không có cuốn sổ công thức gia truyền nào trong ba lô.

Hắn bước ra khỏi cổng Kim Ngân Palace dưới cơn mưa Sài Gòn, vali kéo lạch cạch trên vỉa hè ướt nhẫy, và bỗng nhớ lại đêm mưa cách đây gần một năm khi hắn ném túi đồ của Minh Đức xuống vũng nước.

Karma. Nhân quả. Gieo gì gặt nấy.

Nhưng Thiên Phúc chưa biết rằng, phần tồi tệ nhất vẫn chưa đến. Minh Đức không phải người trả thù bằng cách hả hê nhìn kẻ thù sụp đổ — anh trả thù bằng cách vươn cao đến mức kẻ thù phải ngước lên mà khóc."""

# ─── CHƯƠNG 9 ──────────────────────────────────────────────────────────────────
ch9_title = "Chương 9: Michelin Gõ Cửa"
ch9 = """Sáu tháng sau khi nhà hàng Vỉa Hè khai trương, một email bằng tiếng Pháp được gửi đến hòm thư info@viahesaigon.com. Bảo Ngọc là người đọc email đầu tiên, và cô phải đọc đi đọc lại ba lần trước khi tin rằng mình không mơ.

"Anh Đức, lại đây," cô gọi, giọng run nhẹ.

Email đến từ Văn phòng Hướng dẫn Michelin Quốc tế, thông báo rằng nhà hàng Vỉa Hè đã lọt vào danh sách đề cử cho Michelin Guide Vietnam 2027 — phiên bản đầu tiên của Michelin tại Việt Nam. Đoàn thanh tra viên bí mật đã đến ăn tại nhà hàng ít nhất ba lần trong sáu tháng qua mà không ai hay biết.

Minh Đức đọc email, hai tay anh siết chặt thành ghế.

Ba tuần sau, lễ công bố Michelin Guide Vietnam 2027 được tổ chức trọng thể tại Nhà hát Thành phố Hồ Chí Minh. Hơn ba trăm khách mời từ giới ẩm thực trong nước và quốc tế, đại sứ quán các nước, truyền thông quốc tế tề tựu đông đủ.

Minh Đức mặc vest đen đơn giản, bên cạnh là Bảo Ngọc trong chiếc áo dài trắng thanh lịch. Cô nắm tay anh dưới gầm bàn — lần đầu tiên họ chạm vào nhau trước đám đông, dù không ai nhìn thấy.

Danh sách Bib Gourmand — những quán ăn giá cả phải chăng với chất lượng xuất sắc — được công bố trước. Không có tên Vỉa Hè. Minh Đức siết tay Bảo Ngọc chặt hơn.

Rồi đến phần công bố sao Michelin. Một sao. Hai sao.

"Nhà hàng tiếp theo nhận một sao Michelin," MC đọc, giọng trang trọng, "là một hiện tượng đã khiến cả thế giới ẩm thực quốc tế phải chú ý. Từ quán phở vỉa hè quận 4 đến fine dining street food concept đầu tiên tại Việt Nam, nhà hàng này đã chứng minh rằng ẩm thực đường phố Việt Nam hoàn toàn xứng đáng đứng trên sân khấu thế giới."

"MỘT SAO MICHELIN — NHÀ HÀNG VỈA HÈ, QUẬN 1, THÀNH PHỐ HỒ CHÍ MINH. ĐẦU BẾP TRẦN MINH ĐỨC!"

Hội trường vỡ tung trong tiếng vỗ tay, tiếng hô và tiếng huýt sáo. Ba trăm người đứng dậy ovation khi Minh Đức bước lên sân khấu, nhận tấm bảng Michelin từ tay Giám đốc Michelin Guide International.

Camera truyền hình quốc tế zoom vào khuôn mặt Minh Đức — đầu bếp ba mươi tuổi, da sạm nắng, tay chai sần vì sáu năm bếp núc và một năm vỉa hè, nhưng đôi mắt sáng rực như ngọn lửa trên bếp than hoa mà ông nội đã truyền lại.

"Tôi muốn dành giải thưởng này cho ông nội tôi, Trần Văn Hào," Minh Đức nói vào microphone, giọng anh run nhẹ nhưng vững vàng. "Ông dạy tôi rằng đầu bếp giỏi không cần nhà hàng sang trọng, chỉ cần một trái tim yêu ẩm thực và đôi tay không bao giờ bỏ cuộc. Ngôi sao này thuộc về ông, về cha tôi, và về mỗi người đầu bếp vỉa hè Việt Nam đang nấu ăn bằng cả linh hồn."

Khán phòng lặng đi một giây, rồi tiếng vỗ tay vang lên mãnh liệt hơn bao giờ hết.

Ở hàng ghế phía sau, một người đàn ông ngồi co ro, mặt cúi gằm. Đó là Lý Thiên Phúc. Hắn mua vé khách mời từ chợ đen với giá năm triệu đồng, chỉ để tận mắt chứng kiến. Kể từ khi bị Kim Ngân đuổi, hắn đã gửi hồ sơ xin việc đến hơn ba mươi nhà hàng ở Sài Gòn, nhưng không ai nhận — cái tên Lý Thiên Phúc gắn liền với scandal gian lận nguyên liệu, là vết nhơ không thể rửa sạch trong ngành F&B.

Khi Minh Đức bước xuống sân khấu với tấm bảng Michelin trên tay, ánh mắt anh vô tình gặp ánh mắt Thiên Phúc. Một thoáng nhận ra, rồi Minh Đức quay đi. Không giận dữ, không khinh bỉ, không hả hê. Chỉ là sự thờ ơ — thứ còn đau hơn cả sự căm ghét.

Thiên Phúc cảm thấy như bị một bàn tay vô hình tát thẳng vào mặt. Anh ta lặng lẽ đứng dậy, rời khỏi Nhà hát Thành phố trong bóng tối, bước đi trên đường Lê Lợi vắng người, ngang qua nhà hàng Vỉa Hè đang sáng đèn rực rỡ. Qua cửa kính, hắn thấy đội ngũ đầu bếp trẻ đang nấu nướng tất bật, tiếng cười tiếng nói vang vọng — đó là bầu không khí mà hắn đã từng có, nhưng đã tự tay hủy hoại.

Đêm hôm đó, tin nhắn chúc mừng ào ạt đổ về điện thoại Minh Đức. Nhưng anh chỉ đọc một tin nhắn duy nhất, từ một số lạ: "Minh Đức, anh xứng đáng. Tôi xin lỗi. — Phúc."

Minh Đức nhìn tin nhắn hồi lâu, rồi khóa điện thoại. Anh không trả lời. Có những lời xin lỗi đến quá muộn để được chấp nhận, nhưng đủ sớm để người nói ra nó tự cứu lấy phần nhân tính cuối cùng của mình."""

# ─── CHƯƠNG 10 ─────────────────────────────────────────────────────────────────
ch10_title = "Chương 10: Đế Chế Ẩm Thực Và Cái Giá Của Phản Bội"
ch10 = """Một năm sau ngày nhận sao Michelin, đế chế ẩm thực của Trần Minh Đức đã mở rộng vượt xa mọi dự đoán.

Nhà hàng Vỉa Hè giờ có ba chi nhánh: quận 1 Sài Gòn (một sao Michelin), quận Hoàn Kiếm Hà Nội, và Hội An. Tổng doanh thu hệ thống đạt bảy tỷ đồng mỗi tháng, lợi nhuận ròng hai tỷ một. Đội ngũ một trăm hai mươi nhân viên, trong đó ba mươi hai đầu bếp được Minh Đức tự tay đào tạo.

Bảo Ngọc giờ đã chính thức trở thành CEO của Vỉa Hè Group, kiêm vai trò người phụ nữ bên cạnh Minh Đức. Họ kết hôn trong một lễ cưới giản dị tại chính nhà hàng Vỉa Hè quận 1, mâm cỗ cưới là mười hai món Quốc Bảo mà Minh Đức đã phục dựng hoàn chỉnh. Ba trăm khách mời, từ food blogger đến đại sứ Pháp, đều nghẹn ngào khi nếm tô Phở Hoàng Cung — món ăn đã thất truyền gần một thế kỷ, giờ sống lại trên bàn tiệc cưới của người đầu bếp vỉa hè.

Nhưng chương cuối cùng của câu chuyện không kết thúc ở đám cưới.

Vào một buổi sáng tháng Mười hai, Minh Đức nhận được cuộc gọi từ ngân hàng Vietcombank, chi nhánh quận 1. Tòa nhà số 88 Đồng Khởi, nơi đặt trụ sở và nhà hàng flagship của Kim Ngân Palace suốt mười lăm năm, sắp được ngân hàng phát mại để thu hồi nợ xấu. Hoàng Kim F&B Group đã phá sản, tổng nợ hơn bốn trăm tỷ đồng, tài sản bị niêm phong toàn bộ.

Hoàng Gia Khánh, từ một ông chủ tập đoàn nghìn tỷ, giờ đối mặt với bản án lừa đảo chiếm đoạt tài sản và gian lận thương mại, tổng cộng có thể lên đến mười hai năm tù.

Minh Đức lái xe đến tòa nhà 88 Đồng Khởi, đứng trước cánh cổng kính đã bị niêm phong, nhìn vào căn bếp mà anh đã cống hiến sáu năm tuổi trẻ. Bếp giờ tối om, bàn ghế phủ bụi, cái vinh quang hào nhoáng của Kim Ngân Palace đã tan thành mây khói.

"Anh có muốn mua nó không?" Bảo Ngọc đứng bên cạnh, hỏi nhẹ nhàng.

Minh Đức im lặng hồi lâu. "Mua để làm gì? Để trả thù?"

"Không. Để xây dựng," Bảo Ngọc đáp. "Vị trí này hoàn hảo cho Học viện Ẩm thực Vỉa Hè — nơi đào tạo thế hệ đầu bếp trẻ Việt Nam miễn phí, truyền dạy mười hai món Quốc Bảo và kỹ thuật ẩm thực gia truyền cho bất kỳ ai có đam mê, bất kể xuất thân."

Minh Đức quay sang nhìn vợ, đôi mắt anh sáng lên. Anh gật đầu.

Hai tuần sau, Minh Đức mua lại toàn bộ tòa nhà 88 Đồng Khởi với giá phát mại bốn mươi hai tỷ đồng — chỉ bằng một phần ba giá trị thực. Tin tức khiến toàn bộ giới F&B Sài Gòn chấn động: cựu đầu bếp bị đuổi giờ mua lại chính tòa nhà nơi mình từng bị vứt ra đường.

Ngày Minh Đức đến ký hợp đồng công chứng, anh bước vào tòa nhà bằng cửa chính — cánh cửa mà một năm trước, bảo vệ đã lôi anh ra bằng cửa sau. Anh đi qua sảnh đón khách, qua phòng ăn VIP, lên tầng hai mươi ba — văn phòng cũ của Hoàng Gia Khánh.

Căn phòng trống hoác, chỉ còn lại chiếc bàn gỗ sồi to lớn và chiếc ghế da xoay. Trên bàn, Minh Đức thấy một bức ảnh úp mặt xuống — bức ảnh Khánh chụp với Thiên Phúc trong ngày khai trương Kim Ngân Palace, cả hai cười toe toét, tay nâng ly champagne.

Minh Đức nhặt bức ảnh lên, nhìn hồi lâu, rồi đặt nó vào thùng rác.

"Anh Đức." Một giọng nói yếu ớt vang lên từ cửa phòng.

Minh Đức quay lại. Lý Thiên Phúc đứng đó, gầy rộc đi, râu ria không cạo, mắt trũng sâu. Hắn mặc một chiếc áo sơ mi nhàu nát, tay cầm một phong bì.

"Mày vào đây làm gì?" Minh Đức hỏi, giọng không có cảm xúc.

Thiên Phúc quỳ xuống. Đúng nghĩa đen — hai đầu gối chạm sàn đá hoa cương lạnh ngắt, đầu cúi gằm. Phong bì trong tay hắn rơi xuống sàn, bên trong là một lá thư viết tay dài bốn trang.

"Anh Đức, em xin lỗi," Thiên Phúc nói, giọng nghẹn ngào. "Em biết lời xin lỗi này không đáng một xu. Em đã phản bội anh vì tham lam, vì ghen tị với tài năng của anh, vì muốn tắt đường ngắn đến thành công. Nhưng con đường ngắn đó dẫn em thẳng xuống vực thẳm."

"Em mất tất cả. Việc làm, danh dự, bạn bè, gia đình. Vợ em bỏ đi, mang theo con gái hai tuổi. Ba mẹ em ở quê Bình Dương không dám nhìn mặt em vì xấu hổ. Sáu tháng qua em sống bằng tiền bán xe, bán đồ, ở trọ trong phòng hai triệu rưỡi một tháng ở Bình Tân."

Minh Đức nhìn xuống người đàn ông đang quỳ dưới chân mình — người mà một năm trước đã ném đồ cá nhân của anh xuống vũng nước, đã cười khinh bỉ "anh xứng đáng bị đuổi," đã xước con dao Masamoto gia truyền.

Minh Đức cúi xuống, nhặt phong bì lên, rút lá thư ra đọc. Bốn trang viết tay, chữ run rẩy, kể lại toàn bộ sự thật: Khánh là người chủ mưu toàn bộ vụ vu oan, Thiên Phúc là người chỉnh sửa log kho lạnh, làm giả chứng từ xuất nhập, và dàn dựng bằng chứng camera. Lá thư kèm theo bản sao các tin nhắn Zalo giữa Khánh và Thiên Phúc — bằng chứng trực tiếp về âm mưu cướp đoạt công thức.

"Em giữ những tin nhắn này làm bảo hiểm cho mình, nhưng giờ em giao hết cho anh," Thiên Phúc nói. "Anh muốn dùng nó để kiện Khánh thêm tội vu khống cũng được, em sẵn sàng ra tòa làm chứng."

Minh Đức đọc xong lá thư, gấp lại cẩn thận, bỏ vào túi áo vest.

"Đứng lên," anh nói.

Thiên Phúc ngẩng đầu, mắt đỏ hoe.

"Tôi nói đứng lên." Minh Đức lặp lại, giọng vẫn bình thản.

Thiên Phúc loạng choạng đứng dậy, không dám nhìn thẳng vào mắt Minh Đức.

"Phúc, tôi không tha thứ cho mày," Minh Đức nói, từng chữ rõ ràng như dao cắt. "Những gì mày làm không chỉ hại tôi mà còn hại chính mày. Nhưng tôi cũng không phải người trả thù kẻ đã gục ngã."

Anh rút từ túi trong áo vest ra một tấm danh thiếp, đặt lên bàn.

"Học viện Ẩm thực Vỉa Hè sẽ khai giảng khóa đầu tiên vào tháng tới, tại chính tòa nhà này. Nếu mày thực sự muốn làm lại, mày có thể đăng ký học viên. Không miễn phí — mày sẽ phải rửa bát, dọn bếp, lau sàn, làm mọi công việc nặng nhọc nhất trong sáu tháng trước khi được chạm vào dao. Đó là cái giá cho một lần bắt đầu lại."

Thiên Phúc nhìn tấm danh thiếp, nước mắt lăn dài trên má.

"Và một điều nữa," Minh Đức bước đến cửa, dừng lại quay đầu nhìn Thiên Phúc lần cuối. "Con dao Masamoto mà mày xước. Tôi đã mài lại rồi. Vết xước không còn nữa. Nhưng tôi không bao giờ quên nó từng ở đó."

Minh Đức bước ra khỏi tòa nhà 88 Đồng Khởi, nơi ánh nắng Sài Gòn tháng Mười hai dịu dàng tỏa xuống. Bảo Ngọc đang đợi anh bên chiếc ô tô, mỉm cười.

"Xong chưa?" cô hỏi.

"Xong rồi," anh đáp, nắm tay vợ. "Mình về nhà hàng đi. Còn phải chuẩn bị menu cho Michelin Guide 2028 — lần này, anh nhắm hai sao."

Bảo Ngọc cười, lắc đầu. "Anh tham lam quá."

"Không phải tham lam. Là tham vọng," Minh Đức cười, nụ cười tự tin của người đàn ông đã vượt qua vực thẳm và chạm đến đỉnh cao. "Ông nội nói: đầu bếp ngừng nấu thì chết, nhưng đầu bếp ngừng mơ thì còn tệ hơn chết."

Chiếc xe lăn bánh trên đường Đồng Khởi, ngang qua những nhà hàng sang trọng mà một năm trước Minh Đức không đủ tư cách bước vào. Giờ đây, chính những nhà hàng đó đang treo bảng "Tuyển đầu bếp — Ưu tiên học viên Học viện Vỉa Hè."

Từ quán phở ba mươi nghìn bốn vỉa hè quận 4 đến đế chế Michelin một sao, từ kẻ bị đuổi giữa đêm mưa đến ông chủ mua lại chính tòa nhà nơi mình từng bị sỉ nhục — câu chuyện của Trần Minh Đức không chỉ là sảng văn vả mặt.

Đó là bản hùng ca của tài năng, lòng kiên trì, và niềm tin rằng: không có vực thẳm nào đủ sâu để chôn vùi một người biết nấu ăn bằng cả linh hồn."""

# ═══════════════════════════════════════════════════════════════════════════════
# ASSEMBLY & PUBLISHING PIPELINE
# ═══════════════════════════════════════════════════════════════════════════════

def build_novel():
    """Assemble and format novel into publishable JSON structure."""
    log("🚀 BUILDING NOVEL: " + NOVEL_TITLE)

    chapters_raw = [
        (ch1_title, ch1),
        (ch2_title, ch2),
        (ch3_title, ch3),
        (ch4_title, ch4),
        (ch5_title, ch5),
        (ch6_title, ch6),
        (ch7_title, ch7),
        (ch8_title, ch8),
        (ch9_title, ch9),
        (ch10_title, ch10),
    ]

    formatted_chapters = []
    total_sentences = 0
    for title, raw in chapters_raw:
        html = format_v13(raw)
        sentence_count = html.count("<p>")
        total_sentences += sentence_count
        formatted_chapters.append({
            "title": title,
            "content": html
        })
        log(f"  ✓ {title} — {sentence_count} sentences")

    novel = {
        "title": NOVEL_TITLE,
        "author": NOVEL_AUTHOR,
        "genre": NOVEL_GENRE,
        "intro": NOVEL_INTRO,
        "chapters": formatted_chapters
    }

    log(f"📊 Total: {len(formatted_chapters)} chapters, {total_sentences} sentences")
    return novel


def save_json(novel, path="pending_novel_daubep.json"):
    """Save novel to JSON file."""
    full_path = os.path.join(BASE_DIR, path)
    with open(full_path, "w", encoding="utf-8") as f:
        json.dump(novel, f, ensure_ascii=False, indent=2)
    log(f"💾 Saved to {full_path}")
    return full_path


def generate_cover(title):
    """Generate cover image using overlay engine."""
    base_path = os.path.join(BASE_DIR, COVER_BASE)
    output_path = os.path.join(BASE_DIR, "pending_cover.png")

    if not os.path.exists(base_path):
        log(f"⚠️ Base cover not found: {base_path}")
        return None

    log(f"🎨 Generating cover overlay on {COVER_BASE}...")
    cmd = [
        "python3", os.path.join(BASE_DIR, "cover_overlay_standard.py"),
        "--input", base_path,
        "--output", output_path,
        "--title", title,
        "--subtitle", f"Bản hùng ca sảng văn của {NOVEL_AUTHOR}"
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode == 0:
        log("✓ Cover generated successfully!")
        return output_path
    else:
        log(f"❌ Cover generation failed: {res.stderr}")
        return None


def get_ftp_connection(retries=5, delay=5):
    for i in range(retries):
        try:
            log(f"Connecting to FTP (attempt {i+1}/{retries})...")
            ftp = ftplib.FTP(FTP_HOST, timeout=60)
            ftp.login(FTP_USER, FTP_PASS)
            return ftp
        except Exception as e:
            log(f"⚠️ FTP connection failed: {e}")
            if i < retries - 1:
                time.sleep(delay * (i + 1))
    raise Exception("Fatal: Failed to connect to FTP after multiple attempts")


def publish_live(novel, cover_path=None):
    """Upload cover + publish novel via FTP and publish_novel.php."""
    log("🚀 STARTING LIVE PUBLICATION PIPELINE")

    # Step 1: Upload publish_novel.php helper
    log("📤 Uploading publish_novel.php helper...")
    try:
        ftp = get_ftp_connection()
        helper_path = os.path.join(BASE_DIR, "publish_novel.php")
        with open(helper_path, "rb") as f:
            ftp.storbinary("STOR publish_novel.php", f)
        log("✓ Helper uploaded.")
        ftp.quit()
    except Exception as e:
        log(f"❌ Fatal: Could not upload helper: {e}")
        sys.exit(1)

    # Step 2: Upload cover if available
    cover_local_filename = ""
    if cover_path and os.path.exists(cover_path):
        random_id = random.randint(100000, 999999)
        cover_local_filename = f"cover_sideload_{random_id}.png"
        log(f"📤 Uploading cover as /wp-content/uploads/{cover_local_filename}...")
        try:
            ftp = get_ftp_connection()
            ftp.cwd("wp-content/uploads")
            with open(cover_path, "rb") as cf:
                ftp.storbinary(f"STOR {cover_local_filename}", cf)
            ftp.quit()
            log("✓ Cover uploaded via FTP.")
        except Exception as e:
            log(f"⚠️ Cover upload failed: {e}")
            cover_local_filename = ""

    # Step 3: HTTP POST to publish
    log("🌐 Publishing novel via API...")
    payload = {
        "secret_token": SECRET_TOKEN,
        "title": novel["title"],
        "intro": novel["intro"],
        "author": novel["author"],
        "genre": novel["genre"],
        "chapters": novel["chapters"]
    }
    if cover_local_filename:
        payload["cover_local_filename"] = cover_local_filename

    try:
        api_url = f"{WP_URL}/publish_novel.php"
        res = requests.post(api_url, json=payload, timeout=300)
        res_data = res.json()

        if res_data.get("success"):
            log(f"🎉 SUCCESS! Novel published!")
            log(f"   -> Live ID: {res_data['story_id']}")
            log(f"   -> Cover Status: {res_data['cover_status']}")
            log(f"   -> Chapters: {res_data['chapters_count']} chapters posted.")

            # Update registry
            existing_path = os.path.join(BASE_DIR, "existing_novels.json")
            existing = []
            if os.path.exists(existing_path):
                try:
                    with open(existing_path, "r", encoding="utf-8") as ef:
                        existing = json.load(ef)
                except Exception:
                    pass

            existing.append({
                "id": res_data["story_id"],
                "title": novel["title"],
                "slug": novel["title"].lower().replace(" ", "-"),
                "intro": novel["intro"]
            })
            with open(existing_path, "w", encoding="utf-8") as ef:
                json.dump(existing, ef, ensure_ascii=False, indent=2)
            log("✓ Updated existing_novels.json registry.")
        else:
            log(f"❌ API Error: {res_data}")
    except Exception as ae:
        log(f"❌ API Exception: {ae}")

    # Step 4: Cleanup
    log("🧹 Cleaning up publish_novel.php from remote...")
    try:
        ftp = get_ftp_connection()
        ftp.delete("publish_novel.php")
        log("✓ Deleted publish_novel.php for security.")
        ftp.quit()
    except Exception as e:
        log(f"⚠️ Could not delete helper: {e}")

    # Clean local pending cover
    if cover_path and os.path.exists(cover_path):
        try:
            os.remove(cover_path)
        except Exception:
            pass

    log("🏁 PUBLICATION COMPLETE!")


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Write and publish: ĐẦU BẾP BỊ ĐUỔI")
    parser.add_argument("--dry-run", action="store_true", help="Build + save JSON only, no publish")
    parser.add_argument("--live", action="store_true", help="Full pipeline: build + cover + publish")
    args = parser.parse_args()

    if not args.dry_run and not args.live:
        print("❌ Specify --dry-run or --live")
        parser.print_help()
        sys.exit(1)

    novel = build_novel()
    json_path = save_json(novel)

    if args.dry_run:
        log("🔬 DRY-RUN COMPLETE. Novel saved to JSON.")
        print(f"\n📖 {novel['title']}")
        print(f"✍️  {novel['author']}")
        print(f"📚 {len(novel['chapters'])} chapters")
        for ch in novel["chapters"]:
            sentences = ch["content"].count("<p>")
            print(f"   → {ch['title']} ({sentences} sentences)")
    elif args.live:
        cover = generate_cover(novel["title"])
        publish_live(novel, cover)


if __name__ == "__main__":
    main()
