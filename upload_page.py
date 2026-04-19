import ftplib
import os

local_file = "tehi-theme/page.php"

try:
    ftp = ftplib.FTP("51.79.53.190")
    ftp.login("alotoinghe", "Nghia234!")
    
    remote_dir = "/wp-content/themes/tehi-theme"
    try:
        ftp.cwd(remote_dir)
    except:
        pass
        
    with open(local_file, 'rb') as f:
        ftp.storbinary('STOR page.php', f)
    print("Done uploading page.php")
    ftp.quit()
except Exception as e:
    print("Error:", e)
