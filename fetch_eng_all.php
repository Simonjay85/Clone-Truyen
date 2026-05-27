<?php
ini_set('display_errors', 0);
ini_set('max_execution_time', 30);
header('Content-Type: application/json');
$input = json_decode(file_get_contents('php://input'), true);
if (!isset($input['secret_token']) || $input['secret_token'] !== 'ZEN_TRUYEN_2026_BYPASS') { http_response_code(401); exit; }
require_once('wp-load.php');
global $wpdb;

$result = [];
$nid = intval($input['nid'] ?? 2448);
$chapters = $wpdb->get_results($wpdb->prepare(
    "SELECT p.ID, p.post_title, p.post_content FROM {$wpdb->posts} p
     INNER JOIN {$wpdb->postmeta} pm ON p.ID = pm.post_id
     WHERE p.post_type = 'chuong' AND p.post_status != 'trash'
     AND pm.meta_key = '_truyen_id' AND pm.meta_value = %s
     ORDER BY p.post_date ASC",
    (string)$nid
));
foreach ($chapters as $ch) {
    $text = strip_tags($ch->post_content);
    if (preg_match_all('/[A-Za-z][a-zA-Z0-9\-_\.]{2,}(?:\s+[A-Z][a-z]+)?/u', $text, $m)) {
        $eng = array_unique($m[0]);
        sort($eng);
        $result[] = ['wp_id'=>$ch->ID,'title'=>$ch->post_title,'eng_words'=>array_values($eng)];
    }
}
echo json_encode($result, JSON_UNESCAPED_UNICODE|JSON_PRETTY_PRINT);
?>
