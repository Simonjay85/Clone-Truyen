import os
import ftplib
import re

files_to_patch = [
    "tehi-theme/page-latest.php",
    "tehi-theme/search.php",
    "tehi-theme/page-completed.php",
    "tehi-theme/taxonomy-the_loai.php",
    "tehi-theme/page-directory.php",
    "tehi-theme/page-library.php"
]

for file_path in files_to_patch:
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Fix blurry middle thumbnails by upgrading to large
        content = content.replace("get_the_post_thumbnail_url(get_the_ID(), 'medium')", "get_the_post_thumbnail_url(get_the_ID(), 'large')")

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

# Refactor page-completed.php to use the unified landscape card HTML so the weird "Đang cập nhật" author text is removed and it matches the other pages.
comp_path = "tehi-theme/page-completed.php"
with open(comp_path, "r", encoding="utf-8") as f:
    comp_content = f.read()

card_html = """
        <a href="<?php the_permalink(); ?>" class="mkm-card group" style="background:#fff; border-radius:12px; overflow:hidden; box-shadow:0 1px 4px rgba(0,0,0,0.06); display:block; transition:transform 0.2s, box-shadow 0.2s; border: 1px solid #f3f4f6;">
            <div class="mkm-card-img" style="position:relative; aspect-ratio:3/2; overflow:hidden; background:#f9fafb;">
                <span style="position:absolute; top:8px; left:8px; background:#10b981; color:#fff; font-size:10px; font-weight:700; padding:2px 7px; border-radius:6px; z-index:2; box-shadow:0 2px 4px rgba(0,0,0,0.1);">FULL TẬP</span>
                <span style="position:absolute; top:32px; left:8px; background:#111827; color:#fff; font-size:9px; font-weight:700; padding:2px 7px; border-radius:6px; z-index:2;"><?php echo $chaps; ?> Chương</span>
                <img src="<?php echo esc_url($cover); ?>" style="width:100%; height:100%; object-fit:cover; display:block; transition:transform 0.4s;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'"/>
                <div style="position:absolute; bottom:0; left:0; right:0; padding:20px 10px 8px 10px; background:linear-gradient(transparent, rgba(0,0,0,.7)); display:flex; justify-content:space-between; align-items:center; color:#fff; font-size:11px; font-weight:600; z-index:1;">
                    <span style="display:flex;align-items:center;gap:3px;"><svg width="12" height="12" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/><path stroke-linecap="round" stroke-linejoin="round" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/></svg> <?php echo number_format($views); ?></span>
                    <span style="display:flex;align-items:center;gap:3px;color:#fbbf24;"><svg width="12" height="12" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg> 4.9</span>
                </div>
            </div>
            <div style="padding:12px;">
                <p style="font-size:14px; font-weight:700; color:#111827; margin:0 0 8px 0; line-height:1.4; display:-webkit-box; -webkit-line-clamp:2; -webkit-box-orient:vertical; overflow:hidden; font-family: ui-sans-serif, sans-serif;"><?php the_title(); ?></p>
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <span style="background:#f3f4f6; color:#6b7280; font-size:10px; font-weight:600; padding:4px 8px; border-radius:6px;"><?php 
                        $cats = wp_get_post_terms(get_the_ID(), 'the_loai');
                        echo (!is_wp_error($cats) && !empty($cats)) ? esc_html($cats[0]->name) : 'Micro Drama';
                    ?></span>
                    <span style="background:rgba(217, 119, 6, 0.1); color:#d97706; font-size:10px; font-weight:700; padding:4px 8px; border-radius:6px;">Hoàn thành</span>
                </div>
            </div>
        </a>"""

# Replace entirely. The old block is from "<div class=\"group cursor-pointer" up to "</div>\n                </div>"
# Using regex to find the block
comp_content = re.sub(r'<div class="group cursor-pointer.*?</div>\n                </div>', card_html, comp_content, flags=re.DOTALL)

with open(comp_path, "w", encoding="utf-8") as f:
    f.write(comp_content)

# Upload all files that were modified
try:
    ftp = ftplib.FTP("51.79.53.190")
    ftp.login("alotoinghe", "Nghia234!")
    
    remote_dir = "/wp-content/themes/tehi-theme"
    try:
        ftp.cwd(remote_dir)
    except:
        pass
        
    for local_file in files_to_patch:
        if os.path.exists(local_file):
            filename = os.path.basename(local_file)
            with open(local_file, 'rb') as f:
                ftp.storbinary(f'STOR {filename}', f)
            print(f"Uploaded {filename}")
        
    ftp.quit()
    print("Done uploading blurry image and author structure fixes.")
except Exception as e:
    print("Error:", e)
