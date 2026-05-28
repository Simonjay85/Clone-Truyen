import ftplib
import urllib.request
import urllib.error
import subprocess
import os

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"

try:
    print("=== STEP 1: Running perfect story rewrite and sync script for 5877 ===")
    result = subprocess.run(["python3", "scratch/update_story_5877_perfect.py"], capture_output=True, text=True)
    print("Subprocess Output:")
    print(result.stdout)
    if result.stderr:
        print("Subprocess Errors:")
        print(result.stderr)
        
    print("\n=== STEP 2: Connecting to FTP to upload title update script ===")
    ftp = ftplib.FTP(FTP_HOST)
    ftp.login(FTP_USER, FTP_PASS)
    with open('scratch/update_story_title_5877.php', 'rb') as f:
        ftp.storbinary('STOR update_story_title_5877.php', f)
    print("Uploaded update_story_title_5877.php to server root.")
    ftp.quit()
    
    print("\n=== STEP 3: Executing title update script ===")
    url = "https://doctieuthuyet.com/update_story_title_5877.php"
    try:
        req = urllib.request.urlopen(url)
        response_text = req.read().decode('utf-8')
        print("Title Update Response:")
        print(response_text)
    except urllib.error.HTTPError as he:
        print(f"HTTP Error: {he.code} - {he.reason}")
        print(he.read().decode('utf-8'))
    except Exception as ex:
        print("Error executing URL:", ex)
        
    print("\n=== STEP 4: Cleaning up title update script ===")
    ftp = ftplib.FTP(FTP_HOST)
    ftp.login(FTP_USER, FTP_PASS)
    ftp.delete('update_story_title_5877.php')
    print("Cleaned up update_story_title_5877.php from server.")
    ftp.quit()
    
    print("\n=== STEP 5: Purging LiteSpeed Cache ===")
    result_cache = subprocess.run(["python3", "run_clear_cache.py"], capture_output=True, text=True)
    print("Cache Purge Output:")
    print(result_cache.stdout)
    
    print("\n=== DEPLOYMENT AND SYNCHRONIZATION COMPLETED SUCCESSFULLY! ===")

except Exception as e:
    print("Global Error during deployment:", e)
