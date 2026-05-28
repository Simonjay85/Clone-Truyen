import json, urllib.request, openpyxl

story_data = {
    "secret_token": "ZEN_TRUYEN_2026_BYPASS",
    "story_id": 5592,
    "title": "Bị Vu Oan Đắm Tàu, Tôi Tự Trục Vớt Bằng Chứng Dưới Đáy Biển Khiến Kẻ Thủ Ác Phải Lĩnh Án",
    "intro": "<p>Hai giờ sáng, giữa biển Đông, tàu hàng Hải Phong Star chở ba nghìn tấn gạo xuất khẩu bỗng đắm — không ai chết, nhưng cả con tàu và hàng hóa chìm xuống đáy biển.</p>\n<p>Phạm Quốc Tuấn — thuyền trưởng trẻ nhất đội tàu Việt Hải — bị đổ lỗi: \"Điều khiển tàu vào vùng nước nông khi say rượu.\" Bằng thuyền trưởng bị tước, danh dự bị vấy bẩn, và anh đứng trước nguy cơ ngồi tù.</p>\n<p>Nhưng Tuấn biết sự thật: tàu không đắm vì anh. Tàu đắm vì vỏ tàu đã mục nát — do Giám đốc Nguyễn Hải Đăng cắt giảm bảo trì suốt hai năm để ăn tiền. Và bằng chứng nằm dưới đáy biển — ở xác tàu, sâu ba mươi mét.</p>",
    "author": "Phạm Quốc Tuấn",
    "chapters": []
}

chapters = [
    {
        "title": "Chương 1: Đêm Tàu Đắm",
        "content": """<p>Hai giờ sáng, giữa biển Đông, cách bờ biển Quảng Ngãi sáu mươi hải lý.</p>

<p>Phạm Quốc Tuấn đứng trên đài chỉ huy tàu hàng Hải Phong Star — tàu chở hàng rời, trọng tải bốn nghìn tấn, đang chở ba nghìn tấn gạo xuất khẩu sang Philippines. Biển lặng, gió cấp ba, trời đầy sao — điều kiện hoàn hảo cho hải trình.</p>

<p>Tuấn ba mươi hai tuổi, thuyền trưởng trẻ nhất đội tàu Việt Hải, mười năm kinh nghiệm đi biển, chưa một lần gây sự cố. Anh đang uống cà phê đen — loại cà phê Robusta Đắk Lắk mà anh pha bằng phin nhỏ mang theo mỗi chuyến — khi tiếng kim loại rung lắc dưới thân tàu bắt đầu.</p>

<p>Không phải sóng. Sóng rung theo nhịp — còn tiếng này không có nhịp, nó liên tục, như thể thân tàu đang bị xé từ bên trong.</p>

<p>"Máy trưởng! Kiểm tra khoang máy ngay!" Tuấn gọi qua intercom.</p>

<p>Mười lăm giây im lặng. Rồi giọng máy trưởng Nguyễn Văn Phú — bốn mươi lăm tuổi, hai mươi năm đi biển — vang lên, hổn hển:</p>

<p>"Anh Tuấn! Nước tràn vào khoang số 3! Vỏ tàu nứt — nứt dọc, dài khoảng hai mét, phía mạn phải dưới mớn nước!"</p>

<p>Tim Tuấn đập mạnh. Vỏ tàu nứt dọc — không phải va chạm (va chạm gây nứt ngang), mà là nứt do mỏi kim loại. Tức là thép vỏ tàu đã yếu từ trước — bảo trì không đúng quy trình.</p>

<p>"Bật hết bơm hút nước! Gọi toàn thể thủy thủ đoàn — mặc áo phao, chuẩn bị xuồng cứu sinh!"</p>

<p>Tuấn bấm nút báo động — còi tàu rú lên giữa đêm biển. Mười bảy thủy thủ từ các khoang chạy lên boong, mắt còn ngái ngủ, chân loạng choạng trên sàn tàu đã bắt đầu nghiêng.</p>

<p>Bơm hút nước chạy hết công suất — nhưng nước tràn nhanh hơn bơm. Khoang số 3 ngập trong mười lăm phút, khoang số 4 bắt đầu tràn. Tàu nghiêng mười lăm độ sang phải.</p>

<p>Tuấn có hai lựa chọn: cố cứu tàu và chìm cùng hàng hóa, hoặc bỏ tàu và cứu mười tám mạng người.</p>

<p>"Abandon ship! Tất cả lên xuồng cứu sinh!"</p>

<p>Anh là người cuối cùng rời tàu — theo đúng luật biển và danh dự thuyền trưởng. Anh đứng trên boong, nhìn mũi tàu Hải Phong Star từ từ chìm xuống — nước đen sôi sục quanh thân tàu, ba nghìn tấn gạo hút nước phồng lên rồi kéo cả con tàu xuống đáy.</p>

<p>Bốn phút. Từ lúc vỏ tàu nứt đến lúc tàu chìm hoàn toàn: bốn phút.</p>

<p>Tuấn nhảy xuống biển, bơi đến xuồng cứu sinh. Mười tám người — an toàn. Không ai chết.</p>

<p>Nhưng khi tàu cứu hộ đến lúc bốn giờ sáng, Tuấn biết: từ giây phút này, cuộc đời anh sẽ thay đổi — và không phải theo chiều tốt.</p>"""
    },
    {
        "title": "Chương 2: Bằng Thuyền Trưởng Bị Tước",
        "content": """<p>Cục Hàng hải Việt Nam mở cuộc điều tra sơ bộ trong bảy ngày.</p>

<p>Tuấn bị triệu tập đến Cục — trụ sở ở Hải Phòng, tòa nhà cũ kỹ, phòng họp tầng ba, bàn dài, đèn huỳnh quang. Năm người ngồi đối diện anh: ba cán bộ Cục, một đại diện hãng bảo hiểm P&I, và — Nguyễn Hải Đăng, Giám đốc công ty Việt Hải, chủ tàu Hải Phong Star.</p>

<p>Đăng bốn mươi bảy tuổi, vest xanh đen, tóc vuốt gel, nụ cười lịch sự — loại cười mà Tuấn đã thấy hàng chục lần trong các cuộc họp nội bộ. Nụ cười của người luôn đúng, luôn sạch, luôn có luật sư đứng sau.</p>

<p>Đăng trình bày: "Thuyền trưởng Phạm Quốc Tuấn điều khiển tàu vào vùng nước nông khi không tỉnh táo. Theo báo cáo của sĩ quan trực ca, Tuấn có sử dụng rượu trước khi vào ca."</p>

<p>"Tôi không uống rượu," Tuấn nói ngay. "Tôi uống cà phê đen. Và tàu đắm không phải vì vùng nước nông — tàu đắm vì vỏ tàu nứt do mỏi kim loại. Tôi nghe tiếng rung trước khi máy trưởng báo nước tràn."</p>

<p>"Anh Tuấn, anh có bằng chứng?"</p>

<p>"Bằng chứng nằm dưới đáy biển — ở xác tàu. Nếu Cục cho trục vớt và kiểm tra vỏ tàu, sẽ thấy vết nứt do mỏi, không phải va chạm."</p>

<p>Đăng cười nhẹ: "Xác tàu nằm ở độ sâu ba mươi mét. Chi phí trục vớt: hai mươi tỷ đồng. Ai trả?"</p>

<p>Im lặng. Không ai trả lời.</p>

<p>Cục Hàng hải đình chỉ bằng thuyền trưởng của Tuấn "chờ điều tra." Không bằng, Tuấn không được lên bất kỳ con tàu nào — đồng nghĩa mất việc, mất thu nhập, mất danh dự.</p>

<p>Đăng rời phòng, bắt tay cán bộ Cục, không nhìn Tuấn.</p>

<p>Tuấn đứng một mình trong hành lang, tay cầm tờ quyết định đình chỉ, nhìn ra cửa sổ — cảng Hải Phòng bên ngoài, tàu lớn tàu nhỏ vào ra, còi tàu hụ. Anh đã sống trên biển mười năm — và bây giờ, biển cấm cửa anh.</p>

<p>Anh lấy điện thoại, gọi cho người duy nhất có thể giúp: luật sư hàng hải Trần Văn Minh — bạn học cấp ba, giờ là luật sư chuyên tranh chấp hàng hải ở TP.HCM.</p>

<p>"Minh ơi, tao cần mày."</p>

<p>"Sao, Tuấn?"</p>

<p>"Tao bị vu oan đắm tàu. Bằng chứng nằm dưới đáy biển. Tao cần lặn xuống lấy."</p>

<p>"Mày điên à?"</p>

<p>"Tao tỉnh hơn bao giờ hết."</p>"""
    },
    {
        "title": "Chương 3: Bố Và Biển",
        "content": """<p>Tuấn đi biển vì bố.</p>

<p>Ông Phạm Văn Hải — ngư dân Quảng Ngãi, xã Bình Châu — mất trên biển khi Tuấn mười hai tuổi. Bão số 9 năm 2006, sóng cao sáu mét, gió cấp mười hai. Thuyền đánh cá bảy mét của ông — chiếc thuyền gỗ đóng bằng tay, động cơ Yanmar cũ — không chịu nổi.</p>

<p>Mười hai ngư dân trên thuyền. Sáu người được tàu cứu hộ vớt. Sáu người mất — trong đó có ông Hải.</p>

<p>Tuấn ở nhà cùng mẹ — bà Nguyễn Thị Lý, bán cá ở chợ Bình Châu — nghe tin bão qua radio. Khi danh sách mất tích được đọc, tên bố Tuấn ở vị trí thứ ba.</p>

<p>Mẹ Tuấn khóc ba ngày. Tuấn không khóc — anh mười hai tuổi, nhưng anh đã quyết: anh sẽ đi biển, như bố. Nhưng anh sẽ đi bằng tàu lớn — tàu chịu được bão, tàu có radar, tàu có áo phao đủ cho mọi người. Anh sẽ không để ai chết trên biển như bố.</p>

<p>Mười sáu tuổi, Tuấn thi vào Đại học Hàng hải Hải Phòng — ngành Điều khiển tàu biển. Thi đậu thứ ba. Học bổng toàn phần — vì anh nghèo nhất lớp.</p>

<p>Bốn năm đại học, Tuấn vừa học vừa làm bốc vác ở cảng Hải Phòng, kiếm tiền gửi mẹ. Tốt nghiệp thủ khoa — anh là thuyền trưởng trẻ nhất Việt Nam khi được bổ nhiệm ở tuổi hai mươi sáu.</p>

<p>Sáu năm đi biển, chưa một sự cố. Mỗi chuyến ra khơi, anh mang theo ảnh bố — tấm ảnh 3x4 ép plastic, nhét trong ví. Và mỗi khi tàu qua vùng biển Quảng Ngãi, anh thả một bông hoa cúc xuống biển — cho bố, cho sáu người ngư dân không về.</p>

<p>Giờ đây, bằng thuyền trưởng bị tước, Tuấn mất luôn lý do tồn tại của mình. Anh không phải doanh nhân, không phải trí thức — anh là người đi biển. Lấy đi biển, anh chỉ còn là một gã đàn ông ba mươi hai tuổi ngồi trên bờ, nhìn tàu người khác ra khơi.</p>

<p>Đó là lý do anh quyết định lặn xuống đáy biển — không phải vì liều lĩnh, mà vì không còn gì để mất. Khi đã ở đáy rồi, hướng duy nhất là đi lên.</p>"""
    },
    {
        "title": "Chương 4: Lặn Xuống Đáy Biển",
        "content": """<p>Tuấn cần bằng chứng vật lý: đường nứt trên vỏ tàu chứng minh lỗi mỏi kim loại, không phải va chạm.</p>

<p>Anh thuê thuyền cá từ bác Năm — ngư dân Quảng Ngãi, bạn cũ của bố — ra vùng biển nơi Hải Phong Star chìm. Tọa độ anh nhớ chính xác: 15°48' Bắc, 108°42' Đông — anh là thuyền trưởng, tọa độ là bản năng.</p>

<p>Bộ lặn: Tuấn mua bình khí nén SCUBA đã qua sử dụng giá bốn triệu đồng, mặt nạ lặn, chân nhái, đèn pin chống nước. Camera hành trình GoPro Hero 9 mượn của Minh — luật sư nói: "Mày phải quay video liên tục, không cắt, vì tòa chỉ chấp nhận bằng chứng nguyên bản."</p>

<p>Bốn giờ sáng, thuyền cá ra khơi. Biển tháng Năm — lặng, trời trong, tầm nhìn dưới nước tốt.</p>

<p>Sáu giờ sáng: đến tọa độ. Tuấn mặc bộ lặn, kiểm tra bình khí, gắn GoPro lên đầu, bật record.</p>

<p>"Đây là Phạm Quốc Tuấn, cựu thuyền trưởng tàu Hải Phong Star. Hôm nay ngày hai mươi tháng Năm. Tôi đang tại tọa độ nơi tàu chìm. Tôi lặn xuống để thu thập bằng chứng."</p>

<p>Anh lộn người, lặn xuống.</p>

<p>Mười mét — nước chuyển từ xanh biếc sang xanh đậm. Ánh sáng mặt trời yếu dần.</p>

<p>Hai mươi mét — tối hơn. Tuấn bật đèn pin. Áp suất nước ép vào tai — anh cân bằng áp suất bằng cách bịt mũi thổi.</p>

<p>Ba mươi mét — đáy cát. Và ở đó, giữa lớp bùn cát, nằm nghiêng bốn mươi lăm độ: Hải Phong Star.</p>

<p>Con tàu trông khác dưới nước — nhỏ hơn, buồn hơn, phủ một lớp tảo xanh mỏng. Cá nhỏ bơi quanh ống khói gỉ sét. Mũi tàu cắm vào cát, đuôi tàu hếch lên, cánh quạt chân vịt nằm im lìm.</p>

<p>Tuấn bơi dọc mạn phải — phía nứt vỏ tàu. Đèn pin chiếu: vết nứt dọc dài hai mét rưỡi, rộng mười lăm centimet, mép nứt xù xì — đặc trưng của nứt do mỏi kim loại (fatigue crack), không phải nứt do va chạm (impact crack).</p>

<p>Anh quay cận cảnh mép nứt — GoPro ghi lại từng chi tiết: lớp sơn bong xung quanh, rỉ sét ăn sâu vào thép dọc mép nứt (chứng minh rỉ sét đã có từ trước khi tàu đắm), và các vết lõm nhỏ trên bề mặt thép — dấu hiệu của ăn mòn điện hóa (galvanic corrosion) do thiếu bảo trì anốt hy sinh.</p>

<p>"Vết nứt này không phải do va chạm," Tuấn nói vào GoPro, tiếng bong bóng khí sôi sục quanh miệng. "Đây là fatigue crack — nứt mỏi. Thép vỏ tàu đã bị ăn mòn ít nhất hai năm mà không được thay thế. Anốt hy sinh không còn — tức là không ai kiểm tra vỏ tàu dưới mớn nước trong hai năm gần nhất."</p>

<p>Anh quay tiếp: nhật ký hành hải trong phòng điều khiển — cuốn sổ bọc nhựa, vẫn còn trong ngăn kéo. Tuấn mở ngăn kéo, lấy ra, nhét vào túi lưới chống nước.</p>

<p>Thời gian dưới nước: bốn mươi phút. Bình khí còn đủ cho mười lăm phút. Tuấn từ từ lên — dừng ở mười lăm mét để giảm áp, tránh bệnh giảm áp.</p>

<p>Khi ngoi lên mặt nước, tay cầm cuốn nhật ký hành hải, anh thở gấp, mắt cay vì nước mặn.</p>

<p>Bác Năm kéo anh lên thuyền: "Mày tìm được gì không?"</p>

<p>"Tìm được rồi, bác. Tìm được sự thật."</p>"""
    },
    {
        "title": "Chương 5: Nhật Ký Bảo Trì Bị Làm Giả",
        "content": """<p>Tuấn mang video GoPro và nhật ký hành hải lên bờ, đến văn phòng luật sư Trần Văn Minh ở TP.HCM.</p>

<p>Minh xem video hai lần, dừng ở từng frame, chụp screenshot. Rồi mở nhật ký hành hải — cuốn sổ A4 bọc nhựa, mực đã nhòe nước nhưng vẫn đọc được.</p>

<p>"Tuấn, đây là nhật ký gốc — cuốn mà mày giữ trên tàu, ghi chép hàng ngày. Nhưng bản mà Đăng nộp cho Cục Hàng hải là bản photo — có sửa."</p>

<p>"Sửa chỗ nào?"</p>

<p>Minh so sánh. Nhật ký gốc, trang ngày mười bảy tháng Tư — hai tuần trước khi tàu đắm — Tuấn ghi: "Kiểm tra bơm hút nước khoang 3 — bơm số 2 hỏng, đã báo cáo Giám đốc Đăng yêu cầu sửa chữa. GĐ trả lời: 'Tàu còn chạy tốt, sửa sau.'"</p>

<p>Bản photo mà Đăng nộp: trang này bị cắt — không có dòng ghi chú về bơm hỏng, không có câu trả lời của Đăng. Thay vào đó là ghi chú mới: "Bơm hoạt động bình thường."</p>

<p>"Đăng đã sửa nhật ký," Minh nói. "Y cắt giảm bảo trì hai năm nay — không thay anốt hy sinh, không sửa bơm, không kiểm tra vỏ tàu dưới mớn nước. Tiền bảo trì — theo hợp đồng bảo hiểm P&I — là ba trăm triệu đồng mỗi năm. Đăng khai đã chi, nhưng thực tế không chi. Sáu trăm triệu trong hai năm — Đăng ăn hết."</p>

<p>"Tức là tàu đắm vì Đăng?"</p>

<p>"Đúng. Vỏ tàu mỏi vì không bảo trì, bơm hỏng không sửa, khi vỏ nứt thì nước tràn nhanh hơn khả năng bơm — tàu chìm trong bốn phút."</p>

<p>Tuấn nắm tay. Bốn phút — bốn phút đó suýt giết mười tám người. Và kẻ gây ra nó đang ngồi trong văn phòng điều hòa, mặc vest, cười tươi.</p>

<p>"Minh ơi, tao cần gì để đưa nó ra tòa?"</p>

<p>"Mày cần ba thứ: video GoPro gốc (đã có), nhật ký gốc so với bản photo bị sửa (đã có), và một thứ nữa — lời khai của thủy thủ đoàn."</p>"""
    },
    {
        "title": "Chương 6: Thủy Thủ Đoàn Đứng Lên",
        "content": """<p>Mười bảy thủy thủ — toàn bộ đoàn trừ Tuấn — sống rải rác từ Hải Phòng đến Bà Rịa Vũng Tàu.</p>

<p>Tuấn liên hệ từng người. Mười bảy cuộc gọi, mười bảy câu chuyện khác nhau — nhưng cùng một nỗi sợ.</p>

<p>Máy trưởng Nguyễn Văn Phú — người đầu tiên phát hiện nước tràn — nói: "Tuấn ơi, tao biết mày đúng. Nhưng Đăng dọa: ai khai bất lợi cho công ty sẽ bị kiện ngược tội vi phạm hợp đồng lao động."</p>

<p>Thủy thủ trưởng Lê Hữu Tân: "Anh Tuấn, em muốn khai thật. Nhưng em vừa có con — lương biển nuôi cả gia đình. Nếu bị đuổi, em biết làm gì?"</p>

<p>Thợ máy Hoàng Đình Nam: "Anh, em đã thay bơm cho khoang 3 ba lần trong hai năm — toàn bơm cũ tái sử dụng, không phải bơm mới. Em biết Đăng cắt ngân sách. Nhưng em không dám nói."</p>

<p>Tuấn hiểu. Họ không hèn — họ sợ. Sợ mất việc, sợ bị trả thù, sợ kiện tụng. Đăng có tiền, có luật sư, có quan hệ — còn họ chỉ là thủy thủ lương tám triệu mỗi tháng.</p>

<p>Tuấn bay vào TP.HCM, gặp luật sư Minh. Minh soạn một văn bản cam kết: nếu thủy thủ đoàn đồng ý khai báo, luật sư sẽ bảo vệ họ miễn phí, và mọi lời khai sẽ được bảo mật cho đến khi tòa xét xử.</p>

<p>Tuấn mang văn bản đi gặp từng người — tận nhà, uống trà, nói chuyện.</p>

<p>Với máy trưởng Phú ở Hải Phòng, Tuấn mang theo chai rượu Bàu Đá — loại rượu hai anh em hay uống sau mỗi chuyến tàu.</p>

<p>"Anh Phú, anh nhớ đêm tàu đắm không? Bốn phút — mười tám mạng người. Lần tới, có thể không ai kịp lên xuồng. Đăng sẽ tiếp tục cắt bảo trì — vì y biết không ai dám nói."</p>

<p>Phú uống rượu, im lặng rất lâu.</p>

<p>"Mày đúng, Tuấn. Nếu tao không khai, lần tới có thể là tao chết."</p>

<p>Phú ký.</p>

<p>Tuấn đi tiếp — Hải Phòng, Quảng Ninh, Đà Nẵng, Vũng Tàu. Mười bốn ngày, mười bảy cuộc gặp. Cuối cùng: mười bảy chữ ký — toàn bộ thủy thủ đoàn đồng ý khai báo.</p>

<p>Mỗi người khai cùng một thứ: bơm hút nước khoang 3 đã hỏng nhiều lần, báo cáo lên Giám đốc Đăng nhưng không được sửa chữa; vỏ tàu dưới mớn nước không được kiểm tra định kỳ; thiết bị an toàn (phao cứu sinh, bè tự bung) hết hạn sử dụng nhưng không được thay.</p>

<p>Mười bảy người. Mười bảy lời khai. Một sự thật.</p>"""
    },
    {
        "title": "Chương 7: Đăng Phản Công",
        "content": """<p>Khi luật sư Minh nộp đơn kiện lên Tòa án Nhân dân TP. Hải Phòng, Đăng phản ứng nhanh hơn Tuấn tưởng.</p>

<p>Tuần đầu: Đăng thuê công ty PR đăng bài trên ba trang tin điện tử — nội dung: "Thuyền trưởng Phạm Quốc Tuấn say rượu khi điều khiển tàu, gây thiệt hại ba nghìn tấn gạo và con tàu bốn trăm tỷ đồng. Nay quay sang vu khống giám đốc để trốn tội."</p>

<p>Tuần hai: Đăng gửi thư đe dọa đến mười bảy thủy thủ — thư luật sư, cảnh báo kiện ngược tội "khai man trong tố tụng" nếu họ không rút lời khai.</p>

<p>Ba thủy thủ hoảng — gọi Tuấn lúc nửa đêm.</p>

<p>"Anh Tuấn, Đăng gửi thư luật sư cho em. Em sợ lắm."</p>

<p>"Em bình tĩnh. Thư đó là dọa — Đăng không có cơ sở kiện em. Lời khai của em được bảo vệ bởi luật tố tụng."</p>

<p>Tuần ba: Đăng tìm cách mua chuộc. Sĩ quan trực ca — Lê Hoàng Dũng, người mà Đăng từng viện dẫn nói Tuấn "uống rượu" — gọi Tuấn:</p>

<p>"Anh Tuấn, em xin lỗi. Đăng ép em khai dối — y nói nếu em không khai Tuấn say rượu, y sẽ đuổi em và không trả lương ba tháng còn nợ. Em sợ quá nên khai theo lệnh y. Giờ em muốn khai lại."</p>

<p>"Dũng, em khai lại có nguy hiểm không?"</p>

<p>"Em không biết. Nhưng anh Tuấn ơi, em không ngủ được ba tháng rồi. Mỗi đêm em nằm nghĩ: nếu mười tám người chết đêm đó, em có khai dối được không? Không. Em khai dối không nổi."</p>

<p>Dũng ký đơn rút lời khai cũ, khai lại sự thật: "Tôi không hề thấy thuyền trưởng Tuấn uống rượu. Giám đốc Đăng ép tôi khai dối bằng cách đe dọa sa thải và nợ lương."</p>

<p>Luật sư Minh bổ sung lời khai Dũng vào hồ sơ — đây là viên đạn cuối cùng. Bây giờ Đăng không chỉ bị tố cắt giảm bảo trì, mà còn bị tố ép nhân viên khai man.</p>

<p>Đăng biết mình đang thua. Y thuê thêm luật sư — nhưng bằng chứng quá rõ: video GoPro gốc, nhật ký bị làm giả, mười bảy lời khai thủy thủ đoàn, và lời khai lật ngược của sĩ quan trực ca.</p>

<p>Không có luật sư nào cứu được một vụ kiện mà bằng chứng nằm dưới đáy biển — và bị cáo đã quên rằng đáy biển không biết nói dối.</p>"""
    },
    {
        "title": "Chương 8: Phiên Tòa",
        "content": """<p>Tòa án Nhân dân TP. Hải Phòng, phòng xử án số 2.</p>

<p>Tuấn ngồi phía nguyên đơn, mặc áo sơ mi trắng, quần tây đen — bộ quần áo mà anh chỉ mặc khi dự lễ. Bên cạnh là luật sư Minh. Phía sau: máy trưởng Phú, sĩ quan Dũng, và năm thủy thủ đại diện — họ đến làm nhân chứng.</p>

<p>Đăng ngồi phía bị cáo, hai luật sư bên cạnh, mặt bình thản — nhưng tay phải liên tục mở nắp chai nước, uống, đóng, mở, uống — thói quen của người đang cố giấu lo lắng.</p>

<p>Viện Kiểm sát trình bày cáo trạng: Nguyễn Hải Đăng bị truy tố hai tội danh — "Vi phạm quy định về an toàn giao thông đường thủy nội địa" (Điều 272 BLHS) và "Làm giả tài liệu của cơ quan, tổ chức" (Điều 341 BLHS).</p>

<p>Luật sư Minh đứng lên, trình bày bằng chứng — chiếu video GoPro lên màn hình lớn.</p>

<p>"Kính thưa Hội đồng xét xử. Đây là video ghi hình trực tiếp tại xác tàu Hải Phong Star, độ sâu ba mươi mét. Video không cắt ghép, có metadata gốc xác nhận ngày tháng và tọa độ GPS."</p>

<p>Màn hình chiếu: vết nứt dọc trên vỏ tàu, rỉ sét ăn sâu, anốt hy sinh không còn. Tuấn ngồi im, nhìn con tàu của mình trên màn hình — con tàu mà anh đã chỉ huy ba năm, biết từng đường ống, từng van, từng tiếng máy.</p>

<p>"Tiếp theo: nhật ký hành hải gốc," Minh nói, đặt cuốn sổ bọc nhựa lên bàn thẩm phán. "Và đây là bản photo mà bị cáo Đăng nộp cho Cục Hàng hải."</p>

<p>Hai bản đặt cạnh nhau: một bản có ghi chú "bơm hỏng, GĐ nói sửa sau" — bản kia không có. Thẩm phán đối chiếu, lật từng trang, soi từng dòng.</p>

<p>Đăng bắt đầu mất bình tĩnh. Y đứng dậy: "Tôi phản đối! Nhật ký đó có thể bị sửa đổi bởi nguyên đơn!"</p>

<p>Luật sư Minh cười nhẹ: "Kính thưa, nhật ký gốc đã được giám định pháp y tài liệu — mực bút bi, độ nhòe nước, dấu ấn thời gian — tất cả khớp với ngày ghi chép. Trong khi bản photo của bị cáo có dấu hiệu chỉnh sửa Photoshop ở trang hai mươi ba và hai mươi tám."</p>

<p>Đăng ngồi xuống.</p>

<p>Sĩ quan Dũng được gọi lên bục nhân chứng. Tay run, giọng nhỏ — nhưng rõ ràng.</p>

<p>"Tôi khai lại: thuyền trưởng Phạm Quốc Tuấn không uống rượu đêm hôm đó. Tôi uống cà phê cùng anh ấy. Giám đốc Đăng ép tôi khai dối bằng cách đe dọa sa thải và nợ ba tháng lương."</p>

<p>Phòng xử án im lặng.</p>"""
    },
    {
        "title": "Chương 9: Đăng Lĩnh Án",
        "content": """<p>Tòa tuyên án sau hai ngày xét xử.</p>

<p>Nguyễn Hải Đăng: bốn năm tù giam — hai năm cho tội "vi phạm quy định an toàn giao thông đường thủy" và hai năm cho tội "làm giả tài liệu." Bồi thường thiệt hại cho Phạm Quốc Tuấn: hai trăm triệu đồng — gồm lương mất, tổn thất tinh thần, và chi phí pháp lý.</p>

<p>Bằng thuyền trưởng của Phạm Quốc Tuấn: phục hồi ngay lập tức, kèm thư xin lỗi chính thức từ Cục Hàng hải.</p>

<p>Đăng đứng nghe tuyên án, mặt trắng bệch. Hai cảnh sát tư pháp dẫn y ra — tay còng, đầu cúi, bước qua hành lang tòa án, qua đám phóng viên, qua ống kính camera.</p>

<p>Tuấn đứng ngoài phòng xử, tay cầm tấm bằng thuyền trưởng mới — Cục Hàng hải trao ngay sau phiên tòa. Tấm bằng mới, giấy trắng, mực đen, có chữ ký và con dấu đỏ.</p>

<p>Máy trưởng Phú đến, vỗ vai: "Tuấn, mày thắng rồi."</p>

<p>"Không phải tao thắng, anh. Là sự thật thắng."</p>

<p>Sĩ quan Dũng đứng xa, không dám lại gần. Tuấn đi đến, đưa tay ra.</p>

<p>"Dũng, cảm ơn em đã khai lại."</p>

<p>Dũng bắt tay, mắt đỏ: "Anh ơi, em xin lỗi. Em lẽ ra phải khai thật từ đầu."</p>

<p>"Em khai rồi — chậm nhưng đúng lúc. Đó là đủ."</p>

<hr>

<p>Tối hôm đó, Tuấn ngồi trên bờ kè cảng Hải Phòng, nhìn tàu ra vào. Tay cầm tấm bằng thuyền trưởng, tay kia cầm tấm ảnh bố — ảnh 3x4, ép plastic, góc đã cong.</p>

<p>"Bố ơi, con giữ được bằng. Con vẫn đi biển."</p>

<p>Gió biển thổi. Mùi muối mặn. Tiếng còi tàu xa xa.</p>

<p>Tuấn gấp tấm ảnh, nhét lại vào ví — chỗ cũ, cạnh thẻ thuyền viên. Rồi anh đứng dậy, đi về phòng trọ, soạn đồ.</p>

<p>Ngày mai, anh có hẹn phỏng vấn với một hãng tàu mới — hãng tàu biển Đông Nam. Họ cần thuyền trưởng có kinh nghiệm, có bằng sạch, và có một thứ không ai dạy được: biết đặt mạng người lên trên hàng hóa.</p>"""
    },
    {
        "title": "Chương 10: Ra Khơi Lần Nữa",
        "content": """<p>Tuấn nhận lời làm thuyền trưởng cho hãng tàu Đông Nam — với một điều kiện duy nhất: "Tôi có quyền từ chối xuất bến nếu tàu không đạt chuẩn an toàn."</p>

<p>Giám đốc hãng Đông Nam — ông Trần Văn Bình, sáu mươi tuổi, cựu thuyền trưởng — gật đầu ngay: "Đó không phải điều kiện — đó là quy tắc. Tàu của tôi, thuyền trưởng là vua."</p>

<p>Tàu mới: Việt Hải Star — tàu hàng rời, trọng tải năm nghìn tấn, đóng năm 2020, bảo trì đúng lịch, đăng kiểm Nhật Bản. Vỏ tàu thép đúc dày hơn tiêu chuẩn mười lăm phần trăm. Bơm hút nước: ba cái, công suất lớn, luôn có bơm dự phòng. Áo phao: đủ cho gấp rưỡi thủy thủ đoàn — vì Tuấn yêu cầu thêm.</p>

<p>Trước chuyến đi đầu tiên, Tuấn kiểm tra tàu — từ mũi đến lái, từ boong đến khoang máy, từ phao cứu sinh đến bình chữa cháy. Mất sáu tiếng. Máy trưởng mới — Đỗ Quốc Hùng, ba mươi lăm tuổi — nhìn Tuấn kiểm tra, lắc đầu: "Anh kỹ vậy?"</p>

<p>"Anh đã mất một con tàu vì người ta không kiểm tra. Không mất thêm lần nào nữa."</p>

<hr>

<p>Chuyến đầu: Hải Phòng đi Busan, Hàn Quốc. Bốn nghìn tấn gạo ST25 xuất khẩu.</p>

<p>Tuấn đứng trên đài chỉ huy, nhìn cảng Hải Phòng lùi dần — cần cẩu, container, tàu kéo, bờ kè bê tông — tất cả nhỏ dần rồi biến mất sau đường chân trời.</p>

<p>Biển mở ra trước mắt — xanh thẫm, bao la, và quen thuộc. Mùi muối mặn, tiếng máy tàu rì rì, sàn boong rung nhẹ dưới chân — tất cả trở lại, như thể anh chưa bao giờ rời đi.</p>

<p>Anh mở ví, lấy tấm ảnh bố, dựng trên bàn chỉ huy — cạnh la bàn và bản đồ hải trình.</p>

<p>"Bố ơi, con ra khơi lại rồi."</p>

<p>Gió biển thổi qua cửa sổ đài chỉ huy, tấm ảnh lung lay nhẹ — như thể bố gật đầu.</p>"""
    },
    {
        "title": "Chương 11: Đêm Trăng Trên Biển",
        "content": """<p>Đêm rằm, giữa biển Đông.</p>

<p>Tuấn đứng trên boong tàu Việt Hải Star, nhìn trăng phản chiếu trên mặt biển — mênh mông, lấp lánh, bình yên đến mức anh quên rằng dưới chân mình là vực sâu ba nghìn mét.</p>

<p>Mỗi ngày trên biển, Tuấn viết nhật ký hành trình — viết tay, bằng bút bi, trên sổ bọc nhựa chống nước. Giống hệt cuốn nhật ký mà anh đã trục vớt từ đáy biển.</p>

<p>Anh viết:</p>

<p>"Ngày 15 tháng 6. Vị trí: 17°22' Bắc, 110°45' Đông. Biển lặng, gió cấp 2. Máy hoạt động bình thường. Bơm khoang 3 đã kiểm tra, OK. Vỏ tàu dưới mớn nước đã kiểm tra bằng camera, OK."</p>

<p>"Ngày 16 tháng 6. Gặp đàn cá heo ở 16°50' Bắc. Thủy thủ đoàn phấn khích. Tôi nhớ bố — bố nói cá heo dẫn đường cho ngư dân, thấy cá heo là thấy may mắn."</p>

<p>"Ngày 20 tháng 6. Cập cảng Busan. Gạo ST25 giao đúng hẹn. Đại lý Hàn Quốc khen gạo ngon — hỏi có thêm đơn hàng không."</p>

<p>Anh viết mỗi ngày. Không phải vì luật yêu cầu — luật chỉ yêu cầu ghi chép kỹ thuật. Anh viết vì muốn giữ lại từng ngày trên biển — vì anh biết, sau tất cả, biển không hứa gì với ai. Biển cho ngày lặng, biển cho đêm bão, biển cho cá về, biển cho người đi. Biển là cuộc đời — không công bằng, không bất công — chỉ là biển.</p>

<p>Và anh — Phạm Quốc Tuấn, con trai ngư dân Quảng Ngãi, cựu thuyền trưởng bị vu oan, người đã lặn xuống đáy biển ba mươi mét để tìm sự thật — đứng trên boong tàu đêm rằm, mặt hướng về phía nam, nơi quê nhà nằm bên bờ biển.</p>

<p>Anh lấy bông hoa cúc vàng — mua ở cảng Busan trước khi rời — và nhẹ nhàng thả xuống biển.</p>

<p>"Cho bố. Cho sáu người ngư dân không về."</p>

<p>Bông hoa trôi — nhỏ xíu trên mặt biển đen, ánh trăng rọi, nó lấp lánh một lúc rồi bị sóng cuốn đi, hòa vào biển cả.</p>

<p>Tuấn đứng rất lâu. Không khóc. Không cười. Chỉ đứng — vì đứng trên biển đêm rằm, nghe sóng vỗ nhẹ vào mạn tàu, là điều mà anh suýt mất mãi mãi.</p>

<p>Và anh biết: không phải lúc nào sự thật cũng thắng. Nhưng lần này — lần này, nó thắng. Vì có người dám lặn xuống đáy biển để tìm nó.</p>"""
    }
]

story_data["chapters"] = chapters

with open("scratch/story_5592_rewrite.json", "w", encoding="utf-8") as f:
    json.dump(story_data, f, ensure_ascii=False, indent=2)

print("✅ Truyện 5592 viết xong — 11 CHƯƠNG!")
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
    if ws.cell(row=r, column=2).value and str(ws.cell(row=r, column=2).value).strip() == "5592":
        ws.cell(row=r, column=3).value = story_data["title"]
        ws.cell(row=r, column=4).value = story_data["author"]
        ws.cell(row=r, column=6).value = 11
        ws.cell(row=r, column=12).value = "Thuyền trưởng bị vu oan đắm tàu do say rượu. Lặn xuống đáy biển 30m tìm bằng chứng vỏ tàu nứt do GĐ cắt giảm bảo trì. Thủy thủ đoàn đứng lên. GĐ lĩnh 4 năm tù."
        ws.cell(row=r, column=13).value = "REWRITE TOÀN BỘ: 10 chương quá ngắn (397-940 chars) → 11 CHƯƠNG ĐẦY ĐẶN"
        ws.cell(row=r, column=14).value = "☑️ Đã sửa"
        print(f"  ✅ Excel updated row {r}")
        break
wb.save("danh_sach_truyen_doctieuthuyet.xlsx")
print("\n✅ HOÀN THÀNH TRUYỆN 5592!")
