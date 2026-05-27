import ftplib
import requests
import time

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"
WP_URL = "https://doctieuthuyet.com"

def main():
    print("Connecting to FTP...")
    ftp = ftplib.FTP(FTP_HOST)
    ftp.login(FTP_USER, FTP_PASS)
    
    local_file = "get_all_keys.php"
    remote_file = "get_all_keys.php"
    
    print(f"Uploading {local_file} as {remote_file}...")
    with open(local_file, "rb") as f:
        ftp.storbinary(f"STOR {remote_file}", f)
        
    print("Waiting 2s for remote server synchronization...")
    time.sleep(2)
    
    url = f"{WP_URL}/{remote_file}"
    print(f"Fetching {url}...")
    try:
        res = requests.get(url, timeout=30)
        print("Status Code:", res.status_code)
        print("--- KEYS FOUND ---")
        print(res.text)
        print("------------------")
    except Exception as e:
        print("Request failed:", e)
        
    print(f"Deleting {remote_file} from FTP...")
    try:
        ftp.delete(remote_file)
        print("Deleted successfully.")
    except Exception as e:
        print("Failed to delete remote file:", e)
        
    ftp.quit()

if __name__ == "__main__":
    main()
