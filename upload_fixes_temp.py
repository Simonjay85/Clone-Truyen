import ftplib
ftp = ftplib.FTP("51.79.53.190")
ftp.login("alotoinghe", "Nghia234!")
with open('tehi-theme/single-chuong.php', 'rb') as f:
    ftp.storbinary('STOR /wp-content/themes/tehi-theme/single-chuong.php', f)
with open('tehi-theme/footer.php', 'rb') as f:
    ftp.storbinary('STOR /wp-content/themes/tehi-theme/footer.php', f)
ftp.quit()
print("Uploaded successfully!")
