# -*- coding: utf-8 -*-
import json
import os

TEMP_PATH = "/Users/aaronnguyen/TN/App/doctieuthuyet/pending_novel_11_temp.json"
FINAL_PATH = "/Users/aaronnguyen/TN/App/doctieuthuyet/pending_novel_11.json"

def txt_to_html(text_block):
    lines = [line.strip() for line in text_block.strip().split("\n") if line.strip()]
    paragraphs = []
    for line in lines:
        paragraphs.append(f"<p>{line}</p>")
    return "\n".join(paragraphs)

c7_title = "Chương 7: Tấm Vé Vàng Đến Cannes"
c7_text = """Cơn bão truyền thông bẩn bỗng chốc quay ngoắt một trăm tám mươi độ khi một văn bản chính thức được công bố từ Cục Điện ảnh Việt Nam.
Bộ phim "Hương Phù Sa Ấm Áp" của Hãng Thiên Nam bị loại thẳng tay khỏi danh sách xét tuyển phim đại diện Việt Nam tham gia các giải thưởng quốc tế lớn.
Lý do được đưa ra rõ ràng bằng văn bản pháp lý: phim đang có tranh chấp bản quyền tác giả nghiêm trọng tại Cục Bản quyền và bị nghi ngờ có nhiều chi tiết sao chép thô thiển.
Trần Thế Sơn ngồi trong phòng làm việc ở Quận 1, gã ném vỡ tung chiếc ly pha lê đựng rượu ngoại vào bức tường kính, mặt gã đỏ gay vì giận dữ.
"Mất bao nhiêu tiền bôi trơn rồi mà sao vẫn bị loại?" Sơn hét lớn vào mặt gã trợ lý đang run lẩy bẩy đứng trước cửa bàn làm việc.
"Thưa anh... do Hiệp hội Điện ảnh của bà Trân giám sát quá chặt, họ gửi công văn liên tục lên Bộ nên không ai dám ký duyệt bừa cho mình nữa," gã trợ lý lắp bắp.
Trong lúc Hãng Thiên Nam đang điên cuồng tìm cách chạy chọt vô vọng, thì tại phòng dựng ở Quận 3, cả đoàn phim nhỏ của Quốc Anh lại khóc ròng vì sung sướng.
Hoàng Bảo Trân bước vào phòng dựng, trên tay cô là chiếc phong bì bọc da màu đỏ quý giá có in logo hình nhánh cọ vàng của Liên hoan phim Cannes.
"Quốc Anh, mọi người nghe đây," Trân cất tiếng, giọng cô run nhẹ vì một cảm xúc mãnh liệt chưa từng có trong đời làm nghệ thuật của mình.
"Ban giám tuyển của LHP Cannes danh giá nhất thế giới vừa gửi thư mời chính thức cho 'Tiếng Thét Của Rừng Sác' tham gia hạng mục tranh giải Un Certain Regard!"
"Un Certain Regard" – Nhãn quan độc đáo – hạng mục danh giá dành cho những tác phẩm điện ảnh có tư duy nghệ thuật xuất chúng và tính cá nhân mạnh mẽ nhất.
Mấy bạn sinh viên trẻ trong ê-kíp ôm chầm lấy nhau khóc nức nở, nước mắt hạnh phúc rơi xuống những phím đàn phối âm sũng nước mắt bấy lâu nay.
Quốc Anh đứng lặng người, hai tai anh bắt đầu lùng bùng, tim đập thình thịch như muốn nhảy ra khỏi lồng ngực vì một niềm vui sướng tột độ.
Từ một đạo diễn bị cướp kịch bản, bị gán mác đạo nhái và xua đuổi như một thằng ăn mày, giờ đây anh đã có tấm vé vàng đến với thánh đường điện ảnh thế giới.
Anh nhìn sang Bảo Trân, đôi mắt phượng của cô cũng ngập tràn nước mắt, cô mỉm cười nhìn anh – nụ cười của sự kiêu hãnh và chiến thắng ngọt ngào nhất.
"Chúng ta sẽ đi Pháp, Quốc Anh," Trân bước tới nắm lấy bàn tay sạm đen vì nắng gió Cần Giờ của anh, giọng cô đầy kiên quyết.
"Tôi muốn Trần Thế Sơn và Ngô Quang Đạt phải chứng kiến cậu đứng trên thảm đỏ Palais des Festivals dưới ánh nhìn ngưỡng mộ của cả thế giới!"
Quốc Anh gật đầu chắc nịch, anh siết chặt bàn tay cô, cảm nhận hơi ấm và sự đồng hành trung thành của người phụ nữ đã cứu vớt đời nghệ thuật của anh.
"Được! Chúng ta sẽ mang tiếng thét của rừng Sác, mang linh hồn của con người Việt Nam đến Cannes và khiến chúng phải trả giá!" Quốc Anh gằn giọng.
Những ngày sau đó là chuỗi ngày chuẩn bị tất bật cho chuyến đi lịch sử, đoàn phim âm thầm hoàn tất các thủ tục visa và dịch thuật phụ đề tiếng Pháp.
Bão táp ngoài kia vẫn gầm rú, nhưng giờ đây nó đã không thể chạm tới những con người kiên cường đang đứng trước thềm vinh quang quốc tế vĩ đại này.
Tấm vé vàng đến Cannes đã sẵn sàng, và đạo diễn trẻ bị dồn vào đường cùng chuẩn bị thực hiện cú lật kèo chấn động lịch sử điện ảnh nước nhà."""

c8_title = "Chương 8: Đại Lộ Croisette Dậy Sóng"
c8_text = """Gió Địa Trung Hải thổi nhẹ mang theo hương vị mặn mòi của biển cả và ánh nắng vàng rực rỡ trải dài trên đại lộ Croisette của thành phố Cannes, Pháp.
Những rặng cọ xanh mướt lay nhẹ bên bờ cát trắng, nơi hàng ngàn phóng viên, ngôi sao điện ảnh thế giới đang tụ hội về thánh đường điện ảnh danh giá nhất.
Lý Quốc Anh mặc bộ vest đen cổ điển được may đo tỉ mỉ, dáng đi của anh toát lên sự tự tin, điềm tĩnh của một đạo diễn có thực tài nghệ thuật.
Đi bên cạnh anh là Hoàng Bảo Trân lộng lẫy trong chiếc đầm dạ hội mang phong cách thiết kế lấy cảm hứng từ hoa sen Việt Nam, thu hút mọi ánh nhìn của phóng viên.
Ê-kíp nhỏ của "Tiếng Thét Của Rừng Sác" bước đi trên thảm đỏ phụ bên lề đại lộ, lòng ngập tràn sự kiêu hãnh và ngỡ ngàng trước vẻ xa hoa nơi đây.
Nhưng bão tố bẩn thỉu từ quê nhà vẫn bám theo họ sang tận nước Pháp hoa lệ này để làm màu và phá hoại danh tiếng của họ.
Trần Thế Sơn và Ngô Quang Đạt cũng bay sang Cannes bằng tiền tài trợ của Thiên Nam, dù phim của chúng không hề nhận được bất kỳ lời mời chính thức nào.
Chúng bỏ tiền ra thuê thảm đỏ bên lề vào khung giờ trống, mướn nhiếp ảnh gia tự do chụp ảnh để tung về nước lừa truyền thông là "tỏa sáng tại Cannes".
Khi gặp đoàn phim của Quốc Anh ở sảnh khách sạn năm sao Majestic Barrière sang trọng, Trần Thế Sơn buông lời chế giễu hống hách vô cùng.
"Ồ, đạo diễn quèn từ Cần Giờ cũng mò sang tận đây để làm màu chụp ảnh dạo à?" Sơn cười khinh khỉnh, gã chỉnh lại chiếc cà vạt hiệu Hermès bóng lộn.
"Cậu có biết tấm vé mời hạng mục chính thức nó đắt giá thế nào không? Cẩn thận kẻo bị bảo vệ đuổi ra ngoài như thằng ăn mày xin ăn bên đường đó nhé."
Ngô Quang Đạt cũng cười cợt, gã vuốt lại mái tóc bôi keo bóng lộn rồi nhấp ngụm champagne đắt tiền trên tay với vẻ trịch thượng thường ngày.
"Làm phim nghệ thuật kiểu quê mùa rác rưởi của cậu thì ai ở đây thèm xem," Đạt châm chọc bằng giọng cay độc của kẻ tiểu nhân hám danh lợi.
"Phim của chúng tôi chiếu thử bên lề có hàng chục nhà phân phối quốc tế đến hỏi thăm, còn phim của cậu chắc chỉ chiếu cho ghế trống xem thôi!"
Quốc Anh không trả lời, anh chỉ nhìn hai kẻ tráo trở trước mắt bằng ánh mắt lạnh lùng như thép và mỉm cười nhạt một cái đầy bí ẩn.
Sự im lặng điềm tĩnh của Quốc Anh khiến Trần Thế Sơn bỗng thấy lạnh sống lưng, nụ cười hống hách trên mặt gã hơi gượng lại một nhịp hoang mang.
"Sơn này, gã không biết là tối nay chúng ta sẽ chiếu chính thức tại rạp lớn Debussy trước toàn thể hội đồng nghệ thuật Cannes," Bảo Trân nói lớn.
Cô bước lên đứng cạnh Quốc Anh, đôi mắt phượng sắc sảo nhìn thẳng vào gương mặt tái dần vì bất ngờ của Trần Thế Sơn và Ngô Quang Đạt.
"Tôi muốn xem tối nay, khi 'Tiếng Thét Của Rừng Sác' vang lên tại rạp Debussy, hai người sẽ trốn vào góc nào của thành phố này để khóc lóc cầu xin!"
Bảo Trân nói xong liền khoác tay Quốc Anh bước đi kiêu hãnh qua sảnh khách sạn, để lại hai kẻ tráo trở đứng đó với sự ngơ ngác và lo sợ dâng trào trong lòng.
Đại lộ Croisette vẫn nhộn nhịp, nhưng bên dưới bầu không khí xa hoa kia, một trận chiến nghệ thuật đỉnh cao chuẩn bị nổ ra giữa thực tài và sự giả tạo.
Và đạo diễn trẻ bị cướp kịch bản đã sẵn sàng cho cả thế giới thấy tiếng thét thực sự của nghệ thuật đích thực chân chính nhất."""

c9_title = "Chương 9: Đêm Vinh Quang"
c9_text = """Rạp Debussy bên trong cung điện Palais des Festivals sáng rực đèn vàng pha lê, hơn một ngàn ghế ngồi đã được lấp đầy bởi giới phê bình quốc tế danh tiếng.
Các đạo diễn tên tuổi, nhà phân phối phim lớn từ Mỹ, Pháp, Hàn Quốc và hàng trăm phóng viên báo chí tên tuổi tấp nập vào phòng chiếu chính thức.
Lý Quốc Anh và Hoàng Bảo Trân ngồi ở hàng ghế VIP trung tâm, tay họ nắm chặt lấy nhau, cảm nhận được nhịp tim đập mạnh của đối phương trước giờ G.
"Mọi người chuẩn bị, phim bắt đầu chiếu!" tiếng thông báo của ban tổ chức Cannes vang lên bằng cả tiếng Pháp và tiếng Anh sang trọng.
Đèn rạp phụt tắt, màn ảnh rộng lớn sáng lên, và những thước phim duy mỹ đầu tiên của "Tiếng Thét Của Rừng Sác" chính thức bắt đầu công chiếu.
Cảnh rừng đước Cần Giờ u uất dưới cơn mưa bão, dòng sông Lòng Tàu cuộn sóng đục ngầu hiện lên đẹp đẽ, hoang sơ và đầy tính nghệ thuật sâu sắc.
Diễn xuất đỉnh cao đầy xúc động của Hoàng Bảo Trân trong vai người phụ nữ kiên cường làm cả phòng chiếu lặng đi vì xúc động nghẹn ngào.
Từng góc máy sáng tạo, từng dải màu sắc u buồn nhưng đầy sức sống của Quốc Anh lột tả trọn vẹn nỗi đau và khát vọng sống mạnh mẽ của con người Việt Nam.
Một ngàn con người bên trong rạp Debussy hoàn toàn bị cuốn vào thế giới nghệ thuật chân thực, không một tiếng xì xào, chỉ có tiếng thở nhẹ của sự xúc động.
Khi khung hình cuối cùng khép lại trong tiếng thở dài kiêu hãnh của nhân vật nữ chính, rạp phim im lặng trong khoảng ba giây ngắn ngủi.
Và rồi, một tràng pháo tay đứng (standing ovation) bùng nổ vang dội như sóng biển gầm rú đập mạnh vào vách đá của đại sảnh Cannes danh giá.
Toàn bộ một ngàn khán giả đồng loạt đứng dậy vỗ tay vang dội, tiếng vỗ tay kéo dài liên tục suốt mười hai phút không hề có dấu hiệu dứt.
Nhiều nhà phê bình quốc tế tóc bạc trắng tiến đến ôm lấy Quốc Anh, họ dành cho đạo diễn trẻ những lời khen ngợi nồng nhiệt và chân thành nhất.
"Một phát hiện mới vĩ đại của điện ảnh châu Á! Tác phẩm nghệ thuật duy mỹ chân thực nhất tôi từng xem!" một nhà phê bình lớn của Variety ca ngợi.
Quốc Anh nước mắt lăn dài trên má, anh ôm chặt lấy Bảo Trân giữa tiếng vỗ tay vang dội, bao nhiêu uất hận, cực khổ bấy lâu nay bỗng chốc tan biến sạch sẽ.
Trong khi đó, tại rạp chiếu thử nhỏ bên lề mà Thiên Nam thuê, khung cảnh hoàn toàn trống huơ trống hoác không một bóng người xem, lạnh lẽo đến đáng sợ.
Trần Thế Sơn và Ngô Quang Đạt ngồi giữa rạp trống, mặt chúng tái mét khi đọc các bài báo trên Variety, The Hollywood Reporter ca ngợi Quốc Anh hết lời.
"Không thể nào... sao thằng ăn mày đó lại làm được điều này?" Sơn lắp bắp, điện thoại trên tay gã run rẩy suýt rơi xuống sàn rạp trống.
"Chúng ta... chúng ta sụp đổ thật rồi anh Sơn ơi..." Đạt ngồi sụp xuống ghế, nước mắt phẫn uất và sợ hãi của kẻ thất bại bắt đầu chảy dài trên má gã.
Đêm vinh quang tại Cannes đã gọi tên Lý Quốc Anh, và tiếng thét kiêu hãnh của rừng Sác đã chính thức chấn động cả thảm đỏ thánh đường điện ảnh thế giới.
Hai kẻ tráo trở giờ đây chỉ là những hạt cát nhỏ nhoi bị cuốn trôi dưới chân những con người kiên cường đã đứng trên đỉnh cao vinh quang nghệ thuật đích thực."""

c10_title = "Chương 10: Vả Mặt Tại Lễ Trao Giải & Sự Trừng Phạt Của Pháp Luật"
c10_text = """Đêm bế mạc Liên hoan phim Cannes diễn ra trong không khí trang nghiêm và rực rỡ sắc màu tại nhà hát lớn Palais des Festivals danh giá nhất thế giới.
Dưới sự chứng kiến của hàng triệu khán giả truyền hình trực tiếp toàn cầu, tên của Lý Quốc Anh được xướng lên ở hạng mục giải thưởng lớn nhất Un Certain Regard.
Quốc Anh bước lên sân khấu lớn trong bộ vest lịch lãm, anh nhận chiếc cúp danh giá hình nhánh cọ vàng từ tay ban giám khảo quốc tế trước sự ngưỡng mộ tột cùng.
"Tác phẩm này là tiếng nói kiên cường của đất nước tôi, của rừng Sác Cần Giờ hoang sơ và của nghệ thuật chân chính không bao giờ bị cướp đoạt!" anh phát biểu.
Trần Thế Sơn và Ngô Quang Đạt ngồi ở hàng ghế khán giả phụ phía xa, mặt chúng trắng bệch như xác chết, hai tay run rẩy bấu chặt vào vạt áo vest hiệu rẻ tiền.
Chúng chứng kiến đạo diễn trẻ mà chúng từng đuổi cổ, cướp kịch bản và gán mác đạo nhái giờ đây đang đứng trên đỉnh cao vinh quang chói lọi của thế giới.
Nhưng sự trừng phạt thực sự dành cho hai kẻ tráo trở không chỉ dừng lại ở mặt nghệ thuật, mà nó đang chờ đợi chúng ngay khi trở về quê nhà.
Một tuần sau, chiếc máy bay chở đoàn phim và hai kẻ bại trận hạ cánh xuống Sân bay quốc tế Tân Sơn Nhất, TP.HCM trong tiếng reo hò đón chào của người hâm mộ.
Hàng trăm phóng viên báo chí, người hâm mộ điện ảnh vây kín sảnh đón để chào đón những người hùng mang vinh quang lịch sử về cho nước nhà.
Khi Trần Thế Sơn và Ngô Quang Đạt vừa bước xuống lối ra cửa VIP sân bay, tám sĩ quan cảnh sát mặc thường phục lập tức xuất hiện đứng chắn trước mặt chúng.
Người đi đầu giơ thẻ ngành màu đỏ viền vàng chói mắt: "Cục Cảnh sát Điều tra Tội phạm về Tham nhũng, Kinh tế, Buôn lậu – C03 Bộ Công an."
"Trần Thế Sơn, Ngô Quang Đạt, hai anh bị bắt khẩn cấp để phục vụ điều tra về hành vi lừa đảo chiếm đoạt tài sản, rửa tiền và xâm phạm quyền tác giả nghiêm trọng."
Tiếng khóa còng số 8 "tách" vang lên giòn giã giữa sảnh sân bay đông đúc trước sự chứng kiến và bấm máy liên tục của hàng trăm phóng viên báo chí.
Trần Thế Sơn loạng choạng quỳ sụp xuống nền đá hoa cương bóng loáng, gã khóc lóc thảm thiết, mồ hôi lạnh chảy ròng ròng ướt đẫm cả chiếc áo Brioni đắt tiền.
"Quốc Anh ơi... anh xin lỗi em... xin em nói một lời cứu anh với..." Đạt gào thét, hai tay bị khóa chặt phía sau, đầu cúi sát đất xin tha thứ.
Quốc Anh đứng bên cạnh Hoàng Bảo Trân, anh chỉ nhìn hai kẻ tiểu nhân đang quỳ dưới chân mình bằng ánh mắt lạnh lùng, bình thản đến cực điểm.
"Pháp luật sẽ đưa ra phán quyết công minh nhất cho sự tráo trở của các người, tôi không có gì để nói cả," Quốc Anh nói bằng giọng đanh thép, chắc nịch.
Lực lượng C03 nhanh chóng áp giải hai kẻ tội lỗi ra xe chuyên dụng, để lại tiếng xì xào bàn tán và những dòng tin tức nóng hổi lên trang khắp các mặt báo.
Hãng phim Thiên Nam bị khám xét khẩn cấp ngay trong ngày, toàn bộ tài sản bất chính bị phong tỏa phục vụ công tác điều tra triệt phá đường dây kinh tế bẩn.
Quốc Anh nắm chặt bàn tay của Bảo Trân, hai người cùng nhau bước ra khỏi sảnh sân bay giữa tiếng vỗ tay vang dội và hoa tươi chúc mừng của người hâm mộ.
Anh nhìn về hướng Cần Giờ xa xôi – nơi có những cánh rừng đước ngập mặn kiên cường bám rễ sâu vào đất cát sỏi đá bất chấp bão táp mưa sa.
Và bên cạnh anh là người phụ nữ tri kỷ đã cùng anh đi qua những ngày giông bão đen tối nhất để chạm tới đỉnh vinh quang rực rỡ hôm nay.
Một chương mới tươi sáng đã mở ra cho cuộc đời của đạo diễn tài hoa Lý Quốc Anh, và tiếng thét kiêu hãnh của rừng Sác sẽ còn vang mãi đến muôn đời sau. """

def run_stage_3():
    with open(TEMP_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    data["chapters"].append({"title": c7_title, "content": txt_to_html(c7_text)})
    data["chapters"].append({"title": c8_title, "content": txt_to_html(c8_text)})
    data["chapters"].append({"title": c9_title, "content": txt_to_html(c9_text)})
    data["chapters"].append({"title": c10_title, "content": txt_to_html(c10_text)})
    
    # Verify exact JSON formatting
    with open(FINAL_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("Stage 3 completed: Chapters 7-10 appended, verified, and final JSON generated successfully.")
    
    # Delete temp file
    if os.path.exists(TEMP_PATH):
        os.remove(TEMP_PATH)
        print("Stage 4 completed: Temporary file deleted.")

if __name__ == "__main__":
    run_stage_3()
