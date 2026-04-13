import requests

url = "https://doctieuthuyet.com/wp-content/themes/tehi-theme/assets/js/share-modal.js"
r = requests.get(url)
if r.status_code == 200:
    print("Found in assets/js!")
    print(r.text)
else:
    url = "https://doctieuthuyet.com/wp-content/themes/tehi-theme/share-modal.js"
    r = requests.get(url)
    if r.status_code == 200:
        print("Found in root!")
        print(r.text)
    else:
        print("Not found in theme either!")

