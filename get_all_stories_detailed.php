<?php
/**
 * get_all_stories_detailed.php
 * Fetches all stories (truyen) from doctieuthuyet.com with complete metadata for Excel export.
 */
ini_set('display_errors', 0);
ini_set('max_execution_time', 300);
header('Content-Type: application/json; charset=utf-8');

$input = json_decode(file_get_contents('php://input'), true);
$token = isset($input['secret_token']) ? $input['secret_token'] : (isset($_GET['token']) ? $_GET['token'] : '');
if ($token !== 'ZEN_TRUYEN_2026_BYPASS') {
    http_response_code(401);
    echo json_encode(['error' => 'Unauthorized']);
    exit;
}

require_once('wp-load.php');
global $wpdb;

// Query all posts of type 'truyen'
$stories = get_posts([
    'post_type' => 'truyen',
    'posts_per_page' => -1,
    'post_status' => 'any',
    'orderby' => 'date',
    'order' => 'DESC'
]);

$list = [];
foreach ($stories as $s) {
    $id = $s->ID;
    
    // Get author
    $author = get_post_meta($id, 'truyen_tacgia', true);
    if (empty($author)) {
        $author = 'Đang cập nhật';
    }
    
    // Get views
    $views = get_post_meta($id, '_views', true);
    $views = ($views !== '') ? intval($views) : 0;
    
    // Get genres (the_loai taxonomy)
    $terms = wp_get_post_terms($id, 'the_loai');
    $genres = [];
    if (!is_wp_error($terms) && !empty($terms)) {
        foreach ($terms as $t) {
            $genres[] = $t->name;
        }
    }
    $genre_str = implode(', ', $genres);
    
    // Get chapter count
    $chapter_count = $wpdb->get_var($wpdb->prepare(
        "SELECT COUNT(*) FROM {$wpdb->posts} p
         INNER JOIN {$wpdb->postmeta} pm ON p.ID = pm.post_id
         WHERE p.post_type = 'chuong' 
           AND p.post_status = 'publish' 
           AND pm.meta_key = '_truyen_id' 
           AND pm.meta_value = %s",
        (string)$id
    ));
    $chapter_count = intval($chapter_count);
    
    // Get cover image URL
    $cover_url = '';
    if (has_post_thumbnail($id)) {
        $cover_url = get_the_post_thumbnail_url($id, 'full');
    }
    
    // Intro snippet
    $intro_snippet = wp_strip_all_tags($s->post_content);
    $intro_snippet = preg_replace('/\s+/', ' ', $intro_snippet);
    $intro_snippet = mb_substr($intro_snippet, 0, 300, 'UTF-8') . (mb_strlen($intro_snippet, 'UTF-8') > 300 ? '...' : '');

    $list[] = [
        'id' => $id,
        'title' => $s->post_title,
        'slug' => $s->post_name,
        'url' => home_url('/truyen/' . $s->post_name . '/'),
        'author' => $author,
        'genre' => $genre_str,
        'chapters' => $chapter_count,
        'views' => $views,
        'status' => $s->post_status,
        'date' => $s->post_date,
        'intro' => $intro_snippet,
        'cover' => $cover_url
    ];
}

echo json_encode($list, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
?>
