# -*- coding: utf-8 -*-
import os
import subprocess
import ftplib
import urllib.request
import json

BASE_YEN_SAO = "/Users/aaronnguyen/.gemini/antigravity/brain/5ac01d3a-bfd0-41d8-b4d6-ad0c17177e44/yen_sao_nha_trang_base_1779881229208.png"
BASE_TOM_HUM = "/Users/aaronnguyen/.gemini/antigravity/brain/5ac01d3a-bfd0-41d8-b4d6-ad0c17177e44/vua_tom_hum_base_1779881253316.png"

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"
WP_URL = "https://doctieuthuyet.com"

STORY_ID_YEN_SAO = 5486
STORY_ID_TOM_HUM = 5200

def main():
    print("=" * 60)
    print("🚀 PREMIUM COVER OVERLAY & SIDE-LOAD PUBLISHING PIPELINE")
    print("=" * 60)
    
    # Define output file paths
    out_yen_sao = "scratch/yen_sao_overlaid.png"
    out_tom_hum = "scratch/tom_hum_overlaid.png"
    
    # 1. Overlay clickbait titles in 2 lines
    print("🎨 Layering 2-line clickbait text onto Nha Trang base...")
    # Title: BỊ ĐUỔI KHỎI ĐẢO YẾN \n TÔI LẬT KÈO NGHÌN TỶ
    cmd_yen = [
        "python3", "cover_overlay_standard.py",
        "--input", BASE_YEN_SAO,
        "--output", out_yen_sao,
        "--title", "BỊ ĐUỔI KHỎI ĐẢO YẾN\\nTÔI LẬT KÈO NGHÌN TỶ",
        "--subtitle", "Tác phẩm sảng văn của Đặng Quốc Khánh",
        "--position", "top"
    ]
    res_yen = subprocess.run(cmd_yen, capture_output=True, text=True)
    if res_yen.returncode == 0:
        print("✓ Created Nha Trang Bird's Nest cover with 2-line title overlay.")
    else:
        print("❌ Error overlaying Nha Trang cover:", res_yen.stderr)
        return
        
    print("\n🎨 Layering 2-line clickbait text onto Phú Yên Lobster base...")
    # Title: CHÀNG RỂ NUÔI TÔM HÙM \n LẬT KÈO NGHÌN TỶ
    cmd_tom = [
        "python3", "cover_overlay_standard.py",
        "--input", BASE_TOM_HUM,
        "--output", out_tom_hum,
        "--title", "CHÀNG RỂ NUÔI TÔM HÙM\\nLẬT KÈO NGHÌN TỶ",
        "--subtitle", "Tác phẩm sảng văn của Trần Hải Phong",
        "--position", "top"
    ]
    res_tom = subprocess.run(cmd_tom, capture_output=True, text=True)
    if res_tom.returncode == 0:
        print("✓ Created Phú Yên Lobster cover with 2-line title overlay.")
    else:
        print("❌ Error overlaying Lobster cover:", res_tom.stderr)
        return

    # 2. Upload both overlaid PNGs via FTP to wp-content/uploads/
    sideload_yen = "cover_sideload_yensao_hq.png"
    sideload_tom = "cover_sideload_tomhum_hq.png"
    
    print("\n📤 Uploading overlaid PNGs to FTP server...")
    try:
        ftp = ftplib.FTP(FTP_HOST, timeout=60)
        ftp.login(FTP_USER, FTP_PASS)
        
        ftp.cwd("wp-content/uploads")
        # Upload Yến Sào
        with open(out_yen_sao, "rb") as f:
            ftp.storbinary(f"STOR {sideload_yen}", f)
        print(f"✓ Uploaded Nha Trang cover: {sideload_yen}")
        
        # Upload Tôm Hùm
        with open(out_tom_hum, "rb") as f:
            ftp.storbinary(f"STOR {sideload_tom}", f)
        print(f"✓ Uploaded Phú Yên Lobster cover: {sideload_tom}")
        
        ftp.quit()
    except Exception as e:
        print("❌ FTP Upload Error:", e)
        return

    # 3. Write temp_update_covers.php to perform media_handle_sideload
    php_code = f"""<?php
require_once('wp-load.php');
require_once(ABSPATH . 'wp-admin/includes/image.php');
require_once(ABSPATH . 'wp-admin/includes/file.php');
require_once(ABSPATH . 'wp-admin/includes/media.php');

// Authenticate admin
$admins = get_users(['role' => 'administrator', 'number' => 1]);
if (!empty($admins)) {{
    wp_set_current_user($admins[0]->ID);
}}

function update_featured_cover($story_id, $filename) {{
    $local_path = ABSPATH . 'wp-content/uploads/' . $filename;
    if (!file_exists($local_path)) {{
        return "File not found: " . $local_path;
    }}
    
    $tmp = tempnam(get_temp_dir(), 'cover');
    if (!copy($local_path, $tmp)) {{
        @unlink($tmp);
        return "Failed to copy file to temp dir";
    }}
    
    $file_array = [
        'name' => 'cover-' . $story_id . '-hq-' . rand(100, 999) . '.png',
        'tmp_name' => $tmp
    ];
    
    $attach_id = media_handle_sideload($file_array, $story_id);
    if (is_wp_error($attach_id)) {{
        @unlink($tmp);
        return "Sideload error: " . $attach_id->get_error_message();
    }}
    
    set_post_thumbnail($story_id, $attach_id);
    @unlink($local_path); // Delete the original uploaded file
    return "SUCCESS";
}}

$res_yen = update_featured_cover({STORY_ID_YEN_SAO}, '{sideload_yen}');
$res_tom = update_featured_cover({STORY_ID_TOM_HUM}, '{sideload_tom}');

// Clear Cache
if (function_exists('litespeed_purge_all')) {{
    litespeed_purge_all();
}}

header('Content-Type: application/json');
echo json_encode([
    "success" => true,
    "yensao_update" => $res_yen,
    "tomhum_update" => $res_tom,
    "cache_cleared" => true
], JSON_PRETTY_PRINT);
?>"""

    print("\n📤 Uploading remote database update script via FTP...")
    try:
        with open("temp_update_covers.php", "w", encoding="utf-8") as f:
            f.write(php_code)
            
        ftp = ftplib.FTP(FTP_HOST, timeout=60)
        ftp.login(FTP_USER, FTP_PASS)
        with open("temp_update_covers.php", "rb") as f:
            ftp.storbinary("STOR temp_update_covers.php", f)
        ftp.quit()
        print("✓ Uploaded temp_update_covers.php.")
        
        # 4. Trigger PHP script via HTTP
        print("🔗 Querying database update endpoint...")
        req = urllib.request.urlopen("https://doctieuthuyet.com/temp_update_covers.php")
        print("WordPress Media Core Response:")
        print(req.read().decode('utf-8'))
        
        # 5. Clean up remote file
        print("🧹 Cleaning up remote helper script...")
        ftp = ftplib.FTP(FTP_HOST, timeout=60)
        ftp.login(FTP_USER, FTP_PASS)
        ftp.delete("temp_update_covers.php")
        ftp.quit()
        print("✓ Remote cleanup complete.")
        
        # Clean up local temporary files
        if os.path.exists("temp_update_covers.php"):
            os.remove("temp_update_covers.php")
        if os.path.exists(out_yen_sao):
            os.remove(out_yen_sao)
        if os.path.exists(out_tom_hum):
            os.remove(out_tom_hum)
            
    except Exception as e:
        print("❌ Error during script upload or database update:", e)

if __name__ == "__main__":
    main()
