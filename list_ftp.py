import ftplib
FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"

try:
    ftp = ftplib.FTP(FTP_HOST)
    ftp.login(FTP_USER, FTP_PASS)
    print("In /wp-content/plugins:")
    ftp.cwd("/wp-content/plugins")
    ftp.retrlines('LIST')
    
    print("\nIn /wp-content/themes:")
    ftp.cwd("/wp-content/themes")
    ftp.retrlines('LIST')
    ftp.quit()
except Exception as e:
    print(e)
