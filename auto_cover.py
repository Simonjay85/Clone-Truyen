import argparse
import base64
import os
import random
import time
import urllib.parse

import requests


def build_params(token):
    return {"token": token} if token else {}


def main():
    parser = argparse.ArgumentParser(description="Backfill missing WordPress cover images safely.")
    parser.add_argument("--url", default=os.environ.get("WP_URL", "https://doctieuthuyet.com"))
    parser.add_argument("--token", default=os.environ.get("TEHI_BACKFILL_TOKEN", ""))
    parser.add_argument("--limit", type=int, default=20)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    wp_url = args.url.rstrip("/")
    print("Bat dau kiem tra anh dai dien dang thieu...")

    while True:
        try:
            res = requests.get(
                f"{wp_url}/wp-json/temply/v1/missing-covers",
                params=build_params(args.token),
                timeout=20,
            ).json()
        except Exception as exc:
            print("Loi get missing covers:", exc)
            time.sleep(5)
            continue

        if res.get("code") == "rest_forbidden":
            raise SystemExit("REST endpoint bi chan. Hay dang nhap admin hoac truyen TEHI_BACKFILL_TOKEN hop le.")

        items = res.get("items") or []
        if not items:
            print("Tat ca bai/truyen da co anh dai dien.")
            break

        items = items[: args.limit]
        print(f"Tim thay {len(items)} item thieu anh.")
        if args.dry_run:
            for item in items:
                print(f"[DRY] {item['id']} | {item['type']} | {item['title']} | source={item.get('source_cover') or '-'}")
            break

        for item in items:
            title = item["title"]
            post_id = item["id"]
            source_cover = item.get("source_cover") or ""

            if source_cover:
                print(f"[{post_id}] Dung anh nguon co san: {source_cover}")
                payload = {"post_id": post_id, "image_url": source_cover}
            else:
                if item.get("type") == "truyen":
                    prompt = f"Vietnamese web novel book cover art, illustration, fantasy anime style, professional digital painting, title concept: {title} masterpiece"
                else:
                    prompt = f"A simple, clean, minimalist flat vector illustration representing: {title} web design, corporate aesthetics"

                img_url = (
                    "https://image.pollinations.ai/prompt/"
                    f"{urllib.parse.quote(prompt)}?width=800&height=1200&seed={random.randint(1, 99999)}&nologo=true"
                )
                print(f"[{post_id}] Tao anh moi cho: {title}")
                try:
                    img_res = requests.get(img_url, timeout=45)
                    if img_res.status_code == 429:
                        print("Pollinations qua tai, cho 15s...")
                        time.sleep(15)
                        continue
                    img_res.raise_for_status()
                except Exception as exc:
                    print("Loi tai anh:", exc)
                    time.sleep(5)
                    continue

                payload = {
                    "post_id": post_id,
                    "image_b64": base64.b64encode(img_res.content).decode("utf-8"),
                }
                time.sleep(2)

            try:
                up_res = requests.post(
                    f"{wp_url}/wp-json/temply/v1/upload-cover",
                    params=build_params(args.token),
                    data=payload,
                    timeout=45,
                ).json()
            except Exception as exc:
                print("Loi upload server:", exc)
                continue

            if up_res.get("status") == "success":
                print(f"Da gan anh dai dien cho ID {post_id}")
            else:
                print(f"Loi upload ID {post_id}: {up_res}")

        time.sleep(1)


if __name__ == "__main__":
    main()
