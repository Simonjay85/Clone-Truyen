import ftplib

try:
    ftp = ftplib.FTP("51.79.53.190")
    ftp.login("alotoinghe", "Nghia234!")
    
    print(ftp.pwd())
    print(ftp.nlst())
    
    ftp.quit()
except Exception as e:
    print("Cannot read log:", e)
