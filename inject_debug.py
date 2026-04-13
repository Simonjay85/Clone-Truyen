import os

path = "tehi-theme/single-chuong.php"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

debug_block = """
<!-- DEBUG PANEL -->
<div style="background:#fff3cd; color:#856404; padding:10px; border:1px solid #ffeeba; margin-bottom:20px; font-family:monospace; font-size:12px; z-index:9999; position:relative;">
    DEBUG INFO:<br>
    Post ID: <?php echo get_the_ID(); ?><br>
    Post Title: <?php the_title(); ?><br>
    Content Length: <?php echo strlen(get_the_content()); ?><br>
    Truyen ID Meta: <?php echo get_post_meta(get_the_ID(), '_truyen_id', true); ?><br>
</div>
"""
# Inject right after get_header()
new_content = content.replace('<?php get_header(); ?>', '<?php get_header(); ?>' + debug_block)

with open(path, "w", encoding="utf-8") as f:
    f.write(new_content)
print(f"✓ Injected Debug Panel into: {path}")
