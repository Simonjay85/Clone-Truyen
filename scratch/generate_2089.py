# -*- coding: utf-8 -*-
import json
import os

story = {
    "title": "Trọng Sinh 2008: Ôm Đất Đông Anh Trước Cơn Sốt Nghìn Tỷ",
    "author": "Trần Hải Phong",
    "genre": "Sảng Văn",
    "intro": '<p><strong>"Đông Anh chỉ là vùng đất hoang sơ nghèo đói ven sông Hồng, ai mua đất ở đây đều là kẻ điên!"</strong></p><p><strong>Nhưng Trần Huy biết, chỉ vài năm nữa, khi cầu Nhật Tân thông xe và trục Võ Nguyên Giáp hoàn thành, những bãi ngô hoang dại này sẽ biến thành những mỏ vàng nghìn tỷ lấp lánh.</strong></p><hr /><p>Trọng sinh trở lại mùa hè năm 2008 đúng thời điểm lịch sử sáp nhập Hà Tây vào Hà Nội, Trần Huy đối đầu với người em họ phản bội và thế lực tín dụng đen hung hãn đang ép anh vào đường cùng. Bằng bản đồ quy hoạch chi tiết 1/500 đóng dấu đỏ của Bộ Xây dựng và sự hợp tác sắc sảo với nữ tài phiệt Lê Thu Trang, anh từng bước lật đổ nhóm lợi ích, thiết lập đế chế bất động sản hùng mạnh nhất thủ đô.</p>',
    "seo": {
        "focus_keyword": "trong sinh 2008 om dat dong anh",
        "seo_title": "Trọng Sinh 2008: Ôm Đất Đông Anh Cơn Sốt Nghìn Tỷ",
        "seo_description": "Trọng sinh về 2008 ôm trọn đất vàng Đông Anh trước quy hoạch cầu Nhật Tân. Trận chiến thương trường nảy lửa lật kèo nhóm lợi ích sừng sỏ."
    },
    "chapters": []
}

# Chương 1
c1_content = """
<p>Cơn mưa rào mùa hạ năm 2008 trút xuống thị trấn Đông Anh như trút nước, từng hạt mưa nặng trĩu đập liên hồi vào mái tôn rỉ sét của căn nhà cấp bốn dột nát.</p>
<p>Trần Huy giật mình mở mắt, lồng ngực phập phồng dữ dội, mồ hôi lạnh rịn ra ướt đẫm cả chiếc áo thun ba lỗ đã sờn vai.</p>
<p>Anh đưa bàn tay thô ráp lên vuốt mặt, cảm nhận được hơi ấm và nhịp đập thình thịch nơi huyết quản ở cổ.</p>
<p>"Mình chưa chết sao?"</p>
<p>Ký ức cuối cùng của kiếp trước hiện lên rõ mồn một trong tâm trí: anh bị gã em họ Trần Đức lừa ký vào biên bản bàn giao mặt bằng trắng, cướp sạch dự án khu đô thị ven sông Hồng rộng ba mươi héc-ta, rồi đẩy anh vào cảnh nợ nần chồng chất, cuối cùng chết gục trên vỉa hè lạnh giá giữa mùa đông Hà Nội.</p>
<p>Nhìn tờ lịch treo tường bằng giấy mỏng ghi ngày hai mươi hai tháng năm năm hai ngàn không trăm lẻ tám, Trần Huy siết chặt nắm tay đến mức các khớp xương kêu răng rắc, gân xanh nổi lên cuồn cuộn trên cánh tay rám nắng.</p>
<p>Anh đã thực sự trọng sinh về đúng thời điểm Hà Tây chuẩn bị sáp nhập vào Hà Nội, khi đất Đông Anh vẫn còn bị người đời coi là vùng đất nông nghiệp nghèo nàn bên kia sông Hồng.</p>
<p>"Rầm!"</p>
<p>Cánh cửa gỗ mục nát bị đạp văng ra, đập mạnh vào bức tường vôi vữa bong tróc.</p>
<p>Trần Đức bước vào, mái tóc vuốt gel bóng lộn dựng ngược, chiếc áo sơ mi lụa hoa hòe mở phanh cúc ngực lộ ra chiếc vòng bạc dày cộm.</p>
<p>Đi sau gã là hai tên tay sai bặm trợn, bắp tay xăm trổ đầy hình thù kỳ quái, ánh mắt lạnh lùng liếc nhìn xung quanh căn nhà tuềnh toàng.</p>
<p>"Anh Huy, hạn nợ năm mươi triệu đồng của anh từ chỗ anh Đại Long Biên đã hết cách đây đúng một tiếng rồi."</p>
<p>Trần Đức vừa nói vừa rút từ trong túi quần ra một điếu thuốc ba số năm, châm lửa hít một hơi sâu rồi phả khói thẳng vào mặt Trần Huy.</p>
<p>"Anh Đại bảo em đến báo cho anh một tin mừng."</p>
<p>"Anh Đại rất có lòng tốt, muốn mua lại toàn bộ hai mẫu đất bãi ngô ven sông của anh với giá sáu mươi triệu đồng."</p>
<p>"Trừ đi năm mươi triệu tiền nợ cả gốc lẫn lãi, anh còn dư hẳn mười triệu đồng để tha hồ mua mì tôm ăn qua ngày."</p>
<p>Trần Huy đứng dậy, chiều cao một mét tám mươi lăm của anh đổ bóng dài dưới ánh đèn tuýp leo lét, tạo ra một áp lực vô hình khiến Trần Đức vô thức lùi lại nửa bước.</p>
<p>Đồng tử của Trần Huy co rút lại, ánh mắt sắc như dao găm cắm thẳng vào khuôn mặt tráo trở của gã em họ.</p>
<p>"Sáu mươi triệu đồng cho hai mẫu đất ngay sát chân cầu Nhật Tân tương lai?"</p>
<p>"Trần Đức, mày nghĩ tao vẫn là thằng ngu của kiếp trước sao?"</p>
<p>Trần Đức giật mình, điếu thuốc trên tay gã run nhẹ làm rơi một mẩu tàn nóng xuống mu bàn tay, khiến gã khẽ rít lên một tiếng đau đớn.</p>
<p>Gã không hiểu sao gã anh họ vốn dĩ nhút nhát, hiền lành hôm nay lại sở hữu ánh mắt đáng sợ đến như vậy.</p>
<p>"Mày về bảo với Đại Long Biên, nợ tiền tao sẽ trả bằng tiền mặt trước năm giờ chiều mai."</p>
<p>"Còn đất của tao, một tấc cũng đừng hòng đụng vào!"</p>
<p>Tên tay sai xăm trổ bước lên phía trước, nắm đấm siết chặt định lao vào Trần Huy để dằn mặt.</p>
<p>Trần Huy không hề né tránh, lồng ngực anh ưỡn thẳng, tay nắm chặt chiếc tuýp sắt để sẵn bên cạnh giường ngủ.</p>
<p>"Muốn động thủ ở đây?"</p>
<p>"Tao đã báo cho công an xã Đông Hội đang đi tuần tra ngay đầu ngõ rồi."</p>
<p>"Tụi mày cứ việc bước lên thử xem!"</p>
<p>Trần Đức nhìn thấy sự kiên quyết tột độ trong mắt Trần Huy, gã nghiến răng kèn kẹt, giơ tay ngăn tên đàn em lại.</p>
<p>"Được, Trần Huy, mày khá lắm!"</p>
<p>"Tao để xem trước năm giờ chiều mai mày lấy đâu ra năm mươi triệu đồng bằng tiền mặt."</p>
<p>"Nếu không có tiền, anh Đại sẽ đến siết nợ bằng cả đôi bàn tay của mày!"</p>
<p>Nói xong, Trần Đức quay người bỏ đi, gót giày da của gã nện xuống thềm nhà xi măng vang lên những tiếng cồm cộp đầy tức tối.</p>
<p>Trần Huy đứng lặng trong bóng tối, hơi thở dần ổn định lại, nhịp tim đập mạnh mẽ đầy quyết tâm.</p>
<p>Anh biết rõ trong vòng hai mươi bốn giờ tới, anh phải tìm được nguồn vốn khổng lồ để trả nợ và gom thêm đất Đông Anh trước khi cơn sốt đất nghìn tỷ bùng nổ.</p>
"""
story["chapters"].append({"title": "Chương 1: Sự Trở Lại Của Kẻ Bại Trận", "content": c1_content})

# Chương 2
c2_content = """
<p>Sáng hôm sau, ánh nắng chói chang của mùa hè Hà Nội trải dài trên những con phố nhộn nhịp, Trần Huy bước vào sảnh lớn sang trọng của khách sạn Sofitel Plaza nằm ngay cạnh hồ Tây.</p>
<p>Tiếng gót giày cao gót gõ xuống nền đá hoa cương sắc lạnh vang lên đều đặn, thu hút sự chú ý của Trần Huy.</p>
<p>Lê Thu Trang bước xuống từ chiếc xe Mercedes-Benz màu đen bóng loáng, cô mặc bộ vest công sở màu xanh đen ôm sát cơ thể, mái tóc búi cao gọn gàng lộ ra vầng trán thông minh và đôi khuyên tai kim cương lấp lánh.</p>
<p>Cô là Giám đốc Đầu tư của Quỹ Phát triển Đô thị Hà Nội, nổi tiếng là người phụ nữ lý tính, sắc sảo và cực kỳ lạnh lùng trên thương trường.</p>
<p>"Anh Trần Huy?"</p>
<p>Giọng nói của Lê Thu Trang trong trẻo nhưng mang theo sự uy nghiêm khó tả, cô đứng đối diện với anh, đôi mắt phượng khẽ nheo lại đánh giá người đàn ông ăn mặc giản dị trước mặt.</p>
<p>"Tôi chỉ cho anh đúng mười phút uống trà."</p>
<p>"Nếu đề xuất đầu tư của anh không có giá trị thực tiễn, tôi sẽ lập tức rời đi."</p>
<p>Trần Huy mỉm cười nhẹ, anh đưa bàn tay chỉ về phía bàn trà yên tĩnh ở góc sảnh.</p>
<p>"Mười phút là quá đủ để thay đổi tương lai của Quỹ đầu tư của cô trong mười năm tới, thưa cô Lê Thu Trang."</p>
<p>Ngồi xuống ghế da, Lê Thu Trang không hề đụng vào tách trà nóng, cô khoanh hai tay trước ngực, ngón tay trỏ gõ nhẹ lên bắp tay theo nhịp điệu đều đặn.</p>
<p>"Anh nói anh có thông tin quy hoạch chi tiết về trục đường nối từ trung tâm Hà Nội sang Đông Anh?"</p>
<p>"Hiện tại dự án cầu Nhật Tân vẫn chỉ là những cuộc thảo luận trên giấy tờ của Bộ Giao thông Vận tải."</p>
<p>"Chưa hề có bất kỳ văn bản chính thức nào được ban hành."</p>
<p>"Tại sao tôi phải tin tưởng một người không có danh tiếng như anh?"</p>
<p>Trần Huy nhìn thẳng vào mắt Lê Thu Trang, sự tự tin toát ra từ từng cử chỉ của anh khiến cô gái trẻ khẽ giật mình.</p>
<p>"Bởi vì tôi biết rõ vị trí chính xác của mố cầu Nhật Tân bên phía Đông Anh sẽ nằm ngay tại khu đất xã Đông Hội."</p>
<p>"Tôi cũng biết Quỹ của cô đang bị ép chỉ tiêu giải ngân một trăm tỷ đồng trước khi kết thúc quý hai năm nay."</p>
<p>"Nếu không tìm được dự án khả thi, cô sẽ mất ghế Giám đốc vào tay người phó của mình."</p>
<p>Hơi thở của Lê Thu Trang khựng lại trong một nhịp, lồng ngực cô phập phồng dưới lớp áo vest mỏng.</p>
<p>Đúng là cô đang gặp khủng hoảng nội bộ cực kỳ nghiêm trọng, áp lực hai mươi bốn giờ giải ngân đang đè nặng lên vai cô.</p>
<p>"Anh điều tra tôi?"</p>
<p>"Không, tôi chỉ đưa ra một đề nghị hợp tác sòng phẳng."</p>
<p>"Cô rót vốn năm mươi tỷ đồng để tôi thu mua năm mươi héc-ta đất nông nghiệp ven sông Hồng tại Đông Anh ngay trong hôm nay."</p>
<p>"Tôi sẽ đứng ra lo liệu toàn bộ thủ tục pháp lý và đền bù giải phóng mặt bằng."</p>
<p>"Đổi lại, Quỹ của cô sẽ sở hữu sáu mươi phần trăm cổ phần của dự án khu đô thị sinh thái tương lai."</p>
<p>Lê Thu Trang nhếch môi cười lạnh, ánh mắt cô đầy vẻ lý tính.</p>
<p>"Năm mươi tỷ đồng không phải là lá mít để tôi tùy tiện ký duyệt."</p>
<p>"Điều kiện của tôi rất đơn giản:"</p>
<p>"Trước năm giờ chiều nay, anh phải mang đến cho tôi bản đồ quy hoạch chi tiết một trên năm trăm có dấu đỏ xác nhận của Bộ Xây dựng."</p>
<p>"Nếu anh làm được, tiền sẽ được giải ngân vào tài khoản của anh trong vòng ba mươi phút."</p>
<p>"Nếu không, xin vui lòng không làm phiền tôi nữa."</p>
<p>Trần Huy đứng dậy, anh đưa tay ra và siết nhẹ bàn tay mềm mại nhưng lạnh lùng của Lê Thu Trang.</p>
<p>"Hẹn gặp lại cô lúc bốn giờ ba mươi chiều nay tại văn phòng của cô."</p>
<p>"Tôi sẽ mang theo thứ cô cần."</p>
"""
story["chapters"].append({"title": "Chương 2: Cuộc Gặp Trực Diện Ở Khách Sạn Sofitel", "content": c2_content})

# Chương 3
c3_content = """
<p>Rời khỏi Sofitel Plaza, Trần Huy lập tức bắt xe ôm chạy thẳng sang trụ sở Sở Quy hoạch Kiến trúc Hà Nội trên đường Tràng Thi.</p>
<p>Trong khi đó, tại Đông Anh, Trần Đức đang cùng tên trùm Đại Long Biên ngồi trong một quán cà phê sang trọng trên đường Nguyễn Văn Cừ.</p>
<p>Đại Long Biên là một gã trung niên to béo, cổ đeo sợi dây chuyền vàng to bản, ngón tay đeo đầy nhẫn ngọc bích.</p>
<p>"Thằng Huy nó bảo chiều nay trả năm mươi triệu?"</p>
<p>"Đúng thế đại ca, nó còn dám mạnh miệng thách thức cả chúng ta nữa!"</p>
<p>Trần Đức vừa rót nước vừa thêm dầu vào lửa.</p>
<p>Đại Long Biên đập mạnh cốc nước chè xuống bàn gỗ làm nước bắn tung tóe ra xung quanh.</p>
<p>"Mẹ kiếp, một thằng ranh con nghèo kiết xác lấy đâu ra tiền!"</p>
<p>"Mày gọi thêm chục thằng đàn em mang theo hung khí xuống canh ngay tại khu đất Đông Hội của nó cho tao."</p>
<p>"Cứ quá năm giờ chiều mà nó không có tiền, lập tức phá nát căn nhà của nó, ép nó phải ký giấy bán đất!"</p>
<p>Lúc này tại Tràng Thi, Trần Huy đang đứng trước phòng làm việc của Phó Giám đốc Sở Quy hoạch Kiến trúc.</p>
<p>Mồ hôi chảy ròng ròng trên trán anh, ướt đẫm cả vạt áo sơ mi phía sau lưng.</p>
<p>Anh biết mình chỉ còn chưa đầy bốn tiếng đồng hồ để lấy được bản đồ quy hoạch gốc.</p>
<p>Trần Huy gõ cửa bước vào, đối diện với anh là ông Nguyễn Minh Triết, người đang trực tiếp phụ trách đề án sáp nhập địa giới hành chính Hà Nội mở rộng.</p>
<p>"Cậu Huy, tài liệu quy hoạch cầu Nhật Tân là tài liệu mật cấp nhà nước, chưa được phép công bố ra ngoài."</p>
<p>"Tại sao tôi phải đưa nó cho cậu?"</p>
<p>Trần Huy bình tĩnh lấy từ trong túi tài liệu ra một bản phân tích chi tiết về tác động môi trường và phương án đền bù tái định cư cho hơn một ngàn hộ dân xã Đông Hội mà anh tự tay viết suốt đêm qua.</p>
<p>Đây là những kiến thức đúc kết từ kiếp trước, khi anh trực tiếp tham gia vào dự án đền bù này.</p>
<p>Ông Triết ban đầu định xua tay từ chối, nhưng khi liếc nhìn vào trang đầu tiên, đôi mắt ông bỗng co rút lại.</p>
<p>Ông đeo kính lão vào, chăm chú đọc từng trang tài liệu, ngón tay run nhẹ vì kinh ngạc trước những số liệu chính xác đến từng mét vuông đất nông nghiệp.</p>
<p>"Cậu Huy... những số liệu này cậu lấy ở đâu ra?"</p>
<p>"Thưa chú, đây là kết quả khảo sát thực địa độc lập của cháu suốt ba năm qua."</p>
<p>"Cháu biết nhà nước đang gặp khó khăn trong việc tìm kiếm phương án đền bù hợp lòng dân để đẩy nhanh tiến độ dự án."</p>
<p>"Bản phân tích này sẽ giúp Sở tiết kiệm được ít nhất sáu tháng làm việc và hàng chục tỷ đồng ngân sách."</p>
<p>Ông Triết đứng dậy đi lại trong phòng, nét mặt đăm chiêu suy nghĩ dữ dội dưới áp lực tiến độ từ UBND Thành phố.</p>
<p>Sau mười phút cân nhắc kỹ lưỡng, ông bước đến chiếc két sắt ở góc phòng, lấy ra một bản đồ quy hoạch chi tiết một trên năm trăm của dự án cầu Nhật Tân và đường dẫn hai đầu cầu đã được đóng dấu đỏ phê duyệt của Bộ Xây dựng.</p>
<p>"Cậu Huy, tôi chỉ cho cậu sao chép bản đồ này tại chỗ để làm tài liệu nghiên cứu đối ứng."</p>
<p>"Tuyệt đối không được phát tán ra công chúng trước ngày công bố chính thức."</p>
<p>Trần Huy mừng rỡ vô cùng, lồng ngực anh phập phồng thở phào nhẹ nhõm.</p>
<p>"Cháu xin cam đoan bằng danh dự của mình, thưa chú!"</p>
"""
story["chapters"].append({"title": "Chương 3: 24 Giờ Sinh Tử", "content": c3_content})

# Chương 4
c4_content = """
<p>Đúng bốn giờ hai mươi lăm phút chiều, Trần Huy bước vào văn phòng của Lê Thu Trang tại tòa nhà Capital Tower trên đường Trần Hưng Đạo.</p>
<p>Lê Thu Trang đang đứng nhìn ra cửa sổ kính lớn hướng về phía sông Hồng, trên tay cầm chiếc bút ký đắt tiền.</p>
<p>Nghe tiếng bước chân, cô quay lại, gót giày gõ xuống nền gạch bóng loáng vang lên những âm thanh khô khốc.</p>
<p>"Anh Huy, anh đúng giờ lắm."</p>
<p>"Nhưng chỉ còn năm phút nữa là đến hạn chót."</p>
<p>"Bản đồ quy hoạch có dấu đỏ đâu?"</p>
<p>Trần Huy không nói lời nào, anh bước đến bàn làm việc, mở khóa túi tài liệu da và trải rộng tấm bản đồ quy hoạch chi tiết một trên năm trăm lên mặt bàn kính.</p>
<p>Con dấu đỏ chót của Bộ Xây dựng và chữ ký tươi của Thứ trưởng hiện lên rõ mồn một dưới ánh đèn văn phòng.</p>
<p>Đồng tử của Lê Thu Trang co rút lại, cô vội vàng bước tới, cúi xuống nhìn chăm chú vào vị trí mố cầu Nhật Tân được đánh dấu tọa độ chính xác bằng mực đỏ.</p>
<p>Làn da cô khẽ ửng hồng vì phấn khích, hơi thở gấp gáp làm lồng ngực phập phồng liên tục.</p>
<p>"Trời đất... đây thực sự là bản đồ quy hoạch gốc!"</p>
<p>"Làm sao anh có thể lấy được nó?"</p>
<p>"Điều đó không quan trọng, thưa cô Trang."</p>
<p>"Bây giờ là bốn giờ ba mươi phút chiều."</p>
<p>"Lời hứa giải ngân năm mươi tỷ đồng của cô còn hiệu lực chứ?"</p>
<p>Lê Thu Trang ngẩng đầu lên nhìn Trần Huy, ánh mắt cô không còn sự khinh thường mà thay vào đó là sự tôn trọng và e dè trước năng lực đáng sợ của người đàn ông này.</p>
<p>Cô nhanh chóng lấy lại sự lý tính của một chuyên gia tài chính hàng đầu.</p>
<p>"Tôi sẽ giữ lời hứa."</p>
<p>"Nhưng tôi có thêm điều kiện hợp tác mới:"</p>
<p>"Quỹ của tôi phải nắm giữ năm mươi mốt phần trăm quyền biểu quyết tại công ty dự án Đông Anh do chúng ta thành lập."</p>
<p>"Toàn bộ số tiền năm mươi tỷ đồng giải ngân phải được chuyển thẳng vào tài khoản phong tỏa tại ngân hàng Techcombank chi nhánh Hà Nội để đảm bảo chỉ được dùng cho mục đích mua đất."</p>
<p>"Nếu anh đồng ý, chúng ta ký hợp đồng ngay tại chỗ."</p>
<p>Trần Huy mỉm cười, anh đã lường trước điều kiện này của cô.</p>
<p>"Tôi đồng ý với điều kiện của cô."</p>
<p>"Nhưng tôi phải là người trực tiếp điều hành mọi hoạt động thực địa tại Đông Anh."</p>
<p>"Thỏa thuận!"</p>
<p>Hai bên nhanh chóng ký vào bản hợp đồng hợp tác đầu tư đã được chuẩn bị sẵn.</p>
<p>Đúng bốn giờ năm mươi phút chiều, tiếng chuông điện thoại của Trần Huy vang lên báo tin nhắn chuyển tiền thành công từ Techcombank.</p>
<p>"Tài khoản của quý khách đã được cộng năm mươi tỷ đồng."</p>
<p>Trần Huy nhìn dòng chữ trên màn hình điện thoại, các đầu ngón tay anh siết chặt lại đến trắng bệch.</p>
<p>Anh đã có đủ vũ khí để bắt đầu cuộc thanh trừng kiếp trước.</p>
"""
story["chapters"].append({"title": "Chương 4: Bằng Chứng Thép", "content": c4_content})

# Chương 5
c5_content = """
<p>Đúng năm giờ chiều, tại mảnh đất hai mẫu ven sông Hồng của Trần Huy ở xã Đông Hội, bầu không khí căng thẳng bao trùm như muốn bóp nghẹt lồng ngực những người có mặt.</p>
<p>Trần Đức cùng mười tên đàn em tay lăm lăm gậy sắt và dao phóng lợn đang đứng vây quanh căn nhà cấp bốn.</p>
<p>Tên cầm đầu nhóm tay sai đập mạnh chiếc gậy sắt xuống cánh cửa gỗ, tạo ra tiếng động chói tai vang vọng cả một góc xóm.</p>
<p>"Trần Huy! Hết giờ rồi!"</p>
<p>"Mau cút ra đây ký giấy chuyển nhượng đất cho anh Đại, nếu không tao dỡ nhà mày ngay lập tức!"</p>
<p>Trần Đức đứng bên cạnh cười đắc ý, gã nghĩ rằng Trần Huy chắc chắn đã bỏ trốn vì không thể kiếm đâu ra năm mươi triệu đồng trong một ngày.</p>
<p>Đột nhiên, tiếng còi xe ô tô vang lên dồn dập từ phía đầu ngõ.</p>
<p>Một chiếc xe Ford Transit mười sáu chỗ màu bạc lao tới, phanh gấp tạo ra vệt lốp đen sì trên đường đất ẩm ướt.</p>
<p>Trần Huy bước xuống xe, vẻ mặt lạnh lùng như băng đá, đi sau anh là Lê Thu Trang và bốn nhân viên bảo vệ chuyên nghiệp mặc đồng phục đen lịch sự.</p>
<p>"Trần Đức, mày muốn dỡ nhà ai?"</p>
<p>Trần Huy bước tới, ánh mắt sắc lẹm lướt qua đám tay sai khiến chúng vô thức chùn bước.</p>
<p>Trần Đức cười khẩy, cố gắng che giấu sự lo lắng đang trỗi dậy trong lòng.</p>
<p>"Anh Huy, anh về rồi à?"</p>
<p>"Tiền đâu? Đúng năm mươi triệu đồng tiền mặt."</p>
<p>"Nếu không có, đám đàn em của em không biết giữ bình tĩnh đâu."</p>
<p>Trần Huy rút từ trong túi quần ra một chiếc phong bì dày cộp, ném thẳng vào ngực Trần Đức.</p>
<p>"Năm mươi triệu đồng tiền mặt của mày đây."</p>
<p>"Mau ký vào giấy xác nhận biên nhận thanh toán nợ gốc và lãi lập tức."</p>
<p>Trần Đức mở phong bì ra, những tờ tiền polyme mệnh giá năm trăm ngàn đồng mới cứng hiện ra làm gã trợn tròn mắt kinh ngạc.</p>
<p>Gã không thể tin được Trần Huy lại có thể kiếm được số tiền lớn như vậy chỉ trong vài tiếng đồng hồ.</p>
<p>"Khoan đã... số tiền này..."</p>
<p>Tên trùm Đại Long Biên từ trong chiếc xe Camry gần đó bước xuống, khuôn mặt gã xám ngoét vì tức giận khi thấy kế hoạch cướp đất bị đổ bể.</p>
<p>"Thằng ranh con, mày lấy tiền này ở đâu ra?"</p>
<p>"Dù mày có trả hết nợ, tao vẫn có cách lấy mảnh đất này!"</p>
<p>"Hợp đồng thế chấp đất này tao đã đăng ký giao dịch bảo đảm tại huyện rồi!"</p>
<p>Lê Thu Trang bước lên phía trước, gót giày cao gót của cô nện mạnh xuống nền đất vang lên âm thanh sắc gọn.</p>
<p>Cô rút từ trong cặp tài liệu ra một văn bản của Chi cục Thuế và Phòng Tài nguyên Môi trường huyện Đông Anh.</p>
<p>"Tôi là Lê Thu Trang, Giám đốc Đầu tư Quỹ Phát triển Đô thị Hà Nội."</p>
<p>"Chúng tôi đã chính thức mua lại toàn bộ nghĩa vụ tài chính và quyền sử dụng khu đất này từ ngân hàng nông nghiệp phát triển nông thôn chi nhánh Đông Anh với giá năm mươi tỷ đồng."</p>
<p>"Hợp đồng thế chấp giả mạo của các người hoàn toàn vô hiệu trước pháp luật vì chữ ký giả của chủ đất."</p>
<p>"Biên bản giám định chữ ký của công an tỉnh đã xác nhận điều này."</p>
<p>"Nếu các người không lập tức rút lui, lực lượng cảnh sát hình sự huyện Đông Anh đang đợi sẵn ở đầu ngõ sẽ vào cuộc ngay lập tức!"</p>
<p>Đại Long Biên nhìn thấy con dấu đỏ chót của cơ quan công an trên biên bản giám định chữ ký, mồ hôi hạt to bằng hạt ngô rịn ra trên trán gã.</p>
<p>Gã biết mình đã đụng phải thế lực tài phiệt cực kỳ khủng khiếp.</p>
<p>"Rút! Mau rút lui cho tao!"</p>
<p>Đại Long Biên hét lên rồi vội vã chui tợn vào xe ô tô chạy trốn, bỏ lại Trần Đức đứng chôn chân tại chỗ với khuôn mặt tái mét không còn một giọt máu.</p>
"""
story["chapters"].append({"title": "Chương 5: Đòn Phản Công Đầu Tiên", "content": c5_content})

# Chương 6
c6_content = """
<p>Sau đòn vả mặt đau đớn tại khu đất Đông Hội, Trần Đức và Đại Long Biên không chịu dừng lại.</p>
<p>Chúng quyết định liên kết với ông Trịnh Văn Hùng, Chủ tịch Tập đoàn Bất động sản Hùng Phát — một thế lực bất động sản sừng sỏ tại quận Long Biên và Gia Lâm.</p>
<p>Trong căn biệt thự xa hoa của mình, ông Hùng Phát trầm ngâm hút xì-gà, ánh mắt thâm hiểm nhìn tấm bản đồ quy hoạch tự chế trên bàn.</p>
<p>"Một thằng ranh con và một đứa con gái vắt mũi chưa sạch mà dám ôm trọn năm mươi héc-ta đất Đông Hội trước mũi tao sao?"</p>
<p>"Ông Đại, ông dùng quan hệ bên phía ngân hàng phong tỏa toàn bộ tài khoản đối ứng của Quỹ đầu tư đó cho tôi."</p>
<p>"Tôi sẽ cho người làm giả đơn tố cáo Trần Huy đầu cơ đất đai trái phép, ép chính quyền huyện phải đình chỉ mọi giao dịch đền bù đất đai tại khu vực này."</p>
<p>"Chúng ta phải bắt tụi nó phải nôn đất ra trong vòng mười hai tiếng!"</p>
<p>Sáng hôm sau, khi Trần Huy đang chuẩn bị tiến hành chi trả tiền đền bù đợt một cho hơn hai trăm hộ dân xã Đông Hội, khủng hoảng bất ngờ ập đến.</p>
<p>Hai trăm người dân cầm theo gậy gộc, cuốc xẻng kéo đến bao vây văn phòng tạm thời của dự án.</p>
<p>Họ la hét giận dữ vì có tin đồn Trần Huy là kẻ lừa đảo, tài khoản ngân hàng đã bị phong tỏa và họ sẽ không nhận được một đồng tiền đền bù nào.</p>
<p>"Trần Huy lừa đảo! Trả lại đất cho chúng tôi!"</p>
<p>"Đồ lừa đảo cút đi!"</p>
<p>Cùng lúc đó, Lê Thu Trang gọi điện thoại cho Trần Huy, giọng nói của cô lộ rõ vẻ lo lắng tột độ, nhịp thở dồn dập qua loa điện thoại.</p>
<p>"Anh Huy, tài khoản của công ty dự án tại Techcombank vừa bị phong tỏa tạm thời do có đơn tố cáo gian lận tài chính từ tập đoàn Hùng Phát."</p>
<p>"Tôi đang bị ban hội đồng quản trị triệu tập khẩn cấp yêu cầu đình chỉ chức vụ."</p>
<p>"Chúng ta chỉ có đúng mười hai giờ để giải quyết khủng hoảng này."</p>
<p>"Nếu người dân nổi loạn và rút lại thỏa thuận bán đất, dự án của chúng ta sẽ hoàn toàn sụp đổ!"</p>
<p>Trần Huy đứng trước ban công văn phòng nhìn xuống đám đông giận dữ bên dưới.</p>
<p>Lồng ngực anh siết chặt, gân xanh nổi lên trên cổ, nhưng ánh mắt anh vẫn lạnh lùng và tỉnh táo đến đáng sợ.</p>
<p>Anh biết đây chính là đòn quyết định của kẻ thù ở kiếp trước.</p>
<p>"Trang, cô hãy bình tĩnh và giữ vững vị trí ở ban hội đồng quản trị."</p>
<p>"Tôi sẽ giải quyết đám đông này và bẻ gãy đòn phong tỏa của Trịnh Văn Hùng trong vòng sáu tiếng tới."</p>
<p>"Hãy tin tôi!"</p>
"""
story["chapters"].append({"title": "Chương 6: Bẫy Ngầm Của Nhóm Lợi Ích", "content": c6_content})

# Chương 7
c7_content = """
<p>Trần Huy bước xuống sân văn phòng đối diện với hơn hai trăm người dân đang giận dữ gào thét.</p>
<p>Anh cầm chiếc loa phóng thanh, giọng nói trầm ấm nhưng đanh thép vang vọng khắp khu đất rộng lớn.</p>
<p>"Bà con xã Đông Hội hãy bình tĩnh nghe tôi nói!"</p>
<p>"Tôi biết có kẻ đã tung tin đồn ác ý rằng tài khoản của chúng tôi bị phong tỏa để ép bà con bán đất với giá rẻ mạt cho tập đoàn Hùng Phát."</p>
<p>"Nhưng hôm nay, tôi mang đến đây bằng chứng thép để chứng minh sự minh bạch của chúng tôi!"</p>
<p>Trần Huy giơ cao một chiếc máy tính xách tay kết nối với máy chiếu công suất lớn chiếu thẳng lên bức tường trắng của văn phòng.</p>
<p>Trên màn hình hiện lên sao kê tài khoản ngân hàng Techcombank của công ty dự án Đông Anh có số dư năm mươi tỷ đồng vẫn hoàn toàn bình thường, không hề bị phong tỏa như tin đồn.</p>
<p>Quan trọng hơn, anh trình chiếu một file ghi âm cuộc đối thoại giữa Trịnh Văn Hùng và một cán bộ tín dụng ngân hàng biến chất về việc âm thầm dàn xếp đơn tố cáo giả mạo để phong tỏa tài khoản trái phép.</p>
<p>Giọng nói thâm độc của Trịnh Văn Hùng vang lên rõ ràng qua loa phóng thanh:</p>
<p>"...Cứ phong tỏa tài khoản của thằng Huy trong vòng hai mươi bốn tiếng cho tao."</p>
<p>"Chỉ cần dân chúng hoang mang rút đất, tao sẽ cho người xuống gom sạch với giá rẻ bằng một nửa."</p>
<p>"Xong việc tao sẽ chuyển cho mày hai tỷ đồng vào tài khoản ở Techcombank..."</p>
<p>Đám đông người dân lập tức ồ lên kinh ngạc, những tiếng la hét giận dữ chuyển hướng hoàn toàn sang phía tập đoàn Hùng Phát.</p>
<p>"Trời đất! Hóa ra tập đoàn Hùng Phát định lừa cướp đất của chúng ta!"</p>
<p>"May mà cậu Huy có bằng chứng rõ ràng!"</p>
<p>Đúng lúc đó, ba chiếc xe đặc chủng của Cục Cảnh sát điều tra tội phạm về tham nhũng, kinh tế, buôn lậu (C03) Bộ Công an lao vào sân.</p>
<p>Một điều tra viên trung tá bước xuống xe, cầm lệnh bắt giữ khẩn cấp đối với Trịnh Văn Hùng và Đại Long Biên đang đứng quan sát ở đằng xa.</p>
<p>"Ông Trịnh Văn Hùng, ông bị bắt giữ vì hành vi cố ý làm giả tài liệu của cơ quan tổ chức, hối lộ cán bộ nhà nước và can thiệp trái phép vào hoạt động kinh tế."</p>
<p>Chiếc còng số tám sắc lạnh khóa chặt hai tay Trịnh Văn Hùng trước sự chứng kiến của hàng trăm người dân Đông Anh.</p>
<p>Trần Huy đứng thẳng người nhìn theo chiếc xe cảnh sát chở kẻ thù kiếp trước đi khuất, khóe môi khẽ nhếch lên một nụ cười ngạo nghễ.</p>
<p>Anh đã hoàn thành cú lật kèo ngoạn mục nhất cuộc đời mình.</p>
"""
story["chapters"].append({"title": "Chương 7: Cú Lật Kèo Ngoạn Mục", "content": c7_content})

# Chương 8
c8_content = """
<p>Hai tháng sau khi tập đoàn Hùng Phát sụp đổ, bầu trời Đông Anh trong xanh vời vợi, gió từ sông Hồng thổi vào lồng lộng xua tan cái nóng oi bức của mùa hè.</p>
<p>Chính phủ chính thức công bố quyết định khởi công xây dựng cầu Nhật Tân và phê duyệt quy hoạch trục đường Võ Nguyên Giáp.</p>
<p>Giá đất tại xã Đông Hội tăng vọt phi mã hơn một trăm lần chỉ trong vòng vài tuần ngắn ngủi.</p>
<p>Khu đất năm mươi héc-ta của Trần Huy và Lê Thu Trang giờ đây trị giá hàng ngàn tỷ đồng, biến họ trở thành những tài phiệt bất động sản trẻ tuổi nhất thủ đô.</p>
<p>Tại lễ khởi công dự án Khu đô thị sinh thái Đông Anh Diamond, Trần Huy đứng bên cạnh Lê Thu Trang trên khán đài danh dự nhìn xuống đại công trường đang nhộn nhịp xe lu, xe xúc hoạt động.</p>
<p>Lê Thu Trang mặc chiếc váy dạ hội màu đỏ rượu vang lộng lẫy, bờ vai trần trắng ngần dưới ánh nắng ban mai.</p>
<p>Cô quay sang nhìn Trần Huy, đôi mắt phượng vốn dĩ lạnh lùng nay tràn ngập sự dịu dàng và ngưỡng mộ sâu sắc.</p>
<p>Cô chủ động đưa bàn tay mềm mại của mình đặt vào lòng bàn tay ấm áp của anh.</p>
<p>"Trần Huy, anh thực sự là một người đàn ông kỳ diệu."</p>
<p>"Nếu ngày đó tôi không tin tưởng anh, có lẽ giờ tôi đã thất bại thảm hại."</p>
<p>"Hôm nay, trước sự chứng kiến của dòng sông Hồng lịch sử này, tôi muốn đặt một điều kiện hợp tác mới với anh."</p>
<p>Trần Huy khẽ siết chặt bàn tay cô, mỉm cười hỏi nhẹ.</p>
<p>"Điều kiện gì vậy, thưa cô Trang?"</p>
<p>"Tôi muốn chúng ta không chỉ hợp tác trên thương trường."</p>
<p>"Tôi muốn đồng hành cùng anh suốt cuộc đời này, chia sẻ mọi vinh quang và cay đắng cùng anh."</p>
<p>"Anh đồng ý chứ?"</p>
<p>Trần Huy nhìn sâu vào đôi mắt long lanh chứa chan tình cảm của người con gái kiêu hãnh trước mặt.</p>
<p>"Tôi đã đợi câu nói này của em suốt hai kiếp rồi, Thu Trang."</p>
<p>Tiếng pháo hoa chúc mừng vang lên rộn rã trên bầu trời Đông Anh, đánh dấu sự khởi đầu của một kỷ nguyên mới rực rỡ nghìn tỷ của Trần Huy và người bạn đời tài sắc vẹn toàn.</p>
"""
story["chapters"].append({"title": "Chương 8: Đông Anh Hóa Rồng", "content": c8_content})

# Save JSON
os.makedirs("/Users/aaronnguyen/TN/App/doctieuthuyet/scratch", exist_ok=True)
with open("/Users/aaronnguyen/TN/App/doctieuthuyet/scratch/rewrite_2089_v13.json", "w", encoding="utf-8") as f:
    json.dump(story, f, ensure_ascii=False, indent=2)

print("Generated rewrite_2089_v13.json successfully!")
