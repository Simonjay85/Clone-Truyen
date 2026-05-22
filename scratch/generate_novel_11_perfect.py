# -*- coding: utf-8 -*-
import json
import os

TEMP_PATH = "/Users/aaronnguyen/TN/App/doctieuthuyet/pending_novel_11_temp.json"
FINAL_PATH = "/Users/aaronnguyen/TN/App/doctieuthuyet/pending_novel_11.json"

def txt_to_html(text_block):
    lines = [line.strip() for line in text_block.strip().split("\n") if line.strip()]
    paragraphs = []
    for line in lines:
        paragraphs.append(f"<p>{line}</p>")
    return "\n".join(paragraphs)

intro = """<strong>"Cậu chỉ là thằng đạo diễn quèn từ Cần Giờ, không có Hãng phim Thiên Nam thì kịch bản của cậu chỉ là giấy lộn!"</strong>
Bị gã sản xuất tráo trở cướp đi kịch bản dốc lòng viết suốt ba năm, đạo diễn Lý Quốc Anh bị đẩy vào đường cùng, gán mác đạo nhái và cấm cửa khỏi giới điện ảnh.
Nhưng gã không biết, anh đã gặp Hoàng Bảo Trân – nữ hoàng màn ảnh kiêm Chủ tịch Hiệp hội Điện ảnh Việt Nam, người nhìn ra thiên tài ẩn dật dốc toàn lực đầu tư cho anh.
Tại phim trường hoang sơ Cần Giờ, một kiệt tác điện ảnh mới được thai nghén, sẵn sàng đập tan mọi xiềng xích truyền thông bẩn và chấn động cả thảm đỏ Cannes!"""

# ----------------- CHAPTER 1 -----------------
c1_title = "Chương 1: Kịch Bản Bị Cướp"
c1_text = """Nắng chiều Sài Gòn hắt qua những ô kính cường lực của tòa nhà văn phòng Hãng phim Thiên Nam tại trung tâm Quận 1.
Lý Quốc Anh đứng lặng người trước chiếc bàn làm việc bằng gỗ gõ đỏ bóng loáng của gã giám đốc sản xuất Trần Thế Sơn.
On mặt bàn, xấp kịch bản dày cộp mang tên "Bão Cát Cần Giờ" bị vứt chỏng chơ, góc giấy hơi quăn lại vì những ngón tay siết chặt của Quốc Anh suốt ba năm qua.
Trần Thế Sơn tựa lưng vào chiếc ghế da Brioni sang trọng, khói xì-gà từ điếu Cohiba trên ngón tay đeo nhẫn kim cương của gã phả ra thành những vòng tròn màu xám đục.
Ngồi kế bên gã là đạo diễn Ngô Quang Đạt – kẻ nổi tiếng trong giới with những bộ phim mì ăn liền hài nhảm rẻ tiền nhưng đầy mưu mô.
"Quốc Anh này, tôi đã xem qua kịch bản của cậu rồi," Thế Sơn gạt tàn thuốc, giọng gã thản nhiên đến mức tàn nhẫn.
"Nhưng ban giám đốc quyết định bộ phim này sẽ do anh Đạt đây đứng tên đạo diễn chính, còn cậu... cậu có thể làm phó đạo diễn hiện trường nếu muốn."
Lý Quốc Anh cảm thấy máu trong người như đông cứng lại, hai tai anh bắt đầu lùng bùng như tiếng sóng biển gầm rú.
"Anh Sơn, anh nói cái gì?" Quốc Anh gằn giọng, bàn tay bấu chặt vào mép bàn gỗ đến mức các đầu ngón tay trắng bệch.
"Kịch bản này tôi viết suốt ba năm, lặn lội từng góc rừng ngập mặn Cần Giờ, phơi nắng phơi sương để có từng con chữ, sao anh có thể đưa cho người khác?"
Ngô Quang Đạt cười nhạt, gã nhấp một ngụm trà ô long hảo hạng rồi chỉnh lại chiếc gọng kính đen dày cộp trên sống mũi.
"Quốc Anh à, cậu còn trẻ quá, tư duy điện ảnh nghệ thuật kiểu này không bán được vé đâu," Đạt nói bằng giọng dạy đời trịch thượng.
"Tôi đứng tên là để cứu bộ phim này, giúp nó có cơ hội ra rạp, chứ để cậu làm thì chỉ có nước mang đi triển lãm cho gián xem."
Trần Thế Sơn nhếch mép cười nửa miệng, gã rút từ trong hộc tủ ra một tập tài liệu mỏng rồi ném mạnh trước mặt Quốc Anh.
Tập tài liệu trượt dài trên mặt bàn gỗ bóng loáng, đập thẳng vào ngực Quốc Anh như một đòn cảnh cáo vô hình.
"Bản thỏa thuận chấm dứt hợp đồng lao động và bàn giao toàn bộ quyền tác giả của kịch bản Bão Cát Cần Giờ," Sơn gõ ngón tay lên tập hồ sơ.
"Cậu ký vào đây, tôi sẽ cho cậu năm mươi triệu đồng coi như tiền hỗ trợ mất việc, nếu không ký... cậu tự hiểu hậu quả."
"Năm mươi triệu?" Quốc Anh bật cười cay đắng, nước mắt phẫn uất chực trào ra nhưng anh cố nuốt ngược vào trong.
"Đây là tác phẩm tâm huyết của đời tôi, tôi đã đăng ký bản quyền tác giả tại Cục Bản quyền tác giả từ năm ngoái!"
Trần Thế Sơn cười phá lên, tiếng cười của gã vang vọng khắp căn phòng làm việc rộng lớn, lạnh lẽo và đầy khinh bỉ.
"Bản quyền tác giả? Cậu quên là cậu ký hợp đồng lao động toàn thời gian với Thiên Nam à?" Sơn nghiêng người tới trước, ánh mắt gã sắc lẹm như dao.
"Theo luật sở hữu trí tuệ Việt Nam, cậu là người sáng tạo, nhưng Thiên Nam mới là chủ sở hữu quyền tác giả vì chúng tôi trả lương cho cậu."
"Chưa hết đâu," Ngô Quang Đạt bồi thêm một đòn tàn độc, gã đưa chiếc máy tính bảng ra trước mặt Quốc Anh.
On màn hình là một bài báo lá cải vừa lên trang với dòng tít lớn: "Đạo diễn trẻ Lý Quốc Anh bị tố đạo nhái kịch bản từ phim độc lập Hàn Quốc."
Bài viết sử dụng những hình ảnh so sánh khập khiễng, cố tình bôi nhọ Quốc Anh để hủy hoại danh tiếng vừa chớm nở của anh trong giới.
"Cậu nhìn đi, danh tiếng đạo nhái thế này thì ai dám dùng cậu nữa?" Đạt cười khinh khỉnh, vuốt lại mái tóc vuốt keo bóng lộn.
"Ký đi Quốc Anh, ký để giữ lại chút thể diện cuối cùng, và để khỏi phải hầu tòa vì tội vi phạm bản quyền và bôi nhọ hãng phim."
Mồ hôi lạnh chảy ròng ròng dọc sống lưng Quốc Anh, tay anh run rẩy đến mức không thể kiểm soát nổi nhịp thở của mình.
Anh nhìn hai gương mặt tráo trở trước mắt – một gã tư bản dùng tiền và kẽ hở luật pháp để cướp đoạt chất xám, một kẻ tiểu nhân hám danh đoạt lợi.
Anh nhận ra tất cả đã được chúng lên kế hoạch từ trước, từ việc dụ anh ký hợp đồng lao động đến việc tung bài báo bôi nhọ để ép anh vào đường cùng.
"Các người..." Quốc Anh nghiến răng kèn kẹt, gân xanh trên cổ nổi lên cuồn cuộn như những con giun đất dưới mưa.
"Tôi sẽ không ký bất cứ thứ gì, và tôi sẽ bắt các người phải trả giá gấp trăm lần cho sự tráo trở ngày hôm nay!"
Trần Thế Sơn đứng bật dậy, nụ cười trên mặt gã biến mất, thay vào đó là sự lạnh lùng tột độ của kẻ nắm quyền sinh sát trong tay.
"Bảo vệ! Đuổi thằng này ra ngoài và cấm cửa nó khỏi tòa nhà này vĩnh viễn!" Sơn hét lớn vào chiếc điện thoại nội bộ.
Hai nhân viên bảo vệ to cao nhanh chóng bước vào, nắm chặt lấy vai Quốc Anh và lôi anh đi dọc hành lang lộng lẫy của Thiên Nam.
Quốc Anh bị ném ra khỏi sảnh tòa nhà văn phòng, ngã nhào xuống nền đá granite nóng bỏng dưới cái nắng oi bức của Sài Gòn.
Người qua đường nhìn anh chỉ trỏ, vài phóng viên đứng sẵn bên ngoài bắt đầu đưa máy ảnh lên bấm tách tách liên tục.
Anh đứng dậy, phủi vội bụi cát bám trên chiếc quần jean bạc màu, ánh mắt anh nhìn trân trân vào logo Hãng phim Thiên Nam rực rỡ phía trên cao.
Bàn tay anh nắm chặt đến mức móng tay găm sâu vào lòng bàn tay, rớm máu đỏ tươi hòa cùng bụi bẩn ven đường.
"Trần Thế Sơn, Ngô Quang Đạt," Quốc Anh thì thầm trong tiếng gầm rú của dòng xe cộ Sài Gòn nhộn nhịp.
"Tôi thề sẽ quay lại, và khi đó, tôi sẽ khiến các người phải quỳ xuống trước mặt tôi trên đại lộ điện ảnh!"
Lúc này, anh chỉ có một mình, danh tiếng bị hủy hoại, không tiền bạc, không kịch bản, chỉ còn lại sự căm hận tột cùng nung nấu trong tim.
Anh quay lưng bước đi, bóng dáng đơn độc chìm dần vào dòng người hối hả dưới cái nắng oi nồng của thành phố điện ảnh đầy nghiệt ngã này."""

# ----------------- CHAPTER 2 -----------------
c2_title = "Chương 2: Gặp Gỡ Định Mệnh"
c2_text = """Cơn mưa giông chiều hè bất chợt đổ ập xuống vùng đất rừng ngập mặn Cần Giờ, xóa nhòa ranh giới giữa bầu trời và mặt biển xám xịt.
Lý Quốc Anh ngồi đơn độc dưới mái lá ọp ẹp của một quán nước ven sông Lòng Tàu, tay xoay xoay ly trà đá đã loãng toẹt vì nước mưa rơi vào.
Trước mặt anh là cuốn sổ tay nháp rách nát, những dòng kịch bản mới viết bằng mực xanh đã bị nước mưa thấm vào, nhòe nhoẹt như vết nước mắt.
Suốt hai tuần qua, sau khi bị Thiên Nam đuổi cổ, không một hãng phim nào ở Sài Gòn dám nhận anh, tất cả đều e ngại cái mác "đạo nhái" mà Thế Sơn đã gán ghép.
Anh đã dạt về Cần Giờ – nơi anh từng dành hàng tháng trời để lấy chất liệu thực tế – như một con thú bị thương tìm về hang ổ để liếm vết thương.
Tiếng lốp xe ô tô nghiến trên nền đất cát sũng nước vang lên cắt ngang tiếng mưa rơi lộp bộp trên mái lá.
Một chiếc Range Rover màu đen bóng loáng dừng lại trước quán nước nghèo nàn, ánh đèn pha led xé toạc màn mưa trắng xóa.
Cửa xe mở ra, một người phụ nữ bước xuống dưới chiếc ô đen lớn do tài xế che chắn, dáng đi của cô toát lên vẻ sang trọng và quyền lực tuyệt đối.
Cô mặc chiếc măng-tô dáng dài màu cát, mái tóc đen gợn sóng xõa ngang vai, đôi mắt phượng sắc sảo lướt nhanh qua quán nước rồi dừng lại ở Quốc Anh.
Đó là Hoàng Bảo Trân – nữ diễn viên điện ảnh xuất chúng kiêm Chủ tịch Hiệp hội Điện ảnh Việt Nam, người vừa từ Liên hoan phim quốc tế trở về.
Bảo Trân bước vào quán, gót giày cao gót màu đỏ nện nhẹ trên nền đất nện ẩm ướt, mang theo hương nước hoa Chanel nồng nàn lấn át mùi bùn đất Cần Giờ.
Cô không ngần ngại ngồi xuống chiếc ghế nhựa màu xanh cũ kỹ đối diện Quốc Anh, đôi mắt phượng nhìn thẳng vào gương mặt phờ phạc của đạo diễn trẻ.
"Lý Quốc Anh, đạo diễn xuất sắc nhất khóa K18 Đại học Sân khấu Điện ảnh TP.HCM, người bị Thiên Nam cướp kịch bản và bôi nhọ," Trân mở lời, giọng cô trầm ấm nhưng đầy uy lực.
Quốc Anh ngước nhìn cô, đôi mắt anh đỏ ngầu vì thiếu ngủ và men rượu đế rẻ tiền mà anh vừa uống trước đó.
"Hoàng Bảo Trân... chị tìm một kẻ thất bại, mang danh đạo nhái như tôi để làm gì?" Quốc Anh cười tự giễu, định gấp cuốn sổ tay lại.
Bảo Trân nhanh tay giữ lấy cuốn sổ, cô lật từng trang giấy ẩm ướt, đôi mắt chăm chú đọc những dòng chữ viết tay nguệch ngoạc của anh.
Mười phút trôi qua trong im lặng, chỉ có tiếng mưa bão gầm rú bên ngoài và tiếng thở dài nhẹ của người tài xế đứng che ô ngoài cửa.
"Kịch bản này..." Bảo Trân ngẩng lên, ánh mắt cô sáng rực như những ngôi sao đêm trên bầu trời Cannes.
"Nó xuất sắc hơn nhiều so với Bão Cát Cần Giờ bị cướp. Đây mới thực sự là hơi thở của đất rừng ngập mặn, là linh hồn của những con người lam lũ nơi đây."
"Nhưng tôi không có tiền, không có ê-kíp, và quan trọng nhất là tôi bị cấm cửa," Quốc Anh cúi đầu, bàn tay anh run nhẹ dưới gầm bàn.
Bảo Trân gấp cuốn sổ lại, cô đẩy chiếc kính râm lên đầu, để lộ gương mặt đẹp không góc chết với thần thái của một nữ vương điện ảnh.
"Cậu bị cấm cửa bởi Trần Thế Sơn, nhưng gã không phải là cả nền điện ảnh Việt Nam này," Trân nghiêng người tới trước, giọng cô đầy kiên quyết.
"Hiệp hội Điện ảnh Việt Nam do tôi làm chủ tịch sẽ đứng ra bảo trợ pháp lý cho cậu, bảo chứng rằng cậu hoàn toàn trong sạch trước vụ vu cáo đạo nhái."
"Và tôi – với tư cách cá nhân – sẽ đầu tư mười tỷ đồng để cậu thực hiện bộ phim này ngay tại phim trường Cần Giờ," Trân nói, đặt lên bàn một tấm thẻ ngân hàng VIP màu đen.
Quốc Anh sững sờ, anh nhìn tấm thẻ đen lấp lánh dưới ánh đèn dây tóc vàng vọt của quán nước, rồi nhìn vào đôi mắt phượng kiên định của Bảo Trân.
"Chị tin tôi đến vậy sao? Mười tỷ không phải là con số nhỏ cho một canh bạc với một đạo diễn bị ruồng bỏ," anh hỏi, giọng nghẹn lại.
Bảo Trân mỉm cười, một nụ cười đầy kiêu hãnh và mưu mô, nụ cười của một người phụ nữ đã đứng trên đỉnh cao quyền lực của giới nghệ thuật.
"Tôi không cá cược vào cậu, tôi cá cược vào tài năng của cậu và sự căm hận của chúng ta đối với những kẻ tráo trở," Trân gằn giọng, ánh mắt cô lạnh đi.
"Trần Thế Sơn và Ngô Quang Đạt đang tự đắc với bộ phim cướp của cậu, chúng chuẩn bị bấm máy hoành tráng tại phim trường quận 9."
"Tôi muốn cậu quay bộ phim mới này, đập tan bộ phim của chúng ngay trên mặt trận nghệ thuật, đưa tác phẩm này ra thế giới."
"Tôi không chỉ muốn cứu danh tiếng của cậu, Lý Quốc Anh, tôi muốn cùng cậu bước đi trên thảm đỏ Cannes và giật giải thưởng lớn nhất!"
Lời nói của Bảo Trân như một luồng điện mạnh chạy dọc sống lưng Quốc Anh, đánh thức ngọn lửa nghệ thuật tưởng chừng đã tắt ngóm trong lòng anh.
Anh đứng dậy, nhìn ra dòng sông Lòng Tàu đang cuộn sóng đục ngầu dưới cơn mưa bão, lồng ngực phập phồng vì một cảm xúc mãnh liệt chưa từng có.
"Được!" Quốc Anh quay lại nhìn Bảo Trân, đôi mắt anh không còn sự đờ đẫn của kẻ thất bại mà rực cháy ý chí chiến đấu.
"Bộ phim mới sẽ mang tên 'Tiếng Thét Của Rừng Sác'. Tôi sẽ bắt đầu tuyển ê-kíp ngay trong đêm nay, quay tại chính mảnh đất Cần Giờ này!"
Bảo Trân đứng dậy, cô chìa tay ra trước mặt anh, bàn tay mềm mại nhưng chứa đựng sức mạnh có thể xoay chuyển cả giới điện ảnh.
"Hợp tác vui vẻ, đạo diễn Lý Quốc Anh. Kể từ hôm nay, Hoàng Bảo Trân tôi sẽ là nữ chính và là hậu phương vững chắc nhất của cậu."
Quốc Anh nắm lấy tay cô, cảm nhận được hơi ấm và sự kiên định truyền qua lòng bàn tay, xua tan đi cái lạnh lẽo của cơn mưa bão Cần Giờ.
Bên ngoài, mưa bắt đầu ngớt dần, một vệt sáng yếu ớt của ánh hoàng hôn xé toạc mây đen, rọi xuống dòng sông lòng tàu như một điềm báo về một cuộc lật kèo vĩ đại."""

# ----------------- CHAPTER 3 -----------------
c3_title = "Chương 3: Khởi Quay Trong Bão Táp"
c3_text = """Bình minh lên trên phim trường Cần Giờ hoang sơ, nắng sớm trải dài trên những cánh rừng đước bạt ngàn ngập mặn và những bãi bùn đen loang loáng nước.
Lý Quốc Anh đứng cạnh chiếc máy quay Arri Alexa cũ kỹ thuê lại từ một người bạn thân học khóa dưới – thiết bị tốt nhất anh có thể kiếm được với kinh phí eo hẹp.
Ê-kíp của anh chỉ vỏn vẹn mười lăm người: vài người bạn trung thành từ thời đại học, những người dân địa phương Cần Giờ nhận làm hậu cần, và Hoàng Bảo Trân.
"Mọi người chuẩn bị! Cảnh một, phân đoạn một: Tiếng gọi từ rừng đước!" Quốc Anh hô lớn qua chiếc loa cầm tay bạc màu.
Dù trang thiết bị thiếu thốn, nhưng không khí trong đoàn phim vô cùng nghiêm túc, từng góc máy, từng tấm phản quang đều được bố trí tỉ mỉ dưới sự chỉ đạo của anh.
Giữa lúc đoàn phim đang chuẩn bị bấm máy cảnh quay đầu tiên, tiếng động cơ gầm rú của ba chiếc xe bán tải màu đen vang lên từ phía đường lộ cát.
Xe dừng lại, bụi cát tung bay mù mịt làm đảo lộn cả hiện trường quay phim hoang sơ bên bờ sông.
Bước xuống xe là hơn chục gã đàn ông xăm trổ đầy mình, dẫn đầu bởi Đinh Hùng – trợ lý đắc lực của Trần Thế Sơn tại Hãng phim Thiên Nam.
"Ai cho các người quay phim ở đây?" Đinh Hùng hất hàm, gã cầm một tập tài liệu bước tới giật phắt chiếc loa cầm tay từ tay Quốc Anh.
"Khu vực rừng đước này đã được Hãng phim Thiên Nam thuê trọn gói để làm bối cảnh phụ cho phim 'Hương Phù Sa Ấm Áp' từ tháng trước."
"Đây là giấy tờ thuê đất của Ủy ban nhân dân huyện Cần Giờ cấp cho chúng tôi, yêu cầu các người dọn dẹp đồ đạc và cút khỏi đây ngay lập tức!"
Quốc Anh bước lên, mặt anh lạnh tanh, ánh mắt anh nhìn thẳng vào gã trợ lý hống hách không một chút sợ hãi.
"Giấy tờ này chỉ ghi thuê bối cảnh phân khu A, còn hiện trường của chúng tôi là phân khu B hoang dã, các người không có quyền đuổi chúng tôi," Quốc Anh gằn giọng.
"Hơn nữa, chúng tôi đã xin phép ban quản lý rừng phòng hộ Cần Giờ đầy đủ bằng văn bản pháp lý hợp pháp!"
Đinh Hùng cười sằng sặc, gã giơ chân đạp đổ một chiếc chân đèn phản quang bằng nhôm khiến tấm phản quang rơi xuống bãi bùn đen sũng nước.
"Pháp lý? Ở cái đất điện ảnh này, tiền của Thiên Nam là pháp lý!" Hùng chỉ tay vào mặt Quốc Anh, giọng đầy đe dọa.
"Thằng đạo nhái như mày mà cũng đòi làm phim à? Tao nói cho mày biết, không ai ở Việt Nam này dám phát hành phim của mày đâu!"
"Ai nói không ai dám phát hành?"
Một giọng nói lạnh lùng, sang trọng vang lên từ phía sau cabin thay đồ tạm bợ của đoàn phim.
Hoàng Bảo Trân bước ra, cô đã hóa trang xong cho vai diễn nữ chính – một phụ nữ Cần Giờ lam lũ nhưng kiên cường với chiếc áo bà ba đen cát sũng nước.
Dù mặc đồ giản dị, nhưng thần thái và uy quyền của Chủ tịch Hiệp hội Điện ảnh VN khiến Đinh Hùng và đám tay chân lập tức sững sờ, lùi lại một bước.
"Hoàng... chị Trân?" Đinh Hùng lắp bắp, mồ hôi hột bắt đầu rịn ra trên trán gã.
"Đinh Hùng, cậu về bảo với Trần Thế Sơn rằng nếu gã muốn dùng luật rừng ở Cần Giờ này, tôi sẽ đích thân gửi công văn lên Sở Văn hóa và Thể thao TP.HCM," Trân nói, giọng cô sắc như dao cạo.
"Hiệp hội Điện ảnh VN đang giám sát dự án 'Tiếng Thét Của Rừng Sác' này dưới danh nghĩa tác phẩm nghệ thuật trọng điểm của năm."
"Bất kỳ hành vi cản trở, phá hoại nào của các người đều sẽ được đưa ra ánh sáng truyền thông và pháp luật hình sự!"
Đinh Hùng mặt tái mét, gã liếc nhìn chiếc camera hành trình trên xe bán tải của mình, rồi nhìn vào đôi mắt phượng đầy sát khí của Bảo Trân.
Gã biết Trần Thế Sơn có tiền, nhưng Hoàng Bảo Trân lại có tầm ảnh hưởng chính trị và xã hội cực lớn trong giới nghệ thuật nước nhà mà Sơn không thể xem thường.
"Chúng tôi... chúng tôi chỉ làm theo lệnh," Đinh Hùng nói lý nhí, gã nhặt chiếc loa cầm tay trả lại cho Quốc Anh rồi vẫy tay ra hiệu cho đám đàn em rút lui.
Ba chiếc xe bán tải quay đầu, rồ ga chạy trốn, để lại những vệt bánh xe sâu hoắm trên nền cát sũng nước và bầu không khí im ắng trở lại.
Quốc Anh quay sang nhìn Bảo Trân, anh thấy bờ vai cô hơi run nhẹ – không phải vì sợ, mà vì sự phẫn uất trước những thủ đoạn bẩn thỉu của đối thủ.
"Cảm ơn chị Trân," Quốc Anh nói, giọng anh trầm xuống, đầy sự kính trọng.
"Đừng cảm ơn tôi, Quốc Anh," Trân nhìn anh, tay cô vuốt lại mái tóc giả của nhân vật. "Bọn chúng sẽ không dừng lại ở đây đâu."
"Trần Thế Sơn rất xảo quyệt, gã sẽ dùng truyền thông bẩn để bôi nhọ chúng ta trên các trang mạng xã hội và báo điện tử lớn."
"Chúng ta phải quay thật nhanh, mỗi thước phim phải là một nhát dao chí mạng găm thẳng vào sự kiêu ngạo của chúng!"
Quốc Anh gật đầu chắc nịch, anh bước lại sau máy quay, điều chỉnh góc máy hướng thẳng ra dòng sông lấp lánh nắng sớm.
"Mọi người chuẩn bị! Cảnh một, phân đoạn một, bấm máy!" tiếng hô của Quốc Anh vang vọng khắp cánh rừng đước hoang sơ.
Tiếng máy quay Arri Alexa cũ kỹ chạy rè rè bắt đầu ghi lại những thước phim đầu tiên của "Tiếng Thét Của Rừng Sác".
Bất chấp bão táp truyền thông và sự phá hoại của đối thủ, ngọn lửa sáng tạo của đạo diễn trẻ bị ruồng bỏ đã chính thức bùng cháy tại mảnh đất Cần Giờ lộng gió này."""

if __name__ == "__main__":
    print("Stage 1 definition loaded successfully.")
