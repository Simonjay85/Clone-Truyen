<?php
/**
 * fix_eng_all98.php
 * Bulk replace English words across all 98 evaluated novels (skip ID 1933 draft).
 * Safe replacements: file, email, laptop, penthouse, blockchain, SHA-256/SHA256,
 *                    hash, VPS, badge, PGP, commit (selective)
 * SKIP: CA (ambiguous with Công An)
 */
ini_set('display_errors', 0);
ini_set('max_execution_time', 300);
header('Content-Type: application/json');
$input = json_decode(file_get_contents('php://input'), true);
if (!isset($input['secret_token']) || $input['secret_token'] !== 'ZEN_TRUYEN_2026_BYPASS') {
    http_response_code(401); echo json_encode(['error'=>'Unauthorized']); exit;
}
require_once('wp-load.php');
global $wpdb;

$novel_ids = [
    2465, 2067, 2089, 2738, 2106, 2112, 2703, 3633, 2099, 2724, 2815, 2120,
    3724, 3813, 2013, 2717, 3755, 3769, 3861, 2035, 2752, 3767, 3801, 3837,
    2731, 3789, 4097, 3825, 3940, 2313, 2759, 3743, 3849, 2766, 2787, 3954,
    2696, 2794, 3998, 2475, 2606, 2745, 3873, 3930, 4036, 2482, 2289, 2259,
    2023, 1927, 2773, 3920, 2689, 4084, 2573, 2497, 2238, 2197, 2145, 2001,
    1921, 2780, 2801, 2549, 2448, 2052, 2044, 2658, 2561, 2517, 2279, 2269,
    2190, 2165, 2129, 2007, 4060, 2457, 2249, 4072, 2587, 2508, 2156, 1948,
    2808, 2489, 2137, 1968, 2682, 2675, 2207, 1984, 2227, 2668, 2217,
    2487, 2020,
    // 1933 excluded — draft novel
];

// Ordered by specificity: longer/more specific patterns first
$patterns = [
    '/\bSHA-256\b/u'            => 'mã băm SHA-256',
    '/\bSHA256\b/u'             => 'mã băm SHA-256',
    '/\bblockchain\b/iu'        => 'chuỗi khối',
    '/\bpenthouse\b/iu'         => 'căn hộ tầng thượng',
    '/\blaptop\b/iu'            => 'máy tính xách tay',
    '/\bVPS\b/u'                => 'máy chủ ảo VPS',
    '/\bPGP\b/u'                => 'mã hóa PGP',
    '/\bbadge\b/iu'             => 'thẻ ra vào',
    '/\b(hash|Hash)\b/u'        => 'mã băm',
    '/\bemail\b/iu'             => 'thư điện tử',
    '/\b(file|File)\b/u'        => 'tập tin',
];

$summary = [];
$total_chapters_changed = 0;
$total_chapters_scanned = 0;

foreach ($novel_ids as $nid) {
    $chapters = $wpdb->get_results($wpdb->prepare(
        "SELECT p.ID, p.post_title, p.post_content FROM {$wpdb->posts} p
         INNER JOIN {$wpdb->postmeta} pm ON p.ID = pm.post_id
         WHERE p.post_type = 'chuong' AND p.post_status != 'trash'
         AND pm.meta_key = '_truyen_id' AND pm.meta_value = %s
         ORDER BY p.post_date ASC",
        (string)$nid
    ));
    if (empty($chapters)) continue;

    $total_chapters_scanned += count($chapters);
    $changed = 0;

    foreach ($chapters as $ch) {
        $new_c = $ch->post_content;
        $new_t = $ch->post_title;

        foreach ($patterns as $pat => $rep) {
            $new_c = preg_replace($pat, $rep, $new_c);
            $new_t = preg_replace($pat, $rep, $new_t);
        }

        if ($new_c !== $ch->post_content || $new_t !== $ch->post_title) {
            $update = ['ID' => $ch->ID, 'post_content' => wp_kses_post($new_c)];
            if ($new_t !== $ch->post_title) $update['post_title'] = $new_t;
            wp_update_post($update);
            if (function_exists('litespeed_purge_post')) litespeed_purge_post($ch->ID);
            $changed++;
        }
    }

    if ($changed > 0) {
        $summary[] = ['novel_id' => $nid, 'changed' => $changed, 'total' => count($chapters)];
        $total_chapters_changed += $changed;
    }
}

if (function_exists('litespeed_purge_all')) litespeed_purge_all();

echo json_encode([
    'status'                  => 'done',
    'novels_with_changes'     => count($summary),
    'total_chapters_changed'  => $total_chapters_changed,
    'total_chapters_scanned'  => $total_chapters_scanned,
    'detail'                  => $summary,
], JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
?>
