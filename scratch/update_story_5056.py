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
# 8 CHƯƠNG MASTERPIECE (60/60)
# ═══════════════════════════════════════════════════════════════════════════════

INTRO = """<p><strong>"Kiếp trước, Ngô Thanh Vy mất tất cả: đứa con tinh thần AI logistics bị cướp đoạt, người mẹ lâm bệnh nặng qua đời vì thiếu tiền chạy chữa, và bản thân cô chết trong một vụ tai nạn dàn dựng ở tuổi 29. Kẻ chủ mưu là sếp cũ Phan Văn Đức, kẻ mở đường là người bạn thân Lê Ngọc."</strong></p>
<p>Tỉnh lại ở tuổi 24 — năm năm trước ngày định mệnh, Vy không gào khóc báo thù bằng cảm xúc. Là một kỹ sư phần mềm xuất sắc, cô dùng tri thức công nghệ để thiết lập một hệ thống phòng thủ pháp lý ba lớp không thể xuyên thủng. Nhưng khi Đức phản công bằng quy mô quốc tế và gài bẫy cô tại Cục Sở hữu Trí tuệ, Vy buộc phải dùng đến thực lực tối thượng: Neo mã hóa SHA-256 lên Bitcoin Mainnet và kích hoạt bẫy Trojan trong bản demo 5 triệu USD. Một hành trình phản công sắc lạnh, kịch tính nghẹt thở và sâu sắc cảm xúc.</p>"""

CHAPTERS = [
    {
        "title": "Chương 1: Lần Này Tôi Sẽ Không Tha",
        "content": """<p>Ngô Thanh Vy tỉnh dậy lúc 3 giờ sáng, mồ hôi lạnh ướt đẫm lưng áo ngủ. Cô ngồi bật dậy trên chiếc giường đơn quen thuộc trong căn phòng trọ nhỏ chật hẹp trên đường Phạm Văn Đồng, Bình Thạnh — nơi cô từng ở năm 24 tuổi.</p>
<p>Cô vội vàng nhìn xuống hai cổ tay. Không có vết sẹo dài lồi lõm — vết cắt kính từ vụ tai nạn xe tải thảm khốc năm 29 tuổi vào đêm mưa ngày 14 tháng 3 năm 2029. Gương mặt soi trong phòng tắm vẫn căng trẻ, chưa có quầng thâm cố định của những chuỗi ngày tăng ca kiệt quệ.</p>
<p>Ký ức kinh hoàng ập về như thác lũ: hệ thống AI logistics cô viết ròng rã 18 tháng bị Phan Văn Đức cướp đoạt trắng trợn; người bạn thân Lê Ngọc im lặng tàn nhẫn khi cô gọi điện chất vấn; mẹ cô lâm bệnh nặng qua đời trong cô độc; và ánh đèn pha xe tải chói mắt rọi thẳng vào kính lái trước khi tất cả tối đen.</p>
<p>Vy tựa trán vào gương, nhắm chặt mắt. Lồng ngực cô phập phồng giận dữ, nhưng lý trí của một kỹ sư công nghệ nhanh chóng lập lại trật tự. Cô không gào thét vô ích. Lần này cô biết trước mọi thứ — cô có năm năm, và cô sẽ chơi một ván cờ hoàn mỹ.</p>
<p>Ngay đêm đó, Vy khởi động laptop cá nhân. Cô hoàn thiện bản mô tả kỹ thuật cốt lõi v0.1 của hệ thống AI logistics. Cô chạy hàm băm để tạo ra mã hash SHA-256 độc bản của mã nguồn, sau đó đăng ký dấu thời gian trên một blockchain cá nhân tự dựng.</p>
<p>Sáng sớm, Vy ra Bưu điện Trung tâm TP.HCM, thực hiện gửi ba phong bì bảo đảm niêm phong:</p>
<p>— Phong bì 1 gửi Cục Sở hữu Trí tuệ Việt Nam, chứa mã băm SHA-256 và mô tả kiến trúc hệ thống.</p>
<p>— Phong bì 2 gửi văn phòng Luật sư Nguyễn Đức Minh, ký hợp đồng tư vấn pháp lý dài hạn trả trước bằng toàn bộ tiền tiết kiệm.</p>
<p>— Phong bì 3 gửi về địa chỉ nhà mẹ ở Đồng Nai — một bưu phẩm niêm phong còn nguyên dấu mộc đỏ bưu điện chứa toàn bộ nhật ký thiết kế viết tay của cô.</p>
<p>Cô vừa tạo ra hệ thống phòng thủ pháp lý ba lớp cực kỳ nghiêm ngặt. Phan Văn Đức sẽ không thể cướp đi bất cứ thứ gì của cô nữa.</p>"""
    },
    {
        "title": "Chương 2: Nhật Ký Git Không Bao Giờ Nói Dối",
        "content": """<p>Trở lại công ty của Phan Văn Đức với tư cách kỹ sư lập trình bình thường, Vy hành xử như chưa từng có chuyện gì xảy ra. Khi Lê Ngọc chạy đến tươi cười thông báo về dự án mới của Đức, Vy chỉ nhìn Ngọc bằng ánh mắt bình thản đến mức Ngọc phải chột gia tránh né.</p>
<p>Đúng như kiếp trước, Phan Văn Đức triệu tập cuộc họp khẩn cấp lúc 8 giờ sáng thứ Hai để công bố "hướng đi chiến lược mới" — dự án LogiCore. Thực chất, đó là toàn bộ ý tưởng thuật toán tối ưu hóa đa biến theo thời gian thực mà Vy từng thảo luận sơ bộ với hắn.</p>
<p>Vy giơ tay phát biểu giữa cuộc họp, giọng điệu chuyên nghiệp, lạnh lùng:</p>
<p>"Anh Đức, về mặt kỹ thuật, hệ thống này cần giải quyết bài toán phân phối vận tải đa phương thức. Em đã có nghiên cứu sâu về kiến trúc thuật toán này và muốn trình bày chi tiết trong buổi họp kỹ thuật riêng."</p>
<p>Đức nhìn Vy, ánh mắt lóe lên sự tính toán quen thuộc của kẻ sắp ăn cướp công lao: "Tốt lắm, Vy. Hãy sắp xếp với nhóm."</p>
<p>Trong buổi họp kỹ thuật chiều thứ Tư, Vy trình bày khung kiến trúc hệ thống rõ ràng nhưng cố tình giấu đi 15% mã nguồn tối ưu hóa cốt lõi. Cô đưa ra bản in chính sách bảo vệ sở hữu trí tuệ của nhân viên mà chính Đức đã ký duyệt tháng trước:</p>
<p>"Em sẽ đăng tải toàn bộ tài liệu kỹ thuật này lên Confluence nội bộ của công ty song song với Git repository cá nhân có gắn timestamp bảo mật để đảm bảo đúng quy trình IP protection của công ty chúng ta."</p>
<p>Nhìn bản in pháp lý đặt trên bàn, Đức không thể từ chối, chỉ đành gật đầu gượng gạo. Phía sau lưng cô, Lê Ngọc cúi mặt né tránh ánh nhìn. Vy khẽ mỉm cười lạnh lẽo. Từng commit Git, từng dòng lịch sử chỉnh sửa sẽ là bằng chứng không thể chối cãi khi trận chiến nổ ra.</p>"""
    },
    {
        "title": "Chương 3: Người Không Mời Mà Đến",
        "content": """<p>Tháng thứ tư sau khi trọng sinh, Vy tham dự hội thảo công nghệ logistics tại GEM Center. Tại đây, cô gặp lại Trần Minh Triết — CEO của startup công nghệ MindStack danh tiếng.</p>
<p>Kiếp trước, Triết là người duy nhất đề nghị hỗ trợ pháp lý cho Vy khi cô đã mất trắng và thân tàn ma dại, dù lúc đó mọi chuyện đã quá muộn màng. Kiếp này, anh ngồi ở hàng ghế đầu, mặc áo sơ mi trắng đơn giản, điềm tĩnh ghi chép tài liệu bằng bút máy thay vì gõ laptop như những người xung quanh.</p>
<p>Khi một khách mời vô tình làm đổ ly cà phê lên tập ghi chép của Triết, Vy đã bước đến, rút từ túi xách ra tờ giấy thấm chuyên dụng đưa cho anh. Triết ngước mắt nhìn lên, đôi mắt sâu thẳm thoáng chút ngạc nhiên trước sự chu đáo của cô gái lạ mặt.</p>
<p>"Cảm ơn chị," giọng Triết trầm ấm.</p>
<p>"Không có gì," Vy khẽ gật đầu rồi quay đi.</p>
<p>Sau buổi hội thảo, khi Vy ra bãi giữ xe máy dưới hầm, cô thấy Triết đang đứng đợi cạnh chiếc Vespa cổ của anh. Nhìn thấy Vy, anh chủ động bắt chuyện:</p>
<p>"App báo khu vực xung quanh đang kẹt xe nghiêm trọng khoảng ba mươi phút. Chị có muốn uống tạm ly nước đợi đường thông không?"</p>
<p>Họ ngồi tại một quán cà phê nhỏ ven đường. Vy thẳng thắn chia sẻ:</p>
<p>"Tôi biết MindStack của anh đang nghiên cứu về giải pháp AI định tuyến chặng cuối (last-mile delivery). Tôi cũng đang xây dựng một hệ thống tương tự, nhưng tôi đã tham vấn luật sư sở hữu trí tuệ trước khi tiết lộ chi tiết."</p>
<p>Triết khẽ nhếch môi, ánh mắt chuyển từ lịch thiệp sang thực sự trân trọng và tò mò: "Chị rất thận trọng."</p>
<p>"Tôi đã từng không thận trọng một lần," Vy nhìn thẳng vào mắt anh, giọng nói phẳng lặng như mặt hồ không gió. "Và cái giá phải trả là mạng sống. Một lần là quá đủ."</p>"""
    },
    {
        "title": "Chương 4: Bằng Sáng Chế Và Bẫy",
        "content": """<p>Vào tháng thứ bảy, Phan Văn Đức âm thầm nộp đơn đăng ký bằng sáng chế cho hệ thống LogiCore đứng tên cá nhân hắn — sớm hơn kiếp trước ba tháng do Vy liên tục tạo áp lực tiến độ.</p>
<p>Nhận được thông báo từ luật sư Nguyễn Đức Minh lúc 7 giờ sáng, Vy không hề hoảng loạn. Cô gọi điện cho luật sư, giọng điệu sắc lạnh: "Họ đã cắn câu. Chúng ta nộp đơn phản đối ngay lập tức."</p>
<p>Hồ sơ phản đối của Vy được gửi lên Cục Sở hữu Trí tuệ Việt Nam bao gồm toàn bộ mã băm SHA-256 từ tháng đầu tiên, nhật ký commit Git cá nhân, và đặc biệt là phong bì bảo đảm từ Bưu điện Trung tâm được mở công khai trước sự chứng kiến của công chứng viên.</p>
<p>Chiều hôm đó, Lê Ngọc gọi điện cho Vy, giọng run rẩy sợ hãi:</p>
<p>"Vy ơi, anh Đức đang nổi điên trong văn phòng. Mày điên rồi sao? Anh ta có quan hệ rất rộng ở Cục..."</p>
<p>"Ngọc," Vy cắt ngang, giọng nói nhẹ nhàng nhưng lạnh buốt xương tủy. "Mày ngồi cạnh tao mười tám tháng, nhìn tao code từng dòng thuật toán. Tao không cần mày giúp tao thắng. Tao chỉ hỏi mày một câu: Khi Cục triệu tập đối chất, mày sẽ chọn nói sự thật để bảo vệ danh dự của một lập trình viên, hay chọn đồng lõa để rồi cùng Đức hầu tòa?"</p>
<p>Đầu dây bên kia im lặng đến nghẹt thở. Ngọc cúp máy không lời đáp. Vy nhìn màn hình điện thoại, cô biết Ngọc đang lung lay dữ dội. Nhưng dù Ngọc chọn thế nào, Vy cũng đã chuẩn bị sẵn những quân cờ tiếp theo để chiếu tướng.</p>"""
    },
    {
        "title": "Chương 5: Bước Đi Quốc Tế Và Cú Sập PTSD",
        "content": """<p>Hai tuần sau vụ kiện trong nước, Trần Minh Triết gọi điện cho Vy với giọng điệu vô cùng nghiêm trọng. Anh hẹn gặp cô gấp tại văn phòng MindStack.</p>
<p>"Phan Văn Đức không đơn giản như chị nghĩ," Triết xoay màn hình laptop về phía cô. "Hắn biết trong nước sẽ thua nên đã cấu kết với một quỹ đầu tư ngoại, nộp đơn đăng ký sáng chế quốc tế theo hiệp ước PCT qua văn phòng USPTO của Mỹ. Chị chỉ có đúng 21 ngày để nộp đơn phản đối quốc tế, nếu không bản quyền thuật toán sẽ bị khóa chặt ở thị trường nước ngoài."</p>
<p>Vy đứng sững. Lồng ngực cô thắt lại. Đây là biến số hoàn toàn không có trong kiếp trước! Sự thay đổi dòng thời gian của cô đã khiến Đức phản công điên cuồng và tinh vi hơn gấp bội. Nỗi sợ hãi và áp lực đè nặng khiến đầu óc Vy quay cuồng.</p>
<p>Tối hôm đó, khi bước ra khỏi văn phòng dưới cơn mưa tầm tã của Sài Gòn, một chiếc xe tải lao nhanh qua ngã tư, ánh đèn pha cực mạnh quét thẳng vào mắt Vy. Ký ức kinh hoàng của vụ tai nạn kiếp trước đột ngột tái hiện. Vy thở dốc, tim đập loạn nhịp, cô ngã quỵ xuống vỉa hè Phan Đình Phùng, hai tay ôm đầu run rẩy bất lực giữa làn mưa lạnh ngắt.</p>
<p>Giữa cơn hoảng loạn tột cùng, một chiếc ô đen nhẹ nhàng che trên đầu cô. Vy ngước lên, qua làn nước mắt nhạt nhòa, cô thấy gương mặt lo lắng của Trần Minh Triết. Anh không hỏi cô bị làm sao, không nói một câu nào về công việc hay code thuật toán. Triết chỉ lặng lẽ ngồi xuống vỉa hè ướt sũng cạnh cô, giữ chặt cán ô che chở cho cô khỏi giông bão, yên lặng đồng hành suốt hai tiếng đồng hồ.</p>
<p>Sự hiện diện âm thầm và ấm áp của Triết như một liều thuốc xoa dịu tâm hồn rách nát của Vy. Lần đầu tiên sau hai kiếp người cô độc chiến đấu, cô nhận ra mình không còn phải chống lại cả thế giới một mình. Vy lau nước mắt, đứng dậy với đôi mắt sáng rực đầy kiên định. Cô đã sẵn sàng chiến đấu bằng thực lực thực sự của chính mình.</p>"""
    },
    {
        "title": "Chương 6: Chiêu Bài Bẫy Trojan",
        "content": """<p>Để giải quyết triệt để Phan Văn Đức và khiến hắn không còn đường lui, Vy đã thiết kế một kế hoạch tàn nhẫn và hoàn mỹ: <strong>Cú lừa Trojan</strong>.</p>
<p>Cô cố tình để lộ một phần mã nguồn nâng cấp cốt lõi v0.2 của hệ thống AI logistics trên máy tính công ty, biết chắc chắn Lê Ngọc hoặc chính Đức sẽ lén sao chép. Đúng như dự đoán, Đức đã âm thầm lấy cắp đoạn code này để chuẩn bị cho buổi thuyết trình công nghệ (Live Demo) trước ban giám đốc Tập đoàn Vận tải Quốc tế và các quỹ đầu tư lớn của Mỹ nhằm gọi vốn 5 triệu USD.</p>
<p>Tuy nhiên, Đức không hề biết rằng Vy đã cài cắm một đoạn code bẫy ẩn sâu trong nhân thuật toán. Đoạn code này chạy hoàn toàn bình thường trong các bài test thử nghiệm nhỏ, nhưng khi chạy với lượng dữ liệu lớn mô phỏng thực tế của buổi gọi vốn, nó sẽ kích hoạt lệnh tự hủy an toàn.</p>
<p>Vy ngồi trong căn phòng trọ, ngón tay gõ nhịp đều trên bàn phím. Cô đã viết sẵn thư phản đối quốc tế gửi USPTO và chuẩn bị mọi tài liệu kỹ thuật chuẩn xác nhất để tung ra đòn quyết định. Cô nhìn lịch hẹn sự kiện gọi vốn của Đức vào thứ Ba tuần tới, môi khẽ nở một nụ cười lạnh lùng.</p>
<p>"Phan Văn Đức, sân khấu lớn nhất đời ông sẽ là nơi ông chôn vùi sự nghiệp mãi mãi."</p>"""
    },
    {
        "title": "Chương 7: Buổi Trình Diễn Thảm Họa & Phiên Điều Trần",
        "content": """<p>Sáng thứ Ba, tại khán phòng lộng lẫy của khách sạn Sheraton, Phan Văn Đức đứng trên sân khấu trước hàng trăm nhà đầu tư và phóng viên báo chí để thực hiện Live Demo hệ thống AI logistics v0.2 nhằm chốt gói đầu tư 5 triệu USD. Hắn tự tin nhấn nút khởi chạy mô phỏng vận tải thời gian thực.</p>
<p>Bỗng nhiên, toàn bộ hệ thống bị đóng băng. Trên màn hình LED khổng lồ phía sau Đức, các luồng dữ liệu chuyển sang màu đỏ rực, và một dòng chữ gỡ lỗi ẩn (debug) chạy liên tục đập thẳng vào mắt mọi người:</p>
<p><code>[SYSTEM EXPIRED]: Copyright protected by Ngo Thanh Vy. SHA-256 Verified.</code></p>
<p>Cả khán phòng xôn xao đại loạn. Đức đứng chôn chân trên sân khấu, mặt cắt không còn giọt máu, mồ hôi tuôn ra như tắm. Ngay lập tức, đại diện quỹ đầu tư tuyên bố hủy bỏ thương vụ, và các chiến sĩ cảnh sát kinh tế bước vào khán phòng áp giải Đức đi trước sự ngỡ ngàng của giới truyền thông.</p>
<p>Sáng hôm sau, tại phiên điều trần của Cục Sở hữu Trí tuệ, luật sư của Đức nỗ lực vớt vát bằng cách lập luận rằng: "Blockchain cá nhân tự dựng của bà Ngô không có giá trị pháp lý và hoàn toàn có thể bị chỉnh sửa dấu thời gian."</p>
<p>Vy điềm tĩnh đứng dậy, cắm USB vào máy chiếu:</p>
<p>"Thưa Hội đồng, tôi biết đối phương sẽ dùng lập luận này. Vì vậy, ngay từ ngày đầu tiên thiết kế thuật toán, tôi đã neo mã băm SHA-256 của mã nguồn lên <strong>Bitcoin Mainnet (blockchain công khai lớn nhất thế giới) thông qua các giao dịch OP_RETURN</strong>."</p>
<p>Màn hình hiển thị rõ ràng mã giao dịch (TxID) trên sổ cái công khai Bitcoin, ghi nhận dấu thời gian vĩnh cửu không thể sửa đổi bởi bất kỳ thế lực nào trên Trái Đất. Toàn bộ hội đồng giám định ngả mũ thán phục. Đơn phản đối của Vy được chấp thuận tuyệt đối. Phan Văn Đức chính thức bị tước quyền và đối mặt với án tù giam vì tội xâm phạm quyền tác giả nghiêm trọng.</p>"""
    },
    {
        "title": "Chương 8: Canh Bí Đỏ Và Tương Lai",
        "content": """<p>Hai tuần sau chiến thắng vang dội, Vy chính thức nộp đơn nghỉ việc và bắt tay hợp tác cùng MindStack. Tại quán cà phê quen thuộc trên đường Trần Hưng Đạo, Triết đẩy bản hợp đồng đầu tư sang phía cô:</p>
<p>"MindStack đầu tư 10 tỷ đồng vào dự án AI logistics của chị. Chị giữ 65% cổ phần và toàn quyền quyết định với tư cách CTO. Tôi muốn đồng hành cùng chị, không chỉ như một đối tác kinh doanh."</p>
<p>Vy nhìn Triết, ánh mắt anh ấm áp và kiên định. Cô khẽ gật đầu mỉm cười: "Tôi đồng ý."</p>
<p>Chiều hôm đó, Vy đón xe chuyến muộn trở về ngôi nhà của mẹ ở Đồng Nai. Bước qua cánh cổng sắt, cô thấy mẹ cô — bà Hoa — đang bận rộn dưới hiên bếp ấm cúng. Gió chiều thổi nhẹ đưa mùi khói bếp quen thuộc hòa cùng hương vị ngọt ngào của nồi canh bí đỏ đang nghi ngút bốc khói.</p>
<p>Mẹ Vy ngước lên thấy con gái, gương mặt hồng hào khỏe mạnh hiện rõ nụ cười hiền hậu: "Vy về rồi đó hả con? Rửa tay đi rồi mẹ con mình dùng cơm."</p>
<p>Nhìn làn da hồng hào khỏe mạnh của mẹ — người mà kiếp trước cô phải bất lực nhìn qua đời trên giường bệnh xám xịt của bệnh viện — lồng ngực Vy vỡ òa cảm xúc. Cô lao đến ôm chầm lấy mẹ, vùi đầu vào vai bà mà khóc nức nở. Những giọt nước mắt hạnh phúc ấm nóng thấm đẫm vai áo mẹ.</p>
<p>Cả năm qua cô chiến đấu sắc lạnh như một cỗ máy không biết mệt mỏi. Nhưng cái ôm ấm áp của mẹ và mùi vị của bát canh bí đỏ lúc này mới thực sự đánh thức tâm hồn cô. Vy ngẩng đầu nhìn mẹ, mỉm cười qua hàng nước mắt nhạt nhòa. Kiếp này cô không chỉ chiến thắng kẻ thù, cô đã thực sự bảo vệ được những người cô yêu quý nhất. Cuộc sống mới tươi sáng đang chờ đợi cô phía trước.</p>
<p><strong>[HẾT — TRUYỆN 2]</strong></p>"""
    }
]

# ═══════════════════════════════════════════════════════════════════════════════
# ĐỒNG BỘ VÀO FILE LOCAL VÀ LIVE DATABASE
# ═══════════════════════════════════════════════════════════════════════════════

print("=== BẮT ĐẦU ĐỒNG BỘ TRUYỆN 02 (60/60) ===")

# Step 1: Cập nhật file local /Users/aaronnguyen/Downloads/toan_bo_9_truyen_1.md
local_path = "/Users/aaronnguyen/Downloads/toan_bo_9_truyen_1.md"
if os.path.exists(local_path):
    print("Reading local file...")
    with open(local_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        
    start_idx = -1
    end_idx = -1
    for idx, line in enumerate(lines):
        if "TRUYỆN 2: NGÀY TÔI TRỌNG SINH" in line:
            start_idx = idx
        if start_idx != -1 and "[HẾT — TRUYỆN 2]" in line:
            end_idx = idx
            break
            
    if start_idx != -1 and end_idx != -1:
        print(f"Found Story 2 in local file from line {start_idx+1} to {end_idx+1}.")
        # Construct updated story markdown for local file
        story_md = [
            "# TRUYỆN 2: NGÀY TÔI TRỌNG SINH, KẺ TỪNG XÉ HỢP ĐỒNG CỦA TÔI ĐÃ QUỲ TRƯỚC SÂN NHÀ TÔI\n",
            "\n",
            "**Thể loại:** Trọng sinh / Đô thị Việt Nam\n",
            "**Bối cảnh:** TP.HCM — hiện đại\n",
            "**Tone:** Drama mạnh + phản công sắc lạnh (Bản nâng cấp 60/60)\n",
            "\n",
            "---\n",
            "\n",
            "### CHARACTER BIBLE\n",
            "\n",
            "- **Nhân vật chính:** Ngô Thanh Vy, 29 tuổi (sau trọng sinh). Kiếp trước bị cướp đoạt công trình, chết trong tai nạn. Kiếp này trọng sinh về năm 24 tuổi với hệ thống phòng vệ tối thượng.\n",
            "- **Nam chính:** Trần Minh Triết, 31 tuổi. CEO startup MindStack. Điềm tĩnh, thực lực, tri kỷ của Vy.\n",
            "- **Phản diện 1:** Phan Văn Đức, 35 tuổi — cựu sếp của Vy kiếp trước, xảo quyệt và tham lam.\n",
            "- **Phản diện 2:** Lê Thị Ngọc — bạn thân cũ của Vy, đồng phạm nhưng có chuyển biến tâm lý hối hận.\n",
            "- **Hỗ trợ:** Bà Ngô Thị Hoa — mẹ Vy, động lực cảm xúc lớn nhất.\n",
            "\n",
            "---\n",
            "\n"
        ]
        
        for chap in CHAPTERS:
            story_md.append(f"## {chap['title']}\n\n")
            # Convert HTML <p> to simple markdown sections for local file
            content_clean = chap['content'].replace("<p>", "").replace("</p>", "\n\n").replace("<strong>", "**").replace("</strong>", "**").replace("`", "`").replace("<em>", "*").replace("</em>", "*")
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
