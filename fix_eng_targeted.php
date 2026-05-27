<?php
/**
 * fix_eng_targeted.php
 * Targeted English word replacements based on actual content scan
 * ID 2448: "File" (capitalized), "audio", "flash", "camera" → Vietnamese
 * ID 2259: "laptop" → "máy tính xách tay"
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

function fix_novel_ci($novel_id, $replacements, &$results, $task) {
    // Case-insensitive replacements using preg_replace
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
        foreach ($replacements as $pattern => $replacement) {
            $new_c = preg_replace($pattern, $replacement, $new_c);
            $new_t = preg_replace($pattern, $replacement, $new_t);
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

// ==================== ID 2448 — Tea industry novel ====================
// "File" (capitalized, standalone) → "Tập tin" / "Hồ sơ" based on context
// Since we can't know context for each "File", use "hồ sơ" (document/record) which fits tea industry fraud context
fix_novel_ci(2448, [
    // "File " capitalized at start of sentence or standalone
    '/\bFile\s+ghi\b/u'         => 'Bản ghi',
    '/\bFile\s+âm\b/u'          => 'Tập tin âm',
    '/\bFile\s+ảnh\b/u'         => 'Ảnh',
    '/\bFile\s+video\b/u'       => 'Video',
    '/\bFile\s+tài\s+liệu\b/u'  => 'Tài liệu',
    '/\bFile\s+hợp\s+đồng\b/u'  => 'Hợp đồng',
    '/\bFile\s+dữ\s+liệu\b/u'   => 'Dữ liệu',
    // generic File standalone
    '/\bFile\b/u'               => 'Tập tin',
    // audio context
    '/\bfile\s+audio\b/iu'      => 'bản ghi âm',
    '/\baudio\s+recording\b/iu' => 'bản ghi âm',
    '/\bfile\b/iu'              => 'tập tin',
    // flash drive
    '/\bflash\s+drive\b/iu'     => 'ổ USB',
    '/\bUSB\s+flash\b/iu'       => 'ổ USB',
    // camera — keep as it's a loan word in Vietnamese
], $results, 'fix_eng_2448');

// ==================== ID 2259 — Bakery/food safety novel ====================
fix_novel_ci(2259, [
    '/\blaptop\b/iu'            => 'máy tính xách tay',
    '/\bchiếc\s+laptop\b/iu'    => 'chiếc máy tính xách tay',
    '/\bcái\s+laptop\b/iu'      => 'cái máy tính xách tay',
    '/\bmàn\s+hình\s+laptop\b/iu' => 'màn hình máy tính',
], $results, 'fix_eng_2259');

if (function_exists('litespeed_purge_all')) litespeed_purge_all();
echo json_encode(['results'=>$results], JSON_UNESCAPED_UNICODE|JSON_PRETTY_PRINT);
?>
