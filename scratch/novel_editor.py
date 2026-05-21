#!/usr/bin/env python3
"""
Novel Update Script - Updates a published novel's chapters via WordPress API
Used by the orchestrator after review to fix sub-standard chapters.
"""
import json
import os
import requests
import ftplib

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
} elseif ($action === 'update_story_cover') {
    $story_id = intval($input['story_id']);
    $cover_url = esc_url_raw($input['cover_url']);
    if (!empty($cover_url)) {
        require_once(ABSPATH . 'wp-admin/includes/image.php');
        require_once(ABSPATH . 'wp-admin/includes/file.php');
        require_once(ABSPATH . 'wp-admin/includes/media.php');
        $tmp = download_url($cover_url, 45);
        if (!is_wp_error($tmp)) {
            $file_array = array('name' => 'cover-' . $story_id . '-upd-' . rand(100, 999) . '.jpg', 'tmp_name' => $tmp);
            $attach_id = media_handle_sideload($file_array, $story_id);
            if (!is_wp_error($attach_id)) {
                $old = get_post_thumbnail_id($story_id);
                if ($old) wp_delete_attachment($old, true);
                set_post_thumbnail($story_id, $attach_id);
                echo json_encode(['success' => true]);
            } else {
                echo json_encode(['error' => $attach_id->get_error_message()]);
                @unlink($tmp);
            }
        } else {
            echo json_encode(['error' => $tmp->get_error_message()]);
        }
    } else {
        echo json_encode(['error' => 'Missing cover_url']);
    }
}
?>"""

def upload_helper():
    """Upload the PHP helper to server."""
    with open("novel_editor.php", "w") as f:
        f.write(UPDATE_PHP)
    ftp = ftplib.FTP(FTP_HOST, timeout=30)
    ftp.login(FTP_USER, FTP_PASS)
    with open("novel_editor.php", "rb") as f:
        ftp.storbinary("STOR novel_editor.php", f)
    ftp.quit()
    os.remove("novel_editor.php")
    print("✓ Uploaded novel_editor.php")

def remove_helper():
    """Remove the PHP helper from server."""
    try:
        ftp = ftplib.FTP(FTP_HOST, timeout=30)
        ftp.login(FTP_USER, FTP_PASS)
        ftp.delete("novel_editor.php")
        ftp.quit()
        print("✓ Deleted novel_editor.php from server")
    except:
        pass

def get_story_chapters(story_id):
    """Fetch chapters for a story."""
    res = requests.post(f"{WP_URL}/novel_editor.php",
                       json={"secret": SECRET, "action": "get_story_chapters", "story_id": story_id},
                       timeout=30)
    return res.json()

def update_chapter(chapter_id, title, content):
    """Update a chapter's content."""
    res = requests.post(f"{WP_URL}/novel_editor.php",
                       json={"secret": SECRET, "action": "update_chapter",
                             "chapter_id": chapter_id, "title": title, "content": content},
                       timeout=30)
    return res.json()

def update_story_meta(story_id, title=None, intro=None):
    """Update story title/intro."""
    payload = {"secret": SECRET, "action": "update_story_title", "story_id": story_id}
    if title: payload["title"] = title
    if intro: payload["intro"] = intro
    res = requests.post(f"{WP_URL}/novel_editor.php", json=payload, timeout=30)
    return res.json()

def update_story_cover(story_id, cover_url):
    """Update story cover image."""
    payload = {"secret": SECRET, "action": "update_story_cover", "story_id": story_id, "cover_url": cover_url}
    res = requests.post(f"{WP_URL}/novel_editor.php", json=payload, timeout=120)
    return res.json()

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        story_id = int(sys.argv[1])
        upload_helper()
        result = get_story_chapters(story_id)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        remove_helper()
