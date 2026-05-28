import json, urllib.request, openpyxl

story_data = {
    "secret_token": "ZEN_TRUYEN_2026_BYPASS",
    "story_id": 5558,
    "title": "Bị Ép Nghỉ Vì Dạy Giỏi Hơn Trưởng Khoa, Tôi Mở Học Viện Online Khiến Cả Khoa Mất Sinh Viên",
    "intro": "<p>Lý Minh Châu — giảng viên Kinh tế lượng, Đại học Kinh tế Quốc dân — bị ép nghỉ sau khi sinh viên gửi kiến nghị yêu cầu cô dạy thay PGS Trần Quốc Mạnh, Trưởng khoa Kinh tế. Lý do: bài giảng của cô hay hơn.</p>\n<p>PGS Mạnh coi đó là sỉ nhục — và dùng quyền Trưởng khoa đẩy cô ra khỏi trường. Nhưng Minh Châu không dừng: cô mở học viện online từ phòng ngủ, dạy miễn phí, và thu hút hai triệu sinh viên — trong khi lớp PGS Mạnh ngày càng vắng.</p>",
    "author": "Lý Minh Châu",
    "chapters": []
}

chapters = [
    {
        "title": "Chương 1: Kiến Nghị Sinh Viên",
        "content": """<p>Bốn trăm hai mươi sinh viên Khoa Kinh tế, Đại học Kinh tế Quốc dân, ký tên vào đơn kiến nghị gửi Ban Giám hiệu. Nội dung: "Chúng tôi yêu cầu cô Lý Minh Châu dạy thay PGS Trần Quốc Mạnh môn Kinh tế lượng, vì bài giảng của PGS Mạnh lạc hậu, đọc slide cũ mười năm, và không trả lời được câu hỏi của sinh viên."</p>

<p>Đơn kiến nghị — đánh máy, in giấy A4, bốn trang chữ ký — nằm trên bàn PGS Trần Quốc Mạnh lúc tám giờ sáng thứ Hai.</p>

<p>PGS Mạnh năm mươi tám tuổi, tóc muối tiêu, kính gọng vàng, Trưởng khoa Kinh tế mười lăm năm. Ông đọc đơn — từ trang đầu đến trang cuối — rồi đặt xuống, mặt đỏ tía.</p>

<p>"Bốn trăm hai mươi sinh viên muốn thay tao bằng con bé mới về ba năm?"</p>

<p>Con bé mới về ba năm: Lý Minh Châu, ba mươi tuổi, tiến sĩ Kinh tế lượng tốt nghiệp Đại học Toulouse (Pháp), về Việt Nam năm 2020, giảng viên cơ hữu Khoa Kinh tế. Ba năm giảng dạy — Châu trở thành giảng viên được yêu thích nhất Khoa. Lớp cô luôn hết chỗ, sinh viên xin chuyển sang lớp cô, và đánh giá giảng viên cuối kỳ của cô: 4.8/5.0 — cao nhất Khoa.</p>

<p>Đánh giá của PGS Mạnh: 2.3/5.0 — thấp nhất Khoa.</p>

<p>Mạnh không sai khi nói ông có kinh nghiệm — ông dạy ba mươi năm, viết bốn giáo trình, hướng dẫn hai mươi nghiên cứu sinh. Nhưng giáo trình của ông viết năm 2005, dùng số liệu năm 2003, và chưa cập nhật phương pháp mới nào kể từ khi machine learning thay đổi hoàn toàn ngành kinh tế lượng.</p>

<p>Châu dạy khác: cô dùng Python để minh họa mô hình hồi quy, cho sinh viên làm bài tập với dữ liệu thực từ World Bank, và kết hợp case study doanh nghiệp Việt Nam — VinFast, FPT, Vietjet — vào bài giảng. Sinh viên nói: "Cô Châu dạy xong, em biết ngay về làm được gì. Thầy Mạnh dạy xong, em chỉ biết đọc slide."</p>

<hr>

<p>Mười giờ sáng, PGS Mạnh gọi Châu lên phòng Trưởng khoa.</p>

<p>"Châu, em biết đơn kiến nghị này không?"</p>

<p>"Dạ em không biết. Em không tổ chức sinh viên ký đơn."</p>

<p>"Nhưng sinh viên ký vì em."</p>

<p>"Thưa thầy, sinh viên ký vì họ muốn học tốt hơn. Đó là quyền của họ."</p>

<p>"Em đang nói tôi dạy không tốt?"</p>

<p>"Em không nói. Bốn trăm hai mươi sinh viên nói."</p>

<p>Mạnh đập bàn. "Châu! Em về đây ba năm, chưa có gì trong tay — chưa PGS, chưa GS, chưa đề tài cấp nhà nước — mà dám coi thường tôi? Tôi là Trưởng khoa, tôi quyết ai dạy môn nào."</p>

<p>"Dạ, em hiểu. Em chỉ muốn dạy tốt."</p>

<p>"Em muốn dạy tốt thì em dạy ở nơi khác."</p>

<p>Một tuần sau, Châu nhận thông báo: bị chuyển sang dạy môn Thống kê Cơ bản cho sinh viên năm nhất — môn nhàm chán nhất khoa, lớp ít sinh viên nhất, và quan trọng: không liên quan gì đến chuyên ngành của cô.</p>

<p>Hai tuần sau: Châu bị cắt hướng dẫn luận văn thạc sĩ — lý do: "Chưa đủ thâm niên."</p>

<p>Ba tuần sau: Châu bị cắt phụ cấp nghiên cứu — lý do: "Không có đề tài đang triển khai."</p>

<p>PGS Mạnh không sa thải Châu — ông không cần. Ông chỉ cần biến cô thành giảng viên vô hình.</p>"""
    },
    {
        "title": "Chương 2: Học Viện Online — Bắt Đầu Từ Phòng Ngủ",
        "content": """<p>Châu nộp đơn xin nghỉ việc — không phải vì thua, mà vì không muốn chiến đấu một trận mà kẻ nắm luật là đối thủ.</p>

<p>Phòng ngủ căn hộ thuê ở Cầu Giấy — hai mươi mét vuông, bàn làm việc, laptop Dell cũ, micro Blue Yeti (mua trả góp), webcam Logitech C920. Châu dọn góc phòng: kê bảng trắng sau lưng, dán background tối giản, lắp đèn ring light.</p>

<p>"MinhChâu Academy" — cô đăng ký kênh YouTube, TikTok, và website (minhchauacademy.vn). Khẩu hiệu: "Học kinh tế như chơi game — có level, có reward, có boss."</p>

<p>Video đầu tiên: "Kinh tế lượng cho người mới bắt đầu — Bài 1: Hồi quy tuyến tính, giải thích bằng ví dụ quán phở." Mười bốn phút, Châu dùng dữ liệu thực: giá phở ở ba mươi quán Hà Nội, phân tích yếu tố ảnh hưởng giá (vị trí, diện tích, số bàn, giờ mở cửa) bằng hồi quy tuyến tính trên Python.</p>

<p>Sinh viên comment: "Ước gì trường em có cô giảng như vậy." "Em học cả kỳ Kinh tế lượng không hiểu — xem video này mười bốn phút hiểu hết."</p>

<p>Tuần đầu: năm nghìn lượt xem. Tuần hai: hai mươi nghìn. Tháng đầu: một trăm nghìn subscriber YouTube.</p>

<p>Châu đăng ba video mỗi tuần — mỗi video chuẩn bị hai ngày: một ngày viết bài giảng, soạn code Python, chuẩn bị dữ liệu thực; một ngày quay, cắt, dựng. Cô tự làm tất cả — vì không có tiền thuê ai.</p>

<p>Thu nhập tháng đầu: không đồng. YouTube trả tiền quảng cáo từ tháng thứ ba: hai triệu đồng. Ít hơn lương giảng viên — nhưng Châu không dạy vì tiền. Cô dạy vì bốn trăm hai mươi sinh viên đã ký tên vào đơn kiến nghị mà không ai nghe.</p>

<p>"Nếu trường không nghe, thì internet sẽ nghe," Châu viết trong nhật ký. "Và internet không cần ai duyệt bài."</p>"""
    },
    {
        "title": "Chương 3: PGS Mạnh Phản Công",
        "content": """<p>PGS Mạnh biết MinhChâu Academy khi sinh viên năm ba mang laptop đến lớp, mở YouTube, và nói: "Thầy ơi, cô Châu giảng phần này khác thầy. Cách nào đúng?"</p>

<p>Mạnh nhìn màn hình laptop — mặt Châu trên video, bảng trắng sau lưng, code Python trên màn hình — và hiểu rằng cô không biến mất. Cô đã rời trường, nhưng cô vẫn ở đây — trong laptop của mỗi sinh viên.</p>

<p>Mạnh phản công.</p>

<p>Thứ nhất: ông gửi email toàn khoa, cấm sinh viên sử dụng "tài liệu giảng dạy không chính thống" trong lớp — ám chỉ video MinhChâu Academy. Lý do: "Để đảm bảo tính thống nhất của chương trình đào tạo."</p>

<p>Sinh viên phản ứng: "Thầy cấm YouTube? Thầy cấm cả Google luôn đi."</p>

<p>Thứ hai: Mạnh liên hệ Hội đồng Khoa học Khoa, đề nghị rà soát nội dung MinhChâu Academy — xem có "sử dụng trái phép tài liệu của Khoa" hay không. Kết quả: không có — Châu dùng dữ liệu công khai từ World Bank, tự viết code, tự soạn bài giảng.</p>

<p>Thứ ba: Mạnh gọi điện cho Châu.</p>

<p>"Châu, em dạy online thu hút sinh viên của trường — sinh viên bỏ lớp tôi để xem em. Em có biết đó là phá hoại?"</p>

<p>"Thầy, sinh viên không bỏ lớp thầy vì em. Sinh viên bỏ lớp thầy vì bài giảng của thầy không còn phù hợp. Em chỉ cung cấp lựa chọn — sinh viên tự quyết định."</p>

<p>"Em muốn nói tôi dạy dở?"</p>

<p>"Em muốn nói: cập nhật bài giảng, thầy. Thế giới đã khác. Machine learning, big data, causal inference — tất cả đã thay đổi kinh tế lượng. Thầy dạy OLS regression bằng máy tính Casio trong khi thế giới dùng Python, R, và TensorFlow."</p>

<p>"Em đang dạy tôi à?"</p>

<p>"Không, thầy. Em đang nói sự thật — thứ mà bốn trăm hai mươi sinh viên đã nói trong đơn kiến nghị, và thầy không nghe."</p>

<p>Mạnh cúp máy.</p>"""
    },
    {
        "title": "Chương 4: Phát Hiện Gian Lận Nghiên Cứu",
        "content": """<p>Ba tháng sau khi mở MinhChâu Academy, Châu nhận email từ một nghiên cứu sinh — Nguyễn Hải Đăng, NCS năm hai tại Khoa Kinh tế, do PGS Mạnh hướng dẫn.</p>

<p>"Chị Châu, em cần nói chuyện. Không qua điện thoại — gặp trực tiếp."</p>

<p>Châu gặp Đăng ở quán cà phê ngoài khuôn viên trường. Đăng hai mươi bảy tuổi, mắt quầng thâm, tay run — như người không ngủ nhiều ngày.</p>

<p>"Chị ơi, thầy Mạnh ép em."</p>

<p>"Ép gì?"</p>

<p>"Thầy yêu cầu em đặt tên thầy là tác giả chính (first author) trên bài báo quốc tế của em — dù thầy không viết, không phân tích dữ liệu, thậm chí không đọc bản thảo. Thầy nói: 'Thầy là người hướng dẫn, tên thầy phải đứng đầu. Nếu em không đồng ý, thầy không ký xác nhận luận án.'"</p>

<p>"Đăng, em có bằng chứng?"</p>

<p>"Em có email thầy gửi yêu cầu. Và em có version history trên Google Docs — cho thấy thầy chưa bao giờ mở file bài báo."</p>

<p>Châu im lặng. Cô biết thực trạng này phổ biến trong học thuật Việt Nam — giáo sư đứng tên bài báo của nghiên cứu sinh là "luật bất thành văn." Nhưng phổ biến không có nghĩa là đúng.</p>

<p>"Đăng, em muốn chị làm gì?"</p>

<p>"Em muốn chị công bố. Nhưng em sợ — nếu thầy biết, thầy hủy luận án em. Bốn năm của em sẽ mất."</p>

<p>"Em yên tâm. Chị sẽ không nêu tên em. Chị sẽ điều tra hệ thống — không chỉ thầy Mạnh, mà toàn bộ vấn đề ghost authorship trong học thuật Việt Nam. Bài của em sẽ là một trong nhiều case study — không ai biết đó là em."</p>

<p>Châu dành hai tháng điều tra — liên hệ mười lăm nghiên cứu sinh từ năm khoa khác nhau ở ba trường đại học. Mười một người xác nhận: giáo sư hướng dẫn yêu cầu đứng tên tác giả chính dù không đóng góp.</p>

<p>Châu viết bài: "Ghost Authorship in Vietnamese Academia — A System of Stolen Credit." Đăng trên MinhChâu Academy và gửi cho ba tạp chí khoa học quốc tế về đạo đức nghiên cứu (research ethics).</p>

<p>Bài viết nổ tung.</p>"""
    },
    {
        "title": "Chương 5: Mẹ Và Chiếc Bảng Phấn",
        "content": """<p>Châu đi dạy vì mẹ.</p>

<p>Bà Lý Thị Tuyết — giáo viên Toán trường THPT Lê Quý Đôn, Hải Phòng — dạy học ba mươi lăm năm, lương bốn triệu rưỡi, lớp năm mươi học sinh, bảng phấn trắng xóa.</p>

<p>Mỗi tối, bà Tuyết ngồi chấm bài — năm mươi bài kiểm tra, viết nhận xét từng em bằng bút bi đỏ, cẩn thận như thể mỗi bài kiểm tra là một lá thư.</p>

<p>"Mẹ ơi, sao mẹ viết nhận xét dài vậy? Có ai đọc đâu."</p>

<p>"Con ơi, có đọc. Mẹ biết vì hai mươi năm trước, mẹ cũng đọc nhận xét của cô giáo mẹ."</p>

<p>Châu lớn lên nhìn mẹ dạy — nhìn mẹ chuẩn bị bài lúc năm giờ sáng, nhìn mẹ chạy xe đạp đi dạy dưới mưa, nhìn mẹ khóc khi học trò đỗ đại học, nhìn mẹ buồn khi học trò bỏ học vì nghèo. Mẹ dạy cô rằng: giáo dục là thứ duy nhất không ai lấy đi được — tiền mất, nhà mất, đất mất, nhưng kiến thức thì không.</p>

<p>"Mẹ ơi, con nghỉ việc rồi."</p>

<p>Châu gọi mẹ sau khi nộp đơn nghỉ. Bà Tuyết im lặng.</p>

<p>"Con bị đuổi à?"</p>

<p>"Không, mẹ. Con tự nghỉ."</p>

<p>"Sao?"</p>

<p>"Vì trường không cho con dạy đúng thứ con biết. Trưởng khoa coi con là mối đe dọa vì sinh viên thích con hơn ông ấy."</p>

<p>Im lặng.</p>

<p>"Con ơi, mẹ dạy ba mươi lăm năm. Mẹ biết cảm giác đó — khi người có quyền sợ người có tài. Nhưng con nghỉ thì con dạy ở đâu?"</p>

<p>"Con dạy online, mẹ."</p>

<p>"Online là sao?"</p>

<p>"Là con quay video bài giảng, đăng lên YouTube. Ai muốn học thì xem miễn phí."</p>

<p>"Miễn phí? Con sống bằng gì?"</p>

<p>"Con sống bằng niềm tin rằng dạy giỏi thì học trò sẽ đến — dù không có trường, không có lớp, không có bảng phấn."</p>

<p>Bà Tuyết cười — nụ cười buồn nhưng tự hào.</p>

<p>"Con giống mẹ. Mẹ cũng dạy vì yêu, không phải vì lương."</p>"""
    },
    {
        "title": "Chương 6: PGS Mạnh Bị Tước Học Hàm",
        "content": """<p>Bài viết về ghost authorship gây chấn động cộng đồng học thuật Việt Nam.</p>

<p>Bộ Giáo dục và Đào tạo thành lập tổ công tác rà soát — kiểm tra danh mục bài báo quốc tế của PGS Mạnh trong mười năm gần nhất. Kết quả: trong hai mươi ba bài báo quốc tế mà Mạnh đứng tên tác giả chính hoặc đồng tác giả, có mười bốn bài — ông không đóng góp nội dung đáng kể. Nghiên cứu sinh và giảng viên trẻ viết, phân tích, gửi bài — Mạnh chỉ đặt tên.</p>

<p>Hội đồng Chức danh Giáo sư Nhà nước rà soát hồ sơ phong PGS của Mạnh — trong đó, ba bài báo then chốt dùng để xét duyệt đều là bài "ghost authored."</p>

<p>Quyết định: tước danh hiệu Phó Giáo sư của Trần Quốc Mạnh, cách chức Trưởng khoa, và chuyển sang vị trí giảng viên thường.</p>

<p>Mạnh nhận quyết định trong phòng Trưởng khoa — cái phòng mà mười lăm năm ông ngồi, với bàn gỗ lim, ảnh chụp cùng Bộ trưởng, và tấm bằng PGS đóng khung treo tường.</p>

<p>Ông phải dỡ tấm bằng xuống. Ông phải dọn bàn. Ông phải rời phòng.</p>

<p>Và khi ông bước ra hành lang, sinh viên đứng hai bên — không ai nói gì, không ai cười, không ai hả hê. Chỉ im lặng. Vì sinh viên không ghét thầy — họ chỉ thất vọng. Thất vọng vì người dạy họ về "chính trực" trong học thuật lại là người thiếu chính trực nhất.</p>

<p>Nghiên cứu sinh Đăng — người đã khai báo — tốt nghiệp tiến sĩ sáu tháng sau, với luận án được Hội đồng đánh giá xuất sắc. Bài báo quốc tế của Đăng — bài mà Mạnh muốn đứng tên — được tạp chí Journal of Econometrics chấp nhận, với tên tác giả duy nhất: Nguyễn Hải Đăng.</p>

<p>Đăng gửi tin nhắn cho Châu: "Chị ơi, bài em được đăng rồi. Tên em. Chỉ tên em."</p>

<p>Châu reply: "Đúng rồi. Đó mới là công bằng."</p>"""
    },
    {
        "title": "Chương 7: Hai Triệu Sinh Viên",
        "content": """<p>Một năm sau khi mở MinhChâu Academy.</p>

<p>YouTube: năm trăm video, một triệu rưỡi subscriber. TikTok: ba trăm clip ngắn, tám trăm nghìn follower. Website: hai mươi nghìn học viên đăng ký khóa học có chứng chỉ.</p>

<p>Tổng cộng: hai triệu sinh viên từ Việt Nam, Lào, Campuchia, và cộng đồng người Việt ở Mỹ, Pháp, Úc.</p>

<p>Châu được TEDx Hanoi mời nói chuyện — bài nói: "Tại sao tôi bị đuổi khỏi trường đại học, và tại sao đó là điều tốt nhất xảy ra với giáo dục Việt Nam."</p>

<p>Cô đứng trên sân khấu TEDx, mặc áo dài xanh, tay không cầm gì — không slide, không note.</p>

<p>"Tôi bị đuổi khỏi trường vì sinh viên thích tôi hơn Trưởng khoa. Trong bất kỳ hệ thống lành mạnh nào, đó là lời khen. Nhưng trong hệ thống mà quyền lực sợ năng lực, đó là bản án."</p>

<p>"Tôi mở học viện online vì một lý do đơn giản: giáo dục không phải đặc quyền của ai có ghế giáo sư hay phòng trưởng khoa. Giáo dục là quyền — và internet là lớp học lớn nhất thế giới, không có tường, không có cửa, và không có trưởng khoa nào kiểm soát."</p>

<p>"Hai triệu sinh viên xem video của tôi — không phải vì tôi giỏi. Mà vì họ khát. Khát kiến thức thực tế, khát bài giảng cập nhật, khát giảng viên nói chuyện với họ thay vì đọc slide cho họ."</p>

<p>"Nếu hai triệu người khát mà hệ thống giáo dục không cho uống, thì vấn đề không phải hai triệu người — vấn đề là hệ thống."</p>

<p>Vỗ tay. Đứng dậy.</p>

<p>Video TEDx: sáu triệu lượt xem trên YouTube. Bộ Giáo dục mời Châu tham gia Hội đồng Tư vấn Đổi mới Giáo dục — cố vấn xây dựng nền tảng học liệu mở cho đại học.</p>"""
    },
    {
        "title": "Chương 8: Quay Về Trường — Nhưng Khác",
        "content": """<p>Đại học Kinh tế Quốc dân mời Châu trở lại — vị trí Phó Trưởng khoa Kinh tế, phụ trách Đổi mới Giảng dạy. Trưởng khoa mới — PGS Nguyễn Thị Hoa, bốn mươi lăm tuổi, tiến sĩ Stanford — là người đề cử.</p>

<p>"Chị Châu, Khoa cần chị. Sinh viên cần chị."</p>

<p>Châu suy nghĩ ba ngày. Rồi gọi mẹ.</p>

<p>"Mẹ ơi, trường mời con về."</p>

<p>"Con có muốn về không?"</p>

<p>"Con muốn — nhưng con có điều kiện."</p>

<p>"Điều kiện gì?"</p>

<p>"MinhChâu Academy vẫn chạy. Con dạy trường và dạy online song song. Và sinh viên được quyền chọn giảng viên — không ai bị ép học lớp nào."</p>

<p>"Nghe hợp lý. Con về đi."</p>

<p>Châu về trường — nhưng không ngồi phòng trưởng khoa. Cô ngồi trong giảng đường, cạnh sinh viên, mở laptop, bật projector.</p>

<p>"Chào các em. Cô Châu đây. Cô trở lại. Và hôm nay, chúng ta học Kinh tế lượng — bằng Python, bằng dữ liệu thực, và bằng quán phở."</p>

<p>Sinh viên cười. Vỗ tay. Giảng đường kín chỗ — hai trăm sinh viên, ghế không đủ, có em ngồi bậc cầu thang.</p>

<p>Trên bàn giảng viên: laptop Dell cũ, micro Blue Yeti, và webcam Logitech C920 — những thứ Châu dùng trong phòng ngủ khi mở MinhChâu Academy. Cô mang chúng đến trường — vì bài giảng hôm nay sẽ đồng thời livestream trên YouTube cho hai triệu sinh viên ngoài kia.</p>

<p>"Giáo dục không có tường," Châu nói trước khi bắt đầu bài giảng. "Lớp học này mở cho tất cả — ai có internet, ai muốn học, đều được vào. Không cần đơn xin, không cần điểm đầu vào, không cần ai cho phép."</p>

<p>"Vì kiến thức là quyền. Và quyền thì không ai được phép tước."</p>

<p>Bà Tuyết — mẹ Châu — ngồi ở nhà Hải Phòng, mở YouTube trên iPad cũ, xem con gái giảng bài. Bà mỉm cười — nụ cười của người giáo viên ba mươi lăm năm nhìn thấy đứa con gái tiếp tục thứ mà bà bắt đầu: dạy học, không phải vì lương, mà vì yêu.</p>

<p>Trên bảng trắng sau lưng Châu, cô viết một dòng — bằng bút dạ xanh, chữ to:</p>

<p>"Dạy giỏi không phải tội. Học giỏi không phải đặc quyền."</p>"""
    }
]

story_data["chapters"] = chapters

with open("scratch/story_5558_rewrite.json", "w", encoding="utf-8") as f:
    json.dump(story_data, f, ensure_ascii=False, indent=2)

print("✅ Truyện 5558 viết xong — 8 CHƯƠNG!")
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
    if ws.cell(row=r, column=2).value and str(ws.cell(row=r, column=2).value).strip() == "5558":
        ws.cell(row=r, column=6).value = 8
        ws.cell(row=r, column=12).value = "Giảng viên ĐH KTQD bị ép nghỉ vì dạy giỏi hơn Trưởng khoa. Mở học viện online từ phòng ngủ, 2 triệu sinh viên. Phát hiện PGS Mạnh gian lận ghost authorship, Mạnh bị tước học hàm."
        ws.cell(row=r, column=13).value = "REWRITE TOÀN BỘ: 9 chương quá ngắn → 8 CHƯƠNG ĐẦY ĐẶN"
        ws.cell(row=r, column=14).value = "☑️ Đã sửa"
        print(f"  ✅ Excel updated row {r}")
        break
wb.save("danh_sach_truyen_doctieuthuyet.xlsx")
print("\n✅ HOÀN THÀNH TRUYỆN 5558!")
