import json
import os
import re
import sys
import time
import ftplib
from pathlib import Path

import requests


ROOT = Path("/Users/aaronnguyen/TN/App/doctieuthuyet")
REPORT = ROOT / "danh_gia_van_hoc_2026-05-25.md"
SCRATCH = ROOT / "scratch"
HELPER = SCRATCH / "wp_update_story_v13.php"
RESULTS = SCRATCH / "deploy_report_v13_batch_20260525_results.json"

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"
WP_URL = "https://doctieuthuyet.com"
SECRET_TOKEN = "ZEN_TRUYEN_2026_BYPASS"


def report_ids():
    text = REPORT.read_text(encoding="utf-8")
    ids = []
    for match in re.finditer(r"^### ID (\d+)", text, flags=re.M):
        sid = int(match.group(1))
        if sid not in ids:
            ids.append(sid)
    return ids


def normalize_payload(story_id, data):
    seo = data.get("seo") if isinstance(data.get("seo"), dict) else {}
    title = data.get("title") or data.get("seo_title") or seo.get("seo_title") or f"Truyện ID {story_id}"
    intro = data.get("intro", "")
    chapters = data.get("chapters", [])

    focus_keyword = data.get("focus_keyword") or seo.get("focus_keyword") or title
    seo_title = data.get("seo_title") or seo.get("seo_title") or title[:58]
    seo_description = (
        data.get("seo_description")
        or seo.get("seo_description")
        or re.sub(r"<[^>]+>", " ", intro).strip()[:155]
        or title
    )

    return {
        "secret_token": SECRET_TOKEN,
        "story_id": int(story_id),
        "intro": intro,
        "focus_keyword": focus_keyword,
        "seo_title": seo_title,
        "seo_description": seo_description,
        "chapters": chapters,
    }


def upload_helper():
    ftp = ftplib.FTP(FTP_HOST, timeout=45)
    ftp.login(FTP_USER, FTP_PASS)
    with HELPER.open("rb") as handle:
        ftp.storbinary("STOR wp_update_story_v13.php", handle)
    ftp.quit()


def delete_helper():
    try:
        ftp = ftplib.FTP(FTP_HOST, timeout=45)
        ftp.login(FTP_USER, FTP_PASS)
        ftp.delete("wp_update_story_v13.php")
        ftp.quit()
    except Exception as exc:
        print(f"cleanup_warning={exc}")


def deploy_one(story_id):
    path = SCRATCH / f"rewrite_{story_id}_v13.json"
    if not path.exists():
        return {"story_id": story_id, "status": "missing_json"}

    data = json.loads(path.read_text(encoding="utf-8"))
    payload = normalize_payload(story_id, data)
    if not payload["intro"] or not payload["chapters"]:
        return {"story_id": story_id, "status": "invalid_payload"}

    response = requests.post(f"{WP_URL}/wp_update_story_v13.php", json=payload, timeout=180)
    try:
        body = response.json()
    except ValueError:
        body = {"raw": response.text[:1000]}

    ok = response.status_code == 200 and bool(body.get("success"))
    return {
        "story_id": story_id,
        "status": "ok" if ok else "failed",
        "http_status": response.status_code,
        "title": body.get("title") or data.get("title"),
        "deleted_chapters_count": body.get("deleted_chapters_count"),
        "inserted_chapters_count": body.get("inserted_chapters_count"),
        "response": body if not ok else None,
    }


def main():
    ids = report_ids()
    skipped = {2710: "duplicate_of_2703"}
    selected = [sid for sid in ids if sid not in skipped]
    if len(sys.argv) > 1:
        selected = [int(arg) for arg in sys.argv[1:]]

    results = []
    upload_helper()
    try:
        for index, story_id in enumerate(selected, 1):
            print(f"[{index}/{len(selected)}] deploying {story_id}...")
            result = deploy_one(story_id)
            print(json.dumps(result, ensure_ascii=False))
            results.append(result)
            RESULTS.write_text(json.dumps({
                "updated_at": time.strftime("%Y-%m-%d %H:%M:%S"),
                "skipped": skipped,
                "results": results,
            }, ensure_ascii=False, indent=2), encoding="utf-8")
            time.sleep(0.35)
    finally:
        delete_helper()

    ok_count = sum(1 for item in results if item["status"] == "ok")
    missing = [item["story_id"] for item in results if item["status"] == "missing_json"]
    failed = [item for item in results if item["status"] == "failed"]
    print(f"SUMMARY ok={ok_count} missing={missing} failed={len(failed)} results={RESULTS}")


if __name__ == "__main__":
    main()
