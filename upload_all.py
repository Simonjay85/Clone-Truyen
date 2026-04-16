import ftplib

try:
    ftp = ftplib.FTP("51.79.53.190")
    ftp.login("alotoinghe", "Nghia234!")
    
    with open("tehi-theme/functions.php", 'rb') as f:
        ftp.storbinary("STOR /wp-content/themes/tehi-theme/functions.php", f)
        
    with open("tehi-theme/page-story-studio.php", 'rb') as f:
        ftp.storbinary("STOR /wp-content/themes/tehi-theme/page-story-studio.php", f)
        
    print("✓ Upload thành công 2 tệp!")
    ftp.quit()
except Exception as e:
    print("Lỗi:", e)
