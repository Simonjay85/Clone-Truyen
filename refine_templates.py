import re
import os

files = ["tehi-theme/single-chuong.php", "tehi-theme/single-truyen.php"]

for file_path in files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Replace affiliate link with constant
    content = content.replace('href="<?php echo home_url(\'/\'); ?>"', 'href="<?php echo THEME_AFFILIATE_URL; ?>"')
    
    # Replace watermark text with constant
    content = re.sub(r'--text-copyright:\s*\'[^\']+\'', "--text-copyright: '<?php echo THEME_WATERMARK_TEXT; ?>'", content)
    
    # Replace branding images with a clean logo.png path
    content = re.sub(r'img_data/images/logo-[^.]+\.png', 'assets/images/logo.png', content)
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

print("Template refinement complete.")
