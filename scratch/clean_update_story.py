import ftplib

def clean_deploy_script():
    try:
        ftp = ftplib.FTP("51.79.53.190")
        ftp.login("alotoinghe", "Nghia234!")
        ftp.cwd("/")
        
        # Delete the temporary update_story.php helper script
        try:
            ftp.delete("update_story.php")
            print("✓ Successfully deleted update_story.php from live server.")
        except Exception as delete_err:
            print("⚠️ Could not delete update_story.php (it may already be deleted):", delete_err)
            
        ftp.quit()
    except Exception as e:
        print("❌ FTP Connection/Cleanup error:", e)

if __name__ == "__main__":
    clean_deploy_script()
