import os
import re

theme_path = "tehi-theme"

def clean_content(content):
    # 1. Replace Tehitruyen (mixed case) with name
    content = re.sub(r'Tehitruyen|tehitruyen|TeHiTruyen|TeHi Truyện', 'Đọc Tiểu Thuyết', content)
    
    # 2. Fix the broken URLs introduced by previous scripts
    content = content.replace('https://Đọc Tiểu Thuyết.com', "<?php echo home_url('/'); ?>")
    
    # 3. Handle specific watermark in single-chuong.php
    content = re.sub(r'--text-copyright:\s*\'[^\']+\'', "--text-copyright: 'Đọc Tiểu Thuyết'", content)
    
    # 4. Remove Shopee link specifically
    content = content.replace('https://s.shopee.vn/1BHSFYKG55', "<?php echo home_url('/'); ?>")
    
    # 5. Handle images with Tehi in name or path
    content = re.sub(r'img_data/images/[^"\'>]*TeHi[^"\'>]*\.png', 'assets/images/logo.png', content)
    
    return content

for root, dirs, files in os.walk(theme_path):
    for file in files:
        if file.endswith((".php", ".css", ".js")):
            path = os.path.join(root, file)
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            
            new_content = clean_content(content)
            
            if new_content != content:
                with open(path, "w", encoding="utf-8") as f:
                    f.write(new_content)
                print(f"✓ Surgical Clean: {path}")

print("Surgical cleanup complete.")
