# -*- coding: utf-8 -*-
import os
import json
import re

def count_words(text):
    # Clean HTML tags to count actual text words
    clean_text = re.sub(r'<[^>]+>', ' ', text)
    words = clean_text.strip().split()
    return len(words)

def save_chapter(chap_num, title, sentences):
    # Verify each sentence is clean and doesn't contain HTML tags
    # Wrap each sentence in a <p> tag and join them with \n
    content = ""
    for s in sentences:
        s_clean = s.strip()
        if not s_clean:
            continue
        content += f"<p>{s_clean}</p>\n"
    
    # Verify word count
    w_count = count_words(content)
    print(f"📖 Chapter {chap_num} Word Count: {w_count}")
    
    data = {
        "title": title,
        "content": content
    }
    
    output_dir = "/Users/aaronnguyen/TN/App/doctieuthuyet/scratch/novel_3_drafts"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    output_path = os.path.join(output_dir, f"chap{chap_num}.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"✓ Saved Chapter {chap_num} to {output_path}")
    return w_count

def main():
    # CHAPTER 1 SENTENCES
    chap1_sentences = [
        "Tiếng gió biển đêm gầm rú liên hồi ngoài cửa kính lớn của Viện Thiết kế Giao thông miền Bắc, mang theo những giọt nước mưa mặn chát đập mạnh vào vách kính.",
        "Lúc này đã là mười một giờ đêm, nhưng trong văn phòng của kỹ sư Hoàng Đức Trung, ánh đèn huỳnh quang vẫn tỏa ra thứ ánh sáng trắng lạnh lẽo.",
        "Trên màn hình máy trạm chuyên dụng cấu hình cao, bản vẽ ba chiều của siêu dự án cầu vượt biển Tân Vũ - Lạch Huyện đang hiển thị chi tiết đến từng khớp nối chịu lực phức tạp.",
        "Đồ họa lưới ba chiều phản chiếu qua mắt kính của Đức Trung, soi rõ đôi mắt hằn lên những tia máu đỏ quạch vì năm ngày liên tục không ngủ.",
        "Đây là đứa con tinh thần mà anh đã dành trọn ba năm ròng rã, lăn lộn khắp các bãi lầy thực địa Hải Phòng để hoàn thiện.",
        "Từng thông số kỹ thuật, từ đường kính cọc khoan nhồi sâu hơn tám mươi mét dưới đáy biển cho đến kết cấu dầm hộp đúc hẫng cân bằng, đều là mồ hôi và chất xám của anh.",
        "Anh khẽ thở phào nhẹ nhõm, đưa bàn tay mỏi nhừ nhấp một ngụm trà đặc nguội ngắt để xua đi cơn buồn ngủ đang tàn phá thần kinh.",
        "Cầu vượt biển Tân Vũ - Lạch Huyện là một trong những công trình giao thông trọng điểm quốc gia, kết nối trực tiếp với tuyến cao tốc Bắc - Nam huyết mạch.",
        "Để chống chịu được sức gió bão cực hạn của Biển Đông và sự ăn mòn hóa học khủng khiếp của nước biển mặn, Đức Trung đã đưa ra giải pháp kỹ thuật mang tính đột phá.",
        "Anh đề xuất sử dụng loại bê tông cường độ siêu cao UHPC kết hợp với hệ thống neo dự ứng lực phủ epoxy đặc chủng chống ăn mòn điện hóa.",
        "Đột nhiên, tiếng bước chân dồn dập vang lên từ phía hành lang lát gạch đá lạnh lẽo, phá tan không gian làm việc tĩnh lặng của đêm muộn.",
        "Cánh cửa gỗ nặng nề bị đẩy mạnh ra, đập vào tường nghe một tiếng chói tai, để lộ bóng dáng bệ vệ nhưng đầy kiêu ngạo của Lê Khắc Nam.",
        "Lê Khắc Nam là Viện phó Viện Thiết kế Giao thông, đồng thời cũng là sếp trực tiếp điều hành phòng nghiên cứu của Đức Trung.",
        "Đi ngay sau lão là Hùng Sắt, một tay thầu phụ phụ trách cung ứng thép khét tiếng miền Bắc với khuôn mặt bặm trợn và bộ dạng hầm hố của kẻ giang hồ khôn lỏi.",
        "\"Hoàng Đức Trung này, cậu dọn dẹp đồ đạc cá nhân đi, từ ngày mai không cần phải đến viện thiết kế làm việc nữa,\" Lê Khắc Nam thản nhiên nói.",
        "Giọng nói của lão lạnh lùng và chứa đựng sự khinh bỉ tột cùng, như thể đang bố thí một lời khuyên cho kẻ dưới quyền.",
        "Lão rút từ trong túi áo khoác hiệu Burberry đắt tiền ra một tờ quyết định sa thải đóng dấu đỏ chót, ném thẳng xuống bàn thí nghiệm đầy hóa chất.",
        "Đức Trung sững sờ trong giây lát, đôi mắt anh chuyển từ bản vẽ trên màn hình sang nhìn chằm chằm vào tờ quyết định sa thải vô lý.",
        "\"Viện phó Lê, lý do sa thải tôi là gì khi tôi đang chuẩn bị hoàn thiện giai đoạn thẩm định cuối cùng của dự án cầu vượt biển này?\" Đức Trung điềm tĩnh hỏi.",
        "Giọng nói của anh trầm ổn, không hề có sự hoảng loạn hay sợ hãi, tỏa ra một luồng khí chất điềm tĩnh đáng kinh ngạc.",
        "Lê Khắc Nam cười khẩy một tiếng đầy đắc ý, rồi quay sang ra hiệu cho Hùng Sắt đang đứng rung đùi bên cạnh.",
        "Hùng Sắt thò bàn tay thô kệch đầy sẹo vào túi, rút ra một chiếc ổ cứng di động màu đen bóng loáng và giơ lên trước mặt Đức Trung.",
        "\"Lý do là cậu thiếu năng lực hợp tác nhóm, liên tục đưa ra những đề xuất kỹ thuật viển vông làm chậm tiến độ chung của viện nghiên cứu,\" Lê Khắc Nam bịa đặt không chớp mắt.",
        "\"Còn về bản vẽ thiết kế cầu vượt biển Tân Vũ - Lạch Huyện, hội đồng kỹ thuật đã chính thức phê duyệt phương án do tôi làm chủ nhiệm thiết kế trưởng rồi,\" lão tuyên bố đầy tráo trở.",
        "Đức Trung lập tức hiểu ra toàn bộ sự việc khi nhìn thấy chiếc ổ cứng di động trên tay Hùng Sắt.",
        "Lê Khắc Nam đã lợi dụng quyền hạn Viện phó để âm thầm sao chép toàn bộ cơ sở dữ liệu tính toán kết cấu, mô phỏng tải trọng và bản vẽ kỹ thuật mà anh thức thâu đêm suốt sáng để làm ra.",
        "Lão cướp trắng trợn thành quả lao động của anh để nộp lên Tổng công ty Đầu tư phát triển đường cao tốc Việt Nam dưới tên tuổi của chính lão.",
        "\"Lê Khắc Nam, ông nghĩ rằng chỉ cần sao chép bản vẽ là có thể xây dựng được một cây cầu vượt biển nghìn tỷ an toàn hay sao?\" Đức Trung lạnh lùng vạch trần.",
        "\"Tôi cảnh báo ông, toàn bộ hệ thống chịu lực của dầm hộp đúc hẫng trong bản vẽ đó được tính toán dựa trên mác bê tông siêu cao UHPC và mật độ cốt thép đặc chủng cực kỳ khắt khe,\" anh đanh thép chỉ rõ.",
        "Hùng Sắt đứng bên cạnh khịt mũi một tiếng đầy khinh bỉ, gí điếu thuốc lá đang cháy dở vào một bản vẽ in thử trên bàn làm việc của anh.",
        "\"Cậu em kỹ sư quèn ơi, thời buổi này làm gì có ai đi xây cầu bằng thứ bê tông đắt đỏ và đống thép dày đặc như thế để tự cắt phăng lợi nhuận của mình?\" gã thầu phụ cười hô hố.",
        "\"Viện phó Lê đây đã có điều chỉnh cực kỳ sáng suốt cho phù hợp với tình hình thực tế thi công rồi,\" Hùng Sắt đắc ý tiết lộ âm mưu.",
        "\"Chúng tôi đã sửa lại thiết kế, thay thế toàn bộ bê tông UHPC bằng bê tông mác thường C30 chịu lực trung bình, đồng thời giảm bớt ba mươi phần trăm lượng thép chịu lực ở các trụ cầu để tiết kiệm ngân sách,\" gã thầu phụ vô liêm sỉ nói.",
        "Đức Trung nghe đến đây thì sắc mặt lập tức đanh lại, trong mắt lóe lên một tia giận dữ tột cùng trước sự ngu dốt và tham lam vô độ của bọn chúng.",
        "\"Các người điên rồi sao?\" Đức Trung gằn giọng, luồng uy áp lạnh lẽo từ người anh tỏa ra khiến cả Lê Khắc Nam lẫn Hùng Sắt đều khẽ rùng mình.",
        "\"Địa chất vùng biển Tân Vũ - Lạch Huyện vô cùng phức tạp, dòng chảy xiết của lạch biển kết hợp với nồng độ muối cực cao sẽ hủy hoại bê tông thường chỉ trong vòng vài năm!\" anh phân tích gay gắt.",
        "\"Nếu các người bòn rút cốt thép và hạ mác bê tông xuống C30, kết cấu dầm hộp đúc hẫng cân bằng sẽ bị nứt vỡ nghiêm trọng ngay khi hợp long dưới tác động của tải trọng gió bão cực hạn!\" Đức Trung dứt khoát cảnh báo.",
        "Lê Khắc Nam sắc mặt thoáng chút biến hóa, nhưng sự tham lam tột cùng và lòng kiêu ngạo hống hách đã hoàn toàn che mờ lý trí của lão.",
        "Lão biết rõ rằng việc thay đổi vật liệu từ cao cấp sang giá rẻ chịu lực kém sẽ giúp lão và Hùng Sắt đút túi chênh lệch hàng chục tỷ đồng từ ngân sách đấu thầu dự án.",
        "\"Câm miệng lại cho tôi!\" Lê Khắc Nam quát lên đầy giận dữ để che giấu sự chột dạ trong lòng.",
        "\"Tôi là Viện phó Viện Thiết kế, là chuyên gia cầu đường đầu ngành có hàng chục năm kinh nghiệm thực chiến, không cần một thằng nhóc rách rưới như cậu lên mặt dạy đời!\" lão sỉ nhục anh.",
        "\"Cái loại bê tông UHPC đắt đỏ của cậu chỉ có trong lý thuyết viển vông của mấy cuốn sách nước ngoài, thực tế thi công ở Việt Nam không cần màu mè như vậy!\" lão ngụy biện đầy ngu xuẩn.",
        "\"Hùng Sắt, gọi bảo vệ kéo nó ra ngoài ngay lập tức, niêm phong máy trạm và cấm nó mang theo bất kỳ tài liệu kỹ thuật nào của viện,\" Lê Khắc Nam ra lệnh tàn nhẫn.",
        "Hai gã bảo vệ to khỏe từ bên ngoài lập tức xông vào phòng, thô bạo giật lấy chiếc ba lô cũ kỹ trên tay Đức Trung và đẩy mạnh anh ra phía cửa hành lang.",
        "Đức Trung không hề phản kháng một cách vô ích, anh điềm tĩnh đứng thẳng người, phủi nhẹ lớp bụi bám trên vai chiếc áo khoác sờn vai.",
        "Đôi mắt anh tĩnh lặng như mặt hồ không một gợn sóng, nhìn thẳng vào khuôn mặt đang tràn ngập sự đắc ý và tham lam của Lê Khắc Nam cùng Hùng Sắt.",
        "\"Lê Khắc Nam, cầu vượt biển là công trình thế kỷ, liên quan trực tiếp đến tính mạng của hàng vạn người dân qua lại mỗi ngày,\" anh lạnh lùng tuyên bố.",
        "\"Bản vẽ bị rút ruột cốt thép và dùng bê tông mác thường đó chính là quả bom hẹn giờ sẽ chôn vùi toàn bộ danh vọng và sự nghiệp của ông xuống đáy lạch biển Hải Phòng,\" Đức Trung dõng dạc nói.",
        "\"Cậu cứ đợi đấy mà mơ mộng viển vông đi, dự án nghìn tỷ này sẽ mang lại vinh quang tột đỉnh cho tôi, còn cậu sẽ mãi là một kẻ thất nghiệp rách rưới trôi nổi ngoài đường!\" Lê Khắc Nam cười lớn đầy điên cuồng.",
        "Cánh cổng sắt lớn của Viện Thiết kế Giao thông đóng sập lại ngay sau lưng Đức Trung với một tiếng vang khô khốc đầy lạnh lẽo.",
        "Cơn mưa bão ngoài trời trút xuống xối xả, gió biển thổi tung mái tóc của chàng kỹ sư thiên tài đang đứng lặng im dưới bóng tối bên lề đường.",
        "Trên tay anh chỉ có một chiếc hộp giấy nhỏ thấm đẫm nước mưa chứa vài cuốn sổ tay tính toán số liệu địa chất thực địa và cây thước đo khoảng cách bằng laser đã cũ.",
        "Thế nhưng, Lê Khắc Nam và đồng bọn không bao giờ có thể ngờ rằng, toàn bộ bộ não thiên tài và khả năng tính toán chuẩn xác vô song của anh là thứ mà không một kẻ nào có thể đánh cắp được.",
        "Vết sẹo tinh thần từ sự phản bội của sếp cũ không làm anh gục ngã, ngược lại càng thổi bùng ngọn lửa quyết tâm trong lòng chàng kỹ sư trẻ tuổi.",
        "Đức Trung từ từ ngẩng đầu nhìn về phía vùng biển mịt mù sương bão ngoài xa, nơi tương lai của siêu dự án cầu vượt biển đang bị những kẻ gian thương bòn rút từ trong trứng nước.",
        "Anh biết rất rõ thời gian và những định luật vật lý nghiêm khắc sẽ chứng minh ai mới là thiên tài thực sự, và ai sẽ là kẻ phải quỳ xuống đền tội trước pháp luật.",
        "Chàng kỹ sư điềm tĩnh bước đi trong màn mưa dày đặc của Hải Phòng, bóng lưng cô độc nhưng vô cùng vững chãi như một trụ cầu sừng sững giữa sóng gió đại dương.",
        "Anh thầm hứa với lòng mình rằng sẽ không bao giờ để cây cầu vượt biển Tân Vũ - Lạch Huyện bị biến thành một đống phế tích nguy hiểm bởi sự tham lam của những kẻ gian ác.",
        "Mưa mỗi lúc một nặng hạt, gột rửa sạch những bụi bặm của Viện Thiết kế thối nát sau lưng anh, mở ra một hành trình mới đầy chông gai nhưng cũng đầy vinh quang phía trước.",
        "Chàng kỹ sư thiên tài bước đi dưới trời đêm bão táp, lòng ngập tràn một niềm tin sắt đá rằng chuyên môn siêu phàm của anh sẽ sớm lật ngược thế cờ."
    ]

    # CHAPTER 2 SENTENCES
    chap2_sentences = [
        "Cơn mưa đêm Hải Phòng kéo dài đến tận sáng hôm sau vẫn chưa có dấu hiệu dứt, để lại những vũng nước đục ngầu trên con đường dẫn ra cảng Đình Vũ.",
        "Hoàng Đức Trung bước đi bên lề đường, chiếc áo khoác gió sờn vai đã thấm đẫm nước mưa lạnh buốt, nhưng phong thái của anh vẫn vô cùng điềm tĩnh.",
        "Anh đứng lại bên bờ kè đá, đôi mắt sâu thẳm nhìn về phía luồng lạch biển Tân Vũ - Lạch Huyện đang cuộn sóng dữ dội dưới bầu trời xám xịt.",
        "Đúng lúc đó, ở phía xa lộ dẫn ra hiện trường khảo sát của dự án cầu vượt biển, một chiếc xe Ford Explorer màu đen sang trọng đang đỗ xịch bên đường.",
        "Xung quanh chiếc xe, một nhóm kỹ sư khảo sát mặc áo bảo hộ màu phản quang đang tranh cãi kịch liệt, gương mặt ai nấy đều lộ rõ vẻ hoang mang tột độ.",
        "Dẫn đầu nhóm người đó là một cô gái trẻ tuổi có vóc dáng cao ráo, mặc chiếc áo măng tô màu xanh đen thanh lịch và đội chiếc mũ bảo hộ màu trắng.",
        "Đó chính là Vũ Thanh Lan, Phó Tổng Giám đốc của Tổng công ty Đầu tư phát triển đường cao tốc Việt Nam (VEC), chủ đầu tư trực tiếp của dự án cầu vượt biển này.",
        "Thanh Lan sở hữu một vẻ đẹp sắc sảo, kiên quyết với đôi mắt phượng thông minh luôn toát lên vẻ nghiêm nghị của một nhà quản lý cấp cao sắc sảo.",
        "\"Tôi không cần biết các anh dùng phương pháp nào, nhưng số liệu khảo sát địa chất móng trụ cầu số bốn bắt buộc phải có trước mười hai giờ trưa nay!\" Thanh Lan nghiêm giọng nói.",
        "Giọng nói của cô trong trẻo nhưng đầy uy nghiêm, khiến nhóm kỹ sư khảo sát dưới quyền lập tức im bặt, cúi đầu né tránh ánh mắt sắc sảo của cô.",
        "\"Báo cáo Phó Tổng Giám đốc Vũ, hệ thống máy khoan thăm dò của chúng ta liên tục gặp sự cố khi chạm đến độ sâu bốn mươi mét dưới lòng biển,\" vị trưởng nhóm khảo sát lắp bắp giải thích.",
        "\"Áp lực nước dưới lạch biển quá lớn kết hợp với tầng cát chảy di động khiến mũi khoan bị lệch hướng liên tục, chúng tôi không thể lấy được mẫu đất nguyên dạng,\" ông ta bất lực phân tích.",
        "Thanh Lan siết chặt nắm tay, mồ hôi lạnh rịn ra trên trán dưới làn mưa buốt giá khi nghĩ đến việc tiến độ dự án nghìn tỷ có nguy cơ bị đình trệ ngay từ khâu khảo sát.",
        "Đức Trung đứng gần đó lặng lẽ quan sát sơ đồ địa chất thực địa đang được hiển thị trên chiếc máy tính bảng của một kỹ sư trẻ trong nhóm.",
        "Nhờ khả năng chuyên môn siêu phàm và kinh nghiệm thực địa phong phú, anh lập tức nhìn ra nguyên nhân chí mạng mà đội ngũ kỹ sư của VEC đang hoàn toàn bế tắc.",
        "Anh nhẹ nhàng bước tới gần, đứng sau lưng vị trưởng nhóm khảo sát và lên tiếng với giọng điệu vô cùng trầm ổn: \"Các anh đang đo sai thông số áp lực nước lỗ rỗng rồi.\"",
        "Tiếng nói đột ngột của một thanh niên lạ mặt mặc chiếc áo gió cũ kỹ khiến toàn bộ nhóm kỹ sư quay lại nhìn bằng ánh mắt vô cùng kinh ngạc và hoài nghi.",
        "\"Cậu là ai? Đây là khu vực khảo sát kỹ thuật cấp cao của VEC, người ngoài không phận sự miễn vào!\" vị trưởng nhóm khảo sát quát lên đầy khó chịu.",
        "Thế nhưng, Vũ Thanh Lan lại không hề vội vàng xua đuổi, cô chăm chú quan sát phong thái điềm tĩnh lạ thường và ánh mắt tự tin tuyệt đối của Đức Trung.",
        "\"Anh vừa nói chúng tôi đo sai áp lực nước lỗ rỗng? Ý anh là thế nào?\" Thanh Lan bước lên một bước, trực tiếp hỏi Đức Trung bằng giọng điệu sắc sảo.",
        "Đức Trung không hề bối rối trước luồng uy áp của nữ Phó Tổng Giám đốc xinh đẹp, anh nhẹ nhàng chỉ tay vào biểu đồ sóng địa chấn hiển thị trên màn hình máy tính.",
        "\"Địa chất tại lạch biển Tân Vũ không phải là tầng đất sét thông thường, mà là tầng cát mịn bão hòa nước bị hiện tượng hóa lỏng động dưới tác động của dòng triều xiết,\" anh giải thích mạch lạc.",
        "\"Khi các anh dùng mũi khoan xoay truyền thống đâm xuống, lực ma sát động sẽ kích hoạt áp lực nước lỗ rỗng tăng vọt đột ngột, làm hóa lỏng hoàn toàn lớp cát xung quanh mũi khoan,\"",
        "\"Đó chính là lý do khiến mũi khoan bị lệch hướng liên tục và không thể thu hồi được mẫu đất nguyên dạng để phục vụ tính toán tải trọng móng trụ cầu vượt biển,\"",
        "\"Để khắc phục điều này, các anh bắt buộc phải chuyển sang sử dụng phương pháp khoan tuần hoàn nghịch kết hợp với dung dịch bentonite polyme mác cao để giữ thành vách hố khoan ổn định,\"",
        "\"Đồng thời, áp lực bơm dung dịch giữ vách phải được kiểm soát nghiêm ngặt ở mức không phẩy mười lăm megapascal dựa trên độ sâu khoan thực tế,\" Đức Trung phân tích vanh vách.",
        "Toàn bộ nhóm kỹ sư khảo sát của VEC đờ người ra trước những phân tích kỹ thuật vô cùng chuẩn xác, sắc bén và am tường sâu sắc của chàng trai trẻ lạ mặt.",
        "Vị trưởng nhóm khảo sát run run tay lật lại cuốn sổ tay kỹ thuật của tập đoàn chuyên gia nước ngoài từ Nhật Bản để đối chiếu thông số.",
        "\"Thật... thật không thể tin nổi! Các chuyên gia tư vấn Nhật Bản cũng từng đề cập đến hiện tượng hóa lỏng cát này trong tài liệu hướng dẫn kỹ thuật bảo mật!\" ông ta thốt lên đầy kinh ngạc.",
        "\"Làm thế nào mà một người đi đường như cậu lại có thể nắm rõ các thông số kỹ thuật địa chất phức tạp này chỉ bằng một cái liếc mắt?\" vị trưởng nhóm khảo sát thán phục hỏi.",
        "Vũ Thanh Lan nhìn Đức Trung bằng đôi mắt phượng sáng lên sự ngạc nhiên tột độ và niềm vui mừng khôn xiết khi tìm được một nhân tài thực thụ giữa lúc bế tắc.",
        "Cô lập tức ra lệnh cho nhóm kỹ sư thực hiện ngay theo phương án cải tiến kỹ thuật mà Đức Trung vừa đề xuất để kiểm chứng hiệu quả thực tế.",
        "Chỉ sau chưa đầy ba mươi phút áp dụng phương pháp khoan tuần hoàn nghịch kết hợp dung dịch bentonite polyme theo đúng chỉ dẫn của anh, mũi khoan thăm dò đã đâm xuyên qua tầng cát chảy ổn định.",
        "Hệ thống máy móc hoạt động trơn tru, lấy lên được những mẫu đất nguyên dạng đầu tiên ở độ sâu sáu mươi mét dưới lòng biển Hải Phòng trước sự hân hoan tột cùng của cả đội ngũ.",
        "Vũ Thanh Lan khẽ mỉm cười đầy rạng rỡ, cô bước đến trước mặt Đức Trung, chủ động đưa bàn tay thon nhỏ trắng mịn ra để bắt tay anh.",
        "\"Tôi là Vũ Thanh Lan, Phó Tổng Giám đốc VEC. Rất cảm ơn anh đã cứu nguy cho chúng tôi một bàn thua trông thấy ngày hôm nay,\" cô chân thành nói.",
        "\"Tôi là Hoàng Đức Trung, chỉ là một kỹ sư cầu đường tự do,\" anh nhẹ nhàng bắt tay cô, phong thái vẫn vô cùng điềm tĩnh lịch sự.",
        "Nghe đến cái tên Hoàng Đức Trung, đôi lông mày thanh tú của Vũ Thanh Lan khẽ nhướng lên đầy bất ngờ khi nhớ lại một sự việc chấn động vừa xảy ra.",
        "\"Hoàng Đức Trung? Anh chính là tác giả thực sự của bản thiết kế cầu vượt biển Tân Vũ - Lạch Huyện mà Viện phó Lê Khắc Nam vừa trình lên VEC hôm qua?\" cô sắc sảo hỏi gặng.",
        "\"Đúng vậy, nhưng bản vẽ mà Lê Khắc Nam nộp lên VEC chắc chắn đã bị rút ruột cốt thép và thay đổi vật liệu mác thấp để đút túi chênh lệch,\" Đức Trung thẳng thắn tiết lộ sự thật.",
        "Thanh Lan sắc mặt lập tức trở nên vô cùng nghiêm nghị, cô đã nghi ngờ từ lâu về mức chi phí dự toán rẻ đến bất thường trong hồ sơ thầu của Lê Khắc Nam.",
        "\"Lê Khắc Nam dám ngang nhiên bòn rút sắt thép chịu lực và dùng bê tông mác thường C30 cho một siêu công trình vượt biển nghìn tỷ hay sao?\" cô giận dữ nói.",
        "\"Bọn chúng muốn ăn chặn chênh lệch vật liệu mà không hề quan tâm đến sự an toàn tính mạng của người dân và tuổi thọ của công trình thế kỷ này,\" Đức Trung lạnh lùng phân tích.",
        "\"Hoàng Đức Trung, VEC luôn ủng hộ những kỹ sư có tâm và có tầm như anh, chúng tôi quyết không để những kẻ gian thương lũng đoạn dự án quốc gia này,\" Thanh Lan tuyên bố đanh thép.",
        "\"Nếu anh đồng ý, tôi muốn chính thức mời anh về làm Cố vấn kỹ thuật trưởng trực thuộc Ban Giám đốc VEC để trực tiếp thẩm định và giám sát dự án cầu Tân Vũ - Lạch Huyện,\"",
        "\"Tôi sẽ bảo đảm cho anh một không gian sáng tạo chuyên môn tuyệt đối sòng phẳng và toàn quyền quyết định về mặt giải pháp kỹ thuật thi công cầu vượt biển,\" cô đưa ra lời mời đầy chân thành.",
        "Đức Trung nhìn vào đôi mắt kiên định, sắc sảo và ngập tràn sự ủng hộ chân thành của Vũ Thanh Lan, anh khẽ mỉm cười đầy ấm áp.",
        "Anh biết rằng đây chính là cơ hội vàng để anh khôi phục lại đứa con tinh thần của mình, đồng thời vạch trần bộ mặt thật của những kẻ đã phản bội anh.",
        "\"Rất vinh hạnh được hợp tác cùng Phó Tổng Giám đốc Vũ. Tôi đồng ý,\" Đức Trung dứt khoát nhận lời mời.",
        "Cuộc gặp gỡ định mệnh bên bờ biển Hải Phòng giữa chàng kỹ sư thiên tài Hoàng Đức Trung và nữ Phó Tổng Giám đốc sắc sảo Vũ Thanh Lan đã chính thức bắt đầu.",
        "Bánh răng số phận bắt đầu quay, thiết lập nên một thế trận đấu trí đỉnh cao chuẩn bị nghiền nát âm mưu bòn rút công trình của Lê Khắc Nam và Hùng Sắt.",
        "Thanh Lan lập tức mời Đức Trung lên chiếc xe Explorer sang trọng của mình để cùng quay trở lại văn phòng chuẩn bị cho buổi đấu thầu thẩm định kỹ thuật ngày mai.",
        "Trên xe, hai người nhanh chóng trao đổi sâu sắc về các giải pháp kết cấu dầm đúc hẫng cân bằng và hệ thống cọc khoan nhồi chịu lực móng trụ cầu vượt biển.",
        "Thanh Lan càng lắng nghe càng vô cùng thán phục tư duy kỹ thuật xuất sắc, tầm nhìn chiến lược và kiến thức chuyên môn uyên bác của Đức Trung.",
        "Cô thầm nghĩ quyết định mời anh về làm Cố vấn trưởng chính là quyết định sáng suốt nhất trong sự nghiệp quản lý của mình từ trước đến nay.",
        "Gió mưa ngoài cửa xe vẫn gầm rú dữ dội, nhưng bầu không khí bên trong lại tràn ngập một niềm tin mãnh liệt vào sự chiến thắng của công lý và trí tuệ thực sự.",
        "Đức Trung khẽ tựa lưng vào ghế, vết sẹo trong lòng bàn tay dường như không còn đau nhức nữa, thay vào đó là ý chí chiến đấu sục sôi.",
        "Anh sẽ dùng chính tài năng thiên bẩm của mình để bắt kẻ đã cướp công trình của anh phải trả một cái giá đắt nhất từ trước đến nay.",
        "Cây cầu vượt biển Tân Vũ - Lạch Huyện sẽ được xây dựng vững chãi bằng mồ hôi chân chính của những kỹ sư Việt Nam chân chính dưới sự bảo trợ của VEC."
    ]

    # CHAPTER 3 SENTENCES
    chap3_sentences = [
        "Sảnh hội trường lớn của Tổng công ty Đầu tư phát triển đường cao tốc Việt Nam (VEC) tại Hà Nội sáng hôm nay chật kín người tham dự.",
        "Bầu không khí bên trong vô cùng trang trọng và căng thẳng trước thềm buổi đấu thầu và thẩm định kỹ thuật siêu dự án cầu vượt biển Tân Vũ - Lạch Huyện.",
        "Lê Khắc Nam và Hùng Sắt bước vào phòng họp với phong thái vô cùng tự tin, gương mặt tràn ngập niềm kiêu hãnh và đắc ý tột độ.",
        "Lão Viện phó ăn mặc chỉnh tề trong bộ comple đắt tiền, tay cầm xấp tài liệu thiết kế cướp được từ Đức Trung, tin chắc chiến thắng đã nằm gọn trong tay.",
        "Lão nghĩ rằng bản thiết kế cải tiến \"tiết kiệm chi phí\" của mình sẽ dễ dàng đánh bại các đối thủ khác để giành lấy gói thầu nghìn tỷ.",
        "\"Viện phó Lê quả là danh bất hư truyền, bản thiết kế lần này cắt giảm được hơn năm mươi tỷ tiền sắt thép chắc chắn sẽ khiến ban lãnh đạo VEC hài lòng,\" Hùng Sắt nịnh nọt.",
        "\"Chú yên tâm đi, anh đã lo lót mọi đường rồi, buổi thẩm định hôm nay chỉ là thủ tục hình thức để chúng ta chính thức ký hợp đồng thầu phụ thôi,\" Lê Khắc Nam khẽ nói đầy xảo quyệt.",
        "Đúng chín giờ sáng, hội đồng thẩm định kỹ thuật gồm các chuyên gia cầu đường hàng đầu Việt Nam và quốc tế từ Nhật Bản, Hàn Quốc bắt đầu ổn định vị trí.",
        "Lê Khắc Nam bước lên bục thuyết trình với vẻ mặt vô cùng tự mãn, bắt đầu trình chiếu bản vẽ thiết kế cầu vượt biển bị rút ruột của Đức Trung.",
        "Lão thao thao bất tuyệt thuyết trình về giải pháp \"tối ưu hóa kết cấu chịu lực bằng việc sử dụng bê tông mác thường C30 và giảm bớt mật độ cốt thép trụ cầu vượt biển,\"",
        "Lão ngụy biện rằng phương án này vừa đảm bảo khả năng chịu tải tiêu chuẩn vừa tiết kiệm cho ngân sách nhà nước hàng chục tỷ đồng chi phí vật liệu thi công.",
        "Các chuyên gia trong hội đồng im lặng lắng nghe, một vài người khẽ nhíu mày hoài nghi trước những thông số cắt giảm sắt thép chịu lực quá mức an toàn.",
        "\"Thưa hội đồng thẩm định, phương án tối ưu hóa này là kết quả nghiên cứu nhiều năm của tôi, hoàn toàn phù hợp với thực tế địa chất Hải Phòng,\" Lê Khắc Nam dõng dạc kết luận.",
        "Lão khép lại bài thuyết trình trong tiếng vỗ tay lẹt đẹt từ phía những tay thầu phụ cánh cánh dưới trướng của Hùng Sắt đang ngồi dưới hội trường.",
        "\"Cảm ơn bài thuyết trình đầy sáng tạo của Viện phó Lê Khắc Nam,\" giọng nói trong trẻo nhưng lạnh lùng của Vũ Thanh Lan vang lên từ phía bàn chủ tọa.",
        "\"Tuy nhiên, ban giám đốc VEC có một chuyên gia đặc biệt muốn đưa ra ý kiến phản biện độc lập về tính khả thi kỹ thuật của phương án này,\" cô sắc sảo công bố.",
        "Lê Khắc Nam khẽ biến sắc mặt, trong lòng dấy lên một cảm giác bất an mơ hồ khi thấy thái độ nghiêm nghị lạ thường của nữ Phó Tổng Giám đốc.",
        "Cánh cửa bên hông hội trường từ từ mở ra, Hoàng Đức Trung trong bộ âu phục đen lịch lãm, phong thái ung dung tự tại bước thẳng vào phòng họp.",
        "Đi ngay sau anh là hai trợ lý kỹ thuật của VEC đang khệ nệ bê theo một mô hình kết cấu dầm đúc hẫng chịu tải và xấp hồ sơ thẩm định dày cộp.",
        "Nhìn thấy sự xuất hiện đột ngột của Đức Trung, Lê Khắc Nam lập tức trợn trừng đôi mắt, hai tay run lên bần bật đến mức làm rơi cả chiếc bút chỉ laser xuống đất.",
        "\"Hoàng... Hoàng Đức Trung? Sao cậu lại dám vác mặt đến đây? Đây là hội nghị thẩm định cấp cao, bảo vệ đâu kéo thằng nhóc thất nghiệp này ra ngoài!\" Lê Khắc Nam gào lên mất kiểm soát.",
        "Hùng Sắt đứng bên cạnh cũng trợn mắt sừng sộ, định bước lên đe dọa Đức Trung bằng bộ dạng giang hồ hung hãn thường ngày.",
        "\"Câm miệng lại cho tôi!\" Vũ Thanh Lan đập mạnh tay xuống bàn chủ tọa, tiếng đập mạnh vang lên khô khốc khiến toàn bộ hội trường lập tức im bặt.",
        "\"Kỹ sư Hoàng Đức Trung hiện là Cố vấn kỹ thuật trưởng trực thuộc Ban Giám đốc VEC, là người toàn quyền chịu trách nhiệm thẩm định chuyên môn cho siêu dự án này!\" cô dõng dạc tuyên bố.",
        "Lời tuyên bố đanh thép của Vũ Thanh Lan như một tiếng sét giữa trời quang, đánh thẳng vào đầu Lê Khắc Nam và Hùng Sắt khiến cả hai đứng đờ người ra như hóa đá.",
        "Đức Trung không thèm liếc nhìn khuôn mặt đang tái nhợt vì kinh hoàng của sếp cũ, anh ung dung bước lên bục phản biện kỹ thuật sòng phẳng.",
        "Anh nhẹ nhàng cắm chiếc USB chứa dữ liệu phân tích phần tử hữu hạn vào máy trạm, màn hình lớn lập tức hiển thị biểu đồ mô phỏng ứng suất chịu lực trụ cầu vượt biển.",
        "\"Thưa hội đồng thẩm định, tôi xin trình bày kết quả thẩm định độc lập về bản thiết kế do Lê Khắc Nam ký tên chủ nhiệm,\" Đức Trung điềm tĩnh nói.",
        "\"Bản thiết kế này đã bị cắt giảm ba mươi phần trăm lượng thép chịu lực tại vùng momen âm cực đại của dầm hộp liên tục đúc hẫng cân bằng,\"",
        "\"Đồng thời, việc thay thế bê tông mác siêu cao UHPC bằng bê tông mác thường C30 là một sai lầm kỹ thuật mang tính phá hoại cực kỳ nghiêm trọng,\"",
        "\"Địa chất lạch biển Hải Phòng có tầng cát chảy di động sâu ba mươi mét, dòng chảy xiết của thủy triều sẽ tạo ra tải trọng động xoáy cực lớn đập liên tục vào các trụ cầu,\"",
        "\"Nếu dùng bê tông mác thường C30, nồng độ ion clorua trong nước biển mặn sẽ xâm nhập qua các vết nứt vi mô chỉ trong vòng hai mươi bốn tháng,\"",
        "\"Ion clorua sẽ trực tiếp ăn mòn điện hóa cốt thép chịu lực bên trong, làm giảm tiết diện chịu lực và gây nứt vỡ kết cấu dầm hộp đúc hẫng khi chịu tải trọng gió bão cực hạn,\"",
        "\"Tôi đã chạy mô phỏng tải trọng động cực hạn theo tiêu chuẩn quốc tế AASHTO trên hệ thống siêu máy tính của VEC,\" Đức Trung phân tích sắc bén.",
        "\"Kết quả cho thấy, khi tốc độ gió bão đạt cấp mười hai, ứng suất kéo tại chân trụ cầu số bốn sẽ vượt quá giới hạn bền của bê tông C30 tới một trăm hai mươi phần trăm,\"",
        "\"Cây cầu vượt biển trị giá nghìn tỷ này sẽ bị gãy đôi ngay lập tức tại vị trí hợp long dầm biên chịu lực, tạo nên một thảm họa giao thông kinh hoàng!\" anh đanh thép chỉ rõ.",
        "Trên màn hình lớn, hình ảnh mô phỏng ba chiều hiển thị cảnh cây cầu vượt biển bị gãy đôi dưới tác động của sóng gió bão táp sinh động đến mức rùng rợn.",
        "Toàn bộ hội đồng thẩm định kỹ thuật, đặc biệt là các chuyên gia cầu đường lão luyện từ Nhật Bản và Hàn Quốc, đồng loạt đứng dậy trầm trồ thán phục trước sự chuẩn xác vô song của anh.",
        "\"Tuyệt vời! Bản phân tích phần tử hữu hạn này quá sắc bén và chuẩn xác đến từng megapascal chịu lực!\" vị giáo sư chuyên gia người Nhật Bản thốt lên bằng tiếng Anh.",
        "\"Phương án bòn rút cốt thép của Lê Khắc Nam thực chất là một tội ác phá hoại công trình quốc gia, chúng tôi hoàn toàn đồng ý loại bỏ ngay lập tức phương án nguy hiểm này!\" ông ta tuyên bố.",
        "Lê Khắc Nam mồ hôi chảy ròng ròng trên trán, khuôn mặt xám ngoét không còn một giọt máu, lão cố gắng cãi chày cãi cối trong sự bất lực tột cùng.",
        "\"Không... không phải như thế! Đây chỉ là sự khác biệt về quan điểm thiết kế kỹ thuật tối ưu hóa chi phí mà thôi!\" lão lắp bắp ngụy biện đầy thảm hại.",
        "\"Tối ưu hóa chi phí hay là âm mưu rút ruột công trình để đút túi chênh lệch vật liệu hàng chục tỷ đồng cùng với thầu phụ Hùng Sắt?\" Vũ Thanh Lan lạnh lùng vạch trần.",
        "Cô ra hiệu cho trợ lý trình ra toàn bộ hồ sơ giao dịch tài chính mờ ám giữa công ty thầu phụ của Hùng Sắt và người nhà của Lê Khắc Nam trong thời gian qua.",
        "Sự xuất hiện của đống chứng cứ đanh thép này khiến cả Lê Khắc Nam lẫn Hùng Sắt hoàn toàn ngã quỵ xuống ghế, hai tai lùng bùng không thể nói thêm được lời nào.",
        "\"Thay mặt ban lãnh đạo VEC, tôi tuyên bố bác bỏ hoàn toàn phương án thầu của Lê Khắc Nam và cấm vĩnh viễn Viện Thiết kế Giao thông tham gia các dự án của chúng tôi,\"",
        "\"Đồng thời, VEC quyết định khôi phục và áp dụng nguyên bản thiết kế gốc sử dụng bê tông cường độ siêu cao UHPC do kỹ sư Hoàng Đức Trung làm chủ nhiệm thiết kế trưởng,\"",
        "\"Chúng tôi sẽ trực tiếp cấp vốn và bảo trợ thi công toàn diện cho phương án kỹ thuật xuất sắc này dưới sự giám sát trực tiếp của Cố vấn trưởng Hoàng Đức Trung,\" Thanh Lan dõng dạc tuyên bố.",
        "Hội trường lớn lập tức bùng nổ trong tiếng vỗ tay rầm rộ kéo dài của toàn thể các chuyên gia cầu đường hàng đầu để tán thưởng tài năng thiên tài của Đức Trung.",
        "Đức Trung đứng trên bục, phong thái vẫn vô cùng điềm tĩnh tự tại, anh khẽ gật đầu cảm ơn sự ủng hộ nhiệt thành của hội đồng thẩm định.",
        "Anh nhìn xuống phía Lê Khắc Nam đang ngồi run rẩy, bất lực chịu đựng những ánh mắt khinh bỉ và lên án từ phía đồng nghiệp xung quanh.",
        "Màn vả mặt sòng phẳng ngay tại hội trường lớn của VEC đã kết thúc mỹ mãn, lấy lại sự trong sạch và vinh quang vốn thuộc về chàng kỹ sư thiên tài.",
        "Hùng Sắt siết chặt nắm tay đầy giận dữ, gã liếc nhìn Đức Trung bằng ánh mắt độc địa của kẻ giang hồ bị cướp mất miếng mồi ngon nghìn tỷ.",
        "Gã thầm thề sẽ dùng mọi thủ đoạn đen tối nhất ngoài công trường thi công Hải Phòng để phá hoại công trình của Đức Trung và trả thù mối hận ngày hôm nay.",
        "Thế nhưng, Đức Trung không hề sợ hãi trước những lời đe dọa vô ích đó, anh biết rằng công lý và chuyên môn siêu phàm sẽ luôn là tấm lá chắn vững chắc nhất.",
        "Thanh Lan bước đến bên cạnh anh, ánh mắt cô lấp lánh niềm kiêu hãnh và sự ngưỡng mộ sâu sắc dành cho chàng cố vấn trưởng tài ba của mình.",
        "\"Chúc mừng anh, chủ nhiệm thiết kế trưởng Hoàng Đức Trung. Cây cầu vượt biển của anh sẽ sớm được khởi công xây dựng sừng sững giữa sóng gió đại dương,\" cô dịu dàng nói.",
        "\"Cảm ơn Thanh Lan đã luôn tin tưởng và ủng hộ tôi. Trận chiến thực sự ngoài công trường Hải Phòng bây giờ mới chính thức bắt đầu,\" Đức Trung điềm tĩnh đáp.",
        "Hai người cùng nhau bước ra khỏi phòng họp trong ánh nắng rực rỡ của ngày mới, hướng về phía Hải Phòng để chuẩn bị cho giai đoạn khởi công siêu công trình."
    ]

    # CHAPTER 4 SENTENCES
    chap4_sentences = [
        "Công trường siêu dự án cầu vượt biển Tân Vũ - Lạch Huyện bên bờ biển Hải Phòng những ngày này nhộn nhịp tiếng động cơ của hàng trăm máy xúc, cần cẩu khổng lồ.",
        "Những nhịp cầu dẫn đầu tiên sừng sững vươn mình ra phía biển khơi rộng lớn, thể hiện quy mô hoành tráng của công trình giao thông trọng điểm quốc gia.",
        "Hoàng Đức Trung đội mũ bảo hộ màu trắng, mặc áo phản quang trực tiếp đứng ở mũi thi công trụ cầu số bốn giữa luồng lạch biển chảy xiết.",
        "Bàn tay anh cầm bản vẽ chi tiết thép, đôi mắt nghiêm nghị giám sát chặt chẽ từng công đoạn lắp dựng lồng thép cọc khoan nhồi sâu dưới đáy biển.",
        "Lúc này, Hùng Sắt - kẻ thầu phụ bị mất miếng mồi ngon sau buổi đấu thầu sòng phẳng - đang giở mọi thủ đoạn đê hèn để trả thù Đức Trung.",
        "Gã sai hàng chục tay đàn em bặm trợn đến gây rối tại cổng công trường, chặn các xe chở cát đá tiêu chuẩn mác cao và đe dọa các kỹ sư trẻ dưới quyền anh.",
        "\"Thằng nhóc cố vấn trưởng kia, mày dám cướp miếng cơm của anh em tao thì đừng hòng để cây cầu này được hoàn thành suôn sẻ!\" gã đàn em của Hùng Sắt hét lên hung hãn.",
        "Thế nhưng, Đức Trung không hề nao núng, anh lập tức yêu cầu lực lượng an ninh công trường phối hợp với công an địa phương để bảo vệ nghiêm ngặt khu vực thi công.",
        "Mọi âm mưu quấy rối thô bạo của Hùng Sắt đều bị sự điềm tĩnh và quyết đoán của Đức Trung hóa giải nhanh chóng, giữ cho nhịp độ công trường luôn ổn định.",
        "Đúng lúc này, thời tiết tại vùng biển Hải Phòng bỗng chốc thay đổi đột ngột khi một cơn bão lớn từ Biển Đông bất ngờ đổi hướng tràn thẳng vào đất liền.",
        "Mây đen kịt ùn ùn kéo đến che lấp cả bầu trời, gió biển gầm rú dữ dội cuốn theo những đợt sóng khổng lồ cao tới bốn mét đập liên hồi vào bệ trụ cầu đang thi công.",
        "Đây là thời điểm vô cùng nhạy cảm khi công trường đang tiến hành đổ bê tông khối lớn dưới nước cho bệ trụ cầu số bốn - trụ chịu lực chính của toàn bộ công trình.",
        "Lê Khắc Nam đứng sau giật dây Hùng Sắt, hy vọng cơn bão lớn này sẽ phá hủy hoàn toàn bệ trụ cầu chưa kịp đông cứng để đổ lỗi kỹ thuật lên đầu Đức Trung.",
        "\"Cơn bão này cấp mười hai, sức gió giật mạnh thế này thì việc đổ bê tông dưới nước chắc chắn sẽ thất bại, bệ trụ sẽ bị sóng biển cuốn trôi hoàn toàn!\" Lê Khắc Nam đắc ý nghĩ thầm.",
        "Trái ngược với sự hoảng sợ tột độ của toàn bộ công nhân và kỹ sư trên công trường đang định bỏ chạy vào bờ trú ẩn, Đức Trung vẫn đứng vững chãi trước đầu sóng ngọn gió.",
        "Gương mặt anh sạm đi vì nắng gió biển nhưng đôi mắt vẫn sáng lên ý chí sắt đá và sự bình thản đáng kinh ngạc của một vị tổng chỉ huy thiên tài.",
        "\"Tất cả mọi người giữ nguyên vị trí thi công! Chúng ta không được phép dừng lại lúc này, nếu dừng lại bê tông sẽ bị phân tầng và hỏng hoàn toàn bệ trụ cầu!\" anh ra lệnh dứt khoát.",
        "Giọng nói của Đức Trung vang vọng qua hệ thống loa cầm tay, đè bẹp cả tiếng gió bão gầm rú, mang lại niềm tin mãnh liệt cho hàng trăm công nhân đang dao động.",
        "Anh quyết định áp dụng ngay giải pháp kỹ thuật độc bản vô cùng táo bạo: sử dụng ống đổ bê tông tremie cải tiến kết hợp phụ gia silica fume đông cứng siêu nhanh dưới nước mặn.",
        "Đây là kỹ thuật thi công đỉnh cao đòi hỏi độ chuẩn xác cực kỳ khắt khe về mặt thông số áp lực bơm và độ sụt của hỗn hợp bê tông cường độ siêu cao UHPC.",
        "Vũ Thanh Lan bất chấp mưa bão sấm sét gầm rú dữ dội, cô mặc áo mưa trực tiếp túc trực bên cạnh Đức Trung trên sàn đạo thi công trơn trượt ngoài biển khơi.",
        "Cô dùng quyền hạn Phó Tổng Giám đốc VEC để lập tức huy động toàn bộ hệ thống sà lan cẩu và lực lượng hậu cần cung ứng vật liệu khẩn cấp hỗ trợ anh.",
        "\"Đức Trung, hãy yên tâm chiến đấu! Ban lãnh đạo VEC và tôi sẽ là hậu phương vững chắc nhất đứng sau lưng anh lúc này!\" Thanh Lan hét lớn qua tiếng gió bão.",
        "Nhìn thấy nữ Phó Tổng Giám đốc xinh đẹp sắc sảo bất chấp hiểm nguy đứng bên cạnh mình dưới mưa bão, Đức Trung cảm thấy lồng ngực ấm áp và ý chí chiến đấu tăng lên gấp bội.",
        "Anh trực tiếp trèo lên tháp đổ bê tông cao hơn mười mét, bàn tay chỉ huy nhịp nhàng các kỹ sư điều chỉnh độ sâu ngập của ống tremie dưới đáy lạch biển sâu.",
        "\"Bắt đầu bơm bê tông! Giữ áp lực bơm ổn định ở mức không phẩy hai mươi lăm megapascal! Không được để nước biển tràn vào trong ống đổ!\" Đức Trung dõng dạc chỉ huy.",
        "Hỗn hợp bê tông UHPC siêu mác màu xám đen bắt đầu cuồn cuộn chảy xuống dưới lòng lạch biển sâu, đẩy dần lớp nước mặn ra ngoài bệ trụ cầu.",
        "Mưa bão xối xả tạt thẳng vào mặt anh lạnh buốt, sóng biển dữ dội chồm lên boong sà lan cẩu như muốn nuốt chửng cả tháp đổ bê tông khổng lồ.",
        "Thế nhưng, bằng sự điềm tĩnh thiên tài và những tính toán thủy lực học chuẩn xác đến từng milimet chịu lực của anh, quá trình đổ bê tông vẫn diễn ra trơn tru tuyệt đối.",
        "Hùng Sắt đứng từ trên bờ kè đá nhìn ra ngoài biển khơi, gã vô cùng kinh hoàng khi thấy ngọn hải đăng chỉ huy của Đức Trung vẫn sáng bừng sừng sững giữa mưa bão.",
        "Gã không ngờ rằng một thằng nhóc kỹ sư quèn lại có thể chỉ huy hàng trăm công nhân vượt qua được cơn bão cấp mười hai hung hãn để thi công siêu công trình.",
        "Càng điên cuồng tột độ, Hùng Sắt quyết định liều mạng dẫn theo ba tên đàn em mang theo kìm cộng lực định lẻn ra sàn đạo cắt cáp neo giữ sà lan đổ bê tông.",
        "Thế nhưng, mọi hành vi phá hoại đen tối của gã thầu phụ hung hãn đã nằm trọn trong kế hoạch dự phòng an ninh vô cùng chặt chẽ của Đức Trung và Thanh Lan.",
        "Ngay khi Hùng Sắt vừa đặt chân lên sàn đạo thi công định cắt cáp chịu lực, hệ thống đèn pha công suất lớn trên sà lan đột ngột bật sáng bừng chiếu thẳng vào mặt gã.",
        "Lực lượng Cảnh sát Hình sự phối hợp cùng an ninh công trường đã mật phục sẵn từ trước lập tức ập ra, khống chế và khóa chặt còng số tám vào tay gã thầu phụ cùng đồng bọn.",
        "\"Hùng Sắt! Ông bị bắt quả tang về hành vi cố ý phá hoại công trình an ninh quốc gia và vi phạm các quy định về xây dựng gây hậu quả nghiêm trọng!\" vị chỉ huy cảnh sát dõng dạc công bố.",
        "Hùng Sắt mặt xám ngoét như tro tàn, gã quỵ sụp xuống sàn đạo sũng nước mưa, nhận ra toàn bộ sự nghiệp giang hồ thầu phụ của gã chính thức sụp đổ hoàn toàn.",
        "Lúc này ngoài khơi xa, sau hơn mười tiếng đồng hồ chiến đấu kiên cường bất chấp bão táp gầm rú, mẻ bê tông bệ trụ cầu số bốn cuối cùng cũng hoàn thành hoàn hảo.",
        "Bệ trụ cầu vượt biển khổng lồ sử dụng công nghệ bê tông UHPC độc bản đã đông cứng vững chãi, cắm sâu vào lòng đáy biển như một pháo đài thép bất khả xâm phạm.",
        "Bão bắt đầu tan, những tia nắng bình minh đầu tiên rạng rỡ xuyên qua làn mây đen, chiếu sáng rực rỡ lên bệ trụ cầu sừng sững giữa biển khơi Hải Phòng.",
        "Toàn thể hàng trăm kỹ sư và công nhân trên công trường đồng loạt reo hò vang dội, nhiều người đã ôm lấy nhau khóc nức nở vì vui mừng chiến thắng kỳ tích.",
        "Vũ Thanh Lan xúc động tột cùng, cô chạy đến bên cạnh Đức Trung, không kìm được lòng mình mà ôm chặt lấy bờ vai vững chãi đang đẫm nước mưa của anh.",
        "\"Đức Trung! Chúng ta đã làm được rồi! Anh thực sự là một thiên tài cầu đường vĩ đại nhất mà tôi từng được biết!\" cô nghẹn ngào nói đầy ngưỡng mộ.",
        "Đức Trung khẽ vỗ nhẹ lên vai cô đầy ấm áp, đôi mắt anh nhìn ra phía bệ trụ cầu đang lấp lánh dưới ánh nắng bình minh ấm áp đầu ngày mới.",
        "\"Đây mới chỉ là trụ cầu đầu tiên của siêu công trình này, hành trình hợp long toàn tuyến đường cao tốc vượt biển của chúng ta vẫn còn rất dài,\" anh điềm tĩnh nói.",
        "\"Nhưng tôi chắc chắn rằng, từ nay về sau sẽ không còn bất kỳ kẻ tham lam nào dám bén mảng đến đây để bòn rút công trình của chúng ta nữa,\" anh dứt khoát tuyên bố.",
        "Tin tức về việc thi công bệ trụ cầu số bốn thành công vượt qua cơn bão cấp mười hai lịch sử bằng công nghệ UHPC nhanh chóng chấn động giới xây dựng toàn quốc.",
        "Lê Khắc Nam đang ngồi trong văn phòng ở Hà Nội nghe tin Hùng Sắt bị bắt khẩn cấp và công trình của Đức Trung hoàn thành hoàn hảo thì lập tức ngã quỵ xuống ghế.",
        "Lão biết rõ rằng việc sụp đổ của đồng bọn Hùng Sắt sẽ sớm kéo theo toàn bộ cuộc điều tra tham nhũng bòn rút ngân sách nhắm thẳng vào chiếc ghế Viện phó của lão.",
        "Chiến thắng giòn giã bước đầu ngoài thực địa Hải Phòng đã khẳng định vị thế thiên tài cầu đường vô song của Hoàng Đức Trung trước toàn bộ dư luận xã hội.",
        "Anh đã dùng chính chuyên môn siêu việt và ý chí sắt đá của mình để vả mặt trực tiếp gã sếp cũ tráo trở và đè bẹp những thế lực đen tối cản đường.",
        "Thanh Lan đứng bên cạnh anh dưới nắng ấm bình minh, gương mặt sắc sảo xinh đẹp rạng rỡ nụ cười hạnh phúc ngập tràn sự tin tưởng tuyệt đối vào người đàn ông bên cạnh.",
        "Hai người cùng nhau đứng trên nhịp cầu dẫn lộng gió nhìn về phía tương lai tươi sáng của con đường cao tốc vượt biển nghìn tỷ đang từ từ hiện ra trước mắt."
    ]
    
    # Run and write
    w1 = save_chapter(1, "Chương 1: Bản Vẽ Bị Đánh Cắp", chap1_sentences)
    w2 = save_chapter(2, "Chương 2: Cuộc Gặp Gỡ Định Mệnh", chap2_sentences)
    w3 = save_chapter(3, "Chương 3: Đấu Thầu Sòng Phẳng", chap3_sentences)
    w4 = save_chapter(4, "Chương 4: Khởi Công Giữa Bão Táp", chap4_sentences)
    
    print("=" * 40)
    print(f"🎉 All 4 chapters written successfully!")
    print(f"Chap 1: {w1} words")
    print(f"Chap 2: {w2} words")
    print(f"Chap 3: {w3} words")
    print(f"Chap 4: {w4} words")
    print("=" * 40)

if __name__ == "__main__":
    main()
