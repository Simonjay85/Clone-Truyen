<?php
ini_set('display_errors', 0);
header('Content-Type: application/json');
$input = json_decode(file_get_contents('php://input'), true);
if (!isset($input['secret_token']) || $input['secret_token'] !== 'ZEN_TRUYEN_2026_BYPASS') { http_response_code(401); exit; }
require_once('wp-load.php');
global $wpdb;

// ID 2197: scan for English words
$chs_2197 = $wpdb->get_results($wpdb->prepare(
    "SELECT p.ID, p.post_title, p.post_content FROM {$wpdb->posts} p
     INNER JOIN {$wpdb->postmeta} pm ON p.ID = pm.post_id
     WHERE p.post_type = 'chuong' AND p.post_status != 'trash'
     AND pm.meta_key = '_truyen_id' AND pm.meta_value = %s
     ORDER BY p.post_date ASC",
    '2197'
));
$eng_2197 = [];
foreach ($chs_2197 as $ch) {
    $has_file = preg_match('/\b(file|File|FILE)\b/', $ch->post_content);
    $has_contract = preg_match('/\bcontract\b/i', $ch->post_content);
    $has_ca = preg_match('/\bCA\b/', $ch->post_content);
    if ($has_file || $has_contract || $has_ca) {
        $eng_2197[] = ['id'=>$ch->ID,'title'=>$ch->post_title,'file'=>$has_file,'contract'=>$has_contract,'ca'=>$has_ca];
    }
}

// ID 2013: last chapter content
$chs_2013 = $wpdb->get_results($wpdb->prepare(
    "SELECT p.ID, p.post_title, p.post_content FROM {$wpdb->posts} p
     INNER JOIN {$wpdb->postmeta} pm ON p.ID = pm.post_id
     WHERE p.post_type = 'chuong' AND p.post_status != 'trash'
     AND pm.meta_key = '_truyen_id' AND pm.meta_value = %s
     ORDER BY p.post_date ASC",
    '2013'
));
$total_2013 = count($chs_2013);
$last_2013 = $total_2013 > 0 ? end($chs_2013) : null;
$result_2013 = ['total'=>$total_2013,'chapters'=>array_map(fn($c)=>['id'=>$c->ID,'title'=>$c->post_title,'len'=>strlen($c->post_content)], $chs_2013)];
if ($last_2013) {
    $result_2013['last_content'] = strip_tags($last_2013->post_content);
}

echo json_encode([
    '2197_english' => $eng_2197,
    '2013' => $result_2013,
], JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
?>
