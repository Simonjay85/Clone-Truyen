import re
import os

# --- 1. Fix Fonts in style.css ---
css_path = "tehi-theme/style.css"
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()
# Replace local font-face with Google Font import
css = "@import url('https://fonts.googleapis.com/css2?family=Lato:wght@300;400;700;900&display=swap');\n" + css
css = re.sub(r'@font-face\s*\{.*?\}', '', css, flags=re.DOTALL)
css = css.replace("font-family: 'Arial', sans-serif;", "font-family: 'Lato', sans-serif;")
with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)
print(f"✓ Fixed fonts in: {css_path}")

# --- 2. Fix JS in single-chuong.php ---
chuong_path = "tehi-theme/single-chuong.php"
with open(chuong_path, "r", encoding="utf-8") as f:
    chuong = f.read()

# Fix duplicates and syntax
# Remove the first redundant block if it's identical to the second
double_js = """
        // Toggles cho danh sách chương
        $('#timChuongBtn, #timChuongBtn2').on('click', function(e) {
            e.preventDefault();
            const target = $(this).attr('id') === 'timChuongBtn' ? '#chuongList' : '#chuongList2';
            $(target).slideToggle(300);
        });

        $(document).on('click', function(event) {
            if (!$(event.target).closest('#timChuongBtn, #chuongList').length) $('#chuongList').slideUp(300);
            if (!$(event.target).closest('#timChuongBtn2, #chuongList2').length) $('#chuongList2').slideUp(300);
        });
"""
# If it appears twice, replace the combined block with one instance
if chuong.count(double_js.strip()) > 1:
    chuong = chuong.replace(double_js.strip(), "", 1) # remove one instance

with open(chuong_path, "w", encoding="utf-8") as f:
    f.write(chuong)
print(f"✓ Fixed JS duplicate in: {chuong_path}")

# --- 3. Fix Footer (Share Modal & Logo) ---
footer_path = "tehi-theme/footer.php"
with open(footer_path, "r", encoding="utf-8") as f:
    footer = f.read()

# Better Dummy Share Modal
modal_full = """<div id="shareModal" class="modal fade" tabindex="-1" aria-hidden="true" style="display:none;">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="fb-share-button" data-href=""></div>
            <button class="btn-close" data-bs-dismiss="modal"></button>
        </div>
    </div>
</div>"""
footer = re.sub(r'<div id="shareModal".*?</div>', modal_full, footer)

# Fix logo.png 404 to use a data URI or just remove if failing
# I'll use a blank 1x1 png data URI to prevent 404s
blank_png = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8/5+hHgAHggJ/PchI7wAAAABJRU5ErkJggg=="
footer = footer.replace('/assets/images/logo.png', blank_png)

with open(footer_path, "w", encoding="utf-8") as f:
    f.write(footer)
print(f"✓ Fixed footer modal and logo in: {footer_path}")

# --- 4. Fix Header Logo ---
header_path = "tehi-theme/header.php"
with open(header_path, "r", encoding="utf-8") as f:
    header = f.read()
header = header.replace('/assets/images/logo.png', blank_png)
with open(header_path, "w", encoding="utf-8") as f:
    f.write(header)
print(f"✓ Fixed header logo in: {header_path}")
