import json
import os

TEMP_PATH = "/Users/aaronnguyen/TN/App/doctieuthuyet/pending_novel_7_temp.json"
FINAL_PATH = "/Users/aaronnguyen/TN/App/doctieuthuyet/pending_novel_7.json"

def count_words(text):
    clean_text = text.replace("<p>", "").replace("</p>", "").replace("\n", " ")
    return len([w for w in clean_text.split() if w.strip()])

# Read the temp file containing Chapters 1-6
with open(TEMP_PATH, "r", encoding="utf-8") as f:
    novel_data = json.load(f)

# Chapter 7: Ánh Sáng Từ Hồ Sơ Lưu Trữ
ch7_sentences = [
    "Tiếng sấm rền vang trên bầu trời Hà Nội báo hiệu một trận cuồng phong sắp đổ ập xuống thành phố.",
    "Bên trong văn phòng bí mật của Lê Bảo Ngọc, Đỗ Minh Tuấn đang đối chiếu tấm bản đồ gốc từ thế kỷ mười chín với các hồ sơ tài chính mới thu được.",
    "Ánh đèn chụp rọi xuống mặt bàn gỗ, hắt lên những con số và biểu đồ phức tạp loang lổ vết mực đen.",
    "Ngọc tự tay pha hai tách cà phê đặc nóng, hương thơm đắng dịu lan tỏa trong không gian yên tĩnh và căng thẳng.",
    "\"Nhìn vào dòng tiền này đi, Tuấn,\" Ngọc chỉ ngón tay thanh mảnh vào bảng thống kê giao dịch của Ngân hàng thương mại cổ phần Thịnh Phát.",
    "\"Vương Thế Dũng đã dùng ba công ty bình phong hoạt động trong lĩnh vực xuất nhập khẩu để luân chuyển dòng tiền giả ODA.\"",
    "\"Mục đích thực sự của chúng là biến dự án Hàng Bạc Plaza thành một tài sản thế chấp khổng lồ hòng vay vốn ngân hàng nhà nước.\"",
    "\"Nói cách khác, chúng đang muốn dùng một dự án ảo để rút ruột hàng ngàn tỷ đồng tiền ngân sách công vụ.\"",
    "Tuấn nhìn chằm chằm vào các chứng từ chuyển khoản, mắt anh nheo lại, lồng ngực phập phồng dữ dội vì tức giận.",
    "\"Chúng không chỉ phá hủy di sản để xây trung tâm thương mại, mà còn muốn cướp đoạt tài sản công của quốc gia!\" Tuấn thốt lên, giọng đanh thép.",
    "Ngọc khẽ gật đầu, khuôn mặt lộ rõ vẻ nghiêm nghị sắc sảo của một nhà quản lý tài năng.",
    "\"Đúng thế, đây là lý do tôi đã chuyển toàn bộ tập hồ sơ tài chính này trực tiếp cho các điều tra viên của Cục Cảnh sát C03.\"",
    "\"Ban chuyên án đã chính thức phê duyệt kế hoạch vây bắt liên minh bẩn thỉu này vào ngày mai.\"",
    "Đột nhiên, chuông điện thoại của Ngọc reo lên dồn dập phá tan sự tĩnh lặng của căn phòng bí mật.",
    "Ngọc áp điện thoại lên tai, gương mặt cô bỗng chốc trở nên xám ngoét, hơi thở dồn dập.",
    "\"Đồng chí Ngọc! Vương Thế Dũng đã phát điên khi biết tin có sắc lệnh dừng dự án của Chính phủ!\" Đầu dây bên kia báo cáo khẩn cấp.",
    "\"Hắn đã lệnh cho gã giang hồ khét tiếng Dũng 'Sẹo' dẫn theo hơn năm mươi tên đàn em mang theo xà beng, búa tạ và xe ủi tiến về phố cổ.\"",
    "\"Chúng định lợi dụng đêm mưa bão lớn này để cưỡng chế phá sập căn nhà cổ Hàng Bạc trước khi lệnh chính thức được tống đạt!\"",
    "Ngọc cúp máy, tay cô run rẩy khẽ nắm chặt chén cà phê nóng đến mức nước cà phê sánh ra ngoài bàn.",
    "\"Tuấn! Vương Thế Dũng muốn chơi trò sự đã rồi! Chúng đang cho xe ủi tiến vào phá sập căn nhà cổ ngay trong đêm nay!\" Ngọc hét lên đầy hoảng hốt.",
    "Tuấn đứng bật dậy, chiếc ghế gỗ đằng sau bị đẩy mạnh ra ngã nhào xuống sàn nhà phát ra tiếng động khô khốc.",
    "Mồ hôi lạnh chảy ròng ròng dọc thái dương, nhưng ánh mắt anh lại bùng lên ngọn lửa kiên định dữ dội hơn bao giờ hết.",
    "\"Chúng ta không thể để chúng phá hủy nó! Đó là linh hồn của khu phố! Tôi sẽ đến đó ngay lập tức!\" Tuấn dứt khoát tuyên bố.",
    "Ngọc nắm chặt tay anh: \"Tôi đi cùng cậu! Chiếc xe của tôi có còi ưu tiên, chúng ta sẽ vượt qua mưa bão nhanh nhất có thể.\"",
    "Hai người lao ra cửa, bỏ lại văn phòng ngập tràn tài liệu và tách cà phê chưa kịp uống đã dần nguội ngắt.",
    "Ngoài trời, những hạt mưa lớn bắt đầu trút xuống trắng xóa cả những con phố Tràng Thi, Hàng Khay, hướng về phía Hoàn Kiếm.",
    "Bão tố thiên nhiên hòa cùng bão tố lòng người đang cuộn trào dữ dội, đẩy cuộc chiến bảo tồn di sản lên đỉnh điểm sinh tử."
]
extra_ch7 = [
    "Chiếc xe SUV công vụ của Ngọc rú còi ưu tiên inh ỏi, lao điên cuồng xuyên qua màn mưa dày đặc như trút nước.",
    "Tuấn ngồi ở ghế phụ, hai tay nắm chặt dây an toàn, ánh mắt đăm đăm nhìn về phía trước qua gạt mưa đang hoạt động hết công suất.",
    "Anh biết rằng chỉ cần chậm trễ mười phút, hệ thống cột lim cổ kính hai trăm năm tuổi sẽ bị nghiền nát dưới lưỡi ủi thép của kẻ thù.",
    "\"Cố lên, Ngọc, chúng ta phải đến trước khi bánh xích xe ủi chạm vào thềm nhà cổ,\" Tuấn lẩm bẩm, giọng run rẩy vì lo lắng.",
    "Ngọc siết chặt vô lăng, đôi mắt phượng sắc bén tập trung cao độ vào những khúc cua trơn trượt của phố Hàng Đào.",
    "\"Tôi sẽ không để công sức của cậu và lịch sử của Hà Nội bị chôn vùi dưới bàn tay tàn ác của Vương Thế Dũng,\" Ngọc khẳng định.",
    "Trong đầu cô lúc này chỉ có một suy nghĩ duy nhất: Phải cứu bằng được di sản Thăng Long, bằng mọi giá.",
    "Phía trước họ, ánh đèn flash đỏ rực của đám giang hồ Thịnh Phát đang bao vây đầu phố Hàng Bạc dần hiện ra trong màn mưa bong bóng."
]
ch7_sentences.extend(extra_ch7)

# Chapter 8: Vây Hãm Trưa Hè Phố Cổ
# Note: Keeping the title "Vây Hãm Trưa Hè Phố Cổ" as requested, but the narrative can explain that it starts as a hot day and turns into a violent afternoon thunderstorm/deluge.
ch8_sentences = [
    "Trưa hè Hà Nội oi ả bỗng chốc bị xé toạc bởi một cơn giông cực mạnh kéo theo mưa gió bão bùng đổ xuống phố cổ.",
    "Tại ngõ Phất Lộc và phố Hàng Bạc, hơn năm mươi tên thanh niên xăm trổ hung hãn tay cầm gậy sắt, xà beng đang phong tỏa hai đầu đường.",
    "Một chiếc xe ủi bánh xích khổng lồ màu vàng của Thịnh Phát đang gầm rú động cơ, nhả khói đen kịt cả góc phố cổ kính.",
    "Dũng 'Sẹo' - gã giang hồ khét tiếng cầm đầu, đứng che ô đen, gương mặt dữ dằn lộ rõ vết sẹo dài từ mắt xuống má.",
    "\"Mau cho xe tiến vào! Phá sập bức tường ngoài cho tao! Kẻ nào cản đường cứ đánh gãy chân!\" Dũng 'Sẹo' hét lớn qua tiếng mưa gầm rú.",
    "Chiếc xe ủi gầm lên một tiếng chói tai, từ từ tiến sát vào thềm đá xanh cổ kính của ngôi phủ đệ Thượng thư thời Nguyễn.",
    "Đột nhiên, Đỗ Minh Tuấn từ trong màn mưa lao ra, anh dang rộng hai tay chắn ngang trước mũi xúc thép khổng lồ của xe ủi.",
    "Nước mưa trút xuống mặt Tuấn xối xả, làm ướt sũng bộ quần áo sờn cũ, nhưng ánh mắt anh lại kiên định và sắc lạnh như dao pha.",
    "\"Dừng lại! Đây là di sản quốc gia! Các người không được phép chạm vào một viên gạch ở đây!\" Tuấn hét lên, giọng vang dội phá tan tiếng bão.",
    "Dũng 'Sẹo' khinh bỉ nhổ nước bọt xuống đất, tiến lại gần chỉ thẳng gậy sắt vào mặt Tuấn: \"Thằng nhãi kiến trúc sư què kia!\"",
    "\"Mày chán sống rồi hả? Mau cút ra trước khi lưỡi xúc này nghiền nát xương cốt mày thành cám!\"",
    "\"Tôi không cút! Các người muốn phá ngôi nhà này thì phải đi qua xác tôi trước!\" Tuấn dõng dạc nói, không hề lùi bước dù chỉ một milimét.",
    "Ngay lúc đó, những người dân phố cổ Hàng Bạc xung quanh cũng từ trong các căn nhà ống ập ra dưới màn mưa tầm tã.",
    "Họ là những cụ già tóc bạc phơ, những thanh niên lao động, những người phụ nữ tần tảo quanh năm sống bên bóng mát ngôi nhà cổ.",
    "Họ đồng loạt tiến lên, liên kết tay nhau tạo thành một bức tường người vững chãi đứng bên cạnh Đỗ Minh Tuấn.",
    "\"Bảo vệ nhà cổ! Bảo vệ di sản của tổ tiên! Không cho bọn cướp đất hoành hành!\" Tiếng hô vang dội của nhân dân phố cổ vang lên.",
    "Hàng chục con người đứng hiên ngang dưới mưa bão, đối mặt với lưỡi thép xe ủi và đám giang hồ hung hãn vũ trang đầy mình.",
    "Dũng 'Sẹo' bỗng chốc khựng lại, gương mặt hung tợn lộ rõ vẻ hoang mang khi nhìn thấy làn sóng phẫn nộ của quần chúng nhân dân.",
    "Gã không ngờ một thằng kiến trúc sư nghèo như Tuấn lại có sức ảnh hưởng lớn lao đến người dân phố cổ đến thế.",
    "\"Khốn kiếp! Đập phá cho tao! Không phải sợ! Có anh Dũng Thịnh Phát bảo lãnh rồi!\" Dũng 'Sẹo' điên cuồng ra lệnh.",
    "Đám giang hồ bắt đầu lao lên, dùng gậy sắt hung bạo vụt tới tấp vào bức tường người hòng giải tỏa hiện trường.",
    "Tuấn lao ra đỡ một cú vụt gậy sắt chí mạng cho một cụ già, vai anh chịu một đòn đau điếng khiến anh ngã quỵ xuống vũng nước mưa.",
    "Máu tươi từ trán Tuấn chảy ròng ròng, hòa cùng dòng nước mưa lạnh ngắt chảy loang lổ trên nền gạch bát tràng cổ kính.",
    "\"Tuấn!\" Lê Bảo Ngọc từ chiếc xe công vụ vừa đỗ xịch bên đường lao tới, cô nâng Tuấn dậy, gương mặt ngập tràn sự xót xa và tức giận.",
    "Cô đứng chắn trước mặt Tuấn, rút từ trong túi áo ra sắc lệnh khẩn cấp của Chính phủ, giơ cao trước mặt Dũng 'Sẹo'.",
    "\"Tất cả dừng tay! Tôi là Lê Bảo Ngọc - Phó Giám đốc Sở Quy hoạch Kiến trúc Hà Nội!\"",
    "\"Đây là lệnh khẩn cấp của Phó Thủ tướng Chính phủ yêu cầu bảo tồn nguyên trạng căn nhà này!\"",
    "\"Ai dám bước lên một bước sẽ bị khép vào tội chống đối người thi hành công vụ và hủy hoại tài sản quốc gia đặc biệt nghiêm trọng!\"",
    "Khí chất uy nghiêm và đanh thép của nữ chuyên gia UNESCO khiến toàn bộ đám giang hồ bỗng chốc chôn chân tại chỗ.",
    "Chiếc xe ủi đang rú ga dữ dội cũng chầm chậm dừng lại, người tài xế sợ hãi tắt máy trước áp lực pháp lý quá lớn.",
    "Dũng 'Sẹo' nghiến răng kèn kẹt, gã biết đêm nay gã không thể dùng bạo lực để giải quyết khi có mặt Phó Giám đốc Sở và đám đông nhân dân.",
    "\"Rút quân! Sáng mai anh Dũng sẽ có cách xử lý bọn mày!\" Dũng 'Sẹo' hầm hè ra lệnh cho đàn em rút lui.",
    "Đám giang hồ lầm lũi rút đi trong cơn mưa bão dần ngớt, bỏ lại khu phố cổ Hàng Bạc vẫn hiên ngang đứng vững dưới bầu trời đêm.",
    "Ngọc dùng khăn tay nhẹ nhàng lau vết máu trên trán Tuấn, móng tay cô bấu chặt vào lòng bàn tay vì căm phẫn lũ tàn bạo.",
    "\"Cậu đã làm rất tốt, Tuấn ạ. Cậu đã cứu cả khu phố này đêm nay bằng lòng dũng cảm của mình,\" Ngọc khẽ nói, giọng rung lên vì cảm động.",
    "Tuấn mỉm cười nhạt qua làn nước mưa, lồng ngực phập phồng thở dốc nhưng lòng tràn ngập một cảm giác sướng vui tột cùng."
]
extra_ch8 = [
    "Người dân phố cổ xung quanh ùa tới, người mang dầu gió, người mang trà nóng vây quanh bảo bọc lấy Tuấn.",
    "Họ nhìn người kiến trúc sư trẻ tuổi với ánh mắt đầy trân trọng và biết ơn sâu sắc.",
    "\"Cảm ơn cậu Tuấn, không có cậu thì ngôi nhà tổ tiên để lại đã thành bình địa rồi,\" một cụ già xúc động nói.",
    "Tuấn nắm chặt tay cụ: \"Đây là trách nhiệm của cháu, của thế hệ trẻ đối với linh hồn của Thăng Long.\"",
    "Ngọc nhìn cảnh tượng ấm áp đó, lòng dâng lên niềm kiêu hãnh khôn tả về tình nghĩa của người Hà Nội.",
    "Cô biết rằng dù kẻ thù có bao nhiêu tiền bạc, chúng cũng không bao giờ mua được lòng dân và giá trị lịch sử đích thực.",
    "\"Hãy nghỉ ngơi đi, Tuấn. Sáng mai sẽ là trận chiến cuối cùng tại lễ động thổ của Thịnh Phát,\" Ngọc nói đầy bí ẩn.",
    "Một ngày hè oi ả bão bùng đã qua, nhường chỗ cho ánh bình minh rực rỡ của ngày phán xét đang cận kề."
]
ch8_sentences.extend(extra_ch8)

# Chapter 9: Lưới Trời Lồng Lộng (C03 Xuất Quân)
ch9_sentences = [
    "Sáng hôm sau, bầu trời Hà Nội sau cơn bão trở nên quang đãng và trong vắt như gương.",
    "Tại khu đất vàng xung quanh căn nhà cổ Hàng Bạc, Tập đoàn Thịnh Phát vẫn trơ trẽn dựng lên một sân khấu lễ động thổ vô cùng hoành tráng.",
    "Dàn hoa tươi rực rỡ, thảm đỏ trải dài cùng hàng chục lẵng hoa chúc mừng của các doanh nghiệp đối tác xếp kín hai bên đường.",
    "Vương Thế Dũng đứng ở vị trí trung tâm, bộ vest đen quyền lực, gương mặt kiêu ngạo tự đắc cười nói với các vị khách mời cấp cao.",
    "Nguyễn Minh Hải đứng bên cạnh gã, tay cầm xấp bản vẽ ý tưởng đã được đóng dấu bản quyền khống, gương mặt tràn ngập vẻ đắc ý.",
    "Hoàng Văn Nam - Trưởng phòng Quy hoạch đã bị đình chỉ công tác nhưng vẫn lén lút đến dự, ghé sát tai Dũng thì thầm đầy vẻ xu nịnh.",
    "\"Anh Dũng yên tâm, tôi đã cho người phong tỏa truyền thông, mụ Lê Bảo Ngọc không thể làm gì được chúng ta nữa đâu,\" Nam nói nhỏ.",
    "Dũng cười khẩy, ánh mắt chứa đầy sự tàn nhẫn: \"Một con nhãi ranh và một thằng kiến trúc sư què thì làm nên trò trống gì.\"",
    "\"Hôm nay dự án Hàng Bạc Plaza chính thức động thổ, dòng tiền ODA khống sẽ đổ vào tài khoản, Thịnh Phát sẽ trở thành bá chủ bất động sản!\"",
    "Đúng lúc Nguyễn Minh Hải chuẩn bị bước lên bục phát biểu để giới thiệu về bản vẽ \"thiết kế độc quyền bảo tồn\" của mình.",
    "Tiếng còi hú inh ỏi vang dội từ xa vọng lại, hàng loạt chiếc xe đặc chủng màu đen của Cục Cảnh sát C03 Bộ Công an áp sát hiện trường.",
    "Hơn ba mươi chiến sĩ cảnh sát kinh tế trong sắc phục nghiêm trang, vũ trang đầy đủ nhanh chóng phong tỏa toàn bộ khu vực lễ động thổ.",
    "Cả hội trường lễ động thổ bỗng chốc náo loạn, tiếng la hét hoảng sợ của các khách mời vang lên xôn xao.",
    "Lê Bảo Ngọc bước vào hiện trường dẫn đầu đoàn công tác, đi bên cạnh cô là Đỗ Minh Tuấn với vết băng trắng trên trán đầy kiêu hãnh.",
    "Đi cùng họ là một vị kiểm sát viên đại diện cho Viện Kiểm sát Nhân dân Tối cao, tay cầm văn bản đóng dấu đỏ chót của cơ quan pháp luật.",
    "Vương Thế Dũng nhìn thấy cảnh tượng này, gương mặt chữ điền bỗng chốc cứng đờ, ly rượu vang trên tay rơi xuống đất vỡ tan tành.",
    "Mồ hôi lạnh chảy ròng ròng dọc hai bên thái dương gã, đôi mắt co rút lại đầy sự kinh hoàng và không tin nổi.",
    "\"Lê Bảo Ngọc! Cô... cô dám dẫn công an đến phá lễ khởi công của tôi sao?\" Dũng gầm lên, giọng run rẩy.",
    "Ngọc khẽ nhếch môi nở một nụ cười nửa miệng đầy lạnh lùng và uy lực vô song.",
    "\"Vương Thế Dũng, ông không còn tư cách để tổ chức bất kỳ lễ khởi công nào nữa đâu,\" Ngọc tuyên bố, giọng vang dội toàn trường.",
    "Vị kiểm sát viên bước lên phía trước, dõng dạc đọc to quyết định phê chuẩn khởi tố vụ án và lệnh bắt tạm giam.",
    "\"Thay mặt Viện Kiểm sát Nhân dân Tối cao, chúng tôi công bố lệnh bắt khẩn cấp đối với Vương Thế Dũng về tội rửa tiền và thao túng chứng khoán.\"",
    "\"Bắt tạm giam Hoàng Văn Nam về tội nhận hối lộ và cố ý làm sai lệch hồ sơ quy hoạch di sản quốc gia.\"",
    "\"Bắt tạm giam Nguyễn Minh Hải về tội làm giả tài liệu và cướp đoạt quyền sở hữu trí tuệ bản quyền công nghệ bảo tồn.\"",
    "Lời tuyên án như sét đánh ngang tai giữa trời quang, khiến cả ba kẻ ác bỗng chốc ngã quỵ xuống nền thảm đỏ.",
    "Hai chiến sĩ cảnh sát C03 nhanh chóng tiến lên, rút còng số tám lạnh ngắt tra vào cổ tay của Vương Thế Dũng trước sự chứng kiến của hàng trăm ống kính phóng viên.",
    "Hải run rẩy quỳ sụp xuống đất, nước mắt nước mũi chảy dài đầy thảm hại: \"Anh Tuấn ơi! Em lạy anh! Xin anh tha cho em! Em bị ép buộc!\"",
    "Tuấn cúi xuống nhìn gã bạn phản bội đầy khinh bỉ, giọng nói lạnh lùng đanh thép: \"Khi mày cướp bản vẽ của tao và đe dọa mẹ tao, mày có nghĩ đến ngày này không?\"",
    "\"Pháp luật Việt Nam nghiêm minh, lưới trời lồng lộng, kẻ gieo gió chắc chắn phải gặt bão, Hải ạ.\"",
    "Hoàng Văn Nam mặt cắt không còn một giọt máu, đờ đẫn để cảnh sát áp giải đi như một cái xác không hồn dưới ánh nắng hè rực rỡ.",
    "Toàn bộ người dân phố cổ Hàng Bạc xung quanh chứng kiến cảnh tượng này liền vỗ tay reo hò vang dội cả một góc trời.",
    "Tiếng vỗ tay, tiếng reo hò sảng khoái \"sướng\" vô cùng của nhân dân vang vọng khắp 36 phố phường Hà Nội.",
    "Ngọc nhìn Tuấn, nụ cười rạng rỡ hiện lên trên khuôn mặt thanh tú của cô, xua tan đi mọi căng thẳng của những ngày qua.",
    "Chiếc bẫy thép pháp lý đã sập xuống hoàn hảo, liên minh bẩn thỉu hủy hoại di sản đã bị tiêu diệt tận gốc trước sức mạnh của công lý và lòng dân."
]
extra_ch9 = [
    "Các phóng viên báo chí liên tục ghi lại những khoảnh khắc lịch sử khi chiếc còng số 8 khóa chặt tay Vương Thế Dũng.",
    "Tấm bảng dự án \"Hàng Bạc Plaza\" hoành tráng bị các chiến sĩ cảnh sát tháo dỡ xuống, ném thẳng vào thùng xe đặc chủng.",
    "Thay vào đó, một tấm biển đỏ chói ghi rõ \"Khu di tích kiến trúc nghệ thuật phủ đệ Thượng thư thời Nguyễn - Nghiêm cấm xâm phạm\" được dựng lên.",
    "Tuấn đứng trước thềm ngôi nhà cổ, nhìn tấm biển mới dựng mà lòng trào dâng một cảm xúc thiêng liêng khó tả.",
    "Anh đã lấy lại được công lý cho bản thân, lấy lại danh dự cho ngành bảo tồn di sản nước nhà.",
    "Ngọc tiến lại gần anh, ánh mắt lấp lánh niềm vui chiến thắng: \"Chúc mừng cậu, Giám đốc dự án tương lai.\"",
    "Tuấn khẽ cười, một nụ cười rạng rỡ và sảng khoái thực sự sau những đêm trắng đầy u uất và phẫn hận.",
    "Lưới trời lồng lộng, không một kẻ ác nào có thể thoát khỏi sự trừng phạt nghiêm khắc của pháp luật và lương tâm con người."
]
ch9_sentences.extend(extra_ch9)

# Chapter 10: Rực Rỡ Di Sản Thăng Long
ch10_sentences = [
    "Một tháng sau ngày liên minh bẩn thỉu của Thịnh Phát bị triệt phá hoàn toàn dưới ánh sáng pháp luật.",
    "Phố cổ Hàng Bạc hôm nay rộn ràng trong tiếng trống hội và rực rỡ sắc cờ đỏ sao vàng tung bay trước gió.",
    "Tại ngôi nhà cổ hai trăm năm tuổi, Lễ công bố dự án trùng tu bảo tồn kiểu mẫu di sản Thăng Long chính thức được diễn ra.",
    "Đại diện của văn phòng UNESCO tại Việt Nam cùng dàn chuyên gia quốc tế hàng đầu đang chăm chú lắng nghe bài thuyết trình của Đỗ Minh Tuấn.",
    "Tuấn đứng trên bục giảng trong bộ trang phục lịch lãm, gương mặt rạng rỡ khí chất thông tuệ và sự tự tin vô song.",
    "Bản vẽ tay di sản hệ khung chịu lực lim của anh được phóng lớn đặt ở vị trí trang trọng nhất, dưới tiêu đề ghi rõ tên tác giả: Đỗ Minh Tuấn.",
    "Anh tự tin trình bày chi tiết về kỹ thuật lắp ghép mộng hoa văn đấu củng không cần đinh - niềm tự hào của kiến trúc truyền thống Việt Nam.",
    "Những tràng pháo tay giòn giã và những ánh mắt thán phục của bạn bè quốc tế liên tục vang lên khắp không gian hội nghị.",
    "Trưởng đại diện UNESCO tại Việt Nam tiến lên trao cho Tuấn chứng nhận dự án bảo tồn di sản văn hóa xuất sắc khu vực Đông Nam Á.",
    "\"Kiến trúc sư Đỗ Minh Tuấn đã chứng minh được tài năng xuất chúng và lòng dũng cảm phi thường trong việc cứu vãn di sản này,\" vị đại diện phát biểu.",
    "Tuấn nhận tấm bằng khen danh giá, nước mắt nóng hổi khẽ lăn dài trên má, nhưng đó là những giọt nước mắt của niềm hạnh phúc tột cùng.",
    "Anh được bổ nhiệm làm Giám đốc Dự án Trùng tu Di sản Phố cổ Hà Nội kiêm Cố vấn trưởng ban quản lý di tích cấp thành phố.",
    "Danh dự của anh đã được khôi phục hoàn toàn, thậm chí tên tuổi anh giờ đây đã vươn tầm ra thế giới với tư cách là chuyên gia hàng đầu.",
    "Chiều muộn, khi ngày hội kết thúc tốt đẹp, Tuấn và Lê Bảo Ngọc cùng nhau tản bộ dọc theo ven bờ Hồ Gươm lộng gió.",
    "Ánh hoàng hôn đỏ rực buông xuống Tháp Rùa cổ kính, hắt lên những rặng liễu rủ bóng xuống mặt nước xanh lục đằm thắm.",
    "Gió hồ thổi bay nhẹ mái tóc dài của Ngọc, làm tôn lên gương mặt thanh tú và đôi mắt phượng sáng ngời của cô.",
    "\"Cảm ơn cô, Ngọc. Nếu không có sự dũng cảm và trí tuệ của cô, tôi đã không có được ngày hôm nay,\" Tuấn chân thành nói.",
    "Ngọc dừng bước, quay lại nhìn Tuấn, nụ cười dịu dàng và kiêu hãnh xuất hiện trên môi cô.",
    "\"Chúng ta là những người con của Hà Nội, Tuấn ạ. Bảo vệ hồn cốt của Thăng Long là định mệnh của chúng ta.\"",
    "\"Tôi rất vinh dự được đồng hành cùng một kiến trúc sư tài hoa và kiên cường như cậu trên con đường này.\"",
    "Tuấn nhìn thẳng vào mắt Ngọc, lòng anh dâng lên một tình cảm sâu sắc vượt qua cả tình đồng chí thông thường.",
    "Họ đã cùng nhau đi qua những ngày giông bão đen tối nhất, cùng nhau chiến đấu giành lại công lý bằng cả xương máu.",
    "Giờ đây, trước không gian linh thiêng của thủ đô ngàn năm văn hiến, tương lai rực rỡ đang mở ra trước mắt họ.",
    "Hai người đứng cạnh nhau dưới ánh hoàng hôn rực rỡ của Hồ Gươm, bàn tay họ khẽ chạm vào nhau đầy ấm áp và tin cậy.",
    "Linh hồn của khu phố cổ Hà Nội đã được giữ gìn trọn vẹn, rực rỡ và trường tồn mãi mãi cùng thời gian dưới sự chung tay của thế hệ trẻ hôm nay."
]
extra_ch10 = [
    "Những con sóng nhỏ lăn tăn trên mặt Hồ Gươm như những lời thì thầm chúc phúc của lịch sử gửi tới hai người con ưu tú.",
    "Khu phố cổ ngoài kia đang lên đèn, những mái ngói rêu phong lung linh dưới ánh đèn vàng ấm áp đầy chất thơ.",
    "Đỗ Minh Tuấn kiêu hãnh ngẩng cao đầu nhìn về phía trước, sẵn sàng cho những công trình trùng tu vĩ đại tiếp theo.",
    "Bởi anh biết, chỉ cần có niềm tin và tình yêu chân chính, di sản Thăng Long sẽ luôn luôn rực rỡ và bất tử."
]
ch10_sentences.extend(extra_ch10)

novel_data["chapters"].append({
    "title": "Chương 7: Ánh Sáng Từ Hồ Sơ Lưu Trữ",
    "content": "\n".join([f"<p>{s}</p>" for s in ch7_sentences])
})

novel_data["chapters"].append({
    "title": "Chương 8: Vây Hãm Trưa Hè Phố Cổ",
    "content": "\n".join([f"<p>{s}</p>" for s in ch8_sentences])
})

# Chapter 9
novel_data["chapters"].append({
    "title": "Chương 9: Lưới Trời Lồng Lộng (C03 Xuất Quân)",
    "content": "\n".join([f"<p>{s}</p>" for s in ch9_sentences])
})

# Chapter 10
novel_data["chapters"].append({
    "title": "Chương 10: Rực Rỡ Di Sản Thăng Long",
    "content": "\n".join([f"<p>{s}</p>" for s in ch10_sentences])
})

# Verify that there are exactly 10 chapters
assert len(novel_data["chapters"]) == 10, f"Expected 10 chapters, got {len(novel_data['chapters'])}"

# Verification of word counts and V13 HTML formatting
for i, chap in enumerate(novel_data["chapters"]):
    title = chap["title"]
    content = chap["content"]
    words = count_words(content)
    print(f"Chapter {i+1} ({title}) Word Count: {words}")
    
    # Check V13 formatting
    lines = content.strip().split('\n')
    for line_idx, line in enumerate(lines):
        if not line.startswith("<p>") or not line.endswith("</p>"):
            raise ValueError(f"Formatting error in Chapter {i+1}, Line {line_idx+1}: {line}")

# Write to FINAL_PATH
with open(FINAL_PATH, "w", encoding="utf-8") as f:
    json.dump(novel_data, f, ensure_ascii=False, indent=2)

print("Stage 3 completed. Final novel successfully validated and written to pending_novel_7.json.")

# Stage 4: Delete the temporary file
if os.path.exists(TEMP_PATH):
    os.remove(TEMP_PATH)
    print("Stage 4 completed. Temporary file pending_novel_7_temp.json has been deleted.")
