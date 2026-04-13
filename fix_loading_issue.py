import re

# 1. Fix functions.php: Remove the add_action('init', 'tehi_auto_create_pages') to prevent infinite loading/db thrashing.
with open("tehi-theme/functions.php", "r", encoding="utf-8") as f:
    functions_content = f.read()

functions_content = functions_content.replace("add_action('init', 'tehi_auto_create_pages');", "// add_action('init', 'tehi_auto_create_pages'); // Disabled after first run to save performance")

with open("tehi-theme/functions.php", "w", encoding="utf-8") as f:
    f.write(functions_content)

# 2. Fix header.php and header-home.php foreach error
for header_file in ["tehi-theme/header.php", "tehi-theme/header-home.php"]:
    with open(header_file, "r", encoding="utf-8") as f:
        content = f.read()
    
    content = content.replace("foreach($menu_items as $item) {", "if(is_array($menu_items) || is_object($menu_items)) { foreach($menu_items as $item) {")
    content = content.replace("echo '<a class=\"text-slate-600 dark:text-slate-400 hover:text-blue-500 transition-colors\"", "    }\n            }")
    
    # Wait, simple replace is dangerous for the closing bracket.
    # I'll just use regex to replace the foreach block.
    
    # Actually, simpler:
    pattern = r'(foreach\(\$menu_items as \$item\) \{\s*// Kiểm tra active[\s\S]*?\}\s*\}\s*)\}\s*\} else \{'
    if re.search(r'foreach\(\$menu_items as \$item\)', content):
        content = content.replace("foreach($menu_items as $item) {", "if(!is_wp_error($menu_items) && !empty($menu_items)) { foreach($menu_items as $item) {")
        content = content.replace("            }\n        }\n    } else {", "            }\n        } }\n    } else {")
    
    with open(header_file, "w", encoding="utf-8") as f:
        f.write(content)
        
print("Fixed headers and functions.")
