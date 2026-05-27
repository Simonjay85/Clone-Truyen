import json
import os
import requests
import time

LOCAL_URL = "http://127.0.0.1:8000/v1/chat/completions"

SYSTEM_PROMPT = """Bạn là nhà văn viết truyện sảng văn/vả mặt (web novel) hàng đầu Việt Nam, đạt Chuẩn vàng V13.
Nhiệm vụ của bạn là viết một chương truyện cực kỳ sống động, chân thực, kịch tính và đầy cảm xúc cho tác phẩm: 'Họ Gọi Tôi Là Lang Băm, Hội Thảo Quỳ Xin Tôi Cứu Mạng'.

QUY TẮC PHẢI TUÂN THỦ:
1. ĐỘ DÀI: Chương phải dài từ 1000 - 1500 từ tiếng Việt (khoảng 5000 - 8000 ký tự). Viết cực kỳ chi tiết, diễn giải sâu sắc tâm lý và mô tả bối cảnh chứ không được viết tóm tắt sơ sài!
2. ĐỊNH DẠNG: Mỗi câu văn hoặc đoạn hội thoại ngắn phải được đặt trong một cặp thẻ `<p>...</p>` riêng biệt. Không gộp nhiều câu dài vào một thẻ. Chỉ dùng `<p>`, `<strong>`, `<em>`.
3. SHOW, DON'T TELL: Thay vì viết 'vô cùng sợ hãi', hãy mô tả vật lý: 'mồ hôi lạnh rỉ ra dọc hai bên thái dương', 'làn da xám ngoét không còn một giọt máu', 'gót giày cao gót khẽ gõ xuống sàn đá hoa cương sắc lạnh', 'ngón tay bấu chặt rỉ cả máu'.
4. KHÔNG LẶP TỪ CLICHÉ: Tuyệt đối không dùng các từ sảng văn lặp đi lặp lại như: 'lạnh lùng', 'tột cùng', 'sòng phẳng', 'lý tính', 'giao động' (viết sai chính tả, phải viết là 'dao động'). Hãy dùng từ vựng tinh tế phong phú của tiếng Việt văn học!
5. LORE & TÊN RIÊNG: Nam chính là Nguyễn Lâm Phong, nữ chính là Trịnh Khánh Vy (Tập đoàn Y tế Vạn An). Không có bất kỳ thế lực nào tên 'Trần Gia' (lỗi template cũ). Hãy sử dụng tên 'Phế Đan Vạn An' hoặc 'Lâm Phong' hoặc 'Nguyễn Gia' nếu cần.
6. THOẠI & PHẢN ỨNG: Không giải thích chuyên môn y học quá dài dòng khô khan. Hãy biến các giải thích khoa học thành các đoạn đối thoại đối đáp kịch tính, kèm theo phản ứng ngỡ ngàng hoặc lo lắng của các bác sĩ xung quanh.
7. ĐỊA DANH VÀ THƯƠNG HIỆU THẬT: Sử dụng địa danh thật tại Hà Nội (hồ Tây, bán đảo hồ Tây, Nguyễn Chí Thanh, Trung tâm Hội nghị Quốc gia) và ngân hàng thật (Vietcombank).
"""

CHAPTERS_PROMPTS = {
    1: "Hãy viết Chương 1: Trục Xuất Khỏi Viện Phổi Quốc Tế. Nội dung: Nguyễn Lâm Phong bị Lê Hữu Hoài (Viện trưởng Viện Phổi Việt - Đức) sa thải nhục nhã ngay trong phòng họp giao ban tầng năm trong đêm mưa giông sấm sét tầm tã của Hà Nội. Phan Mỹ Hạnh (vị hôn thê bội bạc, Phó giám đốc tài chính) bước vào cùng Trần Quốc Dũng (Giám đốc NexaCorp). Hạnh ném chiếc nhẫn đính hôn bằng bạc vào mặt Phong khinh bỉ anh nghèo hèn, rồi đuổi Phong ra đường dưới mưa giông. Phong lẩm bẩm lời thề bắt chúng quỳ gối xin lỗi. Hãy viết vô cùng chi tiết, nén chặt cảm xúc đau đớn và phẫn nộ. Giảm đoạn giải thích cơ chế Nexa-09 quá dài, chuyển thành đối thoại giữa Phong và các bác sĩ xung quanh.",
    2: "Hãy viết Chương 2: Y Đức Của Thần Y Phố Cổ. Nội dung: Phong đứng trú mưa dưới hiên một tiệm trà cũ ở phố cổ Hà Nội. Anh bắt gặp một em bé nghèo bán vé số đang bị co thắt phế quản cấp tính, thở rít dữ dội bên đường. Bất chấp sự nghi ngờ của người dân xung quanh gọi anh là kẻ lừa đảo lang băm, Phong điềm tĩnh dùng ba mũi châm cứu vàng ròng giữ mạng và cho em bé uống một viên thuốc thảo dược nhỏ của mình. Cơn suy hô hấp của em bé lập tức dịu đi kỳ diệu. Trịnh Khánh Vy (nữ Chủ tịch điều hành sắc sảo của Tập đoàn Vạn An) tình cờ đi ngang qua trên chiếc xe Maybach, cô chứng kiến toàn bộ sự việc. Vy bảo thư ký điều tra lý lịch của Phong nhưng cô vẫn cực kỳ nghi ngờ Đông y là trò lừa đảo cảm tính.",
    3: "Hãy viết Chương 3: Lời Mời Của Nữ Chủ Tịch. Nội dung: Cha của Khánh Vy (siêu tỷ phú Trịnh Vạn An) bị biến chứng suy hô hấp cấp do đợt dùng thử Nexa-09 trước đó, phổi bị đông đặc gỗ. Các giáo sư Tây y đầu ngành đều bó tay, khuyên gia đình chuẩn bị hậu sự. Vy mặc dù vô cùng nghi ngờ y học cổ truyền và cho rằng đây chỉ là trò lừa đảo cảm tính, nhưng trong hoàn cảnh bế tắc không còn gì để mất, cô đành ra lệnh cho Maybach đi đón Phong về biệt thự hồ Tây. Vy đứng chặn Phong trước cửa phòng bệnh, ra điều kiện nghiêm khắc bằng hành động: Nếu cứu sống được cha cô, cô sẽ đầu tư vô hạn cho anh; ngược lại, thế lực của Vạn An sẽ khiến anh không còn đường sống. Phong điềm nhiên chấp nhận.",
    4: "Hãy viết Chương 4: Cửu Châm Đoạt Mệnh Định Sinh Tử. Nội dung: Phong bước vào phòng bệnh của cụ Trịnh Vạn An đang tím tái nguy kịch. Anh sử dụng chín mũi kim châm cứu vàng ròng 'Cửu Châm Đoạt Mệnh' chuẩn xác tuyệt đối đâm sâu vào các huyệt vị (Đại Chùy, Đàn Trung, Phế Du, Định Suyễn, v.v.). Vị giáo sư Tây y phản đối dữ dội vì cho rằng châm kim bẩn thỉu sẽ gây nhiễm trùng huyết. Phong quát khẽ át vía vị giáo sư, tay đi châm nhanh như chớp. Cụ Trịnh Vạn An khôi phục nhịp thở, chỉ số SpO2 tăng lên 92% an toàn, cứu cụ qua cơn nguy kịch. Tuy nhiên, Phong tuyên bố đây chỉ là 'giữ mạng tạm thời', phế nang vẫn bị tổn thương sâu sắc, cần kiểm chứng lâm sàng nghiêm ngặt và theo dõi liệu trình 7 ngày mới có thể phục hồi thực sự. Khánh Vy bắt đầu bị thuyết phục nhưng cô vẫn lập tức ra lệnh kiểm tra lâm sàng toàn diện bằng Tây y hiện đại.",
    5: "Hãy viết Chương 5: Kiểm Chứng Lâm Sàng Và Hợp Đồng 500 Tỷ. Nội dung: Sáng hôm sau, kết quả chụp HRCT (cắt lớp vi tính lồng ngực độ phân giải cao) và xét nghiệm khí máu động mạch của cụ Trịnh Vạn An chứng minh kỳ tích: các dải xơ hóa tổ chức kẽ đông đặc co hẹp lại hơn 70%. Vy hoàn toàn chấn động trước kết quả số liệu Tây y dứt khoát. Nhận thấy tiềm năng khổng lồ của 'Phế Đan Sâm Đá' để đè bẹp âm mưu thâu tóm của tập đoàn đa quốc gia NexaCorp, Khánh Vy lập tức tổ chức ký kết hợp đồng liên doanh Vạn An - Lâm Phong trị giá 500 tỷ đồng tiền mặt để xây dựng vùng trồng và nhà máy công nghệ cao. Hợp đồng quy định Phong nắm 51% cổ phần kiểm soát chuyên môn y tế. Lê Hữu Hoài và Trần Quốc Dũng nhận được tin rò rỉ bắt đầu lo sợ tột bực.",
    6: "Hãy viết Chương 6: Đòn Bẩn Và Livestream Bôi Nhọ. Nội dung: Trần Quốc Dũng khẩy môi âm mưu tàn nhẫn để bóp chết liên doanh của Phong từ trong trứng nước. Hắn mua chuộc KOL y tế Hoàng Đăng thực hiện buổi livestream trực tiếp kéo dài hai tiếng vạch trần Phong là 'lang băm lừa đảo gây chết người, trộn chất độc corticoid liều cao vào thuốc Phế Đan Sâm Đá'. Phản diện trưng ra hàng loạt bệnh án giả, hồ sơ nạn nhân giả mạo tinh vi. Dư luận bùng nổ phẫn nộ kịch liệt, cổ phiếu Vạn An sụt giảm mạnh. Đối tác cung ứng sâm đá ở Hà Giang hoang mang đòi hủy hợp đồng.",
    7: "Hãy viết Chương 7: Cơn Bão Phong Tỏa Hai Mươi Tư Giờ. Nội dung: Trần Quốc Dũng sử dụng mối quan hệ tín dụng đen ngầm phong tỏa tài khoản ngân hàng của Phong tại Vietcombank trong 24 giờ. Sở Y tế bất ngờ ập vào đình chỉ công trường nhà máy Hòa Lạc của liên doanh. Khánh Vy chịu áp lực khổng lồ từ hội đồng quản trị Vạn An và các cổ đông lớn đòi sa thải Phong và hủy bỏ dự án 500 tỷ. Giữa cơn bão dữ dội, Phong vẫn điềm nhiên rót trà sen thảo luận. Anh khuyên Vy hãy kiên nhẫn: Sự kiêu ngạo luôn khiến kẻ thù để lộ tử huyệt chí mạng.",
    8: "Hãy viết Chương 8: Truy Vết Blockchain Và Nhật Ký Commit. Nội dung: Phong cùng Vy thức trắng đêm tác chiến bảo mật. Bạn thân của Phong là Hùng (hacker mã nguồn mở) ròng rã 10 tiếng giải mã toàn bộ nhật ký commit Git (Git commit history) gốc của Viện Phổi mà Phong đã sao lưu trên ổ cứng di động mã hóa. Bằng chứng đanh thép với mã băm SHA-256 chứng minh chính tài khoản của Lê Hữu Hoài đã lén lút ăn cắp công thức Phế Đan của Phong, đồng thời cắt xén hoạt chất sâm đá để trục lợi làm sản xuất rẻ đi 10 lần, gây ra biến chứng lâm sàng xơ phổi kẽ cho người bệnh nghèo. Luật sư trưởng Minh Đức lập tức soạn thảo đơn khởi kiện hình sự gửi cơ quan C03 Bộ Công an.",
    9: "Hãy viết Chương 9: Nhịp Đập Trí Tuệ Dưới Trăng Hồ Tây. Nội dung: Đêm muộn trước ngày hội thảo hô hấp quốc gia, sương thu mờ ảo trên hồ Tây tĩnh mịch. Tại văn phòng làm việc tầng 20 của Vy, hai người uống trà sen. Vy cởi bỏ lớp vỏ bọc băng giá, chia sẻ nỗi đau mất mẹ 10 năm trước vì căn bệnh suy hô hấp cấp khiến cô phải giấu kín cảm xúc đằng sau những con số vô cảm. Nhìn thấy y đức thuần khiết của Phong cứu cha cô bất chấp hiểm nguy, Vy thực sự rung động sâu sắc. Phong nắm lấy bàn tay lạnh giá của cô, sưởi ấm cô và thề sẽ bảo vệ danh dự kiêu hãnh của cô trước mọi sóng gió. Tuyến tình cảm được đẩy sâu lắng và thuyết phục.",
    10: "Hãy viết Chương 10: Biến Cố Phế Huyết Tại Hội Thảo Quốc Gia. Nội dung: Hội thảo y dược quốc gia diễn ra cực kỳ tráng lệ tại Trung tâm Hội nghị Quốc gia. Lê Hữu Hoài diễn thuyết tự mãn công bố Nexa-09 định giá IPO 1 tỷ USD. Để chứng minh, Dũng cho mời 5 bệnh nhân nghèo dùng thử Nexa-09 lên sân khấu livestream. Ngay trên sóng trực tiếp, 5 bệnh nhân đột ngột ho sặc sụa kịch liệt, trào ra những dòng máu đen đặc tanh tưởi, ngã quỵ co giật trong tình trạng ngạt thở cấp tính. Các giáo sư hô hấp quốc tế hoảng hốt tột bực. Các biện pháp can thiệp Tây y hiện đại của Hoài đều vô hiệu vì phổi bị đông đặc xẹp phế nang hoàn toàn. Hoài bủn rủn chân tay quỳ sụp xuống sàn.",
    11: "Hãy viết Chương 11: Sự Lựa Chọn Của Thần Y. Nội dung: Giữa hội trường hỗn loạn la hét kinh hoàng, cửa sảnh mở toang, Phong hiên ngang sải bước vào trong áo blouse trắng tinh khôi cùng Khánh Vy. Đứng trước 5 bệnh nhân đang nguy kịch sắp chết và lũ phản diện đang bủn rủn, Phong phải đứng trước sự lựa chọn đạo đức: cứu bệnh nhân trước hay công bố bằng chứng hạ gục đối thủ trước? Y đức tối thượng của Phong chiến thắng, anh quỳ xuống bên các vũng máu cứu người trước. Phong dùng chín mũi châm vàng Cửu Châm Đoạt Mệnh và dịch chiết sâm đá nhỏ trực tiếp cứu sống cả 5 bệnh nhân chỉ trong 3 phút ngắn ngủi trước sự ngỡ ngàng kinh hoàng của toàn hội trường.",
    12: "Hãy viết Chương 12: Phán Quyết Cuối Cùng. Nội dung: Sau khi cứu người, Khánh Vy dõng dạc công bố toàn bộ bằng chứng đanh thép: nhật ký commit Git chứng minh Hoài ăn cắp và cắt xén hoạt chất làm đông đặc phổi người bệnh nghèo, báo cáo kiểm toán EY vạch trần dòng tiền hối lộ 2 triệu USD từ NexaCorp vào tài khoản Thụy Sĩ của Hoài và Phan Mỹ Hạnh. Cơ quan C03 Bộ Công an ập vào đọc lệnh bắt giữ khẩn cấp Lê Hữu Hoài và Trần Quốc Dũng. Phan Mỹ Hạnh quỳ sụp bò lết khóc lóc cầu xin Phong tha thứ, cào bấu ngón tay rỉ máu dưới chân anh đầy hối hận muộn màng. Phong lãnh đạm dắt tay Khánh Vy bước đi kiêu hãnh giữa tràng pháo tay vang dội như sấm truyền. Hai người thành lập Viện nghiên cứu Đông Tây y kết hợp Phong An rực rỡ."
}

def generate_chapter(ch_num):
    prompt = CHAPTERS_PROMPTS[ch_num]
    print(f"✍️ Generating Chapter {ch_num}/12...")
    payload = {
        "model": "default",
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.35,
        "max_tokens": 4000
    }
    
    for attempt in range(3):
        try:
            res = requests.post(LOCAL_URL, json=payload, timeout=240)
            if res.status_code == 200:
                data = res.json()
                content = data["choices"][0]["message"]["content"].strip()
                # strip out markdown block symbols if returned
                if content.startswith("```html"):
                    content = content[7:]
                if content.startswith("```"):
                    content = content[3:]
                if content.endswith("```"):
                    content = content[:-3]
                content = content.strip()
                
                # word count check (Vietnamese word count is approximately space separated splits)
                word_count = len(content.split())
                char_count = len(content)
                print(f"✓ Chapter {ch_num} generated! Words: {word_count}, Characters: {char_count}")
                if word_count < 400:
                    print("⚠️ Word count too short! Retrying with higher max_tokens...")
                    continue
                return content
            else:
                print(f"⚠️ API Error (status={res.status_code}): {res.text}. Retrying...")
        except Exception as e:
            print(f"⚠️ Exception on attempt {attempt+1}: {e}")
        time.sleep(2)
        
    raise Exception(f"Failed to generate Chapter {ch_num} after 3 attempts.")

def main():
    print("🚀 SEQUENTIAL GENERATION OF 12 CHAPTERS - V13 GOLD STANDARD")
    chapters = []
    
    # Check existing temp progress
    progress_file = "scratch/story_3940_12ch_progress.json"
    if os.path.exists(progress_file):
        try:
            with open(progress_file, "r", encoding="utf-8") as f:
                chapters = json.load(f)
            print(f"✓ Resuming from progress file: {len(chapters)} chapters loaded.")
        except Exception as e:
            print(f"⚠️ Failed to load progress file: {e}")

    titles = {
        1: "Chương 1: Trục Xuất Khỏi Viện Phổi Quốc Tế",
        2: "Chương 2: Y Đức Của Thần Y Phố Cổ",
        3: "Chương 3: Lời Mời Của Nữ Chủ Tịch",
        4: "Chương 4: Cửu Châm Đoạt Mệnh Định Sinh Tử",
        5: "Chương 5: Kiểm Chứng Lâm Sàng Và Hợp Đồng 500 Tỷ",
        6: "Chương 6: Đòn Bẩn Và Livestream Bôi Nhọ",
        7: "Chương 7: Cơn Bão Phong Tỏa Hai Mươi Tư Giờ",
        8: "Chương 8: Truy Vết Blockchain Và Nhật Ký Commit",
        9: "Chương 9: Nhịp Đập Trí Tuệ Dưới Trăng Hồ Tây",
        10: "Chương 10: Biến Cố Phế Huyết Tại Hội Thảo Quốc Gia",
        11: "Chương 11: Sự Lựa Chọn Của Thần Y",
        12: "Chương 12: Phán Quyết Cuối Cùng"
    }

    start_num = len(chapters) + 1
    for ch_num in range(start_num, 13):
        content = generate_chapter(ch_num)
        chapters.append({
            "title": titles[ch_num],
            "content": content
        })
        # Save progress at each step
        with open(progress_file, "w", encoding="utf-8") as f:
            json.dump(chapters, f, indent=4, ensure_ascii=False)
            
    # Polished Intro from review guidelines
    intro_html = """<p><strong>"Cút khỏi Viện Phổi Quốc tế ngay lập tức! Loại bác sĩ Đông y quèn chỉ biết bốc lá cây và châm cứu rác rưởi như mày không xứng đáng đứng chung hàng ngũ với chúng tao!"</strong></p>
<p>Lời mắng chửi tàn nhẫn của Lê Hữu Hoài - Viện trưởng Viện Phổi Quốc tế Việt - Đức - như một nhát búa đập tan năm năm cống hiến thầm lặng của Nguyễn Lâm Phong. Cứu hàng ngàn bệnh nhân và âm thầm nghiên cứu công thức giải độc phế nang đột phá, nhưng thứ Phong nhận lại chỉ là sự phản bội tàn nhẫn từ người thầy kính trọng và vị hôn thê Phan Mỹ Hạnh, kẻ sẵn sàng từ bỏ hôn ước để chạy theo Trần Quốc Dũng, Giám đốc điều hành của tập đoàn hóa chất dược phẩm đa quốc gia NexaCorp.</p>
<p>Bị vu oan ăn cắp vật tư y tế và bị tống cổ khỏi bệnh viện dưới cơn mưa giông tầm tã của Hà Nội, Phong ngỡ như mất tất cả. Thế nhưng, cơ duyên đưa anh gặp Trịnh Khánh Vy, nữ Chủ tịch điều hành vô cùng nhạy bén và sắc sảo của Tập đoàn Y tế Vạn An. Bằng sự kết hợp kỳ diệu giữa bí thuật châm cứu "Cửu Châm Đoạt Mệnh" và các xét nghiệm lâm sàng Tây y hiện đại, Phong cứu sống siêu tỷ phú Trịnh Vạn An khỏi ranh giới sinh tử, chứng minh hiệu quả thần kỳ của phương thuốc cổ truyền. Cùng nhau, họ vượt qua đòn bẩn phong tỏa 24 giờ, dùng bản gốc nhật ký commit Git, bằng sáng chế quốc tế độc quyền, báo cáo kiểm toán Big 4 của EY và lệnh bắt giữ khẩn cấp từ cơ quan C03 Bộ Công an để đè bẹp tập đoàn phản bội, bắt những kẻ kiêu ngạo phải tự quỳ gối đền tội dưới chân mình.</p>"""

    # Format final deployment payload
    final_payload = {
        "story_id": 3940,
        "title": "Họ Gọi Tôi Là Lang Băm, Đến Khi Cả Hội Thảo Quỳ Xin Tôi Cứu Mạng",
        "intro": intro_html,
        "chapters": chapters,
        "seo": {
            "focus_keyword": "Họ Gọi Tôi Là Lang Băm",
            "seo_title": "Họ Gọi Tôi Là Lang Băm, Hội Thảo Quỳ Xin Tôi Cứu Mạng",
            "seo_description": "Nguyễn Lâm Phong dùng Cửu Châm Đoạt Mệnh và Sâm Đá hồi sinh kẽ phổi, vạch trần âm mưu ăn cắp công trình của Viện trưởng Lê Hữu Hoài."
        }
    }
    
    with open("scratch/story_3940_deploy_ready.json", "w", encoding="utf-8") as f:
        json.dump(final_payload, f, indent=4, ensure_ascii=False)
    print("🎉 SUCCESS! Final compiled 12-chapter payload saved to scratch/story_3940_deploy_ready.json")
    
    # Cleanup temp progress
    if os.path.exists(progress_file):
        os.remove(progress_file)

if __name__ == "__main__":
    main()
