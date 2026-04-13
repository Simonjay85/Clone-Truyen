import re

with open('test_chuong.html', 'r', encoding='utf-8') as f:
    html = f.read()

start_header = html.find('</header>') + 9
end_footer = html.find('<footer class="tm-footer">')

body = html[start_header:end_footer]

# Replace Chapter Title
body = re.sub(r'(<h2 class="mdv-chapter-chuong-title[^>]*>\s*)(.*?)(?=</h2>)', r'\1<?php the_title(); ?>', body, flags=re.DOTALL)

# Replace Chapter Content
body = re.sub(r'(<div id="noi_dung_truyen"[^>]*>\s*)(.*?)(?=</div>\s*</div>)', r'\1<?php the_content(); ?>\n', body, flags=re.DOTALL)

final_php = "<?php get_header(); ?>\n<?php if (have_posts()) : while (have_posts()) : the_post(); ?>\n" + body + "\n<?php endwhile; endif; ?>\n<?php get_footer(); ?>"

with open('tehi-theme/single-chuong.php', 'w', encoding='utf-8') as f:
    f.write(final_php)

print("single-chuong.php generated!")
