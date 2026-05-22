import json

TEMP_PATH = "/Users/aaronnguyen/TN/App/doctieuthuyet/pending_novel_7_temp.json"

def count_words(text):
    clean_text = text.replace("<p>", "").replace("</p>", "").replace("\n", " ")
    return len([w for w in clean_text.split() if w.strip()])

# Read the temp file containing Chapters 1-3
with open(TEMP_PATH, "r", encoding="utf-8") as f:
    novel_data = json.load(f)

# Chapter 4: Bí Mật Bên Trong Căn Nhà Cổ
ch4_sentences = [
    "Đồng hồ điểm mười hai giờ đêm, phố cổ Hàng Bạc chìm trong màn sương mù và những hạt mưa phùn mùa hạ.",
    "Bên dưới bóng tối đen đặc của con ngõ Phất Lộc, hai bóng người lặng lẽ áp sát vào bức tường gạch vồ rêu phong.",
    "Đỗ Minh Tuấn mặc chiếc áo khoác gió sẫm màu, tay cầm chiếc đèn pin chuyên dụng và bộ máy ảnh khảo cổ.",
    "Lê Bảo Ngọc đứng bên cạnh cô, gương mặt thanh tú lộ vẻ kiên định, hơi thở phả ra làn khói mỏng dưới làn gió đêm buốt lạnh.",
    "\"Cậu chắc chắn chúng ta có thể vào bằng lối này chứ?\" Ngọc hỏi khẽ, ánh mắt cảnh giác nhìn xung quanh.",
    "Tuấn gật đầu: \"Đây là lối thông gió cũ của hệ thống nhà ống Hà Nội cổ, cánh cửa gỗ trên cao đã bị mục nát từ lâu.\"",
    "Với sự hỗ trợ của Tuấn, Ngọc nhanh nhẹn trèo lên gờ tường, lách người qua ô cửa gỗ lim mục nát để lẻn vào bên trong.",
    "Tuấn nhanh chóng bám theo sau, cả hai đáp nhẹ nhàng xuống nền đất âm u của tầng gác lửng căn nhà cổ.",
    "Không khí bên trong vô cùng ngột ngạt, sực mùi gỗ lim ẩm mốc và bụi bặm của hàng thế kỷ tích tụ.",
    "Tuấn bật chiếc đèn pin có chụp mờ, ánh sáng vàng ấm áp hắt lên hệ thống xà gồ và các đấu củng khổng lồ.",
    "Dưới ánh sáng dịu, hệ thống kết cấu mộng gỗ hiện lên sừng sững như một tác phẩm nghệ thuật kiến trúc đỉnh cao.",
    "Ngọc khẽ vuốt ve bề mặt cột gỗ lim đen bóng, móng tay cô chạm vào những vết khía hoa văn tinh xảo.",
    "\"Thật không thể tin nổi, đây chính xác là hệ mộng ghép hoa văn thời Nguyễn Minh Mệnh,\" Ngọc thì thầm đầy xúc động.",
    "\"Nhìn những đường chạm khắc hoa văn lá lật này xem, chúng chỉ được phép xuất hiện ở các công trình hoàng gia hoặc phủ đệ quan lại.\"",
    "Tuấn không nói gì, anh quỳ xuống góc tường phía sau bàn thờ cổ bằng gỗ gụ bám đầy tơ nhện.",
    "Tay anh run rẩy cạo sạch lớp thạch cao rẻ tiền mà chủ sở hữu trước đó đã trét lên để che giấu bức tường cũ.",
    "Dưới lớp thạch cao bong tróc, một phiến đá xanh Thanh Hóa nguyên khối dần lộ ra trước sự kinh ngạc của hai người.",
    "Trên mặt bia đá, những dòng chữ Nho cổ được chạm khắc vô cùng sắc nét và sâu hoắm vào lòng đá.",
    "Ngọc vội vàng lấy từ trong túi ra cuốn sổ tay khảo cổ, dùng bút chì và giấy chuyên dụng để dập lại mặt bia.",
    "\"Năm Minh Mệnh thứ mười sáu, sắc phong phủ đệ của Thượng thư bộ Công...\" Ngọc dịch lớn, giọng cô run lên vì chấn động.",
    "\"Tuấn ơi! Đây là phủ đệ của một vị Thượng thư thời Nguyễn! Đây là di tích quốc gia cực kỳ quý hiếm!\"",
    "\"Nó chứng minh rằng ngôi nhà này không chỉ là nhà cổ bình thường, mà là một công trình công cộng có giá trị lịch sử vô giá!\"",
    "Lồng ngực Tuấn phập phồng dữ dội, những giọt mồ hôi lạnh chảy ròng ròng trên trán hòa cùng niềm vui sướng khôn tả.",
    "\"Đúng vậy, hệ mộng chịu lực này chính là do các nghệ nhân kinh đô Huế ra xây dựng,\" Tuấn tiếp lời, giọng nghẹn ngào.",
    "\"Bản vẽ tay của tôi đã tái hiện chính xác hệ thống này, đó là lý do Nguyễn Minh Hải muốn chiếm đoạt nó bằng mọi giá.\"",
    "Đột nhiên, phía dưới tầng trệt vang lên tiếng loảng xoảng của xích sắt bị tháo bỏ, kèm theo tiếng bước chân dồn dập.",
    "Ánh đèn pin cực mạnh từ bên ngoài chiếu thẳng qua khe cửa sổ gỗ, quét qua quét lại trên tầng gác lửng.",
    "\"Có kẻ đột nhập! Mau lùng sục khắp căn nhà cho tao!\" Tiếng một gã đàn ông thô lỗ gầm lên đầy giận dữ.",
    "Ngọc nhanh tay thu hồi cuộn giấy dập bia đá, cất vội vào túi chuyên dụng chống nước dưới ngực.",
    "Tuấn nắm chặt tay Ngọc, kéo cô nép sát vào bóng tối sau cây cột lim khổng lồ để tránh ánh đèn pin quét qua.",
    "Tim họ đập liên hồi như trống trận, mồ hôi lạnh vã ra như tắm dưới sự truy đuổi sát sao của kẻ thù.",
    "Hai gã bảo vệ bặm trợn của Thịnh Phát cầm gậy sắt thô bạo bước lên cầu thang gỗ, tiếng bước chân côm cốp vang lên dội thẳng vào màng nhĩ.",
    "\"Đừng để chúng trốn thoát! Đại ca Dũng đã dặn, nếu gặp thằng Tuấn ở đây, cứ đập gãy chân nó rồi ném xuống sông Hồng!\"",
    "Tuấn siết chặt nắm tay, khớp xương kêu lên răng rắc, sẵn sàng lao ra liều mạng để bảo vệ Ngọc và tập tài liệu quý giá.",
    "Nhưng Ngọc khẽ bấm nhẹ vào tay Tuấn, ra hiệu cho anh nhìn về phía ô thoáng thoát hiểm ở phía sau mái ngói.",
    "Họ nhẹ nhàng di chuyển trên các thanh xà gồ lim chắc chắn, khéo léo trèo ra ngoài mái ngói dốc đứng trơn trượt vì nước mưa.",
    "Tiếng la hét giận dữ vang lên bên trong khi bọn bảo vệ phát hiện ra phiến đá bị cạo sạch thạch cao.",
    "\"Khốn kiếp! Chúng trèo ra mái nhà rồi! Mau đuổi theo!\" Tiếng gầm rú vang lên cắt xé màn đêm phố cổ.",
    "Tuấn và Ngọc trượt nhanh xuống theo đường dốc mái ngói, nhảy thẳng xuống mui chiếc xe SUV công vụ của Sở đang nổ máy chờ sẵn.",
    "Tài xế trung thành lập tức nhấn ga, chiếc xe lao vút đi trong màn đêm, bỏ lại đám giang hồ Thịnh Phát đang gầm rú bất lực phía sau.",
    "Ngọc ôm chặt tập tài liệu dập bia đá vào lòng, khuôn mặt lấm lem bụi than nhưng đôi mắt phượng lại sáng rực lên như sao sa.",
    "\"Chúng ta đã có bằng chứng thép rồi, Tuấn ạ! Vương Thế Dũng và Hoàng Văn Nam lần này không thể chối cãi được nữa!\" Ngọc tuyên bố đầy đanh thép.",
    "Tuấn nhìn ra cửa kính xe, những hạt mưa đêm trôi nhanh trên mặt kính, lòng anh tràn ngập niềm tin vào công lý.",
    "Anh biết, đêm nay họ đã thắng một trận quan trọng, nhưng cơn giận dữ của tập đoàn Thịnh Phát sẽ sớm đổ ập xuống đầu họ."
]

# Let's add extra sentences to make sure Chapter 4 hits ~1200 words.
extra_ch4 = [
    "Chiếc xe công vụ lao nhanh qua những con phố cổ vắng lặng như Hàng Đường, Hàng Ngang rồi hướng thẳng về phía Hồ Tây.",
    "Hơi ấm từ máy điều hòa trong xe dần làm dịu đi cái lạnh thấu xương của trận mưa đêm trên mái nhà cổ.",
    "Tuấn lấy khăn giấy lau vội những vết bùn đất trên mặt Ngọc, hành động tự nhiên khiến cả hai khẽ ngượng ngùng.",
    "Ngọc mỉm cười nhẹ, ánh mắt cô nhìn Tuấn tràn đầy sự tin cậy và trân trọng đối với một người đồng chí thực sự.",
    "\"Phiến bia đá này là chìa khóa pháp lý tối thượng,\" Ngọc mở tập giấy dập ra, cẩn thận kiểm tra từng nét chữ Nho.",
    "\"Theo Luật Di sản văn hóa hiện hành, bất kỳ công trình nào có sắc phong của triều đình đều được tự động xếp hạng bảo vệ khẩn cấp.\"",
    "\"Hoàng Văn Nam dù có một trăm cái gan cũng không dám ký lệnh cưỡng chế phá dỡ khi hồ sơ này được công bố.\"",
    "Tuấn siết chặt hai tay, đôi mắt anh lóe lên tia sáng sắc lạnh: \"Nhưng chúng ta phải nhanh lên, Dũng là kẻ điên cuồng.\"",
    "\"Hắn biết chúng ta đã tìm ra bia đá, hắn chắc chắn sẽ cho người phá hủy phiến đá đó ngay trong đêm nay để phi tang bằng chứng.\"",
    "Ngọc trầm ngâm một lát rồi rút điện thoại ra, gọi một cuộc điện thoại trực tiếp cho thư ký riêng của mình.",
    "\"Alo, lập tức soạn thảo văn bản khẩn gửi UBND Thành phố và Bộ Văn hóa, yêu cầu phong tỏa nghiêm ngặt căn nhà cổ Hàng Bạc.\"",
    "\"Nêu rõ phát hiện khảo cổ về bia đá sắc phong Thượng thư bộ Công thời Nguyễn Minh Mệnh.\"",
    "\"Tôi sẽ ký đóng dấu đỏ ngay khi về đến cơ quan. Làm việc này ngay lập tức, không được chậm trễ một giây!\"",
    "Cúp máy, Ngọc nhìn Tuấn đầy kiên định: \"Tôi đã giăng lưới, giờ hãy xem Vương Thế Dũng xoay xở thế nào với pháp luật.\"",
    "Tuấn nhìn người phụ nữ thông minh tuyệt đỉnh bên cạnh, lòng dâng lên sự ngưỡng mộ sâu sắc đối với khí chất của cô.",
    "Anh biết, cuộc chiến này tuy hiểm nguy nhưng anh không còn đơn độc trên con đường bảo vệ di sản Thăng Long nữa."
]
ch4_sentences.extend(extra_ch4)

# Chapter 5: Bẫy Sập Và Sự Kiêu Ngạo Của Kẻ Đi Săn
ch5_sentences = [
    "Sáng hôm sau, trụ sở của Tập đoàn địa ốc Thịnh Phát tại khu đô thị mới Cầu Giấy hiện ra sừng sững như một tòa tháp kính tráng lệ.",
    "Tại văn phòng Tổng giám đốc rộng hàng trăm mét vuông ở tầng cao nhất, Vương Thế Dũng ngồi chễm chệ trên chiếc ghế da cá sấu đắt tiền.",
    "Gương mặt gã chữ điền oai vệ, đôi mắt sắc lẹm chứa đầy sự tàn nhẫn và kiêu ngạo của một kẻ nắm giữ hàng ngàn tỷ đồng.",
    "Nguyễn Minh Hải đứng bên cạnh gã, vẻ khúm núm sợ hãi lộ rõ trên khuôn mặt khi báo cáo về sự việc đêm qua.",
    "\"Đồ vô dụng! Có hai kẻ đột nhập mà các người cũng để chúng trốn thoát với tài liệu khảo cổ sao?\" Dũng gầm lên, đập mạnh tay xuống bàn kính.",
    "Chiếc ly pha lê đựng rượu ngoại va đập mạnh lên mặt bàn phát ra tiếng kêu leng keng chói tai.",
    "Hải run rẩy cúi đầu, mồ hôi lạnh chảy ròng ròng trên trán gã: \"Dạ thưa anh Dũng, con mụ Lê Bảo Ngọc dùng xe công vụ chở thằng Tuấn đi.\"",
    "\"Bọn đàn em không dám đụng vào xe của Phó Giám đốc Sở vì sợ làm lớn chuyện.\"",
    "Dũng khẽ nhếch môi nở một nụ cười nửa miệng đầy mưu mô và khinh miệt: \"Lê Bảo Ngọc? Một con nhãi ranh học ở Tây về thì làm được gì?\"",
    "\"Hắn nghĩ cái mác UNESCO và chức Phó Giám đốc Sở của hắn có thể chống lại được thế lực của Thịnh Phát sao?\"",
    "Dũng thong thả rút ra một tập hồ sơ tài chính dày cộp, ném mạnh xuống trước mặt Nguyễn Minh Hải.",
    "\"Nhìn cho kỹ đi, đây là phê duyệt dòng vốn ODA khống trị giá ba mươi triệu đô la từ ngân hàng đối tác nước ngoài cho dự án Hàng Bạc Plaza.\"",
    "\"Hội đồng thẩm định liên ngành đã nhận của tao năm mươi tỷ đồng lót tay, tất cả đã ký tên đóng dấu đồng ý phá dỡ.\"",
    "\"Sáng mai, lễ động thổ vẫn sẽ diễn ra rầm rộ với sự tham gia của dàn quan chức cấp cao của thành phố.\"",
    "\"Để xem con nhãi Lê Bảo Ngọc đó dám dùng tờ giấy dập bia đá rách nát kia để ngăn cản bánh xe lịch sử của tao như thế nào!\"",
    "Hải nhìn thấy đống hồ sơ phê duyệt liền thở phào nhẹ nhõm, ánh mắt gã bỗng chốc trở nên vô cùng đắc ý.",
    "\"Anh Dũng quả là thần cơ diệu toán, thằng Tuấn lần này chỉ có nước vào tù mục xương vì tội vu khống và phá hoại kinh tế thôi!\"",
    "Dũng cười lớn, tiếng cười vang lên trầm đục và đầy uy quyền tàn nhẫn trong không gian sang trọng.",
    "\"Tao đã gửi một món quà đặc biệt đến cho thằng kiến trúc sư què quặt đó rồi. Để xem nó có mạng sống để dự lễ động thổ ngày mai không.\"",
    "Cùng lúc đó, tại phòng làm việc tạm thời của Tuấn ở Sở Quy hoạch Kiến trúc, anh vừa nhận được một phong bì thư không người gửi.",
    "Bên trong phong bì là một tấm ảnh chụp ngôi nhà của mẹ anh ở quê hương Nam Định, kèm theo một viên đạn súng bắn tỉa lạnh ngắt.",
    "Dưới bức ảnh là dòng chữ viết tay bằng mực đỏ tươi như máu: \"Dừng lại hoặc chuẩn bị quan tài cho mẹ mày.\"",
    "Tuấn nhìn viên đạn trên tay, mồ hôi lạnh chảy ròng ròng dọc theo sống lưng, đầu óc anh bỗng chốc trống rỗng.",
    "Hai bên màng tang anh giật mạnh liên tục, hơi thở dồn dập khiến lồng ngực phập phồng dữ dội vì lo sợ cho sự an nguy của mẹ.",
    "Sự kiêu ngạo và tàn ác của Vương Thế Dũng đã vượt qua mọi giới hạn đạo đức và luật pháp của con người.",
    "Chúng sẵn sàng dùng mạng sống của người thân để ép anh phải khuất phục trước sức mạnh của đồng tiền.",
    "Ngay lúc đó, Lê Bảo Ngọc bước vào phòng, nhìn thấy viên đạn và bức ảnh trên bàn, sắc mặt cô bỗng chốc trở nên vô cùng nghiêm trọng.",
    "Cô tiến lại gần, đặt tay lên bờ vai đang run rẩy của Tuấn, giọng nói vang lên kiên định và ấm áp.",
    "\"Tuấn, đừng sợ. Tôi đã cho người đón mẹ cậu lên Hà Nội lánh nạn an toàn từ sáng sớm nay rồi.\"",
    "\"Vương Thế Dũng nghĩ rằng hắn có thể dùng bạo lực để che bầu trời, nhưng hắn đã lầm to.\"",
    "\"Hành vi đe dọa giết người này sẽ là bằng chứng đanh thép nhất để cơ quan công an vào cuộc điều tra đặc biệt đối với gã.\"",
    "Tuấn ngước đầu nhìn Ngọc, sự hoảng loạn trong mắt anh dần được thay thế bằng sự biết ơn sâu sắc và lòng căm thù tột độ.",
    "\"Cảm ơn cô, Ngọc. Dũng đã ra tay tàn nhẫn như vậy, tôi quyết không thể lùi bước,\" Tuấn nghiến răng nói, khớp xương tay kêu răng rắc.",
    "Ngọc gật đầu sắc lạnh: \"Đúng vậy, chúng ta sẽ tương kế tựu kế, để chúng tự đắc ý tổ chức lễ động thổ ngày mai.\"",
    "\"Khi sự kiêu ngạo của chúng lên đến đỉnh điểm, cũng chính là lúc chiếc bẫy thép mà chúng ta giăng sẵn sẽ sập xuống nghiền nát chúng.\"",
    "Cô khẽ mỉm cười sắc sảo, nụ cười chứa đựng sự tự tin của một chuyên gia tầm cỡ quốc tế đang nắm giữ thế chủ động."
]
extra_ch5 = [
    "Viên đạn lạnh ngắt nằm trên mặt bàn gỗ như một minh chứng cho sự điên cuồng của những kẻ tài phiệt tha hóa.",
    "Tuấn cầm viên đạn lên, cảm giác kim loại sắc lạnh thấm vào da thịt, kích thích mọi tế bào chiến đấu trong anh.",
    "\"Vương Thế Dũng nghĩ rằng tiền bạc có thể mua được tất cả, từ lương tâm quan chức đến sinh mạng con người,\" Tuấn nói, giọng đanh thép.",
    "\"Nhưng hắn không biết rằng có những thứ di sản vô giá của Thăng Long mà ngàn tỷ đồng cũng không thể mua nổi.\"",
    "Ngọc nhìn anh đầy tán thưởng: \"Rất tốt, khí phách của cậu chính là thứ vũ khí mạnh nhất mà chúng ta có.\"",
    "\"Tôi đã liên hệ với các đồng chí bên Cục Cảnh sát C03, họ đã lập ban chuyên án theo dõi hành vi rửa tiền của Thịnh Phát từ lâu.\"",
    "\"Dòng tiền ODA khống ba mươi triệu đô la mà Dũng vừa khoe khoang thực chất là tiền huy động trái phép từ các công ty ma ở nước ngoài.\"",
    "\"Chỉ cần lễ động thổ diễn ra, dòng tiền đó chính thức được kích hoạt, chúng ta sẽ bắt trọn cả mẻ lưới liên minh bẩn thỉu này.\"",
    "Tuấn thở phào một hơi, nỗi lo lắng cho gia đình hoàn toàn biến mất, thay vào đó là ý chí chiến đấu hừng hực.",
    "Anh nhìn bức ảnh căn nhà cổ Hàng Bạc trên bàn, thầm thề rằng ngày mai sẽ là ngày phán xét cuối cùng cho những kẻ ăn cắp di sản."
]
ch5_sentences.extend(extra_ch5)

# Chapter 6: Cuộc Chiến Trên Bàn Giấy
ch6_sentences = [
    "Bão tố thực sự bùng nổ tại văn phòng Sở Quy hoạch Kiến trúc Hà Nội vào buổi sáng ngày tiếp theo.",
    "Hoàng Văn Nam - Trưởng phòng Quy hoạch, đích thân dẫn đầu một đoàn thanh tra nội bộ ập vào phòng làm việc của Lê Bảo Ngọc.",
    "Trên tay gã là văn bản kỷ luật cảnh cáo có chữ ký của Giám đốc Sở tha hóa, gương mặt gã lộ rõ vẻ hung hãn và đắc ý.",
    "\"Lê Bảo Ngọc! Đồng chí bị cáo buộc lạm dụng chức quyền, tự ý đình chỉ dự án kinh tế trọng điểm Hàng Bạc Plaza không qua phê duyệt!\"",
    "\"Đây là quyết định đình chỉ công tác tạm thời đối với đồng chí để phục vụ công tác điều tra nội bộ!\" Nam dõng dạc tuyên bố.",
    "Đám nhân viên dưới quyền sợ hãi nép sang hai bên, không ai dám lên tiếng trước uy quyền hung hãn của Trưởng phòng Nam.",
    "Lê Bảo Ngọc vẫn ngồi thong thả sau bàn làm việc, đôi mắt phượng khẽ nheo lại nhìn tờ quyết định kỷ luật ném trên bàn.",
    "Cô không hề tỏ ra hoang mang hay sợ hãi, ngược lại, khóe môi cô khẽ nhếch lên nở một nụ cười nửa miệng đầy sự khinh miệt.",
    "\"Hoàng Văn Nam, anh có biết Luật Công chức và Luật Di sản văn hóa quy định thế nào về hành vi cố ý làm sai lệch hồ sơ quy hoạch không?\" Ngọc hỏi, giọng lạnh lùng.",
    "\"Cô đừng có dùng luật ra để lòe tôi! Quyết định này có chữ ký của Giám đốc Sở, cô buộc phải chấp hành!\" Nam quát lớn, đập mạnh tay xuống bàn làm việc.",
    "Mồ hôi hột trên trán gã Nam rịn ra, rơi lã chã xuống mặt bàn gỗ bóng loáng dưới áp lực vô hình từ khí chất của Ngọc.",
    "Ngọc chầm chậm đứng dậy, vạt áo vest đen phẳng phiu, cô rút từ trong ngăn kéo ra một văn bản khẩn cấp có dấu đỏ của Văn phòng Chính phủ.",
    "\"Nhìn cho rõ đi. Đây là lệnh chỉ đạo trực tiếp từ Phó Thủ tướng Chính phủ về việc thanh tra toàn diện công tác bảo tồn di sản phố cổ Hà Nội.\"",
    "\"Văn bản nêu rõ, mọi dự án xây dựng trong vùng bảo vệ di sản cấp một quốc gia phải được dừng lại để thẩm định độc lập.\"",
    "\"Hoàng Văn Nam, anh muốn dùng quyết định của Giám đốc Sở để đè lên lệnh chỉ đạo trực tiếp của Chính phủ sao?\"",
    "Gương mặt Hoàng Văn Nam bỗng chốc trở nên xám ngoét như tro tàn, tờ giấy kỷ luật trên tay gã run rẩy kịch liệt.",
    "Gã không ngờ Lê Bảo Ngọc lại có thể tiếp cận được cấp cao nhất của Chính phủ để lấy được lệnh chỉ đạo tối thượng này nhanh đến thế.",
    "Cùng lúc đó, tại kho lưu trữ tài liệu cổ của Viện Viễn Đông Bác Cổ (EFEO) tại Hà Nội, Đỗ Minh Tuấn đang dầm mưa tìm kiếm tài liệu.",
    "Những hạt mưa mùa hạ trút xuống mái ngói viện nghiên cứu cổ kính, tạo nên những tiếng kêu rào rào liên tục không ngớt.",
    "Tuấn miệt mài lật giở từng trang tài liệu ố vàng từ thế kỷ mười chín, các khớp ngón tay anh đau nhức vì lạnh buốt.",
    "Anh biết, chỉ có bản đồ quy hoạch gốc do chính quyền thuộc địa Pháp lập mới là bằng chứng không thể chối cãi về ranh giới bảo tồn nghiêm ngặt.",
    "Sau bốn tiếng tìm kiếm điên cuồng, bàn tay Tuấn bỗng khựng lại trước một tập hồ sơ da bò mục nát có dòng chữ tiếng Pháp: \"Plan de la zone historique de Hanoi - 1885\".",
    "Anh cẩn thận mở tập hồ sơ, bên trong là tấm bản đồ quy hoạch chi tiết 36 phố phường do chính tay Kiến trúc sư trưởng người Pháp ký nhận.",
    "Trên bản đồ, căn nhà cổ Hàng Bạc được khoanh vùng màu đỏ đậm với ghi chú rõ ràng bằng tiếng Pháp: \"Monument historique protégé - Ne pas détruire\" (Di tích lịch sử được bảo vệ - Nghiêm cấm phá hủy).",
    "Bên cạnh bản vẽ là sơ đồ đo đạc hệ khung gỗ lim chịu lực hoàn toàn trùng khớp với bản vẽ tay độc bản của Tuấn bị Hải cướp đoạt.",
    "Nước mắt Tuấn rơi lã chã xuống mặt kính bảo vệ tấm bản đồ cổ, lồng ngực anh phập phồng dữ dội vì xúc động khôn cùng.",
    "\"Chúng ta thắng rồi... Chúng ta thực sự thắng rồi!\" Tuấn thốt lên, giọng nói nghẹn ngào vang vọng giữa kho lưu trữ vắng lặng.",
    "Anh lập tức dùng máy ảnh chuyên dụng chụp lại toàn bộ tấm bản đồ dưới độ phân giải cao nhất, gửi trực tiếp về máy điện thoại của Ngọc.",
    "Nhận được hình ảnh từ Tuấn, Lê Bảo Ngọc nhìn Hoàng Văn Nam đang đứng đờ đẫn trước bàn làm việc, ánh mắt cô lộ rõ vẻ chiến thắng tuyệt đối.",
    "\"Hoàng Văn Nam, hồ sơ quy hoạch gốc năm một nghìn tám trăm tám mươi lăm đã được tìm thấy,\" Ngọc dõng dạc công bố.",
    "\"Nó chứng minh bản vẽ của Nguyễn Minh Hải là sản phẩm ăn cắp hoàn toàn từ hồ sơ lưu trữ của Pháp, và dự án Hàng Bạc Plaza là hành vi phá hoại di sản đặc biệt nghiêm trọng.\"",
    "\"Anh và Vương Thế Dũng chuẩn bị đón nhận lệnh khởi tố từ Cục Cảnh sát Kinh tế đi!\"",
    "Nam lùi lại vài bước, đầu óc gã quay cuồng, mồ hôi lạnh chảy ròng ròng ướt đẫm cả lưng áo sơ mi đắt tiền.",
    "Gã biết, liên minh lợi ích bẩn thỉu mà gã dày công xây dựng cùng Thịnh Phát giờ đây đang đứng trước nguy cơ sụp đổ hoàn toàn trước đòn đánh trực diện này."
]
extra_ch6 = [
    "Tiếng sấm rền vang ngoài trời như tiếng kèn báo hiệu cho ngày tàn của những kẻ tha hóa quyền lực.",
    "Nam lắp bắp không thành tiếng, định giật lấy điện thoại của Ngọc nhưng bị ánh mắt sắc lạnh của cô chặn đứng.",
    "\"Đừng tự làm nhục nhã bản thân hơn nữa, Nam ạ,\" Ngọc nói, giọng điệu chứa đầy sự khinh bỉ tột cùng.",
    "\"Mọi hành vi của anh từ việc nhận tiền hối lộ đến việc đe dọa cán bộ đều đã được ghi âm và chuyển cho cơ quan thanh tra.\"",
    "Đoàn thanh tra nội bộ đi cùng Nam thấy thế liền vội vã lùi lại, nhìn Nam với ánh mắt ghẻ lạnh và xa lánh.",
    "Họ hiểu rằng kẻ đứng đầu phòng quy hoạch giờ đây đã trở thành một con tốt bị bỏ rơi trên bàn cờ chính trị.",
    "Ngọc quay lưng lại phía gã Nam, nhìn ra cửa sổ văn phòng hướng về phía lăng Bác và quảng trường Ba Đình đầy nắng gió.",
    "Cô biết, trận chiến trên bàn giấy đã kết thúc thắng lợi, nhưng cuộc chiến thực địa đầy hiểm nguy ngoài phố cổ đang chờ đợi cô và Tuấn đêm nay."
]
ch6_sentences.extend(extra_ch6)

novel_data["chapters"].append({
    "title": "Chương 4: Bí Mật Bên Trong Căn Nhà Cổ",
    "content": "\n".join([f"<p>{s}</p>" for s in ch4_sentences])
})

novel_data["chapters"].append({
    "title": "Chương 5: Bẫy Sập Và Sự Kiêu Ngạo Của Kẻ Đi Săn",
    "content": "\n".join([f"<p>{s}</p>" for s in ch5_sentences])
})

novel_data["chapters"].append({
    "title": "Chương 6: Cuộc Chiến Trên Bàn Giấy",
    "content": "\n".join([f"<p>{s}</p>" for s in ch6_sentences])
})

# Write Stage 2 JSON file back to TEMP_PATH
with open(TEMP_PATH, "w", encoding="utf-8") as f:
    json.dump(novel_data, f, ensure_ascii=False, indent=2)

print("Stage 2 completed. Chapters 4-6 appended successfully.")
