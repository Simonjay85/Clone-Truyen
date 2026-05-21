# -*- coding: utf-8 -*-
import sys
import os
import time

sys.path.append('scratch')
import novel_editor
import upload_cover_local

STORY_ID = 2227

# Pre-written V12 Chapters for Story 2227 (Da Lat Programmer Technology Thriller)
ch1_sentences = [
    "Tôi tên là Trần Hưng.",
    "Tôi là một cựu kỹ sư bảo mật hệ thống cao cấp, từng có nhiều năm lăn lộn tại các tập đoàn công nghệ hàng đầu ở Sài Gòn.",
    "Nhưng nửa năm trước, cảm thấy quá mệt mỏi với nhịp sống xô bồ và những cuộc đấu đá chốn công sở, tôi quyết định rời bỏ thành phố để lên Đà Lạt sống ẩn dật.",
    "Hiện tại, tôi thuê một căn homestay gỗ nhỏ nép mình dưới sườn đồi thông xanh ngắt ở đường Khe Sanh.",
    "Mỗi ngày trôi qua của tôi vô cùng giản dị, bình lặng và tự do tự tại.",
    "Sáng sớm, tôi thường tự tay pha một ly cà phê Arabica nóng hổi, ngắm nhìn thung lũng sương mù dày đặc trôi lững lờ dưới chân đồi Khe Sanh đầy mộng mơ.",
    "Công việc chính của tôi là làm lập trình viên tự do cho các dự án bảo mật từ xa của các đối tác nước ngoài.",
    "Số tiền kiếm được từ các hợp đồng này đủ để tôi sống một cuộc đời thoải mái mà không cần phải lo toan nhiều về cơm áo gạo tiền.",
    "Tuy nhiên, sự bình yên đó đã bị phá vỡ hoàn toàn vào một đêm sương mù dày đặc che phủ toàn bộ thành phố Đà Lạt.",
    "Đó là đêm thứ năm tuần trước, khi gió lạnh từ đỉnh Langbiang thổi về làm căn biệt thự gỗ nhỏ của tôi khẽ rung lên bần bật trong đêm tối.",
    "Tôi ngồi trước bàn làm việc, ánh đèn led từ chiếc màn hình máy tính UltraWide hắt lên khuôn mặt tôi những vệt sáng xanh cô độc.",
    "Trong lúc rảnh rỗi sau khi hoàn thành dự án, tôi vô tình khởi động công cụ quét dữ liệu blockchain do mình tự phát triển.",
    "Mục tiêu quét ngẫu nhiên của tôi hôm đó là ví lạnh chứa hợp đồng thông minh ERC-20 của tập đoàn tài chính Thịnh Phát.",
    "Thịnh Phát chính là tập đoàn tài chính lớn nhất nhì cả nước, cũng là nơi tôi từng cống hiến suốt hai năm trước khi xin từ chức.",
    "Chỉ sau mười phút chạy thuật toán truy vết chuyên sâu, màn hình máy tính của tôi bỗng nhiên chớp nháy liên hồi đầy bất thường.",
    "Hàng loạt dòng lệnh cảnh báo màu đỏ tươi hiện lên cảnh báo lỗ hổng nghiêm trọng.",
    "Hệ thống báo: “Phát hiện lỗ hổng backdoor cố ý trong Smart Contract số hiệu khôngxétbảyép...támtámchínba.”",
    "Tôi lập tức nhíu mày, các ngón tay bắt đầu gõ phím nhanh như chớp để đi sâu vào phân tích mã nguồn của hợp đồng thông minh này.",
    "Càng đọc sâu vào cấu trúc các dòng mã Solidity, mồ hôi lạnh trên trán tôi càng rịn ra nhiều hơn vì kinh hãi.",
    "Đây hoàn toàn không phải là một lỗi lập trình vô ý do sự cẩu thả của đội ngũ kỹ sư tập đoàn.",
    "Đây là một backdoor cực kỳ tinh vi được cố ý cài cắm từ bên trong hệ thống giao dịch lõi.",
    "Backdoor này cho phép một tài khoản quản trị ẩn danh định tuyến lại và rút ruột hàng triệu USD từ quỹ đầu tư của khách hàng mà không ai hay biết.",
    "Sau đó, dòng tiền ảo phi pháp này sẽ được chuyển đổi tự động qua các sàn giao dịch phi tập trung và đổ về các tài khoản ngân hàng offshore tại quần đảo Cayman.",
    "Tổng số tiền dịch chuyển phi pháp tính đến thời điểm tôi phát hiện đã lên đến hơn năm mươi triệu USD, tương đương hơn một nghìn tỷ đồng.",
    "Điều đáng sợ là toàn bộ dữ liệu giao dịch này đã được ngụy trang hoàn hảo dưới dạng các giao dịch hoàn phí nội bộ thông thường của tập đoàn.",
    "If không phải là người trực tiếp tham gia xây dựng nền tảng cốt lõi của Thịnh Phát năm xưa, tôi chắc chắn cũng đã bị che mắt.",
    "Tôi tựa lưng vào ghế gỗ, ngón tay gõ nhịp đều đặn lên mặt bàn đầy trăn trở về tương lai của tập đoàn cũ.",
    "Tập đoàn Thịnh Phát hiện tại đang được điều hành bởi những ai?",
    "Tôi nhớ đến Minh Khuê, cô con gái cả của vị chủ tịch sáng lập tập đoàn.",
    "Cô ấy là một phó giám đốc tài chính tài ba, nổi tiếng sắc sảo, độc lập và cực kỳ chính trực trong giới tài chính nước nhà.",
    "Chắc chắn Minh Khuê hoàn toàn không hề biết đến sự tồn tại của lỗ hổng rửa tiền khổng lồ đang tàn phá tập đoàn này.",
    "Tôi khẽ lẩm bẩm một mình giữa đêm đông lạnh giá: “Có kẻ đang âm mưu nuốt chửng cả tập đoàn Thịnh Phát từ bên trong một cách tàn nhẫn.”",
    "Tiếng thông reo rì rào bên ngoài cửa sổ như đang đồng tình với nhận định đầy lo âu của tôi.",
    "Tôi quyết định tải toàn bộ dữ liệu giao dịch đã truy vết được vào một ổ cứng di động mã hóa bảo mật hai lớp cực kỳ an toàn.",
    "Tôi biết, một cơn bão tài chính khủng khiếp sắp sửa ập đến, và tôi vừa vô tình đứng ngay giữa tâm bão dữ."
]

ch2_sentences = [
    "Chiều hôm sau, trời Đà Lạt đột ngột đổ cơn mưa phùn lạnh buốt thấu xương.",
    "Những hạt mưa li ti hòa cùng sương mù dày đặc tạo nên một bầu không khí u sầu bao phủ khắp các ngõ dốc quanh co.",
    "Tôi mặc chiếc áo khoác len dày màu xám, đi bộ dọc theo những con dốc để đến quán cà phê Tùng nằm sâu trong một con hẻm nhỏ.",
    "Cà phê Tùng là địa điểm yêu thích của tôi mỗi khi cần tìm sự yên tĩnh để tập trung viết code bảo mật.",
    "Quán nhỏ nhắn, bức tường quét vôi vàng cũ kỹ ám mùi thời gian, những bộ bàn ghế gỗ thô mộc luôn gợi lên cảm giác hoài cổ sâu sắc.",
    "Tiếng nhạc cổ điển Trịnh Công Sơn vang lên trầm buồn, hòa cùng tiếng mưa rơi lách tách ngoài hiên cửa kính.",
    "Tôi chọn một góc bàn tối cạnh cửa sổ, mở chiếc laptop ThinkPad ra để tiếp tục kiểm tra luồng giao dịch bẩn của Thịnh Phát.",
    "Đột nhiên, tiếng chuông gió ở cửa quán vang lên leng keng phá tan không gian yên ắng.",
    "Một cô gái bước vào quán, mang theo hơi lạnh ẩm ướt của cơn mưa chiều Đà Lạt đầy sương mù.",
    "Cô ấy mặc một chiếc măng tô màu be sang trọng, cổ quấn khăn len xám ấm áp ôm sát bờ vai thon thả.",
    "Gương mặt cô ấy vô cùng thanh tú nhưng đôi mắt lại lộ rõ vẻ mệt mỏi và lo âu tột cùng sau nhiều ngày mất ngủ.",
    "Đó chính là Minh Khuê, ái nữ kiên cường kiêm phó giám đốc tài chính của tập đoàn tài chính Thịnh Phát.",
    "Tôi ngạc nhiên đến mức suýt chút nữa đánh rơi ly cà phê phin đang nhỏ giọt lách tách trên bàn gỗ.",
    "Minh Khuê nhìn quanh quán một lượt, và ánh mắt sắc sảo của cô lập tức dừng lại ở góc bàn của tôi.",
    "Cô ấy bước thẳng tới, tự tay kéo chiếc ghế gỗ đối diện rồi ngồi xuống một cách cực kỳ dứt khoát.",
    "Giọng cô ấy trầm thấp nhưng rõ ràng từng chữ: “Chào anh Hưng, cuối cùng em cũng tìm được anh ở nơi hẻo lánh này.”",
    "Tôi khẽ mỉm cười nhấp một ngụm cà phê đắng: “Chào phó giám đốc Minh Khuê, không ngờ cô lại lặn lội từ Sài Gòn lên tận đây tìm tôi.”",
    "Minh Khuê không hề vòng vo xã giao, cô ấy đi thẳng vào vấn đề chính với phong thái của một nữ cường nhân thực sự.",
    "“Anh Hưng, em biết anh là lập trình viên bảo mật giỏi nhất mà Thịnh Phát từng có trước đây.”",
    "“Tập đoàn của gia đình em đang gặp nguy hiểm cực kỳ lớn, có thể sụp đổ bất cứ lúc nào.”",
    "“Ba của em đang bị giam lỏng tại một căn biệt thự ngoại ô bởi phe cánh của tổng giám đốc Vương Thế Hùng phản bội.”",
    "“Lão ta đang ép ba em phải ký giấy chuyển nhượng toàn bộ cổ phần kiểm soát tập đoàn cho lão vào cuối tháng này.”",
    "“Em đã phát hiện ra có sự thâm hụt tài chính khổng lồ trong quỹ đầu tư chung, nhưng không tài nào tìm ra bằng chứng kỹ thuật.”",
    "Tôi lặng lẽ xoay chiếc laptop ThinkPad của mình sang phía cô ấy để cô nhìn rõ màn hình.",
    "Trên màn hình hiển thị trực quan sơ đồ luồng tiền ảo được mã hóa chi tiết với các mũi tên đỏ hướng thẳng sang Cayman.",
    "Tôi khẽ nói bằng giọng trầm ấm: “Cô nhìn cái này đi, câu trả lời nằm ở đây.”",
    "Minh Khuê chăm chú nhìn vào màn hình, đôi đồng tử của cô đột ngột co rút lại vì kinh ngạc tột độ.",
    "Cô ấy thốt lên thì thầm: “Backdoor rửa tiền qua hợp đồng thông minh ERC-20... Hóa ra là thế!”",
    "“Vương Thế Hùng đang âm thầm tẩu tán toàn bộ tài sản của khách hàng để chuẩn bị cho một cuộc tháo chạy quy mô lớn!”",
    "Cô ấy ngẩng đầu lên nhìn tôi, ánh mắt kiên định, sắc sảo và tràn đầy sự sòng phẳng của một nhà điều hành tài chính chuyên nghiệp.",
    "“Anh Hưng, em không thích nói chuyện tình cảm hay nhờ vả không công dưới danh nghĩa người quen cũ.”",
    "“Chúng ta hãy hợp tác sòng phẳng dưới hình thức một giao dịch thương mại có hợp đồng rõ ràng.”",
    "“Nếu anh giúp em lấy lại quyền kiểm soát hệ thống, vạch trần backdoor và giải cứu ba em khỏi tay kẻ phản bội.”",
    "“Em cam kết sẽ chuyển nhượng cho anh mười phần trăm cổ phần của công ty công nghệ trực thuộc tập đoàn Thịnh Phát.”",
    "“Giá trị số cổ phần đó ở thời điểm hiện tại không dưới năm mươi tỷ đồng.”",
    "“Đồng thời, em sẽ mở một tài khoản Vietcombank chi nhánh Đà Lạt đứng tên anh, cam kết ký quỹ trước năm tỷ đồng làm chi phí hoạt động.”",
    "“Anh thấy điều kiện hợp tác này thế nào?”",
    "Tôi nhìn sâu vào đôi mắt trong veo nhưng vô cùng sắc sảo, kiên định của Minh Khuê.",
    "Tôi cảm nhận được bản lĩnh phi thường và sự chân thành của cô gái này trước giông bão cuộc đời.",
    "Tôi khẽ đóng nắp laptop lại, nở một nụ cười ấm áp: “Thỏa thuận thành công, tôi đồng ý giúp cô lấy lại công lý.”"
]

ch3_sentences = [
    "Tôi đưa Minh Khuê về căn biệt thự gỗ nhỏ của tôi ẩn mình giữa rừng thông trên đường Khe Sanh.",
    "Nơi đây cách biệt hoàn toàn với sự ồn ào náo nhiệt của khu trung tâm Đà Lạt, xung quanh chỉ có tiếng gió thông reo rì rào.",
    "Để chuẩn bị cho trận chiến công nghệ đầy cam go này, tôi dẫn Minh Khuê vào phòng làm việc ở tầng hai của căn biệt thự.",
    "Căn phòng tràn ngập mùi gỗ thông thơm nhẹ dễ chịu, được trang bị hệ thống máy tính chuyên dụng có cấu hình cực mạnh do tôi tự tay lắp ráp.",
    "Minh Khuê lập tức mở chiếc máy tính bảng bảo mật của cô ra, thực hiện một lệnh chuyển tiền nhanh qua ứng dụng ngân hàng.",
    "Chỉ hai phút sau, điện thoại của tôi rung lên báo tin nhắn thông báo biến động số dư từ ngân hàng Vietcombank.",
    "“Tài khoản của bạn đã được cộng năm tỷ đồng từ người gửi Nguyễn Minh Khuê.”",
    "Minh Khuê điềm tĩnh nói: “Đây là chi phí hoạt động ban đầu như đã hứa, anh hãy dùng nó để thuê những tài nguyên mạng tốt nhất.”",
    "Tôi gật đầu gõ bàn phím liên hồi, sử dụng số tiền này để đăng ký thuê cụm máy chủ AWS (Amazon Web Services) phân tán tại Singapore.",
    "Hệ thống máy chủ đám mây AWS này có năng lực tính toán cực kỳ khổng lồ, giúp giải mã các block giao dịch nhanh gấp trăm lần máy tính thông thường.",
    "Tôi bắt đầu viết các đoạn mã Python phức tạp bằng thư viện Web3.py để truy quét sâu vào từng hợp đồng thông minh trên mạng lưới Ethereum.",
    "Đêm Đà Lạt nhiệt độ giảm sâu xuống dưới mười hai độ C, sương mù dày đặc tràn vào qua khe cửa kính làm căn phòng lạnh buốt.",
    "Minh Khuê không hề đi ngủ, cô ấy lẳng lặng xuống bếp tự tay pha hai tách trà Atiso ấm nóng mang lên phòng làm việc cho hai đứa.",
    "Cô ấy đặt tách trà nghi ngút khói cạnh tay tôi, khẽ nói bằng giọng dịu dàng: “Anh uống nước đi cho ấm người, đừng để bị lạnh.”",
    "Tôi nhấp một ngụm trà ngọt mát ấm áp, cảm giác ấm nồng lập tức lan tỏa khắp cơ thể xua tan cái lạnh Đà Lạt.",
    "Chúng tôi cùng nhau thức trắng đêm bên cạnh những dòng lệnh màu xanh lá cây chạy dọc màn hình máy tính liên tục không ngừng nghỉ.",
    "Mỗi khi phát hiện ra một giao dịch bẩn mới, Minh Khuê lại nhanh chóng dùng đầu óc tài chính sắc sảo để phân tích số liệu đối ứng.",
    "Sự phối hợp ăn ý giữa tư duy lập trình đỉnh cao của tôi và tư duy tài chính của cô ấy diễn ra vô cùng hoàn hảo.",
    "Tiếng gõ phím lạch cạch của tôi hòa cùng tiếng gió rít qua những tán thông già ngoài biệt thự tạo nên một bầu không khí vô cùng kịch tính.",
    "Đến bốn giờ sáng, tôi đã thành công thiết lập được một bản đồ truy vết dòng tiền thời gian thực cực kỳ chi tiết và trực quan.",
    "Bản đồ này chỉ ra chính xác cách thức mà Vương Thế Hùng chuyển tiền bẩn qua các ví trung gian trước khi quy đổi ra tiền mặt tại nước ngoài.",
    "Minh Khuê nhìn vào bản đồ dòng tiền trên màn hình, ánh mắt cô lạnh lùng và kiên định như băng giá đồi thông.",
    "Cô ấy khẽ nói: “Lần này tôi nhất định sẽ bắt lão ta phải trả giá đắt trước pháp luật, không để lão lộng hành thêm nữa.”"
]

ch4_sentences = [
    "Đúng lúc nghiên cứu truy vết của chúng tôi bước vào giai đoạn then chốt nhất.",
    "Màn hình máy tính của tôi bỗng nhiên chuyển sang màu đỏ rực rỡ kèm theo những tiếng bíp bíp dồn dập đầy nguy hiểm.",
    "Biểu đồ lưu lượng truy cập mạng AWS báo cáo một đợt tấn công DDoS (Từ chối dịch vụ) khổng lồ đang dội thẳng vào hệ thống của tôi.",
    "Băng thông mạng lập tức bị nghẽn nghiêm trọng, khiến tốc độ truy xuất dữ liệu giảm xuống gần như bằng không trong nháy mắt.",
    "Tôi lập tức phát hiện ra có kẻ đang cố ý tấn công từ xa để phá hủy tiến trình giải mã giao dịch của chúng tôi.",
    "Minh Khuê lo lắng nhìn tôi hỏi: “Có chuyện gì nghiêm trọng thế anh Hưng, hệ thống bị hack rồi sao?”",
    "Tôi bình tĩnh nở nụ cười tự tin, ngón tay gõ phím nhanh như gió: “Phe Vương Thế Hùng đã phát hiện ra có người đang truy vết dòng tiền bẩn của chúng.”",
    "“Lão ta chắc chắn đã bỏ ra số tiền lớn thuê nhóm hacker chuyên nghiệp quốc tế để tiêu diệt hệ thống máy chủ của tôi.”",
    "Chưa dừng lại ở đó, bên ngoài căn biệt thự gỗ bỗng nhiên có tiếng động cơ xe máy gầm rú phá tan sự tĩnh lặng của đồi thông.",
    "Hai chiếc xe bán tải màu đen không biển số chạy tới đỗ xịch ngay trước cổng biệt thự gỗ của tôi.",
    "Nhiều gã đàn ông mặc vest đen bặm trợn bước xuống xe, trên tay cầm các thiết bị quét sóng vô tuyến chuyên dụng để dò tìm.",
    "Chúng đang cố gắng dò tìm tần số sóng wifi của căn nhà để định vị chính xác vị trí máy chủ của tôi nhằm đột nhập cướp dữ liệu.",
    "Minh Khuê đứng bật dậy, gương mặt cô lộ rõ vẻ căng thẳng tột độ trước tình huống nguy hiểm cận kề.",
    "Tôi nắm chặt lấy bàn tay lạnh ngắt của cô, giọng nói vô cùng tự tin để trấn an cô: “Đừng sợ, có tôi ở đây, bọn chúng không làm gì được đâu.”",
    "Tôi lập tức kích hoạt giao thức Honeypot (Bẫy mật) thông minh đã thiết lập sẵn trong hệ thống phòng thủ của mình.",
    "Tôi chuyển hướng toàn bộ lưu lượng tấn công khổng lồ kia sang một máy chủ ảo chứa đầy dữ liệu giả lập không có giá trị để đánh lừa chúng.",
    "Đồng thời, tôi sử dụng kỹ thuật định tuyến ngược thông minh qua mạng Tor để truy tìm địa chỉ IP nguồn của kẻ tấn công mạng.",
    "Chỉ sau ba phút đấu trí căng thẳng trên bàn phím, tôi đã xác định được chính xác tọa độ của nhóm hacker đối phương đang hoạt động.",
    "Chúng đang ngồi trong một căn hộ cao cấp tại khu Thảo Điền, quận hai, thành phố Hồ Chí Minh dưới sự chỉ đạo của Vương Thế Hùng.",
    "Tôi cười lạnh, lập tức gửi ngược lại một đoạn mã độc mã hóa toàn bộ hệ thống máy tính của nhóm hacker đối phương kia.",
    "Màn hình của chúng chắc chắn đã bị đóng băng hoàn toàn kèm theo thông báo đòi tiền chuộc hài hước bằng tiếng Việt do tôi soạn thảo.",
    "Bên ngoài cổng biệt thự, hệ thống đèn pha quét tự động của biệt thự đột ngột bật sáng rực rỡ kèm tiếng còi báo động rú vang khắp đồi thông.",
    "Nhóm người bặm trợn bên ngoài cổng giật mình hoảng hốt, vội vàng lên xe bán tải bỏ chạy trối chết trong màn sương mù dày đặc Đà Lạt."
]

ch5_sentences = [
    "Sáng hôm sau, cơn bão thực sự từ phía tập đoàn Thịnh Phát mới bắt đầu đổ bộ lên Đà Lạt sương mù.",
    "Minh Khuê vừa thức dậy liền nhận được thông báo khẩn cấp từ ứng dụng ngân hàng trực tuyến trên điện thoại cá nhân.",
    "Toàn bộ tài khoản cá nhân và tài khoản doanh nghiệp đứng tên cô tại Vietcombank và MB Bank đã bị đóng băng hoàn toàn không lý do.",
    "Lý do ngân hàng đưa ra là có lệnh phong tỏa khẩn cấp từ tổng giám đốc lâm thời Vương Thế Hùng để phục vụ điều tra nội bộ tập đoàn.",
    "Minh Khuê run rẩy nắm chặt chiếc điện thoại, sắc mặt cô nhợt nhạt hẳn đi vì lo lắng cho ba cô và tương lai tập đoàn.",
    "“Vương Thế Hùng điên thật rồi, lão ta muốn triệt tiêu toàn bộ nguồn lực tài chính của em để ép em đầu hàng vô điều kiện.”",
    "Tôi nhẹ nhàng bước tới bên cạnh cô, vỗ nhẹ lên vai cô để truyền cho cô sự tự tin ấm áp giữa mùa đông lạnh giá.",
    "“Không sao cả, tài khoản Vietcombank Đà Lạt của tôi vẫn hoàn toàn an toàn, số tiền năm tỷ cô chuyển hôm qua dư sức để chúng ta chiến đấu đến cùng.”",
    "Tuy nhiên, sự việc lại càng trở nên tồi tệ hơn khi bọn chúng bắt đầu ra tay phá hoại hạ tầng vật lý của căn nhà.",
    "Đường dây điện thoại nóng của biệt thự bất ngờ bị cắt đứt, mạng internet cáp quang tốc độ cao cũng bị ngắt kết nối vật lý từ bên ngoài.",
    "Bọn chúng đã âm thầm cho người phá hoại tủ cáp truyền dẫn trên đường Khe Sanh hòng cô lập hoàn toàn chúng tôi.",
    "Nhìn ra ngoài cửa sổ đồi thông, tôi thấy xuất hiện thêm nhiều gã đàn ông mặc vest đen lảng vảng xung quanh khuôn viên biệt thự.",
    "Chúng canh gác nghiêm ngặt tất cả các lối ra vào đồi thông, sẵn sàng ập vào khống chế và cướp chiếc ổ cứng chứa dữ liệu bất cứ lúc nào.",
    "Minh Khuê lo lắng tột cùng, cô ấy đan chặt hai bàn tay vào nhau đến mức các khớp ngón tay trắng bệch vì sợ hãi cho sự an toàn của cả hai.",
    "Tôi mỉm cười điềm tĩnh, khởi động thiết bị kết nối internet vệ tinh Starlink dự phòng mà tôi đã lắp đặt bí mật trên mái nhà biệt thự.",
    "Chỉ trong nháy mắt, đường truyền mạng tốc độ cao đã được khôi phục hoàn toàn qua kết nối vệ tinh trực tiếp không phụ thuộc cáp đất.",
    "Tôi nhanh chóng đẩy toàn bộ cơ sở dữ liệu đã giải mã lên đám mây lưu trữ phi tập trung IPFS có tính năng bảo mật tuyệt đối vô song.",
    "Tôi quay sang bảo Minh Khuê: “Em hãy dùng điện thoại kết nối internet vệ tinh này, gọi điện trực tiếp cho đồng chí giám đốc công an tỉnh Lâm Đồng.”",
    "“Hãy báo cáo rằng tính mạng của em đang bị đe dọa nghiêm trọng bởi một băng nhóm tội phạm có tổ chức từ Sài Gòn lên bao vây biệt thự.”",
    "Minh Khuê lập tức hiểu ý tôi, cô ấy nhanh chóng thực hiện cuộc gọi với phong thái đĩnh đạc, quyết đoán và sắc sảo vô cùng.",
    "Tôi quay lại bàn làm việc, các ngón tay tiếp tục gõ phím điên cuồng để hoàn thiện những bước giải mã tài chính cuối cùng của vụ án."
]

ch6_sentences = [
    "Khoảng tám giờ sáng, tiếng còi xe cảnh sát hú vang dồn dập từ phía chân đồi Khe Sanh phá tan bầu không khí tĩnh mịch của rừng thông.",
    "Ba chiếc xe chuyên dụng của lực lượng công an tỉnh Lâm Đồng ập đến, nhanh chóng khống chế và kiểm tra hành chính nhóm người mặc vest đen lảng vảng quanh biệt thự.",
    "Hóa ra chúng là đám giang hồ thuê từ Sài Gòn lên để đe dọa chúng tôi, trong người tàng trữ nhiều vũ khí thô sơ trái phép nên lập tức bị bắt giữ đưa về đồn công an.",
    "Mối đe dọa vật lý bên ngoài hoàn toàn được dọn dẹp sạch sẽ nhờ sự can thiệp kịp thời của lực lượng an ninh.",
    "Trong lúc đó, hệ thống máy chủ AWS của tôi cũng vừa hoàn thành block giải mã giao dịch cuối cùng của tập đoàn Thịnh Phát.",
    "Tôi nhấn phím Enter trên bàn phím một cách dứt khoát và mạnh mẽ.",
    "Toàn bộ báo cáo kiểm toán tài chính số chi tiết dài hơn hai trăm trang được xuất ra định dạng file PDF mã hóa cực kỳ chuyên nghiệp.",
    "Bản báo cáo chứa đầy đủ bằng chứng đanh thép, sơ đồ dòng tiền bẩn và chữ ký số của Vương Thế Hùng trong các phi vụ rửa tiền trị giá ba nghìn tỷ đồng.",
    "Minh Khuê nhìn tập tài liệu bằng chứng đanh thép hiển thị trên màn hình máy tính, những giọt nước mắt hạnh phúc bỗng lăn dài trên đôi má thanh tú của cô.",
    "Cô ấy nghẹn ngào thốt lên đầy xúc động: “Chúng ta làm được rồi! Anh Hưng ơi, chúng ta thực sự đã chiến thắng rồi!”",
    "Tôi mỉm cười nhẹ nhàng đưa cho cô ấy một tờ khăn giấy: “Em hãy dùng mạng vệ tinh gửi tập tài liệu này cho C03 Bộ Công an và Ủy ban Chứng khoán Nhà nước ngay đi.”",
    "Minh Khuê gật đầu dứt khoát, lập tức sử dụng tài khoản bảo mật gửi thẳng hồ sơ bằng chứng sang cơ quan điều tra kinh tế tối cao ở Hà Nội và Sài Gòn.",
    "Chúng tôi biết, quân bài domino đầu tiên đã đổ xuống, và Vương Thế Hùng cùng đồng bọn không còn bất kỳ cơ hội nào để lật kèo nữa.",
    "Màn đêm đen tối bao phủ tập đoàn Thịnh Phát suốt nhiều tháng qua sắp sửa bị xua tan hoàn toàn bởi ánh sáng của công lý và pháp luật."
]

ch7_sentences = [
    "Sáng hôm sau, tin tức chấn động nổ ra trên khắp các trang báo lớn và các phương tiện truyền thông của cả nước.",
    "Tiêu đề nổi bật trên tờ báo Thanh Niên và Tuổi Trẻ: “Bắt khẩn cấp Tổng giám đốc tập đoàn Thịnh Phát Vương Thế Hùng về tội rửa tiền và trốn thuế.”",
    "Lực lượng Cục Cảnh sát điều tra tội phạm về tham nhũng, kinh tế, buôn lậu (C03 - Bộ Công an) đã ập vào khống chế và bắt giữ Hùng ngay tại cửa VIP sân bay Tân Sơn Nhất.",
    "Lúc đó, lão đang chuẩn bị làm thủ tục bỏ trốn sang Canada cùng toàn bộ số tiền vàng tẩu tán trái phép.",
    "Toàn bộ đồng bọn của lão trong hội đồng quản trị phản bội cũng lần lượt sa lưới pháp luật chỉ trong một ngày.",
    "Ba của Minh Khuê được lực lượng an ninh giải cứu an toàn từ căn biệt thự ngoại ô, lập tức lấy lại quyền kiểm soát tối cao của tập đoàn Thịnh Phát.",
    "Đà Lạt sáng hôm đó đón một ngày nắng vàng rực rỡ ấm áp, xua tan đi hoàn toàn màn sương mù dày đặc bấy lâu nay che phủ núi đồi.",
    "Tôi và Minh Khuê cùng nhau đi bộ thong thả dưới những tán thông xanh mướt quanh bờ hồ Xuân Hương tĩnh lặng và thơ mộng.",
    "Mặt hồ phẳng lặng như gương, phản chiếu bầu trời xanh ngắt của cao nguyên Đà Lạt và những tia nắng ban mai lấp lánh như pha lê.",
    "Minh Khuê hôm nay mặc một chiếc áo len mỏng màu hồng phấn ấm áp, gương mặt rạng rỡ nụ cười thanh thản và hạnh phúc vô cùng.",
    "Cô ấy dừng chân bên lan can bờ hồ Xuân Hương, khẽ nhắm mắt hít một hơi thật sâu không khí trong lành, mát mẻ của núi rừng Đà Lạt.",
    "“Anh Hưng, đã lâu lắm rồi em mới có được một cảm giác bình yên, tự do và nhẹ nhõm đến thế này sau những giông bão.”",
    "Tôi nhìn góc nghiêng tuyệt đẹp của cô ấy dưới ánh nắng ban mai rực rỡ, trong lòng bỗng dâng lên một cảm xúc vô cùng khó tả và ấm áp.",
    "“Mọi chuyện tồi tệ đã qua rồi, em đã rất kiên cường, bản lĩnh và dũng cảm trước mọi thử thách cực đại.”",
    "Minh Khuê quay sang nhìn tôi, ánh mắt cô lấp lánh tràn ngập sự biết ơn sâu sắc và một thứ tình cảm dịu dàng chớm nở giữa hai tâm hồn."
]

ch8_sentences = [
    "Chúng tôi cùng nhau quay trở lại căn biệt thự gỗ nhỏ nằm giữa rừng thông Khe Sanh yên tĩnh.",
    "Minh Khuê lấy từ trong chiếc túi xách sang trọng ra một tập tài liệu pháp lý đã được công chứng rõ ràng tại văn phòng công chứng Đà Lạt.",
    "Cô ấy đặt tập tài liệu lên bàn gỗ, nghiêm túc nói: “Anh Hưng, đây là hợp đồng chuyển nhượng mười phần trăm cổ phần của công ty công nghệ trực thuộc tập đoàn Thịnh Phát như chúng ta đã cam kết.”",
    "“Đồng thời, em quyết định sẽ đầu tư thành lập Viện Nghiên cứu Bảo mật và Công nghệ Cao ngay tại thung lũng Đà Lạt này, giao cho anh trực tiếp làm Viện trưởng với toàn quyền điều hành.”",
    "Tôi nhìn tập tài liệu pháp lý sòng phẳng, chuyên nghiệp và đầy trọng trị của cô ấy, khẽ mỉm cười gật đầu tán thưởng bản lĩnh của cô.",
    "Tuy nhiên, Minh Khuê bỗng nhiên bước tới gần tôi hơn, ánh mắt cô không còn vẻ lạnh lùng sắc sảo thường ngày mà tràn đầy sự dịu dàng.",
    "Khoảng cách giữa hai chúng tôi lúc này gần đến mức tôi có thể nghe thấy nhịp tim đập khẽ khàng và cảm nhận được hơi ấm từ cô ấy.",
    "Đôi má cô ấy khẽ ửng hồng dưới ánh nắng chiều tà lọc qua những tán thông già Khe Sanh tuyệt đẹp.",
    "Minh Khuê chủ động nắm lấy hai bàn tay tôi, giọng cô ấy run lên nhè nhẹ nhưng vô cùng chân thành, ấm áp và kiên định.",
    "“Anh Hưng, hợp đồng kinh doanh và cổ phần em đã ký xong rồi, đó là bổn phận của em.”",
    "“Nhưng bây giờ, em muốn tự tay ký một bản hợp đồng trọn đời khác với anh dưới tư cách cá nhân của một cô gái.”",
    "“Em muốn cùng anh chia sẻ những vui buồn, vượt qua mọi sóng gió trong cuộc sống sau này, anh có đồng ý làm bạn đời của em không?”",
    "Tôi ngỡ ngàng trước lời tỏ tình chủ động, sòng phẳng nhưng cực kỳ chân thành và dũng cảm của cô gái phó giám đốc sắc sảo này.",
    "Tôi siết chặt bàn tay mềm mại ấm áp của cô, nhìn sâu vào đôi mắt lấp lánh đầy chân thành của cô với tình yêu thương vô bờ bến.",
    "“Anh đồng ý, Minh Khuê, anh muốn làm bạn đời trọn đời bên em.”",
    "Dưới rặng thông reo rì rào của núi rừng Đà Lạt sương mù thơ mộng, chúng tôi trao nhau một nụ hôn ngọt ngào ấm áp, đánh dấu một khởi đầu mới đầy viên mãn và hạnh phúc trọn đời."
]

def format_paragraphs(sentences):
    return "".join([f"<p>{s}</p>" for s in sentences])

def main():
    print("=" * 60)
    print("🚀 PUBLISHING STORY 2227 (V12 TECH THRILLER)")
    print("=" * 60)
    
    # 1. Update Story Metadata
    title = "Thiên Tài Lập Trình Đà Lạt Sương Mù: Tôi Viết Mã Hoá Lật Đổ Tập Đoàn Tài Chính Phản Bội"
    intro = format_paragraphs([
        "Tôi là Trần Hưng, một cựu kỹ sư bảo mật ẩn cư giữa rừng thông Đà Lạt tĩnh lặng.",
        "Nhưng cuộc sống yên bình kết thúc khi tôi phát hiện ra backdoor rửa tiền nghìn tỷ của tập đoàn Thịnh Phát.",
        "Sát cánh cùng Minh Khuê - ái nữ kiên cường của chủ tịch sáng lập, chúng tôi bắt đầu cuộc đấu trí công nghệ sinh tử để phơi bày sự thật trước ánh sáng."
    ])
    
    print("Uploading novel_editor.php helper to server...")
    novel_editor.upload_helper()
    
    print(f"Updating Story 2227 metadata...")
    meta_res = novel_editor.update_story_meta(STORY_ID, title=title, intro=intro)
    print("Metadata update result:", meta_res)
    
    # 2. Update Chapters
    chapters_data = [
        {"id": 2229, "title": "Chương 1: Sương Mù Trên Đỉnh Langbiang", "sentences": ch1_sentences},
        {"id": 2230, "title": "Chương 2: Ái Nữ Tập Đoàn Và Lời Thỉnh Cầu", "sentences": ch2_sentences},
        {"id": 2231, "title": "Chương 3: Thuật Toán Trong Rừng Thông", "sentences": ch3_sentences},
        {"id": 2232, "title": "Chương 4: Sát Thủ Mạng Tấn Công", "sentences": ch4_sentences},
        {"id": 2233, "title": "Chương 5: Khủng Hoảng Đóng Băng Tài Khoản", "sentences": ch5_sentences},
        {"id": 2234, "title": "Chương 6: Bằng Chứng Thép Và Cuộc Gọi C03", "sentences": ch6_sentences},
        {"id": 2235, "title": "Chương 7: Buổi Sáng Hồ Xuân Hương", "sentences": ch7_sentences},
        {"id": 2236, "title": "Chương 8: Lời Hứa Dưới Rừng Thông", "sentences": ch8_sentences}
    ]
    
    for ch in chapters_data:
        c_id = ch["id"]
        c_title = ch["title"]
        c_content = format_paragraphs(ch["sentences"])
        word_count = len(c_content.split())
        
        print(f"Updating Chapter {c_id} - '{c_title}' (~{word_count} words)...")
        res = novel_editor.update_chapter(c_id, title=c_title, content=c_content)
        print("Result:", res)
        time.sleep(1)
        
    novel_editor.remove_helper()
    print("✓ Successfully deleted helper from server.")
    
    # 3. Generate and upload a beautiful textless cover image
    cover_prompt = "masterpiece, high quality anime illustration, gorgeous foggy pine forest in Da Lat Vietnam, a cool young programmer guy looking at a laptop inside a cozy warm wooden villa, soft sunlight filtering through the window, textless, no logos, no frames"
    print("\nGenerating and setting cover image...")
    cover_success = upload_cover_local.set_cover_via_local_upload(STORY_ID, cover_prompt)
    print("Cover upload success:", cover_success)
    
    print("\n🎉 Story 2227 successfully published with strict V12 formatting!")

if __name__ == "__main__":
    main()
