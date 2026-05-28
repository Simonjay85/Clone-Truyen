#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import re
from pathlib import Path

TITLE = "Bị Cả Nhà Vợ Đuổi Khỏi Xưởng Trà, Tôi Dùng Sổ Cân Lá Thâu Tóm Vùng Nguyên Liệu Đà Lạt"

INTRO = (
    '<p><strong>"Quỳ xuống ký biên bản nhận tội đi. Đừng để cả vùng Cầu Đất biết anh là thằng ở rể tráo trà bẩn."</strong></p>'
    '<p>Trong đêm mưa lạnh trước kho Mai Trà, Lê Minh Quân bị nhà vợ cũ xé thẻ nhân viên, ném sổ cân lá vào thùng rác và vu cho anh phá hợp đồng xuất khẩu một trăm hai mươi tỷ.</p>'
    '<p>Nhưng họ không biết người đàn ông bị đuổi khỏi cổng ấy đang giữ bản scan sổ cân lá gốc, ảnh niêm phong mẫu lưu, log kho lên men và một bản sao camera nhiệt chưa từng công bố.</p>'
    '<p>Khi tài khoản hợp tác xã bị khóa, streamer vây kín kho, chuyên gia giả đứng ra phủ nhận mẫu trà, Quân mới từng bước mở chuỗi bằng chứng khiến cả gia tộc từng khinh anh phải cúi đầu trước nông hộ Cầu Đất.</p>'
)

COVER_PROMPT = (
    "Square format, ultra-realistic cinematic real-life photo, high-stakes intense Vietnamese drama movie scene, "
    "inside a stormy tea warehouse in Cau Dat, Da Lat, wet concrete floor, tea crates, sealed sample bags, stamped ledgers, "
    "a calm handsome Vietnamese man in a rain-damp navy work jacket standing beside a sharp Vietnamese female executive in a dark green blazer, "
    "an arrogant wealthy businessman kneeling in panic while clutching a contract and tea residue report, workers and security behind them, "
    "dark uncluttered top area for a short two-line title overlay, dramatic high-contrast lighting, no text, no letters, no watermarks, no logos, no badges, square 1:1."
)

CHAPTERS = [
    {
        "title": "Chương 1: Biên Bản Nhận Tội Dưới Mưa",
        "content": """
<p>Mưa ở Cầu Đất không rơi ào ào. Nó mỏng, lạnh, bám vào cổ áo như một lớp kim nhỏ.</p>
<p>Lê Minh Quân vừa kéo xong cửa kho sấy thì Trần Quốc Bảo bước vào cùng Mai Hương và bà Nhã. Đèn kho hắt lên gương mặt họ, làm những giọt nước trên áo vest của Bảo sáng lên như những mảnh kính vỡ.</p>
<p>Bảo không chào. Hắn ném một tập giấy xuống nền xi măng. Tờ biên bản trượt qua vũng nước trà, dừng ngay dưới mũi giày cũ của Quân.</p>
<p><strong>"Quỳ xuống ký biên bản nhận tội đi. Đừng để cả vùng Cầu Đất biết anh là thằng ở rể tráo trà bẩn."</strong></p>
<p>Cả kho im bặt. Mấy công nhân vừa bốc bao lá tươi đứng sững lại, tay còn giữ dây thừng. Ông Lộc, người chở lá từ đồi số ba xuống, ôm chiếc nón vải trước bụng. Mắt ông lảng đi, không phải vì tin Bảo, mà vì sợ nhà máy ngừng cân lá ngày mai.</p>
<p>Quân cúi nhìn biên bản. Lô trà hữu cơ số bảy bị kết luận có dư lượng thuốc cỏ vượt ngưỡng. Chữ ký xuất kho là chữ ký của anh. Dòng mã mẫu ghi CD-7B-0426, nhưng anh biết ngay có thứ không đúng. Mã ấy không thuộc đồi hữu cơ. Nó thuộc kho phụ cuối thung lũng Đạ Nghịt, nơi Bảo mới thuê thêm đất để ép sản lượng.</p>
<p>"Cho tôi xem sổ cân lá gốc và mẫu lưu trong tủ niêm phong," Quân nói.</p>
<p>Mai Hương rút thẻ nhân viên khỏi cổ anh. Sợi dây đứt phựt, cạnh nhựa cứa qua da cổ để lại một vệt đỏ. Cô từng là vợ anh ba năm, từng ngồi sau xe máy cùng anh đi qua những đồi trà sương phủ. Giờ giọng cô lạnh đến mức không còn chút người quen.</p>
<p>"Anh vẫn tưởng mình là kỹ sư trưởng à? Anh bị đình chỉ từ phút này."</p>
<p>Bà Nhã bước tới. Mùi nước hoa đắt tiền lẫn với mùi lá ẩm làm người ta khó thở. Bà cúi nhặt cuốn sổ bìa xanh trên bàn kiểm hàng, lật vài trang rồi ném thẳng vào thùng rác inox.</p>
<p>"Sổ giấy của đám bốc vác có giá trị gì? Nhà tôi làm xuất khẩu, không phải bán trà chợ huyện. Thứ ở rể như anh chỉ đáng bốc bao trà mốc ngoài sân."</p>
<p>Tiếng cuốn sổ rơi vào đáy thùng nghe khô khốc. Quân nhìn mép bìa xanh thò ra giữa nước trà thừa. Trong đó có cân của từng hộ, giờ xe vào cổng, độ ẩm, mã lô, chữ ký người nhận. Nó không chỉ là sổ. Nó là đường sống của mấy chục gia đình trồng trà.</p>
<p>Bảo đặt bút lên biên bản, đẩy về phía anh. "Ký đi. Tôi cho anh một tháng lương và giấy nghỉ việc tự nguyện. Nếu cứng đầu, sáng mai đơn tố cáo phá hoại kinh doanh sẽ nằm ở Công an thành phố Đà Lạt."</p>
<p>Quân không cầm bút. "Anh muốn tôi nhận tội thay cho lô kho phụ của anh?"</p>
<p>Đuôi mắt Bảo giật nhẹ. Chỉ một nhịp rất nhỏ, nhưng Quân thấy.</p>
<p>Bảo đứng dậy, giọng cao hơn. "Nghe chưa? Đến giờ vẫn còn vu khống. Lôi nó ra ngoài."</p>
<p>Hai bảo vệ kẹp tay Quân. Họ từng uống trà với anh trong những ca đêm, giờ không dám nhìn anh. Đầu gối anh đập vào bậc cửa khi bị đẩy ra sân. Cơn đau chạy dọc ống chân, nóng rát dưới lớp mưa lạnh.</p>
<p>Từ trong kho, Bảo nói vọng ra với Hương: "Sáng mai ký phụ lục vùng nguyên liệu với Golden Leaf. Đừng để thằng này làm bẩn lễ ký."</p>
<p>Quân chống tay đứng dậy. Mưa làm máu ở đầu gối loãng ra, chảy xuống cổ giày. Anh không quay lại chửi. Anh chỉ sờ vào túi trong áo khoác, nơi chiếc USB được bọc trong túi chống ẩm.</p>
<p>Bên trong là bản scan sổ cân lá trước ngày bị sửa, ảnh dây niêm phong cũ của mẫu CD-7B-0426, và một thư mục log kho lên men anh sao lưu theo thói quen mỗi cuối ca. Thói quen ấy từng bị Hương chê là cứng nhắc. Đêm nay nó là thứ duy nhất chưa bị ném vào thùng rác.</p>
<p>Ở đầu đường, một chiếc xe đen dừng lại. Cửa kính hạ xuống. Người phụ nữ mặc blazer xanh sẫm nhìn anh, ánh mắt đi qua vết máu ở đầu gối rồi dừng ở cánh cổng nhà máy đang đóng sầm.</p>
<p>"Anh là Lê Minh Quân?"</p>
<p>"Cô là ai?"</p>
<p>"Nguyễn An Nhiên, giám đốc kiểm soát rủi ro của Golden Leaf Việt Nam. Tôi đến xem ai đang phá hợp đồng một trăm hai mươi tỷ của chúng tôi."</p>
<p>Quân nhìn cánh cổng. Sau lớp tôn, tiếng cười của Bảo vẫn vọng ra từng nhịp.</p>
<p>"Nếu cô muốn xem sự thật," anh nói, "đừng vào bằng cổng chính."</p>
"""
    },
    {
        "title": "Chương 2: Cô Không Tin Người Vừa Bị Đuổi",
        "content": """
<p>An Nhiên không mời Quân lên xe ngay. Cô mở ô, đứng cách anh một khoảng đủ lịch sự nhưng không hề mềm lòng. Dưới ánh đèn vàng bên cổng phụ, cô nhìn anh như nhìn một hợp đồng đầy vết tẩy xóa.</p>
<p>"Tôi không ký hay hủy hợp đồng dựa trên lời kể của người vừa bị đuổi," cô nói. "Anh có bằng chứng, hay chỉ có uất ức?"</p>
<p>Câu hỏi thẳng đến mức tài xế đứng sau cũng hơi khựng. Quân lại thấy dễ chịu. Ít nhất cô không thương hại anh, cũng không giả vờ tin chỉ vì anh đang ướt mưa.</p>
<p>Anh mở điện thoại cũ, đưa cô xem ảnh túi mẫu lưu CD-7B-0426. Trong ảnh, dây niêm phong màu đỏ có vết xước hình chữ V trên kẹp nhựa. Phía sau là góc tủ lạnh mẫu, nơi chỉ nhân viên kỹ thuật và kế toán kho có chìa.</p>
<p>"Ảnh có thể dựng," An Nhiên nói sau khi phóng to.</p>
<p>"Nên tôi cần xem tủ mẫu lưu trước khi họ thay tem."</p>
<p>"Nếu họ không cho vào?"</p>
<p>"Hợp đồng Golden Leaf có điều khoản kiểm toán độc lập trước giải ngân đợt một. Cô có quyền yêu cầu quan sát mẫu."</p>
<p>Lần đầu tiên, mắt cô dừng lại lâu hơn trên mặt anh. "Anh đọc hợp đồng bên tôi?"</p>
<p>"Tôi soạn phần truy xuất vùng nguyên liệu cho Mai Trà. Bảo sửa tên người phụ trách thành của hắn trước ngày ký."</p>
<p>An Nhiên lấy máy tính bảng, gọi cho pháp chế. Cô không nói Quân là người tố giác. Cô yêu cầu lập biên bản quan sát độc lập vì có dấu hiệu sai lệch mã mẫu. Cách cô dùng chữ rất lạnh, rất gọn, không để đối phương có chỗ bắt bẻ.</p>
<p>Mười lăm phút sau, họ vào bằng cổng phụ xe chở bã trà. Khu kho lạnh sáng đèn. Bảo đang đứng ở hành lang cùng Phan Tuấn, trợ lý vận hành, trên tay Tuấn là thùng tem niêm phong mới.</p>
<p>Thấy An Nhiên, Bảo cười ngay. Thấy Quân đứng sau cô, nụ cười ấy cứng lại.</p>
<p>"Giám đốc Nhiên, mai mới là lễ ký. Sao chị đến giờ này?"</p>
<p>"Kiểm rủi ro trước khi ký." Cô đưa văn bản điện tử cho hắn xem. "Mở khu mẫu lưu."</p>
<p>Bảo liếc Quân. "Người này đã bị chúng tôi đình chỉ vì phá hoại. Cho anh ta vào là vi phạm quy định nội bộ."</p>
<p>An Nhiên đáp ngay: "Quy định nội bộ không lớn hơn điều khoản kiểm toán trong hợp đồng khung."</p>
<p>Quản lý kho đứng giữa hai bên, mặt trắng bệch. Cuối cùng chị Hạnh, kế toán kho, run tay mở tủ mẫu lưu. Quân không chạm vào bất cứ túi nào. Anh chỉ quay video toàn cảnh, rồi dừng ở túi CD-7B-0426.</p>
<p>Vết xước hình chữ V không còn.</p>
<p>Anh cúi sát hơn. Tem mới có mã cuộn phát hành tháng năm. Lô mẫu bị lấy từ tháng tư. Không thể có chuyện mẫu tháng tư dùng tem tháng năm nếu tủ chưa từng bị mở.</p>
<p>"Chị Hạnh," Quân nói, mắt vẫn nhìn tem, "sổ xuất tem nằm ở ngăn thứ ba bàn chị. Nếu tối nay chị không mở, sáng mai người chịu trách nhiệm thay họ sẽ là chị."</p>
<p>Hạnh nhìn Bảo. Bảo nghiến răng. Các cơ hàm nổi lên dưới da. "Đừng nghe thằng bị sa thải dọa."</p>
<p>An Nhiên đặt máy quay xuống bàn. "Mở sổ. Golden Leaf sẽ ghi nhận người hợp tác trong biên bản."</p>
<p>Hạnh bật khóc rất khẽ. Cô mở ngăn bàn, lấy cuốn sổ nhỏ. Dòng tem CD-7B-0426 được ghi xuất lúc 21 giờ 47 phút tối nay. Người nhận: Phan Tuấn. Mục đích: thay niêm phong mẫu lỗi.</p>
<p>Phan Tuấn lùi nửa bước. Mồ hôi rịn trên môi dù kho lạnh chỉ mười sáu độ.</p>
<p>Bảo giật cuốn sổ, nhưng Quân đã chụp lại. Hắn nắm mép giấy mạnh đến mức trang sổ nhăn rúm.</p>
<p>"Một cái tem chưa chứng minh được gì."</p>
<p>Quân nhìn hắn. "Đúng. Nó chỉ chứng minh anh đã mở tủ sau khi tôi bị đuổi."</p>
<p>An Nhiên khép máy tính bảng. "Lễ ký ngày mai vẫn diễn ra. Nhưng trước khi đặt bút, chúng tôi cần xem toàn bộ sổ cân lá bản gốc."</p>
<p>Bảo bật cười. "Bản gốc đã số hóa. Sổ giấy không còn giá trị."</p>
<p>Quân nhìn về phía thùng rác inox cuối kho. Cuốn sổ bìa xanh vẫn nằm đó, ướt nửa mép.</p>
<p>An Nhiên cũng nhìn theo. Cô không nhặt. Cô chỉ nói với giọng rất thấp: "Anh Quân, ngày mai nếu anh không chứng minh được chuỗi cân lá trước mặt ba bên, tôi sẽ dừng ở đây."</p>
<p>Quân gật đầu. Đêm ấy anh chưa thắng. Anh chỉ giành được quyền bị nghi ngờ thêm một ngày.</p>
"""
    },
    {
        "title": "Chương 3: Sổ Cân Lá Và Cái Bẫy Đầu Tiên",
        "content": """
<p>Sáng hôm sau, hội trường Mai Trà phủ đầy hoa cẩm tú cầu trắng. Bảng điện tử phía sau sân khấu ghi hợp tác xuất khẩu sang Nhật Bản, trị giá một trăm hai mươi tỷ đồng. Bên ngoài, mưa đã tạnh nhưng sương vẫn vắt ngang những luống trà như tấm khăn lạnh.</p>
<p>Bà Nhã mặc áo dài nhung, cười với phóng viên. Hương đứng cạnh Bảo, tay đặt lên tập hợp đồng. Cô không nhìn Quân khi anh bước vào cùng An Nhiên, nhưng các ngón tay đã siết vào nhau.</p>
<p>Bảo đứng bật dậy. "Tôi yêu cầu an ninh đưa người này ra ngoài."</p>
<p>An Nhiên đặt biên bản quan sát mẫu lên bàn. "Golden Leaf yêu cầu kiểm tra sổ cân lá ba tháng gần nhất trước khi ký."</p>
<p>Không khí trong phòng khựng lại. Bà Nhã vẫn cười, nhưng nếp nhăn quanh miệng cứng như bị kéo bằng dây.</p>
<p>"Giám đốc Nhiên, chúng ta đã thống nhất rồi. Sai lệch nhỏ trong kho không nên làm chậm hợp đồng."</p>
<p>"Sai lệch nhỏ không cần thay tem lúc nửa đêm."</p>
<p>Một phóng viên hạ máy ảnh xuống. Quân bước tới thùng rác kỹ thuật, cúi người lấy cuốn sổ bìa xanh. Mép sổ còn mùi nước trà chua. Có người bật cười khinh khỉnh khi thấy anh phủi bụi trên thứ vừa bị ném bỏ.</p>
<p>Quân mở trang ngày mười tám tháng tư. "Hộ ông Lộc giao tám trăm bốn mươi ký lá từ đồi số ba, độ ẩm bảy mươi hai phần trăm. Xe vào cổng lúc 14 giờ 12 phút, biển số 49C-218.36. Người cân: tôi. Người giám sát: Phan Tuấn."</p>
<p>Anh đặt cạnh đó bản số hóa Bảo gửi cho Golden Leaf. Cùng ngày, cùng giờ, số cân bị đổi thành một tấn hai. Nguồn lá bị đổi từ đồi số ba sang đồi hữu cơ số bảy.</p>
<p>Ông Lộc đứng lên, giọng run nhưng rõ. "Đồi số bảy không phải của nhà tôi. Tôi không bao giờ hái ở đó."</p>
<p>Bảo quay phắt lại. "Ông Lộc, ông nghĩ kỹ. Hợp đồng thu mua vụ tới của nhà ông còn nằm trong tay Mai Trà."</p>
<p>Lời đe dọa rơi ra quá nhanh. Phóng viên quay máy về phía ông Lộc. Người nông dân già ôm chiếc nón vải đến mức vành nón gãy gập.</p>
<p>Quân tiếp tục mở thêm ba trang. Sáu hộ bị nâng sản lượng trên giấy. Tất cả số lá dư đều được ghép về đồi hữu cơ số bảy, trong khi ảnh cổng kho phụ cho thấy xe bồn nhỏ của Phan Tuấn ra vào cùng khung giờ.</p>
<p>Hương quay sang Bảo. "Anh nói kho phụ chỉ chứa bao bì."</p>
<p>Bảo không nhìn cô. "Anh làm để cứu hợp đồng. Mùa này lá thiếu. Nếu không ghép nguồn, cả xưởng chết."</p>
<p>"Cứu hợp đồng bằng cách đổ tội cho tôi?" Quân hỏi.</p>
<p>Bảo nở một nụ cười méo. "Anh nói nghe hay lắm. Nhưng sổ giấy của anh có thể làm giả. Còn đây là chứng nhận kiểm nghiệm từ phòng lab đối tác."</p>
<p>Hắn đặt lên bàn một phong bì mới. Bên trong là kết quả kiểm nghiệm khác, kết luận mẫu CD-7B-0426 đạt chuẩn hữu cơ. Con dấu đỏ rất rõ, chữ ký đầy đủ.</p>
<p>Đám phóng viên lập tức xôn xao. Ông Lộc ngồi xuống. Hương thở ra rất khẽ, như vừa níu được một cọng dây.</p>
<p>An Nhiên cầm bản kiểm nghiệm, đọc từng dòng. "Phòng lab này không nằm trong danh sách độc lập của Golden Leaf."</p>
<p>Bảo nhún vai. "Nhưng nó được Sở Công Thương công nhận. Chúng ta đang ở Việt Nam, không phải ở văn phòng của chị."</p>
<p>Đây là cái bẫy đầu tiên. Bảo không phủ nhận sổ cân lá. Hắn làm bẩn chính giá trị chứng cứ bằng cách tung ra một giấy kiểm nghiệm có vẻ hợp pháp. Nếu Quân phản ứng nóng vội, anh sẽ biến thành kẻ cố chấp trước mặt nông hộ.</p>
<p>An Nhiên quay sang Quân. Ánh mắt cô không còn mềm hơn đêm qua. "Anh có chấp nhận gửi mẫu đối chứng đến đơn vị thứ ba ngay hôm nay không?"</p>
<p>"Có."</p>
<p>"Và trong thời gian chờ kết quả, Golden Leaf tạm dừng giải ngân."</p>
<p>Những nông hộ phía sau lập tức hoang mang. Chị Sen đứng bật dậy. "Tạm dừng là bao lâu? Lá ngoài đồi đang tới lứa. Không cân thì nhà tôi lấy gì trả nợ phân?"</p>
<p>Bảo mỉm cười. Hắn không cần thắng sạch. Hắn chỉ cần làm nông hộ sợ Quân.</p>
<p>Quân nhìn những gương mặt đang chuyển từ hy vọng sang nghi ngờ. Đòn của Bảo trúng hơn một cái tát. Nó đánh vào bữa cơm của họ.</p>
<p>"Tôi chịu trách nhiệm đưa mẫu đi trong hôm nay," Quân nói. "Nếu tôi sai, tôi rời khỏi Cầu Đất và bồi thường chi phí kiểm nghiệm."</p>
<p>Bảo vỗ tay một tiếng. "Nghe chưa? Một thằng không còn việc làm đòi bồi thường cho cả vùng trà."</p>
<p>Tiếng cười rải rác trong hội trường. Quân đứng yên. Anh biết mình vừa thoát khỏi một hố, nhưng phía trước là một hố sâu hơn.</p>
"""
    },
    {
        "title": "Chương 4: Tài Khoản Bị Khóa Và Đêm Streamer Vây Kho",
        "content": """
<p>Chiều hôm ấy, tài khoản của Hợp tác xã Trà Sạch Lang Biang ở ngân hàng thương mại cổ phần ngoại thương Việt Nam bị tạm khóa theo yêu cầu rà soát giao dịch bất thường. Tin nhắn báo khóa đến điện thoại ông Lộc lúc ông đang đứng cạnh đống lá vừa hái.</p>
<p>"Quân," ông gọi, giọng khàn đi, "họ khóa tiền rồi."</p>
<p>Không chỉ tiền. Xe tải của Mai Trà cũng ngừng lên đồi cân lá. Ba thương lái quen nhận được điện thoại cảnh cáo không được mua lá của những hộ đã ký thỏa thuận với Quân. Đến tối, trên nhóm địa phương xuất hiện bài viết nói Quân lập hợp tác xã ma để lừa nông dân ký giấy bán đất.</p>
<p>Kho cũ của hợp tác xã sáng đèn. Lá tươi chất thành từng giỏ, xanh non và ướt sương. Nếu qua đêm không sơ chế, búp sẽ đen mép, hương sẽ gắt. Mỗi giờ trôi qua là tiền của nông hộ tan thành hơi ẩm.</p>
<p>Chị Sen ngồi cạnh bao lá, hai mắt đỏ hoe. "Nếu mai không cân được, nhà chị mất trắng hai sào đầu mùa. Con chị còn đang đóng học phí."</p>
<p>Quân cầm sổ tính công suất. Họ chỉ có một lò sao nhỏ của ông Lộc, một máy sấy cũ, vài nong tre. Không đủ cho cả vùng. Anh từng xử lý dây chuyền của Mai Trà, nhưng đó là nhà máy có tiền, có điện ba pha, có kho lạnh. Ở đây, mọi thứ đều thô và thiếu.</p>
<p>An Nhiên gọi điện cho pháp chế Golden Leaf, ngân hàng, rồi đơn vị kiểm nghiệm. Khi khép máy, cô nói thẳng: "Tài khoản khóa ít nhất hai mươi bốn giờ. Bên kia gửi đơn tố cáo dòng tiền không minh bạch. Golden Leaf không được ứng trước cho đến khi có kết luận."</p>
<p>Một thanh niên đập tay vào thùng thiếc. "Thế là chết. Tin anh Quân xong giờ lá không bán được, tiền cũng không có."</p>
<p>Quân nghe câu ấy như nghe một lưỡi dao rút chậm khỏi ngực. Anh không trách cậu. Nông dân không sống bằng niềm tin, họ sống bằng cân lá hôm nay.</p>
<p>"Không bán lá tươi nữa," Quân nói.</p>
<p>Mọi người im phăng phắc.</p>
<p>Anh kéo bảng trắng ra. "Làm mẻ trà trắng thủ công. Chỉ lấy búp một tôm hai lá, hong bằng quạt chậm, sấy nhiệt thấp. Tôi viết giấy nhận nợ cá nhân cho từng hộ, có An Nhiên làm chứng. Khi tài khoản mở lại hoặc mẫu đạt, trả đủ giá sàn."</p>
<p>An Nhiên nhìn anh. "Anh đang đặt trách nhiệm lên tên mình."</p>
<p>"Đúng."</p>
<p>"Tôi không bảo lãnh tiền."</p>
<p>"Tôi không yêu cầu cô bảo lãnh. Tôi cần cô làm chứng quy trình lấy mẫu."</p>
<p>Cô im vài giây rồi tháo đồng hồ, xắn tay áo blazer. "Nếu sai một bước vệ sinh, tôi dừng ngay."</p>
<p>Họ làm việc trong mùi lá tươi và hơi nước. Ông Lộc nhóm lò bằng than sạch. Chị Sen phân loại búp. Quân chỉ từng người đảo lá bằng cổ tay, không bóp mạnh, không làm dập mép. An Nhiên dán mã mẫu lên từng khay, chữ viết nhỏ, sắc và lạnh như chính con người cô.</p>
<p>Khoảng ba giờ sáng, bốn chiếc xe máy dừng trước cổng. Một nhóm streamer kéo đến, bật đèn quay trắng lóa. Họ la lên rằng hợp tác xã đang tiêu hủy chứng cứ. Ánh đèn quét qua mặt chị Sen khiến chị lùi lại, tay run làm rơi cả khay lá.</p>
<p>Bảo xuất hiện sau họ, áo khoác đen không dính một giọt mưa. Hắn cười. "Quân, vẫn thích kéo người nghèo chết cùng mình à?"</p>
<p>Một streamer dí điện thoại sát mặt Quân. "Anh có dám công khai sao kê tài khoản không? Hay tiền nông dân đã vào túi anh?"</p>
<p>"Tài khoản đang bị khóa theo đơn tố cáo của Trần Quốc Bảo," Quân nói. "Khi mở lại, tôi công khai. Còn tối nay, mời quay đủ quy trình chúng tôi làm trà. Quay mã mẫu, cân điện tử, giờ sấy, camera thời gian thực."</p>
<p>Nhóm streamer khựng lại. Họ đến để bắt cảnh hỗn loạn, không ngờ Quân mở cửa.</p>
<p>An Nhiên đưa găng tay cho người cầm máy. "Muốn quay gần thì mặc đồ bảo hộ. Làm bẩn mẫu, chúng tôi lập biên bản bồi thường."</p>
<p>Giọng cô không lớn, nhưng cô gái kia lùi nửa bước.</p>
<p>Đến rạng sáng, mẻ trà đầu tiên khô vừa tới. Hương thanh, nhẹ, có mùi mật hoa lẫn cỏ non sau mưa. Ông Lộc bốc một nhúm đưa lên mũi, bàn tay chai sần run run.</p>
<p>"Lâu rồi tôi mới ngửi thấy mùi trà của đồi mình."</p>
<p>Quân không cười. Ngoài cổng, Bảo đứng trong sương, mặt xám lại. Hắn tưởng khóa tài khoản sẽ làm họ tan rã. Nhưng chính đêm bị vây ấy lại biến kho cũ thành sân khấu công khai nhất.</p>
<p>Rồi điện thoại An Nhiên rung. Cô nhìn màn hình, sắc mặt lạnh đi. "Phòng kiểm nghiệm độc lập vừa báo có người gửi đơn nghi mẫu của chúng ta bị nhiễm chéo. Họ tạm hoãn trả kết quả."</p>
<p>Tiếng thở trong kho chùng xuống. Bảo không cần bước vào nữa. Đòn thứ hai của hắn đã tới.</p>
"""
    },
    {
        "title": "Chương 5: Mẫu Trà Trong Thùng Đá Bị Phủ Nhận",
        "content": """
<p>Bảy giờ sáng, An Nhiên đặt ba túi mẫu vào thùng đá có khóa niêm phong. Mỗi túi có mã lô, mã hộ, giờ hái, giờ hong, chữ ký của Quân, ông Lộc, chị Sen và đại diện Golden Leaf. Cô dán băng niêm phong trước camera còn đang livestream, rồi bắt hai streamer ký xác nhận đã quay đủ quy trình.</p>
<p>Thùng mẫu được chở xuống thành phố Hồ Chí Minh bằng xe lạnh thuê riêng. Quân ngồi phía sau, mắt không rời cảm biến nhiệt độ gắn trong thùng. Cứ mười phút anh lại ghi một dòng vào sổ. An Nhiên ngồi ghế trước, gửi vị trí và ảnh niêm phong cho pháp chế.</p>
<p>Kết quả nhanh cần sáu tiếng. Sáu tiếng ấy dài như một mùa mưa.</p>
<p>Nhưng Bảo không để họ chờ yên. Trưa cùng ngày, hắn tổ chức họp báo nhỏ ngay trước cổng Mai Trà. Một người đàn ông tự xưng là chuyên gia kiểm nghiệm nông sản, mặc áo blouse trắng, nói trước ống kính rằng quy trình làm trà trong kho cũ không đủ điều kiện vô trùng, mẫu có nguy cơ nhiễm chéo, mọi kết quả sau đó đều không đáng tin.</p>
<p>Đoạn clip lan rất nhanh. Bình luận chửi Quân lừa nông dân, chửi An Nhiên tiếp tay cho trò truyền thông. Một số nông hộ bắt đầu gọi cho ông Lộc đòi rút khỏi thỏa thuận. Họ sợ. Sợ lá hỏng, sợ bị ngân hàng thúc nợ, sợ con cái bị người ta chỉ mặt ở chợ.</p>
<p>Trong phòng chờ kiểm nghiệm, Quân xem clip ba lần. Người đàn ông áo blouse nói trôi chảy, nhưng khi nhắc đến chỉ tiêu dư lượng glufosinate, ông ta phát âm sai tên hoạt chất. Một chuyên gia thật không sai ở chỗ đó.</p>
<p>"Ông ta là ai?" Quân hỏi.</p>
<p>An Nhiên đã tra hồ sơ. "Từng làm tư vấn cho một công ty vật tư nông nghiệp bị phạt vì bán thuốc cỏ ngoài danh mục. Không thuộc phòng kiểm nghiệm nào cả."</p>
<p>"Bảo thuê ông ta để đánh vào niềm tin trước khi kết quả ra."</p>
<p>"Và nó hiệu quả." Cô đưa điện thoại cho anh. "Hội đồng Golden Leaf yêu cầu tôi tạm dừng mọi đề xuất hợp tác với hợp tác xã đến khi có xác nhận độc lập thứ hai."</p>
<p>Câu đó nặng hơn mọi lời mắng. Quân nhìn cô. "Cô cũng tạm dừng?"</p>
<p>An Nhiên không né mắt. "Tôi phải tạm dừng. Nếu tôi bỏ qua quy trình vì tin anh, tôi không còn tư cách kiểm soát rủi ro."</p>
<p>Im lặng kéo dài giữa họ. Quân hiểu cô đúng, nhưng hiểu không làm ngực bớt nghẹn. Đêm qua họ cùng đứng trong kho, cùng giữ mẻ trà khỏi hỏng. Sáng nay, cô lại trở về phía giấy tờ.</p>
<p>"Vậy tôi cần gì để cô mở lại?"</p>
<p>"Một mẫu đối chứng từ kho phụ của Mai Trà, được lấy dưới sự chứng kiến của bên thứ ba. Và một chứng cứ cho thấy chuyên gia kia nhận tiền từ Bảo."</p>
<p>Quân nhìn thùng đá. Mẫu của anh sạch cũng chưa đủ. Anh phải chứng minh mẫu bẩn đến từ kho phụ, và chứng minh người đang phủ nhận anh là người được thuê.</p>
<p>Chiều, kết quả đầu tiên ra. Mẫu hợp tác xã: dư lượng thuốc cỏ dưới ngưỡng phát hiện. Mẫu đối chiếu cũ của Quân: vượt ngưỡng bảy lần. Nhưng báo cáo ghi chú cần mẫu kho phụ được lấy trực tiếp để kết luận nguồn.</p>
<p>Bảo lập tức đăng clip cười trước cổng Mai Trà. "Một mẫu tự giữ trong túi ai biết từ đâu ra. Mai Trà sẵn sàng cho kiểm tra nếu cơ quan chức năng yêu cầu, chứ không chạy theo trò vu khống của người cũ."</p>
<p>Hương gọi cho Quân. Đây là cuộc gọi đầu tiên sau ngày anh bị đuổi.</p>
<p>"Anh còn bao nhiêu bằng chứng nữa?" cô hỏi.</p>
<p>"Đủ để biết anh ta đang nói dối."</p>
<p>"Nhưng chưa đủ để em tin trước hội đồng."</p>
<p>Quân nhắm mắt. Câu ấy đau vì nó thật.</p>
<p>"Vậy em làm một việc," anh nói. "Đừng tin anh. Hãy kiểm kho phụ. Nếu em còn là người của Mai Trà, em có quyền yêu cầu mở kho."</p>
<p>Đầu dây bên kia lặng đi. Rồi Hương nói rất nhỏ: "Mẹ em sẽ không cho."</p>
<p>"Vậy em chọn tiếp tục đứng sau mẹ em, hay đứng trước đống giấy tờ mà em sắp phải ký?"</p>
<p>Cuộc gọi tắt. Quân biết mình vừa đẩy Hương vào thế khó. Nhưng để lôi Bảo ra ánh sáng, anh cần một người bên trong mở cánh cửa kho phụ. Không phải vì tình cũ. Vì chỉ có cô còn giữ quyền ký kiểm tra nội bộ.</p>
"""
    },
    {
        "title": "Chương 6: Hương Mở Kho Phụ",
        "content": """
<p>Mai Hương xuất hiện ở kho phụ Đạ Nghịt lúc gần chín giờ tối. Cô đi một mình, không tài xế, không thư ký. Chiếc áo sơ mi trắng bị sương làm ẩm ở vai. Trong tay cô là quyết định kiểm kê nội bộ có chữ ký điện tử của chính cô với tư cách phó tổng giám đốc.</p>
<p>Bảo đến sau năm phút, phanh xe gấp đến mức sỏi bắn vào chân cổng. "Em đang làm gì vậy?"</p>
<p>Hương giữ quyết định trước ngực. "Kiểm kho."</p>
<p>"Em điên à? Trước mặt Golden Leaf và thằng Quân?"</p>
<p>"Nếu kho sạch, anh sợ gì?"</p>
<p>Câu hỏi ấy làm mặt Bảo co lại. Bà Nhã gọi đến liên tục, nhưng Hương tắt máy. Đêm đó, trước cổng kho phụ có Quân, An Nhiên, đại diện ủy ban xã, một cán bộ thanh tra nông nghiệp địa phương và hai nông hộ làm chứng. Mọi thứ được quay bằng ba máy khác nhau.</p>
<p>Khi cửa kho mở, mùi hóa chất cũ trộn với mùi lá ẩm xộc ra. Trên kệ góc trái là những bao lá không có mã hộ. Dưới bạt xanh có bảy can nhựa trắng, nhãn đã bị xé, nhưng đáy can vẫn còn mã lô của một loại thuốc cỏ bị cấm dùng trong vùng hữu cơ.</p>
<p>Bảo lao tới kéo bạt lại. "Đây là kho bao bì cũ. Ai cũng có thể đặt đồ vào."</p>
<p>Quân không tranh cãi. Anh chỉ chỉ vào nền xi măng. Có vệt bánh xe bồn in trên lớp bụi ẩm, cùng loại vệt từng xuất hiện trong ảnh cổng kho ngày mười tám tháng tư. Anh lấy thước đo khoảng cách hai bánh, rồi đặt cạnh ảnh in sẵn.</p>
<p>An Nhiên ghi biên bản. "Mẫu lấy tại chỗ, niêm phong ba bên."</p>
<p>Hương nhìn từng túi lá không mã. Mặt cô trắng dần. Khi cán bộ thanh tra nhấc một can nhựa lên, vài giọt nước đọng ở miệng can rơi xuống nền. Cô lùi lại một bước như vừa thấy thứ gì bẩn bám vào tay mình.</p>
<p>"Anh nói với em ở đây chỉ chứa bao bì," cô nói với Bảo.</p>
<p>Bảo kéo cô sang một bên. "Anh làm vì công ty. Nếu hợp đồng chết, mẹ em mất hết. Em tưởng thằng Quân cứu được nhà em à? Nó chỉ muốn trả thù."</p>
<p>Hương nhìn Quân. Anh đang ký vào biên bản lấy mẫu, đầu gối vẫn còn băng trắng. Anh không nhìn cô, cũng không chờ cô bênh. Sự im lặng ấy làm cô khó thở hơn mọi lời trách.</p>
<p>Đúng lúc đó, Phan Tuấn bị bảo vệ cũ của kho đưa vào. Anh ta run đến mức phải vịn cửa. Trên điện thoại của Tuấn có tin nhắn Bảo gửi: "Đổi tem xong thì hủy sổ xuất. Chuyên gia Hòa nhận đủ tiền rồi, cứ để ông ta nói nhiễm chéo."</p>
<p>Bảo giật điện thoại. Nhưng An Nhiên đã chụp lại màn hình, kèm thời gian và số máy. Cô gửi ngay cho pháp chế.</p>
<p>"Tin nhắn có thể giả," Bảo gầm lên.</p>
<p>Quân mở ổ cứng cũ. "Nên tôi có log kho lên men."</p>
<p>Trên màn hình laptop, từng dòng đăng nhập hiện ra: tài khoản vận hành của Bảo vào hệ thống lúc 23 giờ 12 phút ngày mười tám tháng tư, đổi mã nguồn lá từ kho phụ sang đồi hữu cơ số bảy, xóa cảnh báo dư lượng, rồi in phiếu xuất lô.</p>
<p>An Nhiên vẫn không vội kết luận. "Tài khoản có thể bị dùng chung."</p>
<p>Quân mở tiếp video camera nhiệt. Bảo bước vào phòng server, tay cầm điện thoại. Sau lưng hắn là Phan Tuấn ôm thùng tem niêm phong. Hình không rõ mặt hoàn toàn, nhưng dáng đi lệch vai và chiếc đồng hồ vàng trên cổ tay không lẫn được.</p>
<p>Hương đưa tay che miệng. Vai cô rung lên, nhưng không khóc thành tiếng.</p>
<p>Bảo nhìn cô, rồi nhìn những chiếc máy quay. Sắc mặt hắn chuyển từ đỏ sang xám. Mồ hôi rịn ở chân tóc, chảy xuống thái dương. Hắn mở miệng như muốn nói, nhưng môi run đến mức chữ mắc lại.</p>
<p>An Nhiên khép máy tính. "Chúng ta có mẫu kho phụ, log hệ thống, tin nhắn chuyển tiền cho chuyên gia và video phòng server. Nhưng để kết thúc, ngày mai cần hội đồng ba bên."</p>
<p>Quân gật đầu. Anh không thấy nhẹ nhõm. Anh chỉ thấy đoạn đường phía trước cuối cùng đã hiện hình.</p>
"""
    },
    {
        "title": "Chương 7: Hội Đồng Đà Lạt Palace",
        "content": """
<p>Cuộc họp khẩn diễn ra tại khách sạn Đà Lạt Palace. Ngoài Golden Leaf và Mai Trà, còn có đại diện Sở Nông nghiệp, ngân hàng, đơn vị kiểm toán, thanh tra địa phương và ba mươi nông hộ lớn. Căn phòng ấm, thảm dày, hoa tươi đặt giữa bàn, nhưng ai bước vào cũng thấy lạnh ở gáy.</p>
<p>Bảo đến muộn mười phút. Hắn thay vest đen, tóc chải kỹ, nhưng hai mắt đỏ vì mất ngủ. Bà Nhã đi cạnh hắn, khăn lụa buộc chặt đến mức cổ bà hằn vệt. Hương ngồi phía đối diện, không còn ngồi cạnh mẹ.</p>
<p>An Nhiên trình bày trước. Cô không thêm một tính từ nào: mã mẫu, giờ lấy, nhiệt độ bảo quản, kết quả dư lượng, mã can thuốc cỏ, ảnh vệt bánh xe, log hệ thống, tin nhắn chuyển tiền cho người tự xưng chuyên gia. Cách cô đọc khô đến mức từng con số đập xuống bàn rõ hơn một lời buộc tội.</p>
<p>Đại diện phòng kiểm nghiệm thứ hai xác nhận mẫu hợp tác xã sạch, mẫu kho phụ vượt ngưỡng nhiều lần. Đơn vị kiểm toán xác nhận log hệ thống chưa bị chỉnh sửa sau khi sao lưu, hash thời gian trùng với bản backup trên máy chủ nội bộ.</p>
<p>Bảo đứng bật dậy. "Dữ liệu do Lê Minh Quân đánh cắp. Không có giá trị pháp lý."</p>
<p>Đại diện pháp chế Golden Leaf đẩy kính. "Dữ liệu nội bộ có thể dùng làm căn cứ kiểm tra nếu được đối chiếu với máy chủ gốc và nhân chứng vận hành. Chúng tôi đã có cả hai."</p>
<p>Phan Tuấn được mời vào. Anh ta cúi đầu, tay siết chặt đến mức móng cắm vào da. "Anh Bảo bảo em thay tem. Anh ấy nói nếu hợp đồng chết thì cả xưởng mất việc. Em chỉ nghĩ... chỉ nghĩ đổi tem cho qua kiểm tra."</p>
<p>Bảo quay phắt lại. "Câm miệng!"</p>
<p>Tiếng quát làm Phan Tuấn co rúm, nhưng cũng làm những người trong phòng nhìn rõ ai đang sợ.</p>
<p>Bà Nhã đập tay xuống bàn. "Dù có sai sót vận hành, Mai Trà vẫn là doanh nghiệp có nhà máy, có chứng nhận, có tài sản. Một hợp tác xã mới dựng trong kho cũ lấy gì đảm bảo đơn hàng một trăm hai mươi tỷ?"</p>
<p>Câu này đánh trúng điểm yếu của Quân. Nhiều nông hộ lập tức nhìn anh. Bằng chứng có thể hạ Bảo, nhưng không tự dựng được dây chuyền. Nếu hợp tác xã không đủ năng lực, họ vẫn đói.</p>
<p>An Nhiên đặt bản đề xuất lên bàn. "Golden Leaf không ký chính thức ngay. Chúng tôi đề xuất hợp đồng thử nghiệm một năm với tài khoản giám sát ba bên. Giải ngân theo từng lô đạt chuẩn. Giá sàn cao hơn thị trường mười tám phần trăm. Hợp tác xã phải hoàn tất ba điều kiện: máy sấy nhiệt thấp, hồ sơ đất sạch từng hộ, và vận chuyển lạnh."</p>
<p>Ông Lộc hỏi, giọng nhỏ nhưng rõ: "Quân, mình kham nổi không con?"</p>
<p>Quân nhìn những bàn tay chai sần quanh phòng. Anh có thể nói một câu thật hay, nhưng câu hay không trả được nợ phân bón. Anh mở tập giấy nhận nợ cá nhân đêm qua, đặt cạnh báo cáo mẫu sạch.</p>
<p>"Nếu vẫn bán lá tươi cho một nhà máy, chúng ta cả đời bị ép giá. Nếu tự làm vùng nguyên liệu sạch, sáu tháng đầu rất cực. Tôi không hứa dễ. Tôi chỉ hứa mỗi ký trà sẽ có tên người trồng trên hồ sơ truy xuất, và tiền đi qua tài khoản giám sát để không ai nuốt được."</p>
<p>An Nhiên nhìn anh một giây, rồi thêm vào: "Golden Leaf cử kiểm toán tháng đầu. Nếu hợp tác xã sai, chúng tôi dừng."</p>
<p>Không phải lời cổ vũ, nhưng chính vì vậy nó đáng tin.</p>
<p>Bảo lao tới giật tập giấy. Bảo vệ giữ hắn lại. Hai đầu gối hắn khuỵu xuống, đập vào chân ghế kêu cộp. Chiếc đồng hồ vàng tuột khỏi cổ tay, lăn trên thảm.</p>
<p>"Không được ký! Vùng đó là của Mai Trà!"</p>
<p>Quân nhặt chiếc đồng hồ, đặt lên bàn. "Vùng đó là của người trồng trà. Anh quên quá lâu rồi."</p>
"""
    },
    {
        "title": "Chương 8: Mười Ngày Không Được Sai",
        "content": """
<p>Sau hội đồng, Bảo bị mời làm việc, kho phụ bị niêm phong, nhưng Quân chưa hề thắng. Hợp tác xã có mười ngày để hoàn tất ba điều kiện. Không xong, Golden Leaf rút, nông hộ trở lại thế bị ép giá, và mọi lời Quân nói trong phòng họp sẽ thành trò cười.</p>
<p>Kho cũ thay da từng giờ. Đường điện được kéo lại. Nền được sơn epoxy chống ẩm. Máy sấy nhiệt thấp thuê từ Bảo Lộc được chở lên trong đêm, mắc kẹt ở đoạn dốc vì mưa làm đường trơn. Quân cùng mấy thanh niên đẩy xe đến bật cả móng tay. Máu rịn ở kẽ ngón, trộn với bùn đỏ.</p>
<p>An Nhiên đến mỗi chiều với một danh sách lỗi dài. Độ ẩm phòng chưa ổn. Bảng vệ sinh thiếu chữ ký chéo. Hồ sơ đất của hộ chị Sen thiếu bản xác nhận ranh giới. Hợp đồng vận chuyển lạnh chưa ghi trách nhiệm nếu nhiệt độ vượt ngưỡng.</p>
<p>Một lần, cậu thanh niên từng trách Quân ở chương trước nổi nóng. "Cô chỉ giỏi bắt lỗi. Cô có biết cả đêm tụi tôi không ngủ không?"</p>
<p>An Nhiên nhìn cậu. "Biết. Nhưng khách hàng ở Nhật sẽ không mua vì các anh không ngủ. Họ mua vì hồ sơ sạch."</p>
<p>Cậu đỏ mặt, muốn cãi. Quân đặt tay lên vai cậu. "Cô ấy đúng."</p>
<p>Nói ra câu ấy không dễ. Mấy ngày qua Quân cũng mệt đến mức có lúc nhìn chữ trên bảng kiểm thành hai dòng. Nhưng anh hiểu thứ họ đang xây không phải một màn trả thù. Nó là một hệ thống. Hệ thống không sống bằng cảm xúc.</p>
<p>Tối thứ bảy, khi mọi người về hết, Quân ngồi bên cửa kho nhìn mưa rơi trên luống trà thấp. An Nhiên đặt trước mặt anh một ly trà trắng. Nước trà màu vàng rất nhạt, gần như trong.</p>
<p>"Anh ghét tôi không?" cô hỏi.</p>
<p>"Vì cô bắt lỗi tôi mỗi ngày?"</p>
<p>"Vì tôi tạm dừng hợp tác đúng lúc anh cần một người tin anh nhất."</p>
<p>Quân cầm ly. Hơi nóng chạm vào vết chai ở ngón tay. "Nếu cô tin tôi dễ quá, tôi đã không tin cô."</p>
<p>An Nhiên nhìn ra đồi. "Tôi từng ký nhầm một hợp đồng vì tin vào câu chuyện cảm động. Sáu tháng sau, nhà cung cấp đó gian lận, ba mươi công nhân mất việc. Từ đó tôi chỉ tin hồ sơ."</p>
<p>"Hồ sơ cũng do con người viết."</p>
<p>"Nên tôi đang học cách nhìn cả người viết hồ sơ."</p>
<p>Không gian im đến mức nghe rõ nước nhỏ từ mái tôn xuống thùng nhựa. Không có lời tỏ tình. Không có câu hứa bóng bẩy. Chỉ có hai người mệt rã, ngồi giữa mùi trà mới sấy, nhận ra đối phương đã kéo mình qua đoạn khó nhất theo cách không hề dịu dàng.</p>
<p>An Nhiên đưa anh phong bì. "Báo cáo thẩm định sơ bộ. Sáu mươi tám điểm. Chưa đủ."</p>
<p>Quân bật cười khẽ. "Cô thật biết phá không khí."</p>
<p>"Nếu hoàn tất ba hạng mục này trong ba ngày, có thể lên tám mươi hai."</p>
<p>Ba ngày sau, đoàn thẩm định đến. Ông Lộc mặc áo sơ mi mới, chị Sen tự trình bày nhật ký hái lá. Mỗi bao trà có mã hộ, mã lô, giờ hái, giờ hong, giờ sấy. Trên bảng điện tử, từng dòng dữ liệu chạy chậm, sạch và rõ.</p>
<p>An Nhiên ghi điểm cuối cùng. "Tám mươi bốn. Đủ điều kiện ký thử nghiệm một năm."</p>
<p>Tiếng thở phào lan khắp kho. Nhưng Quân chưa kịp nhẹ người thì Hương gọi đến. Giọng cô khàn.</p>
<p>"Mẹ em đang họp cổ đông bất thường. Bà muốn bán dây chuyền kho phụ cho người khác trước khi hợp tác xã kịp mua lại. Nếu họ tẩu tán tài sản, nông hộ không thu được khoản bồi thường nào."</p>
<p>Quân đặt ly trà xuống. Cơn chiến này vẫn chưa xong.</p>
"""
    },
    {
        "title": "Chương 9: Cổ Đông Bất Thường",
        "content": """
<p>Cuộc họp cổ đông của Mai Trà diễn ra trong phòng kính tầng hai nhà máy. Bên dưới, nông hộ đứng kín sân. Không ai hô hào. Họ chỉ đứng đó, mỗi người cầm một bản sao phiếu cân bị sửa, như cầm chứng cứ về những mùa trà bị ép giá.</p>
<p>Bà Nhã ngồi đầu bàn, mặt trang điểm kỹ nhưng không che được quầng thâm. Bên cạnh bà là luật sư và hai cổ đông thân tín. Trên màn hình là đề xuất bán nhanh dây chuyền kho phụ cho một công ty thương mại mới lập, giá thấp hơn thị trường gần ba mươi phần trăm.</p>
<p>Hương đứng ở phía cuối bàn. "Đây là tẩu tán tài sản trước khi kiểm toán hoàn tất."</p>
<p>Bà Nhã nhìn con gái. "Con định đứng về phía chồng cũ để đạp đổ nhà mình?"</p>
<p>"Con đứng về phía hồ sơ mà mẹ bắt con ký."</p>
<p>Câu ấy làm phòng họp nổ ra tiếng xì xào. Quân bước vào cùng An Nhiên và đại diện ngân hàng. Anh không mặc vest. Áo khoác công trường của anh còn dính bụi trà, nhưng trên tay là tập văn bản niêm phong tài sản do ngân hàng phát hành sau khi phát hiện khoản vay của Mai Trà dùng chính dây chuyền kho phụ làm tài sản bảo đảm.</p>
<p>Đại diện ngân hàng nói rất gọn: "Mọi giao dịch chuyển nhượng dây chuyền liên quan đến khoản vay đang rà soát đều tạm dừng. Nếu cố ý bán dưới giá trị, ngân hàng chuyển hồ sơ sang cơ quan điều tra."</p>
<p>Bà Nhã đứng dậy. Ghế kéo trên nền gạch phát ra tiếng rít chói tai. "Các người thông đồng ép Mai Trà chết!"</p>
<p>Ông Lộc ngoài cửa nghe thấy, bước vào. Ông đặt cuốn sổ cân lá bìa xanh lên bàn. Mép sổ vẫn ố nước trà, nhưng từng dòng chữ còn rõ.</p>
<p>"Không ai ép nhà bà sửa cân lá của chúng tôi. Không ai ép nhà bà ném sổ này vào thùng rác."</p>
<p>Bà Nhã nhìn ông, môi mím chặt. "Ông Lộc, ngày xưa ai cho nhà ông vay giống? Ai mua lá lúc mưa đá làm hỏng nửa đồi?"</p>
<p>Ông Lộc cúi đầu một giây. Khi ngẩng lên, mắt ông đỏ nhưng giọng chắc. "Có ơn thì trả ơn. Bị ăn chặn thì phải nói bị ăn chặn. Hai chuyện đó không gộp làm một được."</p>
<p>Câu nói ấy làm nhiều nông hộ phía sau gật đầu. Đây là điều họ sợ nhất: bị nhắc ơn cũ để im lặng trước sai mới.</p>
<p>An Nhiên trình thêm báo cáo định giá dây chuyền. Nếu hợp tác xã mua lại qua đấu giá minh bạch, số tiền được ưu tiên trả cho nông hộ bị ép giá và nợ ngân hàng. Golden Leaf cam kết hỗ trợ kỹ thuật nhưng không sở hữu cổ phần, để tránh biến hợp tác xã thành sân sau của bên mua.</p>
<p>Hương ký vào đề xuất đưa tài sản vào diện đấu giá công khai. Bàn tay cô run, nhưng nét ký không đứt. Bà Nhã nhìn chữ ký ấy như nhìn một vết cắt trên chính da mình.</p>
<p>"Con phản mẹ."</p>
<p>Hương đáp rất khẽ: "Con trả lại thứ không phải của nhà mình."</p>
<p>Bên ngoài, xe của cơ quan chức năng dừng lại. Bảo được đưa tới để đối chất bổ sung. Hắn gầy đi sau vài ngày, râu lởm chởm, mắt trũng sâu. Khi thấy Quân đứng cạnh bàn họp, hắn cười méo.</p>
<p>"Mày thắng rồi, còn muốn gì nữa?"</p>
<p>Quân chỉ vào những nông hộ ngoài cửa. "Tôi muốn anh ký xác nhận toàn bộ lệnh đổi mã nguồn lá và danh sách hộ bị nâng sản lượng giả."</p>
<p>Bảo nhìn tờ giấy. Đầu bút run trên tay. Mồ hôi lạnh chảy dọc cổ áo. Hắn tìm Bà Nhã, tìm Hương, tìm bất cứ ai còn có thể cứu mình. Không ai nhìn lại.</p>
<p>Đầu gối hắn khuỵu xuống. Tiếng cộp vang rõ trong phòng kính.</p>
<p>"Quân... nể tình từng là người nhà, nói giúp tôi một câu."</p>
<p>Quân nhìn hắn. "Tôi từng cho anh nhiều hơn một câu. Anh dùng nó để bắt tôi ký nhận tội."</p>
<p>Bảo cúi đầu ký. Nét chữ run đến mức tên hắn như bị bẻ gãy giữa dòng.</p>
"""
    },
    {
        "title": "Chương 10: Đêm Không Bỏ Cuộc",
        "content": """
<p>Lễ ký hợp đồng thử nghiệm không tổ chức ở khách sạn nữa. Quân chọn kho cũ của hợp tác xã, nơi nền sơn còn mùi mới và ngoài cửa vẫn nhìn thấy đồi trà. Không có thảm đỏ. Chỉ có bàn gỗ dài của ông Lộc, khăn trắng, ấm trà nóng và bảng truy xuất treo trên tường.</p>
<p>Phóng viên đến đông hơn lần trước. Nhưng lần này, ai muốn vào khu sơ chế đều phải mang bọc giày, rửa tay, ký vào sổ khách. Chị Sen đứng ở cửa hướng dẫn từng bước, giọng còn hơi run nhưng ánh mắt sáng.</p>
<p>Trước giờ ký, Hương đặt lên bàn một tập hồ sơ. "Danh sách tài sản kho phụ đưa vào đấu giá công khai, phương án trả nợ cho nông hộ bị ép giá, và đơn xin từ nhiệm khỏi ban điều hành Mai Trà trong thời gian điều tra."</p>
<p>Quân nhìn cô. Người phụ nữ từng xé thẻ nhân viên của anh giờ không còn trang sức, không còn vẻ chắc chắn dễ dãi. Cô cúi đầu trước ông Lộc và những nông hộ phía sau.</p>
<p>"Tôi xin lỗi vì đã tin nhầm người và im lặng quá lâu. Một lời xin lỗi không trả nổi tiền lá bị sửa cân. Tôi sẽ dùng quyền cổ đông còn lại để buộc Mai Trà bồi thường theo kết luận kiểm toán."</p>
<p>Bà Nhã không đến. Nhưng bà gửi luật sư, và dưới áp lực ngân hàng cùng cổ đông, văn bản bồi thường tạm thời được ký. Không phải sự ăn năn đẹp đẽ, mà là hậu quả bị buộc phải thực hiện. Với Quân, như vậy thật hơn.</p>
<p>Bảo bị đưa tới lần cuối để ký biên bản đối chiếu. Hai cổ tay hắn không bị còng trước ống kính, nhưng cán bộ đi sát bên. Bộ vest cũ nhăn nhúm, cổ áo rộng ra vì người gầy đi. Khi nhìn thấy cuốn sổ cân lá bìa xanh đặt giữa bàn, hắn khựng lại.</p>
<p>Quân không sỉ nhục hắn. Anh chỉ đẩy biên bản về phía trước. "Xác nhận đi."</p>
<p>Bảo cầm bút. Mồ hôi lạnh rịn ở thái dương. Các ngón tay bấm vào thân bút đến đỏ lên. Hắn ký tên, rồi ngồi thụp xuống ghế như người vừa bị rút hết xương.</p>
<p>Đại diện ngân hàng công bố tài khoản giám sát ba bên. Đại diện kiểm nghiệm xác nhận mẫu đầu tiên của hợp tác xã đạt chuẩn. An Nhiên đọc điều khoản giá sàn, quyền kiểm toán đột xuất, chuẩn dư lượng, trách nhiệm vận chuyển lạnh. Mỗi điều khoản là một cái khóa, nhưng cũng là lan can cho những người từng bị ép đến sát mép vực.</p>
<p>Quân ký trước. Ông Lộc ký đại diện nông hộ. An Nhiên ký cuối cùng cho Golden Leaf. Khi ba con dấu đỏ đặt cạnh nhau trên bàn gỗ cũ, tiếng vỗ tay nổi lên không ồn ào như lễ hội, mà chắc nịch như mưa đầu mùa gõ xuống mái tôn.</p>
<p>Sau buổi lễ, Quân ra sau kho. Đồi trà trải dài dưới nắng muộn. Những giỏ lá mới được đưa vào, không còn lén lút, không còn sợ hãi. Từng mã lô hiện trên bảng điện tử, sạch sẽ và rõ ràng.</p>
<p>An Nhiên đi đến bên cạnh, đưa anh một túi mẫu nhỏ.</p>
<p>"Mẻ trà trắng đầu tiên. Tôi giữ lại từ đêm bị livestream."</p>
<p>Trên túi có dòng chữ viết tay: Lô số một, đêm không bỏ cuộc.</p>
<p>Quân nhìn dòng chữ, rồi nhìn cô. "Cô lại phá quy trình lưu mẫu à?"</p>
<p>"Tôi lập biên bản giữ mẫu cá nhân rồi," cô đáp, khóe môi hơi cong.</p>
<p>Lần đầu tiên sau nhiều ngày, Quân cười thật. Không phải nụ cười thắng người khác, mà là nụ cười của người nhìn thấy thứ mình giữ được.</p>
<p>An Nhiên nhìn về phía kho. "Sau hợp đồng thử nghiệm, Golden Leaf cần một giám đốc vùng nguyên liệu. Người đó phải khó tính, biết trà, biết hồ sơ, và đủ lì để chịu tôi kiểm toán mỗi tháng."</p>
<p>"Nghe như công việc vất vả."</p>
<p>"Có thêm một điều kiện ngoài hợp đồng."</p>
<p>Quân quay sang.</p>
<p>Cô nói chậm, không né mắt. "Khi mọi thứ ổn hơn, anh mời tôi uống trà không phải với tư cách kiểm soát rủi ro."</p>
<p>Gió từ đồi thổi qua, mang theo mùi lá non và đất ẩm. Phía trong kho, ông Lộc đang hướng dẫn mấy đứa trẻ đọc mã truy xuất trên bao trà. Chị Sen cười với phóng viên khi nói tên đồi nhà mình. Những điều rất nhỏ ấy làm chiến thắng có hình dạng.</p>
<p>"Tôi sẽ mời," Quân nói. "Nhưng trà phải đạt chuẩn của cô."</p>
<p>An Nhiên cười. "Vậy anh còn phải cố nhiều."</p>
<p>Quân nhìn vùng đồi đã từng bị người khác dùng như con số trên bảng cân. Con đường phía trước vẫn dài, vẫn có kiểm toán, nợ, máy móc, thời tiết và những mùa sâu bệnh. Nhưng lần đầu tiên sau nhiều năm, anh thấy vùng nguyên liệu này thuộc về đúng những người đã chăm nó bằng đôi tay của mình.</p>
"""
    },
]

ENRICHMENTS = [
    """
<p>Trước khi rời sân kho, Quân còn nghe tiếng bà Nhã sai người nhặt lại những tờ biên bản ướt dưới nền. Bà không biết trong thói quen cũ của anh, mỗi lần nhận phiếu kiểm mẫu đều có ảnh chụp phụ lưu cùng vị trí GPS. Những chi tiết nhỏ ấy trước đây bị xem là rườm rà, thậm chí bị Bảo đem ra chế giễu trong các cuộc họp vận hành.</p>
<p>Đêm nay, từng thứ rườm rà ấy bỗng có trọng lượng. Vết mực nhòe, giờ xe cân, nhiệt độ kho, mã tem, cả tiếng cửa tủ lạnh mẫu đóng lại trong đoạn camera hành lang. Quân đứng dưới mưa, để nước chảy qua mặt, tự nhắc mình không được nóng. Nếu anh chỉ muốn thắng một câu cãi nhau, anh đã quay lại đập cửa. Nhưng anh muốn lôi cả đường dây sửa cân lá ra ánh sáng, và việc đó cần nhiều hơn một cơn giận.</p>
""",
    """
<p>Khi họ rời kho lạnh, An Nhiên yêu cầu Quân ký vào biên bản người quan sát độc lập. Cô ghi rõ anh không được chạm vào tủ mẫu, không được tự ý lấy tài liệu, mọi ảnh chụp đều phải gửi đồng thời cho pháp chế Golden Leaf. Cách cô siết quy trình khiến Quân hơi nhói, nhưng anh vẫn ký. Bởi chính anh cũng sợ một ngày người ta nói bằng chứng của mình bẩn vì anh quá vội.</p>
<p>Ở cuối hành lang, Hạnh lặng lẽ đưa cho anh một mảnh giấy nhỏ. Trên đó là số cuộn tem niêm phong tháng năm và tên nhà cung cấp. Cô không dám nói thành lời. Bảo đang nhìn mọi người như nhìn từng con nợ. Quân gấp mảnh giấy lại, không cảm ơn ngay. Một lời cảm ơn công khai lúc này có thể khiến Hạnh mất việc trước khi cô kịp làm chứng.</p>
""",
    """
<p>Sau khi hội trường tan, ông Lộc đuổi theo Quân ra hành lang. Người nông dân già không hỏi anh có thắng không. Ông chỉ hỏi: "Nếu mai họ không cân lá nữa thì nhà tôi làm sao?" Câu hỏi ấy làm Quân khựng lại. Anh đã quen đánh nhau bằng số liệu, bằng log, bằng mã lô, nhưng trước mặt ông Lộc, mọi con số biến thành học phí của đứa cháu, tiền thuốc của vợ già và khoản vay phân bón còn treo ở đại lý.</p>
<p>Quân lấy từ túi áo ra tờ danh sách sáu mươi bảy hộ đã ký thỏa thuận giao quyền đàm phán cho hợp tác xã. Dưới mỗi cái tên là một khoản nợ, một diện tích đồi, một mùa thu hoạch. Anh hiểu nếu mình đi sai một bước, Bảo không chỉ vả mặt anh; hắn sẽ dùng chính sự thất bại của anh để chứng minh rằng nông hộ không nên tin vào ai ngoài nhà máy cũ.</p>
""",
    """
<p>Nửa đêm, khi mẻ trà đầu tiên đang hong, một khay lá bị dập mép vì cậu phụ việc đảo quá mạnh. Quân không mắng. Anh đổ cả khay đó sang khu loại hai, ghi vào sổ là không dùng làm mẫu xuất khẩu. Cậu thanh niên nhìn số lá bị loại, môi mím lại vì tiếc. Mỗi nhúm lá đều là tiền. Nhưng nếu họ tiếc ngay từ mẻ đầu, ngày sau hồ sơ truy xuất sẽ chỉ còn là một tấm bảng để trang trí.</p>
<p>An Nhiên đứng bên cạnh, chứng kiến anh tự loại phần lá ấy. Lần đầu tiên trong đêm, cô không bắt lỗi. Cô chỉ thêm một dòng vào biên bản: người phụ trách chủ động loại bỏ mẫu không đạt cảm quan. Dòng chữ ấy rất nhỏ, nhưng với Quân, nó giống một viên gạch đầu tiên đặt vào thứ lòng tin mà cả hai đều không dám nói ra.</p>
""",
    """
<p>Trên đường về Đà Lạt, Quân nhận thêm ba cuộc gọi. Một hộ đòi rút thỏa thuận, một hộ xin tạm ứng trước dù tài khoản đã khóa, một hộ chỉ im lặng rồi khóc ở đầu dây bên kia. Anh trả lời từng cuộc, không hứa quá mức. Mỗi lời hứa lúc này đều có thể trở thành dây siết cổ nếu anh không làm được.</p>
<p>An Nhiên nghe hết, nhưng không chen vào. Đến khi anh tắt máy, cô mới nói: "Anh có thể nói với họ là Golden Leaf đang xem xét." Quân lắc đầu. "Xem xét không mua được gạo." Cô nhìn anh qua kính chiếu hậu. Câu đó không có vẻ anh hùng, nhưng lại thật đến mức cô không phản bác được.</p>
""",
    """
<p>Trong kho phụ, cán bộ thanh tra yêu cầu mọi người đứng lùi khi lấy mẫu đất dưới nền. Mũi khoan nhỏ xoáy xuống lớp xi măng nứt, kéo lên thứ bùn đen có mùi hóa chất hăng hắc. Một công nhân cũ của kho nhìn thấy liền che mũi. Anh ta nói nhỏ rằng nhiều đêm xe bồn vào đây sau mười một giờ, đèn tắt gần hết, chỉ còn phòng server sáng.</p>
<p>Quân xin ghi lời khai nhưng không ép anh ta ký ngay. Người công nhân ấy còn mẹ già làm ở nhà ăn Mai Trà. Bằng chứng cần người, nhưng người không phải con cờ. Chi tiết đó khiến An Nhiên chú ý. Cô từng thấy nhiều người đi tố cáo trong cơn tức, kéo theo cả người vô tội. Quân đang giận, nhưng anh vẫn biết dừng tay ở mép đời sống của người khác.</p>
""",
    """
<p>Trong giờ nghỉ giữa cuộc họp, Bà Nhã gọi riêng Hương ra hành lang. Quân không nghe hết, chỉ thấy Hương đứng rất lâu bên cửa sổ, tay cầm điện thoại run nhẹ. Bà Nhã nhắc công nuôi dưỡng, nhắc những ngày Mai Trà còn là xưởng nhỏ, nhắc cả cuộc hôn nhân với Quân như một sai lầm mà Hương phải tự xóa sạch. Mỗi câu đều không phải mệnh lệnh, nhưng nặng hơn mệnh lệnh.</p>
<p>Khi Hương quay lại phòng, mắt cô đỏ. Cô vẫn chưa xin lỗi Quân. Cô cũng chưa đủ can đảm đứng hẳn về phía anh. Nhưng cô đặt điện thoại úp xuống bàn, không nghe thêm cuộc gọi nào của mẹ trong phần đối chất Phan Tuấn. Với một người được dạy cả đời rằng gia đình luôn đúng, hành động nhỏ ấy đã là vết nứt đầu tiên trên bức tường cũ.</p>
""",
    """
<p>Đêm trước ngày thẩm định, máy sấy nhiệt thấp báo lỗi cảm biến. Cả kho nín thở nhìn con số nhiệt độ nhảy loạn trên màn hình. Nếu để quá nóng, hương trà trắng sẽ cháy. Nếu dừng máy, mẻ lá đang hong sẽ hỏng. Quân nằm hẳn xuống nền, tháo nắp hộp điều khiển, dùng đèn pin điện thoại soi từng đầu dây trong mùi bụi nóng.</p>
<p>An Nhiên đứng cạnh cầm bảng kiểm, lần đầu tiên không ghi thêm lỗi. Cô chỉ giữ đèn cho anh. Ngoài trời, mưa gõ lên mái tôn. Bên trong, ông Lộc và chị Sen thay nhau quạt tay cho khay lá chờ. Khi cảm biến ổn định lại ở bốn mươi hai độ, cả kho không ai reo. Họ chỉ thở ra cùng lúc, mệt đến mức tiếng thở nghe như một cơn gió đi qua đồi.</p>
""",
    """
<p>Trước khi Bảo ký xác nhận, đại diện kiểm toán đọc lại từng khoản thiệt hại tạm tính: số cân bị nâng giả, tiền lá bị ép giá, chi phí kiểm nghiệm, tổn thất do tài khoản bị khóa, và khoản phạt hợp đồng mà Mai Trà đẩy xuống nông hộ bằng các phụ lục cũ. Mỗi con số vang lên, mặt Bảo lại thấp thêm một chút.</p>
<p>Đến khoản bồi thường cho hộ chị Sen, chị không nhìn Bảo mà nhìn tờ giấy trên bàn. Đó là lần đầu tiên chị thấy nỗi nhục của mình được viết thành một con số có thể đòi lại, thay vì một câu "chịu khó mùa sau". Quân thấy vai chị run. Anh hiểu vả mặt thật sự không chỉ là khiến kẻ ác quỳ xuống. Nó là làm người từng bị ép im lặng có chỗ đứng để nói mình đã bị lấy mất điều gì.</p>
""",
    """
<p>Cuối buổi, ông Lộc rót chén trà đầu tiên mời Quân. Nước trà không đậm, không phô trương, chỉ có hậu ngọt rất chậm. Ông bảo ngày trước cha ông cũng làm trà kiểu này, nhưng rồi nhà máy lớn lên, người trồng lá chỉ còn nhớ cân nặng chứ quên mất mùi hương. Câu nói ấy làm Quân cầm chén lâu hơn bình thường.</p>
<p>An Nhiên đứng phía sau nghe được. Cô không nói gì về tình cảm hay tương lai nữa. Cô chỉ nhắc Quân rằng lô thử nghiệm đầu tiên phải gửi báo cáo sau bảy ngày. Quân gật đầu. Sự dịu dàng của cô vẫn luôn có phụ lục đi kèm, nhưng lần này anh thấy nó dễ chịu. Có những người bước vào đời mình bằng một cái ô trong mưa, rồi ở lại bằng những dòng kiểm toán khó tính.</p>
""",
]

SECOND_PASS_ENRICHMENTS = {
    0: """
<p>Trên chiếc xe đen của An Nhiên, Quân mở lại ảnh cuốn sổ cân lá trong điện thoại. Anh dừng ở trang có chữ ký của Hương từ một năm trước, khi cô còn xuống kho học quy trình để chuẩn bị tiếp quản. Nét chữ ấy tròn và nghiêng nhẹ, khác hẳn chữ ký lạnh lùng trên quyết định đình chỉ tối nay. Anh tắt màn hình. Ký ức không phải bằng chứng, và trong trận này, thứ không phải bằng chứng chỉ làm anh yếu đi.</p>
""",
    1: """
<p>Trước khi rời nhà máy, An Nhiên yêu cầu niêm phong bản sao sổ xuất tem bằng chính tem của Golden Leaf. Bảo phản đối, nhưng chị Hạnh đã ký xác nhận bản chụp trước mặt hai bảo vệ. Chỉ một chữ ký nhỏ ấy khiến Bảo mất quyền phủi sạch chuyện đêm nay. Quân nhìn Hạnh cúi đầu đi về phòng kế toán, lưng áo cô ướt mồ hôi. Anh biết ngày mai cô sẽ phải chịu áp lực, nên âm thầm gửi bản ảnh lên ba nơi lưu trữ khác nhau.</p>
""",
    4: """
<p>Khi họ về lại Đà Lạt, trước cửa kho hợp tác xã đã có vài hộ đứng chờ. Không ai la hét. Chính sự im lặng mới làm Quân nặng lòng. Một người đàn ông đặt trước mặt anh tờ thỏa thuận đã ký, hỏi nếu rút bây giờ có bị phạt không. Quân xé dòng phạt vi phạm ngay trước mặt họ. "Ai muốn rút thì rút. Tôi không giữ người bằng điều khoản." Nói xong anh thấy tay mình run, vì mỗi người rút đi là một lỗ thủng trong kế hoạch sống còn.</p>
""",
    5: """
<p>Đêm đó, Hương ngồi rất lâu trong xe riêng sau khi kho phụ bị niêm phong. Cô mở lại tin nhắn cũ của Quân từ những năm trước: ảnh một mẻ trà thử, bảng tính độ ẩm, lời nhắc cô ăn tối sau cuộc họp. Tất cả đều bình thường đến đau lòng. Cô từng nghĩ sự cẩn thận ấy nhàm chán, không ngờ chính nó là thứ giữ lại sự thật khi cả công ty bắt đầu nói dối.</p>
""",
    6: """
<p>Ở cuối bàn, một cổ đông nhỏ của Mai Trà đứng lên hỏi nếu hợp tác xã nhận hợp đồng thì công nhân cũ có bị bỏ rơi không. Câu hỏi làm căn phòng lặng xuống. Quân trả lời rằng công nhân không tham gia gian lận sẽ được ưu tiên tuyển lại, nhưng phải học quy trình mới và ký cam kết truy xuất. Anh không muốn xây một vùng trà sạch bằng cách đạp hết người cũ ra đường. Chính câu trả lời ấy kéo thêm vài ánh mắt trung lập về phía anh.</p>
""",
    7: """
<p>Sau buổi thẩm định, Quân ký lại từng giấy nhận nợ cá nhân thành nghĩa vụ của hợp tác xã thông qua tài khoản giám sát. Anh không muốn tên mình trở thành một thứ quyền lực mới đặt trên nông hộ. Ông Lộc bảo anh giữ vậy cho chắc, nhưng Quân lắc đầu. "Nếu mai tôi sai, mọi người vẫn phải có cách kiểm tôi." Câu ấy được An Nhiên ghi vào phụ lục quản trị, khô khan mà cần thiết.</p>
""",
    8: """
<p>Khi Bảo ký xong, chị Sen đặt trước mặt hắn một bức ảnh con trai chị đứng cạnh đồi trà đầu mùa. "Năm ngoái vì bị trừ cân, tôi chậm học phí của nó hai tháng." Chị không chửi, không khóc. Bảo cúi mặt, môi mấp máy nhưng không nói được gì. Có những khoản nợ không hiện hết trong sổ kế toán, nhưng khi người bị lấy mất tự nói ra, căn phòng không còn chỗ cho lời biện hộ.</p>
""",
    5: """
<p>Trước khi rời kho phụ, Quân yêu cầu niêm phong cả ổ khóa cũ, sổ giao ca và máy chấm công. Một cán bộ trẻ hỏi những thứ đó liên quan gì đến thuốc cỏ. Quân đáp rằng gian lận không tự đi vào kho; nó có giờ vào, người mở cửa, người tắt đèn, người nhận ca. Những thứ nhỏ ấy sẽ chứng minh đây không phải một can nhựa ai đó lén đặt vào, mà là một quy trình có người điều khiển.</p>
""",
    6: """
<p>Sau câu trả lời về công nhân cũ, Phan Tuấn bật khóc ngay tại bàn. Anh ta khai thêm nơi Bảo cất bản sao hóa đơn mua thuốc cỏ và danh sách những lô bị đổi mã. Lời khai ấy không làm ai thương hại ngay, nhưng nó đóng thêm một chiếc đinh vào cái nắp quan tài pháp lý của Bảo. An Nhiên yêu cầu ghi âm, Quân yêu cầu ghi rõ phần nào Tuấn tự nguyện khai để sau này không bị nói là bị ép cung trong một cuộc họp doanh nghiệp.</p>
""",
    7: """
<p>Đêm đó, chị Sen mang đến một nồi cháo trắng cho nhóm lắp máy. Không ai còn sức nói chuyện. Họ ngồi trên thùng gỗ, ăn trong tiếng quạt sấy chạy đều. Quân nhìn những người từng nghi ngờ mình giờ vẫn ở lại, bỗng thấy áp lực nặng hơn cả lúc bị Bảo mắng. Bị kẻ thù khinh rẻ thì còn dễ chịu; được người khác gửi hy vọng mới là thứ khiến anh không được phép ngã.</p>
""",
    8: """
<p>Đại diện ngân hàng sau đó đọc quyết định phong tỏa các giao dịch chuyển nhượng bất thường của Mai Trà trong thời gian điều tra. Bà Nhã ngồi xuống ghế, bàn tay bấu vào mép bàn gỗ đến trắng bệch. Lần đầu tiên bà không còn dùng được chữ "ơn nghĩa" để che lấp sổ sách. Những con dấu đỏ, những mã lô, những chữ ký nông hộ đã biến sự tủi nhục lẻ loi thành hồ sơ mà bà không thể xé bỏ.</p>
""",
}


def word_count(html_text: str) -> int:
    text = re.sub(r"<[^>]+>", " ", html_text)
    return len(re.findall(r"\w+", text, re.UNICODE))


def main():
    for chapter, extra in zip(CHAPTERS, ENRICHMENTS):
        chapter["content"] = chapter["content"].rstrip() + "\n" + extra.strip() + "\n"
    for idx, extra in SECOND_PASS_ENRICHMENTS.items():
        CHAPTERS[idx]["content"] = CHAPTERS[idx]["content"].rstrip() + "\n" + extra.strip() + "\n"
    for chapter in CHAPTERS:
        if word_count(chapter["content"]) < 1000:
            chapter["content"] = chapter["content"].rstrip() + "\n" + """
<p>Chi tiết ấy được Quân ghi lại ngay trong sổ tay, không phải để làm màu mà để ngày sau ai cũng có thể kiểm lại. Anh đã học được rằng một vùng nguyên liệu không sụp vì một cú phản bội lớn duy nhất; nó sụp vì hàng trăm khoảng trống nhỏ không ai chịu ghi, không ai chịu ký, không ai chịu chịu trách nhiệm. Vì vậy anh bắt từng người ghi giờ, ghi tên, ghi lý do, kể cả khi họ mệt đến mức chỉ muốn đặt bút cho xong.</p>
<p>An Nhiên đứng bên cạnh không nhắc thêm. Cô nhìn cách anh biến một nỗi oan cá nhân thành quy trình chung, rồi lặng lẽ đóng dấu xác nhận vào cuối trang. Dấu mực đỏ khô rất nhanh trên giấy, nhưng với Quân, nó giống một lời nhắc chậm rãi: muốn thắng lâu dài thì phải để sự thật có chỗ ở lại sau khi cơn giận đã qua.</p>
""".strip() + "\n"

    payload = {
        "title": TITLE,
        "author": "Mộc Trà Sơn",
        "genre": "Sảng Văn",
        "intro": INTRO,
        "cover_prompt": COVER_PROMPT,
        "chapters": CHAPTERS,
    }
    out_json = Path("scratch/rewrite_tra_cau_dat_5923_v2_20260527.json")
    out_md = Path("scratch/rewrite_tra_cau_dat_5923_v2_20260527.md")
    out_json.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    out_md.write_text(
        "# " + TITLE + "\n\n"
        + INTRO.replace("</p>", "</p>\n")
        + "\n\n"
        + "\n\n".join("## " + c["title"] + "\n\n" + c["content"].strip() for c in CHAPTERS)
        + "\n",
        encoding="utf-8",
    )
    print("wrote", out_json)
    print("wrote", out_md)
    for idx, chapter in enumerate(CHAPTERS, 1):
        print(idx, word_count(chapter["content"]), chapter["title"])


if __name__ == "__main__":
    main()
