<?php
/**
 * Temporary DTT image conversion utility. Upload to web root, run in batches, delete immediately.
 */
require_once __DIR__ . '/wp-load.php';
header('Content-Type: application/json; charset=utf-8');

$token = (string) ($_GET['token'] ?? '');
$expected_token = 'e065b80c2f00c939ba64f8819a1f1ef083867288090f6fc7f8338fed84490349';
if (!hash_equals($expected_token, $token)) {
    status_header(403);
    echo wp_json_encode(array('ok' => false, 'error' => 'Forbidden'));
    exit;
}

function dtt_collect_convertible_images($root) {
    $files = array();
    if (!is_dir($root)) {
        return $files;
    }
    $iterator = new RecursiveIteratorIterator(
        new RecursiveDirectoryIterator($root, FilesystemIterator::SKIP_DOTS)
    );
    foreach ($iterator as $file) {
        if (!$file->isFile()) {
            continue;
        }
        $ext = strtolower($file->getExtension());
        if (in_array($ext, array('jpg', 'jpeg', 'png'), true)) {
            $files[] = $file->getPathname();
        }
    }
    sort($files, SORT_STRING);
    return $files;
}

$uploads = wp_upload_dir();
$files = dtt_collect_convertible_images($uploads['basedir']);
$offset = max(0, (int) ($_GET['offset'] ?? 0));
$limit = max(1, min(20, (int) ($_GET['limit'] ?? 10)));
$dry_run = (($_GET['action'] ?? 'scan') !== 'apply');
$batch = array_slice($files, $offset, $limit);
$results = array();

foreach ($batch as $source) {
    $destination = preg_replace('/\.(jpe?g|png)$/i', '.webp', $source);
    $row = array(
        'source' => str_replace($uploads['basedir'], '', $source),
        'destination' => str_replace($uploads['basedir'], '', $destination),
        'status' => 'would_convert',
    );

    if (file_exists($destination) && filesize($destination) > 0) {
        $row['status'] = 'exists';
        $results[] = $row;
        continue;
    }
    if ($dry_run) {
        $results[] = $row;
        continue;
    }

    $editor = wp_get_image_editor($source);
    if (is_wp_error($editor)) {
        $row['status'] = 'editor_error';
        $row['error'] = $editor->get_error_message();
        $results[] = $row;
        continue;
    }

    $editor->set_quality(82);
    $saved = $editor->save($destination, 'image/webp');
    if (is_wp_error($saved)) {
        $row['status'] = 'save_error';
        $row['error'] = $saved->get_error_message();
    } else {
        $row['status'] = 'converted';
        $row['bytes'] = filesize($destination);
    }
    $results[] = $row;
}

echo wp_json_encode(array(
    'ok' => true,
    'action' => $dry_run ? 'scan' : 'apply',
    'total_files' => count($files),
    'offset' => $offset,
    'limit' => $limit,
    'next_offset' => $offset + count($batch),
    'has_more' => ($offset + count($batch)) < count($files),
    'results' => $results,
), JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
