import ftplib
import urllib.request
import json

try:
    # 1. Upload
    ftp = ftplib.FTP("51.79.53.190")
    ftp.login("alotoinghe", "Nghia234!")
    
    with open('check_attachment_meta.php', 'rb') as f:
        ftp.storbinary('STOR /check_attachment_meta.php', f)
    print("✓ Uploaded check_attachment_meta.php to server root")
    ftp.quit()

    # 2. Call
    req = urllib.request.urlopen("https://doctieuthuyet.com/check_attachment_meta.php")
    resp_text = req.read().decode('utf-8')
    print("Response text:")
    print(resp_text)
    
except Exception as e:
    print("Error:", e)
