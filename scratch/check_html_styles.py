import urllib.request
import ssl
import re

ctx = ssl._create_unverified_context()
url = "https://doctieuthuyet.com/"

print(f"Fetching {url}...")
try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, context=ctx, timeout=15) as r:
        html = r.read().decode('utf-8')
        
    print(f"✓ Success! HTML length: {len(html)}")
    
    # Search for all inline styles containing "display" or "visibility" or "opacity"
    inline_styles = re.findall(r'style="([^"]*(?:display|visibility|opacity)[^"]*)"', html, re.IGNORECASE)
    print(f"\nFound {len(inline_styles)} inline styles with display/visibility/opacity:")
    for s in inline_styles:
        print(f"  style=\"{s}\"")
        
    # Search for any style tags (<style>...</style>) and check if any class like main, main-content, mkm-wrap is set to display: none
    style_tags = re.findall(r'<style[^>]*>(.*?)</style>', html, re.DOTALL | re.IGNORECASE)
    print(f"\nAnalyzing {len(style_tags)} style tags in fetched HTML:")
    for idx, tag in enumerate(style_tags, 1):
        for pattern in ["main", "wrap", "body", "content"]:
            matches = re.findall(r'([^{}\n]*' + pattern + r'[^{}\n]*\{[^}]*display\s*:\s*none[^}]*\})', tag, re.IGNORECASE)
            if matches:
                print(f"  ⚠️ Match in Style Tag {idx} for pattern '{pattern}': {matches}")

except Exception as e:
    print("❌ Error:", e)
