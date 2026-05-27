<?php
/**
 * fetch_short_ch8.php
 * Fetch last chapter content + previous chapter tail for context.
 * Novel IDs with short last chapters that need expansion.
 */
ini_set('display_errors', 0);
ini_set('max_execution_time', 60);
header('Content-Type: application/json');
$input = json_decode(file_get_contents('php://input'), true);
if (!isset($input['secret_token']) || $input['secret_token'] !== 'ZEN_TRUYEN_2026_BYPASS') { http_response_code(401); exit; }
require_once('wp-load.php');
global $wpdb;

$novel_ids = [2089, 2738, 2106, 2703, 2099, 2724, 2717, 2731, 3743, 2787, 2482, 3920, 2448, 2052, 2561, 2249, 2587, 2808, 2207];

$out = [];
foreach ($novel_ids as $nid) {
    $chs = $wpdb->get_results($wpdb->prepare(
        "SELECT p.ID, p.post_title, p.post_content FROM {$wpdb->posts} p
         INNER JOIN {$wpdb->postmeta} pm ON p.ID = pm.post_id
         WHERE p.post_type = 'chuong' AND p.post_status != 'trash'
         AND pm.meta_key = '_truyen_id' AND pm.meta_value = %s
         ORDER BY p.post_date ASC",
        (string)$nid
    ));
    $total = count($chs);
    if ($total === 0) continue;
    $last = $chs[$total-1];
    $prev = $total >= 2 ? $chs[$total-2] : null;
    $out[$nid] = [
        'total_chapters' => $total,
        'prev_ch' => $prev ? [
            'wp_id'  => $prev->ID,
            'title'  => $prev->post_title,
            'tail'   => strip_tags(mb_substr($prev->post_content, -600)),
        ] : null,
        'last_ch' => [
            'wp_id'   => $last->ID,
            'title'   => $last->post_title,
            'len'     => strlen($last->post_content),
            'content' => strip_tags($last->post_content),
        ],
    ];
}
echo json_encode($out, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
?>
