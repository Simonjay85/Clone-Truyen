import ftplib

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"

try:
    ftp = ftplib.FTP(FTP_HOST)
    ftp.login(FTP_USER, FTP_PASS)
    print("FTP Login Successful!")
    
    path = "/wp-content/themes/tehi-theme/img_data/images"
    ftp.cwd(path)
    
    print(f"Listing files in {path}:")
    files = []
    ftp.retrlines('LIST', files.append)
    for f in files:
        print(f)
        
    ftp.quit()
except Exception as e:
    print("Error:", e)
