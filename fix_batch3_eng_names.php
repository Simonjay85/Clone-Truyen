<?php
/**
 * fix_batch3_eng_names.php
 * 1) ID 2517: English words (SHA-256, blockchain, Series B, CA, commit)
 * 2) ID 2489: English words (penthouse, CA, file)
 * 3) ID 2313: English words (VPS, SHA-256, hash, badge)
 * 4) ID 2689: "Thanh Tâm International Hospital" → "Bệnh viện Thanh Tâm"
 * 5) ID 1968: Rename "Lê Vân" → "Trần Minh Hạnh" (conflict with ID 1927 same name)
 * 6) ID 2023: Rename "Lâm Phong" → "Đinh Trọng Phong" (conflict with ID 2035 same protagonist name)
 * 7) ID 2780: "GreenFlora" (Anh lẫn Việt) → "Tập đoàn Hoa Tươi Việt"
 * 8) ID 2794: "Vạn Hoa urban complex" → "khu đô thị Vạn Hoa"
 */
ini_set('display_errors', 0);
ini_set('max_execution_time', 120);
header('Content-Type: application/json');

$input = json_decode(file_get_contents('php://input'), true);
if (!isset($input['secret_token']) || $input['secret_token'] !== 'ZEN_TRUYEN_2026_BYPASS') {
    http_response_code(401); echo json_encode(['error'=>'Unauthorized']); exit;
}
require_once('wp-load.php');
$results = [];

function fix_novel_chapters($novel_id, $replacements, &$results, $task) {
    global $wpdb;
    $chapters = $wpdb->get_results($wpdb->prepare(
        "SELECT p.ID, p.post_title, p.post_content FROM {$wpdb->posts} p
         INNER JOIN {$wpdb->postmeta} pm ON p.ID = pm.post_id
         WHERE p.post_type = 'chuong' AND p.post_status != 'trash'
         AND pm.meta_key = '_truyen_id' AND pm.meta_value = %s
         ORDER BY p.post_date ASC",
        (string)$novel_id
    ));
    $changed = 0;
    foreach ($chapters as $ch) {
        $new_c = $ch->post_content;
        $new_t = $ch->post_title;
        foreach ($replacements as $o => $n) {
            $new_c = str_replace($o, $n, $new_c);
            $new_t = str_replace($o, $n, $new_t);
        }
        if ($new_c !== $ch->post_content || $new_t !== $ch->post_title) {
            $update = ['ID'=>$ch->ID,'post_content'=>wp_kses_post($new_c)];
            if ($new_t !== $ch->post_title) $update['post_title'] = $new_t;
            wp_update_post($update);
            if (function_exists('litespeed_purge_post')) litespeed_purge_post($ch->ID);
            $changed++;
        }
    }
    $results[] = ['task'=>$task,'novel_id'=>$novel_id,'chapters_changed'=>$changed,'total'=>count($chapters)];
}

function fix_novel_chapters_regex($novel_id, $patterns, &$results, $task) {
    global $wpdb;
    $chapters = $wpdb->get_results($wpdb->prepare(
        "SELECT p.ID, p.post_title, p.post_content FROM {$wpdb->posts} p
         INNER JOIN {$wpdb->postmeta} pm ON p.ID = pm.post_id
         WHERE p.post_type = 'chuong' AND p.post_status != 'trash'
         AND pm.meta_key = '_truyen_id' AND pm.meta_value = %s
         ORDER BY p.post_date ASC",
        (string)$novel_id
    ));
    $changed = 0;
    foreach ($chapters as $ch) {
        $new_c = $ch->post_content;
        $new_t = $ch->post_title;
        foreach ($patterns as $pattern => $replacement) {
            $new_c = preg_replace($pattern, $replacement, $new_c);
            $new_t = preg_replace($pattern, $replacement, $new_t);
        }
        if ($new_c !== $ch->post_content || $new_t !== $ch->post_title) {
            $update = ['ID'=>$ch->ID,'post_content'=>wp_kses_post($new_c)];
            if ($new_t !== $ch->post_title) $update['post_title'] = $new_t;
            wp_update_post($update);
            if (function_exists('litespeed_purge_post')) litespeed_purge_post($ch->ID);
            $changed++;
        }
    }
    $results[] = ['task'=>$task,'novel_id'=>$novel_id,'chapters_changed'=>$changed,'total'=>count($chapters)];
}

// ==================== TASK 1: ID 2517 — Fintech English words ====================
fix_novel_chapters_regex(2517, [
    '/\bSHA-256\b/u'            => 'mã băm SHA-256',
    '/\bBlockchain\b/u'         => 'Chuỗi khối',
    '/\bblockchain\b/u'         => 'chuỗi khối',
    '/\bSeries B\b/u'           => 'vòng gọi vốn Series B',
    '/\b\bCA\b(?!\s+[A-Z]{2})/u' => 'chứng chỉ số CA',
    '/\bcommit\b/iu'            => 'xác nhận giao dịch',
    '/\bSHA256\b/u'             => 'mã băm SHA-256',
    '/\b(file|File)\b/u'        => 'tập tin',
    '/\bemail\b/iu'             => 'thư điện tử',
], $results, 'fix_eng_2517');

// ==================== TASK 2: ID 2489 — Fake-poor heir English words ====================
fix_novel_chapters_regex(2489, [
    '/\bpenthouse\b/iu'         => 'căn hộ tầng thượng',
    '/\bPenthouse\b/u'          => 'Căn hộ tầng thượng',
    '/\b(CA)\b/u'               => 'chứng chỉ số CA',
    '/\b(file|File)\b/u'        => 'tập tin',
    '/\bTechcombank\b/u'        => 'Techcombank',  // keep as bank name
], $results, 'fix_eng_2489');

// ==================== TASK 3: ID 2313 — Source code theft English words ====================
fix_novel_chapters_regex(2313, [
    '/\bVPS\b/u'                => 'máy chủ ảo VPS',
    '/\bSHA-256\b/u'            => 'mã băm SHA-256',
    '/\bSHA256\b/u'             => 'mã băm SHA-256',
    '/\b(hash|Hash)\b/u'        => 'mã băm',
    '/\bbadge\b/iu'             => 'thẻ ra vào',
    '/\b(file|File)\b/u'        => 'tập tin',
], $results, 'fix_eng_2313');

// ==================== TASK 4: ID 2689 — Hospital English name ====================
fix_novel_chapters(2689, [
    'Thanh Tâm International Hospital'  => 'Bệnh viện Thanh Tâm',
    'thanh tâm international hospital'  => 'bệnh viện Thanh Tâm',
    'BV Thanh Tâm International'        => 'Bệnh viện Thanh Tâm',
], $results, 'fix_hosp_name_2689');

// ==================== TASK 5: ID 1968 — Rename "Lê Vân" (conflict with ID 1927) ====================
fix_novel_chapters(1968, [
    'Lê Vân'        => 'Trần Minh Hạnh',
    'Vân '          => 'Hạnh ',   // context: she's referred to as just Vân/Hạnh
    ' Vân,'         => ' Hạnh,',
    ' Vân.'         => ' Hạnh.',
    '"Vân'          => '"Hạnh',
    'Vân!'          => 'Hạnh!',
    'Vân?'          => 'Hạnh?',
    'của Vân'       => 'của Hạnh',
    'với Vân'       => 'với Hạnh',
    'đến Vân'       => 'đến Hạnh',
    'theo Vân'      => 'theo Hạnh',
    'bảo Vân'       => 'bảo Hạnh',
    'gọi Vân'       => 'gọi Hạnh',
    'Vân đã'        => 'Hạnh đã',
    'Vân không'     => 'Hạnh không',
    'Vân là'        => 'Hạnh là',
    'Vân nhìn'      => 'Hạnh nhìn',
    'Vân nói'       => 'Hạnh nói',
    'Vân quay'      => 'Hạnh quay',
    'Vân chạy'      => 'Hạnh chạy',
    'chị Vân'       => 'chị Hạnh',
    'cô Vân'        => 'cô Hạnh',
], $results, 'rename_levan_1968');

// ==================== TASK 6: ID 2023 — Rename "Lâm Phong" (conflict with ID 2035) ====================
fix_novel_chapters(2023, [
    'Lâm Phong'     => 'Đinh Trọng Phong',
    'anh Phong'     => 'anh Phong',      // keep short form
    'chàng Phong'   => 'chàng Phong',    // keep short form (no conflict)
    'ông Phong'     => 'ông Phong',      // keep
], $results, 'rename_lamphong_2023');

// ==================== TASK 7: ID 2780 — Replace English org name ====================
fix_novel_chapters(2780, [
    'GreenFlora'    => 'Tập đoàn Hoa Tươi Việt',
    'Tập đoàn GreenFlora' => 'Tập đoàn Hoa Tươi Việt',
    'công ty GreenFlora'  => 'công ty Hoa Tươi Việt',
], $results, 'fix_greenflora_2780');

// ==================== TASK 8: ID 2794 — Replace English project name ====================
fix_novel_chapters(2794, [
    'Vạn Hoa urban complex'     => 'khu đô thị Vạn Hoa',
    'Vạn Hoa Urban Complex'     => 'Khu đô thị Vạn Hoa',
    'vạn hoa urban complex'     => 'khu đô thị vạn hoa',
], $results, 'fix_urban_2794');

if (function_exists('litespeed_purge_all')) litespeed_purge_all();
echo json_encode(['results'=>$results], JSON_UNESCAPED_UNICODE|JSON_PRETTY_PRINT);
?>
