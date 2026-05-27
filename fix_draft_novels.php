<?php
/**
 * fix_draft_novels.php
 * Unpublish các truyện không phù hợp:
 *   - ID 2710: duplicate hoàn toàn của ID 2703
 *   - ID 2020: thể loại xuyên không/sci-fi không phù hợp với site
 */
ini_set('display_errors', 0);
ini_set('max_execution_time', 60);
header('Content-Type: application/json');

$input = json_decode(file_get_contents('php://input'), true);
if (!isset($input['secret_token']) || $input['secret_token'] !== 'ZEN_TRUYEN_2026_BYPASS') {
    http_response_code(401); echo json_encode(['error'=>'Unauthorized']); exit;
}
require_once('wp-load.php');

$to_draft = [
    2710 => 'Duplicate hoàn toàn của ID 2703 (Giáo Sư Đuổi Học Trò)',
    2020 => 'Thể loại xuyên không/sci-fi không phù hợp với phong cách site',
];

$results = [];
foreach ($to_draft as $id => $reason) {
    $post = get_post($id);
    if (!$post) {
        $results[] = ['id' => $id, 'status' => 'not_found'];
        continue;
    }
    $old_status = $post->post_status;
    wp_update_post(['ID' => $id, 'post_status' => 'draft']);
    if (function_exists('litespeed_purge_post')) litespeed_purge_post($id);
    $results[] = [
        'id'         => $id,
        'title'      => $post->post_title,
        'old_status' => $old_status,
        'new_status' => 'draft',
        'reason'     => $reason,
    ];
}

if (function_exists('litespeed_purge_all')) litespeed_purge_all();

echo json_encode(['results' => $results], JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
?>
