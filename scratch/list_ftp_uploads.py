import ftplib

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"

def main():
    try:
        ftp = ftplib.FTP(FTP_HOST, timeout=30)
        ftp.login(FTP_USER, FTP_PASS)
        
        folders = ["wp-content/uploads/2026/05", "wp-content/uploads/2026/04", "wp-content/uploads"]
        
        for folder in folders:
            print(f"\n📂 Listing folder: {folder}")
            try:
                ftp.cwd(f"/{folder}")
                files = ftp.nlst()
                for f in files:
                    if "cover" in f or "3920" in f or "3930" in f or "3940" in f:
                        print(f"  - {f}")
            except Exception as fe:
                print(f"  Error: {fe}")
                
        ftp.quit()
    except Exception as e:
        print("Lỗi:", e)

if __name__ == "__main__":
    main()
