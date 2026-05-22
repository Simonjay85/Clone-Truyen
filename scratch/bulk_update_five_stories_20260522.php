<?php
ini_set('display_errors', 0);
header('Content-Type: application/json; charset=utf-8');

$input = json_decode(file_get_contents('php://input'), true);
if (($input['secret_token'] ?? '') !== 'ZEN_TRUYEN_2026_BYPASS') {
    http_response_code(401);
    echo json_encode(['success' => false, 'error' => 'bad token'], JSON_UNESCAPED_UNICODE);
    exit;
}

require_once('wp-load.php');
require_once(ABSPATH . 'wp-admin/includes/image.php');
require_once(ABSPATH . 'wp-admin/includes/file.php');
require_once(ABSPATH . 'wp-admin/includes/media.php');

$admins = get_users(['role' => 'administrator', 'number' => 1]);
if (!empty($admins)) {
    wp_set_current_user($admins[0]->ID);
}

$results = [];
foreach (($input['stories'] ?? []) as $story_data) {
    $story_id = intval($story_data['story_id'] ?? 0);
    $story = get_post($story_id);
    if (!$story || $story->post_type !== 'truyen') {
        $results[] = ['story_id' => $story_id, 'success' => false, 'error' => 'story not found'];
        continue;
    }

    $title = sanitize_text_field($story_data['title'] ?? $story->post_title);
    $intro = wp_kses_post($story_data['intro'] ?? $story->post_content);
    $excerpt = sanitize_textarea_field(wp_trim_words(wp_strip_all_tags($intro), 58, '...'));

    $update = wp_update_post([
        'ID' => $story_id,
        'post_title' => $title,
        'post_content' => $intro,
        'post_excerpt' => $excerpt,
        'post_status' => 'publish',
    ], true);

    if (is_wp_error($update)) {
        $results[] = ['story_id' => $story_id, 'success' => false, 'error' => $update->get_error_message()];
        continue;
    }

    $chapter_posts = get_posts([
        'post_type' => 'chuong',
        'post_status' => 'any',
        'meta_key' => '_truyen_id',
        'meta_value' => $story_id,
        'posts_per_page' => -1,
        'orderby' => 'ID',
        'order' => 'ASC',
    ]);

    $updated_chapters = [];
    foreach (($story_data['chapters'] ?? []) as $index => $chap) {
        if (!isset($chapter_posts[$index])) {
            continue;
        }
        $chap_id = $chapter_posts[$index]->ID;
        $chap_title = sanitize_text_field($chap['title'] ?? ('Chương ' . ($index + 1)));
        $chap_content = wp_kses_post($chap['content'] ?? '');
        $res = wp_update_post([
            'ID' => $chap_id,
            'post_title' => $chap_title,
            'post_content' => $chap_content,
            'post_status' => 'publish',
        ], true);
        if (!is_wp_error($res)) {
            $updated_chapters[] = ['id' => $chap_id, 'title' => $chap_title];
        }
    }

    $cover_status = 'not provided';
    $cover_filename = sanitize_file_name($story_data['cover_local_filename'] ?? '');
    if (!empty($cover_filename)) {
        $local_path = ABSPATH . $cover_filename;
        if (file_exists($local_path)) {
            $tmp = tempnam(get_temp_dir(), 'coverfive');
            if (copy($local_path, $tmp)) {
                $file_array = [
                    'name' => preg_replace('/[^a-zA-Z0-9_.-]/', '-', pathinfo($cover_filename, PATHINFO_FILENAME)) . '-' . time() . '.png',
                    'tmp_name' => $tmp,
                ];
                $attach_id = media_handle_sideload($file_array, $story_id);
                if (!is_wp_error($attach_id)) {
                    set_post_thumbnail($story_id, $attach_id);
                    $cover_status = 'updated';
                } else {
                    $cover_status = 'media error: ' . $attach_id->get_error_message();
                    @unlink($tmp);
                }
            } else {
                $cover_status = 'copy failed';
            }
            @unlink($local_path);
        } else {
            $cover_status = 'cover file not found';
        }
    }

    $results[] = [
        'story_id' => $story_id,
        'success' => true,
        'title' => get_the_title($story_id),
        'permalink' => get_permalink($story_id),
        'chapters_found' => count($chapter_posts),
        'chapters_updated' => count($updated_chapters),
        'cover_status' => $cover_status,
        'cover_url' => get_the_post_thumbnail_url($story_id, 'full'),
    ];
}

if (class_exists('LiteSpeed\Purge')) {
    \LiteSpeed\Purge::purge_all();
}
wp_cache_flush();

echo json_encode(['success' => true, 'results' => $results], JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
?>