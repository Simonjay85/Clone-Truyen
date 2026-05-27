<?php
/**
 * audit_98novels.php
 * Scan all 98 evaluated novels for:
 * 1) Remaining specific English words flagged in evaluation
 * 2) Short last-chapter (< 3500 bytes = likely incomplete)
 */
ini_set('display_errors', 0);
ini_set('max_execution_time', 180);
header('Content-Type: application/json');
$input = json_decode(file_get_contents('php://input'), true);
if (!isset($input['secret_token']) || $input['secret_token'] !== 'ZEN_TRUYEN_2026_BYPASS') { http_response_code(401); exit; }
require_once('wp-load.php');
global $wpdb;

// All 98 evaluated novel IDs
$novel_ids = [
    2465, 2067, 2089, 2738, 2106, 2112, 2703, 3633, 2099, 2724, 2815, 2120,
    3724, 3813, 2013, 2717, 3755, 3769, 3861, 2035, 2752, 3767, 3801, 3837,
    2731, 3789, 4097, 3825, 3940, 2313, 2759, 3743, 3849, 2766, 2787, 3954,
    2696, 2794, 3998, 2475, 2606, 2745, 3873, 3930, 4036, 2482, 2289, 2259,
    2023, 1927, 2773, 3920, 2689, 4084, 2573, 2497, 2238, 2197, 2145, 2001,
    1921, 2780, 2801, 2549, 2448, 2052, 2044, 2658, 2561, 2517, 2279, 2269,
    2190, 2165, 2129, 2007, 4060, 2457, 2249, 4072, 2587, 2508, 2156, 1948,
    2808, 2489, 2137, 1968, 2682, 2675, 2207, 1984, 2227, 2668, 2217, 1933,
    2487, 2020,
];

// English patterns to detect — only clearly-wrong ones (not common loanwords)
$eng_patterns = [
    '/\b(file|File)\b/u'           => ['label'=>'file', 'fix'=>'tập tin'],
    '/\bemail\b/iu'                => ['label'=>'email', 'fix'=>'thư điện tử'],
    '/\blaptop\b/iu'               => ['label'=>'laptop', 'fix'=>'máy tính xách tay'],
    '/\bpenthouse\b/iu'            => ['label'=>'penthouse', 'fix'=>'căn hộ tầng thượng'],
    '/\bblockchain\b/iu'           => ['label'=>'blockchain', 'fix'=>'chuỗi khối'],
    '/\bSHA-256\b/u'               => ['label'=>'SHA-256', 'fix'=>'mã băm SHA-256'],
    '/\bSHA256\b/u'                => ['label'=>'SHA256', 'fix'=>'mã băm SHA-256'],
    '/\b(hash|Hash)\b/u'           => ['label'=>'hash', 'fix'=>'mã băm'],
    '/\bVPS\b/u'                   => ['label'=>'VPS', 'fix'=>'máy chủ ảo VPS'],
    '/\bbadge\b/iu'                => ['label'=>'badge', 'fix'=>'thẻ ra vào'],
    '/\bcommit\b/iu'               => ['label'=>'commit', 'fix'=>'xác nhận giao dịch'],
    '/\bPGP\b/u'                   => ['label'=>'PGP', 'fix'=>'mã hóa PGP'],
    '/\bpenthouse\b/iu'            => ['label'=>'penthouse', 'fix'=>'căn hộ tầng thượng'],
    '/\b(CA)\b(?!\s*-|\s*\d)/u'   => ['label'=>'CA (cert)', 'fix'=>'chứng chỉ số CA'],
];

$eng_findings  = [];  // novel_id => [ pattern_label => ch_count ]
$short_ch8     = [];  // novel_id => ['wp_id'=>.., 'title'=>.., 'len'=>..]

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

    // Check English words
    foreach ($eng_patterns as $pat => $info) {
        $cnt = 0;
        foreach ($chapters as $ch) {
            if (preg_match($pat, $ch->post_content)) $cnt++;
        }
        if ($cnt > 0) {
            if (!isset($eng_findings[$nid])) $eng_findings[$nid] = [];
            $eng_findings[$nid][$info['label']] = $cnt;
        }
    }

    // Check last chapter length
    $last = end($chapters);
    $len  = strlen($last->post_content);
    if ($len < 3500) {
        $short_ch8[$nid] = ['wp_id'=>$last->ID, 'title'=>$last->post_title, 'len'=>$len];
    }
}

echo json_encode([
    'eng_findings' => $eng_findings,
    'short_ch8'    => $short_ch8,
], JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
?>
