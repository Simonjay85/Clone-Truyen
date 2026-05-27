<?php
/**
 * fix_simple_issues.php
 * Sửa các lỗi đơn giản: tiêu đề, excerpt, unpublish V1 cũ
 * Secret token: ZEN_TRUYEN_2026_BYPASS
 */

ini_set('display_errors', 0);
ini_set('max_execution_time', 120);
header('Content-Type: application/json');

if ($_SERVER['REQUEST_METHOD'] === 'GET') {
    http_response_code(405);
    echo json_encode(['error' => 'POST only']);
    exit;
}

$raw_input = file_get_contents('php://input');
$input = json_decode($raw_input, true);

if (!isset($input['secret_token']) || $input['secret_token'] !== 'ZEN_TRUYEN_2026_BYPASS') {
    http_response_code(401);
    echo json_encode(['error' => 'Unauthorized']);
    exit;
}

require_once('wp-load.php');

$results = [];

// ─── 1. ID 2561: Sửa lỗi đánh máy "Thương Láii" → "Thương Lái" ───────────
$post = get_post(2561);
if ($post && $post->post_type === 'truyen') {
    $new_title = str_replace('Thương Láii', 'Thương Lái', $post->post_title);
    if ($new_title !== $post->post_title) {
        wp_update_post(['ID' => 2561, 'post_title' => $new_title]);
        $results[] = ['id' => 2561, 'action' => 'fix_title', 'status' => 'ok', 'new_title' => $new_title];
    } else {
        $results[] = ['id' => 2561, 'action' => 'fix_title', 'status' => 'no_change', 'note' => 'Không tìm thấy chuỗi cần sửa'];
    }
} else {
    $results[] = ['id' => 2561, 'action' => 'fix_title', 'status' => 'not_found'];
}

// ─── 2. ID 3873: Sửa tiêu đề ALL CAPS → Title Case ──────────────────────────
$post = get_post(3873);
if ($post && $post->post_type === 'truyen') {
    $current = $post->post_title;
    $fixed = 'Thần Y Bị Đuổi, Vợ Cũ Hối Hận Muộn Màng';
    if (strtoupper($current) === strtoupper($fixed) && $current !== $fixed) {
        wp_update_post(['ID' => 3873, 'post_title' => $fixed]);
        $results[] = ['id' => 3873, 'action' => 'fix_caps', 'status' => 'ok', 'old' => $current, 'new' => $fixed];
    } else {
        $results[] = ['id' => 3873, 'action' => 'fix_caps', 'status' => 'no_change', 'current' => $current];
    }
} else {
    $results[] = ['id' => 3873, 'action' => 'fix_caps', 'status' => 'not_found'];
}

// ─── 3. ID 3849: Xóa ký tự lạ "n " trong excerpt ────────────────────────────
$post = get_post(3849);
if ($post && $post->post_type === 'truyen') {
    $exc = $post->post_excerpt;
    // Xóa "n\n" hoặc "\nn " hoặc "n " lọt vào giữa văn bản
    $fixed_exc = preg_replace('/\bn\s+(?=[A-ZÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚĂĐĨŨƠÀÁÂÃÈÉÊẾÌÍÒÓÔÕÙÚĂĐĨŨƠ])/u', '', $exc);
    $fixed_exc = trim($fixed_exc);
    if ($fixed_exc !== $exc) {
        wp_update_post(['ID' => 3849, 'post_excerpt' => $fixed_exc]);
        $results[] = ['id' => 3849, 'action' => 'fix_excerpt', 'status' => 'ok', 'fixed' => substr($fixed_exc, 0, 100)];
    } else {
        // Thử cách thô hơn: tìm pattern cụ thể "!" + newline + "n " + text
        $fixed_exc2 = preg_replace('/!\"\s*\n?\s*n\s+/', '!" ', $exc);
        if ($fixed_exc2 !== $exc) {
            wp_update_post(['ID' => 3849, 'post_excerpt' => trim($fixed_exc2)]);
            $results[] = ['id' => 3849, 'action' => 'fix_excerpt', 'status' => 'ok_v2', 'fixed' => substr(trim($fixed_exc2), 0, 100)];
        } else {
            $results[] = ['id' => 3849, 'action' => 'fix_excerpt', 'status' => 'no_change', 'excerpt_preview' => substr($exc, 0, 200)];
        }
    }
} else {
    $results[] = ['id' => 3849, 'action' => 'fix_excerpt', 'status' => 'not_found'];
}

// ─── 4. ID 2668: Sửa "Hà Ngoại" → "Hà Nội" trong tiêu đề ───────────────────
$post = get_post(2668);
if ($post && $post->post_type === 'truyen') {
    $new_title = str_replace('Hà Ngoại', 'Hà Nội', $post->post_title);
    $new_exc   = str_replace('Hà Ngoại', 'Hà Nội', $post->post_excerpt);
    $changed = false;
    if ($new_title !== $post->post_title || $new_exc !== $post->post_excerpt) {
        wp_update_post(['ID' => 2668, 'post_title' => $new_title, 'post_excerpt' => $new_exc]);
        $changed = true;
    }
    $results[] = ['id' => 2668, 'action' => 'fix_ha_ngoai', 'status' => $changed ? 'ok' : 'no_change', 'new_title' => $new_title];
} else {
    $results[] = ['id' => 2668, 'action' => 'fix_ha_ngoai', 'status' => 'not_found'];
}

// ─── 5. Unpublish V1 cũ (set draft) ─────────────────────────────────────────
// Các truyện V1 cũ có phiên bản V13 mới tốt hơn đang sống song song
$v1_ids = [2137, 2145, 2156, 2165, 2457];
foreach ($v1_ids as $vid) {
    $post = get_post($vid);
    if ($post && $post->post_type === 'truyen') {
        if ($post->post_status === 'publish') {
            wp_update_post(['ID' => $vid, 'post_status' => 'draft']);
            $results[] = ['id' => $vid, 'action' => 'unpublish_v1', 'status' => 'ok', 'title' => $post->post_title];
        } else {
            $results[] = ['id' => $vid, 'action' => 'unpublish_v1', 'status' => 'already_draft', 'current_status' => $post->post_status];
        }
    } else {
        $results[] = ['id' => $vid, 'action' => 'unpublish_v1', 'status' => 'not_found'];
    }
}

// ─── 6. Clear cache ─────────────────────────────────────────────────────────
if (function_exists('litespeed_purge_all')) {
    litespeed_purge_all();
}

echo json_encode([
    'success' => true,
    'total'   => count($results),
    'results' => $results
], JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
?>
