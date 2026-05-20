import ftplib
import requests
import os

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"

def run():
    print("Uploading check_and_clean.php via FTP...")
    ftp = ftplib.FTP(FTP_HOST)
    ftp.login(FTP_USER, FTP_PASS)
    with open("check_and_clean.php", "rb") as f:
        ftp.storbinary("STOR check_and_clean.php", f)
    ftp.quit()
    print("Uploaded successfully!")

    try:
        print("Calling check_and_clean.php over HTTP...")
        res = requests.get("https://doctieuthuyet.com/check_and_clean.php", timeout=30)
        print(f"HTTP Status: {res.status_code}")
        print("Response:")
        print(res.text)
    except Exception as e:
        print(f"Error calling URL: {e}")
    finally:
        print("Deleting check_and_clean.php from server...")
        ftp = ftplib.FTP(FTP_HOST)
        ftp.login(FTP_USER, FTP_PASS)
        try:
            ftp.delete("check_and_clean.php")
            print("Deleted successfully!")
        except Exception as e:
            print(f"Error deleting file: {e}")
        ftp.quit()

if __name__ == "__main__":
    run()
