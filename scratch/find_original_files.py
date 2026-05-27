import ftplib

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"

def main():
    try:
        ftp = ftplib.FTP(FTP_HOST, timeout=30)
        ftp.login(FTP_USER, FTP_PASS)
        
        folder = "wp-content/uploads/2026/05"
        ftp.cwd(f"/{folder}")
        files = ftp.nlst()
        
        print(f"🔍 Searching for 3920, 3930, 3940 files in /{folder}:")
        for f in files:
            f_lower = f.lower()
            if "3920" in f_lower or "3930" in f_lower or "3940" in f_lower:
                print(f"  - {f}")
                
        ftp.quit()
    except Exception as e:
        print("Lỗi:", e)

if __name__ == "__main__":
    main()
