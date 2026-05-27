import ftplib
import requests
import json

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"
WP_URL = "https://doctieuthuyet.com"

def main():
    print("📤 Uploading temp_update_slug.php to FTP root...")
    ftp = ftplib.FTP(FTP_HOST, timeout=30)
    ftp.login(FTP_USER, FTP_PASS)
    with open("scratch/temp_update_slug.php", "rb") as f:
        ftp.storbinary("STOR temp_update_slug.php", f)
    ftp.quit()
    print("✓ PHP helper uploaded successfully.")

    print("🔗 Triggering live DB updates via HTTP POST...")
    payload = {
        "secret_token": "ZEN_TRUYEN_2026_BYPASS"
    }
    try:
        res = requests.post(f"{WP_URL}/temp_update_slug.php", json=payload, timeout=60)
        print(f"HTTP Response Status: {res.status_code}")
        data = res.json()
        print("Response JSON:")
        print(json.dumps(data, indent=4, ensure_ascii=False))
    except Exception as e:
        print("❌ Error during HTTP trigger:", e)

    print("🧹 Cleaning up remote helper script...")
    ftp = ftplib.FTP(FTP_HOST, timeout=30)
    ftp.login(FTP_USER, FTP_PASS)
    try:
        ftp.delete("temp_update_slug.php")
        print("✓ Successfully deleted temp_update_slug.php from server.")
    except Exception as e:
        print(f"⚠️ Remote cleanup failed: {e}")
    ftp.quit()
    print("✓ Cleanup complete.")

if __name__ == "__main__":
    main()
