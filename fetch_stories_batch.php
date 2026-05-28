<?php
ini_set('display_errors', 0);
ini_set('max_execution_time', 120);
header('Content-Type: application/json');
$input = json_decode(file_get_contents('php://input'), true);
if (!isset($input['secret_token']) || $input['secret_token'] !== 'ZEN_TRUYEN_2026_BYPASS') { http_response_code(401); exit; }
require_once('wp-load.php');

$novel_ids = $input['novel_ids'] ?? [];
$result = [];

foreach ($novel_ids as $nid) {
    $story = get_post(intval($nid));
    if (!$story) continue;

    $chapters = get_posts([
        'post_type' => 'chuong',
        'posts_per_page' => -1,
        'orderby' => 'menu_order',
        'order' => 'ASC',
        'meta_query' => [['key'=>'_truyen_id','value'=>(string)$nid,'compare'=>'=']]
    ]);

    $chs = [];
    foreach ($chapters as $ch) {
        $chs[] = [
            'wp_id'   => $ch->ID,
            'title'   => $ch->post_title,
            'content' => $ch->post_content,
        ];
    }

    $result[] = [
        'novel_id' => intval($nid),
        'title' => $story->post_title,
        'intro' => $story->post_content,
        'total' => count($chapters),
        'chapters' => $chs
    ];
}
echo json_encode($result, JSON_UNESCAPED_UNICODE);
?>
