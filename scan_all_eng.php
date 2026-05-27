<?php
/**
 * scan_all_eng.php — Scan ALL novels for remaining English words
 * Returns novel_id => [chapter count with matches, sample]
 */
ini_set('display_errors', 0);
ini_set('max_execution_time', 120);
header('Content-Type: application/json');
$input = json_decode(file_get_contents('php://input'), true);
if (!isset($input['secret_token']) || $input['secret_token'] !== 'ZEN_TRUYEN_2026_BYPASS') { http_response_code(401); exit; }
require_once('wp-load.php');
global $wpdb;

// Patterns to detect (word-boundary English in Vietnamese text)
// We look for clearly-English words that don't belong
$eng_words = [
    'file', 'email', 'laptop', 'contract', 'penthouse', 'blockchain',
    'commit', 'hash', 'badge', 'VPS', 'server', 'software', 'startup',
    'CEO', 'CFO', 'COO', 'blockchain', 'bitcoin', 'token',
    'pitch', 'deal', 'meeting', 'project', 'report', 'update',
    'download', 'upload', 'data', 'online', 'offline', 'app',
    'website', 'chat', 'call', 'check', 'note', 'booking',
];

// SQL pattern combining all words
$like_clauses = [];
foreach ($eng_words as $w) {
    $like_clauses[] = $wpdb->prepare("p.post_content LIKE %s", '%' . $w . '%');
}
$like_sql = implode(' OR ', $like_clauses);

// Get all distinct novel IDs that have chapters matching any pattern
$rows = $wpdb->get_results(
    "SELECT DISTINCT pm.meta_value as novel_id, COUNT(p.ID) as ch_count
     FROM {$wpdb->posts} p
     INNER JOIN {$wpdb->postmeta} pm ON p.ID = pm.post_id
     WHERE p.post_type = 'chuong' AND p.post_status != 'trash'
     AND pm.meta_key = '_truyen_id'
     AND ({$like_sql})
     GROUP BY pm.meta_value
     ORDER BY CAST(pm.meta_value AS UNSIGNED) ASC"
);

$result = [];
foreach ($rows as $row) {
    $result[$row->novel_id] = intval($row->ch_count);
}
echo json_encode(['count' => count($result), 'novels' => $result], JSON_UNESCAPED_UNICODE);
?>
