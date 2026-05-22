import ftplib
import requests
import json
import os

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"
WP_URL = "https://doctieuthuyet.com"

def main():
    print("🤖 Uploading verify_db_k.php to remote server...")
    try:
        ftp = ftplib.FTP(FTP_HOST, timeout=30)
        ftp.login(FTP_USER, FTP_PASS)
        local_path = "/Users/aaronnguyen/TN/App/doctieuthuyet/scratch/verify_db_k.php"
        with open(local_path, "rb") as f:
            ftp.storbinary("STOR verify_db_k.php", f)
        ftp.quit()
        print("  ✓ Uploaded successfully.")
    except Exception as e:
        print(f"  ❌ FTP Upload Error: {e}")
        return

    print("🤖 Fetching results from live WordPress site...")
    try:
        res = requests.get(f"{WP_URL}/verify_db_k.php", timeout=30)
        if res.status_code == 200:
            data = res.json()
            print("\n" + "="*60)
            print("📊 LIVE DATABASE VERIFICATION RESULTS 📊")
            print("="*60)
            print(json.dumps(data, ensure_ascii=False, indent=2))
            print("="*60 + "\n")
        else:
            print(f"  ❌ HTTP Error {res.status_code}: {res.text}")
    except Exception as e:
        print(f"  ❌ Request Error: {e}")

    print("🤖 Cleaning up verify_db_k.php from remote server...")
    try:
        ftp = ftplib.FTP(FTP_HOST, timeout=30)
        ftp.login(FTP_USER, FTP_PASS)
        ftp.delete("verify_db_k.php")
        ftp.quit()
        print("  ✓ Deleted remote file successfully.")
    except Exception as e:
        print(f"  ❌ FTP Delete Error: {e}")

if __name__ == "__main__":
    main()
