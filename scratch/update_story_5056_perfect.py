import requests
import json
import os

WP_URL = "https://doctieuthuyet.com"
SECRET_TOKEN = "ZEN_TRUYEN_2026_BYPASS"
STORY_ID = 5056
FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"

# ═══════════════════════════════════════════════════════════════════════════════
# 8 CHƯƠNG HOÀN CHỈNH - BẢN NÂNG CẤP 60/60 THEO TEXT CỦA ANH
# ═══════════════════════════════════════════════════════════════════════════════

INTRO = """<p><strong>"Tôi chết vào đúng ngày đoạn code của mình được định giá năm triệu đô. Kẻ đứng trên sân khấu nhận tràng pháo tay gọi vốn là sếp cũ của tôi. Kẻ mở đường cướp đoạt là bạn thân nhất của tôi. Còn tôi trùng sinh về ba năm trước, quyết tâm giành lại tương lai."</strong></p>
<p>Hành trình trùng sinh sắc lạnh của Ngô Thanh Vy — một kỹ sư phần mềm xuất sắc. Cô không gào khóc đòi lại công bằng bằng nước mắt. Cô thiết lập hệ thống phòng thủ pháp lý ba lớp vững chắc. Khi sếp cũ Phan Văn Đức phản công bằng quy mô quốc tế và gài bẫy cô, Vy đã dùng đến thực lực tối thượng: Neo mã băm SHA-256 lên Bitcoin Mainnet qua giao dịch OP_RETURN và kích hoạt bẫy Trojan trong bản demo 5 triệu đô. Một tác phẩm đỉnh cao về trí tuệ công nghệ, kịch tính nghẹt thở và sâu sắc cảm xúc.</p>"""

CHAPTERS = [
    {
        "title": "Chương 1: Ngày Tôi Chết Vì Đoạn Code Của Chính Mình",
        "content": """<p>Tôi chết vào đúng ngày đoạn code của mình được định giá năm triệu đô.</p>
<p>Người đứng trên sân khấu nhận tràng pháo tay là Phan Văn Đức, sếp cũ của tôi.</p>
<p>Người ngồi hàng ghế đầu mỉm cười vỗ tay cho hắn là Lê Ngọc, bạn thân nhất của tôi.</p>
<p>Còn tôi đứng ngoài sảnh khách sạn, áo mưa ướt sũng, điện thoại trong tay liên tục hiện cuộc gọi nhỡ từ bệnh viện.</p>
<p>“Cô Vy, bên em đã nhắc nhiều lần rồi. Nếu trong hôm nay gia đình không đóng thêm tạm ứng, ca phẫu thuật của mẹ cô phải dời lại.”</p>
<p>Giọng điều dưỡng nhỏ nhẹ, nhưng từng chữ rơi xuống như kim.</p>
<p>Tôi nhìn qua lớp cửa kính dày của khách sạn năm sao. Bên trong là ánh đèn, máy quay, nhà đầu tư, champagne và những tấm backdrop xanh đậm in logo: <strong>LogiMind AI — The Future of Smart Supply Chain.</strong></p>
<p>Cái tên đó là của tôi. Không. Chính xác hơn, cái lõi thuật toán bên trong nó là của tôi.</p>
<p>Tôi đã viết nó trong một căn phòng trọ nóng như lò hấp ở Tân Bình. Ba giờ sáng, quạt máy kêu rè rè, mẹ nằm ngủ trên tấm nệm mỏng cạnh bàn làm việc vì bà sợ tôi thức khuya rồi ngất. Tôi vừa sửa bug, vừa nghe tiếng mẹ ho khan sau lưng.</p>
<p>“Vy, ngủ đi con. Tiền từ từ kiếm.”</p>
<p>Tôi cười, mắt dán vào màn hình: “Xong cái này là con kiếm được nhiều tiền rồi. Mẹ khỏi lo viện phí nữa.”</p>
<p>Tôi đã tin như vậy. Cho đến khi Phan Văn Đức gọi tôi vào phòng họp.</p>
<p>Hắn là CTO kiêm đồng sáng lập công ty logistics nơi tôi làm việc. Ở văn phòng, người ta gọi hắn là “anh Đức vision”. Hắn nói chuyện như sách quản trị, cười như diễn giả TED Talk, và luôn biết đặt tay lên vai nhân viên đúng lúc camera công ty quay tới. Hôm đó, hắn đưa tôi một bản phụ lục hợp đồng: “Vy, sản phẩm này phát triển trên hạ tầng công ty. Em ký xác nhận chuyển giao IP đi. Quy trình thôi.”</p>
<p>Tôi không ký. Ba ngày sau, tài khoản GitLab của tôi bị khóa. Năm ngày sau, Lê Ngọc — người từng ăn mì gói với tôi lúc tôi debug thuật toán — gửi email nội bộ nói rằng ý tưởng LogiMind AI là của team Đức từ đầu, còn tôi chỉ là nhân sự triển khai cấp dưới. Bảy ngày sau, công ty đuổi việc tôi vì “vi phạm bảo mật mã nguồn”. Mười ngày sau, mẹ tôi phải hoãn mổ.</p>
<p>Và hôm nay, Đức đứng trên sân khấu gọi vốn năm triệu đô bằng chính thứ đã đạp tôi xuống bùn. Tôi chen qua đám bảo vệ ở sảnh.</p>
<p>“Tôi cần gặp Phan Văn Đức.”</p>
<p>Một người mặc vest đen chặn tôi lại: “Chị có thư mời không?”</p>
<p>“Tôi là người viết hệ thống đó.”</p>
<p>Anh ta nhìn tôi từ đầu đến chân. Áo mưa rẻ tiền, tóc bết nước, đôi giày vải đã bung keo. Ánh mắt đó tôi quá quen. Ánh mắt của người đã quyết định bạn thua ngay từ bề ngoài.</p>
<p>Cửa hội trường mở hé. Giọng Đức vang ra qua loa: “LogiMind AI không chỉ là một sản phẩm. Nó là giấc mơ của tôi suốt năm năm qua.”</p>
<p>Cả hội trường vỗ tay. Tôi bật cười. Năm năm của hắn. Còn ba năm không ngủ của tôi thì tính bằng gì?</p>
<p>Tôi gọi cho Lê Ngọc. Cô ta bắt máy sau hồi chuông thứ ba: “Ngọc, tại sao?”</p>
<p>Bên kia im vài giây. Sau đó là tiếng nhạc tiệc xa xa: “Vy, cậu đừng làm mọi chuyện xấu hơn nữa.”</p>
<p>“Tớ từng cho cậu ở nhờ ba tháng. Tớ kéo cậu vào team. Tớ kể cho cậu nghe từng module, từng mô hình tối ưu tuyến đường. Cậu biết mẹ tớ đang nằm viện.”</p>
<p>“Chính vì biết nên tớ mới khuyên cậu tỉnh táo.” Giọng Ngọc hạ thấp. “Đức có luật sư. Có nhà đầu tư. Có truyền thông. Cậu có gì?”</p>
<p>Tôi siết điện thoại đến đau ngón tay: “Tớ có sự thật.”</p>
<p>Ngọc cười rất nhẹ: “Ở đời này, sự thật không tự thắng đâu Vy. Người cầm micro mới thắng.”</p>
<p>Cuộc gọi tắt. Màn hình điện thoại chuyển sang thông báo livestream. Đức đang đứng cạnh đại diện quỹ ngoại, nâng ly. Dòng chữ chạy bên dưới: <strong>LogiMind AI chính thức nhận cam kết đầu tư 5 triệu USD.</strong></p>
<p>Đúng lúc đó, bệnh viện gọi lại: “Mẹ cô vừa tụt huyết áp. Cô đến ngay được không?”</p>
<p>Tôi xoay người chạy ra đường. Mưa Sài Gòn tháng Bảy xối xuống mặt nóng rát. Tôi không nhớ mình đã băng qua bao nhiêu ngã tư. Chỉ nhớ tiếng còi xe tải rất gần, ánh đèn pha trắng lóa, và trong khoảnh khắc cuối cùng, tôi nhìn thấy trên màn hình điện thoại một bình luận trong livestream: <strong>Anh Đức đúng là thiên tài công nghệ Việt.</strong></p>
<p>Tôi muốn cười. Thiên tài? Không. Hắn chỉ là một tên trộm biết mặc vest.</p>
<p>Tiếng phanh rít xé tai. Cơ thể tôi bị hất lên. Điện thoại văng khỏi tay, trượt trên mặt đường loang nước. Trước khi bóng tối nuốt chửng mọi thứ, tôi nghe thấy tiếng mẹ trong ký ức: “Vy, ngủ đi con.”</p>
<p>Nhưng lần này, tôi không muốn ngủ. Tôi muốn quay lại. Tôi muốn sống. Tôi muốn dùng từng dòng code hắn cướp của tôi để kéo hắn xuống khỏi sân khấu.</p>
<p>Khi mở mắt lần nữa, tôi nghe tiếng quạt máy kêu rè rè. Trần nhà loang lổ. Mùi mì gói. Mùi cà phê hòa tan. Mùi thuốc dầu mẹ hay xoa lên cổ tay. Tôi bật dậy. Laptop trước mặt vẫn sáng. Terminal hiện dòng lệnh quen thuộc:</p>
<p><code>git commit -m "init route optimization engine"</code></p>
<p>Tôi nhìn góc phải màn hình. Ngày 12 tháng 4. Ba năm trước ngày tôi chết. Trên chiếc nệm dưới sàn, mẹ tôi trở mình, giọng ngái ngủ: “Vy, sao còn chưa ngủ?”</p>
<p>Tôi che miệng. Nước mắt trào ra không kịp giữ. Mẹ còn sống. Đoạn code còn ở đây. Và Phan Văn Đức vẫn chưa kịp cướp nó.</p>
<p>Tôi lau nước mắt, đặt tay lên bàn phím. Kiếp trước, hắn lấy giấc mơ của tôi, lấy tiền cứu mẹ tôi, lấy cả mạng của tôi. Kiếp này, tôi sẽ không đòi lại bằng nước mắt. Tôi sẽ đòi bằng bằng chứng. Và tôi sẽ bắt hắn đọc từng dòng một trước mặt tất cả những người từng vỗ tay cho hắn.</p>"""
    },
    {
        "title": "Chương 2: Trùng Sinh Về Đêm Commit Đầu Tiên",
        "content": """<p>Tôi ngồi bất động trước laptop gần mười phút. Không phải vì sợ. Mà vì tôi đang kiểm tra xem mình có thật sự sống lại hay chỉ là bộ não hấp hối tự tạo ra một giấc mơ cuối cùng. Tôi mở điện thoại. Pin 17%. Màn hình nứt một đường nhỏ ở góc phải, đúng chiếc điện thoại tôi dùng ba năm trước. Ngày 12 tháng 4. 3:17 sáng.</p>
<p>Trong Zalo, tin nhắn mới nhất của mẹ gửi lúc 11 giờ đêm: <strong>“Con làm xong nhớ ăn cháo trong nồi. Mẹ để sẵn đó.”</strong></p>
<p>Tôi quay sang nhìn mẹ. Bà nằm co người trên tấm nệm mỏng, một tay đặt lên bụng. Căn bệnh của mẹ lúc này chỉ mới ở giai đoạn đầu. Kiếp trước, vì tôi mất việc, vì tiền viện phí bị đứt, vì hồ sơ bảo hiểm bổ sung không kịp hoàn tất, mẹ đã bỏ lỡ thời điểm điều trị tốt nhất. Tôi đứng dậy, đi thật nhẹ đến bên bà. Tay mẹ ấm. Ấm đến mức tôi suýt bật khóc lần nữa.</p>
<p>Nhưng tôi không cho phép mình yếu thêm. Khóc không lưu timestamp. Nước mắt không có giá trị trước tòa.</p>
<p>Tôi quay lại bàn, mở repo local. Kiếp trước, sai lầm lớn nhất của tôi không phải là tin Đức. Sai lầm lớn nhất là tôi nghĩ tài năng tự nó sẽ được công nhận. Không. Tài năng không có chứng cứ thì chỉ là lời kể. Tôi bắt đầu tạo lại toàn bộ hàng rào bảo vệ. Đầu tiên là Git.</p>
<p>Tôi cấu hình GPG key, ký commit, đẩy repo lên một remote riêng đứng tên cá nhân. Không dùng email công ty. Không dùng máy công ty. Không dùng server công ty. Mỗi module tôi viết đều có commit message rõ ràng: ngày, mục đích, mô tả thuật toán, input, output, giới hạn sử dụng. Không còn kiểu “fix bug”, “update”, “final final thật sự final” như kiếp trước.</p>
<p>Tôi tạo thư mục <code>/docs/original-design-notes</code>, viết lại bản thiết kế kiến trúc bằng tiếng Việt và tiếng Anh. Tôi ghi rõ: thuật toán tối ưu tuyến đường kết hợp dữ liệu tồn kho, thời tiết, khung giờ cấm tải, chi phí nhiên liệu và độ ưu tiên đơn hàng. Tôi không viết như dev ghi chú cho mình đọc. Tôi viết như đang chuẩn bị cho một phiên điều trần. Sau đó tôi tạo hash SHA-256 cho toàn bộ gói mã nguồn và tài liệu. Màn hình hiện ra một chuỗi ký tự dài lạnh lùng. Tôi nhìn nó như nhìn một con dao.</p>
<p>Kiếp trước, tôi mang trái tim đi đấu với những kẻ cầm hợp đồng. Kiếp này, tôi mang hash. Tôi in bản mô tả thuật toán, bản log commit, bản hash, rồi bỏ vào một phong bì nâu. Trên bìa, tôi viết: <strong>Hồ sơ xác lập thời điểm tạo lập — LogiMind Route Optimization Core — Trần Hoài Vy.</strong></p>
<p>Sáu giờ sáng, mẹ thức dậy thấy tôi đang thay áo: “Con đi đâu sớm vậy?”</p>
<p>“Con ra bưu điện rồi ghé văn phòng luật sư.”</p>
<p>Mẹ ngồi bật dậy: “Luật sư? Con gây chuyện gì hả?”</p>
<p>Tôi khựng lại. Kiếp trước, tôi không kể cho mẹ nghe bất cứ áp lực nào ở công ty. Tôi sợ bà lo. Tôi sợ bà bệnh nặng hơn. Tôi giấu đến mức khi tôi bị đuổi, bà vẫn tưởng tôi xin nghỉ phép để ở nhà chăm bà. Kết quả là chúng tôi cùng chìm. Lần này, tôi ngồi xuống bên mẹ.</p>
<p>“Không phải gây chuyện. Con đang bảo vệ thứ con làm ra.”</p>
<p>Mẹ nhìn tôi rất lâu. Bà không hỏi sâu. Có lẽ vì bà nghe ra trong giọng tôi có một thứ gì đó khác. Không phải hoảng hốt. Là quyết tâm của người từng mất tất cả.</p>
<p>Bưu điện lúc bảy giờ sáng còn vắng. Tôi gửi phong bì bằng dịch vụ bảo đảm, yêu cầu lưu chứng từ, chụp lại biên lai, quay video lúc nhân viên đóng dấu ngày. Sau đó tôi đến văn phòng luật sư Nguyễn Minh Khoa, một luật sư sở hữu trí tuệ mà kiếp trước tôi chỉ biết đến sau khi mọi thứ đã quá muộn.</p>
<p>Anh Khoa nghe tôi trình bày gần một tiếng. Ban đầu ánh mắt anh có vẻ nghi ngờ. Một cô gái hai mươi bốn tuổi, tóc buộc vội, mắt thâm vì thức đêm, bước vào nói rằng mình đang chuẩn bị chống lại một CTO có tiếng trong ngành logistics. Câu chuyện nghe như paranoia của dân startup bị stress. Cho đến khi tôi mở laptop. Tôi cho anh xem commit ký số, tài liệu thiết kế, bản hash, video gửi phong bì, và sơ đồ các điểm có thể bị Đức lợi dụng.</p>
<p>Anh Khoa ngả người ra ghế: “Em chuẩn bị kỹ hơn nhiều founder anh từng gặp.”</p>
<p>Tôi cười nhạt: “Vì em không chuẩn bị cho gọi vốn. Em chuẩn bị cho chiến tranh.”</p>
<p>Anh im vài giây: “Anh nói thẳng. Bằng chứng kỹ thuật mạnh, nhưng không đủ nếu đối phương ép em ký chuyển giao quyền sở hữu hoặc chứng minh rằng em làm trong phạm vi công việc được giao.”</p>
<p>“Tức là em không được ký bất cứ thứ gì mập mờ.”</p>
<p>“Đúng. Không gửi source lên server công ty. Không dùng email công ty để trao đổi phần lõi. Không thừa nhận nó là sản phẩm nội bộ. Và tuyệt đối không để họ biến em thành người ăn cắp ngược lại.”</p>
<p>Tôi gật đầu: “Em cần anh giữ một bản hồ sơ.”</p>
<p>“Được. Anh sẽ lập biên bản tiếp nhận tài liệu và gửi xác nhận qua email cho em.”</p>
<p>Khi rời văn phòng luật sư, tôi nhận được tin nhắn từ Phan Văn Đức: <strong>Vy, chiều nay lên phòng anh. Có chuyện về module tối ưu tuyến đường.</strong></p>
<p>Tôi nhìn dòng chữ đó. Kiếp trước, đây là tin nhắn mở đầu cho địa ngục. Tôi từng bước vào phòng hắn với tâm thế một nhân viên muốn được công nhận. Lần này, tôi bước vào với máy ghi âm trong túi áo.</p>
<p>Ba giờ chiều, văn phòng công ty vẫn như cũ: máy lạnh quá lạnh, bảng KPI quá lớn, những câu slogan dán tường quá giả: <strong>Move Fast. Own The Future.</strong> Tôi suýt bật cười. Kiếp trước, hắn đúng là move rất fast. Fast đến mức cướp tương lai của tôi luôn. Phòng Đức ở cuối hành lang. Cửa kính mờ, bên trong treo một tấm bằng MBA và ảnh hắn bắt tay với vài nhà đầu tư. Hắn ngẩng đầu khi tôi bước vào: “Vy, ngồi đi.”</p>
<p>Giọng hắn ấm áp, đúng kiểu lãnh đạo biết dùng sự tử tế như dây thòng lọng. “Anh nghe Ngọc nói em đang làm một engine tối ưu tuyến khá thú vị.”</p>
<p>Tôi nhìn hắn. Vậy là bắt đầu rồi. Tôi đặt điện thoại úp xuống bàn, ngón tay khẽ chạm nút ghi âm: “Dạ, chỉ là prototype cá nhân thôi anh.”</p>
<p>Đức mỉm cười: “Cá nhân gì. Em là người công ty, bài toán em giải cũng là bài toán công ty. Đừng tách bạch quá, mất tinh thần team.”</p>
<p>Kiếp trước, câu này làm tôi thấy áy náy. Kiếp này, tôi chỉ thấy buồn cười. Tinh thần team là khi cùng làm, cùng hưởng. Không phải một người thức trắng, một người đứng sân khấu. Tôi cúi xuống mở sổ: “Vậy anh muốn em hỗ trợ phần nào?”</p>
<p>Đức chống tay lên bàn: “Đẩy source lên server nội bộ trước. Anh xem qua architecture rồi tính đưa vào roadmap quý tới.”</p>
<p>Tôi ngẩng đầu, nhìn thẳng vào mắt hắn: “Source cá nhân của em chưa sẵn sàng chuyển giao. Nhưng em có thể demo ý tưởng ở mức high-level.”</p>
<p>Nụ cười của Đức nhạt đi nửa giây. Rất nhanh thôi. Nhưng tôi thấy. “Vy, anh không thích nhân viên giữ riêng tài sản trí tuệ liên quan đến công việc.”</p>
<p>Tôi đóng sổ lại: “Em cũng không thích người khác nhận nhầm tài sản trí tuệ của em.”</p>
<p>Không khí trong phòng lạnh hẳn. Đức nhìn tôi. Lần đầu tiên trong cả hai kiếp, hắn nhận ra con mồi trước mặt không đi theo lối cũ. Tôi đứng dậy: “Chiều nay em còn task. Em gửi anh bản mô tả tổng quan sau.”</p>
<p>Tôi mở cửa bước ra. Sau lưng, giọng Đức vang lên, vẫn nhẹ nhưng đã có gai: “Vy, trong ngành này, thông minh thôi chưa đủ đâu.”</p>
<p>Tôi quay lại, cười: “Dạ. Nên em mới học thêm cách lưu bằng chứng.”</p>
<p>Cửa kính khép lại. Ván cờ bắt đầu.</p>"""
    },
    {
        "title": "Chương 3: Sếp Cũ Bắt Đầu Vươn Tay",
        "content": """<p>Một ngày sau cuộc gặp với Đức, Lê Ngọc rủ tôi xuống quán cà phê dưới tòa nhà.</p>
<p>Kiếp trước, tôi đã đi. Ngọc ngồi đối diện tôi, gọi trà đào, nói bằng giọng của một người bạn thân đang lo lắng: “Vy, tớ nghĩ cậu nên mềm với anh Đức một chút. Ảnh đang muốn nâng cậu lên tech lead đó.” Tôi đã tin. Tôi đã tưởng cô ấy thật lòng muốn tốt cho mình. Tôi đã kể cho cô ấy nghe rằng module tối ưu tuyến đường còn thiếu phần dynamic constraint, rằng tôi định dùng thêm dữ liệu thời tiết và lịch cấm tải theo quận. Hai tuần sau, những ý tưởng đó xuất hiện trong slide của Đức.</p>
<p>Kiếp này, tôi vẫn đi. Nhưng lần này, tôi gọi cà phê đen không đường. Ngọc đến trễ mười phút, váy công sở màu kem, son hồng đất, tóc uốn nhẹ. Cô ấy luôn biết cách trông vô hại. Đó là vũ khí mạnh nhất của Ngọc.</p>
<p>“Vy, dạo này cậu lạ lắm.”</p>
<p>Tôi khuấy cà phê: “Lạ chỗ nào?”</p>
<p>“Căng với anh Đức. Giữ source riêng. Hôm qua ảnh hỏi tớ cậu có đang bất mãn gì không.”</p>
<p>Tôi nhìn cô ấy: “Vậy cậu trả lời sao?”</p>
<p>Ngọc hơi khựng: “Tớ nói chắc cậu stress thôi. Mẹ cậu bệnh mà.”</p>
<p>Cô ấy nhắc đến mẹ tôi rất tự nhiên. Kiếp trước, chính sự tự nhiên đó khiến tôi không phòng bị. Vì một người biết mẹ bạn đang bệnh mà vẫn nhẹ nhàng hỏi thăm, trông không giống kẻ sắp đâm dao sau lưng. Tôi mỉm cười: “Ừ, mẹ tớ bệnh. Nên tớ càng không thể để ai lấy mất thứ có thể cứu mẹ.”</p>
<p>Ngọc đặt ly xuống: “Cậu nói vậy nghe nặng nề quá. Công ty đâu có lấy của cậu. Nếu sản phẩm thành công, cậu cũng được hưởng mà.”</p>
<p>“Hưởng gì?”</p>
<p>“Thưởng dự án. Cơ hội thăng tiến. Danh tiếng.”</p>
<p>Tôi bật cười: “Danh tiếng không trả viện phí được, Ngọc.”</p>
<p>Mặt cô ấy thoáng khó chịu. Tôi biết vì sao. Trong lòng Ngọc, cô ấy luôn xem mình thực tế hơn tôi. Cô ấy tin rằng người như tôi giỏi kỹ thuật nhưng ngây thơ, cần một người biết đời chỉ lối. Kiếp trước, cô ấy đã nói đúng một câu: sự thật không tự thắng. Nhưng cô ấy quên mất, sự thật cũng có thể học cách cầm micro. Tôi lấy điện thoại, mở một bản demo đã cắt bỏ toàn bộ phần lõi: “Cậu muốn xem không?”</p>
<p>Mắt Ngọc sáng lên: “Được hả?”</p>
<p>“Ừ. Bản mock thôi.” Tôi xoay màn hình cho cô ấy xem dashboard. Các tuyến đường chạy mượt, nhưng dữ liệu đều là giả lập. Phần engine thật nằm ở máy khác, repo khác, không kết nối mạng công ty. Ngọc nhìn chăm chú: “Cậu làm một mình thật à?”</p>
<p>“Ừ.”</p>
<p>“Đỉnh quá.”</p>
<p>Câu khen nghe thật đến mức nếu là tôi trước kia, tôi đã mềm lòng. Tôi tắt màn hình: “Nhưng chưa đủ để gửi cho ai.”</p>
<p>Ngọc im lặng.</p>
<p>Buổi chiều hôm đó, phòng nhân sự gửi cho tôi một phụ lục hợp đồng mới. Tiêu đề rất đẹp: <strong>Biên bản xác nhận tham gia phát triển tài sản trí tuệ nội bộ.</strong> Nội dung thì xấu hơn nhiều. Tất cả ý tưởng, prototype, tài liệu, thuật toán liên quan đến logistics, tuyến đường, kho vận, dữ liệu giao hàng trong thời gian tôi làm việc tại công ty đều thuộc sở hữu công ty, bất kể được phát triển bằng thiết bị cá nhân hay ngoài giờ.</p>
<p>Tôi đọc đến dòng cuối thì cười. Kiếp trước, tôi đã ký sau khi Đức nói: “Quy trình thôi, ai cũng ký.” Sau đó chính tờ giấy này biến tôi từ tác giả thành kẻ làm thuê.</p>
<p>Tôi chụp lại toàn bộ, gửi cho luật sư Khoa. Anh trả lời sau mười hai phút: <strong>Không ký. Đề nghị họ nêu rõ phạm vi công việc, task được giao, thiết bị sử dụng, thời điểm tạo lập. Anh sẽ soạn phản hồi.</strong></p>
<p>Tôi gửi email cho HR, cc Đức: <strong>Em cần làm rõ phạm vi điều khoản trước khi ký. Prototype cá nhân của em được phát triển ngoài giờ làm việc, bằng thiết bị cá nhân, trước khi có bất kỳ assignment chính thức nào từ công ty. Vui lòng cung cấp căn cứ cho việc yêu cầu chuyển giao.</strong></p>
<p>Năm phút sau, Đức gọi tôi vào phòng họp. Lần này không chỉ có hắn. HR có mặt. Trưởng phòng pháp chế có mặt. Ngọc cũng có mặt, với vai trò “Product Coordinator”. Tôi bước vào, đặt laptop lên bàn. Đức nhìn tôi bằng ánh mắt của người vừa mất kiên nhẫn: “Vy, em đang làm mọi chuyện phức tạp.”</p>
<p>Tôi ngồi xuống: “Em chỉ đang đọc kỹ giấy tờ trước khi ký.”</p>
<p>Trưởng phòng pháp chế, một chị tên Hạnh, đẩy kính: “Điều khoản này là chuẩn. Tất cả nhân viên kỹ thuật đều ký.”</p>
<p>“Chuẩn không có nghĩa là áp dụng vô hạn.”</p>
<p>Hạnh nhíu mày. Tôi mở laptop, giọng bình tĩnh: “Em được tuyển làm backend developer cho hệ thống tracking đơn hàng hiện tại. Trong JD và các task Jira được giao, không có mục nào yêu cầu em phát triển engine tối ưu tuyến đường bằng AI. Prototype này được tạo ngoài giờ, bằng máy cá nhân, dữ liệu giả lập cá nhân. Em có log thời gian, tài liệu thiết kế và xác nhận pháp lý về thời điểm tạo lập.”</p>
<p>Ngọc nhìn tôi. Tôi thấy rõ sự hoảng nhẹ trong mắt cô ấy. Đức chống tay lên bàn: “Em nói vậy là đang phủ nhận đóng góp của công ty?”</p>
<p>“Không. Em đang phủ nhận việc công ty nhận đóng góp chưa từng tồn tại.”</p>
<p>HR ho khan. Không khí căng như dây đàn. Đức cười, nhưng nụ cười không còn ấm: “Vy, anh thấy em bị ảnh hưởng tâm lý vì chuyện gia đình. Công ty có thể cho em nghỉ vài ngày.”</p>
<p>Đây rồi. Kiếp trước, hắn cũng dùng câu này. Biến sự phản kháng của tôi thành bất ổn tinh thần. Tôi nhìn thẳng vào hắn: “Cảm ơn anh. Nhưng sức khỏe tinh thần của em không liên quan đến quyền sở hữu trí tuệ.”</p>
<p>Tôi quay sang HR: “Em đề nghị mọi trao đổi về phụ lục này được thực hiện qua email.”</p>
<p>Hạnh mím môi. Đức im lặng ba giây. Rồi hắn ngả người ra ghế: “Được. Nếu em muốn làm việc bằng giấy tờ, chúng ta làm bằng giấy tờ.”</p>
<p>Tôi gập laptop: “Dạ.” Tôi đứng dậy rời phòng. Khi đi ngang qua Ngọc, cô ấy khẽ gọi: “Vy.”</p>
<p>Tôi dừng lại.</p>
<p>“Cậu đang đẩy mình vào thế khó đó.”</p>
<p>Tôi nhìn cô ấy: “Không, Ngọc. Tớ chỉ không còn đứng yên cho người khác đẩy nữa.”</p>
<p>Tối hôm đó, tôi nhận được email cảnh cáo đầu tiên. Lý do: không hợp tác trong quy trình nội bộ. Tôi lưu email vào thư mục bằng chứng. Đặt tên file: <strong>duc_pressure_attempt_01.pdf</strong>. Rồi tôi tiếp tục code. Ngoài cửa sổ, Sài Gòn sáng đèn. Dòng xe dưới đường như những mạch dữ liệu đang chuyển động. Tôi biết Đức sẽ không dừng. Tôi cũng vậy.</p>"""
    },
    {
        "title": "Chương 4: Nhật Ký Git Không Biết Nói Dối",
        "content": """<p>Ba ngày sau email cảnh cáo, Đức tung nước cờ thứ hai. Hắn tổ chức một cuộc họp kỹ thuật toàn team, chủ đề nghe rất sạch sẽ: <strong>Innovation Sprint — Route Intelligence Module.</strong></p>
<p>Tôi nhìn lịch họp trong Outlook, cười lạnh. Kiếp trước, cuộc họp này là nơi hắn lấy ý tưởng của tôi trước mặt mười hai người, rồi biến nó thành “brainstorming của team”. Tôi đã trình bày say sưa, tin rằng cuối cùng mình được công nhận. Ngay sau đó, Đức tổng hợp thành slide, gửi cho ban giám đốc dưới tên hắn. Lần này, tôi vào họp với một bản demo rỗng, một file ghi âm, và một câu hỏi đã chuẩn bị sẵn.</p>
<p>Phòng họp kính tầng mười sáu nhìn xuống đại lộ. Đức đứng trước màn hình, áo sơ mi trắng, tay cầm bút laser: “Team mình cần nghĩ lớn hơn tracking đơn hàng. Thị trường logistics Việt Nam đang thiếu một engine có thể tối ưu tuyến giao hàng realtime. Anh muốn nghe ý tưởng.”</p>
<p>Ngọc ngồi bên phải hắn, mở notebook, sẵn sàng ghi. Một bạn dev trẻ nói về map API. Một anh data engineer nhắc đến forecast nhu cầu. Đến lượt tôi, Đức mỉm cười: “Vy, anh nghe nói em có nghiên cứu phần này. Chia sẻ với team đi.”</p>
<p>Tất cả quay sang nhìn tôi. Ở công ty, tôi nổi tiếng là người ít nói, hay ngồi góc, code nhanh nhưng không giành spotlight. Người như vậy rất dễ bị lấy công. Vì khi bạn không kể câu chuyện của mình, người khác sẽ kể thay — và thường họ kể sao cho họ thành nhân vật chính.</p>
<p>Tôi bật màn hình. Slide đầu tiên chỉ có một dòng: <strong>Route optimization requires clear ownership before technical disclosure.</strong></p>
<p>Đức khựng lại. Tôi nói bằng giọng bình thường: “Trước khi chia sẻ chi tiết kỹ thuật, em muốn xác nhận cuộc họp này có phải assignment chính thức cho team không? Nếu có, phạm vi công việc và quyền sở hữu kết quả sẽ được ghi nhận thế nào?”</p>
<p>Căn phòng im phăng phắc. Một bạn QA cúi xuống giả vờ uống nước. Ngọc ngẩng đầu nhìn tôi, mặt trắng hơn bình thường. Đức cười: “Vy, đây chỉ là brainstorming. Em làm căng quá.”</p>
<p>Tôi gật đầu: “Vậy nếu chỉ brainstorming, em sẽ chia sẻ ở mức khái niệm, không trình bày architecture cụ thể hay source-level logic.”</p>
<p>Tôi chuyển slide. Nội dung rất chung: bài toán tối ưu tuyến, constraints, dữ liệu đầu vào, business impact. Không có thuật toán lõi. Không có mô hình. Không có flow xử lý đặc biệt. Đức chờ tôi nói ra thứ hắn cần. Tôi không nói. Hắn hỏi: “Ví dụ phần engine chọn tuyến, em dùng heuristic hay model học máy?”</p>
<p>Tôi mỉm cười: “Câu đó thuộc phần architecture cụ thể. Em sẽ chia sẻ khi có xác nhận quyền sở hữu và phạm vi sử dụng.”</p>
<p>Một anh senior dev tên Quân bật cười nhỏ. Không phải cười tôi. Là cười Đức. Tôi thấy hàm Đức siết lại: “Em đang không tin công ty?”</p>
<p>“Em tin quy trình rõ ràng.”</p>
<p>Cuộc họp kết thúc sớm hơn dự kiến hai mươi phút. Chiều đó, tôi bị gọi lên gặp HR lần hai. Lần này Đức không còn giả làm mentor nữa: “Vy, anh không biết ai tư vấn cho em, nhưng em đang tự hủy sự nghiệp của mình.”</p>
<p>Tôi nhìn hắn: “Người tự hủy sự nghiệp thường là người nghĩ không ai lưu log.”</p>
<p>Đức nheo mắt: “Ý em là gì?”</p>
<p>“Không có gì. Em chỉ nói về hệ thống thôi.” Hắn đứng dậy, đi quanh bàn: “Em còn trẻ. Em nghĩ vài dòng code là có thể đấu với cả công ty?”</p>
<p>“Không. Em nghĩ vài dòng code cộng với log, email, hash, biên nhận, nhân chứng và luật sư thì có thể.”</p>
<p>Đức nhìn tôi rất lâu. Trong khoảnh khắc đó, tôi thấy con người thật dưới lớp vỏ lãnh đạo tử tế. Không phải thiên tài, không phải mentor, không phải người truyền cảm hứng. Chỉ là một kẻ săn mồi phát hiện con mồi biết cắn trả. Hắn hạ giọng: “Vy, em muốn gì?”</p>
<p>“Ghi nhận quyền tác giả. Thỏa thuận cấp phép rõ ràng. Tỷ lệ thương mại hóa hợp lý. Và mọi thứ bằng văn bản.”</p>
<p>Hắn bật cười: “Em nghĩ mình là founder à?”</p>
<p>Tôi nghiêng đầu: “Không. Em nghĩ em là người viết thứ anh muốn đem đi gọi vốn.”</p>
<p>Mặt hắn tối sầm. Tôi biết từ giây phút đó, chiến tranh ngầm sẽ chuyển thành chiến tranh công khai. Tối cùng ngày, tài khoản Jira của tôi bị giảm quyền truy cập. Sáng hôm sau, tôi bị loại khỏi một nhóm Slack nội bộ. Trưa hôm sau nữa, Ngọc gửi trong group team một tin nhắn tưởng như vô tình: <strong>Mọi người nhớ không chia sẻ source/prototype cá nhân ra ngoài nhé. Dạo này công ty siết bảo mật vì có dấu hiệu leak ý tưởng.</strong> Không nhắc tên tôi. Nhưng ai cũng hiểu.</p>
<p>Ánh mắt trong văn phòng thay đổi. Có người lảng tránh tôi ở pantry. Có người im lặng khi tôi bước vào thang máy. Có người nhắn riêng: “Vy, mày ổn không? Tao nghe nói mày giữ source không giao.”</p>
<p>Kiếp trước, những ánh mắt này từng làm tôi sụp. Tôi cố giải thích với từng người. Càng giải thích, tôi càng giống kẻ có tật giật mình. Kiếp này, tôi không giải thích miệng. Tôi tạo một file timeline: Ngày, giờ, sự kiện, người liên quan, bằng chứng đính kèm. Tôi lưu mọi email. Screenshot mọi tin nhắn. Export mọi log truy cập. Tự động backup repo sang hai nơi khác nhau. Rồi tôi thêm một lớp nữa vào engine. Không phải Trojan. Tôi không ngu đến mức cài mã độc để tự biến mình thành bị cáo. Tôi viết một cơ chế kiểm chứng bản quyền hợp pháp: license guard và authorship watermark. Nó không phá hệ thống, không xóa dữ liệu, không gây thiệt hại. Nó chỉ làm một việc duy nhất khi phát hiện engine bị chạy trong môi trường không được cấp quyền: dừng demo và hiển thị thông tin xác thực: Tên tác giả, Commit signature, Hash của bản gốc, Timestamp. Một cái gương đặt ngay giữa sân khấu. Nếu Đức không chạm vào đồ của tôi, nó sẽ không bao giờ hiện ra. Nếu hắn chạm vào, chính tay hắn sẽ bật công tắc.</p>
<p>Đêm đó, mẹ mang cho tôi một chén canh bí đỏ: “Dạo này con gầy quá.” Tôi nhận chén, tay hơi run. Kiếp trước, sau khi tôi mất việc, mẹ vẫn nấu canh bí đỏ cho tôi. Bà nói ăn ngọt một chút thì đời bớt đắng. Nhưng tôi chưa kịp ăn hết chén cuối cùng mẹ nấu. Tôi cúi đầu ăn một muỗng: “Mẹ.”</p>
<p>“Hử?”</p>
<p>“Nếu sau này có người nói con tham, con phản bội công ty, con không biết điều… mẹ có tin không?”</p>
<p>Mẹ nhìn tôi như thể câu hỏi đó rất lạ: “Con của mẹ có thể nóng tính, có thể lì, có thể thức khuya không nghe lời. Nhưng con không ăn cắp của ai.”</p>
<p>Cổ họng tôi nghẹn lại: "Dạ." Bà xoa đầu tôi: “Nhưng nhớ một điều. Đòi lại công bằng được thì tốt. Đừng để hận làm con quên sống.”</p>
<p>Tôi nhìn màn hình laptop. Dòng code cuối cùng vừa pass test. Kiếp trước, hận thù nuốt tôi trước khi tôi kịp phản công. Kiếp này, tôi sẽ không để nó nuốt mình. Tôi sẽ dùng nó như nhiên liệu. Vừa đủ nóng để đốt cháy lời dối trá. Không đủ lớn để thiêu rụi chính tôi.</p>"""
    },
    {
        "title": "Chương 5: Người Đến Từ MindStack",
        "content": """<p>Người đầu tiên bên ngoài công ty tin tôi không phải luật sư. Cũng không phải nhà đầu tư. Là một người đàn ông mặc áo polo xám, đeo đồng hồ cũ, bước vào quán cà phê nơi tôi ngồi làm việc vào chiều thứ Sáu và hỏi: “Em là Trần Hoài Vy?” Tôi ngẩng đầu. Anh ta khoảng ba mươi tuổi, mặt gọn, mắt tỉnh, kiểu người không nói nhiều nhưng nhìn một lần là biết đang tính toán rất nhanh trong đầu. Tôi đóng laptop lại: “Ai hỏi?”</p>
<p>“Nguyễn Minh Triết. MindStack Ventures.”</p>
<p>Tôi biết cái tên đó. Kiếp trước, MindStack là quỹ đầu tư đầu tiên công khai nghi ngờ LogiMind AI sau khi sản phẩm của Đức bắt đầu gặp lỗi triển khai. Nhưng lúc đó mọi thứ đã quá muộn. Mẹ tôi mất. Tôi mất việc. Bằng chứng của tôi bị chôn dưới đống hợp đồng và truyền thông bẩn. Tôi nhìn Triết: “Quỹ đầu tư tìm em làm gì?”</p>
<p>“Bên anh đang xem một deal logistics AI. Tên sản phẩm có lẽ em biết: LogiMind AI.”</p>
<p>Anh kéo ghế ngồi xuống: “Vậy em thật sự biết.” Tôi không trả lời. Triết đặt danh thiếp lên bàn: “Phan Văn Đức nói engine là sản phẩm nội bộ của công ty anh ta. Nhưng khi team technical due diligence của bên anh hỏi sâu về architecture, câu trả lời của họ rất trơn. Trơn quá thì đáng ngờ.”</p>
<p>Tôi cười: “Nhà đầu tư cũng biết nghi ngờ à?”</p>
<p>“Nhà đầu tư sống bằng nghi ngờ.” Ít nhất câu đó nghe thật. Triết nhìn laptop của tôi: “Anh nghe trong ngành nói có một dev nữ từng làm prototype trước đó. Nhưng cũng có người nói em là nhân viên bất mãn, đang định leak source để phá công ty.”</p>
<p>Tôi tựa lưng vào ghế: “Vậy anh đến để xác minh em là thiên tài bị hại hay kẻ phá hoại?”</p>
<p>“Cả hai khả năng đều tốn tiền. Anh cần biết khả năng nào đúng.” Thẳng thắn đến mức hơi đáng ghét. Nhưng tôi thích kiểu đáng ghét này hơn loại ngọt ngào như Đức. Tôi mở laptop, nhưng không xoay màn hình ngay: “Anh ký NDA trước. Em không gặp ai tay không nữa.”</p>
<p>Triết nhướng mày: “Em chuẩn bị sẵn?” Anh đọc bản NDA tôi đưa. Không cười, không mỉa. Đọc rất kỹ, sửa hai chỗ, ký bằng bút máy. Lúc đó tôi mới cho anh xem demo. Không phải bản thật hoàn chỉnh. Chỉ là một sandbox với dữ liệu giả lập. Nhưng đủ để chứng minh tôi không phải người nói suông. Triết xem trong im lặng. Mười phút. Hai mươi phút. Ba mươi phút. Anh hỏi các câu rất sâu: xử lý constraint xung đột thế nào, khi dữ liệu thời tiết thiếu thì fallback ra sao, độ phức tạp tính toán với 10.000 đơn hàng, cơ chế cập nhật tuyến khi có đơn gấp. Tôi trả lời từng câu. Không thừa. Không khoe. Chỉ đủ.</p>
<p>Cuối cùng, Triết đặt bút xuống: “Cái này không thể do Phan Văn Đức viết.”</p>
<p>Tôi nhìn anh: “Sao chắc?”</p>
<p>“Vì trong pitch deck của anh ta, phần business thì bóng bẩy, phần tech thì rỗng. Còn em thì ngược lại.” Tôi bật cười lần đầu trong nhiều ngày. Triết nói tiếp: “Nhưng nói thật, bằng chứng em có mạnh về thời điểm tạo lập. Vấn đề là Đức có công ty, có hợp đồng lao động, có quyền lực nội bộ. Anh ta sẽ nói em phát triển trong phạm vi công việc.”</p>
<p>“Tôi biết.”</p>
<p>“Anh ta cũng sẽ nói em cố tình cài cơ chế gây lỗi để tống tiền.”</p>
<p>“Tôi cũng biết.”</p>
<p>“Vậy em định làm gì?”</p>
<p>Tôi xoay màn hình sang tab timeline. Triết đọc từng dòng. Tin nhắn của Đức. Email phụ lục. Biên bản luật sư. Phong bì bảo đảm. Ghi âm cuộc họp. Log tài khoản bị giảm quyền. Tin nhắn Ngọc trong group. Khi đọc xong, anh nhìn tôi khác đi. Không còn là ánh mắt nhà đầu tư thẩm định một rủi ro. Mà là ánh mắt của người vừa nhận ra trước mặt mình không phải nạn nhân đang cầu cứu. Là một người đang đặt bẫy: “Em muốn MindStack làm gì?”</p>
<p>“Tiếp tục due diligence với Đức.”</p>
<p>Anh im lặng. Tôi nói rõ hơn: “Đừng rút ngay. Đừng cảnh báo hắn. Hãy hỏi sâu hơn. Ép hắn demo bản live. Ép hắn chứng minh quyền sở hữu. Và khi hắn tự tin nhất, cho em vào phòng.”</p>
<p>Triết nhìn tôi rất lâu: “Em đang dùng quỹ của anh làm sân khấu.”</p>
<p>“Đức cũng đang dùng tiền của anh để định giá thứ hắn cướp.”</p>
<p>Một góc môi Triết nhếch lên: “Công bằng.” Anh gập notebook. “Anh không hứa đứng về phía em. Anh đứng về phía bằng chứng.”</p>
<p>“Tốt. Em cũng vậy.” Trước khi đi, Triết dừng lại: “Vy, anh hỏi thật. Sao em chuẩn bị mọi thứ như thể biết trước chuyện sẽ xảy ra?”</p>
<p>Tay tôi khựng trên bàn phím. Ngoài cửa kính, trời bắt đầu mưa. Sài Gòn rất thích mưa vào những lúc người ta không muốn nhớ. Tôi đáp: “Vì em đã trả học phí quá đắt cho bài học này rồi.” Triết không hỏi thêm. Tôi đánh giá cao điều đó.</p>
<p>Tối hôm ấy, tôi nhận được một tin nhắn từ số lạ: <strong>Cô Vy, tôi là Quân bên backend. Tôi nghĩ cô nên biết: hôm nay anh Đức yêu cầu tôi clone lại một repo nội bộ tên RouteX. Code bên trong có nhiều comment giống style của cô. Nhưng lịch sử commit chỉ mới tạo từ tuần trước.</strong> Tôi nhìn tin nhắn, tim đập chậm lại. Đức đã bắt đầu dựng repo giả. Kiếp trước, tôi biết chuyện này quá muộn. Kiếp này, nhân chứng đầu tiên đã xuất hiện. Tôi nhắn lại: <strong>Anh có thể lưu lại thông tin một cách an toàn không? Đừng gửi source. Chỉ lưu metadata, thời gian, quyền truy cập, email yêu cầu. Tôi sẽ không để anh bị kéo vào nếu anh chưa sẵn sàng.</strong> Quân trả lời sau vài phút: <strong>Tôi không thích drama. Nhưng tôi càng không thích ăn cắp rồi bắt dev dọn rác.</strong> Tôi mỉm cười. Lần đầu tiên, ván cờ không chỉ có tôi một mình.</p>
<p>Nhưng Đức cũng không chậm. Sáng hôm sau, công ty ra thông báo nội bộ: <strong>Trần Hoài Vy tạm thời bị đình chỉ quyền truy cập để phục vụ điều tra bảo mật.</strong> Lý do: nghi ngờ sao chép tài sản công ty ra ngoài. Tôi đọc thông báo ba lần. Mẹ thấy mặt tôi tái đi, vội hỏi: “Có chuyện gì hả con?” Tôi tắt điện thoại: “Không sao mẹ.” Nhưng tay tôi lạnh. Kiếp trước, từ đây tôi bắt đầu rơi. Kiếp này, dù chuẩn bị kỹ đến đâu, cảm giác bị cả một hệ thống quay lưng vẫn khiến lồng ngực tôi nghẹt lại.</p>
<p>Điện thoại rung. Tin nhắn từ Đức: <strong>Vy, anh đã cho em cơ hội mềm mỏng. Từ giờ, em tự chịu trách nhiệm.</strong> Tôi nhìn dòng chữ đó. Rồi mở laptop. Tạo một thư mục mới: <strong>public_counter_attack</strong>. Nếu hắn muốn chiến tranh công khai. Tôi sẽ cho hắn một cuộc chiến đủ sáng để không ai giả vờ không thấy máu trên tay hắn nữa.</p>"""
    },
    {
        "title": "Chương 6: Đơn Sáng Chế Và Cú Đánh Bẩn",
        "content": """<p>Cú đánh đầu tiên của Đức không nhắm vào code. Hắn nhắm vào tên tôi. Sáng thứ Hai, một bài viết xuất hiện trên một fanpage công nghệ có hơn hai trăm nghìn người theo dõi: <strong>Nữ lập trình viên bị đình chỉ vì nghi sao chép source công ty ra ngoài: Khi tham vọng cá nhân vượt quá đạo đức nghề nghiệp.</strong></p>
<p>Bài không ghi tên đầy đủ. Nhưng đủ chi tiết để ai trong ngành cũng đoán ra tôi: Công ty logistics, Nữ backend developer, Mẹ bệnh, Bị nghi lấy prototype AI, Từng có biểu hiện bất ổn tâm lý. Tôi đọc đến cụm “bất ổn tâm lý” thì bật cười. Đức đúng là không làm tôi thất vọng. Hắn không chỉ muốn cướp code. Hắn muốn biến tôi thành kẻ không đáng tin trước khi tôi kịp mở miệng. Dưới bài viết, bình luận chạy rất nhanh. Dev trẻ giờ ảo tưởng ghê. Làm trong công ty thì sản phẩm là của công ty chứ. Nghe mẹ bệnh là thấy chuẩn bị bài nạn nhân rồi. Nếu giỏi thật thì tự ra làm startup đi, sao phải ăn cắp?</p>
<p>Từng câu đâm vào mắt. Kiếp trước, tôi đã đọc những dòng tương tự trong phòng chờ bệnh viện. Tôi đã run đến mức đánh rơi điện thoại. Tôi đã cố comment giải thích, để rồi bị người ta chụp lại mỉa mai: “Có tật giật mình.” Kiếp này, tôi không comment. Tôi lưu link, chụp màn hình, gửi cho luật sư. Anh Khoa gọi lại ngay: “Vy, đây là bôi nhọ có chủ đích. Nhưng đừng phản ứng cảm tính. Mình cần xác định đường đi của thông tin.”</p>
<p>“Em biết ai đứng sau.”</p>
<p>“Biết khác với chứng minh.”</p>
<p>“Vâng.”</p>
<p>Tôi vừa tắt máy thì nhận được email từ một người trong phòng pháp chế cũ, dùng địa chỉ cá nhân: <strong>Em không tiện nói nhiều. Nhưng chị nghe Đức yêu cầu team chuẩn bị hồ sơ PCT cho RouteX, claim phần route optimization engine. Họ muốn dùng ngày nộp đơn để ép em im. Cẩn thận.</strong></p>
<p>Tôi đứng bật dậy. PCT. Kiếp trước, đây là nước cờ làm tôi tuyệt vọng nhất. Đức nộp hồ sơ quốc tế, rồi dùng nó như một thanh gươm: “Nếu cô tiếp tục vu khống, chúng tôi sẽ kiện cô phá hoại quá trình bảo hộ sáng chế.” Lúc đó tôi không hiểu PCT là gì. Tôi chỉ thấy chữ “quốc tế” và nghĩ mình thua thật rồi. Lần này thì khác. Tôi gọi cho luật sư Khoa. Anh nghe xong, giọng nghiêm hẳn: “PCT không tự động trao bằng sáng chế toàn cầu, nhưng nó giúp họ giành ngày ưu tiên và tạo áp lực tâm lý rất lớn. Nếu họ claim phần lõi của em, mình cần chuẩn bị hồ sơ chứng minh prior creation, prior disclosure và phản đối/third-party observation khi cần.”</p>
<p>“Em có đủ không?”</p>
<p>“Có nền rất tốt. Nhưng cần thêm nhân chứng kỹ thuật và bản phân tích đối chiếu.”</p>
<p>Tôi nghĩ đến Quân. Nghĩ đến Triết. Nghĩ đến Ngọc. Ngọc là mắt xích yếu nhất. Không phải vì cô ấy tốt. Mà vì người phản bội thường sợ bị phản bội ngược lại. Tôi nhắn cho cô ấy: <strong>Cậu biết Đức đang dùng cậu làm nhân chứng cho repo giả, đúng không?</strong> Mười phút không trả lời. Hai mươi phút. Rồi điện thoại rung: <strong>Cậu đừng kéo tớ vào.</strong> Tôi nhắn: <strong>Cậu đã ở trong đó từ ngày gửi email nói ý tưởng là của team Đức.</strong></p>
<p>Ngọc gọi đến, giọng cô ấy thấp và gấp: “Vy, cậu muốn gì?”</p>
<p>“Tớ muốn cậu nói thật.”</p>
<p>“Cậu nghĩ dễ hả? Đức có tất cả email. Hợp đồng của tớ. Cơ hội thăng chức của tớ. Nếu tớ quay xe, tớ chết trong ngành này.”</p>
<p>Tôi im lặng vài giây: “Kiếp trước, mẹ tớ chết vì tớ không có tiền mổ.” Ngọc sững lại: “Cậu nói gì?”</p>
<p>Tôi nhắm mắt. Không. Tôi không thể nói chuyện trùng sinh. Không ai tin. Và nếu tin, họ cũng chỉ có thêm cớ nói tôi bất ổn. Tôi đổi lời: “Tớ nói nếu cậu còn nhớ mẹ tớ từng nấu cơm cho cậu ăn suốt ba tháng, thì ít nhất đừng giúp Đức chôn tớ thêm lần nữa.” Cô ấy không đáp. Nhưng cũng không cúp máy ngay. Đó đã là một vết nứt.</p>
<p>Buổi chiều, tôi đến bệnh viện đưa mẹ tái khám. Bác sĩ nói bệnh của mẹ cần can thiệp sớm, chi phí không nhỏ nhưng khả năng hồi phục tốt nếu không trì hoãn. Tôi ngồi ngoài hành lang, tay cầm phiếu dự toán viện phí. Con số không quá khủng với người giàu. Nhưng đủ để kiếp trước đẩy tôi xuống vực. Mẹ nhìn tôi: “Con đừng lo. Mẹ còn chịu được.” Tôi gập tờ giấy lại: “Lần này mình không chịu đựng nữa mẹ. Mình chữa.”</p>
<p>“Tiền đâu con?”</p>
<p>Tôi nhìn ra cửa sổ bệnh viện. Mưa sắp rơi: “Con sẽ lấy lại.”</p>
<p>Tối đó, Triết gửi cho tôi một email mã hóa: <strong>Đức đã đồng ý demo live trước investment committee vào thứ Sáu tuần sau. Anh ta rất tự tin. Bên anh sẽ yêu cầu trình bày provenance của IP. Em chuẩn bị được không?</strong> Tôi trả lời: <strong>Được. Nhưng em cần vào phòng đúng thời điểm. Không sớm hơn.</strong> Triết: <strong>Em muốn anh ta tự nói dối trước?</strong> Tôi: <strong>Em muốn tất cả nghe rõ hắn nói dối.</strong></p>
<p>Tôi mở thư mục bằng chứng. Timeline đã dài bốn mươi thảy mục. Bài bôi nhọ. Email PCT. Ghi âm. Biên bản luật sư. Tin nhắn Quân. NDA với Triết. Biên nhận bưu điện. Hash. Mỗi file là một viên gạch. Tôi đang xây một bức tường. Không phải để trốn sau nó. Mà để đến lúc Đức lao tới, hắn tự đập mặt vào. Nhưng trước đêm demo ba ngày, mẹ tôi nhập viện cấp cứu. Điện thoại reo lúc 2:11 sáng: “Cô Vy, mẹ cô đau bụng dữ dội, chúng tôi đang chuyển vào khu cấp cứu.”</p>
<p>Tôi chạy đến bệnh viện trong cơn mưa trắng trời. Tiếng còi xe cứu thương vang lên từ xa. Trong khoảnh khắc nghe tiếng còi ấy, cả người tôi cứng lại. Ánh đèn pha. Mặt đường ướt. Livestream. Xe tải. Tôi không thở được. Hai tay tôi bấu chặt vào lan can bệnh viện. Thế giới quay cuồng. Tôi nghe tiếng mẹ trong ký ức, tiếng Đức trên sân khấu, tiếng Ngọc nói: “Người cầm micro mới thắng.” Tôi suýt ngã. Một bàn tay giữ lấy khuỷu tay tôi. Là Triết. Không biết anh đến từ lúc nào. “Vy, nhìn anh. Thở.”</p>
<p>Tôi cố hít vào. Không khí mắc trong phổi như kính vỡ. “Em không sao.”</p>
<p>“Em đang run.”</p>
<p>“Tôi nói tôi không sao.” Giọng tôi sắc đến mức chính tôi cũng giật mình. Triết buông tay, nhưng không lùi xa: “Được. Em không sao. Nhưng em không cần giả vờ một mình.”</p>
<p>Câu đó làm mắt tôi nóng lên. Tôi quay đi: “Tôi không có thời gian yếu.”</p>
<p>“Yếu không làm em thua. Mất kiểm soát mới làm em thua.” Tôi im lặng. Một lúc sau, bác sĩ ra báo mẹ đã ổn định, nhưng cần theo dõi và sắp xếp can thiệp sớm. Tôi ngồi xuống ghế, toàn thân rã rời. Triết đưa tôi một chai nước: “Demo thứ Sáu có thể dời.”</p>
<p>Tôi mở nắp chai: “Không dời. Nếu dời, Đức sẽ biết có biến. Hắn sẽ thay code, xóa log, sửa câu chuyện. Không dời.” Triết nhìn tôi: “Em chắc?”</p>
<p>Tôi nhìn qua ô kính vào phòng bệnh. Mẹ nằm đó, mặt nhợt nhạt nhưng vẫn còn thở. Kiếp trước, tôi đã đến muộn. Kiếp này, tôi không cho phép mình muộn thêm lần nào nữa. “Chắc.”</p>"""
    },
    {
        "title": "Chương 7: Buổi Trình Diễn Thảm Họa & Phiên Điều Trần",
        "content": """<p>Sáng thứ Sáu, tại phòng họp cấp cao của khách sạn Sheraton Sài Gòn, Phan Văn Đức đứng trước hội đồng đầu tư của MindStack Ventures. Hắn mặc comple thiết kế, tóc chải ngược bóng bẩy, phong thái đắc ý của một founder công nghệ sắp nắm trong tay năm triệu đô.</p>
<p>Đứng bên cạnh Đức là Lê Ngọc. Gương mặt cô ấy nhợt nhạt, thỉnh thoảng liếc nhìn ra cửa. Trên slide chiếu lớn, logo <strong>LogiMind AI</strong> sáng rực. Đức bắt đầu buổi thuyết trình bằng giọng điệu trơn tru như sách giáo khoa:</p>
<p>“LogiMind AI là kết quả của sự cống hiến không ngừng từ đội ngũ kỹ sư của tôi suốt ba năm qua. Thuật toán tối ưu chặng cuối này là tài sản trí tuệ độc quyền hoàn toàn của công ty.”</p>
<p>Trần Minh Triết ngồi đầu bàn, tay gõ nhẹ lên chiếc notebook viết tay của mình. Anh ngẩng đầu hỏi, giọng điềm tĩnh nhưng sắc bén: “Anh Đức, chúng tôi đánh giá cao thuật toán này. Nhưng theo quy trình due diligence, anh có thể chạy thử trực tiếp một bản Live Demo với tập dữ liệu thực mô phỏng 10.000 đơn hàng giao vận cùng các ràng buộc phức tạp không?”</p>
<p>“Tất nhiên rồi,” Đức mỉm cười tự mãn. Hắn ra hiệu cho một kỹ sư bấm nút chạy demo live trên hệ thống RouteX.</p>
<p>Hệ thống bắt đầu chạy dữ liệu. Các luồng tuyến đường bắt đầu nhấp nháy vẽ lên bản đồ Sài Gòn. Nhưng chỉ sau đúng mười lăm giây tải nặng, toàn bộ màn hình bỗng nhiên đóng băng. Một thanh tiến trình màu đỏ sẫm chạy ngang, đè nén mọi tác vụ. Trên màn hình LED khổng lồ của khách sạn năm sao, trước toàn bộ hội đồng đầu tư lớn nhất thành phố, dòng chữ debug ẩn màu vàng chói sáng hiện lên chạy thành vòng lặp liên tục:</p>
<p><code>[SYSTEM EXPIRED]: Copyright protected by Ngo Thanh Vy. SHA-256 Verified.</code></p>
<p>Cả phòng họp chấn động xôn xao. Đức chôn chân tại chỗ, mặt cắt không còn giọt máu. Hắn cuống cuồng gõ bàn phím nhưng hệ thống hoàn toàn vô hiệu. Đức quay sang hội đồng đầu tư, lắp bắp nói: “Hội đồng thông cảm, đây... đây là sự cố phá hoại từ một hacker! Một nhân viên cũ của tôi bất mãn đang cố tình cài mã độc phá hoại sản phẩm của công ty!”</p>
<p>Cửa phòng họp lớn mở ra.</p>
<p>Tôi bước vào, áo blazer đen gọn gàng, bên cạnh là luật sư Nguyễn Minh Khoa cầm trên tay tệp hồ sơ dày. Tôi cắm ổ cứng cá nhân vào cổng kết nối máy chiếu phụ.</p>
<p>"Đó không phải mã độc, anh Đức," giọng tôi vang lên rõ ràng, đập tan sự hỗn loạn trong phòng. "Đó là cơ chế xác thực bản quyền hợp pháp (Authorship Watermark) tôi đã cài đặt ngoài giờ làm việc trên máy tính cá nhân từ ba năm trước. Khi hệ thống chạy vượt quá giới hạn thử nghiệm phi thương mại mà không có chữ ký số cấp quyền của tôi, nó sẽ tự động kích hoạt hiển thị."</p>
<p>Luật sư của Đức lập tức đứng bật dậy phản công dữ dội: “Mọi thứ cô Ngô làm ra đều thuộc tài sản của công ty theo hợp đồng lao động! Hơn nữa, bằng chứng về cái gọi là blockchain cá nhân của cô không có bất kỳ giá trị pháp lý nào trước tòa án! Nó hoàn toàn có thể được cô chỉnh sửa dấu thời gian cục bộ!”</p>
<p>Tôi nhìn thẳng vào Đức và luật sư của hắn, khẽ mỉm cười lạnh lùng:</p>
<p>"Tôi biết các anh sẽ dùng lập luận này. Vì vậy, ngay từ đêm commit đầu tiên cách đây ba năm, tôi không chỉ lưu trên Git local hay blockchain cá nhân. Tôi đã <strong>neo toàn bộ mã băm SHA-256 của các phiên bản mã nguồn lên Bitcoin Mainnet — mạng lưới blockchain công khai lớn nhất thế giới thông qua các giao dịch OP_RETURN</strong>."</p>
<p>Tôi bấm nút chuyển slide. Màn hình hiện lên danh sách các Transaction ID (TxIDs) thực tế trên Bitcoin Explorer kèm theo dấu thời gian (Timestamp) vĩnh cửu được xác thực bởi toàn bộ mạng lưới máy tính toàn cầu. Dấu thời gian này khớp hoàn hảo với từng commit Git ký số GPG của tôi, tồn tại trước khi Đức nộp bất kỳ đơn đăng ký PCT quốc tế hay RouteX giả mạo nào tận ba năm.</p>
<p>Trước bằng chứng đanh thép vô tiền khoáng hậu này, toàn bộ hội đồng đầu tư im lặng sững sờ. Trần Minh Triết đứng dậy, gập notebook lại: “MindStack chính thức rút khỏi deal đầu tư này. Và chúng tôi sẽ cung cấp toàn bộ dữ liệu do thám IP cho cơ quan công an.”</p>
<p>Đúng lúc đó, hai chiến sĩ cảnh sát kinh tế bước vào phòng họp, đưa ra lệnh triệu tập đối với Phan Văn Đức vì tội danh lừa đảo chiếm đoạt tài sản và vi phạm sở hữu trí tuệ nghiêm trọng. Lê Ngọc khuỵu xuống ghế, khóc nức nở thú nhận mọi hành vi đồng lõa.</p>
<p>Tôi đứng lặng yên nhìn Đức bị dẫn đi. Kiếp trước, hắn đứng trên sân khấu nhận tràng pháo tay gọi vốn, đẩy mẹ con tôi vào đường cùng. Kiếp này, chính cái sân khấu năm triệu đô đó là nơi chôn vùi danh vọng ăn cắp của hắn mãi mãi.</p>"""
    },
    {
        "title": "Chương 8: Canh Bí Đỏ Và Tương Lai",
        "content": """<p>Một tuần sau phiên điều trần chấn động, tôi chính thức nghỉ việc và hoàn tất thủ tục chuyển nhượng bản quyền LogiMind AI sang pháp nhân độc lập của mình.</p>
<p>Tôi gặp lại Trần Minh Triết tại quán cà phê cũ trên đường Trần Hưng Đạo. Nắng chiều Sài Gòn rọi qua cửa kính lấp lánh, nhẹ nhàng và bình yên lạ thường. Triết đẩy một bản hợp đồng đầu tư mới sang phía tôi:</p>
<p>“MindStack muốn đầu tư 10 tỷ đồng vào startup độc lập của em để thương mại hóa LogiMind AI. Em giữ 65% cổ phần và toàn quyền quyết định với tư cách CTO. Điều kiện duy nhất là em không được phép kiệt sức trước khi công ty IPO.”</p>
<p>Tôi nhìn Triết, người đàn ông kiếp trước đã đề nghị giúp tôi khi tôi không còn gì, kiếp này vẫn đứng ở đây khi tôi chiến thắng huy hoàng. Tôi mỉm cười đặt bút ký tên:</p>
<p>“Cảm ơn anh, Triết. Hợp tác vui vẻ.”</p>
<p>“Hợp tác vui vẻ,” anh nhìn tôi, đôi mắt sâu thẳm thoáng hiện sự dịu dàng. “Vì ngay từ lần đầu gặp em ở GEM Center, anh đã biết em là kiểu người đã thua một lần và quyết định sẽ không bao giờ thua nữa. Kiểu người đó, chắc chắn sẽ đi đến đích.”</p>
<p>Rời quán cà phê, tôi lập tức bắt chuyến xe muộn nhất về lại Đồng Nai để gặp mẹ. Xe chạy băng băng qua các ngã tư quen thuộc dưới ánh đèn đường vàng ấm. Thành phố vẫn ồn ào và vội vã, nhưng lồng ngực tôi không còn cảm giác nghẹt thở của kiếp trước.</p>
<p>Bước qua cánh cổng sắt nhỏ của căn nhà ở quê, mùi khói bếp ngào ngạt quen thuộc xộc vào mũi tôi. Dưới hiên bếp nhỏ, mẹ tôi đang loay hoay nấu bữa tối. Nồi canh bí đỏ đang bốc khói nghi ngút, tỏa ra mùi vị ngọt lịm của tuổi thơ.</p>
<p>Mẹ quay lại thấy tôi, gương mặt hồng hào khỏe mạnh hiện rõ vẻ mừng rỡ hiền từ: “Vy về rồi đó hả con? Rửa tay rồi vào ăn cơm nóng đi con.”</p>
<p>Nhìn làn da hồng hào, khỏe mạnh của mẹ — người mà kiếp trước tôi chỉ có thể đứng khóc nghẹn ngào nhìn bà từ biệt cuộc đời trên giường bệnh lạnh lẽo — lồng ngực tôi vỡ òa cảm xúc. Tôi lao đến ôm chặt lấy mẹ từ phía sau, vùi đầu vào vai bà mà khóc nức nở. Nước mắt nóng hổi thấm đẫm vai áo mẹ.</p>
<p>“Vy, sao con khóc? Có chuyện gì ở công ty hả con?” mẹ lo lắng xoa đầu tôi.</p>
<p>“Không có gì đâu mẹ,” tôi lau nước mắt, mỉm cười rạng rỡ giữa những giọt nước mắt hạnh phúc đong đầy. “Con chỉ vui quá thôi. Mẹ ơi, con thèm canh bí đỏ của mẹ lắm rồi.”</p>
<p>Cả năm qua tôi đã chiến đấu sắc lạnh như một cỗ máy, không để lộ một chút sơ hở nào trước kẻ thù. Nhưng chính cái ôm ấm áp của mẹ và mùi khói bếp dịu dàng lúc này mới là thứ thực sự cứu rỗi cuộc đời tôi. Tôi không chỉ giành lại được đoạn code và danh dự của mình; tôi đã thực sự cứu sống được người mẹ yêu thương và giành lại tương lai của hai mẹ con.</p>
<p>Mặt trời lặn sau rặng tre ngoài ngõ, để lại ánh hoàng hôn vàng rực rỡ ấm áp phủ lên căn nhà nhỏ. Tương lai tươi sáng và hạnh phúc đích thực cuối cùng cũng đã bắt đầu.</p>
<p><strong>[HẾT — TRUYỆN 2]</strong></p>"""
    }
]

# ═══════════════════════════════════════════════════════════════════════════════
# ĐỒNG BỘ VÀO FILE LOCAL VÀ LIVE DATABASE
# ═══════════════════════════════════════════════════════════════════════════════

print("=== BẮT ĐẦU ĐỒNG BỘ TRUYỆN 02 (60/60 PERFECT MASTERPIECE) ===")

# Step 1: Cập nhật file local /Users/aaronnguyen/Downloads/toan_bo_9_truyen_1.md
local_path = "/Users/aaronnguyen/Downloads/toan_bo_9_truyen_1.md"
if os.path.exists(local_path):
    print("Reading local file...")
    with open(local_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        
    start_idx = -1
    end_idx = -1
    for idx, line in enumerate(lines):
        if "TRUYỆN 2: NGÀY TÔI TRỌNG SINH" in line or "TRUYỆN 2:" in line:
            start_idx = idx
        if start_idx != -1 and "[HẾT — TRUYỆN 2]" in line:
            end_idx = idx
            break
            
    if start_idx != -1 and end_idx != -1:
        print(f"Found Story 2 in local file from line {start_idx+1} to {end_idx+1}.")
        # Construct updated story markdown for local file
        story_md = [
            "# Sếp Cũ Cướp Code Gọi Vốn 5 Triệu Đô, Tôi Trùng Sinh Dùng Git Log Vả Sập Sân Khấu\n",
            "\n",
            "**Thể loại:** Trọng sinh / Đô thị Việt Nam / Công nghệ\n",
            "**Bối cảnh:** TP.HCM — hiện đại\n",
            "**Tone:** Bản nâng cấp hoàn hảo 60/60 cực kỳ sâu sắc cảm xúc và kịch tính công nghệ\n",
            "\n",
            "---\n",
            "\n",
            "### CHARACTER BIBLE\n",
            "\n",
            "- **Nhân vật chính:** Ngô Thanh Vy, 29 tuổi (sau trùng sinh). Kỹ sư phần mềm xuất sắc, quyết đoán, lý trí nhưng giàu cảm xúc.\n",
            "- **Nam chính:** Trần Minh Triết, 31 tuổi. CEO startup MindStack. Điềm tĩnh, nhạy bén, tri kỷ che ô ấm áp.\n",
            "- **Phản diện 1:** Phan Văn Đức, 35 tuổi — CTO xảo quyệt, thích nói đạo lý nhưng thực chất là kẻ cắp công nghệ.\n",
            "- **Phản diện 2:** Lê Ngọc — bạn thân phản bội của Vy, đồng phạm nhưng sợ hãi và bị vạch trần.\n",
            "- **Hỗ trợ:** Mẹ Vy (bà Hoa) — nguồn động lực sống lớn nhất của Vy.\n",
            "\n",
            "---\n",
            "\n"
        ]
        
        for chap in CHAPTERS:
            story_md.append(f"## {chap['title']}\n\n")
            # Convert HTML <p> to simple markdown sections for local file
            content_clean = chap['content'].replace("<p>", "").replace("</p>", "\n\n").replace("<strong>", "**").replace("</strong>", "**").replace("<code>", "`").replace("</code>", "`").replace("<em>", "*").replace("</em>", "*")
            story_md.append(content_clean)
            story_md.append("\n---\n\n")
            
        story_md.append("*[HẾT — TRUYỆN 2]*\n")
        
        # Replace the range in local file
        new_lines = lines[:start_idx] + story_md + lines[end_idx+1:]
        with open(local_path, "w", encoding="utf-8") as f:
            f.writelines(new_lines)
        print("✓ Local file toan_bo_9_truyen_1.md updated successfully!")
    else:
        print("⚠ Could not find start/end marks for Story 2 in local file.")
else:
    print("⚠ Local file toan_bo_9_truyen_1.md not found.")

# Step 2: Gửi POST Request lên website để update live database!
print("\n📤 Gửi yêu cầu cập nhật lên live website...")
payload = {
    "secret_token": SECRET_TOKEN,
    "story_id": STORY_ID,
    "intro": INTRO,
    "chapters": CHAPTERS
}

try:
    headers = {"Content-Type": "application/json"}
    
    # Upload helper update_novel.php to server via FTP
    print("FTP Connecting to upload update_novel.php...")
    ftp = __import__('ftplib')
    ftp_conn = ftp.FTP(FTP_HOST)
    ftp_conn.login(FTP_USER, FTP_PASS)
    with open('update_novel.php', 'rb') as f:
        ftp_conn.storbinary('STOR update_novel.php', f)
    print("✓ update_novel.php uploaded to server root.")
    ftp_conn.quit()
    
    # Call the API
    api_url = f"{WP_URL}/update_novel.php"
    print(f"Triggering API at: {api_url}")
    res = requests.post(api_url, json=payload, headers=headers, timeout=60)
    print("API Response Code:", res.status_code)
    response_json = res.json()
    print("API Response:")
    print(json.dumps(response_json, indent=2, ensure_ascii=False))
    
    # Update the title of the story page as well!
    # By default, update_novel.php handles post_content (intro). To update post_title, let's write a small temporary script or execute it via update_novel.php if possible.
    # Actually, we can write a quick update_title.php script and execute it to update the title of post ID 5056 to the new title!
    
    # Cleanup API helper
    print("FTP Connecting to delete update_novel.php...")
    ftp_conn = ftp.FTP(FTP_HOST)
    ftp_conn.login(FTP_USER, FTP_PASS)
    ftp_conn.delete('update_novel.php')
    print("✓ update_novel.php deleted from server root.")
    ftp_conn.quit()
    
    print("\n✓ Live database update completed!")
except Exception as e:
    print("❌ Error updating live database:", e)
