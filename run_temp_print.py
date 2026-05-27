import ftplib
import urllib.request
import json
import os

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"

def run():
    print("Uploading temp_print_all_wp_novels.php via FTP...")
    ftp = ftplib.FTP(FTP_HOST)
    ftp.login(FTP_USER, FTP_PASS)
    with open("temp_print_all_wp_novels.php", "rb") as f:
        ftp.storbinary("STOR temp_print_all_wp_novels.php", f)
    ftp.quit()
    print("Uploaded successfully!")

    try:
        print("Calling temp_print_all_wp_novels.php over HTTP...")
        req = urllib.request.urlopen("https://doctieuthuyet.com/temp_print_all_wp_novels.php", timeout=60)
        data = req.read().decode('utf-8')
        print("Response received! Parsing JSON...")
        novels = json.loads(data)
        print(f"Total novels found: {len(novels)}")
        with open("temp_list.json", "w", encoding="utf-8") as out:
            json.dump(novels, out, ensure_ascii=False, indent=2)
        print("Saved to temp_list.json")
    except Exception as e:
        print(f"Error calling URL: {e}")
    finally:
        print("Deleting temp_print_all_wp_novels.php from server...")
        ftp = ftplib.FTP(FTP_HOST)
        ftp.login(FTP_USER, FTP_PASS)
        try:
            ftp.delete("temp_print_all_wp_novels.php")
            print("Deleted successfully!")
        except Exception as e:
            print(f"Error deleting file: {e}")
        ftp.quit()

if __name__ == "__main__":
    run()
