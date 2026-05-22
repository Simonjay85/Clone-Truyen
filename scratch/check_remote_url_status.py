import urllib.request

urls = [
    "https://doctieuthuyet.com/wp-content/uploads/2026/05/cover-2808-hq-383-768x768.png",
    "https://doctieuthuyet.com/wp-content/uploads/2026/05/cover-2808-hq-383.png",
    "https://doctieuthuyet.com/wp-content/uploads/2026/05/cover-1927-upd-414.jpg",
    "https://doctieuthuyet.com/wp-content/uploads/2026/05/cover-1933-hq-295.jpg",
    "https://doctieuthuyet.com/wp-content/uploads/2026/05/cover-1948-hq-733.jpg",
]

headers = {'User-Agent': 'Mozilla/5.0'}
for url in urls:
    try:
        req = urllib.request.Request(url, headers=headers, method='HEAD')
        with urllib.request.urlopen(req) as response:
            print(f"URL: {url} -> Status: {response.status}, Length: {response.getheader('Content-Length')}")
    except Exception as e:
        print(f"URL: {url} -> Error: {e}")
