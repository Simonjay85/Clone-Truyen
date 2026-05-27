import json
import os

# Chapter 7
chap_7_title = "Chương 7: Phiên đấu giá quốc tế và cú lật kèo hoàn hảo"
chap_7_content = """<p><strong>Khán phòng sang trọng của Trung tâm Triển lãm Nghệ thuật Quốc tế Phú Mỹ Hưng ngập tràn tiếng nhạc giao hưởng du dương và những bộ trang phục dạ hội lộng lẫy của giới siêu giàu Đông Nam Á.</strong></p>
<p>Lâm Thế Hùng và Vương Quốc Bảo cố gắng thực hiện vụ giao dịch cuối cùng để cứu vãn tập đoàn sắp phá sản bằng cách rao bán tác phẩm sơn mài "Bản Sắc Nam Phương" (đã được làm giả tinh vi) với giá khởi điểm 50 tỷ đồng.</p>
<p>Đúng lúc gõ búa chuẩn bị chốt giao dịch cho một tỷ phú người Singapore, Trần Hoài Nam thong thả bước vào khán phòng.</p>
<p>"Tôi yêu cầu dừng phiên đấu giá tác phẩm này lại vì đây là tranh giả sử dụng hóa chất công nghiệp độc hại!" Giọng nói trầm ấm của Nam vang lên đanh thép.</p>
<p>Vương Quốc Bảo hét lên: "Mày câm miệng! Thằng phế vật tàn phế thì biết gì về nghệ thuật? Bảo vệ đâu, đuổi nó ra ngoài!"</p>
<p>Tuy nhiên, đám bảo vệ chưa kịp tiến tới thì một nhóm cảnh sát kinh tế mặc sắc phục sải bước vào phòng, dẫn đầu là điều tra viên cao cấp thuộc Cục Cảnh sát Điều tra Tội phạm Kinh tế (C03).</p>
<p>Trịnh Hoàng Yến bước lên sân khấu, công bố bằng sáng chế độc quyền men rễ SB-09 của Trần Hoài Nam đã được Cục Sở hữu Trí tuệ cấp bằng chính thức.</p>
<p>"Quy trình sản xuất tranh sơn mài tự nhiên của Trần Hoài Nam đã được bảo hộ quốc tế."</p>
<p>"Bức tranh mà Lâm Thế Hùng đang đấu giá thực chất sử dụng công thức nhựa sơn hóa học ăn cắp thô thiển từ bản thảo cũ của Hoài Nam, vi phạm nghiêm trọng luật sở hữu trí tuệ và có chứa độc tố chì vượt ngưỡng cho phép mười lần!"</p>
<p>Nam cầm chiếc đèn soi quang phổ chuyên dụng quét qua bức tranh của Lâm Gia.</p>
<p>Dưới ánh sáng cực tím, toàn bộ lớp bột màu hóa chất công nghiệp hiện lên loang lổ xanh đỏ gớm ghiếc, hoàn toàn không có độ sâu trầm mặc của lớp sơn ta tự nhiên.</p>
<p>Tỷ phú người Singapore lập tức giận dữ hủy bỏ giao dịch và yêu cầu khởi kiện Lâm Gia vì tội gian lận thương mại.</p>
<p>Toàn bộ khách mời siêu giàu trong khán phòng đồng loạt đứng dậy tẩy chay và lên án sự lừa dối tr trẽn của Lâm Gia.</p>
<p>Vương Quốc Bảo khuỵu ngã xuống sàn, mồ hôi lạnh vã ra như tắm, đôi mắt trợn ngược kinh hoàng nhìn sự sụp đổ của đế chế lừa đảo nghìn tỷ.</p>"""

# Chapter 8
chap_8_title = "Chương 8: Đầu gối quỵ ngã của kẻ phản bội và sắc lệnh C03"
chap_8_content = """<p><strong>Tiếng còi xe cảnh sát rú vang inh ỏi bên ngoài cổng Trung tâm Triển lãm Phú Mỹ Hưng, xua tan hoàn toàn không khí xa hoa giả dối bên trong.</strong></p>
<p>Điều tra viên cao cấp bước lên sân khấu triển lãm, dõng dạc đọc to quyết định đóng dấu đỏ chói lòa.</p>
<p>"Lâm Thế Hùng! Vương Quốc Bảo! Các anh bị khởi tố khẩn cấp và bắt tạm giam vì tội lừa đảo chiếm đoạt tài sản, gian lận tài chính quy mô lớn và vi phạm nghiêm trọng luật sở hữu trí tuệ quốc gia!"</p>
<p>Chiếc còng số tám sáng loáng lạnh lùng bập vào tay Lâm Thế Hùng trước sự chứng kiến của hàng trăm ống kính phóng viên và đài truyền hình.</p>
<p>Lâm Thế Hùng run rẩy quỳ sụp hai đầu gối xuống nền đá hoa cương lạnh lẽo, miệng lảm nhảm xin tha thứ trong tuyệt vọng.</p>
<p>Lâm Mỹ Hạnh khóc lóc thảm thiết chạy đến ôm lấy chân Trần Hoài Nam, đôi mắt đỏ hoe đầy sự hối hận muộn màng.</p>
<p>"Hoài Nam... em sai rồi! Xin anh hãy cứu lấy gia tộc... em vẫn còn yêu anh... hãy cho em một cơ hội quay lại!"</p>
<p>Nam cúi đầu nhìn vị hôn thê cũ đầy khinh bỉ, khẽ rút chân ra khỏi vòng tay của cô ta.</p>
<p>"Cơ hội? Từ ngày cô đứng nhìn tôi bị ném ra ngoài mưa lạnh và giẫm nát chiếc nhẫn đính hôn, tôn nghiêm của tôi đối với cô đã chết!"</p>
<p>"Pháp luật sẽ đưa ra phán quyết công bằng nhất cho sự phản bội và lừa lọc của các người!"</p>
<p>Đám bảo vệ và cảnh sát nhanh chóng áp giải Lâm Thế Hùng, Vương Quốc Bảo và Lâm Mỹ Hạnh lên xe đặc chủng.</p>
<p>Chiếc xe cảnh sát hú còi lăn bánh khuất dần vào màn đêm, kết thúc một chương đen tối của những kẻ tham lam lừa đảo.</p>
<p>Khán phòng dần yên tĩnh trở lại, Trần Hoài Nam đứng bên cạnh Trịnh Hoàng Yến dưới ánh đèn sân khấu rực rỡ ấm áp.</p>
<p>Yến mỉm cười, trao cho anh bức họa "Bản Sắc Nam Phương" đích thực do chính đôi tay hồi sinh của anh phục chế hoàn mỹ.</p>
<p>"Chúc mừng anh, nghệ nhân Trần Hoài Nam! Di sản sơn mài truyền thống trăm năm của Việt Nam đã thực sự trở về đúng chủ nhân của nó."</p>
<p>Nam nắm chặt bàn tay ấm áp của Hoàng Yến, nhìn về phía chân trời bình minh tươi sáng đang ló rạng bên sông Sài Sòn.</p>
<p>"Cảm ơn em, Hoàng Yến. Hành trình mới của chúng ta bây giờ mới thực sự bắt đầu!"</p>"""

# Load existing json and update
path = "scratch/rebuilt_3920_chapters.json"
if os.path.exists(path):
    with open(path, "r", encoding="utf-8") as f:
        db = json.load(f)
else:
    db = {"chapters": []}

db["chapters"].extend([
    {"chap_num": 7, "title": chap_7_title, "content": chap_7_content},
    {"chap_num": 8, "title": chap_8_title, "content": chap_8_content}
])

with open(path, "w", encoding="utf-8") as f:
    json.dump(db, f, ensure_ascii=False, indent=2)
print("Saved Chapters 7-8 successfully!")
