<?php
if ( ! defined( 'ABSPATH' ) ) exit;

global $wpdb;
$table_name = $wpdb->prefix . 'crawler_jobs';

// Xử lý Thêm Job mới
if ( isset( $_POST['submit_crawler_job'] ) && current_user_can('manage_options') ) {
    $url = sanitize_text_field( $_POST['novel_url'] );
    $ai_rewrite = isset($_POST['ai_rewrite']) ? 1 : 0;
    
    if ( !empty($url) ) {
        // Kiểm tra xem đã tồn tại và hoàn thành chưa (bỏ qua truyện trùng)
        $exists = $wpdb->get_var($wpdb->prepare("SELECT id FROM $table_name WHERE novel_url = %s AND (status = 'completed' OR status = 'pending' OR status = 'processing')", $url));
        
        if ( $exists ) {
            echo '<div class="notice notice-warning is-dismissible"><p>URL này đã có trong hệ thống (Đang chờ/Đã Quét xong). Đã tự động bỏ qua!</p></div>';
        } else {
            $wpdb->replace(
                $table_name,
                array(
                    'novel_url' => $url,
                    'status'    => 'pending',
                    'ai_rewrite'=> $ai_rewrite
                )
            );
            echo '<div class="notice notice-success is-dismissible"><p>Đã thêm URL vào hàng đợi cào dữ liệu!</p></div>';
        }
    }
}

// Xử lý Xóa Job
if ( isset($_GET['delete_job']) && current_user_can('manage_options') ) {
    $wpdb->delete( $table_name, array( 'id' => intval($_GET['delete_job']) ) );
}

// Lưu OpenAI Key nếu có submit
if ( isset( $_POST['save_settings'] ) && current_user_can('manage_options') ) {
    update_option('tehi_openai_key', sanitize_text_field($_POST['openai_key']));
    echo '<div class="notice notice-success is-dismissible"><p>Đã lưu API Key AI!</p></div>';
}

$openai_key = get_option('tehi_openai_key', '');

// Hotfix Cập nhật DB (Tạo cột fake_meta nếu chưa có)
$wpdb->query("ALTER TABLE $table_name ADD COLUMN fake_meta text AFTER ai_rewrite");

// Lấy danh sách việc
$jobs = $wpdb->get_results( "SELECT * FROM $table_name ORDER BY created_at DESC" );
?>

<div class="wrap">
    <h1 class="wp-heading-inline">Trạm Quản Lý Crawler & AI Thực Tế Ảo</h1>
    <hr class="wp-header-end">
    
    <!-- Cài đặt AI -->
    <div style="background: #eef2f5; padding: 15px; border-left: 4px solid #0073aa; margin-bottom: 20px;">
        <form method="POST" action="">
            <strong>Cấu hình API Key ChatGPT/DALL-E:</strong> 
            <input name="openai_key" type="password" value="<?php echo esc_attr($openai_key); ?>" placeholder="sk-..." style="width: 300px;">
            <input type="submit" name="save_settings" class="button" value="Lưu Key">
            <span style="font-size:12px; color:#555;">(Hỗ trợ Spin nội dung & Sinh ảnh Avatar tự động bằng AI)</span>
        </form>
    </div>

    <!-- TÍNH NĂNG FETCH HÀNG LOẠT TRUYỆN MỚI -->
    <?php include TEHI_CRAWLER_DIR . 'admin/fetch_tool.php'; ?>

    <!-- Form Thêm Tool -->
    <div style="background: #fff; padding: 20px; box-shadow: 0 1px 1px rgba(0,0,0,.04); max-width: 800px; margin-bottom: 20px;">
        <h3>Thêm Truyện Mới Vào Hàng Đợi (Queue)</h3>
        <form method="POST" action="">
            <table class="form-table">
                <tr>
                    <th scope="row"><label for="novel_url">URL Truyện (Từ TeHi):</label></th>
                    <td><input name="novel_url" type="url" id="novel_url" class="regular-text" required placeholder="https://tehitruyen.com/mot-ly-matcha.html"></td>
                </tr>
                <tr>
                    <th scope="row">AI Viết Lại (Rewrite)</th>
                    <td>
                        <label for="ai_rewrite">
                            <input name="ai_rewrite" type="checkbox" id="ai_rewrite" value="1">
                            Kích hoạt AI tự động tẩy trắng/sáng tạo lại nội dung trước khi đăng (Cần Bot Python có khoá API).
                        </label>
                    </td>
                </tr>
            </table>
            <p class="submit"><input type="submit" name="submit_crawler_job" id="submit" class="button button-primary" value="Vứt vào Hàng Chờ (Queue)"></p>
        </form>
    </div>

    <h3>Tiến độ hệ thống (Dashboard Live) <span id="sync_status" style="font-size: 13px; color: green; font-weight: normal; margin-left: 10px;">Đang làm mới tự động...</span></h3>
    <table class="wp-list-table widefat fixed striped" id="crawler_table">
        <thead>
            <tr>
                <th>ID</th>
                <th>URL Truyện</th>
                <th>Tên Truyện</th>
                <th>Trạng Thái</th>
                <th>Tiến độ</th>
                <th>AI Rewrite</th>
                <th>Lỗi (Error Log)</th>
                <th>Hành Động</th>
            </tr>
        </thead>
        <tbody>
            <?php if ( $jobs ) : ?>
                <?php foreach ( $jobs as $job ) : ?>
                    <tr>
                        <td><?php echo esc_html( $job->id ); ?></td>
                        <td><a href="<?php echo esc_url( $job->novel_url ); ?>" target="_blank"><?php echo esc_html( $job->novel_url ); ?></a></td>
                        <td><strong><?php echo esc_html( $job->novel_title ?: '...' ); ?></strong></td>
                        <td>
                            <?php 
                            if ($job->status == 'pending') echo '<span class="dashicons dashicons-clock" style="color: blue;"></span> Chờ quét';
                            elseif ($job->status == 'processing') echo '<span class="dashicons dashicons-update-alt" style="color: orange;"></span> Đang quét...';
                            elseif ($job->status == 'completed') echo '<span class="dashicons dashicons-yes-alt" style="color: green;"></span> Hoàn thành';
                            elseif ($job->status == 'error') echo '<span class="dashicons dashicons-warning" style="color: red;"></span> Lỗi';
                            ?>
                        </td>
                        <td>
                            <?php 
                                if($job->total_chapters > 0) {
                                    $percent = round(($job->crawled_chapters / $job->total_chapters) * 100);
                                    echo "<div style='margin-bottom:5px; font-weight:bold;'>{$percent}% ({$job->crawled_chapters}/{$job->total_chapters})</div>";
                                    echo "<progress value='{$percent}' max='100' style='width: 100%; height: 18px;'></progress>";
                                } else {
                                    echo "0 / 0";
                                }
                            ?>
                        </td>
                        <td><?php echo $job->ai_rewrite ? 'Có' : 'Không'; ?></td>
                        <td style="color:red; max-width: 150px; overflow:hidden; text-overflow:ellipsis;" title="<?php echo esc_attr($job->error_log); ?>"><?php echo esc_html( $job->error_log ); ?></td>
                        <td>
                            <a href="?page=tehi-crawler&delete_job=<?php echo $job->id; ?>" class="button button-small" onclick="return confirm('Chắc chắn xoá job này?');">Xóa</a>
                        </td>
                    </tr>
                <?php endforeach; ?>
            <?php else : ?>
                <tr><td colspan="8">Không có tiến trình nào trong hàng đợi.</td></tr>
            <?php endif; ?>
        </tbody>
    </table>
</div>

<script>
// AJAX tự động load lại tiến trình không cần F5 (5s 1 lần)
setInterval(function() {
    jQuery.get(location.href, function(data) {
        var newTableBody = jQuery(data).find('#crawler_table tbody').html();
        jQuery('#crawler_table tbody').html(newTableBody);
    });
}, 5000);
</script>
