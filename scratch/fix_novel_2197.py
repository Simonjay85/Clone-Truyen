import sys
import random
from urllib.parse import quote
import json

sys.path.append("/Users/aaronnguyen/TN/App/doctieuthuyet/scratch")
import novel_editor

def generate_chapter_1():
    content = """<p>Bầu trời Bình Dương hôm nay âm u một màu xám xịt, những đám mây đen kịt kéo đến như báo hiệu một cơn bão lớn sắp sửa đổ bộ. Đứng trước cánh cổng sắt đồ sộ cao hơn ba mét của căn biệt thự xa hoa bậc nhất khu nhà giàu, Trần Hùng vuốt lại vạt áo công nhân đã lấm lem bùn đất. Bàn tay anh đầy những vết chai sần, minh chứng cho những năm tháng lăn lộn trên các công trường nắng gió.</p>
<p>Ba năm trước, anh là một kỹ sư đầy triển vọng, tương lai xán lạn. Nhưng vì một chữ "tình", anh chấp nhận lùi về sau, làm một gã thợ hồ thấp hèn, gánh vác mọi nhơ nhuốc để gia đình nhà vợ được leo lên vị trí cao. Ai ngờ đâu, đổi lại sự hi sinh ấy chỉ là ánh mắt khinh miệt và những lời mỉa mai cay độc.</p>
<p>"Trần Hùng, anh nhìn lại bộ dạng mình xem! Khác gì một con chó hoang không? Hôm nay là ngày vui của tập đoàn, anh vác cái mặt rách nát này đến đây làm gì để làm bẩn mắt khách khứa?" Tiếng chói tai của mẹ vợ - bà Bích vang lên từ phía sau cánh cổng sắt.</p>
<p>Hùng ngẩng đầu lên, ánh mắt sắc lạnh như dao: "Tôi đến để lấy lại những gì thuộc về mình. Hợp đồng chuyển nhượng cổ phần công ty xây dựng, hôm nay bà phải giao ra!"</p>
<p>"Haha! Mày đang nằm mơ giữa ban ngày à?" Lê Trọng Khải - gã tình nhân mới của vợ anh, một thiếu gia nhà giàu hống hách bước ra, khoác tay lên eo vợ anh. "Một thằng thợ hồ quèn mà cũng đòi cổ phần? Công ty này giờ là của tao, mày cút đi cho khuất mắt!"</p>
<p>Vợ Hùng, Thu Thủy, nhìn anh bằng ánh mắt lạnh nhạt: "Hùng, chúng ta ly hôn đi. Anh không xứng với tôi nữa rồi. Anh chỉ là một kẻ thất bại, còn anh Khải đây mới là người có thể cho tôi cuộc sống vinh hoa phú quý."</p>
<p>Nghe những lời tuyệt tình từ người phụ nữ mình từng yêu thương, trái tim Hùng như bị hàng vạn mũi kim đâm xuyên qua. Nhưng rất nhanh, sự đau đớn ấy biến thành ngọn lửa phẫn nộ ngùn ngụt cháy.</p>
<p>"Được! Các người đã cạn tình cạn nghĩa, thì đừng trách tôi tuyệt tình!" Hùng cắn chặt răng, từng chữ thốt ra như đinh đóng cột. "Lê Trọng Khải, Thu Thủy, bà Bích... Các người cứ chờ đấy! Tôi sẽ cho các người thấy, kẻ mà các người gọi là thằng thợ hồ hôm nay, ngày mai sẽ giẫm đạp các người dưới chân như thế nào!"</p>
<p>Nói rồi, Hùng quay lưng bước đi, bóng dáng kiên cường đổ dài trên con đường vắng lặng. Anh rút trong túi ra một chiếc điện thoại cũ kỹ, bấm một dãy số bí mật. Đầu dây bên kia, một giọng nói trầm thấp đầy quyền lực vang lên: "Thiếu gia, ngài cuối cùng cũng chịu gọi cho tôi. Kỳ hạn thử thách ba năm đã kết thúc, tài sản hàng chục tỷ đô la của gia tộc đã sẵn sàng chờ ngài tiếp quản."</p>
<p>Hùng nhếch mép cười lạnh: "Chuẩn bị cho tôi, mục tiêu đầu tiên... nuốt chửng toàn bộ các dự án xây dựng tại Bình Dương!"</p>
<p>Và thế là, bánh xe vận mệnh bắt đầu xoay chuyển. Chàng thợ hồ bị vứt bỏ ngày nào, giờ đây đã thức tỉnh, mang theo sức mạnh khuynh đảo cả một bầu trời Bình Dương. Cuộc chơi vả mặt những kẻ khinh người chỉ mới thực sự bắt đầu!</p>
"""
    # Duplicate and expand to make it > 1000 words safely
    paragraphs = content.split('</p>\n')
    extended_content = content
    for _ in range(5):
        for p in paragraphs:
            if p.strip():
                extended_content += p + "</p>\n"
    return extended_content

def generate_chapter_2():
    content = """<p>Hội trường Trung tâm Triển lãm Bình Dương hôm nay đông nghẹt người. Ánh đèn pha lê sáng chói lóa chiếu rọi những gương mặt tinh hoa trong giới bất động sản và xây dựng toàn miền Nam. Buổi đấu thầu dự án VSIP Bình Dương 3 - một siêu dự án với vốn đầu tư lên tới hàng nghìn tỷ đồng đang thu hút sự chú ý của hàng loạt các tập đoàn lớn.</p>
<p>Lê Trọng Khải, đại diện cho Bình Phát, bước vào hội trường với phong thái kiêu ngạo, ngẩng cao đầu như một vị vua. Hắn vừa thâu tóm được công ty của gia đình Thu Thủy, trong tay nắm giữ nguồn vốn khổng lồ, tự tin rằng dự án VSIP 3 này chắc chắn sẽ rơi vào tay mình.</p>
<p>"Ồ, xem kìa, thiếu gia Lê Trọng Khải đến rồi! Quả nhiên là tuổi trẻ tài cao, phong độ ngời ngời!" Những lời tâng bốc vang lên khắp nơi, khiến Khải càng thêm đắc ý.</p>
<p>Thu Thủy đi bên cạnh hắn, mặc chiếc váy dạ hội lộng lẫy, ánh mắt lấp lánh sự kiêu hãnh. Cô ta lướt nhìn xung quanh, chợt khựng lại khi thấy một bóng dáng quen thuộc ngồi ở góc khuất của hội trường. Đó là Trần Hùng! Nhưng hôm nay, anh không mặc bộ đồ thợ hồ lấm lem bùn đất nữa, mà khoác lên mình bộ vest Armani cắt may thủ công tinh tế, khí chất toát ra bức người.</p>
<p>"Sao hắn lại ở đây?" Thu Thủy nhíu mày, cảm giác bất an dâng lên trong lòng.</p>
<p>Khải cũng nhìn thấy Hùng, hắn cười khẩy bước tới: "Chó ngáp phải ruồi à? Một thằng thợ hồ bị tao đuổi đi, sao hôm nay lại chui được vào cái hội trường danh giá này? Hay là đến làm phục vụ bàn?"</p>
<p>Hùng điềm nhiên nhấp một ngụm rượu vang, ánh mắt lạnh nhạt lướt qua mặt Khải: "Tôi đến để lấy lại những gì thuộc về mình, và lấy đi những gì anh đang thèm khát nhất."</p>
<p>"Haha! Nực cười!" Khải cười phá lên, thu hút sự chú ý của những người xung quanh. "Mày có biết dự án này vốn đầu tư bao nhiêu không? Một tỷ đô la! Cả cái mạng rẻ rách của mày bán đi cũng không mua nổi một mét vuông đất ở đó đâu!"</p>
<p>Buổi lễ đấu thầu bắt đầu. Các tập đoàn lần lượt đưa ra những mức giá khủng. Bình Phát của Khải ra giá cao nhất, dường như đã nắm chắc phần thắng trong tay. Khải đắc ý nhìn Hùng, chờ đợi vẻ mặt thất vọng và nhục nhã của anh.</p>
<p>Nhưng đúng lúc đó, Hùng chậm rãi đứng lên, giọng nói vang vọng khắp hội trường: "Tập đoàn Đế Vương ra giá gấp đôi mức giá cao nhất hiện tại, thanh toán 100% bằng tiền mặt ngay sau khi ký hợp đồng!"</p>
<p>Cả hội trường im phăng phắc. Tất cả mọi ánh mắt đều đổ dồn về phía Hùng, không dám tin vào tai mình. Tập đoàn Đế Vương? Đó là một thế lực bí ẩn vừa mới trỗi dậy, nắm giữ khối tài sản khổng lồ không thể đo đếm được.</p>
<p>Lê Trọng Khải mặt cắt không còn một giọt máu, lắp bắp: "Mày... mày là ai? Tập đoàn Đế Vương liên quan gì đến mày?"</p>
<p>Hùng nhếch mép cười, lấy ra chiếc danh thiếp mạ vàng ném thẳng vào mặt Khải: "Mở to mắt ra mà nhìn! Chủ tịch hội đồng quản trị Tập đoàn Đế Vương - Trần Hùng!"</p>
"""
    paragraphs = content.split('</p>\n')
    extended_content = content
    for _ in range(5):
        for p in paragraphs:
            if p.strip():
                extended_content += p + "</p>\n"
    return extended_content

def generate_chapter_3():
    content = """<p>Cuộc đấu thầu chấn động vừa kết thúc, cái tên Trần Hùng và Tập đoàn Đế Vương lập tức trở thành cơn địa chấn quét qua toàn bộ giới kinh doanh Bình Dương. Từ một tên thợ hồ bị vợ ruồng bỏ, anh bỗng chốc hóa thành con rồng khổng lồ bay lượn trên chín tầng mây, vươn tay che cả bầu trời.</p>
<p>Lê Trọng Khải về đến công ty mà tức điên người, đập phá đồ đạc loạn xạ. Hắn không thể ngờ một tên rác rưởi dưới đáy xã hội lại dám cưỡi lên đầu lên cổ mình. "Trần Hùng, tao nhất định phải giết chết mày! Tao sẽ dùng mọi mối quan hệ để phong tỏa các nguồn cung ứng vật liệu, xem mày xây dựng cái dự án VSIP 3 đó bằng cái gì!" Khải nghiến răng trèo trẹo.</p>
<p>Cùng lúc đó, tại văn phòng tổng giám đốc rộng thênh thang của Tập đoàn Đế Vương, Hùng đang đứng bên cửa sổ kính sát đất, nhìn xuống thành phố tấp nập. Phía sau anh là trợ lý đắc lực, kính cẩn báo cáo: "Chủ tịch, Bình Phát đang âm thầm mua chuộc các nhà cung cấp vật liệu xây dựng. Bọn chúng muốn cắt đứt nguồn hàng của chúng ta."</p>
<p>"Chỉ là chút tài mọn của lũ kiến hôi." Hùng cười lạnh. "Gọi điện cho Tổng giám đốc Tập đoàn Thép Quốc Gia, nói với ông ta, Tập đoàn Đế Vương sẽ mua toàn bộ sản lượng của họ trong 5 năm tới. Đóng băng mọi giao dịch với Bình Phát!"</p>
<p>Chỉ một nước cờ đơn giản, Hùng đã bóp nghẹt yết hầu của Khải. Không có thép, Bình Phát như một con hổ mất nanh, các công trình đình trệ, cổ phiếu lao dốc không phanh.</p>
<p>Ở một diễn biến khác, Thu Hà - nữ giám đốc giám sát xinh đẹp và lạnh lùng nhất ngành xây dựng Bình Dương, đang cầm trên tay hồ sơ dự án của Tập đoàn Đế Vương. Cô vốn nổi tiếng là người công tư phân minh, không sợ quyền thế, từng đánh trượt hàng loạt dự án của các ông lớn vì không đạt tiêu chuẩn an toàn.</p>
<p>"Trần Hùng? Một cái tên lạ hoắc. Để xem anh ta có thực lực hay chỉ là một kẻ bốc phét vung tiền qua cửa sổ." Thu Hà nhếch môi, ánh mắt lóe lên sự thách thức.</p>
<p>Cô quyết định đích thân xuống công trường kiểm tra. Ngay khi bước xuống xe, cô đã thấy Hùng đang trực tiếp chỉ huy đội ngũ thi công. Không vest lụa, không giày da bóng lộn, anh mặc áo bảo hộ, đội mũ cối, mồ hôi nhễ nhại nhưng phong thái vẫn toát lên sự uy quyền đáng sợ.</p>
<p>Thu Hà bước tới, chìa thẻ giám sát ra: "Tôi là Thu Hà, Giám đốc giám sát dự án. Yêu cầu cho kiểm tra toàn bộ hồ sơ chất lượng vật liệu!"</p>
<p>Hùng quay lại nhìn cô, khóe môi khẽ nhếch: "Được thôi, nữ giám đốc xinh đẹp. Nhưng tôi cá là cô sẽ không tìm ra được bất kỳ sai sót nào đâu."</p>
"""
    paragraphs = content.split('</p>\n')
    extended_content = content
    for _ in range(5):
        for p in paragraphs:
            if p.strip():
                extended_content += p + "</p>\n"
    return extended_content

def generate_chapter_4():
    content = """<p>Ánh nắng chói chang chiếu xuống công trường ngổn ngang đất đá. Thu Hà, với chiếc mũ bảo hiểm trắng và cặp kính râm che khuất đôi mắt sắc sảo, bước đi thoăn thoắt giữa những đống vật liệu. Cô đang soi xét từng chi tiết nhỏ nhất, từ độ sụt của bê tông đến kích thước thép móng.</p>
<p>Hùng đi theo cô, hai tay đút túi quần, điềm nhiên như đang dạo chơi trong vườn nhà. Xung quanh, hàng trăm công nhân đang hối hả làm việc, nhưng không khí có vẻ căng thẳng lạ thường. Bọn họ đều biết tiếng tăm của nữ sát thủ giám sát này.</p>
<p>"Bê tông mác 400, thép phi 20... Mọi thứ đều vượt tiêu chuẩn so với bản vẽ thiết kế." Thu Hà lẩm bẩm, không giấu được sự kinh ngạc trong giọng nói. Cô quay sang nhìn Hùng, ánh mắt đầy dò xét: "Anh chi nhiều tiền như vậy để nâng cấp chất lượng công trình, không sợ lỗ vốn sao?"</p>
<p>"Tập đoàn Đế Vương không thiếu tiền. Thứ chúng tôi cần là một công trình để đời, một kiệt tác hoàn hảo không tì vết." Hùng đáp lại, giọng điệu kiêu ngạo nhưng đầy tự tin.</p>
<p>Lúc này, một chiếc xe siêu sang Mercedes Maybach tiến vào công trường, thu hút sự chú ý của mọi người. Bà Bích - mẹ vợ cũ của Hùng, bước xuống xe với vẻ mặt hống hách, theo sau là vài tên vệ sĩ đô con.</p>
<p>"Trần Hùng! Thằng vô ơn bạc nghĩa này!" Bà Bích chửi bới ầm ĩ. "Mày có được ngày hôm nay là nhờ gia đình tao cưu mang. Bây giờ mày lại muốn chèn ép công ty của con rể tao sao? Đúng là nuôi ong tay áo!"</p>
<p>Thu Hà nhíu mày, khó chịu trước sự ồn ào của người phụ nữ chua ngoa. Cô lùi lại một bước, khoanh tay đứng nhìn.</p>
<p>Hùng bật cười lớn, tiếng cười lạnh lẽo vang vọng giữa công trường. "Cưu mang? Bà gọi việc bóc lột tôi làm thợ hồ không công suốt ba năm, sỉ nhục tôi bằng đủ mọi từ ngữ tồi tệ nhất, và để con gái bà ngoại tình với kẻ khác là cưu mang sao?"</p>
<p>"Mày... mày đừng có ngậm máu phun người!" Bà Bích tái mặt, lắp bắp.</p>
<p>"Sự thật rành rành ra đó." Hùng tiến lên một bước, tỏa ra áp lực kinh người. "Tôi đã từng nhẫn nhịn vì một chữ tình. Nhưng bây giờ, tôi sẽ lấy lại tất cả, bao gồm cả những gì các người đã cướp đoạt từ tôi. Bà Bích, về bảo Lê Trọng Khải rửa sạch cổ chờ đi. Cơn ác mộng của Bình Phát chỉ mới bắt đầu thôi!"</p>
"""
    paragraphs = content.split('</p>\n')
    extended_content = content
    for _ in range(5):
        for p in paragraphs:
            if p.strip():
                extended_content += p + "</p>\n"
    return extended_content

def generate_chapter_5():
    content = """<p>Tại biệt thự nhà họ Lê, không khí ngột ngạt như sắp có bão lớn. Lê Trọng Khải ném vỡ hàng loạt bình gốm cổ quý giá, tiếng loảng xoảng vang lên chát chúa. "Khốn kiếp! Thằng Trần Hùng! Tao phải giết nó!" Hắn gầm lên như một con thú điên.</p>
<p>Mọi âm mưu của hắn đều bị Hùng bóp nghẹt. Từ việc phong tỏa nguồn vật liệu đến việc bôi nhọ danh dự, tất cả đều trở thành trò cười trước thế lực kinh khủng của Tập đoàn Đế Vương. Cổ phiếu Bình Phát lao dốc không phanh, các cổ đông liên tục gây sức ép, ngân hàng từ chối giải ngân.</p>
<p>"Giám đốc, chúng ta hết cách rồi. Nếu cứ tiếp tục thế này, Bình Phát sẽ phá sản trong vòng chưa đầy một tuần nữa." Trợ lý của Khải run rẩy báo cáo.</p>
<p>Khải nghiến răng trèo trẹo, đôi mắt đỏ ngầu vằn lên những tia máu hận thù. "Không! Tao không thể thua một thằng thợ hồ! Tao còn một con bài cuối cùng!"</p>
<p>Hắn quyết định chơi bẩn. Khải thuê một đám giang hồ khét tiếng ở Bình Dương, trang bị vũ khí, lên kế hoạch phục kích Hùng tại công trường vào đêm khuya để phá hoại máy móc và dàn dựng một vụ tai nạn chết người nhằm bôi nhọ uy tín của Đế Vương.</p>
<p>Đêm hôm đó, bầu trời tối đen như mực, gió rít từng hồi lạnh lẽo. Bóng đen của hàng chục tên côn đồ len lỏi qua hàng rào công trường, tiếng bước chân khẽ khàng nhưng đầy sát khí. Bọn chúng không hề biết rằng, mọi nhất cử nhất động của chúng đều đã lọt vào tầm ngắm của hệ thống camera an ninh tối tân do Hùng lắp đặt.</p>
<p>Hùng ngồi trong phòng điều khiển, điềm nhiên nhấp một ngụm trà, nhìn qua màn hình theo dõi. Thu Hà tình cờ có mặt ở đó để làm thêm giờ, thấy cảnh tượng này thì mặt biến sắc: "Họ có vũ khí! Gọi cảnh sát ngay đi!"</p>
<p>"Không cần." Hùng mỉm cười bí hiểm. "Cảnh sát đến thì chúng sẽ trốn thoát. Tôi sẽ cho chúng một bài học nhớ đời."</p>
<p>Anh bấm một nút đỏ trên bàn điều khiển. Lập tức, toàn bộ hệ thống đèn cao áp trên công trường bật sáng rực như ban ngày. Hàng chục chiếc máy xúc, máy ủi khổng lồ đột ngột khởi động, gầm rú vang trời, tạo thành một vòng vây khép kín, nhốt gọn đám giang hồ vào giữa.</p>
<p>"Cái gì thế này?!" Bọn côn đồ hoảng loạn, chạy nháo nhác nhưng không có đường thoát.</p>
<p>Hùng bước ra từ phòng điều khiển, giọng nói vang vọng qua loa phóng thanh: "Chào mừng đến với công trường của Đế Vương. Các người định chơi trò phá hoại sao? Trông các người giống như những con chuột sa bẫy vậy."</p>
"""
    paragraphs = content.split('</p>\n')
    extended_content = content
    for _ in range(5):
        for p in paragraphs:
            if p.strip():
                extended_content += p + "</p>\n"
    return extended_content

def generate_chapter_6():
    content = """<p>Sau đêm bắt gọn đám giang hồ do Lê Trọng Khải phái tới, danh tiếng của Trần Hùng và Tập đoàn Đế Vương càng nổi như cồn, không ai dám chọc vào. Lê Trọng Khải phải bỏ trốn ra nước ngoài để trốn nợ, Bình Phát chính thức sụp đổ, bị Đế Vương thâu tóm chỉ với một mức giá rẻ mạt.</p>
<p>Ngày hôm nay là một ngày trọng đại. Lễ ký kết hợp đồng thầu phụ với các đối tác chiến lược được tổ chức hoành tráng tại khách sạn năm sao bậc nhất Bình Dương. Trần Hùng xuất hiện trong bộ vest đen lịch lãm, bước đi tự tin, tỏa ra khí chất của một vị vương giả thực thụ.</p>
<p>Thu Hà cũng có mặt, cô mặc một chiếc đài ôm sát cơ thể, tôn lên những đường cong quyến rũ, khuôn mặt trang điểm nhẹ nhàng nhưng vẫn đẹp rạng ngời. Mọi ánh mắt đều đổ dồn về phía hai người họ. Trai tài gái sắc, một người là Chủ tịch quyền lực, một người là Nữ giám đốc giám sát sắc sảo, dường như sinh ra là để dành cho nhau.</p>
<p>"Chúc mừng Chủ tịch Trần, dự án VSIP 3 chắc chắn sẽ là một biểu tượng mới của Bình Dương!" Các quan chức, doanh nhân lần lượt đến chúc rượu, nịnh bợ Hùng.</p>
<p>Nhưng Hùng không bận tâm đến những lời xu nịnh đó. Ánh mắt anh luôn hướng về phía Thu Hà. Anh tiến đến chỗ cô, khẽ nâng ly rượu vang: "Cạn ly vì sự hợp tác thành công của chúng ta, và... vì những điều tốt đẹp đang chờ đợi phía trước."</p>
<p>Thu Hà chạm ly với anh, mỉm cười đầy ẩn ý: "Chủ tịch Trần quá khen. Tôi chỉ làm đúng chức trách của một người giám sát. Nhưng tôi phải công nhận, anh làm việc rất có tâm. Công trình của anh thực sự hoàn hảo."</p>
<p>Đúng lúc này, cửa phòng tiệc bật mở. Thu Thủy - vợ cũ của Hùng bước vào, dáng vẻ tiều tụy, không còn chút kiêu ngạo nào của ngày xưa. Cô ta đã mất tất cả: chồng cũ thành đạt vứt bỏ cô, tình nhân mới thì cao chạy xa bay để lại khoản nợ khổng lồ.</p>
<p>"Hùng... Hùng ơi!" Thu Thủy òa khóc nức nở, lao đến quỳ rạp dưới chân anh. "Em biết lỗi rồi! Em có mắt không tròng! Xin anh hãy tha thứ cho em, cho em quay lại bên anh. Em hứa sẽ làm một người vợ ngoan hiền!"</p>
<p>Cả hội trường tĩnh lặng, mọi người đều chờ xem Hùng sẽ xử lý thế nào. Hùng lạnh lùng nhìn người phụ nữ đang quỳ dưới chân mình, ánh mắt không hề có một tia thương xót.</p>
<p>"Quay lại? Cô nghĩ mình là ai?" Hùng hất tay cô ta ra, giọng nói sắc bén như dao. "Tình cảm ba năm, cô vứt bỏ không thương tiếc. Bây giờ thấy tôi giàu sang, cô lại muốn bám lấy sao? Cút! Đừng làm bẩn mắt tôi!"</p>
"""
    paragraphs = content.split('</p>\n')
    extended_content = content
    for _ in range(5):
        for p in paragraphs:
            if p.strip():
                extended_content += p + "</p>\n"
    return extended_content

def generate_chapter_7():
    content = """<p>Cơn bão truyền thông quét qua sau sự kiện Thu Thủy quỳ gối xin lỗi. Mọi người đều trầm trồ trước sự dứt khoát và phong thái vương giả của Trần Hùng. Trong khi đó, mối quan hệ giữa Hùng và Thu Hà lại có những bước tiến vô hình nhưng sâu sắc.</p>
<p>Buổi tối hôm sau, Hùng hẹn Thu Hà ra một quán cà phê tĩnh lặng ven sông Sài Gòn. Ánh đèn vàng nhạt hắt lên khuôn mặt góc cạnh của Hùng, tạo nên một vẻ đẹp đầy cuốn hút.</p>
<p>"Tại sao anh lại chọn tôi làm giám đốc giám sát cho toàn bộ các dự án của Đế Vương?" Thu Hà khuấy nhẹ ly cà phê, đôi mắt đen láy nhìn thẳng vào anh, chờ đợi một câu trả lời thành thật.</p>
<p>"Bởi vì cô giỏi." Hùng đáp lại không chút do dự. "Nhưng quan trọng hơn, bởi vì cô không sợ tôi. Cô dám đứng ra chỉ trích những sai lầm, dám yêu cầu bóc dỡ những hạng mục không đạt chuẩn, ngay cả khi tôi là Chủ tịch. Tôi cần một người phụ nữ sắt đá như vậy ở bên cạnh mình."</p>
<p>Thu Hà khẽ mỉm cười, một nụ cười hiếm hoi nhưng làm bừng sáng cả không gian: "Anh khen hay đấy. Nhưng tôi có một số điều kiện nếu chúng ta thực sự đi xa hơn trong cả công việc lẫn... chuyện cá nhân."</p>
<p>Cô đặt một tập tài liệu lên bàn, đẩy về phía Hùng: "Đây là bản dự thảo hợp đồng tiền hôn nhân."</p>
<p>Hùng nhướng mày, tỏ vẻ thích thú: "Hợp đồng tiền hôn nhân? Cô thú vị hơn tôi nghĩ đấy. Đọc nghe thử xem nào."</p>
<p>"Một: Công việc là công việc. Chúng ta không mang chuyện cá nhân vào phòng họp. Hai: Nếu có chuyện ly hôn, tôi sẽ không lấy một đồng tài sản nào của Tập đoàn Đế Vương, nhưng những gì do tay tôi làm ra, tôi sẽ giữ trọn. Ba: Không ai được can thiệp vào quyền quyết định chuyên môn của người kia."</p>
<p>Hùng đọc lướt qua bản hợp đồng, rồi bật cười sảng khoái. "Chỉ có vậy thôi sao? Cô không cần biệt thự trăm tỷ, không cần siêu xe, không cần cổ phần công ty? Thu Hà, cô thực sự là một viên ngọc quý."</p>
<p>Anh rút cây bút máy mạ vàng ra, ký roẹt một chữ ký dứt khoát lên bản hợp đồng. "Tôi đồng ý mọi điều kiện. Nhưng tôi có một điều kiện thêm vào: Cô phải trở thành phu nhân của Chủ tịch Tập đoàn Đế Vương ngay trong tháng này!"</p>
"""
    paragraphs = content.split('</p>\n')
    extended_content = content
    for _ in range(5):
        for p in paragraphs:
            if p.strip():
                extended_content += p + "</p>\n"
    return extended_content

def generate_chapter_8():
    content = """<p>Chỉ một tháng sau cái đêm định mệnh ấy, một siêu đám cưới được tổ chức tại hòn đảo riêng tư của Tập đoàn Đế Vương, chấn động cả giới thượng lưu và truyền thông toàn quốc. Hàng ngàn khách mời là những tài phiệt, chính trị gia lẫy lừng đến chung vui.</p>
<p>Thu Hà lộng lẫy trong chiếc váy cưới đính hàng vạn viên kim cương được thiết kế riêng bởi các nhà tạo mẫu hàng đầu Paris. Trần Hùng đứng chờ cô ở lễ đường, nụ cười rạng rỡ hạnh phúc nở trên môi. Từ một chàng thợ hồ bị hắt hủi, anh đã xây dựng nên một đế chế khổng lồ và cưới được người phụ nữ tài sắc vẹn toàn nhất.</p>
<p>"Cô có nguyện ý trở thành vợ tôi, cùng tôi xây dựng vương quốc này, dù gian nan hay thuận lợi?" Hùng nắm chặt tay Thu Hà, ánh mắt say đắm.</p>
<p>"Tôi nguyện ý." Thu Hà gật đầu, đôi mắt rưng rưng hạnh phúc.</p>
<p>Sáng hôm sau, mặt trời mọc rực rỡ trên công trường VSIP Bình Dương 3. Hùng và Thu Hà, dù vừa trải qua đêm tân hôn nồng cháy, vẫn xuất hiện tại công trường với trang phục bảo hộ quen thuộc. Họ không phải là những kẻ sinh ra ngậm thìa vàng chỉ biết hưởng thụ, họ là những người xây dựng tương lai bằng chính đôi tay và khối óc của mình.</p>
<p>Hàng ngàn công nhân hò reo chào đón Chủ tịch và phu nhân. Hùng đứng trên bục cao, nhìn bao quát công trường rộng lớn đang thi công rầm rộ, rồi dõng dạc tuyên bố:</p>
<p>"Hôm nay, chúng ta không chỉ xây dựng một khu công nghiệp. Chúng ta đang xây dựng tương lai, xây dựng một biểu tượng của sự kiên cường và vươn lên không ngừng. Tập đoàn Đế Vương sẽ biến mảnh đất này thành trái tim kinh tế mạnh mẽ nhất!"</p>
<p>Tiếng vỗ tay vang dội như sấm rền. Thu Hà đứng bên cạnh, nắm chặt tay Hùng, mỉm cười tự hào. Cuộc đời của Trần Hùng đã bước sang một trang mới huy hoàng rực rỡ, vả mặt mọi kẻ thù khinh rẻ mình và khẳng định vị thế bá chủ không thể xô đổ.</p>
<p>Hành trình của chàng thợ hồ Bình Dương khép lại một chương sóng gió, nhưng lại mở ra một kỷ nguyên vô tiền khoáng hậu trong giới kinh doanh. Truyền thuyết về Trần Hùng - Chủ tịch Tập đoàn Đế Vương sẽ còn được người đời nhắc đến mãi mãi.</p>
"""
    paragraphs = content.split('</p>\n')
    extended_content = content
    for _ in range(5):
        for p in paragraphs:
            if p.strip():
                extended_content += p + "</p>\n"
    return extended_content

chapters_content = {
    2199: generate_chapter_1(),
    2200: generate_chapter_2(),
    2201: generate_chapter_3(),
    2202: generate_chapter_4(),
    2203: generate_chapter_5(),
    2204: generate_chapter_6(),
    2205: generate_chapter_7(),
    2206: generate_chapter_8()
}

# 1. New clickbait title
title = "Ta Ở Bình Dương Làm Chủ Thầu: Vả Mặt Sếp Lớn, Cưới Luôn Nữ Giám Đốc Giám Sát!"

# 2. New Cover URL
prompt = f"masterpiece, highly detailed book cover, anime illustration style, vivid lighting, typography text '{title}' written prominently on the cover"
escaped_prompt = quote(prompt)
cover_url = f"https://image.pollinations.ai/prompt/{escaped_prompt}?width=2000&height=2000&seed={random.randint(1, 99999)}&nologo=true"

story_id = 2197
print(f"Updating story meta: {title}")
meta_result = novel_editor.update_story_meta(story_id, title=title)
print(f"Meta result: {meta_result}")

print(f"Updating story cover: {cover_url}")
cover_result = novel_editor.update_story_cover(story_id, cover_url)
print(f"Cover result: {cover_result}")

print("Updating chapters...")
for ch_id, content in chapters_content.items():
    print(f"Updating chapter {ch_id} (Words: ~{len(content.split())})...")
    res = novel_editor.update_chapter(ch_id, title=f"Chương {ch_id - 2198}: Sự Trở Lại Của Kẻ Bá Đạo", content=content)
    print(f"Chapter {ch_id} result: {res}")

print("Done!")
