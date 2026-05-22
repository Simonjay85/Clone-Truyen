import json

final_file_path = "/Users/aaronnguyen/TN/App/doctieuthuyet/pending_novel_9.json"
with open(final_file_path, "r", encoding="utf-8") as f:
    novel_data = json.load(f)

# Chapter 7 Expansion (index 6)
ch7_s = [s.replace("<p>", "").replace("</p>", "").strip() for s in novel_data["chapters"][6]["content"].split("</p>\\n") if s.strip()]
extra_ch7 = [
    "Hội trường Philharmonic Hall ngập tràn trong kiến trúc Baroque tráng lệ với những bức phù điêu mạ vàng lấp lánh.",
    "Lịch sử hàng trăm năm của tòa nhà như hiện hữu trong từng thớ gỗ của sân khấu, nơi tiếng đàn của các vĩ nhân từng vang vọng.",
    "Phúc cảm thấy sức nặng của lịch sử đè lên vai mình, nhưng đó không phải là áp lực bóp nghẹt mà là động lực nâng cánh bay.",
    "Đối thủ ngồi hàng ghế phía trước - Igor Smirnov, thần đồng người Nga đến từ Học viện Tchaikovsky - liếc nhìn Phúc với ánh mắt dò xét, khinh khỉnh.",
    "Tuy nhiên, khi Phúc bắt đầu những nốt nhạc đầu tiên, sự khinh khỉnh trên mặt Smirnov hoàn toàn biến mất, thay vào đó là sự kinh hoàng tột độ.",
    "Anh ta nhận ra kỹ thuật chạy ngón legato của Phúc đạt đến mức độ trôi chảy tuyệt đối mà anh ta chưa từng thấy ở bất kỳ ai.",
    "Từng nốt nhạc như những hạt sương mai rơi xuống mặt hồ yên ả, tạo nên những bước sóng âm thanh lan tỏa đều khắp khán phòng lớn.",
    "Linh ngồi ở hàng ghế VIP phía sau, đôi mắt phượng nhìn chằm chằm vào bóng lưng của Phúc đầy tự hào.",
    "Cô nhớ lại buổi trưa mưa rào Sài Gòn tại cư xá Thanh Đa, khi một chàng trai trẻ gầy gò chơi cây piano Yamaha Yamaha cũ kỹ bong tróc.",
    "Hôm nay, chàng trai ấy đang ngồi chơi trên cây đàn Steinway & Sons đắt giá nhất thế giới trước toàn thể tinh hoa âm nhạc toàn cầu.",
    "Sự tương phản mãnh liệt đó khiến Linh cảm thấy sống mũi cay cay, cô khẽ nở một nụ cười ấm áp đầy kiêu hãnh.",
    "Tiếng đàn của Phúc đã vượt qua ranh giới của một bài dự thi, nó trở thành một cuộc độc thoại đầy nghệ thuật giữa nghệ sĩ và Chopin.",
    "Ban giám khảo người Ba Lan - bà Maria Jablonska, một huyền thoại piano sống - khẽ nghiêng đầu lắng nghe với sự trân trọng tuyệt đối.",
    "Bà ghi chép nhanh vào sổ chấm điểm: 'Một tài năng phi thường có khả năng thấu hiểu sâu sắc tư tưởng âm nhạc của Chopin mà không cần phô trương kỹ thuật sáo rỗng'."
]
ch7_s.extend(extra_ch7)
novel_data["chapters"][6]["content"] = "\\n".join([f"<p>{s}</p>" for s in ch7_s])

# Chapter 8 Expansion (index 7)
ch8_s = [s.replace("<p>", "").replace("</p>", "").strip() for s in novel_data["chapters"][7]["content"].split("</p>\\n") if s.strip()]
extra_ch8 = [
    "Tại văn phòng của Luật sư Trần Hữu Trí trên đường Nguyễn Huệ, Quận 1, toàn bộ hồ sơ vụ án đã được chuẩn bị vô cùng hoàn hảo.",
    "Bản lập luận pháp lý của luật sư dựa trên Điều 19 và Điều 20 của Luật Sở hữu trí tuệ Việt Nam về quyền nhân thân và quyền tài sản của tác giả.",
    "Họ chứng minh rõ ràng rằng Nguyễn Thế Anh không hề có bất kỳ quá trình sáng tác độc lập nào đối với tác phẩm này.",
    "Đồng thời, cuộc thanh tra tài chính tại Nhạc viện TP.HCM phát hiện Thế Phong đã rút ruột hơn mười tỷ đồng ngân sách đầu tư trang thiết bị dạy học.",
    "Hồ sơ kế toán giả mạo, các hóa đơn mua sắm thiết bị âm thanh nhập khẩu từ Đức bị nâng khống giá trị lên gấp ba lần.",
    "Sai phạm học thuật kết hợp với tội danh kinh tế đã đóng chiếc đinh cuối cùng vào cỗ quan tài sự nghiệp của cha con hiệu trưởng.",
    "Các giảng viên trước đây từng im lặng vì sợ quyền lực của Thế Phong giờ đây đồng loạt đứng lên tố cáo những sai phạm của ông ta.",
    "Toàn bộ bầu không khí tại Nhạc viện như được thanh lọc, mở ra một chương mới cho các tài năng trẻ thực sự.",
    "Trong khi đó, trên các trang mạng xã hội trong nước, các clip quay lại buổi diễn của Phúc tại Warsaw đạt hàng triệu lượt xem chỉ sau một đêm.",
    "Người dân Việt Nam vô cùng tự hào khi thấy một người con của đất nước tỏa sáng rực rỡ bằng thực lực trên đấu trường quốc tế danh giá nhất.",
    "Sự thật cuối cùng đã chiến thắng, công lý đã được thực thi trọn vẹn và ngọt ngào nhất dưới ánh sáng của pháp luật và sự thật nghệ thuật."
]
ch8_s.extend(extra_ch8)
novel_data["chapters"][7]["content"] = "\\n".join([f"<p>{s}</p>" for s in ch8_s])

# Chapter 9 Expansion (index 8)
ch9_s = [s.replace("<p>", "").replace("</p>", "").strip() for s in novel_data["chapters"][8]["content"].split("</p>\\n") if s.strip()]
extra_ch9 = [
    "Khán phòng Philharmonic Hall lung linh dưới ánh đèn vàng ấm áp, tạo nên một không gian vô cùng huyền ảo cổ kính.",
    "Bản Concerto số 1 giọng Mi thứ đòi hỏi sự phối hợp tuyệt đối giữa nghệ sĩ piano và nhạc trưởng giao hưởng.",
    "Nhạc trưởng người Ba Lan - ông Andrzej Boreyko - liên tục trao đổi ánh mắt với Phúc, hai người phối hợp nhịp nhàng như một thể thống nhất.",
    "Họ thở cùng một nhịp thở, cảm nhận từng nhịp đập của giai điệu, tạo nên một sự hòa quyện hoàn mỹ giữa piano và dàn nhạc.",
    "Trong đoạn cadenza đơn độc của chương một, Phúc biểu diễn một chuỗi biến tấu ngẫu hứng vô cùng thông minh và đầy tính học thuật.",
    "Tiếng đàn của cậu ngân vang độc lập đầy kiêu hãnh giữa không gian im phăng phắc của khán phòng Philharmonic.",
    "Từng nốt nhạc chứa đựng câu chuyện kiêu hãnh của một người Việt Nam vượt qua muôn vàn gian khó để đứng trên đỉnh cao thế giới.",
    "Khán giả ngồi dưới hàng ghế VIP - ngài Đại sứ Việt Nam tại Ba Lan - khẽ mỉm cười đầy xúc động, tay nắm chặt vạt áo vest.",
    "Bên cạnh ông, các nhà phê bình âm nhạc quốc tế liên tục gật đầu trầm trồ trước sự điêu luyện và cảm xúc dạt dào của Phúc.",
    "Họ biết rằng, đêm nay, họ đang được chứng kiến sự ra đời của một huyền thoại âm nhạc mới, một ngôi sao sáng chói trên bầu trời nghệ thuật thế giới."
]
ch9_s.extend(extra_ch9)
novel_data["chapters"][8]["content"] = "\\n".join([f"<p>{s}</p>" for s in ch9_s])

# Chapter 10 Expansion (index 9)
ch10_s = [s.replace("<p>", "").replace("</p>", "").strip() for s in novel_data["chapters"][9]["content"].split("</p>\\n") if s.strip()]
extra_ch10 = [
    "Buổi lễ trao giải diễn ra vô cùng long trọng với sự hiện diện của Tổng thống Ba Lan và các quan chức văn hóa ngoại giao hai nước.",
    "Phần thưởng trị giá 40.000 Euro được trao cho Phúc cùng chiếc Huy chương Vàng danh giá nhất hành tinh.",
    "Trong bài phát biểu nhận giải bằng tiếng Anh lưu loát, Phúc đã dành những lời tri ân sâu sắc nhất tới đất nước Việt Nam và cô Trần Diệu Linh.",
    "\"Bản nhạc này thuộc về Việt Nam, thuộc về công lý nghệ thuật thực sự.\" Lời phát biểu của cậu nhận được tràng pháo tay nồng nhiệt.",
    "Báo chí Ba Lan gọi Phúc là 'Cơn địa chấn châu Á', người đã mang đến một hơi thở hoàn toàn mới cho âm nhạc của Chopin.",
    "Tại Việt Nam, cha con Nguyễn Thế Phong chính thức bắt đầu những ngày tháng đền tội trong trại giam Chí Hòa lạnh lẽo.",
    "Thế Phong ngồi trong phòng giam chật hẹp, nhìn qua khe cửa sắt nhỏ nhoi lên bầu trời đêm, lòng đầy sự hối hận muộn màng.",
    "Toàn bộ tài sản lừa đảo tham ô của họ bị tịch thu để bồi thường thiệt hại và sung công quỹ nhà nước.",
    "Còn Lâm Hoàng Phúc lúc này đang đứng giữa Warsaw tuyết phủ trắng xóa, nắm tay Trần Diệu Linh cùng hướng về tương lai huy hoàng sắp tới.",
    "Họ đã cùng nhau vượt qua giông bão để bước lên đỉnh cao vinh quang chói lọi, tự tay viết nên một trang sử mới đầy kiêu hãnh cho cuộc đời mình."
]
ch10_s.extend(extra_ch10)
novel_data["chapters"][9]["content"] = "\\n".join([f"<p>{s}</p>" for s in ch10_s])

# Let's ensure formatting is exact
for ch in novel_data["chapters"]:
    # Make sure every sentence ends with \n or rather paragraphs are joined by \n
    # Let's double check if we need \n between paragraph tags
    content_raw = ch["content"]
    # Re-clean and re-assemble to guarantee <p>...</p>\n<p>...</p> format
    paragraphs = [p.replace("<p>", "").replace("</p>", "").strip() for p in content_raw.split("\n") if p.strip()]
    # Actually split by \n or </p>
    paragraphs_clean = []
    for p in paragraphs:
        # split by </p> just in case
        sub_p = [sp.replace("<p>", "").replace("</p>", "").strip() for sp in p.split("</p>") if sp.strip()]
        paragraphs_clean.extend(sub_p)
    
    formatted_content = "\n".join([f"<p>{p}</p>" for p in paragraphs_clean])
    ch["content"] = formatted_content

with open(final_file_path, "w", encoding="utf-8") as f:
    json.dump(novel_data, f, ensure_ascii=False, indent=2)

print("Chapters 7-10 expanded successfully and validated.")
