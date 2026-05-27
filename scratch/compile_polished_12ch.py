import json
import os

def main():
    print("🚀 COMPILING PREMIUM 12-CHAPTER NOVEL - V13 GOLD STANDARD")
    
    # 1. Load the first 8 chapters generated successfully by Qwen
    progress_file = "scratch/story_3940_12ch_progress.json"
    if not os.path.exists(progress_file):
        print("❌ Progress file not found! Make sure Qwen generated the first 8 chapters.")
        return
        
    with open(progress_file, "r", encoding="utf-8") as f:
        chapters = json.load(f)
        
    print(f"✓ Successfully loaded {len(chapters)} chapters from Qwen.")
    
    # 2. Write Chapter 9: Nhịp Đập Trí Tuệ Dưới Trăng Hồ Tây (poetic, deep emotion, no clichés)
    c9_content = """<p>Đêm muộn trước ngày diễn ra Hội thảo Y học Hô hấp Quốc gia chấn động giới y khoa, một làn sương thu mờ ảo và bảng lảng bao phủ khắp mặt nước hồ Tây tĩnh mịch rộng lớn.</p>
<p>Căn văn phòng làm việc cao cấp của Trịnh Khánh Vy trên tầng hai mươi của tòa tháp Vạn An Plaza ngập tràn ánh sáng dịu mát từ chiếc đèn bàn cổ kính.</p>
<p>Từ ô cửa kính sát trần lớn kéo dài từ sàn lên trần nhà, có thể phóng tầm mắt ngắm trọn vẹn cảnh đêm lung linh rực rỡ của thủ đô Hà Nội với cầu Nhật Tân lấp lánh ánh đèn ngũ sắc phía chân trời xa.</p>
<p>Bầu không khí yên bình, tĩnh lặng đến lạ kỳ, hoàn toàn tách biệt khỏi những cơn bão truyền thông bẩn đang gào thét không ngừng ngoài kia.</p>
<p>Tiếng gió thu khẽ lùa qua khe cửa, mang theo hơi lạnh thanh khiết và dịu mát của mặt nước hồ Tây.</p>
<p>Mùi hương ngọc lan thoang thoảng dịu nhẹ từ vườn hoa phía dưới bay lên tạo nên một không gian vô cùng thư thái, nhẹ nhõm.</p>
<p>Trịnh Khánh Vy mặc chiếc áo len mỏng màu tơ tằm thanh lịch, rũ bỏ hoàn toàn vẻ lãnh đạm, cứng nhắc của một nữ chủ tịch uy quyền thường ngày trên thương trường.</p>
<p>Cô khẽ bước lại gần chiếc bàn pha trà bằng gỗ trắc, cẩn thận rót hai chén trà sen Tây Hồ tỏa hương thơm thuần khiết, ấm sực.</p>
<p>Cô đưa một chén trà cho Nguyễn Lâm Phong rồi khẽ ngồi xuống chiếc ghế bành đối diện anh, đôi mắt thông tuệ nhìn thẳng vào mắt người đàn ông đã cứu sống cha mình.</p>
<p>"Anh Phong, anh có biết tại sao một người cực kỳ sắc sảo, chỉ làm việc bằng số liệu và hợp đồng pháp lý minh bạch như tôi lại sẵn sàng đặt cược toàn bộ danh tiếng của gia tộc và năm trăm tỷ đồng vào anh không?" Vy khẽ hỏi, giọng nói trầm ấm, dịu dàng vô cùng mà chưa từng một nhân viên nào của Vạn An được nghe thấy.</p>
<p>Phong khẽ nâng chén trà, nhấp một ngụm nhỏ cảm nhận vị chát dịu rồi ngọt hậu lan tỏa nơi đầu lưỡi, anh lắc đầu mỉm cười điềm tĩnh.</p>
<p>"Tôi nghĩ là vì kết quả kiểm tra lâm sàng của cha em quá thuyết phục, và vì tiềm năng thương mại của Phế Đan Sâm Đá trên bản đồ y học toàn cầu."</p>
<p>Vy khẽ cười nhạt, một nụ cười hiếm hoi nhưng vô cùng rạng rỡ, làm xua tan đi hoàn toàn bầu không khí căng thẳng của căn phòng.</p>
<p>"Đó chỉ là những con số thực tế trên bàn đàm phán của một CFO thông thường."</p>
<p>"Sự thật là... tôi đã quá mệt mỏi với thế giới kinh doanh giả dối băng giá này rồi."</p>
<p>"Mẹ tôi mất sớm vì căn bệnh suy hô hấp cấp tính mười năm trước, khi đó y học Tây y bó tay, tôi đã bất lực đứng nhìn bà ra đi trong đau đớn khôn cùng."</p>
<p>"Cha tôi đã nuôi dạy tôi vô cùng nghiêm khắc, dạy tôi cách giấu kín cảm xúc đằng sau những con số vô cảm để bảo vệ bản thân và gia tộc khỏi những kẻ dối trá ngoài kia."</p>
<p>"Nhưng càng lên cao, tôi càng thấy nhiều kẻ như Lê Hữu Hoài và Trần Quốc Dũng, dùng y học làm công cụ để vơ vét tiền bạc, chà đạp lên sinh mạng bệnh nhân nghèo."</p>
<p>"Khi nhìn thấy anh bất chấp sự ngăn cản của tất cả mọi người, điềm tĩnh dùng bộ Cửu Châm và viên thuốc Phế Đan cứu sống cha tôi khỏi ranh giới tử thần bằng một y đức thuần khiết nhất... tôi biết mình đã tìm thấy người đồng hành thực sự của cuộc đời mình."</p>
<p>Vy dừng lại, đôi mắt cô khẽ lay động dưới ánh đèn bàn ấm áp, gương mặt kiêu hãnh của cô thoáng chút yếu đuối nữ tính hiếm hoi.</p>
<p>Phong lặng người đi vì xúc động sâu sắc, anh đặt chén trà xuống bàn, từ từ tiến lại gần cô.</p>
<p>Anh đưa bàn tay mạnh mẽ, ấm áp và tràn đầy sinh lực của mình nhẹ nhàng nắm lấy bàn tay thon nhỏ đang khẽ run lên của Vy.</p>
<p>Xúc giác cực kỳ nhạy bén từ mười đầu ngón tay của Phong cảm nhận rõ ràng nhịp đập thổn thức từ mạch đập của cô.</p>
<p>Anh cảm thấy cái lạnh từ đôi tay Vy dần được xua tan bởi hơi ấm từ lòng bàn tay mình.</p>
<p>"Khánh Vy, em đã gánh vác quá nhiều áp lực của gia tộc trên đôi vai mảnh mai này rồi," Phong nói vô cùng ấm áp, kiên định.</p>
<p>"Y đức của tôi là giữ mạng cho người bệnh, và từ nay về sau, tôi cũng sẽ dùng bộ kim châm cứu và cả cuộc đời này của mình để bảo vệ sự trong sạch, kiêu hãnh của em trước mọi sóng gió cuộc đời."</p>
<p>"Ngày mai, tôi sẽ cùng em ra trận và quét sạch lũ sâu mọt kia khỏi ngành y."</p>
<p>Họ ký kết một bản thỏa thuận bổ sung đặc biệt đầy ấm áp và phân minh.</p>
<p>Bản hợp đồng ghi nhận quyền sở hữu trí tuệ vĩnh viễn thuộc về Phong, trong khi Vạn An chịu trách nhiệm thương mại hóa toàn cầu với tỷ lệ lợi nhuận chia sẻ 50-50 phân minh.</p>
<p>Đây không chỉ là sự hợp tác kinh doanh thông thường, mà còn là lời thề ước đan xen giữa tình yêu và trí tuệ của hai con người xuất chúng nhất.</p>
<p>Dưới ánh trăng khuyết treo lơ lửng ngoài khung cửa sổ của tòa tháp cao tầng giữa lòng Hà Nội, hai tâm hồn kiêu hãnh và trí tuệ đã thực sự hòa chung một nhịp đập, sẵn sàng đương đầu với trận chiến phán quyết sinh tử vào ngày mai.</p>"""

    # 3. Write Chapter 10: Biến Cố Phế Huyết Tại Hội Thảo Quốc Gia (intense, dramatic medical failure of Nexa-09)
    c10_content = """<p>Trung tâm Hội nghị Quốc gia Hà Nội chiều hôm đó rực rỡ dưới hàng ngàn ánh đèn LED công suất lớn vô cùng tráng lệ.</p>
<p>Hội thảo Y học Hô hấp Quốc gia thường niên quy tụ hơn một ngàn giáo sư, tiến sĩ y khoa hàng đầu cả nước, cùng đại diện các quỹ đầu tư y tế quốc tế lớn đến từ Mỹ, Pháp, Singapore và hàng trăm cơ quan báo chí truyền hình lớn nhỏ.</p>
<p>Bầu không khí vô cùng sôi động, hào ngoáng và ngập tràn mùi tiền bạc của giới thượng lưu y dược quốc tế.</p>
<p>Các giáo sư danh tiếng thuộc Viện Hàn lâm Y khoa Pháp và Ủy ban Y tế Singapore đang chăm chú trao đổi số liệu lâm sàng tại các hàng ghế danh dự.</p>
<p>Ánh đèn máy ảnh liên tục chớp nháy tạo nên không gian hào ngoáng tột bực.</p>
<p>Tại bục diễn thuyết trung tâm được trang trí lộng lẫy nhất, Viện Phổi Quốc tế Việt - Đức chiếm trọn tiêu điểm truyền thông.</p>
<p>Viện trưởng Lê Hữu Hoài mặc bộ comple gấm hoa sang trọng, cùng Phan Mỹ Hạnh và Trần Quốc Dũng đứng đón tiếp các vị khách VIP với nụ cười đắc thắng tột bực hiện rõ trên khuôn mặt kiêu ngạo.</p>
<p>Phía sau họ, màn hình LED khổng lồ hiển thị dòng chữ lớn rực rỡ: "Lễ Công Bố Siêu Phẩm Biệt Dược Nexa-09 - Bước Đột Phá Hồi Sinh Kẽ Phổi Toàn Cầu, Định Giá IPO 1 Tỷ USD".</p>
<p>Lê Hữu Hoài tự mãn bước lên bục diễn thuyết chính.</p>
<p>Dưới khán đài, các đại diện quỹ đầu tư quốc tế từ Wall Street liên tục đặt câu hỏi chất vấn về độ an toàn lâm sàng và nguy cơ xơ hóa kẽ phổi của Nexa-09.</p>
<p>Thế nhưng, Lê Hữu Hoài với thái độ kiêu ngạo đỉnh điểm đã gạt phăng mọi nghi ngờ.</p>
<p>"Chúng tôi là cơ quan y khoa quốc tế đầu ngành. Mọi kết quả kiểm chứng của chúng tôi đều đạt chuẩn tuyệt đối. Những tin đồn thất thiệt ngoài kia chỉ là sự ghen ghét đố kỵ của những kẻ Đông y lạc hậu, không có chuyên môn khoa học hiện đại!"</p>
<p>Trần Quốc Dũng dưới khán đài gật đầu đắc ý, thầm mừng vì kế hoạch bịt miệng công luận đã diễn ra vô cùng suôn sẻ.</p>
<p>"Nexa-09 là công trình nghiên cứu độc quyền vĩ đại nhất của Viện Phổi Việt - Đức phối hợp cùng tập đoàn đa quốc gia NexaCorp, mở ra kỷ nguyên mới làm mềm hóa sợi phế nang cho bệnh nhân hô hấp toàn cầu," Lê Hữu Hoài dõng dạc diễn thuyết đầy tự mãn trên bục danh dự trước hàng trăm ống kính phóng viên truyền hình trực tiếp.</p>
<p>Để minh chứng cho sự hiệu quả kỳ diệu của siêu phẩm biệt dược, Trần Quốc Dũng đã cho mời năm bệnh nhân nghèo bị xơ hóa kẽ phổi tiến triển - những người đã được dùng thử Nexa-09 miễn phí suốt hai tuần qua - bước lên khán đài để chia sẻ cảm nhận thực tế trước toàn thể hội trường.</p>
<p>Bọn chúng muốn dùng màn kịch lâm sàng dàn dựng này để đập tan mọi tin đồn bôi nhọ của dư luận về tác dụng phụ của thuốc hóa chất công nghiệp độc hại.</p>
<p>Thế nhưng, ngay khi năm bệnh nhân vừa bước lên bục phát biểu, một biến cố kinh hoàng đột ngột xảy ra ngoài tầm kiểm soát của ban tổ chức.</p>
<p>Một bệnh nhân nam 50 tuổi đột nhiên ho sặc sụa kịch liệt, lồng ngực co thắt dữ dội, tiếng thở rít khò khè đứt quãng vang vọng qua micro khắp cả hội trường rộng lớn.</p>
<p>Chỉ trong vài giây ngắn ngủi, bốn bệnh nhân còn lại cũng đồng loạt đổ gục xuống sàn sân khấu, cơ thể co giật kịch liệt, hai tay bóp chặt lấy cổ họng trong trạng thái ngạt thở vô cùng đau đớn.</p>
<p>Chỉ số SpO2 trên máy đo ngón tay của họ sụt giảm thê thảm xuống dưới 55% cấp cứu nguy kịch.</p>
<p>Tiếng rales nổ, rales ẩm từ hai đáy phổi của họ vang lên rõ rệt qua hệ thống âm thanh, báo hiệu phổi đang bị đông đặc hoàn toàn vì dịch huyết.</p>
<p>Dưới góc độ sinh lý học cấp cứu, nang phổi của họ đang trải qua quá trình xẹp phế nang hàng loạt do sự tích tụ chất hoạt diện dị thường của Nexa-09.</p>
<p>Sự rò rỉ huyết tương vào phế nang diễn ra với tốc độ khủng khiếp, làm bít tắc hoàn toàn diện tích trao đổi khí.</p>
<p>Bệnh nhân rơi vào trạng thái ngạt thở cơ học giống như đang bị chìm sâu dưới nước.</p>
<p>Các giáo sư hô hấp quốc tế lập tức bật dậy khỏi ghế ngồi trong sự hãi hùng tột bực, liên tục hét lên yêu cầu mở lối đi cấp cứu khẩn cấp.</p>
<p>"Máu! Họ đang ho ra máu kìa!"</p>
<p>Tiếng hét thất thanh của một nữ phóng viên vang lên khiến toàn thể hội trường bùng nổ sự hỗn loạn kinh hoàng.</p>
<p>Từ miệng năm bệnh nhân, những dòng máu đen đặc, tanh tưởi trào ra xối xả ướt đẫm sàn gạch sân khấu rực rỡ.</p>
<p>Sắc mặt họ xám ngoét không còn một giọt máu, mồ hôi lạnh chảy ròng ròng ướt sũng cơ thể, ngón tay họ cào bấu rỉ máu trên nền sân khấu vì khó thở tột bực.</p>
<p>Đây chính là biến chứng đông đặc phế nang cấp tính do độc chất tích tụ của Nexa-09 khi thiếu đi chất xúc tác sâm đá tự nhiên.</p>
<p>Lê Hữu Hoài hoảng loạn tột bực, sắc mặt ông ta xám ngoét như tro tàn, hai chân bủn rủn run rẩy dữ dội rồi quỳ sụp hẳn hai đầu gối xuống sàn sân khấu lạnh lẽo, mồ hôi lạnh tuôn ra như tắm ướt đẫm cả tấm lưng áo comple đắt tiền.</p>
<p>Ông ta gào lên điên cuồng ra lệnh cho các bác sĩ cấp cứu Tây y lập tức tiêm thuốc giãn phế quản liều cao và thở oxy liều tối đa.</p>
<p>Thế nhưng, mọi biện pháp can thiệp Tây y hiện đại lúc này đều hoàn toàn vô hiệu, vùng phổi kẽ bị xơ cứng đông đặc của bệnh nhân đã hoàn toàn mất đi chức năng trao đổi khí, kim tiêm rơi loảng xoảng trên sàn nhà.</p>
<p>Trần Quốc Dũng và Phan Mỹ Hạnh đứng bên cạnh đờ đẫn cả người, run rẩy bần bật trước hàng trăm ống kính máy quay đang truyền hình trực tiếp thảm họa y tế này ra toàn thế giới.</p>"""

    # 4. Write Chapter 11: Sự Lựa Chọn Của Thần Y (moral choice, Cửu Châm, dynamic, no clichés)
    c11_content = """<p>Giữa lúc cả hội trường lớn của Trung tâm Hội nghị Quốc gia đang chìm trong sự hỗn loạn, hoảng sợ tột bực và tiếng la hét thất thanh của đám đông, cánh cửa sảnh chính bất ngờ mở toang.</p>
<p>Nguyễn Lâm Phong khoác trên mình chiếc áo blouse trắng tinh khôi, hiên ngang sải bước vào phòng hội thảo với phong thái điềm tĩnh, tự tại như một vị thần y giáng thế.</p>
<p>Đi bên cạnh anh là Trịnh Khánh Vy, kiêu sa, lộng lẫy và vô cùng đanh thép, theo sau là đoàn thanh tra đặc biệt của Bộ Y tế và các chiến sĩ cảnh sát thuộc cơ quan C03 Bộ Công an với sắc lệnh đóng dấu đỏ chói lọi.</p>
<p>"Tránh ra! Để tôi cứu người!" Giọng nói của Phong vang lên vang dội, trầm ấm nhưng chứa đựng một uy lực kiên định khiến đám đông đang hỗn loạn lập tức tự động giãn ra một lối đi rộng lớn.</p>
<p>Phong thần tốc bước lên sân khấu chính, không hề ngần ngại vết máu đen tanh tưởi bám đầy sàn nhà, anh quỳ xuống bên cạnh bệnh nhân đang co giật mạnh nhất.</p>
<p>Lúc này, Phong đứng trước một sự lựa chọn đạo đức lớn lao: công bố ngay bằng chứng hạ gục đối thủ, hay cứu sống những con người đang hấp hối trước?</p>
<p>Không một giây do dự, y đức tối thượng của người thầy thuốc đã đưa ra câu trả lời dứt khoát.</p>
<p>"Cứu người quan trọng hơn tất cả," Phong thầm nghĩ, đôi bàn tay nhạy cảm phục hồi hoàn hảo chuyển động nhanh như chớp.</p>
<p>Anh lấy ra chín cây kim châm cứu vàng ròng "Cửu Châm Đoạt Mệnh", chuẩn xác tuyệt đối đâm sâu vào các huyệt đạo Đại Chùy, Đàn Trung, Phế Du của bệnh nhân để khai thông kinh mạch phổi đang bị bít tắc hoàn toàn.</p>
<p>Đồng thời, Phong nhanh chóng lấy từ trong túi áo ra một lọ dịch chiết xuất từ "Phế Đan Sâm Đá", nhỏ trực tiếp vài giọt vào miệng từng bệnh nhân.</p>
<p>Anh tiếp tục thực hiện châm kim vàng vào các huyệt Thiên Đột và Xích Trạch trên cánh tay để kích thích hệ bạch huyết và làm mềm các cơ phế quản của phổi.</p>
<p>Sự kết hợp nhuần nhuyễn giữa bí thuật châm cứu cổ truyền và dịch chất sinh học của Sâm Đá cổ thụ Phú Thọ đã nhanh chóng cắt đứt chuỗi phản ứng viêm hóa chất, trung hòa hoàn toàn kết tủa polymer độc hại có trong Nexa-09.</p>
<p>"Nhịp tim bệnh nhân đang ổn định trở lại! SpO2 bắt đầu tăng!" Một bác sĩ trẻ bên dưới run rẩy hét lên khi nhìn vào màn hình máy đo.</p>
<p>"Ý anh là... mũi kim vàng đó thực sự giải trừ được kết tủa chất độc hóa học sao?" Một vị giáo sư hô hấp quốc tế thốt lên đầy sửng sốt.</p>
<p>"Nó không chỉ giải độc," Phong điềm tĩnh đáp trong khi tay vẫn đi kim thoăn thoắt. "Nó đang kích hoạt cơ chế tự phục hồi phế nang của cơ thể. Phổi họ sẽ không còn bị đông đặc nữa."</p>
<p>Chỉ trong vòng chưa đầy ba phút ngắn ngủi, một phép màu y học kỳ diệu đã diễn ra trước sự chứng kiến trực tiếp của hơn một ngàn giáo sư hô hấp và hàng triệu khán giả đang xem trực tiếp.</p>
<p>Cơn ho ra máu đen kịch liệt của cả năm bệnh nhân lập tức ngừng hẳn.</p>
<p>Tiếng thở rít co thắt phế quản dịu đi rõ rệt, lồng ngực bắt đầu nhịp nhàng hô hấp sâu trở lại.</p>
<p>Các chỉ số SpO2 trên máy giám sát liên tục nhảy vọt từ 55% nguy kịch lên 90%, rồi 95% cực kỳ an toàn.</p>
<p>Cả năm bệnh nhân dần tỉnh táo, da dẻ hồng hào trở lại, họ xúc động khóc nghẹn nắm chặt tay Phong cảm ơn cứu mạng.</p>
<p>Cả hội trường lớn lặng đi trong giây lát, rồi bùng nổ những tràng pháo tay vang dội như sấm truyền vinh danh vị thần y đích thực của Đông Tây y kết hợp.</p>"""

    # 5. Write Chapter 12: Phán Quyết Cuối Cùng (climax, arrest of villains, Phan My Hanh's muộn màng hối hận)
    c12_content = """<p>Khi sinh mạng của các bệnh nhân đã hoàn toàn vượt qua lưỡi hái tử thần, Trịnh Khánh Vy bước lên bục diễn thuyết chính, cầm lấy micro dõng dạc tuyên bố trước toàn bộ giới truyền thông quốc tế.</p>
<p>"Kính thưa quý vị, biệt dược Nexa-09 của Viện Phổi thực chất là một sản phẩm lỗi, được ăn cắp trắng trợn từ công trình nghiên cứu thô của bác sĩ Nguyễn Lâm Phong nhưng bị Lê Hữu Hoài cắt xén hoạt chất sâm đá chống đông máu tự nhiên để trục lợi bất chính, gây ra thảm họa lâm sàng ngày hôm nay."</p>
<p>"Chúng tôi có đầy đủ bằng chứng vật lý độc bản: Bản gốc nhật ký commit Git của hệ thống máy chủ nội bộ với mã băm bảo mật không thể giả mạo chứng minh quyền tác giả tối cao của Phong; Bằng sáng chế độc quyền quốc tế do Cục Sở hữu trí tuệ cấp; và Báo cáo kiểm toán Big 4 đóng dấu đỏ của EY vạch trần dòng tiền hối lộ hai triệu USD từ NexaCorp chuyển vào tài khoản cá nhân của Lê Hữu Hoài tại Thụy Sĩ!"</p>
<p>Màn hình LED lớn rực sáng lên, hiển thị chi tiết toàn bộ các chứng từ kiểm toán, nhật ký commit Git và đoạn video ghi âm ẩn cảnh Lê Hữu Hoài nhận tiền đút lót vô cùng rõ ràng.</p>
<p>Kẻ cướp công trình hoàn toàn bị lột trần bộ mặt thật xảo quyệt trước pháp luật và toàn thể công luận quốc tế.</p>
<p>Đại diện cơ quan C03 Bộ Công an bước lên sân khấu, dõng dạc đọc to sắc lệnh đóng dấu đỏ.</p>
<p>"Đọc lệnh bắt giữ khẩn cấp đối với Lê Hữu Hoài - Viện trưởng Viện Phổi và Trần Quốc Dũng - Giám đốc NexaCorp về tội Đưa - Nhận hối lộ quy mô lớn và Vi phạm quy định về khám chữa bệnh gây hậu quả nghiêm trọng theo Điều 364 và Điều 315 Bộ luật Hình sự Việt Nam!"</p>
<p>Hai gã cảnh sát nhanh chóng tiến lên, khóa chặt tay hai kẻ phản bội bằng còng số tám lạnh lẽo.</p>
<p>Phan Mỹ Hạnh đứng bên cạnh chứng kiến cảnh tượng đế chế sụp đổ hoàn toàn trong tích tắc, cô ta hoảng loạn, sợ hãi khôn tả.</p>
<p>Mỹ Hạnh quỳ sụp hẳn xuống sàn sân khấu lạnh buốt dưới chân Nguyễn Lâm Phong, khóc lóc thảm thiết, hai bàn tay run rẩy cào bấu chặt lấy nền gạch đá rỉ cả máu ra đầu ngón tay đầy hối hận muộn màng.</p>
<p>"Phong ơi, em sai rồi! Xin anh hãy cứu lấy gia đình em, cứu lấy em! Hãy nhìn vào tình nghĩa sáu năm qua của chúng ta..."</p>
<p>Nguyễn Lâm Phong nhìn Phan Mỹ Hạnh bằng ánh mắt lãnh đạm, hờ hững không có lấy một chút gợn sóng cảm xúc.</p>
<p>Anh quay lưng bước đi đầy kiêu hãnh, bàn tay mạnh mẽ của anh đan chặt lấy bàn tay thon mềm của Trịnh Khánh Vy.</p>
<p>Họ cùng nhau bước đi giữa tiếng vỗ tay rền vang của toàn thể hội trường, vương giả quy lai mở ra một chương mới rực rỡ cho nền y học nước nhà.</p>
<p>Viện nghiên cứu Đông Tây y kết hợp Phong An chính thức được thành lập từ đống tro tàn, đánh dấu sự lên ngôi của nền y học y đức và công lý tối thượng.</p>"""

    # Append these 4 chapters to our chapters list
    chapters.append({
        "title": "Chương 9: Nhịp Đập Trí Tuệ Dưới Trăng Hồ Tây",
        "content": c9_content
    })
    chapters.append({
        "title": "Chương 10: Biến Cố Phế Huyết Tại Hội Thảo Quốc Gia",
        "content": c10_content
    })
    chapters.append({
        "title": "Chương 11: Sự Lựa Chọn Của Thần Y",
        "content": c11_content
    })
    chapters.append({
        "title": "Chương 12: Phán Quyết Cuối Cùng",
        "content": c12_content
    })

    # Validate that we have exactly 12 chapters
    print(f"✓ All chapters compiled. Total chapters: {len(chapters)}")
    for idx, ch in enumerate(chapters):
        print(f"  {idx+1}. {ch['title']} ({len(ch['content'].split())} words)")

    # 6. Beautiful, polished V13 Intro using the suggested title
    intro_html = """<p><strong>"Cút khỏi Viện Phổi Quốc tế ngay lập tức! Loại bác sĩ Đông y quèn chỉ biết bốc lá cây và châm cứu rác rưởi như mày không xứng đáng đứng chung hàng ngũ với chúng tao!"</strong></p>
<p>Lời mắng chửi tàn nhẫn của Lê Hữu Hoài - Viện trưởng Viện Phổi Quốc tế Việt - Đức - như một nhát búa đập tan năm năm cống hiến thầm lặng của Nguyễn Lâm Phong. Cứu hàng ngàn bệnh nhân và âm thầm nghiên cứu công thức giải độc phế nang đột phá, nhưng thứ Phong nhận lại chỉ là sự phản bội tàn nhẫn từ người thầy kính trọng và vị hôn thê Phan Mỹ Hạnh, kẻ sẵn sàng từ bỏ hôn ước để chạy theo Trần Quốc Dũng, Giám đốc điều hành của tập đoàn hóa chất dược phẩm đa quốc gia NexaCorp.</p>
<p>Bị vu oan ăn cắp vật tư y tế và bị tống cổ khỏi bệnh viện dưới cơn mưa giông tầm tã của Hà Nội, Phong ngỡ như mất tất cả. Thế nhưng, cơ duyên đưa anh gặp Trịnh Khánh Vy, nữ Chủ tịch điều hành vô cùng nhạy bén và sắc sảo của Tập đoàn Y tế Vạn An. Bằng sự kết hợp kỳ diệu giữa bí thuật châm cứu "Cửu Châm Đoạt Mệnh" và các xét nghiệm lâm sàng Tây y hiện đại, Phong cứu sống siêu tỷ phú Trịnh Vạn An khỏi ranh giới sinh tử, chứng minh hiệu quả thần kỳ của phương thuốc cổ truyền. Cùng nhau, họ vượt qua đòn bẩn phong tỏa 24 giờ, dùng bản gốc nhật ký commit Git, bằng sáng chế quốc tế độc quyền, báo cáo kiểm toán Big 4 của EY và lệnh bắt giữ khẩn cấp từ cơ quan C03 Bộ Công an để đè bẹp tập đoàn phản bội, bắt những kẻ kiêu ngạo phải tự quỳ gối đền tội dưới chân mình.</p>"""

    # 7. Format final payload
    final_payload = {
        "story_id": 3940,
        "title": "Họ Gọi Tôi Là Lang Băm, Đến Khi Cả Hội Thảo Quỳ Xin Tôi Cứu Mạng",
        "intro": intro_html,
        "chapters": chapters,
        "seo": {
            "focus_keyword": "Họ Gọi Tôi Là Lang Băm",
            "seo_title": "Họ Gọi Tôi Là Lang Băm, Hội Thảo Quỳ Xin Tôi Cứu Mạng",
            "seo_description": "Nguyễn Lâm Phong dùng Cửu Châm Đoạt Mệnh và Sâm Đá hồi sinh kẽ phổi, vạch trần âm mưu ăn cắp công trình của Viện trưởng Lê Hữu Hoài."
        }
    }

    # 8. Save deployment JSON
    with open("scratch/story_3940_deploy_ready.json", "w", encoding="utf-8") as f:
        json.dump(final_payload, f, indent=4, ensure_ascii=False)
        
    print("🎉 SUCCESS! Final compiled 12-chapter payload saved to scratch/story_3940_deploy_ready.json")

if __name__ == "__main__":
    main()
