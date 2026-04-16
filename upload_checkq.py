import ftplib
import urllib.request
try:
    ftp = ftplib.FTP("51.79.53.190")
    ftp.login("alotoinghe", "Nghia234!")
    ftp.cwd("/wp-content/themes/tehi-theme/")
    with open("check_queue.php", 'rb') as f:
        ftp.storbinary("STOR check_queue.php", f)
    ftp.quit()
    req = urllib.request.urlopen("https://doctieuthuyet.com/wp-content/themes/tehi-theme/check_queue.php")
    print(req.read().decode('utf-8'))
except Exception as e:
    print("Lỗi:", e)
