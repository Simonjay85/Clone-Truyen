import re
import os

path = "tehi-theme/single-chuong.php"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Inject Logic at the top
logic = """
<?php
$truyen_id = get_post_meta(get_the_ID(), '_truyen_id', true);
$parent_story = get_post($truyen_id);
$story_title = $parent_story ? $parent_story->post_title : 'Đọc Tiểu Thuyết';
$story_link = $parent_story ? get_permalink($truyen_id) : home_url('/');

$chapters_query = new WP_Query([
    'post_type' => 'chuong',
    'meta_query' => [['key' => '_truyen_id', 'value' => $truyen_id, 'compare' => '=']],
    'orderby' => 'menu_order date',
    'order' => 'ASC',
    'posts_per_page' => -1
]);
$chapter_posts = $chapters_query->posts;
$chapter_ids = wp_list_pluck($chapter_posts, 'ID');
$current_id = get_the_ID();
$current_index = array_search($current_id, $chapter_ids);

$prev_link = ($current_index > 0) ? get_permalink($chapter_ids[$current_index - 1]) : '#';
$next_link = ($current_index !== false && $current_index < count($chapter_ids) - 1) ? get_permalink($chapter_ids[$current_index + 1]) : '#';

$is_first = ($current_index === 0 || $prev_link === '#');
$is_last = ($current_index === count($chapter_ids) - 1 || $next_link === '#');
?>
"""
content = re.sub(r'(<\?php if \(have_posts\(\)\) : while \(have_posts\(\)\) : the_post\(\); \?>)', r'\1' + logic, content)

# 2. Dynamic Breadcrumbs (find Breadcrumb section)
# Usually has "Trang chủ / ..."
# I'll replace the hardcoded story name with $story_title and $story_link
content = re.sub(r'<a href="[^"]+" class="msv-breadcrumb-link">Trang chủ</a>', r'<a href="<?php echo home_url("/"); ?>" class="msv-breadcrumb-link">Trang chủ</a>', content)
content = re.sub(r'trieu-dinh-khong-dung-nu-nhan-ta-la-ngoai-le\.html', r'<?php echo $story_link; ?>', content)
content = content.replace('Triều Đình Không Dụng Nữ Nhân? Ta Là Ngoại Lệ', '<?php echo $story_title; ?>')

# 3. Dynamic Chapter List (Dropdowns/Sidebars)
# Find the <ul> blocks with msv-chuong-item
# I'll replace the HUGE static list with a dynamic loop
list_pattern = r'<ul class="msv-chuong-list p-0">.*?</ul>'
loop_replacement = """<ul class="msv-chuong-list p-0">
    <?php foreach ($chapter_posts as $chap): 
        $active_class = ($chap->ID == $current_id) ? 'active' : '';
    ?>
        <li class="msv-chuong-item <?php echo $active_class; ?>">
            <a href="<?php echo get_permalink($chap->ID); ?>" class="msv-chuong-link">
                <span class="msv-chuong-title"><?php echo get_the_title($chap->ID); ?></span>
            </a>
        </li>
    <?php endforeach; ?>
</ul>"""
content = re.sub(list_pattern, loop_replacement, content, flags=re.DOTALL)

# Also handle the second list if it exists
list_pattern_2 = r'<ul class="msv-chuong-list mdv-chuong-list-box p-0">.*?</ul>'
content = re.sub(list_pattern_2, loop_replacement.replace('msv-chuong-list', 'msv-chuong-list mdv-chuong-list-box'), content, flags=re.DOTALL)

# 4. Next/Prev Buttons
# Find buttons with "Sau" and "Trước"
# Before
prev_btn_pattern = r'<a href="#" class="mdv-chuong-button mdv-chuong-button-truoc hvr-icon-back disabled" style="pointer-events: none; filter: grayscale\(100%\); background-color: #d3d3d3;">(.*?)</a>'
prev_btn_replacement = """<a href="<?php echo $prev_link; ?>" class="mdv-chuong-button mdv-chuong-button-truoc hvr-icon-back <?php echo $is_first ? 'disabled' : ''; ?>" style="<?php echo $is_first ? 'pointer-events: none; filter: grayscale(100%); background-color: #d3d3d3;' : ''; ?>">
    \\1
</a>"""
content = re.sub(prev_btn_pattern, prev_btn_replacement, content, flags=re.DOTALL)

# After (Sau)
next_btn_pattern = r'<a href="<?php echo home_url\(\'/\'\); ?>\?<?php echo \$story_link; ?>\?chuong=2" class="d-inline-flex mdv-chuong-button mdv-chuong-button-sau hvr-icon-forward " style="">(.*?)</a>'
# Re-trying with a more general pattern since I might have already messed it up with previous edits
next_btn_pattern = r'<a href="[^"]+" class="d-inline-flex mdv-chuong-button mdv-chuong-button-sau hvr-icon-forward\s*"[^>]*>(.*?)</a>'
next_btn_replacement = """<a href="<?php echo $next_link; ?>" class="d-inline-flex mdv-chuong-button mdv-chuong-button-sau hvr-icon-forward <?php echo $is_last ? 'disabled' : ''; ?>" style="<?php echo $is_last ? 'pointer-events: none; filter: grayscale(100%); background-color: #d3d3d3;' : ''; ?>">
    \\1
</a>"""
content = re.sub(next_btn_pattern, next_btn_replacement, content, flags=re.DOTALL)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print(f"✓ Dynamically refactored: {path}")
