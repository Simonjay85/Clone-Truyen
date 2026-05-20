import ftplib
import requests

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"

def run():
    print("Uploading get_phe_vat_chaps.php via FTP...")
    ftp = ftplib.FTP(FTP_HOST)
    ftp.login(FTP_USER, FTP_PASS)
    with open("get_phe_vat_chaps.php", "rb") as f:
        ftp.storbinary("STOR get_phe_vat_chaps.php", f)
    ftp.quit()
    print("Uploaded successfully!")

    try:
        print("Calling get_phe_vat_chaps.php over HTTP...")
        res = requests.get("https://doctieuthuyet.com/get_phe_vat_chaps.php", timeout=30)
        print(f"HTTP Status: {res.status_code}")
        print("Response:\n")
        print(res.text)
    except Exception as e:
        print(f"Error calling URL: {e}")
    finally:
        print("\nDeleting get_phe_vat_chaps.php from server...")
        ftp = ftplib.FTP(FTP_HOST)
        ftp.login(FTP_USER, FTP_PASS)
        try:
            ftp.delete("get_phe_vat_chaps.php")
            print("Deleted successfully!")
        except Exception as e:
            print(f"Error deleting file: {e}")
        ftp.quit()

if __name__ == "__main__":
    run()
