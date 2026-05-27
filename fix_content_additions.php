<?php
/**
 * fix_content_additions.php
 * Targeted content additions to fix narrative gaps:
 * 1) ID 3813 WP3820 ch6: add emotional bridge paragraph before ch7 (Warsaw)
 * 2) ID 3873 WP3876 ch2: add early mention of Hùng the Deloitte auditor
 * 3) ID 3755 WP3757 ch1: deepen Lê Văn Nam's motivation backstory
 * 4) ID 2794 WP4662 ch1: add Hùng's reason for hiding as gardener
 * 5) ID 3633: find Lâm Khánh Chi's first appearance and add context
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

function patch_chapter($wp_id, $search, $insert_after, &$results, $label) {
    $post = get_post($wp_id);
    if (!$post) { $results[] = ['task'=>$label,'wp_id'=>$wp_id,'status'=>'post_not_found']; return; }
    if (strpos($post->post_content, $search) === false) {
        $results[] = ['task'=>$label,'wp_id'=>$wp_id,'status'=>'anchor_not_found','anchor'=>mb_substr($search,0,50)];
        return;
    }
    $new_content = str_replace($search, $search . $insert_after, $post->post_content);
    wp_update_post(['ID'=>$wp_id, 'post_content'=>wp_kses_post($new_content)]);
    if (function_exists('litespeed_purge_post')) litespeed_purge_post($wp_id);
    $results[] = ['task'=>$label,'wp_id'=>$wp_id,'status'=>'updated'];
}

// ==================== TASK 1: ID 3813 WP3820 ch6 — Warsaw bridge ====================
// Ch6 "Cơn Giông Trước Giờ Bay" ends with defamation campaign
// Insert bridge at end of closing paragraph (before </p> of last visible block)
$bridge_3813 = '

<p>Tất cả những điều đó — từng dòng chữ vu khống, từng bài đăng giả mạo — Phúc đọc hết trong đêm. Đọc không phải để đau, mà để biết.Đến gần hai giờ sáng, cậu gập máy tính lại, xếp những bản nhạc in tay vào túi đựng đàn đã sờn cạnh — tập bản thảo Sonatina giọng Đô thứ mà cậu viết trong ba năm, từng khuông nhạc là từng ngày không ngủ. Nếu kẻ nào đó muốn chứng minh rằng bản nhạc đó không phải của cậu, thì cậu sẽ chơi nó trước năm trăm khán giả Warsaw. Bằng chứng thật không nằm trên giấy tờ — nó nằm trong mười đầu ngón tay.</p>';

patch_chapter(3820,
    'Lâm Hoàng Phúc',
    '',
    $results, 'ch6_bridge_3813');

// Better approach — append directly to ch6 post content
$post_3820 = get_post(3820);
if ($post_3820) {
    $addition = '
<hr>
<p>Tất cả những điều đó — từng dòng chữ vu khống, từng bài đăng giả mạo — Phúc đọc hết trong đêm. Đọc không phải để đau, mà để biết.Đến gần hai giờ sáng, cậu gập máy tính lại, xếp những bản nhạc in tay vào túi đựng đàn đã sờn cạnh — tập bản thảo <em>Sonatina giọng Đô thứ</em> viết trong ba năm, từng khuông nhạc là từng ngày không ngủ. Nếu có người muốn chứng minh bản nhạc đó không phải của cậu, thì cậu sẽ chơi nó trước năm trăm khán giả Warsaw. Bằng chứng thật không nằm trên giấy tờ — nó nằm trong mười đầu ngón tay.</p>
<p>Cậu nhắn tin cho Linh: <em>"Em đặt vé chưa? Mình đi sáng mai."</em></p>
<p>Ba phút sau, điện thoại rung: <em>"Đã đặt từ hôm qua. Vì em biết anh sẽ không bỏ cuộc."</em></p>';
    $new_content = $post_3820->post_content . $addition;
    wp_update_post(['ID'=>3820, 'post_content'=>wp_kses_post($new_content)]);
    if (function_exists('litespeed_purge_post')) litespeed_purge_post(3820);
    // Remove the failed patch_chapter result and replace
    array_pop($results);
    $results[] = ['task'=>'ch6_bridge_append_3813','wp_id'=>3820,'status'=>'appended'];
}

// ==================== TASK 2: ID 3873 WP3876 ch2 — Add Deloitte auditor mention ====================
// Ch2 is Bảo Châu café meeting. Insert mention of Hùng the auditor friend early in scene
// Anchor: first time Khải thinks about who can help him
$auditor_mention = '
<p>Trong khi chờ Bảo Châu, Khải lướt qua danh bạ điện thoại. Anh dừng lại ở tên Nguyễn Đức Hùng — bạn học cùng lớp từ hồi Đại học Y Hà Nội, giờ là kiểm toán viên cấp cao tại Deloitte Việt Nam. Hùng là người duy nhất trong giới tài chính mà Khải tin được đủ để nhờ đọc báo cáo kiểm toán nội bộ của bệnh viện — nếu anh có được nó. Nhưng trước tiên, phải có bằng chứng đã.</p>';

patch_chapter(3876,
    '<p>Trần Bảo Châu ngồi lặng lẽ ở một chiếc bàn gỗ nhỏ đặt trong góc khuất phía trong của quán.</p>',
    $auditor_mention,
    $results, 'ch2_auditor_3873');

// ==================== TASK 3: ID 3755 WP3757 ch1 — Deepen Lê Văn Nam motivation ====================
// Add a passage early in ch1 establishing Nam's backstory as runner-up who lost to Khải
$nam_backstory = '
<p>Lê Văn Nam — trưởng khoa phẫu thuật thẩm mỹ, người đã nộp đơn kiến nghị đình chỉ anh — đứng ngoài phòng mổ, khuôn mặt phẳng lặng như đá. Giữa Khải và Nam có một quá khứ dài hơn lời giải thích đơn giản là "ganh tị". Ba năm trước, cả hai cùng lọt vào vòng chung kết Giải thưởng Phẫu thuật Thẩm mỹ Xuất sắc nhất Đông Nam Á — Nam đã chuẩn bị bài thuyết trình suốt sáu tháng, còn Khải nộp hồ sơ vào tuần cuối. Hội đồng chấm giải trao cho Khải, và từ ngày đó, mỗi lần nhìn thấy tên Khải xuất hiện trên báo chí, Nam lại cảm thấy thứ gì đó trong lồng ngực thắt lại. Không phải chỉ thua một giải thưởng — mà là cảm giác rằng mình đã cống hiến nhiều hơn và không được nhìn nhận đúng mức.</p>';

patch_chapter(3757,
    '<p>Ngô Hoàng Khải đứng yên như một pho tượng, đôi mắt sâu hoắm phía sau cặp kính bảo hộ phản chiếu ánh sáng dịu nhẹ của màn hình đo sinh hiệu.</p>',
    $nam_backstory,
    $results, 'ch1_nam_backstory_3755');

// ==================== TASK 4: ID 2794 WP4662 ch1 — Add Hùng's reason for hiding ====================
// Add internal monologue early in ch1 before Hùng interacts with Hương
$hung_backstory = '
<p>Hai năm trước, Vũ Quốc Hùng là Phó Tổng Giám đốc của Archi-Việt Group, công ty thiết kế kiến trúc đô thị lớn thứ ba miền Nam. Anh có văn phòng tầng mười bảy, có xe hơi, có danh thiếp dày ký hiệu. Rồi một buổi sáng tháng Tư, kết quả kiểm toán nội bộ chỉ thẳng vào anh — những sai phạm trong một hợp đồng xây dựng mà anh không ký nhưng có chữ ký giống hệt. Vụ kiện pháp lý kéo dài chín tháng, cuối cùng anh được minh oan — nhưng tên anh đã bị công khai trên báo trước đó. Hùng quyết định rời đi. Không phải vì thua, mà vì cần thời gian để nhớ lại điều gì làm cho mình thực sự hứng khởi khi thức dậy mỗi sáng. Trong vườn, đất không dối trá, hoa không cần lý lịch sạch — đó là điều anh cần một thời gian.</p>';

patch_chapter(4662,
    '<p>Hùng ngẩng đầu lên, ánh mắt anh chạm phải Hương, người chủ của căn biệt thự.</p>',
    $hung_backstory,
    $results, 'ch1_backstory_2794');

// ==================== TASK 5: ID 3633 — Find and contextualize Lâm Khánh Chi ====================
// Search all chapters for first appearance of Khánh Chi, add context
global $wpdb;
$chi_chapters = $wpdb->get_results($wpdb->prepare(
    "SELECT p.ID, p.post_title FROM {$wpdb->posts} p
     INNER JOIN {$wpdb->postmeta} pm ON pm.post_id = p.ID AND pm.meta_key='_truyen_id' AND pm.meta_value=%s
     WHERE p.post_type='chuong' AND p.post_status='publish'
     AND p.post_content LIKE %s ORDER BY p.post_date ASC LIMIT 1",
    '3633', '%Khánh Chi%'
));

if ($chi_chapters) {
    $ch_id   = $chi_chapters[0]->ID;
    $ch_post = get_post($ch_id);
    // Add context: before the first mention of Khánh Chi, note the relationship
    $context = 'Lâm Khánh Chi — người đồng nghiệp cũ từ thời Duy Anh còn làm nghiên cứu viên tại Viện Sinh học Nông nghiệp trước khi anh về phụng dưỡng gia nghiệp trà sen của ông nội — ';
    // Find first occurrence and check if she's introduced with context
    if (strpos($ch_post->post_content, $context) === false) {
        // Try to insert before first mention of Khánh Chi
        $new_content = preg_replace(
            '/(?<![a-zàáâãèéêìíòóôõùúýăđưA-ZÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚÝĂĐƯ])Lâm Khánh Chi(?![a-zàáâãèéêìíòóôõùúýăđưA-ZÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚÝĂĐƯ])/',
            $context . 'Lâm Khánh Chi',
            $ch_post->post_content,
            1 // only first occurrence
        );
        if ($new_content !== $ch_post->post_content) {
            wp_update_post(['ID'=>$ch_id,'post_content'=>wp_kses_post($new_content)]);
            if (function_exists('litespeed_purge_post')) litespeed_purge_post($ch_id);
            $results[] = ['task'=>'chi_context_3633','wp_id'=>$ch_id,'title'=>$chi_chapters[0]->post_title,'status'=>'updated'];
        } else {
            $results[] = ['task'=>'chi_context_3633','wp_id'=>$ch_id,'status'=>'regex_no_change'];
        }
    } else {
        $results[] = ['task'=>'chi_context_3633','wp_id'=>$ch_id,'status'=>'already_has_context'];
    }
} else {
    $results[] = ['task'=>'chi_context_3633','status'=>'khanh_chi_not_found_in_novel_3633'];
}

if (function_exists('litespeed_purge_all')) litespeed_purge_all();
echo json_encode(['results'=>$results], JSON_UNESCAPED_UNICODE|JSON_PRETTY_PRINT);
?>
