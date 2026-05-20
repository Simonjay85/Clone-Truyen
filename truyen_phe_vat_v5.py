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
# THE ULTIMATE SẢNG VĂN MASTERPIECE V5
# ======================================================

NEW_INTRO = """<p>Năm đó, Lâm Phong bị coi là <strong>vũng bùn hôi thối</strong> — một phế vật vô dụng bị cả gia tộc chà đạp. Trong đêm mưa giông bão giật, chú ruột Lâm Vĩnh Thịnh thiêu rụi di ảnh của cha mẹ hắn, ném hành lý của hắn ra đường như rác rưởi. Hôn thê Triệu Mỹ Nga giẫm gót giày nhọn lên bàn tay rỉ máu của hắn, cười nhạo: <em>"Mày chỉ là một con chó rách, cả đời này tao thà gả cho lợn cũng không bao giờ nhìn tới mày!"</em></p>

<p>Nhưng lưới trời vô hình, ba năm đày ải khổ luyện dưới sự truyền dạy của tài phiệt ẩn dật Vương Kiến Quốc đã biến Lâm Phong thành <strong>Chủ tịch tối cao của Thiên Long Group</strong> — siêu tập đoàn nắm giữ mạch máu tài chính quốc gia. Hắn trở về không phải để thương lượng, mà để <strong>nghiền nát lòng kiêu hãnh của từng kẻ thủ ác</strong>, bắt bọn chúng phải quỳ lạy trong nhục nhã tột cùng!</p>

<p><em>Hãy chuẩn bị tinh thần để xem những màn vả mặt tàn nhẫn, dồn dập và cực kỳ sướng mắt!</em></p>"""

chapters_updated = [
    {
        "slug": "chuong-1-ke-bi-duoi-co-tro-ve",
        "title": "Chương 1: Kẻ Bị Đuổi Cổ Trở Về",
        "content": """<p>Đêm mưa như trút nước xuống thành phố H, sấm sét xé toạc bầu trời đen kịch. Tiếng gầm rú của gió bão như đang phối nhạc cho một màn trở về kinh hoàng.</p>

<p>Chiếc Mercedes-Maybach độc bản lướt đi trong màn đêm, hai bên đèn pha xé rách màn mưa. Ngồi ở hàng ghế sau, Lâm Phong mặc bộ vest đen thủ công, tay đeo chiếc đồng hồ Patek Philippe trị giá cả một biệt thự. Gương mặt hắn như được tạc từ băng đá, đôi mắt sắc lẹm chứa đựng sát khí vô biên khi nhìn dòng nước mưa xối xả ngoài cửa kính.</p>

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

<p>Lâm Phong không thèm chớp mắt. Đại Phong bước lên một bước, nhanh như chớp tóm lấy ngón tay đang chỉ trỏ của tên bảo vệ, bẻ ngược một tiếng *Rắc* giòn giã.</p>

<p>— "Áaaa!" Tên bảo vệ trưởng rú lên thảm thiết, quỳ sụp xuống đất, mặt mũi méo mó vì đau đớn.</p>

<p>— "Nói với Lâm Vĩnh Thịnh." Lâm Phong giẫm thẳng gót giày da lên khuôn mặt đang gào khóc của tên bảo vệ, nghiền mạnh xuống nền sỏi sắc nhọn. "Đứa phế vật năm đó... hôm nay trở về để lấy mạng Lâm gia."</p>"""
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

<p>Đám bảo vệ Lâm gia cầm gậy lao lên, nhưng chưa kịp áp sát đã bị đám vệ sĩ xám của Lâm Phong ra tay tàn nhẫn, bẻ tay bẻ chân ngã rạp xuống đất gào thét thảm thiết. Máu tươi bắn cả lên những chiếc váy dạ hội đắt tiền của khách mời.</p>

<p>Lâm Phong bước từng bước lên sân khấu, đứng đối diện với Lâm Vĩnh Thịnh đang run bần bật:</p>

<p>— "Mày... mày lấy đâu ra tiền thuê đám giang hồ này? Mày chỉ là một thằng ăn mày!" Lâm Vĩnh Thịnh hét lớn để che giấu sự sợ hãi.</p>

<p>Lâm Phong khẽ cười, nụ cười đầy vẻ khinh bỉ. Luật sư Trần bước lên, rút ra tập hồ sơ pháp lý đóng dấu đỏ chói:</p>

<p>— "Ông Lâm Vĩnh Thịnh, Thiên Long Group đã mua đứt 200 tỷ nợ xấu của Lâm Thị tại ba ngân hàng liên minh. Theo điều khoản thế chấp khẩn cấp, chúng tôi chính thức niêm phong toàn bộ dinh thự này và đóng băng hoạt động của tập đoàn Lâm Thị ngay lập tức!"</p>

<p>Lâm Vĩnh Thịnh cười điên cuồng:</p>

<p>— "Ha ha! Mày hù ai đó hả thằng ranh? Ngân hàng Đông Á là đồng minh của tao, làm sao họ ký chuyển nợ cho mày được—"</p>

<p>Chưa kịp nói hết câu, ba vị Giám đốc đại diện của ba ngân hàng lớn nhất thành phố bước vào sảnh tiệc, cung kính cúi đầu 90 độ trước Lâm Phong trước sự chứng kiến của cả căn phòng:</p>

<p>— "Kính chào ngài Lâm Phong Chủ tịch tối cao! Chúng tôi đã hoàn tất toàn bộ thủ tục niêm phong tài sản của Lâm gia theo lệnh của ngài!"</p>

<p>Lâm Vĩnh Thịnh nhìn cảnh tượng đó mà như ngã từ trên trời xuống đất, hai chân đứng không vững, quỳ sụp xuống sàn sân khấu.</p>

<p>Lâm Kiều Diễm hoảng loạn chạy lên định cào cấu Lâm Phong, nhưng hắn chỉ khẽ lách người. Đại Phong vung tay tát một cú trời giáng khiến cô ta bay xa hai mét, va vào bàn tiệc làm vỡ vụn hàng trăm ly pha lê. Mảnh vỡ đâm rách khuôn mặt kiêu ngạo của cô ta, máu chảy ròng ròng.</p>

<p>— "Anh Phong... cứu em..." Kiều Diễm khóc lóc thảm thiết, bò dưới đất.</p>

<p>Lâm Phong giẫm gót giày da lên bàn tay đầy mảnh vỡ của cô ta, nghiền mạnh khiến tiếng xương ngón tay gãy vang lên rắc rắc đầy ghê rợn:</p>

<p>— "Ba năm trước, tay tôi cũng đau như thế này. Đây mới chỉ là lãi suất thôi, em họ à." Hắn nhìn xuống Lâm Vĩnh Thịnh đang run rẩy. "Chú Hai, chuẩn bị tinh thần đi, tôi sẽ từ từ lột da từng đứa một."</p>"""
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
        "content": """<p>Sau khi lệnh phong tỏa được ban hành, cơn ác mộng thực sự ập xuống Thiên Long Group. Liên minh ngân hàng đóng băng toàn bộ 2.000 tỷ đồng của tập đoàn. Dự án 5.000 tỷ đồng chuẩn bị khởi công buộc phải đình chỉ khẩn cấp. Hàng ngàn công nhân tại công trường kéo đến trụ sở đập phá, la hét đòi nợ lương.</p>

<p>Toàn bộ truyền thông, báo chí lớn nhỏ đồng loạt quay xe, đăng tải hàng loạt bài viết bôi nhọ Lâm Phong: <em>"Bộ mặt thật của kẻ lừa đảo", "Thiên Long Group sụp đổ trước khi bắt đầu"</em>. Bầu không khí tăm tối bao trùm lấy văn phòng tập đoàn.</p>

<p>Đỉnh điểm của sự ức chế là khi Minh Nguyệt vừa bước ra khỏi tòa nhà liền bị đám phóng viên hung hãn và những kẻ đòi nợ vây kín. Bọn chúng xô đẩy, la hét chửi rủa, giật đứt túi xách và xô cô ngã nhào xuống bậc thềm bê tông lạnh lẽo, trầy xước cả đầu gối. Nước mắt của sự bất lực và lo lắng cho Lâm Phong rơi dài trên gương mặt cô.</p>

<p>Lâm Phong đứng trên tầng cao nhìn xuống, bàn tay siết chặt lại đến mức khớp xương trắng bệch, đôi mắt hắn rực cháy ngọn lửa giận dữ. Nhưng hắn bắt buộc phải nhẫn nhịn. Đây là cái bẫy dụ rắn ra khỏi hang mà hắn đã dày công lập nên cùng Vương Kiến Quốc năm xưa: <em>"Muốn diệt sạch thế lực chống lưng, phải cho bọn chúng cảm thấy chúng ta đã hoàn toàn sụp đổ."</em></p>

<p>Lâm Vĩnh Thịnh và Tạ Vĩnh Bình hí hửng tổ chức họp báo công bố việc thu hồi dự án của Thiên Long ngay tại sảnh chính của khách sạn Hoàng Cung, muốn dồn Lâm Phong vào cái chết xã hội trước hàng trăm phóng viên quốc gia.</p>

<p>— "Lâm Phong! Mày định quỳ lạy xin tha hay để tao tống mày vào tù?" Tạ Vĩnh Bình đứng trên bục phát biểu gầm lên đắc thắng.</p>

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

<p>Hày thô bạo lột chiếc nhẫn kim cương bốn cara trên ngón tay Triệu Mỹ Nga, giật phắt chiếc vòng cổ ngọc trai đắt tiền trên cổ cô ta trước sự chứng kiến của năm trăm khách mời quý tộc.</p>

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

<p>Ánh bình minh rực rỡ xua tan đi làn sương mù buổi sớm, chiếu sáng căn penthouse sang trọng của Lâm Phong. Hắn đứng bên lan can ban công nhìn xuống dòng sông phẳng lặng, trên người mặc áo sơ mi trắng đơn giản, phong thái vô cùng ung dung và nhẹ nhõm.</p>

<p>Minh Nguyệt bước ra ban công, đặt lên bàn hai tách cà phê ấm áp, khẽ cười nhìn ngắm bóng lưng cao lớn vững chãi của hắn.</p>

<p>— "Chủ tịch, tất cả kẻ thù đều đã phải trả giá đắt. Lâm Vĩnh Thịnh nhận án tử hình vì tội mưu sát, Hoàng gia phá sản nợ nần chồng chất, Hoàng Tuấn Kiệt đi tù 20 năm, Triệu Mỹ Nga đang phải quét rác ở vùng núi xa xôi." Minh Nguyệt khẽ báo cáo.</p>

<p>Lâm Phong cầm tách cà phê lên nhấp một ngụm, mỉm cười nhẹ nhõm:</p>

<p>— "Tốt lắm. Công lý cuối cùng đã được thực thi trọn vẹn."</p>

<p>Hắn quay sang nắm lấy bàn tay mềm mại của Minh Nguyệt, ánh mắt tràn đầy sự ấm áp chân thành:</p>

<p>— "Minh Nguyệt, ba năm qua em đã đồng hành cùng tôi vượt qua giông bão. Bây giờ bình minh đã tới, em có sẵn sàng cùng tôi đi tiếp chặng đường hạnh phúc phía trước không?"</p>

<p>Minh Nguyệt má đỏ hây hây dưới nắng sớm, khẽ tựa đầu vào ngực hắn, nụ cười rạng rỡ như đóa hoa hướng dương đón nắng:</p>

<p>— "Dạ, em luôn sẵn sàng ở bên anh, trọn đời trọn kiếp!"</p>

<p>Cả hai đứng bên nhau dưới ánh nắng bình minh rực rỡ của ngày mới, cùng hướng về tương lai tươi sáng đang rộng mở trước mắt. Đứa phế vật bị sỉ nhục năm xưa nay đã thực sự tìm lại được hạnh phúc đích thực và vương quyền tối cao của cuộc đời mình.</p>

<p style="text-align:center; margin-top: 40px;">—— <strong>HẾT</strong> ——</p>

<p style="text-align:center;"><em>"Đồ Phế Vật Năm Đó, Hôm Nay Ta Trở Về" — Phiên bản sảng văn vả mặt cực mạnh hoàn hảo.</em></p>
<p style="text-align:center;"><em>Cảm ơn quý độc giả đã luôn theo dõi và ủng hộ nhiệt tình!</em></p>"""
    }
]

# ======================================================
# EXECUTION (V5 PUSH)
# ======================================================

print("=== [V5] Cập nhật mô tả truyện ===")
res_truyen = bypass("POST", f"truyen/{TRUYEN_ID}", {"content": NEW_INTRO})
print(f"Truyen intro update status: {res_truyen.status_code}")

# 1.5. Upload cover image
print("\n=== [V5] Đang upload ảnh bìa (1200x800) ===")
COVER_IMAGE_PATH = "/Users/aaronnguyen/.gemini/antigravity/brain/5d44a410-5358-4686-9682-b008f3aa2f8f/phe_vat_cover_1200x800_1779245473411.png"
FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"

try:
    with open(COVER_IMAGE_PATH, "rb") as f:
        img_data = f.read()
    img_b64 = base64.b64encode(img_data).decode("utf-8")

    php_upload = f"""<?php
require_once('wp-load.php');
require_once(ABSPATH . 'wp-admin/includes/image.php');
require_once(ABSPATH . 'wp-admin/includes/file.php');
require_once(ABSPATH . 'wp-admin/includes/media.php');

$post_id = {TRUYEN_ID};
$img_data = base64_decode($_POST['img_b64']);
$upload_dir = wp_upload_dir();
$filename = 'cover-phe-vat-1200x800-' . rand(100,999) . '.png';
$filepath = $upload_dir['path'] . '/' . $filename;
file_put_contents($filepath, $img_data);
$filetype = wp_check_filetype($filename, null);
$attachment = array(
    'post_mime_type' => $filetype['type'],
    'post_title' => $filename,
    'post_content' => '',
    'post_status' => 'inherit'
);
$attach_id = wp_insert_attachment($attachment, $filepath, $post_id);
$attach_data = wp_generate_attachment_metadata($attach_id, $filepath);
wp_update_attachment_metadata($attach_id, $attach_data);
set_post_thumbnail($post_id, $attach_id);
echo 'OK:' . $attach_id;
?>"""

    with open("upload_cover_temp.php", "w") as f:
        f.write(php_upload)

    ftp = ftplib.FTP(FTP_HOST)
    ftp.login(FTP_USER, FTP_PASS)
    with open("upload_cover_temp.php", "rb") as f:
        ftp.storbinary("STOR upload_cover_temp.php", f)
    print("FTP upload PHP OK")
    
    up_res = requests.post("https://doctieuthuyet.com/upload_cover_temp.php", data={"img_b64": img_b64}, timeout=120)
    print(f"Cover upload result: {up_res.status_code} {up_res.text}")
    
    ftp.delete("upload_cover_temp.php")
    ftp.quit()
    os.remove("upload_cover_temp.php")
except Exception as e:
    print(f"Cover upload error: {e}")

print("\n=== [V5] Lấy danh sách chương ===")
res_chaps = bypass("GET", f"chuong?meta_key=_truyen_id&meta_value={TRUYEN_ID}&per_page=20", {})

if res_chaps.status_code == 200:
    existing_chapters = res_chaps.json()
    slug_to_id = {ch['slug']: ch['id'] for ch in existing_chapters}
    
    print("\n=== [V5] Thực thi vả mặt dồn dập, đè nội dung mới ===")
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

print("\n=== HOÀN TẤT VẢ MẶT CỰC ĐÃ V5 ===")
print("Link bộ truyện sảng văn vả mặt: https://doctieuthuyet.com/truyen/do-phe-vat-nam-do-hom-nay-ta-tro-ve/")
