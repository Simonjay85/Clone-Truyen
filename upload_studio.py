import ftplib

try:
    ftp = ftplib.FTP("51.79.53.190")
    ftp.login("alotoinghe", "Nghia234!")
    
    local = "tehi-theme/page-story-studio.php"
    remote = "/wp-content/themes/tehi-theme/page-story-studio.php"
    
    ftp.cwd("/wp-content/themes/tehi-theme")
    with open(local, 'rb') as f:
        ftp.storbinary("STOR page-story-studio.php", f)
    print(f"✓ Upload thành công: {remote}")
    
    ftp.quit()
except Exception as e:
    print("Lỗi:", e)
