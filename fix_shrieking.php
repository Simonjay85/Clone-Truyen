<?php
/**
 * fix_shrieking.php - Sửa từ tiếng Anh "shrieking" lẫn trong chương 8 của truyện Vua Yến Sào
 */
ini_set('display_errors', 0);
ini_set('max_execution_time', 60);
header('Content-Type: application/json');

$input = json_decode(file_get_contents('php://input'), true);
if (!isset($input['secret_token']) || $input['secret_token'] !== 'ZEN_TRUYEN_2026_BYPASS') {
    http_response_code(401); echo json_encode(['error'=>'Unauthorized']); exit;
}
require_once('wp-load.php');

$post_id = 4045;
$post = get_post($post_id);
if (!$post) {
    echo json_encode(['error' => 'Post not found: ' . $post_id]); exit;
}

$content = $post->post_content;
$original_len = strlen($content);

// Thay thế các biến thể có thể có của "shrieking" lẫn trong tiếng Việt
$replacements = [
    ', shrieking lớn tiếng'  => ', la hét lớn tiếng',
    ',shrieking lớn tiếng'   => ', la hét lớn tiếng',
    ' shrieking lớn tiếng'   => ' la hét lớn tiếng',
    'shrieking lớn tiếng'    => 'la hét lớn tiếng',
    ', shrieking,'            => ', la hét,',
    ' shrieking '             => ' la hét ',
    ' shrieking'              => ' la hét',
    'shrieking'               => 'la hét',
];

$fixed = $content;
$changed_count = 0;
foreach ($replacements as $needle => $replace) {
    if (stripos($fixed, $needle) !== false) {
        $new = str_ireplace($needle, $replace, $fixed);
        if ($new !== $fixed) {
            $changed_count++;
            $fixed = $new;
        }
    }
}

$new_len = strlen($fixed);
$changed = ($fixed !== $content);

if ($changed) {
    wp_update_post(['ID' => $post_id, 'post_content' => wp_kses_post($fixed)]);
    if (function_exists('litespeed_purge_post')) litespeed_purge_post($post_id);
    elseif (function_exists('litespeed_purge_all')) litespeed_purge_all();
}

echo json_encode([
    'id'           => $post_id,
    'changed'      => $changed,
    'replacements' => $changed_count,
    'original_len' => $original_len,
    'new_len'      => $new_len,
], JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
?>
