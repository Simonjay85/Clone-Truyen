import ftplib
import requests
import json

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"
WP_URL = "https://doctieuthuyet.com"

# Upload
print("📤 Uploading dump script to FTP...")
ftp = ftplib.FTP(FTP_HOST, timeout=30)
ftp.login(FTP_USER, FTP_PASS)
with open("scratch/temp_dump_story_content.php", "rb") as f:
    ftp.storbinary("STOR temp_dump_story_content.php", f)
ftp.quit()

# Trigger
print("🔗 Fetching live story content...")
try:
    res = requests.get(f"{WP_URL}/temp_dump_story_content.php", timeout=60)
    data = res.json()
    print(f"✓ Found story: {data['story']['title']} with {len(data['chapters'])} chapters!")
    with open("scratch/story_3940_dump.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print("✓ Saved story content to scratch/story_3940_dump.json")
except Exception as e:
    print("❌ Failed to fetch:", e)

# Cleanup
print("🧹 Cleaning up remote dump script...")
ftp = ftplib.FTP(FTP_HOST, timeout=30)
ftp.login(FTP_USER, FTP_PASS)
try:
    ftp.delete("temp_dump_story_content.php")
except Exception as e:
    print(f"⚠️ Remote cleanup failed: {e}")
ftp.quit()
print("✓ Cleanup complete.")
