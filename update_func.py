import ftplib
import urllib.request

try:
    ftp = ftplib.FTP("51.79.53.190")
    ftp.login("alotoinghe", "Nghia234!")
    
    ftp.cwd("/wp-content/themes/tehi-theme/")
    
    with open("tehi-theme/functions.php", 'rb') as f:
        ftp.storbinary("STOR functions.php", f)
        
    print(f"✓ Upload thành công functions.php")
    ftp.quit()

except Exception as e:
    print("Lỗi:", e)
