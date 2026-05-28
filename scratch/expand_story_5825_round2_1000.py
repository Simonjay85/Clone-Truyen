#!/usr/bin/env python3
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EDITOR_PATH = ROOT / "scratch" / "novel_editor.py"
OUT = ROOT / "scratch" / "story_5825_expand_round2_result.json"

spec = importlib.util.spec_from_file_location("novel_editor", EDITOR_PATH)
editor = importlib.util.module_from_spec(spec)
spec.loader.exec_module(editor)

ADDITIONS = {
    5827: """
<p>Sáu giờ sáng, Hà gửi một email cuối cùng cho Phong, không phải để van xin mà để đóng dấu thời gian. Cô liệt kê từng file, từng ngày chỉnh sửa, từng cuộc họp có mặt khách hàng. Ở cuối mail, cô viết: <em>Nếu anh tiếp tục dùng campaign này như thành quả cá nhân, tôi sẽ buộc phải bảo vệ quyền được ghi nhận của mình bằng mọi cách hợp pháp.</em></p>
<p>Phong trả lời sau bảy phút: <em>Đừng tự hủy sự nghiệp vì sĩ diện. Không agency nào muốn tuyển một creative thích gây chuyện.</em> Hà đọc câu đó ba lần. Lần thứ nhất cô tức đến run tay. Lần thứ hai cô thấy lạnh. Lần thứ ba cô chụp màn hình, lưu vào thư mục bằng chứng. Phong vẫn không hiểu: chính thói quen đe dọa người yếu hơn mới là thứ giúp cô nhìn rõ mình phải rời khỏi cái ngành cũ mà anh ta đại diện.</p>
<p>Khi trời sáng hẳn, Hà mở rèm cửa. Căn phòng trọ vẫn chật, quần áo vẫn treo trên dây, laptop vẫn nóng ran sau một đêm thức trắng. Nhưng trên màn hình, những file bằng chứng đã được sắp thành từng mốc. Cô đặt tên thư mục cuối cùng là <strong>Khong_Bi_Xoa_Ten</strong>. Cái tên nghe hơi trẻ con, nhưng với cô, đó là lời tuyên thệ đầu tiên.</p>
""",
    5828: """
<p>Hà thử đăng một bài rất ngắn trên trang cá nhân: <em>Có những ý tưởng không tự nhiên thuộc về người cầm micro nhận giải.</em> Cô không nhắc tên Phong, không nhắc BlueStar. Vậy mà dưới bài viết, vài tài khoản lạ lập tức vào mỉa mai. Một người viết: <em>Làm thuê mà tưởng mình là chủ thương hiệu.</em> Người khác hỏi: <em>Có bằng chứng thì kiện đi, đừng khóc online.</em></p>
<p>Cô xóa app Facebook khỏi điện thoại trong ba tiếng, rồi lại cài lại vì cần theo dõi phản ứng. Chính vòng lặp đó làm cô kiệt sức: muốn im để giữ bình tĩnh, nhưng càng im càng bị người khác kể thay câu chuyện của mình. Minh thấy cô nhìn màn hình đến đỏ mắt, liền kéo laptop về phía mình. \"Từ giờ mọi bằng chứng đưa vào file, mọi cảm xúc đưa vào brief. Cậu không thắng được đám đông bằng cách đọc từng comment đâu.\"</p>
<p>Câu nói của Minh giúp Hà dừng lại. Cô nhận ra mình không chỉ cần chứng minh Phong sai. Cô cần xây một nơi mà những người trẻ sau này không phải ôm điện thoại đọc từng lời nhục mạ để tự hỏi liệu công sức của mình có thật hay không. Ý nghĩ đó biến cơn giận cá nhân thành một mục tiêu lớn hơn, và chính mục tiêu ấy khiến cô đủ sức ký giấy thành lập công ty vào sáng hôm sau.</p>
""",
    5829: """
<p>Ngày treo bảng tên công ty, Hà không làm lễ khai trương. Cô mua ba ly cà phê sữa đá, một ổ bánh mì chia ba, rồi cùng Minh và Lan đứng nhìn tấm bảng mica nhỏ mới bắt vít lên cửa. Chữ <strong>Thanh Hà Creative</strong> hơi lệch sang trái vì người thợ khoan vội, nhưng cả ba không ai muốn sửa ngay. Nó giống công ty của họ: chưa hoàn hảo, nhưng có thật.</p>
<p>Khó khăn đầu tiên không phải creative mà là hóa đơn. Tiền thuê văn phòng đến trước tiền khách thanh toán. Phí ứng trước sản xuất làm tài khoản công ty tụt xuống còn sáu triệu. Minh phải dùng thẻ tín dụng cá nhân đặt vé ra Huế, còn Lan mang máy ảnh của anh trai đi chụp vì chưa dám thuê ekip. Hà ghi tất cả vào sổ nợ nội bộ, dưới mỗi dòng đều có chữ ký của mình. Cô không muốn sự hy sinh của bạn bè biến thành một kiểu vô danh khác.</p>
<p>Buổi tối trước ngày đi Huế, Hà ngồi một mình trong văn phòng mới, nghe tiếng nước nhỏ từ máy lạnh xuống cái xô nhựa. Cô thấy sợ. Nếu campaign tiệm bún bò thất bại, cô không chỉ mất tiền; cô sẽ kéo Minh và Lan vào một cuộc nổi loạn lãng mạn nhưng ngu ngốc. Nhưng rồi cô nhìn ba quy tắc trên tường. Người khác từng dùng nỗi sợ mất việc để buộc cô im. Cô không muốn vừa mở công ty đã để nỗi sợ ấy điều hành mình.</p>
""",
    5830: """
<p>Sau bài báo đầu tiên, một nhãn hàng gia vị nhỏ nhắn tin hỏi báo giá, rồi biến mất khi nghe con số mười hai triệu. Một chủ quán khác xin toàn bộ ý tưởng trước để \"về bàn với gia đình\". Minh nổi cáu, muốn bắt khách ký phí tư vấn từ đầu. Hà đồng ý, nhưng cô cũng hiểu thị trường mà họ đang bước vào: khách nhỏ sợ bị lừa, agency nhỏ sợ bị quỵt, còn ý tưởng thì luôn nằm ở giữa như thứ dễ bị lấy nhất.</p>
<p>Cô sửa lại quy trình nhận brief. Từ nay buổi tư vấn đầu tiên chỉ nói về vấn đề kinh doanh, không trao concept hoàn chỉnh nếu chưa có phí giữ chỗ. Điều khoản ấy khiến vài khách bỏ đi, nhưng cũng khiến những người ở lại nghiêm túc hơn. Hà học rất nhanh rằng bảo vệ ý tưởng không chỉ là đòi credit trên sân khấu; nó bắt đầu từ việc không phát miễn phí công sức của team trong những cuộc gặp mơ hồ.</p>
<p>Campaign tiệm bún bò vì thế trở thành bài học vận hành đầu tiên. Họ không kiếm được nhiều tiền từ nó, nhưng nó dạy Thanh Hà Creative cách đo đơn, cách kiểm chất lượng, cách từ chối tăng trưởng nếu sản phẩm không chịu nổi. Đêm tổng kết, Lan nói đùa: \"Case này nhỏ mà hành mình như brand quốc gia.\" Hà cười, rồi ghi vào sổ: <em>Khách nhỏ không có nghĩa là tiêu chuẩn nhỏ.</em></p>
""",
    5831: """
<p>Thư luật sư của BlueStar làm cả văn phòng mất ngủ ba đêm. Minh gọi ba người quen xin báo giá tư vấn pháp lý, mỗi báo giá đều khiến mặt anh tối đi. Lan bắt đầu lưu mọi file thiết kế vào hai ổ cứng khác nhau, vì cô sợ một ngày nào đó người ta nói bộ key visual của mình cũng sao chép. Không khí trong văn phòng nhỏ đặc lại, mỗi tiếng thông báo email đều làm mọi người giật mình.</p>
<p>Hà biết mình phải nói thật với team. Cô đặt bản sao thư luật sư lên bàn và nói: \"Nếu ai muốn rút, chị không trách. Công ty mới, tiền ít, lại bị BlueStar dí pháp lý. Ở lại không phải nghĩa vụ.\" Minh nhìn cô như bị xúc phạm. Lan thì kéo ghế ngồi thẳng hơn. \"Em nghỉ chỗ cũ vì bị bắt sửa thiết kế đến sáng rồi sếp nhận hết công,\" Lan nói. \"Nếu chỗ này cũng sợ đến mức bỏ credit, em mới rút.\"</p>
<p>Câu nói ấy khiến Hà thấy cổ họng nghẹn lại. Cô từng nghĩ mình mở agency để cứu tên mình. Đến lúc này, cô hiểu những người ngồi quanh chiếc bàn ọp ẹp kia cũng đang gửi vào công ty một phần danh dự riêng. Nếu cô thua, không chỉ Hà bị gọi là kẻ gây chuyện; tất cả họ sẽ bị chứng minh rằng người làm sáng tạo nhỏ bé tốt nhất nên cúi đầu.</p>
""",
    5832: """
<p>Đêm trước buổi pitch, cả team chạy thử phần trình bày đến lần thứ sáu. Minh cứ đến slide ngân sách là nói quá nhanh. Lan phát hiện màu key visual trên máy chiếu lệch hẳn so với màn hình laptop. Hà bắt cả nhóm dừng lại, tắt hết đèn, rồi hỏi từng người sợ nhất điều gì. Minh sợ khách hỏi năng lực triển khai toàn quốc. Lan sợ bị chê hình ảnh quá đời, không đủ \"premium\". Hà sợ nhất câu hỏi về BlueStar.</p>
<p>Thay vì né, cô đưa nỗi sợ ấy vào slide dự phòng. Slide tên là <strong>Rủi ro và cách kiểm soát</strong>. Trong đó có tranh chấp credit, quản trị file, phê duyệt khách hàng, xử lý khủng hoảng bình luận, ngân sách dự phòng nếu sentiment xấu. Minh nhìn slide, thở dài: \"Không agency nào tự vạch áo như thế trong pitch.\" Hà đáp: \"Vì họ có áo đẹp hơn. Mình chỉ có sự minh bạch.\"</p>
<p>Sáng hôm sau, khi chị Phương hỏi về rủi ro, Hà không còn bị động. Cô mở đúng slide đó. Càng trình bày, cô càng thấy căn phòng thay đổi. Khách hàng không nhìn họ như một agency trẻ đang cố kể chuyện cảm xúc nữa, mà như một đội từng bị đánh vào chỗ đau nhất nên buộc phải xây áo giáp cẩn thận hơn người khác. Chính vết thương cũ, nếu biết xử lý, có thể trở thành năng lực mới.</p>
""",
    5833: """
<p>Đêm đó, Hà không về nhà ngay. Cô ở lại văn phòng cùng Minh rà từng dòng trong bộ hồ sơ năng lực. Có những chỗ đọc lên rất đau: nhân sự chỉ ba người chính thức, mạng lưới sản xuất thuê ngoài, chưa từng chạy campaign ngân sách trên hai tỷ. Minh hỏi có nên viết mềm đi không. Hà lắc đầu. \"Khách lớn sẽ tự biết. Mình giấu thì thành yếu thật.\"</p>
<p>Họ thêm vào sau mỗi điểm yếu một phương án kiểm soát: ít người nên decision nhanh; sản xuất thuê ngoài nhưng có ba nhà cung cấp dự phòng; chưa chạy ngân sách lớn nhưng có quy trình phê duyệt từng mốc và cố vấn media độc lập. Đến ba giờ sáng, bộ hồ sơ không còn giống một bản tự quảng cáo. Nó giống một bản kiểm toán chính mình. Hà đọc xong, lần đầu tiên thấy những vết nứt của công ty không chỉ đáng xấu hổ; chúng là chỗ cần gia cố.</p>
<p>Sáng hôm sau, khách hàng từng tạm hoãn vì sợ rủi ro gọi lại. Họ nói đã đọc bộ hồ sơ mới và muốn gặp thêm một vòng. Minh che điện thoại, há miệng không thành tiếng. Hà chỉ nhắm mắt một giây. Phong đã dùng sự thật nửa vời để đánh họ. Cô dùng sự thật đầy đủ để mở lại cánh cửa.</p>
""",
    5834: """
<p>Trong lúc cả team chuẩn bị váy áo cho lễ trao giải, Hà dành riêng một giờ gọi cho chị Oanh ở Huế. Chị không liên quan gì đến Vinamilk, không có mặt trong đêm trao giải, nhưng với Hà, campaign bún bò là viên gạch đầu tiên. Chị Oanh nghe tin Thanh Hà được đề cử thì cười vang qua điện thoại: \"Rứa là cái văn phòng dột nước của mấy em cũng lên sân khấu lớn rồi hả?\"</p>
<p>Hà kể cho chị nghe về Linh, về credit, về việc vẫn còn sợ khi bước vào Golden Dragon. Chị Oanh im lặng một chút rồi nói: \"Hồi trước chị bán ở chợ, người ta ăn ngon thì khen 'bún Huế', ít ai nhớ tên chị. Từ ngày tụi em làm campaign, khách gọi chị Oanh nhiều hơn gọi tên quán. Chị mới biết tên mình nghe cũng vui.\" Câu nói ấy làm Hà cười rất lâu.</p>
<p>Sau cuộc gọi, Hà thêm một slide vào phần tư liệu nội bộ: ảnh chị Oanh đứng bên nồi nước lèo, bên dưới ghi <em>Khách hàng đầu tiên dạy chúng tôi rằng tên người làm ra giá trị cũng là một phần của giá trị.</em> Slide ấy không trình chiếu ở lễ trao giải. Nó chỉ nằm trong folder công ty, như một mốc nhắc họ không được trở nên hào nhoáng đến mức quên nơi mình bắt đầu.</p>
""",
    5835: """
<p>Sau bài phát biểu, hậu trường trở nên hỗn loạn. Phóng viên muốn phỏng vấn, khách hàng muốn chúc mừng, vài người từng im lặng năm ngoái nay tìm đến bắt tay Hà như thể họ luôn đứng về phía cô. Hà nhận ra điều đó, nhưng không vạch mặt ai. Cô đã quá mệt với việc đòi từng người thừa nhận quá khứ. Tối nay, cô muốn giữ năng lượng cho team mình.</p>
<p>Phong đi ngang qua họ ở cửa ra. Một phóng viên trẻ nhận ra anh ta, hỏi: \"Anh nghĩ sao về phát biểu của chị Hà về việc campaign từng bị gọi dưới tên người khác?\" Mặt Phong thoáng cứng. Anh ta định cười, nhưng khóe miệng không nâng lên nổi. \"Ngành sáng tạo luôn là nỗ lực tập thể,\" anh ta nói. Câu trả lời nghe đúng, nhưng trong hoàn cảnh ấy lại giống một cái áo quá rộng để che một vết bẩn quá rõ.</p>
<p>Lan đứng sau Hà, thì thầm: \"Chị có muốn đáp không?\" Hà lắc đầu. Cô nhìn Phong bước đi, vai hơi khom dưới ánh đèn hành lang. Cú vả mặt lớn nhất không phải là mắng anh ta trước báo chí. Nó là việc từ nay mỗi lần anh ta nói hai chữ tập thể, cả ngành sẽ nhớ đến những cái tên từng bị anh ta xóa khỏi tập thể ấy.</p>
""",
    5836: """
<p>Quy tắc mới cũng khiến Thanh Hà mất một khách hàng. Một thương hiệu thời trang yêu cầu trong hợp đồng rằng mọi ý tưởng trình bày, kể cả không chọn, đều thuộc quyền sử dụng của khách sau buổi pitch. Minh đề nghị đàm phán vì giá trị hợp đồng khá lớn. Hà đọc điều khoản, đặt bút xuống. \"Không ký.\" Cả phòng im lặng, vì ai cũng biết tháng đó dòng tiền không dư dả.</p>
<p>Hà gọi thẳng cho khách, giải thích rằng agency sẵn sàng bán ý tưởng được chọn, nhưng không thể giao toàn bộ phương án chưa mua để khách đem đi triển khai với bên khác. Đầu dây bên kia cười nhạt: \"Agency nhỏ mà nguyên tắc lớn quá.\" Hà đáp rất bình tĩnh: \"Vì agency nhỏ nên càng phải giữ thứ duy nhất mình có.\" Cuộc gọi kết thúc không vui. Hợp đồng mất.</p>
<p>Tối đó, Hà chuyển bảng dòng tiền cho Minh xem. Họ phải hoãn mua máy quay mới, giảm ngân sách trang trí văn phòng, và Hà tự cắt lương founder tháng đó. Không ai thấy quyết định ấy lãng mạn nữa. Nguyên tắc có giá bằng tiền thật. Nhưng chính vì đã trả giá, cả team mới hiểu những dòng quy tắc trên giấy không phải khẩu hiệu để PR sau giải thưởng.</p>
""",
    5837: """
<p>Phong rời đi rồi, Hà mới mở phong bì. Bên trong là bản in case study \"Vị Quê Hương\" đời đầu, góc giấy ố vàng, có vài dòng bút đỏ của cô và một sticky note cũ ghi: <em>Hà xử lý insight mẹ/bữa cơm rất tốt.</em> Nét chữ trên sticky note là của Phong. Hà nhìn nó một lúc lâu, không biết nên cười hay nên thấy buồn.</p>
<p>Cô mang bản giấy vào phòng họp, đặt lên bàn cho team xem. Không phải để khơi lại thù cũ, mà để mọi người hiểu vì sao công ty này đôi khi cứng đầu đến khó chịu. Linh chạm nhẹ vào mép giấy, hỏi: \"Chị có muốn đóng khung không?\" Hà lắc đầu. \"Không. Mình scan nó, lưu vào thư mục đào tạo. Nó không phải chiến lợi phẩm. Nó là bằng chứng về một lỗi hệ thống.\"</p>
<p>Chiều hôm đó, Hà thêm một mục vào buổi onboarding nhân sự mới: mỗi người phải học cách lưu vết ý tưởng của mình, không phải để nghi ngờ đồng đội, mà để tôn trọng quá trình sáng tạo. Cô nói với các bạn trẻ rằng lòng tin không đối lập với giấy tờ. Lòng tin tốt nhất là thứ đủ minh bạch để không ai phải cầu xin được nhớ tên.</p>
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
            marker = f"story_5825_round2_marker_{chapter_id}"
            content = chapter["content"]
            if marker not in content:
                content = content.rstrip() + f"\n<!-- {marker} -->\n" + ADDITIONS[chapter_id].strip()
            res = editor.update_chapter(chapter_id, chapter["title"], content)
            if not res.get("success"):
                raise RuntimeError(f"Chapter update failed {chapter_id}: {res}")
            updates.append({"chapter_id": chapter_id, "title": chapter["title"]})
    finally:
        editor.remove_helper()

    OUT.write_text(json.dumps({"success": True, "updates": updates}, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"success": True, "updates": updates}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
