<?php
/**
 * fix_editorial_endings.php
 * 1) ID 2787 (Giáo Viên Làng Ba Vì): Ch8 full resolution — hiệu trưởng Trần Hữu Đạo bị xử lý
 * 2) ID 2808 (Người Đưa Thư Tòa Nhà): Ch8 rewrite — Đinh Xuân Phú lộ thân phận, Lotus Capital vả mặt trực tiếp
 * 3) ID 3743 (Nữ Hoàng Trà Sen Tây Hồ): Ch10 rewrite — Lê Minh Hùng + Trần Lệ Hoa đối đầu trực tiếp
 */
ini_set('display_errors', 0);
ini_set('max_execution_time', 90);
header('Content-Type: application/json');

$input = json_decode(file_get_contents('php://input'), true);
if (!isset($input['secret_token']) || $input['secret_token'] !== 'ZEN_TRUYEN_2026_BYPASS') {
    http_response_code(401); echo json_encode(['error'=>'Unauthorized']); exit;
}
require_once('wp-load.php');
$results = [];

function get_last_chapter($novel_id) {
    $chapters = get_posts([
        'post_type' => 'chuong', 'posts_per_page' => -1, 'orderby' => 'date', 'order' => 'ASC',
        'meta_query' => [['key'=>'_truyen_id','value'=>(string)$novel_id,'compare'=>'=']]
    ]);
    return count($chapters) > 0 ? end($chapters) : null;
}

// ==================== TASK 1: ID 2787 — Giáo Viên Làng Ba Vì ====================
$ch8_2787 = get_last_chapter(2787);
if ($ch8_2787) {
    $content = <<<'HTML'
<p>Quyết định của Thanh tra Bộ Giáo dục và Đào tạo đến vào sáng thứ Hai — bảy ngày sau khi Lê Thanh Bình gửi hồ sơ kèm bảy mươi hai trang tài liệu: biên bản cuộc họp bị chỉnh sửa, bảng lương giả, và nhật ký ghi âm ba cuộc điện thoại trong đó Trần Hữu Đạo chỉ đạo nhân viên "chỉnh" kết quả kiểm tra của học sinh nghèo để bảo vệ tỷ lệ đỗ của trường.</p>

<p>Kết luận thanh tra: hiệu trưởng Trần Hữu Đạo vi phạm nghiêm trọng quy chế quản lý giáo dục, làm sai lệch hồ sơ, lạm dụng quyền hạn. Đình chỉ chức vụ ngay lập tức. Hồ sơ chuyển sang cơ quan điều tra để xem xét trách nhiệm hình sự về tội làm giả tài liệu công vụ.</p>

<p>Bình đọc quyết định một mình trong phòng giáo viên, buổi sáng Ba Vì mùa đông còn sương. Không cảm thấy chiến thắng. Chỉ cảm thấy nhẹ hơn — cái nhẹ của người đã giữ được điều mình cần giữ.</p>

<p>Vũ Thu Hà đứng ở cửa. "Sao không ra sân?"</p>

<p>"Đang đọc quyết định."</p>

<p>Cô bước vào, nhìn qua vai anh. Đọc xong một đoạn. "Tốt." Chỉ nói vậy.</p>

<p>Bình gấp tờ giấy lại. "Bọn học sinh chưa biết?"</p>

<p>"Chưa. Nhưng sẽ biết vào tiết đầu."</p>

<hr>

<p>Tiết toán lớp 9B. Hai mươi bốn đứa trẻ ngồi im khi Bình bước vào — vẫn chưa quen với việc giáo viên của chúng trở lại sau hai tuần vắng mặt, sau những ngày chúng nghe lỏm người lớn thì thầm. Một đứa ngồi bàn đầu nhìn anh, không hỏi gì.</p>

<p>Bình mở sách giáo khoa. "Chương mười hai. Hàm số bậc hai. Ai giải bài số ba?"</p>

<p>Lớp không thay đổi. Toán học không thay đổi. Ba Vì vẫn sương mù ngoài cửa sổ.</p>

<p>Đó là đủ để bắt đầu lại.</p>
HTML;
    wp_update_post(['ID'=>$ch8_2787->ID,'post_title'=>'Chương 8: Quyết Định Thanh Tra Và Tiết Toán Đầu Tiên','post_content'=>wp_kses_post($content)]);
    if (function_exists('litespeed_purge_post')) litespeed_purge_post($ch8_2787->ID);
    $results[] = ['task'=>'ch8_2787','wp_id'=>$ch8_2787->ID,'status'=>'updated'];
}

// ==================== TASK 2: ID 2808 — Người Đưa Thư Tòa Nhà ====================
$ch8_2808 = get_last_chapter(2808);
if ($ch8_2808) {
    $content = <<<'HTML'
<p>Cuộc họp hội đồng quản trị tòa nhà The Meridian diễn ra lúc mười bốn giờ thứ Tư — phòng họp tầng hai mươi, đủ mặt đại diện mười sáu đơn vị thuê. Lotus Capital gửi ba người đến: luật sư trưởng và hai giám đốc vùng, áo vest xám tro, cặp da đen.</p>

<p>Trần Minh ngồi bên phải bàn họp, mặt bình thản. Anh ta vẫn chưa biết.</p>

<p>Đinh Xuân Phú bước vào từ cửa phụ. Không phải bộ đồng phục xanh giao thư quen thuộc — anh mặc áo sơ mi trắng, tài liệu kẹp nách. Ngồi vào ghế cuối bàn.</p>

<p>Trần Minh nhìn anh, nhíu mày. "Anh ngồi đây làm gì? Cuộc họp này dành cho—"</p>

<p>"Dành cho người sở hữu bất động sản trong tòa nhà?" Phú đặt tập hồ sơ lên bàn. "Tôi là chủ sở hữu. Sở Kế hoạch và Đầu tư TP.HCM. Đăng ký kinh doanh số 0302184670 — công ty Minh Phú Invest. Chúng tôi sở hữu toàn bộ tầng tám, chín, và mười hai của tòa nhà này từ năm 2019."</p>

<p>Phòng họp im lặng.</p>

<p>"Ngoài ra," anh tiếp tục, "chúng tôi cũng là bên đang xem xét ký hợp đồng thuê mặt bằng tầng hai mươi ba cho văn phòng mới — vị trí mà Lotus Capital đang đàm phán. Tôi đề nghị dừng thương lượng với Lotus Capital vì không đáp ứng điều kiện đối tác." Anh nhìn thẳng vào ba người từ Lotus Capital. "Các anh có mười lăm phút để rời khỏi tòa nhà của tôi."</p>

<p>Trần Minh đứng dậy, ghế kêu tiếng mạnh. Nhìn Phú. Nhìn tập hồ sơ. Nhìn xuống sàn.</p>

<p>Không nói được gì.</p>

<hr>

<p>Chiều hôm đó, Phú trở lại tầng trệt. Bộ đồng phục xanh, xe máy dựng ở lối vào. Nguyễn Thị Phượng — lễ tân tầng một — nhìn anh từ quầy. "Sao anh vẫn đến?"</p>

<p>"Còn bưu phẩm chưa giao." Anh cầm cặp thư hỏi địa chỉ. "Tầng mười hai, phòng 1204."</p>

<p>Phượng cười. Lần đầu tiên từ khi Phú đến đây.</p>

<p>Phú gật đầu rồi bước vào thang máy. Anh không cần tòa nhà này biết ơn anh. Anh chỉ cần nó vận hành đúng. Những thứ tốt không cần phải được nhìn thấy để tồn tại.</p>
HTML;
    wp_update_post(['ID'=>$ch8_2808->ID,'post_title'=>'Chương 8: Chủ Sở Hữu Tự Lộ Diện','post_content'=>wp_kses_post($content)]);
    if (function_exists('litespeed_purge_post')) litespeed_purge_post($ch8_2808->ID);
    $results[] = ['task'=>'ch8_2808','wp_id'=>$ch8_2808->ID,'status'=>'updated'];
}

// ==================== TASK 3: ID 3743 — Nữ Hoàng Trà Sen Tây Hồ ====================
$ch10_3743 = get_last_chapter(3743);
if ($ch10_3743) {
    $content = <<<'HTML'
<p>Đại hội cổ đông bất thường của Công ty Trà Sen Tây Hồ diễn ra lúc chín giờ sáng cuối tháng Mười — phòng họp khách sạn Sofitel bên hồ Tây, sáu mươi bảy cổ đông có mặt và ủy quyền.</p>

<p>Lê Minh Hùng ngồi ở đầu bàn. Anh ta vẫn tin tỷ lệ biểu quyết nghiêng về phía mình — cho đến khi thư ký đọc xong danh sách ủy quyền mới.</p>

<p>Lê Minh Nguyệt đã mua lại 8,3% cổ phần từ ba cổ đông nhỏ lẻ trong hai tuần qua. Im lặng, không thông báo. Tỷ lệ hiện tại của cô: 51,4%.</p>

<p>Khi con số được đọc lên, Hùng quay sang luật sư. Luật sư lật tài liệu, xem lại, lật thêm. Không có gì sai. Tất cả đều hợp pháp.</p>

<p>"Biểu quyết bãi miễn thành viên HĐQT Lê Minh Hùng." Chủ tọa đọc đề nghị của Nguyệt. "Xin tay."</p>

<p>Năm mươi ba phần trăm giơ tay.</p>

<p>Hùng nhìn căn phòng. Nhìn những người mà hai năm trước ông nội ông đã nhường đất trồng sen cho con cháu họ. Nhìn Nguyệt ngồi phía bên kia bàn — không nhìn lại anh ta, đang ghi chép biên bản.</p>

<p>Anh ta đứng dậy. Không nói gì. Bước ra.</p>

<hr>

<p>Trần Lệ Hoa — mẹ kế Nguyệt — đợi bên ngoài hành lang. Bà đã biết kết quả ngay khi nhìn mặt Hùng bước ra. "Thôi được. Con đã thắng."</p>

<p>Nguyệt dừng lại trước mặt bà. Không phải để ăn mừng. "Con không thắng gì cả. Con chỉ lấy lại những gì của ông nội."</p>

<p>"Ông nội đã cho bà."</p>

<p>"Ông nội đã cho với điều kiện bảo tồn nghề. Bà đã phá điều kiện đó khi ký hợp đồng với Ethyl Vanillin." Nguyệt dừng lại. "Cục Sở hữu trí tuệ đang xem xét tất cả hợp đồng từ năm 2022. Bà nên tìm luật sư sớm."</p>

<p>Bà Hoa không nói thêm gì.</p>

<hr>

<p>Chiều tà hồ Tây — ánh nắng cuối ngày phủ vàng mặt nước, sen đã tàn nhưng lá còn xanh rộng. Nguyệt ngồi bên bờ với Bảo, không nói gì một lúc.</p>

<p>"Giờ làm gì?" Bảo hỏi.</p>

<p>"Mùa ướp mới tháng Sáu." Nguyệt nhìn ra hồ. "Còn tám tháng. Đủ để chuẩn bị đúng cách."</p>

<p>Trà sen Hồ Tây không vội được. Cô đã biết điều đó từ năm mười một tuổi, khi ông nội dạy cô cách nhét gạo trà vào nhụy sen trước bình minh. Những thứ tốt cần thời gian — và người có thể chờ.</p>
HTML;
    wp_update_post(['ID'=>$ch10_3743->ID,'post_title'=>'Chương 10: Đại Hội Và Mùa Sen Mới','post_content'=>wp_kses_post($content)]);
    if (function_exists('litespeed_purge_post')) litespeed_purge_post($ch10_3743->ID);
    $results[] = ['task'=>'ch10_3743','wp_id'=>$ch10_3743->ID,'status'=>'updated'];
}

if (function_exists('litespeed_purge_all')) litespeed_purge_all();
echo json_encode(['results'=>$results], JSON_UNESCAPED_UNICODE|JSON_PRETTY_PRINT);
?>
