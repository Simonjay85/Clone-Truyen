import ftplib
FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"

try:
    ftp = ftplib.FTP(FTP_HOST)
    ftp.login(FTP_USER, FTP_PASS)
    ftp.cwd("/wp-content/themes/tehi-theme")
    items = []
    ftp.retrlines('LIST', items.append)
    for i in items:
        if '.php' in i:
            print(i)
    ftp.quit()
except Exception as e:
    print("Error:", e)
