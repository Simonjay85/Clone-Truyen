import ftplib
ftp = ftplib.FTP("51.79.53.190")
ftp.login("alotoinghe", "Nghia234!")
with open('tehi-theme/single-truyen.php', 'rb') as f:
    ftp.storbinary('STOR /wp-content/themes/tehi-theme/single-truyen.php', f)
ftp.quit()
