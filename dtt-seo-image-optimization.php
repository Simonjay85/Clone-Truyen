<?php
/**
 * Plugin Name: DTT SEO Schema and Image Optimization
 * Description: Enhances Article/BlogPosting structured data and image delivery site-wide.
 * Version: 1.0.0
 */

if (!defined('ABSPATH')) {
    exit;
}

/**
 * Return SEO-safe metadata for the current post without embedding the full article body.
 */
function dtt_article_schema_data($post_id = 0) {
    $post_id = $post_id ?: get_queried_object_id();
    if (!$post_id || get_post_type($post_id) !== 'post') {
        return array();
    }

    $url = get_permalink($post_id);
    $title = wp_strip_all_tags(get_the_title($post_id));
    $description = get_post_meta($post_id, '_yoast_wpseo_metadesc', true);
    if (!$description) {
        $description = get_post_meta($post_id, 'rank_math_description', true);
    }
    if (!$description) {
        $description = get_the_excerpt($post_id);
    }

    $categories = wp_get_post_categories($post_id, array('fields' => 'names'));
    $tags = wp_get_post_tags($post_id, array('fields' => 'names'));
    $image = get_the_post_thumbnail_url($post_id, 'full');

    $schema = array(
        '@type' => 'BlogPosting',
        'headline' => $title,
        'name' => $title,
        'description' => wp_strip_all_tags(wp_trim_words($description, 45, '…')),
        'datePublished' => get_post_time('c', true, $post_id),
        'dateModified' => get_post_modified_time('c', true, $post_id),
        'inLanguage' => get_bloginfo('language') ?: 'vi-VN',
        'mainEntityOfPage' => array('@type' => 'WebPage', '@id' => $url),
        'wordCount' => preg_match_all('/\\S+/u', wp_strip_all_tags(get_post_field('post_content', $post_id)), $word_matches),
        'articleSection' => array_values(array_filter(array_map('strval', $categories))),
        'keywords' => array_values(array_filter(array_map('strval', $tags))),
        'author' => array(
            '@type' => 'Person',
            'name' => wp_strip_all_tags(get_the_author_meta('display_name', get_post_field('post_author', $post_id))),
            'url' => get_author_posts_url(get_post_field('post_author', $post_id)),
        ),
        'publisher' => array(
            '@type' => 'Organization',
            'name' => get_bloginfo('name') ?: 'DTT',
            'url' => home_url('/'),
        ),
    );

    if ($image) {
        $schema['image'] = array($image);
        $schema['thumbnailUrl'] = $image;
    }

    return $schema;
}

function dtt_schema_enhance_node(&$node, $article) {
    if (!is_array($node)) {
        return false;
    }

    $type = $node['@type'] ?? '';
    $types = is_array($type) ? $type : array($type);
    $is_article = in_array('Article', $types, true) || in_array('BlogPosting', $types, true) || in_array('NewsArticle', $types, true);
    if (!$is_article) {
        return false;
    }

    foreach (array('headline', 'name', 'description', 'datePublished', 'dateModified', 'inLanguage', 'mainEntityOfPage', 'wordCount', 'articleSection', 'keywords', 'image', 'thumbnailUrl') as $key) {
        if (empty($node[$key]) && !empty($article[$key])) {
            $node[$key] = $article[$key];
        }
    }

    if (empty($node['author']) && !empty($article['author'])) {
        $node['author'] = $article['author'];
    }
    if (empty($node['publisher']) && !empty($article['publisher'])) {
        $node['publisher'] = $article['publisher'];
    }

    return true;
}

/**
 * Enhance Rank Math's existing BlogPosting node instead of adding duplicate JSON-LD.
 */
function dtt_enhance_rank_math_schema($data, $jsonld = null) {
    if (!is_singular('post')) {
        return $data;
    }

    $article = dtt_article_schema_data();
    if (empty($article)) {
        return $data;
    }

    $found = false;
    foreach ($data as &$node) {
        if (is_array($node)) {
            if (dtt_schema_enhance_node($node, $article)) {
                $found = true;
            }
            if (isset($node['@graph']) && is_array($node['@graph'])) {
                foreach ($node['@graph'] as &$graph_node) {
                    if (dtt_schema_enhance_node($graph_node, $article)) {
                        $found = true;
                    }
                }
                unset($graph_node);
            }
        }
    }
    unset($node);

    if (!$found) {
        $data['DTTArticle'] = $article;
    }

    return $data;
}
add_filter('rank_math/json_ld', 'dtt_enhance_rank_math_schema', 99, 2);

/**
 * Fallback schema for installations where Rank Math is not active.
 */
function dtt_output_fallback_article_schema() {
    if (!is_singular('post') || has_filter('rank_math/json_ld')) {
        return;
    }

    $article = dtt_article_schema_data();
    if (empty($article)) {
        return;
    }

    echo '<script type="application/ld+json">' . wp_json_encode($article, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES) . '</script>' . "\n";
}
add_action('wp_head', 'dtt_output_fallback_article_schema', 30);

/**
 * Add safe image defaults to every WordPress-generated attachment image.
 */
function dtt_image_attributes($attr, $attachment, $size) {
    if (is_admin()) {
        return $attr;
    }

    if (empty($attr['decoding'])) {
        $attr['decoding'] = 'async';
    }

    $featured_id = is_singular('post') ? get_post_thumbnail_id(get_queried_object_id()) : 0;
    if ($featured_id && (int) $attachment->ID === (int) $featured_id) {
        $attr['loading'] = 'eager';
        $attr['fetchpriority'] = 'high';
    } elseif (empty($attr['loading'])) {
        $attr['loading'] = 'lazy';
    }

    return $attr;
}
add_filter('wp_get_attachment_image_attributes', 'dtt_image_attributes', 20, 3);

/**
 * Ensure raw content images receive loading/decoding attributes when WordPress filters them.
 */
function dtt_content_image_attributes($html, $context, $attachment_id) {
    if (is_admin() || stripos($html, '<img') === false) {
        return $html;
    }

    if (!preg_match('/\\bloading\\s*=\\s*["\\\']/i', $html)) {
        $html = preg_replace('/<img\\b/i', '<img loading="lazy"', $html, 1);
    }
    if (!preg_match('/\\bdecoding\\s*=\\s*["\\\']/i', $html)) {
        $html = preg_replace('/<img\\b/i', '<img decoding="async"', $html, 1);
    }
    return $html;
}
add_filter('wp_content_img_tag', 'dtt_content_image_attributes', 20, 3);

/**
 * Prefer WebP for generated image sub-sizes when the active editor supports it.
 * Existing theme filters continue to serve a matching WebP file when available.
 */
function dtt_prefer_webp_output_format($formats, $mime_type) {
    if (function_exists('imagewebp') && in_array($mime_type, array('image/jpeg', 'image/png'), true)) {
        $formats[$mime_type] = 'image/webp';
    }
    return $formats;
}
add_filter('image_editor_output_format', 'dtt_prefer_webp_output_format', 10, 2);

/**
 * Rewrite custom-template thumbnail URLs to WebP when the generated file exists.
 */
function dtt_serve_webp_image_src($image, $attachment_id, $size, $icon) {
    if (is_admin() || empty($image) || !is_array($image) || empty($image[0])) {
        return $image;
    }
    $url = $image[0];
    $clean_url = preg_replace('/[?#].*$/', '', $url);
    $path = str_replace(content_url(), WP_CONTENT_DIR, $clean_url);
    $webp_path = preg_replace('/\\.(png|jpe?g)$/i', '.webp', $path);
    if (file_exists($webp_path)) {
        $image[0] = preg_replace('/\\.(png|jpe?g)$/i', '.webp', $url);
    }
    return $image;
}
add_filter('wp_get_attachment_image_src', 'dtt_serve_webp_image_src', 10, 4);

function dtt_serve_webp_post_thumbnail_url($url, $post_id, $size) {
    if (is_admin() || empty($url)) {
        return $url;
    }
    $clean_url = preg_replace('/[?#].*$/', '', $url);
    $path = str_replace(content_url(), WP_CONTENT_DIR, $clean_url);
    $webp_path = preg_replace('/\\.(png|jpe?g)$/i', '.webp', $path);
    if (file_exists($webp_path)) {
        return preg_replace('/\\.(png|jpe?g)$/i', '.webp', $url);
    }
    return $url;
}
add_filter('post_thumbnail_url', 'dtt_serve_webp_post_thumbnail_url', 10, 3);

/**
 * Add dimensions to custom image tags that already expose an attachment ID.
 */
function dtt_custom_image_lazy_defaults($html) {
    if (is_admin() || stripos($html, '<img') === false) {
        return $html;
    }
    $html = preg_replace('/<img(?![^>]*\\bloading=)/i', '<img loading="lazy"', $html);
    $html = preg_replace('/<img(?![^>]*\\bdecoding=)/i', '<img decoding="async"', $html);
    return $html;
}
add_filter('the_content', 'dtt_custom_image_lazy_defaults', 20);

function dtt_rewrite_webp_url($url) {
    if (!$url || !preg_match('/\\.(png|jpe?g)(?:[?#].*)?$/i', $url)) {
        return $url;
    }
    $clean_url = preg_replace('/[?#].*$/', '', $url);
    $path = str_replace(content_url(), WP_CONTENT_DIR, $clean_url);
    $webp_path = preg_replace('/\\.(png|jpe?g)$/i', '.webp', $path);
    if (file_exists($webp_path)) {
        return preg_replace('/\\.(png|jpe?g)(?=([?#]|$))/i', '.webp', $url);
    }
    return $url;
}

function dtt_optimize_raw_image_tag($tag) {
    // When used as a preg_replace_callback() handler the argument is an array of matches.
    if (is_array($tag)) {
        $tag = isset($tag[0]) ? $tag[0] : '';
    }
    if (!is_string($tag) || $tag === '') {
        return ''; 
    }
    $tag = preg_replace_callback('/\\bsrc=(["\\\'])(.*?)\\1/i', function ($match) {
        return 'src=' . $match[1] . dtt_rewrite_webp_url($match[2]) . $match[1];
    }, $tag, 1);
    $tag = preg_replace_callback('/\\bsrcset=(["\\\'])(.*?)\\1/i', function ($match) {
        $items = array_map(function ($item) {
            $parts = preg_split('/\\s+/', trim($item), 2);
            $parts[0] = dtt_rewrite_webp_url($parts[0]);
            return implode(' ', $parts);
        }, explode(',', $match[2]));
        return 'srcset=' . $match[1] . implode(', ', $items) . $match[1];
    }, $tag, 1);
    if (!preg_match('/\\bloading\\s*=/i', $tag)) {
        $tag = preg_replace('/<img\\b/i', '<img loading="lazy"', $tag, 1);
    }
    if (!preg_match('/\\bdecoding\\s*=/i', $tag)) {
        $tag = preg_replace('/<img\\b/i', '<img decoding="async"', $tag, 1);
    }
    return $tag;
}

function dtt_optimize_frontend_images($html) {
    if (!$html || stripos($html, '<img') === false) {
        return $html;
    }
    return preg_replace_callback('/<img\\b[^>]*>/i', 'dtt_optimize_raw_image_tag', $html);
}

function dtt_start_frontend_image_optimization() {
    if (is_admin() || wp_doing_ajax() || is_feed() || wp_is_json_request()) {
        return;
    }
    ob_start('dtt_optimize_frontend_images');
}
add_action('template_redirect', 'dtt_start_frontend_image_optimization', 0);
