import urllib.request
import json

url = "http://doctieuthuyet.com/get_hot_covers.php"
headers = {'User-Agent': 'Mozilla/5.0'}

try:
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
        print("Response received:")
        print(html)
except Exception as e:
    print("Error fetching from doctieuthuyet.com:", e)
    # try IP fallback
    url_ip = "http://51.79.53.190/get_hot_covers.php"
    try:
        req = urllib.request.Request(url_ip, headers=headers)
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8')
            print("Response from IP received:")
            print(html)
    except Exception as e2:
        print("Error fetching from IP:", e2)
