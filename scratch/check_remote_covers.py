import ftplib
import requests
import os

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"
WP_URL = "https://doctieuthuyet.com"

def main():
    # 1. Upload helper
    print("📤 Uploading check_covers_info.php via FTP...")
    try:
        ftp = ftplib.FTP(FTP_HOST, timeout=30)
        ftp.login(FTP_USER, FTP_PASS)
        with open("check_covers_info.php", "rb") as f:
            ftp.storbinary("STOR check_covers_info.php", f)
        print("✓ Uploaded query script successfully.")
        ftp.quit()
    except Exception as e:
        print("❌ FTP Upload Error:", e)
        return

    # 2. Trigger endpoint
    print("\n🔗 Querying metadata from server...")
    try:
        res = requests.get(f"{WP_URL}/check_covers_info.php", timeout=60)
        print(f"Response Code: {res.status_code}")
        try:
            data = res.json()
            import json
            print(json.dumps(data, indent=2, ensure_ascii=False))
        except Exception as je:
            print("Raw Response text:", res.text)
    except Exception as e:
        print("❌ HTTP Request Error:", e)

    # 3. Cleanup remote
    print("\n🧹 Cleaning up remote helper...")
    try:
        ftp = ftplib.FTP(FTP_HOST, timeout=30)
        ftp.login(FTP_USER, FTP_PASS)
        ftp.delete("check_covers_info.php")
        print("✓ Deleted remote check_covers_info.php.")
        ftp.quit()
    except Exception as e:
        print("❌ Remote cleanup error:", e)

if __name__ == "__main__":
    main()
