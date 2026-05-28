import ftplib
import urllib.request
import ssl
import json

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"
REMOTE_THEME_DIR = "/wp-content/themes/tehi-theme"

php_debug_code = """<?php
define('WP_USE_THEMES', false);
require_once(__DIR__ . '/../../../wp-load.php');

$q = new WP_Query([
    'post_type' => 'truyen',
    'posts_per_page' => 5,
    'no_found_rows' => true
]);

$results = [];
while ($q->have_posts()) {
    $q->the_post();
    $id = get_the_ID();
    $title = get_the_title();
    
    // Get all post meta
    $meta = get_post_custom($id);
    
    // Simplify meta to only show view keys and other interesting keys
    $view_meta = [];
    foreach ($meta as $k => $v) {
        if (strpos($k, 'views') !== false || $k === '_views' || $k === 'tieuthuyet_views') {
            $view_meta[$k] = $v[0];
        }
    }
    
    $results[] = [
        'id' => $id,
        'title' => $title,
        'view_meta' => $view_meta
    ];
}

header('Content-Type: application/json');
echo json_encode($results, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
"""

try:
    print("Connecting to FTP...")
    ftp = ftplib.FTP(FTP_HOST)
    ftp.login(FTP_USER, FTP_PASS)
    
    print("Uploading temp_check_views.php...")
    with open("temp_check_views.php", "w", encoding="utf-8") as f:
        f.write(php_debug_code)
        
    ftp.cwd(REMOTE_THEME_DIR)
    with open("temp_check_views.php", "rb") as f:
        ftp.storbinary("STOR temp_check_views.php", f)
        
    print("Triggering temp_check_views.php via HTTP...")
    ctx = ssl._create_unverified_context()
    url = "https://doctieuthuyet.com/wp-content/themes/tehi-theme/temp_check_views.php"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    
    with urllib.request.urlopen(req, context=ctx) as response:
        res = response.read().decode('utf-8')
        print("\nResponse from server:")
        print(res)
        
    print("Cleaning up temp_check_views.php on server...")
    ftp.delete("temp_check_views.php")
    ftp.quit()
    
except Exception as e:
    print("Error:", e)

import os
if os.path.exists("temp_check_views.php"):
    os.remove("temp_check_views.php")
