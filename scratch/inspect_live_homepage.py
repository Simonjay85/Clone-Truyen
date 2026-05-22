import urllib.request
import ssl
import re

url = "https://doctieuthuyet.com/"
ctx = ssl._create_unverified_context()

try:
    print(f"Fetching: {url}")
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, context=ctx, timeout=15) as response:
        html = response.read().decode('utf-8')
        
    print("Searching for 'Truyện hot' section in HTML...")
    # Find Truyện hot section in HTML
    # We want to capture the grid of cards following "Truyện hot"
    # We can split the HTML at "Truyện hot"
    parts = html.split("Truyện hot")
    if len(parts) < 2:
        print("Could not find 'Truyện hot' in the HTML text.")
    else:
        # Get the HTML portion after "Truyện hot"
        after_hot = parts[1]
        
        # Let's find all cards inside this section up to the next section "TRUYỆN FULL" or similar
        # We can crop the string to "Truyện full" or "Truyện hoàn thành"
        limit_parts = after_hot.split("Truyện full")
        target_html = limit_parts[0] if len(limit_parts) > 1 else after_hot
        
        # Now find all cards in target_html
        # A card has: <div class="mkm-card">...</div>
        # Let's match each card using regex
        cards = re.findall(r'<div class="mkm-card">.*?</div>\s*</div>\s*</div>', target_html, re.DOTALL)
        if not cards:
            # Try a simpler regex to match <div class="mkm-card">...
            cards = re.findall(r'<div class="mkm-card">.*?</div>\s*</div>', target_html, re.DOTALL)
            
        print(f"Found {len(cards)} raw cards in the hot section.")
        for idx, card in enumerate(cards):
            print(f"\n--- Card {idx+1} ---")
            # Extract card-bg
            bg_match = re.search(r'--card-bg:\s*url\(\'(.*?)\'\)', card)
            if bg_match:
                print(f"  Container bg: {bg_match.group(1)}")
            
            # Extract img src and onerror
            img_match = re.search(r'<img\s+src="(.*?)"(.*?)>', card)
            if img_match:
                img_src = img_match.group(1)
                img_attrs = img_match.group(2)
                onerror_match = re.search(r'onerror="(.*?)"', img_attrs)
                onerror = onerror_match.group(1) if onerror_match else "none"
                print(f"  Img src: {img_src}")
                print(f"  Img onerror: {onerror}")
                
            # Extract card name
            name_match = re.search(r'<p class="mkm-card-name">(.*?)</p>', card)
            if name_match:
                print(f"  Name: {name_match.group(1).strip()}")
            else:
                # Try simple search for paragraph
                name_match = re.search(r'<p class="mkm-card-name">(.*?)</p>', card, re.DOTALL)
                if name_match:
                    print(f"  Name: {name_match.group(1).strip()}")
                    
except Exception as e:
    print(f"Error: {e}")
