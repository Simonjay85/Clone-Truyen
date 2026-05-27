#!/usr/bin/env python3
import ftplib, requests, json, time

H="51.79.53.190"; U="alotoinghe"; P="Nghia234!"
W="https://doctieuthuyet.com"; S="ZEN_TRUYEN_2026_BYPASS"

data = json.load(open("chapter_updates.json", encoding="utf-8"))
print(f"Updates: {len(data)}")

ftp=ftplib.FTP(H,timeout=30); ftp.login(U,P)
with open("fix_dup_chapters.php","rb") as f: ftp.storbinary("STOR fix_dup_chapters.php",f)
ftp.quit(); time.sleep(2)

r=requests.post(f"{W}/fix_dup_chapters.php",json={"secret_token":S,"updates":data},timeout=180)
print(r.status_code, json.dumps(r.json(),ensure_ascii=False,indent=2))

ftp=ftplib.FTP(H,timeout=30); ftp.login(U,P)
ftp.delete("fix_dup_chapters.php"); ftp.quit()
print("Done")
