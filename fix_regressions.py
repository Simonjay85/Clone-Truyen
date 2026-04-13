import re
import os

path = "tehi-theme/single-chuong.php"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Force show content if affiliate is off
content = content.replace('class="<?php echo get_option("tehi_aff_enabled") ? "hidden-content" : ""; ?>">', 'class="<?php echo (get_option("tehi_aff_enabled") && !is_user_logged_in()) ? "hidden-content" : ""; ?>">')
# Actually, let's just make it simpler for aaron: 
content = content.replace('hidden-content', '') # Emergency: remove hidden class entirely for now to guarantee visibility

# 2. Fix dynamic breadcrumb title (current chapter)
content = re.sub(r'Chương 1</a></li>', r'<?php the_title(); ?></a></li>', content)

# 3. Dynamic story title in breadcrumb (ensure it uses $story_title)
content = content.replace('Triều Đình Không Dung Nữ Nhân? Ta Là Ngoại Lệ', '<?php echo $story_title; ?>')

# 4. Fix Chapter List Dropdown text (show current chapter name instead of "Chương 1")
content = re.sub(r'<span class="mdv-chuong-button-text"> Chương 1</span>', r'<span class="mdv-chuong-button-text"> <?php the_title(); ?></span>', content)

# 5. Fix JS Handlers - ensure they are correctly scoped and work for ALL buttons
# Find the JS block for timChuongBtn
js_fix = """
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
# Replace the redundant individual handlers with the combined one
content = re.sub(r'// Khi nhấn vào nút "Tìm chương" - cho #timChuongBtn.*?// Đóng danh sách chương khi nhấn ngoài khu vực.*?\r?\n\s+\}\);', js_fix, content, flags=re.DOTALL)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print(f"✓ Fixed regressions in: {path}")
