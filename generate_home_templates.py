import re
import os

code_path = "/Users/aaronnguyen/Downloads/stitch (3)/code.html"
with open(code_path, "r", encoding="utf-8") as f:
    html = f.read()

# EXTRAT HEAD AND NAV -> header-home.php
head_match = re.search(r'(<!DOCTYPE html>.*?</nav>)', html, re.DOTALL)
header_content = head_match.group(1)

# Modify header_content dynamically for WordPress
header_content = header_content.replace('href="#"', 'href="<?php echo home_url(\'/\'); ?>"')
header_content = header_content.replace('tehitruyen.com', '<?php bloginfo("name"); ?>')
header_content += "\n<?php wp_head(); ?>\n"

with open("tehi-theme/header-home.php", "w", encoding="utf-8") as f:
    f.write(header_content)


# EXTRACT FOOTER -> footer-home.php
footer_match = re.search(r'(<footer.*?>.*?</footer>)', html, re.DOTALL)
footer_content = footer_match.group(1)

# Modify footer dynamically
footer_content = footer_content.replace('tehitruyen.com', '<?php bloginfo("name"); ?>')
footer_content += "\n<?php wp_footer(); ?>\n</body></html>"

with open("tehi-theme/footer-home.php", "w", encoding="utf-8") as f:
    f.write(footer_content)


# EXTRACT MAIN -> front-page.php
main_match = re.search(r'(<main.*?>.*?</main>)', html, re.DOTALL)
main_content = main_match.group(1)

front_page_php = "<?php\n/* Template Name: Home Page */\nget_header('home');\n?>\n\n"
front_page_php += main_content
front_page_php += "\n\n<?php get_footer('home'); ?>\n"

with open("tehi-theme/front-page.php", "w", encoding="utf-8") as f:
    f.write(front_page_php)

print("Created header-home.php, footer-home.php, and front-page.php")
