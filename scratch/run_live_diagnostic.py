import ftplib
import urllib.request
import ssl
import json

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"
LOCAL_FILE = "check_attachment_files.php"
REMOTE_FILE = "/check_attachment_files.php"

try:
    print("1. Connecting to FTP...")
    ftp = ftplib.FTP(FTP_HOST, timeout=30)
    ftp.login(FTP_USER, FTP_PASS)
    
    print("2. Uploading check_attachment_files.php to WordPress root...")
    with open(LOCAL_FILE, "rb") as f:
        ftp.storbinary("STOR check_attachment_files.php", f)
    ftp.quit()
    print("✓ Upload complete!")
    
    print("3. Requesting diagnostic script via HTTP...")
    ctx = ssl._create_unverified_context()
    url = "https://doctieuthuyet.com/check_attachment_files.php"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    
    with urllib.request.urlopen(req, context=ctx, timeout=15) as r:
        response_data = r.read().decode('utf-8')
        
    print("✓ Request complete! Parsing JSON response:")
    try:
        data = json.loads(response_data)
        print(json.dumps(data, indent=2, ensure_ascii=False))
    except Exception as je:
        print("Raw response (not JSON):", response_data[:1000])
        
except Exception as e:
    print("Error:", e)
