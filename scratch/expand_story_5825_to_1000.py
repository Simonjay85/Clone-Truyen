#!/usr/bin/env python3
import importlib.util
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EDITOR_PATH = ROOT / "scratch" / "novel_editor.py"
BACKUP = ROOT / "scratch" / "story_5825_before_expand_1000.json"
OUT = ROOT / "scratch" / "story_5825_expand_1000_result.json"

spec = importlib.util.spec_from_file_location("novel_editor", EDITOR_PATH)
editor = importlib.util.module_from_spec(spec)
spec.loader.exec_module(editor)

ADDITIONS = {
    5827: """
<p>Trong folder cũ, Hà còn giữ cả những đoạn chat Phong từng nhắn lúc nửa đêm. <em>"Đoạn insight về bữa cơm nhà rất tốt, sáng mai em viết thành manifesto cho anh."</em> <em>"Voice-over đoạn mẹ chấm nước mắm còn hơi quảng cáo, sửa lại cho đời hơn."</em> Mỗi tin nhắn khi ấy chỉ là yêu cầu công việc. Đêm nay, chúng trở thành vết mực chứng minh có một người đã thức, đã sửa, đã nghĩ, rồi bị xóa khỏi chính thứ mình tạo ra.</p>
<p>Cô mở bản deck trình bày nội bộ cuối cùng. Ở slide số bảy vẫn còn một dòng comment chưa bị xóa: <em>Hà update theo hướng ký ức bữa cơm, không dùng cảnh biển sáo.</em> Tên cô nhỏ, nằm bên lề phải, nhưng đủ làm mắt cô cay lên. Không phải vì nó cứu được cô ngay. Vì trong hàng trăm file đã bị đổi tên, vẫn còn một dấu vết bướng bỉnh chưa chịu biến mất.</p>
<p>Hà chụp màn hình từng thứ, đặt tên file bằng ngày tháng, rồi lưu thêm một bản lên ổ cứng ngoài. Động tác của cô chậm, cẩn thận như người nhặt lại từng mảnh gương sau khi bị đập vỡ. Đến gần sáng, khi tiếng xe rác dưới hẻm vang lên, cô mới nhận ra mình không còn run nữa. Cơn nhục vẫn ở đó, nhưng nó đã đổi hình dạng: từ một vết thương thành một hồ sơ.</p>
""",
    5828: """
<p>Buổi chiều cùng ngày, Hà đến trước tòa nhà BlueStar để lấy đồ cá nhân còn sót lại. Thẻ nhân viên của cô đã bị khóa. Bảo vệ gọi lên lễ tân, rồi nhìn cô bằng ánh mắt ái ngại. Một thùng carton được mang xuống: cốc uống nước, vài cuốn sách marketing, chiếc áo khoác mỏng và một tấm ảnh team chụp ở Phú Quốc. Trong ảnh, Hà đứng mép ngoài, còn Phong đứng giữa, tay đặt lên vai khách hàng như thể mọi thứ đã thuộc về anh ta từ đầu.</p>
<p>Cô ôm thùng đồ bước ra khỏi sảnh đúng lúc hai nhân viên cũ đi ngang. Họ nhìn thấy cô, rồi lập tức nhìn sang chỗ khác. Không ai ác ý ra mặt, nhưng chính sự né tránh ấy khiến Hà thấy lạnh. Trong ngành sáng tạo, người ta nói rất nhiều về can đảm, phá vỡ giới hạn, dám khác biệt. Vậy mà khi cần nói một câu "tôi có thấy cô ấy làm", ai cũng bận giữ ghế của mình.</p>
""",
    5830: """
<p>Khi lượng đơn tăng đột ngột, chị Oanh muốn chạy thêm quảng cáo ngay. Hà từ chối tăng ngân sách trong hai ngày đầu, yêu cầu bếp thử đóng gói thêm ba mươi hộp rồi gửi đi các quận xa nhất trước. Minh bảo cô quá kỹ. Hà chỉ đưa anh xem ảnh một hộp bún bị đổ nước dùng do đóng nắp chưa chặt. \"Nếu lỗi này lan ra, toàn bộ cảm xúc nhớ nhà biến thành trò lừa đảo,\" cô nói. \"Mình không bán hoài niệm bằng một cái nắp nhựa lỏng.\"</p>
<p>Chính sự khó tính ấy khiến chị Oanh tin cô hơn. Tối hôm đó, chị gửi cho Hà một đoạn ghi âm. Trong đó, mẹ chị ở Huế nói giọng run run: \"Con bán được thì tốt, nhưng đừng làm mất mùi nhà mình.\" Hà nghe đi nghe lại câu ấy, rồi đổi toàn bộ caption ngày hôm sau. Không còn nhấn vào sold out hay viral. Dòng chính chỉ còn: <em>Gửi đi xa, nhưng giữ đúng mùi bếp cũ.</em></p>
""",
    5833: """
<p>Sau cuộc gọi, Phong không dừng ở lời đe dọa. Sáng hôm sau, một khách hàng đang đàm phán với Thanh Hà gửi email xin tạm hoãn vì \"cần rà soát rủi ro truyền thông\". Minh tra được BlueStar vừa gửi cho họ một bản so sánh năng lực, trong đó gạch đỏ từng điểm yếu của agency non trẻ: ít nhân sự, chưa có quy trình kiểm soát khủng hoảng, founder đang có tranh chấp cá nhân với sếp cũ.</p>
<p>Hà đọc bản so sánh, không thể phủ nhận tất cả. Đúng là họ ít người. Đúng là họ chưa có phòng pháp chế riêng. Đúng là văn phòng vẫn phải dùng máy in thuê theo tháng. Cú đánh của Phong độc ở chỗ anh ta trộn lời bẩn với vài sự thật khó cãi, khiến khách hàng không cần ghét Hà vẫn có lý do để sợ.</p>
<p>Chiều đó, Hà gọi cả team họp. Cô không hô khẩu hiệu. Cô viết lên bảng ba lỗ hổng Phong chỉ ra, rồi phân từng việc: Minh xây checklist khủng hoảng, Lan chuẩn hóa quy trình lưu file, Hà làm bộ hồ sơ năng lực có case thật và cách xử lý rủi ro thật. \"Mình không thắng bằng cách nói hắn xấu,\" cô nói. \"Mình thắng bằng cách làm cho những điểm hắn dùng để đánh mình không còn đánh được nữa.\"</p>
""",
    5834: """
<p>Trước khi rời văn phòng, Hà mở lại bản ghi âm buổi brainstorm đầu tiên của chiến dịch. Trong file, giọng Linh nhỏ đến mức gần như bị tiếng máy lạnh nuốt mất. Cô bé nói câu insight rồi lập tức tự phủ nhận: \"Chắc em nói linh tinh thôi.\" Hà nghe đến đó thì dừng lại. Nếu hôm ấy cô cũng bỏ qua như bao trưởng nhóm bận rộn khác, campaign có lẽ vẫn chạy được, nhưng nó sẽ mất phần thật nhất.</p>
<p>Cô cắt đoạn ghi âm ấy lưu riêng vào thư mục case study, không phải để khoe intern ngây thơ, mà để nhắc ban giám khảo thấy ý tưởng được sinh ra như thế nào: từ một câu nói run, một ký ức nhà nghèo, một người đủ kiên nhẫn nghe đến cuối. Với Hà, credit không phải phần chữ nhỏ sau cùng. Credit là cách truy ngược lại khoảnh khắc một ý tưởng bắt đầu có tim.</p>
""",
    5836: """
<p>Không phải ai trong công ty cũng quen ngay với quy tắc mới. Có một buổi, một senior copywriter khó chịu vì phải ghi tên intern vào biên bản sau khi intern chỉ sửa một câu headline. Anh ta nói nửa đùa nửa thật: \"Thế này sau này ai cũng đòi phần, loạn mất.\" Hà không mắng. Cô yêu cầu cả phòng mở lại ba phiên bản headline. Bản đầu nghe như quảng cáo ngân hàng. Bản thứ hai đúng ý nhưng khô. Bản intern sửa chỉ đổi một chữ, nhưng khiến câu nói có hơi người.</p>
<p>\"Đóng góp không phải lúc nào cũng dài,\" Hà nói. \"Có khi nó là một chữ đặt đúng chỗ. Nếu chữ đó làm campaign sống, người đặt nó phải được ghi nhận.\" Từ hôm ấy, senior copywriter kia vẫn hay càu nhàu, nhưng anh là người đầu tiên nhắc team điền credit trước khi gửi file cho khách. Văn hóa không đổi bằng bài diễn văn. Nó đổi bằng những lần khó chịu được xử lý công bằng.</p>
""",
}


def word_count(html):
    return len(re.findall(r"\w+", re.sub(r"<[^>]+>", " ", html), flags=re.UNICODE))


def main():
    data = json.loads(BACKUP.read_text(encoding="utf-8"))
    updates = []
    editor.upload_helper()
    try:
        for chapter in data["chapters"]:
            chapter_id = chapter["id"]
            content = chapter["content"]
            if chapter_id not in ADDITIONS:
                continue
            marker = "story_5825_expand_marker"
            if marker not in content:
                content = content.rstrip() + f'\n<!-- {marker}_{chapter_id} -->\n' + ADDITIONS[chapter_id].strip()
            res = editor.update_chapter(chapter_id, chapter["title"], content)
            if not res.get("success"):
                raise RuntimeError(f"Chapter update failed {chapter_id}: {res}")
            updates.append({"chapter_id": chapter_id, "words_after_local": word_count(content)})
    finally:
        editor.remove_helper()

    OUT.write_text(json.dumps({"success": True, "updates": updates}, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"success": True, "updates": updates}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
