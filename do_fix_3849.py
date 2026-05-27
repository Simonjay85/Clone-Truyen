#!/usr/bin/env python3
import ftplib, requests, json, time
FTP_HOST="51.79.53.190"; FTP_USER="alotoinghe"; FTP_PASS="Nghia234!"
WP_URL="https://doctieuthuyet.com"; SECRET="ZEN_TRUYEN_2026_BYPASS"
ftp=ftplib.FTP(FTP_HOST,timeout=30); ftp.login(FTP_USER,FTP_PASS)
with open("fix_3849.php","rb") as f: ftp.storbinary("STOR fix_3849.php",f)
ftp.quit(); time.sleep(2)
res=requests.post(f"{WP_URL}/fix_3849.php",json={"secret_token":SECRET},timeout=60)
print(json.dumps(res.json(),ensure_ascii=False,indent=2))
ftp=ftplib.FTP(FTP_HOST,timeout=30); ftp.login(FTP_USER,FTP_PASS)
ftp.delete("fix_3849.php"); ftp.quit(); print("Done")
