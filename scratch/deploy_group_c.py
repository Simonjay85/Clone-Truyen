#!/usr/bin/env python3
"""Deploy Group C rewrite stories via FTP + PHP endpoint."""

import ftplib
import json
import requests
import os
import sys
import time

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"
WP_URL = "https://doctieuthuyet.com"
SECRET = "ZEN_TRUYEN_2026_BYPASS"
PHP_FILENAME = "rewrite_api_v13.php"

PHP_CODE = r"""<?php
require_once("wp-load.php");
header("Content-Type: application/json");
$d=json_decode(file_get_contents("php://input"),true);
if(!$d||$d["secret"]!=="ZEN_TRUYEN_2026_BYPASS"){echo json_encode(["error"=>"Unauthorized"]);exit;}
$pid=intval($d["post_id"]);
if(!empty($d["intro"])) wp_update_post(["ID"=>$pid,"post_content"=>$d["intro"]]);
if(!empty($d["focus_keyword"])) update_post_meta($pid,"rank_math_focus_keyword",$d["focus_keyword"]);
if(!empty($d["seo_title"])) update_post_meta($pid,"rank_math_title",$d["seo_title"]);
if(!empty($d["seo_description"])) update_post_meta($pid,"rank_math_description",$d["seo_description"]);
$old=get_posts(["post_type"=>"chuong","meta_key"=>"_truyen_id","meta_value"=>$pid,"posts_per_page"=>200,"post_status"=>"any"]);
foreach($old as $c) wp_delete_post($c->ID,true);
$n=0;
foreach($d["chapters"] as $i=>$c){
$id=wp_insert_post(["post_title"=>$c["title"],"post_content"=>$c["content"],"post_status"=>"publish","post_type"=>"chuong","menu_order"=>$i+1]);
if($id&&!is_wp_error($id)){update_post_meta($id,"_truyen_id",$pid);update_post_meta($id,"_chapter_number",$i+1);$n++;}
}
update_post_meta($pid,"_chapter_count",$n);
if(function_exists("litespeed_purge_all"))litespeed_purge_all();
echo json_encode(["success"=>true,"published"=>$n,"post_id"=>$pid]);
?>"""

SCRATCH_DIR = "/Users/aaronnguyen/TN/App/doctieuthuyet/scratch"
STORY_IDS = [2745, 2752, 2759, 2766, 2773]


def upload_php_via_ftp():
    """Upload PHP file to server root via FTP."""
    print(f"[FTP] Connecting to {FTP_HOST}...")
    ftp = ftplib.FTP()
    ftp.connect(FTP_HOST, 21, timeout=30)
    ftp.login(FTP_USER, FTP_PASS)
    ftp.set_pasv(True)
    
    # Try to find WordPress root
    dirs = ftp.nlst()
    print(f"[FTP] Root dirs: {dirs[:10]}")
    
    php_bytes = PHP_CODE.encode("utf-8")
    import io
    ftp.storbinary(f"STOR {PHP_FILENAME}", io.BytesIO(php_bytes))
    print(f"[FTP] Uploaded {PHP_FILENAME} to root")
    ftp.quit()
    return True


def deploy_story(story_id):
    """Deploy a single story."""
    json_path = os.path.join(SCRATCH_DIR, f"rewrite_{story_id}_v13.json")
    
    if not os.path.exists(json_path):
        print(f"[ERROR] File not found: {json_path}")
        return False
    
    with open(json_path, "r", encoding="utf-8") as f:
        payload = json.load(f)
    
    endpoint = f"{WP_URL}/{PHP_FILENAME}"
    print(f"\n[DEPLOY] Story {story_id} -> POST {endpoint}")
    
    try:
        resp = requests.post(
            endpoint,
            json=payload,
            headers={"Content-Type": "application/json"},
            timeout=120,
            verify=True
        )
        print(f"[DEPLOY] Status: {resp.status_code}")
        print(f"[DEPLOY] Response: {resp.text[:500]}")
        
        if resp.status_code == 200:
            result = resp.json()
            if result.get("success"):
                print(f"[OK] Story {story_id} deployed. Chapters published: {result.get('published')}")
                return True
            else:
                print(f"[ERROR] Story {story_id}: {result}")
                return False
        else:
            print(f"[ERROR] HTTP {resp.status_code}: {resp.text[:300]}")
            return False
    except Exception as e:
        print(f"[ERROR] Story {story_id}: {e}")
        return False


def delete_php_via_ftp():
    """Delete PHP file from server root via FTP for security."""
    print(f"[FTP] Connecting to {FTP_HOST} for cleanup...")
    ftp = ftplib.FTP()
    ftp.connect(FTP_HOST, 21, timeout=30)
    ftp.login(FTP_USER, FTP_PASS)
    ftp.set_pasv(True)
    try:
        ftp.delete(PHP_FILENAME)
        print(f"[FTP] Deleted {PHP_FILENAME} from root")
    except Exception as e:
        print(f"[FTP ERROR] Failed to delete {PHP_FILENAME}: {e}")
    ftp.quit()


def main():
    # Step 1: Upload PHP
    try:
        upload_php_via_ftp()
    except Exception as e:
        print(f"[FTP ERROR] {e}")
        print("Trying to deploy directly (PHP may already be uploaded)...")
    
    time.sleep(2)
    
    # Step 2: Deploy each story
    results = {}
    for sid in STORY_IDS:
        ok = deploy_story(sid)
        results[sid] = ok
        if ok:
            print(f"✅ {sid} DONE")
        else:
            print(f"❌ {sid} FAILED")
        time.sleep(3)
    
    # Step 3: Cleanup PHP for security
    print("\n[FTP] Cleaning up PHP helper file from server...")
    try:
        delete_php_via_ftp()
    except Exception as e:
        print(f"[FTP CLEANUP ERROR] {e}")
        
    print("\n=== SUMMARY ===")
    done_ids = [str(k) for k, v in results.items() if v]
    failed_ids = [str(k) for k, v in results.items() if not v]
    print(f"Done: {', '.join(done_ids) if done_ids else 'None'}")
    print(f"Failed: {', '.join(failed_ids) if failed_ids else 'None'}")
    return done_ids, failed_ids


if __name__ == "__main__":
    main()
