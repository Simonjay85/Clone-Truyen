import ftplib
import requests

# Test current permalink
res = requests.get("https://doctieuthuyet.com/truyen/trieu-dinh-khong-dung-nu-nhan-ta-la-ngoai-le/")
print("Status for /truyen/... URL:", res.status_code)

# Check WP posts via API
res2 = requests.get("https://doctieuthuyet.com/wp-json/wp/v2/truyen?per_page=3", 
                    auth=("alotoinghe", "dtx4 KYEn GDDU 1haF VD2T eljY"))
print("WP API truyen status:", res2.status_code)
if res2.status_code == 200:
    posts = res2.json()
    if posts:
        print("Found posts:", len(posts))
        print("First post link:", posts[0].get('link'))
        print("First post slug:", posts[0].get('slug'))
    else:
        print("No posts found")
else:
    print("Response:", res2.text[:300])

