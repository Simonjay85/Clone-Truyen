#!/usr/bin/env python3
import json
import urllib.request
import ftplib
import os

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"
WP_URL = "https://doctieuthuyet.com"

php_code = """<?php
require('./wp-load.php');
$chaps = get_posts([
    'post_type' => 'chuong',
    'meta_key' => '_truyen_id',
    'meta_value' => 3940,
    'posts_per_page' => -1,
    'orderby' => 'date',
    'order' => 'ASC'
]);
$results = [];
foreach($chaps as $c) {
    $results[] = [
        'id' => $c->ID,
        'title' => $c->post_title,
        'content' => wp_strip_all_tags($c->post_content)
    ];
}
header('Content-Type: application/json; charset=utf-8');
echo json_encode($results, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
?>"""

def check():
    # Write and upload absolute path
    temp_file = "/Users/aaronnguyen/TN/App/doctieuthuyet/scratch/temp_verify.php"
    with open(temp_file, "w", encoding="utf-8") as f:
        f.write(php_code)

    print("Uploading verify script via FTP...")
    ftp = ftplib.FTP(FTP_HOST)
    ftp.login(FTP_USER, FTP_PASS)
    with open(temp_file, "rb") as f:
        ftp.storbinary("STOR temp_verify.php", f)
    ftp.quit()
    
    if os.path.exists(temp_file):
        os.remove(temp_file)

    try:
        print("Fetching verification results...")
        req = urllib.request.urlopen("https://doctieuthuyet.com/temp_verify.php", timeout=30)
        data = req.read().decode('utf-8')
        chaps = json.loads(data)
        print(f"Loaded {len(chaps)} live chapters.")
        
        # Check Chapter 1
        ch1 = chaps[0]
        print(f"\n[Verification] Chapter 1: {ch1['title']} (ID: {ch1['id']})")
        if "Nguyễn Lâm Phong" in ch1['content']:
            print("❌ Error: 'Nguyễn Lâm Phong' still exists in Chapter 1!")
        else:
            print("✅ Success: 'Nguyễn Lâm Phong' successfully renamed!")
            
        if "Vũ Hoài Lâm" in ch1['content']:
            print("✅ Success: 'Vũ Hoài Lâm' is active in Chapter 1!")
        else:
            print("❌ Error: 'Vũ Hoài Lâm' is missing!")

        if "nảy lên mấy vòng" in ch1['content']:
            print("❌ Error: Ring cliché still exists!")
        else:
            print("✅ Success: Ring cliché successfully removed!")

        print("\n=== Live Chapter 1 Polished Excerpt ===")
        print(ch1['content'][400:1500].strip())
        
        # Check Chapter 8
        if len(chaps) >= 8:
            ch8 = chaps[7]
            print(f"\n[Verification] Chapter 8: {ch8['title']} (ID: {ch8['id']})")
            if "Nguyễn Lâm Phong" in ch8['content']:
                print("❌ Error: 'Nguyễn Lâm Phong' still exists in Chapter 8!")
            else:
                print("✅ Success: 'Nguyễn Lâm Phong' successfully renamed to 'Vũ Hoài Lâm' in Chapter 8.")
            
    finally:
        print("\nCleaning up remote verify script...")
        ftp = ftplib.FTP(FTP_HOST)
        ftp.login(FTP_USER, FTP_PASS)
        try:
            ftp.delete("temp_verify.php")
            print("✓ Remote verify script deleted.")
        except Exception as e:
            print(f"Warning: could not delete temp_verify.php: {e}")
        ftp.quit()

if __name__ == "__main__":
    check()
