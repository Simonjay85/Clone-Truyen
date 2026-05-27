import json
import os

# Chapter 1
chap_1_title = "Chương 1: Bàn tay phế và nhát búa đuổi khỏi xưởng"
chap_1_content = """<p><strong>"Cút khỏi xưởng sơn mài họ Lâm ngay lập tức! Loại tàn phế tay run như mày chỉ làm bẩn danh tiếng tranh truyền thống trăm năm của chúng ta!"</strong></p>
<p>Tiếng thét chói tai của Lâm Thế Hùng vang vọng khắp gian nhà xưởng rộng lớn, kèm theo đó là nhát búa gỗ nện mạnh xuống mặt bàn thờ tổ nghiệp.</p>
<p>Trần Hoài Nam đứng lặng yên giữa ánh nắng chiều muộn nhập nhoạng hắt qua khung cửa kính bám đầy bụi đỏ của xưởng sơn mài Hùng Cát danh tiếng Bình Dương.</p>
<p>Bàn tay phải của anh quấn băng gạc trắng toát, rỉ ra những vệt nước vàng nhợt nhạt và máu sẫm, từng ngón tay không ngừng run rẩy.</p>
<p>Sáu năm cống hiến thầm lặng, sáu năm chôn vùi thanh xuân bên những chậu sơn ta độc hại, đổi lại chỉ là một quyết định trục xuất lạnh lùng.</p>
<p>Cứu bức họa cổ "Bản Sắc Nam Phương" - bảo vật trăm năm của họ Lâm khỏi đám cháy tuần trước, anh đã dùng tay trần ôm lấy bức tranh đang cháy rực trong vũng hóa chất.</p>
<p>Hóa chất tẩy rửa công nghiệp cực mạnh bắt lửa đã ăn mòn da thịt anh, phá hủy hoàn toàn hệ thống dây thần kinh nhạy cảm của một nghệ nhân vẽ sơn mài đỉnh cao.</p>
<p>Mùi nhựa sơn, mùi cồn gôm và mùi thịt cháy xém như vẫn còn vương vấn trong không khí, bóp nghẹt lồng ngực anh.</p>
<p>"Thầy... con đã cứu bức họa gia bảo của Lâm Gia..." Nam khàn giọng nói, đôi mắt đỏ ngầu nhìn thẳng vào người thầy mà anh từng tôn kính như cha.</p>
<p>"Cứu gia bảo? Hay là mày tự dàn cảnh để tranh công?" Lâm Mỹ Hạnh - vị hôn thê từng thề non hẹn biển với anh - bước ra từ sau lưng Lâm Thế Hùng.</p>
<p>Cô diện chiếc váy hiệu Chanel sang trọng, đôi mắt kẻ sắc sảo nhìn Nam đầy vẻ ghê tởm.</p>
<p>"Hoài Nam, anh nhìn lại bàn tay tàn phế của mình đi! Một nghệ nhân sơn mài không cầm nổi cây bút cọ thì khác gì kẻ phế vật?"</p>
<p>"Hôn ước giữa tôi và anh chính thức hủy bỏ từ hôm nay. Loại nghèo hèn, tàn phế như anh không xứng bước chân vào Lâm Gia!"</p>
<p>Lâm Mỹ Hạnh lạnh lùng ném chiếc nhẫn đính hôn rẻ tiền xuống nền đất xi măng đầy bụi sơn cát.</p>
<p>Chiếc nhẫn lăn vài vòng rồi nằm im dưới gót giày da bóng loáng của Vương Quốc Bảo - thiếu gia tập đoàn hóa chất công nghiệp Bảo Long.</p>
<p>Bảo Long chính là thế lực đứng sau việc cung cấp dòng hóa chất tạo màu sơn công nghiệp giá rẻ cho Lâm Gia gần đây.</p>
<p>"Hoài Nam à, Mỹ Hạnh nói đúng đấy. Thời đại này ai còn vẽ sơn mài thủ công bằng thứ sơn ta đắt đỏ và độc hại kia?"</p>
<p>"Bảo Long của chúng tôi vừa ký hợp đồng cung cấp bột màu tổng hợp cho Lâm Gia, giúp rút ngắn thời gian hoàn thiện tranh từ sáu tháng xuống còn ba ngày!"</p>
<p>"Bàn tay phế của mày, thôi thì cầm chổi quét rác cũng là một ân huệ rồi!" Vương Quốc Bảo cười cợt, tiến tới giẫm nát chiếc nhẫn đính hôn.</p>
<p>Lâm Thế Hùng vẫy tay ra lệnh cho đám bảo vệ: "Kéo nó ra ngoài! Quăng đống hành lý rác rưởi của nó đi!"</p>
<p>Bảo vệ xông vào lôi kéo Nam một cách tàn nhẫn, vết thương trên tay anh va đập vào góc bàn gỗ khiến gạc trắng lập tức thấm đỏ một màu máu tươi.</p>
<p>Anh bị ném thẳng ra cổng xưởng dưới cơn mưa giông đột ngột trút xuống Bình Dương.</p>
<p>Đống hành lý cá nhân và chiếc hộp gỗ cũ kỹ đựng những mẫu thử nhựa sơn cổ thụ quý giá bị quăng mạnh xuống vũng nước bùn bẩn thỉu.</p>
<p>Nước mưa lạnh buốt dội thẳng vào mặt Nam, hòa lẫn với dòng nước mắt uất nghẹn lăn dài trên má.</p>
<p>Bàn tay phải run rẩy bấu chặt vào nền đất đá sắc nhọn, đau đớn thấu tận tâm can.</p>
<p>"Lâm Thế Hùng! Lâm Mỹ Hạnh! Vương Quốc Bảo!" Nam gầm lên trong tiếng sấm rền rĩ của trời đất.</p>
<p>"Những gì Trần Hoài Nam này đã dâng hiến cho Lâm Gia, hôm nay các người cướp đi, ngày sau tôi sẽ đòi lại gấp trăm lần!"</p>"""

# Chapter 2
chap_2_title = "Chương 2: Độc dược hóa chất và phương thuốc giữ tay"
chap_2_content = """<p><strong>Căn phòng trọ mười hai mét vuông nằm sâu trong con hẻm nhỏ dột nát ở ngoại ô Thủ Dầu Một ngập tràn mùi cồn y tế và tiếng mưa rơi rỉ rả trên mái tôn rỉ sét.</strong></p>
<p>Trần Hoài Nam ngồi gục đầu trên chiếc giường tre cũ kỹ, nhìn bàn tay phải tàn phế đang bắt đầu có dấu hiệu hoại tử do nhiễm độc hóa chất sơn công nghiệp nặng.</p>
<p>Bác sĩ ở bệnh viện đa khoa đã lắc đầu nói rằng anh cần chuẩn bị tinh thần tháo khớp ngón tay nếu tình trạng nhiễm trùng không thuyên giảm.</p>
<p>Mất đi đôi tay cầm cọ vẽ, cuộc đời của một người nghệ nhân sơn mài coi như đã đặt dấu chấm hết.</p>
<p>Đúng lúc Nam rơi vào tuyệt vọng tột cùng, tiếng gõ cửa vang lên dồn dập giữa màn đêm tĩnh mịch.</p>
<p>Anh gượng dậy mở cửa, một bóng người thanh mảnh che chiếc ô đen đứng sừng sững dưới ánh đèn đường mờ ảo.</p>
<p>Đó là Trịnh Hoàng Yến - nữ Giám đốc Tài chính (CFO) nổi tiếng lý tính và sắc bén của Quỹ Đầu tư Nghệ thuật Vạn An tại Sài Gòn.</p>
<p>Yến bước vào phòng, đôi mắt phượng thông minh lướt qua bàn tay đang rỉ máu của Nam rồi khẽ chau mày.</p>
<p>"Trần Hoài Nam, tôi đã tìm hiểu về ca cứu tranh của anh. Một thiên tài nghệ thuật không nên bị chôn vùi ở xó tối này!"</p>
<p>"Tôi là người của Vạn An. Chúng tôi muốn đầu tư vào anh, nhưng trước hết, chúng tôi phải giữ lại đôi tay này!"</p>
<p>Hoàng Yến ra lệnh cho tài xế mang vào một chiếc hộp y tế chuyên dụng và một hũ sứ nhỏ màu xanh ngọc bích.</p>
<p>"Thuốc kháng sinh Tây y thông thường không thể trung hòa được loại độc tố hóa chất công nghiệp pha tạp trong màu sơn giá rẻ của Bảo Long."</p>
<p>"Đây là 'Băng Cơ Cao' - phương thuốc Đông y bí truyền phục hồi cơ khớp làm từ nhựa sáp cây sơn rừng cổ thụ Tây Bắc phối hợp với tinh chất nhân sâm."</p>
<p>Yến đích thân ngồi xuống bên giường, nhẹ nhàng cắt bỏ lớp băng gạc dính máu trên tay Nam.</p>
<p>Nhìn vết thương loét sâu, cô không hề tỏ ra ghê tởm, ngón tay thanh mảnh thoa đều lớp cao thuốc mát lạnh lên da thịt anh.</p>
<p>Cảm giác đau đớn thiêu đốt bấy lâu nay lập tức dịu đi, thay vào đó là một luồng khí mát lành len lỏi vào từng thớ thịt và đầu dây thần kinh.</p>
<p>"Bên cạnh Đông y điều trị gốc, tôi đã liên hệ với giáo sư da liễu hàng đầu của Bệnh viện Pháp Việt để tiến hành trị liệu laser tái tạo tế bào dây thần kinh cho anh vào ngày mai."</p>
<p>"Đông Tây y kết hợp, đôi tay thiên tài của anh nhất định sẽ hồi sinh!" Giọng nói của Trịnh Hoàng Yến tràn đầy sự tự tin và lý tính kiên định.</p>
<p>Nam nhìn cô gái xa lạ đang tận tình giúp đỡ mình, trong lòng dấy lên một tia hy vọng mãnh liệt.</p>
<p>"Tại sao cô lại giúp tôi? Tôi bây giờ chỉ là một kẻ tàn phế bị trục xuất."</p>
<p>Trịnh Hoàng Yến ngẩng đầu, nở nụ cười đầy kiêu hãnh: "Vì tôi biết anh nắm giữ công thức sơn ta cổ truyền thất truyền ngàn năm của nghệ thuật sơn mài Việt Nam."</p>
<p>"Lâm Gia và Bảo Long dùng hóa chất độc hại để sản xuất tranh giả nhanh chóng, đó là sự sỉ nhục đối với nghệ thuật thực thụ!"</p>
<p>"Tôi muốn cùng anh tạo dựng một đế chế nghệ thuật đích thực, đập tan sự kiêu ngạo bẩn thỉu của bọn chúng!"</p>
<p>Dưới sự hỗ trợ y tế chuyên sâu từ Yến, chỉ sau ba ngày đêm, vết thương hoại tử trên tay Nam bắt đầu khép miệng.</p>
<p>Lớp da non màu hồng nhạt dần hình thành, cảm giác nhạy cảm ở các đầu ngón tay kỳ diệu khôi phục trở lại.</p>
<p>Anh đã có thể cầm chắc chiếc bút cọ vẽ sơn mài quen thuộc, đôi mắt ánh lên ngọn lửa phục thù rực cháy.</p>"""

db = {
    "chapters": [
        {"chap_num": 1, "title": chap_1_title, "content": chap_1_content},
        {"chap_num": 2, "title": chap_2_title, "content": chap_2_content}
    ]
}

os.makedirs("scratch", exist_ok=True)
with open("scratch/rebuilt_3920_chapters.json", "w", encoding="utf-8") as f:
    json.dump(db, f, ensure_ascii=False, indent=2)
print("Saved Chapters 1-2 successfully!")
