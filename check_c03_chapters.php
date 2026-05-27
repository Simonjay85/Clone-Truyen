<?php
ini_set('display_errors', 0);
ini_set('max_execution_time', 30);
header('Content-Type: application/json');
$input = json_decode(file_get_contents('php://input'), true);
if (!isset($input['secret_token']) || $input['secret_token'] !== 'ZEN_TRUYEN_2026_BYPASS') { http_response_code(401); exit; }
require_once('wp-load.php');

$nid = intval($input['novel_id'] ?? 0);
$chapters = get_posts([
    'post_type' => 'chuong', 'posts_per_page' => -1, 'orderby' => 'date', 'order' => 'ASC',
    'meta_query' => [['key'=>'_truyen_id','value'=>(string)$nid,'compare'=>'=']]
]);

// Return ch7-last with excerpts
$result = ['novel_id'=>$nid,'total'=>count($chapters),'chapters'=>[]];
foreach (array_slice($chapters, max(0, count($chapters)-4)) as $ch) {
    $result['chapters'][] = [
        'wp_id' => $ch->ID,
        'title' => $ch->post_title,
        'c03'   => (stripos($ch->post_content, 'C03') !== false || stripos($ch->post_title, 'C03') !== false),
        'excerpt' => substr(strip_tags($ch->post_content), 0, 300),
    ];
}
echo json_encode($result, JSON_UNESCAPED_UNICODE|JSON_PRETTY_PRINT);
?>
