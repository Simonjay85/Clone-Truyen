import ftplib
import requests
import json
import os

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"

def main():
    print("Connecting to FTP...")
    ftp = ftplib.FTP(FTP_HOST)
    ftp.login(FTP_USER, FTP_PASS)
    
    # Upload find_missing_covers.php to remote root
    local_php = "find_missing_covers.php"
    remote_php = "/find_missing_covers.php"
    
    print(f"Uploading {local_php} to {remote_php}...")
    with open(local_php, "rb") as f:
        ftp.storbinary(f"STOR {remote_php}", f)
        
    print("Requesting JSON list from doctieuthuyet.com...")
    url = "https://doctieuthuyet.com/find_missing_covers.php"
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        data = response.json()
        print(f"Success! Found {len(data)} missing cover stories.")
        
        # Save locally
        out_path = "/tmp/missing-covers.json"
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"Saved to {out_path}")
        
    except Exception as e:
        print("Error during HTTP request:", e)
    finally:
        print("Cleaning up remote file...")
        try:
            ftp.delete(remote_php)
            print("Deleted remote file successfully.")
        except Exception as e:
            print("Failed to delete remote file:", e)
        ftp.quit()

if __name__ == "__main__":
    main()
