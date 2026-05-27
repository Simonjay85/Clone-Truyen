import json
import os

# Chapter 5
chap_5_title = "Chương 5: Bão nổi 24 giờ thanh tra và tài khoản đóng băng"
chap_5_content = """<p><strong>Cơn mưa dông giăng kín bầu trời Bình Dương, sấm sét xé toạc màn đêm lạnh lẽo hắt ánh sáng xanh mét vào xưởng sản xuất tranh mới của V-Art.</strong></p>
<p>Một đoàn thanh tra liên ngành đột ngột ập vào xưởng vẽ lúc 8 giờ sáng, dẫn đầu là một số cán bộ mang sắc phục quản lý thị trường và tài nguyên môi trường.</p>
<p>"Chúng tôi nhận được đơn tố cáo nặc danh kèm bằng chứng xưởng vẽ này tàng trữ hóa chất độc hại bị cấm và gây ô nhiễm nguồn nước ngầm!"</p>
<p>Cùng lúc đó, điện thoại của Trần Hoài Nam liên tục đổ chuông báo tin dữ: toàn bộ tài khoản ngân hàng Vietcombank của công ty V-Art đã bị phong tỏa khẩn cấp theo lệnh của tòa án để phục vụ điều tra.</p>
<p>Trên mạng xã hội, các trang báo lá cải bẩn đồng loạt đăng tải thông tin giật gân: "Nghệ nhân tàn phế của xưởng vẽ V-Art đầu độc môi trường bằng sơn hóa chất giả tạo màu."</p>
<p>Dư luận phẫn nộ bùng nổ, hàng ngàn bình luận bôi nhọ Nam xuất hiện, khách hàng hoang mang đòi hủy đơn đặt hàng tranh sơn mài.</p>
<p>Đối thủ Bảo Long và Lâm Gia lập tức tung tin đồn V-Art sắp phá sản để lôi kéo các nhà đầu tư của Quỹ Vạn An.</p>
<p>Trần Hoài Nam đứng giữa xưởng vẽ bị niêm phong, đôi tay anh nắm chặt, mồ hôi lạnh chảy dài sau gáy nhưng ánh mắt vẫn lạnh lùng điềm tĩnh.</p>
<p>"Hoài Nam, anh đừng lo! Đây chỉ là chiêu trò bẩn thỉu quen thuộc của chúng." Trịnh Hoàng Yến bước tới, đặt tay lên vai anh trấn an.</p>
<p>"Bọn chúng nghĩ phong tỏa tài khoản ngân hàng trong nước là có thể bóp chết dòng tiền của chúng ta."</p>
<p>"Nhưng bọn chúng quên mất Quỹ Vạn An có nguồn vốn ủy thác quốc tế từ Singapore và Thụy Sĩ hoàn toàn nằm ngoài tầm kiểm soát của chúng!"</p>
<p>Yến nhanh chóng liên hệ với Big 4 kiểm toán quốc tế (EY) để thực hiện một cuộc kiểm toán độc lập khẩn cấp ngay tại xưởng vẽ.</p>
<p>Đồng thời, cô phái đội ngũ chuyên gia an ninh mạng thu thập toàn bộ lịch sử IP của các tài khoản đăng tin bôi nhọ Nam trên mạng xã hội.</p>
<p>Bão giông ngoài kia đang cuồng nộ gầm rú, nhưng bên trong phòng làm việc, Nam và Yến vẫn lặng lẽ chuẩn bị đòn phản công chí mạng.</p>"""

# Chapter 6
chap_6_title = "Chương 6: Bản sao kê đóng dấu đỏ và báo cáo kiểm toán Big 4"
chap_6_content = """<p><strong>Cuộc họp báo khẩn cấp do Quỹ Đầu tư Vạn An tổ chức diễn ra tại khách sạn Sheraton Sài Gòn thu hút hàng trăm phóng viên báo chí và đài truyền hình quốc gia tham dự.</strong></p>
<p>Lâm Thế Hùng và Lâm Mỹ Hạnh cũng có mặt dưới hàng ghế khán giả, vẻ mặt đắc thắng nghĩ rằng Nam sẽ phải cúi đầu nhận tội trước truyền thông.</p>
<p>Trần Hoài Nam bước lên bục phát biểu với bộ vest sang trọng lịch lãm, đôi tay lành lặn tự tin mở tập tài liệu báo cáo.</p>
<p>"Hôm nay, trước mặt toàn thể cơ quan báo chí, chúng tôi xin công bố kết quả thanh tra độc lập của Viện kiểm định Môi trường Quốc tế và Báo cáo kiểm toán pháp lý của EY!"</p>
<p>Trịnh Hoàng Yến đứng lên, trình chiếu bản sao kê ngân hàng đóng dấu đỏ chói lòa lên màn hình lớn.</p>
<p>"Đây là bản sao kê chi tiết tài khoản giao dịch của Bảo Long với một nhóm đối tượng chuyên dàn dựng scandal truyền thông bẩn."</p>
<p>"Chúng tôi đã xác định chính xác địa chỉ IP của kẻ phát tán đơn tố cáo nặc danh xuất phát từ chính văn phòng làm việc của Vương Quốc Bảo!"</p>
<p>Cả khán phòng họp báo ồ lên kinh ngạc, tiếng máy ảnh nháy liên tục như sấm chớp.</p>
<p>Yến tiếp tục công bố báo cáo kiểm toán Big 4 của EY chứng minh toàn bộ dòng tiền IPO của Lâm Gia thực chất là giao dịch ảo (round-tripping) nhằm đẩy khống doanh thu tranh giả lên gấp mười lần.</p>
<p>"Lâm Gia quảng cáo tranh sơn mài tự nhiên sạch, nhưng báo cáo kiểm định chất lượng độc lập chỉ ra 98% tranh của bọn chúng dùng sơn công nghiệp Alkyd độc hại của Bảo Long!"</p>
<p>Gương mặt Lâm Thế Hùng cắt không còn một giọt máu, gối đập mạnh xuống thành ghế kêu cộp.</p>
<p>Lâm Mỹ Hạnh mặt trắng bệch, ngón tay bấu chặt rỉ máu vì sợ hãi trước những chứng cứ đanh thép đóng dấu đỏ chói lòa.</p>
<p>Đòn tấn công truyền thông bẩn của Lâm Gia nay đã biến thành chiếc thòng lọng siết chặt cổ bọn chúng trước ánh sáng pháp luật.</p>
<p>Nam nhìn xuống cặp đôi phản bội, đôi mắt anh lạnh lùng như băng đá: "Màn kịch của các người chính thức hạ màn từ giây phút này!"</p>"""

# Load existing json and update
path = "scratch/rebuilt_3920_chapters.json"
if os.path.exists(path):
    with open(path, "r", encoding="utf-8") as f:
        db = json.load(f)
else:
    db = {"chapters": []}

db["chapters"].extend([
    {"chap_num": 5, "title": chap_5_title, "content": chap_5_content},
    {"chap_num": 6, "title": chap_6_title, "content": chap_6_content}
])

with open(path, "w", encoding="utf-8") as f:
    json.dump(db, f, ensure_ascii=False, indent=2)
print("Saved Chapters 5-6 successfully!")
