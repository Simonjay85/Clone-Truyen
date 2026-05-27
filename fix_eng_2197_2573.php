<?php
/**
 * fix_eng_2197_2573.php
 * ID 2197 (Thợ Hồ Nghìn Tỷ): Replace English "file" → "tập tin", "contract" → "hợp đồng"
 * ID 2573 (Gốm Sứ Bát Tràng): Replace SHA-256, PGP, Finite Element Method, iPhone 15 Pro Max
 *
 * NOTE: "CA" in ID 2197 is kept as-is — in construction context it means "Cơ quan/Chứng nhận An toàn"
 * which is valid in Vietnamese building industry documents.
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

function fix_novel_regex($novel_id, $patterns, &$results, $task) {
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
        foreach ($patterns as $pat => $rep) {
            $new_c = preg_replace($pat, $rep, $new_c);
            $new_t = preg_replace($pat, $rep, $new_t);
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

// ==================== ID 2197 — Thợ Hồ Nghìn Tỷ ====================
fix_novel_regex(2197, [
    '/\b(file|File)\b/u'           => 'tập tin',
    '/\bcontract\b/iu'             => 'hợp đồng',
], $results, 'fix_eng_2197');

// ==================== ID 2573 — Gốm Sứ Bát Tràng ====================
fix_novel_regex(2573, [
    '/\bSHA-256\b/u'               => 'mã băm SHA-256',
    '/\bSHA256\b/u'                => 'mã băm SHA-256',
    '/\bPGP\b/u'                   => 'mã hóa PGP',
    '/\bFinite Element Method\b/iu' => 'phương pháp phần tử hữu hạn',
    '/\bDell UltraSharp\b/u'       => 'màn hình Dell UltraSharp',
    '/\biPhone 15 Pro Max\b/u'     => 'điện thoại iPhone 15 Pro Max',
    '/\biPhone 15\b/u'             => 'điện thoại iPhone 15',
    '/\b(file|File)\b/u'           => 'tập tin',
    '/\bemail\b/iu'                => 'thư điện tử',
], $results, 'fix_eng_2573');

if (function_exists('litespeed_purge_all')) litespeed_purge_all();
echo json_encode(['results'=>$results], JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
?>
