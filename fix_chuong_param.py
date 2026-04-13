import re

with open("tehi-theme/front-page.php", "r", encoding="utf-8") as f:
    code = f.read()

# Replace ?chuong=1 with actual link logic in front-page.php's Hero Slider
# The loop in front-page.php Hero slider starts around line 13:
# $hero_q = new WP_Query($hero_args);
# We need to inject the $first_chap_q logic inside the loop, and then replace ?chuong=1

replacement_logic = """$cover = get_the_post_thumbnail_url(get_the_ID(), 'large') ?: get_post_meta(get_the_ID(), '_cover_image', true);
        $excerpt = wp_trim_words(get_the_excerpt() ?: get_the_content(), 30);
        
        $first_chap_q = new WP_Query(['post_type'=>'chuong','posts_per_page'=>1,'meta_query'=>[['key'=>'_truyen_id','value'=>get_the_ID(),'compare'=>'=']],'orderby'=>'date','order'=>'ASC']);
        $first_chap_link = $first_chap_q->have_posts() ? get_permalink($first_chap_q->posts[0]->ID) : '#';
        wp_reset_postdata();"""

code = re.sub(
    r"\$cover = get_the_post_thumbnail_url\(get_the_ID\(\), 'large'\).*?\$excerpt = wp_trim_words\(get_the_excerpt\(\) \?: get_the_content\(\), 30\);",
    replacement_logic,
    code,
    flags=re.DOTALL
)

code = code.replace('href="<?php the_permalink(); ?>?chuong=1"', 'href="<?php echo $first_chap_link; ?>"')

# Also check Editor's Choice section if they have "Đọc ngay"
# "<a href="<?php the_permalink(); ?>" class="inline-flex bg-white text-primary ... Đọc ngay"
# They currently link to the_permalink() which is fine (Story Details). But wait, do they say "Đọc ngay"?
# If so, maybe they should link to the first chapter or just stay on single-truyen.php. The user click on them is fine.

with open("tehi-theme/front-page.php", "w", encoding="utf-8") as f:
    f.write(code)

print("Fixed front-page.php!")
