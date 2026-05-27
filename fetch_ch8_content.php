<?php
ini_set('display_errors', 0);
ini_set('max_execution_time', 30);
header('Content-Type: application/json');
$input = json_decode(file_get_contents('php://input'), true);
if (!isset($input['secret_token']) || $input['secret_token'] !== 'ZEN_TRUYEN_2026_BYPASS') { http_response_code(401); exit; }
require_once('wp-load.php');
global $wpdb;

$nids = $input['nids'] ?? [];
$result = [];
foreach ($nids as $nid) {
    $chapters = $wpdb->get_results($wpdb->prepare(
        "SELECT p.ID, p.post_title, p.post_content FROM {$wpdb->posts} p
         INNER JOIN {$wpdb->postmeta} pm ON p.ID = pm.post_id
         WHERE p.post_type = 'chuong' AND p.post_status != 'trash'
         AND pm.meta_key = '_truyen_id' AND pm.meta_value = %s
         ORDER BY p.post_date ASC",
        (string)$nid
    ));
    if (!empty($chapters)) {
        $last = end($chapters);
        $result[] = [
            'nid' => $nid,
            'wp_id' => $last->ID,
            'title' => $last->post_title,
            'content_excerpt' => substr(strip_tags($last->post_content), 0, 800),
            'content_end' => substr(strip_tags($last->post_content), -500),
        ];
    }
}
echo json_encode($result, JSON_UNESCAPED_UNICODE|JSON_PRETTY_PRINT);
?>
