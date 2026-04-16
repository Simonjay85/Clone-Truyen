import ftplib
try:
    ftp = ftplib.FTP("51.79.53.190")
    ftp.login("alotoinghe", "Nghia234!")
    ftp.cwd("/")
    with open("test_wp.php", "rb") as f:
        ftp.storbinary("STOR test_wp.php", f)
    ftp.quit()
    print("Uploaded test")
except Exception as e:
    print("Error:", e)
