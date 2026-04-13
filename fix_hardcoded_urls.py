import re
import os

files = ["tehi-theme/single-truyen.php", "tehi-theme/single-chuong.php"]
target_domain = "https://tehitruyen.com/"
replacement = "<?php echo home_url('/'); ?>"

for file_path in files:
    if not os.path.exists(file_path):
        continue
    with open(file_path, "r") as f:
        content = f.read()
    
    # Replace the domain with home_url()
    # Be careful not to replace static assets that might actually exist on tehitruyen and we want to fallback to (like images)
    # Actually, for images, it's better to keep them as is for now if they are on the CDN, but for page links, we MUST change them.
    
    # Replace all .html links to tehitruyen with home_url()
    content = content.replace(target_domain, "<?php echo home_url('/'); ?>")
    
    # Fix the double slash if any
    content = content.replace("home_url('/'); ?>/", "home_url('/'); ?>")
    
    with open(file_path, "w") as f:
        f.write(content)

print("Replacement complete.")
