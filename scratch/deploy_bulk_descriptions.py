import ftplib
import urllib.request
import json
import os
import ssl

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"
TOKEN = "ZEN_TRUYEN_2026_BYPASS"

def main():
    print("=" * 70)
    print("🚀 LIVE BULK UPDATE ORCHESTRATOR - SYNCING ALL STORY DESCRIPTIONS & TITLES")
    print("=" * 70)
    
    local_json = "/Users/aaronnguyen/TN/App/doctieuthuyet/scratch/all_descriptions_update.json"
    local_php = "/Users/aaronnguyen/TN/App/doctieuthuyet/scratch/bulk_update_descriptions.php"
    
    if not os.path.exists(local_json) or not os.path.exists(local_php):
        print("❌ Error: Missing local payload or script files!")
        return

    # 1. Connect and Upload to FTP
    print("Connecting to FTP server...")
    try:
        ftp = ftplib.FTP(FTP_HOST, timeout=30)
        ftp.login(FTP_USER, FTP_PASS)
        print("✓ Logged into FTP.")
        
        # Upload payload JSON
        print("Uploading JSON payload...")
        with open(local_json, "rb") as f:
            ftp.storbinary("STOR all_descriptions_update.json", f)
        print("✓ Uploaded all_descriptions_update.json successfully.")
        
        # Upload PHP updater
        print("Uploading PHP script...")
        with open(local_php, "rb") as f:
            ftp.storbinary("STOR bulk_update_descriptions.php", f)
        print("✓ Uploaded bulk_update_descriptions.php successfully.")
        
        ftp.quit()
    except Exception as e:
        print("❌ FTP Upload Error:", e)
        return

    # 2. Trigger the update over HTTPS (ignoring SSL warnings if self-signed)
    print("Triggering the bulk update script over HTTPS...")
    url = f"https://doctieuthuyet.com/bulk_update_descriptions.php?token={TOKEN}"
    
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, context=ctx, timeout=120) as response:
            res_data = response.read().decode('utf-8')
            res_json = json.loads(res_data)
            
            print("\n" + "=" * 40)
            print("📊 DEPLOYMENT RESULTS:")
            print("=" * 40)
            print(f"Success: {res_json.get('success')}")
            print(f"Total Stories in Payload: {res_json.get('total_payload')}")
            print(f"Successfully Updated: {res_json.get('updated_count')}")
            print(f"Errors Encountered: {res_json.get('errors_count')}")
            print(f"LiteSpeed Cache Purged: {res_json.get('cache_purged')}")
            
            if res_json.get('errors'):
                print("\n❌ Errors Encountered:")
                for err in res_json.get('errors'):
                    print(f" - {err}")
            
            print("=" * 40 + "\n")
            
    except Exception as e:
        print("❌ HTTP Execution Error:", e)

    # 3. Secure Clean-up of remote files
    print("Cleaning up remote files from FTP...")
    try:
        ftp = ftplib.FTP(FTP_HOST, timeout=30)
        ftp.login(FTP_USER, FTP_PASS)
        
        try:
            ftp.delete("all_descriptions_update.json")
            print("✓ Deleted remote all_descriptions_update.json.")
        except Exception:
            pass
            
        try:
            ftp.delete("bulk_update_descriptions.php")
            print("✓ Deleted remote bulk_update_descriptions.php.")
        except Exception:
            pass
            
        ftp.quit()
        print("✓ FTP remote clean-up completed.")
    except Exception as e:
        print("⚠️ FTP clean-up error:", e)

    # 4. Synchronize local registry existing_novels.json
    print("Synchronizing local existing_novels.json registry...")
    try:
        registry_path = "/Users/aaronnguyen/TN/App/doctieuthuyet/existing_novels.json"
        with open(local_json, "r", encoding="utf-8") as f:
            new_data = json.load(f)
            
        with open(registry_path, "r", encoding="utf-8") as f:
            novels = json.load(f)
            
        sync_count = 0
        for novel in novels:
            nid = str(novel.get("id"))
            if nid in new_data:
                novel["title"] = new_data[nid]["title"]
                novel["intro"] = new_data[nid]["intro"]
                sync_count += 1
                
        with open(registry_path, "w", encoding="utf-8") as f:
            json.dump(novels, f, ensure_ascii=False, indent=2)
            
        print(f"✓ Synchronized {sync_count} novels in local existing_novels.json.")
    except Exception as e:
        print("❌ Registry Sync Error:", e)

    print("=" * 70)
    print("🎉 DEPLOYMENT COMPLETE!")
    print("=" * 70)

if __name__ == "__main__":
    main()
