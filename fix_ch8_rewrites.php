<?php
/**
 * fix_ch8_rewrites.php
 * Rewrite three formulaic copy-paste endings in:
 *   ID 2089 WP4389 — "Chương 8: Đông Anh Hóa Rồng"
 *   ID 2106 WP4373 — "Chương 8: Hào Môn Trăm Tỷ Thực Sự"
 *   ID 2099 WP4381 — "Chương 8: Vị Vua Mới Của Hoàng Gia"
 * All three currently use identical romance-proposal + pháo hoa template.
 */
ini_set('display_errors', 0);
ini_set('max_execution_time', 60);
header('Content-Type: application/json');
$input = json_decode(file_get_contents('php://input'), true);
if (!isset($input['secret_token']) || $input['secret_token'] !== 'ZEN_TRUYEN_2026_BYPASS') {
    http_response_code(401); echo json_encode(['error'=>'Unauthorized']); exit;
}
require_once('wp-load.php');
$results = [];

// ============================================================
// ID 2089 — WP4389 — "Chương 8: Đông Anh Hóa Rồng"
// ============================================================
$c2089 = <<<'VIET'
<p>Hai tháng sau khi tập đoàn Hùng Phát sụp đổ, Chính phủ chính thức công bố quyết định khởi công xây dựng cầu Nhật Tân và phê duyệt quy hoạch trục đường Võ Nguyên Giáp kéo dài ra hướng sân bay Nội Bài.</p>

<p>Đêm đó Trần Huy không ngủ được.</p>

<p>Không phải vì giá đất đã tăng hơn trăm lần chỉ trong vài tuần — điều đó anh đã biết trước từ hai kiếp người. Mà vì lần đầu tiên trong cuộc đời này, anh cảm thấy tương lai không còn là bản đồ anh mang theo trong đầu nữa. Nó đang diễn ra ngay trước mắt, bằng xương bằng thịt.</p>

<p>Sáng thứ Tư, anh ra công trường từ lúc năm giờ rưỡi — trước khi đoàn xe của ban tổ chức lễ khởi công xuất hiện. Công trường của dự án Khu đô thị sinh thái Đông Anh Diamond trải dài trên năm mươi héc-ta đã được san lấp, cọc tiêu đỏ cắm dày theo từng ô quy hoạch.</p>

<p>Trần Huy đứng ở góc tây bắc khu đất, nơi trước đây là bờ ao nuôi vịt của ba hộ nông dân xã Đông Hội mà anh đã thương lượng mua lại trước cả khi quy hoạch được công bố. Dưới chân anh là đất — cùng loại đất phù sa sông Hồng mà người ta đã trồng lúa ở đây từ mấy trăm năm nay.</p>

<p>Phía đông, mặt trời đang lên sau tầng mây mùa đông thấp.</p>

<p>"Anh ra đây từ bao giờ?" Giọng Lê Thu Trang vang lên phía sau lưng.</p>

<p>Anh không quay lại ngay. "Sáng sớm."</p>

<p>Cô bước lại đứng bên cạnh, nhìn ra cùng hướng với anh. Không mặc đầm dạ hội như những sự kiện trước. Áo len kem, quần tây xám. Tóc để thấp, đơn giản. Như thể cô cũng biết rằng sáng hôm nay không phải là sự kiện kinh doanh nữa.</p>

<p>"Năm mươi héc-ta," cô nói. "Mười nghìn tỷ đồng theo định giá hôm qua. Anh đang nghĩ gì?"</p>

<p>Trần Huy im lặng một lúc thật sự.</p>

<p>"Tôi nghĩ đến những người đã bán đất cho tôi," anh nói. "Ông Thắng, ông Dần, bà Liên. Họ bán vì cần tiền đóng học cho con, vì nợ ngân hàng, vì không biết gì sẽ xảy ra sau đó. Tôi biết. Họ không biết."</p>

<p>Thu Trang nhìn anh. "Anh hối hận?"</p>

<p>"Không." Anh quay sang cô. "Tôi đã trả giá thị trường đúng lúc đó, không ép giá. Nhưng tôi vẫn nghĩ đến họ. Vì có những thứ biết trước mà không chia sẻ được — không phải vì ích kỷ, mà vì không ai tin."</p>

<p>Ánh sáng ban mai bắt đầu phủ lên cánh đồng đất đỏ chờ móng.</p>

<p>Thu Trang cúi nhìn đôi giày của mình đang dẫm trên đất Đông Anh. "Dự án này, anh muốn xây cái gì thật sự? Không phải trên bản vẽ — thật sự."</p>

<p>"Nhà để ở," Trần Huy trả lời, không do dự. "Trường học tốt. Bệnh viện gần. Công viên bên sông mà người ta đi bộ buổi sáng. Người ta sẽ sống ở đây thật sự, không chỉ mua để sang tay."</p>

<p>Thu Trang gật đầu — không phải gật đầu của người đồng ý về mặt hình thức, mà gật đầu của người hiểu và tin.</p>

<p>"Khi nào anh bắt đầu dự án tiếp theo," cô nói, "tôi muốn vào cùng. Không cần biết quy mô hay lợi suất dự kiến."</p>

<p>"Vì sao?"</p>

<p>Cô nhìn thẳng vào mắt anh. "Vì anh là người duy nhất tôi biết xây thứ gì cũng nghĩ đến người sẽ sống trong đó trước khi nghĩ đến giá bán."</p>

<p>Đoàn xe khởi công bắt đầu tiến vào từ cổng phía nam. Tiếng loa phóng thanh kiểm tra âm thanh vang lên. Ban tổ chức gọi điện thúc giục hai người ra khán đài.</p>

<p>Trần Huy nhìn lần cuối ra cánh đồng đất trước khi quay vào. Đây là nơi anh đã đặt cược tất cả trong kiếp này — không phải vì biết trước, mà vì tin rằng đất tốt và người thật sẽ gặp nhau.</p>

<p>Đông Anh bắt đầu hóa rồng. Và lần này, anh ở đây để chứng kiến — không phải nhìn lại từ một kiếp đã qua.</p>
VIET;

$r = wp_update_post(['ID'=>4389, 'post_content'=>wp_kses_post($c2089)]);
$results[] = ['novel_id'=>2089, 'wp_id'=>4389, 'title'=>'Chương 8: Đông Anh Hóa Rồng', 'updated'=>($r&&!is_wp_error($r))];
if (function_exists('litespeed_purge_post')) litespeed_purge_post(4389);

// ============================================================
// ID 2106 — WP4373 — "Chương 8: Hào Môn Trăm Tỷ Thực Sự"
// ============================================================
$c2106 = <<<'VIET'
<p>Lễ ký kết hợp đồng nhượng quyền thương hiệu Sen Việt với VinCommerce diễn ra lúc mười bốn giờ tại phòng họp tầng ba khách sạn Park Hyatt Sài Gòn. Không phải khán phòng lớn, không phải đèn chiếu rực rỡ — chỉ một căn phòng họp hai mươi ghế, đủ cho đại diện hai bên và luật sư.</p>

<p>Lâm Vy ngồi đối diện Giám đốc phát triển nhượng quyền VinCommerce, tập hợp đồng trước mặt, bút cầm sẵn.</p>

<p>Cô nhớ lại căn bếp thuê ở quận Bình Thạnh ba năm trước — nồi nước nóng để pha trà, bình đựng sen ươm trong đá khô, cuốn sổ ghi công thức bị gạch xóa hàng chục lần. Và người đàn ông ở gia đình hào môn mà cô từng nghĩ sẽ trở thành điểm tựa — rồi mới hiểu ra rằng điểm tựa không bao giờ đến từ bên ngoài.</p>

<p>Cô đặt bút ký.</p>

<p>Hợp đồng nhượng quyền hai trăm cửa hàng trên hệ thống VinMart, giá trị một trăm tỷ đồng ba năm, điều khoản bảo hộ công thức và nguồn gốc nguyên liệu theo tiêu chuẩn cô đã đàm phán kỹ trong mười một buổi họp trước đó.</p>

<p>Trần Minh Quốc ngồi ở ghế bên phải, theo dõi từng trang một. Anh không vỗ tay, không bình luận, chỉ lật trang và đọc. Đó là cách anh làm việc — cẩn thận, không vội, không diễn.</p>

<p>Sau khi ký xong, hai bên bắt tay. Phóng viên vào chụp ảnh ba phút. Rồi căn phòng họp trống dần.</p>

<p>Lâm Vy đứng lại ở cửa sổ nhìn xuống Lam Sơn quảng trường. Xe cộ qua lại bình thường bên dưới — Sài Gòn không biết và không cần biết cô vừa ký gì.</p>

<p>"Em đang nghĩ gì?" Minh Quốc hỏi từ sau lưng.</p>

<p>"Nghĩ đến bà nội." Cô trả lời thật. "Bà trồng sen ở ao nhà từ hồi em còn nhỏ. Bà nói hoa sen buổi sáng sớm mới thơm nhất, phải ra hái trước khi trời sáng hẳn. Em nghĩ hồi đó bà chỉ đang kể về hoa."</p>

<p>Minh Quốc bước lại đứng bên cạnh, nhìn xuống cùng hướng với cô.</p>

<p>"Còn bây giờ?" anh hỏi.</p>

<p>"Bây giờ em hiểu bà đang dạy mình về sự kiên nhẫn." Lâm Vy khẽ cười. "Những thứ tốt không thể vội."</p>

<p>Minh Quốc im lặng một lúc. Rồi anh nói, không nhìn thẳng vào cô — vẫn nhìn xuống quảng trường bên dưới: "Mình có thể ăn tối không? Chỉ ăn tối thôi. Không bàn hợp đồng, không xem báo cáo."</p>

<p>Lâm Vy quay sang nhìn anh.</p>

<p>Trần Minh Quốc — người đàn ông đã ngồi đối diện cô trong mười một buổi họp, đọc từng điều khoản không bỏ sót, không một lần dùng vị trí để ép — đang hỏi cô đi ăn tối theo cách của người lần đầu tiên không biết câu trả lời.</p>

<p>"Được," cô nói.</p>

<p>Đơn giản vậy thôi.</p>

<p>Họ ra khỏi khách sạn khi trời đã gần tối, đi bộ về phía phố đi bộ Nguyễn Huệ. Sen Việt sẽ có mặt trong hai trăm cửa hàng trên toàn quốc — điều đó là thật. Cô gái bán trà sữa ở Bình Thạnh ba năm trước — điều đó cũng là thật. Và bữa tối này, hai người đi bên nhau giữa Sài Gòn buổi chiều — cũng là thật.</p>

<p>Hào môn trăm tỷ không phải điều Lâm Vy tìm kiếm. Nhưng những gì cô xây được bằng tay mình — đó mới là thứ không ai lấy đi được.</p>
VIET;

$r = wp_update_post(['ID'=>4373, 'post_content'=>wp_kses_post($c2106)]);
$results[] = ['novel_id'=>2106, 'wp_id'=>4373, 'title'=>'Chương 8: Hào Môn Trăm Tỷ Thực Sự', 'updated'=>($r&&!is_wp_error($r))];
if (function_exists('litespeed_purge_post')) litespeed_purge_post(4373);

// ============================================================
// ID 2099 — WP4381 — "Chương 8: Vị Vua Mới Của Hoàng Gia"
// ============================================================
$c2099 = <<<'VIET'
<p>Đêm kỷ niệm mười năm chuỗi khách sạn Hoàng Gia diễn ra lúc mười chín giờ tại Grand Ballroom tầng ba — căn phòng tiệc lớn nhất trong tổ hợp mà Trần Gia Huy đã từng bị tống ra khỏi cửa trước như một kẻ vô danh.</p>

<p>Giờ anh đứng ở lối vào và chờ — không phải như khách, không phải như người bị từ chối, mà như người chủ sở hữu đang kiểm tra lần cuối trước khi cửa mở.</p>

<p>Đội phục vụ di chuyển nhịp nhàng, khăn trải bàn trắng tinh, ly pha lê xếp đều. Mùi hoa huệ từ những bình cắm lớn ở góc phòng thoang thoảng. Tất cả đều đúng như anh đã yêu cầu.</p>

<p>Nguyễn Vũ Phương Anh bước vào từ lối sau bếp, vẫn đang cầm tập checklist của ban tổ chức. Cô dừng lại khi thấy anh.</p>

<p>"Anh ra đây từ khi nào?"</p>

<p>"Mười lăm phút trước." Anh gật đầu về phía sảnh. "Hệ thống âm thanh tầng dưới đang bị nhiễu nhẹ ở kênh trái. Đã báo kỹ thuật chưa?"</p>

<p>"Báo rồi, đang xử lý." Cô nhìn anh một lúc. "Anh đi kiểm tra hay anh đang tránh khách?"</p>

<p>Trần Gia Huy cười khẽ. "Cả hai."</p>

<p>Họ đứng bên nhau nhìn vào Grand Ballroom. Hai trăm ghế, tám mươi bàn tròn, đèn chùm pha lê được hạ xuống đúng độ cao cô đã điều chỉnh ba lần trước đó. Phòng tiệc này sẽ đầy người trong chưa đầy một giờ nữa.</p>

<p>"Mười năm trước họ đuổi anh ra khỏi đây," Phương Anh nói, không phải để nhắc lại vết thương mà như người đang ghi nhận một sự thật lịch sử. "Anh có muốn nói điều đó trong bài phát biểu tối nay không?"</p>

<p>"Không." Anh lắc đầu ngay. "Vì tối nay không phải về anh. Tối nay là về nhân viên đã ở lại trong năm khủng hoảng, về khách hàng đã quay lại sau khi chúng ta thay tên. Anh mà đứng lên kể chuyện anh bị đuổi thì tối nay thành tiệc khoe khoang."</p>

<p>Phương Anh nhìn anh.</p>

<p>"Anh đã nghĩ điều này từ bao giờ?"</p>

<p>"Từ tuần trước khi soạn bài phát biểu." Anh quay sang nhìn cô. "Phương Anh viết phần nào giúp anh thì phần đó luôn tốt hơn phần anh tự viết. Lần này cô không viết giúp."</p>

<p>"Vì lần này anh cần nói bằng giọng của anh."</p>

<p>"Đúng."</p>

<p>Tiếng nhạc từ ban nhạc đang thử soundcheck vang lên — nhẹ, du dương, đúng với không khí anh muốn cho buổi tối này.</p>

<p>Phương Anh nhìn xuống tập checklist trên tay, gạch đi mục cuối cùng. "Mọi thứ đã sẵn sàng."</p>

<p>Anh gật đầu. "Đi thôi."</p>

<p>Họ bước vào Grand Ballroom cùng nhau — không phải bằng lối trình diễn, mà bằng lối bếp phụ quen thuộc của người làm việc trong ngành này. Ánh đèn chùm pha lê đổ xuống sàn đại lý đá trắng.</p>

<p>Trần Gia Huy nhìn căn phòng một lần nữa.</p>

<p>Mười năm trước anh bị tống ra từ cửa trước. Tối nay anh bước vào từ cửa bếp. Không có gì khác nhau trong mắt anh — vì cả hai cửa đều dẫn vào cùng một nơi, và điều quan trọng không phải là anh vào bằng cửa nào mà là anh làm được gì bên trong.</p>
VIET;

$r = wp_update_post(['ID'=>4381, 'post_content'=>wp_kses_post($c2099)]);
$results[] = ['novel_id'=>2099, 'wp_id'=>4381, 'title'=>'Chương 8: Vị Vua Mới Của Hoàng Gia', 'updated'=>($r&&!is_wp_error($r))];
if (function_exists('litespeed_purge_post')) litespeed_purge_post(4381);

if (function_exists('litespeed_purge_all')) litespeed_purge_all();

echo json_encode(['status'=>'done','results'=>$results], JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
?>
