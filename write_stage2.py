import json

# Read current temp novel data
temp_file_path = "/Users/aaronnguyen/TN/App/doctieuthuyet/pending_novel_9_temp.json"
with open(temp_file_path, "r", encoding="utf-8") as f:
    novel_data = json.load(f)

# Chapter 4
ch4_sentences = [
    "Ánh đèn chùm pha lê rực rỡ tỏa ánh sáng lộng lẫy xuống đại sảnh Nhà hát Thành phố tại trung tâm Quận 1.",
    "Tối nay là đêm nhạc hội kỷ niệm thành lập Nhạc viện Thành phố Hồ Chí Minh, một sự kiện văn hóa tầm cỡ quy tụ giới thượng lưu và trí thức.",
    "Những chiếc xe sang trọng nối đuôi nhau dừng trước thảm đỏ, bước xuống là các vị khách mời mặc vest đen lịch lãm và đầm dạ hội quý phái.",
    "Hiệu trưởng Nguyễn Thế Phong trong bộ vest chỉnh tề đứng ở sảnh chính, gương mặt rạng rỡ đón tiếp các quan chức và đối tác.",
    "Bên cạnh ông ta, Nguyễn Thế Anh vuốt lại mái tóc bôi keo bóng lộn, vẻ mặt kiêu ngạo tự đắc như thể mình đã là một ngôi sao quốc tế.",
    "Cha con họ đã chuẩn bị cho đêm nay từ rất lâu, coi đây là bục phóng hoàn hảo để đưa Thế Anh lên đỉnh cao danh vọng trước khi đi Warsaw.",
    "Nhưng ở một góc khuất của hàng ghế VIP, Trần Diệu Linh đã ngồi sẵn từ lúc nào.",
    "Cô mặc một chiếc đầm đen dạ hội giản dị nhưng toát lên khí chất quý phái bẩm sinh, bên cạnh cô là Lâm Hoàng Phúc và Luật sư Trần Hữu Trí.",
    "Phúc ngồi lặng lẽ, đôi bàn tay đút trong túi quần siết chặt, ánh mắt nhìn chằm chằm vào chiếc đàn đại dương cầm Steinway trên sân khấu.",
    "Cậu nhớ lại chỉ một tuần trước, chính cậu đã bị xua đuổi khỏi Nhạc viện như một kẻ đạo nhạc đê tiện.",
    "Hôm nay, cậu trở lại đây không phải để xin xỏ, mà để chứng kiến sự sụp đổ của những kẻ đã cướp đoạt chất xám của mình.",
    "\"Bình tĩnh đi Phúc, kịch hay mới chỉ bắt đầu thôi.\" Linh khẽ thì thầm, nụ cười nửa miệng đầy vẻ mưu mô.",
    "Đúng tám giờ tối, chương trình chính thức bắt đầu.",
    "Sau lời phát biểu dài dòng và đầy tự hào của Hiệu trưởng Nguyễn Thế Phong, tiếng vỗ tay vang lên nồng nhiệt.",
    "\"Tiếp theo chương trình, xin trân trọng giới thiệu tài năng piano xuất sắc nhất Nhạc viện - Nguyễn Thế Anh với bản Sonatina Đô thứ do chính em sáng tác!\"",
    "Tiếng loa vang dội khắp nhà hát, và Thế Anh bước ra sân khấu dưới những tràng pháo tay rầm rộ.",
    "Cậu ta cúi đầu chào đầy lịch lãm, ngồi trước cây đàn Steinway quý giá, khẽ nhắm mắt lấy cảm xúc.",
    "Khi những nốt nhạc đầu tiên vang lên, Phúc cảm thấy tim mình như bị ai bóp nghẹt.",
    "Đúng là bản nhạc của cậu, từng nốt nhạc, từng câu nhạc mà cậu đã đổ biết bao xương máu để viết ra.",
    "Nhưng dưới sự biểu diễn của Thế Anh, tiếng đàn trở nên vô cùng sáo rỗng, thiếu đi cái hồn và sự tinh tế bẩm sinh.",
    "Kỹ thuật legato của cậu ta bị cứng, nhịp độ rubato không tự nhiên mà mang đầy vẻ gượng ép, phô trương.",
    "Tuy nhiên, đối với phần lớn khán giả không chuyên phía dưới, đây vẫn là một màn trình diễn vô cùng ấn tượng.",
    "Hiệu trưởng Nguyễn Thế Phong ngồi dưới hàng ghế đầu nhìn con trai biểu diễn với vẻ mặt vô cùng đắc ý.",
    "Ông ta ghé tai một vị quan chức ngồi cạnh, thì thầm đầy tự hào về thiên tài của con trai mình.",
    "Màn biểu diễn kết thúc, toàn bộ khán phòng đứng dậy vỗ tay nồng nhiệt, những đóa hoa tươi thắm được ném lên sân khấu.",
    "Thế Anh đứng giữa ánh đèn sân khấu rực rỡ, đón nhận sự vinh quang cướp đoạt được từ người khác.",
    "Một phóng viên đài truyền hình nhanh chóng bước lên sân khấu, đưa micro phỏng vấn Thế Anh.",
    "\"Chào Thế Anh, bản Sonatina này thực sự là một kiệt tác âm nhạc! Bạn có thể chia sẻ cảm xúc khi sáng tác tác phẩm này không?\"",
    "Thế Anh cầm micro, gương mặt ngẩng cao đầy tự phụ.",
    "\"Dạ, con xin cảm ơn mọi người. Bản nhạc này con viết trong những đêm mất ngủ, lấy cảm hứng từ tình yêu quê hương và sự dạy dỗ nghiêm khắc của cha con.\"",
    "\"Con đã đăng ký bản quyền độc quyền và hy vọng tác phẩm này sẽ giúp Việt Nam ghi dấu ấn tại Chopin Competition sắp tới.\"",
    "Nghe những lời trơ trẽn đó, Phúc không kìm được nữa, một nụ cười lạnh lùng hiện lên trên môi cậu.",
    "Ngay lúc đó, Luật sư Trần Hữu Trí bên cạnh khẽ đứng dậy, mở chiếc cặp da đen, rút ra một văn bản pháp lý dày cộp.",
    "\"Cô Diệu Linh, đơn kiện xâm phạm quyền tác giả và yêu cầu áp dụng biện pháp khẩn cấp tạm thời đã được nộp lên Tòa án Nhân dân TP.HCM chiều nay.\"",
    "\"Tòa án đã chính thức thụ lý vụ án số 47/2026/TLST-DS về tranh chấp quyền sở hữu trí tuệ.\"",
    "\"Đồng thời, Cục Bản quyền tác giả đã nhận đơn yêu cầu hủy bỏ hiệu lực chứng nhận bản quyền của Nguyễn Thế Anh.\"",
    "Linh gật đầu, đôi mắt phượng híp lại đầy nguy hiểm.",
    "\"Tốt lắm, hãy gửi một bản sao văn bản thụ lý của Tòa án cho toàn bộ các phóng viên có mặt ở đây tối nay.\"",
    "\"Và gửi trực tiếp một bản cho Nguyễn Thế Phong ngay trên bàn tiệc sau buổi diễn.\"",
    "Khi tiếng vỗ tay của khán giả dần dứt, hàng loạt phóng viên nhận được email và tài liệu giấy từ các trợ lý của Diệu Linh.",
    "Những tiếng xì xào bắt đầu nổi lên ở các hàng ghế báo chí.",
    "\"Cái gì thế này? Bản nhạc của Nguyễn Thế Anh đang bị kiện đạo nhạc sao?\"",
    "\"Có văn bản thụ lý chính thức của Tòa án TP.HCM này! Nguyên đơn là Lâm Hoàng Phúc!\"",
    "Sự hoang mang lan nhanh như một dịch bệnh trong khán phòng nhà hát.",
    "Thế Phong đứng dậy định đi vào hậu trường chúc mừng con trai thì một phóng viên báo Tuổi Trẻ lao tới chắn đường.",
    "\"Thưa Hiệu trưởng Thế Phong, chúng tôi vừa nhận được thông tin Tòa án TP.HCM đã thụ lý vụ án kiện con trai ông cướp đoạt bản quyền sáng tác của sinh viên Lâm Hoàng Phúc, ông giải thích thế nào về việc này?\"",
    "Mặt Thế Phong lập tức biến sắc, nụ cười đắc ý đông cứng trên môi.",
    "\"Bịa đặt! Đây là sự vu khống trắng trợn để bôi nhọ danh dự Nhạc viện!\" Thế Phong hét lên, gân cổ nổi lên đỏ rực.",
    "Thế nhưng, chiếc máy tính bảng của phóng viên giơ ra trước mặt ông ta hiển thị rõ ràng con dấu đỏ chói của Tòa án Nhân dân TP.HCM.",
    "Thế Anh từ trên sân khấu bước xuống, nhìn thấy cảnh tượng hỗn loạn ở phía dưới thì mặt mày tái mét.",
    "Phúc đứng dậy khỏi hàng ghế VIP, đi lướt qua cha con họ với ánh mắt lạnh lùng như băng.",
    "Cậu không nói một lời nào, nhưng sự im lặng của cậu lúc này có sức mạnh hơn vạn lời nói.",
    "Chiếc mặt nạ thiên tài của Nguyễn Thế Anh đã bắt đầu rạn nứt ngay trong đêm vinh quang nhất của cậu ta.",
    "Và giông bão thực sự mới chỉ là bắt đầu."
]

# Chapter 5
ch5_sentences = [
    "Sáng hôm sau, trang chủ chính thức của Chopin Competition tại Warsaw, Ba Lan công bố danh sách thí sinh chính thức bước vào vòng loại trực tiếp.",
    "Sự kiện này ngay lập tức chấn động giới mộ điệu âm nhạc cổ điển toàn cầu.",
    "Tại Việt Nam, mọi người đổ xô vào xem danh sách để tìm tên của Nguyễn Thế Anh - người được Nhạc viện lăng xê rầm rộ suốt thời gian qua.",
    "Thế nhưng, khi danh sách hiện ra, tên của Nguyễn Thế Anh hoàn toàn biến mất.",
    "Thay vào đó, ở mục thí sinh Việt Nam, chỉ có duy nhất một cái tên xuất hiện: 'Lam Hoang Phuc - Independent Candidate'.",
    "Phía dưới tên của Phúc là dòng ghi chú bảo trợ đầy quyền lực: 'Recommended by Violinist Tran Dieu Linh and Professor Janusz Olejniczak'.",
    "Tin tức này như một trận động đất cấp mười càn quét qua văn phòng Hiệu trưởng Nhạc viện TP.HCM.",
    "Nguyễn Thế Phong đập mạnh tay xuống bàn làm việc, chiếc cúp pha lê trên bàn nảy lên rồi rơi xuống đất vỡ tan tành.",
    "\"Làm sao có thể như vậy được? Lâm Hoàng Phúc lấy tư cách gì thi tự do?\" Thế Phong hét lên, mặt mũi méo mó vì giận dữ.",
    "Nguyễn Thế Anh đứng cạnh đó, gương mặt tái nhợt, đôi môi run rẩy không thốt nên lời.",
    "Cậu ta đã nộp đơn đăng ký với bản nhạc cướp đoạt, nhưng Ban tổ chức Chopin đã từ chối thẳng thừng vì đơn kiện bản quyền đang tranh chấp pháp lý.",
    "Trong khi đó, Phúc lại được đặc cách vượt qua vòng hồ sơ nhờ thư giới thiệu của hai huyền thoại âm nhạc thế giới.",
    "Thế Phong lập tức nhấc điện thoại bàn, gọi cho Trưởng phòng Đào tạo Nhạc viện.",
    "\"Gửi thông báo khẩn cấp cho Lâm Hoàng Phúc!\"",
    "\"Tước vĩnh viễn bằng tốt nghiệp của nó! Trục xuất nó khỏi danh sách sinh viên ngay lập tức!\"",
    "\"Đồng thời, gửi công văn sang Cục Quản lý xuất nhập cảnh Bộ Công an, yêu cầu tạm hoãn xuất cảnh đối với Lâm Hoàng Phúc vì lý do đang liên quan đến tranh chấp pháp lý đạo nhạc tại Nhạc viện!\"",
    "Thế Phong nghĩ rằng, chỉ cần cấm Phúc xuất cảnh, Phúc sẽ không thể bay sang Ba Lan dự thi, và mọi nỗ lực của cậu sẽ đổ sông đổ bể.",
    "Chiều hôm đó, Phúc nhận được quyết định kỷ luật tước bằng tốt nghiệp gửi đến phòng trọ.",
    "Cậu cầm tờ giấy quyết định có chữ ký và con dấu của Nguyễn Thế Phong, tay khẽ run nhưng ánh mắt vô cùng kiên định.",
    "Đúng lúc đó, Trần Diệu Linh lái chiếc xe sang trọng đến đón cậu.",
    "\"Phúc, thu xếp đồ đạc chưa? Chúng ta đi thôi.\" Linh nói qua cửa kính xe.",
    "\"Dạ thưa cô, hiệu trưởng đã gửi quyết định tước bằng tốt nghiệp và đe dọa cấm con xuất cảnh vì tranh chấp pháp lý ạ.\" Phúc nói, giọng thoáng vẻ lo lắng.",
    "Linh nghe vậy thì bật cười khinh bỉ, ánh mắt lộ rõ vẻ ngạo nghễ.",
    "\"Nguyễn Thế Phong nghĩ ông ta là ai mà đòi cấm xuất cảnh một thí sinh quốc tế?\"",
    "\"Ông ta nghĩ hệ thống pháp luật Việt Nam là do nhà ông ta mở ra sao?\"",
    "Linh mở chiếc ipad của mình, hiển thị một văn bản có đóng dấu của Bộ Ngoại giao và Bộ Văn hóa, Thể thao và Du lịch.",
    "\"Tôi đã chủ động làm việc với Thứ trưởng Bộ Văn hóa và Vụ Hợp tác Quốc tế Bộ Ngoại giao từ ba ngày trước.\"",
    "\"Chopin Competition là sự kiện văn hóa tầm cỡ ngoại giao giữa hai nước Việt Nam và Ba Lan.\"",
    "\"Việc cậu đại diện Việt Nam tham gia dưới sự bảo trợ của Giáo sư Janusz Olejniczak đã được đưa vào chương trình hợp tác văn hóa chính thức.\"",
    "\"Bộ Văn hóa đã ký văn bản bảo lãnh xuất cảnh đặc cách cho cậu, hoàn toàn bác bỏ mọi yêu cầu vô lý từ Nhạc viện TP.HCM.\"",
    "\"Còn về tấm bằng tốt nghiệp của Nhạc viện?\" Linh nhướng mày, nụ cười đầy mỉa mai.",
    "\"Một khi cậu giành giải tại Warsaw, các nhạc viện hàng đầu thế giới như Juilliard hay Moscow State Conservatory sẽ tranh nhau trao bằng danh dự cho cậu.\"",
    "\"Tấm bằng của Nhạc viện này chả là cái gì cả.\"",
    "Phúc nghe đến đây thì hoàn toàn trút bỏ được gánh nặng trong lòng, cậu nhìn Diệu Linh với sự kính trọng tuyệt đối.",
    "Cậu nhanh chóng mang theo chiếc balô cũ và hộp sắt đựng các bản thảo viết tay bước lên xe.",
    "Chiếc xe lăn bánh hướng thẳng ra sân bay quốc tế Tân Sơn Nhất.",
    "Tại văn phòng Nhạc viện, Thế Phong nhận được công văn phản hồi từ Cục Quản lý xuất nhập cảnh từ chối yêu cầu cấm xuất cảnh của ông ta.",
    "Đồng thời, một công văn từ Thanh tra Bộ Văn hóa gửi đến yêu cầu Nhạc viện TP.HCM giải trình về việc tự ý kỷ luật sinh viên Lâm Hoàng Phúc khi chưa có kết luận của Tòa án.",
    "Thế Phong ngã sụp xuống ghế giám đốc, mồ hôi lạnh chảy ròng ròng dọc thái dương.",
    "Ông ta nhận ra, vòng vây pháp lý và quyền lực đang dần siết chặt lấy cha con ông ta từ mọi phía.",
    "Còn Lâm Hoàng Phúc lúc này đã ngồi trong khoang thương gia của chuyến bay đi Warsaw, nhìn ngắm Sài Gòn rực rỡ ánh đèn lùi xa dần dưới cánh bay.",
    "Cậu biết, chuyến đi này không chỉ là để thực hiện ước mơ, mà còn là hành trình vinh quang để đòi lại công lý cho chính mình."
]

# Chapter 6
ch6_sentences = [
    "Trước ngày diễn ra buổi họp báo chính thức của Lâm Hoàng Phúc, mạng xã hội âm nhạc cổ điển Việt Nam bùng nổ một chiến dịch bôi nhọ quy mô lớn.",
    "Hàng loạt bài viết từ các trang tin mạng không chính thống và hàng ngàn tài khoản ảo đồng loạt đăng tải thông tin vu khống Phúc.",
    "\"Lâm Hoàng Phúc - kẻ đạo nhạc trắng trợn bị Nhạc viện đuổi học, trốn sang Ba Lan bằng con đường không chính thức.\"",
    "\"Sự nhục nhã của nền âm nhạc nước nhà khi một kẻ cắp chất xám đại diện đi thi Chopin quốc tế.\"",
    "Những bài viết này được chia sẻ chóng mặt trên các hội nhóm, thu hút vô số bình luận chỉ trích dữ dội từ những người thiếu thông tin.",
    "Thế Phong và Thế Anh ngồi trong biệt thự riêng ở Quận 7, đắc ý nhìn những con số tương tác tăng vọt trên màn hình điện thoại.",
    "\"Để xem sau vụ này, danh tiếng của nó bên Ba Lan làm sao cứu vãn được.\" Thế Anh cười khẩy đầy ác độc.",
    "Thế nhưng, họ không biết rằng, Trần Diệu Linh đã chuẩn bị sẵn một đòn phản công pháp lý cực kỳ tàn khốc.",
    "Chín giờ sáng ngày tiếp theo, một buổi họp báo quốc tế được tổ chức trang trọng tại Văn phòng Luật sư LNT & Partners trên đường Nguyễn Huệ, Quận 1.",
    "Hơn năm mươi phóng viên của các cơ quan báo chí lớn như Tuổi Trẻ, Thanh Niên, VnExpress và cả đại diện các hãng thông tấn nước ngoài tại TP.HCM đều có mặt.",
    "Diệu Linh mặc bộ vest đen quyền lực, cùng Luật sư Trần Hữu Trí ngồi ở vị trí trung tâm.",
    "Màn hình máy chiếu lớn phía sau sáng lên, hiển thị dòng chữ: 'Buổi Công Bố Bằng Chứng Quyền Tác Giả Bản Sonatina Đô Thứ'.",
    "Luật sư Trí chậm rãi điều chỉnh kính, giọng nói trầm ấm nhưng vô cùng đanh thép vang lên trong phòng họp.",
    "\"Kính thưa quý nhà báo, hôm nay chúng tôi thay mặt nghệ sĩ piano Lâm Hoàng Phúc công bố toàn bộ bằng chứng thép chứng minh quyền tác giả hợp pháp đối với bản Sonatina Đô thứ.\"",
    "Luật sư Trí bấm nút, màn hình hiển thị file log chi tiết của máy chủ email Google cá nhân của Phúc.",
    "\"Đây là bằng chứng đầu tiên: Email gửi đính kèm file ghi âm demo và bản nhạc số hóa được Lâm Hoàng Phúc gửi cho chính mình vào ngày 15 tháng 9 năm 2024.\"",
    "\"Ngày giờ được ghi nhận trên máy chủ Google là không thể can thiệp. Thời điểm này sớm hơn đơn đăng ký bản quyền của Nguyễn Thế Anh tận bảy tháng.\"",
    "Tiếng máy ảnh nhấp nháy liên hồi, các phóng viên nhanh chóng ghi lại những thông tin đắt giá này.",
    "Tiếp theo, Luật sư Trí công bố kết quả giám định sóng âm thanh độc lập từ Viện Khoa học Hình sự.",
    "\"Bản giám định cho thấy, cấu trúc hòa âm phức tạp và nhịp điệu rubato đặc trưng trong bản ghi âm hai năm trước của Phúc trùng khớp 100% với bản nhạc Nguyễn Thế Anh biểu diễn tại nhà hát vừa qua.\"",
    "\"Nguyễn Thế Anh không hề có bất kỳ bản phác thảo thô hay file demo nào trước ngày đăng ký bản quyền.\"",
    "Diệu Linh lúc này bước lên micro, thần thái ngạo nghễ quyến rũ thường ngày thay bằng một sự nghiêm nghị đáng sợ.",
    "\"Với tư cách là nghệ sĩ violin quốc tế và giám khảo quốc gia, tôi xin khẳng định: Nguyễn Thế Anh hoàn toàn không có đủ trình độ kỹ thuật để sáng tác một tác phẩm có chiều sâu như vậy.\"",
    "\"Hành vi cướp đoạt này là một sự sỉ nhục đối với nền âm nhạc cổ điển nước nhà.\"",
    "\"Chúng tôi đã chính thức gửi đơn tố cáo hành vi lạm dụng quyền lực, vu khống và vi phạm bản quyền của Nguyễn Thế Phong và Nguyễn Thế Anh lên Thanh tra Bộ Văn hóa và Sở Thông tin Truyền thông.\"",
    "\"Tòa án Nhân dân TP.HCM đã ra quyết định áp dụng biện pháp khẩn cấp tạm thời: Cấm Nguyễn Thế Anh biểu diễn và sử dụng bản nhạc này dưới mọi hình thức trong thời gian tranh chấp.\"",
    "Buổi họp báo kết thúc, tin tức lập tức bùng nổ trên các trang báo chính thống với những tiêu đề chấn động.",
    "\"Phơi bày sự thật vụ đạo nhạc tại Nhạc viện TP.HCM: Bằng chứng thép bảo vệ thần đồng piano Lâm Hoàng Phúc.\"",
    "\"Cha con Hiệu trưởng Nguyễn Thế Phong đối mặt với án phạt pháp lý nặng nề và làn sóng tẩy chay của giới mộ điệu.\"",
    "Làn sóng dư luận lập tức quay xe 180 độ.",
    "Những người trước đó chửi bới Phúc giờ đây đồng loạt quay sang chỉ trích sự tráo trở, đê hèn của cha con hiệu trưởng.",
    "Các nhãn hàng tài trợ và các đơn vị tổ chức sự kiện lập tức hủy bỏ toàn bộ hợp đồng biểu diễn đã ký với Nguyễn Thế Anh.",
    "Cùng lúc đó, hai chiếc xe biển xanh của Thanh tra Bộ Văn hóa và cơ quan điều tra dừng trước cổng Nhạc viện TP.HCM.",
    "Các thanh tra viên bước vào phòng làm việc của Nguyễn Thế Phong, trao tận tay ông ta quyết định tạm đình chỉ chức vụ hiệu trưởng để phục vụ thanh tra toàn diện về công tác quản lý đào tạo và tài chính.",
    "Thế Phong đứng không vững, tay chân bủn rủn bám vào thành bàn làm việc, mặt xám xịt như tro tàn.",
    "Ông ta nhận ra, đế chế quyền lực mà ông ta dày công xây dựng suốt hai mươi năm qua đã sụp đổ hoàn toàn chỉ sau một đêm họp báo.",
    "Còn ở Warsaw, Ba Lan, Lâm Hoàng Phúc vừa bước xuống sảnh khách sạn cổ kính cạnh quảng trường cổ Rynek Starego Miasta.",
    "Giữa cái lạnh cuối thu của châu Âu, Phúc hít một hơi sâu, cảm nhận sự tự do thực sự.",
    "Không còn những xiềng xích của quyền lực bóp nghẹt, giờ đây chỉ còn cậu và âm nhạc chuẩn bị chinh phục đỉnh cao thế giới."
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

novel_data["chapters"].append(format_chapter("Chương 4: Đêm Hội Nhạc Viện", ch4_sentences))
novel_data["chapters"].append(format_chapter("Chương 5: Chiếc Vé Đi Warsaw", ch5_sentences))
novel_data["chapters"].append(format_chapter("Chương 6: Cơn Giông Trước Giờ Bay", ch6_sentences))

# Write back to temp file
with open(temp_file_path, "w", encoding="utf-8") as f:
    json.dump(novel_data, f, ensure_ascii=False, indent=2)

print("Stage 2 completed successfully. Appended Chapters 4-6.")
