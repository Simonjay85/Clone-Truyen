import ftplib, os

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"

FILES_TO_DOWNLOAD = [
    "page-latest.php",
    "page-completed.php",
    "page-directory.php",
    "page-library.php",
    "page-teams.php",
    "page-profile.php",
    "page.php",
    "search.php",
    "taxonomy-the_loai.php",
    "page-bxh.php",
]

try:
    ftp = ftplib.FTP(FTP_HOST)
    ftp.login(FTP_USER, FTP_PASS)
    ftp.cwd("/wp-content/themes/tehi-theme")
    
    for f in FILES_TO_DOWNLOAD:
        try:
            with open(f"tehi-theme/{f}", 'wb') as local_f:
                ftp.retrbinary(f'RETR {f}', local_f.write)
            print(f"✓ Downloaded: {f}")
        except Exception as e:
            print(f"❌ Skip {f}: {e}")
    ftp.quit()
    print("Done!")
except Exception as e:
    print("Error:", e)
