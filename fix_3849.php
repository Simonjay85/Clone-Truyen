<?php
ini_set('display_errors', 0);
header('Content-Type: application/json');
$input = json_decode(file_get_contents('php://input'), true);
if (!isset($input['secret_token']) || $input['secret_token'] !== 'ZEN_TRUYEN_2026_BYPASS') {
    http_response_code(401); echo json_encode(['error'=>'Unauthorized']); exit;
}
require_once('wp-load.php');

$p = get_post(3849);
if (!$p) { echo json_encode(['error' => 'not found']); exit; }

$content = $p->post_content;
// Pattern cụ thể: </p>n<p> — chữ n lọt vào giữa 2 thẻ HTML
$fixed = str_replace("</p>n<p>", "</p>\n<p>", $content);
// Cũng xử lý </p>\nn<p>
$fixed = preg_replace('#</p>\s*n\s*<p>#', "</p>\n<p>", $fixed);

$changed = ($fixed !== $content);
if ($changed) {
    wp_update_post(['ID' => 3849, 'post_content' => $fixed]);
    if (function_exists('litespeed_purge_all')) litespeed_purge_all();
}

echo json_encode([
    'id' => 3849,
    'changed' => $changed,
    'before' => mb_substr($content, 0, 300),
    'after'  => $changed ? mb_substr($fixed, 0, 300) : 'no change',
], JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
?>
