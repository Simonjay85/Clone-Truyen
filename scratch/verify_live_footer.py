import urllib.request
import ssl

ctx = ssl._create_unverified_context()
url = "https://doctieuthuyet.com/"

try:
    print(f"Fetching live homepage from {url}...")
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, context=ctx, timeout=15) as r:
        html = r.read().decode('utf-8')
        
    print("✓ Successfully fetched latest live HTML!")
    
    # Check if "#mkmAuthModal { position: fixed;" is in the HTML
    target_str = "#mkmAuthModal { position: fixed;"
    if target_str in html:
        print("✅ SUCCESS! The fixed positioning for the Auth Modal is active on the live website!")
    else:
        print("❌ ERROR! The fixed positioning is NOT active. Cache might not have cleared or file wasn't uploaded.")
        
except Exception as e:
    print("Error:", e)
