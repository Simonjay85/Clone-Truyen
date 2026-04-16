import ftplib

try:
    ftp = ftplib.FTP("51.79.53.190")
    ftp.login("alotoinghe", "Nghia234!")
    
    ftp.cwd("/wp-content/themes/tehi-theme/")
    
    with open("tehi-theme/functions.php", 'rb') as f:
        ftp.storbinary("STOR functions.php", f)
        
    print("✓ Upload functions.php thành công!")
    ftp.quit()
except Exception as e:
    print("Lỗi:", e)
