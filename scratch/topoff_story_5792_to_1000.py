import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HELPER = ROOT / "scratch" / "novel_editor.py"
spec = importlib.util.spec_from_file_location("novel_editor", HELPER)
editor = importlib.util.module_from_spec(spec)
spec.loader.exec_module(editor)

STORY_ID = 5792

ADDITIONS = {
    5794: """
Buổi tối hôm đó, Bảo không về ngay. Anh ngồi ở trạm xe buýt đối diện salon, nhìn tấm bảng đèn vẫn sáng và nghe tiếng nhạc trong tiệm vọng ra như một thứ nhắc nhở cay nghiệt. Chiếc kéo cũ nằm trong túi vải đập nhẹ vào đùi mỗi lần anh đổi tư thế. Nó không phải vật quý theo giá tiền, nhưng là thứ mẹ anh đã cầm suốt mười mấy năm trong căn phòng thuê chật, cắt tóc cho công nhân, sinh viên, người bán vé số, ai thiếu thì ghi nợ.

Một tin nhắn của chị thu ngân cũ hiện lên: "Anh đừng quay lại xin. Anh Hiếu nói ai nói giúp anh cũng bị trừ lương." Bảo đọc xong thì tắt màn hình. Anh không giận chị. Người nghèo thường phải học cách im lặng trước khi học cách phản kháng. Nhưng câu "mày cắt rẻ thì biến" cứ cào trong cổ họng anh. Anh lấy cuốn sổ nhỏ ra, ghi từng dòng: ghế nhựa, gương treo, khăn sạch, bình xịt, cồn sát khuẩn, tông đơ dự phòng, bảng giá rõ ràng. Dưới cùng, anh viết: "Không xin quay lại. Mở chỗ của mình."

Sáng hôm sau, khi đi ngang qua khu chợ lao động, Bảo thấy một bác xe ôm đang lấy tay vuốt mái tóc dài lòa xòa vì nóng. Bác hỏi tiệm nào cắt rẻ, người bán nước chỉ vào cuối phố rồi nói nhỏ: "Toàn tám chục, trăm hai, bác chịu không?" Bảo đứng khựng lại. Anh hiểu cái giá năm mươi nghìn ở salon sang không đắt với khách văn phòng, nhưng với người chạy xe cả ngày, nó là bữa cơm. Cơn xấu hổ vì bị đuổi bỗng chuyển thành một thứ rõ ràng hơn: nếu không có chỗ cho những người ấy, anh sẽ tự tạo ra chỗ đó.
""",
    5795: """
Ngày đầu mở ghế, Bảo chuẩn bị kỹ hơn vẻ ngoài lụp xụp của một góc vỉa hè. Anh trải một tấm bạt sạch dưới chân ghế, để riêng hộp kéo đã lau cồn, kẹp khăn trắng vào túi nilon mới, dán bảng giá bằng bút lông: "Cắt gọn 30K, trẻ em 20K, ai khó quá cứ nói." Dòng cuối khiến mấy người đi ngang bật cười, nhưng cũng làm họ dừng lại lâu hơn. Một ông bảo vệ hỏi: "Khó quá là sao?" Bảo đáp: "Là hôm nay bác chưa có tiền cũng vẫn được cắt. Lần sau trả, hoặc không trả cũng không sao."

Tin ấy lan rất nhanh trong con hẻm phía sau chợ. Người đầu tiên ngồi xuống là bác xe ôm hôm qua. Bảo không cắt vội. Anh hỏi bác thường đội mũ bảo hiểm bao lâu, tóc có hay bết mồ hôi không, muốn gọn để chạy xe hay muốn nhìn trẻ ra khi về nhà. Bác cười: "Có ai cắt tóc mà hỏi kỹ dữ vậy?" Bảo nói: "Cắt rẻ không có nghĩa là cắt ẩu." Mười lăm phút sau, bác soi gương nhựa, im vài giây rồi móc thêm mười nghìn. Bảo đẩy lại. Bác nhét vào hộp khăn: "Cho thằng sau không có tiền."

Đến trưa, nắng hắt xuống mặt đường nóng hầm hập. Bảo treo thêm một chai nước lọc miễn phí bên cạnh ghế, ai chờ thì uống. Một cô lao công ngại ngùng hỏi có cắt tóc nữ không, vì tiệm gần nhà đòi uốn duỗi mới chịu làm. Bảo chỉ cười, lấy kẹp chia tóc, tỉa lại phần đuôi khô và chỉnh mái cho gọn. Cô nhìn mình trong gương, bàn tay chai sần cứ vuốt mãi phần tóc vừa cắt. "Lâu rồi cô mới thấy mình sạch sẽ vậy," cô nói. Câu ấy làm Bảo đứng lặng. Anh biết chiếc ghế nhựa bắt đầu có ý nghĩa lớn hơn một chỗ kiếm tiền.
""",
    5796: """
Video triệu view không đến từ một màn quảng cáo được dựng sẵn, mà từ sự tử tế bị người ta bắt gặp đúng lúc. Chiều đó, mưa kéo đến rất nhanh. Một cậu sinh viên chạy xe giao hàng ghé vào, tóc ướt dính trên trán, nói chỉ còn hai mươi nghìn vì vừa đền khách một ly trà sữa đổ. Bảo kéo ghế vào dưới mái hiên, đưa cậu cái khăn khô rồi bảo: "Ngồi đi. Hai mươi cũng được." Cô bé quay clip ban đầu chỉ định ghi cảnh mưa, nhưng khi nghe câu ấy, điện thoại vô thức hướng về phía Bảo.

Trong clip, Bảo cắt tóc bằng nhịp tay rất chắc. Anh không nói đạo lý, chỉ dặn cậu sinh viên lần sau chạy mưa nhớ đội áo mưa kín cổ, tóc để dày quá dễ bệnh. Khi cậu đứng dậy, gương mặt sáng hẳn ra, cậu cúi đầu cảm ơn rồi hỏi khi nào có tiền có thể quay lại trả thêm không. Bảo đáp: "Khi em khá hơn thì cắt cho người khác một lần tử tế là được." Câu đó bị cắt thành đoạn ngắn, đăng kèm dòng chữ: "Thợ bị đuổi vì cắt rẻ, giờ cắt tóc bằng lòng tự trọng."

Tối ấy điện thoại Bảo rung liên tục. Có người hỏi địa chỉ, có người gửi ảnh tóc, có người chuyển khoản trước ba mươi nghìn dù chưa đến cắt. Nhưng cũng có bình luận mỉa mai: "Làm màu thôi, vài bữa tăng giá." Bảo đọc hết, rồi ghim một bình luận của chính mình: "Tôi sẽ tăng chất lượng trước, không tăng giá trước." Sáng hôm sau, hàng người xếp trước ghế nhựa dài tới tiệm bánh mì. Bảo phải phát số viết tay trên mảnh giấy bìa, mỗi số kèm giờ ước tính để mọi người khỏi chờ vô ích. Một bà cụ bảo: "Cậu nổi tiếng rồi, chắc không cắt cho người già nữa đâu." Bảo nghiêng ghế, đỡ bà ngồi xuống đầu tiên: "Con nổi tiếng vì những người như bà, sao lại quên được."
""",
    5797: """
Salon Đẹp Plus không chịu thua vì mất vài khách; họ sợ mất quyền định nghĩa thế nào là "sang". Hiếu cho nhân viên lập tài khoản ẩn, đăng ảnh vỉa hè kèm chữ "dao kéo không vệ sinh", "cắt tóc phá giá", "ngồi lề đường coi chừng nấm da đầu". Những dòng ấy đánh trúng nỗi sợ của khách mới. Sáng hôm sau, hàng chờ trước ghế Bảo thưa hẳn. Một chị văn phòng tới rồi lại quay đi vì đọc được bài bóc phốt. Bảo nhìn thấy nhưng không gọi lại. Anh biết niềm tin không thể kéo bằng tay áo.

Thay vì cãi nhau trên mạng, Bảo đặt điện thoại quay toàn bộ quy trình của mình: kéo ngâm cồn, tông đơ thay lưỡi, khăn dùng một lần, cổ áo phủ giấy sạch, tóc quét vào túi rác buộc kín. Anh mời cô y tá ở phòng khám gần đó, khách quen mới cắt hôm trước, xem giúp cách vệ sinh có chỗ nào sai không. Cô nói thẳng vài điểm cần sửa: bình xịt không để sát mặt đất, khăn sạch phải có hộp đậy, lược đã dùng phải tách riêng. Bảo ghi hết, sửa ngay trong buổi chiều. Tối đó anh đăng clip không kèm chửi bới, chỉ viết: "Ai góp ý đúng, tôi sửa. Ai vu khống, tôi lưu bằng chứng."

Hiếu tưởng Bảo im là sợ, nên gửi thêm hai người tới quay cận mặt khách rồi hỏi xéo: "Cắt ngoài đường có bị ngứa không?" Một bác tài đang ngồi chờ đứng dậy chắn trước máy quay. Bác nói: "Tụi bay quay tao làm gì? Tóc tao, tiền tao, tao chọn chỗ tử tế." Đám đông xung quanh bắt đầu lên tiếng. Một cô lao công giơ túi khăn sạch Bảo vừa phát, nói: "Người ta cẩn thận hơn tiệm máy lạnh nhiều." Lần đầu tiên, Bảo không phải tự bảo vệ mình một mình. Anh chỉ lặng lẽ cắt nốt đường kéo cuối, nhưng trong lòng hiểu: khi một việc thật sự chạm vào người khác, nó sẽ có người đứng ra làm chứng.
""",
    5798: """
Mở tiệm không phải khoảnh khắc treo bảng rồi mọi thứ tự sáng lên. Bảo thuê được một mặt bằng nhỏ cạnh chợ cũ, tường ẩm, trần thấp, cửa kéo kêu ken két. Anh tự sơn lại tường vào ban đêm, lắp quạt cũ, mua ba chiếc ghế cắt tóc thanh lý và giữ chiếc ghế nhựa ở góc như một lời nhắc. Bảng hiệu chỉ ghi "Tóc Bảo - Cắt đẹp giá rõ". Không có chữ sang, không có ảnh người mẫu tóc bóng loáng, chỉ có bảng giá dán ngay cửa để khách khỏi ngại hỏi.

Ngày khai trương, Bảo không mời KOL, không bắn bóng bay. Anh mời những người từng ngồi trên vỉa hè: bác xe ôm, cô lao công, cậu sinh viên giao hàng, bà cụ bán xôi. Mỗi người được cắt miễn phí một lần, nhưng ai cũng cố bỏ tiền vào hộp. Bảo đành đặt thêm một chiếc hộp khác ghi "quỹ cắt tóc cho người khó". Đến chiều, một nhóm học sinh trường nghề tới xin học việc. Các em nói không muốn vào salon nơi thợ mới bị bắt gội đầu cả năm mới được cầm kéo. Bảo nhìn các em, nhớ ngày mình từng bị mắng vì cắt chậm, rồi nói: "Ở đây học từ quét tóc trước, nhưng quét tóc cũng phải hiểu vì sao khách rơi tóc xuống sàn mà vẫn muốn quay lại."

Áp lực bắt đầu khi khách đông hơn khả năng phục vụ. Có người phàn nàn chờ lâu, có người đòi Bảo phải cắt cho mình chứ không muốn thợ mới. Anh lập sổ hẹn, chia khung giờ, ghi tên thợ phụ trách và yêu cầu mọi người soi gương xác nhận trước khi rời ghế. Sai thì sửa ngay, không đổ lỗi cho tóc khách. Buổi tối, Bảo họp đội thợ trẻ, bắt từng người tự nói một lỗi trong ngày. Không khí căng nhưng sạch. Anh nói: "Tiệm này sinh ra từ một lần bị coi thường. Mình không được phép coi thường khách chỉ vì họ trả ít." Câu ấy trở thành quy định đầu tiên được dán trong phòng nghỉ.
""",
    5799: """
Hiếu đến vào một buổi chiều tiệm kín lịch. Anh ta không còn mặc vẻ chủ salon nắm quyền sinh sát, nhưng vẫn cố giữ giọng bề trên. Hiếu nhìn bảng giá, nhìn hàng ghế chờ, rồi cười: "Mày giỏi thật. Tao có mặt bằng, có thương hiệu, mình hợp tác đi. Tao đưa khách cao cấp, mày giữ nhóm bình dân. Hai bên đều có tiền." Bảo đặt kéo xuống, mời Hiếu ngồi ở chiếc ghế nhựa trong góc. Không phải để sỉ nhục, mà để Hiếu hiểu nơi mọi thứ bắt đầu.

Hiếu nói rất nhiều về chuỗi, về vốn, về quy trình. Nhưng càng nói, anh ta càng lộ một điều: trong đầu anh ta, khách vẫn chỉ là phân khúc để vắt lợi nhuận. Hiếu đề nghị nâng giá dần, giữ bảng 30K như mồi quảng cáo nhưng ép khách mua gói gội, hấp, dưỡng. Bảo nghe đến đó thì khép sổ. Anh hỏi: "Ngày xưa anh đuổi tôi vì tôi cắt cho một bác bảo vệ năm mươi nghìn. Hôm nay anh muốn dùng chính những người đó làm mồi. Anh thấy có gì khác không?" Hiếu đỏ mặt, nói thương trường phải linh hoạt.

Bảo không đáp ngay. Anh gọi cậu học việc mang ra hai ly nước, rồi đưa Hiếu xem bảng quỹ cắt tóc miễn phí treo công khai: thu bao nhiêu, chi bao nhiêu, còn bao nhiêu. Anh đưa thêm sổ phản hồi của khách, trong đó có cả lời khen lẫn lời chê. "Tôi không chống kiếm tiền," Bảo nói, "nhưng tôi chống việc dùng sự tử tế làm bảng hiệu, rồi phía sau lại móc túi người ta." Hiếu đứng dậy, nụ cười biến mất. Trước khi đi, anh ta buông một câu: "Mày sẽ không lớn nổi nếu cứ cứng vậy." Bảo nhìn hàng khách đang chờ ngoài cửa và đáp: "Nếu lớn lên mà phải giống anh, tôi chọn lớn chậm."
""",
    5800: """
Mẹ Bảo đến tiệm vào ngày mưa nhỏ. Bà mặc áo khoác cũ, tay cầm chiếc túi vải đã sờn, bên trong là bộ kéo cũ của bà. Bảo đang cắt cho khách, thấy mẹ đứng ngoài cửa thì tay khựng lại một nhịp. Mấy năm nay anh ít nhắc chuyện nhà vì sợ người ta thương hại. Mẹ từng cắt tóc trong phòng trọ, bị chủ nhà phàn nàn vì tóc rơi, bị khách quỵt tiền, rồi đau cổ tay phải nghỉ. Chiếc kéo của bà là thứ đã nuôi anh lớn, nhưng cũng là thứ khiến anh biết nghề này có thể làm người ta kiệt sức thế nào.

Khách nhận ra bà qua vài câu chuyện trong video cũ nên nhường ghế. Bảo muốn mẹ ngồi nghỉ, nhưng bà chỉ đặt túi kéo lên bàn và nói: "Mẹ không cắt được lâu nữa. Con giữ đi." Anh mở túi, thấy từng chiếc kéo được bọc giấy báo cẩn thận, lưỡi đã mòn nhưng vẫn sáng. Bà bảo ngày xưa bà không dám treo bảng giá, ai đưa bao nhiêu nhận bấy nhiêu, nhiều khi cười vậy thôi chứ tối về khóc vì không đủ tiền chợ. "Con khác mẹ," bà nói. "Con biết thương người nghèo, nhưng con cũng phải biết giữ giá trị của mình."

Tối đó, Bảo sửa lại bảng giá. Anh vẫn giữ mức thấp cho người khó, nhưng thêm dòng tư vấn rõ ràng: khách có điều kiện có thể trả theo gói đầy đủ, phần chênh lệch đưa vào quỹ. Anh không muốn tử tế biến thành tự bóc lột. Mẹ ngồi nhìn anh viết từng chữ, lâu lâu góp ý chỗ nào dễ gây hiểu nhầm. Khi tiệm đóng cửa, Bảo đặt chiếc kéo cũ của mẹ vào khung kính nhỏ gần quầy. Dưới khung, anh ghi: "Nghề này không thấp. Chỉ có người coi thường nghề mới làm nó thấp." Mẹ đọc xong quay mặt đi lau mắt, còn Bảo lần đầu thấy vết thương bị đuổi khỏi salon trong lòng mình khép lại một phần.
""",
    5801: """
Khi mở chi nhánh thứ hai, Bảo không chọn con phố đắt nhất mà chọn khu gần bến xe, nơi công nhân và sinh viên thuê trọ đông. Nhiều người bảo anh dại, vì thương hiệu đang lên thì phải vào trung tâm thương mại. Bảo chỉ hỏi lại: "Nếu người đã giúp mình nổi lên không còn vào được tiệm của mình, vậy mình nổi lên để làm gì?" Anh chuẩn hóa mọi thứ rất kỹ: mỗi chi nhánh có bảng giá công khai, hộp khăn riêng, sổ phản hồi, camera chỉ quay khu vực quầy để tránh xâm phạm khách, và một ngày mỗi tháng cắt miễn phí cho trẻ em ở mái ấm.

Không phải thợ nào cũng chịu được cách làm ấy. Có người muốn nhận thêm tiền riêng để ưu tiên khách quen, có người cắt qua loa với khách trả giá thấp. Bảo phát hiện một trường hợp sau khi đọc phản hồi của bà bán vé số: "Thợ trẻ cắt nhanh quá, cô không dám nói." Anh gọi cả đội họp, không mắng chửi, nhưng cho mọi người xem lại camera khu vực thanh toán và phiếu phản hồi. Người thợ trẻ cúi đầu xin lỗi. Bảo yêu cầu bạn ấy tự gọi cho khách mời quay lại sửa miễn phí, đồng thời nghỉ một ngày có lương để đi cùng anh cắt tóc thiện nguyện, học lại cảm giác đối diện một người không có nhiều lựa chọn.

Tin về chuỗi "cắt đẹp giá rõ" lan sang các quận khác. Một quỹ đầu tư nhỏ tìm đến, đề nghị rót vốn nếu Bảo đổi tên thành thương hiệu nghe thời thượng hơn và bỏ chiếc ghế nhựa khỏi hình ảnh nhận diện. Bảo từ chối phần bỏ ghế. Anh chấp nhận học quản trị, học tài chính, học cách mở rộng không vỡ chất lượng, nhưng không chấp nhận xóa dấu vết của ngày đầu. Trong buổi ký hợp đồng thuê mặt bằng chi nhánh thứ ba, anh mang theo chiếc ghế nhựa đặt ở góc phòng. Đối tác cười: "Anh mê cái ghế này thật." Bảo đáp: "Không. Tôi sợ một ngày mình quên cảm giác từng bị đuổi ra đường."
""",
    5802: """
Năm thứ ba, chiếc ghế nhựa đã bạc màu. Có người khuyên Bảo đem cất vào kho vì nó không hợp với hình ảnh chuỗi tiệm ngày càng chuyên nghiệp. Anh không nghe. Mỗi chi nhánh mới khai trương đều có một bản sao của chiếc ghế ấy đặt gần cửa, không phải để khách ngồi, mà để nhân viên mới nhìn thấy trước khi cầm kéo. Trong buổi đào tạo, Bảo kể lại ngày bị Hiếu đuổi, nhưng anh không kể bằng giọng oán hận nữa. Anh kể như một bài học về giới hạn: người ta có thể lấy mất chỗ làm của mình, nhưng không thể lấy mất lý do mình bắt đầu.

Một buổi tối muộn, Hiếu xuất hiện trước tiệm chính. Salon Đẹp Plus đã sang chủ, bảng hiệu cũ bị tháo xuống. Hiếu trông mệt hơn, tóc lấm tấm bạc. Anh ta không xin hợp tác, cũng không mỉa mai. Chỉ đứng nhìn chiếc ghế nhựa rồi nói: "Hồi đó tao nghĩ mày làm loạn thị trường." Bảo khóa cửa, im lặng chờ. Hiếu thở dài: "Giờ tao mới hiểu thị trường không chết vì có người cắt rẻ. Nó chết vì tụi tao coi khách nghèo như người không đáng được đẹp." Câu xin lỗi đến muộn, nhưng Bảo vẫn nhận. Anh không ôm lấy quá khứ để tự làm mình nặng thêm.

Sau đó, Bảo đi bộ qua con phố cũ nơi anh từng bị đuổi. Chỗ salon ngày xưa đã thành cửa hàng tiện lợi, cửa kính sáng trắng, không còn ai nhớ cuộc cãi vã hôm ấy. Nhưng Bảo nhớ. Anh nhớ cảm giác bị hất ra vỉa hè với chiếc túi kéo trên tay, nhớ nắng rát trên mặt, nhớ bác xe ôm đầu tiên ngồi xuống. Anh quay về tiệm, đặt tay lên lưng ghế nhựa và nhắn cho toàn bộ quản lý chi nhánh: "Tháng này kiểm tra lại bảng giá, quỹ hỗ trợ và phản hồi khách. Đừng để mình lớn lên rồi trở thành nơi từng đuổi mình đi." Tin nhắn được đọc rất nhanh. Ngoài phố, đèn tiệm tắt dần, nhưng chiếc ghế vẫn ở đó, nhỏ bé, bền bỉ, như một lời nhắc rằng phẩm giá đôi khi bắt đầu từ một chỗ ngồi rẻ tiền nhưng không ai bị coi rẻ.
""",
}


def main():
    editor.upload_helper()
    try:
        payload = editor.get_story_chapters(STORY_ID)
        chapters = payload["chapters"] if isinstance(payload, dict) else payload
        result = []
        for chapter in chapters:
            cid = int(chapter["id"])
            addition = ADDITIONS.get(cid)
            if not addition:
                continue
            content = (chapter["content"] or "").rstrip() + "\n\n" + addition.strip()
            editor.update_chapter(cid, chapter["title"], content)
            result.append({"chapter_id": cid, "title": chapter["title"], "added": True})
    finally:
        editor.remove_helper()
    out = ROOT / "scratch" / "story_5792_topoff_result.json"
    out.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
