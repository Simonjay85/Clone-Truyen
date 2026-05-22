# -*- coding: utf-8 -*-
import json

TEMP_PATH = "/Users/aaronnguyen/TN/App/doctieuthuyet/pending_novel_11_temp.json"

def txt_to_html(text_block):
    lines = [line.strip() for line in text_block.strip().split("\n") if line.strip()]
    paragraphs = []
    for line in lines:
        paragraphs.append(f"<p>{line}</p>")
    return "\n".join(paragraphs)

c4_title = "Chương 4: Sự Kiên Trì Của Đạo Diễn Tài Hoa"
c4_text = """Cái nóng tháng năm của vùng ngập mặn Cần Giờ hầm hập phả lên từ những bãi bùn đen, mang theo mùi mặn chát của muối biển và mùn gỗ mục.
Lý Quốc Anh đứng ngập chân dưới bùn lầy sâu đến đầu gối, bàn tay bám chặt vào chân máy quay Arri Alexa để giữ thăng bằng trước dòng nước triều đang dâng.
Gương mặt anh sạm đen vì nắng gió Cần Giờ, đôi mắt trũng sâu vì nhiều đêm liền thức trắng bên đống tư liệu và những bản phân cảnh viết tay.
Xung quanh anh, mười lăm thành viên ê-kíp nhỏ cũng đang vật lộn với đống phản quang, dây cáp điện sũng nước sông và những chiếc đèn nhỏ.
"Chị Trân, cảnh này nhân vật nữ chính phải đi chân đất qua bãi rễ đước nhọn, chị có cần mang dép bảo hộ không?" Quốc Anh hỏi lớn.
Hoàng Bảo Trân đứng bên gốc cây đước già, cô lắc đầu, vén tà áo bà ba sũng nước rồi bước thẳng xuống bãi sình lầy đen ngòm.
"Không cần đâu Quốc Anh, nhân vật của tôi là người con gái của rừng Sác, cô ấy phải thuộc về mảnh đất này từng tấc da tấc thịt," Trân nói.
Đôi chân trần của nữ diễn viên nổi tiếng lún sâu vào bùn lạnh, rễ đước nhọn cào nhẹ vào da thịt cô nhưng Trân không hề nhíu mày một cái.
Mồ hôi chảy dài trên trán Quốc Anh, nhưng ánh mắt anh nhìn qua ống kính ngập tràn sự kính trọng và xúc động trước sự tận hiến của cô.
Một diễn viên hạng A, người từng đứng trên thảm đỏ sang trọng ở các sự kiện quốc tế lớn, giờ đây đang chịu đựng cái lạnh, cái dơ của Cần Giờ không một lời phàn nàn.
Sự đồng điệu giữa đạo diễn trẻ và nữ hoàng màn ảnh ngày càng khăng khít hơn qua từng cảnh quay, từng buổi tối bàn thảo kịch bản dưới ánh đèn dầu.
Họ không cần nói nhiều, chỉ một ánh mắt nhìn nhau ở hiện trường là đủ để cả hai hiểu đối phương đang muốn truyền tải thông điệp gì vào thước phim.
Trong khi đoàn phim nhỏ đang kiên cường bám trụ giữa rừng đước hoang sơ, thì tại Sài Gòn phồn hoa, một thế giới khác hoàn toàn đang diễn ra.
Hãng phim Thiên Nam tổ chức buổi họp báo ra mắt dự án "Hương Phù Sa Ấm Áp" tại một khách sạn năm sao vô cùng hoành tráng ở Quận 1.
Dưới ánh đèn flash sáng lóa của hàng trăm phóng viên, Trần Thế Sơn và Ngô Quang Đạt đứng bên cạnh dàn diễn viên ngôi sao mặc đồ hiệu lộng lẫy.
"Bộ phim của chúng tôi là tác phẩm nghệ thuật đỉnh cao, được đầu tư kinh phí lên tới ba mươi tỷ đồng," Trần Thế Sơn phát biểu tự tin trước micro.
"Chúng tôi tự tin 'Hương Phù Sa Ấm Áp' sẽ đại diện Việt Nam tham gia tranh giải Oscar năm tới và càn quét các liên hoan phim quốc tế."
Một phóng viên báo điện tử đứng dậy hỏi: "Thưa anh Sơn, có tin đồn đạo diễn trẻ Lý Quốc Anh đang thực hiện một bộ phim độc lập tại Cần Giờ để đối đầu?"
Ngô Quang Đạt cười nhạt, gã giật lấy chiếc micro từ tay Thế Sơn, nụ cười trên mặt đầy sự khinh bỉ và trịch thượng thường ngày.
"Tôi không quan tâm đến những kẻ đạo nhái mang danh làm phim nghệ thuật nhưng thực chất chỉ quay những thước phim rác rưởi," Đạt nói bằng giọng cay độc.
"Điện ảnh không dành cho những kẻ nghèo nàn cả về tiền bạc lẫn tư duy, bộ phim đó của cậu ta chắc chỉ chiếu cho gián xem ở bãi rác Cần Giờ thôi."
Tiếng cười rộ lên khắp phòng họp báo xa hoa của Thiên Nam, những lời chế giễu ác ý nhanh chóng được các trang báo mạng đăng tải thành dòng tít lớn.
Quốc Anh đọc được những bài báo đó qua chiếc điện thoại cũ nát vào tối muộn, khi cả đoàn phim đang ăn cơm hộp rẻ tiền dưới hiên nhà sàn lợp lá dừa dột nát.
Anh không nói một lời, chỉ lặng lẽ cất điện thoại vào túi, nắm chặt bàn tay đến mức các khớp xương kêu răng rắc dưới bóng đêm Cần Giờ.
Bảo Trân bước đến cạnh anh, cô đặt lên vai anh một tấm khăn ấm, đôi mắt phượng nhìn ra dòng sông Lòng Tàu lấp lánh ánh trăng khuya.
"Đừng để những lời rác rưởi đó làm phiền cậu, Quốc Anh," Trân nói nhẹ nhàng nhưng giọng cô tràn đầy sự kiên định và lạnh lùng đối với kẻ thù.
"Càng bị chế giễu, chúng ta càng phải làm ra một kiệt tác khiến chúng phải câm miệng vĩnh viễn và quỳ xuống trước mặt cậu!"
Quốc Anh ngước nhìn cô, dưới ánh trăng mờ, gương mặt Bảo Trân đẹp như một vị thần hộ mệnh đang che chở cho ngọn lửa nghệ thuật của đời anh.
"Tôi hiểu, chị Trân," Quốc Anh gật đầu, lòng anh dâng lên một luồng sinh khí mới, xua tan đi mọi sự mệt mỏi và uất hận trong lòng.
"Ngày mai chúng ta sẽ thực hiện cảnh quay khó nhất, cảnh cơn bão trên sông. Tôi sẽ cho cả thế giới thấy tiếng thét thực sự của rừng Sác!"
Gió đêm Cần Giờ thổi mạnh, rặng đước già xào xạc như tiếng reo hò cổ vũ cho những con người kiên cường đang âm thầm chuẩn bị cho một cuộc lật kèo vĩ đại."""

c5_title = "Chương 5: Đòn Truyền Thông Bẩn"
c5_text = """Bão tố thực sự không chỉ diễn ra ngoài biển Cần Giờ, mà nó đã càn quét qua không gian mạng Sài Gòn ngay trước khi bộ phim đóng máy.
Sáng thứ Năm, một chiến dịch truyền thông bẩn quy mô lớn bất ngờ nổ ra nhắm thẳng vào Lý Quốc Anh và dự án "Tiếng Thét Của Rừng Sác".
Hàng loạt trang fanpage lớn về điện ảnh đồng loạt chia sẻ những đoạn video ngắn (footage) chưa qua chỉnh sửa màu sắc và âm thanh của bộ phim.
Những đoạn video bị cắt ghép ác ý, cố tình bôi nhọ chất lượng mỹ thuật của phim là "thảm họa điện ảnh", "phim cấp ba rẻ tiền bôi bẩn hình ảnh Cần Giờ".
Cùng lúc đó, Hãng phim Thiên Nam tung ra đơn tố cáo gửi lên Cục Bản quyền tác giả và Thanh tra Bộ Văn hóa, Thể thao và Du lịch.
Đơn kiện cáo buộc Lý Quốc Anh sử dụng trái phép các thiết kế mỹ thuật và phân cảnh cốt truyện thuộc sở hữu độc quyền của Thiên Nam từ dự án bị cướp.
"Anh Quốc Anh, cục Bản quyền tác giả vừa gửi văn bản khẩn yêu cầu chúng ta đình chỉ ngay lập tức việc ghi hình để phục vụ công tác thanh tra!"
Người bạn thân DP của Quốc Anh chạy vào hiện trường, mặt cắt không còn một giọt máu, tay cầm chiếc điện thoại hiển thị văn bản đóng dấu đỏ.
Ê-kíp nhỏ lập tức xôn xao, sự hoang mang lộ rõ trên khuôn mặt mệt mỏi của những người dân địa phương và các bạn sinh viên trẻ.
Mồ hôi lạnh chảy ròng ròng dọc thái dương Quốc Anh, anh đứng lặng người giữa bãi cát Cần Giờ, cảm giác như một bàn tay vô hình lại bóp nghẹt cổ anh.
Trần Thế Sơn và Ngô Quang Đạt thật tráo trở, chúng không chỉ cướp kịch bản mà còn dùng quyền lực hành chính để triệt hạ con đường sống cuối cùng của anh.
Giữa lúc cả đoàn phim đang đứng bên bờ vực sụp đổ, Hoàng Bảo Trân bước lên phía trước, gương mặt cô lạnh lùng như băng đá ngàn năm.
"Mọi người cứ tiếp tục chuẩn bị bối cảnh, không ai được phép dừng lại!" Trân ra lệnh bằng giọng đầy uy quyền của một vị chủ tịch.
Cô rút điện thoại di động ra, bấm một số gọi trực tiếp cho Chánh Thanh tra Bộ Văn hóa, Thể thao và Du lịch – người cô quen biết từ lâu trong các sự kiện nhà nước.
"Alo, chú Minh ạ? Cháu Trân đây chú," giọng cô ngọt ngào nhưng chứa đựng sự đanh thép của kẻ đang nắm giữ lẽ phải trong tay.
"Về công văn khẩn đối với dự án 'Tiếng Thét Của Rừng Sác', cháu muốn báo cáo với chú rằng đây là một âm mưu triệt hạ nghệ thuật độc lập của Thiên Nam."
"Hiệp hội Điện ảnh VN đang sở hữu toàn bộ bằng chứng chứng minh kịch bản này được đăng ký nháp và có lịch sử sáng tác trước khi Thiên Nam ký hợp đồng với Quốc Anh."
"Cháu sẽ đích thân mang toàn bộ hồ sơ pháp lý lên Bộ trong chiều nay để làm sáng tỏ mọi việc, kính mong chú xem xét lại lệnh đình chỉ tạm thời này."
Sau khi cúp máy, Bảo Trân quay sang nhìn Quốc Anh, cô nắm lấy bàn tay đang run nhẹ vì phẫn uất của đạo diễn trẻ, siết chặt lấy.
"Quốc Anh, cậu cứ tập trung quay cho xong những cảnh cuối cùng ở đây. Mọi việc pháp lý ở Sài Gòn, Hoàng Bảo Trân tôi sẽ gánh vác hết cho cậu!"
"Luật sư Đỗ Minh Trí của Hiệp hội đã thu thập đầy đủ chứng từ chuyển khoản và lịch sử chỉnh sửa kịch bản trên máy tính cũ của cậu từ hai năm trước."
"Chúng ta không chỉ chứng minh mình vô tội, chúng ta sẽ kiện ngược lại Thiên Nam tội xâm phạm quyền tác giả và vu khống bôi nhọ danh dự!"
Lời nói của Bảo Trân như một tấm khiên vững chắc che chở cho Quốc Anh trước cơn bão táp truyền thông bẩn thỉu đang bủa vây xung quanh.
Anh nhìn vào đôi mắt phượng kiên định của cô, lòng ngập tràn sự biết ơn và một niềm tin mãnh liệt rằng công lý sẽ được thực thi.
"Tôi hiểu rồi, chị Trân," Quốc Anh gằn giọng, ánh mắt anh rực sáng ý chí chiến đấu sắt đá của một thiên tài bị dồn vào đường cùng.
"Tôi sẽ quay cảnh cuối cùng ngay trong đêm nay, bất chấp mọi thứ. Kiệt tác này phải được hoàn thành trọn vẹn nhất!"
Chiều hôm đó, Bảo Trân lên chiếc Range Rover trở về Sài Gòn để trực tiếp đối đầu với đòn pháp lý của Thiên Nam tại văn phòng Thanh tra Bộ.
Tại hiện trường Cần Giờ, Quốc Anh cùng ê-kíp nhỏ làm việc liên tục dưới cái nắng gay gắt rồi đến những cơn gió lạnh buốt của đêm muộn ngập mặn.
Từng thước phim được ghi lại dưới sự giám sát nghiêm ngặt của anh, từng chi tiết nhỏ nhất đều được chăm chút bằng tất cả sự phẫn uất và đam mê nghệ thuật.
Bão truyền thông bẩn ngoài kia vẫn đang gầm rú, nhưng bên trong rừng đước Cần Giờ lộng gió, một kiệt tác đích thực đang dần thành hình trong sự kiên cường tột cùng."""

c6_title = "Chương 6: Hoàn Thành Kiệt Tác"
c6_text = """Cơn mưa giông lịch sử quét qua Cần Giờ vào một đêm không trăng, tiếng sóng biển gầm rú đập mạnh vào những gốc đước già ngập mặn.
Lý Quốc Anh đứng dưới cơn mưa tầm tã, nước mưa xối xả vào mặt làm nhòe cả mắt kính bảo hộ của anh, nhưng anh không hề chớp mắt một cái.
Trước mặt anh, Hoàng Bảo Trân đang thực hiện cảnh quay đỉnh cao cuối cùng của phim: nhân vật nữ chính gào thét trong bão tố giữa rừng đước hoang dã.
Mái tóc cô rối bời sũng nước mưa, chiếc áo bà ba đen rách vai bám đầy bùn cát Cần Giờ, đôi mắt phượng ngập tràn sự u uất, phẫn nộ và kiên cường tột độ.
"Tiếng Thét Của Rừng Sác! Cắt! Tốt lắm mọi người ơi!" Quốc Anh hét lớn vào chiếc loa cầm tay sũng nước mưa.
Cả ê-kíp nhỏ lập tức vỡ òa trong tiếng reo hò, vài người bạn sinh viên ôm lấy nhau khóc nức nở dưới làn mưa bão lạnh buốt của vùng biển ngập mặn.
Hoàng Bảo Trân bước lên từ bãi sình lầy, vai cô run lên vì lạnh, nhưng nụ cười trên môi cô rạng rỡ và quyến rũ hơn bất kỳ thảm đỏ nào cô từng bước qua.
Quốc Anh vội chạy đến khoác lên vai cô chiếc khăn khô ấm áp, đôi mắt anh long lanh nước mắt – không phải nước mưa, mà là giọt nước mắt của sự hạnh phúc tột cùng.
"Chúng ta đã làm được rồi, chị Trân," Quốc Anh nói, giọng anh nghẹn ngào vì xúc động sau những ngày tháng vật lộn gian khổ.
"Phim đã chính thức đóng máy an toàn. Cảm ơn chị đã luôn đứng phía sau bảo vệ và đồng hành cùng tôi suốt thời gian qua."
Bảo Trân nhìn anh, tay cô nhẹ nhàng lau đi vệt nước mưa trên má anh, nụ cười cô đầy ấm áp và kiêu hãnh của một người đồng hành trung thành.
"Cậu xứng đáng với điều này, Quốc Anh. Bây giờ là lúc chúng ta đưa kiệt tác này vào phòng dựng để hoàn thiện phần hậu kỳ khép kín," Trân nói.
Ngay trong đêm đó, toàn bộ dữ liệu phim được vận chuyển nghiêm ngặt về một phòng dựng hậu kỳ kín đáo tại Quận 3 dưới sự bảo vệ của Hiệp hội.
Suốt một tháng tiếp theo, Quốc Anh gần như sống trong phòng dựng, tự tay cắt từng khung hình, chỉnh sửa từng dải màu sắc và phối hợp thiết kế âm thanh.
Từng thước phim hoang sơ của Cần Giờ qua bàn tay tài hoa của anh hiện lên đẹp đẽ, u uất và đầy tính nghệ thuật nhân văn sâu sắc.
Trong khi đó, Hãng phim Thiên Nam cũng hoàn thành dự án "Hương Phù Sa Ấm Áp" của họ và tổ chức lễ đóng máy vô cùng xa hoa tại khách sạn Rex Quận 1.
Trần Thế Sơn đứng trên sân khấu rực rỡ, gã nâng ly rượu vang đắt tiền, mặt đỏ gay vì tự mãn trước sự vây quanh của báo giới truyền thông.
"Dự án của chúng tôi đã hoàn tất hậu kỳ tại Singapore với chất lượng âm thanh Dolby Atmos đỉnh cao," Sơn tuyên bố đầy hống hách.
"Chúng tôi đã gửi bản dựng thử đến Hội đồng duyệt phim quốc gia để chuẩn bị đại diện Việt Nam tham gia các liên hoan phim quốc tế lớn nhất."
Ngô Quang Đạt đứng kế bên cũng hùa theo: "Bộ phim này sẽ là một cú hích lớn, khẳng định vị thế độc tôn của Thiên Nam trong ngành điện ảnh."
"Còn những kẻ làm phim độc lập nghèo nàn, nhái kịch bản của chúng tôi thì chắc giờ này đang trốn chui trốn lủi vì sợ hầu tòa rồi."
Tiếng cười tự mãn của hai kẻ tráo trở vang vọng khắp khán phòng sang trọng, những lời khoe khoang được đưa tin rầm rộ trên khắp các mặt báo tài chính.
Nhưng chúng không hề biết rằng, ở một phòng dựng nhỏ tại Quận 3, Lý Quốc Anh vừa bấm nút lưu bản dựng hoàn chỉnh cuối cùng của "Tiếng Thét Của Rừng Sác".
Bản dựng phim nghệ thuật đỉnh cao, chứa đựng tất cả tài năng, mồ hôi và lòng kiên cường của đạo diễn trẻ bị ruồng bỏ đã chính thức hoàn thành.
Và Hoàng Bảo Trân đứng cạnh anh, cô cầm trên tay một chiếc phong bì bọc da màu đỏ sang trọng có in logo hình nhánh cọ vàng quý giá.
Đó là thư phản hồi từ Ban giám tuyển của Liên hoan phim quốc tế Cannes danh giá nhất thế giới gửi trực tiếp cho cô với tư cách Chủ tịch Hiệp hội.
"Quốc Anh," Bảo Trân nghiêng đầu, nụ cười cô đầy sự bí ẩn và mưu mô nham hiểm đối với kẻ thù.
"Cơn ác mộng thực sự của Trần Thế Sơn và Ngô Quang Đạt chuẩn bị bắt đầu rồi đây." """

def append_stage_2():
    with open(TEMP_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    data["chapters"].append({"title": c4_title, "content": txt_to_html(c4_text)})
    data["chapters"].append({"title": c5_title, "content": txt_to_html(c5_text)})
    data["chapters"].append({"title": c6_title, "content": txt_to_html(c6_text)})
    
    with open(TEMP_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("Stage 2 completed: Chapters 4-6 appended successfully.")

if __name__ == "__main__":
    append_stage_2()
