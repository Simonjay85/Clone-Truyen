<?php
/**
 * fix_duplicates_2710.php
 * 1) Unpublish ID 2710 (exact duplicate of ID 2703)
 * 2) Differentiate ID 4060 from ID 4072 — change protagonist/villain names + key phrases
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

// ==================== TASK 1: Unpublish ID 2710 (duplicate novel) ====================
$post_2710 = get_post(2710);
if ($post_2710) {
    if ($post_2710->post_status === 'publish') {
        wp_update_post(['ID'=>2710, 'post_status'=>'draft']);
        if (function_exists('litespeed_purge_post')) litespeed_purge_post(2710);
        $results[] = ['task'=>'unpublish_2710','status'=>'set_to_draft','was'=>'publish'];
    } else {
        $results[] = ['task'=>'unpublish_2710','status'=>'already_'.$post_2710->post_status];
    }
} else {
    $results[] = ['task'=>'unpublish_2710','status'=>'post_not_found'];
}

// ==================== TASK 2: Differentiate ID 4060 from ID 4072 ====================
// 4060 = Cá tra (Pangasius) — Mekong delta context → rename protagonist Bách → Nguyễn Hoàng Bách (keep Bách)
// Change villain/hôn thê names in 4060 to differentiate from 4072
// 4060 protagonist: "Nguyễn Duy Bách" → keep as-is
// 4060 villain hôn thê: "Trần Khánh Linh" (or "Khánh Linh") → change to "Nguyễn Thu Hà"
// 4060 villain sếp: "Huỳnh Thế Hùng" → "Trương Minh Hùng"
// Also update location: ensure 4060 mentions Đồng Tháp / Châu Đốc consistently
// 4072 is the Khánh Hòa/island version — leave as-is (protagonist "Lâm Phong")

function fix_novel_chapters($novel_id, $replacements, &$results, $task) {
    global $wpdb;
    $chapters = $wpdb->get_results($wpdb->prepare(
        "SELECT p.ID, p.post_title, p.post_content FROM {$wpdb->posts} p
         INNER JOIN {$wpdb->postmeta} pm ON pm.post_id=p.ID AND pm.meta_key='_truyen_id' AND pm.meta_value=%s
         WHERE p.post_type='chuong' AND p.post_status='publish'",
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

// Rename villain names in ID 4060 to differentiate from ID 4072
fix_novel_chapters(4060, [
    'Trần Khánh Linh'    => 'Nguyễn Thu Hà',
    'Khánh Linh'         => 'Thu Hà',
    'cô Linh'            => 'cô Hà',
    'em Linh'            => 'em Hà',
    'Huỳnh Thế Hùng'     => 'Trương Minh Hùng',
    'Snow Pangasius'     => 'Cá Tra Đồng Tháp',
], $results, 'differentiate_4060');

// Also rename in ID 4072 (yến sào) to ensure villain names are distinct
fix_novel_chapters(4072, [
    'Nguyễn Khánh Linh'  => 'Phạm Thị Lan Ngọc',
    'Khánh Linh'         => 'Lan Ngọc',
    'cô Linh'            => 'cô Ngọc',
    'Trần Thế Hùng'      => 'Lê Thiên Hùng',
], $results, 'differentiate_4072');

if (function_exists('litespeed_purge_all')) litespeed_purge_all();
echo json_encode(['results'=>$results], JSON_UNESCAPED_UNICODE|JSON_PRETTY_PRINT);
?>
