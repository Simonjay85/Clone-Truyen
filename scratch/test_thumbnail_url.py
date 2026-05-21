import urllib.request
import ssl

urls = [
    "https://doctieuthuyet.com/wp-content/uploads/2026/05/cover-2573-hq-397-768x768.png",
    "https://doctieuthuyet.com/wp-content/uploads/2026/05/cover-2573-hq-397.png"
]

ctx = ssl._create_unverified_context()
for url in urls:
    print(f"Requesting: {url}")
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, context=ctx, timeout=10) as response:
            code = response.getcode()
            print(f"  Status: {code}")
            print(f"  Content-Type: {response.info().get('Content-Type')}")
            print(f"  Content-Length: {response.info().get('Content-Length')}")
    except Exception as e:
        print(f"  Error: {e}")
    print("-" * 50)
