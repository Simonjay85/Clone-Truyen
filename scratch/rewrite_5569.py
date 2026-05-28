import json, urllib.request, openpyxl

story_data = {
    "secret_token": "ZEN_TRUYEN_2026_BYPASS",
    "story_id": 5569,
    "title": "Bị Khinh Là Thợ Sửa Đồng Hồ Vỉa Hè, Tôi Chế Tạo Đồng Hồ Luxury Made In Vietnam Khiến Thụy Sĩ Phải Kinh Ngạc",
    "intro": "<p>Ngô Hải Sơn — ba mươi tuổi, thợ sửa đồng hồ vỉa hè ở phố Hàng Đào, Hà Nội — bị giới đồng hồ cao cấp Việt Nam cười nhạo khi tuyên bố sẽ chế tạo đồng hồ cơ khí luxury Made in Vietnam.</p>\n<p>\"Thằng sửa pin đồng hồ Casio mà đòi làm Rolex à?\" — đó là câu mà chủ cửa hàng đồng hồ lớn nhất Hà Nội nói trước mặt Sơn tại triển lãm đồng hồ năm 2019.</p>\n<p>Nhưng Sơn có một thứ mà họ không có: đôi bàn tay thừa hưởng từ bố — thợ sửa đồng hồ Liên Xô bốn mươi năm — và ước mơ điên rồ: đưa đồng hồ Việt Nam lên sàn Baselworld, Thụy Sĩ.</p>",
    "author": "Ngô Hải Sơn",
    "chapters": []
}

chapters = [
    {
        "title": "Chương 1: Tiếng Cười Của Giới Đồng Hồ",
        "content": """<p>Triển lãm Đồng Hồ & Trang Sức Việt Nam 2019, Trung tâm Hội nghị Quốc gia Hà Nội.</p>

<p>Ngô Hải Sơn đứng trước gian hàng của mình — gian nhỏ nhất triển lãm, ba mét vuông, tường dán giấy trắng, bàn kính trưng bày năm chiếc đồng hồ cơ khí mà anh tự chế tạo trong gian bếp nhà trọ ở phố Hàng Bông.</p>

<p>Năm chiếc đồng hồ — vỏ thép không gỉ đánh bóng thủ công, mặt số sơn mài đen (Sơn thuê nghệ nhân sơn mài Hà Thái làm riêng), kim vàng, dây da bò Ý. Mỗi chiếc có tên: SH-01, SH-02, SH-03, SH-04, SH-05. Bộ máy bên trong: movement ETA 2824 nhập từ Thụy Sĩ, nhưng vỏ, mặt số, kim, và hoàn thiện hoàn toàn Made in Vietnam.</p>

<p>Giá bán: mười hai triệu đồng mỗi chiếc — rẻ hơn mười lần so với đồng hồ Thụy Sĩ cùng bộ máy, nhưng đắt gấp mười lần đồng hồ Trung Quốc.</p>

<p>Không ai mua. Không ai dừng lại.</p>

<p>Trừ một nhóm — ba ông chủ cửa hàng đồng hồ lớn nhất Hà Nội: Nguyễn Hoàng Long (SaiGon Watch), Phạm Trung Kiên (LuxTime), và Đặng Minh Tuấn (Tuấn Watch). Họ dừng lại, cầm chiếc SH-01 lên, xoay, nhìn — rồi cười.</p>

<p>"Thằng này là ai?" Long hỏi.</p>

<p>"Thợ sửa đồng hồ vỉa hè ở Hàng Đào," Kiên nói. "Sửa pin Casio, thay dây đồng hồ bốn mươi nghìn."</p>

<p>Long cười to: "Thằng sửa pin Casio mà đòi làm Rolex à? Movement mua ETA rồi nhét vào vỏ tự làm — cũng gọi là luxury? Anh em ơi, xe đạp lắp động cơ ô tô thì cũng không phải ô tô."</p>

<p>Ba người cười, bỏ đi.</p>

<p>Sơn đứng sau quầy, tay nắm chặt mép bàn, mặt đỏ — không phải vì xấu hổ, mà vì nhịn. Anh muốn đuổi theo, muốn nói: "Tôi không dùng ETA mãi. Tôi đang thiết kế bộ máy riêng. Tôi chỉ cần thời gian." Nhưng anh không nói — vì nói mà chưa làm được thì chỉ là nói suông.</p>

<p>Tối hôm đó, Sơn mang năm chiếc đồng hồ về phòng trọ, đặt lên bàn làm việc. Anh ngồi nhìn chúng — năm chiếc đồng hồ đẹp nhất anh từng làm, và không ai thèm mua.</p>

<p>Vợ anh — Trần Thị Hạnh, hai mươi tám tuổi, kế toán công ty xây dựng — pha trà, ngồi cạnh.</p>

<p>"Anh ơi, đừng buồn. Họ chưa hiểu đồng hồ anh tốt đến đâu."</p>

<p>"Họ không cần hiểu. Họ chỉ cần thấy — và anh chưa làm được thứ đủ tốt để họ phải thấy."</p>

<p>"Vậy anh làm đi."</p>

<p>Sơn nhìn vợ. Rồi anh mở ngăn kéo, lấy ra cuốn sổ — sổ thiết kế bộ máy đồng hồ cơ khí hoàn toàn Made in Vietnam. Anh đã vẽ ba năm rồi — ba năm nghiên cứu, ba năm vẽ từng bánh răng, từng lò xo, từng trục. Chưa hoàn thành. Nhưng gần.</p>

<p>"Anh cần thêm một năm."</p>"""
    },
    {
        "title": "Chương 2: Bố Và Chiếc Đồng Hồ Poljot",
        "content": """<p>Sơn học sửa đồng hồ từ bố — ông Ngô Văn Thành, thợ sửa đồng hồ Liên Xô, bốn mươi năm kinh nghiệm, ngồi ở vỉa hè phố Hàng Đào từ năm 1985.</p>

<p>Ông Thành sáu mươi lăm tuổi, tóc bạc, lưng còng, đeo kính lúp một bên mắt, ngồi trên ghế nhựa nhỏ bên cạnh chiếc bàn gỗ rộng nửa mét — trên bàn là tua vít, nhíp, dầu máy, và hàng trăm bánh răng nhỏ li ti.</p>

<p>Ông sửa đồng hồ Liên Xô — Poljot, Vostok, Raketa — những chiếc đồng hồ cơ khí mà cán bộ nhà nước mang về từ Moscow trong thập niên bảy mươi, tám mươi. Khi Liên Xô sụp đổ, phụ tùng không còn — nhưng ông Thành tự chế: tiện bánh răng từ đồng thau, mài lò xo từ dây thép, đúc trục từ nhôm. Tất cả bằng tay, bằng kính lúp, bằng kiên nhẫn.</p>

<p>"Bố ơi, sao bố không mở tiệm?"</p>

<p>"Vỉa hè là tiệm của bố. Người ta đi ngang, thấy bố, dừng lại. Nếu bố ngồi trong nhà, ai biết bố ở đâu?"</p>

<p>Sơn mười tuổi, bắt đầu ngồi cạnh bố, phụ lau dầu máy, sắp xếp bánh răng. Mười hai tuổi, ông Thành dạy con tháo đồng hồ: "Nhớ, tháo đến đâu ghi đến đó. Đồng hồ có hai trăm chi tiết — quên một cái là chết."</p>

<p>Mười lăm tuổi, Sơn tháo và lắp lại chiếc Poljot đầu tiên — chiếc đồng hồ mạ vàng của ông Hai, cán bộ phường nghỉ hưu. Ông Hai mang đến, nói: "Nó ngừng chạy rồi, cháu sửa được không?" Sơn tháo, tìm lỗi — một bánh răng nhỏ bằng hạt gạo bị mòn, ăn khớp không đúng. Anh mài lại bằng giấy nhám 2000, tra dầu, lắp — đồng hồ chạy lại.</p>

<p>Ông Hai trả năm mươi nghìn đồng. Sơn mang về đưa bố.</p>

<p>"Giỏi. Nhưng con nhớ: sửa đồng hồ là nghề nhỏ. Làm đồng hồ mới là nghề lớn."</p>

<p>"Bố ơi, sao bố không làm đồng hồ?"</p>

<p>"Bố không có máy, không có vốn, không có kiến thức. Bố chỉ có tay. Nhưng con — con có thể học. Nếu con muốn, bố ủng hộ."</p>

<p>Sơn muốn. Mười tám tuổi, anh thi vào Đại học Bách khoa Hà Nội, khoa Cơ khí Chính xác — chuyên ngành gần nhất với chế tạo đồng hồ tại Việt Nam. Bốn năm đại học, anh vừa học vừa sửa đồng hồ cùng bố ở vỉa hè — ngồi ghế nhựa, đeo kính lúp, tay cầm nhíp, trong khi bạn bè đi uống trà sữa.</p>

<p>Tốt nghiệp, Sơn không đi làm công ty. Anh ngồi vỉa hè cạnh bố, sửa đồng hồ — nhưng ban đêm, anh vẽ. Vẽ bộ máy đồng hồ cơ khí đầu tiên của Việt Nam.</p>"""
    },
    {
        "title": "Chương 3: Xưởng Trong Gian Bếp",
        "content": """<p>Xưởng chế tạo đồng hồ của Ngô Hải Sơn: gian bếp phòng trọ hai mươi mét vuông ở Hàng Bông — Sơn dời bếp gas sang góc, kê bàn inox làm bàn gia công, lắp đèn LED công suất cao để chiếu sáng, và mua kính hiển vi soi nổi (stereomicroscope) cũ giá ba triệu đồng từ chợ đồ cũ Giảng Võ.</p>

<p>Dụng cụ: máy tiện mini CNC (mua trả góp mười hai tháng, giá mười lăm triệu), bộ tua vít đồng hồ Bergeon (hàng xịn, mua second-hand từ thợ đồng hồ Thụy Sĩ qua eBay, giá năm triệu), nhíp Dumont (nhíp chính xác nhất thế giới, ba trăm nghìn một chiếc), và cục kẹp từ tính để giữ chi tiết nhỏ không bị rơi.</p>

<p>Tổng đầu tư: ba mươi triệu đồng — toàn bộ tiền tiết kiệm của hai vợ chồng.</p>

<p>Hạnh — vợ Sơn — không phàn nàn. Cô nấu cơm ở phòng khách, giặt đồ trên sân thượng, nhường gian bếp cho chồng chế tạo đồng hồ. Mỗi tối, cô ngồi đọc sách cạnh bàn gia công, nghe tiếng máy tiện rì rì, tiếng nhíp gắp bánh răng lách cách.</p>

<p>"Anh ơi, cơ quan em hỏi sao gian bếp nhà mình có máy tiện."</p>

<p>"Em nói anh đang làm đồ chơi."</p>

<p>"Đồ chơi giá mười hai triệu một chiếc?"</p>

<p>"Đồ chơi cho người lớn."</p>

<p>Sơn thiết kế bộ máy đồng hồ từ số không — không copy movement Thụy Sĩ hay Nhật, mà tạo kiến trúc riêng. Anh nghiên cứu hàng trăm bằng sáng chế đồng hồ (patent miễn phí trên Google Patents), đọc sách kỹ thuật đồng hồ bằng tiếng Anh (dịch bằng Google Translate vì tiếng Anh kỹ thuật anh chưa giỏi), và xem video YouTube của thợ đồng hồ độc lập (independent watchmaker) trên toàn thế giới.</p>

<p>Bộ máy anh đặt tên: Caliber SH-100 — "SH" lấy từ Sơn Hà (tên thương hiệu anh dự định), "100" vì đây là bản thiết kế thứ một trăm (chín mươi chín bản trước đã bỏ).</p>

<p>Caliber SH-100: movement cơ khí lên dây thủ công (manual winding), hai mươi mốt chân kính (jewels), tần số dao động 28.800 lần/giờ, dự trữ năng lượng bốn mươi hai giờ. Tổng số chi tiết: một trăm ba mươi sáu — mỗi chi tiết nhỏ hơn hạt gạo, cần gia công chính xác đến 0,01mm.</p>

<p>Mười hai tháng. Sơn tiện, mài, đánh bóng từng chi tiết bằng tay — ban ngày sửa đồng hồ vỉa hè kiếm tiền, ban đêm chế tạo đồng hồ trong gian bếp. Ngủ bốn tiếng. Ăn cơm Hạnh nấu. Uống cà phê đen. Và tiện bánh răng.</p>"""
    },
    {
        "title": "Chương 4: Ông Thầy Từ Nhật Bản",
        "content": """<p>Tháng thứ tám, Sơn gặp bế tắc: escapement — bộ phận điều tốc, trái tim của đồng hồ cơ khí — anh chế tạo không đạt. Tần số dao động lệch, đồng hồ chạy nhanh ba mươi giây mỗi ngày — tiêu chuẩn COSC (chronometer Thụy Sĩ) cho phép tối đa bốn đến sáu giây.</p>

<p>Ba mươi giây lệch. Quá nhiều.</p>

<p>Sơn đăng video quá trình chế tạo lên YouTube — kênh "Sơn Hà Watchmaking," ba nghìn subscriber, chủ yếu dân yêu đồng hồ quốc tế. Video về escapement bị lỗi thu hút sự chú ý của một người: Tanaka Hiroshi — nghệ nhân đồng hồ độc lập (independent watchmaker) ở Seiko Museum, Tokyo, bảy mươi hai tuổi, bốn mươi năm kinh nghiệm.</p>

<p>Tanaka comment: "Your escapement lever angle is 2 degrees off. The impulse face needs to be polished to mirror finish. Email me — I can help."</p>

<p>Sơn email. Tanaka trả lời — bằng tiếng Anh đơn giản, kèm bản vẽ kỹ thuật chi tiết. Ông chỉ ra: góc cánh tay escapement lever lệch hai độ — sai số quá nhỏ để nhìn bằng mắt thường, nhưng đủ lớn để gây lệch tần số.</p>

<p>Từ đó, hai thầy trò trao đổi email mỗi tuần — Sơn gửi ảnh chụp chi tiết dưới kính hiển vi, Tanaka phản hồi bằng bản vẽ và nhận xét. Miễn phí, vì Tanaka nói: "I was like you forty years ago. Someone helped me. Now I help you."</p>

<p>Ba tháng sau, Tanaka bay sang Hà Nội — tự chi tiền vé máy bay. Ông đến phòng trọ Hàng Bông, nhìn gian bếp-xưởng, nhìn máy tiện mini, nhìn bàn gia công — và mỉm cười.</p>

<p>"You make watches in a kitchen. In Japan, the first Seiko watches were made in a workshop smaller than this."</p>

<p>Tanaka ở Hà Nội bảy ngày. Mỗi ngày, ông ngồi cạnh Sơn từ tám giờ sáng đến mười giờ tối — dạy: cách mài perlage (hoa văn tròn trên platina), cách đánh bóng côtes de Genève (sọc xéo trên mainplate), cách điều chỉnh hairspring bằng cảm giác ngón tay (không có máy nào thay thế được cảm giác tay thợ lành nghề).</p>

<p>"Sơn, watch-making is not engineering. It is art with engineering tools. The machine makes the shape — your hands give it life."</p>

<p>Ngày cuối, Tanaka tặng Sơn một bộ dụng cụ: tua vít Bergeon chính hãng (bộ mới, giá hai mươi triệu yen — khoảng bốn triệu đồng), nhíp Dumont cỡ 5, và một cây bút chì kỹ thuật 0,3mm.</p>

<p>"These are my tools. I'm seventy-two. I won't need them much longer. You will."</p>

<p>Sơn cúi đầu. "Thank you, sensei."</p>

<p>"Don't thank me. Make a watch that makes Vietnam proud. That's enough."</p>"""
    },
    {
        "title": "Chương 5: Caliber SH-100 — Trái Tim Đồng Hồ Việt",
        "content": """<p>Tháng thứ mười hai. Gian bếp. Ba giờ sáng.</p>

<p>Sơn lắp chi tiết cuối cùng vào Caliber SH-100 — chiếc crown wheel (bánh vương miện), kết nối trục lên dây với bộ bánh răng truyền động. Nhíp Dumont kẹp chặt, tay anh ổn định — sau mười hai tháng tiện mài hàng ngày, tay anh vững như tay bác sĩ phẫu thuật.</p>

<p>Một trăm ba mươi sáu chi tiết — tất cả đã vào đúng vị trí.</p>

<p>Sơn nhẹ nhàng xoay crown (núm vặn) — một vòng, hai vòng, ba vòng — lò xo chính (mainspring) căng dần, năng lượng tích trữ. Rồi anh thả tay.</p>

<p>Balance wheel — bánh cân bằng — bắt đầu dao động. Qua lại, qua lại, đều đặn. Tích tắc, tích tắc — tiếng đồng hồ cơ khí, tiếng mà Sơn đã nghe từ khi mười tuổi ngồi cạnh bố trên vỉa hè, nhưng lần này khác: đây là tiếng đồng hồ của anh. Anh thiết kế. Anh chế tạo. Anh lắp ráp. Từ số không.</p>

<p>Sơn đặt movement dưới kính hiển vi, đo tần số bằng ứng dụng Timegrapher trên điện thoại: 28.800 dao động/giờ, sai số +3 giây/ngày.</p>

<p>+3 giây. Trong biên COSC (+4 đến +6).</p>

<p>Sơn ngồi thụp xuống sàn bếp, tay ôm đầu. Anh không khóc — anh chỉ thở. Thở rất sâu, rất chậm, như thể anh đã nín thở mười hai tháng.</p>

<p>Hạnh thức giấc — nghe tiếng tích tắc lạ. Cô bước ra gian bếp, thấy chồng ngồi dưới sàn, trên bàn là bộ máy đồng hồ nhỏ bằng đồng xu đang chạy đều đều.</p>

<p>"Anh?"</p>

<p>"Em ơi, nó chạy rồi."</p>

<p>Hạnh ngồi xuống cạnh chồng, nhìn bộ máy — nhỏ xíu, lấp lánh dưới đèn LED, bánh răng xoay êm ái, balance wheel dao động đều — và cô hiểu: đây không phải đồng hồ. Đây là mười hai tháng mất ngủ, ba mươi triệu tiền tiết kiệm, hàng nghìn giờ tiện mài, và một ước mơ mà không ai tin ngoài cô và bố chồng.</p>

<p>"Anh, giờ anh làm gì?"</p>

<p>"Anh làm vỏ. Rồi anh làm chiếc đồng hồ hoàn chỉnh đầu tiên. Rồi anh mang nó đến Baselworld."</p>

<p>"Baselworld ở đâu?"</p>

<p>"Basel, Thụy Sĩ. Triển lãm đồng hồ lớn nhất thế giới."</p>

<p>"Anh điên."</p>

<p>"Anh biết."</p>"""
    },
    {
        "title": "Chương 6: Thương Hiệu SƠN HÀ Ra Mắt",
        "content": """<p>Sáu tháng sau khi Caliber SH-100 chạy, Sơn hoàn thành chiếc đồng hồ đầu tiên: SƠN HÀ Nhất.</p>

<p>Vỏ: thép 316L đánh bóng bằng tay, đường kính bốn mươi milimet, dày mười hai milimet. Sơn tiện vỏ từ khối thép nguyên bằng máy tiện CNC mini, rồi đánh bóng thủ công ba mươi giờ — từ giấy nhám 400 đến 2000, rồi paste đánh bóng kim loại, cho đến khi bề mặt sáng như gương.</p>

<p>Mặt số: sơn mài đen — thuê nghệ nhân Nguyễn Thị Hoa ở Hà Thái (làng sơn mài nổi tiếng Hà Nội) làm riêng. Bà Hoa sáu mươi tuổi, nghệ nhân sơn mài bốn mươi năm — chưa bao giờ làm mặt số đồng hồ vì chưa ai đặt. Bà mất hai tháng hoàn thiện mười chiếc mặt số — mỗi chiếc qua mười hai lớp sơn mài, mài và phủ lại mỗi lớp, kết thúc bằng lớp son then bóng loáng.</p>

<p>"Cháu Sơn, bác làm sơn mài cả đời, chưa ai đặt đồng vật nhỏ thế này. Khó — nhưng đẹp."</p>

<p>Kim: vàng 18K, đúc bằng phương pháp mất sáp (lost-wax casting) — Sơn thuê thợ kim hoàn ở phố Hàng Bạc đúc theo bản vẽ.</p>

<p>Dây: da bò Ý, mua qua đại lý ở TP.HCM.</p>

<p>Caseback (nắp lưng): kính sapphire trong suốt — để lộ Caliber SH-100 bên trong, với perlage và côtes de Genève do Sơn đánh bóng thủ công.</p>

<p>Khi lắp ráp hoàn chỉnh, Sơn đưa cho bố — ông Thành — xem đầu tiên.</p>

<p>Ông Thành cầm chiếc đồng hồ bằng hai tay — bàn tay chai sạn bốn mươi năm sửa đồng hồ vỉa hè — lật lại, nhìn bộ máy qua caseback kính sapphire, nghe tiếng tích tắc.</p>

<p>"Sơn ơi, bố sửa đồng hồ cả đời. Nhưng chưa bao giờ bố cầm đồng hồ do người Việt Nam chế tạo. Hôm nay bố cầm — và bố tự hào."</p>

<p>Sơn đăng ảnh SƠN HÀ Nhất lên Instagram — tài khoản @sonhawatches, lúc đó có năm nghìn follower. Ảnh chụp trên nền gỗ, ánh sáng tự nhiên, kèm caption: "SƠN HÀ Nhất — chiếc đồng hồ cơ khí đầu tiên hoàn toàn Made in Vietnam. Movement Caliber SH-100, thiết kế và chế tạo tại Hà Nội."</p>

<p>Ba ngày: hai mươi nghìn like. Tạp chí đồng hồ quốc tế Hodinkee chia sẻ. Revolution Magazine (Singapore) viết: "Vietnam just entered the watchmaking world — and the first shot is impressive."</p>"""
    },
    {
        "title": "Chương 7: Những Kẻ Hoài Nghi Quay Lại",
        "content": """<p>Khi SƠN HÀ nổi tiếng trên mạng quốc tế, giới đồng hồ Việt Nam chia làm hai.</p>

<p>Phe ủng hộ — chủ yếu dân trẻ, yêu đồng hồ, tự hào: "Cuối cùng Việt Nam cũng có đồng hồ riêng!"</p>

<p>Phe hoài nghi — chủ yếu giới kinh doanh đồng hồ nhập khẩu: "Làm được movement thì tốt, nhưng chất lượng dài hạn mới quan trọng. Đồng hồ phải chạy chính xác trong mười năm, hai mươi năm — không phải ba tháng đầu."</p>

<p>Nguyễn Hoàng Long — ông chủ SaiGon Watch, người đã cười Sơn ở triển lãm 2019 — đăng bài trên Facebook: "Tôi đánh giá cao nỗ lực của Ngô Hải Sơn. Nhưng xin nhắc: chế tạo một chiếc đồng hồ trong bếp ≠ xây dựng thương hiệu đồng hồ bền vững. Rolex mất 100 năm. Seiko mất 80 năm. SƠN HÀ mới có 1 năm."</p>

<p>Bài đăng có năm nghìn like. Nhiều comment đồng tình.</p>

<p>Sơn đọc, gật đầu. Long không sai — nhưng Long quên một thứ: Rolex và Seiko đều bắt đầu từ một người, một xưởng nhỏ, và một chiếc đồng hồ đầu tiên. Nếu đợi đến khi "sẵn sàng" mới bắt đầu, thì không ai bắt đầu gì cả.</p>

<p>Sơn không trả lời Long trên mạng. Thay vào đó, anh làm một việc: gửi chiếc SƠN HÀ Nhất đi kiểm định COSC (Contrôle Officiel Suisse des Chronomètres) — cơ quan kiểm định độ chính xác đồng hồ uy tín nhất thế giới, trụ sở tại La Chaux-de-Fonds, Thụy Sĩ.</p>

<p>Chi phí kiểm định: hai trăm franc Thụy Sĩ (khoảng năm triệu đồng). Sơn vay mẹ.</p>

<p>Sáu tuần sau, kết quả về qua email:</p>

<p>"Certificate of COSC Chronometer Testing. Movement: Caliber SH-100. Mean daily rate: +2.8 seconds. RESULT: CERTIFIED CHRONOMETER."</p>

<p>Caliber SH-100 — bộ máy đồng hồ chế tạo trong gian bếp phòng trọ Hà Nội — đạt chuẩn chronometer Thụy Sĩ. Lệch +2.8 giây/ngày — tốt hơn nhiều movement ETA sản xuất hàng loạt.</p>

<p>Sơn đăng ảnh chứng nhận COSC lên Instagram. Caption: "Caliber SH-100 — Made in Hanoi kitchen — COSC certified."</p>

<p>Long đọc bài, im lặng. Không comment.</p>"""
    },
    {
        "title": "Chương 8: Baselworld — Giấc Mơ Basel",
        "content": """<p>Baselworld 2023 — triển lãm đồng hồ và trang sức lớn nhất thế giới, tổ chức tại Basel, Thụy Sĩ. Hơn hai nghìn thương hiệu tham gia, từ Rolex, Patek Philippe, Omega đến các thương hiệu độc lập nhỏ nhất.</p>

<p>Sơn nộp đơn tham gia — mục Independent Watchmakers (thợ đồng hồ độc lập). Phí gian hàng: năm nghìn franc Thụy Sĩ (khoảng một trăm ba mươi triệu đồng) — cho gian nhỏ nhất, bốn mét vuông.</p>

<p>Tiền đâu? Sơn bán năm chiếc SƠN HÀ Nhất đã sản xuất — mỗi chiếc bốn mươi triệu đồng (giá cao gấp ba so với phiên bản ETA trước đây, vì giờ là movement in-house). Hai trăm triệu. Trừ chi phí sản xuất, còn một trăm năm mươi triệu. Đủ phí gian hàng, vé máy bay, và ăn ở bảy ngày tại Basel.</p>

<p>Hạnh lo lắng: "Anh ơi, đó là toàn bộ tiền mình có."</p>

<p>"Em ơi, nếu không đến Basel, không ai biết SƠN HÀ. Nếu đến Basel, cả thế giới sẽ thấy."</p>

<p>"Nếu thất bại?"</p>

<p>"Thì anh về sửa đồng hồ vỉa hè. Anh vẫn sống được."</p>

<p>Hạnh ôm chồng: "Em tin anh."</p>

<hr>

<p>Basel, Thụy Sĩ. Tháng Ba.</p>

<p>Gian hàng SƠN HÀ: bốn mét vuông, nhỏ nhất triển lãm. Tường trắng, bàn kính, đèn spot. Trên bàn: ba chiếc đồng hồ SƠN HÀ — mặt sơn mài đen, vỏ thép đánh bóng, caseback kính sapphire lộ Caliber SH-100.</p>

<p>Bên cạnh gian SƠN HÀ: gian Patek Philippe — rộng hai trăm mét vuông, đèn pha lê, thảm nhung, nhân viên vest đen.</p>

<p>Sơn đứng sau quầy, mặc áo sơ mi trắng (giặt đêm qua tại phòng khách sạn giá rẻ), tay hơi run — nhưng mắt sáng.</p>

<p>Giờ đầu tiên: không ai dừng lại. Giờ thứ hai: một nhà sưu tập Đức dừng, cầm chiếc đồng hồ lên, lật caseback, nhìn movement.</p>

<p>"This is handmade?"</p>

<p>"Yes. Every single part. In my kitchen in Hanoi."</p>

<p>"In a kitchen?"</p>

<p>"Yes."</p>

<p>Ông ta cười — nhưng không phải cười khinh, mà cười kinh ngạc. Ông mua một chiếc — năm nghìn euro.</p>

<p>Ngày thứ hai: tạp chí Monochrome Watches đến phỏng vấn. Ngày thứ ba: Hodinkee quay video. Ngày thứ tư: một đại lý Nhật đặt mười chiếc cho chuỗi cửa hàng ở Tokyo.</p>

<p>Ngày cuối cùng, Tanaka Hiroshi — ông thầy người Nhật — gửi tin nhắn: "I saw your booth online. I am proud. You did it."</p>

<p>Sơn reply: "No, sensei. WE did it."</p>"""
    },
    {
        "title": "Chương 9: Quay Về Vỉa Hè",
        "content": """<p>Sơn trở về Hà Nội sau Baselworld, mang theo đơn đặt hàng hai mươi chiếc từ Nhật, mười chiếc từ Đức, và lời mời hợp tác từ hai thương hiệu đồng hồ độc lập Thụy Sĩ.</p>

<p>Anh dời xưởng từ gian bếp sang căn hộ thuê riêng — bốn mươi mét vuông ở Hàng Bông, đủ chỗ cho bàn gia công, máy tiện, kính hiển vi, và hai nhân viên mới: Minh — sinh viên Bách khoa vừa tốt nghiệp, và Hoàng — thợ đồng hồ trẻ từ Đà Nẵng, tìm đến Sơn sau khi xem video YouTube.</p>

<p>Sản lượng: mỗi tháng năm chiếc — làm hoàn toàn bằng tay, mỗi chiếc mất hai tuần. Giá bán: năm nghìn đến tám nghìn euro — phân khúc luxury độc lập, cạnh tranh trực tiếp với thương hiệu Thụy Sĩ cùng phân khúc.</p>

<p>Nhưng mỗi sáng, trước khi vào xưởng, Sơn vẫn ghé vỉa hè phố Hàng Đào — nơi bố vẫn ngồi sửa đồng hồ. Ông Thành bảy mươi tuổi rồi — lưng còng thêm, mắt mờ hơn, tay run nhẹ — nhưng ông vẫn ngồi, vẫn đeo kính lúp, vẫn sửa những chiếc Poljot cũ cho khách quen.</p>

<p>"Bố ơi, bố nghỉ đi. Con nuôi bố."</p>

<p>"Bố sửa đồng hồ không phải vì tiền. Bố sửa vì bố thích. Ngày nào bố còn sửa được, bố còn ngồi."</p>

<p>Sơn ngồi cạnh bố, mười phút mỗi sáng — như hồi mười tuổi. Ông Thành sửa chiếc Vostok cũ, Sơn phụ lau dầu máy. Hai bố con không nói nhiều — vì đàn ông nhà Ngô không hay nói. Họ nói bằng tay — tay cầm nhíp, tay xoay tua vít, tay đặt bánh răng vào đúng vị trí.</p>

<p>Khách qua đường nhìn: một ông già và một anh thanh niên ngồi vỉa hè sửa đồng hồ. Không ai biết anh thanh niên đó vừa triển lãm ở Baselworld. Không ai biết đôi bàn tay đang lau dầu Poljot cũ cũng là đôi bàn tay chế tạo Caliber SH-100 đạt chuẩn COSC.</p>

<p>Và Sơn không cần ai biết. Vì với anh, ngồi vỉa hè cạnh bố, sửa đồng hồ — đó là nguồn gốc. Và nguồn gốc không phải thứ để bỏ đi khi thành công — mà là thứ để trở về.</p>

<p>Trên cổ tay Sơn: chiếc SƠN HÀ Nhất — chiếc đầu tiên, chiếc anh không bán. Mặt sơn mài đen lấp lánh dưới nắng sáng phố Hàng Đào, kim vàng chỉ tám giờ mười lăm phút — giờ mà bố anh mở quầy mỗi sáng, bốn mươi năm nay.</p>

<p>Tích tắc. Tích tắc. Tiếng đồng hồ Việt Nam — nhỏ thôi, nhưng đều đặn. Như bước chân của người thợ vỉa hè đi từ Hàng Đào đến Basel, rồi trở về Hàng Đào.</p>

<p>Vì Basel là nơi thế giới công nhận anh. Nhưng Hàng Đào là nơi anh là chính mình.</p>"""
    }
]

story_data["chapters"] = chapters

with open("scratch/story_5569_rewrite.json", "w", encoding="utf-8") as f:
    json.dump(story_data, f, ensure_ascii=False, indent=2)

print("✅ Truyện 5569 viết xong — 9 CHƯƠNG!")
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
    if ws.cell(row=r, column=2).value and str(ws.cell(row=r, column=2).value).strip() == "5569":
        ws.cell(row=r, column=6).value = 9
        ws.cell(row=r, column=12).value = "Thợ sửa đồng hồ vỉa hè Hàng Đào, chế tạo movement cơ khí đầu tiên Made in Vietnam trong gian bếp, đạt chuẩn COSC Thụy Sĩ, triển lãm Baselworld."
        ws.cell(row=r, column=13).value = "REWRITE TOÀN BỘ: 11 chương quá ngắn → 9 CHƯƠNG ĐẦY ĐẶN"
        ws.cell(row=r, column=14).value = "☑️ Đã sửa"
        print(f"  ✅ Excel updated row {r}")
        break
wb.save("danh_sach_truyen_doctieuthuyet.xlsx")
print("\n✅ HOÀN THÀNH TRUYỆN 5569!")
