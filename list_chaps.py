import requests

BYPASS_URL = "https://doctieuthuyet.com/api_truyen_bypass.php"
TOKEN = "ZEN_TRUYEN_2026_BYPASS"
TRUYEN_ID = 2023

def bypass(method, endpoint, payload):
    res = requests.post(BYPASS_URL, json={
        "secret_token": TOKEN,
        "method": method,
        "endpoint": endpoint,
        "payload": payload
    }, timeout=60)
    return res

res = bypass("GET", f"chuong?meta_key=_truyen_id&meta_value={TRUYEN_ID}&per_page=100", {})
if res.status_code == 200:
    chaps = res.json()
    print(f"Found {len(chaps)} chapters:")
    for c in chaps:
        print(f"ID: {c['id']} | Slug: {c['slug']} | Title: {c['title']['rendered']} | Date: {c['date']}")
else:
    print(f"Error {res.status_code}: {res.text}")
