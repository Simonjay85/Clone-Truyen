<?php
ini_set('display_errors', 1);
error_reporting(E_ALL);
header('Content-Type: application/json; charset=utf-8');

require_once('wp-load.php');

$secret = 'ZEN_TRUYEN_2026_BYPASS';
if (!isset($_GET['secret']) || $_GET['secret'] !== $secret) {
    http_response_code(403);
    echo json_encode(['error' => 'Unauthorized']);
    exit;
}

$json_file = ABSPATH . 'related_three_updates_20260525.json';
if (!file_exists($json_file)) {
    echo json_encode(['error' => 'Payload not found']);
    exit;
}

$payload = json_decode(file_get_contents($json_file), true);
if (!$payload || !isset($payload['secret']) || $payload['secret'] !== $secret || empty($payload['updates'])) {
    echo json_encode(['error' => 'Invalid payload']);
    exit;
}

$admins = get_users(['role' => 'administrator', 'number' => 1]);
if (!empty($admins)) {
    wp_set_current_user($admins[0]->ID);
}

$results = [];
foreach ($payload['updates'] as $item) {
    $post_id = intval($item['id'] ?? 0);
    if (!$post_id || get_post_type($post_id) !== 'truyen') {
        $results[] = ['id' => $post_id, 'success' => false, 'error' => 'Invalid story id'];
        continue;
    }

    $post_data = [
        'ID' => $post_id,
        'post_title' => wp_strip_all_tags($item['title'] ?? ''),
        'post_content' => wp_kses_post($item['content'] ?? ''),
        'post_excerpt' => sanitize_textarea_field($item['excerpt'] ?? ''),
        'post_status' => 'publish',
    ];
    $updated_post = wp_update_post($post_data, true);
    if (is_wp_error($updated_post)) {
        $results[] = ['id' => $post_id, 'success' => false, 'error' => $updated_post->get_error_message()];
        continue;
    }

    foreach (($item['meta'] ?? []) as $key => $value) {
        update_post_meta($post_id, sanitize_key($key), sanitize_text_field($value));
    }

    $chapter_results = [];
    foreach (($item['chapters'] ?? []) as $chapter) {
        $chapter_id = intval($chapter['id'] ?? 0);
        if (!$chapter_id || get_post_type($chapter_id) !== 'chuong') {
            $chapter_results[] = ['id' => $chapter_id, 'success' => false, 'error' => 'Invalid chapter id'];
            continue;
        }
        if ((int)get_post_meta($chapter_id, '_truyen_id', true) !== $post_id) {
            $chapter_results[] = ['id' => $chapter_id, 'success' => false, 'error' => 'Chapter does not belong to story'];
            continue;
        }
        $chapter_update = wp_update_post([
            'ID' => $chapter_id,
            'post_title' => wp_strip_all_tags($chapter['title'] ?? ''),
            'post_content' => wp_kses_post($chapter['content'] ?? ''),
            'post_status' => 'publish',
        ], true);
        $chapter_results[] = is_wp_error($chapter_update)
            ? ['id' => $chapter_id, 'success' => false, 'error' => $chapter_update->get_error_message()]
            : ['id' => $chapter_id, 'success' => true, 'title' => get_the_title($chapter_id)];
    }

    $results[] = [
        'id' => $post_id,
        'success' => true,
        'title' => get_the_title($post_id),
        'chapters_updated' => count(array_filter($chapter_results, fn($r) => !empty($r['success']))),
        'chapter_results' => $chapter_results,
    ];
}

if (function_exists('litespeed_purge_all')) {
    litespeed_purge_all();
}

echo json_encode(['success' => true, 'results' => $results], JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES);
?>
