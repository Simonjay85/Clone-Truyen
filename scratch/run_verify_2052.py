# -*- coding: utf-8 -*-
import requests
import ftplib
import json

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"
WP_URL = "https://doctieuthuyet.com"

def main():
    print("Uploading verify_2052.php...")
    try:
        ftp = ftplib.FTP(FTP_HOST, timeout=30)
        ftp.login(FTP_USER, FTP_PASS)
        with open("/Users/aaronnguyen/TN/App/doctieuthuyet/scratch/verify_2052.php", "rb") as f:
            ftp.storbinary("STOR verify_2052.php", f)
        print("✓ Uploaded successfully.")
        ftp.quit()
    except Exception as e:
        print("❌ FTP Upload Error:", e)
        return

    print("Requesting verification data...")
    try:
        res = requests.get(f"{WP_URL}/verify_2052.php", timeout=30)
        data = res.json()
        print("=" * 60)
        print(f"STORY VERIFICATION FOR ID {data['story']['id']}")
        print(f"Title: {data['story']['title']}")
        print(f"Status: {data['story']['status']}")
        print(f"Total Chapters Online: {data['count']}")
        print("-" * 60)
        for chap in data['chapters']:
            print(f"  {chap['index']}. {chap['title']} (ID: {chap['id']}, Word Count: {chap['word_count']} words)")
        print("=" * 60)
    except Exception as e:
        print("❌ Verification Request Failed:", e)

    print("Cleaning up remote verify_2052.php...")
    try:
        ftp = ftplib.FTP(FTP_HOST, timeout=30)
        ftp.login(FTP_USER, FTP_PASS)
        ftp.delete("verify_2052.php")
        print("✓ Deleted remote script successfully.")
        ftp.quit()
    except Exception as e:
        print("⚠️ Failed to delete remote script:", e)

if __name__ == "__main__":
    main()
