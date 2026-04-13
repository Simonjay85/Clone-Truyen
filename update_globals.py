import os
import shutil

# 1. Move header-home to header, footer-home to footer
shutil.copy("tehi-theme/header-home.php", "tehi-theme/header.php")
shutil.copy("tehi-theme/footer-home.php", "tehi-theme/footer.php")

# 2. Update functions.php to dequeue bootstrap
with open("tehi-theme/functions.php", "r", encoding="utf-8") as f:
    functions = f.read()

# We need to remove wp_enqueue_style for bootstrap/theme stuff if they exist
# A safer way is just to comment out specific bootstrap enqueues if we see them, or add a remove_action.
# Since we know `functions.php` enqueues them, let's inject a dequeue logic or just comment them out.

dequeue_logic = """
function tehi_tailwind_cleanup() {
    wp_dequeue_style('bootstrap');
    wp_dequeue_style('bootstrap-css');
    wp_dequeue_script('bootstrap');
    wp_dequeue_script('bootstrap-bundle');
}
add_action('wp_enqueue_scripts', 'tehi_tailwind_cleanup', 999);
"""
if "tehi_tailwind_cleanup" not in functions:
    functions += dequeue_logic

with open("tehi-theme/functions.php", "w", encoding="utf-8") as f:
    f.write(functions)

print("Updated globals!")
