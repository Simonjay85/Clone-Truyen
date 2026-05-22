import json
import os

TEMP_PATH = "/Users/aaronnguyen/TN/App/doctieuthuyet/pending_novel_7_temp.json"
FINAL_PATH = "/Users/aaronnguyen/TN/App/doctieuthuyet/pending_novel_7.json"

def count_words(text):
    # Strip HTML tags to count words accurately
    clean_text = text.replace("<p>", "").replace("</p>", "").replace("\n", " ")
    return len([w for w in clean_text.split() if w.strip()])

def validate_html_sentences(content):
    lines = content.strip().split('\n')
    for line in lines:
        if not line.startswith("<p>") or not line.endswith("</p>"):
            return False, f"Line missing p tags: {line}"
    return True, ""

# Stage 1 Data: Title, Intro, Chapters 1-3
novel_data = {
    "idx": 7,
    "title": "Kiến Trúc Sư Phố Cổ Hà Nội: Bị Cướp Bản Vẽ Di Sản, Tôi Cứu Cả Khu Phố",
    "author": "Đỗ Minh Tuấn",
    "genre": "Sảng Văn",
    "intro": "<p><strong>\"Một kẻ xuất thân từ gia đình nghèo hèn, không tiền không thế như mày thì lấy tư cách gì đòi bảo vệ di sản của Thăng Long hả Tuấn? Bản vẽ này từ nay mang tên tao, còn mày thì chuẩn bị cuốn gói khỏi giới kiến trúc đi!\"</strong></p>\n<p>Kiến trúc sư bảo tồn Đỗ Minh Tuấn bị người bạn thân nhất phản bội, cấu kết với tập đoàn bất động sản Thịnh Phát để cướp đi công sức cả đời của anh. Không chỉ mất đi bản vẽ trùng tu phố cổ, anh còn bị vu oan làm giả hồ sơ khảo cổ di sản, đứng trước nguy cơ tù tội.</p>\n<p>Trong thời khắc đen tối nhất, anh gặp Lê Bảo Ngọc — Phó Giám đốc Sở Quy hoạch Kiến trúc Hà Nội mới về nước. Bằng trí tuệ sắc bén và lòng kiêu hãnh của những người con Hà Nội, họ bắt đầu cuộc chiến vạch trần liên minh lợi ích bẩn thỉu, bảo vệ hồn cốt ngàn năm của thủ đô.</p>",
    "chapters": []
}

# Chapter 1: Đêm Trắng Phố Gầm Cầu
# We need to construct around 70+ high-quality sentences to hit ~1200 words.
ch1_sentences = [
    "Tiếng mưa đêm phố cổ rơi lộp bộp trên những mái ngói rêu phong của ngõ Phất Lộc.",
    "Bên trong căn nhà cổ hai trăm năm tuổi tại Hàng Bạc, ánh đèn dầu leo lét hắt lên những cột lim đen bóng màu thời gian.",
    "Đỗ Minh Tuấn quỳ trên sàn gỗ gụ bám bụi, bàn tay run rẩy tỉ mẩn dùng thước pan-me đo đạc từng khớp mộng hoa văn đấu củng.",
    "Lồng ngực anh phập phồng theo từng nhịp thở, mắt viễn thị hằn lên những tia máu đỏ vì đã thức trắng ba đêm liên tục.",
    "Anh biết, nếu không hoàn thành bản phác thảo chi tiết này trước bình minh, ngôi nhà cổ quý giá này sẽ biến mất vĩnh viễn.",
    "Bản vẽ tay cao rộng hơn một mét chứa đựng toàn bộ cấu trúc kiến trúc thời Nguyễn đang dần hiện hình dưới ngòi bút sắt sắc sảo.",
    "Đột nhiên, cánh cửa gỗ lim dày cộp bị đẩy mạnh ra, tiếng bản lề rít lên khô khốc vang vọng giữa đêm tĩnh mịch.",
    "Hơi lạnh tràn vào phòng mang theo mùi mưa ẩm ướt và mùi nước hoa đắt tiền đầy nồng nặc.",
    "Nguyễn Minh Hải bước vào, bộ vest sang trọng không một nếp nhăn, đôi giày da bóng loáng không hề dính một hạt bùn đất phố cổ.",
    "Phía sau hắn là bốn gã bảo vệ cao lớn của Tập đoàn địa ốc Thịnh Phát, gương mặt bặm trợn và đầy sát khí.",
    "Hải khẽ nhếch môi nở một nụ cười nửa miệng đầy mưu mô, ánh mắt lướt qua xấp bản vẽ trên bàn gỗ với sự thèm khát tột cùng.",
    "\"Mày vẫn đang còng lưng ra vẽ cho tao đấy à, Tuấn thân mến?\" Hải cất giọng vuốt ve nhưng chứa đầy sự mỉa mai.",
    "Tuấn đặt chiếc bút sắt xuống, trán lấm tấm mồ hôi lạnh, chầm chậm đứng dậy đối diện với người bạn học cùng phòng đại học năm xưa.",
    "\"Hải, đây là công trình khảo sát độc lập của tôi theo yêu cầu của Viện Bảo tồn Di sản, cậu dẫn người của Thịnh Phát đến đây làm gì?\" Tuấn hỏi, giọng đanh lại.",
    "Hải phá lên cười, tiếng cười vang lên lách cách như tiếng kim loại va vào nhau giữa không gian u tối.",
    "Hắn thong thả rút từ trong túi áo trong ra một văn bản đóng dấu đỏ chót của Sở Quy hoạch Kiến trúc Hà Nội.",
    "\"Sai rồi, từ hôm nay, dự án bảo tồn khu nhà cổ Hàng Bạc này đã thuộc quyền sở hữu của Ban dự án Hàng Bạc Plaza do tao làm Kiến trúc sư trưởng.\"",
    "\"Còn mày, Đỗ Minh Tuấn, đây là quyết định chấm dứt hợp đồng lao động và thu hồi giấy phép khảo sát của mày do chính tay Trưởng phòng Hoàng Văn Nam ký.\"",
    "Tuấn giật lấy tờ giấy, đôi mắt co rút lại khi nhìn thấy dòng chữ đen mực đỏ rõ ràng, đầu óc anh vang lên một tiếng oanh oanh.",
    "Mồ hôi lạnh chảy ròng ròng dọc theo thái dương, hai bên màng tang anh giật mạnh liên tục vì phẫn nộ.",
    "\"Các người điên rồi sao? Đây là di sản cấp một quốc gia, quy hoạch đô thị không được phép phá dỡ để xây trung tâm thương mại!\" Tuấn quát lên, ngón tay bóp nát tờ quyết định.",
    "Hải tiến lại gần, ghé sát tai Tuấn, thì thầm bằng giọng điệu rắn độc: \"Di sản hay không là do kẻ có tiền quyết định, Tuấn ạ.\"",
    "\"Thịnh Phát đã rót năm trăm tỷ đồng vào dự án cải tạo cảnh quan Hoàn Kiếm, ai cản đường sẽ bị nghiền nát.\"",
    "\"Còn bản thiết kế này của mày...\" Hải nhanh như cắt giật phắt lấy xấp bản vẽ chi tiết hệ thống chịu lực gỗ cổ truyền trên bàn.",
    "\"Trả lại cho tôi!\" Tuấn lao tới nhưng lập tức bị hai gã bảo vệ hộ pháp ôm chặt lấy, ghì mạnh xuống sàn nhà lạnh lẽo.",
    "Khuỷu tay anh đập xuống nền gạch bát tràng đau nhói, khớp xương vai kêu răng rắc dưới áp lực đè nén dã man.",
    "Anh trơ mắt nhìn Hải cuộn tròn bản vẽ di sản mà anh đã dành ba năm trời nghiên cứu, nâng niu như báu vật.",
    "Hải giơ bản vẽ lên, ánh mắt lấp lánh sự điên cuồng và tham lam tột độ: \"Từ giờ, bản vẽ hệ khung chịu lực độc quyền này sẽ mang tên Nguyễn Minh Hải.\"",
    "\"Tao sẽ dùng nó để lấy chứng chỉ chuyên gia bảo tồn cấp quốc tế của UNESCO, còn mày sẽ chỉ là một kẻ vô danh tiểu tốt.\"",
    "Tuấn cố gắng giãy giụa, móng tay bấu chặt vào lòng bàn tay đến mức rớm máu tươi, hòa cùng bụi đất sàn nhà.",
    "\"Mày là đồ ăn cắp! Hải! Mày sẽ phải trả giá cho việc này!\" Tuấn gầm lên, lồng ngực phập phồng dữ dội.",
    "Hải không hề tức giận, hắn chỉ cúi xuống nhìn Tuấn như nhìn một con kiến hôi dưới đế giày da đắt tiền của mình.",
    "\"Trả giá? Ai tin mày? Ai sẽ đứng ra làm chứng cho một thằng kiến trúc sư què quặt không tiền không quyền thế?\"",
    "\"Để tao cho mày biết thêm một tin vui nhé, sáng mai, báo chí sẽ đăng tin Đỗ Minh Tuấn bị đuổi việc vì làm giả hồ sơ khảo cổ di sản nhằm trục lợi.\"",
    "\"Mày sẽ bị đuổi khỏi giới kiến trúc vĩnh viễn, thậm chí là phải ngồi tù vì tội hủy hoại tài liệu công văn nhà nước.\"",
    "Tuấn đờ đẫn cả người, toàn thân lạnh ngắt như rơi vào hầm băng khi nghe lời tuyên án tàn nhẫn của gã bạn thân cũ.",
    "Hải quay lưng đi, vạt áo vest đen bay lên trong gió đêm lạnh buốt, bỏ lại tiếng cười đắc thắng hòa vào tiếng mưa rơi.",
    "\"Vứt nó ra đường, khóa cửa căn nhà này lại, ngày mai xe ủi của Thịnh Phát sẽ bắt đầu dọn dẹp mặt bằng,\" Hải ra lệnh cho đàn em.",
    "Tuấn bị hai gã bảo vệ lôi xềnh xệch ra ngoài hiên, ném thẳng xuống con ngõ nhỏ ngập nước mưa lạnh ngắt.",
    "Cánh cửa gỗ lim cổ kính đóng sầm lại trước mắt anh, tiếng xích sắt khóa cửa vang lên loảng xoảng như tiếng còng tay đang chờ đợi.",
    "Nước mưa tạt thẳng vào mặt Tuấn, lạnh buốt thấu xương, nhưng không lạnh bằng sự u uất và phẫn hận đang dâng trào trong huyết quản anh.",
    "Anh nằm đó dưới cơn mưa tầm tã của Hà Nội, hai tay nắm chặt bùn đất, hàm răng nghiến chặt đến mức bật máu.",
    "Trời đất như sụp đổ quanh anh, sự nghiệp bảo tồn di sản mà anh dùng cả thanh xuân để theo đuổi giờ đây đã hóa thành mây khói.",
    "Anh không cam tâm, anh tuyệt đối không thể để chúng phá hủy ngôi nhà cổ này, không thể để chúng bôi nhọ thanh danh của mình.",
    "Nhưng giữa đêm đen mịt mù của thủ đô, một kiến trúc sư nghèo như anh phải làm sao để chống lại cả một tập đoàn tài phiệt khổng lồ?",
    "Anh ngẩng đầu nhìn lên bầu trời đen thẫm, những hạt mưa rơi vào mắt cay xè, hứa hẹn một cuộc chiến sinh tử sắp bắt đầu."
]

# Let's write additional sentences to make sure word count is highly safe for Chapter 1.
# Let's expand ch1_sentences to hit ~1200 words. Let's make every sentence punchy.
extra_ch1 = [
    "Tiếng bước chân của đám người Hải xa dần, chỉ còn lại tiếng mưa trút xuống mặt đường nhựa loang lổ.",
    "Tuấn cố gượng đứng dậy, toàn thân đau nhức, bộ quần áo sờn cũ đẫm nước mưa dính chặt lấy da thịt.",
    "Anh điên cuồng đập cửa căn nhà cổ: \"Mở ra! Các người không được chạm vào những cột lim đó! Hệ kết cấu đó đã tồn tại hai thế kỷ rồi!\"",
    "Nhưng đáp lại anh chỉ có tiếng gió rít qua những khe ngách chật hẹp của khu phố cổ Hàng Bạc.",
    "Căn nhà cổ im lìm đứng đó như một chứng nhân lịch sử đang thầm lặng chịu đựng sự chà đạp của lòng tham con người.",
    "Tuấn lảo đảo bước đi trong màn đêm, đầu óc quay cuồng với hàng loạt suy nghĩ đen tối về tương lai.",
    "Nếu ngày mai tập đoàn Thịnh Phát họp báo công bố dự án Hàng Bạc Plaza, mọi công sức cứu vãn di sản của anh sẽ đổ sông đổ biển.",
    "Bản vẽ tay độc bản của anh chứa đựng bí mật về cấu trúc lắp ghép mộng gỗ không cần đinh - một kỹ thuật đã thất truyền từ lâu.",
    "Hải cướp đi bản vẽ đó không chỉ là cướp đi danh tiếng, mà là cướp đi linh hồn của khu di sản này để biến nó thành bê tông cốt thép.",
    "Bên tai Tuấn vẫn vang vọng lời đe dọa tàn nhẫn của Hải về việc vu khống anh làm giả hồ sơ khảo cổ di sản quốc gia.",
    "Trưởng phòng Quy hoạch Hoàng Văn Nam là kẻ nổi tiếng tham lam, đã nhận không biết bao nhiêu tiền lót tay của tập đoàn Thịnh Phát.",
    "Họ đã bắt tay nhau tạo dựng một liên minh ma quỷ nhằm bóp nghẹt những tiếng nói phản biện cuối cùng.",
    "Tuấn biết rõ, hồ sơ khảo cổ gốc của ngôi nhà đang được lưu giữ trong kho tư liệu mật của Sở Quy hoạch Kiến trúc Hà Nội.",
    "Chỉ cần Nam và Hải bắt tay nhau tráo đổi tài liệu đó bằng một tập hồ sơ giả, Tuấn sẽ lập tức trở thành tội đồ của ngành bảo tồn.",
    "Anh bước đi dưới ánh đèn đường vàng vọt hắt hiu của phố Hàng Đào, lòng ngập tràn sự căm hờn và bất lực tột cùng.",
    "Bàn tay anh rớm máu vì bị ghì chặt lúc nãy giờ đây bắt đầu đau nhức nhối dưới làn nước mưa buốt giá.",
    "Nhưng nỗi đau thể xác làm sao sánh bằng nỗi đau khi nhìn thấy di sản Thăng Long bị những kẻ trục lợi xâu xé.",
    "\"Không, mình không thể bỏ cuộc như thế này được,\" Tuấn thầm tự nhủ, ánh mắt bỗng chốc trở nên sắc lạnh dị thường.",
    "Anh nhìn về phía tòa nhà Sở Quy hoạch Kiến trúc Hà Nội xa xa dưới ánh đèn thành phố, nơi ngày mai bão tố sẽ chính thức nổi lên.",
    "Anh sẽ dùng chính mạng sống của mình để vạch trần bộ mặt thật của chúng, bảo vệ từng mét vuông đất cổ của cha ông."
]
ch1_sentences.extend(extra_ch1)

# Chapter 2: Buộc Tội Dưới Ánh Đèn Tràng Thi
# Let's write Chapter 2 sentences
ch2_sentences = [
    "Tòa nhà Sở Quy hoạch Kiến trúc Hà Nội tọa lạc trên con phố Tràng Thi sầm uất sáng rực ánh đèn giữa buổi sáng sớm.",
    "Hội trường lớn ở tầng ba chật kín người, bầu không khí ngột ngạt và căng thẳng bao trùm lên từng hàng ghế đại biểu.",
    "Hơn năm mươi phóng viên của các cơ quan báo chí lớn nhỏ đang lách cách điều chỉnh ống kính máy ảnh hướng thẳng lên bục phát biểu.",
    "Hoàng Văn Nam - Trưởng phòng Quy hoạch đô thị, ngồi chễm chệ ở vị trí trung tâm bàn chủ tọa, gương mặt bóng dầu lộ rõ vẻ uy quyền giả tạo.",
    "Bên cạnh gã là Nguyễn Minh Hải trong bộ vest xám tro sang trọng, nụ cười đắc ý hiện rõ trên môi khi nhìn xuống đám đông.",
    "Đỗ Minh Tuấn bước vào hội trường, bộ quần áo của anh tuy đã được sấy khô nhưng vẫn loang lổ những vết ố vàng từ trận mưa đêm qua.",
    "Ngay khi anh xuất hiện, hàng loạt ánh đèn flash của máy ảnh chớp nháy liên hồi, tiếng bàn tán xôn xao nổi lên như ong vỡ tổ.",
    "\"Kìa, chính là kiến trúc sư Đỗ Minh Tuấn, người bị cáo buộc làm giả hồ sơ khảo cổ của căn nhà cổ Hàng Bạc đấy.\"",
    "\"Nghe nói anh ta cố tình thổi phồng giá trị lịch sử để tống tiền chủ đầu tư Thịnh Phát, thật là vô liêm sỉ!\"",
    "Những lời thì thầm ác ý như những mũi kim độc chọc thẳng vào màng nhĩ của Tuấn, khiến lồng ngực anh phập phồng vì giận dữ.",
    "Anh siết chặt nắm tay, khớp xương kêu lên răng rắc, cố gắng giữ cho bản thân không gục ngã trước những ánh mắt khinh bỉ.",
    "Hoàng Văn Nam gõ mạnh chiếc búa gỗ xuống bàn nghị sự, tiếng động vang lên chát chúa dập tắt mọi tiếng ồn ào xung quanh.",
    "\"Hôm nay, Sở Quy hoạch Kiến trúc phối hợp cùng Tập đoàn Thịnh Phát tổ chức cuộc họp khẩn cấp để làm rõ hành vi vi phạm đạo đức nghề nghiệp.\"",
    "\"Kiến trúc sư Đỗ Minh Tuấn đã lợi dụng nhiệm vụ khảo sát để ngụy tạo tài liệu khảo cổ thời Nguyễn, cản trở dự án phát triển đô thị trọng điểm.\"",
    "Nam dõng dạc tuyên bố, ánh mắt gã nhìn Tuấn đầy sự lạnh lùng và khinh miệt như nhìn một kẻ tội đồ.",
    "Tuấn thẳng lưng, bước lên phía trước, giọng nói vang lên dõng dạc phá tan bầu không khí áp đặt: \"Tôi không làm giả bất cứ thứ gì!\"",
    "\"Bản vẽ hệ khung chịu lực gỗ lim của ngôi nhà Hàng Bạc là di sản kiến trúc độc bản từ thế kỷ mười chín, có giá trị khảo cổ cực kỳ lớn.\"",
    "\"Chính các người, Hoàng Văn Nam và Nguyễn Minh Hải, đã cấu kết với Thịnh Phát để cướp đoạt bản vẽ của tôi và âm mưu phá hủy di sản!\"",
    "Hội trường bỗng chốc lặng đi trong vài giây trước lời cáo buộc đanh thép và trực diện của Đỗ Minh Tuấn.",
    "Nguyễn Minh Hải thong thả đứng dậy, điều chỉnh lại chiếc micro trước mặt, gương mặt lộ vẻ buồn bã đầy giả tạo.",
    "\"Thưa các đồng chí lãnh đạo và các bạn phóng viên, tôi thực sự rất đau lòng khi phải chứng kiến người bạn thân của mình sa ngã.\"",
    "\"Đỗ Minh Tuấn vì đố kỵ với dự án Hàng Bạc Plaza của tôi nên đã lẻn vào văn phòng cướp đi bản vẽ ý tưởng sơ thảo của tôi đêm qua.\"",
    "\"Hơn thế nữa, anh ta còn tự ý chỉnh sửa hồ sơ khảo sát, thêm thắt các chi tiết giả mạo để biến một căn nhà gỗ mục nát thành di sản cấp quốc gia.\"",
    "Hải vừa nói vừa bấm nút trình chiếu, trên màn hình lớn hiện ra hình ảnh quét kỹ thuật số bản vẽ tay của Tuấn nhưng dưới góc tiêu đề ghi tên Nguyễn Minh Hải.",
    "\"Đây là bản vẽ hệ khung lim do chính tôi thiết kế và đã đăng ký bản quyền tác giả từ ba tháng trước tại Cục Bản quyền.\"",
    "Tuấn trừng mắt nhìn màn hình, mồ hôi lạnh chảy ròng ròng dọc sống lưng, toàn thân run rẩy vì không ngờ Hải lại trơ trẽn đến mức này.",
    "Chúng đã mua chuộc cả Cục Bản quyền để hợp thức hóa bản vẽ ăn cắp của anh từ trước đó rất lâu nhằm giăng ra cái bẫy hoàn hảo này.",
    "\"Mày... mày đổi trắng thay đen! Bản vẽ đó là do tao tự tay đo đạc suốt ba năm qua!\" Tuấn hét lên, định lao lên bục giảng.",
    "Nhưng ngay lập tức, hai nhân viên an ninh của Sở đã tiến lên chặn đứng anh lại, ép chặt hai bả vai anh xuống ghế.",
    "Hoàng Văn Nam lạnh lùng gõ búa: \"Đỗ Minh Tuấn, trước chứng cứ rành rành của Kiến trúc sư trưởng Nguyễn Minh Hải, hành vi của cậu đã rõ.\"",
    "\"Sở Quy hoạch Kiến trúc Hà Nội chính thức ra quyết định thu hồi chứng chỉ hành nghề kiến trúc sư bảo tồn của cậu vô thời hạn.\"",
    "\"Đồng thời, chúng tôi sẽ chuyển toàn bộ hồ sơ vụ việc làm giả giấy tờ này sang cơ quan công an quận Hoàn Kiếm để khởi tố hình sự.\"",
    "Mặt Tuấn cắt không còn một giọt máu, đôi mắt đờ đẫn nhìn chăm chăm vào tập hồ sơ trên bàn chủ tọa như nhìn vào bản án tử hình của mình.",
    "Anh thấy rõ nụ cười nửa miệng đầy mưu mô của Hải và ánh mắt đầy đắc ý của Nam hắt lên dưới ánh đèn neon chói mắt của hội trường.",
    "Họ không chỉ muốn cướp đi công trình di sản, mà còn muốn chôn vùi danh dự, sự nghiệp và tự do của anh vĩnh viễn trong chốn ngục tù.",
    "Các phóng viên liên tục đặt câu hỏi dồn dập, máy ảnh chớp nháy liên hồi tạo nên một ma trận ánh sáng vây hãm lấy người kiến trúc sư cô độc.",
    "\"Anh Tuấn, anh giải thích thế nào về việc trùng khớp bản vẽ với kiến trúc sư Hải?\"",
    "\"Có phải anh đã nhận tiền của tổ chức nước ngoài để cố tình phá hoại dự án kinh tế của thành phố không?\"",
    "Tuấn nghẹn họng, cổ họng khô khốc không thể thốt nên lời trước sự bao vây vô lý và tàn nhẫn của búa rìu dư luận.",
    "Giữa lúc sự tuyệt vọng lên đến đỉnh điểm, cánh cửa gỗ lớn phía cuối hội trường đột ngột mở rộng ra.",
    "Một người phụ nữ trẻ tuổi bước vào với những bước chân thanh thoát nhưng vô cùng dứt khoát và uy quyền.",
    "Cô mặc bộ vest đen cắt may tinh xảo, mái tóc dài buộc gọn phía sau, gương mặt thanh tú toát lên khí chất thông tuệ và sắc sảo.",
    "Cả hội trường bỗng chốc im bặt, mọi ánh mắt đổ dồn về phía người mới đến với sự ngạc nhiên tột độ.",
    "Hoàng Văn Nam nhìn thấy cô liền vội vàng đứng bật dậy, gương mặt bóng dầu bỗng chốc tái mét, vội vã cúi đầu chào.",
    "\"Phó Giám đốc Lê Bảo Ngọc! Sao đồng chí lại đến đây lúc này?\" Nam lắp bắp hỏi, mồ hôi hột bắt đầu rịn ra trên trán gã.",
    "Lê Bảo Ngọc - Phó Giám đốc mới nhậm chức của Sở Quy hoạch Kiến trúc Hà Nội, đồng thời là chuyên gia bảo tồn cấp cao của UNESCO vừa về nước.",
    "Cô không thèm nhìn Nam hay Hải, đôi mắt phượng sắc sảo lướt qua Đỗ Minh Tuấn đang bị khống chế trên ghế, ánh mắt cô khẽ dao động.",
    "Cô thong thả đi lên bục chủ tọa, rút từ trong cặp tài liệu ra một tập văn bản có đóng dấu xanh của Ủy ban Quốc gia UNESCO Việt Nam.",
    "\"Hoàng Văn Nam, cuộc họp báo này của các anh chưa hề được Ban Giám đốc Sở thông qua,\" Ngọc cất giọng lạnh lùng nhưng uy lực vô song.",
    "\"Hơn nữa, dự án Hàng Bạc Plaza của tập đoàn Thịnh Phát hiện đang nằm trong danh sách thanh tra đặc biệt về bảo tồn di sản của UNESCO.\"",
    "\"Ai cho phép các anh tự ý kết luận hồ sơ di sản Hàng Bạc là giả mạo khi chưa có sự thẩm định của Hội đồng Di sản Quốc gia?\"",
    "Lời nói của Lê Bảo Ngọc như một gáo nước lạnh dội thẳng vào đầu Hoàng Văn Nam và Nguyễn Minh Hải, khiến cả hai câm nín không thốt nên lời."
]
extra_ch2 = [
    "Nguyễn Minh Hải cố lấy lại sự bình tĩnh, tiến lên nở nụ cười lịch thiệp: \"Chào Phó Giám đốc Ngọc, tôi nghĩ đây chỉ là sự hiểu lầm...\"",
    "\"Im lặng! Ở đây không có chỗ cho một kiến trúc sư trưởng tự phong nói chuyện khi tôi đang làm việc với cán bộ dưới quyền,\" Ngọc cắt lời không chút kiêng nể.",
    "Gương mặt Hải đỏ gay lên vì nhục nhã, nụ cười trên môi đông cứng lại, hai tay nắm chặt dưới gầm bàn giảng.",
    "Cô quay sang nhìn hai gã bảo vệ đang giữ Tuấn, giọng nói đanh thép vang lên: \"Thả cậu ấy ra! Ở đây là cơ quan nhà nước, không phải chợ đen để các người hành hung trí thức!\"",
    "Hai gã bảo vệ sợ hãi nhìn Nam, nhưng thấy Nam đang run rẩy gật đầu, bọn chúng liền vội vàng buông tay ra khỏi vai Tuấn.",
    "Tuấn đứng dậy, lồng ngực phập phồng thở dốc, đôi mắt đầy kinh ngạc nhìn người phụ nữ vừa giải vây cho mình.",
    "Ngọc bước đến trước mặt Tuấn, nhìn thẳng vào mắt anh với sự nghiêm nghị: \"Kiến trúc sư Đỗ Minh Tuấn, tôi đã đọc hồ sơ khảo sát cũ của cậu.\"",
    "\"Cậu có dám cam đoan trước danh dự của một người con Hà Nội rằng hệ khung gỗ Hàng Bạc là di sản thực sự không?\"",
    "Tuấn siết chặt tay, nhìn thẳng vào đôi mắt phượng sắc sảo của cô, dõng dạc nói: \"Tôi dùng cả mạng sống của mình để bảo đảm!\"",
    "Một tia sáng tán thưởng khẽ lóe lên trong mắt Ngọc, cô gật đầu nhẹ rồi quay lại nhìn hội trường.",
    "\"Cuộc họp báo hôm nay kết thúc tại đây, toàn bộ hồ sơ dự án Hàng Bạc Plaza sẽ bị niêm phong để thẩm định lại từ đầu,\" Ngọc tuyên bố.",
    "Nam và Hải đứng chôn chân tại chỗ, gương mặt xám ngoét vì tức giận nhưng không dám cãi lại mệnh lệnh trực tiếp của Phó Giám đốc Sở.",
    "Tuấn thở phào một hơi, nhưng anh biết đây mới chỉ là bắt đầu của một trận chiến vô cùng khốc liệt phía trước."
]
ch2_sentences.extend(extra_ch2)

# Chapter 3: Cuộc Gặp Gỡ Ở Hồ Tây
ch3_sentences = [
    "Chiều muộn, gió từ Hồ Tây thổi vào mang theo hơi nước mát lạnh, làm dịu đi cái nóng hầm hập của mùa hè Hà Nội.",
    "Tại một quán trà sen cổ kính nằm sâu trong ngõ nhỏ ven hồ, không gian yên tĩnh đến mức có thể nghe rõ tiếng lá rơi.",
    "Đỗ Minh Tuấn ngồi đối diện với Lê Bảo Ngọc, trên bàn là hai chén trà sen nghi ngút khói tỏa hương thơm thanh khiết.",
    "Ngọc nhấp một ngụm trà, ngón tay thanh mảnh bấu chặt vào thành chén gốm mộc mạc, ánh mắt đăm chiêu nhìn ra mặt nước mênh mông.",
    "\"Cậu biết không, bản vẽ hệ khung chịu lực lim của cậu đêm qua thực sự đã làm tôi kinh ngạc,\" Ngọc mở lời, giọng nói đã bớt đi vẻ lạnh lùng hành chính.",
    "\"Kỹ thuật lắp ghép mộng hoa văn đấu củng không cần đinh đó chỉ xuất hiện ở các cung điện thời Nguyễn tại Huế, rất hiếm thấy ở nhà dân gian Hà Nội.\"",
    "Tuấn cúi đầu nhìn chén trà, nụ cười cay đắng hiện lên trên gương mặt đầy mệt mỏi: \"Nhưng bây giờ nó đã thuộc về Nguyễn Minh Hải.\"",
    "\"Hắn đã dùng tiền bạc và quan hệ để cướp đi công sức ba năm trời của tôi, biến tôi thành một kẻ lừa đảo bị cả ngành ruồng bỏ.\"",
    "Móng tay Tuấn bấu chặt vào lòng bàn tay đến mức rớm máu, nỗi nhục nhã và uất hận vẫn cuộn trào trong lồng ngực anh.",
    "Ngọc đặt chén trà xuống, ánh mắt cô bỗng trở nên vô cùng sắc bén và kiên định.",
    "\"Nguyễn Minh Hải chỉ là một con tốt thí trên bàn cờ của Tập đoàn địa ốc Thịnh Phát mà thôi, Tuấn ạ.\"",
    "\"Đứng sau hắn là Vương Thế Dũng - Tổng giám đốc Thịnh Phát, một kẻ khét tiếng với những thủ đoạn thâu tóm đất vàng bằng mọi giá.\"",
    "\"Thịnh Phát đang muốn dùng khu đất Hàng Bạc Plaza để làm tài sản thế chấp nhằm phát hành trái phiếu khống trị giá hàng ngàn tỷ đồng.\"",
    "\"Nếu dự án này bị đình chỉ vì lý do di sản, dòng tiền của chúng sẽ lập tức bị đứt gãy, kéo theo sự sụp đổ của cả hệ thống.\"",
    "Tuấn ngẩng đầu lên, ánh mắt đờ đẫn bỗng chốc co rút lại trước thông tin tài chính kinh hoàng mà Ngọc vừa chia sẻ.",
    "Anh không ngờ đằng sau một ngôi nhà cổ 200 năm tuổi lại là một âm mưu tài chính khổng lồ liên quan đến vận mệnh của hàng vạn nhà đầu tư.",
    "\"Vậy... tại sao cô lại giúp tôi? Cô là Phó Giám đốc Sở, việc này sẽ gây ảnh hưởng lớn đến tiền đồ của cô,\" Tuấn hỏi, giọng đầy nghi ngại.",
    "Ngọc khẽ nhếch môi nở một nụ cười nửa miệng đầy kiêu hãnh: \"Tôi về nước không phải để làm một công chức ngồi phòng máy lạnh đợi thăng quan tiến chức.\"",
    "\"Tôi là người con của Hà Nội, gia đình tôi ba đời sống ở phố Hàng Bạc, tôi không thể giương mắt nhìn họ san phẳng hồn cốt của thủ đô.\"",
    "\"Hơn nữa, tôi không chấp nhận để những kẻ lưu manh như Vương Thế Dũng và Hoàng Văn Nam chà đạp lên công lý và khoa học.\"",
    "Lời nói của Ngọc như một luồng điện mạnh mẽ chạy dọc sống lưng Tuấn, đánh tan mọi sự tự ti và tuyệt vọng trong lòng anh.",
    "Anh nhìn thấy ở người phụ nữ trẻ tuổi này một ý chí sắt đá và một tấm lòng yêu di sản sâu sắc không hề thua kém mình.",
    "\"Tôi muốn hợp tác với cậu để lật ngược thế cờ này, bảo vệ bằng được căn nhà cổ và đưa liên minh bẩn thỉu đó ra ánh sáng,\", Ngọc đề nghị.",
    "Tuấn thở phào một hơi dài, lồng ngực phập phồng xúc động: \"Tôi cần phải làm gì? Hiện tại tôi đã bị tước giấy phép hành nghề.\"",
    "Ngọc đẩy về phía anh một tấm thẻ công tác đặc biệt có đóng dấu của Viện Bảo tồn Di sản Quốc gia.",
    "\"Tôi đã bổ nhiệm cậu làm cố vấn khoa học đặc biệt cho văn phòng Phó Giám đốc Sở Quy hoạch Kiến trúc Hà Nội.\"",
    "\"Với danh nghĩa này, cậu có quyền tiếp cận mọi hồ sơ lưu trữ và tham gia vào quá trình thẩm định lại ngôi nhà cổ Hàng Bạc.\"",
    "Tuấn cầm tấm thẻ trên tay, những giọt nước mắt nóng hổi suýt chút nữa rơi xuống chén trà sen cổ kính.",
    "Anh biết cơ hội phục thù và cứu vớt di sản của mình đã đến, nhờ vào sự dũng cảm và trí tuệ của người phụ nữ đối diện.",
    "\"Cảm ơn cô, Ngọc. Tôi sẽ không làm cô thất vọng,\" Tuấn khẳng định bằng giọng nói nghẹn ngào nhưng tràn đầy quyết tâm.",
    "Ngọc khẽ gật đầu, ánh mắt cô hướng ra mặt hồ Tây lộng gió, nơi sóng nước đang cuộn trào dưới ánh hoàng hôn đỏ rực.",
    "\"Đêm nay, chúng ta sẽ bắt đầu đột nhập bí mật vào căn nhà cổ để thu thập những bằng chứng khảo cổ cuối cùng trước khi Thịnh Phát ra tay.\"",
    "\"Vương Thế Dũng chắc chắn sẽ không ngồi yên nhìn tôi trì hoãn dự án, hắn sẽ dùng những thủ đoạn đê tiện nhất.\"",
    "\"Cậu phải chuẩn bị tinh thần, cuộc chiến này không chỉ có bàn giấy, mà có thể sẽ đe dọa đến cả tính mạng của cậu đấy.\"",
    "Tuấn khẽ cười lạnh, ánh mắt anh lộ rõ vẻ kiên định vô song: \"Tôi đã chết một lần vào đêm qua rồi, giờ tôi không còn gì để sợ nữa.\"",
    "Hai người chạm chén trà, một liên minh vô hình nhưng vô cùng mạnh mẽ giữa người kiến trúc sư tài hoa và nữ chuyên gia UNESCO chính thức được thiết lập."
]
extra_ch3 = [
    "Hương trà sen Hồ Tây thoang thoảng bay trong không khí, như một làn sinh khí mới thổi vào tâm hồn đầy vết thương của Tuấn.",
    "Anh nhìn những bản phác thảo tay cũ kỹ của mình được Ngọc nâng niu trân trọng, lòng dâng lên một cảm xúc khó tả.",
    "Những kẻ như Hải và Nam nghĩ rằng chúng đã chiến thắng khi cướp đi tờ giấy bản quyền và danh hiệu Kiến trúc sư trưởng.",
    "Nhưng chúng không biết rằng giá trị thực sự của di sản nằm ở tri thức và tình yêu sâu thẳm trong tim người kiến trúc sư bảo tồn.",
    "Ngọc đứng dậy, vạt áo vest đen bay nhẹ trong gió chiều: \"Đi thôi, chiếc xe công vụ của tôi đang chờ ở ngoài đường lớn.\"",
    "\"Chúng ta phải hành động trước khi Hoàng Văn Nam kịp ký lệnh cưỡng chế phá dỡ dưới áp lực của tập đoàn Thịnh Phát.\"",
    "Tuấn đứng dậy theo cô, bước chân anh giờ đây đã trở nên vô cùng vững chãi và tràn đầy tự tin.",
    "Cuộc phản công của chàng kiến trúc sư phố cổ bị cướp bản vẽ chính thức bắt đầu từ buổi chiều lộng gió bên Hồ Tây lịch sử."
]
ch3_sentences.extend(extra_ch3)

novel_data["chapters"].append({
    "title": "Chương 1: Đêm Trắng Phố Gầm Cầu",
    "content": "\n".join([f"<p>{s}</p>" for s in ch1_sentences])
})

novel_data["chapters"].append({
    "title": "Chương 2: Buộc Tội Dưới Ánh Đèn Tràng Thi",
    "content": "\n".join([f"<p>{s}</p>" for s in ch2_sentences])
})

novel_data["chapters"].append({
    "title": "Chương 3: Cuộc Gặp Gỡ Ở Hồ Tây",
    "content": "\n".join([f"<p>{s}</p>" for s in ch3_sentences])
})

# Let's write Stage 1 JSON file to TEMP_PATH
with open(TEMP_PATH, "w", encoding="utf-8") as f:
    json.dump(novel_data, f, ensure_ascii=False, indent=2)

print("Stage 1 completed. Chapters 1-3 written to temp file successfully.")
