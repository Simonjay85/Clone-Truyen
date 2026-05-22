import urllib.request
import re

url = "https://doctieuthuyet.com/"
headers = {'User-Agent': 'Mozilla/5.0'}

try:
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
        
    # Search for Truyen Hot section in HTML
    start_idx = html.find("Truyện hot")
    if start_idx != -1:
        snippet = html[start_idx:start_idx + 10000]
        print("HTML snippet around 'Truyện hot':")
        # Print all <img> tags in this snippet
        img_tags = re.findall(r'<img[^>]*>', snippet)
        for img in img_tags:
            print(img)
    else:
        print("Could not find 'Truyện hot' in homepage HTML.")
        
except Exception as e:
    print("Error:", e)
