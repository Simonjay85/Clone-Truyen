import requests

urls = [
    "https://doctieuthuyet.com/wp-content/themes/tehi-theme/img_data/images/no-image-cover.png",
    "https://doctieuthuyet.com/wp-content/themes/tehi-theme/img_data/images/background-repeat-2.png"
]

for url in urls:
    try:
        r = requests.get(url, timeout=10)
        print(f"URL: {url} -> Status: {r.status_code}, Length: {len(r.content)} bytes")
    except Exception as e:
        print(f"URL: {url} -> Error: {e}")
