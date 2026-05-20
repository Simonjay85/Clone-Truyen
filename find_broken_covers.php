<?php
require_once('wp-load.php');

$args = array(
    'post_type'      => 'truyen',
    'post_status'    => 'publish',
    'posts_per_page' => -1,
);
$query = new WP_Query($args);
$results = array();

if ($query->have_posts()) {
    while ($query->have_posts()) {
        $query->the_post();
        $id = get_the_ID();
        $title = get_the_title();
        
        $has_thumb = has_post_thumbnail($id);
        $thumb_url = '';
        $file_path = '';
        $file_exists = false;
        $is_broken = false;
        $status = 'ok';
        $aspect_ratio = 'unknown';
        
        if ($has_thumb) {
            $thumb_id = get_post_thumbnail_id($id);
            $thumb_url = get_the_post_thumbnail_url($id, 'full');
            $file_path = get_attached_file($thumb_id);
            
            if (!$file_path) {
                $is_broken = true;
                $status = 'attachment_meta_missing';
            } elseif (!file_exists($file_path)) {
                $is_broken = true;
                $status = 'file_not_found';
            } elseif (filesize($file_path) === 0) {
                $is_broken = true;
                $status = 'empty_file';
            } else {
                // Get dimensions to check aspect ratio
                $info = @getimagesize($file_path);
                if ($info) {
                    $width = $info[0];
                    $height = $info[1];
                    if ($width > 0 && $height > 0) {
                        $ratio = $width / $height;
                        if ($ratio > 1.1) {
                            $aspect_ratio = 'landscape (' . $width . 'x' . $height . ')';
                        } elseif ($ratio < 0.9) {
                            $aspect_ratio = 'portrait (' . $width . 'x' . $height . ')';
                        } else {
                            $aspect_ratio = 'square (' . $width . 'x' . $height . ')';
                        }
                    }
                } else {
                    $is_broken = true;
                    $status = 'invalid_image_file';
                }
            }
        } else {
            $is_broken = true;
            $status = 'no_thumbnail';
        }
        
        if ($is_broken || $aspect_ratio !== 'portrait') {
            $results[] = array(
                'id' => $id,
                'title' => $title,
                'status' => $status,
                'thumb_url' => $thumb_url,
                'file_path' => $file_path,
                'aspect_ratio' => $aspect_ratio
            );
        }
    }
    wp_reset_postdata();
}

header('Content-Type: application/json');
echo json_encode($results, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
?>
