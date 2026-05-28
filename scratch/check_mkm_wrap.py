import urllib.request
import ssl

ctx = ssl._create_unverified_context()
url = "https://doctieuthuyet.com/"

print(f"Fetching {url}...")
try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, context=ctx, timeout=15) as r:
        html = r.read().decode('utf-8')
        
    print(f"✓ Success! HTML length: {len(html)}")
    
    # Search for all occurrences of "mkm-wrap" in the HTML and print 100 chars around each
    import re
    matches = [m.start() for m in re.finditer("mkm-wrap", html)]
    print(f"Found {len(matches)} occurrences of 'mkm-wrap':")
    for idx, pos in enumerate(matches, 1):
        print(f"  Occurrence {idx}: ... {html[max(0, pos-40):pos+80]} ...")

except Exception as e:
    print("❌ Error:", e)
