import requests
import time

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
# UPDATED STORY CONTENT
# ======================================================

NEW_INTRO = """<p>Năm đó, Lâm Phong bị coi là <strong>phế vật</strong> — không tài năng, không thế lực, không ai muốn nhớ đến. Đêm chú ruột ép hắn ký giấy từ bỏ quyền thừa kế trước mặt cả gia tộc, không ai biết rằng đó cũng là đêm hắn phát hiện ra sự thật kinh hoàng: cái chết của cha mẹ hắn năm xưa... không phải tai nạn.</p>

<p>Ra đi với hai bàn tay trắng, Lâm Phong cứu sống một đại lão tài chính trong đêm giông bão. Ba năm được truyền dạy tất cả — quản trị, tài chính, pháp lý, chiến lược — hắn dùng từng ngày để xây dựng <em>Thiên Long Group</em> từ con số không.</p>

<p>Hôm nay hắn trở về. Không phải để khóc lóc hay van xin. Hắn trở về vì <strong>công lý chưa được thực thi</strong>, vì những kẻ có tội chưa một ngày hối hận, và vì hắn đã hứa với vong linh cha mẹ rằng: sẽ đứng thẳng ngay trên mảnh đất này và vả vào mặt tất cả những kẻ đáng bị vả.</p>

<p><em>Đồ phế vật năm đó — hôm nay đã là Vương.</em></p>"""

chapters_updated = [
    {
        "slug": "chuong-1-ke-bi-duoi-co-tro-ve",
        "title": "Chương 1: Kẻ Bị Đuổi Cổ Trở Về",
        "content": """<p>Đêm thành phố H lên đèn, chiếc Mercedes đen lướt nhẹ vào con phố trung tâm. Lâm Phong ngồi trong xe, mắt nhắm, nhưng không ngủ. Hắn đang nghe. Nghe tiếng tim đập. Nghe tiếng ba năm qua nén lại trong từng thớ cơ.</p>

<p>— "Thiếu gia, còn năm phút nữa là đến dinh thự Lâm gia." Tài xế — thực ra là cận vệ trưởng Đại Phong — kính cẩn báo.</p>

<p>Lâm Phong mở mắt. Nhìn qua kính xe, ánh đèn đường vàng nhạt kéo dài vô tận như một chuỗi ký ức không dứt.</p>

<p>Hắn nhớ. Đêm đó cũng là đêm như thế này. Mưa. Lạnh. Và căn đại sảnh Lâm gia sáng choang giữa giông bão, cả gia tộc đứng nhìn hắn ký giấy từ bỏ quyền thừa kế với những nụ cười thỏa mãn trên môi. Chú Lâm Vĩnh Thịnh đứng ở giữa, cầm tập hồ sơ, giọng lạnh như đá: <em>"Ký xong thì biến. Đừng để ta nhìn thấy mày nữa."</em></p>

<p>Lúc đó Lâm Phong không khóc. Không van xin. Hắn chỉ nhìn một lượt khắp phòng — ánh mắt người anh trai Quốc Bình cúi xuống né tránh; nụ cười khinh khỉnh của Kiều Diễm đằng sau chiếc quạt giấy; Triệu Mỹ Nga tựa vào vai Hoàng Tuấn Kiệt không thèm nhìn hắn lấy một lần — và ký.</p>

<p>Nhưng đêm đó còn có một thứ hắn phát hiện ra sau khi bước ra ngoài mưa. Một tập hồ sơ nhỏ rơi ra từ túi áo chú Thịnh trong lúc ông ta quay đi. Hắn lượm lên, tưởng là thứ không quan trọng. Hóa ra đó là bản phác thảo "kế hoạch tái cơ cấu tài sản sau tai nạn của anh Lâm Đình Sơn" — cha hắn — được lập từ ba ngày <em>trước</em> khi vụ tai nạn xảy ra.</p>

<p>Tai nạn giao thông. Đó là lý do chính thức mà cả gia tộc đưa ra cho cái chết của cha mẹ hắn sáu năm về trước. Nhưng kế hoạch được lập trước khi tai nạn xảy ra thì... ai lập? Ai đã biết trước?</p>

<p>Đêm đó Lâm Phong lang thang lên đỉnh núi Bạch Vân, không phải để chết, mà vì hắn cần một nơi không có người để hét thật to một tiếng rồi quyết định bước tiếp.</p>

<p>Trên đỉnh núi, hắn gặp một ông lão đang hấp hối — Vương Kiến Quốc, từng là tỷ phú tài chính lớn nhất vùng, đang bị ba tên đàn em bỏ lại sau khi lật xe vì tranh giành tài sản. Lâm Phong không nghĩ nhiều. Hắn cõng ông lão xuống núi, cầm máu, giữ ấm, gọi cấp cứu và ngồi bên ngoài phòng hồi sức suốt cả đêm.</p>

<p>Vương lão nhìn hắn từ trên giường bệnh, hỏi: "Tại sao mày giúp tao trong khi mày rõ ràng cũng đang khổ không kém?"</p>

<p>Lâm Phong trả lời: "Vì nếu không ai giúp ông thì ông chết. Đơn giản vậy thôi."</p>

<p>Vương lão cười. Nụ cười của người lần đầu tiên gặp được người thật trong đời. Ông ta nói: "Tao đã tìm truyền nhân suốt mười lăm năm. Mày theo tao không?"</p>

<p>Ba năm sau đó là ba năm Lâm Phong học mọi thứ. Quản trị doanh nghiệp. Tài chính. Pháp lý. Chiến lược thương chiến. Và trên hết — cách để kiên nhẫn chờ đợi thời điểm đúng. Vương lão mất vào cuối năm thứ ba, để lại toàn bộ tài sản và đế chế Thiên Long cho hắn với một câu: "Nhớ dùng nó đúng chỗ."</p>

<p>Xe dừng lại. Lâm Phong bước xuống. Trước mặt hắn là cổng dinh thự Lâm gia — đang treo đèn hoa rực rỡ. Bảng hiệu nhỏ ghi: <em>Tiệc kỷ niệm 30 năm thành lập Tập đoàn Lâm — Chào mừng quý khách.</em></p>

<p>Lâm Phong nhếch môi. Hắn không báo trước. Cũng không cần. Hắn biết hôm nay có tiệc — đó chính là lý do hắn chọn về đúng ngày này.</p>

<p>Người bảo vệ bước ra chặn lại. Nhìn chiếc xe, nhìn người đàn ông mặc vest đen đứng thẳng trước mặt mình, hắn ta ngập ngừng:</p>

<p>— "Xin hỏi... ông có giấy mời không?"</p>

<p>Lâm Phong nhìn thẳng vào mắt người bảo vệ với ánh mắt bình thản đến mức lạ lùng.</p>

<p>— "Không cần giấy mời. Nói với Lâm Vĩnh Thịnh rằng... đứa phế vật năm đó đã về."</p>

<p>Người bảo vệ đứng như trời trồng. Không hiểu sao đôi chân hắn bước vào trong gọi điện mà không nói được một lời từ chối.</p>

<p>Lâm Phong nhìn lên bầu trời đêm thành phố. Đúng ba năm. Đủ rồi.</p>

<p>Hắn bước vào."""
    },
    {
        "slug": "chuong-2-bua-tiec-nha-lam-va-cai-tat-dau-tien",
        "title": "Chương 2: Bữa Tiệc Và Video Năm Đó",
        "content": """<p>Bên trong đại sảnh, không khí tiệc đang ở đỉnh điểm. Hàng trăm khách mời — đối tác, quan chức, tài phiệt — đứng rải rác cụm cụm với ly rượu trên tay. Ở cuối phòng, một màn hình LED khổng lồ đang chiếu slideshow "30 năm hành trình Lâm gia" theo nhạc nền hào hùng.</p>

<p>Lâm Phong bước vào đúng lúc màn hình chuyển sang một clip cũ. Hình ảnh hạt nhân trong đó không phải thành tích hay sự kiện khai trương. Đó là clip quay lại bằng camera an ninh — cảnh đại sảnh này ba năm trước. Một người thanh niên gầy gò, tóc ướt đẫm mưa, cúi đầu ký vào một tập giấy dưới ánh đèn. Xung quanh là cả gia tộc đứng nhìn. Không ai giơ tay ngăn lại.</p>

<p>Ai đó trong phòng tiệc nhận ra trước. Rồi người khác. Rồi cả căn phòng dần im lặng như có phép thuật.</p>

<p>Lâm Vĩnh Thịnh đứng ở trung tâm phòng, mặt đang tươi bỗng đông cứng lại. Ông ta nhìn lên màn hình, rồi quay đầu nhìn về phía cửa, và thấy Lâm Phong đang đứng ở đó — áo vest đen, tay đút túi, mắt nhìn thẳng về phía màn hình như đang xem một bộ phim nhạt nhẽo.</p>

<p>— "Tắt clip đó đi!" Lâm Vĩnh Thịnh quay sang trợ lý, giọng gắt.</p>

<p>— "Thôi khoan đã." Lâm Phong lên tiếng, giọng bình thản vang lên trong không khí im lặng như cắt được bằng dao. "Để mọi người xem cho hết. Đây là lịch sử Lâm gia mà. Phải trân trọng chứ."</p>

<p>Tiếng xì xào nổi lên trong đám khách. Lâm Vĩnh Thịnh bước về phía hắn, mặt đỏ bừng:</p>

<p>— "Mày dám vào đây làm loạn hả Lâm Phong? Bảo vệ đâu rồi, tống cổ nó ra ngoài!"</p>

<p>Không ai nhúc nhích. Hai người đàn ông to lớn trong vest xám đứng sau Lâm Phong nhìn đám bảo vệ với ánh mắt khiến họ không dám tiến thêm nửa bước.</p>

<p>— "Chú Hai." Giọng Lâm Phong vẫn đều đều. "Con biết chú đang lo lắng điều gì. Nhưng con không đến để làm loạn." Hắn rút từ túi trong ra một phong bì dày, đặt lên bàn tiệc gần nhất. "Con đến để trao tận tay một thông báo pháp lý."</p>

<p>Một người đàn ông trung niên mặc vest xám bước ra — luật sư trưởng của Thiên Long, học vị Tiến sĩ Luật, từng là Chánh án phó trước khi về làm việc cho khu vực tư.</p>

<p>— "Thưa ông Lâm Vĩnh Thịnh." Ông ta mở tập hồ sơ, giọng chuyên nghiệp lạnh lùng. "Thiên Long Group đã hoàn tất việc mua lại toàn bộ 200 tỷ khoản nợ xấu của Tập đoàn Lâm tại ba ngân hàng: Đông Á, Á Châu và Phương Nam. Đây là bản xác nhận từ cả ba tổ chức tín dụng, có chữ ký và dấu đỏ đầy đủ."</p>

<p>Ông ta lật từng trang ra đặt xuống bàn. Ba tờ xác nhận. Ba con dấu đỏ chói. Không cần giả mạo. Không cần bịa đặt. Tất cả đều là thật, đã được lên hệ thống từ tuần trước.</p>

<p>Giám đốc ngân hàng Đông Á — đang là khách mời trong tiệc — khẽ gật đầu xác nhận khi ánh mắt mọi người nhìn về phía ông ta. Ông ta không có lựa chọn nào khác ngoài gật đầu. Hợp đồng đã ký rồi.</p>

<p>Lâm Vĩnh Thịnh cầm tờ xác nhận lên, tay run. Ông ta nhìn từng chữ, từng con số. Thật. Tất cả đều thật. Thiên Long đã mua lại khoản nợ của gia tộc mình mà ông ta không hay biết — vì mọi giao dịch đều được thực hiện qua một công ty trung gian ở nước ngoài.</p>

<p>— "Điều này... điều này không thể..." Giọng ông ta khàn đi.</p>

<p>— "Hoàn toàn có thể và hoàn toàn hợp pháp." Lâm Phong bước thêm một bước về phía chú. Giờ hai người chỉ cách nhau chưa đầy hai mét. "Chú Hai. Ba năm trước chú đã trao cho con một tờ giấy và bảo con ký. Hôm nay con trao lại cho chú một tập hồ sơ. Công bằng chứ?"</p>

<p>Lâm Vĩnh Thịnh nhìn vào mắt cháu trai. Lần đầu tiên trong đời, ông ta thấy sợ.</p>

<p>— "À, còn một điều nữa." Lâm Phong quay sang phía Lâm Kiều Diễm — cô em họ đang đứng há hốc miệng ở góc phòng. "Nhà cung cấp vải chính cho thương hiệu thời trang của em — Hoa Thịnh Textile — vừa ký hợp đồng độc quyền với Thiên Long sáng nay. Từ quý tới, em sẽ cần đàm phán lại giá nguyên liệu. Chúc may mắn."</p>

<p>Tiếng ly rượu vỡ đâu đó trong góc phòng.</p>

<p>Lâm Phong nhìn quanh một lượt — những gương mặt sững sờ, những ánh mắt hoảng loạn, cái không khí tiệc vui vẻ bây giờ đặc quánh như bê tông — rồi hắn gật đầu lịch sự:</p>

<p>— "Thưa quý vị, xin lỗi đã làm phiền bữa tiệc. Chúc mọi người vui vẻ."</p>

<p>Hắn quay người bước ra. Màn hình LED phía sau vẫn đang chiếu hình ảnh đứa thanh niên tóc ướt cúi đầu ký giấy năm xưa.</p>

<p>Không ai tắt nó đi nữa. Không ai còn nhớ đến việc tắt nó đi."""
    },
    {
        "slug": "chuong-3-nguoi-tinh-cu-va-ten-tieu-nhan",
        "title": "Chương 3: Người Tình Cũ Và Tên Tiểu Nhân",
        "content": """<p>Triệu Mỹ Nga đặt điện thoại xuống bàn, nhìn chằm chằm vào màn hình đang hiển thị bài báo: <em>"Thiếu gia Lâm Phong — Phế vật hay Phụng hoàng?"</em> Dưới bài là tấm ảnh chụp Lâm Phong bước ra khỏi dinh thự Lâm gia tối qua, vest đen, mắt lạnh, đằng sau là cả một bầu trời đèn hoa lung linh.</p>

<p>Cô nhìn mãi vào tấm ảnh đó. Không phải vì tò mò. Mà vì một thứ gì đó trong ngực cô thắt lại mà cô không chịu nhận ra là gì.</p>

<p>— "Anh đặt bàn ở Seasons rồi. Đi thôi em." Hoàng Tuấn Kiệt bước ra từ phòng thay đồ, áo sơ mi trắng, tóc vuốt gọn. Đẹp trai, thành đạt, là con trai của một gia đình có tiếng. Tất cả những thứ Mỹ Nga đã chọn thay vì Lâm Phong.</p>

<p>Seasons là nhà hàng sang nhất thành phố. Bàn VIP tầng bốn nhìn xuống cả con phố đèn hoa. Hoàng Tuấn Kiệt đặt bàn ở đây vì hắn muốn thể hiện — thể hiện với ai không rõ, nhưng cứ thể hiện đã.</p>

<p>Họ vừa ngồi xuống thì cửa nhà hàng mở ra. Lâm Phong bước vào. Đi sau hắn là Minh Nguyệt — trợ lý riêng, vest trắng, kính gọng mỏng, tay cầm tablet luôn sẵn sàng.</p>

<p>Mỹ Nga cứng người. Tim đập loạn một nhịp.</p>

<p>Tuấn Kiệt nhìn thấy, mặt tái đi. Hắn đứng dậy, giọng gắt:</p>

<p>— "Lâm Phong! Mày theo dõi chúng tao à?"</p>

<p>Lâm Phong nhìn qua Tuấn Kiệt như nhìn qua một cái cây trên đường — nhận ra sự hiện diện nhưng không có lý do để dừng lại. Hắn nhìn người quản lý:</p>

<p>— "Tôi có đặt bàn số 7 từ thứ Hai. Tên Lâm Phong."</p>

<p>Người quản lý cúi đầu, mặt khó xử:</p>

<p>— "Vâng, bàn số 7 quả thật là của ngài Lâm ạ. Hôm nay có sự nhầm lẫn trong hệ thống đặt bàn, chúng tôi xin lỗi..."</p>

<p>Hoàng Tuấn Kiệt đỏ mặt. Hắn bước về phía Lâm Phong:</p>

<p>— "Mày nghĩ mày là ai? Mày tưởng có tiền thì được làm tất cả hả—"</p>

<p>Hắn vươn tay ra định túm cổ áo. Nhưng tay hắn chưa chạm được vào áo thì đã bị một bàn tay to hơn nắm lấy cổ tay, bẻ nhẹ ra sau. Cận vệ của Lâm Phong — người đứng im như tượng từ nãy — đã di chuyển nhanh đến mức không ai kịp thấy.</p>

<p>Tuấn Kiệt ré lên vì đau, mặt dúm lại. Cận vệ thả ra, lùi về.</p>

<p>Lâm Phong vẫn chưa nhúc nhích. Hắn nhìn Tuấn Kiệt đang ôm cổ tay với ánh mắt bình thản:</p>

<p>— "Anh Tuấn Kiệt. Tôi nhớ hồi đại học, anh hay vay tiền rồi không trả. Nhà hàng này cũng có khoản nợ 80 triệu chưa thanh toán của anh từ năm ngoái." Hắn quay sang quản lý. "Anh có muốn giải quyết hôm nay không? Tôi có thể làm chứng."</p>

<p>Người quản lý tái mặt nhưng gật đầu rụt rè. Tuấn Kiệt mặt tím tái, kéo tay Mỹ Nga:</p>

<p>— "Đi! Không cần ăn ở đây nữa!"</p>

<p>Mỹ Nga đứng dậy nhưng chân không muốn bước. Cô nhìn về phía Lâm Phong — lần đầu tiên hắn nhìn lại cô. Chỉ một giây. Một ánh mắt không phán xét, không oán hận, không đau. Chỉ là... xa lạ. Như nhìn một người không quen.</p>

<p>Đó là cái nhìn làm cô đau hơn bất kỳ thứ gì.</p>

<p>Sau khi hai người bước ra, Minh Nguyệt khẽ nói bên tai Lâm Phong:</p>

<p>— "Thiếu gia không cần phải chọn chỗ này tối nay."</p>

<p>— "Ta biết." Lâm Phong ngồi xuống ghế, cầm tờ thực đơn lên. "Nhưng hắn hay đến đây vào tối thứ Năm. Ta chỉ muốn nhắc hắn nhớ rằng... thành phố này không còn là nơi hắn muốn làm gì thì làm."</p>

<p>Minh Nguyệt nhìn hắn một lúc. Sau ba năm theo bên cạnh, cô hiểu — những lúc Lâm Phong có vẻ lạnh nhất là những lúc hắn đang cố không để lộ ra thứ gì đó đang rỉ máu bên trong.</p>

<p>— "Thiếu gia có muốn gọi món quen không?"</p>

<p>Lâm Phong khẽ gật. Món quen — cà phê đen, không đường, một đĩa bánh mì nướng. Đúng cái thứ hắn đã ăn suốt ba năm ở căn nhà thuê của Vương lão trong những đêm học bài đến tận sáng.</p>

<p>Không ai biết rằng sau tất cả những màn vả mặt hào nhoáng đó, Lâm Phong đêm nào cũng mơ thấy đêm mưa năm xưa. Và đêm nào hắn cũng thức giấc lúc ba giờ sáng, ngồi một mình trong bóng tối, nhìn ra thành phố đèn sáng và tự hỏi: <em>Sau khi tất cả xong rồi... còn lại gì?</em>"""
    },
    {
        "slug": "chuong-4-man-hop-bao-chan-dong",
        "title": "Chương 4: Họp Báo Và Đòn Phản Công Trong Bóng Tối",
        "content": """<p>Buổi họp báo tại khách sạn Hoàng Cung thu hút hơn năm mươi tờ báo và đài truyền hình. Khi Lâm Phong bước lên sân khấu, tiếng vỗ tay vang lên không phải vì người ta quý mến hắn — mà vì người ta tò mò. Ai cũng muốn tận mắt xem đứa con bị gia tộc hắt hủi đã trở về dưới hình hài gì.</p>

<p>Câu trả lời là: áo vest đen, đứng thẳng, và không có một gam áp lực nào trên mặt.</p>

<p>Phóng sự buổi chiều chạy trên tất cả các kênh lớn. Từ "phế vật" trở thành chủ tịch Thiên Long Group — đế chế tài chính và bất động sản xếp hạng ba toàn quốc. Câu chuyện đẹp. Câu chuyện truyền cảm hứng. Báo chí thích nó.</p>

<p>Nhưng trong khi công chúng đang say sưa với câu chuyện truyền cảm hứng đó, ở một văn phòng kín trên tầng mười lăm của tòa nhà Lâm Group, một cuộc họp khác đang diễn ra — không có đèn chụp ảnh, không có micro, không có người ghi biên bản.</p>

<p>— "Tôi cần anh phong tỏa tài khoản của Thiên Long tại thị trường này." Lâm Vĩnh Thịnh ngồi đối diện với một người đàn ông tóc hoa râm, vest tím nhạt — Phó Chủ tịch Hiệp hội Thương nhân, người có tầm ảnh hưởng rộng với hệ thống ngân hàng địa phương.</p>

<p>— "Đó là việc lớn, anh Thịnh." Người đàn ông kia nhấc ly trà lên. "Thiên Long là tập đoàn tầm quốc gia. Nếu tôi ra tay, sẽ cần lý do hợp pháp."</p>

<p>— "Tôi sẽ tạo ra lý do." Lâm Vĩnh Thịnh nhìn thẳng. "Có người sẵn sàng khai rằng Thiên Long dùng vốn bẩn từ nước ngoài để thâu tóm tài sản trong nước. Chỉ cần lời khai đó đủ để mở điều tra sơ bộ — đoàn kiểm toán vào, tài khoản bị tạm khóa trong thời gian điều tra, hàng loạt hợp đồng đang ký sẽ bị đình hoãn. Đủ để làm Thiên Long mất uy tín ở thị trường này."</p>

<p>Im lặng kéo dài. Người đàn ông tóc hoa râm nhấp một ngụm trà.</p>

<p>— "Anh biết đây là canh bạc lớn chứ? Nếu thằng Lâm Phong có bằng chứng ngược lại..."</p>

<p>— "Thì tôi đã tính toán kỹ." Lâm Vĩnh Thịnh gõ nhẹ ngón tay lên bàn. "Nó mới về. Chưa thiết lập được mạng lưới quan hệ ở đây. Đây là thời điểm tốt nhất."</p>

<p>Người đàn ông kia gật đầu chậm rãi.</p>

<p>Lâm Phong không biết điều này khi hắn bước ra khỏi khách sạn Hoàng Cung sau buổi họp báo. Nhưng Minh Nguyệt đang đứng chờ với khuôn mặt nghiêm trọng hơn mức bình thường.</p>

<p>— "Thiếu gia. Có tin từ trong."</p>

<p>— "Nói đi."</p>

<p>— "Ông Thịnh vừa gặp Phó Chủ tịch Hiệp hội Thương nhân. Nguồn tin từ bên trong xác nhận họ đang lên kế hoạch yêu cầu điều tra nguồn vốn của Thiên Long, có thể dẫn đến phong tỏa tài khoản tạm thời."</p>

<p>Lâm Phong dừng bước. Nhìn lên bầu trời đêm. Thở ra một hơi dài.</p>

<p>— "Nhanh hơn ta tưởng." Hắn khẽ nói. "Họ sẽ đánh vào tuần tới."</p>

<p>— "Chúng ta cần làm gì?"</p>

<p>Lâm Phong suy nghĩ một lúc. Trong ba năm theo Vương lão, ông ta đã dạy hắn một bài học đắt giá: <em>"Đừng chỉ phòng thủ. Hãy biết kẻ thù sẽ đánh vào đâu, và đặt bẫy ở đó trước."</em></p>

<p>— "Để họ đánh." Lâm Phong quay người bước về phía xe. "Ta cần họ đánh để lộ ra tất cả. Chuẩn bị hồ sơ bằng chứng. Và liên hệ với phóng viên Thanh Minh — nói cô ấy chuẩn bị cho một câu chuyện độc quyền vào cuối tuần tới."</p>

<p>Minh Nguyệt ghi chú nhanh vào tablet. Rồi cô ngẩng đầu lên, nhìn hắn với ánh mắt không hẳn là lo lắng mà là... hiểu.</p>

<p>— "Thiếu gia." Cô khẽ nói. "Ông Vương lão nếu còn đây, ông ấy sẽ tự hào lắm."</p>

<p>Lâm Phong không nói gì. Hắn chỉ bước vào xe và đóng cửa lại. Trong bóng tối của khoang xe, gương mặt hắn mới để lộ ra thứ mà ban ngày hắn không bao giờ cho người khác thấy: một thoáng mệt mỏi, và một nỗi nhớ không tên."""
    },
    {
        "slug": "chuong-5-bay-cua-ke-thu-va-don-phan-cong",
        "title": "Chương 5: Khi Cả Thành Phố Quay Lưng",
        "content": """<p>Thứ Ba tuần sau, như đúng dự đoán của Lâm Phong, cơn bão đổ xuống.</p>

<p>Sáng sớm, đoàn kiểm toán thuế xuất hiện tại văn phòng Thiên Long với lệnh điều tra khẩn cấp. Cùng lúc đó, trên các mạng xã hội, hàng loạt tài khoản ẩn danh đồng loạt đăng một bài viết dài với tiêu đề: <em>"Thiên Long Group — Đế chế bẩn được xây từ tiền rửa?"</em> Bài viết lan nhanh như cháy rừng. Đến trưa, nó đã được chia sẻ hơn mười nghìn lần.</p>

<p>Và đòn cuối cùng: ba ngân hàng đối tác tại thành phố H đồng loạt thông báo "tạm dừng giao dịch với Thiên Long để phối hợp điều tra theo yêu cầu cơ quan chức năng". Điều này đồng nghĩa với việc tất cả tài khoản thanh toán dự án tại thành phố H bị đóng băng tạm thời.</p>

<p>Hợp đồng mua đất dự án 2.000 tỷ sắp ký bị đối tác xin hoãn. Hai nhà thầu lớn gọi điện hỏi thăm với giọng điệu lo lắng. Một số nhà đầu tư nhỏ lẻ bắt đầu gọi điện hỏi về việc rút vốn.</p>

<p>Văn phòng Thiên Long tại thành phố H như một con thuyền đang gặp bão.</p>

<p>Minh Nguyệt đứng trước màn hình hiển thị hàng loạt thông báo, mặt tái nhợt:</p>

<p>— "Thiếu gia... tình hình nghiêm trọng hơn dự kiến. Các ngân hàng họ phối hợp quá nhanh. Có vẻ ông Thịnh có người bên trong."</p>

<p>Lâm Phong ngồi sau bàn làm việc, tay đang cầm một tách cà phê nguội. Hắn nghe, gật đầu, và không có biểu cảm gì đặc biệt.</p>

<p>— "Ta biết." Hắn đặt tách xuống. "Đây không phải lần đầu ta ở trong tình huống tệ hơn thế này."</p>

<p>Minh Nguyệt nhớ lại. Năm thứ nhất theo Vương lão, có một lần cả công ty bị đối thủ dùng quan hệ chính trị để phong tỏa hoạt động. Lâm Phong khi đó chỉ là trợ lý nhưng đã thức ba ngày liên tiếp để lập hồ sơ phản biện, tự tay gõ từng trang văn bản pháp lý. Vương lão nhìn hắn và nói: <em>"Bây giờ tao hiểu tại sao mày không chịu chết đêm đó trên núi."</em></p>

<p>— "Bây giờ làm gì?" Cô hỏi.</p>

<p>— "Mở cuộc họp khẩn với đoàn kiểm toán. Cung cấp toàn bộ hồ sơ tài chính — không phải vì ta sợ, mà vì ta muốn họ hoàn tất việc xác minh trong vòng 48 tiếng thay vì hai tuần." Lâm Phong đứng dậy, bước ra cửa sổ nhìn xuống thành phố. "Và kích hoạt phương án B."</p>

<p>— "Phương án B..."</p>

<p>— "Tập hồ sơ ta đã chuẩn bị về vụ tai nạn của cha mẹ ta." Giọng hắn trầm xuống một chút. Chỉ một chút. "Đã đến lúc dùng nó."</p>

<p>Hai ngày tiếp theo là hai ngày khốc liệt nhất. Đoàn kiểm toán làm việc ngày đêm với hồ sơ Thiên Long. Luật sư của Lâm Phong làm việc song song, chuẩn bị tài liệu phản bác từng điểm trong cáo buộc. Minh Nguyệt không rời văn phòng, ngủ ngay trên ghế sofa góc phòng.</p>

<p>Đêm thứ hai, khoảng hai giờ sáng, Lâm Phong bước vào phòng và thấy Minh Nguyệt đang ngủ gật trên đống hồ sơ. Hắn đứng nhìn cô một lúc, rồi lấy áo khoác của mình đắp lên vai cô.</p>

<p>Hắn ngồi xuống đối diện, nhìn ra cửa sổ. Thành phố lúc hai giờ sáng buồn và đẹp theo một cách kỳ lạ. Hắn nghĩ đến cha mẹ. Nghĩ đến Vương lão. Nghĩ đến cái đêm mưa ba năm trước.</p>

<p><em>Cha ơi... con đã gần đến rồi.</em></p>

<p>Sáng thứ Năm, kết quả kiểm toán hoàn tất: <strong>Thiên Long hoàn toàn sạch.</strong> Không một vi phạm nhỏ nhất. Trưởng đoàn kiểm toán ký vào biên bản xác nhận với vẻ mặt vừa ngạc nhiên vừa nể phục.</p>

<p>Cùng ngày hôm đó, phóng sự độc quyền lên sóng. Phóng viên Thanh Minh ngồi đối diện Lâm Phong trong studio.</p>

<p>— "Ngài có biết ai đứng sau vụ tung tin đồn này không?"</p>

<p>— "Tôi biết." Lâm Phong đặt tập hồ sơ lên bàn — không chỉ bằng chứng về việc tung tin đồn. Tập hồ sơ này dày hơn nhiều. "Và tôi đã nộp đơn tố cáo lên cơ quan công an, không chỉ về tội cạnh tranh không lành mạnh." Hắn nhìn thẳng vào máy quay. "Mà còn về một vụ việc cũ hơn. Một vụ tai nạn giao thông xảy ra sáu năm trước. Và một bản kế hoạch được lập ra trước khi tai nạn đó xảy ra."</p>

<p>Cả studio lặng đi. Phóng viên Thanh Minh nhìn vào mắt Lâm Phong và hiểu — câu chuyện này lớn hơn rất nhiều so với những gì cô tưởng.</p>

<p>Đêm hôm đó, điện thoại của Lâm Vĩnh Thịnh không ngừng rung. Nhưng lần này ông ta không bắt máy. Ông ta ngồi trong phòng tối, nhìn chằm chằm vào bức tường, và nhận ra: hắn đã sa vào cái bẫy mà chính hắn đã đào."""
    },
    {
        "slug": "chuong-6-dam-cuoi-bi-pha",
        "title": "Chương 6: Đám Cưới Và Sự Thật Năm Xưa",
        "content": """<p>Đám cưới Hoàng Tuấn Kiệt — Triệu Mỹ Nga được tổ chức vào một sáng thứ Bảy tháng Năm. Hoa hồng trắng phủ kín khách sạn Hoàng Cung từ sảnh chờ đến phòng tiệc. Năm trăm khách mời. Váy cưới đặt may riêng từ Pháp về. Nhẫn kim cương bốn cara.</p>

<p>Triệu Mỹ Nga nhìn mình trong gương — đẹp, hoàn hảo, như mọi thứ cô đã lên kế hoạch. Nhưng có một thứ cô không lên kế hoạch được: buổi sáng đó, khi cô đang ngồi trang điểm, điện thoại cô nhận được tin nhắn từ một số lạ. Chỉ một dòng: <em>"Cô có biết tiền đặt cọc cho hôn trường hôm nay được lấy từ đâu không?"</em></p>

<p>Kèm theo là một đường link đến bản tin tài chính: Hoàng Tuấn Kiệt đã cầm cố căn penthouse — quà cưới cho Mỹ Nga — để vay tiền đầu tư vào một dự án crypto đã sụp đổ hai tháng trước. Khoản vay 15 tỷ đồng, đến hạn từ tháng trước. Ngân hàng đang chuẩn bị thủ tục thu hồi tài sản.</p>

<p>Mỹ Nga ngồi đó, tay run cầm điện thoại, mặt vẫn còn đang được thợ trang điểm kẻ mắt.</p>

<p>Đại diện ngân hàng xuất hiện ở sảnh khách sạn lúc mười giờ sáng — đúng một tiếng trước giờ G. Họ lịch sự nhưng kiên quyết. Tin đồn loang ra trong phòng tiệc chỉ mất mười lăm phút.</p>

<p>Hoàng Tuấn Kiệt gọi điện cho tất cả những người có thể giúp. Không ai bắt máy. Hoặc bắt máy rồi nói "xin lỗi, không tiện".</p>

<p>Hắn gọi cho Lâm Vĩnh Thịnh — người đã hứa sẽ "chống lưng" cho hắn từ ngày hắn bắt đầu tham gia vào các kế hoạch chống Thiên Long. Đầu dây bên kia có tiếng còi bận.</p>

<p>Cuối cùng, trong lúc tuyệt vọng, Hoàng Tuấn Kiệt lặng lẽ bước ra cửa hông khách sạn. Không nói với ai. Không để lại lời nhắn.</p>

<p>Triệu Mỹ Nga đứng giữa phòng tiệc, váy trắng tinh, hoa trong tay, và không có chú rể.</p>

<p>Cô gọi cho Lâm Phong. Không biết sao lại gọi cho hắn. Có lẽ vì trong danh sách liên lạc của cô, hắn là người duy nhất mà cô biết chắc sẽ bắt máy.</p>

<p>Lâm Phong bắt máy sau hồi chuông thứ hai.</p>

<p>— "Phong..." Giọng Mỹ Nga run. "Anh... anh có thể..."</p>

<p>— "Mỹ Nga." Giọng hắn bình thản. Không lạnh. Không ấm. Chỉ là... bình thản. "Anh biết chuyện gì đang xảy ra rồi."</p>

<p>— "Thì anh có thể giúp không? Chỉ cần..."</p>

<p>— "Anh không thể giúp." Một khoảng lặng ngắn. "Không phải vì anh không muốn. Mà vì đây là hậu quả của những lựa chọn mà anh ta đã tự đưa ra. Và em cũng vậy."</p>

<p>Mỹ Nga cắn môi. Nước mắt chảy dài làm hỏng lớp mascara vừa được kẻ cẩn thận.</p>

<p>— "Anh hận em lắm không?"</p>

<p>Khoảng lặng dài hơn lần này. Lâm Phong nhìn ra cửa sổ văn phòng — bầu trời thứ Bảy xanh và sạch.</p>

<p>— "Không." Hắn nói thật. "Anh không hận. Nhưng anh cũng không có gì để cho em nữa, Mỹ Nga." Giọng hắn dịu lại một chút — lần hiếm hoi trong suốt thời gian hắn trở về. "Em xứng đáng được hạnh phúc. Nhưng đó phải là hạnh phúc do em tự xây, không phải hạnh phúc đặt trên lưng người khác."</p>

<p>Máy cúp.</p>

<p>Triệu Mỹ Nga đứng giữa phòng tiệc lộng lẫy, và lần đầu tiên trong ba năm qua, cô cho phép mình khóc thật sự — không phải vì mất đám cưới, không phải vì mất Tuấn Kiệt. Mà vì cô hiểu ra rằng từ ngày cô quay lưng lại với Lâm Phong, cô đã đang đi sai đường.</p>

<p>Ở một nơi khác trong thành phố, Lâm Phong ngồi sau bàn làm việc, nhìn vào tập hồ sơ dày trước mặt. Bên trên trang đầu là ảnh chụp lại bản kế hoạch tái cơ cấu tài sản được lập ba ngày trước khi cha mẹ hắn "gặp tai nạn". Bên dưới là chuỗi bằng chứng mà hắn đã dành ba năm để gom lại, từng mảnh một.</p>

<p>— "Minh Nguyệt." Hắn gọi.</p>

<p>— "Dạ."</p>

<p>— "Ngày mai lên lịch gặp Cục trưởng Cục Điều tra. Đã đến lúc rồi."</p>"""
    },
    {
        "slug": "chuong-7-man-ket-toan-voi-gia-toc-lam",
        "title": "Chương 7: Kết Toán — Và Sự Thật Về Đêm Tai Nạn",
        "content": """<p>Cuộc họp tại đại sảnh Lâm gia không chỉ có luật sư và hồ sơ tài chính. Lần này, ngồi ở đầu bàn bên trái là hai sĩ quan cảnh sát sắc phục chỉnh tề. Sự xuất hiện của họ làm cả căn phòng đông cứng ngay từ lúc họ bước vào.</p>

<p>Lâm Vĩnh Thịnh nhìn hai người cảnh sát, mặt tái nhợt hơn cả hôm ở tiệc. Ông ta hiểu ngay điều gì đang đến.</p>

<p>— "Chúng ta có thể... có thể xử lý chuyện kinh doanh trước không?" Giọng ông ta run.</p>

<p>— "Được." Lâm Phong ngồi xuống ghế chủ tọa, nhìn thẳng vào mắt chú. "Về phần kinh doanh: Thiên Long sẽ tiếp quản 51% cổ phần Tập đoàn Lâm để bù nợ. 49% còn lại, gia tộc giữ. Điều kiện: ông rút khỏi mọi vị trí lãnh đạo và hội đồng quản trị." Hắn đẩy hồ sơ qua bàn. "Ký vào đây."</p>

<p>Lâm Vĩnh Thịnh nhìn tập hồ sơ. Tay ông ta cầm bút nhưng không hạ xuống.</p>

<p>— "Phong... cháu phải hiểu rằng chú làm tất cả là vì gia tộc. Vì anh Sơn — cha cháu — đã mắc sai lầm trong kinh doanh, nếu không có chú xử lý thì cả tập đoàn đã sụp từ lâu..."</p>

<p>— "Chú Hai." Giọng Lâm Phong cắt ngang, bình thản như mặt hồ trước bão. "Đừng nhắc đến cha con."</p>

<p>Lâm Quốc Bình — anh trai — đang ngồi bên cạnh đột nhiên ngẩng đầu lên. Có gì đó trong giọng em trai khiến ông ta cảm thấy như có ai vừa đặt một tảng đá lên ngực.</p>

<p>Lâm Phong đứng dậy, bước đến bên cửa sổ. Nhìn ra khu vườn nơi hắn đã chạy nhảy lúc còn nhỏ. Giọng hắn trầm xuống, lần đầu tiên trong suốt thời gian trở về có chút gì đó không phải là lạnh lùng:</p>

<p>— "Con đã mất sáu năm để hiểu tại sao cha mẹ con chết. Và mất thêm ba năm để có đủ bằng chứng." Hắn quay người lại. "Bản kế hoạch 'tái cơ cấu tài sản sau tai nạn của anh Lâm Đình Sơn' — được lập ba ngày trước khi tai nạn xảy ra — chú Hai có nhớ không? Con đã nhặt nó từ sàn nhà đêm chú đuổi con đi."</p>

<p>Lâm Vĩnh Thịnh mặt biến thành màu tro. Ông ta không nói được lời nào.</p>

<p>— "Và còn có nhân chứng." Lâm Phong gật đầu về phía hai sĩ quan cảnh sát. "Tài xế xe container năm đó — người mà chú đã trả tiền và bố trí visa đi nước ngoài sau vụ tai nạn — anh ấy đã tự nguyện quay về và khai báo đầy đủ."</p>

<p>Lâm Quốc Bình phát ra một tiếng thấp nghẹn trong cổ họng. Ông ta nhìn chú, rồi nhìn em trai, rồi cúi đầu xuống bàn.</p>

<p>— "Anh..." Lâm Phong nhìn anh trai lần đầu tiên trong buổi họp, giọng khác đi — không còn lạnh, nhưng cũng không hề ấm. Chỉ là mệt mỏi thật sự. "Anh có biết không?"</p>

<p>Lâm Quốc Bình không ngẩng đầu lên. Hắn không trả lời. Nhưng sự im lặng đó đã là câu trả lời rồi.</p>

<p>Lâm Phong nhìn anh trai một hồi lâu. Rồi hắn thở ra một hơi thật dài, quay sang luật sư:</p>

<p>— "Tiếp tục thủ tục ký kết. Phần còn lại là việc của cơ quan công an."</p>

<p>Hai sĩ quan cảnh sát đứng dậy. Một trong hai bước về phía Lâm Vĩnh Thịnh:</p>

<p>— "Ông Lâm Vĩnh Thịnh. Mời ông đi theo chúng tôi để làm việc về vụ tai nạn ngày 15 tháng 3 năm 2020."</p>

<p>Lâm Vĩnh Thịnh đứng dậy, đôi chân run. Ông ta nhìn về phía Lâm Phong lần cuối với ánh mắt của một người hiểu rằng mình đã thua — không phải thua về tiền, không phải thua về địa vị, mà thua về nhân cách từ rất lâu trước đây.</p>

<p>Hắn không nói gì. Đi theo cảnh sát ra khỏi căn phòng mà ông ta đã thống trị suốt nhiều năm.</p>

<p>Đại sảnh Lâm gia im lặng tuyệt đối. Lâm Phong đứng giữa phòng một mình, nhìn xuống tập hồ sơ trên bàn. Bên dưới tất cả những trang giấy đó là một tấm ảnh cũ — ảnh gia đình chụp năm hắn mười hai tuổi. Cha, mẹ, và hắn đứng giữa, tất cả đều cười.</p>

<p>Hắn cầm tấm ảnh lên. Đặt vào túi ngực, gần tim.</p>

<p>Rồi bước ra ngoài, không ngoái đầu lại."""
    },
    {
        "slug": "chuong-8-binh-minh-cua-ke-tro-ve",
        "title": "Chương 8: Bình Minh — Và Những Gì Còn Lại",
        "content": """<p>Một tháng sau.</p>

<p>Thành phố H vào buổi sáng sớm đẹp theo cách chỉ người thức giấc trước năm giờ mới biết — bầu trời còn tím thẫm ở phía Đông, ánh đèn đường vàng nhạt đang dần tắt, và con phố dưới lầu vắng đến mức nghe được tiếng gió.</p>

<p>Lâm Phong đứng trên ban công tầng 32, tay cầm tách cà phê, không mặc vest. Áo sơ mi trắng bỏ ngoài quần, tóc chưa chải. Đây là kiểu Lâm Phong mà chỉ một người duy nhất từng thấy — Minh Nguyệt.</p>

<p>Cô bước ra ban công, đứng cạnh hắn, cũng cầm một tách cà phê. Họ không nói gì ngay. Đứng nhìn thành phố thức dậy từng chút một.</p>

<p>— "Hôm nay lịch trống buổi sáng." Minh Nguyệt nói. "Thiếu gia có muốn ngủ thêm không? Lần cuối ngủ đủ giấc là khi nào rồi?"</p>

<p>— "Không nhớ." Lâm Phong nhấp cà phê. "Từ trước khi trở về thành phố này, chắc vậy."</p>

<p>Minh Nguyệt nhìn hắn từ góc nghiêng. Ba năm. Cô đã theo bên hắn ba năm, từ ngày Vương lão đưa hắn vào văn phòng và giới thiệu: "Đây là Lâm Phong, từ nay là người kế thừa của tao, mày lo cho nó." Cô đã xem hắn học từ không biết gì đến biết tất cả. Xem hắn thức đêm. Xem hắn thất bại rồi đứng dậy. Xem hắn xây dựng Thiên Long từ một công ty nhỏ thành đế chế.</p>

<p>Và cô cũng đã xem hắn mỗi đêm nhìn ra cửa sổ với khuôn mặt của một người đang mang theo thứ gì đó không bao giờ đặt xuống được.</p>

<p>— "Ông Vương lão trước lúc mất có nói với tôi một câu." Minh Nguyệt khẽ nói. "Ông nói: 'Thằng Phong nó sẽ thành công. Nhưng mày phải đảm bảo sau khi nó thành công rồi, nó không quên mất cách để là một người bình thường.'"</p>

<p>Lâm Phong không nói gì. Nhưng hắn cầm tách cà phê chặt hơn một chút.</p>

<p>— "Thiếu gia." Cô tiếp tục. "Bây giờ mọi thứ đã xong rồi. Ông Thịnh đang bị điều tra. Gia tộc đã được sắp xếp lại. Tập đoàn Lâm có người quản lý mới. Thiên Long tiếp tục dự án. Công lý đã được thực thi."</p>

<p>— "Ừ."</p>

<p>— "Thiếu gia cảm thấy thế nào?"</p>

<p>Một khoảng lặng dài. Ánh bình minh bắt đầu rạng lên ở chân trời phía Đông — một dải màu cam nhạt, mỏng manh nhưng đủ mạnh để đẩy bóng tối ra xa.</p>

<p>— "Không hẳn là như ta tưởng." Lâm Phong thật thà. "Ta cứ nghĩ khi mọi thứ xong, sẽ thấy nhẹ. Thực ra... vẫn còn đó. Cái nặng đó không biến mất chỉ vì kẻ có lỗi đã bị trừng phạt."</p>

<p>Minh Nguyệt gật đầu. Cô hiểu. Có những vết thương mà công lý không chữa lành được — chỉ có thời gian mới làm được.</p>

<p>— "Mỹ Nga gửi thư lần thứ tư." Cô nói nhẹ nhàng.</p>

<p>— "Ta biết." Hắn nhìn xa ra phía chân trời. "Nguyệt... âm thầm giới thiệu cho cô ấy một vị trí quản lý tốt ở một công ty bạn. Không nhắc tên ta. Chỉ là... đừng để cô ấy khó khăn quá."</p>

<p>Minh Nguyệt mỉm cười — nụ cười nhỏ mà cô cố giấu đi.</p>

<p>— "Thiếu gia vẫn còn tốt đấy."</p>

<p>— "Đừng nói với ai." Hắn khẽ cười. Lần đầu tiên — nụ cười không phải vì thắng, không phải để vả mặt ai, không phải để trấn an người khác. Chỉ là nụ cười của một người đang nhìn mặt trời mọc và thấy ổn.</p>

<p>Ánh nắng đầu tiên chạm vào khuôn mặt hắn. Hắn nhắm mắt lại một giây, để nó ấm.</p>

<p>Ba năm trước, một người thanh niên bước ra trong mưa, không có gì cả, và cả thành phố quay lưng lại.</p>

<p>Hôm nay, người đàn ông đó đứng ở đây — không phải để chứng minh điều gì với ai. Chỉ đơn giản là đứng thẳng, trên mảnh đất này, dưới ánh nắng này, và thở.</p>

<p>Vương lão từng nói: <em>"Thành công thật sự không phải là lúc mày giàu nhất. Mà là lúc mày ngủ được ngon, mày nhìn vào gương không thấy mình xấu hổ, và mày ăn cơm thấy ngon."</em></p>

<p>Lâm Phong đứng dưới bình minh, nghĩ đến câu đó, và thấy mình đang tiến gần đến điều đó.</p>

<p>Chỉ cần thêm một chút thời gian thôi.</p>

<p style="text-align:center; margin-top: 40px;">—— <strong>HẾT</strong> ——</p>

<p style="text-align:center;"><em>"Đồ Phế Vật Năm Đó, Hôm Nay Ta Trở Về" — Phiên bản nâng cấp.</em></p>
<p style="text-align:center;"><em>Cảm ơn bạn đã đọc. Nếu thích, hãy để lại yêu thích và chia sẻ nhé!</em></p>"""
    }
]

# ======================================================
# EXECUTION
# ======================================================

print("=== Cập nhật mô tả truyện ===")
res_truyen = bypass("POST", f"truyen/{TRUYEN_ID}", {"content": NEW_INTRO})
print(f"Truyen update: {res_truyen.status_code}")

print("\n=== Lấy danh sách chương hiện tại ===")
# Get all chapters for this story
res_chaps = bypass("GET", f"chuong?meta_key=_truyen_id&meta_value={TRUYEN_ID}&per_page=20", {})
print(f"Get chapters: {res_chaps.status_code}")

if res_chaps.status_code == 200:
    existing_chapters = res_chaps.json()
    print(f"Tìm thấy {len(existing_chapters)} chương")
    
    # Build slug -> id map
    slug_to_id = {}
    for ch in existing_chapters:
        slug_to_id[ch['slug']] = ch['id']
    print(f"Slug map: {slug_to_id}")
    
    print("\n=== Cập nhật từng chương ===")
    for chap_data in chapters_updated:
        slug = chap_data['slug']
        if slug in slug_to_id:
            chap_id = slug_to_id[slug]
            print(f"Cập nhật: {chap_data['title']} (ID: {chap_id})")
            res_update = bypass("POST", f"chuong/{chap_id}", {
                "title": chap_data["title"],
                "content": chap_data["content"]
            })
            print(f"  -> {res_update.status_code}")
            if res_update.status_code not in [200, 201]:
                print(f"  LỖI: {res_update.text[:300]}")
        else:
            print(f"Không tìm thấy slug '{slug}', tạo mới...")
            res_new = bypass("POST", "chuong", {
                "title": chap_data["title"],
                "content": chap_data["content"],
                "status": "publish",
                "meta": {"_truyen_id": TRUYEN_ID}
            })
            print(f"  -> {res_new.status_code} {res_new.json().get('link','')}")
        time.sleep(1)
else:
    print(f"LỖI lấy chapters: {res_chaps.text[:300]}")

print("\n=== HOÀN TẤT ===")
print(f"Link truyện: https://doctieuthuyet.com/truyen/do-phe-vat-nam-do-hom-nay-ta-tro-ve/")
