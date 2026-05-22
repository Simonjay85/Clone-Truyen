import json
import os

scratch_dir = "/Users/aaronnguyen/TN/App/doctieuthuyet/scratch"

# 1. Update ID 2587 - Chapter 1
path_2587 = os.path.join(scratch_dir, "rewrite_2587_v13.json")
if os.path.exists(path_2587):
    with open(path_2587, "r", encoding="utf-8") as f:
        data_2587 = json.load(f)
    
    new_content_2587_c1 = """<p>Giữa cơn bão Hải Phòng gầm rú trắng xóa trời đất, mưa rơi như trút những bầu nước khổng lồ xuống mặt đường, gió giật cấp 9 gào thét liên hồi qua từng khe cửa kính của phòng làm việc chính Viện Thiết Kế Cầu Đường miền Bắc.</p>
<p>Tôi, Nguyễn Minh Hòa, đứng lặng người trước bàn làm việc, hai bàn tay siết chặt vào mép bàn gỗ ép công nghiệp đến mức các khớp ngón tay trắng bệch ra, rồi rớm những vệt máu đỏ tươi do cạnh sắc cứa vào da thịt.</p>
<p>Khuôn mặt tôi lúc này tái mét đi, từng giọt mồ hôi lạnh toát ngưng tụ trên trán rồi lăn dài theo gò má thái dương, rơi bộp bộp xuống tấm bản vẽ kỹ thuật chi tiết dầm bê tông dự ứng lực chịu mặn đang hiển thị trên màn hình Dell UltraSharp 32 inch độ phân giải 4K cực nét.</p>
<p>Nhịp tim của tôi đập dồn dập liên tục lên tới 130 nhịp mỗi phút, âm thanh dội vào màng nhĩ nghe rõ mồn một như một tiếng trống trận dồn dập giữa trận địa hoang tàn.</p>
<p>Đột nhiên, cánh cửa gỗ sồi dày cộp của phòng viện trưởng bị đẩy mạnh ra, và tiếng cười châm chọc đầy đắc ý của Lê Khắc Nam vang lên như một nhát dao găm đâm thẳng vào lòng tự trọng rỉ máu của tôi.</p>
<p>Lê Khắc Nam đứng đó, chiếc cà vạt lụa Hermes màu đỏ sậm thắt lệch sang một bên, bụng phệ nhô ra dưới lớp áo sơ mi trắng đắt tiền, khuôn mặt hãnh diện vằn lên những tia máu đỏ do vừa uống rượu ngoại cao cấp.</p>
<p>Hắn chỉ tay thẳng vào mặt tôi, đôi môi mỏng dính mím chặt lại rồi nhếch lên nụ cười đầy khinh miệt: "Mày chỉ là một thằng kỹ sư quèn không hơn không kém, Minh Hòa ạ!"</p>
<p>"Mày nghĩ mày là ai mà dám đòi đứng tên tác giả chính cho dự án cầu vượt biển Tân Vũ Lạch Huyện nghìn tỷ này?"</p>
<p>"Hồ sơ thiết kế dầm bê tông cốt thép dự ứng lực chịu mặn này kể từ giờ phút này sẽ mang tên tao, viện trưởng Lê Khắc Nam!"</p>
<p>"Còn mày, tờ quyết định sa thải có dấu mộc đỏ chói của Hội đồng quản trị đã nằm sẵn trên bàn, cút khỏi viện thiết kế này ngay lập tức trong vòng mười phút!"</p>
<p>Nghe những lời cướp đoạt trắng trợn ấy, lồng ngực tôi phập phồng dữ dội, nhịp thở đứt quãng, nhưng tôi tuyệt đối không hề nói một câu van xin hay cãi vã vô ích nào.</p>
<p>Tôi nhìn sâu vào đôi mắt đầy lòng tham của hắn, rồi nhìn xuống ổ cứng di động SanDisk 2TB đang cắm ở cổng USB phía sau máy tính, nơi lưu giữ toàn bộ log băm SHA-256 của lịch sử git log dự án.</p>
<p>Trong các phiên bản commit từ ngày đầu tiên xây dựng mô hình phần tử hữu hạn Finite Element Method, tôi đã dùng chữ ký số cá nhân và khóa PGP bảo mật cao để ký số cho từng dòng code thiết kế dầm.</p>
<p>Hơn thế nữa, trong chính bản vẽ dầm bê tông dự ứng lực mà Lê Khắc Nam vừa cướp đoạt để nộp cho Quỹ đầu tư hạ tầng Việt Phát, tôi đã âm thầm cài đặt một lỗi chết người liên quan đến phân bố ứng suất tại trụ cầu T12.</p>
<p>Lỗi thiết kế hệ số an toàn này nếu không được tính toán lại bằng công nghệ mô phỏng phi tuyến tính độc quyền của tôi, toàn bộ dầm bê tông sẽ bị nứt vỡ và sụt lún nghiêm trọng chỉ sau 24 giờ chịu tải trọng thực tế từ sóng biển mặn.</p>
<p>Đó là quả bom hẹn giờ vô hình mà tôi để lại cho kẻ phản bội, sẵn sàng nổ tung toàn bộ sự nghiệp chính trị và vương quốc danh vọng của hắn.</p>
<p>Tôi lạnh lùng rút chiếc ổ cứng SanDisk ra khỏi máy tính, đút sâu vào túi quần bò sờn bạc, rồi xách chiếc ba lô sờn vai bước thẳng ra ngoài hành lang lạnh lẽo.</p>
<p>Mưa bão Hải Phòng ngoài kia quất thẳng vào mặt tôi lạnh buốt, nhưng ngọn lửa căm hờn và quyết tâm lật kèo đang bùng cháy điên cuồng trong lồng ngực tôi.</p>
<p>Bước đi dưới cơn mưa tầm tã đến trắng xóa cả tầm nhìn trên đường Lạch Tray, tôi lập tức lấy chiếc điện thoại iPhone 15 Pro Max ra, bấm số gọi trực tiếp cho Đỗ Phương Vy.</p>
<p>Đỗ Phương Vy là nữ luật sư nổi tiếng bậc nhất Hải Phòng, người sở hữu văn phòng luật sư Vy & Cộng sự tại tòa nhà SHP Plaza sầm uất.</p>
<p>Vy là người có lối sống cực kỳ lý tính, tư duy sắc sảo như dao cạo và không bao giờ làm việc dựa trên cảm xúc cá nhân hay sự thương hại tầm thường.</p>
<p>Chỉ sau ba tiếng chuông, giọng nói trong trẻo nhưng lạnh lùng và dứt khoát của Vy vang lên qua loa thoại: "Nguyễn Minh Hòa, tôi đã xem qua email tóm tắt vụ việc của anh gửi lúc 2 giờ chiều."</p>
<p>"Anh bị Lê Khắc Nam cướp bản quyền và trục xuất khỏi viện thiết kế, đồng thời đe dọa phong sát toàn bộ ngành cầu đường miền Bắc đối với anh trong vòng 24 giờ tới?"</p>
<p>Tôi gạt dòng nước mưa đang chảy tràn trên mặt, giọng nói đanh thép kiên định: "Đúng vậy, Vy. Tôi cần sự hỗ trợ pháp lý và tài chính từ văn phòng của cô để lập công ty thiết kế cầu đường độc lập, đánh sập Lê Khắc Nam."</p>
<p>Đỗ Phương Vy im lặng trong đúng 5 giây, tiếng lật tài liệu sột soạt ở đầu dây bên kia vang lên rõ ràng: "Minh Hòa, anh biết nguyên tắc làm việc của tôi rồi."</p>
<p>"Tôi không làm từ thiện, tôi chỉ hợp tác dựa trên lợi ích sòng phẳng và các cam kết pháp lý vững chắc đứng tên riêng."</p>
<p>"Điều kiện của tôi là: Anh phải ký hợp đồng chuyển nhượng vĩnh viễn 25% giá trị sở hữu trí tuệ của bằng sáng chế công nghệ dầm bê tông dự ứng lực chịu mặn cho cá nhân tôi."</p>
<p>"Đồng thời, toàn bộ chi phí tố tụng và thành lập doanh nghiệp mới sẽ được quy đổi thành 30% cổ phần đứng tên tôi tại công ty cầu đường mà anh sắp thành lập."</p>
<p>"Nếu anh đồng ý với điều kiện thương lượng sòng phẳng này, hãy đến ngay căn hộ Penthouse của tôi tại Vinpearl Riverfront Hải Phòng để ký hợp đồng dịch vụ pháp lý có công chứng số CA."</p>
<p>"Nếu không đồng ý, cuộc gọi này kết thúc tại đây và chúc anh may mắn với cuộc khủng hoảng bị phong sát 24 giờ tiếp theo."</p>
<p>Tôi không hề chần chừ hay do dự lấy một giây, lập tức đáp lời: "Đồng ý! Tôi đồng ý với toàn bộ điều kiện đặt ra của cô, Vy."</p>
<p>"Tôi sẽ có mặt tại chỗ cô trong vòng 20 phút nữa cùng toàn bộ file log băm SHA-256 chứa chữ ký số PGP chứng minh nguồn gốc bản quyền tác giả gốc."</p>
<p>Cúp máy, tôi vẫy một chiếc xe taxi Mai Linh bên đường, nhanh chóng bước vào trong xe khi mồ hôi lạnh và nước mưa vẫn còn đọng đầy trên da thịt.</p>
<p>Trong xe, nhịp tim tôi dần bình ổn trở lại ở mức 80 nhịp/phút, ánh mắt tôi nhìn ra cửa sổ xe nhòa nước mưa, hướng về phía cảng Lạch Huyện xa xôi.</p>
<p>Lê Khắc Nam nghĩ rằng hắn đã cướp được mỏ vàng nghìn tỷ và đẩy tôi vào đường cùng không thể ngóc đầu lên nổi.</p>
<p>Nhưng hắn không hề biết rằng, chính bản hợp đồng pháp lý thép với nữ luật sư Đỗ Phương Vy và lỗi thiết kế chí mạng ở trụ cầu T12 sẽ là sợi dây thừng siết chặt cổ hắn.</p>
<p>Cuộc khủng hoảng 24 giờ đếm ngược bắt đầu, và tôi sẽ bắt Lê Khắc Nam phải trả giá đắt cho từng giọt mồ hôi và máu của tôi đổ xuống bản vẽ này!</p>"""
    
    data_2587["chapters"][0]["content"] = new_content_2587_c1
    
    with open(path_2587, "w", encoding="utf-8") as f:
        json.dump(data_2587, f, ensure_ascii=False, indent=2)
    print("Successfully expanded 2587 Chapter 1!")

# 2. Update ID 2606 - Chapter 1
path_2606 = os.path.join(scratch_dir, "rewrite_2606_v13.json")
if os.path.exists(path_2606):
    with open(path_2606, "r", encoding="utf-8") as f:
        data_2606 = json.load(f)
        
    new_content_2606_c1 = """<p>Giữa cơn mưa giông trắng trời gào rú bên bờ biển Nha Trang, sấm sét rạch những vệt sáng chói lòa trên nền trời đen kịt, Diệp Thiên Lang bị ném mạnh ra khỏi cổng biệt thự đá lộng lẫy của gia tộc trầm hương họ Lâm.</p>
<p>Cú ngã mạnh khiến đầu gối anh đập xuống nền đá granite gồ ghề, đau buốt đến tận xương tủy, máu tươi đỏ sậm rỉ ra nhanh chóng bị những giọt nước mưa xối xả cuốn trôi đi.</p>
<p>Mồ hôi lạnh toát hòa lẫn cùng nước mưa buốt giá chảy dài trên khuôn mặt góc cạnh của Thiên Lang, hai bàn tay anh siết chặt lại thành nắm đấm đến mức các khớp ngón tay phát ra tiếng kêu răng rắc rớm máu.</p>
<p>Nhịp tim của Thiên Lang đập điên cuồng lên tới 135 lần mỗi phút, hơi thở dồn dập nghẹn ứ ở cổ họng khi anh ngước mắt nhìn lên bậc thềm biệt thự cao sang.</p>
<p>Phía trên thềm đá, Lâm Vĩnh Nghiệp – người tự xưng là "vua trầm hương đất Khánh Hòa" – đứng đó trong chiếc áo choàng nhung sang trọng, tay cầm chiếc gậy gỗ mun bịt vàng chỏ thẳng vào mặt Thiên Lang.</p>
<p>Khuôn mặt Lâm Vĩnh Nghiệp đỏ gay vì tức giận, khóe mắt hắn co giật liên tục, vằn lên những tia máu hung tợn: "Thằng rể vô dụng rách nát kia! Mày dám vu khống gia tộc tao bán trầm giả tẩm hóa chất cực độc benzyl acetate sao?"</p>
<p>"Hôm nay tao trục xuất mày khỏi Lâm gia, tước đoạt toàn bộ bằng sáng chế công nghệ chiết xuất tinh dầu trầm của mày!"</p>
<p>"Tao đã cho người thông báo phong tỏa mọi tài khoản Techcombank đứng tên mày, và phát lệnh truy quét mày trên toàn địa bàn Nha Trang trong vòng 24 giờ tới!"</p>
<p>"Nếu mày dám bén mảng đến vùng đất rừng đặc dụng Hòn Bà hay các xưởng chưng cất của tao, tao sẽ cho đàn em đánh gãy chân mày!"</p>
<p>Nghe những lời nhục mạ và cướp đoạt trắng trợn ấy, Diệp Thiên Lang không hề mở miệng tranh cãi hay giải thích lấy một câu vô ích nào.</p>
<p>Anh chỉ lẳng lặng nhìn vào vết mủ màu vàng đục bám trên kẽ tay của Lâm Vĩnh Nghiệp – di chứng của việc tiếp xúc lâu ngày với hóa chất tạo trầm hương giả benzyl acetate cực độc.</p>
<p>Thiên Lang sở hữu một năng lực thiên bẩm mà không một ai trong gia tộc họ Lâm có được, đó chính là khứu giác siêu phàm đạt đến cảnh giới "Tâm Khứu" tột đỉnh.</p>
<p>Chỉ cần nhắm mắt lại hít một hơi nhẹ, anh có thể phân tích chính xác từng thành phần hóa học có trong không khí, phân biệt rõ ràng trầm hương tự nhiên hàng ngàn năm tuổi với loại trầm giả tẩm độc.</p>
<p>Và hơn thế nữa, trong đầu anh đã lưu trữ chính xác bản đồ tọa độ của một gốc Kỳ Nam nghìn năm cổ thụ ẩn sâu trong khu bảo tồn nghiêm ngặt của rừng Hòn Bà mà anh vô tình tìm thấy hai tuần trước.</p>
<p>Gốc Kỳ Nam nghìn tỷ ấy chính là chìa khóa vàng giúp anh vươn lên thâu tóm toàn bộ đế chế trầm hương Việt Nam, đẩy những kẻ phản bội vào ngục tù tăm tối.</p>
<p>Thiên Lang lững thững đứng dậy, gạt nước mưa trên mặt, quay lưng bước đi trong màn đêm giông bão, bóng lưng anh cô độc nhưng thẳng tắp như một cây tùng vững chãi giữa bão giông.</p>
<p>Mưa vẫn rơi tầm tã xối xả, anh đi bộ suốt ba cây số dọc đường Trần Phú đến khi dừng chân trước một chiếc VinFast VF9 màu xanh sẫm bóng loáng đang đỗ bên lề đường.</p>
<p>Cửa kính xe hạ xuống, lộ ra khuôn mặt đẹp thanh tú nhưng vô cùng lạnh lùng, lý trí của Nguyễn Thanh Thư – nữ giám đốc trẻ tuổi của Tập đoàn Dược liệu Đông y Thanh Thư.</p>
<p>Thanh Thư nhìn Thiên Lang đang ướt sũng nước mưa và đầu gối rớm máu bằng ánh mắt không chút gợn sóng cảm xúc, cô cất giọng trong trẻo sòng phẳng: "Diệp Thiên Lang, tôi đã nhận được tin anh bị Lâm gia trục xuất và đang bị săn lùng ráo riết trên khắp Nha Trang."</p>
<p>"Anh gọi điện cho tôi lúc 8 giờ tối nói rằng anh muốn hợp tác thương lượng dựa trên tọa độ Kỳ Nam nghìn năm?"</p>
<p>Thiên Lang bước thẳng vào hàng ghế phụ ấm áp của xe, mùi da Nappa cao cấp hòa quyện cùng hương thảo dược dịu nhẹ từ người Thanh Thư xoa dịu khứu giác nhạy cảm của anh.</p>
<p>Anh nhìn thẳng vào mắt Thanh Thư, giọng nói trầm ấm đầy kiên định: "Đúng vậy, Thanh Thư. Tôi có tọa độ chính xác của gốc Kỳ Nam ngàn năm tại rừng Hòn Bà, thứ trị giá ít nhất một ngàn tỷ đồng trên thị trường quốc tế."</p>
<p>"Tôi cần tiềm lực tài chính và đội ngũ pháp lý của tập đoàn cô để che chở và khai thác hợp pháp gốc Kỳ Nam này, đập tan tập đoàn trầm hóa chất của Lâm Vĩnh Nghiệp."</p>
<p>Nguyễn Thanh Thư nhấp một ngụm trà sâm ấm, ngón tay thon dài gõ nhẹ lên vô lăng theo nhịp điệu đều đặn, đôi mắt cô lấp lánh sự tính toán thông minh của một nhà kinh doanh lỗi lạc: "Thiên Lang, anh biết tôi là người lý tính, tôi không làm ăn dựa trên lòng thương hại hay những lời hứa suông."</p>
<p>"Để tôi đồng ý che chở anh trước sự truy sát 24 giờ của Lâm gia và bỏ ra hàng chục tỷ đồng chi phí pháp lý khai thác Hòn Bà, chúng ta phải có thỏa thuận cực kỳ rõ ràng đứng tên riêng."</p>
<p>"Thứ nhất: Gốc Kỳ Nam đó sau khi khai thác thành công phải được chuyển về kho bảo mật của tập đoàn tôi, cá nhân tôi đứng tên sở hữu 50% giá trị tài sản ròng bằng văn bản cam kết đóng dấu mộc đỏ giáp lai."</p>
<p>"Thứ hai: Anh phải bàn giao toàn bộ công thức chiết xuất tinh dầu trầm hương tự nhiên không độc hại cho phòng nghiên cứu của tôi độc quyền sử dụng."</p>
<p>"Nếu anh chấp nhận các điều kiện sòng phẳng này, chúng ta sẽ lập tức ký hợp đồng thỏa thuận liên doanh pháp lý có công chứng CA ngay trên xe này."</p>
<p>"Nếu không đồng ý, mời anh bước xuống xe, cơn mưa giông Nha Trang ngoài kia vẫn đang chờ đón anh cùng đám tay sai của Lâm Vĩnh Nghiệp."</p>
<p>Diệp Thiên Lang khẽ mỉm cười, ánh mắt anh hiện lên sự tán thưởng sâu sắc đối với sự thông minh và lý trí tuyệt vời của Thanh Thư.</p>
<p>"Thương vụ sòng phẳng, điều kiện hoàn toàn hợp lý. Tôi đồng ý ký hợp đồng pháp lý ngay lập tức!" Thiên Lang dứt khoát trả lời.</p>
<p>Nguyễn Thanh Thư gật đầu hài lòng, lấy từ trong ngăn kéo xe ra một tập hợp đồng liên doanh pháp lý đã soạn thảo sẵn, cùng thiết bị ký chữ ký số CA cầm tay.</p>
<p>Cả hai thực hiện các thao tác ký số cực kỳ nhanh gọn và chuẩn xác, cam kết pháp lý chính thức được thiết lập và đóng dấu số bảo mật mã hóa SHA-256 bảo vệ nghiêm ngặt.</p>
<p>Khi tiếng còi xe cảnh sát tuần tra và tiếng động cơ xe máy gầm rú của đám tay sai Lâm gia vang lên phía xa, Thanh Thư bình thản nhấn ga, chiếc VinFast VF9 màu xanh sẫm lao vút đi trong màn mưa bão dày đặc.</p>
<p>Diệp Thiên Lang tựa lưng vào ghế xe, hai mắt nhắm nghiền, khứu giác "Tâm Khứu" của anh đã ngửi thấy mùi tanh của dòng tiền bẩn hối lộ và mùi hóa chất độc hại đang dần bốc lên từ phía dinh thự Lâm gia.</p>
<p>Trận chiến sinh tử 24 giờ đếm ngược chính thức bắt đầu, và với tấm bùa hộ mệnh pháp lý từ Nguyễn Thanh Thư cùng gốc Kỳ Nam nghìn tỷ trong tay, anh sẽ tự tay nghiền nát tập đoàn phản bội Lâm gia thành tro bụi!</p>"""
    
    data_2606["chapters"][0]["content"] = new_content_2606_c1
    
    with open(path_2606, "w", encoding="utf-8") as f:
        json.dump(data_2606, f, ensure_ascii=False, indent=2)
    print("Successfully expanded 2606 Chapter 1!")
