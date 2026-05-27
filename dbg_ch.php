<?php
ini_set('display_errors', 1);
header('Content-Type: application/json');
$input = json_decode(file_get_contents('php://input'), true);
if (!isset($input['secret_token']) || $input['secret_token'] !== 'ZEN_TRUYEN_2026_BYPASS') { http_response_code(401); exit; }
require_once('wp-load.php');
global $wpdb;
$nid = intval($input['nid'] ?? 0);
$chapters = $wpdb->get_results($wpdb->prepare(
    "SELECT p.ID, p.post_title, p.post_status, p.post_content FROM {$wpdb->posts} p
     INNER JOIN {$wpdb->postmeta} pm ON p.ID = pm.post_id
     WHERE p.post_type = 'chuong'
     AND pm.meta_key = '_truyen_id' AND pm.meta_value = %s
     ORDER BY p.post_date ASC",
    (string)$nid
));
$out = [];
foreach ($chapters as $ch) {
    $out[] = ['ID'=>$ch->ID, 'title'=>$ch->post_title, 'status'=>$ch->post_status, 'len'=>strlen($ch->post_content)];
}
echo json_encode(['nid'=>$nid,'count'=>count($out),'chapters'=>$out,'last_error'=>$wpdb->last_error], JSON_UNESCAPED_UNICODE);
?>
