<?php
/**
 * fix_editorial_names.php
 * 1) ID 3920 — Sơn Mài: villains "Lâm Thế Hùng" + "Vương Quốc Bảo" copied from ID 3861 → rename
 * 2) ID 3998 — Lụa Bảo Lộc: CFO "Minh Thư" (Vạn An) copied from ID 3930 → rename → "Thanh Vân"
 * 3) ID 2773 — Chồng Nghèo Hào Môn: "Katherine Le" mixed Anh-Việt → "Lê Khánh Quỳnh"
 * 4) ID 3861 — replace clichéd "gót chân A-sin" with story-specific phrase
 * 5) ID 3954 — Trà Shan Tuyết: replace erroneous Hà Nội context with Hà Giang
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

// ==================== TASK 1: ID 3920 — Rename villain names ====================
fix_novel_chapters(3920, [
    'Lâm Thế Hùng'     => 'Phạm Đức Hùng',
    'Vương Quốc Bảo'   => 'Đặng Quốc Bảo',
    'ông Hùng'         => 'ông Phạm', // context-specific title
    'gót chân A-sin'   => 'điểm yếu trong hệ thống sản xuất',
    'Gót chân A-sin'   => 'Điểm yếu trong hệ thống sản xuất',
], $results, 'rename_villains_3920');

// Also rename Lâm Thế Hùng in ID 3861 chapter TITLES only (in content it stays since it's the original)
// Actually leave 3861 as-is — it's the original source. Only rename copies.

// ==================== TASK 2: ID 3998 — Rename CFO Minh Thư → Thanh Vân ====================
fix_novel_chapters(3998, [
    'Minh Thư'    => 'Thanh Vân',
    'chị Thư'     => 'chị Vân',
    'cô Thư'      => 'cô Vân',
    'bà Thư'      => 'bà Vân',
], $results, 'rename_cfo_3998');

// ==================== TASK 3: ID 2773 — "Katherine Le" → Vietnamese name ====================
fix_novel_chapters(2773, [
    'Katherine Le'   => 'Lê Khánh Quỳnh',
    'Katherine'      => 'Khánh Quỳnh',
    'Ms. Le'         => 'bà Quỳnh',
], $results, 'fix_name_2773');

// ==================== TASK 4: ID 3861 — Replace "gót chân A-sin" template phrase ====================
fix_novel_chapters(3861, [
    'gót chân A-sin'   => 'điểm yếu duy nhất trong toàn bộ kế hoạch',
    'Gót chân A-sin'   => 'Điểm yếu duy nhất trong toàn bộ kế hoạch',
], $results, 'fix_phrase_3861');

// ==================== TASK 5: ID 3954 — Fix Hà Nội → Hà Giang references ====================
fix_novel_chapters(3954, [
    ' Hà Nội '        => ' Hà Giang ',
    'ở Hà Nội'        => 'ở Hà Giang',
    'tại Hà Nội'      => 'tại Hà Giang',
    'về Hà Nội'       => 'về Hà Giang',
    'lên Hà Nội'      => 'xuống thị trấn',
    'phố Hà Nội'      => 'thị trấn Vinh Quang',
    'cà phê Hà Nội'   => 'quán nước Hoàng Su Phì',
    'café Hà Nội'     => 'quán nước Hoàng Su Phì',
], $results, 'fix_geography_3954');

if (function_exists('litespeed_purge_all')) litespeed_purge_all();
echo json_encode(['results'=>$results], JSON_UNESCAPED_UNICODE|JSON_PRETTY_PRINT);
?>
