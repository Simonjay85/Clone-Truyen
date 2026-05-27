<?php
ini_set('display_errors', 0);
header('Content-Type: application/json');
$input = json_decode(file_get_contents('php://input'), true);
if (!isset($input['secret_token']) || $input['secret_token'] !== 'ZEN_TRUYEN_2026_BYPASS') { http_response_code(401); exit; }
require_once('wp-load.php');
global $wpdb;

$wp_ids = [4138, 4229, 4237, 4277, 4285];
$result = [];
foreach ($wp_ids as $wid) {
    $post = get_post($wid);
    if ($post) {
        $content = strip_tags($post->post_content);
        $result[$wid] = [
            'title' => $post->post_title,
            'status' => $post->post_status,
            'len' => strlen($post->post_content),
            'content' => $content,
        ];
    } else {
        $result[$wid] = ['error' => 'not found'];
    }
}
echo json_encode($result, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
?>
