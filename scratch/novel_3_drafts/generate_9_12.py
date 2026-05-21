# -*- coding: utf-8 -*-
import json
import os

def save_chapter(chap_num, title, sentences):
    # Form content with <p>...</p>\n for every single sentence
    formatted_content = "".join([f"<p>{s}</p>\n" for s in sentences])
    
    # Calculate word count (splitting by space)
    word_count = sum(len(s.split()) for s in sentences)
    
    data = {
        "title": title,
        "content": formatted_content
    }
    
    filename = f"chap{chap_num}.json"
    filepath = os.path.join(os.path.dirname(__file__), filename)
    
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        
    print(f"✓ Saved Chapter {chap_num} to {filename} ({word_count} words)")
    return word_count

def main():
    # Chapter 9
    chap9_sentences = [
        "Trong căn phòng làm việc rộng lớn tại tầng năm của Viện Thiết kế Giao thông giữa lòng Hà Nội, tiếng mưa giông mùa hạ đập sầm sập vào cửa kính chịu lực nghe buốt nhói.",
        "Lê Khắc Nam đứng chôn chân bên chiếc bàn gỗ lim nguyên khối sang trọng, khuôn mặt xám xịt như tro tàn dưới ánh điện tuýp chập chờn.",
        "Trên màn hình chiếc tivi màn hình cong đắt tiền đang phát sóng bản tin truyền hình khẩn cấp đưa tin về vụ bắt giữ gã thầu phụ Hùng Sắt tại Hải Phòng.",
        "Đôi bàn tay mập mạp đeo chiếc đồng hồ Patek Philippe đắt tiền của lão Viện phó run rẩy kịch liệt khi nghe phát thanh viên dõng dạc đọc quyết định khởi tố tội danh phá hoại công trình quốc gia.",
        "Lão biết rõ rằng Hùng Sắt là quân bài thầu phụ chủ lực do lão cài cắm để thực hiện việc bòn rút cốt thép và hạ mác bê tông từ M400 xuống M250 tại trụ cầu T12.",
        "Bây giờ gã thầu phụ hung hãn đã sa lưới pháp luật, toàn bộ đường dây tham nhũng nghìn tỷ do lão dày công xây dựng đang đứng trước nguy cơ sụp đổ hoàn toàn theo hiệu ứng domino.",
        "Nam lập tức vồ lấy chiếc điện thoại di động Vertu khảm vàng ròng trên bàn, cuống cuồng bấm số điện thoại của vị sếp lớn trong ban chỉ đạo dự án để cầu cứu.",
        "Thế nhưng, đáp lại lão chỉ là những tiếng tút dài vô vọng cùng thông báo thuê bao không liên lạc được vô cùng lạnh lùng.",
        "Lão điên cuồng ném mạnh chiếc điện thoại đắt tiền xuống nền đá hoa cương sáng bóng, tạo ra một tiếng vỡ vụn sắc lạnh vang lên trong phòng.",
        "Ý thức được thời gian không còn nhiều, Nam vội vã quỳ rạp xuống ngăn kéo bí mật dưới gầm bàn làm việc, mở khóa chiếc két sắt ẩn sâu trong hốc tường.",
        "Lão vơ vét tất cả những xấp tiền đô la Mỹ mệnh giá một trăm đô, hàng chục thỏi vàng ròng cùng hai cuốn hộ chiếu ngoại giao nhét đầy vào chiếc vali da cá sấu.",
        "Mồ hôi lạnh vã ra như tắm trên vầng trán hói, chảy ròng ròng xuống cằm và làm ướt sũng cả chiếc áo sơ mi lụa tơ tằm đắt đỏ của lão.",
        "Lão phải bỏ trốn ngay lập tức trước khi lực lượng chức năng phong tỏa các cửa ngõ biên giới đất liền hoặc đường hàng không quốc tế.",
        "Ngay khi Nam vừa kéo khóa chiếc vali da và định quay lưng bước ra phía cửa thoát hiểm bí mật phía sau văn phòng, một tiếng động trầm đục vang lên.",
        "Cánh cửa gỗ lim hai cánh dày nặng của văn phòng bị đẩy mạnh sang hai bên bởi hai người đàn ông cao lớn mặc thường phục với ánh mắt vô cùng sắc lạnh.",
        "Bước vào ngay phía sau họ là Vũ Thanh Lan trong bộ vest công sở màu đen sắc sảo và Hoàng Đức Trung với chiếc áo khoác kỹ sư sạm màu gió biển.",
        "Đi cùng họ là bốn chiến sĩ Cảnh sát Hình sự đeo băng đỏ của Cục Cảnh sát điều tra tội phạm về tham nhũng, kinh tế, buôn lậu C03 dũng mãnh bước vào.",
        "Lê Khắc Nam nhìn thấy Hoàng Đức Trung xuất hiện bên cạnh Thanh Lan thì chiếc vali da cá sấu trên tay lão đột ngột rơi xuống sàn phát ra một tiếng bịch nặng nề.",
        "Lão lảo đảo lùi lại phía sau, lưng đập mạnh vào góc bàn làm việc lim nguyên khối, gương mặt cắt không còn giọt máu.",
        "\"Lê Khắc Nam, ông không cần phải chuẩn bị hành lý cho chuyến đi xa nào nữa đâu,\" Vũ Thanh Lan cất giọng sắc lạnh, đôi mắt phượng đầy sự khinh bỉ tột cùng.",
        "\"Bản thiết kế cải tiến của Đức Trung cùng hệ thống dữ liệu siêu âm chấn động từ chân trụ T12 đã phơi bày toàn bộ tội ác bòn rút của ông ra trước ánh sáng,\" cô dứt khoát tuyên bố.",
        "Đại úy Cảnh sát dẫn đầu đoàn công tác bước lên phía trước, dõng dạc rút ra một văn bản có đóng dấu đỏ chót của Viện Kiểm sát Nhân dân Tối cao.",
        "\"Nhân danh pháp luật, chúng tôi công bố lệnh khởi tố bị can, lệnh bắt tạm giam và khám xét nơi ở, nơi làm việc đối với ông Lê Khắc Nam về tội cố ý làm trái quy định của Nhà nước gây hậu quả nghiêm trọng và tội nhận hối lộ,\" anh đọc to rõ ràng từng từ.",
        "Lê Khắc Nam như bị sét đánh ngang tai, lão quỵ xuống ghế da giám đốc, miệng lẩm bẩm những lời bào chữa vô nghĩa trong cơn hoảng loạn tột độ.",
        "\"Các anh nhầm rồi! Tôi là Viện phó Viện Thiết kế, tôi có đóng góp to lớn cho ngành giao thông vận tải nước nhà suốt ba mươi năm qua!\" lão gào lên trong tuyệt vọng.",
        "\"Bản thiết kế đó chỉ là do tôi điều chỉnh kỹ thuật để tiết kiệm ngân sách cho nhà nước, tôi không hề tư lợi cá nhân hay bòn rút một đồng nào!\" lão ngoan cố chối tội.",
        "Hoàng Đức Trung bước lên một bước, đôi mắt anh trầm mặc nhìn thẳng vào gương mặt già nua và xảo quyệt của gã sếp cũ từng chà đạp lên mình.",
        "\"Tiết kiệm ngân sách bằng cách thay thế bê tông mác cao bằng bê tông giá rẻ pha lẫn tạp chất đất sét tại vị trí xung yếu chịu lực uốn cực hạn dưới biển sao?\" Trung hỏi bằng giọng điệu vô cùng lạnh lùng và đanh thép.",
        "\"Tiết kiệm bằng cách rút bớt bốn mươi phần trăm lượng cáp dự ứng lực cường độ cao chống gió bão giật cấp mười hai sao?\" anh chỉ thẳng vào bản vẽ thiết kế biến đổi đặt trên bàn.",
        "\"Là một kỹ sư xây dựng cầu đường, điều đầu tiên chúng ta được học là sự an toàn tính mạng của người dân ngồi trên nhịp cầu đó,\" Trung nói chậm rãi nhưng vô cùng uy lực.",
        "\"Nhưng ông đã chà đạp lên đạo đức nghề nghiệp tối thiểu, đem tính mạng của hàng vạn người dân ra làm quân bài cá cược cho lòng tham không đáy của mình,\" giọng Trung trầm hùng vang vọng khắp căn phòng.",
        "Lê Khắc Nam nhìn chằm chằm vào Trung, đôi mắt đỏ ngầu sọc máu dâng lên sự căm thù tột độ cùng cực.",
        "\"Mày... tất cả là tại mày! Thằng kỹ sư quèn ranh con! Nếu không có mày vẽ ra cái bản vẽ quỷ quái đó thì tao đã êm đẹp ngồi vào chiếc ghế Viện trưởng rồi!\" lão điên cuồng gào thét.",
        "\"Mày dám phản bội tao, dám cắn ngược lại ân nhân đã nâng đỡ mày vào Viện Thiết kế! Mày sẽ không có kết cục tốt đẹp đâu!\" lão lồng lộn như một con thú bị dồn vào đường cùng.",
        "Đức Trung khẽ thở dài, lắc đầu thương hại cho sự u mê tột cùng của kẻ đứng trước vành móng ngựa.",
        "\"Ông chưa từng nâng đỡ tôi, ông chỉ cướp công sức lao động trí tuệ của tôi để làm bậc thang tiến thân cho bản thân mình,\" anh điềm tĩnh khẳng định.",
        "\"Và hôm nay, lưới trời lồng lộng, tuy thưa nhưng khó lọt, ông phải trả giá trước pháp luật và vong linh của những người công nhân từng ngã xuống vì sự cẩu thả của ông,\" Trung dứt khoát kết luận.",
        "Đại úy cảnh sát ra hiệu cho đồng đội bước lên thực hiện biện pháp cưỡng chế đối với đối tượng ngoan cố.",
        "Hai chiến sĩ cảnh sát nhanh chóng áp sát Lê Khắc Nam, bẻ quặt hai tay lão ra phía sau lưng dưới sự chống cự vô vọng.",
        "Một tiếng cạch khô khốc vang lên khi chiếc còng số tám bằng thép lạnh lẽo khóa chặt hai cổ tay của gã Viện phó hống hách ngày nào.",
        "Toàn bộ vẻ kiêu ngạo, hống hách thường ngày của Lê Khắc Nam biến mất hoàn toàn, chỉ còn lại sự run rẩy, xám ngoét và thảm hại tột cùng của một kẻ tội đồ.",
        "Các chiến sĩ cảnh sát thu giữ chiếc vali chứa đầy đô la và vàng ròng cùng toàn bộ tài liệu dự án liên quan đặt trên bàn làm việc.",
        "Lực lượng chức năng dõng dạc dẫn giải Lê Khắc Nam ra khỏi văn phòng viện phó sang trọng đi dọc hành lang tòa nhà.",
        "Hàng trăm nhân viên, kỹ sư của Viện Thiết kế đứng dạt sang hai bên đường, chứng kiến cảnh tượng gã viện phó quyền lực bị áp giải đi với chiếc còng số tám che dưới vạt áo măng tô.",
        "Nhiều người thầm reo mừng trong lòng vì từ nay Viện Thiết kế đã trút bỏ được một kẻ độc tài tham lam chuyên cướp công và đì đọa cấp dưới.",
        "Vũ Thanh Lan đứng bên cạnh Đức Trung nhìn chiếc xe cảnh sát chuyên dụng hú còi inh ỏi từ từ lăn bánh rời khỏi cổng Viện Thiết kế giao thông.",
        "Cô quay sang nhìn Trung, đôi mắt phượng ngập tràn ánh nắng ấm áp của sự tin cậy và khâm phục tuyệt đối.",
        "\"Trung, chúng ta đã đưa được kẻ ác ra trước công lý, công trình cầu vượt biển từ nay đã sạch bóng những kẻ tham nhũng,\" cô khẽ nói.",
        "\"Nhưng phía trước chúng ta là nhịp cầu hợp long quyết định, tôi cần anh tập trung toàn bộ trí lực để hoàn thành siêu dự án này một cách an toàn nhất,\" cô gửi gắm niềm tin.",
        "Đức Trung nhìn chiếc xe cảnh sát khuất dần sau làn mưa giông Hà Nội, đôi mắt anh rực sáng ý chí sắt đá kiên định.",
        "\"Tôi sẽ không phụ lòng tin của cô và hàng triệu người dân Hải Phòng đang mong chờ cây cầu vượt biển lịch sử này hoàn thành hoàn hảo từng nhịp,\" anh cam kết dứt khoát.",
        "Hai người cùng bước đi bên nhau dưới làn mưa mùa hạ, lòng tràn đầy quyết tâm hướng về phía công trường cầu vượt biển Tân Vũ - Lạch Huyện đang bước vào giai đoạn quyết định.",
        "Cơn bão lòng trong Đức Trung đã hoàn toàn lắng xuống, thay vào đó là một sự thanh thản và ý chí quyết chiến mãnh liệt.",
        "Anh biết rằng kẻ thù lớn nhất không phải là Lê Khắc Nam hay Hùng Sắt, mà chính là những thử thách khốc liệt của tự nhiên ngoài đại dương xanh thẳm.",
        "Những nhịp cầu dầm thép khổng lồ đang đợi bàn tay anh căn chỉnh, những khối bê tông mác siêu cao đang đợi anh thổi hồn sức mạnh.",
        "Thanh Lan nhìn nghiêng gương mặt điềm tĩnh đầy phong trần của anh dưới mưa giông, trong lòng cô dâng lên một cảm xúc thiêng liêng khó tả.",
        "Cô tự hứa với lòng mình sẽ dùng toàn bộ nguồn lực tài chính và tầm ảnh hưởng của tổng công ty VEC để bảo vệ anh đến cùng trên con đường chinh phục ước mơ kỹ nghệ.",
        "Mưa giông Hà Nội trút xuống xối xả như muốn gột rửa sạch sẽ những vết nhơ tham nhũng bẩn thỉu tích tụ suốt nhiều năm qua tại công trình.",
        "Tiếng còi xe tuần tra nhỏ dần trong tiếng mưa giông gào thét, báo hiệu một thời kỳ mới, thời kỳ của những giá trị kỹ thuật thực chất và minh bạch lên ngôi.",
        "Bức tranh toàn cảnh về đại lộ cao tốc vượt biển nghìn tỷ đang tiến gần hơn tới vạch đích hoàn hảo nhờ có bàn tay thiết kế thiên tài của Đức Trung.",
        "Anh không còn là một kỹ sư bị sa thải trong nhục nhã, mà đã trở thành linh hồn thiêng liêng nhất dẫn dắt cả siêu dự án trọng điểm quốc gia.",
        "Đêm nay, anh sẽ lập tức trở lại Hải Phòng, trực tiếp túc trực trên sàn đạo thi công để chuẩn bị cho chiến dịch hợp long mang tính lịch sử.",
        "Từng thông số thủy văn chịu lực, từng dự báo sức gió trên vịnh Bắc Bộ đã được anh cập nhật chi tiết vào bộ vi xử lý máy tính cá nhân.",
        "Sự chuẩn bị kỹ lưỡng của một bộ óc thiên tài điềm tĩnh luôn là chìa khóa vạn năng đè bẹp mọi bất trắc của tự nhiên.",
        "Hai bóng người, một cao lớn vững chãi, một mảnh mai sắc sảo, cùng che chung một chiếc ô đen, khuất dần vào làn mưa mù mịt hướng về phía tương lai rực rỡ.",
        "Lưới trời lồng lộng đã sa lưới Lê Khắc Nam, và giờ đây, chân lý cùng công nghệ đỉnh cao sẽ chính thức hợp nhất làm một trên biển lớn Hải Phòng."
    ]

    # Chapter 10
    chap10_sentences = [
        "Sương sớm mù mịt trên vịnh Bắc Bộ bắt đầu tan dần dưới những tia nắng vàng nhạt đầu tiên của một ngày mùa thu lộng gió.",
        "Trên công trường cầu vượt biển Tân Vũ - Lạch Huyện, không khí thi công nhộn nhịp và khẩn trương đạt đến mức độ đỉnh điểm chưa từng có.",
        "Hôm nay là ngày hợp long nhịp cầu chính vượt biển dài hai trăm mét - nhịp cầu dầm hộp bê tông cốt thép dự ứng lực đúc hẫng cân bằng lớn nhất Việt Nam.",
        "Hàng chục chiếc sà lan cẩu khổng lồ công suất hàng nghìn tấn và các tàu kéo công vụ được bố trí nghiêm ngặt xung quanh khu vực luồng hàng hải sâu.",
        "Hoàng Đức Trung đứng sừng sững trên đỉnh tháp trụ cầu T12 ở độ cao hơn năm mươi mét so với mực nước biển, luồng gió lộng thổi mạnh làm tạt chiếc mũ bảo hộ màu trắng của anh.",
        "Ánh mắt anh bình thản nhưng cực kỳ tập trung, liên tục đối chiếu các thông số kỹ thuật trên bản vẽ thiết kế gốc đúp trên bảng điều khiển điện tử cầm tay.",
        "Khối hợp long chính giữa nhịp cầu ký hiệu KN10 chỉ dài vỏn vẹn hai mét, nhưng nó là điểm kết nối sống còn quyết định toàn bộ khả năng chịu lực liên tục của siêu kết cấu.",
        "Nếu quá trình thi công không đạt độ chính xác tuyệt đối, hiện tượng lệch cao độ giữa hai đầu hẫng đúc từ mố T11 và mố T12 sẽ bẻ gãy nhịp cầu ngay khi căng kéo cáp dự ứng lực.",
        "Sai số cho phép theo tiêu chuẩn AASHTO quốc tế đối với nhịp cầu đúc hẫng quy mô này chỉ nằm trong khoảng cộng trừ năm milimet.",
        "Thế nhưng, Đức Trung tự đặt ra cho bản thân và đội ngũ kỹ sư một mục tiêu khắt khe hơn gấp mười lần: sai số không được vượt quá không phẩy năm milimet.",
        "\"Báo cáo kỹ sư trưởng, nhiệt độ khí quyển hiện tại là hai mươi bốn độ C, độ ẩm tám mươi phần trăm, tốc độ gió đạt năm mét trên giây,\" tiếng một kỹ sư trẻ vang lên qua bộ đàm.",
        "\"Cao độ đầu hẫng mố T11 đang cao hơn đầu hẫng mố T12 là ba milimet do tác động giãn nở nhiệt của ánh nắng mặt trời chiếu không đều,\" cậu báo cáo lo lắng.",
        "Đức Trung đưa tay điều chỉnh tần số bộ đàm, giọng nói trầm ấm và điềm tĩnh của anh vang lên truyền đi sự tự tin vững chãi cho toàn công trường.",
        "\"Mọi người không cần lo lắng! Hiện tượng giãn nở nhiệt không đều này hoàn toàn nằm trong thuật toán dự báo biến dạng kết cấu của tôi,\" anh ôn tồn giải thích.",
        "\"Chúng ta sẽ trì hoãn việc đổ bê tông hợp long cho đến đúng bốn giờ sáng mai, khi nhiệt độ bê tông và dầm thép đạt trạng thái cân bằng nhiệt hoàn hảo nhất,\" Trung ra lệnh dứt khoát.",
        "\"Trong thời gian chờ đợi, lập tức bơm nước tải trọng cân bằng vào các khoang dầm T12 để điều chỉnh độ lệch cao độ về mức không phẩy hai milimet,\" anh chỉ đạo chi tiết.",
        "Vũ Thanh Lan đứng cạnh anh trên sàn đạo thi công, mái tóc đen dài cột cao đung đưa trước gió biển mặn mòi, đôi mắt cô lấp lánh sự ngưỡng mộ vô bờ bến.",
        "Cô mặc chiếc áo khoác phản quang màu cam nổi bật trên nền trời xanh, tay cầm chiếc cặp chứa hồ sơ nghiệm thu kỹ thuật của hội đồng nhà nước.",
        "\"Đức Trung, quyết định lùi thời gian đổ bê tông sang bốn giờ sáng quả thực là một nước đi dũng cảm và cực kỳ khoa học của anh,\" Lan mỉm cười sắc sảo.",
        "\"Ban quản lý dự án ban đầu rất sốt ruột đòi đổ ngay trong chiều nay để lấy thành tích kịp tiến độ bàn giao,\" cô tiết lộ áp lực từ các sếp phía trên.",
        "\"Nhưng tôi đã dùng uy tín của mình để bác bỏ hoàn toàn ý kiến đó, bảo vệ phương án kỹ thuật an toàn tuyệt đối của anh đến cùng,\" cô dịu dàng nói.",
        "Đức Trung quay đầu nhìn cô, ánh mắt anh ngập tràn sự biết ơn sâu sắc dành cho người phụ nữ thông minh đã luôn đồng hành cùng mình vượt qua giông bão.",
        "\"Cảm ơn cô, Thanh Lan. Nếu không có sự thấu hiểu và kiên định của cô, một kỹ sư chỉ biết kỹ thuật như tôi sẽ rất khó chống lại những áp lực hành chính máy móc ngoài kia,\" anh chân thành chia sẻ.",
        "Đêm dần buông xuống trên vịnh biển Hải Phòng, mặt biển phẳng lặng như tờ phản chiếu hàng nghìn ánh đèn cao áp sáng rực từ công trường cầu vượt biển sừng sững.",
        "Không một ai đi ngủ, hàng trăm công nhân và kỹ sư trực tiếp túc trực tại vị trí chiến đấu của mình, mắt hướng về phía nhịp cầu chính khổng lồ đang đợi hợp long.",
        "Đúng ba giờ bốn mươi phút sáng, nhiệt độ không khí giảm xuống mức thấp nhất và ổn định hoàn toàn ở ngưỡng mười chín độ C.",
        "Hệ thống máy đo laser khoảng cách kết nối cảm biến sợi quang gắn dọc thân dầm cầu đồng loạt phát tín hiệu màu xanh lục trên máy tính chỉ huy.",
        "Độ lệch cao độ giữa hai đầu cầu đúc hẫng mố T11 và T12 chính thức co về mức không phẩy một milimet - một thông số chính xác đến mức kinh ngạc.",
        "\"Tất cả các bộ phận chú ý! Bắt đầu đổ bê tông hợp long nhịp chính cầu vượt biển Tân Vũ - Lạch Huyện!\" Đức Trung dõng dạc ra lệnh qua hệ thống loa cầm tay.",
        "Tiếng động cơ của hai chiếc xe bơm bê tông công suất lớn đặt trên sà lan bắt đầu gầm rú dữ dội, xua tan màn đêm tĩnh lặng của vịnh biển.",
        "Hỗn hợp bê tông siêu tính năng UHPC cường độ mác cao, pha trộn phụ gia nano silica chống thấm nước mặn bắt đầu chảy cuồn cuộn vào khuôn đúc khối hợp long KN10.",
        "Trung trực tiếp trèo xuống lồng thép chật hẹp của khối hợp long, bàn tay chỉ huy nhịp nhàng các công nhân sử dụng máy đầm dùi rung tần số cao.",
        "Anh chú ý tỉ mỉ đến từng chi tiết nhỏ nhất, đảm bảo bê tông UHPC len lỏi đều khắp qua mật độ cốt thép dày đặc mà không để lại bất kỳ bọt khí hay vết nứt ngầm nào.",
        "Mồ hôi hòa lẫn với sương đêm lạnh buốt chảy ròng ròng trên má anh, nhưng đôi mắt anh vẫn rực sáng một niềm tin mãnh liệt vào sự hoàn hảo của công nghệ.",
        "Thanh Lan đứng trên sàn cầu công vụ sát bên cạnh lồng thép, cô im lặng dõi theo từng động tác của anh, trái tim đập liên hồi vì hồi hộp tột độ.",
        "Sau hơn ba tiếng đồng hồ làm việc liên tục dưới áp lực nghẹt thở của toàn bộ hệ thống kỹ thuật, mẻ bê tông hợp long cuối cùng đã được đổ đầy và hoàn thiện bề mặt hoàn hảo.",
        "Khi những giọt bê tông cuối cùng được san phẳng, cả công trường đột ngột im lặng trong vài giây rồi đồng loạt vỡ òa trong tiếng reo hò vang dội khắp cả vùng biển.",
        "Nhịp cầu vượt biển Tân Vũ - Lạch Huyện chính thức được hợp nhất làm một dải liên tục, sừng sững nối liền đảo cát Hải Phòng với đất liền rộng lớn.",
        "Cùng lúc đó ngoài khơi xa, mặt trời đỏ rực bắt đầu nhô lên từ đường chân trời biển cả, nhuộm hồng toàn bộ nhịp cầu thế kỷ vĩ đại.",
        "Còi của hàng chục con tàu container và tàu kéo neo đậu dưới luồng hàng hải đồng loạt rú vang rộn rã tạo nên một khúc nhạc chiến thắng vô cùng hào hùng.",
        "Thanh Lan không kìm nổi sự xúc động tột cùng, cô chạy nhanh tới bên cạnh Đức Trung, đôi mắt phượng ngập tràn những giọt lệ hạnh phúc long lanh dưới ánh bình minh.",
        "\"Đức Trung! Chúng ta đã làm được rồi! Nhịp cầu thế kỷ đã chính thức hợp lòng hoàn hảo rồi!\" cô nghẹn ngào hét lớn trong niềm vui sướng tột độ.",
        "Đức Trung tháo chiếc găng tay kỹ thuật sũng nước đầm, anh nhìn nhịp cầu sừng sững kéo dài tít tắp ra biển khơi xa với một nụ cười rạng rỡ và mãn nguyện nhất từ trước đến nay.",
        "Anh quay sang nhìn Thanh Lan, người con gái sắc sảo kiên định đã cùng anh đi qua bao thăng trầm nghiệt ngã của cuộc đời kỹ sư.",
        "\"Vâng, Thanh Lan. Nhịp cầu này không chỉ nối liền hai vùng đất, mà nó còn chứng minh cho cả thế giới thấy rằng trí tuệ và sự trung thực của kỹ sư Việt Nam có thể chinh phục được đại dương,\" anh dứt khoát khẳng định.",
        "Tiếng vỗ tay và reo hò của hàng trăm kỹ sư công nhân vẫn vang vọng không ngớt trên công trường lộng gió đại dương Hải Phòng.",
        "Bình minh rực rỡ chiếu sáng lên nhịp cầu bê tông UHPC xám trắng, một kiệt tác kỹ nghệ cầu đường vượt biển nghìn tỷ chính thức được định hình sừng sững giữa đất trời.",
        "Chiến thắng huy hoàng này là cái tát đanh thép nhất đập tan hoàn toàn những nghi ngờ, đố kỵ và âm mưu phá hoại đen tối của những kẻ tham lam.",
        "Đức Trung đứng bên cạnh Thanh Lan dưới ánh bình minh lộng lẫy, cảm nhận được hơi ấm và sức mạnh mãnh liệt của tình yêu công nghệ và sự thật đang lan tỏa khắp cơ thể.",
        "Hành trình đầy chông gai từ một kỹ sư bị sa thải oan ức đến vị tổng công trình sư thiên tài của siêu dự án vượt biển đã đi đến vạch đích vinh quang nhất.",
        "Những nhịp cầu dẫn tít tắp, những tháp trụ sừng sững, tất cả đều mang đậm dấu ấn tư duy độc bản và ý chí sắt đá của Hoàng Đức Trung.",
        "Hải Phòng lộng gió sáng nay đẹp hơn bao giờ hết, chào đón sự ra đời của một kỳ tích kỹ thuật mang tầm vóc lịch sử quốc gia.",
        "Tập đoàn VEC và cá nhân Thanh Lan đã chứng minh được tầm nhìn chiến lược vĩ đại khi đặt trọn niềm tin vào tài năng vô song của Trung.",
        "Con đường cao tốc vượt biển nghìn tỷ giờ đây đã không còn là một giấc mơ xa vời trên bản vẽ bị đánh cắp, mà đã hiện hữu bằng xương bằng thịt, vững chãi trước sóng gió đại dương.",
        "Đức Trung nhìn ra khơi xa, lòng anh tràn ngập những hoài bão mới về những cung đường cao tốc Bắc-Nam rộng mở, những nhịp cầu vượt sông lớn trên khắp quê hương đang đợi anh kiến tạo.",
        "Anh khẽ nắm lấy tay Thanh Lan, đôi bàn tay chai sần vì nắng gió công trường siết nhẹ lấy bàn tay mềm mại ấm áp của cô.",
        "Lan đỏ mặt nhưng không hề rụt tay lại, cô tựa nhẹ đầu vào vai anh, cùng anh nhìn về phía tương lai tươi sáng của ngành cầu đường Việt Nam đang mở ra rực rỡ."
    ]

    # Chapter 11
    chap11_sentences = [
        "Hoàng hôn buông xuống trên cảng biển Hải Phòng mang theo một vẻ đẹp lộng lẫy, tráng lệ đến ngộp thở của vùng đất đầu sóng ngọn gió.",
        "Bầu trời phía tây rực cháy một màu đỏ cam pha lẫn tím thẫm, phản chiếu những vệt sáng lấp lánh xuống mặt nước biển rộng lớn bao la.",
        "Mặt đường nhựa polymer mác cao trên nhịp cầu chính vượt biển Tân Vũ - Lạch Huyện đã hoàn thành hoàn hảo, phẳng lỳ như một dải lụa đen mịn màng trải dài vô tận.",
        "Hệ thống lan can bảo vệ bằng thép mạ kẽm nhúng nóng sáng loáng chạy dọc hai bên cầu, lấp lánh dưới ánh nắng chiều tà cuối ngày ấm áp.",
        "Hoàng Đức Trung bước đi chậm rãi trên làn đường đi bộ dọc thành cầu, đôi bàn tay phong trần đút sâu vào túi chiếc quần kaki sẫm màu lộng gió.",
        "Gió biển thổi mạnh, làm bay nhẹ vạt áo sơ mi xanh thẫm sạm màu nắng gió công trường của vị tổng công trình sư thiên tài.",
        "Bên cạnh anh, Vũ Thanh Lan thướt tha bước đi trong chiếc váy dạ hội đơn giản màu xanh ngọc bích, tôn lên vóc dáng mảnh mai và gương mặt sắc sảo vô cùng quý phái.",
        "Gió đại dương thổi tung mái tóc đen dài mềm mại của cô, mang theo hương vị mặn mòi của muối biển pha lẫn mùi nước hoa dịu nhẹ thanh lịch.",
        "Họ vừa trải qua một ngày nghiệm thu kỹ thuật căng thẳng và thành công rực rỡ với đoàn kiểm tra liên ngành của Bộ Giao thông Vận tải.",
        "Giờ đây, khi công trường tạm lắng xuống để chuẩn bị cho đại lễ khánh thành ngày mai, hai người mới có được những giây phút tĩnh lặng hiếm hoi bên nhau.",
        "\"Trung này, anh có biết cảm giác của tôi lúc này là gì không?\" Thanh Lan khẽ dừng bước, nghiêng đầu nhìn anh bằng đôi mắt phượng lấp lánh dưới ánh hoàng hôn.",
        "Đức Trung đứng lại bên cạnh cô, tay vịn nhẹ vào thành lan can thép bảo vệ mát lạnh, đôi mắt anh trầm mặc nhìn ra phía những con tàu container khổng lồ đang từ từ cập cảng Lạch Huyện đằng xa.",
        "\"Tôi đoán là cô đang cảm thấy trút bỏ được một gánh nặng khổng lồ sau hàng tháng trời chịu áp lực tài chính và pháp lý từ dự án này,\" Trung ôn tồn trả lời, giọng nói ấm áp trầm lặng quen thuộc.",
        "Thanh Lan lắc đầu nhẹ, một nụ cười rạng rỡ đầy nữ tính hiện lên trên gương mặt sắc sảo thường ngày vốn rất nghiêm nghị của vị Phó Tổng Giám đốc VEC.",
        "\"Đó chỉ là một phần rất nhỏ thôi, Đức Trung ạ,\" cô khẽ thở dài đầy nhẹ nhõm, ánh mắt nhìn sâu vào đôi mắt sâu thẳm của anh.",
        "\"Cảm giác lớn nhất của tôi lúc này là sự tự hào tột cùng và lòng biết ơn sâu sắc đối với một người đàn ông kỳ diệu,\" cô chân thành thổ lộ.",
        "\"Người đàn ông đó đã xuất hiện đúng vào lúc tôi tuyệt vọng nhất, dùng chính đôi vai vững chãi và bộ óc thiên tài của mình để cứu vớt cả siêu dự án này khỏi vực thẳm sụp đổ,\" giọng cô nhỏ dần, chứa đựng những rung động mãnh liệt từ trái tim.",
        "Đức Trung khựng lại một nhịp, lồng ngực anh bỗng dâng lên một luồng cảm xúc ấm áp khó tả trước những lời gan ruột của Thanh Lan.",
        "\"Lan, tôi mới là người phải cảm ơn cô,\" anh quay hẳn người lại đối diện với cô, giọng nói đầy sự nghiêm túc và xúc động chân thành.",
        "\"Nếu không có sự dũng cảm vô song của cô khi dám đứng ra bảo lãnh cho một kỹ sư bị sa thải, bị mang tiếng xấu như tôi lúc đó, tôi đã không có cơ hội đứng đây ngày hôm nay,\" Trung nói, đôi mắt anh rực sáng lên niềm tin.",
        "\"Chính cô đã trả lại sự trong sạch cho bản vẽ của tôi, trao cho tôi quyền tự quyết cao nhất ngoài thực địa để tôi có thể hiện thực hóa những tính toán UHPC độc bản của mình,\" anh khẳng định chắc nịch.",
        "Thanh Lan khẽ mỉm cười, bước lại gần anh hơn một chút, khoảng cách giữa hai người giờ đây chỉ còn tính bằng gang tay dưới ánh hoàng hôn tím hồng.",
        "\"Hôm nay, Bộ trưởng đã trực tiếp trao đổi với tôi về phương án nhân sự sắp tới cho Viện Thiết kế Giao thông miền Bắc,\" Lan ngước nhìn anh, giọng cô có chút hồi hộp.",
        "\"Ghế Viện trưởng hiện đang bỏ trống sau khi Lê Khắc Nam bị bắt giam chờ ngày xét xử tội tham nhũng bòn rút,\" cô giải thích.",
        "\"Bộ muốn bổ nhiệm anh trực tiếp vào chiếc ghế Viện trưởng đó, để anh toàn quyền dẫn dắt lực lượng thiết kế giao thông đầu não của cả nước,\" cô đưa ra lời đề nghị vô cùng danh giá.",
        "\"Ý anh thế nào, Đức Trung? Anh sẽ đồng ý trở lại thủ đô để nhận vị trí quyền lực tối cao đó chứ?\" Lan chăm chú chờ đợi câu trả lời từ anh.",
        "Đức Trung im lặng nhìn ngắm ánh hoàng hôn đang lịm dần phía chân trời xa, tạo nên những mảng màu tối sáng đan xen trên vịnh biển khơi.",
        "Một nụ cười nhẹ nhàng, bình thản hiện lên trên gương mặt sạm nắng gió phong trần đầy nam tính của anh.",
        "\"Cảm ơn sự tín nhiệm của Bộ và cá nhân cô, Thanh Lan. Nhưng tôi xin phép từ chối chiếc ghế Viện trưởng sang trọng đó,\" anh điềm tĩnh trả lời.",
        "Thanh Lan ngạc nhiên tròn mắt nhìn anh, cô không ngờ một kỹ sư từng bị đì đọa lại có thể từ chối một cơ hội thăng tiến quyền lực tột đỉnh mà hàng nghìn người mơ ước như vậy.",
        "\"Tại sao vậy, Trung? Đó là cơ hội tốt nhất để anh khẳng định vị thế và trực tiếp thay đổi toàn bộ hệ thống thiết kế giao thông nước nhà từ gốc rễ mà?\" cô vội vàng hỏi.",
        "Đức Trung lắc đầu khẽ, đôi bàn tay anh đưa lên vuốt nhẹ vào một mối hàn thép trên thành cầu công trình.",
        "\"Vị trí của tôi không nằm trong những căn phòng máy lạnh sang trọng ở thủ đô Hà Nội, Lan ạ,\" anh giải thích bằng giọng trầm ấm đầy lý tưởng nghề nghiệp.",
        "\"Vị trí của tôi là ở đây, ngoài thực địa lộng gió biển, nơi những mẻ bê tông UHPC đang đông cứng, nơi những mũi khoan hầm đang xuyên qua lòng núi sâu,\" anh rực sáng ý chí kỹ nghệ.",
        "\"Tôi muốn dành trọn cuộc đời mình để trực tiếp thiết kế và chỉ huy xây dựng những nhịp cầu vượt biển khổng lồ, những đường hầm xuyên đèo khốc liệt, những tuyến đường sắt tốc độ cao dọc chiều dài đất nước,\" Trung dõng dạc chia sẻ hoài bão lớn.",
        "\"Đó mới chính là lẽ sống, là niềm đam mê cháy bỏng nhất của một kỹ sư cầu đường chân chính như tôi,\" anh dứt khoát kết luận.",
        "Thanh Lan lặng người đi trước câu trả lời đầy khí phách và lý tưởng cao đẹp của Đức Trung.",
        "Sự khâm phục và yêu mến trong lòng cô dành cho người đàn ông này lại tăng lên gấp bội, vượt lên trên cả mối quan hệ đồng nghiệp hay đối tác thông thường.",
        "\"Anh thực sự là một kẻ gàn dở đáng kính nhất mà tôi từng gặp trong đời, Hoàng Đức Trung,\" Lan khẽ cười, đôi mắt phượng lấp lánh nước mắt xúc động ngọt ngào.",
        "\"Nhưng chính sự gàn dở đầy kiêu hãnh đó của anh đã khiến tôi hoàn toàn gục ngã và không thể ngừng tin tưởng vào anh,\" cô dịu dàng nói, gương mặt thanh tú khẽ ửng hồng dưới ánh chiều tà.",
        "Đức Trung nhìn gương mặt xinh đẹp rạng rỡ của Thanh Lan dưới ánh hoàng hôn tím mộng mơ, trái tim stoic sắt đá của anh bỗng đập liên hồi dữ dội.",
        "Anh không ngần ngại bước lên một bước ngắn, khoảng cách giữa hai người hoàn toàn biến mất dưới luồng gió biển lộng lẫy.",
        "Đôi bàn tay sạm nắng phong trần của Trung khẽ đưa lên, nhẹ nhàng và trân trọng nắm lấy hai bàn tay mềm mại ấm áp đang run nhẹ của Thanh Lan.",
        "\"Thanh Lan, hành trình xây dựng những cung đường cao tốc và cầu vượt biển tiếp theo của tôi sẽ rất gian khổ và đầy giông bão khốc liệt,\" Trung nhìn thẳng vào mắt cô, giọng nói chứa chan tình cảm sâu kín nhất.",
        "\"Nhưng tôi mong rằng, trên mỗi nhịp cầu mới mà tôi xây dựng trên khắp quê hương Việt Nam này, sẽ luôn có bóng dáng của cô đi cùng tôi,\" anh chân thành bày tỏ tấm lòng.",
        "\"Cô có đồng ý đồng hành cùng tôi trên con đường chinh phục những đỉnh cao kỹ nghệ mới đầy thử thách phía trước không?\" Trung run run hỏi, chờ đợi quyết định từ cô gái.",
        "Thanh Lan nhìn sâu vào đôi mắt đầy kiên định và ấm áp của Trung, giọt nước mắt hạnh phúc tích tụ bấy lâu cuối cùng cũng lăn dài trên má cô lấp lánh.",
        "Cô khẽ gật đầu dứt khoát, siết chặt lấy đôi bàn tay chai sần vững chãi của người đàn ông thiên tài trước mặt.",
        "\"Em đồng ý, Đức Trung. Dù anh có đi xây cầu ở bất kỳ vùng biển khơi xa xôi hay đỉnh núi hiểm trở nào, em cũng sẽ luôn là hậu phương vững chắc nhất bên cạnh anh,\" cô dịu dàng xưng em đầy ngọt ngào.",
        "Dưới ánh hoàng hôn tráng lệ nhuộm tím cả vịnh biển Hải Phòng, hai người đứng bên nhau trên nhịp cầu vượt biển nghìn tỷ vĩ đại.",
        "Họ khẽ trao nhau một cái ôm ấm áp và trọn vẹn nhất giữa tiếng gió đại dương gào thét phóng khoáng.",
        "Nhịp cầu thế kỷ sừng sững dưới chân họ, như một minh chứng thiêng liêng nhất cho tình yêu đôi lứa hòa quyện cùng lý tưởng cống hiến vĩ đại của tuổi trẻ Việt Nam.",
        "Ánh đèn cao áp dọc thân cầu bắt đầu đồng loạt bật sáng rực rỡ, kết nối thành một dải ngân hà lung linh vắt qua biển khơi rộng lớn.",
        "Con đường cao tốc phía trước đã mở ra, rộng thênh thang và tràn ngập ánh sáng của hạnh phúc và vinh quang tột đỉnh đang đợi họ cùng nhau bước tiếp.",
        "Cảng Hải Phòng đêm nay lung linh huyền ảo, tiếng còi tàu vang vọng như một lời chúc phúc ngọt ngào cho mối tình chín muồi giữa thiên tài cầu đường và nữ phó tổng giám đốc sắc bén.",
        "Họ đã cùng nhau vượt qua bão táp thiên nhiên và những âm mưu đen tối của lòng tham con người để tạo nên một kỳ tích xây dựng chấn động cả nước.",
        "Và giờ đây, một trang mới đầy tự hào của cuộc đời họ chính thức bắt đầu dưới ánh sao đêm lấp lánh trên biển lớn quê hương."
    ]

    # Chapter 12
    chap12_sentences = [
        "Đại lễ khánh thành cầu vượt biển Tân Vũ - Lạch Huyện nghìn tỷ được diễn ra vào một buổi sáng mùa thu trời cao trong xanh vô cùng lộng lẫy.",
        "Hàng vạn lá cờ đỏ sao vàng tung bay phấp phới dọc theo toàn bộ chiều dài hơn năm km của siêu công trình vượt biển lịch sử này.",
        "Hàng trăm lẵng hoa tươi rực rỡ sắc màu được xếp trang trọng dọc hai bên sân lễ chính đặt ngay tại mố cầu dẫn phía bờ Hải Phòng.",
        "Hàng vạn người dân từ khắp nơi trong thành phố Hải Phòng và huyện đảo Cát Hải đã đổ về từ sáng sớm, gương mặt ai nấy đều rạng rỡ niềm vui sướng hân hoan tột cùng.",
        "Hàng chục đài truyền hình, cơ quan thông tấn báo chí lớn trong nước và quốc tế túc trực đông đảo, ống kính máy quay hướng về phía lễ đài chính.",
        "Hoàng Đức Trung đứng ở hàng ghế danh dự hàng đầu bên cạnh Vũ Thanh Lan dưới ánh nắng sớm rực rỡ chan hòa.",
        "Hôm nay, anh không mặc chiếc áo khoác kỹ sư sạm màu bụi bặm thường ngày nữa, mà diện một bộ vest màu xanh navy sang trọng do chính tay Thanh Lan lựa chọn tỉ mỉ.",
        "Bộ vest cắt may thủ công chuẩn xác tôn lên vóc dáng cao lớn, bờ vai rộng vững chãi và gương mặt cương nghị, phong trần đầy nam tính của anh.",
        "Thanh Lan đứng bên cạnh anh trong tà áo dài truyền thống màu đỏ thắm thêu hoa sen vàng tinh xảo, gương mặt sắc sảo trang điểm nhẹ nhàng toát lên vẻ đẹp đài các, kiêu sa của một nữ lãnh đạo xuất chúng.",
        "Đôi mắt phượng của cô thỉnh thoảng lại quay sang nhìn Trung đầy sự tự hào và yêu thương ngọt ngào không thể giấu kín.",
        "Tiếng nhạc nghi lễ hào hùng vang lên rộn rã, MC dõng dạc tuyên bố bắt đầu chương trình lễ khánh thành siêu công trình quốc gia.",
        "Vị Phó Thủ tướng Chính phủ đại diện ban lãnh đạo nhà nước bước lên bục phát biểu trước hàng vạn người dân đang chú ý lắng nghe.",
        "Giọng ông trầm hùng, dõng dạc vang vọng qua hệ thống loa công suất lớn truyền đi khắp công trường lộng gió.",
        "\"Cây cầu vượt biển Tân Vũ - Lạch Huyện hoàn thành ngày hôm nay là một kỳ tích lịch sử, một biểu tượng vĩ đại cho ý chí và sức mạnh sáng tạo vô song của con người Việt Nam,\" ông nhấn mạnh đầy tự hào.",
        "\"Chúng ta đã vượt qua những thử thách khốc liệt nhất của thiên tai, đè bẹp những khó khăn thách thức về mặt kỹ thuật công nghệ bằng chính khối óc và bàn tay của mình,\" vị lãnh đạo phát biểu.",
        "\"Đặc biệt, Chính phủ ghi nhận và biểu dương tinh thần kiên cường, sự trung thực và chuyên môn siêu phàm của đội ngũ kỹ sư thiết kế và thi công dự án,\" ông dõng dạc tuyên bố trước toàn thể hội trường.",
        "\"Trong đó, chúng ta phải vinh danh Hoàng Đức Trung - người kỹ sư trẻ tuổi thiên tài, linh hồn của toàn bộ giải pháp công nghệ bê tông siêu tính năng UHPC độc bản cứu vớt siêu dự án này,\" giọng Phó Thủ tướng đanh thép vang lên.",
        "Cả khán đài đột ngột im lặng trong một giây rồi đồng loạt vỡ òa trong tiếng vỗ tay rầm rộ như sấm dậy kéo dài không ngớt.",
        "Hàng vạn người dân Hải Phòng đồng loạt đứng dậy reo hò vang dội, gọi tên Hoàng Đức Trung đầy sự ngưỡng mộ và lòng biết ơn sâu sắc.",
        "Vũ Thanh Lan xúc động tột cùng, cô quay sang nhìn Trung, hai mắt nhòe lệ hạnh phúc, khẽ siết chặt lấy bàn tay anh dưới hàng ghế đại biểu.",
        "Hoàng Đức Trung đứng dậy, anh cúi đầu chào ban lãnh đạo nhà nước và toàn thể nhân dân bằng một sự điềm tĩnh và khiêm nhường quen thuộc của một thiên tài thực thụ.",
        "Phó Thủ tướng dõng dạc mời Đức Trung bước lên bục danh dự để trao tặng Huân chương Lao động hạng Nhì của Chủ tịch nước dành cho những cống hiến đặc biệt xuất sắc của anh.",
        "Tấm huy chương vàng óng lấp lánh dưới ánh nắng thu rực rỡ được đính trang trọng lên ngực áo vest của vị tổng công trình sư trẻ tuổi.",
        "Tiếng còi của hàng trăm tàu biển container neo đậu dưới luồng hàng hải Hải Phòng đồng loạt rú vang rộn rã, hòa cùng tiếng pháo hoa rực rỡ nổ vang trên bầu trời xanh thẳm.",
        "Khoảnh khắc dải băng đỏ khánh thành được cắt đứt, đoàn xe dẫn đầu là chiếc Limousine chở các vị lãnh đạo từ từ lăn bánh qua cầu vượt biển lịch sử.",
        "Hàng vạn người dân Hải Phòng ùa ra dọc thành cầu, nhiều cụ già đã bật khóc nức nở vì từ nay con cháu họ không còn phải chịu cảnh đò ngang cách trở nguy hiểm giữa sóng gió đại dương nữa.",
        "Đồng thời, trên chiếc màn hình led khổng lồ của sân lễ đang phát sóng trực tiếp bản tin thời sự trưa đưa tin về vụ xét xử sơ thẩm vụ án tham nhũng tại dự án.",
        "Lê Khắc Nam bị tuyên án hai mươi năm tù giam về tội cố ý làm trái gây hậu quả nghiêm trọng và nhận hối lộ, tài sản bòn rút hàng trăm tỷ đồng bị tịch thu hoàn toàn.",
        "Gã thầu phụ hung hãn Hùng Sắt cũng phải nhận mức án mười tám năm tù giam thích đáng sau những hành vi phá hoại cố ý bị bắt quả tang.",
        "Hình ảnh hai kẻ tội đồ mặt xám ngoét cúi đầu trước vành móng ngựa xuất hiện trên màn hình lớn như một lời cảnh báo đanh thép, đồng thời là cái tát hoàn hảo cuối cùng đập tan hoàn toàn những thế lực đen tối cản đường sự thật.",
        "Sự công bằng của pháp luật đã được thực thi triệt để, trả lại hào quang rực rỡ nhất cho trí tuệ chân chính và công sức của Đức Trung.",
        "Buổi tối cùng ngày, tiệc mừng công khánh thành hoành tráng được tổ chức tại trung tâm hội nghị sang trọng bên bờ vịnh Hải Phòng lộng lẫy.",
        "Hàng trăm quan khách, chuyên gia cầu đường quốc tế cùng ban lãnh đạo tổng công ty VEC tề tựu đông đủ chúc mừng chiến thắng kỳ tích.",
        "Hoàng Đức Trung đứng bên cạnh Vũ Thanh Lan dưới ánh đèn chùm pha lê lung linh rực rỡ, tay cầm ly rượu champagne lấp lánh bọt sủi.",
        "\"Chúc mừng anh, Đức Trung - vị thiên tài cầu đường vĩ đại nhất trong lòng em,\" Thanh Lan khẽ chạm ly rượu vào ly của anh, đôi mắt phượng ngập tràn tình yêu thương dịu dàng.",
        "Đức Trung mỉm cười ấm áp, anh nhìn cô gái xinh đẹp tuyệt trần đang đứng bên cạnh mình với tất cả niềm hạnh phúc trọn vẹn nhất của cuộc đời.",
        "\"Cảm ơn em, Thanh Lan. Danh hiệu thiên tài chỉ là phù phiếm, món quà lớn nhất mà anh có được sau dự án này chính là sự đồng hành trọn đời của em,\" anh chân thành nói từ đáy lòng.",
        "Hai người cùng nhau uống cạn ly rượu mừng chiến thắng ngọt ngào giữa tiếng vỗ tay chúc phúc của đông đảo bạn bè và đồng nghiệp xung quanh.",
        "Phía trước họ, con đường cao tốc vượt biển nghìn tỷ Tân Vũ - Lạch Huyện lấp lánh ánh đèn cao áp sáng rực như một dải ngân hà vắt qua biển khơi rộng lớn.",
        "Đại lộ cao tốc Bắc-Nam rộng lớn, những siêu công trình đường sắt tốc độ cao và những cây cầu vượt biển kỳ vĩ tiếp theo đang vẫy gọi bàn tay kiến tạo của Hoàng Đức Trung.",
        "Bản vẽ bị đánh cắp năm xưa giờ đã trở thành nhịp cầu thép vững chãi, đưa tên tuổi của anh bước vào ngôi đền huyền thoại của những thiên tài cầu đường vĩ đại nhất đất nước.",
        "Với sự điềm tĩnh thiên tài, trái tim trung thực vô song và tình yêu ngọt ngào của Vũ Thanh Lan bên cạnh, Hoàng Đức Trung sẵn sàng chinh phục mọi đỉnh cao kỹ nghệ mới, viết tiếp những trang sử vàng chói lọi cho ngành cầu đường Việt Nam vươn tầm thế giới.",
        "Cây cầu vĩ đại đã hoàn thành, kết nối lòng người và đất nước làm một thể thống nhất vững bền trước mọi giông bão thời gian.",
        "Hải Phòng lộng gió đêm nay lung linh, chào đón một chương mới đầy vinh quang rực rỡ của đất nước phồn vinh thịnh vượng.",
        "Tình yêu của họ, hòa cùng dòng chảy mãnh liệt của sự cống hiến kỹ nghệ đỉnh cao, sẽ mãi mãi vững chãi như nhịp cầu thế kỷ vắt qua đại dương xanh thẳm.",
        "Đức Trung nhìn ra khơi xa dưới bầu trời sao đêm lấp lánh rực rỡ đầy hoài bão lớn lao.",
        "Anh khẽ ôm nhẹ Thanh Lan vào lòng, cảm nhận hơi thở ấm áp của cô và biết rằng cuộc hành trình vĩ đại của họ chỉ mới thực sự bắt đầu."
    ]

    # Process and write
    w9 = save_chapter(9, "Chương 9: Lưới Trời Lồng Lộng", chap9_sentences)
    w10 = save_chapter(10, "Chương 10: Hợp Long Nhịp Cầu Thế Kỷ", chap10_sentences)
    w11 = save_chapter(11, "Chương 11: Hoàng Hôn Trên Cảng Hải Phòng", chap11_sentences)
    w12 = save_chapter(12, "Chương 12: Đại Tiệc Khánh Thành", chap12_sentences)

    print("=" * 50)
    print("🎉 Chapters 9, 10, 11, 12 generated successfully!")
    print(f"Chapter 9: {w9} words")
    print(f"Chapter 10: {w10} words")
    print(f"Chapter 11: {w11} words")
    print(f"Chapter 12: {w12} words")
    
    # Check that all chapters are >= 1000 words
    for num, w in [(9, w9), (10, w10), (11, w11), (12, w12)]:
        if w < 1000:
            print(f"⚠️ WARNING: Chapter {num} is below 1000 words ({w} words)!")
        else:
            print(f"✓ Chapter {num} passes 1000 words validation ({w} words)")
    print("=" * 50)

if __name__ == "__main__":
    main()
