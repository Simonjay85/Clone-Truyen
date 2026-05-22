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
        
    print(f"Loaded HTML length: {len(html)}")
    
    # Let's find all titles matching <p class="mkm-card-name">...</p>
    titles = re.findall(r'<p class="mkm-card-name">(.*?)</p>', html, re.DOTALL)
    print(f"\nFound class 'mkm-card-name' titles: {len(titles)}")
    for idx, title in enumerate(titles, 1):
        print(f"  {idx}. {title.strip()}")
        
    # Let's also look for standard wordpress title classes or post titles
    # like slider titles
    slider_titles = re.findall(r'<h2 class="mkm-slider-title">(.*?)</h2>', html, re.DOTALL)
    print(f"\nFound class 'mkm-slider-title' (Slider): {len(slider_titles)}")
    for idx, title in enumerate(slider_titles, 1):
        print(f"  {idx}. {title.strip()}")
        
    # Let's see if there are any other titles or card structures on the page
    # e.g., the ranking list titles
    rank_titles = re.findall(r'<div style="font-size:13px; font-weight:800; color:#c2410c;[^>]*>(.*?)</div>', html, re.DOTALL)
    print(f"\nFound class ranking top titles: {len(rank_titles)}")
    for idx, title in enumerate(rank_titles, 1):
        print(f"  {idx}. {title.strip()}")
        
    rank_other_titles = re.findall(r'<div style="font-size:13px; font-weight:600; color:#4b5563;[^>]*>(.*?)</div>', html, re.DOTALL)
    print(f"\nFound class ranking other titles: {len(rank_other_titles)}")
    for idx, title in enumerate(rank_other_titles, 1):
        print(f"  {idx}. {title.strip()}")

except Exception as e:
    print(f"Error: {e}")
