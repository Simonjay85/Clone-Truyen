import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("novel_editor", ROOT / "scratch" / "novel_editor.py")
editor = importlib.util.module_from_spec(spec)
spec.loader.exec_module(editor)

STORY_ID = 5780

ADDITIONS = {
    5782: """
Trước khi hết ca, Minh Đức đi một vòng qua phòng hậu phẫu. Người phụ nữ vừa mổ còn mê, cậu con trai ngồi bên ngoài ôm túi thuốc như ôm vật cứu mạng. Cậu đứng dậy khi thấy ông, lúng túng hỏi có cần mua thêm gì không. Minh Đức chỉ vào tờ hướng dẫn chăm sóc sau mổ, đọc từng mục với cậu: sốt bao nhiêu phải báo, đau thế nào là bất thường, ăn uống ra sao. Ông nói chậm vì biết người nhà sau cơn sợ thường nghe mà không giữ được gì trong đầu.

Ở cuối hành lang, hai bác sĩ nội trú nhìn cảnh ấy. Một người thì thầm rằng thầy Đức làm vậy mất thời gian quá, bệnh viện đông thì ai cũng giải thích kỹ sao nổi. Minh Đức nghe thấy nhưng không quay lại. Khi đi ngang qua họ, ông chỉ nói: "Mười phút giải thích có thể tiết kiệm một lần cấp cứu lại. Đừng xem sự rõ ràng là xa xỉ." Câu ấy làm hai người im. Với ông, tử tế không phải là nụ cười treo poster, mà là chịu khó nói cho người đang sợ hiểu được chuyện gì xảy ra với thân nhân họ.
""",
    5783: """
Sự cô lập còn len vào cả những việc nhỏ nhất. Hồ sơ ông gửi thường nằm cuối chồng giấy. Mẫu xét nghiệm của bệnh nhân ông phụ trách bị trả lại vì một ô chưa tích, trong khi cùng lỗi ấy ở người khác lại được bỏ qua. Có ngày ông vào phòng mổ mới biết dụng cụ quen dùng đã được chuyển sang ca dịch vụ. Điều dưỡng trẻ xin lỗi rối rít, Minh Đức không trách, nhưng ông ghi lại tất cả vào sổ riêng: ngày, giờ, người chứng kiến, hậu quả nếu có.

Lan hỏi ông ghi làm gì khi chưa định kiện ai. Ông đáp: "Khi người ta muốn biến mình thành kẻ khó chịu vô lý, mình phải giữ lại bằng chứng rằng mình đã chịu đựng những gì." Từ hôm đó, cuốn sổ bìa đen theo ông trong túi áo blouse. Nó không làm ông bớt cô đơn, nhưng giúp ông không nghi ngờ trí nhớ của chính mình. Ở một nơi cái sai được nói bằng giọng tập thể, người còn tỉnh cần một chỗ để ghi sự thật xuống.
""",
    5784: """
Ngày dọn đồ khỏi bệnh viện, Minh Đức chỉ có một thùng carton. Trong thùng là vài cuốn sách phẫu thuật, một cây bút khắc tên hội nghị, ống nghe cũ và khung ảnh khoa ngoại chụp mười năm trước. Ở bức ảnh ấy, Hải còn đứng hàng sau, Khải còn là bác sĩ trẻ cười rất tươi, Lan cầm bó hoa mừng khoa đạt danh hiệu. Minh Đức nhìn bức ảnh, không nỡ vứt. Không phải vì tiếc chức, mà vì tiếc những người từng tốt trước khi học cách thỏa hiệp.

Khi ông bước qua cổng, bác bảo vệ già chạy theo đưa một chai nước. "Bác sĩ Đức, vợ tôi năm đó nhờ bác sĩ mà sống. Tôi không biết chuyện trong kia đúng sai sao, nhưng tôi nhớ ơn." Minh Đức nhận chai nước, cổ họng nghẹn. Một bệnh viện có thể tước bảng tên của ông khỏi cửa phòng, nhưng không thể xóa ông khỏi ký ức những người từng được cứu.
""",
    5785: """
Để bệnh nhân tin viện nhỏ, Minh Đức làm một việc mà nhiều người chê là cực đoan: sau mỗi ca mổ, viện gọi điện theo dõi ba lần trong tuần đầu. Lan lập bảng hỏi ngắn: đau, sốt, vết mổ, ăn uống, tâm trạng, thắc mắc viện phí. Ban đầu nhân viên than mất công, nhưng rồi họ phát hiện nhiều biến chứng được bắt sớm, nhiều hiểu lầm được gỡ trước khi thành bức xúc. Một bà cụ tưởng phải kiêng tắm cả tháng, một chú tài xế uống thuốc sai giờ, một cô công nhân giấu chuyện vết mổ rỉ dịch vì sợ tốn tiền tái khám.

Mỗi tối, Minh Đức đọc báo cáo cuộc gọi. Có dòng khiến ông dừng rất lâu: "Bệnh nhân nói lần đầu có bệnh viện gọi hỏi mình có ổn không sau khi đã thu tiền." Ông in dòng ấy, dán trong phòng họp. Không phải để khoe, mà để nhắc cả viện rằng sự khác biệt không nằm ở lời hứa lớn. Nó nằm ở cuộc gọi nhỏ sau khi người bệnh đã ra khỏi cửa.
""",
    5786: """
Trong lúc bị tấn công, Minh Đức cũng phải học cách bảo vệ nhân viên. Một điều dưỡng mới hoảng đến khóc vì bị người lạ nhắn tin chửi, nói cô tiếp tay cho viện lừa đảo. Ông gọi cả đội họp, không nói những câu rỗng như "phải mạnh mẽ lên". Ông hướng dẫn họ lưu bằng chứng, không tự tranh cãi trên mạng, chuyển mọi đe dọa cho pháp lý, và quan trọng nhất là không để cơn giận trút xuống bệnh nhân thật đang trước mặt.

"Người bẩn muốn kéo mình vào bùn," ông nói. "Nếu mình bước xuống để đánh nhau theo cách của họ, bệnh nhân sẽ là người bị bỏ lại trên bờ." Từ hôm đó, viện lập một kênh xử lý khủng hoảng riêng. Lan phụ trách phản hồi công khai bằng biên bản, hóa đơn, quy trình. Minh Đức phụ trách chuyên môn. Không ai được dùng lời cay độc. Sự sạch sẽ, họ học, cũng cần kỹ thuật để tự vệ.
""",
    5787: """
Luật sư cảnh báo Minh Đức rằng khi hồ sơ bung ra, phía bên kia có thể kiện ngược vì tiết lộ bí mật bệnh viện. Ông ngồi nghe, tay đặt trên tập tài liệu dày, rồi hỏi: "Nếu tôi chỉ gửi cơ quan thanh tra và báo chí dùng dữ liệu đã che thông tin, rủi ro còn bao nhiêu?" Luật sư nói vẫn còn, vì người có quyền thường biết biến quy trình thành mê cung. Minh Đức cười mệt: "Tôi từng mổ ổ bụng dính ruột. Mê cung không đáng sợ bằng để nhiễm trùng lan."

Ông chuẩn bị cho khả năng xấu nhất: ủy quyền điều hành tạm thời cho Lan, lập quỹ lương ba tháng cho nhân viên, sao lưu hồ sơ bệnh án của viện. Ông không lãng mạn hóa cuộc chiến. Người muốn sống sạch mà không chuẩn bị gì sẽ dễ bị nghiền nát rồi trở thành câu chuyện cảnh báo cho người khác. Minh Đức muốn nếu mình ngã, viện vẫn đứng.
""",
    5788: """
Mẹ ông ở lại viện một tuần. Mỗi ngày bà đều quan sát nhân viên rồi góp ý thẳng thừng. Bà bảo cô thu ngân nói nhanh quá làm người quê không hiểu, bảo bảng chỉ dẫn chữ nhỏ, bảo cháo căn tin nấu nhạt như nước mắt. Lan ghi hết, cười nói mẹ thầy còn khó hơn đoàn kiểm tra. Minh Đức lại thấy quý. Những nhận xét ấy đến từ một người bệnh thật, không phải từ phòng họp.

Sau khi mẹ xuất viện, ông cho chỉnh lại bảng chỉ dẫn bằng chữ lớn hơn, thêm bản hướng dẫn bằng hình cho người già, và yêu cầu quầy thu ngân đọc chậm từng khoản với bệnh nhân trên sáu mươi tuổi. Một thay đổi nhỏ, nhưng vài ngày sau có cụ ông nói: "Ở đây già như tôi vẫn hiểu mình trả tiền gì." Minh Đức nhớ lời mẹ: sạch phải đi cùng ấm. Nếu minh bạch mà khiến người yếu thấy mình ngu dốt, đó chưa phải tử tế.
""",
    5789: """
Khi BV Nhân Dân treo bảng mới, nhiều người dân bán tín bán nghi. Một tấm bảng không xóa được nhiều năm hành lang thì thầm. Nhưng thay đổi thật bắt đầu từ vài hành động nhỏ: một điều dưỡng trả lại phong bì và hướng dẫn đóng đúng quầy; một bác sĩ giải thích gói mổ thường không kém an toàn trong trường hợp phù hợp; Khải lập nhóm kiểm tra hồ sơ mổ trì hoãn. Mỗi việc đều bị chống, bị cười, bị nói là làm quá.

Khải nhắn cho Minh Đức: "Giờ em mới hiểu thầy mệt thế nào." Minh Đức trả lời: "Đừng lấy mệt làm lý do dừng. Nhưng cũng đừng lấy đúng làm cớ khinh người chưa dám đúng." Ông biết nếu Khải trở thành một phiên bản cay nghiệt của ông, cậu sẽ nhanh chóng bị cô lập như ông từng bị. Sửa một hệ thống cần lửa, nhưng cũng cần hơi ấm để kéo người còn lưỡng lự quay về.
""",
    5790: """
Viện Minh Đức cũng lập một hội đồng bệnh nhân nhỏ, gồm người từng điều trị, người nhà, đại diện công tác xã hội và một luật sư tình nguyện. Mỗi quý họ ngồi với ban điều hành để nói những điều nhân viên không tự thấy: nhà vệ sinh tầng hai hay hết giấy, giờ hẹn tái khám còn dồn, bác sĩ đôi khi dùng thuật ngữ khó hiểu, bảo vệ chưa hướng dẫn người già rõ ràng. Có góp ý làm nhân viên chạnh lòng, nhưng Minh Đức yêu cầu cảm ơn trước khi giải thích.

"Người ta đã khỏi bệnh còn quay lại góp ý là may cho mình," ông nói. "Nếu họ im lặng rồi đi chỗ khác, mình mới mất." Nhờ hội đồng ấy, viện bớt tự mãn khi được khen trên mạng. Minh Đức sợ nhất ngày mọi người bắt đầu tin mình tử tế sẵn rồi không cần kiểm tra nữa. Một nơi sạch không phải nơi không có bụi, mà là nơi ngày nào cũng chịu quét.
""",
    5791: """
Sau ca trực ấy, Minh Đức viết thêm một dòng vào sổ tay treo trong phòng bác sĩ: "Đừng để bệnh nhân phải dùng phong bì như ngôn ngữ duy nhất để cầu cứu." Dòng chữ nhanh chóng được chụp lại, nhưng ông không quan tâm chuyện nó có lan không. Điều ông quan tâm là sáng hôm sau, bác sĩ trẻ trực cùng ông tự đề xuất làm tờ hướng dẫn cho người nhà cấp cứu, giải thích ngay từ cửa rằng thứ cần chuẩn bị là giấy tờ, số điện thoại, thông tin bệnh nền, không phải tiền lót tay.

Minh Đức ký duyệt bản hướng dẫn, rồi yêu cầu in bằng chữ lớn đặt ở phòng cấp cứu. Ông biết một đêm đẹp không đủ đổi đời. Nhưng mỗi quy trình đúng sinh ra từ một tình huống thật sẽ làm cái đúng dễ lặp lại hơn. Khi cái đúng không còn phụ thuộc vào một người hùng mệt mỏi, nó mới có cơ hội sống lâu hơn người đã khởi xướng.
""",
}


def main():
    editor.upload_helper()
    try:
        payload = editor.get_story_chapters(STORY_ID)
        chapters = payload["chapters"] if isinstance(payload, dict) else payload
        updates = []
        for chapter in chapters:
            cid = int(chapter["id"])
            addition = ADDITIONS.get(cid)
            if not addition:
                continue
            editor.update_chapter(cid, chapter["title"], (chapter["content"] or "").rstrip() + "\n\n" + addition.strip())
            updates.append({"chapter_id": cid, "title": chapter["title"]})
    finally:
        editor.remove_helper()
    out = ROOT / "scratch" / "story_5780_topoff_result.json"
    out.write_text(json.dumps(updates, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(updates, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
