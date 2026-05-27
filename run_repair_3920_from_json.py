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
    print("🚀 LIVE DATABASE CHAPTERS RESTORATION ENGINE (STORY ID 3920)")
    print("=" * 60)
    
    # Check if local json exists
    json_path = "scratch/rebuilt_3920_chapters.json"
    if not os.path.exists(json_path):
        print(f"❌ Local json {json_path} not found!")
        return

    # 1. Upload the JSON data via FTP
    print("📤 Uploading rebuilt_3920_chapters.json via FTP...")
    ftp = ftplib.FTP(FTP_HOST)
    ftp.login(FTP_USER, FTP_PASS)
    with open(json_path, "rb") as f:
        ftp.storbinary("STOR rebuilt_3920_chapters.json", f)
    print("✓ Uploaded rebuilt_3920_chapters.json successfully!")
    ftp.quit()

    # 2. Write the PHP insertion script
    php_code = """<?php
require('./wp-load.php');

$secret_token = "ZEN_TRUYEN_2026_BYPASS";
if (!isset($_GET['secret']) || $_GET['secret'] !== $secret_token) {
    die(json_encode(["error" => "Access denied"]));
}

$story_id = 3920;
$json_file = './rebuilt_3920_chapters.json';

if (!file_exists($json_file)) {
    die(json_encode(["error" => "rebuilt_3920_chapters.json not found on server"]));
}

$raw = file_get_contents($json_file);
$data = json_decode($raw, true);

if (!$data || !isset($data['chapters'])) {
    die(json_encode(["error" => "Invalid JSON structure"]));
}

// Get the existing 8 chapters
$chaps = get_posts([
    'post_type' => 'chuong',
    'meta_key' => '_truyen_id',
    'meta_value' => $story_id,
    'posts_per_page' => -1,
    'orderby' => 'menu_order date',
    'order' => 'ASC'
]);

if (count($chaps) !== 8) {
    die(json_encode(["error" => "WordPress chapters count is not exactly 8. Found " . count($chaps)]));
}

$updated = [];
foreach ($data['chapters'] as $idx => $chap_draft) {
    $c_post = $chaps[$idx];
    $c_title = $chap_draft['title'];
    $c_content = $chap_draft['content'];
    
    // Update the chapter post
    $res = wp_update_post([
        'ID' => $c_post->ID,
        'post_title' => $c_title,
        'post_content' => $c_content,
        'post_status' => 'publish'
    ]);
    
    if (is_wp_error($res)) {
        $updated[] = [
            'title' => $c_title,
            'success' => false,
            'error' => $res->get_error_message()
        ];
    } else {
        $updated[] = [
            'id' => $c_post->ID,
            'title' => $c_title,
            'success' => true,
            'length' => mb_strlen(wp_strip_all_tags($c_content), 'utf-8')
        ];
    }
}

// Clear LiteSpeed Cache if available
if (function_exists('litespeed_purge_all')) {
    litespeed_purge_all();
}

header('Content-Type: application/json; charset=utf-8');
echo json_encode([
    'success' => true,
    'story_id' => $story_id,
    'updated' => $updated
], JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
exit;
?>"""

    # 3. Upload the PHP script via FTP
    print("📤 Uploading temp_insert_3920.php via FTP...")
    ftp = ftplib.FTP(FTP_HOST)
    ftp.login(FTP_USER, FTP_PASS)
    with open("temp_insert_3920.php", "w", encoding="utf-8") as f:
        f.write(php_code)
        
    with open("temp_insert_3920.php", "rb") as f:
        ftp.storbinary("STOR temp_insert_3920.php", f)
    print("✓ Uploaded temp_insert_3920.php successfully!")
    ftp.quit()

    # 4. Trigger the PHP script via HTTP
    try:
        print("🔗 Hitting remote endpoint over HTTP to run database updates...")
        url = f"https://doctieuthuyet.com/temp_insert_3920.php?secret={SECRET}"
        req = urllib.request.urlopen(url, timeout=60)
        response_data = req.read().decode('utf-8')
        res = json.loads(response_data)
        
        if res.get('success'):
            print("\n" + "=" * 60)
            print("🎉 STORY ID 3920 CHAPTERS SUCCESSFULLY RESTORED IN PRODUCTION!")
            print("=" * 60)
            for item in res['updated']:
                if item['success']:
                    print(f"  ✓ {item['title']} (ID: {item['id']}) - {item['length']} characters restored.")
                else:
                    print(f"  ❌ {item['title']} - Failed: {item['error']}")
            print("=" * 60 + "\n")
        else:
            print("❌ Failed response from PHP endpoint:", res)
            
    except Exception as e:
        print("❌ Error during HTTP request:", e)
        
    finally:
        # 5. Clean up both files from the server
        print("🧹 Cleaning up remote files...")
        ftp = ftplib.FTP(FTP_HOST)
        ftp.login(FTP_USER, FTP_PASS)
        try:
            ftp.delete("temp_insert_3920.php")
            print("  ✓ Deleted temp_insert_3920.php")
        except:
            pass
        try:
            ftp.delete("rebuilt_3920_chapters.json")
            print("  ✓ Deleted rebuilt_3920_chapters.json")
        except:
            pass
        ftp.quit()
        if os.path.exists("temp_insert_3920.php"):
            os.remove("temp_insert_3920.php")

if __name__ == "__main__":
    run()
