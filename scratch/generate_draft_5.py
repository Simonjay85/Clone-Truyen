import json
import re

# We will define a python script that will construct the novel draft.
# Let's ensure it has exactly 5 chapters, and each chapter has >= 1000 words.
# We will use precise Vietnamese medical terminology and intense dramatic sảng văn style.
# Each sentence will be split and wrapped in a separate <p>...</p>\n.

# Let's write down the chapters as raw text first, then process it to ensure the <p> formatting.

title = "Giám Đốc Bệnh Viện Sa Thải Bác Sĩ Thực Tập, Hội Đồng Y Tế Quốc Gia Cử Người Điều Tra"
subtitle = "Cuộc chiến học thuật và pháp lý đỉnh cao quét sạch bóng tối ngành y"
author = "Antigravity"
genre = "Sảng Văn"
cover_prompt = "masterpiece, highly detailed book cover, anime illustration style, modern Vietnamese luxury hospital interior, cinematic lighting, a handsome 30-year-old male doctor in a white coat looking determined, beside a sharp 28-year-old female inspector holding a leather folder, in the background a defeated middle-aged director under bright surgical lights, 4k"

# Let's outline the text for Chapter 1
ch1_text = """Tiếng máy thở bíp bíp đơn điệu vang lên trong phòng hồi sức tích cực ICU của Bệnh viện Đa khoa Quốc tế Thành Tâm.
Phạm Quốc Bảo đứng tựa lưng vào tấm kính cường lực ngăn cách, mắt không rời khỏi màn hình theo dõi chỉ số sinh tồn của bệnh nhân Nguyễn Văn Nam.
Lồng ngực của người đàn ông trung niên, một tài xế xe ôm công nghệ nghèo khổ, đang phập phồng yếu ớt dưới lớp băng gạc trắng toát.
Bảo cúi xuống nhìn tập bệnh án dày cộm trên tay, ngón tay anh bóp chặt đến mức các khớp xương chuyển sang màu trắng bệch.
Bản chụp mạch vành và siêu âm tim Doppler hiển thị một lỗ rò động mạch chủ cực kỳ nghiêm trọng, cần phải phẫu thuật thay van tim khẩn cấp.
Nhưng trên tờ chỉ định phẫu thuật vừa được gửi xuống từ văn phòng Giám đốc, loại van tim được phê duyệt lại là dòng van sinh học Bio-Val thế hệ cũ.
Đây là loại van đã bị Hội đồng Y khoa Quốc gia cảnh báo về nguy cơ xơ hóa sớm và gây huyết khối ở bệnh nhân dưới năm mươi tuổi từ hai năm trước.
Mức giá nhập khẩu thực tế của nó chỉ chưa đầy mười lăm triệu đồng, nhưng trên hóa đơn thanh toán bảo hiểm y tế của bệnh nhân, con số đã được khống chế lên tới một trăm hai mươi triệu đồng.
Một tiếng bước chân dồn dập kèm theo mùi nước hoa đắt tiền cắt ngang dòng suy nghĩ của Bảo.
Phó Giáo sư, Tiến sĩ Nguyễn Hữu Hoài, Giám đốc Bệnh viện Quốc tế Thành Tâm, bước vào với chiếc áo blouse lụa phẳng phiu không một nếp nhăn.
Đi sau hắn là ba bác sĩ trưởng khoa cùng hai nhân viên bảo vệ vạm vỡ của bệnh viện.
Nguyễn Hữu Hoài nheo mắt nhìn Bảo, giọng nói khinh khỉnh vang lên trong không gian yên tĩnh của hành lang ICU.
Cậu thực tập sinh Phạm Quốc Bảo, tại sao ca mổ của bệnh nhân Nguyễn Văn Nam vẫn chưa được chuẩn bị?
Tôi đã ký lệnh phẫu thuật từ hai tiếng trước, tại sao cậu dám giữ lại tập hồ sơ bệnh án này?
Bảo ngẩng đầu lên, ánh mắt bình thản nhưng lạnh lùng đối diện thẳng với vị Giám đốc đầy quyền uy.
Thưa Giám đốc Hoài, tôi giữ lại hồ sơ vì loại van sinh học Bio-Val được chỉ định không phù hợp với thể trạng của bệnh nhân Nam.
Bệnh nhân mới bốn mươi hai tuổi, việc sử dụng van Bio-Val thế hệ cũ sẽ khiến ông ấy đối mặt với nguy cơ suy van tim cấp tính trong vòng ba năm tới.
Hơn nữa, mức giá một trăm hai mươi triệu đồng ghi trên hóa đơn là hành vi khống giá thiết bị y tế trắng trợn.
Là một bác sĩ điều trị, tôi không thể ký tên vào biên bản đồng ý phẫu thuật với danh mục vật tư nguy hại này.
Nguyễn Hữu Hoài nghe xong, gương mặt đầy thịt của hắn co giật mạnh, mồ hôi lạnh khẽ rịn ra trên trán nhưng nhanh chóng bị thay thế bằng vẻ giận dữ tột cùng.
Hắn bước lên một bước, chỉ thẳng ngón tay đeo chiếc nhẫn kim cương lớn vào mặt Bảo.
Cậu câm miệng lại cho tôi!
Cậu tưởng mình là ai? Một tên thực tập sinh quèn không có gốc gác, vừa tốt nghiệp đại học y tế địa phương mà dám lên mặt dạy đời tôi sao?
Bệnh viện Quốc tế Thành Tâm này là địa bàn của tôi, từng viên thuốc, từng cái kim tiêm đều do tôi quyết định!
Tên xe ôm kia không có tiền trả viện phí, bệnh viện đã nhân từ cho ông ta nợ để mổ, dùng van Bio-Val là đặc ân lớn nhất rồi!
Cậu dám nói về giá cả và chất lượng ở đây sao? Cậu có biết một năm tôi phải chi bao nhiêu tiền để duy trì cái bệnh viện năm sao này không?
Bảo không hề lùi bước, giọng nói của anh vẫn đều đặn, rành mạch từng chữ như một phán quyết.
Y đức không cho phép chúng ta lừa dối bệnh nhân, thưa Giám đốc.
Nếu ca mổ này diễn ra với loại van đó, bệnh nhân có thể chết ngay trên bàn mổ do hẹp khít van nhân tạo cấp tính.
Tôi đề nghị thay thế bằng dòng van cơ học dòng Edwards Sapien được nhập khẩu chính ngạch theo đúng tiêu chuẩn của Bộ Y tế.
Nguyễn Hữu Hoài cười lớn, tiếng cười tràn đầy sự mỉa mai và khinh bỉ tột độ.
Edwards Sapien? Cậu nằm mơ à? Loại van đó giá gốc bao nhiêu cậu có biết không?
Một kẻ nghèo kiết xác như ông ta lấy gì để trả tiền cho loại vật tư xa xỉ đó?
Còn cậu, Phạm Quốc Bảo, sự kiên nhẫn của tôi đã hết hạn rồi.
Tôi tuyển cậu vào đây làm thực tập sinh là để cậu học cách phục tùng, chứ không phải để cậu làm anh hùng cứu thế.
Kể từ giây phút này, cậu chính thức bị sa thải khỏi Bệnh viện Đa khoa Quốc tế Thành Tâm!
Thẻ nhân viên của cậu sẽ bị thu hồi ngay lập tức, toàn bộ hồ sơ thực tập của cậu sẽ bị xóa sạch trên hệ thống dữ liệu y khoa toàn quốc!
Tôi sẽ đích thân ký công văn gửi đến tất cả các bệnh viện tại Việt Nam để đảm bảo không một nơi nào dám nhận một tên bác sĩ phản loạn như cậu!
Bảo nhìn chiếc thẻ nhân viên treo trên cổ mình, khẽ mỉm cười một cách đầy ẩn ý.
Anh tháo chiếc thẻ ra, đặt nhẹ nhàng lên mặt bàn trực của y tá.
Nếu ông đã quyết định như vậy, tôi hy vọng ông sẽ không hối hận về quyết định ngày hôm nay, Giám đốc Hoài.
Nguyễn Hữu Hoài vẫy tay ra lệnh cho hai nhân viên bảo vệ đứng phía sau.
Trục xuất gã này ra khỏi khuôn viên bệnh viện ngay lập tức!
Đồ đạc cá nhân của nó, gom hết lại rồi ném ra ngoài đường cho tôi!
Bệnh viện Thành Tâm không chứa chấp những kẻ ăn cháo đá bát, không biết điều như thế này!
Hai gã bảo vệ vạm vỡ lập tức bước tới, một gã thô bạo giật lấy tập tài liệu trên tay Bảo, gã còn lại đẩy mạnh vai anh hướng về phía cửa thoát hiểm.
Mồ hôi lạnh chảy sau gáy tên trưởng khoa đứng cạnh Hoài, gã biết Bảo là một bác sĩ có năng lực chuyên môn cực kỳ xuất sắc.
Nhưng trước quyền lực tuyệt đối của Nguyễn Hữu Hoài, không một ai dám ho he nửa lời.
Trời sập tối, những hạt mưa nặng hạt bắt đầu trút xuống đại lộ Nguyễn Văn Linh, Quận 7.
Bảo bị đẩy ra khỏi cánh cửa kính sang trọng của bệnh viện, chiếc balo cũ kỹ bị ném thẳng xuống nền xi măng ẩm ướt vang lên một tiếng cộp nặng nề.
Nước mưa nhanh chóng thấm đẫm vai áo sơ mi trắng của anh, lạnh buốt.
Nhưng ánh mắt của Phạm Quốc Bảo không hề có một chút thất vọng hay sợ hãi nào.
Anh nhặt chiếc balo lên, phủi nhẹ lớp nước mưa bám bên ngoài, rồi lấy từ trong túi quần ra một chiếc điện thoại chuyên dụng màu đen.
Anh nhấn một dãy số khẩn cấp được mã hóa hai chiều.
Đầu dây bên kia nhanh chóng bắt máy, một giọng nữ thanh tao nhưng tràn đầy sự nghiêm nghị vang lên.
Tiến sĩ Bảo, cuộc khảo sát thực địa của anh tại Bệnh viện Thành Tâm đã hoàn tất chưa?
Bảo nhìn ngược lên tòa nhà hai mươi tầng sáng ánh đèn LED rực rỡ của bệnh viện, khóe môi khẽ cong lên.
Hoàn tất rồi, Nguyễn Khánh Vy.
Giám đốc bệnh viện vừa sa thải tôi vì tôi từ chối ký biên bản sử dụng van tim sinh học kém chất lượng.
Hồ sơ trục lợi bảo hiểm và danh sách các ca mổ chui sử dụng vật tư y tế lậu tôi đã gửi vào máy chủ đám mây của Hội đồng Y khoa Quốc gia.
Có thể kích hoạt chiến dịch thanh tra đặc biệt được rồi đấy.
Nguyễn Khánh Vy ở đầu dây bên kia khẽ thở dài, nhưng trong giọng nói lại có một sự phấn khích không thể che giấu.
Rất tốt, tôi đã chuẩn bị sẵn sàng toàn bộ lực lượng điều tra lâm sàng và pháp lý.
Hội đồng Y tế Quốc gia và Bộ Công an đã phê duyệt mật lệnh số 05.
Sáng mai, tôi sẽ đích thân dẫn đoàn thanh tra đến tiếp quản và phong tỏa bệnh viện đó.
Anh cứ nghỉ ngơi đi, ngày mai sẽ là một trận chiến rất lớn đấy, bác sĩ Bảo.
Bảo cúp điện thoại, bước đi dưới màn mưa giông của Sài Gòn, bóng lưng cô độc nhưng vững chãi như một bức tường thành không thể lay chuyển.
"""

# Let's outline the text for Chapter 2
ch2_text = """Sáng sớm hôm sau, tại phòng làm việc tầng cao nhất của tòa tháp tài chính Vietcombank Tower quận 1.
Nguyễn Khánh Vy ngồi tựa lưng vào chiếc ghế da cao cấp, ngón tay thanh mảnh gõ nhẹ lên mặt bàn gỗ gụ nhập khẩu từ Ý.
Trước mặt cô là Phạm Quốc Bảo, lúc này đã thay bộ quần áo ướt sũng tối qua bằng một bộ comple màu xanh đen may đo thủ công cực kỳ lịch lãm.
Khánh Vy, hai mươi tám tuổi, là Trưởng ban Giám sát Pháp lý kiêm Ủy viên Đặc biệt của Hội đồng Y khoa Quốc gia.
Cô đồng thời là con gái lớn của Chủ tịch Tập đoàn Y tế Vạn An - đế chế sở hữu chuỗi bệnh viện tư nhân lớn nhất Việt Nam.
Khánh Vy đẩy một tập tài liệu bọc da màu đỏ về phía Bảo, đôi mắt sắc sảo của cô nhìn thẳng vào anh.
Đây là bản hợp đồng ủy quyền chuyên gia cố vấn độc lập của Hội đồng Y tế Quốc gia dành riêng cho anh, Tiến sĩ Bảo.
Tôi muốn làm rõ một điều trước khi chúng ta chính thức ký kết và xuất quân vào sáng nay.
Mục tiêu của tập đoàn Vạn An là thâu tóm toàn bộ sáu mươi lăm phần trăm cổ phần của Bệnh viện Quốc tế Thành Tâm sau khi đường dây của Nguyễn Hữu Hoài bị triệt hạ.
Chúng tôi cần một Giám đốc điều hành y khoa có năng lực chuyên môn tuyệt đối để tái cấu trúc lại toàn bộ hệ thống lâm sàng của bệnh viện đó.
Và người đó bắt buộc phải là anh.
Bảo cầm cây bút máy lên, nhưng anh không đặt bút ký ngay mà khẽ gõ nhẹ đầu bút xuống mặt bàn.
Tôi có thể nhận lời làm Giám đốc điều hành y khoa cho Vạn An, nhưng tôi có hai điều kiện sòng phẳng cần cô cam kết bằng văn bản pháp lý.
Thứ nhất, toàn bộ các bệnh nhân nghèo đã bị Nguyễn Hữu Hoài lừa dối cấy ghép van tim kém chất lượng phải được phẫu thuật thay thế miễn phí bằng vật tư đạt chuẩn.
Chi phí này sẽ được khấu trừ trực tiếp vào tài sản tịch thu từ Nguyễn Hữu Hoài và nguồn quỹ phúc lợi của tập đoàn Vạn An sau khi thâu tóm.
Thứ hai, tôi có toàn quyền quyết định về nhân sự lâm sàng và tiêu chuẩn kỹ thuật điều trị mà không có bất kỳ sự can thiệp nào từ hội đồng quản trị của tập đoàn cô.
Tôi làm việc để cứu người và khôi phục lại công lý cho ngành y, chứ không phải để làm công cụ tối đa hóa lợi nhuận cho các cổ đông của Vạn An.
Khánh Vy hơi ngạc nhiên trước thái độ sòng phẳng và kiên định của vị bác sĩ trẻ trước mặt.
Hầu hết các bác sĩ khác khi đứng trước lời mời của tập đoàn Vạn An đều sẽ cúi đầu cung kính, nhưng Bảo lại đặt điều kiện ngược lại với cô một cách đầy đanh thép.
Một nụ cười tán thưởng xuất hiện trên môi cô, Khánh Vy nghiêng người ký thẳng vào văn bản bổ sung điều khoản đặc biệt rồi đẩy lại cho anh.
Thỏa thuận thành lập, tôi thích phong cách làm việc rõ ràng và đặt lợi ích chuyên môn lên hàng đầu của anh.
Bản cam kết này có đầy đủ chữ ký của tôi và con dấu đỏ của Hội đồng quản trị Tập đoàn Vạn An.
Kể từ bây giờ, anh là Cố vấn trưởng của Đoàn thanh tra đặc biệt liên ngành.
Hồ sơ mà anh gửi tối qua đã được chuyển thẳng tới Cục Cảnh sát điều tra tội phạm về tham nhũng, kinh tế, buôn lậu C03 của Bộ Công an.
Chúng tôi đã xác định được đường dây của Nguyễn Hữu Hoài không chỉ đơn thuần là nâng khống giá van tim sinh học.
Hắn còn nhập khẩu trái phép hàng loạt máy chụp cắt lớp vi tính CT-Scanner và hệ thống chụp cộng hưởng từ MRI đã qua sử dụng từ các bãi rác y tế ở châu Âu.
Những thiết bị này được mông má lại, dán nhãn mới rồi khai khống giá nhập khẩu cao gấp hai mươi lần giá trị thực tế để rút ruột quỹ bảo hiểm y tế quốc gia.
Tổng số tiền trục lợi ước tính đã vượt quá con số năm trăm tỷ đồng.
Bảo đặt bút ký tên mình xuống bản hợp đồng, nét chữ mạnh mẽ và dứt khoát như một nhát dao mổ chuẩn xác.
Được rồi, chúng ta xuất phát thôi.
Tôi muốn xem phản ứng của Nguyễn Hữu Hoài thế nào khi nhìn thấy tôi quay lại bệnh viện với một thân phận hoàn toàn khác.
Cùng lúc đó, tại Bệnh viện Đa khoa Quốc tế Thành Tâm, không khí buổi sáng diễn ra vô cùng náo nhiệt.
Nguyễn Hữu Hoài đang đứng ở sảnh lớn bệnh viện, gương mặt hớn hở chỉ đạo nhân viên trải thảm đỏ và cắm hoa tươi dọc theo lối đi chính.
Hôm nay là ngày bệnh viện đón tiếp đoàn kiểm tra định kỳ của Sở Y tế và các nhà đầu tư lớn từ Singapore đến khảo sát để chuẩn bị cho kế hoạch phát hành cổ phiếu lần đầu ra công chúng IPO.
Hoài liên tục nhắc nhở các trưởng khoa phải che giấu kỹ các ca tai nạn biến chứng y khoa trong tháng qua, tuyệt đối không được để lộ bất kỳ thông tin nào ra ngoài.
Hắn vuốt lại mái tóc bóng mượt, quay sang nói với gã trưởng khoa tim mạch đứng bên cạnh.
Tên thực tập sinh Phạm Quốc Bảo tối qua đã dọn sạch đồ đạc biến khỏi đây chưa?
Trưởng khoa cúi đầu, vội vàng đáp lời với vẻ khúm núm.
Dạ thưa Giám đốc, bảo vệ đã đuổi nó đi ngay trong đêm mưa hôm qua rồi ạ.
Hồ sơ thực tập của nó cũng đã bị chúng em xóa hoàn toàn khỏi hệ thống lưu trữ nội bộ của bệnh viện.
Nguyễn Hữu Hoài hừ lạnh một tiếng, ánh mắt lộ rõ vẻ tàn nhẫn.
Tốt lắm, loại kiến cỏ đó mà cũng đòi đấu với tôi.
Hôm nay sau khi đón tiếp đoàn kiểm tra và ký kết hợp tác với đối tác Singapore, danh tiếng của bệnh viện Thành Tâm sẽ tăng lên một tầm cao mới.
Cổ phần của tôi sẽ trị giá hàng trăm tỷ đồng, không ai có thể lay chuyển được vị trí của tôi ở thành phố này!
Đúng lúc đó, tiếng còi xe cảnh sát rú vang dồn dập từ phía cổng chính của bệnh viện.
Ba chiếc xe chuyên dụng màu xanh của Bộ Công an cùng bốn chiếc xe limousine màu đen sang trọng của Hội đồng Y khoa Quốc gia đồng loạt tiến vào, đỗ ngay trước thảm đỏ của sảnh lớn.
Gương mặt Nguyễn Hữu Hoài bỗng chốc cứng đờ, nụ cười trên môi hắn vụt tắt.
Hắn ngơ ngác nhìn những người bước xuống từ xe, không phải là đoàn kiểm tra thông thường của Sở Y tế, mà là những nhân vật quyền lực nhất của ngành y tế quốc gia cùng các chiến sĩ cảnh sát kinh tế đeo sắc phục nghiêm chỉnh.
"""

# Let's outline the text for Chapter 3
ch3_text = """Cánh cửa xe limousine mở ra, Nguyễn Khánh Vy bước xuống với phong thái đầy quyền lực của một nữ thanh tra cấp cao.
Theo sau cô là mười chuyên gia đầu ngành y khoa của Hội đồng Y khoa Quốc gia và các kiểm toán viên cao cấp của Nhà nước.
Nguyễn Hữu Hoài vội vàng nuốt nước bọt, cố gắng lấy lại vẻ tự tin rồi rảo bước nhanh tới đón tiếp, hai tay chìa ra run rẩy.
Chào Ủy viên đặc biệt Nguyễn Khánh Vy!
Thật là vinh hạnh lớn cho Bệnh viện Quốc tế Thành Tâm khi được đích thân cô và phái đoàn của Hội đồng ghé thăm đột xuất.
Bệnh viện chúng tôi luôn chấp hành nghiêm chỉnh mọi quy định chuyên môn và pháp luật của Nhà nước.
Khánh Vy không hề chìa tay ra đáp lễ, cô lạnh lùng lướt qua Hoài, đứng ngay giữa sảnh lớn bệnh viện trước sự chứng kiến của hàng trăm y bác sĩ và bệnh nhân.
Giọng nói trong trẻo nhưng đầy uy lực của cô vang lên qua hệ thống loa cầm tay của đoàn thanh tra.
Phó Giáo sư, Tiến sĩ Nguyễn Hữu Hoài, chúng tôi đến đây không phải để ghé thăm hay khảo sát đầu tư.
Thay mặt Hội đồng Y tế Quốc gia và Bộ Y tế, tôi chính thức công bố quyết định thanh tra đặc biệt toàn diện đối với Bệnh viện Đa khoa Quốc tế Thành Tâm.
Nội dung thanh tra bao gồm toàn bộ hoạt động đấu thầu vật tư y tế, quy trình phẫu thuật lâm sàng, và việc sử dụng quỹ bảo hiểm y tế trong ba năm gần đây.
Yêu cầu ông lập tức ra lệnh cho phòng công nghệ thông tin mở khóa toàn bộ hệ thống máy chủ dữ liệu bệnh án và sổ sách kế toán để chúng tôi niêm phong kiểm toán.
Nguyễn Hữu Hoài nghe xong, gối hắn quỳ xuống đất cộp một tiếng do mất đà vì quá hoảng hốt, nhưng hắn nhanh chóng dùng tay gượng dậy, gương mặt tái mét cắt không còn giọt máu.
Hắn cố gắng chống chế, giọng nói bắt đầu run rẩy lộ rõ vẻ lo sợ.
Thưa cô Khánh Vy, chuyện này... chuyện này có sự hiểu lầm nào đó rồi!
Bệnh viện chúng tôi là bệnh viện tư nhân tiêu chuẩn năm sao quốc tế, mọi quy trình đều được kiểm toán độc lập hàng năm.
Hội đồng không thể chỉ dựa vào một vài tin đồn thất thiệt mà tiến hành thanh tra đột xuất làm ảnh hưởng đến uy tín và việc điều trị của hàng ngàn bệnh nhân ở đây được!
Nếu không có chứng cứ kỹ thuật cụ thể chứng minh chúng tôi có sai phạm, tôi buộc phải liên hệ với các cấp lãnh đạo cao hơn để khiếu nại về hành vi lạm quyền này của cô!
Khánh Vy khẽ nhếch môi, ánh mắt lộ rõ sự khinh bỉ trước sự ngoan cố của tên cáo già.
Ông muốn chứng cứ kỹ thuật cụ thể sao, Giám đốc Hoài?
Được thôi, tôi đã chuẩn bị sẵn sàng một cố vấn chuyên môn đặc biệt có thẩm quyền tối cao để chỉ ra từng sai phạm kỹ thuật của ông.
Khánh Vy quay đầu lại phía chiếc xe thứ hai, giọng nói của cô đầy trang trọng.
Mời Cố vấn trưởng Phạm Quốc Bảo bước xuống!
Cửa xe mở ra, Phạm Quốc Bảo bước xuống trong sự ngỡ ngàng tột độ của toàn bộ nhân viên y tế Bệnh viện Thành Tâm đang có mặt tại sảnh lớn.
Hàng chục bác sĩ trưởng khoa mắt trợn ngược, miệng há hốc không tin vào mắt mình.
Nguyễn Hữu Hoài lùi lại ba bước, ngón tay chỉ thẳng vào Bảo, lắp bắp kinh hoàng.
Cậu... cậu... Phạm Quốc Bảo?
Tại sao tên thực tập sinh quèn bị tôi sa thải tối qua lại ở trên chiếc xe đó?
Cậu ta chỉ là một tên lừa đảo mạo danh! Cô Khánh Vy, cô đã bị gã này lừa gạt rồi!
Nó chỉ là một đứa thực tập sinh chưa có chứng chỉ hành nghề y khoa độc lập, làm sao có tư cách làm cố vấn cho Hội đồng Quốc gia được?
Bảo bước tới trước mặt Nguyễn Hữu Hoài, ánh mắt anh sắc lạnh như một mũi dao mổ, khí thế áp đảo hoàn toàn vị Giám đốc ngạo mạn tối qua.
Anh từ tốn lấy từ trong túi áo blouse ra một chiếc huy hiệu bằng vàng nguyên chất của Hội đồng Y khoa Quốc gia cùng tấm thẻ công tác đặc biệt màu đỏ.
Nguyễn Hữu Hoài, ông nhầm rồi.
Tôi tốt nghiệp thủ khoa Đại học Y Harvard, là Tiến sĩ Y khoa trẻ tuổi nhất được phong hàm Giáo sư lâm sàng danh dự tại Viện Tim mạch Quốc gia Hoa Kỳ.
Hai năm trước, tôi được Bộ Sức khỏe Quốc dân bổ nhiệm làm Ủy viên khoa học cấp cao của Hội đồng Y tế Quốc gia Việt Nam.
Tôi ẩn danh làm thực tập sinh tại bệnh viện của ông trong ba tháng qua theo mật lệnh điều tra đặc biệt từ Bộ trưởng.
Mục đích là để trực tiếp thu thập toàn bộ chứng cứ về đường dây mổ chui và hành vi trục lợi bảo hiểm y tế mà ông cùng đồng bọn đang thực hiện.
Lời nói của Bảo như một tiếng sét giữa trời quang, đánh thẳng vào đầu Nguyễn Hữu Hoài khiến hắn lảo đảo đứng không vững.
Mồ hôi lạnh chảy ròng ròng sau gáy tên trưởng khoa tim mạch đứng cạnh Hoài, gã biết lần này bầu trời của bệnh viện Thành Tâm thực sự đã sụp đổ.
Bảo quay sang nhìn thẳng vào đoàn thanh tra, giọng nói của anh vang lên đầy đanh thép.
Đoàn thanh tra chia làm ba mũi cho tôi!
Mũi thứ nhất lập tức tiến vào phòng máy chủ công nghệ thông tin, thu giữ toàn bộ nhật ký chỉnh sửa bệnh án của khoa Tim mạch và khoa Ngoại tổng hợp.
Mũi thứ hai di chuyển xuống kho dược phẩm và vật tư y tế, niêm phong toàn bộ lô van tim sinh học dòng Bio-Val thế hệ cũ không rõ nguồn gốc xuất xứ.
Mũi thứ ba phong tỏa phòng tài chính kế toán, đối chiếu toàn bộ hóa đơn nhập khẩu thiết bị y tế CT-Scanner và MRI với tờ khai hải quan thực tế.
Chúng ta sẽ tiến hành đối chất lâm sàng trực tiếp với Ban giám đốc bệnh viện ngay tại phòng hội thảo khoa học ở tầng năm!
Hội đồng Y khoa sẽ chứng minh cho ông thấy, thế nào là chứng cứ kỹ thuật không thể chối cãi, Nguyễn Hữu Hoài!
"""

# Let's outline the text for Chapter 4
ch4_text = """Phòng hội thảo khoa học tầng năm của Bệnh viện Quốc tế Thành Tâm chật kín người.
Ánh đèn neon trắng lạnh chiếu xuống chiếc bàn tròn lớn, nơi hai bên chiến tuyến đang chuẩn bị cho một cuộc đối đầu học thuật và pháp lý sinh tử.
Một bên là Nguyễn Hữu Hoài cùng dàn giáo sư, trưởng khoa bù nhìn được hắn dùng tiền mua chuộc để làm tấm lá chắn học thuật.
Bên kia là Phạm Quốc Bảo, Nguyễn Khánh Vy cùng các chuyên gia đầu ngành hàng đầu Việt Nam về tim mạch và thiết bị y tế.
Nguyễn Hữu Hoài lúc này đã lấy lại được chút bình tĩnh, hắn dựa lưng vào ghế, cố gắng dùng danh tiếng học hàm Phó Giáo sư của mình để gây sức ép.
Hắn đập tay xuống bàn, giọng nói oang oang đầy tính đe dọa.
Tiến sĩ Bảo, cậu đừng có dùng cái danh hiệu Harvard để dọa nạt những người làm chuyên môn lâu năm như chúng tôi ở đây!
Y học lâm sàng tại Việt Nam có những đặc thù riêng biệt mà một kẻ học ở nước ngoài như cậu không thể hiểu hết được!
Việc chúng tôi sử dụng van sinh học Bio-Val cho bệnh nhân Nguyễn Văn Nam và các bệnh nhân khác là dựa trên chỉ định lâm sàng cụ thể và tình trạng kinh tế của họ!
Y văn thế giới chưa bao giờ cấm tuyệt đối việc sử dụng van Bio-Val cho bệnh nhân trung niên!
Cậu lấy tư cách gì để khẳng định loại van này gây nguy hiểm và là hành vi nâng khống giá trục lợi?
Bảo không hề tức giận, anh thong thả mở chiếc laptop chuyên dụng của mình, kết nối trực tiếp với máy chiếu lớn của phòng hội thảo.
Trên màn hình lớn lập tức xuất hiện hàng chục biểu đồ động học huyết động và hình ảnh siêu âm tim Doppler màu cắt lớp của năm bệnh nhân đã được phẫu thuật thay van tim tại bệnh viện Thành Tâm trong hai tháng qua.
Bảo đứng dậy, cầm chiếc bút chỉ laser màu đỏ, chỉ thẳng vào vùng xoáy màu xanh đỏ hỗn loạn trên hình ảnh siêu âm của bệnh nhân Trần Văn Bình.
Đây là hình ảnh siêu âm tim của bệnh nhân Trần Văn Bình, ba mươi tám tuổi, được phẫu thuật thay van Bio-Val cách đây đúng bốn mươi lăm ngày do chính ông trực tiếp làm phẫu thuật viên chính.
Hãy nhìn vào chỉ số diện tích mở van hiệu dụng EOA này đi, thưa Phó Giáo sư Hoài.
Chỉ số EOA của bệnh nhân chỉ đạt không phẩy tám xăng-ti-mét vuông, tương đương với tình trạng hẹp van tim mức độ nặng.
Lý do là gì? Là do lô van Bio-Val mà ông nhập khẩu thực chất là hàng tồn kho lỗi kỹ thuật từ một nhà sản xuất Trung Quốc bị cấm lưu hành tại thị trường nội địa của họ.
Độ dày của các lá van sinh học này không đồng đều, dẫn đến hiện tượng xơ hóa và vôi hóa sớm ngay sau khi cấy ghép vào cơ thể người bệnh.
Áp lực động mạch chủ phổi của bệnh nhân Bình hiện đã tăng lên mức sáu mươi lăm mi-li-mét thủy ngân, bệnh nhân liên tục bị khó thở cấp tính và đối mặt với nguy cơ tử vong do suy tim phải bất cứ lúc nào!
Bảo tiếp tục chuyển sang slide tiếp theo, hiển thị bản phân tích hóa học cấu trúc mô của van tim sinh học.
Hơn nữa, đây là kết quả phân tích phổ hồng ngoại Fourier FTIR đối với mẫu van Bio-Val lấy từ kho vật tư của ông do Viện Kiểm nghiệm Trang thiết bị Y tế Quốc gia thực hiện khẩn cấp sáng nay.
Hàm lượng glutaraldehyde dùng để xử lý mô động vật trên các lá van này vượt quá tiêu chuẩn cho phép gấp năm lần, gây ra độc tính tế bào cực kỳ nghiêm trọng đối với nội mạc mạch máu của bệnh nhân.
Đây không phải là chỉ định lâm sàng dựa trên thể trạng bệnh nhân, đây là hành vi giết người gián tiếp để ăn chia chênh lệch giá!
Tiếng xầm xì kinh hoàng vang lên khắp phòng họp, các trưởng khoa cúi gầm mặt xuống bàn, không một ai dám lên tiếng phản bác trước những luận điểm học thuật vô cùng sắc bén và những con số kỹ thuật chính xác đến từng chữ số thập phân của Bảo.
Nguyễn Hữu Hoài mặt mũi đỏ gay, trán lấm tấm mồ hôi, hắn gào lên trong sự bất lực và giận dữ tột cùng.
Cậu... cậu vu khống! Đây chỉ là những biến chứng y khoa ngẫu nhiên nằm trong tỷ lệ cho phép của y văn!
Không một ca mổ tim nào là an toàn một trăm phần trăm cả!
Còn về mức giá một trăm hai mươi triệu đồng, đó là chi phí bao gồm cả kỹ thuật mổ cao, chăm sóc hậu phẫu năm sao và khấu hao thiết bị y tế hiện đại của bệnh viện tư nhân!
Chúng tôi hoàn toàn làm đúng quy định của Luật Giá và các thông tư hướng dẫn của Bộ Tài chính!
Khánh Vy đứng dậy, cô mở tập hồ sơ pháp lý màu xanh, ném thẳng xuống trước mặt Nguyễn Hữu Hoài.
Ông Hoài, ông đừng có lôi Luật Giá ra để ngụy biện cho hành vi phạm pháp của mình.
Đây là bản sao kê tài khoản ngân hàng của ông tại ngân hàng Vietcombank và Techcombank, cùng với hồ sơ chuyển tiền của công ty sân sau do vợ ông đứng tên có trụ sở tại Singapore.
Trong ba năm qua, công ty này đã chuyển hơn ba triệu đô la Mỹ, tương đương với hơn bảy mươi tỷ đồng dưới dạng 'phí tư vấn kỹ thuật' vào tài khoản cá nhân của ông.
Nguồn tiền này thực chất là tiền hoàn trả chênh lệch kickback từ nhà cung cấp thiết bị y tế cũ nát mà ông đã nhập khẩu để trang bị cho bệnh viện Thành Tâm.
Chúng tôi cũng đã có trong tay biên bản làm việc chính thức với Tổng cục Hải quan Việt Nam.
Chiếc máy chụp MRI ba chấm không Tesla mà ông khai báo nhập khẩu mới một trăm phần trăm với giá một trăm hai mươi tỷ đồng, thực chất được mua lại từ một bệnh viện thanh lý ở Đức với giá phế liệu chỉ có bốn tỷ đồng!
Toàn bộ hồ sơ kỹ thuật, số seri máy gốc và lịch sử bảo dưỡng tại Đức đã được cảnh sát quốc tế Interpol cung cấp đầy đủ cho chúng tôi.
Ông còn gì để chối cãi nữa không, Phó Giáo sư Nguyễn Hữu Hoài?
Nguyễn Hữu Hoài nghe đến đây, toàn thân hắn bỗng chốc rũ rượi, ngón tay hắn bấm rỉ máu vào cạnh bàn gỗ gụ, đôi mắt hiện rõ sự tuyệt vọng và điên cuồng của một kẻ sắp mất đi tất cả.
"""

# Let's outline the text for Chapter 5
ch5_text = """Không gian phòng họp im lặng đến mức có thể nghe thấy cả tiếng thở gấp gáp đầy hoảng loạn của Nguyễn Hữu Hoài.
Hắn nhìn chằm chằm vào những tài liệu tài chính và hồ sơ Interpol trước mặt, răng cắn chặt đến mức môi bật máu.
Bỗng nhiên, hắn cười lên một tiếng điên cuồng, ánh mắt lộ rõ vẻ tàn nhẫn và liều lĩnh của một con thú bị dồn vào đường cùng.
Hắn đứng bật dậy, đập mạnh tay xuống bàn, chỉ thẳng vào mặt Khánh Vy và Bảo.
Được rồi! Cứ cho là những gì các người nói là thật đi!
Nhưng các người nghĩ có thể dễ dàng triệt hạ được tôi sao?
Có biết ai là người đứng sau chống lưng cho Bệnh viện Quốc tế Thành Tâm này không?
Thứ trưởng Bộ Y tế phụ trách mảng trang thiết bị chính là chú họ của vợ tôi!
Hội đồng Y khoa Quốc gia của các người chỉ là một cơ quan tư vấn chuyên môn, không có quyền hạn bắt giữ hay đình chỉ hoạt động của một bệnh viện tư nhân nghìn tỷ này!
Chỉ cần một cuộc điện thoại của tôi, toàn bộ đoàn thanh tra của các người sẽ phải rút lui ngay lập tức!
Bảo nhìn sự điên cuồng của Hoài, ánh mắt anh không hề có một chút dao động nào, chỉ có sự thương hại sâu sắc.
Nguyễn Hữu Hoài, ông thực sự nghĩ chú họ của vợ ông hiện tại vẫn còn có thể che chở cho ông sao?
Hãy tự mình nhìn lên màn hình lớn một lần nữa đi.
Bảo nhấn nút chuyển kênh trên điều khiển từ xa, kết nối trực tiếp với sóng truyền hình trực tiếp của Ban Thời sự Đài Truyền hình Việt Nam VTV1 lúc mười một giờ trưa.
Trên màn hình lớn, hình ảnh biên tập viên thời sự đang đọc bản tin đặc biệt với giọng đọc trang nghiêm.
Sáng nay, Cục Cảnh sát điều tra tội phạm về tham nhũng, kinh tế, buôn lậu C03 của Bộ Công an đã phối hợp với Viện Kiểm sát nhân dân tối cao tiến hành khởi tố vụ án, khởi tố bị can và thực hiện lệnh bắt tạm giam đối với ông Nguyễn Văn Đức, Thứ trưởng Bộ Y tế về hành vi lợi dụng chức vụ quyền hạn trong khi thi hành công vụ, liên quan đến đường dây nâng khống giá thiết bị y tế và nhận hối lộ tại hàng loạt bệnh viện lớn.
Đồng thời, cơ quan điều tra cũng đã phát lệnh phong tỏa khẩn cấp toàn bộ tài sản và tài khoản ngân hàng của các đối tượng liên quan, trong đó có Bệnh viện Đa khoa Quốc tế Thành Tâm...
Tiếng tivi vang lên đều đặn trong phòng họp như những nhát búa đóng đinh vào chiếc quan tài danh vọng của Nguyễn Hữu Hoài.
Hắn lảo đảo lùi lại, chiếc ghế da phía sau bị đẩy văng ra, gã quỵ ngã xuống sàn nhà lạnh lẽo, miệng há hốc nhưng không thể phát ra bất kỳ âm thanh nào.
Lá chắn quyền lực lớn nhất của hắn đã sụp đổ hoàn toàn chỉ trong một buổi sáng.
Đúng lúc này, cánh cửa phòng họp bị đẩy mạnh ra.
Một toán chiến sĩ cảnh sát kinh tế C03 cùng đại diện Viện Kiểm sát bước vào, trên tay cầm lệnh bắt giữ có dấu đỏ chót.
Đồng chí Nguyễn Hữu Hoài, ông chính thức bị bắt giữ về tội danh vi phạm quy định về đấu thầu gây hậu quả nghiêm trọng, nhận hối lộ và lừa dối khách hàng theo Bộ luật Hình sự nước Cộng hòa Xã hội Chủ nghĩa Việt Nam.
Yêu cầu ông đứng dậy hợp tác chấp hành lệnh bắt giữ!
Hai chiến sĩ cảnh sát lập tức bước tới, chiếc còng số tám bằng thép lạnh buốt khóa chặt hai cổ tay của vị Giám đốc ngạo mạn ngày nào trước sự chứng kiến của toàn thể nhân viên dưới quyền.
Hoài cúi đầu lầm lũi bị dẫn đi, gương mặt xám ngoét không còn một chút sinh khí.
Sau khi Nguyễn Hữu Hoài bị áp giải đi, Khánh Vy quay sang nhìn các trưởng khoa đang run rẩy đứng nép vào góc tường.
Cô dõng dạc công bố quyết định tiếp theo của Hội đồng quản trị Tập đoàn Vạn An.
Kể từ giờ phút này, Tập đoàn Y tế Vạn An chính thức thâu tóm thành công sáu mươi lăm phần trăm cổ phần và nắm quyền kiểm soát toàn diện Bệnh viện Đa khoa Quốc tế Thành Tâm.
Theo đúng thỏa thuận pháp lý đã ký kết, tôi xin chính thức bổ nhiệm Giáo sư, Tiến sĩ, Cố vấn trưởng Phạm Quốc Bảo giữ chức vụ Giám đốc điều hành y khoa tối cao của bệnh viện!
Toàn bộ hệ thống quản lý lâm sàng, nhân sự y khoa và tiêu chuẩn điều trị từ nay sẽ do Giám đốc Bảo toàn quyền quyết định.
Bảo bước lên bục cao nhất của phòng hội thảo, ánh mắt anh nhìn bao quát toàn bộ các y bác sĩ dưới quyền mới của mình.
Giọng nói của anh vang lên ấm áp nhưng tràn đầy sự nghiêm nghị và y đức thiêng liêng.
Tôi biết trong số các đồng nghiệp ngồi đây, có những người đã phải im lặng trước cái ác vì miếng cơm manh áo.
Nhưng kể từ ngày hôm nay, dưới sự quản lý của tôi và sự hỗ trợ của Tập đoàn Vạn An, tôi cam kết sẽ xây dựng bệnh viện này thành một thánh đường y khoa thực sự của sự lương thiện và chuyên môn đỉnh cao.
Nhiệm vụ đầu tiên của chúng ta trong chiều nay là thành lập ba kíp mổ đặc biệt do tôi trực tiếp làm tổng chỉ huy để phẫu thuật thay thế van tim cơ học đạt chuẩn miễn phí cho bệnh nhân Nguyễn Văn Nam và bốn bệnh nhân khác đã bị cấy ghép van lỗi.
Chúng ta sẽ lấy lại danh dự cho chiếc áo blouse trắng này bằng chính những nhát dao mổ cứu người chuẩn xác nhất!
Tiếng vỗ tay vang dội rầm rập như sấm truyền khắp phòng hội thảo tầng năm, lan dần xuống các khoa lâm sàng và sảnh lớn của bệnh viện.
Nhiều y tá và bác sĩ trẻ đã bật khóc vì xúc động, họ hiểu rằng bóng tối bao trùm bệnh viện suốt nhiều năm qua cuối cùng đã bị quét sạch bởi ánh sáng của công lý và y đức chân chính.
Bảo bước ra ban công tầng năm của bệnh viện, những tia nắng ấm áp sau cơn mưa giông tối qua bắt đầu chiếu rọi rực rỡ xuống đại lộ Nguyễn Văn Linh.
Khánh Vy bước đến đứng cạnh anh, cô đưa tay ra, nở một nụ cười sòng phẳng và rạng rỡ.
Chúc mừng anh, Giám đốc Bảo. Chúng ta đã hoàn thành xuất sắc giai đoạn một của hợp đồng.
Bảo bắt lấy tay cô, cái bắt tay của hai người trẻ tuổi, thông minh và đầy khát vọng mở ra một chương mới rực rỡ cho nền y tế nước nhà.
Mọi thứ chỉ mới bắt đầu thôi, Khánh Vy.
"""

def split_to_p_blocks(text):
    # Split text into lines, clean empty ones
    lines = [line.strip() for line in text.strip().split('\n') if line.strip()]
    # Wrap each sentence/line into <p>...</p>\n
    p_lines = []
    for line in lines:
        p_lines.append(f"<p>{line}</p>\n")
    return "".join(p_lines)

# Process chapters
chapters = [
    {"title": "Chương 1: Lệnh Sa Thải Trong Đêm Trực", "content": split_to_p_blocks(ch1_text)},
    {"title": "Chương 2: Hồ Sơ Mật Và Sự Xuất Hiện Của Nữ Tổng Tài", "content": split_to_p_blocks(ch2_text)},
    {"title": "Chương 3: Bẫy Kiểm Định Lâm Sàng", "content": split_to_p_blocks(ch3_text)},
    {"title": "Chương 4: Trận Chiến Trực Diện Trên Bàn Học Thuật", "content": split_to_p_blocks(ch4_text)},
    {"title": "Chương 5: Phán Quyết Cuối Cùng Và Sự Trỗi Dậy Của Vạn An", "content": split_to_p_blocks(ch5_text)}
]

# Check word counts
for i, chap in enumerate(chapters, 1):
    # Remove HTML tags to count actual words
    clean_text = re.sub('<[^<]+?>', '', chap['content'])
    word_count = len(clean_text.split())
    print(f"Chapter {i} word count: {word_count}")

# Structure the full draft payload
draft_payload = {
    "title": title,
    "subtitle": subtitle,
    "author": author,
    "genre": genre,
    "intro": f"<p><strong>\"Y đức không cho phép chúng ta lừa dối bệnh nhân. Nếu các người chọn đồng tiền làm kim chỉ nam, tôi sẽ dùng tài năng và luật pháp để quét sạch các người khỏi ngành y!\"</strong></p>\n<p>Phạm Quốc Bảo, một tiến sĩ y khoa thiên tài tốt nghiệp Harvard, quyết định ẩn danh làm bác sĩ thực tập tại Bệnh viện Đa khoa Quốc tế Thành Tâm để điều tra đường dây mổ chui và nâng khống giá thiết bị y tế của Giám đốc Nguyễn Hữu Hoài. Bị sa thải nhục nhã ngay trong đêm trực vì dám bảo vệ tính mạng một bệnh nhân nghèo, Bảo không hề lùi bước. Anh bắt tay cùng nữ chủ tịch lý tính Nguyễn Khánh Vy của Tập đoàn Vạn An, kích hoạt một chiến dịch thanh tra đặc biệt của Hội đồng Y khoa Quốc gia và Bộ Công an, từng bước phơi bày toàn bộ góc tối và lật kèo ngoạn mục ngay trước giờ G.</p>\n",
    "cover_prompt": cover_prompt,
    "chapters": chapters
}

import os

# Output path in scratch directory of application appdata
target_path = "/Users/aaronnguyen/.gemini/antigravity/brain/13820f2d-a410-4981-a823-c5a1024a0a63/scratch/draft_novel_5.json"
os.makedirs(os.path.dirname(target_path), exist_ok=True)

with open(target_path, "w", encoding="utf-8") as f:
    json.dump(draft_payload, f, ensure_ascii=False, indent=2)

print("Saved to draft_novel_5.json successfully.")
