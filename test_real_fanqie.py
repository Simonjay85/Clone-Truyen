import requests
import re
import json

# Lấy thử cuốn "Kiếm Đạo Đệ Nhất Tiên" (ví dụ)
url = "https://fanqienovel.com/page/6803277174661413896"
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

res = requests.get(url, headers=headers)
print("Status:", res.status_code)

script_match = re.search(r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>', res.text)
if script_match:
    print("Found NEXT_DATA!")
    try:
        data = json.loads(script_match.group(1))
        # print abstract
        book_info = data['props']['pageProps']['pageData']['info']
        print("Title:", book_info['book_name'])
        print("Author:", book_info['author'])
    except Exception as e:
        print("Parse error:", e)
else:
    print("No NEXT_DATA found.")
