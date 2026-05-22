import os
import ftplib
import requests
import json

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"
WP_URL = "https://doctieuthuyet.com"

PHP_AUDITOR = """<?php
require_once('wp-load.php');
header('Content-Type: application/json');

$args = array(
    'post_type'      => 'truyen',
    'post_status'    => 'any',
    'posts_per_page' => -1,
);
$query = new WP_Query($args);
$results = array();

if ($query->have_posts()) {
    while ($query->have_posts()) {
        $query->the_post();
        $id = get_the_ID();
        $title = get_the_title();
        $slug = get_post_field('post_name', $id);
        
        $thumb_url = '';
        if (has_post_thumbnail($id)) {
            $thumb_url = get_the_post_thumbnail_url($id, 'full');
        }
        
        $results[] = array(
            'id' => $id,
            'title' => $title,
            'slug' => $slug,
            'thumb_url' => $thumb_url
        );
    }
    wp_reset_postdata();
}

echo json_encode($results, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
?>"""

def main():
    print("📤 Uploading cover auditor helper...")
    with open("temp_cover_auditor.php", "w", encoding="utf-8") as f:
        f.write(PHP_AUDITOR)
        
    try:
        ftp = ftplib.FTP(FTP_HOST, timeout=30)
        ftp.login(FTP_USER, FTP_PASS)
        with open("temp_cover_auditor.php", "rb") as f:
            ftp.storbinary("STOR temp_cover_auditor.php", f)
        print("✓ Uploaded temp_cover_auditor.php")
        ftp.quit()
    except Exception as e:
        print(f"❌ FTP upload error: {e}")
        return

    os.remove("temp_cover_auditor.php")

    print("📡 Calling auditor API...")
    try:
        res = requests.get(f"{WP_URL}/temp_cover_auditor.php", timeout=60)
        data = res.json()
        print(f"✓ Retrieved data for {len(data)} stories.")
        
        # Save results locally
        out_path = "scratch/all_live_covers.json"
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"✓ Saved results to {out_path}")
        
    except Exception as e:
        print(f"❌ API call or parsing error: {e}")
        
    # Clean up remote helper
    print("🧹 Cleaning up remote helper...")
    try:
        ftp = ftplib.FTP(FTP_HOST, timeout=30)
        ftp.login(FTP_USER, FTP_PASS)
        ftp.delete("temp_cover_auditor.php")
        ftp.quit()
        print("✓ Removed temp_cover_auditor.php from remote server.")
    except Exception as e:
        print(f"⚠️ Could not delete temp_cover_auditor.php: {e}")

if __name__ == "__main__":
    main()
