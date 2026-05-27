<?php
ini_set('display_errors', 0);
ini_set('max_execution_time', 30);
header('Content-Type: application/json');
$input = json_decode(file_get_contents('php://input'), true);
if (!isset($input['secret_token']) || $input['secret_token'] !== 'ZEN_TRUYEN_2026_BYPASS') { http_response_code(401); exit; }
require_once('wp-load.php');
global $wpdb;

$result = [];
foreach ([2448, 2259] as $nid) {
    $chapters = $wpdb->get_results($wpdb->prepare(
        "SELECT p.ID, p.post_title, p.post_content FROM {$wpdb->posts} p
         INNER JOIN {$wpdb->postmeta} pm ON p.ID = pm.post_id
         WHERE p.post_type = 'chuong' AND p.post_status != 'trash'
         AND pm.meta_key = '_truyen_id' AND pm.meta_value = %s
         ORDER BY p.post_date ASC LIMIT 3",
        (string)$nid
    ));
    foreach ($chapters as $ch) {
        $text = strip_tags($ch->post_content);
        // Find lines with English words
        $lines = explode("\n", $text);
        $matches = [];
        foreach ($lines as $line) {
            if (preg_match('/\b(file|email|laptop|blockchain|cloud|hash)\b/i', $line)) {
                $matches[] = trim(substr($line, 0, 200));
            }
        }
        if (!empty($matches)) {
            $result[] = ['nid'=>$nid,'wp_id'=>$ch->ID,'title'=>$ch->post_title,'matches'=>array_slice($matches, 0, 5)];
        }
    }
}
echo json_encode($result, JSON_UNESCAPED_UNICODE|JSON_PRETTY_PRINT);
?>
