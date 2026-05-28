#!/usr/bin/env python3
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EDITOR_PATH = ROOT / "scratch" / "novel_editor.py"
OUT = ROOT / "scratch" / "story_5803_final_topoff_result.json"

spec = importlib.util.spec_from_file_location("novel_editor", EDITOR_PATH)
editor = importlib.util.module_from_spec(spec)
spec.loader.exec_module(editor)

ADDITIONS = {
    5805: "<p>Nhiều năm sau, khi đứng trước học sinh vùng cao, Mai thường bắt đầu bằng chính buổi chiều ấy. Cô không kể để các em sợ người lạ đến mức đóng cửa với thế giới, mà để các em học cách hỏi thêm một câu: đi đâu, với ai, địa chỉ nào, ai xác nhận. Nếu ngày đó có một người lớn hỏi kỹ hơn, có lẽ chiếc xe máy đã không rời bản dễ dàng như vậy.</p>",
    5807: "<p>Buổi tối đầu tiên ở đồn, Mai được cho gọi điện về nhà. Khi nghe tiếng mẹ, cô không nói nổi câu nào. Mẹ cô ở đầu dây bên kia cũng chỉ khóc. Người cán bộ cầm máy giúp, nói chậm rãi rằng con còn sống, đang được chăm sóc, sáng mai sẽ có người đưa gia đình xuống. Mai nghe hai chữ còn sống, lần đầu tiên hiểu sống sót không phải kết thúc câu chuyện. Nó chỉ là điểm bắt đầu để quay lại nhận diện bóng tối vừa đi qua.</p>",
    5808: "<p>Mai cũng phải học lại cách ở trong chính ngôi nhà của mình. Những vật quen thuộc đôi khi trở nên lạ: tiếng then cửa, mùi áo khoác ẩm, ánh đèn xe máy quét qua vách gỗ. Mẹ cô ban đầu muốn cất hết những thứ làm con giật mình, nhưng cô giáo Thảo khuyên gia đình không nên biến cả nhà thành nơi né tránh. Thay vào đó, họ tập gọi tên từng nỗi sợ. Đây là tiếng then nhà mình. Đây là xe của chú họ. Đây là khói bếp, không phải căn phòng kia.</p>",
    5809: "<p>Càng học, Mai càng hiểu việc trở về trường không chỉ để lấy điểm. Mỗi ngày cô ngồi trong lớp là một lần phủ nhận lời người ta từng gán cho cô: rằng trẻ bị bán coi như hỏng đời, rằng con gái vùng cao chỉ cần biết làm nương rồi lấy chồng. Cô không nói những câu lớn lao ấy thành lời. Cô chỉ làm bài, đi học đúng giờ, trả sách thư viện sạch sẽ và sống như thể tương lai vẫn còn quyền gọi tên mình.</p>",
    5813: """
<p>Sau khi bà mất, Mai mơ thấy bà nhiều lần. Trong mơ, bà không nói về cái chết. Bà ngồi thêu trước hiên, hỏi Mai hôm nay đã buộc được sợi chỉ nào chưa. Ban đầu Mai tỉnh dậy là khóc. Sau này, cô hiểu đó không phải lời giục phải cứu hết mọi người, mà là lời nhắc mỗi việc nhỏ đều có nghĩa: một buổi tuyên truyền, một biểu mẫu dễ hiểu, một cuộc gọi kịp lúc, một câu nói rằng người bị hại không có lỗi.</p>
<p>Mai đem câu chuyện con hổ vào tài liệu tập huấn, nhưng cô đổi kết một chút. Con hổ không chỉ tự thoát khỏi bẫy rồi biến mất vào rừng. Nó quay lại cào đứt những sợi dây khác, đánh dấu những hố bẫy bằng mùi của mình để hổ con tránh xa. Bà Páo mà nghe chắc sẽ cười, bảo cháu gái học luật nên kể chuyện cũng nhiều điều khoản hơn ngày xưa. Nhưng Mai tin bà sẽ thích cái kết ấy.</p>
""",
}


def main():
    updates = []
    editor.upload_helper()
    try:
        data = editor.get_story_chapters(5803)
        if not data.get("success"):
            raise RuntimeError(data)
        for chapter in data["chapters"]:
            chapter_id = chapter["id"]
            if chapter_id not in ADDITIONS:
                continue
            marker = f"story_5803_final_topoff_{chapter_id}"
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
