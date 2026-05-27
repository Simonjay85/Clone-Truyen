import json
import re
from pathlib import Path


SCRATCH = Path("/Users/aaronnguyen/TN/App/doctieuthuyet/scratch")


TARGET_COUNTS = {
    2190: 12,
    2129: 11,
    2120: 13,
    2112: 10,
}


def p(text):
    return f"<p>{text.strip()}</p>"


def wc(html):
    return len(re.findall(r"\w+", re.sub(r"<[^>]+>", " ", html)))


def chapter(title, blocks):
    return {"title": title, "content": "\n".join(p(x) for x in blocks)}


def renumber(chapters):
    for index, ch in enumerate(chapters, 1):
        subtitle = re.sub(r"^Chương\s+\d+\s*:\s*", "", ch["title"]).strip()
        ch["title"] = f"Chương {index}: {subtitle}"


EXTRA = {
    2190: [
        chapter("Chương 7: Tài Khoản Ma Ở Singapore", [
            "Manh mối từ công ty tư vấn Cầu Giấy dẫn Hoàng Đức Minh đến một tài khoản lưu ký mở tại Singapore. Nó không đứng tên Trần Minh Tuấn, cũng không đứng tên người thân của ông ta, mà đứng dưới một pháp nhân nghe rất sạch: North Bridge Advisory.",
            "An Nhiên không cho Minh kết luận vội. Cô yêu cầu đối chiếu thời điểm nhận tiền với từng nhịp bán khống HNC. Khi ba giao dịch nhỏ cùng rơi vào đúng ba phút trước tin giả được tung ra, căn phòng như lạnh đi dù máy điều hòa đã tắt.",
            "Tuấn phản công bằng cách gửi đơn tố Minh rửa tiền xuyên biên giới. Đòn này độc hơn mọi bài báo bẩn, vì chỉ cần cơ quan chức năng mở điều tra ngược, toàn bộ hồ sơ cứu khách hàng sẽ chậm lại. Minh phải vừa chứng minh dòng tiền không thuộc về mình, vừa không để khách hàng hoảng loạn bán tháo lần nữa.",
            "Một nhân viên ngân hàng lưu ký cũ đồng ý gặp họ ở quán ăn nhỏ gần phố Huế. Anh ta không muốn làm nhân chứng, nhưng đưa ra một chi tiết: tài khoản North Bridge từng dùng cùng số điện thoại khôi phục với tài khoản tài xế của Tuấn. Đó là một lỗi nhỏ của kẻ quen nghĩ tiền có thể rửa sạch mọi dấu chân.",
            "Minh mang chi tiết ấy về ghép với log IP. Từ đây, đường dây không còn là vài lệnh sai lệch trong nước. Nó là kế hoạch chuyển lợi nhuận ra ngoài trước khi quỹ Phương Bắc sụp xuống, để người nghèo ôm lỗ còn kẻ dựng bẫy biến mất sau lớp vỏ tư vấn quốc tế.",
        ]),
        chapter("Chương 8: Cú Gọi Từ Mẹ", [
            "Đêm trước cuộc họp nhà đầu tư, mẹ Minh gọi điện. Bà nói trước cửa nhà có người lạ đứng hút thuốc suốt một tiếng. Họ không đập cửa, không chửi bới, chỉ để lại trên tay nắm cửa một phong bì chứa ảnh bệnh án của bà.",
            "Minh gần như muốn bỏ hết để chạy về. An Nhiên giữ anh lại bằng một câu thẳng: nếu anh rời bàn chứng cứ lúc này, Tuấn sẽ có cả mẹ anh lẫn hồ sơ khách hàng. Cách bảo vệ bà tốt nhất là làm cho người sai không còn khả năng ra lệnh.",
            "Anh nhờ công an khu vực kiểm tra camera, đồng thời gọi người hàng xóm thân nhất đưa mẹ sang nhà họ trong đêm. Bà không khóc. Bà chỉ dặn anh đừng vì sợ mà ký vào thứ mình không làm. Giọng bà nhỏ, nhưng đủ kéo Minh khỏi cơn run.",
            "Sáng hôm sau, nhóm truyền thông của Tuấn tung tin Minh dùng mẹ bệnh để xin lòng thương. Minh đọc tiêu đề, đặt điện thoại úp xuống. Anh không còn phản ứng như nạn nhân nữa. Anh bắt đầu ghi lại mọi tài khoản phát tán đầu tiên, vì tin bẩn cũng có đường đi của tiền.",
            "An Nhiên tìm thấy ba fanpage tài chính cùng nhận thanh toán quảng cáo từ một thẻ doanh nghiệp liên quan North Bridge. Bằng chứng truyền thông bẩn nối vào bằng chứng dòng tiền. Tuấn tưởng đánh vào gia đình sẽ làm Minh gãy; ông ta không biết vừa tự nối thêm một đoạn dây vào cổ mình.",
        ]),
        chapter("Chương 9: Biên Bản Trước Giờ Mở Cửa", [
            "Sáu giờ sáng, Minh, An Nhiên và đại diện nhóm nhà đầu tư có mặt tại văn phòng công chứng. Tập hồ sơ dày đến mức phải chia thành ba bìa: dữ liệu giao dịch, dòng tiền, và truyền thông thao túng.",
            "Công chứng viên đọc từng trang chậm rãi. Minh sốt ruột vì thị trường sắp mở cửa, nhưng An Nhiên bắt anh ngồi yên. Một dấu mộc đặt đúng chỗ có sức nặng hơn mười lời thanh minh trên mạng.",
            "Trong lúc chờ, khách hàng lớn nhất của quỹ gọi đến. Ông nói nếu Minh không công bố ngay, ông sẽ rút đơn làm nhân chứng để tự bảo vệ công ty mình. Minh hiểu nỗi sợ ấy. Không ai muốn tên mình nằm giữa scandal tài chính.",
            "Minh không năn nỉ. Anh gửi cho ông bản timeline đã niêm phong và hỏi một câu: nếu hôm nay ông im lặng, ngày mai nhân viên của ông có chắc không bị dùng tiền hưu trí làm lá chắn không. Đầu dây bên kia im rất lâu, rồi ông nói sẽ đến cuộc họp.",
            "Khi con dấu cuối cùng hạ xuống, bảng điện cũng vừa mở phiên. HNC rung lắc mạnh, nhưng không rơi sàn. Thị trường như đang nín thở chờ một người nói ra phần còn thiếu của sự thật.",
        ]),
        chapter("Chương 10: Tin Nhắn Tự Hủy", [
            "Trước giờ họp, Hạnh gửi cho Minh một bản ghi màn hình mới. Điện thoại cũ của cô còn lưu ứng dụng chat nội bộ đã bị xóa khỏi máy công ty. Trong đó, Tuấn dùng chế độ tin nhắn tự hủy để chỉ đạo tắt camera phòng họp số ba.",
            "Vấn đề là bản ghi màn hình rất dễ bị luật sư phản bác. An Nhiên yêu cầu Hạnh giao luôn thiết bị, kèm lịch sử sao lưu và mã định danh máy. Hạnh sợ, vì chiếc điện thoại đó cũng chứa ảnh gia đình. Minh cam kết chỉ trích xuất phần liên quan dưới sự chứng kiến của kỹ thuật viên độc lập.",
            "Khi dữ liệu được phục hồi, họ thấy một chuỗi chỉ đạo dài hơn tưởng tượng. Tuấn không chỉ gài Minh. Ông ta còn chuẩn bị danh sách khách hàng sẽ được bồi thường trước để giữ im lặng, còn khách nhỏ bị đẩy vào nhóm kiện tụng kéo dài.",
            "Minh đọc danh sách, thấy tên bác về hưu đã hỏi anh tiền dưỡng già. Cơn giận lần này không ồn ào. Nó nằm trong cách anh đặt tài liệu vào bìa riêng, ghi rõ ưu tiên phong tỏa tài sản để trả cho khách nhỏ trước.",
            "Tin nhắn tự hủy không tự hủy được lòng tham. Nó chỉ làm lộ cách lòng tham nghĩ mình thông minh hơn mọi người. Minh bước vào hội trường với mảnh ghép cuối cùng, không còn cảm giác đơn độc như ngày bị kéo khỏi phòng giao dịch.",
        ]),
    ],
    2129: [
        chapter("Chương 7: Hội Đồng Đạo Đức Bị Mua Im", [
            "Sau kết quả sắc ký, Trần Huy Hoàng tưởng hội đồng đạo đức y sinh sẽ lập tức yêu cầu dừng K-Serum. Nhưng biên bản cuộc họp nội bộ lại ghi rằng phản ứng phụ chưa đủ cơ sở kết luận, cần tiếp tục theo dõi thêm ba tháng.",
            "Ba tháng là quá dài với bệnh nhân men gan đang tăng từng ngày. Lâm Tuệ Nghi đọc kỹ danh sách thành viên hội đồng và phát hiện hai người đang nhận tài trợ nghiên cứu từ quỹ phụ của Khang Thị. Khoản tài trợ không sai trên giấy, nhưng thời điểm chuyển tiền thì bẩn.",
            "Hoàng tìm đến một bác sĩ từng phản đối biên bản. Ông không muốn xuất hiện vì sợ mất phòng nghiên cứu, chỉ đưa cho anh bản nháp có dòng cảnh báo bị xóa. Trong bản nháp ấy, cụm 'nguy cơ nghiêm trọng ở nhóm gene hiếm' bị đổi thành 'biến thiên sinh học cần theo dõi'.",
            "Tuệ Nghi lập tức xin bảo toàn email trao đổi hội đồng. Khang Thị phản ứng bằng công văn tố Hoàng quấy rối nhân viên y tế. Họ muốn biến người gõ cửa xin cứu bệnh nhân thành kẻ gây áp lực bất hợp pháp.",
            "Hoàng không gõ cửa thêm. Anh chuyển toàn bộ mẫu và dữ liệu ẩn danh cho một nhóm chuyên gia độc lập ở Đại học Y. Khi chữ ký thứ ba của chuyên gia xuất hiện dưới báo cáo, hội đồng không còn có thể trốn sau câu chữ mềm.",
        ]),
        chapter("Chương 8: Ca Bệnh Không Có Trong Báo Cáo", [
            "Một điều dưỡng gọi cho Hoàng lúc gần sáng. Có một bệnh nhân tử vong sau khi dùng K-Serum thử nghiệm, nhưng hồ sơ được ghi là suy gan do bệnh nền. Gia đình nghèo, không có luật sư, thi thể đã chuẩn bị hỏa táng.",
            "Hoàng và Tuệ Nghi đến bệnh viện trong mưa. Họ không được phép tiếp cận hồ sơ ngay, chỉ có thể gặp người chị của bệnh nhân ở hành lang. Người phụ nữ cầm túi thuốc, nói em trai cô từng khỏe hơn sau mũi đầu, rồi vàng da rất nhanh sau mũi thứ hai.",
            "Tuệ Nghi giải thích mọi rủi ro pháp lý nếu gia đình đồng ý giám định lại. Không có lời hứa thắng kiện, chỉ có cơ hội biết sự thật. Người chị ký giấy bằng bàn tay run rẩy.",
            "Kết quả giải phẫu bệnh cho thấy tổn thương gan trùng với mẫu phản ứng phụ mà Hoàng dự đoán. Ca này không nằm trong báo cáo IPO, không nằm trong bản trình Cục, cũng không nằm trong danh sách bồi thường kín.",
            "Đêm đó, Hoàng ngồi trước cửa nhà xác rất lâu. Anh từng muốn lấy lại tên công trình. Giờ anh hiểu nếu chỉ dừng ở danh dự của mình, anh cũng sẽ trở thành một dạng ích kỷ. Vụ kiện phải mang tên những người không còn tự nói được.",
        ]),
        chapter("Chương 9: Bản Thỏa Thuận Một Nghìn Tỷ", [
            "Đường Vĩnh Khang gửi người đến gặp Tuệ Nghi với đề nghị hòa giải. Một nghìn tỷ cho trung tâm nghiên cứu mới, phục hồi tên Hoàng trong nhóm sáng chế, đổi lại là cam kết không công bố lỗi quy trình tinh lọc trước khi Khang Thị tái cấu trúc IPO.",
            "Đề nghị ấy đủ lớn để làm bất kỳ người làm khoa học nào chao đảo. Hoàng có thể xây lab, cứu nhiều dự án khác, và cuối cùng được gọi đúng là tác giả. Nhưng cái giá là những bệnh nhân đã chịu phản ứng phụ sẽ tiếp tục bị ghi thành thống kê mờ.",
            "Tuệ Nghi không khuyên anh nhận hay từ chối. Cô chỉ đặt hai tập giấy lên bàn: bản thỏa thuận và hồ sơ ca tử vong bị giấu. Một bên là tương lai cá nhân, một bên là sự thật đã có người trả bằng mạng.",
            "Hoàng ký, nhưng không ký vào bản hòa giải. Anh ký đơn bổ sung chứng cứ hình sự, kèm yêu cầu điều tra hành vi che giấu biến cố bất lợi nghiêm trọng. Tuệ Nghi nhìn chữ ký của anh, lần đầu mỉm cười rất nhạt.",
            "Khang gọi trực tiếp cho Hoàng, giọng không còn đạo mạo. Ông ta nói Hoàng đang tự tay giết tương lai thuốc Việt. Hoàng đáp rằng thuốc Việt không cần tương lai xây trên bệnh án bị chôn. Cuộc gọi ấy được ghi âm hợp pháp và trở thành viên đá cuối trong bức tường chứng cứ.",
        ]),
    ],
    2120: [
        chapter("Chương 7: Bữa Cơm Nhà Vợ Trước Giông", [
            "Trước ngày đại tiệc, bà Tuyết gọi Quốc Bảo về nhà ăn cơm. Bàn ăn vẫn sang, chén vẫn sáng, nhưng mọi người nhìn anh khác đi. Không phải tôn trọng, mà là dè chừng vì anh đang nắm hợp đồng có thể làm Minh Hùng rơi tự do.",
            "Bà Tuyết đặt trước mặt anh giấy cam kết không nhắc chuyện gia đình trong tiệc Michelin. Đổi lại, bà hứa sẽ thuyết phục Ngọc Mai không ly hôn. Quốc Bảo nhìn tờ giấy, nhận ra họ vẫn nghĩ danh dự của anh là thứ có thể mặc cả.",
            "Ngọc Mai ngồi cuối bàn, môi mím chặt. Lần đầu cô nói mẹ mình sai khi bắt Bảo rửa bát để mua vui cho họ hàng. Câu nói không lớn, nhưng làm cả bàn im. Bà Tuyết tái mặt, Minh Hùng đập đũa xuống bàn.",
            "Bảo không ký. Anh cũng không làm ầm. Anh nói chuyện bếp núc và chuyện gia đình giống nhau ở một điểm: thứ đã ôi thì không thể che bằng nước sốt đậm. Muốn ăn cùng bàn, trước hết phải bỏ thói xem người khác là rác dưới chân.",
            "Rời biệt thự, anh nghe tiếng biển chuyển gió. Cơn giông đang tới, đúng như lịch thời tiết. Với một bếp trưởng, giông không chỉ làm ướt khách; nó đổi độ mặn, đổi nhiệt than, đổi cả thời gian món ăn ra bàn.",
        ]),
        chapter("Chương 8: Mẻ Nước Mắm Bị Tráo", [
            "Sáng hôm sau, tổ nước mắm Hàm Ninh báo tin mẻ nhĩ dành cho món chính có mùi lạ. Quốc Bảo mở nắp chum, chỉ cần ngửi đã biết có người pha nước mắm công nghiệp vào để làm gãy hậu vị.",
            "Nếu tố ngay, cả tổ hợp sẽ mang tiếng làm hàng kém. Nếu im, món ăn thất bại và Lê Hữu Đạt có cớ nói nguyên liệu địa phương không đủ chuẩn Michelin. Đòn này nhắm vào người nghèo nhiều hơn nhắm vào Bảo.",
            "Anh yêu cầu niêm phong toàn bộ chum, lấy mẫu so sánh với mẻ lưu trong chai thủy tinh bà tổ trưởng giữ cho gia đình. Mẫu lưu có độ đạm và mùi cá cơm sạch; chum chính bị pha thêm chất điều vị rẻ tiền.",
            "Camera nhà thùng cho thấy một xe giao đá của Minh Hùng ghé qua lúc rạng sáng. Người trên xe đeo khẩu trang, nhưng bước đi cà nhắc vì vết thương cũ ở chân. Bảo nhận ra đó là phụ bếp từng theo Lê Hữu Đạt.",
            "Quỳnh Chi lập biên bản, còn Bảo quyết định đổi kỹ thuật món chính. Thay vì dùng nước mắm nhĩ làm nền sốt, anh dùng vài giọt như điểm kết, để lượng mẫu sạch còn lại đủ phục vụ toàn bộ khách. Kẻ phá nguyên liệu không ngờ chính sự thiếu hụt lại buộc món ăn tinh tế hơn.",
        ]),
        chapter("Chương 9: Cơn Mưa Trên Sân Tiệc", [
            "Một giờ trước khi khách đến, mưa đổ xuống bãi biển. Sảnh ngoài trời không thể dùng theo thiết kế ban đầu. Đội tổ chức hoảng loạn vì mọi thứ từ ánh sáng đến hướng phục vụ đều phải đổi.",
            "Royal Food lập tức gửi tin cho báo chí rằng Marriott tổ chức thiếu chuyên nghiệp. Lê Hữu Đạt xuất hiện trong bộ vest trắng, đề nghị chuyển sang thực đơn dự phòng của ông ta vì món của Bảo phụ thuộc than biển và sân mở.",
            "Bảo nhìn mưa, rồi yêu cầu dựng bếp than vào khu hành lang kính. Hơi nước biển ngoài trời được thay bằng nước dùng tôm cô đặc, còn mùi khói than được kiểm soát bằng gáo dừa đã ngâm muối. Anh không chống thời tiết; anh đổi cách để thời tiết thành một phần món ăn.",
            "Đội bếp ban đầu rối, nhưng Bảo chia lại trạm: một người giữ nhiệt, một người lau đĩa, một người canh hơi nước trên kính để món ra không bị nguội. Quỳnh Chi tháo giày cao gót, trực tiếp bê khay thử đường phục vụ mới.",
            "Khi vị khách đầu tiên bước vào sảnh kính nhìn mưa quất ngoài biển, món khai vị tỏa hương tiêu đỏ vừa kịp ra bàn. Không gian tưởng hỏng lại trở thành trải nghiệm riêng của Phú Quốc mùa giông.",
        ]),
        chapter("Chương 10: Người Phụ Bếp Quay Lưng", [
            "Phụ bếp từng tráo nước mắm bị giữ lại sau khi camera được trích xuất. Cậu ta tên Lộc, mới hai mươi ba tuổi, nợ tiền viện phí cho cha và bị Lê Hữu Đạt ép làm bẩn nguyên liệu để trả nợ.",
            "Minh Hùng muốn đẩy hết tội lên Lộc để thoát. Bà Tuyết cũng nói một thằng phụ bếp nghèo thì tham tiền là đúng. Bảo nghe câu ấy, thấy lại hình ảnh mình bên bồn rửa. Người có tiền luôn nghĩ người nghèo sinh ra để gánh tội thay.",
            "Bảo không tha trắng. Anh yêu cầu Lộc ký lời khai đầy đủ, giao tin nhắn và tài khoản nhận tiền. Đổi lại, anh đề nghị Quỳnh Chi hỗ trợ pháp lý để cậu ta không bị biến thành vật tế thần duy nhất.",
            "Lộc bật khóc, khai ra điểm giao tiền ở bến tàu và người trung gian của Royal Food. Dữ liệu chuyển khoản nối Minh Hùng với Lê Hữu Đạt, rồi nối tiếp đến hợp đồng độc quyền nguyên liệu. Một phụ bếp nhỏ kéo sập được mắt xích mà luật sư lớn cố giấu.",
            "Bảo nhìn Lộc ký tên, không thấy hả hê. Anh biết người sai phải chịu trách nhiệm, nhưng anh cũng biết không thể xây một căn bếp tử tế bằng cách để kẻ nghèo nhất chịu hết lửa thay kẻ ra lệnh.",
        ]),
        chapter("Chương 11: Món Chính Không Có Trong Menu", [
            "Đến lượt món chính, Bảo không phục vụ đúng món đã in trong menu. Anh đổi thành 'Cá mú giông biển, tiêu đỏ và một giọt nhĩ Hàm Ninh'. Quyết định đổi món trước khách Michelin là cực kỳ nguy hiểm.",
            "Quỳnh Chi nhìn anh chờ giải thích. Bảo nói nếu cố bám menu cũ sau khi nguyên liệu bị phá và thời tiết đổi, anh chỉ đang nấu cho cái tôi của mình. Fine dining không phải thuộc lòng công thức; nó là trung thực với điều kiện thật.",
            "Món cá được hấp bằng hơi nước dùng tôm, da áp chảo giòn rất mỏng, sốt tiêu đỏ không phủ kín mà kéo thành một đường cạnh đĩa. Giọt nước mắm nhĩ cuối cùng được đặt bằng đầu thìa gỗ, ít đến mức nhiều người tưởng trang trí.",
            "Trưởng đoàn thẩm định nếm xong hỏi vì sao nước mắm ít như vậy. Bảo trả lời vì nó từng suýt bị làm bẩn, nên phần sạch còn lại phải được dùng như lời chứng, không phải làm nền. Người phiên dịch ngập ngừng, rồi dịch đủ từng chữ.",
            "Cả sảnh lặng đi. Món ăn bỗng mang câu chuyện của nhà thùng, cơn mưa, người phụ bếp, và một đầu bếp từng bị bắt rửa bát. Đó là thứ Lê Hữu Đạt không thể sao chép, vì ông ta chỉ biết cướp công thức, không biết chịu trách nhiệm với nguồn gốc.",
        ]),
    ],
    2112: [
        chapter("Chương 7: Khách Hàng Đi Xe Cũ", [
            "Giữa lúc truyền thông chú ý siêu xe, một người đàn ông chạy xe tải cũ tìm đến Nam. Xe của ông không đắt, không có carbon ceramic, nhưng phanh cũng bị một xưởng liên kết với Vương gia thay phụ tùng kém rồi tính giá chính hãng.",
            "Nam kiểm tra và phát hiện cùng một kiểu gian: mã phụ tùng bị đổi trên hóa đơn, cảm biến báo mòn bị reset để xe qua đăng kiểm. Đường dây không chỉ nhắm vào người giàu mua bảo hiểm siêu xe. Nó ăn cả tiền của người lao động cần xe để kiếm sống.",
            "Khánh Vy đề nghị tách vụ xe tải ra sau cho gọn hồ sơ. Nam không đồng ý. Nếu chỉ cứu siêu xe, anh sẽ bị biến thành chuyên gia phục vụ giới nhiều tiền. Nghề sửa xe của anh bắt đầu từ những chiếc xe cũ, và danh dự của nghề nằm ở chỗ không phân biệt giá xe.",
            "Họ thu thập thêm mười hai hóa đơn từ tài xế công nghệ, chủ xe tải nhỏ và một gia đình mua xe cũ trả góp. Mỗi hóa đơn là một con số không lớn, nhưng ghép lại thành bằng chứng hệ thống.",
            "Khi danh sách nạn nhân được công bố, dư luận đổi hẳn. Vụ việc không còn là drama của Lamborghini và hầm B2. Nó là câu hỏi: bao nhiêu người đang lái xe với niềm tin giả rằng phanh của mình đã được sửa đúng?",
        ]),
        chapter("Chương 8: Bài Test Trên Băng Thử", [
            "Để khóa miệng nhóm luật sư, Nam đề nghị kiểm tra công khai trên băng thử phanh. Một chiếc Aventador, một xe tải cũ và một sedan gia đình được đưa vào cùng quy trình, cùng camera, cùng thiết bị đo độc lập.",
            "Vương Thế Hùng cử chuyên gia đến giám sát, cố bắt lỗi từng thao tác của Nam. Anh không khó chịu. Anh đọc to từng bước, để mọi người thấy kỹ thuật chuẩn không cần che trong phòng kín.",
            "Kết quả xe tải làm nhiều người lạnh sống lưng hơn siêu xe. Ở tải trọng cao, phanh sau lệch lực đủ khiến xe văng đuôi khi xuống dốc. Chủ xe đứng ngoài nhìn màn hình, mặt tái đi vì tuần trước ông vừa chở con gái về quê bằng chiếc xe đó.",
            "Nam giải thích không màu mè: lỗi này có thể giết người, và nó bị bỏ qua vì nạn nhân không đủ nổi tiếng để lên báo. Câu nói ấy khiến Khánh Vy quyết định tài trợ gói kiểm tra phanh miễn phí cho toàn bộ xe từng qua xưởng liên quan.",
            "Lê Duy cố nói băng thử bị can thiệp. Nam mời chính chuyên gia của Vương gia lặp lại phép đo. Kết quả không đổi. Trong kỹ thuật, có những con số không biết nịnh ai. Và hôm đó, từng con số đứng về phía những người từng bị xem thường.",
        ]),
    ],
}


def main():
    for story_id, target in TARGET_COUNTS.items():
        path = SCRATCH / f"rewrite_{story_id}_v13.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        additions = EXTRA[story_id]
        if len(data["chapters"]) >= target:
            continue
        needed = target - len(data["chapters"])
        final = data["chapters"][-1]
        data["chapters"] = data["chapters"][:-1] + additions[:needed] + [final]
        renumber(data["chapters"])
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        print(story_id, len(data["chapters"]))


if __name__ == "__main__":
    main()
