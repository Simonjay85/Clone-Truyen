<?php
ini_set('display_errors', 0);
ini_set('max_execution_time', 30);
header('Content-Type: application/json');
$input = json_decode(file_get_contents('php://input'), true);
if (!isset($input['secret_token']) || $input['secret_token'] !== 'ZEN_TRUYEN_2026_BYPASS') { http_response_code(401); exit; }
require_once('wp-load.php');
global $wpdb;

$novel_id = intval($input['novel_id'] ?? 0);
$ch_num   = intval($input['ch_num'] ?? 0); // 0 = all first 3 chapters

// Direct DB query — faster than get_posts
$rows = $wpdb->get_results($wpdb->prepare(
    "SELECT p.ID, p.post_title, SUBSTRING(p.post_content,1,800) as excerpt
     FROM {$wpdb->posts} p
     INNER JOIN {$wpdb->postmeta} pm ON pm.post_id = p.ID AND pm.meta_key='_truyen_id' AND pm.meta_value=%s
     WHERE p.post_type='chuong' AND p.post_status='publish'
     ORDER BY p.post_date ASC LIMIT 4",
    (string)$novel_id
));

echo json_encode(['novel_id'=>$novel_id,'rows'=>$rows], JSON_UNESCAPED_UNICODE|JSON_PRETTY_PRINT);
?>
