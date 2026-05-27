<?php
ini_set('display_errors', 0);
ini_set('max_execution_time', 20);
header('Content-Type: application/json');
$input = json_decode(file_get_contents('php://input'), true);
if (!isset($input['secret_token']) || $input['secret_token'] !== 'ZEN_TRUYEN_2026_BYPASS') { http_response_code(401); exit; }
require_once('wp-load.php');
global $wpdb;
$novel_id = intval($input['novel_id'] ?? 0);
$ch_index = intval($input['ch_index'] ?? 0);
$row = $wpdb->get_row($wpdb->prepare(
    "SELECT p.ID, p.post_title, SUBSTRING(p.post_content,1,1000) as excerpt
     FROM {$wpdb->posts} p
     INNER JOIN {$wpdb->postmeta} pm ON pm.post_id=p.ID AND pm.meta_key='_truyen_id' AND pm.meta_value=%s
     WHERE p.post_type='chuong' AND p.post_status='publish'
     ORDER BY p.post_date ASC LIMIT 1 OFFSET %d",
    (string)$novel_id, $ch_index
));
echo json_encode($row, JSON_UNESCAPED_UNICODE|JSON_PRETTY_PRINT);
?>
