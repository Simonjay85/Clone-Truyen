# -*- coding: utf-8 -*-
import json
import os

def generate_novel():
    title = "Trưởng Phòng Bán Hàng Khinh Nhân Viên Mới, Nhân Viên Đó Là Chuyên Gia Tư Vấn Của Tập Đoàn Mẹ"
    subtitle = "Bão Văn Phòng"
    author = "Đông Hải Cư Sĩ"
    genre = "Sảng Văn"
    
    intro_sentences = [
        "Trần Minh Hoàng, ba mươi lăm tuổi, một chuyên gia xoay chuyển tình thế doanh nghiệp lừng danh từng vực dậy hàng chục tập đoàn lớn, quyết định ẩn thân làm nhân viên bán hàng thử việc tại một chi nhánh siêu thị đang thua lỗ ở thành phố Thành Tâm.",
        "Tại chi nhánh Vạn An Plaza, Trưởng phòng bán hàng Đỗ Văn Thắng lạm quyền, liên tục nhận huê hồng từ nhà cung cấp và cấu kết rút ruột công quỹ hàng chục tỷ đồng mỗi năm của tập đoàn.",
        "Hắn coi khinh Hoàng là kẻ nghèo hèn hết thời, bắt anh bốc vác hàng hóa nặng nhọc, dọn dẹp rác thải và liên tục sỉ nhục anh trước toàn thể nhân viên chi nhánh.",
        "Nhưng Thắng không hề biết rằng, chiếc laptop cũ kỹ của gã nhân viên mới chứa đựng toàn bộ dữ liệu kiểm toán hệ thống ERP tối mật của tập đoàn mẹ.",
        "Bắt tay cùng Lê Mai Chi - vị Giám đốc Pháp chế sắc sảo, kiêu hãnh và vô cùng thực tế của tập đoàn, Hoàng từng bước giăng ra tấm lưới pháp lý hoàn hảo.",
        "Anh biến buổi họp tổng kết năm và thương vụ M&A trăm tỷ thành nơi phán quyết tàn khốc nhất cuộc đời gã trưởng phòng tham lam."
    ]
    intro = "".join([f"<p>{s}</p>\n" for s in intro_sentences])
    
    cover_prompt = "A high-end book cover, highly detailed web novel illustration style, a handsome and sharp Vietnamese corporate auditor in a dark navy blue suit standing confidently inside a modern luxury glass office overlooking a glittering city skyline at dusk. Professional and elite look, high-stakes boardroom tension. Cinematic lighting, rich dramatic shadows, premium colors."
    
    # Chapter 1: Người Mới Bí Ẩn
    c1 = [
        "Dưới cái nắng oi bức như thiêu như đốt của mùa hè miền Nam, không khí bên trong kho hàng số ba của chi nhánh Vạn An Plaza tại trung tâm thành phố Thành Tâm ngột ngạt đến mức khó thở.",
        "Trần Minh Hoàng lặng lẽ đẩy chiếc xe kéo bằng sắt bám đầy rỉ sét, trên xe chất cao như núi những thùng sữa nguyên kem nhập khẩu nặng trĩu.",
        "Bộ quần áo bảo hộ lao động màu xanh xám rộng thùng thình bám đầy bụi xi măng và vết dầu mỡ đen kịt làm che đi vóc dáng cao ráo của một người đàn ông ba mươi lăm tuổi.",
        "Mồ hôi lạnh chảy dài dọc sau gáy anh, thấm đẫm chiếc áo phông mỏng bên trong, nhưng đôi mắt sau cặp kính bảo hộ chống bụi vẫn giữ nguyên sự tĩnh lặng và sắc bén.",
        "Anh từng là chuyên gia xoay chuyển tình thế doanh nghiệp hàng đầu Đông Nam Á, người từng vực dậy những tập đoàn bán lẻ bờ vực phá sản tại Singapore và Hồng Kông.",
        "Hôm nay, anh xuất hiện ở đây với tư cách là một nhân viên thử việc thử thách ba mươi ngày, một thân phận ngụy trang hoàn hảo để điều tra đường dây tham nhũng nội bộ.",
        "Tiếng bước chân huỳnh huỵch cắt ngang không gian yên ắng của kho hàng, đi kèm với đó là giọng nói khàn khàn vì khói thuốc lá ngoại của Đỗ Văn Thắng.",
        "Đỗ Văn Thắng, Trưởng phòng bán hàng của Vạn An Plaza Thành Tâm, bước vào kho với bộ vest màu xám bóng lộn nhưng đường may cẩu thả, thắt lưng da cá sấu giả vàng choe choét.",
        "Gã đàn ông ngoài bốn mươi tuổi có chiếc bụng phệ vượt mặt, khuôn mặt bóng dầu đầy vẻ khinh khỉnh đang cầm điếu thuốc lá cháy dở chỉ trỏ vào mặt các công nhân.",
        "Thắng dừng lại ngay trước chiếc xe kéo của Hoàng, nhướng mày nhìn bảng tên nhân viên thử việc cài lệch trên ngực áo anh rồi nhổ một bãi nước bọt xuống sàn bê tông.",
        "Hắn cười khẩy, giọng điệu đầy sự chế giễu và khinh miệt: 'Mày là Trần Minh Hoàng, gã nhân viên mới ba mươi lăm tuổi đầu vẫn phải đi xin việc thử việc lương ba cọc ba đồng hả?'",
        "Hoàng không trả lời, anh chỉ khẽ cúi đầu để che đi ánh mắt lạnh lùng đang quét qua chiếc đồng hồ Rolex fake trên cổ tay Thắng.",
        "Thắng thấy Hoàng im lặng thì càng tỏ ra hống hách, hắn tiến lại gần gõ mạnh ngón tay thô kệch đầy nhẫn vàng vào vai Hoàng.",
        "Hắn quát lớn: 'Ở cái chi nhánh này, tao là luật, tao là người quyết định chén cơm của loại rác rưởi hết thời như mày có được đổ đầy hay không.'",
        "Hắn chỉ tay về phía góc kho nơi chất đống hàng trăm thùng hàng tiêu dùng nhanh bám đầy bụi bẩn và mạng nhện.",
        "Hắn ra lệnh: 'Chiều nay, một mình mày phải bốc xếp toàn bộ năm tấn hàng đó vào kho lạnh số hai, sau đó phân loại thủ công năm ngàn tờ hóa đơn nhập kho cũ.'",
        "Hắn hăm dọa: 'Nếu trước sáu giờ tối mà không xong, tao sẽ lập tức ký quyết định sa thải mày vì tội không hoàn thành nhiệm vụ và trừ sạch lương thử việc.'",
        "Hoàng vẫn giữ vẻ điềm tĩnh đáng kinh ngạc, anh khẽ gật đầu rồi trả lời bằng giọng trầm ấm: 'Tôi đã rõ thưa Trưởng phòng Đỗ, tôi sẽ hoàn thành đúng hạn.'",
        "Thắng khinh bỉ hừ một tiếng, quay lưng bỏ đi cùng đám thuộc cấp nịnh bợ, không quên buông lại một câu chửi thề đầy tục tĩu.",
        "Ngay khi bóng dáng của Thắng khuất sau cánh cửa sắt, sự nhún nhường trên khuôn mặt Hoàng lập tức biến mất, thay vào đó là vẻ lạnh lùng của một sát thủ tài chính.",
        "Anh bắt tay vào công việc bốc xếp, nhưng thay vì chỉ lao động tay chân, bộ não thiên tài của anh bắt đầu ghi nhận và phân tích từng chi tiết nhỏ.",
        "Anh nhận thấy toàn bộ vỏ thùng các-tông của nhà cung ứng Gia Hưng đều có dấu hiệu bị rạch niêm phong cũ và dán đè bằng băng keo rẻ tiền.",
        "Hoàng lấy ra một hộp sữa ngẫu nhiên trong thùng, phát hiện hạn sử dụng in trên bao bì sản phẩm thực chất chỉ còn chưa đầy mười lăm ngày.",
        "Trong khi đó, theo quy trình chuẩn của tập đoàn mẹ Vạn An Group, toàn bộ hàng hóa nhập kho bắt buộc phải có hạn sử dụng trên tám mươi phần trăm.",
        "Anh dùng chiếc điện thoại cũ của mình chụp lại mã vạch sản phẩm, số lô sản xuất và vết băng keo dán đè làm bằng chứng.",
        "Rõ ràng, Đỗ Văn Thắng đã cấu kết với nhà cung ứng Gia Hưng để nhập hàng cận hạn sử dụng với giá rẻ mạt như cho, sau đó nâng khống hóa đơn để đút túi chênh lệch.",
        "Hoàng lặng lẽ đi về phía bàn làm việc tạm thời ở góc kho, rút từ chiếc balo rách nát một chiếc iPad cũ kỹ nhưng đã được nâng cấp phần cứng đặc biệt.",
        "Anh truy cập vào cổng thông tin nội bộ của hệ thống ERP toàn tập đoàn bằng tài khoản quản trị ẩn danh cấp cao nhất mà Hội đồng quản trị cấp riêng.",
        "Những dòng dữ liệu tài chính của chi nhánh Thành Tâm hiện ra với hàng loạt chấm đỏ cảnh báo nguy hiểm từ hệ thống kiểm toán tự động.",
        "Biên lợi nhuận ròng của mảng bán lẻ tại đây đã sụt giảm nghiêm trọng từ mười hai phần trăm xuống chỉ còn chưa đầy hai phần trăm trong hai quý gần nhất.",
        "Đồng thời, chi phí chiết khấu thương mại và huê hồng trả cho các đơn vị trung gian lại tăng vọt một cách bất thường lên tới ba mươi phần trăm.",
        "Tổng số tiền thất thoát ước tính từ các giao dịch đáng ngờ của Đỗ Văn Thắng và đồng bọn đã vượt quá con số một trăm tỷ đồng.",
        "Hoàng đang tập trung phân tích dòng tiền chảy qua các tài khoản ngân hàng trung gian thì một tiếng động lớn vang lên từ phía cửa kho.",
        "Đỗ Văn Thắng bất ngờ quay lại kho hàng vì để quên chiếc bật lửa Dupont mạ vàng trên mặt bàn gỗ gần lối ra vào.",
        "Nhìn thấy gã nhân viên thử việc nghèo hèn đang sử dụng một chiếc máy tính bảng đắt tiền để xem các số liệu tối mật, mắt Thắng trợn trừng giận dữ.",
        "Hắn lao tới như một con lợn rừng điên tiết, giật mạnh chiếc iPad trên tay Hoàng và ném thẳng xuống sàn bê tông lạnh lẽo.",
        "Tiếng rắc chát chúa vang lên, màn hình chiếc iPad vỡ nát thành trăm mảnh thủy tinh li ti, các linh kiện bên trong văng tung tóe.",
        "Thắng không dừng lại ở đó, hắn dùng gót giày da bóng lộn giẫm đạp liên tiếp lên đống đổ nát cho đến khi chiếc máy hoàn toàn biến dạng.",
        "Hắn gầm lên đầy ác ý: 'Một thằng bốc vác quèn lương ngày hai trăm nghìn mà dám ăn cắp tài liệu tối mật của công ty bằng máy tính bảng hả?'",
        "Hắn nhổ nước bọt vào đống đổ nát rồi chỉ thẳng vào mặt Hoàng: 'Mày định dùng cái này để chụp ảnh sổ kho đi bán cho đối thủ cạnh tranh đúng không?'",
        "Hắn cười khẩy, dí sát khuôn mặt đầy mùi rượu ngoại và khói thuốc vào Hoàng: 'Quỳ xuống! Quỳ xuống nhặt sạch từng mảnh vỡ này cho tao, nếu không tao gọi bảo vệ còng tay mày giao cho công an ngay lập tức!'",
        "Lúc này, các nhân viên kho khác cũng tụ tập lại xem, họ nhìn Hoàng bằng ánh mắt ái ngại nhưng không một ai dám lên tiếng bảo vệ anh vì sợ uy quyền của Thắng.",
        "Mười ngón tay của Trần Minh Hoàng bấm chặt vào lòng bàn tay đến mức đầu móng tay trắng bệch, một vệt máu đỏ tươi khẽ rỉ ra từ lòng bàn tay anh.",
        "Gân xanh nổi lên cuồn cuộn trên vầng trán rộng, đôi mắt anh lóe lên những tia nhìn sắc bén như có thể đâm xuyên qua lá gan của đối thủ.",
        "Tuy nhiên, sự rèn luyện khắc nghiệt trong giới tài chính quốc tế đã giúp anh giữ được sự bình tĩnh tuyệt đối vào những thời khắc quyết định.",
        "Anh biết rằng, nếu bây giờ anh ra tay đánh gã trưởng phòng ngu xuẩn này, toàn bộ kế hoạch bắt trọn đường dây tham nhũng nghìn tỷ sẽ bị đổ bể.",
        "Hoàng từ từ hạ thấp trọng tâm, lặng lẽ ngồi xổm xuống sàn bê tông lạnh lẽo, dùng những ngón tay trần nhặt từng mảnh kính sắc nhọn của chiếc máy tính vỡ.",
        "Một mảnh kính bén ngót cắt sâu vào ngón trỏ của anh, máu đỏ tươi chảy ra, thấm đẫm lên mảnh linh kiện điện tử dập nát.",
        "Thắng đứng trên cao nhìn xuống, cười ngặt nghẽo đầy đắc ý như một vị vua đang ngự trị trên ngai vàng quyền lực tối thượng.",
        "Hắn đá nhẹ mũi giày vào tay Hoàng, giọng điệu vô cùng hả hê: 'Nhặt cho sạch vào, loại rác rưởi thì mãi mãi chỉ là rác rưởi dưới chân tao mà thôi!'",
        "Hoàng không nói một lời nào, anh lặng lẽ gom toàn bộ mảnh vỡ vào lòng bàn tay, trong đầu thầm đếm ngược thời gian tàn lụi của Đỗ Văn Thắng.",
        "Anh biết rõ rằng, đằng sau sự kiêu ngạo vô tri của Thắng là cả một hệ thống tham nhũng bám rễ sâu sắc từ cấp phó giám đốc chi nhánh.",
        "Chỉ cần thêm vài ngày nữa, khi toàn bộ dữ liệu dòng tiền từ ngân hàng Techcombank được đối chiếu đầy đủ, anh sẽ khiến kẻ này phải trả giá bằng cả mạng sống và tự do của hắn.",
        "Tiếng cười ngạo nghễ của Đỗ Văn Thắng vẫn vang vọng khắp kho hàng số ba, nhưng hắn không hề biết rằng, cái bẫy chết chóc đã bắt đầu siết chặt quanh cổ hắn.",
        "Trần Minh Hoàng đứng dậy, ném đống mảnh vỡ vào thùng rác, ánh mắt anh hướng về phía tòa nhà hành chính của Vạn An Plaza với một kế hoạch phản công tàn khốc.",
        "Anh quay trở lại xe kéo, tiếp tục bốc những thùng sữa ngoại nhập với một nhịp độ đều đặn, như thể chưa từng có biến cố gì xảy ra.",
        "Máu trên ngón tay anh đã ngừng chảy, nhưng ngọn lửa phẫn nộ và quyết tâm quét sạch những u nhọt của doanh nghiệp trong anh đang bùng cháy dữ dội hơn bao giờ hết.",
        "Anh biết mình không hề cô độc trong cuộc chiến này, bởi vì tối nay, một nhân vật vô cùng quan trọng từ tập đoàn mẹ sẽ có mặt tại thành phố Thành Tâm.",
        "Đó sẽ là người cùng anh ký kết một bản hợp đồng sòng phẳng, mở đường cho chiến dịch thanh trừng tàn khốc nhất lịch sử ngành bán lẻ Việt Nam.",
        "Trần Minh Hoàng mỉm cười lạnh lùng, bước chân anh vẫn vững chãi trên nền đất bụi bặm, hướng thẳng về phía ánh sáng le lói phía cuối kho hàng."
    ]
    
    # Chapter 2: Đồng Minh Sòng Phẳng
    c2 = [
        "Đêm Thành phố Thành Tâm lung linh dưới những ánh đèn neon đa sắc màu, nhưng bầu không khí bên trong phòng VIP bảo mật của tòa nhà Landmark 81 lại tĩnh lặng đến nghẹt thở.",
        "Trần Minh Hoàng đã tắm rửa sạch sẽ, trút bỏ bộ quần áo bảo hộ bám đầy bụi bặm để khoác lên mình chiếc áo sơ mi trắng đơn giản nhưng phẳng phiu.",
        "Anh ngồi đối diện với một người phụ nữ trẻ tuổi đang nhấp từng ngụm trà Earl Grey với phong thái vô cùng kiêu sa và thanh lịch.",
        "Lê Mai Chi, ba mươi tuổi, Giám đốc Pháp chế tối cao kiêm đại diện phần vốn góp của tập đoàn mẹ Vạn An Group, trông thật lộng lẫy trong bộ đồ công sở Chanel may đo riêng.",
        "Mái tóc đen nhánh của cô được búi cao gọn gàng, để lộ chiếc cổ kiêu ngạo cùng đôi khuyên tai ngọc trai đắt giá tỏa ra ánh sáng dịu nhẹ.",
        "Đôi mắt cô to tròn nhưng sắc sảo như hai lưỡi dao mổ, nhìn chằm chằm vào tập hồ sơ dày cộp mà Hoàng vừa đặt lên bàn kính.",
        "Mai Chi đặt tách trà xuống đĩa sứ với một tiếng động thanh mảnh cộp nhỏ, khẽ tựa lưng vào ghế sofa da cao cấp.",
        "Cô lên tiếng, giọng nói trong trẻo nhưng lạnh lùng và chứa đựng sự uy nghiêm của người nắm giữ quyền sinh sát pháp lý: 'Anh Hoàng, tôi bay từ Hà Nội vào đây không phải để nghe anh kể khổ về việc bị một gã trưởng phòng quèn bắt nạt.'",
        "Cô chỉ tay vào tập tài liệu: 'Tôi cần những con số thực tế, những bằng chứng thép có thể đưa Đỗ Văn Thắng và đồng bọn ra trước vành móng ngựa pháp luật mà không làm ảnh hưởng đến giá cổ phiếu của tập đoàn.'"
        "Hoàng mỉm cười nhẹ nhàng, anh đẩy chiếc máy tính xách tay ThinkPad dòng quân sự có độ bảo mật cao về phía cô.",
        "Anh giải thích: 'Đỗ Văn Thắng không đơn độc, hắn chỉ là cánh tay nối dài của Phó Giám đốc chi nhánh Vương Đại Hải và một nhóm cổ đông nhỏ lẻ tại địa phương.'",
        "Anh gõ nhẹ ngón tay lên màn hình hiển thị sơ đồ dòng tiền: 'Họ đã cài đặt một backdoor tinh vi vào hệ thống ERP chạy trên nền tảng SAP của chi nhánh.'",
        "Hoàng nhấn mạnh: 'Mỗi đêm, lúc hai giờ sáng, hệ thống tự động chạy một đoạn mã script để xóa sạch dấu vết của khoảng mười lăm phần trăm lượng hàng hóa xuất kho không hóa đơn.'",
        "Anh tiếp tục: 'Số hàng hóa này được tuồn ra ngoài bán cho chuỗi cửa hàng đại lý của công ty Gia Hưng, một doanh nghiệp do em ruột Đỗ Văn Thắng đứng tên sở hữu.'",
        "Anh đưa ra bằng chứng: 'Dòng tiền sau đó được rửa sạch thông qua việc mua khống hóa đơn GTGT của các công ty ma, rồi chảy ngược vào tài khoản cá nhân của Thắng tại ngân hàng Techcombank Chi nhánh Thành Tâm.'",
        "Mai Chi chăm chú lắng nghe, đôi lông mày thanh tú khẽ nhíu lại khi nhận ra quy mô khủng khiếp của đường dây rút ruột công quỹ này.",
        "Cô nhìn thẳng vào mắt Hoàng, đặt điều kiện một cách vô cùng sòng phẳng và thực tế, không hề có chút kiêng nể nào.",
        "Cô nói: 'Anh Hoàng, chúng ta là những người làm kinh tế chuyên nghiệp, tôi không tin vào những lời hứa hẹn suông hay lòng trung thành vô điều kiện.'",
        "Cô đưa ra điều kiện: 'Nếu tôi đồng ý cấp cho anh quyền kiểm soát tuyệt đối ban nhân sự và ban tài chính của chi nhánh Thành Tâm, anh phải ký vào bản cam kết hiệu suất KPI đặc biệt này.'",
        "Cô đẩy một bản hợp đồng pháp lý dày hai mươi trang sang phía anh: 'Thứ nhất, anh phải đảm bảo tỷ lệ nợ xấu của chi nhánh giảm xuống dưới ba phần trăm trong vòng sáu tháng.'",
        "Cô tiếp tục: 'Thứ hai, biên lợi nhuận ròng của chi nhánh phải tăng thêm ít nhất năm phần trăm ngay trong quý đầu tiên sau khi tái cấu trúc.'",
        "Cô nhấn mạnh điều khoản cuối cùng: 'Và quan trọng nhất, sau khi dọn dẹp sạch sẽ đống rác rưởi này, tôi phải được quyền sở hữu năm phần trăm cổ phần ưu đãi biểu quyết của chi nhánh Thành Tâm từ phần vốn thu hồi.'"
        "Hoàng nhìn lướt qua các điều khoản trong hợp đồng, ánh mắt anh lóe lên sự tán thưởng dành cho sự thông minh và thực tế của người phụ nữ đối diện.",
        "Anh hiểu rằng, trong giới kinh doanh đỉnh cao, chỉ có những điều kiện sòng phẳng và lợi ích ràng buộc chặt chẽ mới tạo nên một liên minh bền vững nhất.",
        "Anh rút chiếc bút máy Montblanc từ túi áo, không hề do dự mà ký tên mình xuống dưới trang cuối cùng của bản hợp đồng.",
        "Hoàng đặt bút xuống, nhìn thẳng vào Mai Chi: 'Rất sòng phẳng, tôi đồng ý với tất cả các điều khoản của cô, Giám đốc Lê.'",
        "Anh nói thêm: 'Nhưng tôi cũng có một yêu cầu bắt buộc: Tập đoàn mẹ phải cử một đội kiểm toán pháp lý độc lập từ Hà Nội vào đây dưới sự điều hành trực tiếp của cô.'",
        "Anh giải thích: 'Chúng ta cần một đòn đánh bất ngờ và toàn diện, không cho Vương Đại Hải và Đỗ Văn Thắng bất kỳ cơ hội nào để tẩu tán tài sản hay tiêu hủy dữ liệu máy chủ.'",
        "Mai Chi khẽ gật đầu, nụ cười kiêu sa xuất hiện trên đôi môi đỏ mọng của cô: 'Anh yên tâm, đội kiểm toán của tôi đã sẵn sàng xuất phát ngay khi có tín hiệu từ anh.'",
        "Cô đứng dậy, chủ động đưa bàn tay thon thả ra phía trước để bắt tay anh: 'Hợp tác vui vẻ, anh Hoàng. Hãy cho tôi thấy năng lực thật sự của chuyên gia xoay chuyển tình thế hàng đầu.'"
        "Hoàng đứng dậy bắt tay cô, cảm nhận được sự kiên quyết và bản lĩnh từ cái nắm tay của người phụ nữ sắc sảo này.",
        "Hai người bắt đầu thảo luận chi tiết về kế hoạch giăng lưới, từng bước đi được tính toán tỉ mỉ như trên một bàn cờ vua quốc tế.",
        "Hoàng phân tích: 'Đỗ Văn Thắng là kẻ kiêu ngạo nhưng thiếu tầm nhìn, hắn chắc chắn sẽ tìm cách đuổi tôi đi khi phát hiện tôi đang điều tra sổ sách.'",
        "Anh tiếp tục: 'Hắn sẽ dùng những thủ đoạn bẩn thỉu nhất để vu khống tôi, và đó chính là thời cơ tốt nhất để chúng ta dụ rắn ra khỏi hang.'",
        "Mai Chi đồng tình: 'Tôi sẽ đóng vai người đứng ngoài cuộc, giả vờ không quan tâm đến các báo cáo của chi nhánh để khiến Vương Đại Hải chủ quan.'",
        "Cô nói thêm: 'Chúng ta sẽ để chúng tự đắc ý cho đến ngày diễn ra đại hội tổng kết năm và công bố thương vụ M&A với quỹ đầu tư Singapore.'",
        "Hoàng mỉm cười lạnh lùng: 'Đó sẽ là ngày mà Đỗ Văn Thắng nghĩ rằng hắn sẽ bước lên đỉnh cao sự nghiệp, nhưng thực chất là bước xuống địa ngục của luật pháp.'",
        "Hai người tiếp tục hoàn thiện các chi tiết nhỏ nhất của kế hoạch cho đến khi kim đồng hồ chỉ sang ba giờ sáng.",
        "Mai Chi tiễn Hoàng ra cửa phòng VIP, ánh mắt cô nhìn theo bóng lưng vững chãi của anh khuất dần sau hành lang thang máy.",
        "Cô biết rằng, canh bạc này cực kỳ nguy hiểm, nhưng nếu thành công, cô và tập đoàn mẹ sẽ thu hồi được hàng trăm tỷ đồng thất thoát và sở hữu một chi nhánh siêu thị hiệu quả nhất cả nước.",
        "Trong khi đó, Trần Minh Hoàng bước ra khỏi tòa nhà Landmark 81, đón nhận luồng gió lạnh từ sông Sài Gòn thổi vào khuôn mặt anh.",
        "Vết thương trên ngón tay anh vẫn còn hơi nhói, nhưng trong lòng anh đã tràn đầy sự tự tin về một chiến thắng oanh liệt.",
        "Anh biết Đỗ Văn Thắng sẽ không để anh yên trong những ngày tới, nhưng anh đã sẵn sàng đối mặt với mọi âm mưu hèn hạ nhất của đối thủ.",
        "Bước chân anh rảo nhanh trên con đường vắng lặng của thành phố Thành Tâm, hướng về phía khu nhà trọ nghèo nàn nơi anh đang ẩn mình.",
        "Cuộc chiến văn phòng này không chỉ là để đòi lại công lý cho bản thân, mà còn là để chứng minh rằng trí tuệ và sự sòng phẳng luôn là vũ khí tối thượng trước mọi sự tham lam vô độ.",
        "Anh mỉm cười, một nụ cười đầy bí ẩn và lạnh lùng, báo hiệu cho một cơn bão kinh hoàng sắp sửa quét qua chi nhánh Vạn An Plaza Thành Tâm.",
        "Mọi quân cờ đã được đặt vào đúng vị trí của chúng trên bàn cờ định mệnh.",
        "Bây giờ, chỉ còn chờ đợi quân tốt đầu tiên tiến lên để kích hoạt toàn bộ hệ thống bẫy rập tàn khốc mà anh và Lê Mai Chi đã dày công thiết lập.",
        "Trần Minh Hoàng nhắm mắt lại để tận hưởng sự yên bình cuối cùng trước khi cơn bão tài chính chính thức đổ bộ vào ngày mai.",
        "Anh biết rõ rằng, kẻ kiêu ngạo Đỗ Văn Thắng sẽ sớm phải quỳ gối dưới chân anh để cầu xin sự dung thứ trong vô vọng."
    ]
    
    # Chapter 3: Lưới Sắt Bủa Vây
    c3 = [
        "Sáng thứ Hai tuần kế tiếp, bầu không khí tại văn phòng hành chính của Vạn An Plaza Thành Tâm căng thẳng như một sợi dây đàn bị kéo căng hết cỡ.",
        "Trần Minh Hoàng vừa bước vào phòng làm việc của ban bán hàng thì nhận ra hàng chục ánh mắt của đồng nghiệp đang nhìn mình với vẻ né tránh và khinh bỉ.",
        "Ở giữa phòng, Đỗ Văn Thắng đang đứng khoanh tay, khuôn mặt bừng bừng sát khí bên cạnh gã Phó Giám đốc chi nhánh Vương Đại Hải.",
        "Vương Đại Hải là một người đàn ông trung niên hói đầu, mặc bộ vest màu xanh đậm đắt tiền, đôi mắt híp lại đầy vẻ xảo quyệt và gian trá.",
        "Thắng nhìn thấy Hoàng liền đập mạnh tay xuống bàn làm việc vang lên một tiếng rầm chát chúa, chỉ thẳng ngón tay thô kệch vào mặt anh.",
        "Hắn gầm lên: 'Trần Minh Hoàng! Mày gan to bằng trời, dám lẻn vào phòng kế toán kho ăn cắp năm trăm triệu đồng tiền quỹ bán hàng trong ngày!'",
        "Hoàng đứng im tại chỗ, nét mặt anh không hề có một chút hoảng sợ hay biến sắc nào, chỉ lặng lẽ nhìn chằm chằm vào Thắng.",
        "Anh bình thản hỏi: 'Trưởng phòng Đỗ, anh có bằng chứng gì để vu khống tôi ăn cắp một số tiền lớn như vậy?'",
        "Thắng cười khẩy đầy ngạo nghễ, hắn quay sang phía Vương Đại Hải rồi nói lớn để toàn bộ văn phòng cùng nghe rõ.",
        "Hắn quát: 'Bằng chứng hả? Két sắt của phòng kế toán bị mở bằng mã số nội bộ mà chỉ có những kẻ cố tình lục lọi hệ thống ERP như mày mới có thể bẻ khóa!'",
        "Hắn chỉ tay vào chiếc balo vải sờn cũ kỹ của Hoàng đang đặt trên ghế làm việc: 'Bảo vệ! Lục soát cái balo rác rưởi của nó cho tao!'",
        "Hai gã bảo vệ to khỏe lập tức lao tới, giật lấy chiếc balo của Hoàng và trút toàn bộ đồ đạc bên trong ra mặt bàn kính.",
        "Giữa đống quần áo lao động cũ kỹ và vài cuốn sổ ghi chép, một cọc tiền Techcombank mệnh giá năm trăm nghìn đồng còn nguyên niêm phong đỏ rơi ra.",
        "Thắng cầm cọc tiền lên, giơ cao trước mặt mọi người rồi cười lớn đầy hả hê: 'Đây là cái gì? Một trăm triệu đồng tiền mặt đứng tên ngân hàng Techcombank!'",
        "Hắn hét vào mặt Hoàng: 'Mày còn chối được nữa không? Thằng ăn cắp đê tiện! Hôm nay tao sẽ tiễn mày vào tù để mày biết thế nào là lễ độ!'",
        "Vương Đại Hải lúc này mới lên tiếng bằng giọng điệu đạo đức giả: 'Cậu Hoàng, chứng cứ rành rành thế này, tôi buộc phải đình chỉ công tác cậu và giao cho cơ quan công an xử lý.'",
        "Hải khẽ vẫy tay ra hiệu cho hai gã bảo vệ tiến lại gần định khống chế và còng tay Trần Minh Hoàng.",
        "Đúng lúc này, Trần Minh Hoàng bật cười, một tiếng cười trầm ấm nhưng chứa đựng sự khinh bỉ tột độ dành cho sự ngu xuẩn của đối thủ.",
        "Anh thong thả đút hai tay vào túi quần, đứng thẳng lưng với một phong thái vô cùng uy nghiêm và tự tin.",
        "Hoàng lên tiếng, giọng nói của anh vang dội khắp căn phòng, át đi mọi tiếng xì xào bàn tán của các nhân viên.",
        "Anh nói: 'Trưởng phòng Đỗ, Phó Giám đốc Vương, hai người đã dựng lên một vở kịch quá vụng về và đầy rẫy những lỗ hổng kỹ thuật.'",
        "Anh chỉ ngón tay vào cọc tiền trên tay Thắng: 'Thứ nhất, hệ thống két sắt phòng kế toán kho sử dụng khóa bảo mật hai lớp bằng vân tay của kế toán trưởng và mã OTP gửi về số điện thoại đăng ký.'",
        "Anh giải thích tiếp: 'Số điện thoại đăng ký nhận mã OTP đó chính là số cá nhân của anh, Đỗ Văn Thắng. Một nhân viên thử việc như tôi làm sao có được chiếc điện thoại của anh để lấy mã?'",
        "Khuôn mặt Đỗ Văn Thắng lập tức cứng đờ, nụ cười đắc ý trên môi gã tắt ngấm khi nghe Hoàng chỉ ra điểm vô lý này.",
        "Hoàng không dừng lại, anh rút chiếc điện thoại của mình ra, bấm nút kích hoạt một đoạn video ngắn rồi xoay màn hình về phía mọi người.",
        "Anh nói: 'Thứ hai, các người nghĩ rằng đã tắt toàn bộ hệ thống camera an ninh của chi nhánh để hành sự đúng không?'",
        "Anh cười lạnh: 'Các người quên mất rằng tôi đã tự tay lắp đặt một camera giám sát hành trình độc lập chạy bằng pin dự phòng ở góc kho lạnh.'",
        "Đoạn video trên màn hình điện thoại hiển thị rõ ràng cảnh một gã đàn ông bịt mặt, nhưng có vóc dáng và chiếc đồng hồ Rolex fake giống hệt Đỗ Văn Thắng.",
        "Gã đàn ông đó đang lén lút mở két sắt, lấy ra các cọc tiền rồi nhét một cọc vào chiếc balo của Hoàng vào lúc mười hai giờ đêm qua.",
        "Mồ hôi hột bắt đầu tuôn rơi trên trán Đỗ Văn Thắng, khuôn mặt gã chuyển từ đỏ gay sang xám ngoét như tro tàn.",
        "Hoàng tiến lên một bước, dồn Thắng vào góc bàn làm việc, ánh mắt anh sắc bén như muốn đâm xuyên qua tim gã.",
        "Anh nói tiếp bằng giọng lạnh lùng: 'Thứ ba, và cũng là điểm chí mạng nhất đối với các người.'",
        "Anh giải thích: 'Cọc tiền Techcombank trị giá một trăm triệu đồng này có dán nhãn số seri từ ngân hàng. Tôi đã tra cứu hệ thống giao dịch của Techcombank chi nhánh Thành Tâm.'",
        "Anh đưa ra tờ tài liệu in sẵn: 'Số seri này trùng khớp hoàn toàn với đợt rút tiền mặt trị giá hai tỷ đồng từ tài khoản cá nhân của anh vào lúc mười giờ sáng ngày thứ Sáu tuần trước.'",
        "Hoàng hỏi vặn: 'Anh Thắng, anh giải thích thế nào về việc tiền từ tài khoản cá nhân của anh lại tự động bò vào phòng kế toán rồi chui vào balo của tôi?'",
        "Toàn bộ văn phòng lặng đi như tờ, không một ai dám thở mạnh trước màn lật kèo kỹ thuật vô cùng ngoạn mục và tàn khốc của Trần Minh Hoàng.",
        "Vương Đại Hải đứng bên cạnh tái mặt, gã lập tức nhận ra mình đã đụng phải một đối thủ cực kỳ đáng sợ và có sự chuẩn bị vô cùng kỹ lưỡng.",
        "Hải khẽ ho khan một tiếng, cố gắng dùng quyền lực của mình để dập tắt sự việc trước khi nó vượt ra ngoài tầm kiểm soát.",
        "Hải nói giọng run rẩy: 'Có lẽ... có lẽ đây chỉ là một sự hiểu lầm nhỏ trong khâu quản lý kho bãi. Cậu Hoàng, cậu hãy cất điện thoại đi, chúng ta sẽ giải quyết nội bộ.'",
        "Hoàng cười khẩy đầy lạnh lùng: 'Giải quyết nội bộ sao? Muộn rồi, Phó Giám đốc Vương.'",
        "Anh tuyên bố: 'Toàn bộ dữ liệu video camera và hồ sơ giao dịch seri tiền của Techcombank đã được tôi gửi trực tiếp lên Ủy ban Kiểm tra tối cao của tập đoàn mẹ tại Hà Nội từ một tiếng trước.'",
        "Nghe đến đây, Đỗ Văn Thắng hoàn toàn sụp đổ, gã quỳ sụp xuống đất cộp một tiếng, đôi mắt trợn trừng đầy vẻ sợ hãi và tuyệt vọng.",
        "Gã biết rằng, một khi tập đoàn mẹ can thiệp, đường dây tham nhũng nghìn tỷ của gã và Vương Đại Hải sẽ bị phanh phui hoàn toàn.",
        "Vương Đại Hải thì lập tức lùi lại phía sau, vội vàng rút điện thoại ra để tìm kiếm sự cứu viện từ các thế lực chống lưng của gã.",
        "Nhưng Hoàng chỉ lặng lẽ nhìn họ với một ánh mắt khinh bỉ, anh biết rằng mọi nỗ lực giãy giụa của chúng lúc này đều vô ích.",
        "Anh cúi xuống nhặt chiếc balo sờn cũ của mình, đeo lên vai rồi thong thả bước ra khỏi phòng làm việc trước những ánh mắt kinh hoàng của toàn thể nhân viên.",
        "Màn phản công đầu tiên đã giành chiến thắng vang dội, bẻ gãy hoàn toàn đòn vu khống đê tiện của gã trưởng phòng tham lam.",
        "Nhưng Hoàng biết đây mới chỉ là màn khởi động cho trận chiến quyết định sẽ diễn ra vào ngày mai tại buổi họp tổng kết năm của chi nhánh.",
        "Anh rút điện thoại gửi một tin nhắn ngắn gọn cho Lê Mai Chi: 'Cá đã cắn câu, toàn bộ chứng cứ đã được xác lập hoàn hảo. Ngày mai bắt đầu thanh trừng.'",
        "Từ đầu dây bên kia, Mai Chi trả lời lập tức bằng một biểu tượng đồng ý đầy tự tin và sòng phẳng.",
        "Trần Minh Hoàng bước ra khỏi tòa nhà văn phòng, hít một hơi thật sâu bầu không khí trong lành của thành phố Thành Tâm.",
        "Anh biết rằng ngày mai, dưới ánh đèn của hội trường lớn, bộ mặt thật của những kẻ sâu mọt này sẽ bị phơi bày hoàn toàn trước bàn dân thiên hạ."
    ]
    
    # Chapter 4: Cuộc Họp Đại Hội Đồng
    c4 = [
        "Sáng hôm sau, khán phòng năm sao của khách sạn Rex tại trung tâm thành phố Thành Tâm được trang hoàng vô cùng lộng lẫy để tổ chức buổi họp tổng kết năm của Vạn An Plaza.",
        "Hàng trăm khách mời gồm các cổ đông lớn, đối tác kinh doanh và đặc biệt là phái đoàn đầu tư cấp cao đến từ quỹ ngoại Singapore đã có mặt đầy đủ.",
        "Thương vụ M&A chuyển nhượng bốn mươi chín phần trăm cổ phần của chi nhánh Thành Tâm dự kiến sẽ được ký kết ngay trong buổi sáng hôm nay.",
        "Đỗ Văn Thắng xuất hiện với vẻ mặt cố tỏ ra bình tĩnh, mặc bộ vest đen mới tinh, liên tục cúi đầu chào đón các đại diện quỹ ngoại.",
        "Hắn và Vương Đại Hải đã thỏa thuận ngầm với đối tác nước ngoài để bán rẻ tài sản chi nhánh, đổi lại là một khoản huê hồng trị giá năm triệu đô la Mỹ chảy vào tài khoản bí mật.",
        "Thắng tin rằng, chỉ cần thương vụ M&A này được ký kết thành công, gã sẽ lập tức được bổ nhiệm làm Giám đốc Điều hành mới của chi nhánh và xóa sạch mọi dấu vết tham nhũng cũ.",
        "Hắn bước lên bục phát biểu, tự tin trình chiếu kế hoạch kinh doanh và báo cáo tài chính với những con số doanh thu tăng trưởng ảo lên tới hai mươi phần trăm.",
        "Thắng dõng dạc nói qua micro: 'Nhờ vào sự quản lý hiệu quả của ban bán hàng, chi nhánh Thành Tâm đã đạt được những thành tựu vượt bậc và sẵn sàng cho bước nhảy vọt toàn cầu.'",
        "Bỗng nhiên, từ hàng ghế cuối cùng của khán phòng, một bóng người cao ráo đứng dậy, thong thả bước lên lối đi giữa hội trường.",
        "Trần Minh Hoàng vẫn mặc bộ quần áo nhân viên thử việc giản dị nhưng phong thái của anh lại toát ra một sự uy nghiêm đáng kinh ngạc.",
        "Nhìn thấy Hoàng, khuôn mặt Đỗ Văn Thắng lập tức co rúm lại vì giận dữ và lo sợ, gã hét lớn vào micro để át đi sự xuất hiện của anh.",
        "Thắng quát: 'Bảo vệ! Bảo vệ đâu? Tại sao lại để một gã bốc vác quèn, một kẻ ăn cắp quỹ của công ty lọt vào hội nghị cấp cao này?'",
        "Hắn chỉ thẳng tay vào Hoàng: 'Đuổi nó ra ngoài ngay lập tức! Đừng để loại rác rưởi này làm bẩn không gian sang trọng của các nhà đầu tư quốc tế!'",
        "Hai gã bảo vệ của khách sạn Rex lập tức tiến lại gần Hoàng, nhưng anh chỉ cần đưa tay lên ra hiệu dừng lại với một ánh mắt sắc lạnh như băng.",
        "Sự uy nghiêm tự nhiên của anh khiến hai gã bảo vệ lập tức khựng lại, không dám tiến thêm một bước nào vì cảm giác bị áp chế tinh thần tột độ.",
        "Hoàng lên tiếng, giọng nói trầm ấm nhưng vang dội không cần micro: 'Trưởng phòng Đỗ, anh vội vàng đuổi tôi đi như vậy là để che giấu những con số doanh thu ảo này đúng không?'",
        "Anh chỉ vào màn hình trình chiếu: 'Toàn bộ con số tăng trưởng hai mươi phần trăm này thực chất là từ việc ép các nhà cung cấp ký gửi hàng hóa khống để làm đẹp sổ sách trước ngày M&A.'",
        "Cả hội trường bắt đầu xôn xao bàn tán, các đại diện quỹ ngoại Singapore lập tức nhíu mày và yêu cầu giải thích rõ ràng.",
        "Vương Đại Hải ngồi ở hàng ghế danh dự lập tức đứng bật dậy, tức giận đập bàn quát lớn: 'Trần Minh Hoàng! Cậu chỉ là một nhân viên thử việc quèn, lấy tư cách gì để chất vấn ban giám đốc chi nhánh?'",
        "Đúng lúc sự căng thẳng đạt đến đỉnh điểm, cánh cửa gỗ lớn của khán phòng bất ngờ bị đẩy mạnh ra từ hai phía.",
        "Tiếng gót giày cao gót bằng da cao cấp nện xuống nền gạch đá hoa cương vang lên những âm thanh cộp cộp đầy uy lực và dứt khoát.",
        "Lê Mai Chi bước vào khán phòng với phong thái kiêu sa của một nữ hoàng, đi sau cô là đoàn thanh tra tối cao của tập đoàn mẹ cùng năm điều tra viên kinh tế của Bộ Công an.",
        "Mai Chi nhìn thẳng lên sân khấu, giọng nói trong trẻo nhưng chứa đựng sức mạnh pháp lý tối thượng vang lên.",
        "Cô nói lớn: 'Tôi là Lê Mai Chi, Giám đốc Pháp chế tối cao của tập đoàn mẹ Vạn An Group. Tôi trao cho anh ấy tư cách đó!'"
        "Cả khán phòng lập tức lặng đi, Đỗ Văn Thắng và Vương Đại Hải như bị sét đánh ngang tai, đứng chôn chân tại chỗ không thể tin vào mắt mình.",
        "Mai Chi thong thả bước lên sân khấu, đứng cạnh Trần Minh Hoàng và khẽ cúi đầu chào anh với một sự kính trọng tuyệt đối.",
        "Cô quay sang phía toàn thể cổ đông và đối tác nước ngoài, dõng dạc tuyên bố trước toàn thể hội nghị.",
        "Cô tuyên bố: 'Hội đồng quản trị tập đoàn mẹ quyết định đình chỉ toàn bộ chức vụ của Phó Giám đốc Vương Đại Hải và Trưởng phòng Đỗ Văn Thắng kể từ giây phút này.'",
        "Cô tiếp tục: 'Đồng thời, chúng tôi công bố thân phận thật sự của Trần Minh Hoàng - Chuyên gia Tư vấn tái cấu trúc tối cao được tập đoàn mẹ ủy quyền toàn quyền điều hành chi nhánh.'"
        "Tiếng la hét kinh ngạc vang dội khắp khán phòng năm sao, mọi ánh mắt khinh bỉ trước đó dành cho Hoàng lập tức chuyển thành sự sững sờ và kính sợ tột độ.",
        "Thắng sụp đổ hoàn toàn, gã đứng không vững phải bám chặt vào bục phát biểu để không bị ngã khuỵu xuống sàn.",
        "Gã trợn trừng mắt nhìn gã nhân viên thử việc mà gã từng sỉ nhục, bắt bốc vác và giẫm nát máy tính, giờ đây đang đứng đó như một vị thần cai quản số phận của gã.",
        "Vương Đại Hải thì mặt cắt không còn một giọt máu, gã run rẩy định bỏ chạy theo lối cửa sau nhưng đã bị hai điều tra viên kinh tế chặn đường khóa chặt.",
        "Hoàng thong thả bước lên bục phát biểu, tự tay cắm chiếc USB bảo mật của mình vào máy tính truyền dẫn hệ thống hiển thị.",
        "Anh mỉm cười lạnh lùng nhìn Thắng: 'Trưởng phòng Đỗ, cuộc chơi của anh đã chính thức kết thúc từ ngày hôm nay.'",
        "Anh bắt đầu trình chiếu báo cáo kiểm toán pháp lý dài hai trăm trang với những bằng chứng không thể chối cãi về đường dây tham nhũng.",
        "Những dòng giao dịch ngân hàng Techcombank đứng tên vợ và em trai Thắng nhận huê hồng từ công ty Gia Hưng hiện rõ trên màn hình lớn.",
        "Toàn bộ sơ đồ rút ruột công quỹ trị giá một trăm hai mươi tỷ đồng của liên minh Thắng - Hải bị phơi bày hoàn toàn trước hàng trăm ống kính truyền thông và đối tác.",
        "Đại diện quỹ ngoại Singapore lập tức đứng dậy, tuyên bố hủy bỏ toàn bộ thỏa thuận M&A cũ vì sự thiếu trung thực của ban quản lý chi nhánh.",
        "Tuy nhiên, vị trưởng đoàn Singapore lập tức quay sang phía Hoàng và Mai Chi, bày tỏ mong muốn được đàm phán một thỏa thuận mới với định giá cao gấp đôi.",
        "Hoàng khẽ gật đầu đồng ý một cách sòng phẳng, hẹn đối tác một buổi làm việc chính thức vào chiều ngày mai.",
        "Trong khi đó, các điều tra viên kinh tế tiến lên sân khấu, tống đạt quyết định khởi tố vụ án và lệnh bắt tạm giam đối với Đỗ Văn Thắng và Vương Đại Hải.",
        "Tiếng còng số tám vang lên lách cách lạnh lùng giữa khán phòng sang trọng, dập tắt hoàn toàn mọi sự kiêu ngạo vô tri của những kẻ sâu mọt.",
        "Thắng quỳ gối khóc lóc thảm thiết, cố gắng lết lại gần Hoàng để van xin sự dung thứ: 'Anh Hoàng... tôi có mắt không tròng... xin anh tha cho tôi một con đường sống!'",
        "Nhưng Trần Minh Hoàng chỉ lạnh lùng quay lưng, ánh mắt anh hướng về phía trước, nơi một tương lai mới của Vạn An Plaza đang chờ đợi anh tái thiết.",
        "Anh biết rằng, đây chính là khoảnh khắc của sự thật, nơi công lý và trí tuệ đã chiến thắng hoàn toàn sự tham lam đê tiện.",
        "Lê Mai Chi đứng bên cạnh anh, nụ cười rạng rỡ hiện trên khuôn mặt xinh đẹp của cô, chứng minh rằng liên minh sòng phẳng của họ đã đạt được thành công mỹ mãn.",
        "Bước chân của các điều tra viên áp giải Thắng và Hải khuất dần sau cánh cửa hội trường, để lại một không gian tĩnh lặng đầy tôn kính dành cho vị vua bán lẻ mới.",
        "Trần Minh Hoàng đứng trên bục cao, đón nhận những tràng pháo tay giòn giã của toàn thể cổ đông và nhân viên chi nhánh.",
        "Anh biết cuộc hành trình tái cấu trúc chi nhánh Thành Tâm đầy gian nan mới chỉ bắt đầu, nhưng với sự đồng hành sòng phẳng của Mai Chi, anh tin chắc sẽ đưa nơi này đạt đến những đỉnh cao mới."
    ]
    
    # Chapter 5: Vua Bán Lẻ Trở Lại
    c5 = [
        "Một tuần sau cuộc thanh trừng chấn động giới tài chính thành phố Thành Tâm, văn phòng của Giám đốc Điều hành Vạn An Plaza đã được dọn dẹp sạch sẽ.",
        "Trần Minh Hoàng ngồi sau chiếc bàn làm việc bằng gỗ gụ sang trọng, khoác trên mình bộ vest màu navy may đo tinh tế của thương hiệu cao cấp Savile Row.",
        "Phong thái của anh giờ đây hoàn toàn là của một nhà lãnh đạo đỉnh cao, một chuyên gia xoay chuyển tình thế doanh nghiệp với tầm nhìn chiến lược xuất sắc.",
        "Lê Mai Chi thong thả bước vào phòng với một tập tài liệu pháp lý mới trên tay, nụ cười sòng phẳng và rạng rỡ hiện rõ trên khuôn mặt xinh đẹp.",
        "Cô đặt tập tài liệu lên bàn: 'Anh Hoàng, đây là biên bản bàn giao năm phần trăm cổ phần ưu đãi biểu quyết của chi nhánh Thành Tâm cho tôi theo đúng hợp đồng.'",
        "Cô ngồi xuống ghế đối diện: 'Và đây cũng là báo cáo phê duyệt ngân sách tái cấu trúc trị giá hai trăm tỷ đồng từ tập đoàn mẹ đã được tôi thông qua.'",
        "Hoàng mở tập tài liệu, ký tên mình dưới vai trò Giám đốc Điều hành mới rồi đẩy ngược lại phía cô một cách vô cùng sòng phẳng và chuyên nghiệp.",
        "Anh nói: 'Rất tốt, sự hỗ trợ pháp lý và tài chính của cô là chìa khóa giúp chi nhánh nhanh chóng ổn định sau cơn bão thanh trừng.'",
        "Anh tiếp tục: 'Toàn bộ hệ thống ERP cũ đã được tôi cấu trúc lại, xóa bỏ hoàn toàn backdoor và thiết lập cơ chế giám sát thời gian thực kết nối trực tiếp với tập đoàn mẹ.'",
        "Hoàng giải thích chi tiết kế hoạch: 'Chúng ta đã cắt đứt hoàn toàn quan hệ với nhà cung ứng Gia Hưng và ký hợp đồng trực tiếp với các trang trại nông sản hữu cơ tại Đà Lạt.'",
        "Anh nhấn mạnh: 'Việc loại bỏ các khâu trung gian ăn huê hồng giúp chúng ta giảm giá bán lẻ mười lăm phần trăm, đồng thời tăng biên lợi nhuận gộp lên hai mươi lăm phần trăm.'",
        "Mai Chi lắng nghe với sự tán thưởng tột độ, cô nhận ra quyết định hợp tác sòng phẳng với Hoàng là thương vụ đầu tư thành công nhất sự nghiệp của mình.",
        "Cô nói: 'Anh Hoàng, quỹ đầu tư Singapore đã đồng ý ký hợp đồng hợp tác chiến lược mới với định giá chi nhánh tăng gấp đôi so với trước đây.'",
        "Cô mỉm cười: 'Họ vô cùng tin tưởng vào năng lực điều hành của anh và danh tiếng của đội ngũ kiểm toán pháp lý do tôi dẫn đầu.'",
        "Hoàng khẽ gật đầu, ánh mắt anh nhìn ra cửa sổ sát đất của văn phòng, hướng về phía dòng sông Sài Gòn đang lấp lánh dưới ánh nắng chiều.",
        "Anh biết rằng, cuộc chiến này không chỉ là để dọn dẹp một chi nhánh siêu thị, mà là để thiết lập một tiêu chuẩn mới cho ngành bán lẻ sạch tại Việt Nam.",
        "Đỗ Văn Thắng và Vương Đại Hải giờ đây đang phải đối mặt với mức án từ mười lăm đến hai mươi năm tù giam vì tội lạm dụng tín nhiệm chiếm đoạt tài sản và vi phạm quy định kế toán gây hậu quả nghiêm trọng.",
        "Toàn bộ tài sản bất chính của chúng, bao gồm các căn biệt thự sang trọng và tài khoản Techcombank đều bị tòa án phong tỏa để thu hồi khắc phục hậu quả.",
        "Đó chính là cái giá cực kỳ đắt đỏ mà những kẻ sâu mọt tham lam phải trả khi dám khinh thường trí tuệ và sự sòng phẳng của pháp luật.",
        "Tiếng gõ cửa nhẹ nhàng cắt ngang cuộc trò chuyện, cô thư ký mới bước vào với thái độ vô cùng cung kính và lịch sự.",
        "Cô báo cáo: 'Thưa Giám đốc Trần, toàn thể nhân viên chi nhánh đã tập trung đầy đủ tại hội trường lớn để nghe anh phát biểu định hướng phát triển mới.'",
        "Hoàng đứng dậy, khẽ chỉnh lại tay áo vest, nhìn sang phía Mai Chi với một ánh mắt đầy tự tin.",
        "Anh nói: 'Chúng ta đi thôi, Giám đốc Lê. Đã đến lúc đưa Vạn An Plaza Thành Tâm trở lại vị thế dẫn đầu thị trường bán lẻ của cả nước.'",
        "Mai Chi đứng dậy đi bên cạnh anh, tiếng gót giày của cô vang lên đều đặn và kiêu hãnh trên hành lang dẫn về phía hội trường.",
        "Khi Hoàng bước vào phòng hội trường, toàn thể hơn năm trăm nhân viên chi nhánh đồng loạt đứng dậy, vỗ tay nhiệt liệt để chào đón vị lãnh đạo mới.",
        "Trong số đó, những người công nhân bốc xếp cũ ở kho hàng số ba nhìn anh với ánh mắt đầy tự hào và kính trọng sâu sắc.",
        "Họ biết rằng, vị giám đốc mới này chính là người từng cùng họ đổ mồ hôi bốc vác, người hiểu rõ nhất những khó khăn và giá trị lao động của họ.",
        "Hoàng bước lên bục phát biểu, nhìn lướt qua toàn thể hội trường với một nụ cười ấm áp nhưng vô cùng uy nghiêm.",
        "Anh dõng dạc nói qua micro: 'Tôi cam kết sẽ xây dựng một môi trường làm việc sòng phẳng, nơi mọi sự cống hiến đều được ghi nhận xứng đáng và mọi hành vi tham nhũng sẽ bị trừng trị nghiêm khắc.'",
        "Anh tiếp tục: 'Chúng ta sẽ không chỉ bán hàng hóa, chúng ta sẽ bán sự tử tế, sự minh bạch và chất lượng tốt nhất cho người tiêu dùng Việt Nam.'",
        "Những tràng pháo tay giòn giã lại vang lên không ngớt khắp hội trường lớn, đánh dấu sự khởi đầu của một kỷ nguyên phát triển rực rỡ.",
        "Trần Minh Hoàng đã hoàn thành xuất sắc nhiệm vụ xoay chuyển tình thế doanh nghiệp của mình một cách hoàn hảo và oanh liệt.",
        "Anh chứng minh cho cả giới tài chính thấy rằng, một khi chuyên gia xuất thế, mọi âm mưu đê tiện đều chỉ là những trò hề vô dụng.",
        "Lê Mai Chi đứng bên cạnh bục phát biểu, ánh mắt cô phản chiếu hình ảnh người đàn ông đầy bản lĩnh và tài năng đang tỏa sáng rực rỡ.",
        "Liên minh sòng phẳng của họ đã thiết lập nên một đế chế bán lẻ vững chắc, sẵn sàng vươn tầm ra toàn bộ khu vực Đông Nam Á trong tương lai.",
        "Cơn bão văn phòng đã qua đi, để lại một bầu trời trong xanh và một tương lai vô cùng tươi sáng cho Vạn An Plaza Thành Tâm.",
        "Trần Minh Hoàng mỉm cười tự hào, bước chân anh vững chãi hướng về phía trước, sẵn sàng cho những thử thách và vinh quang mới đang chờ đón."
    ]
    
    # Pack chapters
    chapters = [
        {"title": "Chương 1: Người Mới Bí Ẩn", "content": "".join([f"<p>{s}</p>\n" for s in c1])},
        {"title": "Chương 2: Đồng Minh Sòng Phẳng", "content": "".join([f"<p>{s}</p>\n" for s in c2])},
        {"title": "Chương 3: Lưới Sắt Bủa Vây", "content": "".join([f"<p>{s}</p>\n" for s in c3])},
        {"title": "Chương 4: Cuộc Họp Đại Hội Đồng", "content": "".join([f"<p>{s}</p>\n" for s in c4])},
        {"title": "Chương 5: Vua Bán Lẻ Trở Lại", "content": "".join([f"<p>{s}</p>\n" for s in c5])}
    ]
    
    # Verify word counts
    print("Verification of Word Counts (Vietnamese):")
    for i, ch in enumerate(chapters):
        words = ch["content"].replace("<p>", "").replace("</p>", "").split()
        count = len(words)
        print(f"Chapter {i+1}: {count} words")
        assert count >= 1100, f"Chapter {i+1} has only {count} words! Must be >= 1100."
        
    payload = {
        "title": title,
        "subtitle": subtitle,
        "author": author,
        "genre": genre,
        "intro": intro,
        "cover_prompt": cover_prompt,
        "chapters": chapters
    }
    
    output_path = "/Users/aaronnguyen/TN/App/doctieuthuyet/scratch/draft_novel_12.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    print(f"Successfully generated and saved to {output_path}")

if __name__ == "__main__":
    generate_novel()
