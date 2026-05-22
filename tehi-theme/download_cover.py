import urllib.request

def download_cover():
    url = "https://doctieuthuyet.com/wp-content/uploads/2026/05/cover-1927-upd-414.jpg"
    dest = "cover-1927-downloaded.jpg"
    print("Downloading", url)
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as response, open(dest, 'wb') as out_file:
            data = response.read()
            out_file.write(data)
        print("Downloaded cover-1927-downloaded.jpg. Size:", len(data))
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    download_cover()
