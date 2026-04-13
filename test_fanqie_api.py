import requests

# Example chapter API pattern
# Fanqie App API sometimes isn't obfuscated
header = {'User-Agent': 'Mozilla/5.0'}
res = requests.get('https://fanqienovel.com/api/reader/full?itemId=7221087431362706489', headers=header)
print("Chapter API Status:", res.status_code)
if res.status_code == 200:
    data = res.json()
    if 'data' in data and 'content' in data['data']:
         print("Content snippet:", data['data']['content'][:200])
    else:
         print("JSON keys:", data.keys())
