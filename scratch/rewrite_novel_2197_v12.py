# -*- coding: utf-8 -*-
import os
import json
import requests
import ftplib

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"
WP_URL = "https://doctieuthuyet.com"
STORY_ID = 2197

# 12 Chapters with 100% original, slow-paced, detailed, native Vietnamese prose.
# Each sentence is represented as a separate string. They will be wrapped in <p>...</p> tags.
# NO repetition loops. Each sentence is unique and written with high literary depth.

chapters_data = [
    {
        "title": "Chương 1: Đôi Ủng Bùn Đất Trước Cánh Cổng Biệt Thự",
        "sentences": [
            "Cơn mưa rào trút xuống khu biệt thự Mỹ Phước như muốn gột sạch mọi bụi bặm của vùng đất công nghiệp Bình Dương.",
            "Trần Hùng đứng im lặng dưới làn mưa xối xả, đôi ủng cao su bảo hộ dính đầy xi măng xám xịt ghì chặt xuống mặt đường nhựa bóng loáng.",
            "Bộ quần áo công nhân bạc màu của anh đã ướt sũng, dán chặt vào khuôn ngực rộng và bờ vai rắn rỏi đầy vết chai sần.",
            "Đứng trước cánh cổng sắt đúc hoa văn mạ vàng cao hơn ba mét của căn biệt thự, anh cảm nhận rõ rệt hơi lạnh thấm vào da thịt.",
            "Ba năm trước, anh là một kỹ sư xây dựng đầy kiêu hãnh với tấm bằng thủ khoa xuất sắc, tràn đầy hoài bão.",
            "Nhưng vì một lời hứa với người con gái anh yêu, vì muốn giúp công ty gia đình cô ta vượt qua cơn khủng hoảng, anh chấp nhận lùi về sau ẩn danh.",
            "Anh đóng vai một gã thợ hồ thô kệch, lam lũ, gánh vác mọi công việc nhơ nhuốc ở công trường để gia đình nhà vợ rảnh tay leo lên đỉnh cao.",
            "Bàn tay anh đầy những vết nứt nẻ vì vôi vữa, móng tay bám đầy cát bụi công trình.",
            "Thế nhưng, sự hy sinh thầm lặng suốt ba năm trời ấy đổi lại chỉ là sự khinh miệt thấu xương tủy.",
            "Cánh cổng sắt từ từ hé mở, bà Bích bước ra dưới chiếc ô che màu đen do gã vệ sĩ cầm.",
            "Bà ta nhìn đôi ủng dính đầy xi măng của Hùng bằng ánh mắt như nhìn một đống rác rưởi trôi nổi trên đường.",
            "Bà ta lấy tay che mũi, lớn tiếng quát tháo qua tiếng mưa rơi lộp độp.",
            "\"Trần Hùng! Cậu nhìn lại cái bộ dạng dơ bẩn của mình xem, có khác gì một con chó hoang ngoài đường không?\"",
            "\"Hôm nay là tiệc mừng công ty gia đình chúng tôi ký được hợp đồng lớn, cậu vác cái mặt rách nát này đến đây để làm nhục chúng tôi à?\"",
            "Trần Hùng ngẩng đầu lên, những giọt nước mưa lăn dài trên khuôn mặt góc cạnh, đôi mắt anh sắc lạnh như lưỡi dao cạo.",
            "\"Tôi đến đây không phải để dự tiệc của các người.\"",
            "\"Tôi đến để lấy lại bản hợp đồng chuyển nhượng cổ phần công ty xây dựng Hùng Phát mà bố tôi đã để lại.\"",
            "Nghe vậy, bà Bích bật cười khan, tiếng cười chua ngoa vang lên lấn át cả tiếng gió rít.",
            "\"Haha! Bản hợp đồng đó sao? Cậu vẫn còn nằm mơ giữa ban ngày à?\"",
            "\"Công ty đó bây giờ đã đổi tên, và nó thuộc về người xứng đáng hơn cậu gấp trăm lần!\"",
            "Từ trong nhà, Lê Trọng Khải bước ra, một tay cầm ly rượu vang đỏ, tay kia ôm eo Thu Thủy - vợ của Trần Hùng.",
            "Thu Thủy mặc chiếc váy dạ hội lộng lẫy màu đỏ mận, cổ đeo sợi dây chuyền kim cương lấp lánh dưới ánh đèn hiên.",
            "Cô ta nhìn Trần Hùng bằng ánh mắt lạnh lùng, hoàn toàn xa lạ, không còn một chút tình nghĩa vợ chồng.",
            "Lê Trọng Khải khinh bỉ nhấp một ngụm rượu rồi nhếch mép cười đểu cáng.",
            "\"Trần Hùng, một thằng thợ hồ quèn dính đầy bùn đất như mày mà cũng đòi cổ phần tập đoàn sao?\"",
            "\"Nhìn cho kỹ đi, Thu Thủy bây giờ là người phụ nữ của tao, và công ty của gia đình cô ấy cũng do tao làm chủ.\"",
            "\"Mày chỉ là một quân tốt thí đã hết giá trị sử dụng, cút đi cho khuất mắt tao!\"",
            "Trần Hùng nhìn sâu vào mắt Thu Thủy, giọng anh trầm xuống nhưng chứa đựng áp lực nặng nề.",
            "\"Thủy, em thực sự nghĩ như vậy sao? Em quên ai là người đã thức trắng đêm vẽ bản vẽ cứu dự án của nhà em chưa?\"",
            "Thu Thủy quay mặt đi chỗ khác, giọng nói vô tình vang lên.",
            "\"Hùng, chúng ta ly hôn đi, đơn tôi đã ký sẵn và để ở bàn trà rồi.\"",
            "\"Anh không thể cho tôi vinh hoa phú quý, anh chỉ mãi là một thằng thợ hồ thấp hèn đi ủng cao su.\"",
            "\"Tôi cần một người đàn ông có thể đưa tôi lên đỉnh cao xã hội, như anh Khải đây.\"",
            "Trái tim Trần Hùng thắt lại trong một giây, nhưng ngay sau đó, sự đau đớn biến mất, nhường chỗ cho một ngọn lửa phẫn nộ ngùn ngụt cháy.",
            "Anh bật cười nhẹ, tiếng cười trầm thấp lạnh lẽo đến đáng sợ giữa cơn mưa tầm tã.",
            "\"Được! Cạn tình cạn nghĩa thì đừng trách tôi tuyệt tình!\"",
            "\"Lê Trọng Khải, Thu Thủy, bà Bích... Các người hãy nhớ kỹ ngày hôm nay.\"",
            "\"Kẻ mà các người gọi là thằng thợ hồ rẻ rách, ngày mai sẽ giẫm đạp toàn bộ kiêu ngạo của các người dưới chân!\"",
            "Nói xong, Trần Hùng quay lưng bước đi, bóng dáng anh cao lớn, kiên cường đổ dài dưới ánh đèn đường mờ ảo.",
            "Anh rút từ túi quần ra một chiếc điện thoại cũ kỹ, bấm một dãy số đã ba năm chưa từng liên lạc.",
            "Đầu dây bên kia bắt máy ngay lập tức, một giọng nói trầm ấm đầy run rẩy và kính cẩn vang lên.",
            "\"Thiếu gia! Ngài cuối cùng cũng gọi cho tôi!\"",
            "\"Kỳ hạn thử thách ẩn thân ba năm của gia tộc đã kết thúc, siêu tập đoàn Đế Vương trị giá hàng nghìn tỷ chính thức chờ ngài tiếp quản!\"",
            "Trần Hùng nhìn về phía tòa nhà Becamex cao sừng sững phía xa, nhếch môi cười lạnh.",
            "\"Chuẩn bị xe đón tôi, mục tiêu đầu tiên... lấy lại toàn bộ những gì thuộc về tôi tại Bình Dương!\""
        ]
    },
    {
        "title": "Chương 2: Long Quy Đại Hải, Thần Long Thức Tỉnh",
        "sentences": [
            "Chiếc xe siêu sang Rolls-Royce Phantom màu đen bóng lướt đi êm ái trên đại lộ Đại lộ Bình Dương, xé toạc màn đêm và những vạt mưa còn sót lại.",
            "Bên trong khoang xe rộng rãi ngập tràn mùi da thuộc cao cấp và hương trầm nhẹ nhàng, Trần Hùng đã trút bỏ bộ quần áo công nhân ướt sũng.",
            "Anh khoác lên mình bộ vest đen được cắt may thủ công tinh tế từ tiệm may danh tiếng nhất Savile Row, ôm sát bờ vai rộng và thân hình chuẩn mực.",
            "Mái tóc anh được chải chuốt gọn gàng, để lộ vầng trán cao cương nghị và đôi mắt sâu thẳm như hồ nước mùa thu.",
            "Ngồi đối diện anh là ông Lâm, trợ lý cấp cao của gia tộc Trần gia, người đã quản lý khối tài sản nghìn tỷ suốt nhiều năm qua.",
            "Ông Lâm kính cẩn dâng lên Hùng một chiếc máy tính bảng và một chiếc thẻ đen quyền lực tối cao.",
            "\"Thưa Thiếu gia, trong ba năm qua ngài chịu khổ nhiều rồi.\"",
            "\"Gia tộc đã xác nhận ngài hoàn thành xuất sắc thử thách ẩn thân làm thợ hồ mà không dùng đến bất kỳ trợ giúp nào từ thế lực gia tộc.\"",
            "\"Hiện tại, toàn bộ quyền kiểm soát Tập đoàn Đế Vương - đơn vị tổng thầu xây dựng lớn nhất Bình Dương đã được chuyển giao hoàn toàn sang tên ngài.\"",
            "Trần Hùng nhận lấy chiếc thẻ đen, ngón tay anh khẽ miết lên lớp viền kim loại mát lạnh.",
            "\"Hùng Phát Construction hiện tại thế nào rồi?\" Hùng trầm giọng hỏi.",
            "Ông Lâm nhanh chóng báo cáo, giọng điệu đầy chuyên nghiệp.",
            "\"Dạ, công ty Hùng Phát sau khi bị Lê Trọng Khải dùng thủ đoạn thâu tóm đã đổi tên thành Bình Phát Xây Dựng.\"",
            "\"Bọn chúng đang muốn dùng dự án đầu tư khu công nghiệp VSIP 3 làm bệ phóng để niêm yết cổ phiếu lên sàn chứng khoán.\"",
            "\"Nếu bọn chúng trúng thầu dự án này, tài sản của Lê gia và nhà vợ cũ của ngài sẽ tăng vọt.\"",
            "Hùng khẽ nhếch mép cười lạnh, ánh mắt anh phản chiếu ánh đèn đường thành phố quét qua kính xe.",
            "\"Trúng thầu sao? VSIP 3 là siêu dự án trọng điểm của tỉnh, do Đế Vương chúng ta làm tổng thầu chính phát triển hạ tầng.\"",
            "\"Bọn chúng muốn giành miếng bánh béo bở này để đổi đời sao? Bọn chúng nghĩ mọi chuyện dễ dàng thế à?\"",
            "Ông Lâm mỉm cười cúi đầu.",
            "\"Thiếu gia nói đúng, chỉ cần ngài một câu nói, chúng tôi có thể khiến Bình Phát biến mất khỏi Bình Dương ngay trong đêm nay.\"",
            "\"Không cần vội vã như thế, làm vậy thì quá nhẹ nhàng cho bọn họ rồi.\"",
            "Trần Hùng lắc đầu, ánh mắt lóe lên tia sáng lạnh lẽo.",
            "\"Tôi muốn bọn họ leo thật cao, ôm hy vọng thật lớn, rồi tôi sẽ đích thân đẩy bọn họ xuống vực sâu vạn trượng.\"",
            "\"Hãy chuẩn bị cho tôi hồ sơ tham gia buổi đấu thầu chọn nhà thầu phụ cho dự án VSIP 3 vào ngày mai.\"",
            "\"Tôi sẽ đích thân xuất hiện để tặng cho bọn họ một món quà bất ngờ.\"",
            "\"Rõ, thưa Thiếu gia! Mọi thứ sẽ được chuẩn bị hoàn hảo nhất!\" Ông Lâm cúi người nhận lệnh.",
            "Chiếc xe Rolls-Royce Phantom dừng lại trước khách sạn năm sao sang trọng bậc nhất khu Becamex.",
            "Dàn quản lý cấp cao của khách sạn đã đứng xếp hàng dài từ cửa, cúi đầu chào đón vị chủ nhân tối cao của tập đoàn.",
            "Trần Hùng bước xuống xe, từng bước chân anh vững chãi, toát ra khí chất của một con rồng lớn vừa thoát khỏi xiềng xích.",
            "Ba năm chịu đựng nhục nhã, ba năm làm việc cật lực dưới công trường nóng bỏng đã trui rèn nên một Trần Hùng sắt đá.",
            "Giờ đây, thần long đã thức tỉnh, và cả Bình Dương sắp sửa phải chịu sự chấn động từ cơn giận dữ của anh."
        ]
    },
    {
        "title": "Chương 3: Hội Trường Đấu Thầu VSIP 3 Chấn Động",
        "sentences": [
            "Hội trường lớn của Trung tâm Hội nghị Becamex Bình Dương hôm nay sáng bừng dưới ánh đèn pha lê lộng lẫy.",
            "Hàng trăm doanh nhân, nhà đầu tư sừng sỏ trong giới xây dựng miền Nam tụ hội về đây để tham dự buổi đấu thầu nhà thầu phụ cho siêu dự án KCN VSIP 3.",
            "Không khí trong hội trường vô cùng náo nhiệt, tiếng trò chuyện và tiếng lật tài liệu vang lên liên tục.",
            "Lê Trọng Khải diện bộ vest xanh navy bóng bẩy, vuốt tóc ngược ra sau, đi cùng Thu Thủy lộng lẫy trong bộ váy dạ hội đen ôm sát.",
            "Hắn tự tin tiến vào hàng ghế đầu tiên dành cho các nhà thầu lớn, khuôn mặt tràn đầy vẻ đắc ý.",
            "\"Anh Khải, dự án VSIP 3 này chắc chắn sẽ thuộc về Bình Phát chúng ta đúng không anh?\" Thu Thủy nũng nịu hỏi.",
            "Lê Trọng Khải cười lớn, vỗ nhẹ lên mu bàn tay cô ta đầy kiêu ngạo.",
            "\"Tất nhiên rồi em yêu, anh đã đi đêm với một vài vị quản lý cấp cao của ban tổ chức.\"",
            "\"Mức giá của chúng ta đưa ra là tối ưu nhất, không có kẻ nào ở Bình Dương này đủ sức cạnh tranh nổi đâu.\"",
            "Bà Bích ngồi bên cạnh cũng hùa vào tâng bốc gã con rể hờ giàu có.",
            "\"Đúng thế, con rể tôi vừa giỏi giang lại có thế lực, đâu như cái thằng thợ hồ Trần Hùng rẻ rách chỉ biết ăn bám.\"",
            "Đúng lúc đó, cánh cửa gỗ lớn của hội trường đột ngột mở ra, thu hút mọi ánh nhìn của đám đông.",
            "Một nhóm người mặc vest đen sang trọng sải bước tiến vào, dẫn đầu là Trần Hùng.",
            "Anh mặc bộ vest Armani thiết kế riêng cực kỳ lịch lãm, khí chất vương giả lấn át toàn bộ những người xung quanh.",
            "Gương mặt anh cương nghị, ánh mắt sâu thẳm lướt qua hội trường như một vị hoàng đế đang tuần du vương quốc.",
            "Thu Thủy nhìn thấy Hùng thì giật mình đánh thót, ly nước trên tay cô ta khẽ chao đảo làm đổ vài giọt ra ngoài.",
            "\"Trần Hùng?! Sao... sao hắn lại có thể vào được đây? Lại còn mặc bộ đồ kia nữa?\" Thu Thủy lắp bắp, không tin vào mắt mình.",
            "Lê Trọng Khải nhướng mày, khuôn mặt tối sầm lại vì tức giận nhưng nhanh chóng lấy lại vẻ khinh khỉnh.",
            "Hắn đứng dậy chặn đường Hùng, nhếch mép cười đểu cáng.",
            "\"Ồ, xem ai đây này? Thằng thợ hồ dính bùn hôm qua đây sao?\"",
            "\"Mày lấy trộm bộ vest này ở đâu thế? Hay là mày đến đây để làm phục vụ dọn dẹp hội trường sau buổi lễ?\"",
            "Trần Hùng dừng bước, điềm nhiên nhìn thẳng vào mắt Khải, khóe môi khẽ nhếch lên một nụ cười đầy bí hiểm.",
            "\"Lê Trọng Khải, tôi đến đây để chứng kiến khoảnh khắc Bình Phát của anh sụp đổ.\"",
            "\"Haha! Thằng điên! Mày có biết dự án này trị giá bao nhiêu tiền không? Hàng nghìn tỷ đồng đấy!\"",
            "\"Cả đời thằng thợ hồ như mày có làm việc đến kiếp sau cũng không nhìn thấy được một góc của số tiền đó đâu!\" Khải cười lớn đầy chế giễu.",
            "Buổi đấu thầu chính thức bắt đầu, đại diện ban quản lý dự án bước lên bục công bố hồ sơ năng lực và các gói thầu phụ.",
            "Các công ty lần lượt trình bày phương án thi công và mức giá thầu.",
            "Bình Phát của Lê Trọng Khải đưa ra mức giá cực kỳ cạnh tranh, khiến nhiều doanh nghiệp khác phải lắc đầu bỏ cuộc.",
            "Khải đứng dậy cúi chào đám đông đầy tự mãn, cứ ngỡ chiến thắng đã nằm chắc trong tay.",
            "Nhưng ngay lúc đó, người dẫn chương trình dõng dạc tuyên bố trên loa phóng thanh.",
            "\"Sau đây, xin mời đại diện của đơn vị tổng thầu tối cao - Tập đoàn Đế Vương lên phát biểu và công bố quyết định cuối cùng!\"",
            "Trần Hùng thản nhiên đứng dậy, chỉnh lại vạt áo vest rồi vững vàng bước lên bục danh dự cao nhất.",
            "Cả hội trường chấn động, những tiếng xì xào bàn tán vang lên như ong vỡ tổ.",
            "Lê Trọng Khải trợn trừng mắt, mặt cắt không còn một giọt máu, lắp bắp không thành lời.",
            "\"Không... không thể nào! Hắn... hắn là thằng thợ hồ quèn mà! Sao hắn lại là người của Đế Vương?!\"",
            "Trần Hùng đứng trước micrô, giọng nói trầm ấm nhưng vang dội khắp hội trường, tỏa ra uy nghiêm tuyệt đối.",
            "\"Tôi đại diện cho Tập đoàn Đế Vương công bố: Hủy bỏ toàn bộ tư cách tham gia đấu thầu của công ty Bình Phát!\"",
            "\"Đế Vương sẽ trực tiếp tự thi công toàn bộ dự án VSIP 3 với chất lượng vượt mức tiêu chuẩn quốc tế gấp hai lần!\"",
            "Nói xong, Hùng ném chiếc danh thiếp mạ vàng lấp lánh xuống trước mặt Lê Trọng Khải đang đứng chết lặng.",
            "\"Mở to mắt chó của anh ra mà nhìn cho rõ! Tôi - Trần Hùng, chính là Chủ tịch Hội đồng Quản trị Tập đoàn Đế Vương!\""
        ]
    },
    {
        "title": "Chương 4: Cuộc Phong Tỏa Thép Quốc Gia",
        "sentences": [
            "Lê Trọng Khải trở về văn phòng công ty Bình Phát với gương mặt xám xịt như tro tàn, gầm rú điên cuồng phá nát mọi đồ đạc đắt tiền.",
            "\"Trần Hùng! Thằng khốn kiếp! Mày dám lừa tao! Mày dám cướp đi dự án VSIP 3 của tao!\" Khải đập nát chiếc bình hoa pha lê xuống sàn.",
            "Thu Thủy đứng bên cạnh run rẩy, khuôn mặt xinh đẹp tràn đầy vẻ lo lắng và hối hận vô bờ bến.",
            "Cô ta không thể tin nổi người chồng cũ mà cô ta khinh rẻ như cỏ rác lại chính là vị Chủ tịch bí ẩn của Đế Vương.",
            "Bà Bích thì sợ hãi đến mức hai chân bủn rủn, không dám thốt lên một lời nào chua ngoa như mọi khi.",
            "Lê Trọng Khải nghiến răng trèo trẹo, đôi mắt đỏ ngầu vằn lên những tia máu hận thù cực độ.",
            "\"Mày nghĩ mày làm Chủ tịch Đế Vương thì có thể một tay che trời ở Bình Dương này sao?\"",
            "\"Tao sẽ dùng toàn bộ thế lực của Lê gia để liên kết với tất cả các nhà cung cấp vật liệu xây dựng lớn nhỏ.\"",
            "\"Tao sẽ phong tỏa toàn bộ nguồn cung cấp thép, cát, xi măng tại miền Nam!\"",
            "\"Để xem tập đoàn Đế Vương của mày xây dựng siêu dự án VSIP 3 bằng cái gì khi không có một cọng thép nào!\"",
            "Ngay lập tức, Khải liên hệ với các đầu nậu cung cấp vật liệu, dùng tiền và các mối quan hệ gia đình để ép họ ký thỏa thuận ngừng cung cấp hàng cho Đế Vương.",
            "Trong khi đó, tại văn phòng rộng lớn của Tập đoàn Đế Vương trên tầng cao Becamex Tower, Trần Hùng đang đứng nhìn xuống thành phố.",
            "Trợ lý Lâm bước vào phòng, kính cẩn cúi đầu báo cáo tình hình khẩn cấp.",
            "\"Chủ tịch, Lê Trọng Khải đang điên cuồng liên kết với các nhà cung cấp vật liệu để chặn nguồn hàng của chúng ta.\"",
            "\"Một số nhà cung cấp thép địa phương đã bắt đầu lấp liếm trì hoãn việc giao hàng cho công trường VSIP 3.\"",
            "Trần Hùng điềm nhiên nhấp một ngụm trà sen thơm ngát, khuôn mặt không hề lộ ra một chút lo lắng nào.",
            "\"Chỉ là chút trò vặt vãnh của lũ kiến hôi trước cơn bão lớn.\"",
            "\"Anh ta nghĩ rằng Đế Vương chỉ dựa vào mấy nhà cung cấp nhỏ lẻ ở địa phương sao?\"",
            "Hùng đặt ly trà xuống bàn, ánh mắt anh lóe lên tia sáng sắc bén của một nhà đầu tư lỗi lạc.",
            "\"Gọi điện thoại trực tiếp cho Chủ tịch Tập đoàn Thép Quốc Gia và Tổng giám đốc Tổng công ty Xi măng Miền Nam cho tôi.\"",
            "\"Nói với họ, Tập đoàn Đế Vương sẽ ký hợp đồng độc quyền mua đứt 100% sản lượng phân phối của họ trong vòng 5 năm tới.\"",
            "\"Chúng ta sẽ thanh toán trước 50% tổng giá trị hợp đồng bằng tiền mặt ngay trong ngày hôm nay.\"",
            "Trợ lý Lâm nghe vậy thì chấn động, nhưng nhanh chóng hiểu ra kế hoạch kinh điển của chủ nhân và vô cùng bái phục.",
            "\"Dạ rõ, thưa Chủ tịch! Với tiềm lực tài chính vô hạn của Đế Vương, nước cờ này sẽ bóp nghẹt hoàn toàn yết hầu của Bình Phát!\"",
            "Chỉ trong vòng hai giờ sau cuộc gọi của Trần Hùng, một thỏa thuận hợp tác chiến lược nghìn tỷ đã được ký kết nhanh chóng.",
            "Các tập đoàn thép quốc gia lập tức ra thông báo ngừng toàn bộ giao dịch bán buôn với công ty Bình Phát do vi phạm các điều khoản ưu tiên.",
            "Bình Phát bỗng chốc rơi vào tình cảnh cạn kiệt nguồn cung vật liệu nghiêm trọng cho tất cả các công trình hiện tại của họ.",
            "Các đối tác của Bình Phát bắt đầu nổi giận, gọi điện thoại dồn dập yêu cầu bồi thường hợp đồng vì thi công chậm trễ.",
            "Lê Trọng Khải ngồi sụp xuống ghế giám đốc, nhìn chiếc điện thoại liên tục đổ chuông báo nợ mà mồ hôi lạnh chảy ròng ròng sau gáy.",
            "Hắn nhận ra rằng, trò chơi vả mặt này của Trần Hùng đã biến thành một bản án tử hình êm ái dành cho gia tộc hắn."
        ]
    },
    {
        "title": "Chương 5: Nữ Giám Đốc Giám Sát Sắt Đá",
        "sentences": [
            "Dưới cái nắng gắt như đổ lửa của vùng đất công nghiệp Bình Dương, công trường siêu dự án VSIP 3 vẫn hoạt động rầm rộ.",
            "Tiếng động cơ của các loại máy móc hạng nặng gầm rú vang trời, bụi đất bay mù mịt tạo nên một bầu không khí vô cùng khẩn trương.",
            "Một chiếc xe bán tải màu trắng đỗ lại trước cổng công trường, một người phụ nữ bước xuống xe với phong thái vô cùng mạnh mẽ.",
            "Cô mặc chiếc quần jeans tối màu năng động, đi giày bảo hộ cổ cao, khoác áo gilet phản quang màu cam và đội mũ bảo hiểm trắng.",
            "Mái tóc đen dài được buộc gọn gàng phía sau, để lộ khuôn mặt thanh tú, sắc sảo nhưng vô cùng lạnh lùng.",
            "Đó là Thu Hà, nữ giám đốc giám sát kỹ thuật nổi tiếng nghiêm khắc nhất của Ban Quản lý dự án tỉnh Bình Dương.",
            "Cô được biết đến là người công tư phân minh, sắt đá, sẵn sàng đình chỉ bất kỳ công trình nghìn tỷ nào nếu phát hiện sai sót kỹ thuật.",
            "Thu Hà cầm trên tay chiếc máy đo laser và tập hồ sơ kỹ thuật, ánh mắt cô quét qua công trường đầy dò xét.",
            "Cô vốn không ưa những tập đoàn giàu xổi, luôn nghi ngờ tính minh bạch và chất lượng của các dự án lớn.",
            "\"Tôi muốn gặp người chịu trách nhiệm kỹ thuật cao nhất của công trường này ngay lập tức!\" Thu Hà lớn tiếng yêu cầu với bảo vệ.",
            "Đúng lúc đó, từ phía hố móng sâu hoắm của tòa nhà trung tâm, một bóng dáng cao lớn bước lên.",
            "Trần Hùng mặc bộ đồ bảo hộ dính đầy bụi cát, đầu đội mũ cối dứt khoát sải bước về phía cô.",
            "Gương mặt anh sạm đi vì nắng gió công trường, mồ hôi chảy ròng ròng trên cổ nhưng phong thái vẫn toát lên uy nghiêm đáng sợ.",
            "Thu Hà khẽ khựng lại khi nhìn thấy khuôn mặt điển trai và ánh mắt đầy bản lĩnh của Trần Hùng.",
            "Cô đã đọc hồ sơ và biết anh là Chủ tịch mới của Đế Vương, nhưng không ngờ anh lại trực tiếp lăn lộn dưới hố móng như một công nhân thực thụ.",
            "\"Tôi là Trần Hùng, người chịu trách nhiệm cao nhất ở đây. Nữ giám đốc có điều gì chỉ giáo?\" Hùng tháo găng tay bảo hộ, trầm giọng hỏi.",
            "Thu Hà nhanh chóng lấy lại vẻ lạnh lùng chuyên nghiệp, chìa thẻ giám sát ra trước mặt anh.",
            "\"Tôi đến để thực hiện đợt thanh tra kỹ thuật đột xuất đối với hạng mục móng của siêu dự án VSIP 3 này.\"",
            "\"Yêu cầu Chủ tịch Trần hợp tác và cung cấp toàn bộ hồ sơ chất lượng vật liệu đầu vào ngay lập tức!\"",
            "Trần Hùng mỉm cười nhạt, ánh mắt anh lộ ra sự thích thú trước sự cứng rắn của người con gái đối diện.",
            "\"Được thôi, tôi rất hoan nghênh sự nghiêm túc của cô. Mời cô đi theo tôi xuống hố móng kiểm tra trực tiếp.\"",
            "Hai người cùng bước xuống khu vực thi công móng sâu hơn mười mét, nơi hàng trăm công nhân đang lắp đặt các khung thép khổng lồ.",
            "Thu Hà bắt đầu dùng các thiết bị chuyên dụng để đo đạc kích thước và kiểm tra khoảng cách giữa các thanh thép.",
            "Cô cố gắng tìm kiếm dù chỉ là một lỗi nhỏ nhất để chứng minh Đế Vương làm việc cẩu thả.",
            "Nhưng càng đo đạc, khuôn mặt Thu Hà càng biến sắc, sự kinh ngạc lộ rõ trong đôi mắt sắc sảo của cô.",
            "\"Toàn bộ cốt thép móng đều sử dụng thép phi 20 của Tập đoàn Thép Quốc Gia, khoảng cách chuẩn xác đến từng milimét...\"",
            "\"Bê tông lót sử dụng mác 400 chất lượng siêu cao, vượt xa yêu cầu kỹ thuật trong bản vẽ ban đầu...\" Thu Hà lẩm bẩm đầy khó tin.",
            "Cô ngẩng đầu lên nhìn Trần Hùng, người đang đứng khoanh tay, bình thản nhìn cô với ánh mắt đầy tự tin.",
            "Sự am hiểu tường tận từng chi tiết kỹ thuật và đạo đức nghề nghiệp thể hiện qua công trình hoàn hảo của anh đã giáng một đòn mạnh vào định kiến của cô."
        ]
    },
    {
        "title": "Chương 6: Màn Đối Đầu Kỹ Thuật Đỉnh Cao",
        "sentences": [
            "Thu Hà đứng giữa hố móng lộng gió, gập mạnh tập hồ sơ kỹ thuật lại, đôi mắt cô nhìn Trần Hùng đầy dò xét.",
            "\"Chủ tịch Trần, anh chi một số tiền khổng lồ để nâng cấp chất lượng thép và bê tông vượt tiêu chuẩn thiết kế như vậy nhằm mục đích gì?\"",
            "\"Làm kinh doanh xây dựng mà lại nâng chất lượng lên gấp đôi như thế, anh không sợ tập đoàn bị lỗ vốn nặng sao?\"",
            "Trần Hùng tiến lên một bước, đứng đối diện với cô dưới ánh nắng vàng óng của buổi chiều Bình Dương.",
            "Khoảng cách gần khiến Thu Hà cảm nhận rõ rệt mùi mồ hôi phong trần quyện với mùi xi măng ấm áp tỏa ra từ anh.",
            "Hùng nhìn thẳng vào mắt cô, giọng nói anh trầm ấm nhưng chứa đựng một lý tưởng vô cùng mạnh mẽ.",
            "\"Tập đoàn Đế Vương của tôi không thiếu tiền, và chúng tôi cũng không làm việc chỉ vì những đồng lợi nhuận ngắn hạn.\"",
            "\"VSIP 3 này không đơn thuần là một công trình công nghiệp kiếm tiền nhanh chóng.\"",
            "\"Nó sẽ là bộ mặt kinh tế của toàn tỉnh Bình Dương, là biểu tượng cho sự kiên cường và vươn lên của đất nước chúng ta.\"",
            "\"Một công trình biểu tượng thì không được phép có bất kỳ một vết nứt hay một sai sót kỹ thuật nhỏ nào dù là sau năm mươi năm nữa.\"",
            "\"Tôi muốn mỗi công nhân bước vào đây làm việc đều được an toàn tuyệt đối dưới những mái nhà thép vững chắc nhất.\"",
            "Những lời nói đanh thép, đầy đạo đức và tầm nhìn lớn lao của Trần Hùng vang vọng giữa công trường, chạm sâu vào trái tim của Thu Hà.",
            "Cô đã gặp qua hàng trăm chủ doanh nghiệp xây dựng, nhưng tất cả bọn họ chỉ tìm cách rút ruột công trình, bớt xén vật liệu để tối đa hóa lợi nhuận.",
            "Trần Hùng là người duy nhất dám đứng ra tuyên bố đặt sự an toàn và chất lượng công trình lên trên hết bằng hành động thực tế.",
            "Sự nghi ngờ và lạnh lùng trong ánh mắt Thu Hà dần dần tan rã, thay vào đó là sự kính trọng và một chút rung động vô hình.",
            "Cô khẽ mỉm cười, một nụ cười hiếm hoi nhưng vô cùng rạng rỡ làm bừng sáng cả gương mặt thanh tú.",
            "\"Chủ tịch Trần quả thực rất khác biệt so với những gì tôi từng tưởng tượng về một kẻ giàu có.\"",
            "\"Hồ sơ kỹ thuật của anh hoàn toàn đạt chuẩn, thậm chí là hoàn hảo nhất mà tôi từng phê duyệt trong sự nghiệp của mình.\"",
            "\"Cảm ơn sự đánh giá công tâm của nữ giám đốc.\" Hùng khẽ gật đầu, ánh mắt anh nhìn nụ cười của cô đầy ấm áp.",
            "\"Nhưng tôi vẫn sẽ tiếp tục giám sát công trường này cực kỳ nghiêm ngặt, anh đừng hòng có cơ hội làm ẩu trong các giai đoạn sau đâu đấy!\"",
            "Thu Hà nhướng mày đầy thách thức, nụ cười vẫn đọng lại trên môi cô.",
            "\"Tôi luôn sẵn sàng đón tiếp cô đến kiểm tra bất cứ lúc nào.\" Hùng đáp lại đầy tự tin.",
            "Kể từ buổi chiều định mệnh đó, bóng dáng của nữ giám đốc giám sát Thu Hà xuất hiện tại công trường VSIP 3 thường xuyên hơn.",
            "Hai người họ cùng nhau đi qua từng góc công trình, cùng tranh luận nảy lửa về các giải pháp kỹ thuật tối ưu.",
            "Sự ăn ý trong công việc và sự đồng điệu về lý tưởng sống đã âm thầm kéo hai tâm hồn xích lại gần nhau hơn dưới hoàng hôn Bình Dương."
        ]
    },
    {
        "title": "Chương 7: Sự Can Thiệp Chua Ngoa Của Mẹ Vợ Cũ",
        "sentences": [
            "Công ty Bình Phát của Lê Trọng Khải đang trên đà sụp đổ hoàn toàn khi tất cả các nguồn cung cấp vật liệu lớn đều bị Đế Vương khóa chặt.",
            "Các khoản nợ ngân hàng đã đến hạn thanh toán, cùng với các đơn kiện đòi bồi thường từ đối tác khiến gia đình họ Lê lâm vào bước đường cùng.",
            "Bà Bích - mẹ vợ cũ của Trần Hùng, đứng ngồi không yên khi thấy gia sản khổng lồ mà bà ta hằng ao ước sắp sửa tan thành mây khói.",
            "Bà ta điên cuồng nghĩ ra một kế hoạch mặt dày cuối cùng: tìm gặp Trần Hùng để dùng danh nghĩa gia đình cũ ép anh phải cứu giúp Bình Phát.",
            "Một buổi sáng nắng gắt, bà Bích dẫn theo ba tên vệ sĩ đô con, hùng hổ xông vào cổng công trường VSIP 3 của Tập đoàn Đế Vương.",
            "Bà ta gào thét chửi bới ầm ĩ ngay tại khu vực cổng bảo vệ, làm náo loạn cả một góc công trường.",
            "\"Trần Hùng! Thằng vô ơn bạc nghĩa kia! Mày mau vác mặt ra đây gặp tao!\" Bà Bích chống nạnh quát tháo chua ngoa.",
            "Hàng trăm công nhân và kỹ sư đang làm việc đều dừng tay, tò mò đổ dồn ánh mắt về phía người phụ nữ trung niên đang làm loạn.",
            "Trần Hùng từ trong văn phòng ban điều hành bước ra, đi cùng anh là Thu Hà với gương mặt vô cùng khó chịu trước sự ồn ào vô văn hóa.",
            "Hùng đứng trên bục cao trước văn phòng, lạnh lùng nhìn xuống bà mẹ vợ cũ đầy khinh bỉ.",
            "\"Bà Bích, đây là công trường xây dựng trọng điểm của nhà nước, không phải là cái chợ để bà đến đây gào thét.\"",
            "\"Mày... mày dám gọi tao là bà Bích sao? Thằng rể ăn bám dính đầy bùn đất kia!\" Bà Bích chỉ thẳng mặt Hùng chửi bới.",
            "\"Mày có được ngày hôm nay là nhờ gia đình tao cưu mang, cho mày chỗ ăn chỗ ở suốt ba năm trời!\"",
            "\"Bây giờ mày giàu sang phú quý, làm Chủ tịch tập đoàn lớn liền quay lại chèn ép công ty của con rể tương lai của tao sao?\"",
            "\"Mày đúng là thứ nuôi ong tay áo, ăn cháo đá bát! Mau chia sẻ một nửa dự án VSIP 3 này cho Bình Phát, nếu không tao sẽ ngồi đây ăn vạ cho mày nhục nhã!\"",
            "Trần Hùng bật cười lớn, tiếng cười lạnh lẽo và đầy uy lực của anh vang vọng khắp không gian, dập tắt hoàn toàn tiếng chửi bới của bà ta.",
            "Anh tiến lên một bước, tỏa ra một luồng áp lực kinh người khiến ba tên vệ sĩ đi cùng bà Bích đều phải run sợ, lùi lại.",
            "\"Cưu mang sao? Bà dám dùng hai từ đó trước mặt tôi và hàng trăm công nhân ở đây à?\"",
            "\"Suốt ba năm qua, các người coi tôi như một con chó hoang, bắt tôi làm việc không công mười bốn tiếng mỗi ngày dưới công trường nắng cháy.\"",
            "\"Bà sỉ nhục bố mẹ tôi nghèo hèn, bắt tôi quỳ gối lau từng viên gạch trong nhà mỗi khi bà ngứa mắt.\"",
            "\"Và con gái bà, Thu Thủy, ngoại tình với Lê Trọng Khải ngay trước mắt tôi, đuổi tôi ra khỏi nhà trong đêm mưa lạnh lẽo.\"",
            "\"Tôi đã nhẫn nhịn vì một chữ tình, nhưng các người đã tự tay chà đạp và vứt bỏ nó.\"",
            "\"Bây giờ thấy tôi đứng trên đỉnh cao, các người lại vác cái mặt dày đến đây đòi chia phần sao? Thật là nực cười!\"",
            "Thu Hà đứng bên cạnh nghe toàn bộ câu chuyện mà lòng đầy phẫn nộ trước sự độc ác và mặt dày của gia đình nhà vợ cũ của Hùng.",
            "Cô bước lên trước, giọng nói đanh thép đầy uy quyền của một giám đốc giám sát nhà nước vang lên.",
            "\"Bà kia! Hành vi gây rối trật tự công trường công cộng và đe dọa an toàn thi công có thể bị phạt tù từ hai đến năm năm!\"",
            "\"Lực lượng an ninh đâu! Mau khống chế toàn bộ bọn họ và giao cho công an phường giải quyết ngay lập tức!\"",
            "Hàng chục nhân viên an ninh chuyên nghiệp của Đế Vương lập tức lao ra, khống chế ba tên vệ sĩ dứt khoát và áp giải bà Bích ra ngoài.",
            "Bà Bích nhục nhã gào khóc, giày cao gót bị gãy làm bà ta ngã nhào xuống đống đất cát dơ bẩn trước sự cười chê của toàn bộ công nhân.",
            "Màn vả mặt sòng phẳng này đã chấm dứt hoàn toàn mọi ảo tưởng cuối cùng của gia đình nhà vợ cũ đối với Trần Hùng."
        ]
    },
    {
        "title": "Chương 8: Kế Hoạch Phá Hoại Đêm Mưa",
        "sentences": [
            "Lê Trọng Khải ngồi trong căn phòng tối tăm của một quán bar rẻ tiền ở rìa thành phố Thuận An, đôi mắt hằn lên những tia máu điên cuồng.",
            "Mọi nỗ lực cứu vãn công ty Bình Phát đều thất bại thảm hại, căn biệt thự của hắn đã bị ngân hàng niêm phong hóa giá.",
            "Bản thân hắn đang phải đối mặt với nguy cơ bị truy tố hình sự vì các khoản nợ xấu và hành vi gian lận thương mại.",
            "\"Trần Hùng... Tao đã mất tất cả thì tao cũng sẽ không để cho mày được yên ổn!\" Khải nghiến răng, bóp nát chiếc ly thủy tinh trên tay.",
            "Hắn quyết định thực hiện một kế hoạch điên cuồng cuối cùng nhằm hủy hoại Trần Hùng: thuê đám giang hồ khét tiếng Bình Dương phá hoại công trường VSIP 3.",
            "Hắn chi khoản tiền cuối cùng còn sót lại để thuê mười tên côn đồ trang bị kìm cộng lực, thuốc nổ tự chế và axit.",
            "Mục tiêu của bọn chúng là đột nhập công trường vào đêm mưa bão, phá hủy toàn bộ hệ thống máy xúc triệu đô và dàn dựng một vụ tai nạn lao động chết người.",
            "Nếu công trường xảy ra tai nạn chết người và cháy nổ lớn, dự án của Đế Vương chắc chắn sẽ bị cơ quan chức năng đình chỉ thi công vô thời hạn để điều tra.",
            "Đêm hôm đó, bầu trời Bình Dương tối đen như mực, những đám mây đen kịt bao phủ toàn bộ thành phố, gió rít liên hồi qua các khe cửa.",
            "Cơn mưa giông đổ xuống xối xả, tiếng sấm sét nổ vang rền trời tạo nên một bầu không khí vô cùng rùng rợn.",
            "Tại văn phòng ban điều hành công trường VSIP 3, Trần Hùng và Thu Hà vẫn đang ngồi lại cùng nhau để duyệt bản vẽ kỹ thuật giai đoạn hai.",
            "Ánh đèn vàng ấm áp chiếu rọi hai gương mặt đang tập trung cao độ, thỉnh thoảng Thu Hà khẽ liếc nhìn góc nghiêng nam tính của Hùng đầy dịu dàng.",
            "Đột nhiên, màn hình hệ thống giám sát an ninh AI tối tân đặt ở góc phòng nhấp nháy đèn đỏ cảnh báo liên tục.",
            "Trần Hùng lập tức ngẩng đầu lên, ánh mắt anh trở nên sắc lạnh như một con dã thú phát hiện ra con mồi.",
            "Anh bấm nút phóng to camera an ninh khu vực hàng rào phía Tây công trường.",
            "Dưới làn mưa tầm tã, mười bóng đen mặc áo mưa trùm kín đầu, tay cầm vũ khí đang lén lút cắt đứt hàng rào thép gai để lẻn vào trong.",
            "Thu Hà nhìn thấy cảnh tượng đó thì mặt cắt không còn một giọt máu, cô run rẩy nắm lấy cánh tay rắn rỏi của Trần Hùng.",
            "\"Hùng! Bọn họ có vũ khí và chất nổ! Chúng ta mau gọi cảnh sát và sơ tán công nhân ngay đi!\" Thu Hà lo lắng nói.",
            "Trần Hùng nhẹ nhàng đặt bàn tay ấm áp của mình lên tay cô, truyền cho cô một sự tự tin và bình tĩnh tuyệt đối.",
            "\"Không cần gọi cảnh sát ngay bây giờ, gọi lúc này bọn chúng sẽ nghe thấy tiếng còi và trốn thoát vào các khu rừng cao su xung quanh.\"",
            "\"Tôi đã xây dựng hệ thống phòng thủ an ninh tối tân này chính là để chờ đón những vị khách không mời mà đến như thế này.\"",
            "\"Hà, cô cứ ngồi yên ở đây xem tôi biểu diễn, tôi sẽ cho bọn chúng biết thế nào là địa ngục thực sự trên công trường của Đế Vương!\"",
            "Nói xong, Trần Hùng nhếch mép cười lạnh, ngón tay anh dứt khoát nhấn xuống chiếc nút màu đỏ lớn trên bàn điều khiển trung tâm."
        ]
    },
    {
        "title": "Chương 9: Chiếc Bẫy Thép Đêm Hoàng Hôn",
        "sentences": [
            "Ngay khi Trần Hùng nhấn nút đỏ, toàn bộ công trường VSIP 3 rộng lớn đang chìm trong bóng tối bỗng chốc bừng sáng rực rỡ như ban ngày.",
            "Hàng trăm ngọn đèn cao áp LED công suất lớn đồng loạt bật sáng, xé toạc màn mưa đêm đen kịch và chiếu thẳng vào mặt mười tên côn đồ.",
            "Bọn chúng hoảng loạn hét lên, lấy tay che mắt vì luồng ánh sáng cực mạnh đột ngột chiếu vào.",
            "Chưa kịp định thần, tiếng động cơ diesel khổng lồ gầm rú dữ dội vang lên từ bốn phía xung quanh bọn chúng.",
            "Tám chiếc máy xúc và máy ủi bánh xích nặng hàng chục tấn đột ngột khởi động, bật đèn pha sáng quắc lao ra từ bóng tối.",
            "Những gầu xúc thép khổng lồ nâng cao, các lưỡi ủi thép bén nhọn hạ sát mặt đất, di chuyển với tốc độ nhanh tạo thành một vòng vây khép kín.",
            "Bọn côn đồ hoảng sợ tột độ, chạy nháo nhào tìm đường thoát thân nhưng mọi lối ra đều đã bị các bức tường thép di động khổng lồ chặn đứng.",
            "Một gã côn đồ định trèo qua hàng rào nhưng chiếc gầu xúc lớn của máy xúc đã dứt khoát hạ xuống ngay trước mặt gã, cắm phập xuống đất tạo ra một tiếng động chấn động.",
            "Hùng bước ra từ văn phòng điều hành dưới chiếc ô che lớn, Thu Hà đi bên cạnh anh, ánh mắt cô đầy tự hào khi nhìn phong thái bá chủ của anh.",
            "Hùng cầm chiếc loa phóng thanh cầm tay, giọng nói lạnh lùng của anh vang vọng lấn át cả tiếng mưa gió bão bùng.",
            "\"Chào mừng các người đến với công trường của Tập đoàn Đế Vương!\"",
            "\"Các người nghĩ rằng công trường của tôi là nơi muốn đến thì đến, muốn đi thì đi sao?\"",
            "\"Lê Trọng Khải trả cho các người bao nhiêu tiền để đến đây bán mạng thế?\"",
            "Tên cầm đầu đám côn đồ run rẩy, vứt bỏ vũ khí xuống vũng bùn đất, quỳ rạp xuống đất xin tha thứ.",
            "\"Chủ... Chủ tịch Trần! Xin ngài tha mạng! Chúng tôi chỉ nhận tiền làm thuê của Lê Trọng Khải thôi!\"",
            "\"Hắn ta bảo chúng tôi đến phá hoại máy móc và dàn dựng tai nạn để đình chỉ thi công công trường của ngài!\"",
            "Trần Hùng nhếch môi cười lạnh, ánh mắt anh nhìn bọn chúng như nhìn những con chuột sa bẫy.",
            "\"Rất tốt, toàn bộ hành vi đột nhập trái phép, phá hoại tài sản và lời khai của các người đã được hệ thống camera AI ghi âm ghi hình sắc nét.\"",
            "Đúng lúc đó, còi xe cảnh sát hú vang liên hồi từ phía cổng chính công trường.",
            "Lực lượng cảnh sát hình sự tỉnh Bình Dương cùng các chiến sĩ cơ động nhanh chóng ập vào, khống chế và còng tay toàn bộ mười tên côn đồ.",
            "Trần Hùng bàn giao toàn bộ thiết bị lưu trữ dữ liệu camera an ninh và chất nổ tự chế thu giữ được cho vị trưởng đoàn cảnh sát.",
            "\"Cảm ơn sự phối hợp hỗ trợ của Chủ tịch Trần, vụ án này có đầy đủ chứng cứ pháp lý vững chắc, Lê Trọng Khải chắc chắn sẽ không thể thoát tội!\" Vị cảnh sát trưởng bắt tay Hùng đầy kính cẩn.",
            "Thu Hà đứng bên cạnh thở phào nhẹ nhõm, cô nhìn Trần Hùng bằng ánh mắt tràn đầy sự ngưỡng mộ và tình cảm sâu sắc.",
            "Trận chiến đêm mưa bão này đã chứng minh bản lĩnh, trí tuệ vượt trội và sự chuẩn bị hoàn hảo của vị Chủ tịch Đế Vương trước mọi âm mưu hiểm độc."
        ]
    },
    {
        "title": "Chương 10: Sự Sụp Đổ Của Kẻ Phản Bội",
        "sentences": [
            "Sáng hôm sau, một cơn địa chấn truyền thông thực sự đã quét sạch toàn bộ giới kinh doanh tỉnh Bình Dương và miền Nam.",
            "Lê Trọng Khải bị lực lượng cảnh sát bắt khẩn cấp ngay tại cửa khẩu sân bay Tân Sơn Nhất khi đang cố gắng dùng hộ chiếu giả để trốn sang nước ngoài.",
            "Với các tội danh phá hoại tài sản công trình trọng điểm quốc gia, thuê giang hồ giết người không thành và lừa đảo chiếm đoạt tài sản, hắn phải đối mặt với mức án tù chung thân.",
            "Công ty Bình Phát chính thức tuyên bố phá sản hoàn toàn, toàn bộ tài sản và các dự án dang dở của họ đều bị tòa án niêm phong để phát mại bản nợ.",
            "Gia đình nhà vợ cũ của Trần Hùng cũng lâm vào cảnh trắng tay hoàn toàn khi toàn bộ biệt thự, siêu xe đều bị ngân hàng tịch thu để siết nợ.",
            "Thu Thủy và bà Bích bỗng chốc bị tống ra đường, phải dắt díu nhau thuê một căn phòng trọ chật hẹp, ẩm thấp ở khu lao động nghèo Thuận An.",
            "Một buổi chiều âm u, Trần Hùng đang ngồi trong phòng làm việc sang trọng của mình trên tầng cao Becamex Tower.",
            "Trợ lý Lâm gõ cửa bước vào, vẻ mặt có chút ái ngại báo cáo.",
            "\"Chủ tịch, Thu Thủy - vợ cũ của ngài đang đứng dưới sảnh tòa nhà, cô ta khóc lóc thảm thiết và cầu xin được gặp ngài một lần.\"",
            "Trần Hùng im lặng một lát, ánh mắt anh nhìn ra khoảng không bao la ngoài cửa sổ kính sát đất.",
            "\"Cho cô ta lên đây, tôi muốn giải quyết dứt điểm mọi chuyện dây dưa từ quá khứ.\"",
            "Vài phút sau, Thu Thủy bước vào phòng làm việc.",
            "Cô ta không còn vẻ sang trọng, lộng lẫy và kiêu ngạo của một tiểu thư hào môn ngày nào.",
            "Gương mặt cô ta tiều tụy, nhợt nhạt, mặc bộ quần áo cũ kỹ dính vài vệt bẩn, đôi mắt sưng húp vì khóc quá nhiều.",
            "Nhìn thấy Trần Hùng ngồi uy nghiêm trên chiếc ghế chủ tịch da bò cao cấp, khí chất bức người, Thu Thủy lập tức quỳ sụp xuống sàn gạch lạnh lẽo.",
            "Cô ta bò đến gần bàn làm việc của anh, khóc lóc thảm thiết, hai tay bấu chặt lấy thành ghế.",
            "\"Hùng... Hùng ơi! Em biết lỗi rồi! Em thực sự có mắt không tròng, bị những lời ngon ngọt của Lê Trọng Khải che mắt!\"",
            "\"Xin anh hãy nghĩ đến tình nghĩa vợ chồng ba năm qua mà tha thứ cho em, cho em quay lại bên anh!\"",
            "\"Em hứa sẽ làm một người vợ ngoan hiền, hầu hạ anh suốt đời, không bao giờ đòi hỏi gì nữa!\"",
            "\"Mẹ em cũng đã biết lỗi rồi, bà ấy đang bị bệnh nặng ở phòng trọ, xin anh hãy rủ lòng thương cứu giúp gia đình em với!\"",
            "Trần Hùng lạnh lùng nhìn người phụ nữ đang quỳ rạp dưới chân mình, ánh mắt anh không hề có một tia thương xót hay lay động nào.",
            "Anh đứng dậy, chậm rãi bước ra khỏi bàn làm việc, đứng từ trên cao nhìn xuống cô ta đầy khinh bỉ.",
            "\"Tình nghĩa vợ chồng ba năm sao? Cô dám dùng từ đó trước mặt tôi sau tất cả những gì cô đã làm à?\"",
            "\"Khi tôi làm thợ hồ dầm mưa dãi nắng vì gia đình cô, cô nhìn tôi như nhìn một con vật dơ bẩn.\"",
            "\"Cô ngoại tình với Lê Trọng Khải ngay trước mắt tôi, đuổi tôi ra khỏi nhà không một đồng dính túi.\"",
            "\"Bây giờ thấy tôi giàu sang phú quý, các người trắng tay liền quỳ gối xin tha thứ để bám lấy tôi sao?\"",
            "\"Thu Thủy, cô nghe cho rõ đây: Kẻ phản bội thì không xứng đáng nhận được sự thương hại.\"",
            "\"Cô thậm chí còn không xứng đáng để chạm vào gót ủng dính bùn đất ngày xưa của tôi!\"",
            "\"Trợ lý Lâm! Tiễn khách! Và cấm người phụ nữ này bước vào bất kỳ khu vực nào thuộc sở hữu của Đế Vương từ nay về sau!\"",
            "Nói xong, Trần Hùng dứt khoát quay lưng đi vào phòng nghỉ bên trong, không thèm nhìn lại cô ta dù chỉ một lần.",
            "Thu Thủy bị hai nhân viên bảo vệ lôi đi xềnh xệch ra khỏi phòng trong tiếng gào khóc vô vọng và sự nhục nhã tột cùng."
        ]
    },
    {
        "title": "Chương 11: Bản Hợp Đồng Tiền Hôn Nhân Kỳ Lạ",
        "sentences": [
            "Sau những sóng gió liên tiếp, công trường siêu dự án VSIP 3 đã hoàn thành phần móng và bắt đầu bước vào giai đoạn lắp đặt kết cấu khung thép vĩ đại.",
            "Mối quan hệ giữa Trần Hùng và Thu Hà cũng âm thầm đơm hoa kết trái qua những ngày tháng cùng nhau lăn lộn trên công trường nắng gió.",
            "Một buổi chiều hoàng hôn rực rỡ, ánh mặt trời đỏ rực như lửa nhuộm hồng cả bầu trời Bình Dương và phản chiếu lên những tòa nhà Becamex kiêu hãnh.",
            "Trần Hùng hẹn Thu Hà ra khu vực ban công yên tĩnh trên tầng cao Becamex Tower, nơi có thể nhìn bao quát toàn bộ đại lộ Becamex tấp nập xe cộ.",
            "Thu Hà mặc chiếc váy trắng đơn giản nhưng vô cùng thanh lịch, gió chiều khẽ thổi bay mái tóc đen dài của cô tạo nên một vẻ đẹp vô cùng cuốn hút.",
            "Cô đứng tựa vào lan can, nhấp một ngụm trà ô long ấm áp, đôi mắt đen láy nhìn về phía chân trời xa xăm.",
            "Trần Hùng bước đến bên cạnh cô, bờ vai rộng lớn của anh che chở cho cô trước những cơn gió chiều se lạnh.",
            "\"Hà, ba năm qua tôi sống trong sự khinh miệt và phản bội, tôi đã từng nghĩ mình sẽ không bao giờ tin vào tình yêu nữa.\"",
            "\"Nhưng từ khi gặp cô trên công trường nắng cháy ấy, sự kiên cường, liêm chính và chân thành của cô đã sưởi ấm lại trái tim sắt đá của tôi.\"",
            "\"Tôi muốn cùng cô đi hết quãng đời còn lại, cùng cô xây dựng nên những công trình vĩ đại nhất.\"",
            "\"Cô có nguyện ý trở thành phu nhân của Chủ tịch Tập đoàn Đế Vương không?\" Hùng nhẹ nhàng cầm lấy bàn tay mềm mại của cô, ánh mắt say đắm.",
            "Thu Hà khẽ đỏ mặt, cô nhìn sâu vào đôi mắt chân thành của Hùng, nụ cười hạnh phúc nở trên môi.",
            "\"Hùng, tôi yêu anh không phải vì anh là Chủ tịch Đế Vương sở hữu khối tài sản nghìn tỷ.\"",
            "\"Tôi yêu anh vì anh là người kỹ sư Trần Hùng có tâm, có tầm và đầy bản lĩnh dưới hố móng công trường ngày hôm đó.\"",
            "\"Tôi nguyện ý ở bên cạnh anh, nhưng tôi có một điều kiện trước khi chúng ta chính thức đính ước.\"",
            "Nói xong, Thu Hà lấy từ trong túi xách ra một tập tài liệu mỏng, đẩy về phía anh đầy nghiêm túc.",
            "\"Đây là bản dự thảo hợp đồng tiền hôn nhân do chính tay tôi soạn thảo.\"",
            "Trần Hùng nhướng mày tỏ vẻ vô cùng thích thú, anh nhận lấy tập tài liệu và mở ra đọc lướt qua.",
            "\"Điều khoản thứ nhất: Công việc là công việc, tình cảm là tình cảm. Trong phòng họp chúng ta là đối tác chuyên nghiệp, không ai được can thiệp vào quyết định kỹ thuật của người kia.\"",
            "\"Điều khoản thứ hai: Nếu có chuyện ly hôn xảy ra trong tương lai, tôi sẽ không nhận bất kỳ một đồng tài sản hay cổ phần nào của Tập đoàn Đế Vương.\"",
            "\"Tôi chỉ giữ lại những gì do chính bàn tay và khối óc của tôi làm ra.\"",
            "Trần Hùng đọc xong thì bật cười sảng khoái, tiếng cười vang vọng khắp ban công đầy kiêu hãnh.",
            "Anh nhìn người phụ nữ thông minh, tự lập và đầy tự trọng trước mặt mình bằng ánh mắt tràn đầy sự trân trọng và yêu thương vô bờ bến.",
            "\"Hà, cô thực sự là viên ngọc quý độc nhất vô nhị trên thế gian này!\"",
            "Anh rút cây bút máy mạ vàng từ túi áo vest ra, dứt khoát ký roẹt một chữ ký mạnh mẽ lên bản hợp đồng tiền hôn nhân.",
            "\"Tôi đồng ý mọi điều kiện của cô! Nhưng tôi cũng có một điều kiện thêm vào: Đám cưới của chúng ta phải được tổ chức hoành tráng nhất Bình Dương ngay trong tháng này!\"",
            "Thu Hà mỉm cười hạnh phúc, gật đầu đồng ý, để mặc cho Trần Hùng ôm chặt cô vào lòng dưới ánh hoàng hôn rực rỡ."
        ]
    },
    {
        "title": "Chương 12: Đám Cưới Nghìn Tỷ Và Kỷ Nguyên Mới",
        "sentences": [
            "Ngày hôm nay, cả thành phố mới Bình Dương như khoác lên mình một tấm áo mới rực rỡ để chào đón siêu đám cưới thế kỷ.",
            "Lễ cưới của Chủ tịch Tập đoàn Đế Vương - Trần Hùng và Nữ giám đốc giám sát kỹ thuật - Thu Hà được tổ chức hoành tráng tại Trung tâm Hội nghị Becamex.",
            "Hàng ngàn khách mời VIP là các tài phiệt sừng sỏ, các chính trị gia lẫy lừng và các đối tác chiến lược quốc tế đều tề tựu đông đủ để chúc phúc.",
            "Toàn bộ khuôn viên lễ đường được trang trí bằng hàng vạn bông hồng trắng nhập khẩu từ Pháp và hàng triệu dải pha lê lấp lánh như một lâu đài cổ tích.",
            "Thu Hà lộng lẫy trong chiếc váy cưới đính hàng vạn viên kim cương lấp lánh được thiết kế riêng bởi nhà tạo mốt hàng đầu Paris.",
            "Cô bước đi trên thảm đỏ, tay khoác tay cha mình tiến về phía lễ đường, gương mặt rạng ngời hạnh phúc không tì vết.",
            "Trần Hùng đứng chờ cô ở bục lễ đường trong bộ vest chú rể đen lịch lãm, nụ cười rạng rỡ hạnh phúc nở trên môi cương nghị.",
            "Từ một chàng thợ hồ bị vợ cũ và mẹ vợ khinh miệt, chà đạp dưới đáy xã hội, anh đã dùng bản lĩnh và trí tuệ vươn lên đỉnh cao quyền lực.",
            "Anh đã xây dựng nên một đế chế xây dựng hùng mạnh bậc nhất Bình Dương và cưới được người phụ nữ tài sắc vẹn toàn, đáng trân trọng nhất đời mình.",
            "Hai người trao nhau chiếc nhẫn cưới kim cương lấp lánh và nụ hôn nồng cháy trước sự chứng kiến và tiếng vỗ tay vang dội như sấm rền của hàng ngàn khách mời.",
            "Sáng hôm sau, khi ánh bình minh rực rỡ mọc lên trên công trường siêu dự án VSIP Bình Dương 3.",
            "Trần Hùng và Thu Hà, dù vừa trải qua đêm tân hôn nồng nàn hạnh phúc, vẫn xuất hiện tại công trường trong trang phục bảo hộ quen thuộc.",
            "Họ không phải là những kẻ sinh ra ngậm thìa vàng chỉ biết hưởng thụ vinh hoa phú quý trên mồ hôi nước mắt của người khác.",
            "Họ là những người xây dựng tương lai bằng chính đôi tay dính đầy bụi xi măng và khối óc đầy lý tưởng của mình.",
            "Hàng ngàn công nhân hò reo vang dội, chào đón vị Chủ tịch và Phu nhân tối cao quay trở lại công trường chỉ huy thi công.",
            "Trần Hùng đứng trên bục cao, nhìn bao quát công trường rộng lớn đang thi công rầm rộ, rồi dõng dạc tuyên bố trước loa phóng thanh.",
            "\"Hôm nay, Tập đoàn Đế Vương chúng ta chính thức khởi động giai đoạn thi công hoàn thiện siêu dự án VSIP Bình Dương 3!\"",
            "\"Chúng ta sẽ biến nơi này thành trái tim kinh tế mạnh mẽ nhất, một biểu tượng của chất lượng công trình vĩnh cửu!\"",
            "\"Cảm ơn toàn thể anh em công nhân đã đồng hành cùng tôi suốt chặng đường đầy sóng gió vừa qua!\"",
            "Tiếng vỗ tay hoan hô vang dội cả một góc trời Bình Dương, kéo dài không dứt.",
            "Thu Hà đứng bên cạnh, nắm chặt tay Trần Hùng, ánh mắt cô tràn đầy niềm kiêu hãnh và tự hào khôn tả.",
            "Truyền thuyết về Trần Hùng - chàng thợ hồ nghìn tỷ vươn lên đỉnh cao bá chủ Bình Dương sẽ còn được người đời nhắc đến mãi mãi như một bài ca kiên cường vô tiền khoáng hậu."
        ]
    }
]

# 2. Build Chapters payload for update
formatted_chapters = []
for idx, chap in enumerate(chapters_data):
    # Wrap each sentence in a <p> tag
    content_html = ""
    for sentence in chap["sentences"]:
        if sentence.strip():
            content_html += f"<p>{sentence.strip()}</p>\n"
    formatted_chapters.append({
        "title": chap["title"],
        "content": content_html
    })

# Define novel details
novel_title = "THỢ HỒ NGHÌN TỶ"
novel_author = "Đế Vương"
novel_intro = '''<p><strong>&quot;Ngày tôi đến ra mắt, bà ấy nhìn đôi ủng xi măng trên chân tôi rồi phẩy tay: \\\'Thợ hồ mà dám đòi cưới con gái tôi? Trọng Khải, con rể tương lai của ta, là thiếu gia nhà giàu, đi xe hơi bóng loáng. Còn ngươi chỉ là một thằng thợ hồ rẻ rách!\\\'&quot;</strong></p><p><strong>&quot;Trần Hùng cười nhạt, gạt bỏ sự khinh khi. Ba năm chịu đựng thử thách ẩn thân đã kết thúc, vị thế Chủ tịch Tập đoàn Đế Vương chính thức thức tỉnh, thâu tóm toàn bộ siêu dự án KCN VSIP 3 và buộc toàn bộ giới tài phiệt Bình Dương phải quỳ gối xin lỗi...&quot;</strong></p><hr /><p>Trần Hùng từng là một kỹ sư xây dựng đầy tài năng, nhưng vì một chữ tình, anh chấp nhận lùi về phía sau làm thợ hồ ẩn dật để gia đình nhà vợ leo lên vị trí cao. Đổi lại, anh nhận được sự khinh miệt thấu xương từ mẹ vợ và màn ly hôn tuyệt tình từ người vợ Thu Thủy để chạy theo gã nhân tình giàu có Lê Trọng Khải.</p><p>Họ không ngờ rằng, anh chính là người thừa kế duy nhất của Tập đoàn Đế Vương – siêu thế lực kinh tế bí ẩn nắm trong tay khối tài sản khổng lồ. Đồng thời, bên cạnh anh giờ đây là Thu Hà – nữ giám đốc giám sát sắc sảo, xinh đẹp nhất ngành xây dựng Bình Dương. Trận chiến vả mặt kinh điển, thâu tóm các đại dự án nghìn tỷ và hành trình vươn lên đỉnh cao bá chủ bắt đầu!</p>'''

# 3. Create temp local json payload
draft_payload = {
    "secret_token": "ZEN_TRUYEN_2026_BYPASS",
    "story_id": STORY_ID,
    "title": novel_title,
    "intro": novel_intro,
    "author": novel_author,
    "chapters": formatted_chapters
}

local_json_path = "/Users/aaronnguyen/TN/App/doctieuthuyet/scratch/pending_novel_2197_v12.json"
with open(local_json_path, "w", encoding="utf-8") as f:
    json.dump(draft_payload, f, ensure_ascii=False, indent=2)
print(f"✓ Saved 12-chapter V12 draft payload locally to: {local_json_path}")

# 4. Upload overwrite_story_generic.php helper to FTP root
print("\nUploading overwrite_story_generic.php helper to FTP root...")
local_php_path = "/Users/aaronnguyen/TN/App/doctieuthuyet/scratch/overwrite_story_generic.php"
remote_php_name = "overwrite_story_generic.php"

try:
    ftp = ftplib.FTP(FTP_HOST, timeout=30)
    ftp.login(FTP_USER, FTP_PASS)
    with open(local_php_path, "rb") as f:
        ftp.storbinary(f"STOR {remote_php_name}", f)
    print("✓ Uploaded overwrite_story_generic.php successfully to server.")
    ftp.quit()
except Exception as e:
    print("❌ FTP Upload Error:", e)
    exit(1)

# 5. Trigger Overwrite via HTTP POST request
print("\nTriggering story overwrite on doctieuthuyet.com...")
try:
    api_url = f"{WP_URL}/{remote_php_name}"
    res = requests.post(api_url, json=draft_payload, timeout=120)
    res_data = res.json()
    
    if res_data.get('success'):
        print("=" * 60)
        print("🎉 STORY OVERWRITTEN AND REFINED SUCCESSFULLY!")
        print(f"Story ID: {res_data['story_id']}")
        print(f"Title: {res_data['title']}")
        print(f"Chapters Deleted: {res_data['deleted_chapters_count']}")
        print(f"Chapters Inserted: {res_data['inserted_chapters_count']}")
        print("=" * 60)
        
        # 6. Clean up helper script from remote server for security
        try:
            ftp = ftplib.FTP(FTP_HOST, timeout=30)
            ftp.login(FTP_USER, FTP_PASS)
            ftp.delete(remote_php_name)
            print(f"✓ Deleted remote helper script {remote_php_name}.")
            ftp.quit()
        except Exception as clean_err:
            print("⚠️ Failed to clean up remote helper:", clean_err)
            
        # 7. Sync local existing_novels.json registry
        existing_path = "/Users/aaronnguyen/TN/App/doctieuthuyet/existing_novels.json"
        if os.path.exists(existing_path):
            try:
                with open(existing_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                
                updated = False
                for novel in data:
                    if novel.get("id") == STORY_ID:
                        novel["title"] = novel_title
                        novel["intro"] = novel_intro
                        updated = True
                        break
                
                if not updated:
                    data.append({
                        "id": STORY_ID,
                        "title": novel_title,
                        "slug": "ta-o-binh-duong-lam-chu-thau-va-mat-sep-lon-cuoi-luon-nu-giam-doc-giam-sat",
                        "intro": novel_intro
                    })
                
                with open(existing_path, "w", encoding="utf-8") as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
                print("✓ Synced local registry existing_novels.json.")
            except Exception as sync_err:
                print("⚠️ Failed to sync existing_novels.json:", sync_err)
                
    else:
        print("❌ Overwrite failed:", res_data.get('error', 'Unknown Error'))
        
except Exception as e:
    print("❌ HTTP trigger call failed:", e)
