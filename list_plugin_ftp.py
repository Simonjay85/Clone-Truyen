import ftplib
FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"

try:
    ftp = ftplib.FTP(FTP_HOST)
    ftp.login(FTP_USER, FTP_PASS)
    print("In /wp-content/plugins/tehi-crawler-manager:")
    ftp.cwd("/wp-content/plugins/tehi-crawler-manager")
    ftp.retrlines('LIST')
    
    print("\nIn admin:")
    ftp.cwd("admin")
    ftp.retrlines('LIST')
    ftp.quit()
except Exception as e:
    print(e)
