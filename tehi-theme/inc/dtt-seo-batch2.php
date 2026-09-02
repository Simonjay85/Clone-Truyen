<?php
/**
 * DTT SEO Batch 2 – SERP & Image Authority.
 *
 * Runtime responsibilities only:
 * - use Rank Math SEO-title postmeta as the document title for Wiki posts;
 * - generate a unique 1200x630 OG card on demand for Wiki posts without a thumbnail;
 * - feed the unique fallback card to Facebook/Twitter Open Graph and Article JSON-LD;
 * - never mutate post slugs/content at request time.
 */

if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

function dtt_seo_b2_clusters() {
    return array(
        160 => array('slug' => 'kiem-lai', 'label' => 'Kiếm Lai', 'rgb' => array(34, 65, 122), 'accent' => array(105, 166, 255)),
        177 => array('slug' => 'gia-thien', 'label' => 'Già Thiên', 'rgb' => array(74, 43, 28), 'accent' => array(232, 179, 93)),
        175 => array('slug' => 'quy-bi-chi-chu', 'label' => 'Quỷ Bí Chi Chủ', 'rgb' => array(45, 36, 70), 'accent' => array(174, 140, 255)),
        165 => array('slug' => 'pham-nhan-tu-tien', 'label' => 'Phàm Nhân Tu Tiên', 'rgb' => array(27, 67, 57), 'accent' => array(108, 211, 173)),
        174 => array('slug' => 'pham-nhan-tu-tien-bo-tro', 'label' => 'Phàm Nhân Tu Tiên', 'rgb' => array(27, 67, 57), 'accent' => array(108, 211, 173)),
        164 => array('slug' => 'tien-nghich', 'label' => 'Tiên Nghịch', 'rgb' => array(66, 30, 43), 'accent' => array(238, 117, 143)),
        179 => array('slug' => 'hoan-my-the-gioi', 'label' => 'Hoàn Mỹ Thế Giới', 'rgb' => array(38, 63, 55), 'accent' => array(217, 182, 94)),
        180 => array('slug' => 'thanh-khu', 'label' => 'Thánh Khư', 'rgb' => array(36, 48, 66), 'accent' => array(130, 194, 255)),
    );
}

function dtt_seo_b2_cluster_for_post($post_id) {
    $post_id = absint($post_id);
    if (!$post_id || 'post' !== get_post_type($post_id)) {
        return array();
    }

    foreach (dtt_seo_b2_clusters() as $category_id => $cluster) {
        if (has_category($category_id, $post_id)) {
            $cluster['category_id'] = $category_id;
            return $cluster;
        }
    }

    return array();
}

function dtt_seo_b2_is_wiki_post($post_id = 0) {
    $post_id = $post_id ?: get_queried_object_id();
    return !empty(dtt_seo_b2_cluster_for_post($post_id));
}

function dtt_seo_b2_post_title_meta($post_id) {
    $title = (string) get_post_meta($post_id, 'rank_math_title', true);
    if ('' === $title) {
        $title = (string) get_post_meta($post_id, '_rank_math_title', true);
    }
    return trim(wp_strip_all_tags(html_entity_decode($title, ENT_QUOTES | ENT_HTML5, 'UTF-8')));
}

/**
 * The theme historically forced `single_post_title() - DTT`, bypassing Rank Math title postmeta.
 * For Wiki posts, use the reviewed Rank Math title exactly; H1 and slug remain untouched.
 */
function dtt_seo_b2_document_title($title) {
    if (!is_singular('post')) {
        return $title;
    }

    $post_id = get_queried_object_id();
    if (!dtt_seo_b2_is_wiki_post($post_id)) {
        return $title;
    }

    $seo_title = dtt_seo_b2_post_title_meta($post_id);
    return $seo_title ?: $title;
}
add_filter('pre_get_document_title', 'dtt_seo_b2_document_title', 500);
add_filter('rank_math/frontend/title', 'dtt_seo_b2_document_title', 500);

function dtt_seo_b2_og_signature($post_id) {
    $post = get_post($post_id);
    if (!$post) {
        return '0';
    }
    $cluster = dtt_seo_b2_cluster_for_post($post_id);
    return substr(md5($post->post_title . '|' . $post->post_modified_gmt . '|' . ($cluster['slug'] ?? 'wiki') . '|v2'), 0, 12);
}

function dtt_seo_b2_og_url($post_id) {
    $post_id = absint($post_id);
    if (!$post_id || !dtt_seo_b2_is_wiki_post($post_id)) {
        return '';
    }
    return add_query_arg(
        array(
            'dtt_og' => $post_id,
            'sig'    => dtt_seo_b2_og_signature($post_id),
        ),
        home_url('/')
    );
}

function dtt_seo_b2_font_path($bold = false) {
    $candidates = $bold
        ? array(
            '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',
            '/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf',
        )
        : array(
            '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
            '/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf',
        );

    foreach ($candidates as $font) {
        if (is_readable($font)) {
            return $font;
        }
    }
    return '';
}

function dtt_seo_b2_text_width($text, $font, $size) {
    if (!$font || !function_exists('imagettfbbox')) {
        return strlen($text) * max(8, (int) ($size * 0.55));
    }
    $box = imagettfbbox($size, 0, $font, $text);
    return is_array($box) ? abs($box[2] - $box[0]) : 0;
}

function dtt_seo_b2_wrap_title($text, $font, $size, $max_width, $max_lines = 4) {
    $words = preg_split('/\s+/u', trim($text));
    $lines = array();
    $line = '';

    foreach ($words as $word) {
        $candidate = '' === $line ? $word : $line . ' ' . $word;
        if (dtt_seo_b2_text_width($candidate, $font, $size) <= $max_width) {
            $line = $candidate;
            continue;
        }

        if ('' !== $line) {
            $lines[] = $line;
        }
        $line = $word;

        if (count($lines) >= $max_lines) {
            break;
        }
    }

    if (count($lines) < $max_lines && '' !== $line) {
        $lines[] = $line;
    }

    if (count($lines) > $max_lines) {
        $lines = array_slice($lines, 0, $max_lines);
    }

    if (count($lines) === $max_lines) {
        $joined = implode(' ', $lines);
        if (mb_strlen($joined, 'UTF-8') < mb_strlen(trim($text), 'UTF-8')) {
            $last = rtrim($lines[$max_lines - 1], '.,;:!?—–- ');
            while (dtt_seo_b2_text_width($last . '…', $font, $size) > $max_width && mb_strlen($last, 'UTF-8') > 8) {
                $last = mb_substr($last, 0, -1, 'UTF-8');
            }
            $lines[$max_lines - 1] = rtrim($last) . '…';
        }
    }

    return $lines;
}

function dtt_seo_b2_render_og_card($post_id, $target_file) {
    if (!function_exists('imagecreatetruecolor')) {
        return false;
    }

    $post = get_post($post_id);
    $cluster = dtt_seo_b2_cluster_for_post($post_id);
    if (!$post || empty($cluster)) {
        return false;
    }

    $width = 1200;
    $height = 630;
    $image = imagecreatetruecolor($width, $height);
    if (!$image) {
        return false;
    }

    list($r, $g, $b) = $cluster['rgb'];
    list($ar, $ag, $ab) = $cluster['accent'];
    $background = imagecolorallocate($image, $r, $g, $b);
    $accent = imagecolorallocate($image, $ar, $ag, $ab);
    $white = imagecolorallocate($image, 248, 249, 252);
    $muted = imagecolorallocate($image, 214, 220, 230);
    $deep = imagecolorallocate($image, max(0, $r - 16), max(0, $g - 16), max(0, $b - 16));

    imagefilledrectangle($image, 0, 0, $width, $height, $background);
    imagefilledrectangle($image, 0, 0, 26, $height, $accent);
    imagefilledrectangle($image, 26, 500, $width, $height, $deep);
    imagefilledellipse($image, 1080, 70, 300, 300, $deep);
    imagefilledellipse($image, 1115, 100, 180, 180, $accent);

    $font_bold = dtt_seo_b2_font_path(true);
    $font_regular = dtt_seo_b2_font_path(false);

    if ($font_bold && function_exists('imagettftext')) {
        imagettftext($image, 24, 0, 76, 80, $accent, $font_bold, 'DTT  •  WIKI');
        imagettftext($image, 28, 0, 76, 130, $muted, $font_bold, $cluster['label']);

        $title_size = 46;
        $lines = dtt_seo_b2_wrap_title(wp_strip_all_tags($post->post_title), $font_bold, $title_size, 980, 4);
        $y = 205;
        foreach ($lines as $line) {
            imagettftext($image, $title_size, 0, 76, $y, $white, $font_bold, $line);
            $y += 64;
        }

        imagettftext($image, 22, 0, 76, 562, $muted, $font_regular ?: $font_bold, 'doctieuthuyet.com  •  Wiki & giải thích chuyên sâu');
    } else {
        imagestring($image, 5, 76, 60, 'DTT WIKI - ' . $cluster['label'], $white);
        imagestring($image, 5, 76, 150, wp_strip_all_tags($post->post_title), $white);
        imagestring($image, 4, 76, 550, 'doctieuthuyet.com', $muted);
    }

    $dir = dirname($target_file);
    if (!is_dir($dir)) {
        wp_mkdir_p($dir);
    }

    $ok = imagejpeg($image, $target_file, 88);
    imagedestroy($image);
    return (bool) $ok;
}

/** Serve/cache a unique OG image only for published Wiki posts. */
function dtt_seo_b2_serve_og_image() {
    if (empty($_GET['dtt_og'])) {
        return;
    }

    $post_id = absint($_GET['dtt_og']);
    $post = get_post($post_id);
    if (!$post || 'post' !== $post->post_type || 'publish' !== $post->post_status || !dtt_seo_b2_is_wiki_post($post_id)) {
        status_header(404);
        exit;
    }

    $expected_sig = dtt_seo_b2_og_signature($post_id);
    $requested_sig = isset($_GET['sig']) ? sanitize_key(wp_unslash($_GET['sig'])) : '';
    if ($requested_sig && !hash_equals($expected_sig, $requested_sig)) {
        wp_safe_redirect(dtt_seo_b2_og_url($post_id), 301);
        exit;
    }

    $uploads = wp_upload_dir();
    if (!empty($uploads['error'])) {
        status_header(500);
        exit;
    }

    $dir = trailingslashit($uploads['basedir']) . 'dtt-og-cache';
    $file = trailingslashit($dir) . $post_id . '-' . $expected_sig . '.jpg';

    if (!is_readable($file) && !dtt_seo_b2_render_og_card($post_id, $file)) {
        status_header(500);
        exit;
    }

    nocache_headers();
    header('Content-Type: image/jpeg');
    header('Content-Length: ' . filesize($file));
    header('Cache-Control: public, max-age=31536000, immutable');
    header('X-Robots-Tag: noindex, nofollow', true);
    readfile($file);
    exit;
}
add_action('template_redirect', 'dtt_seo_b2_serve_og_image', -1000);

/** Use the unique card only when a Wiki post has no real featured image. */
function dtt_seo_b2_rank_math_og_image($url) {
    // The PNTT support archive is intentionally indexable as a distinct discovery page.
    // Reuse the canonical PNTT hub card so the archive is not left without social imagery.
    if (is_category(174)) {
        return dtt_seo_b2_og_url(10412) ?: $url;
    }
    if (!is_singular('post')) {
        return $url;
    }
    $post_id = get_queried_object_id();
    if (!$post_id || has_post_thumbnail($post_id) || !dtt_seo_b2_is_wiki_post($post_id)) {
        return $url;
    }
    return dtt_seo_b2_og_url($post_id) ?: $url;
}
add_filter('rank_math/opengraph/facebook/image', 'dtt_seo_b2_rank_math_og_image', 100);
add_filter('rank_math/opengraph/twitter/image', 'dtt_seo_b2_rank_math_og_image', 100);

function dtt_seo_b2_schema_image_fallback($data, $jsonld = null) {
    if (!is_singular('post')) {
        return $data;
    }

    $post_id = get_queried_object_id();
    if (!$post_id || has_post_thumbnail($post_id) || !dtt_seo_b2_is_wiki_post($post_id)) {
        return $data;
    }

    $image = dtt_seo_b2_og_url($post_id);
    if (!$image) {
        return $data;
    }

    $patch = static function (&$node) use ($image) {
        if (!is_array($node)) {
            return;
        }
        $type = $node['@type'] ?? '';
        $types = is_array($type) ? $type : array($type);
        if (array_intersect(array('Article', 'BlogPosting', 'NewsArticle'), $types)) {
            $node['image'] = array($image);
            $node['thumbnailUrl'] = $image;
        }
    };

    foreach ($data as &$node) {
        $patch($node);
        if (is_array($node) && isset($node['@graph']) && is_array($node['@graph'])) {
            foreach ($node['@graph'] as &$graph_node) {
                $patch($graph_node);
            }
            unset($graph_node);
        }
    }
    unset($node);

    return $data;
}
add_filter('rank_math/json_ld', 'dtt_seo_b2_schema_image_fallback', 150, 2);
