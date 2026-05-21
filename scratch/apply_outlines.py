# -*- coding: utf-8 -*-
import os
import json

# Define the new dynamic novels with multi-slap structure
NOVELS = [
    {
        "id": 2207,
        "title": "Thuyền Trưởng Tỷ Phú Cảng Tiên Sa",
        "author": "Lê Quang Vũ",
        "genre": "Sảng Văn",
        "intro": "<p><strong>\"Thuyền trưởng Lê Quang Vũ, người đã điều hành tàu container 50.000 tấn qua eo Malacca ba mươi lần, bị tên cai bến người nước ngoài đá vào lưng và hét: 'Mày chỉ là cu li bốc vác, biết thân thì im!'\"</strong></p><p><strong>Thế nhưng họ không ngờ, chỉ vài tuần sau, anh đứng trên đỉnh cao ngành cảng biển Đà Nẵng, được sự hậu thuẫn tối cao của Cảng vụ hàng hải và các lực lượng chức năng C03, phanh phui toàn bộ hợp đồng ma hòng thôn tính cảng Tiên Sa...</strong></p><hr /><p>Lê Quang Vũ là một thuyền trưởng container kiệt xuất, vì tranh chấp với sếp ngoại bang hống hách tại cảng Tiên Sa Đà Nẵng nên bị sa thải vô cớ, bôi nhọ danh dự. Vô tình, bản phân tích dòng chảy logistics tuyệt hảo của anh lọt vào mắt Ngô Thị Hương – Giám đốc Cảng vụ tài năng và sắc sảo. Được sự tin cậy của cô, Vũ bước vào cuộc chiến cam go bảo vệ chủ quyền logistics cảng Tiên Sa trước âm mưu thâu tóm lén lút của tập đoàn ngoại bang. Với trí tuệ vượt trội và sự hỗ trợ quyết liệt của pháp luật Việt Nam, Vũ đã lật ngược thế cờ ngoạn mục, đưa kẻ hống hách ra ánh sáng.</p>",
        "cover_prompt": "highly detailed book cover, professional anime style, a handsome Vietnamese sea captain in a white uniform standing on the deck of a massive cargo container ship in Da Nang Tiên Sa port, an elegant Vietnamese businesswoman in a premium suit next to him, golden sunset over the East Sea, cinematic lighting",
        "chapters_outline": [
            {
                "chap_num": 1,
                "title_hint": "Chương 1: Bến Cũ Đắng Cay",
                "outline": "Lê Quang Vũ bị tên sếp bốc vác người nước ngoài hống hách nhục mạ thậm tệ trước mặt hàng trăm công nhân tại cảng Tiên Sa Đà Nẵng, rồi bị sa thải vô cớ. Vũ kìm nén cơn giận, âm thầm thu dọn đồ đạc cá nhân trong tiếng xì xào khinh bỉ của phe phản diện."
            },
            {
                "chap_num": 2,
                "title_hint": "Chương 2: Mỹ Nhân Cảng Vụ",
                "outline": "Ngô Thị Hương - Giám đốc Cảng vụ tài năng, phát hiện bản phân tích dòng chảy logistics và phương án vận tải cầu cảng tuyệt hảo của Vũ bị vứt trong thùng rác phòng điều hành. Cô lập tức nhận ra đây là một thiên tài cảng biển đang bị vùi dập và tìm cách tiếp cận anh."
            },
            {
                "chap_num": 3,
                "title_hint": "Chương 3: Thử Thách Cầu Cảng",
                "outline": "Hương gặp Vũ tại quán nước ven cảng Tiên Sa. Cô là người sắc sảo nên đặt thử thách cực kỳ khắc nghiệt: Vũ phải lập phương án giải tỏa ùn tắc nghiêm trọng tại cầu cảng Tiên Sa đang bị tê liệt dòng cont trong vòng 24 giờ. Vũ chấp nhận và hoàn thành xuất sắc phương án kỹ thuật thông minh khiến Hương nể phục tuyệt đối."
            },
            {
                "chap_num": 4,
                "title_hint": "Chương 4: Hợp Đồng Ma Từ Đảo Đài",
                "outline": "Trong quá trình tối ưu hóa cảng, Vũ và Hương tình cờ phát hiện ra một âm mưu động trời: gã sếp ngoại bang đã bí mật ký kết một 'hợp đồng ma' cho thuê độc quyền bến cảng với giá rẻ mạt hòng thâu tóm toàn bộ hạ tầng cảng biển chiến lược của Đà Nẵng cho một tập đoàn ngoại."
            },
            {
                "chap_num": 5,
                "title_hint": "Chương 5: Khủng Hoảng Phong Tỏa Cảng",
                "outline": "Biết bị lộ, đối thủ lập tức ra tay trước. Chúng thuê hàng chục xe tải và container không giấy tờ dàn hàng ngang vây kín mọi lối ra vào cảng Tiên Sa, ép cảng ngừng hoạt động hoàn toàn, gây khủng hoảng chuỗi logistics miền Trung và đổ vạ do năng lực quản lý của Hương."
            },
            {
                "chap_num": 6,
                "title_hint": "Chương 6: Cú Phản Công Bằng Chứng",
                "outline": "Giữa vòng vây khủng hoảng dư luận và sức ép đóng cảng, Vũ cực kỳ điềm tĩnh. Anh cùng Hương dùng Starlink kết nối máy chủ dự phòng, trích xuất toàn bộ file ghi âm hối lộ, log giao dịch ngân hàng ngoại bang và bản gốc hợp đồng ma. Họ gửi thẳng tài liệu nặc danh cho C03 Bộ Công an. [Vả mặt lần 1: Gã sếp ngoại bang hống hách bị phanh phui và bắt giữ khẩn cấp trước toàn thể nhân viên cảng]."
            },
            {
                "chap_num": 7,
                "title_hint": "Chương 7: Thế Lực Ngoại Bang Trừng Phạt",
                "outline": "Phe phản diện không chịu phục, tập đoàn tài phiệt ngoại quốc đứng sau gã sếp cũ dùng thế lực tài chính ép ngân hàng Techcombank đóng băng hạn mức tín dụng của cảng Tiên Sa, đồng thời kích hoạt các điều khoản phạt hợp đồng quốc tế hòng thâu tóm toàn bộ cảng biển thông qua hình thức cưỡng chế nợ M&A lắt léo."
            },
            {
                "chap_num": 8,
                "title_hint": "Chương 8: Cuộc Chiến M&A Chớp Nhoáng",
                "outline": "Vũ và Hương bình tĩnh lật kèo. Nhờ sự hậu thuẫn tài chính từ MB Bank và các quy định pháp lý sắc bén của Luật Doanh nghiệp Việt Nam, Vũ thiết lập một phương án sáp nhập ngược (reverse merger) chớp nhoáng, thâu tóm ngược lại 51% cổ phần công ty mẹ của đối thủ. [Vả mặt lần 2: Đập tan thế lực tài phiệt ngoại quốc, giành lại chủ quyền cảng biển tối cao]."
            },
            {
                "chap_num": 9,
                "title_hint": "Chương 9: Neo Đậu Bình Yên",
                "outline": "Hương sòng phẳng trao hợp đồng quản lý tối cao toàn bộ hệ thống logistics cảng Tiên Sa cho Vũ với mức lương ngàn đô. Dưới bóng hoàng hôn lộng lẫy trên sông Hàn, nhìn về cầu Rồng, Hương chủ động bộc bạch tình cảm tự nguyện chân thành của mình dành cho anh."
            }
        ]
    },
    {
        "id": 2259,
        "title": "Đầu Bếp Hội An Và Sao Michelin Đà Nẵng",
        "author": "Phạm Hoàng Minh",
        "genre": "Sảng Văn",
        "intro": "<p><strong>Phạm Hoàng Minh bị đối thủ hèn hạ trộm mất công thức bánh mì truyền thống 70 năm của gia đình, đồng thời thuê truyền thông vu khống tiệm dùng phụ gia độc hại hòng tiêu diệt danh tiếng dòng họ.</strong></p><p>Thế nhưng họ không ngờ, tài năng của Minh đã lọt vào mắt Trần Diệu Linh – chuyên gia ẩm thực cấp cao của Bộ Y tế. Với sự hỗ trợ của cô, Minh đã mang món ăn truyền thống lên bàn tiệc quốc tế trước hội đồng Michelin Asia Pacific đầy kiêu ngạo...</p>",
        "cover_prompt": "highly detailed book cover, professional anime style, a young Vietnamese chef in a black uniform cooking premium dishes, a beautiful female food expert in a stylish dress tasting next to him, traditional lanterns of Hoi An ancient town in the background, elegant warm lighting",
        "chapters_outline": [
            {
                "chap_num": 1,
                "title_hint": "Chương 1: Trộm Công Thức Gia Truyền",
                "outline": "Phạm Hoàng Minh bị đối thủ cạnh tranh mua chuộc người làm cướp đi công thức bánh mì 70 năm của dòng họ. Kẻ phản diện mở tiệm lớn đối diện, đồng thời thuê báo chí bẩn tung tin đồn tiệm bánh mì của Minh dùng phụ gia hóa chất độc hại gây ngộ độc."
            },
            {
                "chap_num": 2,
                "title_hint": "Chương 2: Vị Khách Đặc Biệt Bộ Y Tế",
                "outline": "Trong lúc tiệm vắng vẻ vì tin đồn, Trần Diệu Linh - chuyên gia ẩm thực cấp cao của Bộ Y tế âm thầm đến nếm thử bánh mì của Minh. Bằng vị giác nhạy bén, cô phát hiện ra hương vị thuần khiết tuyệt hảo không hề có hóa chất và nhận ra Minh có kỹ nghệ nấu ăn đẳng cấp."
            },
            {
                "chap_num": 3,
                "title_hint": "Chương 3: Thách Thức Bàn Tiệc Michelin",
                "outline": "Linh đề xuất cơ hội lớn: Minh phải tham gia nấu tiệc cho một phái đoàn đại biểu Michelin Guide khu vực châu Á - Thái Bình Dương tại resort năm sao. Đây là thử thách cực kỳ khó khăn vì khẩu vị của các giám khảo quốc tế vô cùng khắt khe và kiêu ngạo."
            },
            {
                "chap_num": 4,
                "title_hint": "Chương 4: Phá Hoại Thực Phẩm Bẩn",
                "outline": "Biết tin Minh được chọn, đối thủ lẻn vào phá hoại. Chúng mua chuộc nhân viên kho lạnh tráo toàn bộ nguyên liệu sạch của Minh bằng thịt và rau củ đã ôi thiu hỏng hóc ngay trước giờ tiệc bắt đầu nhằm hủy hoại anh hoàn toàn."
            },
            {
                "chap_num": 5,
                "title_hint": "Chương 5: Khủng Hoảng Đình Chỉ Khẩn Cấp",
                "outline": "Đoàn thanh tra an toàn thực phẩm bất ngờ ập vào niêm phong khu bếp của Minh ngay giữa tiệc do có thư tố cáo nặc danh. Khách khứa xì xào, đối thủ đắc ý tưởng Minh đã hết đường lui và danh tiếng sẽ tan tành."
            },
            {
                "chap_num": 6,
                "title_hint": "Chương 6: Kỹ Nghệ Trung Hòa Độc Tố",
                "outline": "Linh dùng thẩm quyền pháp lý trì hoãn thời gian thanh tra để làm rõ. Minh bình tĩnh sử dụng các loại gia vị Nam dược thảo mộc tự nhiên và kỹ thuật sơ chế độc bản để xử lý hoàn hảo nguyên liệu tươi thay thế, trung hòa mọi dư lượng độc chất và tạo ra món ăn đột phá tuyệt hảo. [Vả mặt lần 1: Giành điểm Michelin tuyệt đối, đập tan màn bôi nhọ trước mặt quan khách]."
            },
            {
                "chap_num": 7,
                "title_hint": "Chương 7: Liên Minh Cắt Nguồn Cung",
                "outline": "Kẻ phản diện không phục, bắt tay với một chuỗi thức ăn nhanh khổng lồ nước ngoài để thu mua gom toàn bộ nguồn nguyên liệu sạch ở các nông trang miền Trung nhằm chặn đứng hoạt động của nhà hàng của Minh."
            },
            {
                "chap_num": 8,
                "title_hint": "Chương 8: Nông Nghiệp Hữu Cơ Tự Chủ",
                "outline": "Minh cùng Linh trực tiếp đi liên hệ với Sở Nông nghiệp và các hợp tác xã nông nghiệp hữu cơ Đắk Lắk và Quảng Nam, ký kết hợp tác cung ứng khép kín trực tiếp không qua trung gian, phá tan thế bao vây cô lập nguồn cung của đối thủ."
            },
            {
                "chap_num": 9,
                "title_hint": "Chương 9: Phán Quyết Michelin Cúi Đầu",
                "outline": "Tại buổi họp báo trao sao Michelin quốc tế diễn ra hoành tráng, đối thủ hống hách xuất hiện để giễu cợt Minh. Ngay lúc đó, Linh công bố bằng chứng trích xuất camera và tài liệu điều tra về hành vi trộm cắp công thức, cài cắm người phá hoại thực phẩm. Cảnh sát ập vào còng tay kẻ phản diện và đại diện chuỗi thức ăn nhanh kia trước toàn thể báo chí quốc tế. Nhà hàng của Minh được trao 2 sao Michelin danh giá. [Vả mặt lần 2: Đập tan liên minh chèn ép và tống giam kẻ thủ ác]."
            },
            {
                "chap_num": 10,
                "title_hint": "Chương 10: Hương Vị Phố Cổ",
                "outline": "Tiệm bánh mì truyền thống của Minh lấy lại công lý và vinh quang, nườm nượp khách xếp hàng dài từ sáng tới tối. Bên dòng sông Hoài Hội An lung linh hoa đăng đèn lồng rực rỡ, Linh chủ động bày tỏ tình yêu chân thành tự nguyện với Minh."
            }
        ]
    },
    {
        "id": 2269,
        "title": "CEO Giấu Mặt Đảo Lộn Tập Đoàn Dệt May Bình Dương",
        "author": "Trần Minh Khải",
        "genre": "Sảng Văn",
        "intro": "<p><strong>Trần Minh Khải bị người cha nuôi và gã anh họ tước đoạt quyền thừa kế tập đoàn dệt may 2000 tỷ đồng tại Bình Dương một cách nhẫn tâm, đuổi anh ra khỏi công ty với hai bàn tay trắng.</strong></p><p>Thế nhưng họ không ngờ, sự xuất hiện của Đinh Lan Anh – nữ luật sư M&A sừng sỏ nhất Hà Nội – đã cùng Khải lập nên một kế hoạch tái cấu trúc pháp lý siêu đẳng, lật ngược thế cờ ngay trước mũi SCIC và toàn bộ hội đồng quản trị hống hách...</p>",
        "cover_prompt": "highly detailed book cover, professional anime style, a handsome young Vietnamese CEO in a sharp dark suit standing in a modern textile factory in Binh Duong VSIP, a brilliant female lawyer in business attire standing beside him holding merger documents, bright industrial lighting",
        "chapters_outline": [
            {
                "chap_num": 1,
                "title_hint": "Chương 1: Đuổi Khỏi Hội Đồng Quản Trị",
                "outline": "Trần Minh Khải bị gã anh họ mưu mô và người cha nuôi hám lợi dùng tài liệu giả tước đoạt toàn bộ cổ phần và quyền thừa kế tập đoàn dệt may trị giá 2000 tỷ. Họ đuổi anh khỏi văn phòng trước mặt tất cả ban quản trị."
            },
            {
                "chap_num": 2,
                "title_hint": "Chương 2: Nữ Luật Sư M&A Sắc Sảo",
                "outline": "Đinh Lan Anh - nữ luật sư M&A xuất chúng, xuất hiện tiếp cận Khải tại Bình Dương. Cô đưa ra bản phân tích cấu trúc pháp lý ẩn của tập đoàn và đề xuất kế hoạch 'sáp nhập ngược' (reverse merger) để thâu tóm lại tập đoàn dệt may."
            },
            {
                "chap_num": 3,
                "title_hint": "Chương 3: Thử Thách SCIC",
                "outline": "Để được SCIC (Tổng công ty Đầu tư và Kinh doanh vốn Nhà nước) hỗ trợ nguồn vốn chiến lược, Khải phải vượt qua thử thách cực kỳ cam go: khôi phục hoạt động của một xưởng dệt dập nát đang thua lỗ 100 tỷ tại khu công nghiệp Bình Dương trong vòng 2 tuần."
            },
            {
                "chap_num": 4,
                "title_hint": "Chương 4: Bẫy Kiểm Toán Thuế",
                "outline": "Đối thủ cài gián điệp vào xưởng dệt của Khải, lén lút sửa đổi chứng từ kế toán nhập khẩu nguyên liệu và báo cáo tài chính giả nhằm vu khống Khải trốn thuế nghiêm trọng và lừa đảo chiếm đoạt tài sản nhà nước."
            },
            {
                "chap_num": 5,
                "title_hint": "Chương 5: Khủng Hoảng Niêm Phong Nhà Máy",
                "outline": "Cơ quan thuế bất ngờ đình chỉ hoạt động nhà máy, phong tỏa tài khoản Techcombank của xưởng dệt. 1000 công nhân hoang mang đình công vì sợ mất lương, đối thủ tung tin đồn thất thiệt lên các trang báo chí nhằm bóp nghẹt Khải."
            },
            {
                "chap_num": 6,
                "title_hint": "Chương 6: Bằng Chứng Lật Kèo Pháp Lý",
                "outline": "Giữa cơn bão phong tỏa tài khoản và sức ép công nhân, Lan Anh cực kỳ sắc bén đưa ra bản sao lưu chứng từ gốc được lưu trữ bảo mật trên blockchain, kèm video quay lại hành vi cài cắm số liệu giả của gián điệp. [Vả mặt lần 1: Đập tan cáo buộc trốn thuế, gỡ phong tỏa tài khoản trong sự ngỡ ngàng của gã anh họ]."
            },
            {
                "chap_num": 7,
                "title_hint": "Chương 7: Đòn Phản Công Rút Ruột Tài Sản",
                "outline": "Phản diện thấy không hại được Khải bằng thuế, liền kích hoạt quyền biểu quyết đa số của hội đồng quản trị cũ nhằm thông qua quyết định bán rẻ toàn bộ đất đai nhà xưởng cốt lõi của tập đoàn cho một công ty sân sau của chúng ở nước ngoài, hòng rút ruột công ty trước khi Khải kịp thâu tóm."
            },
            {
                "chap_num": 8,
                "title_hint": "Chương 8: Cuộc Đua Thu Gom Trên Sàn HNX",
                "outline": "Khải và Lan Anh nhận được sự hậu thuẫn tài chính mạnh mẽ từ các định chế tài chính trong nước, âm thầm gom mua toàn bộ số cổ phiếu trôi nổi của tập đoàn trên thị trường chứng khoán nhằm phá vỡ quyền biểu quyết chi phối của đối thủ."
            },
            {
                "chap_num": 9,
                "title_hint": "Chương 9: Bẫy Lòng Tham Của Cha Nuôi",
                "outline": "Khải cố ý thả thông tin giả về việc xưởng dệt đang gặp khủng hoảng nghiêm trọng không thể cứu vãn để dụ người cha nuôi và gã anh họ bán bớt một lượng cổ phần chiến lược ra thị trường để chốt lời tháo chạy, giúp Khải thâu tóm nốt lượng cổ phần này."
            },
            {
                "chap_num": 10,
                "title_hint": "Chương 10: Đại Hội Cổ Đông Sấm Sét",
                "outline": "Tại đại hội cổ đông quyết định bán tài sản tập đoàn, đối thủ đang hí hửng chuẩn bị ký kết hợp đồng thì Khải và Lan Anh bước vào cùng SCIC. Khải trình ra chứng nhận sở hữu 51% cổ phần chi phối tuyệt đối, tuyên bố bãi nhiệm toàn bộ hội đồng quản trị cũ. Cơ quan C03 ập vào bắt giam cha nuôi và gã anh họ vì tội cố ý hủy hoại tài sản doanh nghiệp và thông đồng lừa đảo. [Vả mặt lần 2: Tước đoạt hoàn toàn vương quyền của kẻ phản bội, tống giam toàn bộ ban quản trị cũ]."
            },
            {
                "chap_num": 11,
                "title_hint": "Chương 11: Sợi Chỉ Gắn Kết",
                "outline": "Tập đoàn dệt may Bình Dương khôi phục hoạt động rực rỡ, vị thế CEO tối cao thuộc về Khải. Bên ngoài ban công văn phòng lộng lẫy nhìn xuống khu công nghiệp VSIP, Lan Anh sòng phẳng thổ lộ tình cảm chân thành tự nguyện với Khải."
            }
        ]
    },
    {
        "id": 2279,
        "title": "Ông Hoàng Địa Ốc Ẩn Thế Phú Mỹ Hưng",
        "author": "Đinh Thanh Tùng",
        "genre": "Sảng Văn",
        "intro": "<p><strong>Đinh Thanh Tùng bị đồng nghiệp phản bội vu khống nhận hoa hồng bẩn 10 tỷ đồng, bị đuổi khỏi công ty định giá bất động sản hàng đầu Sài Gòn và bị bôi nhọ danh dự trên mọi phương tiện truyền thông.</strong></p><p>Thế nhưng họ không ngờ, tài năng định giá thiên tài của Tùng đã lọt vào mắt Nguyễn Minh Châu – nữ CEO xinh đẹp của quỹ đầu tư địa ốc REIT 5000 tỷ. Cuộc chiến giành lại công lý và vương quyền bất động sản Phú Mỹ Hưng bắt đầu từ đây...</p>",
        "cover_prompt": "highly detailed book cover, professional anime style, a handsome Vietnamese real estate expert pointing at a structural plan, next to an elegant wealthy female CEO in a premium business dress, modern glass skyscraper luxury apartment complex of Phu My Hung District 7 in the background",
        "chapters_outline": [
            {
                "chap_num": 1,
                "title_hint": "Chương 1: Bẫy Hoa Hồng Địa Ốc",
                "outline": "Đinh Thanh Tùng bị gã đồng nghiệp phản bội lập hồ sơ khống vu oan anh nhận hoa hồng bẩn 10 tỷ VNĐ từ khách hàng. Tùng bị sa thải vô cớ khỏi công ty định giá bất động sản hàng đầu, bị người yêu cũ khinh miệt."
            },
            {
                "chap_num": 2,
                "title_hint": "Chương 2: Nữ Tổng Tài Quỹ REIT",
                "outline": "Nguyễn Minh Châu - CEO trẻ tuổi sắc sảo của quỹ REIT 5000 tỷ tìm đến Tùng. Cô đang muốn mua lại một tòa nhà thương mại lớn ở Quận 7 nhưng nghi ngờ có bẫy định giá khống nên muốn kiểm chứng tài năng của anh."
            },
            {
                "chap_num": 3,
                "title_hint": "Chương 3: Thử Thách Định Giá",
                "outline": "Châu đặt ra thử thách cực kỳ khó: Tùng phải tìm ra lỗi quy hoạch ẩn và khoản nợ tiềm ẩn của tòa nhà trị giá 1200 tỷ tại Phú Mỹ Hưng trong vòng 3 ngày mà không được tiếp cận hồ sơ gốc."
            },
            {
                "chap_num": 4,
                "title_hint": "Chương 4: Hợp Đồng Khống Siết Nợ",
                "outline": "Đối thủ biết Tùng đang thẩm định nên lén lút tạo hợp đồng giả mạo chữ ký định giá khống của Tùng để gài bẫy anh chịu trách nhiệm pháp lý liên đới nếu dự án xảy ra tranh chấp đổ vỡ."
            },
            {
                "chap_num": 5,
                "title_hint": "Chương 5: Khủng Hoảng Phong Tỏa Tài Sản",
                "outline": "Tài khoản Techcombank của Tùng bị phong tỏa khẩn cấp, cảnh sát kinh tế triệu tập điều tra. Các bài báo bẩn liên tục đăng tin Tùng là kẻ lừa đảo bất động sản lừng danh, khiến danh dự anh rơi xuống vực thẳm."
            },
            {
                "chap_num": 6,
                "title_hint": "Chương 6: Sự Thật Bản Đồ Sở Xây Dựng",
                "outline": "Tùng cực kỳ điềm tĩnh cùng Châu lên Sở Xây Dựng trích xuất bản gốc quy hoạch địa chính quận 7 từ 10 năm trước. Anh chứng minh tòa nhà của đối thủ đang vi phạm kết cấu và nằm trên hành lang an toàn lưới điện nghiêm trọng. [Vả mặt lần 1: Đập tan bẫy định giá khống, cứu nguy quỹ REIT khỏi phi vụ lừa đảo 1200 tỷ]."
            },
            {
                "chap_num": 7,
                "title_hint": "Chương 7: Sự Trả Thù Kích Hoạt Tín Dụng Đen",
                "outline": "Đối thủ điên cuồng vì mất phi vụ 1200 tỷ, bắt tay với một băng nhóm xã hội đen tài chính núp bóng tiệm cầm đồ lớn, làm giả các giấy tờ nợ khống ép buộc gia đình Tùng phải gán nợ khu đất vàng gia bảo ở Phú Mỹ Hưng."
            },
            {
                "chap_num": 8,
                "title_hint": "Chương 8: Cuộc Chiến Trên Bàn Pháp Lý",
                "outline": "Tùng sử dụng kiến thức luật địa ốc sâu sắc và sự hỗ trợ tài chính từ Châu, phát hiện ra toàn bộ giấy tờ nợ của đối thủ vi phạm nghiêm trọng Luật các tổ chức tín dụng và Bộ luật Hình sự Việt Nam."
            },
            {
                "chap_num": 9,
                "title_hint": "Chương 9: Bẫy Ngược Kẻ Đi Đòi Nợ",
                "outline": "Tùng giả vờ yếu thế, dẫn dụ gã phản diện và đồng bọn ký kết hợp đồng chuyển nhượng quyền sử dụng đất có điều kiện, đồng thời bí mật cài cắm camera ghi hình và thiết bị thu âm toàn bộ quá trình đe dọa cưỡng đoạt tài sản."
            },
            {
                "chap_num": 10,
                "title_hint": "Chương 10: Đột Kích Văn Phòng Công Chứng",
                "outline": "Khi đối thủ đang hí hửng ép Tùng ký bàn giao đất tại văn phòng công chứng lớn ở Quận 7, lực lượng công an ập vào khống chế toàn bộ băng nhóm vì tội cưỡng đoạt tài sản và cho vay lãi nặng trong giao dịch dân sự."
            },
            {
                "chap_num": 11,
                "title_hint": "Chương 11: Đập Tan Công Ty Định Giá Cũ",
                "outline": "Tùng công bố toàn bộ tài liệu kiểm toán độc lập phanh phui đường dây định giá khống suốt 5 năm của công ty định giá cũ (nơi đã đuổi anh). Công ty này bị rút giấy phép hoạt động và sụp đổ hoàn toàn trong vòng 24 giờ. [Vả mặt lần 2: Đập tan băng nhóm tín dụng đen và công ty định giá cũ phản bội]."
            },
            {
                "chap_num": 12,
                "title_hint": "Chương 12: Hoàng Hôn Quận 7",
                "outline": "Tùng lấy lại danh tiếng vẻ vang, trở thành cổ đông lớn của dự án Phú Mỹ Hưng. Dưới ánh hoàng hôn lộng lẫy bên cầu Ánh Sao Quận 7 sầm uất, Châu chủ động thổ lộ tình yêu tự nguyện chân thành với Tùng."
            }
        ]
    },
    {
        "id": 2289,
        "title": "Vũ Công Hoàng Gia Và Đế Chế Nhà Hát Lớn",
        "author": "Nguyễn Hoàng Long",
        "genre": "Sảng Văn",
        "intro": "<p><strong>Nguyễn Hoàng Long bị Giám đốc nghệ thuật tham lam cướp trắng vở kịch ballet tâm huyết cả đời, đồng thời vu oan anh đạo nhái và đuổi cổ anh khỏi Nhà hát Lớn Hà Nội trong nhục nhã.</strong></p><p>Thế nhưng họ không ngờ, sự xuất hiện của Lê Bích Ngọc – Chủ tịch tập đoàn giải trí hàng đầu Việt Nam – đã chắp cánh cho thiên tài của Long bùng nổ, tạo nên một vở diễn chấn động giới mộ điệu quốc tế...</p>",
        "cover_prompt": "highly detailed book cover, professional anime style, a handsome male ballet dancer performing a dramatic jump on a grand theater stage, a beautiful elegant female executive watching from a VIP box seat, grand classical lighting of Hanoi Opera House",
        "chapters_outline": [
            {
                "chap_num": 1,
                "title_hint": "Chương 1: Đuổi Khỏi Sân Khấu Hoàng Gia",
                "outline": "Nguyễn Hoàng Long bị gã Giám đốc nghệ thuật hống hách cướp mất vở kịch ballet tâm huyết và vu khống anh đạo nhái ý tưởng. Gã đuổi Long khỏi Nhà hát Lớn Hà Nội ngay trước mặt toàn bộ đoàn diễn viên."
            },
            {
                "chap_num": 2,
                "title_hint": "Chương 2: Nữ Chủ Tịch Đế Chế Giải Trí",
                "outline": "Lê Bích Ngọc - Chủ tịch đế chế giải trí V-League, vô tình xem được đoạn clip nhảy ngẫu hứng đầy đam mê và kỹ thuật đỉnh cao của Long tại phòng tập nhỏ. Cô lập tức nhận ra thiên tài nghệ thuật bị vùi dập và cam kết tài trợ."
            },
            {
                "chap_num": 3,
                "title_hint": "Chương 3: Thử Thách Tuyển Chọn Quốc Tế",
                "outline": "Ngọc đặt thử thách cực kỳ khắc nghiệt: Long phải dàn dựng hoàn chỉnh một vở ballet mới tinh để chinh phục Hội đồng giám khảo nghệ thuật Pháp trong vòng một tuần để chứng minh năng lực thật sự."
            },
            {
                "chap_num": 4,
                "title_hint": "Chương 4: Phá Hoại Đạo Cụ Diễn",
                "outline": "Kẻ phản diện biết tin đã thuê người lẻn vào rạp diễn tập cắt đứt dây cáp treo bảo hộ và rải đinh sắt lên sàn diễn của Long nhằm gây tai nạn chấn thương nghiêm trọng cho toàn đội ngay trước thềm kiểm duyệt."
            },
            {
                "chap_num": 5,
                "title_hint": "Chương 5: Khủng Hoảng Chấn Thương Diễn Viên",
                "outline": "Diễn viên nam chính bị chấn thương nghiêm trọng ngay sát giờ diễn chính thức. Báo chí bẩn lập tức đưa tin chỉ trích Long làm việc tắc trách vô trách nhiệm, đe dọa hủy hoại toàn bộ công sức của cả đoàn."
            },
            {
                "chap_num": 6,
                "title_hint": "Chương 6: Vũ Điệu Thay Thế Kỳ Tích",
                "outline": "Không chịu khuất phục, Long trực tiếp mặc trang phục bước lên sân khấu thay thế vị trí diễn viên chính. Anh thực hiện kỹ thuật xoay người liên hoàn 32 vòng Fouetté đỉnh cao hoàn hảo, chấn động toàn bộ khán phòng. [Vả mặt lần 1: Vở diễn nhận tràng pháo tay vang dội, giám khảo Pháp chấm điểm tuyệt đối, vạch trần âm mưu phá hoại đạo cụ]."
            },
            {
                "chap_num": 7,
                "title_hint": "Chương 7: Đòn Trả Thù Phong Tỏa Sân Khấu",
                "outline": "Giám đốc nghệ thuật cũ cấu kết với nhà tài trợ cũ tìm cách phong tỏa rạp hát, không cho đoàn của Long biểu diễn. Long sử dụng hợp đồng liên kết nghệ thuật quốc tế được phê duyệt bởi Bộ Văn hóa và sự hỗ trợ pháp lý đanh thép từ Ngọc để bãi nhiệm chức vụ của gã phản diện ngay lập tức. [Vả mặt lần 2: Trục xuất hoàn toàn gã cựu giám đốc nghệ thuật phản bội khỏi giới nghệ thuật Việt Nam]."
            },
            {
                "chap_num": 8,
                "title_hint": "Chương 8: Khúc Vĩ Thanh Lãng Mạn",
                "outline": "Long được bổ nhiệm làm Giám đốc Nghệ thuật tối cao trọn đời của Nhà hát Lớn. Dưới ánh đèn lung linh huyền ảo của sân khấu hoàng gia, Ngọc chủ động thổ lộ tình yêu chân thành tự nguyện với anh."
            }
        ]
    },
    {
        "id": 2217,
        "title": "Kỹ Sư Smart Grid Và Bóng Tối EVN",
        "author": "Phan Đức Thành",
        "genre": "Sảng Văn",
        "intro": "<p><strong>Phan Đức Thành phát hiện ra đường dây tham nhũng thiết bị trạm biến áp kém chất lượng gây nguy hiểm cho lưới điện quốc gia, lập tức bị sếp cũ sa thải vu oan phá hoại tài sản nhà nước.</strong></p><p>Thế nhưng họ không ngờ, Nguyễn Thu Trang – Phó Tổng giám đốc EVN trẻ tuổi sắc bén – đã âm thầm điều tra sự việc, cùng Thành bước vào cuộc chiến làm sạch lưới điện quốc gia...</p>",
        "cover_prompt": "highly detailed book cover, professional anime style, a handsome Vietnamese power engineer in a blue uniform analyzing complex glowing electric grid schematics on a digital screen, an intelligent female executive in dark business suit standing next to him, power lines background",
        "chapters_outline": [
            {
                "chap_num": 1,
                "title_hint": "Chương 1: Sa Thải Giữa Đêm Đông",
                "outline": "Phan Đức Thành phát hiện đường dây mua bán thiết bị biến áp kém chất lượng của sếp cũ tại trạm biến áp KCN Hà Nam. Ngay lập tức anh bị sếp cũ dùng quyền lực sa thải vô cớ, vu oan phá hoại thiết bị."
            },
            {
                "chap_num": 2,
                "title_hint": "Chương 2: Nữ Phó Tổng EVN Sắc Sảo",
                "outline": "Nguyễn Thu Trang - Phó Tổng giám đốc EVN trẻ tuổi và sắc bén, nghi ngờ quyết định sa thải Thành nên âm thầm tiếp cận anh để tìm hiểu sự thật về chất lượng thiết bị điện quốc gia."
            },
            {
                "chap_num": 3,
                "title_hint": "Chương 3: Thử Thách Trạm Biến Áp",
                "outline": "Trang đặt ra thử thách cực kỳ khó khăn: Thành phải lập phương án khôi phục lưới điện thông minh (Smart Grid) cho KCN Hà Nam đang bị quá tải công suất nghiêm trọng trong vòng 24 giờ mà không được dùng thiết bị mới."
            },
            {
                "chap_num": 4,
                "title_hint": "Chương 4: Sự Cố Quá Tải Cố Ý",
                "outline": "Sếp cũ của Thành biết chuyện nên lén lút điều khiển ngắt rơ-le an toàn từ xa, cố ý gây mất điện cục bộ trên diện rộng tại KCN Hà Nam nhằm đổ vạ cho phương án lưới điện thông minh của Trang và Thành."
            },
            {
                "chap_num": 5,
                "title_hint": "Chương 5: Khủng Hoảng Tê Liệt Hệ Thống",
                "outline": "KCN Hà Nam mất điện hoàn toàn, các doanh nghiệp nước ngoài phẫn nộ đòi bồi thường hàng trăm tỷ đồng. Dư luận chỉ trích Trang thiếu năng lực, phe phản diện hống hách ép cô từ chức."
            },
            {
                "chap_num": 6,
                "title_hint": "Chương 6: Cứu Nguy Lưới Điện Thông Minh",
                "outline": "Giữa tâm bão khủng hoảng, Thành bình tĩnh sử dụng hệ thống truyền dẫn Starlink kết nối máy chủ dự phòng, định tuyến lại dòng điện thông qua trạm biến áp dự phòng, khôi phục điện hoàn toàn chỉ trong 15 phút. [Vả mặt lần 1: Khôi phục lưới điện thần tốc, chứng minh tài năng kiệt xuất, đập tan mưu đồ đổ vạ của sếp cũ]."
            },
            {
                "chap_num": 7,
                "title_hint": "Chương 7: Cuộc Kiểm Tra Diện Rộng",
                "outline": "Trang dùng thẩm quyền của mình ra lệnh tổng kiểm tra và đình chỉ tạm thời toàn bộ các trạm biến áp đang lắp đặt thiết bị của công ty sân sau của gã sếp cũ để đo đạc chất lượng thực tế."
            },
            {
                "chap_num": 8,
                "title_hint": "Chương 8: Cú Phản Kháng Từ Cấp Trên",
                "outline": "Kẻ phản diện hoảng sợ, nhờ vả một gã quan chức thoái hóa ở cơ quan cấp cao hơn ký văn bản hỏa tốc đình chỉ công tác của Trang và niêm phong tài liệu điều tra của Thành nhằm bóp nghẹt cuộc thanh tra."
            },
            {
                "chap_num": 9,
                "title_hint": "Chương 9: Trích Xuất Dữ Liệu SCADA",
                "outline": "Thành âm thầm dùng quyền quản trị kỹ thuật, trích xuất dữ liệu gốc trên hệ thống SCADA quốc gia, chứng minh đối thủ đã ghi đè thông số kỹ thuật ảo lên hệ thống để lừa dối công tác nghiệm thu."
            },
            {
                "chap_num": 10,
                "title_hint": "Chương 10: Cuộc Gặp Với C03 Bộ Công An",
                "outline": "Trang và Thành trực tiếp mang toàn bộ ổ cứng chứa dữ liệu SCADA gốc và hồ sơ kiểm định giả mạo đến làm việc với Cục Cảnh sát kinh tế C03 Bộ Công an để yêu cầu khởi tố vụ án."
            },
            {
                "chap_num": 11,
                "title_hint": "Chương 11: Sự Sụp Đổ Của Thế Lực Cũ",
                "outline": "C03 tiến hành bắt khẩn cấp gã sếp cũ và đường dây thầu phụ ngay tại cuộc họp giao ban thường niên của tập đoàn điện lực trước sự bàng hoàng của đồng bọn."
            },
            {
                "chap_num": 12,
                "title_hint": "Chương 12: Đập Tan Liên Minh Lợi Ích",
                "outline": "Gã quan chức thoái hóa bảo kê bị đình chỉ công tác điều tra hình sự. Toàn bộ chuỗi cung ứng thiết bị kém chất lượng bị phơi bày trên truyền thông quốc gia. [Vả mặt lần 2: Triệt phá hoàn toàn đường dây lợi ích nhóm cấp cao, làm sạch lưới điện EVN]."
            },
            {
                "chap_num": 13,
                "title_hint": "Chương 13: Dòng Điện Trái Tim",
                "outline": "Thành được bổ nhiệm làm Giám đốc Công nghệ lưới điện thông minh quốc gia. Trang sòng phẳng thổ lộ tình cảm chân thành tự nguyện của mình với anh dưới bầu trời đêm Hà Nội rực rỡ."
            }
        ]
    },
    {
        "id": 2238,
        "title": "Triều Đại Cà Phê Bazan Đắk Lắk",
        "author": "Y Dhăm Nie",
        "genre": "Sảng Văn",
        "intro": "<p><strong>Y Dhăm Nie bị đối tác ngoại bang xảo quyệt cướp mất bằng sáng chế máy rang cà phê bằng tia hồng ngoại gia truyền ba đời, đồng thời vu khống anh ăn cắp công nghệ.</strong></p><p>Thế nhưng họ không ngờ, tài năng của anh đã lọt vào mắt Trần Thị Cẩm Tú – nữ hoàng xuất khẩu nông sản Đắk Lắk. Hành trình giành lại thương hiệu và vương miện cà phê Việt bắt đầu...</p>",
        "cover_prompt": "highly detailed book cover, professional anime style, a handsome Vietnamese Ede man roasting coffee beans with a glowing high-tech roaster, a beautiful businesswoman in green dress holding coffee beans beside him, lush coffee plantation in Dak Lak background",
        "chapters_outline": [
            {
                "chap_num": 1,
                "title_hint": "Chương 1: Bán Đứng Thương Hiệu",
                "outline": "Y Dhăm Nie bị gã đối tác ngoại bang xảo quyệt dùng bẫy hợp đồng cướp mất bằng sáng chế máy rang cà phê bằng tia hồng ngoại gia truyền ba đời của anh, rồi kiện ngược anh vi phạm bản quyền."
            },
            {
                "chap_num": 2,
                "title_hint": "Chương 2: Nữ Hoàng Xuất Khẩu Nông Sản",
                "outline": "Trần Thị Cẩm Tú - Giám đốc chuỗi xuất khẩu cà phê nông sản Đắk Lắk, nhận thấy chất lượng hạt cà phê rang từ máy hồng ngoại của Y Dhăm cực kỳ xuất sắc nên quyết định tài trợ cho anh."
            },
            {
                "chap_num": 3,
                "title_hint": "Chương 3: Thách Thức Đất Đỏ",
                "outline": "Tú đặt thử thách cực kỳ khắc nghiệt: Y Dhăm phải phân biệt và phối ngũ chính xác tỷ lệ 5 loại hạt Robusta từ các vùng thổ nhưỡng khác nhau của Đắk Lắk để tạo ra hương vị độc bản chinh phục cuộc thi cà phê quốc tế."
            },
            {
                "chap_num": 4,
                "title_hint": "Chương 4: Đầu Độc Kho Hạt Cà Phê",
                "outline": "Đối thủ lén mua chuộc kẻ xấu lẻn vào kho hạt cà phê dự thi của Y Dhăm, phun hóa chất độc hại gây nấm mốc hòng hủy hoại toàn bộ số nguyên liệu quý giá của anh ngay trước ngày lên đường dự thi."
            },
            {
                "chap_num": 5,
                "title_hint": "Chương 5: Khủng Hoảng Tước Quyền Dự Thi",
                "outline": "Ban tổ chức cuộc thi nhận được đơn tố cáo nặc danh kèm mẫu thử giả mạo cho thấy cà phê của Y Dhăm chứa dư lượng thuốc trừ sâu cực cao. Danh tiếng của Y Dhăm bị bôi nhọ nghiêm trọng, đứng trước nguy cơ bị tước quyền thi."
            },
            {
                "chap_num": 6,
                "title_hint": "Chương 6: Kỹ Thuật Rang Khử Độc Đột Phá",
                "outline": "Được Tú bảo lãnh pháp lý, Y Dhăm cực kỳ điềm tĩnh. Anh sử dụng nhiệt độ rang hồng ngoại đặc chủng biến đổi cấu trúc hóa học, trung hòa hoàn toàn độc tố và giữ trọn hương vị Bazan thuần khiết thượng hạng, đoạt cúp vô địch thế giới. [Vả mặt lần 1: Đạt điểm số tuyệt đối từ ban giám khảo thế giới, đập tan bẫy vu khống thuốc trừ sâu trước truyền thông]."
            },
            {
                "chap_num": 7,
                "title_hint": "Chương 7: Đơn Kiện Bản Quyền Quốc Tế",
                "outline": "Đối thủ điên cuồng khởi kiện thương hiệu xuất khẩu cà phê của Y Dhăm lên Tòa án thương mại quốc tế tại Singapore, đòi đóng băng toàn bộ các lô hàng xuất khẩu sang châu Âu của anh vì vi phạm sáng chế."
            },
            {
                "chap_num": 8,
                "title_hint": "Chương 8: Đòn Sét Đánh Từ Cục SHTT Việt Nam",
                "outline": "Tú liên hệ với Cục Sở hữu Trí tuệ Việt Nam, trích xuất tài liệu nghiên cứu máy rang gốc có chữ ký của bố Y Dhăm từ 10 năm trước. Bản quyền sáng chế của đối thủ bị tuyên bố hủy bỏ toàn cầu. Tòa án quốc tế tuyên Y Dhăm thắng kiện, phạt đối thủ 10 triệu USD vì hành vi gian lận bản quyền. [Vả mặt lần 2: Đập tan đơn kiện quốc tế, khẳng định chủ quyền trí tuệ cà phê Việt]."
            },
            {
                "chap_num": 9,
                "title_hint": "Chương 9: Hương Cà Phê Ban Mê",
                "outline": "Thương hiệu cà phê Bazan bay cao khắp toàn cầu. Giữa rẫy cà phê hoa trắng muốt nở rộ của vùng đất đỏ Đắk Lắk, Tú chủ động bày tỏ tình cảm chân thành tự nguyện với Y Dhăm."
            }
        ]
    },
    {
        "id": 2249,
        "title": "Nhà Thiết Kế Tàng Hình Vietnam Fashion Week",
        "author": "Châu Minh Hải",
        "genre": "Sảng Văn",
        "intro": "<p><strong>Châu Minh Hải bị người yêu cũ phản bội và gã nhà thiết kế danh tiếng cướp trắng toàn bộ bộ sưu tập dạ hội độc bản dự thi Vietnam Fashion Week, đẩy anh vào cảnh trắng tay nhục nhã.</strong></p><p>Thế nhưng họ không ngờ, sự xuất hiện của Vũ Thanh Huyền – Chủ tịch Hiệp hội Thời trang – đã khai phá thiên tài cắt may và xếp nếp draping đỉnh cao của Hải, vạch trần kẻ đạo nhái trước công chúng...</p>",
        "cover_prompt": "highly detailed book cover, professional anime style, a handsome Vietnamese fashion designer draping rich red silk fabric on a mannequin, a gorgeous confident female fashion president in a luxury blazer standing next to him, runway runway lighting background",
        "chapters_outline": [
            {
                "chap_num": 1,
                "title_hint": "Chương 1: Đánh Cắp Bộ Sưu Tập",
                "outline": "Châu Minh Hải bị người yêu cũ phản bội, lén lút trộm toàn bộ file phác thảo bộ sưu tập dạ hội độc bản của anh đem bán cho một gã nhà thiết kế danh tiếng hống hách. Chúng đuổi Hải đi và vu oan anh là kẻ bất tài ăn cắp."
            },
            {
                "chap_num": 2,
                "title_hint": "Chương 2: Nữ Chủ Tịch Hiệp Hội Thời Trang",
                "outline": "Vũ Thanh Huyền - Chủ tịch Hiệp hội Thời trang Việt Nam (VFA), phát hiện những nét vẽ phác thảo đặc trưng độc nhất vô nhị của Hải bị vứt lại và nhận ra kẻ sáng tạo đích thực đằng sau bộ sưu tập."
            },
            {
                "chap_num": 3,
                "title_hint": "Chương 3: Thử Thách Phác Thảo Sống",
                "outline": "Huyền đặt ra thử thách cực kỳ gắt gao: Hải phải phác thảo và thực hiện cắt may trực tiếp một bộ váy dạ hội cao cấp từ tấm vải lụa thô trong vòng 6 tiếng tại phòng thiết kế của Hiệp hội để chứng minh thực lực."
            },
            {
                "chap_num": 4,
                "title_hint": "Chương 4: Phá Nát Vải Lụa Độc Bản",
                "outline": "Kẻ phản diện lo sợ nên mua chuộc bảo vệ, lén lút tạt mực đen phá hỏng tấm lụa tơ tằm Hà Đông độc nhất vô nhị mà Hải chuẩn bị cho show diễn thời trang quốc tế Vietnam Fashion Week."
            },
            {
                "chap_num": 5,
                "title_hint": "Chương 5: Khủng Hoảng Trước Giờ G",
                "outline": "Show diễn chuẩn bị bắt đầu trong 30 phút, toàn bộ trang phục dự thi của Hải bị phát hiện bị kẻ gian dùng kéo cắt nát tả tơi. Dư luận và báo giới xôn xao, đối thủ đắc ý chuẩn bị ăn mừng chiến thắng."
            },
            {
                "chap_num": 6,
                "title_hint": "Chương 6: Kỹ Thuật Drape Lật Ngược Thế Cờ",
                "outline": "Không hoảng loạn, Hải dùng kỹ thuật xếp nếp draping trực tiếp đỉnh cao trên cơ thể người mẫu, biến những mảnh lụa rách nát thành một kiệt tác thời trang dạ hội bất đối xứng siêu việt chấn động cả khán phòng. [Vả mặt lần 1: Show diễn thành công vang dội ngoài mong đợi, biến khủng hoảng thành kiệt tác thời trang dạ hội độc nhất]."
            },
            {
                "chap_num": 7,
                "title_hint": "Chương 7: Sự Trả Đũa Của Giới Haute Couture",
                "outline": "Gã nhà thiết kế phản diện dùng thế lực truyền thông bêu rếu Hải là kẻ không có bằng cấp học thuật thời trang, chỉ biết cắt may thô sơ không có giá trị nghệ thuật."
            },
            {
                "chap_num": 8,
                "title_hint": "Chương 8: Đòn Phản Công Học Thuật Từ Paris",
                "outline": "Huyền liên hệ với Viện Hàn lâm Thời trang Paris, mời các giáo sư hàng đầu thế giới thẩm định kỹ thuật drape độc bản của Hải. Viện Paris công bố kỹ thuật của Hải là một phát kiến vĩ đại của thời trang hiện đại."
            },
            {
                "chap_num": 9,
                "title_hint": "Chương 9: Ngày Phán Quyết VFA",
                "outline": "Huyền công bố quyết định của Cục Bản quyền tác giả, bảo hộ độc quyền bộ sưu tập cho Hải. Gã NTK phản diện bị cấm hành nghề vĩnh viễn và bị công an khởi tố tội hủy hoại tài sản. [Vả mặt lần 2: Đập tan sự khinh miệt học thuật, cấm hành nghề vĩnh viễn gã phản diện đạo nhái]."
            },
            {
                "chap_num": 10,
                "title_hint": "Chương 10: Sắc Đỏ Sàn Diễn",
                "outline": "Hải đoạt giải Nhà thiết kế xuất sắc nhất năm của Vietnam Fashion Week. Phía sau cánh gà sân khấu rực rỡ ánh đèn, Huyền chủ động bày tỏ tình yêu kiên định, tự nguyện sòng phẳng với Hải."
            }
        ]
    },
    {
        "id": 2190,
        "title": "Thần Tài Chứng Khoán Phố Wall Hà Nội",
        "author": "Hoàng Đức Minh",
        "genre": "Sảng Văn",
        "intro": "<p><strong>Hoàng Đức Minh bị giám đốc quỹ đầu tư sa thải nhục nhã dưới chân sàn HNX, vu khống anh thao túng cổ phiếu để cướp trắng tài sản và tài khoản giao dịch của khách hàng.</strong></p><p>Thế nhưng họ không ngờ, sự xuất hiện của Phan Thị Bảo Châu – Phó Chủ tịch UBCKNN – đã cùng Minh bóc trần đường dây pump-and-dump rửa tiền tinh vi của phe phản diện...</p>",
        "cover_prompt": "highly detailed book cover, professional anime style, a handsome Vietnamese financial analyst analyzing trading stocks graphs on multiple digital screens, a beautiful intelligent female regulator in a luxury suit beside him, stock exchange background",
        "chapters_outline": [
            {
                "chap_num": 1,
                "title_hint": "Chương 1: Sa Thải Dưới Chân HNX",
                "outline": "Hoàng Đức Minh bị giám đốc quỹ đầu tư hống hách sa thải nhục nhã ngay trước cổng HNX phố Đinh Lễ, vu khống anh thao túng giá cổ phiếu để chiếm đoạt tài sản khách hàng. Minh thề sẽ khiến họ trả giá."
            },
            {
                "chap_num": 2,
                "title_hint": "Chương 2: Nữ Phó Chủ Tịch UBCKNN",
                "outline": "Phan Thị Bảo Châu - Phó Chủ tịch UBCKNN, nghi ngờ có khuất tất đằng sau vụ việc nên tiếp cận Minh. Cô muốn làm sạch thị trường chứng khoán khỏi các nhóm lợi ích thao túng bất hợp pháp."
            },
            {
                "chap_num": 3,
                "title_hint": "Chương 3: Thử Thách Thuật Toán",
                "outline": "Châu đặt ra thử thách cực kỳ khắc nghiệt: Minh phải dự báo chính xác dòng tiền khối ngoại và điểm số phiên phái sinh biến động cực mạnh của sàn HOSE/HNX trong vòng 24 giờ bằng thuật toán định lượng tự viết."
            },
            {
                "chap_num": 4,
                "title_hint": "Chương 4: Bẫy Tài Khoản Khống",
                "outline": "Đối thủ mạo danh chữ ký của Minh, lén lút lập hàng chục tài khoản khống tại các công ty chứng khoán để thực hiện các giao dịch quay tay, thao túng giá trị cổ phiếu nhằm đổ oan cho anh."
            },
            {
                "chap_num": 5,
                "title_hint": "Chương 5: Khủng Hoảng Triệu Tập C03",
                "outline": "C03 cảnh sát kinh tế triệu tập Minh điều tra khẩn cấp. Quỹ đầu tư phản diện đăng tải hàng loạt bài báo bôi nhọ Minh là kẻ lừa đảo hàng trăm nhà đầu tư nhẹ dạ, khiến dư luận phẫn nộ dữ dội."
            },
            {
                "chap_num": 6,
                "title_hint": "Chương 6: Bóc Trần Algorithmic Pump",
                "outline": "Giữa cơn bão điều tra, Minh dùng máy tính định lượng phân tích sâu logs dữ liệu lệnh giao dịch, chỉ ra địa chỉ IP nguồn phát lệnh giao dịch khống xuất phát trực tiếp từ văn phòng của gã giám đốc phản diện. [Vả mặt lần 1: Đập tan cáo buộc lừa đảo, C03 chuyển hướng sang điều tra quỹ phản diện]."
            },
            {
                "chap_num": 7,
                "title_hint": "Chương 7: Đối Thủ Liên Minh Tài Phiệt Ngân Hàng",
                "outline": "Gã giám đốc quỹ liên minh với một tài phiệt ngân hàng thương mại lớn, dùng sức mạnh tiền tệ mua chuộc các đơn vị truyền thông bẩn bôi nhọ Minh sử dụng thuật toán gián điệp để phá hoại an ninh tài chính quốc gia."
            },
            {
                "chap_num": 8,
                "title_hint": "Chương 8: Cuộc Điều Tra Của Cục An Ninh Mạng A05",
                "outline": "Cục An ninh mạng A05 Bộ Công an vào cuộc phong tỏa toàn bộ máy chủ và mã nguồn thuật toán của Minh để làm rõ cáo buộc phá hoại an ninh tài chính."
            },
            {
                "chap_num": 9,
                "title_hint": "Chương 9: Trích Xuất File Log Nội Gián",
                "outline": "Minh cực kỳ điềm tĩnh cộng tác với A05, giúp các chiến sĩ an ninh trích xuất file log truy cập từ máy chủ ngân hàng của đối thủ vào hệ thống thông tin của UBCKNN để thực hiện hành vi giao dịch nội gián trục lợi bất chính."
            },
            {
                "chap_num": 10,
                "title_hint": "Chương 10: Chiến Dịch Short Squeeze Lịch Sử",
                "outline": "Được sự chấp thuận kỹ thuật từ Châu, Minh kích hoạt một đợt ép bán khống (short squeeze) dữ dội đối với mã cổ phiếu của ngân hàng phản diện ngay trên sàn giao dịch, đẩy giá cổ phiếu tăng kịch trần liên tục, khiến đối thủ cháy tài khoản hàng ngàn tỷ đồng."
            },
            {
                "chap_num": 11,
                "title_hint": "Chương 11: Ngày Phán Quyết UBCKNN",
                "outline": "UBCKNN công bố quyết định phong tỏa khẩn cấp tài khoản và đình chỉ hoạt động quỹ đầu tư phản diện. Lực lượng C03 Bộ Công an ập vào bắt giữ ban lãnh đạo phản diện ngay trên sàn HNX sầm uất."
            },
            {
                "chap_num": 12,
                "title_hint": "Chương 12: Phanh Phui Đường Dây Thao Túng",
                "outline": "Đường dây thao túng chứng khoán và rửa tiền của liên minh ngân hàng thương mại và quỹ đầu tư bẩn bị bóc trần hoàn toàn trước công luận."
            },
            {
                "chap_num": 13,
                "title_hint": "Chương 13: Vinh Quang Phục Hồi",
                "outline": "Minh trở thành Cố vấn tối cao của UBCKNN, được bồi thường danh dự và khôi phục toàn bộ tài sản. [Vả mặt lần 2: Đập tan hoàn toàn liên minh tài phiệt ngân hàng và quỹ bẩn, thanh lọc phố Wall Hà Nội]."
            },
            {
                "chap_num": 14,
                "title_hint": "Chương 14: Bình Yên Phố Đinh Lễ",
                "outline": "Dưới hàng cây cổ thụ xanh mát phố Đinh Lễ, Châu chủ động bày tỏ tình cảm chân thành tự nguyện, cam kết gắn bó sòng phẳng kiên định với Minh."
            }
        ]
    },
    {
        "id": 2052,
        "title": "Thần Y Phòng Khám Quận 5: Vợ Tôi Là Siêu Tỷ Phú",
        "author": "Lâm Trần",
        "genre": "Sảng Văn",
        "intro": "<p><strong>Lâm Trần bị Trưởng khoa Hoàng Vĩnh cướp công trình nghiên cứu tái tạo tế bào gan, khóa tài khoản Techcombank và ném hành lý ra đường Nguyễn Trãi Quận 5 dưới mưa tầm tã.</strong></p><p>Thế nhưng hắn không ngờ, xe Porsche Panamera của Trịnh Minh Thư – ái nữ tập đoàn y tế Trịnh Gia – đã đỗ trước mặt anh. Với y thuật châm cứu thần sầu và sự đồng hành của cô, Lâm Trần từng bước bước lên đỉnh cao y học...</p>",
        "cover_prompt": "highly detailed book cover, professional anime style, a handsome young Vietnamese doctor holding an ancient silver needle, standing next to a beautiful wealthy female heiress in a premium blazer, traditional medical clinic interior background",
        "chapters_outline": [
            {
                "chap_num": 1,
                "title_hint": "Chương 1: Kẻ Ăn Cắp Công Trình",
                "outline": "Lâm Trần bị Trưởng khoa Hoàng Vĩnh cướp đoạt công trình nghiên cứu đông y Nam dược tái tạo gan tại phòng khám đa khoa An Tâm ở Quận 5. Hoàng Vĩnh đuổi Lâm Trần đi, khóa tài khoản Techcombank của anh, ném hành lý của anh ra đường Nguyễn Trãi dưới mưa."
            },
            {
                "chap_num": 2,
                "title_hint": "Chương 2: Mỹ Nhân Porsche Thách Thức",
                "outline": "Trịnh Minh Thư đón Lâm Trần dưới mưa bằng xe Porsche Panamera. Khi gã vệ sĩ của cô bị ngộ độc cấp tính cực nguy kịch, Lâm Trần cực kỳ bình tĩnh dùng châm bạc gia truyền châm cứu chính xác các đại huyệt để ổn định nhịp tim và giữ mạng sống kỳ tích."
            },
            {
                "chap_num": 3,
                "title_hint": "Chương 3: Thách Thức Ca Bệnh Nan Y",
                "outline": "Minh Thư thách thức Lâm Trần chữa chứng tê liệt chi dưới cho một tỷ phú. Anh châm cứu chẩn trị thần kỳ giúp bệnh nhân cử động lại chân, khiến Thư nể phục tuyệt đối và chuyển ngay 5 tỷ VNĐ mở phòng khám Nhân Y Đường Quận 5."
            },
            {
                "chap_num": 4,
                "title_hint": "Chương 4: Nhân Y Đường Cứu Người",
                "outline": "Nhân Y Đường thu hút bệnh nhân nghèo nhờ chính sách y đức của Lâm Trần. Ông Sáu chạy xe ôm bị xơ gan cổ trướng giai đoạn cuối từng bị An Tâm đuổi đi, tìm đến đây thoi thóp và được Lâm Trần cứu sống bằng phác đồ Nam dược bài bản."
            },
            {
                "chap_num": 5,
                "title_hint": "Chương 5: Khủng Hoảng Truyền Thông Bẩn",
                "outline": "Hoàng Vĩnh thuê báo chí bẩn vu khống Nhân Y Đường dùng thảo dược chứa thạch tín gây ngộ độc. Phòng khám bị đình chỉ 24 giờ để phục vụ công tác thanh tra điều tra."
            },
            {
                "chap_num": 6,
                "title_hint": "Chương 6: Thanh Danh Khôi Phục",
                "outline": "Lâm Trần cực kỳ điềm tĩnh họp báo, công bố kết quả kiểm nghiệm sạch từ Viện Dược liệu quốc gia. Các bài báo bẩn bị gỡ bỏ, đối thủ bị phạt nặng vì hành vi cạnh tranh không lành mạnh. [Vả mặt lần 1: Đập tan cáo buộc thạch tín, khôi phục uy tín Nhân Y Đường]."
            },
            {
                "chap_num": 7,
                "title_hint": "Chương 7: Quyết Định Từ Hiệp Hội Y Học",
                "outline": "Hoàng Vĩnh hoảng sợ, cầu cứu gã phó chủ tịch Hiệp hội Y học cổ truyền là bác ruột của hắn. Gã này ra văn bản khẩn cấp tước chứng chỉ hành nghề y học cổ truyền của Lâm Trần vì lý do anh không có bằng cấp học thuật chính quy."
            },
            {
                "chap_num": 8,
                "title_hint": "Chương 8: Thách Thức Kiểm Tra Lâm Sàng",
                "outline": "Thư dùng ảnh hưởng pháp lý của Trịnh Gia, buộc Hiệp hội phải tổ chức một buổi kiểm tra lâm sàng trực tiếp dưới sự giám sát của đại diện Bộ Y tế để Lâm Trần chứng minh thực lực của mình."
            },
            {
                "chap_num": 9,
                "title_hint": "Chương 9: Trận Chiến Y Học Sấm Sét",
                "outline": "Tại buổi kiểm tra lâm sàng, Lâm Trần thực hiện châm cứu cứu sống một bệnh nhân bị tai biến liệt toàn thân thoi thóp ngay trước mặt toàn bộ hội đồng y khoa, khiến các giáo sư đầu ngành phải đứng dậy vỗ tay khâm phục."
            },
            {
                "chap_num": 10,
                "title_hint": "Chương 10: Độc Chất TX-9 Ám Hại",
                "outline": "Kẻ phản diện Hoàng Vĩnh điên cuồng vì mất hết danh dự và cơ hội, lén lút mua chuộc hộ lý đầu độc bố đẻ của Minh Thư là Chủ tịch Trịnh Gia bằng độc chất sinh học TX-9 tàn phá gan cực nhanh ngay khi ông nằm viện dưỡng bệnh."
            },
            {
                "chap_num": 11,
                "title_hint": "Chương 11: Cận Kề Cái Chết",
                "outline": "Ông Hùng uống nước xong ho ra máu đen ngã quỵ, tim ngừng đập tạm thời. Hoàng Vĩnh lập tức dẫn cảnh sát ập vào đòi niêm phong Nhân Y Đường và bắt giam Lâm Trần vì tội cố ý đầu độc ngộ sát."
            },
            {
                "chap_num": 12,
                "title_hint": "Chương 12: Kim Bạc Cướp Mạng Sống",
                "outline": "Lâm Trần hoàn toàn điềm tĩnh, dùng 15 cây kim bạc châm cứu liên hoàn vào các đại huyệt Kỳ Môn, Chương Môn, giữ chặt dòng khí huyết và ép độc tố TX-9 đào thải ra ngoài dưới dạng chất lỏng màu đen, cứu mạng Chủ tịch thần kỳ trước sự sững sờ của các bác sĩ Tây y."
            },
            {
                "chap_num": 13,
                "title_hint": "Chương 13: Đoạn Băng Tố Cáo Tội Ác",
                "outline": "Minh Thư công bố đoạn video từ camera ẩn ghi lại toàn bộ hành vi gã hộ lý nhận tiền từ Hoàng Vĩnh và lén bỏ độc chất TX-9 vào bình nước của bố cô."
            },
            {
                "chap_num": 14,
                "title_hint": "Chương 14: Ngày Phán Xét Quận 5",
                "outline": "Cảnh sát kinh tế và an ninh ập vào bắt giữ Hoàng Vĩnh và gã phó chủ tịch Hiệp hội y học đồng phạm vì tội cố ý giết người và nhận hối lộ. Phòng khám An Tâm bị đóng cửa vĩnh viễn. [Vả mặt lần 2: Đập tan hoàn toàn Hoàng Vĩnh và thế lực bảo đỡ, thâu tóm toàn bộ y học Quận 5]."
            },
            {
                "chap_num": 15,
                "title_hint": "Chương 15: Cổ Đông Hôn Ước",
                "outline": "Trong vườn hoa Nhân Y Đường Quận 5 ngập tràn ánh hoàng hôn ấm áp, Thư sòng phẳng trao hợp đồng sở hữu 50% cổ phần tập đoàn y tế Trịnh Gia cho Lâm Trần, chủ động bày tỏ tình cảm chân thành tự nguyện và tuyên bố đính ước ngọt ngào."
            }
        ]
    }
]

# Apply to generate_and_deploy_10_novels.py
target_file = "/Users/aaronnguyen/TN/App/doctieuthuyet/scratch/generate_and_deploy_10_novels.py"

with open(target_file, "r", encoding="utf-8") as f:
    content = f.read()

# Locate standard block
pattern_start = "NOVELS = ["
pattern_end = "def load_progress():"

start_idx = content.find(pattern_start)
end_idx = content.find(pattern_end)

if start_idx == -1 or end_idx == -1:
    print("❌ Could not locate boundary patterns in target file!")
    exit(1)

# Format the list of novels nicely
novels_str = "NOVELS = " + json.dumps(NOVELS, ensure_ascii=False, indent=4) + "\n\n"

# Perform replacement
new_content = content[:start_idx] + novels_str + content[end_idx:]

with open(target_file, "w", encoding="utf-8") as f:
    f.write(new_content)

print("✓ Successfully replaced NOVELS definition with the new dynamic multi-slap structure!")
