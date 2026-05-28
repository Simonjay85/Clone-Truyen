import urllib.request
import ssl
import re

ctx = ssl._create_unverified_context()
url = "https://doctieuthuyet.com/gioi-thieu/"

try:
    print(f"Fetching {url}...")
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, context=ctx, timeout=15) as r:
        final_url = r.geturl()
        html = r.read().decode('utf-8')
        
    print(f"✓ Fetch complete!")
    print(f"  Requested URL: {url}")
    print(f"  Final URL:     {final_url}")
    print(f"  HTML Length:   {len(html)} characters")
    
    # Check if there is "Mới cập nhật" or "Bảng xếp hạng"
    print("\nChecking container signatures:")
    print(f"  mkm-wrap:      {'mkm-wrap' in html}")
    print(f"  pg-main:       {'pg-main' in html}")
    print(f"  pg-hero:       {'pg-hero' in html}")
    print(f"  pg-prose:      {'pg-prose' in html}")
    
    # Print the first 1000 characters to see the structure
    print("\n--- FIRST 1000 CHARACTERS ---")
    print(html[:1000])
    
except Exception as e:
    print("Error:", e)
