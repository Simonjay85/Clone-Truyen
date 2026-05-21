import urllib.request
import ssl

urls = [
    "https://doctieuthuyet.com/wp-content/uploads/2026/05/cover-2587-hq-859.png",
    "https://doctieuthuyet.com/wp-content/uploads/2026/05/cover-1927-upd-414.jpg",
    "https://doctieuthuyet.com/wp-content/uploads/2026/05/cover-1933-hq-295.jpg",
    "https://doctieuthuyet.com/wp-content/themes/tehi-theme/img_data/images/no-image-cover.png"
]

ctx = ssl._create_unverified_context()
for url in urls:
    print(f"Requesting: {url}")
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, context=ctx, timeout=10) as response:
            code = response.getcode()
            headers = response.info()
            content_type = headers.get('Content-Type')
            content_length = headers.get('Content-Length')
            data = response.read(100) # Read first 100 bytes
            print(f"  Status: {code}")
            print(f"  Content-Type: {content_type}")
            print(f"  Content-Length: {content_length}")
            print(f"  First 20 bytes: {data[:20]}")
    except Exception as e:
        print(f"  Error: {e}")
    print("-" * 50)
