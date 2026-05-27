import json
import os

# Chapter 3
chap_3_title = "Chương 3: Bản phác thảo lưu dấu máu và sáng chế độc quyền"
chap_3_content = """<p><strong>Dưới ánh đèn huỳnh quang sáng trưng của phòng thí nghiệm thuộc viện nghiên cứu hóa chất TP.HCM, Trần Hoài Nam chăm chú quan sát phản ứng kết tủa giữa nhựa sơn ta tự nhiên và dịch chiết rễ dâu tằm cổ thụ.</strong></p>
<p>Bàn tay phải của anh nay đã hồi phục hoàn toàn da thịt, các khớp xương dẻo dai linh hoạt như chưa từng trải qua trận bỏng hóa chất kinh hoàng.</p>
<p>Trịnh Hoàng Yến đứng bên cạnh, chăm chú nhìn vào màn hình hiển thị quang phổ hồng ngoại của mẫu sơn thử nghiệm.</p>
<p>"Lâm Gia hiện đang tung ra thị trường hàng loạt tác phẩm dùng màu công nghiệp của Bảo Long dưới danh nghĩa sơn mài truyền thống nhằm phục vụ đợt IPO sắp tới."</p>
<p>"Bọn chúng quảng cáo đây là công nghệ sơn nhanh không độc hại, nhưng thực chất đó chỉ là sơn dầu Alkyd pha trộn bột màu hóa chất rẻ tiền nhanh phai."</p>
<p>"Hoài Nam, anh phải tìm ra công thức sơn ta chuẩn để dập tắt sự lừa đảo này!" Hoàng Yến nhấn mạnh.</p>
<p>Nam khẽ gật đầu, anh cầm ống nghiệm nhỏ giọt dung dịch lên men men rễ SB-09 độc quyền mà anh đã dày công nghiên cứu suốt sáu năm qua.</p>
<p>Khi giọt men rễ vừa chạm vào hỗn hợp nhựa sơn cổ thụ chưng cất, một phản ứng hóa học tự nhiên xảy ra.</p>
<p>Hỗn hợp chuyển từ màu nâu đen đục ngầu sang một màu sắc óng ánh, sâu thẳm tựa như ngọc đen dưới đáy đại dương.</p>
<p>Đó chính là màu sơn ta thất truyền - cực kỳ bền màu, chống mối mọt và có độ sâu quang học mà không loại màu hóa học nào có thể giả mạo được.</p>
<p>"Thành công rồi! Đây chính là màu sơn ta truyền thống thượng hạng!" Nam reo lên, ngón tay run rẩy vì xúc động.</p>
<p>Tuy nhiên, trong lúc hoàn thiện bản phác thảo kỹ thuật, một giọt máu từ vết trầy xước nhẹ trên tay Nam đã vô tình rơi vào trang giấy.</p>
<p>"Trang phác thảo lưu dấu máu này chính là minh chứng cho sự hồi sinh của nghệ thuật sơn mài!" Yến khẽ chạm vào vết máu khô.</p>
<p>"Chúng ta phải lập tức đệ đơn đăng ký bằng sáng chế độc quyền lên Cục Sở hữu Trí tuệ!"</p>
<p>Yến nhanh chóng điều động đội ngũ luật sư sở hữu trí tuệ giỏi nhất của Quỹ Vạn An để soạn thảo hồ sơ pháp lý khẩn cấp.</p>
<p>Hồ sơ đăng ký sáng chế men rễ SB-09 và quy trình chưng cất sơn ta tự nhiên được đóng dấu niêm phong gửi đi trong vòng 24 giờ.</p>
<p>Việc này tạo ra một tấm khiên bảo vệ pháp lý vững chắc trước bất kỳ âm mưu cướp đoạt nào từ phía Lâm Gia.</p>
<p>Sáng chế độc quyền này chính là quả bom nổ chậm treo trên đầu tập đoàn lừa đảo của Lâm Thế Hùng.</p>"""

# Chapter 4
chap_4_title = "Chương 4: Quỹ đầu tư lý tính và cái bẫy giăng ra"
chap_4_content = """<p><strong>Tại văn phòng làm việc sang trọng của Quỹ Đầu tư Vạn An tọa lạc trên tầng cao của tòa tháp Bitexco Quận 1, một bản hợp đồng đầu tư trị giá 150 tỷ đồng đã được ký kết.</strong></p>
<p>Trần Hoài Nam chính thức trở thành Giám đốc Nghệ thuật kiêm cổ đông sáng lập của Công ty Cổ phần Mỹ thuật Truyền thống Việt Nam (V-Art).</p>
<p>Trịnh Hoàng Yến mỉm cười đặt chiếc bút ký xuống bàn: "Với 150 tỷ đồng này, chúng ta sẽ mở rộng xưởng sản xuất tranh sơn mài chuẩn tự nhiên tại Thủ Dầu Một."</p>
<p>"Chúng ta sẽ tổ chức phiên đấu giá quốc tế để đưa tác phẩm của anh vươn tầm thế giới, trực tiếp đối đầu với Lâm Gia."</p>
<p>Tuy nhiên, sự trỗi dậy mạnh mẽ của Nam đã khiến Lâm Thế Hùng và Vương Quốc Bảo như ngồi trên đống lửa.</p>
<p>Tại biệt thự họ Lâm, gã thiếu gia hóa chất Vương Quốc Bảo tức giận đập mạnh ly rượu xuống sàn.</p>
<p>"Không thể để thằng phế vật đó lật kèo! Nếu nó công bố màu sơn sạch chuẩn tự nhiên, đợt IPO định giá nghìn tỷ của Lâm Gia sẽ sụp đổ hoàn toàn!"</p>
<p>Lâm Mỹ Hạnh mặt mày xám ngoét: "Anh Bảo, chúng ta phải làm sao? Nó có Quỹ Vạn An đứng sau nâng đỡ!"</p>
<p>Lâm Thế Hùng híp mắt lộ vẻ nham hiểm: "Bình tĩnh. Ta đã cho người ăn cắp bản phác thảo nghiên cứu dang dở của nó từ trước khi nó bị đuổi."</p>
<p>"Chúng ta sẽ đăng ký sáng chế trước nó và kiện ngược lại nó tội ăn cắp bí mật công nghệ của Lâm Gia!"</p>
<p>"Đồng thời, Bảo hãy dùng thế lực của Bảo Long để gài bẫy thanh tra xưởng vẽ của nó!"</p>
<p>Một kế hoạch đen tối nhanh chóng được giăng ra.</p>
<p>Vương Quốc Bảo thuê giang hồ dàn cảnh trà trộn hóa chất cấm vào kho nguyên liệu sạch của xưởng vẽ Nam.</p>
<p>Đồng thời, chúng mua chuộc một số cán bộ biến chất gửi đơn tố cáo khẩn cấp cáo buộc Nam sử dụng hóa chất độc hại gây ô nhiễm môi trường.</p>
<p>Lưới rập đã sẵn sàng, Lâm Gia tự tin sẽ dìm chết Nam trong vũng bùn pháp lý và dư luận bẩn trước khi phiên đấu giá diễn ra.</p>"""

# Load existing json if exists and update
path = "scratch/rebuilt_3920_chapters.json"
if os.path.exists(path):
    with open(path, "r", encoding="utf-8") as f:
        db = json.load(f)
else:
    db = {"chapters": []}

db["chapters"].extend([
    {"chap_num": 3, "title": chap_3_title, "content": chap_3_content},
    {"chap_num": 4, "title": chap_4_title, "content": chap_4_content}
])

with open(path, "w", encoding="utf-8") as f:
    json.dump(db, f, ensure_ascii=False, indent=2)
print("Saved Chapters 3-4 successfully!")
