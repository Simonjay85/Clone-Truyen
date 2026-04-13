import requests

url = "https://fanqienovel.com/page/7104043615951260686" # A random popular book URL example, or just page/7303795689759312937 doesn't matter we just need to see structure.
# If 404, we'll try something else.

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

response = requests.get(url, headers=headers)
print("Status Code:", response.status_code)
html = response.text

import re
# Look for next data or script tags
script_content = re.search(r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>', html)
if script_content:
    print("Found NEXT_DATA JSON!")
    data = script_content.group(1)
    print("Snippet:", data[:500])
else:
    print("No NEXT_DATA. Snippet of HTML:", html[:1000])

