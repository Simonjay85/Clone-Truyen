<?php
ini_set('display_errors', 0);
header('Content-Type: application/json');
$input = json_decode(file_get_contents('php://input'), true);
if (!isset($input['secret_token']) || $input['secret_token'] !== 'ZEN_TRUYEN_2026_BYPASS') { http_response_code(401); exit; }
require_once('wp-load.php');
global $wpdb;

// Fetch ch8 last chapter for novels 4036 and 4084
$novel_ids = [4036, 4084];
$result = [];
foreach ($novel_ids as $nid) {
    $chapters = $wpdb->get_results($wpdb->prepare(
        "SELECT p.ID, p.post_title, p.post_content FROM {$wpdb->posts} p
         INNER JOIN {$wpdb->postmeta} pm ON p.ID = pm.post_id
         WHERE p.post_type = 'chuong' AND p.post_status != 'trash'
         AND pm.meta_key = '_truyen_id' AND pm.meta_value = %s
         ORDER BY p.post_date ASC",
        (string)$nid
    ));
    $total = count($chapters);
    $result[$nid] = ['total' => $total, 'chapters' => []];
    foreach ($chapters as $ch) {
        $result[$nid]['chapters'][] = [
            'wp_id' => $ch->ID,
            'title' => $ch->post_title,
            'len' => strlen($ch->post_content),
        ];
    }
    if ($total > 0) {
        $last = end($chapters);
        $result[$nid]['last_content'] = substr(strip_tags($last->post_content), 0, 1200);
        $result[$nid]['last_end'] = substr(strip_tags($last->post_content), -600);
    }
}

// Also scan Vạn An Fund across key novels
$van_an_novels = [3930, 3954, 3998, 4036, 4097];
$van_an_result = [];
foreach ($van_an_novels as $nid) {
    $count = $wpdb->get_var($wpdb->prepare(
        "SELECT COUNT(*) FROM {$wpdb->posts} p
         INNER JOIN {$wpdb->postmeta} pm ON p.ID = pm.post_id
         WHERE p.post_type = 'chuong' AND p.post_status != 'trash'
         AND pm.meta_key = '_truyen_id' AND pm.meta_value = %s
         AND p.post_content LIKE '%Vạn An%'",
        (string)$nid
    ));
    $van_an_result[$nid] = intval($count);
}
$result['van_an_fund'] = $van_an_result;

// Check Lâm Hoàng Yến in 4036
$lhy_count = $wpdb->get_var($wpdb->prepare(
    "SELECT COUNT(*) FROM {$wpdb->posts} p
     INNER JOIN {$wpdb->postmeta} pm ON p.ID = pm.post_id
     WHERE p.post_type = 'chuong' AND p.post_status != 'trash'
     AND pm.meta_key = '_truyen_id' AND pm.meta_value = %s
     AND p.post_content LIKE '%Lâm Hoàng Yến%'",
    '4036'
));
$result['lam_hoang_yen_4036'] = intval($lhy_count);

echo json_encode($result, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
?>
