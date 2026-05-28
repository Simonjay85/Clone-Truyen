import json, urllib.request, openpyxl

story_data = {
    "secret_token": "ZEN_TRUYEN_2026_BYPASS",
    "story_id": 5546,
    "title": "Bị Đạo Toàn Bộ Tiểu Thuyết Bestseller, Tôi Viết Phần Tiếp Theo Khiến Bản Đạo Phải Rút Khỏi Kệ Sách",
    "intro": "<p>Đỗ Hoàng Anh — nhà văn tự do ở Sài Gòn — mất ba năm viết tiểu thuyết \"Mùa Gió Chướng,\" gửi bản thảo cho nhà xuất bản Sông Hồng. Sáu tháng sau, cuốn sách xuất hiện trên kệ — nhưng tên tác giả không phải Hoàng Anh. Tên trên bìa: Trần Quốc Phúc, biên tập viên NXB Sông Hồng.</p>\n<p>Phúc đạo toàn bộ — từ cốt truyện, nhân vật, đến từng câu thoại — chỉ đổi tên tác giả và sửa vài chi tiết nhỏ. Cuốn sách trở thành bestseller, bán năm mươi nghìn bản.</p>\n<p>Nhưng Hoàng Anh có một vũ khí mà kẻ đạo văn không có: phần tiếp theo của câu chuyện — phần mà chỉ người viết thật mới biết.</p>",
    "author": "Đỗ Hoàng Anh",
    "chapters": []
}

chapters = [
    {
        "title": "Chương 1: Bestseller Của Người Khác",
        "content": """<p>Đỗ Hoàng Anh biết mình bị đạo văn khi đứng trong nhà sách Fahasa Nguyễn Huệ.</p>

<p>Cô hai mươi sáu tuổi, tóc ngắn, đeo kính cận, mặc áo thun cũ, tay cầm ly cà phê sữa đá — đang đi dạo nhà sách sau giờ làm thêm ở quán phở. Cô viết tiểu thuyết ban đêm, làm phục vụ quán phở ban ngày — cuộc sống của nhà văn tự do ở Sài Gòn: lãng mạn trên giấy, khốn khổ ngoài đời.</p>

<p>Góc "Sách Bán Chạy" — bìa đỏ, chữ vàng, xếp chồng cao: "Mùa Gió Chướng" — Trần Quốc Phúc.</p>

<p>Hoàng Anh cầm cuốn sách lên. Lật trang đầu. Đọc dòng đầu tiên:</p>

<p>"Tháng Chạp, gió chướng từ biển Đông thổi ngược sông Mekong, mang theo mùi muối mặn và lời hứa của những người không bao giờ trở về."</p>

<p>Đó là câu mở đầu cô viết — viết lúc ba giờ sáng, trong phòng trọ mười lăm mét vuông ở quận 4, trên chiếc laptop Asus cũ bàn phím đã mòn chữ. Cô nhớ rõ vì cô đã sửa câu này mười bảy lần trước khi hài lòng.</p>

<p>Cô lật tiếp. Chương 1: "Cô gái bên bến đò." Chương 2: "Ông Hai và con trâu sừng gãy." Chương 3: "Đêm trăng ở ruộng tôm."</p>

<p>Tất cả. Mọi chương. Mọi nhân vật. Mọi câu thoại. Giống hệt bản thảo cô gửi cho NXB Sông Hồng sáu tháng trước — chỉ khác: tên tác giả trên bìa là Trần Quốc Phúc, và một số chi tiết nhỏ bị sửa (tên nhân vật phụ, tên địa danh) để tránh bị so sánh trực tiếp.</p>

<p>Hoàng Anh đứng giữa nhà sách, tay cầm cuốn sách, chân run. Không phải vì buồn — mà vì giận. Giận đến mức cô muốn hét lên giữa nhà sách: "Đây là sách của tôi! Tôi viết! Ba năm! Ba nghìn giờ! Và thằng này ăn cắp!"</p>

<p>Nhưng cô không hét. Cô mua một bản — bốn mươi lăm nghìn đồng — và đi về phòng trọ.</p>

<p>Đêm đó, cô ngồi đọc lại "Mùa Gió Chướng" — bản của Phúc — từ đầu đến cuối, đánh dấu từng câu bị sửa, từng chi tiết bị đổi. Kết quả: chín mươi lăm phần trăm giống nguyên bản của cô. Năm phần trăm bị sửa — chủ yếu là tên nhân vật phụ và một số đoạn miêu tả cảnh.</p>

<p>Cô mở laptop, tìm file gốc — bản thảo "Mùa Gió Chướng" mà cô gửi cho NXB Sông Hồng qua email ngày mười lăm tháng Ba. Email vẫn còn trong thư mục "Đã gửi," kèm file đính kèm .docx, timestamp rõ ràng — sáu tháng trước khi cuốn sách của Phúc ra mắt.</p>

<p>"Mày ăn cắp sách tao, Phúc. Nhưng mày không ăn cắp được phần tiếp theo."</p>"""
    },
    {
        "title": "Chương 2: Bằng Chứng Trong Email",
        "content": """<p>Hoàng Anh gọi luật sư — Nguyễn Thị Thanh Hương, luật sư sở hữu trí tuệ, quen qua hội nhóm nhà văn trẻ trên Facebook.</p>

<p>Hương ba mươi hai tuổi, tốt nghiệp Luật TP.HCM, chuyên về bản quyền và sở hữu trí tuệ — thường bảo vệ nhạc sĩ, nhà văn, và nghệ sĩ bị đạo nhái.</p>

<p>"Chị Hương, em bị đạo văn. Toàn bộ tiểu thuyết."</p>

<p>"Em có bằng chứng gì?"</p>

<p>"Email gửi bản thảo cho NXB ngày mười lăm tháng Ba — sáu tháng trước khi sách của Phúc phát hành. File .docx gốc, metadata cho thấy em tạo file từ hai năm trước. Và version history trên Google Docs — em soạn bản thảo trên đó suốt ba năm, có hàng trăm lần chỉnh sửa với timestamp."</p>

<p>"Tuyệt vời. Đó là bằng chứng gốc. Phúc không thể có version history — vì y không viết."</p>

<p>"Chị ơi, nhưng em gửi bản thảo cho NXB — Phúc là biên tập viên NXB. Y nhận bản thảo, đọc, rồi copy, sửa tên, nộp cho NXB dưới tên y. Và NXB Sông Hồng — Giám đốc Lê Hải — có thể biết hoặc không biết."</p>

<p>"Em có email nào từ NXB phản hồi bản thảo không?"</p>

<p>"Có. NXB từ chối bản thảo của em ngày hai mươi tháng Tư — email từ Phúc, ký tên 'Biên tập viên Trần Quốc Phúc,' viết: 'Bản thảo chưa phù hợp với định hướng xuất bản. Xin cảm ơn.' Và năm tháng sau, sách xuất hiện — cùng nội dung, khác tên tác giả."</p>

<p>Hương gật đầu: "Rõ ràng. Phúc nhận bản thảo, từ chối để em không nghi ngờ, rồi copy và đăng dưới tên mình. Đây là hành vi vi phạm quyền tác giả theo Luật Sở hữu Trí tuệ, Điều 28."</p>

<p>"Chị ơi, NXB có trách nhiệm không?"</p>

<p>"Nếu NXB biết — đồng phạm. Nếu NXB không biết — vẫn có trách nhiệm liên đới vì không kiểm tra nguồn gốc bản thảo. Một NXB chuyên nghiệp phải verify tác giả — đặc biệt khi biên tập viên của mình nộp bản thảo."</p>

<p>Hương soạn đơn kiện. Hoàng Anh cung cấp: email gốc (timestamp), file .docx gốc (metadata), Google Docs version history (ba năm soạn thảo), và bản so sánh song song giữa bản gốc và bản của Phúc (chín mươi lăm phần trăm trùng khớp).</p>

<p>"Em, chị cần thêm một thứ: nhân chứng. Ai đã đọc bản thảo của em trước khi em gửi NXB?"</p>

<p>"Mẹ em. Bạn em — Linh, nhà văn, đọc bản nháp chương 1 đến 5 và góp ý. Và ông ngoại em — ông đọc bản hoàn chỉnh trước khi em gửi, vì truyện lấy cảm hứng từ cuộc đời ông."</p>"""
    },
    {
        "title": "Chương 3: Ông Ngoại Và Chiếc Radio Sanyo",
        "content": """<p>Hoàng Anh viết "Mùa Gió Chướng" vì ông ngoại.</p>

<p>Ông Đỗ Văn Tám — nông dân Cần Thơ, tám mươi hai tuổi, sống ở ấp Bình Hòa bên sông Hậu. Ông trồng lúa, nuôi tôm, và mỗi chiều ngồi bên hiên nhà, bật chiếc radio Sanyo cũ nghe cải lương.</p>

<p>Chiếc radio Sanyo — mua năm 1978, màu nâu, ăng-ten gãy, loa rè — là thứ duy nhất ông giữ lại từ thời trẻ. Ông mua nó bằng tiền bán vụ lúa đầu tiên sau giải phóng — hai ký vàng, đổi lấy radio và một chiếc xe đạp Phượng Hoàng.</p>

<p>Mỗi mùa hè, Hoàng Anh về Cần Thơ ở với ông ngoại — ngủ trong nhà sàn, ăn cơm với cá lóc nướng trui, và nghe ông kể chuyện. Ông kể về chiến tranh, về những năm đói, về bà ngoại mất sớm vì bệnh mà không có thuốc, về mùa lũ năm 2000 nước ngập đến ngực nhà sàn.</p>

<p>Nhưng ông kể nhiều nhất về gió chướng — gió từ biển Đông thổi ngược sông Mekong mỗi tháng Chạp, mang nước mặn vào ruộng lúa, giết cây trồng, nhưng cũng mang tôm cá từ biển vào sông.</p>

<p>"Gió chướng là vậy đó, con. Nó phá hoại, nhưng nó cũng nuôi sống. Người miền Tây sống với gió chướng — không chống, không chạy — mà sống cùng. Khi nước mặn vào, mình không trồng lúa — mình nuôi tôm. Khi nước mặn rút, mình trồng lúa lại. Đó là cách người miền Tây tồn tại: uốn theo gió, không gãy."</p>

<p>Hoàng Anh viết "Mùa Gió Chướng" từ những câu chuyện đó — ba năm thu thập, ghi chép, sắp xếp, và viết. Nhân vật chính — ông Hai, nông dân sống bên sông Hậu — được xây dựng từ ông ngoại. Con trâu sừng gãy trong truyện là con trâu thật mà ông ngoại nuôi năm 1985, bị gãy sừng vì húc cọc rào. Cô gái bên bến đò là bà ngoại — người mà ông gặp lần đầu khi bà đứng chờ đò qua sông, chiều tháng Giêng, tóc bay trong gió.</p>

<p>Khi Phúc ăn cắp "Mùa Gió Chướng," hắn không chỉ ăn cắp một cuốn tiểu thuyết — hắn ăn cắp cuộc đời ông ngoại Hoàng Anh. Hắn ăn cắp chiếc radio Sanyo, con trâu sừng gãy, bà ngoại bên bến đò, và gió chướng tháng Chạp.</p>

<p>Và đó là lý do Hoàng Anh quyết không tha.</p>"""
    },
    {
        "title": "Chương 4: Cộng Đồng Văn Học Dậy Sóng",
        "content": """<p>Hoàng Anh đăng bài trên Facebook cá nhân — dài hai nghìn chữ, kèm ảnh chụp màn hình email gửi bản thảo, Google Docs version history, và bản so sánh song song (highlight vàng cho phần trùng khớp, đỏ cho phần Phúc sửa).</p>

<p>Tiêu đề: "Tôi viết 'Mùa Gió Chướng.' Trần Quốc Phúc ăn cắp nó."</p>

<p>Hai mươi bốn giờ: mười lăm nghìn share, hai nghìn comment, năm trăm nghìn lượt xem.</p>

<p>Cộng đồng văn học Việt Nam chia làm hai:</p>

<p>Phe ủng hộ Hoàng Anh: "Bằng chứng rõ ràng — email timestamp, Google Docs history, bản so sánh. Phúc đạo văn rõ ràng."</p>

<p>Phe hoài nghi: "Có thể hai người cùng viết ý tưởng tương tự? Cần chờ tòa xét xử." Nhưng phe này ít — vì chín mươi lăm phần trăm trùng khớp không phải "ý tưởng tương tự," đó là copy-paste.</p>

<p>Nhà văn Nguyễn Nhật Ánh — không bình luận trực tiếp, nhưng chia sẻ bài viết kèm một câu: "Đạo văn là tội ác — vì nó không chỉ ăn cắp chữ, mà ăn cắp thời gian, nước mắt, và linh hồn của người viết."</p>

<p>Phóng viên Tuổi Trẻ liên hệ Phúc — Phúc trả lời: "Tôi viết 'Mùa Gió Chướng' hoàn toàn độc lập. Cô Đỗ Hoàng Anh có gửi bản thảo cho NXB, nhưng bản thảo đó hoàn toàn khác cuốn sách của tôi. Sự trùng hợp là ngẫu nhiên."</p>

<p>"Trùng hợp chín mươi lăm phần trăm?" phóng viên hỏi.</p>

<p>"Tôi không bình luận thêm. Luật sư của tôi sẽ trả lời."</p>

<p>NXB Sông Hồng — Giám đốc Lê Hải — ra thông cáo: "NXB đang xác minh thông tin. Nếu phát hiện vi phạm, NXB sẽ xử lý nghiêm." Thông cáo nhạt, không đứng về bên nào.</p>

<p>Hoàng Anh đọc thông cáo và biết: NXB đang chờ xem gió chiều nào. Nếu dư luận quên, họ sẽ im. Nếu dư luận không quên, họ sẽ đổ lỗi cho Phúc.</p>

<p>"Chị Hương ơi, mình không chờ NXB. Mình đánh trực tiếp — bằng phần tiếp theo."</p>"""
    },
    {
        "title": "Chương 5: Viết Phần Tiếp Theo",
        "content": """<p>"Mùa Gió Chướng" kết thúc mở — ông Hai đứng bên sông Hậu, nhìn gió chướng tháng Chạp, tay cầm lá thư của con trai từ Sài Gòn, và một câu hỏi: "Ông sẽ bán đất, lên thành phố sống với con — hay ở lại, giữ ruộng, và chờ gió chướng mùa sau?"</p>

<p>Phúc không biết câu trả lời — vì hắn không viết câu hỏi đó. Hắn copy câu hỏi từ bản thảo của Hoàng Anh — nhưng Hoàng Anh đã viết câu trả lời. Phần hai — "Mùa Nước Lên" — nằm trong đầu cô, trong cuốn sổ ghi chép, trong những đêm nói chuyện với ông ngoại.</p>

<p>Hoàng Anh viết "Mùa Nước Lên" trong hai tháng — nhanh hơn phần một (ba năm), vì cô đã biết nhân vật, biết thế giới, biết giọng kể. Cô chỉ cần viết tiếp — và viết với sự giận dữ thầm lặng mà chỉ người bị ăn cắp mới hiểu.</p>

<p>"Mùa Nước Lên" — phần hai, mười hai chương, ba trăm trang:</p>

<p>Ông Hai quyết định ở lại. Bán một phần đất, giữ phần còn lại, chuyển sang nuôi tôm sinh thái — loại tôm nuôi theo chuẩn quốc tế, giá gấp ba tôm thường. Con trai từ Sài Gòn về giúp — anh ta là kỹ sư IT, dùng sensor IoT theo dõi chất lượng nước. Hai cha con — nông dân và kỹ sư — hợp tác xây mô hình nông nghiệp thông minh bên sông Hậu.</p>

<p>Và xen kẽ: câu chuyện tình giữa con trai ông Hai và cô giáo trường làng — cô gái bên bến đò thế hệ mới.</p>

<p>Hoàng Anh gửi bản thảo cho NXB Trẻ — không phải Sông Hồng. NXB Trẻ đọc, hiểu câu chuyện, hiểu context đạo văn, và quyết định xuất bản ngay — kèm ghi chú trên bìa: "Phần hai của 'Mùa Gió Chướng' — tác phẩm gốc của Đỗ Hoàng Anh."</p>

<p>"Mùa Nước Lên" phát hành cùng ngày Hoàng Anh đăng bài so sánh trên MXH: "Nếu Phúc viết 'Mùa Gió Chướng,' hãy viết phần tiếp theo. Nếu không viết được — vì không phải tác giả thì không biết câu chuyện đi đâu."</p>

<p>Phúc không viết được. Vì hắn không biết ông Hai chọn gì. Vì hắn không biết con trâu sừng gãy cuối cùng ra sao. Vì hắn không ngồi bên hiên nhà ông ngoại, nghe gió chướng, nghe cải lương trên chiếc radio Sanyo.</p>

<p>Chỉ người viết thật mới biết phần tiếp theo.</p>"""
    },
    {
        "title": "Chương 6: Phúc Và NXB Lĩnh Án",
        "content": """<p>Tòa án Nhân dân TP.HCM xét xử vụ kiện vi phạm quyền tác giả — Đỗ Hoàng Anh kiện Trần Quốc Phúc và NXB Sông Hồng.</p>

<p>Bằng chứng của Hoàng Anh: email gửi bản thảo (timestamp sáu tháng trước ngày phát hành sách Phúc), Google Docs version history (ba năm soạn thảo, hàng trăm lần chỉnh sửa), bản so sánh song song (chín mươi lăm phần trăm trùng khớp), và ba nhân chứng đã đọc bản thảo trước khi gửi NXB (mẹ, bạn Linh, ông ngoại).</p>

<p>Bằng chứng của Phúc: không có. Không có bản nháp, không có ghi chú, không có version history, không có nhân chứng. Phúc nói "viết trên giấy rồi đánh máy" — nhưng không có giấy. Phúc nói "viết trong ba tháng" — nhưng không giải thích được tại sao ba trăm trang trùng chín mươi lăm phần trăm với bản thảo mà cô Đỗ Hoàng Anh gửi cho NXB trước đó.</p>

<p>Luật sư Hương trình bày: "Kính thưa Hội đồng, đây không phải trùng hợp. Đây là copy-paste có chủ đích. Bị cáo Phúc nhận bản thảo với tư cách biên tập viên, từ chối xuất bản để nguyên đơn không nghi ngờ, rồi sao chép gần như nguyên văn và đăng ký dưới tên mình."</p>

<p>Phúc đứng trước vành móng ngựa, mặt cúi, tay nắm chặt. Luật sư của Phúc — do NXB thuê — cố gắng biện hộ: "Có thể hai tác giả cùng lấy cảm hứng từ đề tài nông thôn miền Tây." Nhưng thẩm phán hỏi: "Hai tác giả cùng viết câu mở đầu giống nhau, giống đến từng dấu phẩy?"</p>

<p>Luật sư im.</p>

<p>Tòa tuyên: Trần Quốc Phúc vi phạm quyền tác giả — bồi thường năm trăm triệu đồng cho Đỗ Hoàng Anh, thu hồi toàn bộ ấn phẩm "Mùa Gió Chướng" mang tên Phúc, và cấm Phúc hoạt động xuất bản ba năm.</p>

<p>NXB Sông Hồng — Giám đốc Lê Hải: bị phạt hành chính hai trăm triệu đồng vì thiếu trách nhiệm kiểm tra nguồn gốc bản thảo. Hải bị Bộ Thông tin & Truyền thông yêu cầu từ chức.</p>

<p>Năm mươi nghìn bản "Mùa Gió Chướng" mang tên Phúc: thu hồi, tiêu hủy.</p>

<p>Hoàng Anh đứng ngoài tòa, tay cầm bản sao quyết định. Linh — bạn cô — ôm chầm: "Anh thắng rồi!"</p>

<p>"Không phải anh thắng. Mùa Gió Chướng thắng. Câu chuyện của ông ngoại thắng."</p>"""
    },
    {
        "title": "Chương 7: Hội Sách Quốc Tế",
        "content": """<p>Sau phiên tòa, NXB Trẻ tái bản "Mùa Gió Chướng" dưới tên đúng: Đỗ Hoàng Anh. Bìa mới — tranh sông Hậu do họa sĩ Lê Thiết Cương vẽ riêng — đẹp hơn bản cũ của Phúc.</p>

<p>"Mùa Gió Chướng" + "Mùa Nước Lên" — bộ đôi tiểu thuyết bán tổng cộng một trăm nghìn bản trong sáu tháng. Nằm đầu bảng xếp hạng Fahasa mười hai tuần liên tiếp.</p>

<p>Công ty bản quyền sách Grayhawk Agency (Đài Loan) liên hệ — đề nghị mua bản quyền dịch sang tiếng Anh, tiếng Trung, tiếng Hàn. Hoàng Anh ký hợp đồng — lần đầu tiên cô có đại diện bản quyền quốc tế.</p>

<p>Bản tiếng Anh: "The Season of the Contrary Wind" — do Emily Wilson, dịch giả chuyên văn học Đông Nam Á, dịch. NXB Penguin Random House (Southeast Asia) phát hành.</p>

<p>Hội sách Quốc tế Frankfurt — Frankfurter Buchmesse, Đức — mời Hoàng Anh tham gia panel: "Voices from Southeast Asia: New Literary Voices."</p>

<p>Hoàng Anh đứng trên sân khấu Frankfurt — cô gái phục vụ quán phở ở quận 4, viết tiểu thuyết ban đêm, bị đạo văn, đấu tranh lấy lại tên mình — đứng trước ba trăm người từ năm mươi quốc gia.</p>

<p>"My grandfather told me stories by the Mekong river. I wrote them down. Someone stole them. But stories, like the river, always find their way home."</p>

<p>Vỗ tay.</p>

<p>Sau panel, một biên tập viên từ Nhà xuất bản Gallimard (Pháp) đến gặp: "We want to publish your novel in French. The Mekong is a universal river — every culture has one."</p>

<p>Hoàng Anh gọi ông ngoại từ Frankfurt — qua video call, ông ngồi bên hiên nhà, chiếc radio Sanyo bên cạnh.</p>

<p>"Ông ơi, sách của con được dịch ra tiếng Anh, tiếng Pháp, tiếng Hàn rồi!"</p>

<p>"Ông không hiểu tiếng Anh tiếng Pháp. Nhưng ông hiểu: con viết chuyện của ông, và người ta muốn đọc. Vậy là đủ."</p>"""
    },
    {
        "title": "Chương 8: Quay Về Phòng Trọ Quận 4",
        "content": """<p>Một năm sau Frankfurt.</p>

<p>Hoàng Anh có thể mua nhà rồi — tiền bản quyền từ ba quốc gia, tiền bồi thường từ Phúc, tiền bán sách trong nước — tổng cộng hơn hai tỷ đồng. Nhưng cô vẫn ở phòng trọ quận 4 — mười lăm mét vuông, quạt trần, cửa sổ nhìn ra hẻm.</p>

<p>"Sao em không dọn đi?" Linh hỏi.</p>

<p>"Vì em viết 'Mùa Gió Chướng' ở đây. Em viết 'Mùa Nước Lên' ở đây. Và em đang viết phần ba ở đây. Nếu dọn đi, em sợ mất giọng — giọng của người ở phòng trọ, ăn cơm bụi, viết lúc ba giờ sáng."</p>

<p>Phần ba: "Mùa Gặt" — phần cuối bộ ba, kể về thế hệ cháu ông Hai, đứa con gái lớn lên ở Sài Gòn, quay về miền Tây, học làm nông, và đối mặt với biến đổi khí hậu — nước biển dâng, đồng bằng mất dần, và câu hỏi: miền Tây có còn tồn tại trong năm mươi năm nữa?</p>

<p>Hoàng Anh viết mỗi đêm — từ mười giờ đến ba giờ sáng, giống như ba năm trước. Laptop Asus cũ vẫn dùng — bàn phím đã mòn thêm, chữ "A" và "E" gần như mất hẳn.</p>

<p>Mỗi tháng, cô về Cần Thơ thăm ông ngoại. Ông Tám tám mươi ba tuổi — chậm hơn, yếu hơn, nhưng vẫn ngồi bên hiên, vẫn bật radio Sanyo nghe cải lương.</p>

<p>"Ông ơi, con đang viết phần ba. Phần này có nhân vật mới — cháu gái ông Hai, tên Nhi."</p>

<p>"Nhi giống ai?"</p>

<p>"Giống con."</p>

<p>Ông cười. "Vậy Nhi chắc cũng ương ngạnh lắm."</p>

<p>"Dạ, ương ngạnh — nhưng không bỏ cuộc."</p>

<hr>

<p>Đêm, phòng trọ quận 4. Hoàng Anh ngồi trước laptop, mở file "Mùa Gặt — Chương 1." Cô viết dòng đầu tiên:</p>

<p>"Tháng Giêng, nước rút, đồng bằng lộ ra — nứt nẻ, khô cằn, nhưng dưới lớp bùn khô, hạt lúa vẫn nằm đó, chờ mưa."</p>

<p>Cô dừng, đọc lại, sửa. Rồi sửa nữa. Rồi sửa lần thứ ba — vì câu mở đầu phải hoàn hảo. Phải là câu mà khi ai đó đọc, họ biết ngay: đây là Đỗ Hoàng Anh viết.</p>

<p>Không ai có thể ăn cắp nữa. Vì giờ đây, cả thế giới biết giọng cô. Và giọng — không giống chữ — không ai copy được.</p>

<p>Gió từ cửa sổ thổi vào — gió Sài Gòn, nóng hầm hập, mang theo mùi hẻm: cơm chiên, nước mắm, và tiếng xe máy. Không phải gió chướng — nhưng cũng là gió. Gió của cuộc đời cô. Gió thổi qua phòng trọ mười lăm mét vuông, nơi một cô gái hai mươi bảy tuổi ngồi viết, và không định dừng.</p>"""
    }
]

story_data["chapters"] = chapters

with open("scratch/story_5546_rewrite.json", "w", encoding="utf-8") as f:
    json.dump(story_data, f, ensure_ascii=False, indent=2)

print("✅ Truyện 5546 viết xong — 8 CHƯƠNG!")
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
    if ws.cell(row=r, column=2).value and str(ws.cell(row=r, column=2).value).strip() == "5546":
        ws.cell(row=r, column=6).value = 8
        ws.cell(row=r, column=12).value = "Nhà văn trẻ SG bị biên tập viên NXB đạo toàn bộ tiểu thuyết. Viết phần tiếp theo chứng minh bản quyền, kẻ đạo lĩnh án, sách được dịch ra 3 ngoại ngữ."
        ws.cell(row=r, column=13).value = "REWRITE TOÀN BỘ: 10 chương quá ngắn → 8 CHƯƠNG ĐẦY ĐẶN"
        ws.cell(row=r, column=14).value = "☑️ Đã sửa"
        print(f"  ✅ Excel updated row {r}")
        break
wb.save("danh_sach_truyen_doctieuthuyet.xlsx")
print("\n✅ HOÀN THÀNH TRUYỆN 5546!")
