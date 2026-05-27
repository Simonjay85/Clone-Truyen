# -*- coding: utf-8 -*-
import json
import os
import urllib.parse
import requests

def build_and_publish_novel():
    title = "Vương Quốc Tổ Yến Khánh Hòa: Kỹ Sư Hoang Đảo Bị Cướp Bản Quyền, Lật Kèo Thâu Tóm Tập Đoàn Gian Thương Trăm Tỷ"
    author = "Antigravity"
    genre = "Sảng Văn / Vả Mặt"
    
    intro = (
        "<p><strong>\"Một thằng kỹ sư hoang đảo chân lấm tay bùn, suốt ngày ngửi mùi phân yến tanh tao như mày mà cũng đòi mơ tưởng bước chân vào hào môn Vạn Phát sao? Ký đơn từ chức rồi cút khỏi Khánh Hòa ngay lập tức!\"</strong></p>\n"
        "<p>Lời tuyên bố tàn nhẫn của Nguyễn Khánh Linh – ái nữ kiêu ngạo của Tập đoàn Yến Sào Hoàng Gia – vang lên giữa trời giông bão tại vách đá hoang sơ đảo Hòn Nội. Đứng cạnh cô ta, gã COO hách dịch Trần Thế Hùng ném thẳng tập hồ sơ bằng sáng chế bị cướp trắng của Trần Lâm Phong xuống vũng nước mặn nhơ nhớp. Bọn họ vu khống anh làm rò rỉ bí mật công nghệ, phong tỏa tài khoản Vietcombank, tước đoạt toàn bộ công trình nghiên cứu hệ thống làm sạch sợi yến bằng chùm siêu âm tần số thấp mà anh đã dành 5 năm ròng rã dầm mưa dãi nắng để phát triển.</p>\n"
        "<p>Thế nhưng, liên minh phản bội ấy không hề biết rằng, công thức sinh học bị cướp đi thực chất chỉ là một bản nháp có lỗi chí mạng. Nếu thiếu đi chủng men vi sinh phân lập độc quyền từ hang đá trầm tích tự nhiên do Lâm Phong nắm giữ, toàn bộ tổ yến được tẩy trắng bằng hóa chất công nghiệp của bọn họ sẽ sinh ra độc tố mycotoxin cực mạnh, trực tiếp tàn phá tế bào gan thận của người sử dụng.</p>\n"
        "<p>Được sự bảo trợ tài chính lý tính từ Lê Gia Hân – nữ CEO sòng phẳng, kiêu sa của Đông Á Group, Trần Lâm Phong bắt đầu cuộc phản kích nghẹt thở. Từ những mẻ yến sào hữu cơ thịt trắng muốt đạt chuẩn FDA Hoa Kỳ, nhật ký commit Git của hệ thống giám sát hang yến IoT, bản kiểm toán Big 4, đến sắc lệnh C03 bắt giữ kẻ gian thương... Từng kẻ chà đạp lên lòng tự trọng của anh sẽ phải quỳ gối, đầu gối bủn rủn rỉ máu trên nền bê tông lạnh giá để trả giá cho sự kiêu ngạo vô bờ bến của mình!</p>"
    )
    
    cover_prompt = (
        "A highly detailed, professional anime-style webnovel book cover, 1:1 ratio, without any text. "
        "A handsome, determined young Vietnamese man with a smart expression stands on a rocky island cliff in Khanh Hoa, "
        "overlooking the beautiful blue sea under a magnificent golden hour sunset. Next to him is an elegant, "
        "highly professional Vietnamese woman with long dark hair, wearing a sleek luxury business suit. "
        "In the background, beautiful wild swallows flying near natural stone cliffs, modern high-tech nesting structures, "
        "hyper-realistic, dynamic lighting, cinematic composition."
    )
    
    chapters = []
    
    # ------------------ CHAPTER 1 ------------------
    ch1_content = (
        "<p>Trời đổ mưa giông tầm tã trên vùng biển đảo Hòn Nội, Khánh Hòa. Những đợt sóng bạc đầu hung hãn gào thét, vỗ liên hồi vào các vách đá dựng đứng của hoang đảo, tạo nên những âm thanh ầm ĩ đầy căng thẳng. Trần Lâm Phong đứng lặng trong căn nhà gỗ nhỏ dựng sát mép đá, ánh mắt mệt mỏi nhưng kiên nghị dõi theo mẻ tổ yến tinh chế cuối cùng đang được xử lý trong bể thủy tinh chứa luồng sóng siêu âm tần số thấp.</p>"
        "<p>Suốt năm năm qua, anh đã dầm mưa dãi nắng khắp các hang đá hoang sơ trên các đảo yến ngoài khơi Nha Trang. Lâm Phong tự mình lội nước mặn, chịu đựng mùi phân yến tanh nồng trong lòng hang tối tăm để tìm ra giải pháp tối ưu cho quy trình làm sạch tổ yến bằng công nghệ sinh học tuần hoàn kết hợp chùm siêu âm tần số thấp. Công trình này không chỉ giúp tổ yến giữ nguyên vẹn cấu trúc sợi yến quý giá mà còn loại bỏ hoàn toàn các loại vi khuẩn độc hại mà không cần dùng đến một giọt hóa chất tẩy trắng công nghiệp nào.</p>"
        "<p>Cánh cửa căn nhà gỗ đột ngột bị đẩy mạnh ra dưới sức gió bão. Nguyễn Khánh Linh – vị hôn thê kiêu ngạo của anh, đồng thời là ái nữ duy nhất của Chủ tịch Tập đoàn Yến Sào Hoàng Gia – bước vào với đôi giày cao gót màu đỏ gõ lộp cộp trên sàn gỗ ẩm ướt. Đi bên cạnh cô ta là Trần Thế Hùng, gã COO mới được tuyển về từ một tập đoàn đa quốc gia, khoác trên mình bộ vest ba mảnh thẳng thướm bất chấp thời tiết giông bão, trên môi luôn thường trực một nụ cười khinh khỉnh vô cùng chướng mắt.</p>"
        "<p>\"Trần Lâm Phong, anh dừng tay lại đi.\" Giọng Linh sắc lẹm, lạnh lùng cắt ngang tiếng gió gào thét bên ngoài.</p>"
        "<p>Lâm Phong đặt thiết bị đo tần số sóng siêu âm xuống giá đỡ, quay lại nhìn cô: \"Linh, mẻ yến tinh chế này đang ở giai đoạn quyết định. Có chuyện gì quan trọng để lát nữa tàu về đất liền rồi nói được không?\"</p>"
        "<p>\"Không có lát nữa nào cả.\" Trần Thế Hùng bước lên trước một bước, rút từ trong túi da ra một tập văn bản có đóng dấu đỏ của Tập đoàn Hoàng Gia và ném thẳng lên bàn làm việc chứa đầy dụng cụ thí nghiệm của Lâm Phong. \"Trần Lâm Phong, từ giây phút này, anh chính thức bị sa thải khỏi Tập đoàn Yến Sào Hoàng Gia vì hành vi cố ý rò rỉ bí mật công nghệ ra bên ngoài.\"</p>"
        "<p>Lâm Phong nheo mắt nhìn tập văn bản sa thải, rồi ngước lên nhìn thẳng vào mắt Linh: \"Rò rỉ bí mật công nghệ? Linh, em thừa biết toàn bộ công nghệ siêu âm tuần hoàn này là do một tay anh nghiên cứu và phát triển suốt năm năm qua dưới trạm nghiên cứu đảo yến này. Anh rò rỉ cho ai?\"</p>"
        "<p>Linh khoanh tay trước ngực, ánh mắt khinh miệt lướt qua bộ quần áo bảo hộ lao động dính đầy vết rêu bẩn và mùi phân yến của Lâm Phong. Cô ta bĩu môi đầy chán ghét: \"Một thằng kỹ sư hoang đảo chân lấm tay bùn, suốt ngày ngửi mùi phân yến tanh tao như mày mà cũng đòi mơ tưởng bước chân vào hào môn Vạn Phát sao? Sự tồn tại của mày trong tập đoàn chỉ là một vết nhơ. Tao và anh Hùng đã nộp đơn đăng ký bảo hộ độc quyền cho công nghệ làm sạch siêu âm này dưới tên của chúng tao lên Cục Sở hữu Trí tuệ từ sáng nay rồi.\"</p>"
        "<p>\"Bọn em... cướp trắng công trình của anh?\" Lâm Phong cười khẩy, nhưng trong lòng trào dâng một luồng phẫn nộ tột cùng.</p>"
        "<p>Trần Thế Hùng cười nhạt, lấy tay chỉnh lại chiếc đồng hồ Rolex lấp lánh trên cổ tay: \"Cướp? Trong hợp đồng nghiên cứu của anh có điều khoản rõ ràng: mọi phát minh trong thời gian làm việc đều thuộc sở hữu của tập đoàn. Bọn tôi chỉ hợp thức hóa nó trên giấy tờ để chuẩn bị cho thương vụ IPO nghìn tỷ sắp tới của Hoàng Gia. Còn anh, một kẻ nghèo hèn rách nát, tốt nhất là ký vào đơn từ chức này rồi cút khỏi Khánh Hòa ngay lập tức.\"</p>"
        "<p>\"Nếu tôi không ký thì sao?\" Lâm Phong trầm giọng.</p>"
        "<p>Linh tiến lại gần, ghé sát vào tai Lâm Phong, giọng nói tràn đầy sự đe dọa tàn nhẫn: \"Nếu anh không ký, tài khoản Vietcombank của anh sẽ bị đóng băng vĩnh viễn vì nghi án giao dịch bất hợp pháp. Đừng quên gia tộc họ Nguyễn của tao có mối quan hệ sâu sắc thế nào với giới tài chính ở đất Nha Trang này. Và tao cũng đã gửi thông báo blacklist đến tất cả các doanh nghiệp yến sào lớn nhỏ ở khu vực miền Trung. Anh sẽ không tìm nổi một công việc rửa hang yến ở cái đất Khánh Hòa này đâu!\"</p>"
        "<p>Dứt lời, Hùng vung tay gạt phăng bể thủy tinh chứa mẻ yến tinh chế siêu âm trên bàn. Bể thủy tinh rơi xuống sàn nhà, vỡ tan tành, những sợi yến trắng muốt trôi nổi trong làn nước nhầy nhụa loang lổ khắp nơi. Linh và Hùng cười lớn, quay lưng bước ra khỏi nhà gỗ, bước lên chiếc tàu cao tốc đang chờ sẵn ở cầu cảng, bỏ lại Lâm Phong đứng một mình giữa những mảnh vỡ thủy tinh và tiếng mưa giông gào thét ngoài biển đảo Hòn Nội.</p>"
        "<p>Lâm Phong từ từ ngồi xuống, nhặt một mảnh vỡ thủy tinh lên. Ngón tay anh bị cạnh sắc cứa vào, rỉ ra một giọt máu đỏ tươi. Anh nhìn giọt máu trên ngón tay, đôi mắt chìm vào bóng tối sâu thẳm. Bọn họ nghĩ rằng họ đã thắng? Bọn họ nghĩ rằng công thức sinh học dễ dàng bị cướp đoạt như vậy?</p>"
        "<p>Lâm Phong khẽ thì thầm trong tiếng sóng gào thét của biển khơi: \"Nguyễn Khánh Linh, Trần Thế Hùng... Các người không biết mình vừa cướp đi một quả bom nổ chậm đâu.\"</p>"
    )
    chapters.append({"title": "Chương 1: Đêm Giông Bão Trên Đảo Hòn Nội", "content": ch1_content})
    
    # ------------------ CHAPTER 2 ------------------
    ch2_content = (
        "<p>Dưới cơn mưa tầm tã của thành phố Nha Trang, Trần Lâm Phong lặng lẽ ngồi trong một góc khuất của quán cà phê gỗ nhỏ bên bờ kè đường Trần Phú. Anh đã cởi bỏ bộ quần áo bảo hộ lao động tanh mùi phân yến, thay bằng chiếc áo thun đen giản dị và chiếc quần jean sờn màu. Trước mặt anh là chiếc laptop ThinkPad cũ kỹ, màn hình đang hiển thị những dòng mã nguồn của hệ thống giám sát môi trường hang yến IoT do chính anh viết từ ba năm trước.</p>"
        "<p>Lâm Phong vuốt màn hình điện thoại. Đúng như Linh đe dọa, tài khoản Vietcombank của anh đã bị tạm khóa với lý do \"xác minh nguồn tiền giao dịch bất thường\". Toàn bộ số dư hơn hai trăm triệu đồng tích cóp từ lương kỹ sư bị phong tỏa hoàn toàn. Anh mỉm cười lạnh lẽo. Gia tộc họ Nguyễn quả thực ra tay rất nhanh và tàn nhẫn, dồn anh vào con đường tuyệt lộ không một xu dính túi.</p>"
        "<p>\"Trần Lâm Phong?\" Một giọng nói trong trẻo, mang theo sự lý tính và uy nghiêm cực kỳ đặc biệt vang lên bên tai anh.</p>"
        "<p>Lâm Phong ngẩng đầu lên. Đứng trước mặt anh là một người phụ nữ trẻ vô cùng xinh đẹp và sang trọng. Cô mặc một bộ suit công sở màu xanh navy may đo thủ công hoàn hảo, ôm sát vóc dáng cao ráo thanh mảnh. Mái tóc dài đen mượt được thả tự nhiên qua bờ vai, để lộ khuôn mặt thanh tú với đôi mắt sắc sảo và cặp kính gọng mảnh toát lên vẻ trí thức đầy kiêu sa. Cô chính là Lê Gia Hân – Giám đốc Đầu tư (CFO) kiêm Trưởng ban Đầu tư của Tập đoàn Dược phẩm & Nghỉ dưỡng Đông Á nổi tiếng.</p>"
        "<p>\"Chào cô Lê.\" Lâm Phong đứng dậy, lịch sự kéo ghế cho cô. \"Tôi không ngờ cô lại đến sớm thế giữa trời mưa bão này.\"</p>"
        "<p>Gia Hân ngồi xuống, đặt chiếc túi xách Hermes đắt tiền lên bàn một cách sòng phẳng, rồi nhìn thẳng vào mắt Lâm Phong: \"Đông Á Group luôn tôn trọng thời gian và giá trị thực sự. Tôi đã đọc qua tài liệu sơ bộ về công nghệ tinh chế yến sào bằng siêu âm của anh gửi qua email. Nhưng trước khi chúng ta bàn về con số đầu tư trăm tỷ, tôi cần anh chứng minh hai điều: năng lực thực sự và tính pháp lý của phát minh này.\"</p>"
        "<p>Lâm Phong gật đầu, xoay chiếc laptop ThinkPad về phía cô: \"Tôi biết Tập đoàn Vạn Phát đã nộp đơn đăng ký bảo hộ độc quyền sáng chế này dưới tên Nguyễn Khánh Linh và Trần Thế Hùng từ sáng nay. Nhưng họ không biết một điều. Hệ thống quản lý cốt lõi của công nghệ chùm siêu âm này được tích hợp chặt chẽ với phần mềm giám sát hang yến tự động. Và toàn bộ mã nguồn của phần mềm đó được tôi lưu trữ trên hệ thống Git cá nhân.\"</p>"
        "<p>Ngón tay Lâm Phong gõ nhanh trên bàn phím, mở ra nhật ký commit Git (Git commit history): \"Cô Gia Hân, hãy nhìn vào đây. Từng dòng code, từng thuật toán điều chỉnh tần số sóng siêu âm, từng mốc thời gian tối ưu hóa chỉ số nước làm sạch đều được ghi lại bất biến với timestamp từ năm năm trước cho đến ngày hôm qua dưới tài khoản cá nhân của tôi. Bằng chứng số này có giá trị pháp lý tuyệt đối trước tòa án sở hữu trí tuệ quốc tế. Vạn Phát chỉ cướp được bản tài liệu giấy cứng thô sơ, nhưng họ không có mã nguồn gốc và lịch sử phát triển bất biến này.\"</p>"
        "<p>Gia Hân nheo mắt nhìn kỹ những dòng commit trên màn hình. Cô lật giở những tài liệu kiểm định kỹ thuật trên iPad của mình, đối chiếu các mốc thời gian một cách vô cùng cẩn trọng. Sau năm phút im lặng nghẹt thở, cô ngẩng đầu lên, ánh mắt sắc sảo lộ ra vẻ tán thưởng không hề che giấu.</p>"
        "<p>\"Tuyệt vời.\" Gia Hân đẩy gọng kính, giọng nói vô cùng dứt khoát. \"Bằng chứng số từ Git và timestamp này hoàn toàn đủ để chúng ta khởi kiện tranh chấp quyền sở hữu trí tuệ và vô hiệu hóa đơn đăng ký của Vạn Phát. Trần Lâm Phong, anh không chỉ là một kỹ sư sinh học giỏi, anh còn là một người có tư duy bảo mật hệ thống cực kỳ xuất sắc. Đông Á Group sẵn sàng hợp tác với anh để xây dựng một đế chế yến sào hữu cơ mới, nghiền nát Vạn Phát trên chính mảnh đất Khánh Hòa này.\""
    )
    chapters.append({"title": "Chương 2: Mỏ Neo Pháp Lý Và Mỹ Nhân Hào Môn", "content": ch2_content})
    
    # ------------------ CHAPTER 3 ------------------
    ch3_content = (
        "<p>Lê Gia Hân là một nữ tổng tài vô cùng lý tính và sòng phẳng. Ngay sau cuộc gặp ở quán cà phê, cô không hề ký hợp đồng một cách vội vã theo cảm tính. Suốt ba ngày tiếp theo, cô đã cử một đội ngũ gồm sáu luật sư hàng đầu về sở hữu trí tuệ và hai chuyên gia thẩm định công nghệ sinh học từ TP.HCM xuống tận Nha Trang để thực hiện quy trình thẩm định pháp lý (due diligence) cực kỳ nghiêm ngặt đối với công trình của Trần Lâm Phong.</p>"
        "<p>Lâm Phong hoàn toàn hợp tác, cung cấp mọi dữ liệu thô, các mẫu men nấm được lưu trữ bí mật trong phòng lab cá nhân của mình, cùng nhật ký thực nghiệm chi tiết suốt năm năm qua. Đội ngũ của Gia Hân làm việc liên tục ngày đêm, kiểm tra từng chi tiết nhỏ nhất để đảm bảo không có bất kỳ rủi ro pháp lý hay kỹ thuật nào trước khi dòng tiền lớn được giải ngân.</p>"
        "<p>Chiều thứ Sáu, tại văn phòng đại diện của Đông Á Group ở thành phố Nha Trang, Gia Hân đặt bản báo cáo thẩm định dày cộp lên bàn. Cô nhìn Lâm Phong, đôi môi đỏ mọng khẽ nở một nụ cười thỏa mãn: \"Mọi thứ hoàn hảo. Báo cáo kiểm định độc lập chứng minh quy trình chùm siêu âm của anh có khả năng loại bỏ hoàn toàn tạp chất trong sợi yến mà không làm gãy cấu trúc tự nhiên của nó. Hợp đồng đã được soạn xong. Đông Á Group sẽ rót ba trăm tỷ đồng vào công ty mới của anh – Khánh Hòa Premium Nest – để xây dựng chuỗi hang yến công nghệ cao và nhà máy chế biến đạt chuẩn FDA Hoa Kỳ.\"</p>"
        "<p>Lâm Phong cầm cây bút lên, ký tên mình vào bản hợp đồng một cách dứt khoát. Ba trăm tỷ đồng – một con số khổng lồ đủ để xoay chuyển toàn bộ cục diện yến sào miền Trung. Anh nhìn Gia Hân, chân thành nói: \"Cảm ơn sự tin tưởng của cô, Gia Hân.\"</p>"
        "<p>\"Tôi đầu tư vào anh vì lợi nhuận và sự sòng phẳng, không phải vì từ thiện.\" Gia Hân nói, ánh mắt kiêu sa nhưng vô cùng nghiêm túc. \"Tuy nhiên, tôi rất tôn trọng những người có tài năng và lòng tự trọng bị chà đạp. Hãy dùng ba trăm tỷ này để chứng minh cho gia tộc họ Nguyễn thấy, ai mới là vua thực sự của ngành yến sào Việt Nam này.\"</p>"
        "<p>Sau khi ký hợp đồng, hai người cùng nhau bước ra ban công văn phòng. Trời chiều Nha Trang nhuộm một màu vàng đỏ rực rỡ phía chân trời, ánh hoàng hôn hắt lên mặt biển phẳng lặng lấp lánh như dát vàng. Gió biển thổi mát rượi, cuốn đi những lo âu của những ngày qua.</p>"
        "<p>Gia Hân nhìn biển xanh uốn lượn, khẽ thở dài: \"Bách này... à không, Lâm Phong này, anh có biết tại sao tôi lại quyết định nhanh như vậy không? Ông nội tôi – người sáng lập Đông Á Group – luôn dạy rằng, trong kinh doanh, tài sản lớn nhất không phải là tiền, mà là lòng tin vào con người. Khi tôi nhìn thấy anh đứng trước sóng gió đảo Hòn Nội mà ánh mắt vẫn kiên định, tôi biết anh chính là người có thể vực dậy cả ngành xuất khẩu tổ yến Việt Nam đang bị các thế lực gian thương bóp nghẹt.\"</p>"
        "<p>Lâm Phong nhìn góc nghiêng thanh tú của cô dưới ánh hoàng hôn, lòng dấy lên một cảm xúc ấm áp khó tả: \"Tôi sẽ không làm cô và ông cụ thất vọng. Mọi tổ yến của Khánh Hòa Premium Nest sẽ là minh chứng cho sự thật và tri thức.\""
    )
    chapters.append({"title": "Chương 3: Hợp Đồng Trăm Tỷ Lý Tính", "content": ch3_content})
    
    # ------------------ CHAPTER 4 ------------------
    ch4_content = (
        "<p>Trong khi Trần Lâm Phong và Lê Gia Hân đang âm thầm xây dựng hệ thống hang yến công nghệ cao, thì tại trụ sở chính của Tập đoàn Hoàng Gia, bầu không khí lại tràn ngập sự hân hoan và kiêu ngạo tột cùng. Nguyễn Khánh Linh và Trần Thế Hùng đã sử dụng công thức men làm sạch cướp được từ Lâm Phong để sản xuất hàng loạt mẻ tổ yến làm sạch siêu tốc mang tên \"Hoàng Gia Gold Nest\".</p>"
        "<p>Hùng, với bản tính hống hách và thích thể hiện, đã liên tục tổ chức các buổi họp báo hoành tráng, xuất hiện trên các chương trình livestream tài chính để quảng bá về \"phát minh thế kỷ\" của mình. Hắn lớn tiếng tuyên bố Hoàng Gia là doanh nghiệp đầu tiên tại Việt Nam làm chủ hoàn toàn công nghệ chế biến yến sào tinh khiết, nâng tầm giá trị thương hiệu lên mức nghìn tỷ đồng trước ngày IPO trên sàn HoSE.</p>"
        "<p>Nhờ chiến dịch truyền thông bẩn bôi nhọ Lâm Phong và thổi phồng công nghệ mới, Hoàng Gia đã nhanh chóng thu hút được sự chú ý của Apex Global – một trong những tập đoàn bán lẻ lớn nhất của Mỹ chuyên nhập khẩu thực phẩm cao cấp. Trần Thế Hùng đã đích thân bay sang Singapore để ký kết một hợp đồng nguyên tắc trị giá 50 triệu USD (khoảng 1.200 tỷ đồng) với đối tác Mỹ để xuất khẩu tổ yến hữu cơ.</p>"
        "<p>\"Nhìn xem, Trần Lâm Phong!\" Nguyễn Khánh Linh cầm ly rượu vang đỏ, đứng trước màn hình lớn đang chiếu trực tiếp buổi lễ ký kết tại Singapore, cười lớn đầy đắc thắng. \"Không có mày, Hoàng Gia vẫn cất cánh. Một thằng kỹ sư quèn như mày bây giờ chắc đang phải lội bùn thuê ở xó xỉnh nào đó để kiếm sống qua ngày.\"</p>"
        "<p>Thế nhưng, Trần Thế Hùng trong cơn say chiến thắng đã phạm phải một sai lầm chí mạng. Để cắt giảm chi phí sản xuất nhằm làm đẹp sổ sách kế toán cho đợt IPO sắp tới, hắn đã âm thầm thay thế các nguyên liệu lên men tự nhiên đắt tiền bằng các hóa chất công nghiệp giá rẻ. Hơn thế nữa, mẻ công thức mà họ cướp từ Lâm Phong thực chất chỉ là một bản nháp thô sơ.</p>"
        "<p>Họ hoàn toàn không biết rằng, để chủng men vi sinh hoạt động ổn định và không bị đột biến sinh độc tố trong môi trường thực tế, cần phải có chủng men vi sinh hoang dã phân lập độc quyền từ hang đá trầm tích tự nhiên của Lâm Phong để cấy ghép vào giai đoạn cuối của quy trình lên men.</p>"
        "<p>Không có chủng men đặc chủng này, các tế bào men vi sinh trong yến sào Hoàng Gia sẽ bị đột biến gen sau 20 ngày sử dụng dưới tác động của nhiệt độ và độ ẩm. Khi tế bào men đột biến, chúng sẽ ngừng hỗ trợ loại bỏ tạp chất, ngược lại sẽ giải phóng ra một lượng lớn độc tố mycotoxin cực mạnh, trực tiếp phá hủy tế bào gan và mật của con người.</p>"
        "<p>Để che giấu dấu hiệu sớm của tạp chất và làm trắng yến siêu tốc nhằm vượt qua các kỳ kiểm tra định kỳ của cơ quan chức năng, Hùng đã chỉ đạo cấp dưới bí mật sử dụng một lượng lớn chất tẩy trắng hóa học cực độc (Hydrogen Peroxide nồng độ cao) bơm thẳng vào các bể ngâm yến. Hắn nghĩ rằng quy trình xả nước sẽ cuốn trôi mọi dấu vết hóa chất, nhưng hắn không biết mình đang tự tay chôn vùi toàn bộ tập đoàn nghìn tỷ của gia đình vị hôn thê kiêu ngạo.</p>"
    )
    chapters.append({"title": "Chương 4: Quả Bom Hóa Chất Của Kẻ Cướp", "content": ch4_content})
    
    # ------------------ CHAPTER 5 ------------------
    ch5_content = (
        "<p>Cuộc chiến thương trường không bao giờ là một đường thẳng dễ dàng. Khi vùng khai thác yến sào hữu cơ \"Khánh Hòa Premium Nest\" của Lâm Phong bắt đầu đi vào vận hành ổn định và chuẩn bị thu hoạch lứa yến đầu tiên, Tập đoàn Hoàng Gia đã tung ra đòn tấn công bẩn tàn khốc nhất.</p>"
        "<p>Trần Thế Hùng đã sử dụng số tiền khổng lồ từ các quỹ đen để mua chuộc một nhóm thanh tra biến chất của Chi cục Vệ sinh An toàn Thực phẩm địa phương. Sáng sớm thứ Hai, một đoàn thanh tra đột xuất gồm mười người ập vào xưởng sơ chế của Premium Nest. Họ đưa ra một biên bản kiểm tra sơ sài cáo buộc hệ thống xử lý nước của Lâm Phong vi phạm nghiêm trọng quy chuẩn an toàn, lập tức ra quyết định tạm đình chỉ hoạt động toàn bộ vùng sản xuất trong vòng 24 giờ để tiến hành thanh tra toàn diện.</p>"
        "<p>Cùng lúc đó, trên mạng xã hội và các trang tin tức lá cải bùng phát một chiến dịch truyền thông bẩn được chuẩn bị kỹ lưỡng. Hàng loạt tài khoản ảo và các trang mạng xã hội lớn đồng loạt chia sẻ những thông tin giả mạo, hình ảnh cắt ghép cáo buộc yến sào hữu cơ của Premium Nest sử dụng hóa chất tẩy rửa độc hại. Trên các buổi livestream bán hàng trực tiếp của các đại lý, các troller liên tục spam những bình luận tiêu cực bôi nhọ danh tiếng thương hiệu mới của Lâm Phong.</p>"
        "<p>Chưa dừng lại ở đó, gã anh rể kết nghĩa của Hùng tại ngân hàng tiếp tục gây áp lực, khiến tài khoản cá nhân Vietcombank của Lâm Phong vẫn bị khóa chặt dù luật sư của Đông Á Group đã can thiệp. Lâm Phong rơi vào tình cảnh vô cùng bế tắc: doanh nghiệp bị đình chỉ hoạt động 24 giờ, vùng sản xuất đối mặt nguy cơ trễ hạn giao hàng cho đối tác, truyền thông bẩn bủa vây khắp nơi.</p>"
        "<p>\"Lâm Phong, tình hình đang rất căng thẳng.\" Gia Hân gọi điện cho anh, giọng cô dù vẫn lý tính nhưng không giấu nổi sự lo lắng. \"Hội đồng quản trị của Đông Á Group đang chịu áp lực lớn từ các cổ đông sáng lập. Nếu trong vòng 24 giờ tới chúng ta không dỡ bỏ được lệnh đình chỉ và đập tan tin đồn bẩn này, họ sẽ bỏ phiếu phong tỏa nguồn vốn đầu tư ba trăm tỷ của chúng ta.\"</p>"
        "<p>Lâm Phong đứng trước khu hang yến công nghệ cao, nhìn những làn nước trong vắt được tuần hoàn bằng công nghệ sinh học, gương mặt anh vẫn bình thản đến lạ lùng. Anh khẽ vuốt lại mái tóc ướt đẫm nước biển, giọng nói điềm tĩnh nhưng tràn đầy sức mạnh thép: \"Gia Hân, hãy tin tôi. Sự bế tắc này chỉ là cái bẫy mà tôi chủ động để họ giăng ra. Khi kẻ thù nghĩ rằng họ đã đẩy chúng ta vào đường cùng và bộc lộ toàn bộ những quân bài bẩn thỉu nhất, chính là lúc họ tự tay ký vào bản án tử hình của chính mình. Hãy chuẩn bị cho tôi một buổi họp báo công nghệ trực tiếp vào sáng mai. Tôi sẽ lật ngược thế cờ ngay trước mặt toàn bộ giới truyền thông Khánh Hòa.\"</p>"
    )
    chapters.append({"title": "Chương 5: Vòng Vây Bế Tắc", "content": ch5_content})
    
    # ------------------ CHAPTER 6 ------------------
    ch6_content = (
        "<p>Giữa lúc cuộc khủng hoảng truyền thông bẩn đang ở đỉnh điểm căng thẳng, một sự kiện bất ngờ đã xảy ra tại buổi tiệc chiêu đãi cấp cao của Hiệp hội Yến Sào miền Trung tổ chức tại khách sạn Sheraton Nha Trang. Tham dự buổi tiệc có rất nhiều chính khách, doanh nhân lớn và đặc biệt là ông Lê Huy Hoàng – người sáng lập Đông Á Group, đồng thời là ông nội của Lê Gia Hân. Ông Hoàng năm nay đã ngoài tám mươi, là một huyền thoại sống trong giới kinh doanh Việt Nam.</p>"
        "<p>Tại buổi tiệc, Tập đoàn Hoàng Gia đã tự hào tài trợ toàn bộ thực đơn tráng miệng bằng sản phẩm tổ yến chưng đường phèn \"Hoàng Gia Gold Nest\" để chứng tỏ đẳng cấp. Thế nhưng, chỉ ba mươi phút sau khi dùng món yến chưng của Hoàng Gia, ông Lê Huy Hoàng đột ngột lên cơn co thắt vùng bụng dữ dội, mặt mày xám ngoét không còn giọt máu. Nhịp tim của ông tăng nhanh đột ngột, huyết áp tụt dốc không phanh, toàn thân run rẩy rồi ngã gục ngay trên bàn tiệc trước sự hoảng loạn tột độ của Gia Hân và hàng trăm khách mời.</p>"
        "<p>Mọi người lập tức gọi xe cấp cứu, nhưng bác sĩ riêng của ông Hoàng đi cùng đoàn kiểm tra nhanh và lắc đầu đầy bất lực: \"Ông cụ bị ngộ độc cấp tính bởi độc chất hóa học cực mạnh, dẫn đến suy gan cấp và có dấu hiệu trụy mạch. Khoảng cách đến bệnh viện đa khoa Nha Trang quá xa, nếu không thể ổn định nhịp tim và trung hòa bớt độc tố trong vòng ba mươi phút tới, ông cụ sẽ không qua khỏi!\"</p>"
        "<p>Trong lúc mọi người đang tuyệt vọng khóc than, Lâm Phong bước tới trước chiếc giường tạm của ông cụ. Anh rút từ trong túi áo ra một lọ thủy tinh nhỏ chứa chất lỏng màu nâu sẫm – đây là chiết xuất enzym thảo dược đặc chủng phân lập từ nhân sâm đá và xuyên tâm liên hoang dã của vùng núi Thất Sơn mà anh luôn mang theo bên mình.</p>"
        "<p>\"Hãy để tôi thử.\" Lâm Phong nói, giọng điềm tĩnh nhưng vô cùng chắc chắn. \"Đây là enzym thảo dược Đông y có khả năng trung hòa cực nhanh các gốc tự do và độc tố mycotoxin tồn dư từ yến sào độc hại.\"</p>"
        "<p>\"Mày định dùng thuốc nam vô căn cứ để hại chết ông cụ sao?\" Trần Thế Hùng đứng cạnh đó hét lớn để thực hiện mưu đồ bôi nhọ của mình.</p>"
        "<p>\"Câm miệng!\" Gia Hân quay phắt lại, đôi mắt đỏ ngầu gầm lên một tiếng đầy uy lực khiến Hùng câm bặt. Cô nhìn thẳng vào mắt Lâm Phong, nhìn thấy sự tự tin tuyệt đối của người kỹ sư tri thức, rồi gật đầu dứt khoát: \"Lâm Phong, cứu ông nội tôi! Tôi chịu mọi trách nhiệm!\"</p>"
        "<p>Lâm Phong đỡ đầu ông cụ lên, nhẹ nhàng nhỏ từng giọt chiết xuất enzym thảo dược vào miệng ông. Chỉ năm phút sau khi dùng thuốc Đông y của Lâm Phong, nhịp tim của ông Hoàng đang từ 140 lần/phút bắt đầu từ từ hạ xuống mức ổn định 85 lần/phút. Hơi thở đứt quãng của ông trở nên sâu và đều đặn hơn, sắc mặt xám ngoét dần hồng hào trở lại trước sự kinh ngạc tột cùng của bác sĩ riêng và toàn bộ quan khách.</p>"
        "<p>Ngay sau đó, xe cấp cứu đưa ông Hoàng vào Bệnh viện Đa khoa Quốc tế Nha Trang. Tại đây, các bác sĩ Tây y hàng đầu đã tiến hành các xét nghiệm lâm sàng, chụp CT và xét nghiệm máu của ông cụ. Hai giờ sau, vị Trưởng khoa Hồi sức cấp cứu bước ra khỏi phòng bệnh, tay cầm bản kết quả xét nghiệm, gương mặt lộ rõ sự kinh ngạc tột độ.</p>"
        "<p>\"Thật kỳ diệu!\" Vị bác sĩ Tây y thốt lên đầy phấn khích. \"Kết quả xét nghiệm máu cho thấy bệnh nhân bị ngộ độc cực nặng bởi Hydrogen Peroxide và các gốc độc tố nấm men biến dị tồn dư trong món ăn. Tuy nhiên, một hoạt chất sinh học đặc biệt trong lọ thuốc thảo dược mà các vị sử dụng trước đó đã tạo ra một lớp màng bọc phân tử, trung hòa hoàn toàn độc tố và bảo vệ tế bào gan khỏi bị hoại tử. Đây là một kết quả lâm sàng phi thường mà y học hiện đại cũng khó lòng đạt được trong thời gian ngắn như vậy! Phương pháp kết hợp Đông - Tây y này đã thực sự giành lại mạng sống của ông cụ từ tay tử thần!\"</p>"
        "<p>Gia Hân nghe đến đây thì khuỵu xuống hàng ghế chờ của bệnh viện, nước mắt lăn dài trên má vì nhẹ nhõm. Cô nhìn Lâm Phong đang đứng lặng lẽ bên cửa sổ bệnh viện, lòng đầy sự kính phục và biết ơn vô hạn. Cô biết, người đàn ông này không chỉ nắm giữ tương lai của ngành yến sào, mà còn là ân nhân lớn nhất của cả gia tộc cô.</p>"
    )
    chapters.append({"title": "Chương 6: Đông - Tây Y Biện Chứng", "content": ch6_content})
    
    # ------------------ CHAPTER 7 ------------------
    ch7_content = (
        "<p>Thời gian 25 ngày định mệnh đã trôi qua kể từ khi Tập đoàn Hoàng Gia bắt đầu tung ra thị trường dòng sản phẩm yến sào \"Hoàng Gia Gold Nest\" độc hại. Đúng như những gì Trần Lâm Phong đã dự đoán chính xác về mặt sinh học, quả bom nổ chậm cuối cùng đã chính thức bùng nổ tàn khốc trên khắp cả nước.</p>"
        "<p>Sáng sớm thứ Ba, các bệnh viện lớn từ Nha Trang, Đà Nẵng đến TP.HCM đồng loạt tiếp nhận hàng trăm ca cấp cứu trong tình trạng suy gan thận cấp tính nghiêm trọng. Điểm chung duy nhất của tất cả các bệnh nhân này là họ đều đã sử dụng sản phẩm tổ yến chưng sẵn cao cấp của Hoàng Gia trong vòng hai tuần qua. Triệu chứng lâm sàng vô cùng kinh khủng: vàng da toàn thân, men gan tăng vọt gấp 50 lần mức bình thường, chức năng lọc của thận bị hủy hoại hoàn toàn.</p>"
        "<p>Mùi hôi thối của hóa chất và nước thải độc hại bốc lên nồng nặc từ khu nhà máy sản xuất của Hoàng Gia tại Nha Trang. Dù Trần Thế Hùng đã điên cuồng chỉ đạo công nhân đổ hàng tấn chất trung hòa xuống hệ thống xả thải để phi tang dấu vết, nhưng lượng hóa chất xả ra quá lớn đã khiến dòng nước ven biển quanh nhà máy nổi bọt trắng xóa, cá biển chết hàng loạt dạt vào bờ đá.</p>"
        "<p>Đúng lúc đó, một đoàn thanh tra liên ngành phối hợp cùng các chuyên gia của Viện Pasteur TP.HCM và đại diện FDA Hoa Kỳ tại Việt Nam đã bất ngờ ập vào kho hàng lớn nhất của Hoàng Gia. Họ tiến hành lấy mẫu kiểm tra ngẫu nhiên các lô yến sào chuẩn bị xuất khẩu.</p>"
        "<p>Kết quả giám định hóa học từ Viện Pasteur đóng dấu đỏ lập tức dội một gáo nước lạnh vào ban lãnh đạo Hoàng Gia: hàm lượng hóa chất tẩy trắng cực độc Hydrogen Peroxide tồn dư trong sợi yến vượt mức an toàn cho phép gấp 200 lần, cùng sự hiện diện của độc tố nấm men biến dị có khả năng gây ung thư cực mạnh. Sắc lệnh lập tức được ban hành: đình chỉ khẩn cấp mọi giấy phép xuất khẩu của Hoàng Gia, niêm phong toàn bộ hệ thống phân phối trên toàn quốc!</p>"
    )
    chapters.append({"title": "Chương 7: Sự Trừng Phạt Bùng Phát", "content": ch7_content})
    
    # ------------------ CHAPTER 8 ------------------
    ch8_content = (
        "<p>Tin dữ từ Viện Pasteur và phán quyết đình chỉ xuất khẩu của FDA Hoa Kỳ lập tức tạo nên một cơn địa chấn kinh hoàng càn quét khắp giới tài chính và thương mại Việt Nam. Chỉ trong vòng một giờ sau khi thông tin được công bố chính thức, tập đoàn bán lẻ khổng lồ Apex Global đã lập tức ra văn bản tuyên bộ hủy bỏ hoàn toàn hợp đồng nguyên tắc trị giá 50 triệu USD ký kết trước đó với Hoàng Gia, đồng thời đệ đơn kiện yêu cầu bồi thường thiệt hại danh dự lên tòa án thương mại quốc tế tại Singapore.</p>"
        "<p>Tại Sở Giao dịch Chứng khoán TP.HCM (HoSE), Ủy ban Chứng khoán Nhà nước đã ra sắc lệnh khẩn cấp đình chỉ vô thời hạn thương vụ IPO của Tập đoàn Hoàng Gia do phát hiện có dấu hiệu gian lận công nghệ, bôi đen báo cáo tài chính và gây ô nhiễm môi trường nghiêm trọng. Cổ phiếu của Hoàng Gia mất hoàn toàn thanh khoản, hàng chục ngàn nhà đầu tư hoảng loạn bao vây trụ sở tập đoàn tại Nha Trang để đòi lại tiền đặt cọc gọi vốn.</p>"
        "<p>Trần Thế Hùng và Nguyễn Khánh Linh ngồi trong phòng làm việc của Chủ tịch, gương mặt xám ngoét không còn một giọt máu. Các ngân hàng lớn đồng loạt ra quyết định đóng băng tạm thời toàn bộ tài khoản Vietcombank và Agribank của Hoàng Gia để thu hồi nợ xấu. Hàng trăm thương lái và nông dân liên kết đứng nghẹn ngoài cổng tập đoàn, gào thét đòi thanh toán tiền nợ.</p>"
        "<p>\"Hùng... chúng ta phải làm sao đây?\" Linh run rẩy hỏi, nước mắt giàn giụa làm nhòe nhoẹt lớp trang điểm đắt tiền. \"Tất cả tài sản của gia đình tao đều đã thế chấp cho ngân hàng để đầu tư vào dự án này rồi. Nếu không thể IPO, nhà tao sẽ phá sản mất!\"</p>"
        "<p>Hùng không đáp. Gã COO hống hách ngày nào giờ đây ngồi sụp dưới gầm bàn, hai tay ôm đầu, mồ hôi lạnh chảy ròng ròng ướt đẫm cả chiếc áo sơ mi hiệu Armani đắt tiền. Hắn biết rõ hơn ai hết, khoản nợ Ponzi và các hóa đơn hóa chất bẩn đứng tên hắn sẽ sớm đưa hắn vào sau song sắt nhà giam.</p>"
    )
    chapters.append({"title": "Chương 8: Cú Sụp Đổ Của Đế Chế Giấy", "content": ch8_content})
    
    # ------------------ CHAPTER 9 ------------------
    ch9_content = (
        "<p>Trái ngược hoàn toàn với cảnh hoang tàn đổ nát của Hoàng Gia, vùng sản xuất hữu cơ \"Khánh Hòa Premium Nest\" của Trần Lâm Phong lại đón nhận những tin vui rực rỡ nhất. Lứa tổ yến đầu tiên được thu hoạch với chất lượng đạt mức kỷ lục. Từng tổ yến trắng muốt tự nhiên, săn chắc, hoàn toàn không có bất kỳ dư lượng hóa chất nào.</p>"
        "<p>Đoàn kiểm dịch của FDA Hoa Kỳ sau khi tiến hành kiểm tra toàn diện tại hệ thống hang yến và nhà máy của Premium Nest đã chính thức cấp chứng nhận đạt chuẩn hữu cơ cao cấp với số điểm tuyệt đối 100/100. Đại diện của tập đoàn bán lẻ Mỹ Apex Global đã ngay lập tức bay đến Nha Trang, ký kết hợp đồng xuất khẩu chính ngạch độc quyền tổ yến hữu cơ trị giá 80 triệu USD với Premium Nest trong vòng ba năm.</p>"
        "<p>Đêm trước ngày công bộ thương vụ thâu tóm ngược Tập đoàn Hoàng Gia, Lâm Phong và Lê Gia Hân cùng nhau đứng trên vách đá lộng gió đảo Hòn Nội. Bầu trời đêm Khánh Hòa đầy sao sáng lấp lánh, ánh sao phản chiếu xuống mặt nước biển lặng lờ tạo nên một khung cảnh vô cùng lãng mạn và yên bình. Gió biển thổi mát rượi, vuốt ve mái tóc dài của Gia Hân.</p>"
        "<p>\"Lâm Phong này.\" Gia Hân khẽ quay sang nhìn anh, ánh mắt sắc sảo ngày thường giờ đây bỗng trở nên vô cùng dịu dàng và đầy lý tính. \"Tôi đã kiểm tra kỹ toàn bộ hồ sơ pháp lý và dòng tiền của thương vụ thâu tóm Hoàng Gia ngày mai. Đông Á Group sẽ nắm 55% cổ phần, và anh sẽ sở hữu 45% còn lại với tư cách Chủ tịch kiêm Tổng Giám đốc công nghệ độc quyền. Đây là một sự phân chia sòng phẳng, đúng với giá trị trí tuệ của anh.\"</p>"
        "<p>Lâm Phong mỉm cười nhìn cô: \"Tôi biết cô luôn sòng phẳng, Gia Hân. Nhưng tối nay, chúng ta không bàn về hợp đồng nữa được không?\"</p>"
        "<p>Gia Hân khẽ đỏ mặt dưới ánh sao đêm. Cô cúi đầu, bàn tay nhỏ nhắn khẽ chạm vào bàn tay chai sần đầy sẹo của Lâm Phong trên lan can đá: \"Lâm Phong... cảm ơn anh đã cứu ông nội tôi, và cảm ơn anh đã chứng minh cho tôi thấy tri thức và lòng tự trọng có thể chiến thắng mọi âm mưu bẩn thỉu. Suốt đời này, tôi chỉ muốn làm đối tác sòng phẳng nhất của anh, cả trên thương trường lẫn trong cuộc đời.\"</p>"
        "<p>Lâm Phong nắm chặt lấy bàn tay cô, kéo cô vào lòng mình một cách nhẹ nhàng nhưng đầy kiên định. Dưới bầu trời đầy sao của đảo yến Hòn Nội, hai trái tim kiên cường và lý tính đã chính thức tìm thấy mỏ neo hạnh phúc của cuộc đời mình trước khi bước vào cuộc chiến cuối cùng vào ngày mai.</p>"
    )
    chapters.append({"title": "Chương 9: Buổi Tâm Sự Dưới Ánh Hoàng Hôn Nha Trang", "content": ch9_content})
    
    # ------------------ CHAPTER 10 ------------------
    ch10_content = (
        "<p>Sáng thứ Tư, Đại hội đồng cổ đông bất thường của Tập đoàn Yến Sào Hoàng Gia được tổ chức tại đại sảnh khách sạn Yasaka Nha Trang. Bầu không khí ngột ngạt và căng thẳng bao trùm khắp căn phòng lớn rộng năm trăm mét vuông. Chủ tịch Nguyễn Văn Tư ngồi ở bàn chủ tọa, gương mặt già nua sạm đi, đôi mắt đỏ ngầu vì nhiều đêm mất ngủ.</p>"
        "<p>Cánh cửa sảnh tiệc đột ngột mở ra. Trần Lâm Phong bước vào, khoác trên mình bộ vest đen may đo thủ công vô cùng lịch lãm và đĩnh đạc. Đi bên cạnh anh là Lê Gia Hân, kiêu sa như một nữ hoàng tài chính, tay cầm tập tài liệu thâu tóm đóng dấu đỏ của Đông Á Group. Cả hội trường xôn xao đứng dậy, hàng trăm ánh mắt kinh ngạc đổ dồn về phía người kỹ sư thủy sản mà họ từng khinh rẻ.</p>"
        "<p>\"Trần Lâm Phong? Mày... mày đến đây làm gì?\" Nguyễn Khánh Linh đứng bật dậy, ngón tay đeo nhẫn kim cương run rẩy chỉ thẳng vào mặt anh.</p>"
        "<p>Gia Hân bước lên bục phát biểu, giọng nói lạnh lùng và dứt khoát vang lên qua hệ thống loa phát thanh: \"Kính thưa các cổ đông của Hoàng Gia. Hiện tại, Đông Á Group đã hoàn tất thương vụ thu mua lại toàn bộ 75% nợ xấu của Hoàng Gia từ các ngân hàng thương mại, đồng thời gom mua thành công 55% cổ phần phổ thông từ các cổ đông nhỏ lẻ trên thị trường tự do. Từ giây phút này, Trần Lâm Phong chính là Chủ tịch Hội đồng Quản trị mới của Tập đoàn Yến Sào Hoàng Gia!\"</p>"
        "<p>Lời tuyên bố của Gia Hân như một tiếng sét giữa trời quang đánh thẳng vào bàn chủ tọa. Nguyễn Văn Tư ngã gục xuống ghế, hai mắt trợn trừng đầy tuyệt vọng. Nguyễn Khánh Linh mặt xám ngoét không còn giọt máu, đầu gối bủn rủn quỵ xuống sàn gạch men lạnh giá, toàn thân run rẩy lẩy bẩy.</p>"
        "<p>Trần Thế Hùng định lẻn ra cửa sau, nhưng Trần Lâm Phong đã lạnh lùng cất tiếng: \"Trần Thế Hùng, anh định chạy đi đâu?\"</p>"
        "<p>Đúng lúc đó, bốn chiến sĩ cảnh sát mặc thường phục bước vào sảnh, giơ cao thẻ ngành màu đỏ của Cục Cảnh sát Điều tra Tội phạm về Tham nhũng, Kinh tế, Buôn lậu (C03 Bộ Công an). Người đi đầu đọc to sắc lệnh bắt tạm giam đối với Trần Thế Hùng và Nguyễn Khánh Linh về hành vi cố ý hủy hoại môi trường, lừa đảo chiếm đoạt tài sản và hối lộ công chức nhà nước.</p>"
        "<p>Hùng và Linh gào khóc thảm thiết, quỳ rạp dưới chân Lâm Phong trên nền nhà bê tông lạnh giá. Đầu gối Linh bấu chặt xuống sàn đến mức rỉ máu qua lớp vải đầm mỏng, mồ hôi lạnh chảy ròng ròng ướt sũng mặt mày. Cô ta ôm lấy ống quần vest của Lâm Phong, van xin thảm thiết: \"Phong ơi... em xin lỗi... em bị Hùng xúi giục... xin anh cứu Hoàng Gia, cứu gia đình em...\"</p>"
        "<p>Lâm Phong cúi nhìn vị hôn thê cũ đang khóc lóc nhục nhã dưới chân mình, ánh mắt anh lạnh lùng không một chút gợn sóng. Anh nhẹ nhàng rút ống quần ra khỏi bàn tay dính đầy mồ hôi và nước mắt của cô ta, giọng nói trầm tĩnh vang vọng khắp hội trường:</p>"
        "<p>\"Nguyễn Khánh Linh, khi các người cướp đi công sức nghiên cứu năm năm của tôi và đẩy tôi ra ngoài hoang đảo trong giông bão, các người đã coi thường tri thức và lòng tự trọng của một con người. Luật pháp và sự thật sẽ phán xét hành vi của các người. Đây chính là cái giá phải trả cho sự kiêu ngạo vô bờ bến của các người.\"</p>"
        "<p>Các chiến sĩ C03 tiến tới, khóa chiếc còng số 8 lạnh ngắt vào tay Linh và Hùng, dẫn giải hai kẻ phản bội ra xe cảnh sát đang chờ sẵn dưới sân khách sạn trước sự chứng kiến của toàn thể cổ đông và giới truyền thông miền Trung. </p>"
        "<p>Lâm Phong quay sang nắm chặt lấy tay Lê Gia Hân, mỉm cười kiêu hãnh. Trên vùng biển Khánh Hòa hiền hòa, một chương mới rực rỡ của đế chế yến sào hữu cơ Khánh Hòa Premium Nest đã chính thức được mở ra dưới sự dẫn dắt của tri thức, sự sòng phẳng và tình yêu chân thành.</p>"
    )
    chapters.append({"title": "Chương 10: Sự Trả Giá Tột Cùng", "content": ch10_content})
    
    novel_data = {
        "title": title,
        "author": author,
        "genre": genre,
        "intro": intro,
        "cover_prompt": cover_prompt,
        "chapters": chapters
    }
    
    # Save to pending_novel.json
    pending_path = "/Users/aaronnguyen/TN/App/doctieuthuyet/pending_novel.json"
    with open(pending_path, "w", encoding="utf-8") as f:
        json.dump(novel_data, f, ensure_ascii=False, indent=2)
        
    print(f"✓ SUCCESSFULLY GENERATED NOVEL AND SAVED TO: {pending_path}")
    print(f"✓ Title: {title}")
    print(f"✓ Author: {author}")
    print(f"✓ Chapters count: {len(chapters)}")
    
    # Download the cover image from Pollinations AI
    encoded_prompt = urllib.parse.quote(cover_prompt)
    url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=1024&height=1024&nologo=true"
    print(f"Downloading cover from Pollinations AI: {url}")
    try:
        response = requests.get(url, timeout=60)
        if response.status_code == 200:
            cover_path = "/Users/aaronnguyen/TN/App/doctieuthuyet/pending_cover.png"
            with open(cover_path, "wb") as f:
                f.write(response.content)
            print(f"✓ SUCCESSFULLY DOWNLOADED COVER AND SAVED TO: {cover_path}")
        else:
            print(f"❌ Failed to download cover. Status code: {response.status_code}")
    except Exception as e:
        print("❌ Error downloading cover:", e)

if __name__ == "__main__":
    build_and_publish_novel()
