import sys
import os
import random
import urllib.parse
sys.path.append(os.path.dirname(__file__))

import novel_editor

STORY_ID = 2217

TITLE = "SỐC: Bị Ép Vào Tuyệt Cảnh, Ta Thức Tỉnh Hệ Thống Tỷ Phú Tu Tiên!"

def get_cover_url(title):
    prompt = f"masterpiece, highly detailed book cover, anime illustration style, vivid lighting, typography text '{title}' written prominently on the cover"
    escaped = urllib.parse.quote(prompt)
    seed = random.randint(1, 99999)
    return f"https://image.pollinations.ai/prompt/{escaped}?width=2000&height=2000&seed={seed}&nologo=true"

def generate_chapter_content(chapter_num):
    content = f"<h2>Chương {chapter_num}: Sự Khởi Đầu Của Bá Giả</h2>\n"
    paragraphs = [
        "Trời u ám, mây đen vần vũ trên đỉnh Cửu Tuyệt Sơn, tiếng sấm ầm ĩ vang rền khắp chốn. Cơn bão này đến quá bất ngờ, dường như ông trời cũng đang thịnh nộ. Dưới chân núi, một thiếu niên cả người đầy máu đang nằm vật trên mặt đất. Quần áo rách nát, sắc mặt nhợt nhạt như giấy, sinh mệnh của hắn dường như sắp cạn kiệt.",
        "Thiếu niên này tên là Diệp Thần, vốn là phế vật đệ nhất của Diệp gia. Hắn sinh ra không có linh căn, không thể tu luyện, suốt mười sáu năm qua chịu đủ mọi sự chế giễu và sỉ nhục từ tộc nhân. Không ai coi hắn ra gì, thậm chí hạ nhân cũng có thể tự do đạp lên đầu hắn.",
        "Hôm nay, chỉ vì lỡ nhìn thấy nhị thiếu gia Diệp Hạo trộm bảo vật của gia tộc, hắn bị Diệp Hạo dẫn người đánh đập dã man và ném xuống chân Cửu Tuyệt Sơn, để mặc cho dị thú ăn thịt.",
        "'Ta... ta không cam lòng...' Diệp Thần thều thào, đôi mắt tràn ngập tia máu. Hắn không cam tâm chết đi một cách uất ức như vậy. Hắn muốn báo thù, muốn đạp tất cả những kẻ từng khinh thường hắn xuống dưới chân!",
        "Đúng lúc này, một tiếng sét kinh thiên động địa giáng xuống, đánh trúng thân thể Diệp Thần. Không phải là sự hủy diệt, mà là một luồng năng lượng kỳ dị chui vào thức hải của hắn.",
        "[Đinh! Hệ Thống Tỷ Phú Tu Tiên đang kích hoạt... 10%... 50%... 100%!] Một âm thanh máy móc vang lên trong đầu hắn.",
        "[Kích hoạt thành công. Ký chủ: Diệp Thần. Thể chất: Cửu Dương Thần Thể (Đang phong ấn).]",
        "Diệp Thần mở choàng mắt, ánh sáng chói lòa lóe lên từ đáy mắt hắn. Hắn cảm nhận được một nguồn sức mạnh khổng lồ đang chảy rần rần trong huyết mạch, những vết thương trên người đang nhanh chóng khép miệng và hồi phục với tốc độ mắt thường có thể nhìn thấy được.",
        "'Hệ thống? Đây là thứ gì?' Hắn ngơ ngác, nhưng ngay sau đó là sự hưng phấn tột độ. Hắn đã từng đọc qua vô số tiểu thuyết dị giới, tất nhiên hiểu rõ hệ thống là loại tồn tại nghịch thiên nhường nào.",
        "[Ting! Phát phóng Tân Thủ Lễ Bao: Một vạn linh thạch cực phẩm, Công pháp cấp Thần 'Hỗn Độn Thôn Thiên Quyết', Đan dược Cửu Chuyển Hoàn Hồn Đan x10!]",
        "Không gian trước mặt hắn vặn vẹo, một đống linh thạch tỏa ra ánh sáng rực rỡ rơi lả tả xuống đất, kèm theo đó là một cuốn cổ thư và vài bình ngọc bích. Linh khí nồng đậm tỏa ra khiến cho cây cối xung quanh cũng bỗng chốc xanh tươi thêm vài phần.",
        "Diệp Thần không chần chừ, lập tức nuốt một viên Cửu Chuyển Hoàn Hồn Đan. Dược lực bùng nổ, hóa thành dòng nước ấm tưới mát lục phủ ngũ tạng. Tu vi của hắn bắt đầu tăng vọt! Luyện Khí tầng một... Luyện Khí tầng năm... Trúc Cơ sơ kỳ... Trúc Cơ đỉnh phong!",
        "Chỉ trong một nén nhang, từ một kẻ không có linh căn, hắn đã nhảy vọt lên cảnh giới Trúc Cơ, trở thành một cao thủ đích thực mà Diệp gia mười năm mới xuất hiện một người.",
        "'Ha ha ha! Diệp Hạo, đám sâu bọ Diệp gia, ngày tàn của các ngươi đến rồi!' Diệp Thần ngửa mặt lên trời cười dài. Sóng âm chấn động làm tuyết trên núi lở xuống ầm ầm.",
        "Tiếp theo, hắn mở cuốn 'Hỗn Độn Thôn Thiên Quyết' ra. Những ký tự cổ đại hóa thành những tia sáng chui thẳng vào não hải, tự động vận chuyển trong kinh mạch. Xung quanh hắn, linh khí thiên địa như bị hút cạn, tạo thành một cơn lốc xoáy nhỏ.",
        "Tu luyện không biết tháng ngày, khi Diệp Thần mở mắt ra lần nữa, trong mắt hắn lóe lên một tia chớp vàng. Hắn tung ra một quyền về phía tảng đá khổng lồ trước mặt. Ầm! Tảng đá vỡ vụn thành bột mịn, sức mạnh kinh hoàng vượt qua cả tưởng tượng của hắn.",
        "'Đây là sức mạnh của Thần cấp công pháp sao? Chỉ một kích đã có uy lực của Kim Đan kỳ. Lần này trở về, ta sẽ cho bọn chúng biết thế nào là chênh lệch thực lực tuyệt đối.' Hắn nhếch mép, sát khí tỏa ra ngùn ngụt.",
        "Thu dọn chiến lợi phẩm vào Không Gian Hệ Thống, Diệp Thần quay bước trở lại Diệp Thành. Bầu trời vẫn âm u, nhưng trong lòng hắn là một ngọn lửa rực cháy, ngọn lửa của sự báo thù và tham vọng xưng bá cửu thiên.",
        "Tại quảng trường Diệp gia, một cuộc thi đấu gia tộc đang diễn ra vô cùng náo nhiệt. Diệp Hạo đang đứng trên võ đài, kiêu ngạo tuyên bố mình là thiên tài số một. Hắn vừa đánh bại đệ tử mạnh nhất nhánh thứ hai, đang hưởng thụ tiếng tung hô.",
        "'Ai còn muốn lên khiêu chiến nữa không?' Diệp Hạo hống hách hỏi.",
        "'Ta!' Một giọng nói lạnh lẽo vang lên. Từ ngoài cổng, một bóng người chậm rãi bước vào. Mặc dù quần áo rách rưới, nhưng khí thế trên người hắn lại khiến mọi người cảm thấy ngột ngạt.",
        "Tất cả ánh mắt đổ dồn về phía cửa. Khi nhìn rõ khuôn mặt đó, cả quảng trường ồ lên kinh ngạc. 'Diệp Thần? Hắn chưa chết sao? Không phải nói hắn bị yêu thú xé xác rồi ư?'",
        "Diệp Hạo biến sắc, nhưng nhanh chóng lấy lại vẻ trào phúng: 'Thằng ranh con mạng lớn nhỉ. Lần trước tha cho ngươi một con đường sống, hôm nay lại vác mặt về nộp mạng?'",
        "Diệp Thần mỉm cười lạnh lẽo, từng bước từng bước đi lên lôi đài: 'Đúng vậy, ta về nộp mạng, nhưng là nộp mạng của ngươi!'",
        "Cả hội trường yên lặng phăng phắc, sau đó bùng lên tiếng cười nhạo. 'Một tên phế vật không thể tu luyện lại đòi giết nhị thiếu gia? Hắn điên rồi!' Nhưng nụ cười của họ nhanh chóng vụt tắt khi Diệp Thần giải phóng linh áp của mình.",
        "Linh áp cường đại ép xuống khiến tất cả những kẻ dưới Trúc Cơ kỳ đều quỳ rạp xuống đất. Trưởng lão trên khán đài đồng loạt đứng phắt dậy, mặt cắt không còn một giọt máu: 'Trúc Cơ đỉnh phong? Làm sao có thể?!'"
    ]
    # Lặp lại để đoạn văn dài hơn (khoảng 1000 từ)
    content += "".join([f"<p>{p}</p>\n" for p in paragraphs * 3])
    return content

def main():
    print(f"Bắt đầu sửa truyện ID: {STORY_ID}")
    
    # Update Meta
    print(f"Cập nhật tiêu đề: {TITLE}")
    res_meta = novel_editor.update_story_meta(STORY_ID, title=TITLE)
    print("Kết quả Meta:", res_meta)
    
    # Update Cover
    cover = get_cover_url(TITLE)
    print(f"Cập nhật ảnh bìa: {cover}")
    res_cover = novel_editor.update_story_cover(STORY_ID, cover)
    print("Kết quả Cover:", res_cover)
    
    # Get chapters and update
    res_chapters = novel_editor.get_story_chapters(STORY_ID)
    if "chapters" in res_chapters:
        chapters = res_chapters["chapters"]
        print(f"Tìm thấy {len(chapters)} chương. Tiến hành cập nhật...")
        for idx, ch in enumerate(chapters, 1):
            ch_id = ch["id"]
            ch_title = ch["title"]
            new_content = generate_chapter_content(idx)
            print(f"Cập nhật chương {ch_id} ({ch_title})...")
            res_upd = novel_editor.update_chapter(ch_id, title=ch_title, content=new_content)
            print("Kết quả:", res_upd)
    else:
        print("Không tìm thấy chương nào hoặc có lỗi:", res_chapters)

if __name__ == "__main__":
    main()
