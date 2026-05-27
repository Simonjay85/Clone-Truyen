import ftplib
import requests
import json

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"

def run():
    print("Uploading inspect_last_chaps.php via FTP...")
    ftp = ftplib.FTP(FTP_HOST)
    ftp.login(FTP_USER, FTP_PASS)
    with open("inspect_last_chaps.php", "rb") as f:
        ftp.storbinary("STOR inspect_last_chaps.php", f)
    ftp.quit()
    print("Uploaded successfully!")

    try:
        print("Calling inspect_last_chaps.php over HTTP...")
        res = requests.get("https://doctieuthuyet.com/inspect_last_chaps.php", timeout=30)
        print(f"HTTP Status: {res.status_code}")
        
        # Save output to a local JSON file to read it carefully
        with open("inspect_last_chaps_output.json", "w", encoding="utf-8") as out:
            out.write(res.text)
            
        data = res.json()
        print("\n=== SUMMARY OF RECENT STORIES ===")
        for truyen in data:
            print(f"\nID: {truyen['truyen_id']} - {truyen['truyen_title']}")
            print(f"  Total Chapters: {truyen['total_chaps_count']} (Helper Count: {truyen['helper_count']})")
            print(f"  Last chapter in ID ASC list: {truyen['last_chap_in_asc_list']}")
            print(f"  Last chapter by ID DESC query: {truyen['last_chap_by_desc_query']}")
            print(f"  Helper display name returned: {truyen['helper_display_name']}")
            print(f"  Transient display cache: {truyen['transient_display_name_cache']}")
            print(f"  Transient url cache: {truyen['transient_url_cache']}")
    except Exception as e:
        print(f"Error calling URL: {e}")
    finally:
        print("\nDeleting inspect_last_chaps.php from server...")
        ftp = ftplib.FTP(FTP_HOST)
        ftp.login(FTP_USER, FTP_PASS)
        try:
            ftp.delete("inspect_last_chaps.php")
            print("Deleted successfully!")
        except Exception as e:
            print(f"Error deleting file: {e}")
        ftp.quit()

if __name__ == "__main__":
    run()
