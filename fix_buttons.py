import re

auth_ui = """<?php if(is_user_logged_in()): 
    $current_user = wp_get_current_user();
    $avatar_url = get_avatar_url($current_user->ID);
?>
    <a href="/tai-khoan/" class="flex items-center gap-2 hover:bg-surface-container-high px-3 py-1.5 rounded-full transition-colors cursor-pointer border border-outline-variant/20 shadow-sm bg-white/50">
        <img src="<?php echo esc_url($avatar_url); ?>" class="w-8 h-8 rounded-full object-cover">
        <span class="text-slate-700 font-bold hidden sm:block"><?php echo esc_html($current_user->display_name); ?></span>
    </a>
<?php else: ?>
    <a href="/tai-khoan/" class="text-slate-600 hover:text-blue-500 px-4 py-2 transition-all font-bold">Đăng nhập</a>
    <a href="/tai-khoan/#register" class="bg-gradient-to-br from-primary to-primary-container text-white px-6 py-2 rounded-full shadow-lg shadow-primary/20 hover:shadow-primary/40 active:scale-95 transition-all text-sm font-bold inline-block">Đăng ký</a>
<?php endif; ?>"""

for file_name in ["tehi-theme/header.php", "tehi-theme/header-home.php"]:
    with open(file_name, "r", encoding="utf-8") as f:
        content = f.read()
    
    # We want to replace the buttons inside <div class="flex items-center gap-4 font-\['Plus_Jakarta_Sans'\] text-sm font-medium">
    pattern = r'<button class="text-slate-600 hover:text-blue-500 px-4 py-2 transition-all">Đăng nhập</button>\s*<button class="bg-gradient-to-br from-primary to-primary-container text-white px-6 py-2 rounded-full shadow-lg shadow-primary/20 hover:shadow-primary/40 active:scale-95 transition-all">Đăng ký</button>'

    if re.search(pattern, content):
        content = re.sub(pattern, auth_ui, content)
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Update buttons in {file_name}")
    else:
        print(f"Pattern not found in {file_name}")

