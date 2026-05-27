#!/usr/bin/env python3
import ftplib, requests, json, time

FTP_HOST="51.79.53.190"; FTP_USER="alotoinghe"; FTP_PASS="Nghia234!"
WP_URL="https://doctieuthuyet.com"; SECRET="ZEN_TRUYEN_2026_BYPASS"

with open("chapter_updates.json", encoding="utf-8") as f:
    updates = json.load(f)

print(f"Loaded {len(updates)} chapters to update")

ftp=ftplib.FTP(FTP_HOST,timeout=30); ftp.login(FTP_USER,FTP_PASS)
with open("fix_dup_chapters.php","rb") as f: ftp.storbinary("STOR fix_dup_chapters.php",f)
ftp.quit(); print("PHP uploaded"); time.sleep(2)

res=requests.post(f"{WP_URL}/fix_dup_chapters.php",
    json={"secret_token":SECRET,"updates":updates}, timeout=180)
print(f"HTTP {res.status_code}")
print(json.dumps(res.json(),ensure_ascii=False,indent=2))

ftp=ftplib.FTP(FTP_HOST,timeout=30); ftp.login(FTP_USER,FTP_PASS)
ftp.delete("fix_dup_chapters.php"); ftp.quit(); print("Done")
