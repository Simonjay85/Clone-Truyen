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
        "concept_guidelines": "Bối cảnh: Viện nghiên cứu sinh học Đà Lạt và các tòa cao ốc tài chính Quận 1, TP.HCM. Nam chính là nhà khoa học thiên tài bị đánh cắp bản quyền. Nữ chính là luật sư sở hữu trí tuệ sắc sảo tốt nghiệp từ Anh về, hỗ trợ anh đòi lại công lý. Bẫy phản diện: Giám đốc viện nghiên cứu cấu kết với quỹ đầu tư ngoại bang để ăn cắp công thức, đăng ký sở hữu trí tuệ khống và đệ đơn kiện nam chính tội tiết lộ bí mật công nghệ. Tình huống khó khăn Chương 4: Nam chính bị tạm giữ hình sự 24 giờ để điều tra, tài khoản VietinBank bị đóng băng, phòng thí nghiệm riêng bị niêm phong, truyền thông bôi nhọ anh là kẻ tráo đổi mẫu thử nghiệm gây biến chứng nghiêm trọng. Lật kèo Chương 5: Nữ chính công bố bằng chứng video camera siêu nhỏ ghi lại cảnh phản diện lấy trộm dữ liệu, kết hợp kết quả kiểm nghiệm lâm sàng độc lập chứng minh công thức phản diện ăn cắp chứa lỗi 'khóa phân tử sinh học' khiến thuốc mất tác dụng sau 30 ngày. IPO của phản diện lập tức sụp đổ trắng bên mua trên sàn HoSE, phản diện bị bắt giam khẩn cấp vì tội lừa đảo chiếm đoạt tài sản nhà đầu tư và vi phạm bản quyền quốc gia."
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
    
    # Step 3: Generate Novel Concept & Outlines via OpenAI
    system_concept_prompt = f"""Bạn là biên tập viên văn học kỳ cựu và là bậc thầy lập kịch bản sảng văn / vả mặt (slap-in-the-face web novel) hàng đầu Việt Nam.
Nhiệm vụ của bạn là lập kế hoạch cho một bộ truyện sảng văn/vả mặt 10/10 cực kỳ đặc sắc, lấy bối cảnh 100% tại Việt Nam.

CHỦ ĐỀ ĐƯỢC CHỌN CHO TÁC PHẨM NÀY:
Tên chủ đề: {selected_trope['trope_title']}
Tóm tắt định hướng: {selected_trope['intro_template']}
Hướng dẫn cốt truyện & bối cảnh chi tiết: {selected_trope['concept_guidelines']}

QUY TẮC CỐT LÕI ĐỂ ĐẠT ĐIỂM 10/10 HOÀN HẢO:
1. ĐỘ DÀI LINH HOẠT (Từ 5 Đến 15 Chương): Số chương có thể từ 5 đến 15 chương tùy thuộc vào độ phức tạp của cốt truyện. Hãy phân bổ cấu trúc câu chuyện hợp lý: mở đầu sỉ nhục (chương 1-2), trợ lý/nữ chính đồng hành (chương 2-3), đòn phản kích nhẹ và phản diện gài bẫy (chương giữa), giai đoạn bế tắc khủng hoảng cực đại (khoảng 2/3 truyện), và cú lật kèo vả mặt hoành tráng kết toán kẻ thù ở (các) chương cuối.
2. BỐI CẢNH VIỆT NAM THỰC TẾ: Bối cảnh phải cực kỳ chân thực, lấy tại Hà Nội, TP.HCM, hoặc các địa phương nổi tiếng (Landmark 81, Hồ Tây, đèo Hải Vân, Sa Đéc, Đà Lạt, ngõ phố Hà Nội...). Tên nhân vật phải là tên Việt Nam quen thuộc (Lâm Phong, Minh Nguyệt, Gia Huy, Hoàng Bách...). Tiền tệ dùng VNĐ với các con số tài chính/kinh doanh thực tế (hàng chục tỷ, sính lễ 5 tỷ, dự án 1.000 tỷ...).
3. TRÁNH TRÙNG LẶP: Đảm bảo truyện có tên tập đoàn, tên nhân vật chính/phụ và các tình tiết cụ thể HOÀN TOÀN MỚI, KHÔNG TRÙNG LẶP với các tác phẩm đã có trên hệ thống.
4. PHẢN DIỆN THÔNG MINH, CHIÊU TRÒ CAO TAY: Nhân vật phản diện không được ngốc nghếch hay gào thét vô lý. Họ phải dùng các mưu đồ kinh doanh, pháp lý, tài chính tinh vi thực tế (ví dụ: bẫy thâu tóm thù địch qua thị trường chứng khoán, gài lỗi kiểm toán thuế, rút ruột cổ đông, kiện cáo bản quyền trí tuệ, margin call...).
5. CHI TIẾT TẢ THỰC (SHOW, DON'T TELL): Thay vì dùng các từ sáo rỗng như 'vô biên', 'tột cùng', 'kinh hoàng'. Hãy dùng các mô tả vật lý sắc bén: 'mồ hôi lạnh chảy ròng ròng sau gáy', 'môi trắng bệch không còn một giọt máu', 'hai gối đập mạnh xuống sàn kêu cộp', 'ngón tay bấm chặt rỉ máu'.
6. TUYẾN TÌNH CẢM ẤM ÁP, NỮ CHÍNH/TRỢ LÝ THÔNG MINH: Nhân vật nữ chính hoặc trợ lý đồng hành phải thông minh, có năng lực vượt trội, trợ giúp đắc lực cho nam chính và được giới thiệu sâu sắc ngay từ Chương 2.

Hãy xuất ra định dạng JSON nguyên bản, không chứa bất kỳ văn bản thừa nào bên ngoài (không dùng ```json hoặc ```)."""

    user_concept_prompt = f"""Dựa vào các truyện hiện có để tránh trùng lặp đề tài và nhân vật:
{json.dumps(existing_titles, ensure_ascii=False)}

Hãy tạo ra một bản thiết kế truyện sảng văn/vả mặt từ 5 đến 15 chương hoàn hảo theo chủ đề: "{selected_trope['trope_title']}".
Quyết định số chương (N) phù hợp nhất cho độ phức tạp của cốt truyện (5 <= N <= 15).
Trả về chính xác cấu trúc JSON sau:
{{
  "title": "Tên truyện giật gân, cuốn hút và thuần Việt",
  "author": "Bút danh nhà văn ấn tượng",
  "genre": "Sảng Văn",
  "intro": "Giới thiệu truyện tóm tắt cực kỳ kịch tính, lôi cuốn độc giả (khoảng 200-300 từ dạng HTML)",
  "cover_prompt": "Prompt tiếng Anh chi tiết để vẽ ảnh bìa bằng Pollinations AI (phong cách anime web novel chuyên nghiệp, có chữ hoặc không, đậm chất sang trọng)",
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
1. SHOW, DON'T TELL: Miêu tả chi tiết hành động vật lý, nét mặt, sự run rẩy, giọt mồ hôi, hay tiếng giày gót nhọn giẫm xuống sàn bê tông. Tránh các tính từ sáo rỗng như 'vô biên', 'tột cùng', 'kinh hoàng'.
2. HỘI THOẠI ĐINH TAI NHỨC ÓC: Các câu thoại sắc lẹm, thể hiện sự kiêu ngạo của kẻ thù trước khi bị vả mặt, và sự điềm tĩnh tối thượng của nhân vật chính.
3. CHI TIẾT KINH DOANH & ĐỜI SỐNG THỰC TẾ TẠI VIỆT NAM: Sử dụng các chi tiết thật về cơ cấu cổ đông, sao kê tài chính ngân hàng Việt Nam, luật doanh nghiệp Việt Nam, cơ quan nhà nước (Ủy ban Chứng khoán, C03, Sở Kế hoạch Đầu tư), và thói quen sinh hoạt bản địa.
4. ĐỘ DÀI CỰC KHỦNG (1000 - 1500 TỪ): Bắt buộc viết cực kỳ chi tiết, chậm rãi, phát triển sâu sắc tâm lý nhân vật và các đoạn hội thoại gay cấn dài lâu. Dung lượng bắt buộc phải đạt từ 1000 đến 1500 từ (khoảng 6000 - 9000 ký tự tiếng Việt bao gồm khoảng trắng). Tuyệt đối không được viết tóm tắt hay kết thúc chương quá nhanh.
5. ĐỊNH DẠNG: Chỉ sử dụng các thẻ HTML cơ bản như <p>, <strong>, <em> để trình bày nội dung sạch sẽ.

CHỦ ĐỀ ĐANG VIẾT:
Tên chủ đề: {selected_trope['trope_title']}
Hướng dẫn bối cảnh: {selected_trope['concept_guidelines']}"""

        user_writer_prompt = f"""Dựa trên bản thiết kế truyện sau:
- Tựa truyện: {novel_data['title']}
- Giới thiệu thế giới quan & nhân vật: {novel_data['intro']}
- Tác giả: {novel_data['author']}

Hãy viết CHI TIẾT CHƯƠNG {i} của bộ truyện.
- Dàn ý Chương {i}: {outline_item['outline']}
{f"- Các chương trước đã viết tóm tắt: {json.dumps([c['title'] for c in chapters_content], ensure_ascii=False)}" if chapters_content else ""}

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
        
    # Step 5: Construct Cover Image URL via Pollinations
    escaped_prompt = urllib.parse.quote(novel_data['cover_prompt'] + ", masterpiece, highly detailed book cover, anime illustration style, vivid lighting")
    cover_url = f"https://image.pollinations.ai/prompt/{escaped_prompt}?width=800&height=1200&seed={random.randint(1, 99999)}&nologo=true"
    
    # Step 6: Upload publish_novel.php helper script via FTP
    print("\nUploading publish_novel.php endpoint to FTP root...")
    try:
        ftp = ftplib.FTP(FTP_HOST, timeout=30)
        ftp.login(FTP_USER, FTP_PASS)
        
        with open("publish_novel.php", "rb") as f:
            ftp.storbinary("STOR publish_novel.php", f)
        print("✓ Uploaded publish_novel.php to server.")
        ftp.quit()
    except Exception as e:
        print("FTP Upload Error for helper script:", e)
        raise SystemExit(e)
        
    # Step 7: Trigger story publication via HTTP call to publish_novel.php
    print("\nTriggering novel publication to doctieuthuyet.com database...")
    payload = {
        "secret_token": "ZEN_TRUYEN_2026_BYPASS",
        "title": novel_data['title'],
        "intro": novel_data['intro'],
        "author": novel_data['author'],
        "genre": novel_data['genre'],
        "cover_url": cover_url,
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
