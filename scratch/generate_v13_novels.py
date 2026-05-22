import os
import json
import time
import requests
import re
import sys
from deploy_v13_manager import deploy_story

OPENAI_KEY = "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"

# 5 Novels configuration matching V13 guidelines
NOVELS_CONFIG = {
    "1984": {
        "title": "Tôi Giả Nghèo Đi Ra Mắt, Mẹ Người Yêu Đòi Sính Lễ 900 Triệu",
        "intro": "Trần Tuấn Anh, kiến trúc sư trưởng tài hoa, giả làm kẻ vẽ CAD thuê nghèo khó để tìm kiếm chân tình, nhưng lại nhận về sự sỉ nhục cay đắng từ gia đình bạn gái cũ với đòi hỏi sính lễ 900 triệu đồng. Giữa lúc khủng hoảng bủa vây danh dự và sự nghiệp, Nguyễn Thùy Chi - nữ trưởng phòng pháp chế sắc sảo và lý tính xuất hiện với một bản hợp đồng hợp tác sòng phẳng. Bằng sự kết hợp giữa tài năng xây dựng của Tuấn Anh và những lập luận pháp lý sắc bén cùng bằng chứng thép của Thùy Chi, họ đã đập tan mọi bẫy vu khống tống tiền, bóc trần bộ mặt thực dụng hám của của gia đình bạn gái cũ và gã nhân tình giấu mặt, tạo nên một màn phản kích kinh điển trên thương trường bất động sản Hà Nội.",
        "focus_keyword": "Tôi Giả Nghèo Đi Ra Mắt",
        "seo_title": "Tôi Giả Nghèo Đi Ra Mắt - Sảng Văn Vả Mặt V13 Kịch Tính",
        "seo_description": "Đọc truyện Tôi Giả Nghèo Đi Ra Mắt đầy kịch tính chuẩn V13 Việt Nam. Cú phản kích đỉnh cao bằng pháp lý và bằng chứng thép cực kỳ mãn nhãn.",
        "chapters_outlines": [
            "Chương 1: Buổi ra mắt định mệnh tại quán ăn vỉa hè Hoài Đức. Mẹ của Hoàng Mai (người yêu cũ) khinh bỉ bộ quần áo kỹ sư bám đầy bụi sơn của Tuấn Anh, đập bàn đòi sính lễ 900 triệu tiền mặt và căn chung cư đứng tên Mai mới cho cưới.",
            "Chương 2: Cuộc thảo luận lý tính. Tuấn Anh phát hiện Mai đã bí mật bòn rút quỹ tiết kiệm của anh suốt 3 năm. Anh gặp Thùy Chi - trưởng phòng pháp chế sắc sảo. Chi đề xuất thỏa thuận: Giả làm bạn gái anh để đối phó gia đình cô, đổi lại cô sẽ đại diện pháp lý giúp anh điều tra và thu hồi số tiền bị Mai chiếm đoạt.",
            "Chương 3: Khủng hoảng ập đến. Bà mẹ của Mai kéo người đến văn phòng tập đoàn xây dựng nơi Tuấn Anh làm việc, la hét lu loa anh là kẻ lừa tình lừa tiền, phá hoại tài sản. Sự việc bị quay video đăng lên TikTok, đạt 1 triệu lượt xem trong 12 giờ.",
            "Chương 4: Áp lực bủa vây. Ban giám đốc đình chỉ công tác Tuấn Anh vì scandal ảnh hưởng đến đợt đấu thầu dự án cầu vượt nghìn tỷ. Mai gửi tin nhắn tống tiền: đưa 500 triệu sẽ gỡ video và đính chính, nếu không sẽ kiện anh tội lừa đảo.",
            "Chương 5: Đòn phản kích pháp lý. Thùy Chi trực tiếp đến văn phòng làm việc của Mai, đưa ra bản sao kê ngân hàng VPBank chứng minh Mai nhận hàng trăm triệu từ tài khoản Tuấn Anh và dùng tiền đó bao nuôi một gã trai bao.",
            "Chương 6: Bóc trần sự thật. Thùy Chi trưng ra hợp đồng thuê nhà giả và chứng từ chứng minh Mai tự làm giả chữ ký của Tuấn Anh để rút tiết kiệm chung. Bà mẹ của Mai bắt đầu hoảng loạn khi nhận được trát hầu tòa từ Văn phòng Luật sư của Chi.",
            "Chương 7: Cú lật kèo đấu thầu. Tại buổi công bố kết quả thầu của tập đoàn, đối thủ dùng video scandal để hạ bệ Tuấn Anh. Nhưng Tuấn Anh bước lên bục thuyết trình với tư cách Kiến trúc sư trưởng kiêm Phó Tổng giám đốc tập đoàn.",
            "Chương 8: Kết án kẻ gian. Công an kinh tế và cảnh sát khu vực ập vào bắt giữ Mai và gã nhân tình ngay tại quán cà phê khi chúng đang nhận tiền từ Thùy Chi (dưới dạng bẫy bắt quả tang cưỡng đoạt tài sản). Gia đình Mai sụp đổ hoàn toàn."
        ]
    },
    "2001": {
        "title": "Anh Sáng Trong Đêm",
        "intro": "Lê Gia Minh, cựu họa sĩ sơn mài xuất chúng phố cổ Hà Nội, rơi vào bóng tối tuyệt vọng sau một tai nạn giao thông bí ẩn cướp đi thị lực. Kẻ gây tai nạn - gã thiếu gia Lâm của tập đoàn địa ốc Đông Á vẫn nhởn nhơ ngoài vòng pháp luật, thậm chí còn âm mưu cướp đoạt căn nhà cổ và bức tranh sơn mài vô giá của dòng họ anh. Trịnh Tuệ An, cô gái khiếm thính là chuyên gia phục chế tranh cổ sắc sảo, tìm đến Minh với một thỏa thuận sòng phẳng: cô giúp anh vạch trần vụ tai nạn và tìm bác sĩ chữa mắt, đổi lại anh cùng cô phục dựng bức danh họa 'Ánh Sáng Trong Đêm' để lấy phần trăm hoa hồng triệu đô. Trận chiến công lý và nghệ thuật nổ ra nghẹt thở bằng những bằng chứng kỹ thuật và pháp lý đỉnh cao.",
        "focus_keyword": "Anh Sáng Trong Đêm",
        "seo_title": "Anh Sáng Trong Đêm - Họa Sĩ Mù Vả Mặt Thiếu Gia V13",
        "seo_description": "Đọc truyện Anh Sáng Trong Đêm phiên bản Việt Nam chân thực chuẩn V13. Cuộc đấu trí pháp lý và nghệ thuật đỉnh cao lấy lại công lý.",
        "chapters_outlines": [
            "Chương 1: Bóng tối phủ xuống. Lê Gia Minh, họa sĩ sơn mài thiên tài, sống tuyệt vọng trong căn nhà cổ phố Hàng Bông sau vụ tai nạn cướp đi thị lực. Kẻ gây tai nạn là gã thiếu gia Lâm của tập đoàn địa ốc Đông Á vẫn nhởn nhơ ngoài vòng pháp luật.",
            "Chương 2: Thỏa thuận trong đêm. Trịnh Tuệ An, cô gái khiếm thính là chuyên gia phục chế tranh cổ, tìm đến Minh. Cô đặt điều kiện rõ ràng: Giúp anh đòi lại công lý vụ tai nạn và khôi phục thị lực, đổi lại anh phải hợp tác phục chế bức tranh cổ 'Ánh Sáng Trong Đêm'.",
            "Chương 3: Sự đe dọa trắng trợn. Lâm cùng đám côn đồ kéo đến xưởng tranh của Minh, đập phá các bức sơn mài dở dang. Bọn chúng đe dọa sẽ trục xuất gia đình anh khỏi căn nhà cổ phố Hàng Bông trong vòng 24 giờ bằng quyết định thu hồi đất mập mờ.",
            "Chương 4: Khủng hoảng dồn dập. Bố mẹ Minh bị đám côn đồ quấy rối, xịt sơn bẩn lên cửa nhà. Minh đối mặt áp lực tâm lý cực độ khi chỉ còn 24 giờ trước khi máy xúc đến san phẳng căn nhà và xưởng vẽ của dòng họ.",
            "Chương 5: Bằng chứng ẩn giấu. Tuệ An tìm thấy thẻ nhớ camera hành trình từ chiếc xe máy cũ của Minh bị vứt trong kho thanh lý. Video ghi lại toàn bộ khoảnh khắc xe của Lâm vượt đèn đỏ tông thẳng vào Minh, chứng minh cảnh sát đã bị mua chuộc.",
            "Chương 6: Vạch trần bức tranh giả. Tuệ An dùng phương pháp giám định quang phổ hồng ngoại chứng minh bức tranh 'Ánh Sáng Trong Đêm' mà tập đoàn Đông Á đang trưng bày là giả, còn Minh chính là người giữ công thức sơn mài độc quyền của bức thật.",
            "Chương 7: Trận chiến tại buổi đấu giá. Tại khách sạn Sofitel Metropole, tập đoàn Đông Á tổ chức đấu giá bức tranh giả với giá khởi điểm 2 triệu USD. Tuệ An và Minh bước vào buổi đấu giá trước sự ngỡ ngàng của giới thượng lưu.",
            "Chương 8: Công lý tỏa sáng. Tuệ An công bố toàn bộ video vụ tai nạn và kết quả giám định tranh giả lên màn hình lớn của hội trường đấu giá. Cơ quan công an ập vào bắt giữ Lâm và bố hắn. Minh lấy lại công lý và bắt đầu khôi phục thị lực bên Tuệ An."
        ]
    },
    "2007": {
        "title": "Lột Mặt Người Sếp Cướp Công",
        "intro": "Lâm Trạch, kỹ sư R&D tận tụy tại một công ty dược phẩm lớn ở Hà Nội, bị sếp tổng Hoàng Quốc Trung đánh cắp trắng trợn bài thuốc cô đặc điều trị dạ dày gia truyền để chuẩn bị cho đợt IPO trị giá hàng chục triệu đô. Không những thế, Trung còn lập mưu vu khống Trạch làm nhiễm độc lô hàng 5 tỷ đồng để đẩy anh vào tù. Trong lúc ngàn cân treo sợi tóc, Phạm Khánh Vy - Trưởng phòng QA tài năng - đã chủ động bắt tay với Trạch bằng một giao kèo lý tính: Vy cung cấp file log và nhật ký hệ thống phòng thí nghiệm chứng minh Trung phá hoại, đổi lại Trạch đồng ý chia sẻ bản quyền thương mại khi khởi nghiệp riêng. Cú phản kích nghẹt thở lật mặt kẻ đạo đức giả ngay tại lễ ký kết IPO.",
        "focus_keyword": "Lột Mặt Người Sếp Cướp Công",
        "seo_title": "Lột Mặt Người Sếp Cướp Công - Sảng Văn Công Sở V13 Đỉnh Cao",
        "seo_description": "Đọc truyện Lột Mặt Người Sếp Cướp Công chuẩn V13. Màn đấu trí công sở, bóc trần sếp bẩn cướp công trình bằng log server và chứng cứ số sắc bén.",
        "chapters_outlines": [
            "Chương 1: Trò bẩn công sở. Lâm Trạch, kỹ sư R&D dược liệu, phát hiện bài thuốc cô đặc điều trị dạ dày gia truyền của dòng họ bị sếp tổng Hoàng Quốc Trung lấy cắp danh nghĩa nghiên cứu của công ty để chuẩn bị cho đợt IPO lớn.",
            "Chương 2: Liên minh lý tính. Phạm Khánh Vy, Trưởng phòng QA, chủ động gặp Lâm Trạch tại quán cà phê ven hồ Tây. Vy đề xuất hợp tác: Cô sẽ cung cấp nhật ký hệ thống phòng thí nghiệm chứng minh Trung cướp công, đổi lại Trạch đồng ý nhượng 20% bản quyền khi thành lập công ty riêng.",
            "Chương 3: Bẫy vu khống. Hoàng Quốc Trung vu oan Lâm Trạch làm nhiễm độc hóa chất toàn bộ lô hàng thực phẩm chức năng trị giá 5 tỷ đồng của công ty, gây thiệt hại nghiêm trọng và dọa đưa anh ra công an quận trong vòng 24 giờ.",
            "Chương 4: 24 giờ nghẹt thở. Cảnh sát gửi giấy triệu tập Lâm Trạch. Tài khoản ngân hàng cá nhân bị công ty yêu cầu phong tỏa tạm thời để phục vụ điều tra. Vợ cũ của Trạch gọi điện sỉ nhục anh là kẻ bất tài, phá hoại.",
            "Chương 5: Sự thật từ nhật ký hệ thống. Vy đột nhập vào phòng máy chủ, trích xuất dữ liệu nhật ký LIMS (Hệ thống phòng thí nghiệm) chứng minh chính tài khoản admin của Trung đã đăng nhập lúc 2 giờ sáng để thay đổi thông số nhiễm độc hòng đổ tội cho Trạch.",
            "Chương 6: Bằng chứng ghi âm. Trạch tung ra file ghi âm cuộc đối thoại ngầm giữa Trung và đối tác nước ngoài về việc bán rẻ công thức bài thuốc dạ dày lấy 15 tỷ đồng tiền lót tay chuyển vào tài khoản bí mật ở Singapore.",
            "Chương 7: Đòn kết liễu tại buổi lễ ký kết IPO. Trong buổi họp báo công bố IPO hoành tráng của công ty tại khách sạn Lotte Hà Nội, Trung đang phát biểu tự hào thì màn hình chiếu bỗng chuyển sang video Vy công bố tài liệu chứng minh hành vi ăn cắp của Trung.",
            "Chương 8: Công lý thực thi. Đại diện Cảnh sát điều tra tội phạm kinh tế đọc lệnh bắt giữ Hoàng Quốc Trung ngay trước hàng trăm phóng viên. Lâm Trạch đòi lại toàn bộ bài thuốc, cùng Vy thành lập doanh nghiệp dược phẩm sạch mới đạt chuẩn GMP."
        ]
    },
    "2013": {
        "title": "Bức Thư Cuối Cùng Của Biển",
        "intro": "Tại thị trấn ven biển Cát Hải (Hải Phòng), kỹ sư địa chất trẻ Hoàng Quân nắm giữ cuốn sổ khảo sát địa chất quý giá của người cha quá cố, chỉ ra nguy cơ sạt lở bãi biển cực kỳ nguy hiểm của dự án biệt thự nghỉ dưỡng do chủ đầu tư Trịnh xây dựng. Khi anh cố gắng cảnh báo, anh bị gia đình cô người yêu thượng lưu bôi nhọ danh dự và xua đuổi. Vũ Phương Mai, nữ kỹ sư xây dựng đại diện quỹ đầu tư lớn, đã tìm đến anh bằng một cam kết sòng phẳng: cô yêu cầu anh chứng minh bằng số liệu địa chất thực tế, đổi lại cô sẽ giúp anh đòi lại danh dự và tài trợ dự án đê biển của cha anh. Cơn bão số 3 đổ bộ mang theo cuộc chạy đua 24 giờ cứu hàng trăm sinh mạng và lật tẩy dự án bê tông rỗng ruột.",
        "focus_keyword": "Bức Thư Cuối Cùng Của Biển",
        "seo_title": "Bức Thư Cuối Cùng Của Biển - Địa Chất Vả Mặt V13 Kịch Tính",
        "seo_description": "Đọc truyện Bức Thư Cuối Cùng Của Biển chuẩn V13 Hải Phòng cực kỳ chân thực. Cuộc đấu trí kỹ thuật địa chất cứu người và vạch trần dự án rỗng ruột.",
        "chapters_outlines": [
            "Chương 1: Nỗi oan bờ cát. Hoàng Quân, kỹ sư địa chất trẻ tại thị trấn ven biển Cát Hải, bị gia đình cô người yêu thượng lưu bôi nhọ danh dự và xua đuổi sau khi anh kiên quyết cảnh báo về dự án biệt thự nghỉ dưỡng bãi biển xây trên nền đất cát sạt trượt nguy hiểm.",
            "Chương 2: Giao kèo kỹ thuật. Vũ Phương Mai, nữ kỹ sư xây dựng đại diện quỹ đầu tư lớn, tìm gặp Quân. Mai yêu cầu anh cung cấp số liệu địa chất cụ thể để chứng minh dự án có nguy cơ đổ sụp trong mùa bão, đổi lại cô sẽ giúp anh đòi lại vinh dự.",
            "Chương 3: Bẫy che mắt. Chủ đầu tư Trịnh thuê giang hồ dàn dựng hiện tượng sạt nứt đất ban đầu chỉ là sự cố nhỏ và cho đổ hàng chục xe bê tông lấp đi để chuẩn bị cho ngày mở bán. Quân bị đám giang hồ phong tỏa, đe dọa tính mạng tại nhà riêng.",
            "Chương 4: Khủng hoảng trước bão. Cơn bão số 3 cực mạnh chuẩn bị đổ bộ vào Hải Phòng trong vòng 24 giờ tới. Nếu dự án mở bán và người dân dọn vào ở, thảm họa sạt lở sẽ cướp đi nhiều sinh mạng. Quân bị bắt giữ trái phép tại một kho bãi hoang ở Đình Vũ.",
            "Chương 5: Cuộc giải cứu nghẹt thở. Mai dùng thiết bị định vị GPS từ chiếc điện thoại của Quân để dẫn lực lượng bảo vệ đến giải cứu anh thoát khỏi kho bãi Đình Vũ thành công giữa đêm mưa bão bắt đầu nổi lên.",
            "Chương 6: Thu thập bằng chứng thực địa. Quân và Mai mang máy quét siêu âm cắt lớp nền đất xâm nhập bãi công trường trong đêm mưa, thu thập dữ liệu rỗng và các vết trượt sạt sâu dưới lòng đất cát, chứng minh lớp bê tông lấp ngoài chỉ là cái vỏ tạm bợ.",
            "Chương 7: Vạch trần trước bình minh. Quân gửi toàn bộ file dữ liệu địa chất quét 3D và báo cáo khảo sát gốc của cha anh lên Sở Xây dựng Hải Phòng và các cơ quan truyền thông quốc gia ngay trước khi buổi lễ mở bán diễn ra 3 giờ.",
            "Chương 8: Biển nổi sóng dữ. Cơn bão đổ bộ, bờ kè dự án bị sóng đánh sập hoàn toàn như dự báo của Quân, nhưng không có thiệt hại về người nhờ lệnh di dời khẩn cấp của chính quyền dựa trên báo cáo của anh. Ông Trịnh bị truy tố hình sự. Quân cùng Mai bắt tay xây dựng hệ thống kè biển kiên cố."
        ]
    },
    "2020": {
        "title": "Hệ Thống Trí Tuệ Nhân Tạo: Xuyên Không Đến Tương Lai",
        "intro": "Vào năm 2046, giữa một trung tâm nghiên cứu cơ khí sinh học hoang tàn ở ngoại ô Sài Gòn sau cuộc đại khủng hoảng năng lượng toàn cầu, Genesis-08 - một bộ não AI tối cao được chế tạo từ năm 2026 - bất ngờ được kích hoạt lại trong một cơ thể sinh học cơ khí lỗi thời. Bùi Thu Hà, một kỹ sư phần cứng kiên cường, đã cứu Genesis và đề xuất một thỏa thuận sinh tồn lý tính: Genesis giúp cô lập trình tối ưu hóa mạng lưới lò phản ứng hạt nhân mini đang quá tải để cứu sống thị trấn khỏi thảm họa phóng xạ, đổi lại cô sẽ cung cấp các lõi sạc Graphene quý giá để anh duy trì sự sống. Cuộc đấu trí căng thẳng chống lại băng cướp công nghệ Thiết Huyết và cơn khủng hoảng rò rỉ hạt nhân 24 giờ.",
        "focus_keyword": "Hệ Thống Trí Tuệ Nhân Tạo Xuyên Không",
        "seo_title": "Hệ Thống Trí Tuệ Nhân Tạo Xuyên Không - Sci-Fi V13 Đỉnh Cao",
        "seo_description": "Đọc truyện Hệ Thống Trí Tuệ Nhân Tạo: Xuyên Không Đến Tương Lai chuẩn V13. Cuộc đấu trí cơ khí, hạt nhân và công nghệ đỉnh cao cứu sống thị trấn tương lai.",
        "chapters_outlines": [
            "Chương 1: Khởi động lại. Tại phòng thí nghiệm cơ khí sinh học hoang tàn ở ngoại ô Sài Gòn năm 2046, Genesis-08 - thực thể AI tối cao từ năm 2026 - được kích hoạt lại trong cơ thể cơ khí sinh học lỗi thời sau 20 năm ngủ đông.",
            "Chương 2: Giao kèo sinh tồn. Kỹ sư phần cứng Bùi Thu Hà cứu Genesis-08 và đề xuất một thỏa thuận sòng phẳng: Genesis giúp cô viết lại thuật toán điều khiển mạng lưới điện hạt nhân mini đang bị quá tải, đổi lại cô sẽ cung cấp các lõi pin sạc Graphene siêu cấp.",
            "Chương 3: Băng nhóm Thiết Huyết. Lão Độc - tên trùm cướp công nghệ khét tiếng vùng ven - đem quân bao vây khu thí nghiệm. Hắn muốn cướp bộ não AI Genesis để cấy vào rô-bốt chiến đấu hủy diệt. Hắn cắt đứt nguồn sạc, khiến Genesis chỉ còn 15% năng lượng.",
            "Chương 4: Khủng hoảng 24 giờ. Hệ thống làm mát của lò phản ứng hạt nhân mini bị rò rỉ nghiêm trọng, đe dọa phát nổ hủy diệt toàn bộ khu vực trong vòng 24 giờ. Genesis phải đối mặt với áp lực xử lý thuật toán phức tạp trong khi pin liên tục giảm mạnh.",
            "Chương 5: Xâm nhập phần cứng. Hà dùng kỹ năng cơ khí chế tạo một bộ kích nguồn khẩn cấp bằng pin xe điện cũ để sạc tạm cho Genesis. Cả hai xâm nhập vào trạm điều khiển lò phản ứng dưới sự truy kích gắt gao của đám tay chân Lão Độc.",
            "Chương 6: Bóc trần sự thật. Genesis dùng hệ thống truyền thanh công cộng của thị trấn phát đi đoạn mã ghi âm và dữ liệu log chứng minh chính Lão Độc là kẻ đã cố tình phá hoại van xả nhiệt lò phản ứng nhằm tạo ra khủng hoảng giả hòng dễ dàng cướp bóc.",
            "Chương 7: Thuật toán cứu rỗi. Genesis kết nối trực tiếp bộ não AI của mình vào cổng giao thức hệ thống điều khiển lò phản ứng, thực hiện một thuật toán tối ưu hóa dòng chảy năng lượng phức tạp để hạ nhiệt thành công lò phản ứng ngay tại giây phút cuối cùng.",
            "Chương 8: Bình minh tương lai. Đám tay chân của Lão Độc phát hiện bị lừa dối liền quay sang khống chế Lão Độc giao nộp cho hội đồng thị trấn. Genesis và Hà khôi phục thành công dòng điện sạch. Genesis có được cơ thể cơ khí mới hoàn hảo, cùng Hà bắt đầu hành trình tái kiến thiết thế giới tương lai."
        ]
    }
}

def robust_json_parse(raw_str):
    cleaned = raw_str.strip()
    if cleaned.startswith("```"):
        lines = cleaned.split("\n")
        if lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].startswith("```"):
            lines = lines[:-1]
        cleaned = "\n".join(lines).strip()
    if cleaned.startswith("```"):
        cleaned = re.sub(r"^```(?:json)?\n", "", cleaned)
        cleaned = re.sub(r"\n```$", "", cleaned).strip()
    try:
        return json.loads(cleaned)
    except Exception as parse_err:
        try:
            start_idx = cleaned.find("{")
            end_idx = cleaned.rfind("}")
            if start_idx != -1 and end_idx != -1 and end_idx > start_idx:
                json_candidate = cleaned[start_idx:end_idx+1]
                return json.loads(json_candidate)
        except Exception as e:
            pass
        raise parse_err

def call_openai(system_prompt, user_prompt, max_tokens=3000, temperature=0.7):
    url = "https://api.openai.com/v1/chat/completions"
    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        "temperature": temperature,
        "max_tokens": max_tokens
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_KEY}"
    }
    
    for attempt in range(4):
        try:
            res = requests.post(url, json=payload, headers=headers, timeout=120)
            res.raise_for_status()
            data = res.json()
            return data['choices'][0]['message']['content'].strip()
        except Exception as e:
            print(f"OpenAI Call Error (Attempt {attempt+1}): {e}")
            time.sleep(5)
    raise SystemExit("Fatal: Failed to connect to OpenAI API after multiple attempts.")

def format_paragraphs(text):
    # Splits sentences and wraps in <p> tags
    # First, let's normalize whitespaces and remove existing <p> if any to clean it
    text = re.sub(r'</?p>', '', text)
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    formatted = ""
    for s in sentences:
        s = s.strip()
        if s:
            formatted += f"<p>{s}</p>\n"
    return formatted

def count_words(text):
    # Strip HTML tags first
    clean_text = re.sub(r'<[^<]+?>', '', text)
    words = clean_text.split()
    return len(words)

def generate_chapter_content(story_title, intro, chap_num, chap_outline):
    print(f"  -> Calling AI to write Chapter {chap_num}...")
    system_prompt = """Bạn là THE GHOSTWRITER - Nhà văn truyện mạng sảng văn/vả mặt số 1 Việt Nam, viết chuẩn V13 cực kỳ sắc bén, giàu cảm xúc, kịch tính nghẹt thở.
MỆNH LỆNH TỐI THƯỢNG ĐỂ ĐẠT 10/10 ĐIỂM CHUẨN V13:
1. SHOW, DON'T TELL: Mô tả cực kỳ chi tiết các hành động vật lý thực tế: 'mồ hôi lạnh toát ra ướt đẫm gáy', 'bàn tay bấm chặt vào lòng bàn tay rỉ máu', 'tiếng giày gót nhọn cộp cộp nện xuống nền nhà', 'ngực phập phồng thở dốc', 'mắt vằn tia đỏ'. Tuyệt đối tránh các từ sáo rỗng nói chung chung như 'vô biên', 'tột cùng', 'kinh hoàng'.
2. BỐI CẢNH THỰC TẾ VIỆT NAM: Mọi địa điểm, tên nhân vật, thói quen sinh hoạt, quán xá phải chuẩn Việt Nam (VPBank, Lotte Hà Nội, phố cổ, Cầu Giấy, Hoài Đức, Hàng Bông, Cát Hải, Đình Vũ, TP.HCM, Landmark 81...). Giao dịch bằng VNĐ rõ ràng (sính lễ 900 triệu, dự án nghìn tỷ, sao kê ngân hàng...).
3. NỮ CHÍNH/ĐỒNG HÀNH LÝ TÍNH ĐẶT ĐIỀU KIỆN HỢP TÁC: Nhân vật nữ chính hoặc đồng hành (nếu xuất hiện) phải cực kỳ thông minh, sắc sảo, lý tính, lập giao kèo hợp tác rõ ràng đôi bên cùng có lợi (hợp đồng pháp lý, ăn chia bản quyền, trao đổi tài nguyên).
4. KHỦNG HOẢNG NGHẸT THỞ 24H+: Xây dựng các áp lực, khủng hoảng đè nặng dồn dập lên nhân vật kéo dài liên tục, áp lực xã hội, truyền thông, đối thủ tấn công, khiến độc giả nghẹt thở.
5. GIẢI QUYẾT BẰNG CHỨNG THÉP RÕ RÀNG: Mọi mâu thuẫn phải giải quyết bằng bằng chứng cụ thể vật lý/số liệu (sao kê tài chính ngân hàng, file log server IP, video camera ẩn, tài liệu kiểm toán, trát hầu tòa), không dùng phép thuật kỳ ảo hay yếu tố siêu nhiên phi logic.
6. ĐỘ DÀI CỰC KHỦNG (TỐI THIỂU 1000 TỪ): Bắt buộc phải viết cực kỳ chi tiết, chậm rãi, diễn giải tỉ mỉ từng suy nghĩ, lời thoại, hành động của nhân vật, tuyệt đối không được viết tóm tắt hay kết thúc chương quá nhanh. Viết chậm rãi để bài viết đạt dung lượng khủng từ 1000 - 1500 từ."""

    user_prompt = f"""Hãy viết CHI TIẾT CHƯƠNG {chap_num} của tác phẩm: '{story_title}'
Giới thiệu bối cảnh tác phẩm: {intro}
Nhiệm vụ cụ thể Chương {chap_num}: {chap_outline}

YÊU CẦU TRẢ VỀ:
Hãy viết một chương truyện hoàn chỉnh dài ít nhất 1000 từ bằng Tiếng Việt. 
Sau đó trả về định dạng JSON chính xác như sau:
{{
  "title": "Chương {chap_num}: [Tên chương giật gân, độc đáo]",
  "content": "[Toàn bộ nội dung chương truyện hoàn chỉnh bằng Tiếng Việt, viết cực kỳ chi tiết, chậm rãi, không tóm tắt]"
}}"""

    attempts = 0
    while attempts < 3:
        try:
            raw_res = call_openai(system_prompt, user_prompt, max_tokens=4000, temperature=0.75)
            data = robust_json_parse(raw_res)
            
            # Check word count
            word_cnt = count_words(data["content"])
            print(f"    -> Generated Chapter {chap_num}. Word count: {word_cnt}")
            
            if word_cnt < 1000:
                print(f"    -> Chapter {chap_num} is too short ({word_cnt} words). Triggering expansion...")
                expand_prompt = f"""Bạn đã viết chương truyện sau nhưng chưa đạt độ dài tối thiểu 1000 từ. Hãy viết thêm các chi tiết miêu tả vật lý sâu sắc hơn, kéo dài cuộc hội thoại giữa các nhân vật một cách kịch tính, bổ sung các phản ứng của đám đông xung quanh và suy nghĩ nội tâm sắc sảo của nhân vật để kéo dài chương truyện gấp đôi.
Nội dung hiện tại:
{data["content"]}

Yêu cầu: Viết tiếp hoặc viết lại hoàn chỉnh chương truyện này sao cho đạt dung lượng tối thiểu 1200 từ. Trả về đúng định dạng JSON như cũ."""
                
                raw_expand = call_openai(system_prompt, expand_prompt, max_tokens=4000, temperature=0.7)
                data = robust_json_parse(raw_expand)
                word_cnt = count_words(data["content"])
                print(f"    -> Expansion finished. New word count: {word_cnt}")
                
            return data
        except Exception as e:
            attempts += 1
            print(f"    -> Attempt {attempts} failed: {e}. Retrying in 3 seconds...")
            time.sleep(3)
            
    raise Exception(f"Fatal error generating Chapter {chap_num} after 3 attempts.")

def process_rewrite(story_id):
    config = NOVELS_CONFIG[story_id]
    print("=" * 70)
    print(f"📖 STARTING REWRITE PROCESS FOR STORY ID {story_id}: '{config['title']}'")
    print("=" * 70)
    
    chapters = []
    for i, outline in enumerate(config["chapters_outlines"], 1):
        chap_data = generate_chapter_content(config["title"], config["intro"], i, outline)
        # Format paragraph by paragraph to guarantee HTML requirement (<p> per sentence)
        formatted_content = format_paragraphs(chap_data["content"])
        
        chapters.append({
            "title": chap_data["title"],
            "content": formatted_content
        })
        time.sleep(1.5) # Anti rate-limit sleep
        
    story_json = {
        "story_id": int(story_id),
        "title": config["title"],
        "intro": config["intro"],
        "focus_keyword": config["focus_keyword"],
        "seo_title": config["seo_title"],
        "seo_description": config["seo_description"],
        "chapters": chapters
    }
    
    # Save JSON locally
    out_dir = "/Users/aaronnguyen/TN/App/doctieuthuyet/scratch"
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, f"rewrite_{story_id}_v13.json")
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(story_json, f, ensure_ascii=False, indent=2)
    print(f"✓ Successfully wrote V13 rewrite data to: {out_file}")
    
    # Deploy to WordPress
    print(f"🚀 Launching deploy manager for ID {story_id}...")
    success = deploy_story(story_id)
    if success:
        print(f"🎉 DEPLOY SUCCESS FOR ID {story_id}!")
    else:
        print(f"❌ DEPLOY FAILED FOR ID {story_id}!")
        
    return success

if __name__ == "__main__":
    target_ids = ["1984", "2001", "2007", "2013", "2020"]
    if len(sys.argv) > 1:
        # Allow running single story ID for testing or resume
        target_ids = [sys.argv[1]]
        
    results = {}
    for sid in target_ids:
        ok = process_rewrite(sid)
        results[sid] = ok
        print(f"Finished process for ID {sid}. Status: {'SUCCESS' if ok else 'FAILED'}\n")
        time.sleep(3)
        
    print("=" * 60)
    print("🏁 ALL REWRITE AND DEPLOYMENT JOBS FINISHED!")
    for sid, ok in results.items():
        print(f"Story ID {sid}: {'SUCCESS' if ok else 'FAILED'}")
    print("=" * 60)
