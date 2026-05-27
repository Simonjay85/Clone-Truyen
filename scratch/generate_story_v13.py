# -*- coding: utf-8 -*-
import json
import os

def generate():
    title = "Cướp Công Thức Sâm Ngọc Linh, Kỹ Sư Lật Kèo Thâu Tóm Tập Đoàn Dược Khiến Kẻ Phản Bội Phải Trả Giá"
    author = "Trịnh Đình Quân"
    genre = "Sảng Văn"
    
    intro = (
        "<p><strong>\"Anh chỉ là một thằng thầy lang vườn rách nát mang chút kiến thức thảo dược vụn vặt, lấy tư cách gì mà đòi đứng chung hàng ngũ với các giáo sư đầu ngành của viện công nghệ sinh học? Biến khỏi đây trước khi tôi hủy hoại hoàn toàn tương lai của anh!\"</strong></p>\n"
        "<p>Đoàn Thế Phong, phó giám đốc phòng thí nghiệm sinh học Kon Tum, lạnh lùng ném toàn bộ sổ tay nghiên cứu và đồ đạc của Trịnh Đình Quân ra ngoài hành lang dưới cơn mưa rừng Tây Nguyên tầm tã. Hắn đã âm thầm cướp đoạt công trình nghiên cứu chiết xuất saponin vàng MR2 từ tế bào gốc Sâm Ngọc Linh của anh để chuẩn bị cho buổi gọi vốn thế kỷ và đưa công ty Phong Cát Pharma lên sàn chứng khoán IPO nghìn tỷ.</p>\n"
        "<p>Thế nhưng, kẻ phản bội không thể ngờ rằng công thức chiết xuất ấy chỉ là một nửa bản thiết kế. Bằng tri thức y học cổ truyền uyên bác kết hợp với công nghệ kiểm chứng lâm sàng hiện đại, Trịnh Đình Quân đã liên thủ cùng Lâm Nhã Chi - ái nữ lý tính của tập đoàn dược phẩm lớn nhất Việt Nam. Với nhật ký commit Git bất biến, bằng sáng chế chính thức từ Cục Sở hữu Trí tuệ và sắc lệnh đanh thép từ cơ quan C03, anh sẽ thực hiện một màn phản kích kinh thiên động địa, đẩy kẻ phản bội vào vực thẳm pháp lý không thể dung thứ!</p>"
    )
    
    cover_prompt = (
        "A highly luxurious anime-style book cover, featuring a determined handsome young Vietnamese biochemist in a clean white lab coat, standing inside a state-of-the-art laboratory in Kon Tum. He is holding a glowing golden glass vial with a pure golden Sâm Ngọc Linh extract. In the background, futuristic automated glass chromatography columns are glowing with soft golden and amber light. Hyper-detailed, cinematic soft lighting, premium webnovel art, 1:1 aspect ratio, absolutely no text or words on screen."
    )
    
    chapters = []
    
    # CHAPTER 1
    ch1_title = "Chương 1: Sỉ Nhục Giữa Phòng Thí Nghiệm"
    ch1_content = (
        "<p>Mưa rừng Kon Tum trút xuống tầm tã, từng hạt mưa lạnh buốt quất vào những lớp kính cường lực của Viện Công nghệ Sinh học Tây Nguyên. Tiếng sấm rền vang vọng từ đỉnh Ngọc Linh xa xôi, làm rung động cả những dãy hành lang lát đá hoa cương lạnh lẽo của khu nghiên cứu trọng điểm quốc gia.</p>"
        "<p>Trịnh Đình Quân đứng sững giữa phòng thí nghiệm sắc ký lỏng hiệu năng cao (HPLC). Anh mặc bộ đồ bảo hộ màu xanh sờn cũ, hai tay ôm chặt chiếc hộp giấy đựng vài món đồ cá nhân nghèo nàn: một chiếc kính bảo hộ cá nhân, vài ống nghiệm thủy tinh tự mua và cuốn sổ tay sờn gáy ghi chép thực địa sắc tố thảo dược.</p>"
        "<p>\"Cút đi! Một thằng thầy lang vườn rách nát mang chút kiến thức thảo dược vụn vặt như mày, lấy tư cách gì mà đòi đứng chung hàng ngũ với các giáo sư đầu ngành của chúng tôi?\"</p>"
        "<p>Giọng nói rít lên đầy khinh bỉ của Đoàn Thế Phong vang vọng khắp căn phòng lab hiện đại. Phong đứng đó, cằm hất lên trời, ngón tay đeo chiếc nhẫn ngọc bích liên tục xoay tròn trên mu bàn tay trắng trẻo không một vết chai sạn. Hắn mặc chiếc áo blouse trắng tinh khôi đặt may riêng từ nhà mốt Pháp, ngực thêu chữ nổi vàng óng: \"Phó Giám đốc Đoàn Thế Phong\".</p>"
        "<p>Cạnh hắn là bà Cao Lệ Thu, mẹ ruột của hắn kiêm Chủ tịch Hội đồng Quản trị Phong Cát Pharma. Bà Thu khoanh tay trước ngực, chiếc nhẫn kim cương hai carat lấp lánh dưới ánh đèn huỳnh quang cực mạnh của phòng thí nghiệm. Bà quét ánh mắt sắc như dao cạo qua người Quân, nhổ nước bọt xuống sàn gạch men bóng loáng ngay trước mũi giày bảo hộ sờn rách của anh.</p>"
        "<p>\"Nhìn lại bản thân mày xem, Trịnh Đình Quân,\" bà Thu khinh khỉnh lên tiếng, giọng nói chói tai đầy kiêu ngạo. \"Cha mày chỉ là một ông thầy lang nghèo trên núi Ngọc Linh, bốc thuốc nam đổi gạo ăn qua ngày. Mày may mắn được viện nhận vào làm kỹ sư vận hành máy sắc ký quèn, lại ảo tưởng bản thân là thiên tài chế tạo dược phẩm sao?\"</p>"
        "<p>\"Công trình chiết xuất Saponin vàng MR2 từ tế bào gốc Sâm Ngọc Linh này, từ hôm nay sẽ thuộc về bản quyền của con trai tôi - Đoàn Thế Phong. Hồ sơ đăng ký bằng sáng chế độc quyền đã được gửi lên Cục Sở hữu Trí tuệ dưới tên nó. Mày không còn bất kỳ liên quan nào ở đây nữa,\" bà Thu cười lạnh, vỗ vai con trai đầy tự hào.</p>"
        "<p>Quân nghiến răng chặt đến mức tủy sống lạnh buốt. Lồng ngực anh phập phồng dữ dội dưới lớp áo bảo hộ sờn cũ, lòng bàn tay siết chặt khiến móng tay đâm sâu vào thịt, rỉ ra những giọt máu hồng ấm nóng. Anh nhìn chằm chằm vào màn hình máy tính điều khiển cột sắc ký lỏng — nơi chứa đoạn mã nguồn tự động hóa chu kỳ nhiệt áp suất do chính anh thức trắng ba trăm đêm để viết ra.</p>"
        "<p>\"Đoàn Thế Phong, anh biết rõ công thức kích hoạt chu kỳ nhiệt của cột sắc ký là do tôi phát minh ra. Không có thuật toán điều biến nhiệt độ đó, hoạt chất Saponin Majonoside-R2 (MR2) cực kỳ quý hiếm trong Sâm Ngọc Linh sẽ bị phân hủy hoàn toàn ở nhiệt độ bốn mươi độ C! Các người ăn cắp công trình của tôi để trục lợi!\" Quân lớn tiếng, giọng nói vang lên đanh thép giữa tiếng sấm rền ngoài cửa sổ.</p>"
        "<p>Phong cười khẩy đầy đắc ý. Hắn bước tới gần Quân, dùng ngón tay đeo nhẫn gõ mạnh vào lồng ngực Quân, hơi thở mang theo mùi nước hoa đắt tiền phả vào mặt anh.</p>"
        "<p>\"Ai chứng minh? Ai tin mày?\" Phong ghé sát tai Quân thì thầm đầy nham hiểm. \"Tất cả nhật ký hệ thống cục bộ trong phòng lab này đã bị tôi xóa sạch. Trên danh nghĩa máy chủ cục bộ, tôi mới là người thực hiện dòng commit code cuối cùng. Mày chỉ là thằng chạy việc phụ việc cho tôi. Ngày mai, tập đoàn Phong Cát Pharma sẽ công bố công nghệ này để khởi động chiến dịch IPO hai nghìn tỷ đồng tại sàn HoSE.\"</p>"
        "<p>\"Còn mày? Mày sẽ bị đuổi học, bị trục xuất khỏi viện nghiên cứu và đưa vào danh sách đen của toàn ngành dược Việt Nam. Sẽ không một phòng lab nào ở cái đất nước này dám nhận một kẻ có vết nhơ ăn cắp tài liệu như mày đâu!\"</p>"
        "<p>Bà Thu ra hiệu cho hai gã bảo vệ cao lớn mặc vest đen đứng bên cửa hành lang. Chúng lập tức bước tới, thô bạo giật lấy chiếc hộp giấy trên tay Quân và quăng thẳng ra ngoài hành lang. Chiếc hộp giấy rơi xuống vũng nước mưa dơ bẩn, cuốn sổ tay ghi chép thực địa quý giá bị nước mưa thấm đẫm, nhòe nhoẹt mực.</p>"
        "<p>\"Mời kỹ sư Trịnh rời khỏi đây ngay lập tức. Nơi này là phòng thí nghiệm cấp độ ba vô trùng, không dành cho những kẻ tạp nham không có học vị,\" Hùng - gã trợ lý trung thành của Phong lên tiếng đầy hống hách.</p>"
        "<p>Quân lẳng lặng bước ra ngoài hành lang dưới cơn mưa lạnh ngắt của rừng Tây Nguyên. Anh cúi xuống nhặt cuốn sổ tay sờn rách từ vũng bùn bẩn, cẩn thận lau sạch những vệt nước mưa trên bìa sổ rồi cất vào trong lồng ngực áo khoác ấm nóng của mình.</p>"
        "<p>Nước mưa dội thẳng vào mặt Quân, hòa lẫn vào những giọt mồ hôi lạnh buốt đang chảy dọc thái dương. Nhưng đôi mắt anh không hề có sự tuyệt vọng, ngược lại nó sáng rực lên một tia sáng lạnh lùng, sắc bén như lưỡi dao mổ.</p>"
        "<p>Anh quay lại nhìn bảng hiệu bằng đồng sáng loáng của Viện Công nghệ Sinh học Tây Nguyên lần cuối, nghiến răng tự hứa với lòng mình.</p>"
        "<p>\"Đoàn Thế Phong, Cao Lệ Thu... Các người cướp đi công sức mười năm của tôi, muốn dùng nó để xây dựng đế chế tiền bẩn. Các người nghĩ rằng chỉ cần xóa lịch sử máy chủ cục bộ là có thể cướp sạch tri thức sao?\"</p>"
        "<p>\"Các người không hề biết, cốt lõi thật sự của công nghệ sắc ký tế bào gốc nằm ở đâu. Tôi thề, tôi sẽ khiến các người phải quỳ gối trả giá gấp trăm lần ngay tại thời điểm các người nghĩ mình đang đứng trên đỉnh cao nhất!\"</p>"
    )
    
    # CHAPTER 2
    ch2_title = "Chương 2: Mỹ Nhân Hào Môn Lý Tính"
    ch2_content = (
        "<p>Ba ngày sau buổi chiều định mệnh tại Kon Tum, Trịnh Đình Quân có mặt tại thành phố Đà Nẵng. Anh ngồi lặng lẽ ở một góc khuất trong phòng trà thương gia của khách sạn năm sao InterContinental bên bán đảo Sơn Trà. Khí hậu ven biển dịu mát khác hẳn cái lạnh buốt của núi rừng Ngọc Linh, nhưng tâm trạng của Quân thì vẫn vô cùng trầm tĩnh và tập trung.</p>"
        "<p>Cánh cửa phòng trà mở ra, một người phụ nữ trẻ bước vào dưới sự hộ tống của hai luật sư tài chính trung niên mặc vest xám thanh lịch. Cô mặc một chiếc đầm đen công sở giản dị nhưng cắt may cực kỳ tinh tế, mái tóc dài buộc gọn phía sau để lộ khuôn mặt thanh tú với những đường nét vô cùng sắc sảo, quý phái.</p>"
        "<p>Đó là Lâm Nhã Chi — người thừa kế thế hệ thứ ba kiêm Tổng Giám đốc điều hành của Lâm Gia Group, tập đoàn y dược và bất động sản có quy mô vốn hóa hàng chục ngàn tỷ đồng tại miền Nam. Nhã Chi không phải là kiểu tiểu thư hào môn kiêu kỳ vô não; cô tốt nghiệp thủ khoa ngành Luật Tài chính tại Đại học Harvard và có ba năm làm việc tại văn phòng luật sư quốc tế ở New York trước khi về nước tiếp quản tập đoàn.</p>"
        "<p>Cô bước đến bàn của Quân, không vội vàng ngồi xuống mà đưa mắt quan sát anh một lượt từ đầu đến chân. Đứng trước một chàng trai mặc chiếc áo sơ mi giản dị đã sờn cổ, đi đôi giày da cũ kỹ nhưng có đôi mắt sáng quắc đầy trí tuệ, cô khẽ mỉm cười lịch thiệp và chìa bàn tay mềm mại ra.</p>"
        "<p>\"Chào anh Quân. Tôi là Lâm Nhã Chi. Tôi đã đọc bản tóm tắt đề án nghiên cứu do trung gian gửi tới. Tôi không đầu tư vì sự thương cảm hay những câu chuyện kịch tính trên mạng. Tập đoàn Lâm Gia chỉ đầu tư khi tính khả thi pháp lý và thương mại đạt một trăm phần trăm,\" Nhã Chi cất giọng trong trẻo nhưng vô cùng điềm tĩnh, lý tính và dứt khoát.</p>"
        "<p>\"Tôi hiểu rõ phong cách làm việc của Lâm Gia,\" Quân mỉm cười bình thản, khẽ mời cô ngồi. \"Tôi cũng không đến đây để xin lòng thương hại. Tôi đến đây để mang lại cho cô một cơ hội sở hữu độc quyền công nghệ dược phẩm sinh học lớn nhất Đông Nam Á trong mười năm tới.\""
        "<p>Nhã Chi mở chiếc laptop chuyên dụng của mình ra, đặt lên bàn gỗ sồi. Ngón tay cô gõ nhanh trên bàn phím, truy cập trực tiếp vào hệ thống cơ sở dữ liệu của Cục Sở hữu Trí tuệ Việt Nam và hệ sinh thái bằng sáng chế quốc tế WIPO.</p>"
        "<p>\"Hồ sơ của anh cho thấy anh đã gửi bản phác thảo sáng chế quy trình tách chiết Saponin MR2 từ ba năm trước dưới dạng bảo mật cá nhân, trước khi anh gia nhập Viện Công nghệ Sinh học Tây Nguyên. Điều này có nghĩa là về mặt luật pháp, quyền ưu tiên sở hữu trí tuệ gốc thuộc về cá nhân anh, chứ không thuộc về viện nghiên cứu,\" Nhã Chi phân tích, ánh mắt cô hiện lên sự nhạy bén cực kỳ đáng sợ của một luật sư hàng đầu.</p>"
        "<p>\"Tuy nhiên, Đoàn Thế Phong vừa nộp hồ sơ xin cấp bằng sáng chế khẩn cấp cho cùng một quy trình sắc ký lỏng nhiệt trị vào tuần trước, có kèm theo xác nhận công trình nghiên cứu cấp cơ sở của viện nghiên cứu Kon Tum. Hồ sơ của họ rất mạnh vì có sự hậu thuẫn của Phong Cát Pharma và các mối quan hệ sở ngành.\""
        "<p>Quân không hề nao núng, anh đẩy về phía cô một chiếc ổ cứng di động bọc thép chống sốc.</p>"
        "<p>\"Trong này chứa toàn bộ lịch sử phát triển thuật toán điều khiển cột sắc ký lỏng tự động hóa. Tôi đã viết và đẩy toàn bộ mã nguồn này lên một kho lưu trữ Git riêng tư trên GitHub từ năm năm trước. Mỗi dòng code đều được ký số bằng mã khóa PGP cá nhân của tôi, liên kết trực tiếp với chữ ký số quốc gia đã được công chứng pháp lý.\"</p>"
        "<p>\"Đoàn Thế Phong có thể xóa lịch sử trên máy chủ cục bộ của phòng lab Kon Tum, nhưng hắn không bao giờ có thể giả mạo hoặc thay đổi lịch sử commit bất biến đã được đóng dấu thời gian mật mã trên GitHub quốc tế. Bất kỳ chuyên gia kiểm toán công nghệ nào cũng có thể chứng minh tôi mới là tác giả duy nhất của đoạn code điều khiển hệ thống chiết xuất,\" Quân dõng dạc khẳng định.</p>"
        "<p>Nhã Chi khẽ xoay nhẹ cây bút dạ trên tay, ánh mắt cô sáng lên lấp lánh như tìm thấy một viên kim cương thô quý giá giữa sa mạc cát bụi.</p>"
        "<p>\"Rất xuất sắc. Anh đã chuẩn bị lá chắn pháp lý cực kỳ vững chắc. Nhưng tôi còn một câu hỏi cuối cùng,\" cô nghiêng người về phía trước, giọng nói trầm xuống đầy sức nặng. \"Tại sao công thức của anh lại vượt trội hơn công thức mà Đoàn Thế Phong đang nắm giữ? Hắn cũng có máy móc hiện đại và nguồn nguyên liệu Sâm Ngọc Linh dồi dào.\""
        "<p>Quân nhìn thẳng vào mắt cô ái nữ lý tính, cất giọng đầy tự tin: \"Đơn giản là vì hắn chỉ cướp được cái vỏ. Công thức hắn có chỉ là sắc ký ở nhiệt độ tiêu chuẩn ba mươi bảy độ C, cho ra hiệu suất chiết xuất Saponin MR2 chỉ đạt mười hai phần trăm, kèm theo lượng tạp chất lớn.\"</p>"
        "<p>\"Hắn không hề biết rằng, để kích hoạt hoàn toàn tế bào gốc Sâm Ngọc Linh và nâng hiệu suất chiết xuất lên chín mươi tám phần trăm tinh khiết, hệ thống phải vận hành theo biểu đồ nhiệt hình sin dao động từ mười lăm đến bốn mươi hai độ C trong môi trường áp suất âm áp suất cao luân phiên. Quy trình kích hoạt nhiệt này nằm hoàn toàn trong đầu tôi. Nếu không có nó, các mẻ chiết xuất của Phong sẽ chỉ cho ra một loại dung dịch vô giá trị, thậm chí có thể chứa độc tố tự phân hủy.\"</p>"
        "<p>Lâm Nhã Chi đóng chiếc laptop lại với một tiếng \"cập\" dứt khoát. Cô quay sang gật đầu với hai vị luật sư tài chính đứng phía sau.</p>"
        "<p>\"Soạn thảo hợp đồng hợp tác chiến lược ngay lập tức. Tập đoàn Lâm Gia sẽ đầu tư một trăm năm mươi tỷ đồng giai đoạn một để xây dựng nhà máy chiết xuất sinh học công nghệ cao tại Khu công nghệ cao Đà Nẵng. Anh Quân sẽ giữ bốn mươi lăm phần trăm cổ phần sáng lập và quyền quyết định tối cao về mặt kỹ thuật.\"</p>"
        "<p>\"Nhưng trước khi ký kết chính thức, tôi cần tiến hành một cuộc thẩm định lâm sàng thực tế để chứng minh tính hiệu quả của hoạt chất Saponin MR2 tinh khiết đối với tế bào xơ hóa. Anh có sẵn sàng chứng minh năng lực thực tế của mình không?\"</p>"
        "<p>Quân đứng dậy, siết chặt bàn tay mềm mại của Nhã Chi: \"Tôi sẵn sàng. Sự thật lâm sàng sẽ là câu trả lời đanh thép nhất cho sự hoài nghi của cô.\""
    )
    
    # CHAPTER 3
    ch3_title = "Chương 3: Đông - Tây Y Kết Hợp Biện Chứng"
    ch3_content = (
        "<p>Bệnh viện Quốc tế miền Nam tại trung tâm Sài Gòn chìm trong bầu không khí vô cùng căng thẳng và u ám. Trên tầng cao nhất của khu VIP chuyên biệt, các y bác sĩ và chuyên gia y tế hàng đầu đang túc trực hai mươi bốn trên hai mươi bốn giờ bên ngoài phòng hồi sức tích cực (ICU).</p>"
        "<p>Ông nội của Lâm Nhã Chi — lão chủ tịch Lâm Vạn Trường, người sáng lập và linh hồn của tập đoàn Lâm Gia — đang nằm trên giường bệnh với hệ thống dây rợ nhằng nhịt nối vào cơ thể gầy gò. Máy trợ thở cơ học rít lên từng hồi nặng nề, các chỉ số trên màn hình theo dõi liên tục báo động đỏ chói.</p>"
        "<p>\"Bệnh án xơ hóa phổi vô căn giai đoạn cuối (IPF) của lão chủ tịch đã chuyển biến rất xấu sau cơn viêm phổi cấp tính tối qua. Độ đàn hồi của nhu mô phổi đã giảm xuống mức tối thiểu, các nang phổi bị xơ hóa hoàn toàn không thể trao đổi oxy. Chỉ số SpO2 của cụ hiện chỉ dao động từ bảy mươi hai đến bảy mươi lăm phần trăm dù đã thở oxy liều cao một trăm phần trăm,\" Giáo sư Nguyễn Hoài Nam, Trưởng khoa Hô hấp của bệnh viện lắc đầu ái ngại báo cáo với gia đình.</p>"
        "<p>\"Với y học phương Tây hiện tại, chúng tôi đã sử dụng tất cả các loại thuốc chống xơ hóa mạnh nhất như Pirfenidone và Nintedanib nhưng cơ thể cụ không còn phản ứng. Lão chủ tịch... khó lòng qua khỏi đêm nay. Xin gia đình chuẩn bị tinh thần,\" vị giáo sư kỳ cựu thở dài đầy bất lực.</p>"
        "<p>Nhã Chi đứng bên giường bệnh, hai tay cô đan chặt vào nhau đến mức các đầu ngón tay trắng bệch không còn một giọt máu. Gương mặt cô vẫn giữ được vẻ lạnh lùng lý tính thường ngày, nhưng đôi mắt đỏ hoe đã phản ánh nỗi đau đớn tột cùng đang giằng xé bên trong tâm hồn cô.</p>"
        "<p>Đúng lúc này, cánh cửa phòng VIP mở ra, Trịnh Đình Quân bước vào trong bộ trang phục giản dị, tay xách một chiếc hộp bảo ôn y tế màu bạc nhỏ gọn. Đi sau anh là hai vị bác sĩ Đông y kỳ cựu của dòng họ Trịnh từ Kon Tum xuống.</p>"
        "<p>\"Anh Quân? Anh mang cái gì đến đây thế? Nơi này là phòng vô trùng cấp độ cao, không được phép mang những thứ thảo dược chưa qua kiểm định vào!\" bà Lâm Lệ Bình, cô ruột của Nhã Chi lớn tiếng ngăn cản đầy giận dữ.</p>"
        "<p>Quân không vội vàng giải thích, anh bước đến bên giường bệnh của lão chủ tịch, nhẹ nhàng đặt tay lên mạch cổ tay của ông cụ để cảm nhận nhịp đập yếu ớt, đứt quãng như ngọn đèn trước gió.</p>"
        "<p>\"Bạch giáo sư, theo y học cổ truyền, đây là chứng Phế nuy cực kỳ nguy kịch. Chân âm của cụ đã hao kiệt hoàn toàn do tác dụng phụ của các loại thuốc hóa dược mạnh, khí huyết ứ trệ khiến phế khí không thể lưu thông, dẫn đến tình trạng ngạt thở lâm sàng,\" Quân cất giọng trầm ấm nhưng vô cùng uy lực, giải thích rõ ràng mạch lạc.</p>"
        "<p>\"Thuốc Tây y tuy mạnh ở phần ngọn nhưng lại làm khô cạn chân âm của cụ. Hiện tại, chúng ta phải áp dụng phương pháp Đông - Tây y kết hợp biện chứng. Tôi sẽ dùng một giọt tinh chất Saponin vàng MR2 hoạt hóa tế bào gốc nhỏ dưới lưỡi của cụ để tạm thời giữ lại nguyên khí và kích hoạt khả năng tự bảo vệ của các tế bào nang phổi còn sống sót. Sau đó, tôi sẽ thực hiện châm cứu bấm huyệt các huyệt vị Thái Uyên, Phế Du để khơi thông kinh lạc phế quản.\""
        "<p>\"Điên rồ! Hoang đường!\" Giáo sư Nam tức giận đỏ mặt tai tái. \"Một giọt nước thảo dược của anh mà đòi cứu sống một bệnh nhân đã bị suy hô hấp cấp xơ phổi giai đoạn cuối sao? Nếu cụ có mệnh hệ gì, ai sẽ chịu trách nhiệm pháp lý trước pháp luật?\"</p>"
        "<p>Nhã Chi bước lên một bước, đứng chắn ngay trước mặt Quân. Cô nhìn thẳng vào mắt Giáo sư Nam, giọng nói vang lên đanh thép và đầy quyết đoán.</p>"
        "<p>\"Tôi chịu trách nhiệm! Toàn bộ quyền quyết định y tế đối với ông nội đã được cụ ủy quyền pháp lý cho tôi bằng văn bản công chứng. Bệnh viện đã tuyên bố bất lực, vậy tại sao không cho phép chúng tôi thử phương pháp này? Anh Quân, xin hãy tiến hành ngay lập tức!\"</p>"
        "<p>Quân khẽ gật đầu chào cô ái nữ dứt khoát. Anh mở chiếc hộp bảo ôn bạc, lấy ra một chiếc ống nghiệm thủy tinh nhỏ chứa một giọt dung dịch màu vàng óng ánh như mật ong rừng nguyên chất — đó chính là tinh chất Saponin vàng MR2 siêu tinh khiết được anh tách chiết bằng quy trình sắc ký nhiệt tự động hóa.</p>"
        "<p>Anh nhẹ nhàng dùng dụng cụ y tế nâng lưỡi của lão chủ tịch lên, nhỏ giọt tinh chất quý giá vào vùng niêm mạc dưới lưỡi — nơi có hệ thống mao mạch phong phú giúp hấp thụ hoạt chất thẳng vào tuần hoàn máu mà không qua hệ tiêu hóa bị suy kiệt.</p>"
        "<p>Cùng lúc đó, hai bàn tay của Quân chuyển động cực nhanh. Ngón cái của anh bấm mạnh vào huyệt Thái Uyên ở lằn chỉ cổ tay của cụ, tạo ra một lực ấn đều đặn và sâu sắc để kích thích phế khí. Các vị bác sĩ Đông y đi cùng cũng nhanh chóng châm cứu các kim bạc vô trùng vào các huyệt vị trọng yếu trên lưng cụ.</p>"
        "<p>Mười phút trôi qua trong sự im lặng nghẹt thở của căn phòng VIP. Tiếng tích tắc của chiếc đồng hồ treo tường như tiếng gõ của tử thần đang đếm ngược thời gian.</p>"
        "<p>Đột nhiên, màn hình theo dõi chỉ số SpO2 khẽ chớp sáng. Con số 72 bắt đầu nhảy lên 75... rồi 78... rồi 82!</p>"
        "<p>Nhịp tim đập loạn xạ 140 lần trên phút của ông cụ bắt đầu hạ dần xuống mức ổn định 95 lần trên phút. Tiếng rít nghẹn ngào trong lồng ngực cụ dịu hẳn đi, sắc mặt xám ngoét không còn giọt máu của ông cụ bắt đầu hiện lên một vệt hồng hào nhè nhẹ ở hai bên gò má.</p>"
        "<p>Lão chủ tịch khẽ cử động ngón tay trỏ, đôi mắt nhắm nghiền suốt ba ngày qua từ từ hé mở, nhìn xung quanh đầy tỉnh táo.</p>"
        "<p>\"Oxy... ta cảm thấy... lồng ngực... thông thoáng rồi...\" ông cụ thều thào nói ra được thành tiếng rõ ràng.</p>"
        "<p>Giáo sư Nam há hốc miệng kinh ngạc, hai mắt trợn trừng nhìn màn hình chỉ số như nhìn thấy một bóng ma giữa ban ngày. Toàn bộ các bác sĩ Tây y trong phòng lab đều đứng sững sờ, mồ hôi lạnh chảy ròng ròng dọc sống lưng trước phép màu y học hiển hiện ngay trước mắt.</p>"
    )
    
    # CHAPTER 4
    ch4_title = "Chương 4: Phép Miracle Kiểm Chứng Lâm Sàng"
    ch4_content = (
        "<p>Sáng hôm sau, ánh nắng ban mai rực rỡ chiếu qua những ô cửa kính lớn của Bệnh viện Quốc tế miền Nam. Căn phòng VIP không còn vẻ u ám của ngày hôm trước, thay vào đó là một sự kinh ngạc tột độ bao trùm lên toàn bộ ban lãnh đạo và hội đồng y khoa của bệnh viện.</p>"
        "<p>Giáo sư Nguyễn Hoài Nam đứng trước màn hình đọc phim chụp cắt lớp vi tính độ phân giải cao (HRCT) phổi của lão chủ tịch Lâm Vạn Trường. Trên tay ông là tập kết quả xét nghiệm khí máu động mạch vừa được phòng hóa nghiệm gửi lên khẩn cấp lúc sáu giờ sáng.</p>"
        "<p>\"Đây... điều này hoàn toàn nằm ngoài mọi quy luật sinh lý học và bệnh học hiện đại mà tôi được biết!\" giọng Giáo sư Nam run rẩy bần bật, sắc mặt ông xám ngoét vì không thể tin nổi vào những số liệu thực tế trước mắt.</p>"
        "<p>\"Phim HRCT phổi chụp sáng nay cho thấy các tổn thương dạng kính mờ và các dải xơ hóa dày đặc ở thùy dưới phổi của cụ đã giảm đi tới sáu mươi phần trăm chỉ sau một đêm! Các phế nang bị phá hủy đang có dấu hiệu tái sinh mạnh mẽ, các tế bào biểu mô phế quản bị tổn thương đang tự phục hồi với tốc độ kinh ngạc.\"</p>"
        "<p>\"Đặc biệt, kết quả khí máu động mạch cho thấy phân áp oxy (PaO2) đã tăng từ năm mươi mốt mmHg lên chín mươi lăm mmHg ở điều kiện thở khí trời tự nhiên! Chỉ số SpO2 của cụ hiện đạt mức ổn định tuyệt đối chín mươi tám phần trăm mà không cần đến sự hỗ trợ của máy thở cơ học nữa!\"</p>"
        "<p>Lâm Nhã Chi đứng bên cạnh giường bệnh của ông nội. Cô khẽ nắm lấy bàn tay ấm áp của lão chủ tịch, lúc này ông cụ đã có thể tự ngồi dậy uống nước yến và nói chuyện vô cùng minh mẫn với con cháu. Nụ cười nhẹ nhõm hiếm hoi xuất hiện trên đôi môi thanh tú của cô, nhưng ánh mắt lý tính của cô lập tức hướng về phía Trịnh Đình Quân đang đứng kiểm tra các chỉ số điện tâm đồ.</p>"
        "<p>\"Giáo sư Nam, ông có thể chính thức khẳng định kết quả lâm sàng kỳ diệu này là do tác động trực tiếp của hoạt chất Saponin vàng MR2 hoạt hóa tế bào gốc mà anh Quân đã sử dụng không?\" Nhã Chi lên tiếng hỏi, giọng điệu vô cùng sắc sảo và rõ ràng.</p>"
        "<p>Giáo sư Nam hít một hơi thật sâu, lau những giọt mồ hôi lạnh lấm tấm trên trán. Ông khẽ cúi đầu trước Quân, thái độ khinh miệt ngày hôm trước hoàn toàn biến mất, thay vào đó là một sự kính phục và tôn trọng sâu sắc từ tận đáy lòng của một người làm khoa học chân chính.</p>"
        "<p>\"Tôi hoàn toàn xác nhận lâm sàng. Với tư cách là Trưởng khoa Hô hấp và Chủ tịch Hội đồng Y khoa bệnh viện, tôi khẳng định không có bất kỳ loại biệt dược phương Tây nào có thể tạo ra sự tái sinh nhu mô phổi thần kỳ này trong vòng mười hai giờ.\"</p>"
        "<p>\"Tinh chất Saponin vàng MR2 của kỹ sư Trịnh Đình Quân thực sự là một đột phá vĩ đại, kết hợp hoàn hảo giữa tinh hoa dược liệu Đông y cổ truyền với công nghệ kích hoạt tế bào gốc hiện đại của phương Tây. Tôi xin ký tên và đóng dấu đỏ xác nhận toàn bộ báo cáo kết quả kiểm chứng lâm sàng chính thức này để gửi lên Bộ Y tế,\" Giáo sư Nam dõng dạc tuyên bố.</p>"
        "<p>Ông cụ Lâm Vạn Trường nhìn Quân đầy trìu mến, giọng nói ấm áp mang theo sự uy nghiêm của một vị lão tướng thương trường: \"Chàng trai trẻ... cháu đã cứu mạng ta khỏi bàn tay tử thần. Tri thức của cháu là vô giá. Nhã Chi à, con đã chọn đúng đối tác chiến lược cho tập đoàn chúng ta rồi.\""
        "<p>Nhã Chi quay sang Quân, khẽ kéo anh ra phía ban công lộng gió của phòng bệnh VIP để tránh sự chú ý của mọi người. Cô nhìn thẳng vào mắt anh, phong thái vô cùng tự tin và đĩnh đạc.</p>"
        "<p>\"Anh Quân, cuộc thẩm định lâm sàng đã thành công vượt mong đợi. Báo cáo đóng dấu đỏ này sẽ là vũ khí pháp lý vô địch của chúng ta trước Cục Quản lý Dược và các quỹ đầu tư lớn.\"</p>"
        "<p>\"Tuy nhiên, tôi vừa nhận được tin tức từ Kon Tum. Đoàn Thế Phong và Phong Cát Pharma đã phát hiện ra sự hồi sinh của anh. Hắn biết mẻ chiết xuất thử nghiệm của hắn tại nhà máy bị hỏng vì thiếu chu kỳ nhiệt của anh, nên hắn đang chuẩn bị một âm mưu tàn độc để tiêu diệt chúng ta trước khi chúng ta kịp công bố hợp đồng đầu tư.\"</p>"
        "<p>Quân khẽ cười nửa miệng, ánh mắt anh lóe lên tia nhìn lạnh lùng như sương giá Tây Nguyên: \"Tôi biết hắn sẽ không ngồi yên chờ chết. Hắn sẽ tấn công bằng truyền thông bẩn và các mối quan hệ quyền lực bẩn thỉu của hắn đúng không?\"</p>"
        "<p>\"Đúng vậy,\" Nhã Chi khẽ gật đầu, khuôn mặt cô hiện lên sự quyết tâm sắt đá. \"Hắn đã liên kết với một vài cán bộ thoái hóa biến chất để chuẩn bị ra tay. Nhưng liên minh giữa tôi và anh đã sẵn sàng giăng lưới. Hãy để chúng tự đâm đầu vào cái bẫy tự diệt vong của chính mình.\""
    )
    
    # CHAPTER 5
    ch5_title = "Chương 5: Bước Ngoặt Bế Tắc Thực Sự"
    ch5_content = (
        "<p>Đúng như dự đoán của Lâm Nhã Chi, cơn bão bẩn thỉu từ phía Phong Cát Pharma đã trút xuống liên minh của họ với một sức công phá khủng khiếp. Đoàn Thế Phong và bà Cao Lệ Thu đã quyết định ra tay trước bằng tất cả nguồn lực tài chính đen và các mối quan hệ ngầm mà họ tích lũy suốt nhiều thập kỷ qua.</p>"
        "<p>Tối thứ Năm, lúc tám giờ tối — khung giờ vàng của mạng xã hội, một buổi phát sóng trực tiếp (livestream) được tổ chức rầm rộ trên các nền tảng truyền thông lớn do một trang tin tức tài chính có hàng triệu người theo dõi thực hiện. Khách mời đặc biệt xuất hiện trên sóng chính là Đoàn Thế Phong trong bộ vest sang trọng, bên cạnh là một nhóm người tự xưng là \"đại diện các nhà khoa học độc lập\" và một gã luật sư mặt đầy vẻ gian trá tên Trần Hữu Luật.</p>"
        "<p>\"Kính thưa toàn thể dư luận cả nước,\" Phong cất giọng dõng dạc trước ống kính, vẻ mặt đầy sự chính trực giả tạo nhưng đôi mắt xảo quyệt thì không ngừng liếc nhìn bảng thống kê lượt xem đang tăng vọt từng giây.</p>"
        "<p>\"Chúng tôi vô cùng phẫn nộ khi phát hiện ra một vụ lừa đảo công nghệ y sinh quy mô lớn liên quan đến hoạt chất Sâm Ngọc Linh giả hiệu. Trịnh Đình Quân — một cựu kỹ sư bị đuổi khỏi Viện Công nghệ Sinh học Tây Nguyên vì hành vi ăn cắp tài liệu — đã cấu kết với tập đoàn Lâm Gia để bán ra thị trường một loại dung dịch thảo dược tự chế chưa qua kiểm định của Bộ Y tế.\"</p>"
        "<p>\"Loại tinh chất màu vàng mà họ gọi là Saponin MR2 thực chất là một loại hóa chất độc hại tự phân hủy, có chứa kim loại nặng và độc tố nấm mốc cực cao do quy trình sắc ký lỏng chắp vá lỗi thời của họ. Họ đã dùng loại thuốc độc này để thử nghiệm trái phép trên người bệnh nhân nặng tại Bệnh viện Quốc tế miền Nam, nhằm mục đích thổi phồng năng lực để lừa đảo dòng tiền đầu tư một trăm năm mươi tỷ đồng từ các cổ đông vô tội!\" Phong lớn tiếng buộc tội, đập mạnh tay xuống bàn đầy kịch tính.</p>"
        "<p>Ngay lập tức, gã luật sư Trần Hữu Luật trưng ra trước ống kính một văn bản có con dấu sao y bản chính: \"Chúng tôi đã gửi đơn tố cáo khẩn cấp lên cơ quan điều tra và Bộ Y tế. Đồng thời, chúng tôi cũng đã cung cấp bằng chứng cho thấy tài khoản thanh toán của liên minh Quân - Nhã Chi tại ngân hàng Agribank chi nhánh Phú Mỹ Hưng có những dòng tiền bất minh chạy qua các công ty ma ở nước ngoài để rửa tiền dơ bẩn.\""
        "<p>Cơn bão dư luận lập tức bùng nổ dữ dội như một vụ nổ hạt nhân trên mạng xã hội. Hàng chục ngàn bình luận giận dữ, chửi bới, đòi tẩy chay tập đoàn Lâm Gia và bắt giữ Trịnh Đình Quân xuất hiện ngập tràn dưới buổi phát sóng. Các trang báo mạng lá cải liên tục giật tít câu khách: \"Chấn động vụ lừa đảo Sâm Ngọc Linh nghìn tỷ\", \"Kỹ sư quèn dùng thuốc độc thử nghiệm trên người tài phiệt\"...</p>"
        "<p>Sáng hôm sau, lúc tám giờ ba mươi phút, bế tắc thực sự chính thức ập đến văn phòng của Lâm Nhã Chi tại tòa tháp Bitexco Sài Gòn. Điện thoại bàn reo liên tục không ngừng nghỉ, các trợ lý chạy ra chạy vào với gương mặt tái mét cắt không còn giọt máu.</p>"
        "<p>\"Tổng Giám đốc Nhã Chi! Có biến lớn rồi!\" Trương Minh Khoa, trưởng phòng phân tích tài chính hớt hải chạy vào phòng làm việc, mồ hôi lạnh đầm đìa ướt đẫm cả cổ áo sơ mi.</p>"
        "<p>\"Tài khoản giao dịch chính của liên minh chúng ta tại Agribank chi nhánh Phú Mỹ Hưng — nơi chứa một trăm năm mươi tỷ đồng vốn đầu tư giai đoạn một — đã bị đóng băng phong tỏa tạm thời theo quyết định khẩn cấp của Cơ quan Thanh tra Giám sát Ngân hàng địa phương để phục vụ điều tra rửa tiền dơ bẩn!\"</p>"
        "<p>\"Đồng thời, một đoàn kiểm tra liên ngành đột xuất gồm Quản lý thị trường, Thanh tra Bộ Y tế và Cảnh sát môi trường vừa ập vào phong tỏa niêm phong toàn bộ nhà máy pilot chiết xuất của chúng ta tại Khu công nghệ cao Đà Nẵng. Họ áp dụng lệnh đình chỉ hoạt động khẩn cấp trong vòng hai mươi bốn giờ để thanh tra toàn diện sai phạm vệ sinh an toàn dược phẩm sinh học!\"</p>"
        "<p>Cả căn phòng làm việc chìm vào sự im lặng đáng sợ. Cổ phiếu của tập đoàn Lâm Gia trên sàn chứng khoán bắt đầu bị bán tháo ồ ạt, giá trị vốn hóa bốc hơi hàng trăm tỷ đồng chỉ trong vòng mười lăm phút đầu phiên giao dịch.</p>"
        "<p>Đối tác lớn quay lưng, các quỹ đầu tư mạo hiểm từ Singapore liên tục gửi email yêu cầu rút vốn phòng ngừa rủi ro pháp lý. Toàn bộ dự án tâm huyết của Quân và Nhã Chi dường như đang đứng trước bờ vực của sự sụp đổ hoàn toàn chỉ trong chớp mắt.</p>"
        "<p>Nhã Chi ngồi lặng lẽ trước màn hình máy tính hiển thị các chỉ số tài chính đỏ rực như máu. Gương mặt cô vẫn giữ được vẻ lạnh lùng sắc sảo, nhưng hai bàn tay cô đã siết chặt lại đến mức móng tay rỉ máu trên mặt bàn da thuộc cao cấp.</p>"
        "<p>Cô quay sang nhìn Quân đang đứng tựa lưng vào tường kính, nhìn dòng sông Sài Gòn chảy lặng lờ dưới nắng trưa. Giọng nói của cô trầm xuống đầy lo lắng.</p>"
        "<p>\"Anh Quân... Chúng ta chỉ còn đúng hai mươi ba giờ trước khi Phong Cát Pharma tổ chức đại hội cổ đông IPO lịch sử tại trung tâm hội nghị Gem Center để chính thức niêm yết và hợp thức hóa công thức cướp được.\"</p>"
        "<p>\"Nếu trong vòng hai mươi tư giờ này, chúng ta không thể dỡ bỏ lệnh phong tỏa tài khoản và chứng minh được sự trong sạch của dòng tiền, dự án của chúng ta sẽ bị chôn vùi vĩnh viễn, và anh... có thể phải đối mặt với lệnh bắt giữ tạm giam của công an.\"</p>"
        "<p>Quân quay lại, nhìn thẳng vào mắt Nhã Chi. Ánh mắt anh không hề có một chút sợ hãi hay nao núng nào, ngược lại nó tĩnh lặng như mặt nước hồ đêm trên núi Ngọc Linh.</p>"
        "<p>\"Hai mươi tư giờ... Thế là quá đủ cho một màn kết thúc hoàn hảo,\" Quân khẽ mỉm cười đầy tự tin, cất giọng vô cùng trầm ổn và uy lực. \"Nhã Chi, hãy kích hoạt bước tiếp theo của kế hoạch. Tôi sẽ cho Đoàn Thế Phong biết thế nào là cái giá của sự phản phản bội thực sự.\""
    )
    
    # CHAPTER 6
    ch6_title = "Chương 6: Bản Án Từ Nhật Ký Git Và Camera Ẩn"
    ch6_content = (
        "<p>Trong căn phòng làm việc bí mật của ban pháp chế tập đoàn Lâm Gia, bầu không khí vô cùng tập trung và khẩn trương. Dù tài khoản bị phong tỏa và nhà máy bị đình chỉ hoạt động hai mươi bốn giờ, cả Trịnh Đình Quân và Lâm Nhã Chi đều không hề có một chút hoảng loạn nào. Họ đang nắm giữ những quân bài tẩy tối thượng để lật ngược thế cờ vào phút chót.</p>"
        "<p>Nhã Chi cùng đội ngũ luật sư tài chính hàng đầu Việt Nam phối hợp với công ty kiểm toán độc lập PwC (Big 4) thức trắng đêm để thực hiện một cuộc rà soát pháp lý toàn diện đối với dòng tiền của dự án Phong Cát Pharma.</p>"
        "<p>\"Chúng ta đã có kết quả kiểm toán dòng tiền từ PwC, anh Quân,\" Nhã Chi đẩy về phía anh tập tài liệu dày cộp bọc da đen đóng dấu đỏ chói của công ty kiểm toán hàng đầu thế giới. \"Đúng như anh dự đoán, dòng tiền hai mươi tỷ đồng chảy vào tài khoản của Đoàn Thế Phong tại Agribank không phải là tiền đầu tư hợp pháp.\"</p>"
        "<p>\"Đó là khoản tiền hối lộ trực tiếp từ tập đoàn hóa chất ngoại bang Meridian Chem Corp để mua đứt công thức thô của dự án Sâm Ngọc Linh, sau đó thông qua các công ty ma ở nước ngoài để rửa sạch tiền. Đây là bằng chứng thép đóng dấu đỏ chứng minh hành vi gian lận tài chính và rửa tiền của Phong Cát Pharma. Họ đã dùng chính số tiền này để hối lộ cho gã phó chánh thanh tra ký lệnh phong tỏa khống đối với chúng ta.\""
        "<p>Quân khẽ gật đầu hài lòng, anh kết nối chiếc ổ cứng bọc thép di động vào hệ thống máy chiếu lớn của phòng họp.</p>"
        "<p>\"Còn về mặt công nghệ, Đoàn Thế Phong nghĩ rằng hắn đã xóa sạch lịch sử trên máy chủ cục bộ của phòng lab Kon Tum là có thể cướp trắng công trình. Hắn không hề biết rằng máy chủ đó được tôi cấu hình đồng bộ hóa tự động hóa với kho lưu trữ Git riêng tư trên hệ thống GitHub Enterprise quốc tế từ năm năm trước.\", Quân giải thích, ngón tay gõ phím cực nhanh.</p>"
        "<p>Màn hình lớn hiện lên toàn bộ nhật ký commit Git của phần mềm điều khiển cột sắc ký lỏng. Mỗi dòng code thay đổi, mỗi chu kỳ nhiệt độ tăng giảm áp suất đều hiện rõ tên tác giả: \"Trịnh Đình Quân &lt;quandinh.trinh@biotech.org&gt;\" kèm theo mã khóa mật mã GPG cryptographically signed hợp lệ không thể chối cãi.</p>"
        "<p>\"Mỗi lần Phong cố gắng đăng nhập vào hệ thống để copy dữ liệu vào ban đêm, hệ thống giám sát an ninh tự động của tôi đã âm thầm ghi nhận toàn bộ địa chỉ IP và lưu trữ nhật ký commit thay đổi tác giả giả mạo dưới tên hắn. Hắn đã thực hiện dòng thay đổi tên tác giả cuối cùng vào lúc hai giờ sáng ngày mười lăm tháng năm mà không biết rằng mã khóa PGP ký số của hắn hoàn toàn không trùng khớp với chữ ký số gốc của tôi,\" Quân dõng dạc nói rõ ràng mạch lạc từng chi tiết.</p>"
        "<p>\"Đặc biệt, tôi còn giữ được thứ này.\" Quân bấm nút tiếp theo trên remote. Màn hình chuyển sang một đoạn video độ phân giải cao cực nét hắt ra từ camera ẩn được ngụy trang dưới dạng thiết bị báo khói trong phòng thí nghiệm HPLC.</p>"
        "<p>Video hiển thị rõ ràng hình ảnh Đoàn Thế Phong lén lút bước vào phòng lab lúc hai giờ sáng ngày mười lăm tháng năm. Hắn cẩn thận mở tủ tài liệu cá nhân của Quân bằng chìa khóa vạn năng, copy toàn bộ file thiết kế quy trình sắc ký vào một chiếc USB màu đỏ, sau đó cố tình dùng một ống nghiệm chứa hóa chất axit clohydric loãng nhỏ trực tiếp vào các cảm biến áp suất của cột HPLC nhằm hủy hoại toàn bộ các mẻ thử nghiệm đối chứng còn lại của Quân.</p>"
        "<p>Đoạn video cực kỳ chi tiết, ghi nhận toàn bộ biểu cảm xảo quyệt, nham hiểm của Phong cùng hành vi phá hoại tài sản nhà nước một cách không thể chối cãi. Ngón tay hắn run rẩy vì lo lắng, những giọt mồ hôi lạnh chảy dọc sống lưng in hằn trên lớp áo blouse trắng tinh khôi của hắn.</p>"
        "<p>Nhã Chi nhìn đoạn video, khóe môi cô khẽ cong lên một nụ cười lạnh lùng đầy sự khinh bỉ đối với kẻ phản bội tàn độc.</p>"
        "<p>\"Đoạn video này cộng với báo cáo kiểm toán đóng dấu đỏ của PwC và nhật ký commit Git bất biến sẽ là bản án tử hình pháp lý tàn khốc nhất dành cho Đoàn Thế Phong và Phong Cát Pharma ngay tại buổi lễ IPO của chúng ngày mai.\"</p>"
        "<p>\"Tôi đã gửi toàn bộ hồ sơ bằng chứng này lên Cục Cảnh sát Điều tra Tội phạm về Tham nhũng, Kinh tế, Buôn lậu (C03) của Bộ Công an. Sắc lệnh phê chuẩn lệnh bắt giữ khẩn cấp đối với Đoàn Thế Phong đã được C03 ký duyệt chính thức lúc mười một giờ đêm nay.\"</p>"
        "<p>Quân đứng dậy, thở ra một hơi dài, ánh mắt anh hướng về phía trung tâm hội nghị Gem Center Sài Gòn — nơi ngày mai sẽ diễn ra buổi đấu giá gọi vốn thế kỷ của kẻ phản bội.</p>"
        "<p>\"Đoàn Thế Phong, ngày mai tôi sẽ cho anh bước lên đỉnh cao nhất của vinh quang ảo ảnh, sau đó... chính tay tôi sẽ đẩy anh xuống vực thẳm sâu nhất không lối thoát của cuộc đời.\""
    )
    
    # CHAPTER 7
    ch7_title = "Chương 7: Buổi Thẩm Định IPO Nghẹt Thở"
    ch7_content = (
        "<p>Đại sảnh hội nghị lộng lẫy của trung tâm hội nghị năm sao Gem Center Sài Gòn chật kín không còn một chỗ trống. Ánh sáng từ hàng ngàn bóng đèn chùm pha lê nhập khẩu lung linh chiếu sáng, tạo nên một không gian vô cùng xa hoa và rực rỡ.</p>"
        "<p>Hàng trăm nhà đầu tư lớn, đại diện các quỹ tài chính đa quốc gia, giới truyền thông báo chí trung ương cùng ban lãnh đạo Sở Giao dịch Chứng khoán đã có mặt đầy đủ để tham dự buổi thẩm định IPO lịch sử của tập đoàn Phong Cát Pharma. Sự kiện này được giới tài chính mong đợi như một bước ngoặt y sinh lớn nhất năm, hứa hẹn giá trị vốn hóa của Phong Cát sẽ tăng vọt lên mức hàng nghìn tỷ đồng ngay sau phiên giao dịch đầu tiên.</p>"
        "<p>Đoàn Thế Phong đứng ở trung tâm sân khấu lớn rực rỡ ánh đèn led nghệ thuật. Hắn mặc bộ vest ba mảnh lịch lãm đặt may riêng từ Anh Quốc, mái tóc vuốt gel bóng mượt, khuôn mặt tràn đầy sự đắc ý và kiêu ngạo tột đỉnh. Trên màn hình led khổng lồ phía sau hắn là hình ảnh biểu trưng của giọt tinh chất Sâm Ngọc Linh Gold Saponin, đi kèm dòng chữ nổi bật: \"Công nghệ chiết xuất tế bào gốc độc quyền — Phát minh bởi Giáo sư Đoàn Thế Phong\".</p>"
        "<p>\"Kính thưa quý vị quan khách,\" Phong cất giọng dõng dạc đầy tự tin trước micro, tiếng nói vang vọng khắp đại sảnh rộng lớn. \"Công nghệ chiết xuất Saponin MR2 thế hệ mới của chúng tôi đã hoàn thiện, đạt hiệu suất chiết xuất tối ưu chín mươi tám phần trăm tinh khiết. Đây là phát minh mang tính cách mạng của cá nhân tôi sau mười năm nghiên cứu miệt mài tại vùng núi Ngọc Linh Kon Tum.\"</p>"
        "<p>\"Với công nghệ này, Phong Cát Pharma tự tin sẽ dẫn đầu thị trường dược phẩm sinh học Đông Nam Á, mang lại nguồn lợi nhuận khổng lồ lên tới hàng trăm triệu đô la mỗi năm cho các nhà đầu tư đồng hành cùng chúng tôi hôm nay. Mức giá chào sàn dự kiến sẽ là bảy mươi lăm ngàn đồng một cổ phiếu, và tôi tin tưởng chắc chắn...\"</p>"
        "<p>\"Hồ sơ đăng ký sáng chế của anh là giả mạo! Quy trình sắc ký lỏng nhiệt trị đó hoàn toàn là công sức ăn cắp trắng trợn từ kỹ sư Trịnh Đình Quân!\"</p>"
        "<p>Một giọng nói trầm ấm nhưng vô cùng uy nghiêm, chứa đựng nội lực thâm hậu bất ngờ vang lên từ phía cửa chính của đại sảnh hội nghị, cắt ngang lời nói ngạo mạn của Phong.</p>"
        "<p>Cả hội trường rộng lớn ồ lên kinh ngạc tột độ. Hàng trăm vị khách đồng loạt quay đầu lại nhìn ra cửa sảnh chính. Cửa sảnh lớn mở toang, Trịnh Đình Quân đĩnh đạc bước vào trong bộ vest xám lịch lãm, phong thái vô cùng đĩnh đạc và uy nghi của một đấng trượng phu.</p>"
        "<p>Đi bên cạnh anh là Lâm Nhã Chi — cô ái nữ lý tính của tập đoàn Lâm Gia trong chiếc đầm đen công sở sang trọng đầy khí chất quyến đoán. Phía sau họ là một nhóm chuyên gia kiểm toán công nghệ cao cấp của PwC (Big 4) cùng bốn sĩ quan cảnh sát điều tra kinh tế mặc thường phục của cơ quan C03 Bộ Công an.</p>"
        "<p>Đoàn Thế Phong đờ đẫn cả người trên sân khấu, sắc mặt hắn lập tức chuyển từ hồng hào sang xám ngoét không còn một giọt máu khi nhìn thấy sự xuất hiện của Quân và Nhã Chi. Hàm hắn run nhẹ, chiếc nhẫn ngọc bích trên ngón tay bỗng trở nên lạnh lẽo lạ thường.</p>"
        "<p>\"Mày... Trịnh Đình Quân? Mày chỉ là một thằng kỹ sư bị sa thải, lấy tư cách gì mà dám vào đây gây rối trật tự? Bảo vệ đâu! Đuổi toàn bộ bọn chúng ra ngoài ngay lập tức!\" bà Cao Lệ Thu ngồi ở hàng ghế đầu vip đứng bật dậy chỉ tay quát tháo đầy giận dữ.</p>"
        "<p>\"Ai dám đuổi đại diện hợp pháp của tập đoàn Lâm Gia và các chiến sĩ cơ quan điều tra kinh tế Bộ Công an đang thi hành sắc lệnh của pháp luật?\" Nhã Chi bước lên phía trước, giọng nói trong trẻo nhưng lạnh lùng sắc bén như dao cạo vang lên đanh thép.</p>"
        "<p>Cô đưa mắt ra hiệu cho chuyên gia PwC kết nối trực tiếp hệ thống máy tính của họ với màn hình led khổng lồ của hội trường thông qua đường truyền mạng không dây bảo mật cấp độ cao.</p>"
        "<p>\"Đoàn Thế Phong, anh nghĩ rằng chỉ cần xóa sạch lịch sử sắc ký trên máy chủ cục bộ là có thể cướp trắng công trình nghiên cứu sao?\" Quân bước thẳng lên bục sân khấu chính, đứng đối diện trực tiếp với kẻ phản bội đang run rẩy đứng đó dưới ánh đèn sân khấu chói lọi.</p>"
        "<p>\"Hãy nhìn lên màn hình lớn và xem kỹ sự thật bất biến của tri thức y học chân chính trông như thế nào!\" Quân lớn tiếng dõng dạc tuyên bố.</p>"
    )
    
    # CHAPTER 8
    ch8_title = "Chương 8: Vả Mặt Liên Hoàn Và Bản Án Cho Kẻ Phản Bội"
    ch8_content = (
        "<p>Màn hình led khổng lồ năm trăm inch của trung tâm hội nghị Gem Center bừng sáng. Toàn bộ hình ảnh thiết kế slide IPO hào nhoáng của Phong Cát Pharma biến mất hoàn toàn, thay vào đó là những dòng nhật ký commit Git màu xanh lục sắc nét chạy dọc màn hình.</p>"
        "<p>\"Đây là toàn bộ lịch sử commit Git bất biến của thuật toán điều khiển cột sắc ký lỏng tự động hóa, được lưu trữ trên máy chủ GitHub Enterprise quốc tế từ năm năm trước,\" Quân cất giọng rõ ràng mạch lạc vang vọng khắp hội trường im phăng phắc.</p>"
        "<p>\"Mỗi dòng commit code cốt lõi từ năm 2021 đến nay đều được ký số mật mã bằng khóa GPG cá nhân hợp pháp của tôi — Trịnh Đình Quân. Và đây... lịch sử commit giả mạo do Đoàn Thế Phong thực hiện lúc hai giờ sáng ngày mười lăm tháng năm, có chữ ký số hoàn toàn không trùng khớp, chứng minh hành vi sửa đổi dữ liệu bất hợp pháp của hắn.\""
        "<p>Cả hội trường xôn xao dữ dội như ong vỡ tổ. Các nhà đầu tư lớn há hốc miệng kinh ngạc, liên tục dùng điện thoại chụp lại màn hình làm chứng cứ pháp lý. Đoàn Thế Phong đứng đó, đầu gối hắn run rẩy bủn rủn quỵ xuống sàn sân khấu, hai tay bám chặt vào bục gỗ để khỏi ngã quỵ.</p>"
        "<p>\"Chưa hết! Hãy xem kỹ cách Đoàn Thế Phong 'nghiên cứu' công nghệ độc quyền này như thế nào trong đêm mưa gió bão bùng!\" Quân bấm nút tiếp theo trên remote điều khiển.</p>"
        "<p>Đoạn video camera ẩn siêu nét hiện ra trên màn hình lớn. Cả hội trường nín thở chứng kiến cảnh tượng Đoàn Thế Phong lén lút như một tên trộm bẻ khóa tủ tài liệu cá nhân của Quân, cướp đoạt dữ liệu vào USB màu đỏ, sau đó nhẫn tâm nhỏ axit phá hoại cảm biến cột HPLC HPLC của viện nghiên cứu Kon Tum.</p>"
        "<p>\"Và đây là báo cáo kiểm toán dòng tiền chính thức đóng dấu đỏ của PwC và Cục Phòng chống rửa tiền của Ngân hàng Nhà nước,\" Lâm Nhã Chi bước lên sân khấu đứng bên cạnh Quân, giọng điệu sắc sảo vô cùng dứt khoát.</p>"
        "<p>\"Toàn bộ số tiền hai mươi tỷ đồng chảy vào tài khoản của Đoàn Thế Phong tại Agribank thực chất là tiền hối lộ rửa tiền từ tập đoàn hóa chất Meridian Chem Corp. Chúng tôi cũng đã có đầy đủ văn bản chính thức của Cục Sở hữu Trí tuệ Việt Nam ký duyệt sáng nay, bác bỏ hoàn toàn hồ sơ đăng ký sáng chế của Đoàn Thế Phong và cấp bằng sáng chế độc quyền quy trình chiết xuất Saponin MR2 hoạt hóa tế bào gốc cho kỹ sư Trịnh Đình Quân!\"</p>"
        "<p>Tiếng xì xào phẫn nộ bùng nổ dữ dội khắp cả hội trường. Hàng trăm nhà đầu tư đồng loạt đứng dậy tức giận, ném các tờ rơi giới thiệu IPO của Phong Cát Pharma xuống sàn nhà rào rào. Bà Cao Lệ Thu sắc mặt xám ngoét không còn giọt máu, ngực phập phồng thở dốc rồi ngã sụp xuống hàng ghế VIP vì đột quỵ do huyết áp tăng vọt cực độ.</p>"
        "<p>Thượng úy Nguyễn Minh Cường — đại diện sĩ quan cảnh sát điều tra C03 Bộ Công an bước lên sân khấu, giơ cao văn bản đóng dấu đỏ chói trước mặt Đoàn Thế Phong.</p>"
        "<p>\"Đoàn Thế Phong! Theo quyết định khởi tố và phê chuẩn lệnh bắt tạm giam số 2026-C03-PC-0847 của Viện Kiểm sát Nhân dân Tối cao ký duyệt khẩn cấp đêm qua, anh bị bắt giữ ngay lập tức về hành vi lừa đảo chiếm đoạt tài sản, hủy hoại tài sản nhà nước và vi phạm quy định về sở hữu trí tuệ dược phẩm sinh học. Anh có quyền giữ im lặng và có quyền có luật sư trước tòa!\"</p>"
        "<p>Tiếng \"tách\" vang khô khốc của chiếc còng số tám bằng thép không gỉ khóa chặt hai cổ tay của Đoàn Thế Phong ngay trước sự chứng kiến trực tiếp của hàng trăm ống kính phóng viên báo chí và đài truyền hình trung ương đang phát sóng trực tiếp.</p>"
        "<p>Hắn khóc lóc thảm thiết bủn rủn chân tay, mồ hôi lạnh chảy đầm đìa ướt đẫm cả bộ vest đắt tiền, đầu gối quỵ hẳn xuống sàn gỗ sân khấu run bần bật như một con chó hoang dại bị dồn vào chân tường không còn đường thoát. Toàn bộ đế chế giấy lừa đảo nghìn tỷ của Phong Cát Pharma đã sụp đổ tan tành hoàn toàn chỉ trong vòng mười lăm phút phản kích đanh thép của Quân.</p>"
        "<p>Chiều muộn hôm đó, sau khi cơn bão pháp lý và truyền thông đã tạm lắng dịu, Trịnh Đình Quân và Lâm Nhã Chi cùng nhau dạo bước trong khuôn viên tĩnh lặng của vườn bách thảo dinh độc lập cũ tại trung tâm Sài Gòn. Ánh nắng hoàng hôn vàng óng hắt qua những vòm lá cổ thụ xanh mướt, tạo nên một không gian vô cùng bình yên và lãng mạn.</p>"
        "<p>Họ dừng lại bên một chiếc ghế đá cổ kính, xung quanh là hương thơm dịu nhẹ của các loài kỳ hoa dị thảo phương Nam.</p>"
        "<p>Nhã Chi quay sang nhìn Quân, đôi mắt sắc sảo lý tính thường ngày của cô bỗng hiện lên một tia nhìn vô cùng dịu dàng, ấm áp và chứa chan tình cảm sâu sắc.</p>"
        "<p>\"Anh Quân... Mọi thủ tục do ban pháp chế kiểm tra năng lực pháp lý đối với hợp đồng đầu tư một trăm năm mươi tỷ đã hoàn thành hoàn mỹ tuyệt đối.\" cô khẽ mỉm cười, giọng nói trầm xuống đầy cảm xúc ngọt ngào.</p>"
        "<p>\"Nhưng tối nay... tôi không muốn nói với anh về công việc kinh doanh hay những điều khoản hợp đồng khô khan nữa. Tôi muốn hỏi anh... với tư cách cá nhân của một người phụ nữ đã cùng anh trải qua sinh tử giông bão.\""
        "<p>Quân nhẹ nhàng nắm lấy bàn tay mềm mại ấm áp của Nhã Chi, nhìn sâu vào đôi mắt thông tuệ của cô ái nữ lý tính: \"Nhã Chi, tôi biết em muốn nói gì. Tri thức của tôi có thể chế tạo ra những liều thuốc cứu sống hàng triệu người, nhưng chỉ có em... mới là người giữ lại được sự ấm áp chân chính nhất trong tâm hồn của tôi.\""
        "<p>\"Tôi yêu em, không phải vì em là ái nữ nhà giàu quyền lực, mà vì em chính là người duy nhất thấu hiểu, trân trọng và bảo vệ tri thức chân chính của tôi bằng sự sòng phẳng và lý tính tuyệt vời nhất.\"</p>"
        "<p>Nhã Chi tựa đầu vào vai Quân, những hạt nắng cuối ngày nhuộm vàng đôi bờ vai họ như một bức tranh nghệ thuật tuyệt mỹ. Liên minh thép của họ nay đã đơm hoa kết trái thành một tình yêu vĩ đại, bền chặt không một giông bão nào có thể lay chuyển nổi trên thế gian này.</p>"
    )
    
    chapters.append({"title": ch1_title, "content": ch1_content})
    chapters.append({"title": ch2_title, "content": ch2_content})
    chapters.append({"title": ch3_title, "content": ch3_content})
    chapters.append({"title": ch4_title, "content": ch4_content})
    chapters.append({"title": ch5_title, "content": ch5_content})
    chapters.append({"title": ch6_title, "content": ch6_content})
    chapters.append({"title": ch7_title, "content": ch7_content})
    chapters.append({"title": ch8_title, "content": ch8_content})
    
    novel_data = {
        "title": title,
        "author": author,
        "genre": genre,
        "intro": intro,
        "cover_prompt": cover_prompt,
        "chapters": chapters
    }
    
    output_path = "/Users/aaronnguyen/TN/App/doctieuthuyet/pending_novel.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(novel_data, f, ensure_ascii=False, indent=2)
    print("✓ Successfully generated pending_novel.json with 8 high-quality chapters!")

if __name__ == "__main__":
    generate()
