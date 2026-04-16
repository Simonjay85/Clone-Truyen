import requests
res = requests.get('https://doctieuthuyet.com/check_queue.php')
print(res.text)
