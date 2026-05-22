import json
import os

temp_file_path = "/Users/aaronnguyen/TN/App/doctieuthuyet/pending_novel_9_temp.json"
with open(temp_file_path, "r", encoding="utf-8") as f:
    novel_data = json.load(f)

# Chapter 7
ch7_sentences = [
    "Cơn gió lạnh buốt của mùa đông Ba Lan thổi qua những hàng cây rụng lá dọc theo đại lộ Krakowskie Przedmieście.",
    "Warsaw chào đón Lâm Hoàng Phúc và Trần Diệu Linh bằng những bông tuyết đầu mùa trắng xóa phủ lên những mái ngói cổ kính.",
    "Phúc kéo cao cổ chiếc áo khoác dạ ấm áp mà Linh mua cho cậu, ngước nhìn tòa nhà Philharmonic Hall cổ kính và tráng lệ.",
    "Nơi đây chính là thánh đường của âm nhạc cổ điển thế giới, nơi đã từng chứng kiến sự ra đời của những huyền thoại piano lẫy lừng.",
    "Hôm nay là ngày khai mạc Vòng 1 của cuộc thi Chopin Competition danh giá nhất hành tinh.",
    "Bên trong sảnh lớn, không khí vô cùng căng thẳng và trang nghiêm.",
    "Hơn tám mươi thí sinh xuất sắc nhất đến từ các cường quốc âm nhạc như Nga, Mỹ, Nhật Bản, Ba Lan đang tập trung luyện ngón ở các phòng chờ.",
    "Ai nấy đều toát lên khí chất tự tin, ngạo nghễ của những thiên tài được đào tạo bài bản từ những học viện danh tiếng nhất thế giới.",
    "Lâm Hoàng Phúc - thí sinh tự do duy nhất đến từ Việt Nam - đứng lặng lẽ ở một góc, khẽ xoa hai bàn tay cho bớt lạnh.",
    "\"Đừng lo lắng Phúc, hãy chơi bằng cả trái tim cậu, hãy cho họ nghe tiếng đàn của một linh hồn tự do.\" Linh đứng bên cạnh khẽ nói, ánh mắt chứa đựng niềm tin tuyệt đối.",
    "Đúng lúc đó, tiếng loa phát thanh vang lên bằng tiếng Anh, gọi tên Lâm Hoàng Phúc lên sân khấu.",
    "Phúc hít một hơi thật sâu, bước ra khỏi hậu trường tối tăm, tiến vào ánh đèn sân khấu rực rỡ của khán phòng lớn.",
    "Khán phòng Philharmonic Hall với sức chứa hơn một ngàn chỗ ngồi đã kín chỗ, hàng chục camera truyền hình trực tiếp đang chĩa về phía cậu.",
    "Hàng ghế giám khảo ngồi trang trọng ở chính giữa, đều là những huyền thoại piano thế giới với gương mặt vô cùng nghiêm nghị.",
    "Phúc đi tới bên cây đại dương cầm Steinway D-274 sang trọng, cúi đầu chào khán giả và hội đồng giám khảo.",
    "Cậu ngồi xuống ghế đàn, khẽ nhắm mắt lại.",
    "Trong khoảnh khắc đó, mọi sự ồn ào xung quanh hoàn toàn biến mất, chỉ còn lại cậu và cây đàn piano.",
    "Phúc đặt đôi bàn tay thanh tú lên phím đàn, và bắt đầu chơi bản Ballade số 1 giọng Sol thứ của Chopin.",
    "Ngay từ hợp âm đầu tiên vang lên trầm hùng, cả khán phòng lập tức chấn động.",
    "Đó là một âm thanh vô cùng uy lực nhưng lại chứa đựng một nỗi u sầu sâu thẳm, như tiếng kêu gào của một linh hồn bị giam cầm.",
    "Tiếng đàn của Phúc dẫn dắt người nghe đi qua những thăng trầm của cảm xúc, từ những đoạn tự sự da diết cho đến những giai điệu cuộn trào bão táp.",
    "Kỹ thuật octaves của cậu nhanh và chính xác như máy bắn đá, nhưng lại vô cùng mềm mại nhờ sự chuyển động linh hoạt của cổ tay.",
    "Cách cậu xử lý các câu nhạc rubato tự nhiên đến mức khiến Giáo sư Janusz Olejniczak ngồi dưới hàng ghế giám khảo phải nghiêng đầu kinh ngạc.",
    "Giáo sư nhận ra, đây không phải là một màn trình diễn kỹ thuật vô hồn như đa số các thí sinh khác.",
    "Đây là âm nhạc thực sự, là tiếng lòng của một thiên tài đã trải qua bao nhiêu giông bão cuộc đời để vươn lên.",
    "Từng nốt nhạc ngân vang như những giọt nước mắt lấp lánh dưới ánh đèn sân khấu, chạm vào sâu thẳm tâm hồn của mọi người có mặt trong khán phòng.",
    "Đoạn coda cao trào nhất được Phúc kết thúc bằng một chuỗi âm chạy cực nhanh và mạnh mẽ, đập mạnh xuống phím đàn tạo nên một hợp âm vang dội như sấm sét.",
    "Nốt nhạc cuối cùng ngân dài rồi tan dần vào không gian tĩnh lặng.",
    "Cả khán phòng im lặng trong vòng ba giây, như thể họ vẫn chưa kịp tỉnh dậy khỏi giấc mơ âm nhạc tuyệt mỹ mà Phúc vừa tạo ra.",
    "Và rồi, một tràng pháo tay bùng nổ như sấm dậy vang lên khắp Philharmonic Hall.",
    "Nhiều vị giám khảo quốc tế khó tính nhất cũng đứng dậy vỗ tay tán thưởng, gương mặt lộ rõ vẻ xúc động sâu sắc.",
    "Trần Diệu Linh đứng ở hậu trường nhìn ra, đôi mắt phượng rơm rớm nước mắt vì tự hào.",
    "Cô biết, Lâm Hoàng Phúc đã thực sự làm được.",
    "Cậu đã chấn động cả thủ đô Warsaw bằng tài năng thiên bẩm của mình.",
    "Kết quả được công bố ngay tối hôm đó: Lâm Hoàng Phúc lọt vào vòng tiếp theo với số điểm tuyệt đối từ toàn bộ hội đồng giám khảo.",
    "Tên của cậu lập tức trang trọng xuất hiện trên các trang báo âm nhạc uy tín toàn cầu như Gramophone và BBC Music Magazine.",
    "Một ngôi sao mới của nền piano thế giới đã chính thức bước ra ánh sáng ngay giữa lòng châu Âu cổ kính."
]

# Chapter 8
ch8_sentences = [
    "Trong khi Lâm Hoàng Phúc đang tỏa sáng rực rỡ tại Warsaw, thì tại Việt Nam, một trận cuồng phong pháp lý đã chính thức quét sạch cha con hiệu trưởng.",
    "Sáng thứ Hai, Thanh tra Bộ Văn hóa, Thể thao và Du lịch phối hợp cùng Cơ quan Cảnh sát điều tra (C03) Bộ Công an tổ chức họp báo công bố kết luận thanh tra toàn diện Nhạc viện TP.HCM.",
    "Trước hàng trăm ống kính phóng viên, vị đại diện Bộ Văn hóa dõng dạc đọc quyết định kỷ luật.",
    "\"Cách chức vĩnh viễn chức vụ Hiệu trưởng đối với ông Nguyễn Thế Phong do có các sai phạm nghiêm trọng trong công tác quản lý đào tạo và đạo đức nghề nghiệp.\"",
    "\"Thu hồi toàn bộ các danh hiệu học hàm Giáo sư, Phó Giáo sư đã phong tặng cho ông Nguyễn Thế Phong do vi phạm pháp luật và học thuật.\"",
    "\"Hủy bỏ hiệu lực chứng nhận đăng ký bản quyền đối với bản Sonatina Đô thứ của Nguyễn Thế Anh do có hành vi gian lận, cướp đoạt chất xám của sinh viên Lâm Hoàng Phúc.\"",
    "Quyết định này lập tức được phát sóng trực tiếp trên đài truyền hình quốc gia VTV và đưa tin trang trọng trên toàn bộ các trang báo lớn.",
    "Cùng lúc đó, Cơ quan điều tra C03 chính thức tống đạt quyết định khởi tố bị can và thực hiện lệnh bắt tạm giam đối với Nguyễn Thế Phong về hành vi lợi dụng chức vụ quyền hạn trong khi thi hành công vụ và tham ô tài sản công quỹ Nhạc viện.",
    "Hai chiếc xe biển xanh đỗ trước căn biệt thự sang trọng của Thế Phong ở Quận 7.",
    "Thế Phong bị dẫn ra ngoài với chiếc còng số tám lạnh buốt trên tay, gương mặt xám xịt, đầu cúi gầm xuống đất để tránh các ống kính phóng viên đang vây quanh.",
    "Còn Nguyễn Thế Anh thì bị Nhạc viện chính thức đuổi học, xóa bỏ toàn bộ kết quả học tập suốt bốn năm qua.",
    "Cậu ta đứng trước cổng Nhạc viện, nhìn tấm biển hiệu từng là nơi cha mình làm vua một cõi, giờ đây chỉ còn nhận lại những ánh mắt khinh bỉ và xa lánh của bạn bè.",
    "Các nhãn hàng tài trợ đồng loạt khởi kiện Thế Anh đòi bồi thường hàng chục tỷ đồng vì làm ảnh hưởng nghiêm trọng đến hình ảnh thương hiệu.",
    "Cha con họ đã hoàn toàn mất trắng tất cả: địa vị, tiền tài, danh vọng và cả tương lai.",
    "Sự sụp đổ của họ là cái giá phải trả vô cùng thích đáng cho sự tráo trở, kiêu ngạo và coi thường pháp luật.",
    "Trong khi đó, tin tức Lâm Hoàng Phúc lọt vào vòng tiếp theo của Chopin Competition với điểm số tuyệt đối được truyền về nước.",
    "Toàn bộ truyền thông chính thống và mạng xã hội Việt Nam bùng nổ trong niềm tự hào và hân hoan tột độ.",
    "Những kẻ trước đó tham gia chiến dịch bôi nhọ Phúc giờ đây đồng loạt xóa bài và viết lời xin lỗi, ca ngợi cậu như một người hùng dân tộc.",
    "Nhà báo Hoàng Nam của báo Tuổi Trẻ đã viết một bài xã luận đầy xúc động: 'Lâm Hoàng Phúc không chỉ đòi lại công lý cho bản thân, mà còn chứng minh cho thế giới thấy tài năng của người Việt Nam không bao giờ bị bóp nghẹt bởi những thế lực đen tối'.",
    "Hình ảnh Phúc biểu diễn tại Warsaw Philharmonic Hall tràn ngập trên các trang bìa báo lớn.",
    "Người dân Việt Nam hào hứng theo dõi từng đêm thi của Phúc qua các buổi phát sóng trực tiếp, tự hào khi thấy quốc kỳ Việt Nam tung bay cạnh quốc kỳ các cường quốc âm nhạc thế giới.",
    "Trần Diệu Linh đọc các bài báo từ quê nhà gửi sang, khẽ mỉm cười đầy mãn nguyện.",
    "Cô nhìn Phúc đang tập trung luyện đàn bên cây Steinway trong căn phòng ấm áp của khách sạn, ánh mắt tràn đầy niềm kiêu hãnh.",
    "\"Phúc, quê nhà đã dọn sạch rác rưởi rồi, giờ đây toàn bộ đất nước đang đứng sau lưng cậu.\"",
    "Phúc dừng tay đàn, quay lại nhìn Linh với nụ cười nhẹ nhàng ấm áp.",
    "\"Con cảm ơn cô Diệu Linh. Con sẽ chơi trận chung kết này bằng tất cả tình yêu dành cho âm nhạc và đất nước của chúng ta.\""
]

# Chapter 9
ch9_sentences = [
    "Đêm chung kết của cuộc thi piano danh giá nhất hành tinh - Chopin Competition lần thứ 19 chính thức diễn ra.",
    "Khán phòng của Warsaw Philharmonic Hall không còn một chỗ trống, tụ hội giới mộ điệu, các nhà phê bình âm nhạc hàng đầu và đại diện các hãng đĩa lớn từ khắp thế giới.",
    "Hơn mười triệu khán giả toàn cầu đang theo dõi trực tiếp qua kênh truyền hình trực tiếp và các nền tảng số hóa.",
    "Lâm Hoàng Phúc bước ra sân khấu trong bộ vest đen sang trọng, gương mặt điềm tĩnh nhưng toát lên thần thái của một bậc thầy thực thụ.",
    "Đáp lại cậu là những tràng pháo tay vang dội kéo dài không dứt từ hàng ngàn khán giả có mặt.",
    "Phúc đi tới bên cây đàn Steinway, cúi đầu chào nhạc trưởng và dàn nhạc giao hưởng quốc gia Warsaw đang ngồi sẵn trên sân khấu.",
    "Cậu ngồi xuống chiếc ghế da, khẽ đặt đôi tay lên phím đàn, hít một hơi sâu để cảm nhận sự tĩnh lặng tuyệt đối.",
    "Nhạc trưởng khẽ vung đũa chỉ huy, và dàn nhạc bắt đầu tấu lên giai điệu mở đầu của bản Concerto số 1 giọng Mi thứ của Chopin.",
    "Giai điệu hoành tráng và da diết của dàn nhạc vang lên như khúc dạo đầu cho một câu chuyện huyền thoại.",
    "Và rồi, tiếng đàn piano của Phúc cất lên.",
    "Đó là một âm thanh vô cùng trong trẻo, ngọt ngào nhưng lại chứa đựng một nội lực thâm sâu kỳ diệu.",
    "Tiếng đàn của Phúc như dắt người nghe đi qua những thăng trầm giông bão của cuộc đời cậu.",
    "Từ những đêm đông lạnh giá nhịn đói trong căn phòng trọ chật hẹp ở quận 4, cho đến những giọt mồ hôi rơi trên phím đàn cũ ở cư xá Thanh Đa.",
    "Mọi uất ức, đau khổ, và niềm hy vọng cháy bỏng đều được Phúc hóa thân vào từng nốt nhạc tuyệt mỹ của Chopin.",
    "Tiếng đàn của cậu hòa quyện hoàn hảo với dàn nhạc giao hưởng, lúc nâng đỡ, lúc đối thoại tạo nên một bức tranh âm nhạc vô cùng tráng lệ.",
    "Kỹ thuật legato của cậu mượt mà như một dải lụa mềm bay lượn giữa không trung, từng nốt nhạc vang lên tròn trịa, lấp lánh như những viên ngọc trai.",
    "Ở chương hai da diết, tiếng đàn của Phúc nhẹ nhàng và sâu lắng đến mức khiến nhiều khán giả ngồi dưới khán phòng phải rơm rớm nước mắt.",
    "Họ cảm nhận được một tình yêu âm nhạc thuần khiết, một tâm hồn thánh thiện chưa hề bị vẩn đục bởi những danh lợi tầm thường.",
    "Giáo sư Janusz Olejniczak ngồi trên hàng ghế giám khảo khẽ nhắm mắt, giọt nước mắt xúc động lăn dài trên gương mặt lão luyện của ông.",
    "Ông tự thì thầm: 'Đây chính là Chopin tái thế, âm nhạc của cậu ấy có linh hồn thực sự'.",
    "Đến chương ba cao trào dồn dập, Phúc hoàn toàn thăng hoa, mười đầu ngón tay cậu lướt trên phím đàn nhanh đến mức mắt thường không thể theo kịp.",
    "Cậu chơi với một sự tự tin ngạo nghệ, đập tan mọi xiềng xích của quyền lực bẩn thỉu đã từng muốn chôn vùi cậu.",
    "Hợp âm cuối cùng vang lên trầm hùng phối hợp cùng dàn nhạc giao hưởng kết thúc tác phẩm một cách vô cùng trọn vẹn và hoành tráng.",
    "Phúc đứng bật dậy, hai tay buông thõng, ngực phập phồng thở dốc dưới ánh đèn sân khấu rực rỡ.",
    "Cả khán phòng lặng đi trong một giây.",
    "Và rồi, toàn bộ khán phòng Philharmonic Hall đồng loạt đứng dậy, tiếng vỗ tay vang dội như sấm sét cắt ngang bầu trời đêm Warsaw.",
    "Những tràng pháo tay đứng (standing ovation) kéo dài liên tục mười phút không dứt, khán giả liên tục gọi vang tên 'Lam Hoang Phuc'.",
    "Phúc cúi đầu chào ban giám khảo, chào khán giả trong niềm xúc động tột cùng.",
    "Cậu nhìn về phía hậu trường, nơi Trần Diệu Linh đang đứng vỗ tay với nụ cười rạng rỡ và những giọt nước mắt hạnh phúc lăn dài trên má.",
    "Cậu biết, đêm nay, cậu đã thực sự chạm tới đỉnh cao vinh quang bằng chính đôi bàn tay và linh hồn tự do của mình."
]

# Chapter 10
ch1_sentences_expanded = [
    "Sáng ngày tiếp theo, buổi lễ trao giải chính thức của Chopin Competition lần thứ 19 được tổ chức trang trọng tại Nhà hát lớn Warsaw.",
    "Hàng trăm nhà báo quốc tế vây kín bục danh dự, chờ đợi khoảnh khắc lịch sử công bố kết quả.",
    "Ngài Chủ tịch Hội đồng giám khảo bước lên bục micro, giọng nói dõng dạc vang lên bằng tiếng Anh.",
    "\"The Gold Medal of the 19th International Chopin Piano Competition is awarded to... Lam Hoang Phuc from Vietnam!\"",
    "Cả khán phòng bùng nổ trong tiếng vỗ tay và tiếng reo hò chúc mừng nồng nhiệt.",
    "Quốc kỳ Việt Nam đỏ rực với ngôi sao vàng năm cánh được kéo lên ở vị trí cao nhất trên lễ đài sân khấu quốc tế.",
    "Lâm Hoàng Phúc bước lên bục vinh quang cao nhất, ngài Chủ tịch đích thân đeo chiếc Huy chương Vàng danh giá lên cổ cậu.",
    "Ngoài giải Nhất, Phúc còn đoạt thêm hai giải phụ quan trọng: Giải biểu diễn bản Ballade xuất sắc nhất và Giải biểu diễn Concerto xuất sắc nhất.",
    "Đây là chiến thắng vang dội nhất, vô tiền khoáng hậu trong lịch sử âm nhạc cổ điển Việt Nam và Đông Nam Á từ trước đến nay.",
    "Phúc đứng trên bục vinh quang, tay nâng cao chiếc cúp pha lê lấp lánh, ánh mắt rực sáng niềm kiêu hãnh tự hào.",
    "Cậu nhìn thấy Trần Diệu Linh ngồi dưới hàng ghế VIP đang nở nụ cười rạng rỡ, đôi mắt phượng sáng ngời tự hào.",
    "Tại quê nhà Việt Nam, tin tức Phúc giành giải Nhất Chopin Competition lập tức phủ sóng toàn bộ các phương tiện truyền thông.",
    "Bộ trưởng Bộ Văn hóa gửi điện hoa chúc mừng khẩn cấp, ca ngợi Phúc là niềm tự hào vĩ đại của dân tộc.",
    "Cùng lúc đó, Tòa án Nhân dân TP.HCM chính thức đưa vụ án tranh chấp bản quyền ra xét xử sơ thẩm.",
    "Với đầy đủ các bằng chứng thép không thể chối cãi, Tòa phán quyết: Hủy bỏ toàn bộ quyền tác giả của Nguyễn Thế Anh, trả lại quyền sở hữu trí tuệ độc quyền bản Sonatina Đô thứ cho Lâm Hoàng Phúc.",
    "Nguyễn Thế Phong nhận bản án năm năm tù giam về tội lợi dụng chức vụ quyền hạn và tham ô tài sản công quỹ.",
    "Nguyễn Thế Anh phải bồi thường thiệt hại hàng chục tỷ đồng cho các nhãn hàng và chính thức bị xã hội tẩy chay vĩnh viễn.",
    "Sự trừng phạt nghiêm khắc của pháp luật đã đem lại công lý trọn vẹn cho thần đồng piano Lâm Hoàng Phúc.",
    "Vài ngày sau lễ trao giải, tuyết vẫn rơi nhẹ trên những con phố cổ kính của thủ đô Warsaw, Ba Lan.",
    "Lâm Hoàng Phúc cùng Trần Diệu Linh đứng bên bờ sông Vistula lộng gió, ngắm nhìn dòng sông lững lờ trôi dưới làn tuyết trắng xóa.",
    "Chiếc Huy chương Vàng danh giá nằm ấm áp trong balô của Phúc, nhưng tâm trí cậu giờ đây đã hướng về những chân trời mới.",
    "Cậu đã nhận được lời mời học bổng toàn phần đặc cách từ Học viện Juilliard danh giá của Mỹ và Học viện Âm nhạc Hoàng gia Anh.",
    "Đồng thời, hãng đĩa nổi tiếng Deutsche Grammophon đã ký hợp đồng độc quyền thu âm album đầu tay của Phúc với giá trị lên tới hàng triệu đô la.",
    "Linh quay sang nhìn Phúc, mái tóc đen dài của cô bay nhẹ trong gió tuyết, nụ cười kiêu sa thanh nhã rạng rỡ.",
    "\"Phúc, hành trình phục hận đã kết thúc xuất sắc, giờ đây là lúc cậu viết nên trang sử mới cho cuộc đời mình.\"",
    "Phúc quay lại nhìn người phụ nữ đã thay đổi hoàn toàn số phận cậu, ánh mắt đầy lòng biết ơn và sự gắn kết sâu sắc.",
    "Cậu khẽ nắm lấy bàn tay thanh mảnh của Linh, bàn tay đã từng che ô cho cậu dưới cơn mưa rào Sài Gòn ngày nào.",
    "\"Cô Diệu Linh, con đường phía trước còn rất dài, con hy vọng cô sẽ luôn đồng hành cùng con trên mọi nẻo đường âm nhạc thế giới.\"",
    "Linh khẽ mỉm cười, siết nhẹ bàn tay Phúc, ánh mắt hướng về phía chân trời xa xôi nơi ánh bình minh đang dần lên rực rỡ.",
    "\"Tất nhiên rồi, thiên tài của tôi.\"",
    "Giữa cái lạnh mùa đông châu Âu, hai tâm hồn nghệ sĩ lớn hòa làm một, cùng nhau bước tiếp trên con đường chinh phục những đỉnh cao huy hoàng mới của nghệ thuật thế giới."
]

def format_chapter(title, sentences):
    content = ""
    for s in sentences:
        content += f"<p>{s}</p>\\n"
    if content.endswith("\\n"):
        content = content[:-2]
    return {
        "title": title,
        "content": content
    }

novel_data["chapters"].append(format_chapter("Chương 7: Vòng Loại Warsaw", ch7_sentences))
novel_data["chapters"].append(format_chapter("Chương 8: Phơi Bày Sự Thật", ch8_sentences))
novel_data["chapters"].append(format_chapter("Chương 9: Đêm Chung Kết Lịch Sử", ch9_sentences))
novel_data["chapters"].append(format_chapter("Chương 10: Vinh Quang Trở Về", ch1_sentences_expanded))

# Write the final JSON file
final_file_path = "/Users/aaronnguyen/TN/App/doctieuthuyet/pending_novel_9.json"
with open(final_file_path, "w", encoding="utf-8") as f:
    json.dump(novel_data, f, ensure_ascii=False, indent=2)

print("Stage 3 completed successfully. Written final novel to pending_novel_9.json.")
