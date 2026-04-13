<?php
/**
 * Trạm Dữ Liệu - Hiển thị Thông tin "Bản Thiết Kế Ma Thuật" (Blueprint) đã tạo ra bộ truyện
 */
if (!defined('ABSPATH')) exit;

add_action('add_meta_boxes', 'temply_register_blueprint_metabox');
function temply_register_blueprint_metabox() {
    add_meta_box(
        'temply_blueprint_box',
        '🌟 AI Blueprint (Bản Thiết Kế Gốc)',
        'temply_render_blueprint_metabox',
        'truyen',
        'normal',
        'high'
    );
}

function temply_render_blueprint_metabox($post) {
    // Thu thập Meta data
    $world = get_post_meta($post->ID, '_temply_blueprint_world', true);
    $characters = get_post_meta($post->ID, '_temply_blueprint_characters', true);
    $keywords = get_post_meta($post->ID, '_temply_blueprint_keywords', true);
    $genre = get_post_meta($post->ID, '_temply_blueprint_genre', true);
    $tone = get_post_meta($post->ID, '_temply_blueprint_tone', true);
    $art = get_post_meta($post->ID, '_temply_blueprint_art', true);

    if (empty($world) && empty($keywords)) {
        echo '<p style="color:red; font-weight:bold;">Không tìm thấy dữ liệu Blueprint cho truyện này (Có thể truyện được tạo thủ công hoặc tạo trước bản cập nhật ghi log).</p>';
        return;
    }

    ?>
    <div style="background: #f8f9fa; padding: 15px; border-radius: 8px; border: 1px solid #ddd;">
        <p style="margin-top:0;"><i>Hệ thống tự động lưu lại các tham số Prompt (Bối cảnh, Tương Tác) mà AI đã sử dụng để tạo ra bộ truyện này. Bạn có thể chép lại để giữ nguyên phong cách (tone) cho phần 2. Dữ liệu này chỉ mang tính tham khảo, không hiển thị cho người xem đọc.</i></p>
        
        <div style="display:flex; gap:15px; margin-bottom: 15px;">
            <div style="flex:1;">
                <strong>📚 Thể Loại:</strong>
                <input type="text" class="large-text" readonly value="<?php echo esc_attr($genre); ?>" style="background: #eef1f5;" />
            </div>
            <div style="flex:1;">
                <strong>🖋 Văn Phong:</strong>
                <input type="text" class="large-text" readonly value="<?php echo esc_attr($tone); ?>" style="background: #eef1f5;" />
            </div>
            <div style="flex:1;">
                <strong>🎨 Phong Cách Ảnh:</strong>
                <input type="text" class="large-text" readonly value="<?php echo esc_attr($art); ?>" style="background: #eef1f5;" />
            </div>
        </div>

        <div style="margin-bottom: 15px;">
            <strong>🔑 Từ Khoá / Ý Tưởng (Keywords):</strong>
            <textarea class="large-text" rows="3" readonly style="background: #eef1f5; margin-top:5px; resize:vertical;"><?php echo esc_textarea($keywords); ?></textarea>
        </div>

        <div style="margin-bottom: 15px;">
            <strong>🌍 Bối Cảnh (World Building):</strong>
            <textarea class="large-text" rows="5" readonly style="background: #eef1f5; margin-top:5px; resize:vertical;"><?php echo esc_textarea($world); ?></textarea>
        </div>

        <div>
            <strong>🎭 Hệ Thống Nhân Vật (Characters):</strong>
            <textarea class="large-text" rows="5" readonly style="background: #eef1f5; margin-top:5px; resize:vertical;"><?php echo esc_textarea($characters); ?></textarea>
        </div>
    </div>
    <?php
}
