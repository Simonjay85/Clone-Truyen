import os
import ftplib

file_path = "tehi-theme/front-page.php"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace the single line truncate with dual line clamp for Bảng xếp hạng titles
old_style = "white-space:nowrap; overflow:hidden; text-overflow:ellipsis;"
new_style = "display:-webkit-box; -webkit-line-clamp:2; -webkit-box-orient:vertical; overflow:hidden; line-height:1.3; margin-bottom:6px;"

content = content.replace(old_style, new_style)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

# FTP Upload
try:
    ftp = ftplib.FTP("51.79.53.190")
    ftp.login("alotoinghe", "Nghia234!")
    
    remote_dir = "/wp-content/themes/tehi-theme"
    try:
        ftp.cwd(remote_dir)
    except:
        pass
        
    filename = os.path.basename(file_path)
    with open(file_path, 'rb') as f:
        ftp.storbinary(f'STOR {filename}', f)
    print(f"Uploaded {filename}")
        
    ftp.quit()
    print("Done uploading title multi-line fix.")
except Exception as e:
    print("Error:", e)
