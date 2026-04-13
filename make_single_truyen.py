import re

with open('test_novel.html', 'r', encoding='utf-8') as f:
    html = f.read()

start_header = html.find('</header>') + 9
end_footer = html.find('<footer class="tm-footer">')

body = html[start_header:end_footer]

# Replace Title
body = re.sub(r'(<div class="mdv-san-pham-show-name[^>]*>\s*)(.*?)(?=</div>)', r'\1<?php the_title(); ?>', body, flags=re.DOTALL)

# Replace Intro
body = re.sub(r'(<div class="mdv-san-pham-show-gioi-thieu[^>]*>\s*)(.*?)(?=<div class="bee-gioi-thieu-truyen-xem-them-gradient")', r'\1<?php the_content(); ?>\n', body, flags=re.DOTALL)

# Remove the hardcoded chapters list and replace with a WP query for chapters
chapter_loop = """
<div class="row row-cols-1 row-cols-lg-2">
<?php
$truyen_id = get_the_ID();
$chapters = new WP_Query(array(
    'post_type'      => 'chuong',
    'meta_query'     => array(
        array(
            'key'   => '_truyen_id',
            'value' => $truyen_id
        )
    ),
    'posts_per_page' => -1,
    'order'          => 'ASC'
));
if ($chapters->have_posts()) :
    while ($chapters->have_posts()) : $chapters->the_post();
?>
    <div class="col">
        <div class="mdv-san-pham-show-dsc-table-chuong-box d-flex flex-column align-items-center">
            <div class="mdv-san-pham-show-dsc-table-chuong text-truncate" style="max-width: 100%;">
                <a href="<?php the_permalink(); ?>"><?php the_title(); ?></a>
            </div>
        </div>
    </div>
<?php
    endwhile;
    wp_reset_postdata();
else :
    echo "<p>Truyện này chưa có chương nào.</p>";
endif;
?>
</div>
"""
# Replace the whole <div class="row row-cols-1 row-cols-lg-2"> inside chapter list area
# But the regex might be tricky. Let's just find the container:
import sys
if '<div class="row row-cols-1 row-cols-lg-2">' in body:
    idx_start = body.find('<div class="row row-cols-1 row-cols-lg-2">')
    idx_end = body.find('<!-- ds start end -->')
    if idx_end != -1:
        body = body[:idx_start] + chapter_loop + body[idx_end:]

final_php = "<?php get_header(); ?>\n<?php if (have_posts()) : while (have_posts()) : the_post(); ?>\n" + body + "\n<?php endwhile; endif; ?>\n<?php get_footer(); ?>"

with open('tehi-theme/single-truyen.php', 'w', encoding='utf-8') as f:
    f.write(final_php)

print("single-truyen.php generated!")
