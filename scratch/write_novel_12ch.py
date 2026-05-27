# -*- coding: utf-8 -*-
import json
import os

def main():
    novel_data = {
        "title": "Bị Cướp Trang Trại Mật Ong, Tôi Dùng Một Giọt Mật Vả Sập Tập Đoàn Nghìn Tỷ",
        "author": "Vũ Triệu Đăng",
        "genre": "Sảng Văn",
        "intro": (
            '<p><strong>"Bàn tay bẩn thỉu đầy vết ong đốt của anh không đáng chạm vào chiếc váy cưới Vera Wang trăm triệu của tôi! Kẻ dầm mưa dãi nắng cày cuốc cả đời như anh chỉ cản bước tôi lọt vào giới thượng lưu Hà Thành!"</strong></p>\n'
            '<p>Vị hôn thê Lương Mỹ Hạnh tháo nhẫn đính hôn ném thẳng vào mặt Triệu Hải Đăng ngay giữa ngày anh bị người bạn thân Hoàng Duy Khang vu oan chiếm đoạt vốn và đuổi cổ khỏi trang trại mật ong bạc hà Đồng Văn dưới đêm giông bão tuyết rơi buốt giá của Hà Giang. Chúng cướp đoạt công thức tách nước giữ nguyên enzym mật ong bạc hà tự nhiên cả đời anh nghiên cứu để dâng cho tập đoàn VietHoney hòng niêm yết IPO tỷ đô.</p>\n'
            '<p>Bị tống cổ khỏi cao nguyên đá trong tay trắng, Đăng ngỡ như mất hết tất cả. Nhưng hắn không ngờ, mật ong hữu cơ trong tay anh không phải là thứ "thô sơ lỗi thời", mà là thần dược tối cao! Được Nguyễn Khánh An - nữ chủ tịch sắc lạnh, lý tính của Vạn An Capital chống sau lưng, Đăng lập nên "Đế chế Mật Ong Vạn An", dùng công nghệ truy xuất nguồn gốc số hóa tổ ong, báo cáo kiểm toán Big 4 EY vạch trần đường dây mật ong hóa chất của kẻ phản bội, cùng sắc lệnh điều tra từ C03 Bộ Công an để đẩy chúng xuống vực thẳm.</p>\n'
            '<p><strong>Chúng từng gọi anh là gã nuôi ong đê tiện, cho đến khi cả Triển lãm Nông nghiệp Quốc tế phải cúi đầu run rẩy xin anh chia sẻ một giọt mật ong cứu sống uy tín của cả ngành xuất khẩu Việt Nam!</strong></p>'
        ),
        "chapters": []
    }

    # Chapter 1
    ch1 = """<p>Gió mùa đông bắc tràn qua vách đá cao nguyên Đồng Văn rít lên từng hồi ghê rợn như tiếng gào thét của loài quái thú cổ xưa. Tuyết rơi lất phất trộn lẫn với những hạt mưa đá lạnh buốt, gõ chan chát vào mái tôn của trang trại nuôi ong công nghệ cao bạc hà Hà Giang.</p>
<p>Triệu Hải Đăng đứng lặng im giữa căn phòng điều khiển trung tâm, đôi bàn tay gầy guộc chằng chịt những vết sẹo do ong đốt rỉ ra những vệt mồ hôi lạnh ngắt dưới ánh đèn neon vàng vọt nhấp nháy. Mắt anh đỏ ngầu, dán chặt vào tờ biên bản kiểm toán tài sản và lệnh trục xuất do chính người bạn thân nối khố Hoàng Duy Khang đặt lên bàn.</p>
<p>“Triệu Hải Đăng, ký đi. Đây là lối thoát duy nhất để mày giữ lại cái mạng quèn của mình,” Khang mở nút chai rượu mạnh cao cấp, hớp một ngụm rồi mỉa mai, đôi mắt sắc lạnh và đầy dối trá.</p>
<p>“Khang! Trang trại mật ong bạc hà hữu cơ này là mồ hôi, là máu của tao ròng rã sáu năm qua! Mày cướp sạch công thức tách nước chân không giữ nguyên enzym tự nhiên của tao, giờ còn muốn tống cổ tao đi dưới đêm tuyết lạnh thế này?” Giọng Đăng nghẹn lại, lồng ngực phập phồng kịch liệt, nhịp tim đập dồn dập đến mức tai anh ù đi.</p>
<p>Đột nhiên, cánh cửa gỗ bật mở. Lương Mỹ Hạnh - vị hôn thê mà anh nâng niu suốt ba năm bước vào, khoác trên mình chiếc áo lông thú đắt tiền, đi bên cạnh là hai gã bảo vệ cao lớn mặc vest đen lạnh lùng.</p>
<p>Cô nhìn anh bằng ánh mắt khinh miệt tột cùng, dứt khoát tháo chiếc nhẫn bạc đính hôn ném thẳng vào vũng nước bùn dưới chân anh: “Bàn tay bẩn thỉu đầy vết ong đốt của anh không đáng chạm vào chiếc váy cưới Vera Wang trăm triệu của tôi! Kẻ dầm mưa dãi nắng cày cuốc cả đời như anh chỉ cản bước tôi lọt vào giới thượng lưu Hà Thành!”</p>
<p>“Mỹ Hạnh... cả cô cũng phản bội tôi?” Đăng lảo đảo lùi lại, va vào chiếc máy ly tâm lạnh ngắt.</p>
<p>“Phản bội? Không, tôi chỉ chọn tương lai sáng lạn hơn,” Mỹ Hạnh cười khẩy đầy kiêu ngạo. “Anh Khang đã đồng ý dùng công thức tách nước của anh để liên doanh với tập đoàn hóa chất thực phẩm đa quốc gia VietHoney, thổi phồng dòng tiền để IPO nghìn tỷ trên sàn chứng khoán. Còn anh? Suốt ngày chỉ biết cắm đầu vào tổ ong, ôm mộng hữu cơ thuần tự nhiên chậm chạp, bảo thủ!”</p>
<p>“Mật ong bạc hà nguyên chất Đồng Văn mà dùng hóa chất tạo hương và đường ngô cao phân tử để sản xuất hàng loạt sẽ biến thành thuốc độc phá hủy uy tín nông sản Việt Nam!” Đăng hét lên trong phẫn nộ.</p>
<p>“Câm mồm!” Duy Khang bước tới đập mạnh tập hồ sơ xuống bàn, chỉ thẳng mặt anh. “Người đại diện pháp luật của trang trại hiện tại là tao, con dấu là do Mỹ Hạnh ký bàn giao. Ký tên khước từ quyền tác giả và cút khỏi Hà Giang ngay lập tức, nếu không tao sẽ báo cảnh sát vu oan cho mày tội phá hoại tài sản công nghệ cao!”</p>
<p>Dưới sự cưỡng ép tàn nhẫn, Đăng nghiến răng nghiến lợi ký tên lên tờ giấy trắng. Anh bị hai gã bảo vệ kéo lê ra khỏi trang trại, ném thẳng chiếc ba lô sờn cũ chứa ổ cứng di động vào bùn tuyết lạnh ngắt.</p>
<p>Đêm đông Hà Giang lạnh buốt xương tủy, Đăng quỳ rạp dưới đất nhặt chiếc ổ cứng lên, nước mưa hòa lẫn nước mắt. Anh nhìn lại trang trại rực rỡ ánh đèn đằng xa, hàm răng cắn chặt đến rỉ máu: “Hoàng Duy Khang! Lương Mỹ Hạnh! Các người cướp đi hoài bão của tôi, biến mật ong bạc hà quý giá thành thứ hóa chất độc hại hại người. Tôi thề... có một ngày tôi sẽ trở lại, bắt các người phải quỳ sụp dưới chân cao nguyên này để đền tội!”</p>"""

    # Chapter 2
    ch2 = """<p>Sáng hôm sau, mưa tuyết đã ngớt nhưng cái lạnh cắt da cắt thịt của cao nguyên đá vẫn bao trùm lấy thị trấn cổ Đồng Văn. Triệu Hải Đăng với chiếc ba lô sờn rách, bước đi vô định bên đèo Mã Pí Lèng, nơi những vách đá dựng đứng cheo leo giữa mây ngàn.</p>
<p>Đột nhiên, một tiếng phanh xe chói tai vang lên từ phía khúc cua hiểm trở. Chiếc xe SUV Mercedes-Benz G63 màu đen bóng loạng khựng lại sát sườn núi. Cửa xe mở ra, một gã tài xế trung niên hốt hoảng kêu cứu: “Có ai không? Cứu mạng! Chủ tịch của tôi lên cơn hen suyễn tắc nghẽn phổi cấp tính rồi, thuốc xịt dự phòng bị rơi xuống vực khi va chạm!”</p>
<p>Đăng lập tức lao tới. Trên băng ghế sau xe, một người đàn ông lớn tuổi mặc âu phục sang trọng đang co quắp, khuôn mặt tím tái không còn giọt máu, hai tay bấu chặt lấy cổ họng thở khò khè, nhịp thở đứt quãng vô cùng nguy kịch. Đó chính là Nguyễn Vạn An - siêu tỷ phú đứng đầu tập đoàn Vạn An Group.</p>
<p>“Tránh ra, để tôi!” Đăng lớn tiếng ra lệnh đầy quyết đoán, mở chiếc ba lô sờn cũ rút ra một chai mật ong bạc hà tự nhiên nguyên chất màu xanh ô-liu nhạt – giọt mật cuối cùng anh mang theo từ trang trại.</p>
<p>Anh nhẹ nhàng nhưng dứt khoát bấm mạnh vào huyệt phế du và thiên đột trên cổ ông cụ để giảm co thắt phổi, đồng thời nhỏ từng giọt mật ong bạc hà nguyên chất đậm đặc enzym tự nhiên vào miệng ông. Mật ong bạc hà hữu cơ Hà Giang chứa hàm lượng chất chống viêm tự nhiên cực cao và enzym quý hiếm lập tức làm dịu lớp niêm mạc phế quản đang sưng tấy.</p>
<p>Chỉ trong ba phút nghẹt thở, tiếng khò khè kinh hoàng dịu đi. Ông cụ hít được một hơi thật sâu, đôi mắt dần có lại thần sắc, da mặt hồng hào trở lại dưới sự kinh ngạc tột cùng của gã tài xế.</p>
<p>“Cảm ơn cậu... Cổ họng tôi dịu hẳn rồi. Cậu thực sự đã kéo tôi từ cõi chết trở về,” Nguyễn Vạn An khó nhọc cất tiếng, gương mặt hiện rõ vẻ biết ơn sâu sắc dành cho người thanh niên trẻ tuổi nghèo khó trước mắt.</p>"""

    # Chapter 3
    ch3 = """<p>Tiếng trực thăng y tế cánh quạt rít mạnh xé toạc không gian sương mù đèo Mã Pí Lèng. Nguyễn Khánh An – nữ chủ tịch điều hành sắc lạnh, lý tính của Vạn An Capital bước xuống, bộ vest công sở gọn gàng cùng đôi mắt sắc sảo lập tức khóa chặt lấy Hải Đăng.</p>
<p>“Cha! Cha có sao không?” Khánh An lo lắng đỡ lấy Nguyễn Vạn An. Khi nghe tài xế kể lại toàn bộ sự việc, cô hướng ánh mắt nghi ngờ về phía Đăng, nhìn chiếc ba lô sờn rách và chai mật ong thô sơ trên tay anh.</p>
<p>“Phương pháp cấp cứu bằng Đông y này quá mạo hiểm. Một chai mật ong tự chế không nhãn mác, không chứng nhận lâm sàng của Bộ Y tế làm sao có thể bảo đảm an toàn cho tính mạng của cha tôi?” Khánh An thẳng thắn chất vấn, giọng nói vô cùng lạnh lùng, lý tính.</p>
<p>Đăng không hề e sợ, anh đứng thẳng người, đối diện trực tiếp với ánh mắt lạnh lẽo của cô: “Khoa học Đông y không phải là trò may rủi. Mật ong bạc hà hữu cơ Đồng Văn có hàm lượng hoạt chất kháng viêm tự nhiên cao gấp nhiều lần mật ong thường, cắt cơn co thắt phế quản cấp tốc ngay tại thực địa. Cô có thể đưa mẫu mật này đến bất kỳ phòng lab độc lập nào để xét nghiệm trước khi đưa ra phán xét cảm tính.”</p>
<p>Khánh An khẽ nhíu mày trước thái độ tự tin, cứng cỏi của anh. Cô lập tức ra hiệu cho trợ lý cất giữ chai mật ong: “Được. Tôi sẽ đưa mẫu mật này về Viện Kiểm nghiệm Trung ương xét nghiệm độc lập. Nếu kết quả kiểm định sinh hóa đạt chuẩn và chứng minh được hiệu quả sinh học thực tế, tôi mới bàn bạc về việc đầu tư hay hỗ trợ anh. Ở Vạn An Capital, mọi quyết định đầu tư đều dựa trên số liệu thực tế, không dựa trên lòng biết ơn cảm tính.”</p>
<p>Đăng khẽ mỉm cười: “Rất tốt. Tôi tôn trọng sự lý tính của cô. Hẹn gặp lại khi kết quả kiểm nghiệm chứng minh tôi đúng.”</p>"""

    # Chapter 4
    ch4 = """<p>Ba ngày sau, tại văn phòng Vạn An Capital ở Hà Nội, Nguyễn Khánh An đặt bản báo cáo phân tích sinh hóa lên bàn trước mặt Triệu Hải Đăng. Đôi mắt cô không còn sự nghi ngờ mà thay vào đó là sự kinh ngạc sâu sắc.</p>
<p>“Hàm lượng enzym hoạt tính tự nhiên và các chất kháng viêm hữu cơ trong mẫu mật của anh vượt trội hoàn toàn so với các chỉ số tiêu chuẩn. Kết quả thử nghiệm lâm sàng độc lập hoàn hảo,” Khánh An đan hai tay vào nhau, phong thái vô cùng chuyên nghiệp.</p>
<p>“Tôi đồng ý giải ngân đợt một 50 tỷ đồng. Tuy nhiên, chúng ta sẽ bắt đầu từ một trang trại thử nghiệm nhỏ tại thung lũng đá Đồng Văn để kiểm soát rủi ro chất lượng, chứ chưa thể xây dựng quy mô lớn ngay lập tức. Anh có đồng ý với lộ trình kiểm soát ròng này không?”</p>
<p>“Tôi đồng ý. Mật ong hữu cơ cần thời gian để đàn ong thích nghi với môi trường tự nhiên, vội vã tăng quy mô chỉ làm hỏng chất lượng cốt lõi,” Đăng gật đầu đồng tình sòng phẳng.</p>
<p>Với nguồn vốn ban đầu, Đăng quay trở lại cao nguyên đá, dựng lên vài chục thùng ong thông minh IoT đầu tiên tại một thung lũng hoang sơ. Anh tự tay lắp đặt cảm biến, dọn dẹp cỏ dại, chăm sóc từng đàn ong dưới cái lạnh buốt giá. Không có sự hào nhoáng nhanh chóng, chỉ có sự kiên trì bền bỉ của một người thợ lành nghề bám đất giữ rừng.</p>"""

    # Chapter 5
    ch5 = """<p>Trong khi Đăng đang lặng lẽ xây dựng nền móng, Hoàng Duy Khang và Lương Mỹ Hạnh tại tập đoàn VietHoney bắt đầu tung đòn chèn ép tàn nhẫn để độc chiếm nguồn cung nguyên liệu của vùng cao nguyên đá.</p>
<p>Duy Khang cấu kết với một số đầu nậu địa phương, tung nguồn vốn lớn để ép buộc toàn bộ các hộ nuôi ong nhỏ lẻ tại Đồng Văn ký hợp đồng độc quyền giá rẻ mạt. Chúng đe dọa sẽ phong tỏa đường ra của nông sản nếu họ dám bán mật cho các đơn vị độc lập khác.</p>
<p>“Khang, chúng ta phải triệt tiêu hoàn toàn đường sống của thằng Đăng ngay từ trong trứng nước,” Mỹ Hạnh lạnh lùng nói trong phòng họp VietHoney. “Không được để trang trại nhỏ của nó thu mua được bất kỳ giọt mật nguyên chất nào từ người dân bản địa.”</p>
<p>VietHoney bắt đầu phân phối dòng mật ong giả trộn si-rô đường ngô và hóa chất hương liệu bạc hà ra thị trường với giá rẻ mạt, tạo áp lực khủng khiếp lên giá mật ong truyền thống của Hà Giang, đẩy những người nông dân nuôi ong chân chính vào bước đường cùng cực.</p>"""

    # Chapter 6
    ch6 = """<p>Giữa cơn bão chèn ép giá của VietHoney, gia đình ông Sình – một hộ nuôi ong lâu đời người Mông tại bản Lũng Cú – đang đứng trước nguy cơ phá sản khi toàn bộ 50 thùng ong bị VietHoney từ chối thu mua do ông không chấp nhận pha đường vào mật theo yêu cầu của chúng.</p>
<p>Biết tin, Triệu Hải Đăng lập tức vượt đường đèo đá hiểm trở tìm đến tận nhà ông Sình. Nhìn thấy ông cụ khắc khổ đang đau đớn nhìn đàn ong chết dần vì thiếu kinh phí chăm sóc, Đăng không hề ngần ngại.</p>
<p>“Bác Sình, cháu sẽ thu mua toàn bộ số mật nguyên chất này của bác với giá gấp đôi mức giá ép của VietHoney,” Đăng dứt khoát nói, tự tay giúp ông cụ di chuyển các thùng ong tránh rét.</p>
<p>“Nhưng cậu Đăng ơi, VietHoney thế lực lớn lắm, họ sẽ chặn đường vận chuyển của cậu,” ông Sình lo lắng run rẩy nói.</p>
<p>“Bác yên tâm, cháu dùng công nghệ quét mã QR định vị vệ tinh và blockchain của Vạn An để niêm phong xuất xứ trực tiếp tại vườn. Người tiêu dùng quốc tế sẽ mua trực tiếp từ bác thông qua hệ thống của cháu. Chúng ta liên kết lại, không kẻ gian thương nào có thể bẻ gãy được danh dự của người nuôi ong Đồng Văn!”</p>
<p>Hành động nghĩa khí và sự hỗ trợ công nghệ thực tế của Đăng đã sưởi ấm trái tim người dân cao nguyên đá. Hàng chục hộ nuôi ong nghèo khác trong bản lập tức tình nguyện rút khỏi liên minh của VietHoney, mang thùng ong về hợp tác cùng trang trại thông minh của Đăng, tạo nên một cộng đồng liên kết vô cùng bền vững xung quanh anh.</p>"""

    # Chapter 7
    ch7 = """<p>Sự trỗi dậy của liên minh nông dân xung quanh Triệu Hải Đăng khiến Hoàng Duy Khang vô cùng điên tiết. Gã quyết định dùng đòn chí mạng về pháp lý và truyền thông để nghiền nát Đăng.</p>
<p>Duy Khang gửi đơn kiện khẩn cấp lên Sở Khoa học và Công nghệ tỉnh, cáo buộc trang trại Vạn An vi phạm bản quyền công nghệ tách nước chân không mà gã đã đăng ký sở hữu trí tuệ trước đó dưới tên VietHoney.</p>
<p>Đồng thời, chúng thuê hàng loạt tài khoản ảo trên mạng xã hội tung tin đồn ác ý: “Mật ong bạc hà Vạn An nhiễm độc chì nặng do nguồn nước từ vách đá biên giới bị ô nhiễm, gây nguy hiểm nghiêm trọng cho sức khỏe người tiêu dùng!”</p>
<p>Cơn bão truyền thông bẩn lập tức quét qua các diễn đàn kinh tế, đẩy trang trại non trẻ của Đăng vào cuộc khủng hoảng danh tiếng vô cùng nghiêm trọng trước sự ngỡ ngàng của dư luận.</p>"""

    # Chapter 8
    ch8 = """<p>Áp lực từ cơn bão truyền thông bẩn bắt đầu lan rộng tới tận phòng hội đồng quản trị của Vạn An Capital tại Hà Nội. Nhiều cổ đông lớn lo ngại rủi ro pháp lý đã liên tục gây sức ép buộc Nguyễn Khánh An phải rút vốn khỏi dự án cao nguyên đá Đồng Văn.</p>
<p>“Khánh An, thương hiệu Vạn An không thể gắn liền với một dự án đang bị kiện tụng và smear độc chì trên khắp mặt báo!” Một cổ đông lớn đập bàn giận dữ trong cuộc họp khẩn.</p>
<p>Giữa lúc đó, tin dữ tiếp tục ập đến từ cảng Hải Phòng: Lô hàng container 10 tấn mật ong bạc hà xuất khẩu đầu tiên của Đăng đi thị trường Nhật Bản đã bị cơ quan hải quan tạm đình chỉ thông quan để chờ kết quả giám định độc lập về cáo buộc nhiễm chì.</p>
<p>Khánh An đứng trước gọng kìm áp lực khổng lồ, nhưng đôi mắt cô vẫn sắc lạnh, lý tính: “Tôi chịu hoàn toàn trách nhiệm cá nhân về khoản đầu tư này. Trước khi có kết quả xét nghiệm mẫu đối chứng từ phòng lab Thụy Sĩ, không ai được phép rút một đồng vốn nào khỏi công trường của Vũ Triệu Đăng!”</p>
<p>Tại Đồng Văn, Đăng đứng lặng im nhìn container bị niêm phong dưới mưa gió, lòng kiên định không hề lay chuyển. Anh biết, đây chính là thời khắc thử thách lớn nhất để anh lật bài ngửa với kẻ phản bội.</p>"""

    # Chapter 9
    ch9 = """<p>“Đăng, chúng ta chỉ còn 24 giờ trước khi VietHoney tổ chức họp báo công bố ký hợp đồng xuất khẩu tỷ đô và chính thức gõ búa IPO trên sàn chứng khoán,” Nguyễn Khánh An bay gấp từ Hà Nội lên Đồng Văn, mái tóc ngắn thấm đẫm sương đêm lạnh giá.</p>
<p>“Tôi đã chuẩn bị xong vũ khí để kết thúc trận chiến này,” Đăng lạnh lùng mở chiếc ổ cứng di động sờn cũ, cắm vào cổng kết nối máy chủ.</p>
<p>Màn hình hiển thị toàn bộ lịch sử commit Git gốc của công thức tách nước chân không sinh học từ năm 2022, được mã hóa bằng chữ ký số PGP cá nhân của anh không thể giả mạo. Cùng với đó là mẫu mật ong bạc hà hữu cơ nguyên chất thu hoạch từ ba năm trước được bảo quản lạnh hoàn hảo để làm mẫu đối chứng sinh học trực tiếp.</p>
<p>Đặc biệt, ông Sình và hàng chục hộ nông dân Đồng Văn đã đồng loạt ký vào biên bản làm chứng, vạch trần đường dây thu mua mật ong giả pha si-rô đường hóa chất của VietHoney.</p>
<p>“Mọi dữ liệu gốc và nhân chứng vật chứng đã đầy đủ. Hoàng Duy Khang đã tự đưa cổ vào thòng lọng khi dám công khai sản phẩm giả mạo trước toàn thể giới chuyên môn,” Đăng dứt khoát nói, ánh mắt rực sáng đầy quyết tâm vả mặt công khai.</p>"""

    # Chapter 10
    ch10 = """<p>Triển lãm Nông nghiệp Quốc tế tại Trung tâm Hội nghị Quốc gia Hà Nội diễn ra vô cùng hoành tráng và lộng lẫy dưới hàng ngàn ánh đèn chùm rực rỡ hắt ra từ sảnh lớn chính đón tiếp đối tác toàn cầu.</p>
<p>Hoàng Duy Khang và Lương Mỹ Hạnh đứng ở gian hàng trung tâm được trang hoàng lộng lẫy nhất của VietHoney, phong thái vô cùng hống hách và tự mãn cực hạn. Chúng liên tục nâng ly sâm banh đón chào các nhà đầu tư lớn chuẩn bị cho buổi gõ búa IPO nghìn tỷ diễn ra ngay sau đó.</p>
<p>“Chào mừng quý vị đến với thương hiệu mật ong bạc hà lớn nhất Việt Nam! Chúng tôi cam kết chất lượng sản lượng đạt 500 xuất khẩu!” Mỹ Hạnh dõng dạc giới thiệu đầy kiêu hãnh.</p>
<p>Đúng lúc đó, Triệu Hải Đăng và Nguyễn Khánh An cùng phái đoàn liên ngành bước vào sảnh chính. Đăng mặc bộ vest xám phẳng phiu lịch lãm, phong thái đĩnh đạc kiêu hùng bước đi giữa tiếng xôn xao kinh ngạc của cả hội trường triển lãm.</p>
<p>Duy Khang cười khẩy, bước tới chặn đường với ánh mắt khinh bỉ tột cùng: “Ồ, gã nuôi ong rách rưới Hải Đăng! Mày mang cái đống mật rác rưởi nhiễm chì của mày đến đây để cầu xin tao bố thí à?”</p>"""

    # Chapter 11
    ch11 = """<p>“Tôi đến đây để trả lại cho các người tất cả sự dối trá dơ bẩn này,” Triệu Hải Đăng dứt khoát nói, giọng nói trầm ổn vang dội khắp sảnh triển lãm rộng lớn.</p>
<p>Nguyễn Khánh An lập tức kết nối ổ cứng di động của Đăng lên màn hình LED khổng lồ 500 inch của hội trường chính. Toàn bộ lịch sử commit Git gốc có chữ ký số PGP khóa riêng của Đăng từ năm 2022 và bằng sáng chế độc quyền quốc tế hiện lên sắc nét, đè bẹp hoàn toàn cáo buộc vi phạm bản quyền của VietHoney.</p>
<p>Chưa dừng lại ở đó, đại diện kiểm toán Big 4 EY bước lên bục phát biểu, dõng dạc công bố báo cáo tài chính vạch trần đường đi của dòng tiền khống lừa đảo IPO trị giá 1.200 tỷ của VietHoney qua các công ty ma ở Singapore.</p>
<p>Đăng lạnh lùng lấy ra một máy đo quang phổ sinh học cầm tay, kiểm nghiệm trực tiếp mẫu mật của VietHoney ngay trên sân khấu trước sự chứng kiến của hàng trăm phóng viên báo chí trung ương: “Kết quả đo quang phổ hiển thị rõ ràng: 90% sản phẩm của VietHoney là si-rô đường ngô hóa chất, chứa dư lượng chất tạo hương độc hại vượt ngưỡng an toàn gấp 200 lần!”</p>
<p>Gương mặt Hoàng Duy Khang lập tức chuyển sang xám ngoét cắt không còn giọt máu, gã run rẩy ngã quỵ xuống sàn nhà. Lương Mỹ Hạnh bủn rủn cả chân tay, chiếc túi hiệu đắt tiền rơi xuống đất lả tả.</p>
<p>Đúng lúc đó, các chiến sĩ cảnh sát kinh tế thuộc C03 Bộ Công an bước vào hội trường, dõng dạc đọc lệnh bắt giữ khẩn cấp đối với Hoàng Duy Khang và Lương Mỹ Hạnh về hành vi lừa đảo tài chính, gian lận thương mại và hủy hoại an toàn thực phẩm nghiêm trọng.</p>
<p>Chiếc còng số 8 lạnh ngắt khóa chặt tay hai kẻ phản bội, kéo đi trong sự sỉ nhục, khinh bỉ tột cùng của toàn thể đối tác quốc tế và các cơ quan truyền thông báo chí lớn đang liên tục quay phim chụp ảnh trực tiếp.</p>"""

    # Chapter 12
    ch12 = """<p>Một tháng sau cơn địa chấn pháp lý chấn động cả ngành nông nghiệp sạch, cao nguyên đá Đồng Văn đã lấy lại vẻ thanh khiết, rực rỡ nguyên bản của nó.</p>
<p>Trang trại mật ong thông minh Vạn An lúc này rộn rã tiếng cười của những người nông dân Mông, Dao. Triệu Hải Đăng không xây dựng một biệt thự xa hoa riêng cho mình, anh quay trở lại thung lũng cũ, cùng ông Sình và bà con nông dân xây dựng Hợp tác xã Mật ong sạch Đồng Văn, cam kết bao tiêu toàn bộ sản lượng mật hữu cơ nguyên chất cho bà con với giá cao sòng phẳng.</p>
<p>“Cảm ơn cậu Đăng, nhờ cậu mà người dân cao nguyên đá chúng tôi không còn lo bị ép giá, giữ được cái nghề nuôi ong gia truyền này,” ông Sình xúc động siết chặt tay anh bên cạnh thùng ong số hóa đầu tiên.</p>
<p>Nguyễn Khánh An đứng bên cạnh anh, mái tóc ngắn bay nhẹ trong gió ngàn thổi lướt qua những rặng đá tai mèo nở rộ hoa bạc hà tím nhạt thơm ngát. Cô khẽ chạm ly nước mật ong ấm áp với anh, nụ cười cô vô cùng ấm áp, rạng rỡ:</p>
<p>“Đế chế mật ong sạch của chúng ta đã chính thức niêm yết IPO thành công sòng phẳng trên sàn giao dịch quốc tế tại Singapore hôm nay với định giá vượt mốc nghìn tỷ. Chúc mừng anh, Vua Mật Ong Cao Nguyên Đá đích thực của đất trời Hà Giang.”</p>
<p>Đăng nhìn ra khơi xa ngút ngàn của núi đá biên cương, lòng nhẹ nhõm và tràn đầy kiêu hãnh. Những kẻ phản bội đã phải trả giá đắt nhất sau vành móng ngựa pháp luật, còn anh đã tìm lại được hoài bão nguyên bản của mình giữa tình yêu thương chân thực của bà con nông dân. Triều đại của mật ong sạch chân chính đã chính thức bắt đầu và ngự trị vĩnh cửu!</p>"""

    novel_data["chapters"].extend([
        {"title": "Chương 1: Trục Xuất Dưới Đêm Đông Đồng Văn", "content": ch1},
        {"title": "Chương 2: Cơ Duyên Bên Vách Đá Cao Nguyên", "content": ch2},
        {"title": "Chương 3: Sự Nghi Ngờ Lý Tính", "content": ch3},
        {"title": "Chương 4: Bước Đầu Humble Trên Đá Lạnh", "content": ch4},
        {"title": "Chương 5: Đòn Ép Giá Của Kẻ Gian Thương", "content": ch5},
        {"title": "Chương 6: Hợp Tác Xã Giữa Cao Nguyên", "content": ch6},
        {"title": "Chương 7: Đòn Phản Công Pháp Lý và Smear Độc Chì", "content": ch7},
        {"title": "Chương 8: Gọng Kìm Áp Lực Lên Vạn An Capital", "content": ch8},
        {"title": "Chương 9: Ổ Cứng Di Động Và Nhân Chứng Đồng Văn", "content": ch9},
        {"title": "Chương 10: Triển Lãm Nông Nghiệp Quốc Tế - Đêm Trước Quyết Chiến", "content": ch10},
        {"title": "Chương 11: Phiên Lật Kèo Thế Kỷ", "content": ch11},
        {"title": "Chương 12: Đăng Vương Vua Mật Ong", "content": ch12}
    ])

    out_file = "/Users/aaronnguyen/TN/App/doctieuthuyet/pending_novel.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(novel_data, f, ensure_ascii=False, indent=4)
        
    print(f"🎉 Expanded 12-Chapter Manuscript compiled successfully to {out_file}!")

if __name__ == "__main__":
    main()
