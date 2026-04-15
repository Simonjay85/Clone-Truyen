import ftplib

try:
    ftp = ftplib.FTP("51.79.53.190")
    ftp.login("alotoinghe", "Nghia234!")
    
    # Upload Studio PHP
    local1 = "tehi-theme/page-story-studio.php"
    ftp.cwd("/wp-content/themes/tehi-theme/")
    with open(local1, 'rb') as f:
        ftp.storbinary("STOR page-story-studio.php", f)
    print("✓ Upload thành công: page-story-studio.php")
    
    # Upload Functions PHP
    local2 = "tehi-theme/functions.php"
    with open(local2, 'rb') as f:
        ftp.storbinary("STOR functions.php", f)
    print("✓ Upload thành công: functions.php")
    
    ftp.quit()
except Exception as e:
    print("Lỗi:", e)
