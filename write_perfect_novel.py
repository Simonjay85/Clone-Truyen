# -*- coding: utf-8 -*-
import json
import os

final_file_path = "/Users/aaronnguyen/TN/App/doctieuthuyet/pending_novel_10.json"

novel_data = {
    "idx": 10,
    "title": "Chúa Đảo Resort Phú Quốc: Bị Đuổi Khỏi Resort Mình Xây, Tôi Mua Cả Hòn Đảo",
    "author": "Trịnh Gia Bảo",
    "genre": "Sảng Văn",
    "intro": "<p><strong>\"Cậu nghĩ một kiến trúc sư tay trắng không thế lực như cậu có thể giữ nổi một thiên đường nghìn tỷ này sao? Biến khỏi Phú Quốc trước khi tôi khiến cậu biến mất vĩnh viễn!\"</strong></p>\\n<p>Trịnh Gia Bảo, kiến trúc sư thiên tài đứng sau Băng Dương Resort - siêu dự án sinh thái 5 sao tại Bãi Sao, bị đối tác ngoại quốc Bernard Dupont và gã trợ lý phản bội Lê Văn Hùng giả mạo giấy tờ chiếm đoạt trắng trợn toàn bộ công sức.</p>\\n<p>Giữa lúc bị dồn vào đường cùng, anh gặp Nguyễn Phương Thảo, nữ Phó Chủ tịch UBND tỉnh Kiên Giang sắc sảo và chính trực. Cùng nhau, họ lập nên một liên minh thép, không chỉ lột trần bộ mặt thật của sòng bạc trá hình Băng Dương mà còn giúp Gia Bảo thâu tóm các hòn đảo hoang sơ phía nam An Thới, trở thành vị Chúa Đảo thực thụ của đảo ngọc Phú Quốc.</p>",
    "chapters": []
}

# Chapter 1
ch1 = """<p>Gió biển Phú Quốc về đêm mang theo vị mặn mòi đặc trưng, thổi lướt qua những rặng dừa xanh mướt chạy dọc bãi cát trắng mịn của Bãi Sao.</p>
<p>Dưới ánh đèn LED nghệ thuật lung linh hắt ra từ khu sảnh chính đón khách, Băng Dương Resort hiện lên như một viên ngọc lục bảo khổng lồ, lộng lẫy và hoàn mỹ.</p>
<p>Mỗi viên đá lát đường, mỗi kết cấu mái vòm bằng tre tầm vông uốn lượn, cho đến hệ thống tuần hoàn nước tự nhiên thân thiện với môi trường đều mang đậm dấu ấn sáng tạo của Trịnh Gia Bảo.</p>
<p>Anh đứng trên ban công tầng cao nhất của khu biệt thự VIP, ánh mắt tràn đầy sự tự hào khi nhìn đứa con tinh thần mà mình đã thức trắng hàng trăm đêm để hoàn thiện.</p>
<p>Ngày mai là lễ khai trương chính thức của Băng Dương Resort, đánh dấu bước ngoặt đưa Phú Quốc lên bản đồ du lịch sinh thái xa xỉ thế giới.</p>
<p>\"Đẹp thật đúng không, Gia Bảo?\" Một giọng nói trầm thấp vang lên phía sau, mang theo sự đắc ý không hề giấu diếm.</p>
<p>Gia Bảo quay đầu lại, nhìn thấy đối tác ngoại quốc Bernard Dupont, người đại diện cho quỹ đầu tư viễn dương và bên cạnh là Lê Văn Hùng - gã trợ lý trung thành đã đồng hành cùng anh suốt năm năm qua.</p>
<p>\"Bernard, Hùng, hai người chưa nghỉ ngơi sao? Ngày mai chúng ta có rất nhiều việc phải làm,\" Gia Bảo mỉm cười ôn hòa, không hề nghi ngờ.</p>
<p>Bernard không trả lời, gã chỉ nhấp một ngụm rượu vang đỏ thượng hạng, khẽ lắc ly thủy tinh để những vệt đỏ sẫm bám vào thành ly, như máu.</p>
<p>Lê Văn Hùng bước lên phía trước, sắc mặt gã lạnh lùng, không còn vẻ khúm núm thường ngày, gã đặt lên bàn một xấp tài liệu dày cộp bọc da đen.</p>
<p>\"Anh Bảo, đây là biên bản chuyển nhượng toàn bộ quyền sở hữu trí tuệ và 45% cổ phần sáng lập của anh tại Băng Dương cho tập đoàn Dupont,\" Hùng nói, giọng điệu vô cảm nhưng đâm thẳng vào tim Gia Bảo.</p>
<p>Gia Bảo nhướng mày, nụ cười trên môi đông cứng lại: \"Hùng, cậu đang đùa cái gì vậy? Hợp đồng sáng lập của chúng ta ghi rõ tôi giữ bản quyền thiết kế và quyền điều hành sinh thái.\"</p>
<p>\"Đó là chuyện của ngày hôm qua thôi, kiến trúc sư Trịnh,\" Bernard bật cười thành tiếng, giọng nói mang vẻ khinh miệt rõ rệt bằng thứ tiếng Việt lơ lớ.</p>
<p>\"Chúng tôi đã nộp hồ sơ đăng ký quyền sở hữu mới lên Văn phòng Đăng ký Đất đai và Sở Kế hoạch và Đầu tư tỉnh Kiên Giang.\"</p>
<p>\"Chữ ký và con dấu của anh trên biên bản đồng ý chuyển nhượng tài sản cá nhân để cấn trừ nợ đầu tư đều rất rõ ràng, đã được phòng công chứng số 1 tỉnh xác nhận.\"</p>
<p>Gia Bảo giật phắt xấp tài liệu, ngón tay anh run nhẹ khi lật đến trang cuối cùng.</p>
<p>Dưới ánh đèn, chữ ký của anh hiện lên sắc nét, thậm chí cả dấu vân tay đỏ chót cũng trùng khớp một cách hoàn hảo.</p>
<p>\"Giả mạo! Các người điên rồi! Tôi chưa từng ký bất kỳ văn bản chuyển nhượng nào thế này!\" Gia Bảo gầm lên, lồng ngực phập phồng dữ dội.</p>
<p>Anh trừng mắt nhìn Lê Văn Hùng, người duy nhất có thể tiếp cận con dấu cá nhân và các giấy tờ ủy quyền của anh.</p>
<p>\"Hùng! Tại sao? Tôi đã đối xử với cậu như anh em ruột thịt, chia cho cậu 5% cổ phần từ phần của tôi cơ mà!\" Gia Bảo siết chặt cổ áo Hùng, đôi mắt đỏ ngầu.</p>
<p>Lê Văn Hùng gạt tay Gia Bảo ra một cách thô bạo, chỉnh lại cổ áo, nở nụ cười khinh bỉ.</p>
<p>\"Anh em ruột thịt? Anh Bảo à, anh sống trên mây lâu quá rồi,\" Hùng nhổ nước bọt xuống sàn đá.</p>
<p>\"Anh muốn biến nơi này thành khu bảo tồn sinh thái sinh quyển, từ chối mọi lời mời hợp tác sòng bạc, từ chối câu lạc bộ giải trí VIP thu phí nghìn đô.\"</p>
<p>\"Anh có biết chúng ta đang ngồi trên một mỏ vàng không? Nhưng tư duy của anh quá bảo thủ!\"</p>
<p>\"Ông Bernard đã hứa cho tôi vị trí Tổng Giám đốc điều hành Băng Dương, kèm theo biệt thự ven biển và tài khoản mở tại Singapore.\"</p>
<p>\"Còn anh? Anh chỉ cho tôi vài đồng bạc lẻ từ tiền lương thiết kế!\" Hùng cười lạnh lùng.</p>
<p>Gia Bảo đứng sững như trời trồng, mồ hôi lạnh chảy ròng ròng dọc sống lưng.</p>
<p>Anh nhận ra mình đã quá ngây thơ khi tin vào lòng người, quá tập trung vào nghệ thuật kiến trúc mà quên đi những cạm bẫy thương trường tàn khốc.</p>
<p>\"Bernard, ông không thể làm vậy. Hồ sơ thiết kế cơ sở của tôi đã được nộp lưu trữ tại Bộ Xây Dựng, giấy phép môi trường của dự án này dựa trên cam kết sinh thái 100%,\" Gia Bảo cố giữ bình tĩnh, lên tiếng cảnh cáo.</p>
<p>\"Ồ, cậu Trịnh thân mến,\" Bernard bước tới, vỗ mạnh vào vai Gia Bảo đến mức anh lảo đảo.</p>
<p>\"Cậu nghĩ một kiến trúc sư tay trắng không thế lực như cậu có thể giữ nổi một thiên đường nghìn tỷ này sao?\"</p>
<p>\"Báo chí ngày mai sẽ đăng tin kiến trúc sư Trịnh Gia Bảo bị trầm cảm nặng, tự nguyện rút lui khỏi dự án và chuyển nhượng cổ phần.\"</p>
<p>\"Nếu cậu dám gây rắc rối, tôi sẽ dùng thế lực của mình khiến cậu biến mất vĩnh viễn khỏi đảo ngọc này.\"</p>
<p>Bernard khẽ búng tay, lập tức bốn gã bảo vệ cao lớn mặc vest đen, đeo tai nghe bước vào phòng, áp sát Gia Bảo.</p>
<p>\"Mời cậu Trịnh rời khỏi resort ngay lập tức. Từ bây giờ, cậu là người không được chào đón tại Băng Dương,\" Hùng lớn tiếng ra lệnh đầy hống hách.</p>
<p>Trời đổ mưa rào đột ngột, những hạt mưa Phú Quốc lạnh ngắt dội thẳng vào mặt Gia Bảo khi anh bị đẩy ra khỏi cổng chào bằng tre khổng lồ.</p>
<p>Vali quần áo của anh bị quăng thẳng xuống vũng nước bẩn bên lề đường.</p>
<p>Phía sau anh, cánh cổng sắt nặng nề đóng sầm lại, những ánh đèn lung linh của resort như đang chế giễu sự thất bại cay đắng của kẻ sáng lập.</p>
<p>Nước mưa hòa lẫn nước mắt, nhưng ánh mắt của Trịnh Gia Bảo không hề có sự tuyệt vọng.</p>
<p>Dưới ánh chớp xé toạc bầu trời đêm An Thới, anh quay lại nhìn Băng Dương Resort lần cuối, hàm răng nghiến chặt đến rớm máu.</p>
<p>\"Bernard, Lê Văn Hùng... Các người cướp đi đứa con tinh thần của tôi, biến nó thành công cụ cờ bạc dơ bẩn.\"</p>
<p>\"Tôi thề, tôi sẽ bắt các người phải trả giá gấp trăm lần! Tôi sẽ mua lại toàn bộ vùng biển này, biến các người thành những kẻ không nhà!\" Gia Bảo gầm lên trong tiếng sấm rền.</p>"""

# Chapter 2
ch2 = """<p>Ba ngày sau cơn ác mộng ở Bãi Sao, Trịnh Gia Bảo lặng lẽ bước lên chuyến phà cao tốc từ cảng Bãi Vòng về Rạch Giá.</p>
<p>Anh không mang theo gì nhiều ngoài một chiếc ba lô cũ chứa máy tính cá nhân và cuốn sổ ký họa dày cộp chứa đựng hàng trăm bản vẽ tay về các hòn đảo hoang phía nam Phú Quốc.</p>
<p>Gương mặt anh phờ phạc, râu quai nón lún phún mọc, nhưng đôi mắt sáng quắc như chim ưng lại mang một ý chí sắt đá không thể lay chuyển.</p>
<p>Anh ngồi ở băng ghế phía sau boong tàu, gió biển lồng lộng thổi bay mái tóc rối bời.</p>
<p>Anh đang xem lại các sơ đồ địa hình của quần đảo An Thới - nơi vẫn chưa bị các tập đoàn bất động sản lớn tàn phá.</p>
<p>\"Bản vẽ này rất có tầm nhìn, nhưng tại sao lại chọn Hòn Dăm Ngoài? Nơi đó toàn đá ngầm, dòng hải lưu lại phức tạp.\"</p>
<p>Một giọng nói trong trẻo, mang theo khí chất của người làm chủ vang lên bên cạnh Gia Bảo.</p>
<p>Anh giật mình ngẩng đầu lên, đập vào mắt là một người phụ nữ trẻ chừng ba mươi tuổi, mặc một chiếc sơ mi trắng đơn giản kết hợp quần tây ống đứng thanh lịch.</p>
<p>Mái tóc cô buộc cao gọn gàng, cặp kính cận gọng mảnh không che giấu được ánh mắt thông tuệ, sắc sảo nhưng vô cùng ấm áp.</p>
<p>Đó là Nguyễn Phương Thảo - người vừa được bổ nhiệm làm Phó Chủ tịch UBND tỉnh Kiên Giang phụ trách mảng du lịch và phát triển đô thị chỉ một tháng trước.</p>
<p>Cô đang thực hiện chuyến đi thực tế ẩn danh đến Phú Quốc để đánh giá lại các dự án đang bị phản ánh là tàn phá môi trường tự nhiên.</p>
<p>Gia Bảo khẽ khép cuốn sổ lại, lịch sự trả lời: \"Chào cô. Hòn Dăm Ngoài tuy đá ngầm nhiều, nhưng đó lại là lá chắn tự nhiên hoàn hảo chống lại các cơn bão từ phía Tây Nam.\"</p>
<p>\"Hơn nữa, rạn san hô quanh hòn đảo này là nguyên vẹn nhất Phú Quốc. Nếu xây dựng một resort sinh thái hoàn toàn nổi trên nước bằng vật liệu nhẹ, chúng ta không cần chặt phá một cái cây nào trên đảo.\"</p>
<p>Phương Thảo khẽ nhướng mày, ánh mắt cô sáng lên khi nhận ra người đàn ông trước mặt không phải là một du khách bình thường.</p>
<p>\"Xây dựng nổi trên nước? Chi phí đầu tư sẽ tăng gấp ba lần, và việc xử lý nước thải sinh hoạt sẽ là một cơn ác mộng kỹ thuật. Không một doanh nghiệp nào muốn làm điều đó khi họ có thể dễ dàng san lấp bãi cát,\" Phương Thảo thử lòng.</p>
<p>Gia Bảo cười nửa miệng, nụ cười mang theo chút tự giễu nhưng vô cùng tự tin.</p>
<p>\"Đó là vì họ chỉ muốn kiếm tiền nhanh từ việc bán biệt thự phân lô, chứ không phải làm du lịch bền vững.\"</p>
<p>\"Hệ thống xử lý nước thải sinh học ba cấp bằng tảo biển và vi sinh có thể giải quyết triệt để vấn đề này, thậm chí nước sau xử lý còn đạt tiêu chuẩn nuôi cá biển.\"</p>
<p>\"Tôi đã thiết kế một hệ thống như vậy tại...\" Gia Bảo bỗng ngập ngừng, lồng ngực khẽ thắt lại khi nghĩ đến Băng Dương Resort.</p>
<p>Phương Thảo quan sát nét mặt thay đổi của anh, cô khẽ mỉm cười và chìa tay ra: \"Tôi là Nguyễn Phương Thảo. Anh là Trịnh Gia Bảo đúng không? Kiến trúc sư trưởng của Băng Dương Resort?\"</p>
<p>Gia Bảo sững sờ: \"Cô biết tôi?\"</p>
<p>Phương Thảo gật đầu, cô ngồi xuống băng ghế đối diện anh, phong thái vô cùng tự nhiên và đĩnh đạc.</p>
<p>\"Bản thiết kế sinh thái của Băng Dương Resort từng là đề án xuất sắc nhất được trình lên UBND tỉnh năm ngoái. Tôi đã nghiên cứu rất kỹ tài liệu đó trước khi nhận chức.\"</p>
<p>\"Nhưng hai ngày trước, tôi nhận được báo cáo điều chỉnh quy hoạch từ tập đoàn Dupont. Họ muốn chuyển đổi khu rừng phòng hộ phía sau dự án thành tổ hợp khách sạn cao tầng và câu lạc bộ VIP giải trí có thưởng - nói thẳng ra là sòng bạc trá hình.\"</p>
<p>\"Và điều làm tôi ngạc nhiên nhất là hồ sơ ký tên anh lại đồng ý với toàn bộ những thay đổi mang tính hủy hoại sinh thái đó.\"</p>
<p>Gia Bảo lập tức đứng bật dậy, hai tay nắm chặt thành đấm, mắt đổ lửa: \"Tôi không hề ký! Đó là giấy tờ giả mạo!\"</p>
<p>\"Lê Văn Hùng và Bernard Dupont đã lấy cắp con dấu cá nhân của tôi, làm giả chữ ký để cướp quyền sở hữu và thay đổi toàn bộ triết lý của dự án!\"</p>
<p>Phương Thảo không hề bất ngờ trước phản ứng của anh, cô khẽ ra hiệu cho Gia Bảo ngồi xuống để tránh thu hút sự chú ý của các hành khách khác.</p>
<p>\"Tôi biết chữ ký đó có vấn đề. Nét chữ ký của một kiến trúc sư luôn có độ phóng khoáng đặc trưng của người vẽ, còn nét ký trong hồ sơ mới lại quá cứng nhắc và đều đặn, giống như được đồ lại,\" Phương Thảo bình thản phân tích.</p>
<p>\"Đó là lý do tôi chưa ký duyệt tờ trình điều chỉnh quy hoạch của họ. Tuy nhiên, họ có sự hậu thuẫn pháp lý rất mạnh từ các văn phòng công chứng và một vài thế lực ngầm tại địa phương.\"</p>
<p>Gia Bảo nhìn thẳng vào mắt Phương Thảo, nhận ra sự chính trực và quyết tâm bảo vệ Phú Quốc của nữ lãnh đạo trẻ tuổi này.</p>
<p>Anh hít một hơi thật sâu, giọng nói trở nên trầm ổn: \"Chị Thảo, tôi có giữ bản gốc thiết kế cơ sở và các chứng từ giao dịch chứng minh nguồn vốn ban đầu là từ cá nhân tôi đóng góp.\"</p>
<p>\"Nhưng hiện tại tôi đã bị đuổi khỏi dự án, không có tiếng nói pháp lý để khởi kiện một tập đoàn đa quốc gia.\"</p>
<p>Phương Thảo khẽ xoay cây bút trên tay, ánh mắt cô hiện lên vẻ kiên định.</p>
<p>\"Anh Bảo, một mình anh thì không thể, nhưng nếu có sự vào cuộc của chính quyền tỉnh với danh nghĩa thanh tra sai phạm quy hoạch đất đai và bảo tồn rừng phòng hộ thì lại là chuyện khác.\"</p>
<p>\"Tôi cần anh giúp tôi tìm ra các chứng cứ vật lý về việc họ giả mạo hồ sơ năng lực và các vi phạm xây dựng thực tế tại công trường.\"</p>
<p>\"Ngược lại, tôi sẽ bảo đảm quyền lợi hợp pháp của anh được bảo vệ, và quan trọng hơn... tôi sẽ giúp anh có cơ hội hiện thực hóa giấc mơ sinh thái thật sự của mình tại quần đảo An Thới.\"</p>
<p>Gia Bảo nhìn ra ngoài khơi xa, nơi những hòn đảo hoang sơ đang nhấp nhô giữa làn sóng xanh biếc.</p>
<p>Một kế hoạch phản công vĩ đại bắt đầu hình thành trong đầu anh.</p>
<p>Anh quay lại nhìn Phương Thảo, siết chặt bàn tay cô: \"Thỏa thuận thế đi. Tôi sẽ cho Bernard biết thế nào là cái giá của sự phản bội.\"</p>"""

# Chapter 3
ch3 = """<p>Tại Băng Dương Resort, không khí chuẩn bị cho lễ khai trương đang diễn ra vô cùng khẩn trương và náo nhiệt.</p>
<p>Lê Văn Hùng đứng ở đại sảnh lớn, mặc một bộ vest sang trọng đặt may riêng từ nhà mốt hàng đầu châu Âu, trên ngực tự hào đeo bảng tên vàng óng ánh dòng chữ \"Tổng Giám đốc Điều hành\".</p>
<p>Gã đắc ý nhìn ngắm hàng trăm nhân viên đang tất bật lau chùi, trang hoàng những bình hoa ly khổng lồ dưới sự chỉ đạo của mình.</p>
<p>Từ một gã trợ lý quèn chuyên chạy việc vặt nâng khăn sửa túi cho Trịnh Gia Bảo, giờ đây gã đã đứng trên đỉnh cao quyền lực của một resort 5 sao lớn nhất Phú Quốc.</p>
<p>\"Tổng Giám đốc Hùng, ông Dupont đang đợi ông trong phòng họp VIP thượng đỉnh trên tầng 5,\" một cô thư ký xinh đẹp bước đến, cúi đầu kính cẩn báo cáo.</p>
<p>Hùng khẽ hất cằm lên cao, tỏ vẻ vô cùng hài lòng với danh xưng mới đầy quyền lực này: \"Được rồi, cô đi chuẩn bị tài liệu đi, tôi đến phòng họp ngay lập tức.\"</p>
<p>Trong phòng họp VIP, Bernard Dupont đang ngồi tựa lưng vào chiếc ghế da thuộc Ý màu đen lớn, khuôn mặt gã đầy vẻ tính toán nham hiểm bên cạnh các bản đồ quy hoạch ranh giới đã bị sửa đổi tinh vi.</p>
<p>\"Hùng, cậu làm việc rất xuất sắc. Việc loại bỏ hoàn toàn gã kiến trúc sư gàn dở Trịnh Gia Bảo giúp chúng ta tiết kiệm được rất nhiều thời gian quý báu,\" Bernard cười lớn đầy sảng khoái, rót cho Hùng một ly rượu mạnh Macallan 25 năm.</p>
<p>\"Ông chủ quá khen. Trịnh Gia Bảo chỉ là một kẻ mơ mộng viển vông giữa ban ngày thôi,\" Hùng đón lấy ly rượu bằng cả hai tay, khom lưng cung kính hết mức.</p>
<p>\"Anh ta muốn bảo tồn từng rặng san hô cũ kỹ, từng cái cây cổ thụ vô giá trị, khiến chi phí xây dựng móng nổi tăng vọt và làm giảm đến 60% diện tích phòng có thể khai thác.\"</p>
<p>\"Bây giờ không còn anh ta cản đường cản lối, chúng ta có thể thoải mái thực hiện các kế hoạch tối ưu hóa lợi nhuận siêu khổng lồ.\"</p>
<p>Bernard đập mạnh bàn tay thô kệch xuống bàn, chỉ vào khu vực Bãi Sao: \"Chính xác! Khu vực rừng phòng hộ 20 hecta giáp ranh phía sau resort phải được san lấp phẳng lỳ ngay lập tức trong tuần tới.\"</p>
<p>\"Chúng ta sẽ xây dựng một tổ hợp casino ba tầng lộng lẫy, phục vụ riêng cho các VIP quốc tế bay chuyên cơ thẳng đến Phú Quốc.\"</p>
<p>\"Dưới danh nghĩa câu lạc bộ trò chơi có thưởng dành cho người nước ngoài, chúng ta sẽ thu về hàng triệu đô la mỗi đêm mà không phải chịu thuế suất tiêu thụ đặc biệt cực cao của dịch vụ sòng bạc thông thường.\"</p>
<p>Lê Văn Hùng khẽ rùng mình trước sự táo bạo điên cuồng của Bernard, nhưng lòng tham vô đáy đã nhanh chóng lấn át mọi nỗi sợ hãi pháp luật còn sót lại.</p>
<p>\"Nhưng thưa ông Bernard, khu rừng đó thuộc diện bảo tồn nghiêm ngặt của Sở Nông nghiệp và Phát triển Nông thôn tỉnh Kiên Giang. Nếu chúng ta tự ý san lấp không có giấy phép chính thức từ UBND tỉnh...\" Hùng ngập ngừng.</p>
<p>Bernard cười khẩy đầy ngạo mạn, ánh mắt gã đầy sự khinh thị đối với hệ thống pháp luật địa phương: \"Cậu vẫn còn mang nặng tư duy của một kẻ làm thuê nhút nhát sao, Hùng?\"</p>
<p>\"Tôi đã chi ra một khoản tiền hối lộ khổng lồ cho một số cán bộ cấp dưới của Sở Du lịch và Ban Quản lý Khu kinh tế Phú Quốc.\"</p>
<p>\"Họ sẽ làm ngơ cho chúng ta xây dựng xong trước, sau đó hợp thức hóa bằng biên bản xử phạt hành chính nhẹ nhàng và điều chỉnh quy hoạch bổ sung sau.\"</p>
<p>\"Mọi việc đã được tôi thu xếp ổn thỏa từ trên xuống dưới. Ngày mai, khi lễ khai trương hoành tráng diễn ra, các vị khách VIP sẽ bắt đầu đặt cược đầu tiên tại khu vực thử nghiệm phía sau.\"</p>
<p>Đúng lúc đó, cửa phòng họp đột ngột bị đẩy mạnh ra, một gã giám sát công trình hớt hải chạy vào, mặt cắt không còn giọt máu, mồ hôi đầm đìa.</p>
<p>\"Ông Dupont, Tổng Giám đốc Hùng! Có biến lớn rồi!\" Gã lắp bắp, thở không ra hơi.</p>
<p>\"Chuyện gì mà mất lịch sự thế hả? Cậu không biết gõ cửa phòng họp của hội đồng quản trị sao?\" Hùng lập tức lên giọng quát tháo để thể hiện uy quyền tối cao của mình trước mặt Bernard.</p>
<p>\"Dạ... dạ... có một đoàn kiểm tra liên ngành đột xuất của Sở Tài nguyên và Môi trường phối hợp với Sở Nông nghiệp tỉnh và lực lượng kiểm lâm đang đứng ở ngoài cổng chính.\"</p>
<p>\"Họ yêu cầu chúng ta xuất trình bản gốc giấy phép đánh giá tác động môi trường (DTM) và tạm dừng mọi hoạt động san lấp tại khu vực giáp ranh rừng phòng hộ ngay lập tức.\"</p>
<p>Sắc mặt của Bernard và Lê Văn Hùng lập tức thay đổi từ hồng hào sang xám ngoét.</p>
<p>\"Đoàn kiểm tra liên ngành? Tại sao tôi không nhận được bất kỳ thông báo mật trước nào từ người của chúng ta ở huyện Phú Quốc?\" Bernard đập mạnh tay xuống bàn đứng phắt dậy, đôi mắt trợn trừng giận dữ.</p>
<p>Hùng toát mồ hôi hột dọc sống lưng, gã lập tức nghĩ ngay đến Trịnh Gia Bảo: \"Không lẽ... gã kiến trúc sư Bảo đã đi tố cáo chúng ta?\"</p>
<p>\"Không thể nào! Tên kiến trúc sư rách nát đó làm gì có cửa tiếp cận được ban giám đốc Sở cấp tỉnh nhanh như vậy!\" Bernard gầm lên đầy giận dữ.</p>
<p>Gã quay sang nhìn Hùng với ánh mắt đầy đe dọa tột cùng: \"Hùng, cậu ra ngoài đó giải quyết ngay lập tức. Dùng mọi cách trì hoãn họ, không được để họ tiếp cận khu vực phía sau.\"</p>
<p>\"Nếu cậu không giữ được cái ghế này, thì căn biệt thự đắt đỏ ở Singapore và tài khoản triệu đô cũng sẽ bay mất theo gió đấy!\"</p>
<p>Lê Văn Hùng nuốt nước bọt cái ực, trán lấm tấm mồ hôi lạnh, gã vội vàng gật đầu rồi ba chân bốn cẳng chạy ra phía cổng resort để đối phó với đoàn thanh tra liên ngành.</p>
<p>Gã không hề biết rằng, đằng sau đoàn kiểm tra đột xuất này là một bàn tay đạo diễn vô cùng tinh vi của Nguyễn Phương Thảo, và một kế hoạch bẫy lòng tham cực kỳ hoàn hảo đã chính thức bắt đầu vận hành để đẩy bọn chúng vào vực thẳm.</p>"""

# Chapter 4
ch4 = """<p>Đêm Phú Quốc yên bình lạ thường tại một quán cà phê nhỏ ẩn mình dưới những rặng phi lao rì rào bên bờ biển An Thới hoang sơ.</p>
<p>Nơi đây cách biệt hoàn toàn với sự ồn ào, náo nhiệt của những dự án bất động sản đang ngày đêm san nền, xẻ núi bạt rừng ngoài kia.</p>
<p>Nguyễn Phương Thảo ngồi lặng lẽ ở góc khuất nhất của quán, trước mặt cô là tách trà sen ấm nóng đang tỏa làn khói mỏng nhẹ dịu mát.</p>
<p>Trịnh Gia Bảo bước vào quán rất nhanh, đội chiếc mũ lưỡi trai sụp xuống trán để tránh tai mắt, áo khoác đen giản dị nhưng phong thái đã lấy lại sự tự tin sắc bén vốn có của một thiên tài.</p>
<p>\"Chị Thảo, đây là toàn bộ tài liệu mật mà chị cần để đối phó với tập đoàn Dupont,\" Gia Bảo ngồi xuống ghế đối diện, đặt lên bàn gỗ một chiếc thẻ nhớ nhỏ màu đỏ.</p>
<p>\"Trong này chứa toàn bộ bản vẽ thiết kế kỹ thuật gốc của tôi, bao gồm cả tọa độ GPS chính xác đến từng centimet của các mốc ranh giới đất dự án Băng Dương Resort.\"</p>
<p>\"Tôi cũng đã tổng hợp đầy đủ hồ sơ phân tích địa chất chi tiết và các báo cáo đánh giá tác động môi trường do các chuyên gia độc lập của Viện Sinh thái thực hiện trước khi tôi bị hất cẳng.\"</p>
<p>Phương Thảo khẽ gật đầu hài lòng, cô cất chiếc thẻ nhớ vào túi xách cá nhân một cách cẩn thận rồi đẩy về phía anh một xấp hồ sơ pháp lý đóng dấu mật của UBND tỉnh.</p>
<p>\"Đoàn kiểm tra đột xuất của chúng tôi hôm nay đã thu thập được rất nhiều bằng chứng sai phạm đắt giá tại thực địa Băng Dương,\" cô nói, giọng điệu vô cùng sắc sảo và điềm tĩnh.</p>
<p>\"Đúng như anh Bảo dự đoán, Lê Văn Hùng đã dùng một bản quy hoạch giả mạo có con dấu sao y bản chính của một văn phòng công chứng quận 5, TP.HCM để lấp liếm các sai phạm.\"</p>
<p>\"Họ đã ngang nhiên san lấp trái phép hơn ba hecta rừng phòng hộ thuộc tiểu khu 97 để làm bãi đỗ xe và đổ móng cho khu nhà câu lạc bộ VIP trò chơi giải trí.\"</p>
<p>\"Đây là sai phạm cực kỳ nghiêm trọng về luật đất đai và lâm nghiệp, đủ điều kiện pháp lý để thu hồi giấy phép xây dựng và khởi tố hình sự tội hủy hoại rừng phòng hộ theo Bộ luật Hình sự Việt Nam hiện hành.\"</p>
<p>Gia Bảo nhấp một ngụm trà ấm, ánh mắt anh lóe lên tia sáng lạnh lùng như dao cạo: \"Bernard Dupont là một con cáo già đầy mưu mô, hắn chắc chắn sẽ đổ hết mọi tội lỗi pháp lý lên đầu Lê Văn Hùng.\"</p>
<p>\"Trong các văn bản chuyển nhượng quyền sở hữu giả mạo mà họ thực hiện, Hùng đứng tên làm người đại diện pháp luật của pháp nhân dự án tại Việt Nam.\"</p>
<p>\"Bernard chỉ đứng sau dưới danh nghĩa chủ tịch quỹ đầu tư viễn dương cung cấp vốn đầu tư quốc tế. Hắn có thể dễ dàng rút lui an toàn về nước nếu có biến cố xảy ra.\"</p>
<p>Phương Thảo mỉm cười đầy ẩn ý, một nụ cười đầy mưu trí và khí chất quyết đoán của một nhà chính trị chính trực và sắc bén.</p>
<p>\"Tôi đã tính trước điều đó. Đó là lý do chúng ta chưa vội động binh đến Bernard ngay lúc này để tránh đánh rắn động cỏ. Chúng ta cần để hắn tự tin lún sâu hơn nữa.\"</p>
<p>\"Khi lễ khai trương chính thức diễn ra và sòng bạc thử nghiệm trá hình đi vào hoạt động tiếp khách, chúng ta sẽ bắt quả tang toàn bộ dòng tiền bất hợp pháp chảy qua các tài khoản ma.\"</p>
<p>\"Lúc đó, C03 Bộ Công an phối hợp với Cục Phòng chống rửa tiền của Ngân hàng Nhà nước sẽ phong tỏa toàn diện tài sản của tập đoàn Dupont tại Việt Nam.\"</p>
<p>Gia Bảo nhìn người phụ nữ trẻ tuổi trước mặt, thầm cảm phục sự quyết đoán, tầm nhìn xa trông rộng và mưu lược xuất chúng của cô.</p>
<p>\"Vậy còn dự án sinh thái mới của tôi? Hòn Dăm Ngoài có tiến triển pháp lý gì mới không thưa chị?\" Gia Bảo hỏi, giọng nói mang theo sự háo hức cháy bỏng của một kiến trúc sư khát khao cống hiến.</p>
<p>Phương Thảo lật trang tài liệu tiếp theo, đẩy về phía anh bản đồ quy hoạch sử dụng đất của quần đảo An Thới phía Nam.</p>
<p>\"Tuần tới, UBND tỉnh Kiên Giang sẽ tổ chức phiên đấu giá công khai quyền sử dụng đất và mặt nước biển dài hạn của Hòn Dăm Ngoài để phát triển mô hình du lịch sinh thái kiểu mẫu xanh.\"</p>
<p>\"Dự án này đòi hỏi nhà đầu tư phải có cam kết ký quỹ bảo vệ môi trường lên tới một trăm tỷ đồng và chứng minh được công nghệ xây dựng nổi hoàn toàn không xâm lấn lòng biển.\"</p>
<p>\"Hội đồng thẩm định do tôi làm chủ tịch sẽ đánh giá cao những thiết kế bền vững thực sự. Anh Bảo, anh có tự tin lấy lại danh dự và những gì đã mất không?\"</p>
<p>Gia Bảo siết chặt nắm tay đến mức các khớp xương kêu răng rắc, ngực phập phồng đầy kiêu hãnh: \"Tôi đã chuẩn bị cho ngày này từ năm năm trước bằng cả máu và nước mắt.\"</p>
<p>\"Hòn Dăm Ngoài sẽ không chỉ là một khu nghỉ dưỡng thông thường. Nó sẽ là một kiệt tác kiến trúc xanh nổi trên biển hoàn hảo nhất thế giới, một thiên đường sinh thái thực sự mà không một sòng bạc dơ bẩn nào có thể sánh kịp.\"</p>
<p>\"Tôi sẽ dùng chính dự án vĩ đại này để vả thẳng vào mặt Bernard và Lê Văn Hùng, cho chúng thấy thế nào là giá trị thực sự của kiến trúc sinh thái chân chính.\"</p>
<p>\"Tốt lắm,\" Phương Thảo đứng dậy, đưa tay ra bắt chặt lấy bàn tay thô ráp của Gia Bảo.</p>
<p>\"Hãy chuẩn bị hồ sơ đấu thầu thật xuất sắc. Tôi tin tưởng tuyệt đối vào tài năng của anh. Phú Quốc cần những người có tâm và có tầm như anh để giữ gìn màu xanh nguyên bản của đảo ngọc.\"</p>
<p>Dưới ánh đèn vàng ấm áp của quán nhỏ bên bờ biển, liên minh thép giữa chàng kiến trúc sư thiên tài bị phản bội và nữ Phó Chủ tịch tỉnh chính trực đã chính thức được thiết lập vững chắc, chuẩn bị thổi bùng một cơn bão quét sạch những vết nhơ tham nhũng tại Phú Quốc.</p>"""

# Chapter 5
ch5 = """<p>Một tuần sau, tại trung tâm hội nghị tỉnh Kiên Giang diễn ra buổi đấu giá quyền sử dụng đất quần đảo An Thới vô cùng trang trọng.</p>
<p>Đây là sự kiện thu hút rất nhiều sự quan tâm của giới tài phiệt và các tập đoàn bất động sản lớn, tuy nhiên hầu hết các ông lớn đều ngần ngại vì những điều khoản bảo vệ môi trường cực kỳ ngặt nghèo do UBND tỉnh áp dụng.</p>
<p>Lê Văn Hùng cũng có mặt tại buổi đấu giá với tư cách đại diện cho Băng Dương Resort, gã muốn mua thêm Hòn Dăm Ngoài để mở rộng chuỗi biệt thự VIP ăn chơi cờ bạc của Bernard.</p>
<p>Hùng bước vào sảnh lớn với bộ dạng vô cùng hợm hĩnh, mặc vest bóng lộn, xung quanh gã là một nhóm trợ lý và các vệ sĩ cao lớn cẩn mật che chắn bảo vệ.</p>
<p>Đột nhiên, gã khựng lại khi nhìn thấy Trịnh Gia Bảo bước vào sảnh, đi bên cạnh anh là một nhóm chuyên gia luật kinh tế hàng đầu và đại diện cấp cao của ngân hàng Vietcombank chi nhánh Phú Quốc.</p>
<p>Gia Bảo hôm nay mặc một bộ vest xám lịch lãm thiết kế riêng, phong thái vô cùng đĩnh đạc, sang trọng, hoàn toàn không còn chút dấu vết nhếch nhác của kẻ bị đuổi khỏi resort trong đêm mưa gió bão bùng năm xưa.</p>
<p>Hùng khinh khỉnh bước tới, chặn đường Gia Bảo ngay trước sảnh chính, cất giọng mỉa mai đầy đắc ý: \"Ồ, ai đây thế này? Chẳng phải là kiến trúc sư Trịnh Gia Bảo vĩ đại bị đuổi như chó của chúng ta sao?\"</p>
<p>\"Anh đi lạc chỗ rồi à? Đây là buổi đấu giá nghìn tỷ của các ông chủ lớn và các quỹ đầu tư quốc tế, không phải là nơi dành cho một kẻ thất nghiệp chạy ăn từng bữa như anh đâu.\"</p>
<p>Gia Bảo đứng lại, thản nhiên nhìn gã trợ lý phản bội cũ bằng ánh mắt lạnh lùng, sắc bén như nhìn một con sâu kiến nhỏ nhoi.</p>
<p>\"Hùng, cậu vẫn thích nói nhiều và ảo tưởng sức mạnh như trước,\" Gia Bảo khẽ cười nửa miệng, giọng nói vô cùng trầm ổn và uy lực.</p>
<p>\"Tôi đến đây để lấy lại những gì thuộc về mình, và xây dựng một thứ mà những kẻ bán rẻ lương tâm như cậu cả đời này cũng không bao giờ có tư cách hiểu được.\"</p>
<p>Hùng cười lớn đầy đắc ý, vẻ mặt gã vênh váo: \"Lấy lại? Bằng cái gì đây? Bằng mấy bản vẽ tay mơ mộng hão huyền của anh à?\"</p>
<p>\"Tôi nói cho anh biết, tập đoàn Dupont đã chuẩn bị sẵn ba trăm tỷ đồng tiền mặt để thâu tóm Hòn Dăm Ngoài bằng mọi giá. Anh lấy cái gì để đấu với chúng tôi đây?\"</p>
<p>Gia Bảo không thèm trả lời thêm một lời nào, anh chỉ khẽ gật đầu chào lịch sự rồi lướt qua Hùng, bước thẳng vào phòng đấu giá chính.</p>
<p>Buổi đấu giá diễn ra vô cùng gay cấn và nghẹt thở dưới sự điều hành trực tiếp của Hội đồng Thẩm định tỉnh Kiên Giang.</p>
<p>Khi quyền sử dụng Hòn Dăm Ngoài được đưa ra đấu giá với mức khởi điểm là một trăm năm mươi tỷ đồng, Lê Văn Hùng lập tức tự tin giơ bảng ra giá đầu tiên.</p>
<p>\"Một trăm tám mươi tỷ!\" Hùng dõng dạc hô to trước toàn thể hội trường, vẻ mặt đầy kiêu ngạo tột cùng.</p>
<p>Cả phòng họp khẽ xôn xao, nhiều doanh nghiệp vừa và nhỏ khẽ lắc đầu ngao ngán bỏ cuộc trước tiềm lực của Băng Dương.</p>
<p>\"Một trăm chín mươi tỷ,\" Gia Bảo bình thản giơ bảng ra giá ngay lập tức.</p>
<p>Hùng nhướng mày nhìn Gia Bảo, khinh bỉ cười khẩy đầy thách thức: \"Hai hai mươi tỷ!\"</p>
<p>\"Hai trăm ba mươi tỷ,\" Gia Bảo lập tức theo sát không một giây chần chừ.</p>
<p>Nhịp độ tăng giá nhanh chóng được đẩy lên cao trào, Hùng bắt đầu cảm thấy căng thẳng, mồ hôi hột bắt đầu rịn ra trên trán khi mức giá đã dần vượt qua ngân sách dự kiến ban đầu của Bernard.</p>
<p>\"Hai trăm tám mươi tỷ!\" Hùng nghiến răng hô lớn, đôi mắt đỏ ngầu nhìn Gia Bảo đầy đe dọa.</p>
<p>Gia Bảo khẽ nhấp một ngụm nước lọc, khuôn mặt không hề biến sắc hay lo lắng, anh giơ bảng một cách vô cùng dứt khoát: \"Ba trăm tỷ.\"</p>
<p>Hùng đứng bật dậy khỏi ghế, chỉ tay thẳng về phía Gia Bảo hét lớn: \"Tôi yêu cầu ban tổ chức kiểm tra năng lực tài chính của Trịnh Gia Bảo ngay lập tức!\"</p>
<p>\"Anh ta chỉ là một cá nhân, một kiến trúc sư bị sa thải, làm sao có đủ ba trăm tỷ để ký quỹ và thanh toán tiền đấu giá đất hợp pháp?\"</p>
<p>Đúng lúc này, đại diện Vietcombank chi nhánh Phú Quốc bước lên phía trước chủ tọa, đặt lên bàn một văn bản bảo lãnh thanh toán vô điều kiện đóng dấu đỏ chói.</p>
<p>\"Chúng tôi, ngân hàng Vietcombank, cam kết bảo lãnh tài chính vô điều kiện cho dự án sinh thái của ông Trịnh Gia Bảo với hạn mức tín dụng lên tới năm trăm tỷ đồng,\" vị đại diện dõng dạc tuyên bố trước toàn hội trường.</p>
<p>Cả phòng đấu giá ồ lên kinh ngạc tột độ. Lê Văn Hùng đờ đẫn cả người như bị rút sạch dưỡng khí, gã không thể tin nổi một kẻ trắng tay lại có thể nhận được sự bảo lãnh khổng lồ từ một ngân hàng lớn nhất Việt Nam như vậy.</p>
<p>Gã đâu biết rằng, chính Phương Thảo đã thẩm định dự án \"Kỳ Quan Xanh\" của Bảo là dự án xanh trọng điểm, giúp anh kết nối với các quỹ phát triển bền vững của Nhật Bản và Thụy Sĩ.</p>
<p>\"Ba trăm tỷ lần thứ nhất... lần thứ hai... lần thứ ba! Quyết định trúng đấu giá Hòn Dăm Ngoài thuộc về ông Trịnh Gia Bảo!\"</p>
<p>Tiếng búa đập xuống bàn vang lên đanh thép như một cái tát trời giáng làm chấn động toàn bộ tinh thần của Lê Văn Hùng.</p>
<p>Gia Bảo đứng dậy, chỉnh lại nếp áo vest phẳng phiu, nhìn thẳng vào gương mặt tái mét cắt không còn giọt máu của Hùng.</p>
<p>\"Hùng, về nói với Bernard, hòn đảo này giờ là lãnh địa của tôi. Và trò chơi của chúng ta... bây giờ mới thực sự bắt đầu,\" Gia Bảo nói nhỏ đủ để Hùng nghe thấy rồi quay lưng bước đi trong tiếng vỗ tay rộn rã kéo dài của cả hội trường.</p>"""

# Chapter 6
ch6 = """<p>Sau chiến thắng vang dội tại buổi đấu giá cấp tỉnh, dự án \"Kỳ Quan Xanh\" trên Hòn Dăm Ngoài của Trịnh Gia Bảo lập tức được khởi công với tốc độ chóng mặt.</p>
<p>Hàng chục chiếc sà lan chở vật liệu tre tầm vông, gỗ tái chế cao cấp và hệ thống móng nổi sinh học thân thiện với môi trường liên tục cập bến hòn đảo hoang sơ phía Nam An Thới.</p>
<p>Gia Bảo túc trực tại công trường ngày đêm, trực tiếp giám sát từng chi tiết nhỏ cùng với các kỹ sư công nghệ môi trường hàng đầu Việt Nam và Nhật Bản.</p>
<p>Sự hồi sinh mạnh mẽ và ngoạn mục của Gia Bảo khiến Bernard Dupont vô cùng điên tiết, gã cảm nhận được mối đe dọa trực tiếp đến sự sống còn của dự án Băng Dương.</p>
<p>\"Hùng! Tại sao gã Bảo lại có thể huy động được nguồn vốn và thế lực lớn như vậy?\" Bernard gầm lên như một con thú bị thương trong phòng làm việc VIP tại Băng Dương Resort.</p>
<p>\"Tôi đã bảo cậu phải triệt hạ hoàn toàn uy tín và danh dự của hắn tại Phú Quốc cơ mà! Cậu làm việc kiểu gì thế?\"</p>
<p>Lê Văn Hùng run rẩy cúi đầu sát đất: \"Thưa ông Bernard, tôi... tôi đã thuê các công ty truyền thông bẩn bôi nhọ dự án Kỳ Quan Xanh của hắn trên khắp các trang mạng xã hội lớn.\"</p>
<p>\"Chúng ta đã tung tin rằng công nghệ móng nổi của hắn chưa được kiểm định, sẽ phá hủy rạn san hô quý hiếm của vùng biển An Thới và lừa đảo nhà đầu tư.\"</p>
<p>\"Nhưng không hiểu sao, các cơ quan báo chí chính thống của tỉnh và trung ương đều đồng loạt đăng bài bảo vệ hắn, khen ngợi đây là mô hình kiểu mẫu bảo tồn sinh thái bền vững.\"</p>
<p>Bernard đập mạnh tay xuống bàn làm việc, đôi mắt xanh đục lóe lên tia nhìn độc ác, xảo quyệt: \"Chắc chắn có thế lực rất lớn trong chính quyền tỉnh đang bảo kê nâng đỡ cho hắn.\"</p>
<p>\"Chúng ta không thể ngồi chờ chết được nữa. Lễ khai trương Băng Dương chỉ còn ba ngày nữa là diễn ra.\"</p>
<p>\"Hùng, cậu dẫn người sang Hòn Dăm Ngoài ngay lập tức. Thuê vài nhóm giang hồ giả danh ngư dân địa phương sang đó quấy phá, đập phá công trường của hắn.\"</p>
<p>\"Cứ bảo là công trình của hắn làm cản therapeutic đường đánh bắt cá và phá hoại ngư trường gia truyền lâu đời của họ. Phải bắt hắn dừng thi công bằng mọi giá!\"</p>
<p>Hùng lập tức sáng mắt ra, gã nhận ra đây là cơ hội cuối cùng để gã lập công chuộc tội trước ông chủ ngoại quốc: \"Ý kiến tuyệt vời, thưa ông chủ! Tôi sẽ thu xếp giang hồ bến tàu làm ngay lập tức!\"</p>
<p>Sáng hôm sau, khi công trường trên Hòn Dăm Ngoài đang nhộn nhịp thi công đổ móng nổi sinh học, bất ngờ có năm chiếc tàu gỗ chở theo hơn ba mươi gã đàn ông bặm trợn, tay cầm gậy gộc, dao búa hung hãn ập vào bãi san hô nông.</p>
<p>Chúng hò hét vang trời, ném đá xối xả vào các sà lan vật liệu và đe dọa hành hung các công nhân đang thi công trên mặt nước.</p>
<p>\"Dừng ngay công trình lại! Các người xây dựng trái phép phá hoại ngư trường kiếm ăn của chúng tôi! Biến khỏi đảo hoang này ngay lập tức nếu không muốn mất mạng!\" Một gã dẫn đầu xăm trổ đầy mình, mặt sẹo lớn tiếng thách thức.</p>
<p>Các công nhân hoảng sợ lùi lại phía sau cầu phao. Đúng lúc này, Trịnh Gia Bảo bình thản bước ra từ văn phòng công trường lâm thời bằng tre.</p>
<p>Anh nhìn nhóm người hung hãn bằng ánh mắt vô cùng điềm tĩnh, không một chút sợ hãi, trên tay là chiếc điện thoại đang ở chế độ ghi hình trực tiếp truyền thẳng lên máy chủ của tỉnh.</p>
<p>\"Các anh bảo công trình này phá hoại ngư trường gia truyền của các anh sao?\" Gia Bảo cất giọng rõ ràng, mạch lạc và uy nghiêm.</p>
<p>\"Hòn Dăm Ngoài đã được UBND tỉnh cấp phép quy hoạch mặt nước rõ ràng, ranh giới dự án nằm hoàn toàn ngoài luồng lạch giao thông đường thủy của ngư dân.\"</p>
<p>\"Hơn nữa, các anh không phải là ngư dân An Thới. Tôi đã sống ở vùng biển này năm năm, tôi biết mặt từng người dân chài ở đây. Các anh là giang hồ bến tàu Rạch Giá được thuê đến phá hoại đúng không?\"</p>
<p>Gã xăm trổ dẫn đầu giận dữ, lao tới định giật lấy điện thoại của Gia Bảo để đập phá: \"Mày câm mồm! Tao bảo phá là phá! Anh em xông lên đập nát cái đống tre gỗ kia cho tao!\"</p>
<p>\"Ai dám động vào tài sản nhà nước và công trình trọng điểm cấp tỉnh của chúng tôi?\"</p>
<p>Một giọng nói uy nghiêm đầy quyền lực vang lên từ phía cầu cảng tạm của hòn đảo.</p>
<p>Mọi người quay lại và sững sờ khi thấy hai chiếc tàu tuần tra tốc độ cao của lực lượng Biên phòng Phú Quốc và Cảnh sát đường thủy rẽ sóng lao tới với tốc độ cực nhanh.</p>
<p>Nguyễn Phương Thảo bước xuống từ tàu tuần tra, đi bên cạnh cô là Thượng tá Lê Minh Cường, Chỉ huy trưởng đồn Biên phòng An Thới cùng hàng chục chiến sĩ vũ trang đầy đủ đang lăm lăm súng trên tay.</p>
<p>Nhóm côn đồ lập tức tái mét mặt mày, vứt hết gậy gộc xuống biển định nhảy xuống tàu gỗ bỏ trốn nhưng đã bị các chiến sĩ biên phòng nhanh chóng áp sát, nổ súng cảnh chỉ và khống chế toàn bộ chỉ trong ba phút.</p>
<p>Lê Văn Hùng lúc này đang ngồi trên một chiếc tàu gỗ ẩn nấp phía xa quan sát tình hình, chứng kiến cảnh tượng kinh hoàng đó liền toát mồ hôi hột, vội vã ra lệnh cho tài xế quay đầu tàu chạy trốn trối chết về đất liền.</p>
<p>Phương Thảo bước đến bên Gia Bảo, mỉm cười khích lệ đầy ấm áp: \"Anh Bảo, anh và các công nhân không sao chứ?\"</p>
<p>\"Tôi không sao, cảm ơn chị Thảo và các chiến sĩ đã đến kịp thời cứu nguy,\" Gia Bảo tắt điện thoại, thở phào nhẹ nhõm.</p>
<p>\"Toàn bộ hình ảnh ghi lại hôm nay và lời khai của nhóm côn đồ này sẽ là đòn chí mạng tiếp theo giáng vào Lê Văn Hùng và Bernard,\" Phương Thảo nhìn về phía chiếc tàu gỗ đang tháo chạy ngoài xa bằng ánh mắt sắc lạnh.</p>
<p>\"Cơn bão pháp lý đã nổi lên rồi, anh Bảo. Bọn họ sẽ không thể trốn chạy khỏi lưới trời lồng lộng được nữa đâu.\"</p>
<p>Gia Bảo nhìn ra khơi xa, sóng biển Tây đang cuồn cuộn nổi sóng như báo hiệu cho ngày tàn của những kẻ phản bội tham tàn sắp sửa bắt đầu một cách vô cùng tàn khốc.</p>"""

# Chapter 7
ch7 = """<p>Đúng ngày khai trương hoành tráng của Băng Dương Resort, bầu trời Bãi Sao trong xanh không một gợn mây, nắng vàng trải dài rực rỡ.</p>
<p>Hàng chục chiếc xe siêu sang Rolls-Royce, Bentley nối đuôi nhau tiến vào cổng chào bằng tre khổng lồ lung linh, đưa các khách VIP quốc tế và giới thượng lưu đến tham dự buổi tiệc.</p>
<p>Khuôn viên của khu resort 5 sao rực rỡ dưới hàng ngàn bóng đèn chùm pha lê nhập khẩu, hoa tươi nhập khẩu từ Hà Lan trang trí khắp các lối đi, tạo nên một bầu không khí xa hoa xa xỉ tột cùng.</p>
<p>Các quý bà trong những chiếc đầm dạ hội lộng lẫy và các quý ông lịch lãm nâng ly chúc mừng cho sự xuất hiện của một thiên đường giải trí mới tại đảo ngọc Phú Quốc.</p>
<p>Bernard Dupont và Lê Văn Hùng đứng ở trung tâm sảnh lớn đón khách sang trọng, nụ cười vô cùng rạng rỡ và tràn đầy sự tự mãn cực hạn.</p>
<p>Hùng khẽ nâng ly rượu sâm banh đắt đỏ hướng về phía Bernard: \"Thưa ông Bernard, mọi việc đã hoàn toàn hoàn hảo ngoài mong đợi. Khu casino thử nghiệm trá hình phía sau đã chật kín các khách VIP đặt cược.\"</p>
<p>\"Hôm nay chúng ta sẽ thu về không dưới năm triệu đô la chỉ từ tiền cược ban đầu của các đại gia.\"</p>
<p>Bernard cười đắc ý, ánh mắt hiện rõ sự tham lam vô độ: \"Cậu làm việc tốt lắm, Hùng. Cậu đã chứng minh được giá trị thực tế của mình hơn gã kiến trúc sư gàn dở Trịnh Gia Bảo kia gấp trăm lần.\"</p>
<p>Đột nhiên, tiếng còi hú vang dội từ phía cổng chính của resort làm gián đoạn tiếng nhạc cổ điển êm dịu đang phát trong sảnh.</p>
<p>Ba chiếc xe chuyên dụng màu xanh của lực lượng Cảnh sát Kinh tế và xe biển xanh của Sở Du lịch, Sở Tài nguyên và Môi trường tỉnh Kiên Giang bất ngờ ập vào khuôn viên resort.</p>
<p>Hàng chục chiến sĩ cảnh sát cơ động phối hợp cùng cán bộ thanh tra nhanh chóng phong tỏa toàn bộ các lối ra vào của Băng Dương Resort.</p>
<p>Đứng đầu đoàn thanh tra liên ngành chính là Nguyễn Phương Thảo, Phó Chủ tịch tỉnh, bên cạnh cô là Thượng tá Nguyễn Văn Nam, Trưởng phòng Cảnh sát Điều tra tội phạm về tham nhũng, kinh tế, buôn lậu (C03) tỉnh Kiên Giang.</p>
<p>Khách khứa trong sảnh bắt đầu xôn xao, náo loạn cực độ. Lê Văn Hùng giật mình hoảng hốt, chiếc ly pha lê trên tay rơi xuống sàn đá cẩm thạch vỡ tan tành thành trăm mảnh.</p>
<p>Hùng vội vàng chạy tới chặn đường đoàn thanh tra, cố nở nụ cười gượng gạo trên gương mặt đang tái mét đi vì sợ hãi.</p>
<p>\"Chào chị Thảo, chào Thượng tá Nam! Hôm nay là ngày khai trương trọng đại của chúng tôi, không biết có chuyện gì mà các anh chị lại đến bất ngờ thế này?\" Hùng hỏi, giọng nói run rẩy thấy rõ.</p>
<p>Phương Thảo nhìn Hùng bằng ánh mắt lạnh lùng như băng giá, cô không thèm bắt tay gã mà trực tiếp công bố quyết định thanh tra khẩn cấp trước toàn thể quan khách.</p>
<p>\"Theo chỉ đạo trực tiếp của Chủ tịch UBND tỉnh Kiên Giang và Bộ Công an, chúng tôi tiến hành thanh tra đột xuất toàn diện dự án Băng Dương Resort ngay lập tức,\" Phương Thảo dõng dạc tuyên bố, giọng nói đầy uy lực của cô vang vọng khắp sảnh lớn.</p>
<p>\"Nội dung thanh tra bao gồm việc chấp hành các quy định pháp luật về đất đai theo Luật Đất đai năm 2013, bảo vệ rừng phòng hộ Phú Quốc theo Luật Lâm nghiệp năm 2017, đánh giá tác động môi trường và tính pháp lý của hồ sơ chuyển nhượng quyền sở hữu dự án.\"</p>
<p>Bernard Dupont bước tới với khuôn mặt vô cùng dữ tợn, gã lớn tiếng bằng thứ tiếng Anh giận dữ đầy ngạo mạn: \"Các người không có quyền làm thế này! Chúng tôi là nhà đầu tư nước ngoài được bảo hộ bởi luật đầu tư quốc tế!\"</p>
<p>Thượng tá Nam bước lên phía trước một bước, chìa ra lệnh khám xét khẩn cấp và lệnh phong tỏa tài sản do Viện Kiểm sát Nhân dân tỉnh phê duyệt chính thức.</p>
<p>\"Ông Dupont, chúng tôi có đầy đủ chứng cứ pháp lý và kết quả giám định của Viện Khoa học Hình sự thuộc Bộ Công an về việc tập đoàn của ông giả mạo giấy tờ của cơ quan nhà nước và chữ ký của công chứng viên để chiếm đoạt tài sản của ông Trịnh Gia Bảo,\" Thượng tá Nam dứt khoát tuyên bố.</p>
<p>\"Đồng thời, lực lượng chức năng đang tiến hành bắt quả tang hoạt động tổ chức đánh bạc và đánh bạc bất hợp pháp quy mô lớn tại khu nhà câu lạc bộ VIP phía sau resort, vi phạm nghiêm trọng Điều 321 và Điều 322 Bộ luật Hình sự Việt Nam.\"</p>
<p>Như để minh chứng cho lời nói của Thượng tá Nam, từ phía sau resort, hàng chục chiến sĩ cảnh sát cơ động đang áp giải hơn năm mươi con bạc VIP cùng toàn bộ máy móc, phỉnh phạt cờ bạc và hàng triệu đô la tiền mặt ra ngoài sảnh chính.</p>
<p>Lê Văn Hùng đổ sụp hoàn toàn xuống sàn nhà, mồ hôi lạnh ướt đẫm cả lưng áo vest đắt tiền trị giá hàng ngàn đô.</p>
<p>Gã trợ lý phản bội cũ run rẩy như cầy sấy khi nhận ra chữ ký của chính mình nằm ở tất cả các biên bản phê duyệt lấn chiếm rừng phòng hộ và xây dựng trái phép sòng bạc.</p>
<p>Gã trợn tròn mắt nhìn các cán bộ kỹ thuật hình sự đang tiến hành niêm phong toàn bộ sổ sách kế toán, máy tính dữ liệu tại quầy lễ tân để phục vụ công tác điều tra.</p>
<p>Bernard Dupont đứng chôn chân tại chỗ như một bức tượng đá, gương mặt gã xám xịt như tro tàn khi nhận ra toàn bộ kế hoạch lừa đảo tinh vi của mình đã bị bóc trần hoàn toàn chỉ trong một tích tắc ngắn ngủi.</p>
<p>Sự sụp đổ của Băng Dương Resort dưới sự điều hành của hai kẻ tham lam đã chính thức bắt đầu ngay trong ngày khai trương lộng lẫy nhất của nó.</p>"""

# Chapter 8
ch8 = """<p>Sau đêm kinh hoàng tại lễ khai trương, Băng Dương Resort bị cơ quan công an ra quyết định đình chỉ hoạt động hoàn toàn để phục vụ công tác điều tra hình sự.</p>
<p>Lê Văn Hùng ngồi thẫn thờ như một xác không hồn trong văn phòng Tổng Giám đốc sang trọng đã bị niêm phong một nửa bằng băng keo đỏ.</p>
<p>Gã điên cuồng bấm điện thoại gọi cho Bernard Dupont hàng trăm cuộc nhưng đầu dây bên kia chỉ luôn là những tiếng tút dài vô vọng đầy lạnh lùng.</p>
<p>Hùng vội vàng chạy lên căn hộ penthouse xa hoa của Bernard trên tầng cao nhất để tìm kiếm, nhưng căn phòng đã trống trơn không còn một bóng người, mọi tài liệu mật và vali quần áo của gã ngoại quốc đều đã biến mất sạch sẽ từ đêm qua.</p>
<p>Hùng hớt hải chạy xuống hầm gửi xe và phát hiện chiếc xe Mercedes VIP thường ngày gã đi cũng đã bị thu hồi theo lệnh khẩn cấp của quỹ đầu tư viễn dương.</p>
<p>Đúng lúc này, gã nhận được một tin nhắn lạnh lùng từ một số điện thoại lạ gửi đến: \"Hùng, toàn bộ sai phạm lấn chiếm rừng phòng hộ và giả mạo hồ sơ đều do cậu đứng tên ký duyệt trực tiếp với tư cách người đại diện pháp luật của dự án.\"</p>
<p>\"Tôi đã rút toàn bộ số tiền mặt còn lại của dự án sang tài khoản ẩn danh tại Thụy Sĩ và đang trên đường rời khỏi Việt Nam. Hãy ở lại và gánh tội thay tôi đi nhé. Chúc may mắn trong tù.\" Người gửi chính là Bernard Dupont.</p>
<p>Hùng như bị sét đánh ngang tai, gã gào lên điên cuồng như một con thú điên, ném mạnh chiếc điện thoại vào tường vỡ tan tành thành trăm mảnh vụn.</p>
<p>Gã cay đắng nhận ra mình chỉ là một con tốt thí mạng rẻ tiền không hơn không kém trong trò chơi cờ bạc đầy quỷ quyệt của gã ngoại quốc cáo già.</p>
<p>Đối mặt với án tù chung thân vì tội tổ chức đánh bạc trái phép quy mô lớn và tội hủy hoại rừng phòng hộ quốc gia, Hùng hoàn toàn suy sụp tinh thần.</p>
<p>Trong cơn tuyệt vọng tột cùng không còn đường lui, gã nghĩ ngay đến người duy nhất có đủ tài năng và thế lực để cứu mình lúc này - Trịnh Gia Bảo.</p>
<p>Chiều hôm đó, tại văn phòng công trường lộng gió của dự án Kỳ Quan Xanh trên Hòn Dăm Ngoài, Gia Bảo đang xem lại bản vẽ kết cấu mái vòm tre nổi sinh thái.</p>
<p>Tiếng gõ cửa vang lên dồn dập, hoảng loạn, và Lê Văn Hùng bước vào văn phòng, bộ dạng vô cùng nhếch nhác, quần áo xộc xệch bẩn thỉu, râu tóc phờ phạc hốc hác.</p>
<p>Vừa nhìn thấy Gia Bảo đứng đó, Hùng lập tức quỳ sụp xuống sàn gỗ, bò tới ôm chặt lấy chân anh, khóc lóc thảm thiết van xin lòng thương hại.</p>
<p>\"Anh Bảo! Em xin anh! Em là đứa khốn nạn, em bị lòng tham vô đáy che mờ mắt nên mới làm hại anh!\" Hùng tát liên tục vào mặt mình đến mức rớm máu.</p>
<p>\"Xin anh cứu em một mạng! Bernard đã lừa em, hắn ôm hết tiền bỏ trốn và đổ hết mọi tội lỗi pháp lý lên đầu em gánh chịu rồi!\"</p>
<p>\"Anh Bảo ơi, chúng ta từng là anh em ruột thịt, em đã theo anh làm việc vất vả năm năm trời, xin anh nghĩ đến tình xưa nghĩa cũ mà cứu vớt em với!\"</p>
<p>Gia Bảo thản nhiên đứng dậy, gạt chân ra một cách dứt khoát để Hùng ngã nhào xuống sàn nhà lạnh lẽo, ánh mắt anh nhìn gã lạnh lùng như băng giá, không một chút hơi ấm tình người.</p>
<p>\"Tình xưa nghĩa cũ sao? Hùng,\" Gia Bảo chậm rãi nói, từng lời nói đanh thép như nhát dao cứa thẳng vào lòng Hùng.</p>
<p>\"Đêm mưa gió bão bùng ở Bãi Sao, khi cậu sai bảo vệ ném vali của tôi xuống vũng nước bẩn bên lề đường, cậu có nghĩ đến tình nghĩa năm năm đó không?\"</p>
<p>\"Khi cậu cấu kết với Bernard làm giả chữ ký cướp đi đứa con tinh thần xương máu của tôi, cậu có nghĩ đến việc tôi từng coi cậu như em ruột không?\"</p>
<p>Hùng khóc nghẹn ngào trong sự nhục nhã, gã vội vã lôi từ trong chiếc ba lô cũ ra một chiếc ổ cứng di động và một tập hồ sơ kế toán dày cộp ném lên bàn làm việc.</p>
<p>\"Anh Bảo, em có tài liệu mật cực kỳ quan trọng! Đây là toàn bộ hồ sơ giao dịch chuyển tiền trốn thuế, rửa tiền của Bernard qua các công ty bình phong ở đảo Cayman!\"</p>
<p>\"Trong này có cả danh sách những cán bộ biến chất tại Ban Quản lý Khu kinh tế Phú Quốc đã nhận hối lộ của Bernard để làm ngơ cho hoạt động sòng bạc trái phép!\"</p>
<p>\"Em giao hết toàn bộ cho anh! Chỉ xin anh nói với chị Thảo Phó Chủ tịch tỉnh và Thượng tá Nam cho em được hưởng lượng khoan hồng, em không muốn mục xương trong tù đâu!\"</p>
<p>Gia Bảo khẽ liếc nhìn chiếc ổ cứng di động, anh thản nhiên cầm điện thoại lên gọi cho Thượng tá Nam của phòng C03.</p>
<p>\"Thượng tá Nam, Lê Văn Hùng đang ở văn phòng của tôi tại Hòn Dăm Ngoài. Gã muốn đầu thú và giao nộp toàn bộ chứng cứ phạm tội của Bernard Dupont và đường dây nhận hối lộ tại địa phương.\"</p>
<p>Anh cúp máy, nhìn gã trợ lý cũ đang run rẩy co quắp dưới đất bằng ánh mắt khinh bỉ và thương hại tột cùng.</p>
<p>\"Hùng, đầu thú và thành khẩn khai báo là con đường sống duy nhất của cậu lúc này trước pháp luật Việt Nam nghiêm minh.\"</p>
<p>\"Nhưng sự phản bội đê tiện của cậu đối với lòng tin của tôi... tôi sẽ không bao giờ tha thứ. Cậu hãy tự mình gánh chịu hậu quả từ lòng tham vô đáy của mình đi.\"</p>
<p>Mười lăm phút sau, chiếc ca nô tuần tra của lực lượng công an cập bến Hòn Dăm Ngoài, áp giải Lê Văn Hùng đi trong sự lạnh lùng tột cùng của Trịnh Gia Bảo và toàn bộ công nhân công trường.</p>
<p>Kẻ gieo gió cuối cùng đã phải gặt bão, và cái giá phải trả cho sự phản bội đê hèn luôn là sự sụp đổ hoàn toàn trong nhục nhã.</p>"""

# Chapter 9
ch9 = """<p>Ba tháng sau khi vụ án Băng Dương Resort chấn động dư luận Phú Quốc bị triệt phá hoàn toàn, dự án \"Kỳ Quan Xanh\" của Trịnh Gia Bảo trên Hòn Dăm Ngoài đã hoàn thành xuất sắc.</p>
<p>Hòn đảo hoang sơ ngày nào giờ đã thực sự biến thành một thiên đường nghỉ dưỡng sinh thái xa xỉ có một không hai trên thế giới.</p>
<p>Hàng chục căn biệt thự bằng tre tầm vông nổi trên mặt nước biển trong vắt như pha lê, được kết nối với nhau bằng những cây cầu gỗ uốn lượn mềm mại như những dải lụa.</p>
<p>Hệ thống điện năng lượng mặt trời áp mái tự cấp 100% cùng công nghệ tuần hoàn xử lý nước sinh học ba cấp giúp resort hoạt động hoàn hảo mà không thải ra môi trường một giọt nước thải bẩn nào.</p>
<p>Dưới làn nước xanh biếc quanh các biệt thự nổi, rạn san hô tự nhiên được phục hồi sinh trưởng mạnh mẽ, cá biển đủ màu sắc bơi lội tung tăng tạo nên một khung cảnh vô cùng huyền ảo tựa thiên đường.</p>
<p>Hệ thống móng nổi sinh học đặc biệt được chế tạo từ hạt nhựa tái chế ép mật độ cao gia cường sợi thủy tinh, giúp công trình nổi vững chãi trước những cơn sóng dữ mà hoàn toàn không gây ô nhiễm vi nhựa cho nguồn nước biển.</p>
<p>Hôm nay, Kỳ Quan Xanh vinh dự được UBND tỉnh Kiên Giang và Bộ Ngoại giao chọn làm nơi đón tiếp phái đoàn ngoại giao quốc tế gồm Đại sứ các nước châu Âu và Nhật Bản đến tham quan mô hình kinh tế tuần hoàn kiểu mẫu xanh.</p>
<p>Trịnh Gia Bảo đứng ở đầu cầu cảng đón khách, phong thái vô cùng lịch lãm, tự tin và quyền lực của một doanh nhân thành đạt bậc nhất Phú Quốc.</p>
<p>Đi bên cạnh anh chính là Nguyễn Phương Thảo, nữ Phó Chủ tịch tỉnh sắc sảo, cô mặc chiếc áo dài lụa màu xanh ngọc sang trọng tôn lên khí chất quý phái, thanh lịch.</p>
<p>\"Thật là một kiệt tác kiến trúc xanh tuyệt vời ngoài sức tưởng tượng, ông Trịnh,\" Ngài Đại sứ Thụy Điển trầm trồ khen ngợi không ngớt lời khi bước xuống ca nô tuần tra.</p>
<p>\"Tôi chưa từng thấy một khu nghỉ dưỡng nào kết hợp hoàn hảo giữa sự sang trọng xa xỉ bậc nhất và bảo tồn thiên nhiên nghiêm ngặt đến như vậy. Đây thực sự là tương lai của ngành du lịch thế giới!\"</p>
<p>Gia Bảo dắt ngài Đại sứ đi dọc cây cầu gỗ tầm vông và giải thích chi tiết về kỹ thuật xử lý tre đặc biệt của dự án.</p>
<p>\"Thưa ngài Đại sứ, toàn bộ vật liệu tre ở đây đã trải qua quá trình ngâm tẩm muối áp chân không sinh học và sơn phủ dầu hạt điều tự nhiên.\"</p>
<p>\"Quy trình truyền thống này giúp tre kháng muối biển, chống mối mọt và chịu lực lên đến ba mươi năm mà hoàn toàn không dùng đến hóa chất độc hại gây hại san hô.\"</p>
<p>Ngài Đại sứ Nhật Bản đứng bên cạnh cũng gật đầu tán thưởng đầy kính phục: \"Ở Nhật Bản, chúng tôi cũng rất coi trọng sự hòa hợp giữa kiến trúc và thiên nhiên, nhưng công trình nổi sinh thái này của anh thực sự là một bước tiến vượt bậc của kỹ thuật hiện đại Việt Nam.\"</p>
<p>Gia Bảo mỉm cười lịch thiệp, cúi đầu chào vị khách quý quốc tế: \"Cảm ơn ngài Đại sứ đã dành lời khen tặng. Triết lý thiết kế của chúng tôi là con người không làm chủ thiên nhiên, chúng ta chỉ là những vị khách may mắn được thiên nhiên chào đón và che chở.\"</p>
<p>Phương Thảo nhìn Gia Bảo bằng ánh mắt đầy tự hào và ngưỡng mộ sâu sắc, sự kiên trì phi thường và tài năng thiên bẩm của anh đã giúp du lịch Phú Quốc lấy lại thể diện quốc tế sau vụ bê bối Băng Dương Resort.</p>
<p>Trong khi Kỳ Quan Xanh đón nhận những cơn mưa lời khen từ giới ngoại giao và truyền thông quốc tế lớn, thì ở đất liền, cuộc truy quét đường dây tội phạm của Bernard Dupont đã đi vào giai đoạn phán quyết cuối cùng.</p>
<p>Nhờ những bằng chứng đắt giá từ chiếc ổ cứng của Lê Văn Hùng giao nộp và sự phối hợp quốc tế của tổ chức Interpol, Bernard Dupont đã bị lực lượng an ninh sân bay Tân Sơn Nhất bắt giữ khẩn cấp khi gã đang cố tình sử dụng hộ chiếu giả của nước khác để bay sang Bangkok trốn chạy.</p>
<p>Toàn bộ tài khoản ngân hàng trị giá hơn một nghìn tỷ đồng của tập đoàn Dupont tại Việt Nam bị cơ quan cảnh sát phong tỏa hoàn toàn để khắc phục các hậu quả sai phạm lấn chiếm rừng phòng hộ và trốn thuế quy mô lớn.</p>
<p>Hơn mười cán bộ biến chất tại các ban ngành địa phương nhận hối lộ nâng đỡ cho sòng bạc trá hình cũng đã bị đình chỉ công tác khẩn cấp, khởi tố hình sự tội nhận hối lộ và lợi dụng chức vụ quyền hạn.</p>
<p>Dưới sự chỉ đạo quyết liệt và không khoan nhượng của Nguyễn Phương Thảo, môi trường đầu tư Phú Quốc đang được thanh lọc vô cùng mạnh mẽ, mở đường cho những giá trị du lịch xanh bền vững lên ngôi thống trị.</p>
<p>Đêm đó, trên ban công lộng gió của biệt thự Tổng thống tại Kỳ Quan Xanh, Gia Bảo và Phương Thảo cùng nhau nâng ly rượu vang đỏ chúc mừng chiến thắng vang dội.</p>
<p>Gió biển An Thới thổi lộng lẫy mát rượi, ánh trăng vàng trải dài trên mặt biển lung linh huyền ảo như một bức tranh dát vàng vô giá.</p>
<p>\"Anh Bảo, anh đã thực sự biến giấc mơ không tưởng thành hiện thực rồi,\" Phương Thảo khẽ nói, ánh mắt cô phản chiếu ánh trăng lấp lánh đầy cảm xúc.</p>
<p>\"Anh đã thực sự trở thành vị Chúa Đảo danh tiếng thực thụ của vùng biển phía Nam đảo ngọc này rồi đấy.\"</p>
<p>Gia Bảo nhìn ra khơi xa, nụ cười nửa miệng đầy mưu trí và tự tin hiện rõ trên môi: \"Đây mới chỉ là bước khởi đầu cho đế chế sinh thái của chúng ta thôi, chị Thảo.\"</p>
<p>\"Tôi sẽ mua lại và hồi sinh cả vùng biển này, biến toàn bộ khu vực phía Nam Phú Quốc thành một quần đảo di sản sinh thái thực thụ vươn tầm thế giới.\"</p>
<p>\"Và bước tiếp theo... chính là lấy lại đứa con đầu lòng Băng Dương Resort của tôi từ đống tro tàn của sự tham nhũng dơ bẩn ngoài kia.\"</p>
<p>Phương Thảo khẽ mỉm cười nâng ly cùng anh, cô biết chắc chắn rằng, với ý chí sắt đá và tài năng xuất chúng của Trịnh Gia Bảo, không một thế lực nào có thể ngăn cản anh tiến về phía trước.</p>"""

# Chapter 10
ch10 = """<p>Lễ trao giải Du lịch Quốc gia lần thứ 15 được tổ chức vô cùng hoành tráng tại trung tâm hội nghị quốc tế lớn nhất Phú Quốc.</p>
<p>Đây là sự kiện quy tụ toàn bộ các doanh nghiệp lữ hành, các chủ đầu tư bất động sản nghỉ dưỡng hàng đầu Việt Nam, các chuyên gia quốc tế và giới truyền thông trong nước, nước ngoài.</p>
<p>Không khí trong hội trường vô cùng náo nhiệt dưới ánh đèn flash sáng lòa liên tục của hàng trăm phóng viên báo chí lớn.</p>
<p>Trịnh Gia Bảo bước vào hội trường bên cạnh Nguyễn Phương Thảo, lập tức thu hút toàn bộ ống kính phóng viên bởi sự thành công rực rỡ mang tầm quốc tế của siêu dự án Kỳ Quan Xanh.</p>
<p>Các đại gia bất động sản từng khinh rẻ, chế giễu Gia Bảo ngày trước giờ đây đều xì xào bàn tán với vẻ mặt đầy kiêng dè và ngưỡng mộ trước sự trỗi dậy thần kỳ của anh.</p>
<p>Đúng lúc hội nghị đang diễn ra trang trọng, hai chiếc xe cảnh sát chuyên dụng đỗ sịch trước sảnh chính của trung tâm hội nghị.</p>
<p>Dưới sự áp giải nghiêm ngặt của các chiến sĩ công an vũ trang, Bernard Dupont mặc áo tù nhân màu sọc xám và Lê Văn Hùng bị còng tay bấu chặt bước vào sảnh để thực hiện buổi thực nghiệm hiện trường cuối cùng theo lệnh của Viện Kiểm sát.</p>
<p>Chứng kiến hai kẻ từng vô cùng hống hách cướp resort của Trịnh Gia Bảo giờ đây thảm hại, cúi gục đầu nhục nhã trước ống kính truyền thông báo chí, cả hội trường ồ lên bàn tán xôn xao đầy khinh bỉ.</p>
<p>Hùng ngẩng đầu lên, nhìn thấy Gia Bảo đang đứng ở đỉnh cao danh vọng chói lọi bên cạnh Phó Chủ tịch tỉnh, gã chỉ biết cúi đầu khóc hận trong sự muộn màng và nhục nhã tột cùng không lời nào tả xiết.</p>
<p>Bernard Dupont trừng mắt nhìn Gia Bảo bằng đôi mắt đỏ ngầu, giọng gã khàn đặc đầy bất lực và cam chịu: \"Trịnh Gia Bảo... mày... mày thực sự là một con quái vật... mày đã thắng hoàn toàn rồi.\"</p>
<p>Gia Bảo bước tới trước mặt hai kẻ phản bội, ánh mắt anh vô cùng thản nhiên, kiêu hãnh và đầy uy nghi của một vị chúa tể.</p>
<p>\"Tôi không chỉ giành lại công lý và chiến thắng, Bernard,\" Gia Bảo chậm rãi nói, giọng điệu đanh thép vang vọng khắp sảnh lớn trung tâm hội nghị.</p>
<p>\"Hôm nay, trước toàn thể quý vị quan khách và giới truyền thông, tôi có một thông báo cực kỳ quan trọng muốn công bố chính thức.\"</p>
<p>Gia Bảo quay sang phía các phóng viên báo chí, khẽ gật đầu ra hiệu đầy tự tin.</p>
<p>Lập tức, trên màn hình LED khổng lồ của hội trường hiện lên văn bản quyết định chính thức của UBND tỉnh Kiên Giang do chính Nguyễn Phương Thảo ký duyệt.</p>
<p>\"Quyết định thu hồi vĩnh viễn toàn bộ đất dự án Băng Dương Resort do chủ đầu tư có các sai phạm nghiêm trọng về đất đai và bảo tồn rừng phòng hộ quốc gia.\"</p>
<p>\"Đồng thời, chấp thuận kết quả bán đấu giá tài sản công ích trên đất của dự án Băng Dương cho người trúng đấu giá hợp pháp duy nhất - Công ty Cổ phần Đầu tư Sinh thái Kỳ Quan Xanh do ông Trịnh Gia Bảo làm Chủ tịch Hội đồng Quản trị!\"</p>
<p>Cả hội trường như bùng nổ trong tiếng vỗ tay rầm rộ như sấm truyền và tiếng trầm trồ kinh ngạc tột độ của hàng trăm doanh nhân, tài phiệt lớn có mặt.</p>
<p>Gia Bảo dõng dạc tuyên bố trước toàn thể ống kính truyền thông quốc tế: \"Tôi chính thức mua lại toàn bộ Băng Dương Resort với giá trị giao dịch một ngàn hai trăm tỷ đồng thanh toán một lần.\"</p>
<p>\"Từ ngày hôm nay, Băng Dương Resort sẽ được đổi tên thành 'Kỳ Quan Xanh Bãi Sao', được cải tạo hoàn toàn theo chuẩn sinh thái sinh quyển 100%, đập bỏ hoàn toàn khu casino dơ bẩn trái phép để trả lại màu xanh nguyên bản cho rừng phòng hộ Phú Quốc.\"</p>
<p>\"Chúng tôi sẽ sát nhập hai siêu dự án làm một quần thể bảo tồn sinh thái biển lớn nhất Việt Nam tại quần đảo An Thới và Bãi Sao.\"</p>
<p>Phương Thảo bước lên bục phát biểu, dõng dạc khẳng định triết lý phát triển mới của tỉnh: \"Kiên Giang kiên quyết nói không với các dự án tàn phá thiên nhiên nhân danh phát triển.\"</p>
<p>\"Chúng tôi sẽ áp dụng các tiêu chuẩn sinh thái nghiêm ngặt nhất cho toàn bộ quần đảo An Thới để bảo vệ môi trường cho thế hệ tương lai, và Kỳ Quan Xanh chính là ngọn hải đăng dẫn lối cho tầm nhìn đó.\"</p>
<p>Bernard Dupont đổ sụp hoàn toàn xuống sàn nhà cẩm thạch, mặt xám ngoét không còn một giọt máu, tinh thần hoàn toàn điên loạn.</p>
<p>Gã trợ lý cũ phản bội Lê Văn Hùng gào khóc thảm thiết đầy tuyệt vọng khi bị lực lượng cảnh sát kéo đi áp giải ra xe tù, gã hiểu rằng cả phần đời còn lại gã sẽ phải sống trong sự hối hận muộn màng sau bốn bức tường giam lạnh lẽo.</p>
<p>Nguyễn Phương Thảo bước lên sân khấu chính, trang trọng trao cho Trịnh Gia Bảo chiếc cúp vàng danh giá nhất \"Doanh nhân Vì Môi trường Quốc gia\".</p>
<p>Dưới ánh đèn sân khấu lộng lẫy và tiếng vỗ tay rộn rã chúc mừng kéo dài không dứt của cả hội trường, Gia Bảo đứng bên cạnh Phương Thảo, ánh mắt hướng về vùng biển Phú Quốc xanh bao la lộng lẫy ngoài cửa sổ kính.</p>
<p>Anh tự hứa với bản thân sẽ cống hiến trọn đời để giữ gìn vẻ đẹp hoang sơ, tráng lệ của quê hương đất nước Việt Nam.</p>
<p>Anh đã lấy lại tất cả danh dự và tài sản bằng chính tài năng phi thường của mình, bắt những kẻ phản bội tàn ác phải trả cái giá thích đáng nhất trước pháp luật nghiêm minh, và trở thành vị Chúa Đảo thực thụ - người bảo hộ vĩ đại cho màu xanh vĩnh cửu của đảo ngọc Phú Quốc.</p>
<p>Một chương mới vô cùng huy hoàng, rực rỡ và phát triển bền vững đã thực sự được mở ra cho hòn đảo ngọc thân yêu của đất nước Việt Nam.</p>"""

novel_data["chapters"].append({"title": "Chương 1: Đêm Trắng Ở Bãi Sao", "content": ch1})
novel_data["chapters"].append({"title": "Chương 2: Cuộc Gặp Gỡ Định Mệnh Trên Chuyến Phà Đất Liền", "content": ch2})
novel_data["chapters"].append({"title": "Chương 3: Lòng Tham Lộ Diện", "content": ch3})
novel_data["chapters"].append({"title": "Chương 4: Liên Minh Thầm Lặng", "content": ch4})
novel_data["chapters"].append({"title": "Chương 5: Quân Bài Bí Mật - Hòn Đảo Phía Nam", "content": ch5})
novel_data["chapters"].append({"title": "Chương 6: Bão Nổi Trên Biển Tây", "content": ch6})
novel_data["chapters"].append({"title": "Chương 7: Thanh Tra Đột Xuất", "content": ch7})
novel_data["chapters"].append({"title": "Chương 8: Gậy Ông Đập Lưng Ông", "content": ch8})
novel_data["chapters"].append({"title": "Chương 9: Chúa Đảo Thật Sự Lộ Diện", "content": ch9})
novel_data["chapters"].append({"title": "Chương 10: Vả Mặt Huy Hoàng, Phú Quốc Sang Trang", "content": ch10})

# Verify before saving
print("=== VERIFYING WORD COUNTS ===")
valid = True
for idx, chap in enumerate(novel_data["chapters"], start=1):
    content = chap["content"]
    title = chap["title"]
    # Estimate words
    words = content.replace("<p>", "").replace("</p>", "").replace("\n", " ").split()
    word_count = len(words)
    print(f"Chapter {idx} ({title}): {word_count} words")
    if word_count < 1000 or word_count > 1500:
        print(f"-> WARNING: CHAPTER {idx} HAS {word_count} WORDS (OUTSIDE 1000-1500 RANGE!)")
        valid = False
    
    # Check V13 tags
    lines = content.strip().split("\n")
    for l_idx, line in enumerate(lines):
        line_stripped = line.strip()
        if not (line_stripped.startswith("<p>") and line_stripped.endswith("</p>")):
            print(f"-> WARNING: Formatting error in Chapter {idx}, line {l_idx+1}: {line_stripped}")
            valid = False

if valid:
    # Save the final file
    with open(final_file_path, "w", encoding="utf-8") as f:
        json.dump(novel_data, f, ensure_ascii=False, indent=2)
    print("Verification SUCCESS! Final JSON written to:", final_file_path)
    
    # Clean up scripts and temp files
    temp_file_path = "/Users/aaronnguyen/TN/App/doctieuthuyet/pending_novel_10_temp.json"
    if os.path.exists(temp_file_path):
        os.remove(temp_file_path)
        print("Stage 4: Temporary file deleted successfully.")
else:
    print("Verification FAILED! Output file not written.")
