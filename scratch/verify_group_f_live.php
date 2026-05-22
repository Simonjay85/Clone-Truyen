<?php
require_once('wp-load.php');
header('Content-Type: application/json');

$secret = isset($_GET['secret']) ? $_GET['secret'] : '';
if ($secret !== 'ZEN_TRUYEN_2026_BYPASS') {
    http_response_code(401);
    echo json_encode(['error' => 'Unauthorized']);
    exit;
}

$ids = [2013, 2007, 2001];
$out = [];
foreach ($ids as $id) {
    $chapters = get_posts([
        'post_type'      => 'chuong',
        'posts_per_page' => -1,
        'orderby'        => 'menu_order',
        'order'          => 'ASC',
        'meta_query'     => [
            [
                'key'     => '_truyen_id',
                'value'   => $id,
                'compare' => '=',
            ],
        ],
    ]);
    $out[] = [
        'id' => $id,
        'title' => get_the_title($id),
        'chapter_count' => count($chapters),
        'thumbnail' => get_the_post_thumbnail_url($id, 'full'),
        'first_chapter' => !empty($chapters) ? $chapters[0]->post_title : '',
        'last_chapter' => !empty($chapters) ? $chapters[count($chapters) - 1]->post_title : '',
    ];
}

echo json_encode(['success' => true, 'stories' => $out], JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES | JSON_PRETTY_PRINT);
?>
