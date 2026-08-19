<?php
/**
 * DTT TOC migration utility.
 *
 * Temporary, token-protected endpoint intended to run once from the site root.
 * Upload, run dry-run, run apply in batches, then delete this file immediately.
 */

if (!defined('DTT_TOC_MIGRATION')) {
    define('DTT_TOC_MIGRATION', true);
}

require_once __DIR__ . '/wp-load.php';

header('Content-Type: application/json; charset=utf-8');

$token = (string) ($_GET['token'] ?? '');
$expected_token = '68420e20cb887e2a59a18c340ddc2d9700965a07a38dedfc76ff1085661838c7';

if ($expected_token === '' || !hash_equals($expected_token, $token)) {
    status_header(403);
    echo wp_json_encode(array('ok' => false, 'error' => 'Forbidden'));
    exit;
}

if ($_SERVER['REQUEST_METHOD'] !== 'POST' && !isset($_GET['action'])) {
    status_header(405);
    echo wp_json_encode(array('ok' => false, 'error' => 'Use POST or provide an action.'));
    exit;
}

function dtt_toc_slug($text, $used_ids) {
    $id = sanitize_title(wp_strip_all_tags($text));
    if ($id === '') {
        $id = 'section';
    }
    $base = $id;
    $suffix = 2;
    while (in_array($id, $used_ids, true)) {
        $id = $base . '-' . $suffix;
        $suffix++;
    }
    return $id;
}

function dtt_toc_escape_title($html) {
    return trim(wp_strip_all_tags(html_entity_decode($html, ENT_QUOTES | ENT_HTML5, get_bloginfo('charset') ?: 'UTF-8')));
}

function dtt_toc_render_nodes($nodes) {
    if (empty($nodes)) {
        return '';
    }

    $html = '<ol>';
    foreach ($nodes as $node) {
        $item = $node['item'];
        $li_class = !empty($node['children']) ? ' class="dtt-toc-parent dtt-toc-collapsed"' : '';
        $html .= '<li' . $li_class . '><a href="#' . esc_attr($item['id']) . '">' . esc_html($item['title']) . '</a>';
        if (!empty($node['children'])) {
            $html .= dtt_toc_render_nodes($node['children']);
        }
        $html .= '</li>';
    }
    return $html . '</ol>';
}

function dtt_toc_build_tree($items) {
    $tree = array();
    $stack = array();
    $levels = array();

    foreach ($items as $item) {
        while (!empty($levels) && end($levels) >= $item['level']) {
            array_pop($levels);
            array_pop($stack);
        }

        if (empty($stack)) {
            $parent =& $tree;
        } else {
            $parent =& $stack[count($stack) - 1];
        }

        $parent[] = array('item' => $item, 'children' => array());
        $last_index = count($parent) - 1;
        $stack[] =& $parent[$last_index]['children'];
        $levels[] = $item['level'];
        unset($parent);
    }

    return $tree;
}

function dtt_toc_remove_existing_nav($content) {
    return preg_replace(
        '~<nav\\b[^>]*aria-label\\s*=\\s*(["\\\'])[^"\\\']*Mục lục[^"\\\']*\\1[^>]*>.*?</nav>\\s*~isu',
        '',
        $content
    );
}

function dtt_toc_transform_content($content) {
    $content = dtt_toc_remove_existing_nav($content);
    $items = array();
    $used_ids = array();

    $pattern = '~<h([2-4])\\b([^>]*)>(.*?)</h\\1>~isu';
    $transformed = preg_replace_callback($pattern, function ($match) use (&$items, &$used_ids) {
        $level = (int) $match[1];
        $attrs = $match[2];
        $inner = $match[3];
        $title = dtt_toc_escape_title($inner);

        if ($title === '') {
            return $match[0];
        }

        $id = dtt_toc_slug($title, $used_ids);
        $used_ids[] = $id;
        $attrs = preg_replace('~\\s+id\\s*=\\s*(["\\\']).*?\\1~isu', '', $attrs);
        $attrs = rtrim($attrs) . ' id="' . esc_attr($id) . '"';
        $items[] = array('level' => $level, 'id' => $id, 'title' => $title);

        return '<h' . $level . $attrs . '>' . $inner . '</h' . $level . '>';
    }, $content);

    if (!is_string($transformed) || count($items) < 2) {
        return array('content' => $content, 'items' => $items, 'changed' => false);
    }

    $tree = dtt_toc_build_tree($items);
    $toc = '<nav class="dtt-auto-toc" aria-label="Mục lục bài viết" data-toc-version="1">';
    $toc .= '<div class="dtt-auto-toc__head"><h2>Mục lục bài viết</h2><span class="dtt-auto-toc__hint">Chọn mục để đọc nhanh</span></div>';
    $toc .= dtt_toc_render_nodes($tree);
    $toc .= '</nav>';

    $first_heading = false;
    $summary_match = array();
    if (preg_match('~<div\\b[^>]*class\\s*=\\s*(["\\\'])[^"\\\']*\\bkiem-lai-summary\\b[^"\\\']*\\1[^>]*>.*?</div>~isu', $transformed, $summary_match, PREG_OFFSET_CAPTURE)) {
        $first_heading = $summary_match[0][1] + strlen($summary_match[0][0]);
    } elseif (preg_match('~<h[2-4]\\b[^>]*>~i', $transformed, $first_match, PREG_OFFSET_CAPTURE)) {
        $first_heading = $first_match[0][1];
    }

    if ($first_heading === false) {
        return array('content' => $content, 'items' => $items, 'changed' => false);
    }

    $final_content = substr($transformed, 0, $first_heading) . $toc . substr($transformed, $first_heading);
    return array('content' => $final_content, 'items' => $items, 'changed' => true);
}

function dtt_toc_backup_dir() {
    $uploads = wp_upload_dir();
    $dir = trailingslashit($uploads['basedir']) . 'dtt-toc-backups';
    if (!wp_mkdir_p($dir)) {
        return new WP_Error('backup_dir_failed', 'Unable to create backup directory.');
    }
    return $dir;
}

function dtt_toc_backup_post($post) {
    $dir = dtt_toc_backup_dir();
    if (is_wp_error($dir)) {
        return $dir;
    }

    $file = trailingslashit($dir) . 'post-' . (int) $post->ID . '-' . gmdate('Ymd-His') . '.json';
    $payload = array(
        'id' => (int) $post->ID,
        'post_type' => $post->post_type,
        'post_status' => $post->post_status,
        'post_title' => $post->post_title,
        'post_content' => $post->post_content,
        'saved_at_utc' => gmdate('c'),
    );

    if (false === file_put_contents($file, wp_json_encode($payload, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT))) {
        return new WP_Error('backup_write_failed', 'Unable to write backup file.');
    }
    return $file;
}

function dtt_toc_process_posts($args) {
    $query = new WP_Query(array(
        'post_type' => 'post',
        'post_status' => 'publish',
        'posts_per_page' => max(1, min(100, (int) ($args['limit'] ?? 20))),
        'offset' => max(0, (int) ($args['offset'] ?? 0)),
        'orderby' => 'ID',
        'order' => 'ASC',
        'no_found_rows' => false,
        'fields' => 'all',
    ));

    $results = array();
    $dry_run = !empty($args['dry_run']);

    foreach ($query->posts as $post) {
        $transformed = dtt_toc_transform_content($post->post_content);
        $row = array(
            'id' => (int) $post->ID,
            'slug' => $post->post_name,
            'title' => $post->post_title,
            'headings' => count($transformed['items']),
            'changed' => (bool) $transformed['changed'],
            'dry_run' => $dry_run,
        );

        if (!$transformed['changed']) {
            $row['status'] = 'skipped';
            $results[] = $row;
            continue;
        }

        if ($dry_run) {
            $row['status'] = 'would_update';
            $results[] = $row;
            continue;
        }

        $backup = dtt_toc_backup_post($post);
        if (is_wp_error($backup)) {
            $row['status'] = 'backup_failed';
            $row['error'] = $backup->get_error_message();
            $results[] = $row;
            continue;
        }

        $updated = wp_update_post(wp_slash(array(
            'ID' => $post->ID,
            'post_content' => $transformed['content'],
        )), true);

        if (is_wp_error($updated)) {
            $row['status'] = 'update_failed';
            $row['error'] = $updated->get_error_message();
        } else {
            $row['status'] = 'updated';
            $row['backup'] = $backup;
        }
        $results[] = $row;
    }

    return array(
        'total_found' => (int) $query->found_posts,
        'offset' => (int) ($args['offset'] ?? 0),
        'limit' => (int) ($args['limit'] ?? 20),
        'results' => $results,
    );
}

$action = sanitize_key($_GET['action'] ?? $_POST['action'] ?? 'dry-run');
$limit = max(1, min(100, (int) ($_GET['limit'] ?? $_POST['limit'] ?? 20)));
$offset = max(0, (int) ($_GET['offset'] ?? $_POST['offset'] ?? 0));

if ($action === 'dry-run') {
    $result = dtt_toc_process_posts(array('limit' => $limit, 'offset' => $offset, 'dry_run' => true));
} elseif ($action === 'apply') {
    $result = dtt_toc_process_posts(array('limit' => $limit, 'offset' => $offset, 'dry_run' => false));
} else {
    status_header(400);
    echo wp_json_encode(array('ok' => false, 'error' => 'Unknown action. Use dry-run or apply.'));
    exit;
}

$result['ok'] = true;
$result['action'] = $action;
$result['backup_note'] = 'Backups are stored under wp-content/uploads/dtt-toc-backups/. Delete this endpoint after migration.';
echo wp_json_encode($result, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
