import ftplib
import urllib.request
import ssl

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"
LOCAL_FILE = "/Users/aaronnguyen/TN/App/doctieuthuyet/tehi-theme/footer.php"
REMOTE_FILE = "/wp-content/themes/tehi-theme/footer.php"

try:
    print("1. Connecting to FTP...")
    ftp = ftplib.FTP(FTP_HOST, timeout=30)
    ftp.login(FTP_USER, FTP_PASS)
    
    print("2. Uploading footer.php to theme folder...")
    with open(LOCAL_FILE, "rb") as f:
        ftp.storbinary("STOR " + REMOTE_FILE, f)
    ftp.quit()
    print("✓ Upload complete!")
    
    print("3. Purging LiteSpeed Cache via HTTP...")
    ctx = ssl._create_unverified_context()
    url = "https://doctieuthuyet.com/wp-content/themes/tehi-theme/clear_lscache.php"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    
    with urllib.request.urlopen(req, context=ctx, timeout=15) as r:
        response_data = r.read().decode('utf-8')
        
    print("✓ Cache purge complete! Response:", response_data)
    
except Exception as e:
    print("Error:", e)
