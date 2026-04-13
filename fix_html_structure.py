import re
import os

path = "tehi-theme/single-chuong.php"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Remove Debug Block
content = re.sub(r'<!-- DEBUG PANEL -->.*?</div>\s*', '', content, flags=re.DOTALL)

# 2. Fix the unclosed span and hardcoded "Chương 1:"
bad_title = '<span class="mdv-san-pham-detail-chuong-title-label"><span class="mdv-san-pham-detail-chuong-title-text">Chương 1:</span>'
good_title = '<span class="mdv-san-pham-detail-chuong-title-label"><span class="mdv-san-pham-detail-chuong-title-text"><?php the_title(); ?>:</span></span>'
content = content.replace(bad_title, good_title)

# Also fix the Breadcrumb link:
content = content.replace('?chuong=1"><?php the_title(); ?></a>', '"><?php the_title(); ?></a>')

# 3. Fix the PREV button (Trước) which was missed
bad_prev = '<a href="#" class="d-inline-flex  mdv-chuong-button mdv-chuong-button-truoc hvr-icon-back disabled" style="pointer-events: none; filter: grayscale(100%); background-color: #d3d3d3;">'
good_prev = '<a href="<?php echo $prev_link; ?>" class="d-inline-flex mdv-chuong-button mdv-chuong-button-truoc hvr-icon-back <?php echo $is_first ? \'disabled\' : \'\'; ?>" style="<?php echo $is_first ? \'pointer-events: none; filter: grayscale(100%); background-color: #d3d3d3;\' : \'\'; ?>">'
content = content.replace(bad_prev, good_prev)

# 4. Fix the middle CHƯƠNG 1 button
content = content.replace('<span class="mdv-chuong-button-text">Chương 1</span>', '<span class="mdv-chuong-button-text"><?php the_title(); ?></span>')

# 5. Remove the red div from the_content
red_div = """                        <div style="color: red !important; font-size: 20px; border: 2px solid red; display:block !important;">
                            <?php echo get_the_content(); ?>
                        </div>"""
normal_content = "                        <?php the_content(); ?>"
content = content.replace(red_div, normal_content)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("✓ Fixed unclosed HTML tags and remaining hardcoded text")
