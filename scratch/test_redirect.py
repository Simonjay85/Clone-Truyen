import urllib.request
import ssl

url = "https://doctieuthuyet.com/wp-content/themes/tehi-theme/img_data/images/doesnotexist.png"
ctx = ssl._create_unverified_context()

print(f"Requesting non-existent image: {url}")
try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, context=ctx, timeout=10) as response:
        print(f"  Status: {response.getcode()}")
        print(f"  URL resolved to: {response.geturl()}")
        print(f"  Content-Type: {response.info().get('Content-Type')}")
except Exception as e:
    print(f"  Error: {e}")
