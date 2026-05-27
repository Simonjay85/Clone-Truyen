import ftplib
import urllib.request
import json
import os

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"
SECRET = "ZEN_TRUYEN_2026_BYPASS"

def run():
    print("=" * 60)
    print("🚀 LIVE DATABASE STORY CLEANUP ENGINE (STORY ID 2710)")
    print("=" * 60)
    
    php_code = """<?php
require('./wp-load.php');

$secret_token = "ZEN_TRUYEN_2026_BYPASS";
if (!isset($_GET['secret']) || $_GET['secret'] !== $secret_token) {
    die(json_encode(["error" => "Access denied"]));
}

$story_id = 2710;
$t = get_post($story_id);
if (!$t) {
    die(json_encode(["error" => "Story 2710 not found"]));
}

// Update story to draft
wp_update_post([
    'ID' => $story_id,
    'post_status' => 'draft'
]);

// Update all its chapters to draft
$chaps = get_posts([
    'post_type' => 'chuong',
    'meta_key' => '_truyen_id',
    'meta_value' => $story_id,
    'posts_per_page' => -1
]);

$updated_chaps = [];
foreach($chaps as $c) {
    wp_update_post([
        'ID' => $c->ID,
        'post_status' => 'draft'
    ]);
    $updated_chaps[] = [
        'id' => $c->ID,
        'title' => $c->post_title,
        'status' => 'draft'
    ];
}

// Clear LiteSpeed Cache if available
if (function_exists('litespeed_purge_all')) {
    litespeed_purge_all();
}

header('Content-Type: application/json; charset=utf-8');
echo json_encode([
    'success' => true,
    'story_id' => $story_id,
    'story_status' => 'draft',
    'chapters_count' => count($updated_chaps),
    'chapters' => $updated_chaps
], JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
exit;
?>"""

    print("📤 Uploading temp_cleanup_duplicate.php via FTP...")
    ftp = ftplib.FTP(FTP_HOST)
    ftp.login(FTP_USER, FTP_PASS)
    with open("temp_cleanup_duplicate.php", "w", encoding="utf-8") as f:
        f.write(php_code)
        
    with open("temp_cleanup_duplicate.php", "rb") as f:
        ftp.storbinary("STOR temp_cleanup_duplicate.php", f)
    print("✓ Uploaded temp_cleanup_duplicate.php successfully!")
    ftp.quit()

    try:
        print("🔗 Hitting remote endpoint over HTTP to perform draft changes...")
        url = f"https://doctieuthuyet.com/temp_cleanup_duplicate.php?secret={SECRET}"
        req = urllib.request.urlopen(url, timeout=30)
        res = json.loads(req.read().decode('utf-8'))
        
        if res.get('success'):
            print("\n" + "=" * 60)
            print("🎉 DUPLICATE STORY ID 2710 SET TO DRAFT!")
            print("=" * 60)
            print(f"  Story status: {res['story_status']}")
            print(f"  Chapters marked as draft: {res['chapters_count']}")
            for item in res['chapters']:
                print(f"    - {item['title']} (ID: {item['id']}) -> {item['status']}")
            print("=" * 60 + "\n")
        else:
            print("❌ Failed response from PHP endpoint:", res)
            
    except Exception as e:
        print("❌ Error during HTTP request:", e)
        
    finally:
        print("🧹 Cleaning up remote files...")
        ftp = ftplib.FTP(FTP_HOST)
        ftp.login(FTP_USER, FTP_PASS)
        try:
            ftp.delete("temp_cleanup_duplicate.php")
            print("  ✓ Deleted temp_cleanup_duplicate.php")
        except:
            pass
        ftp.quit()
        if os.path.exists("temp_cleanup_duplicate.php"):
            os.remove("temp_cleanup_duplicate.php")

if __name__ == "__main__":
    run()
