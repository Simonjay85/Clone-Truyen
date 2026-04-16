import ftplib
import os

try:
    ftp = ftplib.FTP("51.79.53.190")
    ftp.login("alotoinghe", "Nghia234!")
    
    ftp.cwd("/wp-content/themes/tehi-theme/")
    
    with open("tehi-theme/page-story-studio.php", 'rb') as f:
        ftp.storbinary("STOR page-story-studio.php", f)
        
    with open("tehi-theme/single-truyen.php", 'rb') as f:
        ftp.storbinary("STOR single-truyen.php", f)
        
    print(f"✓ Upload thành công page-story-studio.php và single-truyen.php")
    ftp.quit()

except Exception as e:
    print("Lỗi:", e)
