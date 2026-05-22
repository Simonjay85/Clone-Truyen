import json
import os

novel_data = {
  "title": "Tài Xế Taxi Bị Khách VIP Khinh Thường, Tài Xế Đó Sở Hữu Công Ty Taxi Lớn Nhất Thành Tâm",
  "subtitle": "Hành Trình Vinh Quang",
  "author": "Đông Hải Cư Sĩ",
  "genre": "Sảng Văn",
  "intro": "<p><strong>\"Cậu chỉ là một gã tài xế taxi truyền thống rác rưởi, cả đời này cũng không ngẩng đầu lên được trước ứng dụng gọi xe công nghệ của chúng tôi!\"</strong></p><p>Tại Sân bay Quốc tế Thành Tâm, gã quản lý kiêu ngạo Phạm Gia Bảo của Go-Fast lớn tiếng sỉ nhục Hoàng Văn Nam trước hàng ngàn hành khách. Hắn không hề biết rằng, người đàn ông 40 tuổi mặc chiếc áo đồng phục bạc màu đang lặng lẽ chịu đựng kia chính là tỷ phú sáng lập Tập đoàn Vận tải Đông Á - đế chế taxi lớn nhất Thành Tâm với hàng chục ngàn đầu xe.</p><p>Bắt tay cùng nữ kiểm toán viên vận hành sắc sảo Trần Thanh Mai, người đòi hỏi quyền điều hành sòng phẳng và cổ phần ưu đãi để tái cấu trúc bộ phận, Hoàng Văn Nam từng bước giăng ra một thiên la địa võng từ luật pháp công đoàn đến các đòn bẩy tài chính tàn khốc, đẩy đối thủ vào cảnh phá sản và phải quỳ gối tạ tội.</p>",
  "cover_prompt": "A high-end book cover, highly detailed web novel illustration style, a handsome and mature Vietnamese CEO in his late 30s standing confidently next to a sleek luxury black sedan in front of a busy modern international airport terminal in Vietnam during a beautiful sunrise. Professional and elite look, clean cinematic lighting, rich colors.",
  "chapters": []
}

def count_words(text):
    clean_text = text.replace("<p>", "").replace("</p>", "").replace("\n", " ")
    words = clean_text.split()
    return len(words)

chapter_1_detailed = [
    "Chiếc xe Toyota Vios cũ kỹ màu bạc mang logo taxi truyền thống Đông Á đỗ im lìm tại làn đường đón khách B của ga đến quốc tế Sân bay Quốc tế Thành Tâm.",
    "Cái nắng oi bức của trưa hè miền Nam dội xuống lớp vỏ kim loại rỉ sét của xe, phả ra hơi nóng hầm hập vô cùng khó chịu lên mặt đường nhựa bốc khói.",
    "Hoàng Văn Nam, bốn mươi tuổi, lặng lẽ tựa lưng vào cabin lái, tay cầm chiếc khăn lông cũ đã sờn rách lau vội những giọt mồ hôi đang lăn dài trên trán.",
    "Gương mặt anh sạm nắng, in hằn những vết sương gió của cuộc đời bươn chải đầy gian khổ trên từng cung đường ngang dọc của thành phố Thành Tâm năng động.",
    "Thế nhưng, sâu trong đôi mắt sáng quắc như chim ưng của người đàn ông trung niên kia lại ẩn chứa một tia lạnh lùng và điềm tĩnh đến đáng sợ.",
    "Không ai tại sân bay quốc tế đông đúc này biết được rằng, người đàn ông mặc chiếc áo đồng phục xanh bạc màu đang đứng đây chính là tỷ phú sáng lập Tập đoàn Vận tải Đông Á.",
    "Tập đoàn Đông Á dưới sự chèo lái âm thầm của anh đã sở hữu hơn mười ngàn đầu xe taxi truyền thống trên khắp các tỉnh thành cả nước từ Nam ra Bắc.",
    "Một chiếc xe siêu sang Mercedes-Maybach màu đen bóng lướt tới cực êm, đỗ xịch ngay phía trước chiếc xe Vios cũ kỹ đầy bụi bặm của Nam.",
    "Cánh cửa xe mở ra, Phạm Gia Bảo bước xuống trong bộ vest xanh Navy may đo tỉ mỉ từ nhà mốt Pháp, mái tóc vuốt gel chải chuốt bóng loáng không một sợi lệch.",
    "Bảo hiện là Giám đốc Vận hành của ứng dụng gọi xe công nghệ đối thủ Go-Fast, thế lực mới nổi đang dùng dòng vốn ngoại để điên cuồng bành trướng.",
    "Đi cùng Bảo là một khách VIP người nước ngoài tên David, vị đại diện tối cao của quỹ đầu tư mạo hiểm lớn đang khảo sát thị trường giao thông Việt Nam.",
    "Phạm Gia Bảo nhìn lướt qua chiếc xe của Nam với vẻ mặt vô cùng khinh bỉ, rồi quay sang nói lớn bằng tiếng Anh để thể hiện đẳng cấp vượt trội của mình.",
    "Hắn chỉ tay vào chiếc Vios cũ kỹ của Nam và bảo rằng đây chính là đống sắt vụn hết thời, là vết nhơ cần phải dọn dẹp sạch sẽ của ngành giao thông Thành Tâm.",
    "Sau đó, Bảo tiến lại gần Nam, ném mạnh ba chiếc vali da cá sấu đắt tiền xuống mặt đường đầy khói bụi và dầu mỡ ngay trước mũi giày của anh.",
    "Hắn hất cằm lên trời, giọng hống hách ra lệnh cho Nam phải ngay lập tức xách toàn bộ hành lý này đặt gọn gàng vào cốp xe cho vị khách VIP kia.",
    "Nam khẽ nhíu mày, nhìn những chiếc vali da đắt tiền rồi lịch sự giải thích rằng xe của anh đã có khách đặt trước qua tổng đài truyền thống từ trước.",
    "Khách hàng đặt xe là một sản phụ vừa đáp chuyến bay dài từ Singapore về nước, anh bắt buộc phải tuân thủ đúng thứ tự đón khách và không thể nhận chuyến này.",
    "Phạm Gia Bảo nghe xong lời giải thích liền nổi trận lôi đình, mặt đỏ gay vì cho rằng gã tài xế taxi quèn dám làm mất mặt hắn trước vị đối tác nước ngoài.",
    "Hắn rút chiếc ví da hiệu Hermès ra, lấy ra một tờ tiền mệnh giá năm trăm ngàn đồng rồi ném thẳng vào mặt Hoàng Văn Nam với thái độ cực kỳ ngạo mạn.",
    "Tờ tiền mệnh giá lớn bay lơ lửng trong không trung rồi rơi xuống mặt đường nhựa nóng ran, nằm im lìm bên cạnh chiếc bánh xe rỉ sét bám đầy bùn đất.",
    "Bảo cười khẩy, mỉa mai Nam chỉ là kẻ nghèo hèn rách nát, cả đời này chỉ biết bám lấy cái vô lăng rách để kiếm từng đồng bạc lẻ qua ngày.",
    "Hắn lớn tiếng tuyên bố trước đám đông hành khách rằng Go-Fast chuẩn bị ký kết hợp đồng độc quyền khai thác toàn bộ làn đón khách VIP của sân bay Thành Tâm.",
    "Khi hợp đồng độc quyền này được ký kết, Go-Fast sẽ quét sạch toàn bộ dòng taxi truyền thống của Đông Á ra khỏi khu vực bến bãi đỗ xe VIP này.",
    "Bảo khẳng định chắc nịch rằng Đông Á sẽ sớm phá sản trong vòng ba tháng tới, và hàng ngàn tài xế nghèo khổ của hãng sẽ phải ra đường ăn xin.",
    "Hoàng Văn Nam lặng lẽ nhìn tờ tiền nằm dưới đất, rồi khẽ cúi người nhặt lên, phủi nhẹ lớp cát bụi bám trên bề mặt tờ tiền polyme một cách cẩn thận.",
    "Anh không hề tỏ ra tức giận hay nhục nhã, gương mặt anh vẫn bình thản như mặt nước hồ không một chút gợn sóng giữa cơn bão táp cuộc đời.",
    "Thế nhưng, ngón tay anh khẽ siết chặt tờ tiền đến mức khớp xương ngón tay trắng bệch, lộ rõ những đường gân xanh cứng như thép nguội.",
    "Sự bình thản đến mức lạnh lùng của Nam khiến Phạm Gia Bảo đột nhiên cảm thấy một luồng mồ hôi lạnh toát chảy dài sau gáy hắn ta.",
    "Hắn khẽ rùng mình một cái, tự dưng cảm thấy bất an mà không hiểu vì sao ánh mắt của gã tài xế trung niên trước mặt lại sâu thẳm như vực thẳm.",
    "Để che giấu sự hoang mang đang dâng lên trong lòng, Bảo lớn tiếng mắng nhiếc thêm vài câu thô tục rồi thúc giục vị khách VIP bước lên xe.",
    "Chiếc xe sang trọng của Go-Fast rú ga mạnh mẽ phóng đi, để lại một làn khói đen kịt phả thẳng vào gương mặt điềm tĩnh của Hoàng Văn Nam.",
    "Phía góc khuất của ga đến quốc tế, Trần Thanh Mai đứng lặng lẽ quan sát toàn bộ sự việc kịch tính từ đầu đến cuối không bỏ sót một chi tiết nào.",
    "Cô diện bộ vest công sở màu đen ôm sát cơ thể thanh mảnh, trên tay cầm chiếc máy tính bảng iPad liên tục ghi chép số liệu vận hành thực tế.",
    "Mai là một kiểm toán viên vận hành vô cùng sắc sảo và có tiếng tăm trong giới tài chính, vừa được tập đoàn Đông Á mời về làm việc.",
    "Cô đã nhận ra Hoàng Văn Nam từ trước qua các tài liệu mật của hội đồng quản trị, nhưng cô không hề lên tiếng vạch trần thân phận của anh.",
    "Mai khẽ mỉm cười, ánh mắt cô lóe lên sự thú vị và kính nể khi nhìn thấy sự nhẫn nại ẩn giấu sức mạnh sấm sét của Hoàng Văn Nam.",
    "Cô biết rằng gã quản lý kiêu ngạo Phạm Gia Bảo của Go-Fast đã tự tay châm ngòi cho một cơn thịnh nộ khủng khiếp của vị chúa tể vận tải.",
    "Hoàng Văn Nam quay trở lại cabin xe, khẽ vuốt ve chiếc vô lăng bọc da đã mòn vẹt và lẩm nhẩm tự nhủ rằng trò chơi thực sự bây giờ mới bắt đầu.",
    "Anh mở chiếc điện thoại Nokia cũ kỹ ra, gửi một tin nhắn ngắn gọn cho người trợ lý thân cận yêu cầu chuẩn bộ bến bãi sân bay.",
    "Gió chiều từ sông Sài Gòn thổi vào khu vực sân bay mang theo hơi ẩm mằn mặn, nhưng không thể làm dịu đi bầu không khí ngột ngạt của cuộc chiến.",
    "Dòng người qua lại tấp nập tại Sân bay Quốc tế Thành Tâm vẫn không hề hay biết về một cơn bão tài chính sắp sửa quét qua thành phố này.",
    "Hoàng Văn Nam đạp nhẹ ga, chiếc Toyota Vios cũ kỹ từ từ chuyển bánh lách qua những hàng rào chắn an ninh nghiêm ngặt của sân bay quốc tế."
]

chapter_2_detailed = [
    "Quán cà phê Highland nằm nép mình bên dưới tòa tháp Vietcombank sừng sững tại trung tâm Quận 1 chìm trong ánh đèn vàng ấm áp và yên tĩnh.",
    "Hoàng Văn Nam ngồi lặng lẽ ở một góc khuất gần cửa sổ sát đất, ánh mắt anh dõi theo những vệt sáng dài của dòng xe cộ trên đường Tôn Đức Thắng.",
    "Lúc này, khí chất của một gã tài xế taxi truyền thống lam lũ đã hoàn toàn biến mất, nhường chỗ cho vẻ uy nghiêm, lạnh lùng của một vị chủ tịch.",
    "Trần Thanh Mai bước vào quán với phong thái vô cùng tự tin và chuyên nghiệp, chiếc chân váy bút chì màu đen kết hợp với sơ mi trắng thanh lịch.",
    "Cô không hề vòng vo xã giao, kéo ghế ngồi đối diện Nam rồi đặt mạnh xấp tài liệu kiểm toán dày cộp bọc da lên mặt bàn kính bóng loáng cộp một cái.",
    "Mai nhìn thẳng vào mắt Nam, giọng nói sắc sảo và dứt khoát của cô vang lên phá tan bầu không khí im lặng giữa hai người.",
    "Cô bắt đầu vạch trần những lỗ hổng vận hành nghiêm trọng đang âm thầm hủy hoại Tập đoàn Đông Á từ sâu bên trong hệ thống quản lý.",
    "Theo báo cáo kiểm toán của Mai, rất nhiều trưởng ca và quản lý bến bãi tại khu vực sân bay đang nhận hối lộ từ các nhóm tài xế ruột.",
    "Họ ưu tiên phân bổ những ca trực tốt nhất, những vị trí đón khách VIP thuận lợi nhất cho những kẻ chịu chi tiền hoa hồng cao dưới gầm bàn.",
    "Điều này gây ra sự bất mãn cực kỳ lớn trong công đoàn tài xế chân chính, những người đang ngày đêm làm việc cật lực nhưng bị chèn ép.",
    "Tệ hại hơn, Mai đã phát hiện ra Go-Fast đang âm thầm dùng tiền để mua chuộc các nhân sự chủ chốt trong ban chấp hành công đoàn tài xế Đông Á.",
    "Họ muốn kích động một cuộc đình công quy mô lớn ngay tại Sân bay Thành Tâm để khiến Đông Á bị Ban quản lý sân bay phạt nặng vì vi phạm hợp đồng bến bãi.",
    "Nam lặng lẽ lắng nghe từng lời của Mai, gương mặt anh đanh lại như đá tảng, gân xanh trên trán khẽ giật mạnh theo từng con số báo cáo.",
    "Anh khẽ bấm ngón tay dưới bàn sâu vào lòng bàn tay đến mức rỉ máu đỏ tươi để kiềm chế sự tức giận trước sự thối nát của bộ máy dưới quyền.",
    "Trần Thanh Mai nhìn thấy phản ứng của Nam nhưng cô không hề e sợ, trái lại cô càng tỏ ra kiêu hãnh và sòng phẳng hơn bao giờ hết.",
    "Cô đẩy một bản hợp đồng thỏa thuận hợp tác đã được soạn thảo sẵn sang phía Nam, trên đó ghi rõ những điều khoản điều kiện vô cùng chi tiết.",
    "Mai dứt khoát tuyên bố cô muốn có được năm phần trăm cổ phần ưu đãi biểu quyết của Tập đoàn Vận tải Đông Á để cam kết gắn bó lâu dài.",
    "Đồng thời, cô yêu cầu phải được trao toàn quyền quyết định tối cao trong việc tái cấu trúc bộ phận gọi xe công nghệ mới thành lập là Đông Á Go.",
    "Mai khẳng định cô là người làm việc dựa trên năng lực và hiệu quả thực tế, cô không bao giờ bán rẻ chất xám của mình cho bất kỳ ai.",
    "Nếu Hoàng Văn Nam không chấp nhận những điều kiện sòng phẳng này, cô sẽ lập tức ký hợp đồng đầu quân cho một quỹ đầu tư ngoại bang lớn của Singapore.",
    "Quỹ đầu tư đó hiện đang là cổ đông chiến lược đứng sau hậu thuẫn cho ứng dụng Go-Fast của Phạm Gia Bảo để tiêu diệt các doanh nghiệp nội địa.",
    "Nam nhìn sâu vào đôi mắt kiên định của Trần Thanh Mai, cảm nhận được ngọn lửa đam mê và bản lĩnh phi thường của người con gái trẻ tuổi sắc sảo này.",
    "Anh biết rằng Đông Á đang cực kỳ cần một người có cái đầu lạnh, sự am hiểu sâu sắc về quản trị số và sự sòng phẳng như cô để lột xác.",
    "Nam khẽ nở một nụ cười nhạt, lấy chiếc bút ký cao cấp Parker từ trong túi áo đồng phục ra, ký xoạch một đường dứt khoát dưới bản thỏa thuận.",
    "Anh ngẩng đầu lên nhìn cô và khẳng định rằng anh hoàn toàn chấp nhận những điều kiện sòng phẳng mà cô đưa ra không thiếu một chữ.",
    "Kể từ giây phút này, Trần Thanh Mai chính thức trở thành Giám đốc Kiểm toán Vận hành kiêm Phó Tổng giám đốc điều hành dự án Đông Á Go.",
    "Nam giao cho cô toàn quyền kiểm soát nhân sự của mảng công nghệ, sẵn sàng sa thải bất kỳ kẻ nào cản đường cuộc cách mạng tái cấu trúc này.",
    "Mai khẽ thở phào nhẹ nhõm, nhưng nhanh chóng lấy lại vẻ lạnh lùng vốn có, cất bản thỏa thuận có chữ ký của chủ tịch vào chiếc cặp táp da.",
    "Cô bắt đầu trình bày chi tiết kế hoạch hành động khẩn cấp trong vòng bốn mươi tám giờ tới để đập tan âm mưu kích động đình công của Go-Fast.",
    "Nam gật đầu đồng ý, ánh mắt anh lóe lên những tia sáng lạnh lẽo khi nghĩ đến gã quản lý kiêu ngạo Phạm Gia Bảo và những kẻ phản bội.",
    "Họ nghĩ rằng có thể dùng tiền để thao túng những người tài xế nghèo khổ, dùng công nghệ để đè bẹp các giá trị truyền thống vững chắc.",
    "Nhưng họ không biết rằng Hoàng Văn Nam là người bước lên từ vị trí tài xế taxi quèn, anh hiểu rõ tài xế cần gì và nghĩ gì hơn ai hết.",
    "Cuộc họp kết thúc khi đồng hồ điểm mười hai giờ đêm, cả khu trung tâm Quận 1 đã chìm sâu vào giấc ngủ dưới làn sương mỏng từ sông thổi vào.",
    "Nam tiễn Mai ra xe taxi Đông Á đang chờ sẵn ngoài sảnh tòa nhà, khẽ nhắc nhở cô chú ý an toàn trong những ngày sóng gió sắp tới.",
    "Mai mỉm cười chào anh, chiếc xe lướt đi trong đêm tĩnh lặng, để lại Hoàng Văn Nam đứng một mình dưới chân tòa tháp Vietcombank sừng sững.",
    "Anh ngửa mặt nhìn lên bầu trời đêm không một vì sao của Thành Tâm, lòng tràn đầy quyết tâm bảo vệ đế chế vận tải mà mình đã dành cả đời gầy dựng.",
    "Ngày mai, cơn bão kiểm toán sẽ quét sạch những vết nhơ đầu tiên tại bến bãi sân bay, bắt đầu từ những gã trưởng ca tham lam vô độ.",
    "Nam biết rằng Phạm Gia Bảo sẽ sớm nhận ra sự thay đổi kỳ lạ này, nhưng lúc đó mọi thứ đã quá muộn để hắn có thể xoay chuyển tình thế.",
    "Máu từ lòng bàn tay Nam đã ngưng chảy, nhưng vết thương đó như một lời nhắc nhở đanh thép về trách nhiệm nặng nề của anh với hàng vạn tài xế.",
    "Anh sẽ không để bất kỳ ai bị bỏ lại phía sau trong cuộc chiến sinh tử này, đó là lời hứa danh dự của người sáng lập Đông Á."
]

chapter_3_detailed = [
    "Phạm Gia Bảo ngồi trong phòng làm việc sang trọng của Go-Fast, gương mặt tối sầm lại khi kế hoạch mua chuộc trưởng ca sân bay bị đổ bể.",
    "Hắn quyết định điên cuồng kích hoạt quân cờ tẩy mạnh nhất: Nguyễn Văn Hùng, Trưởng ban Chấp hành Công đoàn chi nhánh sân bay Thành Tâm của Đông Á.",
    "Bảo đã chuyển thẳng một khoản tiền lớn vào tài khoản Vietcombank của Hùng để ép gã phải kích động một cuộc đình công quy mô lớn ngay lập tức.",
    "Hùng lập tức lôi kéo hơn ba trăm tài xế taxi Đông Á nhẹ dạ cả tin tụ tập tại một nhà kho cũ nát nằm sâu gần khu vực cảng Cát Lái.",
    "Họ dự định sẽ đồng loạt khóa xe tại các làn đường đón khách của ga quốc tế sân bay Thành Tâm, tạo ra một vụ ùn tắc giao thông kinh hoàng.",
    "Mục đích của Bảo là mượn tay Ban quản lý sân bay để đơn phương chấm dứt hợp đồng cho thuê bến bãi dài hạn với Tập đoàn Vận tải Đông Á.",
    "Bầu không khí trong nhà kho cũ nát ngột ngạt tiếng la ó, khói thuốc lá bay mù mịt làm cay xè mắt những người tài xế đang hoang mang.",
    "Nguyễn Văn Hùng đứng trên chiếc bục gỗ cũ, lớn tiếng rêu rao rằng ban lãnh đạo Đông Á đang bóc lột tài xế và sắp bán công ty cho nước ngoài.",
    "Gã ra sức kích động mọi người hãy đình công, hãy mang xe ra chặn các ngả đường sân bay để đòi quyền lợi và gây áp lực tối đa.",
    "Đúng lúc đó, tiếng động cơ quen thuộc vang lên bên ngoài, chiếc xe Toyota Vios cũ kỹ của Hoàng Văn Nam đỗ xịch trước cửa nhà kho.",
    "Nam lặng lẽ bước xuống xe, vẫn trong bộ đồng phục tài xế màu xanh bạc màu, anh bình thản đẩy cánh cửa sắt rỉ sét bước vào trong.",
    "Nguyễn Văn Hùng nhìn thấy anh liền cười khẩy khinh bỉ, lớn tiếng sỉ nhục Nam chỉ là một gã tài xế quèn, nhát gan và làm tay sai cho sếp.",
    "Hùng thách thức Nam bước lên bục nếu dám khuyên ngăn mọi người từ bỏ cuộc đình công vì quyền lợi của những người lao động nghèo khổ.",
    "Hoàng Văn Nam không hề nao núng, anh điềm tĩnh bước từng bước vững chãi lên bục gỗ, khí chất trầm hùng bỗng chốc bao trùm cả nhà kho.",
    "Giọng nói trầm ấm nhưng đanh thép của anh vang lên qua chiếc loa cầm tay, rõ ràng và mạch lạc át đi toàn bộ những tiếng la ó ồn ào.",
    "Nam không hề dùng bạo lực hay lời lẽ đe dọa, anh từ tốn lấy ra một cuốn sách nhỏ chứa Luật Công đoàn Việt Nam và Bộ luật Lao động.",
    "Anh bắt đầu phân tích khúc chiết về mặt pháp lý cho toàn thể tài xế đang ngồi dưới hiểu rõ về hậu quả pháp lý cực kỳ nghiêm trọng.",
    "Nam chỉ ra rằng cuộc đình công tự phát này hoàn toàn không tuân thủ quy trình của Tổng Liên đoàn Lao động, tức là một cuộc đình công bất hợp pháp.",
    "Theo quy định pháp luật, việc dùng phương tiện giao thông chặn lối đi tại sân bay - công trình an ninh quốc gia trọng điểm - là vi phạm hình sự.",
    "Những tài xế tham gia không những không đòi được quyền lợi, mà còn đối mặt với nguy cơ bị thu hồi vĩnh viễn thẻ hành nghề taxi của mình.",
    "Thế thậm chí, họ còn có thể bị khởi tố hình sự về tội gây rối trật tự công cộng và hủy hoại hoạt động kinh tế của cả một cửa ngõ quốc gia.",
    "Hàng trăm tài xế ngồi dưới nghe đến đây liền giật mình thon thót, những khuôn mặt sạm đen bắt đầu lấm tấm những giọt mồ hôi lạnh ngắt.",
    "Sau đó, Hoàng Văn Nam đanh thép bóc trần bộ mặt thật đầy dối trá của ứng dụng gọi xe công nghệ Go-Fast mà Hùng đang ra sức ca ngợi.",
    "Anh vạch rõ Go-Fast chỉ coi tài xế là đối tác độc lập trên danh nghĩa để trốn tránh toàn bộ nghĩa vụ đóng bảo hiểm xã hội và bảo hiểm y tế.",
    "Khi tài xế gặp tai nạn hay ốm đau trên đường, Go-Fast sẽ lập tức khóa tài khoản và phủi bỏ toàn bộ trách nhiệm pháp lý lẫn nhân đạo.",
    "Họ sẵn sàng tăng mức chiết khấu lên đến ba mươi phần trăm một khi đã tiêu diệt được taxi truyền thống để độc chiếm hoàn toàn thị trường.",
    "Trong khi đó, Đông Á suốt hai mươi năm qua luôn bảo đảm mức lương cứng ổn định, đóng đầy đủ bảo hiểm tại Bảo hiểm Xã hội Thành Tâm.",
    "Đông Á còn thành lập Quỹ Nâng Bước Ước Mơ để tài trợ toàn bộ học phí cho con em của những tài xế có hoàn cảnh khó khăn vươn lên học giỏi.",
    "Nam nhìn thẳng vào mắt Nguyễn Văn Hùng, hỏi gã có dám lấy danh dự và số tiền hối lộ trong tài khoản ra để bảo đảm cuộc sống cho anh em không.",
    "Nguyễn Văn Hùng nghe xong mặt cắt không còn giọt máu, toàn thân gã run rẩy cầm cập, mồ hôi lạnh chảy ròng ròng ướt đẫm cả vạt áo sơ mi.",
    "Gã lắp bắp không nói nên lời, lùi lại phía sau rồi bất ngờ trượt chân ngã cộp xuống sàn gỗ cũ nát trước sự chứng kiến của hàng trăm người.",
    "Nhìn thấy sự hèn nhát và dối trá của Hùng bị phơi bày, hàng trăm tài xế dưới nhà kho đồng loạt nhận ra mình đã bị lợi dụng làm quân cờ.",
    "Họ đồng thanh hô to ủng hộ Đông Á, quyết định lập tức giải tán cuộc tụ tập và lái xe trở lại sân bay làm việc như bình thường.",
    "Âm mưu kích động bạo loạn nhằm cướp bến bãi sân bay của Phạm Gia Bảo đã hoàn toàn bị Hoàng Văn Nam đập tan chỉ bằng sự thấu hiểu và luật pháp.",
    "Trần Thanh Mai đứng ngoài cửa nhà kho khẽ mỉm cười đầy thán phục, cô nhanh chóng dùng điện thoại báo cáo tình hình an toàn cho ban giám đốc.",
    "Nam bước xuống bục, vỗ vai từng người tài xế, dặn dò họ hãy yên tâm làm việc vì Đông Á luôn là chỗ dựa vững chắc cho gia đình họ.",
    "Nguyễn Văn Hùng nằm bệt dưới đất, ngón tay bấm chặt vào lòng bàn tay đến rỉ máu vì nhục nhã và sợ hãi trước hình phạt pháp luật sắp tới.",
    "Nam lặng lẽ lướt qua gã phản bội mà không thèm nhìn lại, anh biết pháp luật và ban pháp chế của Mai sẽ xử lý gã một cách thích đáng nhất.",
    "Chiếc Toyota Vios của Nam lại nổ máy lướt đi trong chiều muộn, hướng về phía sân bay để hỗ trợ giải tỏa lượng khách đang ùn ứ tại ga đến.",
    "Bầu trời Thành Tâm chiều nay lộng gió, xua đi những làn khói bụi ngột ngạt và mang lại niềm tin cho hàng ngàn con người lao động chân chính."
]

chapter_4_detailed = [
    "Phạm Gia Bảo điên cuồng kích hoạt chiến dịch trợ giá tự sát mang tên Bão Giá 0 Đồng để quyết tâm đè bẹp ứng dụng mới Đông Á Go.",
    "Hắn liên tục ký các quyết định chiết khấu cực sâu cho khách hàng và trợ cấp gấp đôi cho tài xế để lôi kéo họ rời bỏ Đông Á truyền thống.",
    "Mỗi ngày, Go-Fast đốt sạch hơn năm trăm ngàn đô la Mỹ từ nguồn vốn ngoại của quỹ đầu tư Singapore để duy trì thị phần ảo của mình.",
    "Bảo tự tin rằng với quy mô tài chính hạn hẹp của một doanh nghiệp truyền thống nội địa, Đông Á sẽ kiệt quệ dòng tiền trong vòng hai tuần.",
    "Thế nhưng, Trần Thanh Mai đã sắc bén triển khai một chiến lược tài chính vô cùng thông minh và tiết kiệm hiệu quả tối đa.",
    "Cô chủ động đàm phán sòng phẳng với các ngân hàng lớn hàng đầu Việt Nam là Techcombank và VietinBank để liên kết thanh toán trực tiếp.",
    "Đông Á Go tung ra chương trình hoàn tiền năm mươi phần trăm cho mọi giao dịch thanh toán không dùng tiền mặt qua thẻ của các ngân hàng này.",
    "Chi phí trợ giá này được các ngân hàng đồng tài trợ nhằm phát triển hệ sinh thái thanh toán số, giúp Đông Á không tốn một đồng vốn tự có.",
    "Chương trình lập tức tạo nên một cơn sốt cực lớn trong giới nhân viên văn phòng và tầng lớp trung lưu tại trung tâm thành phố Thành Tâm.",
    "Đồng thời, Hoàng Văn Nam đã âm thầm kích hoạt quân bài tài chính tối mật của mình thông qua một quỹ đầu tư trung gian tại Singapore.",
    "Quỹ đầu tư này do Nam sở hữu toàn bộ cổ phần, đã lặng lẽ mua lại hai mươi lăm phần trăm nợ chuyển đổi sắp đáo hạn của Go-Fast Việt Nam.",
    "Đây là khoản nợ khổng lồ mà Go-Fast đã vay từ các trái chủ quốc tế với những điều khoản cam kết vô cùng khắt khe về tỷ lệ an toàn vốn.",
    "Khi Go-Fast đang điên cuồng đốt tiền đốt vốn ở mức đỉnh điểm, Nam nhận thấy thời cơ chín muồi đã đến để giáng đòn chí mạng lên đối thủ.",
    "Anh yêu cầu các ngân hàng đối tác Techcombank và VietinBank lập tức tiến hành rà soát kỹ lưỡng các khoản bảo lãnh tín dụng của Go-Fast.",
    "Do tỷ lệ nợ trên vốn chủ sở hữu của Go-Fast đã vượt qua ngưỡng an toàn cho phép theo quy định nghiêm ngặt của Ngân hàng Nhà nước.",
    "Techcombank chi nhánh Thành Tâm đã chính thức phát đi văn bản yêu cầu đóng băng toàn bộ tài khoản thanh toán và siết nợ đối với Go-Fast.",
    "Phạm Gia Bảo lúc này đang ngồi trong văn phòng làm việc sang trọng ngập tràn ánh đèn tại tòa tháp Landmark 81 cao chọc trời của thành phố.",
    "Hắn đang đắc ý nhìn biểu đồ tăng trưởng lượng người dùng ảo thì chiếc điện thoại trên bàn làm việc đổ chuông liên hồi như đòi mạng.",
    "Đầu dây bên kia là giọng nói lạnh lùng của Giám đốc Tín dụng Techcombank thông báo về quyết định đình chỉ toàn bộ hạn mức tín dụng của hãng.",
    "Mồ hôi lạnh của Bảo lập tức tuôn ra như tắm, chảy ròng ròng từ trán xuống cằm làm ướt đẫm cả chiếc cổ áo vest hàng hiệu đắt tiền.",
    "Hắn lắp bắp hỏi lý do thì nhận được câu trả lời rằng toàn bộ khoản nợ chuyển đổi của Go-Fast đã bị một chủ nợ bí ẩn mua đứt từ Singapore.",
    "Và chủ nợ bí ẩn đó đã yêu cầu ngân hàng thực hiện đúng điều khoản siết nợ ngay lập tức do Go-Fast vi phạm cam kết tài chính nghiêm trọng.",
    "Bảo nghe xong như sét đánh ngang tai, toàn thân hắn mềm nhũn ra, gục ngã cộp xuống chiếc ghế da giám đốc sang trọng phía sau lưng.",
    "Hắn bàng hoàng nhận ra mình đã hoàn toàn rơi vào một chiếc bẫy nợ tài chính khổng lồ không có lối thoát do đối thủ giăng sẵn từ trước.",
    "Gã quản lý kiêu ngạo giờ đây run rẩy như một chiếc lá trước gió, ngón tay hắn bấm chặt vào mép bàn gỗ đến mức rỉ cả máu đỏ tươi.",
    "Hắn lập tức gọi điện cho các nhà đầu tư tại Singapore để cầu cứu, nhưng đầu dây bên kia chỉ là những tiếng tút dài vô vọng và lạnh lùng.",
    "Các quỹ đầu tư ngoại bang một khi nhận thấy rủi ro pháp lý và tài chính quá lớn sẽ lập tức phủi tay bỏ rơi quân cờ của mình không thương tiếc.",
    "Bảo biết rằng nếu không có dòng vốn mới bơm vào trong vòng hai mươi bốn giờ tới, Go-Fast Việt Nam sẽ chính thức tuyên bố phá sản hoàn toàn.",
    "Trong khi đó, tại trụ sở Tập đoàn Đông Á, Hoàng Văn Nam và Trần Thanh Mai đang đứng trước bản đồ số hiển thị dòng xe Đông Á Go.",
    "Hàng vạn chấm xanh của taxi Đông Á đang phủ kín mọi nẻo đường Thành Tâm, minh chứng cho sự thành công vượt bậc của chiến dịch tái cấu trúc.",
    "Mai nhìn Nam với ánh mắt tràn đầy sự ngưỡng mộ và tôn trọng đối với tầm nhìn chiến lược vĩ đại của vị chủ tịch trung niên sương gió.",
    "Cô khẽ mỉm cười và khẳng định rằng đòn phản công tài chính này đã hoàn toàn bẻ gãy xương sống của Go-Fast tại thị trường Việt Nam.",
    "Nam gật đầu, ánh mắt anh điềm tĩnh nhưng chứa đựng sự kiên định của một người chiến thắng sòng phẳng trên thương trường khốc liệt.",
    "Anh bảo Mai hãy chuẩn bị đầy đủ hồ sơ thâu tóm để sẵn sàng nuốt trọn Go-Fast vào ngày mai khi họ chính thức mất khả năng thanh toán nợ.",
    "Đêm nay, toàn bộ hệ thống máy chủ của Đông Á Go vẫn hoạt động hết công suất để phục vụ hàng triệu chuyến đi an toàn của người dân.",
    "Những người tài xế taxi truyền thống giờ đây đã hoàn toàn tin tưởng vào tương lai tươi sáng dưới sự dẫn dắt của Hoàng Văn Nam.",
    " họ biết rằng họ không chỉ là những người lái xe kiếm sống, mà là những thành viên chính thức được tôn trọng của một tập đoàn lớn nội địa.",
    "Bảo ngồi một mình trong bóng tối của văn phòng Landmark 81, nhìn xuống thành phố Thành Tâm lấp lánh ánh đèn mà lòng đầy cay đắng và sợ hãi.",
    "Hắn biết rằng ngày mai, tại sự kiện ký kết độc quyền bến bãi sân bay, hắn sẽ phải đối mặt với một sự thật vô cùng tàn nhẫn và đau đớn.",
    "Và gã tài xế taxi truyền thống mà hắn từng khinh miệt nhổ nước bọt vào mặt hôm nào chính là người nắm giữ sinh mệnh của cuộc đời hắn."
]

chapter_5_detailed = [
    "Sự kiện ký kết độc quyền quyền khai thác vận tải VIP tại Sân bay Quốc tế Thành Tâm được tổ chức vô cùng trang trọng tại khách sạn Park Hyatt.",
    "Khán phòng rộng lớn được trang hoàng lộng lẫy bằng những ánh đèn pha lê lấp lánh, quy tụ toàn bộ giới tinh hoa tài chính của thành phố.",
    "Phạm Gia Bảo xuất hiện trong bộ dạng vô cùng mệt mỏi, gương mặt hốc hác và đôi mắt thâm quầng vì mất ngủ suốt nhiều đêm liền.",
    "Tuy nhiên, hắn vẫn cố giữ lấy vẻ kiêu ngạo hống hách cuối cùng của mình, hy vọng giành được gói thầu này để đàm phán kéo dài nợ.",
    "Hắn nhìn thấy Hoàng Văn Nam bước vào khán phòng trong bộ vest đen sang trọng, lịch lãm đứng cạnh Trần Thanh Mai vô cùng sắc sảo.",
    "Bảo cười khẩy tiến lại gần Nam, cất giọng mỉa mai lớn tiếng sỉ nhục anh trước mặt toàn bộ các doanh nhân thượng lưu đang có mặt.",
    "Hắn bảo Nam chỉ là một gã tài xế taxi truyền thống rác rưởi, ăn cắp bộ vest sang trọng này để lẻn vào ăn chực tiệc của giới quý tộc.",
    "Bảo đắc ý tuyên bố rằng Go-Fast dù có gặp chút khó khăn tài chính tạm thời nhưng vẫn dư sức đè bẹp dòng taxi Đông Á rách nát của anh.",
    "Hắn thách thức Nam hãy quỳ xuống đất cầu xin hắn ban cho một công việc lái xe công nghệ sau khi Đông Á chính thức tuyên bố phá sản.",
    "Hoàng Văn Nam không hề đáp lời, anh chỉ lặng lẽ nhìn Bảo với ánh mắt điềm tĩnh sâu thẳm chứa đựng sự thương hại cho kẻ ngu xuẩn.",
    "Đúng lúc đó, tiếng nhạc trang trọng vang lên báo hiệu buổi lễ ký kết độc quyền chính thức bắt đầu trước sự mong đợi của mọi người.",
    "Chủ tịch Ban quản lý Sân bay Quốc tế Thành Tâm bước lên bục phát biểu, trân trọng tuyên bố về kết quả đấu thầu gói thầu độc quyền khai thác.",
    "Ông dõng dạc tuyên bố đơn vị giành chiến thắng tuyệt đối chính là Tập đoàn Vận tải Đông Á với ứng dụng công nghệ đột phá Đông Á Go.",
    "Đồng thời, ông trân trọng kính mời Hoàng Văn Nam - Nhà sáng lập kiêm Chủ tịch Hội đồng Quản trị tối cao của Tập đoàn Đông Á bước lên sân khấu.",
    "Tiếng vỗ tay vang dội như sấm bên tai khiến Phạm Gia Bảo nghe như sét đánh ngang tai, toàn thân hắn cứng đờ ra như một khúc gỗ mục.",
    "Trần Thanh Mai lúc này bước lên cạnh Nam, lịch sự công bố quyết định Đông Á đã chính thức hoàn tất thâu tóm toàn bộ Go-Fast Việt Nam.",
    "Do Go-Fast mất khả năng thanh toán khoản nợ chuyển đổi hai mươi lăm phần trăm mà quỹ đầu tư của Hoàng Văn Nam đang nắm giữ trực tiếp.",
    "Phạm Gia Bảo nghe xong tin dữ liền ngã quỵ cộp xuống sàn đá hoa cương lạnh ngắt của khách sạn sang trọng trước hàng trăm ống kính.",
    "Hai đầu gối hắn đập mạnh xuống đất phát ra âm thanh khô khốc, mồ hôi lạnh tuôn ra như tắm chảy dài làm ướt đẫm cả chiếc áo vest.",
    "Ngón tay hắn bấm chặt vào lòng bàn tay đến mức rỉ máu đỏ tươi trên tấm danh thiếp Go-Fast bóp nát trong tay vì nhục nhã tột cùng.",
    "Hắn run rẩy bò đến sát chân Hoàng Văn Nam, cất giọng khàn đặc van xin vị tỷ phú ẩn danh hãy tha thứ và để lại cho hắn một con đường sống.",
    "Hắn thừa nhận sự kiêu ngạo ngu xuẩn của mình khi coi thường một vị chúa tể vận tải ẩn danh dưới chiếc áo tài xế taxi truyền thống.",
    "Hoàng Văn Nam thản nhiên bước qua gã quản lý kiêu ngạo đang quỳ gối dưới đất mà không hề ban phát cho hắn một cái nhìn thương hại nào.",
    "Anh bước lên bục danh dự, đặt bút ký kết hợp đồng độc quyền khai thác bến bãi sân bay sòng phẳng trước sự chứng kiến của giới truyền thông.",
    "Đông Á Go chính thức độc chiếm ngôi vương vận tải tại Thành Tâm, xác lập một kỷ nguyên mới của sự minh bạch và phúc lợi tài xế cao.",
    "Trần Thanh Mai mỉm cười rạng rỡ bên cạnh Nam, cô biết rằng sự sòng phẳng của cô đã mang lại một quả ngọt vô cùng xứng đáng và ngọt ngào.",
    "Hàng vạn tài xế taxi Đông Á ngoài kia đang reo hò vui sướng khi nhận được tin vui thâu tóm lịch sử qua ứng dụng gọi xe của tập đoàn.",
    "Họ biết rằng từ nay về sau, cuộc sống của gia đình họ đã được bảo đảm an toàn vững chắc dưới vương triều vận tải nhân văn của Nam.",
    "Phạm Gia Bảo bị lực lượng an ninh khách sạn Park Hyatt thẳng tay kéo lê ra ngoài sảnh trong sự khinh bỉ và chế giễu của toàn bộ quan khách.",
    "Sự nghiệp và danh tiếng của gã quản lý kiêu ngạo chính thức chôn vùi trong nấm mồ tài chính do chính lòng tham lam của hắn đào sẵn.",
    "Hoàng Văn Nam nâng ly rượu vang đỏ sòng phẳng chúc mừng cùng Trần Thanh Mai và các đối tác ngân hàng lớn Techcombank và VietinBank.",
    "Ánh đèn pha lê lấp lánh phản chiếu nụ cười đầy bản lĩnh và điềm tĩnh của người đàn ông bốn mươi tuổi đã bước qua bao giông bão cuộc đời.",
    "Anh đã chứng minh cho cả thế giới thấy rằng taxi truyền thống Việt Nam khi biết thay đổi công nghệ vẫn có thể đứng vững kiên cường.",
    "Và tấm lòng nhân văn coi trọng người lao động sẽ luôn là nền móng vững chắc nhất để xây dựng nên một đế chế kinh doanh trường tồn.",
    "Trần Thanh Mai khẽ chạm ly với Nam, ánh mắt cô lấp lánh niềm kiêu hãnh của một người phụ nữ sắc sảo đã chọn đúng minh quân để phò tá.",
    "Cô cam kết sẽ dùng toàn bộ tài năng kiểm toán vận hành của mình để đưa Đông Á Go vươn tầm ra toàn bộ khu vực Đông Nam Á sòng phẳng.",
    "Nam gật đầu đồng ý, anh biết rằng với sự đồng hành của cô, không một thế lực ngoại bang nào có thể đe dọa được Đông Á thêm một lần nữa.",
    "Tiệc mừng công kéo dài đến tận đêm khuya trong không khí hân hoan chiến thắng rực rỡ của toàn thể cán bộ nhân viên tập đoàn vận tải.",
    "Bên ngoài khách sạn, những chiếc xe taxi Đông Á Go mới tinh vẫn hối hả lướt đi trên các ngả đường rực rỡ ánh đèn của Thành Tâm.",
    "Hoàng Văn Nam khẽ mỉm cười nhẹ nhàng, trò chơi vương quyền vận tải đã kết thúc viên mãn, mở ra một chương mới đầy vinh quang cho Đông Á."
]

def make_html(paragraphs):
    return "\n".join(f"<p>{p}</p>" for p in paragraphs) + "\n"

c1 = make_html(chapter_1_detailed)
c2 = make_html(chapter_2_detailed)
c3 = make_html(chapter_3_detailed)
c4 = make_html(chapter_4_detailed)
c5 = make_html(chapter_5_detailed)

novel_data["chapters"] = [
    {"title": "Chương 1: Cuộc Gặp Gỡ Lớn Ở Sân Bay", "content": c1},
    {"title": "Chương 2: Cơn Bão Kiểm Toán Và Điều Kiện Sòng Phẳng", "content": c2},
    {"title": "Chương 3: Trò Chơi Pháp Lý Và Quyền Lực Công Đoàn", "content": c3},
    {"title": "Chương 4: Đòn Phản Công Tài Chính", "content": c4},
    {"title": "Chương 5: Vinh Quang Quy Lai, Vả Mặt Kẻ Kiêu Ngạo", "content": c5}
]

for i, ch in enumerate(novel_data["chapters"]):
    w_count = count_words(ch["content"])
    print(f"Chương {i+1} có {w_count} từ.")

output_path = "/Users/aaronnguyen/TN/App/doctieuthuyet/scratch/draft_novel_14.json"
os.makedirs(os.path.dirname(output_path), exist_ok=True)
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(novel_data, f, ensure_ascii=False, indent=2)

print(f"Đã ghi draft thành công vào {output_path}")
