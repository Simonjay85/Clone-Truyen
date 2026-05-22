import json
import os

def count_words(text):
    # Strip HTML tags to count actual words
    plain_text = text.replace("<p>", "").replace("</p>", "").replace("\n", " ").replace("\r", " ")
    words = [w for w in plain_text.split() if w.strip()]
    return len(words)

# Novel ID 24 Draft Generator
novel_data = {
  "title": "Người Đưa Thư Bị Cả Tòa Nhà Cao Cấp Coi Thường, Anh Là Chủ Sở Hữu Tòa Nhà Đó",
  "subtitle": "Quyền Lực Hạng A",
  "author": "Đông Hải Cư Sĩ",
  "genre": "Sảng Văn",
  "intro": "<p>Đinh Xuân Phú, vị tỷ phú bất động sản thương mại bí ẩn đứng đầu tập đoàn địa ốc Đinh Gia sở hữu hàng loạt tòa nhà văn phòng hạng A+ tại khu trung tâm, quyết định khoác lên mình bộ đồng phục bưu tá sờn cũ để điều tra thực địa.</p>\n<p>Tại Thành Tâm Financial Tower - biểu tượng kiêu hãnh cao 45 tầng của sự thịnh vượng, anh phải đối mặt với sự sỉ nhục tột cùng từ Trần Quang Hùng, Trưởng ban Quản lý tòa nhà đầy tham nhũng và ngạo mạn.</p>\n<p>Nhưng dưới lớp áo của kẻ đưa thư nghèo khổ là một cái bẫy pháp y tài chính và dòng tiền tinh vi đang dần siết chặt cổ kẻ lạm quyền.</p>\n<p>Cùng sự bắt tay sòng phẳng của Phan Bích Phượng, Asset Manager sắc sảo của quỹ đầu tư Lotus Capital, một cuộc lật kèo kinh điển bằng quyền sở hữu tuyệt đối và pháp lý tối cao chuẩn bị bắt đầu.</p>",
  "cover_prompt": "A high-end book cover, highly detailed web novel illustration style, a powerful and handsome mature Vietnamese billionaire in his early 40s in a sharp dark charcoal grey suit standing confidently inside a modern luxury glass-walled lobby of a soaring skyscraper at sunset. Gleaming marble floors, cinematic sun flare, premium colors.",
  "chapters": []
}

# CHƯƠNG 1
ch1_paragraphs = [
  "Tiếng giày cao gót nện xuống sàn đá Marble Carrara nhập khẩu từ Ý vang lên những âm thanh sắc gọn, đập vào không gian tĩnh lặng của sảnh lớn.",
  "Đinh Xuân Phú đứng ở góc khuất cạnh cột trụ chịu lực bọc kính cường lực, đôi bàn tay chai sần khẽ siết chặt lấy quai chiếc túi da đựng thư đã sờn rách.",
  "Anh mặc bộ đồng phục bưu tá màu xanh thẫm bạc màu, chiếc mũ lưỡi trai sờn mép che khuất nửa khuôn mặt sương gió của một người đàn ông bốn mươi mốt tuổi.",
  "Không ai có thể ngờ rằng, người đàn ông đang bị coi là kẻ nghèo hèn nhất tòa nhà này lại chính là chủ sở hữu tối cao của Thành Tâm Financial Tower - tòa nhà văn phòng hạng A+ đắt đỏ bậc nhất trung tâm Quận 1.",
  "Phú nhắm mắt lại, lắng nghe tiếng rì rầm của hệ thống điều hòa trung tâm Chiller hoạt động có phần nặng nề và phát ra những tiếng rung động bất thường.",
  "Là một chuyên gia bất động sản thương mại với hơn hai mươi năm lăn lộn trên thị trường, anh chỉ cần nghe tiếng gió thổi qua họng gió AHU cũng biết hệ thống cơ điện trị giá hàng triệu đô này đang gặp sự cố nghiêm trọng.",
  "Đúng lúc đó, Trần Quang Hùng - Trưởng ban Quản lý tòa nhà, bước ra từ thang máy tốc độ cao dành riêng cho ban quản trị.",
  "Hùng bốn mươi lăm tuổi, diện bộ vest màu xanh navy bóng lộn, mái tóc vuốt gel ngược ra sau bóng mượt, bên cạnh là cô nhân viên lễ tân trưởng Nguyễn Thu Trang đang nép sát vào người gã.",
  "Hùng liếc nhìn đồng hồ Longines mạ vàng trên cổ tay, lông mày gã nhíu chặt lại khi nhìn thấy bóng dáng Phú đang đứng gần khu vực thang máy dịch vụ.",
  "Gã sải bước tới, tiếng giày da Oxford nện xuống sàn đá bóng loáng đầy uy quyền và ngạo mạn.",
  "\"Này, thằng đưa thư kia, mắt mày mù hay sao mà đứng lù lù ở đây?\" Hùng quát lớn, giọng điệu khinh khỉnh không hề che giấu sự coi thường.",
  "\"Mày có biết đây là khu vực sảnh VIP không? Bộ dạng bẩn thỉu, nghèo hèn của mày đang làm bôi bẩn cả hình ảnh hạng A+ của tòa nhà này đấy!\"",
  "Phú từ từ ngẩng đầu lên, ánh mắt đằng sau vành mũ lưỡi trai vô cùng bình thản, không một chút gợn sóng.",
  "\"Tôi đến giao thư khẩn từ ngân hàng Vietcombank gửi cho Ban quản trị tòa nhà, thư yêu cầu ký nhận trực tiếp từ người có thẩm quyền,\" Phú trả lời, giọng nói trầm ấm và đĩnh đạc.",
  "Trang đứng bên cạnh Hùng che miệng cười khúc khích, ánh mắt đầy sự giễu cợt quét qua đôi giày vải sờn gót của Phú.",
  "\"Anh Hùng xem kìa, giờ đến cả mấy đứa giao bưu phẩm cũng dám lên giọng đĩnh đạc ở đây rồi, thật là không biết thân biết phận,\" Trang nũng nịu nói, tay vuốt ve vạt áo vest của Hùng.",
  "Hùng nghe vậy thì càng được đà thể hiện quyền lực, gã bước tới giật phăng chiếc giỏ da trên vai Phú.",
  "Lực giật mạnh đến nỗi khiến toàn bộ đống thư từ, hồ sơ quan trọng bên trong văng ra ngoài, rơi vãi tung tóe trên sàn đá marble lấp lánh.",
  "\"Thư khẩn cái gì? Mấy cái loại giấy lộn này mà cũng đòi vào sảnh VIP sao?\" Hùng cười khẩy, mũi giày da Ý đắt tiền của gã giẫm thẳng lên một lá thư có logo niêm phong đỏ của Vietcombank.",
  "Phú không hề tức giận, anh chậm rãi quỳ một gối xuống sàn đá lạnh ngắt để nhặt từng lá thư.",
  "Ngón tay anh khẽ lướt qua lá thư bị giẫm dưới chân Hùng, khóe mắt anh nheo lại khi nhìn thấy tiêu đề khẩn: 'Cảnh báo về việc sai lệch kiểm toán tài sản thế chấp thiết bị Chiller'.",
  "Đây chính là lý do Phú giả dạng làm người đưa thư suốt một tháng qua để điều tra thực địa tại chính tòa nhà của mình.",
  "Các báo cáo tài chính gửi về văn phòng Tập đoàn Đinh Gia liên tục cho thấy chi phí vận hành tăng vọt, trong khi hệ thống trang thiết bị liên tục báo hỏng và cần ngân sách thay thế khổng lồ.",
  "\"Mày nhìn cái gì? Nhặt nhanh cái tay lên rồi cút xéo bằng lối thoát hiểm cho tao!\" Hùng hằn học nói, gã cố tình di di mũi giày lên mu bàn tay của Phú.",
  "Áp lực từ đế giày da cứng ngắc nện xuống khiến xương bàn tay Phú đau nhức, nhưng anh vẫn im lặng, khớp ngón tay bấm chặt vào lòng bàn tay đến mức rỉ ra vài giọt máu đỏ tươi.",
  "Phú ngước mắt lên nhìn thẳng vào mắt Trần Quang Hùng.",
  "Ánh mắt của vị tỷ phú ẩn danh lúc này đột ngột thay đổi, nó không còn là ánh mắt của một kẻ bưu tá nghèo hèn, mà là ánh mắt lạnh lùng, sắc lẹm của một kẻ đứng đầu chuỗi bất động sản trị giá hàng tỷ đô la.",
  "Trần Quang Hùng bỗng nhiên cảm thấy một luồng khí lạnh chạy dọc sống lưng, sống gáy gã toát ra một tầng mồ hôi lạnh buốt.",
  "Gã vô thức lùi lại một bước, tim đập chệch đi một nhịp trước cái nhìn đầy uy lực của người đàn ông trung niên trước mặt.",
  "Nhưng sự kiêu ngạo tích tụ nhiều năm ở vị trí trưởng ban quản lý nhanh chóng khỏa lấp nỗi sợ hãi vô hình đó.",
  "\"Mày... mày dám trợn mắt nhìn tao thế à? Có tin tao gọi bảo vệ đập gãy chân mày rồi ném ra đường không?\" Hùng quát lớn để che giấu sự chột dạ của mình.",
  "\"Một thằng đưa thư quèn lương ba cọc ba đồng mà cũng bày đặt tỏ vẻ nguy hiểm sao?\"",
  "Phú đứng dậy, phủi bụi trên đầu gối, cẩn thận cất lá thư niêm phong của Vietcombank vào sâu trong túi áo đồng phục.",
  "\"Trần trưởng ban, hệ thống chiếu sáng sảnh lớn vốn được thiết kế dùng bóng Philips Master LED tiêu chuẩn châu Âu để đảm bảo độ rọi và tiết kiệm điện,\" Phú bình thản nói, ngón tay chỉ lên trần sảnh cao chín mét.",
  "\"Nhưng hiện tại toàn bộ đã bị thay thế bằng bóng LED Trung Quốc rẻ tiền, ánh sáng ngả xanh và độ hoàn màu cực thấp.\"",
  "\"Chưa kể, ba camera an ninh ở góc khuất hành lang dịch vụ phía sau đã bị ngắt kết nối nguồn điện suốt mười hai ngày qua.\"",
  "\"Ông nghĩ những việc này không ai biết sao?\" Phú khẽ mỉm cười, nụ cười ẩn chứa sự lạnh lẽo tột cùng.",
  "Trần Quang Hùng nghe đến đây thì mặt biến sắc hoàn toàn, môi gã khẽ giật giật, gân xanh trên thái dương nổi lên cuồn cuộn.",
  "Những chi tiết kỹ thuật này là bí mật nội bộ mà gã cùng đội ngũ kỹ thuật thân tín đã thực hiện để ăn bớt hàng trăm triệu đồng tiền vật tư và tạo góc tối để vận chuyển trang thiết bị biển thủ ra ngoài.",
  "Làm sao một thằng đưa thư quèn lại có thể nắm rõ cấu trúc kỹ thuật và phát hiện ra những lỗ hổng này một cách chính xác đến vậy?",
  "\"Mày... mày ngậm miệng lại! Mày ăn nói hàm hồ, vu khống ban quản lý!\" Hùng hét lên đầy giận dữ.",
  "\"Bảo vệ đâu! Lập tức đuổi cổ thằng điên này ra ngoài cho tôi! Ký lệnh cấm cửa vĩnh viễn không cho nó bước chân vào tòa nhà này nữa!\"",
  "Hai nhân viên bảo vệ to khỏe lập tức lao tới, nắm chặt lấy bả vai Phú định lôi đi.",
  "Phú khẽ nhún vai, tự mình chấn chỉnh lại vạt áo bưu tá, quay người bước đi mà không cần bảo vệ phải kéo.",
  "\"Trần trưởng ban, thế giới này rất nhỏ, chúng ta sẽ sớm gặp lại nhau thôi, lúc đó hy vọng đầu gối của ông vẫn đủ vững,\" Phú nói vọng lại trước khi bước qua cánh cửa xoay pha lê hướng ra đường lớn.",
  "Trần Quang Hùng nhìn theo bóng lưng đĩnh đạc của người đưa thư, gã bực bội nới lỏng chiếc cà vạt hiệu Hermes đang thắt chặt ở cổ.",
  "Một cảm giác bất an dâng tràn trong lòng Hùng, mồ hôi lạnh sau gáy gã vẫn liên tục túa ra, thấm đẫm cả mảng áo sơ mi đắt tiền.",
  "Gã không hề biết rằng, bánh răng của số phận đã bắt đầu chuyển động, và vị chủ nhân tối cao của tòa nhà này vừa ký bản án tử hình cho sự nghiệp của gã.",
  "Phú bước ra ngoài hiên tòa nhà, ngước nhìn đỉnh tháp Thành Tâm Financial Tower sừng sững chọc thủng những tầng mây dưới ánh nắng ban mai rực rỡ.",
  "Anh lấy chiếc điện thoại Vertu Signature S bằng vàng khối từ trong túi quần ra, bấm một số gọi khẩn cấp.",
  "\"Alô, Tiến đấy à? Tôi là Xuân Phú đây. Hãy chuẩn bị cho tôi hồ sơ kiểm toán pháp y toàn bộ các khoản vay thế chấp của ban quản lý Thành Tâm Financial Tower ngay lập tức.\"",
  "Đầu dây bên kia, giọng nói của vị Tổng giám đốc chi nhánh Vietcombank run lên vì kính cẩn: \"Dạ vâng, thưa Chủ tịch Đinh, tôi sẽ đích thân xử lý việc này trong vòng hai tiếng đồng hồ!\"",
  "Phú cúp máy, khóe môi vẽ nên một đường cong sắc lạnh, ánh mắt anh hướng về phía dòng xe cộ tấp nập dưới lòng đường trung tâm thành phố Thành Tâm."
]

# CHƯƠNG 2
ch2_paragraphs = [
  "Phòng khánh tiết VIP tại tầng ba mươi tám của tòa nhà Thành Tâm Financial Tower ngập tràn ánh sáng từ những bức tường kính sát trần nhìn ra toàn cảnh sông Sài Gòn rực rỡ.",
  "Bầu không khí bên trong phòng họp rộng lớn lúc này đang căng thẳng đến mức tưởng chừng như chỉ cần một tia lửa nhỏ cũng có thể làm bùng nổ bầu không khí ngột ngạt này.",
  "Phan Bích Phượng ngồi ở vị trí trung tâm của dãy bàn gỗ gõ đỏ nguyên khối, đôi bàn tay thanh mảnh đan chéo vào nhau, đặt nhẹ trên tập tài liệu đàm phán bìa da màu đen.",
  "Ở tuổi ba mươi sáu, Phượng là biểu tượng của sự thành công và quyền lực trong giới quản lý tài sản thương mại tại Việt Nam.",
  "Dưới danh nghĩa Asset Manager của Quỹ đầu tư bất động sản quốc tế Lotus Capital, cô đang trực tiếp quản lý và vận hành danh mục tài sản trị giá hơn năm trăm triệu USD.",
  "Đối diện cô là Trần Quang Hùng, Trưởng ban Quản lý tòa nhà, trán gã lấm tấm mồ hôi dù hệ thống điều hòa trong phòng đang đặt ở mức mười chín độ C.",
  "\"Cô Phan, mức phí quản lý một phẩy năm phần trăm trên tổng doanh thu thuê là con số hoàn toàn hợp lý đối với một tòa nhà hạng A+ ở vị trí độc tôn này,\" Hùng cố gắng giữ giọng điệu tự tin, đẩy tập hồ sơ về phía Phượng.",
  "\"Chúng tôi cung cấp dịch vụ bảo trì tiêu chuẩn năm sao, hệ thống an ninh đa lớp, và cam kết đảm bảo trải nghiệm tốt nhất cho các khách thuê lớn của Lotus Capital như HSBC hay PwC.\"",
  "Phượng không thèm liếc mắt nhìn tập hồ sơ của Hùng, cô khẽ nhếch môi, nụ cười mang theo sự lạnh lùng và sắc sảo của một nữ tướng thương trường.",
  "\"Trần trưởng ban, ông nghĩ tôi là một đứa trẻ mới bước chân vào thị trường bất động sản thương mại thương lượng bằng những lời hứa hẹn sáo rỗng sao?\" Phượng lên tiếng, giọng nói trong trẻo nhưng đầy uy lực.",
  "\"Lotus Capital đại diện cho mười tầng văn phòng cao cấp nhất tại tòa nhà này, chiếm tới ba mươi phần trăm tổng diện tích cho thuê của toàn bộ dự án.\"",
  "\"Chúng tôi yêu cầu mức phí quản lý nghiêm ngặt chỉ không phẩy năm phần trăm ròng, không đi kèm bất kỳ khoản phụ phí ngoài giờ nào cả.\"",
  "\"Đồng thời, hợp đồng mới phải quy định rõ quyền phủ quyết hoàn toàn của Lotus Capital đối với việc gia hạn hợp đồng thuê của bất kỳ đơn vị liền kề nào ở các tầng thương mại.\"",
  "Trần Quang Hùng nghe xong thì mặt biến sắc, gã đập mạnh tay xuống bàn, gân xanh nổi lên đầy giận dữ.",
  "\"Không phẩy năm phần trăm? Cô Phan, cô đang đùa tôi đấy à? Mức phí đó thậm chí không đủ để chúng tôi chi trả cho đội ngũ vận hành hệ thống điều hòa trung tâm Chiller!\"",
  "\"Hơn nữa, quyền phủ quyết gia hạn là thuộc về chủ sở hữu tòa nhà, một quỹ đầu tư như các cô lấy tư cách gì đòi quyền hạn tối cao đó?\"",
  "Phượng nhẹ nhàng mở tập tài liệu bìa da trước mặt, lấy ra một tập báo cáo kỹ thuật dày đặc các biểu đồ và hình ảnh thực tế.",
  "\"Tôi lấy tư cách là người đang nắm giữ dòng tiền cứu sống tòa nhà này để đòi hỏi điều đó, Trần trưởng ban,\" Phượng lạnh lùng ném tập báo cáo lên mặt bàn gỗ vang lên một tiếng cộp.",
  "\"Hãy nhìn vào trang số mười bốn. Đây là báo cáo kỹ thuật độc lập do Lotus Capital thuê chuyên gia từ Singapore sang khảo sát bí mật.\"",
  "\"Hệ thống điều hòa trung tâm Chiller York nguyên bản của tòa nhà đã bị tháo dỡ các linh kiện máy nén chính hãng, thay thế bằng các linh kiện Daikin hàng bãi trôi nổi loại hai.\"",
  "\"Việc biển thủ thiết bị này đã khiến hệ thống hoạt động quá tải liên tục, nhiệt độ phòng máy chủ của ngân hàng HSBC tại tầng mười tám tuần trước tăng vọt lên ba mươi hai độ C, gây hư hỏng hệ thống ổ cứng và suýt làm gián đoạn giao dịch của cả chi nhánh!\"",
  "\"Chi phí bảo trì bị khai khống lên đến hàng tỷ đồng mỗi tháng để đút túi riêng, trong khi hạ tầng kỹ thuật bị hủy hoại nghiêm trọng.\"",
  "\"Nếu Lotus Capital công bố thông tin này rộng rãi, đồng thời kích hoạt điều khoản rút lui, rút toàn bộ mười tầng văn phòng sang tòa nhà Deutsches Haus bên cạnh vào tháng sau...\"",
  "Phượng dừng lại một nhịp, đôi mắt sắc sảo nhìn chằm chằm vào khuôn mặt đang dần chuyển sang màu xám ngoét của Trần Quang Hùng.",
  "\"Tỷ lệ trống của Thành Tâm Financial Tower sẽ lập tức vượt ngưỡng bốn mươi phần trăm.\"",
  "\"Lúc đó, theo điều khoản vay hợp vốn trị giá một nghìn hai trăm tỷ đồng giữa chủ đầu tư và ngân hàng BIDV, Vietcombank, ngân hàng sẽ lập tức kích hoạt điều khoản phạt thế chấp và siết nợ tòa nhà.\"",
  "\"Trần trưởng ban, ông có gánh nổi trách nhiệm này trước chủ tịch tập đoàn Đinh Gia không?\" Phượng hỏi dồn dập, từng câu từng chữ như những nhát dao đâm thẳng vào điểm yếu chí mạng của Hùng.",
  "Trần Quang Hùng lúc này run rẩy thực sự, mồ hôi lạnh chảy ròng ròng ướt đẫm cả lưng áo vest đắt tiền.",
  "Gã không ngờ Phượng lại có thể nắm giữ những bằng chứng kỹ thuật chính xác và nắm thóp được cả cấu trúc điều khoản tài chính thế chấp của tòa nhà với các ngân hàng một cách tường tận đến thế.",
  "Đầu gối gã run run, suýt chút nữa đã quỳ cộp xuống sàn nếu không bấu chặt tay vào mép bàn gỗ.",
  "Đúng lúc đó, cửa phòng họp khẽ mở, một người đưa thư mặc đồng phục bưu chính sờn cũ bước vào sảnh khánh tiết để giao tài liệu bổ sung.",
  "Đó chính là Đinh Xuân Phú.",
  "Anh im lặng đứng ở góc phòng, đặt tập hồ sơ lên bàn phụ, ánh mắt thản nhiên quan sát toàn bộ diễn biến cuộc đàm phán.",
  "Nhìn thấy Phú, Trần Quang Hùng lập tức như tìm được chỗ để xả cơn thịnh nộ và che giấu sự hoảng loạn của mình.",
  "\"Mày... thằng đưa thư khốn kiếp kia! Ai cho phép mày tự ý bước vào phòng khánh tiết VIP này?\" Hùng gầm lên, ngón tay chỉ thẳng vào mặt Phú.",
  "\"Lính bảo vệ đâu? Sao lại để cái loại rác rưởi này đi lại tự do trong tòa nhà thế này? Định làm bôi nhọ cuộc họp cấp cao của chúng tôi à?\"",
  "Phan Bích Phượng khẽ chau mày, ánh mắt cô hướng về phía Phú.",
  "Trái ngược với sự giận dữ thô lỗ của Hùng, Phượng nhận thấy người đưa thư trung niên này có một phong thái vô cùng kỳ lạ.",
  "Dù bị mắng nhiếc thậm tệ, nhưng xương sống của anh vẫn thẳng tắp, ánh mắt sâu thẳm tĩnh lặng như nước hồ thu, hoàn toàn không có sự sợ hãi hay khúm núm của một kẻ dưới đáy xã hội.",
  "\"Trần trưởng ban, tôi chỉ vào giao bản sao phụ lục hợp đồng thế chấp bổ sung từ Vietcombank theo yêu cầu của văn phòng ban quản trị,\" Phú bình thản nói, giọng nói trầm ổn vang vọng khắp phòng khánh tiết.",
  "Hùng lao tới, giật phăng tập hồ sơ từ tay Phú rồi ném thẳng vào thùng rác góc phòng.",
  "\"Cút ngay cho tao! Một thằng bưu tá quèn thì biết cái gì về hợp đồng thế chấp với phí quản lý?\" Hùng quát tháo.",
  "\"Cô Phan, cuộc đàm phán hôm nay dừng lại ở đây. Việc gia hạn hợp đồng và các điều khoản này, tôi buộc phải trình lên Chủ tịch Tập đoàn Địa ốc Đinh Gia - người sở hữu tối cao của tòa nhà này quyết định.\"",
  "\"Chủ tịch Đinh Gia là nhân vật thần bí cực kỳ bận rộn, không phải loại người ai muốn gặp cũng được. Lần tới gặp lại, tôi hy vọng Lotus Capital sẽ có thái độ biết điều hơn!\" Hùng cố vớt vát thể diện bằng cách lôi danh nghĩa chủ tịch tối cao ra đe dọa.",
  "Phượng đứng dậy, xếp tài liệu vào cặp da một cách dứt khoát.",
  "\"Được thôi, tôi cho ông thời hạn ba ngày để trình lên Chủ tịch của ông,\" Phượng nói sòng phẳng.",
  "\"Nếu sau ba ngày không có phản hồi bằng văn bản đồng ý với mức phí không phẩy năm phần trăm và quyền phủ quyết của chúng tôi, Lotus Capital sẽ chính thức đơn phương chấm dứt đàm phán và khởi kiện ban quản lý ra Tòa án Kinh tế Thành Tâm vì vi phạm tiêu chuẩn vận hành cơ điện.\"",
  "Cô bước nhanh ra khỏi phòng họp, gót giày cao gót nện xuống sàn đá phát ra những âm thanh đầy dứt khoát.",
  "Phú khẽ cúi đầu chào Phượng khi cô bước qua, ánh mắt hai người chạm nhau trong một khoảnh khắc ngắn ngủi.",
  "Phượng bỗng khựng lại một nhịp, tim cô đập nhanh hơn khi nhìn sâu vào đôi mắt của người đưa thư nghèo khổ đó - một đôi mắt chứa đựng quyền lực tuyệt đối của kẻ đứng trên đỉnh cao vạn người.",
  "Phú im lặng quay người bước đi theo lối thang máy dịch vụ, để lại Trần Quang Hùng đang đứng thở hồng hộc trong phòng họp trống trải, mồ hôi lạnh chảy dài trên trán gã không ngừng rơi xuống sàn đá marble lạnh lẽo."
]

# CHƯƠNG 3
ch3_paragraphs = [
  "Quán cà phê Runam Bistro dưới chân tòa nhà Vietcombank Tower lộng lẫy ngập tràn tiếng nhạc Jazz êm dịu và hương thơm nồng nàn của những hạt cà phê Arabica thượng hạng.",
  "Phan Bích Phượng ngồi ở góc bàn VIP cạnh cửa sổ kính lớn nhìn ra bến Bạch Đằng, ngón tay cô khẽ gõ nhẹ theo nhịp nhạc, tâm trạng cô lúc này vô cùng bồn chồn.",
  "Cô vừa nhận được một cuộc gọi từ số điện thoại lạ, người gọi tự xưng là người có thể cung cấp toàn bộ hồ sơ kiểm toán pháp y tài chính của Thành Tâm Financial Tower để giúp cô thắng tuyệt đối trong vụ đàm phán.",
  "Và người đó hẹn cô ở đây.",
  "Cánh cửa quán cà phê mở ra, Phượng ngước mắt nhìn lên và hoàn toàn sững sờ.",
  "Người đàn ông bước vào không còn mặc bộ đồng phục đưa thư màu xanh sờn cũ bẩn thỉu của ngày hôm trước.",
  "Anh mặc một chiếc áo sơ mi màu xám tro may đo thủ công từ nhà mốt cao cấp Savile Row cực kỳ vừa vặn, kết hợp với chiếc quần tây đen lịch lãm và đôi giày da cá sấu được đánh bóng hoàn hảo.",
  "Mái tóc hoa râm được cắt tỉa gọn gàng, phong thái điềm đạm, uy nghiêm của anh tỏa ra một sức hút mạnh mẽ khiến những thực khách xung quanh vô thức phải ngoái nhìn.",
  "Đó chính là Đinh Xuân Phú - người đưa thư bị Trần Quang Hùng sỉ nhục hôm qua.",
  "\"Chào cô Phan, rất vui vì cô đã đến đúng giờ,\" Phú bước tới, kéo ghế đối diện Phượng và ngồi xuống một cách đĩnh đạc, tự nhiên.",
  "Phượng mở to mắt kinh ngạc, đôi môi đỏ mọng khẽ mấp máy, cô phải dùng hai ngón tay bấm mạnh vào lòng bàn tay đến mức rỉ máu để giữ cho mình không hét lên vì sửng sốt.",
  "\"Anh... anh là người đưa thư hôm qua? Sao anh lại... chuyện này là thế nào?\" Phượng lắp bắp hỏi, sự sắc sảo thường ngày của một Asset Manager bỗng chốc bay biến sạch sẽ.",
  "Phú mỉm cười nhẹ nhàng, anh đẩy một tách trà hoa cúc ấm áp về phía cô để giúp cô lấy lại bình tĩnh.",
  "\"Người đưa thư chỉ là một trong những vai diễn của tôi để nhìn thấu những góc tối dưới đáy tòa nhà mà thôi, cô Phan,\" Phú thong thả nói.",
  "\"Còn đây mới là thân phận thực sự của tôi. Tôi là Đinh Xuân Phú, Chủ tịch Hội đồng Quản trị Tập đoàn Địa ốc Đinh Gia - chủ sở hữu duy nhất của tòa nhà Thành Tâm Financial Tower mà cô đang muốn thuê.\"",
  "Phượng cảm thấy đầu óc mình như nổ tung, một luồng điện chạy khắp toàn thân khiến các dây thần kinh của cô căng lên.",
  "Vị chủ tịch thần bí, người đứng sau đế chế bất động sản thương mại khổng lồ sở hữu hàng chục tòa cao ốc hạng A+ tại Việt Nam, lại chính là người đưa thư bị ban quản lý giẫm lên tay và đuổi cổ như một con chó rác rưởi?",
  "\"Chủ tịch Đinh... thật sự là ngài sao?\" Phượng hít một hơi thật sâu, cố gắng chấn chỉnh lại tinh thần, cô nhận ra đây là một bước ngoặt lịch sử.",
  "Phú không trả lời bằng lời nói, anh lấy từ trong cặp da cao cấp ra một tệp tài liệu dày hơn ba trăm trang, đóng dấu đỏ bảo mật của Ngân hàng Nhà nước Việt Nam và Vietcombank gửi trực tiếp cho cô.",
  "\"Hãy đọc cái này đi. Đây là kết quả kiểm toán pháp y tài chính (financial forensics) khẩn cấp mà tôi vừa yêu cầu Vietcombank thực hiện đối với dòng tiền vận hành của ban quản lý tòa nhà dưới thời Trần Quang Hùng,\" Phú nói, giọng nói lạnh lùng hẳn đi.",
  "Phượng đón lấy tập tài liệu, nhanh chóng lật từng trang, mắt cô càng đọc càng mở to, sống lưng toát ra một tầng mồ hôi lạnh buốt.",
  "Hồ sơ pháp y tài chính vạch trần một đường dây tham nhũng kinh hoàng.",
  "Trần Quang Hùng đã thông đồng với công ty xây dựng sân sau mang tên 'Thiết bị Cơ điện Phương Nam' để lập khống các hóa đơn bảo trì hệ thống phòng cháy chữa cháy của tập đoàn Hochiki (Nhật Bản) trị giá bốn mươi lăm tỷ đồng.",
  "Nhưng trên thực tế, toàn bộ thiết bị lắp đặt tại tòa nhà chỉ là đồ nhái loại hai nhập khẩu từ biên giới, không hề có chứng chỉ CO/CQ chuẩn quy chuẩn xây dựng Việt Nam.",
  "Nghiêm trọng hơn nữa, Hùng đã tự ý ký một hợp đồng thế chấp ngầm quyền khai thác bãi đỗ xe ngầm ba tầng của tòa nhà cho một tổ chức tín dụng đen để lấy khoản tiền mặt sáu mươi tỷ đồng.",
  "Khoản tiền này đã bị Hùng chuyển vào tài khoản cá nhân để đầu tư chứng khoán phái sinh và hiện tại đã thua lỗ cháy sạch tài khoản.",
  "\"Kẻ lừa đảo này... gã dám tự ý thế chấp cả tài sản của tòa nhà sao? Đây là tội hình sự cực kỳ nghiêm trọng!\" Phượng thốt lên, ngón tay run rẩy kẹp chặt lấy trang giấy.",
  "\"Đúng vậy. Khoản vay thế chấp một nghìn hai trăm tỷ đồng của tòa nhà tại Vietcombank đang đứng trước nguy cơ bị chuyển thành nợ xấu nhóm năm do tài sản đảm bảo bị hủy hoại và thất thoát dòng tiền khai thác bãi xe,\" Phú phân tích chi tiết bằng thuật ngữ tài chính chuyên sâu.",
  "\"Trần Quang Hùng đang tìm mọi cách để lấp liếm lỗ hổng một trăm lẻ năm tỷ đồng này trước kỳ kiểm toán cuối tháng của ngân hàng.\"",
  "\"Và gã đang chuẩn bị giăng một cái bẫy lớn để đẩy toàn bộ hậu quả cho Lotus Capital và các ngân hàng liên quan gánh chịu.\"",
  "Phượng nhìn Phú, trong mắt cô hiện lên sự ngưỡng mộ và cả sự kiêng dè trước trí tuệ pháp lý và tầm nhìn sắc bén của vị tỷ phú bốn mươi mốt tuổi.",
  "\"Vậy Chủ tịch Đinh muốn tôi hợp tác như thế nào?\" Phượng thẳng thắn đặt điều kiện, cô biết mình đang đứng trước một cơ hội ngàn năm có một để khẳng định vị thế của quỹ.",
  "\"Cô rất thông minh, Phan Bích Phượng,\" Phú khen ngợi, ánh mắt anh lộ ra sự tán thưởng.",
  "\"Tôi muốn cô tiếp tục đẩy mạnh sức ép đàm phán. Hãy giả vờ như không biết gì về vụ biển thủ kỹ thuật này, ép Hùng phải ký hợp đồng gia hạn với mức phí không phẩy năm phần trăm ròng.\"",
  "\"Khi gã bị dồn vào đường cùng và buộc phải tìm nguồn tiền khác để bù đắp dòng tiền khống, gã chắc chắn sẽ ký hợp đồng với một đối tác lừa đảo ngoài luồng để lấy tiền đặt cọc ngắn hạn.\"",
  "\"Đó chính là lúc chiếc bẫy pháp lý của chúng ta sập xuống hoàn toàn.\"",
  "\"Tôi sẽ đích thân đứng ra bảo lãnh thanh toán cho toàn bộ danh mục thuê của Lotus Capital, đồng thời trao cho cô quyền phủ quyết tuyệt đối và mức phí quản lý không phẩy năm phần trăm như cô mong muốn.\"",
  "Phượng hít một hơi thật sâu, cô đưa bàn tay thon thả ra trước mặt Phú.",
  "\"Thỏa thuận thành lập, thưa Chủ tịch Đinh. Lotus Capital sẽ đồng hành cùng ngài trong ván bài lật ngửa này!\"",
  "Phú đưa tay ra bắt lấy tay cô, một cái bắt tay sòng phẳng, chặt chẽ giữa hai bộ óc thiên tài tài chính.",
  "Ánh hoàng hôn buông xuống sông Sài Gòn rực sáng, phản chiếu lên vách kính của quán cà phê, vẽ nên một khung cảnh tráng lệ như điềm báo cho một cơn bão quyền lực sắp quét sạch những kẻ lạm quyền tại Thành Tâm Financial Tower."
]

# CHƯƠNG 4
ch4_paragraphs = [
  "Trần Quang Hùng đứng trong văn phòng trưởng ban quản lý tại tầng năm, hai tay gã chống xuống bàn làm việc, thở dốc như một con thú bị dồn vào chân tường.",
  "Mồ hôi lạnh tuôn ra như tắm, làm ướt sũng cả chiếc áo sơ mi kẻ sọc đắt hiệu Burberry của gã.",
  "Báo cáo kiểm toán khẩn cấp từ Vietcombank gửi tới sáng nay yêu cầu ban quản lý phải giải trình chi tiết về khoản thâm hụt dòng tiền sáu mươi tỷ đồng từ bãi đỗ xe ngầm và chứng thư PCCC Hochiki trong vòng bốn mươi tám tiếng.",
  "Nếu không giải trình được, hồ sơ sẽ lập tức được chuyển sang Cục Cảnh sát điều tra tội phạm về tham nhũng, kinh tế, buôn lậu (C03) của Bộ Công an.",
  "\"Khốn kiếp! Làm sao lũ khốn ngân hàng lại phát hiện ra nhanh thế được?\" Hùng gầm rú, đập nát chiếc gạt tàn pha lê xuống sàn nhà.",
  "Đúng lúc đó, chiếc điện thoại bàn vang lên tiếng chuông chói tai.",
  "Hùng run rẩy nhấc máy, đầu dây bên kia là giọng nói của Nguyễn Thế Anh, Giám đốc Công ty Đầu tư Tài chính Thịnh Phát.",
  "\"Anh Hùng à, bên tôi đã chuẩn bị sẵn khoản tiền đặt cọc một trăm tỷ đồng bằng tiền mặt để thuê toàn bộ khu vực sảnh trệt và tầng hai của tòa nhà làm trụ sở sàn giao dịch tiền số Thịnh Phát Coin,\" Thế Anh nói, giọng điệu đầy dụ dỗ.",
  "\"Chỉ cần anh ký hợp đồng thuê ngay trong ngày hôm nay, tiền mặt sẽ lập tức được giải ngân vào tài khoản ban quản lý tòa nhà để anh cân đối sổ sách ngân hàng.\"",
  "\"Nhưng chúng tôi yêu cầu phải tổ chức lễ ký kết công khai rầm rộ tại sảnh chính tòa nhà để tạo lòng tin cho các nhà đầu tư.\"",
  "Hùng nghe như người sắp chết đuối vớ được cọc, gã không cần suy nghĩ nhiều, lập tức đồng ý.",
  "Gã biết thừa Thịnh Phát là một sàn đa cấp tiền số lừa đảo đang bị báo chí cảnh báo, việc cho bọn chúng thuê sảnh lớn sẽ làm hủy hoại hoàn toàn danh tiếng hạng A+ của tòa nhà Thành Tâm Financial Tower.",
  "Nhưng lúc này gã đã lâm vào đường cùng, nếu không có một trăm tỷ đó để bù đắp dòng tiền thâm hụt trước kỳ kiểm toán của Vietcombank, gã sẽ phải bóc lịch trong tù cả đời.",
  "Sáng hôm sau, sảnh chính của tòa nhà Thành Tâm Financial Tower được trang hoàng lộng lẫy bằng những lẵng hoa tươi đắt tiền và dải băng rôn đỏ rực rỡ.",
  "Hàng chục phóng viên báo chí, đại diện các ngân hàng thương mại BIDV và Vietcombank được Hùng mời đến tham dự buổi lễ ký kết hợp đồng hợp tác chiến lược giữa Ban Quản lý tòa nhà và Công ty Tài chính Thịnh Phát.",
  "Trần Quang Hùng diện bộ vest chỉnh tề nhất, bước lên bục phát biểu với nụ cười tự đắc, cố che giấu đi sự run rẩy trong ánh mắt.",
  "\"Kính thưa quý vị biểu khách, dưới sự quản lý xuất sắc của Ban quản lý chúng tôi, Thành Tâm Financial Tower liên tục đạt tỷ lệ lấp đầy kỷ lục,\" Hùng dõng dạc phát biểu vào micro.",
  "\"Hợp đồng ký kết hôm nay với tập đoàn tài chính Thịnh Phát trị giá hàng trăm tỷ đồng là minh chứng cho vị thế dẫn đầu của tòa nhà trên thị trường bất động sản thương mại hạng A+.\"",
  "Phan Bích Phượng đứng ở hàng ghế VIP phía dưới, cô mặc bộ đồ vest màu trắng tuyết thanh lịch, đôi mắt sắc lạnh nhìn chằm chằm vào màn kịch lố bịch của Hùng.",
  "Bên cạnh cô, các chuyên gia tài chính của Lotus Capital đã chuẩn bị sẵn sàng toàn bộ hồ sơ pháp lý để lật tẩy sàn đa cấp Thịnh Phát.",
  "Đúng lúc Trần Quang Hùng chuẩn bị đặt bút ký vào bản hợp đồng thuê khống, cửa sảnh lớn bỗng nhiên bị đẩy ra phát ra một tiếng động trầm đục.",
  "Một người đàn ông mặc bộ đồng phục đưa thư màu xanh thẫm sờn cũ, trên tay bê một chiếc thùng carton lớn màu nâu, bình thản sải bước đi thẳng vào trung tâm của buổi lễ.",
  "Đó chính là Đinh Xuân Phú.",
  "Sự xuất hiện đột ngột của một kẻ nghèo hèn bẩn thỉu ngay giữa một sự kiện sang trọng bậc nhất khiến toàn bộ quan khách và giới truyền thông xôn xao bàn tán.",
  "Trần Quang Hùng nhìn thấy Phú thì lập tức mặt đỏ gay vì giận dữ, gã cảm thấy thể diện của mình đang bị chà đạp nghiêm trọng trước mặt các đối tác lớn.",
  "Gã đập mạnh tay xuống bàn ký kết, hét lớn vào micro vang vọng khắp sảnh lớn:",
  "\"Bảo vệ đâu! Lũ ăn hại các người làm việc kiểu gì thế hả? Sao lại để một thằng đưa thư quèn, một kẻ rác rưởi bẩn thỉu như thế này vào phá hoại lễ ký kết trọng đại của chúng tôi?\"",
  "\"Lập tức bắt giữ nó lại! Còng tay nó lại rồi giải lên đồn công an cho tôi! Thằng này phạm tội xâm nhập bất hợp pháp và phá hoại tài sản doanh nghiệp!\"",
  "Bốn nhân viên bảo vệ to khỏe cầm gậy ba-toong lập tức lao tới, vây chặt lấy Phú định khống chế anh.",
  "Phú vẫn vô cùng điềm tĩnh, anh đặt nhẹ chiếc thùng carton xuống sàn đá Marble Carrara bóng loáng, ánh mắt anh nhìn thẳng vào Trần Quang Hùng đầy sự giễu cợt.",
  "Phan Bích Phượng lúc này từ hàng ghế VIP đứng thẳng dậy, gót giày cao gót nện xuống sàn đá vang lên âm thanh đanh thép.",
  "\"Dừng tay lại hết cho tôi!\" Phượng dõng dạc ra lệnh, giọng nói của cô đầy uy lực khiến đám bảo vệ vô thức khựng lại.",
  "Hùng nhìn Phượng cười khẩy: \"Cô Phan, cô định can thiệp vào công việc nội bộ của ban quản lý chúng tôi sao? Cô đừng quên Lotus Capital vẫn chưa ký hợp đồng gia hạn chính thức đâu nhé!\"",
  "Phượng không thèm liếc nhìn Hùng, cô bước nhanh tới đứng cạnh Phú, hướng về phía toàn thể quan khách và giới báo chí đang chĩa ống kính camera vào họ.",
  "\"Tôi tuyên bố cho tất cả quý vị và giới truyền thông được biết,\" Phượng dõng dạc nói, từng câu chữ rõ ràng như búa gõ.",
  "\"Người đàn ông mặc đồng phục đưa thư đang đứng trước mặt các vị đây...\"",
  "\"Chính là Chủ tịch Hội đồng Quản trị Tập đoàn Địa ốc Đinh Gia, chủ sở hữu tối cao hợp pháp duy nhất của tòa tháp Thành Tâm Financial Tower này!\"",
  "Lời tuyên bố của Phượng như một quả bom hạng nặng nổ tung ngay giữa sảnh lớn, khiến toàn bộ không gian lập tức rơi vào trạng thái im lặng đến đáng sợ.",
  "Trần Quang Hùng sững sờ, cây bút montblanc đắt tiền trên tay gã rơi bộp xuống bàn, môi gã giật giật liên hồi, mồ hôi lạnh chảy dài thành dòng trên khuôn mặt đang dần chuyển sang màu xám ngắt."
]

# CHƯƠNG 5
ch5_paragraphs = [
  "Sự im lặng bao trùm sảnh lớn của tòa nhà Thành Tâm Financial Tower ngột ngạt đến mức có thể nghe rõ cả tiếng gió rì rào thổi qua các khe cửa kính.",
  "Trần Quang Hùng đứng đờ người trên bục phát biểu, gã nhìn người đưa thư quèn trước mặt, rồi lại nhìn Phan Bích Phượng, bất chợt gã cười lên hô hố đầy điên cuồng.",
  "\"Ha ha ha! Cô Phan, cô điên rồi sao? Cô bị thằng đưa thư nghèo hèn này lừa tình hay sao mà lại dựng lên trò đùa lố bịch này?\" Hùng hét lớn, ngón tay chỉ thẳng vào mặt Phú.",
  "\"Một thằng bưu tá rách rưới lương tháng vài triệu đồng mà lại là Chủ tịch Đinh Gia sao? Nếu nó là chủ sở hữu tòa nhà này, thì tao chính là Hoàng đế nước Anh rồi!\"",
  "\"Bảo vệ! Đừng nghe mụ điên này nói nhảm! Lập tức tống cổ thằng đưa thư này vào ngục cho tao!\"",
  "Nhưng lực lượng bảo vệ không ai dám động đậy, bởi ngay lúc đó, tiếng còi xe cảnh sát rú vang dội từ phía ngoài hiên tòa nhà.",
  "Cánh cửa xoay pha lê của sảnh lớn một lần nữa mở toang, một đoàn người mặc vest đen sang trọng và đồng phục cảnh sát kinh tế bước vào với thần thái vô cùng uy nghiêm.",
  "Dẫn đầu đoàn người là Nguyễn Minh Tiến, Tổng giám đốc Chi nhánh Sở giao dịch Vietcombank, theo sau là Giám đốc Sở Xây dựng Thành Tâm và đội ngũ luật sư hàng đầu của hãng luật quốc tế Baker McKenzie.",
  "Nhìn thấy Nguyễn Minh Tiến, Trần Quang Hùng như bị sét đánh ngang tai, đầu gối gã run rẩy dữ dội, gã vội vã chạy xuống bục khúm núm chào đón.",
  "\"Dạ... chào Tổng giám đốc Tiến! Ngài đích thân đến tham dự lễ ký kết của chúng tôi sao? Thật là vinh hạnh cho ban quản lý...\" Hùng khúm núm đưa tay ra định bắt.",
  "Nhưng Nguyễn Minh Tiến hoàn toàn ngó lơ Hùng, vị tổng giám đốc ngân hàng quyền lực thẳng bước tới trước mặt Đinh Xuân Phú, gập người chín mươi độ kính cẩn cúi chào.",
  "\"Kính chào Chủ tịch Đinh! Tôi đã hoàn thành toàn bộ hồ sơ kiểm toán pháp y tài chính và chứng thư thế chấp gốc của tòa nhà theo lệnh của ngài!\" Tiến dõng dạc báo cáo.",
  "Phú từ từ tháo chiếc mũ lưỡi trai bưu tá bạc màu xuống, đưa tay chỉnh lại cổ áo sơ mi Savile Row đắt tiền ẩn bên dưới lớp áo đồng phục sờn cũ.",
  "Trong một khoảnh khắc, thần thái của anh hoàn toàn thay đổi, tỏa ra một khí thế vương giả và uy quyền tuyệt đối đè bẹp toàn bộ không gian sảnh lớn.",
  "Anh mở chiếc thùng carton trên bàn ra, lấy ra giấy chứng nhận sở hữu toàn tháp Thành Tâm Financial Tower đóng dấu đỏ của Bộ Tài nguyên và Môi trường đứng tên Đinh Xuân Phú.",
  "Cùng với đó là chứng thư giải chấp gốc khẳng định tập đoàn Đinh Gia sở hữu một trăm phần trăm tòa nhà mà không còn bất kỳ nghĩa vụ thế chấp quá hạn nào.",
  "\"Trần Quang Hùng, ông nhìn kỹ những thứ này xem là giấy lộn hay là quyền sở hữu tối cao?\" Phú bình thản nói, giọng nói trầm ấm vang vọng khắp sảnh lớn như sấm truyền.",
  "Hùng nhìn chằm chằm vào những con dấu đỏ chói và tên của Đinh Xuân Phú trên trang giấy, mắt gã trợn trừng lên, toàn thân run rẩy như cầy sấy.",
  "\"Chủ tịch Đinh... ngài... ngài thật sự là Chủ tịch Đinh Gia sao?\" Hùng lắp bắp, giọng nói lạc hẳn đi.",
  "Đầu gối gã quỳ cộp xuống sàn đá Marble Carrara lạnh buốt phát ra một âm thanh khô khốc, mồ hôi lạnh túa ra như tắm làm ướt sũng toàn bộ chiếc áo sơ mi hiệu Burberry đắt tiền.",
  "Gã nhớ lại cảnh tượng mình đã sỉ nhục Phú, giật giỏ thư ném xuống đất, và dùng mũi giày giẫm lên bàn tay của vị tỷ phú đứng đầu tập đoàn sở hữu vận mệnh của gã suốt một tháng qua.",
  "Nỗi sợ hãi tột cùng bóp nghẹt lấy cổ họng Hùng, khiến gã không thể thở nổi, khớp ngón tay bấu chặt xuống sàn đá đến mức rỉ máu đỏ tươi.",
  "\"Trần Quang Hùng, ông đã lợi dụng chức vụ Trưởng ban quản lý để thực hiện hàng loạt hành vi phạm pháp nghiêm trọng,\" Phú lạnh lùng tuyên bố từ trên cao nhìn xuống.",
  "\"Ông đã thông đồng với công ty sân sau để lập khống hóa đơn bảo trì hệ thống PCCC Hochiki trị giá bốn mươi lăm tỷ đồng, thay thế bằng thiết bị nhái loại hai gây mất an toàn nghiêm trọng cho hàng ngàn người trong tòa nhà.\"",
  "\"Ông còn tự ý thế chấp ngầm quyền khai thác bãi đỗ xe ngầm để lấy sáu mươi tỷ đồng từ tổ chức tín dụng đen để nướng vào chứng khoán thua lỗ.\"",
  "\"Hôm nay, tôi với tư cách là chủ sở hữu tối cao duy nhất của tòa nhà này, chính thức tuyên bố sa thải ông lập tức và chuyển giao toàn bộ hồ sơ phạm tội của ông cho cơ quan cảnh sát điều tra!\"",
  "Phú dứt lời, ba điều tra viên của Cục Cảnh sát điều tra tội phạm về tham nhũng, kinh tế, buôn lậu (C03) lập tức bước lên, xuất trình lệnh bắt tạm giam Trần Quang Hùng.",
  "Tiếng còng số tám bập vào cổ tay Hùng vang lên những tiếng lách cách lạnh lùng.",
  "Hùng gào khóc thảm thiết, bò rạp dưới chân Phú cầu xin sự tha thứ: \"Chủ tịch Đinh! Tôi sai rồi! Xin ngài tha cho tôi một con đường sống! Tôi sẽ trả lại tiền! Xin ngài...\"",
  "Nhưng Phú hoàn toàn ngó lơ, hai cảnh sát kinh tế dứt khoát lôi Hùng xềnh xệch ra xe biển xanh trước sự chứng kiến và ghi hình của hàng chục phóng viên báo đài.",
  "Đại diện của sàn đa cấp lừa đảo Thịnh Phát Coin cũng hoảng loạn bỏ chạy khỏi hiện trường nhưng lập tức bị lực lượng an ninh tòa nhà giữ lại để phối hợp điều tra.",
  "Phú quay sang Phan Bích Phượng, người nãy giờ vẫn đứng bên cạnh anh với nụ cười sòng phẳng, tự tin.",
  "Anh đưa tay ra trước mặt cô, ánh mắt tràn đầy sự tán thưởng và tin cậy: \"Cô Phan, hợp đồng gia hạn mười tầng văn phòng của Lotus Capital đã được chuẩn bị sẵn sàng.\"",
  "\"Mức phí quản lý sẽ là không phẩy năm phần trăm ròng như cô yêu cầu, và Lotus Capital có quyền phủ quyết tuyệt đối đối với tất cả các khách thuê thương mại liền kề để bảo vệ danh tiếng hạng A+ của tòa nhà.\"",
  "Phượng đưa tay ra bắt lấy tay Phú, ngón tay cô khẽ run nhẹ vì phấn khích trước một chiến thắng pháp lý và thương trường hoàn mỹ.",
  "\"Rất vinh hạnh được hợp tác lâu dài với ngài, thưa Chủ tịch Đinh,\" Phượng mỉm cười rạng rỡ.",
  "Dưới ánh hoàng hôn rực rỡ của thành phố Thành Tâm, đỉnh tháp Thành Tâm Financial Tower lấp lánh như một ngọn hải đăng kiêu hãnh của sự thịnh vượng.",
  "Quyền lực hạng A đã được thiết lập lại một cách tuyệt đối, khẳng định vị thế độc tôn của những kẻ dùng trí tuệ và pháp lý để làm chủ vận mệnh."
]

# Chuyển đổi mỗi đoạn thành cấu trúc HTML V12: mỗi dòng/câu là 1 thẻ <p>
# Để đáp ứng >= 1100 từ mỗi chương, chúng ta cần đảm bảo các chương có số lượng từ dồi dào.
# Hãy kiểm tra số từ của mỗi chương và tạo chuỗi HTML chính xác.

chapters_data = []

# Chương 1
content_ch1 = ""
for p in ch1_paragraphs:
    content_ch1 += f"<p>{p}</p>\n"
chapters_data.append({
    "title": "Chương 1: Lá Thư Và Kẻ Lên Mặt",
    "content": content_ch1
})

# Chương 2
content_ch2 = ""
for p in ch2_paragraphs:
    content_ch2 += f"<p>{p}</p>\n"
chapters_data.append({
    "title": "Chương 2: Đàm Phán Hạng A",
    "content": content_ch2
})

# Chương 3
content_ch3 = ""
for p in ch3_paragraphs:
    content_ch3 += f"<p>{p}</p>\n"
chapters_data.append({
    "title": "Chương 3: Pháp Y Tài Chính Và Lỗ Hổng 100 Tỷ",
    "content": content_ch3
})

# Chương 4
content_ch4 = ""
for p in ch4_paragraphs:
    content_ch4 += f"<p>{p}</p>\n"
chapters_data.append({
    "title": "Chương 4: Bẫy Sập Tại Phòng Khánh Tiết",
    "content": content_ch4
})

# Chương 5
content_ch5 = ""
for p in ch5_paragraphs:
    content_ch5 += f"<p>{p}</p>\n"
chapters_data.append({
    "title": "Chương 5: Quyền Lực Hạng A Lật Kèo",
    "content": content_ch5
})

novel_data["chapters"] = chapters_data

# In số từ ra màn hình để kiểm tra
for idx, ch in enumerate(chapters_data):
    words = count_words(ch["content"])
    print(f"Chương {idx+1}: {words} từ")

# Ghi file JSON
output_path = "/Users/aaronnguyen/TN/App/doctieuthuyet/scratch/draft_novel_24.json"
os.makedirs(os.path.dirname(output_path), exist_ok=True)
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(novel_data, f, ensure_ascii=False, indent=2)

print(f"Đã ghi bản thảo vào {output_path} thành công!")
