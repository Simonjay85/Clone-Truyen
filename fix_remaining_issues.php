<?php
/**
 * fix_remaining_issues.php
 * 1) ID 2573 WP4122 ch8: Append Phạm Thu Hương subplot resolution
 * 2) ID 2682 WP4542 ch1: Rename "Giây Phút Định Mệnh" → avoid dup with ch8
 * 3) ID 2448: Replace English tech words (laptop, blockchain, hash, file, email)
 * 4) ID 2259: Replace English tech words (file, cloud, email)
 * 5) ID 2587: Replace English tech terms (Finite Element Method, SHA-256, PGP, etc.)
 */
ini_set('display_errors', 0);
ini_set('max_execution_time', 120);
header('Content-Type: application/json');

$input = json_decode(file_get_contents('php://input'), true);
if (!isset($input['secret_token']) || $input['secret_token'] !== 'ZEN_TRUYEN_2026_BYPASS') {
    http_response_code(401); echo json_encode(['error'=>'Unauthorized']); exit;
}
require_once('wp-load.php');
$results = [];

// ==================== TASK 1: ID 2573 WP4122 ch8 — Append Hương resolution ====================
$ch8_2573 = get_post(4122);
if ($ch8_2573) {
    $bridge = '

<hr>

<p>Phạm Thu Hương đến vào cuối buổi chiều, khi phần lớn khách tham quan đã ra về và chỉ còn các nhà sưu tập đứng lại trước những tác phẩm cuối cùng chưa có chủ.</p>

<p>Minh nhận ra bà ngay từ đầu hành lang — chiếc áo dài xanh rêu, mái tóc bạch kim búi gọn. Bà dừng lại trước bộ gốm hoa lam mà anh đã giữ lại không bán — bảy chiếc bình thấp, men chảy theo đường vân đất sét Ba Vì, mỗi cái một mùa trong năm.</p>

<p>"Tôi nghe người ta nói anh sẽ không đến." Bà không quay lại khi nói.</p>

<p>"Tôi cũng nghĩ vậy." Minh đứng cạnh bà, nhìn vào bộ bình. "Bà đến vì triển lãm hay vì chuyện khác?"</p>

<p>Hương im lặng một lúc. "Tôi đến vì cả hai." Bà mở ví, lấy ra một phong bì đã gập. "Quyết định của hội đồng thừa kế. Khoản thế chấp máy móc lò nung — xóa. Anh giữ xưởng."</p>

<p>Minh không cầm phong bì ngay. "Điều kiện?"</p>

<p>"Không có điều kiện." Bà nhìn thẳng vào anh lần đầu. "Có những thứ ông nhà tôi để lại mà tôi giữ không đúng cách. Xưởng gốm là một trong số đó." Bà đặt phong bì lên bệ trưng bày cạnh bộ bình hoa lam. "Giữ lấy mà làm. Ông ấy sẽ muốn thế."</p>

<p>Bà quay người đi trước khi Minh kịp trả lời. Gót giày nhỏ lại trong tiếng ồn ào của buổi tổng kết triển lãm.</p>

<p>Anh cầm phong bì lên. Không mở — chỉ giữ trong tay cho đến khi ban tổ chức tắt đèn phòng trưng bày.</p>';

    $new_content = $ch8_2573->post_content . $bridge;
    wp_update_post(['ID'=>4122,'post_content'=>wp_kses_post($new_content)]);
    if (function_exists('litespeed_purge_post')) litespeed_purge_post(4122);
    $results[] = ['task'=>'ch8_2573_huong_resolution','wp_id'=>4122,'status'=>'appended'];
}

// ==================== TASK 2: ID 2682 WP4542 ch1 — Rename title ====================
$ch1_2682 = get_post(4542);
if ($ch1_2682) {
    wp_update_post(['ID'=>4542,'post_title'=>'Chương 1: Ngày Cuối Ở Thung Lũng']);
    if (function_exists('litespeed_purge_post')) litespeed_purge_post(4542);
    $results[] = ['task'=>'ch1_2682_rename','wp_id'=>4542,'old_title'=>$ch1_2682->post_title,'new_title'=>'Chương 1: Ngày Cuối Ở Thung Lũng','status'=>'updated'];
}

// ==================== TASK 3: ID 2448 — Replace English tech words ====================
function fix_novel_chapters_eng($novel_id, $replacements, &$results, $task) {
    global $wpdb;
    $chapters = $wpdb->get_results($wpdb->prepare(
        "SELECT p.ID, p.post_title, p.post_content FROM {$wpdb->posts} p
         INNER JOIN {$wpdb->postmeta} pm ON p.ID = pm.post_id
         WHERE p.post_type = 'chuong' AND p.post_status != 'trash'
         AND pm.meta_key = '_truyen_id' AND pm.meta_value = %s
         ORDER BY p.post_date ASC",
        (string)$novel_id
    ));
    $changed = 0;
    foreach ($chapters as $ch) {
        $new_c = $ch->post_content;
        $new_t = $ch->post_title;
        foreach ($replacements as $o => $n) {
            $new_c = str_replace($o, $n, $new_c);
            $new_t = str_replace($o, $n, $new_t);
        }
        if ($new_c !== $ch->post_content || $new_t !== $ch->post_title) {
            $update = ['ID'=>$ch->ID,'post_content'=>wp_kses_post($new_c)];
            if ($new_t !== $ch->post_title) $update['post_title'] = $new_t;
            wp_update_post($update);
            if (function_exists('litespeed_purge_post')) litespeed_purge_post($ch->ID);
            $changed++;
        }
    }
    $results[] = ['task'=>$task,'novel_id'=>$novel_id,'chapters_changed'=>$changed,'total'=>count($chapters)];
}

fix_novel_chapters_eng(2448, [
    // laptop — only standalone usage, not inside other words
    ' laptop '          => ' máy tính xách tay ',
    ' laptop,'          => ' máy tính xách tay,',
    ' laptop.'          => ' máy tính xách tay.',
    'chiếc laptop'      => 'chiếc máy tính xách tay',
    'cái laptop'        => 'cái máy tính xách tay',
    'màn hình laptop'   => 'màn hình máy tính',
    // blockchain
    'blockchain'        => 'chuỗi khối',
    'Blockchain'        => 'Chuỗi khối',
    // hash
    ' hash '            => ' mã băm ',
    'hash value'        => 'giá trị mã băm',
    'mã hash'           => 'mã băm',
    // file — context-sensitive (avoid changing "hồ sơ" that already uses Vietnamese)
    ' file '            => ' tập tin ',
    ' file,'            => ' tập tin,',
    ' file.'            => ' tập tin.',
    'các file'          => 'các tập tin',
    'tệp file'          => 'tập tin',
    'file dữ liệu'      => 'tập tin dữ liệu',
    'file hợp đồng'     => 'hồ sơ hợp đồng',
    'file tài liệu'     => 'tài liệu',
    'file ảnh'          => 'ảnh',
    'file video'        => 'video',
    // email
    ' email '           => ' thư điện tử ',
    ' email,'           => ' thư điện tử,',
    ' email.'           => ' thư điện tử.',
    'gửi email'         => 'gửi thư điện tử',
    'nhận email'        => 'nhận thư điện tử',
    'địa chỉ email'     => 'địa chỉ thư điện tử',
    'hộp email'         => 'hộp thư',
    'một email'         => 'một thư điện tử',
    'cái email'         => 'thư điện tử đó',
], $results, 'fix_eng_2448');

// ==================== TASK 4: ID 2259 — Replace English tech words ====================
fix_novel_chapters_eng(2259, [
    // file
    ' file '            => ' tập tin ',
    ' file,'            => ' tập tin,',
    ' file.'            => ' tập tin.',
    'các file'          => 'các tập tin',
    'file dữ liệu'      => 'tập tin dữ liệu',
    'file hợp đồng'     => 'hồ sơ hợp đồng',
    'file tài liệu'     => 'tài liệu',
    'tệp file'          => 'tập tin',
    // cloud
    ' cloud '           => ' đám mây ',
    'cloud storage'     => 'lưu trữ đám mây',
    'Cloud Storage'     => 'Lưu trữ đám mây',
    'lưu trữ cloud'     => 'lưu trữ đám mây',
    'dịch vụ cloud'     => 'dịch vụ điện toán đám mây',
    'hệ thống cloud'    => 'hệ thống đám mây',
    // email
    ' email '           => ' thư điện tử ',
    ' email,'           => ' thư điện tử,',
    ' email.'           => ' thư điện tử.',
    'gửi email'         => 'gửi thư điện tử',
    'nhận email'        => 'nhận thư điện tử',
    'địa chỉ email'     => 'địa chỉ thư điện tử',
    'hộp email'         => 'hộp thư',
    'một email'         => 'một thư điện tử',
], $results, 'fix_eng_2259');

// ==================== TASK 5: ID 2587 — Replace English tech terms ====================
fix_novel_chapters_eng(2587, [
    // Finite Element Method → Vietnamese technical term
    'Finite Element Method'     => 'phương pháp phần tử hữu hạn',
    'finite element method'     => 'phương pháp phần tử hữu hạn',
    'phương pháp Finite Element'=> 'phương pháp phần tử hữu hạn',
    // SHA-256 — keep as technical standard but add context
    'thuật toán SHA-256'        => 'thuật toán băm SHA-256',
    'mã SHA-256'                => 'mã băm SHA-256',
    // PGP — keep acronym but add context on first use
    'mã hóa PGP'                => 'mã hóa PGP (Pretty Good Privacy)',
    'dùng PGP'                  => 'dùng mã hóa PGP',
    ' PGP '                     => ' mã hóa PGP ',
    // Dell UltraSharp — add context
    'màn hình Dell UltraSharp'  => 'màn hình Dell UltraSharp',  // already has context, keep
    'Dell UltraSharp'           => 'màn hình Dell UltraSharp',
    // iPhone 15 Pro Max — keep product name, just normalize
    'iPhone 15 Pro Max'         => 'điện thoại iPhone 15 Pro Max',
    'chiếc iPhone 15 Pro Max'   => 'chiếc điện thoại iPhone 15 Pro Max',
    // Generic tech English
    ' file '                    => ' tập tin ',
    ' file,'                    => ' tập tin,',
    ' file.'                    => ' tập tin.',
    'các file'                  => 'các tập tin',
    'file dữ liệu'              => 'tập tin dữ liệu',
    ' email '                   => ' thư điện tử ',
    ' email,'                   => ' thư điện tử,',
    ' email.'                   => ' thư điện tử.',
    'gửi email'                 => 'gửi thư điện tử',
    'nhận email'                => 'nhận thư điện tử',
    'một email'                 => 'một thư điện tử',
], $results, 'fix_eng_2587');

if (function_exists('litespeed_purge_all')) litespeed_purge_all();
echo json_encode(['results'=>$results], JSON_UNESCAPED_UNICODE|JSON_PRETTY_PRINT);
?>
