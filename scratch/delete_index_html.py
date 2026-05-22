import ftplib

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"

try:
    ftp = ftplib.FTP(FTP_HOST)
    ftp.login(FTP_USER, FTP_PASS)
    ftp.cwd("/")
    
    print("Listing files in root directory before deletion...")
    files = ftp.nlst()
    if "index.html" in files:
        print("Found index.html. Deleting it now...")
        ftp.delete("index.html")
        print("index.html deleted successfully!")
    else:
        print("index.html was not found in remote root.")
        
    ftp.quit()
except Exception as e:
    print("Error during FTP operation:", e)
