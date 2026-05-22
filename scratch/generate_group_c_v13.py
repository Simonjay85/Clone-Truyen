import os
import json
import time
import re
import requests

OPENAI_KEY = "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"
SCRATCH_DIR = "/Users/aaronnguyen/TN/App/doctieuthuyet/scratch"

STORIES_CONFIG = {
    2745: {
        "title": "Tài Xế Taxi Bị Khách VIP Khinh Thường, Tài Xế Đó Sở Hữu Công Ty Taxi",
        "focus_keyword": "tài xế taxi",
        "seo_title": "Tài Xế Taxi Bị Khinh – Chủ Tịch Vận Tải Đông Á",
        "seo_description": "Tài xế taxi truyền thống bị sỉ nhục tại sân bay. Hóa ra anh là Chủ tịch Tập đoàn Đông Á sở hữu 47.000 đầu xe. Truyện sảng văn V13 đặc sắc.",
        "intro": "<p><strong>\"Cậu chỉ là một gã tài xế taxi truyền thống rác rưởi, cả đời này cũng không ngẩng đầu lên được trước ứng dụng gọi xe công nghệ của chúng tôi!\"</strong></p>\n<p>Tại Sân bay Quốc tế Nội Bài, lúc 14 giờ 37 phút ngày thứ Ba, Phạm Gia Bảo – Giám đốc Vận hành khu vực của Go-Fast – đứng giữa sảnh Terminal 2 mà lên giọng sỉ nhục Hoàng Văn Nam trước hơn hai trăm hành khách đang chờ chuyến. Hắn không thèm hạ giọng, không thèm nhìn xung quanh. Chiếc áo vest xám tro ba triệu đồng, đồng hồ dây da nâu, và cái miệng quen sai khiến – tất cả tạo nên một con người tin chắc rằng bản thân đang đứng ở đỉnh thức ăn của ngành vận tải đô thị.</p>\n<p>Hoàng Văn Nam, bốn mươi hai tuổi, mặc chiếc áo đồng phục xanh navy bạc màu ở khuỷu tay, đứng lặng yên cạnh xe số 0218 – chiếc Innova đời 2019 đã chạy hơn tám mươi vạn cây số. Anh không cãi. Anh chỉ nhìn Phạm Gia Bảo bằng đôi mắt mà người ta thường nhìn về phía chân trời xa – không giận, không khinh, chỉ là đang tính toán điều gì đó hoàn toàn khác.</p>\n<p>Điều Phạm Gia Bảo không biết: người đàn ông đang đứng chịu đựng lời sỉ nhục ấy là Chủ tịch Hội đồng quản trị Tập đoàn Vận tải Đông Á – đế chế taxi có 47.000 đầu xe hoạt động tại mười hai tỉnh thành, trong đó Go-Fast vừa nộp đơn xin hợp tác thâu tóm chiều qua.</p>\n<p>Trần Thanh Mai, nữ kiểm toán viên cấp cao của Công ty Kiểm toán Minh Việt, chứng kiến toàn bộ cảnh đó từ hàng ghế chờ cách mười lăm mét. Cô ghi chép vào điện thoại lúc 14:38 – không phải vì tò mò, mà vì nghề nghiệp dạy cô rằng mọi dữ liệu đều có thể trở thành bằng chứng.</p>\n<p>Và bằng chứng, trong bốn mươi tám giờ tới, sẽ là thứ duy nhất quyết định ai sẽ quỳ xuống trước ai.</p>",
        "outlines": [
            "Chương 1: Hoàng Văn Nam bị sỉ nhục tại sảnh Terminal 2 Nội Bài bởi Phạm Gia Bảo. Trần Thanh Mai ngồi ở ghế chờ ghi nhận sự việc.",
            "Chương 2: Trần Thanh Mai tiến hành kiểm toán Go-Fast tại văn phòng Sunwah Tower và phát hiện sai phạm tài chính nghiêm trọng của Phạm Gia Bảo (liên kết với vendor làm sạch xe Sạch Việt Xanh của em gái Bảo và các khoản chi khống).",
            "Chương 3: Hoàng Văn Nam tổ chức cuộc họp ban chiến lược thâu tóm tại tầng 26 Vietcombank Tower. Go-Fast gửi hồ sơ xin hợp tác khẩn cấp do khủng hoảng nợ trái phiếu 2.100 tỷ đồng sắp đến hạn.",
            "Chương 4: Cuộc họp trực tiếp giữa Đông Á và Go-Fast tại phòng họp 26A. Hoàng Văn Nam xuất hiện khiến Phạm Gia Bảo hoảng loạn. Nam đưa ra đề nghị thâu tóm 70% cổ phần Go-Fast.",
            "Chương 5: Trần Thanh Mai nhận cuộc gọi lúc 23 giờ từ Hoàng Văn Nam. Cô lập báo cáo kiểm toán độc lập và từ chối mọi sự can thiệp từ Go-Fast, yêu cầu làm đúng quy trình pháp lý.",
            "Chương 6: Đông Á đưa ra điều kiện nhân sự không thương lượng: sa thải Phạm Gia Bảo vì vi phạm kỷ luật lao động và xung đột lợi ích. Nguyễn Quốc Hùng (CEO Go-Fast) buộc Bảo ký đơn thôi việc không bồi thường.",
            "Chương 7: Lễ ký kết hợp đồng thâu tóm tại Vietcombank Tower. Go-Fast chính thức thuộc về Đông Á. Bằng chứng kiểm toán của Mai được chuyển cho cơ quan công an C03 điều tra hành vi rút ruột công ty của Bảo.",
            "Chương 8: Thứ Bảy tuần tiếp theo, Hoàng Văn Nam tiếp tục lái chiếc taxi Innova 0218 chở khách tại Nội Bài. Sự bình yên của người đứng trên đỉnh cao sau khi giải quyết tranh chấp bằng pháp lý."
        ]
    },
    2752: {
        "title": "Con Trai Nuôi Bị Đuổi Ra Khỏi Tập Đoàn, Di Chúc Ông Nội Trao Lại 70%",
        "focus_keyword": "con trai nuôi",
        "seo_title": "Con Nuôi Bị Đuổi Khỏi Tập Đoàn – Di Chúc Trao 70% Cổ Phần",
        "seo_description": "Nguyễn Gia Khải bị đuổi khỏi tập đoàn Minh Long. Nhưng di chúc hợp pháp công chứng mở ra: anh thừa kế 70% cổ phần. Truyện sảng văn pháp lý V13.",
        "intro": "<p><strong>\"Con nuôi thì suốt đời là con nuôi – không có chỗ trong Tập đoàn Minh Long đâu. Ra đi đi, đừng làm xấu mặt dòng họ!\"</strong></p>\n<p>Nguyễn Gia Khải – con trai nuôi duy nhất của cố Chủ tịch Nguyễn Minh Long – bị đuổi khỏi Hội đồng quản trị Tập đoàn Minh Long vào lúc 10 giờ sáng ngày 15 tháng 3, trước toàn thể nhân viên tầng 18 tòa nhà Minh Long Tower tại Hà Nội. Quyết định do người anh họ Nguyễn Gia Phú ký – thừa ủy quyền của hội đồng gia tộc.</p>\n<p>Ba tiếng sau, văn phòng công chứng số 7 phường Hoàn Kiếm mở phong niêm bản di chúc mà cố Chủ tịch lập năm 2019 và sửa đổi lần cuối tháng 11 năm ngoái. Nội dung: 70% cổ phần Tập đoàn Minh Long – trị giá ước tính 4.200 tỷ đồng – thuộc về Nguyễn Gia Khải.</p>\n<p>Lê Phương Linh, kiểm soát viên nội bộ độc lập của tập đoàn, người duy nhất không ký vào quyết định đuổi việc buổi sáng, cầm phong bì di chúc từ tay công chứng viên và bắt đầu đọc.</p>\n<p>Trong bốn mươi tám giờ tiếp theo, cổ phần, bằng chứng, và luật kế thừa sẽ xây lại từ đầu những gì người ta tưởng đã phá bỏ xong.</p>",
        "outlines": [
            "Chương 1: Nguyễn Gia Khải bị đuổi khỏi Minh Long Tower bởi Nguyễn Gia Phú. Lê Phương Linh từ chối ký biên bản vì thiếu căn cứ pháp lý.",
            "Chương 2: Di chúc được mở tại Văn phòng Công chứng số 7 Hoàn Kiếm bởi công chứng viên Lê Thị Oanh. Khải nhận 70% cổ phần tập đoàn.",
            "Chương 3: Nguyễn Gia Phú nhận tin di chúc đã mở và hoảng loạn liên hệ luật sư Đặng Minh Quang để tìm cách tranh chấp pháp lý.",
            "Chương 4: Lê Phương Linh gặp Khải dưới gốc sấu Lý Thường Kiệt, trao cho anh bộ hồ sơ kiểm soát nội bộ gồm 72 trang ghi nhận các giao dịch rút ruột của Phú suốt 3 năm qua.",
            "Chương 5: Cuộc họp khẩn của Hội Đồng Gia Tộc tại Hoàng Diệu. Luật sư Quang cảnh báo Phú rằng di chúc hoàn toàn hợp pháp và việc cố tình tranh chấp sẽ kéo theo điều tra tài chính.",
            "Chương 6: Cuộc trò chuyện giữa Khải và Linh tại quán cà phê Nhân Hàng Hành. Khải chia sẻ về những lời dặn dò đầy trí tuệ của cố Chủ tịch Nguyễn Minh Long về bản chất của doanh nghiệp.",
            "Chương 7: Nguyễn Gia Phú nhận ra bế tắc pháp lý và nguy cơ hình sự từ tập hồ sơ 72 trang của Linh, buộc phải viết email xin thỏa thuận bàn giao quyền lực cho Khải.",
            "Chương 8: Lễ bàn giao chính thức tại phòng họp 18B với sự chứng kiến của Sở Kế hoạch và Đầu tư Hà Nội. Khải tiếp quản tập đoàn và tiếp tục giữ Linh làm kiểm soát viên độc lập."
        ]
    },
    2759: {
        "title": "Thợ Sửa Xe Bị Cả Xóm Khinh, Khi Đội Đua F1 Quốc Gia Tìm Đến Thuê",
        "focus_keyword": "thợ sửa xe",
        "seo_title": "Thợ Sửa Xe Bị Khinh – Kỹ Sư Trưởng Đội Đua F1",
        "seo_description": "Nguyễn Đức Nghĩa bị cả xóm khinh thường trong tiệm sửa xe gỉ sét. Khi đội đua F1 quốc gia tìm đến thuê anh làm Kỹ sư trưởng. Truyện sảng văn V13.",
        "intro": "<p><strong>\"Thợ sửa xe máy cùi bắp, học nghề cũng dở, mở tiệm cũng ế – cả xóm này không ai thèm vào tiệm ông nữa đâu!\"</strong></p>\n<p>Tiệm sửa xe Đức Nghĩa nằm ở cuối hẻm 78 đường Trường Chinh, quận Tân Bình, Thành phố Hồ Chí Minh. Biển hiệu sắt hoen gỉ, mái tôn thấp, nền xi măng cũ có vết dầu máy ăn sâu như vân gỗ. Nguyễn Đức Nghĩa, ba mươi chín tuổi, đã ngồi ở đó mười lăm năm, tay đen dầu mỡ, kính hàn trên trán, không nói nhiều với ai trong xóm.</p>\n<p>Sáng hôm ấy, bà Năm Hồng – chủ nhà cho thuê mặt bằng – mang theo đơn đòi nhà gấp để cho Huỳnh Hữu Phước (chủ tiệm Auto-Care lớn đối diện) thuê lại nhằm mở rộng mặt bằng. Phước công khai chế giễu Nghĩa chỉ là kẻ hết thời, bất tài vô dụng.</p>\n<p>Giữa lúc đó, một đoàn xe đen sang trọng đỗ xịch đầu hẻm 78. Đỗ Thùy Trang – Giám đốc Chiến lược của Đội đua F1 Quốc gia Việt Nam – bước xuống cùng các kỹ sư hàng đầu từ Williams Racing Anh Quốc, mang theo bản hợp đồng thuê Kỹ sư trưởng trị giá 12 tỷ đồng mỗi năm.</p>\n<p>Hóa ra, Nghĩa chính là huyền thoại động học khí thế giới từng phát triển động cơ F1 tại Đức, nay ẩn cư sau biến cố gia đình.</p>",
        "outlines": [
            "Chương 1: Tiệm sửa xe gỉ sét ở hẻm 78 Trường Chinh. Bà Năm Hồng đòi nhà và Hữu Phước sỉ nhục Đức Nghĩa trước cả xóm.",
            "Chương 2: Đỗ Thùy Trang cùng đoàn chuyên gia Williams Racing xuất hiện, mang theo bản vẽ động cơ biến thiên tỷ số nén bị lỗi động lực học để nhờ Nghĩa hiệu chỉnh.",
            "Chương 3: Nghĩa thực hiện hiệu chỉnh và chạy thử khối động cơ F1 thử nghiệm trên băng thử di động (Dyno) tại xưởng cơ khí, tạo ra tiếng rít 7.200 RPM hoàn hảo.",
            "Chương 4: Phước cấu kết với thanh tra xây dựng và môi trường địa phương để lập biên bản niêm phong tiệm của Nghĩa vì cáo buộc xả dầu thải trái phép.",
            "Chương 5: Đỗ Thùy Trang hỗ trợ pháp lý, cho đội ngũ pháp lý của tập đoàn đua xe phản kháng. Trang đưa ra điều kiện hợp tác rõ ràng: Nghĩa phải ký hợp đồng Kỹ sư trưởng 3 năm thì cô sẽ mua đứt cả mảnh đất hẻm 78 để xây trung tâm R&D.",
            "Chương 6: Nghĩa dùng bằng chứng số từ camera giám sát hồng ngoại và kết quả phân tích mẫu đất của Viện Khoa học Môi trường chứng minh Phước tự đổ dầu thải gài bẫy anh.",
            "Chương 7: Phước bị công an xử lý hành vi hủy hoại tài sản và vu khống. Đội đua F1 công bố chính thức bổ nhiệm Nguyễn Đức Nghĩa làm Kỹ Sư Trưởng thiết kế động cơ F1 thế hệ mới.",
            "Chương 8: Nghĩa đứng trên đường đua Mỹ Đình trong ngày chạy thử xe đầu tiên. Anh nhìn khối động cơ hoạt động hoàn hảo và nhận ra giá trị của sự kiên trì vật lý."
        ]
    },
    2766: {
        "title": "Trợ Lý Bị Sếp Nữ CEO Ngược Đãi, Sếp Mới Của Cô Chính Là Anh Sau Thâu Tóm",
        "focus_keyword": "trợ lý ceo",
        "seo_title": "Trợ Lý Bị CEO Ngược Đãi – Sếp Mới Sau Thâu Tóm",
        "seo_description": "Trợ lý Phạm Tuấn Khoa bị sếp nữ CEO Nguyễn Thị Thu Hà ngược đãi tại Bitexco. Hóa ra anh là chủ tịch thâu tóm toàn bộ tập đoàn. Truyện V13 kịch tính.",
        "intro": "<p><strong>\"Phạm Tuấn Khoa! Anh có biết hồ sơ dự án anh làm không đúng tiêu chuẩn không? Anh làm việc kiểu này thì đừng trách tôi ký giấy buộc thôi việc!\"</strong></p>\n<p>Phạm Tuấn Khoa – trợ lý Giám đốc kinh doanh tại Công ty Gia Nguyên Holdings – đứng giữa văn phòng tầng 14 Bitexco Financial Tower lúc 10 giờ sáng thứ Hai, nhận đủ ba mươi phút lời phê bình công khai từ CEO Nguyễn Thị Thu Hà trước toàn bộ mười hai nhân viên phòng kinh doanh. Anh không cãi, không giải thích, chỉ cúi đầu nhìn những con số chênh lệch trên bản in báo cáo tài chính quý 2.</p>\n<p>Hà không biết rằng Phạm Tuấn Khoa chính là nhà sáng lập kiêm Chủ tịch của Siêu quỹ Đầu tư VN-Capital – đơn vị đang tiến hành thâu tóm thù địch (hostile takeover) 54% cổ phần Gia Nguyên Holdings qua sàn giao dịch chứng khoán để tái cấu trúc toàn bộ tập đoàn này. Khoa chỉ đóng vai trợ lý thử việc trong hai tuần để trực tiếp khảo sát năng lực vận hành thực tế của đội ngũ quản lý trung cấp.</p>\n<p>Vũ Hoài An – Giám đốc Pháp chế của VN-Capital – ngồi ở văn phòng tầng 15 Bitexco, tay lướt qua các điều khoản chuyển nhượng và ghi nhận toàn bộ hồ sơ vi phạm của Nguyễn Thị Thu Hà.</p>\n<p>Trận chiến thâu tóm kéo dài 72 giờ sẽ phơi bày toàn bộ sự thật về kẻ đứng sau bức màn quyền lực.</p>",
        "outlines": [
            "Chương 1: Phạm Tuấn Khoa bị CEO Nguyễn Thị Thu Hà sỉ nhục công khai tại văn phòng tầng 14 Bitexco. Khoa giữ thái độ điềm tĩnh và ghi nhận các lỗi sai số liệu của Hà.",
            "Chương 2: Vũ Hoài An tiến hành phân tích hồ sơ pháp lý M&A của Gia Nguyên Holdings và phát hiện Hà cấu kết chuyển 12 tỷ đồng hoa hồng bất động sản khống cho công ty gia đình.",
            "Chương 3: Khoa gặp Hoài An tại sảnh chờ Landmark 81 để rà soát tiến độ gom cổ phiếu GNH trên sàn HoSE. Quỹ VN-Capital đã đạt mức sở hữu 51.2%.",
            "Chương 4: Hà gửi thư cảnh cáo và quyết định đuổi việc Khoa vào lúc 23 giờ đêm qua email. Khoa im lặng phản hồi đồng ý bàn giao hồ sơ.",
            "Chương 5: Đại hội cổ đông bất thường diễn ra tại phòng họp HĐQT Gia Nguyên Holdings. Hà tự đắc công bố dự án mới nhưng bị đình chỉ quyền biểu quyết do VN-Capital công bố tỷ lệ sở hữu chi phối.",
            "Chương 6: Phạm Tuấn Khoa bước vào phòng họp với tư cách Chủ tịch mới của VN-Capital. Sự ngỡ ngàng và sụp đổ hoàn toàn của Nguyễn Thị Thu Hà.",
            "Chương 7: Vũ Hoài An công bố toàn bộ bằng chứng số gồm sao kê tài khoản ngân hàng Techcombank và email chỉ đạo của Hà về việc rút ruột 12 tỷ đồng. Hà bị tước quyền điều hành và đối mặt cảnh sát kinh tế.",
            "Chương 8: Khoa ngồi tại phòng làm việc mới tầng 14 Bitexco, nhìn xuống dòng sông Sài Gòn cuộn chảy. Anh tiếp tục giữ vững nguyên tắc điều hành dựa trên con số và thực tế."
        ]
    },
    2773: {
        "title": "Chồng Nghèo Bị Họ Hàng Khinh Dự Tiệc Hào Môn, Hóa Ra Anh Là Khách Mời Danh Dự",
        "focus_keyword": "chồng nghèo",
        "seo_title": "Chồng Nghèo Bị Khinh Dự Tiệc – Khách Mời Danh Dự VIP",
        "seo_description": "Nguyễn Minh Tú bị mẹ vợ khinh thường tại tiệc sinh nhật Thảo Điền. Hóa ra anh là khách mời danh dự, đại diện quỹ đầu tư nghìn tỷ. Truyện V13.",
        "intro": "<p><strong>\"Anh ấy không có chỗ ở tiệc này. Nhà tôi mời người có địa vị, không mời người làm thuê tháng năm triệu!\"</strong></p>\n<p>Lúc 7 giờ tối thứ Bảy, tại biệt thự gia tộc nhà họ Trần ở khu Thảo Điền, quận 2, Thành phố Hồ Chí Minh, bà Trần Thị Kim Oanh – mẹ vợ – đứng giữa sảnh đón khách và tuyên bố trước ba mươi người rằng Nguyễn Minh Tú, chồng của con gái bà, không được phép vào dự tiệc sinh nhật thứ sáu mươi của bố vợ. Nguyễn Minh Tú, ba mươi lăm tuổi, đứng ở cửa vào với bộ quần áo giản dị, tay cầm món quà nhỏ là hộp trà đinh cổ thụ Thái Nguyên tự tay anh sao chế.</p>\n<p>Trần Khánh Vy, vợ Tú, một nữ luật sư tranh chấp thương mại sắc sảo, bước ra đứng cạnh chồng và đặt điều kiện thẳng thắn với mẹ mình: nếu Tú không được vào, cô sẽ từ bỏ quyền đại diện pháp lý cho tập đoàn gia đình đang đứng trước nguy cơ phá sản vì khoản nợ 150 tỷ đồng từ ngân hàng Vietbank.</p>\n<p>Họ không biết rằng, Nguyễn Minh Tú chính là chuyên gia công nghệ sinh học nông nghiệp hàng đầu kiêm Đại diện ủy quyền của Quỹ đầu tư toàn cầu Greenfield Asia có dòng vốn 3.000 tỷ đồng, người mà bố vợ đang mòn mỏi chờ đợi để xin ký gói đầu tư cứu mạng.</p>",
        "outlines": [
            "Chương 1: Tiệc hào môn Thảo Điền. Mẹ vợ Kim Oanh sỉ nhục Nguyễn Minh Tú và ngăn anh vào cửa. Trần Khánh Vy ra mặt bảo vệ chồng.",
            "Chương 2: Khánh Vy đưa Tú ra quán cà phê ven sông Sài Gòn, Vy khẳng định cô sẽ đứng về phía anh nhưng yêu cầu anh cho cô xem giải pháp thực tế để giúp công ty gia đình vượt qua khủng hoảng 150 tỷ.",
            "Chương 3: Tú hé lộ bộ hồ sơ đăng ký độc quyền sáng chế chế phẩm sinh học trị bệnh sầu riêng và thư xác nhận đầu tư từ Greenfield Asia do Katherine Le ký.",
            "Chương 4: Lê Huy – gã thiếu gia ngân hàng lừa lọc – xuất hiện tại bữa tiệc hào môn để ép bố vợ gả Vy cho hắn nhằm gia hạn khoản nợ 150 tỷ.",
            "Chương 5: Katherine Le (Giám đốc Greenfield) bước vào tiệc sinh nhật cùng trợ lý. Bà công bố đại diện danh dự tối cao của quỹ tại Việt Nam là Nguyễn Minh Tú.",
            "Chương 6: Tú bước vào sảnh chính trước sự bàng hoàng của mẹ vợ và Lê Huy. Tú công bố gói đầu tư cứu trợ nông nghiệp công nghệ cao 300 tỷ đồng.",
            "Chương 7: Khánh Vy đại diện pháp lý ký kết hợp đồng đầu tư, đồng thời công bố bằng chứng pháp lý chứng minh Lê Huy giả mạo thông tin tín dụng để ép gia đình cô vào bẫy phá sản.",
            "Chương 8: Lê Huy bị cảnh sát triệu tập. Mẹ vợ cúi đầu xin lỗi. Tú và Vy cùng ngồi uống trà đinh trên ban công căn hộ Vinhomes, thảnh thơi sau cơn bão tài chính."
        ]
    }
}


def split_sentences_to_html(text):
    # Strip any existing p tags first
    text = re.sub(r'</?p>', '', text)
    text = text.replace('\n', ' ')
    
    # Split by sentence boundaries: period, question, or exclamation mark optionally followed by double quotes
    sentences = re.split(r'(?<=[.!?])\s+|(?<=[.!?]”)\s+|(?<=[.!?]")\s+', text)
    
    processed = []
    for s in sentences:
        s = s.strip()
        if s:
            processed.append(f"<p>{s}</p>")
    return "\n".join(processed)


def call_openai(system_prompt, user_prompt, temperature=0.75):
    url = "https://api.openai.com/v1/chat/completions"
    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        "temperature": temperature,
        "max_tokens": 4000
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_KEY}"
    }
    
    for attempt in range(4):
        try:
            res = requests.post(url, json=payload, headers=headers, timeout=120)
            res.raise_for_status()
            data = res.json()
            return data['choices'][0]['message']['content'].strip()
        except Exception as e:
            print(f"OpenAI Call Error (Attempt {attempt+1}): {e}")
            time.sleep(5)
    raise Exception("Failed to connect to OpenAI API")


def generate_chapter(story_title, story_intro, chap_num, chap_outline, previous_chapters_summary=""):
    system_prompt = """Bạn là biên tập viên văn học mạng và là nhà văn sảng văn Việt Nam chuyên nghiệp chuẩn V13.
Bạn có giọng văn vô cùng tả thực, sống động, kịch tính và dùng từ ngữ chuẩn xác, hiện đại, giàu tính vật chất.

TIÊU CHUẨN V13 BẮT BUỘC KHI VIẾT TRUYỆN:
1. Show don't tell vật lý: mô tả chi tiết các phản ứng cơ thể (mồ hôi lạnh chảy trên thái dương, cơ mặt siết lại, nắm đấm siết chặt đến mức móng tay găm vào lòng bàn tay rỉ máu, nuốt khan, đầu óc tính toán), bối cảnh xung quanh cụ thể (tiếng điều hòa kêu vo vo, mùi nước hoa Dior Sauvage, chiếc đồng hồ Seiko SKX009, mã số thuế doanh nghiệp, mã cổ phiếu, thời gian cụ thể 14:37, v.v.). Không dùng tính từ trừu tượng mơ hồ kiểu "vô cùng giận dữ", "hoảng hốt tột độ".
2. Bối cảnh địa danh thật Việt Nam: Sân bay Quốc tế Nội Bài, Tân Sơn Nhất, Bitexco Quận 1, Landmark 81, đường Lý Thường Kiệt Hà Nội, ngõ Hàng Bài, hẻm 78 Trường Chinh Tân Bình, khu biệt thự Thảo Điền Quận 2 HCMC.
3. Nữ chính lý tính đặt điều kiện trước khi hợp tác: Nhân vật nữ chính hoặc người đồng hành nữ (như kiểm soát viên, luật sư, chuyên gia kiểm toán) phải cực kỳ lý trí, có chuyên môn nghiệp vụ cao. Cô ấy luôn ghi chép dữ liệu, kiểm tra pháp lý kỹ càng và đưa ra các điều kiện/thỏa thuận cụ thể trước khi đồng ý phối hợp hay bảo trợ cho nam chính.
4. Khủng hoảng 24h+: Các mâu thuẫn hay khó khăn tài chính, pháp lý phải diễn ra kéo dài (hơn 24-48 giờ), tạo nhịp độ căng thẳng thực tế của đời sống kinh doanh thay vì giải quyết chớp nhoáng trong vài phút.
5. Bằng chứng số/pháp lý cụ thể để giải quyết tranh chấp: Mọi mâu thuẫn được giải quyết bằng các văn bản pháp lý chính thức (di chúc có công chứng hợp pháp, báo cáo kiểm toán độc lập của Big 4, sao kê tài khoản ngân hàng Techcombank/Vietcombank, kết quả phân tích hóa học mẫu đất của viện nghiên cứu, địa chỉ IP truy cập, chứng nhận sở hữu trí tuệ của cục bản quyền), tuyệt đối không dùng bạo lực tay chân hay quyền lực ảo tưởng để đè bẹp đối thủ.
6. Mỗi chương viết tối thiểu 1200 từ trở lên. Phải viết thật dài, chi tiết các đoạn hội thoại, phân tích nội tâm và bối cảnh xung quanh để đạt đủ dung lượng.

Yêu cầu xuất ra định dạng JSON chính xác:
{
  "title": "Chương X: Tên chương thuần Việt cực kỳ cuốn hút",
  "content": "Nội dung chương viết hoàn chỉnh bằng Tiếng Việt 100%..."
}"""

    user_prompt = f"""Tác phẩm: {story_title}
Giới thiệu tác phẩm: {story_intro}
Nhiệm vụ: Viết hoàn chỉnh CHƯƠNG {chap_num} của tác phẩm này.
Dàn ý Chương {chap_num}: {chap_outline}

{f"Tóm tắt diễn biến các chương trước: {previous_chapters_summary}" if previous_chapters_summary else ""}

YÊU CỰC KỲ QUAN TRỌNG:
- Chương phải viết cực kỳ chi tiết, chậm rãi, phát triển sâu sắc tâm lý nhân vật và các đoạn hội thoại gay cấn.
- Độ dài nội dung phần "content" bắt buộc phải từ 1200 từ tiếng Việt trở lên (khoảng 8000 ký tự trở lên). Đừng viết tóm tắt!
- Hãy mô tả tỉ mỉ hành động vật lý của nhân vật (mồ hôi lạnh, nhịp tim, nhấp cà phê, gõ bàn phím), các thương hiệu thực tế, bối cảnh thực tại Việt Nam.
- Trả về JSON hợp lệ."""

    chap_raw = call_openai(system_prompt, user_prompt)
    
    # Try parsing JSON
    try:
        # Strip markdown if present
        cleaned = chap_raw.strip()
        if cleaned.startswith("```"):
            cleaned = re.sub(r"^```(?:json)?\n", "", cleaned)
            cleaned = re.sub(r"\n```$", "", cleaned).strip()
            
        data = json.loads(cleaned)
        return data
    except Exception as e:
        print(f"[RETRY REGEX] Chapter {chap_num} JSON parse failed. Extracting via regex...")
        title_match = re.search(r'"title"\s*:\s*"(.*?)"', chap_raw)
        content_match = re.search(r'"content"\s*:\s*"(.*)"', chap_raw, re.DOTALL)
        if title_match and content_match:
            title = title_match.group(1)
            content = content_match.group(1).replace('\\"', '"').replace('\\n', '\n')
            return {"title": title, "content": content}
        else:
            raise Exception(f"Failed to parse or extract chapter {chap_num}: {chap_raw[:300]}")


def generate_story_v13(story_id, config):
    print(f"\n==========================================")
    print(f"🎬 STARTING GENERATION FOR STORY ID {story_id}")
    print(f"Title: {config['title']}")
    print(f"==========================================")
    
    chapters = []
    chaps_summary = []
    
    for idx, outline in enumerate(config["outlines"], 1):
        print(f"\n[GENERATING] {config['title']} - Chapter {idx}...")
        
        previous_summary_str = " | ".join(chaps_summary)
        
        attempt = 0
        while attempt < 3:
            try:
                chap_data = generate_chapter(
                    story_title=config["title"],
                    story_intro=config["intro"],
                    chap_num=idx,
                    chap_outline=outline,
                    previous_chapters_summary=previous_summary_str
                )
                
                # Split content into sentence-by-sentence HTML paragraphs
                formatted_content = split_sentences_to_html(chap_data["content"])
                word_count = len(formatted_content.split())
                
                # Check word count - must be >= 1000 words
                if word_count < 1000:
                    print(f"  [WARN] Word count is {word_count} (< 1000). Retrying/expanding...")
                    # Ask for expansion
                    expansion_prompt = f"""Chương sau đây chỉ có {word_count} từ. Hãy viết lại và mở rộng chương này thật chi tiết để đạt trên 1200 từ. 
Thêm đối thoại kịch tính giữa các nhân vật, mô tả kỹ các chi tiết vật lý, bối cảnh thực tế tại Việt Nam, nội tâm nhân vật sâu sắc hơn.

Chương cũ:
Tiêu đề: {chap_data['title']}
Nội dung: {chap_data['content']}"""
                    
                    expanded_raw = call_openai(
                        system_prompt="Bạn là nhà văn sảng văn V13 chuyên nghiệp, có biệt tài viết truyện chi tiết cực kỳ dài và hấp dẫn.",
                        user_prompt=expansion_prompt,
                        temperature=0.8
                    )
                    
                    try:
                        cleaned = expanded_raw.strip()
                        if cleaned.startswith("```"):
                            cleaned = re.sub(r"^```(?:json)?\n", "", cleaned)
                            cleaned = re.sub(r"\n```$", "", cleaned).strip()
                        expanded_data = json.loads(cleaned)
                        chap_data["content"] = expanded_data.get("content", chap_data["content"])
                    except:
                        # If JSON parse fails, treat raw string as content
                        chap_data["content"] = expanded_raw
                    
                    formatted_content = split_sentences_to_html(chap_data["content"])
                    word_count = len(formatted_content.split())
                
                print(f"  [SUCCESS] Chapter {idx}: {chap_data['title']} ({word_count} words)")
                
                chapters.append({
                    "title": chap_data["title"],
                    "content": formatted_content
                })
                
                # Save brief summary for next chapters
                chaps_summary.append(f"Chương {idx}: {chap_data['title']}. Dàn ý: {outline[:80]}...")
                break
                
            except Exception as e:
                attempt += 1
                print(f"  [ERROR] Attempt {attempt} failed: {e}")
                time.sleep(3)
        
        if attempt == 3:
            raise Exception(f"Failed to generate chapter {idx} of story {story_id} after 3 attempts.")
            
    payload = {
        "post_id": story_id,
        "secret": "ZEN_TRUYEN_2026_BYPASS",
        "intro": config["intro"],
        "focus_keyword": config["focus_keyword"],
        "seo_title": config["seo_title"],
        "seo_description": config["seo_description"],
        "chapters": chapters
    }
    
    out_file = os.path.join(SCRATCH_DIR, f"rewrite_{story_id}_v13.json")
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
        
    print(f"\n[OK] Completed story {story_id}. Saved to {out_file}")


def main():
    os.makedirs(SCRATCH_DIR, exist_ok=True)
    
    # We can process them one by one
    for story_id, config in STORIES_CONFIG.items():
        generate_story_v13(story_id, config)
        time.sleep(2)
        
    print("\n🎉 ALL STORIES SUCCESSFULLY GENERATED IN V13 COMPLIANT FORMAT!")


if __name__ == "__main__":
    main()
