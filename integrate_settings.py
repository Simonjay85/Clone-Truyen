import re
import os

def update_file(path, replacements):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    new_content = content
    for target, subst in replacements.items():
        new_content = new_content.replace(target, subst)
        
    if new_content != content:
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"✓ Integrated settings into: {path}")

# 1. Update single-chuong.php
replacements_chuong = {
    # Affiliate Modal Wrapper
    '<?php if (TRUE): // logic placeholder ?>': '<?php if ( get_option("tehi_aff_enabled") ): ?>',
    '<?php if (TRUE): ?>': '<?php if ( get_option("tehi_aff_enabled") ): ?>',
    '<div id="affiliate-notification" class="affiliate-notification">': '<?php if ( get_option("tehi_aff_enabled") ): ?>\n<div id="affiliate-notification" class="affiliate-notification">',
    '<?php endwhile; endif; ?>': '<?php endif; // End tehi_aff_enabled ?>\n<?php endwhile; endif; ?>',
    
    # Dynamic Link
    'href="<?php echo THEME_AFFILIATE_URL; ?>"': 'href="<?php echo esc_url(get_option("tehi_aff_url", home_url("/"))); ?>"',
    
    # AdSense Dynamic
    'data-ad-client="ca-pub-2935799637584410"': 'data-ad-client="<?php echo esc_attr(get_option("tehi_ads_client", "ca-pub-2935799637584410")); ?>"',
    'data-ad-slot="8234900970"': 'data-ad-slot="<?php echo esc_attr(get_option("tehi_ads_slot_chuong", "8234900970")); ?>"'
}

# The grep result earlier showed the notification div at line 217.
# I'll manually check and do a safer regex-based replacement if needed, 
# but let's try the direct string first.

# 2. Update single-truyen.php
replacements_truyen = {
    'data-ad-client="ca-pub-2935799637584410"': 'data-ad-client="<?php echo esc_attr(get_option("tehi_ads_client", "ca-pub-2935799637584410")); ?>"',
    'data-ad-slot="8234900970"': 'data-ad-slot="<?php echo esc_attr(get_option("tehi_ads_slot_truyen", "8234900970")); ?>"'
}

update_file("tehi-theme/single-chuong.php", replacements_chuong)
update_file("tehi-theme/single-truyen.php", replacements_truyen)
