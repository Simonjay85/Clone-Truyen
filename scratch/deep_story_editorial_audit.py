#!/usr/bin/env python3
import importlib.util
import json
import re
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE_AUDIT = ROOT / "scratch" / "audit_doctieuthuyet_site.py"
OUT = ROOT / "de_xuat_sua_truyen_dat_10_10_2026-05-24.md"

spec = importlib.util.spec_from_file_location("base_audit", BASE_AUDIT)
base = importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)


def text(item):
    return base.strip_html(item.get("content", {}).get("rendered", ""))


def title(item):
    return base.strip_html(item["title"]["rendered"])


def wc(s):
    return base.word_count(s)


def sample(s, n=34):
    return base.first_words(s, n)


def chapter_num(item):
    return base.chapter_number(title(item)) or 9999


def terms_count(s, terms):
    return len(re.findall("|".join(terms), s, flags=re.I))


EVIDENCE_TERMS = [
    r"bằng sáng chế", r"hợp đồng", r"sao kê", r"camera", r"video", r"email",
    r"tin nhắn", r"ghi âm", r"mã nguồn", r"commit", r"log", r"kiểm toán",
    r"Big 4", r"C03", r"công an", r"thanh tra", r"giám định", r"xét nghiệm",
    r"chứng cứ", r"hồ sơ", r"con dấu", r"văn bản", r"sổ đỏ", r"di chúc",
]
RESISTANCE_TERMS = [
    r"đình chỉ", r"phong tỏa", r"đóng băng", r"khởi kiện", r"tố cáo",
    r"bôi nhọ", r"livestream", r"phản công", r"gài bẫy", r"đe dọa",
    r"tấn công", r"cấm", r"tịch thu", r"phản bội", r"quay lưng",
]
ENDING_TERMS = [
    r"bị bắt", r"còng tay", r"khởi tố", r"phán quyết", r"xin lỗi",
    r"sụp đổ", r"phá sản", r"tương lai", r"bình minh", r"công lý",
]
EMOTION_TERMS = [
    r"im lặng", r"nghẹn", r"run", r"nước mắt", r"thở", r"đau", r"xấu hổ",
    r"mẹ", r"cha", r"gia đình", r"ôm", r"nhìn", r"lặng",
]
GENERIC_TITLE_TERMS = [
    r"lật kèo", r"phản công", r"vạch trần", r"phán quyết", r"bí mật",
    r"chấn động", r"đế chế", r"cuộc chiến", r"đòn", r"sự thật",
]
TECH_OVERLOAD = [
    r"polymer", r"vi sinh", r"enzyme", r"blockchain", r"token", r"AI",
    r"API", r"thuật toán", r"IoT", r"server", r"mã nguồn",
]


def build_data():
    cache = base.read_cache()
    stories_idx = base.rest_all("truyen", "id,slug,link,title,date,modified")
    chapters_idx = base.rest_all("chuong", "id,slug,link,title,date,modified")
    key = f"{len(stories_idx)}-{len(chapters_idx)}"
    if cache.get("key") == key:
        stories = cache["stories"]
        chapters = cache["chapters"]
        story_links = cache.get("story_links", {})
    else:
        stories = base.fill_details("truyen", stories_idx)
        chapters = base.fill_details("chuong", chapters_idx)
        story_links = {}
        base.write_cache({"key": key, "stories": stories, "chapters": chapters, "story_links": story_links})
    if len(story_links) < len(stories):
        missing = [s for s in stories if s["link"] not in story_links]
        with ThreadPoolExecutor(max_workers=12) as pool:
            futures = {pool.submit(base.chapter_links_for_story, s["link"]): s for s in missing}
            for i, future in enumerate(as_completed(futures), start=1):
                s = futures[future]
                story_links[s["link"]] = future.result()
                if i % 20 == 0:
                    print(f"Fetched {i}/{len(missing)} story chapter lists", flush=True)
        base.write_cache({"key": key, "stories": stories, "chapters": chapters, "story_links": story_links})
    by_link = {c["link"].rstrip("/") + "/": c for c in chapters}
    by_slug = {c["slug"]: c for c in chapters}
    infos = []
    for story in stories:
        mapped = []
        for link in story_links.get(story["link"], []):
            clean = link.rstrip("/") + "/"
            item = by_link.get(clean) or by_slug.get(base.title_slug(clean))
            if item:
                mapped.append(item)
        mapped = sorted(dict((c["id"], c) for c in mapped).values(), key=lambda c: (chapter_num(c), c["date"]))
        infos.append((story, mapped))
    return infos, chapters


def editorial_flags(story, chapters):
    stitle = title(story)
    intro = text(story)
    ch_texts = [text(c) for c in chapters]
    full = "\n".join(ch_texts)
    flags = []
    positives = []
    fixes = []

    if len(stitle) > 95:
        flags.append("Tên truyện quá dài, SEO/card dễ loãng.")
        fixes.append("Rút title còn 14-18 từ: giữ nhục ban đầu + cú lật + cái giá, bỏ bớt thuật ngữ phụ.")
    elif re.search(r":", stitle):
        positives.append("Tên có cấu trúc định vị rõ.")

    if wc(intro) < 100:
        flags.append("Mô tả hơi mỏng, chưa đủ lời hứa cảm xúc.")
        fixes.append("Thêm 1 đoạn mô tả cái giá cá nhân và một câu hỏi móc cuối để kéo đọc chương 1.")
    if wc(intro) > 330:
        flags.append("Mô tả dài, chứa nhiều thông tin hơn mức cần thiết.")
        fixes.append("Cô mô tả còn 180-260 từ, mỗi đoạn chỉ giữ một lực kéo: nỗi nhục, bí mật năng lực, cú phản công.")

    nums = [chapter_num(c) for c in chapters if chapter_num(c) != 9999]
    if nums:
        gaps = sorted(set(range(min(nums), max(nums) + 1)) - set(nums))
        if gaps:
            flags.append("Danh sách chương thiếu số: " + ", ".join(map(str, gaps)) + ".")
            fixes.append("Kiểm tra slug/post parent hoặc tạo lại chương thiếu để độc giả không bị hụt mạch.")
    if len(chapters) < 8:
        flags.append("Số chương ít so với nhịp sảng văn 10/10.")
    if not chapters:
        flags.append("Không map được chương trên trang truyện.")
        return flags, positives, fixes, 0

    first = ch_texts[0]
    last = ch_texts[-1]
    mid = "\n".join(ch_texts[1:-1])
    avg_words = sum(wc(x) for x in ch_texts) // max(1, len(ch_texts))
    short_count = sum(1 for x in ch_texts if wc(x) < 800)
    very_short_count = sum(1 for x in ch_texts if wc(x) < 650)

    if wc(first) < 900:
        flags.append("Mở truyện hơi mỏng, cú nhục chưa đủ thời lượng.")
        fixes.append("Mở rộng chương 1: thêm 1 cảnh công khai bị ép/nhục, phản ứng cơ thể, và một chi tiết chứng cứ nhỏ bị giẫm nát.")
    if not re.search(r"“|\"|!|cút|khinh|đuổi|sỉ nhục|phản bội", first[:1200], re.I):
        flags.append("Chương 1 chưa bật hook thoại/hành động trong 1.200 ký tự đầu.")
        fixes.append("Đưa câu thoại sỉ nhục hoặc hành động tước quyền lên ngay đoạn đầu.")
    else:
        positives.append("Mở đầu có xung đột trực diện.")

    if short_count >= max(3, len(chapters) // 2):
        flags.append(f"Nhiều chương ngắn ({short_count}/{len(chapters)} chương dưới 800 từ), đọc sẽ giống tóm tắt.")
        fixes.append("Mỗi chương ngắn thêm 300-500 từ bằng cảnh đối đầu, hậu quả và một beat cảm xúc sau va chạm.")
    elif avg_words >= 1000:
        positives.append("Độ dài chương tương đối đủ để triển khai cảnh.")

    evidence = terms_count(full, EVIDENCE_TERMS)
    resistance = terms_count(mid, RESISTANCE_TERMS)
    emotion = terms_count(full, EMOTION_TERMS)
    ending = terms_count(last, ENDING_TERMS)
    tech = terms_count(full, TECH_OVERLOAD)
    generic_titles = sum(1 for c in chapters if terms_count(title(c), GENERIC_TITLE_TERMS) > 0)

    if evidence < max(10, len(chapters) * 2):
        flags.append("Chuỗi chứng cứ chưa dày; cú vả mặt có nguy cơ dựa vào tuyên bố hơn là bằng chứng.")
        fixes.append("Cài thêm chứng cứ vật lý theo bậc thang: log gốc/sao kê/camera/giám định/biên bản có người thứ ba xác nhận.")
    else:
        positives.append("Có nền chứng cứ đủ để tạo cảm giác lật kèo.")

    if resistance < max(8, len(chapters)):
        flags.append("Lực cản giữa truyện chưa đủ nặng; nhân vật chính thắng hơi thuận.")
        fixes.append("Thêm bế tắc thật ở giữa: tài khoản bị phong tỏa, bằng chứng bị nghi ngờ, đồng minh quay lưng, hoặc thanh tra đình chỉ 24h.")
    else:
        positives.append("Giữa truyện có dấu hiệu phản công/kháng cự.")

    if ending < 2:
        flags.append("Kết truyện chưa có tín hiệu phán quyết/trả giá đủ rõ.")
        fixes.append("Kết cần có ba nhịp: phản diện trả giá cụ thể, nhân vật chính mất/giữ lại điều gì, và hình ảnh dư âm sau chiến thắng.")
    if wc(last) < 900:
        flags.append("Chương kết ngắn, cao trào dễ bị xử vội.")
        fixes.append("Kéo chương kết lên 1.000-1.400 từ bằng phiên chất vấn, phản đòn cuối của phản diện và khoảnh khắc hạ màn.")
    if emotion < max(12, len(chapters) * 2):
        flags.append("Cảm xúc nội tâm/hậu quả cá nhân còn mỏng so với phần tiền-quyền-chứng cứ.")
        fixes.append("Cài thêm cảnh riêng tư: nhân vật chính đối diện người thân/đồng minh, nói về cái giá thay vì chỉ công bố thắng lợi.")
    if tech >= 22:
        flags.append("Thuật ngữ kỹ thuật dày; dễ làm truyện giống hồ sơ hơn là cảnh.")
        fixes.append("Giữ thuật ngữ ở điểm chứng cứ, còn cảnh đối đầu hãy chuyển sang hành động, ánh mắt, lời khai và phản ứng đám đông.")
    if generic_titles >= len(chapters) // 2:
        flags.append("Tên chương dùng nhiều cụm chung, chưa tạo cảm giác mỗi chương có sự kiện riêng.")
        fixes.append("Đổi tên chương theo vật chứng/sự kiện cụ thể: 'Con Dấu Đỏ Trên Sao Kê', 'Camera Kho Lạnh Lúc 23:17'.")

    score = 10
    score -= min(3.0, len(flags) * 0.55)
    score -= min(1.0, very_short_count * 0.12)
    score = max(5.5, round(score, 1))
    return flags, positives, fixes, score


def main():
    infos, all_chapters = build_data()
    scored = []
    for story, chapters in infos:
        flags, positives, fixes, score = editorial_flags(story, chapters)
        scored.append((score, story, chapters, flags, positives, fixes))
    scored.sort(key=lambda x: (x[0], title(x[1])))

    lines = []
    lines.append("# Đề xuất sửa truyện để đạt 10/10")
    lines.append("")
    lines.append(f"- Thời điểm đọc/audit: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append(f"- Phạm vi: {len(infos)} truyện public, {len(all_chapters)} chương public.")
    lines.append("- Cách đọc: xem mô tả, chương 1, mạch chương giữa, chương cuối, tên chương, độ dài, chuỗi chứng cứ, lực cản, cảm xúc và độ hợp lý của cú lật.")
    lines.append("- Điểm là điểm biên tập tương đối để ưu tiên sửa, không phải đánh giá độc giả tuyệt đối.")
    lines.append("")
    lines.append("## Kết luận tổng quan")
    lines.append("")
    lines.append("Site đã có đúng chất sảng văn/vả mặt: nỗi nhục mở đầu rõ, chủ đề Việt hóa tốt, nhiều ngành nghề cụ thể, và phần lớn truyện có 8-10 chương nên dễ đọc nhanh. Tuy nhiên để lên 10/10, vấn đề lớn nhất không nằm ở ý tưởng mà nằm ở độ dày cảnh: một số truyện thắng quá thuận, chương cuối xử nhanh, nhiều chương giống bản tóm tắt diễn biến hơn là cảnh có va chạm sống động.")
    lines.append("")
    lines.append("Ưu tiên sửa theo thứ tự:")
    lines.append("1. Các truyện có nhiều chương dưới 800 từ: thêm cảnh đối đầu và hậu quả, không chỉ thêm mô tả cho dài.")
    lines.append("2. Chương 1: phải làm nỗi nhục đau hơn, công khai hơn, có một vật chứng/chi tiết bị hủy để độc giả muốn trả thù.")
    lines.append("3. Giữa truyện: thêm bế tắc thật trước khi lật kèo, ví dụ bị phong tỏa tài khoản, bằng chứng bị bác, đồng minh quay lưng, hoặc truyền thông bẻ lái.")
    lines.append("4. Chương cuối: kéo dài phiên phán quyết, cho phản diện phản đòn lần cuối rồi mới sụp; sau đó thêm một cảnh yên tĩnh để chiến thắng có dư âm.")
    lines.append("5. Giảm title quá dài và thuật ngữ quá dày; chuyển kỹ thuật thành vật chứng dễ hình dung.")
    lines.append("")

    lines.append("## Nhóm cần sửa trước")
    lines.append("")
    for score, story, chapters, flags, positives, fixes in scored[:20]:
        lines.append(f"- **{title(story)}** - khoảng {score}/10: {', '.join(flags[:3]) if flags else 'gần ổn'}.")
    lines.append("")

    lines.append("## Chi tiết từng truyện")
    lines.append("")
    for score, story, chapters, flags, positives, fixes in scored:
        stitle = title(story)
        intro = text(story)
        ch_texts = [text(c) for c in chapters]
        first = ch_texts[0] if ch_texts else ""
        last = ch_texts[-1] if ch_texts else ""
        lines.append(f"### {stitle}")
        lines.append("")
        lines.append(f"- Link: {story['link']}")
        lines.append(f"- Điểm biên tập hiện tại: **{score}/10**")
        lines.append(f"- Cấu trúc: {len(chapters)} chương; mô tả {wc(intro)} từ; chương 1 {wc(first)} từ; chương kết {wc(last)} từ.")
        lines.append(f"- Mở truyện: {sample(first, 38)}")
        lines.append(f"- Kết truyện: {sample(last, 38)}")
        if positives:
            lines.append("- Điểm đang ổn: " + "; ".join(positives[:3]) + ".")
        if flags:
            lines.append("- Cần sửa: " + "; ".join(flags) + ".")
        else:
            lines.append("- Cần sửa: ít vấn đề lớn, chỉ cần polish câu chữ và tăng cảm xúc ở một vài cảnh.")
        unique_fixes = []
        for fix in fixes:
            if fix not in unique_fixes:
                unique_fixes.append(fix)
        if not unique_fixes:
            unique_fixes = ["Đọc lại chương 1 và chương cuối để thêm một chi tiết cảm xúc độc quyền của truyện, tránh kết thúc quá công thức."]
        lines.append("- Đề xuất sửa cụ thể: " + " ".join(unique_fixes[:5]))
        if chapters:
            short = [f"{chapter_num(c)} ({wc(text(c))} từ)" for c in chapters if wc(text(c)) < 800]
            if short:
                lines.append("- Chương nên bồi thêm cảnh: " + ", ".join(short[:12]) + ("..." if len(short) > 12 else "") + ".")
        lines.append("")

    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
