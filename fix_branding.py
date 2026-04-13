content = """
/**
 * Force site title to "Đọc Tiểu Thuyết"
 */
function tehi_clone_custom_title($title) {
    return 'Đọc Tiểu Thuyết';
}
add_filter('pre_get_document_title', 'tehi_clone_custom_title', 999);
"""
filename = "tehi-theme/functions.php"
with open(filename, "a") as f:
    f.write(content)
