import os
import ftplib
import glob

# Find all PHP files in tehi-theme
files = glob.glob("tehi-theme/*.php")

old_chaps_logic = "$chaps = wp_count_posts('chuong')->publish;"
new_chaps_logic = "$chapters_arr = get_posts(['post_type' => 'chuong', 'meta_key' => '_truyen_id', 'meta_value' => get_the_ID(), 'posts_per_page' => -1, 'fields' => 'ids']); $chaps = count($chapters_arr);"

modified_files = []

for file_path in files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    if old_chaps_logic in content:
        content = content.replace(old_chaps_logic, new_chaps_logic)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        modified_files.append(file_path)

if modified_files:
    # Upload all files that were modified
    try:
        ftp = ftplib.FTP("51.79.53.190")
        ftp.login("alotoinghe", "Nghia234!")
        
        remote_dir = "/wp-content/themes/tehi-theme"
        try:
            ftp.cwd(remote_dir)
        except:
            pass
            
        for local_file in modified_files:
            filename = os.path.basename(local_file)
            with open(local_file, 'rb') as f:
                ftp.storbinary(f'STOR {filename}', f)
            print(f"Uploaded {filename}")
            
        ftp.quit()
        print("Done uploading accurate chap count fixes.")
    except Exception as e:
        print("Error:", e)
else:
    print("No files matched for replacement")
