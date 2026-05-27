import requests

urls = [
    "https://doctieuthuyet.com/wp-content/uploads/2026/05/cover-3920-215.jpg",
    "https://doctieuthuyet.com/wp-content/uploads/2026/05/cover-3930-486.jpg",
    "https://doctieuthuyet.com/wp-content/uploads/2026/05/cover-3940-620.jpg"
]

for url in urls:
    try:
        res = requests.head(url, timeout=10)
        print(f"{url} -> Status Code: {res.status_code}")
    except Exception as e:
        print(f"Error for {url}: {e}")
