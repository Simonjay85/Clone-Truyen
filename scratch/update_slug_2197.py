import ftplib
import urllib.request
import os

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"
STORY_ID = 2197
NEW_SLUG = "tho-ho-nghin-ty"

PHP_CODE = f"""<?php
require('./wp-load.php');
header('Content-Type: application/json');

$story_id = {STORY_ID};
$new_slug = "{NEW_SLUG}";

// Update post_name (permalink slug)
$result = wp_update_post([
    'ID' => $story_id,
    'post_name' => $new_slug
]);

if (is_wp_error($result)) {{
    echo json_encode([
        'success' => false,
        'error' => $result->get_error_message()
    ]);
}} else {{
    // Flush rewrite rules to make sure new permalinks are active instantly
    global $wp_rewrite;
    $wp_rewrite->flush_rules(true);
    
    if (function_exists('litespeed_purge_all')) {{
        litespeed_purge_all();
    }}
    
    $post = get_post($story_id);
    echo json_encode([
        'success' => true,
        'story_id' => $story_id,
        'new_slug' => $post->post_name,
        'permalink' => get_permalink($story_id)
    ], JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE);
}}
?>"""

def main():
    temp_file = "temp_update_slug.php"
    with open(temp_file, "w", encoding="utf-8") as f:
        f.write(PHP_CODE)
        
    print("Uploading slug update helper via FTP...")
    ftp = ftplib.FTP(FTP_HOST, timeout=30)
    ftp.login(FTP_USER, FTP_PASS)
    with open(temp_file, "rb") as f:
        ftp.storbinary(f"STOR {temp_file}", f)
    ftp.quit()
    print("✓ Uploaded.")
    
    print("Executing slug update via HTTP...")
    try:
        req = urllib.request.urlopen("https://doctieuthuyet.com/temp_update_slug.php")
        print("Server Response:", req.read().decode('utf-8'))
    except Exception as e:
        print("Error executing:", e)
        
    print("Cleaning up remote helper...")
    ftp = ftplib.FTP(FTP_HOST, timeout=30)
    ftp.login(FTP_USER, FTP_PASS)
    ftp.delete(temp_file)
    ftp.quit()
    print("✓ Remote cleanup done.")
    
    if os.path.exists(temp_file):
        os.remove(temp_file)

if __name__ == "__main__":
    main()
