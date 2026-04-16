import urllib.request
import re

urls = [
    "https://doctieuthuyet.com/chuong/chuong-2-luoi-bay-tien-bac-va-cu-go-nhe-kinh-hoang/",
    "https://doctieuthuyet.com/chuong/chuong-3-tieng-tho-dai-cua-thuong-de-khi-phap-luat-hoa-tro-he/",
    "https://doctieuthuyet.com/chuong/chuong-10-giong-bao-cuong-no-khi-su-that-chi-la-mot-kich-ban/",
    "https://doctieuthuyet.com/chuong/chuong-12-dai-hoi-de-vuong-ban-tiec-cua-nhung-vi-than/"
]

headers = {'User-Agent': 'Mozilla/5.0'}

for u in urls:
    try:
        req = urllib.request.Request(u, headers=headers)
        html = urllib.request.urlopen(req).read().decode('utf-8')
        ps = re.findall(r'<p>(.*?)</p>', html, re.DOTALL)
        content = "\n".join([re.sub(r'<[^>]+>', '', p).strip() for p in ps])
        
        print("\n=== " + u.split('/')[-2] + " ===")
        print(content[:800] + "...\n")
    except Exception as e:
        print("Error fetching", u, e)
