import base64
import requests
import os

WP_URL = "https://doctieuthuyet.com"
# No token provided, assuming the endpoint might be open or we'll need to handle auth if it fails.
# Based on auto_cover.py, it uses /wp-json/temply/v1/upload-cover

covers = [
    {"post_id": 1736, "path": "/home/ubuntu/covers/1736.png"},
    {"post_id": 1648, "path": "/home/ubuntu/covers/1648.png"},
    {"post_id": 1649, "path": "/home/ubuntu/covers/1649.png"},
    {"post_id": 1650, "path": "/home/ubuntu/covers/1650.png"},
    {"post_id": 1651, "path": "/home/ubuntu/covers/1651.png"},
]

for cover in covers:
    post_id = cover["post_id"]
    path = cover["path"]
    
    if not os.path.exists(path):
        print(f"File not found: {path}")
        continue
        
    with open(path, "rb") as f:
        img_b64 = base64.b64encode(f.read()).decode("utf-8")
        
    payload = {
        "post_id": post_id,
        "image_b64": img_b64
    }
    
    try:
        print(f"Uploading cover for ID {post_id}...")
        res = requests.post(f"{WP_URL}/wp-json/temply/v1/upload-cover", data=payload, timeout=60)
        print(f"Response for {post_id}: {res.text}")
    except Exception as e:
        print(f"Error uploading {post_id}: {e}")
