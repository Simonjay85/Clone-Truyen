#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import ftplib
import html
import json
import random
import re
import time
from pathlib import Path

import requests

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"
WP_URL = "https://doctieuthuyet.com"
SECRET = "ZEN_CONTEXT_COMMENTS_2026"

ROOT = Path(__file__).resolve().parents[1]
HELPER_LOCAL = ROOT / "scratch" / "contextual_comments_helper.php"

HELPER_PHP = r"""<?php
require_once('wp-load.php');
header('Content-Type: application/json; charset=utf-8');

$raw = file_get_contents('php://input');
$input = json_decode($raw, true);

if (!isset($input['secret']) || $input['secret'] !== 'ZEN_CONTEXT_COMMENTS_2026') {
    http_response_code(403);
    echo json_encode(['error' => 'Unauthorized']);
    exit;
}

$action = $input['action'] ?? '';

if ($action === 'list_stories') {
    $q = new WP_Query([
        'post_type' => 'truyen',
        'post_status' => 'publish',
        'posts_per_page' => -1,
        'orderby' => 'ID',
        'order' => 'ASC',
    ]);
    $stories = [];
    foreach ($q->posts as $p) {
        $terms = wp_get_post_terms($p->ID, 'the_loai', ['fields' => 'names']);
        if (is_wp_error($terms)) $terms = [];
        $chapters = get_posts([
            'post_type' => 'chuong',
            'post_status' => 'publish',
            'meta_key' => '_truyen_id',
            'meta_value' => $p->ID,
            'posts_per_page' => 4,
            'orderby' => 'date',
            'order' => 'ASC',
        ]);
        $chapter_titles = [];
        foreach ($chapters as $c) {
            $chapter_titles[] = $c->post_title;
        }
        $stories[] = [
            'id' => $p->ID,
            'title' => get_the_title($p->ID),
            'intro' => wp_strip_all_tags($p->post_content),
            'genres' => $terms,
            'chapter_titles' => $chapter_titles,
            'comment_count' => get_comments_number($p->ID),
        ];
    }
    echo json_encode(['success' => true, 'stories' => $stories], JSON_UNESCAPED_UNICODE);
    exit;
}

if ($action === 'replace_comments') {
    $post_id = intval($input['post_id'] ?? 0);
    $comments = $input['comments'] ?? [];
    if (!$post_id || !is_array($comments)) {
        echo json_encode(['error' => 'Missing post_id/comments']);
        exit;
    }

    $old_comments = get_comments([
        'post_id' => $post_id,
        'status' => 'all',
        'type' => 'comment',
    ]);
    foreach ($old_comments as $c) {
        wp_delete_comment($c->comment_ID, true);
    }

    $inserted = 0;
    foreach ($comments as $idx => $c) {
        $author = sanitize_text_field($c['author'] ?? 'Độc giả');
        $content = sanitize_textarea_field($c['content'] ?? '');
        $rating = intval($c['rating'] ?? 5);
        $days_ago = intval($c['days_ago'] ?? ($idx + 1));
        if ($content === '') continue;
        $comment_id = wp_insert_comment([
            'comment_post_ID' => $post_id,
            'comment_author' => $author,
            'comment_author_email' => sanitize_title($author) . $post_id . $idx . '@gmail.com',
            'comment_content' => $content,
            'comment_type' => 'comment',
            'comment_parent' => 0,
            'comment_approved' => 1,
            'comment_date' => date('Y-m-d H:i:s', current_time('timestamp') - ($days_ago * DAY_IN_SECONDS) - ($idx * HOUR_IN_SECONDS)),
        ]);
        if ($comment_id) {
            update_comment_meta($comment_id, 'comment_rating', max(4, min(5, $rating)));
            $inserted++;
        }
    }
    clean_post_cache($post_id);
    if (function_exists('litespeed_purge_post')) litespeed_purge_post($post_id);
    echo json_encode(['success' => true, 'post_id' => $post_id, 'deleted' => count($old_comments), 'inserted' => $inserted], JSON_UNESCAPED_UNICODE);
    exit;
}

if ($action === 'purge') {
    if (function_exists('litespeed_purge_all')) litespeed_purge_all();
    echo json_encode(['success' => true]);
    exit;
}

echo json_encode(['error' => 'Unknown action']);
?>"""

NAMES = [
    "Bảo Lâm", "Bích Trâm", "Trọng Nghĩa", "Phan Khải", "Mai Anh", "Quốc Bảo",
    "Ngọc Diệp", "Minh Nhật", "Khánh Linh", "Hoàng Nam", "Thu Trang", "Đức Thịnh",
    "Cẩm Tú", "Tấn Đạt", "Thanh Hằng", "Minh An", "Tuyết Mai", "Đăng Khoa",
]

STOPWORDS = {
    "bị", "tôi", "là", "và", "của", "cho", "ngày", "một", "cả", "với", "khỏi",
    "thành", "trong", "ở", "để", "khi", "vì", "vào", "đã", "này", "kia", "lên",
}


def upload_helper():
    HELPER_LOCAL.write_text(HELPER_PHP, encoding="utf-8")
    ftp = ftplib.FTP(FTP_HOST, timeout=30)
    ftp.login(FTP_USER, FTP_PASS)
    with HELPER_LOCAL.open("rb") as f:
        ftp.storbinary("STOR contextual_comments_helper.php", f)
    ftp.quit()


def remove_helper():
    try:
        ftp = ftplib.FTP(FTP_HOST, timeout=30)
        ftp.login(FTP_USER, FTP_PASS)
        ftp.delete("contextual_comments_helper.php")
        ftp.quit()
    except Exception:
        pass
    try:
        HELPER_LOCAL.unlink()
    except FileNotFoundError:
        pass


def api(action, **payload):
    data = {"secret": SECRET, "action": action, **payload}
    r = requests.post(f"{WP_URL}/contextual_comments_helper.php", json=data, timeout=90)
    r.raise_for_status()
    return r.json()


def clean_text(text):
    text = html.unescape(text or "")
    text = re.sub(r"\s+", " ", text).strip()
    return text


def split_title(title):
    title = clean_text(title)
    if ":" in title:
        base, hook = title.split(":", 1)
        return base.strip(), hook.strip()
    parts = re.split(r"[,–—-]", title, 1)
    if len(parts) == 2 and len(parts[0]) > 8:
        return parts[0].strip(), parts[1].strip()
    return title, title


def pick_keywords(title, intro, genres):
    source = f"{title} {intro} {' '.join(genres or [])}".lower()
    words = re.findall(r"[a-zA-ZÀ-ỹ0-9]+", source)
    chunks = []
    for i, w in enumerate(words):
        if len(w) < 3 or w in STOPWORDS:
            continue
        if i + 1 < len(words):
            w2 = words[i + 1]
            if len(w2) >= 3 and w2 not in STOPWORDS:
                chunks.append(f"{w} {w2}")
        chunks.append(w)
    priority = [
        "căn nhà", "biệt thự", "camera giấu kín", "con gái chủ tịch",
        "tôm hùm", "sơn mài", "gốm sứ", "bát tràng", "phú yên", "vệ tinh",
        "đàn bầu", "mỏ", "địa chất", "trà", "đà lạt", "châm cứu", "lãn ông",
        "paychain", "hđqt", "nha trang", "kiểm toán", "phòng trà", "hàng giả",
        "buôn lậu", "vu oan", "phản bội", "thâu tóm", "nghìn tỷ",
    ]
    picked = []
    for p in priority:
        if p in source and p not in picked:
            picked.append(p)
    for c in chunks:
        if c not in picked and len(picked) < 5:
            picked.append(c)
    return picked[:5] or ["cú lật kèo", "bằng chứng"]


def generate_comments(story):
    title = clean_text(story["title"])
    intro = clean_text(story.get("intro", ""))
    source_lower = f"{title} {intro}".lower()
    genres = story.get("genres") or []
    chapters = [clean_text(x) for x in story.get("chapter_titles") or []]
    base, hook = split_title(title)
    short_hook = hook if len(hook) <= 82 else hook[:79].rstrip() + "..."
    kws = pick_keywords(title, intro, genres)
    main_kw = kws[0]
    second_kw = kws[1] if len(kws) > 1 else base
    first_chap = chapters[0] if chapters else ""
    genre = genres[0] if genres else "sảng văn"
    pressure = "bị vu oan" if "vu oan" in source_lower else ("bị cướp công" if "cướp" in source_lower else "bị xem thường")
    antagonist = "bọn vu oan" if "vu oan" in source_lower else ("người cướp công" if "cướp" in source_lower else "những người khinh thường")

    templates = [
        f"Đọc tên truyện đã thấy đúng gu: {short_hook}. Cú bị dồn vào đường cùng rồi dùng bằng chứng bật lại rất đã.",
        f"Phần {main_kw} viết có chất riêng, không phải kiểu vả mặt nói miệng. Mình thích nhất cảm giác nhân vật chính càng bị ép càng tỉnh.",
        f"{base} nghe tưởng đơn giản mà vào truyện căng thật. Mấy đoạn liên quan {second_kw} làm mình đọc liền mấy chương.",
        f"Thích cách truyện bám vào vụ {short_hook.lower()}, có mâu thuẫn rõ nên lúc phản công mới sướng.",
        f"Nếu ai thích {genre} kiểu có nghề, có chứng cứ, có cú lật mặt trước đám đông thì bộ này hợp lắm.",
        f"Đoạn đầu dựng mâu thuẫn chắc, nhân vật chính không thắng dễ. Càng đọc càng muốn xem {antagonist} phải trả giá.",
        f"Chi tiết {main_kw} làm bối cảnh truyện khác hẳn mấy bộ chung chung. Có cảm giác tác giả có tìm hiểu thật.",
        f"Không ngờ chủ đề {second_kw} mà viết thành sảng văn cuốn vậy. Vừa tức thay nhân vật chính vừa hóng màn phản đòn.",
        f"Đọc tới mấy cảnh bị khinh thường mới thấy cú thâu tóm phía sau đã. Vả mặt phải có nền đau như vậy mới ngấm.",
        f"Điểm mình thích là truyện không chỉ hô khẩu hiệu cho kêu, mà có mâu thuẫn cụ thể và cách gỡ từng lớp.",
        f"{first_chap} mở khá bắt. Hy vọng các chương sau giữ nhịp căng như phần giới thiệu.",
        f"Nhân vật phản diện trong vụ {short_hook.lower()} đọc mà bực thật, nhưng càng bực thì đoạn lật kèo càng đáng chờ.",
        f"Bộ này nên đọc từ đầu để thấy quá trình nhân vật chính {pressure} rồi mới bật lên, đọc lẻ chương sẽ không đã bằng.",
    ]

    rng = random.Random(story["id"])
    rng.shuffle(templates)
    comments = []
    for i, text in enumerate(templates[:13]):
        author = NAMES[(story["id"] + i * 5) % len(NAMES)]
        comments.append({
            "author": author,
            "content": text,
            "rating": 4 if i in (6, 11) else 5,
            "days_ago": 3 + ((story["id"] + i * 7) % 60),
        })
    return comments


def main():
    upload_helper()
    try:
        stories = api("list_stories")["stories"]
        print(f"Found {len(stories)} stories")
        total_inserted = 0
        sample = []
        for idx, story in enumerate(stories, 1):
            comments = generate_comments(story)
            res = api("replace_comments", post_id=story["id"], comments=comments)
            total_inserted += res.get("inserted", 0)
            if len(sample) < 5:
                sample.append({
                    "id": story["id"],
                    "title": story["title"],
                    "first_comment": comments[0]["content"],
                    "result": res,
                })
            print(f"[{idx}/{len(stories)}] {story['id']} inserted {res.get('inserted')} comments")
            time.sleep(0.05)
        api("purge")
        (ROOT / "scratch" / "contextual_comments_sample_20260531.json").write_text(
            json.dumps(sample, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        print(f"Done. Inserted {total_inserted} comments")
    finally:
        remove_helper()


if __name__ == "__main__":
    main()
