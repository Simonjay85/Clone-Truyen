import ftplib
try:
    ftp = ftplib.FTP("51.79.53.190")
    ftp.login("alotoinghe", "Nghia234!")
    ftp.cwd("/wp-content/themes/tehi-theme")
    with open("tehi-theme/single-truyen.php", 'rb') as f:
        ftp.storbinary('STOR single-truyen.php', f)
    ftp.quit()
    print("Done!")
except Exception as e:
    print(e)
