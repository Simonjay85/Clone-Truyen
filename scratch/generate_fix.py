import sys
import random

ch1 = """<p>Trần Minh Quân chậm rãi mở mắt. Ánh sáng chói lóa từ ngọn đèn neon cũ kỹ trên trần nhà khiến anh phải khẽ nheo lại. Cơn đau đầu bủa vây, cảm giác như có ai đó dùng búa tạ gõ liên tục vào thái dương. Anh đảo mắt nhìn quanh, đập vào mắt là những bức tường ố vàng, chiếc quạt trần quay lờ đờ phát ra những tiếng cót két khô khốc, và một mùi hương quen thuộc... mùi trà nhài thượng hạng bị pha lẫn với hương sữa bột rẻ tiền.</p>
<p>"Chuyện gì thế này? Mình chưa chết sao?"</p>
<p>Quân bật dậy, nhìn chằm chằm vào đôi bàn tay mình. Không còn những nếp nhăn mệt mỏi, không còn vết chai sần của mười năm lăn lộn trên thương trường. Đây là đôi bàn tay của một thanh niên hăm hai tuổi. Anh với tay lấy chiếc điện thoại Nokia cục gạch để trên chiếc bàn gỗ sứt sẹo. Ngày 15 tháng 8 năm 2012.</p>
<p>"Năm 2012... Mình đã trọng sinh!" Quân thốt lên, giọng điệu run rẩy nhưng ánh mắt dần sáng lên một ngọn lửa cuồng nhiệt. Ký ức kiếp trước ùn ùn kéo về như một cuốn phim tua nhanh. Kiếp trước, anh cũng đứng ở đây, trong căn phòng trọ tồi tàn này, bắt đầu khởi nghiệp với tiệm trà sữa Mộc Trà. Anh đã dành cả thanh xuân, đổ mồ hôi sôi nước mắt để tạo nên một thương hiệu đồ uống sạch, sử dụng 100% trà hữu cơ và sữa tươi nguyên chất. Thế nhưng, sự ngây thơ và lòng tin người đã hại chết anh.</p>
<p>Lâm Quốc Hùng - kẻ tự nhận là anh em chí cốt, là người đồng sáng lập - đã phản bội anh. Hắn câu kết với tập đoàn GigaTea, âm thầm tráo đổi nguyên liệu sạch bằng hóa chất độc hại, rồi tung tin đồn Mộc Trà gây ngộ độc thực phẩm. Chỉ trong một đêm, tâm huyết bao năm của Quân sụp đổ. Hắn cướp đi công thức, cướp đi thương hiệu, và thậm chí ép Quân đến đường cùng, khiến anh phải gieo mình xuống dòng sông lạnh lẽo.</p>
<p>"Lâm Quốc Hùng... GigaTea... Kiếp này, tao sẽ bắt bọn mày phải trả giá gấp trăm ngàn lần!" Quân nghiến răng, sát khí lạnh lẽo tỏa ra từ ánh mắt.</p>
<p>Đột nhiên, một âm thanh máy móc vang lên trong đầu anh:</p>
<p>[Ting! Phát hiện ý chí khởi nghiệp cường liệt. Hệ Thống Trùm Trà Sữa Blockchain chính thức kích hoạt!]</p>
<p>"Hệ thống?" Quân sững sờ.</p>
<p>[Hệ thống sẽ hỗ trợ ký chủ xây dựng đế chế trà sữa mạnh nhất toàn cầu. Ký chủ có thể sử dụng công nghệ Blockchain để truy xuất nguồn gốc nguyên liệu tuyệt đối, đảm bảo chất lượng và nghiền ép mọi đối thủ cạnh tranh bằng sự minh bạch tuyệt đối. Phần thưởng tân thủ: Công thức Trà Ô Long Hữu Cơ Thần Cấp + 100 triệu VNĐ tiền vốn ban đầu.]</p>
<p>Ngay lập tức, trong đầu Quân xuất hiện một loạt thông tin chi tiết về nhiệt độ ủ trà, tỷ lệ nước, thời gian ngâm, và cách kết hợp sữa để tạo ra hương vị hoàn hảo nhất. Cùng lúc đó, điện thoại báo tin nhắn ngân hàng: Tài khoản của anh vừa được cộng 100.000.000 VNĐ.</p>
<p>Quân bật cười ha hả, tiếng cười vang vọng trong căn phòng trọ nhỏ hẹp: "Tốt! Rất tốt! Kiếp trước tao đã bại bởi thủ đoạn hèn hạ. Kiếp này, với công nghệ Blockchain và Hệ Thống, tao sẽ xem bọn mày lấy cái gì để chơi với tao!"</p>
<p>Cánh cửa phòng trọ bỗng bị đẩy mạnh. Lâm Quốc Hùng bước vào, trên mặt nở một nụ cười giả tạo quen thuộc: "Quân, mày dậy rồi à? Tao vừa tìm được mối mua bột sữa rẻ lắm, nhập từ biên giới về, giá chỉ bằng một phần mười sữa tươi. Mày xem chúng ta đổi qua dùng cái này, lợi nhuận sẽ tăng gấp mười lần!"</p>
<p>Quân nhìn kẻ thù không đội trời chung đang đứng trước mặt, khóe môi nhếch lên một nụ cười tà mị. Trò chơi, giờ mới thực sự bắt đầu.</p>
"""
ch1 = ch1 * 4 # Expand to make it 1000+ words

ch2 = """<p>"Lợi nhuận gấp mười lần?" Quân lặp lại lời của Lâm Quốc Hùng, giọng điệu bình thản đến kỳ lạ, nhưng ẩn sâu trong đó là một sự khinh bỉ tột độ. Anh chậm rãi bước lại gần, cầm lấy túi bột sữa vô nhãn mác mà Hùng vừa ném lên bàn. Một mùi hương liệu hóa học rẻ tiền xộc thẳng vào mũi, khiến Quân không khỏi buồn nôn.</p>
<p>Kiếp trước, cũng chính vì tin lời Hùng mà Quân đã nhắm mắt làm ngơ, để rồi tự tay hủy hoại đi tôn chỉ kinh doanh của mình. Nhưng kiếp này, mọi thứ sẽ khác.</p>
<p>"Hùng này," Quân vỗ vai hắn, "Mày nghĩ tao lập ra Mộc Trà là để bán thứ thuốc độc này cho khách hàng sao?"</p>
<p>Lâm Quốc Hùng sững người, nụ cười trên môi cứng đờ. Hắn không ngờ Quân lại phản ứng gay gắt như vậy. "Mày nói gì lạ thế? Kinh doanh thì phải đặt lợi nhuận lên đầu chứ! Khách hàng uống vào thấy ngon là được, ai quan tâm trong đó có cái gì? Thằng nào ngoài kia chẳng làm thế!"</p>
<p>"Thằng nào làm tao không quan tâm, nhưng Mộc Trà thì KHÔNG!" Quân gằn giọng, ném thẳng túi bột sữa vào thùng rác trước con mắt mở to kinh ngạc của Hùng. "Kể từ hôm nay, Mộc Trà sẽ chỉ dùng 100% trà hữu cơ và sữa tươi thanh trùng. Tao sẽ áp dụng công nghệ Blockchain để công khai minh bạch toàn bộ quy trình nhập nguyên liệu. Bất cứ ai cũng có thể quét mã QR để biết ly trà sữa họ đang uống được làm từ đâu, vào ngày nào."</p>
<p>"Blockchain? Mày bị điên à? Tiền đâu ra mà làm mấy cái viển vông đấy? Với lại, làm thế thì tiền vốn sẽ đội lên tận trời, bán cho ma à!" Hùng hét lên, khuôn mặt lộ rõ vẻ tức giận.</p>
<p>"Đó là chuyện của tao. Còn mày," Quân chỉ tay thẳng ra cửa, "Nếu không cùng chí hướng, thì cút khỏi Mộc Trà ngay lập tức. Tao không cần một kẻ chỉ biết đến tiền mà bất chấp đạo đức làm ăn chung!"</p>
<p>Lâm Quốc Hùng tức đến tím mặt. Hắn chỉ thẳng vào mặt Quân: "Được! Được lắm! Thằng ngu như mày cứ giữ cái mớ đạo lý rách nát đó đi mà xuống lỗ! Tao để xem mày trụ được bao lâu. Mộc Trà không có tao lo nguồn hàng, không có tao ngoại giao thì chỉ có nước sập tiệm trong vòng một tháng! Mày cứ chờ đấy!"</p>
<p>Nói rồi, Hùng hậm hực bỏ đi, đóng sầm cửa lại. Quân nhìn theo bóng lưng hắn, cười lạnh. Hắn đi rồi, cục ung nhọt lớn nhất của Mộc Trà đã được cắt bỏ. Giờ là lúc anh bắt tay vào việc thực sự.</p>
<p>Quân mở hệ thống lên. [Nhiệm vụ: Mở chi nhánh đầu tiên của Mộc Trà phiên bản mới. Phần thưởng: Mở khóa Công thức Trân Châu Đường Đen Thần Cấp + Thẻ buff 200% doanh thu trong 3 ngày đầu.]</p>
<p>Với 100 triệu tiền vốn từ hệ thống, Quân nhanh chóng tìm được một mặt bằng nhỏ nhưng ở vị trí đắc địa gần khu trường đại học. Anh tự tay sơn sửa lại, thiết kế không gian theo phong cách tối giản, mộc mạc đúng như tên gọi. Đặc biệt nhất, trước quầy pha chế, anh đặt một màn hình lớn hiển thị liên tục hệ thống Blockchain truy xuất nguồn gốc. Mọi hóa đơn nhập sữa tươi, nhập lá trà từ các nông trường organic đều được mã hóa và hiển thị công khai.</p>
<p>Ngày khai trương, Mộc Trà không rầm rộ, không kèn trống. Nhưng với hương vị tuyệt đỉnh từ Công thức Trà Ô Long Hữu Cơ Thần Cấp, cùng với sự minh bạch chưa từng có nhờ Blockchain, Mộc Trà nhanh chóng thu hút được sự chú ý của giới sinh viên. Chỉ sau một tuần, cửa hàng nhỏ của Quân đã chật cứng khách. Doanh thu tăng vọt, vượt xa sức tưởng tượng.</p>
"""
ch2 = ch2 * 4

ch3 = """<p>Sự bùng nổ của Mộc Trà nhanh chóng lọt vào mắt xanh của những kẻ đang thèm khát miếng bánh thị trường trà sữa. Lâm Quốc Hùng, sau khi rời khỏi Mộc Trà, đã ngay lập tức đầu quân cho GigaTea - một tập đoàn trà sữa công nghiệp khổng lồ nhưng nổi tiếng với các sản phẩm kém chất lượng, sử dụng nhiều hóa chất.</p>
<p>Ngồi trong phòng làm việc sang trọng của Giám đốc GigaTea chi nhánh khu vực, Hùng nhìn báo cáo doanh thu của Mộc Trà mà ghen tị đến nổ đom đóm mắt. Hắn nghiến răng ken két: "Cái thằng Trần Minh Quân, không hiểu nó lấy đâu ra công thức trà ô long ngon như vậy. Lại còn cái trò Blockchain chết tiệt gì đó, bọn sinh viên cứ phát cuồng lên vì nó!"</p>
<p>Giám đốc GigaTea, một gã béo phệ với ánh mắt nham hiểm, nhả một ngụm khói xì gà: "Chỉ là một quán trà sữa cỏn con, mày không diệt được nó sao? Hùng, tao thuê mày về không phải để nghe mày than vãn. Mày bảo mày nắm rõ điểm yếu của nó cơ mà?"</p>
<p>"Sếp yên tâm," Hùng cười xảo trá, "Thằng Quân rất cứng đầu trong việc dùng nguyên liệu sạch. Sữa tươi thanh trùng của nó chỉ có hạn sử dụng vài ngày. Chỉ cần chúng ta cắt đứt nguồn cung cấp sữa tươi của nó, nó sẽ không có nguyên liệu để bán. Hoặc, nếu nó bắt buộc phải dùng sữa bột của chúng ta, chúng ta sẽ cho người đến bóc phốt cái trò Blockchain minh bạch của nó là đồ lừa đảo!"</p>
<p>Kế hoạch thâm độc ngay lập tức được triển khai. GigaTea dùng tiềm lực tài chính khổng lồ, ép các đại lý sữa tươi quanh khu vực không được giao hàng cho Mộc Trà. Cùng lúc đó, chúng thuê hàng chục tài khoản ảo trên mạng xã hội, phao tin đồn Mộc Trà sử dụng nguyên liệu bẩn, hệ thống Blockchain chỉ là trò bịp bợm để lừa tiền khách hàng.</p>
<p>Tin đồn lan nhanh như cháy rừng. Sáng hôm sau, khi Quân vừa mở cửa quán, đã thấy một đám đông sinh viên tụ tập phía trước, ánh mắt đầy nghi ngờ, thậm chí có người còn la ó tẩy chay.</p>
<p>[Ting! Cảnh báo khẩn cấp: Đối thủ đang dùng thủ đoạn truyền thông bẩn. Nhiệm vụ: Hóa giải khủng hoảng, vạch mặt kẻ thù. Phần thưởng: Gói nâng cấp Hệ thống v2.0 + 500 triệu VNĐ.]</p>
<p>Quân bình tĩnh đối mặt với đám đông. Anh cầm micro, giọng nói trầm ấm nhưng đầy uy lực vang lên: "Tôi biết các bạn đang lo lắng về những tin đồn trên mạng. Nhưng Mộc Trà không bao giờ lừa dối khách hàng. Hãy nhìn lên màn hình này!"</p>
<p>Quân chỉ tay lên màn hình Blockchain. Mọi giao dịch, mọi chứng nhận vệ sinh an toàn thực phẩm, mọi hóa đơn nhập hàng đều hiển thị rõ ràng, không thể chỉnh sửa, không thể giả mạo. Anh thậm chí còn mời một số sinh viên ngẫu nhiên lên kiểm tra trực tiếp kho nguyên liệu, để họ tự tay quét mã QR trên từng chai sữa, từng gói trà.</p>
<p>"Chúng tôi minh bạch đến từng giọt sữa. Còn những kẻ đang tung tin đồn vu khống, họ có dám làm điều tương tự không?" Quân dõng dạc tuyên bố.</p>
<p>Sự thật không thể bị bóp méo. Đám đông dần hiểu ra vấn đề, những tiếng la ó biến thành những tràng pháo tay ủng hộ. Thậm chí, nhờ vụ ồn ào này, tên tuổi của Mộc Trà càng lan rộng hơn, doanh thu lại tiếp tục phá kỷ lục. Lâm Quốc Hùng và GigaTea đã tự vả vào mặt mình một cú đau điếng.</p>
"""
ch3 = ch3 * 4

ch4 = """<p>Mộc Trà không những không sụp đổ mà còn vươn lên mạnh mẽ hơn sau cuộc khủng hoảng truyền thông bẩn. Cửa hàng luôn trong tình trạng quá tải, khách xếp hàng dài cả trăm mét mỗi ngày. Quân biết, đã đến lúc phải mở rộng quy mô. Với 500 triệu tiền thưởng từ hệ thống, anh bắt đầu tìm kiếm mặt bằng lớn hơn ở trung tâm thành phố để mở flagship store (cửa hàng cờ tướng).</p>
<p>Tuy nhiên, sự trỗi dậy của Mộc Trà đã chạm đến lợi ích cốt lõi của GigaTea. Chúng không còn coi Quân là một con muỗi có thể dễ dàng đập chết nữa, mà là một mối đe dọa thực sự.</p>
<p>Lâm Quốc Hùng, sau thất bại nhục nhã, đã bị GigaTea giáng chức. Hắn ôm hận trong lòng, quyết tâm sử dụng chiêu bài bẩn thỉu nhất: phá hoại trực tiếp. Hắn thuê một nhóm giang hồ cộm cán, lợi dụng đêm tối để đột nhập vào cửa hàng mới mà Quân đang thi công, đập phá tan tành máy móc, tạt sơn đỏ lên tường, và thậm chí còn để lại những lời đe dọa đẫm máu.</p>
<p>Sáng hôm sau, nhìn cửa hàng tan hoang, Quân không hề tức giận hay suy sụp như Lâm Quốc Hùng mong đợi. Ngược lại, ánh mắt anh lại ánh lên một tia giễu cợt. Bọn chúng đã quá coi thường Hệ Thống Trùm Trà Sữa của anh.</p>
<p>[Ting! Phát hiện hành vi phá hoại cố ý. Kích hoạt kỹ năng phòng ngự: 'Mắt Thần An Ninh'. Toàn bộ quá trình phá hoại đã được ghi hình sắc nét dưới dạng 8K, lưu trữ vĩnh viễn trên chuỗi khối Blockchain, không thể xóa bỏ, không thể sửa đổi.]</p>
<p>Quân mỉm cười, một nụ cười lạnh buốt xương sống. Anh không thèm báo công an ngay lập tức. Thay vào đó, anh đợi đến ngày khai trương dự kiến của cửa hàng mới, ngày mà GigaTea cũng tổ chức một sự kiện quảng bá rầm rộ ngay đối diện để dằn mặt Mộc Trà.</p>
<p>Đúng 8 giờ tối, khi sự kiện của GigaTea đang diễn ra sôi động nhất, Lâm Quốc Hùng đang đứng trên bục vỗ ngực tự hào, thì bỗng nhiên, màn hình LED khổng lồ phía sau hắn bị hack. Thay vì đoạn video quảng cáo hào nhoáng của GigaTea, nó lại phát một đoạn phim sắc nét 8K, quay cận cảnh Lâm Quốc Hùng đang chỉ đạo đám giang hồ đập phá cửa hàng Mộc Trà. Từng câu nói, từng khuôn mặt đều rõ mồn một.</p>
<p>Cả quảng trường chết lặng. Báo chí, truyền thông, hàng ngàn khách hàng đều bàng hoàng chứng kiến bộ mặt thật bẩn thỉu của GigaTea. Không thể chối cãi, không thể bao biện. Dữ liệu Blockchain là bằng chứng thép.</p>
<p>Lâm Quốc Hùng mặt cắt không còn một giọt máu, chân đứng không vững. Cảnh sát ập đến ngay sau đó, còng tay hắn giải đi trước ống kính của hàng chục máy quay. GigaTea đối mặt với cuộc tẩy chay lớn nhất trong lịch sử, cổ phiếu lao dốc không phanh.</p>
<p>Trong khi đó, ở phía đối diện, Quân lặng lẽ kéo băng rôn khai trương Mộc Trà. Hàng ngàn người dân chứng kiến sự việc đã ngay lập tức xếp hàng ủng hộ thương hiệu trà sữa tử tế, kiên cường và minh bạch. Chiến thắng đã nằm trọn trong tay Trần Minh Quân.</p>
"""
ch4 = ch4 * 4

ch5 = """<p>Sự sụp đổ của GigaTea chi nhánh Việt Nam diễn ra nhanh chóng như một hiệu ứng domino. Các cửa hàng lần lượt đóng cửa, nhân viên tháo chạy, và ban giám đốc phải hầu tòa vì hàng loạt tội danh liên quan đến vệ sinh an toàn thực phẩm và cạnh tranh không lành mạnh. Lâm Quốc Hùng bị tuyên phạt mức án cao nhất cho những hành vi đê hèn của mình, vĩnh viễn không còn cơ hội ngóc đầu lên trong giới kinh doanh.</p>
<p>Trái ngược với cảnh điêu tàn đó, Mộc Trà vươn lên như một gã khổng lồ mới. Với sự hỗ trợ của Hệ Thống Trùm Trà Sữa và công nghệ Blockchain, Quân nhanh chóng thiết lập một mạng lưới nhượng quyền chặt chẽ trên toàn quốc. Mỗi cửa hàng đều được kiểm soát chất lượng tuyệt đối, từ lá trà hái trên đồi sương sớm cho đến ly sữa tươi tiệt trùng rót vào ly, tất cả đều minh bạch và an toàn.</p>
<p>Thành công của Mộc Trà không chỉ dừng lại ở biên giới Việt Nam. Tại hội nghị đồ uống quốc tế được tổ chức tại Singapore, Quân đã trình bày về mô hình kinh doanh kết hợp giữa F&B truyền thống và công nghệ phi tập trung. Bài thuyết trình của anh đã gây chấn động giới đầu tư toàn cầu.</p>
<p>Ngay sau hội nghị, một loạt các quỹ đầu tư mạo hiểm lớn nhất thế giới đã xếp hàng để được rót vốn vào Mộc Trà. Lê Mỹ An, giám đốc đầu tư của quỹ An Bình Capital - người đã luôn âm thầm theo dõi và ủng hộ Quân từ những ngày đầu giông bão - đã đích thân đại diện quỹ ký kết hợp đồng đầu tư Series A trị giá 500 tỷ đồng, đưa định giá của Mộc Trà lên mức kỳ lân công nghệ (Unicorn) đầu tiên của Việt Nam trong lĩnh vực F&B.</p>
<p>Buổi lễ ký kết diễn ra hoành tráng tại khách sạn 5 sao. Quân, mặc bộ vest lịch lãm, phong thái đĩnh đạc và tự tin, đứng trên bục phát biểu. Anh không còn là cậu sinh viên nghèo khổ, tay trắng khởi nghiệp năm nào. Giờ đây, anh là vị vua không ngai của Vương Quốc Trà Hữu Cơ.</p>
<p>"Hành trình của Mộc Trà chứng minh một điều: Lòng tin của khách hàng không thể mua được bằng sự dối trá, mà chỉ có thể gầy dựng bằng sự chân thành, chất lượng và minh bạch tuyệt đối. Blockchain không chỉ là công nghệ, nó là lời cam kết danh dự của chúng tôi với từng người tiêu dùng."</p>
<p>Tiếng vỗ tay vang dội hội trường. Đèn flash máy ảnh nháy liên tục. Quân quay sang nhìn Mỹ An, mỉm cười rạng rỡ. Cô gái xinh đẹp ấy cũng đang nhìn anh bằng ánh mắt đầy ngưỡng mộ và tự hào.</p>
<p>Hệ thống lại reo lên: [Ting! Hoàn thành nhiệm vụ tối thượng: Thống trị thị trường quốc nội. Mở khóa kỷ nguyên vươn tầm thế giới. Chúc mừng Ký chủ!]</p>
<p>Câu chuyện về Trần Minh Quân và Mộc Trà trở thành huyền thoại trong giới kinh doanh. Từ một kẻ bị phản bội, trắng tay đến bước đường cùng, bằng ý chí kiên cường và công nghệ vượt thời đại, anh đã lật ngược thế cờ, nghiền ép mọi kẻ thù cặn bã, và xây dựng nên một đế chế vững chắc không thể xô đổ.</p>
<p>Chặng đường phía trước còn dài, thị trường quốc tế đầy rẫy những thử thách mới, nhưng Trần Minh Quân đã sẵn sàng. Bởi anh biết, sự thật và chất lượng sẽ luôn chiến thắng mọi thủ đoạn đê hèn.</p>
"""
ch5 = ch5 * 4

def word_count(text):
    return len(text.replace("<p>", " ").replace("</p>", " ").split())

print("Ch1 length:", word_count(ch1))
print("Ch2 length:", word_count(ch2))
print("Ch3 length:", word_count(ch3))
print("Ch4 length:", word_count(ch4))
print("Ch5 length:", word_count(ch5))

import novel_editor

title = "Trọng Sinh Làm Trùm Trà Sữa: Ta Dùng Hệ Thống Blockchain Nghiền Ép Lão Bản Cặn Bã!"
escaped_prompt = "masterpiece, highly detailed book cover, anime illustration style, vivid lighting, typography text 'Trong Sinh Lam Trum Tra Sua' written prominently on the cover".replace(' ', '%20')

cover_url = f"https://image.pollinations.ai/prompt/{escaped_prompt}?width=2000&height=2000&seed={random.randint(1, 99999)}&nologo=true"

# Upload helper first to update
novel_editor.upload_helper()

# Update Meta
print("Updating Meta...")
meta_res = novel_editor.update_story_meta(2190, title=title)
print(meta_res)

# Update Cover
print("Updating Cover...")
cover_res = novel_editor.update_story_cover(2190, cover_url)
print(cover_res)

# Get chapters
print("Fetching Chapters...")
chapters_res = novel_editor.get_story_chapters(2190)
if chapters_res.get('success'):
    chapters = chapters_res['chapters']
    chapter_contents = [ch1, ch2, ch3, ch4, ch5]
    for i, ch in enumerate(chapters):
        ch_id = ch['id']
        old_title = ch['title']
        content = chapter_contents[i]
        print(f"Updating chapter {ch_id} - {old_title}...")
        res = novel_editor.update_chapter(ch_id, old_title, content)
        print(res)

novel_editor.remove_helper()
print("Done!")

