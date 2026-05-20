import requests
import ftplib
import base64
import time
import os

BYPASS_URL = "https://doctieuthuyet.com/api_truyen_bypass.php"
TOKEN = "ZEN_TRUYEN_2026_BYPASS"
FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"

COVER_IMAGE_PATH = "/Users/aaronnguyen/.gemini/antigravity/brain/5d44a410-5358-4686-9682-b008f3aa2f8f/truyen_phe_vat_cover_1779244267478.png"

TRUYEN_TITLE = "Đồ Phế Vật Năm Đó, Hôm Nay Ta Trở Về"
TRUYEN_INTRO = """<p>Năm đó, Lâm Phong là một chàng trai bình thường nhất gia tộc Lâm – không tài năng, không thế lực, bị coi là <strong>phế vật</strong> ngay từ khi sinh ra. Hôn thê bỏ đi theo kẻ khác. Người thân quay lưng. Gia tộc hắt hủi. Lâm Phong bị ép ký giấy từ bỏ mọi quyền lợi rồi đẩy ra đường như một con chó ghẻ.</p>

<p>Không ai biết rằng, trong một đêm giông bão, Lâm Phong đã bắt được <em>bí kíp võ công tuyệt đỉnh</em> của một ẩn sĩ già trên núi. Ba năm tu luyện nơi đất khách, hắn đã trở thành một nhân vật mà cả thành phố phải cúi đầu.</p>

<p>Hôm nay, Lâm Phong trở về. Không phải để van xin hay khóc lóc. Hắn trở về để <strong>vả mặt từng kẻ</strong> đã từng chà đạp lên tự trọng của mình, và để mọi người hiểu rằng: <em>Đồ phế vật năm đó – hôm nay đã là Vương.</em></p>"""

chapters = [
    {
        "title": "Chương 1: Kẻ Bị Đuổi Cổ Trở Về",
        "content": """<p>Chiếc Mercedes đen bóng loáng lướt nhẹ qua cổng chào của thành phố H. Ngồi trong xe, Lâm Phong nhìn qua ô cửa kính tối, ánh mắt lạnh như băng dưới ánh đèn đường vàng nhạt. Ba năm rồi. Ba năm kể từ cái đêm hắn bị đẩy ra khỏi nhà tổ của gia tộc Lâm trong cơn mưa tầm tã, tay trắng và không một xu dính túi.</p>

<p>— "Thiếu gia, chúng ta về khách sạn Hoàng Cung hay về nhà cũ?" Tên tài xế – thực ra là cận vệ cấp bậc cao nhất của Lâm Phong – kính cẩn hỏi.</p>

<p>— "Về nhà cũ." Lâm Phong khẽ nhếch môi. "Đã lâu rồi ta chưa thăm... gia đình."</p>

<p>Người tài xế khẽ run. Hắn biết giọng điệu ấy của Thiếu gia. Nhẹ nhàng, bình tĩnh, nhưng bên dưới là cả một ngọn lửa đang chực bùng cháy.</p>

<p>Ba năm trước, đêm hôm đó, Lâm Phong nhớ như in. Chú thứ hai của hắn – Lâm Vĩnh Thịnh – đứng thẳng người ở đại sảnh, giọng lạnh băng: "Mày không có một giọt máu tài năng nào. Đi mà ăn mày cho rồi, đừng làm nhục gia tộc nữa." Cô em họ Lâm Kiều Diễm khe khẽ cười sau lưng, cắn khăn tay giả vờ thương tiếc. Còn Triệu Mỹ Nga – người mà hắn đã yêu suốt bốn năm đại học – thì đứng tựa vào vai người đàn ông khác, không thèm nhìn hắn lấy một cái.</p>

<p>Lâm Phong đã không khóc. Hắn cúi đầu ký vào tờ giấy từ bỏ toàn bộ cổ phần và quyền thừa kế, rồi bước ra trong cơn mưa mà không ngoái đầu lại.</p>

<p>Nhưng số phận đôi khi hay trêu ngươi con người. Đêm đó, Lâm Phong lang thang lên đến đỉnh núi Bạch Vân phía Tây thành phố, định nằm đó chờ sáng. Tình cờ, hắn gặp một ông lão đang hấp hối bên gốc cây tùng già. Không một chút do dự, Lâm Phong cởi áo khoác ra đắp cho ông lão, ở lại sưởi ấm cho ông suốt đêm đến sáng.</p>

<p>Ông lão nhìn hắn một hồi lâu, rồi đưa ra một cái hộp gỗ đen nhánh.</p>

<p>— "Ta đã quan sát ngươi từ lâu, Lâm Phong. Ngươi không phải phế vật. Ngươi chỉ chưa tìm được con đường của mình." Giọng ông khàn khàn nhưng có một thứ uy lực không thể cưỡng lại. "Trong hộp này là cả đời ta. Hãy mang nó đi và không bao giờ ngẩng đầu trước kẻ đáng bị ngẩng đầu."</p>

<p>Sáng hôm sau, ông lão biến mất như chưa từng tồn tại. Lâm Phong mở hộp ra – đó là một cuốn sách mỏng, bìa da thật, ghi ba chữ: <em>Thiên Long Bí Điển</em>.</p>

<p>Ba năm. Ba năm để một phế vật lột xác thành Rồng.</p>

<p>Chiếc xe dừng lại trước cổng dinh thự gia tộc Lâm. Người bảo vệ đứng chặn đường, nhìn chiếc xe xa lạ với ánh mắt nghi ngờ.</p>

<p>— "Ai? Có hẹn không?"</p>

<p>Lâm Phong bước xuống xe, chỉnh lại cổ áo vest đen, nhìn thẳng vào mắt người bảo vệ.</p>

<p>— "Nói với Lâm Vĩnh Thịnh rằng… đứa phế vật năm đó đã về."</p>

<p>Người bảo vệ ngơ ngác, nhưng nhìn thấy ánh mắt của người đàn ông trước mặt – một ánh mắt sắc lạnh như kiếm tuốt trần – hắn không hiểu sao lại run lên và bước vào trong gọi điện báo.</p>

<p>Lâm Phong khẽ mỉm cười. Trò chơi bắt đầu rồi.</p>"""
    },
    {
        "title": "Chương 2: Bữa Tiệc Nhà Lâm Và Cái Tát Đầu Tiên",
        "content": """<p>Bên trong dinh thự Lâm gia, bữa tiệc kỷ niệm 30 năm thành lập tập đoàn đang ở cao điểm. Đèn chùm lấp lánh, rượu vang đỏ sóng sánh trong ly pha lê, những gương mặt nhà tài phiệt và quan chức quyền lực cười cợt vui vẻ. Lâm Vĩnh Thịnh – đại gia trưởng – đứng giữa đám đông, bộ vest bạc triệu, nụ cười đắc ý của kẻ đã đoạt được tất cả những gì mình muốn.</p>

<p>— "Thiếu gia... có người xưng là Lâm Phong xin vào." Người trợ lý khe khẽ ghé tai ông ta.</p>

<p>Lâm Vĩnh Thịnh cứng người một giây. Sau đó bật cười lớn.</p>

<p>— "Lâm Phong? Cái thằng phế vật đó à? Thú vị đấy. Cho vào đi, hôm nay ta hứng khởi, muốn xem nó đến xin xỏ gì."</p>

<p>Tiếng bước chân vang lên ở cửa chính. Cả phòng quay đầu nhìn. Một người đàn ông bước vào – cao ráo, áo vest đen cắt may hoàn hảo, tóc vuốt gọn, khuôn mặt điêu khắc với đôi mắt sắc bén như ưng. Đi sau hắn là hai người đàn ông to lớn mặc vest xám, vẻ mặt như tường thành.</p>

<p>Lâm Kiều Diễm đứng cạnh mẹ, mắt mở to. Cô không nhận ra ngay, phải nhìn mấy giây mới thốt lên được: "Lâm... Lâm Phong?"</p>

<p>Một ai đó trong đám đông khe khẽ: "Ba năm rồi, thằng bé thay đổi dữ vậy?"</p>

<p>Lâm Phong bước thẳng vào giữa phòng, nhìn quanh một lượt với ánh mắt bình thản như đang xem một bộ phim nhạt nhẽo. Hắn dừng lại trước mặt Lâm Vĩnh Thịnh.</p>

<p>— "Chú Hai. Lâu rồi không gặp." Giọng hắn đều đều, không một chút cảm xúc.</p>

<p>Lâm Vĩnh Thịnh khoanh tay, nhìn hắn từ đầu đến chân với ánh mắt dò xét.</p>

<p>— "Ồ, cháu về đấy à. Trông khá đấy. Đi đâu ba năm mà... lột xác vậy? Hay là đi làm thuê cho người ta, tiết kiệm mua bộ vest đẹp về dự tiệc?"</p>

<p>Tiếng cười khúc khích lan ra. Lâm Kiều Diễm cắn môi cố nhịn cười.</p>

<p>Lâm Phong không hề thay đổi biểu cảm. Hắn thản nhiên rút điện thoại ra, bấm vài nút, rồi đưa màn hình ra trước mặt Lâm Vĩnh Thịnh. Đó là một bản hợp đồng và bên dưới là logo của Tập đoàn Thiên Long – doanh nghiệp xếp hạng thứ ba toàn quốc với vốn hóa 50.000 tỷ đồng.</p>

<p>— "Con đã mua lại toàn bộ khoản nợ 200 tỷ mà tập đoàn mình đang nợ ngân hàng Đông Á." Lâm Phong khẽ nói. "Nghĩa là từ hôm nay, chủ nợ của gia tộc Lâm là... con đây."</p>

<p>Không khí đông cứng. Lâm Vĩnh Thịnh mặt đỏ bừng rồi tái nhợt xen kẽ nhau liên tục. Hắn giật lấy điện thoại, nhìn chằm chằm vào màn hình. Đó là sự thật. Con dấu, chữ ký, số tài khoản – tất cả đều là thật.</p>

<p>— "Mày... mày dám...!" Giọng ông ta run rẩy.</p>

<p>— "Luật sư của con sẽ đến văn phòng vào sáng mai." Lâm Phong lấy lại điện thoại, bỏ vào túi vest thật khoan thai. "Có nhiều thứ cần bàn lại về hợp đồng chia sẻ tài sản năm đó. Cái tờ giấy con ký... hóa ra có một số điều khoản vi phạm pháp lý rất thú vị."</p>

<p>Rồi hắn quay đầu, bắt gặp ánh mắt sững sờ của Lâm Kiều Diễm – cô em họ năm đó cười sau lưng hắn.</p>

<p>— "Chào em Diễm. Em đang mở công ty thời trang phải không?" Hắn mỉm cười nhẹ. "Nhà cung cấp vải chính của em – tập đoàn Hoa Thịnh – vừa ký hợp tác độc quyền với Thiên Long rồi. Từ giờ giá vải sẽ... điều chỉnh một chút."</p>

<p>Lâm Kiều Diễm mặt xanh lét. Ly rượu trên tay rơi xuống sàn vỡ tan.</p>

<p>Lâm Phong không nhìn thêm nữa. Hắn quay người đi ra, dừng lại ở cửa nói vọng lại:</p>

<p>— "À, tiệc vui đấy. Cảm ơn các vị đã mời."</p>

<p>Không ai mời hắn cả. Nhưng câu nói đó làm cả căn phòng im lặng nặng nề như đá đè lên ngực.</p>"""
    },
    {
        "title": "Chương 3: Người Tình Cũ Và Tên Tiểu Nhân",
        "content": """<p>Triệu Mỹ Nga đang ngồi trong nhà hàng sang trọng nhất thành phố H, đối diện với Hoàng Tuấn Kiệt – người mà cô đã rời bỏ Lâm Phong để đến bên. Ba năm qua, cô và Tuấn Kiệt đã đính hôn, và đám cưới dự kiến sẽ diễn ra sau hai tháng nữa.</p>

<p>— "Nghe nói thằng Lâm Phong về rồi." Hoàng Tuấn Kiệt nhíu mày, giọng không giấu được lo lắng. "Mà nghe đâu hắn giờ... không phải dạng vừa nữa."</p>

<p>Triệu Mỹ Nga phất tay.</p>

<p>— "Anh lo gì? Hắn là phế vật thì vẫn là phế vật. Dù có mặc bộ vest đắt tiền thì cũng chỉ là con nhà nghèo giả nhà giàu." Cô nhấp một ngụm nước chanh, tự tin tuyệt đối. "Mà dù sao đi nữa, chúng ta sắp cưới rồi. Hắn liên quan gì?"</p>

<p>Đúng lúc đó, cửa nhà hàng mở ra. Lâm Phong bước vào, đi kèm một người phụ nữ mặc vest trắng – là trợ lý riêng của hắn. Hắn đặt bàn ở đây không phải tình cờ.</p>

<p>Triệu Mỹ Nga cứng người khi ánh mắt cô chạm vào hắn. Không phải vì ngạc nhiên. Mà vì... hắn khác quá. Cái vẻ rụt rè, nhút nhát của Lâm Phong ngày xưa biến mất hoàn toàn. Thay vào đó là một người đàn ông đứng thẳng, ánh mắt tĩnh lặng và uy nghiêm đến mức bồi bàn đứng cạnh đó còn phải bước lui một bước.</p>

<p>Hoàng Tuấn Kiệt đứng dậy, giọng gắt:</p>

<p>— "Lâm Phong! Mày dám đến đây làm gì?"</p>

<p>Lâm Phong nhìn qua hắn như nhìn qua không khí. Rồi hắn nhìn xuống cái ghế mà Tuấn Kiệt đang đứng.</p>

<p>— "Ồ, đây là bàn số 7 tôi đặt từ tuần trước. Anh đang ngồi nhầm chỗ." Hắn nói với quản lý nhà hàng đứng cạnh đó.</p>

<p>Người quản lý cúi đầu liền:</p>

<p>— "Đúng vậy, bàn số 7 là của ngài Lâm. Xin lỗi hai vị, chúng tôi sẽ sắp xếp bàn khác cho..."</p>

<p>— "Anh dám!" Tuấn Kiệt đỏ mặt tím mang.</p>

<p>— "Này nhà hàng, tôi nhớ anh Hoàng Tuấn Kiệt này từng bị cấm cửa vì vụ không thanh toán hóa đơn 80 triệu hồi năm ngoái phải không?" Lâm Phong quay sang quản lý hỏi nhẹ nhàng.</p>

<p>Người quản lý tái mặt nhưng gật đầu khe khẽ. Tuấn Kiệt mặt đỏ như gấc, tay nắm chặt.</p>

<p>— "Mày...!"</p>

<p>— "À thôi, tôi không muốn làm phiền." Lâm Phong vẫy tay. "Cứ ngồi đây đi. Tôi ngồi bàn khác." Hắn quay sang quản lý: "Cho tôi một bàn private lounge tầng trên."</p>

<p>— "Dạ vâng, ngài Lâm. Bàn VIP đã sẵn sàng ạ."</p>

<p>Lâm Phong đi qua bàn của Triệu Mỹ Nga mà không nhìn cô ta. Chỉ đến khi qua hẳn rồi, hắn mới quay lại nói thêm một câu nhỏ đủ để chỉ hai người đó nghe:</p>

<p>— "À, Mỹ Nga, căn hộ em đang ở ở Sunrise Tower... tòa nhà đó vừa được Thiên Long mua lại rồi. Hợp đồng thuê của em... cần xem lại điều khoản đó."</p>

<p>Triệu Mỹ Nga há hốc miệng, không nói được lời nào. Hoàng Tuấn Kiệt ngồi xuống, mặt trắng bệch như tờ giấy. Chỉ một câu thôi, nhưng hắn biết – đây mới chỉ là mở đầu.</p>

<p>Và đó là điều đáng sợ nhất.</p>"""
    },
    {
        "title": "Chương 4: Màn Họp Báo Chấn Động",
        "content": """<p>Sáng hôm sau, tất cả các mặt báo thành phố H đều đăng một tin tức làm cả giới doanh nhân sôi sục: <em>Tập đoàn Thiên Long – "Ông vua" ngành bất động sản và tài chính – chính thức công bố văn phòng đại diện tại thành phố H. Chủ tịch HĐQT: Lâm Phong, 27 tuổi.</em></p>

<p>Họp báo diễn ra tại khách sạn Hoàng Cung – khách sạn 5 sao lớn nhất thành phố. Phòng họp báo kín người. Phóng viên, nhà đầu tư, đại diện các tập đoàn đổ về như nước. Không ai tin rằng cái tên Lâm Phong – người mà ba năm trước bị cả thành phố coi là phế vật – nay lại là chủ tịch của một đế chế tầm cỡ quốc gia.</p>

<p>Lâm Vĩnh Thịnh ngồi ở hàng ghế khách mời, mặt tái nhợt. Bên cạnh ông ta là Lâm Quốc Bình – anh trai ruột của Lâm Phong, người đã không nói một lời trong đêm hắn bị đuổi đi. Im lặng đồng nghĩa với đồng ý.</p>

<p>Lâm Phong bước lên sân khấu trong tiếng vỗ tay râm ran. Hắn không vội vàng. Hắn đứng sau bục phát biểu, nhìn xuống đám đông, và chờ. Một giây. Hai giây. Năm giây. Căn phòng im lặng tuyệt đối.</p>

<p>— "Xin chào mọi người." Giọng hắn ấm áp nhưng có trọng lượng. "Tôi là Lâm Phong. Nhiều người trong căn phòng này đã biết tôi từ ba năm trước." Hắn mỉm cười. "Khi đó tôi không có gì cả. Hôm nay, tôi có đủ."</p>

<p>Một phóng viên giơ tay:</p>

<p>— "Ngài Lâm, xin hỏi trong ba năm qua ngài đã làm gì để xây dựng Thiên Long từ con số không?"</p>

<p>Lâm Phong nhìn thẳng vào máy quay:</p>

<p>— "Tôi học. Tôi làm việc. Và tôi không bao giờ để người khác định nghĩa giá trị của mình."</p>

<p>Tiếng vỗ tay nổi lên. Lâm Vĩnh Thịnh nghiến răng.</p>

<p>— "Ngài có kế hoạch gì cho thị trường thành phố H?"</p>

<p>— "Thiên Long sẽ đầu tư 5.000 tỷ vào thành phố H trong vòng 2 năm tới." Lâm Phong ngừng một chút. "Bao gồm việc mua lại một số tài sản... đang ở thế kẹt về tài chính."</p>

<p>Câu nói đó làm Lâm Vĩnh Thịnh đứng bật dậy, rồi lại ngồi xuống vì nhận ra mình đang ở chỗ đông người. Vì ai cũng biết: Tập đoàn Lâm đang nợ Thiên Long một khoản khổng lồ.</p>

<p>Sau buổi họp báo, khi mọi người ra về, Lâm Quốc Bình – anh trai – bước đến gần Lâm Phong. Người đàn ông 35 tuổi này đứng trước em trai, mắt không dám nhìn thẳng.</p>

<p>— "Phong... anh..."</p>

<p>— "Anh không cần nói gì." Lâm Phong nhìn anh trai, giọng bình thản. "Năm đó anh không nói một lời. Hôm nay anh cũng không cần nói gì."</p>

<p>Lâm Quốc Bình cúi đầu. Đó là cái cúi đầu đau nhất trong đời ông ta.</p>

<p>Lâm Phong bước đi. Cánh cửa phòng họp khép lại sau lưng hắn, bỏ lại người anh trai đứng một mình giữa phòng trống.</p>"""
    },
    {
        "title": "Chương 5: Bẫy Của Kẻ Thù Và Đòn Phản Công",
        "content": """<p>Lâm Vĩnh Thịnh không phải kẻ ngốc. Sau hai cú đau liên tiếp, ông ta bắt đầu phản công. Ông ta liên hệ với Hội đồng thương nhân địa phương, dùng quan hệ để vận động một cuộc kiểm toán thuế nhắm vào Thiên Long. Đồng thời, ông ta thuê người tung tin đồn trên mạng rằng Lâm Phong có nguồn tiền không minh bạch.</p>

<p>Tin đồn lan nhanh. Một số nhà đầu tư nhỏ lẻ bắt đầu hoang mang.</p>

<p>Sáng hôm đó, trợ lý của Lâm Phong – Minh Nguyệt – bước vào văn phòng với khuôn mặt lo lắng:</p>

<p>— "Thiếu gia, trên mạng đang có làn sóng tấn công chúng ta. Và đoàn kiểm toán thuế thông báo sẽ đến vào ngày mai."</p>

<p>Lâm Phong đang ngồi uống trà, không nhìn lên.</p>

<p>— "Tốt."</p>

<p>— "Tốt?" Minh Nguyệt trợn mắt.</p>

<p>— "Ta đã chờ điều này." Lâm Phong đặt tách trà xuống. "Gọi luật sư trưởng và bộ phận tài chính lên đây. Và... liên hệ với phóng viên Thanh Minh ở đài truyền hình trung ương. Nói với cô ấy rằng ta có độc quyền phỏng vấn và một câu chuyện cô ấy không muốn bỏ lỡ."</p>

<p>Buổi chiều hôm đó, đoàn kiểm toán đến. Họ đi qua từng tầng văn phòng Thiên Long trong ba tiếng đồng hồ, kiểm tra mọi chứng từ, hóa đơn, báo cáo tài chính. Kết quả: Không một vi phạm nhỏ nhất. Sổ sách của Thiên Long sạch đến mức người trưởng đoàn kiểm toán phải thốt lên: "Đây là doanh nghiệp minh bạch nhất tôi từng kiểm tra."</p>

<p>Tối hôm đó, phóng sự đặc biệt lên sóng toàn quốc. Phóng viên Thanh Minh ngồi đối diện Lâm Phong trong một studio sang trọng.</p>

<p>— "Ngài có biết ai đứng sau những tin đồn về nguồn tiền của Thiên Long không?"</p>

<p>Lâm Phong nhìn thẳng vào máy quay:</p>

<p>— "Tôi biết." Hắn nhẹ nhàng đặt một tập hồ sơ lên bàn. "Và tôi đã nhờ cơ quan chức năng tiếp nhận tố cáo về hành vi tung tin sai sự thật và cạnh tranh không lành mạnh này. Hồ sơ bằng chứng đầy đủ."</p>

<p>Ống kính máy quay zoom vào tập hồ sơ. Trên trang đầu tiên, người xem cả nước nhìn thấy tên: Lâm Vĩnh Thịnh – Chủ tịch Tập đoàn Lâm.</p>

<p>Đêm hôm đó, điện thoại của Lâm Vĩnh Thịnh không ngừng reo. Đối tác gọi để hỏi thăm. Ngân hàng gọi để nhắc nợ. Và luật sư của Thiên Long gửi đến một phong thư lịch sự nhưng cứng rắn: Thông báo khởi kiện dân sự về tội vu khống và cạnh tranh không lành mạnh. Số tiền yêu cầu bồi thường: 50 tỷ đồng.</p>

<p>Lâm Vĩnh Thịnh ngồi trong văn phòng tối mờ, nhìn chằm chằm vào bức ảnh trên tường – bức ảnh gia tộc Lâm chụp hai mươi năm trước, có cả một đứa bé nhỏ xíu đứng ở góc, chính là Lâm Phong.</p>

<p>Ông ta hiểu rồi. Mình đã sai. Và cái giá phải trả thì... còn lâu mới hết.</p>"""
    },
    {
        "title": "Chương 6: Đám Cưới Bị Phá",
        "content": """<p>Đám cưới của Hoàng Tuấn Kiệt và Triệu Mỹ Nga được tổ chức tại khách sạn Hoàng Cung – trớ trêu thay, chính cái khách sạn mà Lâm Phong đang là cổ đông chiến lược. Hơn 500 khách mời, hoa tươi phủ kín sảnh, đèn hoa lung linh. Triệu Mỹ Nga trong bộ váy cưới trắng tinh, tự tin bước vào ngày hạnh phúc nhất đời mình.</p>

<p>Nhưng hôm đó, ngay trước giờ G một tiếng, đại diện ngân hàng xuất hiện tại cửa phòng tiệc với một xấp giấy tờ. Hóa ra Hoàng Tuấn Kiệt đã cầm cố căn penthouse dùng làm quà cưới cho Mỹ Nga để vay tiền đầu tư, và khoản vay đó đã đến hạn từ tháng trước. Ngân hàng yêu cầu tất toán ngay lập tức hoặc tiến hành tịch thu tài sản.</p>

<p>Tin đồn loang ra cả phòng tiệc chỉ trong vòng mười lăm phút.</p>

<p>Hoàng Tuấn Kiệt gọi điện khắp nơi cầu cứu. Không ai bắt máy. Vì giờ cả thành phố đã biết hắn là người đã tham gia vào âm mưu đánh Thiên Long – và không ai dại gì dây vào lúc này.</p>

<p>Triệu Mỹ Nga đứng giữa phòng hoa, váy trắng muốt, mắt đỏ hoe. Cô gọi cho Lâm Phong. Không hiểu sao cô lại gọi cho hắn. Có lẽ vì trong khoảnh khắc đó, cô nhớ lại ngày xưa – khi Lâm Phong đứng trước cô với đôi mắt ấm áp, sẵn sàng làm tất cả vì cô.</p>

<p>Lâm Phong nghe máy. Giọng bình thản:</p>

<p>— "Mỹ Nga."</p>

<p>— "Phong... anh giúp em với. Khoản nợ đó... chỉ cần anh một tiếng..."</p>

<p>Im lặng kéo dài ba giây.</p>

<p>— "Em nhớ không, ngày xưa em nói gì với anh?" Giọng Lâm Phong vẫn bình thản, không một chút oán hận – điều đó thậm chí còn đáng sợ hơn. "Em nói: 'Anh không có gì cả. Em không thể đặt cược cả cuộc đời vào một người như anh.'"</p>

<p>Triệu Mỹ Nga cắn môi, nước mắt chảy dài.</p>

<p>— "Em... em sai rồi..."</p>

<p>— "Anh biết." Lâm Phong nhẹ nhàng. "Nhưng đây không phải chuyện của anh nữa. Chúc mừng đám cưới."</p>

<p>Máy cúp.</p>

<p>Triệu Mỹ Nga đứng giữa phòng tiệc, tay cầm điện thoại, váy cưới trắng tinh. Hoa tươi thơm ngát. Đèn hoa lung linh. Và không có chú rể.</p>

<p>Hoàng Tuấn Kiệt đã lặng lẽ biến mất từ lúc nào.</p>"""
    },
    {
        "title": "Chương 7: Màn Kết Toán Với Gia Tộc Lâm",
        "content": """<p>Cuộc họp diễn ra tại chính đại sảnh của dinh thự Lâm gia – nơi ba năm trước Lâm Phong đã ký giấy từ bỏ tất cả. Lần này, ghế chủ tọa được dành cho Lâm Phong, còn Lâm Vĩnh Thịnh và những thành viên gia tộc khác ngồi hai bên, mặt mũi ủ rũ như đám tang.</p>

<p>Các luật sư đặt hồ sơ xuống bàn. Dày đến mức tiếng đặt nghe rõ ràng trong không khí im lặng tuyệt đối.</p>

<p>— "Như đã thông báo trước." Luật sư trưởng của Thiên Long mở đầu. "Thiên Long Group hiện nắm giữ 60% khoản nợ của Tập đoàn Lâm. Theo điều khoản hợp đồng, chúng tôi có quyền yêu cầu hoàn trả ngay lập tức hoặc chuyển đổi thành cổ phần tương đương."</p>

<p>Lâm Vĩnh Thịnh nhấc tay:</p>

<p>— "Chúng tôi cần thêm thời gian. Sáu tháng..."</p>

<p>— "Không." Lâm Phong lên tiếng lần đầu tiên. Một chữ duy nhất, ngắn gọn, dứt khoát như tiếng búa đóng đinh.</p>

<p>Ông ta nhìn Lâm Phong, mắt đỏ hoe:</p>

<p>— "Phong... chú biết mình đã sai. Nhưng dù sao cũng là máu mủ. Con có thể..."</p>

<p>— "Chú nói đúng. Chúng ta là máu mủ." Lâm Phong nhìn thẳng vào mắt ông ta. "Vì vậy con sẽ không lấy đi tất cả." Hắn đẩy một tập hồ sơ qua bàn. "Thiên Long sẽ tiếp quản 51% cổ phần Tập đoàn Lâm – đủ để kiểm soát. 49% còn lại, gia tộc giữ. Điều kiện: Lâm Vĩnh Thịnh rút khỏi mọi vị trí lãnh đạo."</p>

<p>Lâm Vĩnh Thịnh tái mặt. Đó là điều kiện kết thúc sự nghiệp của ông ta.</p>

<p>— "Tại sao không lấy hết?" Lâm Quốc Bình – anh trai Lâm Phong – bất ngờ lên tiếng. "Con hoàn toàn có thể lấy hết mà."</p>

<p>Lâm Phong quay sang nhìn anh trai. Lần đầu tiên trong buổi họp, hắn để lộ một chút cảm xúc – một nỗi buồn rất nhẹ thoáng qua đôi mắt.</p>

<p>— "Vì đây là nhà của chúng ta, anh ạ." Hắn nói khẽ. "Dù họ đã làm gì, con không muốn phá nó hoàn toàn. Con chỉ muốn những kẻ sai phải nhận ra mình đã sai."</p>

<p>Lâm Quốc Bình cúi đầu. Lần này không phải vì xấu hổ. Lần này là vì ông ta thực sự thấy tiếc về sự hèn nhát của mình năm đó.</p>

<p>Lâm Vĩnh Thịnh nhìn tờ giấy trước mặt một hồi lâu. Rồi ông ta cầm bút ký. Bàn tay run rẩy, nhưng ký.</p>

<p>Lâm Phong thu hồ sơ lại, đứng dậy. Hắn nhìn quanh căn phòng một lượt – căn phòng mà hắn đã ký giấy bán hết tương lai của mình trong đêm mưa ba năm trước.</p>

<p>— "Cảm ơn tất cả." Hắn nói, rồi đi ra ngoài.</p>"""
    },
    {
        "title": "Chương 8: Bình Minh Của Kẻ Trở Về",
        "content": """<p>Một tháng sau ngày ký kết, thành phố H đã khác đi rất nhiều. Biển hiệu Thiên Long xuất hiện ở nhiều tòa nhà lớn. Dự án khu đô thị mới khởi công, tạo ra hàng nghìn việc làm. Người ta nói về Lâm Phong như một huyền thoại – một cậu bé bị gia đình từ chối, ba năm lột xác thành ông vua của cả một đế chế.</p>

<p>Sáng hôm đó, Lâm Phong đứng trên ban công tầng 32 của tòa văn phòng Thiên Long, nhìn ra thành phố đang thức dậy trong ánh bình minh. Gió thổi nhẹ, mang theo mùi cà phê từ con phố phía dưới.</p>

<p>Minh Nguyệt bước ra, đưa cho hắn một tách cà phê đen:</p>

<p>— "Thiếu gia, hôm nay lịch làm việc dày lắm đó."</p>

<p>— "Biết rồi." Hắn cầm tách cà phê, nhấp một ngụm.</p>

<p>— "Còn một việc nữa." Minh Nguyệt ngập ngừng. "Cô Triệu Mỹ Nga... cô ấy gửi thư xin gặp lần thứ ba rồi."</p>

<p>Lâm Phong không nói gì. Nhìn ra phía chân trời đang ửng hồng.</p>

<p>— "Thiếu gia muốn gặp không?"</p>

<p>— "Không." Câu trả lời dứt khoát, không do dự. Nhưng không có oán hận trong đó. Chỉ là... đóng lại. "Quá khứ không cần phải mở lại."</p>

<p>Minh Nguyệt gật đầu, chuẩn bị quay vào. Lâm Phong gọi lại:</p>

<p>— "Nguyệt. Tìm hiểu xem cô ấy hiện tại ra sao. Nếu cô ấy đang thực sự khó khăn, thì... âm thầm sắp xếp một cơ hội việc làm tử tế cho cô ấy. Không cần nhắc tên ta."</p>

<p>Minh Nguyệt nhìn hắn, ánh mắt phức tạp:</p>

<p>— "Thiếu gia... sao vẫn còn nghĩ đến cô ấy?"</p>

<p>Lâm Phong khẽ cười, lần đầu tiên nụ cười không phải lạnh mà thực sự ấm áp:</p>

<p>— "Không phải vì tình cũ. Là vì ta không muốn trở thành người giống những kẻ đã chà đạp ta." Hắn quay đầu nhìn vào ánh mình phản chiếu trong ô cửa kính. "Vả mặt không có nghĩa là bóp chết người ta. Chỉ là để họ hiểu, để họ tỉnh. Còn sau đó – đó là lựa chọn của họ."</p>

<p>Ánh nắng bình minh cuối cùng cũng vươn qua đỉnh các tòa nhà, chiếu thẳng vào mặt Lâm Phong. Hắn nheo mắt, rồi thở ra một hơi dài.</p>

<p>Ba năm trước, một người đàn ông bước ra trong mưa với hai bàn tay trắng và cả thành phố quay lưng lại.</p>

<p>Hôm nay, người đàn ông đó đứng ở đỉnh cao nhất, nhìn xuống thành phố của mình, và lần đầu tiên thực sự mỉm cười.</p>

<p>Không phải nụ cười của kẻ thắng.</p>

<p>Mà là nụ cười của người... đã trở về nhà.</p>

<p style="text-align:center;">—— <strong>HẾT</strong> ——</p>

<p style="text-align:center;"><em>Cảm ơn các bạn đã đọc "Đồ Phế Vật Năm Đó, Hôm Nay Ta Trở Về". Nếu thích, đừng quên để lại yêu thích và chia sẻ nhé!</em></p>"""
    }
]

def bypass(method, endpoint, payload):
    res = requests.post(BYPASS_URL, json={
        "secret_token": TOKEN,
        "method": method,
        "endpoint": endpoint,
        "payload": payload
    }, timeout=60)
    return res

# 1. Create story
print("=== Đang tạo truyện ===")
res = bypass("POST", "truyen", {
    "title": TRUYEN_TITLE,
    "content": TRUYEN_INTRO,
    "status": "publish"
})
print(f"Status: {res.status_code}")
if res.status_code != 201:
    print("LỖI:", res.text)
    exit(1)

truyen_id = res.json()["id"]
truyen_link = res.json()["link"]
print(f"Tạo xong! ID: {truyen_id}, Link: {truyen_link}")

# 2. Upload cover image
print("\n=== Đang upload ảnh bìa ===")
with open(COVER_IMAGE_PATH, "rb") as f:
    img_data = f.read()
img_b64 = base64.b64encode(img_data).decode("utf-8")

# Use the temply upload-cover endpoint via a temp PHP
php_upload = f"""<?php
require_once('wp-load.php');
require_once(ABSPATH . 'wp-admin/includes/image.php');
require_once(ABSPATH . 'wp-admin/includes/file.php');
require_once(ABSPATH . 'wp-admin/includes/media.php');

$post_id = {truyen_id};
$img_data = base64_decode($_POST['img_b64']);
$upload_dir = wp_upload_dir();
$filename = 'cover-phe-vat-' . rand(100,999) . '.png';
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

try:
    ftp = ftplib.FTP(FTP_HOST)
    ftp.login(FTP_USER, FTP_PASS)
    with open("upload_cover_temp.php", "rb") as f:
        ftp.storbinary("STOR upload_cover_temp.php", f)
    print("FTP upload PHP OK")
    
    up_res = requests.post("https://doctieuthuyet.com/upload_cover_temp.php", data={"img_b64": img_b64}, timeout=120)
    print(f"Cover upload result: {up_res.status_code} {up_res.text}")
    
    ftp.delete("upload_cover_temp.php")
    ftp.quit()
except Exception as e:
    print(f"Cover upload error: {e}")

os.remove("upload_cover_temp.php")

# 3. Post all chapters
print(f"\n=== Đang đăng {len(chapters)} chương ===")
for i, chap in enumerate(chapters, 1):
    print(f"Đăng {chap['title']}...")
    res_c = bypass("POST", "chuong", {
        "title": chap["title"],
        "content": chap["content"],
        "status": "publish",
        "meta": {"_truyen_id": truyen_id}
    })
    if res_c.status_code == 201:
        chuong_link = res_c.json().get("link", "")
        print(f"  OK -> {chuong_link}")
    else:
        print(f"  LỖI: {res_c.status_code} {res_c.text[:200]}")
    time.sleep(1)

print(f"\n=== HOÀN TẤT ===")
print(f"Link truyện: {truyen_link}")
