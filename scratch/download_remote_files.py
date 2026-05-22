import ftplib

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"

try:
    ftp = ftplib.FTP(FTP_HOST)
    ftp.login(FTP_USER, FTP_PASS)
    ftp.cwd("/wp-content/themes/tehi-theme")
    with open("/Users/aaronnguyen/.gemini/antigravity-ide/brain/12ea8d69-8883-4c0b-9ecb-fc7822e46167/remote-front-page.php", 'wb') as f:
        ftp.retrbinary('RETR front-page.php', f.write)
    print("✓ Downloaded front-page.php")
    
    with open("/Users/aaronnguyen/.gemini/antigravity-ide/brain/12ea8d69-8883-4c0b-9ecb-fc7822e46167/remote-functions.php", 'wb') as f:
        ftp.retrbinary('RETR functions.php', f.write)
    print("✓ Downloaded functions.php")
    
    ftp.quit()
except Exception as e:
    print("Error:", e)
