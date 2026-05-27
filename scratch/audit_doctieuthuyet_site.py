#!/usr/bin/env python3
import html
import json
import re
import textwrap
import time
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen

BASE = "https://doctieuthuyet.com"
OUT = Path("audit_toan_bo_truyen_doctieuthuyet_2026-05-24.md")
CACHE = Path("scratch/.audit_doctieuthuyet_cache.json")


class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []

    def handle_data(self, data):
        data = data.strip()
        if data:
            self.parts.append(data)

    def text(self):
        return normalize(" ".join(self.parts))


def fetch(url, retries=3):
    last = None
    for attempt in range(retries):
        try:
            req = Request(url, headers={"User-Agent": "CodexAudit/1.0"})
            with urlopen(req, timeout=15) as res:
                return res.read().decode("utf-8", "replace")
        except (HTTPError, URLError, TimeoutError) as exc:
            last = exc
            time.sleep(1 + attempt)
    raise RuntimeError(f"Fetch failed: {url}: {last}")


def fetch_json(url):
    return json.loads(fetch(url))


def strip_html(value):
    parser = TextExtractor()
    parser.feed(value or "")
    return parser.text()


def normalize(text):
    text = html.unescape(text or "")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def words(text):
    return re.findall(r"[0-9A-Za-zÀ-ỹ]+", text or "")


def word_count(text):
    return len(words(text))


def first_words(text, count=26):
    ws = words(text)
    return " ".join(ws[:count]) + ("..." if len(ws) > count else "")


def rest_all(kind, fields=None):
    items = []
    page = 1
    while True:
        url = f"{BASE}/wp-json/wp/v2/{kind}?per_page=100&page={page}"
        if fields:
            url += "&_fields=" + fields
        try:
            batch = fetch_json(url)
        except RuntimeError as exc:
            if "400" in str(exc) and page > 1:
                break
            raise
        if not batch:
            break
        items.extend(batch)
        if len(batch) < 100:
            break
        page += 1
    return items


def rest_detail(kind, item):
    url = f"{BASE}/wp-json/wp/v2/{kind}/{item['id']}?_fields=id,slug,link,title,content,excerpt,date,modified"
    return fetch_json(url)


def fill_details(kind, items):
    details = []
    with ThreadPoolExecutor(max_workers=10) as pool:
        futures = [pool.submit(rest_detail, kind, item) for item in items]
        for i, future in enumerate(as_completed(futures), start=1):
            details.append(future.result())
            if i % 100 == 0:
                print(f"Fetched {i}/{len(items)} {kind} details", flush=True)
    return details


def read_cache():
    if CACHE.exists():
        return json.loads(CACHE.read_text(encoding="utf-8"))
    return {}


def write_cache(data):
    CACHE.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")


def chapter_links_for_story(link):
    page = fetch(link)
    links = re.findall(r"https://doctieuthuyet\.com/chuong/[^\"'<>\s]+", page)
    seen = []
    for link in links:
        clean = link.split("#")[0].rstrip("/") + "/"
        if clean not in seen:
            seen.append(clean)
    return seen


def chapter_number(title):
    m = re.search(r"Chương\s+(\d+)", title, flags=re.I)
    return int(m.group(1)) if m else None


def title_slug(link):
    return urlparse(link).path.rstrip("/").split("/")[-1]


def sentence_count(text):
    return len([s for s in re.split(r"[.!?…]+|\n+", text) if s.strip()])


def flag_text(title, text):
    flags = []
    wc = word_count(text)
    if wc < 700:
        flags.append(f"ngắn ({wc} từ)")
    if wc > 3600:
        flags.append(f"rất dài ({wc} từ), nên tách nhịp")
    if re.search(r"Change Log|Self-Check|STATE UPDATE|Audit Report|JSON|```", text, re.I):
        flags.append("có dấu hiệu rò meta/quy trình")
    if re.search(r"&[a-z]+;|&#\d+;", text):
        flags.append("còn entity HTML trong text")
    if re.match(r"\s*Chương\s+\d+", text, re.I):
        flags.append("body có thể lặp lại tiêu đề chương")
    if text.count("Đồng thời") + text.count("đồng thời") >= 5:
        flags.append("lặp cụm 'đồng thời' nhiều")
    if len(re.findall(r"tuyệt đối|hoàn hảo|thần y|giáng thế|kinh thiên|chấn động", text, re.I)) >= 12:
        flags.append("cường điệu dày, nên hạ bớt để tăng thật")
    if len(re.findall(r"ngay lập tức|lập tức|chỉ trong|trong vòng chưa đầy", text, re.I)) >= 8:
        flags.append("giải quyết quá nhanh, thiếu lực cản")
    if sentence_count(text) < 12 and wc > 900:
        flags.append("câu/đoạn có thể quá dài")
    if len(title) > 90:
        flags.append("tên chương dài")
    return flags


def flag_group(flag):
    if flag.startswith("ngắn"):
        return "chương ngắn dưới 700 từ"
    if flag.startswith("rất dài"):
        return "chương rất dài"
    if "cường điệu" in flag:
        return "cường điệu dày"
    if "quá nhanh" in flag:
        return "giải quyết quá nhanh"
    if "đồng thời" in flag:
        return "lặp cụm 'đồng thời'"
    if "meta" in flag:
        return "rò meta/quy trình"
    if "entity HTML" in flag:
        return "entity HTML"
    if "tiêu đề" in flag:
        return "lặp hoặc dài tiêu đề"
    return flag


def intro_flags(title, intro):
    flags = []
    wc = word_count(intro)
    if not intro:
        flags.append("thiếu mô tả")
    if wc < 80:
        flags.append(f"mô tả hơi mỏng ({wc} từ)")
    if wc > 330:
        flags.append(f"mô tả dài ({wc} từ), nên cô lại")
    if len(title) > 95:
        flags.append("tên truyện rất dài, dễ vỡ layout/SEO")
    if re.search(r"Change Log|Self-Check|STATE UPDATE|Audit Report|JSON|```", intro, re.I):
        flags.append("mô tả có dấu hiệu rò meta")
    if len(re.findall(r"tỷ|nghìn tỷ|trăm tỷ|C03|Big 4|sắc lệnh|đóng dấu đỏ", intro, re.I)) >= 7:
        flags.append("mô tả nhồi nhiều tín hiệu quyền lực/tiền, cần chọn điểm nhấn")
    return flags


def main():
    cache = read_cache()
    story_index = rest_all("truyen", "id,slug,link,title,date,modified")
    chapter_index = rest_all("chuong", "id,slug,link,title,date,modified")
    print(f"Found {len(story_index)} stories and {len(chapter_index)} chapters", flush=True)
    cache_key = f"{len(story_index)}-{len(chapter_index)}"
    if cache.get("key") == cache_key:
        stories = cache["stories"]
        chapters = cache["chapters"]
        story_links_cache = cache.get("story_links", {})
        print("Loaded cached REST details", flush=True)
    else:
        stories = fill_details("truyen", story_index)
        chapters = fill_details("chuong", chapter_index)
        story_links_cache = {}
        write_cache({"key": cache_key, "stories": stories, "chapters": chapters, "story_links": story_links_cache})
    chapter_by_link = {item["link"].rstrip("/") + "/": item for item in chapters}
    chapter_by_slug = {item["slug"]: item for item in chapters}

    story_infos = []
    missing_chapter_links = []
    all_story_chapter_links = set()

    missing_link_stories = [s for s in stories if s["link"] not in story_links_cache]
    if missing_link_stories:
        print(f"Fetching chapter lists for {len(missing_link_stories)} story pages", flush=True)
        with ThreadPoolExecutor(max_workers=12) as pool:
            futures = {pool.submit(chapter_links_for_story, s["link"]): s for s in missing_link_stories}
            for i, future in enumerate(as_completed(futures), start=1):
                story = futures[future]
                story_links_cache[story["link"]] = future.result()
                if i % 20 == 0:
                    print(f"Fetched {i}/{len(missing_link_stories)} story chapter lists", flush=True)
        write_cache({"key": cache_key, "stories": stories, "chapters": chapters, "story_links": story_links_cache})

    for story in stories:
        title = strip_html(story["title"]["rendered"])
        intro = strip_html(story.get("content", {}).get("rendered", ""))
        links = story_links_cache.get(story["link"], [])
        mapped = []
        for link in links:
            item = chapter_by_link.get(link) or chapter_by_slug.get(title_slug(link))
            if item:
                mapped.append(item)
                all_story_chapter_links.add(item["link"].rstrip("/") + "/")
            else:
                missing_chapter_links.append(link)
        mapped = sorted(mapped, key=lambda c: (chapter_number(strip_html(c["title"]["rendered"])) or 9999, c["date"]))
        story_infos.append({"story": story, "title": title, "intro": intro, "chapters": mapped})

    orphan_chapters = [
        c for c in chapters if c["link"].rstrip("/") + "/" not in all_story_chapter_links
    ]

    lines = []
    now = datetime.now(timezone.utc).astimezone().strftime("%Y-%m-%d %H:%M:%S %Z")
    lines.append("# Audit toàn bộ truyện doctieuthuyet.com")
    lines.append("")
    lines.append(f"- Thời điểm audit: {now}")
    lines.append(f"- Nguồn đọc: `{BASE}/wp-json/wp/v2/truyen`, `{BASE}/wp-json/wp/v2/chuong`, trang HTML từng truyện để map danh sách chương.")
    lines.append(f"- Phạm vi: {len(stories)} truyện public, {len(chapters)} chương public trong REST API.")
    lines.append(f"- Ghi chú: đây là audit biên tập tự động có đọc text từng mô tả/chương và bắt lỗi bằng rule nội dung; các mục bị flag nặng nên được đọc lại thủ công trước khi sửa live.")
    lines.append("")

    story_issue_count = 0
    chapter_issue_count = 0
    flag_counter = Counter()
    per_story_flags = defaultdict(int)

    lines.append("## Tóm tắt nhanh")
    lines.append("")
    for info in story_infos:
        nums = [chapter_number(strip_html(c["title"]["rendered"])) for c in info["chapters"]]
        nums_clean = [n for n in nums if n is not None]
        gaps = []
        if nums_clean:
            expected = set(range(min(nums_clean), max(nums_clean) + 1))
            gaps = sorted(expected - set(nums_clean))
        duplicates = [n for n, count in Counter(nums_clean).items() if count > 1]
        flags = intro_flags(info["title"], info["intro"])
        if gaps:
            flags.append("thiếu số chương: " + ", ".join(map(str, gaps)))
        if duplicates:
            flags.append("trùng số chương: " + ", ".join(map(str, duplicates)))
        if flags:
            story_issue_count += 1
        lines.append(f"- **{info['title']}**: {len(info['chapters'])} chương, mô tả {word_count(info['intro'])} từ. " + ("Cần xem: " + "; ".join(flags) if flags else "Ổn ở mức tổng quan."))

    lines.append("")
    lines.append("## Việc nên sửa ưu tiên")
    lines.append("")
    lines.append("1. Rút gọn các tên truyện quá dài để tránh vỡ UI và tăng CTR: giữ motif vả mặt nhưng bỏ bớt cụm giải thích kỹ thuật trong title.")
    lines.append("2. Giảm các đoạn giải quyết quá nhanh ở chương cuối/cao trào: thêm lực cản, phản đòn hụt, chứng cứ bị nghi ngờ hoặc chi phí nhỏ cho nhân vật chính.")
    lines.append("3. Hạ mật độ cụm cường điệu như “tuyệt đối”, “thần y”, “kinh thiên”, “giáng thế” ở những chương bị flag; thay bằng hành động/chứng cứ cụ thể.")
    lines.append("4. Dọn các chương ngắn hoặc mất nhịp bằng cách bổ sung cảnh chuyển tiếp, cảm xúc sau va chạm, và hậu quả thực tế.")
    lines.append("")

    lines.append("## Chi tiết từng truyện")
    lines.append("")

    for info in story_infos:
        story = info["story"]
        title = info["title"]
        intro = info["intro"]
        intro_issue = intro_flags(title, intro)
        lines.append(f"### {title}")
        lines.append("")
        lines.append(f"- Link: {story['link']}")
        lines.append(f"- Mô tả: {word_count(intro)} từ. " + ("Cần sửa: " + "; ".join(intro_issue) if intro_issue else "Ổn."))
        lines.append(f"- Mở đầu mô tả: {first_words(intro, 42)}")
        lines.append("")
        lines.append("| Chương | Số từ | Nhận xét cần sửa | Mở đầu để nhận diện |")
        lines.append("|---:|---:|---|---|")

        for c in info["chapters"]:
            ctitle = strip_html(c["title"]["rendered"])
            text = strip_html(c.get("content", {}).get("rendered", ""))
            flags = flag_text(ctitle, text)
            for f in flags:
                flag_counter[flag_group(f)] += 1
            if flags:
                chapter_issue_count += 1
                per_story_flags[title] += len(flags)
            num = chapter_number(ctitle) or ""
            safe_flags = "; ".join(flags) if flags else "Ổn"
            sample = first_words(text, 24)
            lines.append(f"| {num} | {word_count(text)} | {safe_flags} | {sample} |")
        lines.append("")

    if orphan_chapters:
        lines.append("## Chương chưa map được vào trang truyện")
        lines.append("")
        lines.append("Các chương dưới đây có trong REST API nhưng không thấy trong danh sách chương của 6 trang truyện public. Nên kiểm tra parent/post meta hoặc truyện bị ẩn.")
        lines.append("")
        for c in sorted(orphan_chapters, key=lambda x: x["date"], reverse=True):
            title = strip_html(c["title"]["rendered"])
            text = strip_html(c.get("content", {}).get("rendered", ""))
            flags = flag_text(title, text)
            lines.append(f"- {title} ({word_count(text)} từ): {c['link']} " + (f"==> {'; '.join(flags)}" if flags else ""))
        lines.append("")

    if missing_chapter_links:
        lines.append("## Link chương trên trang truyện nhưng không đọc được qua REST")
        lines.append("")
        for link in missing_chapter_links:
            lines.append(f"- {link}")
        lines.append("")

    lines.append("## Thống kê lỗi")
    lines.append("")
    lines.append(f"- Truyện có vấn đề ở mô tả/thứ tự: {story_issue_count}/{len(stories)}")
    lines.append(f"- Chương bị flag: {chapter_issue_count}/{len(chapters)}")
    lines.append("- Nhóm lỗi phổ biến:")
    for flag, count in flag_counter.most_common(20):
        lines.append(f"  - {flag}: {count} chương")
    lines.append("")
    lines.append("## Gợi ý biên tập theo truyện")
    lines.append("")
    for title, count in sorted(per_story_flags.items(), key=lambda x: x[1], reverse=True):
        lines.append(f"- **{title}**: {count} flag nội dung. Ưu tiên đọc lại các chương trong bảng có nhiều nhận xét, nhất là nơi bị cường điệu/giải quyết quá nhanh.")
    lines.append("")

    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUT} with {len(stories)} stories, {len(chapters)} chapters, {chapter_issue_count} flagged chapters.")


if __name__ == "__main__":
    main()
