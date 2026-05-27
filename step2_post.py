#!/usr/bin/env python3
"""POST chapter updates to WordPress endpoint."""
import requests, json, ftplib

data = json.load(open("chapter_updates.json", encoding="utf-8"))
r = requests.post(
    "https://doctieuthuyet.com/fix_dup_chapters.php",
    json={"secret_token": "ZEN_TRUYEN_2026_BYPASS", "updates": data},
    timeout=180
)
print(r.status_code)
print(json.dumps(r.json(), ensure_ascii=False, indent=2))

# cleanup
ftp = ftplib.FTP("51.79.53.190", timeout=30)
ftp.login("alotoinghe", "Nghia234!")
ftp.delete("fix_dup_chapters.php")
ftp.quit()
print("Done")
