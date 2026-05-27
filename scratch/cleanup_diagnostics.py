import ftplib

try:
    ftp = ftplib.FTP("51.79.53.190")
    ftp.login("alotoinghe", "Nghia234!")
    
    # Delete temporary PHP scripts
    for filepath in ['/check_php_extensions.php', '/check_attachment_meta.php']:
        try:
            ftp.delete(filepath)
            print(f"✓ Remote file deleted: {filepath}")
        except Exception as e:
            print(f"⚠ Could not delete remote file {filepath}: {e}")
            
    ftp.quit()
    print("Remote cleanup completed.")
except Exception as e:
    print("Cleanup Error:", e)
