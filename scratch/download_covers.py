import urllib.request
import ssl

ctx = ssl._create_unverified_context()

urls = {
    "cover-2573.png": "https://doctieuthuyet.com/wp-content/uploads/2026/05/cover-2573-hq-210.png",
    "cover-1927.jpg": "https://doctieuthuyet.com/wp-content/uploads/2026/05/cover-1927-upd-414.jpg",
}

for name, url in urls.items():
    print(f"Downloading {url}...")
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, context=ctx) as response:
            with open(f"/Users/aaronnguyen/.gemini/antigravity-ide/brain/12ea8d69-8883-4c0b-9ecb-fc7822e46167/{name}", "wb") as f:
                f.write(response.read())
        print(f"Saved to {name}")
    except Exception as e:
        print(f"Failed to download {name}: {e}")
