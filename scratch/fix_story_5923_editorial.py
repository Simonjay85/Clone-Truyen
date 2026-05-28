#!/usr/bin/env python3
import importlib.util
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EDITOR_PATH = ROOT / "scratch" / "novel_editor.py"
BACKUP = ROOT / "scratch" / "story_5923_before_fix.json"
OUT = ROOT / "scratch" / "story_5923_editorial_fix_result.json"

spec = importlib.util.spec_from_file_location("novel_editor", EDITOR_PATH)
editor = importlib.util.module_from_spec(spec)
spec.loader.exec_module(editor)

STORY_ID = 5923

INTRO = (
    "<p><strong>\"Quỳ xuống ký biên bản nhận tội đi. Đừng để cả vùng Cầu Đất biết anh là thằng ở rể tráo trà bẩn.\"</strong> "
    "Trong đêm mưa lạnh trước kho Mai Trà, Lê Minh Quân bị nhà vợ cũ xé thẻ nhân viên, ném sổ cân lá vào thùng rác và vu cho anh phá hợp đồng xuất khẩu một trăm hai mươi tỷ. "
    "Nhưng họ không biết người đàn ông bị đuổi khỏi cổng ấy đang giữ bản scan sổ cân lá gốc, ảnh niêm phong mẫu lưu, log kho lên men và một bản sao camera nhiệt chưa từng công bố. "
    "Khi tài khoản hợp tác xã bị khóa, streamer vây kín kho, chuyên gia giả đứng ra phủ nhận mẫu trà, Quân mới từng bước mở chuỗi bằng chứng khiến cả gia tộc từng khinh anh phải cúi đầu trước nông hộ Cầu Đất.</p>"
)

REPEATED_BLOCK = re.compile(
    r"<p>Chi tiết ấy được Quân ghi lại ngay trong sổ tay, không phải để làm màu.*?muốn thắng lâu dài thì phải để sự thật có chỗ ở lại sau khi cơn giận đã qua\.</p>",
    flags=re.S,
)

REPLACEMENTS = {
    5939: (
        "<p>Quân không nói thêm. Anh chỉ yêu cầu thư ký hội đồng photo lời khai của Phan Tuấn thành ba bản: một bản cho thanh tra, một bản cho ngân hàng, một bản gửi cho đại diện nông hộ. Lần này, không ai còn được giữ sự thật trong ngăn kéo riêng.</p>"
        "\n<p>Khi Bảo bị đưa ra khỏi phòng, những người từng quay mặt tránh Quân lúc ở kho lần lượt đứng dậy. Không ai vỗ tay. Sự im lặng ấy nặng hơn mọi tiếng reo, vì nó báo rằng cán cân quyền lực trong vùng trà đã đổi bên.</p>"
    ),
    5940: (
        "<p>Đêm đó, Quân ghi vào bảng kiểm một dòng rất ngắn: <em>mẻ đầu tiên đạt vì không ai được phép bỏ qua việc nhỏ</em>. Anh không treo câu ấy lên tường. Anh để nó ở trang cuối sổ vận hành, nơi ngày mai người trực ca sẽ phải ký tên trước khi bật máy.</p>"
        "\n<p>An Nhiên nhìn dòng chữ rồi đóng dấu xác nhận. Không phải lời khen, nhưng dấu mực đỏ ấy khiến cả kho hiểu rằng họ vừa vượt qua cửa ải khó nhất: biến một lời hứa danh dự thành quy trình có thể kiểm tra.</p>"
    ),
    5941: (
        "<p>Sau quyết định phong tỏa, bà Nhã đứng dậy nhưng không bước nổi ra khỏi phòng ngay. Bên dưới sân, nông hộ vẫn cầm những phiếu cân bị sửa. Họ không chửi mắng. Họ chỉ nhìn lên tầng kính, và cái nhìn ấy khiến mọi lời bao biện về \"ơn nghĩa\" rơi xuống như lá khô.</p>"
        "\n<p>Quân gấp bản sao quyết định lại, đặt trước mặt ông Lộc. \"Từ giờ, tiền bồi thường đi qua tài khoản giám sát. Không ai được ký thay nông hộ nữa.\" Ông Lộc cầm tờ giấy bằng cả hai tay. Lần đầu tiên trong nhiều năm, con dấu đỏ không đứng về phía nhà máy.</p>"
    ),
}

CH10_INSERT_AFTER = "Hắn ký tên, rồi ngồi thụp xuống ghế như người vừa bị rút hết xương.</p>"
CH10_ADDITION = (
    "\n<p>Ống kính phóng viên chĩa thẳng vào tờ biên bản. Người dẫn livestream từng đứng trước cổng kho chửi Quân là kẻ tráo trà bẩn giờ phải đọc lại kết luận kiểm nghiệm ngay trên sóng: lô số bảy bị đánh tráo sau khi rời kho, còn chữ ký của Quân bị dùng để che một chuỗi phiếu cân giả.</p>"
    "\n<p>Bảo ngẩng đầu lên, môi run run như muốn xin tắt máy quay. Không ai đáp. Chính hắn từng kéo cả vùng Cầu Đất đến xem Quân bị nhục dưới mưa; hôm nay, hắn phải tự ký từng dòng xác nhận trước mặt những người trồng trà mà hắn đã ép giá nhiều năm.</p>"
)


def fix_content(chapter_id, content):
    if chapter_id in REPLACEMENTS:
        new_content, count = REPEATED_BLOCK.subn(REPLACEMENTS[chapter_id], content)
        if count != 1:
            raise RuntimeError(f"Expected one repeated block in chapter {chapter_id}, found {count}")
        return new_content
    if chapter_id == 5942 and "hắn phải tự ký từng dòng xác nhận" not in content:
        if CH10_INSERT_AFTER not in content:
            raise RuntimeError("Could not find insertion point in chapter 10")
        return content.replace(CH10_INSERT_AFTER, CH10_INSERT_AFTER + CH10_ADDITION, 1)
    return content


def main():
    data = json.loads(BACKUP.read_text(encoding="utf-8"))
    updates = []
    editor.upload_helper()
    try:
        meta = editor.update_story_meta(STORY_ID, intro=INTRO)
        if not meta.get("success"):
            raise RuntimeError(f"Intro update failed: {meta}")
        updates.append({"story_id": STORY_ID, "intro": "updated"})

        for ch in data["chapters"]:
            new_content = fix_content(ch["id"], ch["content"])
            if new_content != ch["content"]:
                res = editor.update_chapter(ch["id"], ch["title"], new_content)
                if not res.get("success"):
                    raise RuntimeError(f"Chapter update failed {ch['id']}: {res}")
                updates.append({"chapter_id": ch["id"], "title": ch["title"]})
    finally:
        editor.remove_helper()

    OUT.write_text(json.dumps({"success": True, "updates": updates}, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"success": True, "updates": updates}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
