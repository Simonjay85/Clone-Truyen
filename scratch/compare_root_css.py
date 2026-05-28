import urllib.request
import ssl
import hashlib

ctx = ssl._create_unverified_context()
url = "https://doctieuthuyet.com/wp-content/themes/tehi-theme/style.css?ver=1.0.0"

try:
    print(f"Fetching live root style.css from {url}...")
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, context=ctx, timeout=15) as r:
        live_css = r.read().decode('utf-8')
    print("✓ Successfully fetched live root CSS!")
    
    local_path = "/Users/aaronnguyen/TN/App/doctieuthuyet/tehi-theme/style.css"
    with open(local_path, "r", encoding="utf-8") as f:
        local_css = f.read()
        
    live_md5 = hashlib.md5(live_css.encode('utf-8')).hexdigest()
    local_md5 = hashlib.md5(local_css.encode('utf-8')).hexdigest()
    
    print(f"Live MD5:  {live_md5} (length: {len(live_css)})")
    print(f"Local MD5: {local_md5} (length: {len(local_css)})")
    
    if live_md5 == local_md5:
        print("✅ The live root CSS and local root CSS match perfectly!")
    else:
        print("⚠️ CSS MISMATCH! The live and local root CSS files are different.")
        with open("/Users/aaronnguyen/TN/App/doctieuthuyet/scratch/live_root_style.css", "w", encoding="utf-8") as f:
            f.write(live_css)
        print("Saved live root CSS to scratch/live_root_style.css")
        
except Exception as e:
    print("Error:", e)
