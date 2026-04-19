import os
import ftplib
import re

files_to_patch = [
    "tehi-theme/page-directory.php",
    "tehi-theme/taxonomy-the_loai.php"
]

# For taxonomy and directory (which currently use .mkm-card custom CSS):
card_html = """
        <a href="<?php the_permalink(); ?>" class="mkm-card group" style="background:#fff; border-radius:12px; overflow:hidden; box-shadow:0 1px 4px rgba(0,0,0,0.06); display:block; transition:transform 0.2s, box-shadow 0.2s; border: 1px solid #f3f4f6;">
            <div class="mkm-card-img" style="position:relative; aspect-ratio:3/2; overflow:hidden; background:#f9fafb;">
                <span style="position:absolute; top:8px; left:8px; background:#10b981; color:#fff; font-size:10px; font-weight:700; padding:2px 7px; border-radius:6px; z-index:2; box-shadow:0 2px 4px rgba(0,0,0,0.1);">Ch.<?php echo $chaps; ?></span>
                <img src="<?php echo esc_url($cover); ?>" style="width:100%; height:100%; object-fit:cover; display:block; transition:transform 0.4s;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'"/>
                <div style="position:absolute; bottom:0; left:0; right:0; padding:20px 10px 8px 10px; background:linear-gradient(transparent, rgba(0,0,0,.7)); display:flex; justify-content:space-between; align-items:center; color:#fff; font-size:11px; font-weight:600; z-index:1;">
                    <span style="display:flex;align-items:center;gap:3px;"><svg width="12" height="12" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/><path stroke-linecap="round" stroke-linejoin="round" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/></svg> <?php echo $formatted_views; ?></span>
                    <span style="display:flex;align-items:center;gap:3px;color:#fbbf24;"><svg width="12" height="12" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/></svg> 2 giờ trước</span>
                </div>
            </div>
            <div style="padding:12px;">
                <p style="font-size:14px; font-weight:700; color:#111827; margin:0 0 8px 0; line-height:1.4; display:-webkit-box; -webkit-line-clamp:2; -webkit-box-orient:vertical; overflow:hidden; font-family: ui-sans-serif, sans-serif;"><?php the_title(); ?></p>
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <span style="background:#f3f4f6; color:#6b7280; font-size:10px; font-weight:600; padding:4px 8px; border-radius:6px;"><?php echo esc_html($term_name_display); ?></span>
                    <span style="background:rgba(217, 119, 6, 0.1); color:#d97706; font-size:10px; font-weight:700; padding:4px 8px; border-radius:6px;">Chi tiết</span>
                </div>
            </div>
        </a>"""

for file_path in files_to_patch:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # We replace the whole <a href="..."> block for the card
    new_content = re.sub(r'<a href="<\?php the_permalink\(\); \?>" class="mkm-card">.*?</a>', card_html, content, flags=re.DOTALL)
    
    # We also update the grid column count to look better with landscape images!
    # Instead of repeat(4, 1fr) we probably want repeat(3, 1fr) so landscape isn't too tiny
    new_content = new_content.replace('grid-template-columns: repeat(4, 1fr) !important;', 'grid-template-columns: repeat(3, 1fr) !important;')
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)


# For page-completed.php, it uses a different structural template, so fix it separately:
comp_path = "tehi-theme/page-completed.php"
with open(comp_path, "r", encoding="utf-8") as f:
    comp_content = f.read()

# Replace the specific card structure in page-completed.php
comp_old = """<div class="relative rounded-xl overflow-hidden mb-3 bg-surface-container-high shadow-inner" style="aspect-ratio: 3/4;">"""
comp_new = """<div class="relative rounded-xl overflow-hidden mb-3 bg-surface-container-high shadow-inner" style="aspect-ratio: 3/2;">"""
comp_content = comp_content.replace(comp_old, comp_new)

# Also update the grid class on completed to 3 cols instead of 4 so landscape looks good
comp_content = comp_content.replace('grid-cols-2 md:grid-cols-3 xl:grid-cols-4', 'grid-cols-1 sm:grid-cols-2 md:grid-cols-3')

with open(comp_path, "w", encoding="utf-8") as f:
    f.write(comp_content)


files_to_upload = files_to_patch + [comp_path]

# FTP Upload
try:
    ftp = ftplib.FTP("51.79.53.190")
    ftp.login("alotoinghe", "Nghia234!")
    
    remote_dir = "/wp-content/themes/tehi-theme"
    try:
        ftp.cwd(remote_dir)
    except:
        pass
        
    for local_file in files_to_upload:
        filename = os.path.basename(local_file)
        with open(local_file, 'rb') as f:
            ftp.storbinary(f'STOR {filename}', f)
        print(f"Uploaded {filename}")
        
    ftp.quit()
    print("Done uploading landscape aspect ratio fixes.")
except Exception as e:
    print("Error:", e)
