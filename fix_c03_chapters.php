<?php
/**
 * fix_c03_chapters.php
 * Replace "C03 xuất quân" deus ex machina across IDs 3724, 3789, 3801, 3837
 * Fix chapter titles that explicitly name "C03"
 * Replace with protagonist-driven resolution language
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

// --- Common C03 text replacements (applied to all 4 novels) ---
$c03_replacements = [
    'C03 xuất quân'                     => 'cơ quan điều tra kinh tế tiếp nhận hồ sơ',
    'Sự Can Thiệp Của C03'              => 'Phán Quyết Sau Đêm Phản Công',
    'can thiệp của C03'                 => 'kết quả điều tra độc lập',
    'C03 đã xuất quân'                  => 'cơ quan điều tra đã hành động sau khi nhận đủ bằng chứng',
    'Cục Cảnh sát Kinh tế C03'          => 'Cơ quan Cảnh sát Điều tra kinh tế',
    'Cục Cảnh sát Kinh tế (C03)'        => 'Cơ quan Cảnh sát Điều tra kinh tế',
    'lực lượng C03'                     => 'lực lượng điều tra kinh tế',
    'đội C03'                           => 'đội điều tra',
    'C03 bao vây'                       => 'lực lượng điều tra bao vây',
    'C03 ập vào'                        => 'lực lượng điều tra ập vào',
    'C03 xuất hiện'                     => 'lực lượng điều tra xuất hiện',
    'C03 tiến hành'                     => 'cơ quan điều tra tiến hành',
    'điều tra của C03'                  => 'điều tra của cơ quan chức năng',
    ' C03 '                             => ' cơ quan điều tra kinh tế ',
    '(C03 Xuất Quân)'                   => '',
    '& Sự Trừng Phạt Của Pháp Luật'    => 'Và Lẽ Công Bằng',
];

function apply_c03_fixes($novel_id, $replacements, $title_fixes, &$results) {
    $chapters = get_posts([
        'post_type' => 'chuong', 'posts_per_page' => -1, 'orderby' => 'date', 'order' => 'ASC',
        'meta_query' => [['key'=>'_truyen_id','value'=>(string)$novel_id,'compare'=>'=']]
    ]);
    $changed = 0;
    foreach ($chapters as $ch) {
        $new_c = $ch->post_content;
        $new_t = $ch->post_title;
        foreach ($replacements as $o => $n) {
            $new_c = str_replace($o, $n, $new_c);
            $new_t = str_replace($o, $n, $new_t);
        }
        // Apply specific title fixes for this chapter
        if (isset($title_fixes[$ch->ID])) {
            $new_t = $title_fixes[$ch->ID];
        }
        if ($new_c !== $ch->post_content || $new_t !== $ch->post_title) {
            $update = ['ID'=>$ch->ID,'post_content'=>wp_kses_post($new_c)];
            if ($new_t !== $ch->post_title) $update['post_title'] = $new_t;
            wp_update_post($update);
            if (function_exists('litespeed_purge_post')) litespeed_purge_post($ch->ID);
            $changed++;
        }
    }
    $results[] = ['task'=>'fix_c03','novel_id'=>$novel_id,'chapters_changed'=>$changed,'total'=>count($chapters)];
}

// ID 3724 — WP3732 title has explicit "C03"
apply_c03_fixes(3724, $c03_replacements, [
    3732 => 'Chương 7: Phiên Livestream Gọi Vốn Và Bẫy Phản Công',
], $results);

// ID 3789 — WP3799 title has "(C03 Xuất Quân)"
apply_c03_fixes(3789, $c03_replacements, [
    3799 => 'Chương 9: Lưới Trời Lồng Lộng',
], $results);

// ID 3801 — no specific title fix, just content
apply_c03_fixes(3801, $c03_replacements, [], $results);

// ID 3837 — WP3848 has C03 in content
apply_c03_fixes(3837, $c03_replacements, [
    3848 => 'Chương 10: Lẽ Công Bằng Tại Cannes',
], $results);

if (function_exists('litespeed_purge_all')) litespeed_purge_all();
echo json_encode(['results'=>$results], JSON_UNESCAPED_UNICODE|JSON_PRETTY_PRINT);
?>
