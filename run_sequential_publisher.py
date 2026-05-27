#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
run_sequential_publisher.py — Sequentially orchestrates the publication of exactly 50 premium V13 novels.
"""

import subprocess
import time
import sys
import json
import os

PROJECT_DIR = "/Users/aaronnguyen/TN/App/doctieuthuyet"
LOG_FILE = os.path.join(PROJECT_DIR, "sequential_run_progress.log")

TARGET_INDICES = [38, 39, 42, 43, 44, 45, 46, 47, 49, 50, 51, 53, 55, 56, 57, 58, 60, 62, 63]

def log_progress(msg):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    formatted_msg = f"[{timestamp}] {msg}"
    print(formatted_msg)
    sys.stdout.flush()
    
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(formatted_msg + "\n")

def check_qwen_alive():
    import requests
    try:
        res = requests.get("http://127.0.0.1:8000/v1/models", timeout=5)
        return res.status_code == 200
    except Exception:
        return False

def main():
    log_progress("🚀 STARTING SEQUENTIAL PUBLICATION OF 50 PREMIUM V13 NOVELS")
    log_progress(f"Target Indices Range: 14 to 63 (Total: {len(TARGET_INDICES)} novels)")
    
    success_count = 0
    failed_indices = []
    
    for i, idx in enumerate(TARGET_INDICES):
        log_progress("-" * 60)
        log_progress(f"📖 Novel {i+1}/{len(TARGET_INDICES)}: Processing Index {idx}...")
        
        # Verify local Qwen model server is healthy before launching
        if not check_qwen_alive():
            log_progress("⚠️ Local Qwen API server is not responding. Waiting 30s for it to recover...")
            time.sleep(30)
            if not check_qwen_alive():
                log_progress("❌ Local Qwen API server is completely offline! Halting orchestrator.")
                sys.exit(1)
                
        cmd = [sys.executable, "batch_v13_publisher.py", "--indices", str(idx)]
        
        start_time = time.time()
        res = subprocess.run(cmd, cwd=PROJECT_DIR, capture_output=True, text=True)
        elapsed = time.time() - start_time
        
        if res.returncode == 0:
            log_progress(f"✓ Success! Index {idx} published in {elapsed:.1f}s.")
            success_count += 1
        else:
            log_progress(f"❌ Failed! Index {idx} return code: {res.returncode}. Time: {elapsed:.1f}s.")
            log_progress("--- STDERR ---")
            log_progress(res.stderr)
            log_progress("--------------")
            failed_indices.append(idx)
            
        # Standard cooling period between novels to prevent memory thrashing
        log_progress("Sleeping for 15 seconds cooldown...")
        time.sleep(15)
        
    log_progress("=" * 60)
    log_progress("🏁 SEQUENTIAL PUBLICATION BATCH FINISHED")
    log_progress(f"  -> Successfully Published: {success_count}/{len(TARGET_INDICES)}")
    if failed_indices:
        log_progress(f"  -> Failed Indices: {failed_indices}")
    log_progress("=" * 60)

if __name__ == "__main__":
    main()
