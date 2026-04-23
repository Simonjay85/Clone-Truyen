import ftplib
ftp = ftplib.FTP("51.79.53.190")
ftp.login("alotoinghe", "Nghia234!")
with open('tehi-theme/header.php', 'rb') as f:
    ftp.storbinary('STOR /wp-content/themes/tehi-theme/header.php', f)
ftp.quit()
print("Uploaded header.php successfully!")
