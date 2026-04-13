import requests
import time
wp_url = "https://doctieuthuyet.com/index.php"
api_endpoint = f"{wp_url.rstrip('/')}/index.php/wp-json/crawler/v1/get-task"
api_endpoint_nocache = f"{api_endpoint}?t={time.time()}"
print(f"Fetch {api_endpoint_nocache}")
res = requests.get(api_endpoint_nocache, timeout=10)
print(res.status_code)
print(res.text)
