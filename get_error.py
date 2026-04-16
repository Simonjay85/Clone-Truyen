import ftplib
import os

try:
    ftp = ftplib.FTP("51.79.53.190")
    ftp.login("alotoinghe", "Nghia234!")
    
    with open("remote_debug.log", "wb") as f:
        ftp.retrbinary("RETR wp-content/debug.log", f.write)
    
    ftp.quit()
    
    with open("remote_debug.log", "r") as f:
        lines = f.readlines()
        print("".join(lines[-30:]))
except Exception as e:
    print("Error:", e)
