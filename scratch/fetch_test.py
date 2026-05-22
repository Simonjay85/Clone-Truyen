import requests
import json

url = "https://doctieuthuyet.com/wp-json/wp/v2/truyen/2238"
try:
    res = requests.get(url, timeout=10)
    if res.status_code == 200:
        data = res.json()
        print("Title:", data.get("title", {}).get("rendered"))
        print("Intro (first 200 chars):", data.get("content", {}).get("rendered")[:200])
    else:
        print("Error status:", res.status_code)
except Exception as e:
    print("Error:", e)
