import re
import os

path = "tehi-theme/single-chuong.php"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Remove hidden-content class from the main div
content = content.replace('<div id="noi_dung_truyen" class="hidden-content">', '<div id="noi_dung_truyen" class="<?php echo get_option("tehi_aff_enabled") ? "hidden-content" : ""; ?>">')

# 2. Fix the Share Modal Error in footer.php (separate file)
# 3. Handle banner path in footer.php

with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print(f"✓ Fixed visibility logic in: {path}")

# --- FOOTER FIXES ---
footer_path = "tehi-theme/footer.php"
with open(footer_path, "r", encoding="utf-8") as f:
    footer_content = f.read()

# Add a dummy shareModal if it's missing to satisfy share-modal.js
if 'id="shareModal"' not in footer_content:
    footer_content = footer_content.replace('</body>', '<div id="shareModal" style="display:none;"></div>\n</body>')

# Replace the broken placeholder banner with a safe path
footer_content = footer_content.replace('img_data/images/banner-placeholder.png', 'assets/images/logo.png')

with open(footer_path, "w", encoding="utf-8") as f:
    f.write(footer_content)
print(f"✓ Fixed footer placeholders and scripts in: {footer_path}")
