#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test_single_realistic_cover.py — Generate a highly realistic cover for Story 1 (NFT) and show it to the user.
"""

import sys
import os
import requests
import subprocess

sys.path.append("/Users/aaronnguyen/TN/App/doctieuthuyet")
from cover_overlay_standard import apply_standard_overlay

def main():
    print("🚀 STEP 1: Verifying pre-saved Gemini-generated base image...")
    local_base = "scratch/temp_base_5498.png"
    local_overlaid = "/Users/aaronnguyen/.gemini/antigravity-ide/brain/e3a08db2-59bd-42c1-9c12-2621e1bea495/test_cover_5498.png"
    
    if not os.path.exists(local_base):
        print(f"❌ Error: Gemini-generated base image not found at '{local_base}'!")
        print("Please ensure you have generated the base image using Gemini and saved it to this path.")
        return
    print(f"✓ Found base image at: {local_base}")

    print("\n🎨 STEP 2: Applying premium 2-line title overlay (NO subtitle)...")
    title = "BỊ CƯỚP BST NFT\nVẼ LẠI TỪ SỐ 0"
    
    # Run the overlay engine
    ok = apply_standard_overlay(
        input_path=local_base,
        output_path=local_overlaid,
        title=title,
        subtitle="", # Empty string skips subtitle completely!
        position="top"
    )
    
    if ok and os.path.exists(local_overlaid):
        print(f"🎉 SUCCESS! Test cover saved to: {local_overlaid}")
        # Clean up the temp base
        if os.path.exists(local_base):
            os.remove(local_base)
    else:
        print("❌ Failed to apply standard title overlay!")

if __name__ == "__main__":
    main()
