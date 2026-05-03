import ftplib
import os

# FTP Config (reusing existing credentials from project)
FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"
THEME_DIR = "/wp-content/themes/tehi-theme/"
LOCAL_DIR = os.path.dirname(os.path.abspath(__file__)) + "/tehi-theme/"

# Files to upload
files_to_upload = [
    "header.php",
    "footer.php",
    "front-page.php",
]

def upload():
    ftp = ftplib.FTP(FTP_HOST)
    ftp.login(FTP_USER, FTP_PASS)
    ftp.cwd(THEME_DIR)

    for filename in files_to_upload:
        local_path = LOCAL_DIR + filename
        if os.path.exists(local_path):
            with open(local_path, 'rb') as f:
                ftp.storbinary(f'STOR {filename}', f)
            print(f"✅ Uploaded: {filename}")
        else:
            print(f"⚠️  Skipped (not found): {filename}")

    # Upload .htaccess-performance to root
    htaccess_path = LOCAL_DIR + ".htaccess-performance"
    if os.path.exists(htaccess_path):
        ftp.cwd("/")
        with open(htaccess_path, 'rb') as f:
            ftp.storbinary('STOR .htaccess-performance', f)
        print("✅ Uploaded: .htaccess-performance (to root)")
        print("⚠️  NOTE: You need to manually append the contents to your .htaccess file!")
        print("   Run: cat .htaccess-performance >> .htaccess")
    
    ftp.quit()
    print("\n🎉 Upload complete!")
    print("📋 Next steps:")
    print("   1. SSH or FTP into server")
    print("   2. Append .htaccess-performance to .htaccess: cat .htaccess-performance >> .htaccess")  
    print("   3. Purge LiteSpeed Cache")
    print("   4. Re-run PageSpeed Insights to verify")

if __name__ == "__main__":
    upload()
