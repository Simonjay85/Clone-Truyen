#!/usr/bin/env python3
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EDITOR_PATH = ROOT / "scratch" / "novel_editor.py"
OUT = ROOT / "scratch" / "story_5803_topoff_1000_result.json"

spec = importlib.util.spec_from_file_location("novel_editor", EDITOR_PATH)
editor = importlib.util.module_from_spec(spec)
spec.loader.exec_module(editor)

ADDITIONS = {
    5805: """
<p>Trước khi đi, Mai còn quay lại nhìn mái nhà mình một lần. Mẹ đứng ở hiên, tay lau vào vạt áo, miệng dặn xuống thành phố phải nghe lời người lớn. Bà ngoại không dặn nữa, chỉ nhìn rất lâu, cái nhìn khiến Mai thấy hơi ngại nên cúi xuống chỉnh quai dép. Nếu lúc đó có ai hỏi cô sợ không, cô sẽ nói không. Trẻ con thường không biết gọi tên nỗi sợ khi nó mặc áo đẹp và cầm kẹo ngọt.</p>
<p>Trên đường, người phụ nữ hỏi Mai thích ăn gì, có muốn mua áo mới không, có biết dùng điện thoại không. Những câu hỏi ấy làm Mai bối rối nhưng cũng khiến cô thấy mình được quan tâm. Ở bản, người lớn bận nương, bận em nhỏ, ít ai hỏi một đứa bé muốn gì. Sau này khi học luật, Mai mới hiểu nhiều kẻ lừa đảo không bắt đầu bằng bạo lực. Chúng bắt đầu bằng cách khiến đứa trẻ nghèo cảm thấy lần đầu tiên mình được chọn.</p>
<p>Khi chiếc xe rẽ khỏi con đường quen, Mai lấy gói xôi mẹ nắm ra ăn. Hạt xôi đã nguội, dính vào tay. Người phụ nữ bảo để dành lát nữa, xuống nơi làm sẽ có cơm ngon hơn. Mai ngoan ngoãn gói lại. Cái ngoan ấy nhiều năm sau vẫn làm cô đau. Không phải vì cô có lỗi, mà vì cô biết bao nhiêu đứa trẻ được dạy phải ngoan với người lớn, trong khi không ai dạy các em cách nghi ngờ một lời hứa quá ngọt.</p>
""",
    5806: """
<p>Mai bắt đầu đếm ngày bằng vết cào nhỏ sau tấm chiếu. Mỗi sáng còn sống, cô dùng móng tay rạch một đường lên tường. Đến khi vết rạch nhiều quá không đếm nổi, chị Mỷ lấy than bếp chấm thành từng cụm năm. \"Đếm để biết mình vẫn còn ở đây,\" chị nói. \"Đừng để họ biến mình thành đồ vật.\" Câu ấy làm Mai nhớ rất lâu. Người bị giam không chỉ mất tự do; họ bị bắt quên rằng mình từng có ngày sinh, có tên, có đường về.</p>
<p>Có một lần, người phụ nữ mặt lạnh gọi sai tên Mai thành tên một cô gái khác. Mai nhìn bà ta, bất ngờ nói rất rõ bằng tiếng H'Mông: \"Tôi tên Vàng Thị Mai.\" Bà ta tát cô một cái, không mạnh đến mức ngã nhưng đủ làm tai ù đi. Đêm đó, chị Mỷ chườm khăn ướt lên má cô và thì thầm: \"Nhớ lấy cảm giác này. Một ngày nào đó, khi người ta hỏi vì sao em muốn kiện bọn chúng, em kể rằng ngay cả tên mình em cũng phải giữ bằng máu.\"</p>
<p>Từ hôm ấy, mỗi tối trước khi ngủ, bốn cô gái lần lượt nói tên mình. Vàng Thị Mai. Giàng Thị Mỷ. Lầu Thị Súa. Mùa Thị Lử. Nói nhỏ thôi, chỉ đủ để nhau nghe. Trong căn phòng khóa ngoài, nghi thức ấy giống một phiên điểm danh của những linh hồn chưa chịu biến mất.</p>
""",
    5807: """
<p>Khi người chiến sĩ biên phòng khoác áo mưa lên vai Mai, cô giật bắn vì tưởng bị kéo lại. Anh lập tức lùi một bước, giơ hai tay ra cho cô thấy mình không giữ cô. Cử chỉ nhỏ ấy cứu Mai khỏi một cơn hoảng loạn. Sau này, khi làm luật sư, cô luôn nhắc cán bộ trẻ: với nạn nhân vừa thoát khỏi khống chế, đừng vội nắm tay, đừng đứng chặn cửa, đừng hỏi dồn. Muốn lấy lời khai, trước hết phải trả lại cho họ cảm giác được lựa chọn.</p>
<p>Trong phòng y tế của đồn, Mai ăn bát cháo đầu tiên sau ba ngày. Tay cô run đến mức làm rơi thìa. Một nữ quân y ngồi cạnh, không giục. Cô ấy chỉ đẩy bát lại gần và nói bằng tiếng Kinh chậm rãi: \"Ăn được miếng nào hay miếng đó.\" Mai không hiểu hết câu, nhưng hiểu ánh mắt. Không thương hại. Không ghê sợ. Chỉ kiên nhẫn. Nhiều năm sau, cô vẫn nhớ khuôn mặt người nữ quân y ấy rõ hơn khuôn mặt nhiều người thân.</p>
<p>Khi cán bộ hỏi có còn ai bị giữ trong căn nhà đó không, Mai bật khóc đến nghẹn. Cô sợ nếu nói ra mà họ không cứu được, chị Mỷ sẽ bị đánh. Cô cũng sợ nếu không nói, mình phản bội lời hứa. Cuối cùng, cô dùng tay run run vẽ căn nhà, vẽ cửa sổ, vẽ con đường có cây cong trước ngõ. Bản vẽ méo mó ấy trở thành manh mối đầu tiên để phía biên phòng phối hợp xác minh. Mai không biết số phận ba cô gái còn lại ra sao ngay lúc đó, nhưng cô đã làm điều chị Mỷ dặn: kể lại.</p>
""",
    5808: """
<p>Có những đêm mẹ Mai ngồi bên bếp đến sáng. Bà không dám ngủ sâu vì chỉ cần Mai trở mình mạnh, bà lại chạy vào xem con có khó thở không. Ban ngày, bà cố tỏ ra bình thường, sai Mai nhặt rau, phơi ngô, gấp chăn như trước. Không phải vì bà vô tâm. Bà sợ nếu cả nhà nhìn Mai như đồ sứ vỡ, cô sẽ tin mình thật sự đã vỡ không thể dùng lại được.</p>
<p>Bố Mai thì khác. Ông im lặng nhiều hơn, nhận thêm việc phụ hồ dưới thị trấn để có tiền đưa con đi khám. Có lần Mai thấy ông ngồi sau nhà, cầm mảnh giấy ghi số điện thoại giả của người phụ nữ áo đỏ, vò nát rồi lại vuốt phẳng. Ông tự trách mình nghèo nên con mới bị dụ. Mai lúc đó chưa biết an ủi bố. Sau này cô mới hiểu tội phạm buôn người sống bằng cách biến nghèo đói thành mặc cảm, để gia đình nạn nhân tự nhận lỗi thay chúng.</p>
<p>Cô giáo Thảo là người đầu tiên đề nghị gia đình đưa Mai đi tham vấn tâm lý ở huyện. Ban đầu, mấy người trong họ phản đối, bảo người H'Mông không có bệnh \"nghĩ nhiều\" như người thành phố. Bà ngoại Páo đập gậy xuống nền: \"Chân gãy thì bó. Tim sợ thì cũng phải có người biết bó.\" Nhờ câu nói ấy, Mai được gặp một cô tư vấn viên. Buổi đầu cô chỉ vẽ núi. Buổi thứ hai cô vẽ cửa. Buổi thứ ba, cô vẽ một con hổ đứng trước cửa mở.</p>
""",
    5809: """
<p>Học giỏi không làm lời đồn biến mất ngay. Có ngày Mai được điểm mười môn Văn, ra sân vẫn nghe một bạn trai gọi với theo: \"Luật sư bị bán!\" Cả nhóm cười. Mai đứng khựng lại. Cô đã hứa với mẹ không đánh nhau, nhưng tay vẫn nắm chặt đến đau. Cô giáo Thảo không bắt cô bỏ qua. Cô yêu cầu bạn trai ấy viết bản kiểm điểm và đứng trước lớp đọc một đoạn về quyền được tôn trọng của người bị hại. Hình phạt ấy làm cậu ta xấu hổ, nhưng nó dạy cả lớp rằng xúc phạm cũng có hậu quả.</p>
<p>Lên cấp ba, Mai phải ở bán trú vì trường xa hơn. Đêm đầu trong phòng tập thể, tiếng then cửa đóng làm cô lạnh sống lưng. Một bạn cùng phòng thấy vậy liền đổi giường, để Mai nằm gần cửa sổ. Không phải ai cũng hiểu hết chuyện của cô, nhưng có những người biết giúp bằng cách rất nhỏ: không hỏi quá sâu, không kể lại cho người khác, không tắt đèn đột ngột khi cô còn thức.</p>
<p>Mai bắt đầu làm một cuốn sổ riêng tên là <strong>Những điều cần nói với trẻ em vùng cao</strong>. Trong đó không có lý thuyết lớn. Chỉ có những câu ngắn: đừng đi theo người lạ dù họ nói tiếng mình; số điện thoại có thể giả; tiền đưa trước không phải lòng tốt; nếu bạn bị lừa, bạn vẫn có quyền về nhà. Cuốn sổ ấy sau này trở thành bản nháp đầu tiên của tài liệu Mạng lưới An Toàn.</p>
""",
    5810: """
<p>Ở Hà Nội, Mai cũng gặp định kiến kiểu khác. Có bạn hỏi cô người H'Mông có còn bắt vợ không, có phải ai cũng biết thổi khèn không, có phải vùng cao dễ bị bán vì \"ngây thơ\" không. Những câu hỏi ấy đôi khi không ác, nhưng làm cô mệt. Cô không muốn cả dân tộc mình bị biến thành một hình ảnh nghèo và lạc hậu trong mắt người thành phố. Vì vậy, trong các bài thuyết trình, Mai luôn nói rõ: buôn người không xảy ra vì nạn nhân ngây thơ; nó xảy ra vì có kẻ tổ chức, có lợi nhuận, có lỗ hổng pháp lý và có sự im lặng.</p>
<p>Năm ba, Mai thực tập ở một trung tâm trợ giúp pháp lý. Hồ sơ đầu tiên cô được đọc là một vụ bé gái bị dụ sang bên kia biên giới qua người quen. Trong biên bản, lời khai của em bị ghi rất cụt: <em>tự nguyện đi làm, sau đó muốn về</em>. Mai đọc mà tức đến run. Cô xin được gặp em cùng luật sư hướng dẫn, dùng tiếng H'Mông hỏi lại từng mốc. Hóa ra em bị đe dọa không được nói, bị giữ giấy tờ, bị ép gọi về nhà nói mình ổn. Chỉ vì người ghi lời khai ban đầu không hỏi đúng, vụ việc suýt bị xem nhẹ.</p>
<p>Từ vụ đó, Mai học được sức mạnh của câu hỏi. Một câu hỏi sai có thể làm nạn nhân im. Một câu hỏi đúng có thể mở đường cho công lý. Cô ghi vào sổ: <em>Đừng hỏi vì sao em đi. Hãy hỏi ai rủ em, hứa gì, giữ gì của em, em có được tự về không.</em></p>
""",
    5811: """
<p>Văn phòng của Mai không chỉ tư vấn luật. Nó dần trở thành nơi người ta đến ngồi cho qua cơn run. Có hôm một cô gái được cứu về chỉ xin ngồi trong góc vì về nhà ai cũng hỏi quá nhiều. Mai pha nước gừng, đặt cạnh cô, rồi tiếp tục làm hồ sơ khác. Hai tiếng sau, cô gái tự nói câu đầu tiên: \"Chị ơi, nếu em kể không đúng thứ tự thì có sao không?\" Mai đáp: \"Không sao. Kẻ làm hại em mới phải sợ thứ tự. Em chỉ cần nói từng mảnh.\"</p>
<p>Có vụ Mai thua. Một gia đình rút đơn vì bị họ hàng ép, sợ con gái không lấy được chồng. Mai đến tận nhà, nói khản cổ, nhưng người cha vẫn ký giấy xin không tiếp tục. Đêm đó cô về văn phòng, ngồi trước tủ hồ sơ đến khuya. Cô hiểu luật sư không phải người có thể cứu tất cả bằng ý chí. Muốn thay đổi, phải khiến cả cộng đồng hiểu rằng che giấu không bảo vệ danh dự; nó bảo vệ kẻ phạm tội.</p>
<p>Thất bại ấy là lý do Mai chuyển từ cứu từng hồ sơ sang xây mạng lưới. Cô bắt đầu ghi tên những người có thể trở thành mắt xích: cô giáo biết học sinh vắng bất thường, tài xế xe khách nhớ mặt khách quen, cán bộ hội phụ nữ nghe tin đồn sớm, chủ quán nước gần bến xe thấy ai đón trẻ đi lúc sáng sớm. Công lý ở vùng cao không thể chỉ nằm trong văn phòng luật. Nó phải có chân đi trên đường đất.</p>
""",
    5812: """
<p>Để mạng lưới hoạt động, Mai phải học cách nói chuyện với cả những người không thích mình. Có trưởng bản sợ cô làm bản mang tiếng. Có gia đình sợ bị điều tra chuyện cho con nghỉ học. Có người bảo cô nhận tiền dự án nên phóng đại nguy cơ. Mai không nổi nóng. Cô mang đến từng bản những vụ việc đã ẩn tên, chỉ giữ lại cách lừa, thời gian mất tích, hậu quả pháp lý. Khi nỗi đau được trình bày như bài học chứ không phải lời buộc tội, người ta bắt đầu nghe.</p>
<p>Mạng lưới cũng lập quỹ xe khẩn cấp. Nhiều vụ không được chặn vì gia đình không có tiền xuống huyện trình báo ngay. Mỗi hội viên góp một ít, người bán rau góp năm nghìn, tài xế góp chuyến xe, quán phở góp bữa ăn cho người đi tìm. Số tiền nhỏ nhưng ý nghĩa lớn: cả bản cùng nói rằng một đứa trẻ mất tích không phải việc riêng của một nhà.</p>
<p>Sau năm đầu tiên, Mai tổ chức buổi tổng kết dưới mái nhà văn hóa cũ. Không có hoa nhiều, chỉ có danh sách những vụ đã chặn và những lỗ hổng còn tồn tại. Cô đọc tên các tình nguyện viên, không đọc tên nạn nhân. Mọi người vỗ tay cho những người đã gọi điện đúng lúc, giữ xe đúng lúc, hỏi thêm một câu đúng lúc. Mai muốn họ hiểu: cứu người không phải lúc nào cũng là cảnh lao vào phá cửa. Nhiều khi nó bắt đầu bằng một cuộc gọi không im lặng.</p>
""",
    5813: """
<p>Mai từng hỏi bà có ghét người phụ nữ áo đỏ không. Bà Páo im lặng rất lâu rồi nói: \"Ghét chứ. Nhưng ghét không đủ nuôi con lớn. Phải nhớ.\" Với bà, ký ức không phải để cào lại vết thương mỗi ngày, mà để biết chỗ nào trên đường có bẫy. Bà bảo người già trong bản phải kể chuyện thật cho trẻ nghe, không chỉ kể chuyện ma hay chuyện rừng. Trẻ em cần biết kẻ xấu có thể cười, có thể nói tiếng mình, có thể gọi đúng tên mẹ mình.</p>
<p>Những buổi tối mất điện, Mai cùng bà ngồi bên bếp, sửa lại tài liệu tuyên truyền bằng tiếng H'Mông. Có từ trong luật rất khó dịch. \"Mua bán người\" nếu dịch khô quá, bà con nghe như chuyện xa. Bà Páo đề nghị nói là <em>đem người đi như đem con trâu ra chợ</em>. Mai ban đầu thấy câu ấy đau, nhưng đúng. Người nghe trong bản hiểu ngay sự nhục nhã của việc bị biến thành hàng hóa.</p>
<p>Bà mất vào một mùa đông nhiều sương. Trước khi mất, bà gọi Mai lại, đặt vào tay cô túi vải đựng những sợi chỉ đỏ đã se sẵn. \"Bà không buộc được nữa thì con buộc cho người khác,\" bà nói. Sau tang lễ, Mai mang túi chỉ ấy về văn phòng. Mỗi khi gặp một đứa trẻ vừa được cứu, cô không luôn buộc chỉ cho các em, vì không phải ai cũng cần cùng một biểu tượng. Nhưng cô luôn nhớ lời bà: người sống sót cần thứ gì đó để biết mình vẫn có đường về.</p>
""",
    5814: """
<p>Khi Mai về đến Lao Chải, Dợ và mẹ em đã ngồi trong văn phòng mạng lưới chờ cô. Cô bé vẫn ôm ba lô, nhưng dây kéo đã mở. Bên trong chỉ có hai bộ quần áo, một gói mì tôm và tấm ảnh gia đình gấp làm tư. Mai nhìn tấm ảnh, lòng nhói lên. Năm xưa, cô cũng mang theo quá ít thứ cho một chuyến đi quá dài.</p>
<p>Mai không bắt Dợ hứa sẽ không bao giờ tin ai nữa. Một đứa trẻ không thể lớn lên bằng cách nghi ngờ cả thế giới. Cô chỉ cùng em viết một danh sách kiểm tra: đi đâu, với ai, địa chỉ nào, ai xác nhận, số nào gọi được, nếu đổi lịch thì báo ai. Dợ đọc từng dòng, ban đầu miễn cưỡng, sau đó hỏi thêm: \"Nếu người ta bảo không được nói với bố mẹ thì sao?\" Mai đáp: \"Đó là dấu hiệu đầu tiên phải nói với bố mẹ.\"</p>
<p>Tối ấy, Mai đứng trước lớp học bản Lao Chải, kể lại vụ Dợ nhưng giấu tên. Cô nhìn những gương mặt mười hai, mười ba tuổi dưới ánh bóng đèn vàng, thấy trong đó có chính mình ngày xưa. Cô không kể để các em sợ đến mức không dám mơ rời núi. Cô nói: \"Các em có quyền đi học xa, đi làm xa, nhìn thế giới rộng hơn bản mình. Nhưng không ai có quyền bắt các em đi trong bí mật.\"</p>
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
            marker = f"story_5803_topoff_{chapter_id}"
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
