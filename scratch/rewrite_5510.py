import json, urllib.request, openpyxl

story_data = {
    "secret_token": "ZEN_TRUYEN_2026_BYPASS",
    "story_id": 5510,
    "title": "Bị Đạo Toàn Bộ Thiết Kế Bảo Tàng, Tôi Xây Công Trình Khiến Thằng Đạo Nhái Bị Cấm Hành Nghề",
    "intro": "<p>Nguyễn Thanh Vân — kiến trúc sư trẻ ở TP.HCM — bị đồng nghiệp cấp trên đánh cắp toàn bộ thiết kế Bảo tàng Lịch sử Miền Nam. Khi bản thiết kế đạo nhái đoạt giải kiến trúc quốc gia, Vân quyết định chứng minh bản quyền bằng metadata file gốc — và xây một công trình còn đẹp hơn.</p>",
    "author": "Nguyễn Thanh Vân",
    "chapters": []
}

chapters = [
    {
        "title": "Chương 1: Bản Vẽ Bị Đánh Cắp",
        "content": """<p>Nguyễn Thanh Vân biết mình bị đạo thiết kế khi xem truyền hình trực tiếp Lễ trao giải Kiến trúc Quốc gia.</p>

<p>Trên màn hình: Trần Đức Hùng — KTS trưởng, công ty Saigon Architects, sếp cũ của Vân — đứng trên sân khấu Nhà hát Lớn TP.HCM, cầm cúp vàng, nụ cười rạng rỡ. Bản thiết kế chiếu trên màn hình lớn phía sau: Bảo tàng Lịch sử Miền Nam — công trình hình hoa sen cách điệu, mặt đứng kính phản quang, mái cong uốn lượn mô phỏng sóng sông Sài Gòn.</p>

<p>Đó là thiết kế của Vân. Từng đường nét, từng tỷ lệ, từng chi tiết — cô vẽ trong hai năm, từ sketch tay đến 3D model trên Revit và Rhino.</p>

<p>Vân hai mươi tám tuổi, tốt nghiệp Đại học Kiến trúc TP.HCM, thạc sĩ Kiến trúc từ Đại học Kỹ thuật Delft (Hà Lan). Cô vào Saigon Architects khi hai mươi lăm tuổi — công ty KTS lớn nhất miền Nam, chuyên thiết kế công trình công cộng.</p>

<p>Dự án Bảo tàng Lịch sử Miền Nam — công trình trọng điểm của TP.HCM, ngân sách hai nghìn tỷ đồng — được giao cho nhóm thiết kế do Vân dẫn đầu. Cô là người vẽ concept, phát triển mặt đứng, thiết kế kết cấu mái, và giải quyết bài toán kỹ thuật phức tạp nhất: làm sao để mái cong vượt nhịp bốn mươi mét mà không cần cột chống (free-span).</p>

<p>Giải pháp của Vân: shell structure — kết cấu vỏ mỏng bằng thép và bê tông cốt sợi thủy tinh (GFRC), tự chịu lực bằng hình dạng cong, không cần cột. Cô nghiên cứu từ công trình TWA Terminal (Eero Saarinen) và Sydney Opera House (Jørn Utzon) — rồi phát triển giải pháp riêng cho khí hậu nhiệt đới Sài Gòn.</p>

<p>Hai năm vẽ. Hàng nghìn giờ trên Revit. Ba mươi bản render. Và khi hoàn thành — KTS trưởng Hùng nói: "Vân, anh sẽ trình bày dự án cho Hội đồng. Em tập trung vẽ chi tiết thi công nhé."</p>

<p>Vân đồng ý — vì trong ngành kiến trúc Việt Nam, KTS trưởng trình bày là bình thường. Nhưng cô không ngờ: Hùng trình bày dưới tên mình, nộp hồ sơ dự thi Giải Kiến trúc Quốc gia dưới tên mình, và khi đoạt giải — không nhắc tên Vân.</p>

<p>"Bản thiết kế này là tác phẩm của nhóm Saigon Architects, do tôi — Trần Đức Hùng — chỉ đạo thiết kế."</p>

<p>Chỉ đạo thiết kế. Không phải "thiết kế." Một từ — nhưng đủ để ăn cắp hai năm làm việc của cô.</p>

<p>Vân tắt TV. Mở laptop. Kiểm tra: file gốc trên Revit — metadata rõ ràng: "Created by: Nguyen Thanh Van. Created date: 15/03/2021. Last modified by: Nguyen Thanh Van." Hàng nghìn revision, mỗi revision có tên cô.</p>

<p>Hùng không bao giờ mở file. Ông ta chỉ xem bản render PDF mà Vân gửi — rồi nộp dưới tên mình.</p>"""
    },
    {
        "title": "Chương 2: Mẹ Và Ngôi Nhà Lá",
        "content": """<p>Vân yêu kiến trúc vì mẹ.</p>

<p>Bà Nguyễn Thị Mai — năm mươi lăm tuổi, bán bún ở chợ Tân Định — nuôi Vân một mình từ khi bố mất. Bà sống trong ngôi nhà lá ở hẻm nhỏ quận 1 — nhà rộng mười lăm mét vuông, mái lá dừa nước, vách tôn, nền xi măng. Mùa mưa dột, mùa nắng nóng, gió lùa tứ phía.</p>

<p>"Mẹ ơi, lớn lên con xây nhà mới cho mẹ."</p>

<p>"Nhà lá cũng là nhà, con ơi. Có mái che mưa, có chỗ ngủ — là đủ."</p>

<p>Nhưng Vân không đồng ý "đủ." Mười hai tuổi, cô bắt đầu vẽ — vẽ nhà cho mẹ trên giấy vở học sinh, bằng bút chì 2B. Ngôi nhà nhỏ, hai tầng, có ban công trồng hoa, có cửa sổ lớn đón gió — vì mẹ thích gió.</p>

<p>Mười tám tuổi, Vân thi vào Đại học Kiến trúc TP.HCM — đậu thủ khoa. Sáu năm (cử nhân + thạc sĩ), cô vừa học vừa làm render 3D freelance kiếm tiền — ban đêm render nhà cho người ta, ban ngày vẽ nhà trong mơ cho mẹ.</p>

<p>Khi Vân tốt nghiệp thạc sĩ Delft, cô gửi tiền về xây lại nhà cho mẹ — ngôi nhà nhỏ ba mươi mét vuông, hai tầng, ban công trồng hoa, cửa sổ lớn đón gió. Đúng bản vẽ năm mười hai tuổi — chỉ chuyên nghiệp hơn.</p>

<p>Bà Mai khóc khi bước vào nhà mới: "Con ơi, con xây nhà đẹp quá. Đẹp hơn nhà ai trong hẻm."</p>

<p>"Mẹ xứng đáng, mẹ ơi."</p>

<p>Giờ đây, khi Hùng ăn cắp thiết kế bảo tàng, Vân không chỉ mất một dự án — cô mất niềm tin vào nghề. Nghề mà cô yêu từ năm mười hai tuổi, nghề mà mẹ hy sinh bán bún để cô được học.</p>

<p>"Mẹ ơi, người ta ăn cắp bản vẽ của con."</p>

<p>"Con ơi, người ta ăn cắp bản vẽ — nhưng không ăn cắp được cái đầu con. Con vẽ lại — đẹp hơn."</p>"""
    },
    {
        "title": "Chương 3: Chứng Minh Bằng Metadata",
        "content": """<p>Vân không kiện ngay — cô cần bằng chứng chắc chắn trước.</p>

<p>File Revit gốc: metadata "Created by: Nguyen Thanh Van" không thể sửa mà không để lại dấu vết. Revision history trên BIM 360 (Autodesk cloud) — ghi lại mỗi lần save, mỗi thay đổi, tên người thực hiện, timestamp chính xác đến giây. Hai năm revision history: hàng nghìn bản ghi, tất cả tên Vân.</p>

<p>Sketch tay: Vân có thói quen vẽ concept bằng bút chì trên giấy tracing trước khi lên máy. Ba mươi tờ sketch, mỗi tờ có chữ ký và ngày tháng ở góc phải — thói quen từ thời Delft, thầy hướng dẫn dạy: "Always sign and date your sketches. It's your intellectual fingerprint."</p>

<p>Email nội bộ: Vân gửi bản render cho Hùng qua email công ty — mỗi email có timestamp, tên file đính kèm, và nội dung: "Anh Hùng, em gửi bản render Bảo tàng Lịch sử Miền Nam — version 12. Xin anh review."</p>

<p>Hùng chưa bao giờ reply bằng góp ý thiết kế — chỉ reply: "OK" hoặc "Đẹp." Vì ông ta không biết góp ý — ông ta là KTS quản lý, không phải KTS thiết kế. Ông ta giỏi pitch dự án, giỏi quan hệ khách hàng — nhưng không vẽ được một mặt bằng hoàn chỉnh.</p>

<p>Vân liên hệ luật sư — Hoàng Thị Minh Ngọc, luật sư sở hữu trí tuệ chuyên về kiến trúc. Ngọc review bằng chứng:</p>

<p>"Vân, em có bộ bằng chứng gần như hoàn hảo: metadata file gốc, revision history trên cloud, sketch tay có chữ ký, email nội bộ. Hùng không thể phản bác — vì ông ta không có bất kỳ file nào mang tên mình."</p>

<p>"Chị ơi, em kiện Hùng hay kiện công ty?"</p>

<p>"Cả hai. Hùng — vi phạm quyền tác giả. Saigon Architects — vi phạm vì không bảo vệ quyền sở hữu trí tuệ của nhân viên."</p>

<p>Đồng thời, Vân gửi đơn khiếu nại đến Hội Kiến trúc sư Việt Nam và UIA (International Union of Architects) — yêu cầu rà soát hồ sơ dự thi Giải Kiến trúc Quốc gia.</p>"""
    },
    {
        "title": "Chương 4: Hùng Phản Công",
        "content": """<p>Khi biết Vân khiếu nại, Hùng phản ứng nhanh.</p>

<p>Bước một: Hùng gửi email nội bộ toàn công ty Saigon Architects — tuyên bố: "Dự án Bảo tàng là sản phẩm tập thể. Không cá nhân nào có quyền nhận toàn bộ công trạng. KTS Nguyễn Thanh Vân là thành viên nhóm — nhưng concept, chỉ đạo thiết kế, và giải pháp kỹ thuật do tôi phụ trách."</p>

<p>Bước hai: Hùng liên hệ Hội đồng Giải Kiến trúc Quốc gia, nộp "bằng chứng" — một số file PDF render mà Hùng tự đổi metadata bằng công cụ online (PDF Metadata Editor). Nhưng Hùng quên: PDF có thể đổi metadata, còn file Revit trên BIM 360 cloud thì không — vì Autodesk giữ log server-side, không ai sửa được.</p>

<p>Bước ba: Hùng gọi Vân.</p>

<p>"Vân, em nên rút đơn. Anh không muốn chuyện này ầm ĩ — xấu mặt cả hai."</p>

<p>"Anh Hùng, anh ăn cắp hai năm làm việc của em. Em không rút."</p>

<p>"Em chỉ là nhân viên. Thiết kế tạo ra trong thời gian làm việc thuộc quyền sở hữu của công ty — theo hợp đồng lao động."</p>

<p>"Đúng, thiết kế thuộc công ty — không phải thuộc ANH. Anh nộp dự thi dưới tên cá nhân anh, không phải tên công ty. Anh vi phạm cả hợp đồng với công ty lẫn quyền tác giả của em."</p>

<p>Hùng im lặng. Vì Vân đúng — ông ta nộp dự thi dưới tên "KTS Trần Đức Hùng," không phải "Saigon Architects." Đó là lỗi chết người: ông ta vừa ăn cắp của nhân viên, vừa ăn cắp của công ty.</p>

<p>Saigon Architects — khi biết Hùng nộp dự thi dưới tên cá nhân — lập tức sa thải Hùng và đứng về phía Vân trong vụ kiện.</p>

<p>Hùng mất việc, mất đồng minh, và mất luôn luật sư (vì công ty ngừng trả phí pháp lý cho ông ta).</p>"""
    },
    {
        "title": "Chương 5: Hùng Bị Cấm Hành Nghề",
        "content": """<p>Hội Kiến trúc sư Việt Nam và UIA cùng rà soát hồ sơ.</p>

<p>Bằng chứng của Vân: không thể bác bỏ. BIM 360 revision history — Autodesk cung cấp log chính thức theo yêu cầu pháp lý — xác nhận: Trần Đức Hùng chưa bao giờ mở file Revit dự án Bảo tàng. Ông ta chỉ nhận file PDF render qua email và nộp dự thi.</p>

<p>Hội KTS Việt Nam tuyên bố: thu hồi Giải Kiến trúc Quốc gia đã trao cho Trần Đức Hùng, trao lại cho Nguyễn Thanh Vân — tác giả thực sự.</p>

<p>UIA gửi thông báo đến 124 hội KTS thành viên trên toàn thế giới: Trần Đức Hùng bị đưa vào danh sách "vi phạm đạo đức nghề nghiệp" — tương đương cấm hành nghề quốc tế.</p>

<p>Tòa án TP.HCM xét xử bổ sung: Hùng bị phạt hành chính một trăm triệu đồng và bồi thường Vân năm trăm triệu đồng.</p>

<p>Hùng — năm mươi hai tuổi, ba mươi năm hành nghề, chứng chỉ hành nghề KTS hạng I — bị tước chứng chỉ. Không còn được ký tên trên bất kỳ bản vẽ nào tại Việt Nam.</p>

<p>Vân nhận cúp Giải Kiến trúc Quốc gia — lễ trao riêng, không hoành tráng như lần đầu, chỉ có Hội đồng giám khảo và vài phóng viên. Nhưng Vân không cần hoành tráng — cô cần công bằng.</p>

<p>"Cảm ơn Hội đồng. Giải thưởng này nhắc nhở chúng ta: trong kiến trúc, tên trên bản vẽ phải là tên người vẽ — không phải tên người ký."</p>"""
    },
    {
        "title": "Chương 6: Văn Phòng KTS Riêng",
        "content": """<p>Vân rời Saigon Architects — không phải vì bất mãn, mà vì đã đến lúc đi riêng.</p>

<p>Văn phòng KTS Thanh Vân: căn hộ năm mươi mét vuông ở Thảo Điền, quận 2 — Vân thuê, cải tạo thành studio thiết kế. Bàn vẽ lớn, hai máy tính workstation, máy in A0, và một bức tường trắng dài sáu mét để treo bản vẽ.</p>

<p>Đội ngũ: ba KTS trẻ — Linh (bạn học Kiến trúc), Dũng (cựu đồng nghiệp Saigon Architects), và Hà (sinh viên mới tốt nghiệp Delft, Vân quen khi du học). Quy tắc Vân đặt ra: "Tên trên bản vẽ là tên người vẽ. Không bao giờ đặt tên sếp nếu sếp không vẽ."</p>

<p>Dự án đầu tiên: Trung tâm Cộng đồng Thủ Thiêm — công trình nhỏ hơn bảo tàng, ngân sách vừa phải, nhưng Vân thiết kế với cùng tâm huyết: mái cong bằng tre đan (thay thép — rẻ hơn, bền vững hơn), mặt đứng gạch nung thủ công từ Vĩnh Long, và khoảng sân trong trồng cây xanh để thông gió tự nhiên — giảm điều hòa, phù hợp khí hậu nhiệt đới.</p>

<p>Công trình hoàn thành trong mười tám tháng — và đoạt giải Architecture Asia Awards — hạng mục công trình cộng đồng tốt nhất Đông Nam Á.</p>

<p>Tạp chí ArchDaily đăng bài: "A Young Vietnamese Architect's Response to Plagiarism: Build Something Better." Dezeen feature, Archinect share.</p>

<p>Vân không đề cập vụ đạo nhái trong phỏng vấn — cô chỉ nói về công trình: "Kiến trúc Việt Nam cần dùng vật liệu Việt Nam. Tre, gạch, đá ong — tất cả đều đẹp nếu KTS biết cách dùng."</p>"""
    },
    {
        "title": "Chương 7: Venice Architecture Biennale",
        "content": """<p>Venice Architecture Biennale 2025 — triển lãm kiến trúc lớn nhất thế giới, tổ chức hai năm một lần tại Venice, Ý.</p>

<p>Gian hàng Việt Nam — do Hội KTS Việt Nam tổ chức — mời Vân trưng bày Trung tâm Cộng đồng Thủ Thiêm và bản thiết kế Bảo tàng Lịch sử Miền Nam (bản gốc, tên Vân).</p>

<p>Vân đến Venice lần đầu — thành phố nổi, kênh đào, cầu đá, và kiến trúc Gothic hàng nghìn năm tuổi. Cô đứng trước gian hàng Việt Nam — nhỏ nhất khu Arsenal, nhưng thu hút đông khách tham quan nhất.</p>

<p>Vì câu chuyện: một KTS trẻ bị đạo thiết kế, đấu tranh lấy lại bản quyền, rồi xây một công trình còn đẹp hơn — câu chuyện mà KTS toàn thế giới đồng cảm, vì đạo nhái thiết kế là vấn nạn toàn cầu.</p>

<p>Curators từ MoMA (New York) dừng lại, xem mô hình Trung tâm Cộng đồng Thủ Thiêm — mái tre cong, gạch nung, sân trong xanh mướt.</p>

<p>"This is remarkable. The structure is minimal but the spatial quality is extraordinary. How did you achieve this curvature with bamboo?"</p>

<p>"We worked with bamboo artisans from Bình Dương — they've been bending bamboo for furniture for three generations. We adapted their technique for structural bamboo."</p>

<p>MoMA đề nghị đưa mô hình Thủ Thiêm vào triển lãm thường trực "Architecture of Community" — bên cạnh công trình của Tadao Ando và Shigeru Ban.</p>

<p>Vân gọi mẹ từ Venice:</p>

<p>"Mẹ ơi, mô hình công trình con thiết kế sẽ ở MoMA, New York."</p>

<p>"MoMA là gì, con?"</p>

<p>"Là bảo tàng nghệ thuật lớn nhất thế giới, mẹ."</p>

<p>"Vậy con giỏi lắm. Nhưng con ăn cơm chưa? Ở Ý có phở không?"</p>

<p>Vân cười. "Không có phở, mẹ. Nhưng có pasta — cũng ngon."</p>"""
    },
    {
        "title": "Chương 8: Đi Qua Bảo Tàng",
        "content": """<p>Bảo tàng Lịch sử Miền Nam — công trình mà Vân thiết kế — cuối cùng được xây dựng. Không phải bản đạo nhái của Hùng (đã bị hủy), mà bản gốc của Vân — có sửa đổi nhỏ theo yêu cầu kỹ thuật, nhưng giữ nguyên concept: hình hoa sen cách điệu, mái shell structure vượt nhịp bốn mươi mét, mặt đứng kính phản chiếu sông Sài Gòn.</p>

<p>KTS chỉ đạo xây dựng: Nguyễn Thanh Vân — lần đầu tiên tên cô đứng trên biển công trình trọng điểm quốc gia.</p>

<p>Ngày khánh thành — Vân đứng trước bảo tàng, nhìn mái cong vươn lên trời Sài Gòn, kính phản quang phản chiếu mây trắng và sông xanh. Công trình đẹp hơn bản render — vì kiến trúc thật luôn đẹp hơn hình ảnh, khi ánh sáng, gió, và con người đi qua nó.</p>

<p>Mẹ đứng cạnh — bà Mai, sáu mươi tuổi, mặc áo dài xanh, tay cầm bó hoa. Bà nhìn bảo tàng, nhìn tên con gái trên biển, và nước mắt chảy.</p>

<p>"Con ơi, ngày xưa con vẽ nhà cho mẹ trên giấy vở. Giờ con vẽ bảo tàng cho cả thành phố."</p>

<p>"Mẹ ơi, nhà mẹ vẫn đẹp hơn bảo tàng."</p>

<p>"Con nói bậy."</p>

<p>"Thật mà. Vì nhà mẹ, con vẽ bằng tình yêu. Bảo tàng, con vẽ bằng chuyên môn. Tình yêu lúc nào cũng đẹp hơn chuyên môn."</p>

<hr>

<p>Tối hôm đó, Vân đi bộ một mình quanh bảo tàng. Đèn chiếu lên mái cong, bóng sen in trên mặt nước hồ nhân tạo. Gió sông Sài Gòn thổi nhẹ, mang theo mùi phù sa.</p>

<p>Cô ngồi trên bậc thang bảo tàng, mở sổ sketch — cuốn sổ giấy tracing mà cô mang theo từ Delft. Lật đến trang đầu tiên: sketch concept bảo tàng, vẽ bằng bút chì 2B, góc phải: "Nguyen Thanh Van, 15/03/2021."</p>

<p>Bốn năm trước, cô vẽ trang này trong ký túc xá Delft, nhìn ra kênh đào Hà Lan, và mơ về một bảo tàng bên sông Sài Gòn. Giờ bảo tàng đó đứng trước mặt cô — bằng thép, kính, và bê tông — và mang tên cô.</p>

<p>Cô gấp sổ, đứng dậy, đi về phía sông. Sài Gòn đêm — đèn lung linh trên mặt nước, tàu chở hàng chầm chậm trôi, tiếng còi xa xa.</p>

<p>Và bảo tàng sau lưng cô — hình hoa sen, mái cong, ánh sáng ấm — đứng vững vàng bên sông, như thể nó đã ở đó từ luôn.</p>

<p>Vì kiến trúc tốt là thế: nó trông như thể nó đã luôn thuộc về nơi đó — dù ai vẽ nó đã phải chiến đấu để nó tồn tại.</p>"""
    }
]

story_data["chapters"] = chapters

print("✅ Truyện 5510 viết xong — 8 CHƯƠNG!")
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
    if ws.cell(row=r, column=2).value and str(ws.cell(row=r, column=2).value).strip() == "5510":
        ws.cell(row=r, column=6).value = 8
        ws.cell(row=r, column=12).value = "KTS trẻ TPHCM bị sếp cũ đạo thiết kế bảo tàng dự thi giải quốc gia. Chứng minh bằng BIM metadata, sếp bị cấm hành nghề, công trình gốc được MoMA trưng bày."
        ws.cell(row=r, column=13).value = "REWRITE TOÀN BỘ: 10 chương quá ngắn → 8 CHƯƠNG ĐẦY ĐẶN"
        ws.cell(row=r, column=14).value = "☑️ Đã sửa"
        print(f"  ✅ Excel updated row {r}")
        break
wb.save("danh_sach_truyen_doctieuthuyet.xlsx")
print("\n✅ HOÀN THÀNH TRUYỆN 5510!")
