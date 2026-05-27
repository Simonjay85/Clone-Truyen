"""
run_all_fixes.py
Orchestrate toàn bộ fixes từ báo cáo đánh giá danh_gia_truyen_2025-05-25.md
"""

import ftplib
import requests
import json
import time
import re
import anthropic

# ─── CONFIG ──────────────────────────────────────────────────────────────────
FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"
WP_URL   = "https://doctieuthuyet.com"
SECRET   = "ZEN_TRUYEN_2026_BYPASS"

OPENAI_KEY = "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"
# Claude API key lấy từ env var ANTHROPIC_API_KEY (tự động có trong Claude Code)
import os
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")

# Thông tin truyện có chương trùng cần viết lại
NOVELS_WITH_DUP_CHAPTERS = {
    2497: {
        "title": "Công Thức Thuốc Bị Cướp: Bẫy IPO Dược Phẩm Nghìn Tỷ",
        "male_lead": "Nguyễn Đức Trí",
        "context": "Dược sĩ tài năng ở Đà Lạt bị sếp cướp công thức thuốc chữa gan, bị đuổi khỏi lab. Anh phải lật tẩy âm mưu IPO nghìn tỷ của kẻ đã cướp công trình của mình.",
        "dup_chapters": [2, 3, 4, 6, 7],  # index 0-based
    },
    2313: {
        "title": "Cướp Mã Nguồn Nghìn Tỷ, Kích Hoạt Bẫy Chôn Vùi Tập Đoàn",
        "male_lead": "Đức",
        "context": "Lập trình viên thiên tài bị đồng nghiệp và sếp cướp mã nguồn, bị đuổi khỏi công ty. Anh kích hoạt bẫy tinh vi để phá sập tập đoàn kẻ phản bội.",
        "dup_chapters": [6],  # index 0-based (chương 7 là index 6)
    },
    2658: {
        "title": "Chàng Rể Ngọc Linh Lật Kèo Cứu Bị Cướp",
        "male_lead": "Trần Hoàng Vũ",
        "context": "Chàng rể ở vùng rừng núi Ngọc Linh bị băng đảng cướp sâm quý, bị khinh rẻ là kẻ nghèo hèn. Anh dùng mưu trí lật kèo, phá bẫy và lấy lại danh dự.",
        "dup_chapters": [],  # sẽ xác định sau khi fetch
    },
    3940: {
        "title": "Họ Gọi Tôi Là Lang Băm, Đến Khi Cả Hội Thảo Quỳ Xin Tôi Cứu Mạng",
        "male_lead": "Lâm",
        "context": "Thầy thuốc đông y bị viện phổi đuổi, bị gọi là lang băm. Trong hội thảo y tế quốc tế, anh cứu cả khán phòng khỏi khủng hoảng bằng kiến thức đông y gia truyền.",
        "remove_dup_paragraphs": True,  # chỉ xóa đoạn lặp, không viết lại
        "dup_chapters": [0],  # chương 1 (index 0) có đoạn lặp
    },
}

def log(msg):
    print(msg)

# ─── FTP HELPERS ─────────────────────────────────────────────────────────────
def ftp_upload(local_path, remote_name):
    log(f"  [FTP] Uploading {remote_name}...")
    ftp = ftplib.FTP(FTP_HOST, timeout=30)
    ftp.login(FTP_USER, FTP_PASS)
    with open(local_path, "rb") as f:
        ftp.storbinary(f"STOR {remote_name}", f)
    ftp.quit()
    log(f"  [FTP] Uploaded OK: {remote_name}")

def ftp_delete(remote_name):
    try:
        ftp = ftplib.FTP(FTP_HOST, timeout=30)
        ftp.login(FTP_USER, FTP_PASS)
        ftp.delete(remote_name)
        ftp.quit()
        log(f"  [FTP] Deleted remote: {remote_name}")
    except Exception as e:
        log(f"  [FTP] Warning: could not delete {remote_name}: {e}")

def call_php(endpoint, payload, timeout=120):
    url = f"{WP_URL}/{endpoint}"
    payload["secret_token"] = SECRET
    res = requests.post(url, json=payload, timeout=timeout)
    if res.status_code != 200:
        raise Exception(f"HTTP {res.status_code}: {res.text[:500]}")
    return res.json()

# ─── STEP 1: Simple fixes + unpublish V1 ─────────────────────────────────────
def run_simple_fixes():
    log("\n" + "="*60)
    log("STEP 1: Simple fixes (titles, excerpts, unpublish V1)")
    log("="*60)

    local_php = "/Users/aaronnguyen/TN/App/doctieuthuyet/fix_simple_issues.php"
    remote_php = "fix_simple_issues.php"

    ftp_upload(local_php, remote_php)
    time.sleep(1)

    try:
        result = call_php(remote_php, {})
        log(f"  Result: {json.dumps(result, ensure_ascii=False, indent=2)}")
        return result.get("success", False)
    finally:
        ftp_delete(remote_php)

# ─── STEP 2: Fetch chapter info từ live site ─────────────────────────────────
def upload_chapter_php():
    local_php = "/Users/aaronnguyen/TN/App/doctieuthuyet/fix_chapter_content.php"
    ftp_upload(local_php, "fix_chapter_content.php")
    time.sleep(1)

def get_chapters(truyen_id):
    result = call_php("fix_chapter_content.php", {"action": "get_chapters", "truyen_id": truyen_id})
    return result.get("chapters", [])

# ─── STEP 3: Dùng Claude API viết lại chương trùng ──────────────────────────
def generate_chapter_content(novel_info, chapter_title, chapter_index, prev_chapters_summary):
    """Dùng Claude API tạo nội dung chương mới độc đáo."""
    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

    system_prompt = """Bạn là nhà văn chuyên viết truyện sảng văn Việt Nam.
Hãy viết nội dung chương truyện theo phong cách: kịch tính, hành động nhanh, cảm xúc mạnh, nhân vật nam chính thể hiện tài năng/bản lĩnh.
Văn phong: câu ngắn, súc tích, có đối thoại. Độ dài: 800-1200 từ. Không dùng ký tự đặc biệt ngoài dấu câu cơ bản."""

    user_prompt = f"""Viết nội dung Chương {chapter_index + 1} cho truyện: "{novel_info['title']}"

Thông tin truyện:
- Nam chính: {novel_info['male_lead']}
- Cốt truyện: {novel_info['context']}
- Tên chương cần viết: "{chapter_title}"
- Vị trí: Chương {chapter_index + 1} trong câu chuyện
{f'- Tóm tắt diễn biến trước đó: {prev_chapters_summary}' if prev_chapters_summary else ''}

Yêu cầu:
- Nội dung phải TIẾP NỐI hợp lý với diễn biến trước
- Phù hợp với tên chương "{chapter_title}"
- Kết thúc chương phải tạo hứng thú để đọc tiếp
- Định dạng: văn xuôi với đoạn văn bình thường, có thẻ <p>...</p> bao mỗi đoạn

Chỉ xuất nội dung chương, không có tiêu đề, không có giải thích."""

    message = client.messages.create(
        model="claude-opus-4-7",
        max_tokens=2000,
        messages=[{"role": "user", "content": user_prompt}],
        system=system_prompt,
    )

    content = message.content[0].text

    # Wrap thành HTML nếu chưa có thẻ <p>
    if "<p>" not in content:
        paragraphs = [p.strip() for p in content.split("\n\n") if p.strip()]
        content = "\n".join(f"<p>{p}</p>" for p in paragraphs)

    return content


def fix_duplicate_paragraphs_in_chapter(chapter_content):
    """Xóa đoạn văn bị lặp lại trong chương."""
    # Tách thành các đoạn
    paragraphs = re.split(r'</p>\s*<p>|<br\s*/?>|\n\n+', chapter_content)
    paragraphs = [p.strip() for p in paragraphs if p.strip()]

    seen = {}
    unique_paragraphs = []
    for p in paragraphs:
        # Normalize để so sánh (bỏ HTML tags, lowercase)
        normalized = re.sub(r'<[^>]+>', '', p).lower().strip()
        if len(normalized) < 30:
            unique_paragraphs.append(p)
            continue
        # Dùng 100 ký tự đầu làm key
        key = normalized[:100]
        if key not in seen:
            seen[key] = True
            unique_paragraphs.append(p)

    return "\n".join(f"<p>{p}</p>" if not p.startswith("<") else p for p in unique_paragraphs)


def update_chapter(chapter_id, new_content, new_title=None):
    payload = {
        "action": "update_chapter",
        "chapter_id": chapter_id,
        "content": new_content,
    }
    if new_title:
        payload["title"] = new_title
    return call_php("fix_chapter_content.php", payload)


def run_chapter_fixes():
    log("\n" + "="*60)
    log("STEP 2+3: Fetch chapters & fix duplicate content")
    log("="*60)

    # Upload PHP helper
    upload_chapter_php()

    for truyen_id, novel_info in NOVELS_WITH_DUP_CHAPTERS.items():
        log(f"\n--- Processing ID {truyen_id}: {novel_info['title']} ---")

        chapters = get_chapters(truyen_id)
        if not chapters:
            log(f"  WARNING: No chapters found for ID {truyen_id}")
            continue

        log(f"  Found {len(chapters)} chapters")

        # ── Truyện 3940: Chỉ xóa đoạn lặp trong chương 1 ──
        if novel_info.get("remove_dup_paragraphs"):
            ch0 = chapters[0]
            log(f"  Fetching full content of Ch1 (ID {ch0['id']}) to remove dup paragraphs...")
            # Lấy full content qua API (preview đã có)
            # Chúng ta cần fetch full HTML từ site
            ch_url = f"{WP_URL}/wp-json/wp/v2/chuong/{ch0['id']}?_fields=content"
            r = requests.get(ch_url, timeout=30)
            if r.status_code == 200:
                full_content = r.json().get("content", {}).get("rendered", "")
                fixed = fix_duplicate_paragraphs_in_chapter(full_content)
                res = update_chapter(ch0['id'], fixed)
                log(f"  Fixed dup paragraphs in Ch1: {res}")
            else:
                log(f"  Could not fetch full content: HTTP {r.status_code}")
            continue

        # ── Các truyện khác: phát hiện và viết lại chương trùng ──
        if not chapters:
            continue

        # Tìm chương trùng bằng content_hash
        hash_count = {}
        for ch in chapters:
            h = ch["content_hash"]
            hash_count[h] = hash_count.get(h, 0) + 1

        dup_hashes = {h for h, cnt in hash_count.items() if cnt > 1}

        # Chương đầu tiên (index 0) là chương gốc, các chương khác trùng cần viết lại
        first_hash = chapters[0]["content_hash"] if chapters else None

        # Xác định chương cần viết lại
        chapters_to_fix = []
        if novel_info["dup_chapters"]:
            # Dùng index cụ thể từ báo cáo
            for idx in novel_info["dup_chapters"]:
                if idx < len(chapters):
                    chapters_to_fix.append((idx, chapters[idx]))
        else:
            # Tự phát hiện
            for i, ch in enumerate(chapters):
                if i > 0 and ch["content_hash"] in dup_hashes:
                    chapters_to_fix.append((i, ch))

        if not chapters_to_fix:
            log(f"  No duplicate chapters detected (or already fixed)")
            continue

        ch_labels = [f"Ch{i+1} (ID {ch['id']})" for i, ch in chapters_to_fix]
        log(f"  Chapters to rewrite: {ch_labels}")

        # Tạo tóm tắt context từ các chương trước
        prev_summary = ""
        for idx, chap in chapters_to_fix:
            log(f"  Generating content for Ch{idx+1}: '{chap['title']}'...")

            # Lấy tóm tắt từ chương trước đó (nếu có)
            if idx > 0 and idx - 1 < len(chapters):
                prev_ch = chapters[idx - 1]
                prev_summary = f"Chương {idx}: {prev_ch['title']} - {prev_ch['content_preview'][:150]}"

            new_content = generate_chapter_content(novel_info, chap["title"], idx, prev_summary)
            log(f"  Generated {len(new_content)} chars. Updating chapter ID {chap['id']}...")

            res = update_chapter(chap["id"], new_content)
            log(f"  Update result: {res}")
            time.sleep(2)  # Rate limit

    # Cleanup PHP
    ftp_delete("fix_chapter_content.php")
    log("\nChapter fixes done.")


# ─── MAIN ────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    import sys

    steps = sys.argv[1:] if len(sys.argv) > 1 else ["simple", "chapters"]

    if "simple" in steps:
        ok = run_simple_fixes()
        if ok:
            log("\n✅ Simple fixes applied successfully.")
        else:
            log("\n❌ Simple fixes had errors, check log above.")

        # Fix repeated paragraphs in ID 3940 Ch1
        log("\n--- Fixing repeated paragraphs in ID 3940 Ch1 ---")
        php_3940 = "/Users/aaronnguyen/TN/App/doctieuthuyet/fix_3940.php"
        if os.path.exists(php_3940):
            try:
                ftp_upload(php_3940, "fix_3940.php")
                time.sleep(1)
                r3940 = call_php("fix_3940.php", {})
                log(f"  Result: {json.dumps(r3940, ensure_ascii=False)}")
                ftp_delete("fix_3940.php")
                log("  ✅ ID 3940 Ch1 dedup done")
            except Exception as e:
                log(f"  ❌ Error: {e}")
                ftp_delete("fix_3940.php")

        # Also run duplicate chapter content fix
        log("\n--- Running duplicate chapter content fix ---")
        chapter_json = "/Users/aaronnguyen/TN/App/doctieuthuyet/chapter_updates.json"
        php_local = "/Users/aaronnguyen/TN/App/doctieuthuyet/fix_dup_chapters.php"
        if os.path.exists(chapter_json) and os.path.exists(php_local):
            try:
                with open(chapter_json, encoding="utf-8") as f:
                    updates = json.load(f)
                log(f"  Loaded {len(updates)} chapter updates")
                ftp_upload(php_local, "fix_dup_chapters.php")
                time.sleep(2)
                result = call_php("fix_dup_chapters.php", {"updates": updates})
                log(f"  Result: {json.dumps(result, ensure_ascii=False, indent=2)}")
                ftp_delete("fix_dup_chapters.php")
                log("  ✅ Chapter content fix done")
            except Exception as e:
                log(f"  ❌ Chapter fix error: {e}")
                ftp_delete("fix_dup_chapters.php")
        else:
            log("  Skipping: chapter_updates.json or fix_dup_chapters.php not found")

    if "fix3849" in steps:
        # Fix </p>n<p> pattern in ID 3849
        import ftplib, time as _time
        log("\nFixing ID 3849 stray n character...")
        ftp_upload("/Users/aaronnguyen/TN/App/doctieuthuyet/fix_3849.php", "fix_3849.php")
        _time.sleep(2)
        try:
            r = call_php("fix_3849.php", {})
            log(f"  Result: {json.dumps(r, ensure_ascii=False)}")
        finally:
            ftp_delete("fix_3849.php")

    if "chapters" in steps:
        run_chapter_fixes()
        log("\n✅ Chapter content fixes done.")

    log("\n🎉 All fixes complete.")
