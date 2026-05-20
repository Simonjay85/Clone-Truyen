# -*- coding: utf-8 -*-
import os
import json
import time
import requests
import re

OPENAI_KEY = "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"

OUTLINES = [
    {
        "chap_num": 1,
        "title_hint": "Chương 1: Kẻ Ăn Cắp Công Trình",
        "outline": "Lâm Trần bị Trưởng khoa Hoàng Vĩnh cướp công trình nghiên cứu tế bào gan Nam dược tại phòng khám đa khoa An Tâm ở Quận 5. Hoàng Vĩnh đuổi Lâm Trần đi, khóa tài khoản Techcombank của anh, ném hành lý của anh ra đường Nguyễn Trãi dưới cơn mưa tầm tã Sài Gòn. Lâm Trần quỳ dưới mưa lập lời thề phục hận sâu sắc."
    },
    {
        "chap_num": 2,
        "title_hint": "Chương 2: Mỹ Nhân Thử Thách",
        "outline": "Lâm Trần ngồi dưới mưa Quận 5 thì xe Porsche Panamera của Trịnh Minh Thư (ái nữ Trịnh Gia) đỗ trước mặt. Minh Thư có biết về tài năng của anh nhưng chưa tin tưởng hoàn toàn. Đột nhiên, gã tài xế/vệ sĩ riêng của cô quỵ xuống đau đớn, mặt xám xịt do ngộ độc/chất độc cấp tính cực kỳ nguy kịch. Lâm Trần không hoảng hốt, dùng châm bạc gia truyền châm cứu chính xác các đại huyệt để GIỮ MẠNG, TẠM ỔN ĐỊNH sự sống cho tài xế chứ không làm anh ta tỉnh dậy ngay trong 5 phút. Lâm Trần yêu cầu gọi cấp cứu đưa tài xế đến bệnh viện lớn Quận 5 khẩn cấp. Tại phòng cấp cứu, các bác sĩ Tây y tiến hành xét nghiệm máu và lâm sàng, bàng hoàng xác nhận chính nhờ những mũi châm cứu ổn định huyết mạch thần sầu lúc trước của Lâm Trần mà tài xế mới giữ được mạng sống trước khi độc tố phá hủy nội tạng hoàn toàn. Điều này khiến Minh Thư hoàn toàn bị chấn động và nể phục, tin tưởng anh tuyệt đối."
    },
    {
        "chap_num": 3,
        "title_hint": "Chương 3: Nhân Y Đường Khai Trương",
        "outline": "Minh Thư là ái nữ tài phiệt sắc sảo, cô không vội rót ngay 5 tỷ VNĐ. Thay vào đó, cô đặt ra một điều kiện thử thách cực kỳ khắc nghiệt: Lâm Trần phải cứu chữa một ca bệnh nan y vô cùng phức tạp đang nằm tại biệt thự Trịnh Gia của một đối tác kinh tế quan trọng bị chứng tê liệt chi dưới/bệnh gan hiếm gặp mà các bác sĩ hàng đầu đều bó tay. Lâm Trần đồng ý, trực tiếp dùng chẩn đoán bắt mạch chuẩn xác và thực hiện kỹ thuật châm cứu vi diệu cùng đơn thuốc thảo dược phục hồi thần kinh/gan độc đáo để phục hồi cảm giác chân của bệnh nhân trong sự kinh ngạc của tất cả mọi người. Sau khi vượt qua thử thách hoàn hảo, Minh Thư nể phục tuyệt đối và chính thức ký hợp đồng rót vốn lớn, chuyển ngay 5 tỷ VNĐ vào tài khoản Vietcombank mới mở cho Lâm Trần để mở phòng khám 'Nhân Y Đường' tại Quận 5, đối diện trực tiếp phòng khám An Tâm của Hoàng Vĩnh."
    },
    {
        "chap_num": 4,
        "title_hint": "Chương 4: Y Thuật Trực Chiến",
        "outline": "Nhân Y Đường thu hút bệnh nhân nghèo nhờ chính sách từ thiện và y đức của Lâm Trần. Ông Sáu, một người chạy xe ôm ở Quận 5 bị xơ gan cổ trướng giai đoạn cuối từng bị An Tâm đuổi đi, tìm đến đây thoi thóp. Lâm Trần cứu ông Sáu bằng một phác đồ bài bản dài hạn (gồm châm cứu 3 đợt, bốc thảo dược Nam dược giải độc và tái tạo gan như nhân trần, diệp hạ châu, hội chẩn, phục hồi trong 2 tuần). Bụng ông Sáu xẹp dần, sức khỏe hồi phục rõ rệt qua từng ngày, tạo danh tiếng vang dội cho Nhân Y Đường."
    },
    {
        "chap_num": 5,
        "title_hint": "Chương 5: Truyền Thông Giông Bão",
        "outline": "Hoàng Vĩnh thuê báo chí bẩn tung tin đồn Nhân Y Đường dùng thảo dược chứa thạch tín gây ngộ độc. Khủng hoảng không giải quyết trong tích tắc mà kéo dài và cực kỳ nghiêm trọng: Nhân Y Đường bị thanh tra y tế chính thức đình chỉ hoạt động trong 24 giờ để điều tra, hàng loạt bệnh nhân hoảng loạn gọi điện hủy lịch khám, các nhà cung cấp dược liệu đầu mối ở Quận 5 lập tức đơn phương cắt đứt nguồn hàng để tránh liên lụy, hàng chục phóng viên bẩn và YouTuber túc trực livestream gào thét gây áp lực trước cửa phòng khám. Giữa tâm bão dư luận gay gắt suốt đêm, Lâm Trần vẫn bình tĩnh cùng Minh Thư chuẩn bị kế sách. Hôm sau, họ tổ chức họp báo, đưa ra bằng chứng sở hữu trí tuệ bản quyền công thức từ một năm trước cùng kết quả kiểm định chính thức sạch độc tố từ Viện kiểm nghiệm dược phẩm quốc gia, đồng thời công bố chứng cứ Hoàng Vĩnh chuyển tiền hối lộ cho kẻ vu khống, lập tức đảo chiều truyền thông một cách ngoạn mục và đập tan âm mưu phản diện."
    },
    {
        "chap_num": 6,
        "title_hint": "Chương 6: Độc Chất TX-9",
        "outline": "Hoàng Vĩnh bị dồn vào chân tường, âm mưu cùng thế lực ngầm mua độc chất sinh học TX-9 tàn phá gan cực nhanh để đầu độc Trịnh Văn Hùng (Chủ tịch Trịnh Gia, bố Minh Thư) khi ông đến Nhân Y Đường khám bệnh. Gã mua chuộc hộ lý Tuấn của phòng khám nhỏ độc chất vào nước uống của ông Hùng. Ông Hùng uống xong ho ra máu đen ngòm và ngã quỵ. Hoàng Vĩnh đã chuẩn bị sẵn, lập tức dẫn cảnh sát Quận 5 ập vào niêm phong phòng khám, vu oan Lâm Trần cố ý giết người."
    },
    {
        "chap_num": 7,
        "title_hint": "Chương 7: Kim Bạc Đoạt Mạng Sống",
        "outline": "Khi ông Hùng trúng độc TX-9 cực mạnh và ngã quỵ, da xám xanh, hơi thở yếu ớt, Lâm Trần cực kỳ bình tĩnh dùng 15 cây kim bạc châm liên hoàn phong tỏa huyết mạch ngăn độc công tâm, đồng thời pha khẩn cấp liều thuốc Nam dược đặc hiệu để giải độc tố ban đầu. Sau khi châm cứu, ông Hùng tuy phun ra dịch đen nhưng chưa tỉnh ngay lập tức mà được đưa đi cấp cứu hồi sức cấp tốc tại bệnh viện trung ương Quận 5. Tại đây, trưởng khoa Tây y đầu ngành trực tiếp chỉ đạo xét nghiệm men gan, sinh hóa máu, bàng hoàng xác nhận: độc tố TX-9 đã được trung hòa hoàn toàn một cách kỳ tích nhờ acupuncture của Lâm Trần, gan đang phục hồi ngoạn mục. Trưởng khoa Tây y kinh ngạc chứng kiến và xác nhận: 'Bệnh nhân đã qua cơn nguy kịch nhờ y thuật châm cứu thần sầu ban đầu, nhưng cần theo dõi thêm'. Minh Thư lúc này cũng công bố video camera ẩn vạch trần Hoàng Vĩnh mua chuộc hộ lý Tuấn."
    },
    {
        "chap_num": 8,
        "title_hint": "Chương 8: Cổ Đông Hôn Ước",
        "outline": "Hoàng Vĩnh bị C03 khởi tố bắt giam. Trước buổi họp báo lớn của Trịnh Gia, Lâm Trần và Minh Thư có một cuộc trò chuyện riêng tư sâu lắng, đầy cảm xúc trong vườn hoa yên tĩnh phía sau phòng khám Nhân Y Đường Quận 5 dưới ánh hoàng hôn ấm áp. Minh Thư chủ động bộc bạch tâm tình chân thật, độc lập của mình: cô chọn yêu và ở bên anh hoàn toàn là từ sự tự nguyện, ngưỡng mộ đức độ và tài năng của anh, chứ không phải vì di nguyện của gia đình hay quyền lợi kinh doanh nào cả. Lâm Trần nắm tay cô, cả hai có khoảnh khắc rung động chân thành gắn kết sâu đậm. Khi họp báo diễn ra, Chủ tịch Trịnh Văn Hùng tuyên bố chuyển giao 20% cổ phần tập đoàn cho Lâm Trần và công bố đính ước. Minh Thư tự tin đứng bên anh, quay sang gọi một tiếng 'Chồng yêu' ngọt ngào trước sự chúc phúc của báo giới, tạo nên kết cục mỹ mãn, trọn vẹn tình cảm."
    }
]

def robust_json_parse(raw_str):
    cleaned = raw_str.strip()
    if cleaned.startswith("```"):
        cleaned = re.sub(r"^```(?:json)?\n", "", cleaned)
        cleaned = re.sub(r"\n```$", "", cleaned).strip()
    try:
        return json.loads(cleaned)
    except Exception as parse_err:
        start_idx = cleaned.find("{")
        end_idx = cleaned.rfind("}")
        if start_idx != -1 and end_idx != -1 and end_idx > start_idx:
            json_candidate = cleaned[start_idx:end_idx+1]
            return json.loads(json_candidate)
        raise parse_err

def call_openai(system_prompt, user_prompt, max_tokens=4000, temperature=0.7):
    url = "https://api.openai.com/v1/chat/completions"
    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        "temperature": temperature,
        "max_tokens": max_tokens
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_KEY}"
    }
    
    for attempt in range(4):
        try:
            res = requests.post(url, json=payload, headers=headers, timeout=120)
            res.raise_for_status()
            data = res.json()
            return data['choices'][0]['message']['content'].strip()
        except Exception as e:
            print(f"  [Attempt {attempt+1}] OpenAI Call Error: {e}")
            time.sleep(5)
    raise SystemExit("Fatal: Failed to connect to OpenAI API after multiple attempts.")

def main():
    print("=" * 60)
    print("🌟 8-CHAPTER MASTERPIECE WRITER ENGINE Starting...")
    print("=" * 60)
    
    novel_data = {
        "title": "Thần Y Phòng Khám Quận 5: Vợ Tôi Là Siêu Tỷ Phú",
        "author": "Thanh Phong",
        "genre": "Sảng Văn",
        "intro": "<p><strong>&quot;Năm đó, sếp giật công trình nghiên cứu, bảo vệ ném hành lý của tôi ra đường Nguyễn Trãi dưới cơn mưa tầm tã. Hắn khóa tài khoản Techcombank, ép tôi vào đường cùng và cười khẩy: \\\'Mày chỉ là một con thực tập sinh quèn rách rưới!\\\'&quot;</strong></p><p><strong>&quot;Thế nhưng hắn không ngờ, chỉ một tháng sau, tôi đứng trên đỉnh cao y học Sài Gòn, nắm giữ Nhân Y Đường, châm một cây kim cứu sống siêu tỷ phú đứng đầu Trịnh Gia. Và bên cạnh tôi, là cô con gái độc nhất của Trịnh Gia – siêu mỹ nhân tài phiệt nắm trong tay hàng ngàn tỷ đồng...&quot;</strong></p><hr /><p>Lâm Trần là một bác sĩ thực tập thiên tài tại phòng khám đa khoa An Tâm ở Quận 5, người đã cống hiến cả thanh xuân để nghiên cứu ra liệu pháp đột phá tái tạo tế bào gan bằng thảo dược tự nhiên. Thế nhưng, sự thật tàn nhẫn ập đến khi Trưởng khoa Hoàng Vĩnh – một kẻ tham lam và xảo quyệt – đã cướp đoạt toàn bộ công trình của anh, biến nó thành của riêng rồi đuổi anh ra khỏi phòng khám trong nhục nhã.</p><p>Giữa cơn mưa tầm tã của Sài Gòn, Lâm Trần gặp gỡ Minh Thư, ái nữ sắc sảo của siêu tập đoàn y tế Trịnh Gia. Được sự hậu thuẫn mạnh mẽ của cô, anh quyết định mở phòng khám y học cổ truyền &quot;Nhân Y Đường&quot; ngay đối diện kẻ thù, bắt đầu hành trình lấy lại danh dự và vươn lên đỉnh cao y học. Những trận chiến y lý nghẹt thở, những cú lật kèo pháp lý ngoạn mục và sự trừng phạt đích đáng cho kẻ phản bội đang chờ đón bạn trong tác phẩm này.</p>",
        "cover_prompt": "masterpiece, highly detailed book cover, professional anime illustration, a handsome young Vietnamese doctor in a white coat holding an ancient acupuncture needle, standing next to a beautiful and confident female executive in a modern high-end office overlooking Ho Chi Minh City skyline, bright dramatic lighting, cinematic composition",
        "chapters": []
    }
    
    for idx, chap_outline in enumerate(OUTLINES, 1):
        print(f"\nWriting Chapter {idx}: {chap_outline['title_hint']}...")
        
        system_prompt = """Bạn là THE GHOSTWRITER - Nhà văn tiểu thuyết mạng sảng văn (y thuật, vả mặt, hào môn) số 1 Việt Nam. Bạn có phong cách viết sâu sắc, cực kỳ chi tiết, nhiều kịch tính và cảm xúc tả thực chân thực.
QUY TẮC VIẾT ĐẠT 10/10 ĐIỂM MASTERPIECE:
1. SHOW, DON'T TELL: Hãy tả thực chi tiết các hành động vật lý của nhân vật (như mồ hôi rịn ra trán, ngón tay bấu chặt vào da rỉ máu, nhịp tim hỗn loạn, làn da chuyển xám xanh, hoặc tiếng gót giày gõ sắc lạnh xuống sàn gạch men Quận 5). Tránh các cụm từ sáo rỗng như 'vô biên', 'tột cùng', 'kinh khủng'.
2. Y THUẬT CHÂN THỰC: Khi châm cứu hoặc bốc thuốc, hãy nêu chi tiết khoa học/đông y thực tế (tên các huyệt đạo như Kỳ Môn, Thái Xung, Nhân Trung, Chương Môn, Dũng Tuyền, giải thích sâu cơ chế tuần hoàn huyết khí, các vị thảo dược Nam dược như nhân trần, diệp hạ châu, bồ công anh, cỏ mực, tỉ lệ phối ngũ ấm/mát để giải độc gan, tái tạo mô gan thay vì dùng phép màu thần bí hóa).
3. ĐỒNG BỘ ĐỊA DANH VÀ CHI TIẾT:
   - Toàn bộ bối cảnh phải ở QUẬN 5, TP.HCM (phòng khám An Tâm và Nhân Y Đường nằm đối diện nhau trên các giao lộ sầm uất Quận 5 như Nguyễn Trãi, Hồng Bàng). Tuyệt đối KHÔNG nhắc tới Quận 1.
   - Tài khoản bị khóa lúc đầu là TECHCOMBANK. Tài khoản mới do Minh Thư tài trợ là VIETCOMBANK chứa 5 tỷ VNĐ.
4. HỘI THOẠI ĐANH THÉP: Lời thoại sắc sảo, tự phụ của phản diện và điềm tĩnh, thông minh của nam chính. Các đoạn đối thoại và suy nghĩ nội tâm kéo dài, tạo chiều dày cho tác phẩm.
5. CHIỀU SÂU VÀ ĐỘ DÀI CỰC ĐẠI: Bắt buộc phần 'content' phải có độ dài từ 1000 đến 1500 từ tiếng Việt (khoảng 6000 đến 9000 ký tự bao gồm khoảng trắng). Hãy viết chậm rãi, kéo dài cảnh quay bằng cách đặc tả tâm lý nhân vật, phân tích y lý chi tiết, tả ngoại cảnh mưa giông Sài Gòn Quận 5 hoặc sự náo nhiệt của khu phố đông y Quận 5. Không viết tóm tắt!
6. ĐỊNH DẠNG: Chỉ sử dụng các thẻ HTML cơ bản như <p>, <strong>, <em>."""

        user_prompt = f"""Dựa vào cốt truyện chung:
- Tựa truyện: {novel_data['title']}
- Giới thiệu thế giới quan: {novel_data['intro']}
- Tác giả: {novel_data['author']}

Hãy viết CHI TIẾT CHƯƠNG {idx} của bộ truyện.
- Dàn ý gợi ý Chương {idx}: {chap_outline['outline']}
- Tên chương gợi ý: {chap_outline['title_hint']}

{f"- Các chương trước đã viết tóm tắt: {json.dumps([c['title'] for c in novel_data['chapters']], ensure_ascii=False)}" if novel_data['chapters'] else ""}

BẮT BUỘC ĐỘ DÀI PHẢI TỪ 1000 ĐẾN 1500 TỪ TIẾNG VIỆT (6000 - 9000 ký tự). Hãy kéo dài chi tiết, mô tả từng cử chỉ, nét mặt, phân tích sâu y lý châm cứu/bốc thuốc, phát triển tình cảm tự nhiên giữa Lâm Trần và Minh Thư.

Hãy trả về định dạng JSON chính xác tuyệt đối như sau:
{{
  "title": "Chương {idx}: [Tên chương giật gân, độc đáo]",
  "content": "Nội dung chương viết hoàn chỉnh bằng Tiếng Việt 100%, định dạng HTML với các thẻ <p>, <strong>, <em>..."
}}"""

        chap_raw = call_openai(system_prompt, user_prompt, max_tokens=4500, temperature=0.7)
        
        try:
            chap_data = robust_json_parse(chap_raw)
            novel_data["chapters"].append(chap_data)
            
            # Verify length
            import re as std_re
            text_only = std_re.sub(r'<[^>]+>', ' ', chap_data["content"])
            words = text_only.split()
            print(f"  -> ✓ Success! Generated Chapter {idx}: {chap_data['title']}")
            print(f"     Word count: {len(words)} words (~ {len(chap_data['content'])} characters)")
        except Exception as e:
            print(f"Failed to parse Chapter {idx} JSON. Raw content preview:")
            print(chap_raw[:800])
            # Fallback parsing
            try:
                title_match = re.search(r'"title"\s*:\s*"(.*?)"', chap_raw)
                content_match = re.search(r'"content"\s*:\s*"(.*)"', chap_raw, re.DOTALL)
                if title_match and content_match:
                    novel_data["chapters"].append({
                        "title": title_match.group(1),
                        "content": content_match.group(1).replace('\\"', '"').replace('\\n', '\n')
                    })
                    print(f"  -> ✓ Success (via regex recovery) for Chapter {idx}")
                else:
                    raise e
            except:
                raise SystemExit(f"Fatal error generating Chapter {idx}")
                
        time.sleep(2)
        
    # Write output to pending_novel_8.json
    output_path = "/Users/aaronnguyen/TN/App/doctieuthuyet/scratch/pending_novel_8.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(novel_data, f, ensure_ascii=False, indent=2)
    print(f"\n🎉 ALL 8 CHAPTERS GENERATED AND WRITTEN TO: {output_path}")

if __name__ == "__main__":
    main()
