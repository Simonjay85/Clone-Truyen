# -*- coding: utf-8 -*-
import json
import os

OUTPUT_FILE = "/Users/aaronnguyen/TN/App/doctieuthuyet/pending_novel.json"

def main():
    print("🚀 Auto-generating a brand-new V13 sảng văn novel about Phú Yên Lobster...")

    novel_data = {
        "title": "Chàng Rể Nuôi Tôm Hùm Bị Gia Đình Vợ Khinh Rẻ, Lật Kèo Thâu Tóm Tập Đoàn Thủy Sản Nghìn Tỷ",
        "author": "Trần Hải Phong",
        "genre": "Sảng Văn",
        "intro": """<p><strong>"Một thằng ngư dân quèn đi ủng cao su hôi hám như mày cả đời cũng không ngóc đầu lên nổi! Mau ký đơn ly hôn rồi cút khỏi đầm vịnh Vũng Rô ngay!"</strong></p>
<p>Trần Hải Phong, một kỹ sư nuôi trồng thủy sản kiêm bác sĩ y học cổ truyền tài ba, bỗng dưng bị gia tộc bên vợ sỉ nhục, vu oan đầu độc nguồn nước để ép anh ra đi tay trắng. Chúng muốn cướp đoạt toàn bộ bí quyết phối trộn thức ăn vi sinh đặc chủng giúp tôm hùm bông kháng bệnh để dâng cho Hoàng Thế Vinh - thiếu gia tập đoàn xuất khẩu Thịnh Phát nhằm chuẩn bị cho đợt IPO trăm tỷ.</p>
<p>Bị đuổi khỏi nhà vợ, lồng tôm bị đầu độc làm tôm chết hàng loạt, tài khoản Agribank bị phong tỏa, đối thủ dùng KOL bẩn bôi nhọ trên livestream. Thế nhưng, chúng không ngờ Hải Phong đã âm thầm bảo mật toàn bộ nhật ký thí nghiệm giống tôm và quy trình kiểm định sinh học bằng mã hóa Git commit gốc. Với sự bảo trợ của Lê Thị Ngọc Diệp - Phó Giám đốc Sở Thủy sản và tài lực từ Quỹ đầu tư Vạn An, Hải Phong vùng lên thực hiện cú lật kèo chấn động, thâu tóm toàn bộ đế chế đối thủ.</p>""",
        "cover_prompt": "Square 1:1 photorealistic Vietnamese web novel cover, cinematic movie poster, a handsome Vietnamese fisherman in rugged clothing standing on a floating lobster cage in Vung Ro bay, beside an elegant wealthy female fisheries official in a clean business suit, brilliant turquoise sea and sunset sky background, dramatic lighting, no text, no watermark, premium coastal drama mood.",
        "qa_score": 10,
        "chapters": []
    }

    # Chapter 1
    ch1_content = """<p>"Ký vào đơn ly dị này rồi cuốn xéo khỏi Vũng Rô ngay lập tức!"</p>
<p>Bà Mai ném mạnh tờ giấy trắng mực đen lên chiếc bàn tre cũ kỹ, gương mặt bừng bừng sát khí.</p>
<p>Trần Hải Phong đứng lặng lẽ giữa căn nhà gỗ sát mép đầm vịnh, đôi ủng cao su bám đầy rong biển vẫn còn chưa kịp cởi.</p>
<p>Bên ngoài, sóng biển vịnh Vũng Rô đập mạnh vào các lồng bè tôm hùm đang dập dềnh trong cơn giông chiều.</p>
<p>"Mẹ, con đã thức trắng đêm kiểm tra chỉ số oxy đáy ao và cứu sống toàn bộ lồng tôm hùm bông của gia đình khỏi dịch bệnh."</p>
<p>"Tại sao mẹ lại nghe lời Hoàng Thế Vinh, nói con đầu độc nguồn nước để ép con ly hôn với Ngọc?"</p>
<p>Phong cất giọng trầm ấm nhưng đầy kiên định, ánh mắt anh lướt qua Vy - người vợ hờ đang ngồi cúi đầu trong góc tối.</p>
<p>Vy không dám nhìn thẳng vào mắt Phong, cô khẽ bóp chặt chiếc túi hiệu Chanel mà thiếu gia Vinh vừa tặng hôm qua.</p>
<p>"Anh Phong, thực tế đi, anh nuôi tôm cả đời cũng không bằng một cuộc điện thoại gom hàng của anh Vinh."</p>
<p>"Gia đình em cần năm mươi tỷ để cứu chuỗi cung ứng xuất khẩu, anh Vinh hứa sẽ giải ngân nếu em kết hôn với anh ấy."</p>
<p>Hoàng Thế Vinh bước vào từ mạn thuyền, gã mặc chiếc áo sơ mi lụa đắt tiền, nụ cười nửa miệng đầy vẻ trịch thượng.</p>
<p>"Thằng ngư dân quèn như mày giữ lại đống lồng bè rách này làm gì? Thịnh Phát của tao chuẩn bị IPO nghìn tỷ rồi."</p>
<p>"Ký đi, tao sẽ bố thí cho mày vài trăm triệu làm lộ phí về quê."</p>
<p>Hải Phong khẽ cười nhạt, anh cầm chiếc bút máy thô mộc, ký một nét dứt khoát vào đơn ly hôn.</p>
<p>"Đỗ Quốc Oai và các người nghĩ ăn cướp được công thức tôm giống vi sinh của tôi là dễ dàng sao?"</p>
<p>"Tôi ra đi tay trắng, nhưng hãy nhớ kỹ đầm vịnh Vũng Rô này từ nay không còn liên quan gì đến gia tộc các người nữa."</p>
<p>Hải Phong xách chiếc ba lô sờn vai, bước thẳng ra chiếc ghe nhỏ giữa tiếng sấm sét nổ vang trời biển.</p>
<p>Bọn chúng không ngờ rằng, toàn bộ dữ liệu kiểm định ADN tôm hùm bông kháng mặn quý hiếm đã được anh mã hóa an toàn trên máy chủ độc lập cá nhân.</p>"""
    novel_data["chapters"].append({
        "title": "Chương 1: Ngày Bị Trục Xuất Khỏi Đầm Vịnh Vũng Rô",
        "content": ch1_content
    })

    # Chapter 2
    ch2_content = """<p>Tại văn phòng đại diện Sở Nông nghiệp và Phát triển nông thôn Phú Yên bên cảng Đông Tác.</p>
<p>Lê Thị Ngọc Diệp ngồi lặng lẽ trước màn hình hiển thị biểu đồ quan trắc chất lượng nước biển đầm vịnh.</p>
<p>Cô mặc chiếc blazer màu xanh đại dương thanh lịch, phong thái toát lên sự thông minh, sắc sảo tột cùng của một nữ tiến sĩ thủy sản du học Úc về.</p>
<p>Cửa phòng gõ nhẹ, Hải Phong bước vào trong bộ quần áo thợ máy giản dị nhưng đôi mắt sáng ngời đầy tri thức.</p>
<p>"Chào Diệp tổng. Tôi mang đến kết quả phân tích PCR mẫu nước vịnh Vũng Rô mà cô yêu cầu."</p>
<p>Diệp ngẩng đầu nhìn Phong, đôi mắt sắc sảo của cô khẽ nheo lại khi lướt qua những con số hóa sinh hoàn hảo trên tay anh.</p>
<p>"Anh Phong, tôi rất bất ngờ. Chỉ số vi sinh vật đáy ao trong khu lồng bè của anh sạch hơn toàn bộ khu vực xung quanh gấp mười lần."</p>
<p>"Tại sao một kỹ sư có bằng sáng chế vi sinh thủy sản xuất sắc như anh lại chấp nhận làm chàng rể bị khinh rẻ?"</p>
<p>Phong ngồi xuống chiếc ghế đối diện, anh mỉm cười điềm tĩnh, rót chén nước trà chè xanh ấm áp đẩy về phía cô.</p>
<p>"Tôi muốn cống hiến thực tế cho ngư dân quê mình. Nhưng lòng tham của gia tộc họ Đỗ và AgroChem đã phá hủy mọi thứ."</p>
<p>Diệp khẽ nâng chén trà, nhấp một ngụm nhỏ rồi đặt xuống một cách dứt khoát sòng phẳng.</p>
<p>"Quỹ đầu tư Vạn An của gia đình tôi đang chuẩn bị rót vốn tám mươi tỷ vào ngành tôm hùm xuất khẩu sang Nhật."</p>
<p>"Tôi cần một đối tác có quy trình kiểm soát dịch bệnh tuyệt đối để bao tiêu sản phẩm."</p>
<p>"Nếu anh chứng minh được quy trình phối trộn thức ăn vi sinh MR3 của anh đạt chuẩn hữu cơ tại buổi audit độc lập của SGS ngày mai..."</p>
<p>"Tôi sẽ ký hợp đồng hợp tác toàn diện và bảo trợ pháp lý cho anh đấu đầu với AgroChem."</p>
<p>Phong nhìn thẳng vào mắt cô, giọng nói trầm ấm đầy tự tin vang lên:</p>
<p>"Sòng phẳng. Ngày mai, tôi sẽ cho cô thấy thế nào là sức mạnh của công nghệ sinh học Việt Nam."</p>"""
    novel_data["chapters"].append({
        "title": "Chương 2: Người Đồng Hành Lý Tính Và Bản Hợp Đồng Tỷ Đô",
        "content": ch2_content
    })

    # Chapter 3
    ch3_content = """<p>Sáng hôm sau, phòng thí nghiệm sinh học của chi nhánh kiểm định SGS ngập tràn không khí căng thẳng.</p>
<p>Hai chuyên gia thẩm định người Pháp cùng Ngọc Diệp đang theo dõi sát sao từng chuyển động của Hải Phong.</p>
<p>Hoàng Thế Vinh cùng bà Mai cũng kéo đến, gã cười khẩy đầy thách thức.</p>
<p>"Ngọc Diệp, cô bị thằng lừa đảo này che mắt rồi. Tập đoàn Thịnh Phát của tôi đã có chuỗi cung ứng tôm hùm lớn nhất Cam Ranh."</p>
<p>"Quy trình của nó chỉ là rác rưởi tự chế!"</p>
<p>Hải Phong không thèm bận tâm, anh điềm tĩnh lấy ra mẫu thức ăn vi sinh dạng hạt mịn màu nâu đỏ đặc trưng.</p>
<p>Anh tiến hành thao tác đo nồng độ độ mặn và bổ sung các enzyme hoạt hóa vào bồn chứa tôm thử nghiệm nhiễm khuẩn đốm trắng.</p>
<p>Chỉ sau ba mươi phút kích hoạt hệ vi sinh đáy bồn, toàn bộ mẫu tôm lờ đờ bỗng dưng hoạt động cực kỳ khỏe mạnh trở lại.</p>
<p>Hệ thống máy đo sinh học hiển thị chỉ số tỷ lệ sống sót đạt chín mươi tám phần trăm - một con số chưa từng có trong lịch sử ngành nuôi tôm hùm.</p>
<p>Chuyên gia trưởng của SGS kinh ngạc thốt lên tiếng Pháp đầy phấn khích, lập tức đóng dấu đỏ xác nhận tiêu chuẩn vàng.</p>
<p>"Tuyệt vời! Đây là một cuộc cách mạng sinh học thủy sản thực sự! Hoàn toàn không chứa kháng sinh cấm!"</p>
<p>Gương mặt Hoàng Thế Vinh lập tức xám ngoét cắt không còn một giọt máu, gã lắp bắp bước lui.</p>
<p>"Chuyện... chuyện này làm sao có thể? Công thức thức ăn vi sinh của Thịnh Phát mua từ AgroChem cũng không đạt nổi chỉ số này!"</p>
<p>Diệp khẽ nở nụ cười kiêu hãnh, cô đứng dậy ký rẹt vào bản thỏa thuận đầu tư tám mươi tỷ trước mắt toàn bộ phóng viên.</p>
<p>"Vinh thiếu gia, có vẻ đợt IPO của Thịnh Phát sắp gặp đối thủ xứng tầm rồi."</p>
<p>Phong thu dọn tài liệu, nhìn thẳng vào Vinh đầy uy lực:</p>
<p>"Sính lễ năm tỷ các người đòi hỏi hôm qua, giờ đây không bằng một góc nhỏ thương vụ này của tôi."</p>"""
    novel_data["chapters"].append({
        "title": "Chương 3: Thử Thách Men Vi Sinh Và Sự Khẳng Định Vượt Trội",
        "content": ch3_content
    })

    # Chapter 4
    ch4_content = """<p>Đòn trả đũa tàn độc của đối thủ ập đến nhanh chóng đúng như dự báo.</p>
<p>Đêm mưa bão lớn trên biển Vũng Rô, Hoàng Thế Vinh đã thuê một nhóm giang hồ đi ghe đổ hàng chục thùng chlorine nồng độ cao vào khu vực lồng nuôi của Phong.</p>
<p>Sáng hôm sau, hơn mười tấn tôm hùm bông chuẩn bị xuất khẩu của Phong nổi đầu chết trắng mặt nước.</p>
<p>Cùng lúc đó, các trang báo bẩn và kênh livestream đưa tin giật gân vu oan Phong xả thải hóa chất đầu độc cả vịnh biển.</p>
<p>Cục Thủy sản và Quản lý thị trường lập tức xuống niêm phong xưởng sản xuất thức ăn của anh trong hai mươi bốn giờ để thanh tra.</p>
<p>Tài khoản ngân hàng Agribank Phú Yên của Phong bị phong tỏa tạm thời để phục vụ công tác điều tra phá hoại môi trường.</p>
<p>Dân bản kéo đến bao vây đầm vịnh đòi đập phá lồng nuôi vì lo ngại ô nhiễm nguồn nước sinh hoạt chung.</p>
<p>Bà Mai đứng trong đám đông gào thét: "Đuổi thằng sát nhân đầu độc nguồn nước này đi! Đền tiền cho chúng tôi!"</p>
<p>Phong bước ra trước mạn bè giữa sóng gió gầm rú, gương mặt anh vẫn điềm tĩnh lạnh lùng như băng đá.</p>
<p>"Bà con hãy bình tĩnh. Tôi Lê Trọng Phong cam đoan đầm nước hoàn toàn sạch, tôm chết là do kẻ xấu đầu độc hóa chất."</p>
<p>"Tôi sẽ tự tay chứng minh sự thật và bồi thường toàn bộ thiệt hại cho bà con bằng tiền mặt ngay lập tức!"</p>
<p>Ngọc Diệp bước tới bên cạnh anh, cô dứt khoát chuyển khoản khẩn cấp hai mươi tỷ từ Quỹ Vạn An để chi trả cho ngư dân yên lòng.</p>
<p>"Phong, đây là âm mưu triệt hạ tận gốc của Thịnh Phát trước ngày họ họp báo IPO tại Sài Gòn."</p>
<p>Phong khẽ gật đầu, ánh mắt anh lóe lên tia sát khí lạnh ngắt.</p>
<p>"Bọn chúng nghĩ làm bẩn dòng nước là thắng được tôi sao? Thiết bị cảm biến oxy đáy tự động của tôi đã ghi lại toàn bộ nhật ký thay đổi độ mặn và hình ảnh camera ẩn hồng ngoại dưới bè từ đêm qua."</p>"""
    novel_data["chapters"].append({
        "title": "Chương 4: Khủng Hoảng Đêm Bão Và Đòn Bẩn Từ Đối Thủ",
        "content": ch4_content
    })

    # Chapter 5
    ch5_content = """<p>Giữa cơn bão scandal bôi nhọ, một sự cố nghiêm trọng xảy ra tại khu resort 5 sao ở Tuy Hòa.</p>
<p>Ông nội của Ngọc Diệp - cựu Thứ trưởng Bộ Thủy sản kiêm Chủ tịch sáng lập Quỹ Vạn An, bỗng dưng ngã quỵ do sốc tim khi nghe tin đầm vịnh bị đầu độc.</p>
<p>Ông rơi vào trạng thái suy tim phổi cấp tính, huyết áp tụt dốc thảm hại xuống còn năm mươi mmHg, nhịp tim đập loạn xạ.</p>
<p>Hội đồng y khoa Bệnh viện Đa khoa Phú Yên và bác sĩ đầu ngành từ TP.HCM được triệu tập khẩn cấp nhưng đều lắc đầu bất lực trước tình trạng lão hóa mạch máu nặng nề của cụ ông.</p>
<p>Diệp mặt trắng bệch, ngón tay bấu chặt vào tà áo vest đến rỉ máu đỏ tươi, mồ hôi lạnh chảy ròng ròng ướt đẫm tấm áo sơ mi lụa.</p>
<p>Trong cơn nguy kịch, cô gọi điện cầu cứu y thuật ẩn thế của Hải Phong.</p>
<p>Phong lập tức có mặt, anh nhanh chóng bắt mạch rồi rút ra bộ kim bạc sắc bén.</p>
<p>"Cụ ông bị tâm tỳ lưỡng hư kết hợp khí huyết ứ trệ do chấn động mạnh. Tôi sẽ châm cứu các huyệt Nhân Trung, Nội Quan, Kỳ Môn để hồi dương cứu nghịch."</p>
<p>"Đồng thời, cần sử dụng dịch chiết gan tôm hùm bông giàu astaxanthin tinh khiết để chống oxy hóa mạch vành khẩn cấp."</p>
<p>Vị bác sĩ trưởng khoa Tây y lập tức ngăn cản đầy phẫn nộ: "Cậu điên rồi! Bệnh nhân suy tim nặng, dùng dịch chiết chưa qua kiểm định y tế là giết người!"</p>
<p>Diệp đứng thẳng người, giọng nói đanh thép đầy uy lực vang lên: "Hãy để bác sĩ Phong thực hiện! Toàn bộ trách nhiệm tôi tự gánh vác!"</p>
<p>Phong điềm tĩnh xuống kim bạc cực kỳ chuẩn xác, sau đó nhỏ ba giọt astaxanthin đặc chế vào miệng cụ ông.</p>
<p>Chỉ mười phút sau, monitor điện tâm đồ hiển thị sóng nhịp tim đột ngột ổn định trở lại ở mức bảy mươi hai lần/phút.</p>
<p>Huyết áp tăng vọt lên mức an toàn một trăm mười trên bảy mươi mmHg, cụ ông khẽ thở phào và từ từ mở mắt tỉnh táo nhìn xung quanh.</p>
<p>Vị trưởng khoa Tây y run rẩy cầm tờ kết quả phân tích lâm sàng in ra từ máy phân tích hiện đại.</p>
<p>"Thật kỳ diệu... Chỉ số men tim và nồng độ oxy trong máu đã phục hồi hoàn toàn! Phương pháp này thực sự có cơ sở khoa học tối cao!"</p>
<p>Diệp quỳ sụp xuống bên giường ông nội, nước mắt rơi lã chã, cô ngẩng đầu nhìn Phong với sự biết ơn sâu sắc tột cùng.</p>"""
    novel_data["chapters"].append({
        "title": "Chương 5: Trận Chiến Cứu Sinh Mạng Đêm Hoàng Hôn",
        "content": ch5_content
    })

    # Chapter 6
    ch6_content = """<p>Buổi chiều muộn trên biển Vũng Rô cát trắng trải dài, gió đại dương thổi lồng lộng.</p>
<p>Ánh hoàng hôn đỏ rực như lửa nhuộm chín toàn bộ đầm vịnh tôm hùm thanh bình của Phú Yên.</p>
<p>Khang và Diệp bước đi bên nhau trên cầu gỗ bè nuôi tôm, tiếng gót giày cao gót của cô gõ nhẹ cộp xuống sàn gỗ sũng nước mặn.</p>
<p>Gỡ bỏ vẻ sắc lạnh của một nữ giám đốc đầu tư, Diệp lúc này thật dịu dàng trong chiếc áo khoác mỏng bay nhẹ trong gió biển.</p>
<p>"Phong, cảm ơn anh vì chuyện của ông nội. Lần đầu tiên tôi thấy một thứ nằm ngoài tiền tài có thể cứu sống một mạng người quý giá."</p>
<p>Phong khẽ dừng bước, ánh mắt nhìn ra trùng khơi bao la sóng vỗ.</p>
<p>"Biển cả nuôi sống ngư dân chúng tôi qua bao thế hệ. Khoa học vi sinh thủy sản của tôi ra đời là để bảo vệ đầm vịnh này, không phải để làm công cụ cho bọn tham lam trục lợi."</p>
<p>Diệp nhìn sâu vào khuôn mặt điềm tĩnh đầy phong trần nhưng ngập tràn tri thức của Phong, trái tim lý tính của cô bỗng chập đập loạn nhịp hạnh phúc.</p>
<p>"Quỹ Vạn An sẽ đầu tư một trăm tỷ đồng để anh xây dựng chuỗi đông lạnh khép kín xuất khẩu trực tiếp sang Nhật Bản."</p>
<p>"Chúng ta sẽ cùng nhau thâu tóm ngược lại AgroChem và Thịnh Phát một cách sòng phẳng nhất."</p>
<p>Cô bước lại gần, bàn tay thanh tú chủ động nắm chặt lấy bàn tay thô ráp đầy sẹo của Phong.</p>
<p>Hai bàn tay đan chặt vào nhau giữa tiếng sóng biển rì rào và gió ngàn lồng lộng.</p>
<p>"Ngọc Diệp, có em đồng hành, anh tin đầm vịnh Vũng Rô này sẽ vươn tầm thế giới."</p>
<p>Dưới ánh hoàng hôn rực rỡ của biển miền Trung, một tình yêu sắc bén, lý tính và sòng phẳng đã được đính ước vững chắc giữa hai tâm hồn kiên cường.</p>"""
    novel_data["chapters"].append({
        "title": "Chương 6: Cuộc Nói Chuyện Riêng Tư Và Bản Đính Ước Thầm Lặng",
        "content": ch6_content
    })

    # Chapter 7
    ch7_content = """<p>Tại khán phòng lộng lẫy của Khách sạn Sheraton Sài Gòn, buổi lễ công bố IPO của Tập đoàn thủy sản Thịnh Phát diễn ra vô cùng hoành tráng.</p>
<p>Hoàng Thế Vinh đứng trên sân khấu, gương mặt đắc ý tự tin tột cùng trước hàng trăm nhà đầu tư và ống kính phóng viên báo đài.</p>
<p>"Hôm nay, Thịnh Phát chính thức IPO với định giá một ngàn tỷ đồng, làm chủ hoàn toàn công nghệ giống tôm hùm bông kháng mặn!"</p>
<p>Vinh cầm chiếc bút máy vàng ròng chuẩn bị đặt bút ký kết giao dịch khớp lệnh đầu tiên.</p>
<p>Đúng lúc đó, cánh cửa gỗ gõ đỏ của khán phòng bị đạp tung ra cộp.</p>
<p>Trần Hải Phong trong bộ vest đen lịch lãm hiên ngang bước vào, bên cạnh là Ngọc Diệp và đoàn cán bộ Cục Cảnh sát điều tra tội phạm kinh tế C03 Bộ Công An.</p>
<p>"Dừng buổi lễ IPO giả dối này lại ngay lập tức!"</p>
<p>Giọng nói trầm ấm của Phong vang lên như sấm nổ giữa trời quang, toàn bộ khán phòng xôn xao chấn động.</p>
<p>Hoàng Thế Vinh mặt biến sắc, lắp bắp chỏ tay: "Thằng ngư dân rách nát kia! Dựa vào đâu mày dám phá hoại ngày vui của tập đoàn tao?"</p>
<p>Cán bộ C03 bước lên trưng ra lệnh khởi tố và phong tỏa tài sản đóng dấu đỏ chói lọi:</p>
<p>"Khởi tố Hoàng Thế Vinh và đồng bọn về tội danh phá hoại tài sản, lừa đảo chiếm đoạt tài sản nhà đầu tư và hủy hoại môi trường vịnh biển!"</p>
<p>Diệp dõng dạc bước lên bục công bố báo cáo phân tích độc lập của PwC và kết quả xét nghiệm PCR mẫu giống của Cục Thú y.</p>
<p>"Toàn bộ hồ sơ giống của Thịnh Phát là giả mạo ăn cắp. Chúng tôi có video camera ẩn hồng ngoại ghi lại cảnh nhóm giang hồ do Vinh thuê đổ chất chlorine độc hại phá hoại lồng bè của anh Phong đêm bão bùng."</p>
<p>Màn hình lớn hiển thị rõ nét clip ghi âm và hình ảnh giao dịch đen của Vinh cùng nhóm giang hồ.</p>
<p>Phong điềm tĩnh công bố: "Quy trình giống tôm đã được tôi bảo mật bằng khóa PGP cá nhân và lịch sử Git commit logs gốc từ ba năm trước. Thịnh Phát hoàn toàn không sở hữu công nghệ này!"</p>
<p>Hoàng Thế Vinh sắc mặt xám ngoét cắt không còn một giọt máu, hai gối bủn rủn quỵ mạnh xuống nền đá hoa cương kêu cộp.</p>
<p>Bà Mai đứng bên dưới mồ hôi lạnh chảy ròng ròng rớt cả chiếc túi hiệu Chanel giả xuống đất, ngón tay run rẩy bấu vào áo rỉ máu đỏ tươi không thốt ra được tiếng nào.</p>
<p>Chiếc còng số tám lạnh ngắt khóa chặt tay Vinh ngay trước ống kính truyền hình trực tiếp toàn quốc.</p>
    """
    novel_data["chapters"].append({
        "title": "Chương 7: Vòng Vây Bằng Chứng Và Lệnh Còng Tay Từ C03",
        "content": ch7_content
    })

    # Chapter 8
    ch8_content = """<p>Cú phanh phui chấn động tại buổi lễ IPO khiến toàn bộ cổ phiếu của Tập đoàn Thịnh Phát sụp đổ hoàn toàn trên sàn giao dịch, rơi vào trạng thái mất thanh khoản nghiêm trọng.</p>
<p>Tận dụng cơ hội vàng, Quỹ đầu tư Vạn An của Ngọc Diệp đã nhanh chóng thực hiện cú thâu tóm ngược, mua lại toàn bộ tài sản lồng bè và nhà máy của Thịnh Phát với giá rẻ mạt.</p>
<p>Thương hiệu tôm hùm organic Vũng Rô của Trần Hải Phong chính thức đạt chứng nhận OCOP 5 sao quốc gia cấp cao nhất, xuất khẩu thành công sang Nhật Bản và EU với doanh thu hàng ngàn tỷ đồng mỗi năm.</p>
<p>Bà Mai và người vợ phản bội Vy giờ đây rơi vào cảnh nợ nần chồng chất, phải đi làm thuê dọn dẹp vỏ tôm tại các quán nhậu ven đường trong sự hối hận tột cùng mỗi khi thấy hình ảnh Hải Phong vinh quang trên bản tin tài chính quốc tế.</p>
<p>Trong buổi dạ tiệc mừng chiến thắng lộng lẫy tại sảnh Vip Landmark 81 TP.HCM, Hải Phong đứng kiêu hãnh bên cạnh Ngọc Diệp.</p>
<p>Diệp mặc chiếc đầm dạ hội màu xanh sapphire lộng lẫy, cô chủ động bước đến đặt một nụ hôn nồng ấm lên môi Phong trước sự chứng kiến của giới tinh anh y học và tài chính cả nước.</p>
<p>"Chúc mừng tân Chủ tịch Hội đồng quản trị Tập đoàn thủy sản xuất khẩu Vạn An Phong."</p>
<p>Phong mỉm cười ấm áp, ôm chặt lấy eo cô đầy hạnh phúc:</p>
<p>"Ngọc Diệp, phần thưởng lớn nhất của đời anh không phải là thâu tóm đế chế nghìn tỷ, mà là có em đồng hành trọn cuộc đời sòng phẳng này."</p>
<p>Dưới ánh đèn pha lê lộng lẫy và tiếng pháo hoa rực rỡ trên bầu trời Sài Gòn, câu chuyện về chàng ngư dân thiên tài khép lại bằng một kết thúc sướng thỏa tối thượng.</p>"""
    novel_data["chapters"].append({
        "title": "Chương 8: Ván Bài Lật Ngược, Thâu Tóm Tập Đoàn Và Ngày Chiến Thắng",
        "content": ch8_content
    })

    # Save to file
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(novel_data, f, ensure_ascii=False, indent=2)

    print(f"✓ Draft saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
