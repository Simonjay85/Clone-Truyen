# -*- coding: utf-8 -*-
import json
import os

story = {
    "title": "Cô Gái Bán Trà Sữa Và Hợp Đồng Trăm Tỷ",
    "author": "Vũ Tuyết Mai",
    "genre": "Sảng Văn",
    "intro": '<p><strong>"Một ly trà sữa ba mươi nghìn đồng rách nát cũng đòi bước chân vào hào môn nhà chúng tôi sao? Cô chỉ xứng đáng đi phục vụ bưng bê thôi!"</strong></p><p><strong>Trong tiệc đính hôn lộng lẫy, mẹ chồng tương lai lạnh lùng ném hợp đồng thuê mặt bằng bị hủy bỏ vào mặt Lâm Vy, hủy hôn ngay trước mặt hàng trăm khách mời để cưới con gái của một chuỗi trà sữa đối thủ. Lâm Vy bị đuổi khỏi sảnh tiệc, quán trà sữa nhỏ trong hẻm của cô bị phong tỏa và bôi nhọ danh tiếng.</strong></p><hr /><p>Thế nhưng, không ai biết rằng quán trà sữa nhỏ ấy chính là phòng nghiên cứu và phát triển sản phẩm (R&D Lab) cốt lõi của chuỗi đồ uống thuần chay "Sen Việt" đang âm thầm vận hành thử nghiệm chuẩn bị ra mắt toàn quốc. Bắt tay với Giám đốc vận hành chuỗi bán lẻ quốc gia Trần Minh Quốc và sử dụng kết quả kiểm định độc học của Viện Pasteur cùng văn bản đăng ký bảo hộ công thức của Cục Sở hữu Trí tuệ, Lâm Vy đã thực hiện màn livestream vạch trần âm mưu ăn cắp công nghệ cực đỉnh, ký kết hợp đồng trăm tỷ và đẩy gia đình chồng hụt vào cảnh phá sản.</p>',
    "seo": {
        "focus_keyword": "co gai ban tra sua va hop dong tram ty",
        "seo_title": "Cô Gái Bán Trà Sữa Và Hợp Đồng Trăm Tỷ V13",
        "seo_description": "Lâm Vy bị gia đình chồng hụt khinh thường sỉ nhục liền dùng bằng chứng thép đập tan âm mưu cướp công thức, ký hợp đồng trăm tỷ nhượng quyền."
    },
    "chapters": []
}

# Chương 1
c1_content = """
<p>Hương nước hoa đắt tiền quyện cùng mùi rượu vang đỏ thượng hạng lan tỏa khắp sảnh tiệc của trung tâm hội nghị tiệc cưới Riverside Palace quận bốn.</p>
<p>Lâm Vy đứng im lặng giữa sân khấu lớn, bộ váy cưới màu trắng tinh khôi bỗng trở nên lạc lõng vô cùng.</p>
<p>Lồng ngực cô phập phồng dữ dội, bàn tay siết chặt tạt vào tà váy đến mức các khớp ngón tay chuyển sang màu trắng bệch.</p>
<p>"Một ly trà sữa ba mươi nghìn đồng rách nát của cô cũng đòi bước chân vào hào môn nhà chúng tôi sao?"</p>
<p>Bà Nguyễn Thị Lan, mẹ của bạn trai cô, cầm một xấp tài liệu ném thẳng vào người Lâm Vy, những tờ giấy bay lả tả rồi rơi cộp xuống nền đất.</p>
<p>"Đây là thông báo thu hồi mặt bằng quán trà sữa trong hẻm của cô."</p>
<p>"Gia đình tôi đã mua đứt căn nhà đó rồi."</p>
<p>"Con trai tôi là Hoàng Minh phải lấy người có cùng đẳng cấp như Phương Trinh, tiểu thư của chuỗi trà sữa Royal Tea Việt Nam, chứ không phải một đứa bán nước dạo nghèo hèn!"</p>
<p>Hoàng Minh đứng bên cạnh mẹ mình, gã mặc bộ vest chú rể bảnh bao nhưng ánh mắt lẩn tránh, không dám nhìn thẳng vào Lâm Vy.</p>
<p>Gã khẽ nhích người lại gần Phương Trinh đang đứng cười đắc ý, tay trong tay đầy tình cảm.</p>
<p>Lâm Vy nhìn vết mực in đen thẫm trên thông báo thu hồi mặt bằng, đôi mắt cô không hề rơi một giọt nước mắt nào, thay vào đó là sự lạnh lùng và lý tính tột độ.</p>
<p>Da mặt cô hơi tái đi vì tức giận, nhưng giọng nói vẫn vô cùng đanh thép và rành mạch.</p>
<p>"Bà Lan, bà nghĩ rằng hủy bỏ hợp đồng thuê mặt bằng là có thể ép chết tôi sao?"</p>
<p>"Hoàng Minh, anh vì muốn cướp đoạt công thức trà hoa sen phủ kem muối độc quyền của tôi để làm quà cưới cho Phương Trinh mà sẵn sàng dàn dựng màn kịch đê tiện này?"</p>
<p>Phương Trinh nhếch môi cười khẩy, gót giày cao gót nhọn của ả nện xuống nền gạch hoa cương vang lên âm thanh chói tai.</p>
<p>"Lâm Vy, cô nói cái gì là công thức độc quyền?"</p>
<p>"Chuỗi Royal Tea của chúng tôi đã nộp đơn đăng ký bảo hộ công thức đó lên Cục Sở hữu Trí tuệ vào sáng nay rồi."</p>
<p>"Bắt đầu từ ngày mai, nếu quán của cô còn dám bán loại trà đó, tôi sẽ cho quản lý thị trường xuống tịch thu và niêm phong cửa hàng vì vi phạm sở hữu trí tuệ!"</p>
<p>Lâm Vy khẽ nhếch mép, một nụ cười đầy bí ẩn hiện lên trên khuôn mặt xinh đẹp.</p>
<p>"Được, tôi để xem ai mới là kẻ bị niêm phong cửa hàng trước!"</p>
<p>Cô dứt khoát quay người bước đi, chiếc váy cưới dài quết đất bị cô dùng kéo cắt phăng vạt sau ngay trên sân khấu trước sự bàng hoàng của toàn bộ quan khách.</p>
<p>Gót giày cao gót của cô đập mạnh xuống nền nhà sắc lạnh, mỗi bước đi đều chứa đựng quyết tâm đập tan những kẻ phản bội.</p>
"""
story["chapters"].append({"title": "Chương 1: Tiệc Đính Hôn Hủy Bỏ", "content": c1_content})

# Chương 2
c2_content = """
<p>Bước ra khỏi trung tâm tiệc cưới, Lâm Vy lập tức cởi bỏ bộ váy cưới vướng víu, thay vào đó là bộ đồ công sở màu ghi xám thanh lịch.</p>
<p>Cô bước vào quán trà sữa nhỏ mang tên "Sen Việt" trong một con hẻm nhỏ trên đường Nguyễn Đình Chiểu, quận ba.</p>
<p>Nơi này nhìn bề ngoài chỉ là một quán trà sữa đơn sơ, nhưng đằng sau bức tường gỗ trang trí là một phòng Lab nghiên cứu và phát triển sản phẩm (R&D Lab) cực kỳ hiện đại với đầy đủ máy móc kiểm nghiệm, máy ly tâm và các thiết bị chiết xuất nhập khẩu từ Đức.</p>
<p>Ngồi đợi sẵn ở bàn trà là Trần Minh Quốc, Giám đốc Vận hành chuỗi bán lẻ quốc gia VinCommerce.</p>
<p>Anh mặc chiếc áo sơ mi xanh thẫm phẳng phiu, đồng hồ Hublot lấp lánh trên cổ tay, ánh mắt đầy lý tính khẽ lướt nhìn xung quanh phòng Lab.</p>
<p>"Cô Lâm Vy, tôi chỉ quan tâm đến các chỉ số kỹ thuật và tính khả thi thương mại."</p>
<p>"Quỹ đầu tư của tập đoàn chúng tôi đang tìm kiếm một thương hiệu trà thuần chay thuần Việt để nhượng quyền độc quyền trị giá một trăm tỷ đồng."</p>
<p>"Nhưng tôi có những tiêu chuẩn cực kỳ khắt khe:"</p>
<p>"Trong vòng hai mươi bốn giờ tới, cô phải cung cấp cho tôi giấy chứng nhận tiêu chuẩn an toàn thực phẩm ISO 22000 quốc tế cho toàn bộ quy trình chiết xuất trà sen của phòng Lab này."</p>
<p>"Đồng thời, cô phải chứng minh được công thức trà hoa sen phủ kem muối kia không hề bị tranh chấp bản quyền pháp lý với chuỗi Royal Tea."</p>
<p>"Nếu không có hai thứ đó, thương vụ trăm tỷ này sẽ bị hủy bỏ ngay lập tức."</p>
<p>Lâm Vy ngồi đối diện với Minh Quốc, nhịp thở của cô dần ổn định lại sau cơn chấn động ở tiệc đính hôn.</p>
<p>Cô mở ngăn kéo bàn làm việc, lấy ra một tập tài liệu dày đóng dấu giáp lai đỏ chói của Viện Pasteur và Cục Sở hữu Trí tuệ.</p>
<p>"Thưa ông Quốc, đây là giấy chứng nhận ISO 22000 do tập đoàn kiểm định SGS của Thụy Sĩ cấp cho phòng Lab Sen Việt cách đây ba tháng."</p>
<p>"Còn đây là bằng độc quyền giải pháp hữu ích cho quy trình chiết xuất tinh chất hoa sen giữ hương tự nhiên đã được Cục Sở hữu Trí tuệ cấp cho cá nhân tôi từ một năm trước."</p>
<p>"Hồ sơ nộp đơn của Royal Tea sáng nay chỉ là một bản sao chép vụng về công thức của tôi và chắc chắn sẽ bị bác bỏ."</p>
<p>Minh Quốc cúi xuống đọc kỹ từng trang tài liệu, các ngón tay anh khẽ lướt qua con dấu nổi của Cục Sở hữu Trí tuệ.</p>
<p>Gương mặt anh hiện rõ sự kinh ngạc trước sự chuẩn bị pháp lý vô cùng bài bản và chặt chẽ của cô gái trẻ.</p>
<p>"Xuất sắc... Cô Vy, cô thực sự làm tôi bất ngờ."</p>
<p>"Nhưng hiện tại trên mạng xã hội đang lan truyền thông tin quán trà sữa của cô sử dụng hóa chất độc hại gây vô sinh."</p>
<p>"Sở Y tế quận ba đã ký quyết định thanh tra đột xuất cửa hàng của cô vào chín giờ sáng mai."</p>
<p>"Nếu cô không vượt qua được cuộc thanh tra này, hợp đồng của chúng ta vẫn vô hiệu."</p>
<p>Lâm Vy siết chặt các đầu ngón tay, ánh mắt cô lóe lên tia sáng đầy sắc bén.</p>
<p>"Đó là đòn bẩn của Royal Tea."</p>
<p>"Tôi sẽ dùng chính cuộc thanh tra sáng mai để tổ chức một buổi livestream vạch trần bộ mặt thật của chúng trước toàn bộ công chúng!"</p>
"""
story["chapters"].append({"title": "Chương 2: Điều Kiện Nhượng Quyền", "content": c2_content})

# Chương 3
c3_content = """
<p>Đêm hôm đó, tại trụ sở văn phòng của chuỗi trà sữa Royal Tea Việt Nam, Hoàng Minh và Phương Trinh đang ngồi trước màn hình máy tính theo dõi chiến dịch bôi nhọ truyền thông chống lại Sen Việt.</p>
<p>Từng bài viết giật gân, sử dụng các hình ảnh giả mạo về nguyên liệu bẩn chứa hóa chất Trung Quốc được chia sẻ rầm rộ trên các hội nhóm ẩm thực Sài Gòn.</p>
<p>"Minh à, anh chắc chắn là anh đã xóa sạch file camera lưu trữ lúc anh lấy trộm công thức trong máy tính của con Vy rồi chứ?"</p>
<p>Phương Trinh nheo mắt hỏi, ngón tay sơn đỏ gõ nhẹ lên mặt bàn gỗ.</p>
<p>Hoàng Minh cười đắc ý, rót một ly rượu đưa cho ả.</p>
<p>"Em yên tâm đi, anh đã dùng tài khoản admin xóa sạch log hệ thống và camera an ninh của quán rồi."</p>
<p>"Sáng mai khi đoàn thanh tra Sở Y tế đến niêm phong quán của nó, Sen Việt sẽ hoàn toàn biến mất khỏi thị trường."</p>
<p>"Công thức trà sen muối độc quyền đó sẽ hoàn toàn thuộc về Royal Tea chúng ta!"</p>
<p>Lúc này tại phòng Lab Sen Việt, Lâm Vy đang thức trắng đêm cùng đội ngũ kỹ thuật của mình.</p>
<p>Mồ hôi rịn ra ướt đẫm trán cô, làm bết lại vài sợi tóc mai bên má.</p>
<p>Cô biết mình đang phải đối mặt với hạn chót sinh tử trong vòng mười hai giờ tới.</p>
<p>"Chị Vy, hệ thống camera của chúng ta đã bị Hoàng Minh xóa sạch dữ liệu ghi đè từ tối qua rồi."</p>
<p>Tên kỹ thuật viên trẻ tuổi lo lắng nói.</p>
<p>Lâm Vy không hề hoảng loạn, cô đứng thẳng người, khoanh hai tay trước ngực.</p>
<p>"Hoàng Minh chỉ biết hệ thống camera lưu trữ cục bộ."</p>
<p>"Gã không biết tôi đã cài đặt chế độ tự động đồng bộ hóa thời gian thực lên dịch vụ đám mây AWS của Amazon đặt máy chủ tại Singapore."</p>
<p>"Hãy truy cập vào tài khoản AWS dự phòng, tải toàn bộ video ghi hình Hoàng Minh lẻn vào phòng Lab sao chép file công thức vào lúc hai giờ sáng ngày mười lăm tháng năm."</p>
<p>"Tải luôn cả địa chỉ IP truy cập từ máy tính cá nhân của gã."</p>
<p>Khi đoạn video sắc nét hiển thị rõ mồn một hành vi trộm cắp tài liệu của Hoàng Minh hiện lên trên màn hình, các đầu ngón tay của Lâm Vy siết chặt lại.</p>
<p>"Bằng chứng trộm cắp công nghệ đã đủ."</p>
<p>"Ngày mai, cuộc chơi thực sự mới bắt đầu!"</p>
"""
story["chapters"].append({"title": "Chương 3: Đêm Trước Cuộc Chiến", "content": c3_content})

# Chương 4
c4_content = """
<p>Đúng chín giờ sáng ngày hôm sau, ngõ nhỏ Nguyễn Đình Chiểu chật kín người khi đoàn thanh tra liên ngành của Sở Y tế và Quản lý thị trường Thành phố Hồ Chí Minh đỗ xe ngay trước cửa quán Sen Việt.</p>
<p>Hoàng Minh, Phương Trinh cùng bà Lan cũng có mặt, đi sau họ là một nhóm phóng viên báo chí do chúng thuê để đưa tin trực tiếp cảnh niêm phong cửa hàng.</p>
<p>"Bà con nhìn xem! Hôm nay cơ quan chức năng sẽ niêm phong quán trà sữa bẩn này!"</p>
<p>Bà Lan lớn tiếng rêu rao trước đám đông người dân xung quanh.</p>
<p>Trưởng đoàn thanh tra bước vào quán, nét mặt vô cùng nghiêm nghị.</p>
<p>"Cô Lâm Vy, chúng tôi nhận được đơn tố cáo nặc danh kèm theo bằng chứng hình ảnh về việc cửa hàng sử dụng phụ gia công nghiệp không rõ nguồn gốc."</p>
<p>"Yêu cầu cô xuất trình toàn bộ giấy tờ nguyên liệu và cho phép kiểm tra phòng Lab."</p>
<p>Lâm Vy đứng sau quầy pha chế, bộ đồ công sở phẳng phiu tôn lên phong thái tự tin đáng kinh ngạc của cô.</p>
<p>Cô không hề sợ hãi, mà lập tức bấm nút khởi động hệ thống camera livestream độ phân giải cao đã được chuẩn bị sẵn, phát trực tiếp trên trang cá nhân có hơn một triệu người theo dõi của thương hiệu Sen Việt.</p>
<p>"Kính thưa toàn thể quý khách hàng và cơ quan chức năng."</p>
<p>"Hôm nay, Sen Việt hoàn toàn mở cửa phòng Lab R&D để đoàn thanh tra kiểm tra công khai trước sự giám sát của hàng chục ngàn người đang xem livestream."</p>
<p>Lâm Vy dẫn đoàn thanh tra bước vào phòng Lab hiện đại.</p>
<p>Cô xuất trình toàn bộ hóa đơn mua nguyên liệu trà sen tươi từ các hợp tác xã chuẩn VietGAP ở Đồng Tháp, kèm theo biên lai chuyển khoản ngân hàng Techcombank đối ứng cho từng lô hàng.</p>
<p>Đặc biệt, cô trình bày bản kết quả phân tích độc học của Viện Pasteur TP.HCM khẳng định tất cả các mẫu trà của Sen Việt đều không chứa bất kỳ dư lượng hóa chất bảo vệ thực vật hay kim loại nặng nào.</p>
<p>Vị Trưởng đoàn thanh tra sau khi kiểm tra kỹ lưỡng các trang thiết bị hiện đại và hồ sơ pháp lý, khuôn mặt ông giãn ra, gật đầu đầy tán thưởng.</p>
<p>"Quy trình vô trùng đạt chuẩn ISO 22000, nguyên liệu có nguồn gốc rõ ràng, kết quả kiểm nghiệm hoàn toàn đạt tiêu chuẩn quốc gia."</p>
<p>"Thông tin tố cáo hoàn toàn vô căn cứ!"</p>
<p>Đám đông người dân xung quanh và người xem livestream lập tức bùng nổ những lời khen ngợi dành cho sự minh bạch của Sen Việt.</p>
"""
story["chapters"].append({"title": "Chương 4: Livestream Minh Bạch", "content": c4_content})

# Chương 5
c5_content = """
<p>Nhìn thấy đoàn thanh tra tuyên bố Sen Việt đạt chuẩn, Phương Trinh mặt tái xám, vội vàng lên tiếng phá bĩnh.</p>
<p>"Cho dù không sử dụng hóa chất bẩn, công thức trà sen phủ kem muối của cô vẫn là ăn cắp từ chuỗi Royal Tea của chúng tôi!"</p>
<p>"Hồ sơ bảo hộ của chúng tôi đã được gửi lên Cục Sở hữu Trí tuệ rồi!"</p>
<p>Lâm Vy nhìn thẳng vào ống kính livestream, khóe môi khẽ nhếch lên một nụ cười đầy lạnh lùng.</p>
<p>"Phương Trinh, cô thích nói về sở hữu trí tuệ đúng không?"</p>
<p>"Vậy hãy để tôi cho toàn bộ khán giả xem đoạn video này."</p>
<p>Lên màn hình livestream lập tức trình chiếu đoạn video trích xuất từ đám mây AWS.</p>
<p>Hình ảnh Hoàng Minh lẻn vào phòng Lab lúc hai giờ sáng, dùng ổ cứng di động sao chép các tệp công thức pha chế hiện lên rõ nét đến từng chi tiết trên khuôn mặt gã hốt hoảng.</p>
<p>Kèm theo đó là bảng tra cứu lịch sử truy cập hệ thống từ địa chỉ IP mạng nhà riêng của Hoàng Minh.</p>
<p>Hoàng Minh nhìn màn hình, toàn thân gã run lẩy bẩy, chiếc điện thoại trên tay rơi xuống đất vỡ nát, mồ hôi lạnh tuôn ra như tắm ướt đẫm cả chiếc áo sơ mi lụa đắt tiền.</p>
<p>"Không... không thể như thế được... anh đã xóa sạch camera rồi mà..."</p>
<p>Lâm Vy dõng dạc tuyên bố trước hàng trăm ngàn người xem livestream:</p>
<p>"Đây là bằng chứng Hoàng Minh ăn cắp bí mật công nghệ của công ty chúng tôi."</p>
<p>"Cục Sở hữu Trí tuệ đã chính thức ra văn bản bác bỏ hồ sơ của Royal Tea và ban hành quyết định xử phạt vi phạm sở hữu công nghiệp đối với chuỗi của các người."</p>
<p>Bà Lan nghe đến đây thì đứng không vững, ngã quỵ xuống nền đất ẩm ướt của con hẻm nhỏ, miệng lẩm bẩm trong vô vọng.</p>
<p>"Hủy hoại rồi... con trai tôi... chuỗi cửa hàng của chúng tôi..."</p>
<p>Đúng lúc đó, lực lượng cảnh sát kinh tế công an quận ba bước vào quán, áp giải Hoàng Minh và Phương Trinh đi vì hành vi xâm phạm bí mật kinh doanh quy mô lớn.</p>
"""
story["chapters"].append({"title": "Chương 5: Vả Mặt Kẻ Trộm Công Thức", "content": c5_content})

# Chương 6
c6_content = """
<p>Mặc dù Hoàng Minh và Phương Trinh đã bị bắt, thế nhưng gia đình bạn trai cũ vẫn cố gắng dùng mối quan hệ cuối cùng để trả thù.</p>
<p>Bố của Hoàng Minh, ông Hoàng Văn Hùng — một cổ đông lớn của ngân hàng thương mại cổ phần — đã dùng quyền lực của mình để yêu cầu ngân hàng phong tỏa toàn bộ tài khoản thanh toán quốc tế của Sen Việt.</p>
<p>Đồng thời, ông ta gửi đơn khiếu nại lên Sở Kế hoạch và Đầu tư cáo buộc Sen Việt hoạt động kinh doanh không đúng giấy phép đăng ký để đình chỉ hoạt động của chuỗi.</p>
<p>Khủng hoảng pháp lý và tài chính hai mươi bốn giờ tiếp tục đè nặng lên vai Lâm Vy khi cô đang chuẩn bị ký kết hợp đồng nhượng quyền với tập đoàn bán lẻ của Trần Minh Quốc.</p>
<p>Tại văn phòng đại diện Sen Việt, Trần Minh Quốc ngồi đăm chiêu, ngón tay trỏ gõ mạnh lên mặt bàn kính.</p>
<p>"Vy, ban hội đồng quản trị của tập đoàn chúng tôi đang vô cùng lo ngại về đòn phong tỏa tài khoản này."</p>
<p>"Nếu tài khoản thanh toán quốc tế của cô bị khóa, quy trình nhập khẩu thiết bị phòng Lab đợt hai trị giá hai mươi tỷ đồng từ Đức sẽ bị hủy bỏ."</p>
<p>"Chúng ta chỉ có đúng mười hai tiếng để gỡ bỏ phong tỏa này trước khi hợp đồng đầu tư bị tự động hủy bỏ theo điều khoản cam kết."</p>
<p>Lâm Vy đứng bên cửa sổ nhìn xuống đường phố tấp nập, lồng ngực cô phập phồng dữ dội dưới lớp áo sơ mi trắng.</p>
<p>Các đầu ngón tay cô siết chặt đến mức hằn đỏ, nhưng ánh mắt cô vẫn tràn đầy sự lý tính sắc bén.</p>
<p>"Ông Quốc, ông hãy chuẩn bị sẵn hợp đồng ký kết."</p>
<p>"Tôi sẽ trực tiếp đến Sở Kế hoạch Đầu tư và gỡ phong tỏa ngân hàng của Hoàng Văn Hùng trong vòng bốn tiếng tới."</p>
<p>"Kẻ muốn lừa dối pháp luật sẽ phải trả giá đắt!"</p>
"""
story["chapters"].append({"title": "Chương 6: Đòn Phong Tỏa Cuối Cùng", "content": c6_content})

# Chương 7
c7_content = """
<p>Chiều hôm đó, tại phòng tiếp dân của Sở Kế hoạch và Đầu tư Thành phố Hồ Chí Minh, ông Hoàng Văn Hùng cùng nhóm luật sư đang đắc ý chờ đợi quyết định đình chỉ giấy phép hoạt động của Sen Việt.</p>
<p>Lâm Vy bước vào phòng họp cùng Trần Minh Quốc, trên tay cô cầm một tập tài liệu đóng dấu đỏ của Ngân hàng Nhà nước Việt Nam và Ủy ban Chứng khoán Nhà nước.</p>
<p>"Hoàng Văn Hùng, ông nghĩ mình có thể dùng quyền lực ngân hàng tư nhân để thao túng hoạt động kinh doanh hợp pháp của chúng tôi sao?"</p>
<p>Lâm Vy ném mạnh tập tài liệu lên bàn trước mặt vị Giám đốc Sở và ông Hùng.</p>
<p>Tài liệu hiển thị chi tiết hành vi thao túng cổ phiếu và cho vay sai đối tượng ưu đãi trị giá hàng trăm tỷ đồng của cá nhân ông Hùng tại ngân hàng do ông ta làm cổ đông lớn.</p>
<p>Quan trọng hơn, có văn bản kết luận thanh tra khẩn cấp của Ngân hàng Nhà nước xác định quyết định phong tỏa tài khoản của Sen Việt là hoàn toàn trái quy định pháp luật và mang tính chất tư thù cá nhân.</p>
<p>"Thưa Giám đốc Sở, đây là hành vi lạm dụng chức vụ quyền hạn trong hoạt động tín dụng nhằm triệt hạ doanh nghiệp khởi nghiệp trong nước."</p>
<p>Trần Minh Quốc bước lên dõng dạc tuyên bố bằng giọng nói đanh thép đầy uy lực.</p>
<p>"Tập đoàn VinCommerce chúng tôi cam kết bảo trợ pháp lý toàn diện cho Sen Việt."</p>
<p>"Nếu quyết định đình chỉ vô căn cứ này được ban hành, chúng tôi sẽ khởi kiện yêu cầu bồi thường thiệt hại hàng trăm tỷ đồng!"</p>
<p>Giám đốc Sở Kế hoạch Đầu tư nhìn tập tài liệu thanh tra của Ngân hàng Nhà nước, mặt ông lập tức trở nên nghiêm nghị.</p>
<p>Ông thẳng thừng bác bỏ đơn khiếu nại của Hoàng Văn Hùng và ký văn bản xác nhận hoạt động hợp pháp của Sen Việt.</p>
<p>Hoàng Văn Hùng mặt xám ngoét không còn một giọt máu, toàn thân run rẩy ngã khuỵu xuống ghế da khi nhận được tin nhắn đình chỉ chức vụ từ hội đồng quản trị ngân hàng.</p>
<p>Gia đình bạn trai cũ của Lâm Vy đã hoàn toàn sụp đổ dưới đòn đánh chí mạng của cô.</p>
"""
story["chapters"].append({"title": "Chương 7: Đòn Quyết Định", "content": c7_content})

# Chương 8
c8_content = """
<p>Một tháng sau, lễ ký kết hợp đồng hợp tác chiến lược và nhượng quyền thương hiệu trị giá một trăm tỷ đồng giữa chuỗi trà sen thuần Việt "Sen Việt" và tập đoàn bán lẻ VinCommerce được tổ chức vô cùng trang trọng tại khán phòng lớn của khách sạn Park Hyatt Sài Gòn.</p>
<p>Ánh đèn sân khấu rực rỡ chiếu sáng lộng lẫy lên tấm bảng ký kết hợp đồng khổng lồ.</p>
<p>Lâm Vy diện bộ đầm dạ hội màu xanh ngọc bích vô cùng sang trọng, tôn lên vẻ đẹp đài các, thông minh và đầy bản lĩnh của một nữ doanh nhân thành đạt.</p>
<p>Bên cạnh cô, Trần Minh Quốc lịch lãm trong bộ vest đen sang trọng.</p>
<p>Sau khi đặt bút ký vào bản hợp đồng lịch sử, Minh Quốc quay sang nhìn Lâm Vy, ánh mắt anh không còn sự lý tính lạnh lùng của một chuyên gia tài chính mà tràn ngập tình cảm dịu dàng, chân thành tự nguyện.</p>
<p>Anh chủ động bước lại gần, nắm lấy bàn tay mềm mại của cô khẽ siết nhẹ.</p>
<p>"Lâm Vy, em thực sự là người con gái bản lĩnh và sắc sảo nhất mà anh từng gặp trong đời."</p>
<p>"Hôm nay, trước sự chứng kiến của hàng trăm đối tác lớn, anh muốn đưa ra một đề xuất hợp tác mới với em."</p>
<p>Lâm Vy mỉm cười nhẹ, ánh mắt long lanh nhìn anh.</p>
<p>"Đề xuất gì vậy, thưa ông Giám đốc vận hành?"</p>
<p>"Anh muốn đồng hành cùng em xây dựng không chỉ chuỗi Sen Việt, mà là cả tương lai rực rỡ phía trước."</p>
<p>"Em đồng ý ký vào bản hợp đồng trọn đời này với anh chứ?"</p>
<p>Lâm Vy nhìn sâu vào đôi mắt chứa chan tình cảm của người đàn ông đã sát cánh cùng cô vượt qua giông bão.</p>
<p>"Em đồng ý, thưa anh Quốc!"</p>
<p>Tiếng pháo hoa chúc mừng vang dội khắp khán phòng lộng lẫy, tiếng vỗ tay của hàng trăm quan khách kéo dài không dứt, đánh dấu sự thắng lợi vinh quang của cô gái bán trà sữa kiên cường và một tình yêu viên mãn nghìn tỷ.</p>
"""
story["chapters"].append({"title": "Chương 8: Hào Môn Trăm Tỷ Thực Sự", "content": c8_content})

# Save JSON
os.makedirs("/Users/aaronnguyen/TN/App/doctieuthuyet/scratch", exist_ok=True)
with open("/Users/aaronnguyen/TN/App/doctieuthuyet/scratch/rewrite_2106_v13.json", "w", encoding="utf-8") as f:
    json.dump(story, f, ensure_ascii=False, indent=2)

print("Generated rewrite_2106_v13.json successfully!")
