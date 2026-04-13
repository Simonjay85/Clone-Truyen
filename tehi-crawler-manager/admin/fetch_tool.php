<?php
if ( ! defined( 'ABSPATH' ) ) exit;

// Hàm chuyển đổi 22.4K -> 22400
function tehi_parse_number($str) {
    $str = strtoupper(trim(strip_tags($str)));
    $multiplier = 1;
    if (strpos($str, 'K') !== false) {
        $multiplier = 1000;
        $str = str_replace('K', '', $str);
    } elseif (strpos($str, 'M') !== false) {
        $multiplier = 1000000;
        $str = str_replace('M', '', $str);
    }
    return floatval($str) * $multiplier;
}

// Xử lý nạp danh sách truyện từ máy chủ (Tehitruyen)
$fetched_list = [];
if ( isset($_POST['fetch_list_btn']) && current_user_can('manage_options') ) {
    $limit = intval($_POST['fetch_limit']);
    if ($limit < 10) $limit = 50;
    
    $pages_to_fetch = ceil($limit / 20); // Giả sử 1 trang tehi trả về 20 truyện
    
    for ($page = 1; $page <= $pages_to_fetch; $page++) {
        $response = wp_remote_post( 'https://tehitruyen.com/sources/ajax/mongdaovien/load-truyen-hoan-thanh.php', array(
            'body' => array('page' => $page),
            'timeout' => 15
        ) );
        
        if ( ! is_wp_error( $response ) ) {
            $body = wp_remote_retrieve_body( $response );
            // Xóa BOM ẩn của UTF-8
            $body = preg_replace('/^[\xef\xbb\xbf]+/', '', $body);
            
            // Parse JSON hoặc HTML tùy site trả về
            $html = '';
            $json = json_decode($body, true);
            if ($json && isset($json['html'])) {
                $html = $json['html'];
            } else {
                // Nếu API trả về chuỗi JSON raw bị lỗi khác, ta fallback bỏ dấu \
                $html = stripslashes($body); 
            }
            
            // Chia nhỏ từng card truyện để bóc tách chính xác
            $cards = explode('<div class="truyen-comic-card">', $html);
            array_shift($cards); // Bỏ phần header trước card đầu
            
            foreach ($cards as $card) {
                // Tiết kiệm dung lượng: Dừng ngay khi đủ chỉ tiêu limit
                if (count($fetched_list) >= $limit) break;
                
                // Trích xuất URL
                preg_match('/href=[\'"](.*?)[\'"]/', $card, $url_match);
                $href = !empty($url_match[1]) ? $url_match[1] : '';
                
                // Trích xuất Title
                preg_match('/<h3 class="truyen-comic-title.*?>(.*?)<\/h3>/s', $card, $title_match);
                $title = !empty($title_match[1]) ? strip_tags(trim($title_match[1])) : '';
                
                if (empty($href) || empty($title)) continue;
                
                // Trích xuất Lượt View (tìm div có icon-lua.png)
                $real_views = 0;
                preg_match('/icon-lua.*?<span class="truyen-stat-count">(.*?)<\/span>/s', $card, $view_match);
                if (!empty($view_match[1])) {
                    $real_views = tehi_parse_number($view_match[1]);
                }
                
                // Trích xuất Trạng thái (tìm thẻ status xem có chữ HOT không)
                $is_hot = 0;
                if (stripos($card, 'HOT') !== false || stripos($card, 'icon-lua-hot') !== false) {
                    $is_hot = 1;
                }
                
                // Trích xuất ngày? (Thường danh sách không hiện ngày cụ thể, nên ta random biên độ nhỏ quanh thời điểm hiện tại hoặc để mặc định)
                
                $fetched_list[] = array(
                    'url' => $href,
                    'title' => $title,
                    'real_views' => $real_views,
                    'is_hot' => $is_hot
                );
            }
        }
        if (count($fetched_list) >= $limit) break;
    }
}

// Xử lý Thêm Hàng Loạt (Bulk Add)
if ( isset($_POST['bulk_add_jobs']) && current_user_can('manage_options') ) {
    global $wpdb;
    $table_name = $wpdb->prefix . 'crawler_jobs';
    
    $urls = $_POST['bulk_urls'];
    $views = $_POST['bulk_views'];
    $hots = isset($_POST['bulk_hots']) ? $_POST['bulk_hots'] : [];
    $dates = $_POST['bulk_dates'];
    $added_count = 0;
    
    if ( !empty($urls) && is_array($urls) ) {
        foreach ( $urls as $index => $url ) {
            $url = sanitize_text_field($url);
            
            // Xây dựng chuỗi JSON fake meta
            $is_hot = isset($hots[$index]) ? 1 : 0;
            $view_count = intval($views[$index]);
            // Nếu người dùng lười không điền view, tự random
            if ($view_count <= 0) {
                $view_count = rand(10000, 500000);
            }
            $date = sanitize_text_field($dates[$index]);
            
            $fake_meta = json_encode(array(
                'views' => $view_count,
                'hot'   => $is_hot,
                'date'  => $date
            ));
            
            // Kiểm tra trùng lặp chưa hoàn thành
            $exists = $wpdb->get_var($wpdb->prepare("SELECT id FROM $table_name WHERE novel_url = %s AND (status = 'completed' OR status = 'pending' OR status = 'processing')", $url));
            if ( !$exists ) {
                $wpdb->replace(
                    $table_name,
                    array(
                        'novel_url' => $url,
                        'status'    => 'pending',
                        'ai_rewrite'=> 0, // Mặc định không AI cho hàng loạt để giữ tốc độ
                        'fake_meta' => $fake_meta
                    )
                );
                $added_count++;
            }
        }
        echo '<div class="notice notice-success is-dismissible"><p>Đã vứt ' . $added_count . ' truyện kèm Meta ảo vào hàng chờ!</p></div>';
    }
}
?>

<div style="background: #fff; padding: 20px; box-shadow: 0 1px 1px rgba(0,0,0,.04); margin-bottom: 20px;">
    <h3><span class="dashicons dashicons-search" style="margin-top:4px;"></span> Fetcher: Quét danh sách truyện hàng loạt</h3>
    
    <!-- Form Get Data -->
    <form method="POST" action="" style="margin-bottom: 20px;">
        <label>Muốn quét ra bao nhiêu truyện mới nhất? (Limit): </label>
        <input type="number" name="fetch_limit" value="50" min="10" max="500" style="width: 80px;"> Cuốn
        <input type="submit" name="fetch_list_btn" class="button" value="Bắt Đầu Quét">
        <span style="font-size:12px; color:#666;">(Tool sẽ tự động quét các trang Tehitruyen, cào Views/Hot thực tế để bạn đối chiếu)</span>
    </form>
    
    <!-- Kết quả Bảng Truyện -->
    <?php if ( !empty($fetched_list) ) : ?>
    <hr>
    <form method="POST" action="">
        <table class="wp-list-table widefat fixed striped">
            <thead>
                <tr>
                    <th style="width:40px;"><input type="checkbox" id="checkAll"></th>
                    <th style="width:30%;">Tên Truyện</th>
                    <th>Fake Lượt Đọc (Views)</th>
                    <th style="width:100px;">Gắn mác HOT</th>
                    <th>Fake Ngày Đăng</th>
                </tr>
            </thead>
            <tbody>
                <?php foreach ( $fetched_list as $index => $item ) : ?>
                <tr>
                    <td>
                        <input type="checkbox" class="cb-select" name="bulk_urls[<?php echo $index; ?>]" value="<?php echo esc_attr($item['url']); ?>">
                    </td>
                    <td>
                        <strong><?php echo esc_html($item['title']); ?></strong><br>
                        <a href="<?php echo esc_attr($item['url']); ?>" target="_blank" style="font-size:11px; text-decoration:none;"><?php echo esc_html($item['url']); ?></a>
                    </td>
                    <td>
                        <input type="number" name="bulk_views[<?php echo $index; ?>]" value="<?php echo esc_attr($item['real_views']); ?>" style="width: 100px;">
                    </td>
                    <td>
                        <input type="checkbox" name="bulk_hots[<?php echo $index; ?>]" value="1" <?php echo $item['is_hot'] ? 'checked' : ''; ?>>
                    </td>
                    <td>
                        <input type="date" name="bulk_dates[<?php echo $index; ?>]" value="<?php echo date('Y-m-d'); ?>">
                    </td>
                </tr>
                <?php endforeach; ?>
            </tbody>
        </table>
        <p class="submit">
            <input type="submit" name="bulk_add_jobs" class="button button-primary" value="Bơm vào Hàng Chờ (Queue)">
        </p>
    </form>
    <script>
        document.getElementById('checkAll').addEventListener('change', function(e) {
            var cbs = document.querySelectorAll('.cb-select');
            for(var i=0; i<cbs.length; i++) cbs[i].checked = e.target.checked;
        });
    </script>
    <?php endif; ?>
</div>
