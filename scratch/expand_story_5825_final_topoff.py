#!/usr/bin/env python3
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EDITOR_PATH = ROOT / "scratch" / "novel_editor.py"
OUT = ROOT / "scratch" / "story_5825_final_topoff_result.json"

spec = importlib.util.spec_from_file_location("novel_editor", EDITOR_PATH)
editor = importlib.util.module_from_spec(spec)
spec.loader.exec_module(editor)

ADDITIONS = {
    5829: """
<p>Trước khi tắt đèn, Hà chụp lại văn phòng trống. Trong ảnh, ba chiếc ghế nhựa không cùng màu, dây điện lòng thòng dưới bàn, tường còn vết khoan cũ của người thuê trước. Cô gửi ảnh vào nhóm chat mới lập, đặt tên nhóm là <strong>Không Ai Vô Danh</strong>. Minh thả một dấu chấm than. Lan gửi lại ảnh bàn tay dính màu thiết kế. Chẳng có gì giống một khởi đầu hoành tráng, nhưng cả ba đều hiểu họ vừa đặt viên gạch đầu tiên cho thứ mình muốn bảo vệ.</p>
""",
    5831: """
<p>Hôm sau, Hà nhận được một cuộc gọi từ nhân sự cũ ở BlueStar. Người đó không dám làm chứng, chỉ nói nhỏ rằng Phong đã yêu cầu phòng IT rà lại toàn bộ lịch sử truy cập của Hà để tìm lỗi. Không tìm thấy lỗi lớn, họ chuyển sang soi những lần cô gửi file về email cá nhân lúc làm việc đêm. Hà nghe xong, lưng lạnh đi. Những thao tác từng là cách tự cứu deadline giờ có thể bị bẻ thành tội. Cô thêm ngay một mục vào quy trình mới: mọi file làm ngoài giờ phải lưu qua drive công ty có log rõ ràng.</p>
""",
    5832: """
<p>Trong thang máy sau buổi pitch, Lan mới thú nhận cô đã để sẵn một túi giấy trong balo vì nghĩ nếu khách hỏi quá gắt, cô sẽ nôn. Minh cười phá lên, rồi tựa đầu vào vách kính vì chân cũng mềm nhũn. Hà nhìn hai người, tự nhiên bật cười theo. Họ vừa trình bày như một agency trưởng thành, nhưng bên trong vẫn là ba con người đang học cách không bị những căn phòng lớn nuốt mất. Chính sự thật ấy làm chiến thắng sau đó có vị rất khác: không phải phép màu, mà là sống sót qua từng câu hỏi.</p>
""",
    5835: """
<p>Khi về đến văn phòng, cả team không mở champagne. Họ ăn mì ly vì đã quá khuya, đặt chiếc cúp Golden Dragon ở giữa bàn họp như một món đồ hơi lạc lõng. Linh vừa ăn vừa nhìn tên mình trong brochure, cứ vài phút lại chạm tay vào dòng chữ ấy một lần. Hà thấy động tác đó và không nhắc. Có những thứ phải được chạm đi chạm lại mới đủ thật, nhất là với người lần đầu thấy công sức của mình không bị giấu sau tên người khác.</p>
""",
}


def main():
    updates = []
    editor.upload_helper()
    try:
        data = editor.get_story_chapters(5825)
        if not data.get("success"):
            raise RuntimeError(data)
        for chapter in data["chapters"]:
            chapter_id = chapter["id"]
            if chapter_id not in ADDITIONS:
                continue
            marker = f"story_5825_final_topoff_{chapter_id}"
            content = chapter["content"]
            if marker not in content:
                content = content.rstrip() + f"\n<!-- {marker} -->\n" + ADDITIONS[chapter_id].strip()
            res = editor.update_chapter(chapter_id, chapter["title"], content)
            if not res.get("success"):
                raise RuntimeError(f"Chapter update failed {chapter_id}: {res}")
            updates.append({"chapter_id": chapter_id})
    finally:
        editor.remove_helper()
    OUT.write_text(json.dumps({"success": True, "updates": updates}, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"success": True, "updates": updates}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
