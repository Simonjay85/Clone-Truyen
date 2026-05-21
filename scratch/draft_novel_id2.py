# -*- coding: utf-8 -*-
import json
import os

def build_novel_2():
    novel = {
        "title": "Cô Vợ Hào Môn Khinh Tôi Vô Dụng, Cả Hà Ngoại Biết Tôi Là Chủ Tịch Tập Đoàn Thép",
        "author": "Đông Hải Cư Sĩ",
        "genre": "Sảng Văn",
        "intro": (
            "<p><strong>\"Lê Minh Khôi, chủ tịch bí ẩn của tập đoàn thép Vạn Lợi lớn nhất miền Bắc, lấm lem bụi sắt trong bộ đồng phục công nhân sờn rách, bị cô vợ hào môn Nguyễn Mỹ Hạnh ném thẳng tờ đơn ly hôn vào mặt: 'Anh chỉ là thằng bốc vác quèn vô tích sự, cút khỏi gia tộc họ Nguyễn trước khi làm bẩn gạch nền nhà tao!'...\"</strong></p>"
            "<p>Thế nhưng, chúng không thể ngờ chiếc áo công nhân đẫm mồ hôi ấy thuộc về người nắm giữ mạch máu thép của toàn bộ đại công trình quốc gia, sở hữu khối tài sản nghìn tỷ mà cả gia tộc họ Nguyễn thèm khát. Khi tập đoàn Trường Sinh của nhà vợ đối mặt với khủng hoảng đứt gãy nguồn cung thép và nguy cơ phá sản cận kề, họ đã phải quỳ rạp cầu xin sự ban ơn của vị chủ tịch ẩn danh. Cú vả mặt chấn động nổ ra ngay tại đại sảnh Vạn Lợi, bóc trần những âm mưu bẩn thỉu của gã anh rể tham lam và thâu tóm toàn bộ gia sản nhà vợ trong sự ngỡ ngàng của báo chí và giới tài chính Hà Ngoại.</p>"
        ),
        "cover_prompt": (
            "A high-end book cover, highly detailed web novel illustration style, a powerful and handsome young Vietnamese man in a sharp navy suit, "
            "standing with a confident and cold look near a high-tech steel smelting furnace with sparks flying in a modern industrial setting. "
            "Beside him is a beautiful female luxury lawyer in professional clothes. In the background are giant industrial structures and modern Hanoi skyline. "
            "Cinematic neon lighting, rich dramatic shadows, premium colors."
        ),
        "chapters": []
    }

    # Chapter 1: Tờ Đơn Ly Hôn Rẻ Tiền
    chap1_lines = [
        "Tiệc mừng thọ bảy mươi tuổi của ông nội Nguyễn Mỹ Hạnh được tổ chức xa hoa tại khách sạn năm sao lớn nhất Hà Ngoại.",
        "Tiếng nhạc du dương quyện cùng mùi nước hoa đắt tiền của giới thượng lưu tạo nên một bầu không khí vô cùng ngột ngạt.",
        "Lê Minh Khôi đứng ở góc phòng tiệc, mặc bộ quần áo kaki giản dị mua ở chợ Đồng Xuân, tay cầm chiếc hộp gỗ nhỏ bọc nhung đỏ.",
        "Bên trong chiếc hộp là một mảnh phôi thép thô sơ, được chạm khắc hoa văn thủ công vô cùng tinh xảo mà chính tay anh chế tác.",
        "Đối với một người thợ luyện thép, phôi thép tinh luyện chính là lời chúc thọ vững chắc như bàn thạch, trường tồn cùng thời gian.",
        "Thế nhưng, món quà tâm huyết của anh chưa kịp dâng lên thì đã bị gã anh họ Nguyễn Tiến Đạt giật phắt lấy rồi ném thẳng vào thùng rác bên cạnh.",
        "\"Cái thứ sắt vụn bẩn thỉu này mà cũng dám mang đến chúc thọ ông nội sao?\"",
        "\"Nhìn bộ dạng nghèo hèn, bám đầy bụi sắt của mày xem, thật làm xấu mặt gia tộc họ Nguyễn chúng ta trước các quan khách!\"",
        "Đạt cười lớn đầy hách dịch, giọng nói chói tai của gã vang vọng khắp sảnh tiệc, thu hút hàng trăm ánh mắt khinh miệt đổ dồn về phía Khôi.",
        "Nguyễn Mỹ Hạnh, vợ của Khôi, đứng bên cạnh Đạt trong chiếc váy dạ hội sang trọng lấp lánh.",
        "Cô nhìn Khôi bằng ánh mắt lạnh lùng, ghê tởm, không hề có một chút tình nghĩa vợ chồng suốt ba năm qua.",
        "Hạnh mở chiếc túi xách hàng hiệu, rút ra một tập hồ sơ dày cộm rồi ném thẳng vào ngực Khôi.",
        "Tờ giấy trắng rơi lạch cạch xuống sàn nhà bóng loáng, hiện rõ dòng chữ đen chói mắt: Đơn Ly Hôn.",
        "\"Ký đi, Lê Minh Khôi.\"",
        "\"Tôi đã chịu đựng sự vô dụng, nghèo hèn của anh quá đủ rồi.\"",
        "\"Gia đình tôi làm vật liệu xây dựng cao cấp, không thể có một thằng chồng làm công nhân bốc vác quèn ở nhà kho thép.\"",
        "Bố vợ của Khôi, ông Nguyễn Văn Trường – CEO của tập đoàn Trường Sinh, thong thả bước tới, nhấp một ngụm rượu vang đắt đỏ.",
        "\"Cậu Lê Minh Khôi này, năm xưa cha tôi thương hại cậu là trẻ mồ côi có tay nghề cơ khí, mới ép gả Mỹ Hạnh cho cậu.\"",
        "\"Nhưng bây giờ cha tôi đã lẫn rồi, quyền quyết định gia tộc nằm trong tay tôi.\"",
        "\"Trường Sinh sắp ký hợp đồng cung cấp vật liệu trị giá năm trăm tỷ với siêu tập đoàn thép Vạn Lợi ở khu công nghiệp phía Bắc.\"",
        "\"Chúng tôi không thể để một thằng con rể nghèo kiết xác làm ảnh hưởng đến hình ảnh của tập đoàn trước đối tác lớn.\"",
        "\"Cút khỏi gia tộc họ Nguyễn ngay lập tức, đừng để cái mùi dầu mỡ của mày làm bẩn nền gạch của khách sạn này!\"",
        "Hàng trăm vị khách hào môn xung quanh đồng loạt bật cười chế giễu, những lời bàn tán xầm xì đầy ác ý như những mũi dao nhọn hoắt đâm vào Khôi.",
        "Khôi đứng lặng im giữa vòng vây khinh miệt, tấm lưng vẫn thẳng tắp như một thanh thép được tôi luyện trong lò lửa nghìn độ.",
        "Gương mặt anh không hề có một chút tức giận hay đau khổ, chỉ có sự bình thản đến đáng sợ.",
        "Anh cúi xuống nhặt tờ đơn ly hôn lên, lấy chiếc bút bi thiên long trong túi áo ra ký một đường dứt khoát.",
        "\"Nguyễn Mỹ Hạnh, ba năm qua tôi đã làm tròn bổ phận của một người chồng, âm thầm giúp đỡ tập đoàn Trường Sinh qua nhiều sóng gió.\"",
        "\"Hôm nay các người đã chọn con đường này, hy vọng sau này các người sẽ không hối hận.\"",
        "Khôi ném chiếc bút xuống bàn rượu, quay lưng sải bước rời khỏi phòng tiệc sang trọng.",
        "Sau lưng anh, tiếng cười đắc thắng của gã anh họ Tiến Đạt và vẻ mặt lạnh lùng của Mỹ Hạnh vẫn tiếp tục vang lên.",
        "Họ không hề biết rằng, người đàn ông mà họ vừa đuổi đi như một con chó hoang chính là Lê Minh Khôi.",
        "Anh là Chủ tịch hội đồng quản trị ẩn danh, người sở hữu tuyệt đối 100% cổ phần của tập đoàn thép Vạn Lợi danh tiếng."
    ]

    # Chapter 2: Khủng Hoảng Đột Ngột
    chap2_lines = [
        "Sáng ngày hôm sau, bầu không khí tại trụ sở tập đoàn vật liệu xây dựng Trường Sinh bao trùm bởi sự hoảng loạn tột độ.",
        "Các cuộc điện thoại từ các nhà thầu liên tục reo vang dồn dập, tiếng la hét của các trưởng phòng vang khắp các hành lang.",
        "Bên trong phòng họp hội đồng quản trị, ông Nguyễn Văn Trường đập mạnh tay xuống bàn, gương mặt đỏ gay vì tức giận và lo sợ.",
        "\"Cái gì? Tập đoàn thép Vạn Lợi đột ngột chấm dứt đàm phán hợp đồng cung cấp thép cốt thép xây dựng cho chúng ta sao?\"",
        "\"Ai là người đưa ra quyết định này? Lý do là gì?\"",
        "Gã trưởng phòng mua hàng run rẩy báo cáo: \"Thưa Chủ tịch, phía Vạn Lợi chỉ gửi một thông báo ngắn gọn.\"",
        "\"Họ nói rằng tập đoàn Trường Sinh không đủ tiêu chuẩn đạo đức kinh doanh để làm đối tác của họ.\"",
        "\"Toàn bộ các đơn hàng thép đã ký trước đó cũng bị đình chỉ cung cấp vô thời hạn để phục vụ thanh tra chất lượng.\"",
        "Nguyễn Mỹ Hạnh mặt cắt không còn giọt máu, cô đứng bật dậy: \"Không thể như thế được!\"",
        "\"Chúng ta đã đặt cọc năm mươi tỷ đồng từ khoản vay Agribank cho mẻ thép này.\"",
        "\"Nếu không có thép Vạn Lợi để bàn giao cho dự án tuyến đường cao tốc phía Bắc vào tuần tới, Trường Sinh sẽ bị phạt hợp đồng ba trăm tỷ!\"",
        "\"Lúc đó, ngân hàng sẽ siết nợ toàn bộ tài sản, Trường Sinh chắc chắn sẽ phá sản!\"",
        "Tiến Đạt đứng bên cạnh, mồ hôi lạnh chảy ròng ròng trên trán: \"Bác hai, hay là chúng ta trực tiếp đến văn phòng Vạn Lợi để xin gặp vị Chủ tịch ẩn danh của họ?\"",
        "\"Nghe nói vị Chủ tịch này cực kỳ trẻ tuổi và bí ẩn, nắm quyền sinh sát toàn bộ nguồn cung thép xây dựng miền Bắc.\"",
        "\"Nếu chúng ta quỳ xin ông ấy cứu giúp, có lẽ vẫn còn một con đường sống.\"",
        "Ông Trường nghiến răng: \"Chuẩn bị xe ngay lập tức! Mỹ Hạnh, Tiến Đạt, hai đứa đi cùng ta đến Vạn Lợi!\"",
        "\"Chúng ta phải bằng mọi giá gặp được người đứng đầu tập đoàn thép để giải quyết cuộc khủng hoảng này!\"",
        "Cùng lúc đó, tại khu văn phòng cao cấp của tập đoàn thép Vạn Lợi, Lê Minh Khôi đang ngồi trên chiếc ghế da chủ tịch sang trọng.",
        "Anh đã thay bộ quần áo lao động rách nát bằng một bộ vest Ý may đo thủ công màu xanh đen lịch lãm, toát lên phong thái uy nghiêm của một bậc đế vương.",
        "Đứng trước bàn làm việc của anh là Trần Quốc Nam, phó giám đốc điều hành danh tiếng của Vạn Lợi.",
        "\"Chủ tịch, gia đình họ Nguyễn của tập đoàn Trường Sinh đang quỳ xin gặp anh ở sảnh lớn tầng một.\"",
        "\"Họ mang theo rất nhiều quà cáp và đang khóc lóc cầu xin sự ban ơn.\"",
        "Khôi xoay nhẹ chiếc bút máy Montblanc đắt đỏ, khóe môi hiện lên một nụ cười lạnh lùng.",
        "\"Cho họ đợi ở sảnh ba tiếng đồng hồ.\"",
        "\"Sau đó, đưa họ vào phòng họp tổng thống lớn nhất.\"",
        "\"Tôi muốn chính tay mình bóc trần bộ mặt thật của những kẻ hống hách đó.\"",
        "Nam gật đầu kính cẩn: \"Rõ, thưa Chủ tịch! Tôi sẽ sắp xếp ngay lập tức.\"",
        "Dưới sảnh lớn của tòa nhà Vạn Lợi, ông Trường, Mỹ Hạnh và Tiến Đạt đang đứng ngồi không yên giữa sự dòm ngó của nhân viên.",
        "Họ phải chịu đựng sự khinh miệt của những người bảo vệ, những người mà ngày hôm qua họ còn coi như cỏ rác.",
        "Mỹ Hạnh nắm chặt chiếc túi xách, trong lòng dấy lên một cảm giác bất an kỳ lạ mà cô không thể lý giải nổi.",
        "Cô chợt nghĩ đến Lê Minh Khôi, người chồng cũ mà cô vừa đuổi đi đêm qua.",
        "Nhưng cô nhanh chóng gạt ý nghĩ đó ra khỏi đầu, tự nhủ một thằng bốc vác nghèo hèn thì làm sao có thể xuất hiện ở một nơi sang trọng như thế này."
    ]

    # Chapter 3: Cuộc Gặp Gỡ Ở Phòng VIP
    chap3_lines = [
        "Sau ba tiếng đồng hồ chờ đợi mỏi mòn dưới sảnh lớn, ba người nhà họ Nguyễn cuối cùng cũng được nhân viên dẫn lên tầng cao nhất.",
        "Cánh cửa gỗ gõ đỏ của phòng họp tổng thống mở ra, để lộ một không gian vô cùng sang trọng với góc nhìn panorama toàn cảnh Hà Ngoại.",
        "Ông Trường, Mỹ Hạnh và Tiến Đạt bước vào với vẻ mặt đầy khúm núm, cúi đầu chào phó giám đốc Trần Quốc Nam đang đứng chờ sẵn.",
        "\"Chào Giám đốc Nam! Trăm sự nhờ anh giúp đỡ giới thiệu chúng tôi với vị Chủ tịch tôn kính!\"",
        "Ông Trường vội vàng dâng lên một chiếc hộp gỗ sồi chứa chai rượu vang trị giá hai trăm triệu đồng.",
        "Nam nhìn chai rượu bằng ánh mắt thờ ơ, xua tay ra hiệu cho thư ký mang đi chỗ khác.",
        "\"Ông Trường, quà cáp không có tác dụng với Chủ tịch của chúng tôi đâu.\"",
        "\"Chủ tịch quyết định cắt nguồn cung của Trường Sinh là vì các người đã vi phạm nghiêm trọng quy chuẩn đạo đức nghề nghiệp.\"",
        "Mỹ Hạnh bước lên, giọng nói khẩn khoản: \"Thưa anh Nam, có phải có sự hiểu lầm nào ở đây không?\"",
        "\"Tập đoàn Trường Sinh luôn tuân thủ pháp luật, chất lượng vật liệu của chúng tôi đều đạt chuẩn ISO.\"",
        "Nam cười khẩy, mở chiếc máy tính bảng đẩy sang trước mặt ba người.",
        "Trên màn hình hiện lên hàng chục hóa đơn mua bán khống, biên bản giao nhận thép phế liệu kém chất lượng giả mạo nhãn hiệu Vạn Lợi.",
        "Tất cả đều do gã anh họ Nguyễn Tiến Đạt ký tên đóng dấu, cấu kết với một vài quản lý kho cũ của Vạn Lợi để rút ruột công trình.",
        "\"Cái này... cái này là do Tiến Đạt tự ý làm! Chúng tôi không hề biết!\" Ông Trường tái mặt, lập tức đẩy toàn bộ trách nhiệm sang gã cháu họ.",
        "Tiến Đạt quỳ sụp xuống sàn nhà, mặt cắt không còn giọt máu, run rẩy van xin: \"Giám đốc Nam cứu tôi với! Tôi chỉ làm theo chỉ đạo của bác hai để kiếm thêm chút tiền chênh lệch thôi!\"",
        "Bầu không khí trong phòng họp trở nên vô cùng căng thẳng, tiếng cãi vã đùn đẩy trách nhiệm của ba người nhà họ Nguyễn khiến Nam cảm thấy ghê tởm.",
        "Đúng lúc này, cánh cửa phòng VIP bên trong từ từ mở ra.",
        "Tiếng bước chân vững chãi gõ nhịp đều đặn trên nền đá cẩm thạch thu hút toàn bộ sự chú ý của mọi người.",
        "Một bóng người cao lớn, khoác trên mình bộ vest Ý sang trọng bước ra, theo sau là hai vệ sĩ cao to lực lưỡng.",
        "Gương mặt góc cạnh, đôi mắt sắc bén như chim ưng và thần thái uy nghiêm của người đàn ông khiến cả phòng họp im phăng phắc.",
        "Mỹ Hạnh ngước mắt lên nhìn, và ngay lập tức, toàn bộ thế giới của cô như sụp đổ hoàn toàn.",
        "Đôi mắt cô trợn trừng lên vì kinh hoàng, chiếc túi xách đắt tiền trên tay rơi phịch xuống đất, son phấn văng tung tóe.",
        "\"Lê... Lê Minh Khôi?!\"",
        "\"Sao có thể là anh?! Anh làm gì ở đây trong bộ dạng này?!\"",
        "Tiến Đạt và ông Trường cũng đồng loạt há hốc mồm, đứng sững như trời trồng, không thể tin nổi vào mắt mình.",
        "Người đàn ông mặc bộ vest trị giá hàng trăm triệu, được phó giám đốc điều hành cúi đầu kính cẩn chào đón lại chính là thằng con rể nghèo hèn bị họ sỉ nhục đêm qua.",
        "Khôi điềm tĩnh bước đến chiếc ghế chủ tịch ở đầu bàn, thong thả ngồi xuống, hai tay đan vào nhau.",
        "\"Nguyễn Mỹ Hạnh, chúng ta lại gặp nhau rồi.\"",
        "\"Tôi đã nói đêm qua là các người đừng hối hận, sao hôm nay lại vội vàng đến đây quỳ lạy thế này?\"",
        "Giọng nói trầm thấp của Khôi vang lên như tiếng sấm nổ ngang tai ba người nhà họ Nguyễn.",
        "Mỹ Hạnh lùi lại hai bước, gương mặt trắng bệch không còn một giọt máu, lồng ngực phập phồng dữ dội trong sự hoảng loạn tột cùng.",
        "Cô nhận ra, người chồng mà cô khinh thường suốt ba năm qua chính là Steel King đứng đầu cả ngành thép miền Bắc."
    ]

    # Chapter 4: Cú Vả Mặt Chấn Động Đại Sảnh
    chap4_lines = [
        "Phòng họp tổng thống rộng lớn lúc này im lặng đến mức có thể nghe thấy cả tiếng thở gấp gáp của ông Nguyễn Văn Trường.",
        "Nguyễn Mỹ Hạnh run rẩy tiến lên một bước, nước mắt lã chã rơi trên khuôn mặt trang điểm cầu kỳ của cô.",
        "\"Khôi... anh Khôi... chuyện đêm qua chỉ là sự hiểu lầm...\"",
        "\"Tại em bị áp lực công việc, bị Tiến Đạt xúi giục nên mới hành động dại dột như vậy...\"",
        "\"Chúng ta vẫn là vợ chồng ba năm qua mà anh, xin anh hãy vì chút tình nghĩa cũ mà cứu lấy tập đoàn Trường Sinh!\"",
        "Cô lao đến định nắm lấy vạt áo vest của Khôi, nhưng hai vệ sĩ lập tức bước lên một bước chặn đứng cô lại đầy lạnh lùng.",
        "Khôi nhìn cô bằng ánh mắt lạnh lẽo như băng tuyết Đông Bắc, không hề có một chút dao động cảm xúc nào.",
        "\"Tình nghĩa cũ sao?\"",
        "\"Ngày tôi dâng lên mảnh phôi thép chạm khắc thủ công chúc thọ ông nội, các người đã ném nó vào thùng rác.\"",
        "\"Ngày tôi bưng nước rửa chân cho mẹ cô, bà ta đã cố ý đổ cả thau nước nóng vào chân tôi.\"",
        "\"Ngày các người ném tờ đơn ly hôn vào mặt tôi, các người có nghĩ đến hai chữ tình nghĩa không?\"",
        "Ông Nguyễn Văn Trường lúc này cũng vứt bỏ toàn bộ sự kiêu ngạo của một CEO, quỳ rụp xuống trước mặt Khôi.",
        "\"Con rể... Khôi ơi... là bố sai rồi! Bố bị mù mới không nhận ra long phượng giữa loài người như con!\"",
        "\"Xin con hãy ra lệnh cho Vạn Lợi tiếp tục cung cấp thép cho Trường Sinh, nếu không gia sản cả đời của bố sẽ tiêu tan mất!\"",
        "Khôi khẽ cười nhạt, nụ cười mang theo sự khinh miệt tột cùng dành cho những kẻ hèn hạ trước mắt.",
        "\"Nguyễn Văn Trường, ông không cần gọi tôi là con rể nữa, tôi đã ký đơn ly hôn rồi.\"",
        "\"Hơn nữa, việc Vạn Lợi dừng cung cấp thép không chỉ vì chuyện cá nhân của tôi với các người.\"",
        "\"Trần Quốc Nam, đọc báo cáo kiểm toán cho họ nghe.\"",
        "Nam lập tức mở file tài liệu, giọng nói dõng dạc vang lên đầy đanh thép trước sự chứng kiến của giới truyền thông vừa được mời vào.",
        "\"Theo báo cáo kiểm toán của C03 phối hợp cùng phòng an ninh Vạn Lợi, tập đoàn Trường Sinh đã cố tình tráo đổi ba mươi ngàn tấn thép kết cấu cường độ cao của Vạn Lợi bằng thép phế liệu rẻ tiền nhập khẩu trái phép từ biên giới.\"",
        "\"Hành vi gian lận này đã trực tiếp gây ra sự cố nứt dầm bê tông tại dự án cầu vượt quốc lộ Hà Ngoại tuần trước.\"",
        "\"Tiến Đạt đã nhận hối lộ năm mươi tỷ đồng từ nhà cung cấp lậu để làm giả giấy tờ kiểm nghiệm chất lượng.\"",
        "\"Tất cả hồ sơ chứng cứ và file ghi âm giao dịch đã được chúng tôi chuyển giao hoàn toàn cho cơ quan cảnh sát điều tra tội phạm về kinh tế.\"",
        "Tiến Đạt nghe xong liền ngất xỉu ngay tại chỗ, cơ thể gã đổ rụp xuống sàn nhà như một bao cát.",
        "Mỹ Hạnh và ông Trường hoảng loạn tột độ, họ hiểu rằng đây không còn là vấn đề kinh doanh thông thường nữa, mà là án hình sự nghiêm trọng.",
        "Đúng lúc này, tiếng còi xe cảnh sát hú vang dồn dập dưới sân tòa nhà Vạn Lợi.",
        "Một đoàn chiến sĩ cảnh sát kinh tế mặc sắc phục uy nghiêm bước vào phòng họp, trưng ra lệnh bắt khẩn cấp đóng dấu đỏ chói.",
        "\"Nguyễn Tiến Đạt! Nguyễn Văn Trường! Các ông bị bắt khẩn cấp về hành vi lừa đảo chiếm đoạt tài sản và vi phạm quy định về xây dựng gây hậu quả nghiêm trọng!\"",
        "Chiếc còng số tám lạnh ngắt lập tức bập vào tay Trường và Đạt trước sự chứng kiến của hàng chục ống kính phóng viên báo chí.",
        "Mỹ Hạnh gào khóc thảm thiết, quỳ lạy dưới chân Khôi: \"Khôi ơi! Cứu bố em với! Em lạy anh! Em sẽ làm nô lệ cho anh cả đời, xin anh hãy cứu gia đình em!\"",
        "Khôi đứng dậy, chỉnh lại cổ áo vest thẳng thớm, quay lưng đi thẳng vào phòng làm việc bên trong.",
        "\"Đưa họ đi, từ hôm nay Hà Ngoại sẽ không còn tập đoàn Trường Sinh nữa.\""
    ]

    # Chapter 5: Vương Quốc Thép Mới
    chap5_lines = [
        "Một tháng sau vụ bê bối chấn động ngành xây dựng miền Bắc, tập đoàn Trường Sinh chính thức tuyên bố phá sản do không thể thanh toán các khoản nợ quá hạn.",
        "Toàn bộ tài sản thế chấp bao gồm trụ sở tập đoàn, biệt thự hào môn của họ Nguyễn và các dự án dang dở đều bị ngân hàng Agribank niêm yết đấu giá công khai.",
        "Người đứng ra mua lại toàn bộ số tài sản đó với mức giá tượng trưng một nghìn đồng kèm theo cam kết bảo lãnh toàn bộ khoản nợ chính là tập đoàn thép Vạn Lợi.",
        "Thương hiệu vật liệu xây dựng Trường Sinh được tái cấu trúc hoàn toàn dưới cái tên mới: Vạn Lợi Logistics & Materials.",
        "Lê Minh Khôi đứng bên cửa kính sát đất của văn phòng chủ tịch mới đặt tại đỉnh tòa nhà Vạn Lợi, ngắm nhìn công trường cầu vượt quốc lộ đang được thi công lại bằng những thanh thép cường độ cao sáng loáng.",
        "Làn gió mát từ sông Hồng thổi vào làm bay nhẹ vạt áo vest đen lịch lãm của anh, toát lên phong thái kiêu hùng của một Steel King thực thụ.",
        "Cửa phòng làm việc gõ nhẹ, Trần Quốc Nam bước vào cùng với một tập hồ sơ nhân sự mới.",
        "\"Chủ tịch, đây là danh sách nhân sự đã được thanh lọc hoàn toàn của Vạn Lợi Logistics.\"",
        "\"Và... có một người muốn xin gặp anh để nộp đơn xin việc làm công nhân quét dọn nhà kho.\"",
        "Khôi nhướng mày: \"Ai?\"",
        "\"Là Nguyễn Mỹ Hạnh.\"",
        "Khôi quay người lại, điềm tĩnh nhìn vào tập hồ sơ, nơi có dán bức ảnh chân dung của Mỹ Hạnh trong bộ dạng tiều tụy, xơ xác không còn chút kiêu sa nào.",
        "Sau khi gia tộc sụp đổ, cha và anh họ bị kết án tù chung thân, toàn bộ tài sản bị tịch thu, cô đã bị giới thượng lưu Hà Ngoại hoàn toàn ruồng bỏ, phải đi làm thuê kiếm sống qua ngày.",
        "\"Cho cô ta vào làm việc ở kho thép phế liệu số 09 phía Bắc.\"",
        "\"Hãy để cô ta hàng ngày được nhìn thấy những mẻ thép rực rỡ được tinh luyện từ chính những đống phế thải.\"",
        "\"Đó là nơi thích hợp nhất để cô ta suy ngẫm về giá trị thực sự của một con người.\"",
        "Nam gật đầu: \"Rõ, thưa Chủ tịch! Tôi sẽ sắp xếp ngay lập tức.\"",
        "Chiều hôm đó, dưới cơn mưa phùn nhẹ của Hà Ngoại, Nguyễn Mỹ Hạnh khoác trên mình bộ đồng phục công nhân vệ sinh màu xanh bạc màu, tay cầm chiếc chổi tre quét dọn những mảnh rác bên ngoài tường rào kho thép Vạn Lợi.",
        "Cô ngước mắt nhìn lên chiếc xe siêu sang Rolls-Royce Phantom đen bóng đang từ từ chuyển bánh rời khỏi cổng tập đoàn.",
        "Qua lớp kính chống đạn tối màu, cô lờ mờ nhìn thấy gương mặt góc cạnh đầy điềm tĩnh của Lê Minh Khôi đang lướt qua.",
        "Nước mắt cô lại tuôn rơi hòa cùng nước mưa lạnh buốt, lòng ngực nghẹn ngào một nỗi hối hận muộn màng tột cùng.",
        "Cô từng khinh thường anh là thằng công nhân bẩn thỉu không xứng bước vào hào môn của cô.",
        "Để rồi giờ đây, cô phải quỳ dưới đất quét dọn từng mảnh rác dưới chân giang sơn thép vĩ đại mà anh làm chủ.",
        "Khôi ngồi phía sau xe Rolls-Royce, nhắm mắt nghỉ ngơi, chiếc xe nhanh chóng lướt đi trên con đường cao tốc thênh thang hướng về phía những công trình mới đang trỗi dậy.",
        "Đối với anh, ân oán cũ đã khép lại như một mẻ quặng xỉ được gạt bỏ khỏi lò nung khổng lồ.",
        "Phía trước anh là cả một đế chế thép Vạn Lợi đang vươn mình ra biển lớn, vững chãi, kiên cường và trường tồn mãi mãi với thời gian."
    ]

    # Convert sentences to V12 HTML structure
    def sentences_to_v12_html(lines_list):
        return "".join([f"<p>{line}</p>" for line in lines_list])

    novel["chapters"].append({
        "title": "Chương 1: Tờ Đơn Ly Hôn Rẻ Tiền",
        "content": sentences_to_v12_html(chap1_lines)
    })
    novel["chapters"].append({
        "title": "Chương 2: Khủng Hoảng Đột Ngột",
        "content": sentences_to_v12_html(chap2_lines)
    })
    novel["chapters"].append({
        "title": "Chương 3: Cuộc Gặp Gỡ Ở Phòng VIP",
        "content": sentences_to_v12_html(chap3_lines)
    })
    novel["chapters"].append({
        "title": "Chương 4: Cú Vả Mặt Chấn Động Đại Sảnh",
        "content": sentences_to_v12_html(chap4_lines)
    })
    novel["chapters"].append({
        "title": "Chương 5: Vương Quốc Thép Mới",
        "content": sentences_to_v12_html(chap5_lines)
    })

    # Save to pending_novel.json
    output_path = "/Users/aaronnguyen/TN/App/doctieuthuyet/pending_novel.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(novel, f, ensure_ascii=False, indent=2)
    
    print("=" * 60)
    print("🎉 SUCCESS: Built Novel 2 in pending_novel.json under V12 standard!")
    print("=" * 60)

if __name__ == "__main__":
    build_novel_2()
