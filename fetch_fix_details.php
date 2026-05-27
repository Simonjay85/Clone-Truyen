<?php
ini_set('display_errors', 0);
header('Content-Type: application/json');
$input = json_decode(file_get_contents('php://input'), true);
if (!isset($input['secret_token']) || $input['secret_token'] !== 'ZEN_TRUYEN_2026_BYPASS') { http_response_code(401); exit; }
require_once('wp-load.php');
global $wpdb;

$result = [];

// --- ID 2561: find ch7 and ch8 titles and WP IDs ---
$chapters_2561 = $wpdb->get_results($wpdb->prepare(
    "SELECT p.ID, p.post_title FROM {$wpdb->posts} p
     INNER JOIN {$wpdb->postmeta} pm ON p.ID = pm.post_id
     WHERE p.post_type = 'chuong' AND p.post_status != 'trash'
     AND pm.meta_key = '_truyen_id' AND pm.meta_value = %s
     ORDER BY p.post_date ASC",
    '2561'
));
$result['2561'] = array_map(fn($c) => ['id'=>$c->ID,'title'=>$c->post_title], $chapters_2561);

// --- ID 2668: list chapters + scan for "Hà Ngoại" ---
$chapters_2668 = $wpdb->get_results($wpdb->prepare(
    "SELECT p.ID, p.post_title, p.post_content FROM {$wpdb->posts} p
     INNER JOIN {$wpdb->postmeta} pm ON p.ID = pm.post_id
     WHERE p.post_type = 'chuong' AND p.post_status != 'trash'
     AND pm.meta_key = '_truyen_id' AND pm.meta_value = %s
     ORDER BY p.post_date ASC",
    '2668'
));
$result['2668'] = [];
foreach ($chapters_2668 as $ch) {
    $ha_ngoai_count = substr_count($ch->post_content, 'Hà Ngoại');
    $result['2668'][] = ['id'=>$ch->ID,'title'=>$ch->post_title,'ha_ngoai'=>$ha_ngoai_count,'len'=>strlen($ch->post_content)];
}

// --- ID 3998: scan for Minh Thư and Vạn An ---
$chapters_3998 = $wpdb->get_results($wpdb->prepare(
    "SELECT p.ID, p.post_title, p.post_content FROM {$wpdb->posts} p
     INNER JOIN {$wpdb->postmeta} pm ON p.ID = pm.post_id
     WHERE p.post_type = 'chuong' AND p.post_status != 'trash'
     AND pm.meta_key = '_truyen_id' AND pm.meta_value = %s
     ORDER BY p.post_date ASC",
    '3998'
));
$result['3998'] = [];
foreach ($chapters_3998 as $ch) {
    $minh_thu = substr_count($ch->post_content, 'Minh Thư');
    $van_an = substr_count($ch->post_content, 'Vạn An');
    if ($minh_thu > 0 || $van_an > 0) {
        $result['3998'][] = ['id'=>$ch->ID,'title'=>$ch->post_title,'minh_thu'=>$minh_thu,'van_an'=>$van_an];
    }
}

// --- ID 3930: also verify Minh Thư/Vạn An ---
$mt_count_3930 = $wpdb->get_var($wpdb->prepare(
    "SELECT COUNT(*) FROM {$wpdb->posts} p
     INNER JOIN {$wpdb->postmeta} pm ON p.ID = pm.post_id
     WHERE p.post_type = 'chuong' AND p.post_status != 'trash'
     AND pm.meta_key = '_truyen_id' AND pm.meta_value = %s
     AND p.post_content LIKE '%Minh Thư%'",
    '3930'
));
$result['3930_minh_thu'] = intval($mt_count_3930);

echo json_encode($result, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
?>
