import ftplib

try:
    ftp = ftplib.FTP("51.79.53.190")
    ftp.login("alotoinghe", "Nghia234!")
    print(ftp.nlst("/wp-content/themes"))
    ftp.quit()
except Exception as e:
    print("Lỗi:", e)
