import requests

book_id = "7104043615951260686"
url = f"https://novel.snssdk.com/api/novel/book/directory/detail/v1/?book_id={book_id}"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

res = requests.get(url, headers=headers)
if res.status_code == 200:
    data = res.json()
    if data.get('code') == 0 and data.get('data'):
        print("Success! Chapter List found.")
        print(data['data']['item_list'][0:2])
    else:
        print("API failed:", data)
else:
    print("Status:", res.status_code)

