import re

# 1. Update functions.php
with open("tehi-theme/functions.php", "r", encoding="utf-8") as f:
    functions_content = f.read()

if "register_nav_menus" not in functions_content:
    theme_setup = """
// Khởi tạo các menu
function tehi_theme_menus() {
    register_nav_menus([
        'header-menu' => 'Menu Chính (Header)'
    ]);
}
add_action('init', 'tehi_theme_menus');
"""
    functions_content += "\\n" + theme_setup
    with open("tehi-theme/functions.php", "w", encoding="utf-8") as f:
        f.write(functions_content)

# 2. Update header.php and header-home.php
dynamic_menu_php = """<div class="hidden md:flex gap-6 font-['Plus_Jakarta_Sans'] text-sm font-medium">
    <?php
    $locations = get_nav_menu_locations();
    if(isset($locations['header-menu'])) {
        $menu = get_term($locations['header-menu'], 'nav_menu');
        if($menu && !is_wp_error($menu)) {
            $menu_items = wp_get_nav_menu_items($menu->term_id);
            foreach($menu_items as $item) {
                // Kiểm tra active (Trang hiện tại trùng với URL của menu)
                $is_active = (htmlspecialchars_decode($item->url) == get_permalink() || htmlspecialchars_decode($item->url) == $_SERVER['REQUEST_URI'] || htmlspecialchars_decode($item->url) == home_url($_SERVER['REQUEST_URI']));
                
                if($is_active) {
                    echo '<a class="text-blue-700 dark:text-blue-400 border-b-2 border-blue-600 pb-1 font-bold" href="' . esc_url($item->url) . '">' . esc_html($item->title) . '</a>';
                } else {
                    echo '<a class="text-slate-600 dark:text-slate-400 hover:text-blue-500 transition-colors" href="' . esc_url($item->url) . '">' . esc_html($item->title) . '</a>';
                }
            }
        }
    } else {
        // Fallback default
        ?>
        <a class="text-blue-700 dark:text-blue-400 border-b-2 border-blue-600 pb-1 font-bold" href="<?php echo home_url('/'); ?>">Trang chủ</a>
        <a class="text-slate-600 dark:text-slate-400 hover:text-blue-500 transition-colors" href="/danh-muc">Danh mục</a>
        <a class="text-slate-600 dark:text-slate-400 hover:text-blue-500 transition-colors" href="/bang-xep-hang">Bảng xếp hạng</a>
        <?php
    }
    ?>
    </div>"""

for header_file in ["tehi-theme/header.php", "tehi-theme/header-home.php"]:
    with open(header_file, "r", encoding="utf-8") as f:
        header_content = f.read()
    
    # We want to replace the div section.
    # regex to match: <div class="hidden md:flex gap-6 font-\['Plus_Jakarta_Sans'\] text-sm font-medium">.*?</div>
    pattern = r'<div class="hidden md:flex gap-6 font-\[\'Plus_Jakarta_Sans\'\] text-sm font-medium">.*?</div>'
    
    if re.search(pattern, header_content, re.DOTALL):
        header_content = re.sub(pattern, dynamic_menu_php, header_content, flags=re.DOTALL)
        with open(header_file, "w", encoding="utf-8") as f:
            f.write(header_content)
        print(f"Updated {header_file}")
    elif "tehi_header_dynamic" in header_content:
         print(f"Already dynamic {header_file}")
    else:
        # manual replace
        print(f"Failed to regex {header_file}, searching alternative")

