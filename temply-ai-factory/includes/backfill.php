<?php
add_action('rest_api_init', function () {
    register_rest_route('temply/v1', '/missing-covers', array(
        'methods' => 'GET',
        'callback' => 'temply_api_missing_covers',
        'permission_callback' => '__return_true'
    ));
    register_rest_route('temply/v1', '/upload-cover', array(
        'methods' => 'POST',
        'callback' => 'temply_api_upload_cover',
        'permission_callback' => '__return_true'
    ));
});

function temply_api_missing_covers() {
    $q = new WP_Query([
        'post_type' => ['page', 'post', 'truyen'],
        'posts_per_page' => 20,
        'post_status' => 'publish',
        'meta_query' => [['key' => '_thumbnail_id', 'compare' => 'NOT EXISTS']]
    ]);
    $list = [];
    if($q->have_posts()) {
        foreach($q->posts as $p) {
            $list[] = ['id' => $p->ID, 'title' => $p->post_title, 'type' => $p->post_type];
        }
    }
    return rest_ensure_response(['status'=>'success', 'items'=>$list]);
}

function temply_api_upload_cover($request) {
    $post_id = $request->get_param('post_id');
    $b64 = $request->get_param('image_b64');
    if(!$post_id || !$b64) return rest_ensure_response(['status'=>'error', 'msg'=>'Missing data']);
    
    $img_data = base64_decode($b64);
    $upload_dir = wp_upload_dir();
    $filename = 'cover-' . $post_id . '-' . wp_rand(100,999) . '.jpg';
    $filepath = $upload_dir['path'] . '/' . $filename;
    
    file_put_contents($filepath, $img_data);
    
    $filetype = wp_check_filetype($filename, null);
    $attachment = array(
        'post_mime_type' => $filetype['type'],
        'post_title'     => sanitize_file_name($filename),
        'post_content'   => '',
        'post_status'    => 'inherit'
    );
    
    require_once(ABSPATH . 'wp-admin/includes/image.php');
    $attach_id = wp_insert_attachment($attachment, $filepath, $post_id);
    $attach_data = wp_generate_attachment_metadata($attach_id, $filepath);
    wp_update_attachment_metadata($attach_id, $attach_data);
    
    set_post_thumbnail($post_id, $attach_id);
    
    return rest_ensure_response(['status'=>'success', 'attach_id'=>$attach_id]);
}
