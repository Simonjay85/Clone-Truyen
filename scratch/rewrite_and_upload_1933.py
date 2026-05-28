import json
import urllib.request

# ============================================================
# TRUYỆN REWRITE: ID 1933 — STT 188
# Tên mới: "Cô Gái Ngồi Cạnh Máy In, Phòng Kế Toán Gọi Tôi Là Đứa Đánh Máy"
# Bối cảnh: Kiểm toán nội bộ tại công ty bất động sản Việt Nam
# Nhân vật chính: Nguyễn Khánh Linh — kế toán viên bị coi thường
# Không siêu nhiên, không tên Trung Quốc
# ============================================================

story_data = {
    "secret_token": "ZEN_TRUYEN_2026_BYPASS",
    "story_id": 1933,
    "title": "Cô Gái Ngồi Cạnh Máy In, Phòng Kế Toán Gọi Tôi Là Đứa Đánh Máy",
    "intro": "<p>Nguyễn Khánh Linh ngồi ở góc khuất nhất phòng kế toán của Tập đoàn Bất động sản Thành Phát — cái bàn sát máy in, nơi tiếng máy chạy rè rè suốt tám tiếng mỗi ngày.</p>\n<p>Ba năm trong công ty, cô chưa từng được giao một hồ sơ quan trọng. Đồng nghiệp gọi cô là \"con bé đánh máy\", sếp trưởng phòng chưa bao giờ nhớ đúng tên cô.</p>\n<p>Nhưng Khánh Linh có một thứ mà không ai biết: cô tốt nghiệp thủ khoa ngành Kiểm toán tại Đại học Kinh tế TP.HCM, và cô đã âm thầm phát hiện ra một lỗ hổng 47 tỷ đồng trong sổ sách mà cả phòng đã cố tình bưng bít suốt hai năm.</p>\n<p>Khi cô quyết định lên tiếng, cả phòng kế toán quay lưng. Nhưng Khánh Linh không cần họ đứng về phía mình — cô chỉ cần sự thật đứng về phía cô.</p>",
    "author": "Phạm Hoàng Minh",
    "seo": {
        "focus_keyword": "cô gái phòng kế toán, kiểm toán nội bộ, gian lận tài chính",
        "seo_title": "Cô Gái Ngồi Cạnh Máy In — Truyện Kiểm Toán Kịch Tính | Đọc Tiểu Thuyết",
        "seo_description": "Bị gọi là đứa đánh máy suốt 3 năm, Khánh Linh âm thầm phát hiện lỗ hổng 47 tỷ đồng. Khi cô lên tiếng, cả phòng kế toán quay lưng."
    },
    "chapters": []
}

# ============================================================
# CHƯƠNG 1: CÁI BÀN SÁT MÁY IN
# ============================================================
ch1 = {
    "title": "Chương 1: Cái Bàn Sát Máy In",
    "content": """<p>Nguyễn Khánh Linh đếm: hôm nay máy in HP LaserJet bên cạnh bàn cô đã chạy bốn mươi ba lần.</p>

<p>Bốn mươi ba lần tiếng rè rè xé qua tai, bốn mươi ba lần giấy A4 phun ra nóng hổi rồi ai đó bước tới nhấc đi mà không thèm liếc cô lấy một cái.</p>

<p>Phòng kế toán Tập đoàn Bất động sản Thành Phát nằm ở tầng mười hai, trông ra đại lộ Nguyễn Huệ. Hai mươi bốn người, chia thành bốn tổ, ngồi trong một không gian mở rộng rãi với bàn gỗ sáng màu và ghế xoay lưng lưới. Mọi thứ đều ngăn nắp, chuyên nghiệp — trừ cái góc của Khánh Linh.</p>

<p>Bàn cô bị đẩy sát tường, kẹp giữa máy in và tủ hồ sơ. Mỗi khi ai đó in tài liệu, họ phải đi ngang qua chỗ cô, và tiện tay nhờ: "Linh ơi, lấy giùm chị mấy tờ vừa in." Hoặc: "Bé Linh, photocopy giúp anh hai bộ nhé."</p>

<p>Bé Linh. Con bé đánh máy. Đứa ngồi cạnh máy in.</p>

<p>Ba năm rồi, Khánh Linh chưa bao giờ được gọi bằng chức danh chính thức của mình: Kế toán viên.</p>

<p>Trưởng phòng Đặng Tuấn Kiệt ngồi ở bàn đầu dãy, vị trí gần cửa sổ nhất, nơi ánh nắng chiều rọi vào tạo thành một vầng sáng xung quanh bàn ông ta — như thể vũ trụ cũng thiên vị. Ông ta năm mươi hai tuổi, tóc vuốt gel bóng mượt, đeo kính gọng vàng, và có thói quen gọi nhân viên bằng biệt danh thay vì tên thật.</p>

<p>"Con bé máy in, đem hồ sơ dự án Phú Mỹ qua đây."</p>

<p>Khánh Linh đứng dậy, bê chồng hồ sơ đi qua hai dãy bàn. Cô hai mươi sáu tuổi, dáng người nhỏ nhắn, tóc buộc đuôi ngựa gọn gàng, gương mặt không trang điểm. Cô mặc áo sơ mi trắng bỏ trong quần tây đen — giống hệt ngày đầu tiên đi làm, giống hệt ba năm trước.</p>

<p>"Anh Kiệt, hồ sơ dự án Phú Mỹ đây ạ."</p>

<p>Đặng Tuấn Kiệt không ngẩng lên. Ông ta đang xem điện thoại, ngón tay lướt qua một bài đăng Facebook của vợ — bà Kiệt vừa check-in ở một resort Phú Quốc.</p>

<p>"Để đó đi."</p>

<p>Khánh Linh đặt hồ sơ xuống, quay người định đi thì nghe tiếng Trần Mỹ Hạnh — kế toán trưởng nhóm thanh toán, ngồi bàn kế bên — bật cười khúc khích.</p>

<p>"Linh ơi, tiện tay in giùm chị cái bảng lương tháng này luôn nhé. File trong email chị gửi sáng nay đó."</p>

<p>"Chị Hạnh, em là kế toán viên, không phải nhân viên photocopy," Khánh Linh nói, giọng nhỏ nhưng rõ ràng.</p>

<p>Cả phòng im bặt. Hai mươi ba cặp mắt quay về phía cô.</p>

<p>Trần Mỹ Hạnh chậm rãi đặt ly cà phê xuống. Chị ta ba mươi lăm tuổi, tốt nghiệp Đại học Mở, vào công ty trước Khánh Linh một năm nhưng đã được thăng chức nhờ mối quan hệ với vợ Tổng Giám đốc. Đôi mắt chị ta nheo lại.</p>

<p>"Em vừa nói gì?"</p>

<p>"Em nói em là kế toán viên," Khánh Linh lặp lại, lần này không nhỏ hơn. "Nếu chị cần in tài liệu, chị có thể tự gửi lệnh in từ máy tính."</p>

<p>Đặng Tuấn Kiệt cuối cùng ngẩng lên, mắt ông ta lạnh tanh.</p>

<p>"Linh, em mới có ba năm kinh nghiệm. Trong phòng này ai cũng phải hỗ trợ nhau. Đừng tỏ thái độ."</p>

<p>Khánh Linh muốn nói: Em có bằng thủ khoa. Em đã phát hiện ra dự án Phú Mỹ có vấn đề từ sáu tháng trước. Em biết chị Hạnh đang ký khống hóa đơn thanh toán cho nhà thầu ma.</p>

<p>Nhưng cô không nói. Chưa phải lúc.</p>

<p>Cô quay về bàn, ngồi xuống, mở máy tính. Màn hình hiện lên bảng tính Excel mà cô đã làm việc suốt sáu tháng qua — không phải file công ty giao, mà là file cô tự tạo.</p>

<p>Một bảng đối chiếu chi tiết: hóa đơn thanh toán cho nhà thầu xây dựng dự án Phú Mỹ Hưng Residence so với báo cáo tiến độ thi công thực tế. Sáu tháng thu thập dữ liệu, so sánh từng con số, kiểm tra chéo với hồ sơ đăng ký kinh doanh của nhà thầu trên Cổng thông tin Quốc gia về Đăng ký Doanh nghiệp.</p>

<p>Kết quả: bốn mươi bảy tỷ đồng thanh toán cho ba nhà thầu không tồn tại.</p>

<p>Ba công ty ma. Ba mươi sáu hóa đơn khống. Tất cả được ký duyệt bởi trưởng phòng Đặng Tuấn Kiệt và kế toán trưởng nhóm Trần Mỹ Hạnh.</p>

<p>Khánh Linh nhìn lên, bắt gặp ánh mắt Mỹ Hạnh đang nhìn cô từ phía bên kia phòng. Chị ta mỉm cười — nụ cười của người tự tin rằng mình đã kiểm soát được mọi thứ.</p>

<p>Khánh Linh cũng mỉm cười lại, rồi cúi xuống tiếp tục làm việc.</p>

<p>Cô không vội. Sáu tháng rồi, thêm vài ngày cũng không sao.</p>

<p>Nhưng tối hôm đó, khi Khánh Linh về đến căn phòng trọ ở quận Bình Thạnh, cô nhận được một email từ địa chỉ lạ.</p>

<p>Tiêu đề: "Tôi biết em đang tìm gì. Gặp tôi ở quán cà phê Highlands Lê Văn Sỹ, 7 giờ sáng mai. Đi một mình."</p>

<p>Khánh Linh nhìn email, ngón tay lướt qua bàn phím. Cô không sợ — cô đã quen với việc bị đe dọa từ khi còn là sinh viên thực tập, khi phát hiện một công ty niêm yết khai khống doanh thu và bị giảng viên hướng dẫn khuyên "đừng dây vào".</p>

<p>Cô đóng laptop, nằm xuống giường, nhìn lên trần nhà.</p>

<p>Ngày mai, bốn mươi bảy tỷ đồng sẽ bắt đầu biết nói.</p>"""
}

# ============================================================
# CHƯƠNG 2: NGƯỜI GỬI EMAIL
# ============================================================
ch2 = {
    "title": "Chương 2: Người Gửi Email",
    "content": """<p>Quán Highlands trên đường Lê Văn Sỹ lúc bảy giờ sáng vắng tanh. Vài bàn rải rác có dân văn phòng ngồi uống cà phê trước giờ làm, mắt dán vào điện thoại.</p>

<p>Khánh Linh chọn bàn góc sát cửa sổ, gọi một ly trà đào cam sả, và chờ.</p>

<p>Đúng bảy giờ mười lăm, một người đàn ông khoảng bốn mươi tuổi bước vào. Anh ta mặc áo polo xám, quần kaki, đeo kính cận gọng đen — trông như một giảng viên đại học hơn là dân tài chính. Anh ta nhìn quanh, thấy Khánh Linh, rồi đi thẳng tới.</p>

<p>"Nguyễn Khánh Linh?"</p>

<p>"Anh là ai?"</p>

<p>Người đàn ông ngồi xuống, đặt một chiếc cặp da mỏng lên bàn.</p>

<p>"Tôi là Phạm Trung Hiếu, kiểm toán viên hành nghề, chứng chỉ CPA Việt Nam số 2847. Trước đây tôi làm ở Deloitte Việt Nam bảy năm, giờ tôi đang làm freelance cho Hội Kiểm toán viên Hành nghề."</p>

<p>Khánh Linh không phản ứng. Cô đợi.</p>

<p>Phạm Trung Hiếu mở cặp, lấy ra một tập giấy mỏng.</p>

<p>"Tôi đã theo dõi dự án Phú Mỹ Hưng Residence từ chín tháng trước, khi một nguồn tin nội bộ cho tôi biết Tập đoàn Thành Phát đang thanh toán cho các nhà thầu không tồn tại. Tôi đã xác minh được hai trong ba công ty ma mà em phát hiện."</p>

<p>Khánh Linh cảm thấy tim đập nhanh hơn, nhưng mặt cô vẫn bình thản.</p>

<p>"Sao anh biết tôi đang tìm hiểu chuyện này?"</p>

<p>"Vì em là người duy nhất trong phòng kế toán truy cập hồ sơ đăng ký kinh doanh của nhà thầu Hùng Phát Construction trên hệ thống Cổng thông tin Doanh nghiệp vào lúc mười một giờ đêm. Phòng IT của Thành Phát ghi log truy cập, và tôi có người quen ở đó."</p>

<p>Khánh Linh đặt ly trà xuống. Cô hiểu ngay: anh ta không đe dọa cô — anh ta đang cảnh báo.</p>

<p>"Anh đang nói rằng họ biết tôi đang tìm hiểu?"</p>

<p>"Chưa. Nhưng sẽ biết sớm thôi. Đặng Tuấn Kiệt không ngu, ông ta có thói quen kiểm tra log truy cập vào cuối mỗi tháng. Tháng này còn ba ngày."</p>

<p>Ba ngày. Khánh Linh tính nhanh trong đầu.</p>

<p>"Vậy anh muốn gì?"</p>

<p>Phạm Trung Hiếu nhìn thẳng vào mắt cô.</p>

<p>"Tôi muốn phối hợp. Em có dữ liệu nội bộ mà tôi không thể tiếp cận — bảng kê thanh toán chi tiết, phiếu chi, ủy nhiệm chi ngân hàng. Tôi có kinh nghiệm kiểm toán và mối quan hệ với Thanh tra Sở Tài chính TP.HCM. Nếu chúng ta kết hợp, hồ sơ sẽ đủ cơ sở để Thanh tra vào cuộc."</p>

<p>"Và nếu tôi bị phát hiện trước khi kịp gửi hồ sơ?"</p>

<p>"Em sẽ bị đuổi việc. Và không chỉ đuổi việc — Đặng Tuấn Kiệt có quan hệ với Phó Tổng Giám đốc Lê Quốc Bảo. Họ có thể vu cho em tội tiết lộ bí mật kinh doanh."</p>

<p>Khánh Linh im lặng một lúc lâu. Tiếng máy pha cà phê trong quán kêu rè rè — giống hệt tiếng máy in ở công ty, cái tiếng đã đi theo cô suốt ba năm.</p>

<p>"Được rồi," cô nói. "Nhưng tôi có điều kiện."</p>

<p>"Nói đi."</p>

<p>"Thứ nhất, tất cả dữ liệu tôi cung cấp phải được mã hóa và lưu trữ trên ổ cứng ngoài, không qua cloud. Thứ hai, tôi sẽ không xuất hiện trong bất kỳ đơn tố cáo nào cho đến khi Thanh tra chính thức vào cuộc. Thứ ba, nếu tôi bị lộ, anh phải đảm bảo rằng tôi có luật sư."</p>

<p>Phạm Trung Hiếu gật đầu chậm rãi.</p>

<p>"Hợp lý. Tôi có một luật sư chuyên về tội phạm tài chính — Nguyễn Thị Thanh Trúc, từng tham gia vụ kiện công ty Địa ốc Hoàng Quân năm 2024."</p>

<p>"Tôi biết vụ đó," Khánh Linh nói. Cô đã đọc toàn bộ bản án trên Cổng thông tin Tòa án khi còn là sinh viên năm ba.</p>

<p>Họ trao đổi thêm hai mươi phút. Phạm Trung Hiếu cho cô một USB mã hóa với phần mềm VeraCrypt đã cài sẵn, mật khẩu là một dãy số mà cô phải nhớ chứ không được ghi ra giấy.</p>

<p>Khi ra khỏi quán, Khánh Linh nhìn đồng hồ: bảy giờ bốn mươi lăm. Cô còn mười lăm phút để đi bộ đến công ty.</p>

<p>Ba ngày. Bốn mươi bảy tỷ đồng. Và một chiếc USB nặng hai mươi gram trong túi áo khoác.</p>

<p>Cô bước nhanh hơn, lòng bàn tay hơi ướt mồ hôi lần đầu tiên trong ba năm.</p>"""
}

# ============================================================
# CHƯƠNG 3: BA NGÀY VÀ BA MƯƠI SÁU HÓA ĐƠN
# ============================================================
ch3 = {
    "title": "Chương 3: Ba Ngày Và Ba Mươi Sáu Hóa Đơn",
    "content": """<p>Ngày thứ nhất.</p>

<p>Khánh Linh đến công ty lúc tám giờ kém năm, sớm hơn mọi người mười lăm phút. Cô bật máy tính, đăng nhập hệ thống kế toán SAP bằng tài khoản của mình, và bắt đầu làm việc bình thường — nhập hóa đơn, đối chiếu công nợ, in báo cáo cho trưởng phòng.</p>

<p>Nhưng trong lúc chờ máy in chạy, cô mở một cửa sổ khác. Không phải trên máy tính công ty — mà trên chiếc điện thoại cá nhân đặt dưới bàn, kết nối WiFi riêng qua hotspot.</p>

<p>Cô chụp ảnh màn hình bảng kê thanh toán dự án Phú Mỹ Hưng Residence — từng phiếu chi, từng ủy nhiệm chi, từng chữ ký phê duyệt. Máy in bên cạnh chạy rè rè che đi tiếng chụp ảnh.</p>

<p>Mỗi lần có người đi ngang, cô đặt điện thoại úp xuống bàn. Tự nhiên như thể đang xem tin nhắn.</p>

<p>Đến trưa, cô đã chụp được sáu mươi bốn ảnh — bao gồm ba mươi sáu hóa đơn thanh toán cho ba nhà thầu: Hùng Phát Construction, Tân Tiến Xây Dựng, và Minh Quang Vật Liệu.</p>

<p>Cô mở ứng dụng Cổng thông tin Doanh nghiệp trên điện thoại, tra cứu mã số thuế của từng công ty:</p>

<p>Hùng Phát Construction — đăng ký tại quận 12, TP.HCM. Giám đốc: Nguyễn Văn Thịnh. Vốn điều lệ: 500 triệu đồng. Ngành nghề: xây dựng dân dụng. Tình trạng: đang hoạt động.</p>

<p>Nhưng khi Khánh Linh kiểm tra địa chỉ trụ sở — số 147 đường Tô Ký, phường Tân Chánh Hiệp — trên Google Maps, cô thấy đó là một quán bún bò Huế.</p>

<p>Tân Tiến Xây Dựng — đăng ký tại Bình Dương. Giám đốc: Lê Thị Hồng Vân. Cùng ngày thành lập với Hùng Phát. Cùng người ký giấy ủy quyền. Trụ sở: một khu đất trống.</p>

<p>Minh Quang Vật Liệu — đăng ký tại Long An. Giám đốc: Trần Minh Quang. Khi Khánh Linh tra trên mạng xã hội, cô tìm thấy Facebook của Trần Minh Quang — một thanh niên hai mươi ba tuổi, sinh viên mới ra trường, hiện đang làm nhân viên giao hàng cho Shopee.</p>

<p>Ba công ty ma. Ba giám đốc bù nhìn. Bốn mươi bảy tỷ đồng chảy vào ba tài khoản ngân hàng rồi biến mất.</p>

<p>Khánh Linh lưu tất cả vào USB mã hóa của Phạm Trung Hiếu, xóa sạch lịch sử duyệt trên điện thoại, và quay lại làm việc như không có gì xảy ra.</p>

<hr>

<p>Ngày thứ hai.</p>

<p>Trần Mỹ Hạnh gọi Khánh Linh vào phòng họp nhỏ lúc mười giờ sáng.</p>

<p>"Linh, ngồi đi."</p>

<p>Khánh Linh ngồi xuống, tay đặt trên đùi, biểu cảm bình thường.</p>

<p>"Em có biết tại sao chị gọi em vào đây không?"</p>

<p>"Không ạ."</p>

<p>Mỹ Hạnh mở laptop, xoay màn hình về phía Khánh Linh. Trên đó là log truy cập hệ thống SAP — dòng highlight vàng ghi rõ: tài khoản NKLINH truy cập module thanh toán dự án Phú Mỹ vào lúc 23:17 ngày 15/05.</p>

<p>"Em truy cập hồ sơ thanh toán dự án Phú Mỹ vào lúc mười một giờ đêm. Tại sao?"</p>

<p>Khánh Linh đã chuẩn bị cho câu hỏi này.</p>

<p>"Em đang làm báo cáo đối chiếu công nợ quý II cho anh Kiệt. Dự án Phú Mỹ có số dư lớn nhất nên em kiểm tra trước."</p>

<p>"Lúc mười một giờ đêm?"</p>

<p>"Dạ, em thường làm thêm ở nhà vì ban ngày không đủ thời gian. Hệ thống SAP cho phép truy cập từ xa qua VPN mà."</p>

<p>Mỹ Hạnh nhìn cô chằm chằm một lúc lâu. Đôi mắt chị ta cố tìm một dấu hiệu nói dối — nhưng Khánh Linh đã quen với áp lực này từ những đêm thi vấn đáp tại đại học.</p>

<p>"Được rồi," Mỹ Hạnh nói, giọng nhẹ hơn nhưng mắt vẫn lạnh. "Nhưng từ giờ, mọi truy cập ngoài giờ phải được anh Kiệt phê duyệt trước. Em hiểu chứ?"</p>

<p>"Dạ, em hiểu."</p>

<p>Khánh Linh ra khỏi phòng họp, tim đập nhanh nhưng bước chân vẫn đều.</p>

<p>Cô biết: đồng hồ đã bắt đầu đếm ngược nhanh hơn.</p>

<p>Tối hôm đó, cô gặp Phạm Trung Hiếu ở một quán phở trên đường Phan Đình Phùng. Cô đưa USB cho anh, kể lại cuộc gặp với Mỹ Hạnh.</p>

<p>"Họ đã nghi em," Hiếu nói, mặt nghiêm lại. "Chúng ta phải nhanh hơn. Tôi sẽ liên hệ Thanh tra Sở Tài chính ngay ngày mai."</p>

<p>"Nhưng hồ sơ đã đủ chưa?"</p>

<p>"Gần đủ. Còn thiếu một thứ: bằng chứng tiền đã chảy về đâu sau khi vào tài khoản ba công ty ma. Nếu có sao kê ngân hàng của các công ty đó, hồ sơ sẽ hoàn chỉnh."</p>

<p>"Sao kê ngân hàng thì tôi không thể lấy được."</p>

<p>"Đúng, nhưng Thanh tra có thể yêu cầu ngân hàng cung cấp — nếu hồ sơ tố cáo đủ cơ sở." Hiếu nhìn cô. "Em đã làm rất tốt, Khánh Linh. Giờ để tôi lo phần còn lại."</p>

<p>Khánh Linh gật đầu, nhưng trong lòng cô biết: ngày mai sẽ là ngày khó nhất.</p>"""
}

# ============================================================
# CHƯƠNG 4: CON MỒI HAY THỢ SĂN
# ============================================================
ch4 = {
    "title": "Chương 4: Con Mồi Hay Thợ Săn",
    "content": """<p>Ngày thứ ba.</p>

<p>Khánh Linh bước vào văn phòng và biết ngay có gì đó sai. Không khí trong phòng kế toán nặng hơn bình thường — kiểu nặng của một phiên tòa trước khi tuyên án.</p>

<p>Đặng Tuấn Kiệt ngồi ở bàn mình, không nhìn điện thoại như mọi ngày. Ông ta đang đọc một tập hồ sơ, mặt cứng như đá.</p>

<p>Trần Mỹ Hạnh ngồi cạnh, hai tay đan chéo trước ngực, mắt nhìn thẳng phía trước.</p>

<p>"Linh, vào phòng họp."</p>

<p>Giọng Đặng Tuấn Kiệt không lớn, nhưng cả phòng nghe rõ. Hai mươi ba đôi mắt nhìn Khánh Linh — lần này không phải ánh mắt thờ ơ quen thuộc. Mà là ánh mắt của những người đang chờ xem ai sẽ ngã.</p>

<p>Phòng họp nhỏ. Bốn người: Khánh Linh, Đặng Tuấn Kiệt, Trần Mỹ Hạnh, và Phó Tổng Giám đốc Lê Quốc Bảo — một người đàn ông năm mươi lăm tuổi, dáng to béo, mặt đỏ au, đeo đồng hồ Rolex Submariner bản vàng.</p>

<p>Lê Quốc Bảo ngồi đầu bàn, tay gõ nhẹ lên mặt gỗ.</p>

<p>"Nguyễn Khánh Linh, tôi đi thẳng vào vấn đề. Chúng tôi phát hiện em đã truy cập trái phép vào hồ sơ thanh toán dự án Phú Mỹ Hưng Residence ngoài giờ hành chính, không có phê duyệt của trưởng phòng."</p>

<p>"Dạ, em có truy cập, nhưng không trái phép. Tài khoản SAP của em có quyền truy cập module thanh toán — đó là phần công việc em được giao."</p>

<p>"Ngoài giờ hành chính, không có phê duyệt."</p>

<p>"Quy chế nội bộ chỉ yêu cầu phê duyệt khi truy cập module nhân sự và lương. Module thanh toán không nằm trong danh sách đó."</p>

<p>Đặng Tuấn Kiệt liếc Mỹ Hạnh. Mỹ Hạnh cúi xuống — cô ta biết Khánh Linh nói đúng.</p>

<p>Lê Quốc Bảo chuyển hướng.</p>

<p>"Được rồi. Nhưng còn vấn đề khác. Chúng tôi có cơ sở để cho rằng em đang thu thập thông tin nội bộ của công ty với mục đích bất hợp pháp."</p>

<p>"Cơ sở nào ạ?"</p>

<p>"Camera an ninh ghi lại em chụp ảnh màn hình máy tính bằng điện thoại cá nhân vào sáng hôm qua."</p>

<p>Khánh Linh cảm thấy máu dồn lên mặt. Camera. Cô đã quên camera góc trần phòng kế toán — cái camera mà cô nghĩ chỉ quay hành lang.</p>

<p>Nhưng cô không để sự hoảng sợ lộ ra.</p>

<p>"Dạ, em chụp ảnh bảng kê thanh toán để đối chiếu với sổ sách ở nhà. Em thường làm thêm ngoài giờ."</p>

<p>"Đối chiếu gì?"</p>

<p>"Đối chiếu số liệu thanh toán với tiến độ thi công thực tế. Em thấy có một số khoản thanh toán chưa khớp với báo cáo tiến độ mà phòng dự án gửi sang."</p>

<p>Câu nói này làm cả ba người đối diện im lặng.</p>

<p>Đặng Tuấn Kiệt nắm chặt tay dưới bàn. Lê Quốc Bảo nheo mắt.</p>

<p>"Em đang ám chỉ điều gì?"</p>

<p>"Em không ám chỉ gì cả," Khánh Linh nói, giọng bình tĩnh. "Em chỉ làm đúng công việc kế toán viên: kiểm tra số liệu, đối chiếu chứng từ. Nếu có sai sót, em sẽ báo cáo theo quy trình."</p>

<p>"Báo cáo cho ai?"</p>

<p>"Cho trưởng phòng," cô nói, nhìn thẳng vào Đặng Tuấn Kiệt. "Trừ khi trưởng phòng cũng là người liên quan đến sai sót đó."</p>

<p>Không khí trong phòng đóng băng.</p>

<p>Đặng Tuấn Kiệt đứng dậy, ghế xoay lùi ra sau kêu cót két.</p>

<p>"Nguyễn Khánh Linh, kể từ bây giờ em bị đình chỉ công việc. Nộp thẻ nhân viên và laptop công ty trước khi ra về."</p>

<p>"Dạ, em hiểu. Nhưng em xin hỏi: quyết định đình chỉ này có được lập thành văn bản không?"</p>

<p>"Gì?"</p>

<p>"Theo Điều 128 Bộ luật Lao động, việc tạm đình chỉ công việc phải có quyết định bằng văn bản, nêu rõ lý do, thời hạn, và người lao động vẫn được nhận ít nhất năm mươi phần trăm tiền lương."</p>

<p>Đặng Tuấn Kiệt mở miệng rồi đóng lại. Ông ta không ngờ cô gái ngồi cạnh máy in lại thuộc luật lao động.</p>

<p>Lê Quốc Bảo vỗ bàn.</p>

<p>"Sẽ có quyết định bằng văn bản! Giờ em ra ngoài đi."</p>

<p>Khánh Linh đứng dậy, bước ra khỏi phòng họp. Hai mươi ba cặp mắt lại nhìn theo cô, nhưng lần này có vài ánh mắt không còn khinh bỉ — mà là ngạc nhiên.</p>

<p>Cô về bàn, nộp thẻ nhân viên, thu dọn đồ cá nhân vào một chiếc túi vải. Máy in bên cạnh vẫn chạy rè rè, phun ra một tập hồ sơ mà không ai nhấc.</p>

<p>Lần đầu tiên trong ba năm, Khánh Linh bước ra khỏi phòng kế toán mà không quay lại nhìn.</p>

<p>Trong túi áo khoác, chiếc điện thoại rung nhẹ. Tin nhắn từ Phạm Trung Hiếu: "Thanh tra Sở Tài chính đã nhận hồ sơ. Họ sẽ ra quyết định kiểm tra trong 48 giờ."</p>

<p>Khánh Linh bước vào thang máy, nhấn nút tầng trệt.</p>

<p>Cánh cửa thang máy đóng lại, và cô nhìn thấy gương mặt mình phản chiếu trên lớp thép bóng — không phải gương mặt của con bé đánh máy nữa.</p>"""
}

# ============================================================
# CHƯƠNG 5: BỐN MƯƠI TÁM GIỜ
# ============================================================
ch5 = {
    "title": "Chương 5: Bốn Mươi Tám Giờ",
    "content": """<p>Bốn mươi tám giờ sau khi Khánh Linh bị đình chỉ, cô nhận được một cuộc gọi từ số lạ vào lúc sáu giờ sáng.</p>

<p>"Nguyễn Khánh Linh? Tôi là Hoàng Minh Đức, Phó Chánh Thanh tra Sở Tài chính TP.HCM. Tôi cần gặp em vào lúc chín giờ sáng nay tại trụ sở Sở Tài chính, số 142 Nguyễn Thị Minh Khai, quận 3."</p>

<p>Khánh Linh ghi lại địa chỉ, xác nhận giờ hẹn, và tắt máy.</p>

<p>Cô ngồi trên giường, nhìn ra cửa sổ căn phòng trọ. Trời Sài Gòn đang mưa — loại mưa nhỏ, dai dẳng, không đủ lớn để che ô nhưng đủ ẩm để thấm vào quần áo.</p>

<p>Cô mặc bộ đồ duy nhất đàng hoàng nhất mình có: áo sơ mi trắng, blazer xám, quần tây đen. Cô soi gương, chải tóc, và lần đầu tiên trong ba năm — cô bôi một chút son.</p>

<p>Không phải để đẹp. Mà để trông như một người đáng được nghe.</p>

<hr>

<p>Trụ sở Sở Tài chính TP.HCM là một tòa nhà hành chính cũ kỹ nhưng trang nghiêm, nằm trên đường Nguyễn Thị Minh Khai. Khánh Linh đến sớm mười phút, ngồi chờ ở phòng tiếp dân tầng hai.</p>

<p>Đúng chín giờ, Phó Chánh Thanh tra Hoàng Minh Đức bước ra — một người đàn ông bốn mươi lăm tuổi, gầy, tóc cắt ngắn, mặt nghiêm nhưng ánh mắt sáng.</p>

<p>"Vào đi, Khánh Linh."</p>

<p>Trong phòng làm việc, ngoài Hoàng Minh Đức còn có hai người: một nữ thanh tra viên và Phạm Trung Hiếu. Hiếu gật đầu chào cô.</p>

<p>"Khánh Linh, chúng tôi đã xem qua hồ sơ mà anh Hiếu chuyển đến. Bây giờ tôi cần em trình bày trực tiếp — em phát hiện bất thường như thế nào, quy trình thu thập dữ liệu, và tất cả những gì em biết."</p>

<p>Khánh Linh hít một hơi sâu.</p>

<p>Rồi cô bắt đầu nói.</p>

<p>Cô nói về cái bàn sát máy in, về việc bị gọi là con bé đánh máy. Cô nói về lần đầu tiên phát hiện bất thường — khi cô đối chiếu phiếu chi thanh toán cho Hùng Phát Construction với báo cáo tiến độ thi công, và thấy rằng một hạng mục đã được thanh toán một trăm phần trăm trong khi tiến độ thực tế chỉ có ba mươi phần trăm.</p>

<p>Cô trình bày bảng đối chiếu mà cô đã xây dựng suốt sáu tháng — từng dòng, từng con số, từng mã số thuế, từng địa chỉ trụ sở ảo.</p>

<p>Cô kể về ba giám đốc bù nhìn: một chủ quán bún bò, một khu đất trống, và một shipper Shopee.</p>

<p>Nữ thanh tra viên ghi chép liên tục. Hoàng Minh Đức lắng nghe không ngắt lời, chỉ thỉnh thoảng gật đầu.</p>

<p>Khi Khánh Linh trình bày xong, phòng im lặng một lúc.</p>

<p>"Em có biết số tiền bốn mươi bảy tỷ sau khi vào tài khoản ba công ty ma thì đi đâu không?" Hoàng Minh Đức hỏi.</p>

<p>"Em không thể truy cập sao kê ngân hàng. Nhưng dựa trên thời điểm thanh toán và các giao dịch bất thường khác trong hệ thống SAP, em nghi rằng tiền được chuyển tiếp vào các tài khoản cá nhân."</p>

<p>"Tài khoản của ai?"</p>

<p>Khánh Linh nhìn xuống bàn tay mình. Cô biết câu trả lời, nhưng cô cũng biết rằng một khi nói ra, không có đường quay lại.</p>

<p>"Em nghi rằng người nhận cuối cùng là Phó Tổng Giám đốc Lê Quốc Bảo," cô nói. "Và người thực hiện quy trình thanh toán là trưởng phòng kế toán Đặng Tuấn Kiệt cùng kế toán trưởng nhóm Trần Mỹ Hạnh."</p>

<p>Hoàng Minh Đức ngồi thẳng lưng hơn.</p>

<p>"Đây là cáo buộc rất nghiêm trọng, Khánh Linh. Em cần hiểu rằng nếu sai, em sẽ phải chịu trách nhiệm pháp lý."</p>

<p>"Em hiểu. Nhưng em có bằng chứng."</p>

<p>"Bằng chứng nào?"</p>

<p>"Ủy nhiệm chi ngân hàng. Người ký duyệt cuối cùng trên tất cả ba mươi sáu khoản thanh toán là Lê Quốc Bảo. Không qua Tổng Giám đốc, không qua Hội đồng quản trị — vi phạm Điều lệ công ty quy định mọi khoản thanh toán trên năm tỷ phải có chữ ký kép."</p>

<p>Hoàng Minh Đức nhìn Phạm Trung Hiếu. Hiếu gật đầu xác nhận.</p>

<p>"Được rồi," Hoàng Minh Đức nói. "Chúng tôi sẽ ra quyết định kiểm tra trong hôm nay. Khánh Linh, từ giờ em là nhân chứng. Em cần giữ liên lạc và không tiết lộ thông tin cho bất kỳ ai ngoài chúng tôi."</p>

<p>Khánh Linh gật đầu.</p>

<p>Khi cô bước ra khỏi trụ sở Sở Tài chính, mưa đã tạnh. Trời Sài Gòn trong vắt sau cơn mưa, ánh nắng chiều rọi xuống vỉa hè ướt, phản chiếu lấp lánh.</p>

<p>Cô đứng lại, ngước nhìn lên bầu trời.</p>

<p>Ba năm ngồi cạnh máy in. Sáu tháng thu thập bằng chứng. Ba ngày đếm ngược. Và hôm nay, cô đã nói ra sự thật.</p>

<p>Bốn mươi bảy tỷ đồng cuối cùng đã biết nói.</p>"""
}

# ============================================================
# CHƯƠNG 6: THANH TRA VÀO CUỘC
# ============================================================
ch6 = {
    "title": "Chương 6: Thanh Tra Vào Cuộc",
    "content": """<p>Đoàn Thanh tra Sở Tài chính TP.HCM đến Tập đoàn Thành Phát vào sáng thứ Hai, đúng một tuần sau ngày Khánh Linh bị đình chỉ.</p>

<p>Bốn người trong đoàn: Phó Chánh Thanh tra Hoàng Minh Đức, hai thanh tra viên, và một chuyên viên phân tích tài chính từ Sở Kế hoạch và Đầu tư.</p>

<p>Họ đến không báo trước.</p>

<p>Khánh Linh biết điều này không phải vì cô có mặt — cô đang ngồi ở quán cà phê đối diện tòa nhà Thành Phát, nhìn qua lớp kính cửa sổ — mà vì Phạm Trung Hiếu nhắn tin cho cô lúc tám giờ ba mươi: "Đoàn đã vào. Kiểm tra bắt đầu."</p>

<p>Cô nhấp một ngụm cà phê, tay hơi run. Không phải sợ — mà là một cảm giác kỳ lạ, như đứng trên bờ vực và biết rằng mình sắp nhảy, nhưng không biết sẽ rơi hay bay.</p>

<hr>

<p>Bên trong tòa nhà Thành Phát, phòng kế toán tầng mười hai rơi vào trạng thái hỗn loạn có kiểm soát.</p>

<p>Đoàn thanh tra yêu cầu niêm phong toàn bộ hồ sơ thanh toán dự án Phú Mỹ Hưng Residence, bao gồm: sổ cái, sổ chi tiết, hóa đơn, phiếu chi, ủy nhiệm chi, và tất cả file mềm trên hệ thống SAP.</p>

<p>Đặng Tuấn Kiệt mặt tái xanh như tờ giấy A4 mà ông ta vẫn bắt Khánh Linh photocopy mỗi ngày. Ông ta cố gắng liên lạc Lê Quốc Bảo, nhưng Phó Tổng đã bị đoàn thanh tra mời vào phòng riêng để "trao đổi".</p>

<p>Trần Mỹ Hạnh ngồi yên tại bàn, hai tay đặt trên đùi, mắt nhìn ra cửa sổ — cái cửa sổ mà trước đây chỉ Đặng Tuấn Kiệt mới được ngồi gần.</p>

<p>Những nhân viên kế toán khác thì thầm với nhau, đoán già đoán non. Ai đó nói: "Chắc liên quan đến con bé Linh bị đuổi tuần trước." Ai đó khác đáp: "Nó biết gì mà liên quan. Chỉ là đứa ngồi cạnh máy in."</p>

<hr>

<p>Cuộc kiểm tra kéo dài ba ngày.</p>

<p>Ngày thứ nhất, đoàn thanh tra đối chiếu hóa đơn thanh toán với hồ sơ đăng ký kinh doanh của ba nhà thầu. Kết quả: trùng khớp hoàn toàn với phát hiện của Khánh Linh — ba công ty ma, không có hoạt động kinh doanh thực tế.</p>

<p>Ngày thứ hai, họ yêu cầu ngân hàng Vietcombank và BIDV cung cấp sao kê tài khoản của ba công ty. Sao kê cho thấy: tiền được chuyển vào rồi rút ra ngay trong ngày, qua nhiều tài khoản trung gian, cuối cùng đổ về hai tài khoản cá nhân — một tại ngân hàng Techcombank chi nhánh Tân Bình, một tại MB Bank chi nhánh quận 1.</p>

<p>Ngày thứ ba, đoàn thanh tra xác minh chủ sở hữu hai tài khoản cá nhân.</p>

<p>Tài khoản Techcombank: đứng tên Lê Thị Phương Thảo — vợ Lê Quốc Bảo.</p>

<p>Tài khoản MB Bank: đứng tên Đặng Hoàng Anh — con trai Đặng Tuấn Kiệt, hai mươi tuổi, sinh viên Đại học Ngoại thương.</p>

<p>Bốn mươi bảy tỷ đồng tiền công ty, chảy qua ba công ty ma, về túi hai gia đình.</p>

<hr>

<p>Khánh Linh nhận được cuộc gọi từ Hoàng Minh Đức vào chiều ngày thứ ba.</p>

<p>"Khánh Linh, kết quả kiểm tra ban đầu đã xác nhận các cáo buộc của em. Chúng tôi sẽ chuyển hồ sơ sang Cơ quan Cảnh sát Điều tra — Công an TP.HCM theo Điều 165 Bộ luật Hình sự về tội Lạm dụng chức vụ, quyền hạn chiếm đoạt tài sản."</p>

<p>"Dạ, em hiểu."</p>

<p>"Và còn một chuyện nữa — Tổng Giám đốc Thành Phát, ông Nguyễn Đình Trung, muốn gặp em. Ông ta nói ông ta không biết gì về vụ việc này."</p>

<p>Khánh Linh không ngạc nhiên. Trong sáu tháng theo dõi, cô nhận thấy rằng tất cả hóa đơn và ủy nhiệm chi đều được phê duyệt bởi Lê Quốc Bảo với tư cách Phó Tổng — tên Nguyễn Đình Trung không xuất hiện ở bất kỳ đâu.</p>

<p>Hoặc ông ta thật sự không biết. Hoặc ông ta rất giỏi giấu mình.</p>

<p>"Em sẽ gặp," Khánh Linh nói.</p>

<p>Cô đặt điện thoại xuống, nhìn ra cửa sổ phòng trọ. Trời chiều Sài Gòn đang chuyển sang cam đỏ — màu của những thứ sắp kết thúc, và những thứ sắp bắt đầu.</p>"""
}

# ============================================================
# CHƯƠNG 7: ĐỐI MẶT
# ============================================================
ch7 = {
    "title": "Chương 7: Đối Mặt",
    "content": """<p>Tổng Giám đốc Nguyễn Đình Trung ngồi trong phòng làm việc ở tầng hai mươi, trước mặt là Khánh Linh và luật sư Nguyễn Thị Thanh Trúc.</p>

<p>Ông Trung sáu mươi tuổi, tóc bạc, gương mặt khắc khổ của một người đã xây dựng công ty từ hai bàn tay trắng — bắt đầu từ một công ty xây dựng nhỏ ở Bình Dương, phát triển thành tập đoàn bất động sản trị giá hai nghìn tỷ trong hai mươi năm.</p>

<p>"Cô là Nguyễn Khánh Linh?" ông ta hỏi, giọng trầm, mệt mỏi.</p>

<p>"Dạ."</p>

<p>"Ba năm trong công ty, ngồi cạnh máy in, và cô phát hiện ra thứ mà cả ban kiểm soát và kiểm toán nội bộ của tôi không tìm ra?"</p>

<p>"Dạ, vì ban kiểm soát của anh không kiểm tra chéo hóa đơn với hồ sơ đăng ký kinh doanh. Và kiểm toán nội bộ chỉ đối chiếu số liệu trên sổ sách — tức là so sánh con số giả với con số giả khác. Em đi từ hướng khác: em so sánh tiền thực với công trình thực."</p>

<p>Nguyễn Đình Trung nhìn cô một lúc lâu.</p>

<p>"Cô tốt nghiệp trường nào?"</p>

<p>"Đại học Kinh tế TP.HCM, ngành Kiểm toán. Thủ khoa khóa 2020."</p>

<p>"Thủ khoa?" Ông ta hơi ngạc nhiên. "Vậy tại sao cô lại ngồi ở vị trí kế toán viên cấp thấp nhất trong ba năm?"</p>

<p>"Vì khi em nộp hồ sơ, phòng nhân sự xếp em vào vị trí trống duy nhất: kế toán viên tổng hợp, bàn số 24 — cạnh máy in. Và trong ba năm, trưởng phòng chưa bao giờ xem xét thăng chức cho em vì em không có mối quan hệ."</p>

<p>Luật sư Thanh Trúc lên tiếng:</p>

<p>"Anh Trung, thân chủ của tôi đã bị đình chỉ công việc trái pháp luật — không có quyết định bằng văn bản, không nêu rõ thời hạn, và không đảm bảo quyền lợi theo Điều 128 Bộ luật Lao động. Chúng tôi yêu cầu khôi phục quyền làm việc và bồi thường."</p>

<p>Nguyễn Đình Trung gật đầu.</p>

<p>"Tôi sẽ xử lý. Đặng Tuấn Kiệt và Trần Mỹ Hạnh đã bị đình chỉ từ hôm qua. Lê Quốc Bảo đang bị Công an TP.HCM triệu tập."</p>

<p>Ông ta quay sang Khánh Linh.</p>

<p>"Cô Linh, tôi nợ cô một lời xin lỗi. Không phải vì tôi sai — mà vì tôi đã không biết rằng trong phòng kế toán của mình có một người như cô."</p>

<p>Khánh Linh không nói gì. Cô nhìn xuống tay mình — đôi bàn tay đã gõ phím suốt ba năm, đã chụp sáu mươi bốn tấm ảnh, đã cầm chiếc USB nặng hai mươi gram.</p>

<p>"Tôi muốn đề nghị cô một vị trí mới," Nguyễn Đình Trung tiếp tục. "Trưởng phòng Kiểm toán Nội bộ — phòng mới, do tôi trực tiếp giám sát. Cô sẽ có quyền tiếp cận tất cả hồ sơ tài chính, không qua bất kỳ ai."</p>

<p>Khánh Linh im lặng một lúc.</p>

<p>"Em cần suy nghĩ."</p>

<p>"Được."</p>

<p>Cô đứng dậy, cúi đầu chào, và bước ra.</p>

<p>Ngoài hành lang, cô gặp Phạm Trung Hiếu đang đứng chờ.</p>

<p>"Sao rồi?" anh hỏi.</p>

<p>"Họ mời em làm trưởng phòng kiểm toán nội bộ."</p>

<p>"Em sẽ nhận?"</p>

<p>Khánh Linh nhìn ra cửa sổ hành lang. Tầng hai mươi, nhìn xuống đại lộ Nguyễn Huệ, phố đi bộ đông đúc dưới ánh đèn chiều.</p>

<p>"Em chưa biết. Nhưng có một thứ em biết chắc."</p>

<p>"Gì?"</p>

<p>"Em sẽ không bao giờ ngồi cạnh máy in nữa."</p>

<p>Phạm Trung Hiếu cười — lần đầu tiên cô thấy anh cười.</p>

<p>"Cũng phải. Em xứng đáng ngồi cạnh cửa sổ."</p>

<p>Khánh Linh mỉm cười, rồi bước vào thang máy. Lần này, cô nhấn nút tầng mười hai — phòng kế toán cũ.</p>

<p>Cô muốn lấy lại một thứ.</p>"""
}

# ============================================================
# CHƯƠNG 8: CÔ GÁI TỪ BÀN SỐ 24
# ============================================================
ch8 = {
    "title": "Chương 8: Cô Gái Từ Bàn Số 24",
    "content": """<p>Khánh Linh bước vào phòng kế toán tầng mười hai lần cuối.</p>

<p>Phòng vắng hơn cô nhớ. Bàn của Đặng Tuấn Kiệt đã bị niêm phong bằng băng keo vàng — loại băng keo mà Thanh tra dùng để đánh dấu tài sản liên quan đến vụ việc. Bàn của Trần Mỹ Hạnh cũng vậy. Hai cái bàn trống hoác, như hai cái lỗ thủng trên tấm vải đã mục.</p>

<p>Hai mươi mốt người còn lại ngẩng đầu nhìn cô.</p>

<p>Không ai nói gì. Không có tiếng "bé Linh", không có tiếng "con bé đánh máy". Chỉ có sự im lặng — loại im lặng của những người nhận ra mình đã nhìn nhầm ai đó suốt ba năm.</p>

<p>Khánh Linh đi thẳng đến bàn số 24 — cái bàn sát máy in, cái bàn kẹp giữa tường và tủ hồ sơ, cái bàn mà không ai muốn ngồi.</p>

<p>Cô mở ngăn kéo, lấy ra một chiếc cốc sứ trắng. Cốc đã cũ, viền bị sứt một mảnh nhỏ ở phía tay cầm — cô mua nó ở chợ đêm Bến Thành bằng đồng lương đầu tiên, hai mươi hai nghìn đồng.</p>

<p>Cô cầm cốc lên, nhìn nó một lúc.</p>

<p>Ba năm cô uống trà từ cái cốc này, mỗi sáng, mỗi chiều, bên tiếng máy in rè rè. Ba năm cô nhìn đồng nghiệp qua lại, lấy giấy, nhờ photocopy, không bao giờ hỏi cô đang làm gì, đang nghĩ gì, đang theo đuổi điều gì.</p>

<p>Lê Thu Hà — kế toán viên ngồi bàn số 23, người hiếm hoi rủ cô đi ăn trưa — rụt rè lên tiếng.</p>

<p>"Linh ơi, chị... chị xin lỗi. Chị biết em không phải đứa đánh máy. Nhưng chị không dám nói gì."</p>

<p>Khánh Linh nhìn Thu Hà. Chị ta ba mươi hai tuổi, hai con nhỏ, chồng chạy Grab. Lương kế toán viên ba mươi triệu — đủ để nuôi gia đình nếu không mất việc.</p>

<p>"Em hiểu, chị Hà. Không ai trách chị được."</p>

<p>Thu Hà mắt đỏ hoe, cúi xuống.</p>

<p>Khánh Linh bỏ cốc vào túi vải, quay người đi ra.</p>

<p>Nhưng khi cô ngang qua bàn trưởng phòng — cái bàn cạnh cửa sổ, nơi ánh nắng chiều từng rọi vào tạo thành vầng sáng xung quanh Đặng Tuấn Kiệt — cô dừng lại.</p>

<p>Cô nhìn ra cửa sổ. Đại lộ Nguyễn Huệ dưới tầng mười hai, phố đi bộ đông đúc, ánh đèn bắt đầu sáng. Sài Gòn về chiều đẹp lạ lùng — kiểu đẹp mà cô chưa bao giờ được ngắm từ góc này, vì cái bàn sát máy in quay lưng vào cửa sổ.</p>

<p>Cô đứng đó một phút. Hai phút. Ba phút.</p>

<p>Rồi cô quay đi.</p>

<hr>

<p>Ba tháng sau.</p>

<p>Cơ quan Cảnh sát Điều tra — Công an TP.HCM khởi tố vụ án hình sự đối với Lê Quốc Bảo, Đặng Tuấn Kiệt, và Trần Mỹ Hạnh về tội "Lạm dụng chức vụ, quyền hạn chiếm đoạt tài sản" theo Điều 355 Bộ luật Hình sự, với số tiền thiệt hại xác định là bốn mươi bảy tỷ ba trăm triệu đồng.</p>

<p>Lê Quốc Bảo bị bắt tạm giam. Đặng Tuấn Kiệt bị cấm xuất cảnh. Trần Mỹ Hạnh hợp tác điều tra và khai nhận toàn bộ.</p>

<p>Nguyễn Đình Trung — Tổng Giám đốc Thành Phát — không bị truy cứu, nhưng ông ta tự nguyện từ chức và chuyển giao quyền điều hành cho Hội đồng Quản trị mới.</p>

<p>Trước khi rời đi, ông ta ký một quyết định cuối cùng: bổ nhiệm Nguyễn Khánh Linh làm Trưởng phòng Kiểm toán Nội bộ Tập đoàn Thành Phát.</p>

<hr>

<p>Khánh Linh nhận quyết định bổ nhiệm vào một buổi sáng thứ Hai.</p>

<p>Phòng làm việc mới của cô ở tầng mười lăm — phòng riêng, có cửa sổ lớn nhìn ra sông Sài Gòn. Bàn làm việc bằng gỗ sồi, ghế lưng cao, một chiếc máy tính Dell mới. Không có máy in trong phòng.</p>

<p>Cô ngồi xuống, đặt chiếc cốc sứ trắng sứt viền lên góc bàn — đúng vị trí nó từng đứng suốt ba năm ở bàn số 24.</p>

<p>Cô mở laptop, bắt đầu ngày làm việc đầu tiên.</p>

<p>Việc đầu tiên cô làm: gửi email cho phòng nhân sự, yêu cầu cung cấp danh sách tất cả nhân viên mới tuyển trong sáu tháng qua — đặc biệt là những người được xếp vào vị trí cấp thấp, ngồi ở những góc khuất, làm những công việc mà không ai để ý.</p>

<p>Vì Khánh Linh biết: trong mỗi công ty, đều có một người ngồi cạnh máy in. Và đôi khi, chính người đó mới là người nhìn thấy rõ nhất.</p>

<p>Cô nhấp một ngụm trà từ chiếc cốc sứt viền, nhìn ra sông Sài Gòn lấp lánh dưới nắng sáng.</p>

<p>Phía dưới tầng mười hai, máy in HP LaserJet vẫn chạy rè rè. Nhưng không còn ai gọi: "Bé Linh, photocopy giùm chị."</p>

<p>Không còn ai gọi cô là con bé đánh máy.</p>

<p>Và sẽ không bao giờ nữa.</p>"""
}

# Compile all chapters
story_data["chapters"] = [ch1, ch2, ch3, ch4, ch5, ch6, ch7, ch8]

# Save to JSON for review
with open("scratch/story_1933_rewrite.json", "w", encoding="utf-8") as f:
    json.dump(story_data, f, ensure_ascii=False, indent=2)

print("✅ Truyện 1933 đã được viết lại hoàn toàn!")
print(f"   Title: {story_data['title']}")
print(f"   Author: {story_data['author']}")
print(f"   Chapters: {len(story_data['chapters'])}")
for i, ch in enumerate(story_data['chapters']):
    wc = len(ch['content'])
    print(f"   Ch{i+1}: {ch['title']} — {wc} chars")
print(f"\n   Saved to scratch/story_1933_rewrite.json")

# Now upload to WordPress
print("\n📤 Uploading to WordPress...")
url = "https://doctieuthuyet.com/overwrite_story_v13.php"
payload = json.dumps(story_data).encode('utf-8')
req = urllib.request.Request(url, data=payload, headers={'Content-Type': 'application/json'})
try:
    resp = urllib.request.urlopen(req, timeout=120)
    result = json.loads(resp.read().decode('utf-8'))
    print(f"   ✅ Upload success!")
    print(f"   Story ID: {result.get('story_id')}")
    print(f"   Title: {result.get('title')}")
    print(f"   Deleted old chapters: {result.get('deleted_old_chapters')}")
    print(f"   New chapters: {result.get('chapters_count')}")
    print(f"   SEO updated: {result.get('seo_updated')}")
except Exception as e:
    print(f"   ❌ Error uploading: {e}")
    import traceback
    traceback.print_exc()
