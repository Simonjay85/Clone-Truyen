#!/usr/bin/env python3
"""Upload fix_remaining.php via FTP and execute it."""
import ftplib, requests, json, time

FTP_HOST = "51.79.53.190"; FTP_USER = "alotoinghe"; FTP_PASS = "Nghia234!"
WP_URL = "https://doctieuthuyet.com"; SECRET = "ZEN_TRUYEN_2026_BYPASS"

ftp = ftplib.FTP(FTP_HOST, timeout=30)
ftp.login(FTP_USER, FTP_PASS)
with open("fix_remaining.php", "rb") as f:
    ftp.storbinary("STOR fix_remaining.php", f)
ftp.quit()
print("Uploaded OK")
time.sleep(2)

res = requests.post(f"{WP_URL}/fix_remaining.php", json={"secret_token": SECRET}, timeout=60)
print("HTTP:", res.status_code)
print(json.dumps(res.json(), ensure_ascii=False, indent=2))

ftp = ftplib.FTP(FTP_HOST, timeout=30)
ftp.login(FTP_USER, FTP_PASS)
ftp.delete("fix_remaining.php")
ftp.quit()
print("Cleaned up")
