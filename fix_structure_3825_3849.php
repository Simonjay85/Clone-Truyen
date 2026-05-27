<?php
/**
 * fix_structure_3825_3849.php
 * 1) ID 3825 WP3829 ch3: Add villain re-concealment layer after early reveal — Lê Văn Hùng
 * 2) ID 3849 WP3853 ch3: Add human relationship moment between Thành and Hồng Vân
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

// ==================== TASK 1: ID 3825 WP3829 — Villain re-concealment ====================
// Ch3 title "Lòng Tham Lộ Diện" reveals Hùng's betrayal too openly too early
// Add a scene at the end of ch3 where Hùng receives a call and appears to have second thoughts —
// creating ambiguity about how deep the betrayal goes, sustaining tension for later chapters

$post_3829 = get_post(3829);
if ($post_3829) {
    $addition_3825 = '
<hr>
<p>Đang đứng giữa sảnh resort, điện thoại Hùng rung lên. Số gọi đến là của Bernard Dupont.</p>
<p>"Anh ở đâu? Cuộc họp với nhóm luật sư bắt đầu lúc ba giờ." Giọng Dupont khô và sắc như dao cạo.</p>
<p>"Đang trên đường." Hùng bước vội ra phía cổng phụ, khép nhẹ cánh cửa lại sau lưng.</p>
<p>Một khoảnh khắc anh ta dừng lại ở hành lang vắng. Nhìn ra khoảng sân resort trải rộng ra đến tận bãi biển — từng viên đá lát, từng bụi hoa giấy, từng bờ tường stucco màu trắng kem đó đều được Trịnh Gia Bảo tự tay vẽ phác thảo. Hùng biết điều đó. Anh ta đã ngồi cạnh Bảo trong những đêm thiết kế thức khuya, đã uống cùng nhau bao nhiêu ly cà phê đen.</p>
<p>Rồi điện thoại Dupont rung lần nữa.</p>
<p>Hùng xóa ký ức đó đi, bước ra ánh nắng.</p>
<p>Chỉ là kinh doanh. Anh ta tự nhủ. <em>Chỉ là kinh doanh.</em></p>';

    $new_content = $post_3829->post_content . $addition_3825;
    wp_update_post(['ID'=>3829,'post_content'=>wp_kses_post($new_content)]);
    if (function_exists('litespeed_purge_post')) litespeed_purge_post(3829);
    $results[] = ['task'=>'villain_recon_3825','wp_id'=>3829,'status'=>'appended'];
} else {
    $results[] = ['task'=>'villain_recon_3825','wp_id'=>3829,'status'=>'post_not_found'];
}

// ==================== TASK 2: ID 3849 WP3853 ch3 — Human relationship moment ====================
// At the Vietcombank meeting, add a moment of connection between Thành and Vân
// Insert after the bank officer's skepticism — a scene where Vân quietly vouches for Thành

$post_3853 = get_post(3853);
if ($post_3853) {
    // Try to insert after the skeptical bank officer description
    $anchor = 'với vẻ hoài nghi rõ rệt';
    if (strpos($post_3853->post_content, $anchor) !== false) {
        $insert = '
<p>Đúng lúc đó, Hồng Vân đặt thêm một tập tài liệu lên bàn. Không phải báo cáo tài chính — đó là album ảnh vườn sầu riêng Êđê của gia đình Thành chụp bằng điện thoại, từng tấm ghi rõ ngày tháng trải dài bảy năm.</p>
<p>"Ông Khải," cô nói, giọng bình tĩnh, "Tôi hiểu tiêu chí tín dụng của ngân hàng. Nhưng đây là bảy năm của một người không biết nghỉ. Số liệu thổ nhưỡng, năng suất từng mùa, và tỷ lệ cây sống sót qua ba đợt khô hạn liên tiếp — tất cả đều ở trong tập này. Ông có thể cho chúng tôi mười phút để xem không?"</p>
<p>Khải nhìn album, nhìn Vân, rồi nhìn Thành. Thành không nói gì — anh chưa bao giờ giỏi thuyết trình trong phòng họp. Nhưng trong đôi mắt anh có thứ gì đó mà Khải đã thấy nhiều lần trong ba mươi năm làm ngân hàng: sự thật của người không có gì để che giấu.</p>
<p>Ông mở album ra.</p>';
        $new_content = str_replace($anchor, $anchor . $insert, $post_3853->post_content);
        wp_update_post(['ID'=>3853,'post_content'=>wp_kses_post($new_content)]);
        if (function_exists('litespeed_purge_post')) litespeed_purge_post(3853);
        $results[] = ['task'=>'relationship_3849','wp_id'=>3853,'status'=>'updated'];
    } else {
        // Fallback: append brief relationship moment
        $addition_3849 = '
<p>Trên đường ra khỏi ngân hàng, khi Hồng Vân và Thành bước xuống cầu thang, cô hỏi khẽ: "Anh có lo không?"</p>
<p>Thành im lặng một nhịp. "Tôi không quen xin tiền."</p>
<p>Vân gật đầu. "Tôi biết. Tôi cũng không quen. Nhưng hôm nay không phải xin — hôm nay là thuyết phục." Cô nhìn thẳng ra đường. "Và anh thuyết phục được. Ông Khải đọc hết album ảnh đó rồi — tôi nhìn thấy ông lật từng trang."</p>
<p>Thành dừng lại ở chân cầu thang, nhìn sang cô một lúc. Trong bảy năm trồng sầu riêng, chưa ai ngồi cạnh anh trong phòng ngân hàng như vậy. Anh không biết nói điều đó ra thành lời — nhưng anh nhớ.</p>';
        $new_content = $post_3853->post_content . $addition_3849;
        wp_update_post(['ID'=>3853,'post_content'=>wp_kses_post($new_content)]);
        if (function_exists('litespeed_purge_post')) litespeed_purge_post(3853);
        $results[] = ['task'=>'relationship_3849','wp_id'=>3853,'status'=>'appended_fallback'];
    }
} else {
    $results[] = ['task'=>'relationship_3849','wp_id'=>3853,'status'=>'post_not_found'];
}

if (function_exists('litespeed_purge_all')) litespeed_purge_all();
echo json_encode(['results'=>$results], JSON_UNESCAPED_UNICODE|JSON_PRETTY_PRINT);
?>
