import ftplib

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"

try:
    ftp = ftplib.FTP(FTP_HOST)
    ftp.login(FTP_USER, FTP_PASS)
    ftp.cwd("/")
    
    print("Checking if index.html exists in remote root...")
    files = ftp.nlst()
    if "index.html" in files:
        print("Found index.html. Downloading contents...")
        contents = []
        ftp.retrlines("RETR index.html", contents.append)
        print("\n=== Remote index.html Contents ===")
        print("\n".join(contents))
        print("==================================\n")
    else:
        print("index.html not found on FTP server root.")
    
    ftp.quit()
except Exception as e:
    print("Error:", e)
