#!/usr/bin/env python3
"""
Upload fix_dup_chapters.php và gửi nội dung chương mới để cập nhật.
Nội dung được viết sẵn, không cần gọi AI API.
"""
import ftplib, requests, json, time

FTP_HOST = "51.79.53.190"; FTP_USER = "alotoinghe"; FTP_PASS = "Nghia234!"
WP_URL   = "https://doctieuthuyet.com"; SECRET = "ZEN_TRUYEN_2026_BYPASS"

# ─────────────────────────────────────────────────────────────────────────────
# NỘI DUNG CHƯƠNG MỚI (viết tay, không dùng AI API)
# ─────────────────────────────────────────────────────────────────────────────

CHAPTER_UPDATES = [

# ═══════════════════════════════════════════════════════════════════════════
# ID 2497 — Công Thức Thuốc Bị Cướp: Bẫy IPO Dược Phẩm Nghìn Tỷ
# Nhân vật: Nguyễn Đức Trí (dược sĩ), Lâm Gia Hân (CEO Hòa Phát)
# Phản diện: Minh (kẻ cướp công thức)
# ═══════════════════════════════════════════════════════════════════════════

{
"slug": "chuong-2-bay-thoi-gian",
"title": "Chương 2: Bẫy Thời Gian",
"content": """<p><strong>"Còn đúng hai mươi hai tiếng."</strong></p>
<p>Lâm Gia Hân đặt điện thoại xuống bàn, giọng bình thản đến đáng sợ. Nguyễn Đức Trí nhìn cô — CEO ba mươi hai tuổi của Hòa Phát Pharma — và lần đầu tiên anh thấy trong mắt người phụ nữ đó không phải ánh tự tin thường ngày, mà là một tia lo lắng bị kiểm soát rất kỹ.</p>
<p>"Nếu IPO được thông qua lúc chín giờ sáng mai," Hân nói, "mọi cáo buộc của anh về công thức bị cướp sẽ chìm nghỉm trong đống giấy tờ pháp lý của họ. Hội đồng quản trị sẽ gạt anh ra như gạt một hạt bụi."</p>
<p>Trí siết chặt tay. Hai năm nghiên cứu. Hai năm ăn ngủ trong phòng lab tại Đà Lạt, tay lạnh cóng vì điều hòa phải chỉnh thấp để bảo quản mẫu. Và giờ tất cả đang được người khác dùng để đổi lấy tiền tỷ.</p>
<p>"Anh có backup không?" Hân hỏi thẳng.</p>
<p>"Có. Toàn bộ dữ liệu thô được sync lên cloud mỗi đêm. Nhưng account đã bị khóa." Trí chạy ngón tay qua bàn phím laptop. "Ai đó đổi mật khẩu lúc hai giờ sáng hôm qua. Trùng với thời điểm Minh rời lab."</p>
<p>Hân khẽ nhướng mày. "Minh Dược?"</p>
<p>"Phó giám đốc R&amp;D. Người duy nhất ngoài tôi có quyền truy cập lab tầng B3." Trí nói, giọng đắng. "Tôi từng tin hắn như tin chính mình."</p>
<p>Im lặng bao trùm căn phòng khách sạn nhỏ. Bên ngoài cửa sổ, Đà Lạt lúc nửa đêm chìm trong sương mù dày đặc như bông gòn.</p>
<p>"Được." Hân đứng dậy, kéo ghế ngồi cạnh Trí, mở máy tính của cô. "Tôi có một người quen ở bộ phận bảo mật của nhà cung cấp cloud. Anh ta có thể mở recovery log — những file đã bị xóa trong vòng 48 giờ vẫn còn dấu vết." Cô gõ nhanh một tin nhắn. "Mười lăm phút."</p>
<p>Trí nhìn cô. "Sao cô làm vậy? Cô không biết tôi."</p>
<p>Hân không nhìn lên. "Công thức thuốc gan của anh đã được ba viện độc lập kiểm chứng. Tỷ lệ hồi phục enzyme gan tăng 340% so với phác đồ chuẩn." Cô dừng gõ, liếc sang anh. "Nếu nó thật — và tôi tin là thật — thì để nó rơi vào tay kẻ chỉ muốn bán cổ phiếu là tội ác. Không phải chỉ với anh. Với cả những bệnh nhân cần nó."</p>
<p>Trí không trả lời được. Cổ họng anh thắt lại.</p>
<p>Điện thoại Hân rung. Cô nhìn màn hình, gật đầu nhẹ.</p>
<p>"Recovery log vừa mở. Có bảy file bị xóa đêm qua." Cô đẩy máy tính về phía Trí. "Anh nhận ra cái nào không?"</p>
<p>Trí nhìn danh sách. Tim anh đập mạnh khi thấy tên file thứ ba: <em>Formula_LG_v8_FINAL_encrypted.zip</em>.</p>
<p>"Đó là bản hoàn chỉnh." Giọng anh run nhẹ. "Bản mã hóa. Chỉ có tôi biết key."</p>
<p>"Tốt." Hân gõ ngay. "Tôi download về. Anh giải mã đi." Cô đứng dậy, đi về phía tủ lạnh, lấy ra hai chai nước. "Đêm nay sẽ dài. Và anh cần đầu óc tỉnh táo."</p>
<p>Trí nhận chai nước, nhìn người phụ nữ trước mặt. Cô không hỏi thêm, không do dự. Chỉ làm. Như thể đây là điều hiển nhiên nhất trên đời.</p>
<p><strong>Còn hai mươi mốt tiếng bốn mươi phút.</strong></p>
<p>Cuộc đua đã bắt đầu thật sự.</p>"""
},

{
"slug": "chuong-3-nhung-manh-ghep-bat-ngo",
"title": "Chương 3: Những Mảnh Ghép Bất Ngờ",
"content": """<p>Ba giờ sáng. Phòng khách sạn tràn ngập ánh đèn màn hình.</p>
<p>Nguyễn Đức Trí gõ key giải mã lần thứ tư. Lần này file mở. Dữ liệu thô tràn ra màn hình — hàng nghìn dòng kết quả thử nghiệm, biểu đồ enzyme, ảnh mô gan bệnh nhân.</p>
<p>"Nguyên vẹn." Anh thở phào. "Toàn bộ còn nguyên."</p>
<p>Lâm Gia Hân ngồi bên cạnh, đang điện thoại với ai đó bằng giọng thấp. Cô cúp máy, quay sang anh: "Có tin mới. Nhưng không phải tin tốt."</p>
<p>Trí ngẩng đầu.</p>
<p>"Người của tôi theo dõi văn phòng Minh Dược suốt đêm nay." Hân đặt điện thoại xuống bàn. "Lúc hai giờ, có một xe không biển số đến đón hắn. Đi hướng sân bay Liên Khương."</p>
<p>Trí đứng bật dậy. "Hắn bỏ trốn?"</p>
<p>"Chưa chắc. Có thể hắn đang đến gặp đối tác." Hân bình tĩnh. "IPO không phải trò một người chơi. Hắn cần ai đó đứng sau. Ai đó có đủ ảnh hưởng để ép ủy ban chứng khoán thông qua trong vòng một đêm."</p>
<p>Trí ngồi xuống, đầu óc quay cuồng. Hắn chạm vào màn hình, vuốt qua các file đã giải mã. Và dừng lại.</p>
<p>"Hân." Anh gọi khẽ. "Nhìn cái này."</p>
<p>Trong thư mục thứ mười hai, nằm lẫn giữa các file dữ liệu thô, là một file ảnh. Tên file: <em>mtg_0312_scan.jpg</em>. Một trang biên bản cuộc họp, ngày ba mươi mốt tháng một.</p>
<p>Cả hai cúi xuống đọc.</p>
<p>Biên bản cuộc họp giữa Minh Dược và một công ty đầu tư có tên <em>Sino-Delta Capital</em>. Nội dung: chuyển nhượng quyền sở hữu trí tuệ công thức LG-v8 với giá sáu mươi triệu đô la Mỹ, thanh toán qua tài khoản tại Singapore.</p>
<p>Ngày ký: một tuần trước khi Trí bị đuổi khỏi lab.</p>
<p>Trí cảm thấy máu dồn lên đầu. "Hắn đã bán trước khi cướp. Hắn lên kế hoạch từ lâu rồi."</p>
<p>"Và file này vẫn còn trong cloud của anh." Hân giọng điều tĩnh như mặt nước trước bão. "Anh có bằng chứng gốc về giao dịch này. Sino-Delta Capital sẽ không muốn cái tên đó bị kéo ra công khai trong một vụ kiện — họ đang cần thị trường Việt Nam."</p>
<p>Trí nhìn cô. "Cô định làm gì với thông tin này?"</p>
<p>Hân đã cầm điện thoại. "Gọi cho luật sư. Và một phóng viên tôi biết ở báo Đầu Tư." Ánh mắt cô sắc lại. "Anh vừa tìm ra mảnh ghép quan trọng nhất. Bây giờ chúng ta cần ráp chúng lại trước chín giờ sáng."</p>
<p><strong>Còn mười tám tiếng.</strong></p>"""
},

{
"slug": "chuong-4-cuoc-dua-chong-thoi-gian-2",
"title": "Chương 4: Cuộc Đua Chống Thời Gian",
"content": """<p>Sáu giờ sáng. Đà Lạt vừa le lói ánh bình minh.</p>
<p>Nguyễn Đức Trí và Lâm Gia Hân chia nhau hai hướng.</p>
<p>"Anh đến Cục Sở Hữu Trí Tuệ tại TP.HCM." Hân trao cho Trí một phong bì dày. "Trong đó có đơn yêu cầu tạm hoãn đăng ký sáng chế khẩn cấp — luật sư tôi soạn lúc bốn giờ sáng. Anh cần nộp trực tiếp trước tám giờ, khi cửa vừa mở." Cô nhìn đồng hồ. "Chuyến bay sớm nhất rời Liên Khương lúc sáu rưỡi. Anh có hai mươi phút."</p>
<p>"Còn cô?" Trí cầm phong bì.</p>
<p>"Tôi đến Ủy Ban Chứng Khoán. Có người tôi cần gặp mặt trực tiếp." Hân khoác áo, khóa vali nhỏ gọn. "Nếu chúng ta làm đúng, IPO sẽ bị đình chỉ trước khi chuông mở cửa buổi chiều."</p>
<p>Trí gật đầu. Không còn gì để nói — chỉ còn hành động.</p>
<p>---</p>
<p>Chín giờ hai mươi. Sảnh Cục Sở Hữu Trí Tuệ, tầng bốn, tòa nhà cao ốc trên đường Đinh Tiên Hoàng.</p>
<p>Trí đứng trước cửa phòng tiếp nhận hồ sơ, nhìn tấm biển ghi <em>Tạm ngưng tiếp nhận hồ sơ khẩn từ 9:00 — 10:30</em>.</p>
<p>Anh nghiến răng.</p>
<p>Anh nhìn quanh. Một nhân viên đang đi qua, tay cầm xấp hồ sơ dày. Trí bước tới:</p>
<p>"Xin lỗi anh. Tôi cần gặp trưởng phòng tiếp nhận. Trường hợp khẩn — có nguy cơ vi phạm sở hữu trí tuệ liên quan đến đợt IPO đang diễn ra sáng nay."</p>
<p>Người nhân viên dừng lại, nhìn Trí một giây. "Anh chờ."</p>
<p>Mười hai phút sau, trưởng phòng tiếp nhận hồ sơ — một phụ nữ khoảng năm mươi tuổi, mắt kính gọng vàng — mời Trí vào phòng.</p>
<p>Trí trải toàn bộ bằng chứng lên bàn: file giải mã nguyên bản, biên bản cuộc họp với Sino-Delta Capital, log cloud recovery có timestamp, và bản phân tích độc lập của ba viện nghiên cứu.</p>
<p>Người phụ nữ đọc. Im lặng kéo dài năm phút.</p>
<p>"Anh có hai nhân chứng không?" bà hỏi.</p>
<p>Điện thoại Trí rung. Tin nhắn từ Hân: <em>UBCK đồng ý xem xét. Cần một nhân chứng nội bộ từ phía lab. Anh có ai không?</em></p>
<p>Trí gõ ngón tay lên bàn. Một cái tên hiện ra trong đầu anh — người anh đã không nghĩ đến suốt hai ngày qua.</p>
<p>Hoàng — kỹ thuật viên lab, người giao ca cuối cùng đêm Minh Dược lấy công thức.</p>
<p>Anh gọi ngay.</p>
<p>Hồi âm sau hai tiếng chuông: "Anh Trí... Em biết anh sẽ gọi. Em đã quay lại cảnh đó bằng camera điện thoại cá nhân. Em sợ quá không dám đưa. Nhưng nếu anh cần..."</p>
<p>"Em cần đến đây ngay bây giờ." Trí giữ giọng bình tĩnh dù tim anh đang đập loạn. "Mang theo mọi thứ em có."</p>
<p><strong>Còn chín tiếng.</strong></p>
<p>Những mảnh ghép cuối cùng đang hội tụ.</p>"""
},

{
"slug": "chuong-6-bay-ipo-cuoc-chay-dua-thoi-gian",
"title": "Chương 6: Bẫy IPO — Cuộc Chạy Đua Thời Gian",
"content": """<p>Bảy giờ tối. Trung tâm hội nghị Dalat Palace.</p>
<p>Nguyễn Đức Trí đứng ngoài hành lang, nhìn qua cửa kính vào khán phòng đang dần chật kín người. Vest đen mượn từ Hân, tie màu xanh đậm. Trông anh như một nhà đầu tư thứ thiệt.</p>
<p>Bên trong, banner của cuộc ra mắt IPO căng rộng phía sau sân khấu: <em>LG-Pharma — Công thức đột phá cho ngành dược Việt Nam</em>.</p>
<p>Dạ dày Trí quặn lại.</p>
<p>"Badge của anh." Hân đứng kế bên, dúi vào tay anh tấm thẻ nhựa có logo một quỹ đầu tư. "Tôi mượn từ đối tác. Không ai kiểm tra ảnh trong sự kiện này." Cô nhìn đồng hồ. "Chín mươi phút nữa họ bắt đầu phiên hỏi đáp nhà đầu tư. Đó là cửa sổ duy nhất của chúng ta."</p>
<p>"Minh Dược có ở đây không?"</p>
<p>"Đang trong phòng VIP, tầng hai." Hân khẽ gật. "Cùng với ba người từ Sino-Delta Capital và hai đại diện từ công ty chứng khoán bảo lãnh." Cô ngừng lại. "Anh sẵn sàng chưa?"</p>
<p>Trí nhìn vào khán phòng một lần nữa. Gần hai trăm nhà đầu tư, phóng viên, đại diện từ các quỹ. Tất cả sắp rót tiền vào một sản phẩm được xây trên nền tảng ăn cắp.</p>
<p>"Sẵn sàng."</p>
<p>Họ đi vào.</p>
<p>Mươi lăm phút sau, Trí ngồi ở hàng ghế thứ sáu từ trái, laptop mở, tai nghe cắm một bên. Hân ngồi ở hàng sau, điện thoại cầm sẵn. Trên sân khấu, phát ngôn viên của LG-Pharma đang trình bày về "đột phá lâm sàng" và "công thức độc quyền".</p>
<p>Mỗi từ họ nói là một nhát dao.</p>
<p>Điện thoại Trí rung. Tin nhắn từ luật sư: <em>Lệnh tạm hoãn đã được nộp. Nhưng tòa chưa phê duyệt — thẩm phán đang xem xét tối nay. Không đảm bảo trước 9 giờ sáng mai.</em></p>
<p>Trí gõ phản hồi: <em>Chúng tôi sẽ xử lý tại đây. Giữ mọi thứ sẵn sàng.</em></p>
<p>Hân chuyển tiếp một file qua Airdrop: đoạn video Hoàng — kỹ thuật viên lab — quay lén từ điện thoại, rõ mặt Minh Dược lấy ổ cứng mã hóa lúc một giờ mười bảy sáng.</p>
<p>Cùng với biên bản cuộc họp với Sino-Delta Capital. Cùng với log recovery có timestamp. Cùng với báo cáo độc lập của ba viện.</p>
<p>Tất cả đã ở đây, trong chiếc laptop nhỏ trên đùi anh.</p>
<p>Trên sân khấu, người MC bắt đầu: "Và bây giờ, chúng tôi mời các quý vị nhà đầu tư đặt câu hỏi—"</p>
<p>Tay Trí đã giơ lên.</p>"""
},

{
"slug": "chuong-7-duong-bat-loi-va-bang-chung-dinh-menh",
"title": "Chương 7: Đường Bất Lối và Bằng Chứng Định Mệnh",
"content": """<p>Khi Trí đứng dậy, cả khán phòng quay nhìn anh.</p>
<p>"Tên tôi là Nguyễn Đức Trí." Giọng anh vang đều, không run. "Tôi là tác giả gốc của công thức LG-v8 mà các ông đang trình bày tối nay như tài sản của mình."</p>
<p>Tiếng xì xào lan ra. Trên sân khấu, phát ngôn viên khựng lại.</p>
<p>Từ tầng hai, qua cửa sổ kính mờ, Minh Dược nhìn xuống. Khuôn mặt hắn biến sắc.</p>
<p>"Tôi có bằng chứng." Trí mở laptop, kết nối với màn hình trình chiếu phụ phía bên trái sân khấu — Hân đã cài sẵn thiết bị wireless lúc vào phòng. Màn hình bật lên: đoạn video từ camera điện thoại Hoàng, rõ nét, timestamp hiển thị đỏ ở góc trái.</p>
<p>Cả hội trường im bặt.</p>
<p>Minh Dược trên màn hình, đội mũ kéo thấp, tay cầm ổ cứng của phòng lab B3. Đồng hồ tường phía sau chỉ một giờ mười bảy sáng.</p>
<p>"Đây là biên bản cuộc họp ngày ba mươi mốt tháng một." Trí chuyển slide. Trang hợp đồng với Sino-Delta Capital hiện ra. "Công thức bị bán trước khi tôi bị đuổi việc. Và đây là log server cloud — timestamp ghi nhận toàn bộ dữ liệu gốc mang tên tôi."</p>
<p>Một phóng viên ngồi hàng đầu bật dậy, giơ máy ảnh lên.</p>
<p>Từ góc phải khán phòng, hai người đàn ông mặc vest đứng dậy — bảo vệ sự kiện. Nhưng trước khi họ tiến đến nơi Trí đứng, một tiếng nói khác cắt ngang khán phòng:</p>
<p>"Dừng lại."</p>
<p>Lâm Gia Hân đứng dậy ở hàng sau, điện thoại đưa lên. "Tôi là Lâm Gia Hân, CEO Hòa Phát Pharmaceutical. Chúng tôi vừa nhận được xác nhận từ Ủy Ban Chứng Khoán — phiên giao dịch IPO của LG-Pharma đã bị tạm đình chỉ để điều tra, hiệu lực từ hai mươi hai giờ hôm nay."</p>
<p>Cô giơ điện thoại lên đủ để những người xung quanh nhìn thấy màn hình — email chính thức từ UBCKNN, con dấu đỏ, chữ ký số.</p>
<p>Cả hội trường vỡ ra.</p>
<p>Tiếng ghế kéo. Tiếng máy ảnh loạt xoạt. Tiếng ai đó nói to bằng tiếng Anh về phía những người từ Sino-Delta Capital đang tái mặt nhìn nhau.</p>
<p>Trên tầng hai, cửa phòng VIP mở ra. Minh Dược bước ra hành lang, nhìn xuống khán phòng — và bắt gặp ánh mắt Nguyễn Đức Trí đang nhìn thẳng lên phía hắn.</p>
<p>Hai năm. Anh đã chờ khoảnh khắc này hai năm.</p>
<p>"Bằng chứng định mệnh." Hân đứng cạnh Trí, giọng thấp. "Giờ thì không còn đường nào thoát cho hắn nữa."</p>"""
},

# ═══════════════════════════════════════════════════════════════════════════
# ID 2313 — Cướp Mã Nguồn Nghìn Tỷ, Kích Hoạt Bẫy Chôn Vùi Tập Đoàn
# Nhân vật: Phạm Minh Đức, Hoàng Thế Vinh (phản diện), Triệu Vy Linh
# ═══════════════════════════════════════════════════════════════════════════

{
"slug": "chuong-7-bay-nguoc-do-mau",
"title": "Chương 7: Bẫy Ngược — Đổ Máu",
"content": """<p>Phòng server tầng hầm của CyberShield. Mười một giờ đêm.</p>
<p>Hoàng Thế Vinh đứng trước màn hình, nhìn dòng chữ đỏ nhấp nháy: <em>SYSTEM LOCK — UNAUTHORIZED ACCESS DETECTED</em>.</p>
<p>Ba tiếng trước, hắn đã kích hoạt toàn bộ hệ thống mới — cái mà hắn tưởng là mã nguồn hoàn chỉnh của CyberShield. Nhưng ngay khi server chạy lần đầu, toàn bộ dữ liệu khách hàng bắt đầu tự mã hóa ngược. Không phải virus. Không phải bug.</p>
<p>Đây là bẫy.</p>
<p>"Mày làm cái gì vậy, Đức?" Vinh quay sang Triệu Vy Linh — người phụ nữ hắn thuê để theo dõi Đức suốt sáu tháng qua. "Mày nói mã nguồn đã hoàn chỉnh!"</p>
<p>Vy Linh đứng yên, tay khoanh trước ngực. "Tôi nói tôi có thể lấy được mã nguồn. Tôi không nói đó là phiên bản thật."</p>
<p>Vinh trợn mắt. "Cái gì—"</p>
<p>"Anh Vinh." Giọng cô lạnh. "Anh có biết tại sao tôi chấp nhận làm việc cho anh với cái giá rẻ như vậy không?"</p>
<p>Cửa phòng server mở ra. Phạm Minh Đức bước vào, sau lưng là hai người từ Cục An Ninh Mạng, huy hiệu kẹp trước ngực.</p>
<p>Vinh lùi lại, lưng chạm vào rack server.</p>
<p>"Mày—" Hắn nhìn Đức, rồi nhìn Vy Linh, rồi lại nhìn Đức. "Mày thuê cô ta từ đầu?"</p>
<p>"Không." Đức lắc đầu, tiến thêm một bước. "Vy Linh đến tìm tôi. Cô ấy là người đầu tiên biết anh đang lên kế hoạch cướp mã nguồn — vì anh đã tiếp cận cô ấy trước. Anh muốn cô ấy giả vờ là gián điệp của tôi để lấy lòng tin." Anh dừng lại. "Nhưng cô ấy chọn ngược lại."</p>
<p>Vy Linh móc từ túi áo ra một ổ USB. "Toàn bộ cuộc trò chuyện giữa tôi và anh Vinh. Sáu tháng. Bao gồm lệnh chuyển khoản hai triệu đô la đặt cọc từ tài khoản Cayman Islands của anh." Cô đưa ổ USB cho người của Cục An Ninh Mạng. "Và đây là ba mảnh mã nguồn thật. Đức giấu ở ba nơi khác nhau — phòng server của viện nghiên cứu, máy chủ dự phòng ở Hà Nội, và một node blockchain không thể xóa."</p>
<p>Vinh nhìn Đức. Trong ánh đèn xanh của phòng server, khuôn mặt hắn trắng bệch như tờ giấy.</p>
<p>"Mày đã tính toán việc này từ lúc nào?"</p>
<p>Đức nhìn hắn thẳng vào mắt. "Từ ngày mày bắt đầu hỏi tôi quá nhiều về kiến trúc hệ thống. Sáu tháng trước."</p>
<p>Bẫy được gài từ trước khi cuộc phản bội bắt đầu. Và tối nay, nó đã sập xuống đúng lúc.</p>
<p>Người của Cục An Ninh Mạng bước tới. "Hoàng Thế Vinh. Mời anh theo chúng tôi."</p>"""
},

# ═══════════════════════════════════════════════════════════════════════════
# ID 2658 — Chàng Rể Ngọc Linh Lật Kèo Cứu Bị Cướp
# Nhân vật: Trần Hoàng Vũ (nhà nghiên cứu sâm), Nguyễn Minh Thư (CFO),
#           Gia đình Phạm (phản diện), sâm Ngọc Linh nhân tạo độc sau 30 ngày
# ═══════════════════════════════════════════════════════════════════════════

{
"slug": "chuong-2-con-bao-tu-gia-dinh-pham-gia",
"title": "Chương 2: Cơn Bão Từ Gia Đình Phạm Gia",
"content": """<p>Sáng sớm ngày hôm sau, văn phòng của Nguyễn Minh Thư tại Kon Tum.</p>
<p>Trần Hoàng Vũ đặt điện thoại xuống bàn, mặt tái đi.</p>
<p>"Lô hàng đầu tiên đã xuất cảng." Anh nói, giọng khan đặc. "Hai mươi tấn sâm nhân tạo. Cảng Hải Phòng, tàu rời bến lúc sáu giờ sáng nay. Đến Thụy Sĩ trong mười hai ngày."</p>
<p>Nguyễn Minh Thư ngừng gõ bàn phím. Cô nhìn thẳng vào mặt Vũ, đôi mắt sắc lại. "Mười hai ngày. Sâm sẽ độc sau ba mươi ngày. Vậy người tiêu dùng sẽ có mười tám ngày an toàn từ khi nhận hàng."</p>
<p>"Đủ để họ dùng. Đủ để họ tin tưởng vào chất lượng ban đầu." Vũ ngồi xuống ghế, hai tay ôm mặt. "Và khi độc tố tích lũy đến ngưỡng nguy hiểm... sẽ không ai trace được nguồn gốc kịp thời."</p>
<p>Im lặng nặng nề.</p>
<p>"Gia đình Phạm không biết sâm sẽ độc?" Thư hỏi.</p>
<p>"Họ biết." Vũ ngẩng đầu. "Tôi tìm thấy email nội bộ trong máy tính của Phạm Tuấn Kiệt — hắn đã thuê một phòng lab riêng để kiểm tra. Báo cáo ghi rõ: enzyme phân hủy sau hai mươi tám đến ba mươi hai ngày ở nhiệt độ thông thường." Giọng anh trở nên lạnh. "Họ biết và vẫn xuất."</p>
<p>Thư đứng dậy, đi đến cửa sổ nhìn ra dãy núi xanh xa. Tay cô siết chặt vào thành cửa.</p>
<p>"Chúng ta cần dừng tàu đó lại."</p>
<p>"Tàu đã ra khơi sáu tiếng rồi."</p>
<p>"Không phải tàu đó." Thư quay lại, mắt cô sáng lên. "Lô hàng thứ hai. Theo lịch xuất khẩu tôi hack được từ hệ thống của Phạm Gia tối qua — còn ba lô nữa, lô gần nhất xuất sau bốn ngày." Cô mở laptop. "Chúng ta cần bằng chứng phân tích độc tố để yêu cầu cơ quan thú y kiểm định trước khi họ thông quan."</p>
<p>Vũ nhìn cô. Trong ba năm nghiên cứu sâm Ngọc Linh, anh đã quen với những người chỉ xem sâm như hàng hóa. Nguyễn Minh Thư là người đầu tiên nhìn vào vấn đề như nhìn vào một tội ác cần phải dừng lại.</p>
<p>"Tôi cần vào lại phòng lab của mình." Anh đứng dậy. "Mẫu đối chứng vẫn còn đó — bằng chứng sâm nhân tạo của Phạm Gia sẽ cho thấy chính xác độc tố hình thành ở ngày mấy."</p>
<p>"Phòng lab đã bị niêm phong." Thư nhíu mày.</p>
<p>"Tôi biết một lối vào phụ." Vũ khoác áo. "Họ niêm phong cửa chính. Nhưng đường hầm thoát hiểm tầng hầm thì không."</p>
<p>Thư nhìn anh một giây, rồi cũng đứng dậy lấy chìa khóa xe.</p>
<p>"Đi."</p>"""
},

{
"slug": "chuong-3-doi-dau-cung-thoi-gian",
"title": "Chương 3: Đối Đầu Cùng Thời Gian",
"content": """<p>Đường hầm thoát hiểm tầng hầm của Trung Tâm Nghiên Cứu Sâm Ngọc Linh.</p>
<p>Trần Hoàng Vũ dẫn Nguyễn Minh Thư đi trong bóng tối, chỉ có đèn pin điện thoại soi đường. Mùi đất ẩm và kẽm gỉ. Tiếng drip drip của nước nhỏ giọt đâu đó trong vách tường.</p>
<p>"Còn xa không?" Thư thì thầm.</p>
<p>"Mười lăm mét nữa." Vũ đếm bước. "Cửa phụ vào kho mẫu lạnh. Họ không biết lối này vì tôi tự đào thêm năm ngoái — lúc cúp điện liên tục mùa mưa."</p>
<p>Cửa sắt hiện ra. Vũ rút chìa khóa — một chiếc chìa cũ kỹ gỉ sét mà anh giữ trong ví suốt ba năm.</p>
<p>Kho mẫu lạnh, bốn độ C. Tủ lạnh xếp thành hai hàng dài, mỗi tủ dán nhãn ngày tháng và mã mẫu.</p>
<p>Vũ tìm tủ số mười bảy. Mở ra. Bên trong: hàng chục ống nghiệm nhỏ, mỗi ống là một mẫu sâm từ các lô khác nhau — bao gồm ba mẫu anh đã lấy từ lô sâm nhân tạo của Phạm Gia trước khi bị đuổi khỏi lab.</p>
<p>"Mẫu đối chứng." Anh lấy ba ống, đưa cho Thư. "Cần phân tích enzyme ngay hôm nay."</p>
<p>Thư cầm ống nghiệm, rút điện thoại. "Viện Pasteur Đà Nẵng. Tôi có quen trưởng phòng phân tích — cô ấy có thể cho kết quả trong sáu tiếng nếu tôi xin ưu tiên."</p>
<p>Tiếng bước chân phía cửa chính.</p>
<p>Cả hai đứng im.</p>
<p>Bảo vệ — hai người, đang kiểm tra vòng. Ánh đèn pin quét qua khe cửa tủ lạnh.</p>
<p>Vũ nhìn Thư. Cô đã cho ba ống mẫu vào túi áo khoác, khóa kéo lại không một tiếng động. Khuôn mặt cô bình tĩnh tuyệt đối.</p>
<p>Họ chờ. Ba phút. Năm phút.</p>
<p>Bước chân bảo vệ đi xa dần.</p>
<p>Vũ ra hiệu. Hai người rút lui theo đường hầm, lần này nhanh hơn.</p>
<p>Khi ra đến ngoài, ánh nắng buổi sáng chiếu thẳng vào mặt. Vũ nhìn đồng hồ: tám giờ hai mươi.</p>
<p>"Nếu lấy kết quả phân tích lúc hai giờ chiều," anh tính, "còn kịp nộp cho Chi Cục Kiểm Dịch trước khi họ đóng cửa lúc năm giờ."</p>
<p>"Kịp." Thư đã gọi điện, giọng bình thản như đang đặt lịch họp. "Chị Lan ơi, em cần chị chạy phân tích enzyme khẩn... Vâng, có mẫu đối chứng đầy đủ... Kết quả trước hai giờ được không ạ?"</p>
<p>Cô cúp máy, nhìn Vũ. "Được. Hai giờ kém mười lăm."</p>
<p>Vũ thở ra. Đây không phải chiến thắng — chỉ là một bước trong cuộc đua chưa biết hồi kết. Phạm Gia có luật sư, có quan hệ, có tiền. Nhưng họ có thứ mà tiền không mua được: sự thật trong ba ống nghiệm nhỏ bằng ngón tay cái.</p>
<p>"Đi." Anh bước về phía xe. "Thời gian không chờ ai."</p>"""
},

]  # end CHAPTER_UPDATES

# ─────────────────────────────────────────────────────────────────────────────

def run():
    # Upload PHP
    print("Uploading fix_dup_chapters.php...")
    ftp = ftplib.FTP(FTP_HOST, timeout=30)
    ftp.login(FTP_USER, FTP_PASS)
    with open("fix_dup_chapters.php", "rb") as f:
        ftp.storbinary("STOR fix_dup_chapters.php", f)
    ftp.quit()
    print("Uploaded.")
    time.sleep(2)

    # Call PHP with all updates
    print(f"Sending {len(CHAPTER_UPDATES)} chapter updates...")
    payload = {"secret_token": SECRET, "updates": CHAPTER_UPDATES}
    res = requests.post(f"{WP_URL}/fix_dup_chapters.php", json=payload, timeout=180)
    print(f"HTTP {res.status_code}")
    data = res.json()
    print(json.dumps(data, ensure_ascii=False, indent=2))

    # Cleanup
    ftp = ftplib.FTP(FTP_HOST, timeout=30)
    ftp.login(FTP_USER, FTP_PASS)
    ftp.delete("fix_dup_chapters.php")
    ftp.quit()
    print("Cleaned up. Done.")

if __name__ == "__main__":
    run()
