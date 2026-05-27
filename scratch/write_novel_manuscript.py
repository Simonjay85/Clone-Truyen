# -*- coding: utf-8 -*-
import json
import os

def main():
    novel_data = {
        "title": "Vua Mật Ong Cao Nguyên Đá: Bị Đuổi Khỏi Trang Trại, Tôi Xây Đế Chế Thảo Dược Nghìn Tỷ",
        "author": "Vũ Triệu Đăng",
        "genre": "Sảng Văn",
        "intro": (
            '<p><strong>"Bàn tay bẩn thỉu đầy vết ong đốt của anh không đáng chạm vào chiếc váy cưới Vera Wang trăm triệu của tôi! Kẻ dầm mưa dãi nắng cày cuốc cả đời như anh chỉ cản bước tôi lọt vào giới thượng lưu Hà Thành!"</strong></p>\n'
            '<p>Vị hôn thê Lương Mỹ Hạnh tháo nhẫn đính hôn ném thẳng vào mặt Triệu Hải Đăng ngay giữa ngày anh bị người bạn thân Hoàng Duy Khang vu oan chiếm đoạt vốn và đuổi cổ khỏi trang trại mật ong bạc hà Đồng Văn dưới đêm giông bão tuyết rơi buốt giá của Hà Giang. Chúng cướp đoạt công thức tách nước giữ nguyên enzym mật ong bạc hà tự nhiên cả đời anh nghiên cứu để dâng cho tập đoàn VietHoney hòng niêm yết IPO tỷ đô.</p>\n'
            '<p>Bị tống cổ khỏi cao nguyên đá trong tay trắng, Đăng ngỡ như mất hết tất cả. Nhưng hắn không ngờ, mật ong hữu cơ trong tay anh không phải là thứ "thô sơ lỗi thời", mà là thần dược tối cao! Được Nguyễn Khánh An - nữ chủ tịch sắc lạnh, lý tính của Vạn An Capital chống sau lưng, Đăng lập nên "Đế chế Mật Ong Vạn An", dùng công nghệ truy xuất nguồn gốc số hóa tổ ong, báo cáo kiểm toán Big 4 EY vạch trần đường dây mật ong hóa chất của kẻ phản bội, cùng sắc lệnh điều tra từ C03 Bộ Công an để đẩy chúng xuống vực thẳm.</p>\n'
            '<p><strong>Chúng từng gọi anh là gã nuôi ong đê tiện, cho đến khi cả Triển lãm Nông nghiệp Quốc tế phải cúi đầu run rẩy xin anh chia sẻ một giọt mật ong cứu sống uy tín của cả ngành xuất khẩu Việt Nam!</strong></p>'
        ),
        "chapters": []
    }

    # Chapter 1
    ch1_content = """<p>Gió mùa đông bắc tràn qua vách đá cao nguyên Đồng Văn rít lên từng hồi ghê rợn như tiếng gào thét của loài quái thú cổ xưa. Tuyết rơi lất phất trộn lẫn với những hạt mưa đá lạnh buốt, gõ chan chát vào mái tôn của trang trại nuôi ong công nghệ cao bạc hà Hà Giang.</p>
<p>Triệu Hải Đăng đứng lặng im giữa căn phòng điều khiển trung tâm, đôi bàn tay gầy guộc chằng chịt những vết sẹo do ong đốt rỉ ra những vệt mồ hôi lạnh ngắt dưới ánh đèn neon vàng vọt nhấp nháy. Mắt anh đỏ ngầu, dán chặt vào tờ biên bản kiểm toán tài sản và lệnh trục xuất do chính người bạn thân nối khố Hoàng Duy Khang đặt lên bàn.</p>
<p>“Triệu Hải Đăng, ký đi. Đây là lối thoát duy nhất để mày giữ lại cái mạng quèn của mình,” Khang mở nút chai rượu mạnh cao cấp, hớp một ngụm rồi mỉa mai, đôi mắt sắc lạnh và đầy dối trá.</p>
<p>“Khang! Trang trại mật ong bạc hà hữu cơ này là mồ hôi, là máu của tao ròng rã sáu năm qua! Mày cướp sạch công thức tách nước chân không giữ nguyên enzym tự nhiên của tao, giờ còn muốn tống cổ tao đi dưới đêm tuyết lạnh thế này?” Giọng Đăng nghẹn lại, lồng ngực phập phồng kịch liệt, nhịp tim đập dồn dập đến mức tai anh ù đi.</p>
<p>Đột nhiên, cánh cửa gỗ bật mở. Lương Mỹ Hạnh - vị hôn thê mà anh nâng niu suốt ba năm bước vào, khoác trên mình chiếc áo lông thú đắt tiền, đi bên cạnh là hai gã bảo vệ cao lớn mặc vest đen lạnh lùng.</p>
<p>Cô nhìn anh bằng ánh mắt khinh miệt tột cùng, dứt khoát tháo chiếc nhẫn bạc đính hôn ném thẳng vào vũng nước bùn dưới chân anh: “Bàn tay bẩn thỉu đầy vết ong đốt của anh không đáng chạm vào chiếc váy cưới Vera Wang trăm triệu của tôi! Kẻ dầm mưa dãi nắng cày cuốc cả đời như anh chỉ cản bước tôi lọt vào giới thượng lưu Hà Thành!”</p>
<p>“Mỹ Hạnh... cả cô cũng phản bội tôi?” Đăng lảo đảo lùi lại, va vào chiếc máy ly tâm lạnh ngắt.</p>
<p>“Phản bội? Không, tôi chỉ chọn tương lai sáng lạn hơn,” Mỹ Hạnh cười khẩy đầy kiêu ngạo. “Anh Khang đã đồng ý dùng công thức tách nước của anh để liên doanh với tập đoàn hóa chất thực phẩm đa quốc gia VietHoney, thổi phồng dòng tiền để IPO nghìn tỷ trên sàn chứng khoán. Còn anh? Suốt ngày chỉ biết cắm đầu vào tổ ong, ôm mộng hữu cơ thuần tự nhiên chậm chạp, bảo thủ!”</p>
<p>“Mật ong bạc hà nguyên chất Đồng Văn mà dùng hóa chất tạo hương và đường ngô cao phân tử để sản xuất hàng loạt sẽ biến thành thuốc độc phá hủy uy tín nông sản Việt Nam!” Đăng hét lên trong phẫn nộ.</p>
<p>“Câm mồm!” Duy Khang bước tới đập mạnh tập hồ sơ xuống bàn, chỉ thẳng mặt anh. “Người đại diện pháp luật của trang trại hiện tại là tao, con dấu là do Mỹ Hạnh ký bàn giao. Ký tên khước từ quyền tác giả và cút khỏi Hà Giang ngay lập tức, nếu không tao sẽ báo cảnh sát vu oan cho mày tội phá hoại tài sản công nghệ cao!”</p>
<p>Dưới sự cưỡng ép tàn nhẫn, Đăng nghiến răng nghiến lợi ký tên lên tờ giấy trắng. Anh bị hai gã bảo vệ kéo lê ra khỏi trang trại, ném thẳng chiếc ba lô sờn cũ chứa ổ cứng di động vào bùn tuyết lạnh ngắt.</p>
<p>Đêm đông Hà Giang lạnh buốt xương tủy, Đăng quỳ rạp dưới đất nhặt chiếc ổ cứng lên, nước mưa hòa lẫn nước mắt. Anh nhìn lại trang trại rực rỡ ánh đèn đằng xa, hàm răng cắn chặt đến rỉ máu: “Hoàng Duy Khang! Lương Mỹ Hạnh! Các người cướp đi hoài bão của tôi, biến mật ong bạc hà quý giá thành thứ hóa chất độc hại hại người. Tôi thề... có một ngày tôi sẽ trở lại, bắt các người phải quỳ sụp dưới chân cao nguyên này để đền tội!”</p>"""

    novel_data["chapters"].append({
        "title": "Chương 1: Trục Xuất Dưới Đêm Đông Đồng Văn",
        "content": ch1_content
    })

    # Chapter 2
    ch2_content = """<p>Sáng hôm sau, mưa tuyết đã ngớt nhưng cái lạnh cắt da cắt thịt của cao nguyên đá vẫn bao trùm lấy thị trấn cổ Đồng Văn. Triệu Hải Đăng với chiếc ba lô sờn rách, bước đi vô định bên đèo Mã Pí Lèng, nơi những vách đá dựng đứng cheo leo giữa mây ngàn.</p>
<p>Đột nhiên, một tiếng phanh xe chói tai vang lên từ phía khúc cua hiểm trở. Chiếc xe SUV Mercedes-Benz G63 màu đen bóng loạng khựng lại sát sườn núi. Cửa xe mở ra, một gã tài xế trung niên hốt hoảng kêu cứu: “Có ai không? Cứu mạng! Chủ tịch của tôi lên cơn hen suyễn tắc nghẽn phổi cấp tính rồi, thuốc xịt dự phòng bị rơi xuống vực khi va chạm!”</p>
<p>Đăng lập tức lao tới. Trên băng ghế sau xe, một người đàn ông lớn tuổi mặc âu phục sang trọng đang co quắp, khuôn mặt tím tái không còn giọt máu, hai tay bấu chặt lấy cổ họng thở khò khè, nhịp thở đứt quãng vô cùng nguy kịch. Đó chính là Nguyễn Vạn An - siêu tỷ phú đứng đầu tập đoàn Vạn An Group.</p>
<p>“Tránh ra, để tôi!” Đăng lớn tiếng ra lệnh đầy quyết đoán, mở chiếc ba lô sờn cũ rút ra một chai mật ong bạc hà tự nhiên nguyên chất màu xanh ô-liu nhạt – giọt mật cuối cùng anh mang theo từ trang trại.</p>
<p>Anh nhẹ nhàng nhưng dứt khoát bấm mạnh vào huyệt phế du và thiên đột trên cổ ông cụ để giảm co thắt phổi, đồng thời nhỏ từng giọt mật ong bạc hà nguyên chất đậm đặc enzym tự nhiên vào miệng ông. Mật ong bạc hà hữu cơ Hà Giang chứa hàm lượng chất chống viêm tự nhiên cực cao và enzym quý hiếm lập tức làm dịu lớp niêm mạc phế quản đang sưng tấy.</p>
<p>Chỉ trong ba phút nghẹt thở, tiếng khò khè kinh hoàng dịu đi. Ông cụ hít được một hơi thật sâu, đôi mắt dần có lại thần sắc, da mặt hồng hào trở lại dưới sự kinh ngạc tột cùng của gã tài xế.</p>
<p>Đúng lúc đó, một chiếc chuyên cơ trực thăng đáp xuống bãi đất trống gần đèo Mã Pí Lèng. Nguyễn Khánh An - nữ chủ tịch điều hành sắc lạnh, lý tính của Vạn An Capital bước xuống xe chuyên dụng áp sát hiện trường. Cô sở hữu mái tóc ngắn cá tính, bộ vest công sở sắc sảo cùng đôi mắt thông tuệ lấp lánh như sương lạnh cao nguyên.</p>
<p>“Cha! Cha có sao không?” Khánh An lao tới ôm lấy cha mình, rồi quay sang nhìn Đăng bằng ánh mắt vô cùng cảnh giác và lạnh lùng: “Anh là ai? Anh đã dùng thứ gì cho cha tôi uống?”</p>
<p>“Đây là mật ong bạc hà hữu cơ nguyên chất Đồng Văn,” Đăng bình thản lau vệt mật ong trên tay, đứng dậy đối diện thẳng với cô. “Nếu không có hàm lượng enzym tự nhiên kháng viêm cực mạnh này cắt cơn co thắt phế quản cấp tốc, cha cô đã ngưng tim trước khi trực thăng y tế kịp đáp.”</p>
<p>Khánh An lập tức ra hiệu cho bác sĩ riêng của gia đình lên xe kiểm tra các chỉ số sinh tồn của ông cụ. Sau hai phút, bác sĩ ngẩng đầu lên, giọng run rẩy kinh ngạc: “Thưa Chủ tịch Khánh An... thật kỳ diệu! Phổi của ngài An đã thông thoáng hoàn toàn, các chỉ số hô hấp ổn định một cách khó tin. Phương pháp bấm huyệt và thảo dược của cậu thanh niên này thực sự là cứu mạng kịp thời!”</p>
<p>Khánh An khẽ nhíu mày, ánh mắt cô quét qua người Đăng từ chiếc áo khoác sờn vai đến chiếc ba lô lấm bùn tuyết. Bằng trực giác nhạy bén của một nhà đầu tư hàng đầu, cô lập tức nhận ra giá trị vô giá của con người này.</p>
<p>“Tôi không bao giờ nợ ai, đặc biệt là ân nhân cứu mạng của cha tôi,” Khánh An bước tới gần Đăng, đưa ra một tấm danh thiếp mạ vàng sang trọng. “Tôi là Nguyễn Khánh An. Tôi đã điều tra về vụ việc trang trại mật ong bạc hà hữu cơ bị VietHoney cướp đoạt của anh. Anh có muốn lấy lại tôn nghiêm và xây dựng một đế chế nông sản sạch nghiền tỷ đè bẹp những kẻ phản bội kia không?”</p>
<p>Đăng nhìn tấm danh thiếp, rồi nhìn vào đôi mắt kiên định của cô: “Tôi đồng ý. Nhưng tôi chỉ làm việc dựa trên tiêu chuẩn hữu cơ nguyên bản, không thỏa hiệp với hóa chất sinh lợi nhanh.”</p>
<p>“Rất tốt, tôi thích sự lý tính và kiên định của anh,” Khánh An mỉm cười sắc sảo. “Hợp đồng đầu tư 200 tỷ của Vạn An Capital đã sẵn sàng. Trò chơi phản sát chính thức bắt đầu!”</p>"""

    novel_data["chapters"].append({
        "title": "Chương 2: Cơ Duyên Bên Vách Đá Cao Nguyên",
        "content": ch2_content
    })

    # Chapter 3
    ch3_content = """<p>Tại thung lũng đá tai mèo hoang sơ giáp biên giới Đồng Văn, trang trại mật ong thông minh Vạn An chính thức được dựng lên như một pháo đài công nghệ nông nghiệp xanh hiện đại bậc nhất Việt Nam.</p>
<p>Triệu Hải Đăng đứng trên đài quan sát, xung quanh là hàng ngàn thùng ong kỹ thuật số được trang bị cảm biến IoT theo dõi nhiệt độ, độ ẩm và hoạt động của đàn ong mật tự nhiên. Búp hoa bạc hà hoang dại màu tím nhạt nở rộ khắp thung lũng đá, tỏa ra hương thơm thanh mát ngọt ngào trong nắng sớm.</p>
<p>Mỗi thùng ong của Đăng đều được liên kết trực tiếp với hệ thống blockchain truy xuất nguồn gốc số hóa. Người tiêu dùng chỉ cần quét mã QR trên mỗi chai mật ong là có thể kiểm tra chính xác tọa độ tổ ong, ngày thu hoạch, hàm lượng enzym tự nhiên và chứng nhận không chứa kháng sinh do tổ chức SGS Thụy Sĩ kiểm định.</p>
<p>“Anh Bảo... à không, anh Đăng, công nghệ giám sát tần số cánh đập của ong mật đã hoàn thiện và đồng bộ lên GitHub thành công,” Nguyễn Khánh An bước đến bên cạnh anh, mái tóc ngắn bay nhẹ trong gió ngàn, tay cầm chiếc iPad hiển thị biểu đồ dòng dữ liệu sinh học thời gian thực.</p>
<p>“Tốt lắm, Khánh An. Việc số hóa toàn bộ quy trình này giúp chúng ta bảo vệ bản quyền công nghệ tách nước chân không giữ nguyên enzym tuyệt đối,” Đăng gật đầu, ánh mắt anh tràn đầy sự kiêu hãnh. “Khi Duy Khang và Mỹ Hạnh dùng công thức giả mạo ăn cắp của tôi, chúng sẽ chỉ có vỏ bọc bên ngoài mà không có linh hồn công nghệ kiểm soát sinh học bên trong.”</p>
<p>Khánh An khẽ đẩy gọng kính cận mạ vàng, nụ cười cô mang theo sự lạnh lùng của một CFO sắt đá: “Quỹ đầu tư Vạn An đã hoàn tất thủ tục đăng ký bằng sáng chế quốc tế độc quyền tại Mỹ và EU cho công nghệ tách nước sinh học của anh. Đồng thời, dòng tiền 200 tỷ đã được giải ngân sòng phẳng sang tài khoản Vietcombank đứng tên riêng của anh.”</p>
<p>“Cùng lúc đó, tình báo thị trường của tôi báo về: VietHoney của Hoàng Duy Khang đang chuẩn bị nộp hồ sơ xin IPO trên sàn chứng khoán TP.HCM vào cuối tháng này. Chúng đã thổi phồng doanh thu bằng cách ký hợp đồng xuất khẩu khống 500 tấn mật ong bạc hà sang thị trường Mỹ thông qua một công ty bình phong tại Singapore.”</p>
<p>Đăng khẽ cười lạnh, bàn tay siết chặt lan can gỗ: “500 tấn mật ong bạc hà hữu cơ? Cả cao nguyên đá Đồng Văn này gộp lại mỗi năm chỉ thu hoạch được tối đa 50 tấn mật ong nguyên chất tự nhiên nở hoa bạc hà. Chúng lấy đâu ra 500 tấn để xuất khẩu nếu không dùng mật mía, mạch nha và hóa chất tạo mùi nhân tạo của Trung Quốc?”</p>
<p>“Chính xác,” Khánh An nhấp một ngụm trà sen ấm nóng, đôi mắt lóe lên tia sáng mưu lược tột cùng. “Chúng đang tự đào mồ chôn mình khi cố tình gian lận xuất xứ để IPO nhanh chóng. Tôi đã liên hệ với Big 4 EY để bắt đầu tiến hành kiểm toán dòng tiền pháp lý độc lập đối với các công ty vệ tinh của VietHoney.”</p>
<p>“Bên cạnh đó, nhật ký commit Git trên máy chủ trang trại cũ của anh vẫn lưu giữ đầy đủ bằng chứng chữ ký số cá nhân PGP của anh trước ngày bị sa thải. Đó chính là quả bom hẹn giờ vô hình sẽ kích nổ toàn bộ kế hoạch lừa đảo IPO nghìn tỷ của bọn chúng.”</p>
<p>Đăng nhìn đàn ong mật đang chăm chỉ bay về tổ mang theo những giọt mật ngọt ngào tinh túy của đất trời cao nguyên. Ngọn lửa phục thù rực cháy trong lồng ngực anh giờ đây đã được dẫn dắt bởi một kế hoạch lý tính sắc bén của người đồng hành xuất sắc.</p>
<p>“Hãy để chúng kiêu ngạo leo lên đỉnh cao danh vọng đi, Khánh An. Khi chúng chuẩn bị gõ búa khai trương sàn chứng khoán, tôi sẽ giật dây thừng siết chặt cổ tất cả những kẻ phản bội đó!” Đăng trầm giọng đầy đanh thép.</p>"""

    novel_data["chapters"].append({
        "title": "Chương 3: Công Nghệ Tổ Ong Số Hóa",
        "content": ch3_content
    })

    # Chapter 4
    ch4_content = """<p>Tại đại bản doanh lộng lẫy của tập đoàn VietHoney ở Hà Nội, không khí chuẩn bị cho phi vụ IPO nghìn tỷ đang diễn ra vô cùng náo nhiệt và khẩn trương.</p>
<p>Hoàng Duy Khang đứng trước tấm bản đồ quy hoạch ranh giới trang trại nuôi ong Đồng Văn mới bị gã sửa đổi tinh vi, khuôn mặt gã đầy vẻ tính toán nham hiểm và kiêu ngạo tột cùng. Bên cạnh gã, Lương Mỹ Hạnh diện chiếc váy đắt tiền sang trọng nâng ly rượu vang đỏ chúc mừng.</p>
<p>“Anh Khang, mọi việc đã hoàn toàn trơn tru. Hồ sơ xin IPO đã được Sở Giao dịch Chứng khoán phê duyệt vòng sơ tuyển. Nhờ hợp đồng xuất khẩu khống 500 tấn sang Mỹ ký với công ty Singapore, định giá của VietHoney đã vọt lên mốc 1.200 tỷ đồng!” Mỹ Hạnh đắc ý cười lớn, ôm chầm lấy gã.</p>
<p>“Tất cả là nhờ công thức tách nước chân không của thằng ngu Hải Đăng để lại,” Duy Khang nhấp một ngụm rượu vang, mỉa mai khinh bỉ. “Nhưng để tối ưu hóa tối đa lợi nhuận khổng lồ này và đáp ứng sản lượng 500 tấn, tao đã ra lệnh cho nhà xưởng tại Hưng Yên pha trộn 85% si-rô ngô cao phân tử Fructose và hóa chất tạo hương bạc hà nhân tạo nhập khẩu giá rẻ.”</p>
<p>“Chỉ cần dán nhãn ‘Mật Ong Bạc Hà Hữu Cơ Đồng Văn Hà Giang’, người tiêu dùng bình thường làm sao phân biệt được đâu là tự nhiên, đâu là nhân tạo? Lợi nhuận biên sẽ tăng lên đến 400%!”</p>
<p>Mỹ Hạnh khẽ rùng mình trước sự táo bạo điên cuồng của Khang, nhưng lòng tham vô đáy đã nhanh chóng lấn át nỗi sợ hãi pháp luật: “Nhưng thưa anh... nếu bên phía đối tác Mỹ yêu cầu kiểm nghiệm lâm sàng độc lập và truy xuất nguồn gốc sinh học của sản phẩm thì sao?”</p>
<p>“Lo gì chứ?” Khang cười lớn đầy tự mãn. “Tao đã chi hàng trăm triệu đồng để đút lót cho vài cán bộ kiểm định chất lượng địa phương để họ cấp giấy chứng nhận giả mạo. Chỉ cần đưa được cổ phiếu lên sàn chứng khoán và xả sạch cổ phần thu về hàng trăm tỷ, tập đoàn sụp đổ sau đó thế nào không còn là việc của chúng ta!”</p>
<p>Đúng lúc đó, cánh cửa phòng họp đột ngột bị đẩy mạnh ra. Trưởng phòng truyền thông hớt hải chạy vào, mặt cắt không còn giọt máu, trán đầm đìa mồ hôi lạnh: “Chủ tịch Khang! Có biến lớn rồi! Trên mạng xã hội bất ngờ xuất hiện một video phân tích chi tiết của một chuyên gia sinh học giấu mặt.”</p>
<p>“Video đó chỉ ra toàn bộ sản phẩm mật ong bạc hà bán chạy nhất của VietHoney thực chất là nước đường hóa học pha chế bằng hóa chất tạo mùi nhân tạo của Trung Quốc, hoàn toàn không có hoạt tính enzym tự nhiên của mật ong bạc hà Hà Giang!”</p>
<p>“Cái gì?” Duy Khang trừng mắt giận dữ, đập mạnh ly rượu vang xuống sàn nhà vỡ tan tành. “Ai dám tung tin đồn nhảm phá hoại phiên IPO của tao? Lập tức thuê đội ngũ truyền thông bẩn đánh sập clip đó ngay lập tức!”</p>
<p>“Không... không được thưa Chủ tịch,” gã trưởng phòng lắp bắp run rẩy. “Đồng thời, Sở Nông nghiệp tỉnh Hà Giang và Cục An toàn Thực phẩm Bộ Y tế vừa ban hành công văn khẩn cấp yêu cầu thanh tra đột xuất nhà máy pha chế của chúng ta tại Hưng Yên dựa trên đơn tố cáo nặc danh kèm theo tọa độ các thùng ong giả mạo.”</p>
<p>Lương Mỹ Hạnh nghe vậy liền bủn rủn cả tay chân, chiếc ví hiệu Hermes rơi bộp xuống đất: “Khang... không lẽ là thằng Hải Đăng? Nó... nó làm sao có sức ảnh hưởng lớn thế này được?”</p>
<p>“Mẹ kiếp! Thằng nuôi ong quèn rách rưới đó làm sao có cửa đấu với thế lực tài chính của tao!” Duy Khang trừng mắt đầy sát khí hung hãn. “Hạnh, cô lập tức liên hệ với bên công ty công chứng quận 5 để xóa sạch dấu vết của chữ ký số cũ. Bằng mọi giá phải đè bẹp dư luận bẩn này trước ngày hội chợ triển lãm nông nghiệp quốc gia diễn ra vào tuần tới!”</p>
<p>Gã không hề biết rằng, toàn bộ đường dây kiểm định chất lượng giả mạo và dòng tiền bất hợp pháp của gã đã bị Nguyễn Khánh An cài cắm kiểm toán Big 4 kiểm soát từ trước, chỉ chờ ngày đưa tất cả ra ánh sáng công lý tàn khốc.</p>"""

    novel_data["chapters"].append({
        "title": "Chương 4: Kẻ Phản Bội Lộ Mặt",
        "content": ch4_content
    })

    # Chapter 5
    ch5_content = """<p>Để đối phó với cuộc khủng hoảng truyền thông đang lan rộng trước ngày IPO định mệnh, Hoàng Duy Khang và Lương Mỹ Hạnh quyết định tung đòn truyền thông bẩn tàn khốc nhất hòng triệt tiêu đối thủ cạnh tranh trực tiếp.</p>
<p>Chỉ trong một đêm, hàng loạt trang tin tức không chính thống và tài khoản mạng xã hội đồng loạt đăng tải thông tin vu khống trang trại mật ong hữu cơ Vạn An của Triệu Hải Đăng sử dụng kháng sinh cấm và đường hóa học nhằm tăng sản lượng ép ong sản xuất.</p>
<p>“Sự thật kinh hoàng về mật ong bạc hà thông minh Vạn An: Công nghệ IoT thực chất là chiêu trò lừa đảo công nghệ để che giấu mật ong bẩn nhiễm chì từ vách đá biên giới!” – Những tiêu đề giật gân, đầy ác ý liên tục xuất hiện trên trang đầu các diễn đàn nông nghiệp.</p>
<p>Lương Mỹ Hạnh ngồi trong văn phòng sang trọng, theo dõi các chỉ số tương tác tiêu cực tăng vọt của Vạn An bằng nụ cười độc địa tột cùng: “Triệu Hải Đăng, để tôi xem một gã nuôi ong quèn rách rưới như anh lấy gì để chống chọi lại cơn bão truyền thông bẩn nghìn tỷ này!”</p>
<p>Tại trang trại Vạn An trên cao nguyên đá Đồng Văn, không khí vô cùng căng thẳng. Hàng chục phóng viên báo chí bẩn kéo đến đứng nghẹt ngoài cổng chính, lăm lăm máy quay phim đòi phỏng vấn chất vấn Đăng về các cáo buộc sử dụng hóa chất.</p>
<p>“Anh Đăng, đại diện của nhà nhập khẩu Mỹ vừa gửi email khẩn cấp yêu cầu tạm đình chỉ việc xếp hàng lên container tại cảng Hải Phòng cho đến khi có kết quả làm rõ từ chính quyền,” Trưởng phòng kinh doanh lo lắng báo cáo, khuôn mặt lo âu tột độ.</p>
<p>Đăng đứng yên lặng bên chiếc máy ly tâm, ánh mắt anh vẫn vô cùng bình thản và kiên định như băng tuyết ngàn năm trên đỉnh núi lửa.</p>
<p>“Đừng lo lắng, hãy để chúng tự tin đẩy cuộc tấn công bẩn này lên đỉnh điểm cao trào nhất đi,” Đăng quay sang mỉm cười nhẹ nhàng nhìn Nguyễn Khánh An đang gõ bàn phím tốc độ cao bên chiếc máy chủ trang trại.</p>
<p>“Khánh An, dữ liệu log băm SHA-256 của nhật ký commit Git trên máy chủ trang trại cũ từ ba năm trước đã được giải mã và đối chiếu xong chưa?”</p>
<p>Khánh An khẽ gạt mái tóc ngắn, nở nụ cười đầy lạnh lùng và mưu trí xuất chúng: “Xong hoàn toàn, anh Đăng. Chữ ký số PGP cá nhân của anh gắn liền với từng phiên bản nghiên cứu công thức gốc đã được tổ chức sở hữu trí tuệ WIPO của Liên Hợp Quốc chứng thực đóng dấu xác nhận quyền tác giả gốc.”</p>
<p>“Đồng thời, đội ngũ pháp lý của Vạn An Capital đã hoàn tất báo cáo kiểm toán độc quyền từ Big 4 EY. Báo cáo này vạch trần chi tiết đường đi của dòng tiền 1.200 tỷ của VietHoney thực chất là các khoản giao dịch khống vòng quanh các công ty ma ở Singapore để lừa đảo cổ đông.”</p>
<p>“Tuyệt vời,” Đăng bước ra ngoài ban công, nhìn về phía đám phóng viên đang hò hét náo động bên dưới. “Sự thật là thứ duy nhất không thể bị bóp méo bởi truyền thông bẩn. Đã đến lúc đưa ra đòn phản công chí mạng lật kèo thế kỷ!”</p>
<p>Chỉ mười phút sau, trên cổng thông tin chính thống của Ban chỉ đạo Quốc gia về Chống buôn lậu và gian lận thương mại bất ngờ công bố quyết định thanh tra khẩn cấp và đình chỉ tạm thời phiên phát hành cổ phiếu IPO của tập đoàn VietHoney để phục vụ điều tra hành vi lừa đảo tài chính và an toàn thực phẩm.</p>
<p>Hoàng Duy Khang lúc này đang ngạo nghễ ngồi trên xe Maybach đắt tiền chuẩn bị đến dự triển lãm nông nghiệp quốc gia, nhận được cuộc gọi từ môi giới chứng khoán thông báo tin sét đánh lập tức đờ đẫn cả người, điện thoại rơi khỏi tay, mặt xám ngoét cắt không còn giọt máu.</p>
<p>Cơn bão pháp lý thực sự đã ập đến, xé toang bức màn dối trá hào nhoáng của những kẻ phản bội tham tàn, bắt đầu quá trình trừng phạt tàn khốc nhất.</p>"""

    novel_data["chapters"].append({
        "title": "Chương 5: Đòn Truyền Thông Bẩn",
        "content": ch5_content
    })

    # Chapter 6
    ch6_content = """<p>Đêm trước ngày diễn ra Triển lãm Nông nghiệp Quốc tế tại Trung tâm Hội nghị Quốc gia Hà Nội, văn phòng làm việc của Nguyễn Khánh An tại tòa nhà Lotte Liễu Giai sáng rực đèn dưới cơn mưa giông tầm tã của thủ đô.</p>
<p>Triệu Hải Đăng và Khánh An cùng ngồi trước màn hình hiển thị cơ sở dữ liệu số hóa của trang trại cũ. Trên bàn là tập báo cáo kiểm toán dày cộp của Big 4 EY đóng dấu đỏ chói cùng sắc lệnh hỗ trợ điều tra đặc biệt từ C03 Bộ Công an.</p>
<p>“Anh Đăng, toàn bộ dữ liệu lịch sử commit Git trên ổ cứng di động của anh đã được phục chế hoàn hảo,” Khánh An đẩy chiếc kính cận gọng mảnh lên, giọng điệu cô vô cùng sắc sảo và lý tính cực hạn.</p>
<p>“Mỗi phiên bản cập nhật công thức tách nước giữ enzym tự nhiên từ năm 2022 đến nay đều ghi nhận rõ ràng địa chỉ IP phát sinh từ máy tính cá nhân của anh tại Đồng Văn, có chữ ký số PGP khóa riêng của anh xác thực và không thể chối cãi.”</p>
<p>“Trong khi đó, Hoàng Duy Khang chỉ mới đăng ký quyền tác giả giả mạo vào đầu năm 2026 bằng cách sao chép nguyên bản thiết kế cũ bị thiếu phần mã hóa tối ưu hóa nhiệt độ dòng ly tâm.”</p>
<p>Đăng khẽ vuốt ve chiếc ổ cứng di động sờn cũ – thứ duy nhất anh giữ lại được trong đêm đông giông bão tuyết rơi buốt giá của Hà Giang: “Bản thiết kế mà Khang cướp đoạt có một lỗ hổng kỹ thuật chí mạng. Do thiếu thuật toán tự động cân bằng áp suất chân không sinh học, khi sản xuất công nghiệp quy mô lớn vượt quá 10 tấn, hệ thống ly tâm sẽ tự động sinh nhiệt vượt mức 40 độ C.”</p>
<p>“Nhiệt độ này sẽ tiêu diệt hoàn toàn hoạt tính enzym glucose oxidase tự nhiên của mật ong, biến nó thành một hỗn hợp đường biến tính độc hại, dễ bị lên men chua và hỏng mốc chỉ sau 14 ngày bảo quản.”</p>
<p>“Đúng như vậy,” Khánh An mỉm cười đầy ẩn ý mưu trí. “Báo cáo kiểm toán chất lượng từ viện đo lường chất lượng độc lập của Mỹ gửi về chiều nay xác nhận: Toàn bộ lô hàng 500 tấn mật ong bạc hà giả mạo xuất khẩu của VietHoney đang bị giữ lại tại cảng Los Angeles do phát hiện chứa dư lượng cao chất tạo hương độc hại Methyl Anthranilate vượt ngưỡng cho phép 200 lần!”</p>
<p>“Cùng lúc đó, Big 4 EY đã hoàn tất việc bóc trần dòng tiền của VietHoney. Hóa ra, toàn bộ doanh thu khổng lồ của chúng thực chất là các khoản vay tín dụng đen lãi suất cao từ các công ty bình phong của Duy Khang nhằm tạo tài khoản doanh thu khống để lừa đảo các nhà đầu tư cá nhân trên sàn chứng khoán.”</p>
<p>Đăng đứng dậy, ánh mắt anh nhìn ra cửa sổ kính lớn hướng về phía khách sạn Daewoo xa hoa bên kia đường – nơi Duy Khang và Mỹ Hạnh đang tổ chức buổi tiệc VIP ăn mừng IPO thành công hờ.</p>
<p>“Bọn họ nghĩ rằng đã cướp được vương miện nghìn tỷ của tôi để bước chân vào giới thượng lưu sang chảnh,” Đăng khẽ lắc đầu lạnh lùng. “Nhưng ngày mai, tại Triển lãm Nông nghiệp Quốc tế, trước sự chứng kiến của hàng trăm đối tác quốc tế và các cơ quan truyền thông trung ương chính thống, tôi sẽ bắt bọn họ phải trả lại từng giọt máu và nước mắt mà họ đã ném vào vũng bùn tuyết của tôi dưới chân đèo đèo Hà Giang!”</p>
<p>Khánh An siết nhẹ tay anh, ánh mắt cô đầy kiên định và ấm áp: “Mọi thứ đã sẵn sàng. Ngày mai, cả ngành nông nghiệp Việt Nam sẽ chứng kiến ai mới thực sự là Vua Mật Ong Cao Nguyên Đá đích thực!”</p>"""

    novel_data["chapters"].append({
        "title": "Chương 6: Cuộc Phản Sát Bằng Dữ Liệu Lịch Sử",
        "content": ch6_content
    })

    # Chapter 7
    ch7_content = """<p>Sảnh lớn Triển lãm Nông nghiệp Quốc tế tại Hà Nội rực rỡ dưới hàng ngàn ánh đèn chùm lộng lẫy và cờ hoa rực rỡ. Hàng trăm gian hàng nông sản cao cấp của các tập đoàn đa quốc gia và đối tác quốc tế từ Mỹ, Nhật Bản, châu Âu chật kín người qua lại.</p>
<p>Hoàng Duy Khang và Lương Mỹ Hạnh đứng ở gian hàng trung tâm lộng lẫy nhất của tập đoàn VietHoney, bộ dạng vô cùng hống hách và tự mãn cực hạn. Mỹ Hạnh mặc chiếc đầm dạ hội sang trọng lấp lánh trang sức đắt tiền, khoác tay Khang nở nụ cười kiêu ngạo đón tiếp các đại biểu quốc tế.</p>
<p>“Chào mừng các vị khách quý đến với buổi nếm thử mật ong bạc hà hữu cơ độc quyền thương hiệu VietHoney của chúng tôi!” Mỹ Hạnh dõng dạc giới thiệu đầy kiêu hãnh.</p>
<p>Đúng lúc này, từ phía cửa chính, một đoàn đại biểu cao cấp của Ban tổ chức hội nghị cùng đại diện Sở Giao dịch Chứng khoán bước vào, đi bên cạnh là Triệu Hải Đăng và Nguyễn Khánh An. Đăng mặc bộ vest xám phẳng phiu lịch lãm, phong thái đĩnh đạc kiêu hùng bước đi giữa tiếng vỗ tay rộn rã kính nể của các chuyên gia nông nghiệp sạch.</p>
<p>Hoàng Duy Khang trừng mắt nhìn Đăng, khuôn mặt gã vặn vẹo đầy tức giận và khinh bỉ tột cùng. Gã lớn tiếng chế giễu đầy thách thức trước mặt các phóng viên truyền thông: “Ồ, thằng nuôi ong quèn rách rưới bị đuổi như chó Hải Đăng! Mày cũng có tư cách đến tham dự triển lãm quốc tế cao cấp này sao?”</p>
<p>“Có phải mày đến đây để xin tao bố thí cho vài đồng lẻ từ phi vụ IPO nghìn tỷ của VietHoney không?”</p>
<p>Đăng đứng yên lặng nhìn gã trợ lý cũ bằng ánh mắt sắc lạnh như dao găm của loài chim ưng: “Duy Khang, tôi đến đây không phải để xin bố thí. Tôi đến để phơi bày sự dối trá dơ bẩn của các người và lấy lại những gì thuộc về mình.”</p>
<p>“Dối trá? Mày có bằng chứng gì?” Mỹ Hạnh cười khẩy đầy kiêu ngạo mỉa mai. “Bản quyền công nghệ tách nước đã đứng tên VietHoney, giấy tờ công chứng đầy đủ. Mày chỉ là kẻ thất bại ghen ăn tức ở!”</p>
<p>Đúng lúc này, Nguyễn Khánh An dứt khoát bước lên phía trước chủ tọa, đặt lên bàn trình chiếu một ổ cứng di động, kết nối trực tiếp với màn hình LED khổng lồ 500 inch của hội trường triển lãm.</p>
<p>“Tôi là Nguyễn Khánh An, đại diện pháp luật của Vạn An Capital và cũng là đơn vị sở hữu độc quyền công nghệ số hóa tổ ong blockchain Kỳ Quan Xanh,” giọng nói cô đanh thép, lạnh lùng vang dội khắp sảnh triển lãm.</p>
<p>“Trên màn hình là toàn bộ dữ liệu lịch sử commit Git gốc của công nghệ tách nước sinh học bảo tồn enzym, được mã hóa bằng chữ ký số PGP cá nhân của anh Triệu Hải Đăng từ năm 2022, trước ngày bị các người giả mạo con dấu chiếm đoạt ba năm.”</p>
<p>“Đồng thời, đây là văn bản từ Cục Sở hữu Trí tuệ Hoa Kỳ (USPTO) và EUIPO chứng nhận bằng sáng chế quốc tế độc quyền đứng tên riêng của Triệu Hải Đăng!”</p>
<p>Cả phòng triển lãm ồ lên kinh ngạc tột độ. Gương mặt Hoàng Duy Khang lập tức chuyển sang xám ngoét cắt không còn giọt máu.</p>
<p>Chưa dừng lại ở đó, đại diện kiểm toán Big 4 EY bước lên phát biểu dõng dạc trước micro: “Qua kết quả kiểm toán dòng tiền độc lập, chúng tôi xác nhận: Tập đoàn VietHoney đã làm giả toàn bộ hợp đồng xuất khẩu 500 tấn mật ong sang Mỹ. Thực chất, VietHoney đã nhập khẩu hàng ngàn tấn si-rô đường ngô hóa chất giá rẻ từ Trung Quốc để pha chế mật ong bạc hà giả mạo lừa đảo nhà đầu tư!”</p>
<p>Cùng lúc đó, đại diện đoàn kiểm tra y tế quốc tế đột ngột bước tới gian hàng VietHoney, ném thẳng kết quả xét nghiệm mẫu thử xuống bàn: “Sản phẩm mật ong của các người chứa dư lượng độc chất hóa học Methyl Anthranilate cực cao gây ngộ độc cấp tính! Chúng tôi chính thức đình chỉ và niêm phong toàn bộ gian hàng của VietHoney!”</p>
<p>Mỹ Hạnh đờ đẫn rụng rời chân tay, ngã sụp xuống sàn nhà lạnh lẽo, trang sức đắt tiền rơi lả tả. Duy Khang hoảng loạn định quay lưng bỏ chạy trốn thoát nhưng cánh cửa sắt lớn đã bị chặn đứng.</p>
<p>Hơn mười chiến sĩ cảnh sát kinh tế thuộc C03 Bộ Công an bước vào phòng đấu giá, cầm trên tay sắc lệnh bắt giữ khẩn cấp có dấu đỏ chói đóng mộc của Bộ Công an dõng dạc tuyên bố: “Hoàng Duy Khang! Lương Mỹ Hạnh! Các người bị bắt khẩn cấp về hành vi lừa đảo chiếm đoạt tài sản, gian lận thương mại và hủy hoại an toàn thực phẩm nghiêm trọng!”</p>
<p>Chiếc còng số 8 lạnh ngắt khóa chặt tay Duy Khang và Mỹ Hạnh kéo đi giữa sự khinh bỉ, sỉ nhục tột cùng của hàng trăm đối tác quốc tế và các cơ quan báo chí truyền thông đang quay phim chụp ảnh liên tục.</p>
<p>Đăng đứng yên lặng nhìn bóng dáng hai kẻ phản bội bị kéo lê đi trong vũng bùn nhơ nhuốc ô nhục do chính chúng tạo ra, lòng anh nhẹ nhõm và tràn đầy kiêu hãnh hào hùng.</p>"""

    novel_data["chapters"].append({
        "title": "Chương 7: Triển Lãm Nông Nghiệp Quốc Tế - Vả Mặt Công Khai",
        "content": ch7_content
    })

    # Chapter 8
    ch8_content = """<p>Một tháng sau cơn địa chấn pháp lý quét sạch tập đoàn phản bội VietHoney tại thủ đô, cao nguyên đá Đồng Văn đã lấy lại vẻ yên bình thanh khiết vốn có.</p>
<p>Trang trại mật ong thông minh Vạn An lúc này tấp nập những dòng xe container chở hàng của các đối tác xuất khẩu quốc tế từ Mỹ, Nhật Bản và các nước Bắc Âu đến ký kết hợp đồng thu mua mật ong hữu cơ nguyên chất dài hạn đứng tên Triệu Hải Đăng.</p>
<p>Buổi tiệc vinh danh nông sản sạch Việt Nam được tổ chức ngay tại trung tâm thung lũng hoa bạc hà rực rỡ nắng vàng và hương thơm thanh mát ngọt ngào.</p>
<p>Triệu Hải Đăng đứng trên bục vinh dự lớn nhất, bên cạnh anh là Nguyễn Khánh An kiêu sa đĩnh đạc và ông cụ Trịnh Vạn An – siêu tỷ phú đã hoàn toàn khỏe mạnh, hồng hào rạng rỡ.</p>
<p>“Hôm nay, trước sự chứng kiến của toàn thể các đối tác quốc tế và người dân Hà Giang, tôi chính thức tuyên bố Triệu Hải Đăng là Vua Mật Ong Cao Nguyên Đá Đông Nam Á!” Ông cụ Trịnh Vạn An dõng dạc tuyên bố đầy tự hào trước micro, tiếng vỗ tay rộn rã kéo dài vang dội khắp thung lũng đá cao nguyên.</p>
<p>Đăng bước lên nhận chiếc cúp vàng danh giá, ánh mắt anh nhìn về phía những rặng núi đá tai mèo sừng sững cheo leo giữa mây ngàn – nơi anh từng quỳ rạp dưới tuyết lạnh căm hờn u uất năm xưa.</p>
<p>Anh cất giọng trầm ấm, đanh thép và đầy uy lực truyền cảm hứng mạnh mẽ: “Mật ong bạc hà hữu cơ Hà Giang không chỉ là một sản phẩm thương mại. Nó là tinh hoa đất trời, là mồ hôi và danh dự của người nông dân Việt Nam.”</p>
<p>“Khi chúng ta làm việc bằng cả trái tim chân thực và khoa học kỹ thuật lý tính chuẩn mực, không một thế lực bẩn thỉu nào có thể bẻ gãy hay cướp đi hoài bão chân chính của chúng ta!”</p>
<p>Khánh An bước tới bên cạnh anh, chạm ly rượu vang lấp lánh rực rỡ dưới nắng vàng cao nguyên: “Chúc mừng anh, Vua Mật Ong Triệu Hải Đăng. Đế chế Vạn An Honey của chúng ta đã chính thức hoàn tất thủ tục niêm yết IPO thành công sòng phẳng trên sàn giao dịch quốc tế tại Singapore hôm nay!”</p>
<p>“Cảm ơn cô, Khánh An. Người đồng hành xuất sắc và tuyệt vời nhất của tôi,” Đăng nhìn sâu vào đôi mắt thông tuệ ấm áp của cô, cảm nhận một tương lai rực rỡ huy hoàng đang mở ra trước mắt.</p>
<p>Phía xa xa dưới chân đèo đèo Đồng Văn, Hoàng Duy Khang và Lương Mỹ Hạnh đang phải mặc những chiếc áo tù nhân xám xịt đứng trước vành móng ngựa chịu án tù chung thân cho những tội lỗi tham tàn dơ bẩn của mình. Chúng đã phải trả giá đắt nhất cho sự kiêu ngạo, tham lam và phản bội.</p>
<p>Sóng núi Hà Giang cuồn cuộn đổ về, mang theo tiếng hát vang dội của vương quốc mật ong hữu cơ nghìn tỷ, đánh dấu một triều đại huy hoàng rực rỡ của Vua Mật Ong Cao Nguyên Đá chính thức đăng vương ngự trị vĩnh cửu!</p>"""

    novel_data["chapters"].append({
        "title": "Chương 8: Đăng Vương Vua Mật Ong",
        "content": ch8_content
    })

    # Write payload file
    out_file = "/Users/aaronnguyen/TN/App/doctieuthuyet/pending_novel.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(novel_data, f, ensure_ascii=False, indent=4)
        
    print(f"🎉 Manuscript compiled successfully to {out_file}!")

if __name__ == "__main__":
    main()
