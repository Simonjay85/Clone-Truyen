import os
import json
import ftplib
import requests
import subprocess

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"
WP_URL = "https://doctieuthuyet.com"

def main():
    print("=" * 60)
    print("🗑️ DELETING DUPLICATE STORY ID 7470...")
    print("=" * 60)
    
    # 1. Create the PHP delete script
    php_content = """<?php
ini_set('display_errors', 1);
error_reporting(E_ALL);
header('Content-Type: application/json');

if (!isset($_GET['token']) || $_GET['token'] !== 'zen_delete_story_2026') {
    http_response_code(403);
    echo json_encode(['error' => 'Unauthorized']);
    exit;
}

require_once('wp-load.php');

$id = 7470;
$post = get_post($id);
if ($post) {
    $chapters = get_posts(array(
        'post_type' => 'chuong',
        'meta_key' => '_truyen_id',
        'meta_value' => $id,
        'posts_per_page' => -1,
        'fields' => 'ids'
    ));
    
    foreach($chapters as $cid) {
        wp_delete_post($cid, true);
    }
    wp_delete_post($id, true);
    
    if (function_exists('litespeed_purge_all')) {
        litespeed_purge_all();
    }
    
    echo json_encode([
        'success' => true,
        'deleted_id' => $id,
        'chapters_deleted' => count($chapters)
    ]);
} else {
    echo json_encode(['success' => false, 'error' => 'Post not found']);
}
?>"""

    php_filename = "temp_delete_story.php"
    with open(php_filename, "w", encoding="utf-8") as f:
        f.write(php_content)
        
    # 2. Upload via FTP
    print("📤 Uploading temp_delete_story.php to server via FTP...")
    try:
        ftp = ftplib.FTP(FTP_HOST, timeout=60)
        ftp.login(FTP_USER, FTP_PASS)
        with open(php_filename, "rb") as f:
            ftp.storbinary("STOR temp_delete_story.php", f)
        print("✓ Uploaded successfully.")
        ftp.quit()
    except Exception as e:
        print("❌ FTP Upload Error:", e)
        if os.path.exists(php_filename):
            os.remove(php_filename)
        return

    # 3. Trigger deletion over HTTP
    print("🔗 Triggering story deletion via HTTP call...")
    try:
        url = f"{WP_URL}/temp_delete_story.php?token=zen_delete_story_2026"
        res = requests.get(url, timeout=90)
        print("Response Code:", res.status_code)
        try:
            print("Response Data:", res.json())
        except:
            print("Raw Response:", res.text)
    except Exception as e:
        print("❌ HTTP Request Error:", e)

    # 4. Clean up PHP script
    print("🧹 Cleaning up remote helper...")
    try:
        ftp = ftplib.FTP(FTP_HOST, timeout=60)
        ftp.login(FTP_USER, FTP_PASS)
        ftp.delete("temp_delete_story.php")
        print("✓ Deleted temp_delete_story.php on server.")
        ftp.quit()
    except Exception as e:
        print("❌ Remote clean up error:", e)

    if os.path.exists(php_filename):
        os.remove(php_filename)
        print("✓ Deleted local temp_delete_story.php.")

    # 5. Clean up existing_novels.json
    existing_path = "existing_novels.json"
    if os.path.exists(existing_path):
        print("\n🧹 Cleaning up local registry existing_novels.json...")
        try:
            with open(existing_path, "r", encoding="utf-8") as f:
                existing = json.load(f)
            
            # Filter out ID 7470
            new_existing = [x for x in existing if x.get("id") != 7470]
            
            with open(existing_path, "w", encoding="utf-8") as f:
                json.dump(new_existing, f, ensure_ascii=False, indent=2)
            print(f"✓ Updated existing_novels.json (filtered from {len(existing)} to {len(new_existing)} items).")
        except Exception as e:
            print("❌ Registry cleanup error:", e)

    # 6. SEO Cache Clear
    print("\n⚡ Triggering RankMath SEO and cache update...")
    seo_res = subprocess.run(["python3", "scratch/update_all_rankmath_seo.py"], capture_output=True, text=True)
    print(seo_res.stdout)

if __name__ == "__main__":
    main()
