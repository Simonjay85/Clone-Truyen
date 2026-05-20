import ftplib
import urllib.request
import os

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"

print("Uploading get_keys.php to FTP root...")
try:
    ftp = ftplib.FTP(FTP_HOST, timeout=30)
    ftp.login(FTP_USER, FTP_PASS)
    
    with open("get_keys.php", "rb") as f:
        ftp.storbinary("STOR get_keys.php", f)
    print("✓ Uploaded get_keys.php")
    
    # Request via HTTP
    print("Calling https://doctieuthuyet.com/get_keys.php ...")
    req = urllib.request.urlopen("https://doctieuthuyet.com/get_keys.php")
    resp_text = req.read().decode('utf-8')
    print("Output from server:")
    print(resp_text)
    
    # Delete from remote
    ftp.delete("get_keys.php")
    print("✓ Deleted get_keys.php from remote server")
    ftp.quit()
    
except Exception as e:
    print("Error:", e)
