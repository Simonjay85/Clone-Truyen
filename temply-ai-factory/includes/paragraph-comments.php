<?php
if (!defined('ABSPATH')) exit;

/**
 * Handle Adding a Paragraph Comment
 */
add_action('wp_ajax_temply_add_paragraph_comment', 'temply_ajax_add_paragraph_comment');
add_action('wp_ajax_nopriv_temply_add_paragraph_comment', 'temply_ajax_add_paragraph_comment');

function temply_ajax_add_paragraph_comment() {
    // Basic verification
    if (!isset($_POST['nonce']) || !wp_verify_nonce($_POST['nonce'], 'temply_ai_nonce')) {
        wp_send_json_error(['message' => 'Lỗi bảo mật bảo vệ form. Khuyên bạn tải lại trang.']);
    }

    $post_id = intval($_POST['post_id']);
    $p_index = intval($_POST['p_index']);
    $comment_content = sanitize_textarea_field($_POST['comment_content']);

    if(empty($comment_content)) wp_send_json_error(['message' => 'Nội dung bình luận rỗng!']);

    $user = wp_get_current_user();
    $author_name = '';
    $author_email = '';
    
    if ( $user->exists() ) {
        $author_name = $user->display_name;
        $author_email = $user->user_email;
    } else {
        $author_name = sanitize_text_field($_POST['author_name'] ?? '');
        $author_email = sanitize_text_field($_POST['author_email'] ?? '');
        if(empty($author_name)) wp_send_json_error(['message' => 'Vui lòng nhập Tên của bạn.']);
    }

    $time = current_time('mysql');
    
    $data = array(
        'comment_post_ID' => $post_id,
        'comment_author' => $author_name,
        'comment_author_email' => $author_email,
        'comment_content' => $comment_content,
        'comment_type' => 'comment',
        'comment_parent' => 0,
        'user_id' => $user->exists() ? $user->ID : 0,
        'comment_date' => $time,
        'comment_approved' => 1,
    );

    $comment_id = wp_insert_comment($data);
    
    if($comment_id) {
        // Lưu index đoạn văn vào comment meta
        add_comment_meta($comment_id, 'temply_p_index', $p_index);
        
        // Trả về HTML render sẵn comment mới nhất để chèn cục bộ
        $avatar = get_avatar($author_email, 40, '', '', array('class' => 'w-full h-full object-cover'));
        $date_str = date('d/m/Y H:i', strtotime($time));
        $content_safe = wp_kses_post($comment_content);
        
        $html = "
        <div class='flex gap-4 border-b border-surface-container-high pb-4 mb-4 last:border-0 last:pb-0 last:mb-0'>
            <div class='w-10 h-10 rounded-full bg-surface-container overflow-hidden shrink-0'>{$avatar}</div>
            <div class='flex-1'>
                <div class='flex items-baseline gap-2 mb-1'>
                    <h4 class='font-bold text-sm text-on-surface'>" . esc_html($author_name) . "</h4>
                    <span class='text-[11px] text-on-surface-variant'>{$date_str}</span>
                </div>
                <p class='text-sm text-on-surface-variant leading-relaxed'>{$content_safe}</p>
            </div>
        </div>";

        wp_send_json_success(['html' => $html, 'message' => 'Bình luận thành công!']);
    } else {
        wp_send_json_error(['message' => 'Lỗi hệ thống khi gửi bình luận.']);
    }
}

/**
 * Handle Fetching Paragraph Comments
 */
add_action('wp_ajax_temply_load_paragraph_comments', 'temply_ajax_load_paragraph_comments');
add_action('wp_ajax_nopriv_temply_load_paragraph_comments', 'temply_ajax_load_paragraph_comments');

function temply_ajax_load_paragraph_comments() {
    $post_id = intval($_POST['post_id']);
    
    // Nếu truyền p_index cụ thể, ta load comments cho paragraph đó
    // Nếu request_type = 'map', ta load số lượng comment của toàn bộ bài
    $request_type = sanitize_text_field($_POST['request_type'] ?? 'map');
    
    $comments = get_comments(array('post_id' => $post_id, 'status' => 'approve'));
    
    if ($request_type === 'map') {
        // Đếm số lượng comment theo mỗi p_index gốc
        $counts = [];
        foreach($comments as $c) {
            $p_index = get_comment_meta($c->comment_ID, 'temply_p_index', true);
            if($p_index !== '') {
                if(!isset($counts[$p_index])) $counts[$p_index] = 0;
                $counts[$p_index]++;
            }
        }
        wp_send_json_success(['counts' => $counts]);
        return;
    } 
    else if ($request_type === 'chunk') {
        // Lấy riêng list comment html cho đoạn được chọn
        $p_index_target = intval($_POST['p_index']);
        $html = '';
        $found = 0;
        foreach($comments as $c) {
            $p_index = get_comment_meta($c->comment_ID, 'temply_p_index', true);
            if($p_index !== '' && intval($p_index) === $p_index_target) {
                $avatar = get_avatar($c->comment_author_email, 40, '', '', array('class' => 'w-full h-full object-cover'));
                $date_str = date('d/m/Y H:i', strtotime($c->comment_date));
                $content_safe = wp_kses_post($c->comment_content);
                $author_name = esc_html($c->comment_author);
                
                $html .= "
                <div class='flex gap-4 border-b border-surface-container-high pb-4 mb-4 last:border-0 last:pb-0 last:mb-0'>
                    <div class='w-10 h-10 rounded-full bg-surface-container overflow-hidden shrink-0'>{$avatar}</div>
                    <div class='flex-1'>
                        <div class='flex items-baseline gap-2 mb-1'>
                            <h4 class='font-bold text-sm text-on-surface'>{$author_name}</h4>
                            <span class='text-[11px] text-on-surface-variant'>{$date_str}</span>
                        </div>
                        <p class='text-sm text-on-surface-variant leading-relaxed'>{$content_safe}</p>
                    </div>
                </div>";
                $found++;
            }
        }
        if($found == 0) {
            $html = "<div class='text-center py-6 text-sm text-on-surface-variant italic'>Chưa có cao kiến nào. Hãy bóc tem đoạn này!</div>";
        }
        wp_send_json_success(['html' => $html, 'count' => $found]);
        return;
    }

    wp_send_json_error(['message' => 'Lệnh không hợp lệ']);
}
