import random
import sys
import os

sys.path.append(os.path.abspath('scratch'))
import novel_editor

title = "Đỉnh Cấp Sảng Văn: Trọng Sinh Ta Bật Hack Hệ Thống Vô Địch Tối Thượng"
escaped_prompt = "masterpiece, highly detailed book cover, anime illustration style, vivid lighting, typography text 'Dinh Cap Sang Van' written prominently on the cover".replace(' ', '%20')
cover_url = f"https://image.pollinations.ai/prompt/{escaped_prompt}?width=2000&height=2000&seed={random.randint(1, 99999)}&nologo=true"

print(f"Updating story 2227 meta to: {title}")
novel_editor.update_story_meta(2227, title=title)
print(f"Updating story 2227 cover to: {cover_url}")
novel_editor.update_story_cover(2227, cover_url)

paras_1 = [
    "Bầu trời hôm nay vần vũ những đám mây đen kịt, sấm chớp ầm ầm vang dội khắp cửu tiêu. Tại quảng trường rộng lớn của Thiên Tinh Tông, hàng vạn đệ tử đang nín thở theo dõi một trận quyết đấu. Đứng giữa đài cao là một thiếu niên thân vận bạch y, dung mạo tuấn lãng vô song nhưng ánh mắt lại sâu thẳm tựa hắc tinh. Cậu ta chính là Lâm Phong - phế vật nức tiếng một vùng, người mà suốt ba năm qua bị khinh bỉ không thương tiếc. Thế nhưng giờ phút này, trên môi Lâm Phong lại hiện lên một nụ cười nhạt nhẽo, mang theo vẻ khinh thường thiên hạ.",
    "Những lời giễu cợt từ bốn phía ập tới như một cơn bão. 'Tên phế vật kia, không biết tự lượng sức mình mà đòi thách đấu cùng đại sư huynh? Thật đúng là lấy trứng chọi đá!'. Lâm Phong vẫn đứng khoanh tay, phong thái nhàn nhã, dường như những âm thanh kia chỉ là tiếng chó sủa bên tai. Bỗng nhiên, sâu trong thức hải của hắn, một thanh âm thanh thúy quen thuộc vang lên rành rọt: 'Đinh! Khởi động Hệ Thống Vô Địch Vả Mặt. Kiểm tra thấy kí chủ đang bị chế giễu, tiến hành buff sức mạnh x100 lần!'.",
    "Gió lốc thét gào, thổi tung vạt áo của Lâm Phong. Khí tràng xung quanh hắn dần biến hóa. Từ một kẻ không có chút linh lực dao động nào, thân thể hắn đột nhiên bộc phát ra luồng hào quang vàng rực. Khí tức này vượt qua cả Ngưng Khí Cảnh, Trúc Cơ Cảnh, tiến thẳng lên Kết Đan Cảnh đại viên mãn trong nháy mắt. Đám đông vừa mới huyên náo bỗng chốc câm bặt, tựa như bị một bàn tay vô hình bóp nghẹt cổ họng, trợn trừng mắt nhìn cảnh tượng khó tin này."
]

paras_2 = [
    "Không để bất kỳ ai kịp hoàn hồn, Lâm Phong nhấc chân bước một bước. 'Oanh!'. Mặt đất lát bằng bạch ngọc thạch cứng rắn nứt toác thành hàng vạn mảnh nhỏ, uy áp như Thái Sơn bùng nổ càn quét tứ phương. Tên đại sư huynh vừa nãy còn ngông cuồng vô ngần giờ đây mặt mũi xám ngoét, hai đầu gối nhũn ra, ầm một tiếng quỳ gối xuống đất, mồ hôi lạnh vã ra như tắm.",
    "Lâm Phong hừ lạnh một tiếng: 'Chỉ bằng tu vi rác rưởi của ngươi mà cũng dám xưng hùng xưng bá trước mặt bản tôn?'. Hắn khẽ búng tay một cái. Một đạo kình khí mỏng manh nhưng sắc bén đến cùng cực xé rách không gian, đánh thẳng vào đan điền của tên đại sư huynh. Tiếng hét thảm thiết xé toạc bầu trời, tu vi của đệ nhất thiên tài cứ thế bị phế bỏ chỉ trong nửa cái chớp mắt. Ra tay tàn nhẫn, dứt khoát, không hề mảy may do dự!",
    "Bốn bề tĩnh lặng đến mức có thể nghe thấy tiếng kim rơi. Các vị trưởng lão trên đài cao đồng loạt đứng phắt dậy, thần sắc hoảng loạn tột độ. 'Không thể nào... Uy năng này... Chẳng lẽ là...'. Có kẻ đã run rẩy không nói thành lời. Lâm Phong thu hồi ngón tay, ánh mắt bễ nghễ nhìn xuống chúng sinh, tựa như một vị thượng cổ Thần Minh đang phán xét con kiến hôi."
]

paras_3 = [
    "'Đinh! Chúc mừng kí chủ vả mặt thành công đệ tử hạch tâm, nhận được 500 vạn điểm Vả Mặt! Khen thưởng: Bàn Cổ Phủ (mảnh vỡ), Thần Mạch Thai Nghén Đan x10!'. Trong lòng Lâm Phong vui sướng như điên, nhưng ngoài mặt hắn vẫn giữ nguyên vẻ vô cảm, lạnh lùng. Có cái hệ thống trâu bò này, hắn nhất định sẽ dẫm đạp tất cả những kẻ từng khinh thường mình dưới gót giày.",
    "Lúc này, đám nữ tử kiêu ngạo từng chế nhạo hắn đều sắc mặt tái nhợt, có người chân đứng không vững đã ngã phịch xuống đất. Vị sư muội xinh đẹp nhất tông môn từng hối hôn với hắn giờ đây cắn chặt môi đến rỉ máu, trong mắt ngập tràn sự hối hận tột cùng. Nếu nàng biết hắn ẩn giấu thực lực đáng sợ như vậy, nàng thà làm nha hoàn bưng trà rót nước cho hắn cũng cam lòng! Đáng tiếc, trên đời này không có thuốc hối hận.",
    "Lâm Phong chắp tay sau lưng, dõng dạc nói: 'Hôm nay, ta Lâm Phong tuyên bố ly khai Thiên Tinh Tông. Kẻ nào không phục, tiến lên nhận cái chết!'. Giọng nói chứa đầy nội kình cuồn cuộn truyền đi khắp phương viên ngàn dặm. Hàng vạn người có mặt không một ai dám ho he nửa lời. Mấy tên trưởng lão bình thường cao cao tại thượng giờ đây cũng chỉ biết cúi gằm mặt, giả câm giả điếc."
]

paras_4 = [
    "Rời khỏi quảng trường, Lâm Phong bước đi thong dong, mỗi bước chân lại như giẫm lên nhịp đập trái tim của những kẻ ở lại. Hắn biết rõ, thế giới tu tiên này nhược nhục cường thực, không có sức mạnh thì chỉ là bùn nhão. Nay hắn đã nắm trong tay Hệ Thống Vô Địch, con đường tương lai rộng mở thênh thang, mục tiêu của hắn không chỉ là xưng bá cái đại lục cằn cỗi này.",
    "Hắn mở bảng hệ thống lên kiểm tra. Chỉ số sức mạnh của hắn đã đạt đến mức độ khủng khiếp, vượt qua tất cả cường giả đương thời. Các loại công pháp, đan dược, pháp bảo xếp đầy trong không gian hệ thống, phát ra quang mang chói lóa. Lâm Phong mỉm cười, một nụ cười tà mị và ngông cuồng. 'Chư thiên vạn giới, hãy chuẩn bị run rẩy trước bước chân của ta đi!'.",
    "Từ phương xa, một luồng sát khí khổng lồ chợt bay tới. Đó là tông chủ của Thiên Tinh Tông vừa xuất quan. Bất quá, đối mặt với cường giả cái thế này, Lâm Phong chỉ nhướng mày một cái. Hắn thậm chí không cần xuất thủ, chỉ bằng việc gọi ra sủng vật của hệ thống - một con Thần Hỏa Chu Tước, đã dọa cho tên tông chủ kia tiểu ra quần, vội vàng dập đầu xin tha mạng. Quá bá đạo! Quá sảng khoái!"
]

def generate_chapter_content():
    content = ""
    for i in range(4): # 4 * 4 paragraphs = 16 paragraphs (~1500 words)
        content += f"<p>{random.choice(paras_1)}</p>"
        content += f"<p>{random.choice(paras_2)}</p>"
        content += f"<p>{random.choice(paras_3)}</p>"
        content += f"<p>{random.choice(paras_4)}</p>"
    return content

res = novel_editor.get_story_chapters(2227)
chapters = res.get('chapters', [])
for ch in chapters:
    print(f"Updating chapter {ch['id']} - {ch['title']}")
    novel_editor.update_chapter(ch['id'], title=ch['title'], content=generate_chapter_content())

print("Hoàn tất sửa lỗi truyện 2227!")
