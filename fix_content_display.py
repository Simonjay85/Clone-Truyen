import re
import os

path = "tehi-theme/single-chuong.php"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace `the_content()` with echo `get_the_content()` just to bypass WP filters that might be rogue.
# And add a brightly colored DIV so we know if it's there.
replacement = """
                        <div style="color: red !important; font-size: 20px; border: 2px solid red; display:block !important;">
                            <?php echo get_the_content(); ?>
                        </div>
"""
content = re.sub(r'<\?php the_content\(\); \?>', replacement, content)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("Updated single-chuong.php to force get_the_content")
