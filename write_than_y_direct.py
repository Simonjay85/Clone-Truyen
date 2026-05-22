# -*- coding: utf-8 -*-
import json
import os
import re
import sys

OUTPUT_FILE = "/Users/aaronnguyen/TN/App/doctieuthuyet/pending_novel.json"

def split_into_sentences(text):
    # Standardize spaces
    t = re.sub(r'\s+', ' ', text).strip()
    
    # Abbreviations list to avoid splitting on them
    abbrevs = ["TS.", "BS.", "CFO.", "Dr.", "Mr.", "Mrs.", "Ms.", "A.S.A.P.", "Deloitte.", "Keangnam.", "BIDV.", "GC-MS.", "C03."]
    for i, abb in enumerate(abbrevs):
        t = t.replace(abb, f"__ABB{i}__")
        
    # Mark sentence endings: punctuation (. ! ?) followed by optional quotes, then space, then capital or quote/number
    t = re.sub(r'([.!?]["”\'’]?)\s+(?=[A-Z"“\'‘\d\-\w])', r'\1[SENTENCE_END]', t)
    
    # Restore abbreviations
    for i, abb in enumerate(abbrevs):
        t = t.replace(f"__ABB{i}__", abb)
        
    sentences = t.split("[SENTENCE_END]")
    result = []
    for s in sentences:
        s = s.strip()
        if s:
            result.append(s)
    return result

def clean_and_format_content(raw_text):
    # Remove HTML tags to let the Python splitter handle V13 paragraph wrapping purely
    clean_text = re.sub(r'<[^>]+>', ' ', raw_text)
    sentences = split_into_sentences(clean_text)
    
    v13_paragraphs = []
    for s in sentences:
        if s:
            v13_paragraphs.append(f"<p>{s}</p>")
            
    return "\n".join(v13_paragraphs) + "\n"

def count_words(text):
    words = text.split()
    # Simple word count ignoring html tags
    clean = re.sub(r'<[^>]+>', '', text)
    return len(clean.split())

def main():
    print("🚀 DIRECT NOVEL EXPANSION ENGINE - V13 GOLD STANDARD")
    
    novel_blueprint = {
        "title": "THẦN Y BỊ ĐUỔI, VỢ CŨ HỐI HẬN MUỘN MÀNG",
        "author": "Lương Minh Khải",
        "genre": "Sảng Văn",
        "intro": "<p><strong>\"Anh cống hiến sáu năm ròng rã cứu sống hàng ngàn người, nhưng đến ngày bài thuốc gan gia truyền của anh có kết quả kiểm nghiệm đột phá, họ vu oan anh kê đơn sai gây chết người rồi đuổi anh ra khỏi bệnh viện không thương tiếc.\"</strong></p>\n<p>Lương Minh Khải, bác sĩ y học cổ truyền kiệt xuất bị chính người vợ đầu ấp tay gối Nguyễn Thanh Hà phản bội và gã sếp Phạm Hoàng Vũ âm mưu giàn dựng cướp đoạt toàn bộ công trình nghiên cứu gia truyền của họ Lương.</p>\n<p>Giữa lúc bị dồn vào đường cùng, anh gặp Trần Bảo Châu, nữ CFO sắc sảo và lý tính của tập đoàn dược phẩm Thiên Phúc. Cùng nhau, họ lập nên một liên minh thép, không chỉ lột trần bộ mặt thật của những kẻ ăn cắp chất xám mà còn chứng minh hiệu quả lâm sàng vượt trội của bài thuốc, đưa những kẻ phản bội vào chốn lao tù và khiến người vợ cũ phải chịu đựng sự hối hận muộn màng tột cùng.</p>",
        "cover_prompt": "A highly premium, cinematic anime-style web novel cover. A handsome 32-year-old Vietnamese traditional doctor in a modern laboratory, holding a vintage wooden medical box with intricate gold patterns. Beside him stands a beautiful, sophisticated 30-year-old Vietnamese corporate woman (CFO) wearing a elegant blazer. Background displays state-of-the-art chemical analysis screens showing GC-MS chromatography graphs and molecular models of liver cells. Beautiful dramatic studio lighting, golden accents, bold and inspiring art.",
        "chapters": []
    }
    
    # CHAPTER 1 - Trimmed to be under 1500 words
    ch1 = """Tờ quyết định sa thải được đặt trên bàn làm việc của Lương Minh Khải vào đúng 7 giờ sáng thứ Hai lạnh lẽo giữa mùa đông Hà Nội. Không phải là một email thông báo tự động từ phòng hành chính nhân sự, cũng chẳng phải là một cuộc gọi điện thoại trao đổi trước từ giám đốc. Đó chỉ là một tờ giấy A4 trắng tinh đóng dấu đỏ chói lọi của Bệnh viện Đa khoa Hà Thành, gấp gọn gàng nằm im lìm trong một chiếc phong bì màu trắng đục có ghi tên anh viết tay bằng mực xanh. Khải lặng lẽ nhìn vào tờ quyết định sa thải lạnh lùng ấy, mười đầu ngón tay của anh hoàn toàn bất động, cứng đờ giữa bầu không khí xám xịt của phòng làm việc.

Hàng chữ in đậm đập thẳng vào mắt anh như một vết dao cứa sắc lẹm: "Căn cứ vào biên bản kiểm tra y khoa ngày 14/11, bác sĩ Lương Minh Khải đã kê đơn sai dẫn đến phản ứng thuốc nghiêm trọng cho bệnh nhân Trần Văn Long, 58 tuổi. Hội đồng kỷ luật nhất trí đình chỉ công tác y tế và chấm dứt hợp đồng lao động kể từ ngày ký." Bệnh nhân Trần Văn Long, Khải nhớ cực kỳ rõ ca bệnh này. Ông Long nhập viện nửa tháng trước trong tình trạng men gan AST/ALT tăng vọt gấp năm lần ngưỡng bình thường, chẩn đoán xơ gan giai đoạn hai kèm theo các triệu chứng suy nhược cơ thể trầm trọng. Anh đã thức trắng đêm nghiên cứu, kê thang thuốc bổ can giải độc gia truyền của dòng họ mình, kết hợp hài hòa với phác đồ Tây y hiện đại và trực tiếp theo dõi sát sao chỉ số sinh hóa của bệnh nhân từng ngày. Kết quả là ông Long xuất viện sau mười bốn ngày điều trị với chỉ số men gan phục hồi kỳ diệu về gần mức bình thường.

Hoàn toàn không có bất kỳ phản ứng bất thường hay dị ứng nào xảy ra trong suốt thời gian ông Long điều trị tại bệnh viện Hà Thành. Nhưng tờ quyết định đuổi việc trên bàn vẫn được đóng dấu đỏ tươi chói mắt, biểu thị một thực tế phũ phàng đã được an bài từ trước. Khải khẽ đứng dậy khỏi chiếc ghế xoay, anh định mở cửa bước ra ngoài thì nhận ra cánh cửa phòng làm việc của mình - căn phòng trưởng khoa Y học cổ truyền mà anh đã gắn bó suốt sáu năm ròng rã - đã bị đổi khóa từ hồi nào không hay. Anh cay đắng bước ra hành lang bệnh viện ngập tràn mùi thuốc khử trùng nồng nặc.

Phạm Hoàng Vũ, giám đốc bệnh viện Hà Thành đứng ngay trước cửa phòng sảnh chính hành lang. Bên cạnh ông ta là Tiến sĩ Ngô Quang Đức - phó khoa Y học cổ truyền, kẻ luôn chải chuốt mái tóc mượt mà bóng loáng, mặc bộ comple màu xanh đen sang trọng và nở nụ cười đủng đỉnh đầy đắc ý. Và đứng lùi lại thêm một bước ở phía sau, mắt nhìn chăm chăm xuống sàn gạch hoa mát lạnh, chính là Nguyễn Thanh Hà - người vợ đầu ấp tay gối suốt bốn năm qua của anh.

"Khải." Giám đốc Phạm Hoàng Vũ lên tiếng trước bằng chất giọng nhẹ tênh, bình thản như thể đang nói chuyện thời tiết ngoài trời. "Anh đã đọc kỹ tờ quyết định sa thải rồi chứ? Thủ tục bàn giao toàn bộ trang thiết bị phòng làm việc và hồ sơ bệnh án phải xong trước mười giờ sáng nay nhé."

"Ông và Ngô Quang Đức đã dựng chuyện vu khống tôi." Khải nói, giọng nói của anh phẳng lặng như mặt nước hồ mùa đông, không hề có một chút run rẩy hay tức giận lộ ra ngoài.

"Chứng cứ y khoa đã quá đầy đủ rồi." Tiến sĩ Đức bước lên một bước, chen vào bằng giọng điệu châm chọc. "Hồ sơ bệnh án của ông Long, đơn thuốc do chính tay anh ký nhận, biên bản giám định y tế lâm sàng - tất cả mọi thứ đều chỉ thẳng sai phạm nghiêm trọng vào anh."

Khải nhìn thẳng vào đôi mắt hí xảo quyệt của Đức. Đó không phải là ánh mắt tức giận hay phẫn uất của kẻ yếu thế, mà là sự nhận ra lạnh người: cái hồ sơ bệnh án số hóa trên máy chủ bệnh viện đã bị thay đổi dữ liệu một cách tinh vi.

"Hà." Anh chuyển ánh mắt lạnh lẽo sang nhìn người vợ của mình. "Em biết chuyện này từ bao giờ?"

Nguyễn Thanh Hà ngẩng đầu lên đối diện với ánh mắt của anh. Ánh mắt cô ta hoàn toàn không có lấy một chút tội lỗi hay áy náy nào, chỉ có sự lạnh lùng tàn nhẫn và nét mệt mỏi của một người phụ nữ đã quyết định xong xuôi mọi thứ từ lâu.

"Tôi đã nộp đơn ly hôn đơn phương lên tòa án quận sáng nay rồi." Cô ta lạnh lùng nói. "Tòa án đã thụ lý và hẹn chúng ta hòa giải vào tháng sau."

Khải đứng im lìm như một pho tượng đá giữa hành lang bệnh viện lộng gió. Mồ hôi không chảy trên trán anh, trái tim anh cũng không hề đập loạn nhịp vì đau đớn. Chỉ có một khoảng trống lạ lùng, lạnh lẽo mở ra ở sâu thẳm trong lồng ngực anh, tựa như khi người ta rút chiếc chìa khóa cũ ra khỏi ổ khóa rỉ sét mà không buồn khép cánh cửa lại.

"Được rồi." Anh nói khẽ.

Chỉ vỏn vẹn đúng hai tiếng ngắn ngủi ấy. Khải quay lưng bước vào phòng làm việc cũ, lấy chiếc túi vải đựng vài cuốn sách chuyên ngành y học cổ truyền mà anh đã sắp xếp sẵn từ sáng sớm - cứ như thể anh đã biết trước kịch bản bẩn thỉu này từ rất lâu - rồi sải bước thẳng ra phía lối thoát hiểm.

Giám đốc Phạm Hoàng Vũ gọi với theo từ phía sau hành lang: "Anh Khải, hồ sơ nghiên cứu chi tiết về bài thuốc gan của anh - theo đúng quy định pháp lý của bệnh viện, tất cả tài sản trí tuệ phát sinh trong thời gian anh công tác tại đây đều thuộc sở hữu vô thời hạn của Bệnh viện Hà Thành."

Khải dừng bước chân, anh từ từ xoay người lại đối mặt với hai gã phản diện.

"Ông thực sự muốn cái gì ở tôi nữa?" Anh hỏi, giọng vẫn phẳng lặng.

"Ký vào biên bản bàn giao nghiên cứu. Đây chỉ là thủ tục hành chính bắt buộc thôi." Ngô Quang Đức đưa ra một tập hồ sơ dày cộp bọc da đen trước mặt anh.

Khải nhìn tập hồ sơ đó trong mười giây dài đằng dãng. Rồi anh mỉm cười lần đầu tiên trong buổi sáng tăm tối hôm đó - một nụ cười nhỏ, khô khốc và không hề có một chút niềm vui nào, giống như một người vừa xác nhận xong một điều nghi ngờ kinh tởm mà mình đã đoán biết từ lâu.

"Tôi chưa từng nộp tài liệu nghiên cứu nào về bài thuốc gan họ Lương vào kho lưu trữ của bệnh viện này để phải ký bàn giao." Khải dõng dạc nói. "Bài thuốc đó là di sản gia tộc họ Lương bốn đời truyền lại, chưa bao giờ và sẽ không bao giờ là tài sản của ông."

"Anh Khải, anh hãy cẩn thận với lời nói của mình đấy—" Đức giận dữ gầm gừ.

"Chúc ông một buổi sáng tốt lành." Khải quay đầu đi thẳng.

Anh bước ra khỏi cánh cửa kính lớn của bệnh viện Hà Thành. Nắng tháng Mười một của Hà Nội đổ xuống mặt đường nhựa nhựa như thể bị ai đó đổ mạnh ra từ một chiếc xô khổng lồ. Khải đứng một mình trước cổng bệnh viện, nhìn vào dòng xe cộ đông đúc đang ùn tắc nghiêm trọng ở ngã tư lớn trước mặt, và lần đầu tiên kể từ khi mở mắt thức dậy vào buổi sáng - anh thở ra một hơi dài và chậm rãi.

Chiếc điện thoại cũ trong túi quần anh bất chợt rung lên bần bật. Đó là một tin nhắn ngắn gửi đến từ một số điện thoại hoàn toàn xa lạ: "Bác sĩ Lương Minh Khải, tôi là Trần Bảo Châu - CFO của Tập đoàn Dược phẩm Thiên Phúc. Tôi có việc rất quan trọng muốn gặp anh trực tiếp. Không phải để gửi lời an ủi sáo rỗng. Tôi muốn đề xuất một thương vụ hợp tác thương mại lớn."
"""

    # CHAPTER 2
    ch2 = """Quán cà phê cổ kính nằm trên phố Tràng Tiền chỉ có đúng ba bàn khách vào buổi sáng giữa tuần lạnh giá. Trần Bảo Châu ngồi lặng lẽ ở một chiếc bàn gỗ nhỏ đặt trong góc khuất phía trong của quán. Cô mặc một chiếc áo blazer màu đen cắt may vô cùng tinh xảo, mái tóc đen mượt được búi thấp gọn gàng sau gáy, để lộ ra gương mặt thanh tú nhưng toát lên vẻ sắc sảo lạnh lùng. Một tay cô khẽ cầm cốc bạc xỉu ấm áp nhưng chưa hề nhấp một ngụm nào, tay còn lại đặt lên một tập hồ sơ mỏng đóng bìa màu xanh dương bóng loáng.

Cô hoàn toàn không đứng dậy khi Lương Minh Khải bước đến gần bàn. Cô chỉ khẽ gật đầu một cái thật nhẹ, dùng ánh mắt sắc bén ra hiệu cho anh ngồi vào chiếc ghế gỗ trống đối diện mình.

"Anh đến rất đúng giờ." Bảo Châu lên tiếng bằng chất giọng thanh mảnh nhưng vô cùng rõ ràng và dứt khoát. Đó không phải là một lời khen ngợi xã giao, mà chỉ đơn thuần là một lời nhận xét thực tế.

"Cô là ai?" Khải ngồi xuống ghế, đi thẳng vào vấn đề mà không cần vòng vo.

"Tôi vừa tự giới thiệu danh tính và chức vụ của mình qua tin nhắn lúc sáng rồi."

"Tôi hỏi cô là ai trong ván bài âm mưu này của bệnh viện Hà Thành." Khải hỏi lại, đôi mắt nhìn thẳng vào cô không chút né tránh.

Bảo Châu nhìn anh trong ba giây dài - kiểu nhìn chăm chú và lạnh lùng của một nhà tài phiệt chuyên nghiệp đang đánh giá giá trị thực sự của một món hàng hóa quý hiếm trước khi quyết định đặt cọc số tiền lớn.

"Cha tôi là Trần Văn Long." Cô bình thản nói. "Ông chính là bệnh nhân xơ gan giai đoạn hai của anh tại khoa Y học cổ truyền bệnh viện Hà Thành. Và ông cũng chính là người mà ban giám đốc bệnh viện đang lấy làm cái cớ để vu khống và sa thải anh."

Khải vẫn giữ nguyên nét mặt phẳng lặng như tờ của mình, không hề tỏ ra ngạc nhiên.

"Cha cô hiện tại tình hình sức khỏe thế nào rồi?" anh hỏi thăm với tư cách một người bác sĩ.

"Chỉ số men gan của cha tôi đã giảm về mức 42/38 U/L. Kết quả siêu âm ổ bụng tuần trước tại Bệnh viện Bạch Mai cho thấy tình trạng xơ hóa tế bào gan đã giảm đi rõ rệt." Bảo Châu từ từ mở tập hồ sơ xanh ra, đẩy nhẹ tờ kết quả xét nghiệm sinh hóa về phía Khải. "Cha tôi hoàn toàn khỏe mạnh sau khi xuất viện nhờ thang thuốc can giải độc của anh, chứ không hề bị phản ứng thuốc hay nguy kịch như những gì bệnh viện Hà Thành đang dựng chuyện để bôi nhọ anh."

Khải nhìn xuống tờ kết quả xét nghiệm được đóng dấu đỏ của Bệnh viện Bạch Mai.

Các chỉ số hiện lên vô cùng hoàn hảo: AST 42 U/L, ALT 38 U/L, Bilirubin toàn phần 1.1 mg/dL. Đó là các chỉ số sinh hóa của một người đàn ông trung niên có là gan hoàn toàn khỏe mạnh.

"Cô giữ kết quả xét nghiệm thực tế này làm gì?" Khải hỏi.

"Để dùng làm vũ khí quyết định khi cần thiết." Giọng nói của cô vẫn không có một chút dao động cảm xúc nào. "Anh có muốn biết lý do vì sao bệnh viện Hà Thành lại chọn ca bệnh của cha tôi để làm bằng chứng giả sa thải anh không?"

"Tôi có thể đoán được phần nào." Khải trả lời.

"Bởi vì họ nghĩ cha tôi là một ông già nghỉ hưu không có con trai hay thế lực gia tộc để đứng ra khiếu nại. Họ nghĩ tôi chỉ là một người phụ nữ làm văn phòng và sẽ lựa chọn im lặng để bảo toàn danh dự gia đình." Bảo Châu nhẹ nhàng nhấp một ngụm nhỏ cà phê bạc xỉu. "Nhưng ban giám đốc bệnh viện Hà Thành đã đánh giá sai lầm hoàn toàn."

Khải khẽ chống hai khuỷu tay lên mặt bàn gỗ, ánh mắt sắc sảo.

"Cô nói muốn đề xuất hợp tác y tế. Điều kiện cụ thể là gì?"

Bảo Châu gập tập hồ sơ bệnh án lại, cô rút từ trong túi xách ra một tờ tài liệu khác - tờ này là bản tóm tắt phân tích thị trường dược phẩm bổ gan tại Việt Nam với những con số doanh thu vô cùng rõ ràng.

"Thị trường các sản phẩm thuốc bổ gan và hỗ trợ điều trị xơ gan tại Việt Nam năm ngoái đạt quy mô 4.200 tỷ đồng, với tốc độ tăng trưởng trung bình đạt 18% mỗi năm. Tập đoàn Thiên Phúc hiện tại chỉ mới chiếm giữ khoảng 9% thị phần." Cô đặt chiếc bút máy Montblanc đắt giá lên bàn. "Bài thuốc bổ can giải độc gia truyền của dòng họ Lương anh - theo tất cả những thông tin khoa học mà tôi đã âm thầm thu thập - có khả năng tái tạo tế bào và đảo ngược quá trình xơ hóa gan mà không một sản phẩm dược phẩm nào trên thị trường hiện nay có thể làm được. Nếu chúng ta phát triển thành công sản phẩm thương mại, giá trị của bài thuốc này sẽ không dưới ba trăm tỷ đồng."

"And Thiên Phúc muốn có được điều gì từ bài thuốc của gia đình tôi?"

"30% cổ phần công thức độc quyền của sản phẩm mới. Tập đoàn Thiên Phúc chúng tôi sẽ cam kết lo liệu toàn bộ quy trình sản xuất công nghiệp đạt chuẩn GMP, kiểm định chất lượng nghiêm ngặt, hệ thống kênh phân phối toàn quốc và đăng ký lưu hành chính thức tại Bộ Y tế. Anh sẽ giữ vững 70% cổ phần còn lại, đồng thời sở hữu toàn quyền kiểm soát tên thương hiệu sản phẩm và xuất xứ nguồn dược liệu gốc." Bảo Châu nhìn thẳng vào mắt anh bằng vẻ kiên định tuyệt đối. "Tôi không đứng ra cứu anh khỏi vụ bê bối này vì lòng thương hại hay từ tâm xã hội. Tôi cứu anh vì đây là một thương vụ thương mại béo bở mang lại lợi nhuận khổng lồ."

Khải ngồi im lặng một lát, suy nghĩ sâu sắc.

"Cô có thể giúp tôi kiện bệnh viện Hà Thành ra tòa không?"

"Tôi hoàn toàn có thể cung cấp đầy đủ bằng chứng y khoa pháp lý về tình trạng sức khỏe thực tế của cha tôi để phủ nhận mọi cáo buộc kê đơn sai của họ. Nhưng phần còn lại để đưa bọn họ ra tòa án hình sự thì anh cần một luật sư sở hữu trí tuệ xuất sắc." Bảo Châu trả lời rõ ràng. "Nhưng trước hết - tôi cần xác nhận bài thuốc gia truyền đó có thực sự mang lại hiệu quả tái tạo gan kỳ diệu như vậy trên số mẫu lớn không? Hay nó chỉ là một bài thuốc dân gian ăn may chưa được kiểm chứng khoa học?"

Khải tự tin nhìn cô.

"Cô có thể thu xếp cho tôi toàn quyền sử dụng phòng thí nghiệm R&D hiện đại bậc nhất của Thiên Phúc không?"

"Hoàn toàn được."

"Vậy thì hãy cho tôi thời gian bốn tuần."

Bảo Châu hài lòng gật đầu nhẹ. Cô chủ động đưa bàn tay thon dài ra phía trước.

Khải đưa tay ra bắt chặt lấy tay cô.

Cái bắt tay giữa hai người không hề mang lại cảm giác ấm áp của một mối quan hệ thông thường. Nhưng nó cực kỳ chắc chắn, biểu thị một liên minh thép đã chính thức được thiết lập.
"""

    # CHAPTER 3
    ch3 = """Ông nội của Lương Minh Khải - cụ Lương Văn Đạo - năm nay đã bước sang tuổi bảy mươi hai. Cụ sống tĩnh lặng trong một ngôi nhà cổ kính nằm sâu trong con hẻm nhỏ ngoằn ngoèo ở phố Hàng Bồ. Căn nhà ba tầng trát lớp vôi vàng cũ kỹ, rêu phong bám đầy trên những mảng tường cổ xưa mà không một viên gạch nào chịu thay đổi theo thời gian.

Cụ Đạo đang ngồi sàng những lá thuốc nam thơm nồng trên chiếc nong tre lớn khi Khải bước chân vào nhà. Đôi bàn tay gầy gò đầy những vết chai sạn của cụ vẫn vô cùng thoăn thoắt, đôi mắt hiền từ nhưng tinh anh nhìn Khải từ đầu đến chân rồi lại tiếp tục quay về công việc sàng thuốc của mình.

"Con bị bệnh viện Hà Thành đuổi việc rồi phải không." Cụ cất tiếng nói trầm ấm. Đó không phải là một câu hỏi để xác nhận thông tin, mà là một lời khẳng định chắc chắn.

"Ông nội đã biết chuyện này rồi sao?" Khải hỏi.

"Bố con đã điện thoại báo cho tao từ tối hôm qua ngay sau khi thằng Vũ gọi điện đe dọa." Cụ đặt chiếc nong tre đựng thuốc xuống sàn nhà gỗ. "Con ngồi xuống đây đi."

Khải lặng lẽ ngồi xuống chiếc ghế gỗ thấp đối diện với ông nội mình.

"Bọn họ đang dùng mọi thủ đoạn dơ bẩn để cướp lấy công thức bài thuốc gan gia truyền của gia đình mình." Khải nói.

"Tao biết thừa dã tâm của tụi nó." Giọng cụ Đạo vẫn bình thản như thể đang nói về một cơn mưa rào ngoài phố. "Hồi con còn học năm thứ ba Học viện Y Dược, tao đã từng nghiêm khắc dặn dò con - tuyệt đối đừng bao giờ mang bài thuốc bổ can của dòng họ mình áp dụng bừa bãi vào hệ thống bệnh viện nhà nước khi chưa có sự phòng bị pháp lý đầy đủ. Con đã không nghe lời tao dặn."

"Con chỉ muốn dùng y thuật của mình để cứu chữa cho nhiều bệnh nhân nghèo khổ thôi, con hoàn toàn không đăng ký bài thuốc đó dưới danh nghĩa sở hữu của bệnh viện..." Khải cúi đầu.

"Nhưng con đã dại dột ghi chép chi tiết các hoạt chất dược lý và tỷ lệ phối ngũ vào hồ sơ nghiên cứu nội bộ của khoa. Như thế là quá đủ để những kẻ tham lam như thằng Vũ và thằng Đức lấy làm cái cớ để cướp đoạt trắng trợn rồi."

Khải im lặng cúi đầu, lòng nặng trĩu.

Cụ Đạo khẽ đứng dậy, bước chậm rãi vào căn phòng thờ tổ tiên ở phía trong, tiếng chìa khóa sắt lách cách vang lên trong không gian tĩnh mịch. Một lát sau, cụ mang ra một chiếc hộp gỗ sơn then màu đen bóng, chiếc khóa đồng bên ngoài đã xỉn màu xám xịt theo năm tháng.

"Đây." Cụ từ từ đặt chiếc hộp gỗ quý giá xuống bàn trà. "Đây là bản gốc bài thuốc gia truyền họ Lương. Chữ viết tay của ông cố con viết từ năm 1948 bằng mực Nho trên giấy bản cổ. Tao đã chủ động công chứng bản dịch thuật y khoa cổ và nộp hồ sơ đăng ký quyền sở hữu trí tuệ sáng chế độc quyền từ tháng trước rồi - đây là mã số hồ sơ chính thức."

Cụ Đạo rút từ trong túi áo ra một tờ giấy A4 đóng dấu giáp lai của Cục Sở hữu trí tuệ. Mã số hồ sơ đăng ký sáng chế độc quyền ghi rõ ngày nộp: 28/10 - đúng hai tuần trước ngày Lương Minh Khải bị sa thải khỏi bệnh viện Hà Thành.

Khải bàng hoàng nhìn vào tờ giấy chứng nhận đăng ký.

Đôi bàn tay anh không hề run rẩy, nhưng có một luồng cảm xúc thắt chặt lại ở phía sau hốc mắt anh, dâng lên một sự kính phục vô hạn đối với sự minh triết của ông nội.

"Ông nội đã biết trước bọn họ sẽ giở trò bỉ ổi này sao?"

"Tao tuy già rồi nhưng mắt tao không mờ, tao đã quen ngửi thấy mùi tham lam của lòng người rồi." Cụ Đạo ngồi xuống ghế, lại cầm chiếc nong tre sàng thuốc lên. "Con hãy mang tập hồ sơ sáng chế này đi đi. Muốn làm gì thì cứ việc làm. Nhưng hãy luôn ghi nhớ một điều cốt lõi: bài thuốc này sinh ra là để chữa bệnh cứu người - chứ không phải là công cụ đơn thuần để kiếm tiền vinh thân phù gia. Con có thực sự hiểu rõ lời tao nói không?"

"Con hiểu thấu đáo rồi ạ." Khải cung kính trả lời.

"Chưa chắc con đã hiểu hết đâu." Cụ Đạo nói khẽ bằng giọng trầm ngâm. "Nhưng rồi dòng đời xô đẩy sẽ bắt con phải hiểu."

Chiều muộn hôm đó, khi Khải vừa bước ra khỏi nhà ông nội, anh nhận được một cuộc gọi điện thoại từ số máy bàn quen thuộc của bệnh viện Đa khoa Hà Thành.

Người gọi đến không phải là giám đốc Phạm Hoàng Vũ, mà chính là Tiến sĩ Ngô Quang Đức.

"Khải à." Giọng nói của Đức vang lên nhẹ nhàng và giả tạo theo đúng phong cách quen thuộc của gã. "Chúng ta là đồng nghiệp lâu năm, mình nghĩ nên nói chuyện thẳng thắn với nhau một lần cho rõ ràng nhé. Bài thuốc gan đó, mình biết thừa cậu đã âm thầm nghiên cứu thử nghiệm lâm sàng suốt ba năm qua tại khoa. Tội gì cậu phải một mình ôm khư khư lấy nó làm gì để rồi rước họa vào thân? Chỉ cần cậu đồng ý ký vào biên bản bàn giao nghiên cứu cho bệnh viện, tụi này cam kết sẽ chia phần trăm doanh thu thương mại cực kỳ sòng phẳng cho cậu - điều này mình có thể ký giấy bảo đảm riêng."

Khải kiên nhẫn lắng nghe toàn bộ những lời dụ dỗ dơ bẩn của Đức qua điện thoại.

"Ngô Quang Đức à." Anh lạnh lùng lên tiếng. "Mày có biết về luật sở hữu trí tuệ Việt Nam không?"

Một khoảng im lặng chết chóc kéo dài hai giây ở đầu dây bên kia.

"Ý cậu là sao?" Đức hỏi lại, giọng bắt đầu mất đi vẻ tự tin.

"Ông nội tao đã nộp hồ sơ đăng ký sáng chế độc quyền cho bài thuốc gan họ Lương lên Cục Sở hữu trí tuệ từ ngày 28 tháng 10 rồi. Số hồ sơ đăng ký chính thức là 2024-SHTT-04471. Và tao vừa được Cục bổ sung tên đồng tác giả sáng chế vào sáng ngày hôm nay." Giọng nói của Khải vẫn phẳng lặng, lạnh tanh như băng. "Mày muốn kiện cáo hay dùng thế lực gì để cướp đoạt thì cứ việc làm. Tao luôn sẵn sàng chờ đợi mày."

Đầu dây bên kia im lặng kéo dài một cách đáng sợ.

Rồi một tiếng "tút" khô khốc vang lên, Đức đã cúp máy đột ngột trong sự hoảng loạn tột cùng.
"""

    # CHAPTER 4 - Expanded to over 1150 words
    ch4 = """Ba tuần trôi qua kể từ ngày bị sa thải khỏi bệnh viện Hà Thành. Khải lúc này đang miệt mài làm việc trong phòng thí nghiệm R&D hiện đại của Tập đoàn Thiên Phúc thì chiếc điện thoại trên bàn bất ngờ đổ chuông. Tiếng chuông reo dồn dập phá tan bầu không khí tĩnh mịch, chỉ có tiếng vo vo đều đặn từ hệ thống máy lọc khí cao cấp của phòng thí nghiệm chuyên sâu.

Màn hình điện thoại hiển thị cái tên Nguyễn Thanh Hà. Đó là lần đầu tiên cô ta chủ động liên lạc với anh kể từ cái buổi sáng lạnh lùng tuyên bố đã đơn phương nộp đơn ly hôn lên tòa án ngay tại hành lang bệnh viện Đa khoa Hà Thành.

"Khải à... Chúng ta có thể gặp nhau nói chuyện một lát được không anh?" Giọng nói của Thanh Hà vang lên qua loa thoại nghe hoàn toàn khác lạ - nó không còn giữ được sự kiêu ngạo, điềm tĩnh và đầy toan tính của một người phụ nữ thực dụng như trước nữa. Thay vào đó là một sự run rẩy, hoang mang tột độ lộ rõ trong từng hơi thở đứt quãng của cô ta.

"Em có chuyện gì thì cứ nói thẳng qua điện thoại đi." Khải trả lời, tay vẫn lướt nhanh trên bàn phím máy tính, mắt không hề rời khỏi màn hình hiển thị biểu đồ phân tích hoạt chất sắc ký khí GC-MS.

"Anh... anh đang ở đâu vậy? Em thực sự muốn gặp trực tiếp anh để giải thích mọi chuyện..."

"Tôi đang làm việc tại phòng lab." Khải thản nhiên đáp.

Một giây im lặng ngập ngừng đầy bối rối ở đầu dây bên kia. "Anh... anh đã bị bệnh viện sa thải và tước giấy phép nghiên cứu nội bộ rồi mà, làm sao có thể tìm được công việc mới nhanh đến như thế được? Hơn nữa, chú Vũ nói rằng anh sẽ không thể xin việc ở bất kỳ cơ sở y tế nào tại Hà Nội nữa..."

"Đó là việc của Phạm Hoàng Vũ, còn tôi tự có lối đi riêng của mình." Khải lạnh lùng cắt lời cô ta. "Hà có chuyện gì cần nói thì hãy nói nhanh đi, tôi đang ở giữa ca chạy thử nghiệm hóa chất và không có thời gian để lãng phí cho những câu chuyện vô bổ."

Thanh Hà im lặng vài giây để cố gắng lấy lại sự bình tĩnh, rồi cô ta mếu máo nói bằng chất giọng nghẹn ngào đầy cay đắng: "Chú Vũ vừa mới đột ngột thông báo với em là sẽ cắt toàn bộ chi phí sinh hoạt hàng tháng của em. Anh cũng biết là hiện tại em đang phải sống nhờ trong căn hộ chung cư cao cấp đứng tên chú ấy ở khu Cầu Giấy mà... Bây giờ chú ấy đòi lại nhà, bắt em phải dọn đi ngay trong tuần này..."

"Tôi biết chuyện đó." Giọng nói của Khải vẫn phẳng lặng như mặt nước hồ mùa đông, không hề có một chút oán hận hay hả hê nào của kẻ trả thù, chỉ có sự rõ ràng đến đáng sợ. "Và đó hoàn toàn là vấn đề cá nhân giữa em và ông chú giám đốc của em. Nó hoàn toàn không liên quan gì đến cuộc sống hiện tại của tôi cả."

"Khải! Tại sao anh lại có thể trở nên tuyệt tình và tàn nhẫn như thế được chứ?" Thanh Hà hét lên qua điện thoại trong nước mắt. "Dù sao chúng ta cũng từng là vợ chồng suốt bốn năm trời cơ mà! Anh biết rõ Ngô Quang Đức đã lừa dối em đúng không? Sau khi gã lấy được hồ sơ nghiên cứu từ tài khoản của anh, gã đối xử với em hoàn toàn khác hẳn! Gã trở nên lạnh nhạt, patronize, thậm chí không thèm trả lời tin nhắn của em! Gã thẳng thừng nói rằng em không còn giá trị lợi dụng gì nữa khi gã đã nắm chắc bài thuốc trong tay! Em đã quá ngu ngốc khi tin lời gã..."

"Mọi thứ đều là do chính em tự lựa chọn và toan tính từ đầu." Khải dứt khoát ngắt lời cô ta bằng giọng điệu điềm tĩnh. "Em đã chọn đứng về phía kẻ mạnh, chọn tiền bạc và danh vọng ảo ảnh của Đức và Vũ. Tôi hoàn toàn tôn trọng và chấp nhận sự lựa chọn đó của em. Nhưng từ nay về sau, xin em đừng bao giờ gọi điện làm phiền tôi vì những tranh chấp tiền bạc hay tình cảm dơ bẩn của em nữa. Cửa đã đóng rồi, Hà ạ."

"Khải! Anh hãy nghe em giải thích một lần thôi—"

Khải không chần chừ thêm một giây nào, anh dứt khoát nhấn nút cúp máy, đặt chiếc điện thoại xuống mặt bàn thí nghiệm làm bằng vật liệu composite chống ăn mòn hóa chất. Anh tiếp tục tập trung cao độ vào màn hình, nơi các pic đỉnh sắc ký của bài thuốc đang hiện lên vô cùng rõ nét.

Anh chỉ tay vào các đỉnh hấp thụ (peaks) trên màn hình máy tính, quay sang giải thích chi tiết cho Trần Bảo Châu - người đã đứng lặng lẽ quan sát ở cửa phòng lab từ bao giờ: "Bảy hoạt chất chính trong bài thuốc gia truyền họ Lương liên kết với nhau theo một cơ chế hiệp đồng sinh học vô cùng kỳ diệu. Ba hoạt chất mới chưa từng xuất hiện trong y văn có khả năng kích hoạt trực tiếp các tế bào hình sao trong gan ngừng tăng sinh collagen dơ bẩn, đồng thời đẩy nhanh tốc độ tự tái tạo của các nhu mô gan lành lặn xung quanh. Đây chính là chìa khóa vàng giúp đảo ngược xơ gan hoàn toàn."

Bảo Châu chăm chú nghe, mười ngón tay thon dài gõ nhanh các thuật ngữ khoa học vào cuốn sổ tay da đen nhỏ. Cô khẽ mỉm cười, trao cho anh lon cà phê espresso đóng chai mát lạnh.

"Vợ cũ của anh có vẻ đang phải trải qua một bài học đắt giá về nhân quả." Bảo Châu nhẹ nhàng nói, mắt vẫn nhìn vào các chỉ số kỹ thuật trên màn hình.

"Đó là việc của cô ta." Khải thản nhiên mở nắp lon cà phê, nhấp một ngụm đắng ngắt nhưng sảng khoái. "Chúng ta chỉ cần tập trung vào việc hoàn thành kiểm định lâm sàng. Đó mới là giá trị cốt lõi."

Bảo Châu gật đầu đồng ý, ánh mắt cô hiện lên vẻ kính trọng sâu sắc đối với bản lĩnh và sự tập trung cao độ của người bác sĩ y học cổ truyền trước mặt.
"""

    # CHAPTER 5 - Expanded to over 1150 words
    ch5 = """Bước sang tuần thứ năm sau khi Khải rời khỏi bệnh viện Hà Thành, Hùng - người bạn thân thiết nhất từ thời đại học của anh, hiện đang đảm nhận vị trí kiểm toán viên cao cấp tại Deloitte Việt Nam - đột ngột gọi điện thoại cho anh vào lúc mười một giờ đêm muộn.

"Mày có đang rảnh và ở một mình không Khải? Tao bắt buộc phải gặp mày ngay." Giọng nói của Hùng qua điện thoại vô cùng nghiêm trọng và khẩn trương, hoàn toàn không còn vẻ cợt nhả, hay bông đùa thường ngày của cậu ta nữa.

"Tôi đang ở một mình tại căn hộ thuê. Có chuyện gì mà gấp gáp thế Hùng?" Khải hỏi.

"Tao có một vài tài liệu tài chính cực kỳ mật mà mày bắt buộc phải xem tận mắt ngay lập tức." Hùng nói nhanh. "Sáng mai đúng bảy giờ gặp nhau tại quán phở quen ở ngõ Đào Duy Từ nhé. Nhớ kỹ là đừng nói chuyện này với bất kỳ ai, kể cả Trần Bảo Châu."

Sáng hôm sau, bầu trời Hà Nội mù mịt sương muối lạnh giá, gió mùa đông rít từng hồi ngoài ngõ nhỏ, thổi bạt những chiếc lá bàng khô rụng xuống mặt đường xi măng ẩm ướt của phố cổ. Tại một chiếc bàn gỗ nhỏ nằm sâu trong góc quán phở nghi ngút khói ở ngõ Đào Duy Từ, tiếng băm hành, tiếng thìa đũa va chạm lách cách hòa cùng tiếng xuýt xoa của khách ăn phở tạo nên một không gian vô cùng đặc trưng. Hùng đẩy đĩa quẩy nóng hổi qua phía Khải, giục anh ăn cho ấm người trước khi bắt đầu bàn bạc công việc căng thẳng. Sau đó, Hùng lặng lẽ đặt lên bàn một chiếc USB màu đen nhỏ nhắn.

"Tháng trước, văn phòng Deloitte của tao được phía tập đoàn Thiên Phúc thuê để thực hiện một chiến dịch kiểm toán độc lập, rà soát lại toàn bộ các đối tác giao dịch lớn nhằm chuẩn bị cho đợt phát hành cổ phiếu mới." Hùng ngồi xuống, khẽ nhấp một ngụm trà nóng để xua tan cái lạnh. "Trong quá trình đối chiếu sổ sách tài chính chi tiết, tao đã vô tình phát hiện ra một loạt giao dịch chuyển tiền vô cùng bất thường từ tài khoản ngân hàng chính thức của bệnh viện Đa khoa Hà Thành sang một công ty shell mới thành lập tên là Đức Phát Pharma. Tao thấy nghi ngờ nên đã âm thầm điều tra sâu hơn vào hồ sơ đăng ký doanh nghiệp của công ty này và phát hiện ra Đức Phát Pharma do chính Ngô Quang Đức đứng tên sở hữu 100% cổ phần."

Khải chăm chú nhìn chiếc USB đặt trên bàn, ánh mắt sắc sảo.

"Số tiền giao dịch cụ thể là bao nhiêu?" anh hỏi.

"Đã có bốn lần chuyển khoản lớn được thực hiện liên tục trong vòng sáu tháng qua. Tổng số tiền lên đến 2,3 tỷ đồng." Hùng ghé sát tai Khải nói khẽ. "Ban đầu tao chỉ nghĩ đơn giản đây là những khoản tiền hoa hồng bẩn từ các nhà thầu dược phẩm thông thường. Nhưng sau đó tao tiếp tục tra cứu trên hệ thống thông tin của Cục Sở hữu trí tuệ và phát hiện ra công ty Đức Phát Pharma vừa nộp đơn đăng ký bảo hộ nhãn hiệu độc quyền cho một sản phẩm bổ gan mới tên là 'Hoàn Can Đạo'. Thành phần hoạt chất của nó thì mày thử tự đoán xem."

Dạ dày của Khải thắt chặt lại một cái lạnh buốt. Anh lập tức đoán ra câu trả lời.

"Bọn chúng đã đánh cắp toàn bộ công thức phối ngũ từ hồ sơ nghiên cứu nội bộ của tao khi tao còn làm việc tại bệnh viện." Khải lạnh lùng nói.

"Chính xác là như vậy." Hùng gật đầu xác nhận. "Hùng tỉ mỉ chỉ ra các bút toán chuyển tiền giả mạo được hạch toán dưới danh mục 'chi phí mua sắm vật tư y tế tiêu hao'. Bằng việc sử dụng nghiệp vụ phân tích dòng tiền chuyên sâu của Deloitte, tao đã dễ dàng bóc trần đường đi lắt léo của dòng tiền 2,3 tỷ đồng này từ quỹ phúc lợi bệnh viện Hà Thành chạy vòng qua hai tài khoản trung gian rồi đổ thẳng vào tài khoản ngân hàng của Đức Phát Pharma. Mọi bằng chứng đã được đóng dấu kiểm toán đỏ chói với mã số kiểm toán bảo mật DLV-2024-HN-09917."

"Nhưng bọn chúng lại phạm phải một sai lầm chết người vì quá vội vàng." Hùng cười lạnh. "Bọn chúng đăng ký nhãn hiệu sản phẩm sau ngày ông nội mày nộp hồ sơ đăng ký sáng chế độc quyền cho bài thuốc gia truyền họ Lương. Nếu tập hồ sơ sáng chế của ông nội mày được Cục xác nhận hợp lệ..."

"Ông nội tao đã chính thức nộp hồ sơ từ ngày 28 tháng 10." Khải nói rõ ràng. "Còn công ty Đức Phát của Đức nộp đơn đăng ký nhãn hiệu vào ngày nào?"

Hùng lật nhanh cuốn sổ tay kiểm toán: "Ngày 15 tháng 11. Đúng mười tám ngày sau khi mày bị sa thải khỏi bệnh viện Hà Thành. Đây là bằng chứng thép không thể chối cãi."

Khải khẽ cầm chiếc USB màu đen lên, nắm chặt trong lòng bàn tay.

"Hùng, mày lấy được những tài liệu giao dịch mật này từ đâu? Có vi phạm quy định bảo mật thông tin kiểm toán của Deloitte không?" Khải lo lắng cho bạn mình.

"Mày yên tâm đi, tao chỉ làm đúng nghiệp vụ chuyên môn của mình thôi." Hùng nhún vai cười tự tin. "Theo đúng các điều khoản trong hợp đồng kiểm toán độc lập ký giữa Deloitte và Thiên Phúc, tao hoàn toàn có quyền yêu cầu cung cấp tài liệu tài chính từ bên đối tác thứ ba có phát sinh giao dịch thương mại lớn với Thiên Phúc. Bệnh viện Hà Thành từng bán một lô thiết bị y tế cũ trị giá hơn năm mươi tỷ cho Thiên Phúc từ hai năm trước. Vì vậy tao hoàn toàn có quyền yêu cầu họ cung cấp tài liệu đối chiếu tài khoản. Họ bắt buộc phải cung cấp đầy đủ theo luật định. Mọi tài liệu tao thu thập được đều hoàn toàn hợp pháp và có thể dùng làm chứng cứ trước tòa."

Khải nhìn chiếc USB trong tay. Bốn giao dịch chuyển tiền mờ ám, một công ty shell, đơn đăng ký nhãn hiệu trùng lặp hoạt chất. Đây chính là sợi chỉ đỏ đầu tiên giúp anh giật sập toàn bộ cái mạng nhện âm mưu bẩn thỉu của cha con Phạm Hoàng Vũ và Ngô Quang Đức.

"Tôi cần một luật sư xuất sắc." Khải nói.

"Tao đã chủ động liên hệ trước cho mày rồi." Hùng rút từ ví ra một tấm danh thiếp sang trọng. "Văn phòng Luật sư Minh Đức & Partners. Họ là những chuyên gia hàng đầu tại Việt Nam về sở hữu trí tuệ và tranh chấp y tế. Họ đã đồng ý thu xếp thời gian gặp mày vào chiều ngày mai."
"""

    # CHAPTER 6
    ch6 = """Hai tháng sau ngày bị sa thải khỏi bệnh viện Hà Thành.

Phòng họp lớn của Cục Sở hữu trí tuệ thuộc Bộ Khoa học và Công nghệ, nằm trên tầng mười hai của tòa nhà văn phòng hiện đại trên phố Ngụy Như Kon Tum. Mười một người đang ngồi nghiêm túc vây quanh một chiếc bàn dài phủ lớp nỉ màu xanh lá cây sang trọng.

Phía bên nguyên đơn gồm có Lương Minh Khải, Trần Bảo Châu, luật sư Minh Đức và cụ Lương Văn Đạo. Cụ Đạo mặc một bộ quần áo vải thô màu nâu giản dị, ngồi thẳng lưng trên chiếc ghế đệm với phong thái điềm tĩnh, ung dung tự tại như một thiền sư.

Phía bên bị đơn gồm có Tiến sĩ Ngô Quang Đức, Giám đốc Phạm Hoàng Vũ, luật sư đại diện pháp lý của họ và hai người đại diện cho công ty Đức Phát Pharma.

Hội đồng xem xét tranh chấp sáng chế của Cục gồm có ba vị chuyên gia dược học đầu ngành và một vị đại diện ban lãnh đạo Cục Sở hữu trí tuệ làm chủ tọa.

Ngô Quang Đức ngồi đối diện với Khải với một nụ cười vô cùng tự tin của một kẻ đã chuẩn bị kỹ lưỡng mọi kịch bản. Gã mang theo một bộ hồ sơ nghiên cứu dày cộp chia làm ba tập lớn, bản phân tích định lượng thành phần hoạt chất chi tiết và một tờ giấy ủy quyền sở hữu trí tuệ có chữ ký đóng dấu chính thức của Giám đốc bệnh viện Hà Thành.

"Chúng tôi khẳng định công thức sản phẩm Hoàn Can Đạo hoàn toàn là kết quả nghiên cứu độc lập của Tiến sĩ Ngô Quang Đức trong suốt thời gian dài công tác tại bệnh viện Hà Thành." Luật sư của phía bị đơn mở đầu bài trình bày bằng giọng điệu đanh thép. "Bằng chứng pháp lý rõ ràng nhất là cuốn nhật ký nghiên cứu nội bộ của khoa y học cổ truyền đã được ban giám đốc bệnh viện kiểm tra và đóng dấu xác nhận chính thức từ hai năm trước."

Vị đại diện Cục Sở hữu trí tuệ khẽ mở tập hồ sơ vụ việc ra. "Ý kiến của phía nguyên đơn về cáo buộc này thế nào?"

Luật sư Minh Đức đứng dậy vô cùng lịch sự. Ông từ từ đặt lên mặt bàn nỉ xanh ba thứ tài liệu quan trọng: chiếc hộp gỗ sơn then đen cổ kính chứa bản gốc bài thuốc gia truyền họ Lương viết bằng chữ Nho từ năm 1948, bản dịch thuật y khoa cổ có công chứng pháp lý kèm theo tờ xác nhận tính xác thực lịch sử của Hội đồng Sử học Việt Nam, và cuối cùng là bản kết quả phân tích sắc ký khí GC-MS cực kỳ chi tiết của phòng lab Thiên Phúc đã được kiểm định và đóng dấu xác nhận độc lập bởi Viện Kiểm nghiệm thuốc Trung ương.

"Bài thuốc gia truyền của dòng họ Lương - nguyên bản từ năm 1948 - sở hữu cấu trúc phối ngũ gồm bảy hoạt chất sinh học chủ chốt, trong đó có ba hoạt chất hoàn toàn chưa từng được mô tả trong y văn hiện đại." Luật sư Minh Đức chỉ tay vào bảng so sánh cấu trúc hóa học được chiếu trên màn hình lớn. "Công thức sản phẩm Hoàn Can Đạo của phía bị đơn cũng sở hữu chính xác bảy hoạt chất sinh học đó, với tỷ lệ phối ngũ trùng khớp hoàn toàn, sai lệch định lượng dưới mức 3%. Đây tuyệt đối không thể là một sự trùng hợp nguyên nhiên trong nghiên cứu khoa học độc lập được."

Đức khẽ nhíu mày, nụ cười trên môi gã bắt đầu đông cứng lại một chút, nhưng gã vẫn cố giữ vẻ bình tĩnh tự tin.

"Sự trùng hợp trong nghiên cứu khoa học thực nghiệm là điều hoàn toàn có thể xảy ra..." Đức cố cãi cọ.

"Thưa hội đồng khoa học." Trần Bảo Châu bất ngờ lên tiếng. Giọng nói của cô không hề cao giọng hay gay gắt, nhưng âm lượng vừa đủ và vô cùng đanh thép khiến cả phòng họp lập tức im lặng phăng phắc. "Tôi xin phép được bổ sung thêm các bằng chứng pháp lý quan trọng khác."

Cô mở chiếc laptop cá nhân của mình, kết nối trực tiếp với máy chiếu của phòng họp và hiển thị lên màn hình lớn: bản sao sao kê lịch sử giao dịch tài khoản ngân hàng chính thức của bệnh viện Đa khoa Hà Thành - có đóng dấu đỏ xác nhận của ngân hàng BIDV - với bốn giao dịch chuyển tiền lớn mờ ám sang tài khoản của công ty shell Đức Phát Pharma do Ngô Quang Đức sở hữu.

Tiếp theo là đơn đăng ký bảo hộ nhãn hiệu Hoàn Can Đạo của Đức Phát Pharma với ngày nộp chính thức là 15/11, tức là sau ngày Lương Minh Khải bị sa thải khỏi bệnh viện đúng 18 ngày.

And cuối cùng, chấn động nhất, chính là bản nhật ký commit Git được trích xuất trực tiếp từ máy chủ nội bộ của bệnh viện Hà Thành - được khôi phục hoàn hảo bởi chuyên gia pháp chứng kỹ thuật số độc lập. Nhật ký hệ thống ghi rõ: file hồ sơ nghiên cứu bài thuốc gan của bác sĩ Lương Minh Khải đã bị tài khoản cá nhân của Tiến sĩ Ngô Quang Đức truy cập trái phép và tải xuống vào lúc 23 giờ 15 phút ngày 5 tháng 11.

Cả phòng họp của Cục Sở hữu trí tuệ lập tức rơi vào một khoảng im lặng chết chóc đến đáng sợ.

Gương mặt của Ngô Quang Đức biến sắc hoàn toàn, nét mặt gã tái mét không còn một giọt máu. Cơ má bên trái của gã khẽ giật lên liên hồi một cách mất kiểm soát - một chi tiết rất nhỏ nhưng Khải ngồi đối diện đã thu trọn vào tầm mắt của mình.

"Đây hoàn toàn là những tài liệu giả mạo bôi nhọ danh dự..." Luật sư của Đức cố gắng lên tiếng bào chữa trong tuyệt vọng.

"Chữ ký xác nhận kiểm toán ở cuối mỗi trang tài liệu tài chính này là của Deloitte Việt Nam." Bảo Châu lạnh lùng nói rõ ràng. "Mã xác minh audit trail quốc tế là DLV-2024-HN-09917. Hội đồng khoa học hoàn toàn có thể tự tra cứu trực tiếp mã số này trên cổng thông tin điện tử chính thức của Deloitte toàn cầu ngay tại đây."

Phạm Hoàng Vũ - lần đầu tiên kể từ khi buổi họp bắt đầu - từ từ quay sang nhìn Ngô Quang Đức bằng ánh mắt đầy giận dữ và hoảng hốt. Đó là ánh mắt của một kẻ cầm lái vừa nhận ra gã đồng hành của mình đã bí mật đục một chiếc lỗ lớn dưới đáy thuyền từ lúc nào.

Vị đại diện Cục Sở hữu trí tuệ gõ mạnh chiếc bút xuống bàn họp.

"Hội đồng khoa học của Cục sẽ tiến hành họp kín riêng để đưa ra quyết định cuối cùng. Đề nghị các bên tạm thời di chuyển ra phòng chờ bên ngoài."
"""

    # CHAPTER 7 - Expanded to over 1150 words
    ch7 = """Hai mươi phút trôi qua trong sự căng thẳng tột độ ở hành lang phòng chờ của Cục Sở hữu trí tuệ. Cánh cửa gỗ lớn của phòng họp cuối cùng cũng từ từ mở ra, tiếng bản lề kim loại kêu cót két khẽ vang lên trong không gian yên tĩnh.

Tiến sĩ Ngô Quang Đức bước ra ngoài đầu tiên. Nụ cười kiêu ngạo thường ngày của gã đã hoàn toàn biến mất, đôi môi gã mím chặt lại thành một đường thẳng, hai bên khóe miệng kéo trễ xuống đầy thảm hại. Hai bàn tay gã đút sâu vào túi quần comple để che giấu sự run rẩy dữ dội của các ngón tay trước ánh mắt dò xét của mọi người.

Bước theo sau gã là Giám đốc Phạm Hoàng Vũ. Ông ta bước đi vô cùng chậm chạp, đôi chân như bị đeo thêm hàng chục cân xích sắt nặng nề, gương mặt xám xịt như tro tàn, không còn vẻ oai phong lẫm liệt của vị giám đốc bệnh viện lớn ngày nào.

Vị đại diện Cục Sở hữu trí tuệ dõng dạc đọc văn bản quyết định chính thức trước toàn thể mọi người:

"Hội đồng khoa học của Cục Sở hữu trí tuệ chính thức xác nhận: hồ sơ đăng ký sáng chế độc quyền số 2024-SHTT-04471 của đồng tác giả Lương Văn Đạo và Lương Minh Khải có đầy đủ tính ưu tiên pháp lý về ngày nộp hồ sơ hợp lệ và tính mới tuyệt đối về đối tượng bảo hộ khoa học. Đơn đăng ký nhãn hiệu sản phẩm Hoàn Can Đạo của công ty Đức Phát Pharma chính thức bị từ chối hoàn toàn. Toàn bộ hồ sơ vụ việc có dấu hiệu vi phạm nghiêm trọng quyền sở hữu trí tuệ và gian lận hồ sơ khoa học y tế sẽ được Cục chuyển giao trực tiếp sang cơ quan cảnh sát điều tra để xử lý nghiêm theo đúng quy định của pháp luật hiện hành."

Cơ quan cảnh sát điều tra. Hai chữ ấy vang lên dõng dạc và đanh thép, đập tan mọi hy vọng cuối cùng của Ngô Quang Đức và Phạm Hoàng Vũ.

Khải đứng lặng yên giữa hành lang lộng gió của tòa nhà trên phố Ngụy Như Kon Tum, nghe rõ từng lời tuyên bố ấy mà trong lòng không hề có một cảm xúc chiến thắng hay hả hê nào. Anh chỉ đơn giản cảm thấy mình vừa đặt được một viên gạch nền móng đầu tiên về đúng vị trí vốn có của nó sau bao ngày bị xô lệch bởi những âm mưu bẩn thỉu.

Đúng ba ngày sau buổi lật bàn chấn động tại Cục Sở hữu trí tuệ, Khải nhận được văn bản thông báo chính thức từ Cơ quan Cảnh sát điều tra tội phạm về tham nhũng, kinh tế, buôn lậu (C03) thuộc Bộ Công an. Văn bản nêu rõ: vụ án hình sự liên quan đến hành vi chiếm đoạt tài sản trí tuệ quy mô lớn, gian lận hồ sơ y tế và cố ý làm trái quy định nhà nước xảy ra tại Bệnh viện Đa khoa Hà Thành và công ty Đức Phát Pharma đã chính thức được khởi tố điều tra vụ án và khởi tố bị can đối với Phạm Hoàng Vũ và Ngô Quang Đức.

Khải nghe kể chi tiết từ Hùng qua điện thoại rằng, ngay chiều hôm qua, hai chiếc xe biển xanh của lực lượng Cảnh sát Kinh tế (C03) đã đỗ xịch trước sảnh chính bệnh viện Hà Thành. Các trinh sát mặc cảnh phục đã bước vào phòng làm việc của giám đốc Phạm Hoàng Vũ và niêm phong toàn bộ tài liệu kế toán, ổ cứng máy tính nội bộ. Ngô Quang Đức cũng bị áp giải ra xe trong trạng thái hoảng loạn tột độ, tay che mặt trước những ống kính điện thoại của các y bác sĩ và bệnh nhân hiếu kỳ xung quanh. Cả bệnh viện Hà Thành như nổ tung trước thông tin động trời này.

Toàn bộ tài khoản ngân hàng cá nhân và tài khoản doanh nghiệp của công ty Đức Phát Pharma đã lập tức bị phong tỏa hoàn toàn để phục vụ công tác điều tra phá án chuyên sâu.

Chiều hôm đó, Nguyễn Thanh Hà gửi tin nhắn thứ ba cho anh.

Khải không hề bấm vào đọc tin nhắn ngay lập tức. Anh đang ngồi thư thái trong phòng khách ấm cúng của nhà ông nội ở phố Hàng Bồ, cùng ông uống những chén trà sen thơm ngát đầu mùa và nhìn ngắm con hẻm nhỏ quen thuộc qua ô cửa sổ bằng gỗ bạc màu. Mùi hương trà sen Tây Hồ dịu ngọt lan tỏa khắp căn phòng khách lát gạch hoa cổ kính. Cụ Đạo lấy chiếc kẹp tre khẽ gắp những nhị hoa sen vàng óng bỏ vào trong chén trà, rồi từ từ rót nước sôi. Dòng nước ấm nóng bốc hơi nghi ngút, phản chiếu ánh sáng nhạt nhòa của buổi chiều đông Hà Nội.

"Mọi chuyện coi như đã xong xuôi rồi phải không con?" Cụ Đạo nhẹ nhàng hỏi, tay khẽ đặt chén trà xuống bàn.

"Vẫn chưa hoàn toàn xong hẳn đâu ông ạ. Quá trình điều tra hình sự của C03 chắc chắn sẽ còn kéo dài rất nhiều tháng. Nhưng quyền sở hữu bài thuốc của dòng họ mình thì đã được bảo vệ tuyệt đối rồi." Khải nhìn vào làn khói trà nghi ngút. "Có những lúc con đã tự trách bản thân mình thật sự sai lầm khi quyết định mang bài thuốc gia truyền này vào áp dụng tại bệnh viện Hà Thành."

"Con hoàn toàn không hề sai khi muốn dùng y thuật cứu người." Cụ Đạo rót thêm nước nóng vào ấm trà sen. "Sai lầm duy nhất của con là đã đặt niềm tin nhầm chỗ vào những kẻ tiểu nhân tham lam mà thôi. Hai việc đó hoàn toàn khác nhau về bản chất, con cần phải phân định cho rõ ràng."

Khải im lặng gật đầu, lòng nhẹ nhõm đi rất nhiều.

"Chú thím của con cả đời làm nghề bốc thuốc nam, ông nội con và cụ cố con cũng vậy. Dòng họ Lương nhà mình chưa từng có một ai trở nên giàu có nứt đố đổ vách nhờ bài thuốc gan này cả." Cụ Đạo đặt ấm trà xuống mặt bàn gỗ cổ. "Nhưng quan trọng nhất là dòng họ nhà mình chưa từng có một ai phải chết hay chịu cảnh tù tội vì bài thuốc đó cả. Lương tâm của người thầy thuốc luôn sạch sẽ."

Khải từ từ lấy chiếc điện thoại cũ ra, mở hộp thư tin nhắn của Nguyễn Thanh Hà lên.

"Chú Vũ vừa mới bị cơ quan công an bắt tạm giam sáng nay rồi anh Khải ơi. Anh Ngô Quang Đức cũng đã bị triệu tập khẩn cấp phục vụ điều tra. Em... em thực sự hoảng loạn quá, anh có thể bớt chút thời gian gặp em một lát được không?"

Khải lặng lẽ đọc hết từng chữ trong tin nhắn của người vợ cũ.

Anh nhẹ nhàng tắt màn hình điện thoại, đặt nó nằm im lìm trên mặt bàn trà.

Anh từ từ nâng chén trà sen thơm ngát lên nhấp một ngụm nhỏ đầy tĩnh lặng.

Anh hoàn toàn không nhắn tin trả lời cô ta.
"""

    # CHAPTER 8
    ch8 = """Bốn tháng sau ngày bị sa thải khỏi bệnh viện Hà Thành.

Lễ ký kết hợp đồng hợp tác chiến lược toàn diện giữa Công ty TNHH Lương Gia Dược và Tập đoàn Dược phẩm Thiên Phúc được diễn ra trang trọng tại phòng họp VIP nằm trên tầng mười hai của tòa nhà Keangnam Landmark 72 sang trọng bậc nhất Hà Nội. Đó hoàn toàn không phải là một buổi tiệc lớn ồn ào với hàng trăm phóng viên báo chí đưa tin rầm rộ, mà chỉ là một buổi lễ ký kết nội bộ ấm cúng với sự tham dự của đúng mười hai người có liên quan trực tiếp.

Bản hợp đồng ghi rõ: Tập đoàn Thiên Phúc sẽ nắm giữ 30% cổ phần công thức sản phẩm bổ gan mới, đổi lại họ sẽ chịu trách nhiệm chi trả toàn bộ chi phí nghiên cứu phát triển, quy trình sản xuất đạt chuẩn y tế GMP, thử nghiệm lâm sàng nghiêm ngặt, đăng ký giấy phép lưu hành chính thức tại Bộ Y tế và xây dựng hệ thống phân phối trên toàn quốc. Công ty Lương Gia Dược do dòng họ Lương sở hữu sẽ giữ vững 70% cổ phần còn lại, đồng thời sở hữu toàn quyền kiểm soát thương hiệu sản phẩm và quy trình kiểm định chất lượng nguồn dược liệu đầu vào.

Cụ Lương Văn Đạo ngồi trang nghiêm ở vị trí đầu bàn họp lớn. Cụ mặc một bộ áo the truyền thống màu nâu đất giản dị nhưng vô cùng sang trọng, từ từ đặt bút ký tên mình bằng nét mực đen sắc sảo vào bản hợp đồng chiến lược.

Bàn tay của cụ khẽ run nhẹ một chút khi đặt bút ký - đó hoàn toàn không phải là sự run rẩy vì xúc động hay già yếu, mà là di chứng vật lý còn sót lại sau một cơn đột quỵ nhẹ vào năm ngoái, một sự cố sức khỏe nghiêm trọng mà trước đây không một ai trong ban giám đốc bệnh viện Hà Thành bận tâm muốn biết.

Sau khi các bên hoàn tất thủ tục ký kết hợp đồng, Trần Bảo Châu chủ động đứng dậy, lịch sự bắt tay chúc mừng từng thành viên của Lương Gia Dược.

Khi bước đến lượt của Lương Minh Khải, cô khẽ giữ chặt bàn tay anh lại thêm một giây đầy ẩn ý.

"Kết quả kiểm định lâm sàng giai đoạn một của bài thuốc gan vừa mới được gửi về văn phòng tôi sáng nay." Cô nói khẽ bằng giọng điệu vừa đủ cho hai người nghe. "Hiệu quả thực tế trên việc đảo ngược quá trình xơ hóa tế bào gan đạt tỷ lệ kinh ngạc: 71% số ca bệnh có sự cải thiện rõ rệt có ý nghĩa thống kê y khoa cực kỳ cao chỉ sau 12 tuần điều trị thử nghiệm. Kết quả này thực sự tốt hơn rất nhiều so với những gì tôi từng kỳ vọng ban đầu."

"Nhưng nó hoàn toàn nằm trong dự tính khoa học của tôi." Khải mỉm cười nhẹ nhàng đáp lại.

Bảo Châu chăm chú nhìn anh trong một giây ngắn ngủi. Cô không hỏi thêm bất kỳ câu hỏi chuyên môn thừa thãi nào nữa. Nhưng khóe miệng thanh tú của cô khẽ nhúc nhích tạo nên một đường cong vô cùng nhẹ nhàng - đó hoàn toàn không phải là một nụ cười rạng rỡ thường thấy, nhưng nó là biểu cảm gần gũi và ấm áp nhất mà Khải từng thấy xuất hiện trên gương mặt lạnh lùng của nữ CFO sắc sảo này suốt bốn tháng qua.

Chiều muộn hôm đó, khi tất cả mọi người tham dự buổi lễ ký kết đã rời đi hết, Khải vẫn lặng lẽ ngồi lại một mình trong phòng họp lớn yên tĩnh của tòa nhà Keangnam.

Anh nhẹ nhàng mở chiếc điện thoại cá nhân của mình lên.

Tin nhắn gửi đến từ Nguyễn Thanh Hà từ ba tháng trước vẫn nằm im lìm trong hộp thư lưu trữ - hoàn toàn chưa từng được anh trả lời:

"Khải à... Tiến sĩ Ngô Quang Đức thực ra chỉ là một kẻ lừa đảo đê tiện vô liêm sỉ, gã chỉ muốn lợi dụng em và gia thế của chú Vũ để tiến thân mà thôi. Đến tận bây giờ em mới nhận ra bộ mặt thật dơ bẩn của gã thì mọi chuyện đã quá muộn màng rồi. Em thực sự xin lỗi anh vô cùng vì tất cả những sai lỗi nông nổi trước đây. Anh... anh có thể nể tình nghĩa vợ chồng cũ mà cho em một cơ hội duy nhất để chúng ta gặp mặt nói chuyện trực tiếp được không anh?"

Khải chăm chú đọc lại từng câu chữ trong tin nhắn xin lỗi muộn màng của người vợ cũ một lần nữa. Lần này, anh đọc vô cùng kỹ lưỡng từng từ một chứ không lướt qua như trước.

Rồi anh nhẹ nhàng nhấn nút xóa vĩnh viễn tin nhắn đó khỏi bộ nhớ điện thoại của mình.

Anh thực hiện hành động đó hoàn toàn không phải vì lòng còn vương vấn sự tức giận, thù hận hay oán trách cô ta. Mà đơn giản là vì anh nhận ra sâu sắc một quy luật của cuộc đời: có những lời xin lỗi được gửi đi đúng lúc sẽ cứu vãn được một mối quan hệ - và có những lời xin lỗi chỉ được gửi đến sau khi cánh cửa ngăn cách giữa hai người đã hoàn toàn được đóng chặt lại từ lâu.

Khải khẽ đứng dậy, cầm chiếc áo khoác đen lên sải bước đi ra phía ngoài sảnh tòa nhà.

Hà Nội vào những ngày tháng Ba đã bắt đầu đón nhận những luồng hơi ấm áp của mùa xuân. Ánh nắng vàng óng ả, loãng nhẹ đổ xuống mặt hồ Tây rộng lớn phía xa xa, những con sóng nhỏ gợn lăn tăn trên mặt nước tựa như nhịp thở nhẹ nhàng của đất trời.

Chiếc điện thoại trong túi áo anh bất ngờ rung lên.

Đó là cuộc gọi từ Trần Bảo Châu.

"Anh Khải, anh đang ở đâu vậy?"

"Tôi đang đứng ngắm hồ Tây." Khải trả lời.

"Tôi cũng đang ở đây." Đầu dây bên kia dừng lại một giây ngắn ngủi. "Căn hộ của gia đình tôi nằm ngay mặt đường ven hồ Tây này."

Khải khẽ đưa mắt nhìn về phía dãy nhà biệt thự sang trọng chạy dọc ven hồ.

"Tôi chưa từng nghe cô nói về việc này bao giờ." anh mỉm cười nói.

"Vì trước đây tôi chưa từng nghĩ có lý do cần thiết để chia sẻ nó với anh." Giọng nói của cô khẽ vang lên ấm áp hơn thường lệ qua điện thoại. "Anh có muốn... ghé qua nhà tôi uống một chén trà nóng không? Tôi vừa mới tự tay pha xong một ấm trà ngon."

Đó hoàn toàn không phải là một lời mời chào khách sáo mang tính chất xã giao, cũng chẳng phải là một kịch bản ngôn tình lãng mạn. Đó chỉ đơn thuần là một câu hỏi vô cùng giản dị của một người phụ nữ vừa pha xong một ấm trà ngon và chợt nhận ra lượng trà nhiều hơn một người có thể uống hết.

Nhưng đó cũng là khoảnh khắc đầu tiên Lương Minh Khải nhận ra: Trần Bảo Châu đã chủ động mở lời mời ai đó bước vào không gian sống riêng tư của mình mà hoàn toàn không kèm theo bất kỳ một điều khoản thương mại hay lợi ích kinh doanh nào.

Khải nhẹ nhàng cất chiếc điện thoại vào túi quần.

Rồi anh từ từ sải bước chân đi bộ dọc theo con đường ven hồ Tây lộng gió, hướng về phía ánh nắng xuân ấm áp đang rạng rỡ phía trước.
"""

    novel_blueprint["chapters"].append({
        "title": "Chương 1: Ngày Bị Đuổi Và Ngày Bị Phụ Bạc",
        "content": clean_and_format_content(ch1)
    })
    novel_blueprint["chapters"].append({
        "title": "Chương 2: Người Đàn Bà Không Cứu Người Vì Từ Tâm",
        "content": clean_and_format_content(ch2)
    })
    novel_blueprint["chapters"].append({
        "title": "Chương 3: Bài Thuốc Bốn Đời Và Kẻ Muốn Đánh Cắp",
        "content": clean_and_format_content(ch3)
    })
    novel_blueprint["chapters"].append({
        "title": "Chương 4: Vợ Cũ Và Vị Khách Không Mời",
        "content": clean_and_format_content(ch4)
    })
    novel_blueprint["chapters"].append({
        "title": "Chương 5: Kẻ Phản Bội Và Bằng Chứng",
        "content": clean_and_format_content(ch5)
    })
    novel_blueprint["chapters"].append({
        "title": "Chương 6: Hội Đồng Khoa Học Và Ngày Lật Bàn",
        "content": clean_and_format_content(ch6)
    })
    novel_blueprint["chapters"].append({
        "title": "Chương 7: Đầu Gối Bủn Rủn Và Báo Cáo C03",
        "content": clean_and_format_content(ch7)
    })
    novel_blueprint["chapters"].append({
        "title": "Chương 8: Giá Trị Thật Và Một Cái Bắt Tay Nữa",
        "content": clean_and_format_content(ch8)
    })

    # Verifications
    for i, ch in enumerate(novel_blueprint["chapters"]):
        word_cnt = count_words(ch["content"])
        print(f"✓ Chapter {i+1} total words: {word_cnt}")
        if not (1000 <= word_cnt <= 1500):
            print(f"⚠️ WARNING: Chapter {i+1} has {word_cnt} words. Out of gold standard [1000 - 1500] range!")

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(novel_blueprint, f, ensure_ascii=False, indent=2)
        
    print(f"🎉 SUCCESS! Completed V13 gold standard direct expansion for {novel_blueprint['title']}")
    print(f"Saved complete novel file to: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
