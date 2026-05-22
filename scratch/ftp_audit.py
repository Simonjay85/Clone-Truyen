from ftplib import FTP

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"

def main():
    print("Connecting to FTP...")
    ftp = FTP(FTP_HOST, timeout=30)
    ftp.login(FTP_USER, FTP_PASS)
    print("Files in root directory:")
    files = ftp.nlst()
    for f in files:
        if "update_story" in f or "overwrite_story" in f or "rebuild" in f or "wp_update_story" in f:
            print(f"⚠️ Found helper file: {f}")
            # Try to delete it
            try:
                ftp.delete(f)
                print(f"✓ Deleted: {f}")
            except Exception as e:
                print(f"❌ Failed to delete {f}: {e}")
        else:
            # Print standard files to see what's there
            if f.endswith(".php"):
                print(f"  {f}")
    ftp.quit()

if __name__ == "__main__":
    main()
