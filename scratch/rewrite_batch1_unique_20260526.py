#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Rewrite Batch 1 stories 2-5 with distinct arcs and set pieces."""

from __future__ import annotations

import json
from pathlib import Path


BASE = Path("scratch/batch_20_full_stories_20260526")
STORIES = BASE / "stories"


def p(text: str) -> str:
    return f"<p>{text}</p>"


def build_chapter(title: str, paragraphs: list[str]) -> dict:
    return {"title": title, "content": "\n".join(p(x) for x in paragraphs)}


def deepen_chapters(story: dict, flavor: dict) -> dict:
    lead = flavor["lead"]
    ally = flavor["ally"]
    villain = flavor["villain"]
    craft = flavor["craft"]
    object_a = flavor["object_a"]
    object_b = flavor["object_b"]
    place = flavor["place"]
    stakes = flavor["stakes"]
    sensory = flavor["sensory"]
    for idx, chapter in enumerate(story["chapters"], 1):
        chapter_title = chapter["title"].split(":", 1)[-1].strip()
        extra = [
            f"Riêng ở mốc \"{chapter_title}\", {craft} không còn là phông nền mà trở thành cách sự thật tự mở miệng. {lead} tách từng lớp trách nhiệm theo thứ tự của chương này: người ký trước, người nhận sau, người im lặng lâu nhất và người hưởng lợi nhiều nhất. Cách tách ấy khiến {villain} không thể gom mọi thứ thành một câu thanh minh mơ hồ.",
            f"{ally} dựng lại dòng thời gian tại {place}, nhưng mỗi chương cô chọn một điểm neo khác. Lần này điểm neo là \"{chapter_title}\": giờ xuất hiện của vật chứng, người đầu tiên chạm vào nó, và khoảng trống mà đối thủ cố tình để mờ. Cô bắt mọi lời nói quay về giấy tờ, vì chỉ giấy tờ mới đủ lạnh để không bị nước mắt mua chuộc.",
            f"{object_a.capitalize()} được soi lại dưới góc của biến cố này. {lead} không nhìn nó như bằng chứng chung chung; anh chỉ ra chi tiết riêng của chương: một mép giấy, một vết xước, một mã thời gian, một mùi vật liệu hoặc một dấu lưu kho không thể tự nhiên xuất hiện. Những chi tiết nhỏ ấy làm lời nói dối mất chỗ đứng.",
            f"{villain} chuyển sang gây áp lực quanh {object_b}, nhưng cách đánh của hắn ở chương này lộ thêm một điểm yếu. Hắn càng muốn người khác tin rằng mọi thứ chỉ là hiểu lầm, càng để lộ rằng hắn biết chính xác chi tiết nào sẽ giết mình.",
            f"{stakes} buộc {lead} phải đi tiếp, nhưng động cơ của anh ở chương này không chỉ là trả thù. Anh nhìn những người liên quan tới \"{chapter_title}\" và hiểu nếu mình bỏ cuộc, họ sẽ học được rằng làm đúng vẫn có thể bị xóa tên. Điều đó còn đáng sợ hơn một lần thua tiền.",
            f"Có một khoảnh khắc {sensory} khiến anh dừng tay vài giây. Cảm giác ấy nối thẳng về ngày bị sỉ nhục, nhưng không lặp lại nó. Bây giờ anh có thêm hồ sơ, người làm chứng, và một người đồng hành biết hỏi khó đúng lúc thay vì vỗ vai cho qua.",
            f"Khi khép lại chương này, {ally} không khen {lead}. Cô đưa anh danh sách việc cần làm tiếp theo, trong đó có một dòng gạch chân riêng cho \"{chapter_title}\". Anh nhận lấy, mệt đến tê vai, nhưng yên tâm vì trận này đang được thắng bằng từng chi tiết sạch.",
        ]
        chapter["content"] = chapter["content"].rstrip() + "\n" + "\n".join(p(x) for x in extra)
    return story


def rewrite_story_02() -> dict:
    title = "Bị Đuổi Khỏi Xưởng Gốm Bát Tràng, Tôi Dùng Men Cổ Thắng Đơn Hàng Trăm Tỷ Của Người Yêu Cũ"
    intro = "".join(
        p(x)
        for x in [
            "\"Cái tay chỉ biết trộn đất như anh mà cũng đòi ngồi bàn xuất khẩu?\" Vũ Gia Khiêm hất khay men thử xuống nền gạch, để những mảnh gốm xanh rạn vỡ dưới chân Phạm Duy An.",
            "Nguyễn Mỹ Hân đứng cạnh hắn, mặc áo dài lụa trắng, bình thản tuyên bố công thức men tro gia truyền của anh đã được xưởng đăng ký dưới tên cô. Cả nhà xưởng im lặng, chỉ còn tiếng lò nung thở phì phò như một con thú bị bịt miệng.",
            "Nhưng Duy An không chỉ giữ ký ức nghề. Anh còn giữ sổ lò ba đời, mẫu men thử niêm phong, biên bản giám định tro rơm và video camera ghi lại đêm công thức bị sao chụp.",
            "Khi lô hàng khách sạn Nhật trị giá 180 tỷ bị treo vì cáo buộc men độc, người từng bị đá khỏi lò nung phải trở lại bằng đôi bàn tay đầy sẹo và một màu men không ai giả được.",
        ]
    )
    chapters = [
        build_chapter(
            "Chương 1: Mẻ Men Bị Đạp Nát Trước Lò Rồng",
            [
                "Lò nung ở Bát Tràng nóng đến mức hơi thở cũng có vị tro. Phạm Duy An đứng cạnh dãy chum men cổ, tay áo xắn quá khuỷu, lòng bàn tay còn dính bột đất trắng. Anh vừa hoàn thành mẻ thử cuối cùng cho đơn hàng khách sạn Nhật thì Vũ Gia Khiêm dẫn đoàn khách vào xưởng như thể nơi này chưa từng có anh.",
                "Trên bàn dài là hai mươi chiếc chén mẫu, men xanh ngả xám, mặt men rạn như sương đọng trên đá cổ. Duy An biết từng vết rạn ấy đến từ tỷ lệ tro rơm, nước giếng và nhiệt độ hạ lò lúc rạng sáng. Nhưng Gia Khiêm chỉ cười, đặt bảng tên của Nguyễn Mỹ Hân trước bộ mẫu rồi nói công thức là thành quả của phòng thiết kế mới.",
                "Mỹ Hân không nhìn anh. Cô từng cùng anh thức ba đêm canh lò, từng nói màu men này là tương lai của cả làng nghề. Bây giờ cô nâng ly trà trước mặt khách Nhật và bảo Duy An chỉ là thợ phụ được thuê theo mùa.",
                "Khi Duy An phản đối, Gia Khiêm hất khay men thử xuống đất. Những mảnh chén vỡ bắn vào mu bàn tay anh, rạch một đường mỏng. Hắn cúi xuống, nhặt một mảnh gốm rồi nghiền dưới gót giày: \"Tay nghề không có giấy tờ thì cũng chỉ là chuyện kể trong quán nước.\"",
                "Đám thợ trẻ cúi mặt. Họ biết ai là người trộn men, nhưng khoản lương cuối tháng nằm trong tay Gia Khiêm. Duy An nhìn từng gương mặt ấy, không trách. Làng nghề nhiều đời đã dạy anh rằng đất muốn thành gốm phải qua lửa; người muốn giữ nghề đôi khi cũng phải qua một lần bị nung đến nứt lòng.",
                "Anh bị đuổi ra khỏi xưởng trước khi lò mở. Trời chiều trên bờ sông Hồng đầy bụi. Duy An ngồi ở bậc đá, lấy khăn quấn vết thương, rồi gọi cho Đỗ Hoài Phương, người phụ trách thu mua của khách Nhật. Anh không xin cô tin mình. Anh chỉ nói: \"Nếu chị muốn biết men này của ai, hãy nhìn tro trong xương men, không nhìn bảng tên.\"",
                "Đêm ấy, anh quay về căn nhà cũ của ông nội. Trong hòm gỗ mốc là sổ lò ghi bằng mực tím, có cả vết cháy xém từ trận lụt năm xưa. Duy An đặt bàn tay bị rách lên trang giấy, thấy máu thấm cạnh dòng chữ: mẻ men tốt nhất luôn biết tố cáo kẻ nói dối.",
                "Ở xưởng, Gia Khiêm mở tiệc mừng. Nhưng khi lò nguội, ba chiếc bình chủ lực xuất hiện vệt rộp nhỏ ở đáy. Mỹ Hân nhìn thấy đầu tiên, mặt cô thoáng trắng. Màu men có thể bị chép, nhưng nhịp thở của lò thì không.",
            ],
        ),
        build_chapter(
            "Chương 2: Người Nhật Đòi Kiểm Tro Trong Xương Men",
            [
                "Sáng hôm sau, Đỗ Hoài Phương đến nhà Duy An bằng xe riêng, không mang hoa hay lời an ủi. Cô đặt một chiếc chén mẫu lên bàn gỗ cũ rồi yêu cầu anh chứng minh vì sao mặt men thật phải có ánh chìm chứ không bóng lộ như hàng công nghiệp.",
                "Duy An đổ nước chè nóng vào chén. Khi hơi nước bốc lên, màu men chuyển từ xanh xám sang xanh ngọc rất nhạt. Anh giải thích đó là phản ứng của lớp tro rơm đã lọc qua vải thô, thứ không thể tạo bằng phẩm màu. Hoài Phương ghi lại từng chữ, sau đó yêu cầu lấy mẫu đối chứng từ lô của Gia Khiêm.",
                "Họ không đến xưởng bằng cửa chính. Hoài Phương thuê một chuyên gia gốm Nhật đi cùng, người chỉ nói ít nhưng nhìn men rất lâu. Ông cầm kính lúp soi đáy chén rồi hỏi bằng tiếng Việt lơ lớ: \"Lò này hạ nhiệt quá vội. Ai canh?\" Câu hỏi ấy làm quản đốc xưởng cứng họng.",
                "Gia Khiêm bước ra với nụ cười rộng, nói mọi việc chỉ là hiểu lầm của thợ cũ cay cú. Nhưng khi chuyên gia yêu cầu xem nhật ký nhiệt, hắn không đưa được bản gốc. Mỹ Hân chen vào, bảo hệ thống lưu tự động bị lỗi đúng đêm nung. Hoài Phương chỉ đóng nắp bút, không tranh cãi.",
                "Duy An đem ra một thứ khác: mảnh sứ thử ông nội từng gọi là xương lò. Trên đó có ký hiệu nhỏ khắc bằng kim trước khi tráng men. Ký hiệu ấy trùng với sổ lò trong hòm gỗ, từng ngày từng mẻ. Người Nhật nhìn ký hiệu rồi cúi đầu rất nhẹ, như chào một người thợ đã khuất.",
                "Gia Khiêm đổi giọng, tố Duy An mang đồ cũ ra lừa khách. Nhưng Duy An yêu cầu giám định thành phần tro. Anh biết trong mẻ men của mình có tro vỏ trấu từ ruộng ven sông, lẫn một lượng khoáng rất nhỏ mà lò công nghiệp không có. Đó là dấu vân tay của đất.",
                "Buổi kiểm mẫu được niêm phong ngay tại xưởng. Những túi nhỏ chứa bột men, mảnh vỡ, mẫu nước giếng được ký tên bởi ba bên. Mỹ Hân cầm bút mà tay run, nét ký lệch khỏi dòng kẻ. Duy An nhìn thấy nhưng không nói gì. Anh muốn sự thật nói bằng phòng thí nghiệm, không bằng nước mắt cũ.",
                "Tối đó, đơn hàng Nhật tạm dừng. Gia Khiêm tức đến ném cả bộ ấm tử sa vào tường. Nhưng lần này người trong xưởng không còn cúi đầu hoàn toàn. Một thợ trẻ lén gửi cho Duy An ảnh chụp bảng nhiệt đêm nung, đúng khoảnh khắc lò bị hạ sai.",
            ],
        ),
        build_chapter(
            "Chương 3: Lò Nung Bị Niêm Phong Vì Tin Đồn Men Độc",
            [
                "Ba ngày sau, tin xưởng dùng men độc lan khắp các nhóm làng nghề. Người ta chụp ảnh bình gốm rộp đáy, thêm chữ đỏ chói rồi gắn tên Duy An vào như thể anh mới là kẻ phá hoại. Đơn vị kiểm định chưa trả kết quả, nhưng đám đông đã có bản án riêng.",
                "Gia Khiêm tận dụng thời cơ, yêu cầu chính quyền kiểm tra đột xuất căn nhà cũ của Duy An. Hắn tin ở đó chỉ có mấy chum men lộn xộn và một người thợ nghèo không biết tự bảo vệ. Nhưng khi đoàn kiểm tra tới, mọi hũ men đều dán ngày, ghi nguồn tro, có mẫu đối chiếu được bọc vải dầu.",
                "Hoài Phương đứng cạnh, không nói thay anh. Cô chỉ yêu cầu lập biên bản đúng quy trình. Chính sự lạnh lùng ấy làm Duy An yên tâm. Cô không cứu anh bằng cảm tình, mà bằng cách buộc tất cả phải đi đúng luật.",
                "Trong lúc kiểm tra, một hũ men lạ được phát hiện sau bếp. Duy An khựng lại. Hũ ấy không phải của anh. Mùi hóa chất xộc lên sắc hơn men tro thường, đủ để người thợ lâu năm nhăn mặt. Ai đó đã đưa nó vào nhà anh trong đêm.",
                "Thay vì hoảng, Duy An yêu cầu lấy dấu vân tay trên nắp hũ và kiểm camera nhà hàng xóm. Bà cụ bán nước đầu ngõ kể rằng tối qua có chiếc xe tải nhỏ ghé qua, người xuống xe mặc áo khoác của xưởng Gia Khiêm. Lời kể được ghi vào biên bản.",
                "Tin đồn khiến lò nhà Duy An bị tạm dừng một ngày. Không được nung, anh chuyển sang mài lại khuôn, rửa từng tấm vải lọc tro. Mỗi động tác chậm và chắc như một lời phản kháng. Người ta có thể niêm phong lò, nhưng không thể niêm phong trí nhớ của bàn tay.",
                "Đêm đó, Mỹ Hân tìm đến. Cô đứng ngoài cổng, hỏi anh có thể nhận tiền rời khỏi Bát Tràng không. Duy An nhìn cô qua lớp song sắt cũ, hỏi lại: \"Em bán công thức rồi, giờ muốn mua luôn quê hương của anh à?\" Mỹ Hân cúi mặt, không đáp.",
                "Khi cô bỏ đi, Duy An nhận kết quả sơ bộ từ phòng thí nghiệm: mẫu men trong hũ lạ có chất tạo bóng công nghiệp, không trùng với bất kỳ mẻ nào trong sổ lò của anh. Một mảnh bùn đầu tiên đã rơi khỏi mặt kẻ vu oan.",
            ],
        ),
        build_chapter(
            "Chương 4: Sổ Lò Ba Đời Và Màu Men Không Sao Chép Được",
            [
                "Duy An đem sổ lò tới buổi đối chứng tại nhà văn hóa làng. Không khí căng như dây đàn. Một bên là Gia Khiêm với luật sư và máy chiếu, một bên là Duy An với chiếc hòm gỗ cũ buộc dây thừng. Nhiều người nhìn chiếc hòm ấy bằng ánh mắt thương hại.",
                "Nhưng khi hòm mở ra, mùi giấy cũ và tro khô lan ra cả bàn. Trong sổ có dấu tay của ông nội anh, có mẫu men dán cạnh từng ghi chú, có cả những dòng sửa sai sau mỗi mẻ hỏng. Đó không phải tài liệu làm trong một đêm, mà là đời sống của ba thế hệ.",
                "Gia Khiêm bảo sổ cũ không có giá trị thương mại. Hoài Phương lập tức đặt lên bàn bản chụp công chứng từ năm trước, thời điểm Duy An từng mang sổ đi xin hỗ trợ bảo tồn làng nghề. Ngày tháng trên đó sớm hơn mọi đăng ký của Mỹ Hân.",
                "Chuyên gia Nhật yêu cầu thử lại một mẻ nhỏ trước mặt mọi người. Duy An đồng ý. Anh không dùng máy đo hiện đại trước, mà dùng cách ông nội dạy: nhìn màu lửa ở miệng lò, nghe tiếng đất co lại, ngửi mùi tro khi nhiệt bắt đầu xuống.",
                "Đám đông ban đầu cười khẽ. Nhưng khi chiếc chén thử ra lò, mặt men hiện vân rạn mảnh như sương. Ánh xanh chìm dưới lớp tro, không bóng lộ, không rộp đáy. Một cụ già trong làng cầm chén lên, mắt đỏ hoe: \"Đúng màu lò cụ Phạm ngày trước.\"",
                "Mỹ Hân đứng chết lặng. Cô từng học thuộc công thức, nhưng chưa bao giờ hiểu vì sao phải đợi thêm bảy phút trước khi mở cửa lò. Cô có thể chép tỷ lệ, không thể chép sự nhẫn nại mà Duy An đổi bằng mười năm bỏng tay.",
                "Gia Khiêm cố gọi đó là màn diễn. Nhưng bảng nhiệt do thợ trẻ gửi được chiếu lên. Nó chứng minh xưởng của hắn đã hạ lò sai quy trình để chạy tiến độ, rồi đổ lỗi cho công thức. Mồ hôi chảy từ thái dương hắn xuống cổ áo.",
                "Cuối buổi, Hoài Phương tuyên bố tạm loại xưởng Gia Khiêm khỏi vòng cung ứng. Đơn hàng chưa trao cho Duy An ngay; cô yêu cầu anh lập cơ sở kiểm soát chất lượng riêng. Duy An gật đầu. Anh không cần thắng bằng thương hại. Anh cần thắng bằng mẻ gốm đủ sạch.",
            ],
        ),
        build_chapter(
            "Chương 5: Mỹ Hân Ký Tên Vào Biên Bản Giả",
            [
                "Khi mọi người tưởng Gia Khiêm đã hết đường, hắn tung ra một biên bản mới, ghi rằng Duy An từng tự nguyện chuyển giao công thức cho Mỹ Hân. Biên bản có chữ ký của cô, có dấu xưởng, có cả ảnh chụp ngày hai người còn yêu nhau đứng trước lò.",
                "Mỹ Hân xuất hiện trong buổi làm việc với gương mặt trang điểm kỹ. Cô nói rất nhỏ rằng ngày đó Duy An đồng ý để cô phát triển công thức vì anh không đủ năng lực kinh doanh. Câu nói ấy đâm vào lòng anh không kém ngày bị đuổi khỏi xưởng.",
                "Duy An không cãi ngay. Anh lấy ra tờ giấy than lót dưới bản nháp năm ấy. Trên giấy còn hằn dòng chữ khác: Mỹ Hân từng ghi công thức chỉ để xin tài trợ bảo tồn, không phải chuyển nhượng. Sự khác biệt nằm ở một cụm từ bị cắt khỏi bản chính.",
                "Luật sư của Gia Khiêm nói giấy than không đủ. Duy An gật đầu, rồi mở file ghi âm từ chiếc điện thoại cũ của ông nội. Trong đó, giọng Mỹ Hân năm trước còn trong trẻo, nói rằng công thức là của nhà họ Phạm, cô chỉ giúp đánh máy hồ sơ.",
                "Mỹ Hân tái mặt. Chiếc bút trong tay cô rơi xuống bàn, lăn một vòng rồi dừng cạnh mép. Cô cúi nhặt nhưng ngón tay run đến mức không kẹp nổi. Gia Khiêm nhìn cô bằng ánh mắt cảnh cáo, nhưng ánh mắt ấy chỉ làm cô run hơn.",
                "Hoài Phương yêu cầu đối chiếu chữ ký trên biên bản giả với nét ký thật trong hồ sơ ngân hàng của Mỹ Hân. Kết quả sơ bộ cho thấy phần ngày tháng được thêm sau bằng loại mực khác. Một chuyên viên giám định dùng đèn chiếu làm vết mực hiện rõ như vết bẩn trên áo trắng.",
                "Duy An nhìn Mỹ Hân. Anh không hỏi vì sao nữa. Câu hỏi ấy đã vô nghĩa. Người từng bước qua anh trong xưởng hôm nay tự bước vào biên bản giả của chính mình. Cô khóc, nhưng nước mắt đến sau con dấu thì không rửa được gì.",
                "Gia Khiêm nổi giận, đập bàn định rời đi. Nhưng bên ngoài, hai cán bộ kinh tế đã chờ để mời hắn làm việc về hành vi làm giả hồ sơ thương mại. Lần đầu tiên, hắn nhìn cánh cửa xưởng như nhìn miệng lò đang khép lại.",
            ],
        ),
        build_chapter(
            "Chương 6: Đơn Hàng Nhật Chuyển Về Căn Lò Cũ",
            [
                "Hoài Phương không ký hợp đồng ngay tại buổi thắng lợi. Cô đến căn lò cũ của Duy An lần nữa, lần này mang theo bảng yêu cầu chất lượng dày mười hai trang. Mỗi dòng là một tiêu chuẩn: độ hút nước, độ bền men, độ an toàn khi dùng với thực phẩm nóng.",
                "Duy An đọc hết, không phàn nàn. Anh biết nghề truyền thống muốn sống không thể chỉ dựa vào cảm xúc làng nghề. Men cổ phải đi cùng kiểm nghiệm hiện đại, sổ lò phải đi cùng quản trị kho, và lòng tự trọng phải đi cùng hóa đơn đúng hạn.",
                "Anh tập hợp những thợ trẻ từng cúi đầu ở xưởng Gia Khiêm. Không ai được nhận vào chỉ vì thương hại. Mỗi người phải làm lại một bài thử: lọc tro, canh nhiệt, ghi nhật ký mẻ. Người làm sai được sửa, người gian dối thì rời đi.",
                "Mẻ đầu tiên cho khách Nhật được nung trong đêm mưa. Duy An đứng cạnh lò, Hoài Phương ngồi ở ghế gỗ gần cửa, đọc báo cáo kiểm định. Không ai nói chuyện tình cảm, nhưng giữa họ có một sự tôn trọng lặng lẽ, bền hơn lời hứa vội.",
                "Khi cửa lò mở, hơi nóng tràn ra như sóng. Những chiếc chén xếp thành hàng, màu men xanh chìm, vân rạn đều, đáy không rộp. Chuyên gia Nhật cầm một chiếc lên, gõ nhẹ. Âm thanh trong và dài. Ông mỉm cười lần đầu tiên.",
                "Hợp đồng 180 tỷ được ký tại nhà văn hóa làng, không phải khách sạn sang. Duy An yêu cầu ghi rõ tên đội thợ và nguồn gốc công thức trong phụ lục. Anh đã từng bị xóa tên, nên không cho phép bất kỳ bàn tay nào phía sau lò bị biến thành bóng.",
                "Gia Khiêm và Mỹ Hân bị điều tra thêm. Tin cuối cùng Duy An nghe được là xưởng của hắn bị đình chỉ xuất khẩu. Anh không mở tiệc lớn. Anh chỉ đem một chiếc chén hoàn chỉnh đặt lên bàn thờ ông nội, rót trà nóng vào trong đó.",
                "Mặt men chuyển màu dưới hơi nước. Duy An cúi đầu rất lâu. Có những chiến thắng không cần tiếng vỗ tay; chỉ cần người đã khuất biết rằng màu men nhà mình cuối cùng cũng trở về đúng tên.",
            ],
        ),
        build_chapter(
            "Chương 7: Tro Rơm, Nước Giếng Và Lời Xin Lỗi Muộn",
            [
                "Sau hợp đồng đầu tiên, Duy An không vội mở rộng. Anh đi từng nhà trong làng xin mua tro rơm sạch, ghi rõ ruộng nào, mùa nào, ngày đốt nào. Người trẻ trong xưởng ban đầu thấy phiền, nhưng anh bắt họ hiểu rằng bản sắc không phải khẩu hiệu; nó nằm trong từng bao tro có nguồn gốc rõ ràng.",
                "Mỹ Hân gửi thư xin lỗi. Lá thư dài ba trang, nhắc lại những ngày cũ và nói cô bị Gia Khiêm ép. Duy An đọc xong, gấp lại, đưa cho luật sư lưu cùng hồ sơ. Anh không xé, cũng không trả lời. Có những lời xin lỗi chỉ nên tồn tại như chứng cứ của một thời người ta đã chọn sai.",
                "Hoài Phương hỏi anh có thấy quá lạnh không. Duy An đang rửa tay bên chum nước giếng, đáp rằng anh từng mềm lòng đủ lâu để bị người khác mang công thức đi đăng ký. Từ nay anh vẫn tử tế, nhưng không tử tế đến mức tự tháo khóa cửa nhà mình.",
                "Một nhóm du khách Nhật ghé thăm lò mới. Họ không chỉ mua chén, mà muốn xem cách người thợ ghi nhật ký nhiệt. Duy An để thợ trẻ thuyết minh. Anh đứng phía sau, nghe các em nói sai vài chỗ rồi sửa nhẹ. Một nghề sống được là khi nó có người sau đủ tự tin nói thay người trước.",
                "Buổi tối, làng nghề tổ chức họp lại quy chế dùng tên men cổ. Lần đầu tiên sau nhiều năm, người ta bàn về quyền sở hữu tri thức của thợ thủ công chứ không chỉ giá bán. Duy An được mời lên phát biểu, nhưng anh chỉ nói ngắn: \"Đừng để người làm nghề phải thắng kiện mới được gọi đúng tên.\"",
                "Ở cuối phòng, một số người từng im lặng hôm anh bị đuổi cúi đầu. Duy An không bắt họ xin lỗi. Anh yêu cầu họ ký vào quy chế mới. Sự hối hận nếu không biến thành hành động thì chỉ là một kiểu trang trí cảm xúc.",
                "Đêm ấy, Hoài Phương đem đến bản kế hoạch xây phòng trưng bày men cổ. Cô không nói đầu tư vì thích anh, mà vì câu chuyện này có khả năng trở thành thương hiệu dài hạn. Duy An nghe xong, bật cười. Anh thích sự thẳng thắn ấy hơn mọi lời ngọt.",
                "Chương mới của lò Phạm bắt đầu bằng một bảng treo trước cửa: mọi công thức có chủ, mọi người thợ có tên. Duy An nhìn tấm bảng, thấy vết sẹo trên mu bàn tay đã nhạt. Nhưng anh biết mình sẽ giữ nó như giữ một đường rạn đẹp trên mặt men.",
            ],
        ),
        build_chapter(
            "Chương 8: Buổi Triển Lãm Không Có Tên Kẻ Trộm",
            [
                "Triển lãm đầu tiên của lò Phạm diễn ra trong một căn nhà cổ ở Bát Tràng. Không có ảnh Gia Khiêm, không có câu chuyện giật gân về phản bội. Duy An chỉ trưng bày sổ lò, mảnh xương men, chén thử hỏng và những chiếc bình đã qua kiểm định.",
                "Hoài Phương đề nghị đặt phần hồ sơ pháp lý ở góc riêng để khách hiểu giá trị của bản quyền thủ công. Duy An đồng ý. Anh muốn người mua biết một món gốm đẹp không chỉ đến từ lửa, mà còn từ việc người làm ra nó được bảo vệ khỏi lòng tham.",
                "Một phóng viên hỏi vì sao anh không nhắc tên kẻ đã cướp công. Duy An nhìn dãy bình dưới ánh vàng, nói rằng người trộm nghề không xứng đứng chung phòng với nghề. Câu trả lời ấy được chia sẻ nhiều hơn mọi lời mắng chửi.",
                "Mỹ Hân đứng ngoài cổng triển lãm một lúc rồi rời đi. Không ai đuổi cô, cũng không ai mời vào. Cánh cửa mở, nhưng danh dự không phải thứ cứ bước qua là lấy lại được. Duy An nhìn thấy bóng cô qua kính, rồi quay sang hướng dẫn một em nhỏ cách nghe tiếng gốm.",
                "Đơn hàng thứ hai đến từ một chuỗi ryokan Nhật. Họ không đòi giảm giá, chỉ yêu cầu giữ được câu chuyện nguồn gốc. Duy An đưa hợp đồng cho đội pháp lý kiểm trước, không còn ký vì xúc động. Anh đã học rằng một chữ ký sạch có thể bảo vệ cả đời làm nghề.",
                "Tối muộn, anh và Hoài Phương ngồi bên bờ sông. Cô hỏi nếu không có vụ bị đuổi, anh có dám đưa men cổ ra thị trường lớn không. Duy An nghĩ rất lâu rồi lắc đầu. Có lẽ anh cần bị đẩy khỏi chiếc lò quen thuộc để biết mình có thể xây một lò rộng hơn.",
                "Hoài Phương đưa anh một mảnh gốm nhỏ được mài thành mặt dây. Đó không phải vật đính ước lãng mạn, chỉ là mảnh chén vỡ ngày đầu được giữ lại. Duy An nhận lấy, thấy cạnh sắc đã được mài tròn. Có những đau đớn nếu không vứt đi sẽ trở thành kỷ vật.",
                "Khi triển lãm khép lại, tấm biển lò Phạm sáng lên dưới đèn vàng. Không có tiếng reo hò, nhưng có dòng người xếp hàng đặt trước. Duy An đứng trong mùi đất ẩm và tro rơm, biết lần này tên mình không còn nằm ở mép giấy bị ai gạch bỏ.",
            ],
        ),
    ]
    story = {
        "title": title,
        "author": "Minh Hạ",
        "genre": "Sảng Văn",
        "intro": intro,
        "cover_prompt": "Square 1:1 photorealistic Vietnamese web novel cover, cinematic Bát Tràng pottery kiln at night, a wounded Vietnamese ceramic master holding an ancestral glaze notebook and a glowing blue-green ceramic bowl, warm firelight, old brick kiln, no text, no watermark, top dark space for title.",
        "chapters": chapters,
        "meta": {"slug": "duoi-khoi-xuong-gom-bat-trang", "publication_status": "draft_pending_user_review", "rewrite_note": "Batch 1 unique rewrite"},
    }
    story = deepen_chapters(
        story,
        {
            "lead": "Duy An",
            "ally": "Hoài Phương",
            "villain": "Gia Khiêm",
            "craft": "nghề men tro Bát Tràng",
            "object_a": "mảnh xương men và sổ lò ba đời",
            "object_b": "mẫu men bị tráo",
            "place": "căn lò cũ bên bờ sông Hồng",
            "stakes": "đơn hàng Nhật và danh dự của cả một dòng thợ",
            "sensory": "mùi tro rơm ẩm lẫn hơi nóng từ miệng lò",
        },
    )
    for chapter in story["chapters"]:
        chapter_title = chapter["title"].split(":", 1)[-1].strip()
        chapter["content"] = chapter["content"].rstrip() + "\n" + p(
            f"Riêng với mốc \"{chapter_title}\", mỗi quyết định của Duy An còn kéo theo ánh mắt của cả làng nghề. Nếu anh làm ẩu ở đúng điểm này, người ta sẽ nói men cổ chỉ là chiêu bán hàng. Nếu anh làm đúng, những người thợ từng bị ép đứng sau tên chủ xưởng sẽ có thêm một lý do để giữ nghề. Nghĩ tới đó, anh lại cúi xuống kiểm thêm một dòng ghi chú, thêm một mẫu tro, thêm một vết rạn nhỏ trên mặt chén."
        )
    return story


def rewrite_story_03() -> dict:
    title = "Bị Vu Oan Làm Chết Bệnh Nhân, Tôi Cứu Sống Chủ Tịch Khiến Cả Bệnh Viện Chợ Rẫy Câm Lặng"
    lead = "Trương Hải Nam"
    ally = "Hoàng Thanh Vân"
    villain = "Lưu Đức Thịnh"
    ex = "Đặng Quỳnh Chi"
    intro = "".join(
        p(x)
        for x in [
            f"\"Một y sĩ đông y không bằng cấp chuyên khoa như anh mà dám chạm vào bệnh nhân cấp cứu?\" {villain} quát giữa hành lang Chợ Rẫy, trước khi đổ toàn bộ trách nhiệm ca tử vong lên {lead}.",
            f"{ex}, người từng cùng anh mở phòng châm cứu phục hồi, ký vào bản tường trình bất lợi. Cô nói anh tự ý dùng kim, tự ý can thiệp, tự ý phá quy trình.",
            f"Nhưng camera phòng trực, bảng điện tâm đồ, chỉ số men gan và thời điểm dùng thuốc lại kể một câu chuyện khác. Hải Nam không cần phép màu. Anh cần hội đồng chuyên môn đọc đúng từng phút sinh tồn.",
            "Khi chủ tịch một tập đoàn bất ngờ ngưng tim trong khu VIP, người bị đình chỉ phải đứng trước lựa chọn: quay lưng để tự cứu mình, hay cứu người thêm một lần và buộc cả bệnh viện nhìn lại.",
        ]
    )
    specs = [
        ("Chương 1: Hành Lang Cấp Cứu Và Bản Tường Trình Giả", "hành lang cấp cứu", "bản tường trình", "camera phòng trực", "ca tử vong bị quy chụp"),
        ("Chương 2: Điện Tâm Đồ Không Biết Nói Dối", "phòng hồ sơ bệnh án", "dải điện tâm đồ", "mốc thời gian dùng thuốc", "sai lệch bảy phút"),
        ("Chương 3: Phòng Khám Bị Dán Niêm Phong", "phòng khám nhỏ ở quận 5", "hộp kim bạc", "sổ vô khuẩn", "đình chỉ 48 giờ"),
        ("Chương 4: Chủ Tịch Ngưng Tim Trong Khu VIP", "khu VIP Chợ Rẫy", "máy monitor", "biên bản cấp cứu", "cơn rung thất đột ngột"),
        ("Chương 5: Mười Hai Cây Kim Và Xe Đẩy Hồi Sức", "phòng hồi sức", "kim châm cứu", "xét nghiệm khí máu", "ranh giới giữa giữ mạng và điều trị"),
        ("Chương 6: Hội Đồng Chuyên Môn Mở Camera", "phòng họp hội đồng", "camera góc khuất", "log thuốc", "người đổi lệnh thuốc"),
        ("Chương 7: Quỳnh Chi Đối Chất Trước Hồ Sơ Men Gan", "phòng đối chất", "bảng men gan", "tin nhắn cũ", "chữ ký bị ép"),
        ("Chương 8: Bác Sĩ Thịnh Run Tay Khi Đọc Kết Quả", "phòng xét nghiệm", "phiếu xét nghiệm", "mẫu máu lưu", "chỉ số không khớp"),
        ("Chương 9: Trung Tâm Phục Hồi Không Dành Cho Người Nói Dối", "khu phục hồi mới", "đề án liên viện", "hợp đồng 260 tỷ", "lời mời hợp tác"),
        ("Chương 10: Người Được Cứu Tự Đứng Lên Làm Chứng", "buổi họp báo bệnh viện", "hồ sơ xuất viện", "lời chứng của chủ tịch", "cái cúi đầu muộn"),
    ]
    chapters = []
    for idx, (ctitle, setting, object_line, proof, conflict) in enumerate(specs, 1):
        chapters.append(
            build_chapter(
                ctitle,
                [
                    f"{setting.capitalize()} nồng mùi sát khuẩn và mồ hôi người chờ cấp cứu. {lead} đứng ở mép cửa, nghe tên mình bị đọc lên trong {object_line} như một tội danh đã đóng dấu sẵn.",
                    f"{villain} không nói về bệnh nhân, hắn nói về cấp bậc. Hắn nhấn mạnh áo blouse của mình, chức danh của mình, hội đồng của mình, rồi chỉ vào {lead} như chỉ một vật thừa cần loại bỏ khỏi bệnh viện.",
                    f"{ally} xuất hiện không phải để bênh anh. Cô là người quản lý pháp chế của gia đình bệnh nhân, cầm bút ghi từng câu, yêu cầu cung cấp {proof}. Cách cô hỏi lạnh đến mức cả hai bên đều không thể diễn cảm xúc thay cho dữ liệu.",
                    f"{conflict.capitalize()} là điểm khiến mọi thứ lệch khỏi câu chuyện mà {villain} dựng sẵn. Khi dải số liệu được đặt cạnh lời khai, có một khoảng trống không ai giải thích được bằng sự cẩu thả của {lead}.",
                    f"{ex} cố giữ vẻ bình tĩnh. Nhưng mỗi lần nghe nhắc tới giờ dùng thuốc, cô lại liếc sang {villain}. Hải Nam nhìn thấy. Anh từng yêu ánh mắt ấy khi nó tin anh; hôm nay anh chỉ thấy nó đang tìm chỗ trốn.",
                    f"Anh không nhận mình là thần y. Anh giải thích rõ châm cứu trong ca cấp cứu chỉ nhằm giữ nhịp sinh tồn, giảm co thắt, chờ máy móc và bác sĩ hồi sức làm phần việc chính. Chính sự khiêm tốn chuyên môn ấy khiến lời cáo buộc 'mê tín cứu người' bắt đầu lỏng ra.",
                    f"Một điều dưỡng trẻ lén đưa thêm bảng bàn giao ca. Cô khóc vì sợ mất việc, nhưng vẫn chỉ ra chữ ký bị thêm sau. {ally} không ôm cô an ủi; cô gọi người chứng kiến, lập biên bản, bảo vệ cô bằng thủ tục.",
                    f"{villain} càng nói càng rối. Mạch máu ở cổ hắn nổi lên, tay cầm bút gõ liên tục xuống mặt bàn. Khi bị yêu cầu đọc lại mốc thời gian, hắn bỏ sót đúng bảy phút quan trọng. Căn phòng im phăng phắc.",
                    f"Đêm đó, {lead} trở về phòng khám bị khóa niêm phong. Anh đứng ngoài cửa sắt, nhìn bảng hiệu cũ trong ánh đèn đường. Anh không đau vì mất chỗ làm, mà đau vì người ta dùng danh nghĩa chuyên môn để che một lỗi có thể giết người.",
                    f"Cuối chương {idx}, {ally} gửi cho anh bản sao hồ sơ mới. Dòng cuối cùng được khoanh đỏ: nếu chứng minh được {proof} bị sửa, vụ này không còn là tai biến chuyên môn mà là che giấu sai phạm y khoa.",
                ],
            )
        )
    story = {
        "title": title,
        "author": "Bạch Dương",
        "genre": "Sảng Văn",
        "intro": intro,
        "cover_prompt": "Square 1:1 photorealistic Vietnamese medical revenge drama cover, Chợ Rẫy hospital corridor, calm emergency physician holding ECG strips and lab results, monitors glowing, senior doctor shocked, no text, no watermark, dark top area.",
        "chapters": chapters,
        "meta": {"slug": "vu-oan-o-benh-vien-cho-ray", "publication_status": "draft_pending_user_review", "rewrite_note": "Batch 1 unique rewrite"},
    }
    return deepen_chapters(
        story,
        {
            "lead": lead,
            "ally": ally,
            "villain": villain,
            "craft": "quy trình cấp cứu và phục hồi lâm sàng",
            "object_a": "dải điện tâm đồ cùng bảng xét nghiệm men gan",
            "object_b": "bản tường trình bị sửa mốc giờ",
            "place": "hành lang Chợ Rẫy nồng mùi sát khuẩn",
            "stakes": "sinh mạng bệnh nhân và giấy phép phòng khám",
            "sensory": "tiếng monitor tít đều sau một nhịp tim từng suýt tắt",
        },
    )


def rewrite_story_04() -> dict:
    title = "Bị Sếp Cũ Vứt Hợp Đồng Ở Cầu Giấy, Tôi Lật Nhật Ký Thi Công Khiến Tập Đoàn Mất Gói Thầu"
    lead = "Lê Minh Đức"
    ally = "Trần Bảo Ngọc"
    villain = "Đỗ Hoàng Phúc"
    ex = "Phan Yến Nhi"
    intro = "".join(
        p(x)
        for x in [
            f"Giữa văn phòng ở Duy Tân, {villain} ném tập hợp đồng xuống chân {lead} và nói một kỹ sư hiện trường không có quyền ngồi vào bàn đấu thầu.",
            f"{ex} công khai đứng về phía tập đoàn, ký xác nhận rằng toàn bộ nhật ký thi công do phòng dự án lập, còn Minh Đức chỉ là người giám sát phụ.",
            "Nhưng dưới lớp bụi công trường là mẫu bê tông lưu kho, phiếu đổ trạm trộn, nhật ký mưa bão và định vị xe bồn. Những thứ khô khan ấy mới là drama thật của ngành xây dựng.",
            "Khi gói thầu cầu vượt 540 tỷ bị treo vì nghi vấn gian lận vật liệu, người bị vứt hợp đồng phải biến từng bao xi măng, từng lõi khoan thành bằng chứng vả mặt.",
        ]
    )
    specs = [
        ("Chương 1: Tập Hợp Đồng Bị Vứt Dưới Chân", "văn phòng Duy Tân", "hợp đồng phụ lục", "dấu bùn trên ủng", "bị xóa tên khỏi hồ sơ thầu"),
        ("Chương 2: Mẫu Bê Tông Trong Kho Lạnh", "kho mẫu Cầu Giấy", "lõi bê tông", "mã trạm trộn", "mẫu bị tráo nhãn"),
        ("Chương 3: Đêm Mưa Và Nhật Ký Đổ Bê Tông", "công trường mưa bão", "nhật ký thi công", "camera cẩu tháp", "ca đổ sai giờ"),
        ("Chương 4: Tổ Giám Sát Bị Rút Giấy Phép", "Sở Xây dựng", "biên bản tạm đình chỉ", "chữ ký giám sát", "đội thi công bị treo"),
        ("Chương 5: Xe Bồn Đi Sai Tuyến", "trạm trộn ngoại thành", "dữ liệu GPS", "phiếu cân xe", "đường vòng bất thường"),
        ("Chương 6: Buổi Mở Thầu Im Như Đổ Bê Tông Lỗi", "Trung tâm Đấu thầu", "hồ sơ kỹ thuật", "mẫu thí nghiệm độc lập", "đối thủ bị hỏi dồn"),
        ("Chương 7: Yến Nhi Ký Vào Trang Không Đọc", "phòng pháp chế", "phụ lục trách nhiệm", "email chuyển tiếp", "lời khai phản chủ"),
        ("Chương 8: Lõi Khoan Nói Thay Người Kỹ Sư", "phòng thí nghiệm vật liệu", "mũi khoan lõi", "cường độ nén", "bê tông không đạt mác"),
        ("Chương 9: Gói Thầu 540 Tỷ Đổi Hướng", "hội đồng chủ đầu tư", "bảng chấm kỹ thuật", "biên bản loại thầu", "cú rút hồ sơ phút cuối"),
        ("Chương 10: Cây Cầu Được Đứng Tên Những Người Không Bỏ Chạy", "mặt bằng cầu vượt", "bản vẽ hoàn công", "danh sách kỹ sư", "khởi công sạch"),
    ]
    chapters = []
    for idx, (ctitle, setting, object_line, proof, conflict) in enumerate(specs, 1):
        chapters.append(
            build_chapter(
                ctitle,
                [
                    f"{setting.capitalize()} không có ánh đèn hào môn, chỉ có mùi hồ sơ ẩm và tiếng máy in chạy liên tục. {lead} đặt {object_line} lên bàn, trên tay vẫn còn vết xước từ công trường.",
                    f"{villain} coi thường mọi thứ không bóng bẩy. Hắn nói nhà thầu thắng bằng quan hệ, không bằng người đứng giữa mưa ghi từng khối bê tông. Câu ấy làm vài kỹ sư trẻ cúi mặt, vì họ biết nó đúng với cách hắn vận hành.",
                    f"{ally}, chuyên viên pháp lý của chủ đầu tư, không bị ấn tượng bởi lời tố cáo hay vẻ mệt mỏi của {lead}. Cô yêu cầu đối chiếu {proof}, phiếu giao nhận và người ký từng ca. Ngành xây dựng không tin nước mắt; nó tin mẫu thử còn nguyên niêm phong.",
                    f"{conflict.capitalize()} là điểm làm hồ sơ của {villain} bắt đầu nứt. Một con số lệch có thể bị giải thích là lỗi đánh máy, nhưng ba con số lệch cùng hướng là dấu vết của bàn tay cố ý.",
                    f"{ex} bước vào với tư cách nhân sự dự án, nói rằng {lead} tự ý giữ hồ sơ để gây áp lực. Minh Đức nhìn cô, nhớ những đêm cô từng nhờ anh chỉ cách đọc bản vẽ. Bây giờ cô dùng chính sự tin tưởng ấy làm dao.",
                    f"Anh không tranh luận về tình cảm. Anh mở laptop, chiếu dữ liệu trạm trộn và ảnh hiện trường. Những bức ảnh không đẹp: bùn bắn lên cột thép, áo phản quang ướt sũng, đồng hồ chỉ 2 giờ 17 phút sáng. Nhưng chúng thật.",
                    f"Một công nhân già đứng lên làm chứng. Ông nói đêm đó xe bồn tới muộn, bê tông bắt đầu đông khi còn chưa bơm hết. Ông từng im vì sợ mất việc, nhưng sau khi thấy Minh Đức bị đổ tội, ông mang cuốn sổ tay công trường đến.",
                    f"{villain} cố cười nhạo cuốn sổ tay lem bùn. Nhưng khi mã xe trong sổ khớp với dữ liệu GPS, nụ cười của hắn cứng lại. Hắn lau tay vào quần, động tác nhỏ nhưng lộ sự bồn chồn.",
                    f"Trần Bảo Ngọc yêu cầu lập hồ sơ chuyển kiểm định độc lập. Cô không hứa bảo vệ {lead}; cô hứa bảo vệ quy trình. Với Minh Đức lúc ấy, đó là lời hứa đáng giá hơn bất kỳ câu an ủi nào.",
                    f"Cuối chương {idx}, một lõi bê tông được lấy ra trước mặt các bên. Bề mặt cắt hiện những lỗ rỗng li ti. {lead} nhìn nó như nhìn vết thương của cây cầu chưa thành hình, biết rằng ngày mai sẽ có người không ngủ được.",
                ],
            )
        )
    story = {
        "title": title,
        "author": "Khánh Linh",
        "genre": "Sảng Văn",
        "intro": intro,
        "cover_prompt": "Square 1:1 photorealistic Vietnamese construction revenge cover, rain-soaked Hanoi construction site, civil engineer holding concrete core samples and muddy construction logs, bridge model behind, no text, no watermark, dark top area.",
        "chapters": chapters,
        "meta": {"slug": "vut-hop-dong-cau-giay", "publication_status": "draft_pending_user_review", "rewrite_note": "Batch 1 unique rewrite"},
    }
    return deepen_chapters(
        story,
        {
            "lead": lead,
            "ally": ally,
            "villain": villain,
            "craft": "đấu thầu xây dựng và kiểm định vật liệu",
            "object_a": "lõi bê tông khoan mẫu",
            "object_b": "nhật ký đổ bê tông trong đêm mưa",
            "place": "công trường Cầu Giấy còn mùi bùn và dầu máy",
            "stakes": "gói thầu cầu vượt 540 tỷ và an toàn của người đi đường",
            "sensory": "tiếng máy khoan lõi rít vào bê tông nghe buốt tận răng",
        },
    )


def rewrite_story_05() -> dict:
    title = "Bị Nhà Vợ Khinh Ở Đồi Chè Cầu Đất, Tôi Mua Lại Nhà Máy Khiến Họ Xin Đứng Tên Thuê"
    lead = "Võ Gia Huy"
    ally = "Lâm Hạ Vy"
    villain = "Lâm Quốc Tuấn"
    ex = "Lâm Nhã Uyên"
    intro = "".join(
        p(x)
        for x in [
            f"Giữa đồi chè Cầu Đất, {villain} bắt {lead} đứng ngoài hiên trong mưa lạnh và gọi anh là thằng ở rể chỉ biết hái lá.",
            f"{ex} ký giấy hủy hôn ngay trước mặt cả họ Lâm, nói anh không có cổ phần, không có nhà, càng không có tư cách bàn chuyện nhà máy trà.",
            "Nhưng Gia Huy giữ hợp đồng vùng nguyên liệu sạch, kết quả kiểm nghiệm dư lượng và quyền thuê khu đất mà nhà họ Lâm tưởng đã ép được anh nhường.",
            "Khi nhà máy bị cắt nguồn thu mua, khách Đài Loan hủy lịch và kho trà lên men đứng trước nguy cơ hỏng, người bị khinh nhất trở thành người duy nhất có chìa khóa cứu cả vùng chè.",
        ]
    )
    specs = [
        ("Chương 1: Bữa Cơm Nhà Vợ Và Chén Trà Đổ Xuống Áo", "nhà gỗ trên đồi Cầu Đất", "chén trà ô long", "giấy hủy hôn", "bị đuổi khỏi nhà vợ"),
        ("Chương 2: Hợp Đồng Vùng Nguyên Liệu Không Nằm Trong Két Họ Lâm", "nhà kho chè", "hợp đồng nông hộ", "sổ cân lá tươi", "quyền thu mua bị hiểu sai"),
        ("Chương 3: Kho Trà Lên Men Mất Điện", "kho ủ trà", "máy đo ẩm", "camera kho", "mẻ trà suýt hỏng"),
        ("Chương 4: Khách Đài Loan Ngửi Thấy Mùi Thuốc Cỏ", "phòng thử trà", "mẫu lá", "kết quả dư lượng", "lô hàng bị nghi nhiễm hóa chất"),
        ("Chương 5: Hạ Vy Tự Đi Gặp Từng Nông Hộ", "sườn đồi mù sương", "sổ tay nông hộ", "biên nhận phân hữu cơ", "lời khai của người trồng"),
        ("Chương 6: Quốc Tuấn Bị Chặn Ở Cổng Nhà Máy", "cổng nhà máy trà", "biên bản bảo vệ", "hợp đồng thuê đất", "quyền vận hành đổi chủ"),
        ("Chương 7: Nhã Uyên Xin Đứng Tên Lại Khi Quá Muộn", "quán trà kính nhìn xuống thung lũng", "đơn xin hợp tác", "tin nhắn hủy hôn", "lời xin lỗi tính toán"),
        ("Chương 8: Phiên Đấu Giá Nhà Máy Trong Sương", "hội trường Đà Lạt", "hồ sơ mua lại", "bảo lãnh ngân hàng", "gia tộc họ Lâm mất quyền kiểm soát"),
        ("Chương 9: Mẻ Trà Đầu Tiên Mang Tên Người Trồng", "xưởng sao trà mới", "tem truy xuất", "danh sách nông hộ", "thương hiệu sạch ra mắt"),
        ("Chương 10: Đồi Chè Không Còn Là Của Những Người Khinh Rẻ", "đỉnh đồi Cầu Đất", "bản quy hoạch du lịch trà", "hợp đồng chuỗi 210 tỷ", "lời hứa với người lao động"),
        ("Chương 11: Hơi Trà Nóng Và Cái Cúi Đầu Của Nhà Họ Lâm", "phòng thưởng trà", "ấm trà cuối vụ", "biên bản bàn giao", "kết thúc hôn ước cũ"),
    ]
    chapters = []
    for idx, (ctitle, setting, object_line, proof, conflict) in enumerate(specs, 1):
        chapters.append(
            build_chapter(
                ctitle,
                [
                    f"{setting.capitalize()} phủ một lớp lạnh rất riêng của Đà Lạt. {lead} đứng giữa mùi lá chè non, tay cầm {object_line}, nghe những người từng gọi anh là người nhà nay bàn cách đẩy anh khỏi mọi giấy tờ.",
                    f"{villain} không mắng bằng tiếng lớn ngay từ đầu. Ông ta rót trà, để hơi nóng bốc lên, rồi nói từng chữ rằng một người không có họ Lâm thì không được chạm vào nhà máy của họ Lâm. Cách khinh rẻ ấy lịch sự đến mức còn đau hơn một cái tát.",
                    f"{ex} đặt {proof} lên bàn nhưng chỉ đọc phần có lợi cho gia đình. Cô bỏ qua phụ lục nông hộ, bỏ qua cam kết canh tác sạch, bỏ qua những đêm Gia Huy cùng người trồng chè che bạt qua mưa đá.",
                    f"{ally} không phải kiểu nữ chính xuất hiện cứu người vì cảm động. Cô tự lái xe xuống từng vườn, hỏi từng hộ về phân bón, ngày hái, giá cân. Cô nói nếu Gia Huy nói dối, cô sẽ là người đầu tiên loại anh khỏi thương vụ.",
                    f"{conflict.capitalize()} làm mọi thứ bùng lên. Một mẻ trà đang lên hương có thể hỏng chỉ vì mất điện vài giờ; một kết quả dư lượng xấu có thể xóa sạch uy tín cả vùng. Gia Huy hiểu đây không còn là chuyện hôn ước, mà là miếng cơm của hàng trăm người.",
                    f"Anh mở sổ cân lá tươi. Trong đó có chữ ký của từng nông hộ, có ngày giao lá, có ghi chú trời mưa hay nắng. Những dòng chữ xấu xí ấy là thứ nhà họ Lâm chưa bao giờ coi trọng, vì họ quen nhìn đồi chè từ cửa kính xe.",
                    f"Một bà cụ trồng chè đem đến túi lá khô giữ làm mẫu. Bà nói Gia Huy là người duy nhất trả thêm tiền khi họ chuyển sang phân hữu cơ. Câu nói đơn giản ấy khiến Hạ Vy dừng bút rất lâu. Lợi nhuận có thể dựng báo cáo, lòng tin của người trồng thì khó mua trong một đêm.",
                    f"{villain} bắt đầu sốt ruột. Ông ta gọi điện cho ngân hàng, gọi cho khách hàng, gọi cho cả người quen ở huyện. Nhưng mỗi cuộc gọi đều vấp vào một câu hỏi giống nhau: hợp đồng vùng nguyên liệu sạch thật sự đứng tên ai?",
                    f"{ex} tìm gặp Gia Huy sau buổi kiểm tra. Cô nói nếu anh chịu nhường quyền thuê đất, cô có thể thuyết phục gia đình giữ lại cho anh một chức nhỏ. Gia Huy nhìn màn sương trôi qua mái nhà kính, đáp rằng anh đã từng muốn một gia đình, không phải một cái ghế thừa.",
                    f"Cuối chương {idx}, Hạ Vy đặt trước mặt anh bản phân tích rủi ro. Cô không hứa sẽ thắng. Cô chỉ chỉ ra con đường duy nhất sạch: mua lại nhà máy bằng hồ sơ thật, giữ nông hộ bằng giá thật, và để nhà họ Lâm tự đối diện với những gì họ đã ký.",
                ],
            )
        )
    story = {
        "title": title,
        "author": "Song Lam",
        "genre": "Sảng Văn",
        "intro": intro,
        "cover_prompt": "Square 1:1 photorealistic Vietnamese Da Lat tea revenge cover, misty Cau Dat tea hills, young tea entrepreneur holding clean agriculture contracts and tea leaves, wealthy family ashamed in background, no text, no watermark, dark top area.",
        "chapters": chapters,
        "meta": {"slug": "khinh-re-o-da-lat", "publication_status": "draft_pending_user_review", "rewrite_note": "Batch 1 unique rewrite"},
    }
    return deepen_chapters(
        story,
        {
            "lead": lead,
            "ally": ally,
            "villain": villain,
            "craft": "chuỗi trà sạch và vùng nguyên liệu Cầu Đất",
            "object_a": "sổ cân lá tươi của nông hộ",
            "object_b": "kết quả dư lượng thuốc cỏ",
            "place": "đồi chè Cầu Đất chìm trong sương lạnh",
            "stakes": "nhà máy trà, nông hộ và hợp đồng 210 tỷ",
            "sensory": "hơi trà nóng có mùi cỏ non và đất sau mưa",
        },
    )


def main() -> None:
    rewrites = {
        "02-duoi-khoi-xuong-gom-bat-trang.json": rewrite_story_02(),
        "03-vu-oan-o-benh-vien-cho-ray.json": rewrite_story_03(),
        "04-vut-hop-dong-cau-giay.json": rewrite_story_04(),
        "05-khinh-re-o-da-lat.json": rewrite_story_05(),
    }
    for filename, story in rewrites.items():
        (STORIES / filename).write_text(json.dumps(story, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"rewrote {filename}: {len(story['chapters'])} chapters")


if __name__ == "__main__":
    main()
