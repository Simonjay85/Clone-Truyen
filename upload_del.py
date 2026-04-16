import ftplib
import requests
import time

try:
    ftp = ftplib.FTP("51.79.53.190")
    ftp.login("alotoinghe", "Nghia234!")
    with open("hard_delete.php", 'rb') as f:
        ftp.storbinary("STOR hard_delete.php", f)
    ftp.quit()
    
    time.sleep(1)
    res = requests.get("https://doctieuthuyet.com/hard_delete.php")
    print(res.text)
except Exception as e:
    print(e)
