import ftplib
import urllib.request
import json
import os
import ssl

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"
TOKEN = "ZEN_TRUYEN_2026_BYPASS"
STORY_ID = 4740

def main():
    print("=" * 70)
    print(f"🔄 OVERWRITING STORY ID {STORY_ID} WITH 12-CHAPTER PREMIUM EDITION")
    print("=" * 70)
    
    pending_file = "/Users/aaronnguyen/TN/App/doctieuthuyet/pending_novel.json"
    if not os.path.exists(pending_file):
        print(f"❌ Error: {pending_file} not found!")
        return
        
    try:
        with open(pending_file, "r", encoding="utf-8") as f:
            novel_data = json.load(f)
        print(f"✓ Loaded 12-chapter expanded manuscript: {novel_data['title']}")
    except Exception as e:
        print("❌ Error parsing pending JSON:", e)
        return

    # 1. Prepare PHP Overwrite Script
    php_code = f"""<?php
/**
 * Overwrite Story ID {STORY_ID} with 12 Chapters - Clone Truyện App
 */

ini_set('display_errors', 0);
header('Content-Type: application/json; charset=utf-8');

$secret_token = "{TOKEN}";
if (!isset($_GET['token']) || $_GET['token'] !== $secret_token) {{
    http_response_code(401);
    echo json_encode(['error' => 'Từ chối truy cập: Sai Secret Token!']);
    exit;
}}

require_once('wp-load.php');

$admins = get_users(['role' => 'administrator', 'number' => 1]);
if (empty($admins)) {{
    http_response_code(500);
    echo json_encode(['error' => 'Không tìm thấy tài khoản Administrator nào']);
    exit;
}}
$admin_id = $admins[0]->ID;
wp_set_current_user($admin_id);

$story_id = {STORY_ID};
$title = "{novel_data['title']}";
$intro = '{novel_data['intro'].replace("'", "\\'")}';

$post = get_post($story_id);
if (!$post || $post->post_type !== 'truyen') {{
    http_response_code(404);
    echo json_encode(['error' => 'Không tìm thấy truyện với ID: ' . $story_id]);
    exit;
}}

// Delete existing chapters
$chaps = get_posts([
    'post_type' => 'chuong',
    'meta_key' => '_truyen_id',
    'meta_value' => $story_id,
    'posts_per_page' => -1
]);
$deleted_count = 0;
foreach ($chaps as $c) {{
    wp_delete_post($c->ID, true);
    $deleted_count++;
}}

// Update main story title and content
wp_update_post([
    'ID'           => $story_id,
    'post_title'   => $title,
    'post_content' => $intro,
    'post_status'  => 'publish'
]);

// Prepare new chapters array
$chapters_data = [
"""
    
    # Append chapters info to PHP array format
    for idx, chap in enumerate(novel_data['chapters']):
        escaped_title = chap['title'].replace("'", "\\'")
        escaped_content = chap['content'].replace("'", "\\'")
        php_code += f"    ['title' => '{escaped_title}', 'content' => '{escaped_content}'],\n"
        
    php_code += f"""];

$published_chapters = [];
foreach ($chapters_data as $index => $chap) {{
    $chap_title = $chap['title'];
    $chap_content = $chap['content'];
    
    $chap_id = wp_insert_post([
        'post_title'   => $chap_title,
        'post_content' => $chap_content,
        'post_status'  => 'publish',
        'post_type'    => 'chuong',
        'post_author'  => $admin_id,
        'menu_order'   => $index + 1
    ]);
    
    if (!is_wp_error($chap_id)) {{
        update_post_meta($chap_id, '_truyen_id', $story_id);
        $published_chapters[] = [
            'id' => $chap_id,
            'title' => $chap_title
        ];
    }}
}}

// Purge Cache
if (function_exists('litespeed_purge_all')) {{
    litespeed_purge_all();
    $cache_purged = true;
}} else {{
    $cache_purged = false;
}}

echo json_encode([
    'success' => true,
    'story_id' => $story_id,
    'title' => $title,
    'deleted_chapters_count' => $deleted_count,
    'chapters_count' => count($published_chapters),
    'cache_purged' => $cache_purged
], JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
?>
"""

    temp_php_file = "overwrite_story_4740.php"
    with open(temp_php_file, "w", encoding="utf-8") as f:
        f.write(php_code)
    print("✓ Prepared remote update PHP script.")

    # 2. Upload via FTP
    print("Uploading update script via FTP...")
    try:
        ftp = ftplib.FTP(FTP_HOST, timeout=30)
        ftp.login(FTP_USER, FTP_PASS)
        with open(temp_php_file, "rb") as f:
            ftp.storbinary(f"STOR {temp_php_file}", f)
        ftp.quit()
        print("✓ Uploaded overwrite_story_4740.php successfully.")
    except Exception as e:
        print("❌ FTP Upload Error:", e)
        return

    # 3. Execute HTTP Call
    print("Triggering the overwrite script over HTTPS...")
    url = f"https://doctieuthuyet.com/{temp_php_file}?token={TOKEN}"
    
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, context=ctx, timeout=120) as response:
            res_data = response.read().decode('utf-8')
            res_json = json.loads(res_data)
            
            print("\n" + "=" * 40)
            print("📊 OVERWRITE RESULTS:")
            print("=" * 40)
            print(f"Success: {res_json.get('success')}")
            print(f"Story ID: {res_json.get('story_id')}")
            print(f"Updated Title: {res_json.get('title')}")
            print(f"Old Chapters Deleted: {res_json.get('deleted_chapters_count')}")
            print(f"New Chapters Inserted: {res_json.get('chapters_count')}")
            print(f"LiteSpeed Cache Purged: {res_json.get('cache_purged')}")
            print("=" * 40 + "\n")
            
    except Exception as e:
        print("❌ HTTP Execution Error:", e)

    # 4. Clean up remote file
    print("Cleaning up remote updater file...")
    try:
        ftp = ftplib.FTP(FTP_HOST, timeout=30)
        ftp.login(FTP_USER, FTP_PASS)
        ftp.delete(temp_php_file)
        ftp.quit()
        print("✓ Remote cleanup completed successfully.")
    except Exception as e:
        print("⚠️ Remote cleanup failed:", e)
        
    if os.path.exists(temp_php_file):
        os.remove(temp_php_file)
        print("✓ Local temp script deleted.")

    # 5. Synchronize local registry existing_novels.json
    print("Synchronizing local existing_novels.json registry...")
    try:
        registry_path = "/Users/aaronnguyen/TN/App/doctieuthuyet/existing_novels.json"
        if os.path.exists(registry_path):
            with open(registry_path, "r", encoding="utf-8") as f:
                novels = json.load(f)
                
            updated = False
            for novel in novels:
                if novel.get("id") == STORY_ID:
                    novel["title"] = novel_data["title"]
                    novel["intro"] = novel_data["intro"]
                    updated = True
                    break
                    
            if updated:
                with open(registry_path, "w", encoding="utf-8") as f:
                    json.dump(novels, f, ensure_ascii=False, indent=2)
                print("✓ Synchronized local existing_novels.json registry.")
    except Exception as e:
        print("❌ Local registry synchronization error:", e)

    # 6. Clean up manuscript
    if os.path.exists(pending_file):
        os.remove(pending_file)
        print("✓ Cleaned up pending_novel.json manuscript file.")

    print("=" * 70)
    print("🎉 PROCESS COMPLETED SUCCESSFULLY!")
    print("=" * 70)

if __name__ == "__main__":
    main()
