<?php
add_action('rest_api_init', function () {
    register_rest_route('temply/v1', '/missing-covers', array(
        'methods' => 'GET',
        'callback' => 'temply_api_missing_covers',
        'permission_callback' => 'temply_api_can_backfill_covers'
    ));
    register_rest_route('temply/v1', '/upload-cover', array(
        'methods' => 'POST',
        'callback' => 'temply_api_upload_cover',
        'permission_callback' => 'temply_api_can_backfill_covers'
    ));
});

function temply_api_can_backfill_covers($request) {
    if (current_user_can('manage_options')) {
        return true;
    }

    $configured_token = defined('TEHI_BACKFILL_TOKEN') ? TEHI_BACKFILL_TOKEN : get_option('tehi_backfill_token', '');
    $request_token = $request ? (string) $request->get_param('token') : '';

    return $configured_token && hash_equals((string) $configured_token, $request_token);
}

function temply_api_find_source_cover($post_id) {
    $meta_keys = array('cover_url', '_cover_url', 'source_cover', '_source_cover', 'image_url', '_image_url', 'thumbnail_url', '_thumbnail_url');
    foreach ($meta_keys as $key) {
        $value = get_post_meta($post_id, $key, true);
        if ($value && filter_var($value, FILTER_VALIDATE_URL)) {
            return esc_url_raw($value);
        }
    }

    return '';
}

function temply_api_missing_covers($request = null) {
    $q = new WP_Query([
        'post_type' => ['page', 'post', 'truyen'],
        'posts_per_page' => 20,
        'post_status' => 'publish',
        'meta_query' => [['key' => '_thumbnail_id', 'compare' => 'NOT EXISTS']]
    ]);
    $list = [];
    if($q->have_posts()) {
        foreach($q->posts as $p) {
            $list[] = [
                'id' => $p->ID,
                'title' => $p->post_title,
                'type' => $p->post_type,
                'source_cover' => temply_api_find_source_cover($p->ID),
            ];
        }
    }
    return rest_ensure_response(['status'=>'success', 'items'=>$list]);
}

function temply_api_upload_cover($request) {
    $post_id = absint($request->get_param('post_id'));
    $b64 = $request->get_param('image_b64');
    $image_url = esc_url_raw($request->get_param('image_url'));
    if(!$post_id || (!$b64 && !$image_url)) return rest_ensure_response(['status'=>'error', 'msg'=>'Missing data']);

    require_once(ABSPATH . 'wp-admin/includes/image.php');
    require_once(ABSPATH . 'wp-admin/includes/file.php');
    require_once(ABSPATH . 'wp-admin/includes/media.php');

    if ($image_url) {
        $tmp = download_url($image_url, 30);
        if (is_wp_error($tmp)) {
            return rest_ensure_response(['status'=>'error', 'msg'=>$tmp->get_error_message()]);
        }

        $filename = basename(parse_url($image_url, PHP_URL_PATH));
        if (!$filename || strpos($filename, '.') === false) {
            $filename = 'cover-' . $post_id . '.jpg';
        }

        $file_array = array(
            'name' => sanitize_file_name($filename),
            'tmp_name' => $tmp,
        );

        $attach_id = media_handle_sideload($file_array, $post_id);
        if (is_wp_error($attach_id)) {
            @unlink($tmp);
            return rest_ensure_response(['status'=>'error', 'msg'=>$attach_id->get_error_message()]);
        }

        set_post_thumbnail($post_id, $attach_id);
        return rest_ensure_response(['status'=>'success', 'attach_id'=>$attach_id, 'source'=>'url']);
    }
    
    $img_data = base64_decode($b64);
    if (!$img_data) {
        return rest_ensure_response(['status'=>'error', 'msg'=>'Invalid base64 image']);
    }
    $upload_dir = wp_upload_dir();
    $filename = 'cover-' . $post_id . '-' . wp_rand(100,999) . '.jpg';
    $filepath = $upload_dir['path'] . '/' . $filename;
    
    if (false === file_put_contents($filepath, $img_data)) {
        return rest_ensure_response(['status'=>'error', 'msg'=>'Cannot write upload file']);
    }
    
    $filetype = wp_check_filetype($filename, null);
    if (empty($filetype['type']) || strpos($filetype['type'], 'image/') !== 0) {
        @unlink($filepath);
        return rest_ensure_response(['status'=>'error', 'msg'=>'Invalid image type']);
    }
    $attachment = array(
        'post_mime_type' => $filetype['type'],
        'post_title'     => sanitize_file_name($filename),
        'post_content'   => '',
        'post_status'    => 'inherit'
    );
    
    $attach_id = wp_insert_attachment($attachment, $filepath, $post_id);
    $attach_data = wp_generate_attachment_metadata($attach_id, $filepath);
    wp_update_attachment_metadata($attach_id, $attach_data);
    
    set_post_thumbnail($post_id, $attach_id);
    
    return rest_ensure_response(['status'=>'success', 'attach_id'=>$attach_id]);
}
