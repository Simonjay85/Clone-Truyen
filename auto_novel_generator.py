import os
import json
import time
import urllib.parse
import random
import requests
import re
import ftplib

OPENAI_KEY = "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"
FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"
WP_URL = "https://doctieuthuyet.com"

# 10 Highly Localized Vietnamese Hot Tropes Database
TROPE_DATABASE = [
    {
        "id": "thau_tom_cong_nghe",
        "title_keywords": ["Công Nghệ", "Thâu Tóm", "Bẫy", "Cổ Phiếu", "Tập Đoàn"],
        "trope_title": "Bẫy Thâu Tóm Tập Đoàn Công Nghệ",
        "intro_template": "Main character is a silent co-founder of a top tech firm in Hanoi, kicked out by his greedy partner using fake intellectual property claims. He forms a new startup, recruits a brilliant female AI researcher (early competent helper), and triggers a massive short squeeze / hostile takeover on the stock market to crush the partner.",
        "concept_guidelines": "Bối cảnh: Hà Nội, cụ thể là các tòa văn phòng tại Cầu Giấy và Hoàn Kiếm. Nam chính là cựu đồng sáng lập thiên tài bị đuổi đi. Nữ chính là tiến sĩ AI xuất sắc du học từ Mỹ về, làm việc trực tiếp hỗ trợ nam chính. Bẫy phản diện: dùng giao dịch khống gài nam chính vi phạm luật bản quyền sở hữu trí tuệ của tập đoàn cũ. Tình huống khó khăn Chương 4: Dự án mới bị thanh tra Sở Thông tin và Truyền thông kết hợp thanh tra Sở Kế hoạch Đầu tư đình chỉ khẩn cấp vì đơn tố cáo giả mạo, tài sản cá nhân bị phong tỏa tạm thời tại Vietcombank, đối thủ bơm tiền truyền thông bôi nhọ trên mạng xã hội với hàng triệu lượt xem. Lật kèo Chương 5: Nam chính tung bằng chứng ghi âm giao dịch ngầm của phản diện và hồ sơ kiểm toán chứng minh phản diện cấu kết với thế lực nước ngoài để rút ruột tập đoàn cũ, đồng thời thực hiện cú thâu tóm ngược (hostile takeover) thông qua gom cổ phiếu trên sàn giao dịch chứng khoán Hà Nội (HNX), khiến phản diện bị cơ quan cảnh sát điều tra tội phạm kinh tế C03 còng tay ngay trong phòng họp cổ đông."
    },
    {
        "id": "chang_re_bep_truong",
        "title_keywords": ["Rể", "Bếp Trưởng", "Phú Quốc", "Michelin", "Ẩn Thế"],
        "trope_title": "Chàng Rể Bếp Trưởng Ẩn Thế",
        "intro_template": "Mocked as a lazy stay-at-home husband by his wife's family (who runs a failing boutique resort in Phu Quoc). But he is actually the 'Bàn Tay Vàng' - a culinary god certified by Michelin who owns the supreme restaurant network. When the family resort is about to be seized by a corrupt competitor, he steps in, cooks the legendary banquet for the prime minister/global VIP, and vả mặt the entire rival clan.",
        "concept_guidelines": "Bối cảnh: Đảo ngọc Phú Quốc và các nhà hàng sang trọng ven biển. Nam chính bị gia đình vợ (đặc biệt là mẹ vợ và anh rể hờ) sỉ nhục là vô dụng, chỉ biết nấu cơm rửa bát. Nữ chính (vợ nam chính) là người luôn bảo vệ anh âm thầm dù áp lực rất lớn từ gia tộc. Bẫy phản diện: gài bẫy tài chính khiến resort của gia đình vợ nợ ngân hàng Vietcombank 50 tỷ sắp bị siết nợ, ép bán lại resort với giá rẻ mạt. Tình huống khó khăn Chương 4: Nhà hàng của resort bị phá hoại thức ăn gây ngộ độc thực phẩm giả, báo chí đưa tin giật gân, resort bị phong tỏa, người vợ bị tai nạn xe máy gãy tay phải nhập viện cấp cứu do kẻ xấu dàn dựng. Lật kèo Chương 5: Nam chính công khai thân phận là siêu đầu bếp Michelin thế giới, được đích thân chủ tịch tập đoàn khách sạn toàn cầu và đoàn VIP cấp cao của bộ ngoại giao đến đón tiếp. Anh thực hiện một bữa tiệc ẩm thực đỉnh cao thuyết phục hoàn toàn các siêu tỷ phú nước ngoài rót vốn 200 tỷ trực tiếp cứu resort, đồng thời trưng ra bằng chứng đối thủ thuê người độc hại thực phẩm và dàn dựng tai nạn, khiến đối thủ lập tức bị bắt giữ."
    },
    {
        "id": "than_y_phong_kham",
        "title_keywords": ["Thần Y", "Phòng Khám", "Sài Gòn", "Bác Sĩ", "Bệnh Viện"],
        "trope_title": "Thần Y Phòng Khám Đa Khoa Sài Gòn",
        "intro_template": "An outstanding young doctor working at an ordinary clinic in TP.HCM, framed for a medical error by a jealous boss who stole his revolutionary research paper. Nam chính is actually the personal doctor of the nation's wealthiest tycoons. When the tycoon collapses, the boss fails to treat him, and nam chính performs a miraculous surgery right in front of the TV cameras.",
        "concept_guidelines": "Bối cảnh: Các bệnh viện lớn ở TP.HCM (Quận 1, Quận 5). Nam chính bị giám đốc phòng khám đa khoa tư nhân tư lợi chà đạp, cướp đề tài nghiên cứu ghép tạng/tế bào gốc. Nữ chính là cô y tá trưởng thông minh, luôn hỗ trợ nam chính ghi lại các bằng chứng nghiên cứu thực tế. Bẫy phản diện: vu khống nam chính làm chết bệnh nhân bằng cách tráo đổi đơn thuốc của phòng khám. Tình huống khó khăn Chương 4: Nam chính bị đình chỉ giấy phép hành nghề y, bị đưa lên công an quận điều tra, dư luận phẫn nộ ném đá, người bố già của nam chính ở quê nghe tin đổ bệnh nặng. Lật kèo Chương 5: Siêu tỷ phú hàng đầu Việt Nam bị đột quỵ nguy kịch, các bác sĩ đầu ngành bất lực, nam chính được đặc cách thực hiện ca mổ cứu sống tỷ phú ngay trước sự chứng kiến của hội đồng y học. Toàn bộ âm mưu tráo đổi thuốc của phản diện được y tá trưởng công khai bằng video camera ẩn, khiến phản diện bị tước bằng vĩnh viễn và chịu án tù chung thân."
    },
    {
        "id": "trong_sinh_bat_dong_san",
        "title_keywords": ["Trọng Sinh", "Bất Động Sản", "Làm Giàu", "Đất", "Hà Thành"],
        "trope_title": "Trọng Sinh Đầu Cơ Bất Động Sản Hà Thành",
        "intro_template": "Main character dies of poverty and betrayal after a land deal in Hanoi. He is reborn in 2008 with a clear memory of all real estate booms, major infrastructure projects (Cầu Nhật Tân, vành đai 3), and stock surges. He outsmarts the predatory loan sharks, partners with an elite legal consultant (female lead), and buys out the rival developer's entire portfolio before they can trigger a margin call on him.",
        "concept_guidelines": "Bối cảnh: Hà Nội thời kỳ mở rộng địa giới hành chính (2008). Các khu vực đất Hoài Đức, Đông Anh, Ba Vì sốt nóng. Nam chính trọng sinh về năm 2008 đúng ngày bị người yêu cũ cắm sừng và bị chủ nợ siết nhà. Nữ chính là nữ luật sư bất động sản vô cùng tài năng và sắc sảo, giúp anh xử lý pháp lý. Bẫy phản diện: dùng hợp đồng ủy quyền giả để gài nam chính vào khoản nợ tín dụng đen 10 tỷ nhằm cướp mảnh đất vàng anh vừa mua. Tình huống khó khăn Chương 4: Văn phòng môi giới bị giang hồ đập phá, tài khoản ngân hàng Techcombank bị tòa án phong tỏa tạm thời để giải quyết tranh chấp đất, đối thủ mua chuộc truyền thông đưa tin anh là kẻ lừa đảo đa cấp bất động sản. Lật kèo Chương 5: Nam chính dùng kiến thức kiếp trước dự đoán chính xác quy hoạch cầu Nhật Tân và đường vành đai giúp tập đoàn lớn gom đất lãi hàng ngàn tỷ, nhận được sự bảo trợ cấp cao. Anh lật mặt bẫy hợp đồng giả bằng việc công khai chữ ký kiểm định pháp y, đẩy toàn bộ nhóm tín dụng đen và phản diện vào vòng lao lý vì tội lừa đảo chiếm đoạt tài sản."
    },
    {
        "id": "thua_ke_tram_ty",
        "title_keywords": ["Thừa Kế", "Trăm Tỷ", "Giả Nghèo", "Sính Lễ", "Mẹ Vợ"],
        "trope_title": "Người Thừa Kế Trăm Tỷ Giả Nghèo",
        "intro_template": "Mocked by his fiancee and her mother who demands a 5-billion sính lễ and calls him a 'nhà quê'. The next day, he inherits a 900-billion VND trust fund left by his legendary grandfather, but he continues to dress simple. When the fiancee's family tries to humiliate him at a high-end bidding event at Landmark 81, he casually walks on stage as the VIP buyer.",
        "concept_guidelines": "Bối cảnh: TP.HCM, Landmark 81, các biệt thự Phú Mỹ Hưng quận 7. Nam chính giả nghèo làm nhân viên văn phòng bình thường để thử lòng bạn gái, bị mẹ vợ tương lai sỉ nhục, đòi sính lễ 5 tỷ đồng và ép gả cho một thiếu gia giàu xỏ lá. Nữ chính là trợ lý tổng tài xinh đẹp, thông minh thuộc quỹ thác do ông nội nam chính để lại. Bẫy phản diện: gài bẫy khiến nam chính bị vu khống ăn cắp tài liệu mật của công ty và bị đuổi việc nhục nhã. Tình huống khó khăn Chương 4: Nam chính bị bạn gái ruồng bỏ công khai trong tiệc đính hôn hoành tráng, bị đám bảo vệ đánh đuổi ra ngoài dưới mưa, tài khoản bị khóa tạm thời do thủ tục xác minh tài sản thừa kế kéo dài. Lật kèo Chương 5: Tại buổi đấu thầu dự án thế kỷ của thành phố diễn ra tại sảnh Vip Landmark 81, phản diện tự đắc nghĩ mình thắng thầu, nhưng nam chính bước ra với tư cách Chủ tịch hội đồng quản trị kiêm đại diện pháp luật của Siêu quỹ Thác có tài sản 1.000 tỷ, từ chối toàn bộ gói thầu của phản diện, công bố hành vi trộm cắp và hối lộ của phản diện khiến gia đình bạn gái cũ quỳ lạy xin tha thứ nhưng vô vọng."
    },
    {
        "id": "chang_re_hao_mon_mien_tay",
        "title_keywords": ["Rể", "Hào Môn", "Miền Tây", "Sầu Riêng", "Tỷ Phú"],
        "trope_title": "Chàng Rể Hào Môn Miền Tây",
        "intro_template": "A billionaire heir of a premier shipping empire in Saigon hides his status and works in a fruit orchard in Ben Tre to find true love. Mocked as a dirt-poor peasant by greedy local wealthy families who try to seize the land, he steps up when a financial crisis strikes the orchard, using his massive shipping network and capital to conquer the market.",
        "concept_guidelines": "Bối cảnh: Miền Tây sông nước thanh bình nhưng khốc liệt thương trường (Bến Tre, Cần Thơ). Nam chính giả làm nông dân chăm vườn sầu riêng trăm tỷ. Nữ chính là con gái chủ vườn xinh đẹp, kiên cường, luôn cùng nam chính vượt qua khó khăn. Bẫy phản diện: liên minh thu mua ép giá nông sản, gài bẫy tài chính khiến chủ vườn nợ ngân hàng Agribank 30 tỷ sắp bị siết nợ để ép nữ chính gả cho con trai gã đầu nậu độc quyền phân phối thuốc trừ sâu. Tình huống khó khăn Chương 4: Toàn bộ hệ thống tưới tiêu của vườn bị đầu độc hóa chất, trái non rụng đầy gốc, các ngân hàng đồng loạt từ chối gia hạn nợ, tài khoản người cha bị phong tỏa. Lật kèo Chương 5: Nam chính khôi phục thân phận thế tử của Tập đoàn vận tải hàng hải lớn nhất Việt Nam. Trong vòng 2 tiếng, anh điều động hạm đội drone phun thuốc trung hòa sinh học từ Singapore về cứu vườn, đồng thời mua đứt chi nhánh ngân hàng Agribank địa phương để xóa nợ, thực hiện thâu tóm ngược tập đoàn hóa chất của phản diện, khiến gã và con trai bị khởi tố vì tội phá hoại tài sản và đầu độc môi trường."
    },
    {
        "id": "chien_than_duoc_pham",
        "title_keywords": ["Dược", "Chiến Thần", "Đà Lạt", "Công Thức", "Y Học"],
        "trope_title": "Chiến Thần Dược Phẩm Độc Bản",
        "intro_template": "A brilliant bio-tech researcher in Dalat who holds the patented formula for a breakthrough liver drug. When his corrupt director steals the formula to launch a highly hyped IPO, the main character and his brilliant intellectual property lawyer (female lead) trigger a massive clinical trial audit and molecular trap that destroys the corrupt director's entire empire.",
        "concept_guidelines": "Bối cảnh: Viện nghiên cứu sinh học Đà Lạt và các tòa cao ốc tài chính Quận 1, TP.HCM. Nam chính là nhà khoa học thiên tài bị đánh cắp bản quyền. Nữ chính là luật sư sở hữu trí tuệ sắc sảo tốt nghiệp từ Anh về, hỗ trợ anh đòi lại công lý. Bẫy phản diện: Giám đốc viện nghiên cứu cấu kết với quỹ đầu tư ngoại bang để ăn cắp công thức, đăng ký sở hữu trí tuệ khống và đệ đơn kiện nam chính tội tiết lộ bí mật công nghệ. Tình huống khó khăn Chương 4: Nam chính bị tạm giữ hình sự 24 giờ để điều tra, tài khoản VietinBank bị đóng băng, phòng thí nghiệm riêng bị niêm phong, truyền thông bôi nhọ anh là kẻ tráo đổi mẫu thử nghiệm gây biến chứng nghiêm trọng. Lật kèo Chương 5: Nữ chính công bố bằng chứng video camera siêu nhỏ ghi lại cảnh phản diện lấy trộm dữ liệu, kết hợp kết quả kiểm nghiệm lâm sàng độc lập chứng minh công thức phản diện ăn cắp chứa lỗi 'khóa phân tử sinh học' khiến thuốc mất tác dụng sau 30 ngày. IPO của phản diện lập tức sụp đổ trắng bên mua trên sàn HoSE, phản diện bị bắt giam khân cấp vì tội lừa đảo chiếm đoạt tài sản nhà đầu tư và vi phạm bản quyền quốc gia."
    },
    {
        "id": "vua_ban_le_duong_pho",
        "title_keywords": ["Bán Lẻ", "Đường Phố", "Sài Gòn", "Chuỗi", "Trà Sữa"],
        "trope_title": "Vua Bán Lẻ Đường Phố Sài Gòn",
        "intro_template": "A street-food stall owner in Saigon uses game theory and cutting-edge decentralized supply chains to build the fastest-growing domestic tea/coffee franchise, fighting against a predatory multi-billion foreign cafe chain that attempts to crush local businesses by bribing suppliers and running black PR.",
        "concept_guidelines": "Bối cảnh: Các ngõ hẻm ẩm thực Quận 3, Quận 10 và các văn phòng tại Quận 1, TP.HCM. Nam chính là chàng trai nghèo tự thân khởi nghiệp. Nữ chính là cựu giám đốc vận hành thông minh từ tập đoàn đa quốc gia đầu quân cho anh từ ngày đầu. Bẫy phản diện: Chuỗi cà phê ngoại bang mua chuộc toàn bộ nhà cung cấp nguyên liệu nông sản sạch tại Lâm Đồng nhằm cắt đứt nguồn cung của nam chính, đồng thời thuê KOL bẩn đưa tin sản phẩm của anh chứa chất cấm gây ung thư. Tình huống khó khăn Chương 4: Cơ quan Quản lý thị trường đình chỉ hoạt động toàn bộ 50 cửa hàng của nam chính để thanh tra chuyên đề, các nhà cung cấp đồng loạt đơn phương chấm dứt hợp đồng, nợ đối tác lên tới 15 tỷ đồng, nhân viên hoang mang nghỉ việc. Lật kèo Chương 5: Nam chính công bố hệ thống truy xuất nguồn gốc nông sản bằng công nghệ Blockchain tích hợp mã QR trên từng ly trà, chứng minh nguyên liệu hoàn toàn organic đạt chuẩn VietGAP. Đồng thời, anh công khai video ghi âm phản diện đưa hối lộ cho KOL để tạo scandal giả. Chuỗi ngoại bang bị tẩy chay triệt để, buộc phải rút khỏi thị trường Việt Nam, còn phản diện chịu án phạt hành chính kịch khung và phạt tù vì tội cạnh tranh không lành mạnh."
    },
    {
        "id": "vo_than_bao_ve",
        "title_keywords": ["Võ Thần", "Bảo Vệ", "Hải Phòng", "Cảng", "Vệ Sĩ"],
        "trope_title": "Võ Thần Bảo Vệ Đại Tiểu Thư",
        "intro_template": "An elite special forces operative returns to Haiphong as a humble bodyguard to protect the beautiful heiress of the largest shipping and logistics corporation in Northern Vietnam. He unravels a massive conspiracy of corrupt board members who are smuggling illegal cargo to seize control of the ports.",
        "concept_guidelines": "Bối cảnh: Thành phố cảng Hải Phòng, các bến tàu sầm uất và biệt thự tại Đồ Sơn. Nam chính là cựu đặc nhiệm hải quân tinh nhuệ ẩn thân. Nữ chính là đại tiểu thư thông minh, sắc sảo kế thừa tập đoàn hàng hải của cha. Bẫy phản diện: Các chú bác ruột trong hội đồng quản trị móc nối với băng nhóm buôn lậu quốc tế để đầu độc chủ tịch (cha nữ chính) và dàn dựng tai nạn cướp quyền điều hành cảng. Tình huống khó khăn Chương 4: Người cha rơi vào hôn mê sâu tại bệnh viện Tiệp Khắc Hải Phòng, phản diện tổ chức đại hội cổ đông khẩn cấp tước quyền của nữ chính, chặn mọi đường rút tài chính, và phái sát thủ truy kích hai người trong đêm mưa bão tại một kho bến bãi hoang phế. Lật kèo Chương 5: Nam chính phô diễn võ lực đỉnh cao, một tay dẹp gọn toán sát thủ, bảo vệ an toàn cho nữ chính. Anh trưng ra sắc lệnh đặc biệt phối hợp với Cảnh sát biển Việt Nam và Cục phòng chống buôn lậu, bắt quả tang lô hàng cấm trị giá 500 tỷ của phản diện tại cảng Đình Vũ, tống giam toàn bộ nhóm phản diện ngay trong cuộc họp hội đồng quản trị, trả lại sự trong sạch và vinh quang cho gia tộc nữ chính."
    },
    {
        "id": "thien_tai_fintech",
        "title_keywords": ["Fintech", "Thiên Tài", "Công Nghệ", "Ngân Hàng", "Hà Nội"],
        "trope_title": "Thiên Tài Khởi Nghiệp Fintech",
        "intro_template": "A brilliant mathematics genius and coder in Hanoi invents an un-hackable micro-lending blockchain application. Traditional banking elites try to frame him for financial fraud to steal his technology, but he and his female cyber-security co-founder trigger a brilliant algorithmic trap that bankrupts the rival's digital bank.",
        "concept_guidelines": "Bối cảnh: Thung lũng silicon thu nhỏ tại Duy Tân, Cầu Giấy và các văn phòng tài chính quanh Hồ Hoàn Kiếm, Hà Nội. Nam chính là nhà toán học trẻ xuất chúng. Nữ chính là chuyên gia an ninh mạng hàng đầu, người luôn đồng hành kỹ thuật cùng anh. Bẫy phản diện: Thiếu gia ngân hàng truyền thống cài gián điệp ăn cắp mã nguồn bản thử nghiệm, sau đó cấu kết với một số cán bộ thoái hóa để cáo buộc nam chính vận hành tín dụng đen bất hợp pháp. Tình huống khó khăn Chương 4: Máy chủ của dự án bị tấn công DDoS tê liệt hoàn toàn, app bị gỡ khỏi App Store/Google Play, nam chính bị triệu tập điều tra, người dân kéo đến bao vây trụ sở đòi rút tiền do tin đồn ác ý. Lật kèo Chương 5: Nam chính và nữ chính kích hoạt 'giao thức dự phòng phi tập trung' bảo mật đa tầng, chuyển dịch toàn bộ dữ liệu an toàn sang đám mây của Thụy Sĩ. Anh công bố bằng chứng cuộc tấn công DDoS bắt nguồn từ địa chỉ IP của ngân hàng đối thủ, đồng thời kích hoạt thuật toán thắt chặt thanh khoản khiến bộ phận ngân hàng số của phản diện bị rút tiền hàng loạt (bank run) dẫn đến mất khả năng thanh toán, phản diện bị bắt giữ vì tội danh phá hoại an ninh mạng và gian lận tài chính."
    }
]

# Datasets definition for Name Anti-Collision Filter & geographical setting rotation
PROTAGONISTS = [
    "Lê Quốc Khánh", "Đặng Thái Sơn", "Vũ Hoài Lâm", "Cao Tiến Dũng",
    "Bùi Lạc Phong", "Phùng Nhất Huy", "Trương Minh Triết", "Đỗ Trọng Nhân",
    "Tô Hoài Nam", "Đặng Thế Dân", "Phan Chí Trung", "Nguyễn Lâm Bách",
    "Võ Hoàng Minh", "Trịnh Gia Bảo", "Phạm Tuấn Kiệt", "Lâm Quốc Việt",
    "Nguyễn Đăng Khoa", "Lê Thanh Tùng", "Trần Đình Khang", "Vũ Nhật Anh",
    "Đặng Văn Lâm", "Hoàng Thế Anh", "Phùng Xuân Đông", "Tống Khánh Duy",
    "Bùi Thế Vinh", "Cao Thiên Lạc", "Lê Khắc Nam", "Trần Thế Hải",
    "Nguyễn Tấn Đạt", "Phạm Tuấn Anh", "Hoàng Việt", "Nguyễn Đức Trí",
    "Trịnh Gia Huy", "Nguyễn Hoàng Minh", "Lê Gia Bách", "Nguyễn Hải Long",
    "Trần Minh Hoàng", "Lê Quang Minh", "Hoàng Văn Nam", "Lâm Thế Khải"
]

FEMALE_LEADS = [
    "Nguyễn Hoàng Mai Chi", "Đỗ Thục Đoan", "Trịnh Khánh Quỳnh", "Phạm Nhã Phương",
    "Lê Cát Tiên", "Vũ Khánh An", "Trần Ngọc Diệp", "Đặng Mỹ Dung",
    "Cao Hoài An", "Bùi Phương Thảo", "Trịnh Hoàng Yến", "Nguyễn Minh Thư",
    "Lê Minh Thư", "Nguyễn Khánh Vy", "Trần Mỹ Duyên", "Lê Minh An",
    "Nguyễn Minh Tuyền", "Lâm Gia Hân", "Lâm Vy", "Trần Diệu Nhi",
    "Ngô Thị Hương", "Lê Mai Chi", "Trần Thanh Mai", "Lâm Vy Anh",
    "Phạm Quỳnh Chi", "Đặng Thu Thảo", "Hoàng Bảo Trâm", "Vũ Phương Trinh"
]

VILLAINS = [
    "Tạ Đình Phong", "Hứa Gia Ấn", "Phan Thanh Bình", "Lê Hữu Phước",
    "Hoàng Thế Vinh", "Trần Vĩnh Thịnh", "Đỗ Quốc Oai", "Trương Vô Kỵ",
    "Cao Hữu Hoài", "Lâm Vĩnh Nghiệp", "Lý Bách", "Nguyễn Hữu Hoài",
    "Trần Khánh Vy", "Đỗ Văn Thắng", "Phạm Gia Bảo", "Lý Bách Hoài",
    "Hoàng Kim Định", "Phạm Gia Hưng", "Vũ Hoài Nam", "Nguyễn Văn Hải",
    "Trần Quốc Thắng", "Tạ Minh Tuấn", "Vũ Minh Quân"
]

GOOD_COMPANIES = [
    "Quỹ Khởi Nguyên", "Siêu quỹ Thái Bình", "Tập đoàn Tràng An", "LogiVina",
    "Dược phẩm Bách Thảo", "Nông sản Cát Tường", "Công nghệ VinaBlock",
    "Quỹ Vạn Lộc", "Quỹ Vạn An", "Vạn An Corp", "Tập đoàn Thép Đông Hải",
    "Đế chế Bách Nghệ", "Dược Thảo Ngọc Linh", "Bảo Long Tea", "LogiChain",
    "Công nghệ PayBlock", "Đại Việt Logistics", "Năng lượng Xanh Việt"
]

EVIL_COMPANIES = [
    "Tập đoàn Thịnh Phát", "Tập đoàn Đông Á", "SouthernRealty", "PrimeTech",
    "AgroChem Việt Nam", "CyberShield", "Royal Sip", "Tập đoàn Bán lẻ Hoàng Gia",
    "Dược phẩm Vạn Xuân", "Thương mại Tín Nghĩa", "Bất động sản Đất Vàng"
]

SETTINGS = [
    "Hà Nội",
    "Sài Gòn / TP.HCM",
    "Phú Quốc",
    "Miền Tây",
    "Hải Phòng",
    "Đà Lạt",
    "Đà Nẵng",
    "Nha Trang / Khánh Hòa",
    "Tây Nguyên"
]

NARRATIVE_DISRUPTORS = [
    "Sự cố sập hệ thống máy chủ và tấn công DDoS quy mô lớn từ Thụy Sĩ gây gián đoạn dịch vụ toàn quốc, làm suy giảm nghiêm trọng uy tín dự án mới.",
    "Sự phản bội và bán đứng mã nguồn/bí mật kinh doanh từ người cộng sự thân tín nhất thuở lập nghiệp.",
    "Thay đổi đột ngột về chính sách hải quan xuất khẩu và các rào cản thuế quan phi kỹ thuật của thị trường châu Âu gây tắc nghẽn toàn bộ lô hàng đầu tiên.",
    "Khủng hoảng thanh khoản liên hoàn và đợt rút tiền hàng loạt (bank run) đột biến do tin đồn phá sản giả mạo lan truyền trên báo chí.",
    "Phản diện mua chuộc KOL bẩn và sử dụng công nghệ deepfake tinh vi để dựng scandal thực phẩm nhiễm độc hoặc ô nhiễm môi trường trên mạng xã hội."
]

def get_used_text(existing_novels):
    used_text = ""
    for novel in existing_novels:
        used_text += " " + novel.get("title", "")
        used_text += " " + novel.get("intro", "")
    return used_text

def select_unique_name(name_list, used_text, category_name="Entity"):
    valid_names = []
    for name in name_list:
        full_collision = name.lower() in used_text.lower()
        parts = name.split()
        mid_first_collision = False
        if len(parts) >= 2:
            mid_first = " ".join(parts[1:]).lower()
            mid_first_collision = mid_first in used_text.lower()
            
        if not full_collision and not mid_first_collision:
            valid_names.append(name)
            
    if valid_names:
        return random.choice(valid_names)
    return random.choice(name_list)

def rotate_setting(existing_novels):
    setting_freq = {s: 0 for s in SETTINGS}
    used_text = get_used_text(existing_novels)
    for s in SETTINGS:
        keyword = s.split("/")[0].strip()
        setting_freq[s] = used_text.count(keyword)
    sorted_settings = sorted(setting_freq.items(), key=lambda x: x[1])
    min_freq = sorted_settings[0][1]
    least_used = [s for s, freq in sorted_settings if freq == min_freq]
    return random.choice(least_used)

def robust_json_parse(raw_str):
    cleaned = raw_str.strip()
    
    # Remove markdown code fences if present
    if cleaned.startswith("```"):
        lines = cleaned.split("\n")
        if lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].startswith("```"):
            lines = lines[:-1]
        cleaned = "\n".join(lines).strip()
    
    # If the first line is still a code fence like ```json
    if cleaned.startswith("```"):
        cleaned = re.sub(r"^```(?:json)?\n", "", cleaned)
        cleaned = re.sub(r"\n```$", "", cleaned).strip()
        
    try:
        return json.loads(cleaned)
    except Exception as parse_err:
        try:
            # Try to locate the first '{' and the last '}'
            start_idx = cleaned.find("{")
            end_idx = cleaned.rfind("}")
            if start_idx != -1 and end_idx != -1 and end_idx > start_idx:
                json_candidate = cleaned[start_idx:end_idx+1]
                return json.loads(json_candidate)
        except Exception as e:
            pass
        raise parse_err

def call_openai(system_prompt, user_prompt, max_tokens=2500, temperature=0.7):
    url = "https://api.openai.com/v1/chat/completions"
    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        "temperature": temperature,
        "max_tokens": max_tokens
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_KEY}"
    }
    
    for attempt in range(3):
        try:
            res = requests.post(url, json=payload, headers=headers, timeout=120)
            res.raise_for_status()
            data = res.json()
            return data['choices'][0]['message']['content'].strip()
        except Exception as e:
            print(f"OpenAI Call Error (Attempt {attempt+1}): {e}")
            time.sleep(5)
    raise SystemExit("Fatal: Failed to connect to OpenAI API after multiple attempts.")

def get_existing_novels():
    local_path = "existing_novels.json"
    if os.path.exists(local_path):
        try:
            with open(local_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            pass
    return []

def select_unique_trope(existing_novels):
    for trope in TROPE_DATABASE:
        duplicated = False
        for novel in existing_novels:
            title = novel.get("title", "")
            matches = [kw for kw in trope["title_keywords"] if kw.lower() in title.lower()]
            if len(matches) >= 2:
                duplicated = True
                break
        if not duplicated:
            return trope
    return random.choice(TROPE_DATABASE)

def main():
    print("=" * 60)
    print("🚀 AUTOMATED 10/10 VIETNAMESE NOVEL GENERATOR & PUBLISHER")
    print("=" * 60)
    
    # Step 1: Load existing novels to prevent duplication
    existing = get_existing_novels()
    existing_titles = [item['title'] for item in existing]
    print(f"✓ Loaded {len(existing)} existing novels from database to avoid duplicates.")
    
    # Step 2: Select unique trope
    selected_trope = select_unique_trope(existing)
    print(f"✓ Selected unique trope theme: {selected_trope['trope_title']}")
    
    # Step 2.5: Apply V13 Gold name filter and geographical rotation
    used_text = get_used_text(existing)
    
    selected_protagonist = select_unique_name(PROTAGONISTS, used_text, "Protagonist")
    selected_helper = select_unique_name(FEMALE_LEADS, used_text, "Female Helper")
    selected_villain = select_unique_name(VILLAINS, used_text, "Villain")
    selected_good_company = select_unique_name(GOOD_COMPANIES, used_text, "Good Company")
    selected_evil_company = select_unique_name(EVIL_COMPANIES, used_text, "Evil Company")
    selected_setting = rotate_setting(existing)
    selected_disruptor = random.choice(NARRATIVE_DISRUPTORS)
    
    print(f"✓ Programmatic V13 Gold constraints selected:")
    print(f"  - Nam chính: {selected_protagonist}")
    print(f"  - Nữ trợ lý: {selected_helper}")
    print(f"  - Phản diện: {selected_villain}")
    print(f"  - Doanh nghiệp tốt: {selected_good_company}")
    print(f"  - Doanh nghiệp xấu: {selected_evil_company}")
    print(f"  - Bối cảnh rotated: {selected_setting}")
    print(f"  - Biến cố Chương 4: {selected_disruptor[:50]}...")
    
    # Step 3: Generate Novel Concept & Outlines via OpenAI
    system_concept_prompt = f"""Bạn là biên tập viên văn học kỳ cựu và là bậc thầy lập kịch bản sảng văn / vả mặt (slap-in-the-face web novel) hàng đầu Việt Nam.
Nhiệm vụ của bạn là lập kế hoạch cho một bộ truyện sảng văn/vả mặt 10/10 cực kỳ đặc sắc, lấy bối cảnh 100% tại Việt Nam.

CHỦ ĐỀ ĐƯỢC CHỌN CHO TÁC PHẨM NÀY:
Tên chủ đề: {selected_trope['trope_title']}
Tóm tắt định hướng: {selected_trope['intro_template']}
Hướng dẫn cốt truyện & bối cảnh chi tiết: {selected_trope['concept_guidelines']}

RÀNG BUỘC CỨNG VỀ TÊN NHÂN VẬT & TỔ CHỨC (BẮT BUỘC SỬ DỤNG CHÍNH XÁC):
1. Nhân vật Nam chính (Protagonist): Phải là "{selected_protagonist}".
2. Nhân vật Nữ trợ lý / Nữ chính đồng hành (Helper): Phải là "{selected_helper}" (người đồng hành tài năng hỗ trợ cực mạnh cho nam chính từ Chương 2).
3. Nhân vật Phản diện (Villain): Phải là "{selected_villain}" (sếp cũ, hôn thê cũ hoặc đối thủ hống hách).
4. Công ty chính diện / Siêu quỹ bảo trợ của nam chính: Phải là "{selected_good_company}".
5. Tập đoàn phản diện: Phải là "{selected_evil_company}".
6. Bối cảnh chính của câu chuyện: Phải lấy tại "{selected_setting}" và các địa danh chân thực xung quanh nó.

QUY TẮC CỐT LÕI ĐỂ ĐẠT ĐIỂM 10/10 HOÀN HẢO (CHUẨN VÀNG V13):
1. ĐỘ DÀI LINH HOẠT (Từ 8 Đến 15 Chương): Số chương tùy thuộc độ phức tạp cốt truyện, không cố định cùng một số chương cho cả batch. Hãy phân bổ cấu trúc hợp lý: mở đầu sỉ nhục (chương 1-2), nữ chính đồng hành sau khi kiểm chứng năng lực (chương 2-3), 3-5 vòng vả mặt tăng cấp, giai đoạn bế tắc khủng hoảng cực đại (khoảng 2/3 truyện), và cú lật kèo kết toán kẻ thù ở các chương cuối.
2. BIẾN CỐ NÚT THẮT CHƯƠNG KỊCH TÍNH (BẮT BUỘC): Ở chương giữa (thường là khoảng Chương 4 hoặc Chương 5), hãy lồng ghép biến cố sau: "{selected_disruptor}". Đây là đòn hiểm hóc của phản diện khiến nam chính lâm vào tình trạng bế tắc cực đại (chứ không chỉ đơn thuần là bị phong tỏa tài khoản ngân hàng).
3. PHẢN DIỆN THÔNG MINH, TRÍ TUỆ: Nhân vật phản diện không được ngốc nghếch hay chửi rủa thô thiển. Họ là giới tinh hoa hoặc kẻ trục lợi có thủ đoạn tinh vi, dùng các mưu đồ kinh doanh, pháp lý, tài chính tinh vi thực tế (ví dụ: bẫy thâu tóm thù địch qua thị trường chứng khoán, gài lỗi kiểm toán thuế, rút ruột cổ đông, kiện cáo bản quyền trí tuệ, margin call...).
4. CHI TIẾT TẢ THỰC (SHOW, DON'T TELL): Thay vì dùng các từ sáo rỗng như 'vô biên', 'tột cùng', 'kinh hoàng'. Hãy dùng các mô tả vật lý sắc bén: 'mồ hôi lạnh chảy ròng ròng sau gáy', 'môi trắng bệch không còn một giọt máu', 'hai gối đập mạnh xuống sàn kêu cộp', 'ngón tay bấm chặt rỉ máu'.
5. STORY_DNA RIÊNG: Mỗi truyện phải có bối cảnh nghề riêng, vật chứng trung tâm riêng, ít nhất 5 set-piece không bê sang truyện khác được, khủng hoảng giữa truyện riêng, signature quan hệ nam-nữ riêng và kiểu kết riêng.
6. TIÊU ĐỀ & INTRO: Tiêu đề dài 12-22 từ, có nhục ban đầu -> cú lật -> payoff. Intro 3-5 đoạn HTML, hook mạnh trong 2 câu đầu.
7. COVER PROMPT: Viết bằng tiếng Anh cho ChatGPT Image Generation, phong cách photorealistic/cinematic real human actors, 1:1, no text, no watermark, chừa vùng trên tối để đặt title.

Hãy xuất ra định dạng JSON nguyên bản, không chứa bất kỳ văn bản thừa nào bên ngoài (không dùng ```json hoặc ```)."""

    user_concept_prompt = f"""Dựa vào các truyện hiện có để tránh trùng lặp đề tài và nhân vật:
{json.dumps(existing_titles, ensure_ascii=False)}

Hãy tạo ra một bản thiết kế truyện sảng văn/vả mặt từ 8 đến 15 chương hoàn hảo theo chủ đề: "{selected_trope['trope_title']}".
Quyết định số chương (N) phù hợp nhất cho độ phức tạp của cốt truyện (8 <= N <= 15).
Trả về chính xác cấu trúc JSON sau:
{{
  "title": "Tên truyện 12-22 từ, có nhục ban đầu -> cú lật -> payoff",
  "author": "Bút danh nhà văn ấn tượng",
  "genre": "Sảng Văn",
  "intro": "3-5 đoạn HTML, mở bằng hook sỉ nhục hoặc phản bội cực mạnh",
  "cover_prompt": "Square 1:1 photorealistic Vietnamese web novel cover, real human actors, cinematic movie poster, no text, no watermark...",
  "story_dna": {{
    "profession_world": "Bối cảnh nghề/ngành riêng",
    "central_evidence": "Vật chứng trung tâm riêng",
    "unique_set_pieces": ["5 cảnh lớn riêng biệt theo ngành"],
    "midpoint_crisis": "Khủng hoảng giữa truyện riêng",
    "relationship_signature": "Cách nam nữ chính tương tác riêng",
    "ending_signature": "Kiểu kết/đạo cụ/cảnh cuối riêng"
  }},
  "outlines": [
    {{ "chap_num": 1, "outline": "Tóm tắt kịch tính chương 1..." }},
    {{ "chap_num": 2, "outline": "Tóm tắt kịch tính chương 2..." }},
    ...
    {{ "chap_num": N, "outline": "Tóm tắt kịch tính chương N..." }}
  ]
}}"""

    print("Generating unique novel concept...")
    concept_raw = call_openai(system_concept_prompt, user_concept_prompt, max_tokens=1500, temperature=0.85)
    
    try:
        novel_data = robust_json_parse(concept_raw)
        print(f"✓ Created Novel Blueprint: {novel_data['title']} by {novel_data['author']}")
    except Exception as e:
        print("Failed to parse novel blueprint JSON:")
        print(concept_raw)
        raise SystemExit(e)
        
    # Step 4: Generate detailed content for each chapter sequentially
    chapters_content = []
    
    for i, outline_item in enumerate(novel_data['outlines'], 1):
        print(f"Generating detailed Chapter {i}: {outline_item['outline'][:50]}...")
        
        system_writer_prompt = f"""Bạn là THE GHOSTWRITER - Nhà văn truyện mạng sảng văn/vả mặt số 1 Việt Nam. Bạn có văn phong miêu tả cực kỳ sống động, chân thực, sắc sảo.
QUY TẮC VIẾT 10/10 CHUYÊN NGHIỆP:
1. TUÂN THỦ TUYỆT ĐỐI TÊN NHÂN VẬT & TỔ CHỨC:
   * Nam chính: "{selected_protagonist}"
   * Nữ trợ lý/Nữ chính đồng hành: "{selected_helper}"
   * Phản diện: "{selected_villain}"
   * Công ty chính diện/Bảo trợ: "{selected_good_company}"
   * Tập đoàn phản diện: "{selected_evil_company}"
   * Bối cảnh: "{selected_setting}"
2. SHOW, DON'T TELL: Miêu tả chi tiết hành động vật lý, nét mặt, sự run rẩy, giọt mồ hôi, hay tiếng giày gót nhọn giẫm xuống sàn bê tông. Tránh các tính từ sáo rỗng như 'vô biên', 'tột cùng', 'kinh hoàng'.
3. HỘI THOẠI ĐINH TAI NHỨC ÓC: Các câu thoại sắc lẹm, thể hiện sự kiêu ngạo của kẻ thù trước khi bị vả mặt, và sự điềm tĩnh tối thượng của nhân vật chính.
4. CHI TIẾT KINH DOANH & ĐỜI SỐNG THỰC TẾ TẠI VIỆT NAM: Sử dụng các chi tiết thật về cơ cấu cổ đông, sao kê tài chính ngân hàng Việt Nam, luật doanh nghiệp Việt Nam, cơ quan nhà nước (Ủy ban Chứng khoán, C03, Sở Kế hoạch Đầu tư), và thói quen sinh hoạt bản địa.
5. ĐỘ DÀI CỰC KHỦNG (1000 - 1500 TỪ): Bắt buộc viết cực kỳ chi tiết, chậm rãi, phát triển sâu sắc tâm lý nhân vật và các đoạn hội thoại gay cấn dài lâu. Dung lượng bắt buộc phải đạt từ 1000 đến 1500 từ (khoảng 6000 - 9000 ký tự tiếng Việt bao gồm khoảng trắng). Tuyệt đối không được viết tóm tắt hay kết thúc chương quá nhanh.
6. BÁM STORY_DNA: Mỗi chương phải có ít nhất 3 chi tiết nghề/vật chứng/bối cảnh chỉ thuộc riêng truyện này, không mở chương theo template và không lặp câu/cảnh đã dùng.
7. ĐỊNH DẠNG: Chỉ sử dụng các thẻ HTML cơ bản như <p>, <strong>, <em> để trình bày nội dung sạch sẽ. Không in tiêu đề chương trong content, không in ghi chú/audit/meta.

CHỦ ĐỀ ĐANG VIẾT:
Tên chủ đề: {selected_trope['trope_title']}
Hướng dẫn bối cảnh: {selected_trope['concept_guidelines']}"""

        # Prepare context of previous chapters to maintain perfect continuity
        prev_chapters_context = ""
        if chapters_content:
            prev_titles = [c['title'] for c in chapters_content]
            prev_chapters_context += f"- Danh sách các chương trước: {json.dumps(prev_titles, ensure_ascii=False)}\n"
            
            # Lấy toàn bộ nội dung của chương liền kề trước đó (chương i-1) để làm cơ sở nối tiếp mạch lạc
            last_chap = chapters_content[-1]
            prev_chapters_context += f"- NỘI DUNG CHI TIẾT CHƯƠNG TRƯỚC ĐÓ ({last_chap['title']}) - HÃY ĐỌC LẠI ĐỂ VIẾT NỐI TIẾP TRÁNH TRÙNG LẶP HOẶC LỆCH BỐI CẢNH:\n"
            prev_chapters_context += f"\"\"\"\n{last_chap['content']}\n\"\"\"\n"

        user_writer_prompt = f"""Dựa trên bản thiết kế truyện sau:
- Tựa truyện: {novel_data['title']}
- Giới thiệu thế giới quan & nhân vật: {novel_data['intro']}
- Tác giả: {novel_data['author']}
- Story DNA chống trùng: {json.dumps(novel_data.get('story_dna', {}), ensure_ascii=False)}
 
- Dàn ý Chương {i}: {outline_item['outline']}
{prev_chapters_context}
YÊU CẦU ĐẶC BIỆT VỀ ĐỘ DÀI:
Bắt buộc nội dung trong phần "content" phải có độ dài tối thiểu từ 1000 từ trở lên (khoảng 6000 ký tự tiếng Việt đến 9000 ký tự). Hãy viết cực kỳ chi tiết, diễn giải từng hành động, suy nghĩ và hội thoại chậm rãi để đạt đủ độ dài này. Không viết tóm tắt!

YÊU CẦU TRẢ VỀ dạng JSON chính xác:
{{
  "title": "Chương {i}: Tên chương giật gân, cuốn hút",
  "content": "Nội dung chương viết hoàn chỉnh bằng Tiếng Việt 100%, định dạng HTML với các thẻ <p>, <strong>, <em>..."
}}"""

        chap_raw = call_openai(system_writer_prompt, user_writer_prompt, max_tokens=4500, temperature=0.7)
        
        try:
            chap_data = robust_json_parse(chap_raw)
            chapters_content.append(chap_data)
            print(f"  -> ✓ Finished Chapter {i}: {chap_data['title']} ({len(chap_data['content'])} chars)")
        except Exception as e:
            print(f"Failed to parse Chapter {i} JSON, trying fallback regex...")
            try:
                title_match = re.search(r'"title"\s*:\s*"(.*?)"', chap_raw)
                content_match = re.search(r'"content"\s*:\s*"(.*)"', chap_raw, re.DOTALL)
                if title_match and content_match:
                    chapters_content.append({
                        "title": title_match.group(1),
                        "content": content_match.group(1).replace('\\"', '"').replace('\\n', '\n')
                    })
                    print(f"  -> ✓ Recovered Chapter {i} via regex")
                else:
                    raise e
            except:
                print(chap_raw[:1000])
                raise SystemExit(f"Fatal error generating Chapter {i}")
                
        time.sleep(2)
        
    # Step 5: Construct premium cover from an approved local image and cover_overlay_standard.py
    import subprocess
    import shutil
    
    base_idx = random.randint(14, 63)
    base_cover_file = f"base_cover_{base_idx}.png"
    pending_cover_file = "pending_cover.png"
    
    if not os.path.exists(base_cover_file):
        # Fallback if selected index doesn't exist
        for idx in range(14, 64):
            if os.path.exists(f"base_cover_{idx}.png"):
                base_cover_file = f"base_cover_{idx}.png"
                break
                
    print(f"\n🎨 Local Cover Engine: Compiling title onto approved local image {base_cover_file}...")
    subtitle_text = f"Tác phẩm sảng văn đặc sắc của {novel_data['author']}"
    try:
        cmd = [
            "python3", "cover_overlay_standard.py",
            "--input", base_cover_file,
            "--output", pending_cover_file,
            "--title", novel_data['title'],
            "--subtitle", subtitle_text
        ]
        res = subprocess.run(cmd, capture_output=True, text=True)
        if res.returncode != 0:
            print(f"⚠️ Cover overlay failed: {res.stderr}. Copying approved local cover directly.")
            shutil.copy(base_cover_file, pending_cover_file)
        else:
            print("✓ Cover overlay generated successfully.")
    except Exception as ce:
        print(f"⚠️ Cover overlay exception: {ce}. Copying approved local cover directly.")
        shutil.copy(base_cover_file, pending_cover_file)
        
    random_id = random.randint(100000, 999999)
    cover_local_filename = f"cover_sideload_{random_id}.png"
    
    # Step 6: Upload files via FTP (Cover Sideload + Helper Script)
    print("\nUploading cover and publish_novel.php endpoint via FTP...")
    try:
        ftp = ftplib.FTP(FTP_HOST, timeout=30)
        ftp.login(FTP_USER, FTP_PASS)
        
        # Upload cover_sideload to uploads folder
        ftp.cwd("wp-content/uploads")
        with open(pending_cover_file, "rb") as f:
            ftp.storbinary(f"STOR {cover_local_filename}", f)
        print(f"✓ Uploaded sideload cover: {cover_local_filename}")
        
        # Reset directory to root and upload publish helper
        ftp.cwd("/")
        with open("publish_novel.php", "rb") as f:
            ftp.storbinary("STOR publish_novel.php", f)
        print("✓ Uploaded publish_novel.php helper script.")
        ftp.quit()
    except Exception as e:
        print("FTP Sideload Error:", e)
        raise SystemExit(e)
        
    # Clean up local pending cover file
    if os.path.exists(pending_cover_file):
        os.remove(pending_cover_file)
        
    # Step 7: Trigger story publication via HTTP call to publish_novel.php
    print("\nTriggering novel publication to doctieuthuyet.com database...")
    payload = {
        "secret_token": "ZEN_TRUYEN_2026_BYPASS",
        "title": novel_data['title'],
        "intro": novel_data['intro'],
        "author": novel_data['author'],
        "genre": novel_data['genre'],
        "cover_local_filename": cover_local_filename,
        "chapters": chapters_content
    }
    
    try:
        api_url = f"{WP_URL}/publish_novel.php"
        res = requests.post(api_url, json=payload, timeout=90)
        res_data = res.json()
        
        if res_data.get('success'):
            print("=" * 60)
            print("🎉 NOVEL PUBLISHED SUCCESSFULLY TO THE LIVE WEBSITE!")
            print(f"ID: {res_data['story_id']}")
            print(f"Title: {res_data['title']}")
            print(f"Author: {res_data['author']}")
            print(f"Cover Status: {res_data['cover_status']}")
            print(f"Chapters Published: {res_data['chapters_count']}")
            print("=" * 60)
            
            # Clean up the publish helper script from remote for security
            try:
                ftp = ftplib.FTP(FTP_HOST, timeout=30)
                ftp.login(FTP_USER, FTP_PASS)
                ftp.delete("publish_novel.php")
                print("✓ Deleted publish_novel.php helper from remote server for security.")
                ftp.quit()
            except:
                pass
                
            # Clean up local existing list cache to update it next time
            new_novel_entry = {
                "id": res_data['story_id'],
                "title": res_data['title'],
                "slug": res_data['title'].lower().replace(" ", "-"),
                "intro": novel_data['intro']
            }
            existing.append(new_novel_entry)
            with open("existing_novels.json", "w", encoding="utf-8") as f:
                json.dump(existing, f, ensure_ascii=False, indent=2)
            print("✓ Updated existing_novels.json local database.")
            
        else:
            print("Failed to publish novel via API response:", res_data)
            
    except Exception as e:
        print("API Call Error during publication:", e)
        
if __name__ == "__main__":
    main()
