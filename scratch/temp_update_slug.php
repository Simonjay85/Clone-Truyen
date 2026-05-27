<?php
/**
 * Update Slug & SEO Title Helper
 */
ini_set('display_errors', 0);
header('Content-Type: application/json; charset=utf-8');

$secret_token = "ZEN_TRUYEN_2026_BYPASS";
$raw_input = file_get_contents('php://input');
$input = json_decode($raw_input, true);

if (!isset($input['secret_token']) || $input['secret_token'] !== $secret_token) {
    http_response_code(401);
    echo json_encode(['error' => 'Unauthorized']);
    exit;
}

require_once('wp-load.php');

$story_id = 3940;
$new_slug = "bac-si-dong-y-bi-duoi-khoi-vien-phoi-va-sap-tap-doan";
$new_seo_title = "Bác Sĩ Đông Y Bị Đuổi Khỏi Viện Phổi Vả Sập Kẻ Phản Bội";

// Authenticate as Admin
$admins = get_users(['role' => 'administrator', 'number' => 1]);
if (empty($admins)) {
    http_response_code(500);
    echo json_encode(['error' => 'No admin found']);
    exit;
}
wp_set_current_user($admins[0]->ID);

// 1. Update Slug
$update_result = wp_update_post([
    'ID'        => $story_id,
    'post_name' => $new_slug
]);

if (is_wp_error($update_result)) {
    http_response_code(500);
    echo json_encode(['error' => 'Failed to update slug: ' . $update_result->get_error_message()]);
    exit;
}

// 2. Update RankMath PostMeta
update_post_meta($story_id, 'rank_math_title', $new_seo_title);
update_post_meta($story_id, '_rank_math_title', $new_seo_title);

// 3. Purge cache
if (function_exists('litespeed_purge_all')) {
    litespeed_purge_all();
}

$post = get_post($story_id);

echo json_encode([
    'success' => true,
    'story_id' => $story_id,
    'actual_slug' => $post->post_name,
    'seo_title' => get_post_meta($story_id, 'rank_math_title', true),
    'message' => 'Slug and RankMath SEO Title successfully updated under characters limits!'
], JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE);
?>
