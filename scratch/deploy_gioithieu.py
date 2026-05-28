import ftplib
import urllib.request
import urllib.error

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"

try:
    print("Connecting to FTP...")
    ftp = ftplib.FTP(FTP_HOST)
    ftp.login(FTP_USER, FTP_PASS)
    print("FTP connected.")
    
    # Upload the script to the root directory
    with open('check_and_create_gioithieu.php', 'rb') as f:
        ftp.storbinary('STOR check_and_create_gioithieu.php', f)
    print("Uploaded check_and_create_gioithieu.php to remote WordPress root.")
    ftp.quit()
    
    # Execute the script
    url = "https://doctieuthuyet.com/check_and_create_gioithieu.php"
    print(f"Triggering execution at: {url}")
    try:
        req = urllib.request.urlopen(url)
        response_text = req.read().decode('utf-8')
        print("Execution Response:")
        print(response_text)
    except urllib.error.HTTPError as he:
        print(f"HTTP Error: {he.code} - {he.reason}")
        print(he.read().decode('utf-8'))
    except Exception as ex:
        print("Error executing URL:", ex)
        
    # Re-connect to delete the script for security
    print("Re-connecting to FTP to clean up...")
    ftp = ftplib.FTP(FTP_HOST)
    ftp.login(FTP_USER, FTP_PASS)
    try:
        ftp.delete('check_and_create_gioithieu.php')
        print("Cleaned up check_and_create_gioithieu.php from remote server.")
    except Exception as de:
        print("Error deleting script:", de)
    ftp.quit()

except Exception as e:
    print("Error:", e)
