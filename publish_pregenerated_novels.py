#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
publish_pregenerated_novels.py — Standard Publisher for Pregenerated Novels
========================================================================
Reads the local pending_novel_{idx}.json files written by our V13 subagents,
applies the standard cover overlay, sideloads covers via FTP, publishes to
WordPress using the atomic helper API, and performs complete cleanup.
"""

import os
import sys
import json
import time
import random
import re
import shutil
import subprocess
import ftplib
import requests

# ─── CONFIGURATION ────────────────────────────────────────────────────────────
FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"
WP_URL = "https://doctieuthuyet.com"

TARGET_INDICES = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def log(msg):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {msg}")
    sys.stdout.flush()

def process_novel(idx):
    novel_file = f"pending_novel_{idx}.json"
    if not os.path.exists(novel_file):
        log(f"⚠️ Pregenerated file {novel_file} not found yet. Skipping index {idx}.")
        return False

    log(f"============================================================")
    log(f"📖 PUBLISHING PREGENERATED NOVEL INDEX {idx}")
    log(f"============================================================")

    # Read the pregenerated JSON file
    try:
        with open(novel_file, "r", encoding="utf-8") as f:
            novel_data = json.load(f)
    except Exception as re_err:
        log(f"❌ Failed to parse pregenerated file {novel_file}: {re_err}")
        return False

    title = novel_data["title"]
    author = novel_data["author"]
    intro = novel_data["intro"]
    chapters = novel_data["chapters"]

    log(f"Loaded: '{title}' by {author} ({len(chapters)} chapters)")

    # ─── 1. COVER OVERLAY DESIGN ──────────────────────────────────────────────
    base_cover_file = f"base_cover_{idx}.png"
    pending_cover_file = "pending_cover.png"

    if not os.path.exists(base_cover_file):
        log(f"❌ Error: Base cover file {base_cover_file} not found!")
        return False

    log(f"🎨 Running cover overlay engine for base cover: {base_cover_file}...")
    try:
        # Determine a subtle premium subtitle
        male_lead = novel_data.get("male_lead", "Nam chính")
        female_lead = novel_data.get("female_lead", "Nữ chính")
        subtitle_text = f"Tác phẩm sảng văn đặc sắc của {author}"
        cmd = [
            "python3", "cover_overlay_standard.py",
            "--input", base_cover_file,
            "--output", pending_cover_file,
            "--title", title,
            "--subtitle", subtitle_text
        ]
        res = subprocess.run(cmd, capture_output=True, text=True)
        if res.returncode != 0:
            log(f"⚠️ Cover overlay failed with error:\n{res.stderr}")
            # fallback: copy base cover directly
            shutil.copy(base_cover_file, pending_cover_file)
            log("⚠️ Fallback to direct base cover copy.")
        else:
            log("✓ Cover overlay created successfully.")
    except Exception as ce:
        log(f"❌ Cover overlay system exception: {ce}")
        return False

    # ─── 2. FTP COVER SIDELOADING ─────────────────────────────────────────────
    random_id = random.randint(100000, 999999)
    cover_local_filename = f"cover_sideload_{random_id}.png"
    log(f"📤 Uploading premium cover to FTP: wp-content/uploads/{cover_local_filename}...")
    try:
        ftp = ftplib.FTP(FTP_HOST, timeout=30)
        ftp.login(FTP_USER, FTP_PASS)
        ftp.cwd("wp-content/uploads")
        with open(pending_cover_file, "rb") as f:
            ftp.storbinary(f"STOR {cover_local_filename}", f)
        ftp.quit()
        log("✓ Sideloaded cover uploaded via FTP successfully.")
    except Exception as fe:
        log(f"❌ FTP Sideload Cover Error: {fe}")
        return False

    # ─── 3. UPLOAD PUBLISH ENDPOINT HELPER ────────────────────────────────────
    log("📤 Uploading publish_novel.php helper script via FTP...")
    try:
        ftp = ftplib.FTP(FTP_HOST, timeout=30)
        ftp.login(FTP_USER, FTP_PASS)
        with open("publish_novel.php", "rb") as f:
            ftp.storbinary("STOR publish_novel.php", f)
        ftp.quit()
        log("✓ Helper script uploaded successfully.")
    except Exception as fe:
        log(f"❌ FTP Helper Upload Error: {fe}")
        return False

    # ─── 4. TRIGGER ATOMIC WORDPRESS PUBLICATION ──────────────────────────────
    log("🌐 Triggering publication via HTTP POST request...")
    payload = {
        "secret_token": "ZEN_TRUYEN_2026_BYPASS",
        "title": title,
        "intro": intro,
        "author": author,
        "genre": "Sảng Văn",
        "cover_local_filename": cover_local_filename,
        "chapters": chapters
    }

    try:
        api_url = f"{WP_URL}/publish_novel.php"
        res = requests.post(api_url, json=payload, timeout=120)
        res_data = res.json()

        if res_data.get('success'):
            log(f"🎉 NOVEL {idx} PUBLISHED SUCCESSFULLY!")
            log(f"  -> Story ID: {res_data['story_id']}")
            log(f"  -> Cover Status: {res_data['cover_status']}")
            log(f"  -> Chapters: {res_data['chapters_count']} chapters published.")

            # Clean up remote helper
            try:
                ftp = ftplib.FTP(FTP_HOST, timeout=30)
                ftp.login(FTP_USER, FTP_PASS)
                ftp.delete("publish_novel.php")
                log("✓ Cleaned up remote publish_novel.php endpoint securely.")
                ftp.quit()
            except Exception as ce:
                log(f"⚠️ Non-critical remote cleanup error: {ce}")

            # Clean up local pending files
            if os.path.exists(pending_cover_file):
                os.remove(pending_cover_file)
                log("✓ Cleaned up local pending_cover.png.")

            # Update local database existing_novels.json
            existing_path = "existing_novels.json"
            existing = []
            if os.path.exists(existing_path):
                try:
                    with open(existing_path, "r", encoding="utf-8") as f:
                        existing = json.load(f)
                except Exception:
                    pass

            new_novel_entry = {
                "id": res_data['story_id'],
                "title": res_data['title'],
                "slug": res_data['title'].lower().replace(" ", "-"),
                "intro": intro
            }
            existing.append(new_novel_entry)
            with open(existing_path, "w", encoding="utf-8") as f:
                json.dump(existing, f, ensure_ascii=False, indent=2)
            log("✓ Updated existing_novels.json local database.")

            # Remove the local pending_novel_{idx}.json file
            os.remove(novel_file)
            log(f"✓ Cleaned up local pregenerated file {novel_file}.")
            return True
        else:
            log(f"❌ API Publication error response: {res_data}")
            return False

    except Exception as ae:
        log(f"❌ API HTTP POST Exception: {ae}")
        return False

def main():
    log("🚀 PREGENERATED NOVEL PUBLISHER ACTIVATED")
    success_count = 0
    failed_indices = []

    for idx in TARGET_INDICES:
        if process_novel(idx):
            success_count += 1
        else:
            failed_indices.append(idx)
        time.sleep(5)

    log(f"============================================================")
    log(f"🏁 PROCESS FINISHED")
    log(f"  -> Total successfully published: {success_count}/{len(TARGET_INDICES)}")
    if failed_indices:
        log(f"  -> Failed or pending indices: {failed_indices}")
    log(f"============================================================")

if __name__ == "__main__":
    main()
