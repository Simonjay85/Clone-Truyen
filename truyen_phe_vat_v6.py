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
# THE ULTIMATE SẢNG VĂN MASTERPIECE V6 (9/10 RATING)
# ======================================================

NEW_INTRO = """<p>Năm đó, Lâm Phong bị coi là <strong>vũng bùn hôi thối</strong> — một phế vật vô dụng bị cả gia tộc chà đạp. Trong đêm mưa giông bão giật, chú ruột Lâm Vĩnh Thịnh thiêu rụi di ảnh của cha mẹ hắn, ném hành lý của hắn ra đường như rác rưởi. Hôn thê Triệu Mỹ Nga giẫm gót giày nhọn lên bàn tay rỉ máu của hắn, cười nhạo: <em>"Mày chỉ là một con chó rách, cả đời này tao thà gả cho lợn cũng không bao giờ nhìn tới mày!"</em></p>

<p>Nhưng lưới trời vô hình, ba năm đày ải khổ luyện dưới sự truyền dạy của tài phiệt ẩn dật Vương Kiến Quốc đã biến Lâm Phong thành <strong>Chủ tịch tối cao của Thiên Long Group</strong> — siêu tập đoàn nắm giữ mạch máu tài chính quốc gia. Hắn trở về không phải để thương lượng, mà để <strong>nghiền nát lòng kiêu hãnh của từng kẻ thủ ác</strong>, bắt bọn chúng phải quỳ lạy trong nhục nhã tột cùng!</p>

<p><em>Hãy chuẩn bị tinh thần để xem những màn vả mặt tàn nhẫn, dồn dập và cực kỳ sướng mắt!</em></p>"""

chapters_updated = [
    {
        "slug": "chuong-1-ke-bi-duoi-co-tro-ve",
        "title": "Chương 1: Kẻ Bị Đuổi Cổ Trở Về",
        "content": """<p>Đêm mưa như trút nước xuống thành phố H, sấm sét xé toạc bầu trời đen kịt. Tiếng gầm rú của gió bão như đang phối nhạc cho một màn trở về kinh hoàng.</p>

<p>Chiếc Mercedes-Maybach độc bản lướt đi trong màn đêm, hai bên đèn pha xé rách màn mưa. Ngồi ở hàng ghế sau, Lâm Phong mặc bộ vest đen thủ công, tay đeo chiếc đồng hồ Patek Philippe trị giá cả một biệt thự. Gương mặt hắn như được tạc từ băng đá, đôi mắt sắc lẹm chứa đựng sát khí vô biên khi nhìn dòng nước mưa xối xả ngoài cửa kính.</p>

<p>Trước khi rời khỏi xe, Lâm Phong khẽ lật giở lại tập hồ sơ cũ kỹ về vụ tai nạn sáu năm trước của cha mẹ. Đôi mắt hắn híp lại đầy nghi vấn khi nhìn vào sơ đồ hiện trường vụ tai nạn. Trong báo cáo giám định pháp y và lời khai nhân chứng, có một chi tiết cực kỳ nhỏ đã bị xóa bỏ một cách lộ liễu: sự xuất hiện của một chiếc xe container màu xanh lá cây đậm ở làn đường đối diện chỉ vài giây trước khi cú đâm định mệnh xảy ra. Chiếc xe đó đã biến mất không dấu vết khỏi mọi văn bản chính thức.</p>

<p>— "Nguyễn Văn Hùng... kẻ cầm lái chiếc xe đó, rốt cuộc đang trốn ở xó xỉnh nào?" Lâm Phong lẩm bẩm trong miệng, ánh mắt lạnh lùng tựa như thấu xương.</p>

<p>— "Thiếu gia, sảnh tiệc Lâm gia ở ngay phía trước." Cận vệ Đại Phong cung kính nói, trong mắt tràn đầy sự trung thành và phấn khích. Hắn biết, đêm nay, máu sẽ chảy trên thương trường thành phố H.</p>

<p>Lâm Phong khẽ nhếch môi, một nụ cười lạnh lùng đến rợn tóc gáy. Hắn đang nhớ về đêm mưa ba năm trước. Đêm đó, hắn bị sỉ nhục đến mức không bằng một con chó.</p>

<p>Lâm Vĩnh Thịnh — người chú ruột tàn nhẫn — đã tự tay châm lửa đốt sạch di ảnh của cha mẹ hắn ngay giữa sảnh chính. Tro cốt bay tán loạn trong không khí hòa lẫn với tiếng cười hô hố của cả dòng họ. <em>"Thằng phế vật! Bố mẹ mày chết rồi thì tài sản thuộc về tao! Cầm lấy tập hồ sơ từ bỏ quyền thừa kế này, ký vào rồi cút ra chuồng chó mà sống!"</em></p>

<p>Lâm Kiều Diễm lúc đó tiến lên, nâng ly rượu vang đỏ đổ thẳng lên đầu hắn, nhìn hắn ướt sũng nhục nhã mà cười ré lên: <em>"Ôi, nhìn anh họ của chúng ta giống con chó ướt chưa kìa! Đi xin ăn nhớ né cửa Lâm gia ra nhé!"</em></p>

<p>Đau đớn nhất là Triệu Mỹ Nga, cô gái hắn yêu thương nhất, tiến lên giẫm mạnh gót giày nhọn lên bàn tay đang ôm ngực của hắn, nhổ nước bọt khinh bỉ: <em>"Lâm Phong, nhìn lại bộ dạng nghèo kiết xác của mày đi! Tao thà làm người tình thứ mười của Hoàng thiếu gia còn hơn làm vợ chính thức của loại rác rưởi như mày. Biến đi cho sạch mắt tao!"</em></p>

<p>Lâm Phong bị ném ra đường giữa đêm giông bão, bàn tay rách nát rỉ máu. Nhưng số phận đã cho hắn gặp Vương Kiến Quốc — một đại lão tài chính quốc gia đang ẩn dật, người bị chính thuộc hạ thân tín phản bội dẫn đến tai nạn giao thông trên núi Bạch Vân. Lâm Phong đã dùng tấm thân gầy gò của mình cõng ông lão vượt qua cơn bão tuyết xuống núi cứu mạng.</p>

<p>Để trả ơn, Vương Kiến Quốc nhận hắn làm truyền nhân duy nhất, truyền dạy cho hắn tất cả tinh hoa về quản trị cấp cao, cấu trúc tài chính, pháp lý thương mại và các chiêu thức thâu tóm doanh nghiệp tàn bạo nhất trên thương trường. Ba năm ròng rã khổ luyện như địa ngục, Lâm Phong học hỏi ngày đêm, tự tay thực chiến thâu tóm hàng chục công ty con sắp sụp đổ để xây dựng nên Thiên Long Group — một siêu tập đoàn tài chính hùng mạnh đứng trên đỉnh cao quyền lực.</p>

<p>Hôm nay, hắn trở về.</p>

<p>Xe dừng trước cổng Lâm gia. Hôm nay là tiệc kỷ niệm 30 năm Lâm Thị, sảnh tiệc đèn hoa rực rỡ, khách khứa tấp nập toàn giới siêu giàu.</p>

<p>Lâm Phong bước xuống xe, Đại Phong cầm chiếc ô đen che cho hắn. Hắn đứng sừng sững như một vị thần chiến tranh, khí thế áp đảo khiến không khí xung quanh như giảm xuống âm độ.</p>

<p>Tên bảo vệ trưởng Lâm gia — kẻ năm xưa từng tham gia đập phá đồ đạc của cha mẹ Lâm Phong — nghênh ngang bước ra, chỉ tay vào mặt hắn:</p>

<p>— "Thằng ăn mày nào đây? Đi chỗ khác... Ủa? Lâm Phong?! Thằng phế vật này sao mày chưa chết xó nào à? Cút ngay không tao thả chó cắn nát mặt mày!"</p>

<p>Lâm Phong không thèm chớp mắt. Đại Phong bước lên một bước, nhanh như chớp tóm chặt lấy cổ tay đang chỉ trỏ của tên bảo vệ, bẻ ngoặt ra sau lưng rồi ấn mạnh mặt hắn áp sát vào cánh cổng sắt lạnh lẽo của Lâm gia. Tên bảo vệ lập tức rú lên vì đau đớn, khớp vai tê dại hoàn toàn.</p>

<p>— "Nói với Lâm Vĩnh Thịnh." Lâm Phong tiến tới, đứng sừng sững như một ngọn núi lớn, đôi mắt lạnh lùng nhìn thẳng vào khuôn mặt đang méo mó vì sợ hãi của gã bảo vệ. "Đứa phế vật năm đó... hôm nay trở về để đòi lại từng món nợ máu."</p>"""
    },
    {
        "slug": "chuong-2-bua-tiec-nha-lam-va-cai-tat-dau-tien",
        "title": "Chương 2: Bữa Tiệc Và Video Năm Đó",
        "content": """<p>Bên trong sảnh tiệc Lâm gia, hàng trăm khách mời sang trọng đang nâng ly chúc tụng Lâm Vĩnh Thịnh. Trên sân khấu, Lâm Vĩnh Thịnh mặt mày rạng rỡ, phát biểu đầy tự hào:</p>

<p>— "Tập đoàn Lâm Thị dưới sự dẫn dắt của tôi sẽ sớm thống trị thành phố H—"</p>

<p>Bỗng nhiên, toàn bộ ánh đèn vụt tắt. Màn hình LED khổng lồ phía sau sân khấu đột ngột bật sáng. Nhưng thay vì hình ảnh quảng bá tập đoàn, màn hình lại phát ra những thước phim camera an ninh sắc nét từ ba năm trước: Lâm Vĩnh Thịnh cười man dại đốt sạch di ảnh cha mẹ Lâm Phong ngay giữa sảnh chính, Lâm Kiều Diễm đổ rượu lên đầu hắn cười cợt, và Triệu Mỹ Nga thẳng tay giẫm gót giày nhọn rách nát tay hắn sỉ nhục.</p>

<p>Cả sảnh tiệc bùng nổ những tiếng xầm xì kinh hoàng. Khách mời trố mắt nhìn nhau, hướng ánh mắt khinh bỉ tột cùng về phía Lâm Vĩnh Thịnh và Lâm gia. Sự thật nhục nhã của dòng họ mang danh thượng lưu bị lột trần công khai trước bàn dân thiên hạ.</p>

<p>Lâm Vĩnh Thịnh mặt tái mét, gầm lên điên cuồng:</p>

<p>— "Tắt đi! Đứa nào làm trò này?! Kỹ thuật đâu, tao giết tụi mày!"</p>

<p>— "Chú Hai, xem tiếp đi chứ, phim hay mới chỉ bắt đầu mà."</p>

<p>Cửa sảnh tiệc bị đạp tung. Lâm Phong bước vào, vest đen tột đỉnh quyền lực, khí thế lạnh lùng tàn nhẫn càn quét cả khán phòng khiến ai nấy đều run rẩy nín thở.</p>

<p>Lâm Kiều Diễm nhìn thấy hắn, cơn giận dữ lấn át nỗi sợ, cô ta chỉ tay hét lên:</p>

<p>— "Thằng phế vật! Mày dám đến đây làm loạn tiệc của gia đình tao? Bảo vệ đâu, đập gãy hai chân nó vứt ra đường cho tao!"</p>

<p>Đám bảo vệ Lâm gia cầm gậy lao lên, nhưng chưa kịp áp sát đã bị các vệ sĩ chuyên nghiệp của Lâm Phong nhanh gọn tước vũ khí, khống chế chặt trên sàn đấu bằng những thế khóa nghiệp vụ. Sự uy phong và lạnh lùng của lực lượng vệ sĩ áo xám khiến cả phòng tiệc chết lặng, không ai dám hó hé.</p>

<p>Lâm Phong bước từng bước lên sân khấu, đứng đối diện với Lâm Vĩnh Thịnh đang run bần bật:</p>

<p>— "Mày... mày lấy đâu ra tiền thuê đám giang hồ này? Mày chỉ là một thằng ăn mày!" Lâm Vĩnh Thịnh hét lớn để che giấu sự sợ hãi.</p>

<p>Lâm Phong khẽ cười, nụ cười đầy vẻ khinh bỉ. Luật sư Trần bước lên, rút ra tập hồ sơ pháp lý đóng dấu đỏ chói:</p>

<p>— "Ông Lâm Vĩnh Thịnh, Thiên Long Group đã mua đứt 200 tỷ nợ xấu của Lâm Thị tại ba ngân hàng liên minh. Theo điều khoản thế chấp khẩn cấp, chúng tôi chính thức niêm phong toàn bộ dinh thự này và đóng băng hoạt động của tập đoàn Lâm Thị ngay lập tức!"</p>

<p>Lâm Vĩnh Thịnh cười điên cuồng:</p>

<p>— "Ha ha! Mày hù ai đó hả thằng ranh? Ngân hàng Đông Á là đồng minh của tao, làm sao họ ký chuyển nợ cho mày được—"</p>

<p>Chưa kịp nói hết câu, ba vị Giám đốc đại diện của ba ngân hàng lớn nhất thành phố bước vào sảnh tiệc, cung kính cúi đầu 90 độ trước Lâm Phong trước sự chứng kiến của cả căn phòng:</p>

<p>— "Kính chào ngài Lâm Phong Chủ tịch tối cao! Chúng tôi đã hoàn tất toàn bộ thủ tục niêm phong tài sản của Lâm gia theo lệnh của ngài!"</p>

<p>Lâm Vĩnh Thịnh nhìn cảnh tượng đó mà như ngã từ trên trời xuống đất, hai chân đứng không vững, quỳ sụp xuống sàn sân khấu.</p>

<p>Lâm Kiều Diễm hoảng loạn chạy lên định cào cấu Lâm Phong, nhưng chưa kịp tiến lại gần, cô ta đã bị Đại Phong giơ tay chặn đứng một cách dứt khoát. Lực đẩy mạnh mẽ khiến cô ta loạng choạng ngã nhào vào đống ly pha lê đổ vỡ cạnh sân khấu, đầm dạ hội ướt sũng trong đống rượu vang rơi vãi.</p>

<p>— "Anh Phong... cứu em..." Kiều Diễm khóc lóc thảm thiết, nhìn khuôn mặt mình dính đầy rượu vang đỏ như máu.</p>

<p>Lâm Phong bước từng bước thong thả đến bên cạnh, đứng sừng sững nhìn xuống cô ta với ánh mắt như nhìn một đống rác rưởi. Hắn nhẹ nhàng dẫm gót giày da bóng loáng lên bản giao ước nợ rách nát trước mặt cô ta, giọng nói thản nhiên nhưng lạnh buốt:</p>

<p>— "Lâm Kiều Diễm, ngày xưa cô đổ rượu vang lên đầu tôi, ép tôi liếm giày cho cô. Bây giờ dòng họ của cô đang nợ tôi 200 tỷ. Chỉ cần tôi búng tay, cả đời cô và bố cô sẽ phải ở trong phòng biệt giam để trả nợ. Đây mới chỉ là lãi suất thôi, em họ à." Hắn nhìn xuống Lâm Vĩnh Thịnh đang run rẩy. "Chú Hai, chuẩn bị tinh thần đi, tôi sẽ từ từ lột da từng đứa một."</p>"""
    },
    {
        "slug": "chuong-3-nguoi-tinh-cu-va-ten-tieu-nhan",
        "title": "Chương 3: Người Tình Cũ Và Tên Tiểu Nhân",
        "content": """<p>Tại nhà hàng Seasons siêu sang, Hoàng Tuấn Kiệt đang ôm eo Triệu Mỹ Nga ngồi ở bàn VIP số 7. Tuấn Kiệt cười đắc ý, ném một xấp tiền dày xuống sàn dưới chân Lâm Phong vừa bước vào:</p>

<p>— "Ê thằng phế vật! Nghe nói mày mới về hả? Nhặt đống tiền này lên rồi bò quanh bàn liếm sạch giày cho tao và Mỹ Nga, tao sẽ bố trí cho mày làm chân rửa bát ở đây!"</p>

<p>Triệu Mỹ Nga che miệng cười khinh bỉ, ánh mắt đầy sự ghê tởm nhìn Lâm Phong:</p>

<p>— "Lâm Phong ơi là Lâm Phong, mặc vest giả hiệu thì cũng không che được cái mùi nghèo kiết xác của mày đâu. Nhặt tiền đi kìa, bằng cả năm lương làm thuê của mày đó!"</p>

<p>Khách xung quanh đổ dồn ánh mắt châm biếm về phía Lâm Phong. Nhưng gương mặt hắn vẫn tĩnh lặng như nước hồ mùa thu. Hắn nhìn xấp tiền dưới chân, rồi nhìn thẳng vào Hoàng Tuấn Kiệt.</p>

<p>— "Hoàng Tuấn Kiệt, anh thích ném tiền lắm đúng không?" Lâm Phong khẽ hỏi, giọng nói mang theo cái lạnh thấu xương.</p>

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

<p>— "Bẩn áo tôi." Lâm Phong lạnh lùng gạt tay cô ta ra khiến cô ta ngã nhào lên xấp tiền đang rải rác dưới đất. Hắn giẫm thẳng lên đống tiền đó, nhìn cô ta bằng ánh mắt đầy sự khinh bỉ tột cùng. "Triệu Mỹ Nga, đống tiền này cô thích thì cứ nhặt lấy mà dùng để mua váy cưới rách của cô đi."</p>

<p>Lâm Phong bước đi trong sự cung kính cúi đầu của toàn bộ nhân viên nhà hàng, để lại hai kẻ tiểu nhân đang khóc lóc nhục nhã giữa đống tiền rơi vãi dưới đất.</p>"""
    },
    {
        "slug": "chuong-4-man-hop-bao-chan-dong",
        "title": "Chương 4: Họp Báo Và Đòn Phản Công Trong Bóng Tối",
        "content": """<p>Buổi họp báo công bố dự án 5.000 tỷ của Thiên Long Group tại thành phố H diễn ra vô cùng hoành tráng, thu hút toàn bộ sự chú ý của giới truyền thông quốc gia. Sự xuất hiện rực rỡ của Lâm Phong làm lu mờ hoàn toàn mọi thế lực cũ.</p>

<p>Nhưng sự nhục nhã của Lâm gia và Hoàng gia đã đẩy Lâm Vĩnh Thịnh vào bước đường cùng. Lão liên thủ với Tạ Vĩnh Bình — Phó Chủ tịch Hiệp hội Thương nhân, kẻ nắm giữ quyền lực đen trong giới ngân hàng địa phương.</p>

<p>— "Thằng ranh con đó muốn diệt chúng ta." Lâm Vĩnh Thịnh nghiến răng bên ly rượu mạnh. "Tôi đã chuẩn bị một bộ hồ sơ giả hoàn hảo chứng minh Thiên Long rửa tiền. Chỉ cần anh Bình ký lệnh phong tỏa khẩn cấp tài khoản của nó, dự án 5.000 tỷ sẽ chết yểu. Lúc đó, tôi sẽ thuê giang hồ lấy mạng nó!"</p>

<p>Tạ Vĩnh Bình cười lạnh, ánh mắt đầy vẻ tham lam:</p>

<p>— "Một thằng nhóc từ nơi khác về mà đòi làm loạn ở đây sao? Cứ để tôi ra tay, tôi sẽ bắt nó phải quỳ xuống xin lỗi chúng ta!"</p>

<p>Sáng hôm sau, Tạ Vĩnh Bình dẫn đầu một đoàn thanh tra liên ngành rầm rộ ập vào trụ sở Thiên Long Group. Lão ngang tàng bước vào phòng làm việc của Lâm Phong, ném tờ lệnh phong tỏa lên bàn, cười đắc ý:</p>

<p>— "Lâm Phong! Toàn bộ tài khoản 2.000 tỷ của mày đã bị phong tỏa khẩn cấp để điều tra tội rửa tiền. Mày xong đời rồi con trai ạ! Ở thành phố H này, tao mới là luật lệ!"</p>

<p>Lâm Vĩnh Thịnh đứng đằng sau cũng cười hô hố đầy đắc thắng:</p>

<p>— "Ha ha! Thằng phế vật! Mày tưởng mày mạnh lắm sao? Bây giờ không có tiền thanh toán cho nhà thầu, dự án của mày sẽ bị tịch thu! Mày lại chuẩn bị đi ăn mày tiếp đi!"</p>

<p>Nhân viên Thiên Long xung quanh hoang mang cực độ, không khí căng thẳng đến nghẹt thở.</p>

<p>Lâm Phong chậm rãi đứng dậy từ ghế chủ tịch. Gương mặt hắn không hề có một chút lo sợ, ngược lại, khóe môi hắn khẽ cong lên một đường cười đầy tàn nhẫn:</p>

<p>— "Tạ Vĩnh Bình, ông nghĩ cái chức Phó Chủ tịch Hiệp hội của ông lớn lắm sao?"</p>

<p>— "Thằng ranh! Mày dám thái độ đó với tao?!" Tạ Vĩnh Bình đập bàn quát lớn.</p>

<p>— "Minh Nguyệt, chiếu phương án 'Lưới Trời' lên cho họ xem." Lâm Phong thản nhiên ra lệnh.</p>

<p>Màn hình lớn trong văn phòng lập tức bật sáng, hiển thị toàn bộ hồ sơ giao dịch đen, các khoản hối lộ trị giá hàng triệu USD và danh sách 12 tài khoản bí mật ở nước ngoài của Tạ Vĩnh Bình cùng Lâm Vĩnh Thịnh.</p>

<p>— "Cái... cái gì?!" Tạ Vĩnh Bình lắp bắp, mặt cắt không còn giọt máu.</p>

<p>— "Đây mới chỉ là món khai vị thôi." Lâm Phong lạnh lùng nhìn hai kẻ đang run rẩy trước mặt. "Trò chơi chính thức bắt đầu rồi."</p>"""
    },
    {
        "slug": "chuong-5-bay-cua-ke-thu-va-don-phan-cong",
        "title": "Chương 5: Khi Cả Thành Phố Quay Lưng",
        "content": """<p>Sau khi lệnh phong tỏa từ Tạ Vĩnh Bình được ban hành, một cơn ác mộng thực sự có quy mô chưa từng thấy đã ập xuống Thiên Long Group. Suốt 48 giờ đồng hồ liên tiếp, cả thành phố H dường như quay lưng lại với Lâm Phong. Liên minh ngân hàng dưới trướng Tạ Vĩnh Bình phong tỏa toàn bộ 2.000 tỷ đồng tiền mặt của tập đoàn. Các đối tác, nhà cung cấp lớn nhỏ lập tức nháo nhào như ong vỡ tổ.</p>

<p>Tại văn phòng Chủ tịch, điện thoại đổ chuông liên tục không ngừng nghỉ. Tiếng gào thét, trách móc và hoảng loạn của các cổ đông vang lên qua loa thoại. 
— "Lâm Phong! Cậu làm cái gì thế hả? Tại sao tài khoản lại bị điều tra rửa tiền? Dự án 5.000 tỷ của chúng ta chuẩn bị khởi công, bây giờ bị đình chỉ khẩn cấp rồi! Cậu có biết thiệt hại mỗi ngày lên tới hàng chục tỷ không?!" 
Lâm Phong vẫn ngồi yên vị trên chiếc ghế da, gương mặt không một chút gợn sóng, thản nhiên cúp máy mà không thèm giải thích một lời.</p>

<p>Đúng lúc đó, cuộc gọi từ Trần Thế Nam — Tổng giám đốc Nam Sơn Construction, nhà thầu xây dựng lớn nhất dự án — đổ chuông. Giọng gã bên kia đầu dây đầy vẻ đắc ý và cợt nhả:
— "Lâm tổng, à không, Lâm phế vật chứ nhỉ? Nghe nói tài khoản Thiên Long sạch sành sanh rồi hả? Nam Sơn chúng tôi không thể hợp tác với một kẻ lừa đảo. Tôi đã ký đơn phương hủy hợp đồng xây dựng, và toàn bộ máy móc đã được chuyển sang công trường của Lâm gia rồi. Lâm Vĩnh Thịnh đại nhân đã nhận chúng tôi làm đối tác chiến lược. Mày chuẩn bị ra đường nhặt rác tiếp đi con trai!"</p>

<p>Cùng lúc đó, làn sóng truyền thông bẩn bùng nổ dữ dội trên mọi nền tảng mạng xã hội và các mặt báo lớn nhỏ. Những cái tít giật gân xuất hiện dày đặc: <em>"Vén màn bộ mặt thật của Chủ tịch Thiên Long Group", "Siêu dự án 5.000 tỷ chỉ là bánh vẽ để rửa tiền?", "Kẻ bị Lâm gia trục xuất ba năm trước nay trở về làm trò bịp bợm"</em>. Các bài phân tích tài chính giả mạo liên tục được đăng tải nhằm định hướng dư luận, biến Lâm Phong thành một kẻ tội đồ kinh tế của cả thành phố H.</p>

<p>Bên ngoài tòa nhà Thiên Long, hàng trăm người biểu tình được thuê mướn và đám phóng viên lá cải vây kín mọi lối ra vào. Bầu không khí căng thẳng, u ám bao trùm toàn bộ văn phòng. Nhân viên Thiên Long hoang mang tột độ, nhiều người bắt đầu thu dọn đồ đạc để tìm đường lui.</p>

<p>Đỉnh điểm của sự phẫn uất diễn ra vào buổi chiều ngày thứ hai. Minh Nguyệt, trợ lý trung thành của Lâm Phong, ôm tập tài liệu chứng cứ tuyệt mật bước ra khỏi sảnh chính tòa nhà để đến nộp cho cơ quan điều tra cấp cao. Ngay khi bóng dáng cô vừa xuất hiện, hàng chục máy ảnh, camera chớp nháy liên hồi, cùng một đám phóng viên hung hãn lao tới như đàn kền kền ngửi thấy mùi xác chết.</p>

<p>— "Cô Minh Nguyệt! Hãy trả lời đi! Lâm Phong thực chất có phải là con rối rửa tiền của thế lực ngầm không?!"
— "Có phải Thiên Long Group chuẩn bị tuyên bố phá sản?!"
Đám người xô đẩy dữ dội. Một gã đàn ông to béo được thuê mướn cố tình huých mạnh vào vai Minh Nguyệt. Cú huých tàn nhẫn khiến cô mất đà, ngã nhào từ trên bậc thềm bê tông cao xuống sân gạch lạnh lẽo. Tập tài liệu vương vãi khắp nơi. Đầu gối cô bị mài xuống nền gạch thô ráp, máu tươi rỉ ra thấm đỏ cả chiếc váy công sở màu nhạt. Chiếc túi xách bị giật đứt quai, điện thoại rơi vỡ vụn.</p>

<p>Nhưng thay vì khóc lóc bỏ chạy, Minh Nguyệt run rẩy bò dậy, mặc cho vết thương ở đầu gối đau đớn đến thấu xương. Cô bò trên đất, cẩn thận nhặt lại từng trang tài liệu, ôm chặt vào lồng ngực như bảo vệ sinh mệnh của chính mình. Đối diện với hàng chục ống kính đang dí sát vào mặt, cô ngẩng cao đầu, ánh mắt ngập tràn sự kiên định tột cùng, hét lớn giữa đám đông:
— "Các người im miệng! Lâm tổng không bao giờ là kẻ lừa đảo! Thiên Long Group sẽ không sụp đổ! Sự thật sẽ sớm được sáng tỏ, và những kẻ đứng sau trò bẩn thỉu này sẽ phải quỳ xuống tạ tội!"</p>

<p>Đứng trên tầng 30 nhìn xuống qua cửa kính sát đất, Lâm Phong chứng kiến toàn bộ cảnh tượng đó. Hai bàn tay hắn siết chặt lại đến mức khớp xương trắng bệch, phát ra tiếng rắc rắc nhỏ, đôi mắt hắn rực cháy ngọn lửa giận dữ vô biên. Hắn hận không thể lập tức xuống nghiền nát đầu những kẻ vừa chạm vào cô. Nhưng hắn bắt buộc phải nhẫn nhịn. Đây là nước cờ cuối cùng trong phương án 'Lưới Trời' mà hắn và Vương Kiến Quốc đã dày công lập nên: <em>"Muốn diệt sạch thế lực chống lưng đứng sau Lâm gia, phải cho bọn chúng cảm thấy chúng ta đã hoàn toàn sụp đổ và lâm vào đường cùng, để bọn chúng tự đắc ý lộ diện hết."</em></p>

<p>Hắn hít một hơi thật sâu, giọng nói trầm xuống như băng đá nghìn năm, khẽ nói vào tai nghe liên lạc với Đại Phong:
— "Đại Phong, đón Minh Nguyệt vào. Chăm sóc vết thương cho cô ấy. Hãy bảo cô ấy nhẫn nhịn thêm vài giờ nữa thôi... Tôi sẽ bắt cả thành phố H này phải quỳ xuống chân cô ấy để tạ lỗi."</p>

<p>Sáng hôm sau, Lâm Vĩnh Thịnh và Tạ Vĩnh Bình hí hửng tổ chức họp báo công bố việc thu hồi dự án của Thiên Long ngay tại sảnh chính của khách sạn Hoàng Cung, muốn dồn Lâm Phong vào cái chết xã hội trước hàng trăm phóng viên quốc gia.</p>

<p>— "Lâm Phong! Mày định quỳ lạy xin tha hay để tao tống mày vào tù?" Tạ Vĩnh Bình đứng trên bục phát biểu gầm lên đắc thắng trước hàng trăm phóng viên.</p>

<p>Lâm Phong khẽ gật đầu với phía cửa sảnh.</p>

<p>Ngay lập tức, một đoàn người mặc vest đen nghiêm nghị bước vào. Dẫn đầu là **Thống đốc Ngân hàng Nhà nước** và **Cục trưởng Cục Điều tra Tội phạm Kinh tế Bộ Công an**.</p>

<p>Cả hội trường họp báo lập tức im phăng phắc như tờ.</p>

<p>Thống đốc Ngân hàng Nhà nước bước lên bục phát biểu, dõng dạc thông báo:</p>

<p>— "Chúng tôi chính thức xác nhận toàn bộ nguồn vốn của Thiên Long Group là hoàn toàn hợp pháp và minh bạch. Đồng thời, lệnh phong tỏa tài khoản của Thiên Long do Tạ Vĩnh Bình ký là hành vi lạm dụng quyền hạn trái pháp luật nhằm mục đích tư lợi cá nhân!"</p>

<p>Cục trưởng Cục Điều tra bước xuống, chỉ tay thẳng vào mặt Tạ Vĩnh Bình đang há hốc miệng kinh hoàng:</p>

<p>— "Tạ Vĩnh Bình! Ông bị bắt khẩn cấp vì tội nhận hối lộ, rửa tiền và lạm dụng chức vụ quyền hạn gây hậu quả nghiêm trọng! Yêu cầu khóa tay đối tượng!"</p>

<p>Hai cảnh sát hình sự lao lên, đè nghiến Tạ Vĩnh Bình xuống sàn họp báo trước hàng trăm ống kính camera đang phát sóng trực tiếp toàn quốc. Tạ Vĩnh Bình sợ hãi đến mức tiểu cả ra quần, khóc lóc thảm thiết:</p>

<p>— "Oan uổng quá! Lâm chủ tịch! Lâm thiếu gia cứu tôi với! Tôi bị Lâm Vĩnh Thịnh xúi giục!"</p>

<p>Lâm Vĩnh Thịnh đứng cạnh đó mặt mũi xám ngoét như người chết trôi, định lén lút lùi ra cửa để bỏ trốn.</p>

<p>— "Lâm Vĩnh Thịnh, chú định đi đâu?" Giọng nói của Lâm Phong vang lên như tiếng gọi của tử thần qua loa phóng thanh.</p>

<p>Đại Phong cùng các vệ sĩ chặn đứng lối thoát của Lâm Vĩnh Thịnh, đá mạnh vào nhượng chân khiến lão quỳ sụp xuống sàn xi măng lạnh lẽo trước hàng trăm phóng viên.</p>

<p>— "Chú Hai, trò chơi chỉ mới bắt đầu thôi. Chú đã chuẩn bị tinh thần để trả nợ máu cho cha mẹ tôi chưa?" Lâm Phong nhìn xuống lão bằng ánh mắt lạnh lùng không một chút hơi người.</p>"""
    },
    {
        "slug": "chuong-6-dam-cuoi-bi-pha",
        "title": "Chương 6: Đám Cưới Và Sự Thật Năm Xưa",
        "content": """<p>Hôm nay là ngày cưới của Hoàng Tuấn Kiệt và Triệu Mỹ Nga tại sảnh tiệc lộng lẫy nhất của khách sạn Hoàng Cung. Triệu Mỹ Nga khoác lên mình chiếc váy cưới thiết kế tinh xảo, nở nụ cười kiêu ngạo đón tiếp khách khứa. Cô ta nghĩ rằng dù Hoàng gia đang gặp khó khăn, nhưng đám cưới này vẫn giúp cô ta bước chân vào giới thượng lưu.</p>

<p>Nhưng ngay khi cô dâu chú rể chuẩn bị bước lên lễ đường bước vào giờ G làm lễ, một đội ngũ cưỡng chế niêm phong tài sản của tòa án phối hợp cùng cảnh sát ập vào.</p>

<p>Họ thô bạo lột chiếc nhẫn kim cương bốn cara trên ngón tay Triệu Mỹ Nga, giật phắt chiếc vòng cổ ngọc trai đắt tiền trên cổ cô ta trước sự chứng kiến của năm trăm khách mời quý tộc.</p>

<p>— "Tài sản này thuộc danh mục thế chấp nợ xấu của Hoàng gia tại Thiên Long Group và đang bị niêm phong khẩn cấp để thu hồi nợ!" Đại diện tòa án lạnh lùng thông báo.</p>

<p>Hoàng Tuấn Kiệt hoảng loạn định bỏ trốn thì bị cảnh sát đè chặt xuống sàn lễ đường hoa tươi, khóa tay ra sau vì cáo buộc lừa đảo chiếm đoạt tài sản và trốn thuế.</p>

<p>Khách mời bên dưới nhao nhao chửi rủa, ném hoa cưới và những ly nước vào người cô dâu chú rể đang thảm hại dưới đất. Hoàng gia sụp đổ hoàn toàn ngay trong ngày cưới!</p>

<p>Triệu Mỹ Nga tóc tai bù xù, váy cưới rách nát, khóc lóc thảm thiết gọi điện cho Lâm Phong để cầu xin. Đầu dây bên kia kết nối, giọng Lâm Phong vang lên vô cùng bình thản:</p>

<p>— "Mỹ Nga, đám cưới vui vẻ chứ?"</p>

<p>— "Phong! Em sai rồi! Em là con khốn! Xin anh hãy nể tình xưa nghĩa cũ cứu em với... Hoàng Tuấn Kiệt bị bắt rồi, em không còn nhà để về nữa..." Mỹ Nga quỳ thụp xuống đống đổ nát của lễ đường đám cưới, gào khóc xin xỏ.</p>

<p>— "Tình xưa nghĩa cũ?" Lâm Phong khẽ cười lạnh. "Nghĩa cũ của cô là giẫm gót giày lên bàn tay rỉ máu của tôi đêm đó sao? Cô yên tâm, tôi đã bảo người sắp xếp cho cô một công việc rồi. Làm công nhân vệ sinh quét rác ở chi nhánh vùng sâu vùng xa của Thiên Long. Hãy dùng cả đời cô để quét sạch đống rác rưởi trong tâm hồn mình đi."</p>

<p>Lâm Phong dứt khoát cúp máy. Triệu Mỹ Nga trợn mắt nhìn màn hình điện thoại đã tắt, tinh thần hoàn toàn sụp đổ, điên loạn la hét giữa lễ đường trống trải.</p>"""
    },
    {
        "slug": "chuong-7-man-ket-toan-voi-gia-toc-lam",
        "title": "Chương 7: Kết Toán — Và Sự Thật Về Đêm Tai Nạn",
        "content": """<p>Tại đại sảnh dinh thự Lâm gia, bầu không khí âm u lạnh lẽo như nhà xác. Lâm Phong ngồi sừng sững trên chiếc ghế chủ tọa bằng gỗ mun của gia tộc. Đi sau hắn là mười vệ sĩ xám đứng nghiêm trang.</p>

<p>Lâm Vĩnh Thịnh bị Đại Phong xách cổ ném thẳng xuống sàn nhà dưới chân Lâm Phong, mặt mũi đầy máu và vết bầm dập.</p>

<p>— "Lâm Phong! Mày là đồ nghịch tử! Mày dám đối xử với chú ruột mày như thế này sao?! Tao sẽ kiện mày ra tòa!" Lâm Vĩnh Thịnh gào hét trong vô vọng.</p>

<p>Lâm Phong không nói một lời, chỉ khẽ gật đầu. Luật sư Trần ném xấp tài liệu dày cộp kèm đĩa CD bằng chứng xuống trước mặt lão:</p>

<p>— "Ông Lâm Vĩnh Thịnh, đây là toàn bộ bằng chứng về việc ông đã thuê Nguyễn Văn Hùng lái xe container cố tình đâm chết vợ chồng ông Lâm Đình Sơn sáu năm trước để cướp tập đoàn Lâm Thị. Chúng tôi cũng đã tìm ra tài khoản Thụy Sĩ chuyển tiền thuê sát thủ của ông!"</p>

<p>Đồng thời, Nguyễn Văn Hùng — gã tài xế container năm xưa — bị cảnh sát áp giải bước vào phòng, chỉ tay thẳng vào mặt Lâm Vĩnh Thịnh:</p>

<p>— "Chính là lão ta! Lão ta đã đưa tôi 5 tỷ để đâm chết xe của vợ chồng ông Sơn!"</p>

<p>Lâm Vĩnh Thịnh nghe xong tai ù đi, cả người run bắn lên như cầy sấy. Lão lết đến ôm chặt chân Lâm Phong, khóc lóc thảm thiết, tự vả bôm bốp vào mặt mình:</p>

<p>— "Phong! Cháu ơi! Chú sai rồi! Chú bị quỷ ám! Xin cháu nể tình máu mủ tha cho chú một con đường sống... Chú sẽ trả lại toàn bộ cổ phần cho cháu!"</p>

<p>Lâm Phong cúi xuống nhìn lão, ánh mắt đầy sự ghê tởm tột độ. Hắn dùng gót giày da giẫm thẳng lên khuôn mặt đang cầu xin của Lâm Vĩnh Thịnh, nghiền mạnh xuống sàn nhà khiến lão đau đớn rú lên thảm thiết:</p>

<p>— "Máu mủ? Lúc chú thuê người đâm chết cha mẹ tôi, chú có nghĩ đến hai chữ máu mủ không? Lúc chú thiêu rụi di ảnh cha mẹ tôi, chú có nghĩ đến máu mủ không?"</p>

<p>Cảnh sát hình sự lập tức lao lên, khóa chặt tay Lâm Vĩnh Thịnh áp giải đi trước sự chứng kiến của cả gia tộc Lâm đang quỳ lạy run rẩy xung quanh.</p>

<p>Lâm Phong đứng dậy, phủi nhẹ ống quần vest. Hắn nhìn lướt qua Lâm Quốc Bình đang quỳ rạp dưới đất không dám ngẩng đầu:</p>

<p>— "Lâm gia từ hôm nay đổi chủ. Kẻ nào dám có ý kiến phản đối?"</p>

<p>Cả gia tộc Lâm đồng loạt dập đầu sát đất, run rẩy đồng thanh vang lên: <em>"Không dám! Kính chào Lâm chủ tịch!"</em></p>

<p>Lâm Phong bước ra ngoài sảnh lớn, ngẩng đầu nhìn lên bầu trời đêm đã tạnh mưa. Nợ máu cuối cùng đã được trả bằng máu và nước mắt của kẻ thù.</p>"""
    },
    {
        "slug": "chuong-8-binh-minh-cua-ke-tro-ve",
        "title": "Chương 8: Bình Minh — Và Những Gì Còn Lại",
        "content": """<p>Một tháng sau sóng gió thương trường chấn động thành phố H.</p>

<p>Mọi ồn ào và bụi bặm của những cuộc trả thù cuối cùng cũng lắng xuống. Lâm gia từ hôm nay đã thuộc về Lâm Phong, nhưng hắn không chọn ở lại căn penthouse hào nhoáng ở trung tâm thành phố. Hắn chọn quay về ngôi biệt thự cổ của gia đình năm xưa — nơi từng bị Lâm Vĩnh Thịnh chiếm đoạt và tàn phá.</p>

<p>Dưới bàn tay trùng tu tỉ mỉ của Lâm Phong, ngôi nhà cũ đã tìm lại được vẻ ấm cúng và tôn nghiêm vốn có. Tại sảnh thờ chính, ánh nắng sớm khẽ len lỏi qua ô cửa sổ bằng gỗ, chiếu lên bức hoành phi và di ảnh của cha mẹ hắn đã được phục chế hoàn hảo.</p>

<p>Lâm Phong đứng sừng sững trước bàn thờ, trên người mặc bộ đồ đơn giản nhưng thanh lịch. Hắn cầm ba nén hương vừa được đốt cháy, làn khói trầm hương nghi ngút bay lên mang theo mùi hương thanh tịnh. Hắn chậm rãi cúi đầu ba vái, đôi mắt vốn lạnh lùng tàn nhẫn trên thương trường giờ đây dâng lên một tầng sương mỏng, tràn đầy cảm xúc ấm áp.</p>

<p>Hắn khẽ cắm nén hương vào bát đồng cổ, rồi nhìn thẳng vào di ảnh cha mẹ, nói nhỏ với giọng run run nhưng đầy kiêu hãnh:
— "Ba, mẹ... Đứa phế vật bị người ta chà đạp năm đó, hôm nay đã thực sự mang vinh quang trở về rồi. Những kẻ hãm hại gia đình ta đều đã phải trả giá đắt trước pháp luật. Con đã làm được rồi."</p>

<p>Một bàn tay ấm áp, mềm mại khẽ luồn vào lòng bàn tay hắn, siết nhẹ. Lâm Phong quay đầu lại, nhìn thấy Minh Nguyệt đang đứng bên cạnh. Trên đầu gối cô, vết sẹo từ cú ngã hôm đó đã mờ dần, được che đi bằng một chiếc đầm trắng tinh khôi như hoa cúc sớm. Trong mắt cô lúc này cũng lấp lánh nước mắt xúc động.</p>

<p>Minh Nguyệt khẽ tiến lên, thắp một nén hương, cúi đầu cung kính vái lạy:
— "Thưa hai bác, con là Minh Nguyệt. Từ nay về sau, con xin nguyện ở bên cạnh chăm sóc và đồng hành cùng anh Phong trên mọi nẻo đường đời. Xin hai bác yên lòng yên nghỉ."</p>

<p>Lâm Phong nhìn cô, trái tim hắn tràn ngập sự ấm áp chưa từng có suốt sáu năm qua. Hắn đưa tay nhẹ nhàng lau đi giọt nước mắt lăn trên má cô, khẽ kéo cô vào lòng, tựa cằm lên mái tóc thơm ngát của cô.</p>

<p>— "Cảm ơn em, Minh Nguyệt. Nếu không có sự kiên định của em đêm hôm đó, có lẽ tôi đã không thể hoàn thành ván cờ này trọn vẹn như vậy." Hắn thì thầm.</p>

<p>— "Được ở bên anh, nhìn anh tìm lại công lý, đó là hạnh phúc lớn nhất của đời em." Minh Nguyệt khẽ ngẩng đầu mỉm cười, đôi mắt rạng rỡ.</p>

<p>Hắn quay sang nắm lấy bàn tay mềm mại của Minh Nguyệt, dắt cô bước ra ngoài sảnh lớn. Ánh bình minh rực rỡ xua tan đi làn sương mù cuối cùng, chiếu rọi hai bóng hình cao lớn và dịu dàng đi bên nhau hướng về phía tương lai tươi sáng phía trước. Đứa phế vật năm đó nay đã thực sự đứng trên đỉnh cao quyền lực, tìm lại được cả vương quyền lẫn tình yêu đích thực của cuộc đời mình.</p>

<p style="text-align:center; margin-top: 40px;">—— <strong>HẾT</strong> ——</p>"""
    }
]

# ======================================================
# EXECUTION (V6 PUSH)
# ======================================================

print("=== [V6] Cập nhật mô tả truyện ===")
res_truyen = bypass("POST", f"truyen/{TRUYEN_ID}", {"content": NEW_INTRO})
print(f"Truyen intro update status: {res_truyen.status_code}")

print("\n=== [V6] Lấy danh sách chương ===")
res_chaps = bypass("GET", f"chuong?meta_key=_truyen_id&meta_value={TRUYEN_ID}&per_page=20", {})

if res_chaps.status_code == 200:
    existing_chapters = res_chaps.json()
    slug_to_id = {ch['slug']: ch['id'] for ch in existing_chapters}
    
    print("\n=== [V6] Thực thi vả mặt dồn dập, ghi đè nội dung 9/10 ===")
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

print("\n=== HOÀN TẤT CẬP NHẬT TRUYỆN V6 ===")
