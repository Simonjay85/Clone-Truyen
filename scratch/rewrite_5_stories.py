#!/usr/bin/env python3
"""
Master script: Fetch chapters for stories 2217, 2238, 2249, 2190, 2052
Then save raw content for rewriting.
"""
import json
import os
import requests
import ftplib
import sys

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"
WP_URL = "https://doctieuthuyet.com"
SECRET = "ZEN_TRUYEN_2026_BYPASS"

UPDATE_PHP = """<?php
require_once('wp-load.php');
header('Content-Type: application/json');

$raw = file_get_contents('php://input');
$input = json_decode($raw, true);

if (!isset($input['secret']) || $input['secret'] !== 'ZEN_TRUYEN_2026_BYPASS') {
    echo json_encode(['error' => 'Unauthorized']);
    exit;
}

$action = $input['action'] ?? 'update_chapter';

if ($action === 'update_chapter') {
    $chapter_id = intval($input['chapter_id']);
    $new_title = sanitize_text_field($input['title'] ?? '');
    $new_content = wp_kses_post($input['content'] ?? '');
    
    $result = wp_update_post([
        'ID' => $chapter_id,
        'post_title' => $new_title,
        'post_content' => $new_content,
    ]);
    
    if (is_wp_error($result)) {
        echo json_encode(['error' => $result->get_error_message()]);
    } else {
        echo json_encode(['success' => true, 'chapter_id' => $chapter_id]);
    }
    
} elseif ($action === 'get_story_chapters') {
    $story_id = intval($input['story_id']);
    $chapters = get_posts([
        'post_type' => 'chuong',
        'meta_key' => '_truyen_id',
        'meta_value' => $story_id,
        'posts_per_page' => -1,
        'orderby' => 'date',
        'order' => 'ASC',
    ]);
    
    $result = [];
    foreach ($chapters as $c) {
        $result[] = [
            'id' => $c->ID,
            'title' => $c->post_title,
            'content' => $c->post_content,
            'word_count' => str_word_count(wp_strip_all_tags($c->post_content)),
        ];
    }
    echo json_encode(['success' => true, 'chapters' => $result], JSON_UNESCAPED_UNICODE);
    
} elseif ($action === 'update_story_title') {
    $story_id = intval($input['story_id']);
    $new_title = sanitize_text_field($input['title'] ?? '');
    $new_intro = wp_kses_post($input['intro'] ?? '');
    
    $data = ['ID' => $story_id];
    if ($new_title) $data['post_title'] = $new_title;
    if ($new_intro) $data['post_content'] = $new_intro;
    
    $result = wp_update_post($data);
    
    if (is_wp_error($result)) {
        echo json_encode(['error' => $result->get_error_message()]);
    } else {
        if (function_exists('litespeed_purge_all')) litespeed_purge_all();
        echo json_encode(['success' => true, 'story_id' => $story_id]);
    }
} elseif ($action === 'get_story_meta') {
    $story_id = intval($input['story_id']);
    $post = get_post($story_id);
    if ($post) {
        echo json_encode([
            'success' => true,
            'id' => $post->ID,
            'title' => $post->post_title,
            'content' => $post->post_content,
            'status' => $post->post_status,
        ], JSON_UNESCAPED_UNICODE);
    } else {
        echo json_encode(['error' => 'Story not found']);
    }
}
?>"""

def upload_helper():
    php_path = "/tmp/novel_editor.php"
    with open(php_path, "w") as f:
        f.write(UPDATE_PHP)
    ftp = ftplib.FTP(FTP_HOST, timeout=30)
    ftp.login(FTP_USER, FTP_PASS)
    with open(php_path, "rb") as f:
        ftp.storbinary("STOR novel_editor.php", f)
    ftp.quit()
    os.remove(php_path)
    print("✓ Uploaded novel_editor.php")

def remove_helper():
    try:
        ftp = ftplib.FTP(FTP_HOST, timeout=30)
        ftp.login(FTP_USER, FTP_PASS)
        ftp.delete("novel_editor.php")
        ftp.quit()
        print("✓ Deleted novel_editor.php from server")
    except Exception as e:
        print(f"Warning: Could not delete novel_editor.php: {e}")

def get_story_chapters(story_id):
    res = requests.post(f"{WP_URL}/novel_editor.php",
                       json={"secret": SECRET, "action": "get_story_chapters", "story_id": story_id},
                       timeout=60)
    return res.json()

def get_story_meta(story_id):
    res = requests.post(f"{WP_URL}/novel_editor.php",
                       json={"secret": SECRET, "action": "get_story_meta", "story_id": story_id},
                       timeout=30)
    return res.json()

def update_chapter(chapter_id, title, content):
    res = requests.post(f"{WP_URL}/novel_editor.php",
                       json={"secret": SECRET, "action": "update_chapter",
                             "chapter_id": chapter_id, "title": title, "content": content},
                       timeout=60)
    return res.json()

def update_story_meta(story_id, title=None, intro=None):
    payload = {"secret": SECRET, "action": "update_story_title", "story_id": story_id}
    if title: payload["title"] = title
    if intro: payload["intro"] = intro
    res = requests.post(f"{WP_URL}/novel_editor.php", json=payload, timeout=30)
    return res.json()

if __name__ == "__main__":
    story_ids = [2217, 2238, 2249, 2190, 2052]
    
    print("=== UPLOADING PHP HELPER ===")
    upload_helper()
    
    all_data = {}
    for sid in story_ids:
        print(f"\n=== FETCHING STORY {sid} ===")
        
        # Get story meta
        meta = get_story_meta(sid)
        print(f"  Meta: {json.dumps(meta, ensure_ascii=False)[:200]}")
        
        # Get chapters
        chaps = get_story_chapters(sid)
        if chaps.get("success"):
            count = len(chaps.get("chapters", []))
            print(f"  Chapters: {count}")
            for c in chaps.get("chapters", []):
                print(f"    [{c['id']}] {c['title']} ({c.get('word_count', '?')} words)")
        else:
            print(f"  Error: {chaps}")
        
        all_data[sid] = {
            "meta": meta,
            "chapters": chaps
        }
    
    # Save to file
    out_path = "/tmp/stories_raw.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(all_data, f, ensure_ascii=False, indent=2)
    print(f"\n✓ Saved raw data to {out_path}")
    
    print("\n=== REMOVING PHP HELPER ===")
    remove_helper()
