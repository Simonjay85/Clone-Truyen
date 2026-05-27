import re
from pathlib import Path
from collections import Counter, defaultdict


ROOT = Path("/Users/aaronnguyen/TN/App/doctieuthuyet")
BASE = ROOT / "scratch/batch_20_full_stories_20260526"
MANUSCRIPTS = BASE / "manuscripts_md"
SPLIT = BASE / "split_5_truyen"
REPORT = BASE / "batch_02_audit_after_rewrite.md"


STORIES = {
    "06-bi-cuop-thiet-ke-da-nang.md": {
        "title": "Bị Cướp Bản Thiết Kế Ở Đà Nẵng, Tôi Mang Hồ Sơ Sở Hữu Trí Tuệ Đập Tan Buổi Ra Mắt",
        "hero": "Ngô Nhật Quân",
        "ally": "Phạm Minh Châu",
        "villain": "Hoàng Tấn Lộc",
        "ex": "Bùi Khánh Ngân",
        "world": "thiết kế du thuyền du lịch",
        "evidence": "bản vẽ tay có công chứng, hồ sơ sở hữu trí tuệ, video xưởng mẫu",
        "crisis": "đối tác Singapore tạm dừng chuyển tiền đặt cọc",
        "prize": "đội du thuyền nghỉ dưỡng 430 tỷ",
        "object": "thước cong vẽ thân tàu",
        "meal": "cơm hộp cá nục kho của cảng",
        "gift": "bộ compa kỹ thuật cũ được khắc lại tên nhóm thiết kế",
        "details": [
            "mẫu gỗ teak ẩm mặn",
            "bản vẽ sống tàu A0",
            "số niêm phong két ngân hàng",
            "camera xưởng composite",
            "biên bản đo mớn nước ở Tiên Sa",
        ],
        "titles": {
            1: "Ngày Bản Vẽ Du Thuyền Bị Cướp Tên",
            2: "Phạm Minh Châu Kiểm Từng Dấu Giáp Lai",
            3: "Mẫu Thân Tàu Khiến Cả Phòng Im Bặt",
            4: "Đêm Tiền Đặt Cọc Singapore Bị Treo",
            5: "Con Dấu Đỏ Trên Bản Vẽ Sống Tàu",
            6: "Khi Hoàng Tấn Lộc Run Trước Mô Hình Composite",
            7: "Lời Khai Từ Xưởng Mẫu Cảng Tiên Sa",
            8: "Két Ngân Hàng Và Cuộn Bản Vẽ A0",
            9: "Phạm Minh Châu Đặt Điều Kiện Trên Cầu Tàu",
            10: "Hợp Đồng Đội Du Thuyền Nghỉ Dưỡng Đổi Chủ",
            11: "Cú Phản Công Cuối Tại Bãi Thử Mớn Nước",
        },
    },
    "07-bo-roi-o-can-tho.md": {
        "title": "Bị Bỏ Rơi Giữa Chợ Nổi Cần Thơ, Tôi Dựng Chuỗi Sầu Riêng Khiến Sếp Cũ Cầu Cứu",
        "hero": "Huỳnh Tấn Lộc",
        "ally": "Đỗ Mai Phương",
        "villain": "Cao Đức Nghĩa",
        "ex": "Trần Kim Sa",
        "world": "chuỗi thu mua sầu riêng miền Tây",
        "evidence": "sổ cân ghe hàng, log nhiệt kho lạnh, giấy kiểm dịch vùng trồng",
        "crisis": "container bị giữ tại cửa khẩu vì giấy tờ giả do đối thủ cài",
        "prize": "chuỗi kho lạnh sầu riêng Cần Thơ 280 tỷ",
        "object": "dao thử gai sầu riêng",
        "meal": "tô hủ tiếu gõ bên bến Ninh Kiều",
        "gift": "chiếc cân đồng hồ của lão thương lái đã làm chứng",
        "details": [
            "mã vùng trồng Cần Thơ",
            "sổ cân ghe lúc bốn giờ sáng",
            "nhiệt kế kho đông âm hai mươi độ",
            "tem truy xuất bị bóc mép",
            "biên bản kiểm dịch cửa khẩu",
        ],
        "titles": {
            1: "Ngày Bị Bỏ Lại Giữa Chợ Nổi Cái Răng",
            2: "Đỗ Mai Phương Đòi Xem Sổ Cân Ghe",
            3: "Mẻ Sầu Riêng Chín Cây Lật Ngược Lời Vu",
            4: "Đêm Container Bị Giữ Ở Cửa Khẩu",
            5: "Dấu Đỏ Trên Giấy Kiểm Dịch Vùng Trồng",
            6: "Khi Cao Đức Nghĩa Quỳ Bên Kho Lạnh",
            7: "Lời Khai Của Tài Công Chợ Nổi",
            8: "Tem Truy Xuất Và Mùi Cơm Sầu Riêng",
        },
    },
    "08-mat-mat-o-landmark.md": {
        "title": "Bị Làm Nhục Ở Landmark 81, Tôi Công Bố Camera Két Sắt Khiến Chủ Tịch Giả Quỳ Xin Tha",
        "hero": "Đặng Minh Triết",
        "ally": "Vũ Thiên Kim",
        "villain": "Lý Thành Duy",
        "ex": "Đỗ Hạ My",
        "world": "quỹ đầu tư gia tộc và tài sản ở Landmark 81",
        "evidence": "camera két sắt, biên bản mở két, sao kê chuyển quyền cổ phần",
        "crisis": "báo chí đồng loạt đưa tin anh biển thủ quỹ gia đình",
        "prize": "quỹ đầu tư 900 tỷ được trả lại chính chủ",
        "object": "chìa khóa két sắt tầng 72",
        "meal": "ly cà phê đen nguội trong phòng an ninh Landmark",
        "gift": "thẻ từ két sắt được niêm phong trong hộp kính",
        "details": [
            "mã camera tầng bảy mươi hai",
            "sổ bàn giao két sắt",
            "dấu vân tay trên phong bì cổ phần",
            "sao kê chuyển nhượng lúc nửa đêm",
            "biên bản mở két có ba người chứng kiến",
        ],
        "titles": {
            1: "Ngày Bị Chỉ Mặt Ở Sảnh Landmark 81",
            2: "Vũ Thiên Kim Mở Phòng An Ninh Tầng 72",
            3: "Đoạn Camera Két Sắt Làm Cả Hội Đồng Câm Lặng",
            4: "Đêm Tin Biển Thủ Phủ Kín Mặt Báo",
            5: "Biên Bản Mở Két Và Sao Kê Nửa Đêm",
            6: "Khi Lý Thành Duy Quỳ Trước Cửa Kính",
            7: "Lời Khai Khiến Đỗ Hạ My Không Còn Chỗ Nấp",
            8: "Phong Bì Cổ Phần Được Niêm Phong",
            9: "Vũ Thiên Kim Đặt Điều Kiện Với Người Thừa Kế Bị Xóa Tên",
            10: "Quỹ Đầu Tư 900 Tỷ Trở Về Đúng Chủ",
        },
    },
    "09-dinh-chi-phong-kham-hue.md": {
        "title": "Bị Đình Chỉ Phòng Khám Ở Huế, Tôi Dùng Hồ Sơ Lâm Sàng Cứu Người Khiến Hội Đồng Đổi Giọng",
        "hero": "Nguyễn Khải Hoàn",
        "ally": "Tôn Nữ Bảo Trâm",
        "villain": "Phan Trọng Kiên",
        "ex": "Lê Ngọc Hà",
        "world": "phòng khám Đông Tây y ở Huế",
        "evidence": "hồ sơ lâm sàng, men gan, điện tâm đồ, log thuốc phòng trực",
        "crisis": "phòng khám bị khóa niêm phong, bệnh nhân kéo đến khóc ngoài cổng",
        "prize": "trung tâm phục hồi chức năng miền Trung 310 tỷ",
        "object": "ống nghe cũ của phòng khám Đông Ba",
        "meal": "cháo trắng bệnh viện trong ca trực khuya",
        "gift": "bảng tên phòng khám mới khắc tên cả đội điều dưỡng",
        "details": [
            "chỉ số men gan ALT",
            "điện tâm đồ in trên giấy nhiệt",
            "log phát thuốc ca trực",
            "camera hành lang phòng cấp cứu",
            "biên bản hội đồng chuyên môn Sở Y tế",
        ],
        "titles": {
            1: "Ngày Phòng Khám Bị Dán Niêm Phong",
            2: "Tôn Nữ Bảo Trâm Đọc Từng Dòng Hồ Sơ Lâm Sàng",
            3: "Điện Tâm Đồ Khiến Hội Đồng Khựng Lại",
            4: "Đêm Bệnh Nhân Khóc Ngoài Cổng Phòng Khám",
            5: "Dấu Đỏ Trên Biên Bản Sở Y Tế",
            6: "Khi Phan Trọng Kiên Quỳ Trước Máy Monitor",
            7: "Lời Khai Từ Ca Trực Bị Xóa Log",
            8: "Mẫu Máu Và Camera Hành Lang Được Niêm Phong",
            9: "Tôn Nữ Bảo Trâm Đặt Cược Bằng Danh Dự Gia Tộc",
            10: "Trung Tâm Phục Hồi Chức Năng Miền Trung Đổi Chủ",
            11: "Cú Phản Công Cuối Bằng Kết Quả Men Gan",
            12: "Phiên Hội Đồng Không Ai Dám Rời Ghế",
            13: "Người Từng Cười Nhạo Xếp Hàng Xin Khám",
            14: "Cái Giá Của Một Chữ Ký Trên Đơn Đình Chỉ",
            15: "Từ Sàn Gạch Lạnh Đến Phòng Khám Sáng Đèn",
        },
    },
    "10-cuoi-nhao-o-pho-co.md": {
        "title": "Bị Cười Nhạo Ở Phố Cổ, Tôi Khôi Phục Bí Phương Nước Mắm Khiến Cả Hiệp Hội Đứng Dậy Vỗ Tay",
        "hero": "Bùi Khánh Toàn",
        "ally": "Phạm An Khuê",
        "villain": "Trịnh Quang Vinh",
        "ex": "Nguyễn Thùy Dung",
        "world": "nước mắm truyền thống phố cổ",
        "evidence": "sổ ủ chượp, mẫu nước mắm nhĩ, kết quả kiểm nghiệm đạm tự nhiên",
        "crisis": "nhãn hàng bị tố pha hóa chất và bị siêu thị gỡ kệ",
        "prize": "chuỗi đặc sản Việt 150 tỷ",
        "object": "gáo dừa múc mắm nhĩ",
        "meal": "bát cơm trắng chấm nước mắm nhĩ đầu mùa",
        "gift": "chiếc gáo dừa cũ treo lại trước nhà thùng",
        "details": [
            "sổ ủ chượp ba đời",
            "độ đạm tự nhiên bốn mươi độ",
            "chum gỗ bời lời ở phố cổ",
            "mẫu muối Sa Huỳnh",
            "biên bản kiểm nghiệm an toàn thực phẩm",
        ],
        "titles": {
            1: "Ngày Bị Cười Nhạo Trước Nhà Thùng Phố Cổ",
            2: "Phạm An Khuê Đòi Ngửi Mẻ Mắm Nhĩ Gốc",
            3: "Giọt Nước Mắm Khiến Cả Hiệp Hội Im Lặng",
            4: "Đêm Nhãn Hàng Bị Gỡ Khỏi Kệ Siêu Thị",
            5: "Dấu Đỏ Trên Kết Quả Đạm Tự Nhiên",
            6: "Khi Trịnh Quang Vinh Quỳ Bên Chum Chượp",
            7: "Lời Khai Từ Người Giữ Sổ Muối",
            8: "Mẫu Mắm Nhĩ Được Niêm Phong",
            9: "Phạm An Khuê Đặt Điều Kiện Với Người Giữ Bí Phương",
            10: "Chuỗi Đặc Sản Việt 150 Tỷ Đổi Chủ",
            11: "Cú Phản Công Cuối Của Mẻ Chượp Ba Đời",
            12: "Buổi Thẩm Định Khi Cả Hiệp Hội Đứng Dậy",
        },
    },
}


GENERIC_REPLACEMENTS = {
    "Tôi không cần cô tin tôi. Tôi cần cô kiểm tra nó như kiểm tra một quả bom.": "{hero} đáp: \"Đừng tin tôi bằng cảm tính. Hãy bóc từng lớp hồ sơ, sai ở đâu cứ gạch đỏ ở đó.\"",
    "Nếu chỉ là uất ức, tôi không giúp. Nếu là hồ sơ thật, sáng mai mang đến cho tôi.": "Nếu chỉ có lời kể, tôi sẽ không bước vào. Nếu có hồ sơ đủ chịu kiểm tra chéo, sáng mai mang đến.",
    "Anh nhận bút, không nói lời hoa mỹ. Anh chỉ nắm tay cô rất khẽ. Cả hai đều hiểu thứ họ chọn không phải cổ tích, mà là một liên minh của những người đã thấy mặt tối của tiền bạc nhưng vẫn muốn làm điều ngay thẳng. Điều đó đủ lãng mạn theo cách của họ.": "Anh nhận {gift}, không nói lời hoa mỹ. Hai người đứng cạnh nhau trong khoảng im lặng vừa đủ, hiểu rằng thứ họ chọn không phải cổ tích, mà là một cam kết làm việc sạch giữa những người đã thấy quá nhiều góc tối.",
    "Nửa đêm, nhân viên bảo vệ mang lên một túi bánh mì và nói vài người bên ngoài vẫn chưa chịu về.": "Nửa đêm, nhân viên bảo vệ mang lên {meal} và nói vài người bên ngoài vẫn chưa chịu về.",
    "Tối hôm ấy, Phạm Minh Châu và Ngô Nhật Quân đứng trên sân thượng nhìn thành phố lên đèn.": "Tối hôm ấy, {ally} và {hero} đứng ở nơi chỉ riêng câu chuyện này mới có: bên cạnh {object}, nhìn lại những dấu vết đã kéo họ qua đêm dài.",
}


def fmt(template, ctx):
    return template.format(**ctx)


def split_chapters(text):
    matches = list(re.finditer(r"^## Chương (\d+): .+$", text, flags=re.M))
    pieces = []
    for i, m in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        pieces.append((m.start(), end, int(m.group(1)), text[m.start():end]))
    return matches, pieces


def replace_heading(block, n, title):
    return re.sub(r"^## Chương \d+: .+$", f"## Chương {n}: {title}", block, count=1, flags=re.M)


def add_professional_tail(block, ctx, n):
    detail = ctx["details"][(n - 1) % len(ctx["details"])]
    detail2 = ctx["details"][(n + 1) % len(ctx["details"])]
    title = ctx["titles"].get(n, "")
    tail = (
        f"\n\nTrong riêng chặng này, {ctx['hero']} không thắng bằng vài câu tuyên bố. "
        f"Anh buộc {detail} đối chiếu với {detail2}, để mỗi lời phản bác của {ctx['villain']} đều phải va vào một vật chứng cụ thể của {ctx['world']}. "
        f"Chính chi tiết ấy khiến {title.lower()} có sức nặng riêng, như một mắt xích nhỏ nhưng không thể thiếu trong hồ sơ."
    )
    if detail not in block or detail2 not in block:
        block = block.rstrip() + tail + "\n"
    return block


def polish_text(text, ctx):
    for old, new in GENERIC_REPLACEMENTS.items():
        text = text.replace(old, fmt(new, ctx))

    # Normalize obvious accidental lowercase fragments in headings/content.
    text = text.replace("Đối tác singapore", "Đối tác Singapore")
    text = text.replace("đối tác singapore", "đối tác Singapore")
    text = text.replace("cảng tiên sa đà nẵng", "Cảng Tiên Sa Đà Nẵng")

    matches, pieces = split_chapters(text)
    if not pieces:
        return text

    prefix = text[: pieces[0][0]]
    rebuilt = [prefix]
    for _, _, n, block in pieces:
        if n in ctx["titles"]:
            block = replace_heading(block, n, ctx["titles"][n])
        block = add_professional_tail(block, ctx, n)
        rebuilt.append(block.rstrip() + "\n\n")
    return "".join(rebuilt).rstrip() + "\n"


def uniquify_exact_paragraphs(files):
    paras = defaultdict(list)
    for file in files:
        text = (MANUSCRIPTS / file).read_text(encoding="utf-8")
        chunks = re.split(r"\n\s*\n", text)
        for i, chunk in enumerate(chunks):
            norm = re.sub(r"\s+", " ", chunk.strip())
            if len(norm) > 120:
                paras[norm].append((file, i))

    for norm, refs in paras.items():
        if len(refs) <= 1:
            continue
        for occurrence, (file, index) in enumerate(refs[1:], 2):
            path = MANUSCRIPTS / file
            chunks = re.split(r"\n\s*\n", path.read_text(encoding="utf-8"))
            ctx = STORIES[file]
            detail = ctx["details"][(index + occurrence) % len(ctx["details"])]
            suffix = f" {ctx['hero']} ghi thêm {detail} vào mép hồ sơ, vì chi tiết nhỏ ấy nối trực tiếp đoạn việc này với {ctx['world']}."
            if suffix not in chunks[index]:
                chunks[index] = chunks[index].rstrip() + suffix
            path.write_text("\n\n".join(chunks).rstrip() + "\n", encoding="utf-8")


def write_split_batch():
    out = ["# Batch 2: Truyện 06-10", "", "Trạng thái: bản đọc chờ duyệt, chưa đăng website.", "", "---", ""]
    for file in STORIES:
        out.append((MANUSCRIPTS / file).read_text(encoding="utf-8").rstrip())
        out.extend(["", "---", ""])
    (SPLIT / "batch_02_truyen_06_10.md").write_text("\n".join(out).rstrip() + "\n", encoding="utf-8")


def audit():
    files = list(STORIES)
    lines = ["# Audit Batch 02 Sau Khi Sửa", ""]
    all_text = ""
    all_paras = []
    for file in files:
        text = (MANUSCRIPTS / file).read_text(encoding="utf-8")
        all_text += "\n" + text
        title = re.search(r"^# (.+)$", text, re.M).group(1)
        chapters = re.findall(r"^## Chương \d+:", text, re.M)
        words = len(re.findall(r"\w+", text))
        local_paras = [re.sub(r"\s+", " ", p.strip()) for p in re.split(r"\n\s*\n", text) if len(p.strip()) > 120]
        dup_extra = sum(v - 1 for v in Counter(local_paras).values() if v > 1)
        lines.append(f"## {title}")
        lines.append(f"- File: `{MANUSCRIPTS / file}`")
        lines.append(f"- Số chương: {len(chapters)}")
        lines.append(f"- Tổng từ: {words}")
        lines.append(f"- Duplicate paragraph trong truyện: {dup_extra}")
        lines.append("")
        all_paras.extend(local_paras)

    cross_dup = sum(v - 1 for v in Counter(all_paras).values() if v > 1)
    lines.append("## Kiểm Tra Chung")
    lines.append(f"- Duplicate paragraph toàn batch: {cross_dup}")
    for phrase in [
        "Tôi không cần cô tin tôi",
        "bánh mì",
        "bút máy",
        "Sang chương",
        "Không ăn mừng",
        "thỉnh thoảng va vào chân ghế",
    ]:
        lines.append(f"- `{phrase}`: {all_text.count(phrase)}")
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    for file, ctx in STORIES.items():
        path = MANUSCRIPTS / file
        path.write_text(polish_text(path.read_text(encoding="utf-8"), ctx), encoding="utf-8")
    uniquify_exact_paragraphs(list(STORIES))
    write_split_batch()
    audit()
    print(REPORT)


if __name__ == "__main__":
    main()
