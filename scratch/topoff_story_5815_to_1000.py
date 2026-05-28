import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("novel_editor", ROOT / "scratch" / "novel_editor.py")
editor = importlib.util.module_from_spec(spec)
spec.loader.exec_module(editor)

STORY_ID = 5815

ADDITIONS = {
    5817: """
Khi gần hết mưa, một người đàn ông say rượu loạng choạng ghé xe chè, đập tay xuống mặt kính đòi ăn chịu. Bảo sợ đến mức lùi sát vào gốc me. Ông Phước vẫn bình tĩnh múc một chén chè nóng, đặt trước mặt người ấy rồi nói: "Ăn cho ấm bụng rồi về ngủ, đừng làm trẻ con sợ." Người đàn ông lầm bầm vài câu, ăn xong bỏ đi không trả tiền. Bảo nhìn theo, hỏi ông sao không mắng. Ông Phước lau mặt kính, đáp: "Có người đói bụng, có người đói tỉnh táo. Mình cho được gì thì cho, nhưng vẫn phải giữ mình không thành người dữ."

Câu ấy Bảo chưa hiểu hết. Cậu chỉ thấy ông già này khác những người từng xua mình khỏi mái hiên. Ông không hỏi cậu có ngoan không mới cho ăn, không bắt cậu kể chuyện đời mình để đổi lấy lòng thương hại. Ông đặt chén chè xuống trước, rồi để cậu tự quyết có tin hay không. Chính sự chậm rãi ấy làm Bảo nán lại thêm một chút dưới mái đèn vàng.
""",
    5818: """
Có lần một bà bán vé số ghé qua, thấy Bảo lau muỗng thì dúi cho cậu một tờ vé số ế. Bảo lắc đầu không nhận, bà cười móm mém: "Không phải cho con đổi đời, cho con biết người nghèo cũng có thứ để tặng." Cậu cầm tờ vé số, vuốt phẳng rồi kẹp vào cuốn sổ của ông Phước. Đêm ấy cậu hỏi ông: "Người nghèo cho nhau thì có bị nghèo thêm không?" Ông Phước suy nghĩ một lúc rồi nói: "Nếu cho để khoe thì nghèo thêm. Nếu cho để người kia đứng dậy được, lòng mình rộng thêm."

Từ đó Bảo nhìn khách bằng mắt khác. Cậu thấy bác bảo vệ để dành phần chè cho vợ bị bệnh ở nhà, thấy cô công nhân mua một bịch nhưng xin thêm hai cái muỗng để chia với bạn cùng phòng, thấy chú tài xế mệt rã rời vẫn hỏi ông Phước có cần chở đi khám không. Thế giới của cậu trước kia chỉ có đuổi và tránh. Bên xe chè, cậu bắt đầu học một từ mới chưa viết được nhưng cảm được rất rõ: nương tựa.
""",
    5819: """
Buổi chiều hôm đó, dì của Bảo bất ngờ tìm tới sau khi nghe người quen nói thấy cậu ở chợ. Người phụ nữ đứng ngoài cửa, mặt vừa mừng vừa ngại, tay xách túi trái cây rẻ tiền. Bảo núp sau lưng ông Phước, toàn thân căng cứng. Dì không trách, cũng không đòi đưa cậu về. Bà chỉ khóc, nói ngày ấy nhà khổ quá, lời nặng quá, giờ nghĩ lại cứ ân hận. Ông Phước pha trà, để hai dì cháu ngồi trước cửa, còn mình lui vào bếp.

Bảo không ôm dì. Cậu chưa thể. Nhưng cậu nhận trái chuối bà đưa và hỏi mấy đứa em có đi học không. Cuộc gặp ngắn, vụng về, không xóa được những đêm cậu ngủ ngoài đường, nhưng nó làm một nút thắt trong lòng cậu bớt siết. Sau khi dì đi, ông Phước nói: "Tha thứ không phải là quên hết. Tha thứ là mình không để chuyện cũ cắn mình mỗi ngày." Bảo nhìn nồi chè sôi lục bục, lần đầu hiểu có những vết thương cần lửa nhỏ rất lâu mới mềm ra.
""",
    5820: """
Có hôm mất điện, cả hẻm tối om. Ông Phước thắp cây đèn dầu nhỏ, ánh sáng run rẩy phủ lên trang vở của Bảo. Ngoài đường, tiếng mưa gõ mái tôn, tiếng người gọi nhau kéo đồ khỏi chỗ dột. Bảo đọc một đoạn văn về biển, cứ vấp ở chữ "mênh mông". Ông Phước cũng không đọc trơn được, hai ông cháu ngồi đánh vần mãi rồi cùng bật cười. Bảo nói: "Ông cũng dở." Ông gật đầu rất thật: "Ừ, nên ông học chung với con."

Chính câu ấy làm Bảo hết xấu hổ. Cậu từng nghĩ đi học là phải giỏi ngay, sai là bị phạt, chậm là đáng bị bỏ lại. Nhưng ông Phước, một người già tóc bạc, vẫn cúi xuống học từng chữ với cậu mà không thấy nhục. Từ đó mỗi lần gặp chữ khó, Bảo không vò giấy nữa. Cậu lấy bút gạch chân, hỏi lại, đọc chậm. Cậu hiểu học không phải để chứng minh mình chưa từng thấp kém; học là để từ ngày mai mình bớt bị bóng tối dắt đi.
""",
    5821: """
Cuối học kỳ, lớp tổ chức buổi đọc bài trước phụ huynh. Bảo không định mời ông Phước vì sợ ông bỏ buổi nấu chè, nhưng cô chủ nhiệm tự gọi điện. Chiều đó ông mặc áo sơ mi cũ, tay cầm bó hoa cúc mua ở chợ, ngồi ở hàng ghế cuối. Khi Bảo bước lên đọc bài văn về người thân, giọng cậu run đến mức chữ đầu tiên gần như mắc lại. Rồi cậu nhìn thấy ông Phước giơ ngón cái lên, rất kín đáo.

Bảo đọc hết bài. Cậu đọc không hay như bạn khác, nhưng từng chữ rõ ràng, không bỏ dòng. Đến câu "ông cho em ăn khi em đói và bắt em đi học khi em muốn biến mất", nhiều phụ huynh quay lại nhìn người đàn ông bán chè ngồi cuối lớp. Ông Phước cúi đầu, hai tay đặt trên bó hoa. Sau buổi đó, Bảo không còn giấu chuyện mình từng lang thang. Cậu nhận ra quá khứ nghèo khổ không phải cái bảng xấu treo trước ngực, nếu hiện tại mình vẫn đang bước về phía sáng.
""",
    5822: """
Những ngày ông nằm viện, Bảo học thêm một kiểu sợ khác: sợ tiếng điện thoại reo lúc nửa đêm, sợ bác sĩ gọi người nhà, sợ chiếc giường bệnh trống khi mình quay lại. Cậu giấu nỗi sợ ấy rất vụng. Ban ngày cậu đi học, ghi bài thật nhanh. Chiều về nấu chè, tối bán, khuya rửa nồi, rồi đạp xe vào bệnh viện ngủ gục trên ghế nhựa. Có hôm cô y tá đánh thức, bảo trẻ con không được ngủ ngoài hành lang lạnh. Bảo đáp: "Con là người nhà."

Hai chữ đó làm ông Phước nghe thấy mà mở mắt. Người nhà. Không giấy nhận nuôi nào kịp hoàn tất, không họ hàng nào chứng kiến, nhưng cậu bé từng không có chỗ ngủ đã tự nhận mình thuộc về ông bằng một câu chắc nịch. Ông Phước nắm tay Bảo, bàn tay già lạnh hơn mọi khi. "Người nhà thì phải nghe lời nhau," ông nói. "Con hứa không bỏ học vì ông." Bảo cắn môi gật đầu. Cậu hiểu nếu vì thương ông mà tự cắt mất tương lai, ông sẽ còn đau hơn bệnh.
""",
    5823: """
Khi Bảo đi thực tập ở một bếp khách sạn, đầu bếp trưởng từng khuyên cậu nên bỏ xe chè. Ông ta nói nghề đường phố không có tương lai, muốn tiến xa phải học món Âu, học trình bày, học phục vụ khách sang. Bảo nghe rất chăm chú, vì cậu biết người ta nói có phần đúng. Nhưng tối về, nhìn ông Phước ngồi bên xe chè hỏi từng khách hôm nay có mệt không, cậu hiểu tương lai của mình không nhất thiết phải chạy khỏi nơi bắt đầu.

Cậu bắt đầu ghi chép công thức nghiêm túc hơn: lượng đường, thời gian ngâm đậu, cách bảo quản nước cốt dừa, cách nấu chè ít ngọt cho người lớn tuổi. Ông Phước nhìn cuốn sổ dày lên từng ngày thì trêu: "Chè của ông mà con làm như nghiên cứu khoa học." Bảo đáp: "Vì con muốn sau này dù ông không đứng đây, vị chè vẫn không lạc." Nói xong, cả hai đều im. Có những câu thật quá, chạm vào điều họ sợ nhất.
""",
    5824: """
Quán chè nhỏ sau này có một quy định lạ: nhân viên mới phải ngồi một đêm bên chiếc xe cũ, không bán gì cả, chỉ nghe khách nói chuyện. Bảo bảo họ phải hiểu trước khi múc chè. Hiểu vì sao có người ăn thật chậm để kéo dài một chỗ ngồi ấm; vì sao có sinh viên mua một chén rồi xin thêm nước nóng; vì sao một bác tài xế đêm nào cũng chọn đúng góc bàn nhìn ra đường. Chè có thể học công thức, nhưng sự tử tế phải học bằng cách ngồi đủ lâu với nỗi mệt của người khác.

Thỉnh thoảng, Bảo vẫn mơ thấy đêm mưa đầu tiên. Trong mơ, cậu bé gầy gò ngồi dưới gốc me, còn ông Phước bưng chén chè đi qua màn mưa. Lần nào tỉnh dậy, Bảo cũng xuống bếp kiểm nồi đậu, lau lại tấm bảng gỗ rồi bật bóng đèn trước cửa. Anh biết mình không thể cứu hết những đứa trẻ lạc trong thành phố. Nhưng anh có thể giữ một góc sáng, một chén nóng, một câu hỏi dịu dàng. Và đôi khi, chỉ vậy thôi cũng đủ để một đời người đổi hướng.
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
            content = (chapter["content"] or "").rstrip() + "\n\n" + addition.strip()
            editor.update_chapter(cid, chapter["title"], content)
            updates.append({"chapter_id": cid, "title": chapter["title"]})
    finally:
        editor.remove_helper()
    out = ROOT / "scratch" / "story_5815_topoff_result.json"
    out.write_text(json.dumps(updates, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(updates, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
