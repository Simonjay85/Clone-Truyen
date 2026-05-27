<?php
ini_set('display_errors', 0);
ini_set('max_execution_time', 60);
header('Content-Type: application/json');
$input = json_decode(file_get_contents('php://input'), true);
if (!isset($input['secret_token']) || $input['secret_token'] !== 'ZEN_TRUYEN_2026_BYPASS') { http_response_code(401); exit; }
require_once('wp-load.php');

$novel_ids = $input['novel_ids'] ?? [];
$result = [];

foreach ($novel_ids as $nid) {
    $chapters = get_posts([
        'post_type' => 'chuong', 'posts_per_page' => -1, 'orderby' => 'date', 'order' => 'ASC',
        'meta_query' => [['key'=>'_truyen_id','value'=>(string)$nid,'compare'=>'=']]
    ]);
    $chs = [];
    foreach ($chapters as $ch) {
        $chs[] = [
            'wp_id'   => $ch->ID,
            'title'   => $ch->post_title,
            'excerpt' => substr(strip_tags($ch->post_content), 0, 500),
        ];
    }
    $result[] = ['novel_id'=>$nid, 'total'=>count($chapters), 'chapters'=>$chs];
}
echo json_encode($result, JSON_UNESCAPED_UNICODE|JSON_PRETTY_PRINT);
?>
