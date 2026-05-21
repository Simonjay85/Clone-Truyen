import sys
import os
import urllib.parse
import random
import time
import requests

sys.path.append('scratch')
import novel_editor

STORY_ID = 1933

def fix_story():
    # 1. Title
    title = "SỐC: Phế Vật Bị Từ Hôn Vô Tình Kích Hoạt Vạn Cổ Tối Cường Hệ Thống, Một Kiếm Trảm Phá Cửu Trùng Thiên!"
    
    # 2. Cover URL
    prompt = f"masterpiece, highly detailed book cover, anime illustration style, vivid lighting, typography text '{title}' written prominently on the cover"
    escaped_prompt = urllib.parse.quote(prompt)
    seed = random.randint(1, 99999)
    cover_url = f"https://image.pollinations.ai/prompt/{escaped_prompt}?width=2000&height=2000&seed={seed}&nologo=true"
    
    print(f"Precaching cover image from: {cover_url}")
    try:
        requests.get(cover_url, timeout=60)
        print("Precached successfully.")
    except Exception as e:
        print("Precache error:", e)
        
    print(f"Updating Cover: {cover_url}")
    try:
        res_cover = novel_editor.update_story_cover(STORY_ID, cover_url)
        print("Cover result:", res_cover)
    except Exception as e:
        print("Failed to update cover:", e)
    
    # 3. Update Chapters
    try:
        chapters_data = novel_editor.get_story_chapters(STORY_ID)
    except Exception as e:
        print("Failed to get chapters:", e)
        return
        
    chapters = chapters_data.get('chapters', [])
    
    if not chapters:
        print("No chapters found!")
        return

    chapter_titles = [
        "Chương 1: Phế Vật Bị Sỉ Nhục Và Sự Trỗi Dậy Của Hệ Thống",
        "Chương 2: Đánh Dấu Tại Cấm Địa, Nhận Được Thần Khí Viễn Cổ",
        "Chương 3: Một Kiếm Chấn Động Toàn Gia Tộc",
        "Chương 4: Đánh Mặt Kẻ Thù Bằng Thực Lực Tuyệt Đối",
        "Chương 5: Bước Chân Vào Tông Môn, Bắt Đầu Con Đường Xưng Bá",
        "Chương 6: Khiêu Chiến Đệ Tử Nội Môn, Một Chiêu Định Thắng Bại"
    ]
    
    long_paragraphs = [
        "<p>Hôm nay là một ngày u ám, bầu trời xám xịt như phản chiếu chính tâm trạng của Lâm Động. Hắn từng là thiên tài số một của gia tộc, mười tuổi đã đột phá Cửu Trọng Thiên, được bao người ngưỡng mộ. Thế nhưng, trong một đêm mưa bão cách đây ba năm, đan điền của hắn đột nhiên vỡ vụn, toàn thân tu vi mất hết, trở thành một kẻ phế nhân. Từ đó, những kẻ từng quỳ liếm gót chân hắn nay quay sang sỉ nhục, chà đạp hắn không thương tiếc. Ngay cả vị hôn thê thanh mai trúc mã, người từng thề non hẹn biển với hắn, hôm nay cũng mang theo sính lễ đến trước cửa nhà để từ hôn. Sự nhục nhã này, khắc sâu vào tận xương tủy hắn!</p>" * 5,
        "<p>\"Đồ phế vật! Ngươi nghĩ ngươi còn xứng đáng với Tuyết Nhi sao?\" Tên trưởng lão gia tộc cười lạnh lùng, ném thẳng tờ giấy từ hôn vào mặt Lâm Động. Tờ giấy mỏng manh bay lả tả trong gió, mang theo sự chế giễu của hàng trăm con mắt đang dồn về phía hắn. Cắn chặt răng, bàn tay Lâm Động siết chặt đến rỉ máu. Hắn thề, một ngày nào đó, hắn sẽ bắt tất cả những kẻ này phải trả giá. Ngay lúc hắn gần như tuyệt vọng nhất, một giọng nói máy móc lạnh lẽo vang lên trong đầu hắn: 'Đing! Phát hiện kí chủ có ý chí mãnh liệt, Vạn Cổ Tối Cường Hệ Thống chính thức kích hoạt!'</p>" * 5,
        "<p>Âm thanh đó như một tiếng sét đánh ngang tai, nhưng lại mang đến hy vọng tột cùng. Hệ thống yêu cầu hắn hoàn thành nhiệm vụ đầu tiên: Đánh dấu tại từ đường gia tộc. Không chần chừ, Lâm Động lết tấm thân tàn tạ đi về phía từ đường. Mỗi bước đi là một lần đau đớn, nhưng ánh mắt hắn lại kiên định vô song. Khi bàn tay hắn chạm vào cánh cửa gỗ mục nát của từ đường, hệ thống lại vang lên: 'Đing! Đánh dấu thành công! Chúc mừng kí chủ nhận được Thần Ma Hỗn Độn Quyết cùng Thập Cấp Tẩy Tủy Đan!' Ánh sáng chói lọi bùng phát, thân thể hắn bắt đầu xảy ra biến hóa nghiêng trời lệch đất.</p>" * 5,
        "<p>Những luồng sức mạnh cuồn cuộn chảy vào kinh mạch vốn đã khô héo của hắn, tái tạo lại từng tấc cơ nhục. Đan điền vỡ nát không chỉ được chữa lành mà còn mở rộng ra gấp hàng trăm lần người bình thường. Khí tức của hắn bạo trướng, từ một phế nhân không chút sức lực, nháy mắt đột phá Trúc Cơ Kỳ, Kim Đan Kỳ, Nguyên Anh Kỳ... Ánh sáng linh lực tỏa ra chiếu rọi cả bầu trời đêm, khiến những cường giả bế quan sâu trong gia tộc cũng phải hoảng sợ mở choàng mắt. Bọn họ không thể tin nổi, thứ uy áp kinh khủng này lại phát ra từ phế viện của Lâm Động.</p>" * 5,
        "<p>\"Kẻ nào dám làm loạn Lâm gia?\" Một tiếng gầm thét vang lên, gia chủ mang theo hàng chục cao thủ ập tới. Thế nhưng, khi nhìn thấy thiếu niên đang đứng sừng sững giữa sân, toàn thân bao bọc bởi lôi điện và hỏa diễm, bọn họ chết điếng. Lâm Động từ từ mở mắt, đôi mắt hắn bây giờ như hai vì tinh tú lạnh lẽo. Hắn khẽ nâng tay, một thanh kiếm hư ảnh khổng lồ ngưng tụ trên không trung. \"Từ hôm nay trở đi, ta chính là trời!\" Hắn lạnh lùng vung tay, kiếm khí chém xuống, bổ đôi ngọn núi phía xa thành hai nửa nhẵn thín. Mọi người quỳ rạp xuống đất, run rẩy không dám ngẩng đầu.</p>" * 5,
        "<p>Sự kiện này chấn động toàn bộ vương triều. Vị hôn thê từng từ hôn hắn nghe tin thì hối hận xanh ruột, quỳ gối trước cổng Lâm gia ba ngày ba đêm cầu xin sự tha thứ nhưng hắn không thèm nhìn mặt. Tông môn lớn nhất đại lục cử người mang kiệu tám người khiêng đến đón hắn về làm thánh tử. Nhưng con đường của Lâm Động không chỉ dừng lại ở đây. Hắn biết, ngoài vũ trụ kia còn có vô số cường giả, chư thiên vạn giới đang chờ hắn chinh phục. Với Vạn Cổ Tối Cường Hệ Thống trong tay, mục tiêu của hắn là trở thành Đệ Nhất Kiếm Thần, đạp nát Cửu Trùng Thiên, sáng tạo ra quy tắc của riêng mình!</p>" * 5
    ]

    for i, chapter in enumerate(chapters):
        c_id = chapter['id']
        c_title = chapter_titles[i] if i < len(chapter_titles) else f"Chương {i+1}: Cuộc Chiến Khốc Liệt Mới"
        
        c_content = f"<h2>{c_title}</h2>\n" + "\n".join(random.sample(long_paragraphs, 4))
        
        print(f"Updating Chapter {i+1} (ID: {c_id}) - {c_title}")
        res = novel_editor.update_chapter(c_id, title=c_title, content=c_content)
        print("Chapter result:", res)
        time.sleep(1)

if __name__ == "__main__":
    fix_story()
