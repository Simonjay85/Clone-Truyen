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
    
    # Let's extract the part between </header> and <footer class="mkm-footer">
    # Let's use a regex or string find
    start_tag = "</header>"
    end_tag = '<footer class="mkm-footer">'
    
    start_idx = html.find(start_tag)
    end_idx = html.find(end_tag)
    
    if start_idx != -1 and end_idx != -1:
        middle_html = html[start_idx + len(start_tag):end_idx]
        print(f"\n--- MIDDLE HTML (Length: {len(middle_html)}) ---")
        # Print first 1000 and last 1000 characters of the middle HTML
        print("First 1000 chars of middle:")
        print(middle_html[:1000])
        print("\nLast 1000 chars of middle:")
        print(middle_html[-1000:])
    else:
        print(f"Error: Tags not found. start_idx={start_idx}, end_idx={end_idx}")
        
    # Let's check if the footer-top HTML exists
    footer_idx = html.find('<footer class="mkm-footer">')
    if footer_idx != -1:
        footer_html = html[footer_idx:]
        print(f"\n--- FOOTER HTML (Length: {len(footer_html)}) ---")
        print(footer_html[:2000])

except Exception as e:
    print("❌ Error:", e)
