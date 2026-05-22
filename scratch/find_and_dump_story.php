<?php
require_once('./wp-load.php');
header('Content-Type: application/json; charset=utf-8');

$slug = 'nghe-nhan-tra-sen-bi-khinh-re-truc-xuat-lat-keo-dem-hoi-tra-quoc-te-dua-ke-phan-boi-vao-tu';

$args = [
    'name'        => $slug,
    'post_type'   => 'truyen',
    'post_status' => 'any',
    'numberposts' => 1
];
$posts = get_posts($args);

if (empty($posts)) {
    echo json_encode([
        'success' => false,
        'message' => 'Không tìm thấy truyện với slug: ' . $slug
    ], JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
    exit;
}

$story = $posts[0];
$story_id = $story->ID;

// Get categories
$terms = wp_get_post_terms($story_id, 'the_loai');
$genres = [];
foreach ($terms as $t) {
    $genres[] = $t->name;
}

// Get Featured Image Alt
$thumb_id = get_post_thumbnail_id($story_id);
$alt_text = '';
if ($thumb_id) {
    $alt_text = get_post_meta($thumb_id, '_wp_attachment_image_alt', true);
}

// Get RankMath SEO Metadata
$rm_title = get_post_meta($story_id, '_rank_math_title', true);
$rm_desc = get_post_meta($story_id, '_rank_math_description', true);
$rm_keyword = get_post_meta($story_id, '_rank_math_focus_keyword', true);

// Get Comments
$comments_query = get_comments(['post_id' => $story_id, 'status' => 'approve']);
$comments = [];
foreach ($comments_query as $c) {
    $comments[] = [
        'author' => $c->comment_author,
        'content' => $c->comment_content,
        'date' => $c->comment_date
    ];
}

// Get Chapters
$chapters_posts = get_posts([
    'post_type'      => 'chuong',
    'posts_per_page' => -1,
    'meta_key'       => '_truyen_id',
    'meta_value'     => $story_id,
    'orderby'        => 'ID',
    'order'          => 'ASC'
]);

$chapters = [];
foreach ($chapters_posts as $c) {
    $chapters[] = [
        'id' => $c->ID,
        'title' => $c->post_title,
        'slug' => $c->post_name,
        'content' => $c->post_content,
        'word_count' => mb_strlen(strip_tags($c->post_content), 'UTF-8')
    ];
}

echo json_encode([
    'success' => true,
    'story' => [
        'id' => $story_id,
        'title' => $story->post_title,
        'slug' => $story->post_name,
        'content' => $story->post_content,
        'genres' => $genres,
        'image_alt' => $alt_text,
        'rank_math' => [
            'title' => $rm_title,
            'description' => $rm_desc,
            'keyword' => $rm_keyword
        ],
        'comments' => $comments
    ],
    'chapters_count' => count($chapters),
    'chapters' => $chapters
], JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
?>
