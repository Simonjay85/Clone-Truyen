<?php
header('Content-Type: application/json');
$input = json_decode(file_get_contents('php://input'), true);
if ($input['secret_token'] !== 'ZEN_TRUYEN_2026_BYPASS') { http_response_code(401); exit; }
require_once('wp-load.php');
$results = [];
foreach ($input['updates'] as $u) {
    $wp_id = intval($u['wp_id']);
    $post = get_post($wp_id);
    if (!$post) { $results[] = ['wp_id'=>$wp_id,'status'=>'not_found']; continue; }
    $data = ['ID'=>$wp_id];
    if (!empty($u['title'])) $data['post_title'] = $u['title'];
    if (!empty($u['content'])) $data['post_content'] = wp_kses_post($u['content']);
    wp_update_post($data);
    if (function_exists('litespeed_purge_post')) litespeed_purge_post($wp_id);
    $results[] = ['wp_id'=>$wp_id,'slug'=>$post->post_name,'status'=>'updated'];
}
if (function_exists('litespeed_purge_all')) litespeed_purge_all();
echo json_encode(['results'=>$results], JSON_UNESCAPED_UNICODE|JSON_PRETTY_PRINT);
?>
