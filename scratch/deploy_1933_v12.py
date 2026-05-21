# -*- coding: utf-8 -*-
import sys
import os
import time

sys.path.append('scratch')
import novel_editor
import upload_cover_local

STORY_ID = 1933

# Pre-written V12 Chapters for Story 1933
ch1_sentences = [
    "Tôi tên là Tô Khanh Khanh.",
    "Một con sen công sở bình thường đến mức không thể bình thường hơn.",
    "Ưu điểm duy nhất của tôi có lẽ là vận may bùng nổ đến mức vô lý.",
    "Ví dụ như hôm thứ hai tuần trước, công ty của tôi tiến hành cắt giảm mười phần trăm nhân sự do tình hình kinh tế khó khăn.",
    "Danh sách sa thải ban đầu rõ ràng là có tên tôi chễm chệ ở dòng thứ năm.",
    "Nhưng đúng lúc chiếc máy in của phòng nhân sự chạy đến tên tôi thì nó lại đột ngột kẹt giấy.",
    "Lão trưởng phòng nhân sự mắt mũi kèm nhèm, lười in lại bản mới nên cứ thế ký xoẹt một cái vào bản danh sách lỗi.",
    "Thế là tôi nghiễm nhiên thoát nạn một cách thần kỳ.",
    "Hay như chuyện thuê nhà ở quận Gò Vấp này.",
    "Bà chủ trọ vốn là một người sùng đạo Phật vô cùng thành kính.",
    "Ngày đầu tiên tôi đến xem phòng, bà cứ nhìn chằm chằm vào trán tôi rồi vỗ đùi đánh đét.",
    "Bà bảo trán tôi rộng, tai dày, mang sẵn Phật quang vạn trượng giúp tích đức cho cả dãy trọ.",
    "Ngay lập tức, bà chủ vung bút giảm liền một nửa tiền nhà cho tôi mà không cần mặc cả.",
    "Tôi cứ ngỡ cuộc đời mình là một chuỗi phúc báo ngọt ngào nhờ sự lương thiện tích lũy từ kiếp trước.",
    "Cho đến khi tôi dọn về căn hộ chung cư mini này được tròn một tuần.",
    "Mọi chuyện bắt đầu trở nên vô cùng kỳ quái.",
    "Giữa đêm hè Sài Gòn nóng như đổ lửa, trong phòng tôi không hề bật điều hòa.",
    "Nhưng cứ thỉnh thoảng lại có một luồng gió lạnh buốt thấu xương thổi xượt qua gáy tôi.",
    "Chiếc tủ lạnh cũ kỹ của tôi trống trơn không có một giọt nước.",
    "Thế mà lâu lâu vào lúc nửa đêm, nó lại phát ra những tiếng nuốt nước bọt ực ực vô cùng thèm thuồng.",
    "Nhiều lần tôi mở cửa tủ lạnh ra kiểm tra thì chỉ thấy hơi lạnh trống rỗng phả vào mặt.",
    "Nhỏ bạn thân của tôi nghe xong câu chuyện liền rùng mình trợn mắt: “Mày bị ma ám chắc rồi!”",
    "Nói đoạn, nó thần bí lục trong ví ra một tấm danh thiếp cũ kỹ duy nhất dúi chặt vào tay tôi.",
    "Tấm danh thiếp ố vàng, chất giấy nhám xịt, bên trên viết mấy chữ to đùng bằng bút lông gà: “Truyền nhân chính tông Huyền Môn — Thẩm Triệt.”",
    "Phía dưới ghi kèm dòng chữ quảng cáo: “Chuyên bắt ma diệt quỷ, kiêm dán cường lực điện thoại dạo.”",
    "Khuyến mãi đặc biệt: “Không linh hoàn tiền, tặng kèm một miếng dán cường lực chống nhìn trộm.”",
    "Còn có một dòng chữ lí nhí viết bằng bút bi: “Đánh giá năm sao hoàn lại hai mươi nghìn đồng qua ví Momo.”",
    "Tôi nhìn tấm danh thiếp mà cạn lời toàn tập.",
    "Vị đạo sĩ này có hạng mục kinh doanh thật sự phong phú và hợp thời thế.",
    "Nhưng vì quá sợ hãi luồng gió lạnh đêm qua, tôi vẫn bấm số gọi đi.",
    "Đầu dây bên kia bắt máy rất nhanh, kèm theo tiếng ồn ào của xe cộ trên đường Quang Trung.",
    "Một giọng nam trầm ấm vang lên: “A-lô, ai đấy?”",
    "“Dán cường lực thì năm mươi nghìn một máy, còn bắt ma thì hai triệu trọn gói nhé.”",
    "Tôi ngập ngừng nói: “Dạ... em muốn bắt ma ở chung cư mini đường Phan Văn Trị.”",
    "Giọng nam kia lập tức nghiêm túc hẳn: “Địa chỉ cụ thể thế nào?”",
    "“Mười lăm phút nữa tôi có mặt, đang tiện chuyến dán cường lực cho khách gần Giga Mall.”",
    "Tôi cúp máy, ngồi co rúm trên ghế sofa đợi chờ.",
    "Đúng mười lăm phút sau, tiếng gõ cửa vang lên dứt khoát.",
    "Tôi rụt rè mở cửa ra nhìn.",
    "Đứng trước mặt tôi là một thanh niên cao ráo, mặc chiếc áo phông đen giản dị và quần jeans sờn gối.",
    "Trên vai anh ta đeo một chiếc ba lô vải bố to đùng, tay phải cầm một chiếc hộp nhựa đựng dụng cụ dán màn hình.",
    "Gương mặt anh ta khá tuấn tú, góc cạnh rõ ràng nhưng ánh mắt lại toát ra vẻ lười biếng khó tả.",
    "Anh ta nhìn tôi một lượt, rồi khẽ hít một hơi thật sâu.",
    "Đôi lông mày thanh tú của anh ta lập tức nhíu chặt lại.",
    "Anh ta lẩm bẩm: “Kỳ lạ thật.”",
    "“Dương khí trên người cô dồi dào như mặt trời ban trưa, thậm chí còn mang theo chút Phật quang may mắn.”",
    "“Thứ tà ma ngoại đạo nào dám bén mảng đến gần cô chứ?”",
    "Tôi ngơ ngác: “Hả? Phật quang gì cơ ạ?”",
    "Anh ta không giải thích, chỉ xua tay: “Tôi là Thẩm Triệt.”",
    "“Cho tôi vào nhà xem thử nào.”",
    "Thẩm Triệt bước vào căn hộ nhỏ của tôi.",
    "Anh ta đặt chiếc hộp dụng cụ xuống bàn, bắt đầu rút từ trong ba lô ra một thanh kiếm bằng gỗ đào màu nâu sẫm.",
    "Thanh kiếm trông khá cũ kỹ, trên thân kiếm khắc đầy những ký tự cổ ngoằn ngoèo.",
    "Thẩm Triệt đi vòng quanh phòng khách, mũi kiếm khẽ rung lên khe khẽ.",
    "Tôi đi sát sau lưng anh ta, hai tay nắm chặt vạt áo vì sợ.",
    "Đi đến trước cửa tủ lạnh, Thẩm Triệt đột ngột dừng chân.",
    "Anh ta dùng kiếm gỗ đào gõ nhẹ vào cánh cửa tủ lạnh.",
    "Một tiếng “cọc cọc” khô khốc vang lên giữa không gian tĩnh mịch.",
    "Bỗng nhiên, từ bên trong tủ lạnh phát ra một tiếng thở dài thườn thượt.",
    "Tiếng nuốt nước bọt “ực” một cái rõ mồn một khiến tôi nổi hết da gà da vịt.",
    "Thẩm Triệt nhếch mép cười lạnh: “Lén lén lút lút, cớ sao không hiện hình?”",
    "Mũi kiếm gỗ đào đột ngột bùng phát một luồng hào quang đỏ nhạt.",
    "Cánh cửa tủ lạnh tự động bật mở cái xoạch.",
    "Một luồng âm khí đen kịt từ bên trong tràn ra ngoài.",
    "Nhưng luồng âm khí này vừa chạm vào người tôi liền như tuyết gặp ánh mặt trời, nháy mắt tan biến không còn một dấu vết.",
    "Từ trong làn khói đen, một bóng đen cao lớn lờ mờ xuất hiện.",
    "Bóng đen mang theo uy áp nặng nề, dường như là một ác quỷ vô cùng đáng sợ.",
    "Thẩm Triệt lập tức bày ra tư thế chiến đấu, kiếm gỗ đào chĩa thẳng về phía trước.",
    "Anh ta quát lớn: “Nghiệt súc phương nào dám làm loạn nhân gian!”",
    "Nhưng bóng đen kia đột ngột hét lên một tiếng thảm thiết.",
    "Nó không hề tấn công mà lập tức quay đầu, co giò chạy bán sống bán chết về phía phòng ngủ của tôi.",
    "Tôi và Thẩm Triệt ngây người nhìn theo.",
    "Bóng đen lao thẳng vào phòng ngủ, rồi biến mất hút ngay đầu giường tôi.",
    "Thẩm Triệt nắm chặt kiếm gỗ đào, thận trọng từng bước tiến vào phòng ngủ.",
    "Tôi cũng run rẩy bám theo sau.",
    "Trên chiếc giường nhỏ của tôi, con gấu bông Pikachu khổng lồ màu vàng đang nằm im lìm.",
    "Đó là con gấu bông cao một mét rưỡi mà tôi vừa trúng thưởng trong hội chợ Gò Vấp hôm kia.",
    "Mũi kiếm gỗ đào của Thẩm Triệt chọc nhẹ vào cái bụng mập mạp của con Pikachu.",
    "Đột nhiên, từ trong bụng gấu bông phát ra một giọng nói mếu máo đầy đau khổ.",
    "“Đại sư cứu mạng! Đừng đánh tôi! Tôi đầu hàng!”"
]

ch2_sentences = [
    "Cả tôi và Thẩm Triệt đều giật nảy mình trước tiếng khóc phát ra từ con Pikachu nhồi bông.",
    "Thẩm Triệt trợn mắt, mũi kiếm gỗ đào vẫn găm chặt vào bụng con Pikachu.",
    "Anh ta quát lớn: “Yêu nghiệt phương nào, trốn trong đồ chơi trẻ con làm gì?”",
    "Giọng nói từ trong bụng Pikachu lại càng thêm phần thảm thiết và tủi thân.",
    "“Đại sư ơi, tôi đâu có muốn trốn trong con mập màu vàng này đâu!”",
    "“Số tôi khổ quá mà!”",
    "Thẩm Triệt nhíu mày: “Nói rõ ràng xem nào, nếu không tôi một kiếm đánh cho ngươi hồn phi phách tán!”",
    "Con gấu bông Pikachu khẽ run lên bần bật.",
    "Giọng nói khàn đục tự xưng: “Tôi vốn là một Quỷ Vương phong kiến, bị phong ấn dưới lòng đất Gò Vấp này hơn hai trăm năm.”",
    "“Vừa mới thoát ra được vài ngày, tôi định tìm một nơi âm u lạnh lẽo để tụ tập âm khí.”",
    "“Ai ngờ đâu tôi vừa bước chân vào căn hộ này thì suýt chút nữa bị thiêu cháy thành tro bụi.”",
    "Tôi ngạc nhiên chỉ tay vào mũi mình: “Tôi á? Tôi có làm gì đâu?”",
    "Tiếng thở dài từ bụng Pikachu vang lên đầy oán hận.",
    "“Cô nương ơi, dương khí trên người cô dồi dào kinh khủng, lại còn mang cái Phật quang may mắn gì đó chói lòa cả mắt.”",
    "“Tôi vừa vào nhà, chưa kịp làm gì đã bị Phật quang của cô nướng chín năm mươi phần trăm công lực.”",
    "“Tôi sợ quá, định trốn vào tủ lạnh để làm mát vết thương.”",
    "“Nhưng cái tủ lạnh của cô cũng nhiễm dương khí từ cô, lạnh thì lạnh thật mà nó cứ như chảo dầu đốt linh hồn tôi.”",
    "“Trong lúc tuyệt vọng nhất, tôi thấy con gấu màu vàng này nằm trên giường.”",
    "“Chất liệu bông của nó vừa xốp vừa cách nhiệt tốt, màu vàng của nó lại làm tiêu hao bớt ánh sáng Phật quang của cô.”",
    "“Thế là tôi đành chui tọt vào đây trốn tạm.”",
    "“Trong này ấm áp dễ chịu vô cùng, tôi chỉ muốn ngủ yên thôi chứ có làm hại ai đâu!”",
    "Tôi ngơ ngác nhìn Thẩm Triệt.",
    "Vị đạo sĩ Huyền Môn lúc này cũng đờ người ra, vẻ mặt vô cùng vi diệu.",
    "Anh ta từ từ hạ kiếm gỗ đào xuống, ánh mắt nhìn tôi hệt như nhìn một con quái vật thời tiền sử.",
    "Thẩm Triệt lẩm bẩm: “Thể chất cực dương may mắn... quả nhiên là trăm năm khó gặp.”",
    "“Đến cả Quỷ Vương tu vi trăm năm cũng bị cô nương này vô tình hành hạ đến mức phải chui vào bụng Pikachu trốn nóng.”",
    "Tôi ngượng ngùng gãi đầu gãi tai.",
    "Tôi rụt rè hỏi: “Vậy... giờ tính sao hả anh?”",
    "“Có cần trục xuất anh ta đi không?”",
    "Nghe thấy từ “trục xuất”, con Pikachu lập tức mếu máo.",
    "“Đừng mà! Tôi chưa muốn ra ngoài đâu!”",
    "“Ra ngoài kia gặp dương khí của cô nương này là tôi tan rã mất!”",
    "“Xin đại sư và cô nương từ bi hỷ xả, cho tôi ở lại trong con gấu Pikachu này đi!”",
    "“Tôi hứa sẽ ngoan ngoãn, không quấy phá ai hết!”",
    "Thẩm Triệt khoanh tay trước ngực, hừ lạnh một tiếng.",
    "“Nói nhẹ nhàng thế mà nghe được à?”",
    "“Ngươi là Quỷ Vương âm ty, dù có phế vật thế nào thì bản chất vẫn là âm hồn cực nặng.”",
    "“Để ngươi ở đây lâu ngày sẽ làm ảnh hưởng đến phong thủy căn nhà.”",
    "Tôi nhìn con Pikachu mập mạp tội nghiệp, trong lòng bỗng thấy mềm đi.",
    "Tôi kéo nhẹ tay áo Thẩm Triệt: “Anh Thẩm ơi... hay là... cứ cho anh ta ở lại đi.”",
    "“Trông anh ta cũng đáng thương quá, vả lại cũng đâu có làm hại em.”",
    "“Tiền nhà em được giảm một nửa, coi như chia sẻ bớt không gian cho anh ta vậy.”",
    "Thẩm Triệt nhìn tôi thở dài.",
    "“Cô đúng là hiền lành quá mức quy định rồi.”",
    "Anh ta trầm ngâm một lát rồi gõ kiếm gỗ đào xuống bàn.",
    "“Muốn ở lại cũng được, nhưng phải ký hợp đồng lao động với ta.”",
    "Bụng Pikachu phát ra tiếng kêu ngơ ngác: “Hợp đồng lao động?”",
    "Thẩm Triệt gật đầu cái rụp.",
    "“Đúng vậy.”",
    "“Làm trợ lý âm ty không lương cho ta.”",
    "“Khi nào ta đi trừ tà bắt ma, ngươi phải đi theo hỗ trợ cảm ứng âm khí và bảo vệ cô nương này.”",
    "“Bù lại, ta sẽ dùng bí thuật Huyền Môn để luyện hóa âm khí của ngươi, giúp ngươi không bị Phật quang của cô nương này thiêu rụi.”",
    "“Ngươi thấy thế nào?”",
    "Con Pikachu nhồi bông im lặng ba giây, rồi gật đầu lia lịa làm hai cái tai dài đập vào nhau bành bạch.",
    "“Đồng ý! Tôi đồng ý trăm phần trăm!”",
    "“Đại sư vạn tuế! Cô nương vạn tuế!”",
    "Tôi bật cười khúc khích.",
    "Thẩm Triệt lúc này mới cất kiếm gỗ đào vào ba lô, lấy ra một miếng dán cường lực điện thoại.",
    "Anh ta điềm nhiên nói: “Xong việc bắt ma nhé.”",
    "“Giờ tôi dán cường lực cho cô luôn, bảo hành chống trầy xước ba tháng.”",
    "Tôi cạn lời, lẳng lặng đưa điện thoại cho anh ta dán."
]

ch3_sentences = [
    "Kể từ hôm đó, căn hộ nhỏ của tôi xuất hiện thêm một thành viên vô cùng đặc biệt.",
    "Chúng tôi gọi anh ta là Pika-Quỷ.",
    "Ban ngày, Pika-Quỷ ngoan ngoãn thu mình bên trong con gấu bông Pikachu khổng lồ đầu giường.",
    "Đến đêm, khi tôi đã ngủ say, anh ta mới dám bò ra ngoài dưới dạng một đốm sáng màu vàng nhạt.",
    "Tôi phát hiện ra Pika-Quỷ rất chăm chỉ.",
    "Sáng sớm thức dậy, tôi luôn thấy sàn nhà sạch bóng không một hạt bụi.",
    "Bát đĩa ăn tối hôm trước đã được rửa sạch sẽ, úp ngăn nắp trên chạn.",
    "Thậm chí quần áo phơi ngoài ban công cũng được gấp vuông vức như trong quân đội.",
    "Tôi gõ nhẹ vào đầu Pikachu: “Cảm ơn nha, Pika-Quỷ.”",
    "Bụng gấu bông khẽ rung lên nhè nhẹ, phát ra tiếng cười khì khì đầy tự hào.",
    "Tuy nhiên, Pika-Quỷ cũng có một sở thích vô cùng hiện đại.",
    "Anh ta cực kỳ nghiện xem phim hoạt hình Doraemon trên tivi.",
    "Mỗi đêm, anh ta đều dùng âm lực điều khiển chiếc điều khiển từ xa, mở tivi ở chế độ âm lượng nhỏ nhất để xem.",
    "Nhìn bóng một đốm sáng vàng bay lơ lửng trước màn hình tivi xem chú mèo máy thông minh, tôi chỉ biết cười trừ.",
    "Công việc của Thẩm Triệt dạo này cũng khấm khá hơn rất nhiều.",
    "Nhờ có Pika-Quỷ làm anten cảm ứng âm khí cực nhạy, anh ta bắt ma chuẩn xác trăm phát trăm trúng.",
    "Một buổi tối thứ bảy, Thẩm Triệt gọi điện cho tôi.",
    "“Khanh Khanh ơi, có một ca bắt ma lớn ở văn phòng bất động sản trên đường Nguyễn Oanh.”",
    "“Giám đốc ở đó chịu chi lắm, ra giá ba mươi triệu đồng.”",
    "“Em mang theo Pika-Quỷ đi cùng anh nhé, có dương khí của em đi kèm thì anh mới yên tâm.”",
    "Tôi lập tức đồng ý.",
    "Tôi ôm con Pikachu khổng lồ bỏ vào một chiếc túi canvas lớn, xách theo đi gặp Thẩm Triệt.",
    "Chúng tôi hẹn gặp nhau lúc mười một giờ đêm trước cổng tòa nhà văn phòng.",
    "Tòa nhà cao tầng im lìm dưới ánh đèn đường hiu hắt, toát ra vẻ âm u lạnh lẽo khó tả.",
    "Giám đốc công ty bất động sản là một người đàn ông mập mạp, mặt mũi bơ phờ vì mất ngủ.",
    "Ông ta run rẩy kể: “Đạo sư ơi, nửa tháng nay cứ sau mười hai giờ đêm là văn phòng của tôi lại tự động hoạt động.”",
    "“Máy in tự chạy ra giấy trắng liên tục, bàn phím tự gõ lạch cạch lạch cạch.”",
    "“Bảo vệ vào kiểm tra thì không thấy một bóng người nào.”",
    "“Mấy nhân viên tăng ca đêm đều sợ quá xin nghỉ việc hết rồi.”",
    "Thẩm Triệt vỗ vai ông ta: “Yên tâm, có tôi ở đây rồi.”",
    "Chúng tôi đi thang máy lên tầng năm, nơi xảy ra hiện tượng kỳ quái.",
    "Không gian văn phòng tối om, chỉ có ánh đèn khẩn cấp màu xanh lá cây le lói.",
    "Tôi ôm chặt chiếc túi canvas chứa Pikachu trước ngực.",
    "Đột nhiên, tiếng “tít tít” từ chiếc máy in ở góc văn phòng vang lên khô khốc.",
    "Chiếc máy in tự động khởi động, đèn quét sáng xanh chạy qua chạy lại.",
    "Từng tờ giấy trắng tinh bắt đầu chạy ra khỏi khay, rơi lả tả xuống sàn nhà.",
    "Ngay sau đó, tiếng gõ bàn phím nhanh liên hồi “cạch cạch cạch” vang lên từ một góc làm việc.",
    "Tôi sợ hãi nấp sau lưng Thẩm Triệt.",
    "Thẩm Triệt khẽ rút kiếm gỗ đào ra, lẩm nhẩm niệm chú.",
    "Pika-Quỷ trong túi canvas khẽ thì thầm bên tai tôi.",
    "“Cô chủ ơi... âm khí này không có sát ý.”",
    "“Hình như... đây là vong hồn của một nhân viên văn phòng cũ.”",
    "Thẩm Triệt bước tới gần góc làm việc phát ra tiếng gõ phím.",
    "Anh ta khẽ phất kiếm gỗ đào, thổi bay luồng sương mù âm u đang che phủ.",
    "Hiện ra dưới ánh đèn điện thoại là bóng hình một thanh niên trẻ tuổi, mặc áo sơ mi công sở sờn vai.",
    "Đôi mắt cậu ta thâm quầng như gấu trúc, hai tay vẫn đang điên cuồng gõ phím trên chiếc máy tính đã tắt nguồn.",
    "Cậu ta lẩm bẩm trong vô thức: “Kịp KPI rồi... ngày mai phải nộp báo cáo... không được trễ...”",
    "Tôi nhìn cảnh tượng đó mà trong lòng bỗng dâng lên một nỗi chua xót nghẹn ngào.",
    "Hóa ra đây là một vong hồn cuồng công việc, ngay cả khi chết vẫn không quên làm việc."
]

ch4_sentences = [
    "Đúng lúc Thẩm Triệt định bước lên để trò chuyện cùng vong hồn đáng thương kia.",
    "Phía sau lưng chúng tôi bỗng vang lên tiếng bước chân rầm rập.",
    "Cánh cửa văn phòng bị đẩy mạnh ra.",
    "Một người đàn ông trung niên mặc áo bào vàng, tay cầm chuông đồng bước vào.",
    "Đi sau ông ta là hai đệ tử trẻ tuổi xách rương gỗ đựng đầy đồ cúng bái.",
    "Vị giám đốc mập mạp cũng lật đật chạy theo sau, vẻ mặt vô cùng cung kính.",
    "Ông ta giới thiệu: “A, Đạo sư Thẩm, giới thiệu với cậu đây là Đại sư Nguyễn Bỉnh, pháp sư đệ nhất quận Gò Vấp này.”",
    "“Tôi sợ cậu còn trẻ chưa đủ kinh nghiệm nên đã mời thêm Đại sư Nguyễn Bỉnh qua giúp sức.”",
    "Nguyễn Bỉnh liếc nhìn Thẩm Triệt bằng nửa con mắt khinh bỉ.",
    "Ông ta vuốt chòm râu dê, cười lạnh: “Hừ, một thằng nhóc dán cường lực vỉa hè mà cũng đòi bắt ma diệt quỷ sao?”",
    "“Thời buổi này đúng là ai cũng tự xưng đạo sư được.”",
    "Thẩm Triệt không hề giận dữ, chỉ cười nhạt nhẽo.",
    "Anh ta khoanh tay tựa vào bàn làm việc: “Đại sư Nguyễn Bỉnh danh tiếng lẫy lừng, vậy xin mời đại sư ra tay trước để vãn bối được mở mang tầm mắt.”",
    "Nguyễn Bỉnh hất hàm tự đắc.",
    "Ông ta bước ra giữa văn phòng, ra hiệu cho hai đệ tử bày bàn cúng tế.",
    "Hắn thắp ba nén hương lớn, tay lắc chuông đồng kêu leng keng liên hồi.",
    "Hắn cầm một thanh kiếm gỗ đào sơn son thếp vàng bóng loáng, miệng lẩm nhẩm đọc chú ngữ vô nghĩa.",
    "Đột nhiên, hắn vung kiếm chém vào không trung, miệng phun ra một ngụm cồn vào ngọn nến.",
    "Một luồng lửa lớn bùng phát rực rỡ giữa văn phòng.",
    "Vị giám đốc mập mạp sợ hãi vỗ tay trầm trồ: “Tuyệt quá! Đúng là thần thông quảng đại!”",
    "Thẩm Triệt khẽ ghé tai tôi thì thầm: “Trò bịp bợm phun cồn rẻ tiền, thế mà cũng lừa được người khác.”",
    "Tôi tò mò: “Sao thế anh?”",
    "Thẩm Triệt cười: “Hắn dùng bột lycopodium trộn cồn để tạo lửa lớn không gây bỏng.”",
    "“Kiến thức hóa học cấp ba thôi mà cũng dám xưng là thần thông.”",
    "Đúng lúc đó, vong hồn thanh niên cuồng KPI bị tiếng chuông leng keng ồn ào làm cho thức tỉnh.",
    "Đôi mắt đen kịt của vong hồn đột ngột trừng lớn.",
    "Cậu ta nhìn thấy bàn cúng tế và đống bùa chú dán xung quanh liền nổi giận lôi đình.",
    "Cậu ta thét lên một tiếng chói tai: “Ai... ai cản tôi làm việc!”",
    "“Tôi chưa hoàn thành KPI! Báo cáo tài chính chưa xong!”",
    "Oán khí bùng nổ dữ dội.",
    "Gió lạnh từ đâu thổi tới làm vỡ tung các cửa kính văn phòng.",
    "Giấy tờ bay tứ tung khắp nơi như một trận tuyết trắng.",
    "Nguyễn Bỉnh hoảng hốt, lập tức cầm một lá bùa màu vàng lao lên định dán vào trán vong hồn.",
    "Nhưng lá bùa chưa kịp chạm vào vong hồn đã bị âm khí xé rách thành trăm mảnh nhỏ.",
    "Vong hồn cuồng KPI vung tay một cái.",
    "Một luồng oán khí mạnh mẽ đánh thẳng vào ngực Nguyễn Bỉnh.",
    "Nguyễn Bỉnh hét lên một tiếng, văng lùi lại đập mạnh vào bàn làm việc.",
    "Lá gan của gã pháp sư lừa đảo này cực kỳ nhỏ bé.",
    "Thấy vong hồn hung dữ thật sự, hắn sợ đến mức mặt cắt không còn một giọt máu.",
    "Đột nhiên, một mùi khai khằn khè bốc lên giữa văn phòng.",
    "Chiếc quần bào vàng của Nguyễn Bỉnh ướt sũng một mảng lớn.",
    "Hắn sợ đến mức tè dầm ngay tại chỗ.",
    "Hắn gào khóc thảm thiết: “Ma thật! Ma thật rồi! Cứu mạng!”",
    "Nói đoạn, Nguyễn Bỉnh vứt cả kiếm vàng lẫn chuông đồng, co giò chạy biến ra hướng cầu thang bộ.",
    "Hai tên đệ tử cũng hoảng hồn vứt rương gỗ chạy theo sau sư phụ.",
    "Vị giám đốc mập mạp sợ đến mức nhũn chân ngã phịch xuống đất, vừa bò vừa khóc lóc cầu cứu.",
    "Trong văn phòng lúc này chỉ còn lại tôi, Thẩm Triệt và vong hồn đang cuồng loạn."
]

ch5_sentences = [
    "Vong hồn cuồng KPI sau khi đuổi cổ kẻ lừa đảo liền quay sang nhìn chúng tôi.",
    "Đôi mắt đen ngòm của cậu ta ngập tràn oán hận và đau khổ.",
    "Cậu ta thét lên: “Tại sao ai cũng cản tôi? Tôi phải làm việc!”",
    "Oán khí xung quanh cậu ta ngưng tụ thành những sợi tơ đen kịt, quăng quật bàn ghế văn phòng bay vèo vèo.",
    "Thẩm Triệt lập tức kéo tôi ra sau lưng.",
    "Nhìn đống bàn ghế bay vùn vụt, tôi sợ hãi ôm chặt chiếc túi canvas chứa Pikachu trước ngực.",
    "Thẩm Triệt nắm chặt thanh kiếm gỗ đào cổ kính, thần sắc vô cùng nghiêm nghị.",
    "“Khanh Khanh, đứng yên đó đừng cử động!”",
    "Nói đoạn, Thẩm Triệt lao lên phía trước.",
    "Thanh kiếm gỗ đào trên tay anh ta bùng phát hào quang đỏ rực, chém đứt những sợi tơ oán khí.",
    "Thẩm Triệt đâm thẳng mũi kiếm vào ngực vong hồn.",
    "Nhưng vong hồn này tích lũy oán khí làm việc quá sức trong nhiều năm, sức mạnh vô cùng khủng khiếp.",
    "Cậu ta gầm lên một tiếng, hai tay chụp chặt lấy kiếm gỗ đào.",
    "Một tiếng “rắc” giòn giã vang lên giữa văn phòng trống trải.",
    "Thanh kiếm gỗ đào gia truyền của Thẩm Triệt bị gãy làm đôi.",
    "Thẩm Triệt bị chấn động lùi lại mấy bước, khóe miệng rỉ ra một vệt máu đỏ tươi.",
    "Tôi hoảng hốt kêu lên: “Anh Thẩm!”",
    "Vong hồn cuồng KPI không dừng lại, tiếp tục lao về phía chúng tôi với tốc độ cực nhanh.",
    "Trong tình thế ngàn cân treo sợi tóc.",
    "Tôi theo bản năng ném mạnh chiếc túi canvas chứa con gấu bông Pikachu về phía vong hồn.",
    "Tôi hét lớn: “Pika-Quỷ, cứu mạng!”",
    "Con gấu bông Pikachu khổng lồ bay vút qua không trung.",
    "Đúng lúc đó, Pika-Quỷ trong bụng gấu bông cũng bị tình huống khẩn cấp làm cho giật mình.",
    "Hắn lập tức bộc phát âm lực của một Quỷ Vương trăm năm.",
    "Con Pikachu nhồi bông bỗng nhiên phát ra luồng ánh sáng vàng rực rỡ như một quả bom sáng.",
    "Đặc biệt hơn, do con gấu bông Pikachu này nằm cạnh giường tôi suốt một tuần qua.",
    "Nó đã hấp thụ toàn bộ dương khí may mắn và Phật quang ấm áp từ cơ thể tôi.",
    "Pika-Quỷ bám chặt lấy mặt vong hồn cuồng KPI.",
    "Hắn hoảng hốt hắt hơi một cái thật mạnh: “Hắt xì!”",
    "Cú hắt hơi chứa đựng âm lực Quỷ Vương kết hợp với Phật quang may mắn tích tụ trên gấu bông tạo ra một vụ nổ ánh sáng vàng cực kỳ chói lòa.",
    "Luồng ánh sáng ấm áp phả vào mặt vong hồn.",
    "Oán khí đen kịt bao quanh vong hồn lập tức như gặp nước ấm, tan biến sạch sành sanh.",
    "Gương mặt hung dữ của vong hồn cuồng KPI dần dần dịu xuống.",
    "Đôi mắt thâm quầng của cậu ta trở lại màu sắc bình thường.",
    "Cậu ta nhìn con gấu bông Pikachu đang bám trên mặt mình, rồi nhìn xuống hai bàn tay mình.",
    "Cậu ta lẩm bẩm: “Tôi... tôi chết rồi sao?”",
    "“Hóa ra... tôi đã chết rồi...”",
    "Tôi nhẹ nhàng bước lên một bước, giọng ấm áp: “Cậu đã làm việc rất chăm chỉ rồi.”",
    "“Giờ là lúc nghỉ ngơi rồi, không cần làm KPI nữa đâu.”",
    "Giọt nước mắt trong suốt từ khóe mắt vong hồn rơi xuống, tan vào hư không.",
    "Cậu ta mỉm cười thanh thản.",
    "“Cảm ơn cô... cuối cùng tôi cũng được nghỉ phép rồi...”",
    "Bóng hình vong hồn dần dần hóa thành những đốm sáng trắng lấp lánh, bay vút lên bầu trời đêm qua ô cửa kính vỡ.",
    "Căn phòng trở lại yên tĩnh.",
    "Con gấu bông Pikachu rơi phịch xuống sàn nhà, phát ra tiếng thở phào nhẹ nhõm của Pika-Quỷ."
]

ch6_sentences = [
    "Vị giám đốc mập mạp chứng kiến toàn bộ cảnh tượng từ đầu đến cuối liền run rẩy đứng dậy.",
    "Ông ta quỳ sụp xuống trước mặt Thẩm Triệt và tôi, dập đầu lia lịa.",
    "“Đạo sư cứu mạng! Thần tiên hiển linh!”",
    "“Tôi xin dâng thù lao ba mươi triệu như đã hứa, cộng thêm bảy mươi triệu tiền thưởng bồi thường cái kiếm gỗ đào của đạo sư!”",
    "Nói đoạn, ông ta run rẩy ký một tấm séc một trăm triệu đồng đưa bằng hai tay.",
    "Thẩm Triệt nhận lấy tấm séc, gương mặt lười biếng lúc này mới hiện lên một nụ cười hài lòng.",
    "Anh ta khẽ lau vệt máu trên khóe môi: “Cảm ơn giám đốc.”",
    "“Văn phòng của ông từ nay sẽ bình yên vô sự.”",
    "Ngày hôm sau, tên lừa đảo Nguyễn Bỉnh bị cảnh sát quận Gò Vấp mời về đồn làm việc.",
    "Nhờ đoạn clip bóc phốt hắn tè dầm chạy trốn được bảo vệ tòa nhà chia sẻ lên mạng.",
    "Nhiều nạn nhân bị hắn lừa đảo cúng bái trước đây đã đồng loạt làm đơn tố cáo gã.",
    "Nguyễn Bỉnh nhục nhã ê chề, phải đối mặt với án phạt tù vì tội lừa đảo chiếm đoạt tài sản.",
    "Còn Thẩm Triệt và tôi chia đôi số tiền một trăm triệu thù lao.",
    "Tôi dùng một phần tiền mua tặng Pika-Quỷ một chiếc tivi màn hình phẳng năm mươi lăm inch cực xịn.",
    "Tôi còn mua thêm ba bao bông gòn loại cao cấp nhất để nhét vào bụng gấu bông Pikachu cho hắn có một ngôi nhà thật êm ái.",
    "Pika-Quỷ sướng đến mức bay lượn tung tăng khắp nhà dưới dạng đốm sáng vàng.",
    "Chiều tối hôm đó, Thẩm Triệt tiễn tôi về chung cư.",
    "Gió chiều Gò Vấp lộng gió, thổi tung làn tóc rối của tôi.",
    "Đứng ở hành lang lộng gió, Thẩm Triệt bảo tôi đưa điện thoại cho anh ta.",
    "Tôi ngạc nhiên: “Sao thế anh?”",
    "Anh ta tỉ mẩn lột miếng dán cường lực cũ bị xước nhẹ của tôi ra.",
    "Rồi anh ta lấy từ trong hộp nhựa ra một miếng dán cường lực phiên bản giới hạn cực kỳ cao cấp.",
    "Anh ta cẩn thận dán lên màn hình điện thoại của tôi, vuốt từng bọt khí nhỏ một cách vô cùng nhẹ nhàng.",
    "Ánh mắt anh ta nhìn tôi lúc này không còn lười biếng nữa, mà tràn đầy sự dịu dàng ấm áp.",
    "Thẩm Triệt khẽ nói: “Cường lực của em, sau này cả đời cứ để anh bảo hành miễn phí.”",
    "Tôi đỏ mặt, cúi đầu mỉm cười e thẹn: “Dạ... cảm ơn anh.”",
    "Từ trong phòng ngủ, con gấu bông Pikachu đầu giường khẽ phát ra tiếng cười “khì khì” trêu chọc của Pika-Quỷ.",
    "Tôi biết, cuộc sống sau này của tôi sẽ không bao giờ còn tẻ nhạt bên chiếc máy in nữa."
]

def format_paragraphs(sentences):
    return "".join([f"<p>{s}</p>" for s in sentences])

def main():
    print("=" * 60)
    print("🚀 PUBLISHING STORY 1933 (V12 PIKACHU GHOST COMEDY)")
    print("=" * 60)
    
    # 1. Update Story Metadata
    title = "Đừng Gọi Tôi Là Con Bé Gần Máy In: Tôi Nuôi Quỷ Vương Trong Gấu Bông Pikachu"
    intro = format_paragraphs([
        "Tôi là Tô Khanh Khanh, một nữ nhân viên văn phòng bình thường có vận may bùng nổ.",
        "Nhưng cuộc sống của tôi thay đổi hoàn toàn kể từ khi một Quỷ Vương tu vi trăm năm sợ nóng chui vào trú ngụ trong con gấu bông Pikachu của tôi.",
        "Cùng với Thẩm Triệt - chàng đạo sĩ Huyền Môn kiêm nghề dán cường lực dạo vỉa hè, chúng tôi mở ra một hành trình trừ tà hài hước bậc nhất Sài Gòn."
    ])
    
    print("Uploading novel_editor.php helper to server...")
    novel_editor.upload_helper()
    
    print(f"Updating Story 1933 metadata...")
    meta_res = novel_editor.update_story_meta(STORY_ID, title=title, intro=intro)
    print("Metadata update result:", meta_res)
    
    # 2. Update Chapters
    chapters_data = [
        {"id": 1934, "title": "Chương 1: Chiếc Máy In Kẹt Giấy Và Vận May Bùng Nổ", "sentences": ch1_sentences},
        {"id": 1935, "title": "Chương 2: Quỷ Vương Sợ Nóng Trong Bụng Pikachu", "sentences": ch2_sentences},
        {"id": 1936, "title": "Chương 3: Trợ Lý Âm Ty Kiêm Shipper Dạo", "sentences": ch3_sentences},
        {"id": 1937, "title": "Chương 4: Vả Mặt Đại Sư Rác Rưởi", "sentences": ch4_sentences},
        {"id": 1938, "title": "Chương 5: Sức Mạnh Của Gấu Bông Màu Vàng", "sentences": ch5_sentences},
        {"id": 1939, "title": "Chương 6: Hào Quang Chiến Thắng Và Lời Hứa Cường Lực Trọn Đời", "sentences": ch6_sentences}
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
    # The prompt should be textless, logoless, depicting a cute large Pikachu plushie in a warm anime bedroom with vivid lighting
    cover_prompt = "masterpiece, high quality anime illustration, warm cozy bedroom in Gò Vấp Saigon, a giant cute yellow chubby Pikachu plushie sitting on the bed, soft sunlight filtering through the window, vivid cinematic lighting, textless, no logos, no frames"
    print("\nGenerating and setting cover image...")
    cover_success = upload_cover_local.set_cover_via_local_upload(STORY_ID, cover_prompt)
    print("Cover upload success:", cover_success)
    
    print("\n🎉 Story 1933 successfully published with strict V12 formatting!")

if __name__ == "__main__":
    main()
