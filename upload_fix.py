import ftplib
import os
import requests

try:
    ftp = ftplib.FTP("51.79.53.190")
    ftp.login("alotoinghe", "Nghia234!")
    
    local_func = "tehi-theme/fix_chapters.php"
    ftp.cwd("/wp-content/themes/tehi-theme/")
    with open(local_func, 'rb') as f:
        ftp.storbinary("STOR fix_chapters.php", f)
    print(f"✓ Upload thành công")
    
    ftp.quit()

    response = requests.get("https://doctieuthuyet.com/wp-content/themes/tehi-theme/fix_chapters.php")
    print(response.text)

    # Clean up locally
    os.remove("upload_fix.py")
    os.remove("tehi-theme/fix_chapters.php")

except Exception as e:
    print("Lỗi:", e)
