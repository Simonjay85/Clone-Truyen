<?php
/**
 * fix_text_errors_batch1.php
 * 1) ID 2668: "Hà Ngoại" (fictional) → "Đông Anh"; chapter title "Cuộc Đua Chạy Đua Thời Gian" → "Cuộc Chạy Đua Với Thời Gian"
 * 2) ID 1948: villain "Tô Khanh Khanh" → "Đặng Thu Minh" (conflict with ID 1933 protagonist)
 * 3) ID 2001: geographic inconsistency — "tòa án TP.HCM" / "Tòa Án Nhân Dân TP.HCM" references → "Tòa Án Nhân Dân TP Hà Nội"
 * 4) ID 4097: "Trịnh Hoàng Yến" → "Nguyễn Thị Huyền Yến" (differentiate from "Lâm Hoàng Yến" in batch)
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

function fix_novel_chapters($novel_id, $replacements, &$results, $task) {
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

// ==================== TASK 1: ID 2668 — Fix "Hà Ngoại" + chapter title typo ====================
fix_novel_chapters(2668, [
    'Hà Ngoại'                          => 'Đông Anh',
    'hà ngoại'                          => 'đông anh',
    'Cuộc Đua Chạy Đua Thời Gian'       => 'Cuộc Chạy Đua Với Thời Gian',
    'khu Hà Ngoại'                      => 'khu Đông Anh',
    'tại Hà Ngoại'                      => 'tại Đông Anh',
    'ở Hà Ngoại'                        => 'ở Đông Anh',
    'dự án Hà Ngoại'                    => 'dự án Đông Anh',
], $results, 'fix_ha_ngoai_2668');

// ==================== TASK 2: ID 1948 — Rename villain Tô Khanh Khanh ====================
fix_novel_chapters(1948, [
    'Tô Khanh Khanh'    => 'Đặng Thu Minh',
    'Khanh Khanh'       => 'Thu Minh',
    'cô Khanh'          => 'cô Minh',
    'bà Khanh'          => 'bà Minh',
    'chị Khanh'         => 'chị Minh',
    'Tô Khánh Khánh'    => 'Đặng Thu Minh',
], $results, 'rename_villain_1948');

// ==================== TASK 3: ID 2001 — Fix geographic inconsistency (court only) ====================
// Story is set in Hà Nội (Hàng Bông) but court references erroneously say TP.HCM
fix_novel_chapters(2001, [
    'Tòa Án Nhân Dân TP.HCM'       => 'Tòa Án Nhân Dân TP Hà Nội',
    'Tòa án Nhân dân TP.HCM'       => 'Tòa án Nhân dân TP Hà Nội',
    'Tòa án TP.HCM'                => 'Tòa án TP Hà Nội',
    'Tòa án Hồ Chí Minh'          => 'Tòa án Hà Nội',
    'phiên tòa tại TP.HCM'        => 'phiên tòa tại Hà Nội',
    'tòa án thành phố Hồ Chí Minh' => 'tòa án thành phố Hà Nội',
], $results, 'fix_geography_2001');

// ==================== TASK 4: ID 4097 — Differentiate Yến character name ====================
fix_novel_chapters(4097, [
    'Trịnh Hoàng Yến'   => 'Nguyễn Huyền Yến',
    'Hoàng Yến'         => 'Huyền Yến',
    'chị Yến'           => 'chị Yến',  // keep "chị Yến" as-is for flow
    'cô Yến'            => 'cô Yến',   // keep
    'bà Yến'            => 'bà Yến',   // keep
], $results, 'rename_yen_4097');

if (function_exists('litespeed_purge_all')) litespeed_purge_all();
echo json_encode(['results'=>$results], JSON_UNESCAPED_UNICODE|JSON_PRETTY_PRINT);
?>
