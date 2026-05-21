import ftplib
import urllib.request
import ssl

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"
REMOTE_THEME_DIR = "/wp-content/themes/tehi-theme"

php_debug_code = """<?php
define('WP_USE_THEMES', false);
require_once(__DIR__ . '/../../../wp-load.php');

$q = new WP_Query([
    'post_type' => 'truyen',
    's' => 'Bát Tràng',
    'posts_per_page' => 10,
    'no_found_rows' => true
]);

$results = [];
while ($q->have_posts()) {
    $q->the_post();
    $id = get_the_ID();
    $title = get_the_title();
    $thumb_id = get_post_thumbnail_id($id);
    $thumb_url_full = get_the_post_thumbnail_url($id, 'full');
    $thumb_url_medium_large = get_the_post_thumbnail_url($id, 'medium_large');
    $file_path = get_attached_file($thumb_id);
    
    $results[] = [
        'id' => $id,
        'title' => $title,
        'thumb_id' => $thumb_id,
        'thumb_url_full' => $thumb_url_full,
        'thumb_url_medium_large' => $thumb_url_medium_large,
        'file_path' => $file_path,
        'file_exists' => $file_path ? (file_exists($file_path) ? 'yes' : 'no') : 'n/a',
        'file_size' => $file_path && file_exists($file_path) ? filesize($file_path) : 0,
    ];
}

header('Content-Type: application/json');
echo json_encode($results, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
"""

print("Connecting to FTP...")
ftp = ftplib.FTP(FTP_HOST)
ftp.login(FTP_USER, FTP_PASS)

print("Uploading find_post.php...")
with open("find_post.php", "w") as f:
    f.write(php_debug_code)

ftp.cwd(REMOTE_THEME_DIR)
with open("find_post.php", "rb") as f:
    ftp.storbinary("STOR find_post.php", f)

print("Triggering find_post.php via HTTP...")
ctx = ssl._create_unverified_context()
try:
    url = "https://doctieuthuyet.com/wp-content/themes/tehi-theme/find_post.php"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, context=ctx) as response:
        html = response.read().decode('utf-8')
        print("Response from server:")
        print(html)
except Exception as e:
    print("HTTP Request failed:", e)

print("Cleaning up find_post.php on server...")
try:
    ftp.delete("find_post.php")
except Exception as e:
    print("Failed to delete from server:", e)

ftp.quit()

import os
if os.path.exists("find_post.php"):
    os.remove("find_post.php")

print("Done!")
