import json
import os

def run():
    print("Loading existing concepts from novel_concepts_50.json...")
    with open("novel_concepts_50.json", "r", encoding="utf-8") as f:
        concepts = json.load(f)
    
    print(f"Loaded {len(concepts)} existing concepts.")
    
    # 37 Premium V13 highly-localized unique concepts (indices 64 to 100)
    extra_concepts = [
        {
            "idx": 64,
            "title": "Vua Cà Phê Đắk Lắk: Bị Cướp Thương Hiệu, Tôi Xây Chuỗi Đồ Uống Tỷ Đô",
            "author": "Y Jút Niê",
            "num_chapters": 10,
            "setting": "Đắk Lắk, Buôn Ma Thuột, cảng ICD Tân Cảng Cát Lái, Sở KH&CN",
            "male_lead": "Y Jút Niê, chuyên gia nông học phát triển hạt cà phê Robusta đặc sản đạt 85 điểm SCA",
            "female_lead": "Nguyễn Hoàng Mai Chi, Giám đốc điều hành Quỹ Khởi Nguyên, MBA Stanford",
            "conflict": "Đối tác cướp chỉ dẫn địa lý và nhãn hiệu 'Ban Me Coffee', pha trộn đậu nành cháy bẩn bán ra thị trường",
            "cover_desc": "Ede coffee farmer standing proudly in a sun-drenched coffee plantation holding red ripe coffee cherries, elegant female investor in business suit beside him, lush highlands landscape",
            "genre_visual": "coffee bean trade empire"
        },
        {
            "idx": 65,
            "title": "Đế Chế Yến Sào Khánh Hòa: Chàng Rể Quèn Lật Kèo Thâu Tóm Vách Đá Nghìn Tỷ",
            "author": "Lê Quốc Khánh",
            "num_chapters": 11,
            "setting": "Khánh Hòa, đảo yến Hòn Nội, Nha Trang, Vietcombank Nha Trang",
            "male_lead": "Lê Quốc Khánh, kỹ sư sinh học dẫn dụ yến bị gia đình vợ khinh rẻ, đuổi khỏi công ty yến sào",
            "female_lead": "Đỗ Thục Đoan, Phó Chủ tịch Hiệp hội Yến sào Việt Nam, chuyên gia phân tích chất lượng",
            "conflict": "Anh rể hờ dùng yến sào giả nhập khẩu từ Malaysia chứa hóa chất tẩy trắng, gài bẫy nam chính tội đầu độc người tiêu dùng",
            "cover_desc": "Confident Vietnamese engineer standing on a rocky island cliff overlooking the sea, flock of swiftlets flying in the dark stormy sky, beautiful female scientist with laboratory clipboard",
            "genre_visual": "island luxury aquaculture drama"
        },
        {
            "idx": 66,
            "title": "Chúa Tể Nước Mắm Phan Thiết: Nghệ Nhân Bị Hãm Hại Vực Dậy Vị Ngon Trăm Năm",
            "author": "Đặng Thái Sơn",
            "num_chapters": 9,
            "setting": "Phan Thiết, làng nước mắm Thanh Hải, Hiệp hội Nước mắm Truyền thống",
            "male_lead": "Đặng Thái Sơn, nghệ nhân ủ chượp nước mắm cá cơm than rút nỏ truyền thống bị cướp xưởng",
            "female_lead": "Trịnh Khánh Quỳnh, Kiểm toán viên cao cấp Big 4 EY, chuyên gia thẩm định tài chính",
            "conflict": "Tập đoàn hóa chất ép mua lại thương hiệu gia truyền, đầu độc bể chượp bằng thạch tín nhằm bôi nhọ nước mắm truyền thống",
            "cover_desc": "Traditional Vietnamese fish sauce maker in wooden vat warehouse, beautiful female auditor inspecting large jars, dramatic warm light shining on amber liquid",
            "genre_visual": "traditional food industry war"
        },
        {
            "idx": 67,
            "title": "Thần Y Dược Liệu Trà Cổ: Bị Đuổi Khỏi Lâm Trường, Tôi Xây Thung Lũng Thảo Dược",
            "author": "Vũ Hoài Lâm",
            "num_chapters": 10,
            "setting": "Quảng Ninh, Móng Cái, rừng ngập mặn Trà Cổ, Viện Dược liệu Trung ương",
            "male_lead": "Vũ Hoài Lâm, nhà nghiên cứu cây thuốc biển bị sếp gài bẫy sa thải, tước công trình sâm biển",
            "female_lead": "Phạm Nhã Phương, Phó Cục trưởng Cục Y dược Cổ truyền, Bộ Y tế",
            "conflict": "Sếp cũ ăn cắp giống sâm biển quý hiếm bán sang biên giới, vu khống nam chính phá hoại tài nguyên quốc gia",
            "cover_desc": "Vietnamese herbalist holding glowing green marine root, beautiful female government official beside him, sea-side mangrove forest at dusk, scientific mystery atmosphere",
            "genre_visual": "biotech herbal thriller"
        },
        {
            "idx": 68,
            "title": "Vua Cao Su Bình Phước: Bị Đốt Rừng Mủ, Tôi Trở Lại Làm Chủ Tập Đoàn",
            "author": "Cao Tiến Dũng",
            "num_chapters": 12,
            "setting": "Bình Phước, nông trường cao su Lộc Ninh, Sở Tài nguyên và Môi trường",
            "male_lead": "Cao Tiến Dũng, kỹ sư mủ cao su tự nhiên bị cướp quyền điều hành công ty gia đình",
            "female_lead": "Lê Cát Tiên, Luật sư chuyên ngành tranh chấp tài sản đất đai, tốt nghiệp Đại học Oxford",
            "conflict": "Chú ruột cấu kết thế lực bất động sản đốt phá rừng cao su để ép chuyển đổi mục đích sử dụng đất làm khu công nghiệp phân lô",
            "cover_desc": "Vietnamese rubber plantation manager in front of massive towering rubber trees, female lawyer holding official land lease documents, dramatic sunset casting long shadows",
            "genre_visual": "industrial forestry empire drama"
        },
        {
            "idx": 69,
            "title": "Thần Đồng Hoa Kiểng Sa Đéc: Chàng Nông Dân Quèn Thống Trị Thị Trường Tết",
            "author": "Bùi Lạc Phong",
            "num_chapters": 10,
            "setting": "Đồng Tháp, làng hoa Sa Đéc, chợ hoa xuân Bến Bình Đông Sài Gòn",
            "male_lead": "Bùi Lạc Phong, nghệ nhân lai tạo giống hoa cúc mâm xôi độc bản kháng sâu bệnh bị ép giá",
            "female_lead": "Vũ Khánh An, Giám đốc thiết kế cảnh quan đô thị TP.HCM, cựu sinh viên Đại học Kyoto",
            "conflict": "Gã thương lái độc quyền phun thuốc ức chế sinh trưởng làm hỏng toàn bộ vườn hoa Tết của bà con nhằm cưỡng đoạt đất",
            "cover_desc": "Vietnamese horticulturist looking at vibrant yellow chrysanthemums blooming under morning sun, beautiful female architect holding design layouts, colorful Sa Dec canals in the background",
            "genre_visual": "floriculture agriculture drama"
        },
        {
            "idx": 70,
            "title": "Bậc Thầy Tơ Lụa Bảo Lộc: Bị Phá Hủy Khung Dệt, Tôi Chinh Phục Sàn Di Sản Châu Á",
            "author": "Phùng Nhất Huy",
            "num_chapters": 10,
            "setting": "Lâm Đồng, Bảo Lộc, nhà máy dệt tơ lụa dâu tằm, Triển lãm Thời trang ASEAN",
            "male_lead": "Phùng Nhất Huy, kỹ sư cơ khí phục dựng khung cửi cổ dệt lụa tơ tằm vân rồng 4 tầng",
            "female_lead": "Trần Ngọc Diệp, nhà thiết kế thời trang haute couture quốc tế",
            "conflict": "Đối thủ cạnh tranh thuê côn đồ đập phá máy dệt gia truyền, tráo tơ polyester Trung Quốc rẻ tiền vào lô hàng xuất khẩu",
            "cover_desc": "Vietnamese silk weaver operating a traditional wooden loom with glowing gold silk fabrics, elegant female designer holding a rolls of premium silk, warm glowing workshop",
            "genre_visual": "luxury textile heritage drama"
        },
        {
            "idx": 71,
            "title": "Vua Gạo Nếp Tú Lệ: Nông Dân Bị Ép Đất, Tôi Bảo Vệ Quốc Hồn Dưới Chân Ruộng",
            "author": "Trương Minh Triết",
            "num_chapters": 9,
            "setting": "Yên Bái, thung lũng Tú Lệ, ruộng bậc thang Mù Cang Chải, Bộ NN&PTNT",
            "male_lead": "Trương Minh Triết, người giữ giống lúa nếp tan Tú Lệ thơm dẻo gia truyền bị cướp quyền gieo cấy",
            "female_lead": "Đặng Mỹ Dung, chuyên gia đa dạng sinh học Viện Khoa học Nông nghiệp Việt Nam",
            "conflict": "Tập đoàn phân bón giả gài bẫy bán chất độc làm bạc màu đất thung lũng nhằm mua rẻ đất ruộng bậc thang xây dựng resort",
            "cover_desc": "Vietnamese ethnic agriculturalist standing in golden terraced rice paddies at sunrise, beautiful female scientist collecting soil samples, stunning Yen Bai mountains backdrop",
            "genre_visual": "ethnic agricultural heritage"
        },
        {
            "idx": 72,
            "title": "Thần Trà Ô Long Mộc Châu: Bị Cướp Đồi Chè, Tôi Thâu Tóm Lại Sàn Giao Dịch",
            "author": "Đỗ Trọng Nhân",
            "num_chapters": 10,
            "setting": "Sơn La, đồi chè trái tim Mộc Châu, Sở Giao dịch Hàng hóa Việt Nam (MXV)",
            "male_lead": "Đỗ Trọng Nhân, brewmaster trà đen và trà Ô Long bị đối tác lừa ký hợp đồng chuyển nhượng khống",
            "female_lead": "Cao Hoài An, Giám đốc Phân tích rủi ro Sở Giao dịch Hàng hóa, cực kỳ sắc sảo",
            "conflict": "Đối tác ép nông dân phun thuốc kích thích tăng trưởng nhanh để IPO công ty nông sản, phá hủy đất chè Mộc Châu",
            "cover_desc": "Vietnamese tea master picking fresh tea leaves on misty green tea hills of Moc Chau, beautiful female financial analyst in suit looking at stock trends tablet",
            "genre_visual": "commodity trade agriculture"
        },
        {
            "idx": 73,
            "title": "Chúa Đất Hạt Điều Bình Phước: Bị Vu Oan Trốn Thuế, Tôi Xây Đế Chế Xuất Khẩu Mỹ",
            "author": "Tô Hoài Nam",
            "num_chapters": 11,
            "setting": "Bình Phước, nhà máy chế biến hạt điều xuất khẩu, Cục Thuế tỉnh, Hải quan Mỹ (CBP)",
            "male_lead": "Tô Hoài Nam, chủ cơ sở chế biến hạt điều organic bị giám đốc kiểm toán cũ cài bẫy",
            "female_lead": "Bùi Phương Thảo, Chuyên viên thương mại quốc tế Đại sứ quán Việt Nam tại Mỹ",
            "conflict": "Kẻ xấu tuồn hạt điều kém chất lượng nhiễm nấm mốc aflatoxin vào container xuất khẩu Mỹ để FDA cấm biên hãng nam chính",
            "cover_desc": "Vietnamese cashew factory owner standing before clean automated processing machinery, elegant female diplomat beside him, shipping containers at port, bright lighting",
            "genre_visual": "international trade business"
        },
        {
            "idx": 74,
            "title": "Vua Muối Ớt Tây Ninh: Chàng Trai Quèn Vực Dậy Đặc Sản Nghìn Tỷ",
            "author": "Đặng Thế Dân",
            "num_chapters": 10,
            "setting": "Tây Ninh, làng nghề làm muối ớt Trảng Bàng, Cục Sở hữu trí tuệ",
            "male_lead": "Đặng Thế Dân, thợ rang muối ớt tôm Tây Ninh gia truyền bị cướp công thức độc quyền",
            "female_lead": "Trịnh Hoàng Yến, luật sư đại diện pháp lý quyền sở hữu trí tuệ",
            "conflict": "Đầu nậu hóa chất sử dụng bột tôm thối và phẩm màu độc hại, đăng ký sở hữu trí tuệ khống tên nhãn để triệt hạ xưởng muối gốc",
            "cover_desc": "Vietnamese artisan roasting chili salt over huge traditional iron pan, hot steam and red chili flakes in air, beautiful female lawyer in suit holding SHTT certificates",
            "genre_visual": "traditional culinary battle"
        },
        {
            "idx": 75,
            "title": "Ông Trùm Nuôi Tôm Bến Tre: Bị Phá Hoại Ao Công Nghệ Cao, Tôi Thâu Tóm Thị Trường Nhật",
            "author": "Phan Chí Trung",
            "num_chapters": 11,
            "setting": "Bến Tre, Bình Đại, ao tôm siêu thâm canh công nghệ cao, VietinBank Bến Tre",
            "male_lead": "Phan Chí Trung, kỹ sư cơ điện phát minh hệ thống tuần hoàn nước ao tôm tự động bị cướp",
            "female_lead": "Nguyễn Minh Thư, Giám đốc Thẩm định tín dụng VietinBank, thạc sĩ tài chính",
            "conflict": "Đối thủ cắt nguồn điện dự phòng và xả thải bùn độc vào 20 ao tôm giống chuẩn xuất khẩu Nhật nhằm ép gán nợ ngân hàng",
            "cover_desc": "Vietnamese shrimp aquaculture engineer operating control panels at high-tech circular ponds, beautiful female bank manager with loan approval folder, coastal sunset",
            "genre_visual": "high-tech shrimp farming"
        },
        {
            "idx": 76,
            "title": "Bậc Thầy Gốm Đỏ Vĩnh Long: Bị Cướp Lò Nung, Tôi Vực Dậy Dòng Sông Đất Sét",
            "author": "Nguyễn Lâm Bách",
            "num_chapters": 10,
            "setting": "Vĩnh Long, dòng sông gốm đỏ Mang Thít, nhà máy sản xuất gốm xuất khẩu",
            "male_lead": "Nguyễn Lâm Bách, nhà thiết kế mỹ thuật đất sét đỏ không men bị giám đốc sản xuất đuổi đi",
            "female_lead": "Lê Minh Thư, kiến trúc sư trưởng quy hoạch bảo tồn làng nghề di sản Mang Thít",
            "conflict": "Chủ đầu tư phá hủy các lò gạch gốm cổ hình nấm cổ kính 100 năm để khai thác cát sông trái phép gây sạt lở nặng nề",
            "cover_desc": "Vietnamese ceramic artist shaping red clay pot in traditional brick kiln, beautiful female architect inspecting restoration drawings, Mang Thit river sunset",
            "genre_visual": "cultural heritage preservation"
        },
        {
            "idx": 77,
            "title": "Thần Y Thuốc Nam Yên Tử: Bị Vu Oan Đầu Độc, Tôi Cứu Cả Tập Đoàn Dược",
            "author": "Võ Hoàng Minh",
            "num_chapters": 10,
            "setting": "Quảng Ninh, núi thiêng Yên Tử, Viện Y học Cổ truyền Quân đội",
            "male_lead": "Võ Hoàng Minh, truyền nhân bài thuốc nam giải độc gan Yên Tử bị vu khống bốc thuốc giả",
            "female_lead": "Nguyễn Khánh Vy, Thượng tá bác sĩ quân y, trưởng khoa dược lý lâm sàng",
            "conflict": "Đối thủ tráo cây thuốc độc (lá ngón) vào kho dược liệu nam chính để tạo scandal chết người, triệt tiêu bài thuốc nam",
            "cover_desc": "Vietnamese herbal healer gathering wild herbs on mist-shrouded Yen Tu mountain cliffs, elegant female military doctor in uniform watching with research notebook",
            "genre_visual": "traditional medical thriller"
        },
        {
            "idx": 78,
            "title": "Vua Bưởi Năm Roi Bình Minh: Chàng Rể Quèn Lật Mặt Gian Thương Bán Đất Vàng",
            "author": "Trịnh Gia Bảo",
            "num_chapters": 9,
            "setting": "Vĩnh Long, thị xã Bình Minh, cù lao Mỹ Hòa, Agribank Vĩnh Long",
            "male_lead": "Trịnh Gia Bảo, kỹ sư nông nghiệp phục tráng giống bưởi ngọt Năm Roi không hạt bị mẹ vợ khinh miệt",
            "female_lead": "Trần Mỹ Duyên, kiểm toán viên kiểm soát nội bộ ngân hàng Agribank",
            "conflict": "Mẹ vợ ép bán đất cù lao trồng bưởi cho tập đoàn bất động sản lấy tiền cho con trai phá sản, gài bẫy nợ xấu ngân hàng",
            "cover_desc": "Vietnamese agriculturalist holding large green pomelo fruits in sunny orchard, elegant female auditor showing financial statement sheets, Mekong river background",
            "genre_visual": "rural real estate battle"
        },
        {
            "idx": 79,
            "title": "Nữ Hoàng Thổ Cẩm Sapa: Bị Cướp Hoa Văn, Tôi Chinh Phục London Fashion Week",
            "author": "Lâm Quốc Việt",
            "num_chapters": 10,
            "setting": "Lào Cai, Sapa, làng nghề thổ cẩm Hmong, London Fashion Week",
            "male_lead": "Lâm Quốc Việt, nghệ nhân nhuộm chàm cổ truyền vùng cao Tây Bắc",
            "female_lead": "Lê Minh An, nhà thiết kế thời trang bền vững thổ cẩm tốt nghiệp Central Saint Martins London",
            "conflict": "Tập đoàn dệt công nghiệp Trung Quốc sao chép kỹ thuật vẽ sáp ong và hoa văn thổ cẩm đăng ký bản quyền toàn cầu",
            "cover_desc": "Beautiful ethnic textile designer holding hand-woven indigo fabrics, handsome young indigo dyer beside her, dramatic foggy Sapa mountain peak at background",
            "genre_visual": "ethnic fashion design drama"
        },
        {
            "idx": 80,
            "title": "Chúa Đảo Ngọc Phú Quốc: Bị Tráo Ngọc Trai Đen, Tôi Cứu Cả Vương Quốc Biển",
            "author": "Nguyễn Đăng Khoa",
            "num_chapters": 10,
            "setting": "Phú Quốc, vịnh Dương Tơ, trang trại nuôi ngọc trai, Sở Du lịch Kiên Giang",
            "male_lead": "Nguyễn Đăng Khoa, kỹ sư cấy nhân ngọc trai đen quý hiếm bị vu oan trộm cắp ngọc quý",
            "female_lead": "Nguyễn Minh Tuyền, Chuyên gia giám định ngọc trai thuộc Viện đá quý quốc gia",
            "conflict": "Đối tác tráo ngọc trai nhựa Trung Quốc rẻ tiền vào lô ngọc trai đen xuất khẩu cho hoàng gia Nhật, kiện nam chính lừa đảo",
            "cover_desc": "Vietnamese pearl farmer presenting glowing black pearl in shell on diving boat, elegant female gemologist examining it with microscope, beautiful turquoise sea of Phu Quoc",
            "genre_visual": "ocean pearl luxury drama"
        },
        {
            "idx": 81,
            "title": "Bậc Thầy Chè Đắng Cao Bằng: Bị Đốt Rừng Trà Cổ, Tôi Thâu Tóm Sàn Trà Thế Giới",
            "author": "Lê Thanh Tùng",
            "num_chapters": 9,
            "setting": "Cao Bằng, Thạch An, đồi chè đắng cổ thụ, Cục Bảo vệ Thực vật",
            "male_lead": "Lê Thanh Tùng, thợ sao chè đắng thủ công giữ kỹ thuật sấy than củi hồng ngoại bị sa thải",
            "female_lead": "Lâm Gia Hân, Giám đốc Quỹ bảo tồn di sản nông nghiệp Đông Nam Á",
            "conflict": "Hãng trà công nghiệp xịt thuốc diệt cỏ thiêu rụi đồi chè cổ thụ 200 tuổi để triệt hạ nguồn nguyên liệu đặc sản",
            "cover_desc": "Vietnamese tea farmer drying green tea leaves on bamboo mats, beautiful female foundation director, dramatic mountain scenery of Cao Bằng karst landscape",
            "genre_visual": "tea agriculture battle"
        },
        {
            "idx": 82,
            "title": "Vua Muối Hầm Tuyết Sa Cà Ná: Chàng Kỹ Sư Quèn Vực Dậy Đặc Sản Hoàng Gia",
            "author": "Trần Đình Khang",
            "num_chapters": 10,
            "setting": "Ninh Thuận, đồng muối Cà Ná, Viện Tiêu chuẩn Chất lượng Việt Nam",
            "male_lead": "Trần Đình Khang, kỹ sư nhiệt động lực học chế tạo lò hầm muối tuyết tinh khiết bị cướp máy",
            "female_lead": "Lâm Vy, chuyên gia kiểm định tiêu chuẩn thực phẩm quốc tế HACCP",
            "conflict": "Gã quản lý nhà máy cướp thiết kế lò muối, sử dụng thạch cao rẻ tiền pha trộn muối hầm gây suy thận người dùng",
            "cover_desc": "Vietnamese engineer standing proudly in a glowing white salt field of Ca Na under burning sun, beautiful female inspector holding quality certificate, red sunset",
            "genre_visual": "salt processing drama"
        },
        {
            "idx": 83,
            "title": "Ông Trùm Nước Khoáng Kim Bôi: Bị Đầu Độc Nguồn Khoáng, Tôi Trở Lại Làm Chủ Mỏ",
            "author": "Vũ Nhật Anh",
            "num_chapters": 11,
            "setting": "Hòa Bình, suối khoáng nóng Kim Bôi, Sở Tài nguyên và Môi trường",
            "male_lead": "Vũ Nhật Anh, địa chất học phát hiện mạch nước khoáng nóng sâu 400m bị cướp quyền khai thác",
            "female_lead": "Trần Diệu Nhi, Luật sư trưởng tập đoàn nước giải khát lớn nhất Việt Nam",
            "conflict": "Tập đoàn rác thải chôn trộm chất độc hóa học gần mạch nước khoáng nóng nhằm ép nam chính bán rẻ đất mỏ nước khoáng",
            "cover_desc": "Vietnamese geologist testing water in steaming hot spring of Kim Boi, beautiful female lawyer beside him, lush tropical jungle, misty dramatic lighting",
            "genre_visual": "environmental corporate thriller"
        },
        {
            "idx": 84,
            "title": "Thiên Tài Đúc Đồng Đại Bái: Bị Cướp Kiệt Tác, Tôi Tạo Đỉnh Đồng Đạt Kỷ Lục",
            "author": "Đặng Văn Lâm",
            "num_chapters": 10,
            "setting": "Bắc Ninh, làng đúc đồng Đại Bái, Bảo tàng Lịch sử Quốc gia",
            "male_lead": "Đặng Văn Lâm, nghệ nhân đúc đồng nghệ thuật dát vàng 24K bị vu oan ăn cắp đồng nguyên liệu",
            "female_lead": "Ngô Thị Hương, Phó Giám đốc Bảo tàng Lịch sử Quốc gia, chuyên gia cổ vật",
            "conflict": "Học trò tráo đồng tạp chứa chì vào đỉnh thờ cúng của nhà nước, vu oan cho nghệ nhân đúc đồng gốc phá hoại bảo vật",
            "cover_desc": "Vietnamese bronze caster examining a glowing gold and bronze incense burner, elegant female museum curator beside him, sparkling molten copper sparks in background",
            "genre_visual": "traditional metal craft drama"
        },
        {
            "idx": 85,
            "title": "Vua Gà Đồi Yên Thế: Bị Đầu Độc Trang Trại, Tôi Xây Chuỗi Thực Phẩm Sạch Triệu Đô",
            "author": "Hoàng Thế Anh",
            "num_chapters": 10,
            "setting": "Bắc Giang, Yên Thế, Sở Nông nghiệp và Phát triển nông thôn, chi nhánh Agribank",
            "male_lead": "Hoàng Thế Anh, kỹ sư chăn nuôi lai tạo giống gà đồi thảo dược kháng kháng sinh bị hại",
            "female_lead": "Lê Mai Chi, Chuyên gia dịch tễ học thú y thuộc Viện Chăn nuôi Quốc gia",
            "conflict": "Đối thủ cạnh tranh thả virus cúm gia cầm độc lực cao vào trang trại 2 vạn con gà thịt dự kiến xuất siêu thị nhằm triệt hạ tài chính",
            "cover_desc": "Vietnamese poultry farmer holding a healthy golden chicken in hill farm, beautiful female veterinarian examining samples, verdant green hills of Yen The",
            "genre_visual": "poultry farming empire"
        },
        {
            "idx": 86,
            "title": "Bậc Thầy Nấm Mối Đen Tây Ninh: Chàng Nông Dân Quèn Lật Kèo Tập Đoàn Ngoại",
            "author": "Phùng Xuân Đông",
            "num_chapters": 10,
            "setting": "Tây Ninh, trang trại nấm mối công nghệ sinh học, Cục Trồng trọt",
            "male_lead": "Phùng Xuân Đông, kỹ sư lai tạo phôi nấm mối đen hữu cơ siêu năng suất bị đuổi đi",
            "female_lead": "Trần Thanh Mai, Giám đốc thu mua chuỗi siêu thị organic lớn nhất Đông Nam Á",
            "conflict": "Tập đoàn nông nghiệp ngoại bang ăn cắp phôi nấm, đăng ký bản quyền tại Singapore, gài bẫy nam chính vi phạm luật sở hữu trí tuệ",
            "cover_desc": "Vietnamese agricultural scientist in high-tech mushroom dark room inspecting organic black mushrooms, beautiful female supermarket buyer beside him, dramatic cool lighting",
            "genre_visual": "high-tech mushroom farming"
        },
        {
            "idx": 87,
            "title": "Vua Long Nhãn Hưng Yên: Bị Đốt Lò Sấy, Tôi Xuất Khẩu Long Nhãn Sang Mỹ",
            "author": "Tống Khánh Duy",
            "num_chapters": 9,
            "setting": "Hưng Yên, làng nghề long nhãn Khoái Châu, Cục An toàn thực phẩm",
            "male_lead": "Tống Khánh Duy, nghệ nhân sấy nhãn bằng hơi nước không lưu huỳnh bị cướp xưởng sấy",
            "female_lead": "Lâm Vy Anh, Thạc sĩ khoa học thực phẩm Đại học California, chuyên gia FDA",
            "conflict": "Thương lái lớn tráo nhãn tẩm lưu huỳnh độc hại vào lô hàng xuất khẩu sang Mỹ của nam chính nhằm bôi nhọ chất lượng",
            "cover_desc": "Vietnamese artisan examining glowing golden dried longan, beautiful female food scientist beside him, sunny traditional longan drying yard, old quarter architecture",
            "genre_visual": "traditional dried fruit trade"
        },
        {
            "idx": 88,
            "title": "Vua Quế Trà Bồng: Chàng Kỹ Sư Quèn Vực Dậy Mạch Sống Núi Rừng",
            "author": "Bùi Thế Vinh",
            "num_chapters": 10,
            "setting": "Quảng Ngãi, Trà Bồng, vùng quế organic xuất khẩu, Hiệp hội Gia vị Thế giới",
            "male_lead": "Bùi Thế Vinh, kỹ sư lâm nghiệp phục tráng giống quế cổ thụ chứa hàm lượng tinh dầu 6%",
            "female_lead": "Phạm Quỳnh Chi, chuyên gia đàm phán thương mại quốc tế SpiceTrade London",
            "conflict": "Doanh nghiệp đầu nậu cạo sạch vỏ rừng quế non, ép giá thu mua đất rừng quế của đồng bào Cor để khai thác quặng đất hiếm",
            "cover_desc": "Vietnamese forester stripping fragrant cinnamon bark in a high canopy cinnamon forest, elegant female trade negotiator beside him, sunrays cutting through misty trees",
            "genre_visual": "spices agroforestry empire"
        },
        {
            "idx": 89,
            "title": "Chúa Tể Ngọc Trai Đen Nha Trang: Chàng Thợ Lặn Quèn Lật Kèo Trùm Đá Quý",
            "author": "Cao Thiên Lạc",
            "num_chapters": 10,
            "setting": "Khánh Hòa, Nha Trang, vịnh Vân Phong, Viện Hải dương học Nha Trang",
            "male_lead": "Cao Thiên Lạc, thợ lặn cấy nhân ngọc trai biển sâu bị vu khống đánh tráo cổ vật biển",
            "female_lead": "Đặng Thu Thảo, Phó Viện trưởng Viện Hải dương học, chuyên gia sinh học biển",
            "conflict": "Trùm đá quý cấu kết cán bộ thoái hóa tráo ngọc trai nhuộm hóa chất độc hại vào khu bảo tồn biển vân phong để bôi nhọ dự án",
            "cover_desc": "Vietnamese diver holding open pearl shell showing a giant shimmering black pearl on boat, beautiful female marine biologist beside him, deep blue ocean water",
            "genre_visual": "marine aquaculture drama"
        },
        {
            "idx": 90,
            "title": "Bậc Thầy Chè Đắng Thạch An: Bị Vu Oan Đầu Độc, Tôi Dựng Lại Danh Tiếng Trà Việt",
            "author": "Lê Khắc Nam",
            "num_chapters": 9,
            "setting": "Cao Bằng, vùng nguyên liệu trà Thạch An, Cục Quản lý thị trường",
            "male_lead": "Lê Khắc Nam, chuyên gia sấy trà shan tuyết cổ thụ bị vu oan chè chứa dư lượng thuốc diệt cỏ",
            "female_lead": "Hoàng Bảo Trâm, Giám đốc kiểm định chất lượng SGS Việt Nam",
            "conflict": "Hãng trà đối thủ thuê gián điệp phun thuốc trừ sâu vào kho trà thành phẩm chuẩn bị xuất khẩu Thụy Sĩ nhằm tạo scandal quốc tế",
            "cover_desc": "Vietnamese master tea maker sifting tea leaves on bamboo basket, elegant female inspector holding certification folder, pristine mountain background",
            "genre_visual": "premium tea trade drama"
        },
        {
            "idx": 91,
            "title": "Vua Muối Sa Độc Địa Hải Phòng: Chàng Kỹ Sư Quèn Vực Dậy Cánh Đồng Trắng",
            "author": "Trần Thế Hải",
            "num_chapters": 10,
            "setting": "Hải Phòng, đồng muối Bạch Long, Cát Hải, Cục Hàng hải Việt Nam",
            "male_lead": "Trần Thế Hải, kỹ sư phát triển công nghệ muối kết tinh trên bạt HDPE đạt độ sạch 99.8%",
            "female_lead": "Vũ Phương Trinh, chuyên gia phân tích chất lượng thực phẩm xuất khẩu sang EU",
            "conflict": "Chủ đầu tư khu đô thị đổ phế thải xây dựng xả thẳng ra kênh dẫn nước đồng muối để ép di dời toàn bộ di dân Bạch Long",
            "cover_desc": "Vietnamese engineer standing on white salt pyramid in a high-tech salt field, beautiful female scientist inspecting water salinity, stormy ocean at horizon",
            "genre_visual": "industrial salt production"
        },
        {
            "idx": 92,
            "title": "Chúa Tể Nho Ninh Thuận: Bị Đầu Độc Hầm Ủ, Tôi Xây Đế Chế Rượu Vang Tỷ Đô",
            "author": "Nguyễn Tấn Đạt",
            "num_chapters": 11,
            "setting": "Ninh Thuận, thung lũng nho Phan Rang, Sở Khoa học và Công nghệ, giải Asia Wine Trophy",
            "male_lead": "Nguyễn Tấn Đạt, chuyên gia lên men vang nho Cabernet Sauvignon nhiệt đới bị đối thủ hãm hại",
            "female_lead": "Nguyễn Hoàng Mai Chi, Trưởng Đại diện Thương mại Việt Nam tại Liên minh Châu Âu (EU)",
            "conflict": "Đối thủ cạnh tranh thả vi khuẩn axetic vào toàn bộ 50 thùng gỗ sồi ủ rượu vang chuẩn bị dự thi quốc tế nhằm phá hoại men rượu",
            "cover_desc": "Vietnamese winemaker examining rich dark red wine in crystal glass in a wooden barrel cellar, elegant female diplomat beside him, warm candlelight glow",
            "genre_visual": "tropical winery empire"
        },
        {
            "idx": 93,
            "title": "Thần Y Thuốc Nam Nam Đàn: Chàng Trai Quèn Vực Dậy Mạch Thuốc Dân Tộc",
            "author": "Phạm Tuấn Anh",
            "num_chapters": 10,
            "setting": "Nghệ An, Nam Đàn, khu bảo tồn dược liệu quý, Bộ Y tế",
            "male_lead": "Phạm Tuấn Anh, lương y phục dựng bài thuốc nam trị dạ dày từ cây chè dây rừng sâu",
            "female_lead": "Đỗ Thục Đoan, Phó Giám đốc Trung tâm Kiểm nghiệm Thuốc Trung ương",
            "conflict": "Tập đoàn dược ngoại nhập lậu cao dược liệu rác từ Trung Quốc, đóng nhãn mác nam dược Nam Đàn để đầu độc bệnh nhân nhằm đổ oan",
            "cover_desc": "Vietnamese traditional herbalist sorting green medicinal herbs on a drying tray, beautiful female doctor looking on, traditional wooden house interior",
            "genre_visual": "medical corporate drama"
        },
        {
            "idx": 94,
            "title": "Vua Xoài Cát Hòa Lộc: Bị Ép Giá Cướp Vườn, Tôi Xây Chuỗi Logistics Trái Cây Toàn Cầu",
            "author": "Hoàng Việt",
            "num_chapters": 10,
            "setting": "Tiền Giang, Cái Bè, hợp tác xã xoài cát Hòa Lộc, cảng hàng không Tân Sơn Nhất",
            "male_lead": "Hoàng Việt, kỹ sư nông nghiệp thiết lập quy trình bao trái xoài xuất khẩu chống ruồi vàng",
            "female_lead": "Trịnh Khánh Quỳnh, Giám đốc chuỗi cung ứng hàng không lạnh CargoVina",
            "conflict": "Gã đầu nậu thu mua liên kết với hãng vận tải tăng cước đột biến 300% và giam hàng ở kho nóng để làm thối rữa toàn bộ lô xoài cát xuất khẩu",
            "cover_desc": "Vietnamese agriculturalist holding large yellow mangoes under tree, elegant female logistics director beside him, modern cargo aircraft taking off in background",
            "genre_visual": "fruit trade logistics war"
        },
        {
            "idx": 95,
            "title": "Thợ Đúc Đồng Ngũ Xã: Bị Cướp Tác Phẩm Quốc Gia, Tôi Dát Vàng Lên Số Phận",
            "author": "Nguyễn Đức Trí",
            "num_chapters": 10,
            "setting": "Hà Nội, Ngũ Xã, Ba Đình, Hội Mỹ thuật Việt Nam, Sở Văn hóa và Thể thao",
            "male_lead": "Nguyễn Đức Trí, nghệ nhân đúc tượng đồng rỗng nguyên khối cực mỏng bị tráo sản phẩm",
            "female_lead": "Phạm Nhã Phương, Giáo sư khảo cổ học và phục chế kim loại, Đại học Quốc gia Hà Nội",
            "conflict": "Đối thủ tráo tượng đồng rỗng đúc bằng kim loại tạp chất độc hại chì-cadmium dâng lên đền thờ di sản quốc gia nhằm khép nam chính vào tội xúc phạm tâm linh",
            "cover_desc": "Vietnamese copper caster hammering detailed patterns on a large bronze sculpture, beautiful female archaeologist holding ancient artifact, glowing gold sparks surrounding them",
            "genre_visual": "heritage art craftsmanship"
        },
        {
            "idx": 96,
            "title": "Vua Hạt Sen Tịnh Tâm Huế: Chàng Trai Quèn Vực Dậy Đặc Sản Tiến Vua",
            "author": "Trịnh Gia Huy",
            "num_chapters": 10,
            "setting": "Huế, hồ Tịnh Tâm, Kinh thành Huế, Cục Vệ sinh An toàn Thực phẩm",
            "male_lead": "Trịnh Gia Huy, nghệ nhân phục tráng sen trắng cổ hồ Tịnh Tâm hạt to bùi dẻo đặc trưng",
            "female_lead": "Lê Cát Tiên, Thạc sĩ dinh dưỡng học tốt nghiệp Đại học Tokyo, CEO chuỗi thực phẩm thực dưỡng",
            "conflict": "Đối thủ cạnh tranh thả ốc bươu vàng phá hoại toàn bộ diện tích sen trắng cổ, pha trộn sen hồ thường ngâm chất tẩy trắng độc hại",
            "cover_desc": "Vietnamese young farmer holding lotus seed pods on a boat, elegant female executive beside him, ancient architecture of Hue Imperial Citadel in misty background",
            "genre_visual": "royal culinary heritage"
        },
        {
            "idx": 97,
            "title": "Nữ Hoàng Trà San Tuyết Hà Giang: Bị Đuổi Khỏi Bản, Tôi Xây Chuỗi Trà Di Sản Triệu Đô",
            "author": "Lê Cát Tiên",
            "num_chapters": 10,
            "setting": "Hà Giang, Hoàng Su Phì, rừng trà cổ thụ đồi chè Tây Côn Lĩnh, Sở Công Thương",
            "male_lead": "Đặng Thái Sơn, chuyên gia chế biến trà sấy lạnh shan tuyết bằng năng lượng mặt trời",
            "female_lead": "Lê Cát Tiên, con gái vua trà bị anh họ đuổi khỏi hợp tác xã gia tộc",
            "conflict": "Anh họ bán rẻ danh tiếng hợp tác xã bằng việc nhập trà cám hóa chất rẻ tiền gán mác Shan Tuyết cổ thụ, vu khống em gái đầu độc khách",
            "cover_desc": "Beautiful Vietnamese female tea entrepreneur standing in front of giant ancient tea trees in high misty mountains of Ha Giang, male tea master beside her",
            "genre_visual": "highlands tea empire drama"
        },
        {
            "idx": 98,
            "title": "Vua Muối Hột Bến Tre: Chàng Trai Quèn Vực Dậy Di Sản Dưới Cát",
            "author": "Nguyễn Hoàng Minh",
            "num_chapters": 9,
            "setting": "Bến Tre, Ba Tri, ruộng muối truyền thống, Bộ Văn hóa, Thể thao và Du lịch",
            "male_lead": "Nguyễn Hoàng Minh, di dân giữ nghề muối hột Bến Tre làm sạch bằng nước biển tầng sâu",
            "female_lead": "Vũ Khánh An, Giám đốc trung tâm xúc tiến văn hóa ẩm thực Nam Bộ",
            "conflict": "Tập đoàn hóa chất thải nước nhiễm dầu ra biển Ba Tri, làm ô nhiễm ruộng muối nhằm cưỡng chế thu hồi đất ruộng xây khu xử lý rác",
            "cover_desc": "Vietnamese salt worker carrying bamboo baskets of salt hột under brilliant sky, beautiful female cultural official beside him, scenic salt fields at sunset",
            "genre_visual": "coastal community heritage"
        },
        {
            "idx": 99,
            "title": "Chúa Tể Dừa Sáp Trà Vinh: Chàng Rể Quèn Thâu Tóm Đế Chế Nông Sản Tỷ Đô",
            "author": "Lê Gia Bách",
            "num_chapters": 11,
            "setting": "Trà Vinh, Cầu Kè, Sở Nông nghiệp và Phát triển Nông thôn, chi nhánh Agribank",
            "male_lead": "Lê Gia Bách, chuyên gia cấy phôi giống dừa sáp tỷ lệ sáp 85% bị gia đình vợ khinh rẻ đuổi đi",
            "female_lead": "Trần Ngọc Diệp, Phó Giám đốc thẩm định công nghệ cao Sở NN&PTNT",
            "conflict": "Anh vợ tráo giống dừa thường vào lô giống dừa sáp cấy phôi xuất khẩu Singapore để hủy hoại danh tiếng, chiếm đoạt phòng thí nghiệm",
            "cover_desc": "Vietnamese coconut scientist examining a split coconut showing thick white waxy flesh, beautiful female government official beside him, tropical coconut plantation",
            "genre_visual": "coconut farming high-tech"
        },
        {
            "idx": 100,
            "title": "Vua Quế Văn Yên: Kỹ Sư Quèn Vực Dậy Mạch Hương Vàng Tây Bắc",
            "author": "Nguyễn Hải Long",
            "num_chapters": 10,
            "setting": "Yên Bái, Văn Yên, vùng rừng quế xuất khẩu organic, Cục Xúc tiến Thương mại",
            "male_lead": "Nguyễn Hải Long, kỹ sư chưng cất tinh dầu quế organic không lẫn tạp chất hóa học bị cướp xưởng",
            "female_lead": "Đặng Thục Đoan, Chuyên viên cao cấp Cục Xúc tiến Thương mại, Bộ Công Thương",
            "conflict": "Trùm thu mua quế pha trộn vỏ quế cạo lẫn keo hóa học độc hại để tăng trọng lượng xuất khẩu, vu khống hãng nam chính làm giả xuất xứ",
            "cover_desc": "Vietnamese engineer stripping fragrant red-brown cinnamon bark in a dense forest, elegant female trade official holding standard guidelines documents, dramatic sunrays",
            "genre_visual": "forestry cinnamon spice empire"
        }
    ]
    
    concepts.extend(extra_concepts)
    
    # Write to novel_concepts_100.json in scratch/exported_100_novels/
    output_path = "scratch/exported_100_novels/novel_concepts_100.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(concepts, f, ensure_ascii=False, indent=2)
        
    print(f"✓ Expanded pool successfully! Total concepts: {len(concepts)}")
    print(f"✓ Saved to {output_path}")

if __name__ == "__main__":
    run()
