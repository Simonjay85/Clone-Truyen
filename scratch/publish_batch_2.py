# -*- coding: utf-8 -*-
import os
import json
import time
import subprocess

def format_paragraphs(sentences):
    return "".join([f"<p>{s}</p>" for s in sentences])

def main():
    print("=" * 60)
    print("🚀 BATCH 2 GENERATION & PUBLISHING ENGINE")
    print("=" * 60)

    # =========================================================================
    # 1. NOVEL ID 6: Đội Trưởng Bảo Vệ Khinh Tôi Làm Bảo Vệ Chân Vịt, Mật Vụ Tổng Cục 2 Xuất Hiện Bắt Hắn
    # =========================================================================
    n6_title = "Đội Trưởng Bảo Vệ Khinh Tôi Làm Bảo Vệ Chân Vịt, Mật Vụ Tổng Cục 2 Xuất Hiện Bắt Hắn"
    n6_author = "Đông Hải Cư Sĩ"
    n6_genre = "Sảng Văn"
    n6_cover_prompt = (
        "masterpiece, highly detailed book cover, anime illustration style, a cool young Vietnamese intelligence officer "
        "standing inside a high-tech modern server room with glowing blue led lights, next to an elegant corporate woman in a business suit, "
        "dramatic lighting, textless cover art"
    )
    n6_intro = format_paragraphs([
        "Vũ Đình Long, cựu thiếu tá tình báo thuộc Tổng cục 2, ẩn thân làm bảo vệ gác cổng tại tòa nhà Lotte Center Liễu Giai.",
        "Nhưng cuộc sống yên bình kết thúc khi gã đội trưởng bảo vệ hống hách khinh thường anh và tiếp tay cho đường dây gián điệp kinh tế.",
        "Đồng hành cùng Nguyễn Mai Lan - tổng giám đốc tập đoàn quốc phòng tư nhân, Long âm thầm giăng bẫy bắt trọn ổ phản bội ngay trong đêm mưa bão Hà Nội."
    ])

    n6_ch1 = [
        "Tiếng còi xe inh ỏi dội thẳng vào tầng hầm B3 của tòa nhà Lotte Center Liễu Giai giữa lòng Hà Nội.",
        "Vũ Đình Long đứng nghiêm trang ở bốt gác cổng, khoác trên mình bộ đồng phục bảo vệ màu xanh sờn vai.",
        "Đôi ủng cao su màu đen của anh bám đầy bụi xi măng khô khốc từ những công trình sửa chữa xung quanh tòa nhà.",
        "Trên tay anh là chiếc gậy chân vịt tuần tra chuyên dụng bằng sắt lạnh ngắt, dùng để kiểm tra gầm xe tránh bom mìn.",
        "Ít ai biết rằng, người bảo vệ quèn lặng lẽ chịu thương chịu khó gác hầm suốt nửa năm qua lại là Thiếu tá tình báo Tổng cục 2 ẩn danh.",
        "Anh đang thực hiện chuyên án mật để truy quét đường dây gián điệp công nghiệp đang nhắm vào dự án sợi carbon quân sự.",
        "Đột nhiên, gã đội trưởng bảo vệ Trần Hữu Hùng bước tới với vẻ mặt khệnh khạng đầy hống hách.",
        "Hùng diện bộ vest quản lý phẳng phiu, tay cầm điếu thuốc lá phả khói mù mịt làm căn phòng gác ngột ngạt.",
        "Lão nhìn đôi ủng bám đầy bụi của Long, lập tức đá mạnh vào chiếc gậy chân vịt tuần tra anh đang cầm.",
        "Tiếng gậy sắt chạm xuống sàn bê tông kêu 'coong' một tiếng khô khốc vang vọng khắp tầng hầm.",
        "Hùng nhổ một bãi nước bọt ngay sát mũi giày của Long và quát lớn: “Thằng cu li quét rác này, sao không cúi đầu chào sếp ngoại bang vừa đi qua?”",
        "“Mày chỉ là thằng bảo vệ chân vịt ăn lương tám triệu một tháng, biết thân biết phận thì im lặng mà làm việc!”",
        "Long im lặng nhặt chiếc gậy lên, ánh mắt anh bình thản nhưng sâu hoắm như đại dương không gợn sóng.",
        "Anh khẽ nói bằng giọng trầm ấm: “Báo cáo đội trưởng, tôi đang làm đúng quy trình kiểm tra an ninh đầu vào.”",
        "Hùng cười khẩy đầy ngạo mạn, chỉnh lại cổ áo rồi bỏ đi, không hề biết chiếc camera ẩn của anh đã ghi lại toàn bộ thái độ của lão."
    ]

    n6_ch2 = [
        "Mười hai giờ đêm, toàn bộ tòa nhà Lotte Center chìm vào sự tĩnh lặng đáng sợ.",
        "Long nhẹ nhàng di chuyển qua các hành lang tối tăm của tầng 30 bằng những bước chân không hề phát ra tiếng động.",
        "Anh sử dụng thiết bị dò sóng tần số cao tự chế, phát hiện một nguồn sóng vô tuyến bất thường phát ra từ phòng server lõi.",
        "Đi sâu vào phòng điều khiển, Long phát hiện một thiết bị USB gián điệp tinh vi đang cắm trực tiếp vào máy chủ dữ liệu.",
        "Thiết bị này đang âm thầm sao chép và truyền tải trái phép công thức dệt carbon quân sự ra ngoài qua mạng không dây.",
        "Đúng lúc đó, Long nghe thấy tiếng thì thầm phát ra từ góc tối hành lang ngoài phòng máy chủ.",
        "Đó chính là giọng của gã đội trưởng bảo vệ Trần Hữu Hùng đang nhận một xấp tiền USD dày cộm từ gã đàn ông lạ mặt.",
        "Gã lạ mặt chính là Vương Thế Xương, đại diện của tập đoàn công nghệ đối thủ cạnh tranh sinh tử.",
        "Hùng cười khúm núm: “Anh Xương yên tâm, tôi đã tắt toàn bộ camera an ninh ở khu vực tầng 30 trong vòng một tiếng.”",
        "“Thằng bảo vệ quèn gác cổng tối nay là thằng khờ, lão cứ thoải mái lấy dữ liệu mà không sợ ai phát hiện.”",
        "Long lặng lẽ đứng trong bóng tối, dùng chiếc điện thoại bảo mật ghi hình lại toàn bộ cuộc giao dịch bẩn thỉu này.",
        "Đường dây gián điệp kinh tế khổng lồ rút ruột tài sản quốc gia cuối cùng đã lộ diện hoàn toàn trước ánh sáng."
    ]

    n6_ch3 = [
        "Sáng hôm sau, tổng giám đốc tập đoàn công nghệ Nguyễn Mai Lan bước vào văn phòng với gương mặt vô cùng căng thẳng.",
        "Cô mặc chiếc đầm công sở màu đen sang trọng, mái tóc búi cao lộ rõ vẻ mệt mỏi sau một đêm mất ngủ vì lo lắng.",
        "Dự án dệt sợi carbon quân sự trị giá nghìn tỷ của cô đã bị rò rỉ thông tin ra thị trường chứng khoán khiến cổ phiếu lao dốc.",
        "Lan triệu tập cuộc họp khẩn cấp nhưng toàn bộ ban giám đốc đều im lặng, không ai dám nhận trách nhiệm bảo mật thông tin.",
        "Đúng lúc cô tuyệt vọng nhất, Long bước vào văn phòng tổng giám đốc dưới danh nghĩa nhân viên bảo vệ báo cáo sự cố điện.",
        "Anh nhẹ nhàng đặt lên bàn làm việc của cô một chiếc ổ cứng di động mã hóa bảo mật cực kỳ chuyên nghiệp.",
        "Long nói bằng giọng trầm ấm: “Tổng giám đốc Lan, đây là bản phân tích nhiễu sóng vô tuyến và bằng chứng rò rỉ dữ liệu đêm qua.”",
        "Lan sửng sốt nhìn tập tài liệu hiển thị trên máy tính, chứa đầy đủ hình ảnh giao dịch của Hùng và Xương.",
        "Cô ngẩng đầu nhìn người bảo vệ quèn trước mặt với ánh mắt tràn ngập sự ngạc nhiên và khâm phục sâu sắc.",
        "“Anh không phải là bảo vệ thông thường, anh thực sự là ai?” Lan hỏi, giọng cô run lên nhè nhẹ vì xúc động.",
        "Long khẽ mỉm cười: “Điều đó không quan trọng, quan trọng là chúng ta phải cùng nhau giăng bẫy bắt trọn ổ phản bội đêm nay.”"
    ]

    n6_ch4 = [
        "Đêm hôm đó, bầu trời Hà Nội đột ngột đổ cơn mưa giông dữ dội, gió rít liên hồi qua các khe cửa kính tòa nhà.",
        "Vương Thế Xương cùng ba gã hacker chuyên nghiệp đột nhập vào phòng server tầng 30 dưới sự tiếp tay của Trần Hữu Hùng.",
        "Chúng nhanh chóng kết nối thiết bị sao chép ổ cứng chuyên dụng, hí hửng vì nghĩ sắp lấy được bản công thức cuối cùng.",
        "Đột nhiên, toàn bộ hệ thống đèn chiếu sáng của tầng 30 vụt tắt, thay thế bằng ánh sáng đỏ lòm của đèn khẩn cấp.",
        "Tiếng còi báo động rú lên dồn dập, đồng thời các cửa thép chống cháy tự động hạ xuống, cô lập hoàn toàn căn phòng.",
        "Hùng hoảng hốt rút súng ngắn định bắn phá ổ khóa cửa nhưng toàn bộ hệ thống khóa đã bị thay đổi giao thức mã hóa.",
        "Long bước ra từ lối đi kỹ thuật, ánh sáng đỏ hắt lên khuôn mặt nam tính của anh vẻ kiên định, lạnh lùng như thép nguội.",
        "Hùng nghiến răng quát: “Thằng bảo vệ chân vịt mạt hạng này! Mày dám gài bẫy tao sao? Hôm nay mày phải chết ở đây!”",
        "Ba gã hacker và Hùng rút hung khí lao thẳng về phía Long, định dùng số đông khống chế anh trong tuyệt vọng."
    ]

    n6_ch5 = [
        "Long đứng im không hề né tránh, đôi mắt anh lóe lên tia nhìn lạnh lẽo của một chiến sĩ tình báo thực thụ.",
        "Chỉ bằng ba động tác võ thuật đặc nhiệm gọn gàng và chuẩn xác, anh đã quật ngã hai gã hacker xuống sàn bê tông lạnh ngắt.",
        "Đúng lúc Hùng giơ súng lên định bóp cò, cánh cửa thép dày phía sau đột ngột bị phá tung bởi một tiếng nổ lớn.",
        "Hàng chục chiến sĩ phản gián thuộc Tổng cục 2 quân đội mặc giáp đen, tay lăm lăm súng trường tấn công ập vào khống chế toàn bộ căn phòng.",
        "Vị chỉ huy dẫn đầu bước tới trước mặt Long, nghiêm trang giơ tay chào điều lệnh quân đội đầy trang trọng.",
        "“Báo cáo Thiếu tá Vũ Đình Long! Lực lượng phản gián đã bao vây toàn bộ tòa nhà và bắt giữ tất cả đồng bọn bên ngoài!”",
        "Hùng rụng rời tay chân, khẩu súng ngắn rơi bộp xuống đất, mặt lão xám ngoét không còn một giọt máu vì kinh hoàng tột độ.",
        "Lão run rẩy quỳ sụp xuống đất: “Thiếu tá tình báo... Hóa ra mày là mật vụ của Tổng cục 2 ẩn thân gác cổng suốt nửa năm qua...”",
        "Long nhìn lão bằng ánh mắt lạnh lùng: “Đưa tất cả bọn chúng về đơn vị để tiến hành lấy lời khai theo đúng luật pháp quân đội.”"
    ]

    n6_ch6 = [
        "Sáng hôm sau, chuyên án triệt phá đường dây gián điệp kinh tế Lotte được đưa tin rầm rộ trên các phương tiện truyền thông.",
        "Tập đoàn công nghệ của Mai Lan được bảo vệ an toàn tuyệt đối, cổ phiếu bùng nổ tăng trần liên tiếp trên sàn chứng khoán HNX.",
        "Trong văn phòng lộng lẫy, Lan chủ động ký sắc lệnh trao tặng gói thầu an ninh công nghệ cao trị giá 50 tỷ đồng cho đơn vị của Long.",
        "Cô bước đến gần anh, ánh mắt không còn vẻ kiêu sa của nữ tổng giám đốc mà tràn đầy sự dịu dàng và biết ơn chân thành.",
        "“Anh Long, cảm ơn anh đã bảo vệ giấc mơ công nghệ của em và cứu cả tập đoàn khỏi vực thẳm sụp đổ.”",
        "“Em không muốn chỉ hợp tác trên danh nghĩa công việc, em muốn mời anh làm bạn đời đồng hành cùng em suốt đời.”",
        "Long nhìn sâu vào đôi mắt trong veo của cô gái kiên cường, khẽ nắm lấy bàn tay mềm mại ấm áp của cô.",
        "“Tôi đồng ý, Mai Lan, chúng ta sẽ cùng nhau bảo vệ bình yên cho giang sơn này,” Long cười ấm áp dưới ánh nắng ban mai rực rỡ."
    ]

    n6_chapters = [
        {"title": "Chương 1: Anh Bảo Vệ Quèn Lotte Liễu Giai", "content": format_paragraphs(n6_ch1)},
        {"title": "Chương 2: Ám Mưu Rút Ruột Tài Liệu Công Nghệ", "content": format_paragraphs(n6_ch2)},
        {"title": "Chương 3: Mỹ Nhân Tổng Giám Đốc Vào Cuộc", "content": format_paragraphs(n6_ch3)},
        {"title": "Chương 4: Bẫy Sập Đêm Mưa Hà Ngoại", "content": format_paragraphs(n6_ch4)},
        {"title": "Chương 5: Thân Phận Bại Lộ: Mật Vụ Tổng Cục 2 Xuất Hiện", "content": format_paragraphs(n6_ch5)},
        {"title": "Chương 6: Công Lý Thực Thi Và Vinh Quang", "content": format_paragraphs(n6_ch6)}
    ]

    n6_data = {
        "title": n6_title,
        "author": n6_author,
        "genre": n6_genre,
        "intro": n6_intro,
        "cover_prompt": n6_cover_prompt,
        "chapters": n6_chapters
    }

    # =========================================================================
    # 2. NOVEL ID 7: Bị Đuổi Khỏi Công Ty Khởi Nghiệp, Sản Phẩm Của Tôi Thống Trị Top 1 App Store Đông Nam Á
    # =========================================================================
    n7_title = "Bị Đuổi Khỏi Công Ty Khởi Nghiệp, Sản Phẩm Của Tôi Thống Trị Top 1 App Store Đông Nam Á"
    n7_author = "Lâm Nam Tử"
    n7_genre = "Sảng Văn"
    n7_cover_prompt = (
        "masterpiece, highly detailed book cover, vivid anime style, a cool young Vietnamese developer looking determined "
        "sitting in front of dual monitors displaying advanced programming code, a beautiful elegant corporate woman standing beside him, "
        "neon lights, high-tech startup style"
    )
    n7_intro = format_paragraphs([
        "Cao Thanh Tùng, lập trình viên thiên tài, bị chính người bạn thân đồng sáng lập cướp công thức và đuổi cổ khỏi startup PayViet tại phố Duy Tân.",
        "Trở về căn phòng trọ 15m2 lạnh lẽo, Tùng bắt đầu xây dựng lại sản phẩm mới vượt trội hơn gấp trăm lần.",
        "Sát cánh cùng nữ giám đốc quỹ đầu tư sắc bén Nguyễn Khánh Linh, Tùng đưa app mới thống trị Top 1 App Store toàn Đông Nam Á và quay lại thâu tóm kẻ phản bội."
    ])

    n7_ch1 = [
        "Cơn mưa rào mùa hạ trút xối xả xuống con phố Duy Tân, quận Cầu Giấy, Hà Nội.",
        "Cao Thanh Tùng đứng dưới sảnh tòa nhà văn phòng, ôm chiếc thùng giấy cũ chứa bàn phím cơ và vài món đồ cá nhân.",
        "Chiếc thẻ nhân viên sáng lập của anh đã bị bẻ đôi vứt trong thùng rác văn phòng một cách phũ phàng.",
        "Người bạn thân đồng sáng lập Lâm Vĩnh phát biểu trước toàn bộ công ty: “Tùng chỉ là thằng gõ code quèn, không có tư duy kinh doanh.”",
        "“Hôm nay PayViet vừa nhận được Series A trị giá mười triệu USD, cậu không còn giá trị gì ở đây nữa, hãy cút đi!”",
        "Tùng nhìn gã bạn thân đầy tham lam, anh không hề tức giận mà chỉ khẽ nở một nụ cười lạnh lùng đầy bí hiểm.",
        "Anh bước đi dưới màn mưa lạnh giá, quay trở về căn phòng trọ nhỏ hẹp vỏn vẹn mười lăm mét vuông ở ngõ 165 Cầu Giấy.",
        "Đặt chiếc thùng giấy xuống giường tre cũ kỹ, Tùng khởi động chiếc máy tính bàn tự lắp ráp có hiệu năng cực cao của mình.",
        "Anh khẽ nói một mình: “Lâm Vĩnh, cậu nghĩ cậu ăn cắp được lõi mã nguồn của tôi là có thể vận hành được app sao?”",
        "“Cậu hoàn toàn không biết cấu trúc phân rã sharding đa tầng do chính tay tôi viết ra nguy hiểm thế nào đâu.”"
    ]

    n7_ch2 = [
        "Những đêm tiếp theo, căn phòng trọ nhỏ của Tùng luôn sáng đèn led xanh mờ ảo đến tận bốn giờ sáng.",
        "Tiếng gõ phím cơ lạch cạch vang lên liên hồi xua tan đi sự tĩnh mịch của con ngõ nghèo Hà Nội.",
        "Tùng bắt đầu viết từng dòng code đầu tiên cho dự án ứng dụng thanh toán fintech thế hệ mới có tên FinSafe.",
        "Ứng dụng này sử dụng giao thức bảo mật phi tập trung kết hợp thuật toán tối ưu hóa băng thông truyền tải dữ liệu.",
        "Nó cho phép thực hiện hàng triệu giao dịch mỗi giây với mức phí gần như bằng không và độ an toàn tuyệt đối tuyệt đối.",
        "Tùng tự tay pha những tách cà phê đen đặc không đường để giữ cho đầu óc luôn tỉnh táo sắc bén.",
        "Mồ hôi rịn ra trên trán anh nhưng đôi mắt anh vẫn rực sáng niềm tin chiến thắng và khát vọng lật đổ kẻ phản bội.",
        "Sau hai tuần viết code không ngừng nghỉ, phiên bản thử nghiệm đầu tiên của FinSafe đã hoàn thành một cách xuất sắc."
    ]

    n7_ch3 = [
        "Chiều hôm sau, Tùng hẹn gặp Nguyễn Khánh Linh tại quán cà phê sang trọng trên tầng cao Lotte Center.",
        "Linh là nữ giám đốc trẻ tuổi kiêm sáng lập của quỹ đầu tư mạo hiểm lớn nhất khu vực Đông Nam Á.",
        "Cô mặc chiếc đầm màu đỏ rượu vang quý phái, phong thái đĩnh đạc, lý tính và cực kỳ sắc sảo trong các quyết định tài chính.",
        "Linh nhấp một ngụm trà Anh quốc, chăm chú lắng nghe Tùng trình bày bản demo của ứng dụng FinSafe trên máy tính bảng.",
        "Đôi mắt lá liễu của cô dần hiện lên vẻ kinh ngạc tột độ trước kiến trúc bảo mật vô song của ứng dụng.",
        "“Tùng, đây không chỉ là một ứng dụng thanh toán thông thường, đây là một cuộc cách mạng fintech thực sự!” Linh thốt lên.",
        "Cô ấy điềm tĩnh đặt chiếc ví cầm tay xuống bàn, ký sắc lệnh đầu tư quỹ khẩn cấp năm triệu USD vào FinSafe ngay lập tức.",
        "“Tôi cam kết sẽ dùng toàn bộ nguồn lực truyền thông và mạng lưới đối tác của quỹ để đưa FinSafe bùng nổ toàn khu vực.”",
        "Tùng nhìn sự sòng phẳng quyết đoán của cô gái xinh đẹp, nở nụ cười tự tin: “Thỏa thuận thành công, cô sẽ không phải thất vọng.”"
    ]

    n7_ch4 = [
        "Ngày ra mắt chính thức của FinSafe cũng là ngày PayViet tổ chức sự kiện họp báo công bố tích hợp cổng thanh toán quốc gia.",
        "Lâm Vĩnh đứng trên sân khấu hoành tráng, tự tin đọc diễn văn ca ngợi PayViet là ứng dụng thanh toán số một Việt Nam.",
        "Đột nhiên, dưới sự kích hoạt của Tùng, toàn bộ hệ thống máy chủ của PayViet bất ngờ báo động đỏ liên hồi.",
        "Hệ thống lõi do Vĩnh ăn cắp đã gặp lỗi phân rã sharding nghiêm trọng do không có khóa đồng thuận sinh trắc học của Tùng.",
        "Hàng loạt giao dịch của khách hàng bị treo cứng, số dư tài khoản hiển thị sai lệch làm nổ ra làn sóng phẫn nộ tột cùng.",
        "Cùng lúc đó, Linh ra lệnh cho phi đội marketing kích hoạt chiến dịch ra mắt FinSafe trên toàn bộ các kênh truyền thông lớn.",
        "FinSafe xuất hiện như một đấng cứu thế hoàn hảo, giải quyết triệt để mọi lỗi bảo mật và nghẽn mạng mà PayViet đang gặp phải.",
        "Hàng triệu người dùng điên cuồng tải FinSafe, khiến hệ thống của PayViet hoàn toàn bị bỏ rơi chỉ trong vòng vài tiếng đồng hồ."
    ]

    n7_ch5 = [
        "Chỉ sau ba mươi ngày ra mắt, tin tức chấn động nổ ra trên khắp các diễn đàn công nghệ toàn cầu.",
        "FinSafe chính thức thống trị Top 1 bảng xếp hạng App Store tại Việt Nam, Singapore, Thái Lan và Indonesia.",
        "Tổng số người dùng đăng ký hoạt động hàng ngày vượt mốc mười triệu lượt, định giá doanh nghiệp vọt lên năm trăm triệu USD.",
        "Trong khi đó, PayViet của Lâm Vĩnh hoàn toàn sụp đổ, các nhà đầu tư lớn đồng loạt rút vốn và yêu cầu bồi thường thiệt hại.",
        "Vĩnh mặt mày xám ngoét, chạy đến phòng trọ cũ của Tùng gõ cửa điên cuồng, quỳ sụp xuống đất xin anh cứu giúp.",
        "“Tùng ơi... Tôi sai rồi... Cầu xin cậu quay lại cứu PayViet... Tôi sẽ nhường lại toàn bộ chức vụ CEO cho cậu...” Vĩnh khóc lóc.",
        "Tùng đứng tựa lưng vào cửa phòng trọ, ánh mắt lạnh lùng nhìn gã bạn phản bội đang run rẩy dưới chân mình.",
        "“Muộn rồi, Lâm Vĩnh, tài khoản ngân hàng Vietcombank của tôi vừa được Linh chuyển thêm mười triệu USD để mua đứt PayViet với giá rẻ mạt,” Tùng nói."
    ]

    n7_ch6 = [
        "Thương vụ thâu tóm ngược PayViet được hoàn tất nhanh chóng dưới sự tư vấn pháp lý sắc sảo của Khánh Linh.",
        "Lâm Vĩnh phải ra đi với hai bàn tay trắng, đồng thời đối mặt với án phạt tù do hành vi gian lận tài chính doanh nghiệp.",
        "FinSafe chính thức đổi tên thành FinSafe Global, trở thành kỳ lân công nghệ mới của Đông Nam Á với văn phòng lộng lẫy tại Duy Tân.",
        "Khánh Linh bước vào văn phòng CEO của Tùng, mang theo một bó hoa hồng đỏ thắm và nụ cười rạng rỡ như nắng mùa thu.",
        "“Chúc mừng anh, chủ tịch Cao Thanh Tùng, chúng ta đã tạo nên một kỳ tích lịch sử cho nền công nghệ nước nhà.”",
        "Cô ấy khẽ tựa đầu vào vai anh, giọng nói dịu dàng chứa đựng tình cảm chân thành kiên định bấy lâu nay giữ kín.",
        "“Em muốn đồng hành cùng anh không chỉ trên thương trường, mà còn suốt cuộc đời dài phía trước, anh đồng ý chứ?”",
        "Tùng siết chặt bàn tay mềm mại của cô gái thông minh, nở nụ cười ngập tràn hạnh phúc: “Anh đồng ý, Linh, cảm ơn em đã luôn tin anh.”"
    ]

    n7_chapters = [
        {"title": "Chương 1: Đêm Mưa Duy Tân Và Gã Bạn Phản Bội", "content": format_paragraphs(n7_ch1)},
        {"title": "Chương 2: Khởi Nghiệp Lại Từ Phòng Trọ 15m2", "content": format_paragraphs(n7_ch2)},
        {"title": "Chương 3: Nữ Giám Đốc Quỹ Đầu Tư Sắc Sảo", "content": format_paragraphs(n7_ch3)},
        {"title": "Chương 4: Ngày Ra Mắt Và Đòn Đánh Trộm Của Kẻ Thù", "content": format_paragraphs(n7_ch4)},
        {"title": "Chương 5: Thống Trị Đông Nam Á: Top 1 App Store Gọi Tên", "content": format_paragraphs(n7_ch5)},
        {"title": "Chương 6: Thu Mua Ngược Và Sự Sụp Đổ Của Kẻ Phản Bội", "content": format_paragraphs(n7_ch6)}
    ]

    n7_data = {
        "title": n7_title,
        "author": n7_author,
        "genre": n7_genre,
        "intro": n7_intro,
        "cover_prompt": n7_cover_prompt,
        "chapters": n7_chapters
    }

    # =========================================================================
    # 3. NOVEL ID 8: Nhà Chồng Khinh Tôi Không Biết Nấu Ăn, Tôi Giật Giải Đầu Bếp Số 1 Đông Nam Á Trước Mặt Họ
    # =========================================================================
    n8_title = "Nhà Chồng Khinh Tôi Không Biết Nấu Ăn, Tôi Giật Giải Đầu Bếp Số 1 Đông Nam Á Trước Mặt Họ"
    n8_author = "Nam Phương Nhất Nhạn"
    n8_genre = "Sảng Văn"
    n8_cover_prompt = (
        "masterpiece, highly detailed book cover, anime illustration style, a beautiful young Vietnamese female chef "
        "wearing a premium white chef uniform, holding a glowing traditional culinary dish in a professional luxury kitchen, "
        "next to an elegant older gentleman, cinematic lighting, textless cover art"
    )
    n8_intro = format_paragraphs([
        "Lê Thị Nhung, nàng dâu hiền lành chịu khó xuất thân nghèo khó, bị gia đình chồng hào môn ở Đà Thành khinh miệt không biết nấu ăn.",
        "Hóa ra cô là đầu bếp thiên tài ẩn danh, người nắm giữ công thức ẩm thực cung đình độc bản được Michelin công nhận.",
        "Được sự ủng hộ kiên định của chuyên gia ẩm thực cấp cao Nguyễn Thu Trang, Nhung từng bước bước lên đỉnh cao, đoạt giải Đầu bếp số 1 Đông Nam Á và khiến nhà chồng quỳ gối hối hận."
    ])

    n8_ch1 = [
        "Cơn gió biển lạnh buốt từ bán đảo Sơn Trà thổi vào căn biệt thự lộng lẫy của nhà họ Trần ở Đà Thành.",
        "Lê Thị Nhung đứng trong gian bếp rộng lớn, tay bưng chiếc thố sứ đựng canh hầm sâm nóng hổi.",
        "Đôi bàn tay cô đỏ ửng, chai sần vì phải rửa hàng trăm chiếc bát đĩa sau bữa tiệc gia tộc hào môn.",
        "Mẹ chồng cô, bà Lâm Mỹ Hạnh, nhìn chiếc thố canh liền gạt phắt tay làm nước canh nóng bắn lên mu bàn tay Nhung đỏ rát.",
        "Bà Hạnh mỉa mai: “Thứ con gái quê mùa chỉ biết nấu ba món luộc dở tệ, gả vào nhà họ Trần đúng là nỗi nhục của chúng tôi!”",
        "“Tiệc mừng thọ cụ cố ngày mai có sự tham gia của các đối tác nước ngoài, cô cấm được sờ vào bếp, để bếp trưởng Hoàng làm việc!”",
        "Nhung im lặng cúi đầu dọn dẹp đống sứ vỡ, ánh mắt cô thoáng lên vẻ lạnh lùng nhưng kiên định đến lạ lùng.",
        "Không ai biết rằng, cô chính là đệ tử chân truyền duy nhất của Vua bếp cung đình Huế, sở hữu khứu giác nhạy bén vô song.",
        "Nhung khẽ nói thầm: “Bếp trưởng Hoàng tham lam kia, công thức súp bào ngư vạn đạm của ông ta thực ra chỉ là hóa chất nhân tạo.”"
    ]

    n8_ch2 = [
        "Ngày hôm sau, tiệc mừng thọ cụ cố diễn ra vô cùng hoành tráng tại sảnh lớn của resort năm sao Đà Thành.",
        "Bếp trưởng Hoàng Thế Nam tự tin bưng món súp bào ngư vạn đạm gia truyền lên phục vụ hội đồng thẩm định ẩm thực quốc tế.",
        "Tuy nhiên, ngay khi cụ cố và vị chuyên gia Michelin người Pháp nhấp thử một thìa súp, gương mặt họ bỗng biến sắc nghiêm trọng.",
        "Mùi hóa chất nhân tạo nồng nặc và vị tanh của bào ngư kém chất lượng bốc lên làm cụ cố lên cơn ho kịch liệt.",
        "Bà Hạnh hốt hoảng, định đổ tội cho Nhung đã đột nhập vào bếp phá hoại nguồn nguyên liệu sạch của resort.",
        "Nhung bước ra trước đám đông khách quý, mặc chiếc áo bà ba màu nâu giản dị nhưng phong thái đĩnh đạc phi thường.",
        "Cô điềm tĩnh nói: “Bào ngư này đã bị ngâm hóa chất bảo quản formaldehyde vượt ngưỡng cho phép mười lần để che giấu mùi ôi thối.”",
        "“Bếp trưởng Hoàng đã rút ruột ngân sách mua bào ngư đông lạnh rẻ tiền để đút túi riêng, tôi có đầy đủ hóa đơn đối chứng đây.”",
        "Hoàng Thế Nam mặt cắt không còn giọt máu, lập tức bị lực lượng an ninh kiểm tra và đình chỉ công tác ngay tại sảnh tiệc."
    ]

    n8_ch3 = [
        "Giữa lúc bữa tiệc mừng thọ đứng trước nguy cơ đổ vỡ hoàn toàn, Nhung đề xuất tự tay vào bếp để hoàn thiện món ăn thay thế.",
        "Nguyễn Thu Trang, chuyên gia ẩm thực cấp cao của Bộ Y tế kiêm giám khảo Michelin Asia, nhìn Nhung với ánh mắt đầy tò mò.",
        "Trang nói: “Cô Nhung, thời gian chỉ còn ba mươi phút, cô định nấu món gì để thuyết phục hội đồng khó tính của chúng tôi?”",
        "Nhung tự tin mỉm cười: “Tôi sẽ nấu món Cá bớp kho tộ vị cung đình kết hợp hương thảo mộc Hội An ngọt ngào.”",
        "Bước vào gian bếp, Nhung di chuyển các ngón tay nhanh thoăn thoắt, dùng dao cắt thái điêu luyện như một nghệ sĩ thực thụ.",
        "Cô tự tay pha chế nước màu từ mật mía truyền thống kết hợp muối hầm tinh khiết và các loại thảo dược bí truyền.",
        "Lửa đỏ bùng lên dưới chiếc niêu đất nung cổ xưa, tỏa ra một mùi hương ngọt ngào, ấm nồng chấn động cả resort."
    ]

    n8_ch4 = [
        "Khi chiếc niêu đất kho tộ nghi ngút khói được Nhung bưng lên bàn tiệc, toàn bộ sảnh tiệc bỗng chìm vào sự im lặng tuyệt đối.",
        "Vị chuyên gia Michelin người Pháp nhấp thử một miếng cá bớp mềm mại, đôi mắt ông lập tức rực sáng lên vì kinh ngạc tột độ.",
        "“Mon Dieu! Đây không phải là món ăn thông thường, đây là kiệt tác nghệ thuật ẩm thực kết hợp hoàn hảo giữa đất và nước!”",
        "Cụ cố nhà họ Trần ăn xong miếng cá liền cảm thấy cơ thể khỏe khoắn hẳn ra, huyết áp ổn định và liên tục gật đầu khen ngợi.",
        "Thu Trang mỉm cười đĩnh đạc, ký sắc lệnh trao tặng Nhung tấm thẻ vàng đề cử giải thưởng Đầu bếp xuất sắc Đông Nam Á.",
        "Mẹ chồng Lâm Mỹ Hạnh và gã chồng bội bạc Trần Minh đứng ngây người ra như phỗng, không thể tin nổi đứa con dâu quê mùa lại có tài năng thiên sứ như vậy.",
        "Nhung nhìn sự ngỡ ngàng uất ức của họ, khẽ nở nụ cười lạnh lùng: “Đây mới chỉ là sự khởi đầu cho cú tát pháp lý của tôi.”"
    ]

    n8_ch5 = [
        "Ba tháng sau, đêm chung kết giải đấu ẩm thực Đông Nam Á diễn ra vô cùng kịch tính tại trung tâm hội nghị quốc tế Đà Nẵng.",
        "Nhung đại diện cho Việt Nam, mặc bộ trang phục bếp trưởng trắng muốt thêu đóa hoa sen vàng rực rỡ và kiêu sa.",
        "Đối thủ của cô là các đầu bếp hàng đầu đến từ Thái Lan, Singapore và Malaysia với những trang bị tối tân nhất.",
        "Nhà chồng cũ của Nhung cũng có mặt dưới hàng ghế khán giả dưới tư cách nhà tài trợ phụ, mặt mày hậm hực không yên.",
        "Nhung thực hiện món Phở sâm ngọc linh độc bản, kết hợp tinh túy của nước dùng hầm xương ba mươi tiếng và sâm quý Việt Nam.",
        "Mùi hương thơm ngọt ngào tinh khiết của sâm hòa cùng vị béo ngậy của tủy xương lan tỏa khắp khán phòng rộng lớn.",
        "Hội đồng giám khảo đồng loạt chấm điểm tuyệt đối mười điểm, tuyên bố Nhung đoạt cúp vô địch Đầu bếp số một Đông Nam Á."
    ]

    n8_ch6 = [
        "Chiếc cúp vàng lấp lánh được Nhung giơ cao dưới ánh đèn sân khấu rực rỡ và tiếng vỗ tay vang dội của hàng ngàn khán giả.",
        "Gia đình họ Trần đứng bên ngoài hành lang, bà mẹ chồng Mỹ Hạnh quỳ sụp xuống đất, khóc lóc cầu xin Nhung quay lại nhà.",
        "“Nhung ơi... Mẹ sai rồi... Con quay lại nhà giúp resort họ Trần vực dậy danh tiếng đi... Mẹ sẽ nhường lại toàn quyền quản lý bếp cho con...”",
        "Nhung nhìn bà ta bằng ánh mắt lạnh lùng như băng tuyết Sơn Trà, khẽ giơ tập hồ sơ ly hôn đã được tòa án Đà Nẵng phê duyệt.",
        "“Bà Lâm Mỹ Hạnh, tôi đã ký đơn ly hôn sòng phẳng với con trai bà rồi. Hiện tại tôi là đại sứ thương hiệu của tập đoàn Michelin toàn cầu.”",
        "“Tập đoàn của tôi vừa hoàn tất thủ tục mua đứt chuỗi resort của gia đình bà do nợ nần quá hạn tại Agribank,” Nhung nói.",
        "Thu Trang bước tới bên cạnh Nhung, trao cho cô chiếc ôm chúc mừng ấm áp và ánh mắt chứa đầy tình cảm sâu sắc.",
        "“Chúc mừng em, Nhung, từ nay em chính là nữ hoàng ẩm thực truyền thống của Đông Nam Á,” Trang cười rạng rỡ dưới nắng biển xanh mát."
    ]

    n8_chapters = [
        {"title": "Chương 1: Nàng Dâu Rửa Bát Ở Hào Môn Đà Thành", "content": format_paragraphs(n8_ch1)},
        {"title": "Chương 2: Tiệc Mừng Thọ Sóng Gió Và Gã Bếp Trưởng Gian Trá", "content": format_paragraphs(n8_ch2)},
        {"title": "Chương 3: Sự Gặp Gỡ Định Mệnh Với Nữ Chuyên Gia Michelin", "content": format_paragraphs(n8_ch3)},
        {"title": "Chương 4: Lửa Đỏ Hội An: Món Ăn Truyền Thống Thức Tỉnh", "content": format_paragraphs(n8_ch4)},
        {"title": "Chương 5: Đêm Chung Kết Đông Nam Á Chấn Động", "content": format_paragraphs(n8_ch5)},
        {"title": "Chương 6: Vả Mặt Hào Môn: Mẹ Chồng Quỳ Xin Quay Lại", "content": format_paragraphs(n8_ch6)}
    ]

    n8_data = {
        "title": n8_title,
        "author": n8_author,
        "genre": n8_genre,
        "intro": n8_intro,
        "cover_prompt": n8_cover_prompt,
        "chapters": n8_chapters
    }

    # =========================================================================
    # PUBLISHING SEQUENCE
    # =========================================================================
    novels = [n6_data, n7_data, n8_data]
    
    for i, novel in enumerate(novels, start=6):
        print(f"\n[+] Preparing to publish Novel ID {i}: {novel['title']}...")
        
        # Write to pending_novel.json
        pending_file = "pending_novel.json"
        with open(pending_file, "w", encoding="utf-8") as f:
            json.dump(novel, f, ensure_ascii=False, indent=2)
        print(f"✓ Written draft to {pending_file}.")
        
        # Run publish_local_novel.py
        print(f"🚀 Launching publish_local_novel.py for Novel ID {i}...")
        res = subprocess.run(["python3", "publish_local_novel.py"], capture_output=True, text=True)
        print(res.stdout)
        if res.stderr:
            print("STDERR:", res.stderr)
            
        print(f"✓ Finished processing Novel ID {i}.\n")
        time.sleep(2)

    print("=" * 60)
    print("🎉 ALL BATCH 2 NOVELS PUBLISHED SUCCESSFULLY!")
    print("=" * 60)

if __name__ == "__main__":
    main()
