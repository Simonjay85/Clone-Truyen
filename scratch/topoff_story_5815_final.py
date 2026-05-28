import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("novel_editor", ROOT / "scratch" / "novel_editor.py")
editor = importlib.util.module_from_spec(spec)
spec.loader.exec_module(editor)

STORY_ID = 5815

ADDITIONS = {
    5818: """
Trước khi ngủ, Bảo lấy tờ vé số bà cụ cho ra nhìn dưới ánh đèn. Nó không trúng, chắc chắn không trúng, nhưng cậu vẫn cất kỹ như một tấm giấy chứng nhận rằng hôm nay mình được ai đó nhớ tới. Ông Phước thấy vậy chỉ cười, lấy dây thun buộc lại cuốn sổ nhỏ cho cậu. "Mai mốt con có nhiều thứ quý hơn tiền trúng số," ông nói. "Nhưng tối nay, cứ giữ nó đi."
""",
    5819: """
Tối ấy, Bảo tự nguyện rửa nồi lâu hơn mọi ngày. Cậu không nói cảm ơn ông Phước, vì chữ ấy với cậu lúc đó vẫn ngượng. Nhưng cậu để phần chè chuối ngon nhất trong cái chén sứt cho ông, đặt thêm cái muỗng sạch bên cạnh. Ông Phước nhận ra, không nói gì. Có những đứa trẻ đáp lại tình thương bằng cách vụng về nhất, và người lớn tử tế phải đủ tinh để không làm chúng xấu hổ.
""",
    5820: """
Vài tuần sau, Bảo đọc được dòng chữ trên toa thuốc của ông Phước. Cậu phát hiện ông uống sai giờ, liền lấy bút màu kẻ lại lịch uống thuốc dán lên tường. Ông Phước nhìn bảng chữ méo mà bật cười: "Học chữ để quản ông hả?" Bảo nghiêm mặt gật đầu. Lần đầu tiên chữ nghĩa không chỉ mở đường cho cậu, mà còn giúp cậu chăm lại người đã chăm mình.
""",
    5821: """
Sau buổi đọc bài, cô chủ nhiệm đưa cho Bảo một phiếu đăng ký thư viện miễn phí. Cậu cầm tấm thẻ nhỏ, thấy tên mình in trên đó thì cứ nhìn mãi. Tối về, cậu khoe với từng khách rằng mình được mượn sách đem về. Ông Phước đặt thẻ vào túi nilon chống ướt, dặn: "Sách cũng như chè, nhận rồi phải giữ cho sạch để người sau còn dùng."
""",
    5822: """
Ngày ông Phước xuất viện, cả góc đường góp tiền mua cho ông một chiếc ghế có tựa lưng. Bảo đặt ghế cạnh xe chè như đặt ngai vàng cho một vị vua nghèo. Ông ngồi xuống, cười đến nheo mắt, rồi bắt mọi người ăn chè miễn phí vì "ông còn sống về lại đây là lời rồi." Không ai chịu miễn phí cả. Họ bỏ tiền vào hộp, người ít người nhiều, như trả cho những đêm mình từng được ông giữ ấm.
""",
    5823: """
Một chiều, Bảo đưa ông Phước tới xem mặt bằng quán chè tương lai. Nơi đó nhỏ, tường còn bong, nền xi măng nứt, nhưng có mái che rộng và đủ chỗ đặt chiếc xe cũ. Ông đi chậm quanh căn phòng, sờ tay lên bức tường rồi hỏi: "Con chắc không?" Bảo đáp: "Chắc. Nhưng con muốn ông đặt tên." Ông Phước nghĩ rất lâu, cuối cùng nói: "Đặt tên gì cũng được, miễn người đói bước vào không thấy ngại."

Vài ngày sau, Bảo treo bản vẽ quán lên vách phòng trọ. Ông Phước cứ nằm trên giường nhìn nó, thỉnh thoảng góp ý chỗ để nồi, chỗ rửa chén, chỗ treo bảng. Những góp ý nhỏ ấy làm ông vui như mình còn đang xây một đời mới cùng Bảo. Cậu hiểu, đôi khi người già không sợ chết bằng sợ bị gạt ra ngoài những việc đang tiếp diễn. Vì vậy cậu hỏi ông mọi thứ, từ màu sơn đến loại ghế. Mỗi câu hỏi là một cách nói: ông vẫn ở trong tương lai của con.
""",
}


def main():
    editor.upload_helper()
    try:
        payload = editor.get_story_chapters(STORY_ID)
        chapters = payload["chapters"] if isinstance(payload, dict) else payload
        for chapter in chapters:
            cid = int(chapter["id"])
            addition = ADDITIONS.get(cid)
            if addition:
                editor.update_chapter(cid, chapter["title"], (chapter["content"] or "").rstrip() + "\n\n" + addition.strip())
                print(cid, chapter["title"])
    finally:
        editor.remove_helper()


if __name__ == "__main__":
    main()
