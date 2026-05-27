<?php
ini_set('display_errors', 1);
ini_set('max_execution_time', 30);
header('Content-Type: application/json');
$input = json_decode(file_get_contents('php://input'), true);
if (!isset($input['secret_token']) || $input['secret_token'] !== 'ZEN_TRUYEN_2026_BYPASS') { http_response_code(401); exit; }
require_once('wp-load.php');
global $wpdb;

$nid = intval($input['nid'] ?? 0);
$chapters = $wpdb->get_results($wpdb->prepare(
    "SELECT p.ID, p.post_title, p.post_content FROM {$wpdb->posts} p
     INNER JOIN {$wpdb->postmeta} pm ON p.ID = pm.post_id
     WHERE p.post_type = 'chuong' AND p.post_status != 'trash'
     AND pm.meta_key = '_truyen_id' AND pm.meta_value = %s
     ORDER BY p.post_date ASC",
    (string)$nid
));
$total = count($chapters);
if ($total === 0) { echo json_encode(['error'=>'no chapters','nid'=>$nid,'last_error'=>$wpdb->last_error]); exit; }
$last = end($chapters);
echo json_encode([
    'nid'=>$nid, 'total'=>$total, 'wp_id'=>$last->ID, 'title'=>$last->post_title,
    'excerpt'=>substr(strip_tags($last->post_content),0,600),
    'ending'=>substr(strip_tags($last->post_content),-600),
], JSON_UNESCAPED_UNICODE|JSON_PRETTY_PRINT);
?>
