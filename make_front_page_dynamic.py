import re
import os

path = "tehi-theme/front-page.php"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Hero Slider (Trending Now)
# Find the slide container
# <div class="min-w-full relative h-full"> ... </div>
hero_pattern = re.compile(r'(<div class="min-w-full relative h-full">.*?)(</div>\s*</div>\s*<!-- Slider Navigation -->)', re.DOTALL)
hero_match = hero_pattern.search(content)

if hero_match:
    slider_html = hero_match.group(1)
    
    # We will replace the static slide with a WP_Query loop
    hero_php = """
    <?php
    $hero_args = ['post_type' => 'truyen', 'posts_per_page' => 4, 'meta_key' => '_views', 'orderby' => 'meta_value_num', 'order' => 'DESC'];
    $hero_q = new WP_Query($hero_args);
    if($hero_q->have_posts()): while($hero_q->have_posts()): $hero_q->the_post();
        $cover = get_the_post_thumbnail_url(get_the_ID(), 'large') ?: get_post_meta(get_the_ID(), '_cover_image', true);
        $excerpt = wp_trim_words(get_the_excerpt() ?: get_the_content(), 30);
    ?>
    <div class="min-w-full relative h-full flex-shrink-0">
        <img class="absolute inset-0 w-full h-full object-cover" src="<?php echo esc_url($cover); ?>" />
        <div class="absolute inset-0 bg-gradient-to-r from-black/90 via-black/60 to-transparent"></div>
        <div class="absolute inset-y-0 left-0 flex flex-col justify-center px-12 md:px-20 max-w-3xl z-10">
            <div class="flex gap-2 mb-4">
                <span class="bg-blue-600 text-white text-[10px] font-bold px-3 py-1 rounded-full uppercase tracking-widest">Trending Now</span>
            </div>
            <h1 class="text-5xl md:text-7xl font-extrabold text-white leading-tight mb-6"><?php the_title(); ?></h1>
            <p class="text-white/80 text-lg md:text-xl mb-10 line-clamp-3 leading-relaxed"><?php echo $excerpt; ?></p>
            <div class="flex items-center gap-6">
                <a href="<?php the_permalink(); ?>?chuong=1" class="bg-primary hover:bg-primary/90 text-white font-bold px-10 py-4 rounded-full shadow-xl shadow-primary/20 transition-all flex items-center gap-2 text-lg">
                    Đọc ngay <span class="material-symbols-outlined">auto_stories</span>
                </a>
                <a href="<?php the_permalink(); ?>" class="bg-white/10 hover:bg-white/20 backdrop-blur-md text-white font-bold px-10 py-4 rounded-full border border-white/20 transition-all text-lg">
                    Chi tiết
                </a>
            </div>
        </div>
    </div>
    <?php endwhile; wp_reset_postdata(); endif; ?>
    """
    content = content.replace(slider_html, hero_php)


# Add Javascript for slider
js_addon = """
<script>
document.addEventListener('DOMContentLoaded', function() {
    const sliderContainer = document.querySelector('.mb-12 > div.flex');
    const slides = document.querySelectorAll('.min-w-full');
    const prevBtn = document.querySelector('button .material-symbols-outlined:contains("arrow_back")').parentElement;
    const nextBtn = document.querySelector('button .material-symbols-outlined:contains("arrow_forward")').parentElement;
    
    let currentSlide = 0;
    
    function updateSlider() {
        if(!sliderContainer) return;
        sliderContainer.style.transform = `translateX(-${currentSlide * 100}%)`;
    }
    
    // We will hook this up later, simple for now
});
</script>
"""

with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("Hero slider dynamicized!")
