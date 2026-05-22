import ftplib
import urllib.request
import json
import os

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"

def main():
    local_php = "scratch/find_and_dump_story.php"
    remote_php = "find_and_dump_story.php"
    
    print("Uploading helper to remote server via FTP...")
    ftp = ftplib.FTP(FTP_HOST, timeout=30)
    ftp.login(FTP_USER, FTP_PASS)
    with open(local_php, "rb") as f:
        ftp.storbinary(f"STOR {remote_php}", f)
    ftp.quit()
    print("✓ Uploaded.")
    
    print("Executing query via HTTP...")
    try:
        req = urllib.request.urlopen("https://doctieuthuyet.com/find_and_dump_story.php", timeout=60)
        data = json.loads(req.read().decode('utf-8'))
        
        if data.get('success'):
            print(f"Success! Found story: {data['story']['title']} (ID: {data['story']['id']})")
            print(f"Total chapters: {data['chapters_count']}")
            for idx, c in enumerate(data['chapters']):
                print(f"  Chap {idx+1}: {c['title']} ({c['word_count']} chars)")
                
            with open("scratch/story_dump.json", "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print("✓ Story data saved to scratch/story_dump.json")
        else:
            print("Server returned failure:", data.get('message'))
    except Exception as e:
        print("Error during HTTP request:", e)
        
    print("Cleaning up remote helper...")
    ftp = ftplib.FTP(FTP_HOST, timeout=30)
    ftp.login(FTP_USER, FTP_PASS)
    try:
        ftp.delete(remote_php)
        print("✓ Remote file deleted.")
    except Exception as e:
        print("Error deleting remote file:", e)
    ftp.quit()

if __name__ == "__main__":
    main()
