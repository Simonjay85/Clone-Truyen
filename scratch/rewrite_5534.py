import json, urllib.request, openpyxl

story_data = {
    "secret_token": "ZEN_TRUYEN_2026_BYPASS",
    "story_id": 5534,
    "title": "Bị Cướp Công Thức Serum Tái Tạo Da, Tôi Lập Thương Hiệu Mỹ Phẩm Sạch Khiến Kẻ Trộm Phá Sản",
    "intro": "<p>Mai Phương Linh — thạc sĩ Hóa dược, Đại học Dược Hà Nội — mất bốn năm nghiên cứu serum tái tạo da chiết xuất từ hoa sen Tây Hồ. Khi cô nộp công thức cho công ty GlowMax Cosmetics để hợp tác sản xuất, Giám đốc R&D Trần Văn Đức đánh cắp toàn bộ — đăng ký bằng sáng chế dưới tên công ty, và đuổi cô ra khỏi dự án.</p>\n<p>Nhưng Phương Linh có một thứ mà GlowMax không có: kiến thức sâu về chiết xuất sen — và bà nội bên Hồ Tây, người đã trồng sen bảy mươi năm.</p>",
    "author": "Mai Phương Linh",
    "chapters": []
}

chapters = [
    {
        "title": "Chương 1: Công Thức Sen Bị Đánh Cắp",
        "content": """<p>Mai Phương Linh biết mình bị phản bội khi đọc thông cáo báo chí của GlowMax Cosmetics trên trang chủ công ty:</p>

<p>"GlowMax ra mắt dòng sản phẩm Lotus Renewal Serum — công nghệ chiết xuất từ hoa sen Việt Nam, nghiên cứu độc quyền bởi đội ngũ R&D GlowMax, do Giám đốc R&D Trần Văn Đức dẫn dắt."</p>

<p>Phương Linh hai mươi tám tuổi, thạc sĩ Hóa dược Đại học Dược Hà Nội, chuyên ngành chiết xuất hoạt chất sinh học từ thực vật. Bốn năm nghiên cứu — từ năm thứ hai thạc sĩ đến hai năm sau tốt nghiệp — cô đã phát triển công thức serum tái tạo da dựa trên chiết xuất polyphenol và flavonoid từ nhị hoa sen Tây Hồ.</p>

<p>Công thức: chiết xuất bằng phương pháp siêu âm nhiệt độ thấp (ultrasound-assisted extraction, UAE) ở 40°C — thấp hơn nhiều so với phương pháp truyền thống (80-100°C) — giữ nguyên cấu trúc phân tử polyphenol, tăng hiệu quả chống oxy hóa gấp ba lần. Nồng độ hoạt chất: 12% — cao nhất trong các serum chiết xuất thực vật trên thị trường.</p>

<p>Bốn năm: hai trăm thí nghiệm, ba mươi lần thất bại, tám mươi trang lab notebook viết tay, và một bài báo quốc tế đăng trên Journal of Cosmetic Dermatology — tên đầu tiên: Mai Phương Linh.</p>

<p>Khi GlowMax — công ty mỹ phẩm top 5 Việt Nam, doanh thu hai trăm tỷ đồng/năm — liên hệ đề nghị hợp tác thương mại hóa, Phương Linh vui mừng. Cô ký hợp đồng tư vấn (consulting agreement), chia sẻ công thức chiết xuất, quy trình sản xuất, và dữ liệu thử nghiệm lâm sàng.</p>

<p>Ba tháng sau: GlowMax đăng ký bằng sáng chế công thức — tên đăng ký: Trần Văn Đức, Giám đốc R&D. Tên Mai Phương Linh: không xuất hiện.</p>

<p>Phương Linh gọi Đức.</p>

<p>"Anh Đức, công thức serum là của em. Em chia sẻ để hợp tác — không phải để anh đăng ký bằng sáng chế dưới tên anh."</p>

<p>"Linh, em ký hợp đồng tư vấn — theo điều khoản, mọi sản phẩm trí tuệ phát sinh trong quá trình tư vấn thuộc về GlowMax."</p>

<p>"Nhưng công thức em phát triển từ TRƯỚC khi ký hợp đồng. Em có bài báo quốc tế, em có lab notebook, em có dữ liệu thử nghiệm — tất cả trước ngày ký."</p>

<p>"Linh, em nên đọc kỹ hợp đồng. Và em nên biết: GlowMax có luật sư, em thì không."</p>

<p>Đức cúp máy.</p>

<p>Phương Linh ngồi trong phòng trọ ở Kim Mã — mười tám mét vuông, bàn làm việc đầy sách Hóa dược — tay cầm bản hợp đồng, đọc lại từng điều khoản. Điều khoản 7.2: "Mọi sản phẩm trí tuệ phát sinh TRONG QUÁ TRÌNH TƯ VẤN thuộc quyền sở hữu của Bên A (GlowMax)."</p>

<p>"Trong quá trình tư vấn" — công thức cô phát triển TRƯỚC quá trình tư vấn. Đức đang lợi dụng ngôn ngữ hợp đồng để chiếm đoạt công thức có sẵn. Đó là gian lận — nhưng chứng minh được thì cần luật sư, cần bằng chứng, cần tiền.</p>

<p>Và Phương Linh không có tiền.</p>"""
    },
    {
        "title": "Chương 2: Bà Nội Và Hoa Sen Tây Hồ",
        "content": """<p>Phương Linh nghiên cứu sen vì bà nội.</p>

<p>Bà Nguyễn Thị Hồng — bảy mươi tám tuổi, sống bên Hồ Tây — trồng sen bảy mươi năm. Từ năm tám tuổi, bà theo mẹ hái sen ở đầm Trị — đầm sen lớn nhất Hà Nội, nằm giữa phường Quảng An và Nhật Tân.</p>

<p>Mỗi mùa hè, bà Hồng thức dậy lúc bốn giờ sáng, chèo thuyền nhỏ ra đầm, hái sen khi hoa vừa nở — vì sen hái lúc mới nở có hương thơm nhất, nhị vàng tươi nhất.</p>

<p>Bà bán hoa sen, trà sen, hạt sen, và một thứ mà ít ai biết: bột nhị sen — nhị hoa sen phơi khô, nghiền mịn, trộn với bồ kết và bồ hòn để gội đầu. Phụ nữ Hà Nội xưa gội đầu bằng bột nhị sen — tóc mượt, da đầu sạch, và thơm mùi sen.</p>

<p>"Bà ơi, sao bà không bán bột nhị sen nhiều hơn?"</p>

<p>"Vì người ta không tin, con ơi. Người ta chỉ tin dầu gội có mác ngoại. Bột nhị sen của bà — bà làm bằng tay, phơi nắng, không có hộp đẹp, không có quảng cáo — ai mua?"</p>

<p>Năm hai mươi tuổi, Phương Linh thi vào Đại học Dược — vì cô muốn chứng minh khoa học đằng sau bột nhị sen của bà: polyphenol trong nhị sen có khả năng chống oxy hóa, ức chế melanin (giảm sạm da), và kích thích collagen (tái tạo da). Bà nội đúng — chỉ là bà không biết gọi tên.</p>

<p>Bốn năm nghiên cứu — Phương Linh chứng minh: chiết xuất nhị sen Tây Hồ có hàm lượng polyphenol cao hơn bốn mươi phần trăm so với sen các vùng khác (do đất bùn Hồ Tây giàu khoáng chất đặc thù). Và phương pháp UAE ở 40°C giữ nguyên hoạt chất tốt hơn mọi phương pháp chiết xuất khác.</p>

<p>Khi GlowMax đánh cắp công thức, họ không chỉ ăn cắp khoa học — họ ăn cắp bảy mươi năm bà Hồng trồng sen. Họ ăn cắp bột nhị sen gội đầu. Họ ăn cắp mùi sen Tây Hồ lúc bốn giờ sáng.</p>

<p>"Bà ơi, người ta ăn cắp công thức sen của con."</p>

<p>"Con ơi, sen mọc từ bùn. Bùn bẩn — nhưng sen sạch. Người ta ăn cắp thì người ta là bùn. Con cứ sạch — rồi sen sẽ nở."</p>"""
    },
    {
        "title": "Chương 3: Lab Trong Phòng Ngủ",
        "content": """<p>Phương Linh quyết định: không kiện GlowMax (vì không có tiền thuê luật sư), mà tự lập thương hiệu mỹ phẩm riêng — dùng đúng công thức của mình, cải tiến thêm, và bán trực tiếp cho khách hàng.</p>

<p>Lab mới: phòng ngủ mười tám mét vuông. Bàn gia công: bàn bếp inox mua ở chợ Đồng Xuân, hai triệu đồng. Thiết bị: máy đồng hóa cầm tay (homogenizer) mua second-hand giá năm triệu, cân phân tích điện tử giá ba triệu, và bộ dụng cụ thủy tinh (beaker, bình tam giác, pipette) từ phòng thí nghiệm cũ của trường Dược — thầy hướng dẫn cho mượn.</p>

<p>Nguyên liệu: nhị sen Tây Hồ — bà nội hái cho, miễn phí. Bà Hồng mỗi sáng chèo thuyền ra đầm, hái nhị sen tươi, phơi trên mái nhà, rồi đóng gói gửi cháu bằng xe khách Hà Nội - Kim Mã.</p>

<p>Vốn ban đầu: mười lăm triệu đồng — tiền tiết kiệm bốn năm đi làm thêm.</p>

<p>Phương Linh cải tiến công thức: thay vì chỉ dùng polyphenol từ nhị sen, cô kết hợp thêm chiết xuất lá sen (chứa alkaloid nuciferine — có tác dụng kháng viêm) và chiết xuất gương sen (chứa vitamin C tự nhiên). Ba thành phần từ cùng một cây sen — tận dụng triệt để, không lãng phí.</p>

<p>Thương hiệu: LinhSen — "Linh" từ tên cô, "Sen" từ bà nội.</p>

<p>Sản phẩm đầu tiên: LinhSen Lotus Serum — chai thủy tinh ba mươi ml, nhãn in giấy kraft, thiết kế tối giản. Giá: hai trăm năm mươi nghìn đồng — rẻ hơn mười lần so với Lotus Renewal Serum của GlowMax (hai triệu rưỡi), nhưng cùng hoạt chất, cùng nồng độ.</p>

<p>Kênh bán: Instagram, Shopee, và một số chợ organic ở Hà Nội.</p>

<p>Tháng đầu: bán được ba mươi chai. Tháng hai: sáu mươi. Tháng ba: một trăm năm mươi — vì khách dùng thấy hiệu quả, review tốt, và chia sẻ.</p>

<p>Đặc biệt: một beauty blogger — Trần Thị Hạnh Nguyên, 500K follower trên YouTube — mua LinhSen dùng thử, quay video so sánh với Lotus Renewal của GlowMax. Kết luận: "Hiệu quả tương đương, thành phần sạch hơn, giá rẻ hơn mười lần. Tôi chuyển sang LinhSen."</p>

<p>Video: hai triệu lượt xem.</p>"""
    },
    {
        "title": "Chương 4: GlowMax Phản Công",
        "content": """<p>Khi LinhSen bắt đầu ảnh hưởng doanh số, GlowMax phản ứng.</p>

<p>Bước một: Đức gửi thư luật sư cho Phương Linh — cáo buộc LinhSen "vi phạm bằng sáng chế" của GlowMax. "Công thức chiết xuất sen bằng UAE đã được đăng ký bảo hộ dưới tên GlowMax. Bất kỳ sản phẩm nào sử dụng công thức tương tự đều vi phạm."</p>

<p>Phương Linh đọc thư, cười chua chát: "Anh ăn cắp công thức của tôi, đăng ký bằng sáng chế, rồi cáo buộc TÔI vi phạm bằng sáng chế của anh?"</p>

<p>Cô gọi luật sư — Phạm Minh Tú, luật sư sở hữu trí tuệ, được giới thiệu qua thầy hướng dẫn ở trường Dược. Tú nhận vụ miễn phí (pro bono) — vì anh ta ghét kẻ ăn cắp công thức.</p>

<p>"Linh, bằng sáng chế của GlowMax có thể bị vô hiệu hóa nếu em chứng minh em phát triển công thức TRƯỚC ngày nộp đơn sáng chế. Em cần: lab notebook gốc (có ngày tháng), bài báo quốc tế (published date trước ngày nộp đơn), và dữ liệu thử nghiệm lâm sàng (có timestamp)."</p>

<p>"Em có hết. Lab notebook tám mươi trang, viết tay, có chữ ký thầy hướng dẫn xác nhận mỗi tuần. Bài báo Journal of Cosmetic Dermatology đăng mười tám tháng trước ngày GlowMax nộp đơn sáng chế. Và dữ liệu thử nghiệm lưu trên server trường Dược — có timestamp."</p>

<p>Bước hai của GlowMax: Đức liên hệ các chợ organic ở Hà Nội, đe dọa kiện nếu họ bán LinhSen. Hai chợ rút sản phẩm LinhSen khỏi kệ.</p>

<p>Bước ba: GlowMax mua quảng cáo Facebook, target đúng tệp khách hàng của LinhSen: "Cẩn thận mỹ phẩm handmade không rõ nguồn gốc, không được Bộ Y tế cấp phép."</p>

<p>Phương Linh bị dồn — nhưng cô không lùi. Cô đăng ký giấy phép lưu hành mỹ phẩm tại Cục Quản lý Dược (một quy trình mà cô biết rõ, vì cô học Đại học Dược). Ba tháng: LinhSen có giấy phép chính thức — hợp pháp, sạch sẽ, minh bạch.</p>

<p>Và cô phản công — bằng sự thật.</p>"""
    },
    {
        "title": "Chương 5: Phát Hiện Dị Ứng Hàng Loạt",
        "content": """<p>Hai tháng sau khi GlowMax ra mắt Lotus Renewal Serum, báo cáo dị ứng bắt đầu xuất hiện trên mạng xã hội.</p>

<p>Một khách hàng đăng ảnh mặt sưng đỏ: "Dùng Lotus Renewal hai tuần, da tôi bị viêm, ngứa, bong tróc." Rồi thêm người — năm, mười, hai mươi, năm mươi. Group Facebook "Nạn nhân mỹ phẩm" có thread riêng cho Lotus Renewal: bảy mươi hai trường hợp dị ứng, mười lăm trường hợp viêm da tiếp xúc nặng phải đi bệnh viện.</p>

<p>Phương Linh đọc các báo cáo — và hiểu ngay vấn đề: GlowMax sao chép công thức của cô nhưng thay đổi quy trình sản xuất để giảm chi phí. Thay vì chiết xuất UAE ở 40°C (tốn thời gian, tốn năng lượng), GlowMax chiết xuất ở 90°C — nhanh hơn nhưng phá hủy cấu trúc polyphenol, tạo ra sản phẩm phụ gây kích ứng da.</p>

<p>Và quan trọng hơn: GlowMax thêm paraben (chất bảo quản rẻ) với nồng độ cao hơn tiêu chuẩn EU — vì sản phẩm chiết xuất ở nhiệt độ cao kém ổn định hơn, cần nhiều chất bảo quản.</p>

<p>Phương Linh mua một chai Lotus Renewal trên Shopee, mang về phòng trọ, phân tích bằng máy đo pH và bộ test kit (mua trên Lazada, giá năm trăm nghìn). Kết quả: pH 3.2 (quá acid — tiêu chuẩn serum da mặt: 4.5-5.5), nồng độ paraben gấp hai lần giới hạn EU.</p>

<p>Cô gửi mẫu đến Viện Kiểm nghiệm Thuốc — kiểm tra chính thức. Kết quả: xác nhận — pH ngoài ngưỡng an toàn, paraben vượt chuẩn, và phát hiện thêm: có chứa hydroquinone nồng độ thấp — chất bị cấm trong mỹ phẩm tại Việt Nam vì gây hại da lâu dài.</p>

<p>Phương Linh đăng kết quả lên Facebook — kèm ảnh chứng nhận Viện Kiểm nghiệm, ảnh bản phân tích, và so sánh thành phần giữa LinhSen (sạch, đủ chuẩn) và Lotus Renewal (vi phạm).</p>

<p>"Tôi là người phát triển công thức gốc. GlowMax ăn cắp công thức của tôi, sản xuất sai quy trình, và bán sản phẩm gây hại cho người dùng. Đây là bằng chứng."</p>

<p>Bài đăng: năm trăm nghìn lượt xem trong hai ngày.</p>"""
    },
    {
        "title": "Chương 6: Đức Bị Tước Bằng",
        "content": """<p>Cục Quản lý Dược vào cuộc — thu hồi giấy phép lưu hành Lotus Renewal Serum, yêu cầu GlowMax recall toàn bộ sản phẩm trên thị trường. Đồng thời, chuyển hồ sơ sang Cục Sở hữu Trí tuệ để rà soát bằng sáng chế.</p>

<p>Luật sư Phạm Minh Tú nộp đơn phản đối bằng sáng chế (patent opposition) — kèm bằng chứng: lab notebook gốc, bài báo quốc tế, dữ liệu thử nghiệm trên server trường Dược — tất cả có timestamp trước ngày GlowMax nộp đơn sáng chế mười tám tháng.</p>

<p>Cục Sở hữu Trí tuệ xét xử: bằng sáng chế của GlowMax bị vô hiệu hóa — vì "công thức đã được công bố trước ngày nộp đơn" (prior art). Tức là: Phương Linh đã công bố công thức trên tạp chí quốc tế TRƯỚC khi GlowMax đăng ký — bằng sáng chế không hợp lệ.</p>

<p>Trần Văn Đức: bị GlowMax sa thải — vì vụ bê bối ảnh hưởng doanh thu và uy tín. Bộ Khoa học & Công nghệ rà soát hồ sơ đăng ký bằng sáng chế của Đức — phát hiện đây không phải lần đầu: trong ba bằng sáng chế trước đó, hai bằng cũng dựa trên nghiên cứu của người khác mà Đức đứng tên. Tất cả bị rà soát lại.</p>

<p>GlowMax: bồi thường bảy trăm triệu đồng cho bảy mươi hai khách hàng bị dị ứng, nộp phạt hai trăm triệu cho Cục Quản lý Dược, và mất hình ảnh — doanh thu giảm ba mươi phần trăm trong quý tiếp theo.</p>

<p>Phương Linh nhận quyết định vô hiệu hóa bằng sáng chế — văn bản chính thức, dấu đỏ, chữ ký. Cô đọc ba lần, gấp lại, nhét vào ví — cạnh tấm ảnh bà nội đứng bên đầm sen.</p>

<p>Cô gọi bà.</p>

<p>"Bà ơi, họ hủy bằng sáng chế rồi. Công thức sen là của con."</p>

<p>"Bà biết rồi, con ơi. Công thức sen không phải của ai — nó là của sen. Con chỉ là người nghe sen nói."</p>"""
    },
    {
        "title": "Chương 7: LinhSen Bùng Nổ",
        "content": """<p>Sau vụ bê bối GlowMax, LinhSen trở thành thương hiệu mỹ phẩm sạch được biết đến nhất Việt Nam — không phải vì quảng cáo, mà vì câu chuyện: cô gái học Dược bị cướp công thức, tự làm serum trong phòng ngủ, và thắng tập đoàn mỹ phẩm bằng khoa học.</p>

<p>Doanh số tháng đầu sau vụ bê bối: một nghìn chai. Tháng thứ hai: ba nghìn. Tháng thứ sáu: mười nghìn chai mỗi tháng.</p>

<p>Phương Linh thuê xưởng sản xuất — phòng sạch (clean room) chuẩn GMP tại khu công nghiệp Quang Minh, Mê Linh. Đầu tư: năm trăm triệu đồng — vay ngân hàng, thế chấp bằng đơn hàng.</p>

<p>Đội ngũ: năm nhân viên — hai dược sĩ (bạn học trường Dược), một designer (freelancer), một nhân viên kho, và Phương Linh vừa làm CEO vừa làm trưởng phòng R&D.</p>

<p>Sản phẩm mở rộng: LinhSen Lotus Toner (nước hoa hồng sen), LinhSen Lotus Mask (mặt nạ bùn sen), LinhSen Lotus Cleanser (sữa rửa mặt chiết xuất lá sen). Tất cả dùng nguyên liệu từ đầm sen Tây Hồ — bà nội vẫn hái mỗi sáng, nhưng giờ có thêm ba người hái phụ.</p>

<p>Đặc biệt: Phương Linh cam kết "Open Formula" — công khai toàn bộ thành phần và nồng độ trên nhãn sản phẩm. Không giấu, không che — vì cô tin rằng: "Mỹ phẩm sạch phải minh bạch. Nếu bạn không dám nói thành phần, bạn không xứng đáng bán."</p>

<p>Beauty blogger Hạnh Nguyên — người đã so sánh LinhSen với GlowMax — trở thành đại sứ thương hiệu (không lương, tình nguyện): "Tôi không đại diện cho thương hiệu. Tôi đại diện cho quyền được biết mình bôi gì lên mặt."</p>

<p>LinhSen lọt top 10 thương hiệu mỹ phẩm nội địa trên Shopee — đứng cạnh những tên tuổi lớn hơn gấp trăm lần về ngân sách marketing.</p>"""
    },
    {
        "title": "Chương 8: Hội Nghị Da Liễu Quốc Tế",
        "content": """<p>International Federation of Societies of Cosmetic Chemists (IFSCC) — Hội nghị hàng năm tại Seoul, Hàn Quốc — mời Phương Linh trình bày nghiên cứu.</p>

<p>Bài trình bày: "Ultrasound-Assisted Extraction of Nelumbo nucifera Polyphenols at Low Temperature: A Novel Approach to Botanical Skincare" — chính là nghiên cứu mà GlowMax đã ăn cắp, nhưng giờ được trình bày bởi đúng tác giả, trước đúng hội đồng khoa học.</p>

<p>Phương Linh đứng trên bục — áo dài tím, tóc búi, giọng tiếng Anh hơi run nhưng rõ ràng — trước ba trăm nhà hóa mỹ phẩm từ bốn mươi quốc gia.</p>

<p>"I developed this formula in a bedroom in Hanoi. Someone stole it. A corporation sold it. And consumers were harmed because the thief didn't understand the science behind it."</p>

<p>"The formula works at 40 degrees — not 90. Because at 90 degrees, you destroy the polyphenols. You turn medicine into poison. That's what happens when you steal science without understanding it."</p>

<p>"I'm here not just to present my research — but to say: intellectual property theft in cosmetics doesn't just hurt scientists. It hurts consumers. And it hurts trust."</p>

<p>Vỗ tay dài.</p>

<p>Sau hội nghị: hai hãng mỹ phẩm Hàn Quốc (Amorepacific và LG Household) liên hệ — đề nghị hợp tác R&D, cung cấp chiết xuất sen Tây Hồ cho dòng sản phẩm K-beauty. Điều kiện Phương Linh: "Tên tôi trên mọi bằng sáng chế. Và nguyên liệu phải mua từ đầm sen Tây Hồ — giúp bà nội tôi và những người trồng sen có thu nhập."</p>

<p>Amorepacific đồng ý.</p>

<p>Phương Linh gọi bà từ Seoul:</p>

<p>"Bà ơi, người Hàn Quốc muốn mua sen của bà."</p>

<p>"Họ mua bao nhiêu?"</p>

<p>"Nhiều lắm, bà. Nhiều đến mức bà phải thuê thêm người hái."</p>

<p>Bà Hồng cười — tiếng cười của người bảy mươi tám tuổi, suốt đời hái sen ở Tây Hồ, lần đầu nghe tin hoa sen của mình bay đến xứ người.</p>

<p>"Con ơi, sen Tây Hồ đi Hàn Quốc. Bà không ngờ."</p>

<p>"Bà ơi, sen đi đâu cũng là sen. Và sen nở từ bùn — bà dạy con vậy mà."</p>"""
    },
    {
        "title": "Chương 9: Quay Về Hồ Tây",
        "content": """<p>Một năm sau IFSCC Seoul.</p>

<p>LinhSen: doanh thu mười lăm tỷ đồng/năm, hai mươi nhân viên, xưởng GMP chuẩn quốc tế, bán trên Shopee, Lazada, TikTok Shop, và hai mươi điểm bán retail tại Hà Nội và TP.HCM. Hợp tác R&D với Amorepacific — sản phẩm collab "Lotus by LinhSen x Amorepacific" bán tại Hàn Quốc và Việt Nam.</p>

<p>Phương Linh có thể mua nhà, mua xe, thuê văn phòng sang. Nhưng mỗi sáng thứ Bảy, cô vẫn về Hồ Tây — ngồi trên thuyền nhỏ cùng bà nội, hái sen.</p>

<p>Bốn giờ sáng. Trời còn tối, sương mù phủ mặt hồ, mùi bùn và sen quyện vào nhau. Bà Hồng chèo thuyền — chậm, đều, như bảy mươi năm qua — còn Phương Linh ngồi mũi thuyền, tay hái nhị sen, bỏ vào rổ tre.</p>

<p>"Bà ơi, ngày xưa bà hái sen bán được bao nhiêu?"</p>

<p>"Ngày xưa à? Mỗi mùa hái được vài ký nhị sen, bán được vài trăm nghìn. Đủ mua gạo."</p>

<p>"Giờ nhị sen bà hái bán cho Amorepacific, mỗi ký bốn trăm nghìn."</p>

<p>"Bà già rồi, con ơi. Bà không hiểu Amorepacific là gì. Bà chỉ biết: sen đẹp, sen thơm, và con gái bà giỏi."</p>

<p>Phương Linh cười, ôm bà — trên thuyền, giữa đầm sen, bốn giờ sáng.</p>

<hr>

<p>Chiều hôm đó, Phương Linh về xưởng, mở lab notebook mới — trang đầu tiên, cô viết:</p>

<p>"Dự án mới: Chiết xuất hoạt chất từ lá sen già (lá sen sau mùa, thường bỏ đi). Giả thuyết: lá sen già chứa nồng độ alkaloid nuciferine cao hơn lá non — tiềm năng cho sản phẩm chống viêm da."</p>

<p>Cô lật trang, bắt đầu vẽ sơ đồ quy trình. Bên cạnh: chiếc beaker chứa dung dịch chiết xuất màu xanh lá — từ lá sen già mà bà nội hái hôm nay.</p>

<p>Phương Linh không dừng ở một sản phẩm. Cô là nhà khoa học — và nhà khoa học không bao giờ dừng. Họ chỉ bắt đầu lại, với câu hỏi mới, từ cùng một bông sen.</p>

<p>Trên bàn lab, cạnh notebook, là tấm ảnh bà nội — bà Hồng đứng bên đầm sen Tây Hồ, tay cầm bông sen, cười. Phía sau là Hồ Tây — mênh mông, phẳng lặng, và đầy sen.</p>

<p>Sen nở từ bùn. Và từ bùn, LinhSen đã nở — không phải vì ai cho phép, mà vì sen không cần ai cho phép để nở.</p>"""
    }
]

story_data["chapters"] = chapters

print("✅ Truyện 5534 viết xong — 9 CHƯƠNG!")
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
    if ws.cell(row=r, column=2).value and str(ws.cell(row=r, column=2).value).strip() == "5534":
        ws.cell(row=r, column=6).value = 9
        ws.cell(row=r, column=12).value = "Thạc sĩ Dược bị GĐ R&D cướp công thức serum chiết xuất sen Tây Hồ. Tự lập thương hiệu LinhSen, phát hiện sản phẩm đạo gây dị ứng hàng loạt, GlowMax bồi thường."
        ws.cell(row=r, column=13).value = "REWRITE TOÀN BỘ: 10 chương quá ngắn → 9 CHƯƠNG ĐẦY ĐẶN"
        ws.cell(row=r, column=14).value = "☑️ Đã sửa"
        print(f"  ✅ Excel updated row {r}")
        break
wb.save("danh_sach_truyen_doctieuthuyet.xlsx")
print("\n✅ HOÀN THÀNH TRUYỆN 5534!")
