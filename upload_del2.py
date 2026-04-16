import ftplib
try:
    ftp = ftplib.FTP("51.79.53.190")
    ftp.login("alotoinghe", "Nghia234!")
    with open("hard_delete.php", 'rb') as f:
        ftp.storbinary("STOR hard_delete.php", f)
    ftp.quit()
    print("Upload OK")
except Exception as e:
    print(e)
