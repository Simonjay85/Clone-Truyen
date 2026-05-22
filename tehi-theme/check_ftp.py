import ftplib
import os

def check_ftp():
    host = "51.79.53.190"
    user = "alotoinghe"
    passwd = "Nghia234!"
    
    print("Connecting to FTP...")
    ftp = ftplib.FTP(host)
    ftp.login(user, passwd)
    print("Connected.")
    
    # Change directory to wp-content/themes/tehi-theme
    ftp.cwd("/wp-content/themes/tehi-theme")
    print("Current remote directory:", ftp.pwd())
    
    # List files
    files = []
    ftp.dir(files.append)
    for f in files:
        print(f)
        
    ftp.quit()

if __name__ == "__main__":
    check_ftp()
