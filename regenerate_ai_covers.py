import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import html
import json
import random
import re
import time
import urllib.parse
from pathlib import Path

import requests
from PIL import Image


WIDTH = 1200
HEIGHT = 800


def clean(value):
    value = html.unescape(value or "")
    value = re.sub(r"\s+", " ", value).strip()
    return value


def visual_direction(title):
    t = title.lower()
    if any(k in t for k in ["cứu hỏa", "đám cháy", "lửa"]):
        return "dramatic fire rescue scene, smoke, orange emergency light, brave female firefighter silhouette"
    if any(k in t for k in ["ma túy", "sát nhân", "án mạng", "hung thủ", "dao", "đen tối"]):
        return "moody crime thriller scene, neon rain, shadowy investigation, suspenseful composition"
    if any(k in t for k in ["100 tỷ", "10 tỷ", "công ty", "chủ tịch", "tổng giám đốc", "thừa kế", "siêu giàu"]):
        return "luxury corporate revenge drama, glass skyscraper, elegant protagonist, gold and teal cinematic lighting"
    if any(k in t for k in ["phi tần", "triều đình", "đích nữ", "kiếp trước", "gia tộc"]):
        return "ancient palace revenge fantasy, elegant noble woman, lanterns, silk robes, royal courtyard"
    if any(k in t for k in ["làng chài", "biển", "mưa"]):
        return "coastal mystery drama, fishing village, stormy sea, cinematic blue light"
    if any(k in t for k in ["bác sĩ", "bệnh viện"]):
        return "medical suspense drama, modern hospital corridor, determined young doctor, teal lighting"
    if any(k in t for k in ["học sinh", "trường học", "họp lớp"]):
        return "school reunion drama, upscale banquet hall, emotional reveal, cinematic lighting"
    if any(k in t for k in ["chồng", "bạn trai", "mẹ chồng", "con dâu", "cưới", "hôn nhân", "người tình"]):
        return "modern romance revenge drama, elegant Vietnamese female lead, city night, emotional tension"
    return "high-stakes modern Vietnamese drama, cinematic character poster, emotional atmosphere"


def build_prompt(title, team=False):
    if team:
        return (
            f"Premium square-friendly team avatar key art for a Vietnamese online novel group named {title}. "
            "Stylized cinematic illustration, beautiful character emblem, polished web novel platform art, "
            "rich lighting, clean composition, no text, no letters, no logo, no watermark."
        )

    return (
        "Cinematic Vietnamese web novel cover art, landscape 3:2 composition for website thumbnail. "
        f"Story title concept: {title}. "
        f"Visual direction: {visual_direction(title)}. "
        "Professional digital painting, high-end streaming drama poster quality, expressive atmosphere, "
        "clear central subject, rich depth of field, refined color grading, beautiful lighting, "
        "no text, no letters, no title typography, no watermark, no logo, no UI."
    )


def download_image(prompt, seed, out_path, retries=3):
    encoded = urllib.parse.quote(prompt)
    params = urllib.parse.urlencode(
        {
            "width": WIDTH,
            "height": HEIGHT,
            "seed": seed,
            "nologo": "true",
            "private": "true",
            "enhance": "true",
            "model": "flux",
        }
    )
    url = f"https://image.pollinations.ai/prompt/{encoded}?{params}"

    for attempt in range(1, retries + 1):
        try:
            response = requests.get(url, timeout=120)
            if response.status_code == 429:
                wait = 35 * attempt
                print(f"Rate limited for {out_path.name}; waiting {wait}s", flush=True)
                time.sleep(wait)
                continue
            response.raise_for_status()
            out_path.write_bytes(response.content)
            with Image.open(out_path) as img:
                if img.size != (WIDTH, HEIGHT):
                    img = img.convert("RGB").resize((WIDTH, HEIGHT), Image.Resampling.LANCZOS)
                    img.save(out_path, "JPEG", quality=94, optimize=True)
                else:
                    img.convert("RGB").save(out_path, "JPEG", quality=94, optimize=True)
            return True
        except Exception as exc:
            print(f"Attempt {attempt} failed for {out_path.name}: {exc}", flush=True)
            time.sleep(6 * attempt)
    return False


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="/tmp/missing-covers.json")
    parser.add_argument("--covers-out", default="generated_covers_ai")
    parser.add_argument("--team-out", default="tehi-theme/templates/images")
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--covers-only", action="store_true")
    parser.add_argument("--teams-only", action="store_true")
    args = parser.parse_args()

    covers_out = Path(args.covers_out)
    covers_out.mkdir(parents=True, exist_ok=True)

    with open(args.input, "r", encoding="utf-8") as handle:
        items = json.load(handle)

    jobs = []
    if not args.teams_only:
        for item in items:
            post_id = int(item["id"])
            title = clean(item["title"])
            out_path = covers_out / f"{post_id}.jpg"
            if out_path.exists() and not args.force:
                print(f"Skipping existing cover {post_id}", flush=True)
                continue
            jobs.append(("cover", post_id, title, build_prompt(title), post_id + 20260503, out_path))

    teams = [
        ("team1.jpeg", "Mèo Kam Mập"),
        ("team2.jpeg", "Lạc Giới Tinh Thư"),
        ("team3.jpeg", "Mỗi Ngày Chỉ Muốn"),
        ("team4.jpeg", "Cá Chép Ngắm Mưa"),
        ("team5.jpeg", "Trong Tim Có Cậu"),
        ("team6.jpeg", "Ổ Mật Mật"),
        ("team7.jpeg", "Nguyệt Sát Tinh"),
        ("team8.jpeg", "Mèo Bủng Beo"),
    ]
    team_out = Path(args.team_out)
    team_out.mkdir(parents=True, exist_ok=True)
    if not args.covers_only:
        for idx, (filename, name) in enumerate(teams, start=1):
            out_path = team_out / filename
            if out_path.exists() and not args.force:
                print(f"Skipping existing team avatar {idx}", flush=True)
                continue
            jobs.append(("team", idx, name, build_prompt(name, team=True), 99000 + idx, out_path))

    failures = []
    with ThreadPoolExecutor(max_workers=max(1, args.workers)) as executor:
        futures = {}
        for kind, ident, title, prompt, seed, out_path in jobs:
            print(f"Queueing {kind} {ident}: {title}", flush=True)
            futures[executor.submit(download_image, prompt, seed, out_path)] = (kind, ident, out_path)

        for future in as_completed(futures):
            kind, ident, out_path = futures[future]
            ok = future.result()
            if ok:
                print(f"Generated {kind} {ident}: {out_path}", flush=True)
            else:
                failures.append(f"{kind} {ident}")

    if failures:
        raise SystemExit("Failed: " + ", ".join(failures))


if __name__ == "__main__":
    main()
