import ftplib
try:
    ftp = ftplib.FTP("51.79.53.190")
    ftp.login("alotoinghe", "Nghia234!")
    with open("check_queue.php", 'rb') as f:
        ftp.storbinary("STOR check_queue.php", f)
    ftp.quit()
    print("Upload check_queue.php ok")
except Exception as e:
    print(e)
