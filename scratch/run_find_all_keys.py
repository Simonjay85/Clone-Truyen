import ftplib
import requests
import os

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"
WP_URL = "https://doctieuthuyet.com"

def main():
    print("Uploading find_all_keys.php to FTP root...")
    try:
        ftp = ftplib.FTP(FTP_HOST, timeout=30)
        ftp.login(FTP_USER, FTP_PASS)
        with open("scratch/find_all_keys.php", "rb") as f:
            ftp.storbinary("STOR find_all_keys.php", f)
        ftp.quit()
        print("✓ Uploaded successfully.")
        
        print("Executing script on remote server...")
        res = requests.get(f"{WP_URL}/find_all_keys.php", timeout=30)
        print("="*40)
        print("REMOTE OUTPUT:")
        print(res.text)
        print("="*40)
        
    except Exception as e:
        print("Error during execution:", e)
    finally:
        print("Cleaning up remote file...")
        try:
            ftp = ftplib.FTP(FTP_HOST, timeout=30)
            ftp.login(FTP_USER, FTP_PASS)
            ftp.delete("find_all_keys.php")
            ftp.quit()
            print("✓ Remote cleanup completed.")
        except Exception as e:
            print("Remote cleanup error:", e)

if __name__ == "__main__":
    main()
