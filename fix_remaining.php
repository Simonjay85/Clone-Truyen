<?php
ini_set('display_errors', 0);
header('Content-Type: application/json');
$input = json_decode(file_get_contents('php://input'), true);
if (!isset($input['secret_token']) || $input['secret_token'] !== 'ZEN_TRUYEN_2026_BYPASS') {
    http_response_code(401); echo json_encode(['error'=>'Unauthorized']); exit;
}
require_once('wp-load.php');
$results = [];

// ── ID 3873: Force title case ─────────────────────────────────────────────
$p = get_post(3873);
if ($p && $p->post_type === 'truyen') {
    wp_update_post(['ID' => 3873, 'post_title' => 'Thần Y Bị Đuổi, Vợ Cũ Hối Hận Muộn Màng']);
    $results[] = ['id' => 3873, 'action' => 'fix_title_case', 'status' => 'ok'];
} else {
    $results[] = ['id' => 3873, 'action' => 'fix_title_case', 'status' => 'not_found'];
}

// ── ID 3849: Remove stray "n " from excerpt ───────────────────────────────
$p = get_post(3849);
if ($p && $p->post_type === 'truyen') {
    $exc = $p->post_excerpt;
    // Pattern: dấu ngoặc kép đóng + " n " + chữ hoa → xóa " n "
    $fixed = preg_replace('/(\x{201D}|\&#8221;|!&quot;|!")\s+n\s+/u', '$1 ', $exc);
    if ($fixed !== $exc) {
        wp_update_post(['ID' => 3849, 'post_excerpt' => $fixed]);
        $results[] = ['id' => 3849, 'action' => 'fix_excerpt_n', 'status' => 'ok', 'fixed_preview' => mb_substr(strip_tags($fixed), 0, 150)];
    } else {
        // Fallback: xóa thẳng chuỗi cụ thể
        $exc_raw = get_post_field('post_excerpt', 3849, 'raw');
        $fixed2 = str_replace(['!" n ', '!" n ', '!&quot; n '], ['!" ', '!" ', '!&quot; '], $exc_raw);
        // Cũng thử với raw HTML entity
        $fixed2 = preg_replace('/!\&#8221;\s+n\s+/', '!&#8221; ', $fixed2);
        if ($fixed2 !== $exc_raw) {
            wp_update_post(['ID' => 3849, 'post_excerpt' => $fixed2]);
            $results[] = ['id' => 3849, 'action' => 'fix_excerpt_n', 'status' => 'ok_raw', 'fixed_preview' => mb_substr(strip_tags($fixed2), 0, 150)];
        } else {
            $results[] = ['id' => 3849, 'action' => 'fix_excerpt_n', 'status' => 'no_match', 'raw_preview' => mb_substr($exc_raw, 0, 200)];
        }
    }
} else {
    $results[] = ['id' => 3849, 'action' => 'fix_excerpt_n', 'status' => 'not_found'];
}

if (function_exists('litespeed_purge_all')) litespeed_purge_all();
echo json_encode(['success' => true, 'results' => $results], JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
?>
