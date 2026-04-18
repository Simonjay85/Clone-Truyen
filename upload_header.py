import ftplib

try:
    ftp = ftplib.FTP("51.79.53.190")
    ftp.login("alotoinghe", "Nghia234!")
    ftp.cwd("/wp-content/themes/tehi-theme/")
    with open("tehi-theme/header.php", 'rb') as f:
        ftp.storbinary("STOR header.php", f)
    print("✓ Upload thành công header.php")
    ftp.quit()
except Exception as e:
    print("Lỗi:", e)
