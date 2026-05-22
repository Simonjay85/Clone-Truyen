import json
import os

novel_data = {
    "idx": 9,
    "title": "Thần Đồng Piano Nhạc Viện: Bị Cấm Biểu Diễn, Tôi Chấn Động Chopin Competition",
    "author": "Lâm Hoàng Phúc",
    "genre": "Sảng Văn",
    "intro": "<p><strong>\"Một đứa không cha không mẹ, sống bằng học bổng như cậu, lấy tư cách gì đòi đứng chung hàng ngũ với con trai tôi ở đấu trường quốc tế?\"</strong></p>\n<p>Lâm Hoàng Phúc bị cướp đi bản giao hưởng độc tấu piano đầy tâm huyết, bị Nhạc viện TP.HCM đuổi cổ dưới danh nghĩa kẻ đạo nhạc hèn hạ. Trong cơn bão sỉ nhục, anh đã gặp Trần Diệu Linh - nữ thần violin kiêm giám khảo quyền lực, người nhìn thấu đôi bàn tay thiên tài bị vùi dập.</p>\n<p>Dưới sự bảo trợ của cô, thần đồng bị cấm biểu diễn bắt đầu hành trình phản công chấn động từ Sài Gòn tới Warsaw, vạch trần bộ mặt giả tạo của cha con hiệu trưởng và chấn động toàn bộ giới mộ điệu Chopin Competition thế giới.</p>",
    "cover_prompt": "A beautiful anime-style book cover, a talented young Vietnamese man with determined eyes playing a grand piano on a brilliant stage, glowing keys, beside him stands a beautiful Vietnamese woman holding a violin, dramatic stage lighting, background hints of Warsaw Philharmonic Hall and historic Saigon, classical music elegance, emotional and premium web novel poster art",
    "chapters": []
}

# Chapter 1
ch1_sentences = [
    "Tiếng đàn Steinway & Sons vang vọng khắp phòng hòa nhạc lớn của Nhạc viện Thành phố Hồ Chí Minh trên đường Nguyễn Du.",
    "Lâm Hoàng Phúc nhắm mắt, mười đầu ngón tay lướt như bay trên những phím ngà bóng loáng.",
    "Bản Sonatina giọng Đô thứ do chính cậu sáng tác đang bước vào những khuông nhạc cao trào nhất.",
    "Giai điệu lúc thì dồn dập như cơn mưa rào đổ xuống phố phường Sài Gòn, lúc lại da diết trầm mặc như tiếng thở dài của đêm thâu.",
    "Trên trán Phúc lấm tấm mồ hôi, nhưng ánh mắt cậu rực sáng một niềm đam mê thuần khiết.",
    "Cậu đã dành suốt ba năm qua, thức thâu đêm trong căn phòng trọ chật hẹp ở quận 4 để hoàn thành tác phẩm này.",
    "Đây không chỉ là bài thi tốt nghiệp, mà còn là chiếc vé giúp cậu nộp đơn tham gia cuộc thi piano danh giá nhất thế giới - Chopin Competition tại Ba Lan.",
    "Nốt nhạc cuối cùng vang lên, âm thanh ngân dài rồi tan dần vào không gian tĩnh lặng của khán phòng.",
    "Phúc thở phào nhẹ nhõm, từ từ đứng dậy và cúi đầu chào ban giám khảo phía dưới.",
    "Thế nhưng, đáp lại cậu không phải là những tràng pháo tay tán thưởng, mà là một sự im lặng đáng sợ.",
    "Hiệu trưởng Nguyễn Thế Phong ngồi ở hàng ghế trung tâm, gương mặt trung niên đạo mạo không một chút cảm xúc.",
    "Bên cạnh ông ta, Nguyễn Thế Anh - con trai hiệu trưởng và cũng là bạn cùng lớp của Phúc - đang nở một nụ cười đầy mỉa mai.",
    "Thế Phong chậm rãi tháo kính xuống, đặt lên bàn rồi đứng dậy, tiếng gót giày da gõ cộp cộp xuống nền gỗ nghe vô cùng buốt tai.",
    "\"Lâm Hoàng Phúc, cậu giải thích thế nào về bản nhạc vừa rồi?\" Giọng Thế Phong trầm xuống, chứa đựng một sự áp bức vô hình.",
    "Phúc hơi khựng lại, đôi bàn tay thanh tú vô thức siết nhẹ gấu áo vest cũ.",
    "\"Dạ thưa Hiệu trưởng và Hội đồng, đây là bản Sonatina do con tự sáng tác trong suốt ba năm qua ạ.\"",
    "\"Tự sáng tác?\" Nguyễn Thế Anh bất ngờ đứng bật dậy, gương mặt điển trai méo mó vì khinh bỉ.",
    "\"Mày còn dám mở miệng nói là tự sáng tác sao?\"",
    "\"Bản Sonatina này là tác phẩm tao đã hoàn thành từ sáu tháng trước, thậm chí đã đăng ký bảo hộ quyền tác giả tại Cục Bản quyền tác giả!\"",
    "\"Mày là đồ ăn cắp!\"",
    "Lời buộc tội của Thế Anh như một tia sét giữa trời quang, khiến toàn bộ học sinh dự thính phía sau xôn xao bàn tán.",
    "Phúc cảm thấy máu trong người như đông cứng lại, hai tai ù đi.",
    "Cậu nhìn thẳng vào Thế Anh, giọng nói run rẩy nhưng kiên quyết.",
    "\"Cậu nói cái gì? Bản nhạc này tôi viết từng nốt một, từ bản phác thảo thô cho đến phối khí đều do tôi làm.\"",
    "\"Làm sao có thể là của cậu được?\"",
    "Nguyễn Thế Phong lúc này bước lên sân khấu, ném mạnh một tập tài liệu dày lên nắp đàn Steinway kêu lên một tiếng \"rầm\" chói tai.",
    "\"Cậu tự nhìn đi! Đây là chứng nhận đăng ký bản quyền mang tên Nguyễn Thế Anh, được cấp cách đây ba tháng.\"",
    "\"Mọi cấu trúc hòa âm, nhịp điệu rubato đặc trưng và cả đoạn chuyển tông đều trùng khớp hoàn toàn với những gì cậu vừa chơi.\"",
    "Phúc run rẩy cầm tập tài liệu lên, từng dòng chữ, con dấu đỏ chói của Cục Bản quyền hiện rõ mồn một trước mắt.",
    "Đó chính xác là bản Sonatina của cậu, không sai một nốt nhạc.",
    "Nhưng tên tác giả lại ghi rõ ràng: Nguyễn Thế Anh.",
    "Đầu óc Phúc quay cuồng, cậu nhớ lại cách đây một tháng, Thế Anh đã mượn tập nhạc của cậu với lý do \"học hỏi tham khảo\".",
    "Hóa ra, cha con họ đã âm thầm đem bản nhạc này đi đăng ký bản quyền dưới tên của Thế Anh.",
    "\"Hiệu trưởng, đây là sự tráo trở!\" Phúc uất ức đến cực điểm, gân xanh nổi lên trên cổ.",
    "\"Chính Thế Anh đã mượn bản thảo của con! Con vẫn còn bản phổ viết tay ở phòng trọ!\"",
    "Nguyễn Thế Phong cười lạnh một tiếng, ánh mắt nhìn Phúc như nhìn một con kiến hôi.",
    "\"Bản phổ viết tay? Ai chứng minh được cậu không phải là kẻ sao chép từ bản quyền đã được bảo hộ hợp pháp của con trai tôi?\"",
    "\"Hội đồng nghệ thuật Nhạc viện TP.HCM quyết định: Hủy bỏ tư cách thi tốt nghiệp của Lâm Hoàng Phúc.\"",
    "\"Đồng thời, cấm cậu biểu diễn tại tất cả các sự kiện của Nhạc viện và tước quyền đại diện Nhạc viện tham gia Chopin Competition năm nay.\"",
    "Từng lời nói của Thế Phong như những nhát búa nện thẳng vào tương lai của Phúc.",
    "Bao nhiêu nỗ lực, bao nhiêu đêm thức trắng nhịn ăn để mua sách nhạc, giờ đây đều sụp đổ chỉ trong chớp mắt.",
    "Thế Anh đi lướt qua vai Phúc, thì thầm vào tai cậu bằng giọng đầy đắc ý.",
    "\"Một đứa nghèo kiết xác như mày thì lấy tư cách gì thi quốc tế?\"",
    "\"Bản nhạc này viết rất tốt, từ nay nó sẽ giúp tao tỏa sáng tại Warsaw, còn mày thì biến đi là vừa.\"",
    "Phúc siết chặt nắm tay đến mức móng tay găm vào lòng bàn tay đau nhói, nhưng cậu không thể làm gì.",
    "Quyền lực của Nguyễn Thế Phong tại Nhạc viện này là tuyệt đối.",
    "Không một giảng viên nào dám đứng ra nói giúp cho một sinh viên nghèo không gia thế như Phúc.",
    "Cậu bị bảo vệ trục xuất khỏi phòng hòa nhạc dưới những ánh mắt đầy thương hại của một vài người và sự khinh bỉ của đa số.",
    "Bước ra khỏi cổng Nhạc viện, cái nóng hầm hập của trưa hè Sài Gòn ập vào mặt Phúc.",
    "Cậu ngước nhìn bầu trời cao rộng, cảm thấy bản thân nhỏ bé và bất lực trước bức tường quyền lực vô hình.",
    "Nhưng trong lòng cậu, ngọn lửa uất hận không hề tắt đi, mà bắt đầu cháy âm ỉ.",
    "Họ muốn cướp đi âm nhạc của cậu, muốn dìm cậu xuống bùn đen.",
    "Nhưng họ quên mất rằng, thiên tài thực sự không nằm ở tờ giấy chứng nhận bản quyền kia.",
    "Nó nằm ở đôi bàn tay này, và ở linh hồn kiên cường chưa bao giờ biết đầu hàng của cậu."
]

# Chapter 2
ch2_sentences = [
    "Trời Sài Gòn đổ cơn mưa rào lớn, nước mưa xối xả trút xuống những con đường Quận 1.",
    "Lâm Hoàng Phúc ôm chặt chiếc balô cũ kỹ trước ngực, bước đi vô định dưới làn mưa lạnh buốt.",
    "Mưa ngấm qua lớp áo sơ mi mỏng, dính sát vào da thịt, nhưng cái lạnh bên ngoài không bằng nỗi buốt giá trong tim cậu.",
    "Mọi ngả đường tương lai của cậu dường như đã bị chặn đứng hoàn toàn bởi thế lực của cha con hiệu trưởng.",
    "Cậu đi mãi, đi mãi, cho đến khi bước chân đưa cậu tới cư xá Thanh Đa cũ kỹ bên sông Sài Gòn.",
    "Nơi đây tách biệt khỏi sự ồn ào của phố thị, những dãy nhà ba tầng mang màu sơn vàng úa nhuốm màu thời gian.",
    "Phúc rẽ vào một quán cà phê nhỏ nằm nép mình dưới bóng cây bàng lớn, bảng hiệu gỗ ghi tên đơn giản: 'Ký Ức'.",
    "Quán vắng khách do trời mưa lớn, chỉ có tiếng nhạc trịnh du dương phát ra từ chiếc loa cũ ở góc phòng.",
    "Ở trung tâm quán, một cây đàn piano upright hiệu Yamaha màu đen cũ kỹ đứng lặng lẽ, nước sơn đã bong tróc vài chỗ.",
    "Chủ quán là một ông lão tóc bạc phơ đang lau ly thủy tinh sau quầy, ngước mắt nhìn Phúc đầy ái ngại.",
    "\"Cậu trẻ, vào trú mưa đi, ướt hết cả rồi kìa.\"",
    "Phúc cúi chào, tìm một góc khuất ngồi xuống, nhưng ánh mắt cậu không thể rời khỏi cây đàn cũ.",
    "Cậu bước tới trước cây đàn, khẽ hỏi chủ quán bằng giọng khàn đặc.",
    "\"Dạ bác ơi, con có thể chơi thử một bản nhạc được không ạ?\"",
    "Ông lão cười hiền từ, gật đầu: \"Cứ tự nhiên đi cậu, trời mưa thế này có tiếng đàn nghe cũng ấm lòng.\"",
    "Phúc ngồi xuống chiếc ghế gỗ tròn, khẽ đặt đôi bàn tay vẫn còn run rẩy vì lạnh lên các phím đàn sờn cũ.",
    "Cậu nhắm mắt lại, hít một hơi sâu để bình tâm, rồi bắt đầu gõ phím.",
    "Cậu không chơi bản Sonatina bị cướp đoạt kia, mà chọn bản Nocturne giọng Đô thứ của Chopin.",
    "Ngay từ những nốt nhạc đầu tiên, không gian quán cà phê như ngưng đọng lại.",
    "Tiếng đàn của Phúc không còn là những nốt nhạc vô hồn, mà là tiếng khóc nghẹn ngào, là nỗi uất hận ngút trời của một linh hồn bị tổn thương sâu sắc.",
    "Kỹ thuật legato của cậu mượt mà như nước chảy, từng nốt nhạc vang lên tròn trịa, đầy đặn dù cây đàn đã xuống tông ít nhiều.",
    "Dưới bàn tay Phúc, cây đàn cũ kỹ như được hồi sinh, phát ra những âm thanh có chiều sâu kỳ diệu.",
    "Đúng lúc đó, tiếng chuông gió ở cửa quán vang lên leng keng.",
    "Một người phụ nữ bước vào quán, tay cầm chiếc ô màu đen vẫn còn đọng những giọt nước mưa lấp lánh.",
    "Cô mặc một chiếc măng tô mỏng màu be thanh lịch, mái tóc đen dài được bới gọn gàng bằng một chiếc kẹp ngọc trai tinh tế.",
    "Khuôn mặt cô đẹp thanh tú, toát lên khí chất kiêu sa, tao nhã của một nghệ sĩ thực thụ.",
    "Đó chính là Trần Diệu Linh - nữ thần violin danh tiếng của Việt Nam, người vừa trở về từ các chuyến lưu diễn châu Âu và đang đảm nhận vai trò giám khảo cuộc thi âm nhạc quốc gia.",
    "Linh định bước vào tìm bàn ngồi, nhưng bước chân cô hoàn toàn khựng lại khi tiếng đàn piano vang lên.",
    "Đôi mắt đẹp của cô mở to đầy ngạc nhiên khi nhìn về phía góc quán, nơi một chàng trai trẻ gầy gò, quần áo ướt sũng đang độc tấu.",
    "Là một nghệ sĩ violin đẳng cấp quốc tế, Linh đã nghe vô số nghệ sĩ piano hàng đầu biểu diễn.",
    "Nhưng tiếng đàn này mang một sức hút mãnh liệt, một thứ cảm xúc chân thật đến mức chạm vào sâu thẳm tâm hồn cô.",
    "Kỹ thuật rubato vô cùng tự nhiên, cách xử lý các bè phức điệu cực kỳ thông minh mà chỉ những thiên tài thực sự mới có được.",
    "Linh đứng im lặng dưới mái hiên quán, không nỡ phá vỡ bầu không khí âm nhạc tuyệt mỹ này.",
    "Phúc hoàn toàn chìm đắm vào thế giới riêng, nốt nhạc cuối cùng kết thúc bằng một hợp âm trầm ấm, ngân dài vô tận.",
    "Cậu thở dài, buông lỏng đôi tay, những giọt nước mưa pha lẫn mồ hôi từ tóc nhỏ xuống phím đàn.",
    "Lúc này, một tiếng vỗ tay nhẹ nhàng vang lên từ phía sau.",
    "Phúc giật mình quay lại, nhìn thấy Trần Diệu Linh đang mỉm cười nhìn cậu.",
    "\"Tiếng đàn tuyệt vời lắm, cậu trẻ.\" Linh bước tới, giọng nói thanh tao như tiếng đàn violin của cô.",
    "Cô rút từ túi xách ra một chiếc khăn lụa nhỏ, nhẹ nhàng đưa cho Phúc.",
    "\"Lau mặt đi kẻo cảm lạnh, một đôi tay chơi đàn đẹp thế này không nên để bị lạnh đâu.\"",
    "Phúc bối rối nhận lấy chiếc khăn, nhận ra người phụ nữ trước mặt chính là vị giám khảo nổi tiếng mà cậu từng thấy trên tivi.",
    "\"Dạ... con cảm ơn cô Diệu Linh.\"",
    "Linh hơi nhướng mày, mỉm cười ngồi xuống chiếc ghế gỗ đối diện cây đàn.",
    "\"Cậu nhận ra tôi sao? Vậy thì chúng ta dễ nói chuyện rồi.\"",
    "\"Cậu tên là gì? Đang học ở đâu? Với kỹ thuật này, cậu chắc chắn phải là học trò xuất sắc của một giáo sư danh tiếng nào đó.\"",
    "Phúc cúi đầu, ánh mắt thoáng hiện vẻ đau đớn khó tả.",
    "\"Dạ, con tên Lâm Hoàng Phúc, là... cựu sinh viên Nhạc viện TP.HCM ạ.\"",
    "\"Cựu sinh viên?\" Linh ngạc nhiên hỏi. \"Cậu trông còn rất trẻ, đáng lẽ phải đang chuẩn bị cho kỳ thi tốt nghiệp chứ?\"",
    "Phúc cắn chặt môi đến mức rớm máu, nỗi uất ức kìm nén bấy lâu nay như muốn trào ra.",
    "Nhìn vào ánh mắt ấm áp và chân thành của Diệu Linh, Phúc quyết định kể hết mọi chuyện.",
    "Từ việc cậu dành ba năm sáng tác bản Sonatina, đến việc bị Thế Anh mượn bản thảo rồi cha con hiệu trưởng Thế Phong cướp đoạt bản quyền và cấm cậu thi tốt nghiệp lẫn thi Chopin Competition quốc tế.",
    "Linh chăm chú nghe, gương mặt cô dần trở nên nghiêm nghị, đôi lông mày thanh tú nhíu chặt lại.",
    "Sự phẫn nộ hiện rõ trong mắt cô khi nghe đến những thủ đoạn đê hèn của cha con Nguyễn Thế Phong.",
    "Là người hoạt động nghệ thuật lâu năm, cô ghét nhất là những kẻ cướp đoạt chất xám của người khác.",
    "\"Thật là quá đáng!\" Linh vỗ mạnh tay xuống bàn, giọng nói run lên vì giận dữ.",
    "\"Nguyễn Thế Phong dám dùng quyền lực để bóp nghẹt một tài năng thực sự như cậu sao?\"",
    "Cô nhìn thẳng vào mắt Phúc, đôi mắt rực sáng một sự kiên định.",
    "\"Phúc, cậu có muốn lấy lại những gì thuộc về mình không?\"",
    "\"Có muốn cho thế giới thấy ai mới là chủ nhân thực sự của bản nhạc đó không?\"",
    "Phúc ngẩng đầu lên, nhìn vị nữ thần trước mặt, ngọn lửa hy vọng trong lòng cậu bỗng chốc bùng cháy mãnh liệt.",
    "Cậu kiên quyết gật đầu: \"Con muốn! Dù có phải trả giá thế nào, con cũng không để họ chà đạp lên âm nhạc của con!\"",
    "Linh mỉm cười, một nụ cười đầy bí hiểm và quyền lực.",
    "\"Tốt lắm. Vậy thì từ nay, tôi sẽ là người bảo trợ cho cậu.\""
]

# Chapter 3
ch3_sentences = [
    "Chiều tối hôm đó, Trần Diệu Linh đưa Lâm Hoàng Phúc về căn biệt thự cổ kính của cô nằm ven sông Sài Gòn ở khu Thảo Điền, Quận 2.",
    "Ngôi nhà mang đậm phong cách kiến trúc Pháp cổ với những bức tường sơn trắng, giàn hoa giấy đỏ rực trước cổng và khoảng sân vườn rộng rãi.",
    "Bên trong phòng khách, một cây đại dương cầm Steinway & Sons màu đen bóng loáng đặt trang trọng cạnh cửa sổ lớn nhìn ra sông.",
    "Linh rót cho Phúc một tách trà gừng ấm, khuyên cậu đi tắm và thay một bộ quần áo sạch sẽ do cô chuẩn bị.",
    "Khi Phúc bước ra, cậu cảm thấy cơ thể đã ấm áp trở lại, nhưng tâm trí vẫn còn chấn động trước những gì đang diễn ra.",
    "Linh ngồi trên ghế sofa da, trên bàn trước mặt cô là chiếc máy tính xách tay đang hiển thị trang web chính thức của Chopin Competition.",
    "\"Phúc, ngồi xuống đây đi.\" Linh vẫy tay gọi cậu.",
    "Phúc đi tới ngồi đối diện cô, đón lấy tách trà ấm áp tỏa hương thơm dịu nhẹ.",
    "\"Tôi đã suy nghĩ kỹ về trường hợp của cậu.\" Linh bắt đầu nói, giọng trầm tĩnh nhưng vô cùng sắc bén.",
    "\"Nguyễn Thế Phong nghĩ rằng ông ta nắm giữ Nhạc viện thì có thể che bầu trời bằng một tay, nhưng ông ta đã lầm.\"",
    "\"Về mặt pháp lý, việc họ đăng ký bản quyền trước là một lợi thế lớn của họ, nhưng không phải là không thể lật ngược.\"",
    "\"Cậu nói cậu vẫn giữ các bản phác thảo tay và các file ghi âm quá trình sáng tác đúng không?\"",
    "Phúc gật đầu chắc chắn: \"Dạ đúng ạ, con lưu toàn bộ các bản thảo viết tay từ những ngày đầu tiên trong một chiếc hộp sắt ở phòng trọ.\"",
    "\"Ngoài ra, con còn gửi các file demo cho chính mình qua email cá nhân từ hai năm trước để lưu trữ ngày giờ cụ thể.\"",
    "Mắt Linh sáng lên, cô khẽ gật đầu đầy tán thưởng.",
    "\"Tốt lắm! Thói quen gửi email đó chính là bằng chứng vàng ròng trước pháp luật.\"",
    "\"Ngày giờ gửi trên máy chủ email của Google là thứ không ai có thể làm giả hay can thiệp được.\"",
    "\"Tôi sẽ liên hệ với Luật sư Trần Hữu Trí, một trong những chuyên gia hàng đầu về sở hữu trí tuệ tại Việt Nam để đại diện cho cậu.\"",
    "\"Chúng ta sẽ âm thầm thu thập đầy đủ chứng cứ pháp lý, chờ thời cơ chín muồi sẽ giáng cho cha con họ một đòn chí mạng.\"",
    "Phúc cảm động sâu sắc, cậu đứng dậy cúi đầu thật sâu trước Diệu Linh.",
    "\"Cô Diệu Linh, con thực sự không biết phải cảm ơn cô thế nào.\"",
    "\"Nếu không có cô, con... con thực sự đã nghĩ đến việc bỏ cuộc.\"",
    "Linh đứng dậy, nhẹ nhàng đỡ vai Phúc đứng thẳng lên.",
    "\"Đừng cảm ơn tôi, hãy cảm ơn tài năng của chính cậu.\"",
    "\"Tôi giúp cậu không chỉ vì công lý, mà vì tôi không muốn giới âm nhạc nước nhà mất đi một thiên tài thực sự.\"",
    "Cô đi tới bên cây đàn Steinway, khẽ lướt tay trên nắp đàn gỗ quý.",
    "\"Nhưng lấy lại bản quyền chỉ là bước đầu tiên để vạch mặt họ.\"",
    "\"Để hủy diệt hoàn toàn sự kiêu ngạo của cha con Nguyễn Thế Phong, cậu phải đứng ở một tầm cao mà họ không bao giờ với tới được.\"",
    "\"Ý cô là... cuộc thi Chopin quốc tế?\" Phúc khẽ hỏi, tim đập nhanh liên hồi.",
    "\"Đúng vậy!\" Linh quay lại nhìn cậu, ánh mắt rực sáng kiên định.",
    "\"Nguyễn Thế Phong cấm cậu thi tốt nghiệp, tước quyền cử đi thi của Nhạc viện, nhưng ông ta không có quyền cấm cậu thi tự do.\"",
    "\"Ban tổ chức Chopin Competition tại Warsaw cho phép các thí sinh tự do nộp đơn đăng ký trực tiếp nếu có thư giới thiệu từ các nghệ sĩ uy tín quốc tế.\"",
    "\"Tôi sẽ viết thư giới thiệu cho cậu với tư cách là nghệ sĩ violin danh tiếng thế giới.\"",
    "\"Đồng thời, tôi sẽ gửi bản thu âm tiếng đàn của cậu tối nay cho Giáo sư Janusz Olejniczak, giám khảo kỳ cựu của Chopin Competition tại Warsaw.\"",
    "\"Tôi tin chắc rằng, sau khi nghe tiếng đàn của cậu, giáo sư sẽ không ngần ngại đồng ký tên vào thư giới thiệu này.\"",
    "Nghe đến đây, Phúc cảm thấy toàn thân như có một luồng điện chạy qua, các đầu ngón tay run lên vì phấn khích.",
    "Cơ hội thi Chopin quốc tế - ước mơ lớn nhất đời cậu, tưởng chừng đã tắt ngấm, giờ đây lại mở ra rộng lớn hơn bao giờ hết.",
    "\"Con... con có thể thi tự do sao?\" Phúc lắp bắp hỏi.",
    "\"Đúng vậy, và chúng ta sẽ làm điều đó hoàn toàn bí mật.\" Linh mỉm cười đầy mưu mô.",
    "\"Hãy để cha con Nguyễn Thế Phong đắc ý biểu diễn bản nhạc cướp đoạt của cậu tại Việt Nam.\"",
    "\"Hãy để Nguyễn Thế Anh huênh hoang chuẩn bị đi Warsaw.\"",
    "\"Và rồi, khi danh sách thí sinh chính thức của Chopin Competition được công bố toàn cầu, tên của Lâm Hoàng Phúc sẽ xuất hiện bên cạnh thư giới thiệu của các huyền thoại âm nhạc.\"",
    "\"Đó mới là cái tát đau đớn nhất dành cho sự ngạo mạn của họ.\"",
    "Phúc nhìn Diệu Linh, sự ngưỡng mộ và lòng biết ơn trong lòng cậu dâng trào.",
    "Cậu bước tới bên cây đàn Steinway, ngồi xuống ghế đàn đầy tự tin.",
    "\"Cô Diệu Linh, con muốn chơi lại bản Sonatina đó cho cô nghe.\"",
    "\"Bản Sonatina thực sự của Lâm Hoàng Phúc, chứ không phải bản sao chép vô hồn của Nguyễn Thế Anh.\"",
    "Linh tựa lưng vào thành đàn, khẽ gật đầu: \"Tôi rất vinh hạnh được thưởng thức.\"",
    "Dưới ánh đèn vàng ấm áp của phòng khách biệt thự Thảo Điền, tiếng đàn piano của Phúc lại vang lên.",
    "Tiếng đàn lần này không còn nỗi uất hận cô độc của buổi trưa mưa gió ở cư xá Thanh Đa.",
    "Nó mang theo một niềm hy vọng mãnh liệt, một sức mạnh tái sinh mạnh mẽ như phượng hoàng hồi sinh từ đống tro tàn.",
    "Diệu Linh đứng bên cạnh khẽ nhắm mắt, lắng nghe từng hòa âm tuyệt mỹ vang vọng ra mặt sông Sài Gòn lộng gió ngoài kia.",
    "Cô biết, một huyền thoại mới của nền piano thế giới đang bắt đầu thành hình ngay tại căn phòng này."
]

def format_chapter(title, sentences):
    content = ""
    for s in sentences:
        content += f"<p>{s}</p>\\n"
    # Remove the last \\n
    if content.endswith("\\n"):
        content = content[:-2]
    return {
        "title": title,
        "content": content
    }

novel_data["chapters"].append(format_chapter("Chương 1: Bản Nhạc Bị Đánh Cắp", ch1_sentences))
novel_data["chapters"].append(format_chapter("Chương 2: Cuộc Gặp Gỡ Dưới Mưa Sài Gòn", ch2_sentences))
novel_data["chapters"].append(format_chapter("Chương 3: Kế Hoạch Phản Công", ch3_sentences))

# Write to temp file
temp_file_path = "/Users/aaronnguyen/TN/App/doctieuthuyet/pending_novel_9_temp.json"
with open(temp_file_path, "w", encoding="utf-8") as f:
    json.dump(novel_data, f, ensure_ascii=False, indent=2)

print("Stage 1 completed successfully. Written 3 chapters to temp file.")
