import urllib.request
import re

url = "https://doctieuthuyet.com/truyen/di-chuc-vo-hinh-tran-chien-tai-san/"
headers = {'User-Agent': 'Mozilla/5.0'}

req = urllib.request.Request(url, headers=headers)
html = urllib.request.urlopen(req).read().decode('utf-8')

# Find all chapter links
links = re.findall(r'<a[^>]+href="(https://doctieuthuyet.com/chuong/[^"]+)"[^>]*>Chương', html)
# Remove duplicates while preserving order
unique_links = list(dict.fromkeys(links))
unique_links.reverse()  # Since recent ones are typically listed first

for u in unique_links:
    try:
        creq = urllib.request.Request(u, headers=headers)
        chtml = urllib.request.urlopen(creq).read().decode('utf-8')
        ps = re.findall(r'<p>(.*?)</p>', chtml, re.DOTALL)
        content = "\n".join([re.sub(r'<[^>]+>', '', p).strip() for p in ps if len(p.strip()) > 20])
        
        print("\n=== " + u.split('/')[-2] + " ===")
        print(content[:500] + "...\n")
    except Exception as e:
        print("Error fetching", u, e)
