import re

with open("tehi-theme/functions.php", "r", encoding="utf-8") as f:
    content = f.read()

new_setup_code = """
// Tự động tạo trang cần thiết nếu chưa có
function tehi_auto_create_pages() {
    $pages = [
        ['title' => 'Bảng xếp hạng', 'slug' => 'bang-xep-hang', 'template' => 'page-bangxephang.php'],
        ['title' => 'Tài khoản', 'slug' => 'tai-khoan', 'template' => 'page-profile.php'],
        ['title' => 'Truyện Hoàn Thành', 'slug' => 'truyen-hoan-thanh', 'template' => 'page-completed.php'],
        ['title' => 'Danh Mục', 'slug' => 'danh-muc', 'template' => 'page-directory.php'],
        ['title' => 'Tủ Truyện', 'slug' => 'tu-truyen', 'template' => 'page-library.php'],
        ['title' => 'Nhóm Dịch', 'slug' => 'nhom-dich', 'template' => 'page-teams.php'],
        ['title' => 'Truyện Mới', 'slug' => 'truyen-moi', 'template' => 'page-latest.php']
    ];

    foreach ($pages as $p) {
        $page_check = get_page_by_path($p['slug']);
        if (!isset($page_check->ID)) {
            $new_page_id = wp_insert_post(array(
                'post_title' => $p['title'],
                'post_name' => $p['slug'],
                'post_type' => 'page',
                'post_status' => 'publish'
            ));
            if(!is_wp_error($new_page_id)) {
                update_post_meta($new_page_id, '_wp_page_template', $p['template']);
            }
        } else {
            // Đảm bảo template đã được set đúng
            $current_template = get_post_meta($page_check->ID, '_wp_page_template', true);
            if($current_template != $p['template']) {
                update_post_meta($page_check->ID, '_wp_page_template', $p['template']);
            }
        }
    }
}
add_action('init', 'tehi_auto_create_pages');
"""

# replace the old function block
content = re.sub(r'// Tự động tạo trang cần thiết nếu chưa có[\s\S]*?add_action\(\'init\', \'tehi_auto_create_pages\'\);', new_setup_code.strip(), content)

with open("tehi-theme/functions.php", "w", encoding="utf-8") as f:
    f.write(content)
print("Functions updated")
