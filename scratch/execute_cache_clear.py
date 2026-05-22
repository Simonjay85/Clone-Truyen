import ftplib
import urllib.request

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"

def main():
    temp_file = "clear_remote_caches.php"
    local_path = "scratch/clear_remote_caches.php"
    
    print("Uploading cache clearing script...")
    ftp = ftplib.FTP(FTP_HOST, timeout=30)
    ftp.login(FTP_USER, FTP_PASS)
    with open(local_path, "rb") as f:
        ftp.storbinary(f"STOR {temp_file}", f)
    ftp.quit()
    print("✓ Uploaded.")
    
    print("Invoking remote script...")
    try:
        req = urllib.request.urlopen(f"https://doctieuthuyet.com/{temp_file}", timeout=60)
        output = req.read().decode('utf-8')
        print("\n=== Execution Output ===")
        print(output)
        print("========================\n")
    except Exception as e:
        print("Error invoking remote script:", e)
        
    print("Cleaning up remote file...")
    ftp = ftplib.FTP(FTP_HOST, timeout=30)
    ftp.login(FTP_USER, FTP_PASS)
    ftp.delete(temp_file)
    ftp.quit()
    print("✓ Remote file cleaned up.")

if __name__ == "__main__":
    main()
