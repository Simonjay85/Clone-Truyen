import re

with open("tehi-theme/functions.php", "r", encoding="utf-8") as f:
    functions_code = f.read()

setup_code = """
// Tự động tạo trang cần thiết nếu chưa có
function tehi_auto_create_pages() {
    $pages = [
        ['title' => 'Bảng xếp hạng', 'slug' => 'bang-xep-hang', 'template' => 'page-bangxephang.php'],
        ['title' => 'Tài khoản', 'slug' => 'tai-khoan', 'template' => 'page-profile.php'],
        ['title' => 'Truyện Hoàn Thành', 'slug' => 'truyen-hoan-thanh', 'template' => 'page-completed.php']
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

if 'tehi_auto_create_pages' not in functions_code:
    functions_code += "\\n" + setup_code
    with open("tehi-theme/functions.php", "w", encoding="utf-8") as f:
        f.write(functions_code)
    print("Added page setup hook")
else:
    print("Page setup hook already exists")

