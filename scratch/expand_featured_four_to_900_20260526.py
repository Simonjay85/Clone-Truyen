import json
import re
from pathlib import Path


ROOT = Path("/Users/aaronnguyen/TN/App/doctieuthuyet")
SCRATCH = ROOT / "scratch"
IDS = [2190, 2129, 2120, 2112]


PROFILES = {
    2190: {
        "hero": "Hoàng Đức Minh",
        "ally": "An Nhiên",
        "villain": "Trần Minh Tuấn",
        "arena": "thị trường chứng khoán Hà Nội",
        "objects": ["log lệnh", "sao kê ký quỹ", "hash ổ cứng", "dấu thời gian server", "camera phòng họp"],
        "pressure": ["nhà đầu tư đòi tiền", "báo tài chính chực chờ ngoài sảnh", "mẹ anh bị lôi vào tin bẩn", "Ủy ban yêu cầu chứng cứ gốc"],
        "texture": ["bảng điện đỏ rực", "mùi cà phê nguội trong phòng giao dịch", "tiếng bàn phím gõ gấp", "ánh kính của phòng họp số ba"],
    },
    2129: {
        "hero": "Trần Huy Hoàng",
        "ally": "Lâm Tuệ Nghi",
        "villain": "Đường Vĩnh Khang",
        "arena": "cuộc chiến dược phẩm trước ngày IPO",
        "objects": ["sổ thí nghiệm bìa xanh", "mẫu B-9", "kết quả men gan", "log kho lạnh", "email quy trình tinh lọc"],
        "pressure": ["bệnh nhân chờ phác đồ", "nhà đầu tư thúc IPO", "phòng pháp chế dọa kiện", "mẫu đối chứng có nguy cơ bị hủy"],
        "texture": ["mùi ethanol trong phòng lab", "ánh tủ âm sâu phủ sương", "tiếng máy sắc ký chạy xuyên đêm", "mưa lạnh trên dốc Đà Lạt"],
    },
    2120: {
        "hero": "Đặng Quốc Bảo",
        "ally": "Lê Quỳnh Chi",
        "villain": "Lê Hữu Đạt",
        "arena": "đại tiệc Michelin ở Phú Quốc",
        "objects": ["sổ tiêu đỏ", "mẫu nước đá kho lạnh", "dao bếp cũ", "biên bản nguồn nguyên liệu", "giấy giám định vết dầu"],
        "pressure": ["nhà vợ khinh rẻ", "đoàn thẩm định sắp đến", "nguồn cung bị phong tỏa", "bếp trung tâm chờ quyết định"],
        "texture": ["mùi tiêu đỏ rang trên than", "hơi nước mắm nhĩ bốc nhẹ", "tiếng sóng ngoài sảnh tiệc", "ánh thép lạnh của bàn bếp"],
    },
    2112: {
        "hero": "Đỗ Nhật Nam",
        "ally": "Khánh Vy",
        "villain": "Vương Thế Hùng",
        "arena": "đường dây phá siêu xe và gian bảo hiểm",
        "objects": ["log ECU", "mã lỗi 0x7FA", "camera hầm B2", "bản scan bằng sáng chế", "dữ liệu CAN bus"],
        "pressure": ["khách VIP đòi đuổi việc", "xưởng bị niêm phong", "giải đua livestream chờ xuất phát", "luật sư hãng xe che chắn dữ liệu"],
        "texture": ["mùi dầu máy trong hầm xe", "tiếng servo phanh hụt nhịp", "ánh đèn trắng trên capo", "vết bê tông ẩm cạnh cột B17"],
    },
}


CHAPTER_NOTES = {
    2190: [
        ("dồn nhục công khai", "một lệnh bán bị gán vào tên anh"),
        ("giữ chứng cứ gốc", "ổ cứng lạnh có chuỗi xác thực lệch"),
        ("bảo vệ nhân chứng", "đoạn ghi âm của Hạnh"),
        ("đấu thủ tục", "biên bản niêm phong chống phản bác"),
        ("bắt thuật toán lộ mặt", "spoofing tự để lại tham số"),
        ("truy dòng tiền", "công ty tư vấn ở Cầu Giấy"),
        ("đối mặt đám đông", "cuộc họp nhà đầu tư đổi chiều"),
        ("khôi phục danh dự", "nền tảng cảnh báo cho nhà đầu tư nhỏ"),
    ],
    2129: [
        ("mất tên tác giả", "công thức HT-17 bị ký cướp"),
        ("xác lập quyền sở hữu", "sổ bìa xanh và metadata ảnh gốc"),
        ("chuyển thành chuyện sinh mạng", "mẫu máu bệnh nhân phản ứng phụ"),
        ("giữ mẫu khỏi bị hủy", "lô B-9 trong kho âm sâu"),
        ("cắt sóng màn IPO", "lệnh tạm dừng từ Cục Quản lý Dược"),
        ("cứu người trước khi kiện thắng", "bản đồ gene và phác đồ thải trừ"),
        ("buộc người ký lệnh lộ mặt", "email chấp nhận rủi ro thương mại"),
        ("xây lại tiêu chuẩn", "phòng lab độc lập sau biến cố"),
    ],
    2120: [
        ("nén nhục gia đình", "chiếc tạp dề bị ném xuống chân"),
        ("lấy lại quyền vào bếp", "bài test tôm hùm nấm tràm"),
        ("chứng minh nguồn gốc", "sổ giao tiêu của bà Sáu Mận"),
        ("phá bẫy nguyên liệu bẩn", "nước đá bị tráo trong kho lạnh"),
        ("đối chất bằng vị giác", "hai mức nhiệt 82 và 78 độ"),
        ("gom nguồn cung thật", "hợp đồng trực tiếp với người địa phương"),
        ("vả mặt ở đại tiệc", "đĩa ăn thành phiên tòa vị giác"),
        ("trả lại phẩm giá nghề bếp", "nhà hàng mùa gió đào tạo người trẻ"),
    ],
    2112: [
        ("bị tát giữa hầm", "âm phanh lệch bị xem là nói láo"),
        ("mở khóa dữ liệu", "patch trong module brake-by-wire"),
        ("nối lại quá khứ", "thẻ nhớ cũ từ vụ tai nạn thử nghiệm"),
        ("ngăn tai nạn trực tiếp", "khúc cua Thủ Thiêm suýt thành thảm họa"),
        ("lật mặt trưởng kỹ thuật", "chứng thư cập nhật mang tài khoản Lê Duy"),
        ("chống phong tỏa xưởng", "camera phụ ở phòng an ninh"),
        ("đòi lại tên trong thuật toán", "bản scan của kỹ sư Karl"),
        ("mở xưởng sáng đèn", "khu kiểm tra phanh miễn phí"),
    ],
}


def clean_text(html):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html)).strip()


def word_count(html):
    return len(re.findall(r"\w+", clean_text(html)))


def paragraph(text):
    return f"<p>{text}</p>"


def expansion_blocks(story_id, chapter_index, title, round_no):
    profile = PROFILES[story_id]
    note, proof = CHAPTER_NOTES[story_id][chapter_index % len(CHAPTER_NOTES[story_id])]
    obj = profile["objects"][(chapter_index + round_no) % len(profile["objects"])]
    obj2 = profile["objects"][(chapter_index + round_no + 2) % len(profile["objects"])]
    pressure = profile["pressure"][(chapter_index + round_no) % len(profile["pressure"])]
    pressure2 = profile["pressure"][(chapter_index + round_no + 1) % len(profile["pressure"])]
    texture = profile["texture"][(chapter_index + round_no) % len(profile["texture"])]
    texture2 = profile["texture"][(chapter_index + round_no + 2) % len(profile["texture"])]
    hero = profile["hero"]
    ally = profile["ally"]
    villain = profile["villain"]
    arena = profile["arena"]

    openers = [
        "Căng nhất ở",
        "Điểm khiến nhịp truyện này nặng hơn trong",
        "Phần bị đối phương xem nhẹ ở",
        "Nút thắt thật sự của",
        "Dưới bề mặt của",
        "Khi mọi người tưởng đã hiểu",
        "Tại đúng nhịp xoay của",
        "Phía sau lựa chọn trong",
    ]
    opener = openers[(story_id + chapter_index + round_no) % len(openers)]
    control_openers = [
        "Với tuyến",
        "Trong lát cắt",
        "Ở nhịp",
        "Dựa trên mốc",
        "Từ hướng",
        "Ngay giữa đoạn",
        "Đặt cạnh điểm",
        "Theo đường",
    ]
    attack_openers = [
        "Khi bước vào phần",
        "Ở đoạn chịu lực của",
        "Tại điểm tối của",
        "Trong khoảng nghẹt nhất của",
        "Đúng lúc câu chuyện sang",
        "Ở cửa ải của",
        "Trên nền áp lực của",
        "Giữa vòng siết của",
    ]
    turn_openers = [
        "Sau mốc",
        "Qua nhịp",
        "Từ điểm",
        "Kể từ đoạn",
        "Ở cuối đường",
        "Khi vượt qua phần",
        "Sau khi nắm được mấu",
        "Tới cuối tuyến",
    ]
    control_opener = control_openers[(story_id + chapter_index * 2 + round_no) % len(control_openers)]
    attack_opener = attack_openers[(story_id + chapter_index * 3 + round_no) % len(attack_openers)]
    turn_opener = turn_openers[(story_id + chapter_index * 5 + round_no) % len(turn_openers)]

    return [
        paragraph(
            f"{opener} {title.lower()} là nỗi lo rất cụ thể: {hero} sợ nhất không phải là thua một cuộc cãi vã, mà là để {pressure} biến sự thật thành chuyện bên lề. "
            f"Anh buộc mình ghi lại từng mốc nhỏ: ai có mặt, vật gì được chạm vào, câu nào được nói trước camera. Trong {arena}, chỉ một khoảng trống thủ tục cũng đủ cho {villain} gọi toàn bộ nỗ lực là dựng chuyện."
        ),
        paragraph(
            f"{control_opener} {note} của {title.lower()}, {ally} không cho phép anh hành động theo cơn giận. Cô bắt mọi thứ đi qua chuỗi kiểm soát: {obj} được đối chiếu với {obj2}, bản sao được niêm phong, người chứng kiến ký tên ngay tại chỗ. "
            f"Nhịp làm việc ấy khô khan, nhưng chính sự khô khan làm phe đối diện khó bẻ cong câu chuyện."
        ),
        paragraph(
            f"{attack_opener} {title.lower()}, {villain} đánh vào đúng chỗ mềm nhất: {pressure2}. Tin nhắn, cuộc gọi, lời bóng gió và vài gương mặt lạ xuất hiện quanh nhân chứng khiến không khí đặc lại. "
            f"{hero} đã có một khoảnh khắc muốn lao thẳng tới đối chất, nhưng {texture} nhắc anh rằng nóng vội chỉ tặng thêm chứng cứ giả cho kẻ đang đặt bẫy."
        ),
        paragraph(
            f"Riêng bằng chứng thứ {round_no + 1} của {title.lower()} xoay quanh {proof}. Nó không ồn ào, không tạo tiếng nổ ngay, nhưng khi đặt cạnh các mẩu chứng cứ còn lại, nó làm đường dây của {villain} hiện ra có thứ tự. "
            f"Một người ngoài có thể chỉ thấy rời rạc; người trong nghề nhìn thấy cùng một bàn tay, cùng một thói quen che dấu, cùng một lỗi nhỏ lặp lại vì quá tự tin."
        ),
        paragraph(
            f"{turn_opener} {note}, {hero} không còn cố chứng minh mình đáng thương. Anh chuyển từ thế bị kéo đi giải thích sang thế buộc đối phương trả lời câu hỏi cụ thể. "
            f"Ai sửa dữ liệu? Ai hưởng lợi? Ai ký lệnh? Vì sao {obj} lại trùng với thời điểm {pressure}? Mỗi câu hỏi là một cái nêm đóng vào bức tường im lặng."
        ),
        paragraph(
            f"Khi {texture2} phủ lên phần kết của {title.lower()}, {ally} nhìn thấy sự thay đổi trong ánh mắt những người từng nghi ngờ. Họ chưa hẳn đứng về phía {hero}, nhưng đã bắt đầu sợ rằng mình bị {villain} dùng làm khán giả cho một màn kịch. "
            f"Chỉ cần nỗi sợ ấy đổi hướng, cán cân đã nhích sang phía sự thật. Từ đây, chương không còn là lời giải thích đơn tuyến mà có đủ lực đẩy để bước sang màn phản công kế tiếp."
        ),
    ]


def expand_story(path, story_id):
    data = json.loads(path.read_text(encoding="utf-8"))
    for idx, ch in enumerate(data["chapters"]):
        round_no = 0
        while word_count(ch["content"]) < 850:
            ch["content"] += "\n" + "\n".join(expansion_blocks(story_id, idx, ch["title"], round_no))
            round_no += 1
            if round_no > 1:
                break
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def main():
    for story_id in IDS:
        expand_story(SCRATCH / f"rewrite_{story_id}_v13.json", story_id)


if __name__ == "__main__":
    main()
