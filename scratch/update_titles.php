<?php
/**
 * Update novel titles to clickbait-style names
 */
require_once('wp-load.php');
header('Content-Type: application/json');

$raw = file_get_contents('php://input');
$input = json_decode($raw, true);

if (!isset($input['secret']) || $input['secret'] !== "ZEN_TRUYEN_2026_BYPASS") {
    echo json_encode(['error' => 'Unauthorized']);
    exit;
}

$updates = $input['updates']; // array of {id, title}
$results = [];

foreach ($updates as $u) {
    $post_id = intval($u['id']);
    $new_title = sanitize_text_field($u['title']);
    
    $result = wp_update_post([
        'ID' => $post_id,
        'post_title' => $new_title
    ]);
    
    if (is_wp_error($result)) {
        $results[] = ['id' => $post_id, 'error' => $result->get_error_message()];
    } else {
        $results[] = ['id' => $post_id, 'title' => $new_title, 'success' => true];
    }
}

if (function_exists('litespeed_purge_all')) {
    litespeed_purge_all();
}

echo json_encode(['success' => true, 'results' => $results], JSON_UNESCAPED_UNICODE);
?>
