import os
import re

theme_path = "tehi-theme"
replacements = {
    r"(?i)tehitruyen": "Đọc Tiểu Thuyết",
    r"(?i)tehi truyen": "Đọc Tiểu Thuyết",
    r"(?i)tehi clone": "Đọc Tiểu Thuyết Theme",
    "https://s.shopee.vn/1BHSFYKG55": "<?php echo home_url('/'); ?>", # Default to homepage for now
    "Độc quyền tại Tehitruyen": "Đọc Tiểu Thuyết",
    "logo-tehitruyen-v1-nen_anh.png": "logo.png",
    "Me_Zhihu_-_O_nha_be_Chanh_TeHi_Truyen_1.png": "banner-placeholder.png"
}

for root, dirs, files in os.walk(theme_path):
    for file in files:
        if file.endswith((".php", ".css", ".js")):
            file_path = os.path.join(root, file)
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            
            new_content = content
            for pattern, subst in replacements.items():
                if pattern.startswith("(?i)"):
                    new_content = re.sub(pattern, subst, new_content)
                else:
                    new_content = new_content.replace(pattern, subst)
            
            # Additional logic for fonts
            new_content = new_content.replace("font-family: lato-black;", "font-family: 'Outfit', sans-serif;")
            new_content = new_content.replace("lato-black", "Outfit")
            
            if new_content != content:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(new_content)
                print(f"✓ Cleaned: {file_path}")

print("Global cleanup complete.")
