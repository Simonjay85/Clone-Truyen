<?php
ini_set('display_errors', 0);
header('Content-Type: application/json');
$input = json_decode(file_get_contents('php://input'), true);
if (!isset($input['secret_token']) || $input['secret_token'] !== 'ZEN_TRUYEN_2026_BYPASS') { http_response_code(401); exit; }
require_once('wp-load.php');
global $wpdb;

$result = [];

// ID 2682: check chapter titles for "Giây Phút" pattern
$chs_2682 = $wpdb->get_results($wpdb->prepare(
    "SELECT p.ID, p.post_title FROM {$wpdb->posts} p
     INNER JOIN {$wpdb->postmeta} pm ON p.ID = pm.post_id
     WHERE p.post_type = 'chuong' AND p.post_status != 'trash'
     AND pm.meta_key = '_truyen_id' AND pm.meta_value = %s
     ORDER BY p.post_date ASC",
    '2682'
));
$result['2682_titles'] = array_map(fn($c) => ['id'=>$c->ID,'title'=>$c->post_title], $chs_2682);

// ID 3920: check how many chapters still have "Lâm Thế Hùng"
$lth_count = $wpdb->get_var($wpdb->prepare(
    "SELECT COUNT(*) FROM {$wpdb->posts} p
     INNER JOIN {$wpdb->postmeta} pm ON p.ID = pm.post_id
     WHERE p.post_type = 'chuong' AND p.post_status != 'trash'
     AND pm.meta_key = '_truyen_id' AND pm.meta_value = %s
     AND p.post_content LIKE '%Lâm Thế Hùng%'",
    '3920'
));
$result['3920_lam_the_hung'] = intval($lth_count);

// Also check ID 3861 which is the OTHER novel with Lâm Thế Hùng
$lth_3861 = $wpdb->get_var($wpdb->prepare(
    "SELECT COUNT(*) FROM {$wpdb->posts} p
     INNER JOIN {$wpdb->postmeta} pm ON p.ID = pm.post_id
     WHERE p.post_type = 'chuong' AND p.post_status != 'trash'
     AND pm.meta_key = '_truyen_id' AND pm.meta_value = %s
     AND p.post_content LIKE '%Lâm Thế Hùng%'",
    '3861'
));
$result['3861_lam_the_hung'] = intval($lth_3861);

// Check ID 2682: Bích Ngọc role issue (wife vs partner in ch8)
$ch8_2682 = end($chs_2682);
if ($ch8_2682) {
    $post = get_post($ch8_2682->ID);
    $result['2682_ch8_excerpt'] = substr(strip_tags($post->post_content), 0, 800);
}

echo json_encode($result, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
?>
