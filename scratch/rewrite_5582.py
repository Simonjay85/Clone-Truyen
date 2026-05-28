import json, urllib.request, openpyxl

story_data = {
    "secret_token": "ZEN_TRUYEN_2026_BYPASS",
    "story_id": 5582,
    "title": "Bị Sa Thải Vì Phanh Phui Tham Nhũng, Tôi Lập Tòa Soạn Độc Lập Khiến Cả Hệ Thống Rút Đơn",
    "intro": "<p>Vũ Phương Nhi — phóng viên điều tra báo Nhân Dân Tỉnh H — bị sa thải sau khi gửi bài điều tra tham nhũng đất đai cho tổng biên tập. Bài báo bị giết. Nguồn tin bị lộ. Và cô — người duy nhất dám viết sự thật — bị đuổi ra khỏi tòa soạn vì \"vi phạm quy trình xuất bản.\"</p>\n<p>Nhưng Phương Nhi không dừng. Cô lập tòa soạn độc lập từ quán cà phê, tuyển ba phóng viên trẻ, và đăng loạt bài điều tra trên trang web riêng — loạt bài mà không tòa soạn nào dám đăng, nhưng hai triệu người đọc.</p>",
    "author": "Vũ Phương Nhi",
    "chapters": []
}

chapters = [
    {
        "title": "Chương 1: Bài Báo Bị Giết",
        "content": """<p>Vũ Phương Nhi ngồi trước màn hình máy tính trong tòa soạn báo Nhân Dân Tỉnh H, nhìn email từ Tổng biên tập Trần Quốc Hùng — ba dòng ngắn gọn:</p>

<p>"Bài điều tra về dự án KĐT Đông Hải không phù hợp với định hướng tuyên truyền. Xóa bản thảo. Không lưu bản sao. Gặp tôi phòng TBT lúc 2 giờ chiều."</p>

<p>Nhi hai mươi tám tuổi, phóng viên điều tra bốn năm kinh nghiệm, từng đoạt Giải Báo chí Quốc gia hạng B cho loạt bài về ô nhiễm môi trường ở khu công nghiệp. Cô là phóng viên trẻ nhất tòa soạn, và cũng là người duy nhất tình nguyện viết bài điều tra — thể loại mà đồng nghiệp gọi là "nghề tự sát" vì ai viết cũng bị ghét.</p>

<p>Bài báo mà Tổng biên tập muốn giết: một cuộc điều tra sáu tháng về dự án Khu đô thị Đông Hải — dự án ba nghìn tỷ đồng do UBND Tỉnh H phê duyệt, giao cho Tập đoàn Hoàng Gia đầu tư. Nhi phát hiện: đất dự án trước đó là đất nông nghiệp của hai trăm hộ dân — bị thu hồi với giá đền bù bốn trăm nghìn đồng mỗi mét vuông, trong khi Hoàng Gia bán lại cho khách hàng giá bốn mươi triệu đồng mỗi mét vuông. Chênh lệch: gấp một trăm lần.</p>

<p>Quan trọng hơn: biên bản họp nội bộ UBND mà Nhi có được — từ nguồn tin ẩn danh — cho thấy Phó Chủ tịch Tỉnh Nguyễn Đức Thắng đã ký duyệt giá đền bù thấp bất thường, đồng thời nhận cổ phần ẩn danh trong Tập đoàn Hoàng Gia thông qua công ty vỏ bọc ở Singapore.</p>

<p>Bằng chứng: biên bản họp, sổ cổ đông công ty vỏ bọc (Nhi đã nhờ luật sư ở Singapore tra cứu), tin nhắn Zalo giữa Phó Chủ tịch Thắng và Chủ tịch Hoàng Gia — ảnh chụp màn hình do nguồn tin cung cấp.</p>

<p>Nhi viết bài sáu nghìn chữ, đặt tên: "Đất Đông Hải: Ai được, ai mất?"</p>

<p>Và Tổng biên tập giết bài trong ba dòng email.</p>

<hr>

<p>Hai giờ chiều, phòng Tổng biên tập.</p>

<p>Trần Quốc Hùng — năm mươi lăm tuổi, tóc muối tiêu, kính gọng vàng — ngồi sau bàn gỗ lim, mặt bình thản.</p>

<p>"Nhi, em giỏi. Bài viết rất tốt. Nhưng không đăng được."</p>

<p>"Tại sao, anh Hùng? Bằng chứng đầy đủ. Pháp lý chặt chẽ. Luật sư đã kiểm tra."</p>

<p>"Vì Phó Chủ tịch Thắng là người phê duyệt ngân sách cho tòa soạn mình. Em hiểu không? Ngân sách mỗi năm — ba mươi tỷ — từ tỉnh. Nếu bài này đăng, tỉnh cắt ngân sách, tòa soạn đóng cửa, sáu mươi người mất việc."</p>

<p>"Anh Hùng, hai trăm hộ dân mất đất. Họ nhận bốn trăm nghìn một mét, trong khi đất đó bán bốn mươi triệu. Đó là ăn cướp."</p>

<p>"Anh biết. Nhưng đây là lựa chọn: sáu mươi người trong tòa soạn, hay hai trăm người ngoài kia. Anh chọn sáu mươi người mình."</p>

<p>Nhi đứng dậy. "Vậy em chọn hai trăm người ngoài kia."</p>

<p>Sáng hôm sau, Nhi nhận quyết định sa thải — lý do: "Vi phạm quy trình xuất bản và bảo mật nguồn tin." Tòa soạn thu lại thẻ phóng viên, laptop, và khóa tài khoản email nội bộ.</p>

<p>Nhi bước ra khỏi tòa soạn, tay cầm hộp đựng đồ cá nhân — một cuốn sổ ghi chép, cây bút bi, và tấm ảnh chụp chung với bạn đồng nghiệp ngày nhận giải báo chí.</p>

<p>Cô không khóc. Cô mở laptop cá nhân — bản sao bài điều tra đã lưu trong USB, nhét trong ví — và bắt đầu nghĩ: nếu không tòa soạn nào dám đăng, thì cô sẽ tự đăng.</p>"""
    },
    {
        "title": "Chương 2: Tòa Soạn Trong Quán Cà Phê",
        "content": """<p>Tòa soạn mới của Vũ Phương Nhi: một chiếc bàn gỗ ở góc quán cà phê Bụi Đời, phường 3, TP.H — quán nhỏ, tường gạch trần, WiFi miễn phí, cà phê sữa đá mười lăm nghìn đồng.</p>

<p>Vốn: laptop cá nhân Asus cũ, điện thoại Samsung A52, USB chứa bài điều tra, và mười hai triệu đồng tiền tiết kiệm — đủ sống hai tháng nếu ăn cơm bụi ba bữa.</p>

<p>Nhi lập website: TinDieuTra.vn — trang tin điều tra độc lập, không quảng cáo, không ngân sách nhà nước, không ai duyệt bài ngoài cô.</p>

<p>Domain: một trăm bốn mươi nghìn đồng mỗi năm. Hosting: hai trăm nghìn mỗi tháng. Template WordPress: miễn phí.</p>

<p>Tổng chi phí lập tòa soạn: bốn trăm nghìn đồng.</p>

<p>Ngày đầu tiên, Nhi đăng bài: "Giới thiệu TinDieuTra.vn — trang tin dành cho những bài báo mà không tòa soạn nào dám đăng."</p>

<p>Không ai đọc. Ngày thứ hai: hai mươi lượt xem. Ngày thứ ba: mười lăm.</p>

<p>Nhưng Nhi không cần lượt xem — cô cần phóng viên. Một mình không thể điều tra nhiều vụ cùng lúc.</p>

<p>Cô gọi điện cho ba người — ba phóng viên trẻ mà cô quen trong nghề, đều bị sa thải hoặc tự nghỉ vì không chịu nổi áp lực tự kiểm duyệt.</p>

<p>Lê Hồng Quân — hai mươi sáu tuổi, cựu phóng viên VnExpress, nghỉ vì bài điều tra về thực phẩm bẩn bị sửa thành bài PR. "Chị Nhi, em theo."</p>

<p>Trương Thị Mai — hai mươi bảy tuổi, cựu phóng viên Tuổi Trẻ, bị chuyển sang viết giải trí vì "viết điều tra nhiều quá gây thù chuốc oán." "Chị, em đang thất nghiệp. Em có hai nguồn tin ở Sở Tài nguyên Tỉnh K chưa dùng."</p>

<p>Nguyễn Đức Anh — hai mươi bốn tuổi, mới ra trường, chưa có việc chính thức, nhưng đã tự làm podcast điều tra trên YouTube với mười nghìn subscriber. "Chị, em làm video và podcast cho TinDieuTra được không?"</p>

<p>"Được. Nhưng có ba quy tắc: một, bằng chứng phải xác minh ít nhất hai nguồn độc lập. Hai, không nhận tiền từ bất kỳ ai — kể cả những người muốn mình viết. Ba, bảo vệ nguồn tin bằng mọi giá — kể cả vào tù."</p>

<p>Ba người gật đầu.</p>

<p>Tòa soạn TinDieuTra.vn: bốn người, một quán cà phê, một laptop, và một USB chứa sự thật.</p>"""
    },
    {
        "title": "Chương 3: Loạt Bài Đông Hải",
        "content": """<p>Nhi đăng loạt bài "Đất Đông Hải: Ai được, ai mất?" — chia thành năm kỳ, mỗi kỳ cách nhau ba ngày, đăng trên TinDieuTra.vn và chia sẻ qua Facebook.</p>

<p>Kỳ 1: "200 hộ dân mất đất, giá đền bù 400.000đ/m² — đất bán lại 40 triệu/m²."</p>

<p>Kỳ 2: "Biên bản họp UBND: Phó Chủ tịch Thắng ký duyệt giá đền bù thấp bất thường."</p>

<p>Kỳ 3: "Công ty vỏ bọc ở Singapore: ai là cổ đông ẩn danh?"</p>

<p>Kỳ 4: "Tin nhắn Zalo giữa Phó Chủ tịch và Chủ tịch Hoàng Gia: 'Cứ ký đi, phần anh có.'"</p>

<p>Kỳ 5: "200 hộ dân lên tiếng: 'Chúng tôi bị cướp đất.'"</p>

<p>Kỳ 1 đăng ngày thứ Hai — năm trăm lượt xem. Kỳ 2 đăng ngày thứ Năm — ba nghìn lượt xem. Kỳ 3 — hai mươi nghìn. Kỳ 4 — một trăm năm mươi nghìn. Kỳ 5 — bốn trăm nghìn lượt xem trong hai mươi bốn giờ.</p>

<p>TinDieuTra.vn từ trang web không ai biết trở thành hiện tượng — không phải vì Nhi PR giỏi, mà vì bài điều tra có bằng chứng cứng đến mức không ai phản bác được.</p>

<p>Báo chí chính thống bắt đầu đưa tin — nhưng không trích dẫn TinDieuTra.vn (vì không dám), mà viết: "Theo nguồn tin trên mạng xã hội..." Cách né tránh quen thuộc — nhưng Nhi không quan tâm ai trích dẫn. Cô quan tâm hai trăm hộ dân có đọc không.</p>

<p>Họ đọc. Và họ làm đơn khiếu nại tập thể gửi Thanh tra Chính phủ — đơn dày ba mươi trang, đính kèm năm bài báo của TinDieuTra.vn làm tài liệu tham khảo.</p>

<p>Quân — phóng viên trẻ nhất nhóm — phấn khích: "Chị Nhi, mình viral rồi!"</p>

<p>"Viral không phải mục tiêu, Quân. Mục tiêu là hai trăm hộ dân được đền bù đúng giá. Chưa đạt thì chưa xong."</p>

<p>Mai gọi: "Chị, em có thêm nguồn tin mới — một cán bộ Sở Tài nguyên sẵn sàng khai báo, nhưng cần đảm bảo an toàn."</p>

<p>"Gặp riêng. Không ghi âm lần đầu. Xây dựng niềm tin trước. Bảo vệ nguồn tin là ưu tiên số một."</p>"""
    },
    {
        "title": "Chương 4: Bị Đe Dọa",
        "content": """<p>Tuần thứ ba sau khi loạt bài đăng, Nhi bắt đầu nhận tin nhắn.</p>

<p>Tin nhắn đầu tiên — từ số lạ, 2 giờ sáng: "Cô Nhi, cô nên dừng lại. Cô còn trẻ, đừng tự hại mình."</p>

<p>Tin nhắn thứ hai — ngày hôm sau: "Chúng tôi biết cô ở đâu. Quán cà phê Bụi Đời, phường 3. Cô ngồi bàn góc, uống sữa đá. Dừng lại."</p>

<p>Tin nhắn thứ ba — kèm ảnh: ảnh chụp cổng nhà mẹ Nhi ở Nghệ An, chụp từ xe ô tô, góc nhìn cho thấy người chụp đang đậu đối diện nhà.</p>

<p>Nhi đọc tin nhắn thứ ba, tay run. Không phải vì sợ cho mình — mà vì mẹ. Bà Nguyễn Thị Lan, sáu mươi hai tuổi, giáo viên nghỉ hưu, sống một mình ở Vinh — bà không biết gì về bài điều tra của con gái.</p>

<p>Nhi gọi mẹ ngay: "Mẹ ơi, mẹ có thấy ai lạ quanh nhà không?"</p>

<p>"Không, sao con hỏi vậy?"</p>

<p>"Không có gì. Mẹ khóa cửa cẩn thận nha."</p>

<p>Nhi gọi luật sư — Phạm Thị Hương, luật sư nhân quyền, chuyên bảo vệ nhà báo. Hương nói: "Nhi, screenshot tất cả tin nhắn, gửi email cho chị. Chị sẽ gửi đơn tố giác đe dọa đến Công an. Và từ giờ, em đổi chỗ làm việc — đừng ngồi cố định một quán."</p>

<p>Nhi đổi quán mỗi ngày — hôm nay Bụi Đời, ngày mai Highland, ngày kia quán bún bò gần chợ. Laptop luôn khóa mật khẩu hai lớp. USB chứa bài điều tra — cất hai bản: một trong ví, một gửi luật sư Hương giữ.</p>

<p>Quân hoảng: "Chị ơi, mình có nên dừng không?"</p>

<p>"Em sợ thì em dừng. Chị không ép ai."</p>

<p>"Em không sợ. Em chỉ... em chưa bao giờ bị đe dọa."</p>

<p>"Chị cũng vậy. Lần đầu tiên luôn sợ nhất. Nhưng nếu mình dừng vì sợ, thì hai trăm hộ dân kia phải sợ suốt đời — sợ mất đất, sợ không ai nói thay họ."</p>

<p>Quân im lặng. Rồi anh mở laptop, bắt đầu viết bài tiếp theo.</p>

<p>Mai gọi: "Chị, nguồn tin ở Sở Tài nguyên bị điều chuyển công tác đột ngột — chuyển từ phòng Quản lý đất sang phòng Hành chính. Họ đang bịt miệng."</p>

<p>"Em liên hệ nguồn tin, hỏi có muốn tiếp tục không. Nếu họ muốn dừng, mình tôn trọng. Nhưng nói với họ: lời khai của họ đã được mã hóa và lưu ở luật sư — không ai truy ngược được."</p>

<p>Nguồn tin quyết định tiếp tục. Vì cán bộ đó — Lê Minh Tâm, ba mươi lăm tuổi — cũng là dân Tỉnh H, cũng có bà con trong hai trăm hộ mất đất. Anh ta không khai vì can đảm — anh ta khai vì lương tâm.</p>"""
    },
    {
        "title": "Chương 5: Mẹ Và Trang Nhật Ký",
        "content": """<p>Nhi đi báo chí vì mẹ.</p>

<p>Bà Nguyễn Thị Lan — giáo viên văn trường THCS Vinh — dạy học ba mươi năm, lương bốn triệu mỗi tháng (trước khi nghỉ hưu). Bà dạy Nhi đọc sách từ năm bốn tuổi, viết văn từ năm sáu tuổi, và yêu sự thật từ năm mười hai tuổi — khi Nhi hỏi mẹ: "Mẹ ơi, sao cô giáo bảo con không được viết bài văn về nhà mình nghèo?"</p>

<p>"Vì người ta không muốn nghe sự thật, con ơi. Nhưng con cứ viết. Viết cho con, không phải viết cho cô giáo."</p>

<p>Nhi viết nhật ký từ năm mười hai — cuốn sổ bìa cứng màu xanh, mỗi tối viết một trang. Năm mười lăm, bà Lan đọc trộm — không phải vì tò mò, mà vì lo. Con gái bà viết về bất công ở trường, về thầy hiệu trưởng ăn bớt tiền quỹ phụ huynh, về chị bán nước ở cổng trường bị công an phường đuổi.</p>

<p>"Con ơi, con viết hay lắm. Nhưng mẹ sợ. Viết thế này, lớn lên con sẽ gặp rắc rối."</p>

<p>"Mẹ ơi, nếu không ai viết, ai sẽ biết?"</p>

<p>Bà Lan im lặng. Bà biết con gái đúng — nhưng bà cũng biết cái giá của "đúng" ở đất nước này có thể rất đắt.</p>

<p>Giờ đây, hai mươi tám tuổi, Nhi đang trả cái giá đó — bị sa thải, bị đe dọa, mẹ bị chụp ảnh cổng nhà. Và Nhi chưa dám nói cho mẹ biết.</p>

<p>Cho đến khi mẹ tự biết.</p>

<p>Bà Lan đọc TinDieuTra.vn — một đồng nghiệp cũ chia sẻ link trên Facebook: "Con bé Nhi viết hay ghê, xem kìa." Bà đọc cả năm kỳ, đọc rất chậm, đọc đi đọc lại.</p>

<p>Rồi bà gọi Nhi.</p>

<p>"Nhi, con bị sa thải rồi phải không?"</p>

<p>"Dạ, mẹ..."</p>

<p>"Con bị đe dọa phải không? Mẹ thấy có xe lạ đậu trước nhà mấy hôm rồi."</p>

<p>"Mẹ, con xin lỗi. Con không muốn mẹ lo."</p>

<p>Im lặng. Rồi bà Lan nói — giọng bình tĩnh, như thể bà đã suy nghĩ câu này rất lâu:</p>

<p>"Nhi ơi, con đừng xin lỗi. Con đang làm đúng thứ mà mẹ muốn dạy con suốt ba mươi năm: nói sự thật. Mẹ sợ — nhưng mẹ tự hào hơn là sợ."</p>

<p>Nhi khóc. Lần đầu tiên kể từ khi bị sa thải, cô khóc — không phải vì buồn, mà vì nhẹ. Vì có một người nói "mẹ tự hào" — và người đó là mẹ.</p>"""
    },
    {
        "title": "Chương 6: Nguồn Tin Được Bảo Vệ",
        "content": """<p>Thanh tra Chính phủ vào cuộc — nhưng không phải vì TinDieuTra.vn. Họ vào cuộc vì đơn khiếu nại của hai trăm hộ dân, kết hợp với đơn tố cáo ẩn danh từ nội bộ UBND Tỉnh H.</p>

<p>Và Phó Chủ tịch Nguyễn Đức Thắng — khi biết Thanh tra vào cuộc — phản công.</p>

<p>Thắng gửi công văn yêu cầu Công an Tỉnh H "điều tra trang web TinDieuTra.vn về hành vi đăng tải thông tin sai sự thật, gây hoang mang dư luận." Công an mời Nhi lên "làm việc" — một buổi hỏi cung trá hình, bốn tiếng đồng hồ, trong phòng nhỏ tường trắng, hai điều tra viên ngồi đối diện.</p>

<p>"Chị Nhi, ai cung cấp biên bản họp UBND cho chị?"</p>

<p>"Tôi không tiết lộ nguồn tin. Đây là quyền của nhà báo theo Luật Báo chí, Điều 25, Khoản 4."</p>

<p>"Chị không phải nhà báo nữa. Thẻ phóng viên đã bị thu."</p>

<p>"Tôi là công dân Việt Nam. Luật Báo chí bảo vệ mọi người cung cấp thông tin cho báo chí — không riêng người có thẻ."</p>

<p>Luật sư Hương ngồi cạnh Nhi — bà đã bay từ Hà Nội vào, ngồi im suốt buổi, nhưng mỗi khi điều tra viên hỏi câu vượt quá phạm vi, bà đặt tay lên bàn và nói: "Câu hỏi này vi phạm Điều 25 Luật Báo chí. Thân chủ tôi có quyền từ chối trả lời."</p>

<p>Bốn tiếng. Nhi không tiết lộ nguồn tin.</p>

<p>Ra khỏi trụ sở công an, Nhi ngồi trên ghế đá công viên, tay run. Quân chạy đến, đưa ly cà phê.</p>

<p>"Chị ổn không?"</p>

<p>"Ổn. Nhưng Quân, em kiểm tra ngay: nguồn tin Lê Minh Tâm ở Sở Tài nguyên có bị gì không?"</p>

<p>Quân gọi. Tâm vẫn an toàn — vì không ai biết anh ta là nguồn tin. Nhi đã mã hóa tất cả liên lạc với Tâm qua Signal — ứng dụng nhắn tin mã hóa đầu cuối. Tên Tâm trong hệ thống của Nhi là "Cây Bàng" — mã danh mà chỉ Nhi và luật sư Hương biết.</p>

<p>"Bảo vệ nguồn tin là giữ lời hứa," Nhi nói với Quân. "Nếu mình lộ một nguồn, không ai dám nói với mình nữa. Và không có nguồn tin, không có báo chí điều tra."</p>"""
    },
    {
        "title": "Chương 7: Đổ Domino",
        "content": """<p>Thanh tra Chính phủ công bố kết luận thanh tra sau ba tháng — kết luận dày năm mươi trang, xác nhận toàn bộ những gì TinDieuTra.vn đã đăng:</p>

<p>Một: Giá đền bù đất dự án Đông Hải thấp hơn giá thị trường từ năm mươi đến tám mươi lần — vi phạm Luật Đất đai.</p>

<p>Hai: Phó Chủ tịch Nguyễn Đức Thắng có cổ phần ẩn danh trong Tập đoàn Hoàng Gia thông qua công ty vỏ bọc — vi phạm Luật Phòng chống tham nhũng.</p>

<p>Ba: Tổng biên tập Trần Quốc Hùng nhận chỉ đạo miệng từ Phó Chủ tịch Thắng để "giết" bài điều tra — vi phạm Luật Báo chí.</p>

<p>Domino bắt đầu đổ.</p>

<p>Phó Chủ tịch Nguyễn Đức Thắng: bị đình chỉ chức vụ, chuyển hồ sơ sang Viện Kiểm sát truy tố tội "Lợi dụng chức vụ quyền hạn" và "Tham ô tài sản."</p>

<p>Chủ tịch Tập đoàn Hoàng Gia — Lê Hoàng Phúc: bị khởi tố tội "Đưa hối lộ" và "Vi phạm quy định về quản lý đất đai."</p>

<p>Tổng biên tập Trần Quốc Hùng: bị cách chức, chuyển sang vị trí không chức danh — kỷ luật nội bộ.</p>

<p>Giám đốc Sở Tài nguyên: bị kiểm điểm, cảnh cáo.</p>

<p>Hai trăm hộ dân: được Thanh tra kiến nghị đền bù bổ sung theo giá thị trường — tổng số tiền bổ sung: hai trăm bốn mươi tỷ đồng.</p>

<p>Tin tức lan khắp cả nước. Báo Tuổi Trẻ, VnExpress, Thanh Niên — tất cả đều đưa tin, và lần này, họ trích dẫn đúng nguồn: "Theo loạt bài điều tra của trang TinDieuTra.vn, do nhà báo Vũ Phương Nhi thực hiện."</p>

<p>Nhi đọc tin, không cười, không vui. Cô chỉ gọi cho nguồn tin "Cây Bàng" — Lê Minh Tâm:</p>

<p>"Anh Tâm, Thanh tra đã công bố. Anh an toàn."</p>

<p>"Chị Nhi, cảm ơn chị. Cảm ơn chị đã giữ lời hứa."</p>

<p>"Tôi hứa thì tôi giữ. Đó là quy tắc."</p>"""
    },
    {
        "title": "Chương 8: Giải Thưởng Báo Chí",
        "content": """<p>Hội Nhà báo Việt Nam trao Giải Báo chí Quốc gia hạng A cho loạt bài "Đất Đông Hải" — giải cao nhất, lần đầu tiên trao cho tác phẩm đăng trên trang tin độc lập, không thuộc bất kỳ tòa soạn chính thống nào.</p>

<p>Lễ trao giải ở Hà Nội — Nhà hát Lớn, sáng thứ Bảy. Nhi mặc áo dài trắng — chiếc áo dài mà mẹ may cho cô ngày tốt nghiệp đại học. Quân, Mai, Đức Anh ngồi hàng ghế thứ hai — ba phóng viên trẻ đã cùng cô xây TinDieuTra.vn từ quán cà phê.</p>

<p>Nhi đứng trên bục, cầm cúp, nhìn xuống khán phòng — ba trăm nhà báo, biên tập viên, tổng biên tập từ cả nước. Trong đó có Trần Quốc Hùng — cựu tổng biên tập, người đã giết bài và sa thải cô. Ông ngồi hàng cuối, không vỗ tay.</p>

<p>"Giải thưởng này không phải của tôi," Nhi nói. "Nó thuộc về hai trăm hộ dân Đông Hải — những người mất đất và không ai nói thay. Thuộc về nguồn tin đã chấp nhận rủi ro để khai báo. Thuộc về ba đồng nghiệp trẻ đã theo tôi dù không có lương, không có tòa soạn, không có gì ngoài WiFi quán cà phê và niềm tin rằng sự thật đáng để kể."</p>

<p>Vỗ tay.</p>

<p>"Và thuộc về mẹ tôi — bà Nguyễn Thị Lan, giáo viên văn trường THCS Vinh, người đã dạy tôi viết từ năm sáu tuổi và nói: 'Con cứ viết sự thật, kể cả không ai muốn nghe.' Mẹ, con viết rồi. Và có người nghe."</p>

<p>Bà Lan ngồi hàng ghế thứ ba — cạnh Quân và Mai. Bà khóc, tay ôm chiếc túi vải cũ, bên trong là cuốn nhật ký bìa xanh mà Nhi viết năm mười hai tuổi — bà mang theo từ Vinh, như bùa hộ mệnh.</p>

<p>Sau lễ trao giải, Hùng — cựu tổng biên tập — đến gặp Nhi ở hành lang.</p>

<p>"Nhi, anh sai. Anh lẽ ra phải đăng bài."</p>

<p>"Anh sai vì anh chọn sáu mươi người thay vì hai trăm người. Nhưng em hiểu — lựa chọn nào cũng có cái giá."</p>

<p>"Em còn giận anh không?"</p>

<p>"Em không giận. Em chỉ thất vọng — vì anh là người dạy em viết điều tra, và anh là người giết bài điều tra của em. Nhưng cuối cùng, bài vẫn đăng. Sự thật không chết — nó chỉ tìm đường khác."</p>"""
    },
    {
        "title": "Chương 9: Quay Về Tỉnh H",
        "content": """<p>Một năm sau giải Báo chí Quốc gia.</p>

<p>TinDieuTra.vn: tám phóng viên, hai trăm nghìn độc giả mỗi tháng, tài trợ bởi quỹ báo chí quốc tế và đóng góp của độc giả — không nhận quảng cáo, không nhận tài trợ từ doanh nghiệp hay chính quyền.</p>

<p>Nhi trở lại Tỉnh H — không phải để ở, mà để gặp hai trăm hộ dân Đông Hải.</p>

<p>Buổi sáng, cô đến nhà ông Bảy — bảy mươi tuổi, nông dân, người đã dẫn đầu đoàn khiếu nại. Ông ở nhà cấp bốn, sân trước trồng rau muống, sau nhà là ruộng lúa — mảnh ruộng duy nhất không bị thu hồi.</p>

<p>"Cháu Nhi! Vào nhà, vào nhà!"</p>

<p>Ông Bảy pha trà. Bà Bảy bưng bánh tráng nướng.</p>

<p>"Ông ơi, tiền đền bù bổ sung đã nhận chưa?"</p>

<p>"Nhận rồi, cháu. Mỗi hộ nhận thêm trung bình một tỷ hai — đúng giá thị trường. Hai trăm hộ đều nhận rồi."</p>

<p>"Ông dùng tiền làm gì?"</p>

<p>"Ông sửa nhà. Cho thằng Út đi học đại học. Và ông mua lại một mảnh đất nhỏ ở xã bên — để trồng lúa tiếp."</p>

<p>Nhi cười. Ông Bảy bảy mươi tuổi, mất đất, suýt mất tất cả — nhưng khi có tiền, ông mua đất trồng lúa. Vì ông là nông dân — đất là cuộc sống, lúa là hơi thở.</p>

<p>"Cháu Nhi, ông nói thiệt: nếu không có cháu, không ai biết chuyện ông. Hai trăm người mất đất — mà báo đài không ai đưa. Cháu là người đầu tiên."</p>

<p>"Ông ơi, cháu chỉ viết. Người đứng lên là ông và hai trăm hộ dân. Cháu chỉ cầm bút — ông cầm cuốc và đứng trước mặt họ."</p>

<p>Ông Bảy cười, rót thêm trà.</p>

<hr>

<p>Chiều hôm đó, Nhi đứng trước trụ sở tòa soạn báo Nhân Dân Tỉnh H — nơi cô từng làm việc bốn năm, nơi cô bị sa thải. Tấm biển "Tòa soạn Báo Nhân Dân Tỉnh H" vẫn treo trước cổng, sơn đỏ trên nền trắng.</p>

<p>Tổng biên tập mới — người thay Hùng — mời cô vào uống trà.</p>

<p>"Chị Nhi, tòa soạn muốn mời chị về — vị trí Phó Tổng biên tập phụ trách Điều tra."</p>

<p>Nhi uống trà, đặt tách xuống.</p>

<p>"Cảm ơn anh. Nhưng em không về."</p>

<p>"Tại sao?"</p>

<p>"Vì TinDieuTra.vn cần em hơn tòa soạn cần em. Và vì em đã hiểu: báo chí không cần tòa nhà, không cần biên chế, không cần ngân sách nhà nước. Báo chí chỉ cần một thứ: sự thật. Và sự thật thì ngồi ở quán cà phê cũng viết được."</p>

<p>Nhi bắt tay, rời tòa soạn. Bên ngoài, Quân đợi trên xe máy.</p>

<p>"Chị, đi đâu?"</p>

<p>"Quay lại quán cà phê. Có vụ mới ở Tỉnh K — Mai vừa gọi, nguồn tin khai có gian lận xây dựng cầu cao tốc."</p>

<p>Quân cười, nổ máy.</p>

<p>Nhi ngồi sau xe, laptop trong ba lô, gió thổi tóc bay. Cô không phải Tổng biên tập. Cô không có tòa nhà. Cô không có ngân sách ba mươi tỷ.</p>

<p>Cô chỉ có một cây bút, một laptop, ba đồng nghiệp, và niềm tin rằng sự thật — dù bị giết ở tòa soạn này — sẽ tìm đường sống ở nơi khác.</p>

<p>Vì sự thật không cần ai cho phép. Sự thật chỉ cần người dám viết.</p>"""
    }
]

story_data["chapters"] = chapters

with open("scratch/story_5582_rewrite.json", "w", encoding="utf-8") as f:
    json.dump(story_data, f, ensure_ascii=False, indent=2)

print("✅ Truyện 5582 viết xong — 9 CHƯƠNG!")
for i, ch in enumerate(chapters):
    print(f"  Ch{i+1}: {ch['title']} — {len(ch['content'])} chars")

print("\n📤 Uploading...")
url = "https://doctieuthuyet.com/overwrite_story_v13.php"
payload = json.dumps(story_data).encode('utf-8')
req = urllib.request.Request(url, data=payload, headers={'Content-Type': 'application/json'})
try:
    resp = urllib.request.urlopen(req, timeout=120)
    result = json.loads(resp.read().decode('utf-8'))
    print(f"  ✅ Success! ID={result['story_id']}, Chapters={result['chapters_count']}")
except Exception as e:
    print(f"  ❌ Error: {e}")

print("\n📊 Updating Excel...")
wb = openpyxl.load_workbook("danh_sach_truyen_doctieuthuyet.xlsx")
ws = wb.active
for r in range(5, ws.max_row+1):
    if ws.cell(row=r, column=2).value and str(ws.cell(row=r, column=2).value).strip() == "5582":
        ws.cell(row=r, column=6).value = 9
        ws.cell(row=r, column=12).value = "Phóng viên điều tra bị sa thải vì phanh phui tham nhũng đất đai. Lập tòa soạn độc lập từ quán cà phê, đăng loạt bài viral, Phó CT tỉnh lĩnh án, 200 hộ dân được đền bù."
        ws.cell(row=r, column=13).value = "REWRITE TOÀN BỘ: 8 chương quá ngắn → 9 CHƯƠNG ĐẦY ĐẶN"
        ws.cell(row=r, column=14).value = "☑️ Đã sửa"
        print(f"  ✅ Excel updated row {r}")
        break
wb.save("danh_sach_truyen_doctieuthuyet.xlsx")
print("\n✅ HOÀN THÀNH TRUYỆN 5582!")
