import os
import json
import sys

TEMP_FILE = "/Users/aaronnguyen/TN/App/doctieuthuyet/pending_novel_13_temp.json"
FINAL_FILE = "/Users/aaronnguyen/TN/App/doctieuthuyet/pending_novel_13.json"

def wrap_sentences(text_list):
    return "".join(f"<p>{s.strip()}</p>\n" for s in text_list if s.strip())

def main():
    if len(sys.argv) < 2:
        print("Usage: python build_novel_13.py <stage>")
        sys.exit(1)
        
    stage = sys.argv[1]
    
    if stage == "1":
        # Write Intro and Chapters 1-3
        intro = wrap_sentences([
            "<strong>\"Năm năm đổ máu và mồ hôi trên từng dòng code blockchain tại căn penthouse phố Nguyễn Huệ, tôi tạo ra NexaSphere - giao thức DeFi nghìn tỷ đầu tiên của người Việt. Thế nhưng, kẻ đồng sáng lập mà tôi từng coi như anh em ruột thịt lại cấu kết với thế lực ngầm, cướp đoạt private key, giả mạo chữ ký số của tôi rồi cười khẩy: 'Mày chỉ là một thằng gõ code quèn!'\"</strong>",
            "Không ai ngờ, chính chiếc ví lạnh chứa token nghìn tỷ mà hắn cướp đi lại mang một lỗ hổng bảo mật ẩn mà chỉ tôi mới biết. Khi hắn bắt tay với sàn GateVortex để tẩu tán tài sản, hắn đã kích hoạt quả bom nổ chậm do tôi cài cắm.",
            "Với sự sát cánh của Trần Ngọc Bích - Phó Cục trưởng Cục An ninh mạng A05, chúng tôi bắt đầu cuộc đi săn công nghệ nghẹt thở trên không gian số, hack ngược cả sàn giao dịch crypto quốc tế để đòi lại công lý!"
        ])
        
        c1 = [
            "Cơn mưa dông tháng năm quất liên hồi vào những tấm kính cường lực bóng loáng của căn penthouse tầng bốn mươi hai.",
            "Từ góc nhìn này, phố đi bộ Nguyễn Huệ bên dưới nhòe nhoẹt trong màn nước, những ánh đèn neon xanh đỏ của trung tâm Quận 1 kéo dài thành những vệt sáng ma mị.",
            "Trương Minh Đức ngồi bất động trước dãy màn hình Dell UltraSharp ba mươi hai inch, gương mặt hốc hác hiện rõ quầng thâm đen sẫm sau hai tuần mất ngủ liên tục.",
            "Ánh sáng xanh từ các dòng code Solidity phản chiếu lên đôi mắt đờ đẫn nhưng sắc lạnh của anh.",
            "Trên bàn làm việc, ba ly cà phê sữa đá đã tan hết đá, nước đọng chảy loang lổ trên mặt bàn gỗ óc chó đắt tiền.",
            "NexaSphere, giao thức tài chính phi tập trung (DeFi) trị giá hơn một nghìn tỷ đồng do anh tự tay viết từng dòng code, vừa hoàn thành đợt kiểm toán bảo mật cuối cùng.",
            "Đức đưa bàn tay run rẩy vì kiệt sức nhấp một ngụm nước lã, cảm giác mệt mỏi rã rời lan khắp cơ thể.",
            "Cánh cửa gỗ gõ đỏ của căn penthouse đột ngột mở ra.",
            "Tiếng cười trầm thấp và mùi nước hoa Sauvage nồng nặc phá vỡ không gian tĩnh mịch của phòng làm việc.",
            "Lâm Thế Hùng bước vào, áo vest Tom Ford xám tro thẳng tắp, mái tóc chải chuốt bóng lộn phản chiếu ánh đèn trần.",
            "Phía sau Hùng là bốn gã đàn ông lực lưỡng mặc vest đen đeo tai nghe đàm thoại, gương mặt lạnh lùng không chút cảm xúc.",
            "Đức hơi nhíu mày, trực giác nhạy bén của một kỹ sư công nghệ báo cho anh biết có điều gì đó không ổn.",
            "Hùng tiến lại gần, đứng tựa lưng vào mép bàn làm việc của Đức, ánh mắt nhìn những dòng code trên màn hình với vẻ khinh miệt.",
            "— Đức này, cậu nghỉ ngơi được rồi đấy, — Hùng nói, giọng điệu nhẹ nhàng nhưng chứa đựng sự lạnh lẽo đáng sợ.",
            "Đức ngẩng đầu nhìn người bạn thân mười năm, người đồng sáng lập đã cùng anh đi qua những ngày tháng ăn mì tôm trong phòng trọ mười mét vuông.",
            "— Ý anh là sao, anh Hùng? Ngày mai là chúng ta chính thức mainnet và mở bán token cộng đồng rồi, — Đức khàn giọng hỏi.",
            "Hùng khẽ bật cười, tiếng cười vang lên giữa phòng khách penthouse rộng lớn nghe lạnh tanh như tiếng kim loại chạm nhau.",
            "Gã rút từ trong túi áo vest ra một chiếc iPad, lướt ngón tay rồi quay màn hình về phía Đức.",
            "Trên màn hình là giao diện ví lạnh Ledger của dự án NexaSphere, nhưng địa chỉ ví multisig (đa chữ ký) điều hành giao thức đã được thay đổi.",
            "Địa chỉ ví quản trị tối cao của Đức đã hoàn toàn bị xóa bỏ, thay vào đó là một địa chỉ ví lạ hoắc.",
            "Đức bàng hoàng lao về phía bàn phím, ngón tay gõ liên hồi trên terminal để kiểm tra quyền truy cập admin.",
            "Dòng chữ đỏ chót hiện lên tàn nhẫn trên màn hình: \"Error: Access Denied. Sender address is not the owner.\"",
            "Mồ hôi lạnh từ trên trán Đức chảy ròng ròng xuống cằm, thấm ướt cả cổ áo sơ mi sờn cũ.",
            "— Anh... anh đã làm gì? Làm sao anh thay đổi được ví multisig khi không có chữ ký số của tôi? — Đức quát lên, giọng run rẩy dữ dội.",
            "Hùng ngửa cổ cười lớn, nụ cười đầy kiêu ngạo và thỏa mãn của kẻ đã nắm chắc phần thắng trong tay.",
            "Gã chỉ tay lên chiếc đèn trần pha lê lộng lẫy ngay phía trên bàn làm việc của Đức.",
            "— Đức à, cậu giỏi code thật, nhưng cậu quá ngây thơ về lòng người, — Hùng nói, mắt co thắt đầy mưu mô.",
            "— Tôi đã gắn một camera siêu nhỏ tiêu cự cực cao ngay trên chiếc đèn đó suốt hai tháng qua.",
            "— Từng ký tự trong mật khẩu ví lạnh, từng ký tự trong hai mươi bốn từ khóa khôi phục (passphrase) của cậu, tôi đều ghi lại không sót một nét.",
            "— Còn về chữ ký số? Đội luật sư của tôi đã chuẩn bị sẵn một biên bản từ nhiệm và chuyển nhượng tài sản trí tuệ có chữ ký số giả mạo của cậu.",
            "— Trên danh nghĩa pháp lý và blockchain, cậu đã tự nguyện rời bỏ NexaSphere và chuyển toàn bộ 50 triệu USD token cho tôi.",
            "Đức đứng phắt dậy, lồng ngực phập phồng thở dốc, hai mắt đỏ ngầu sọc máu vì tức giận.",
            "Anh muốn lao vào túm lấy cổ áo gã phản bội, nhưng hai gã bảo vệ lập tức bước lên chắn trước mặt Hùng, cánh tay thép của chúng đè chặt vai Đức xuống ghế.",
            "— Hùng! Đó là công sức năm năm qua của tôi! Là máu và nước mắt của tôi! — Đức hét lên, tiếng hét khản đặc vì phẫn nộ.",
            "Hùng cúi xuống nhìn Đức, nụ cười nửa miệng đầy mưu mô hiện rõ trên gương mặt điển trai xảo quyệt.",
            "Gã vỗ nhẹ vào má Đức, từng cái vỗ nhẹ nhưng nhục nhã như những cái tát vô hình.",
            "— Công sức? Đức ơi, trong thế giới này, kẻ gõ code chỉ là lũ làm thuê hạng sang mà thôi.",
            "— Không có quan hệ ngoại giao của tôi, không có những buổi tiệc tùng tiếp khách với các quỹ đầu tư lớn ở Singapore, không có sự bảo trợ của sàn GateVortex, thì đống code của cậu chỉ là rác rưởi.",
            "— Mày chỉ là một thằng gõ code quèn, hiểu chưa? Bây giờ, NexaSphere là của tôi, căn penthouse này là của tôi.",
            "— Bảo vệ, đưa cựu founder của chúng ta ra ngoài. Trời đang mưa, nhớ cho cậu ta một chiếc ô rách nhé.",
            "Hai gã bảo vệ thô bạo xách Đức dậy, giật phăng chiếc ba lô cũ kỹ của anh rồi đẩy anh ra phía cửa thang máy chuyên dụng.",
            "Cửa thang máy đóng lại, che khuất nụ cười ngạo nghễ của Lâm Thế Hùng và ánh mắt chế giễu của những kẻ phản bội.",
            "Đức bị ném ra khỏi sảnh tòa nhà Penthouse Nguyễn Huệ.",
            "Cơn mưa tầm tã trút xuống đầu anh, nước mưa lạnh ngắt thấm đẫm mái tóc và bộ quần áo xộc xệch.",
            "Anh đứng dưới mưa, chiếc ba lô sũng nước ôm chặt trước ngực, hai bàn tay siết chặt đến mức móng tay găm vào da thịt rớm máu.",
            "Đường phố Nguyễn Huệ về đêm lấp lánh ánh đèn phản chiếu trên mặt đường ướt nhẹp.",
            "Đức nhìn lên tầng bốn mươi hai, nơi ánh sáng căn penthouse vẫn rực rỡ, lòng căm hận trào dâng bóp nghẹt cuống họng.",
            "Nhưng trong đôi mắt đỏ ngầu của thiên tài blockchain không có sự tuyệt vọng, chỉ có một ngọn lửa lạnh lẽo đang âm ỉ cháy.",
            "Hùng không hề biết một điều.",
            "Đức đã cài một hàm ẩn (hidden backdoor) trong cấu trúc hợp đồng thông minh của ví multisig NexaSphere đề phòng trường hợp bị tấn công mạng.",
            "Lỗ hổng zero-day này chỉ được kích hoạt khi có một chuỗi giao dịch có chữ ký số bị lỗi cấu trúc n-ounce do chính Đức thiết kế.",
            "Anh lẩm bẩm trong tiếng mưa rơi xối xả:",
            "— Lâm Thế Hùng, anh cướp được private key của tôi, nhưng anh không cướp được bộ não này.",
            "— Tôi sẽ khiến anh phải quỳ xuống dưới chân tôi trên chính con phố Nguyễn Huệ này."
        ]
        
        c2 = [
            "Đức bước đi lếch thếch dọc theo phố đi bộ Nguyễn Huệ, nước mưa từ tóc nhỏ giọt xuống vỉa hè đá hoa cương.",
            "Anh ghé vào một quán cà phê nhỏ nằm sâu trong một con hẻm trên đường Ngô Đức Kế, chọn một chiếc bàn khuất trong góc tối.",
            "Quán cà phê vắng khách, tiếng nhạc jazz nhẹ nhàng vang lên đối lập hoàn toàn với tiếng sét đánh đùng đoàng ngoài trời.",
            "Đức mở chiếc laptop ThinkPad X1 Carbon cũ kỹ từ trong ba lô ra, may mắn là ba lô chống nước tốt nên máy vẫn khô ráo.",
            "Anh cắm chiếc USB chứa môi trường Linux bảo mật vào máy, nhanh chóng khởi động hệ thống và kết nối với mạng Tor.",
            "Ngón tay Đức gõ nhanh trên bàn phím, đôi mắt dán chặt vào terminal theo dõi luồng giao dịch trên blockchain explorer.",
            "Đúng như anh dự đoán, Lâm Thế Hùng đã bắt đầu tẩu tán tài sản.",
            "Số token trị giá năm trăm tỷ đồng đầu tiên đã được chuyển từ ví nóng của dự án sang một ví trung gian.",
            "Từ ví trung gian này, dòng tiền đang được chia nhỏ để đẩy lên sàn GateVortex — một sàn giao dịch crypto quốc tế nổi tiếng với các hoạt động rửa tiền mờ ám.",
            "— Hắn muốn rửa sạch số token này thành USDT rồi rút về tài khoản ngân hàng ngoại biên ở Singapore, — Đức lẩm bẩm, răng nghiến chặt.",
            "Bỗng nhiên, một bóng người cao ráo đứng che khuất ánh đèn vàng phía trên đầu Đức.",
            "Một mùi hương thoang thoảng của hoa sen nhẹ nhàng, thanh khiết lan tỏa trong không gian ẩm ướt.",
            "Đức cảnh giác gập nửa màn hình laptop, tay phải đặt sẵn vào phím tắt để xóa nhanh bộ nhớ tạm của máy.",
            "Người phụ nữ đứng trước mặt anh mặc một bộ vest công sở màu xanh đen cực kỳ lịch sự, mái tóc đen dài được cột gọn gàng phía sau.",
            "Gương mặt cô thanh tú, đôi mắt sáng như sao đêm và toát lên vẻ uy nghiêm, sắc sảo của người nắm quyền lực.",
            "Cô ngồi xuống chiếc ghế đối diện Đức mà không cần anh đồng ý, đặt một chiếc thẻ ngành bọc da đen lên bàn gỗ.",
            "Trên chiếc thẻ có quốc huy Việt Nam và dòng chữ: \"Bộ Công an — Cục An ninh mạng và phòng, chống tội phạm sử dụng công nghệ cao (A05)\".",
            "Dòng chữ nhỏ hơn ghi tên và chức vụ: \"Trần Ngọc Bích — Phó Cục trưởng\".",
            "Đức nheo mắt nhìn người phụ nữ trước mặt, nhịp tim hơi tăng nhanh.",
            "— Anh Trương Minh Đức, tôi đã tìm anh suốt hai tiếng qua, — Ngọc Bích lên tiếng, giọng nói trầm ấm nhưng vô cùng dứt khoát.",
            "Đức im lặng hai giây, ánh mắt dò xét gương mặt không chút sơ hở của nữ Phó Cục trưởng.",
            "— Cục An ninh mạng tìm một thằng dev thất nghiệp như tôi để làm gì? — Đức hỏi, giọng khàn khàn vì lạnh.",
            "Ngọc Bích khẽ mỉm cười, một nụ cười mỏng nhưng vô cùng tự tin.",
            "Cô đẩy chiếc điện thoại chuyên dụng bảo mật về phía Đức, màn hình đang hiển thị biểu đồ giao dịch của sàn GateVortex.",
            "— Anh không phải thằng dev thất nghiệp. Anh là người duy nhất ở Việt Nam hiểu rõ cấu trúc mật mã của NexaSphere, — Bích nói.",
            "— Chúng tôi đã theo dõi Lâm Thế Hùng và sàn GateVortex hơn sáu tháng qua.",
            "— Sàn giao dịch này đang nằm trong tầm ngắm của chuyên án phối hợp giữa A05 và C03 về đường dây đánh bạc và rửa tiền xuyên quốc gia trị giá hàng chục nghìn tỷ đồng.",
            "— Việc Lâm Thế Hùng cướp token của anh và đẩy lên sàn GateVortex tối nay đã nằm trong hệ thống cảnh báo sớm của chúng tôi.",
            "Đức siết chặt hai tay dưới gầm bàn, ánh mắt lóe lên tia sáng hy vọng.",
            "— Các chị có thể đóng băng số token đó không? — Đức hỏi dồn.",
            "Ngọc Bích lắc đầu, ánh mắt lộ vẻ nghiêm trọng.",
            "— GateVortex là sàn giao dịch quốc tế có máy chủ đặt tại nước ngoài, họ hoàn toàn phớt lờ các yêu cầu pháp lý thông thường từ Việt Nam.",
            "— Hơn nữa, Hùng đã dùng chữ ký số hợp lệ của công ty để thực hiện giao dịch, về mặt pháp lý trên blockchain, đó là giao dịch hợp pháp.",
            "— Nếu không có bằng chứng kỹ thuật chứng minh chữ ký số bị giả mạo và private key bị đánh cắp, chúng tôi không thể can thiệp.",
            "Đức mở lại màn hình laptop, gõ một dòng lệnh hiển thị cấu trúc mã nguồn của hợp đồng thông minh NexaSphere.",
            "— Tôi có bằng chứng, — Đức nói, giọng lạnh lùng.",
            "— Tôi đã cài một hàm kiểm tra tính toàn vẹn của chữ ký số trong smart contract.",
            "— Nếu chữ ký số được tạo ra từ private key bị sao chép bất hợp pháp bằng camera hoặc thiết bị ngoại vi, nó sẽ để lại một sai số nhỏ trong hàm băm sha-256.",
            "— Sai số này cực kỳ nhỏ, chỉ có tôi mới giải mã được.",
            "Ngọc Bích nhìn thẳng vào mắt Đức, ánh mắt cô đầy vẻ kinh ngạc trước sự chuẩn bị xa trông rộng của chàng kỹ sư trẻ.",
            "— Xuất sắc, — Bích nói, gật đầu đánh giá cao.",
            "— Tôi cần anh hợp tác với A05 với tư cách là cố vấn công nghệ đặc biệt.",
            "— Chúng ta sẽ lập chuyên án chung. Tôi cho anh quyền lực pháp lý và hạ tầng mạng của Bộ Công an.",
            "— Còn anh, anh phải giúp chúng tôi vạch trần đường dây rửa tiền của GateVortex và lấy lại những gì đã mất.",
            "Đức nhìn ra ngoài cửa sổ, cơn mưa ngoài phố Nguyễn Huệ đã bắt đầu ngớt, để lộ những ánh đèn neon rực rỡ phản chiếu trên mặt đường.",
            "Anh quay lại nhìn Ngọc Bích, đưa bàn tay gầy gò nhưng rắn rỏi ra.",
            "— Tôi đồng ý. Tôi sẽ khiến Lâm Thế Hùng phải trả giá đắt gấp trăm lần những gì hắn đã gây ra.",
            "Ngọc Bích siết chặt tay anh, ánh mắt cô kiên định như thép nguội.",
            "— Chào mừng anh đến với chuyên án. Xe của A05 đang chờ bên ngoài. Chúng ta đi thôi."
        ]
        
        c3 = [
            "Trụ sở làm việc của Cục An ninh mạng A05 tại TP.HCM nằm trong một tòa nhà nghiêm trang trên đường Nguyễn Trãi, Quận 1.",
            "Đức bước theo Ngọc Bích qua ba lớp cửa an ninh quét vân tay và mống mắt, tiến vào phòng tác chiến công nghệ cao của chuyên án.",
            "Căn phòng rộng lớn ngập tràn ánh sáng xanh dương dịu mắt từ hàng chục màn hình máy tính cỡ lớn.",
            "Hơn mười chiến sĩ an ninh mạng trẻ tuổi mặc cảnh phục, tay gõ phím liên hồi, gương mặt tập trung cao độ.",
            "Giữa phòng là một bàn điều khiển trung tâm hiển thị bản đồ địa lý các cuộc tấn công mạng thời gian thực và luồng dữ liệu IP.",
            "— Mọi người dừng lại một chút, — Ngọc Bích dõng dạc nói, giọng cô vang lên đầy uy quyền khắp căn phòng.",
            "— Đây là anh Trương Minh Đức, cố vấn công nghệ đặc biệt của chuyên án từ hôm nay. Mọi người hỗ trợ anh ấy tối đa.",
            "Các chiến sĩ đồng loạt đứng dậy chào, ánh mắt tò mò nhìn chàng dev gầy gò trong bộ quần áo sũng nước vừa bước vào.",
            "Đức không lãng phí một giây nào. Anh bước thẳng đến bàn điều khiển trung tâm, cắm chiếc USB của mình vào cổng kết nối.",
            "— Cho tôi quyền truy cập vào cổng giám sát ví blockchain của sàn GateVortex, — Đức yêu cầu, giọng nói đã lấy lại sự tự tin của một thiên tài.",
            "Ngọc Bích gật đầu với lập trình viên trưởng của đội. — Cấp quyền tối cao cho anh Đức.",
            "Màn hình lớn lập tức chuyển sang giao diện theo dõi ví nóng (hot wallet) của sàn GateVortex.",
            "Dòng tiền từ ví chứa 500 tỷ token NexaSphere bị cướp của Đức đang hiển thị dưới dạng một chấm đỏ nhấp nháy liên tục.",
            "Chấm đỏ này đang di chuyển qua một loạt ví phụ, chuẩn bị đi vào bể thanh khoản (liquidity pool) của sàn.",
            "— Hắn đang dùng kỹ thuật 'bóc vỏ hành' (peeling chain) để chia nhỏ dòng tiền, — Đức phân tích, ngón tay chỉ vào các nút mạng.",
            "— Cứ mỗi năm phút, mười phần trăm số token sẽ được swap sang USDT để xóa dấu vết dòng tiền gốc.",
            "— Nếu toàn bộ số token đi vào bể thanh khoản, chúng ta sẽ hoàn toàn mất dấu vết do cơ chế trộn giao dịch của GateVortex.",
            "Ngọc Bích khoanh tay trước ngực, chân mày thanh tú nhíu chặt lại đầy lo lắng.",
            "— Chúng ta còn bao nhiêu thời gian trước khi hắn swap hết số token đó? — Bích hỏi.",
            "— Chính xác là ba mươi sáu tiếng, — Đức trả lời, ánh mắt sắc như dao găm.",
            "— Nhưng vấn đề lớn hơn là GateVortex vừa kích hoạt cơ chế multisig 3-of-5 cho ví chứa tài sản của NexaSphere.",
            "— Nghĩa là muốn đóng băng hoặc rút tiền ra, cần phải có chữ ký của ba trong năm khóa riêng nằm ở ba máy chủ khác nhau trên thế giới.",
            "— Lâm Thế Hùng nắm một khóa, GateVortex nắm ba khóa ở Singapore, Tokyo, và Zurich. Khóa còn lại thuộc về một quỹ đầu tư bóng tối ở Cayman.",
            "Lập trình viên trưởng của A05, Đại úy Nguyễn Hoàng Minh, thở dài vẻ bế tắc.",
            "— Hack vào ba máy chủ bảo mật của một sàn giao dịch quốc tế trong ba mươi sáu tiếng là nhiệm vụ bất khả thi.",
            "— Hệ thống tường lửa của họ là Cloudflare Enterprise kết hợp với phần cứng bảo mật HSM chuyên dụng.",
            "Đức khẽ nở nụ cười nửa miệng, ánh mắt lộ rõ vẻ ngạo nghễ của một kẻ đứng trên đỉnh cao công nghệ.",
            "Anh quay lại nhìn Ngọc Bích và các chiến sĩ an ninh mạng trong phòng.",
            "— Đối với người khác thì bất khả thi, nhưng đối với tôi thì không, — Đức nói, giọng điệu vô cùng tự tin.",
            "— Khi viết smart contract cho NexaSphere năm xưa, tôi đã phát hiện ra một lỗi logic trong thư viện mã hóa của GateVortex khi họ tích hợp với giao thức của chúng tôi.",
            "— Họ đã sử dụng một phiên bản OpenSSL cũ chứa lỗ hổng tràn bộ đệm chưa được công bố công khai.",
            "— Tôi có thể viết một script khai thác (exploit script) để đánh lừa máy chủ của họ, tự động ký duyệt giao dịch rút tiền mà không cần cả ba khóa riêng.",
            "Cả căn phòng tác chiến xôn xao. Đại úy Minh trố mắt nhìn Đức như nhìn một sinh vật ngoài hành tinh.",
            "— Anh định hack ngược cả sàn giao dịch crypto quốc tế sao? — Minh lắp bắp hỏi.",
            "— Đúng thế, — Đức lạnh lùng đáp. — Lâm Thế Hùng cướp của tôi bằng thủ đoạn hèn hạ, tôi sẽ lấy lại bằng công nghệ tối cao.",
            "— Tôi sẽ hack ngược toàn bộ ví nóng của GateVortex, đóng băng dòng tiền và rút sạch số token bị cướp về ví của Bộ Công an.",
            "Ngọc Bích nhìn Đức, ánh mắt cô lóe lên tia nhìn sắc sảo đầy quyết đoán.",
            "Cô đặt tay lên vai anh, cảm nhận được ý chí mạnh mẽ đang rung lên trong cơ thể gầy gò ấy.",
            "— Tốt lắm. Hãy bắt đầu đi. Tôi sẽ chịu mọi trách nhiệm về mặt pháp lý và ngoại giao cho cú hack này.",
            "— Nhưng trước hết, anh Đức, anh cần phải chứng minh cho cả đội thấy anh có khả năng thực hiện điều đó.",
            "— Chúng tôi có một thử thách dành cho anh để kiểm tra thực lực. Anh có dám nhận không?"
        ]
        
        # Save to temp JSON
        data = {
            "idx": 13,
            "title": "Thiên Tài Blockchain Phố Nguyễn Huệ: Bị Cướp Token Nghìn Tỷ, Tôi Hack Ngược Cả Sàn",
            "author": "Trương Minh Đức",
            "genre": "Sảng Văn",
            "intro": intro,
            "chapters": [
                {"title": "Chương 1: Bị Đuổi Khỏi Căn Penthouse Phố Nguyễn Huệ", "content": wrap_sentences(c1)},
                {"title": "Chương 2: Cuộc Gặp Định Mệnh Dưới Đèn Neon Phố Đi Bộ", "content": wrap_sentences(c2)},
                {"title": "Chương 3: Dấu Vết Số Trên Blockchain", "content": wrap_sentences(c3)}
            ]
        }
        
        with open(TEMP_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print("Stage 1 completed successfully. Temp file created.")

if __name__ == "__main__":
    main()
