import json

with open('/Users/aaronnguyen/Downloads/har.json', 'r') as f:
    data = json.load(f)

entries = data['log']['entries']
slow_requests = sorted(entries, key=lambda x: x['time'], reverse=True)[:10]

print("Top 10 Slowest Requests:")
for entry in slow_requests:
    url = entry['request']['url']
    time = entry['time']
    print(f"{time:.2f}ms - {url}")
