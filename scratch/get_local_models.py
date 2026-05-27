import requests

try:
    res = requests.get("http://127.0.0.1:8000/v1/models", timeout=5)
    print("Status:", res.status_code)
    print("Response:", res.json())
except Exception as e:
    print("Error:", e)
