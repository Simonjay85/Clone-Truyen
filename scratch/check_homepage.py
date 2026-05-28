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
    
    # Print the first 1000 characters
    print("\n--- FIRST 1000 CHARACTERS ---")
    print(html[:1000])
    
    # Print the last 1500 characters
    print("\n--- LAST 1500 CHARACTERS ---")
    print(html[-1500:])
    
    # Let's search for "mkm-wrap" or any content classes to see if they are in the HTML
    print("\nChecking for containers:")
    containers = ["mkm-wrap", "mkm-body", "mkm-main", "mkm-aside", "mkm-footer", "mkm-slider-wrap"]
    for c in containers:
        print(f"  Presence of '{c}': {c in html}")
        
    # Search for PHP errors/warnings
    print("\nChecking for PHP warnings/errors:")
    errors = ["fatal error", "parse error", "warning:", "notice:", "wp-content/themes", "stack trace"]
    for err in errors:
        if err in html.lower():
            print(f"  ⚠️ FOUND '{err}' in HTML!")
            # Print matching line
            for line in html.split("\n"):
                if err in line.lower():
                    print("    ", line[:200])

except Exception as e:
    print("❌ Error:", e)
