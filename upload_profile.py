import ftplib
ftp = ftplib.FTP("51.79.53.190")
ftp.login("alotoinghe", "Nghia234!")
with open('test_profile.php', 'rb') as f:
    ftp.storbinary('STOR /wp-content/test_profile.php', f)
ftp.quit()
