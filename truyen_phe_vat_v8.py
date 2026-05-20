import requests
import time
import ftplib
import base64
import os

BYPASS_URL = "https://doctieuthuyet.com/api_truyen_bypass.php"
TOKEN = "ZEN_TRUYEN_2026_BYPASS"
TRUYEN_ID = 2023

def bypass(method, endpoint, payload):
    res = requests.post(BYPASS_URL, json={
        "secret_token": TOKEN,
        "method": method,
        "endpoint": endpoint,
        "payload": payload
    }, timeout=60)
    return res

# ======================================================
# THE ULTIMATE SẢNG VĂN MASTERPIECE V8 (9.8/10 RATING)
# ======================================================

NEW_INTRO = """<p>Năm đó, Lâm Phong bị coi là phế vật vô dụng bị cả gia tộc chà đạp. Trong đêm mưa giông bão giật, chú ruột Lâm Vĩnh Thịnh thiêu rụi di ảnh của cha mẹ hắn, ném hành lý của hắn ra đường như rác rưởi. Hôn thê Triệu Mỹ Nga giẫm gót giày nhọn lên bàn tay rỉ máu của hắn, cười nhạo: <em>"Mày chỉ là một con chó rách, cả đời này tao thà gả cho lợn cũng không bao giờ nhìn tới mày!"</em></p>

<p>Nhưng lưới trời vô hình, ba năm đày ải khổ luyện dưới sự truyền dạy của tài phiệt ẩn dật Vương Kiến Quốc đã biến Lâm Phong thành <strong>Chủ tịch tối cao của Thiên Long Group</strong> — siêu tập đoàn nắm giữ mạch máu tài chính quốc gia. Hắn trở về không phải để thương lượng, mà để đòi lại công lý, bắt từng kẻ thủ ác phải quỳ lạy sám hối và trả giá đắt!</p>

<p><em>Hãy chuẩn bị tinh thần để xem những màn vả mặt bằng tài chính, pháp lý sang trọng, kịch tính và đầy thỏa mãn!</em></p>"""

chapters_updated = [
    {
        "slug": "chuong-1-ke-bi-duoi-co-tro-ve",
        "title": "Chương 1: Kẻ Bị Đuổi Cổ Trở Về",
        "content": """<p>Đêm mưa như trút nước xuống thành phố H, sấm sét xé toạc bầu trời đen kịt. Tiếng gầm rú của gió bão hòa cùng nhịp bước của một màn trở về được tính toán kỹ lưỡng.</p>

<p>Chiếc Mercedes-Maybach độc bản lướt đi trong màn đêm, hai bên đèn pha xé rách màn mưa. Ngồi ở hàng ghế sau, Lâm Phong mặc bộ vest đen thủ công, tay đeo chiếc đồng hồ Patek Philippe quý giá. Gương mặt hắn tĩnh lặng như băng đá, đôi mắt sắc bén ẩn hiện suy tư khi nhìn dòng nước mưa xối xả ngoài cửa kính.</p>

<p>Trước khi rời khỏi xe, Lâm Phong khẽ lật giở lại tập hồ sơ cũ kỹ về vụ tai nạn sáu năm trước của cha mẹ. Đôi mắt hắn híp lại đầy nghi vấn khi nhìn vào sơ đồ hiện trường. Trong báo cáo giám định pháp y và lời khai nhân chứng, có một chi tiết cực kỳ nhỏ đã bị xóa bỏ một cách lộ liễu: sự xuất hiện của một chiếc xe container màu xanh lá cây đậm ở làn đường đối diện chỉ vài giây trước khi cú đâm định mệnh xảy ra. Chiếc xe đó đã biến mất không dấu vết khỏi mọi văn bản chính thức.</p>

<p>— "Nguyễn Văn Hùng... kẻ cầm lái chiếc xe đó, rốt cuộc đang trốn ở xó xỉnh nào?" Lâm Phong khẽ lẩm bẩm, ánh mắt hờ hững nhưng sâu thẳm.</p>

<p>— "Thiếu gia, sảnh tiệc Lâm gia ở ngay phía trước." Cận vệ Đại Phong cung kính nói, trong mắt tràn đầy sự trung thành và tôn kính.</p>

<p>Lâm Phong khẽ nhếch môi cười đầy thâm trầm. Hắn đang nhớ về đêm mưa ba năm trước. Đêm đó, hắn bị sỉ nhục đến tận cùng.</p>

<p>Lâm Vĩnh Thịnh — người chú ruột tàn nhẫn — đã tự tay châm lửa đốt sạch di ảnh của cha mẹ hắn ngay giữa sảnh chính. Tro cốt bay tán loạn trong không khí hòa lẫn với tiếng cười hả hê của cả dòng họ. <em>"Thằng phế vật! Bố mẹ mày chết rồi thì tài sản thuộc về tao! Cầm lấy tập hồ sơ từ bỏ quyền thừa kế này, ký vào rồi cút đi!"</em></p>

<p>Lâm Kiều Diễm lúc đó tiến lên, nâng ly rượu vang đỏ đổ thẳng lên đầu hắn, nhìn hắn ướt sũng nhục nhã mà cười ré lên: <em>"Ôi, nhìn anh họ của chúng ta giống con chó ướt chưa kìa! Đi xin ăn nhớ né cửa Lâm gia ra nhé!"</em></p>

<p>Đau đớn nhất là Triệu Mỹ Nga, cô gái hắn từng yêu thương, tiến lên giẫm mạnh gót giày nhọn lên bàn tay đang ôm ngực của hắn, nhổ nước bọt khinh bỉ: <em>"Lâm Phong, nhìn lại bộ dạng nghèo kiết xác của mày đi! Tao thà làm người tình thứ mười của Hoàng thiếu gia còn hơn làm vợ chính thức của loại rác rưởi như mày. Biến đi cho sạch mắt tao!"</em></p>

<p>Lâm Phong bị ném ra đường giữa đêm giông bão, bàn tay rách nát rỉ máu. Nhưng số phận đã cho hắn gặp Vương Kiến Quốc — một đại lão tài chính quốc gia đang ẩn dật, người bị chính thuộc hạ thân tín phản bội dẫn đến tai nạn giao thông trên núi Bạch Vân. Lâm Phong đã dùng tấm thân gầy gò của mình cõng ông lão vượt qua cơn bão tuyết xuống núi cứu mạng.</p>

<p>Để trả ơn, Vương Kiến Quốc nhận hắn làm truyền nhân duy nhất, truyền dạy cho hắn tất cả tinh hoa về quản trị cấp cao, cấu trúc tài chính, pháp lý thương mại và các chiêu thức thâu tóm doanh nghiệp khốc liệt nhất trên thương trường. Ba năm ròng rã khổ luyện, Lâm Phong học hỏi ngày đêm, tự tay thực chiến thâu tóm hàng chục công ty con sắp sụp đổ để xây dựng nên Thiên Long Group — một siêu tập đoàn tài chính hùng mạnh đứng trên đỉnh cao quyền lực.</p>

<p>Hôm nay, hắn trở về.</p>

<p>Xe dừng trước cổng Lâm gia. Hôm nay là tiệc kỷ niệm 30 năm Lâm Thị, sảnh tiệc đèn hoa rực rỡ, khách khứa tấp nập toàn giới siêu giàu.</p>

<p>Lâm Phong bước xuống xe, Đại Phong cầm chiếc ô đen che cho hắn. Hắn đứng sừng sững, khí thế áp đảo khiến đám bảo vệ không tự chủ được mà lùi lại.</p>

<p>Tên bảo vệ trưởng Lâm gia — kẻ năm xưa từng tham gia đập phá đồ đạc của cha mẹ Lâm Phong — nghênh ngang bước ra, chỉ tay vào mặt hắn:</p>

<p>— "Thằng ăn mày nào đây? Đi chỗ khác... Ủa? Lâm Phong?! Thằng phế vật này sao mày chưa chết xó nào à? Cút ngay không tao thả chó cắn nát mặt mày!"</p>

<p>Lâm Phong không thèm chớp mắt. Tên bảo vệ hùng hổ vung nắm đấm định lao tới. Đại Phong chỉ khẽ bước lên một bước, nhanh như chớp tóm chặt lấy cổ tay gã bảo vệ, xoay nhẹ một vòng tạo thành thế khóa khớp vai điêu luyện. Gã bảo vệ lập tức quỳ sụp xuống đất, mồ hôi hột tuôn ra như tắm vì đau đớn, hoàn toàn bất động.</p>

<p>— "Nói với Lâm Vĩnh Thịnh." Lâm Phong tiến tới, đứng sừng sững nhìn xuống tên bảo vệ bằng ánh mắt sắc bén. "Đứa phế vật năm đó... hôm nay trở về để đòi lại từng món nợ năm xưa."</p>"""
    },
    {
        "slug": "chuong-2-bua-tiec-nha-lam-va-cai-tat-dau-tien",
        "title": "Chương 2: Bữa Tiệc Và Video Năm Đó",
        "content": """<p>Bên trong sảnh tiệc Lâm gia, hàng trăm khách mời sang trọng đang nâng ly chúc tụng Lâm Vĩnh Thịnh. Trên sân khấu, Lâm Vĩnh Thịnh mặt mày rạng rỡ, phát biểu đầy tự hào:</p>

<p>— "Tập đoàn Lâm Thị dưới sự dẫn dắt của tôi sẽ sớm thống trị thành phố H—"</p>

<p>Bỗng nhiên, toàn bộ ánh đèn vụt tắt. Màn hình LED khổng lồ phía sau sân khấu đột ngột bật sáng. Nhưng thay vì hình ảnh quảng bá tập đoàn, màn hình lại phát ra những thước phim camera an ninh sắc nét từ ba năm trước: Lâm Vĩnh Thịnh cười man dại đốt sạch di ảnh cha mẹ Lâm Phong ngay giữa sảnh chính, Lâm Kiều Diễm đổ rượu lên đầu hắn cười cợt, và Triệu Mỹ Nga thẳng tay giẫm gót giày nhọn sỉ nhục hắn.</p>

<p>Cả sảnh tiệc bùng nổ những tiếng xầm xì kinh ngạc. Khách mời trố mắt nhìn nhau, hướng ánh mắt khinh bỉ về phía Lâm Vĩnh Thịnh và Lâm gia. Sự thật của dòng họ mang danh thượng lưu bị lột trần công khai trước bàn dân thiên hạ.</p>

<p>Lâm Vĩnh Thịnh mặt tái mét, gầm lên điên cuồng:</p>

<p>— "Tắt đi! Đứa nào làm trò này?! Kỹ thuật đâu, tao giết tụi mày!"</p>

<p>— "Chú Hai, xem tiếp đi chứ, vở diễn mới chỉ bắt đầu thôi mà."</p>

<p>Cửa sảnh tiệc bị đạp tung. Lâm Phong bước vào, vest đen tột đỉnh quyền lực, khí thế điềm tĩnh áp đảo khiến cả khán phòng im lặng nín thở.</p>

<p>Lâm Kiều Diễm nhìn thấy hắn, cơn giận dữ lấn át nỗi sợ, cô ta chỉ tay hét lên:</p>

<p>— "Thằng phế vật! Mày dám đến đây làm loạn tiệc của gia đình tao? Bảo vệ đâu, đập gãy hai chân nó vứt ra đường cho tao!"</p>

<p>Đám bảo vệ hung hãn định lao lên. Nhưng chưa kịp chạm vào chéo áo Lâm Phong, một nhóm cảnh sát kinh tế và thanh tra thuế cùng các vệ sĩ mặc vest xám của Thiên Long đã đồng loạt bước vào. Các thanh tra xuất trình lệnh khám xét và niêm phong khẩn cấp khiến đám bảo vệ Lâm gia tái mặt, lập tức bỏ gậy đầu hàng không dám manh động.</p>

<p>Lâm Phong bước từng bước lên sân khấu, đứng đối diện với Lâm Vĩnh Thịnh đang run bần bật:</p>

<p>— "Mày... mày lấy đâu ra quyền lực này? Mày chỉ là một thằng nghèo kiết xác!" Lâm Vĩnh Thịnh hét lớn để che giấu sự sợ hãi.</p>

<p>Lâm Phong khẽ cười, nụ cười đầy vẻ khinh bỉ. Luật sư Trần bước lên, rút ra tập hồ sơ pháp lý đóng dấu đỏ chói:</p>

<p>— "Ông Lâm Vĩnh Thịnh, Thiên Long Group đã mua đứt 200 tỷ nợ xấu của Lâm Thị tại ba ngân hàng liên minh. Theo điều khoản thế chấp khẩn cấp, chúng tôi chính thức niêm phong toàn bộ dinh thự này và đóng băng hoạt động của tập đoàn Lâm Thị ngay lập tức!"</p>

<p>Lâm Vĩnh Thịnh cố gượng gạo cười:</p>

<p>— "Ha ha! Mày hù ai đó hả thằng ranh? Ngân hàng Đông Á là đối tác của tao, làm sao họ ký chuyển nợ cho mày được—"</p>

<p>Chưa kịp nói hết câu, ba vị Giám đốc đại diện của ba ngân hàng lớn nhất thành phố bước vào sảnh tiệc, cung kính cúi đầu trước Lâm Phong trước sự chứng kiến của cả căn phòng:</p>

<p>— "Kính chào ngài Lâm Phong Chủ tịch tối cao! Chúng tôi đã hoàn tất toàn bộ thủ tục niêm phong tài sản của Lâm gia theo lệnh của ngài!"</p>

<p>Lâm Vĩnh Thịnh nhìn cảnh tượng đó mà như ngã từ trên trời xuống đất, hai chân đứng không vững, quỳ sụp xuống sàn sân khấu.</p>

<p>Lâm Kiều Diễm hoảng loạn chạy lên định cào cấu Lâm Phong. Nhưng cô ta vấp phải tà váy dài thướt tha của chính mình, loạng choạng ngã nhào vào đống ly pha lê đổ vỡ cạnh sân khấu, đầm dạ hội ướt sũng trong đống rượu vang đỏ rơi vãi. Cả tháp rượu đổ ập lên người cô ta, làm khuôn mặt trang điểm đậm bê bết rượu vang đỏ thẫm, thảm hại không sao tả xiết.</p>

<p>— "Anh Phong... cứu em..." Kiều Diễm khóc lóc thảm thiết.</p>

<p>Lâm Phong bước từng bước thong thả đến bên cạnh, đứng sừng sững nhìn xuống cô ta với ánh mắt đầy sự hững hờ. Hắn nhẹ nhàng dẫm gót giày da bóng loáng lên bản giao ước nợ rách nát trước mặt cô ta, giọng nói thản nhiên:</p>

<p>— "Lâm Kiều Diễm, ngày xưa cô đổ rượu vang lên đầu tôi, ép tôi liếm giày cho cô. Bây giờ dòng họ của cô đang nợ tôi 200 tỷ. Chỉ cần tôi búng tay, cả đời cô và bố cô sẽ phải ở trong phòng biệt giam để trả nợ. Đây mới chỉ là một phần nhỏ thôi, em họ à." Hắn nhìn xuống Lâm Vĩnh Thịnh đang run rẩy. "Chú Hai, chuẩn bị tinh thần đi, tôi sẽ thu hồi từng đồng nợ một từ các người."</p>"""
    },
    {
        "slug": "chuong-3-nguoi-tinh-cu-va-ten-tieu-nhan",
        "title": "Chương 3: Người Tình Cũ Và Tên Tiểu Nhân",
        "content": """<p>Tại nhà hàng Seasons siêu sang, Hoàng Tuấn Kiệt đang ôm eo Triệu Mỹ Nga ngồi ở bàn VIP số 7. Tuấn Kiệt cười đắc ý, ném một xấp tiền dày xuống sàn dưới chân Lâm Phong vừa bước vào:</p>

<p>— "Ê thằng phế vật! Nghe nói mày mới về hả? Nhặt đống tiền này lên rồi bò quanh bàn lau giày cho tao và Mỹ Nga, tao sẽ bố trí cho mày làm chân rửa bát ở đây!"</p>

<p>Triệu Mỹ Nga che miệng khinh bỉ, ánh mắt đầy sự khinh ghét nhìn Lâm Phong:</p>

<p>— "Lâm Phong ơi là Lâm Phong, mặc vest giả hiệu thì cũng không che được cái mùi nghèo kiết xác của mày đâu. Nhặt tiền đi kìa, bằng cả năm lương làm thuê của mày đó!"</p>

<p>Khách xung quanh đổ dồn ánh mắt châm biếm về phía Lâm Phong. Nhưng gương mặt hắn vẫn tĩnh lặng như nước hồ mùa thu. Hắn nhìn xấp tiền dưới chân, rồi nhìn thẳng vào Hoàng Tuấn Kiệt.</p>

<p>— "Hoàng Tuấn Kiệt, anh thích ném tiền lắm đúng không?" Lâm Phong khẽ hỏi, giọng nói điềm tĩnh nhưng đanh thép.</p>

<p>— "Tao thích đó, thì sao? Thằng nghèo rách như mày làm gì được tao?" Tuấn Kiệt nghênh mặt thách thức.</p>

<p>Lâm Phong khẽ búng tay. Ngay lập tức, Giám đốc điều hành nhà hàng Seasons cùng năm nhân viên bảo vệ lực lưỡng chạy ra, nhưng thay vì đuổi Lâm Phong, họ lập tức đè chặt Hoàng Tuấn Kiệt xuống bàn ăn, úp mặt hắn vào đĩa súp nóng hổi.</p>

<p>— "Áaaa! Nóng quá! Đứa nào dám làm thế với tao?!" Hoàng Tuấn Kiệt hét lên đau đớn, mặt đỏ bỏng vì súp nóng.</p>

<p>— "Hoàng thiếu gia, anh bị cấm cửa khỏi toàn bộ hệ thống nhà hàng của Thiên Long Group trên toàn quốc." Giám đốc Seasons lạnh lùng thông báo. "Bởi vì Chủ tịch tối cao của tập đoàn chúng tôi chính là ngài Lâm Phong đây!"</p>

<p>Chưa dừng lại ở đó, Minh Nguyệt bước lên, rút ra chiếc máy tính bảng:</p>

<p>— "Hoàng Tuấn Kiệt, dự án khu đô thị phía Nam của Hoàng gia đang vay vốn 500 tỷ từ quỹ tài chính Thiên Long. Do anh vi phạm điều khoản đạo đức và có hành vi xúc phạm Chủ tịch tối cao, chúng tôi chính thức đơn phương chấm dứt hợp đồng, thu hồi nợ trước hạn trong vòng 24 giờ. Cổ phiếu Hoàng gia trên sàn chứng khoán đang bị chúng tôi đánh sập 30% chỉ trong vòng năm phút qua!"</p>

<p>Hoàng Tuấn Kiệt nghe xong tin tức, điện thoại trong túi đổ chuông liên tục. Tiếng gào khóc của cha hắn qua điện thoại vang lên rõ mồn một: <em>"Thằng nghịch tử! Mày đã chọc giận ai mà để Hoàng gia phá sản rồi?! Tao giết mày!"</em></p>

<p>Tuấn Kiệt quỳ sụp xuống sàn, lết đến chân Lâm Phong, mặt mũi lấm lem súp và nước mắt, tự tát liên tục vào mặt mình:</p>

<p>— "Lâm thiếu! Tôi sai rồi! Tôi là con chó, tôi là đống rác! Xin ngài tha cho Hoàng gia!"</p>

<p>Triệu Mỹ Nga run rẩy đứng không vững, cô ta tái mặt, lắp bắp tiến lên định nắm lấy tay áo Lâm Phong:</p>

<p>— "Phong... ngày xưa em bị gia đình ép buộc... thật ra em vẫn luôn yêu anh..."</p>

<p>— "Bẩn áo tôi." Lâm Phong lạnh lùng gạt tay cô ta ra khiến cô ta ngã nhào lên xấp tiền đang rải rác dưới đất. Hắn giẫm thẳng lên đống tiền đó, nhìn cô ta bằng ánh mắt hờ hững lạnh nhạt. "Triệu Mỹ Nga, đống tiền này cô thích thì cứ nhặt lấy mà dùng để mua chiếc váy cưới rách của cô đi."</p>

<p>Lâm Phong bước đi trong sự cung kính cúi đầu của toàn bộ nhân viên nhà hàng, để lại hai kẻ đang khóc lóc nhục nhã giữa đống tiền rơi vãi dưới đất.</p>"""
    },
    {
        "slug": "chuong-4-man-hop-bao-chan-dong",
        "title": "Chương 4: Họp Báo Và Đòn Phản Công Trong Bóng Tối",
        "content": """<p>Buổi họp báo công bố dự án 5.000 tỷ của Thiên Long Group tại thành phố H diễn ra vô cùng hoành tráng, thu hút toàn bộ sự chú ý của giới truyền thông quốc gia. Sự xuất hiện rực rỡ của Lâm Phong làm lu mờ hoàn toàn mọi thế lực cũ.</p>

<p>Nhưng sự nhục nhã của Lâm gia và Hoàng gia đã đẩy Lâm Vĩnh Thịnh vào bước đường cùng. Lão liên thủ với Tạ Vĩnh Bình — Phó Chủ tịch Hiệp hội Thương nhân, kẻ nắm giữ quyền lực trong giới ngân hàng địa phương để chuẩn bị một đòn phản công chí mạng.</p>

<p>— "Thằng ranh con đó muốn diệt chúng ta." Lâm Vĩnh Thịnh nghiến răng bên ly rượu mạnh. "Tôi đã chuẩn bị một bộ hồ sơ giả hoàn hảo chứng minh Thiên Long rửa tiền. Chỉ cần anh Bình ký lệnh phong tỏa khẩn cấp tài khoản của nó, dự án 5.000 tỷ sẽ chết yểu. Lúc đó, chúng ta sẽ ép nó vào đường cùng!"</p>

<p>Tạ Vĩnh Bình cười lạnh, ánh mắt đầy vẻ tham lam:</p>

<p>— "Một thằng nhóc từ nơi khác về mà đòi làm loạn ở đây sao? Cứ để tôi ra tay, tôi sẽ bắt nó phải trắng tay!"</p>

<p>Sáng hôm sau, Tạ Vĩnh Bình dẫn đầu một đoàn thanh tra liên ngành rầm rộ ập vào trụ sở Thiên Long Group. Lão ngang tàng bước vào phòng làm việc của Lâm Phong, ném tờ lệnh phong tỏa lên bàn, cười đắc ý:</p>

<p>— "Lâm Phong! Toàn bộ tài khoản 2.000 tỷ của mày đã bị phong tỏa khẩn cấp để điều tra tội rửa tiền. Mày xong đời rồi con trai ạ! Ở thành phố H này, tao mới là luật lệ!"</p>

<p>Lâm Vĩnh Thịnh đứng đằng sau cũng cười đầy đắc thắng:</p>

<p>— "Ha ha! Thằng phế vật! Mày tưởng mày mạnh lắm sao? Bây giờ không có tiền thanh toán cho nhà thầu, dự án của mày sẽ bị tịch thu! Mày lại chuẩn bị đi xin ăn tiếp đi!"</p>

<p>Trái ngược hoàn toàn với sự đắc ý của đối thủ, Lâm Phong chỉ chậm rãi đứng dậy từ ghế chủ tịch. Gương mặt hắn không hề có một chút lo sợ hay tức giận. Khóe môi hắn khẽ cong lên một nụ cười đầy bí hiểm. Hắn đón nhận tờ lệnh phong tỏa một cách trầm tĩnh, thản nhiên cầm lên lướt qua rồi đặt xuống:</p>

<p>— "Tạ Vĩnh Bình, lệnh phong tỏa này ký rất nhanh đấy. Nhưng ông có chắc là bản thân đã suy nghĩ kỹ chưa?"</p>

<p>— "Thằng ranh! Mày còn dám mạnh miệng sao?!" Tạ Vĩnh Bình đập bàn quát lớn rồi đắc thắng cùng Lâm Vĩnh Thịnh quay lưng bỏ đi, đinh ninh rằng Lâm Phong chỉ đang cố tỏ ra cứng rắn trước khi sụp đổ.</p>

<p>Ngay sau khi phái đoàn thanh tra rời đi, một cơn chấn động dữ dội lập tức càn quét qua Thiên Long Group:</p>

<p>Hiệu ứng dây chuyền xảy ra lập tức khi liên minh các ngân hàng địa phương siết chặt dòng tiền mặt. Điện thoại tại phòng Quan hệ Cổ đông và phòng Tài chính đổ chuông liên tục không ngừng nghỉ. Các cổ đông lớn liên tục gọi điện chất vấn Lâm Phong với thái độ hoang mang cực độ, thậm chí một vài nhóm đầu tư lớn bắt đầu gây áp lực, đe dọa rút vốn khẩn cấp để bảo toàn nguồn lực.</p>

<p>Tại đại sảnh tòa nhà Thiên Long, hàng chục đại diện của các nhà thầu phụ chịu trách nhiệm thi công siêu dự án 5.000 tỷ nháo nhào kéo đến. Họ mang theo đơn kiến nghị đòi dừng thi công khẩn cấp và yêu cầu đối chất, thanh toán ngay lập tức các khoản nợ đọng vì lo sợ Thiên Long sẽ rơi vào cảnh vỡ nợ trước pháp luật.</p>

<p>Lâm Phong vẫn ngồi tĩnh lặng trên chiếc ghế da lớn trong phòng làm việc. Hắn khẽ xoay chiếc bút ký trên tay, ánh mắt sâu thẳm nhìn xuống toàn cảnh thành phố đang dần lên đèn qua lớp kính lớn. Hắn đang chủ động để các đối thủ đẩy mình vào chân tường, bắt những kẻ phản bội ẩn nấp sâu nhất trong hệ thống phải tự lộ diện.</p>

<p>— "Chưa đẩy đến bờ vực, làm sao biết được ai là người trung thành, kẻ nào là quân phản bội." Hắn thì thầm.</p>

<p>Đúng lúc đó, Minh Nguyệt bước nhanh vào văn phòng, gương mặt lộ rõ vẻ lo lắng tột độ, báo cáo một tin tức chí mạng:</p>

<p>— "Chủ tịch, Hứa Quốc Hoa — Giám đốc tài chính của chúng ta — vừa đột ngột cắt đứt toàn bộ liên lạc cá nhân, xóa tài khoản hệ thống nội bộ và đem theo toàn bộ hồ sơ kỹ thuật số mật đi mất rồi!"</p>

<p>Lâm Phong nghe xong, mắt khẽ híp lại, giọng nói vô cùng điềm tĩnh:</p>

<p>— "Quân cờ đã đi, không thể rút lại. Trận chiến thực sự bắt đầu rồi."</p>"""
    },
    {
        "slug": "chuong-5-bay-cua-ke-thu-va-don-phan-cong",
        "title": "Chương 5: Khi Cả Thành Phố Quay Lưng",
        "content": """<p>Đúng như dự liệu, sự biến động dữ dội bao trùm lấy Thiên Long Group trong 48 giờ tiếp theo. Cả thành phố H dường như quay lưng lại với Lâm Phong. Liên minh ngân hàng dưới trướng Tạ Vĩnh Bình phong tỏa toàn bộ 2.000 tỷ đồng tiền mặt của tập đoàn. Các đối tác, nhà cung cấp lớn nhỏ lập tức nháo nhào như ong vỡ tổ.</p>

<p>Trong lúc dầu sôi lửa bỏng đó, một sự phản bội chí mạng đã xảy ra. Hứa Quốc Hoa — vị cổ đông sáng lập kiêm Giám đốc tài chính của Thiên Long Group, người mà Lâm Phong luôn hết mực tin tưởng — đã chính thức quay lưng. Lão ôm toàn bộ bản vẽ thiết kế phân khu công nghệ cao, hồ sơ mật của siêu dự án 5.000 tỷ đào tẩu sang đầu quân cho Lâm Vĩnh Thịnh. Lão thậm chí còn công khai phát biểu trên sóng truyền hình địa phương, cáo buộc Thiên Long Group là một vỏ bọc lừa đảo sắp vỡ nợ. Sự phản bội chí mạng này lập tức thổi bùng ngọn lửa hoang mang, khiến cổ phiếu của Thiên Long trên thị trường phi tập trung sụt giảm nghiêm trọng tới 10% chỉ trong vài giờ. Đây là lần đầu tiên Thiên Long phải hứng chịu tổn thất thực tế lớn đến thế.</p>

<p>Trước tình thế ngàn cân treo sợi tóc, để bảo toàn huyết mạch doanh nghiệp, đại lão Vương Kiến Quốc đang ẩn dật đã buộc phải phá lệ ra tay. Ông dùng uy tín tích lũy cả đời của mình thực hiện một cuộc gọi bảo mật khẩn cấp đến Thống đốc Ngân hàng Nhà nước, cam kết bảo lãnh cá nhân bằng toàn bộ tài sản ẩn danh ở nước ngoài của mình để giữ vững hạn mức tín dụng khẩn cấp cho Thiên Long Group. Nước đi hiểm hóc này đã mua thêm cho Lâm Phong 12 giờ vàng ngọc vô giá để xoay chuyển cục diện.</p>

<p>Nhưng đau đớn nhất đối với Lâm Phong chính là sự việc xảy ra vào buổi chiều ngày thứ hai. Minh Nguyệt, trợ lý trung thành của hắn, đang ôm tập hồ sơ tài liệu chứng cứ tuyệt mật bước ra khỏi sảnh tòa nhà để đến nộp cho cơ quan điều tra cấp cao. Ngay khi cô vừa xuất hiện, một đám đông côn đồ giả danh phóng viên do Lâm Vĩnh Thịnh thuê mướn đã bao vây chặt lấy cô, xô đẩy dữ dội. Một gã to xác cố tình huých cực mạnh vào vai Minh Nguyệt, khiến cô mất đà ngã nhào từ trên bậc thềm bê tông cao xuống sân gạch lạnh lẽo. Đầu cô va đập mạnh vào gờ bê tông, máu tươi tuôn xối xả làm ướt đầm đìa cả mái tóc và chiếc váy công sở màu nhạt. Dù đau đớn đến bán mê bán tỉnh, cô vẫn dùng chút sức tàn ôm chặt tập tài liệu vào lồng ngực như bảo vệ sinh mệnh của chính mình. Minh Nguyệt lập tức được đưa vào bệnh viện cấp cứu trong tình trạng chấn thương sọ não nhẹ và đầu gối rách sâu phải khâu 12 mũi.</p>

<p>Lâm Phong lao như điên đến bệnh viện. Đứng bên giường bệnh, nhìn Minh Nguyệt nằm hôn mê, đầu quấn băng trắng toát, gương mặt nhợt nhạt không còn giọt máu, lồng ngực hắn co thắt dữ dội vì một nỗi đau đớn và ân hận tột cùng. Hắn nắm chặt bàn tay lạnh ngắt của cô, sát khí trong mắt ngưng tụ thành băng giá lạnh buốt:
<br>— "Minh Nguyệt... tôi thề sẽ bắt cả Lâm gia và những kẻ đứng sau phải quỳ dưới chân em để sám hối!"</p>

<p>Sáng hôm sau, Lâm Vĩnh Thịnh và Tạ Vĩnh Bình hí hửng tổ chức họp báo công bố việc thu hồi dự án của Thiên Long ngay tại sảnh chính của khách sạn Hoàng Cung, muốn dồn Lâm Phong vào cái chết xã hội trước hàng trăm phóng viên quốc gia.</p>

<p>— "Lâm Phong! Mày định quỳ lạy xin tha hay để tao tống mày vào tù?" Tạ Vĩnh Bình đứng trên bục phát biểu gầm lên đầy đắc thắng trước hàng trăm phóng viên.</p>

<p>Lâm Phong khẽ gật đầu với phía cửa sảnh.</p>

<p>Ngay lập tức, một đoàn người mặc vest đen nghiêm nghị bước vào. Dẫn đầu là **Thống đốc Ngân hàng Nhà nước** và **Cục trưởng Cục Điều tra Tội phạm Kinh tế Bộ Công an**.</p>

<p>Cả hội trường họp báo lập tức im phăng phắc như tờ.</p>

<p>Thống đốc Ngân hàng Nhà nước bước lên bục phát biểu, dõng dạc thông báo:</p>

<p>— "Chúng tôi chính thức xác nhận toàn bộ nguồn vốn của Thiên Long Group là hoàn toàn hợp pháp và minh bạch. Đồng thời, lệnh phong tỏa tài khoản của Thiên Long do Tạ Vĩnh Bình ký là hành vi lạm dụng quyền hạn trái pháp luật nhằm mục đích tư lợi cá nhân!"</p>

<p>Cục trưởng Cục Điều tra bước xuống, chỉ tay thẳng vào mặt Tạ Vĩnh Bình đang há hốc miệng kinh hoàng:</p>

<p>— "Tạ Vĩnh Bình! Ông bị bắt khẩn cấp vì tội nhận hối lộ, rửa tiền và lạm dụng chức vụ quyền hạn gây hậu quả nghiêm trọng! Yêu cầu khóa tay đối tượng!"</p>

<p>Hai cảnh sát hình sự lao lên, đè nghiến Tạ Vĩnh Bình xuống sàn họp báo trước hàng trăm ống kính camera đang phát sóng trực tiếp toàn quốc. Tạ Vĩnh Bình sợ hãi khóc lóc thảm thiết:</p>

<p>— "Oan uổng quá! Lâm chủ tịch! Lâm thiếu gia cứu tôi với! Tôi bị Lâm Vĩnh Thịnh xúi giục!"</p>

<p>Lâm Vĩnh Thịnh đứng cạnh đó mặt vũ xám ngoét, định lén lút lùi ra cửa để bỏ trốn.</p>

<p>— "Lâm Vĩnh Thịnh, chú định đi đâu?" Giọng nói của Lâm Phong vang lên điềm tĩnh nhưng vang vọng khắp cả sảnh hội trường.</p>

<p>Đại Phong cùng các vệ sĩ chặn đứng lối thoát của Lâm Vĩnh Thịnh, đá mạnh vào nhượng chân khiến lão quỳ sụp xuống sàn xi măng lạnh lẽo trước hàng trăm phóng viên.</p>

<p>— "Chú Hai, những món nợ cũ, đã đến lúc phải thanh toán sòng phẳng rồi." Lâm Phong nhìn xuống lão bằng ánh mắt hờ hững, lạnh nhạt.</p>"""
    },
    {
        "slug": "chuong-6-dam-cuoi-bi-pha",
        "title": "Chương 6: Đám Cưới Và Sự Thật Năm Xưa",
        "content": """<p>Hôm nay là ngày cưới của Hoàng Tuấn Kiệt và Triệu Mỹ Nga tại sảnh tiệc lộng lẫy nhất của khách sạn Hoàng Cung. Triệu Mỹ Nga khoác lên mình chiếc váy cưới thiết kế tinh xảo, nở nụ cười kiêu ngạo đón tiếp khách khứa. Cô ta nghĩ rằng dù Hoàng gia đang gặp khó khăn, nhưng đám cưới này vẫn giúp cô ta bước chân vào giới thượng lưu.</p>

<p>Nhưng ngay khi cô dâu chú rể chuẩn bị bước lên lễ đường làm lễ, một đội ngũ cưỡng chế niêm phong tài sản của tòa án phối hợp cùng cảnh sát ập vào.</p>

<p>Họ thô bạo lột chiếc nhẫn kim cương bốn cara trên ngón tay Triệu Mỹ Nga, giật phắt chiếc vòng cổ ngọc trai đắt tiền trên cổ cô ta trước sự chứng kiến của năm trăm khách mời quý tộc.</p>

<p>— "Tài sản này thuộc danh mục thế chấp nợ xấu của Hoàng gia tại Thiên Long Group và đang bị niêm phong khẩn cấp để thu hồi nợ!" Đại diện tòa án lạnh lùng thông báo.</p>

<p>Hoàng Tuấn Kiệt hoảng loạn định bỏ trốn thì bị cảnh sát đè chặt xuống sàn lễ đường hoa tươi, khóa tay ra sau vì cáo buộc lừa đảo chiếm đoạt tài sản và trốn thuế.</p>

<p>Khách mời bên dưới nhao nhao chửi rủa, ném hoa cưới và những ly nước vào người cô dâu chú rể đang thảm hại dưới đất. Hoàng gia sụp đổ hoàn toàn ngay trong ngày cưới!</p>

<p>Triệu Mỹ Nga tóc tai bù xù, váy cưới rách nát, khóc lóc thảm thiết gọi điện cho Lâm Phong để cầu xin. Đầu dây bên kia kết nối, giọng Lâm Phong vang lên vô cùng bình thản:</p>

<p>— "Mỹ Nga, đám cưới vui vẻ chứ?"</p>

<p>— "Phong! Em sai rồi! Em là con khốn! Xin anh hãy nể tình xưa nghĩa cũ cứu em với..."</p>

<p>— "Tình xưa nghĩa cũ?" Lâm Phong khẽ cười lạnh. "Nghĩa cũ của cô là giẫm gót giày lên bàn tay rỉ máu của tôi đêm đó sao?"</p>

<p>Triệu Mỹ Nga lúc này như phát điên, quỳ sụp xuống đống hoa cưới nát bét, gào khóc điên cuồng qua điện thoại để tung ra con át chủ bài cuối cùng hòng tự cứu mạng:</p>

<p>— "Lâm Phong! Anh không được tuyệt tình như vậy! Em biết một bí mật động trời về vụ tai nạn sáu năm trước của cha mẹ anh! Đêm đó, chính tai em đã nghe thấy Lâm Vĩnh Thịnh gọi điện cho kẻ đứng sau ở thủ đô! Vụ tai nạn đó có một thế lực lớn ở thủ đô che lưng, chiếc container màu xanh lá cây đậm chính là do họ sắp xếp và xóa sạch mọi hồ sơ điều tra của cảnh sát! Lâm Vĩnh Thịnh đã lén lút ghi âm lại cuộc gọi thỏa thuận chia chác cổ phần với kẻ đó và lưu trong một chiếc thẻ nhớ siêu nhỏ, giấu bên trong bức tượng Phật ngọc ở thư phòng của lão! Xin anh cứu em, em sẽ đưa nó cho anh!"</p>

<p>Lâm Phong nghe xong, đồng tử co rút mạnh mẽ. Chiếc xe container màu xanh lá cây đậm... Manh mối bị xóa bỏ sáu năm trước rốt cuộc đã lộ diện! Hắn dằn giọng đầy sắc bén:</p>

<p>— "Cảm ơn cô đã cung cấp tin tức. Nhưng chiếc thẻ nhớ đó, người của tôi đã lấy được từ 10 phút trước rồi. Còn cô, tôi đã sắp xếp cho cô một công việc phù hợp: làm công nhân vệ sinh quét rác ở chi nhánh vùng sâu vùng xa của Thiên Long. Hãy dùng cả đời cô để quét sạch đống rác rưởi trong tâm hồn mình đi."</p>

<p>Lâm Phong dứt khoát cúp máy. Triệu Mỹ Nga trợn mắt nhìn màn hình điện thoại đã tắt, tinh thần hoàn toàn sụp đổ, điên loạn la hét giữa lễ đường trống trải.</p>"""
    },
    {
        "slug": "chuong-7-man-ket-toan-voi-gia-toc-lam",
        "title": "Chương 7: Kết Toán — Và Sự Thật Về Đêm Tai Nạn",
        "content": """<p>Tại đại sảnh dinh thự Lâm gia, bầu không khí âm u lạnh lẽo bao trùm toàn bộ không gian. Lâm Phong ngồi sừng sững trên chiếc ghế chủ tọa bằng gỗ mun của gia tộc. Đi sau hắn là mười vệ sĩ xám đứng nghiêm trang.</p>

<p>Lâm Vĩnh Thịnh bị Đại Phong xách cổ ném thẳng xuống sàn nhà dưới chân Lâm Phong, mặt mũi bơ phờ, bầm dập.</p>

<p>— "Lâm Phong! Mày là đồ nghịch tử! Mày dám đối xử với chú ruột mày như thế này sao?! Tao sẽ kiện mày ra tòa!" Lâm Vĩnh Thịnh gào hét trong vô vọng.</p>

<p>Lâm Phong không thèm chớp mắt. Hắn nhẹ nhàng giơ tay, Đại Phong lập tức cắm một chiếc đầu đọc thẻ nhớ vào máy tính bảng, kết nối trực tiếp với hệ thống âm thanh đại sảnh. Ngay lập tức, một đoạn ghi âm thoại rõ mồn một vang lên, lấp đầy toàn bộ không gian:</p>

<p><em>"Tôi đã sắp xếp chiếc container xanh lá cây của Nguyễn Văn Hùng đâm trực diện xe của Lâm Đình Sơn ở khúc cua... Yêu cầu ông xóa sạch mọi hồ sơ giao thông của xe container này... Cổ phần Lâm Thị sau khi tôi cướp được sẽ chia cho ông 30%..."</em></p>

<p>Tiếng nói của Lâm Vĩnh Thịnh cùng một giọng nói trầm lạnh từ thủ đô vang lên rõ mồn một. Lâm Vĩnh Thịnh nghe xong tai ù đi, cả người run bắn lên. Nhưng lão vẫn ngoan cố gào hét chối tội đầy điên cuồng:</p>

<p>— "Bịa đặt! Đây là giả mạo! Lũ khốn chúng mày cắt ghép giọng nói của tao! Nguyễn Văn Hùng chỉ là tên tài xế đã bị mày mua chuộc để khai gian đổ tội cho tao! Mày không có bằng chứng pháp lý nào cả!"</p>

<p>Lâm Phong khẽ lật giở một tập hồ sơ đỏ trên tay, lấy ra tập tài liệu thứ hai ném thẳng trước mặt Lâm Vĩnh Thịnh:</p>

<p>— "Vậy còn khoản giao dịch chuyển khoản 5 tỷ đồng này thì sao? Tiền được trích xuất từ tài khoản offshore của một công ty vỏ bọc tại Singapore do chú đứng tên, chuyển thẳng vào tài khoản ngân hàng của vợ Nguyễn Văn Hùng ngay trong đêm tai nạn xảy ra. Đây là bản sao kê tài chính có dấu đỏ xác nhận trực tiếp của cơ quan thanh tra Bộ Công an. Chú giải thích thế nào về việc tự dưng làm từ thiện cho gia đình tài xế container?"</p>

<p>Lâm Vĩnh Thịnh trợn mắt nhìn bản sao kê ngân hàng, cổ họng nghẹn ứ, mặt mũi xám xịt không nói thành lời.</p>

<p>Lâm Phong thong thả ném tiếp tập tài liệu thứ ba:</p>

<p>— "Chưa hết. Đây là dữ liệu trích xuất từ camera giám sát hành trình và hệ thống định vị GPS của xe container. Nó chứng minh chiếc xe đã đậu chờ sẵn tại khúc cua Bạch Vân suốt hai tiếng đồng hồ, nhận được ba cuộc gọi điều phối từ số điện thoại cá nhân của chú chỉ ba phút trước khi đâm trực diện vào xe của cha mẹ tôi. Chú nghĩ xóa dữ liệu giao thông của cảnh sát địa phương là có thể xóa sạch mọi dấu vết của Lưới Trời sao?"</p>

<p>Từng đòn chứng cứ đập xuống như những cú búa tạ nghiền nát mọi lời ngụy biện cuối cùng. Lâm Vĩnh Thịnh hoàn toàn sụp đổ, hai đầu gối khuỵu xuống, run lẩy bẩy bò rạp dưới đất khóc lóc cầu xin tha thứ trong tuyệt vọng tột cùng:</p>

<p>— "Phong! Cháu ơi! Chú sai rồi! Chú bị quỷ ám... Xin cháu nể tình máu mủ tha cho chú một con đường sống... Chú sẽ trả lại toàn bộ cổ phần và tài sản cho cháu!"</p>

<p>Lâm Phong cúi xuống nhìn lão, ánh mắt đầy sự ghê tởm. Hắn nhẹ nhàng dùng gót giày da gạt phắt tay Lâm Vĩnh Thịnh ra, thản nhiên đứng dậy, giọng nói lạnh lùng:</p>

<p>— "Máu mủ? Lúc chú thuê người đâm chết cha mẹ tôi, chú có nghĩ đến hai chữ máu mủ không? Lúc chú thiêu rụi di ảnh cha mẹ tôi, chú có nghĩ đến máu mủ không? Chú Hai, yên tâm đi. Kẻ chống lưng ở thủ đô đứng sau chú trong đoạn băng này, tôi cũng sẽ sớm đưa hắn ra ánh sáng."</p>

<p>Cảnh sát hình sự lập tức lao lên, khóa chặt tay Lâm Vĩnh Thịnh áp giải đi trước sự chứng kiến của cả gia tộc Lâm đang quỳ lạy run rẩy xung quanh.</p>

<p>Lâm Phong đứng sừng sững giữa sảnh chính, nhìn lướt qua các thành viên Lâm gia đang quỳ rạp dưới đất không dám ngẩng đầu:</p>

<p>— "Lâm gia từ hôm nay đổi chủ. Kẻ nào dám có ý kiến phản đối?"</p>

<p>Cả gia tộc Lâm đồng loạt dập đầu sát đất, run rẩy đồng thanh vang lên: <em>"Không dám! Kính chào Lâm chủ tịch!"</em></p>"""
    },
    {
        "slug": "chuong-8-binh-minh-cua-ke-tro-ve",
        "title": "Chương 8: Bình Minh — Và Những Gì Còn Lại",
        "content": """<p>Một tháng sau sóng gió thương trường chấn động thành phố H.</p>

<p>Mọi ồn ào và bụi bặm của những cuộc trả thù cuối cùng cũng lắng xuống. Lâm gia từ hôm nay đã thuộc về Lâm Phong, nhưng hắn không chọn ở lại căn penthouse hào nhoáng ở trung tâm thành phố. Hắn chọn quay về ngôi biệt thự cổ của gia đình năm xưa — nơi từng bị Lâm Vĩnh Thịnh chiếm đoạt và tàn phá.</p>

<p>Dưới bàn tay trùng tu tỉ mỉ của Lâm Phong, ngôi nhà cũ đã tìm lại được vẻ ấm cúng và tôn nghiêm vốn có.</p>

<p>Tại sảnh thờ chính trang nghiêm, ánh nắng sớm khẽ len lỏi qua ô cửa sổ bằng gỗ, chiếu rọi lên bức hoành phi cổ kính và di ảnh của cha mẹ Lâm Phong vừa được phục chế hoàn hảo. Lâm Phong đứng lặng lẽ trước bàn thờ, trên người mặc bộ đồ đen giản dị. Hắn chậm rãi thắp ba nén hương trầm nghi ngút. Khói hương bay lơ lửng mang theo gánh nặng và nỗi đau suốt sáu năm đày ải của hắn.</p>

<p>Lâm Phong chậm rãi cúi đầu vái lạy ba vái sâu. Đôi mắt vốn luôn sắc bén, coi thường vạn vật trên thương trường giờ đây bỗng đỏ hoe, ngập tràn sương mỏng. Một giọt nước mắt khẽ lăn dài trên má hắn. Hắn đứng sừng sững trước bàn thờ, thì thầm với giọng run rẩy nhưng đầy kiêu hãnh:
<br>— "Ba, mẹ... con đã trở về rồi. Con đã lấy lại toàn bộ gia sản, danh dự và đòi lại công lý cho gia đình ta. Những kẻ thủ ác hại ba mẹ đều đã phải trả giá đắt trước pháp luật. Xin ba mẹ ở trên cao linh thiêng hãy yên lòng yên nghỉ..."</p>

<p>Một bàn tay ấm áp khẽ luồn vào lòng bàn tay hắn, siết nhẹ. Lâm Phong quay đầu lại, nhìn thấy Minh Nguyệt đang đứng bên cạnh. Trên đầu gối cô, vết thương từ cú ngã hôm đó đã lành lặn, cô mặc một chiếc đầm trắng tinh khôi như hoa cúc sớm. Trong mắt cô lúc này cũng lấp lánh nước mắt xúc động.</p>

<p>Minh Nguyệt khẽ tiến lên, thắp một nén hương, cúi đầu cung kính vái lạy trước di ảnh:
<br>— "Thưa hai bác, con là Minh Nguyệt. Từ nay về sau, con xin nguyện ở bên cạnh chăm sóc và đồng hành cùng anh Phong trên mọi nẻo đường đời. Xin hai bác yên lòng yên nghỉ."</p>

<p>Lâm Phong nhìn cô, trái tim hắn tràn ngập sự ấm áp chưa từng có suốt sáu năm qua. Hắn đưa tay nhẹ nhàng lau đi giọt nước mắt lăn trên má cô, khẽ kéo cô vào lòng, tựa cằm lên mái tóc thơm ngát của cô.</p>

<p>— "Cảm ơn em, Minh Nguyệt. Nếu không có sự kiên định của em đêm hôm đó, có lẽ tôi đã không thể hoàn thành ván cờ này trọn vẹn như vậy." Hắn thì thầm.</p>

<p>— "Được ở bên anh, nhìn anh tìm lại công lý, đó là hạnh phúc lớn nhất của đời em." Minh Nguyệt khẽ ngẩng đầu mỉm cười, đôi mắt rạng rỡ.</p>

<p>Hắn quay sang nắm lấy bàn tay mềm mại của Minh Nguyệt, dắt cô bước ra ngoài sảnh lớn. Ánh bình minh rực rỡ xua tan đi làn sương mù cuối cùng, chiếu rọi hai bóng hình đi bên nhau hướng về phía tương lai tươi sáng.</p>

<p>Nhờ vào toàn bộ tài liệu chứng cứ đanh thép được Lâm Phong gửi đi, Ủy ban Kiểm tra Đặc biệt Trung ương đã chính thức phê chuẩn quyết định khởi tố, bắt giam thế lực lớn chống lưng tại thủ đô. Toàn bộ tài sản bất hợp pháp và cổ phần chiếm đoạt của hắn đều bị phong tỏa, thu hồi triệt để. Lưới trời lồng lộng, không một ai có thể đứng ngoài vòng pháp luật.</p>

<p>Đứa phế vật năm đó nay đã thực sự đứng trên đỉnh cao quyền lực, tìm lại được cả danh dự gia tộc lẫn tình yêu đích thực của cuộc đời mình.</p>

<p style="text-align:center; margin-top: 40px;">—— <strong>HẾT</strong> ——</p>"""
    }
]

# ======================================================
# EXECUTION (V8 PUSH)
# ======================================================

print("=== [V8] Cập nhật mô tả truyện ===")
res_truyen = bypass("POST", f"truyen/{TRUYEN_ID}", {"content": NEW_INTRO})
print(f"Truyen intro update status: {res_truyen.status_code}")

print("\n=== [V8] Lấy danh sách chương ===")
res_chaps = bypass("GET", f"chuong?meta_key=_truyen_id&meta_value={TRUYEN_ID}&per_page=20", {})

if res_chaps.status_code == 200:
    existing_chapters = res_chaps.json()
    slug_to_id = {ch['slug']: ch['id'] for ch in existing_chapters}
    
    print("\n=== [V8] Thực thi nâng cấp kịch tính & vả mặt tối thượng ===")
    for chap_data in chapters_updated:
        slug = chap_data['slug']
        if slug in slug_to_id:
            chap_id = slug_to_id[slug]
            print(f"Đang ghi đè Chương: '{chap_data['title']}' (ID: {chap_id})")
            res_update = bypass("POST", f"chuong/{chap_id}", {
                "title": chap_data["title"],
                "content": chap_data["content"]
            })
            print(f"  -> {res_update.status_code}")
        else:
            print(f"Không tìm thấy chương '{slug}', tạo mới...")
            res_new = bypass("POST", "chuong", {
                "title": chap_data["title"],
                "content": chap_data["content"],
                "status": "publish",
                "meta": {"_truyen_id": TRUYEN_ID}
            })
            print(f"  -> {res_new.status_code}")
        time.sleep(1)
else:
    print(f"Lỗi: {res_chaps.text[:200]}")

print("\n=== HOÀN TẤT CẬP NHẬT TRUYỆN V8 PREMIUM ===")
