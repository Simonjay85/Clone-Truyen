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
    
    local_php = "find_broken_covers.php"
    remote_php = "/find_broken_covers.php"
    
    print(f"Uploading {local_php} to {remote_php}...")
    with open(local_php, "rb") as f:
        ftp.storbinary(f"STOR {remote_php}", f)
        
    print("Requesting JSON list from doctieuthuyet.com...")
    url = "https://doctieuthuyet.com/find_broken_covers.php"
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        data = response.json()
        print(f"\nSuccess! Found {len(data)} items that are either broken or not standard portrait aspect ratio.\n")
        print(json.dumps(data, ensure_ascii=False, indent=2))
        
        # Save results locally
        with open("/tmp/broken_covers_result.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            
    except Exception as e:
        print("Error during HTTP request:", e)
    finally:
        print("\nCleaning up remote file...")
        try:
            ftp.delete(remote_php)
            print("Deleted remote file successfully.")
        except Exception as e:
            print("Failed to delete remote file:", e)
        ftp.quit()

if __name__ == "__main__":
    main()
