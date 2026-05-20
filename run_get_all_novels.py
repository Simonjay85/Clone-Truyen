import ftplib
import urllib.request
import json

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"

print("Uploading get_all_novels.php to FTP...")
try:
    ftp = ftplib.FTP(FTP_HOST, timeout=30)
    ftp.login(FTP_USER, FTP_PASS)
    
    with open("get_all_novels.php", "rb") as f:
        ftp.storbinary("STOR get_all_novels.php", f)
    
    print("Calling https://doctieuthuyet.com/get_all_novels.php ...")
    req = urllib.request.urlopen("https://doctieuthuyet.com/get_all_novels.php")
    resp_text = req.read().decode('utf-8')
    
    try:
        data = json.loads(resp_text)
        print(f"✓ Found {len(data)} existing novels:")
        for idx, item in enumerate(data, 1):
            print(f"{idx}. {item['title']} (Slug: {item['slug']})")
            print(f"   Intro: {item['intro']}...")
        with open("existing_novels.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception as je:
        print("Response was not valid JSON:")
        print(resp_text[:1000])
        
    ftp.delete("get_all_novels.php")
    ftp.quit()
    print("✓ Done")
except Exception as e:
    print("Error:", e)
