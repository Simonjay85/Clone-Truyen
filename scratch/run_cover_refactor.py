#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scratch/run_cover_refactor.py — Batch Cover Refactoring Runner
"""

import os
import sys
import subprocess

targets = [
    {
        "post_id": 7466,
        "base_image": "base_cover_25.png",
        "title": "HỒN SƠN MÀI\\nĐẾ CHẾ CHỐNG GIẢ",
        "position": "bottom",
        "description": "Hồn Sơn Mài"
    },
    {
        "post_id": 7448,
        "base_image": "base_cover_42.png",
        "title": "VUA TÔM HÙM\\nPHÚ YÊN",
        "position": "top",
        "description": "Vua Tôm Hùm Phú Yên"
    },
    {
        "post_id": 7437,
        "base_image": "base_cover_59.png",
        "title": "ĐẾ CHẾ GỐM SỨ\\nBÁT TRÀNG",
        "position": "top",
        "description": "Đế Chế Gốm Sứ Bát Tràng"
    },
    {
        "post_id": 1933,
        "base_image": "scratch/remade_related_three_20260525/base_1933.png",
        "title": "CON BÉ BÊN MÁY IN\\nBÁO CÁO NGHÌN TỶ",
        "position": "top",
        "description": "Con Bé Bên Máy In"
    },
    {
        "post_id": 7379,
        "base_image": "lan_ong_base_cover.png",
        "title": "THẦN Y CHÂM CỨU\\nPHỐ LÃN ÔNG",
        "position": "top",
        "description": "Thần Y Châm Cứu Phố Lãn Ông"
    },
    {
        "post_id": 7369,
        "base_image": "base_cover_16.png",
        "title": "ĐUỔI KHỎI CÔNG TRƯỜNG\\nTÔI LÀM ÔNG CHỦ",
        "position": "top",
        "description": "Kẻ Bị Đuổi Khỏi Công Trường"
    },
    {
        "post_id": 5046,
        "base_image": "base_cover_20.png",
        "title": "KÝ ĐƠN LY HÔN\\nVỢ LÀ CEO 500 TỶ",
        "position": "top",
        "description": "Sáng Ký Đơn Ly Hôn"
    },
    {
        "post_id": 5180,
        "base_image": "base_cover_33.png",
        "title": "CẤM BẾN NHA TRANG\\nĐỘI TÀU CỨU HỘ",
        "position": "top",
        "description": "Bị Cấm Bến Ở Nha Trang"
    },
    {
        "post_id": 5294,
        "base_image": "base_cover_40.png",
        "title": "GẠT KHỎI HĐQT\\nTÔI XÂY PAYCHAIN",
        "position": "top",
        "description": "Bị Gạt Khỏi HĐQT Công Ty"
    },
    {
        "post_id": 7389,
        "base_image": "tu_nu_base_cover.png",
        "title": "TÚ NỮ ÁO VẢI CỨU QUÝ PHI\\nTHỪA TƯỚNG PHÙ SỤP ĐỎ",
        "position": "top",
        "description": "Tú Nữ Áo Vải (7389)"
    },
    {
        "post_id": 7492,
        "base_image": "tu_nu_base_cover.png",
        "title": "TÚ NỮ ÁO VẢI CỨU QUÝ PHI\\nTHỪA TƯỚNG PHÙ SỤP ĐỎ",
        "position": "top",
        "description": "Tú Nữ Áo Vải (7492)"
    },
    {
        "post_id": 7480,
        "base_image": "base_cover_33.png",
        "title": "SẮC KÝ HPLC PHƠI BÀY\\nĐẾ CHẾ TRÀ BẨN",
        "position": "top",
        "description": "Bị Đuổi Khỏi Phòng Trà"
    }
]

def main():
    print("=" * 60)
    print("🎨 BATCH COVER REFACTORING RUNNER STARTED")
    print(f"Total target covers to refactor: {len(targets)}")
    print("=" * 60)

    success_count = 0
    failure_count = 0

    for idx, t in enumerate(targets, 1):
        print(f"\n[{idx}/{len(targets)}] Processing '{t['description']}' (Post ID: {t['post_id']})...")
        
        # Verify base image path
        if not os.path.exists(t['base_image']):
            print(f"❌ ERROR: Base image path does not exist locally: {t['base_image']}")
            failure_count += 1
            continue

        cmd = [
            "python3", "process_and_upload_cover.py",
            "--base-image", t['base_image'],
            "--post-id", str(t['post_id']),
            "--title", t['title'],
            "--subtitle", "",
            "--position", t['position']
        ]

        try:
            # Run the upload and update process
            res = subprocess.run(cmd, check=True, capture_output=True, text=True)
            print(res.stdout)
            print(f"✓ Successfully processed and uploaded cover for ID {t['post_id']}.")
            success_count += 1
        except subprocess.CalledProcessError as e:
            print(f"❌ FAILED to process cover for ID {t['post_id']}:")
            print(e.stdout)
            print(e.stderr)
            failure_count += 1

    print("\n" + "=" * 60)
    print("🎉 BATCH COVER REFACTORING PROCESS COMPLETED")
    print(f"Successes: {success_count}")
    print(f"Failures:  {failure_count}")
    print("=" * 60)

if __name__ == "__main__":
    main()
