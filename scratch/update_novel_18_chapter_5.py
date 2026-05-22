import json

path = "/Users/aaronnguyen/TN/App/doctieuthuyet/scratch/draft_novel_18.json"
with open(path, "r", encoding="utf-8") as f:
    data = json.load(f)

# Update chapter 5 content
chapter_5_content = """<p>Dưới hàng chục luồng ánh sáng spotlight rực rỡ quét qua, Bùi Anh Tuấn từ từ bước ra khỏi góc tối của sảnh tiệc Grand Ballroom khách sạn JW Marriott.</p>
<p>Anh thong thả cởi bỏ chiếc áo khoác kaki màu xám tro lấm lem bụi đất của công trường thầu phụ và quẳng nhẹ nó xuống nền sàn đá cẩm thạch xám xịt.</p>
<p>Lộ ra bên trong là bộ tuxedo màu xanh navy may đo thủ công tinh xảo của nhà mốt nổi tiếng Savile Row ôm sát thân hình chuẩn mực, cao ráo của anh.</p>
<p>Trên ngực áo của anh lấp lánh chiếc ghim cài hình chim phượng hoàng bằng vàng trắng dát kim cương tự nhiên cực kỳ quý hiếm và sang trọng.</p>
<p>Đó chính là biểu tượng quyền lực tối cao dành riêng cho người sáng lập kiêm Chủ tịch ẩn danh tối cao của tập đoàn Vạn Xuân Group.</p>
<p>Hàng trăm quan khách thượng lưu đồng loạt né sang hai bên nhường lối, những tiếng xầm xì kinh ngạc vang lên như sóng triều vỗ bờ cát.</p>
<p>Bùi Anh Tuấn đĩnh đạc bước đi trên tấm thảm đỏ sang trọng hướng thẳng về phía sân khấu lớn rực rỡ ánh đèn pha lê dát vàng của sảnh tiệc.</p>
<p>Đi dọc hai bên thảm đỏ, toàn bộ ban quản trị cấp cao và đội ngũ vệ sĩ của Vạn Xuân Group đồng loạt nghiêm cẩn cúi gập người chín mươi độ chào đón.</p>
<p>Trần Quang Hải đứng trên sân khấu nhìn thấy gương mặt quen thuộc của Tuấn, đôi mắt gã trợn ngược kinh hoàng như nhìn thấy ác quỷ hiện hình.</p>
<p>Hai gối của Hải bủn rủn hoàn toàn không còn chút lực chống đỡ nào, gã quỳ xuống đất cộp một tiếng thật mạnh trước sự bàng hoàng của mọi người.</p>
<p>Mồ hôi lạnh chảy ra như tắm, ướt sũng cả mái tóc vuốt gel bóng lộn ban nãy của gã giám đốc kiêu ngạo nay đã biến thành kẻ tội đồ.</p>
<p>Trần Mỹ Hạnh đứng phía dưới sân khấu ôm chặt lấy lồng ngực đang phập phồng dữ dội, nước mắt tuôn rơi như mưa trong sự tiếc nuối tột cùng.</p>
<p>Cô khóc nấc lên từng tiếng nghẹn ngào khi nhận ra người chồng nghèo hèn bị cả gia đình cô chà đạp lại chính là vị tỷ phú đứng đầu đế chế Vạn Xuân.</p>
<p>Bùi Anh Tuấn bước lên sân khấu lớn, đĩnh đạc đứng ở vị trí trung tâm rực rỡ ánh hào quang dưới hàng trăm ống kính phóng viên báo chí.</p>
<p>Ngô Phương Thảo bước đến bên cạnh anh, nghiêm cẩn dâng lên tập hồ sơ M&A đã được ban pháp chế sửa đổi toàn bộ các điều khoản ký kết.</p>
<p>Tuấn cầm chiếc bút Montblanc mạ vàng đắt giá lên, ký những nét chữ sắc bén, dứt khoát quyết định số phận của gia tộc họ Trần đêm nay.</p>
<p>"Hợp đồng M&A dự án Royal Lotus Tây Hồ chính thức được ký kết với giá trị chuyển nhượng thực tế là không đồng chấn động thị trường."</p>
<p>"Khoản tiền một nghìn năm trăm tỷ đồng ban đầu sẽ được cấn trừ toàn bộ vào khoản nợ phạt kỹ thuật và bồi thường thiệt hại rút ruột công trình."</p>
<p>"Đồng thời, Vạn Xuân Group chính thức mua lại toàn bộ khoản nợ gốc một nghìn hai trăm tỷ đồng của Trần Gia Group tại ngân hàng Agribank."</p>
<p>"Từ giây phút này, Trần Gia Group chính thức trở thành công ty con phụ thuộc hoàn toàn vào sự kiểm soát tuyệt đối của Vạn Xuân chúng tôi."</p>
<p>Giọng nói trầm ấm nhưng đầy uy lực của Bùi Anh Tuấn vang vọng khắp khán phòng rộng lớn của khách sạn JW Marriott như một lời phán quyết cuối cùng.</p>
<p>Để tăng tính thuyết phục, ông Vũ Nam Sơn - đại diện pháp lý cao cấp của ngân hàng Agribank chi nhánh Hà Đông cũng đĩnh đạc bước lên sân khấu.</p>
<p>Ông Sơn dõng dạc tuyên bố trước toàn thể quan khách về việc chuyển nhượng toàn bộ quyền đòi nợ và tài sản thế chấp của Trần gia sang cho Vạn Xuân Group.</p>
<p>Gương mặt ông cụ Trần Thế Xương xám ngoét không còn chút sắc khí, lồng ngực phập phồng liên hồi, bàn tay khô héo bấu chặt lấy thành ghế để tránh ngã quỵ.</p>
<p>Toàn bộ tài sản tích lũy cả đời của dòng họ Trần bỗng chốc bốc hơi sạch sẽ chỉ sau một chữ ký đanh thép của chàng rể nghèo bị họ khinh bỉ.</p>
<p>Từ phía cửa sảnh chính, sáu chiến sĩ cảnh sát kinh tế thuộc Cục Cảnh sát điều tra C03 đĩnh đạc bước vào sảnh tiệc hướng thẳng lên sân khấu.</p>
<p>Chiếc còng số tám bằng thép lạnh ngắt nhanh chóng khóa chặt hai tay của Trần Quang Hải trong tiếng la hét hoảng loạn, tuyệt vọng của gã rể hách dịch.</p>
<p>"Bố ơi cứu con! Mỹ Hạnh ơi cứu anh rể với! Tôi không muốn đi tù! Tôi bị vu khống! Xin Chủ tịch Bùi tha mạng cho tôi!"</p>
<p>Trần Quang Hải bị hai cảnh sát áp giải kéo lê đi trên thảm đỏ sảnh tiệc trong sự ghẻ lạnh và khinh bỉ tột cùng của toàn thể quan khách thượng lưu.</p>
<p>Mỹ Hạnh đứng bên dưới sân khấu, đôi bàn tay đan chặt vào nhau đến mức móng tay cắm sâu vào da thịt rỉ máu đỏ tươi mà không hề cảm thấy đau đớn.</p>
<p>Nỗi ân hận tột cùng cào xé tâm can cô khi nhớ lại ba năm qua chồng mình đã thầm lặng chăm sóc cô từng chút một, chịu đựng mọi tủi nhục.</p>
<p>Cô tiến lên một bước định bám lấy vạt áo tuxedo của Tuấn để van xin: "Tuấn ơi, em biết lỗi rồi, xin anh cho gia đình em một đường sống!"</p>
<p>Bùi Anh Tuấn lạnh lùng nhìn cô, ánh mắt không còn một chút ấm áp nào mà chỉ là một khoảng băng giá sâu thẳm đầy lý trí.</p>
<p>Ngô Phương Thảo lập tức bước lên chắn giữa hai người, giọng nói của nữ giám đốc vô cùng đanh thép, thiết lập ranh giới sòng phẳng rạch ròi.</p>
<p>"Trần tiểu thư, xin hãy tự trọng và giữ khoảng cách phù hợp với Chủ tịch của chúng tôi trước khi bảo vệ phải can thiệp cưỡng chế."</p>
<p>"Tất cả mọi điều khoản trong hợp đồng M&A đã được ký kết và thực thi đúng theo các quy định của luật doanh nghiệp hiện hành."</p>
<p>"Chúng tôi làm việc hoàn toàn dựa trên cơ sở pháp lý và sự sòng phẳng tài chính, không có chỗ cho những lời cầu xin tình cảm sáo rỗng."</p>
<p>Trần Mỹ Hạnh ngã quỵ xuống nền đá cẩm thạch buốt giá, khóc than trong muộn màng khi hiểu rằng cô đã vĩnh viễn đánh mất đi hào quang gia tộc đích thực.</p>
<p>Bùi Anh Tuấn đứng ở trung tâm sân khấu rực rỡ ánh hào quang, Ngô Phương Thảo đứng bên cạnh nghiêm cẩn hỗ trợ anh công bố chiến dịch PR mới.</p>
<p>"Đêm nay, chiến dịch tái cấu trúc toàn diện chuỗi khách sạn siêu sang mang thương hiệu Vạn Xuân Lotus chính thức được bắt đầu vận hành."</p>
<p>"Chúng tôi sẽ quét sạch mọi sâu mọt, xây dựng những công trình chất lượng đỉnh cao bằng sự sòng phẳng, minh bạch và luật pháp nghiêm minh."</p>
<p>Hàng trăm ống kính phóng viên báo chí liên tục chớp nháy, ghi lại khoảnh khắc lịch sử chấn động toàn bộ giới kinh doanh địa ốc cả nước.</p>
<p>Dưới ánh đèn pha lê rực rỡ dát vàng của đêm tiệc thượng lưu, Bùi Anh Tuấn đứng sừng sững trên đỉnh cao quyền lực, tỏa sáng hào quang rực rỡ.</p>"""

data["chapters"][4]["content"] = chapter_5_content

with open(path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Novel 18 Chapter 5 updated successfully!")
