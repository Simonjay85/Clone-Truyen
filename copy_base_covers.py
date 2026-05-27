#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
copy_base_covers.py — Securely maps and copies existing premium base covers to all missing indices.
"""

import os
import shutil

PROJECT_DIR = "/Users/aaronnguyen/TN/App/doctieuthuyet"

# Existing premium covers in the workspace
PREMIUM_COVERS = [
    "base_cover_4.png",
    "base_cover_5.png",
    "base_cover_6.png",
    "base_cover_7.png",
    "base_cover_8.png",
    "base_cover_9.png",
    "base_cover_10.png",
    "base_cover_11.png",
    "base_cover_12.png",
    "base_cover_13.png",
    "base_cover_14.png",
    "base_cover_15.png",
    "base_cover_16.png",
    "base_cover_17.png",
    "base_cover_18.png"
]

def main():
    print("🚀 RE-MAPPING AND COPYING PREMIUM IMAGEN 3 BASE COVERS...")
    
    # Verify all source premium covers exist
    available_covers = []
    for c in PREMIUM_COVERS:
        path = os.path.join(PROJECT_DIR, c)
        if os.path.exists(path):
            available_covers.append(path)
            
    if not available_covers:
        print("❌ Error: No premium source covers found in workspace!")
        return
        
    print(f"Found {len(available_covers)} premium source covers for replication.")
    
    copied_count = 0
    for idx in range(14, 64):
        target_name = f"base_cover_{idx}.png"
        target_path = os.path.join(PROJECT_DIR, target_name)
        
        if os.path.exists(target_path):
            print(f"✓ {target_name} already exists. Skipping.")
            continue
            
        # Select one of the available premium covers sequentially to distribute them evenly
        src_cover = available_covers[copied_count % len(available_covers)]
        shutil.copy(src_cover, target_path)
        print(f"  -> Copied {os.path.basename(src_cover)} to {target_name}")
        copied_count += 1
        
    print(f"🎉 Successfully pre-mapped {copied_count} base covers in workspace!")

if __name__ == "__main__":
    main()
