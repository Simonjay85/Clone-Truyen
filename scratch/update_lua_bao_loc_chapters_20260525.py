#!/usr/bin/env python3
import ftplib
import json
from pathlib import Path

import requests


FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"
WP_URL = "https://doctieuthuyet.com"
SECRET = "ZEN_TRUYEN_2026_BYPASS"
OUT_DIR = Path("scratch/chatgpt_covers_3954_3998_4036_20260525")

UPDATES = {
    4005: {
        "title": "Chương 6: Chiếc Bẫy Hóa Chất Và Sự Thật Phơi Bày",
        "content": """<p>24 giờ đình chỉ hoạt động trôi qua nhanh chóng, nhưng với Trần Duy Anh, từng phút trong khoảng thời gian đó dài như một sợi tơ bị kéo căng đến mức sắp đứt. Bên ngoài cổng xưởng Bảo Lộc Ngọc Ty, phóng viên dựng máy quay từ sáng sớm. Vài hộ dân trồng dâu đứng nép dưới mái hiên, mắt đỏ hoe vì sợ hợp đồng thu mua kén tằm bị hủy. Một bà cụ đưa cho Duy Anh chiếc khăn lụa cũ đã bạc màu, giọng run run: “Nếu xưởng của con sập, cả làng này cũng mất mùa theo.”</p>
<p>Duy Anh nắm chặt chiếc khăn. Anh không nói lời hứa suông. Anh chỉ mở chiếc hộp chống nước, bên trong là ba mẫu nước thải được niêm phong bằng tem của Sở Tài nguyên Môi trường, một ổ cứng chứa dữ liệu cảm biến pH mười hai tháng, và bản nhật ký men sinh học có chữ ký xác nhận của hợp tác xã Da Nhim. Lê Minh Thư đứng cạnh anh, áo vest đen ướt mưa, nhưng ánh mắt tỉnh táo đến lạnh người. Cô nói nhỏ: “Hôm nay không chỉ cứu một xưởng dệt. Hôm nay phải khiến họ không còn đường quay lại cắn ngược.”</p>
<p>Đúng chín giờ, kết quả phân tích mẫu nước thải của Bảo Lộc Ngọc Ty từ Viện Pasteur và Sở Tài nguyên Môi trường được công bố chính thức trước sự ngỡ ngàng của truyền thông. Nước thải sau nhuộm của xưởng đạt tiêu chuẩn nước sinh hoạt loại A, nhờ sử dụng công nghệ men sinh học phân hủy hữu cơ độc quyền của Trần Duy Anh. Không hề có bất kỳ hóa chất độc hại nào được xả ra môi trường. Lệnh đình chỉ bị hủy bỏ lập tức, tài khoản Vietcombank của công ty cũng được giải tỏa sau khi cơ quan thuế xác nhận sổ sách kế toán minh bạch.</p>
<p>Đám phóng viên vừa quay sang Duy Anh thì một chiếc xe màu đen lao tới trước cổng. Lâm Thế Vinh bước xuống, vẫn mặc bộ vest xám đắt tiền, trên miệng còn giữ nụ cười khinh miệt. Hắn giơ điện thoại lên trước mặt mọi người: “Một bản xét nghiệm không chứng minh được gì. Tao có nhân chứng nói chính mày đã tráo mẫu trước khi gửi đi.”</p>
<p>Cả sân xưởng im phăng phắc. Một công nhân trẻ từng làm ở Bảo Lộc Ngọc Ty bị Vinh kéo ra, mặt trắng bệch, lắp bắp nói Duy Anh từng yêu cầu anh ta đổi can nước thải vào đêm trước thanh tra. Cú đánh này hiểm độc hơn mọi lời vu khống trước đó, bởi nó đánh thẳng vào lòng tin vừa mới được khôi phục.</p>
<p>Duy Anh nhìn người công nhân trẻ. Anh nhận ra vết bầm ở cổ tay cậu ta và ánh mắt né tránh về phía chiếc xe của Vinh. Anh không nổi giận. Anh chỉ hỏi: “Mẹ em còn nằm viện ở khoa thận đúng không?” Cậu công nhân sững người. Duy Anh mở một file ghi âm từ điện thoại dự phòng. Trong file, giọng Lâm Thế Vinh vang lên rõ ràng: “Ký giấy làm chứng đi. Tao trả viện phí cho mẹ mày. Nếu không, tao cho cả nhà mày khỏi sống ở Bảo Lộc nữa.”</p>
<p>Tiếng máy quay bắt đầu dồn dập. Người công nhân bật khóc ngay trước cổng xưởng. “Em xin lỗi anh Duy Anh. Em bị ép. Em không tráo mẫu. Em chỉ đứng ngoài cửa kho, họ bảo em học thuộc lời khai.”</p>
<p>Lê Minh Thư không để truyền thông kịp loạn nhịp. Cô bước lên, đặt thêm một tập hồ sơ xuống bàn thanh tra. Kết quả kiểm toán đột xuất của PwC tại Lâm Gia Tơ Lụa phơi bày một hố đen tài chính tàn khốc: Lâm Gia báo cáo thu mua 50 tấn kén tằm hảo hạng từ nông dân địa phương với trị giá hàng chục tỷ đồng, nhưng thực tế kho của họ chỉ có 2 tấn kén mục. Thay vào đó, PwC phát hiện hóa đơn nhập khẩu lậu 48 tấn sợi polyester tổng hợp giá rẻ cùng hàng chục thùng hóa chất nhuộm công nghiệp chứa amine thơm độc hại từ công ty vỏ bọc Vạn Phát Chemical.</p>
<p>Duy Anh tung tiếp đòn thứ hai: đoạn video camera ẩn do một công nhân cũ cung cấp. Màn hình dựng ngay giữa sân chiếu rõ Lâm Thế Vinh đang chỉ đạo kỹ thuật viên đổ những xô bột màu hóa học vào lò nhuộm và nói: “Cứ trộn đều sợi hóa học vào sợi tơ tằm theo tỷ lệ 8:2, dệt thật bóng lên rồi dán nhãn tơ tằm thiên nhiên 100%. Bọn nhà giàu chỉ nhìn bề ngoài thôi, không phát hiện ra đâu!”</p>
<p>Đòn thứ ba là bản sao kê tài khoản cá nhân của Lâm Thế Vinh tại Agribank, có dấu đỏ xác nhận của cơ quan điều tra, phơi bày khoản tiền huê hồng lậu 15 tỷ đồng từ nhà cung cấp hóa chất. Đòn thứ tư là báo cáo độc chất của Bệnh viện Đa khoa Lâm Đồng về chiếc khăn lụa gây sốc phản vệ cho Chủ tịch Lê Minh Triết. Từng tờ giấy được đưa ra không ồn ào, nhưng mỗi con dấu đỏ rơi xuống bàn lại như một nhát búa đóng vào chiếc quan tài danh tiếng của Lâm Gia.</p>
<p>Lâm Thế Vinh lùi một bước, khuôn mặt tái nhợt. Hắn vẫn cố gào lên rằng mọi thứ là giả. Nhưng phía sau hắn, hai cán bộ C03 đã bước xuống từ chiếc xe biển xanh. Một người đọc lệnh triệu tập khẩn cấp liên quan đến hành vi buôn lậu nguyên liệu, làm giả nhãn hàng hóa và xâm phạm sở hữu trí tuệ. Chiếc micro trên tay Vinh rơi xuống nền xi măng ướt, phát ra tiếng chát khô khốc.</p>
<p>Duy Anh nhìn đống sợi tơ bị ném dưới mưa từ ngày anh bị trục xuất. Anh cúi xuống nhặt một bó lên, giũ sạch bùn đất rồi đặt lại vào tay bà cụ trồng dâu. “Tơ thật không sợ nước bẩn,” anh nói, giọng khàn đi. “Chỉ sợ lòng người bẩn mà vẫn tự nhận mình là lụa.”</p>
<p>Tấm lưới pháp lý khép chặt quanh cổ Lâm Thế Vinh. Và lần đầu tiên sau nhiều tháng bị chà đạp, những người thợ Bảo Lộc không cúi đầu nữa. Họ đứng thẳng dưới mưa, nhìn kẻ từng nắm quyền sinh sát của cả phường dệt bị đưa đi trong tiếng máy quay và ánh đèn lạnh buốt.</p>""",
    },
    4007: {
        "title": "Chương 8: Quốc Bảo Tái Sinh Và Lời Ước Hẹn Trên Cao Nguyên",
        "content": """<p>Sau đêm lật kèo chấn động tại khách sạn Da Lat Palace, tập đoàn Lâm Gia Tơ Lụa rơi vào cảnh sụp đổ hoàn toàn. Cổ phiếu của họ bị bán tháo kịch sàn rồi đình chỉ giao dịch. Toàn bộ nhà xưởng, máy nhuộm và kho hóa chất bị niêm phong để phục vụ điều tra mở rộng đường dây buôn lậu của Lâm Thế Vinh. Những tấm biển “lụa thiên nhiên cao cấp” từng treo sáng rực trên các showroom bị tháo xuống trong sự im lặng ê chề.</p>
<p>Nhưng Duy Anh không thấy hả hê như anh từng tưởng. Sáng hôm sau, anh đứng trước cổng xưởng cũ của Lâm Gia, nhìn từng công nhân ôm thùng đồ đi ra. Có người từng cười nhạo anh, có người từng im lặng khi anh bị bảo vệ kéo lê dưới mưa. Bây giờ họ tránh mắt anh, không biết nên xin lỗi hay oán trách. Duy Anh chỉ bảo Lê Minh Thư lập một quỹ hỗ trợ chuyển việc cho những thợ dệt không liên quan đến đường dây hóa chất. “Sai là ban lãnh đạo,” anh nói. “Bàn tay người thợ không đáng bị chặt theo lòng tham của ông chủ.”</p>
<p>Quyết định ấy khiến nhiều người bất ngờ. Ngay cả Minh Thư cũng nhìn anh rất lâu. Cô từng quen với những thương vụ thắng thua dứt khoát, nơi bên thua bị loại khỏi bàn cờ không thương tiếc. Nhưng ở Duy Anh, cô nhìn thấy thứ còn bền hơn lợi nhuận: sự tử tế đủ cứng để không bị lợi dụng, nhưng cũng đủ ấm để giữ lại con người.</p>
<p>Ba tuần sau, Bảo Lộc Ngọc Ty mở lại xưởng trong tiếng máy dệt vang đều như nhịp tim. Không còn những dây chuyền bóng loáng để khoe mẽ, chỉ có khung cửi, bồn men sinh học, phòng kiểm nghiệm nhỏ và một bức tường kính để khách hàng nhìn thấy toàn bộ quy trình nhuộm thảo mộc. Những hộ dân Da Nhim mang kén tằm đến xếp hàng trước cổng. Bà cụ từng đưa chiếc khăn cũ cho Duy Anh nay dắt theo cháu gái, mắt rưng rưng khi nhận hợp đồng thu mua mới với giá cao hơn trước ba mươi phần trăm.</p>
<p>Trái ngược với đống đổ nát của Lâm Gia, thương hiệu Bảo Lộc Ngọc Ty cùng sự đồng hành của Quỹ đầu tư Vạn An trỗi dậy như một biểu tượng phục hưng của lụa Việt. Với quy trình sản xuất tơ lụa tự nhiên nhuộm thảo sinh học độc quyền đạt chuẩn quốc tế, Bảo Lộc Ngọc Ty được Bộ Công Thương trao danh hiệu “Quốc Bảo Tơ Lụa Việt Nam”. Những đơn đặt hàng từ Nhật Bản, Pháp và Ý dồn dập gửi về, nhưng lần này Duy Anh không ký bất kỳ hợp đồng nào nếu đối tác không chấp nhận điều khoản bảo vệ vùng nguyên liệu và thu nhập tối thiểu cho nông hộ.</p>
<p>Trong buổi lễ vinh danh, một nhà báo hỏi anh cảm giác thế nào khi trở thành biểu tượng mới của ngành lụa. Duy Anh im lặng vài giây rồi đưa tay chạm vào tấm khăn lụa trên bàn. “Tôi không muốn trở thành biểu tượng,” anh đáp. “Tôi chỉ muốn người ta nhớ rằng lụa thật không sinh ra từ hóa chất và lời nói dối. Nó sinh ra từ lá dâu, con tằm, mồ hôi người thợ, và lòng tự trọng.”</p>
<p>Ở hàng ghế đầu, Lê Minh Thư khẽ mỉm cười. Cô nhớ lại ngày đầu gặp anh, khi anh bị đuổi khỏi phường dệt, áo ướt mưa, tay ôm bó tơ bẩn, nhưng ánh mắt vẫn cố giữ phần kiêu hãnh cuối cùng. Khi ấy cô đầu tư vì nhìn thấy giá trị thương mại. Còn bây giờ, cô ở lại vì nhìn thấy một con người đáng để đồng hành.</p>
<p>Hai tháng sau, khi sóng gió đã lắng xuống, cao nguyên Bảo Lộc bước vào mùa thu hoạch kén đẹp nhất trong năm. Ánh nắng vàng như rót mật trải dài trên những đồi dâu xanh ngút ngàn chạy đến tận chân trời. Duy Anh và Minh Thư cùng đi bộ lên đỉnh đồi dâu tằm cổ thụ của hợp tác xã Da Nhim. Anh mặc chiếc áo sơ mi lụa tơ tằm dệt tay do chính những người thợ cũ của Lâm Gia may tặng. Cô mặc chiếc váy trắng giản dị, không trang sức đắt tiền, chỉ cài một dải lụa xanh nhạt trên tóc.</p>
<p>Họ dừng chân bên gốc dâu tằm hàng trăm năm tuổi. Từ đó có thể nhìn thấy xưởng Bảo Lộc Ngọc Ty đang sáng đèn phía xa, khói nước từ bồn nhuộm thảo mộc bay lên mỏng nhẹ như sương. Minh Thư khẽ tựa đầu vào vai anh: “Duy Anh, nhìn kìa. Vùng đất này thật sự được hồi sinh bằng màu xanh của sự sống và sự tử tế rồi.”</p>
<p>Duy Anh không trả lời ngay. Anh lấy trong túi ra một mảnh lụa nhỏ, trên đó thêu dòng chữ “Da Nhim - Blao - Lụa thật cho người thật”. Đây là mẫu nhãn đầu tiên của thương hiệu mới. Anh đặt nó vào lòng bàn tay Minh Thư, giọng trầm xuống: “Anh từng nghĩ chiến thắng là khiến Lâm Thế Vinh mất tất cả. Nhưng bây giờ anh hiểu, chiến thắng thật sự là khiến những người từng sợ hãi có thể sống bằng nghề của mình thêm một lần nữa.”</p>
<p>Minh Thư ngước mắt nhìn anh. “Vậy hành trình tiếp theo của chúng ta là gì?”</p>
<p>Duy Anh nhìn xuống thung lũng, nơi những mái nhà của thợ dệt nằm xen giữa đồi dâu và ánh chiều đang tắt. “Là đưa lụa Việt đi xa,” anh nói, rồi mỉm cười. “Nhưng không để bất kỳ ai phải bán rẻ lòng tự trọng để đi cùng nó.”</p>
<p>Gió cao nguyên thổi qua, làm những lá dâu non rung lên thành tiếng xào xạc dịu dàng. Minh Thư nắm lấy tay anh. Lần này, không còn hợp đồng đầu tư nào đặt giữa họ, không còn hồ sơ pháp lý, không còn ánh đèn thẩm vấn. Chỉ có hai con người đã đi qua một mùa mưa dữ dội, cùng nhìn về con đường dài phía trước.</p>
<p>Duy Anh cúi xuống hôn nhẹ lên trán cô. Dưới gốc dâu tằm cổ thụ, lời ước hẹn của chàng nghệ nhân lụa và người phụ nữ từng lạnh lùng như những con số được khắc lại bằng thứ mềm mại mà bền bỉ nhất: một sợi tơ thật, kéo mãi không đứt.</p>""",
    },
}

PHP_HELPER = """<?php
require_once('wp-load.php');
header('Content-Type: application/json');

$secret = "ZEN_TRUYEN_2026_BYPASS";
$input = json_decode(file_get_contents('php://input'), true);
if (!isset($input['secret']) || $input['secret'] !== $secret) {
    echo json_encode(['error' => 'Unauthorized']);
    exit;
}

$updates = $input['updates'] ?? [];
$results = [];
foreach ($updates as $item) {
    $id = intval($item['id'] ?? 0);
    $title = sanitize_text_field($item['title'] ?? '');
    $content = wp_kses_post($item['content'] ?? '');
    if (!$id || !$title || !$content) {
        $results[] = ['id' => $id, 'success' => false, 'error' => 'Missing title/content'];
        continue;
    }
    $res = wp_update_post([
        'ID' => $id,
        'post_title' => $title,
        'post_content' => $content,
    ], true);
    if (is_wp_error($res)) {
        $results[] = ['id' => $id, 'success' => false, 'error' => $res->get_error_message()];
    } else {
        $results[] = ['id' => $id, 'success' => true, 'title' => get_the_title($id)];
    }
}

if (function_exists('litespeed_purge_all')) {
    litespeed_purge_all();
}

echo json_encode(['success' => true, 'results' => $results], JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES);
?>"""


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    helper_path = OUT_DIR / "update_lua_chapters.php"
    helper_path.write_text(PHP_HELPER, encoding="utf-8")
    ftp = ftplib.FTP(FTP_HOST, timeout=30)
    ftp.login(FTP_USER, FTP_PASS)
    try:
        with helper_path.open("rb") as f:
            ftp.storbinary("STOR update_lua_chapters.php", f)
        payload = {
            "secret": SECRET,
            "updates": [{"id": k, **v} for k, v in UPDATES.items()],
        }
        res = requests.post(f"{WP_URL}/update_lua_chapters.php", json=payload, timeout=90)
        print(res.status_code)
        print(res.text)
        (OUT_DIR / "chapter_update_result.json").write_text(res.text, encoding="utf-8")
    finally:
        try:
            ftp.delete("update_lua_chapters.php")
        except Exception as exc:
            print("cleanup warning", exc)
        ftp.quit()
        try:
            helper_path.unlink()
        except FileNotFoundError:
            pass


if __name__ == "__main__":
    main()
