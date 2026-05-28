#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from pathlib import Path

TITLE = "Bị Cả Nhà Vợ Đuổi Khỏi Xưởng Trà, Tôi Dùng Sổ Cân Lá Thâu Tóm Vùng Nguyên Liệu Đà Lạt"

INTRO = (
    '<p><strong>"Thứ ở rể như anh chỉ đáng bốc bao trà mốc ngoài sân, đừng mơ chạm vào hợp đồng trăm tỷ của nhà tôi."</strong></p>'
    '<p>Trong đêm mưa Cầu Đất, Lê Minh Quân bị nhà vợ xé thẻ nhân viên, vu cho tráo lô trà hữu cơ và đẩy ra khỏi xưởng trước mặt hàng chục nông hộ.</p>'
    '<p>Nhưng họ không biết người đàn ông im lặng ấy đang giữ ba thứ có thể lật tung cả vùng nguyên liệu: sổ cân lá gốc, mẫu dư lượng thuốc cỏ đã niêm phong, và nhật ký kho lên men bị giấu trong ổ cứng cũ.</p>'
    '<p>Khi tập đoàn ngoại đến Đà Lạt ký hợp đồng xuất khẩu, Quân trở lại. Lần này, kẻ từng bắt anh quỳ giữa nền kho ướt sẽ phải tự tay đặt con dấu chuyển nhượng lên bàn.</p>'
)

COVER_PROMPT = (
    "Square format, ultra-realistic cinematic real-life photo, high-stakes intense Vietnamese drama movie scene, "
    "inside a stormy tea warehouse in Cau Dat, Da Lat, wet concrete floor, tea crates, sealed sample bags, stamped ledgers, "
    "a calm handsome Vietnamese man in a rain-damp navy work jacket standing beside a sharp Vietnamese female executive in a dark green blazer, "
    "an arrogant wealthy businessman kneeling in panic while clutching a contract and tea residue report, workers and security behind them, "
    "dark at the TOP 30% for title readability, dramatic high-contrast lighting, no text, no letters, no watermarks, no logos, no badges, square 1:1."
)

CHAPTERS = [
    {
        "title": "Chương 1: Đêm Mưa Trước Cửa Kho Trà",
        "content": """
<p>Mưa ở Cầu Đất rơi rất nhỏ, nhưng lạnh đến mức người đứng dưới mái tôn cũng thấy các khớp tay buốt lên.</p>
<p>Lê Minh Quân cúi người buộc lại dây bao tải, lòng bàn tay còn dính nhựa lá trà non. Anh vừa kiểm xong lô hàng ba tấn chuẩn bị gửi xuống cảng Cát Lái thì cánh cửa kho bật mở.</p>
<p>Trần Quốc Bảo bước vào cùng vợ cũ của Quân, Mai Hương. Sau lưng họ là bà Nhã, mẹ Hương, khoác khăn lụa đắt tiền nhưng vẫn nhăn mặt vì mùi lá ẩm.</p>
<p>Bảo ném một tập giấy xuống nền xi măng. Những tờ biên bản kiểm nghiệm trượt trên vũng nước, mép giấy thấm đen.</p>
<p><strong>"Lô trà hữu cơ số bảy có dư lượng thuốc cỏ vượt ngưỡng. Chữ ký xuất kho là của anh."</strong></p>
<p>Quân nhìn tờ giấy, rồi nhìn con dấu photo nhòe ở góc phải. Anh nhận ra ngay mẫu mã phiếu nội bộ của xưởng đã bị sửa. Dòng thời gian lấy mẫu ghi tám giờ tối, trong khi camera khu sơ chế hôm ấy bị bảo trì từ sáu giờ.</p>
<p>Anh chưa kịp nói, Hương đã rút thẻ nhân viên trên cổ anh. Sợi dây đứt phựt, cạnh nhựa quệt qua da cổ để lại một vệt đỏ.</p>
<p>"Anh đừng diễn nữa. Tôi biết anh cay vì ly hôn không lấy được cổ phần. Nhưng hại cả hợp đồng xuất khẩu thì hèn quá."</p>
<p>Câu ấy khiến mấy nông hộ đứng ngoài cửa kho xì xào. Ông Lộc, người chở lá từ đồi số ba xuống, ôm chiếc nón cũ trong tay, mắt tránh đi. Họ không ghét Quân. Họ chỉ sợ nhà máy ngừng cân lá.</p>
<p>Bà Nhã bước tới, mũi giày da dừng sát tờ biên bản ướt. "Thứ ở rể như anh chỉ đáng bốc bao trà mốc ngoài sân, đừng mơ chạm vào hợp đồng trăm tỷ của nhà tôi."</p>
<p>Bảo cười khẽ. Hắn là giám đốc vận hành mới, người vừa được nhà họ Mai giao toàn bộ vùng nguyên liệu. Trên cổ tay hắn, chiếc đồng hồ vàng bắt ánh đèn kho lạnh như một lưỡi dao mỏng.</p>
<p>"Quân, quỳ xuống xin lỗi đi. Tôi sẽ cho anh một tháng lương và giấy xác nhận nghỉ việc tự nguyện. Nếu anh cãi, sáng mai đơn tố cáo phá hoại kinh doanh sẽ nằm ở Công an thành phố Đà Lạt."</p>
<p>Quân cúi nhặt một tờ giấy. Nước mưa làm nhòe chữ, nhưng số mã mẫu vẫn còn rõ: CD-7B-0426. Không phải mã từ đồi hữu cơ. Đó là mã kho phụ ở cuối thung lũng, nơi Bảo mới thuê người ngoài phun thuốc để ép năng suất.</p>
<p>Anh ngẩng lên. "Cho tôi kiểm lại sổ cân lá gốc và mẫu lưu trong tủ niêm phong."</p>
<p>Hương bật cười. Tiếng cười của cô không lớn, nhưng rơi xuống nền kho nghe còn lạnh hơn mưa. "Anh vẫn nghĩ mình là kỹ sư trưởng à? Từ phút này, anh không được bước vào bất kỳ khu vực nào của Mai Trà."</p>
<p>Bảo giật chùm chìa khóa khỏi tay bảo vệ, tự mở tủ hồ sơ. Hắn lấy ra một cuốn sổ bìa xanh, giơ lên trước mặt mọi người, rồi ném vào thùng rác inox. "Sổ cân lá đã được số hóa. Bản giấy này vô giá trị."</p>
<p>Quân nhìn cuốn sổ rơi xuống, nước trà thừa trong thùng văng lên mép bìa. Anh nhớ từng dòng trong đó: cân của hộ ông Lộc, hộ chị Sen, độ ẩm từng mẻ, giờ xe vào cổng, chữ ký người nhận. Cuốn sổ ấy không chỉ là giấy. Nó là mồ hôi của mấy chục gia đình trên đồi.</p>
<p>Bà Nhã ra hiệu. Hai bảo vệ kẹp tay Quân kéo ra sân. Mưa tạt vào mặt, ướt cả áo khoác cũ. Trước khi bị đẩy khỏi cổng, anh nghe Bảo nói với Hương: "Sáng mai anh ký lại phụ lục vùng nguyên liệu với Golden Leaf. Đừng để thằng đó làm bẩn lễ ký."</p>
<p>Quân ngã xuống bậc đá. Đầu gối đập vào mép xi măng, đau nhói. Nhưng anh không quay lại chửi, cũng không van xin.</p>
<p>Anh chỉ thò tay vào túi trong áo khoác, chạm vào chiếc USB bọc trong túi chống ẩm. Bên trong là bản scan sổ cân lá trước ngày bị tráo, ảnh niêm phong mẫu lưu, và file log kho lên men mà anh sao lưu theo thói quen mỗi cuối ca.</p>
<p>Ở đầu đường, một chiếc xe màu đen dừng lại. Cửa kính hạ xuống, để lộ gương mặt người phụ nữ mặc blazer xanh sẫm. Ánh mắt cô lướt qua vết máu ở đầu gối Quân rồi dừng ở cánh cổng nhà máy đang đóng sầm.</p>
<p>"Anh là Lê Minh Quân?" cô hỏi.</p>
<p>Quân lau nước mưa trên cằm. "Còn cô là ai?"</p>
<p>"Nguyễn An Nhiên, giám đốc kiểm soát rủi ro của Golden Leaf Việt Nam. Tôi đến để xem ai đang phá hợp đồng trăm tỷ của chúng tôi."</p>
<p>Quân im vài giây. Sau cánh cổng, tiếng cười của Bảo vẫn còn vọng ra.</p>
<p>Anh đứng dậy, nhét chiếc USB sâu hơn vào túi áo. "Nếu cô muốn xem sự thật, đừng vào bằng cổng chính."</p>
"""
    },
    {
        "title": "Chương 2: Người Phụ Nữ Không Tin Lời Cầu Cứu",
        "content": """
<p>An Nhiên không đưa Quân lên xe ngay. Cô mở ô, đứng dưới mép mưa, nhìn anh từ đầu đến chân như đang kiểm một hồ sơ có quá nhiều chỗ bị tẩy xóa.</p>
<p>"Tôi không ký hợp đồng dựa trên lời kể của người vừa bị đuổi," cô nói. "Anh có bằng chứng, hay chỉ có uất ức?"</p>
<p>Câu hỏi thẳng đến mức ông tài xế phía sau cũng hơi khựng lại. Quân lại thấy dễ chịu. Ít nhất cô không thương hại anh.</p>
<p>Anh lấy điện thoại cũ, mở một ảnh chụp trong kho lạnh. Trên màn hình là túi mẫu lưu CD-7B-0426, dây niêm phong màu đỏ và vết xước nhỏ hình chữ V trên kẹp nhựa.</p>
<p>"Mã này không thuộc đồi hữu cơ số bảy. Nó là mẫu từ kho phụ thung lũng Đạ Nghịt. Người ký nhận là trợ lý của Trần Quốc Bảo."</p>
<p>An Nhiên nhận điện thoại, phóng to ảnh. Móng tay cô rất gọn, không sơn màu nổi. "Ảnh có thể dựng."</p>
<p>"Nên tôi cần lấy mẫu lưu thật trước khi họ hủy."</p>
<p>Cô nhìn về cổng xưởng. Bên trong, đèn phòng họp tầng hai sáng lên. Bảo đang chuẩn bị lễ ký cho sáng hôm sau, chắc chắn cũng chuẩn bị dọn hết dấu vết trong đêm.</p>
<p>"Nếu tôi giúp anh vào kho, anh làm được gì?"</p>
<p>"Tủ mẫu lưu có hai khóa. Một khóa ở phòng kỹ thuật, một khóa do kế toán kho giữ. Tôi không cần mở tủ. Tôi chỉ cần quay lại tem niêm phong, số cân, và camera hành lang trước khi chúng bị ghi đè."</p>
<p>An Nhiên im lặng lâu hơn. Rồi cô mở máy tính bảng, gọi cho bộ phận pháp chế của Golden Leaf. Cô không nhắc đến Quân như người tố giác; cô yêu cầu lập biên bản quan sát độc lập vì có dấu hiệu sai lệch mẫu kiểm nghiệm.</p>
<p>Mười phút sau, cô đưa Quân một chiếc áo mưa màu xám và thẻ khách tạm thời. "Anh đi với tư cách người hỗ trợ kỹ thuật cho bên mua. Nếu anh nói dối, tôi sẽ là người đầu tiên đưa anh ra khỏi cổng."</p>
<p>Quân gật đầu. "Được."</p>
<p>Họ vào bằng cổng phụ, nơi xe tải chở bã trà thường đi. Bảo không ngờ phía Golden Leaf xuất hiện lúc nửa đêm. Khi hắn thấy An Nhiên trong hành lang kho lạnh, nụ cười trên mặt cứng lại như lớp sáp gặp hơi lạnh.</p>
<p>"Giám đốc Nhiên, mai mới là lễ ký. Sao chị đến giờ này?"</p>
<p>"Tôi kiểm chứng rủi ro trước khi ký." Cô đưa văn bản điện tử cho hắn xem. "Đề nghị mở khu mẫu lưu."</p>
<p>Bảo liếc thấy Quân đứng sau cô. Gân ở thái dương hắn giật nhẹ. "Người này đã bị chúng tôi sa thải vì phá hoại. Cho anh ta vào là vi phạm quy định nội bộ."</p>
<p>An Nhiên không cao giọng. "Quy định nội bộ không lớn hơn điều khoản kiểm toán độc lập trong hợp đồng khung."</p>
<p>Một câu ấy khiến quản lý kho luống cuống đi tìm chìa. Quân bước vào hành lang lưu mẫu. Mùi lạnh, mùi lá lên men và mùi nhựa niêm phong quyện vào nhau. Anh không đụng vào tủ, chỉ giơ điện thoại quay một vòng chậm.</p>
<p>Túi CD-7B-0426 vẫn nằm đó. Nhưng dây niêm phong đã bị thay. Vết xước hình chữ V không còn.</p>
<p>Quân cúi xuống, soi dãy số trên tem mới. "Tem này xuất từ cuộn niêm phong tháng năm. Lô mẫu bị lấy từ tháng tư. Không thể dùng tem tháng năm trừ khi có người mở tủ sau đó."</p>
<p>Bảo cười khẩy. "Anh bịa giỏi thật. Tem nào chẳng giống tem nào."</p>
<p>Quân quay sang kế toán kho. Cô gái trẻ siết chặt chùm khóa, mặt tái đi. "Chị Hạnh, sổ xuất tem niêm phong nằm ở ngăn thứ ba bàn chị. Nếu không mở bây giờ, sáng mai chị sẽ là người chịu trách nhiệm thay họ."</p>
<p>Hạnh run tay. Cô nhìn Bảo. Hắn nghiến răng, ánh mắt tối sầm. Nhưng An Nhiên đã đặt máy quay xuống bàn.</p>
<p>"Mở sổ," cô nói.</p>
<p>Trong cuốn sổ nhỏ, dòng tem CD-7B-0426 được ghi xuất lúc 21 giờ 47 phút tối nay. Người nhận: trợ lý vận hành Phan Tuấn.</p>
<p>Không ai nói gì trong vài giây. Chỉ có tiếng máy lạnh chạy đều đều trên đầu.</p>
<p>Bảo giật cuốn sổ, nhưng Quân đã chụp lại. Hắn bước tới, vai căng lên, bàn tay bóp mạnh đến mức mép giấy cong lại.</p>
<p>"Một cái tem chưa chứng minh được gì."</p>
<p>Quân nhìn hắn. "Đúng. Nó chỉ chứng minh anh đang sợ."</p>
<p>Sắc mặt Bảo sa xuống. Mồ hôi rịn ở chân tóc dù trong kho lạnh chỉ mười sáu độ.</p>
<p>An Nhiên khép máy tính bảng. "Lễ ký ngày mai vẫn diễn ra. Nhưng nội dung sẽ khác."</p>
"""
    },
    {
        "title": "Chương 3: Sổ Cân Lá Bị Ném Vào Thùng Rác",
        "content": """
<p>Sáng hôm sau, hội trường Mai Trà được trang trí bằng hoa cẩm tú cầu trắng và dải lụa xanh. Bảng điện tử ghi dòng chữ hợp tác xuất khẩu sang Nhật Bản, trị giá một trăm hai mươi tỷ đồng.</p>
<p>Bà Nhã mặc áo dài nhung, cười với phóng viên. Mai Hương đứng cạnh Bảo, bàn tay đặt trên tập hợp đồng như đặt lên một chiếc ngai nhỏ. Cô đã quen với cảm giác mọi thứ thuộc về mình.</p>
<p>Khi Quân bước vào cùng An Nhiên, tiếng nói trong hội trường hạ xuống.</p>
<p>Bảo lập tức đứng dậy. "Tôi yêu cầu an ninh đưa người này ra ngoài."</p>
<p>An Nhiên đặt một tập phụ lục lên bàn. "Golden Leaf yêu cầu bổ sung điều kiện: toàn bộ dữ liệu cân lá và mẫu lưu ba tháng gần nhất phải được kiểm tra trước khi giải ngân đợt một."</p>
<p>Nụ cười của bà Nhã tắt đi. "Giám đốc Nhiên, chúng ta đã thống nhất rồi. Bên tôi có chứng nhận hữu cơ, có phòng kiểm nghiệm đối tác."</p>
<p>"Tôi cũng có chứng nhận sai lệch tem niêm phong lúc 21 giờ 47 phút tối qua."</p>
<p>Không khí đông cứng. Một phóng viên hạ máy ảnh xuống, mắt sáng lên như bắt được mùi tin lớn.</p>
<p>Bảo kéo ghế, cố giữ giọng mềm. "Có thể nhân viên kho thao tác nhầm. Việc nhỏ như vậy không nên ảnh hưởng hợp đồng."</p>
<p>Quân bước tới thùng rác inox đặt sau bục kỹ thuật. Anh không nói với Bảo. Anh cúi xuống, lấy ra cuốn sổ bìa xanh đã bị nước trà làm ố một góc. Cả hội trường nhìn anh như nhìn người nhặt lại một thứ rác rưởi.</p>
<p>Hương mím môi. "Anh định bày trò gì nữa?"</p>
<p>Quân mở cuốn sổ ở trang ngày mười tám tháng tư. "Hộ ông Lộc giao tám trăm bốn mươi ký lá từ đồi số ba, độ ẩm bảy mươi hai phần trăm. Xe vào cổng lúc 14 giờ 12 phút, biển số 49C-218.36. Người cân: tôi. Người giám sát: Phan Tuấn."</p>
<p>Anh đặt cạnh đó bản số hóa mà Bảo gửi cho Golden Leaf. Cùng ngày, cùng giờ, số cân bị đổi thành một tấn hai. Nguồn lá bị đổi từ đồi số ba sang đồi hữu cơ số bảy.</p>
<p>Ông Lộc đứng bật dậy. "Tôi chưa từng chở lá ở đồi số bảy. Đồi đó nhà tôi không có quyền hái."</p>
<p>Bảo đập bàn. "Ông già, ông nghĩ kỹ trước khi nói. Hợp đồng thu mua của nhà ông còn nằm trong tay chúng tôi."</p>
<p>Lời đe dọa bật ra quá nhanh. Phóng viên quay máy về phía ông Lộc. Người nông dân già siết chiếc mũ vải, các khớp ngón tay nổi lên trắng bệch.</p>
<p>Quân lấy thêm ba phiếu cân. "Không chỉ nhà ông Lộc. Sáu hộ bị nâng sản lượng trên giấy để hợp thức hóa lá từ kho phụ. Nếu lấy mẫu ở kho phụ, dư lượng thuốc cỏ chắc chắn vượt ngưỡng."</p>
<p>Hương nhìn Bảo. Lần đầu tiên trong mắt cô có một vết nứt. "Anh nói với em kho phụ chỉ để chứa bao bì."</p>
<p>Bảo nuốt khan. Yết hầu hắn trượt lên xuống. "Anh làm vậy để cứu công ty. Mùa này lá thiếu, nếu không ghép nguồn, hợp đồng chết."</p>
<p>"Cứu công ty bằng cách đổ tội cho tôi?" Quân hỏi.</p>
<p>Bảo không trả lời. Mồ hôi đã thấm thành mảng ở nách áo sơ mi trắng. Hắn đưa tay lau trán, nhưng bàn tay run nên quệt lệch xuống má.</p>
<p>Bà Nhã vẫn cố giữ dáng vẻ chủ tịch. "Dù có sai sót vận hành, anh Quân cũng không còn tư cách can thiệp. Gia đình tôi sẽ xử lý nội bộ."</p>
<p>An Nhiên mở máy chiếu. Trên màn hình xuất hiện thư pháp lý của Golden Leaf. "Không còn nội bộ nữa. Theo điều khoản bảo vệ vùng nguyên liệu, nếu bên bán gian lận nguồn lá, bên mua có quyền dừng giải ngân và yêu cầu đơn vị kiểm toán độc lập."</p>
<p>Cô dừng lại, nhìn Quân. "Nhưng nếu có bên thứ ba chứng minh được chuỗi truy xuất sạch và đứng ra mua lại vùng nguyên liệu hợp pháp, Golden Leaf có thể ký hợp đồng mới."</p>
<p>Cả hội trường quay sang Quân.</p>
<p>Bảo bật cười gằn, nhưng tiếng cười hụt hơi. "Anh ta? Một thằng ở rể bị đuổi khỏi nhà? Anh ta lấy gì mua vùng nguyên liệu?"</p>
<p>Quân mở USB, chiếu lên màn hình một hợp đồng ủy quyền. Sáu mươi bảy nông hộ đã ký thỏa thuận giao quyền đàm phán thu mua cho Hợp tác xã Trà Sạch Lang Biang, tổ chức mà anh âm thầm đăng ký từ ba tháng trước để bảo vệ họ khỏi bị ép giá.</p>
<p>Ông Lộc đứng lên đầu tiên. Rồi chị Sen, rồi thêm mười mấy người khác. Họ không vỗ tay. Họ chỉ đứng đó, lặng lẽ, như những cây trà lâu năm sau một mùa sương muối.</p>
<p>Bảo nhìn dãy người đứng lên, môi run cầm cập. Chiếc đồng hồ vàng trên cổ tay hắn va vào mép bàn, phát ra tiếng cạch khô khốc.</p>
"""
    },
    {
        "title": "Chương 4: Tài Khoản Hợp Tác Xã Bị Đóng Băng",
        "content": """
<p>Vòng phản đòn đầu tiên khiến Mai Trà mất quyền chủ động, nhưng Bảo chưa chịu thua.</p>
<p>Chiều hôm ấy, khi Quân cùng An Nhiên rời hội trường, điện thoại của ông Lộc rung liên tục. Mấy nông hộ báo hợp đồng thu mua bị hủy, xe của Mai Trà không lên đồi cân lá nữa. Đến tối, tài khoản hợp tác xã ở ngân hàng thương mại cổ phần ngoại thương Việt Nam bị tạm khóa theo yêu cầu rà soát giao dịch bất thường.</p>
<p>Tin đồn lan nhanh hơn sương. Trên các nhóm mạng địa phương, một tài khoản ẩn danh đăng bài nói Quân lập hợp tác xã ma để lừa nông dân ký giấy bán đất. Dưới bài, hàng trăm bình luận chửi anh là kẻ ăn cháo đá bát.</p>
<p>Đêm xuống, sân kho cũ của hợp tác xã sáng đèn. Lá tươi chất thành từng giỏ, không thể để quá lâu. Nếu qua đêm không sơ chế, hương sẽ gắt, búp non sẽ đen mép. Mỗi giờ trôi qua là tiền của nông hộ tan trong hơi ẩm.</p>
<p>Chị Sen ngồi trên bao tải, hai mắt đỏ hoe. "Quân, nếu mai không cân được, nhà chị mất trắng hai sào đầu mùa."</p>
<p>Quân cầm sổ ghi tay, tính lại công suất máy sao chè thủ công. Họ chỉ có một lò nhỏ của ông Lộc, dùng than sạch, mỗi mẻ được sáu mươi ký. Không đủ.</p>
<p>An Nhiên đứng bên bàn, không thúc ép. Cô gọi ba cuộc cho bộ phận pháp chế, hai cuộc cho ngân hàng, rồi khép máy. "Tài khoản bị khóa ít nhất hai mươi bốn giờ. Bên kia gửi đơn tố cáo dòng tiền không minh bạch."</p>
<p>Một cậu thanh niên đập tay vào thùng thiếc. "Thế là hết rồi. Mai Trà ép chúng ta chết đói."</p>
<p>Quân không trách cậu. Anh nhìn đống lá, nhìn hơi nước bám trên mái tôn. Lúc bị đuổi khỏi nhà vợ, anh còn chịu được. Nhưng nhìn lá của nông dân héo đi vì mình, ngực anh thắt lại.</p>
<p>"Không bán lá tươi nữa," anh nói.</p>
<p>Mọi người im phăng phắc.</p>
<p>Quân kéo bảng trắng ra. "Chúng ta làm mẻ trà trắng thủ công đầu tiên, chỉ lấy búp một tôm hai lá. Không cần tài khoản chuyển khoản tối nay. Tôi viết giấy nhận nợ cá nhân, có An Nhiên làm chứng, trả sau khi Golden Leaf kiểm mẫu."</p>
<p>An Nhiên ngẩng lên. "Anh đang đặt toàn bộ trách nhiệm lên tên mình."</p>
<p>"Đúng."</p>
<p>Cô nhìn anh một lúc, rồi lấy bút ký vào góc bảng kiểm mẫu. "Tôi không bảo lãnh tiền. Tôi chỉ xác nhận quy trình lấy mẫu độc lập. Làm sai, tôi dừng ngay."</p>
<p>Quân gật đầu. Chính sự lạnh lùng ấy làm quyết định của cô có trọng lượng.</p>
<p>Họ làm việc suốt đêm. Lá được trải mỏng trên nong tre, quạt gió chạy chậm để giữ hương. Quân hướng dẫn từng người đảo lá bằng cổ tay, không bóp mạnh. An Nhiên tháo đồng hồ đắt tiền, tự tay dán mã mẫu lên từng khay, chữ viết nhỏ và sắc.</p>
<p>Khoảng ba giờ sáng, một nhóm streamer kéo đến trước cổng. Họ bật đèn quay, la ó rằng hợp tác xã đang tiêu hủy chứng cứ. Ánh đèn trắng quét qua mặt chị Sen làm chị lùi lại.</p>
<p>Bảo xuất hiện sau nhóm người ấy, mặc áo khoác đen, miệng cười mỏng. "Quân, vẫn thích kéo người nghèo chết cùng mình à?"</p>
<p>Quân bước ra cổng, trên áo còn dính vụn lá. "Anh trả tiền cho họ đến livestream?"</p>
<p>Bảo dang tay. "Dư luận tự tìm sự thật thôi."</p>
<p>Một streamer dí điện thoại sát mặt Quân. "Anh có dám công khai sao kê tài khoản hợp tác xã không?"</p>
<p>"Tài khoản đang bị khóa theo đơn tố cáo của Trần Quốc Bảo," Quân nói rõ từng chữ. "Ngày mai mở lại, tôi sẽ công khai. Còn tối nay, mời mọi người quay đủ quy trình chúng tôi làm trà. Quay cả mã mẫu, cả cân điện tử, cả camera thời gian thực."</p>
<p>Câu trả lời khiến nhóm người chững lại. Họ đến để bắt cảnh hỗn loạn, không ngờ Quân mở cửa cho quay.</p>
<p>An Nhiên đứng trong kho, đưa găng tay cho một streamer nữ. "Muốn quay gần thì mặc đồ bảo hộ. Làm bẩn mẫu, tôi yêu cầu bồi thường."</p>
<p>Cô nói bình thản, nhưng ánh mắt khiến cô gái kia vội lùi nửa bước.</p>
<p>Đến rạng sáng, mẻ trà đầu tiên khô vừa tới. Hương thanh, nhẹ, có mùi mật hoa lẫn cỏ non sau mưa. Ông Lộc bốc một nhúm, đưa lên mũi, bàn tay chai sần run run.</p>
<p>"Lâu rồi tôi mới ngửi thấy mùi trà của đồi mình."</p>
<p>Quân không cười. Anh biết đây chỉ là một hơi thở nhỏ giữa cơn siết cổ.</p>
<p>Ngoài cổng, Bảo đứng trong sương, mặt xám lại. Hắn tưởng tài khoản bị khóa sẽ làm họ tan rã. Không ngờ chính đêm bị vây ấy lại biến kho cũ thành sân khấu công khai nhất.</p>
"""
    },
    {
        "title": "Chương 5: Mẫu Trà Đi Trong Thùng Đá",
        "content": """
<p>Bảy giờ sáng, An Nhiên đặt ba túi mẫu vào thùng đá có khóa niêm phong. Cô dán nhãn trước mặt camera của các streamer vẫn còn ngái ngủ, rồi yêu cầu hai bên ký vào biên bản.</p>
<p>Phòng kiểm nghiệm độc lập ở thành phố Hồ Chí Minh nhận mẫu lúc mười một giờ trưa. Kết quả nhanh cần sáu tiếng. Sáu tiếng ấy dài như cả mùa mưa.</p>
<p>Bảo dùng thời gian đó để đánh thêm một đòn. Hắn gửi cho báo địa phương một đoạn ghi âm cắt ghép, trong đó giọng Quân như đang nói "cứ nâng số cân lên, miễn đủ hợp đồng". Đoạn ghi âm lan ra, đè lên mọi nỗ lực của hợp tác xã.</p>
<p>Hương gọi cho Quân. Đây là cuộc gọi đầu tiên từ sau ngày ly hôn.</p>
<p>"Anh nói thật đi, đoạn ghi âm đó là gì?"</p>
<p>Quân nhìn màn hình một lúc. Ngoài sân, ông Lộc đang vá lại tấm bạt che lá. "Là cuộc họp tháng ba. Tôi nói câu đó để phản đối Bảo, nhưng đoạn đầu đã bị cắt."</p>
<p>Hương im lặng. Quân nghe tiếng thở cô rất nhẹ, như người đang đứng trong căn phòng quá rộng.</p>
<p>"Em từng có cơ hội hỏi anh trước khi xé thẻ nhân viên," anh nói.</p>
<p>Cô tắt máy.</p>
<p>Buổi chiều, Quân và An Nhiên đến phòng kiểm nghiệm nhận kết quả. Trong hành lang trắng, mùi cồn sát khuẩn phủ lên mùi trà bám trên áo. An Nhiên mở phong bì, đọc từng dòng.</p>
<p>Mẫu trà của hợp tác xã: dư lượng thuốc cỏ dưới ngưỡng phát hiện. Mẫu kho phụ do Quân giữ ảnh đối chiếu: vượt ngưỡng bảy lần. Đặc biệt, dấu vân quang trên bao mẫu kho phụ trùng với hóa chất bảo quản dùng ở nhà máy Mai Trà, không phải từ nông hộ.</p>
<p>An Nhiên khép giấy. "Đủ để dừng hợp đồng với Mai Trà. Nhưng chưa đủ để anh thâu tóm vùng nguyên liệu. Anh cần chứng minh họ cố ý gian lận, không phải tai nạn quản lý."</p>
<p>Quân lấy từ ba lô ra ổ cứng cũ. "Tôi có log kho lên men."</p>
<p>Cô nhìn ổ cứng, rồi nhìn anh. "Sao không đưa ngay từ đầu?"</p>
<p>"Vì trong đó có dữ liệu cá nhân của công nhân. Tôi cần lọc phần liên quan, tránh kéo người vô tội vào."</p>
<p>Lần đầu tiên, nét mặt An Nhiên dịu xuống một chút. "Anh bị đuổi khỏi cổng vẫn còn nghĩ cho họ?"</p>
<p>Quân cười nhạt. "Tôi làm ở đó sáu năm. Người sai không phải tất cả."</p>
<p>Họ ngồi trong một quán nhỏ gần sân bay Liên Khương, mở log bằng máy tính của An Nhiên. Dữ liệu hiện ra từng dòng: thời gian xe vào kho phụ, nhiệt độ buồng lên men, mã pallet, tài khoản đăng nhập.</p>
<p>Ngày mười tám tháng tư, tài khoản vận hành của Bảo đăng nhập lúc 23 giờ 12 phút, đổi mã nguồn lá từ kho phụ sang đồi hữu cơ số bảy. Sau đó, cùng tài khoản xóa cảnh báo dư lượng trên hệ thống nội bộ.</p>
<p>An Nhiên chụp màn hình, nhưng vẫn lắc đầu. "Tài khoản có thể bị dùng chung."</p>
<p>Quân mở thư mục camera cục bộ. "Nên tôi còn đoạn này."</p>
<p>Video đen trắng hiện lên. Bảo bước vào phòng server, tay cầm điện thoại, phía sau là trợ lý Phan Tuấn ôm thùng tem niêm phong. Góc camera không rõ mặt hoàn toàn, nhưng chiếc đồng hồ vàng và dáng đi lệch vai của hắn không lẫn được.</p>
<p>An Nhiên không nói gì. Cô tua lại ba lần, mỗi lần mặt càng lạnh.</p>
<p>"Tôi sẽ gửi hồ sơ cho pháp chế và đề nghị báo cáo Sở Nông nghiệp cùng Công an kinh tế địa phương. Nhưng anh cần chuẩn bị. Khi đòn này tung ra, bên kia sẽ không chỉ mất hợp đồng. Họ sẽ mất quyền kiểm soát cả vùng nguyên liệu."</p>
<p>Quân nhìn qua cửa kính. Bên ngoài, mưa đã ngừng, những vạt đồi xanh hiện lên sau mây thấp.</p>
<p>"Tôi không muốn họ mất vì tôi," anh nói. "Tôi muốn nông hộ không còn bị một nhà máy bắt nghẹt cổ."</p>
<p>An Nhiên gấp hồ sơ. "Vậy ngày mai anh phải nói câu đó trước tất cả mọi người. Không phải như người trả thù. Như người đủ tư cách nhận trách nhiệm."</p>
"""
    },
    {
        "title": "Chương 6: Hội Đồng Ở Khách Sạn Đà Lạt Palace",
        "content": """
<p>Cuộc họp khẩn được tổ chức tại một phòng hội nghị của khách sạn Đà Lạt Palace. Ngoài Golden Leaf và Mai Trà, còn có đại diện Sở Nông nghiệp, ngân hàng, đơn vị kiểm toán và ba mươi nông hộ lớn.</p>
<p>Bảo đến muộn mười phút. Hắn thay bộ vest đen, tóc chải kỹ, nhưng hai mắt đỏ vì mất ngủ. Hương đi bên cạnh, sắc mặt nhợt nhạt. Bà Nhã vẫn giữ vẻ cứng cỏi, song chiếc khăn lụa trên cổ bà buộc lệch.</p>
<p>An Nhiên trình bày kết quả kiểm nghiệm trước. Cô không thêm một tính từ nào. Chỉ số, mã mẫu, thời gian, chữ ký nhận. Chính sự khô khan ấy làm căn phòng nặng xuống.</p>
<p>Đến phần log kho, Bảo bật dậy. "Dữ liệu này do Lê Minh Quân đánh cắp. Không có giá trị pháp lý."</p>
<p>Đại diện kiểm toán đẩy kính. "Nếu dữ liệu trùng với máy chủ nội bộ và có hash thời gian, chúng tôi vẫn có thể dùng làm căn cứ kiểm tra."</p>
<p>Mồ hôi bắt đầu rịn trên trán Bảo. Hắn kéo cổ áo, nhưng nút trên cùng đã mở sẵn.</p>
<p>Bà Nhã quay sang Hương, nói nhỏ nhưng cả bàn vẫn nghe thấy: "Con xử lý chồng cũ của con đi."</p>
<p>Hương khép mắt một giây. Khi mở ra, cô không nhìn Quân mà nhìn Bảo. "Anh có làm không?"</p>
<p>Bảo sững lại. "Em hỏi anh trước mặt người ngoài?"</p>
<p>"Em hỏi trước khi ký bất cứ giấy nào nữa."</p>
<p>Căn phòng im. Bảo đưa tay nắm cạnh bàn. Đầu ngón tay hắn bấm mạnh, vùng da quanh móng trắng bệch.</p>
<p>Quân mở video. Hình ảnh Bảo trong phòng server hiện lên màn hình lớn. Khi đoạn hắn nhận thùng tem niêm phong xuất hiện, tiếng bút của đại diện ngân hàng rơi xuống bàn nghe rõ mồn một.</p>
<p>Bảo bước lùi một bước. Mặt hắn xám ngoét. "Camera này... camera này đã bị tháo."</p>
<p>"Camera chính bị tháo," Quân nói. "Camera giám sát nhiệt ở góc trên vẫn còn. Nó không ghi âm, nhưng ghi đủ giờ, đủ hình."</p>
<p>Phan Tuấn, trợ lý của Bảo, ngồi cuối phòng bỗng ôm mặt. Vai anh ta run lên. "Anh Bảo bảo em chỉ đổi tem, không sao đâu. Anh ấy nói nếu hợp đồng chết, cả xưởng mất việc."</p>
<p>Bảo quay phắt lại. "Câm miệng!"</p>
<p>Tiếng quát làm Phan Tuấn co rúm. Nhưng đại diện công an kinh tế đã ghi lại lời khai ban đầu.</p>
<p>An Nhiên đặt bản đề xuất mới lên bàn. Golden Leaf sẽ dừng hợp đồng với Mai Trà, chuyển sang ký biên bản ghi nhớ với Hợp tác xã Trà Sạch Lang Biang nếu hợp tác xã chứng minh năng lực sơ chế trong bốn mươi lăm ngày. Khoản ứng trước được giải ngân qua tài khoản giám sát ba bên, không cho một cá nhân rút tùy tiện.</p>
<p>Quân đọc từng điều khoản. Không có cái bẫy nào dễ chịu, cũng không có món quà nào miễn phí. Đây là cơ hội, nhưng cũng là dây thừng buộc vào cổ nếu anh làm sai.</p>
<p>Ông Lộc hỏi nhỏ: "Quân, mình kham nổi không con?"</p>
<p>Quân nhìn những bàn tay chai sần quanh phòng. "Nếu vẫn bán lá tươi cho một nhà máy, chúng ta cả đời bị ép giá. Nếu tự làm vùng nguyên liệu sạch, sáu tháng đầu sẽ rất cực. Nhưng mỗi ký trà sẽ có tên người trồng trên hồ sơ truy xuất."</p>
<p>Anh quay sang An Nhiên. "Tôi chấp nhận tài khoản giám sát. Chấp nhận kiểm toán từng tháng. Nhưng hợp đồng phải ghi rõ giá sàn thu mua cho nông hộ trong ba năm."</p>
<p>An Nhiên nhìn anh, rồi gật đầu. "Hợp lý."</p>
<p>Bảo nghe đến đó thì lao tới giật tập giấy. Bảo vệ giữ hắn lại. Hai đầu gối hắn khuỵu xuống, đập vào chân ghế kêu cộp. Chiếc đồng hồ vàng tuột khỏi cổ tay, rơi xuống thảm.</p>
<p>"Không được ký! Vùng đó là của Mai Trà!"</p>
<p>Quân nhặt chiếc đồng hồ, đặt lại lên bàn trước mặt hắn. "Vùng đó là của người trồng trà. Anh quên quá lâu rồi."</p>
"""
    },
    {
        "title": "Chương 7: Cánh Cửa Kho Mở Lại",
        "content": """
<p>Ba ngày sau, Mai Trà bị thanh tra niêm phong khu kho phụ để phục vụ điều tra. Bảo và Phan Tuấn bị mời làm việc. Bà Nhã không còn xuất hiện trước phóng viên, còn Hương gửi đơn tạm dừng chức vụ trong ban điều hành để hợp tác kiểm toán.</p>
<p>Nhưng chiến thắng trên giấy chưa biến thành cơm áo. Hợp tác xã phải dựng dây chuyền sơ chế tạm, thuê kỹ thuật, mở lại tài khoản, xin mã truy xuất. Việc nào cũng cần tiền, chữ ký và người chịu trách nhiệm.</p>
<p>Quân gần như ngủ trên ghế gấp trong kho cũ. An Nhiên mỗi chiều đều đến kiểm tiến độ, luôn mang theo một danh sách lỗi dài. Độ ẩm phòng chưa đạt. Hồ sơ hộ trồng thiếu căn cước. Bảng kiểm vệ sinh chưa có chữ ký chéo. Cô chỉ ra từng điểm, không nể nang.</p>
<p>Một tối, khi mọi người về hết, Quân ngồi bên cửa kho nhìn mưa rơi trên luống trà thấp. An Nhiên đặt trước mặt anh một ly trà trắng vừa pha. Nước trà màu vàng rất nhạt, gần như trong.</p>
<p>"Anh ghét tôi không?" cô hỏi.</p>
<p>Quân cầm ly, hơi nóng chạm vào vết chai ở ngón tay. "Vì cô bắt lỗi tôi mỗi ngày?"</p>
<p>"Vì tôi không đứng hẳn về phía anh theo cách dễ nghe hơn."</p>
<p>Quân uống một ngụm. Vị trà lên chậm, đầu lưỡi hơi chát rồi ngọt ở cuống họng. "Nếu cô dễ nghe, tôi đã không tin."</p>
<p>An Nhiên nhìn ra đồi. Đèn vàng từ kho hắt lên một nửa gương mặt cô, nửa còn lại nằm trong bóng tối. "Tôi từng ký nhầm một hợp đồng vì tin vào câu chuyện cảm động của một nhà cung cấp. Sau đó, ba mươi công nhân của họ mất việc khi vụ gian lận vỡ ra. Từ đó tôi chỉ tin hồ sơ."</p>
<p>Quân đặt ly xuống. "Hồ sơ cũng do con người viết."</p>
<p>"Nên tôi đang học cách nhìn cả người viết hồ sơ."</p>
<p>Không gian yên tĩnh đến mức nghe rõ tiếng nước nhỏ từ mái tôn xuống thùng nhựa. Đây không phải cảnh tỏ tình ồn ào. Cũng không có lời hứa nào bóng bẩy. Chỉ có hai người mệt mỏi, ngồi giữa mùi trà mới sấy, nhận ra đối phương đã đi cùng mình qua đoạn khó nhất.</p>
<p>An Nhiên lấy từ túi ra một phong bì. "Báo cáo thẩm định sơ bộ. Hợp tác xã đạt sáu mươi tám trên một trăm điểm. Chưa đủ ký hợp đồng chính thức."</p>
<p>Quân bật cười khẽ. "Cô thật biết phá không khí."</p>
<p>"Nhưng nếu hoàn tất ba hạng mục này trong mười ngày, điểm có thể lên tám mươi hai. Lúc đó tôi có cơ sở trình hội đồng."</p>
<p>Quân mở phong bì. Ba hạng mục đều khó, nhưng không bất khả thi: bổ sung máy sấy nhiệt thấp, hợp đồng vận chuyển lạnh, và hồ sơ đất sạch cho từng hộ.</p>
<p>"Tôi làm."</p>
<p>An Nhiên đứng dậy. Trước khi đi, cô dừng lại ở cửa. "Quân, đừng thắng bằng giận dữ. Giận dữ cháy nhanh lắm. Anh cần một thứ bền hơn."</p>
<p>"Ví dụ?"</p>
<p>"Trách nhiệm. Và một người dám sửa lỗi cho anh trước khi người khác tìm ra."</p>
<p>Mười ngày tiếp theo, kho cũ thay da. Máy sấy được đặt ở góc đông, đường điện kéo lại, nền được sơn epoxy chống ẩm. Mỗi bao trà có mã hộ, mã lô, giờ hái, giờ sao, giờ sấy. Những thứ từng nằm trong đầu Quân giờ trở thành quy trình ai cũng đọc được.</p>
<p>Khi đoàn thẩm định của Golden Leaf đến lần hai, ông Lộc mặc áo sơ mi mới, chị Sen tự tin trình bày nhật ký hái lá. Quân đứng lùi về sau, để nông hộ nói về trà của họ.</p>
<p>An Nhiên ghi điểm cuối cùng, rồi khép hồ sơ. "Tám mươi bốn điểm. Đủ điều kiện ký hợp đồng thử nghiệm một năm, giá sàn cao hơn thị trường mười tám phần trăm."</p>
<p>Tiếng thở phào lan khắp kho. Ông Lộc cúi mặt, lấy tay áo lau khóe mắt.</p>
<p>Quân nhìn những kệ trà mới, rồi nhìn An Nhiên. Cô không cười lớn. Chỉ hơi gật đầu, như nói: bây giờ anh mới thật sự bắt đầu.</p>
"""
    },
    {
        "title": "Chương 8: Con Dấu Trên Bàn Gỗ Cũ",
        "content": """
<p>Lễ ký hợp đồng lần này không tổ chức ở khách sạn. Quân chọn kho cũ của hợp tác xã, nơi nền sơn còn mùi mới và ngoài cửa vẫn nhìn thấy đồi trà.</p>
<p>Không có thảm đỏ. Chỉ có bàn gỗ dài của ông Lộc, khăn trắng, ấm trà nóng và bảng truy xuất treo trên tường. Phóng viên đến đông hơn lần trước, nhưng họ phải mang bọc giày nếu muốn bước vào khu sơ chế.</p>
<p>Hương xuất hiện trước giờ ký mười phút. Cô mặc áo sơ mi đơn giản, không trang sức. Quân tưởng cô đến để gây khó, nhưng cô đặt lên bàn một tập hồ sơ.</p>
<p>"Đây là danh sách tài sản kho phụ của Mai Trà có thể chuyển nhượng. Em đã ký đồng ý bán thanh lý qua kiểm toán để trả nợ cho nông hộ bị ép giá. Mẹ em phản đối, nhưng hội đồng cổ đông không còn lựa chọn."</p>
<p>Quân nhìn cô. Những ngày qua chắc cô đã già đi nhiều. Không phải vì nếp nhăn, mà vì trong mắt cô không còn sự chắc chắn dễ dãi của người luôn đứng trên cao.</p>
<p>"Cảm ơn," anh nói.</p>
<p>Hương cười buồn. "Em nợ anh một lời xin lỗi. Nhưng em biết một lời không trả nổi những gì đã xảy ra."</p>
<p>"Vậy đừng trả cho tôi. Trả cho người trồng trà."</p>
<p>Cô gật đầu, lùi sang một bên.</p>
<p>Bảo được đưa đến theo đoàn làm việc của cơ quan điều tra để đối chiếu hồ sơ chuyển nhượng. Hai cổ tay hắn không bị còng trước ống kính, nhưng có cán bộ đi sát bên. Bộ vest đắt tiền nhăn nhúm, cằm lún phún râu. Khi nhìn thấy Quân đứng ở bàn ký, hắn khựng lại.</p>
<p>Quân không sỉ nhục hắn. Anh chỉ đẩy bản biên bản đối chiếu về phía trước. "Anh xác nhận chữ ký và lệnh đổi mã nguồn lá?"</p>
<p>Bảo cầm bút. Đầu bút chạm giấy rồi dừng. Mồ hôi lạnh chảy từ thái dương xuống cổ. Hắn nhìn quanh, tìm một ánh mắt cứu mình. Bà Nhã không đến. Hương nhìn xuống. Phan Tuấn đã khai hết.</p>
<p>Đầu gối Bảo run thấy rõ dưới gầm bàn. Hắn ký tên, nét chữ đứt quãng.</p>
<p>"Quân..." hắn khàn giọng. "Nể tình từng là người nhà, xin anh nói giúp tôi một câu."</p>
<p>Quân nhìn con dấu tròn đỏ vừa đóng xuống biên bản. Tiếng cộp vang lên gọn ghẽ, không cần ai lên giọng.</p>
<p>"Tôi từng cho anh nhiều hơn một câu. Anh dùng nó để đẩy tội cho người khác."</p>
<p>Bảo cúi đầu. Vai hắn sụp xuống, hai bàn tay đặt trên đùi co giật nhẹ. Sự kiêu ngạo từng phủ kín người hắn giờ rơi từng mảng như sơn cũ gặp mưa.</p>
<p>Đến phần ký hợp đồng chính, An Nhiên đứng đối diện Quân. Cô đọc lại điều khoản giá sàn, tài khoản giám sát, chuẩn dư lượng, quyền kiểm toán đột xuất. Mỗi điều khoản là một cái khóa, nhưng cũng là một lan can.</p>
<p>Quân ký trước. Ông Lộc ký đại diện nông hộ. An Nhiên ký cuối cùng cho Golden Leaf. Khi ba con dấu đặt cạnh nhau trên bàn gỗ cũ, cả kho vỡ ra tiếng vỗ tay. Không ồn ào như một lễ hội, mà chắc nịch như tiếng mưa đầu mùa gõ xuống mái tôn.</p>
<p>Sau buổi lễ, Quân ra sau kho. Đồi trà trải dài dưới nắng muộn. An Nhiên đi đến bên cạnh, đưa anh một túi mẫu nhỏ.</p>
<p>"Mẻ trà trắng đầu tiên. Tôi giữ lại từ đêm bị livestream."</p>
<p>Quân nhận lấy. Trên túi có dòng chữ viết tay của cô: Lô số một, đêm không bỏ cuộc.</p>
<p>"Cô lại phá quy trình lưu mẫu à?" anh hỏi.</p>
<p>"Tôi đã lập biên bản giữ mẫu cá nhân," cô đáp, khóe môi hơi cong.</p>
<p>Quân bật cười. Lần này tiếng cười nhẹ hơn, không còn mắc trong ngực.</p>
<p>An Nhiên nhìn anh. "Sau hợp đồng thử nghiệm, Golden Leaf sẽ cần một giám đốc vùng nguyên liệu. Người đó phải khó tính, biết trà, biết hồ sơ, và đủ lì để chịu tôi kiểm toán mỗi tháng."</p>
<p>"Nghe như một công việc vất vả."</p>
<p>"Có thêm một điều kiện ngoài hợp đồng."</p>
<p>Quân quay sang.</p>
<p>Cô nói rất chậm, nhưng không né mắt. "Khi mọi thứ ổn hơn, anh mời tôi uống trà không phải với tư cách kiểm soát rủi ro."</p>
<p>Gió từ đồi thổi qua, mang theo mùi lá non và đất ẩm. Quân nhìn túi trà trong tay, rồi nhìn người phụ nữ đã đứng cạnh mình từ đêm mưa tệ nhất.</p>
<p>"Tôi sẽ mời," anh nói. "Nhưng trà phải đạt chuẩn của cô."</p>
<p>An Nhiên cười. "Vậy anh còn phải cố nhiều."</p>
<p>Phía sau họ, kho trà mở cửa. Những giỏ lá mới được đưa vào, không còn lén lút, không còn sợ hãi. Từng mã lô hiện trên bảng điện tử, sạch sẽ và rõ ràng. Quân biết con đường phía trước không hề ngắn. Nhưng lần đầu tiên sau nhiều năm, anh nhìn thấy vùng đồi này thuộc về đúng những người đã chăm nó bằng đôi tay của mình.</p>
"""
    },
]


def main():
    payload = {
        "title": TITLE,
        "author": "Mộc Trà Sơn",
        "genre": "Sảng Văn",
        "intro": INTRO,
        "cover_prompt": COVER_PROMPT,
        "chapters": CHAPTERS,
    }
    Path("pending_novel.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    Path("scratch/test_story_tra_cau_dat_20260527.md").write_text(
        "# " + TITLE + "\n\n"
        + INTRO.replace("</p>", "</p>\n")
        + "\n\n"
        + "\n\n".join(
            "## " + chapter["title"] + "\n\n" + chapter["content"].strip()
            for chapter in CHAPTERS
        )
        + "\n",
        encoding="utf-8",
    )
    print(f"Wrote pending_novel.json with {len(CHAPTERS)} chapters")
    print("Wrote scratch/test_story_tra_cau_dat_20260527.md")


if __name__ == "__main__":
    main()
