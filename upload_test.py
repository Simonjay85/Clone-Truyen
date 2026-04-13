import ftplib
ftp = ftplib.FTP("51.79.53.190")
ftp.login("alotoinghe", "Nghia234!")
with open('test.php', 'rb') as f:
    ftp.storbinary('STOR /wp-content/test.php', f)
ftp.quit()
