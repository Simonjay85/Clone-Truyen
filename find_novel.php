<?php
ini_set('display_errors', 0);
header('Content-Type: application/json');
$input = json_decode(file_get_contents('php://input'), true);
if (!isset($input['secret_token']) || $input['secret_token'] !== 'ZEN_TRUYEN_2026_BYPASS') { http_response_code(401); exit; }
require_once('wp-load.php');
global $wpdb;

$nid = intval($input['nid'] ?? 0);
// Search for the truyen post with this ID
$post = get_post($nid);
$result = ['nid'=>$nid];
if ($post) {
    $result['post_title'] = $post->post_title;
    $result['post_type'] = $post->post_type;
    $result['post_status'] = $post->post_status;
}
// Also try to find chapters with _truyen_id = nid
$count = $wpdb->get_var($wpdb->prepare(
    "SELECT COUNT(*) FROM {$wpdb->posts} p
     INNER JOIN {$wpdb->postmeta} pm ON p.ID = pm.post_id
     WHERE p.post_type = 'chuong' AND pm.meta_key = '_truyen_id' AND pm.meta_value = %s",
    (string)$nid
));
$result['chapters_with_meta'] = intval($count);

// Also try to find by post title containing the novel ID number
$by_parent = $wpdb->get_results($wpdb->prepare(
    "SELECT p.ID, p.post_title, p.post_parent FROM {$wpdb->posts} p
     WHERE p.post_type = 'chuong' AND p.post_parent = %d LIMIT 3",
    $nid
));
$result['chapters_by_parent'] = count($by_parent);
if (!empty($by_parent)) {
    $result['sample'] = ['wp_id'=>$by_parent[0]->ID,'title'=>$by_parent[0]->post_title];
}

// List all chapters with that truyen_id in meta
$last = $wpdb->get_results($wpdb->prepare(
    "SELECT DISTINCT pm.meta_value FROM {$wpdb->postmeta} pm
     WHERE pm.meta_key = '_truyen_id' AND pm.meta_value LIKE %s LIMIT 5",
    '%' . substr($nid, 0, 3) . '%'
));
$result['nearby_truyen_ids'] = array_column($last, 'meta_value');

echo json_encode($result, JSON_UNESCAPED_UNICODE|JSON_PRETTY_PRINT);
?>
