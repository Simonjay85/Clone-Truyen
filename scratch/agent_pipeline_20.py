#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
agent_pipeline_20.py — Orchestrator for verifying and publishing 20 premium sảng văn novels.
========================================================================================
This script automates:
1. Loading the draft from scratch/draft_novel_<id>.json.
2. Verifying V12 compliance (word counts, HTML paragraph structures, JSON schema).
3. Finding the local base cover scratch/base_cover_<id>.png.
4. Calling cover_overlay_standard.py to create pending_cover.png.
5. Preparing pending_novel.json.
6. Invoking publish_local_novel.py to sideload and publish the novel.
7. Updating the progress log scratch/progress_20_novels.json.

Usage:
    python3 scratch/agent_pipeline_20.py --id <id>
"""

import os
import sys
import json
import argparse
import subprocess
import re

def count_words(text):
    # Strip HTML tags
    clean_text = re.sub(r'<[^>]+>', ' ', text)
    # Split by whitespace
    words = clean_text.split()
    return len(words)

def verify_v12_compliance(draft):
    print("🔍 Running V12 Compliance verification...")
    errors = []
    
    # 1. Check basic fields
    for field in ["title", "subtitle", "author", "genre", "intro", "cover_prompt", "chapters"]:
        if field not in draft:
            errors.append(f"Missing required field: '{field}'")
            
    if errors:
        return False, errors

    # 2. Check chapters length and content
    chapters = draft["chapters"]
    if len(chapters) < 5:
        errors.append(f"Expected at least 5 chapters, found only {len(chapters)}")
        
    for idx, chap in enumerate(chapters):
        c_num = idx + 1
        c_title = chap.get("title", f"Chương {c_num}")
        c_content = chap.get("content", "")
        
        # Word count check
        w_count = count_words(c_content)
        print(f"   📖 Chapter {c_num}: '{c_title}' -> {w_count} words")
        if w_count < 1000:
            errors.append(f"Chapter {c_num} ('{c_title}') has only {w_count} words. Must be >= 1000 words.")
            
        # HTML tag checks: must wrap everything in <p>...</p>\n
        # We check that every sentence/paragraph block is wrapped in <p>...</p>
        # A simple check is that the content starts with <p> and ends with </p> (ignoring trailing whitespace)
        content_stripped = c_content.strip()
        if not (content_stripped.startswith("<p>") or content_stripped.startswith("<strong>") or content_stripped.startswith("<!--") or content_stripped.startswith("<hr")):
            errors.append(f"Chapter {c_num} ('{c_title}') content does not seem to start with standard HTML tags.")
            
        if not content_stripped.endswith("</p>"):
            errors.append(f"Chapter {c_num} ('{c_title}') content does not end with '</p>'.")
            
        # Count <p> tags to make sure it's structured nicely
        p_count = content_stripped.count("<p>")
        if p_count < 10:
            errors.append(f"Chapter {c_num} has only {p_count} <p> tags. Must have rich, detailed mobile paragraphs.")

    if errors:
        return False, errors
    return True, []

def update_progress(novel_id, status, wp_id=None, error_msg=None):
    progress_file = "scratch/progress_20_novels.json"
    progress = {}
    if os.path.exists(progress_file):
        try:
            with open(progress_file, "r", encoding="utf-8") as f:
                progress = json.load(f)
        except Exception:
            pass
            
    progress[str(novel_id)] = {
        "status": status,
        "wp_id": wp_id,
        "error": error_msg,
        "last_updated": time_str()
    }
    
    with open(progress_file, "w", encoding="utf-8") as f:
        json.dump(progress, f, ensure_ascii=False, indent=2)

def time_str():
    import datetime
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def main():
    parser = argparse.ArgumentParser(description="Novel Batch Coordinator & Publisher")
    parser.add_argument("--id", type=int, required=True, help="ID of the novel to publish (from missing_pipeline.json)")
    args = parser.parse_args()
    
    novel_id = args.id
    draft_file = f"scratch/draft_novel_{novel_id}.json"
    
    print("=" * 70)
    print(f"🚀 Batch Coordinator running for Novel ID: {novel_id}")
    print("=" * 70)
    
    # 1. Load Draft
    if not os.path.exists(draft_file):
        print(f"❌ Error: Draft file not found: {draft_file}")
        sys.exit(1)
        
    try:
        with open(draft_file, "r", encoding="utf-8") as f:
            draft = json.load(f)
        print(f"✓ Loaded draft: '{draft['title']}' by {draft.get('author', 'Unknown')}")
    except Exception as e:
        print(f"❌ Error parsing JSON from {draft_file}: {e}")
        sys.exit(1)
        
    # 2. Verify V12 Compliance
    ok, errors = verify_v12_compliance(draft)
    if not ok:
        print("❌ V12 Compliance check FAILED!")
        for err in errors:
            print(f"   - {err}")
        update_progress(novel_id, "failed_v12_verification", error_msg="; ".join(errors))
        sys.exit(1)
    print("✅ V12 Compliance verification PASSED!")

    # 3. Locate Base Cover Image
    base_cover_file = f"scratch/base_cover_{novel_id}.png"
    if not os.path.exists(base_cover_file):
        # Check parent folder as fallback
        base_cover_file = f"base_cover_{novel_id}.png"
        if not os.path.exists(base_cover_file):
            print(f"⚠️ Warning: Base cover image '{base_cover_file}' not found.")
            print("   Please generate the image first using the parent agent's generate_image tool.")
            print("   Saving draft validation state. Run again when the cover image is ready.")
            update_progress(novel_id, "validated_pending_cover")
            sys.exit(0)
            
    # 4. Generate Premium Titled Cover via cover_overlay_standard.py
    print(f"🎨 Compositing gold borders and 3D titles onto cover...")
    pending_cover = "pending_cover.png"
    title_escaped = draft["title"].replace("\n", "\\n")
    subtitle_escaped = draft.get("subtitle", "")
    
    overlay_cmd = [
        "python3", "cover_overlay_standard.py",
        "--input", base_cover_file,
        "--output", pending_cover,
        "--title", title_escaped,
        "--subtitle", subtitle_escaped
    ]
    
    try:
        res = subprocess.run(overlay_cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(res.stdout)
        print("✓ Successfully created premium titled cover 'pending_cover.png'")
    except subprocess.CalledProcessError as e:
        print("❌ Error running cover_overlay_standard.py:")
        print(e.stderr)
        update_progress(novel_id, "failed_cover_overlay", error_msg=e.stderr)
        sys.exit(1)

    # 5. Copy base cover to scratch directory for backup
    backup_base = f"scratch/base_cover_{novel_id}.png"
    if not os.path.exists(backup_base) and os.path.exists(base_cover_file) and base_cover_file != backup_base:
        import shutil
        shutil.copy(base_cover_file, backup_base)
        print(f"✓ Backed up base cover to {backup_base}")

    # 6. Prepare pending_novel.json
    pending_novel = "pending_novel.json"
    try:
        # We need to construct the standard payload format
        payload = {
            "title": draft["title"].replace("\\n", " ").replace("\n", " "),
            "author": draft["author"],
            "genre": draft["genre"],
            "intro": draft["intro"],
            "cover_prompt": draft["cover_prompt"],
            "chapters": draft["chapters"]
        }
        with open(pending_novel, "w", encoding="utf-8") as f:
            json.dump(payload, f, ensure_ascii=False, indent=2)
        print("✓ Prepared 'pending_novel.json' for the publisher engine.")
    except Exception as e:
        print(f"❌ Error creating pending_novel.json: {e}")
        update_progress(novel_id, "failed_pending_novel_creation", error_msg=str(e))
        sys.exit(1)

    # 7. Execute publish_local_novel.py
    print("🚀 Triggering publish_local_novel.py...")
    try:
        res = subprocess.run(["python3", "publish_local_novel.py"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(res.stdout)
        
        # Parse the output to find WP ID
        wp_id_match = re.search(r"ID:\s*(\d+)", res.stdout)
        wp_id = int(wp_id_match.group(1)) if wp_id_match else None
        
        if "🎉 NOVEL PUBLISHED SUCCESSFULLY" in res.stdout:
            print(f"🎉 SUCCESS! Novel published to WordPress with ID: {wp_id}")
            update_progress(novel_id, "published", wp_id=wp_id)
            
            # Backup final cover as well
            backup_cover = f"scratch/cover_{novel_id}.png"
            # Since publish_local_novel.py deletes pending_cover.png, we should have copied it before.
            # Let's see if we can do this next time or retrieve it if still present (it deletes it at the end).
            # We can re-overlay once more to save a backup, or just let it go. Let's do a quick re-run of overlay for the backup!
            try:
                subprocess.run([
                    "python3", "cover_overlay_standard.py",
                    "--input", backup_base,
                    "--output", backup_cover,
                    "--title", title_escaped,
                    "--subtitle", subtitle_escaped
                ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                print(f"✓ Backed up premium titled cover to {backup_cover}")
            except Exception:
                pass
                
        else:
            print("❌ Error: publish_local_novel.py ran but did not confirm successful publication.")
            update_progress(novel_id, "failed_publishing_execution", error_msg="Publication confirmation not found in logs")
            sys.exit(1)
            
    except subprocess.CalledProcessError as e:
        print("❌ Error executing publish_local_novel.py:")
        print(e.stdout)
        print(e.stderr)
        update_progress(novel_id, "failed_publishing_execution", error_msg=e.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
